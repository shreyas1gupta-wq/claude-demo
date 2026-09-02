"""F2-WF — fold-consistency of the F2-index shortlist (pre-registered; M4 harness).

Ledger 2026-09-02. Cells {trig 0.80, 1-of-2} x {calendar, decay} over 4 disjoint eras
(min_train=504bd, embargo=63bd). Exposure paths recomputed on the FULL history (the rule is
expanding/parameter-free); each era reports its own drag and any deep-episode DD delta.
"""
from pathlib import Path

import numpy as np
import pandas as pd

from quant.ladder import expanding_percentile
from quant.ladder.fast_stress import drawdown_depth, fast_stress_composite, realized_vol
from quant.validation.walkforward import evaluate_walkforward, walkforward_folds

VAULT = Path(__file__).resolve().parents[1] / "ingest" / "vault" / "index"
COST = 0.0028
DEEP = [("GFC core*", "2008-09-01", "2008-11-30"), ("COVID crash", "2020-02-20", "2020-04-30")]

df = pd.read_csv(VAULT / "nifty50_daily_2007_2026.csv", parse_dates=["Date"]).sort_values("Date")
df["ret"] = df["Close"].pct_change()
df = df.dropna(subset=["ret"]).reset_index(drop=True)
r = df["ret"].values
dates = df["Date"].values

rv_p = expanding_percentile(realized_vol(r, 21), min_obs=252)
dd_p = expanding_percentile(drawdown_depth(r), min_obs=252)
state = fast_stress_composite(rv_p, dd_p)
st_p = expanding_percentile(state, min_obs=252)

def exposure_path(family, trig=0.8):
    n = len(r)
    expo = np.ones(n)
    pos, pending, t_cut = 1.0, 0, None
    for t in range(1, n):
        if np.isnan(st_p[t - 1]):
            expo[t] = pos
            continue
        legs = int(rv_p[t - 1] >= trig) + int(dd_p[t - 1] >= trig)
        if pos == 1.0 and st_p[t - 1] >= trig and legs >= 1:
            pos, t_cut, pending = 0.5, t, 0
        elif pos < 1.0:
            full = False
            if family == "decay":
                full = st_p[t - 1] < 0.5
            else:  # calendar
                gate = st_p[t - 1] < trig
                if (t - t_cut) >= 42 and gate and pending == 0:
                    pos, pending = 0.75, t
                elif pending and (t - pending) >= 21 and gate:
                    full = True
            if full:
                pos, pending = 1.0, 0
        expo[t] = pos
    turn = np.abs(np.diff(expo, prepend=1.0))
    return expo * r - turn * COST

def dd_of(x):
    lvl = np.cumprod(1 + x)
    return float((1 - lvl / np.maximum.accumulate(lvl)).max())

folds = walkforward_folds(len(r), n_folds=4, min_train=504, embargo=63)
for family in ("calendar", "decay"):
    pret = exposure_path(family)
    def metric(f):
        seg_r, seg_p = r[f.test_start:f.test_end], pret[f.test_start:f.test_end]
        yrs = len(seg_r) / 252
        drag = ((np.prod(1 + seg_r)) ** (1 / yrs) - (np.prod(1 + seg_p)) ** (1 / yrs)) * 100
        deep_note = ""
        for name, a, b in DEEP:
            i = np.where((dates >= np.datetime64(a)) & (dates <= np.datetime64(b)))[0]
            if len(i) and f.test_start <= i[0] < f.test_end:
                j0, j1 = i[0] - f.test_start, i[-1] - f.test_start
                deep_note = f"{name}: DD {dd_of(seg_r[j0:j1+1])*100:.0f}%->{dd_of(seg_p[j0:j1+1])*100:.0f}%"
        return {"drag_pp": drag, "deep": deep_note}
    res = evaluate_walkforward(folds, metric)
    n_ok = sum(1 for x in res if x["drag_pp"] <= 2.0)
    print(f"\n{family}:")
    for x in res:
        era = f"{str(dates[x['test_start']])[:10]}..{str(dates[x['test_end']-1])[:10]}"
        print(f"  era {era}: drag {x['drag_pp']:+5.2f}pp/yr {'OK ' if x['drag_pp'] <= 2.0 else 'OVER'} {x['deep']}")
    print(f"  -> {n_ok}/4 eras within budget; BAR >=3/4: {'PASS — seat kept' if n_ok >= 3 else 'FAIL — seat lost'}")
