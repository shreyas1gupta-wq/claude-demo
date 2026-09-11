"""One-parameter-at-a-time sweeps around a base point (DEV window only): is the region a plateau or a ridge?"""
from __future__ import annotations
import importlib.util, json, sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402

spec = importlib.util.spec_from_file_location("cde", HERE / "signals" / "composite_dual_engine.py")
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

COST, FIN = 3.0, 60.0
df = E.load_market(end="2012-06-30")
base = json.loads(sys.argv[1])
AX = {
    "v_calm": [13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 19.0, 20.0],
    "v_high": [19.0, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 25.0, 26.0, 28.0],
    "hyst": [0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20],
    "k": [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
    "out_days": [5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 20, 25],
    "min_hold": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 20],
}


def run(p):
    lev = M.signal(df, **p).reindex(df.index)
    m = E.run(df, lev, cost_bps=COST, financing_spread_bps=FIN, start="1990-01-01", end="2012-06-30").metrics()
    return m["sharpe"], m["max_drawdown_pct"], m["position_changes_per_year"], m["pct_days_cash"]


b = run(base)
print(f"base {base}: Sharpe {b[0]:.4f} DD {b[1]:.2f}% chg/yr {b[2]:.2f} cash {b[3]:.1f}%")
rows = []
for ax, vals in AX.items():
    line = []
    for v in vals:
        p = dict(base); p[ax] = v
        s, dd, c, cash = run(p)
        line.append(f"{v}:{s:.3f}/{dd:.0f}")
        rows.append(dict(axis=ax, value=v, sharpe=s, maxdd=dd, chg_yr=c, cash=cash))
    print(f"  {ax:9s} " + "  ".join(line))
pd.DataFrame(rows).to_csv(HERE / "dev_results" / f"{sys.argv[2]}.csv", index=False, float_format="%.4f")
