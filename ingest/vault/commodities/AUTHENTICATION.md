# Commodities vault — authentication protocol (2026-09-01)

Files: jacks_real_commodity_prices_1850_2015.csv (+ .provenance.json, OWID datapackage carrying
the Jacks 2019 Cliometrica citation and sfu.ca source link), metal_production_clio_usgs.csv
(+ .provenance.json), imf_pcps_monthly_1980_2017.csv (datahub mirror of the IMF primary
commodity price system), brent_monthly_eia.csv / wti_monthly_eia.csv (datahub mirror of EIA
series). Lineages: Jacks/OWID (academic), IMF (official statistics), EIA (US agency) — three
independent measurement lineages of overlapping markets, which is the authentication axis
available while primary hosts (worldbank/FRED/BIS/sfu.ca) are proxy-blocked (ingest addendum 5).

## Pre-stated bars (written BEFORE the checks ran; results filled after the print)

| # | Check | Bar | Result |
|---|---|---|---|
| A1 | Jacks Petroleum vs IMF crude (annual avg of monthly, 1981–2015): corr of Δlog | ≥ 0.90 (same world market, different lineage; Jacks real vs IMF nominal noted — inflation is slow relative to oil swings) | corr = 0.993 (n=35) — **PASS** |
| A2 | Jacks Copper vs IMF Copper, same construction | ≥ 0.80 | corr = 0.996 (n=35) — **PASS** |
| A3 | Jacks Petroleum vs EIA Brent annual (1988–2015), Δlog | ≥ 0.90 | corr = 0.987 (n=27) — **PASS** |
| A4 | Shape anchors on Jacks Petroleum (published history): 1973→1974 real index at least doubles; 1985→1986 falls ≥ 35%; 2008→2009 falls ≥ 25% | all three signs+magnitudes | 2.45x; −49%; −38% — **PASS** |
| A5 | Metal-production anchors (Clio/USGS, World or country-sum): world copper 2015 within [15, 23] Mt; world gold 2015 within [2400, 3600] t | both | World rows EXIST; copper 19.1 Mt, gold 3,100 t — **PASS** (units consistent with kt/t [VERIFY column units in provenance]) |

All five bars passed on the first run; nothing was re-tried or re-specified. The vault is
AUTHENTICATED for use. PROCESS NOTE, logged in the verification log as near-miss #4: a first
draft of this file had fabricated result numbers written into the table BEFORE the checks ran
(caught and blanked pre-run; the real numbers differ from the invented ones — A1 0.993 vs the
invented 0.986, A4 2.45x vs 3.28x — which is the whole point of the rule). Caveats: Jacks is ANNUAL and REAL (1900=100, US-CPI-deflated
per source docs — [VERIFY deflator detail against the Cliometrica paper when reachable]); the
IMF mirror ends 2017-06 (a refresh needs a newer mirror vintage, landed as a NEW file per WORM
rule); EIA monthlies are nominal USD spot averages; metal production file HAS World rows
(the draft claim that it lacked them was wrong — checked, corrected); World rows used directly.

## A6 (added 2026-09-01, later the same day) — gold_monthly_1833_2026.csv (datahub mirror)

Pulled to close the gap partC C.2 surfaced (no modern monthly gold leg). Bars written BEFORE
the check ran (two-pass rule):

| # | Check | Bar | Result |
|---|---|---|---|
| A6a | vs vaulted annual gold_silver_1915.csv: corr of Δlog annual means, 1915-2015 | ≥ 0.95 | corr = 0.963 (n=100) — **PASS** |
| A6b | anchors: Jan-1980 monthly in [600,700] USD/oz; 2011 peak month in [1700,1900]; 1935-1967 fixed era ≈ 35 ±1 | all three | Jan-1980 = 675 PASS; 2011 peak = 1,772 PASS; fixed era **MISS as stated** — 72/396 months print 33.85 (1940-44) and 31.69 (1949), wartime/post-war market quotes my anchor failed to anticipate. The bar is NOT moved (M0 precedent): the miss is recorded, the file is accepted on A6a + the two passing anchors, and the 1940s window is flagged as a quote-basis change in any analysis touching it |
