"""CU-D6 — FX -> equity in both denominations. Registered 2026-09-07 BEFORE this run."""
import sys
import numpy as np
import pandas as pd
from scipy import stats
sys.path.insert(0, "/home/user/claude-demo")

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "xrusd"]].sort_values(["country", "year"])
us = df[df.country == "USA"].set_index("year")
us_infl = us.cpi.pct_change()

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
    g["dep5"] = g.dep.rolling(5).mean()
    g["fwd5_loc"] = np.log1p(g.req).rolling(5).mean().shift(-5).apply(np.expm1)
    g["fwd5_usd"] = np.log1p(g.rusd).rolling(5).mean().shift(-5).apply(np.expm1)
    g["nxt_loc"] = g.req.shift(-1)
    g["nxt_usd"] = g.rusd.shift(-1)
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)

j = p[["dep", "rusd"]].dropna()
rho = stats.spearmanr(j.dep, j.rusd)[0]
beta = stats.linregress(j.dep, j.rusd).slope
print(f"CU-D6(a) same-year: corr(dep, USD real ret) = {rho:+.2f} | pass-through beta = {beta:+.2f} (n={len(j)})")

p["bkt"] = np.where(p.dep >= 0.10, "WEAK(dep>=10%)",
             np.where(p.dep <= -0.05, "STRONG(app>=5%)", "normal"))
print(f"\nCU-D6(b) depreciation-regime buckets (same-year and next-1y means):")
print(f"{'bucket':>16} {'n':>5} {'same-yr LOCAL':>14} {'same-yr USD':>12} {'next-1y LOCAL':>14} {'next-1y USD':>12}")
for b in ["WEAK(dep>=10%)", "normal", "STRONG(app>=5%)"]:
    d = p[(p.bkt == b) & p.dep.notna()]
    print(f"{b:>16} {len(d):>5} {100*d.req.mean():>13.1f}% {100*d.rusd.mean():>11.1f}% "
          f"{100*d.nxt_loc.mean():>13.1f}% {100*d.nxt_usd.mean():>11.1f}%")

for k, label in [("fwd5_loc", "LOCAL"), ("fwd5_usd", "USD  ")]:
    j = p[["dep5", k]].dropna()
    print(f"CU-D6(c) trail-5y depreciation -> next-5y {label} real CAGR: rho "
          f"{stats.spearmanr(j.dep5, j[k])[0]:+.2f} (n={len(j)})")

# India
inr = pd.read_csv(f"{ROOT}/ingest/vault/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"])
inr_y = inr.set_index("Date").INR_per_USD.resample("YE").last(); inr_y.index = inr_y.index.year
dep = np.log(inr_y).diff()
iima = pd.read_csv(f"{ROOT}/ingest/vault/factors/iima_monthly_factors.csv")
iima["year"] = iima.Date.str[:4].astype(int)
mkt = iima.groupby("year").apply(lambda g: np.expm1(np.log1p((g.MF + g.RF) / 100).sum()))
usd_ret = (1 + mkt) * (inr_y.shift(1) / inr_y) - 1
d = pd.concat([dep, mkt, usd_ret], axis=1, keys=["dep", "loc", "usd"]).dropna()
d = d[(d.index >= 1994) & (d.index <= 2025)]
print(f"\nCU-D6(d1) India same-year corr(INR dep, USD market ret) = "
      f"{stats.spearmanr(d.dep, d.usd)[0]:+.2f} (n={len(d)})  [local was -0.69]")
weak = d[d.dep >= 0.05]; rest = d[d.dep < 0.05]
print(f"CU-D6(d2) India weak-INR years (dep>=5%, n={len(weak)}): local {100*weak['loc'].mean():+.1f}% | "
      f"USD {100*weak.usd.mean():+.1f}%; other years: local {100*rest['loc'].mean():+.1f}% | USD {100*rest.usd.mean():+.1f}%")
nx = d.shift(-1)
print(f"CU-D6(d3) India NEXT year after weak-INR: local {100*nx['loc'][d.dep>=0.05].mean():+.1f}% | "
      f"USD {100*nx.usd[d.dep>=0.05].mean():+.1f}%  (nominal both legs)")
