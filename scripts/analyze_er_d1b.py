"""ER-D1b — within vs between attribution of the pooled ER reads.

Registered 2026-09-05 BEFORE this run. Predictive legs use OWN-COUNTRY EXPANDING
percentiles (quant.ladder, min_obs=20 — recursive, no full-sample demeaning); attribution
legs may demean. Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "eq_dp", "rgdpmad"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1
df["g"] = np.log(df.rgdpmad).groupby(df.country).diff()

frames = []
for c, g in df.groupby("country"):
    g = g[(g.year >= 1950) & (g.year <= 2020)].set_index("year").copy()
    g["g5"] = g.g.rolling(5).mean()
    g["dp_pct"] = expanding_percentile(g.eq_dp.to_numpy(), min_obs=20)
    g["g5_pct"] = expanding_percentile(g.g5.to_numpy(), min_obs=20)
    g["in_pct"] = expanding_percentile(g.infl.to_numpy(), min_obs=20)
    for h in (10, 20):
        g[f"fwd{h}"] = np.log1p(g.req).rolling(h).mean().shift(-h).apply(np.expm1)
    g["gg20"] = g.g.rolling(20).mean().shift(-20)          # same-window growth (ER-D5 leg)
    g["y20"] = g["fwd20"]
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)

print("ER-D1b (1-4) — PREDICTIVE, own-country expanding-percentile form, pooled Spearman:")
for key, label in [("dp_pct", "dp rank"), ("g5_pct", "g5 rank")]:
    for h in (10, 20):
        j = p[[key, f"fwd{h}"]].dropna()
        print(f"  {label:8} -> next-{h}y: rho {stats.spearmanr(j[key], j[f'fwd{h}'])[0]:+.2f}"
              f" (n={len(j)})")

# (5) per-country median of own-country corr(g5 level, fwd10)
percountry = [stats.spearmanr(g.g5, g.fwd10, nan_policy="omit")[0]
              for _, g in p.groupby("country") if g[["g5", "fwd10"]].dropna().shape[0] >= 30]
print(f"ER-D1b (5) per-country corr(g5, fwd10): median {np.median(percountry):+.2f} "
      f"(n countries={len(percountry)})")

# (6-7) BETWEEN components
rows = []
for c, g in p.groupby("country"):
    j = g[["g5", "eq_dp", "req"]].dropna()
    if len(j) >= 45:
        rows.append((j.g5.mean(), j.eq_dp.mean(), float(np.expm1(np.log1p(j.req).mean()))))
bg, bd, br = np.array(rows).T
print(f"ER-D1b (6-7) BETWEEN: corr(mean g5, mean ret) {stats.spearmanr(bg, br)[0]:+.2f} | "
      f"corr(mean dp, mean ret) {stats.spearmanr(bd, br)[0]:+.2f} (n={len(rows)})")

# (8) ER-D5's 20y same-window growth cell, within-country demeaned (attribution leg)
j = p[["country", "gg20", "y20"]].dropna()
j = j.assign(gg=j.gg20 - j.groupby("country").gg20.transform("mean"),
             yy=j.y20 - j.groupby("country").y20.transform("mean"))
print(f"ER-D1b (8) same-20y growth vs return, WITHIN-demeaned: rho "
      f"{stats.spearmanr(j.gg, j.yy)[0]:+.2f} (n={len(j)}) [pooled raw was -0.20]")

# (9) FISH-D1(iii) regime split with own-country expanding inflation percentile
k = p[["in_pct", "req"]].dropna()
top = k[k.in_pct >= 0.8].req
bot = k[k.in_pct <= 0.2].req
print(f"ER-D1b (9) real eq return, own-country inflation quintiles: top {100*top.mean():+.1f}%/yr"
      f" vs bottom {100*bot.mean():+.1f}%/yr -> WITHIN gap {100*(bot.mean()-top.mean()):.1f}pp"
      f" (pooled raw gap was 12.0pp)")
