"""OP-D1 — the option-state battery (measured VRP + state tables for the multi-tenor
option portfolio). Registered 2026-09-07 BEFORE this run. Prints only."""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

V = "/home/user/claude-demo/ingest/vault"
vix = pd.read_csv(f"{V}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"]).set_index("date")["close"]
nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
px = nf["Adj Close"]
r = np.log(px).diff()

# forward realized vol (annualized vol points) and forward moves
fwd_rv21 = (r.pow(2).rolling(21).sum().shift(-21) * 252 / 21).pow(0.5) * 100
fwd_mv21 = (np.log(px.shift(-21) / px)).abs()
fwd_mv5 = (np.log(px.shift(-5) / px)).abs()
fwd_r126 = np.expm1(np.log(px.shift(-126) / px))
fwd_r252 = np.expm1(np.log(px.shift(-252) / px))

j = pd.concat([vix, fwd_rv21, fwd_mv21, fwd_mv5, fwd_r126, fwd_r252, r.abs()], axis=1,
              keys=["vix", "frv", "m21", "m5", "f6m", "f12m", "absr"]).dropna(subset=["vix"])
j["vrp"] = j.vix - j.frv
j["vpct"] = expanding_percentile(j.vix.to_numpy(), min_obs=252)
val = j.dropna(subset=["vrp"])

print(f"sample: {val.index[0].date()}..{val.index[-1].date()} (n={len(val)} days; 2008 NOT in sample — stated)")
print(f"a1 mean VRP = {val.vrp.mean():+.1f} vol pts (median {val.vrp.median():+.1f}; % positive {100*(val.vrp>0).mean():.0f}%)")
print("a2 VRP by VIX quintile (expanding pct):")
for lo, hi in [(0, .2), (.2, .4), (.4, .6), (.6, .8), (.8, 1.01)]:
    d = val[(val.vpct >= lo) & (val.vpct < hi)]
    print(f"   Q{int(lo*5)+1} (VIX pct {lo:.1f}-{hi:.1f}): mean VRP {d.vrp.mean():+5.1f} | "
          f"median {d.vrp.median():+5.1f} | worst {d.vrp.min():+6.1f} | %>0 {100*(d.vrp>0).mean():3.0f}% (n={len(d)})")
w = val.vrp.idxmin()
print(f"a3 worst 21d VRP: {val.vrp.min():+.1f} pts on {w.date()} (VIX {val.vix[w]:.1f} -> fwd RV {val.frv[w]:.1f})")

# b: breach of VIX-implied 1-sigma 21d move
val2 = j.dropna(subset=["m21"])
imp21 = val2.vix / 100 * np.sqrt(21 / 252)
breach = (val2.m21 >= imp21)
print(f"\nb1 breach of VIX-implied 1σ 21d move: {100*breach.mean():.0f}% (Gaussian-neutral 32%)")
bot = val2.vpct < 0.2
top = val2.vpct >= 0.8
print(f"b2 breach FROM bottom-VIX-quintile days: {100*breach[bot].mean():.0f}% | "
      f"from top-quintile: {100*breach[top].mean():.0f}%")

# c: post-storm buyer's edge
storm = val.absr >= 0.02
under = val.frv > val.vix
print(f"\nc1 VIX understates fwd 21d RV: unconditional {100*under.mean():.0f}% | "
      f"on storm days {100*under[storm].mean():.0f}% (n_storm={int(storm.sum())})")

# d: weekly breach, trailing-vol implied
tr21 = (r.pow(2).rolling(21).sum() * 252 / 21).pow(0.5)
jj = pd.concat([tr21, fwd_mv5, r.abs()], axis=1, keys=["tr", "m5", "absr"]).dropna()
imp5 = jj.tr * np.sqrt(5 / 252)
br5 = jj.m5 >= imp5
calm_e = jj.absr < 0.02
print(f"d1 weekly 1σ breach (trailing-vol implied): all {100*br5.mean():.0f}% | "
      f"calm-day entry {100*br5[calm_e].mean():.0f}% | storm-day entry {100*br5[~calm_e].mean():.0f}%")

# e: overnight variance share
on = np.log(nf.Open / nf.Close.shift(1)).dropna()
intra = np.log(nf.Close / nf.Open).dropna()
print(f"\ne1 overnight share of daily variance: {100*on.var()/(on.var()+intra.var()):.0f}% "
      f"(overnight sd {100*on.std():.2f}% vs intraday {100*intra.std():.2f}%)")

# f: 6m/12m states
v6 = j.dropna(subset=["f6m"])
spike = v6.vpct >= 0.9
calm = v6.vpct < 0.2
print(f"\nf1 fwd 6m return: after VIX top-decile days {100*v6.f6m[spike].mean():+.1f}% "
      f"(median {100*v6.f6m[spike].median():+.1f}) vs unconditional {100*v6.f6m.mean():+.1f}% (n={int(spike.sum())})")
v12 = j.dropna(subset=["f12m"])
spike12 = v12.vpct >= 0.9
print(f"f2 fwd 12m: after top-decile {100*v12.f12m[spike12].mean():+.1f}% vs unconditional {100*v12.f12m.mean():+.1f}%")
print(f"f3 fwd 6m tail P(<= -10%): from calm (bottom quintile) {100*(v6.f6m[calm] <= -0.10).mean():.1f}% "
      f"vs unconditional {100*(v6.f6m <= -0.10).mean():.1f}%")

# g: the mix test — monthly seller proxy vs post-spike buyer proxy
m_vrp = val.vrp.resample("ME").mean()
m_spike_f6 = v6.f6m.where(v6.vpct >= 0.9).resample("ME").mean()
g = pd.concat([m_vrp, m_spike_f6], axis=1, keys=["sell", "buy"]).dropna()
print(f"\ng1 mix test: corr(monthly seller proxy, post-spike 6m buyer proxy) = "
      f"{stats.spearmanr(g.sell, g.buy)[0]:+.2f} (n={len(g)} overlap-months, flagged)")
