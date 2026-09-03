# AUTHENTICATION — India VIX daily, 2010-2023 (TradingView export mirror)

## Two-pass protocol (near-miss #4 discipline)
Pass 1 (this section) is written and committed BEFORE any anchor value is checked.
Pass 2 (appended after) records each anchor's PASS/MISS. Bars are never edited after pass 2.

## Source and provenance chain
- File: `NSE_INDIAVIX, 1D.csv` from github.com/Gaurav7888/Predicting_Market_Volatility
  @ commit `1ee886e65b63ac60398b09a6b71bcd2b12fd9a2a` (uploaded 2023-04-08 IST).
- Chain: NSE (primary) → TradingView aggregation (NSE:INDIAVIX daily bars) → a user's chart
  export (with indicator columns) → GitHub. **This is the weakest provenance chain admitted
  to any vault so far** — one hop longer than the Kaggle-mirror panels. The anchors below
  carry the full weight of admission; a majority-anchor failure refuses the file.
- Status vs the runsheet: the Priority-1 India VIX pull (NSE archive, 2009-, via
  `ingest/pull_india_vix.py`) remains REQUIRED and unsubstituted. This mirror can only
  PARTIALLY discharge registered designs, exactly like the NIFTY 50 / bhavcopy precedent.
  Mirrors never outrank primary pulls.

## Extraction spec (fixed before extraction)
- Keep columns: `time,open,high,low,close`. Drop all TradingView indicator columns
  (Chars/Shapes/SuperTrend/Buy/Sell/Volume/HV etc. — chart overlays, not exchange data).
- `time` is epoch seconds at bar open; convert to IST (UTC+05:30) calendar date.
- Expected shape: ≈3,142 data rows, spanning 2010-07 .. 2023-04.
- Output: `india_vix_daily_2010_2023.csv` (`date,open,high,low,close`), manifested alongside
  the raw file (WORM).

## Disclosure (pass-1 honesty)
During format inspection the first and last 3 rows were necessarily seen (head close 19.24
on the first row; tail closes 12.935/12.585/12.725). Those rows are therefore EXCLUDED from
serving as anchors; every anchor below was chosen from the public record independent of the
file's contents.

## Anchors — bars stated BEFORE values are read
| # | Anchor | Bar | Basis (public record) |
|---|---|---|---|
| A1 | COVID panic peak | close on 2020-03-24 ∈ [82, 85] AND equals the sample max close | India VIX all-time closing high ≈83.6 printed 24-Mar-2020, the day after the NIFTY −12.98% crash low (our index vault's 2020-03-23 anchor) |
| A2 | China-deval Black Monday | close on 2015-08-24 ∈ [26, 30] | reported ≈+64% spike to ≈28.1 on 24-Aug-2015 |
| A3 | Yearly completeness | every calendar year 2011-2022 has 240-252 rows | NSE trading calendar ≈245-252 sessions/yr |
| A4 | Sanity structure | all closes ∈ (7, 100); dates strictly increasing; no duplicate dates | India VIX has never printed single digits below ~8 nor above 100 |
| A5 | Vol-mageddon spillover | max close over 2018-02-01..2018-02-15 ∈ [17, 23] | India VIX rose to ~20 in the first week of Feb-2018 (US VIX spike spillover + LTCG budget) |
| A6 | Cross-vault co-movement | Pearson correlation of monthly last closes with the authenticated CBOE VIX vault (overlap 2010-08..2023-03) ≥ 0.55 | implied-vol indices co-move; India VIX uses the CBOE VIX methodology (NSE white paper) |

Special-session check (reported, not barred): TradingView exports sometimes omit NSE's
Saturday special sessions. Presence of 2015-02-28 and 2020-02-01 (Saturday Union Budget
sessions) is CHECKED and REPORTED in pass 2; if absent, the CW-D1v event day maps to the
next trading day — stated at that design's registration, before its run.

<!-- PASS 2 IS APPENDED BELOW THIS LINE, AFTER COMMIT -->

## Pass 2 — results (2026-09-03, script: scripts/extract_india_vix.py)
Extraction: 3,142 rows, 2010-07-23 .. 2023-04-05, as specified.

| # | Result | Verdict |
|---|---|---|
| A1 | 2020-03-24 close = **83.6075** = sample max (the published all-time closing high, matched to 4 decimals) | **PASS** |
| A2 | 2015-08-24 close = 28.13 (bar [26, 30]) | **PASS** |
| A3 | yearly rows 2011-2022 all ∈ [243, 252] | **PASS** |
| A4 | closes ∈ [10.45, 83.61]; dates monotone; 0 duplicates | **PASS** |
| A5 | Feb-2018 window max = 20.01 on 2018-02-06 (bar [17, 23]) | **PASS** |
| A6 | monthly level corr with CBOE VIX vault = **0.728** over 154 months (bar ≥ 0.55) | **PASS** |

**6/6 PASS — ADMITTED.** Saturday budget special sessions 2015-02-28 and 2020-02-01 both
PRESENT (reported check). Sample min close 10.45 (within A4's structural band; no anchor
claimed the exact low). The provenance chain remains the weakest admitted — the anchors,
not the chain, carry this admission; the NSE primary pull stays on the runsheet.
Coverage limits carried by every consumer: starts 2010-07-23 (misses the 2009 head), ends
2023-04-05 (misses the 2024 election spike and everything after) — every design run on this
vault is a PARTIAL of its parent and says so.
