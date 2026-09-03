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

---

## 2026-09-03 additions — the Kilian index + the Känzig oil-supply-news shocks (two-pass)

### Pass 1 — sources, extraction specs, and anchors (committed BEFORE any value check)

**File 1: kilian_replication_raw.xlsx** — from github.com/mauep2025/Global-Oil-Market
(third-party Kilian-2009 replication repo; sheet columns Data/RAC/WTI/Oil_Prod/Oil_Inv/
Kilian_Index/Hamilton_Index, monthly 1973-01..2019-06, 558 rows). Provenance chain:
Kilian/Dallas-Fed series → a replication author's workbook → GitHub — a WEAK chain (the
TradingView class); the anchors below carry the admission. Extraction: Data + Kilian_Index
only → kilian_index_monthly_1973_2019.csv; the price/production columns are NOT consumed
and are NOT authenticated. Disclosure: rows 0-2 of the sheet were seen during format
inspection (Kilian_Index −8.32, −3.54, +14.35) — early-1973 rows serve as no anchor.

**File 2: oil_supply_news_2025M12_raw.xlsx** — from github.com/dkaenzig/oilsupplynews,
THE AUTHOR'S OWN distribution repo for Känzig (2021 AER) oil-supply-news shocks, vintage
2025M12; sheets Daily / Monthly (+pre-Covid variants); Monthly = 612 rows 1975M01..2025M12
(surprise + VAR news shock). Provenance: effectively primary (author-maintained). Extraction:
Monthly sheet → oil_supply_news_monthly_1975_2025.csv; Daily sheet → consumed only for the
sign anchors below. Disclosure: sheet names, column names, row counts and END DATES were
seen during format inspection; no shock VALUES were read.

Anchors — bars stated BEFORE values are read (scale-free where the series' units are
uncertain):

| # | File | Anchor | Bar |
|---|---|---|---|
| K1 | Kilian | pre-GFC global boom = the sample's activity top | sample MAX month falls in 2007-01..2008-10 |
| K2 | Kilian | GFC collapse | window 2008-10..2009-12 contains a bottom-decile value of the full sample |
| K3 | Kilian | first-oil-shock recession | window 1974-01..1975-12 contains a bottom-quartile value |
| K4 | Kilian | cross-vault co-movement | Spearman(Kilian_Index, PCPS All-Commodity YoY%) ≥ 0.25 monthly over the 1981-2017 overlap |
| K5 | Kilian | structure | 558 contiguous months 1973-01..2019-06; both signs present; all |values| ≤ 300 |
| Z1 | Känzig | 2014-11-27 OPEC "no cut" (price collapse) | daily surprise on that date NEGATIVE |
| Z2 | Känzig | 2016-11-30 Vienna cut agreement (price jump) | daily surprise on that date POSITIVE |
| Z3 | Känzig | 2020-03-06 OPEC+ collapse (price war) | daily surprise on that date NEGATIVE |
| Z4 | Känzig | structure | Monthly sheet 612 rows 1975M01..2025M12; monthly news-shock |mean| < 0.5 × its std |

Admission rule (stated now): each file admits on ITS OWN anchors (Kilian needs K1-K5
majority with K1 mandatory; Känzig needs Z1-Z4 all, given its primary-grade chain);
a miss is recorded, never re-barred.
