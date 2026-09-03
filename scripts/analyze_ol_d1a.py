"""OL-D1a — OL1 replicated with the REAL structural flavor (the Kilian index).

Registration (trial-ledger.md 2026-09-03, committed before this ran): OL1's construction
VERBATIM (scripts/analyze_oil_cycle.py is the record), changing ONLY the flavor definition:
demand-flavored year = mean monthly Kilian index > prior year's mean; supply-flavored
otherwise. PRIMARY BAR (parent's, unchanged): demand-mean minus supply-mean >= +10pp among
oil-up years. Desk prior on record: passes but shrinks below OL1's +81.2pp.
SECONDARY (descriptive): the flavor-agreement table vs OL1's equity-sign flavor.
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
V = ROOT / "ingest" / "vault"

# ---- OL1's construction, verbatim ----
br = pd.read_csv(V / "commodities/brent_monthly_eia.csv", parse_dates=["Date"])
br["Year"] = br.Date.dt.year
oil_ann = br.groupby("Year").Price.mean()
oil_ret = np.log(oil_ann).diff()

rr = pd.read_csv(V / "debt/jst_real_returns.csv", comment="#")
glob = rr.pivot(index="year", columns="iso", values="equity").astype(float).mean(axis=1)

f = pd.read_csv(V / "factors/iima_monthly_factors.csv", na_values=["NA"])
f["Year"] = f.Date.str[:4].astype(int)
ind = f.groupby("Year").MF.apply(lambda x: float(np.expm1(np.log1p(x / 100).sum())))

# ---- the ONLY change: Kilian flavor ----
k = pd.read_csv(V / "commodities/kilian_index_monthly_1973_2019.csv", parse_dates=["date"])
k["Year"] = k.date.dt.year
k_ann = k.groupby("Year").kilian_index.mean()
k_flavor = (k_ann > k_ann.shift(1))          # True = global real activity rising = demand

j = pd.concat([oil_ret, glob, ind, k_flavor], axis=1,
              keys=["oil", "glob", "ind", "kd"]).dropna()
j = j.loc[1994:2015]
up = j[j.oil > np.log(1.10)]
demand = up[up.kd.astype(bool)]
supply = up[~up.kd.astype(bool)]
print(f"OL-D1a: oil-up years n={len(up)} -> Kilian-demand {len(demand)} / Kilian-supply {len(supply)}")

if len(demand) == 0 or len(supply) == 0:
    print("OL-D1a PRIMARY: UNTESTABLE (an empty flavor cell) — recorded, bar unmoved")
else:
    md, ms = float(demand.ind.mean()), float(supply.ind.mean())
    diff = md - ms
    verdict = "PASS" if diff >= 0.10 else "FAIL"
    print(f"OL-D1a PRIMARY: demand {md*100:+.1f}% vs supply {ms*100:+.1f}% -> "
          f"diff {diff*100:+.1f}pp (bar >= +10pp) -> {verdict}")
    print(f"  vs OL1's +81.2pp: spread {'SHRANK' if abs(diff) < 0.812 else 'did NOT shrink'}")

agree = int((up.kd.astype(bool) == (up.glob > 0)).sum())
print(f"SECONDARY flavor-agreement: Kilian flavor == equity-sign flavor in {agree}/{len(up)} oil-up years")
for y, r in up.iterrows():
    print(f"  {int(y)}: oil {np.expm1(r.oil)*100:+.0f}% | Kilian={'D' if r.kd else 'S'} "
          f"equity={'D' if r.glob > 0 else 'S'} | India {r.ind*100:+.1f}%")
