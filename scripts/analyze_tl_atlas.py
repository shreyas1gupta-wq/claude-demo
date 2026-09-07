"""TL-D1 — the return-distribution atlas (tails, sigma, clustering, horizons).

Registered 2026-09-07 BEFORE this run. Prints + writes research/notes/tl_atlas_stats.json
for the artifact charts. No decisions here.
"""
import json
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
ROOT = "/home/user/claude-demo"
OUT = {}

# ---------- NIFTY daily ----------
nf = pd.read_csv(f"{ROOT}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                 parse_dates=["Date"]).set_index("Date").sort_index()
r = nf["Adj Close"].pct_change().dropna()
sd, mu = r.std(), r.mean()
z = (r - mu) / sd
n = len(r)
print(f"NIFTY daily {r.index[0].date()}..{r.index[-1].date()}: n={n}, mean {100*mu:.3f}%/d, "
      f"sd {100*sd:.2f}%/d (ann vol {100*sd*np.sqrt(252):.1f}%)")
print("\nc1 SIGMA TABLE (full-sample sigma):")
rows = []
for k in (1, 2, 3, 4, 6):
    obs_lo, obs_hi = int((z <= -k).sum()), int((z >= k).sum())
    gauss = 2 * stats.norm.sf(k) * n
    rows.append(dict(k=k, lo=obs_lo, hi=obs_hi, gauss=gauss))
    print(f"  |z|>={k}: observed {obs_lo + obs_hi:4d} ({obs_lo} down / {obs_hi} up) vs "
          f"Gaussian {gauss:8.2f}  -> {((obs_lo+obs_hi)/gauss if gauss>0 else np.inf):8.1f}x")
OUT["sigma_table"] = rows
print(f"  1-sigma move = {100*sd:.2f}% | 2s {200*sd:.2f}% | 3s {300*sd:.2f}% | 6s {600*sd:.2f}%")
ek, sk = float(stats.kurtosis(r)), float(stats.skew(r))
print(f"c2 shape: excess kurtosis {ek:.1f}, skew {sk:+.2f}")
OUT["daily"] = dict(n=n, mu=mu, sd=sd, ek=ek, skew=sk,
                    hist=np.histogram(z, bins=np.arange(-14, 14.5, 0.5))[0].tolist())

print("\nc3 CLUSTERING:")
ac_r = [float(r.autocorr(l)) for l in range(1, 31)]
ac_abs = [float(r.abs().autocorr(l)) for l in range(1, 31)]
pos30 = all(a > 0 for a in ac_abs)
vol21 = r.rolling(21).std() * np.sqrt(252)
phi = float(vol21.dropna().autocorr(1))
hl = np.log(0.5) / np.log(phi)
print(f"  autocorr(r) lag1 {ac_r[0]:+.3f} (signal ~none) | autocorr(|r|) lag1 {ac_abs[0]:+.2f}, "
      f"lag5 {ac_abs[4]:+.2f}, lag30 {ac_abs[29]:+.2f}; all positive thru 30: {pos30}")
print(f"  rolling-21d vol AR(1) phi {phi:.3f} -> half-life {hl:.0f} trading days")
q = vol21.dropna().quantile([.05, .25, .5, .75, .95, 1.0])
print(f"  21d ann vol distribution: p5 {100*q[.05]:.1f}% | median {100*q[.5]:.1f}% | "
      f"p95 {100*q[.95]:.1f}% | max {100*q[1.0]:.1f}% (a {q[1.0]/q[.5]:.1f}x regime range)")
OUT["clustering"] = dict(ac_abs=ac_abs, ac_r=ac_r, phi=phi, hl=hl,
                         vol_hist=np.histogram(100*vol21.dropna(),
                                               bins=np.arange(4, 92, 4))[0].tolist(),
                         vol_series=[[str(d.date()), round(100*v, 1)]
                                     for d, v in vol21.dropna().iloc[::5].items()])

vix = pd.read_csv(f"{ROOT}/ingest/vault/globalvol/cboe_vix_daily_1990_2026.csv",
                  parse_dates=["DATE"]).set_index("DATE").sort_index()
v = vix["CLOSE"].dropna()
print(f"\nc4 VIX 1990-2026 (n={len(v)}): median {v.median():.1f}, mean {v.mean():.1f}, "
      f"p95 {v.quantile(.95):.1f}, max {v.max():.1f} ({v.idxmax().date()}); "
      f"mean>median: {v.mean() > v.median()}")
OUT["vix"] = dict(median=float(v.median()), mean=float(v.mean()), mx=float(v.max()),
                  hist=np.histogram(v, bins=np.arange(8, 84, 3))[0].tolist())

# ---------- US 155y (Shiller real TR) ----------
sh = pd.read_csv(f"{ROOT}/ingest/vault/us_index/sp500_shiller_monthly_1871.csv",
                 parse_dates=["Date"]).set_index("Date").sort_index()
sh = sh[sh["Real Price"] > 0]  # mirror's CPI/real columns stop 2023-09; run note in ledger
rtr = ((sh["Real Price"] + sh["Real Dividend"] / 12) / sh["Real Price"].shift(1)).dropna() - 1
lr = np.log1p(rtr)
jst = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
ju = jst[jst.country == "USA"].set_index("year")
jreq = ((1 + ju.eq_tr) / (1 + ju.cpi.pct_change()) - 1).dropna()

wk = np.log1p(r).resample("W").sum().pipe(np.expm1)
mo = np.log1p(r).resample("ME").sum().pipe(np.expm1)
print("\nc5 KURTOSIS LADDER (excess kurtosis):")
lad = [("NIFTY daily", r), ("NIFTY weekly", wk), ("NIFTY monthly", mo),
       ("US monthly real (avg-flag)", rtr), ("US annual real (JST)", jreq)]
OUT["ladder"] = []
for lab, s in lad:
    e = float(stats.kurtosis(s.dropna()))
    OUT["ladder"].append([lab, round(e, 2), round(float(stats.skew(s.dropna())), 2)])
    print(f"  {lab:28}: {e:6.1f} (skew {stats.skew(s.dropna()):+.2f}, n={len(s.dropna())})")

print("\nc6 US HORIZON TABLE (Shiller real total return, rolling, overlap flagged):")
OUT["horizons"] = []
print(f"  {'horizon':>8} {'mean':>7} {'median':>7} {'sd':>6} {'worst':>7} {'best':>7} {'%>0':>5} {'n':>6}")
for lab, months in [("1m", 1), ("1y", 12), ("3y", 36), ("5y", 60), ("10y", 120), ("20y", 240)]:
    w = lr.rolling(months).sum().dropna()
    cagr = np.expm1(w * (12 / months)) if months >= 12 else np.expm1(w)
    OUT["horizons"].append(dict(lab=lab, mean=float(cagr.mean()), med=float(cagr.median()),
                                sd=float(cagr.std()), worst=float(cagr.min()),
                                best=float(cagr.max()), pos=float((cagr > 0).mean()),
                                n=int(len(cagr)),
                                hist=np.histogram(100*cagr, bins=30)[0].tolist(),
                                edges=np.round(np.histogram(100*cagr, bins=30)[1], 1).tolist()))
    u = "%" if months < 12 else "%/yr"
    print(f"  {lab:>8} {100*cagr.mean():>6.1f} {100*cagr.median():>6.1f} {100*cagr.std():>6.1f} "
          f"{100*cagr.min():>6.1f} {100*cagr.max():>6.1f} {100*(cagr>0).mean():>4.0f}% {len(cagr):>6}  ({u})")
w20 = np.expm1(pd.Series(np.log1p(jreq)).rolling(20).sum() / 20)
print(f"  JST annual cross-check: worst 20y real CAGR {100*w20.min():+.1f}%/yr "
      f"(vs Shiller {100*OUT['horizons'][-1]['worst']:+.1f}%)")

print("\nc7 NIFTY weekly/monthly (nominal): weekly sd {:.1f}%, worst {:+.1f}% | monthly sd {:.1f}%, worst {:+.1f}%".format(
    100*wk.std(), 100*wk.min(), 100*mo.std(), 100*mo.min()))

print("\nc8 EVENT LISTS:")
print("  worst 10 NIFTY days:", [(str(d.date()), f"{100*x:.1f}%") for d, x in r.nsmallest(10).items()])
print("  best 10 NIFTY days: ", [(str(d.date()), f"{100*x:.1f}%") for d, x in r.nlargest(10).items()])
OUT["events"] = dict(worst=[[str(d.date()), round(100*x, 1)] for d, x in r.nsmallest(10).items()],
                     best=[[str(d.date()), round(100*x, 1)] for d, x in r.nlargest(10).items()])
mo_us = lr.groupby(pd.Grouper(freq="YE")).sum().pipe(np.expm1)
print("  worst US real years:", [(d.year, f"{100*x:.0f}%") for d, x in mo_us.nsmallest(5).items()])
print("  best US real years: ", [(d.year, f"{100*x:.0f}%") for d, x in mo_us.nlargest(5).items()])
idx = lr.cumsum()
dd = idx - idx.cummax()
print(f"  deepest US real TR drawdown: {100*(1-np.exp(dd.min())):.0f}% at {dd.idxmin().date()}")
OUT["us_dd"] = [[str(d.date()), round(100*(1-np.exp(x)), 1)] for d, x in dd.iloc[::4].items()]
OUT["us_years"] = dict(worst=[[int(d.year), round(100*x)] for d, x in mo_us.nsmallest(5).items()],
                       best=[[int(d.year), round(100*x)] for d, x in mo_us.nlargest(5).items()])

with open(f"{ROOT}/research/notes/tl_atlas_stats.json", "w") as f:
    json.dump(OUT, f)
print("\nstats json written")
