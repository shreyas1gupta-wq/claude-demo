"""H67a/H68a — the phase file's last gates at index resolution (pre-registered).

Ledger 2026-09-02. Same construction as F7a. H67a: dead-band grid calibration
(measurement). H68a: age effect at high state (prior: fails).
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol
from quant.ladder.phase import phase_state

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "index"

df = pd.read_csv(VAULT / "nifty50_daily_2007_2026.csv", parse_dates=["Date"]).sort_values("Date")
r = df["Close"].pct_change().dropna().values
rv_p = expanding_percentile(realized_vol(r, 21), min_obs=252)
dd_p = expanding_percentile(drawdown_depth(r), min_obs=252)
state = fast_stress_composite(rv_p, dd_p)
st_p = expanding_percentile(state, min_obs=252)
yrs = (df["Date"].iloc[-1] - df["Date"].iloc[1]) / pd.Timedelta(days=365)

print("H67a — dead-band grid calibration (display hysteresis):")
for db in (0.15, 0.25, 0.35):
    ph = phase_state(state, k_slope=21, smooth=5, deadband_pct=db)
    d = ph.direction
    ok = ~np.isnan(d)
    flips = int(np.nansum(np.abs(np.diff(d[ok])) > 0))
    runs = []
    cur = 1
    dv = d[ok]
    for i in range(1, len(dv)):
        if dv[i] == dv[i - 1]:
            cur += 1
        else:
            runs.append(cur); cur = 1
    runs.append(cur)
    print(f"  dead-band {db:.2f}: {flips/float(yrs):5.1f} flips/yr, median run {np.median(runs):4.0f}bd, "
          f"mean run {np.mean(runs):5.0f}bd")

print("\nH68a — age effect at high state (prior: FAILS):")
ph = phase_state(state, k_slope=21, smooth=5, deadband_pct=0.25)
def sample(cond):
    idx = [i for i in range(len(r)) if not np.isnan(st_p[i]) and st_p[i] >= 0.8 and cond(i)]
    picked, last = [], -10**9
    for i in idx:
        if i - last >= 21:
            picked.append(i); last = i
    return picked
def fwd63(i):
    seg = r[i + 1:i + 64]
    return float(np.prod(1 + seg) - 1) * 100 if len(seg) == 63 else None
young = [x for x in (fwd63(i) for i in sample(lambda i: ph.age[i] <= 21)) if x is not None]
old = [x for x in (fwd63(i) for i in sample(lambda i: ph.age[i] > 21)) if x is not None]
print(f"  young (age<=21bd): n={len(young)}, median fwd63 {np.median(young):+.2f}%")
print(f"  old   (age> 21bd): n={len(old)}, median fwd63 {np.median(old):+.2f}%")
if min(len(young), len(old)) >= 10:
    u, p = stats.mannwhitneyu(young, old, alternative="two-sided")
    diff = abs(np.median(young) - np.median(old))
    ok = diff > 2.0 and p < 0.10
    print(f"  |median diff| {diff:.2f}pp, MW two-sided p={p:.3f} -> "
          f"{'AGE EFFECT (bar met)' if ok else 'NO age effect — prior lands; age stays a caption'}")
else:
    print("  UNDERPOWERED (a group has n<10) — no verdict")
