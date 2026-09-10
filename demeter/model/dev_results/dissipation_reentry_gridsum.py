#!/usr/bin/env python3
"""Digest a dev_harness grid CSV for dissipation_reentry: gate-proxy pass counts, marginal means per parameter,
top rows, and the rows passing all DEV gate proxies (G2 Sharpe>=0.4253, G3 maxDD>=-30, G4 min era cagr>0 & worst era dd>=-40,
G5 chg/yr<=25). Usage: python dev_results/dissipation_reentry_gridsum.py dev_results/dissipation_reentry_g1_grid.csv"""
import sys
import pandas as pd

pd.set_option("display.width", 220)
g = pd.read_csv(sys.argv[1])
params = [c for c in g.columns if c in ("rv_exit", "vix_fall", "vix_win", "vix_min", "hold_days", "stop_loss")]
print(f"rows {len(g)}; errors {g['error'].notna().sum() if 'error' in g else 0}")
g["G2"] = g["dev_1990_sharpe"] >= 0.4253
g["G3"] = g["dev_1990_maxdd"] >= -30
g["G4"] = (g["min_era_cagr"] > 0) & (g["worst_era_dd"] >= -40)
g["G5"] = g["dev_1990_chg_yr"] <= 25
g["ALL"] = g.G2 & g.G3 & g.G4 & g.G5
print("gate-proxy pass counts:", {k: int(g[k].sum()) for k in ("G2", "G3", "G4", "G5", "ALL")})
print("\ndev_1990 sharpe: min %.3f median %.3f max %.3f | maxdd: best %.1f median %.1f worst %.1f" % (
    g.dev_1990_sharpe.min(), g.dev_1990_sharpe.median(), g.dev_1990_sharpe.max(),
    g.dev_1990_maxdd.max(), g.dev_1990_maxdd.median(), g.dev_1990_maxdd.min()))
print("\nmarginal means by parameter (dev_1990 sharpe / maxdd / chg_yr / dev_1950 sharpe / worst_era_dd):")
for p in params:
    t = g.groupby(p).agg(sh90=("dev_1990_sharpe", "mean"), dd90=("dev_1990_maxdd", "mean"), chg=("dev_1990_chg_yr", "mean"),
                         sh50=("dev_1950_sharpe", "mean"), era_dd=("worst_era_dd", "mean"), n_G3=("G3", "sum"), n_ALL=("ALL", "sum"))
    print(f"-- {p}\n{t.round(3).to_string()}")
cols = params + ["dev_1990_sharpe", "dev_1990_cagr", "dev_1990_maxdd", "dev_1990_chg_yr", "dev_1990_cash", "dev_1950_sharpe", "min_era_cagr", "worst_era_dd"]
print("\ntop 15 by dev_1990 sharpe:")
print(g.sort_values("dev_1990_sharpe", ascending=False)[cols].head(15).round(3).to_string(index=False))
print("\nbest maxDD rows (top 10):")
print(g.sort_values("dev_1990_maxdd", ascending=False)[cols].head(10).round(3).to_string(index=False))
if g.ALL.any():
    print("\nrows passing ALL gate proxies:")
    print(g[g.ALL].sort_values("dev_1990_sharpe", ascending=False)[cols].round(3).to_string(index=False))
else:
    print("\nNO row passes all gate proxies.")
