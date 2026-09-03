"""EN-D2a — the ENSO→monsoon first-link contingency table, computed as registered.

Registration (trial-ledger.md 2026-09-03, committed BEFORE this ran): El Niño year = mean
ONI anom over MJJ/JJA/JAS/ASO of Y >= +0.5 (secondary: >=3 of those seasons labeled
el_nino); deficient year = JJAS < 90% of the full-sample-mean LPA (sensitivity: 1961-2010
LPA); joint span 1950-2016; eras 1950-1969 / 1970-1990 / 1991-2016; verification bar:
pooled P(deficient | El Nino) in [45%, 70%].
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CLIM = ROOT / "ingest" / "vault" / "climate"
MONSOON_SEASONS = ["MJJ", "JJA", "JAS", "ASO"]

o = pd.read_csv(CLIM / "oni_seasonal_1950_2026.csv")
m = o[o.season.isin(MONSOON_SEASONS)].groupby("year").agg(
    anom=("anom_c", "mean"),
    n_elnino_lbl=("oni", lambda x: (x == "el_nino").sum()))
r = pd.read_csv(CLIM / "aismr_jjas_1872_2016.csv").set_index("year")

j = m.join(r, how="inner").loc[1950:2016]
lpa_full = pd.read_csv(CLIM / "aismr_jjas_1872_2016.csv").jjas_mm.mean()
lpa_6110 = r.loc[1961:2010, "jjas_mm"].mean()
j["elnino"] = j.anom >= 0.5
j["elnino2"] = j.n_elnino_lbl >= 3
j["deficient"] = j.jjas_mm < 0.90 * lpa_full
print(f"Joint span {j.index.min()}-{j.index.max()} n={len(j)}; "
      f"LPA full-sample {lpa_full:.1f}mm, 1961-2010 {lpa_6110:.1f}mm")


def table(sub, tag):
    en = sub[sub.elnino]
    nn = sub[~sub.elnino]
    p_en = en.deficient.mean() if len(en) else float("nan")
    p_nn = nn.deficient.mean() if len(nn) else float("nan")
    print(f"{tag}: n={len(sub)} | El Nino {len(en)} (deficient {int(en.deficient.sum())}, "
          f"P={p_en:.0%}) | non-EN {len(nn)} (deficient {int(nn.deficient.sum())}, "
          f"P={p_nn:.0%}) | lift {p_en / p_nn if p_nn else float('nan'):.1f}x")
    return p_en


p_pooled = table(j, "POOLED 1950-2016")
for lo, hi in ((1950, 1969), (1970, 1990), (1991, 2016)):
    table(j.loc[lo:hi], f"ERA {lo}-{hi}")

bar = 0.45 <= p_pooled <= 0.70
print(f"\nVERIFICATION BAR: pooled P(deficient | El Nino) = {p_pooled:.1%} "
      f"in [45%, 70%] -> {'PASS' if bar else 'MISS (recorded on the B4a compilation)'}")

ens = sorted(j[j.elnino].index)
defs = sorted(j[j.deficient].index)
both = sorted(j[j.elnino & j.deficient].index)
print(f"El Nino years ({len(ens)}): {ens}")
print(f"Deficient years ({len(defs)}): {defs}")
print(f"Both ({len(both)}): {both}")
agree = (j.elnino == j.elnino2).mean()
print(f"Secondary definition (>=3 el_nino labels): agrees with primary in {agree:.0%} of years")
j2 = j.copy()
j2["deficient_6110"] = j2.jjas_mm < 0.90 * lpa_6110
en = j2[j2.elnino]
print(f"Sensitivity (LPA 1961-2010): P(deficient | El Nino) = {en.deficient_6110.mean():.0%}")
