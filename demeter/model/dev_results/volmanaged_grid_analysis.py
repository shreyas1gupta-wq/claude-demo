"""Analyse dev_results/volmanaged_grid.csv (DEV ONLY): gate pass counts, axis marginals, trade count vs band,
neighbourhood plateau score. Usage: python dev_results/volmanaged_grid_analysis.py [grid.csv]"""
import sys
from pathlib import Path
import numpy as np, pandas as pd
HERE = Path(__file__).resolve().parents[1]
path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "dev_results" / "volmanaged_grid.csv"
g = pd.read_csv(path)
P = ["target_vol", "hl", "long_mult", "band_up", "band_dn"]
g["G2"] = g["dev_1990_sharpe"] >= 0.4253
g["G3"] = g["dev_1990_maxdd"] >= -30
g["G4"] = (g["min_era_cagr"] > 0) & (g["worst_era_dd"] >= -40)
g["G5"] = g["dev_1990_chg_yr"] <= 25
g["ALL"] = g.G2 & g.G3 & g.G4 & g.G5
print(f"n={len(g)}  G2 {g.G2.mean():.0%}  G3 {g.G3.mean():.0%}  G4 {g.G4.mean():.0%}  G5 {g.G5.mean():.0%}  ALL {g.ALL.mean():.0%} ({g.ALL.sum()})")
print(f"dev_1990 sharpe: min {g.dev_1990_sharpe.min():.3f} q25 {g.dev_1990_sharpe.quantile(.25):.3f} med {g.dev_1990_sharpe.median():.3f} q75 {g.dev_1990_sharpe.quantile(.75):.3f} max {g.dev_1990_sharpe.max():.3f}")
print(f"dev_1950 sharpe: min {g.dev_1950_sharpe.min():.3f} med {g.dev_1950_sharpe.median():.3f} max {g.dev_1950_sharpe.max():.3f}   (B&H 0.47)")
for p in P:
    t = g.groupby(p).agg(sh90=("dev_1990_sharpe", "mean"), sh90_min=("dev_1990_sharpe", "min"), dd90=("dev_1990_maxdd", "mean"),
                         chg=("dev_1990_chg_yr", "mean"), sh50=("dev_1950_sharpe", "mean"), eradd=("worst_era_dd", "mean"),
                         eradd_min=("worst_era_dd", "min"), passALL=("ALL", "mean"), passG4=("G4", "mean")).round(3)
    print(f"\n-- marginal by {p}:\n{t.to_string()}")
print("\n-- trade count vs band (mean chg/yr, dev_1990):")
print(g.pivot_table(index="band_up", columns="band_dn", values="dev_1990_chg_yr", aggfunc="mean").round(1).to_string())
print("\n-- Sharpe vs band (mean dev_1990):")
print(g.pivot_table(index="band_up", columns="band_dn", values="dev_1990_sharpe", aggfunc="mean").round(3).to_string())
print("\n-- Sharpe: target_vol x hl (mean over other axes):")
print(g.pivot_table(index="target_vol", columns="hl", values="dev_1990_sharpe", aggfunc="mean").round(3).to_string())
print("\n-- worst era DD: target_vol x long_mult (mean):")
print(g.pivot_table(index="target_vol", columns="long_mult", values="worst_era_dd", aggfunc="mean").round(1).to_string())

# neighbourhood plateau score: for each cell, the set of cells differing in exactly one axis by one grid step
vals = {p: sorted(g[p].unique()) for p in P}
idx = {tuple(r[p] for p in P): i for i, r in g.iterrows()}
def neighbours(key):
    out = []
    for j, p in enumerate(P):
        k = vals[p].index(key[j])
        for kk in (k - 1, k + 1):
            if 0 <= kk < len(vals[p]):
                nk = list(key); nk[j] = vals[p][kk]; nk = tuple(nk)
                if nk in idx: out.append(idx[nk])
    return out
rows = []
for key, i in idx.items():
    nb = neighbours(key); b = g.loc[i, "dev_1990_sharpe"]
    if not nb: continue
    n = g.loc[nb]
    within = (abs(n.dev_1990_sharpe - b) <= 0.25 * abs(b)).mean()
    nb_all = n.ALL.mean()
    rows.append({**dict(zip(P, key)), "sharpe": b, "dd": g.loc[i, "dev_1990_maxdd"], "chg": g.loc[i, "dev_1990_chg_yr"],
                 "eradd": g.loc[i, "worst_era_dd"], "sh50": g.loc[i, "dev_1950_sharpe"], "ALL": g.loc[i, "ALL"],
                 "n_nb": len(nb), "nb_within25": within, "nb_passALL": nb_all, "nb_min_sharpe": n.dev_1990_sharpe.min(),
                 "nb_worst_eradd": n.worst_era_dd.min()})
s = pd.DataFrame(rows)
s["score"] = s.nb_passALL + s.nb_within25 + 0.5 * s.ALL
print("\n-- plateau candidates: cells passing ALL whose neighbours also pass ALL (sorted by nb_passALL, nb_min_sharpe):")
c = s[s.ALL].sort_values(["nb_passALL", "nb_min_sharpe"], ascending=False)
print(c.head(25).round(3).to_string(index=False))
print("\n-- cells passing ALL with nb_passALL == 1.0:", int((c.nb_passALL >= 0.999).sum()))
c.to_csv(HERE / "dev_results" / "volmanaged_grid_plateau.csv", index=False, float_format="%.4f")
