"""GDP-D4 — within-country growth -> future-return grid (k-trailing x h-forward).

Registered 2026-09-07 BEFORE this run. Prints only.
"""
import numpy as np
import pandas as pd
from scipy import stats

ROOT = "/home/user/claude-demo"
COMBOS = [(5, 5), (10, 5), (10, 10), (20, 10), (20, 20)]

df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "rgdpmad"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1
df["g"] = np.log(df.rgdpmad).groupby(df.country).diff()

frames = []
for c, g in df.groupby("country"):
    g = g[(g.year >= 1950) & (g.year <= 2020)].set_index("year").copy()
    for k in {k for k, _ in COMBOS}:
        g[f"tg{k}"] = g.g.rolling(k).mean()
    for h in {h for _, h in COMBOS}:
        g[f"fw{h}"] = np.log1p(g.req).rolling(h).mean().shift(-h).apply(np.expm1)
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)

print("GDP-D4 — trailing k-yr GDP/cap growth -> next h-yr real equity CAGR")
print(f"{'combo':>8} {'median own-country rho':>24} {'n countries':>12} {'pooled rho':>11} {'n pooled':>9}")
for k, h in COMBOS:
    per = []
    for c, g in p.groupby("country"):
        j = g[[f"tg{k}", f"fw{h}"]].dropna()
        if len(j) >= 25:
            per.append(stats.spearmanr(j.iloc[:, 0], j.iloc[:, 1])[0])
    jp = p[[f"tg{k}", f"fw{h}"]].dropna()
    pool = stats.spearmanr(jp.iloc[:, 0], jp.iloc[:, 1])[0]
    print(f"{k:>4}-{h:<3} {np.median(per):>24.2f} {len(per):>12} {pool:>11.2f} {len(jp):>9}")
print("(20-20: <2 independent blocks per country — read the SIGN, never the magnitude)")
