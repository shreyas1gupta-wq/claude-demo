"""ER-D7 — the HONEST GRID: expanding within-country rank bins, pooled purged cell means.

Registered 2026-09-05 (audit follow-up) BEFORE this run. All states real-time
(quant.ladder expanding percentiles, min_obs=20y); forecasts use COMPLETED windows only
(s <= t-h); benchmark = expanding pooled mean on the identical information set. Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "eq_dp"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1

frames = []
for c, g in df.groupby("country"):
    g = g[(g.year >= 1950) & (g.year <= 2020)].set_index("year").copy()
    if g[["eq_dp", "infl", "req"]].dropna().shape[0] < 60:
        continue
    g["dp_pct"] = expanding_percentile(g.eq_dp.to_numpy(), min_obs=20)
    g["in_pct"] = expanding_percentile(g.infl.to_numpy(), min_obs=20)
    for h in (5, 10):
        g[f"fwd{h}"] = np.log1p(g.req).rolling(h).mean().shift(-h).apply(np.expm1)
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)
print(f"panel: {p.country.nunique()} countries, {len(p)} country-years")

def terc(x):
    return np.where(np.isnan(x), np.nan, np.where(x <= 1/3, 1, np.where(x <= 2/3, 2, 3)))

p["dp_t"] = terc(p.dp_pct.to_numpy())
p["in_t"] = terc(p.in_pct.to_numpy())

for h, y0, y1 in [(5, 1970, 2010), (10, 1970, 2000)]:
    sse_m, sse_b, preds = 0.0, 0.0, []
    for t in range(y0, y1 + 1):
        past = p[(p.year <= t - h)].dropna(subset=[f"fwd{h}"])          # completed windows
        pool_mean = past[f"fwd{h}"].mean() if len(past) else np.nan
        now = p[(p.year == t)].dropna(subset=[f"fwd{h}", "dp_t", "in_t"])
        for _, r in now.iterrows():
            cell = past[(past.dp_t == r.dp_t) & (past.in_t == r.in_t)][f"fwd{h}"]
            f = cell.mean() if len(cell) >= 4 else pool_mean
            if np.isnan(f) or np.isnan(pool_mean):
                continue
            sse_m += (r[f"fwd{h}"] - f) ** 2
            sse_b += (r[f"fwd{h}"] - pool_mean) ** 2
            preds.append(1)
    r2 = 1 - sse_m / sse_b
    print(f"ER-D7(i) {h}y recursive OOS (starts {y0}-{y1}, n={len(preds)}): "
          f"R2 vs expanding pooled mean = {100*r2:+.1f}%")

# (ii)+(iii) real-time corner spread at 5y + era split
j5 = p[(p.year >= 1970) & (p.year <= 2010)].dropna(subset=["fwd5", "dp_t", "in_t"])
cheap = j5[(j5.dp_t == 3) & (j5.in_t == 1)]
expen = j5[(j5.dp_t == 1) & (j5.in_t == 3)]
print(f"ER-D7(ii) real-time corners 5y: cheap+lowinfl {100*cheap.fwd5.mean():+.1f}%/yr "
      f"(n={len(cheap)}) vs expensive+highinfl {100*expen.fwd5.mean():+.1f}%/yr "
      f"(n={len(expen)}) -> SPREAD {100*(cheap.fwd5.mean()-expen.fwd5.mean()):+.1f}pp/yr")
for a, b in [(1970, 1989), (1990, 2010)]:
    ch = cheap[(cheap.year >= a) & (cheap.year <= b)].fwd5
    ex = expen[(expen.year >= a) & (expen.year <= b)].fwd5
    print(f"ER-D7(iii) era {a}-{b}: spread {100*(ch.mean()-ex.mean()):+.1f}pp/yr "
          f"(n {len(ch)}/{len(ex)})")

# (iv) dp->10y in expanding-rank form: pooled + Germany
j = p.dropna(subset=["dp_pct", "fwd10"])
print(f"ER-D7(iv) dp(expanding rank)->10y Spearman: pooled "
      f"{stats.spearmanr(j.dp_pct, j.fwd10)[0]:+.2f} (n={len(j)})", end="")
gj = j[j.country == "Germany"]
print(f" | Germany {stats.spearmanr(gj.dp_pct, gj.fwd10)[0]:+.2f} (n={len(gj)})")
