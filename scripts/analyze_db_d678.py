"""DB-D6/D7/D8 — fiscal dominance, housing everywhere, top-carrier profiles.

Registered 2026-09-07 BEFORE this run. Prints only."""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "bond_tr", "bill_rate", "housing_tr",
         "debtgdp", "tloans", "gdp", "xrusd", "rgdpmad", "crisisJST",
         "ltrate"]].sort_values(["country", "year"])
gold = pd.read_csv(f"{ROOT}/ingest/vault/commodities/gold_monthly_1833_2026.csv")
gold.columns = [c.strip().lower() for c in gold.columns]
dcol = [c for c in gold.columns if "date" in c or "month" in c or "year" in c][0]
pcol = [c for c in gold.columns if c != dcol][0]
gold["year"] = pd.to_datetime(gold[dcol]).dt.year
gold_y = gold.groupby("year")[pcol].last()

frames = []
for c, g in df.groupby("country"):
    g = g.set_index("year").copy()
    g["infl"] = g.cpi.pct_change()
    g["req"] = (1 + g.eq_tr) / (1 + g.infl) - 1
    g["rbond"] = (1 + g.bond_tr) / (1 + g.infl) - 1
    g["rbill"] = (1 + g.bill_rate) / (1 + g.infl) - 1
    g["rlt"] = (1 + g.ltrate / 100) / (1 + g.infl) - 1
    g["rhouse"] = (1 + g.housing_tr) / (1 + g.infl) - 1
    g["grw"] = np.log(g.rgdpmad).diff()
    g["g5"] = g.grw.rolling(5).mean()
    g["dep"] = np.log(g.xrusd).diff() if c != "USA" else np.nan
    g["dpriv5"] = (g.tloans / g.gdp).diff(5)
    g["pub_pct"] = expanding_percentile(g.debtgdp.to_numpy(), min_obs=20)
    g["in_pct"] = expanding_percentile(g.infl.to_numpy(), min_obs=20)
    fx = g.xrusd if c != "USA" else pd.Series(1.0, index=g.index)
    g["gold_ret"] = (1 + (gold_y * fx).pct_change()) / (1 + g.infl) - 1
    for col, tag in [("rhouse", "fh5"), ("req", "fe5"), ("grw", "fg5"), ("rbill", "fb5")]:
        g[tag] = np.log1p(g[col]).rolling(5).mean().shift(-5).apply(np.expm1)
    g["nxt_house"] = g.rhouse.shift(-1)
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)
BK = [(0, 0.6, "<60%"), (0.6, 0.9, "60-90%"), (0.9, 1.2, "90-120%"), (1.2, 9, ">=120%")]

print("DB-D6 — FISCAL DOMINANCE:")
j = p[["pub_pct", "rbill"]].dropna()
print(f"  f1 corr(debt pct, same-yr real bill) = {stats.spearmanr(j.pub_pct, j.rbill)[0]:+.2f} (n={len(j)})")
j = p[["pub_pct", "fb5"]].dropna()
print(f"  f2 corr(debt pct, next-5y real bill) = {stats.spearmanr(j.pub_pct, j.fb5)[0]:+.2f} (n={len(j)})")
per = [stats.spearmanr(g.pub_pct, g.rlt, nan_policy="omit")[0] for c, g in p.groupby("country")
       if g[["pub_pct", "rlt"]].dropna().shape[0] >= 40]
print(f"  f3 within-country median corr(debt pct, real long rate) = {np.median(per):+.2f} (n={len(per)})")
print(f"  {'bucket':>8} {'f4 real bill':>13} {'f5 inflation':>13} {'f6 r-g':>9} {'f7 next-5y growth':>18} {'n':>6}")
for lo, hi, lab in BK:
    d = p[(p.debtgdp >= lo) & (p.debtgdp < hi)]
    rg = (d.rbill - d.grw).mean()
    print(f"  {lab:>8} {100*d.rbill.mean():>12.1f}% {100*d.infl.mean():>12.1f}% {100*rg:>8.1f}%"
          f" {100*d.fg5.mean():>17.1f}% {len(d):>6}")

print("\nDB-D7 — HOUSING:")
print("  h1 next-5y real housing by debt bucket:", " | ".join(
    f"{lab} {100*p[(p.debtgdp>=lo)&(p.debtgdp<hi)].fh5.mean():+.1f}%" for lo, hi, lab in BK))
cr = p[p.dep >= 0.15]
print(f"  h2 currency-crash years: same-yr housing real {100*cr.rhouse.mean():+.1f}% "
      f"(median {100*cr.rhouse.median():+.1f}%), next-1y {100*cr.nxt_house.mean():+.1f}% (n={len(cr.rhouse.dropna())})")
j = p[["g5", "fh5"]].dropna()
je = p[["g5", "fe5"]].dropna()
print(f"  h3 trail-5y growth -> next-5y HOUSING rho {stats.spearmanr(j.g5, j.fh5)[0]:+.2f} "
      f"(vs EQUITY {stats.spearmanr(je.g5, je.fe5)[0]:+.2f})")
j = p[["dpriv5", "fh5"]].dropna()
print(f"  h4 5y d(private credit) -> next-5y housing rho {stats.spearmanr(j.dpriv5, j.fh5)[0]:+.2f} (n={len(j)})")
top = p[p.in_pct >= 0.8]
bot = p[p.in_pct <= 0.2]
print(f"  h5 top-quintile own-inflation years: housing real {100*top.rhouse.mean():+.1f}% "
      f"vs equities {100*top.req.mean():+.1f}% | bottom-quintile housing {100*bot.rhouse.mean():+.1f}%")
hi_d = p[p.debtgdp >= 0.9]
lo_d = p[(p.debtgdp < 0.9) & p.debtgdp.notna()]
print(f"  h6 gold-local real in >=90% debt years: {100*hi_d.gold_ret.mean():+.1f}% "
      f"vs {100*lo_d.gold_ret.mean():+.1f}% others")

print("\nDB-D8 — TOP-CARRIER PROFILES (within-episode real CAGRs, %/yr):")
EP = [("UK", 1918, 1964), ("USA", 1945, 1950), ("Belgium", 1983, 2003),
      ("Italy", 1992, 2020), ("Japan", 1997, 2020)]
print(f"  {'episode':>20} {'equity':>7} {'bonds':>7} {'bills':>7} {'housing':>8} {'gold':>7} {'infl':>6} {'crises':>7}")
for c, a, b in EP:
    d = p[(p.country == c) & (p.year >= a) & (p.year <= b)]
    def cagr(s):
        s = s.dropna()
        return 100 * np.expm1(np.log1p(s).mean()) if len(s) else np.nan
    cr_yrs = sorted(int(y) for y in d[d.crisisJST.fillna(0) == 1].year)
    print(f"  {c+' '+str(a)+'-'+str(b):>20} {cagr(d.req):>6.1f} {cagr(d.rbond):>6.1f} "
          f"{cagr(d.rbill):>6.1f} {cagr(d.rhouse):>7.1f} {cagr(d.gold_ret):>6.1f} "
          f"{100*d.infl.mean():>5.1f} {str(cr_yrs) if cr_yrs else '-':>7}")
