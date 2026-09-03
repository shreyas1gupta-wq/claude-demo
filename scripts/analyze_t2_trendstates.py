"""T2 — trend-on-states at the slow band, run exactly as registered.

Next-month NIFTY return ~ Kilian LEVEL (expanding percentile over full Kilian history)
+ TREND (sign of 12m change). NW lags 3. Bar: |t_trend| >= 2. Prior: FAILS.
"""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.ladder import expanding_percentile

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "ingest" / "vault"

k = pd.read_csv(V / "commodities/kilian_index_monthly_1973_2019.csv", parse_dates=["date"])
k = k.sort_values("date").reset_index(drop=True)
k["lvl_p"] = expanding_percentile(k.kilian_index.to_numpy(), min_obs=120)
k["trend"] = np.sign(k.kilian_index - k.kilian_index.shift(12))
k["ym"] = k.date.dt.to_period("M")

nifty = pd.read_csv(V / "index/nifty50_daily_2007_2026.csv", parse_dates=["Date"])
nm = nifty.sort_values("Date").set_index("Date")["Close"].resample("ME").last().pct_change()
ny = pd.DataFrame({"ym": nm.index.to_period("M"), "ret_next": nm.shift(-1).values})

j = k.merge(ny, on="ym").dropna(subset=["lvl_p", "trend", "ret_next"])
print(f"T2 window {j.ym.min()}..{j.ym.max()} n={len(j)}")

y = j.ret_next.to_numpy()
X = np.column_stack([np.ones(len(j)), j.lvl_p.to_numpy(), j.trend.to_numpy()])
beta, *_ = np.linalg.lstsq(X, y, rcond=None)
e = y - X @ beta
XtX_inv = np.linalg.inv(X.T @ X)
lags = 3
S = np.zeros((3, 3))
for l in range(lags + 1):
    w = 1 - l / (lags + 1)
    for t in range(l, len(e)):
        u = X[t] * e[t]
        v = X[t - l] * e[t - l]
        S += w * (np.outer(u, v) + (np.outer(v, u) if l > 0 else 0))
cov = XtX_inv @ S @ XtX_inv
se = np.sqrt(np.diag(cov))
names = ["const", "kilian level pctile", "kilian 12m trend sign"]
for i, nme in enumerate(names):
    print(f"  {nme}: beta {beta[i]*100:+.2f}%/mo, NW t = {beta[i]/se[i]:+.2f}")
t_trend = beta[2] / se[2]
print(f"T2 BAR (|t_trend| >= 2): {'PASS — doctrine cracks at the slow band' if abs(t_trend) >= 2 else 'FAIL — levels-not-directions holds at the slow band too'}")
