"""Real long rate by decade (JST R6, 18 economies) and its relation to equity returns.

CONTEXT NOTE computation (descriptive; no hypothesis, no bars, no census consumption).
Real long rate_t = (1 + ltrate_t/100)/(1 + infl_t) - 1 (ex-post, realized CPI).
Per decade: median across countries of the decade-average real long rate, and the median
real equity geometric CAGR. Relation: pooled country-decade correlations, same-decade and
next-decade (rate in decade d vs equity return in d+1).
"""
import numpy as np
import pandas as pd
from scipy import stats

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "ltrate", "eq_tr"]].sort_values(["country", "year"])
df["infl"] = df.groupby("country")["cpi"].pct_change()
df["real_lt"] = (1 + df.ltrate / 100) / (1 + df.infl) - 1
df["real_eq"] = (1 + df.eq_tr) / (1 + df.infl) - 1
df["decade"] = (df.year // 10) * 10

rows = []
for (c, dec), g in df.groupby(["country", "decade"]):
    rl = g.real_lt.dropna()
    re = g.real_eq.dropna()
    rows.append(dict(country=c, decade=int(dec),
                     real_lt=float(rl.mean()) if len(rl) >= 7 else np.nan,
                     real_eq=float(np.exp(np.log1p(re).mean()) - 1) if len(re) >= 7 else np.nan))
cd = pd.DataFrame(rows)

print("MEDIAN ACROSS COUNTRIES, BY DECADE (real %/yr; n = countries with >=7 yrs)")
print(f"{'decade':>7} {'real long rate':>15} {'n':>3} {'real equity CAGR':>17} {'n':>3}")
for dec, g in cd.groupby("decade"):
    if dec < 1870 or dec > 2010:
        continue
    rl, re = g.real_lt.dropna(), g.real_eq.dropna()
    print(f"{dec:>6}s {100*rl.median():>14.1f} {len(rl):>3} {100*re.median():>16.1f} {len(re):>3}")

# pooled country-decade relation
j = cd.dropna(subset=["real_lt", "real_eq"])
j = j[(j.decade >= 1870) & (j.decade <= 2010)]
pr, pp = stats.pearsonr(j.real_lt, j.real_eq)
sr, sp = stats.spearmanr(j.real_lt, j.real_eq)
print(f"\nSAME-DECADE, pooled country-decades (n={len(j)}):")
print(f"  Pearson {pr:+.2f} (p={pp:.3f})   Spearman {sr:+.2f} (p={sp:.3f})")

nxt = cd.copy()
nxt["decade"] -= 10
j2 = cd.merge(nxt[["country", "decade", "real_eq"]], on=["country", "decade"],
              suffixes=("", "_next")).dropna(subset=["real_lt", "real_eq_next"])
j2 = j2[(j2.decade >= 1870) & (j2.decade <= 2000)]
pr2, pp2 = stats.pearsonr(j2.real_lt, j2.real_eq_next)
sr2, sp2 = stats.spearmanr(j2.real_lt, j2.real_eq_next)
print(f"NEXT-DECADE (rate decade d -> equity d+1, n={len(j2)}):")
print(f"  Pearson {pr2:+.2f} (p={pp2:.3f})   Spearman {sr2:+.2f} (p={sp2:.3f})")

# same-decade relation by rate bucket (terciles of real_lt)
q = j.real_lt.quantile([1/3, 2/3])
lo = j[j.real_lt <= q.iloc[0]]
mid = j[(j.real_lt > q.iloc[0]) & (j.real_lt <= q.iloc[1])]
hi = j[j.real_lt > q.iloc[1]]
print("\nEQUITY REAL CAGR BY REAL-RATE TERCILE (same decade, pooled):")
for name, b in [("low (repressed)", lo), ("middle", mid), ("high", hi)]:
    print(f"  {name:16}: rate median {100*b.real_lt.median():+5.1f} -> "
          f"equity median {100*b.real_eq.median():+5.1f} %/yr  (n={len(b)})")
