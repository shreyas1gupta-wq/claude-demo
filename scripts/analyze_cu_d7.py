"""CU-D7 — crash anatomy + India/US regime tables. Registered 2026-09-07 BEFORE this run."""
import numpy as np
import pandas as pd
from scipy import stats

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "xrusd"]].sort_values(["country", "year"])
us = df[df.country == "USA"].set_index("year")
us_infl = us.cpi.pct_change()

gold = pd.read_csv(f"{ROOT}/ingest/vault/commodities/gold_monthly_1833_2026.csv")
gold.columns = [c.strip().lower() for c in gold.columns]
dcol = [c for c in gold.columns if "date" in c or "month" in c or "year" in c][0]
pcol = [c for c in gold.columns if c != dcol][0]
gold["year"] = pd.to_datetime(gold[dcol]).dt.year
gold_y = gold.groupby("year")[pcol].last()

frames = []
for c, g in df.groupby("country"):
    if c == "USA":
        continue
    g = g[(g.year >= 1950) & (g.year <= 2020)].set_index("year").copy()
    g["infl"] = g.cpi.pct_change()
    g["req"] = (1 + g.eq_tr) / (1 + g.infl) - 1
    g["dep"] = np.log(g.xrusd).diff()
    usd_nom = (1 + g.eq_tr) * (g.xrusd.shift(1) / g.xrusd) - 1
    g["rusd"] = (1 + usd_nom) / (1 + us_infl) - 1
    g["nxt_loc"], g["nxt_usd"] = g.req.shift(-1), g.rusd.shift(-1)
    g["f3_loc"] = np.log1p(g.req).rolling(3).mean().shift(-3).apply(np.expm1)
    g["f3_usd"] = np.log1p(g.rusd).rolling(3).mean().shift(-3).apply(np.expm1)
    g["gold_ret"] = (1 + (gold_y * g.xrusd).pct_change()) / (1 + g.infl) - 1
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)
cr = p[p.dep >= 0.15]
ot = p[(p.dep < 0.15) & p.dep.notna()]

print(f"CU-D7(a1) crash census: {len(cr)} episodes; by decade:",
      dict(cr.groupby((cr.year // 10) * 10).size()))
print(f"   median depreciation {100*cr.dep.median():.0f}%, max {100*cr.dep.max():.0f}% "
      f"({cr.loc[cr.dep.idxmax()].country} {int(cr.loc[cr.dep.idxmax()].year)}); "
      f"countries: {cr.country.value_counts().head(5).to_dict()}")
def stat(s):
    s = s.dropna()
    return f"mean {100*s.mean():+.1f}% | median {100*s.median():+.1f}% | %>0: {100*(s>0).mean():.0f}% (n={len(s)})"
print(f"CU-D7(a2) crash-yr LOCAL real:  {stat(cr.req)}")
print(f"CU-D7(a3) crash-yr USD real:   {stat(cr.rusd)}")
print(f"CU-D7(a4) next-1y LOCAL: {stat(cr.nxt_loc)} | USD: {stat(cr.nxt_usd)}")
print(f"CU-D7(a5) next-3y LOCAL CAGR: {stat(cr.f3_loc)} | USD: {stat(cr.f3_usd)}")
print(f"CU-D7(a6) gold-local real in crash yrs: {stat(cr.gold_ret)} vs others median "
      f"{100*ot.gold_ret.median():+.1f}%")

# ---- India ----
inr = pd.read_csv(f"{ROOT}/ingest/vault/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"])
inr_y = inr.set_index("Date").INR_per_USD.resample("YE").last(); inr_y.index = inr_y.index.year
dep = np.log(inr_y).diff()
iima = pd.read_csv(f"{ROOT}/ingest/vault/factors/iima_monthly_factors.csv")
iima["year"] = iima.Date.str[:4].astype(int)
mkt = iima.groupby("year").apply(lambda g: np.expm1(np.log1p((g.MF + g.RF) / 100).sum()))
usd_ret = (1 + mkt) * (inr_y.shift(1) / inr_y) - 1
d = pd.concat([dep, mkt, usd_ret], axis=1, keys=["dep", "loc", "usd"]).dropna()
d = d[(d.index >= 1994) & (d.index <= 2025)]
d["bkt"] = np.where(d.dep >= 0.08, "WEAK(dep>=8%)",
             np.where(d.dep <= -0.02, "STRONG(app>=2%)", "normal"))
print(f"\nCU-D7(b) INDIA regime table (nominal, 1994-2025):")
print(f"{'bucket':>16} {'n':>3} {'same-yr LOCAL':>14} {'same-yr USD':>12} {'next-1y LOCAL':>14} {'next-1y USD':>12}")
for b in ["WEAK(dep>=8%)", "normal", "STRONG(app>=2%)"]:
    x = d[d.bkt == b]
    nx = d.shift(-1).loc[x.index]
    print(f"{b:>16} {len(x):>3} {100*x['loc'].mean():>13.1f}% {100*x.usd.mean():>11.1f}% "
          f"{100*nx['loc'].mean():>13.1f}% {100*nx.usd.mean():>11.1f}%")
big = dep[dep >= 0.15]
print(f"CU-D7(b5) INR >=15% crash years since 1973: "
      + ", ".join(f"{int(y)} ({100*v:.0f}%)" for y, v in big.items()))

# ---- US: broad dollar ----
dollar = p.groupby("year").dep.mean() * -1  # + = USD strong... dep is local weaken = USD strong; so mean dep IS dollar strength
dollar = p.groupby("year").dep.mean()       # + = USD strong vs panel
usre = ((1 + us.eq_tr) / (1 + us_infl) - 1)
j = pd.concat([dollar.rename("dxy"), usre.rename("req")], axis=1).dropna()
j = j[(j.index >= 1950) & (j.index <= 2020)]
print(f"\nCU-D7(c1) same-year corr(broad-dollar change, US real equity) = "
      f"{stats.spearmanr(j.dxy, j.req)[0]:+.2f} (n={len(j)})")
j["bkt"] = np.where(j.dxy >= 0.05, "USD STRONG(>=+5%)",
             np.where(j.dxy <= -0.05, "USD WEAK(<=-5%)", "normal"))
j["nxt"] = j.req.shift(-1)
print(f"CU-D7(c2/c3) US regime table:")
print(f"{'bucket':>18} {'n':>3} {'same-yr US real':>16} {'next-1y US real':>16}")
for b in ["USD STRONG(>=+5%)", "normal", "USD WEAK(<=-5%)"]:
    x = j[j.bkt == b]
    print(f"{b:>18} {len(x):>3} {100*x.req.mean():>15.1f}% {100*x.nxt.mean():>15.1f}%")
