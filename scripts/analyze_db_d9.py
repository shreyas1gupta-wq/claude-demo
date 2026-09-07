"""DB-D9 — debt vs currency, the borrower's spread, and the equity-positivity checks.
Registered 2026-09-07 BEFORE this run. Prints only."""
import sys
import numpy as np
import pandas as pd
from scipy import stats
sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "eq_dp", "ltrate", "housing_tr", "debtgdp",
         "xrusd"]].sort_values(["country", "year"])
frames = []
for c, g in df.groupby("country"):
    g = g.set_index("year").copy()
    g["infl"] = g.cpi.pct_change()
    g["req"] = (1 + g.eq_tr) / (1 + g.infl) - 1
    g["rhouse"] = (1 + g.housing_tr) / (1 + g.infl) - 1
    g["rlt"] = (1 + g.ltrate / 100) / (1 + g.infl) - 1
    g["pub_pct"] = expanding_percentile(g.debtgdp.to_numpy(), min_obs=20)
    g["dp_pct"] = expanding_percentile(g.eq_dp.to_numpy(), min_obs=20)
    g["dep5f"] = (np.log(g.xrusd).shift(-5) - np.log(g.xrusd)) / 5 if c != "USA" else np.nan
    g["fe5"] = np.log1p(g.req).rolling(5).mean().shift(-5).apply(np.expm1)
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)
BK = [(0, 0.6, "<60%"), (0.6, 0.9, "60-90%"), (0.9, 1.2, "90-120%"), (1.2, 9, ">=120%")]

j = p[["pub_pct", "dep5f"]].dropna()
print(f"c1 debt pct -> next-5y depreciation: rho {stats.spearmanr(j.pub_pct, j.dep5f)[0]:+.2f} (n={len(j)})")
print("c2 next-5y depreciation by debt bucket:", " | ".join(
    f"{lab} {100*p[(p.debtgdp>=lo)&(p.debtgdp<hi)].dep5f.mean():+.1f}%/yr" for lo, hi, lab in BK))
print("c3 BORROWER SPREAD housing - real long rate:", " | ".join(
    f"{lab} {100*(p[(p.debtgdp>=lo)&(p.debtgdp<hi)].rhouse.mean() - p[(p.debtgdp>=lo)&(p.debtgdp<hi)].rlt.mean()):+.1f}%" for lo, hi, lab in BK))
print("c4 BORROWER SPREAD equity - real long rate: ", " | ".join(
    f"{lab} {100*(p[(p.debtgdp>=lo)&(p.debtgdp<hi)].req.mean() - p[(p.debtgdp>=lo)&(p.debtgdp<hi)].rlt.mean()):+.1f}%" for lo, hi, lab in BK))
for a, b, lab in [(1870, 1979, "pre-1980"), (1980, 2020, "post-1980")]:
    j = p[(p.year >= a) & (p.year <= b)][["pub_pct", "fe5"]].dropna()
    print(f"c5 {lab}: debt pct -> next-5y equity rho {stats.spearmanr(j.pub_pct, j.fe5)[0]:+.2f} (n={len(j)})")
print("c6 valuation control (within dp terciles, next-5y equity, high-debt vs rest):")
j = p.dropna(subset=["dp_pct", "pub_pct", "fe5"])
for lo, hi, lab in [(0, 1/3, "expensive"), (1/3, 2/3, "mid"), (2/3, 1.01, "cheap")]:
    d = j[(j.dp_pct >= lo) & (j.dp_pct < hi)]
    hi_d, rest = d[d.pub_pct >= 0.8], d[d.pub_pct < 0.8]
    print(f"   {lab:9}: high-debt {100*hi_d.fe5.mean():+5.1f}% vs rest {100*rest.fe5.mean():+5.1f}% "
          f"(n {len(hi_d)}/{len(rest)})")
