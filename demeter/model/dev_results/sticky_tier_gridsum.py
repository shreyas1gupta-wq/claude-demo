"""Summarise a sticky_tier grid CSV: top rows, marginal means per parameter, gate-feasible region. Usage: gridsum.py <csv> [groupcols]"""
import sys
import pandas as pd
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40)
g = pd.read_csv(sys.argv[1])
if "error" in g:
    print("errors:", g["error"].notna().sum()); g = g[g["error"].isna()]
cols = [c for c in ["v_lo", "gap", "target_vol", "h", "hl", "long_mult", "M", "P", "floor", "p_dn", "weekly_up"] if c in g]
show = cols + ["dev_1990_sharpe", "dev_1990_cagr", "dev_1990_maxdd", "dev_1990_chg_yr", "dev_1990_cash",
               "dev_1950_sharpe", "dev_1950_maxdd", "dev_1950_chg_yr", "min_era_cagr", "worst_era_dd"]
g["gates_ok"] = (g.dev_1990_sharpe >= 0.425) & (g.dev_1990_maxdd >= -30) & (g.dev_1990_chg_yr <= 25) & (g.min_era_cagr > 0) & (g.worst_era_dd >= -40)
print(f"n={len(g)}  gate-feasible (G2-G5 proxies)={g.gates_ok.sum()}")
print("\nTOP 15 by dev_1990 Sharpe:")
print(g.sort_values("dev_1990_sharpe", ascending=False)[show].head(15).to_string(index=False))
print("\nTOP 10 gate-feasible by dev_1990 Sharpe:")
print(g[g.gates_ok].sort_values("dev_1990_sharpe", ascending=False)[show].head(10).to_string(index=False))
for c in cols:
    print(f"\nmarginal by {c}:")
    print(g.groupby(c).agg(sh90=("dev_1990_sharpe", "mean"), sh90_max=("dev_1990_sharpe", "max"), cagr90=("dev_1990_cagr", "mean"),
                           dd90=("dev_1990_maxdd", "mean"), chg=("dev_1990_chg_yr", "mean"), cash=("dev_1990_cash", "mean"),
                           sh50=("dev_1950_sharpe", "mean"), era_dd=("worst_era_dd", "mean"), ok=("gates_ok", "mean")).round(3).to_string())
