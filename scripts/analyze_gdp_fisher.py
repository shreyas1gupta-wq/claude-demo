"""GDP-D1 + FISH-D1 — growth vs the market, Fisher vs the market (JST R6, 1950-2020).

Registered 2026-09-05 in research/register/trial-ledger.md BEFORE this run; definitions,
bars and priors live there. This script prints; it decides nothing.
"""
import numpy as np
import pandas as pd
from scipy import stats

ROOT = "/home/user/claude-demo"
Y0, Y1 = 1950, 2020

df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "rgdpmad"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["g"] = np.log(df.rgdpmad).groupby(df.country).diff()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1
df = df[(df.year >= Y0) & (df.year <= Y1)]

# ---- GDP-D1 (i): cross-country full-sample means ----
rows = []
for c, gdf in df.groupby("country"):
    j = gdf[["g", "req"]].dropna()
    if len(j) >= 50:
        rows.append((c, j.g.mean(), float(np.exp(np.log1p(j.req).mean()) - 1)))
cc = pd.DataFrame(rows, columns=["country", "g", "req"])
r_cc, p_cc = stats.pearsonr(cc.g, cc.req)
print(f"GDP-D1(i) cross-country (n={len(cc)}): corr(mean growth, real eq CAGR) = {r_cc:+.2f} (p={p_cc:.2f})")
print("   ", ", ".join(f"{c} g{100*g:.1f}/eq{100*e:.1f}" for c, g, e in
                       cc.sort_values("g").itertuples(index=False))[:400])

# ---- GDP-D1 (ii)+(iii): pooled within-country ----
df["g_next"] = df.groupby("country")["g"].shift(-1)
df["req_next"] = df.groupby("country")["req"].shift(-1)
j = df[["g", "req", "g_next", "req_next"]].dropna()
r_same, _ = stats.pearsonr(j.g, j.req)
r_fwd, _ = stats.pearsonr(j.g, j.req_next)       # growth predicting the market
r_rev, _ = stats.pearsonr(j.req, j.g_next)       # market predicting growth
print(f"GDP-D1(ii) pooled same-year corr(growth, real eq) = {r_same:+.2f} (n={len(j)})")
print(f"GDP-D1(iii) forward corr(growth_t, eq_t+1) = {r_fwd:+.2f} | "
      f"reverse corr(eq_t, growth_t+1) = {r_rev:+.2f}")

# ---- FISH-D1 (i): 1y Fisher slope, nominal eq on inflation ----
k = df[["eq_tr", "infl", "req"]].dropna()
sl = stats.linregress(k.infl, k.eq_tr)
print(f"\nFISH-D1(i) 1y pooled slope nominal-eq on inflation: beta = {sl.slope:+.2f} "
      f"(se {sl.stderr:.2f}, n={len(k)}; Fisher predicts +1)")

# ---- FISH-D1 (ii): 10y overlapping horizons ----
p10 = []
for c, gdf in df.groupby("country"):
    gdf = gdf.set_index("year")
    for t in range(Y0, Y1 - 9):
        w = gdf.loc[t:t + 9, ["eq_tr", "infl"]].dropna()
        if len(w) == 10:
            p10.append((float(np.exp(np.log1p(w.infl).mean()) - 1),
                        float(np.exp(np.log1p(w.eq_tr).mean()) - 1)))
xi, yn = np.array(p10).T
sl10 = stats.linregress(xi, yn)
print(f"FISH-D1(ii) 10y slope nominal-eq CAGR on inflation: beta = {sl10.slope:+.2f} "
      f"(se {sl10.stderr:.2f}, n={len(p10)} overlapping — se inflated-down, flag stands)")

# ---- FISH-D1 (iii): inflation-quintile split of REAL equity returns ----
q = k.infl.quantile([0.2, 0.8])
top, bot = k[k.infl >= q.iloc[1]], k[k.infl <= q.iloc[0]]
print(f"FISH-D1(iii) real eq return: top-quintile inflation {100*top.req.mean():+.1f}%/yr "
      f"(infl med {100*top.infl.median():.1f}%) vs bottom-quintile {100*bot.req.mean():+.1f}%/yr "
      f"(infl med {100*bot.infl.median():.1f}%)")
