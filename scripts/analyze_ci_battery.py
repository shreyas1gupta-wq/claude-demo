"""CI-D1..D5 — the credit + inflation battery (acceleration test, cross-asset regime
table, credit x inflation 2x2, crisis event study, India partial).

Registered 2026-09-07 BEFORE this run; priors/conventions live in the ledger. Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

ROOT = "/home/user/claude-demo"
df = pd.ExcelFile(f"{ROOT}/ingest/vault/jst/JSTdatasetR6.xlsx").parse("JRT6 Data")
df = df[["country", "year", "cpi", "eq_tr", "bond_tr", "bill_rate", "housing_tr",
         "tloans", "gdp", "xrusd", "crisisJST"]].sort_values(["country", "year"])

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
    g["rhouse"] = (1 + g.housing_tr) / (1 + g.infl) - 1
    g["dinfl"] = g.infl.diff()
    g["in_pct"] = expanding_percentile(g.infl.to_numpy(), min_obs=20)
    g["dpriv5"] = (g.tloans / g.gdp).diff(5)
    g["boom_pct"] = expanding_percentile(g.dpriv5.to_numpy(), min_obs=20)
    fx = g.xrusd if c != "USA" else pd.Series(1.0, index=g.index)
    g["gold_ret"] = (1 + (gold_y * fx).pct_change()) / (1 + g.infl) - 1
    for col, tag in [("req", "feq5"), ("rbond", "fbd5"), ("rhouse", "fh5")]:
        g[tag] = np.log1p(g[col]).rolling(5).mean().shift(-5).apply(np.expm1)
    g["crisis3"] = g.crisisJST.fillna(0).rolling(3).max().shift(-3)
    g["nxt_req"] = g.req.shift(-1)
    g["country"] = c
    frames.append(g.reset_index())
p = pd.concat(frames, ignore_index=True)
pw = p[(p.year >= 1950) & (p.year <= 2020)]  # postwar span for CI-D1/D2

print("CI-D1 — INFLATION DYNAMICS (1950-2020):")
acc = pw[pw.dinfl >= 0.02]
dec = pw[pw.dinfl <= -0.02]
stb = pw[(pw.dinfl > -0.02) & (pw.dinfl < 0.02)]
for lab, d in [("i1 accel (>=+2pp)", acc), ("i1 stable", stb), ("i1 decel (<=-2pp)", dec)]:
    print(f"  {lab:20}: same-yr real equity mean {100*d.req.mean():+6.1f}% / "
          f"median {100*d.req.median():+6.1f}% (n={d.req.notna().sum()})")
print("  i2 LEVEL x DIRECTION (own pct >=0.8 x dinfl sign), same-yr real equity:")
for hi in (True, False):
    for ris in (True, False):
        d = pw[(pw.in_pct >= 0.8) == hi]
        d = d[(d.dinfl > 0) == ris].dropna(subset=["req", "dinfl", "in_pct"])
        print(f"    {'HIGH' if hi else 'low ':>4} + {'rising ' if ris else 'falling'}: "
              f"mean {100*d.req.mean():+6.1f}% / median {100*d.req.median():+6.1f}% (n={len(d)})")
j = pw[["dinfl", "req"]].dropna()
k = pw[["infl", "req"]].dropna()
print(f"  i3 corr(dinfl, same-yr real equity)  = {stats.spearmanr(j.dinfl, j.req)[0]:+.2f} (n={len(j)})")
print(f"  i4 corr(level, same-yr real equity)  = {stats.spearmanr(k.infl, k.req)[0]:+.2f} (n={len(k)})")
print(f"  i5 next-1y real equity after accel years: mean {100*acc.nxt_req.mean():+.1f}% / "
      f"median {100*acc.nxt_req.median():+.1f}% (n={acc.nxt_req.notna().sum()})")

print("\nCI-D2 — CROSS-ASSET REGIME TABLE (same-yr real means, 1950-2020):")
print(f"  {'cell':>16} {'equity':>7} {'bonds':>7} {'bills':>7} {'housing':>8} {'gold-loc':>9} {'n':>5}")
for hi in (True, False):
    for ris in (True, False):
        d = pw[(pw.in_pct >= 0.8) == hi]
        d = d[(d.dinfl > 0) == ris].dropna(subset=["dinfl", "in_pct"])
        lab = f"{'HIGH' if hi else 'low'}+{'rising' if ris else 'falling'}"
        print(f"  {lab:>16} {100*d.req.mean():>6.1f}% {100*d.rbond.mean():>6.1f}% "
              f"{100*d.rbill.mean():>6.1f}% {100*d.rhouse.mean():>7.1f}% "
              f"{100*d.gold_ret.mean():>8.1f}% {len(d):>5}")

print("\nCI-D3 — CREDIT BOOM x HIGH INFLATION (full span; fwd-5y flagged overlapping):")
print(f"  {'cell':>18} {'j1 eq5':>7} {'j2 crisis3':>10} {'j3 bond5':>9} {'j4 house5':>10} {'n':>5}")
for bm in (True, False):
    for hi in (True, False):
        d = p[(p.boom_pct >= 0.8) == bm]
        d = d[(d.in_pct >= 0.8) == hi].dropna(subset=["boom_pct", "in_pct"])
        lab = f"{'BOOM' if bm else 'calm'}+{'HIGHinfl' if hi else 'lowinfl'}"
        print(f"  {lab:>18} {100*d.feq5.mean():>6.1f}% {100*d.crisis3.mean():>9.1f}% "
              f"{100*d.fbd5.mean():>8.1f}% {100*d.fh5.mean():>9.1f}% {len(d):>5}")

print("\nCI-D4 — CRISIS EVENT STUDY (full span, t=0 crisisJST year, real %/yr means):")
ev = {t: {"req": [], "rhouse": []} for t in range(-1, 4)}
hi_e, lo_e = [], []
for c, g in p.groupby("country"):
    g = g.set_index("year")
    for y in g.index[g.crisisJST.fillna(0) == 1]:
        for t in range(-1, 4):
            if y + t in g.index:
                ev[t]["req"].append(g.req.get(y + t))
                ev[t]["rhouse"].append(g.rhouse.get(y + t))
        (hi_e if g.in_pct.get(y, np.nan) >= 0.8 else lo_e).append(g.req.get(y))
n_ev = len([1 for c, g in p.groupby("country") for y in g.year[g.crisisJST.fillna(0) == 1]])
print(f"  {n_ev} crisis-years. {'t':>4} {'k1 equity':>10} {'k2 housing':>11}")
for t in range(-1, 4):
    r = pd.Series(ev[t]["req"], dtype=float)
    h = pd.Series(ev[t]["rhouse"], dtype=float)
    print(f"  {t:>4} {100*r.mean():>9.1f}% {100*h.mean():>10.1f}%")
hi_s, lo_s = pd.Series(hi_e, dtype=float), pd.Series(lo_e, dtype=float)
print(f"  k3 crisis-yr equity from HIGH-inflation entry: {100*hi_s.mean():+.1f}% "
      f"(n={hi_s.notna().sum()}) vs other entries {100*lo_s.mean():+.1f}% (n={lo_s.notna().sum()})")

print("\nCI-D5 — INDIA PARTIAL (nominal; IIMA RF as the rate proxy; 1994-2025):")
iima = pd.read_csv(f"{ROOT}/ingest/vault/factors/iima_monthly_factors.csv")
iima["year"] = iima.Date.str[:4].astype(int)
ann = iima.groupby("year").apply(lambda g: pd.Series({
    "mkt": np.expm1(np.log1p((g.MF + g.RF) / 100).sum()),
    "rf": np.expm1(np.log1p(g.RF / 100).sum())}))
ann = ann[(ann.index >= 1994) & (ann.index <= 2025)].dropna()
ann["drf"] = ann.rf.diff()
ann["nxt"] = ann.mkt.shift(-1)
j = ann.dropna(subset=["drf", "mkt"])
print(f"  l1 corr(dRF, same-yr market) = {stats.spearmanr(j.drf, j.mkt)[0]:+.2f} (n={len(j)})")
up, dn = j[j.drf > 0], j[j.drf <= 0]
print(f"  l2 rising-RF years: mean {100*up.mkt.mean():+.1f}% / median {100*up.mkt.median():+.1f}% (n={len(up)})"
      f"  ||  falling-RF: mean {100*dn.mkt.mean():+.1f}% / median {100*dn.mkt.median():+.1f}% (n={len(dn)})")
print(f"  l3 next-1y after rising-RF years: mean {100*up.nxt.mean():+.1f}% / "
      f"median {100*up.nxt.median():+.1f}% (n={up.nxt.notna().sum()})")
