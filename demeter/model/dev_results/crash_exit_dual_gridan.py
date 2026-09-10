"""Analyse a crash_exit_dual grid CSV: gate-passing combos, top rows, marginal means per parameter value (plateau/cliff map).
Usage: python dev_results/crash_exit_dual_gridan.py dev_results/<stem>_grid.csv [param1 param2 ...]"""
import sys
import pandas as pd
pd.set_option("display.width", 220); pd.set_option("display.max_columns", 40)
p = sys.argv[1]
g = pd.read_csv(p)
params = sys.argv[2:] or [c for c in g.columns if not c.startswith(("dev_", "min_era", "worst_era", "error"))]
if "error" in g:
    print("errors:", int(g["error"].notna().sum()))
    g = g[g["error"].isna()]
g["gate"] = (g["dev_1990_sharpe"] >= 0.4253) & (g["dev_1990_maxdd"] >= -30) & (g["dev_1990_chg_yr"] <= 25) \
            & (g["min_era_cagr"] > 0) & (g["worst_era_dd"] >= -40)
g["g2"] = g["dev_1990_sharpe"] >= 0.4253; g["g3"] = g["dev_1990_maxdd"] >= -30; g["g5"] = g["dev_1990_chg_yr"] <= 25
g["g4"] = (g["min_era_cagr"] > 0) & (g["worst_era_dd"] >= -40)
print(f"{p}: {len(g)} combos; gate-passers (G2-G5 proxies): {int(g['gate'].sum())} | G2 {int(g.g2.sum())} G3 {int(g.g3.sum())} G4 {int(g.g4.sum())} G5 {int(g.g5.sum())}")
cols = params + ["dev_1990_sharpe", "dev_1990_cagr", "dev_1990_maxdd", "dev_1990_worst_m", "dev_1990_chg_yr", "dev_1990_cash",
                 "dev_1950_sharpe", "dev_1950_maxdd", "min_era_cagr", "worst_era_dd", "gate"]
print("\nTop 25 by dev_1990 Sharpe (all):")
print(g.sort_values("dev_1990_sharpe", ascending=False)[cols].head(25).to_string(index=False, float_format=lambda x: f"{x:.3f}"))
gp = g[g.gate]
if len(gp):
    print(f"\nTop 25 gate-passers by dev_1990 Sharpe:")
    print(gp.sort_values("dev_1990_sharpe", ascending=False)[cols].head(25).to_string(index=False, float_format=lambda x: f"{x:.3f}"))
print("\nMarginal means by parameter value (Sharpe90 / maxDD90 / chg90 / Sharpe50 / worst_era_dd / n_pass):")
for k in params:
    m = g.groupby(k).agg(sh90=("dev_1990_sharpe", "mean"), dd90=("dev_1990_maxdd", "mean"), chg=("dev_1990_chg_yr", "mean"),
                         sh50=("dev_1950_sharpe", "mean"), era_dd=("worst_era_dd", "mean"), n_pass=("gate", "sum"), best=("dev_1990_sharpe", "max"))
    print(f"  {k}:\n" + m.to_string(float_format=lambda x: f"{x:.3f}"))
