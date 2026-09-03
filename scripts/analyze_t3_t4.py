"""T3 (dual momentum NIFTY/INR-gold) + T4 (India low-vol quintile) — run as registered."""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew

from quant.stats.dsr import census_n, deflated_sharpe_ratio
from quant.stats.bootstrap import max_drawdown

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "ingest" / "vault"
COST = 0.0028


def sharpe(x, per=12):
    return float(np.mean(x) / np.std(x, ddof=1) * np.sqrt(per))


def nw_t(x, lags=3):
    x = np.asarray(x, float)
    n, m = len(x), np.mean(x)
    e = x - m
    s = e @ e / n
    for l in range(1, lags + 1):
        s += 2 * (1 - l / (lags + 1)) * (e[l:] @ e[:-l]) / n
    return m, m / np.sqrt(s / n)


# ---------------- T3 ----------------
nifty = pd.read_csv(V / "index/nifty50_daily_2007_2026.csv", parse_dates=["Date"])
nm = nifty.sort_values("Date").set_index("Date")["Close"].resample("ME").last()
gold = pd.read_csv(V / "commodities/gold_monthly_1833_2026.csv")
g = pd.Series(gold.Price.values, index=pd.PeriodIndex(gold.Date, freq="M").to_timestamp("M"))
fx = pd.read_csv(V / "fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"])
f = pd.Series(fx.INR_per_USD.values, index=fx.Date.dt.to_period("M").dt.to_timestamp("M"))
ginr = (g * f).dropna()
px = pd.concat([nm, ginr], axis=1, keys=["nifty", "gold"], sort=True).dropna()
rets = px.pct_change().dropna()
print(f"T3 joint span {rets.index.min():%Y-%m}..{rets.index.max():%Y-%m} n={len(rets)} months")

r5050 = 0.5 * rets.nifty + 0.5 * rets.gold
bench = {"nifty": sharpe(rets.nifty), "gold": sharpe(rets.gold), "50/50": sharpe(r5050)}
print(f"  Sharpe: nifty {bench['nifty']:.2f} | gold(INR) {bench['gold']:.2f} | 50/50 {bench['50/50']:.2f}; "
      f"maxDD 50/50 {max_drawdown(r5050.to_numpy())*100:.0f}%")

for k in (3, 12):
    mom = px.pct_change(k)
    pick = (mom.nifty > mom.gold).shift(1)  # decide at month-end t-1, hold month t
    valid = pick.notna() & mom.shift(1).notna().all(axis=1)
    pick = pick[valid]
    rr = rets[valid]
    strat = np.where(pick, rr.nifty, rr.gold)
    switches = np.abs(np.diff(pick.astype(float), prepend=pick.iloc[0]))
    net = strat - switches * COST
    sr = sharpe(net)
    dsr = deflated_sharpe_ratio(sr / np.sqrt(12), len(net), float(skew(net)),
                                float(kurtosis(net, fisher=False)),
                                n_trials=census_n() + 2, sr_var_across_trials=1e-4)
    ok = sr > max(bench.values()) and dsr > 0.95
    print(f"  T3 k={k}: net Sharpe {sr:.2f} (bars: > all of {max(bench.values()):.2f} and DSR>0.95 "
          f"[{dsr:.3f}]) -> {'SURVIVES' if ok else 'FAIL'} | maxDD {max_drawdown(net)*100:.0f}% "
          f"vs 50/50 {max_drawdown(r5050[valid].to_numpy())*100:.0f}% | switches/yr "
          f"{switches.sum()/ (len(net)/12):.1f}")

# ---------------- T4 ----------------
pxp = pd.read_csv(V / "panel/n500_adjclose_2012_2022.csv.gz", index_col=0, parse_dates=True)
r = pxp.pct_change()
vol252 = r.rolling(252).std()
me = r.index.to_series().groupby(r.index.to_period("M")).max()  # month-end trading days
low_r, uni_r = [], []
months = sorted(set(r.index.to_period("M")))
for i in range(12, len(months) - 0):
    m = months[i]
    prev_end = me[months[i - 1]]
    v = vol252.loc[prev_end].dropna()
    if len(v) < 100:
        continue
    q = v.quantile(0.2)
    low_names = v[v <= q].index
    mask = r.index.to_period("M") == m
    rm = r.loc[mask]
    low_r.append(float(((1 + rm[low_names]).prod() - 1).mean()))
    uni_r.append(float(((1 + rm[v.index]).prod() - 1).mean()))
low_r, uni_r = np.array(low_r), np.array(uni_r)
print(f"\nT4: {len(low_r)} months, {months[12]}..{months[len(low_r)+11]}")
sr_low, sr_uni = sharpe(low_r), sharpe(uni_r)
X = np.column_stack([np.ones_like(uni_r), uni_r])
beta, *_ = np.linalg.lstsq(X, low_r, rcond=None)
resid = low_r - X @ beta
_, t_alpha = nw_t(resid + beta[0])  # NW t on alpha via residual+alpha series mean
print(f"  low-vol quintile Sharpe {sr_low:.2f} vs universe {sr_uni:.2f}; "
      f"CAPM beta {beta[1]:.2f}, alpha {beta[0]*12*100:+.2f}%/yr (NW t={t_alpha:.2f})")
present = (sr_low > sr_uni) and (t_alpha >= 2)
print(f"  T4 BAR (Sharpe> AND alpha t>=2): {'PASS (decisive-leaning per one-way)' if present else 'FAIL (inconclusive per one-way)'}")
print(f"  maxDD low-vol {max_drawdown(low_r)*100:.0f}% vs universe {max_drawdown(uni_r)*100:.0f}%")
