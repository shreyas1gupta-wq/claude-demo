"""Summarise a harness grid CSV: Sharpe surface shares, marginals, cliffs. Usage: gridsum.py <csv> [param ...]"""
import sys
import pandas as pd, numpy as np
g = pd.read_csv(sys.argv[1])
params = sys.argv[2:]
s = g["dev_1990_sharpe"]
print(f"{sys.argv[1]}: n={len(g)} errors={g['error'].notna().sum() if 'error' in g else 0}")
print(f"Sharpe: min {s.min():.3f} p10 {s.quantile(.1):.3f} median {s.median():.3f} p90 {s.quantile(.9):.3f} max {s.max():.3f}")
print(f"share > 0.425 {(s > 0.425).mean():.2%} | > 0.50 {(s > 0.5).mean():.2%} | > 0.55 {(s > 0.55).mean():.2%} | > 0.60 {(s > 0.6).mean():.2%}")
print(f"maxDD better than -25%: {(g['dev_1990_maxdd'] > -25).mean():.2%}; chg/yr <= 25: {(g['dev_1990_chg_yr'] <= 25).mean():.2%}; "
      f"all-gate-proxy (Sh>=.425 & DD>=-30 & chg<=25 & worst_era_dd>=-40 & min_era_cagr>0): "
      f"{((s >= .425) & (g['dev_1990_maxdd'] >= -30) & (g['dev_1990_chg_yr'] <= 25) & (g['worst_era_dd'] >= -40) & (g['min_era_cagr'] > 0)).mean():.2%}")
for p in params:
    t = g.groupby(p)["dev_1990_sharpe"].agg(["mean", "min", "max", lambda x: (x > 0.5).mean()])
    t.columns = ["mean", "min", "max", "share>0.5"]
    dd = g.groupby(p)["dev_1990_maxdd"].mean(); ch = g.groupby(p)["dev_1990_chg_yr"].mean(); cs = g.groupby(p)["dev_1990_cash"].mean()
    t["avg_dd"] = dd; t["avg_chg"] = ch; t["avg_cash"] = cs
    print(f"-- marginal by {p}\n{t.round(3).to_string()}")
print("-- worst 8 cells")
print(g.nsmallest(8, "dev_1990_sharpe")[params + ["dev_1990_sharpe", "dev_1990_maxdd", "dev_1990_chg_yr", "dev_1990_cash"]].round(3).to_string(index=False))
print("-- best 8 cells")
print(g.nlargest(8, "dev_1990_sharpe")[params + ["dev_1990_sharpe", "dev_1990_maxdd", "dev_1990_chg_yr", "dev_1990_cash"]].round(3).to_string(index=False))
