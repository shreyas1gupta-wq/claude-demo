"""Extract ONI + AISMR vault files and run pass-2 anchors (bars fixed in AUTHENTICATION.md)."""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CLIM = ROOT / "ingest" / "vault" / "climate"

SEASONS = ["DJF", "JFM", "FMA", "MAM", "AMJ", "MJJ", "JJA", "JAS", "ASO", "SON", "OND", "NDJ"]


def flag(ok):
    return "PASS" if ok else "MISS"


# ---- ONI ----
o = pd.read_csv(CLIM / "oni_seasonal_1950_2026_raw.csv")
o = o[["season", "year", "anom_c", "oni"]]
o.to_csv(CLIM / "oni_seasonal_1950_2026.csv", index=False)
print(f"ONI extracted: {len(o)} rows {o.year.min()}-{o.year.max()}")

for tag, yr, bar, lo in (("O1", 1997, 2.0, False), ("O2", 2015, 2.0, False),
                         ("O3", 1988, -1.5, True), ("O4", 2023, 1.5, False)):
    sub = o[o.year == yr].anom_c
    v = sub.min() if lo else sub.max()
    ok = (v <= bar) if lo else (v >= bar)
    print(f"{tag} {flag(bool(ok))}: {yr} {'min' if lo else 'max'} anom = {v:+.2f} (bar {'<=' if lo else '>='} {bar})")

full_years = o.groupby("year").size()
interior = full_years.loc[1951:2025]
o5 = bool((interior == 12).all() and o.anom_c.between(-3, 3.5).all()
          and o.season.iloc[0] == "DJF" and int(o.year.iloc[0]) == 1950
          and o.season.iloc[-1] == "AMJ" and int(o.year.iloc[-1]) == 2026)
print(f"O5 {flag(o5)}: full years all 12 rows={bool((interior == 12).all())}, "
      f"anom range [{o.anom_c.min():+.2f},{o.anom_c.max():+.2f}], ends {o.season.iloc[-1]}-{o.year.iloc[-1]}")

# ---- AISMR ----
a = pd.read_csv(CLIM / "aismr_monthly_1872_2016_raw.csv")
a.columns = [c.strip() for c in a.columns]
out = pd.DataFrame({"year": a.YEAR, "jjas_mm": a.JJAS / 10.0})
out.to_csv(CLIM / "aismr_jjas_1872_2016.csv", index=False)
s = pd.Series(a.JJAS.values, index=a.YEAR.values)
mean = s.mean()
print(f"\nAISMR extracted: {len(s)} rows {s.index.min()}-{s.index.max()}, JJAS mean {mean:.0f} (tenths of mm)")

r1 = s.loc[1877] <= np.quantile(s, 0.10)
print(f"R1 {flag(bool(r1))}: 1877 JJAS = {s.loc[1877]} vs bottom decile {np.quantile(s, 0.10):.0f}")
r2 = s.loc[1972] < 0.90 * mean
print(f"R2 {flag(bool(r2))}: 1972 JJAS = {s.loc[1972]} vs 90% of mean {0.9 * mean:.0f}")
r3 = s.loc[2002] < 0.90 * mean
print(f"R3 {flag(bool(r3))}: 2002 JJAS = {s.loc[2002]} vs 90% of mean {0.9 * mean:.0f}")
r4 = s.loc[1961] >= np.quantile(s, 0.90)
print(f"R4 {flag(bool(r4))}: 1961 JJAS = {s.loc[1961]} vs top decile {np.quantile(s, 0.90):.0f}")
consistency = (a.JJAS - (a.JUN + a.JUL + a.AUG + a.SEP)).abs().max()
years_contig = bool((np.diff(a.YEAR.values) == 1).all())
r5 = bool(len(a) == 145 and years_contig and consistency <= 2 and 8000 <= mean <= 9000)
print(f"R5 {flag(r5)}: n=145={len(a) == 145}, contiguous={years_contig}, "
      f"max|JJAS-sum|={consistency}, mean {mean:.0f} in [8000,9000]")
