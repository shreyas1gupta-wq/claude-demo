"""CU-D1..D5 — the currency battery (PPP, UIP/carry, FX-equity, crashes, India partial).

Registered 2026-09-07 BEFORE this run; conventions/priors live in the ledger. Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "xrusd", "stir", "peg"]].sort_values(
    ["country", "year"])
us = df[df.country == "USA"].set_index("year")
us_infl = us.cpi.pct_change()
us_cpi = us.cpi
us_stir = us.stir

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
    g["dep"] = np.log(g.xrusd).diff()                                  # + = weakens
    g["idiff"] = (g.stir - us_stir) / 100
    g["infdiff"] = g.infl - us_infl
    g["ln_rer"] = -(np.log(g.xrusd) + np.log(us_cpi) - np.log(g.cpi))  # high = expensive
    g["rer_pct"] = expanding_percentile(g.ln_rer.to_numpy(), min_obs=20)
    g["rer_chg5"] = (g.ln_rer.shift(-5) - g.ln_rer) / 5
    g["fwd5"] = np.log1p(g.req).rolling(5).mean().shift(-5).apply(np.expm1)
    # USD investor real return
    usd_nom = (1 + g.eq_tr) * (g.xrusd.shift(1) / g.xrusd) - 1
    usd_real = (1 + usd_nom) / (1 + us_infl) - 1
    g["fwd5_usd"] = np.log1p(usd_real).rolling(5).mean().shift(-5).apply(np.expm1)
    g["dep_next"] = g.dep.shift(-1)
    # gold in local currency, real
    g["gold_loc"] = (gold_y * g.xrusd)
    g["gold_ret"] = (1 + g.gold_loc.pct_change()) / (1 + g.infl) - 1
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)
print(f"panel: {p.country.nunique()} non-US countries, {len(p)} country-years")

# ---- CU-D1: PPP ----
rows = [(c, g.dep.mean(), g.infdiff.mean()) for c, g in p.groupby("country")
        if g[["dep", "infdiff"]].dropna().shape[0] >= 50]
dd, ii = np.array([(a, b) for _, a, b in rows]).T
print(f"\nCU-D1(i) cross-country corr(mean depreciation, mean infl diff) = "
      f"{stats.spearmanr(dd, ii)[0]:+.2f} (n={len(rows)})")
j = p[["rer_pct", "rer_chg5"]].dropna()
print(f"CU-D1(ii) pooled corr(RER percentile, next-5y RER change) = "
      f"{stats.spearmanr(j.rer_pct, j.rer_chg5)[0]:+.2f} (n={len(j)})")
k = p.groupby("country").apply(lambda g: g.ln_rer - g.ln_rer.mean()).reset_index(drop=True)
kk = pd.DataFrame({"x": k, "y": k.groupby(p.country.values).shift(-1)}).dropna()
phi = np.polyfit(kk.x, kk.y, 1)[0]
print(f"CU-D1(iii) pooled RER AR(1) phi = {phi:.2f} -> half-life {np.log(0.5)/np.log(phi):.1f}y")

# ---- CU-D2: UIP/carry ----
j = p[p.peg == 0][["idiff", "dep_next"]].dropna()
sl = stats.linregress(j.idiff, j.dep_next)
print(f"\nCU-D2(i) UIP slope (floating years, n={len(j)}): next-1y depreciation on rate diff"
      f" = {sl.slope:+.2f} (UIP predicts +1; se {sl.stderr:.2f})")
per = [stats.spearmanr(g.idiff, g.dep_next, nan_policy="omit")[0]
       for c, g in p[p.peg == 0].groupby("country")
       if g[["idiff", "dep_next"]].dropna().shape[0] >= 20]
print(f"CU-D2(ii) within-country median Spearman = {np.median(per):+.2f} (n={len(per)})")

# ---- CU-D3: FX and equities ----
j = p[["dep", "req"]].dropna()
print(f"\nCU-D3(i) same-year corr(depreciation, local real equity) = "
      f"{stats.spearmanr(j.dep, j.req)[0]:+.2f} (n={len(j)})")
j = p[["rer_pct", "fwd5"]].dropna()
print(f"CU-D3(ii) RER pct -> next-5y LOCAL real equity: {stats.spearmanr(j.rer_pct, j.fwd5)[0]:+.2f} (n={len(j)})")
j = p[["rer_pct", "fwd5_usd"]].dropna()
print(f"CU-D3(iii) RER pct -> next-5y USD real return: {stats.spearmanr(j.rer_pct, j.fwd5_usd)[0]:+.2f} (n={len(j)})")

# ---- CU-D4: crashes ----
p["crash"] = p.dep >= 0.15
cr, ot = p[p.crash], p[~p.crash & p.dep.notna()]
print(f"\nCU-D4(i) local real equity: crash years {100*cr.req.mean():+.1f}% (n={len(cr)}) vs "
      f"others {100*ot.req.mean():+.1f}%")
print(f"CU-D4(ii) gold in LOCAL currency, real: crash years {100*cr.gold_ret.mean():+.1f}% vs "
      f"others {100*ot.gold_ret.mean():+.1f}%")
nxt = p.assign(f3=p.groupby("country").req.transform(
    lambda s: np.log1p(s).rolling(3).mean().shift(-3).apply(np.expm1)))
print(f"CU-D4(iii) next-3y local real equity after crash: {100*nxt[nxt.crash].f3.mean():+.1f}%/yr "
      f"vs after others {100*nxt[~nxt.crash & nxt.dep.notna()].f3.mean():+.1f}%/yr")

# ---- CU-D5: India partial ----
inr = pd.read_csv(f"{ROOT}/ingest/vault/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"])
inr_y = inr.set_index("Date").INR_per_USD.resample("YE").last()
inr_y.index = inr_y.index.year
dep_in = np.log(inr_y).diff()
iima = pd.read_csv(f"{ROOT}/ingest/vault/factors/iima_monthly_factors.csv")
iima["year"] = iima.Date.str[:4].astype(int)
mkt = iima.groupby("year").apply(lambda g: np.expm1(np.log1p((g.MF + g.RF) / 100).sum()))
j = pd.concat([dep_in, mkt], axis=1, keys=["dep", "ret"]).dropna()
j = j[(j.index >= 1994) & (j.index <= 2025)]
print(f"\nCU-D5(i) India same-year corr(INR depreciation, nominal market return) = "
      f"{stats.spearmanr(j.dep, j.ret)[0]:+.2f} (n={len(j)})")
gold_inr = (gold_y * inr_y).pct_change().dropna()
worst = dep_in[(dep_in.index >= 1994)].nlargest(5)
print(f"CU-D5(ii) gold-INR nominal return in the 5 worst INR years "
      f"({list(worst.index)}): {100*gold_inr.reindex(worst.index).mean():+.1f}%/yr "
      f"vs other-year mean {100*gold_inr[(gold_inr.index >= 1994) & (~gold_inr.index.isin(worst.index))].mean():+.1f}%/yr")
