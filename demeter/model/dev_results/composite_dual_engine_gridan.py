"""Analyse a composite_dual_engine grid CSV: gate-feasible region, top rows, neighbourhood stability."""
import sys
from pathlib import Path
import pandas as pd

pd.set_option("display.width", 250)
p = Path(sys.argv[1])
g = pd.read_csv(p)
cols = ["v_calm", "v_high", "hyst", "k", "out_days", "min_hold",
        "dev_1990_sharpe", "dev_1990_cagr", "dev_1990_maxdd", "dev_1990_chg_yr", "dev_1990_cash",
        "dev_1990_worst_m", "min_era_cagr", "worst_era_dd"]
cols = [c for c in cols if c in g.columns]
g = g[cols].copy()
ok = ((g.dev_1990_sharpe >= 0.425) & (g.dev_1990_maxdd >= -30.0) & (g.dev_1990_chg_yr <= 25.0)
      & (g.min_era_cagr > 0) & (g.worst_era_dd >= -40.0))
g["gate_ok"] = ok
print(f"n={len(g)}  gate-feasible (G2,G3,G4,G5) = {int(ok.sum())}")
print("\n-- top 20 by Sharpe --")
print(g.sort_values("dev_1990_sharpe", ascending=False).head(20).to_string(index=False))
if ok.any():
    print("\n-- gate-feasible rows, by Sharpe --")
    print(g[ok].sort_values("dev_1990_sharpe", ascending=False).head(30).to_string(index=False))
for v in ("v_high", "v_calm", "hyst", "min_hold", "k", "out_days"):
    if v in g.columns and g[v].nunique() > 1:
        print(f"\n-- mean/max Sharpe and mean maxDD by {v} --")
        print(g.groupby(v).agg(n=("dev_1990_sharpe", "size"), mean_sh=("dev_1990_sharpe", "mean"),
                               max_sh=("dev_1990_sharpe", "max"), mean_dd=("dev_1990_maxdd", "mean"),
                               n_ok=("gate_ok", "sum")).round(3).to_string())
