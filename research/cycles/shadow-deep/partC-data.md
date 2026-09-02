# Part C — Data engineering: the funding-freeze variables, free (atlas 2.2)

*v1.0 · 2026-09-01 · desk principal's compact chapter (the entry's data surface is narrow —
funding variables — so this Part is written in-house; the per-source discipline follows the
house style of the sibling Part C chapters).*

The entry owns ONE new measurement job: the funding-freeze signature that feeds L2. The
composition side (NBFC share of credit) is already engineered in credit-deep partC (bank+NBFC
netting rule) — cross-referenced, not rebuilt. Everything below is a candidate INPUT to L2's
stress family, daily/weekly cadence, reduce-only consequences.

## C.1 CP market — the run's native variable

| Item | Source | Cadence / lag | Notes |
|---|---|---|---|
| CP outstanding, fortnightly issuance | RBI Weekly Statistical Supplement (WSS) + RBI Bulletin "Money Market" tables | weekly / ~1w | THE freeze variable: rollover collapse shows as outstanding falling while rates spike |
| CP/CD primary rates by rating/tenor | RBI Bulletin; FBIL money-market benchmarks | monthly (bulletin) / daily (FBIL) | spread over T-bill of matching tenor = the price of rollover risk [VERIFY FBIL CP curve free-access history depth] |
| CP/CD secondary trades | CCIL F-TRAC public dissemination | daily / T+0 | volume evaporation is itself the signal; portal likely proxy-blocked here — runsheet item |
| 91d T-bill (the spread's base leg) | RBI WSS / auction results | weekly | already in the debt-deep pull list — no duplication |

Construction: **freeze index = z(CP spread, 3m tenor, top-rated) + z(−rollover ratio)** where
rollover ratio = fresh issuance / maturing amount (both from WSS fortnightly tables). The two
z's on expanding windows (shared grids); daily FBIL leg when available, weekly WSS leg always.
Warm-up: WSS CP tables are continuous from the 2000s — ranks mature quickly at weekly cadence.

## C.2 Debt-MF chain — the holder's side

| Item | Source | Cadence / lag | Notes |
|---|---|---|---|
| Debt AUM by category (liquid, credit-risk, corporate bond) | AMFI monthly AUM releases | monthly / ~1w | category redemptions = the run, one step removed; liquid-fund AUM drops led both 2013 and 2018 stress [VERIFY lead precisely on pull] |
| Scheme portfolio disclosures (issuer-level CP holdings) | AMFI/fund-house monthly portfolios | monthly / ~10d | the EXPOSURE map: which funds hold whose paper; heavy engineering, Phase-2 of the runsheet |
| NAV history | portal.amfiindia.com NAVAll (ingest/pull_amfi.py, UNTESTED LIVE) | daily | side-pocket events appear as NAV discontinuities — breaks registry entries, never silent |

## C.3 The lender itself — NBFC returns and supervisory data

RBI FSR (half-yearly) NBFC chapter: sector CRAR, GNPA, funding-mix shares (CP dependence %),
ALM buckets — the SLOW confirmation layer (lag ~6m; regime documentation, never L2 input).
RBI's scale-based "upper layer" list (annual) = the watch list of systemic names. Ratings
actions from public rationales (Crisil/ICRA/CARE sites) are LAGGING confirms only — the
IL&FS lesson is codified: a rating is never an input, only a post-mortem variable.

## C.4 PIT/vintage hazards

| Hazard | Reality | Rule |
|---|---|---|
| WSS table reformatting | RBI reorganizes WSS periodically | breaks registry entry per reformat; puller pins table names per vintage |
| AMFI category redefinition | SEBI's 2017-18 scheme categorization re-drew every category series | pre/post-2018 category series never spliced silently |
| FBIL benchmark methodology | revisions documented by FBIL | registry entries; spread construction pinned to methodology vintage |
| Side-pockets/gates | NAV series survivorship | side-pocketed units tracked as separate series, never dropped |

## C.5 What cannot be measured free
Issuer-level rollover calendars (who matures next week) — the run's true fuse — are visible
only in aggregate; inter-corporate deposit markets are dark; bank lines' undrawn status is
quarterly at best. Stated once: the freeze index detects the fire, not the first spark.

## C.6 Runsheet addendum 8 (continuing from addendum 7's step 45 [VERIFY last number])
46. WSS money-market tables backfill (CP outstanding/issuance/rates, weekly, 2000s→) ~4-6h
47. FBIL money-market benchmarks daily pull + methodology-vintage registry ~3-4h
48. AMFI monthly AUM-by-category backfill (post-2018 categories; pre-2018 kept separate) ~3-4h
49. pull_amfi.py first live test + NAVAll daily cron + side-pocket break rules ~2-3h
50. CCIL F-TRAC access test from the principal's machine; daily CP/CD trade pull if open ~3-4h
51. Freeze-index assembly + SC2 acceptance registration (BEFORE any backtest look) ~4-6h
Total ~19-27h. SC2's acceptance bars are registered at step 51 against L2's stress dates,
per the two-pass rule — the design is in the ledger, the bars wait for the data.
