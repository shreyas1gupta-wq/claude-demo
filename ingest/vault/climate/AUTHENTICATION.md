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
