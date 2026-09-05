"""ER-D8 — the market as the economy's forecaster (trailing returns -> future GDP growth).

Registered 2026-09-05 BEFORE this run. Pooled 3x3 grid + within-country diagonal + India
descriptive. Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo"
TRAIL, FWD = [1, 5, 10], [1, 5, 10]

df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "rgdpmad"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["req"] = (1 + df.eq_tr) / (1 + df.infl) - 1
df["g"] = np.log(df.rgdpmad).groupby(df.country).diff()

frames = []
for c, g in df.groupby("country"):
    g = g[(g.year >= 1950) & (g.year <= 2020)].set_index("year").copy()
    for k in TRAIL:
        g[f"tr{k}"] = np.log1p(g.req).rolling(k).mean().apply(np.expm1)
    for h in FWD:
        g[f"gw{h}"] = g.g.rolling(h).mean().shift(-h)
    for k in TRAIL:
        g[f"tr{k}_pct"] = expanding_percentile(g[f"tr{k}"].to_numpy(), min_obs=20)
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)

print("ER-D8(a) — pooled Spearman: trailing real equity return -> NEXT real GDP/cap growth")
print(f"{'trailing':>10}" + "".join(f"  next-{h}y" for h in FWD))
for k in TRAIL:
    row = f"{k:>8}y  "
    for h in FWD:
        j = p[[f"tr{k}", f"gw{h}"]].dropna()
        row += f"  {stats.spearmanr(j.iloc[:, 0], j.iloc[:, 1])[0]:+6.2f}"
    print(row + f"   (n at next-5y: {len(p[[f'tr{k}','gw5']].dropna())})")

print("\nER-D8(b) — within-country diagonal (own-country expanding rank of trailing return):")
for k, h in [(1, 1), (5, 5), (10, 10)]:
    j = p[[f"tr{k}_pct", f"gw{h}"]].dropna()
    print(f"  trail-{k}y rank -> next-{h}y growth: rho "
          f"{stats.spearmanr(j.iloc[:, 0], j.iloc[:, 1])[0]:+.2f} (n={len(j)})")

# India descriptive
nifty = pd.read_csv(f"{ROOT}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                    parse_dates=["Date"]).set_index("Date").sort_index().iloc[:, 0]
ny = nifty.resample("YE").last().pct_change().dropna()
ny.index = ny.index.year
tr3 = np.log1p(ny).rolling(3).mean().apply(np.expm1)
pwt = pd.read_csv(f"{ROOT}/ingest/vault/macro/pwt100.csv")
gcol = [c for c in pwt.columns if "GDP (output, multiple" in c][0]
ind = pwt[pwt.Entity == "India"].set_index("Year")
ig = np.log(ind[gcol].astype(float) / ind.Population.astype(float)).diff()
print("\nER-D8(c) — India (NIFTY trail-3y vs PWT growth; SHORT, descriptive):")
for h in (1, 3):
    fwd = ig.rolling(h).mean().shift(-h)
    j = pd.concat([tr3, fwd], axis=1, keys=["x", "y"]).dropna()
    r = stats.spearmanr(j.x, j.y)[0] if len(j) > 4 else np.nan
    print(f"  trail-3y -> next-{h}y growth: rho {r:+.2f} (n={len(j)})")
