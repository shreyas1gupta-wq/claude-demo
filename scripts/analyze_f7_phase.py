"""F7a — phase-quadrant asymmetry at matched high state (pre-registered bars).

Ledger 2026-09-02. Qualifying: state expanding-percentile >= 0.8. U = boom quadrant
(high, rising; code 1); D = slowdown (falling-from-high; code 2). Every 21st qualifying
day per group; forward 63bd return + max-drawdown; 21bd secondary.
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol
from quant.ladder.phase import phase_state

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "index"

df = pd.read_csv(VAULT / "nifty50_daily_2007_2026.csv", parse_dates=["Date"])
df = df.sort_values("Date").reset_index(drop=True)
df["ret"] = df["Close"].pct_change()
df = df.dropna(subset=["ret"]).reset_index(drop=True)
r = df["ret"].values

rv_p = expanding_percentile(realized_vol(r, 21), min_obs=252)
dd_p = expanding_percentile(drawdown_depth(r), min_obs=252)
state = fast_stress_composite(rv_p, dd_p)
st_p = expanding_percentile(state, min_obs=252)
ph = phase_state(state, k_slope=21, smooth=5)

def fwd(i, h):
    seg = r[i + 1:i + 1 + h]
    if len(seg) < h:
        return None, None
    lvl = np.cumprod(1 + seg)
    peak = np.maximum.accumulate(lvl)
    return float(lvl[-1] - 1), float((1 - lvl / peak).max())

def sample(code):
    idx = [i for i in range(len(r)) if not np.isnan(st_p[i]) and st_p[i] >= 0.8
           and ph.quadrant[i] == code]
    picked, last = [], -10**9
    for i in idx:
        if i - last >= 21:
            picked.append(i)
            last = i
    return picked

for h, tag in ((63, "PRIMARY 63bd"), (21, "secondary 21bd")):
    groups = {}
    for name, code in (("U(boom)", 1), ("D(slowdown)", 2)):
        rows = [fwd(i, h) for i in sample(code)]
        rows = [x for x in rows if x[0] is not None]
        groups[name] = (np.array([x[0] for x in rows]) * 100, np.array([x[1] for x in rows]) * 100)
    (ur, ud), (dr, dd_) = groups["U(boom)"], groups["D(slowdown)"]
    print(f"\n{tag}: nU={len(ur)}, nD={len(dr)}")
    print(f"  fwd return: U median {np.median(ur):+.2f}% mean {ur.mean():+.2f}% | "
          f"D median {np.median(dr):+.2f}% mean {dr.mean():+.2f}%")
    print(f"  fwd maxDD:  U mean {ud.mean():.2f}% | D mean {dd_.mean():.2f}%")
    if len(ur) and len(dr):
        u, p = stats.mannwhitneyu(dr, ur, alternative="greater")
        print(f"  MW one-sided (D returns > U): p={p:.4f}")
        if tag.startswith("PRIMARY"):
            if min(len(ur), len(dr)) < 10:
                print("F7a VERDICT: UNDERPOWERED (a group has n<10) — no pass/fail")
            else:
                ok = (np.median(dr) > np.median(ur)) and (p < 0.10) and (dd_.mean() < ud.mean())
                print(f"F7a VERDICT: {'PASS — phase-D graduates to Challenger (reduce-only) per parent F7' if ok else 'FAIL — phase stays display-only for L2'}")
