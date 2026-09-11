"""Fast dev_1990-only grid over the surviving region + a neighbourhood ('plateau') score, so the frozen
point is the centre of a flat area rather than a peak. DEV window only (E.load_market(end=2012-06-30))."""
from __future__ import annotations
import importlib.util, itertools, json, sys
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
GRID = json.loads(Path(sys.argv[1]).read_text())
fixed = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
keys = list(GRID)
rows = []
for c in itertools.product(*[GRID[k] for k in keys]):
    p = dict(M.DEFAULT_PARAMS); p.update(fixed); p.update(dict(zip(keys, c)))
    lev = M.signal(df, **p).reindex(df.index)
    m = E.run(df, lev, cost_bps=COST, financing_spread_bps=FIN, start="1990-01-01", end="2012-06-30").metrics()
    rows.append(dict(**{k: p[k] for k in keys}, sharpe=m["sharpe"], maxdd=m["max_drawdown_pct"],
                     cagr=m["annualized_return_pct"], chg_yr=m["position_changes_per_year"],
                     cash=m["pct_days_cash"], lev_inv=m["avg_leverage_when_invested"],
                     up_cap=m["up_capture_pct"], worst_m=m["worst_month_pct"]))
g = pd.DataFrame(rows)
idx = {k: {v: i for i, v in enumerate(GRID[k])} for k in keys}
pos = np.array([[idx[k][r[k]] for k in keys] for _, r in g.iterrows()])
nb_sh, nb_dd, nb_n = [], [], []
for i in range(len(g)):
    d = np.abs(pos - pos[i]).sum(axis=1)          # 1-step Manhattan neighbourhood (self + immediate neighbours)
    sel = d <= 1
    nb_sh.append(g.sharpe[sel].mean()); nb_dd.append(g.maxdd[sel].max()); nb_n.append(int(sel.sum()))
g["nb_sharpe"] = nb_sh; g["nb_worst_dd"] = nb_dd; g["nb_n"] = nb_n
g["feasible"] = (g.sharpe >= 0.425) & (g.maxdd >= -30.0) & (g.chg_yr <= 25.0)
g.to_csv(HERE / "dev_results" / f"{sys.argv[2]}.csv", index=False, float_format="%.4f")
pd.set_option("display.width", 250)
print(f"n={len(g)} feasible={int(g.feasible.sum())}")
print("\n-- top 15 by NEIGHBOURHOOD mean Sharpe (plateau centres), feasible only --")
print(g[g.feasible].sort_values("nb_sharpe", ascending=False).head(15).to_string(index=False))
print("\n-- top 8 by raw Sharpe (peaks, for contrast) --")
print(g.sort_values("sharpe", ascending=False).head(8).to_string(index=False))
