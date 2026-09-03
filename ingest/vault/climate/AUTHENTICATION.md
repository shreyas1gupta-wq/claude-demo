# Climate vault — authentication protocol (2026-09-02)

File: elnino_sst_1950_2010.csv — statsmodels' vendored El Niño-region monthly SST dataset
(1950-2010, 61 years x 12 months; statsmodels docs describe it as Pacific El Niño-region
average sea-surface temperatures [VERIFY region definition — Niño 1+2 per docs]). Lineage:
statsmodels (major scientific package, data vendored in-repo) — pulled via
raw.githubusercontent (NOAA hosts proxy-blocked, no other mirror found).

## Pre-stated bars (written BEFORE the checks ran; results filled after the print)

| # | Check | Bar | Result |
|---|---|---|---|
| EA1a | Seasonal climatology shape: warmest calendar months in Feb-Apr, coolest in Aug-Oct (the Niño-region annual cycle) | both | warmest MAR/FEB/APR, coolest SEP/AUG/OCT — **PASS** |
| EA1b | By-month standardized anomalies must rank the canonical strong El Niños at the top: 1972, 1982-83, 1997-98 ALL in the top 5 annual peak-anomaly years | all three in top 5 | top-5 = 1998, 1997, 1983, 1982, 1972 — exactly the canon — **PASS** |
| EA1c | 1997-98 (the century's strongest event) in the top 2 | yes | top-2 = 1998, 1997 — **PASS** |

All bars passed first run; vault AUTHENTICATED. Caveat: 61 years, ends 2010 — episode
chronology after 2010 (2015-16, 2023-24 events) enters via the cases chapter's public record,
never spliced into this series.

---

## 2026-09-03 additions — ONI 1950-2026 + all-India summer monsoon rainfall 1872-2016 (two-pass)

### Pass 1 — sources, extraction specs, anchors (committed BEFORE any value check)

**File 1: oni_seasonal_1950_2026_raw.csv** — from github.com/ahuang11/ninodata (a maintained
mirror of the NOAA CPC ONI table; columns season/year/sst_c/anom_c/threshold/cumulative/
ntotal/oni). Chain: NOAA CPC → mirror repo → here. This closes the runsheet's "ONI post-2010
continuation" gap. Extraction: season, year, anom_c, oni (CPC-style episode label) →
oni_seasonal_1950_2026.csv. Disclosure: head rows (DJF-FMA 1950) and tail rows (FMA-AMJ 2026)
were seen during format inspection — they serve as no anchor.

**File 2: aismr_monthly_1872_2016_raw.csv** — from github.com/trinity652/
Monsoon-Prediction-Indian-Subcontinent (a student forecasting repo vendoring what is, by
shape and span, the IITM all-India summer-monsoon homogeneous series v1871-2016: YEAR, JUN,
JUL, AUG, SEP, JJAS; 145 rows 1872-2016; units appear to be TENTHS OF MM — anchor R5 tests
this). WEAK chain (the TradingView class) — anchors carry the admission; IMD/IITM primaries
stay on the runsheet. Extraction: YEAR, JJAS/10 → aismr_jjas_1872_2016.csv (mm).
Disclosure: rows 1872, 1873 (head), 2014, 2015, 2016 (tail) were seen during coverage
inspection — NONE of those years serves as an anchor.

| # | File | Anchor | Bar |
|---|---|---|---|
| O1 | ONI | 1997-98 El Niño (published peak 2.4) | max anom_c in seasons of 1997 ≥ 2.0 |
| O2 | ONI | 2015-16 El Niño (published peak 2.6) | max anom_c in seasons of 2015 ≥ 2.0 |
| O3 | ONI | 1988-89 La Niña (published trough −1.8) | min anom_c in seasons of 1988 ≤ −1.5 |
| O4 | ONI | 2023 El Niño (published peak ~2.0) | max anom_c in seasons of 2023 ≥ 1.5 |
| O5 | ONI | structure | contiguous seasons DJF-1950..AMJ-2026; 12 rows per full year; all anom_c ∈ [−3, 3.5] |
| R1 | AISMR | 1877 Great-Famine failure | 1877 JJAS in the sample's bottom decile |
| R2 | AISMR | 1972 drought (documented ~−24%) | 1972 JJAS < 90% of full-sample mean |
| R3 | AISMR | 2002 drought (documented ~−19%) | 2002 JJAS < 90% of full-sample mean |
| R4 | AISMR | 1961 flood year (documented ~+21%) | 1961 JJAS in the sample's top decile |
| R5 | AISMR | structure + units | 145 contiguous years 1872-2016; JJAS = JUN+JUL+AUG+SEP (±2 units); full-sample JJAS mean ∈ [8000, 9000] tenths-of-mm (the canonical 800-900mm all-India scale) |

Admission rule (stated now): each file admits on its own anchors — ONI needs O1-O5 all
(primary-adjacent chain); AISMR needs ≥4 of R1-R5 with R5 (units) mandatory; misses recorded,
never re-barred.
