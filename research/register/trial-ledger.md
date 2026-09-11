# Cumulative trial ledger (CONTRACT §9 — deflated Sharpe uses the TRUE count, program-wide, never reset)

Opened 2026-08-31, at design time — before any test has run. Every grid a sweep will touch is
logged BEFORE it runs; the deflated-Sharpe N is the cumulative product/sum of everything below
plus whatever is added later. Undercounting this ledger silently voids every significance claim.

| # | Sweep family | Grid size (committed at design) | Owner section | Status |
|---|---|---|---|---|
| 1 | Hedge ratio × regime bucket | 7 × 4 = 28 cells | DESIGN §5.5 | pre-registered, not run |
| 2 | DD-violation test (z × K) | 3 × 3 = 9 | DESIGN §5.6 | pre-registered, not run |
| 3 | Grossman-Zhou α × response f | broad grid, size TBD before run | DESIGN §5.4 | to be sized before run |
| 4 | Hamilton filter h (two bands) | ~5 × 2 = 10 | DESIGN §11.1 | pre-registered, not run |
| 5 | τ_ref (band-width anchor) | grid TBD | DESIGN §7.3 | to be sized before run |
| 6 | f_Kelly ∈ [0.15, 0.35] | grid TBD | DESIGN §7.4 | to be sized before run |
| 7 | Cushion exponent p | small grid incl. p=1 | DESIGN §7.4 | to be sized before run |
| 8 | Participation cap per rank bucket | 5 buckets × grid | DESIGN §9.2 | to be sized before run |
| 9 | Impact coefficient Y ∈ [0.5, 1.0] | sweep | DESIGN §9.2 | to be sized before run |
| 10 | Momentum construct variants (12-1, 6-1, 52wk blends) | ~6–8 pre-registered constructs | D01 §6 | pre-registered, not run |
| 11 | Factor-weight grid (value/quality/low-vol/size ranges) | TBD before run | DESIGN §6.2 | to be sized before run |
| 12 | Stage-2 rung thresholds / reference forecaster | fixed pre-launch (not swept) | DESIGN §8 | frozen at design |
| 13 | Regime-score block-weight split (6 blocks) | grid TBD before run | config/ladder.yaml budgets (red-team: the split is a design choice, must be swept) | to be sized before run |
| 14 | DD-test TE window W ∈ {30, 60, 90} sessions | 3 | DESIGN §5.6 / mandate.yaml | pre-registered, not run |

Rules: a rejected hypothesis is retired permanently (no re-test with tweaked parameters);
re-opening requires a new mechanism argument as a NEW ledger entry carrying its own count;
sweep families share one cumulative N — they are not separately-budgeted pools.

## Entries J1–J5 (2026-09-01) — JST R6 pooled panel, first real data
Data: JST R6 GitHub mirror (sha256 in ingest/vault/jst/manifest.json; authenticated vs independent
R4 mirror + published crisis chronologies). Script: scripts/analyze_jst_panel.py. Purpose: pooled
PRIORS + replications for L10 (pre-registered in docs/cycles/01-credit-cycle.md §5). NOT India.

| # | What | Cells | Result (headline) | Status |
|---|---|---|---|---|
| J1 | Real-time credit-state AUROC, h grid {4,5,6}y × horizons {3,5}y + ST-growth benchmark | 8 | 0.62–0.65 pooled; per-country median 0.667, 14/18 > 0.5. THE honest number: real-time expanding construction gives ~0.64, NOT the published full-sample 0.83–0.85 — our India prior band 0.65–0.75 [A] is validated at its lower half | prior set |
| J2 | ST-style logit replication (5y avg real credit growth, country FE, crisis≤3y) | 1 | +3.15pp per 1σ on 9.4% base (published: ~+2.8pp); AUROC 0.679 | replicated |
| J3 | R-zone replication (business + total variants, full-sample quantiles) | 2 | business: 27.2% vs 7.8% base (3.5×); total: 15.5% vs 10.1%. Direction confirmed, magnitude below published 45%/7% | replicated (weaker) |
| J4 | Fwd 3y REAL equity max-DD by state quintile | 1 | U-shaped: Q1 19.0%, Q2–Q4 12–14%, Q5 17.1%. NOT monotone — low states are post-bust aftermath years. Design: L10 harvests TOP-state de-risk only; low state ≠ safe-to-lever | prior set (nuance) |
| J5 | H66 preliminary: U vs D at matched level [0.55,0.90] | 1 | Crisis prob ~equal (6.0% vs 6.7%); fwd DD ~equal; but median fwd 3y REAL return D +22.5% vs U +13.1%. Phase asymmetry may live in RE-RISKING (returns), not crisis prediction. Exploratory only | H66 prior noted, stays open |

Method notes on the record: first run crashed on NaN (hamilton_filter hardened + test added);
first J4 run used NOMINAL equity returns and produced a +5.9e10% Weimar cell — switched to
CPI-deflated real returns (script comment documents it). Total new ledger trials: 13 cells.

## Entries M0–M5 (2026-09-01) — momentum real data (India factor mirror + US crash replication)
Data: ingest/vault/factors (3 files, sha256-manifested). Script: scripts/analyze_momentum_panels.py.

| # | What | Result (headline) | Status |
|---|---|---|---|
| M0 | Authentication | India mirror: worst months = published crash set (Nov-01 −27.6%, May-09 −25.0%). US pair correlation 0.892 vs pre-stated 0.9 bar — **MISS recorded**; accepted on the independent chronology axis (worst-6 = exactly the published set) with [VERIFY] on the construction-difference explanation | accepted-with-note |
| M1 | India WML level + decay | Full-period +13.4%/yr (24.5% vol). Post-2015 mean +13.2% ≈ 1994-2014 +13.1% (no mean decay) but vol HALVED → Sharpe 0.21→0.51. Mirror-level caveat: 21.9%/yr in secondary literature unreconciled [VERIFY]. Standing 25-35% forward haircut UNCHANGED (it prices future decay, not just realized) | prior set |
| M2 | India DM conditional | Crash zone (bear & mkt-up): −2.24%/m vs +3.93 (bear & down), +1.39 bull. The option-payoff signature confirmed on India | replicated |
| M3 | US DM conditional 1927-2025 | Crash zone −4.59%/m vs +6.85 (bear & down). Textbook | replicated |
| M4 | Our crash_guard on real US months | ON −2.19%/m (n=95) vs OFF +1.81 (n=1069); crash tail lives in guard-ON. Mirrors the synthetic test | validated |
| M5 | Vol-managed WML (BSC direction) | Sharpe 0.77→1.29, maxDD 83%→29% (12% target, 2x cap). Direction matches BSC 2015 | replicated |

## Entries V0–V4 (2026-09-01) — value real data (India HML mirror + US Fama-French)
Script: scripts/analyze_value_panels.py. New vault file: fff_monthly_us.csv (FF3, 202411 CRSP).

| # | What | Result (headline) | Status |
|---|---|---|---|
| V0 | US HML authentication | Chronology exact (worst Mar-20 −13.9%, best Jul/Aug-32 +35.6/+34.2) | accepted |
| V1 | India HML level/sub-periods | Full +8.6%/yr but Sharpe vs RF only 0.09 (Indian RF high); 2015-19 growth mania +0.8%/yr Sh −0.39 (the India value winter, confirmed); post-2020 +18.8%/yr Sh 0.82 | prior set |
| V2 | Value-momentum correlation | India −0.37, US −0.41 — AMP's diversification claim confirmed on both panels by us | replicated |
| V3 | Combination arithmetic | 50/50 Sharpe beats BOTH legs both panels (US 0.72 vs 0.33/0.45; India 0.86 vs 0.42/0.55) | prior set (feeds sleeve-weight prior) |
| V4 | Value winters | US: 8 episodes >20%, incl. post-2009 58% STILL OPEN at 202411; India: 5 episodes incl. 2018-2022 50% | prior set (spread-conditioned patience rule) |

## Entries DS1–DS4 (2026-09-01) — Atlas 0.1 debt supercycle, JST R6 (advanced-economy priors)
Script: scripts/analyze_debt_supercycle.py. Purpose: L15 priors (Tier C, reduce-only).

| # | What | Result (headline) | Status |
|---|---|---|---|
| DS1 | Completed fiat-era deleveragings | 4/18 countries completed a >=30pp lasting decline from a pre-2000 peak; 11/18 peaked in 2020 (censored, still ascending) — the atlas's "n<2" is conservative-but-right in spirit: the current arc is UNRESOLVED almost everywhere | prior set |
| DS2 | Repression eras | Negative-real-rate share: 1945-80 = 44%; 1981-2007 = 10%; **post-GFC 2008-20 = 76%** — the modern echo exceeds the classic era on this measure | replication-lite (R-Sbrancia direction) |
| DS3 | r − g by era | Repression era −4.3pp (r<g in 83% of years); post-GFC −1.0pp (73%) — the painless-arc arithmetic is ON in the modern era | prior set |
| DS4 | Investor translation | Fiscal-dominance state (high debt + negative real rates): mean real equity +4.5% vs +9.5-10% in positive-real-rate states — halved but POSITIVE: gold floor + tail budget justified, equity exit not | prior set (L15 rationale) |

## Entry DS5 (2026-09-01) — the RR 90% cliff, re-run on the HAP panel
Data: ingest/vault/debt/RR-processed.csv (Herndon-Ash-Pollin replication panel, vault-manifested).
Script: scripts/analyze_rr_cliff.py. Result: pooled mean growth at debt>90% = **+2.17%** (HAP
published 2.2%; RR 2010 claimed −0.1%); 60-90 vs >90 gap +1.02pp, bootstrap CI [+0.26, +1.77] —
a modest gradient, NO cliff, no negative bucket. Canonical justification for the no-threshold-
cliffs design rule. Status: replicated (near-exact).

## Entries RC0–RC3 (2026-09-01) — Atlas 0.2 reserve currency, IMF COFER mirror
Script: scripts/analyze_reserve_currency.py. Data: cofer_1995_2023q1.csv (vault).

| # | What | Result (headline) | Status |
|---|---|---|---|
| RC0 | Authentication | 1999Q1 USD 71.2%, 2021Q4 58.8% — match the published AESB anchors exactly | accepted |
| RC1 | The drift, measured | −0.51pp/yr average 1999-2023; ~57 more years to sterling's 30% endgame at this pace — the century-scale claim in one number | prior set |
| RC2 | Where it went | Not to one challenger: EUR +1.6pp, GBP +2.1, RMB +1.5, AUD/CAD/Other +3.5 — diversification at the margin (AESB reproduced); gold outside COFER entirely | replicated |
| RC3 | Accelerating? | No, in FX shares: post-2015 −0.23pp/yr vs pre-2015 −0.69; the 2022 sanctions response lives in CB GOLD (WGC leg, runsheet) | prior set |

## Entries SR1–SR3 (2026-09-01) — Atlas 0.3 suprasecular real rates, JST R6
Script: scripts/analyze_real_rates.py.

| # | What | Result | Status |
|---|---|---|---|
| SR1 | 150y pooled trend | −1.27bp/yr — independently inside Schmelzing's 700y −1 to −2bp/yr band; decade medians swing −2.1% (1940s) to +5.1% (1870s) | replicated (order-of-magnitude) |
| SR2 | Swings vs trend, 30y horizon | Median country range of rolling 30y means = 5.4pp vs the trend's 0.38pp per 30y: **14x** — the single number that settles the CONTEXT-only verdict | verdict confirmed |
| SR3 | The 2010s in context | Median +0.5% = 27th percentile since 1870 — low, not unprecedented; keeps company with the 1910s/1940s war/repression eras | prior set |

## Entries GC1–GC3 (2026-09-01) — Atlas 0.4 golden constant (1915-2020 mirror + JST CPI)
Script: scripts/analyze_golden_constant.py. Authentication: $20.67/$35/1980-$608 anchors match.

| # | What | Result | Status |
|---|---|---|---|
| GC1 | The century anchor | +1.31%/yr real over 1915-2020 (ends mid-bull); departures −57% (1970) to +267% (2012) | prior set |
| GC2 | Reversion half-life | rho_corrected = 1.000: indistinguishable from a random walk on 105 annual obs — NO measurable reversion. Pre-written "halves in a decade" text falsified (instance #3, verification log) | honest null |
| GC3 | Decades off anchor | 58% of years >±50% from anchor; longest stretch 22 years | prior set (ceiling/floor sizing rationale) |

## Entries IR1–IR3 (2026-09-01) — Atlas 0.5 inflation-regime arcs, JST R6
Script: scripts/analyze_inflation_regimes.py.

| # | What | Result | Status |
|---|---|---|---|
| IR1 | The arcs, dated mechanically | Up-arc 1930 (−2.1% rolling-10y) → 1982 peak (+10.4%) = 52y; down-arc 1982 → 2020 trough (+1.2%) = 38y. TWO completed fiat-era arcs — regime object, clock test fails by an order of magnitude | prior set |
| IR2 | Era stickiness | P(same >4%/≤4% state next year) = 81% pooled — eras persist, prints don't; the design's persistence-gauge choice justified | prior set |
| IR3 | Investor outcomes | Cross-referenced to DS2/DS4/SR1 — no re-runs, no new seat: the information already flows through L15 + L6 | scope discipline |

## Entries DG1–DG2 (2026-09-01) — Atlas 0.7 demographics, JST R6
Script: scripts/analyze_demographics.py.

| # | What | Result | Status |
|---|---|---|---|
| DG1 | Crude size-growth → forward 10y real equity | Pooled corr −0.03 (n=1,977); era signs flip (+0.22 / −0.14 / −0.08); 4/16 countries positive, median −0.26 — sign-inconsistent everywhere. "Superbly measured, weakly tradable" is now measured. Age-structure version pre-registered (UN WPP runsheet) with the same sign-consistency bar | verdict confirmed |
| DG2 | India's window | Context marker only — L16 zero allocation authority, 2030 review; jobs-absorption condition datable only in retrospect | scope discipline |

## Entries FC1–FC3 (2026-09-01) — Atlas 1.1 financial cycle, JST R6
Script: scripts/analyze_financial_cycle.py. Grid cells ledgered: FC3 peak thresholds {0.6, 0.8}.

| # | What | Result | Status |
|---|---|---|---|
| FC1 | Credit-property co-movement | corr(5y Δcredit/GDP, 5y Δlog real HP): median +0.40, **17/17 countries positive** — the cleanest sign-consistency pass in the project (contrast demographics' 4/16) | replicated (strong) |
| FC2 | Length pre/post-1985 | Peak spacing 11y → 13y — Drehmann-Borio's lengthening DIRECTION on our cruder tool; feeds H65b lengthening watch | direction confirmed |
| FC3 | Crises at peaks | Loose peaks 22% vs 18% base (1.2x); major peaks 23% (1.3x) — WEAK with our real-time construction; interpretation written after the print. Peak-DATING stays out of bounds; the seat's evidence rests on FC1 + the credit AUROC work | honest weak |

## Entries RE1–RE2 (2026-09-01) — Atlas 1.2 real-estate cycle (merge entry), JST R6
Script: scripts/analyze_realestate.py. PRE-REGISTERED before running (this block written first;
results column filled after the print, per the standing rule).

Pre-declared constructions and pass bars:
- RE1 (folk 18-year claim): peaks of REAL house prices (hpnom/cpi, 3y centered smooth, local max,
  min_gap 8y — half the claimed period). The fixed-period claim PASSES only if (a) pooled median
  peak-to-peak spacing lies in [14, 22]y AND (b) ≥50% of all spacings fall in [14, 22]y. Grid: the
  min_gap cell {8} only (declared; no other cells will be tried).
- RE2 (Kuznets 15–25y swing): same construction on investment/GDP (iy). Claim PASSES only if
  (a) pooled median spacing in [15, 25]y AND (b) ≥50% of spacings in [15, 25]y. Also report
  pre-1950 vs post-1950 split (Abramovitz's "passing" claim predicts the swing weakens post-war;
  direction only, no bar).

| # | What | Result | Status |
|---|---|---|---|
| RE1 | 18-year folk cycle spacing test | median 14y (in [14,22]) but share in-window 45% < 50% — **FAIL**, informatively: length real (IQR 10-17y), FIXED period dies; per-country medians 10-20y; min_gap bias favored the claim | fail, bar unmoved |
| RE2 | Kuznets swing spacing test | median 11y, share 25% — **FAIL** clean; pre/post-1950 12y→11y (no 'passing' direction on this tool; tool-limits noted) | fail, bar unmoved |

## Entries CS1–CS4 (2026-09-01) — Atlas 1.3 commodity supercycle, Jacks 1850-2015 + Clio/USGS
Script: scripts/analyze_commodity_supercycle.py. PRE-REGISTERED before running (two-pass rule
per verification-log near-miss #4: this block first, results filled only after the print).

Pre-declared constructions and bars:
- Index: equal-weight mean of log real prices (Jacks, 1900=100), per year over available
  series; also group indices {energy, metals, agriculture} by the file's natural grouping.
  Peaks/troughs machinery identical to RE1 (3y centered smooth, local extrema) with min_gap
  15y (half the low end of the claimed 30-40y trough-to-trough period).
- CS1 (existence/shape): the Erten-Ocampo-style claim "3-4 supercycles 1870-2015, trough-to-
  trough 30-40y". Bar: count of broad-index troughs in [3,5] AND median trough-to-trough
  spacing in [25,45]y. Grid: min_gap {15} only.
- CS2 (breadth/common factor): supercycles are claimed BROAD. Measure median pairwise corr of
  10y Δlog real prices within groups vs across groups. Bar: pooled across-group median > 0
  and at least half the across-group pairs positive. (Direction/consistency, not size.)
- CS3 (mechanism, price→capacity): corr of 10y Δlog real price with the NEXT decade's Δlog
  world production, per metal (matched Jacks price × Clio/USGS World production). Bar:
  sign-consistency ≥ 70% of matched metals positive.
- CS4 (mechanism, capacity→glut): corr of 10y Δlog production with the NEXT decade's Δlog
  real price, per metal. Bar: sign-consistency ≥ 70% negative.

| # | What | Result | Status |
|---|---|---|---|
| CS1 | Supercycle existence/shape | 8 troughs 1870-2015, spacings 15-21y, median 18y — **FAIL** the 3-5/30-40y literature claim; measured spacing lands on the ATLAS prior (15-20y); canonical supercycles = alternate arcs of the finer sequence | fail, informative |
| CS1b | Same, chained-Δlog index (composition-robust variant; declared before running — the plain mean-of-available-logs can jump when series enter; SAME bar) | identical trough chronology to CS1 — **FAIL** the same way; composition artifact ruled out | fail, robust |
| CS2 | Breadth (common factor direction) | across-group median corr(10yΔ) +0.30, 89% of 451 pairs positive (within-group +0.42) — **PASS**; the ToT-state design measures a real broad factor | pass |
| CS3 | Price → next-decade capacity | 6/11 metals positive (55% vs 70% bar) — **FAIL**; production trend-dominated at decade windows; detrended event design registered for later, NOT re-run now | fail, bar unmoved |
| CS4 | Capacity → next-decade price | 7/11 negative (64% vs 70% bar) — **FAIL** (near miss recorded as a miss); same trend caveat | fail, bar unmoved |

## Entries KW1–KW2 (2026-09-01) — Atlas 1.4 Kondratieff rejection, Jacks 1850-2015 + JST R6
Script: scripts/analyze_longwaves.py. PRE-REGISTERED before running (two-pass rule).

Pre-declared constructions and bars:
- KW1 (K-wave on real commodity prices): chained Jacks index (CS1b construction, unchanged),
  extrema machinery as RE1/CS1 (3y centered smooth, local extrema), min_gap 25y (half the
  claimed 50y midpoint). The claim PASSES only if trough count since 1850 is in [2,4] AND
  ≥50% of trough spacings fall in [45,60]y. Grid: min_gap {25} only.
- KW2 (Kondratieff's actual object, price waves): JST cpi → rolling 10y mean inflation for
  the three countries Kondratieff himself used (UK, USA, France), full available spans;
  same extrema machinery, min_gap 25y. Claim PASSES only if pooled median trough spacing in
  [45,60]y AND ≥50% of spacings in-window. Fiat-era caveat stated in advance: proponents
  claim the wave CONTINUED post-1971, so the full span is the honest test of their claim.

| # | What | Result | Status |
|---|---|---|---|
| KW1 | 45-60y wave in real commodity prices | 6 troughs spaced 26-31y, 0/5 in [45,60] — **FAIL**; no min_gap lands on the K-band (paired with CS1's 15-21y) | fail, decisive |
| KW2 | 45-60y price/inflation waves (UK/US/FR) | synchronized generational inflation peaks REAL (~1920/1949/1982/2010) but spacings 25-41y (median 36y, 1/10 in-window) — **FAIL**; decomposes into the already-seated inflation-regime arcs (IR1) | fail, informative |

## Entries IN1–IN3 (2026-09-01) — Atlas 1.6 capex cycle (seat L11), JST R6 analogues
Script: scripts/analyze_capex_cycle.py. PRE-REGISTERED before running (two-pass rule). India
official series (OBICUS/IIP/GFCF) are proxy-blocked here → the atlas's own "C→B via analogues"
clause governs: pooled JST iy (investment/GDP, 18 countries) + vaulted jst_real_returns.

Pre-declared constructions and bars:
- State: expanding Hamilton gap of iy (annual h from the shared {4,5,6} grid at midpoint 5,
  p=1) → expanding percentile (min_obs 20). Identical machinery to the seated entries.
- IN1 (overbuild → weak forward returns, the seat's core claim): per-country corr of the
  capex state with FORWARD 5y cumulative real equity return. Bar: ≥70% of countries with
  ≥40 overlapping years NEGATIVE.
- IN2 (repair takes years): after each iy peak (extrema machinery, min_gap 8y), years until
  iy regains the peak level (censored at sample end = counted at censoring value, stated).
  Bar: median recovery ≥ 4 years ("balance-sheet repair takes years no information flow can
  shortcut").
- IN3 (the non_positive clamp's justification — asymmetry): pooled mean forward-5y real
  equity return in top-quintile capex state vs bottom-quintile. MEASUREMENT (prior set), no
  bar: the clamp is a design decision already made on consistency-audit grounds; IN3 records
  what the analogue panel says about it.

| # | What | Result | Status |
|---|---|---|---|
| IN1 | Capex state → forward 5y real equity | 9/15 countries negative (60% vs 70% bar) — **FAIL**; between DG1 (4/16) and FC1 (17/17) on the project's scale; C→B NOT triggered, L11 stays Tier C | fail, calibrating |
| IN2 | Post-peak repair length | 195 spells, median 4y (bar ≥4y) — **PASS at the bar**; IQR 1-12y; censoring counted against the claim as pre-stated | pass, marginal |
| IN3 | Top-vs-bottom quintile asymmetry | top +0.242 < bottom +0.287 (mild overbuild penalty ~0.9%/yr) but middle +0.202 lowest — NON-monotone; the non_positive clamp's design now has analogue numbers behind it | measured, prior set |

## Entries SC1–SC2 (2026-09-01) — Atlas 2.2 NBFC/shadow-credit sub-cycle
Script: scripts/analyze_shadow_credit.py (SC1); SC2 is a DESIGN (runsheet-gated). PRE-REGISTERED
before running (two-pass rule). Data: vaulted iima_monthly_factors.csv (1993-10..2025-12).

Pre-declared construction and bars:
- SC1 (the funding-run factor signature): the mechanism says an NBFC funding freeze is a
  CREDIT-SUPPLY event concentrated in small/funding-dependent firms, not a broad macro crash.
  Windows (fixed): IL&FS crunch 2018-09..2019-08. Comparators (context prints, no bars):
  GFC 2008-09..2009-08, taper 2013-05..2014-04, COVID 2020-02..2021-01.
  Claim PASSES only if BOTH: (a) SMB 12m cumulative return in the crunch window is in the
  BOTTOM DECILE of all rolling 12m SMB windows (1994+); (b) MF (market) in the same window is
  NOT in its own bottom decile. Both bars fixed before looking.
- SC2 (design, not run): CP-spread freeze signature vs L2 stress dates — needs CCIL/RBI WSS
  pulls (runsheet); acceptance to be registered when the data lands.

| # | What | Result | Status |
|---|---|---|---|
| SC1 | IL&FS window: SMB bottom-decile AND market not | SMB −24.8% (18th pct), market −20.2% (16th) — **FAIL**: the freeze propagated to a broad macro event within 12m; that is the CASE for routing the signature to L2 (faster variables), not for equity-factor detection | fail, informative |
| SC2 | CP-freeze signature vs L2 | (design only) | runsheet-gated |

## Entries BC1–BC3 (2026-09-02) — Atlas 2.3 business cycle proper, JST R6 analogues
Script: scripts/analyze_business_cycle.py. PRE-REGISTERED before running (two-pass rule).
Series: rgdpmad (real GDP per capita, Maddison line in JST). India is NOT in JST — these are
the analogue calibrations behind a CONTEXT entry; India dating itself is the cases chapter's
job (Dua-Banerji chronology) and the nowcast surface is runsheet-gated.

Pre-declared constructions and bars:
- State: expanding Hamilton gap of log rgdpmad (h=2y annual for the SHORT cycle — declared
  here as the business-cycle band's own h, distinct from the medium-cycle h=5; p=1) →
  expanding percentile (min_obs 20). Extrema machinery as before, min_gap 2y.
- BC1 (the 4-5y claim): pooled peak-to-peak spacing of the growth-cycle state. Bar: median
  spacing in [3, 6]y AND ≥50% of spacings in [3, 7]y.
- BC2 (the imported "credit leads growth" direction): per country, peak of the cross-
  correlation between the credit gap (credit monograph construction, h=5) and the GDP gap
  (h=2) over lags −5..+5y (positive lag = credit leads). Bar: ≥60% of countries with ≥60
  overlapping years show peak at lag ≥ +1y. If this FAILS, the imported direction is shaky
  even on its home panel — the Saini caution generalizes.
- BC3 (persistence, measurement, prior set): P(state stays on the same side of 0.5 next
  year), pooled — the growth-regime stickiness number, no bar.

| # | What | Result | Status |
|---|---|---|---|
| BC1 | Growth-cycle spacing vs the 4-5y claim | median 6y, 65% in [3,7]y — **PASS**; the band exists on real-time machinery | pass |
| BC2 | Does credit lead growth on the home panel? | **FAIL, 11%** — 16/18 countries peak at NEGATIVE lags (−3..−5): GDP leads credit at cycle frequency almost everywhere; the Saini India finding generalizes. Caveats logged (h mismatch, grid-edge pinning, location-only) — none rescue the import. STANDING WARNING added: imported lead-lag directions are hypotheses, never assumptions; J1's crisis-AUROC claim untouched | fail, major finding |
| BC3 | Growth-state persistence | P(same side next year) = 77% pooled — growth regimes persist (cf. IR2 81%) | measured, prior set |

## Entry KJ1 (2026-09-02) — Atlas 2.4/2.5 Kitchin clock test on monthly commodity prices
Script: scripts/analyze_kitchin.py. PRE-REGISTERED before running (two-pass rule). Kitchin's
1923 claim (~40 months) was measured on bank clearings, commodity prices and interest rates —
the vault holds his variable class at monthly cadence: gold (floating era 1968-01..2026-07;
the fixed-price eras are excluded AT REGISTRATION because a pegged price is not a market
process) and the IMF all-commodity index (1980-02..2017-06). Two cells, both declared:
- Construction: expanding Hamilton gap (monthly h=24 from the shared grid, p=4) → expanding
  percentile (min_obs 36) → extrema machinery, min_gap 18 months (just under half the claimed
  period). NOMINAL series (no monthly deflator vaulted) — stated; at 40-month scale spacing is
  insensitive to slow deflators.
- Bar (same for both cells): the ~40-month clock passes only if median peak-to-peak spacing
  is in [30, 50] months AND ≥50% of spacings fall in [30, 50].

| # | What | Result | Status |
|---|---|---|---|
| KJ1a | Gold monthly, floating era | median 21m, **0%** of 28 spacings in [30,50]m — **FAIL**; spacings truncate at the 18m registration floor (no structure above resolution — a 21m clock may NOT be read from this) | fail, floor-artifact noted |
| KJ1b | IMF all-commodity index | median 23m, **0%** of 9 in-window — **FAIL**, same shape | fail |

## Entries MP1–MP3 (2026-09-02) — Atlas 2.6 monetary-policy cycle (seat L6), JST analogues
Script: scripts/analyze_mp_cycle.py. PRE-REGISTERED before running. Per the BC2 STANDING
WARNING these lead-lag constructions use MATCHED transformations on both legs (simple 1y
changes, no differential smoothing) and a declared magnitude floor.

Pre-declared constructions and bars:
- Legs: Δstir_t (1y change in the JST short rate) and g_credit_t (1y growth of REAL loans,
  tloans/cpi). Annual, per country, countries with ≥50 overlapping years.
- MP1 (does the policy rate LEAD credit, negatively?): per country, the MOST NEGATIVE cross-
  correlation over lags −3..+3 (positive lag = rate leads credit). Countries count toward the
  claim only if that minimum is ≤ −0.10 (the floor). Bar: ≥60% of qualifying countries place
  the minimum at lag ≥ +1.
- MP2 (where does the peak effect sit? — the seat's "~1y lag" convention): pooled corr of
  Δstir_t with g_credit at t+0, +1, +2, +3. Measurement, prior set, no bar.
- MP3 (stance persistence): P(sign of Δstir_{t+1} = sign of Δstir_t), pooled — do
  tightening/easing campaigns persist? Measurement, prior set.

| # | What | Result | Status |
|---|---|---|---|
| MP1 | Rate leads credit (negative, matched legs, floor) | 9 qualify; **67% at lag ≥ +1 — PASS** (bar 60%); direction survives the BC2-grade test; magnitudes small → regime consumption, not print-chasing | pass, modest |
| MP2 | Lag profile of the transmission | contemporaneous +0.07 (reaction-function face), peak NEGATIVE at +1y (−0.06), decay at +2/+3 — the seat's ~1y lag convention calibrated; the sign flip is the measured case against same-day stance reads | measured, prior set |
| MP3 | Campaign persistence | 53% annual sign-persistence — near coin flip: regime content is in the stance LEVEL, not move direction; Δ-based stance variant closed off | measured, informative |

## Entries FP1a–FP1b (2026-09-02) — Atlas 2.7 fiscal/political cycle, India factors
Script: scripts/analyze_fiscal_cycle.py. PRE-REGISTERED before running. Data: vaulted
iima_monthly_factors.csv (MF = market factor, monthly, 1993-10..2025-12). General-election
RESULT months (fixed list, public record): 1996-05, 1998-03, 1999-10, 2004-05, 2009-05,
2014-05, 2019-05, 2024-06 (n=8 — tiny, stated). Window = the 3 months ENDING in the result
month (the campaign window).
- FP1a (the folk "pre-election rally"): PASSES only if the mean window monthly MF return
  exceeds the all-months mean AND ≥6/8 elections have positive window means. (The atlas/L5
  prior says direction is SURPRISE — this trial grades the folk claim against that prior.)
- FP1b (the L5 scheduling rationale): median |monthly MF return| inside windows vs all
  months — measurement, prior set, no bar (L5 schedules vol, not direction).

| # | What | Result | Status |
|---|---|---|---|
| FP1a | Pre-election direction (folk claim) | window mean +3.99%/m vs +0.72 base, 7/8 positive — **PASS as registered**, then dissected: window contains the result month (drift/surprise conflation), 2009 carries the mean (ex-2009 ≈ +1.9%/m), n=8 association only. Routed to heuristics lane as HL-7 (teach-only/paper-trade); L5 unchanged | pass, deflated honestly |
| FP1b | Window absolute-move profile | median |monthly| 5.4% in windows vs 4.2% all months; result-month median 6.5%, range −17.7..+33.6 — L5's vol-scheduling rationale measured; direction-is-surprise re-proven | measured, prior set |

## Entries GF1–GF3 (2026-09-02) — Atlas 2.8 global financial cycle (seat L9)
Script: scripts/analyze_global_cycle.py. PRE-REGISTERED before running. Data: vaulted
jst_real_returns.csv (16 countries, annual real equity) + iima_monthly_factors.csv (India MF).

Pre-declared constructions and bars:
- GF1 (the factor's RISE): median pairwise corr of annual real equity returns across the JST
  panel, pre-1990 (1900-1989) vs post-1990 (1990-2015). Bar: post-1990 median exceeds
  pre-1990 median by ≥ 0.10 (the globalization-of-the-cycle claim).
- GF2 (India's loading): annual India market-factor return (compounded iima MF, 1994-2015)
  vs the equal-weight JST-panel mean real return, same years (n=22, matched annual legs).
  Bar: corr ≥ 0.30 ("India is materially inside the global cycle" — the seat's transfer
  premise).
- GF3 (breadth of global downs): in years where the pooled JST mean real return < 0
  (post-1950), the median share of countries individually negative. Bar: ≥ 75% ("one cycle,
  everywhere" in its crude testable form).

| # | What | Result | Status |
|---|---|---|---|
| GF1 | Pairwise co-movement, pre vs post 1990 | +0.28 → +0.77 — **PASS**, the project's cleanest regime-change print; standing caveat born: pre-1990 analogue evidence discounts on transfer | pass, strong |
| GF2 | India's loading on the global factor | corr +0.57 (annual, 1994-2015, n=22) — **PASS**; the L9 transfer premise measured | pass |
| GF3 | Breadth of global down-years | median 69% of countries negative vs 75% bar — **FAIL**: 'one cycle everywhere' is too strong; 'most places, most of the time' is the licensed sentence; partial insulation real but never assumable ex ante | fail, refining |

## Entries DL1–DL3 (2026-09-02) — Atlas 2.9/2.10 dollar/Fed folds
Script: scripts/analyze_dollar_cycle.py. PRE-REGISTERED before running. Construction: REAL
equal-weight dollar index vs the JST panel currencies, 1950-2015 — chained mean over countries
of [Δlog xrusd_i − π_i + π_US] (USD real appreciation), USA excluded from the currency set.
- DL1 (the "~7-10y dollar swing" claim): peaks of the index (3y smooth, min_gap 4y). Bar:
  median peak-to-peak spacing in [7,10]y AND ≥50% of spacings in [6,11]y.
- DL2 (EM headwind transfer): corr of annual index change vs India market-factor annual
  return, 1994-2015 (n=22). Bar: corr ≤ −0.30 ("EM equity's single most reliable macro
  headwind" — the atlas's own sentence, tested on India).
- DL3 (the Fed sub-face): corr of ΔUS short rate (stir_USA) vs SAME-year and NEXT-year index
  change — measurement, prior set (the rate-differential mechanism's crude read).

| # | What | Result | Status |
|---|---|---|---|
| DL1 | Dollar-swing spacing vs 7-10y | peaks [1969,1984,1993,2000,2009], spacings [15,9,7,9], median 9y — **PASS as registered on n=4**, promotion REFUSED (FP1a precedent + the five-fail frequency-sweep prior; index ends 2015); swings real, clock not crowned, L9 leg stays a state | pass, not promoted |
| DL2 | Dollar-up = India headwind | corr −0.34 (bar ≤ −0.30) — **PASS**; the dollar leg's India transfer number (companion to GF2) | pass |
| DL3 | US rate → dollar (lag profile) | −0.03 same-year, +0.06 next — ZERO at annual frequency: realized-policy paths don't carry the dollar; the 2.10 fold into L9's real-yield-LEVEL leg is evidence-backed | measured, fold-supporting |

## Entries CI1a–CI1b (2026-09-02) — Atlas 2.11 China credit impulse (candidate H54), proxy trials
Script: scripts/analyze_china_impulse.py. PRE-REGISTERED before running. China is in neither
JST nor the vault (BIS blocked; no mirror — commodity partC C.6); these are PROXY trials on
the China-demand channel in commodity prices. Confounds stated at registration: energy,
dollar, global IP — a proxy licenses state-enrichment candidacy, never a standalone signal.
- Basket: metals_rel = mean log real price of {Iron ore, Copper, Steel, Zinc, Nickel,
  Aluminum} MINUS mean log real price of the agriculture group (grains+softs+animal), Jacks
  annual. IMF monthly analogue: Metals Price Index minus Agricultural Raw Materials+Food.
- CI1a (the China era changed the metals-ags relative dynamics): std of 3y Δmetals_rel,
  2000-2015 vs 1950-1999 (Jacks). Bar: post-2000 std ≥ 1.5× pre-2000 std.
- CI1b (named-pulse sign check, IMF monthly, n=2 windows — tiny, stated): cumulative
  metals-minus-ags log change positive in BOTH windows [2008-11..2010-12] and
  [2016-01..2017-06]. Bar: 2/2 positive.

| # | What | Result | Status |
|---|---|---|---|
| CI1a | Metals-vs-ags variance shift, China era | std ratio **2.19x** (bar 1.5x) — **PASS**: something structural entered metals' relative dynamics ~2000, consistent with the China channel | pass |
| CI1b | Named-pulse sign check (n=2) | 2/2 positive (+0.34, +0.16) — **PASS**, confounds named (global reflation/dollar in w1; supply-side reform in w2); licenses L9-enrichment CANDIDACY only, never a standalone signal; H54 graduation waits on real TSF | pass, bounded |

## Entry OL1 (2026-09-02) — Atlas 2.12 oil/energy fold: the shock-type asymmetry
Script: scripts/analyze_oil_cycle.py. PRE-REGISTERED before running. The Kilian premise in its
crudest vault-computable form: an oil-price rise means DIFFERENT things for India depending on
whether it rides global demand (partly self-hedging) or a supply shock (unambiguous hit).
- Construction: annual Brent/WTI-spliced real oil return (EIA monthlies annualized; pre-1987
  from Jacks Petroleum); world-demand proxy = pooled JST mean real equity return sign
  (positive = demand-flavored year, negative = supply-flavored year, stated as a CRUDE proxy);
  India leg = annual iima MF return, 1994-2015.
- OL1: among oil-UP years (annual real oil return > +10%), mean India return in
  demand-flavored years MINUS mean in supply-flavored years. Bar: difference ≥ +10pp
  (demand-flavored oil-up years materially less damaging). n will be small — stated.

| # | What | Result | Status |
|---|---|---|---|
| OL1 | Oil-up asymmetry by shock flavor | demand-flavored +38.1% vs supply-flavored −43.1% (n=11: 8/3) — **PASS by 8x, capped on dissection**: the flavor proxy IS the global-equity sign, so the print is ~GF2's loading in an oil costume (+ the 2008 annual-averaging artifact); licenses the decomposition COMMITMENT and the briefing table, not a measured oil-specific asymmetry — that waits for the real Kilian index | pass, capped |

## Entries FL1–FL2 (2026-09-02) — Atlas 2.13 FPI positioning (seat L14): DATA-GATED designs
No trial RUNS in this entry — no flow/ownership data is vaulted (NSDL/shareholding pulls are
runsheet items). Designs registered NOW with acceptance bars, run when the data lands:
- FL1 (the exclusion's quantification): on NSDL monthly equity flows vs Nifty returns,
  matched legs, lags −6..+6m. The flows-follow-returns claim is CONFIRMED if the peak
  |cross-corr| sits at returns-leading lags in ≥2 of 3 declared sub-eras (2003-08, 2009-14,
  2015-26); any flow-momentum PREDICTIVE claim must clear corr ≥ 0.15 at flow-leading lags
  with purging — else §7 REJECT stands.
- FL2 (the seat's own test): float-scaled FPI ownership percentile ≥ 0.9 (expanding) →
  forward 12m drawdown conditioning, purged; acceptance: top-decile positioning months show
  deeper median max-drawdown than the unconditional median by a margin set at data-landing
  (two-pass rule) — reduce-only consequences either way.

| # | What | Result | Status |
|---|---|---|---|
| FL1 | Flows-follow-returns quantification | (awaits NSDL vault) | registered design |
| FL2 | Positioning-extreme drawdown conditioning | (awaits shareholding vault) | registered design |

## Entries EN1–EN3 (2026-09-02) — Atlas 2.14 ENSO (candidate H55), statsmodels SST vault
Script: scripts/analyze_enso.py. PRE-REGISTERED before running (two-pass). Series: by-month
standardized SST anomalies, 3-month centered smooth (the ONI-convention analogue, declared).
- Episode onset = first month of a run with smoothed anomaly ≥ +0.5σ lasting ≥ 5 consecutive
  months (El Niño); symmetric at ≤ −0.5σ for La Niña.
- EN1 (THE QUASI-PERIODICITY TEST — the frequency sweep's physics counterpoint): El Niño
  onset-to-onset spacings, 1950-2010. Bar: median in [2,7]y AND ≥70% of spacings in [2,7]y.
  If ENSO passes where five financial clocks failed, the register gains its control group:
  the machinery CAN crown a clock when physics provides one.
- EN2 (India transfer shadow): India factor annual return in El Niño-onset years vs all
  years, 1994-2010 overlap (n≈4 — tiny; measurement, prior set, no bar; the real India test
  is monsoon/CPI, runsheet).
- EN3 (forecastability shadow): P(smoothed anomaly sign persists next month) — measurement.

| # | What | Result | Status |
|---|---|---|---|
| EN1 | ENSO quasi-periodicity (the physics clock) | median 4.0y (dead-center) but 62% in [2,7] vs 70% bar — **FAIL**: sub-2y re-crossing artifacts + one 8y gap; the sweep's crowning lesson — even PHYSICS can't clear a strict clock bar under a real-time rule, so no financial clock ever should be expected to; ENSO consumed as a STATE | fail, doctrine-sealing |
| EN2 | El Niño years vs India factor | +14.3% vs +14.0% (n=6) — NO equity penalty; the transfer is monsoon→CPI→RBI (H55's design), not the index | measured, prior set |
| EN3 | Monthly sign persistence | 92% — the forecastability shadow; state representation captures the calendar's content without the calendar | measured |

## Entries PS1–PS3 (2026-09-02) — Atlas 2.15 profit-share cycle (candidate H56), PWT 10.0
Script: scripts/analyze_profit_share.py. PRE-REGISTERED before running. Proxy: capital share
= 1 − labsh (a MACRO share, broader than corporate profits/GDP — stated). Countries with ≥50
observations.
- PS1 (mean reversion): per country, corr(capital-share level_t, next-10y change). Reversion
  predicts NEGATIVE. Bar: ≥70% of countries negative.
- PS2 (the extremes condition): pooled P(next-10y change < 0 | level in top quintile of own
  expanding history) vs unconditional P. Bar: conditional ≥ unconditional + 15pp.
- PS3 (India context): India's capital-share path + end-of-sample (2019) own-history
  percentile — measurement, prior set; the atlas's 2019-24 corporate tripling is POST-sample
  and enters via the cases record, never spliced.

| # | What | Result | Status |
|---|---|---|---|
| PS1 | Level → next-decade change (reversion) | **85% of 114 countries negative — PASS** (FC1-class breadth): relative mean reversion is real | pass, strong |
| PS2 | Top-quintile conditioning | 27% vs 21% declines (+6pp vs +15pp bar) — **FAIL**: reversion operates AROUND a rising trend; extremes predict smaller RISES, not falls. H56 sharpened: extrapolation discipline, never decline prediction | fail, design-sharpening |
| PS3 | India's arc + 2019 percentile | 0.478 = 81st own-history pct in 2019, BEFORE the listed tripling; macro-vs-listed caveat travels | measured |

## Entries IS1–IS2 (2026-09-02) — Atlas 3.2 issuance/sentiment (seat L7): DATA-GATED designs
No trial RUNS here — primary-market histories (issue calendars, subscription books, listing
pops) are runsheet pulls (NSE/BSE/SEBI bulletins). Designs registered with acceptance shapes:
- IS1 (the Baker-Wurgler India test): monthly issuance value / market cap, expanding
  percentile, vs forward 12m and 24m index returns, purged. Acceptance bars set at data-
  landing (two-pass); the PRIOR is stated now: top-quintile issuance months → below-median
  forward returns in ≥60% of instances or the volume leg is demoted to confirm-only.
- IS2 (the ladder's changes_if episodes): the two-leg state's reads through 2018 (pipeline
  freeze) and 2023-24 (SME frenzy + SEBI curbs) must match the narrative chronology
  directionally (shape check, dates pre-listed at registration when data lands).

| # | What | Result | Status |
|---|---|---|---|
| IS1 | Issuance percentile → forward returns | (awaits primary-market vault) | registered design |
| IS2 | 2018 / 2023-24 episode shape check | (awaits primary-market vault) | registered design |

## Entries CR1–CR2 (2026-09-02) — Atlas 3.3/3.4 crowding, vaulted India factors
Script: scripts/analyze_crowding.py. PRE-REGISTERED before running. Data: iima monthly factors
(1993-10..2025-12). The crowding literature's testable shadow on returns alone: a CROWDED
factor exits synchronously — crash asymmetry.
- CR1a (skewness ordering): monthly skew(WML) ≤ −0.5 AND skew(WML) below BOTH skew(SMB) and
  skew(HML). (Momentum as the crowded factor par excellence — Daniel-Moskowitz + Lou-Polk.)
- CR1b (crash concentration): each factor's worst month in own-σ units; bar: WML's worst
  ≤ −4σ AND more extreme than SMB's and HML's.
- CR2 (the atlas's named episode): 2025 monthly WML prints listed; any month ≤ −2σ flagged —
  MEASUREMENT (prior set) grading whether the "mid-2025 quant unwind" shows in India's
  momentum factor at all.

| # | What | Result | Status |
|---|---|---|---|
| CR1a | Skewness ordering (WML most negative) | WML +0.05, SMB +0.04, HML +0.60 — **FAIL**: the US negative-momentum-skew import dies on India's library; danger is regime-local (consistent with 03's CONDITIONAL crash finding); crash_guard's conditional design vindicated | fail, import-refining |
| CR1b | Worst-month concentration | WML worst −4.1σ vs SMB −2.9σ / HML −3.4σ — **PASS**: synchronized-exit tail depth confirmed | pass |
| CR2 | The mid-2025 unwind in India WML | ZERO 2025 months ≤ −2σ — the named episode is invisible at monthly academic-factor granularity; consequence: the 3.4 monitor CANNOT be monthly factor returns — AUM/comomentum legs are structural, not decorative | measured, design-setting |

## Entries RT1–RT2 (2026-09-02) — Atlas 3.6 retail wave (candidate H57): DATA-GATED designs
No trial RUNS here — no participation data is vaulted (NSDL/CDSL demat counts, SEBI retail
F&O shares are runsheet pulls). Designs registered with acceptance shapes:
- RT1 (the cohort-wave state): new-demat-account growth-rate + retail share of index-option
  turnover, expanding percentiles → the H57 sub-input to L7. Acceptance at data-landing
  (two-pass); the PRIOR stated now: the 2021-24 window must print top-decile states and the
  post-curb 2025 window must print falling states (shape check against the public record)
  or the construction is wrong.
- RT2 (the VRP-compression watch): India VIX minus subsequent realized vol (the crude VRP)
  regressed on the retail-F&O-share percentile — direction prior: high retail share
  compresses VRP; bars at registration when both legs are vaulted.
Also noted for the 3.5 record: NO RV-design exists — a REJECT FOR DATA registers no designs;
its revisit trigger (a free consensus-estimate source appearing) lives in the entry's Part H.

| # | What | Result | Status |
|---|---|---|---|
| RT1 | Cohort-wave state (shape prior stated) | (awaits participation vault) | registered design |
| RT2 | Retail share → VRP compression | (awaits vault + India VIX archive) | registered design |

## Entry PL1 (2026-09-02) — Atlas 3.7: direction-is-surprise, formalized
Script: scripts/analyze_political.py. PRE-REGISTERED before running. Data: iima MF monthly;
the 8 general-election result months (FP1's fixed list). MEASUREMENT (prior set, no bar —
n=8): does the pre-window sign (mean of the 2 months BEFORE the result month) predict the
result-month sign? Report the agreement rate; L5's "direction is surprise" predicts ~coin-flip.

| # | What | Result | Status |
|---|---|---|---|
| PL1 | Pre-window sign → result-month sign | **3/8 agreement** — at/below coin-flip: 'direction is surprise' measured; L5's scheduling-only design + HL-7's paper-trade routing both re-confirmed | measured, prior set |

## Entries CW1–CW3 (2026-09-02) — Atlas 4.1/4.2/4.11: the calendar-as-signal trials
PRE-REGISTERED before running (bars below written before any number was computed).
Script: scripts/analyze_calendar.py. Data: iima_monthly_factors.csv (MF, SMB; 1993-11..2025-12).
Resolution caveat stated NOW: Budget-day vol is a 1–3 day phenomenon; monthly granularity
attenuates it severely (the CR2 lesson). A CW1 FAIL therefore routes to "real at daily
resolution, invisible monthly" ONLY IF the literature/VIX record supports it — it does NOT
license inventing a pass. Rank bars, not magic thresholds.
- CW1 (Budget-month vol, 4.1): |MF| by calendar month. BAR: February's median |MF| ranks in
  the top 3 of 12 months AND one-sided Mann-Whitney (|MF| Feb vs non-Feb) p < 0.10. July
  (election-year full budgets) is NOT tested — documented limitation.
- CW2 (FY-end small-cap reversal, 4.2): SMB by calendar month. BAR: April's median SMB ranks
  #1 or #2 of 12 months AND April median SMB > 0 AND one-sided Mann-Whitney p < 0.10.
  A FAIL kills the EDGE hypothesis at monthly resolution (it was registered "small,
  cost-fragile" in the atlas — the C-tier prior).
- CW3 (month-of-year omnibus, 4.11): Kruskal-Wallis of MF across 12 months. INTERPRETATION
  RULE PRE-STATED: p ≥ 0.05 → consistent with no calendar structure, REJECT confirmed;
  p < 0.05 → the REJECT STILL STANDS (Contract §8 mechanism ban; 12-way comparisons expect
  ~0.6 false positives at 5%) — the print is logged and dissected, promoted NEVER. This
  trial is a demonstration, and that purpose is declared before the print.

| # | What | Result | Status |
|---|---|---|---|
| CW1 | Feb |MF| rank + MW test | Feb rank 7/12, median 4.27 vs 4.22, p=0.522 — **FAIL**: the Budget month is ordinary at monthly resolution (the CR2 pattern again); L5's budget scheduling rests on the daily-resolution VIX record + the fixed-date mechanism, NOT on this print | fail, resolution-routed |
| CW2 | Apr SMB rank + MW test | Apr median SMB +2.47, rank 1/12, p=0.020 — **PASS**: the FY-end small-cap-rebound signature is real at monthly resolution; post-hoc note (NOT pre-registered): Feb/Mar are the two most NEGATIVE SMB months — the selling leg of the same mechanism, tagged for a follow-up trial. Promotion: Tier-C instrumentation + pre-registered paper-trade, NO return budget (cost-fragile per the atlas prior) | pass, promotion-refused |
| CW3 | 12-month omnibus (demonstration) | H=12.13, p=0.354 — no calendar structure; the 4.11 REJECT confirmed exactly as pre-stated (and the rank-1 months in CW1/CW3 stay logged, never interpreted) | measured, reject-confirmed |

## Designs CW-D1 / CW-PT1 / CW2b (2026-09-02) — Atlas 4.1/4.2 follow-ons, DATA-GATED
- CW-D1 (daily budget-window vol): India VIX daily (NSE, 2009-) + NIFTY daily around budget
  days vs matched non-event days; bar: one-sided p < 0.05 on budget-day ±1 |return| and VIX
  change (n≈18 budgets+interims). Pre-2001 5pm-presentation era excluded by design (event-day
  definition break). Runsheet pull.
- CW-PT1 (April small-cap paper trade): modeled tilt Apr-1..Apr-30 net of config/costs.yaml,
  ledgered like HL-7; promotion discussable only after 3 Aprils AND net-positive in ≥2.
- CW2b (the selling leg, pre-registered for the NEXT factor-library refresh): Feb+Mar pooled
  median SMB < 0 AND MW one-sided p < 0.10 vs the other ten months. Registered BEFORE any
  new data exists; the current library's print is quarantined as the post-hoc observation
  that motivated it and cannot grade it.

| # | What | Result | Status |
|---|---|---|---|
| CW-D1 | Daily budget-day vol event study | (awaits India VIX vault) | registered design |
| CW-PT1 | April tilt paper ledger | (first grading April 2027) | registered design |
| CW2b | Feb+Mar selling-leg confirmation | (awaits library refresh) | registered design |

## Designs H58-D1..D3 + RC1 (2026-09-02) — Atlas 4.3-4.6 calendar-mechanics, DATA-GATED
Pure ops (no alpha claim anywhere in this block — the pre-stated framing). Machinery ships
now (quant/ladder/exclusion_calendar.py); every GRADE waits on daily data:
- H58-D1 (drain-date false-fire count): once L2's daily trigger history exists, count
  funding-stress fires landing inside statutory drain windows (advance-tax Jun/Sep/Dec/Mar
  15 ±2bd; GST due 20th ±1bd) vs outside; the exclusion earns its keep if drain-window fires
  are ≥2x the base rate AND ≥80% of them mean-revert within 5bd (mechanical, not stress).
- H58-D2 (results-date gap dodge): count staged-entry tranches that would have crossed a
  holding's results date; report the |gap| distribution dodged vs ordinary days (bhavcopy +
  exchange results calendar). No bar — a frequency report; the rule is mechanical prudence.
- H58-D3 (expiry-day noise): |close-to-close| and close-auction behavior on expiry days vs
  matched weekdays (bhavcopy). Expiry weekday is CONFIG, not constant — the 2024-25 SEBI
  curbs + exchange moves make hardcoding a bug (documented in the module).
- RC1 (reconstitution pop, Atlas 4.6): event study on Nifty semi-annual add/drop lists
  (announcement→effective window) — the special-sits EDGE leg + the momentum-exclusion leg
  (adds' pre-effective pop must NOT feed L3/L4 lookbacks). Bars at registration when the
  add/drop lists + daily prices are vaulted.

| # | What | Result | Status |
|---|---|---|---|
| H58-D1 | Drain-window false-fire frequency | (awaits L2 daily history) | registered design |
| H58-D2 | Results-gap dodge count | (awaits results calendar vault) | registered design |
| H58-D3 | Expiry-day noise measurement | (awaits bhavcopy vault) | registered design |
| RC1 | Reconstitution add/drop event study | (awaits index lists vault) | registered design |

## Entry GS1 (2026-09-02) — Atlas 4.9: gold festival-seasonality demonstration
PRE-REGISTERED before running. Script: scripts/analyze_gold_seasonality.py. Data: vaulted
gold monthly 1833-2026; TEST WINDOW = the float era only (1972-01 onward — Bretton Woods
convertibility suspended Aug-1971; the fixed-parity era has no monthly price process to
test). Log returns by calendar month.
DESIGN (a CW3-style demonstration; the interpretation rule pre-stated): D06 says India is a
price TAKER — festival demand (Akshaya Tritiya ~Apr-May, Dhanteras ~Oct-Nov, weddings) lives
in LOCAL premia, not the world price. Kruskal-Wallis of monthly log returns across 12
months. p >= 0.05 → consistent: no world-price festival structure, the 4.9 CONTEXT verdict
confirmed. p < 0.05 → the CONTEXT verdict STILL stands (12-way comparison; and any single
strong month would need a mechanism by which Indian festivals move the WORLD price — none
is on offer at India's ~25% share of consumer demand and ~0% of price formation venue).
Also report (descriptive, no bar): September's median — the folk "gold's strong month"
claim, logged for the lesson either way.

| # | What | Result | Status |
|---|---|---|---|
| GS1 | Gold month-of-year omnibus (float era) | H=10.87, p=0.454 (n=654, 1972-2026) — no world-price festival structure; the festival months are the WORST ranks (Apr 12/12, May 11/12, Nov 10/12) and folk-September is 6/12 — D06 price-taker verdict demonstrated, CONTEXT confirmed | measured, context-confirmed |

## Entries FS-U1 / FS-U2 (2026-09-02) — Atlas 5.1: vol clustering demonstrated on OUR library
PRE-REGISTERED before running. Script: scripts/analyze_vol_clustering.py. FRAMING STATED
NOW: vol clustering is Tier-A physics (the most replicated fact in finance); these are
DEMONSTRATION trials at monthly resolution on the vaulted series — the value is (a) the
Cycle School chart computed by us, (b) a library-integrity check (a FAIL would indict the
library or the monthly-aggregation claim, not the daily fact), and (c) an honest measure of
how much clustering SURVIVES monthly aggregation (the fast layer is daily by design; the
resolution theorem cuts both ways and the print quantifies the loss).
- FS-U1 (India market factor): |MF| monthly, 1993-2025. BAR: Ljung-Box on |ret| lags 1-6
  p < 0.05 AND lag-1 autocorrelation of |ret| positive.
- FS-U2 (gold, float era): |log ret| monthly, 1972-2026. Same bar.
Both bars two-legged; interpretations AFTER the prints.

| # | What | Result | Status |
|---|---|---|---|
| FS-U1 | Monthly vol clustering, India MF | |ret| ACF(1..6) 0.141-0.188 all positive, LB(6) Q=60.3 p=4e-11 — **PASS**: clustering survives monthly aggregation clearly, though at ~0.15-0.19 vs the ~0.2-0.4 typical of daily |ret| — the aggregation loss is visible and quantified | pass, demonstration |
| FS-U2 | Monthly vol clustering, gold | ACF(1..6) 0.17-0.245 all positive, LB(6) Q=166.3 p=3e-33 — **PASS**: the Tier-A fact holds cross-asset on our vault; library integrity corroborated | pass, demonstration |

## Designs FS-D1 / FS-D2 (2026-09-02) — Atlas 5.2/5.3 folds into L2, DATA-GATED
Registered in research/cycles/faststress-upgrade/partDH-upgrade.md (bars there):
- FS-D1 (backwardation flag, distinct from F5's IV-level redundancy test): near/far implied
  variance ratio; must ADD episode AUROC over the RV leg (incremental, purged) or be excluded.
- FS-D2 (order-of-arrival taxonomy): first top-decile print per leg per episode; 2018
  funding-led and 2020 vol-led orderings are the pre-stated shape checks; failing them kills
  the classification, not the legs.

## Design MR1 (2026-09-02) — Atlas 5.4: 1-month cross-sectional reversal, DATA-GATED
Tier-C flag with ZERO return budget by atlas verdict (the most cost-fragile anomaly known;
20bp STT round trip; no India magnitude studies). Design registered so the flag is graded,
never guessed: on vaulted bhavcopy, decile long-short 1-month reversal within the liquid
half of NIFTY 750, NET of the config/costs.yaml stack per book; acceptance shape: the freeze
is permanent unless net-of-cost spread > 0 across BOTH halves of the sample AND survives the
McLean-Pontiff haircut — and even then consumption stays "H08-informing flag", never a
sleeve (the atlas's own cap).

| # | What | Result | Status |
|---|---|---|---|
| FS-D1 | VIX term-structure adds over RV | (awaits VIX/option-chain vault) | registered design |
| FS-D2 | Leg order-of-arrival by episode | (awaits CCIL+VIX dailies) | registered design |
| MR1 | 1m reversal net-of-cost grade | (awaits bhavcopy vault) | registered design |

## Design H59-D1 (2026-09-02) — the semiconductor-transmission test, DATA-GATED
The last §8 candidate gets its registration — WITH THE PRIOR STATED: the desk expects this
to FAIL. India's listed IT sector sells services (enterprise IT budgets, US BFSI spend),
not chips; the semiconductor shipment cycle's transmission story is indirect at best.
Design: WSTS worldwide billings YoY, expanding-percentile state (monthly, 1976-, free Blue
Book — runsheet pull; see research/cycles/semis-candidate/DATA-PROBE.md) vs NIFTY IT
relative returns (NSE, 1990s-), purged CV. BAR at data landing: incremental explanatory
power over the L9 global-cycle state — if the semi cycle adds nothing beyond global macro,
the candidate dies as designed and the death certificate blocks the "it cycles, therefore
trade it" costume. A candidate registered to die is still knowledge.

| # | What | Result | Status |
|---|---|---|---|
| H59-D1 | WSTS state → NIFTY IT incremental (prior: fails) | (awaits WSTS + NIFTY IT vault) | registered design |

## Entries CW-D1a / DW1 / F1a / F2a (2026-09-02) — the FIRST DAILY-RESOLUTION batch
The NIFTY 50 daily vault (2007-09..2026-04, mirror authenticated 6/6, ingest/vault/index/)
unblocks partial runs of already-registered designs. PRE-REGISTERED before running; script:
scripts/analyze_nifty_daily.py. Budget dates are public record, listed in the script
(2008-2026 fulls + interims; the Mar-16-2012 late budget included; span is all 11am-era).
- CW-D1a (the return leg of CW-D1, whose bar was set at registration): budget-day |return|
  vs all non-budget days, one-sided Mann-Whitney p < 0.05. The VIX leg of CW-D1 stays gated
  (no VIX vault yet); this is a PARTIAL run and is labeled as such. Secondary (no bar):
  the same test on budget-day ±1 window.
- DW1 (5.5 demonstration addendum): Kruskal-Wallis of daily returns across the five
  weekdays. INTERPRETATION RULE PRE-STATED (the CW3/GS1 mold): p >= 0.05 confirms the 5.5
  REJECT with evidence; p < 0.05 does NOT reinstate day-of-week trading (5-way comparison,
  no mechanism) — logged and dissected only. This upgrades 36-fastlayer-close's "no trial
  spent" to "trial spent for free once the data landed for other reasons".
- F1a (partial F1): AR(1) half-life of the two-leg composite (RV21 pct + DD pct, weights
  0.5/0.5 — the module test defaults, stated as such; confirm legs absent, n_legs=2).
  MEASUREMENT with a moving-block bootstrap CI (block 63d, 1000 draws); registered ladder
  value is tau_half [1,3] months — the print either sits inside/overlapping or triggers the
  changes_if note. No pass/fail bar (F1's design: CI -> ladder).
- F2a (detection-only leg of F2): composite >= 0.3 within [start-5bd, end+21bd] of each of
  the 12 in-span pre-named episodes (docs/cycles/02-fast-stress.md §3). BAR: >= 8/12
  detected, misses named and dissected. Also reported (no bar): false-fire days (>= 0.3
  outside every episode window ±2 months) and median detection lag from episode start.

| # | What | Result | Status |
|---|---|---|---|
| CW-D1a | Budget-day |ret| vs non-budget (daily) | day-only median 1.14% vs 0.59%, p=0.110 — **FAIL as registered** (n=19 underpowered). PROCESS NOTE: this partial registration mis-transcribed the ORIGINAL CW-D1 window (registered as budget-day **±1**); the original-window print: median 0.95% vs 0.59%, p=0.0049 — **PASS on the original CW-D1 return-leg bar**. Both recorded; neither bar moved; VIX leg still gated | fail (partial) / pass (original leg), process note |
| DW1 | Weekday omnibus (demonstration) | H=2.83, p=0.587 — no weekday structure; 5.5 REJECT now carries evidence; note: Monday's median is the HIGHEST (+0.102), the OPPOSITE sign of the classic weekend effect — logged, never interpreted | measured, reject-confirmed |
| F1a | tau_half of 2-leg composite (daily) | point estimate 61 trading days (~2.9 months) — inside the registered [1,3]m band, near its top. The 63d-block bootstrap CI ([0.9,1.5]m) is UNRELIABLE here (block length ~ half-life => persistence broken, phi biased down; the point estimate falls outside its own CI). Method inadequacy documented; proper CI deferred to full F1 (bias-corrected machinery) | measured; CI method flagged |
| F2a | Real-episode detection >= 8/11 in-span | **7/11 — FAIL as registered.** Dissection: Jan-2008 UNTESTABLE (expanding-percentile warm-up NaN — vault starts 2007-09; a coverage artifact the registration failed to anticipate; post-hoc 7/10 does NOT flip the verdict); taper-2013 miss (max 0.20) VALIDATES the three-leg design — 2013 was funding/FX-led, exactly the absent confirm leg; demonetization miss consistent (index barely moved); Feb-2018 miss (−0.10) is a genuine finding: THE 2008 SHADOW — once a mega-crisis enters the expanding history, 2018-size vol spikes rank low; percentile de-sensitization after tail events is now a measured property. False fires 2.6% of days (measurement) | fail, design-informing |

## Design F2b (2026-09-02) — percentile-memory sweep (the 2008-shadow follow-up)
Registered at the daily-batch honest read (research/cycles/daily-batch/daily-RESULTS.md):
expanding vs trailing-{5y,10y} percentiles on the F2 detection/false-fire/DD-improvement
tables. Prior: a trade (re-sensitization vs earlier false fires), not a free lunch.

| # | What | Result | Status |
|---|---|---|---|
| F2b | Percentile-memory sweep | (awaits full F2 run) | registered design |

## Entry MR1-S (2026-09-02) — the SURVIVOR-PANEL preliminary of MR1: ASYMMETRIC by design
PRE-REGISTERED before running. Script: scripts/analyze_reversal_prelim.py. Data: the
vaulted NIFTY500 survivor panel (2012-2021; survivorship stated in its AUTHENTICATION.md).
MR1's registered spec (point-in-time membership) is NOT met by this panel, so this
preliminary carries a ONE-WAY decision rule, stated now:
- it can CORROBORATE the L1 freeze (a signal that fails even on survivorship-flattered
  data is dead);
- it can NEVER unfreeze — a positive print is only a survivor-panel UPPER BOUND and the
  true MR1 (point-in-time bhavcopy) remains required.
DESIGN: monthly (month-end) 1-month-return deciles within the liquid half (top 50% by
trailing-63d median value traded among tickers with full trailing month data); long D1
losers / short D10 winners, equal weight, hold one month. COSTS: config/costs.yaml
cash_delivery all-in per-side grid [24,32]bps midpoint 28bps per side, applied to actual
monthly turnover of each side. BARS:
- net mean monthly L-S <= 0 in EITHER half-sample (2012-2016 / 2017-2021) => freeze
  CORROBORATED;
- net > 0 in BOTH halves => recorded as upper-bound-positive, freeze UNCHANGED (one-way).
Also reported (no bars): gross vs net decomposition; Nagel-style stress conditionality
(mean gross L-S in top-decile NIFTY-vol months vs others).

| # | What | Result | Status |
|---|---|---|---|
| MR1-S | Survivor-panel reversal, net of costs | GROSS +0.20%/mo (t=0.39 — nothing, even survivorship-flattered) − cost drag 0.99%/mo (89% monthly one-side turnover × the 28bp stack) = NET −0.80%/mo; NEGATIVE IN BOTH HALVES (−1.20 / −0.42) — **FREEZE CORROBORATED** under the one-way rule. Twist logged (measurement): top-decile-vol months print gross −0.36%/mo vs +0.26 calm — the OPPOSITE sign of Nagel's US stress-spike, n≈12, tagged for the true MR1 | freeze corroborated |

## Entry CR-D2a (2026-09-02) — comomentum on the survivor panel: bars registered at data-landing
CR-D2's registration (docs/cycles/30-rotation-crowding.md Part F) deferred acceptance bars
to the moment stock-level returns were vaulted; the survivor panel (2012-2021) is that
moment for a PRELIMINARY leg (the true NSE-500 PIT run stays registered as CR-D2). This is
a MONITOR CALIBRATION, not a signal test — the bars are shape checks, stated before any
construction runs. Script: scripts/analyze_comomentum.py.
CONSTRUCTION (documented deviation from Lou-Polk: market-adjusted weekly returns instead of
FF3 residuals — the factor library is monthly; deviation recorded): monthly, within the
liquid half, rank by 12-2 momentum; comomentum(t) = average pairwise correlation of
trailing-52-week market-adjusted weekly returns within the LOSER decile (Lou-Polk's own
portfolio choice).
BARS (shape priors):
- P1 (slow state): lag-1 monthly autocorrelation of the comomentum series > 0.5 — a
  monitor must be a state, not noise.
- P2 (the 2018 accumulation): the 2017-12..2018-06 mean comomentum prints ABOVE the full-
  sample median (the pre-smallcap-unwind crowding the public record describes).
Report (no bars): the 2020 COVID print; the series' full path for the monitor's dashboard.

| # | What | Result | Status |
|---|---|---|---|
| CR-D2a | Comomentum calibration (survivor panel) | P1 PASS (lag-1 AC 0.65 — a real slow state). P2 **FAIL**: 2017-12..2018-06 prints 0.071 vs median 0.090, and 2017 is the sample's LOWEST year (0.041) — the pre-smallcap-unwind period shows NO Lou-Polk-style momentum crowding. Dissection (both routed to CR-D2 full): (a) India's 2018 unwind may not have been factor-crowding at all — the THIRD failure of the imported crowding narrative on India data (after CR1a skew, CR2 2025); (b) the documented deviation binds — the 2020 peak (Jun-2020, 0.162, highest year 0.120) tracks the market-wide stress-correlation regime, so market-adjustment without full residualization contaminates the measure. Bars unmoved; machinery now exists | P1 pass / P2 fail, design-informing |

## Entry F2-index (2026-09-02) — the BOUNDED partial run of F2 on the vaulted index
PRE-REGISTERED before running. Script: scripts/analyze_f2_index.py. Data: vaulted NIFTY 50
daily (state valid from ~Sep-2008 after the 252d percentile warm-up; the GFC episode is
only PARTIALLY testable and is flagged as such). This is F2's grid run on an INDEX-PROXY
book (long-only, exposure 1.0, no leverage/hedge/options) with the two available legs —
it can DISQUALIFY grid cells and shortlist survivors; it CANNOT arm the R4 mapping
(that stays with full F2: three legs, book-level costs, M4 walk-forward). Stated
adaptations, all documented: confirm axis {1-of-2, 2-of-2} (the third leg is data-gated);
triggers are quantile rules on the composite's OWN expanding percentile (risk.yaml
bucket_boundaries: no fixed numeric thresholds); action = cut exposure to 0.5 (R4 leverage
midpoint [0.4,0.6]); costs 28bp per unit turnover (cash-delivery midpoint).
GRID (verbatim from F2 where applicable): trigger pctile {0.8, 0.9, 0.95} × confirm
{1-of-2, 2-of-2} × re-entry {phase-D (MEASUREMENT ONLY — F7 gates adoption), pctile-decay
(state pctile < 0.5, the below-median normalization rule), calendar (42bd then 2 tranches
21bd apart, state-gated — config cash_call_reentry post_R4_book, tranches=2)}. 18 cells.
DEEP-EPISODE SET pre-named: episodes where buy-hold episode maxDD >= 20% in-window —
expected {GFC core, EU-2011, COVID}; the set is determined by the buy-hold print, not
chosen after seeing rule results.
BARS per cell: SUPPORTIVE if mean deep-episode maxDD improvement >= 5pp AND full-period
return drag vs buy-hold <= 2.0pp/yr (DESIGN risk-drag outer bound, aggressive). Report the
whole grid (F6's spirit: never a single cell); false-fire counts included.

| # | What | Result | Status |
|---|---|---|---|
| F2-index | 18-cell de-risk grid on real index | Deep set printed as {GFC*, COVID} (2011 fell short of 20% in-window). **3/18 SUPPORTIVE, all at trigger 0.80 + 1-of-2 confirm**: phaseD +8.4pp deep-DD improvement at 0.56pp/yr drag (19 fires; MEASUREMENT ONLY until F7), decay +5.6pp at 1.83, calendar +5.6pp at 1.23. Architecture findings: 2-of-2 confirm kills protection everywhere (the DD leg lags — 'any one arms' is now evidence-backed); triggers above 0.80 fire too late for a 23-session crash; three cells print NEGATIVE drag with sub-bar protection (logged, not promoted). Shortlist for full F2: {0.80, 1of2} x {calendar, decay}; phaseD's dominance is the case FOR running F7 | 3/18 supportive, shortlist set |

## Entry F7a (2026-09-02) — the phase-quadrant asymmetry test (H66 fast band), first real run
PARENT: F7 (docs/cycles/02-fast-stress.md §5, frozen): "at matched state LEVELS: forward
1-3m returns and DD, U vs D; passes => re-entry rules may condition on D via Challenger,
reduce-only first; fails => phase stays display-only for L2." Parent decision rule quoted
VERBATIM per process note #5. The parent fixed the comparison but not numeric bars; bars
declared NOW, before running. Script: scripts/analyze_f7_phase.py. Data: vaulted NIFTY
daily; the same composite/phase construction as F2-index (k_slope=21, smooth=5).
DESIGN: qualifying days = state expanding-percentile >= 0.8 (the F2 trigger zone — re-entry
is what F7 gates). Split by phase direction: U (rising: quadrant boom/recovery-rising
coding) vs D (falling-from-high: slowdown quadrant). To limit overlap inflation, sample
every 21st qualifying day per group. BARS (all three required to PASS):
- median forward 63bd return (D) > (U), one-sided MW p < 0.10;
- mean forward 63bd max-drawdown (D) < (U);
- n >= 10 sampled days in EACH group (else UNDERPOWERED verdict, no pass/fail).
Forward 21bd horizon reported as secondary (no bar). PASS => phase-D graduates to
Challenger status for L2 re-entry, reduce-only first, exactly as the parent registered.

| # | What | Result | Status |
|---|---|---|---|
| F7a | U-vs-D at matched high state | 63bd forward returns: D median +5.62% vs U +5.67%, MW p=0.653 — **FAIL** (return leg decisively flat; DD leg mildly favors D, 7.03 vs 7.63, insufficient alone). Per the parent F7's registered rule: **phase stays display-only for L2**. The reconciliation with F2-index is the finding: phaseD's grid dominance came from re-entering EARLIER (less time out during V-recoveries), not from D carrying information — BOTH directions at high state show ~+5.5%/63bd forward returns. THE LEVEL carries the rebound; the DIRECTION adds nothing. 'States, never dates' gains a sibling: LEVELS, NOT DIRECTIONS | fail, doctrine-refining |


## Design F2c (2026-09-02) — registered at the F7a honest read
F7a's reconciliation implies the phaseD family's F2-index advantage is EARLINESS, not phase
information. The full F2 grid therefore adds a direction-free early-calendar re-entry
variant: calendar-21bd (re-enter after 21bd in 2 state-gated tranches). Prior stated: it
should approximate phaseD's drag numbers WITHOUT the F7 dependence; if it does, the phase
overlay exits the re-entry conversation entirely (display and diagnostics only, everywhere).

| # | What | Result | Status |
|---|---|---|---|
| F2c | Calendar-21bd re-entry variant | (awaits full F2) | registered design |

## Entry TS1 (2026-09-02) — L4 TSMOM calibration, both legs (index + gold)
PRE-REGISTERED before running. Script: scripts/analyze_tsmom.py. Data: vaulted NIFTY daily
(month-end closes, 2007-2026) + vaulted gold monthly (float era 1972-2026). Fills the gap
docs/cycles/03-momentum-trend.md names at its L4 row ("India-specific TSMOM magnitude/cost
estimate — D01 Tier B only"). L4 is a REGIME seat (regime-matrix input + gold tilt), so the
bars are DD-shaped, not alpha-shaped.
RULE FAMILY (CONTRACT §6's own flavor; MOP2012): long if trailing k-month total return > 0
else flat; k in {3, 6, 12} (the D01/L4 lookback grid); monthly decisions applied the next
month; costs 28bp per switch (index) / 10bp (gold ETF-era proxy, stated assumption [A]).
BARS per (asset, k): PASS if net maxDD <= buy-hold maxDD − 10pp AND net CAGR >= buy-hold
CAGR − 2.0pp/yr (the DESIGN risk-drag outer bound). PRIORS stated: 12m passes on DD via the
2008 exit; 3m whipsaws hardest; gold TSMOM historically robust across the 1980-99 bear.
Report per cell: hit rate, switches, net CAGR, maxDD, drag. Consumption: calibrates L4's
Tier-B prior; NO promotion beyond the seat's existing regime role.

| # | What | Result | Status |
|---|---|---|---|
| TS1 | TSMOM {3,6,12}m × {NIFTY, gold} | NIFTY: ONLY k=3 passes (maxDD 22% vs 47% bh, drag 1.1pp/yr, THROUGH 2008); k=6 fails (39% DD, 3.4pp drag); k=12 fails (DD 32% vs 29% — WORSE than buy-hold, 5.8pp drag). PRIOR INVERTED — and honestly: the k=12 window starts 2009 (12m warm-up), so the '12m exits 2008' prior was UNTESTABLE in-window, not refuted; the k=3 pass includes 2008 and is real. Gold: ALL THREE pass, k=12 strongest (net +9.0% vs bh +8.0%, maxDD 34% vs 62%) — the literature prior lands exactly. Lesson: at monthly cadence on India equity, SPEED is the DD-controller (rhymes with F2-index's earliest-trigger finding); gold trend is robust at every speed | index: 1/3 pass; gold: 3/3 pass |

## Entry N4a (2026-09-02) — 52wk-high vs 12-1: the structure leg, survivor panel
PARENT: N4 (docs/cycles/03-momentum-trend.md Part F: "52wk-high vs 12-1 redundancy/
complement split"). The parent named priors via Part C's Raju citations, which on re-reading
cover cadence/concentration rather than this split — so bars are DECLARED NOW, before
running, from the George-Hwang (2004) lineage. Structure questions (rank correlations,
overlaps) are computed on identical universes for both signals, so survivorship biases both
identically — the bounded run is defensible where MR1-level return claims were not (stated).
Script: scripts/analyze_52wk_vs_mom.py. Data: survivor panel, liquid half, monthly.
BARS: REDUNDANT verdict if mean monthly cross-sectional Spearman rho(12-1 rank,
52wk-high-proximity rank) >= 0.8 (near-degenerate blend); COMPLEMENT verdict otherwise.
Report (no bars): mean top-decile overlap; the state-dependence leg — rho in top-decile
index-vol months vs calm months (GH04's mechanism predicts the two signals DIVERGE
post-crash: 12-1 chases the rebound, 52wk-high stays anchored — so the prior is rho FALLS
in/after stress).

| # | What | Result | Status |
|---|---|---|---|
| N4a | 12-1 vs 52wk-high structure | mean Spearman rho 0.519 (range −0.17..0.88), top-decile overlap only 19% — **COMPLEMENT**: the L3 blend earns its place (the signals pick substantially different names). Stress prior FAILED instructively: rho RISES in top-vol months (0.623 vs 0.507) — during a crash both signals compress toward 'who fell least'; GH04's divergence mechanism lives in POST-TROUGH REBOUNDS, which vol-decile months do not isolate. The mis-specified conditioning window is recorded; full N4 gets rebound-window definitions | complement confirmed; prior mis-windowed |

## Entry FS-D3 (2026-09-02) — CBOE VIX as the INTERIM confirm leg for L2
PRE-REGISTERED before running. Script: scripts/analyze_global_vix_leg.py. Data: vaulted
CBOE VIX daily (mirror, admitted with recorded misses) + vaulted NIFTY daily. L2's third
(confirm) leg is empty pending the India VIX vault; global VIX is NOT India VIX — it is the
Rey global-factor reading — and the question is whether it ADDS anything for INDIAN stress
detection while the domestic leg waits. Bars declared now:
- FS-D3a (incremental detection): on the F2a episode set (11 in-span), does adding a
  CBOE-VIX expanding-percentile leg (three-leg composite, equal weights) detect any episode
  the two-leg composite MISSED at the same 0.3 threshold, without losing any it caught?
  BAR: net episodes detected (3-leg minus 2-leg) >= +1 AND false-fire days rise by <= 50%
  (relative) — else the leg is refused as the F5 decision rule prescribes for redundant legs.
- FS-D3b (timing, measurement no bar): for episodes both configurations catch, the median
  detection-lag change (a global leg may fire EARLIER on global-origin crises: 2008, 2020,
  2022 — and add nothing on domestic ones: IL&FS, 2016, 2024 — the order-of-arrival
  taxonomy's prediction, stated as the prior).
Consumption if PASS: interim confirm leg, explicitly superseded the day India VIX lands
(FS-D1/F5 then adjudicate the domestic leg as registered).

| # | What | Result | Status |
|---|---|---|---|
| FS-D3 | Global-VIX interim confirm leg | **FAIL both legs**: net episodes −1 (LOSES the 2024 election day — global VIX quiet, symmetric averaging DILUTED the domestic signal below threshold) and false fires +54%. But FS-D3b's measurement lands the taxonomy's prediction exactly: on global-origin crises the leg is a huge accelerant (EU-2011 lag +91 → +13bd; Russia +17→+9; median both-caught 24→14bd). The refusal is of SYMMETRIC AVERAGING, not of the information — routed to FS-D4 | fail; the dilution mechanism named |


## Design FS-D4 (2026-09-02) — arm-only global-VIX input (registered at FS-D3's honest read)
FS-D3's dissection: a global leg must never DILUTE domestic detection (2024 loss) — the
correct architecture is ARM-ONLY (a global-VIX percentile fire can arm/accelerate the L2
switch; its calm can never subtract). Deliberately DEFERRED to the full F2 grid run rather
than run same-day, to keep distance from the tweak-and-retest trap (CONTRACT §9): bars set
now — on the F2 grid, an arm-only global-VIX input must improve median detection lag on the
pre-named global-origin episodes (2008, 2011, 2015, 2020, 2022) by >= 5bd with false-fire
days <= +50%, and by construction may not lose any domestically-detected episode.

| # | What | Result | Status |
|---|---|---|---|
| FS-D4 | Arm-only global-VIX input | (deferred to full F2) | registered design |

## Entry F1b (2026-09-02) — F1a's deferred estimate, completed with Track-R machinery
F1a measured tau_half ~61 trading days with an inline AR(1) and a moving-block-bootstrap CI
it then had to disown (point estimate outside its own CI). Track R's estimate_tau_half
(quant/stats/tau_half.py) already documents EXACTLY that failure from its 2026-08-31 Monte
Carlo (MC1: block resampling of levels chops persistence; 0-7% coverage at rho>=0.9) and
carries the fix (Kendall correction + parametric pivot bootstrap). F1b re-runs the same
composite through the library estimator. MEASUREMENT (no bar): corrected tau_half + 90% CI
in months vs the ladder's [1,3]; near_unit_root flag reported (Andrews remains the
data-phase substitute if flagged). Script: scripts/analyze_f1b_tau.py.

| # | What | Result | Status |
|---|---|---|---|
| F1b | Corrected tau_half of the L2 composite | Kendall-corrected 3.18 months (naive 2.92), 90% CI [2.39, 5.72]m, near_unit_root FLAGGED (rho 0.99 daily — the CI itself degrades there per the estimator's own MC1 docs; Andrews at data phase). The CI OVERLAPS the registered [1,3]m band, so under tau_half_drift_policy's hysteresis the config value STANDS — with a LENGTHENING watch noted (the estimate sits at/above the band top; the DD leg's mechanical persistence is a suspected contributor, a construction note for full F1) | measured; config stands, drift watch set |

## Entry F2-WF (2026-09-02) — fold-consistency of the F2-index shortlist (M4 harness's first run)
PRE-REGISTERED before running. Script: scripts/analyze_f2_walkforward.py. The two ADOPTABLE
shortlist cells from F2-index ({trig 0.80, 1-of-2} x {calendar, decay}) re-evaluated over
4 disjoint eras (M4 harness: n_folds=4, min_train=504bd, embargo=63bd ~ the F1b tau_half).
The rule is parameter-free and expanding, so folds test CONSISTENCY: was the cell's value
one episode's gift? BARS (per cell): keeps its shortlist seat if per-era drag <= 2.0pp/yr
in >= 3 of 4 eras; deep-episode DD improvement reported per era containing one (only 2
exist — no bar on that leg, stated). PhaseD is NOT re-run (display-only per F7a).

| # | What | Result | Status |
|---|---|---|---|
| F2-WF | Shortlist fold-consistency | **BOTH CELLS FAIL (2/4 eras within budget each)** — the full-period drags (1.23/1.83pp) were flattered by the quiet 2009-2018 eras; the 2018-2022 and 2022-2026 eras run +2.5 to +4.1pp/yr of whipsaw. The shortlist is now EMPTY of adoptable cells at index level pending full F2 — the M4 adjudicator doing its registered job on its first run. What survives in the print: in the COVID era the same cells cut the crash DD 37%→26% — the insurance economics quantified (premium 2.5-4pp/yr in whipsaw-rich eras vs an 11pp payout when the deep episode lands). Dissection note: the per-era <=2pp bar is STRICTER than the DESIGN budget's program-average framing — recorded, not relitigated; full F2's registered currency (episode DD net of costs, M4-judged, book-level) adjudicates | both fail; era-dependence measured |

## Entries H67a / H68a (2026-09-02) — the phase file's remaining gates, at index resolution
PRE-REGISTERED before running. Script: scripts/analyze_phase_gates.py. Data: the vaulted
index; the same L2 composite/phase construction as F7a (k_slope=21, smooth=5). F7a closed
H66's fast-band leg (FAIL); these two close the file at this resolution.
- H67a (dead-band calibration — MEASUREMENT, no bar): for the registered dead-band grid
  {0.15, 0.25, 0.35}, count direction flips per year and the median run length. The grid's
  JOB is hysteresis; the print shows what each point buys. No adoption question arises
  (phase is display-only per F7a) — this calibrates the DISPLAY.
- H68a (age effect): within high-state days (state pctile >= 0.8), does quadrant AGE add
  information — median forward 63bd return of YOUNG (age <= 21bd) vs OLD (age > 21bd)
  high-state days, sampled every 21st qualifying day per group. PRIOR STATED: FAILS (F7a
  showed the level carries the rebound; age is direction's cousin). BAR: |median
  difference| must exceed 2pp with MW two-sided p < 0.10 AND n >= 10 per group to count as
  an effect; anything less = no age effect, the display keeps age as a caption only.

| # | What | Result | Status |
|---|---|---|---|
| H67a | Dead-band grid flip counts | 7.4 / 6.9 / 6.0 flips-per-year across {0.15, 0.25, 0.35}; median runs 25-27bd — the display is stable at every grid point; 0.35 buys the longest runs (mean 38bd). Calibration recorded; display keeps the registered mid-point 0.25 (no reason to move) | measured, display calibrated |
| H68a | Age effect at high state (prior: fails) | young (age<=21bd) median fwd63 +6.17% vs old +5.65% — diff 0.52pp, MW p=0.843: **NO age effect, prior lands.** With F7a (direction) and H68a (age) both failed at index resolution, THE PHASE FILE CLOSES: the LEVEL carries all measurable information; quadrant and age are captions for the reader, not inputs for a rule | fail-as-predicted; phase file closed |

## Entry F1c (2026-09-02) — the near-unit-root re-estimate F1b's flag queued
PRE-REGISTERED before running. F1b flagged rho~0.99 daily (near_unit_root: the Kendall
path's CI degrades there per MC1); the queued remedy — Andrews-style median-unbiased
inversion — is now built and Monte-Carlo tested (quant/stats/andrews.py). F1c re-estimates
the L2 composite's tau_half with it. MEASUREMENT (no bar): rho_mu + simulated central
interval, in months, vs the ladder's [1,3] and F1b's 3.18m [2.39, 5.72]. Script:
scripts/analyze_f1c_andrews.py. Grid-edge hits reported, never hidden.

| # | What | Result | Status |
|---|---|---|---|
| F1c | Andrews tau_half of the L2 composite | median-unbiased rho 0.9897 -> tau 3.19 months, 90% interval [2.19, 4.63]m (no grid edge) — CORROBORATES F1b's 3.18m with a tighter, properly-constructed interval; two independent estimators agree; the lengthening watch STANDS (the interval still reaches above the band top); the P3 Andrews queue item is DONE | measured, convergent |

## Process/design note (2026-09-02) — the machinery flagged an episode the pre-named list lacks
The Stage-1 regime demo (regime-DEMO.md) independently printed a 14-session R4 episode over
2016-02-11..2016-03-01 — the global-selloff bottom — which is NOT in the §3 pre-named
episode set of docs/cycles/02-fast-stress.md (that list has "Aug 2015 China deval" but
nothing for the Jan-Feb 2016 continuation). DISCIPLINE APPLIED: the §3 set stays FROZEN for
every design already registered against it (F2a/F2-index/F7a/FS-D3 denominators are
untouched — adding an episode after seeing rule results is exactly the door the freeze
exists to close). CONSEQUENCE REGISTERED: when the FULL F2's episode set is re-frozen
before its PIT run, the Feb-2016 window is a candidate for inclusion, to be decided from
the public record BEFORE any rule output on it is seen; this note is the dated evidence
that the candidate was raised by the state machinery, not cherry-picked afterward.

## Entry H53a (2026-09-02) — the ToT→INR link: H53's first-test first LINK, bounded
PRE-REGISTERED before running. Script: scripts/analyze_tot_inr.py. Data: vaulted IMF PCPS
monthly (1980-2017) + the new INR/USD monthly vault (Fed H.10 mirror, 4/4 anchors). H53's
registered first test asks whether the ToT state adds to L9's India transfer via the
INR/CAD channel; CAD is not vaulted, so this bounded leg tests only the channel's FIRST
LINK — do commodity-price moves transmit to the currency at all?
DESIGN: non-overlapping calendar-year (Dec-to-Dec) log changes, 1980-2017 overlap (n~36).
Primary: PCPS Fuel(Energy) index (India's dominant commodity import) vs INR/USD change
(positive = depreciation). MECHANISM PRIOR: energy up => ToT worse => INR depreciates =>
POSITIVE Spearman. BAR: rho > 0 AND one-sided p < 0.10. Secondary (no bar): the
All-Commodity index. CONFOUND STATED NOW: nominal INR trends on inflation differentials;
annual CHANGES limit but do not remove this; the full H53 test (real exchange rate + CAD,
purged) remains registered and is NOT discharged by this link check.

| # | What | Result | Status |
|---|---|---|---|
| H53a | Energy-price change → INR depreciation (annual) | **FAIL — with an INVERTED sign**: Fuel/Energy rho = −0.518 (p one-sided 0.995), All-Commodity −0.635; effective window 1993-2016, n=24 (the PCPS columns' NaN head shrank the registered ~36 — recorded, bar unmoved). Dissection: commodity booms are GLOBAL RISK-ON years with EM inflows — INR APPRECIATES when commodities rise (2003-07) and weakens when they crash (2008/2013/2015); the common global factor owns both series, so the unconditional ToT channel is not identifiable and points the wrong way. CONSEQUENCE: H53's registered full test ('does the ToT state ADD TO L9') was the right formulation all along — the candidate can never be promoted on any unconditional print, and this fail is the evidence why. The naive 'oil up = INR down = India down' desk heuristic is hereby a measured casualty | fail, sign inverted; conditional-only framing locked |

## Vault admission (2026-09-03) — India VIX daily 2010-2023, TradingView-export mirror
Source: github.com/Gaurav7888/Predicting_Market_Volatility @ 1ee886e, "NSE_INDIAVIX, 1D.csv"
(TradingView daily export). Two-pass AUTHENTICATION (ingest/vault/vix/): **6/6 anchors PASS**,
including the exact published all-time closing high 83.6075 on 2020-03-24 and 0.728 monthly
level correlation with the CBOE VIX vault; both Saturday budget sessions present. The weakest
provenance chain admitted so far (NSE → TradingView → user export → GitHub) — admitted on
anchors, with the NSE primary pull STILL REQUIRED on the runsheet (bhavcopy precedent).
Coverage 2010-07-23..2023-04-05: no 2009 head, no post-Apr-2023 tail — every consumer below
is a PARTIAL of its parent and quotes the parent verbatim (process note #5).

## Entries CW-D1v / F5a (2026-09-03) — PRE-REGISTERED before any number is computed
**CW-D1v — the VIX leg of CW-D1, partial (mirror coverage).** Parent design QUOTED VERBATIM
from its 2026-09-02 registration: "CW-D1 (daily budget-window vol): India VIX daily (NSE,
2009-) + NIFTY daily around budget days vs matched non-event days; bar: one-sided p < 0.05
on budget-day ±1 |return| and VIX change (n≈18 budgets+interims). Pre-2001 5pm-presentation
era excluded by design (event-day definition break)."
Partial scope fixed now: VIX leg ONLY (the return leg already graded — CW-D1a, both prints
booked). Event set = the canonical BUDGET_DAYS list (scripts/analyze_nifty_daily.py)
intersected with the vault span = 15 events (2011-02-28 .. 2023-02-01, incl. interims
2014-02-17 and 2019-02-01; DEVIATION from parent n≈18 stated: mirror coverage). Reading of
"VIX change" fixed BEFORE the run: PRIMARY BAR = |Δlog VIX| on budget-day ±1 window days vs
all other days, one-sided Mann-Whitney (elevated), p < 0.05. SECONDARY (descriptive, no
bar): signed mean Δlog VIX split by day −1 / day 0 / day +1 — the uncertainty-resolution
shape (run-up, then crush) is reported, never graded. Saturday budget sessions are present
in the vault, so no event-day remapping is needed.

**F5a — partial of F5 (daily closes only, mirror coverage).** Parent QUOTED VERBATIM from
docs/cycles/02-fast-stress.md §"harvest": "F5 | India-VIX vs RV redundancy + VRP | IV rank
vs RV rank correlation + incremental AUROC; IV−RV spread (variance-risk-premium proxy) as
separate candidate | Redundant ⇒ RV stays primary (longer history); IV adds ⇒ confirm seat;
VRP tested as its own pre-registration before any use."
Partial scope fixed now: (i) RV = 21d realized vol of the NIFTY 50 index vault, expanding
percentile (house construction, min_obs=252 — the DW1/F2a machinery); IV = expanding
percentile of India VIX close (min_obs=252 ⇒ usable from ~2011-07). (ii) REDUNDANCY BAR:
Spearman(IV pctile, RV pctile) ≥ 0.80 on days where both exist ⇒ REDUNDANT (RV stays
primary, per parent rule). (iii) ADDS BAR: AUROC(IV pctile → §3 in-span episode days) ≥
AUROC(RV pctile → same) + 0.03, evaluated ONLY on days where both legs exist; episode set =
the frozen §3 in-span list intersected with the joint span (expected: EU-2011*, taper,
China-deval, demonetization, Feb-2018, IL&FS, COVID, Russia-2022; *EU-2011 clipped by IV
warm-up — days actually covered are printed, set frozen regardless). If NEITHER bar fires:
"correlated but not additive" ⇒ RV stays primary. (iv) VRP proxy (IV² − 252·21d-RV², daily,
annualized): DESCRIPTIVE PRINT ONLY — mean/quartiles/sign frequency; consumption requires
its own future registration per the parent's decision rule. This partial CANNOT confirm the
IV seat (parent requires the full series + M4); it can only kill redundancy or record adds.

| # | What | Result | Status |
|---|---|---|---|
| CW-D1v | Budget-day ±1 \|Δlog VIX\| elevated vs other days | **PASS** — window \|dlogVIX\| median 5.53% vs 2.60% elsewhere, one-sided MW p = 2.7e-06 (n=45 window days, 15 events). DESCRIPTIVE (no bar): mean dlogVIX is NEGATIVE all three days — day −1 −1.8%, day 0 **−8.9%**, day +1 −2.9% — the uncertainty CRUSH: implied vol is bid before the window opens and collapses through the speech. Both CW-D1 legs are now graded (return leg: CW-D1a's parent-window print p=0.0049) — the parent CW-D1 is DISCHARGED at mirror coverage; the 2009/2024-26 events remain unobserved (NSE primary pull) | **pass (partial, 15/≈18 events)** |
| F5a | IV-vs-RV redundancy + incremental episode AUROC | Neither bar fired ⇒ the registered fallback: **correlated but not additive — RV stays primary** (the parent's own decision). Spearman(iv_p, rv_p) = 0.763 (redundancy bar ≥0.80 not met); AUROC(IV→episodes) = 0.770 vs AUROC(RV) = 0.786 on 2,866 joint days, 8 frozen episodes covered — the domestic implied leg is a slightly WORSE episode classifier than realized vol, echoing FS-D3's refusal of the global leg. VRP proxy (descriptive only): mean +0.0076 ann-variance, positive 85.4% of days — the premium exists; consumption still requires its own registration. The full F5 (proper series + M4) stays owed | **rv-primary (partial)** |

## Vault admission (2026-09-03) — the Kilian index + the Känzig oil-supply-news shocks
Two files into ingest/vault/commodities/ under the dated two-pass section there: the monthly
Kilian global-real-activity index 1973-2019 (replication-repo mirror, weak chain, **5/5
anchors** incl. the published boom peak 190.7 in 2008-05 and 0.634 cross-vault Spearman with
PCPS YoY) and Känzig (2021 AER) oil-supply-news shocks vintage 2025M12 (**the author's own
repo** — primary-grade; **4/4 anchors**, all three documented OPEC-event signs correct).
Runsheet's Kilian/BH row → PARTIALLY MIRRORED; BH decomposition + post-2019 Kilian months
still owed.

## Entry OL-D1a (2026-09-03) — PRE-REGISTERED before running: OL1 with the REAL structural flavor
Parent design QUOTED VERBATIM (research/cycles/oil-fold/partDH-verdict-routing.md): "**OL-D1**
the Kilian-index pull + replication of OL1 with structural flavors (acceptance registered at
pull; the desk expects the asymmetry to SURVIVE but shrink once the global factor is
controlled)." Parent trial OL1 QUOTED VERBATIM (ledger 2026-09-02): "among oil-UP years
(annual real oil return > +10%), mean India return in demand-flavored years MINUS mean in
supply-flavored years. Bar: difference ≥ +10pp (demand-flavored oil-up years materially less
damaging). n will be small — stated." OL1's print: +38.1% vs −43.1% (spread +81.2pp, n=11:
8/3), PASS capped BECAUSE the flavor proxy was the global-equity sign itself.
This is acceptance-at-pull; bars fixed NOW:
- Construction: OL1's verbatim, changing ONLY the flavor definition: a year is
  demand-flavored if its mean monthly Kilian index EXCEEDS the prior year's mean (global
  real activity rising), supply-flavored otherwise. Oil return and India leg exactly as OL1
  (annual real oil return > +10%; India = annual iima MF return, 1994-2015; mirror coverage
  1973-2019 covers all of it).
- PRIMARY BAR (unchanged from parent): demand-flavored mean MINUS supply-flavored mean
  ≥ +10pp among oil-up years. Desk prior ON RECORD: PASSES but the spread SHRINKS below
  OL1's +81.2pp.
- SECONDARY (descriptive, no bar): the flavor-agreement table — in how many of the n
  oil-up years do the Kilian flavor and OL1's equity-sign flavor coincide; plus each year
  named with both flavors. If n in either flavor cell is 0, the primary is UNTESTABLE and
  recorded as such (no bar moved).

| # | What | Result | Status |
|---|---|---|---|
| OL-D1a | OL1 replicated with Kilian-index flavor | **PASS — and the desk's registered prior printed true on BOTH halves**: demand-flavored +36.8% vs supply-flavored −9.1%, diff **+46.0pp** (bar ≥ +10pp), the spread SHRINKING from OL1's +81.2pp exactly as predicted. The flavor split rebalanced 8/3 → 6/5 and agrees with the equity-sign proxy in only 7/11 oil-up years — OL1's proxy really was measuring risk appetite, and the REAL activity flavor still separates India's oil-up outcomes decisively (1999/2003/2007 demand-years +84/+97/+59% vs 2008/2011 supply-years −62/−31%). The supply-flavored mean softened from −43.1% to −9.1% (1996 and 2005-06 reclassified) — the asymmetry is real but the catastrophe cell was partly the equity sign talking to itself. Consumption: the L9 oil fold's shock-type briefing table now carries a MEASURED structural print; still no standalone signal (n=11, annual) | **pass, prior confirmed (partial: Kilian mirror 1973-2019)** |

## Vault admission (2026-09-03) — ONI seasonal 1950-2026 + AISMR JJAS 1872-2016
Two mirrors into ingest/vault/climate/ (dated two-pass section): the NOAA CPC ONI table
(ahuang11/ninodata mirror, **5/5 anchors** incl. the exact 1997 peak +2.40) and the
IITM-shape all-India summer-monsoon series (student-repo vendored, weak chain, **5/5
anchors** incl. 1877's 604mm and the canonical 848.2mm mean confirming units). Runsheet's
ONI+IMD row → PARTIALLY MIRRORED (IMD %-of-LPA official bulletins + post-2016 rainfall
still owed).

## Entry EN-D2a (2026-09-03) — PRE-REGISTERED before running: the first-link contingency,
computed at last. Parent design QUOTED VERBATIM (research/cycles/enso-deep/partCDEFH.md):
"**EN-D2** the chain contingency table maintained live (cases chapter's base-rate exhibit,
re-printed annually)." The B4a exhibit's own [VERIFY] flag records three UN-RECONCILED
countings (71% / 44% / 47%) with a defended range of "roughly 45-70%". This partial computes
the FIRST LINK ONLY (El Niño → all-India monsoon deficiency) on the two vaulted series with
ONE fixed definition pair, resolving that flag with a reconciled counting. Definitions fixed
NOW, before any table is computed:
- EL NIÑO YEAR (primary): mean ONI anom over the monsoon-season windows MJJ, JJA, JAS, ASO
  of year Y ≥ +0.5. (Secondary, descriptive: Y counted El Niño if ≥3 of those 4 seasons
  carry the file's own CPC-style el_nino label.)
- DROUGHT/DEFICIENT YEAR: JJAS(Y) < 90% of LPA, LPA = the vaulted series' full-sample mean
  (self-referenced, no magic number). Sensitivity print (no bar): LPA = 1961-2010 mean.
- SPAN: the joint 1950-2016. ERA SPLIT as registered in the cases chapter: 1950-1969,
  1970-1990, 1991-2016 (the Green-Revolution / liberalization / inflation-targeting
  boundaries; the 2016 IT boundary leaves no post-2016 rainfall in this vault — stated).
- OUTPUT: the full 2×2 (El Niño × deficient) pooled + per era; P(deficient | El Niño),
  P(deficient | not), and the lift.
- VERIFICATION BAR (on the compilation, not a promotion bar): pooled P(deficient | El Niño)
  ∈ [45%, 70%] — the record's own defended range. Outside ⇒ a recorded miss on B4a's
  compilation; the computed table stands either way and the [VERIFY] flag resolves.
This partial does NOT run EN-D1 (sector returns + food-CPI remain data-gated) and promotes
nothing (H55 stays Tier-C candidate; Contract §4 requires the purged era-split EN-D1).

| # | What | Result | Status |
|---|---|---|---|
| EN-D2a | First-link contingency (computed, reconciled) | **VERIFICATION BAR PASS — the [VERIFY] flag resolves**: pooled P(deficient \| El Niño) = **56.2%** (9 of 16), inside the defended [45,70]%; base rate without El Niño **14%** → lift **4.1x** — the first link is real and now stands on one reconciled counting instead of three irreconcilable ones. THE SHARPENING: era-split shows the METEOROLOGICAL link STRENGTHENING (1950-69: 29%, lift 1.9x; 1970-90: 100% on n=3; 1991-2016: **67% vs 5%, lift 13.3x**) — the non-stationarity the cases chapter documented (falling drought severity/impact) lives in links 2-3 (Green-Revolution and policy buffers), NOT in link 1. 1997 confirmed as the great save (El Niño, no deficiency); 2014 deficient but sub-threshold on the primary definition (borderline, noted). Robust: secondary CPC-label definition agrees 94%; LPA choice immaterial (56% either way). H55 stays Tier-C candidate — EN-D1 (sector returns + food-CPI, purged, era-split) remains the promotion test | **bar pass; [VERIFY] resolved (partial: link 1 only)** |

## Entry OL-D2a (2026-09-03) — PRE-REGISTERED before running: the windfall reverse experiment
Parent design QUOTED VERBATIM (research/cycles/oil-fold/partDH-verdict-routing.md): "**OL-D2**
the windfall asymmetry (supply-driven oil-DOWN years — 2014-16 — as the reverse experiment;
design only, n tiny)." The instrument the design lacked is now vaulted (Känzig 2021 supply-news
shocks, author-repo, 4/4 anchors). Bars fixed NOW:
- Construction: OL1's verbatim oil/India legs (annual Brent log return; India = annual iima MF
  return, 1994-2015). OIL-DOWN year: annual log oil return < −log(1.10) (the mirror of OL1's
  +10% up-threshold). FLAVOR (the pre-stated instrument): a down-year is SUPPLY-DRIVEN if the
  annual SUM of Känzig monthly news shocks < 0 (net supply-expanding news, price-falling);
  DEMAND-DRIVEN otherwise. (Känzig sign convention: positive = supply-contractionary.)
- PRIMARY BAR: mean India return in supply-driven down-years MINUS demand-driven down-years
  ≥ +10pp (the windfall: an importer should fare better when oil falls because of supply).
  DESK PRIOR stated: expected to PASS, at MICROSCOPIC power (n≈4-5 down-years total) — a
  fail at this n refutes nothing and is recorded as underpowered, not as a death.
- SECONDARY (descriptive): the year table with BOTH instruments (Känzig annual sum + the
  Kilian activity direction from OL-D1a) — instrument agreement reported.
- Empty cell ⇒ UNTESTABLE recorded, bar unmoved.

| # | What | Result | Status |
|---|---|---|---|
| OL-D2a | Windfall asymmetry in oil-DOWN years | **FAIL — underpowered exactly as pre-stated (n=4, one cell n=1), and the dissection is the finding**: supply-driven downs (1998/2001/2015 per Känzig) averaged −14.7% for India vs the sole demand-driven down (2009) at +87.8% — diff −102.5pp against a +10pp bar. But 2009 is the GFC-rebound year AND an annual-averaging artifact (oil's 2009 annual mean sits below 2008's even though oil RALLIED all year — the same artifact OL1 documented for 2008); and the three supply-driven downs are Asian-crisis, dotcom and China-slowdown years — **the global factor owns oil-DOWN years exactly as it owned the ToT→INR link (H53a)**. Instruments diverge as they should: Känzig calls 2009 supply-CONTRACTIONARY (OPEC's Dec-2008 cuts) while Kilian activity fell in all 4 years (agreement 1/4). CONSEQUENCE: the windfall claim survives only CONDITIONALLY (net of L9's global state) — 'oil crash = India windfall' joins 'oil up = INR down' in the measured-casualty column at descriptive grade; no unconditional briefing line ships | **fail (underpowered, as pre-stated); conditional-only framing — the H53a rhyme** |

## Entry F3a (2026-09-03) — PRE-REGISTERED before running: vol-managed NIFTY, the index partial
Parent design QUOTED VERBATIM (docs/cycles/02-fast-stress.md harvest table): "F3 |
**Vol-managed Nifty (two-sided)** | Moreira-Muir c/σ̂² scaling, full-period AND Cederburg
real-time OOS protocol; costs in | Stated prior: DD control robust, alpha unproven. Either
result documented; alpha claim may NOT be promoted from full-period evidence alone."
Partial scope FIXED NOW (mirror coverage: NIFTY 50 index vault 2007-09..2026-04; the full F3
on PIT data remains owed):
- Construction: MONTHLY strategy. w_t = c / σ̂²_{t−1}, σ̂²_{t−1} = previous month's realized
  variance of daily returns (annualized), applied over month t. Buy-hold = the index.
- Cell F3a-1 (full-period, uncapped — the literature replication): c set so managed
  unconditional monthly vol equals buy-hold vol (the MM convention). DOCUMENT: monthly
  regression alpha of managed on buy-hold (t-stat, NW lags 3), Sharpe pair, maxDD pair.
  PRIOR: direction per MM plausible, magnitude unproven for India; nothing promotes.
- Cell F3a-2 (Cederburg real-time OOS): c re-estimated EXPANDING (only data through t−1;
  first 36 months warm-up), same scaling. DOCUMENT: OOS Sharpe(managed) − Sharpe(buy-hold),
  with a 90% CI from quant/stats/bootstrap.stationary_bootstrap on the monthly return
  difference (mean_block=6 months, n=2000, seed=0 — first seed, no curation). PRIOR ON
  RECORD: the improvement is ABSENT out-of-sample (the Cederburg-et-al. finding
  generalizes); i.e., the CI includes 0.
- Cell F3a-3 (desk-feasible): weights CAPPED at 1 (no leverage — funding_rate is unset and
  the leverage feature is dark), NET of costs at 16 bps per unit turnover (index_futures
  registry HI end, conservative; |Δw| monthly). DOCUMENT: maxDD delta vs buy-hold, net
  annualized drag/premium, COVID-window DD. PRIOR: DD improves but by LESS than the
  F2-index fast-trigger cells (vol scaling is slower than trigger logic) at lower whipsaw
  cost.
No promotion bar exists by the parent's own rule — these are documentation cells with
priors; consumption is knowledge for the full F2/F3 adjudication, never an armed rule.

| # | What | Result | Status |
|---|---|---|---|
| F3a-1 | MM full-period replication (uncapped) | **The parent's prior verbatim, in numbers**: alpha +5.76%/yr at NW t=1.67 — positive, NOT significant (alpha unproven, exactly as stated); Sharpe 0.61 vs 0.51; maxDD 26% vs 55% (DD control robust, exactly as stated). Weights ranged 0.03-6.12 (mean 1.16) — the uncapped strategy LEVERS 6x in calm, which the desk cannot do (funding_rate dark) | documented; prior confirmed both halves |
| F3a-2 | Cederburg real-time OOS Sharpe diff | **Prior CONFIRMED: the improvement is absent out-of-sample.** Expanding-c real-time: OOS Sharpe 0.60 vs buy-hold 0.62 (diff −0.02); mean return diff +8.05%/yr but 90% stationary-bootstrap CI [−0.97, +17.41]%/yr INCLUDES 0 (mean_block=6, seed=0) — the extra return arrives with proportional extra vol and huge dispersion. The Cederburg finding generalizes to India at index resolution | documented; prior confirmed |
| F3a-3 | Capped-at-1, net-of-cost DD economics | **Prior WRONG in direction on DD — recorded**: the desk-feasible capped variant's maxDD is 22% vs buy-hold 55% (COVID window 10% vs 23%) — BETTER than the F2-index fast-trigger survivors (26% COVID DD), not worse as registered. The price is why it still cannot arm: **−4.86%/yr net drag** (mean weight 0.73 in a rising market; costs trivial at 0.32%/yr on 2x annual turnover) — roughly double the F2 cells' whipsaw-era premium and far outside any drag budget. The insurance-economics doctrine sharpens: continuous de-risking buys MORE protection at MUCH higher premium than episode-triggered de-risking; the full F2/F3 must adjudicate this trade at book level, and the desk cannot access the levered side of MM at all | documented; DD prior missed, recorded |

## Entry F4a (2026-09-03) — PRE-REGISTERED before running: the correlation-spike leg, survivor partial
Parent design QUOTED VERBATIM (docs/cycles/02-fast-stress.md harvest table): "F4 |
**Correlation-spike increment** | Mean pairwise correlation (top-50 names, window grid)
percentile; incremental episode AUROC over RV alone | Adds ⇒ enters as confirm input
candidate; redundant ⇒ documented, excluded."
Partial scope FIXED NOW (data: the SURVIVOR panel 2012-2021, survivorship stated — one-way
reading declared below):
- Top-50: by PREVIOUS calendar year's median daily value traded (n500_value_traded),
  refreshed each January — real-time-safe by construction.
- Signal: mean pairwise correlation of daily returns across the top-50, trailing windows
  {21, 63} days (the house month/quarter grid); expanding percentile, min_obs 252.
- RV leg: the index vault's 21d realized-vol expanding percentile (the F5a construction,
  verbatim); all comparisons on joint non-NaN days.
- BARS (the F5a house precedent, quoted): REDUNDANT if Spearman(corr_p, rv_p) ≥ 0.80;
  ADDS if AUROC(corr_p → episodes) ≥ AUROC(rv_p → episodes) + 0.03. Episodes = frozen §3
  in-span (2012-2021): taper, China deval, demonetization, Feb-2018, IL&FS, COVID (6).
- ONE-WAY READING (survivorship): dead names were disproportionately high-vol; their absence
  most plausibly SMOOTHS the correlation signal's stress spikes, but the bias direction on
  the AUROC increment is not provable here. Declared: a REDUNDANT / no-adds print is
  decisive-leaning (the leg failed even on clean survivors); an ADDS print caps at
  "[VERIFY-PIT] confirm-input CANDIDATE" — the parent's promotion needs the PIT panel.

| # | What | Result | Status |
|---|---|---|---|
| F4a-21d | redundancy + adds, 21d window | Spearman(corr_p, rv_p) = 0.765 (below the 0.80 redundancy bar) BUT AUROC 0.716 vs RV's 0.748 — the correlation leg is a WORSE episode classifier; parent rule ⇒ **EXCLUDED as confirm input**. 1,745 joint days 2014-2021; 5 of 6 in-span episodes covered (taper lost to percentile warm-up — stated); days with a zero-variance top-50 name drop mechanically (suspended names) | **excluded (one-way: failed to add even on flattered data)** |
| F4a-63d | redundancy + adds, 63d window | Spearman 0.649, AUROC 0.663 vs RV 0.759 — even further from adding at the quarter window | **excluded** — and the doctrine consolidates: F4a + F5a + FS-D3 make it THREE candidate confirm-inputs (cross-sectional correlation, domestic implied vol, global implied vol) refused at index resolution; the L2 composite's realized-vol spine is now measured against every proposed echo and kept all three times | **excluded; the RV-spine doctrine, third print** |

## Entry F6a (2026-09-03) — PRE-REGISTERED before running: the whipsaw/false-fire ledger, index partial
Parent design QUOTED VERBATIM (docs/cycles/02-fast-stress.md harvest table): "F6 | **Whipsaw /
false-fire ledger** | Full threshold-grid table: false-fire rate, round-trip cost per false
fire by book, missed-episode rate (per §4's measured-bound rule) | The de-risk rule must
clear the cost-in-SR speed limit per book; Conservative likely needs the slowest cell —
documented per book."
Partial scope FIXED NOW: the F2-index grid VERBATIM (same state construction, same 18 cells:
triggers {0.80, 0.90, 0.95} × confirm {1-of-2, 2-of-2} × re-entry {decay, phaseD, calendar};
same frozen episode list; same COST=28bps per unit turnover). Definitions fixed:
- FIRE = an entry into the de-risked position (the grid's own fires counter, start-indexed).
- TRUE fire = start date inside any frozen episode window; FALSE fire otherwise.
- MISSED episode = a deep episode (buy-hold window DD ≥ 20%, the grid's own bound) with no
  fire starting inside its window.
- Ledger per cell: fires/yr, false-fire share, missed-deep-episode count, whipsaw cost/yr at
  three cost points {8, 16, 28} bps per unit turnover (index-futures registry lo/hi + the
  parent grid's own 28) — the PER-BOOK cost-in-SR grading is the full F6, NOT discharged
  here (books need their own mixes and the M4 frame; stated).
No pass/fail bar (documentation trial per parent); priors ON RECORD: (i) false-fire share
FALLS as trigger rises and confirm tightens; (ii) the 0.80/1-of-2 survivors of F2-index pay
the HIGHEST whipsaw cost; (iii) 0.95/2-of-2 misses at least one deep episode (the speed
trade-off has two ends).

| # | What | Result | Status |
|---|---|---|---|
| F6a | 18-cell false-fire ledger | **The premium decomposed**: whipsaw TRANSACTION cost is 0.02-0.28%/yr across the entire grid at {8,16,28}bps — a rounding error against F2-WF's 2.5-4pp/yr drags, which are therefore ~pure EXPOSURE drag (time de-risked), not trading cost. Prior (i) CONFIRMED: false-fire share falls monotonically 58%→0% as trigger rises and confirm tightens. Prior (ii) CONFIRMED: the F2-index survivors (0.80/1-of-2 decay+calendar) pay the highest non-phaseD whipsaw (0.10%/yr at 28bps; the phaseD re-entry family re-fires pathologically — up to 1.0 fires/yr at 89% false — and was never a survivor). Prior (iii) MISSED as testable: only 2 deep episodes in-span and GFC is warm-up-untestable (the state is NaN through most of it — the F2a shadow), so the one testable deep episode is COVID and even the slowest cell (0.95/2-of-2) caught it; n=1, underpowered, recorded not moved. CONSEQUENCE for B3-1: the drag budget decision is really an EXPOSURE-drag budget — transaction cost needs no budget line at index-futures scale | **documented; 2 priors confirmed, 1 missed (n=1), the drag decomposition ships** |

## Entry H58-D3a (2026-09-03) — PRE-REGISTERED before running: expiry-day noise, index partial
Parent design QUOTED VERBATIM (ledger 2026-09-02): "H58-D3 (expiry-day noise):
|close-to-close| and close-auction behavior on expiry days vs matched weekdays (bhavcopy).
Expiry weekday is CONFIG, not constant — the 2024-25 SEBI curbs + exchange moves make
hardcoding a bug (documented in the module)." The block's framing binds: "Pure ops (no alpha
claim anywhere in this block)".
Partial scope FIXED NOW (index vault; the close-auction leg needs bhavcopy and is NOT
discharged): expiry day = the LAST trading Thursday of each calendar month, shifted to the
immediately preceding trading day when that Thursday is a holiday (2007-2026; the monthly
F&O expiry convention across this sample — the 2024-25 weekday moves affect WEEKLY expiries,
noted, and the sample's monthly convention is checked against the holiday-shift rule, with
the module's config-not-constant warning carried). MATCHED CONTROL: all OTHER trading
Thursdays (weekday-matched by construction — necessary because weekly Thursday expiries from
2019 make Thursday itself special).
- Cell 1 (full sample): median |close-to-close| on monthly-expiry days vs other Thursdays;
  two-sided Mann-Whitney p. DESCRIPTIVE — no bar, per the parent's no-alpha framing;
  consumption is the exclusion calendar's mechanical-prudence rule, unchanged either way.
- Cell 2 (era split, descriptive): pre-2019 vs 2019+ (the weekly-expiry era).

| # | What | Result | Status |
|---|---|---|---|
| H58-D3a | Expiry-day |ret| vs other Thursdays | **No index-level expiry effect**: 224 monthly-expiry days median \|ret\| 0.674% vs 0.574% on 702 other Thursdays, two-sided p=0.211; weaker in both eras (pre-2019 p=0.345; weekly-era p=0.479). At close-to-close index resolution the expiry day is an ordinary Thursday. The exclusion calendar's expiry rule stays exactly what the parent said it was — mechanical prudence, no alpha claim, no measured index cost of ignoring it — and its true object (single-stock close-auction mechanics) remains bhavcopy-gated | **documented; null at index resolution** |

## Entries HG1 / BW1 (2026-09-03) — the two frozen future sweeps, PRE-REGISTERED YEARS early
Both sweeps have lived as forward references since design time (config/risk.yaml's
"trial-ledger #1"; config/ladder.yaml's "trial-ledger entry #13"). They will run under
maximum temptation — they size the actual books — so their bars are fixed NOW, while no
number exists to argue with. Both are DATA-GATED (Phase-0 PIT bhavcopy + the rebuilt episode
table) and DECISION-GATED as stated below; this entry discharges the forward references.

**HG1 — the hedge-grid × regime-bucket joint sweep.**
- GRID (frozen; the validator already refuses alterations): the 7-point hedge grid
  {0, 25, 50, 75, 100, 125, 150}% × the 4 regime buckets = 28 cells, swept JOINTLY,
  exactly as config/risk.yaml's sweep_note states.
- METRIC (PIPELINE.md's own words, quoted): "crisis-insurance currency: payoff in
  worst-decile NIFTY months net of bleed, with India-specific bleed (STT, roll costs)
  validated first".
- BARS, fixed now: a cell is ADMISSIBLE only if (i) mean worst-decile-month payoff net of
  bleed > 0; (ii) annualized bleed ≤ the hedge share of the exposure-drag budget THAT B3-1
  FIXES — if B3-1 is unanswered when the data lands, THE SWEEP MAY NOT RUN (sequencing bar);
  (iii) admissibility must hold era-split in the M4 walk-forward, not merely full-period
  (the F2-WF precedent); (iv) any Sharpe-flavored read deflates with
  n_trials ≥ quant.stats.dsr.census_n() + 28.
- PRIORS on record: R4 cells with hedge ≥ 100% pay their way in crisis months; R1 cells with
  hedge > 25% fail the bleed bar; the two Tier-C hedge-effectiveness placeholders
  ([0.60,0.75] slow-bear, [0.45,0.60] fast-crash) get MEASURED here and their illustrative
  values retire either way.

**BW1 — the regime-score block-weight sweep.**
- INCUMBENT (the standing design split, Tier C by its own provenance): fast_stress 0.25,
  trend_tsmom 0.20, macro_credit 0.20, global_cycle 0.20, valuation_sentiment 0.10,
  calendar 0.05.
- GRID (frozen now): the incumbent plus every single 5pp transfer between an ordered pair of
  blocks (6×5 = 30 candidates; any vector with a block < 0 or > 0.30 is dropped at run time
  and counted). No second transfer, no re-optimization — one step from the incumbent, once.
- BARS, fixed now: a challenger vector REPLACES the incumbent only if it dominates on BOTH
  registered currencies — episode-conditional DD improvement AND full-period exposure drag —
  era-split in M4 with purged CV (embargo per the blocks' tau bands), and survives DSR at
  n_trials ≥ census_n() + |valid cells|. Ties or single-currency wins keep the incumbent
  (the split is a design choice; evidence must beat it on its own stated terms, twice).
- PRIOR on record: the incumbent survives — the F2-WF and F6a prints already show the fast
  block carrying the DD constraint, and no measured result to date argues for moving 5pp
  anywhere else.

| # | What | Result | Status |
|---|---|---|---|
| HG1 | Hedge grid × buckets, 28 cells | (registered; gated on Phase-0 data AND B3-1) | registered design |
| BW1 | Block-weight ±5pp neighborhood | (registered; gated on Phase-0 data) | registered design |

## Principal directive + the reopened generation (2026-09-03, evening)
The principal (in session): "check all top amc and funds and pms/aif/us based... anything
missed or anything can add alpha significantly... new theories that can work in 2026-2040...
then move from cycle to technical-quant-systematic stuff." Candidate generation, closed at
atlas completion, is REOPENED under the same discipline (bars before data; census; DSR;
crowding haircuts). The sweep of record: research/frontier/manager-frontier-sweep.md.
Named candidates from the sweep (registrations deferred to their data, priors stated there):
- **H60-VRP** — India variance-risk-premium harvesting; must era-split at breaks BR3/BR4;
  gated on options-chain data (runsheet). F5a's descriptive print (IV>RV on 85% of days) is
  the motivating observation, quarantined as such.
- **H61-FLOWMULT** — the India price multiplier (Gabaix-Koijen inelastic-markets frame:
  aggregate multiplier ~5 [NBER w28967]); gated on NSDL FPI + AMFI SIP flows (AMFI probed
  BLOCKED at this proxy 2026-09-03 — principal pull; puller exists). Reframes L14's theory.
TRACK T OPENS (technical-quant-systematic; charter in the sweep doc §C): T-series ledger
IDs, same census/DSR/cost law, control-group-first.

## Entries T1 / T-CTRL1 (2026-09-03) — Track T's first pair, PRE-REGISTERED before running
**T1 — overnight/intraday decomposition (index).** Data: the index vault's OHLC (Open
column authenticated with the vault's 6/6 admission). Definitions fixed: overnight
o_t = Open_t/Close_{t−1} − 1; intraday i_t = Close_t/Open_t − 1 (o+i compounds to
close-to-close). Cells: (1) full-sample decomposition — annualized mean of each component
and share of total return; (2) the anomaly test — BAR: the US signature (overnight mean > 0,
intraday mean ≤ 0) with Newey-West t on mean(o−i) ≥ 2; (3) era split at BR3 (2019
weekly-expiry) + COVID-window sensitivity (descriptive). PRIOR on record: signature PRESENT
but attenuated, and mechanically loaded in India — the Indian overnight window carries most
global news (US close → India open). CONSUMPTION CAP stated now: even a PASS cannot arm a
trade (2 trades/day dies at STT instantly); the print's use is EXECUTION TIMING for the
desk's staged deployments (open vs close tranches) and Track T context. No alpha claim.
**T-CTRL1 — the Brock-Lakonishok-LeBaron MA-rule family (the control group).** Track T
opens the way the cycle program opened (ENSO): with the most-mined space in the field and a
registered expectation of death. Rules: the canonical VMA set — fast/slow (1,50), (1,150),
(5,150), (1,200), (2,200), each with 0% and 1% bands = 10 rules; long/flat (no shorting;
flat = 0 excess), signal evaluated on close t−1, position held day t. Costs: 28bps per unit
turnover (the F2-grid convention, quoted). BAR per rule: survives only if net Sharpe >
buy-hold Sharpe AND deflated-Sharpe p < 0.05 at n_trials = census_n() + 10. PRIOR on
record: ZERO survivors. A surprise pass promotes NOTHING — it goes to the challenger lane
discussion like every pass.

| # | What | Result | Status |
|---|---|---|---|
| T1 | Overnight/intraday decomposition + signature test | **PASS — and NOT attenuated (prior half-missed, recorded)**: overnight +24.0%/yr (NW t=+10.5) vs intraday −12.6%/yr (t=−2.9), gap t=+7.6; robust ex-COVID; STRONGER post-BR3 (+41.7%/yr gap). The entire Nifty premium accrues overnight. Consumption cap holds (no trade — STT); the print is EXECUTION-TIMING evidence: staged deployments default to buy-at-close. Full honest read: research/track-t/T-RESULTS.md | **pass; execution-timing consumption only** |
| T-CTRL1 | BLL MA family, 10 rules, net + DSR | **0/10 survivors — the control group died on schedule**: best cells net Sharpe 0.56-0.58 vs buy-hold 0.55, ALL DSR < 0.95 at n_trials=174. Track T's bar is now calibrated by a printed graveyard, as the cycle program's was by ENSO | **prior confirmed (0 survivors)** |

## Entries T3 / T4 (2026-09-03) — Track T backlog pair, PRE-REGISTERED before running
**T3 — dual momentum, NIFTY vs INR-gold (the Antonacci rotation, India version).** Distinct
from TS1 (which tested each asset's OWN trend); T3 tests RELATIVE momentum as a rotation.
- Data fixed: NIFTY monthly (index vault closes); INR-gold = gold_monthly (USD) × the fx
  vault's INR/USD (both authenticated); joint span 2007-10..2026-04 monthly.
- Rule: at each month-end, hold the asset with the higher trailing-k total return; k ∈
  {3, 12} — TS1's two winners (3m won on the index, 12m on gold; a relative rule must pick,
  so both are cells and the TENSION is the point). Long-only, fully invested, switch cost
  28 bps per full rotation (the grid convention; an ETF switch is cheaper — conservative).
- BARS per k-cell: SURVIVES only if net Sharpe > BOTH single assets AND > the monthly-
  rebalanced 50/50 static, AND DSR > 0.95 at n_trials = census_n() + 2. Max-DD vs 50/50
  documented either way.
- PRIOR on record: FAILS the Sharpe bar against the 50/50 static (the diversification
  arithmetic the V-entries measured is hard to beat by timing) but IMPROVES maxDD — the
  desk expects dual momentum here to be a DD tool wearing an alpha costume.
**T4 — the India low-volatility quintile (survivor partial, one-way FAVORING the null).**
- Data: survivor panel daily 2012-2021. Monthly rebalance: rank names with ≥252 trailing
  daily obs by trailing-252d vol; LONG the bottom quintile equal-weight; UNIVERSE = equal-
  weight all ranked names. 2012 warm-up; effective 2013-2021.
- ONE-WAY DECLARED (the reverse of MR1-S's direction): the panel's dead names were
  disproportionately HIGH-vol losers, so their absence flatters the high-vol side and biases
  AGAINST the low-vol premium — a PASS here is decisive-leaning; a FAIL is inconclusive
  (PIT still owed either way).
- BARS: low-vol quintile Sharpe > universe Sharpe AND monthly CAPM alpha vs universe with
  NW t ≥ 2 (both, jointly, = the anomaly present); DSR context at census_n() + 2.
- PRIOR on record: PRESENT (the defensive anomaly is the most replicated cross-sectional
  regularity after momentum, and the one-way bias runs against it here) — but consumption
  even on a pass is CANDIDATE-for-the-factor-library only (a low-vol SLEEVE needs PIT + the
  full cost stack + a McLean-Pontiff haircut conversation).

| # | What | Result | Status |
|---|---|---|---|
| T3-k3 | Dual momentum k=3 vs singles + 50/50 | **FAIL** — net Sharpe 1.14 vs INR-gold alone 1.19 and 50/50 static 1.17; maxDD 23% vs 24% (no DD edge either). Side print worth its own line: INR-GOLD's OWN Sharpe was 1.19 over 2007-2026 (USD gold × depreciation) — the diversifier carried the era | **fail; prior's Sharpe half confirmed** |
| T3-k12 | Dual momentum k=12 vs singles + 50/50 | **FAIL, and the prior's DD half was WRONG (recorded)**: net Sharpe 1.13; in the k=12 window the 50/50's maxDD was 11% vs the rotation's 18% — dual momentum was worse on BOTH axes. The static blend strictly dominated: a relative rule forces one speed onto two assets that TS1 showed trend at different speeds (3m equity / 12m gold), and loses both. The V-entries' diversification arithmetic wins again | **fail both halves; 50/50 dominance recorded** |
| T4 | Low-vol quintile vs universe (one-way) | Signature VISIBLE, bar MISSED: Sharpe 1.45 vs universe 1.34, CAPM beta 0.67, maxDD 24% vs 34% — the defensive shape exactly; but alpha +2.65%/yr at NW t=1.88 < 2 fails the joint bar. Per the DECLARED one-way (survivorship biases AGAINST low-vol), a fail is INCONCLUSIVE — the anomaly is neither confirmed nor dead here; the PIT test stays owed and no factor-library candidacy arises (the bar is the bar) | **inconclusive per one-way; PIT owed** |

## Entry T2 (2026-09-03) — PRE-REGISTERED before running: trend-on-states at the slow band
The frontier sweep deferred T2 until a falsifiable target existed; this is it. The phase
file CLOSED at INDEX RESOLUTION for the fast-stress state (F7a/H67a/H68a) with its reopening
condition stated: "a pre-registered pass at another band or resolution." T2 is that test at
the SLOW band, on the AQR trends-everywhere motif restricted to our consumable form: does
the TREND of a slow macro state add to its LEVEL in predicting India equity?
- Data fixed: Kilian index monthly (vault, 1973-2019) ∩ NIFTY monthly (index vault) =
  2007-10..2019-06, n≈140 months. SMALL — power stated, no subgroup mining.
- Design: next-month NIFTY return regressed on (i) Kilian LEVEL (percentile, expanding on
  the full Kilian history — no warm-up loss in-window) and (ii) TREND = sign of the 12m
  change. NW lags 3. Cells: the level t (context) and the trend t (the bar).
- BAR: the trend term's |NW t| ≥ 2 incremental to level ⇒ the doctrine CRACKS at the slow
  band (and the phase file's reopening clause activates for discussion — nothing reopens
  automatically). PRIOR on record: FAILS — levels-not-directions generalizes.

| # | What | Result | Status |
|---|---|---|---|
| T2 | Kilian trend incremental to level → NIFTY | **FAIL — the prior confirmed and the doctrine extends**: trend-sign beta +0.33%/mo at NW t=+0.48 (bar ≥2, nowhere near); the level itself also unconditional-inert here (t=−0.54, n=142 — consistent with L9's conditional-transfer framing). LEVELS-NOT-DIRECTIONS now has prints at BOTH bands (fast: F7a/H67a/H68a at index resolution; slow: T2 at monthly-macro) and the phase file's reopening clause does NOT activate. The trends-everywhere motif dies in our consumable form | **fail as registered; doctrine at both bands** |

## Entries T1b / T6-TOM (2026-09-03, night) — PRE-REGISTERED before running
**T1b — the overnight drift under stress (T1's conditional follow-on).** T1 printed the
unconditional split; the ops question is whether the overnight accrual SURVIVES stress —
it prices the desk's choice of execution time for de-risk fires (sell at next open vs wait
for close).
- Cells fixed: mean overnight and intraday returns (i) inside the frozen §3 episode windows
  vs outside; (ii) on days where the prior day's rv_p ≥ 0.90 (the state the fires actually
  see) vs below. NW t on the overnight mean within each condition.
- BAR (one, pre-stated): overnight mean IN-EPISODE ≥ 0 with NW |t| < 2 counts as "drift
  ABSENT in stress" (the null); overnight mean in-episode SIGNIFICANTLY NEGATIVE (t ≤ −2)
  = "overnight is where stress lands" — either way the consumption is execution guidance,
  no trade. PRIOR on record: in-episode overnight mean is NEGATIVE (global bad news lands
  overnight in India), i.e., the unconditional +24%/yr drift is a CALM-days phenomenon.
**T6-TOM — turn-of-month, era-split for the SIP age (the H61 fingerprint at index level).**
The inelastic-markets candidate predicts systematic flow days move prices. India's most
systematic flow is the monthly SIP cycle, which BOOMED from ~FY2015. Registered NOW as
break **BR6 (SIP-era onset, FY2015)** in the breaks registry — source: AMFI SIP-book growth
from ~₹1.2k cr/mo (2014) to >₹20k cr/mo (2025) [press-sourced; pin AMFI numbers at pull].
- Design: ToM window = last trading day of month + first 4 of the next (the Lakonishok-Smidt
  convention, fixed); mean daily return in-window vs out, full sample + era split at BR6
  (2007-2015-03 vs 2015-04-2026). MW one-sided (in-window greater) p per era.
- BARS: (i) ToM premium present full-sample (p < 0.05); (ii) the H61 FINGERPRINT = the
  in-window minus out-of-window daily mean is LARGER post-BR6 than pre (direction only,
  descriptive — n too small for a difference test to bind, stated). PRIOR on record: (i)
  passes (ToM is the most robust calendar regularity known); (ii) the desk EXPECTS the
  fingerprint (SIP flows are ToM-concentrated) — a reversed sign would count against H61's
  index-level relevance and be recorded as such.
- CONSUMPTION CAP: no trade from either print (calendar tilts live under L5's regime and
  CW's cost discipline); T6 feeds H61's motivation and the deployment-timing playbook only.

| # | What | Result | Status |
|---|---|---|---|
| T1b | Overnight mean in/out of stress (2 conditionings) | **Null as barred — the drift is a CALM-DAYS phenomenon** (in-episode overnight +9.2%/yr at t=+0.66, nothing) — but the prior's mechanism was WRONG (recorded): stress does NOT land overnight; it lands INTRADAY (in-episode intraday −66.3%/yr, t=−3.3; out-of-episode intraday only −6%/yr, t=−1.5). India's crisis damage is a local-session event. EXECUTION consumption: in stress the buy-at-close argument vanishes (no drift to capture) and de-risk fires executed at next open sacrifice no measurable drift | **null confirmed; mechanism prior missed; ops guidance ships** |
| T6-TOM | ToM premium + SIP-era fingerprint | Bar (i) **PASS**: full-sample ToM premium +7.2bp/day (p=0.025). Bar (ii) **the fingerprint is ABSENT — booked against H61's index-level relevance as pre-stated**: the premium SHRANK across BR6 (+12.2bp/d pre-2015 → +3.8bp/d, p=0.29 in the SIP era). The naive SIP-amplification story fails at the index calendar; the honest reading is the US-style decay pattern (deeper markets absorb the systematic flow) and/or SIP-date dispersion. H61's core (the aggregate flow multiplier) is untouched — but it can no longer claim this bump as motivation, and the sweep doc's C3 line inherits this print | **premium real, fingerprint absent (recorded against)** |

## Entry EN-D1a (2026-09-03) — PRE-REGISTERED before running: onset-conditioned sectoral
contrast, the runnable partial of EN-D1. Parent design QUOTED VERBATIM
(research/cycles/enso-deep/partCDEFH.md): "**EN-D1** H55's promotion test (sector
conditional returns on REALIZED rainfall deficits + food-CPI spikes, purged, era-split;
bars at registration — runsheet step 73)." Principal directive 2026-09-03: "El Niño onset
marked... we can check sectoral impact on logically impacted sectors for this not all...
+1 or -1 sigma next 1y or 6month." STATED DEVIATION from the parent: conditions on El Niño
ONSET (the real-time-knowable state) rather than realized rainfall deficit — the tradeable
timing; realized-deficit conditioning, food-CPI, purging and era-split all remain the full
EN-D1's, which this partial does NOT run and CANNOT replace. Promotes nothing (H55 stays
Tier-C candidate).

Data: ONI seasonal 1950-2026 (climate vault, CPC-style labels) × N500 SURVIVOR panel
adjclose 2012-2022 (panel vault). ONE-WAY DECLARATION (survivorship stated at admission):
dead rural/smallcap names are absent, inflating the treated basket's measured return, i.e.
biasing AGAINST finding treated underperformance — so a treated-underperforms print is
admissible evidence; a null print is INCONCLUSIVE, never evidence against H55.

Definitions fixed NOW, before any number:
- ONSET: first season labeled `el_nino` in the vaulted ONI file following >=2 consecutive
  non-el_nino seasons, sustained el_nino for >=3 consecutive seasons. Event date = first
  panel trading day after the onset season's last calendar month. All onsets inside the
  panel's usable span run; expected from the record: the 2014-16 event and the 2018-19
  event (the script prints what the rule finds; no hand-picking).
- TREATED basket (rural/monsoon-exposed, equal-weight, declared ex ante, only names present
  in the panel; M&M absent from the panel — recorded): HINDUNILVR, DABUR, EMAMILTD,
  GODREJCP, BRITANNIA, MARICO, ITC, HEROMOTOCO, BAJAJ-AUTO, ESCORTS, UPL, PIIND,
  COROMANDEL, CHAMBLFERT, GNFC, RALLIS, KSCL, JYOTHYLAB, VBL (19).
- PLACEBO basket (export-oriented, monsoon-orthogonal; the "not all sectors" control):
  TCS, INFY, WIPRO, HCLTECH, TECHM, MPHASIS, MINDTREE, SUNPHARMA, DRREDDY, CIPLA, LUPIN,
  AUROPHARMA, DIVISLAB (13).
- MARKET: equal-weight mean of all panel names alive that day.
- OUTCOME (the principal's spec): basket-minus-market cumulative return over the next 126
  and 252 trading days from the event date, z-scored against that basket's own full-sample
  distribution of overlapping rolling 126/252-day market-relative returns.
- BARS (set NOW): (i) TREATED: z <= -1 at either horizon in EVERY onset found -> PASS
  (sectoral transmission real at 1-sigma); z <= -1 in some but not all -> MIXED (recorded,
  no consumption beyond context); no onset with z <= -1 -> NULL (inconclusive under the
  one-way declaration). (ii) PLACEBO CONTROL: |z| < 1 at both horizons in every onset ->
  control CLEAN; any |z| >= 1 -> control CONTAMINATED and the treated print may not be
  read as sectoral (market/global factor owns it — the H53a lesson).
- PRIOR on record: 2015 treated z <= -1 plausible (the 2014+2015 double-deficit rural
  distress is documented); the weak 2018-19 event likely null; PASS-in-every-onset ~25%.
  Placebo clean ~60% (IT carries global beta; 2015-16 had a global RV episode).
- Census: 2 baskets x 2 horizons = 4 run cells.

| # | What | Result | Status |
|---|---|---|---|
| EN-D1a | Onset-conditioned sectoral contrast, survivor panel (interpretation hand-appended AFTER the print) | Rule found 3 in-panel onsets: 2014 SON, 2018 ASO, 2019 OND (the last is the 2018-19 event's label lapse re-triggering — the rule ran as written, no hand-picking). TREATED: NO onset reaches z <= -1 at either horizon (2014: +0.39/-0.38; 2018: -0.27/+0.39; 2019: +1.99/+0.34) -> **NULL**. PLACEBO: CLEAN for 2014 and 2018 (all abs z < 1) but **CONTAMINATED for 2019 OND** (+1.33 6m / +1.34 12m) — those windows are the COVID crash/recovery, which also owns treated's +1.99 (defensive staples in the crash), so the 2019 cells may not be read as sectoral, exactly as the control was designed to catch. PRIOR MISS recorded: the registration called 2015 treated z <= -1 plausible; measured -0.38 at 12m only. Mechanism read: the panel's rural-REVENUE large caps are urban-margin franchises, and the true rural casualties are dead names a survivor panel cannot hold — the bias the one-way declaration anticipated. Under that declaration this NULL is INCONCLUSIVE, not evidence against H55 | **null — inconclusive (one-way); H55 stays Tier-C candidate; full EN-D1 (PIT panel + realized deficits + food-CPI) remains the promotion test; census +4 = 197** |

## Entry GDP-D1 + FISH-D1 (2026-09-05) — PRE-REGISTERED before running: growth vs the
market, and the Fisher equation vs the market. Principal directive: "gdp impact on stock
market or fisher equation vs market backtest it." Both are VERIFICATION designs on the JST
R6 panel (17-18 economies, 1950-2020, postwar span fixed to avoid war/hyperinflation
regimes; stated). Consumption is CONTEXT only: GDP keeps its [CONTEXT] tag in the
sub-parts menu and the Fisher print underwrites the L9 inflation-regime state. No
promotion path; nothing enters the stack.

Definitions fixed NOW: real GDP growth = Δlog real GDP per capita (rgdppc); inflation =
CPI pct change; nominal equity return = eq_tr; real equity = (1+eq_tr)/(1+infl)-1.
Overlapping-window p-values are flagged inflated, never trusted.

**GDP-D1 (3 cells):**
- (i) CROSS-COUNTRY: corr across countries of full-sample (>=50y) real GDP/cap growth vs
  real equity CAGR. PRIOR (Ritter 2005/DMS): ~zero or NEGATIVE. BAR: corr < +0.3 confirms
  "growth is not the cross-country equity driver"; corr >= +0.5 is a recorded miss.
- (ii) WITHIN, CONTEMPORANEOUS: pooled corr(same-year growth, real equity return).
  PRIOR: modest positive (+0.1 to +0.3).
- (iii) WITHIN, LEAD-LAG: pooled corr(growth_t, real equity_{t+1}) vs corr(real equity_t,
  growth_{t+1}). PRIOR: prediction ~0 (|corr| < 0.1); the REVERSE larger (the market is
  the leading indicator, not the lagging consumer). BAR: reverse > forward confirms the
  growth-state [CONTEXT] tag; forward >= +0.15 pooled is a recorded miss AND a reopening
  flag for the growth band.

**FISH-D1 (3 cells):**
- (i) 1Y FISHER SLOPE: pooled OLS slope of NOMINAL equity return on same-year inflation.
  Fisher predicts beta = 1. PRIOR (Fama-Schwert 1977): beta BELOW ZERO at annual horizon.
  BAR: beta significantly < 1 rejects the 1y Fisher hedge; beta >= +0.5 is a recorded miss.
- (ii) 10Y FISHER SLOPE: slope of overlapping 10y nominal equity CAGR on 10y inflation.
  PRIOR: beta rises toward 1 (partial long-horizon hedge restored).
- (iii) REGIME SPLIT (the L9 tie): pooled real equity return in top-quintile inflation
  country-years vs bottom-quintile. PRIOR: strongly negative in the top quintile (the
  1970s mechanism); gap >= 5pp expected.
- Census: 6 run cells (3 + 3).

| # | What | Result | Status |
|---|---|---|---|
| GDP-D1 | Growth vs the market, JST R6 1950-2020 (interpretation hand-appended AFTER the print) | (i) CROSS-COUNTRY corr(mean real GDP/cap growth, real eq CAGR) = **-0.21** (n=16) — BAR PASS, Ritter's paradox reproduced on our own vault: Japan grew fastest (3.6%/yr) with mid-pack equity returns; Switzerland/UK grew slowest with solid returns; Portugal grew 2.7%/yr and equity holders LOST money. (ii) same-year pooled corr **+0.09** (n=1120) — bottom of the prior band; even contemporaneously, annual growth barely co-moves with returns. (iii) forward corr(growth_t, eq_t+1) = **-0.06** (bar: abs < 0.1 PASS); reverse corr(eq_t, growth_t+1) = **+0.31** — the market leads GDP by 5x more than GDP leads the market. Growth stays [CONTEXT]; the reopening flag stays untriggered | **all 3 bars pass — "GDP does not drive equity returns" confirmed at panel breadth** |
| FISH-D1 | Fisher equation vs the market, JST R6 1950-2020 | (i) 1y pooled slope of NOMINAL equity on inflation: beta = **-0.21** (se 0.16, n=1136) vs Fisher's +1 — 7.6 se's below; the Fama-Schwert result reproduced: stocks are NOT a 1-year inflation hedge, the sign is the WRONG WAY. (ii) 10y slope beta = **+0.21** (n=976 overlapping, se flagged) — direction of the prior confirmed (rises with horizon) but "toward 1" was generous: even at 10y the hedge is ~one-fifth restored. PARTIAL PRIOR MISS recorded. (iii) regime split: top-quintile inflation country-years (median 9.9%) real equity **+2.9%/yr** vs bottom-quintile (0.5%) **+14.9%/yr** — 12pp gap, bar (>=5pp) PASS, but PRIOR MISS on sign recorded: high-inflation real equity is LOW, not negative (the truly negative years are the ACCELERATION years inside the arc — the L9 state distinction, now sharpened by this print) | **Fisher rejected at 1y as registered; 12pp regime gap underwrites L9; two honest prior misses booked; census +6 = 203** |

## Entry ER-D1..D4 (2026-09-05) — PRE-REGISTERED before running: the expected-return
horizon battery. Principal directive (verbatim intent): regress GDP growth vs returns
across major markets + India at 1/3/5/10/20y; adjust growth by a hurdle (bond yield x1.25
as the WACC proxy; value-creation only above it); test share dilution vs returns; then club
factors (max 10, simple equation) into the best no-lookahead prediction of 1/5/10/20y
returns, outliers excluded; verify (not assume) the hypothesis "valuation/quality matter at
5-10y, 1-3y is ~random."

Data: JST R6 (17-18 economies, 1870-2020; postwar 1950-2020 primary, full-sample
secondary where stated); India partial from NIFTY vault + PWT (short — stated). STATED
LIMITS: aggregate ROE and CAPE are NOT in any vault — ROE is proxied by DELIVERED real
dividend growth (D_t reconstructed as cumprod(1+eq_capgain) x eq_dp), CAPE by the
dividend yield eq_dp (both are valuation/payout-anchored; Shiller ie_data + Damodaran
ROE/issuance added to the RUNSHEET). Outlier rule fixed NOW: correlograms use SPEARMAN
(rank, outlier-robust); OLS legs winsorize all variables at 1%/99%. Overlapping-window
p-values are flagged, never trusted. All p-values descriptive.

**ER-D1 — horizon correlogram (25 cells + 4 India):** pooled Spearman of predictor at t vs
cumulative REAL equity return over next 1/3/5/10/20y. Predictors (5): dividend yield
(eq_dp); trailing-5y real GDP/cap growth; trailing-5y real dividend growth; real long rate;
trailing-5y real return. India (4 cells): trailing-3y return and PWT growth vs next 1/3y
NIFTY real return (short sample, descriptive strength only).
PRIORS: dp is the ONLY predictor reaching |rho| >= 0.3 at 10y/20y and rises monotonically
with horizon; ALL predictors |rho| < 0.15 at 1y (the "random at 1-3y" hypothesis); growth
predictors below dp at every horizon >= 5y (GDP-D1's lesson extends).
**ER-D2 — dilution/slippage (2 cells):** per-country full-sample gap = mean real GDP/cap
growth MINUS mean real dividend growth (the Bernstein-Arnott 2003 "two-percent dilution"
construction on our vault); (i) the panel median gap (prior: positive, 1-3pp/yr); (ii)
cross-country corr(gap, real equity CAGR) (prior: NEGATIVE — slippage eats returns).
**ER-D3 — the hurdle interaction (2 cells):** value-creation proxy = trailing-5y real
dividend growth minus the real hurdle (ltrate x1.25 minus inflation). Next-5y real return,
top vs bottom tercile of the proxy, pooled. PRIOR: top beats bottom by >= 2pp/yr —
delivered growth above the financing hurdle is good growth; the principal's rule
directionally confirmed. STATED DEVIATION: true ROE unavailable; this is the runnable form.
**ER-D4 — the clubbed equation (6 cells):** pooled OLS, real next-h return on 5 factors
[dp, trail growth, real long rate, inflation, trail return], winsorized: (i) full-sample
R2 at 5y and 10y with coefficients (the "simple equation"); (ii) full-sample R2 at 1y and
3y (randomness check); (iii) NO-LOOKAHEAD OOS: fit on starts <= 1989 only, predict starts
1990-2010(5y)/2000(10y), OOS R2 vs the historical-mean benchmark (Goyal-Welch test).
PRIORS: in-sample R2 ~ <5% (1y), 5-12% (3y), 10-25% (5y), 20-40% (10y); OOS R2 POSITIVE
but at most half of in-sample — if OOS <= 0 the Goyal-Welch critique wins and the
consumption is "valuation states, never point forecasts."
CONSUMPTION: context/verification for the L4/L9 seats and the policy-horizon valuation
state; no promotion, no signal enters the stack from this entry. Census: 25+4+2+2+6 = 39.

| # | What | Result | Status |
|---|---|---|---|
| ER-D1 | Horizon correlogram, 5 predictors x 1/3/5/10/20y, pooled Spearman (n~950-1100/cell; interpretation hand-appended AFTER the print) | Dividend yield rises MONOTONICALLY +0.15/+0.21/+0.24/+0.29/+0.38 (prior confirmed; AUDIT NOTE 2026-09-05: under the persistent-regressor null [Stambaugh 1999; Boudoukh-Richardson-Whitelaw 2008] a rising ladder is null-consistent — 'confirmed' demoted to 'shape observed, significance vs the null untested pending ER-D1c'; per-country dp->10y: USA +0.63, UK +0.70, Japan +0.76, Germany +0.01 the outlier). Trailing GDP growth is NEGATIVE at every horizon, monotone to **-0.36 at 20y** — high trailing growth predicts LOWER returns. Trailing dividend growth negative (-0.10 at 10y); real long rate weakly positive (+0.13..+0.20); trailing return negative (LT reversal). PRIOR MISS (partial): 1y is not fully random — g5 -0.17 and dp/rlt +0.15 breach the <0.15 bar by a hair; tiny but nonzero. India (short, descriptive): nothing at 1y, +0.24 at 3y on n=14 — noise-level, consistent with short-horizon randomness | **valuation-rises-with-horizon confirmed; growth-negative confirmed and extended; 1y near-random (bar missed by 0.02)** |
| ER-D2 | Slippage (mean GDP/cap growth - mean delivered real dividend growth), full postwar, per country | Panel median gap **+0.7pp/yr** (9/16 positive; prior band 1-3pp partially missed — median lower). THE HEADLINE: cross-country Spearman corr(gap, real equity CAGR) = **-0.79** (n=16) — the slippage wedge, not growth itself, is what prices: Portugal (gap 17.8pp) grew 2.7%/yr and equity holders LOST money; Italy 3.2/France 2.5 weak returns; Germany/Switzerland/Sweden negative gaps and strong returns (Germany's -7.9 flagged as a probable series artifact; Spearman robust to it). RUN NOTE: first print returned nan from a non-finite dividend-growth cell; a finite-value guard was added and the design re-run once — a repair of a broken cell, no bar moved | **Bernstein-Arnott dilution mechanism CONFIRMED at panel breadth — this resolves GDP-D1's paradox** |
| ER-D3 | Hurdle interaction: next-5y return, top vs bottom tercile of (delivered 5y div growth - real 1.25x-bond-yield hurdle), pooled | **PRIOR MISS — INVERTED**: top tercile +4.6%/yr vs bottom +8.4%/yr. At INDEX level the principal's rule runs backwards in time: periods of delivered growth above the hurdle are late-cycle and priced; the best forward returns follow periods of DELIVERED-growth famine (which are high-dp, cheap periods). The rule's natural home is the cross-section (profitability/quality factor at stock level, with true ROE) — runsheet row stands. Booked as measured | **miss recorded — timing-inverted; cross-sectional form data-gated** |
| ER-D4 | The clubbed equation: pooled winsorized OLS on [dp, g5, real long rate, inflation, trail return] | In-sample R2: 1y **9.3%** (prior <5% MISSED — mildly less random than hypothesized), 3y 14.9%, 5y **18.0%**, 10y **26.7%** (both in prior bands). THE EQUATION (10y): r ≈ **+1.17·dp − 0.90·g5 + 0.78·rlt + 0.49·infl − 0.03·r5** — valuation in with ~Gordon weight, trailing growth NEGATIVE. NO-LOOKAHEAD OOS (fit ≤1989, test 1990+): 5y **−7.4%** (WORSE than the historical mean — Goyal-Welch wins at 5y), 10y **+7.0%** (survives, but a fraction of in-sample). Registered consumption rule triggers: valuation is a STATE for expectations-setting, never a point forecast | **horizon structure verified; OOS discipline binds; census +39 = 242** — AUDIT NOTE 2026-09-05: the OOS cells carry confirmed defects (full-sample winsorization before the split; no label-window purge; executed test windows exceed the registered ones; frozen pooled benchmark mislabeled Goyal-Welch). The 5y 'GW wins' verdict stands a fortiori (all leaks pro-model); the 10y '+7.0% survives' read is SUSPENDED pending ER-D4b. See the audit addendum. **CORRECTION BOX (2026-09-05, per ER-D4b's registered bar): the restore test FAILED (purged 10y OOS R2 -15.7% vs the honest benchmark, band includes 0) — GOYAL-WELCH WINS AT BOTH HORIZONS; the '+7.0% survives' read is WITHDRAWN (print preserved above as the record of the defective run)** |

## Entry ER-D5 (2026-09-05) — PRE-REGISTERED before running: the SAME-PERIOD question.
Principal directive: "what if we look same period metrics to check if stock median/index
return explained by it." The contemporaneous complement to ER-D1..D4: not prediction —
attribution. Same JST R6 panel, 1950-2020, same outlier rule (Spearman; winsorized OLS),
windows of h = 1/3/5/10/20y measured over the SAME span (t+1..t+h) as the return.

**Cells (25):**
- (a) CORRELOGRAM (15): pooled Spearman of same-window real return CAGR vs same-window
  (i) real GDP/cap growth, (ii) real dividend growth, (iii) inflation — at the 5 horizons.
  PRIORS: same-window GDP growth stays WEAK at every horizon (< +0.3 even at 20y — the
  slippage wedge, not measurement, is why); same-window DIVIDEND growth rises strongly
  with horizon (>= +0.5 at 20y — delivered cash flows own long returns); inflation
  negative at short horizons (FISH-D1), fading by 20y.
- (b) DECOMPOSITION SHARES (5): log-return identity y ~ delivered real dividend growth +
  revaluation (-Δlog dp / h) + income (mean log(1+dp)); covariance shares
  s_i = cov(c_i, y)/var(y) at each horizon. PRIOR (Bogle/DMS): revaluation owns >= 70% of
  return variance at 1y, declining monotonically, < 50% by 10y, < 40% at 20y; delivered
  growth + income own the 20y window.
- (c) MACRO-ONLY R2 (5): winsorized pooled OLS of same-window return on [same-window GDP
  growth, inflation] ONLY (no market-derived variables — the "if you had perfect macro
  foresight" test) at the 5 horizons. PRIOR: R2 < 10% at 1y; < 25% even at 20y — perfect
  macro foresight would NOT have told you the market's return.
CONSUMPTION: context/verification (the strongest form of the GDP-D1 lesson: even knowing
the future macro, the short-run return is the multiple's, not the economy's). No
promotion. Census: 25.

| # | What | Result | Status |
|---|---|---|---|
| ER-D5 | Same-period attribution (interpretation hand-appended AFTER the print) | (a) same-window GDP growth vs same-window return: +0.08/+0.17/+0.11/**0.00**/**-0.20** at 1/3/5/10/20y — bar (<+0.3 everywhere) PASS and sharper than the prior: at 20y the SAME-period relation turns negative (long high-growth eras dilute more — ER-D2's wedge compounding). Same-window DELIVERED dividend growth: +0.39/+0.50/+0.54/+0.55/**+0.61** — prior (>=+0.5 at 20y) PASS: delivered cash flows own long returns. Inflation: -0.25..-0.15..**-0.24** — PARTIAL MISS: it does NOT fade by 20y (consistent with FISH-D1's one-fifth-restored hedge). (b) variance shares: revaluation 55/54/46/40/**40%**, delivered growth 45/47/54/61/**62%**, income ~0% of VARIANCE (it sets the LEVEL, not the variation). PRIOR MISS at 1y: revaluation 55%, not >=70% — on ANNUAL country-year data delivered dividends are volatile enough to carry 45% even short-run; the 10y (<50% ✓) and 20y (=40%, at the boundary) cells land as registered. (c) MACRO-ONLY R2 with same-window GDP growth + inflation: 8.4/14.7/14.3/13.4/**18.8%** — bars (<10% at 1y, <25% at 20y) PASS: perfect macro foresight would explain less than a fifth of the market's return at every horizon | **all three sub-designs land; three honest partial misses booked; census +25 = 267** |

## Entry ER-D6 (2026-09-05) — PRE-REGISTERED before running: US + India country models,
all vaulted metrics, linear vs nonlinear. Principal directive: "just check us and india
and all major metrics and combination linear nonlinear regression."

US (JST R6 annual, 1950-2020; the deep sample): factors = dp, trailing-5y GDP/cap growth,
trailing-5y real dividend growth, real long rate, inflation, trailing-5y return, TERM
SPREAD (ltrate - stir), 5y Δ(tloans/gdp) — 8 factors, the vault's full major-metric set.
Outcomes: next-5y and next-10y real return CAGR. Winsorize 1%/99%.
India (annual, 1994-2025; IIMA market = MF+RF, excess outcome = MF; SHORT — stated):
factors = trailing-3y and trailing-1y excess return, RF level, trailing-12m realized vol
(NIFTY daily, so vol usable 2008+), PWT real GDP/cap growth (to 2019). Outcomes: next-1y
and next-3y excess CAGR. India OOS split 2015+ is n~8: DESCRIPTIVE only, no bar.

MODELS (fixed now): (L) linear OLS; (Q) quadratic — linear + squared terms of dp and
inflation only (US) / trail3y and vol (India); (B) the house nonlinear: 3x3 RANK-BIN grid
(dp tercile x inflation tercile for US at 5y) conditional means — grids/ranks per
CONTRACT, no fitted trees/nets (no sklearn dependency; under 10 regime transitions the
contract forbids fitted switching anyway).
CELLS (14): US in-sample R2 for L and Q at 5y and 10y (4); US OOS (fit<=1989, test 1990+)
for L and Q at 5y and 10y (4); US bin-grid spread read (1); US factor-ranking read by
|t| at 10y (1); India in-sample L at 1y and 3y (2); India OOS descriptive (1); India
factor-ranking read (1).
BARS/PRIORS: (i) US: quadratic beats linear IN-SAMPLE by construction but does NOT beat
it OOS at either horizon (the overfit prior; if Q wins OOS at both horizons that is a
recorded miss and a genuine nonlinearity flag). (ii) US bin grid: cheap+low-inflation
corner beats expensive+high-inflation corner by >= 6pp/yr at 5y, monotone-ish across the
diagonal. (iii) US 10y factor ranking: dp first (largest |t|). (iv) India: in-sample 1y
R2 < 15% and NOTHING stable OOS (prior: India's sample cannot certify a return model —
the honest expected print). CONSUMPTION: context; the L4 valuation state and L9 regime
state are the only standing consumers. No promotion. Census: 14.

| # | What | Result | Status |
|---|---|---|---|
| ER-D6 | US + India, all vaulted metrics, linear vs nonlinear (interpretation hand-appended AFTER the print) | US 8-factor: in-sample R2 **65.8%** (5y) / **54.2%** (10y) — and OOS **-389% / -591%**: catastrophically worse than the historical mean; quadratic worse still (-445% / -949%) — bar (i) PASS, nonlinearity adds in-sample fit and subtracts OOS. THE CONTRAST THAT MATTERS: ER-D4's pooled-panel 5-factor scored -7.4%/+7.0% OOS on the same horizons — pooling 17 countries is the regularizer; a single-country kitchen sink with n=66 overlapping obs is pure memorization. 10y factor ranking: **dp +4.6** first (bar iii PASS), then g5 -2.4 (growth negative AGAIN), term +2.2, dg5 +2.2; credit gap last. The house nonlinear — the 3x3 dp x inflation RANK-BIN grid — is the only structure that survives inspection: cheap+low-infl **+14.2%/yr** -> expensive **+2.3%/yr**, ~12pp spread (bar ii >=6pp PASS), monotone down the diagonal; the expensive+high-inflation corner is EMPTY in US history (n<4) — that combination barely occurs. India: the registered 5-factor set on its n=13 intersection prints a fake 57.5% R2 (the overfit demo, as predicted); the honest reduced model R2 9-14% with NOTHING above t 1.7 (growth again NEGATIVE, -1.7); OOS -93.5% — bar (iv) PASS: India's sample cannot certify a return model | **all 4 registered priors confirmed; the grid (states/ranks) is the only nonlinearity that earns anything; census +14 = 281** — AUDIT NOTE 2026-09-05: the US OOS cells share ER-D4's split/winsorization defects (verdicts stand a fortiori, pro-model leaks); the 12pp grid spread is IN-SAMPLE (full-sample tercile breaks, no OOS cell) — real-time validation registered as ER-D7. See the audit addendum |

## Audit addendum (2026-09-05) — ER battery, adversarial multi-agent code review
A 14-agent workflow (4 audit lenses -> refute-by-default verification -> synthesis;
8/9 findings survived) reviewed every ER-battery script against the ledger and CONTRACT.
Booked facts (prints NEVER edited; bars NEVER moved; annotations are dated):
1. **Winsorization lookahead** (analyze_er_horizon.py:117-126/138-139; analyze_er_d6_usindia.py):
   1%/99% clip bounds computed on the FULL sample including test years, applied BEFORE the
   OOS split — the "NO-LOOKAHEAD" label was not earned as coded.
2. **No label-window purge**: h-year train labels for starts 1980-1989 realize INSIDE the
   test era — the exact case quant/stats/cv.py and CONTRACT §9:144 (purged/embargoed CV)
   exist for. Pro-model bias; all NEGATIVE verdicts stand a fortiori.
3. **Unregistered test windows**: executed starts 1990-2015(5y)/1990-2010(10y) vs the
   registered 1990-2010(5y)/1990-2000(10y) — an unstated deviation (the 10y test set ~2x
   the registered one), against house precedent (ER-D2/D3 stated theirs).
4. **Benchmark mislabel**: the OOS benchmark is a FROZEN POOLED grand mean; Goyal-Welch
   uses the expanding mean, and pooling credits the model for cross-country level capture
   that ER-D2 showed is large (-0.79). "(Goyal-Welch test)" is therefore a mislabel.
5. **Stambaugh departure**: CONTRACT §9:142 ("Correct Stambaugh bias on persistent
   predictors") applied nowhere in the battery and never stated as a deviation; the
   monotone dp ladder is null-consistent under BRW-2008/Valkanov-2003. ER-D4's +1.17 dp
   coefficient and ER-D6's dp |t|=4.6 are uncorrected magnitudes (sign/ranking use only).
6. **Pooling conflates within/between**: the "growth-negative" reads mix within-country
   timing with the between-country ER-D2 wedge; the within-country timing claim is
   genuinely unmeasured (registered two-sided in ER-D1b). Pooled dp is the CONSERVATIVE
   direction (per-country majors +0.63/+0.70/+0.76 vs pooled +0.29).
CONSEQUENCE: every negative/null verdict of the battery is robust (all defects flatter the
model). The sole positive OOS cell — ER-D4 10y "+7.0% survives" — is SUSPENDED pending
ER-D4b. Follow-ups registered below: ER-D7 (honest grid), ER-D4b (purged correction rerun),
ER-D1b (within/between), ER-D1c (persistent-regressor null band).
**PROCESS NOTE #8 (standing, from this addendum):** any registration using the words
"no-lookahead" or "OOS" must state, AT REGISTRATION: the purge rule (per quant/stats/cv.py),
the preprocessing information set (winsorization/rank/demean bounds fitted on TRAIN only —
machinery: quant/stats/preprocess.py), the exact test-start window, and the benchmark
definition (expanding vs frozen; pooled vs per-country). Campbell-Thompson omission noted
as anti-model (mention-only, no fix owed).

## Entry ER-D7 (2026-09-05) — PRE-REGISTERED before running: the HONEST GRID — expanding
within-country rank bins with pooled purged cell means. Audit follow-up to ER-D6.
Motivation: the 3x3 dp x inflation grid is the only ER structure with standing consumers
(the L4 valuation state, the L9 regime state), and its printed ~12pp corner spread is
IN-SAMPLE — full-sample tercile breaks (analyze_er_d6_usindia.py:81-84), all-years cell
means, no OOS cell among ER-D6's 14. This design gives the consumed structure the
house-standard real-time test, or retires it.
Data: JST R6, 1950-2020, all countries with complete dp/cpi/eq_tr (~16 countries, ~1,100
pooled country-years). Variable construction IDENTICAL to ER-D1..D6: infl = per-country cpi
pct-change; req = (1+eq_tr)/(1+infl)-1; dp = eq_dp; fwd_h = expm1(mean log1p(req) over
t+1..t+h) at start year t; h = 5, 10.
DEFINITIONS FIXED NOW (all real-time; purge per quant/stats/cv.py; process note #8 fields):
- STATE at (country,t): tercile bucket (cuts 1/3, 2/3) of the WITHIN-COUNTRY EXPANDING
  percentile of dp and of infl, computed on that country's own data 1950..t only, >=20y
  warmup (first usable state year 1970). No full-sample ranks anywhere.
- FORECAST at (country,t) for fwd_h: pooled mean of fwd_h over past observations (all
  countries, starts s <= t-h — COMPLETED windows only) in the same 3x3 cell; cell n<4
  completed obs falls back to the expanding pooled mean of all completed fwd_h.
- BENCHMARK: the expanding pooled mean of all completed fwd_h at the same t (identical
  information set to the model). NO winsorization in the recursive legs (no fitted
  parameters — no preprocessing lookahead); no slopes anywhere (no Stambaugh exposure).
- Recursive over forecast starts 1970-2010 (5y) and 1970-2000 (10y). Overlapping windows:
  no p-values printed; bars on magnitudes only.
CELLS (6): (i) OOS R2 vs the expanding pooled mean, 5y and 10y (2). (ii) REAL-TIME CORNER
SPREAD at 5y: realized mean fwd5 of country-years classified in real time cheap (dp
tercile 3) + low-infl (tercile 1) MINUS expensive (dp tercile 1) + high-infl (tercile 3);
corner n's printed; a corner with pooled n<20 is booked descriptive (1). (iii) ERA SPLIT of
(ii): starts 1970-1989 vs 1990-2010 (1). (iv) ER-D1's dp->10y Spearman re-run with dp in
within-country expanding-percentile form — pooled, and Germany alone (2).
BARS (fixed now): B1 real-time corner spread >= 4pp/yr at 5y (decay from 12pp EXPECTED;
<2pp triggers a RECORDED DOWNGRADE of the grid state's expectations consumption with dated
notes on ER-D6 and the L4/L9 seats; 2-4pp = miss booked, consumption qualified but
retained). B2: OOS R2 > 0 at 10y. B3: Germany dp->10y recovers from +0.01 (raw level) to
>= +0.2 in expanding-rank form (informative because expanding ranks are NOT a monotone
transform of the full series — the Lettau-Van Nieuwerburgh 2008 mean-shift mechanism).
PRIORS: corner spread ~5-7pp/yr; 10y OOS R2 +2..+10%; 5y OOS R2 near zero, sign TWO-SIDED;
era split positive both eras, smaller post-1990. WHY IT CAN SURVIVE WHERE OLS FAILED
(argued before the print): 9 conditional means on ~1,100 country-years, no slopes;
expanding within-country ranks are invariant to steady-state dp mean shifts (LVN 2008;
Germany is the vault's own smoking gun); pooling is the regularizer ER-D6 printed.
CONSUMPTION: validates or honestly retires the structure the L4/L9 seats consume; NO
promotion in any outcome. Script: scripts/analyze_er_d7_honestgrid.py. Census: 6.

## Entry ER-D4b (2026-09-05) — PRE-REGISTERED before running: the purged, honest-benchmark
correction rerun. Parent design QUOTED VERBATIM (ER-D1..D4 entry): "NO-LOOKAHEAD OOS: fit
on starts <= 1989 only, predict starts 1990-2010(5y)/2000(10y), OOS R2 vs the
historical-mean benchmark (Goyal-Welch test)." This correction design fixes, AT
REGISTRATION (audit items 1-4): (i) PURGED split — train starts <= 1990-h (no train label
realizes inside the test era, per quant/stats/cv.py); (ii) winsorization bounds fitted on
TRAIN ONLY (quant/stats/preprocess.py), applied unchanged to test; (iii) the REGISTERED
test windows verbatim — starts 1990-2010 (5y), 1990-2000 (10y); (iv) TWO benchmarks — (a)
the expanding PER-COUNTRY historical mean (the honest Goyal-Welch analogue for a panel),
(b) the parent's frozen pooled mean (continuity print only). Same 5 factors, same pooled
panel. Plus the ER-D6 US cells rerun purged with train-only bounds vs the expanding US
mean. CELLS (6): pooled 5y/10y vs benchmark (a) [2]; pooled 5y/10y vs benchmark (b) [2];
US 5y/10y vs expanding US mean [2]. BAR (fixed now): the ER-D4 10y "survives" read is
RESTORED only if pooled 10y OOS R2 > 0 vs benchmark (a) AND a calendar-year block-bootstrap
90% band (quant/stats/bootstrap.py, B>=300) on that R2 excludes 0; otherwise the ER-D4 row
gets a dated correction box reading "Goyal-Welch wins at BOTH horizons." PRIOR on record:
the 10y cell flips to <= 0 or its band includes 0 (60%); the 5y cell stays negative (85%).
Parent prints and bars UNTOUCHED. Script: scripts/analyze_er_d4b.py. Census: 6.

## Entry ER-D1b (2026-09-05) — PRE-REGISTERED before running: within vs between attribution
of the pooled ER reads. Audit item 6. All variables as in ER-D1/ER-D5/FISH-D1. For
PREDICTIVE legs, within-country form = the regressor's OWN-COUNTRY EXPANDING percentile
(recursive, >=20y warmup — full-sample demeaning is FORBIDDEN here, it induces the
Nickell/Stambaugh-type bias [Hjalmarsson 2010]); for ATTRIBUTION (same-window) legs,
within-country demeaning is permitted. CELLS (9): (1-2) dp -> next-10y/20y pooled Spearman,
expanding-rank form; (3-4) trailing-5y growth -> next-10y/20y pooled Spearman,
expanding-rank form — the within-country timing read, registered TWO-SIDED (sign genuinely
uncertain); (5) per-country MEDIAN of own-country corr(g5, fwd10) (levels, descriptive
robustness); (6-7) BETWEEN components printed separately: cross-country corr of full-sample
mean g5 vs mean return, and mean dp vs mean return; (8) ER-D5's 20y same-window growth cell
recomputed on within-country demeaned variables; (9) FISH-D1(iii) regime split recomputed
with inflation in own-country expanding-percentile form (top vs bottom quintile).
BARS/PRIORS: dp within-rank >= pooled level form at 10y (prior: strengthens, per-country
majors say so); growth within-form: TWO-SIDED, prior 55% it stays negative but attenuates
by >= a third (the wedge is between-country); FISH within-gap >= 5pp keeps L9's underwrite
— < 5pp is a recorded miss AND a dated L9 annotation. Script: scripts/analyze_er_d1b.py.
Census: 9.

## Entry ER-D1c (2026-09-05) — PRE-REGISTERED before running: the persistent-regressor
null band for the dp ladder. Audit item 5; restores the CONTRACT §9:142 standard the
battery departed from. DESIGN: per country, fit AR(1) to dp (phi, innovations e_t) and
estimate corr(e_t, return innovation u_t). NULL: returns have NO predictability — real
return_t = own-country mean + u_t. Resample the JOINT innovation vectors (e_t, u_t across
countries) by CALENDAR-YEAR blocks with the house stationary block bootstrap
(quant/stats/bootstrap.py; expected block length 5y; B=300; seeded rng(7)); rebuild dp by
AR(1) recursion from each country's actual 1950 level; recompute the pooled Spearman
dp->fwd_h ladder each replication. CELLS (6): observed ladder vs the simulated 95% band at
h = 1, 3, 5, 10, 20 (5 cells: INSIDE = null-consistent, demotion stands; OUTSIDE =
"confirmed vs the null" restored at that horizon); (6) Amihud-Hurvich (2004)
bias-corrected 1y US dp slope vs the raw OLS slope (one print). BARS: none beyond the
band rule itself (a verification design). PRIOR on record: h=1,3 INSIDE the band; h=10,20
borderline — genuine uncertainty; the AH-corrected US slope shrinks toward zero but stays
positive. Script: scripts/analyze_er_d1c.py. Census: 6.

| # | What | Result | Status |
|---|---|---|---|
| ER-D7 | The honest grid (real-time ranks, purged cell means; interpretation hand-appended AFTER the print) | Panel 15 countries / 1,065 country-years. (i) recursive OOS R2 vs the expanding pooled mean: 5y **-29.8%** (n=606), 10y **-27.2%** (n=456) — **B2 FAIL**: the grid's cell means have NO point-forecast value in real time. (ii) real-time corner spread at 5y: cheap+lowinfl +3.3%/yr (n=27) vs expensive+highinfl -1.8%/yr (n=52) = **+5.1pp/yr — B1 PASS** (bar >=4pp; prior 5-7pp confirmed; the in-sample 12pp roughly halves, as predicted). (iii) era split UNSTABLE by construction: the corners barely coexist within an era (1970-89: cheap n=4; 1990-2010: expensive+highinfl n=3, spread -15.2pp on that n) — the pooled spread is substantially cross-era composition; booked as measured, read with corner-n eyes. (iv) dp->10y in expanding-rank form: pooled +0.24 (vs +0.29 levels — no gain); Germany +0.01 -> **+0.12 — B3 MISS** (bar >=+0.2; direction right, magnitude short) | **B1 pass / B2 fail / B3 miss. The grid state survives ONLY as an expectations qualifier (cheap+calm > expensive+hot by ~5pp), never as a forecaster — L4/L9 consumption retained at reduced strength, no downgrade trigger (<2pp) hit** |
| ER-D4b | Purged, honest-benchmark correction rerun (registered windows verbatim) | Pooled, purged, train-only bounds: 5y (train<=1985, test 1990-2010, n=321) OOS R2 **+8.5%** vs expanding per-country mean / **-0.3%** vs frozen pooled; 10y (train<=1980, test 1990-2000, n=165) **-15.7%** vs per-country / -44.3% vs frozen; 10y block-bootstrap 90% band on R2 vs (a): **[-56.6%, +23.8%] — includes 0**. US kitchen-sink cells: 5y -73.4%, 10y +15.3% on n=11 (uninformative). **BAR VERDICT: the 10y restore test FAILS on both conditions** -> the registered correction box fires (see ER-D4 row). PRIOR MISS booked: the 5y cell was registered 85% stays-negative and printed +8.5% vs benchmark (a) — the two-benchmark design exposes why: early per-country expanding means average FEW completed windows (a noisy, easier benchmark), while vs the frozen pooled mean the same model prints -0.3%. Honest read: 5y forecast skill indistinguishable from zero, benchmark-dependent in sign | **correction box fired; 5y prior miss booked; census** |
| ER-D1b | Within vs between attribution | THE TIMING QUESTION RESOLVES: growth-negative is **WITHIN-country** — own-country expanding-rank g5 -> 10y/20y rho **-0.20/-0.23**; per-country median corr(g5, fwd10) = **-0.41** (16 countries); ER-D5's same-20y cell within-demeaned **-0.28** (stronger than pooled -0.20). The two-sided registration lands NEGATIVE: within a single country's own history, high trailing growth is a bad time to buy — no longer attributable to the between-country wedge alone (between printed separately: mean-g5 vs mean-ret -0.36; mean-dp vs mean-ret +0.16). dp bar PARTIAL MISS: within-rank dp -> 10y +0.23 < pooled-level +0.29 (bar said strengthens); at 20y +0.47 > +0.38 it does. FISH-D1(iii) within-form: top own-country inflation quintile real return **-4.1%/yr** vs bottom **+14.2%/yr** -> **WITHIN gap 18.2pp** (pooled was 12.0pp, and the earlier sign-miss REVERSES within-country: high-inflation years are outright NEGATIVE against a country's own history — the pooled +2.9% was chronic-inflation-country dilution). Bar >=5pp: **PASS — L9's underwrite is STRONGER within-country** | **growth-negative upgraded to a within-country timing fact; L9 reinforced at 18.2pp; one dp partial miss booked** |
| ER-D1c | Persistent-regressor null band (Stambaugh/BRW restored per CONTRACT §9:142) | 15 countries, median AR(1) phi 0.71, B=300 joint year-block null. Observed dp ladder vs 95% null band: 1y +0.14 [+0.02,+0.18] INSIDE; 3y +0.20 [-0.02,+0.25] INSIDE; 5y +0.23 [-0.07,+0.27] INSIDE; 10y +0.27 [-0.14,+0.30] INSIDE; **20y +0.36 [-0.19,+0.32] OUTSIDE — the only horizon that beats the null**. The ER-D1 demotion is now QUANTIFIED: the rising staircase through 10y is exactly what persistence + overlap manufactures under NO predictability (BRW 2008 vindicated on our own vault); only the 20-year relation is evidence against the null. AH-corrected US 1y dp slope: +2.97 -> **+1.63** (shrinks 45%, stays positive — prior confirmed) | **ladder demotion quantified: dp is a 20y (and expectations-band) instrument, nothing shorter; census +27 total = 308** |

## Entry ER-D8 (2026-09-05) — PRE-REGISTERED before running: the market as the economy's
forecaster. Principal directive: "predicting next 5y/1y gdp growth using current 5y 10y
stock return" (the reverse arrow of GDP-D1(iii), which printed corr(eq_t, growth_t+1) =
+0.31 vs -0.06 for the forward direction — quoted as the parent print). Literature anchor:
Fama (1981, 1990) — US stock returns lead production growth by ~1 year. JST R6, 1950-2020,
same variable construction as the ER battery. No OOS/no-lookahead claims (correlational
verification; overlap flagged; no p-value bars). Trailing returns are NOT dp-persistent so
Stambaugh exposure is low — stated, not corrected.
CELLS (14):
- (a) POOLED 3x3 Spearman grid: trailing {1y, 5y, 10y} real equity return (through t) x
  next {1y, 5y, 10y} real GDP/cap growth (t+1..t+h). 9 cells.
- (b) WITHIN-COUNTRY diagonal: own-country expanding-percentile (min_obs=20) of the
  trailing return, for trail1->next1, trail5->next5, trail10->next10. 3 cells.
- (c) INDIA descriptive (short, no bar): NIFTY trailing-3y annual return vs PWT growth
  next 1y and next 3y. 2 cells.
BARS/PRIORS (verification): (i) trail1->next1 pooled >= +0.2 confirms market-leads-GDP at
panel breadth (parent print +0.31); (ii) for EACH trailing horizon, predictive rho DECAYS
as the forward horizon lengthens — the market is a 1-2 year business-cycle thermometer,
not a decade forecaster; trail-any -> next-10y expected ~0 (|rho| < 0.15); (iii) within-
country diagonal cells within 0.1 of their pooled counterparts (the lead is cyclical, not
composition). Misses recorded as always. CONSUMPTION: context — sharpens the L3/L18
business-cycle seat's "the market is the leading indicator" doctrine; no promotion.
Script: scripts/analyze_er_d8.py. Census: 14.

| # | What | Result | Status |
|---|---|---|---|
| ER-D8 | Market -> future GDP growth, 3x3 grid + within-country + India (interpretation hand-appended AFTER the print) | Pooled grid (trailing return -> next growth): trail-1y: **+0.29 / +0.05 / +0.02** at next-1/5/10y; trail-5y: +0.18/+0.08/+0.06; trail-10y: +0.13/+0.06/-0.01. ALL THREE BARS PASS: (i) trail1->next1 +0.29 >= +0.2 (parent GDP-D1(iii) +0.31 corroborated at grid breadth); (ii) monotone DECAY across forward horizons in every row, all next-10y cells ~0 — the market is a 1-2 year business-cycle thermometer, not a decade forecaster; (iii) within-country diagonals +0.31/+0.08/+0.02 — within 0.03 of pooled: the lead is CYCLICAL anticipation, not country composition. Bonus read (in-grid): fresh returns beat stale ones as growth predictors (trail-1y +0.29 > trail-5y +0.18 > trail-10y +0.13 at next-1y) — the news is in the recent move. India descriptive: noise on n<=9, as registered. Fama (1981, 1990) reproduced at 15-country/70-year breadth | **all 3 bars pass — the L3/L18 doctrine sharpened: the market leads the economy by ~1 year and no further; census +14 = 322** |

## Entry GDP-D3 (2026-09-07) — PRE-REGISTERED before running: the growth-FLOOR test.
Principal challenge (verbatim intent): "i do not think a long term no growth gdp can give
good median stock high return; index are mostly largecap biased." The prior GDP prints
measure VARIATION among growing economies (full-sample means 1.5-3.6%/yr — no long-term
zero-growth country exists in the panel, stated as a support limit); this design tests the
LEVEL floor inside the observed support: do near-zero-growth DECADES deliver bad returns?
JST R6, country-decades 1950s-2010s, decade real GDP/cap growth (mean of annual Δlog
rgdpmad) and decade real equity CAGR, as in the realrate-decades note conventions.
CELLS (3): (i) median real equity return by growth bucket: <1%/yr, 1-3%, >3% (pooled
country-decades, n per bucket printed); (ii) the same split EXCLUDING high-inflation
decades (decade mean inflation >= 5%) — isolates the growth floor from the inflation
confounder (the L9 state owns those losses per FISH/ER-D1b); (iii) named-case prints
(descriptive): Japan 1990-2020 (the longest near-zero-growth stretch in the panel) and
Switzerland full-sample (the low-growth/high-return counterexample) — decade growth and
equity return per case.
BARS/PRIORS (two-sided; verification): if the <1% bucket's median return is within 2pp of
the 1-3% bucket (especially ex-high-inflation), the growth FLOOR is unsupported in-sample
and the large-cap/global-revenue mechanism stands; if the <1% bucket is lower by >= 3pp in
BOTH cells, the principal's floor intuition is CONFIRMED within support and the ER-arc
reads get a dated qualifier. PRIOR on record: the raw <1% bucket looks bad (war/stagflation
decades) but MOST of the gap vanishes ex-high-inflation (60%); Japan 1990-2020 prints poor
(valuation unwind confounder, stated); Switzerland prints low-growth/high-return.
MEDIAN-STOCK caveat registered: all panel indices are cap-weighted large-cap composites;
the median-stock version of the floor question is DATA-GATED (needs micro panels beyond
the survivor N500) and is NOT answered by this design. Census: 3.

| # | What | Result | Status |
|---|---|---|---|
| GDP-D3 | The growth-floor test (interpretation hand-appended AFTER the print) | (i) ALL country-decades 1950s-2010s: <1%/yr growth decades median real equity **+3.5%** (n=16); 1-3%: **+8.9%** (n=65); >3%: **+4.9%** (n=31). (ii) EX-HIGH-INFLATION: **+3.5% / +9.1% / +5.7%** — and the <1% bucket's n stays 16: the stagnation decades were NOT the high-inflation decades, so the inflation confounder does NOT explain the floor. **BAR: <1% bucket lower by >=3pp in BOTH cells (5.4pp and 5.6pp) — the PRINCIPAL'S FLOOR INTUITION IS CONFIRMED within support.** PRIOR MISS booked: the registration gave 60% that the gap mostly vanishes ex-inflation — it did not budge. THE FULL SHAPE IS A HUMP: the >3% bucket ALSO trails the middle by ~4pp — stagnation hurts through the earnings floor (the principal's channel), boom-growth hurts through dilution/pricing (ER-D1/D2's channel), and the 1-3% middle is the sweet spot. This RECONCILES the negative correlations (driven by the right side of the hump, where panel variation lives) with the floor. (iii) Named cases as registered: Japan 1990-2020 growth +0.8%/yr -> real equity **-0.1%/yr for 30 years** (valuation-unwind confounder stated); Switzerland 1950-2020 growth +1.5%/yr -> **+6.3%/yr** — the counterexample: the floor binds when the index's REVENUE is domestic; it does not when large-caps earn globally and slippage is negative (CH -2.8pp). Median-stock version remains DATA-GATED as registered | **floor confirmed within support; hump shape booked; prior miss recorded; ER-arc growth reads get the dated qualifier below; census +3 = 325** |

**Dated qualifier (2026-09-07, per GDP-D3's bar) on the ER-arc growth reads:** "growth-
negative" (ER-D1/D1b) describes the panel's observed support — economies growing ~1-4%/yr,
where the dilution/priced-in channel dominates. It does NOT extend to the stagnation left
tail: below ~1%/yr decade growth the earnings floor binds and returns are poor (GDP-D3).
Both channels are real; the sweet spot is the middle.

## Entry ER-D9 (2026-09-07) — PRE-REGISTERED before running: the cross-country long-run
structure sweep + the dividend-GDP tether. Principal directive: deep-dive slippage and
"find other corrl which is logical and cointegrated and has >0.6 corrl." JST R6 1950-2020,
full-sample per-country means (the ER-D2 dot construction), n~15-17 dots, Spearman.
HONESTY DECLARED AT REGISTRATION: (1) with n~16 and 8 candidate cells, chance |rho|~0.5 is
possible — only the mechanism-declared priors below count as confirmations, all cells enter
the census; (2) MECHANICAL-SHARE CAVEAT: return contains delivered dividend growth
positively and slippage contains it negatively, so corr(slippage, return) is PARTLY built
in — the sweep decomposes it: cell (a1) prints corr(dgro, ret) and the between print
corr(mean g, ret) = -0.36 (ER-D1b(6)) already isolates the growth leg; (3) formal
cointegration tests are meaningless on 16 country-means — the registered "tether" cells
are the honest substitute (does the D/GDP ratio mean-revert within countries?).
CELLS (10):
(a) cross-country corr(full-sample mean X, real equity CAGR), one cell each, priors fixed:
  a1 delivered real dividend growth (prior: STRONGEST positive, >= +0.6; partly mechanical
     — declared sanity anchor, not independent evidence);
  a2 mean inflation (prior: -0.4..-0.7 — chronic inflation is chronic expropriation);
  a3 real government bond return (prior: +0.5..+0.8 — the INSTITUTIONS common factor:
     regimes that protected bondholders protected shareholders; the repression panel
     showed both crushed together);
  a4 real bill return (prior: positive, weaker than a3);
  a5 equity return volatility, std of annual real returns (prior: NEGATIVE -0.3..-0.6 —
     no cross-country reward for country risk, the DMS finding);
  a6 crisisJST count (prior: negative, modest);
  a7 mean debt/GDP (prior: weak, |rho| < 0.4);
  a8 housing real return (prior: +0.3..+0.6 — shared institutional quality).
(b) THE TETHER (cointegration-lite): b1 pooled corr(own-country expanding percentile of
  log(D_real/GDP_real), next-10y change of that log ratio) — prior: <= -0.3 (the ratio
  mean-reverts: dividends and GDP share a trend, so slippage is a bounded WEDGE, not a
  random drift); b2 fraction of countries with negative own-country level->change relation
  (prior: >= 12/15).
BAR (the principal's threshold): cells reported against |rho| >= 0.6 explicitly; only
a1/a3 are EXPECTED to clear it. CONSUMPTION: context — sharpens the ER-D2 read and the
country-quality lens of the reserve/debt monographs; no promotion.
Script: scripts/analyze_er_d9.py. Census: 10.

| # | What | Result | Status |
|---|---|---|---|
| ER-D9 | Cross-country structure sweep + tether (interpretation hand-appended AFTER the print) | (a) n=16 dots: **a1 delivered real dividend growth +0.84 — the ONLY cell clearing the principal's 0.6 bar** (declared partly mechanical: the sanity anchor); a2 inflation -0.49 (in band); a3 real bond return **+0.48 — below the +0.5..+0.8 prior band, near-miss booked** (institutions factor real but moderate); a4 bills +0.40 (as registered); a5 volatility **-0.16 — MISS** (no meaningful cross-country risk-return line either way); a6 crisis count **+0.14 — SIGN MISS**; a7 debt/GDP -0.30 (in band); a8 housing +0.20 — below band, near-miss. (b) **THE TETHER IS REJECTED**: pooled corr(D/GDP percentile, next-10y ratio change) = **+0.15 (prior <= -0.3 — SIGN MISS)**; own-country negative in only **8/15 (prior >=12)**. Dividends and GDP do NOT share a mean-reverting ratio at the 10y scale — the slippage wedge is PERSISTENT/TRENDING, a structural country characteristic that COMPOUNDS rather than self-corrects. Honest read: this strengthens ER-D2's cross-sectional map (-0.79) while killing any "the wedge will close" argument — high-slippage countries stay high-slippage; there is no cointegration rescue for the growth-buyer. Five prior misses booked in one sweep — the register working | **one 0.6-clearer (the cash-flow engine); tether rejected; misses booked; census +10 = 335** |

## Entry GDP-D4 (2026-09-07) — PRE-REGISTERED before running: the within-country growth ->
future-return grid across window combinations. Principal directive: "do it for 5-5, 10-5,
10-10, 20-20, 20-10y" (extending ER-D1b's trail-5y -> next-10y median -0.41). JST R6
1950-2020, same conventions. For each combo (trailing real GDP/cap growth over k years ->
real equity CAGR over next h years): (i) MEDIAN across countries of the own-country
Spearman (>=25 usable starts required per country), (ii) pooled Spearman companion.
Combos: (k,h) = (5,5), (10,5), (10,10), (20,10), (20,20). CELLS: 5 x 2 = 10.
DECLARED CAVEAT: at (20,20) a 70y sample holds ~31 overlapping starts per country but
fewer than TWO independent blocks — booked with that flag; no p-values anywhere.
PRIORS (fixed now): all combos NEGATIVE; magnitude non-decreasing in the trailing window
(20y-trailing most negative — long-run growth reputations are the most fully priced and
most dilution-generating); medians in the -0.2..-0.55 range; pooled slightly less negative
than medians at long k (the between-country dp dilution effect). Misses recorded as
always. CONSUMPTION: context — sharpens the ER-arc growth doctrine; no promotion.
Script: scripts/analyze_gdp_d4.py. Census: 10.

| # | What | Result | Status |
|---|---|---|---|
| GDP-D4 | Within-country growth->return window grid (interpretation hand-appended AFTER the print) | median own-country rho / pooled: **5-5: -0.32/-0.28; 10-5: -0.36/-0.31; 10-10: -0.36/-0.29; 20-10: -0.05/-0.05; 20-20: +0.12/-0.02** (all 16 countries per cell; 20-20 sign-only per the declared caveat). **PRIOR MISS booked**: the registration called 20y-trailing the most negative — instead the effect PEAKS at 5-10y trailing and VANISHES at 20y. Sharpened doctrine: the anti-growth signal is a MEDIUM-TERM CYCLE phenomenon — a strong 5-10 year growth RUN is what gets priced, diluted, and mean-reverted against; a country's 20-year growth CHARACTER carries no signal either way (consistent with GDP-D1(i)'s weak level effect and GDP-D3's hump: the permanent level doesn't price, the recent run does). With ER-D1b's 5y->10y median -0.41, the full within-country map: dangerous = fresh 5-10y booms; neutral = long-run growth identity | **grid booked; prior miss recorded; census +10 = 345** |

## Entry CU-D1..D5 (2026-09-07) — PRE-REGISTERED before running: THE CURRENCY BATTERY.
Principal directive: "lets now move from gdp to currency, show all max u can with data
regression model research." Data: JST R6 (xrusd = local per USD, cpi, eq_tr, stir, peg
flags; 1950-2020, USD cross-rates so USA excluded where FX is the variable), fx vault
USDINR monthly 1973-2026, gold USD monthly (gold-INR = gold_usd x USDINR), IIMA market.
Conventions fixed NOW: depreciation_t = Δlog xrusd (positive = local currency WEAKENS);
inflation differential = local infl − US infl; REAL exchange rate RER_t (real value of
local currency) = −(log xrusd + log cpi_us − log cpi_local), so HIGH RER percentile =
locally EXPENSIVE currency; RER percentile = own-country expanding percentile (min_obs=20,
usable 1970+); USD investor return = (1+eq_tr)x(xr_t-1... prior year xr / current) − 1,
deflated by US CPI. Overlap flagged; no p-values; Spearman throughout.

**CU-D1 — PPP: the currency's gravity (3 cells).** (i) cross-country corr(mean annual
depreciation, mean inflation differential), full sample — PRIOR: >= +0.8 (the PPP anchor;
the FX analog of ER-D9's a1 sanity cell). (ii) pooled corr(RER percentile, next-5y RER
change) — PRIOR: <= −0.3 (REAL exchange rates DO mean-revert — the opposite of the
rejected dividend/GDP tether; Rogoff 1996). (iii) implied half-life from the pooled AR(1)
of demeaned log RER — PRIOR: 3-7 years (the PPP puzzle range).
**CU-D2 — UIP/carry: does the interest differential price? (2 cells).** Pooled OLS slope
of next-1y depreciation on (stir − stir_US): UIP predicts +1. (i) slope, floating years
only (peg==0); (ii) within-country Spearman median. PRIOR (Fama 1984 forward-premium
puzzle): slope well BELOW 1, plausibly <= 0.5 — high-rate currencies do not depreciate
enough, carry historically paid; stated two-sided on the exact value.
**CU-D3 — FX and equity returns (3 cells).** (i) same-year pooled corr(depreciation, local
REAL equity return) — PRIOR: negative (−0.1..−0.35): depreciation years are stress years.
(ii) RER percentile -> next-5y LOCAL real equity CAGR, pooled — PRIOR: negative (cheap
currency -> competitiveness + reversion tailwind), −0.1..−0.3. (iii) RER percentile ->
next-5y USD real return of that market — PRIOR: MORE negative than (ii) (FX reversion adds
directly for the USD investor), −0.2..−0.4. [High percentile = expensive currency, so
NEGATIVE rho = cheap-currency markets pay more.]
**CU-D4 — currency crashes (3 cells).** Crash year = depreciation >= 15% (fixed threshold,
~top decile). (i) local real equity return in crash years vs all other years (pooled
means); (ii) GOLD in LOCAL currency, real, in crash years vs others (JST panel: gold_usd x
xrusd deflated by local cpi) — PRIOR: strongly positive in crash years (>= +15% mean; the
gold book's crash-hedge print); (iii) next-3y local real equity CAGR after a crash year —
PRIOR: two-sided (recovery vs continued stress).
**CU-D5 — India partial (2 cells, short sample, descriptive).** (i) same-year corr(USDINR
annual depreciation, IIMA real... IIMA is nominal INR — use NOMINAL excess and state it)
1994-2025; (ii) gold-INR return in the 5 worst INR years since 1994 vs its other-year
mean. No bars (descriptive).
CONSUMPTION: context for the FX/gold seats (L23 dollar cycle, the gold book, Tier-C
descent playbook); no promotion. Script: scripts/analyze_cu_battery.py. Census: 13.

| # | What | Result | Status |
|---|---|---|---|
| CU-D1..D5 | The currency battery (interpretation hand-appended AFTER the print) | **CU-D1 PPP: (i) +0.94** (n=17) — the strongest cross-country relation in the register: long-run depreciation IS the inflation differential (bar >=+0.8 PASS). (ii) RER percentile -> next-5y RER change **-0.40** — REAL exchange rates mean-revert (bar <=-0.3 PASS): the tether that FAILED for dividends/GDP HOLDS for currencies. (iii) half-life **7.3y** vs the 3-7y prior band — boundary miss booked (Rogoff-puzzle-slow, annual pooled). **CU-D2 UIP: slope -0.06** vs the predicted +1 (floating years, n=352; 6 se's below) — the Fama-1984 forward-premium puzzle reproduced: rate differentials do NOT price 1y FX; carry historically paid; within-country median -0.18. **CU-D3: (i) same-year dep vs LOCAL real equity +0.02 — PRIOR MISS** (expected negative): at the panel level, local equities are currency-crash-neutral (real-asset pass-through nets out exporters/importers). (ii) RER -> next-5y local equity -0.18 (in band). (iii) RER -> next-5y **USD** return **-0.36** (in band, stronger as registered): buying cheap-currency markets pays the USD investor double — FX reversion stacks on equity. **CU-D4 crashes (dep >=15%, n=71): (i) local real equity in crash years +8.7% vs +8.5% others — PRIOR MISS**, equities self-hedge their currency at index level; (ii) gold-in-local-currency real: **+8.8% in crash years vs +2.7% others** — direction PASS, magnitude bar (>=15%) missed, ~6pp crash premium booked; (iii) next-3y after crash **+13.2%/yr vs +6.2%** — the two-sided cell resolves to RECOVERY: crash years are entry states, not exit states. **CU-D5 India: (i) same-year corr(INR dep, market) -0.69** (n=32) — India is the OPPOSITE of the panel's +0.02: INR weakness and equity weakness are one event (the Rey/FII global-flows channel, L22/L26 vindicated); (ii) gold-INR in the 5 worst INR years +13.4% vs +12.0% other years — the annual edge is mild because gold-INR pays in ALL years (secular INR depreciation + gold), the hedge value is at stress horizons (T-series Sharpe 1.19 stands) | **PPP/UIP doctrine landed; 3 misses booked; India's FX-equity coupling (-0.69) is the panel outlier and the design consequence; census +13 = 358** |

## Entry CU-D6 (2026-09-07) — PRE-REGISTERED before running: the FX -> equity matrix in
BOTH denominations. Principal directive: "currency impacts on stock market mostly in both
local and global currency." Same data/conventions as CU-D1..D5 (JST R6 1950-2020, 17
non-US; depreciation = Δlog xrusd, + = weaker; local return = real in local CPI; USD
return = FX-converted, real in US CPI; India = IIMA nominal market 1994-2025 with USDINR,
NOMINAL both legs — stated).
CELLS (12):
(a) SAME-YEAR, pooled: a1 corr(depreciation, USD real return) — PRIOR: -0.4..-0.6 (the
mechanical pass-through, partially offset); a2 pass-through beta (OLS of USD real return
on depreciation) — PRIOR: -0.6..-1.0, i.e. the local market does NOT rise enough in a
depreciation year to shield the USD investor.
(b) DEPRECIATION-REGIME BUCKETS (fixed: dep >= +10% weak-year / -5..+10% normal /
<= -5% strong-year): mean SAME-YEAR local real and USD real (2 cells), mean NEXT-1y local
and USD (2 cells). PRIORS: weak-years -> local ~flat, USD strongly negative; next-1y after
weak-years positive in BOTH, USD stronger (reversion).
(c) PREDICTIVE: trailing-5y depreciation -> next-5y c1 LOCAL real CAGR and c2 USD real
CAGR, pooled Spearman. PRIOR: both POSITIVE (past weakness = cheap currency), USD larger
(+0.15..+0.35) — the mirror of CU-D3(iii).
(d) INDIA (descriptive, short): d1 same-year corr(INR dep, USD market return) — PRIOR:
<= -0.75 (the -0.69 local coupling PLUS mechanical FX); d2 bucket means both denominations;
d3 next-1y after weak-INR years, both denominations.
CONSUMPTION: context for the gold/FX cluster and any future USD-share reporting of the
books; no promotion. Script: scripts/analyze_cu_d6.py. Census: 12.

| # | What | Result | Status |
|---|---|---|---|
| CU-D6 | FX -> equity in both denominations (interpretation hand-appended AFTER the print) | (a) same-year corr(dep, USD real ret) **-0.36** (prior -0.4..-0.6, near-miss by 0.04, booked); pass-through beta **-0.99** — FULL pass-through: the local market gives the USD investor ZERO same-year shield. (b) buckets: WEAK-currency years (dep>=10%, n=185): local real **+11.6%** vs USD **-3.2%**; normal: +8.3/+8.1; STRONG-currency years: local +7.0 vs USD **+21.4%**. NEXT-1y after weak years: **+13.8% local / +13.9% USD** vs 6.7/7.9 normal — reversion pays both denominations, as registered. Refinement of CU-D3(i): local real returns are actually HIGHER in weak-currency years — for the LOCAL investor, depreciation is mildly good (competitiveness + real-asset repricing); the damage is entirely the USD leg. (c) trail-5y depreciation -> next-5y: local **+0.22**, USD **+0.32** — both positive, USD larger, as registered (the mirror of CU-D3(iii)). (d) INDIA: same-year corr with USD return **-0.79** (prior <=-0.75 PASS); weak-INR years (dep>=5%, n=11): local **-12.6%** / USD **-20.6%** vs **+34.2%/+35.5%** in other years — a ~50pp regime split, the double-hit quantified; NEXT year after weak-INR: **+25.5% local / +23.7% USD** — the crash-year-as-entry-state result reproduced at India scale (2013->2014 pattern is systematic) | **matrix booked; the panel/India asymmetry is the doctrine: panel-wide FX weakness is a USD-leg problem only; in India it is everyone's problem the same year and historically the entry state the next; census +12 = 370** |

## Entry CU-D7 (2026-09-07) — PRE-REGISTERED before running: crash anatomy + India/US
regime tables. Principal directive: detail the >=15% crash set, more data points, and the
CU-D6 regime table separately for India and the US. Same conventions as CU-D1..D6. The US
has no depreciation-vs-USD, so its registered regime variable is the BROAD DOLLAR: the
equal-weight mean Δlog xrusd across the 17 panel currencies (positive = USD strong).
CELLS (14):
(a) CRASH ANATOMY, panel dep>=15% (6): a1 episode census — count by decade + median/max
depreciation (descriptive); a2 crash-year LOCAL real: median + hit-rate (%>0) alongside
the booked mean; a3 crash-year USD real: median + hit-rate; a4 next-1y medians both
denominations; a5 next-3y CAGR medians both; a6 gold-in-local real median in crash years
vs others. PRIORS: local median BELOW the +8.7% mean (skew from high-inflation years),
hit-rate 50-60%; USD median -8..-15%, hit-rate < 40%; next-1y/3y medians positive both
denominations; gold-local crash median positive.
(b) INDIA regime table, buckets fixed NOW (weak dep>=8% / normal -2..8% / strong <=-2%),
IIMA nominal market + USDINR 1994-2025 (5): b1-b2 same-year local and USD means per
bucket; b3-b4 next-1y local and USD; b5 the INR >=15% crash-year list since 1973 with
outcomes (descriptive; equity coverage only from 1994). PRIORS: weak bucket local negative
and USD worse; next-1y after weak strongly positive (CU-D6 pattern at the sharper cut).
(c) US dollar-regime table (3): c1 same-year corr(broad-dollar change, US real equity) —
PRIOR: weakly positive, two-sided stated (risk-off strengthens USD and sinks stocks, but
strong-USD eras were US-strong eras); c2 bucket means (strong >=+5% / normal / weak
<=-5%) same-year US real equity; c3 next-1y US real equity per bucket. CONSUMPTION:
context for the gold/FX cluster and L23 (dollar cycle); no promotion.
Script: scripts/analyze_cu_d7.py. Census: 14.

| # | What | Result | Status |
|---|---|---|---|
| CU-D7 | Crash anatomy + India/US regime tables (interpretation hand-appended AFTER the print) | (a1) 71 crashes: **32 of 71 in the 1980s** (the EMS/Volcker era); top crashers Spain 8, Portugal 7, Sweden 7, UK 7, Italy 6 — the European soft-currency club, NOT emerging markets; median dep 20%, max Portugal 1983 (39%). (a2) crash-yr LOCAL real: mean +8.7 / median **+8.7** / 67% positive — **PRIOR MISS (pleasant)**: no skew, the local-equity crash immunity is robust, not a mean artifact. (a3) crash-yr USD: median **-8.8%**, only 38% positive (in band). (a4) next-1y: LOCAL median **+18.3% (79% positive)**, USD median +12.0% (65%). (a5) next-3y CAGR medians: +10.5% local (83% pos) / +13.4% USD (79% pos). (a6) gold-local real in crash years: median **+8.2%** vs **-1.1%** in other years — a ~9pp MEDIAN spread, stronger than the mean print. (b) INDIA table (1994-2025, nominal): WEAK INR (dep>=8%, n=7): **-15.2% local / -24.4% USD**; normal (n=18): +17.3/+14.0; STRONG INR (n=7): **+53.7% local / +62.4% USD** — INR-strength years are the monster years (the inflow side of the same Rey coupling); next-1y after WEAK: **+24.4/+23.1**; after STRONG: only +7.3/+7.0 — chasing strength pays nothing. INR >=15% crashes since 1973: **1984 (16%), 1991 (35%), 2008 (21%)**. (c) US: same-year corr(broad dollar, US real equity) **-0.03 — PRIOR MISS** (registered weakly positive); the bucket table is a HUMP: USD-strong years +5.8%, normal **+11.3%**, USD-weak +6.4% — BOTH dollar extremes are below-normal for US equities; next-1y roughly flat (6.7/9.7/8.0) | **anatomy booked; 2 misses recorded; the crash playbook (below) enters the gold/Tier-C context; census +14 = 384** |

## Entry DB-D1..D5 (2026-09-07) — PRE-REGISTERED before running: THE DEBT BATTERY.
Principal directive: "move to debt cycle... lessor data so we can study outliers and us
and historical pattern." Data: JST R6 1870-2020 (debtgdp = public debt/GDP; tloans/gdp =
private credit; crisisJST; eq_tr, bond_tr, cpi), full-span deliberately (the outliers ARE
the pre-1950 wars); own-country expanding percentiles (min_obs=20) for level states;
Spearman; overlap flagged, no p-values. Research anchors declared: Reinhart-Rogoff 90%
threshold; Reinhart-Sbrancia repression; Mian-Sufi-Verner 2017 (credit growth -> lower
future returns); our own credit monograph (gap->crisis AUROC — levels-not-directions
already seated there).
CELLS (16):
**DB-D1 — levels (4):** public-debt percentile -> next-5y/10y real equity (2); private
credit/GDP percentile -> next-5y/10y real equity (2). PRIOR: all |rho| <= 0.15 — debt
LEVELS do not price equities (the levels-doctrine extended to debt).
**DB-D2 — the outlier club (4):** d1 episode census, descriptive: all country-years with
public debt/GDP >= 100%, grouped into episodes (entry year = first year >= 100% after >=5y
below), listed with country/era; d2 from >=100% starts: next-10y REAL BOND CAGR vs REAL
EQUITY CAGR (medians + hit-rates) — THE REGISTERED ASYMMETRY: bonds NEGATIVE median
(repression/inflation is how debt resolves), equities positive median (the repression
playbook); d3 the same at >=130% (deeper outliers, worse bonds); d4 resolution table:
for each episode entry, debt at +10y/+20y and mean inflation next-10y (mechanical; the
taxonomy is the hand-appended read).
**DB-D3 — acceleration (4):** 5y Δ(public debt/GDP) -> next-5y real equity (prior: ~0 to
mildly POSITIVE — public debt rises after busts, equities recover); 5y Δ(private
credit/GDP) -> next-5y real equity (prior: NEGATIVE -0.1..-0.3 — the MSV credit-boom
hangover); same Δprivate -> next-5y real BOND return (prior: positive-ish — busts bring
disinflation); Δprivate own-country expanding-rank variant -> next-5y equity (prior:
negative, similar).
**DB-D4 — the US arc (2):** d1 the US public-debt peaks 1870-2020 named + levels
(descriptive); d2 for each US year with debt >= 90%: next-10y real equity, real bond,
inflation (the US high-debt playbook table).
**DB-D5 — twin peaks (2):** 2x2 state (public debt percentile >= 0.8 x private credit
percentile >= 0.8): next-5y real equity mean per cell (1); crisis frequency (crisisJST
within next 3y) per cell (1). PRIOR: the twin-high cell is the worst for equities and the
highest crisis rate (the fiscal-space + credit-boom interaction).
CONSUMPTION: context for the L1 credit band, DS1/Tier-C, and the repression playbook; no
promotion. Script: scripts/analyze_db_battery.py. Census: 16.

| # | What | Result | Status |
|---|---|---|---|
| DB-D1..D5 | The debt battery (interpretation hand-appended AFTER the print) | **DB-D1 levels**: public-debt percentile -> next-5y/10y equity **+0.16/+0.17** — misses the <=|0.15| bar by a hair, POSITIVE sign: high public debt has never been bad for subsequent equities in this record; private credit -0.10/-0.14 (in bar). **DB-D2 the >=100% club**: 295 country-years, 34 episodes listed. REGISTERED ASYMMETRY PARTIAL MISS: next-10y real bonds from >=100% starts median **+3.3% (70%>0)** — NOT negative as registered; equity +3.8% (81%>0); at >=130% bonds degrade to +1.3%/56% while equity holds +3.7%/84% (the DIRECTION of the asymmetry held, the bond sign did not). The resolution table explains the miss — THREE RESOLUTION REGIMES: (i) the 1940s cohort resolved violently or by repression (Germany 102->19 via reform-default; Japan 105->13 at 136%/yr inflation; Italy 110->32 at 61%; US/UK/Canada/Benelux ground it down at 4-5% inflation — the cohort where bonds died); (ii) pre-1914 episodes drifted under gold-standard deflation; (iii) **the post-1983 cohort does not resolve at all — it CARRIES** (Italy 101->126, Japan 105->231, Belgium round-trips) in disinflation, which is exactly where long bonds printed their best decade returns — hence the pooled positive bond median. DS1's "arc unresolved" now has its mechanism cohort. **DB-D3 acceleration**: d(private)->equity **+0.01 — PRIOR MISS** (the MSV hangover does NOT show at pooled 5y return level; the credit gap's power stays where the credit monograph seated it — CRISIS odds, not average returns); d(public)->equity +0.14 (post-bust recoveries, as registered). **DB-D4 US**: arc 31% (1870) -> 119% (1946) -> 33% (1974) -> 128% (2020); from US >=90% years: next-10y real equity median **+13.7% (7/7 positive)** vs real bonds median **-1.0% (1/7 positive)** — the repression asymmetry is crisp exactly in the US high-debt cohort. **DB-D5 twin peaks — PRIOR MISS**: the worst equity cell is LOW-public x HIGH-private (+3.9%), not twin-high (+6.2%); crisis-in-3y is ~12-14% whenever PRIVATE credit is high vs ~4% otherwise, regardless of public debt. Private credit is the crisis variable; public debt alone pairs with BETTER subsequent equity (+7.7%) | **doom-priors refuted: high public debt kills BONDS (US cohort 1/7 positive), not equities; private booms make crises, not low average returns; the modern era carries rather than resolves; census +16 = 400** |

## Entry DB-D6/D7 (2026-09-07) — PRE-REGISTERED before running: fiscal dominance + the
housing extension + top-carrier profiles. Principal directives: (i) "isn't it if debt/gdp
is too high country will be forced not to raise interest... inflation higher as real bond
yield would be negative" — the FISCAL-DOMINANCE fingerprint, testable; (ii) the honest
debt->GDP cell (the prior battery tested debt->EQUITY only — stated); (iii) housing added
to the debt/currency/growth batteries (the missed asset); (iv) top-carrier asset profiles.
Data: JST R6 full span, conventions as DB-D1..D5; housing = housing_tr real; gold-local as
CU-D4. STATED LIMITS: JST has headline CPI only (no food-CPI split), no company/sector
data — those need principal pulls; profiles are index-level.
**DB-D6 — fiscal dominance (7 cells):**
f1 pooled corr(public-debt pct, same-year real bill rate) — PRIOR: NEGATIVE <= -0.15;
f2 pooled corr(debt pct, next-5y mean real bill) — PRIOR: negative (repression persists);
f3 within-country median corr(debt pct, real long rate) — PRIOR: negative;
f4 REAL BILL RATE by debt bucket (<60 / 60-90 / 90-120 / >=120%) — PRIOR: monotone down,
   >=120% bucket NEGATIVE (the principal's spiral-prevention threshold made visible);
f5 INFLATION by the same buckets — TWO-SIDED (the 1940s cohort says up, the post-1983
   carry cohort says down);
f6 r-g (real bill minus real GDP/cap growth) by bucket — PRIOR: most negative at >=120%
   (the carry condition that lets debt sit);
f7 the honest debt->GDP cell: next-5y real GDP/cap growth by bucket — PRIOR: mild decline
   at high debt, NO cliff (Reinhart-Rogoff 90% as corrected by Herndon-Ash-Pollin).
**DB-D7 — housing everywhere (6 cells):**
h1 debt buckets -> next-5y real housing return — two-sided, lean positive (repression
   pushes savings into real assets; the 1950-80 panel's housing win);
h2 currency-crash years (dep>=15%) -> same-year + next-1y housing local real — PRIOR:
   resilient like equities (crash-neutral or better);
h3 trailing-5y GDP growth -> next-5y housing, pooled — PRIOR: LESS NEGATIVE THAN EQUITIES
   (>= -0.1 vs equity's -0.22): housing has NO dilution channel and no market pre-pricing,
   so if the equity growth-negative is dilution/pricing (ER-D2), housing should escape it —
   a MECHANISM TEST of the slippage doctrine;
h4 5y d(private credit) -> next-5y housing — PRIOR: NEGATIVE and worse than equities
   (housing is the financial-cycle bust asset, JST/L12);
h5 own-country inflation quintiles -> same-year housing real — PRIOR: top-quintile housing
   BEATS top-quintile equities (-4.1% booked): the better inflation-year real asset;
h6 gold-local real in >=90% public-debt years vs others — PRIOR: positive premium.
**DB-D8 — top-carrier profiles (2 cells, descriptive):** for UK 1918-1964, US 1945-1950,
Belgium 1983-2003, Italy 1992-2020, Japan 1997-2020: within-episode real CAGRs of equity,
bonds, bills, housing, gold-local + mean inflation + crisis years. CONSUMPTION: context
(monograph 0.1, L9, L12, the gold book); no promotion.
Script: scripts/analyze_db_d678.py. Census: 15.

| # | What | Result | Status |
|---|---|---|---|
| DB-D6/D7/D8 | Fiscal dominance + housing + profiles (interpretation hand-appended AFTER the print) | **D6**: f1/f2/f3 debt-pct vs real rates +0.03/+0.01/+0.14 — **correlation-form MISSES** (no smooth relation); but the BUCKET form carries the principal's threshold: f4 real bills 1.3 -> 1.1 -> 1.1 -> **0.5% at >=120%** (monotone down; the registered "negative at >=120%" missed — repressed, not negative); f5 inflation **4.2 -> 2.6% — the inflation leg of the hypothesis REJECTED in the pooled record**: high-debt eras were LOWER-inflation eras (the modern carry mode; the 1940s cohort is the exception, not the rule); f6 r-g most negative at >=120% (**-1.3%**) — the spiral-prevention is real and achieved by rates-below-GROWTH, with disinflation, not inflation; f7 debt->next-5y GDP/cap growth **2.0 / 1.2 / 1.0 / 0.7% — monotone decline, NO cliff at 90%** (HAP-corrected RR shape; maturity/aging confound stated). **D7 housing**: h1 positive in every debt bucket (6.9 -> 5.4); h2 currency-crash years +2.9% same-yr, +5.5% next — resilient as registered; **h3 THE MECHANISM TEST: growth -> next-5y HOUSING +0.09 vs EQUITY -0.09** — housing, which has no dilution and no market pre-pricing, does NOT show the growth-negative: the ER-D2 slippage/pricing explanation of the equity result is CONFIRMED by the asset that lacks the channel; h4 credit boom -> housing -0.12 (vs equities +0.01) — housing is the financial-cycle bust asset, as registered (L12); h5 top-own-inflation years: housing **+2.6% vs equities -2.2%** — the better inflation-year real asset; h6 gold-local +4.6% in >=90% debt years vs +2.7%. **D8 profiles** (real CAGR %/yr): UK 1918-64: eq 5.2 / bonds 0.7 / bills -0.2 / housing 4.3 / gold -0.2 / infl 2.9. USA 1945-50: eq 7.5 / bonds **-2.5** / bills **-4.1** / housing **+8.9** / gold -4.7 / infl 5.5. Belgium 1983-2003: eq 10.6 / bonds **+8.0** / housing 9.3 / infl 2.6. Italy 1992-2020: **bonds +6.7 BEAT equities +4.6** / housing 3.5 / gold 4.7. Japan 1997-2020: **gold +6.3 beat everything**; bonds 3.4 > housing 2.9 > eq 2.1; infl 0.2. THE EPISODE DOCTRINE: repression mode (US/UK 1940s) pays equities+housing and kills paper; carry mode (Belgium/Italy/Japan) pays BONDS and gold — the high-debt playbook is decided by the L9 inflation-regime state, not the debt level | **hypothesis verdict: repressed-rates and r<g CONFIRMED at >=120%, inflation leg REJECTED in the modern mode; debt->growth monotone decline booked (no cliff); housing mechanism test confirms the slippage doctrine; census +15 = 415** |

## Entry DB-D9 (2026-09-07) — PRE-REGISTERED before running: is the high-debt equity
positivity real, what does debt do to the CURRENCY, and the leveraged-real-asset spread.
Principal directives verbatim: "high debt impact on equity in positive way? what about
currency and is it good time to buy real assets with debt?" JST R6, conventions as before.
CELLS (7):
c1 debt percentile -> next-5y annualized depreciation vs USD (pooled Spearman, non-US) —
   TWO-SIDED prior: near zero (PPP says INFLATION drives FX, and the modern high-debt mode
   is low-inflation; the 1940s mode would say positive).
c2 next-5y depreciation by debt bucket (<60/60-90/90-120/>=120) — prior: NOT monotone.
c3 THE BORROWER'S SPREAD: (real housing return - real long rate) same-year mean by debt
   bucket — PRIOR: WIDEST at >=120% (repression subsidizes the leveraged owner of real
   assets); c4 the same with equities. 
c5 era-split of the high-debt equity positivity: debt pct -> next-5y real equity, pre-1980
   vs post-1980 (2 cells) — TWO-SIDED: if positive only post-1980 it is the disinflation
   era in disguise.
c6 valuation control: within own-country dp terciles, mean next-5y equity for high-debt
   (pct>=0.8) vs rest — PRIOR: the debt effect mostly WASHES OUT given valuation (debt is
   not a positive signal; it is the absence of a negative one).
CONSUMPTION: context; no promotion. Script: scripts/analyze_db_d9.py. Census: 7.

| # | What | Result | Status |
|---|---|---|---|
| DB-D9 | Equity-positivity checks + debt->currency + the borrower's spread (interpretation hand-appended AFTER the print; c3 f-string typo fixed pre-print, run note) | c1 debt pct -> next-5y depreciation pooled **+0.01** (two-sided prior lands ~0) BUT c2 the bucket tail bites: <60% +0.8 / 60-90% +1.9 / 90-120% +1.6 / **>=120% +3.7%/yr** — the extreme club leaks its currency ~3pp/yr faster. c3 borrower spread (housing - real long rate): **positive in EVERY bucket** (+5.5/+3.6/+3.1/+3.6) — prior "widest at >=120%" MISSED (widest at LOW debt); c4 equity - real long rate: +4.9/+5.4/+3.1/**+5.7% at >=120%** (widest at high debt, as registered, in the equity form). c5 THE ERA SPLIT SETTLES IT: debt pct -> next-5y equity **pre-1980 +0.19, post-1980 -0.05** — the high-debt equity positivity is a PRE-1980 phenomenon (war-recovery entry points + repression herding savers into equities); in the modern carry era debt tells you NOTHING about equities either way. c6 valuation control: the effect persists within dp terciles (cheap+high-debt +10.5% vs +6.8%) — so within the old era it was real, not just valuation; but c5 rules it out as a modern signal. PARTIAL MISS on "washes out" booked | **the myth dies both ways: high debt is neither a reason to avoid equities (81% positive 10y windows) nor a modern reason to buy them (-0.05 post-1980); the >=120% tail leaks FX at ~3.7%/yr; the leveraged-real-asset spread has been positive in every regime with the L12 credit-bust caveat; census +7 = 422** |

## Entry CI-D1..D5 (2026-09-07) — PRE-REGISTERED before running: THE CREDIT + INFLATION
BATTERY. Principal directive verbatim: "okay, lets move to credit, inflation impacts and
stocks." Data: JST R6; CI-D1/D2 on 1950-2020 (war/hyperinflation regimes excluded,
matching FISH-D1's stated span); CI-D3/D4 on the full 1870-2020 span (credit booms and
crises are sparse; matching the DB battery's stated span). Conventions: real return =
(1+nom)/(1+infl)-1; Dinfl_t = infl_t - infl_{t-1} (pp of annual CPI inflation);
ACCELERATION = Dinfl >= +2pp, DECELERATION = Dinfl <= -2pp; HIGH inflation = own-country
expanding percentile >= 0.8 (min_obs=20, the ER-D1b(9) construction); RISING = Dinfl > 0;
CREDIT BOOM = own-country expanding rank of 5y d(tloans/gdp) >= 0.8 (the DB-D3 rank
construction); gold-local real as CU-D4/DB-D6; Spearman throughout; overlapping windows
flagged, p-values never trusted. NO OOS/no-lookahead claims anywhere in this battery, so
PROCESS NOTE #8 fields are not triggered (stated). Parent prints quoted to avoid duplicate
cells: FISH-D1 (1y Fisher beta -0.21; pooled regime gap 12.0pp with the sign-miss);
ER-D1b(9) (within-country gap 18.2pp; top-own-quintile years -4.1%/yr real); DB-D1
(private-credit percentile -> 5/10y equity -0.10/-0.14); DB-D3 (5y d(private) -> next-5y
equity +0.01 pooled null); DB-D5 (crisis-in-3y 12-14% when private credit high vs ~4%);
DB-D7 h4 (credit boom -> housing -0.12) and h5 (top-inflation years: housing +2.6% vs
equities -2.2%).
CELLS (20):
**CI-D1 — inflation DYNAMICS (5): the direct test of the L9 claim "the killer is
acceleration" (booked as INTERPRETATION in FISH-D1(iii) and never tested).**
- i1 same-year real equity by Dinfl bucket (accel >=+2pp / stable / decel <=-2pp) — PRIOR:
  acceleration years <= -5%/yr; deceleration years >= +10%/yr (the disinflation rally);
  monotone across the three buckets.
- i2 the 2x2 LEVEL (own pct >=0.8) x DIRECTION (rising/falling) same-year real equity —
  PRIOR: high+rising is the killer cell (<= -8%/yr); high+falling POSITIVE. The registered
  decomposition claim: ER-D1b(9)'s -4.1%/yr top-quintile number splits into a deeply
  negative rising half and a positive falling half.
- i3 pooled corr(Dinfl, same-year real equity) — PRIOR: <= -0.25.
- i4 pooled corr(infl LEVEL, same-year real equity) — PRIOR: |i3| > |i4| (change beats
  level; if the level wins, the L9 sharpening is REFUSED and recorded).
- i5 next-1y real equity after acceleration years — PRIOR: positive (recovery), lean only
  (the CU-D4 crash-recovery analogy).
**CI-D2 — the cross-asset regime table (5):** same-year REAL returns of equity, bonds,
bills, housing, gold-local (one read per asset) across i2's four cells — PRIORS: bonds
best in high+falling (the DB-D2 carry cohort's decade); gold best in high+rising; equity
worst in high+rising; housing beats equity in BOTH high cells (DB-D7 h5 quoted) but is
lower when rising; bills negative in both high cells (repression).
**CI-D3 — credit x inflation (4):** the 2x2 CREDIT BOOM x HIGH INFLATION, full span:
- j1 next-5y real equity per cell — TWO-SIDED: boom+high-infl worst is the lean, but
  DB-D3's pooled +0.01 (quoted) means any damage must be CONDITIONAL; a flat 2x2 extends
  the null and the credit gap stays a crisis-odds variable only.
- j2 crisis-in-3y rate per cell — PRIOR: owned by the credit axis (DB-D5 quoted);
  the inflation axis adds <= 3pp within credit states.
- j3 next-5y real BOND per cell — PRIOR: worst in boom+high-infl (duration + default).
- j4 next-5y real HOUSING per cell — PRIOR: credit axis owns it (DB-D7 h4 quoted).
**CI-D4 — the crisis event study (3), full span (crises sparse; stated):**
- k1 real EQUITY event-time means t-1..t+3 around crisisJST=1 (t=0 crisis year) — PRIOR:
  t0 <= -8%/yr; positive by t+2 (recovery).
- k2 the same for real HOUSING — PRIOR: shallower at t0 but SLOWER — still negative at
  t+2 (L12's slow bust; the equity/housing clock difference made event-time).
- k3 crisis-year real equity split by inflation state at entry (own pct >=0.8 vs rest) —
  PRIOR: worse from high-inflation entries.
**CI-D5 — India partial (3):** STATED LIMITS: India CPI is NOT vaulted (runsheet row
stands) so NOMINAL forms only; the IIMA RF (annualized from monthly) is the
rate/inflation-expectation proxy; the India credit leg is data-gated (BIS runsheet row).
- l1 same-year corr(dRF, nominal market return), 1994-2025 — PRIOR: negative (tightening
  years hurt), two-sided stated.
- l2 market nominal return, rising-RF vs falling-RF years (means + medians).
- l3 next-1y market return after rising-RF years — TWO-SIDED (n~15 per side; descriptive
  strength only).
CONSUMPTION: the acceleration verdict enters L9 as a dated update box if i1/i2 confirm;
context for the credit band (L1/L12) and DS1; no promotion, nothing enters the stack.
Script: scripts/analyze_ci_battery.py. Census: 20.

| # | What | Result | Status |
|---|---|---|---|
| CI-D1..D5 | The credit + inflation battery (interpretation hand-appended AFTER the print; i2's n counts complete equity rows, D2's n counts regime-years — stated) | **CI-D1 THE ACCELERATION TEST**: i1 monotone as registered — accel years **-0.4% mean / -1.4% median**, stable +8.7%, decel **+15.8%** (decel bar >=+10 PASS; accel bar <=-5% MISSED — flat-to-negative, not deeply negative); i2 the 2x2: **HIGH+rising -3.0% (median -4.0)** vs **HIGH+falling +4.4%** — the registered decomposition CONFIRMED: ER-D1b(9)'s -4.1%/yr top-quintile number is owned by the RISING half (falling-from-high years are positive); low+rising +6.8 vs low+falling +13.5 — direction splits BOTH levels by ~7pp; i3/i4 **PRIOR MISS, the refusal clause fires**: corr(dinfl, req) -0.20 vs corr(level, req) **-0.24** — in correlation form the LEVEL is not beaten by the change; the killer is the CONJUNCTION (high AND rising), not acceleration per se — L9 sharpened in bucket form only, recorded as measured; i5 next-1y after accel +2.1% mean / +0.1% median — muted recovery (no currency-crash-style rebound). **CI-D2 THE REGIME TABLE** (same-yr real means): HIGH+rising: gold **+9.6** > housing **+6.8** >> equity -3.0 > bills -2.8 > bonds **-5.6** — gold-best and equity-worst as registered; housing NEARLY UNIMPAIRED in the killer cell (the inflation-passthrough asset) and it beats equity there by 9.8pp (h5 extended), but the housing sub-priors partially missed: high+falling housing +4.3 vs equity +4.4 (tie, not a beat) and housing is HIGHER when rising (6.8 > 4.3) — housing hedges the acceleration, not the level; bills negative in both HIGH cells (repression confirmed); bonds' best cell is low+falling (+5.6), NOT high+falling (+0.4) — **MISS**: the carry-cohort's bond decade is the DESCENT INTO low, not the high+falling year itself. **CI-D3 CREDIT x INFLATION**: a clean DIVISION OF LABOR — the INFLATION axis owns returns (equity 3.3-3.4% in HIGH cells vs 5.4-5.9% low, near-identical across credit states: DB-D3's credit-return null extends CONDITIONALLY; the two-sided j1 lands flat-credit); the CREDIT axis owns crises (j2: boom 15.0-19.4% crisis-in-3y vs calm 5.3-6.5% — DB-D5 reproduced; inflation adds +4.4pp within boom, 1.4pp over the <=3pp bar — partial miss); j3 **MISS**: bonds worst in calm+HIGH (-2.5), not boom+HIGH (-0.5) — inflation owns bonds entirely; j4 housing: boom cells lower (3.7/5.4 vs 6.7/7.4) — the credit axis owns housing (DB-D7 h4 in bucket form), worst cell boom+HIGH +3.7%. **CI-D4 THE CRISIS EVENT STUDY** (88 crisis-years): equity t-1 -0.5 / **t0 -14.1** / t+1 +9.7 / t+2 +13.9 / t+3 +4.6 — t0 bar PASS, recovery arrives at t+1 already; k2 **MISS on sign**: housing NEVER prints a negative event-time mean (8.3 -> 4.6 -> 4.3 -> 3.8 -> 4.3) — the slow bust shows as a multi-year SLOWDOWN in the pooled record, not negative means (the L12 Big-5 severity is diluted by 88 pooled crises; stated); k3 crisis-yr equity from HIGH-inflation entry **-18.2%** vs -13.0% other entries — worse as registered. **CI-D5 INDIA** (nominal, RF proxy): l1 corr(dRF, mkt) -0.12 (leaned sign, weak); l2 rising-RF years +15.4% mean vs falling +20.8% (medians 14.9/12.1 — means only); l3 next-1y after tightening +19.1% — no hangover; descriptive strength only, n=31 | **the killer cell is the CONJUNCTION (high + rising): direction splits the level effect ~7pp at both levels but the level survives in corr form (refusal clause fired, recorded); asset ranking in the killer cell booked (gold > housing >> equity > bills > bonds); crises belong to credit, returns to inflation; crisis event-time table booked (t0 -14.1, recovery t+1, housing = slowdown-not-crash); 6 misses/partials recorded; census +20 = 442** |

## Entry SEC-D1..D4 (2026-09-07) — PRE-REGISTERED before running: THE SECTOR BATTERY
(India partial). Principal directive verbatim: "now lets check sectoral impact which
sectors best which worst which unaffected, gdp, debt, credit, currency, inflation."
DATA REALITY, stated first: the only vaulted sector-capable data is the NIFTY500 survivor
panel (n500_adjclose_2012_2022.csv.gz, 487 tickers, daily adjcloses) — SURVIVORSHIP BIAS
KNOWN AND STATED: one-way/RELATIVE reads only (all baskets carry the bias the same
direction, but not equally — differential churn per sector is an unquantified residual,
stated as a limit); equal-weight baskets, not cap-weighted (stated). The US/long-history
sector leg (Ken French industry portfolios) is BLOCKED: the primary host is egress-dead
and a GitHub mirror hunt (repo-scoped probes: Soderlind course repos, Rdatasets index)
came up empty this session — SEC-D5 registered UNRUN below; runsheet row added. India CPI
is NOT vaulted, so the inflation x sector map is NOT runnable here (goes with SEC-D5 /
the CPI runsheet row); the runnable GDP-shock reads are the two event windows (E2, E4) —
the annual growth x sector cell needs longer sector history (stated). Debt/credit at
sector level = the E3 credit-crunch episode + the rate-state cells.
SECTOR BASKETS, fixed NOW (EN-D1a precedent; names absent from the panel are dropped by
the script filter; M&M, NESTLEIND, COFORGE absent from panel — stated):
IT: TCS INFY WIPRO HCLTECH TECHM MPHASIS MINDTREE BSOFT CYIENT LTI |
PHARMA: SUNPHARMA DRREDDY CIPLA LUPIN AUROPHARMA DIVISLAB ALKEM BIOCON GLENMARK
TORNTPHARM IPCALAB | FMCG: HINDUNILVR ITC BRITANNIA DABUR MARICO GODREJCP COLPAL EMAMILTD
TATACONSUM VBL | PVTBANK: HDFCBANK ICICIBANK KOTAKBANK AXISBANK INDUSINDBK FEDERALBNK CUB
RBLBANK IDFCFIRSTB BANDHANBNK | PSUBANK: SBIN BANKBARODA PNB CANBK BANKINDIA UNIONBANK
CENTRALBK IOB MAHABANK INDIANB | NBFC: BAJFINANCE CHOLAFIN SRTRANSFIN LICHSGFIN
MUTHOOTFIN MANAPPURAM PNBHOUSING CANFINHOME CREDITACC | AUTO: MARUTI TATAMOTORS
BAJAJ-AUTO HEROMOTOCO EICHERMOT ASHOKLEY TVSMOTOR ESCORTS APOLLOTYRE CEATLTD | METALS:
TATASTEEL JSWSTEEL HINDALCO VEDL SAIL NMDC JINDALSTEL NATIONALUM HINDZINC COALINDIA MOIL
| ENERGY: RELIANCE ONGC OIL GAIL IOC BPCL HINDPETRO PETRONET CASTROLIND IGL MGL (upstream
+ OMC mixed — crude sensitivities OPPOSITE within the basket, stated) | CAPGOODS: LT
SIEMENS ABB BHEL BEL CUMMINSIND THERMAX KEC NCC ASHOKA ADANIPORTS CONCOR | REALTY: DLF
GODREJPROP OBEROIRLTY PRESTIGE SOBHA BRIGADE PHOENIXLTD SUNTECK IBREALEST | CEMENT:
ULTRACEMCO ACC AMBUJACEM SHREECEM RAMCOCEM JKCEMENT DALBHARAT BIRLACORPN INDIACEM |
DURABLES: TITAN HAVELLS VOLTAS CROMPTON BLUESTARCO BATAINDIA PAGEIND RELAXO WHIRLPOOL
AMBER BAJAJELEC | UTILITIES: NTPC POWERGRID TATAPOWER CESC TORNTPOWER NHPC SJVN
ADANIPOWER JSWENERGY
CONVENTIONS: daily basket return = equal-weight mean of member returns; panel mean = mean
of all 487; REL = compounded (basket-minus-panel) daily series over the window (EN-D1a's
rel_curve machinery); UNAFFECTED = |cum REL| < 3pp per episode (|annualized REL diff| <
3pp for annual states). Episode windows fixed NOW (public-record dates): E1 TAPER
2013-05-22..2013-09-03 (currency); E2 DEMONETIZATION 2016-11-09..2017-01-31 (growth/cash
shock); E3 NBFC CRUNCH 2018-09-04..2019-02-07 (credit); E4 COVID CRASH
2020-02-20..2020-03-23 + E4b RECOVERY 2020-03-24..2020-12-31 (growth/crisis); E5 INR+OIL
SLIDE 2018-04-02..2018-10-09 (currency; overlaps E3 in Sep-Oct, stated); E6 EASING CYCLE
2019-02-07..2019-12-31 (rates). Annual states: WEAK-INR year = calendar dlog(INR/USD) >=
+5% (fx vault); RATE state = sign of annual change in IIMA RF.
CELLS (14):
**SEC-D1 — episode tables (7):** cum REL per sector for E1/E2/E3/E4/E4b/E5/E6; best/
worst/unaffected named per the 3pp rule. PRIORS: E1 best IT+PHARMA, worst REALTY/PSUBANK/
CAPGOODS/NBFC, FMCG unaffected; E2 worst REALTY/NBFC/DURABLES/AUTO, IT+PHARMA unaffected-
to-best; E3 worst NBFC+REALTY, PSUBANK negative, best IT/FMCG (flight to quality); E4
worst NBFC/PSUBANK/REALTY/METALS, best PHARMA+FMCG; E4b led by METALS/AUTO/REALTY (the
junk rally), PHARMA also STRONG (COVID demand — two-sided vs the junk-rally lag prior,
stated); E5 best IT, worst NBFC/AUTO, ENERGY two-sided (mixed basket); E6 TWO-SIDED for
NBFC/REALTY (cuts vs credit stress).
**SEC-D2 — the currency-sector map (3):** (i) per-sector annualized REL in WEAK-INR years
vs other years (the map); (ii) THE EXPORTER HEDGE BAR: (IT+PHARMA composite) REL
difference weak-minus-other >= +5pp/yr; (iii) next-year reversal: rank-corr across
sectors of weak-year REL vs next-calendar-year REL, averaged over weak years — prior:
NEGATIVE (reversal), two-sided lean.
**SEC-D3 — the rate-sector map (2):** (i) per-sector annualized REL in rising-RF vs
falling-RF years; (ii) THE LEVERAGED-TRIO BAR: (NBFC+REALTY+PSUBANK composite) REL
rising-minus-falling <= -3pp/yr; IT and FMCG |diff| < 3pp (rate-insensitive).
**SEC-D4 — credit-crunch specificity (2):** (i) THE FUNDING-SHOCK ORDERING through E3:
cum REL NBFC < PSUBANK < PVTBANK (a registered ordering bar on the E3 print); (ii) REALTY
cum REL <= -8pp in E3 (credit transmission).
CONSUMPTION: context for the India regime playbook (sector overlay), L14 (FII flows),
L20 (RBI cycle), the CU/CI battery doctrine; no promotion; descriptive strength only
(episodes n=7, years n=10). Script: scripts/analyze_sec_battery.py. Census: 14.

## Entry SEC-D5 (2026-09-07) — REGISTERED, UNRUN (data-gated; counts 0 until run): US
INDUSTRY x MACRO-STATE LONG-HISTORY BATTERY. Needs Ken French 12-industry monthly returns
1926- (value-weight; primary mba.tuck.dartmouth.edu egress-blocked; mirror hunt failed
2026-09-07 — principal-machine pull, runsheet row added). DESIGN, frozen now: JST-USA
macro states (inflation 2x2 level x direction as CI-D1; credit boom as CI-D3; debt >=90%
years as DB-D4; crisis years; broad-dollar terciles as CU-D7) x 12 industries; per-state
industry REL (vs equal-weight industry mean) annualized; named reads: the inflation-2x2
industry table, the crisis-year table, the debt-bucket table, the dollar-tercile table
(4 cells + grading vs the SEC-D1..D4 India priors). PRIORS frozen with the design: energy
+ materials best in HIGH+rising inflation; durables/retail worst; utilities hurt by
rising rates; banks worst in crisis years; staples least affected everywhere (the
"unaffected" seat). Census: 0 now; 4 on the day it runs.

| # | What | Result | Status |
|---|---|---|---|
| SEC-D1..D4 | The sector battery, India partial (interpretation hand-appended AFTER the print) | **SEC-D1 episodes** (cum REL, pp): **E1 TAPER**: IT +47.5 / PHARMA +22.4 best, PSUBANK -35.4 / PVTBANK -22.8 worst (prior nailed except PVTBANK's severity — banks generally, not just PSU, absorb the FII-outflow leg); FMCG +15.2 (registered "unaffected" missed pleasantly — defensives WIN taper windows). **E2 DEMONET**: worst REALTY -8.1 / CEMENT -7.8 (the cash-transaction chain, as registered) but best METALS +13.2 / UTILITIES +12.2 — CONFOUND STATED: demonetization landed the same week as the Trump global-reflation rally; the worst column is the domestic signal, the best column is the global confound. **E3 NBFC CRUNCH — THE SURVIVORSHIP ARTIFACT, flagged**: NBFC basket printed **+8.4** (basket holds only 2021 survivors — BAJFINANCE/gold financiers; DHFL, IBULHSGFIN, RELCAPITAL are structurally ABSENT from a survivor panel); the honest reads are PSUBANK -7.5, METALS -10.2 (global H2-2018 selloff overlay), PVTBANK +10.0 / PHARMA +10.1 (flight-to-quality within financials, as registered in direction). **E4 COVID CRASH**: worst NBFC -20.8 / PVTBANK -18.7 (moratorium fear), best PHARMA +27.9 / FMCG +18.2 (as registered); PSUBANK +0.4 — PRIOR MISS: already so cheap it fell WITH the panel, not worse. **E4b RECOVERY**: **IT +27.5 led (WFH boom — not in the prior)**, METALS +16.8 second (junk-rally leg confirmed); worst PSUBANK -27.1 / ENERGY -22.4 / UTILITIES -21.1; PHARMA -2.2 (the two-sided landed on the lag side). **E5 INR+OIL**: IT +36.1 / PHARMA +31.8 vs REALTY -17.4 / PSUBANK -17.0 / NBFC -15.2 / AUTO -12.7 (as registered); ENERGY -6.5 (two-sided, OMC drag edge). **E6 EASING**: REALTY +22.2 / NBFC +21.0 best (the two-sided lands on cuts-win, survivor caveat on NBFC), PSUBANK -23.7 / IT -17.2 worst. **SEC-D2 currency map** (weak-INR years 2013/2015/2018, REL diff weak-minus-other, pp/yr): IT **+34.6**, PHARMA +29.3, **FMCG +22.2**, AUTO +7.9, PVTBANK +7.1 || REALTY **-27.5**, CEMENT -20.1, PSUBANK -19.8, **METALS -16.5**, NBFC -10.1; (ii) EXPORTER HEDGE BAR: +31.9pp/yr (bar >=5 — 6x through); METALS on the LOSER side despite USD pricing — weak-INR years are global-risk-off years, the commodity leg loses more than the FX leg gains; (iii) reversal mean **-0.03** (-0.08/-0.19/+0.18) — NO systematic next-year reversal: weak-year sector moves are repricing, not overshoot (two-sided lean missed). **SEC-D3 rate map**: LEVERAGED TRIO rising-minus-falling **-8.1pp/yr (bar <=-3 PASS)**; but the rate-insensitivity bar **FAILED**: IT +12.2 / FMCG +7.2 in rising years — because rising-RF years (2012-14, 2018) ARE the weak-INR years (the L20 defense mechanism): **India's sector space collapses to ONE AXIS — domestic-leverage (REALTY/PSUBANK/NBFC/CEMENT/METALS) vs exporter-defensive (IT/PHARMA/FMCG) — activated jointly by INR-stress = rate-rising = credit-stress**; the two maps are one map. **SEC-D4**: (i) ordering NBFC < PSUBANK < PVTBANK **FAIL** as printed (+8.4 / -7.5 / +10.0) — attribution: survivorship (the basket cannot contain the casualties; stated as interpretation, the FAIL stands); (ii) REALTY E3 -1.8pp vs bar <=-8 **MISS** (survivor developers + realty already deflated pre-crunch) | **the one-axis doctrine is the headline; exporter hedge 6x its bar; E3/NBFC reads carry the survivorship flag permanently; 2 bars failed + 4 partials recorded honestly; SEC-D5 (US long history) data-gated on the runsheet; census +14 = 456** |

## Entry SEC-D6 (2026-09-07) — PRE-REGISTERED before running: THE CHARACTERISTIC
DECOMPOSITION of crisis safety. Principal hypothesis verbatim: "pharma i.e. export
oriented and pharma, fmcg i.e. durables / good free cash flow are safer in crisis.
perishable/ non-durable, non-cyclical cyclical and other check all." NOTE ON TERMS,
stated at registration: FMCG is the NON-durable (staples) basket; DURABLES is the
deferrable-goods basket — the hypothesis is re-stated as four separable axes to test.
Same panel/baskets/REL machinery as SEC-D1..D4 (survivorship and equal-weight limits
carry over verbatim). NO fundamentals are vaulted for India: the FCF leg is proxied by
sector-TYPICAL leverage scores declared here (a crude, stated proxy; the measured-FCF
form is data-gated — Damodaran runsheet row covers the US side only).
AXIS SCORES, fixed NOW (ordinal; from public sector knowledge, NOT from returns):
- EXPORT: IT 2, PHARMA 2, METALS 1 (global-priced, not exporter-margin), all others 0.
- CYCLICALITY (demand deferrability): FMCG/PHARMA/UTILITIES 0; IT/ENERGY 1; AUTO/
  DURABLES/CAPGOODS/METALS/CEMENT/REALTY/PVTBANK/PSUBANK/NBFC 2 (financials scored
  cyclical by construction).
- LEVERAGE (balance-sheet, sector-typical; the FCF proxy INVERTED): IT/FMCG/PHARMA/
  DURABLES 0; AUTO/CEMENT/ENERGY/CAPGOODS 1; METALS/REALTY/UTILITIES/PVTBANK/PSUBANK/
  NBFC 2.
- DURABILITY (product; GOODS sectors only, n=9 — services/financials/utilities/IT
  excluded as not-scorable, stated): FMCG 0, PHARMA 0, ENERGY 0; METALS 1, CEMENT 1;
  AUTO 2, DURABLES 2, CAPGOODS 2, REALTY 2.
STRESS COMPOSITE = mean cum REL across the four stress episodes E1/E3/E4/E5 (E2 excluded
as confounded per the SEC-D1 print; E4b/E6 are non-stress). n=14 sectors (9 for
durability) — descriptive strength only, flagged.
CELLS (10):
c1 (4): Spearman rank-corr of the stress composite vs each axis score. PRIORS: LEVERAGE
  the strongest, <= -0.6 (the principal's FCF intuition, carried by the balance-sheet
  side); CYCLICALITY second, -0.4..-0.6; EXPORT positive but WEAKER (+0.3..+0.5 — FMCG
  is domestic yet safe, so export cannot be the primary axis); DURABILITY NEGATIVE — the
  hypothesis's durability leg INVERTED as registered: NON-durable (non-deferrable
  demand) is the safe side, durable goods are the deferrable side.
c2 (4): clean pairwise contrasts on the stress composite (pp): (i) FMCG - DURABLES > 0
  (non-cyclicality effect, leverage held ~equal); (ii) IT - FMCG TWO-SIDED (export hedge
  vs domestic defensive — both crisis-safe for different reasons); (iii) IT - METALS >=
  +15 (global-priced + leveraged is NOT export-safe); (iv) FMCG - UTILITIES > 0 (the
  leverage penalty with cyclicality held at 0).
c3 (1): the same four axis rank-corrs on E4b RECOVERY — TWO-SIDED lean: signs flip
  (stress axes become recovery fuel), imperfectly (the E4b IT-led print is known).
c4 (1): THE SAFEST-SEAT TABLE: per-sector WORST single stress-episode cum REL; named
  list of sectors whose worst episode >= -5pp. PRIOR: FMCG, PHARMA qualify; IT fails on
  no episode but E6 is non-stress (two-sided whether IT qualifies); NO leverage-2 sector
  qualifies.
CONSUMPTION: the India playbook sector overlay (the "what buys safety" line) + frames
SEC-D5's US graded rerun; no promotion. Script: scripts/analyze_sec_d6.py. Census: 10.

| # | What | Result | Status |
|---|---|---|---|
| SEC-D6 | The characteristic decomposition of crisis safety (interpretation hand-appended AFTER the print; RUN NOTE: the script imports analyze_sec_battery for its baskets/REL machinery, which re-echoes the booked SEC-D1..D4 prints verbatim — an echo, not new cells) | **c1 rank-corr(stress composite, axis)**: LEVERAGE **-0.75** (bar <=-0.6 PASS — the strongest, by 0.01); CYCLICALITY **-0.74** (registered band -0.4..-0.6 EXCEEDED — stronger than registered, pleasant partial miss; at n=14 leverage and cyclicality are a statistical TIE and heavily co-scored on financials — stated); EXPORT **+0.57** (a hair above the +0.3..+0.5 band; the registered ordering claim HOLDS: export is real but secondary); DURABILITY **-0.73** (n=9) — the inversion registered CONFIRMED: NON-durable/perishable demand (non-deferrable) is the SAFE side. **c2 contrasts** (stress composite, pp): FMCG-DURABLES **+7.5** (non-cyclicality effect, PASS); IT-FMCG **+11.0** (the two-sided lands: export adds on TOP of defensive); IT-METALS **+24.1** (bar >=15 PASS — global-priced+leveraged is NOT export-safe); FMCG-UTILITIES **+10.0** (the leverage penalty with cyclicality held at 0, PASS). **c3 recovery corrs**: CYCLICALITY +0.28 and DURABILITY +0.43 flip as leaned; EXPORT **+0.52 does NOT flip** (IT led E4b); **LEVERAGE +0.05 — flips to ZERO, not positive: leverage costs -0.75 in stress and pays NOTHING in recovery — NEGATIVE CONVEXITY, the sharpest new fact in the entry**. **c4 safest seats** (worst stress episode >= -5pp): **PHARMA +10.1, IT +7.5, FMCG +5.2, DURABLES +2.9** — DURABLES qualifying was NOT in the prior (pleasant miss: zero-leverage discretionary never got hit inside a stress window); NO leverage-2 sector qualifies (best of them UTILITIES -9.4) — as registered. Worst-episode tail: PSUBANK -35.4, PVTBANK -22.8, REALTY -21.2, NBFC -20.8. THE HYPOTHESIS VERDICT: the principal's FCF leg is the PRIMARY axis (via the leverage proxy); export is real but secondary and conditional on a clean balance sheet; the durability leg runs INVERTED (non-durable safer); the safest quadrant = zero leverage x non-deferrable demand, with export as the bonus | **crisis safety is bought by the BALANCE SHEET first, the demand curve second, the revenue currency third; leverage shows negative convexity (hurts in stress, unpaid in recovery); proxy-not-measured-FCF limit stands; census +10 = 466** |

## Entry SEC-D7 (2026-09-07) — PRE-REGISTERED before running: STOCK-LEVEL LEVERAGE
DECOMPOSITION. Principal directive verbatim: "check the high financial leverage and low
financial leverage, high debt low debt, high operating leverage low operating leverage
stocks impacts on all very detailed." No fundamentals are vaulted, so three legs, limits
stated: (a) MEASURED beta/vol quintile sorts (Modigliani-Miller: equity beta scales with
D/E, so a beta sort is a joint leverage x business-risk sort — stated; T4's India low-vol
print is the unconditional parent, cited; these cells are the STATE-CONDITIONAL
increment); (b) DECLARED financial-leverage name lists (public-knowledge provenance,
EN-D1a precedent; NON-FINANCIALS only — banks/NBFC excluded, their leverage is the
business); (c) DECLARED operating-leverage lists (fixed-cost businesses vs variable-cost).
Panel/REL conventions as SEC-D1..D6 (equal weight; REL = compounded basket-minus-panel;
stress composite = mean cum REL over E1/E3/E4/E5; survivorship one-way limits verbatim).
THE CEMETERY CENSUS, known at registration: 9/28 declared HIGH-FL names are ABSENT from
the survivor panel (JPASSOCIAT SUZLON RCOM RELINFRA RPOWER UNITECH HCC JETAIRWAYS GVKPIL
— the decade's leverage casualties, most near-total equity losses) vs 1/25 LOW-FL
(ABBOTINDIA, an index-membership absence, not a death) — so every HIGH-FL damage print is
a LOWER BOUND on true damage; the absence-rate asymmetry is itself booked as b0.
LISTS fixed NOW (present-in-panel members only):
HIGH-FL (19): GMRINFRA ADANIPOWER ADANIENT DLF JSWENERGY TATAPOWER TATASTEEL JSWSTEEL
JINDALSTEL VEDL BHARTIARTL IDEA TATAMOTORS SAIL ASHOKLEY LEMONTREE INDHOTEL ADANIGREEN
IRB. LOW-FL/NET-CASH (24): TCS INFY WIPRO HCLTECH ITC HINDUNILVR COLPAL CASTROLIND
PAGEIND PIDILITIND ASIANPAINT BERGEPAINT DABUR MARICO BAJAJ-AUTO HEROMOTOCO EICHERMOT
DIVISLAB AKZOINDIA GILLETTE 3MINDIA HONAUT OFSS MPHASIS. HIGH-OL (17): INDHOTEL LEMONTREE
EIHOTEL INDIGO PVR ULTRACEMCO ACC AMBUJACEM SHREECEM TATASTEEL JSWSTEEL SAIL JINDALSTEL
TATAMOTORS ASHOKLEY BHEL MHRIL. LOW-OL (18): TCS INFY WIPRO HCLTECH TECHM MPHASIS
HINDUNILVR ITC DABUR MARICO GODREJCP BRITANNIA PIDILITIND ASIANPAINT BERGEPAINT COLPAL
EMAMILTD JYOTHYLAB. OVERLAP STATED: steel/auto/hotels sit in BOTH high lists (high on
both axes in reality); the convexity-contrast cell (c4) is the discriminator.
QUINTILE MACHINERY: per calendar year y in 2013-2021, per-stock beta (vs panel mean) and
total vol computed on year y-1 daily returns (>=150 obs), quintiles formed at Dec 31 and
HELD through year y (no lookahead); equal-weight quintile portfolios; Q5 = highest.
Annual-state reads on quintiles use 2013-2021 only (2012 has no assignment — stated);
weak-INR years within that span: 2013/2015/2018; rising-RF: 2013/2014/2018.
CELLS (22):
**D7a measured (10):** for BETA quintiles and VOL quintiles separately: a1/a6 full-period
CAGR ladder (abs, %/yr) — PRIOR: Q5 does NOT out-earn Q1 (T4/low-vol, two-sided on exact
ordering); a2/a7 stress-composite ladder — PRIOR: monotone negative, Q5-Q1 <= -10pp;
a3/a8 E4b recovery ladder — PRIOR: partial inversion (Q5 bounces); a4/a9 weak-INR annual
REL diff ladder — PRIOR: monotone against high quintiles; a5/a10 rising-RF diff ladder —
PRIOR: same direction, weaker.
**D7b declared FL (7):** b0 the cemetery census (booked from the registration counts);
b1 full-period CAGR HIGH vs LOW — PRIOR: LOW wins by >= 5pp/yr (the twin-balance-sheet
decade); b2 stress composite spread — BAR: HIGH-LOW <= -10pp; b3 per-episode REL table
(both baskets, all 7 windows) — PRIOR: HIGH-FL negative in ALL four stress windows, E6
easing its best window; b4 THE CONVEXITY TEST at stock level: HIGH-FL E4b recovery gain
< |its stress-composite loss| (registered directly this time); b5 weak-INR annual diff —
PRIOR: HIGH hit hardest (FX+funding); b6 rising-RF annual diff — PRIOR: negative for HIGH.
**D7c declared OL (5):** c1 full-period CAGR HIGH-OL vs LOW-OL — TWO-SIDED; c2 stress
composite spread — PRIOR: negative but SMALLER than the FL spread (b2); c3 recovery
spread — PRIOR: HIGH-OL bounce POSITIVE and larger than FL's; c4 THE CONVEXITY CONTRAST
(the entry's registered claim): (E4b gain + stress-composite loss) >= 0 for HIGH-OL while
< 0 for HIGH-FL — OPERATING leverage is a symmetric two-way amplifier, FINANCIAL leverage
an asymmetric one-way tax; c5 weak-INR diff — PRIOR: HIGH-OL negative, milder than FL.
CONSUMPTION: the playbook leverage/safety addendum (stock-selection line) + Track P label
features; no promotion; descriptive strength (10y, survivor panel). Script:
scripts/analyze_sec_d7.py. Census: 22.

| # | What | Result | Status |
|---|---|---|---|
| SEC-D7 | Stock-level leverage decomposition (interpretation hand-appended AFTER the print; import re-echo run note as SEC-D6) | **D7a BETA quintiles**: stress composite MONOTONE +9.8/+4.4/+2.6/-4.5/**-10.5** (Q5-Q1 -20.3pp, bar <=-10 PASS); E4b recovery FULLY inverts (-10.2 -> +16.2, stronger than the registered partial); weak-INR ladder monotone against high beta (+10.2 -> -8.9); rising-RF same with a Q3 wobble; full CAGR Q1 27.4 vs Q5 **23.1** — beta paid NOTHING for its stress cost (T4's parent read consistent). **VOL quintiles**: stress/recovery ladders as beta (Q5-Q1 -12.8 PASS; inversion holds) BUT full CAGR is MONOTONE UP **22.2 -> 32.6%/yr — PRIOR MISS, flagged as THE survivorship-concentrated cell**: volatile losers get deleted from a survivor panel, volatile winners remain — the a6 ladder is where the bias maximizes and is NOT evidence against low-vol (T4 one-way design governs); a9 broken monotonicity at Q5 (-0.3) and a10 non-monotone — 2 misses booked. **D7b DECLARED FL** (non-financials; b0 cemetery: 9/28 HIGH-FL declared names ABSENT vs 1/25 LOW-FL — 32% vs 4%): b1 full CAGR LOW 25.9 vs HIGH 21.7 = **+4.2pp/yr** (bar >=5 MISSED by 0.8 — and a LOWER BOUND, the cemetery uncounted); b2 stress spread HIGH-LOW **-23.9pp** (bar <=-10 PASS, 2.4x); b3 HIGH-FL negative in 3 of 4 stress windows (E5 +0.6 — the metals leg; partial miss) and its best window is **E4b +34.6**, not E6 (+10.5) — registered E6-best MISSED; b4 **THE STOCK-LEVEL CONVEXITY TEST FAILS AS REGISTERED**: recovery +34.6 > |stress -7.2| — surviving leveraged non-financials DID get the recovery payoff; b5 weak-INR HIGH -16.9 vs LOW **+21.6** (a 38.5pp state spread — the widest single print in the SEC series); b6 rising-RF HIGH -20.0 (as registered). **D7c DECLARED OL**: c1 full CAGR HIGH-OL **17.8** vs LOW-OL **28.3%/yr** (-10.5pp/yr — the two-sided lands hard: fixed-cost businesses were the decade's structural losers); c2 stress spread -22.6pp (registered "smaller than FL's -23.9" holds by 1.3pp — effectively EQUAL, the shared steel/auto/hotel members stated); c3 HIGH-OL recovery +4.8 — positive but FL bounced 7x harder (registered "OL bounce larger" MISSED); c4 **THE CONVEXITY CONTRAST INVERTED**: OL sum +1.1 (>=0 as registered) but FL sum **+27.4**, not <0 — the registered "FL = one-way tax" FAILS at stock level; c5 weak-INR +1.4 (sign miss). RECONCILIATION (interpretation): the sector print (leverage unpaid in recovery, +0.05) was carried by leveraged FINANCIALS (PSU banks -27.1 in E4b); the stock list here EXCLUDES financials by design — leveraged NON-financial survivors behave as CALL OPTIONS (torqued equity stubs: -24pp stress spread, +34.6 bounce), and the cemetery (9 dead names, most ~total losses) is the unexercised side of the same option. Unconditionally (dead included) the one-way-tax read likely survives; conditionally (survivors) leverage is a lottery that paid. LEVERAGE TAXONOMY BOOKED: leveraged financials = negative convexity; leveraged non-financials = binary call (cemetery or bounce); operating leverage = symmetric-mild but a -10.5pp/yr structural CAGR drag; zero-leverage + variable-cost (LOW-OL: 28.3%/yr AND +19.0 stress AND +31.0 weak-INR) = best in calm AND crisis in this panel — with its own composition flag (IT+FMCG-heavy) | **8 misses/partials + 1 registered-claim inversion booked; the cemetery census (32% vs 4%) is the loudest number; vol-CAGR cell survivorship-flagged permanently; census +22 = 488** |

## Entry CM-D1..D6 (2026-09-07) — PRE-REGISTERED before running: THE COMMODITY BATTERY
(oil, gold, silver, copper + the cross-section). Principal directive: "lets move to
commodity now tell me everything... oil, gold silver copper and more." BOOKED PRINTS ARE
CITED, NOT RE-RUN: CS1-4 (supercycle troughs 15-21y median 18y; breadth PASS +0.30/89%;
capacity links FAIL both ways); KJ1 (no 3-4y commodity clock); GF1-3 (global factor
+0.28 pre-1990 -> +0.77 post; India loading +0.57; down-year breadth 69%); OL-D1a PASS
(Kilian decomposition: demand-driven oil != supply-driven oil for equities); H53a + OL-D2a
FAIL unconditionally (commodity->India links are OWNED by the global factor;
conditional-only framings LOCKED); L8 golden constant (gold ~0 real drift, centuries);
CI-D2 (gold-local +9.6%/yr real in HIGH+rising inflation years, the killer-cell winner);
CU-D4/D5 (gold-local +8.2pp median crash-year spread; gold-INR +19.9%/yr in the 5 worst
INR years); DB-D6 h6 / DB-D8 (gold +4.6% in >=90%-debt years; Japan-carry gold +6.3 beat
everything); T2/T3 (Kilian trend-on-states; NIFTY/gold dual momentum). DATA: Jacks
1850-2015 ANNUAL REAL indices (1900=100, US-CPI-deflated — 42 commodities incl Petroleum/
Gold/Silver/Copper; authenticated A1-A5); IMF PCPS monthly 1980-2017 (wide, nominal);
WTI monthly 1986-2026; JST USA (CPI regime, rgdpmad) and the JST panel broad dollar
(CU-D7 construction, panel-mean dlog xrusd, strong >= +5% / weak <= -5%); INR fx vault.
Conventions: real log changes on Jacks (already real — a real change IS the real hedge
read); expanding percentiles min_obs=20; Spearman; overlap flagged; sample ends 2015/2017
for Jacks/IMF — "today" reads are NOT available from the vault (stated).
CELLS (15):
**CM-D1 — the century table (2):** d1 real price CAGR 1900-2015 for Petroleum, Gold,
Silver, Copper (PRIORS: oil the only clearly positive; gold ~0 [L8]; silver < gold;
copper <= 0 — extraction tech deflates metals); d2 group medians (energy/metals/agri) —
PRIOR: agri most negative (Prebisch-Singer), energy positive, metals ~0-negative.
**CM-D2 — the inflation-hedge table (4):** US 2x2 regime (own-history CPI pct >= 0.8 x
rising/falling, the CI-D1 construction on JST USA), mean SAME-YEAR REAL price change per
cell for oil / gold / silver / copper (1 cell each). PRIORS: all four positive in
HIGH+rising; OIL strongest (oil IS 1970s inflation); gold second; silver = high-beta gold;
copper weakest (demand-cyclical offset). The commodity complement of CI-D2's asset table.
**CM-D3 — dollar & growth states (3):** d1 strong-USD years (>= +5%) vs weak (<= -5%):
median real change across the 4 commodities + all-42 median — PRIOR: negative in strong-
USD years, positive in weak (the inverse-dollar law); d2 Dr. Copper PREDICTIVE:
copper/gold ratio log change_t -> US real GDP/cap growth_{t+1} Spearman — PRIOR: +0.1..
+0.3 (weak); d3 Dr. Copper COINCIDENT (same-year) — PRIOR: stronger than d2 (copper reads
the present, not the future).
**CM-D4 — ratio structure (3):** d1 gold/silver ratio expanding percentile -> next-5y
(silver minus gold) real return — PRIOR: mean reversion, rho >= +0.3 (high ratio = silver
cheap -> silver outperforms); d2 oil/gold ratio percentile -> next-5y (oil minus gold) —
TWO-SIDED (era-shifted market structure); d3 descriptive: the 2015 endpoint percentile of
both ratios vs their own history (context only).
**CM-D5 — cross-sectional momentum, spot-only (2):** IMF PCPS monthly 1980-2017,
individual commodity columns (>=15 series with 12m history), 12-1 momentum, monthly
rebalance, EW top tercile minus bottom tercile. STATED LIMIT: price indices = SPOT
momentum (no futures roll/carry — the tradeable form needs futures data, runsheet-free
note only). d1 annualized L/S mean return — PRIOR: positive +2..6%/yr (Miffre-Rallis);
d2 worst rolling 12m of the L/S — PRIOR: <= -15% (momentum crashes exist here too).
**CM-D6 — the oil->INR channel (1):** WTI annual change vs same-year INR depreciation,
1987-2025 — PRIOR: positive +0.2..+0.4 (the import-bill channel; India imports ~85% of
its crude). Complements the LOCKED H53a verdict (equity link dead; the FX link is the
one being tested).
CONSUMPTION: gold book (L8) + supercycle (L14) + Kilian (L25) context refresh; the
inflation-hedge table feeds the CI-D2 asset ranking; no promotion. Script:
scripts/analyze_cm_battery.py. Census: 15.

## Entry CM-D2b (2026-09-07) — PRE-REGISTERED before running: the floating-era split of
the CM-D2 gold cell. The CM-D2 print (booked below) shows gold at only +0.7%/yr in US
HIGH+rising years — but 29 such years include the pre-1971 FIXED-gold-price era where the
real gold price mechanically FALLS in inflation years. CELL (1): gold same-year real
change in US HIGH+rising years, 1972-2015 only, vs the fixed-era (pre-1972) same cell.
PRIOR: floating-era gold in HIGH+rising >= +5%/yr; fixed-era negative (the confound made
visible). Script: same, param rerun. Census: 1.

| # | What | Result | Status |
|---|---|---|---|
| CM-D1..D6 | The commodity battery (interpretation hand-appended AFTER the print) | **CM-D1 the century table** (real CAGR 1900-2015): Petroleum **+0.96%/yr** (the only clear positive, as registered), Gold +0.57 (a shade above the L8 ~0 prior — the 2011-13 endpoint; partial), Silver **-0.16** < gold (as registered), Copper **-0.52** (as registered — extraction tech deflates metals); groups: agri **-1.08%/yr median** (Prebisch-Singer confirmed), energy +0.40, metals -0.11. Commodities are NOT buy-and-hold assets; only energy carried a century premium. **CM-D2 the inflation-hedge 2x2** (same-yr REAL change, US regime): HIGH+rising: oil **+13.1** / copper +4.0 / silver +1.9 / gold +0.7 — all four positive (bar PASS), oil strongest (as registered) BUT **ordering MISS: gold printed WEAKEST** — resolved by CM-D2b (below): the 29 HIGH+rising years mix the fixed-gold era; HIGH+falling: **everything crashes** (oil -1.2, gold -6.2, silver -10.5, copper **-14.8**) — commodities are the MIRROR of CI-D2's financial assets: they pay when paper burns and burn when paper pays (disinflation is the commodity graveyard); low+falling oil -8.7. **CM-D3**: d1 the dollar law crisp — strong-USD years big4 **-5.0%** / all-42 median -4.0 vs weak-USD **+8.5 / +4.8** (as registered); d2 **Dr. Copper PREDICTIVE IS DEAD: +0.01** (prior +0.1..+0.3 MISS) — copper/gold forecasts nothing; d3 coincident +0.33 (as registered: copper reads the present, never the future). **CM-D4 ratios**: gold/silver pct -> next-5y silver-minus-gold rho **+0.14** (bar >=+0.3 MISS — only weak reversion; silver is NOT a reliable cheapness trade on the ratio); oil/gold +0.37 (two-sided lands: high oil/gold -> gold outperforms next 5y); 2015 endpoints: gold/silver pct 0.87 (silver historically cheap), oil/gold 0.38. **CM-D5 spot momentum**: +1.4%/yr, Sharpe-shape 0.12 (prior +2..6 **MISS** — spot-index momentum is ~nothing; the documented commodity-momentum premium lives in FUTURES carry/roll, which this vault cannot see — stated); worst 12m **-33.2%** (Oct-1991; crash bar pass). **CM-D6 oil->INR: SIGN MISS, the best print in the entry: -0.44** (registered +0.2..+0.4) — oil-UP years are INR-STRONG years: the global demand/risk factor (Kilian demand leg + Rey flows) swamps the import-bill channel; oil crashes are risk-off years that sink INR too. The LOCKED H53a doctrine ("the global factor owns commodity links") now extends to the FX channel | **5 misses booked honestly; the inflation 2x2 completes CI-D2's asset table from the commodity side; Dr. Copper predictive dead; import-bill intuition inverted by the global factor; census +15 = 503** |
| CM-D2b | Floating-era split of the gold inflation cell | US HIGH+rising years: floating era (1973/74/77/78/79/80, n=6) gold real **+24.9%/yr** vs fixed era (n=23) **-5.6%/yr** — both registered signs PASS (bar >=+5 cleared 5x). The CM-D2 ordering miss is fully explained: post-1971, gold is the SECOND-strongest inflation-acceleration hedge after oil (+24.9 vs +13.1), and the pooled +0.7 was a regime mix. Standing caveat: n=6, all from ONE arc (the 1970s) — one episode, not a law | **the fixed-era confound made visible and booked; gold's hedge rank restored conditional on a floating regime; census +1 = 504** |

## Entry MG-D1..D4 (2026-09-07) — PRE-REGISTERED before running: THE MACRO GAP-CLOSER
(yield curve, twin deficits, rare-disaster census, demographics/fiscal). Principal
directive: "move to next i think macro and global everything is covered if anything left
tell me." Gap audit against the register: the TERM SPREAD appears only as an ER-D6
kitchen-sink factor (never its own battery); JST's ca, pop, revenue/expenditure columns
are untested; no drawdown census exists. JST R6, 1950-2020 unless stated; conventions as
the prior batteries (real returns, expanding percentiles min_obs=20, Spearman, overlap
flagged); slope = ltrate - stir (pp); ca/gdp; fiscal balance = (revenue-expenditure)/gdp;
pop growth = trailing-10y mean dlog pop. CELLS (13):
**MG-D1 — the yield curve (4):** d1 pooled corr(slope_t, real GDP/cap growth_t+1) —
PRIOR +0.1..+0.3 (the classic, diluted pooled); d2 INVERTED years (slope<0): next-1y
growth and negative-growth frequency vs normal years — PRIOR: growth lower by >=1pp,
recession freq ~2x; d3 slope -> next-1y REAL EQUITY — PRIOR: WEAK (+0.05..+0.15) — THE
DOCTRINE TEST: the curve predicts growth and growth does not price equities (GDP-D1), so
a strong d3 would be a doctrine anomaly; d4 inverted years -> next-1y real BOND — PRIOR:
positive (inversion = tight money -> subsequent disinflation pays duration).
**MG-D2 — twin deficits (4):** d1 worst-CAD state (ca/gdp own pct <= 0.2) -> next-1y
depreciation vs USD (non-US) — PRIOR: positive, modest (deficits leak currency); d2 same
state -> next-1y local real equity — TWO-SIDED (boom-in-progress vs sudden-stop); d3
pooled corr(ca/gdp, SAME-year real equity) — PRIOR: -0.05..-0.2 (deficit years are boom
years); d4 the sign census: fraction of countries whose own-history corr(d1 state,
depreciation) is positive — PRIOR: >= 60%. India is NOT in JST — the 2013 CAD episode is
cited from CU-D7/SEC-D1 prints, stated.
**MG-D3 — the rare-disaster census (3), full span:** d1 per-country WORST real-equity
drawdown (log real TR index, peak-to-trough) + recovery years (trough back to prior
peak; ">span" if never) — descriptive table; d2 medians across countries — PRIOR: median
worst drawdown >= 60%, median recovery >= 10y (Barro/DMS); d3 the same for HOUSING —
PRIOR: shallower (median <= 40%) but recovery NOT faster than equities (the slow-asset
doctrine, DB-D7/CI-D4).
**MG-D4 — demographics-lite + fiscal (2):** d1 trailing-10y pop growth -> next-10y real
equity, pooled — TWO-SIDED, lean negative (the dilution/growth doctrine extends to
demographic growth; the M/O age-structure form is DATA-GATED — no age pyramids vaulted,
stated); d2 fiscal-balance percentile -> next-5y real equity AND real bond — PRIOR: |rho|
<= 0.15 both (the levels-don't-price doctrine; misses recorded if breached).
CONSUMPTION: closes the macro sweep; L18 (business cycle) + L20 context; the disaster
census feeds the risk chapter of the India playbook; no promotion. Script:
scripts/analyze_mg_battery.py. Census: 13.

| # | What | Result | Status |
|---|---|---|---|
| MG-D1..D4 | The macro gap-closer (interpretation hand-appended AFTER the print) | **D1 YIELD CURVE**: d1 slope -> next-1y growth **+0.12** (in band, low end — the classic dilutes badly at panel breadth); d2 inverted years: negative-growth freq **21% vs 13%** (1.6x, near the ~2x prior) BUT mean growth only -0.3pp lower (bar >=1pp **MISS**) — inversion is a pooled RECESSION-ODDS signal, not a mean-growth signal; d3 slope -> next-1y equity **+0.06 — THE DOCTRINE TEST PASSES**: the curve predicts growth and growth does not price equities (GDP-D1 doctrine held where it could have broken); d4 bonds after inversion +2.5 vs +2.9% — **MISS**: no pooled duration edge from inversion (rate-control eras dilute the US intuition). **D2 TWIN DEFICITS**: d1 worst-CAD years -> next-1y depreciation **+2.5% vs -0.5%** (as registered) and d4 sign census **10/14 countries** (bar 60% pass); d2 the two-sided lands SUDDEN-STOP: next-1y equity after worst-CAD years **+4.1% vs +9.5%** — a -5.4pp state (the 2013 India CAD episode, CU-D7/SEC-D1, is the same physics); d3 corr(ca/gdp, same-yr equity) **+0.17 — SIGN MISS** (registered negative): external-strength years ARE good equity years — the "deficits are booms" intuition is wrong in this panel. **D3 THE RARE-DISASTER CENSUS** (full span, real TR): median worst equity drawdown **-78%**, median recovery **18 YEARS** (bars pass); the tail: France -98% (1977 trough, NEVER re-peaked in span), Germany -98% (1948, 37y), Portugal -98% (1984, >span), Japan -94% (1948, 24y), Italy -86%/37y; the USA — source of most investing folklore — had the SHALLOWEST major disaster (-52%, 1932, 7y recovery): US-based intuition is survivor-country intuition. HOUSING: median worst **-29%**, recovery **10y** — shallower AND faster than equities at the disaster scale (registered "not faster" **MISS**: the slow-asset doctrine holds for busts, not for century-scale disasters — housing never has a -78% real event; Belgium/Finland WWI-era -77/-73% are the war exceptions). **D4**: d1 pop growth -> next-10y equity **-0.17** — the dilution doctrine EXTENDS TO DEMOGRAPHICS (population growth buys no equity return; lean confirmed); d2 fiscal-balance pct -> equity -0.15 (at the bar exactly, levels-doctrine holds) but -> bonds **-0.24 — MISS**: fiscal SURPLUS percentile predicts WORSE bond returns — surpluses come in booms with rising rates, deficits precede disinflation/easing (busts) which pays duration; a state fact, not a signal | **the macro sweep is CLOSED: 4 misses booked (inversion mean-growth, inversion bonds, CA same-year sign, housing-recovery); the doctrine survived its yield-curve test; the disaster census is the risk chapter's anchor table; census +13 = 517** |

## Entry TL-D1 (2026-09-07) — PRE-REGISTERED before running: THE RETURN-DISTRIBUTION
ATLAS (tails, sigma events, volatility clustering, horizon distributions). Principal
directive: daily returns, tail analysis both ends, 1/2/3/6-sigma points, volatility
distribution and clustering, and D/W/M/Y/3y/5y/10y/20y distributions with graphs, for
"Dow 100y+ and S&P 50y+". DATA CORRECTION, stated first: NO US daily index series is
vaulted or free-reachable from this container (Dow daily probes dead; runsheet row added
below). The runnable set: NEW VAULT us_index/sp500_shiller_monthly_1871.csv (Shiller
mirror, monthly 1871-01..2026-08, 6/6 anchors passed; monthly prices are AVERAGES — 1m
reads flagged, >=1y unaffected); NIFTY50 daily 2007-2026 (the true-daily specimen, our
own market); CBOE VIX daily 1990-2026 (the vol distribution measured directly); JST USA
annual 1872-2020 real TR (the 150y cross-check). US real total return from Shiller:
(RealPrice_t + RealDividend_t/12)/RealPrice_{t-1}. Sigma = full-sample sd of the series
in question (stated; a rolling-sigma variant is a different design). Descriptive entry
with SHAPE BARS (demonstrations count; consumed looks):
c1 DAILY SIGMA TABLE (NIFTY): counts beyond +-1/2/3/4/6 sigma vs Gaussian expectation —
   BARS: |z|>=3 count >= 3x Gaussian; at least one event beyond 6 sigma in 4,700 days
   (Gaussian expectation ~1e-5 events).
c2 DAILY SHAPE (NIFTY): excess kurtosis >= 5; skew negative (two-sided lean).
c3 CLUSTERING (NIFTY): autocorr(|r|) positive at EVERY lag 1..30; AR(1) phi of rolling
   21d vol >= 0.95 (half-life >= ~13 trading days).
c4 VIX DISTRIBUTION: median in [15,20]; right-skewed (mean > median); max > 80.
c5 THE KURTOSIS LADDER (aggregational gaussianity): excess kurtosis monotone down from
   daily -> weekly -> monthly -> annual; annual (JST US real) |excess kurtosis| <= 2.
c6 US HORIZON TABLE (Shiller real TR, rolling windows M/1y/3y/5y/10y/20y + JST annual
   cross-check): positive-fraction ladder MONOTONE RISING with horizon (prior ~60% 1m ->
   ~95-100% 20y); worst 20y real CAGR in [-1.5%, +1.5%] (the classic near-zero floor);
   overlap flagged everywhere.
c7 NIFTY WEEKLY/MONTHLY shape reads (nominal; the same table one and two aggregation
   steps up).
c8 THE EVENT LISTS (descriptive): worst/best 10 days (NIFTY), worst/best months and
   years (US real), deepest US real drawdowns with recovery years.
CONSUMPTION: the risk chapter (with MG-D3's disaster census), L2 fast-stress context,
and the published atlas artifact (preservation rule #5: artifact + committed copy).
Script: scripts/analyze_tl_atlas.py. Census: 8.

| # | What | Result | Status |
|---|---|---|---|
| TL-D1 | The return-distribution atlas (interpretation hand-appended AFTER the print; RUN NOTES: VIX column-name fix pre-print; Shiller mirror's real columns end 2023-09 — completeness guard added after a -100% artifact appeared in a first print, series truncated, no bar touched) | **c1 THE SIGMA LEDGER** (NIFTY daily, n=4,553, sigma=1.30%): +-3sigma observed 69 vs Gaussian 12.3 (**5.6x**, bar >=3x PASS); +-4sigma 35 vs 0.29 (121x); **beyond 6sigma: 6 events** (4 down, 2 up) vs Gaussian ~1e-5 (**~700,000x**, bar >=1 PASS). **c2**: excess kurtosis **15.8** (bar >=5 PASS); skew **+0.06 — the negative lean MISSED**: at daily frequency the up-tail is as fat as the down-tail (best day +17.7% > |worst| 13.0%); the felt asymmetry is vol-timing, not skew. **c3 CLUSTERING**: autocorr(|r|) positive at all 30 lags (+0.28 lag-1, +0.18 lag-30) vs autocorr(r) lag-1 +0.04 — size echoes, sign does not; rolling-vol AR(1) phi **0.992 -> 82-trading-day half-life** (bar PASS); 21d vol regime range 7.8% -> 87.9% (6.1x median-to-max). **c4 VIX**: median 17.6 (in band), mean 19.4 > median (right skew PASS), max 82.7 on 2020-03-16 (>80 PASS). **c5 THE KURTOSIS LADDER**: NIFTY daily 15.8 -> weekly 4.6 -> monthly 4.3 -> US annual **0.2** (monotone within-market, annual bar PASS) — **PARTIAL**: US monthly over 152y prints **18.0** (the 1930s never aggregate away; averaging flag stated) — aggregational gaussianity holds within eras, not across a Depression. **c6 US HORIZON TABLE** (Shiller real TR 1871-2023, overlap flagged): 1y mean +8.6/sd 19.3/worst -58.1; 5y +7.2/7.8/-13.2; 10y +6.9/5.1/-5.9; 20y +6.6/**2.9**/**-0.2, 100% of 1,593 windows positive** — positive-fraction ladder 61->69->78->81->89->100% MONOTONE (PASS); worst 20y -0.2%/yr in the [-1.5,+1.5] band (PASS; JST annual cross-check +0.9%). **c7** NIFTY weekly sd 2.7%/worst -15.9%; monthly 6.0%/-26.4%. **c8 EVENTS**: all 20 extreme NIFTY days sit inside 2008 / the 2009 reopen / Mar-2020; worst US real years 2008 -39, 1917 -37, 1931 -36, 1974 -34; deepest US real drawdown **-77% (Jun-1932)**. NEW VAULT us_index/ (Shiller mirror, 6/6 anchors); Dow daily runsheet row added. ARTIFACT: docs/learn/artifacts/return-distribution-atlas.html (published 292e6690) | **2 bars missed honestly (daily skew; the ladder's US-monthly exception); the atlas is the risk chapter's second anchor with MG-D3; census +8 = 525** |

## Entry TL-D2 (2026-09-07) — PRE-REGISTERED before running: THE ATLAS EXTENSION — S&P at
maximum span, the US market at 99y monthly, and SMALL vs LARGE on both markets. Principal
directive verbatim: "i told u to do it for sp500 and dow jones max possible lets keep the
current nifty but i want it for the mentioned and smallcaps and indian smallcaps if
possible seperately." DATA REALITY restated: US DAILY (Dow 1896-/SPX 1957-) remains
principal-machine (stooq re-probed dead 2026-09-07; runsheet row stands) — the maximum
RUNNABLE spans are: S&P NOMINAL MONTHLY 1871-01..2026-08 (Shiller mirror, 1,867 months;
monthly-AVERAGE smoothing flag — tails muted, stated); US MARKET monthly TOTAL return
1926-07..2024-11 = (Mkt-RF + RF) from the vaulted FF3 (CRSP value-weight — broader than
the Dow, THE maximal true-month-end US series; stated substitution); US SMALL proxy =
market + SMB (the market is cap-weighted ~ the big side, so the SMB tilt approximates the
small side — a stated proxy; true ME-decile portfolios are on the Ken French runsheet
row); INDIA market monthly 1993-10..2025-12 = MF+RF (IIMA, nominal); INDIA SMALL monthly
proxy = market + SMB (IIMA, same construction); INDIA SMALL DAILY proxy = bottom tercile
of the survivor panel by PRIOR-YEAR median rupee value traded (n500_value_traded vault),
equal weight, reformed each Dec-31, 2013-2021 — SURVIVORSHIP AT MAXIMUM SEVERITY, stated:
smallcap deaths are exactly what a 2021-survivor panel deletes; every small-cap damage
number here is a SEVERE lower bound. Sigma = full-sample sd per series.
CELLS (12): s1 S&P 155y monthly sigma ledger + worst/best months — BARS: >=3sigma count
>= 3x Gaussian; >=4sigma >= 10x; 6sigma presence TWO-SIDED (averaging mutes tails).
s2 S&P monthly excess kurtosis >= 8; skew two-sided lean negative. s3 US market 99y
(true month-end): sigma ledger + kurtosis (prior: kurtosis 7-12; worst month <= -25%;
>= 2 months beyond 6sigma). s4 US SMALL vs MARKET: vol ratio >= 1.25x; kurtosis compare
TWO-SIDED; worst drawdown deeper for small (prior: 1929-32 small <= -90% nominal).
s5 monthly AR(1): small exceeds market by >= +0.05 (nonsynchronous-trading smoothing).
s6 US horizon table small vs market (1/5/10/20y): small mean-CAGR premium >= +1.5pp/yr;
small worst-20y TWO-SIDED. s7 India market monthly sigma/kurtosis (n=387, descriptive
bars: kurtosis >= 3). s8 INDIA SMALL vs MARKET (IIMA proxy): vol ratio >= 1.15x; worst
month deeper; AR(1) higher; full-period mean TWO-SIDED (the Indian smallcap premium is
contested). s9 INDIA SMALL DAILY (survivor tercile) vs NIFTY50: kurtosis and sigma-ledger
compare — TWO-SIDED (survivor cleansing may thin the measured tails); loud flag. s10 its
clustering: |r| autocorr all-positive thru 30; vol half-life same order as NIFTY's 82d.
s11 drawdown table small-vs-large both markets (descriptive). s12 the verdict read: does
small pay for its tail (mean/vol/worst joint summary, descriptive synthesis).
CONSUMPTION: the atlas artifact (same URL, extended), risk chapter, T4/low-vol context;
no promotion. Script: scripts/analyze_tl_d2.py. Census: 12.

| # | What | Result | Status |
|---|---|---|---|
| TL-D2 | Atlas extension: S&P 155y, US market 99y, small vs large US+India (interpretation hand-appended AFTER the print) | **s1 S&P MONTHLY 1871-2026** (1,867 months, sigma 4.05%): >=3sigma 25 vs 5.0 (**5x**, bar PASS); >=4sigma 9 vs 0.12 (**76x**, bar >=10x PASS); **4 months beyond 6-sigma** (two-sided landed PRESENT despite averaging): worst Nov-1929 -26.5 / Apr-1932 -24.0 / Oct-2008 -20.4 / Mar-2020 -19.1; best **Aug-1932 +50.3**. **s2** ex.kurt 16.7 (bar >=8 PASS); skew **+0.37 — lean-miss booked**: the most extreme month of American history is UP (the NIFTY daily-skew lesson repeats at 155y). **s3 US MARKET 99y** (true month-end): kurtosis 7.4 (in band), worst month **Sep-1931 -29.1%** (bar PASS), 3 months beyond 6sigma (bar >=2 PASS). **s4** small/mkt vol ratio **1.32x** (bar >=1.25 PASS); small kurtosis 8.6 > 7.4 (two-sided, fatter); worst drawdown small 85% vs mkt 84% — **the <=-90% prior MISSED — proxy artifact stated** (mkt+SMB compresses true bottom-decile depth; the ME-decile file is the runsheet fix). **s5** AR(1) small +0.15 vs mkt +0.09 (bar >=+0.05 PASS — the staleness signature). **s6 US HORIZONS**: small premium +2.7/+1.7/+1.6/+1.5pp/yr at 1/5/10/20y (bar >=1.5 PASS at every horizon); at 20y small's WORST (+5.3%/yr) beats the market's (+1.9%) and 10y positive-fraction 98% vs 95% — the US small premium RAISES the long-horizon floor (two-sided landed pleasant). **s7 INDIA MARKET monthly** (n=386): kurtosis **2.1 — the >=3 bar MISSED** (monthly aggregation already tames India's tails; 2 months beyond 4sigma, none beyond 6). **s8 INDIA SMALL (IIMA proxy)**: vol ratio 1.34x (PASS), worst month -35.3 vs -28.4 (PASS), AR(1) +0.17 vs +0.11 (PASS), maxDD **-90% (2001-09) vs -62%** — and THE HEADLINE: full-period mean **12.4%/yr vs market 15.3%/yr — the two-sided lands NEGATIVE: -2.9pp/yr for 32 years**. Indian smallcap BETA is uncompensated at factor level: more vol, deeper crashes, LESS return. The smallcap money in India is selection inside the segment, never the segment. **s9 INDIA SMALL DAILY** (survivor tercile, flag at maximum): kurtosis 12.0 < NIFTY's 16.6 and sd 1.02% < 1.09% (two-sided landed on the CLEANSED side) but skew -1.57 vs -1.01 and **daily AR(1) +0.20 vs 0.00 — the stale-price illiquidity signature: measured smallcap vol understates true risk because shocks arrive over days**; CAGR prints (39.6%/yr) are survivor-absurd, flagged as printed. **s10** |r| autocorr all-positive thru 30 (PASS); vol half-life 42d vs NIFTY 82d — same order, PARTIAL (half). **s11/s12 THE VERDICT**: US small pays (+1.5-2.7pp/yr, higher 20y floor) for its 1.32x vol; India small charges you (-2.9pp/yr) for 1.34x vol and -90% drawdowns. ARTIFACT extended, same URL | **US-vs-India smallcap verdict is the headline (opposite signs); 3 misses/partials booked (S&P skew lean, small-DD proxy artifact, India monthly kurtosis bar); US daily stays runsheet-gated; census +12 = 537** |

## Entry TL-D3 (2026-09-07) — PRE-REGISTERED before running: US DAILY TAILS LANDED + the
atlas extras. Principal directive: "have u added all 100y+ dow data and all sp500 data
like u did for nifty... check what more stuff we can add and interesting stuff... final
dashboard." DATA EVENT: the mirror hunt finally landed US DAILY — djia_daily_1980_2012
(Rdatasets/AER, 8,610 days, B1-B3 passed incl. Black Monday -22.61% exact) and SPX
futures daily 1982-09..2024-03 (pysystemtrade; hourly resampled by the declared
20:00-else-last convention; returns = d(adjusted)/lag(unadjusted) as declared; B4-B6
passed with one span miss recorded). The TRUE 100y+ DOW DAILY (1896-1980) remains
principal-machine (runsheet row stands — these two give 1980-2012 + 1982-2024 with 1987).
CELLS (12): t1 DJIA daily sigma ledger (zero-return holiday rows dropped, stated) —
BARS: >=3sigma >= 3x Gaussian; >=1 day beyond 6sigma. t2 DJIA shape/clustering: excess
kurtosis >= 15 (1987 dominates); |r| autocorr positive at all 30 lags; skew TWO-SIDED
(two prior skew leans have missed — registered symmetric). t3 SPX futures ledger — same
bars as t1. t4 SPX shape/clustering: kurtosis >= 15; vol half-life within [40, 160]
trading days (the NIFTY 82d order). t5 THE 1987 ANATOMY (descriptive): the day in sigma
units both series, the surrounding week, days to recover the prior peak. t6 S&P
MONTH-OF-YEAR SEASONALITY, 155y (12 calendar-month means + hit rates) — BAR: September
mean NEGATIVE (the September effect; the only registered directional month). t7 DECADE
TABLE 1870s-2020s, S&P nominal + real CAGR (descriptive). t8 STORM-TRANSITION MATRIX,
SPX futures: P(|r|>=2% tomorrow given |r|>=2% today) >= 3x the unconditional P — BAR.
t9 the same on NIFTY daily — BAR >= 3x. t10 3-sigma-days-per-year timeline (descriptive
— clustering made visible). t11 top-5 US real drawdowns with peak/trough/recovery years
(extends TL-D1 c8, descriptive). t12 LONGEST STREAKS: max consecutive down days
(DJIA/SPX/NIFTY) + max consecutive down years (S&P 155y, nominal) — descriptive.
CONSUMPTION: the atlas artifact (same URL — the final dashboard build), risk chapter, L2.
Script: scripts/analyze_tl_d3.py. Census: 12.

| # | What | Result | Status |
|---|---|---|---|
| TL-D3 | US daily tails landed + the atlas extras (interpretation hand-appended AFTER the print) | **t1/t2 DJIA DAILY 1980-2012** (8,307 days, holiday-zeros dropped as declared): >=3sigma 108 vs 22.4 (**5x**, PASS); **14 days beyond 6sigma** (PASS); ex.kurt **27.2** (bar >=15 PASS); skew **-0.95** (two-sided registered — the US daily tail IS asymmetric-down, unlike NIFTY's +0.06: 1987 lives on the down side); |r| autocorr all-positive thru 30 (PASS), vol half-life 67d. **t3/t4 SPX FUTURES 1982-2024** (10,468 days, declared conventions): >=3sigma 148 vs 28.3 (5x PASS); **18 beyond 6sigma** (PASS); ex.kurt **46.0** (PASS — the fattest series in the atlas); half-life 71d in [40,160] (PASS). **t5 BLACK MONDAY**: DJIA -22.61% = **-20.2 sigma**, SPX futures -28.61% = **-23.9 sigma**; preceded by -3.8/-2.4/-4.6 (the storm was on) and followed by **+10.1% within 48h** (the 2nd-biggest up-day of 33 years — the rebound-inside-the-crash law again); Dow recovered the pre-crash peak in **675 days**. **t6 SEASONALITY 155y — THE SEPTEMBER BAR FAILED**: Sep mean **+0.24%** (the September effect does NOT exist in this series); the only negative month is **OCTOBER -0.34%** (50% hit — where 1929/1987/2008 actually sit); Jan strongest +1.49%/66%; the calendar-folklore audit matches the India band verdict (only TOM survived there). **t7 DECADES**: best real 1950s +16.7, 1990s +14.6, 1920s +16.3; the destructions are INFLATIONARY (1910s -1.9, 1970s -1.4 real) not deflationary (1930s +2.1 real WITH dividends); 2000s -3.2. **t8/t9 STORM MATRIX**: P(|r|>=2% | storm yesterday) / unconditional = SPX **3.0x** (bar >=3 PASS at the line), NIFTY **3.2x** (PASS), DJIA 2.9x (descriptive). **t10**: 3sigma days/yr — 0 most years, **34 in 2008**, 20 in 2020, 11 in 1987. **t11 TOP-5 REAL DRAWDOWNS**: -77% 1929-32 (rec 1936), -52% 2000-09 (rec 2013), -50% 1973-74 (**rec 1985 — 12 years**), -48% 1937-42, -47% 1917-20. **t12 STREAKS**: max down-days DJIA 8 / SPX 9 / **NIFTY 10**; max down-YEARS 4 (1929-32); 34% of years are down years. VAULT: 3 new files, B1-B6 passed with one span miss recorded (repo snapshot ends 2024-03); dashboard rebuilt at the same URL | **one folklore bar FAILED honestly (September); one anchor span miss; US daily skew resolves the skew question (asymmetry is real in the US, absent in India daily); census +12 = 549** |

## Entry TL-D4 (2026-09-07) — PRE-REGISTERED before running: THE SIGMA LEDGER AT THREE
SPEEDS. Principal directive verbatim: "i want same 1sigma 2, 3 and 6 for weekly and
monthly for nifty 50 and the smallcap and the us one." ALREADY-BOOKED monthly ledgers are
CITED, not re-run (TL-D2 printed 2/3/4/6-sigma for S&P 155y monthly, US market 99y, US
small 99y, India market and India small monthly). NEW CELLS: the WEEKLY ledgers and NIFTY
monthly. Constructions declared: weekly return = calendar-week (W-FRI) sum of log daily
returns, exponentiated; monthly likewise; sigma = full-sample sd of the series at that
frequency; thresholds REPORTED IN PERCENT (the "points" the directive asks for). Series:
NIFTY 50 daily vault; India small = the SEC-D7/TL-D2 survivor bottom-tercile daily series
(2013-2021, survivorship flag verbatim); SPX futures 1982-2024 and DJIA 1980-2012 (TL-D3
vault, declared conventions).
CELLS (6): w1 NIFTY weekly ledger — BARS: 3sigma ratio in [2,6]x Gaussian; 4sigma ratio
BELOW the daily 121x (aggregation decay); 6sigma presence TWO-SIDED. w2 India-small
weekly ledger — same bars. w3 SPX futures weekly — same, plus: the 1987 week is the worst
week (prior). w4 DJIA weekly — same. m1 NIFTY monthly ledger — 3sigma ratio in [2,6]x;
6sigma lean ABSENT (n=224). x1 the 1-sigma completion row for the six monthly series
displayed (the |z|>=1 counts, one consumed look across them). THE REGISTERED SHAPE CLAIM:
within each market the 3sigma and 4sigma Gaussian-failure ratios DECAY MONOTONICALLY
daily -> weekly -> monthly (aggregational gaussianity in ledger form; the c5/TL-D1 ladder
restated as tail counts). CONSUMPTION: the atlas dashboard (one unified three-speed
table); census 6. Script: scripts/analyze_tl_d4.py.

| # | What | Result | Status |
|---|---|---|---|
| TL-D4 | The sigma ledger at three speeds (interpretation hand-appended AFTER the print) | **WEEKLY** (W-FRI): NIFTY 1sigma=2.71%/6sigma=16.2%; 3sigma ratio **5.3x** (bar [2,6] PASS), 4sigma 98x < daily 121x (decay leg holds HERE); worst week -15.9% = -6.0sigma (2008-10-24), no 6sigma count (two-sided). India small* weekly: 3sigma 3.9x (PASS); worst -12.4% (2020-03-20). **S&P futures weekly: 3 weeks beyond 6sigma** (two-sided landed present); worst week **2008-10-10 -19.6% = -8.4sigma** — **PRIOR MISS: the 1987 week is NOT the worst week** (Black Monday was one day; October 2008 was a regime); DJIA weekly the same shape (2 beyond 6sigma; worst 2008-10-10 -18.2%/-8.0sigma). **MONTHLY**: NIFTY 1sigma=5.98%/6sigma=35.9%; 3sigma ratio **6.6x — bar [2,6] MISSED by 0.6**; no 6sigma month (lean confirmed; worst 2008-10 -26.4% = -4.6sigma). India small* monthly 1sigma=6.46%, worst -27.2% (2020-03). S&P futures monthly worst **1987-10 -20.4% (-4.8sigma)**; DJIA monthly worst 1987-10 -23.2% (-5.5sigma). Cited TL-D2 monthly series rendered with the x1 completion row: US market 6sigma months = 3 (6sigma = 31.9%); US small* 2 (6sigma = 42.0%); **India small monthly 1sigma = 9.49%, 6sigma = 56.9% — never printed, but that is the scale of its "impossible"**; S&P 155y worst month Nov-1929 **-6.7sigma**. **THE REGISTERED DECAY CLAIM FAILED**: NIFTY 3sigma ratios 5.6 -> 5.3 -> **6.6x** (monthly EXCEEDS daily) and SPX 4sigma 84 -> **110** -> 64x — at monthly n=224-497 the tail counts are owned by two episodes (2008, 2020), so ledger RATIOS at low frequency measure EPISODE CLUSTERING, not distribution shape; the kurtosis ladder (TL-D1 c5) remains the honest aggregation instrument — miss booked, instrument boundary learned | **the three-speed table is on the dashboard; 3 misses booked (1987-week, NIFTY-monthly band, the decay claim); 1sigma-in-percent "points" delivered for all 13 series-speeds; census +6 = 555** |

## Entry OP-D1 (2026-09-07) — PRE-REGISTERED before running: THE OPTION-STATE BATTERY
(the measured inputs for a multi-tenor buy/sell option portfolio). Principal directive:
"mix weekly monthly and 6m 1y to get the best multi-strategy option buying-selling best
portfolio think deep." Rather than advise, MEASURE: with India VIX daily (2010-07..
2023-04, authenticated) and NIFTY daily OHLC, the variance-risk premium and every
state-conditional quantity that decides buyer-vs-seller at each tenor is computable
WITHOUT option chains (the chain pull upgrades this to strike-level; stated). H60-VRP is
the frontier parent. Conventions: RV over h days = sqrt(252/h * sum of squared daily log
returns), annualized, in vol points; implied = India VIX close (annualized vol points);
VRP_t = VIX_t - RV_{t+1..t+21}; VIX-implied 1-sigma h-day move = VIX/100*sqrt(h/252);
storm day = |ret| >= 2%; VIX percentiles = own-history expanding (min_obs 252d); overlap
flagged everywhere; sample 2010-2023 (excludes 2008 — stated: the worst seller's year in
the NIFTY record is NOT in the VIX sample, so all seller-friendly reads are UPPER bounds).
CELLS (12):
a1 mean VRP (prior: POSITIVE +2..+6 vol pts — sellers are paid on average);
a2 VRP by VIX quintile (5 reads as one table cell) — prior: mean VRP HIGHEST in the top
   quintile (fat premium post-spike), and the top quintile also holds the single WORST
   VRP print (two-sided honesty);
a3 the worst 21d VRP (prior: <= -25 pts, the Mar-2020 cell — what one bad month costs);
b1 breach rate of the VIX-implied 1-sigma 21d move (prior: < 32% — implied overprices
   on average, the seller's base edge);
b2 breach rate FROM THE BOTTOM VIX QUINTILE (prior: HIGHER than b1 — the registered
   complacency claim: calm implied underprices its own tail; if confirmed, "sell in calm"
   is refuted by measurement, not opinion);
c1 post-storm-day read: fraction of storm days where VIX_t still UNDERSTATES fwd 21d RV
   vs the unconditional fraction (prior: higher — the early-storm BUYER's edge;
   two-sided);
d1 weekly: breach rate of the trailing-21d-vol-implied 1-sigma 5d move, calm vs storm
   entry (prior: calm ~32%, storm-entry > calm);
e1 overnight share of total daily variance, full sample (prior: 25-40%; the T1
   overnight-drift/intraday-stress print cited) — the weekly-seller gap-risk input;
f1 fwd 6m NIFTY return after VIX top-decile days vs unconditional (prior: higher mean —
   the recovery asymmetry, CU-D7/CI-D4 cited);
f2 fwd 12m same (prior: higher, stronger);
f3 fwd 6m tail from BOTTOM-VIX-quintile days: P(return <= -10%) vs unconditional (prior:
   NOT lower — calm does not reduce the 6m tail; the cheap-wing/hedge-buying state);
g1 the mix test: correlation of the monthly seller proxy P&L (VRP sign/size) with the
   post-spike 6m buyer proxy (fwd 6m return after top-decile entries overlapping that
   month) — prior: NEGATIVE (the two sleeves hedge each other; the portfolio logic).
CONSUMPTION: the H60-VRP design brief + the option-portfolio note; NO promotion — paper
designs only until the option-chain pull + funding_rate land (CONTRACT). Script:
scripts/analyze_op_d1.py. Census: 12.

| # | What | Result | Status |
|---|---|---|---|
| OP-D1 | The option-state battery (interpretation hand-appended AFTER the print; 2008-not-in-sample caveat governs every seller-favorable read) | **a1 THE VRP IS REAL: +3.0 vol pts mean, +3.6 median, 82% of days positive** (prior band PASS) — Indian implied vol has systematically overpriced delivered vol, 2010-2023. **a2 AND IT IS STATE-PRICED**: mean VRP by VIX quintile +1.9/+2.2/+2.6/+3.7/**+5.9** — monotone, the top quintile pays 3x the bottom; the worst prints sit in EVERY quintile (-62..-64.5 — the crash traverses all states on its way up; two-sided honesty confirmed). **a3 the cost of one event: -64.5 pts** (2020-03-05: VIX 23.2 -> realized 87.8) = **21 months of mean premium in one window**. **b1/b2 THE HEADLINE — THE SELLER'S EDGE LIVES ONLY IN ELEVATED STATES**: VIX-implied 1-sigma 21d move breached 26% overall (< the 32% Gaussian-neutral, edge exists) BUT **32% from bottom-quintile VIX days (NO edge at all — calm implied exactly underprices its own tail) vs 17% from top-quintile days (a massive edge)**. "Sell premium in calm markets" is REFUTED BY MEASUREMENT; "sell after the spike" is confirmed. **c1 MISS (buyer side)**: on storm days VIX understates fwd RV only 15% vs 18% base — by the time the first storm day prints, implied has already caught up: post-storm VOL BUYING is NOT licensed. **d1 MISS (inverted, same shape as b2)**: weekly 1-sigma breach 36% from calm entries vs 30% from storm entries — the weekly seller's edge is ALSO post-storm, never calm-harvest. **e1**: overnight = only **20%** of daily variance (prior 25-40 missed low; T1 consistent — stress is intraday, which is stoppable, unlike gaps). **f1/f2 THE LONG-TENOR STATE IS DIRECTIONAL**: fwd 6m after VIX top-decile days **+18.2% vs +5.5%** unconditional; fwd 12m **+32.4% vs +12.0%** — the 6-12m post-spike instrument is a BULL structure (call spreads), not long-vol. **f3 MISS with a stated artifact**: calm-state 6m tail 3.8% < 7.3% base — but the sample's one calm-origin crash (COVID) RECOVERED inside 6m and 2008 is not in the VIX sample; the benign read does not travel. **g1 MISS, the most useful one: corr(seller proxy, post-spike buyer proxy) = +0.41, NOT negative** (n=24, flagged) — the monthly seller and the post-spike call buyer are THE SAME RECOVERY BET at different tenors; they do NOT diversify each other. The portfolio's true diversifiers are bought wings, the event sleeve, and CASH in the no-edge state | **the two-sided state law is measured (edge post-spike, none in calm, at both weekly and monthly tenor); 4 misses booked and each one reshaped the design; feeds the H60-VRP brief; paper-only until chain data + funding_rate (CONTRACT); census +12 = 567** |

## Entry OP-D2 (2026-09-07) — PRE-REGISTERED before running: THE OPTION-PORTFOLIO
OPTIMIZATION SWEEP (60-agent workflow: 22 researchers + 22 paired adversarial verifiers +
12 combiners + 4 synthesis, max 3 concurrent per house rule #6; agents read CONTRACT.md
from disk; every family's bars below are registered BEFORE launch; agents run EXACTLY the
registered cells; misses recorded, bars never moved). Principal directive: optimize
sizing/risk with HMM, vol clustering, candles, technicals, MR/trend at multiple
frequencies, gamma/theta, IV/RV/HV, daily management of weekly/monthly selling. Data:
vaulted only (NIFTY daily OHLC 07-26, India VIX 10-23, survivor panel, INR fx). All
no-lookahead constructions: expanding/rolling fits, state at t uses data <= t. Outputs:
scripts/opt_sweep/<id>.py + research/opt_sweep/<id>.json per family. NO promotion; feeds
the H60-VRP paper design only. FAMILIES (cells, prior/bar one-liners):
F01 HMM 2-state daily (EM refit quarterly-expanding) vs VIX-pct baseline (4) — prior: no
material gain over the simple state (fwd-vol spread ratio <= 1.15x baseline's).
F02 3-state HMM, same protocol (3) — prior: the 3rd state adds crash-onset separation or
nothing; two-sided.
F03 EWMA lambda {0.90,.94,.97} vs rolling {10,21,63} 1d-ahead vol QLIKE (6) — prior:
EWMA .94 beats rolling-21 by >= 3% QLIKE.
F04 GARCH(1,1) MLE vs EWMA .94 (3) — prior: statistical tie (<2% QLIKE gap); both lag
Mar-2020 by >= 20 vol pts at onset.
F05 vol-target sizing of the OP-D1 monthly VRP capture (target/EWMA, cap 2x) vs fixed (3)
— BAR: worst-month improves >= 30% at <= 20% mean cost.
F06 200d-MA trend x VIX-quintile -> fwd 21d ret/vol matrix (4) — prior: belowMA+hiVIX has
the widest fwd dispersion (structure-skew input); T-CTRL1 standalone-failure cited.
F07 12-1 momentum sign -> fwd 1m/3m ret+vol (3) — prior: weak positive tilt (T3 cited).
F08 daily MR: 5d z<= -2 / >= +2 -> fwd 5d (3) — prior: decayed post-2015; |effect| < 0.5
sigma; two-sided.
F09 panel-breadth washout (survivor panel %>200dMA proxy) -> fwd 21d index ret (2) —
two-sided.
F10 candles: doji/engulf/hammer/3-down on index OHLC -> fwd 1d/5d (8) — PRIOR: ALL NULL
(graveyard registration; any |t|>2 cell is a recorded surprise, not a signal).
F11 gaps: |overnight gap|>=1% direction -> intraday continuation + by VIX state (4) —
two-sided.
F12 Parkinson (OHLC) vs close-close 21d vol for 1d-ahead QLIKE (2) — prior: Parkinson
better by >= 5%.
F13 VIX vs fwd RV horizon match {5,10,21,63} + IV-HV spread pct -> VRP capture (5) —
prior: 21d peak corr; top-quintile spread best capture.
F14 VIX spike decay: half-life from >=90th pct; days to re-enter <60th (3) — prior:
half-life 15-40 trading days (the sleeve-A holding window).
F15 BS structural math (NO data mining): theta/gamma/vega for 1-sigma condors 7d vs 30d
at VIX 12/18/30 + stop-value math under the measured storm matrix (4) — analytic.
F16 THE MONTHLY PAPER SIM: daily-managed BS condor (entry VIXpct>=0.6, wings 2.5 sigma,
VIX-flat vol) mgmt {hold, stop-2x-credit, delta-band roll} 2010-23 (3) — BAR: stop-2x
cuts worst month >= 50% at <= 30% mean cost.
F17 THE WEEKLY PAPER SIM: storm/hi-vol entry weekly condor, mgmt {hold, daily-stop} +
per-unit-margin weekly-vs-monthly compounding compare (3) — the compounding claim
measured; two-sided.
F18 Kelly/ruin math on F16/F17 P&L distributions: full-Kelly, half-Kelly, DD-constrained
f (P(book DD>10%)<=1%/yr) (3) — analytic on measured odds.
F19 event calendar: |move| and VIX behavior around budget/election/RBI dates (declared
public dates) (3) — prior: budget vol-crush (CW-D1v cited); elections = the tail.
F20 L2-style stress flag x VRP capture vs VIX-pct alone (3) — prior: overlay trims left
tail >= 20% with <= 10% mean cost; two-sided.
F21 high-VIX beta stability of bank-heavy vs smallcap-tercile baskets (2) — hedge-
instrument input; prior: bank beta expands in stress.
F22 INR 21d momentum x VRP capture (the one-axis overlay at option frequency) (3) —
two-sided (CU coupling cited).
Census: 73 research cells + combiner cells booked at completion. Workflow: opt-sweep-60
(3 concurrent, sonnet). CONSUMPTION: the H60-VRP design brief v2 + SYNTHESIS.md.

| # | What | Result | Status |
|---|---|---|---|
| OP-D2 | The 60-agent optimization sweep — results (interpretation from the verified board; every family's full print in research/opt_sweep/fXX.json, scripts committed; each researcher adversarially verified by a paired refuter) | **THE DESIGN THAT SURVIVED** (SYNTHESIS.md, red-teamed): monthly symmetric condor (short 1.0-sigma, long 2.5-sigma wings, defined-risk mandatory), entry ONLY at India-VIX expanding-pct >= 0.60 (F16: in-state VRP capture +5.58 vs +2.96 unconditional, hit-rate 0.80, n=41/136 entries); sizing f_t = min(f_DD x s_t, **0.10 of book**) with s_t = EWMA(.94) vol-target capped 2x and f_DD = 0.150 (hold-arm conservative); management = **delta-band roll at |delta|>=0.30, max 3 rolls** (35.5% worst-month cut at 9.6% mean cost, 2.6x more cost-efficient than the stop-2x, which MISSED both its bars); capital split **80/20 monthly/weekly** (weekly preferably 0 — adds only +1.3%/yr); daily book-loss stop -2.22% (gap-budget -3.22%), halve at -5% sleeve DD, flat at -10%, re-entry only below the 60th pct (median wait 29td, never the 2-day VIX snapback); overlays kept: Budget T-1/T/T+1 exclusion (|ret| 0.95 vs 0.59%, p=0.0049, + the day-0 IV crush trade) and stress stand-down at pct >= 0.90. **THE COMPOUNDING VERDICT (F17): sizing-dependent, NOT frequency** — monthly compounds +13.96%/yr geometric (worst month -30.6% of margin) while weekly at full margin is IN-SAMPLE RUIN (the 2016-02-29 Budget week = -100% of margin); a <=20% earmark converts ruin into a bounded drawdown. **TAIL LAW CONFIRMED STRUCTURALLY**: no vol machinery sees crashes — EWMA and GARCH alike lagged the Mar-2020 onset by **72-74 vol points** (F04), so tail safety lives in the 0.10 cap + 2.5-sigma wings (max gapped loss 9.0x credit, F15 -> net premium at risk <= 1.11% of book), never in forecasts; s_t upsized INTO Aug-2013/Aug-2015 losses. **PASSES**: F06 trend-x-VIX dispersion, F16 roll-arm, F19 budget, F20 stress-composite (x2). **MISSES booked**: F01 HMM (45% storm capture vs VIX-pct's 82%, 0/41 crash onsets), F03 (EWMA tuning +1.21% vs >=3% bar), F05 (vol-target as tail protection), F07 momentum sign, F12 Parkinson (-7.5%, actively WORSE), F14, F16 stop-2x. **REFUTED (process)**: F13 IV-HV quintile gate — the paired verifier caught a groupby leak; dead until re-registered and re-run. **THE GRAVEYARD (c10)**: 10+ families buried — HMM (both), GARCH machinery, Parkinson, momentum/MR/breadth/gap direction overlays, candles (6/8 null, survivors unpromoted), INR overlay (null, 58% flag rate at +53% cost), bank-heavy hedge (beta CONTRACTS in stress — F21 prior falsified; smallcap-tercile hedge instead). UPPER-BOUND caveats stand: no 2008 in the VIX sample, post-2023-04 tail missing (2024 election + SEBI-curbs era break), flat-sigma BS, zero costs, funding_rate unset — **paper-only; H60-VRP registration deferred until the chain + VIX-tail pulls land** | **the sweep's verdict: simplicity won (one state variable, one structure, one management rule); the roll needs its own pre-registered bar before H60-VRP; 60 agents, 0 errors, every researcher refuter-checked, 1 process refutation caught; census: 73 research + 12 combiner looks = +85 -> 652** |

## Entry OP-D3 (2026-09-08) — PRE-REGISTERED before running: THE INTEGRATED PAPER
BACKTEST + THE HONEST IMPROVEMENT GRID. Principal directive: "backtest and improve."
OP-D2's design was validated family-by-family; this runs it as ONE system with all rules
interacting, then permits improvement ONLY through a pre-registered grid with train/test
selection — the baseline STANDS unless a variant beats it out-of-sample (no bar-shopping,
no post-hoc tuning). PROCESS NOTE #8 fields: purge = 21 trading days at the split
boundary (no test entry before 1 purge window after 2016-12-31); preprocessing info set =
expanding only (VIX pct min_obs=252, EWMA recursive); exact windows = train entries
2011-07..2016-12, test entries 2017-02..2023-03; benchmark = the FROZEN baseline variant
run on the same test window. Data: India VIX daily 2010-07..2023-04 + NIFTY daily; BS
flat-sigma pricing at India VIX, r=0.06; zero costs (stated — paper best-case); margin =
defined-risk max loss. SIM CONVENTIONS declared now: monthly sleeve only (weekly earmark
0 per c04's preference); expiry = last Thursday of the target month (>=15 calendar days
out at entry); enter on any flat day with VIX-pct >= threshold, outside Budget T-1..T+1
(budget list: 2011-02-28, 2012-03-16, 2013-02-28, 2014-02-17, 2014-07-10, 2015-02-28,
2016-02-29, 2017-02-01, 2018-02-01, 2019-02-01, 2019-07-05, 2020-02-01, 2021-02-01,
2022-02-01, 2023-02-01) and not in stand-down; structure = short 1.0-sigma strangle +
long WINGxsigma wings (sigma = VIX/100*sqrt(T)); size: max structural loss = f x book,
f = min(0.150 x s_t, 0.10), s_t = min(15%/EWMA94-vol, 2.0); DAILY MANAGEMENT: (i) roll
when |net structure delta| >= ROLL (re-strike at current spot, same expiry, max 3 rolls,
4th trigger = close); (ii) stand-down close at VIX-pct >= 0.90; (iii) book day-loss stop
-2.22% (close all); after any forced exit, re-arm only after VIX-pct prints < 0.60 once.
Baseline = (WING 2.5, ENTRY 0.60, ROLL 0.30) — the OP-D2 spec verbatim, frozen.
CELLS (38):
**OP-D3a — the integrated baseline (5):** b1 book maxDD <= 10% (the design's structural
claim — THE validation bar); b2 >= 70% of position-months positive; b3 sleeve
contribution >= +1.0%/yr on book (paper); b4 worst calendar month >= -3.5% of book;
b5 the yearly P&L table (descriptive; two-sided read on worst year).
**OP-D3b — the improvement grid (29):** 27 variants = WING {2.0,2.5,3.0} x ENTRY
{0.50,0.60,0.70} x ROLL {0.25,0.30,0.35}, each run on TRAIN only; selection cell:
pick argmax of [geometric mean - 2x|worst train month|] subject to train maxDD <= 10%;
validation cell: the ONE selected variant runs on TEST vs the frozen baseline on TEST —
IMPROVEMENT IS ACCEPTED ONLY IF test geometric mean is higher AND test maxDD is not
worse; otherwise the verdict "no improvement — baseline stands" is booked as the result.
**OP-D3c — robustness (4):** era split of the final choice (2011-16 vs 2017-23 reads),
ex-COVID (drop 2020-02..2020-06) read, r-sensitivity (r=0.05 vs 0.07) read.
CONSUMPTION: the H60-VRP design brief v3; paper-only (funding_rate unset; no chains —
flat-sigma stated); census 38 on completion. Script: scripts/analyze_op_d3.py.

| # | What | Result | Status |
|---|---|---|---|
| OP-D3 | The integrated paper backtest + the honest improvement grid (interpretation hand-appended AFTER the print; RUN NOTE: b2 first printed over all calendar months — recomputed over POSITION months per the registration, no bar moved) | **D3a THE INTEGRATED BASELINE** (all OP-D2 rules as one system, 2011-07..2023-03, zero-cost flat-sigma paper): book CAGR **+1.07%/yr**, maxDD **-2.93%**, worst month -1.41%, deployed 53/140 months (38%). BARS: b1 maxDD<=10% **PASS** (by 3.4x — the structural cap works as designed); b3 >=+1%/yr **PASS** (at the line); b4 worst month >=-3.5% **PASS**; **b2 MISS: 66% of position-months positive vs the 70% bar** (mean position-month +0.24%, median +0.28%); b5 yearly: 10 of 12 years positive, worst year 2020 **-2.0%**, best 2018 +3.0% — no losing year worse than -5% (two-sided read lands benign). **D3b THE IMPROVEMENT GRID — THE OOS GATE REFUSED IT**: train (2011-16) selected the aggressive corner (entry 0.50, wing 2.0, roll 0.25; obj +0.77) but on test (2017-23, 21td purge) it printed geo +2.17 with maxDD **-5.55% vs the baseline's -2.93%** — higher return, WORSE tail; the registered acceptance rule (better geo AND no-worse maxDD) fails -> **NO IMPROVEMENT, BASELINE STANDS** booked as the result. The grid's lesson mirrors ER-D4b/Goyal-Welch: train winners buy their edge with tail. **D3c ROBUSTNESS**: era-stable (2011-16 +1.16/-1.62 vs 2017-23 +1.01/-2.93); ex-COVID mean month +0.106 vs +0.090 incl (COVID is a small net NEGATIVE to the sleeve — the stand-down worked); r-insensitive (+1.10/+1.13 at r=0.05/0.07). CONSUMPTION READ: as a SLEEVE the design delivers ~+1.1%/yr on the whole book at a bounded -3% maxDD while using ~10% margin 38% of the time — a return-on-margin of ~+11%/yr in-state, consistent with F16; scaling beyond f_cap=0.10 is exactly what the ruin math forbids. Upper-bound caveats verbatim (no 2008, no chains/costs, post-2023 tail missing, funding_rate unset — paper-only) | **the design survived integration; "improve" was tried under a pre-registered protocol and honestly refused OOS; one bar missed (b2 66%); the H60-VRP brief v3 inherits this baseline verbatim; census +38 = 690** |

## Entry OP-D4 (2026-09-08) — PRE-REGISTERED before running: THE COMPOSED BOOK vs the
principal's 15/15 TARGET ("i want cagr>15% mdd<15%"). DISCIPLINE STATEMENT: the
composition is FROZEN from already-validated components with weights fixed by rationale
BEFORE running — this is a one-shot verification against the target, not a search; if it
misses, the honest frontier is reported and the miss booked (no re-weighting after the
print). COMPONENTS (all booked): (a) CORE 80%: NIFTY with EWMA(.94) vol-target 15%
capped 1.5x (F3a's validated mechanism) x a VIX stand-down multiplier 0.5 when India-VIX
expanding-pct >= 0.90 (OP-D2's rule; pct available 2011-07+, else 1.0); (b) DIVERSIFIER
20%: the T3 dual-momentum switcher — hold NIFTY or gold-INR, whichever has the higher
trailing-252d return, evaluated monthly (gold vault is monthly; gold-INR = gold_usd x
INR; sleeve marks at month-ends, flat intra-month — small DD-smoothing bias STATED);
(c) OVERLAY: the OP-D3 baseline option sleeve's daily P&L added on top (frozen spec).
Window 2011-07..2023-03 (the VIX-pct span); NIFTY price-only (dividends missing ~+1.3pp/yr
TR adjustment REPORTED alongside, declared not tuned); zero costs, paper.
CELLS (6): B1 nominal CAGR >= 15% (the target; also reported +1.3pp TR-adjusted);
B2 maxDD <= 15% (daily marks); B3 worst calendar year >= -10%; B4 era halves both >= 10%
CAGR; B5 component attribution table (descriptive); B6 the frontier read: if B1/B2 miss,
the measured trade-off (what CAGR the 15%-DD constraint actually buys) — booked as the
honest answer. PRIOR (two-sided, stated): CAGR lands 12-16%, maxDD 14-22% (COVID decides
B2); genuine uncertainty. CONSUMPTION: the book-level design brief; paper-only; census 6.
Script: scripts/analyze_op_d4.py.

| # | What | Result | Status |
|---|---|---|---|
| OP-D4 | The composed book vs the 15/15 target (one-shot; interpretation hand-appended AFTER the print; no re-weighting after seeing it, as registered) | **B1 MISS**: CAGR **+9.86%/yr** price-only (**~+11.2% TR-adjusted**) vs the >=15% target. **B2 MISS**: maxDD **-22.71%** vs <=15% (the drawdown is COVID-shaped: EWMA vol-target was AT ITS 1.5x CAP entering late-Feb-2020 because realized vol was low — the F04 onset-lag lesson reproduced at book level; the stand-down halves exposure only after the VIX spike). B3 PASS (worst year -7.9%, 2015). **B4 MISS**: era halves +5.80% / +13.63% (the 2011-16 NIFTY grind drags; 2017-23 TR-adjusted ~+14.9% touches the target). B5 attribution: core +6.62, switcher +1.97, option overlay +1.07 %/yr. THE HONEST ACHIEVEMENT vs raw NIFTY (+10.03%, -38.4%): **same return, 40% less drawdown** — the machinery converts the index's ratio 0.26 to **0.43**, but the target demands 1.0. **B6 THE FRONTIER**: no composition of currently-validated components reaches 15/15 on 2011-2023; the measured neighborhood is ~10-11% TR at -15 to -23% DD. THE TWO REGISTERED PATHS TO CLOSE THE GAP: (i) leverage on the composed book (~1.4x would print ~15%/-32% — FAILS B2; leverage helps only applied to a ratio>1 sleeve, none of which exists in the register; and funding_rate is unset — gated); (ii) ADD validated alpha sleeves — the strongest booked candidate is **M5 vol-managed India momentum (Sharpe 0.77->1.29, maxDD 83%->29%)**, unpriced for costs/implementation and carrying the standing 25-35% forward haircut — a NEW composition including it must be its own registered design, not a post-hoc retry of this one. Paper caveats verbatim (zero costs, price-only core, no 2008 VIX, funding_rate unset) | **the 15/15 target is REFUSED by the current validated toolbox, booked as a measurement not a failure of nerve; 3 bars missed, 1 passed; the gap-closing candidates are named and gated; census +6 = 696** |

## Entry OP-D5 (2026-09-08) — PRE-REGISTERED before running: THE STACKED MULTI-STRATEGY
BOOK under the principal's margin model ("2.5% of notional margin if hedged else 10% if
unhedged"). THE DESIGN LOGIC, stated before the print: OP-D4's miss decomposed into a
RETURN gap (needs gated alpha) and a RISK gap (-22.7% COVID DD caused by the measured
onset-lag — no reactive rule can fix it); this design attacks the RISK gap with an
always-on structure and adds measured-VRP overlays that consume MARGIN not CAPITAL
(hedged margin 2.5% of notional per the principal; long options = premium; pledge
haircut 10% stated). One-shot vs the same 15/15 bars; no re-weighting after the print.
COMPONENTS (frozen): (A) the OP-D4 core VERBATIM (80% vol-managed NIFTY + 20% dual-
momentum switcher); (B) PERMANENT PUT LADDER: 91-day 5%-OTM puts on the core's live
notional, rolled at 30 days remaining, BS-priced at India VIX (the always-on convexity;
its carry cost is the price of the DD bar); (C) COVERED CALLS: when VIX-pct >= 0.60 at a
monthly cycle, sell 1m 1-sigma-OTM calls on 50% of core notional (hedged by the core ->
2.5% margin class), settle at expiry; (D) the OP-D3 condor sleeve verbatim.
CELLS (8): s1 CAGR >= 15% (TR-adjusted +1.3pp reported); s2 maxDD <= 15% — THE bar this
design exists for (prior: the ladder converts -22.7 to -12..-17, genuine uncertainty);
s3 the put ladder's measured carry cost %/yr and its 2020 payoff (descriptive); s4 the
covered-call contribution and its rally-year give-up (two-sided); s5 peak margin+premium
utilization under the principal's model (feasibility read; prior < 20% of book);
s6 worst year >= -10%; s7 era halves; s8 the dominance read vs OP-D4 (better DD at what
return cost — the frontier). PRIOR on record: s2 PASSES or comes within 2pp; s1 likely
still MISSES (the return gap needs M5-class sleeves, not structure); if BOTH pass it is
a pleasant surprise to be treated with ER-D4b-grade suspicion. Paper caveats verbatim
(flat-sigma BS, zero costs, no 2008, price-only core +1.3pp TR note, funding_rate unset).
Script: scripts/analyze_op_d5.py. Census: 8.

| # | What | Result | Status |
|---|---|---|---|
| OP-D5 | The stacked multi-strategy book under the principal's margin model (one-shot; RUN NOTE: s3's in-loop cost tracker printed garbage from a broken accumulator — the registered quantity recomputed cleanly in a standalone pass, book P&L unaffected) | **s8 THE HEADLINE: OP-D5 STRICTLY DOMINATES OP-D4** — CAGR +10.08%/yr (TR ~+11.4) vs +9.86 AND maxDD **-16.04% vs -22.71%** (+6.7pp of drawdown bought at zero net return cost). **2020 flipped from +8.3% to +22.8%** — the permanent put ladder monetized the crash no reactive rule can see (the F04 onset-lag answered structurally). **s3 CLEAN COLLAR ECONOMICS**: ladder gross premium 7.58%/yr of protected notional, roll recovery 5.97%, net carry 1.62%/yr; ladder net P&L -1.60%/yr of notional (2020 +4.3, 2011 +7.5, worst carry-years 2012 -8.5 gross of payoff); **s4** covered calls +1.05%/yr book — THE CALLS FINANCE THE PUTS almost exactly (net structure cost ~0.3-0.5%/yr for 6.7pp less drawdown). BARS: **s1 MISS** (+10.08/+11.38TR vs >=15 — the return gap persists, as the registered prior said: structure cannot create alpha); **s2 MISS BY 1.04pp** (-16.04 vs <=15 — the registered "passes or within 2pp" prior lands in its within-2pp branch; the bar is NOT retuned to pass, per discipline); s5 MISS (peak margin+premium 26.3% vs the <20% prior — still trivially feasible under pledge, the prior was wrong not the design); s6 PASS (worst year -6.4%, 2015); s7 halves +4.99/+14.78 (the 2017-23 half prints **+16.1% TR-adjusted at -16% DD** — the target ratio exists in the good era). CONSUMPTION: the collar-stacked book is the new risk-side baseline; the REMAINING gap to 15/15 is ~3.6pp of CAGR and 1.04pp of DD, and its registered candidates are unchanged: the M5 vol-managed momentum sleeve (new design, cost-gated) + real option chains (credits/skew replace flat sigma) + the VIX tail. Paper caveats verbatim | **risk gap substantially closed by structure (collar: calls pay for puts); return gap confirmed to need alpha, not engineering; 3 misses booked honestly incl. the near-miss s2; census +8 = 704** |

## Entry OP-D6 (2026-09-08) — PRE-REGISTERED before running: THE FULL MULTI-STRATEGY
BOOK — OP-D5 plus the FACTOR SLEEVE. Principal directive: "more improve add more
strategies." The one validated, vault-runnable sleeve not yet stacked is the M/V-series
factor composite: vol-managed 50/50 WML+HML (IIMA monthly 1993-2025; M5 booked WML
vol-managed Sharpe 0.77->1.29 maxDD 83->29%; V3 booked the 50/50 combination Sharpe 0.86
beating both legs; V2 corr(value,momentum) -0.37). WEIGHTS FROZEN BY RATIONALE: core
65% (was 80 — the carve funds the higher-Sharpe sleeve), switcher 20%, FACTOR SLEEVE 15%
(vol-managed to 15% target, EWMA(.94) on monthly factor returns, leverage cap 2x, marks
monthly flat-intra-month like the switcher — stated). All OP-D5 overlays verbatim (put
ladder on the core notional, covered calls, condor sleeve). The weekly condor sleeve
stays EXCLUDED (c04's preference retained). STATED LIMITS: the factor sleeve is paper
LONG-SHORT (India SLB/borrow constraints and costs unmodeled — the M-series standing
25-35% haircut is reported as a sensitivity, not skipped); IIMA factor returns are
academic-construction gross returns. One-shot vs the same 15/15 bars; no re-weighting
after the print.
CELLS (8): s1 CAGR >= 15% (TR +1.3pp on the equity core reported); s2 maxDD <= 15%;
s3 factor-sleeve contribution %/yr + its worst year (descriptive); s4 THE HAIRCUT
SENSITIVITY: the same book with factor means cut 30% — both bars re-read (the honest
number); s5 peak margin/premium utilization (feasibility); s6 worst year >= -10%;
s7 era halves; s8 dominance vs OP-D5 (+10.08/-16.04). PRIOR (two-sided, stated): CAGR
lands 12.5-15 TR gross / ~11.5-14 at haircut; maxDD stays 14-17 (the sleeve is
low-corr); s1 at FULL factor is a genuine coin-flip, s1 at haircut likely MISSES —
if both pass at haircut, ER-D4b-grade suspicion applies. Census 8.
Script: scripts/analyze_op_d6.py.

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| OP-D6 | The full multi-strategy book: OP-D5 + the vol-managed 50/50 WML+HML factor sleeve at 15% (core cut 80->65), one-shot vs the 15/15 bars | **s8 THE HEADLINE: OP-D6 STRICTLY DOMINATES OP-D5** — CAGR +10.74%/yr (TR ~+12.04) vs +10.08 AND maxDD **-10.47% vs -16.04%** (dCAGR +0.66pp, dDD +5.57pp). The factor sleeve is the program's first stacked component that improves BOTH sides at once: **s3** contribution +1.80%/yr at 15% weight (sleeve standalone +17.02%/yr, worst sleeve year only -2.0% in 2018, mean leverage 1.59x of cap 2.0) — low-corr long-short cuts book vol, which the vol-managed core then re-levers less painfully through drawdowns. **s2 PASSES WITH ROOM** (-10.47 vs <=15) — the registered 14-17 prior was WRONG on the good side (two-sided prior miss recorded: the sleeve's diversification effect on DD was underestimated). s6 PASS (worst year -2.0%; NOTE 2023 is a Q1 stub — worst FULL year -1.7%, 2015). s7 halves +6.16/+14.96 (the improvement is era-concentrated: 2017 +33.7% is the sleeve's big year). **s1 MISS** (+10.74/+12.04TR vs >=15) — TR lands just BELOW the registered 12.5-15 gross prior band; **s4 THE HONEST NUMBER: at the -30% factor-mean haircut CAGR +10.17 (TR ~+11.47), maxDD -10.69, worst year -2.2% — s1 MISSES at haircut exactly as the prior said, s2 still passes**. s5 MISS (peak margin+premium 22.3% vs <20% prior — the prior was wrong again, not the design; feasible under pledge; factor long-short gross adds up to 30% notional needing SLB, unmodeled and stated). CONSUMPTION: the 65/20/15 collar-stacked book is the NEW BASELINE at ~+11.5-12.0 TR / -10.5 DD; the remaining gap to 15/15 is now ~3.0-3.5pp of CAGR with **4.5pp of DD headroom to spend** — the registered paths unchanged (real option chains, PIT breadth, funding_rate) are all principal-gated pulls. Paper caveats verbatim: flat-sigma BS zero costs, price-only core, academic gross long-short factors, no 2008 in the VIX sample | **both risk bars now pass with room; the return bar confirmed alpha-gated (structure exhausted: two stacks in a row moved DD, not CAGR); 2 prior errors + 2 misses booked honestly; census +8 = 712** |

## Entry OP-D6b (2026-09-08) — PRE-REGISTERED before running: CORRECTION LEG (principal
directive: "check for errors"). Audit of the OP-D4/D5/D6 book scripts found TWO
implementation errors vs their registered designs, confirmed by diagnostic before this
registration (magnitude checks only — no book number recomputed yet):
(E1) MONTH-DROP BUG: monthly sleeves (switcher, factor) mark returns at CALENDAR
month-ends via `if me in daily_index` — 44 of 141 months (31%) fall on non-trading days
and were silently ZEROED, not deferred. The registered designs said "marks at month-end,
flat intra-month" — intent was every month. Fix: mark at the LAST TRADING DAY of each
month. Direction: understates booked CAGRs.
(E2) FREE-LEVERAGE OMISSION: the vol-managed core runs expo>1.0x on 57% of days (mean
excess +0.28x) with no financing cost — ~0.95%/yr of core notional unmodeled. "Paper,
zero costs" was declared, but leverage financing is not a trading cost — it is part of
the return definition. Fix: subtract r=0.06 (the BS rate, declared as the paper funding
rate pending the funding_rate config) x (expo-1)+ daily. Direction: overstates CAGR.
(Audit also noted, run-note grade, no re-run: OP-D3's budget exclusion window is
T-2..T+1, one day wider than the registered T-1..T+1 — conservative direction, fewer
entries; stands as a declared deviation.)
Originals get dated run notes; bars are NOT moved; the corrected prints are the new
baselines. CELLS (5): a1 magnitude diagnostic (booked from the pre-registration check);
a2 OP-D4 re-run with E1 fix (bars re-read); a3 OP-D5 re-run with E1 (bars re-read);
a4 OP-D6 re-run with E1 (bars re-read); a5 OP-D6 re-run with E1+E2 — THE HONEST BASELINE
for everything downstream (bars re-read). PRIOR: E1 adds roughly +0.3-0.8pp CAGR to
D5/D6 (sleeve means positive); E2 subtracts ~0.4-0.7pp at 65-80% core weight; net for
a5 vs the booked D6 print: -0.5 to +0.5pp, DD roughly unchanged. Census 5.
Script: scripts/analyze_op_d6b.py.

## Entry MR-D1 (2026-09-08) — PRE-REGISTERED before running: THE MEAN-REVERSION BATTERY
(principal directive: "mean reversion opportunities and monthly bets"). NIFTY vault,
2011-07..2023-03 unless stated; all signals from information available at the close of
the signal day; expanding percentiles min_obs=252; VIX-pct = the house expanding pct.
CELLS (8):
m1 next-1d return after >=3 consecutive down days vs unconditional (daily MR existence);
m2a next-5d return after bottom-decile trailing-5d return (expanding decile), CALM
(VIX-pct<0.60); m2b same, STRESS (VIX-pct>=0.60);
m3a next-week return after 2 consecutive down weeks; m3b after 3 (weekly MR);
m4a next-month return after a <=-5% month; m4b same conditional on VIX-pct>=0.80
(monthly bets — informational for the NEXT design, not wired into OP-D7);
m5 THE OVERLAY ECONOMICS CELL: rule = after bottom-decile trailing-5d return AND
VIX-pct>=0.60, add +0.30x book synthetic long exposure for 5 trading days (financed at
r=0.06, margin 10% of add-on notional); report the rule's standalone contribution
%/yr, its active-day mean excess return, and both era halves.
INCLUSION RULE FROZEN NOW: the MR overlay enters the OP-D7 grid as an on/off axis ONLY
if m5 active-day mean excess return > 0 AND the contribution is positive in BOTH era
halves; otherwise the axis is dropped and its grid cells are not run.
PRIOR (two-sided): daily/weekly MR in India is weak post-2010 (T-CTRL1 precedent);
m2b/m4b (stress-conditioned) are the live candidates — post-spike buyer edge is booked
doctrine (OP-D1 f1/f2). Expect m1 ~ 0, m2b positive but noisy, m5 a coin-flip on the
both-halves condition. Census 8. Script: scripts/analyze_mr_d1.py.

## Entry OP-D7 (2026-09-08) — PRE-REGISTERED before running: THE OPTIMIZED BOOK UNDER
RELAXED CONSTRAINTS (principal directive: "add more strategies if needed relax some
constraints optimize ... weekly sells ... synthetic futures using options for long
entries"). Base = the OP-D6b a5 corrected book (E1+E2 fixes in ALL cells). RELAXATIONS,
each named and frozen:
R1 SYNTHETIC-FUTURES TOP-UP: core exposure cap raised 1.5x -> 2.0x; all exposure above
1.0x is implemented as synthetic long futures (long ATM call + short ATM put),
financing embedded at r=0.06 via put-call parity — subtracted as r x (expo-1)+ daily;
margin 10% of synthetic notional (the short-put leg is directional — unhedged under the
principal's model). The principal directed synthetics explicitly; r=0.06 is declared
the paper funding rate pending the funding_rate config (validator WARN stands).
R2 WEEKLY SELLS, POST-SPIKE ONLY: weekly condor sleeve — entry ONLY at VIX-pct>=0.80
(the sole state with booked seller breach-edge, OP-D1 b2/d1; c04's exclusion of
ALWAYS-ON weekly selling stands — this is a state-gated relaxation, not a reversal);
next-Thursday expiry (>=3 td else following), short 1.0-sigma strikes, 2.5-sigma wings,
units = 0.05 x book / maxloss, no rolls, sleeve day-stop -1% book, margin 2.5% notional
(hedged). Computed once as a book-relative stream.
R3 MR OVERLAY: per MR-D1's frozen inclusion rule (axis dropped if m5 fails).
R4 WEIGHT RE-OPTIMIZATION with the house purge protocol: TRAIN 2011-07..2016-12,
TEST 2017-02-01..2023-03-31 (21td purge, OP-D3b verbatim). Weight simplex
(core/switcher/factor): {65/20/15, 55/20/25, 60/15/25, 70/10/20, 50/25/25, 60/20/20}.
GRID = 6 weights x R1 {on,off} x R2 {on,off} = 24 train cells (x2 if R3 survives — the
24 doubles to 48; the census row will state which). SELECTION (frozen): maximize train
CAGR subject to train maxDD >= -15% AND train worst-year >= -10%; tie-break = smaller
|maxDD|. VALIDATION (frozen): the selected config vs the corrected-D6 config (65/20/15,
R1 off, R2 off) on TEST; ACCEPT iff test CAGR improves AND test maxDD >= max(baseline
test maxDD, -15%); else THE BASELINE STANDS and OP-D7 books "no improvement" honestly.
FINAL READS on the accepted config, full period (8): s1 CAGR>=15% TR; s2 maxDD<=15%;
s3 peak margin (incl. synthetic 10% + weekly 2.5% legs; prior <30% now — the 20% prior
missed twice); s4 the -30% factor-mean haircut, both bars re-read; s5 era halves;
s6 worst year >=-10%; s7 dominance vs OP-D6b a5; s8 yearly table + attribution.
All OP-D5 overlays verbatim throughout (ladder scales with expo — protection follows
leverage). PRIOR (two-sided): R1 adds +0.8-1.5pp CAGR at +1-3pp DD cost (financed
leverage into a vol-managed core is the one lever with real headroom — 4.5pp of DD room
exists); R2 adds +0.2-0.5pp at little DD (rare state, small size); the 15/15 TR target
is REACHABLE on s1 for the first time (call it 40-55%) but s4-at-haircut remains the
honest read and likely lands 13-14.5; if s1 passes at haircut too, ER-D4b-grade
suspicion applies. Census: 24 or 48 grid + selection + validation + 8 final = 34 or 58.
Script: scripts/analyze_op_d7.py.

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| OP-D6b | Correction leg: E1 month-drop (31% of monthly-sleeve months silently zeroed) + E2 free leverage (57% of days levered, ~0.95%/yr of core notional unfinanced), found by directed audit | a2 OP-D4+E1 +10.13/-22.75 (booked +9.86/-22.71, d+0.27pp); a3 OP-D5+E1 +10.32/-16.09 (booked +10.08); a4 OP-D6+E1 **+11.78/-11.40** (booked +10.74/-10.47 — the factor sleeve gained the most, +1.04pp: 31% of its months had been zeroed); **a5 OP-D6+E1+E2 = THE HONEST BASELINE: CAGR +11.13 (TR ~+12.43), maxDD -11.53, worst yr -2.3 (Q1-23 stub), peak margin 22.2% (incl. 10% on the levered synthetic fraction), eras +7.55/+14.41** — E2 costs -0.65pp, net vs the booked D6 print +0.39pp, inside the registered -0.5..+0.5 prior. Bars re-read: s1 MISS / s2 PASS / s6 PASS unchanged in direction everywhere. CORRECTION NOTE (2026-09-08, ER-D4b protocol): the OP-D4/D5/D6 headline numbers above are SUPERSEDED by a2/a3/a5 respectively; originals stay visible; no bar moved. All downstream comparisons now cite a5. Run-note grade, no re-run: OP-D3's budget window is T-2..T+1, one day wider than registered (conservative; declared deviation) | **both errors real and material (offsetting); corrected baseline +11.13/-11.53; census +5 = 717** |
| MR-D1 | Mean-reversion battery: daily/weekly/monthly + the m5 overlay economics cell with a FROZEN inclusion rule for the OP-D7 grid | **MEAN REVERSION IN NIFTY IS DEAD AT EVERY FREQUENCY POST-2011.** m1 next-1d after >=3 down days -2.3bp vs +4.5bp unconditional (continuation, not reversal); m2a/m2b next-5d after bottom-decile 5d ret +0.05/+0.06% vs +0.23% unconditional — WORSE than baseline in both states; m3a/m3b weekly nulls (+0.20/+0.14 vs +0.21); **m4a/m4b THE MONTHLY-BETS ANSWER: after a <=-5% month the next month averages -0.24% (vs +0.97% unconditional), and -2.86% when VIX-pct>=0.80 (n=5)** — India monthly returns CONTINUE, they do not revert; the monthly bet that works is the momentum switcher already in the book. m5 overlay +0.11%/yr, active-day excess +3.0bp, halves -0.20/+0.40 -> INCLUSION RULE NOT MET, MR axis dropped from OP-D7 exactly as pre-declared. Consistent with the registered prior and T-CTRL1. CONSUMPTION: no MR sleeve enters any book; post-spike longs remain a 6-12m horizon trade (OP-D1 f1/f2), never a 5d one | **clean negative battery; the frozen gate fired correctly; census +8 = 725** |
| OP-D7 | The optimized book under relaxed constraints: 24-cell purged grid (6 weight simplexes x synthetic top-up x post-spike weekly sleeve), frozen selection + validation | **VALIDATION REJECTED THE TRAIN WINNER — THE BASELINE STANDS.** Train selected 50/25/25 + weekly sleeve (+11.74 vs +7.55 baseline on train, every weekly-on cell beat its sibling by ~+2.3pp); on TEST it made +13.15/-9.60 vs baseline +13.35/-10.13 — the train edge did NOT carry, booked as NO IMPROVEMENT per the frozen rule. TWO DOCTRINE FINDINGS: (1) **synthetic-futures leverage at r=6% does not pay** — syn=Y is negative in ALL 12 train pairs (~-0.15pp each): the incremental calm-period equity premium over 6% financing is ~zero; the 4.5pp DD headroom cannot be spent on levered beta at Indian funding costs (funding_rate config now matters only if the principal's real rate is materially below 6%); (2) the post-spike weekly sleeve's edge is ERA-CONCENTRATED in 2011-16 (standalone +0.56%/yr full-period, +2.3pp train, ~flat test) — weekly selling stays excluded from the standing book. FINAL (= OP-D6b a5 verbatim): +11.13 (TR ~+12.43) / -11.53; s1 MISS, s2 PASS, s3 peak margin 22.2% PASS (<30%), s4 haircut +10.29 (TR ~+11.59) MISS / -11.86 PASS, s6 PASS, s7 identity with a5. The s1-reachable prior (40-55%) was WRONG — recorded: structure AND financed leverage are both now exhausted; the return gap to 15/15 TR is ~2.6pp and is ALPHA-GATED (real chains, PIT breadth, sub-6% funding — all principal-machine) | **optimization ran and honestly refused itself; two relaxations tested and rejected with doctrine; census +34 = 759** |

## Entry SW-2 (2026-09-08) — REGISTERED before launch: STRATEGY SWEEP 2 (principal
directive: "improve, use sonnet 5 for many parallel strategy max 5 at a time and 1
fable"). Track-E exploratory sweep over 15 strategy families not yet exhausted by the
register (overnight core, VRP-scaled condor sizing, lagged IV-RV gate redo, tri-asset
momentum w/ SPX-INR, factor-sleeve extensions, put-ladder + covered-call grids
(train/test PROPOSALS only), drawdown governor, gold sleeve upgrade, TOM overlay,
factor rotation timing, low-vol core (one-way), permanent USD-asset crash sleeve,
VIX-momentum stand-down, cash-yield accounting audit). 15 Sonnet research agents in
waves of <=5 concurrent + paired adversarial refuters (refute-by-default) + 1 Fable
synthesizer. RULES BOUND ON EVERY AGENT: CONTRACT.md read from disk; vault-only;
expanding/lagged signals; scratch to scripts/opt_sweep2/ + research/opt_sweep2/ only;
no ledger writes, no commits; every conditional mean/variant counted as a consumed
cell. ALL exploratory cells enter the census at completion (OP-D2 precedent); no sweep
number is a booked result; any surviving design gets its OWN one-shot registration
(bars + prior frozen) before running against the corrected baseline (OP-D6b a5,
+11.13/-11.53, TR ~+12.43). Census: exploratory cell count booked on return.

## Entry SW2-A1 (2026-09-08) — PRE-REGISTERED before running: THE IDLE-CASH ACCOUNTING
CORRECTION (SW-2 rank-1 consumption; f15 audit + Fable-synthesizer spec, adopted
verbatim). Not a strategy — an accounting gap symmetric to E2: core_stream charges
financing on expo>1 (E2 fix) but credits NOTHING on the idle core fraction when expo<1
(44.1% of days; avg 7.5% of book idle, 46.9% in the COVID window). FROZEN: credit rate
4.0%/yr (conservative net-liquid-fund, deliberately BELOW the 6% financing rate so the
credit leg can never outrank the cost leg; when the principal sets funding_rate,
re-book by linear rescale, never re-tune); credit base = CORE_W x (1-expo.shift(1))+ —
the engine's own one-day-lagged deployment series, zero new signal; day-count R/252;
applied via run_book's extra_ret hook (process note #6). Weights/caps unchanged.
CELLS (3): c1 baseline repro + credited-4% run — ACCEPTANCE: bit-for-bit vs f15's
liquid_fund_4pct cell (corrected CAGR 11.456, maxDD -11.3644); on acceptance ADOPTED
as the corrected baseline all future designs compare against; c2 the 6%-repo footnote
read; c3 peak-margin re-read INCLUDING the missing factor-sleeve margin line (f15
capital-use check: run_book's m-series carries ZERO margin for the long-short factor
sleeve, gross up to 60% of book) — both treatments printed (hedged 2.5% / unhedged 10%
on gross), declared as bounds pending a principal convention. MACHINERY (no cells):
stats_of(eq, d0, d1) in analyze_op_d6b.py silently ignored d0/d1 on the equity slice
(the f07 verifier's find) — fixed to slice; NO booked print used non-default args
(OP-D7 train/test used its own correctly-slicing win_stats), so no booked number is
affected — but the trap is real and a shared sliced-stats helper is owed to
quant/stats/ on the next machinery leg. Census 3.
Script: scripts/analyze_sw2_a1.py.

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| SW-2 | Strategy sweep 2: 15 Sonnet research agents (waves of <=5) x 15 families + 5 adversarial refuters + 1 Fable synthesizer; 21 agents, 0 errors; artifacts in research/opt_sweep2/ + scripts/opt_sweep2/ | **12 OF 15 FAMILIES HONESTLY DEAD; THE AUDIT LAYER EARNED ITS KEEP** (3 of 5 self-judged-promising families REFUTED by verifiers on flaws invisible to their own authors). Dead with mechanisms named: f01 overnight core (spectacular gross +26.3/-5.5 but cost-breakeven only 2-4bp one-way — a cost mirage; also 4.3x worse on zero-warning shocks); f02 VRP-quintile condor sizing (vacuous — reduces to a naive cap raise breaching the 10%-DD invariant); f03 lagged IV-RV gate (clean re-registration of the dead F13: DEAD AGAIN — a trade-more-often frequency confound, loses to frequency-matched VIX-pct controls); f05 factor extensions (SMB doubles maxDD; keep 50/50); f06 put-ladder frontier (REFUTED: protection axis silently measured Feb-2016, not 2020); f07 covered-call grid (REFUTED: its OOS bar was computationally vacuous — the agent inherited the stats_of d0/d1 no-op trap; TRUE test edge only +0.55pp with flat-worse DD); f08 DD governor (buys headroom the book does not need); f09 gold upgrades (flat/negative); f10 TOM overlay (era fingerprint flips under window shift; principal's no-trade cap stands); f11 factor rotation timing (destroys the -0.37 diversification benefit); f12 low-vol core (REFUTED twice: survivor panel positive-claim + undisclosed 2013-16 concentration); f14 faster stand-downs (rarer AND worse DD; do not re-try with tweaked thresholds). SURVIVORS: f15 idle-cash accounting gap (-> SW2-A1, adopted); f13 static 10% SPX-in-INR carve (+1.07pp CAGR/+1.55pp DD in-sample, self-haircut ~+0.3pp net of feeder TER; CONTRACT S1 scope-gated -> OPEN_QUESTIONS B4-4); f04 tri-asset 12-1 switcher (verified clean but ADDS NO CAGR: -0.12pp for +1.82pp DD — parked as stored DD budget, MUTUALLY EXCLUSIVE with f13). SYNTHESIS: the remaining ~2pp of the CAGR gap CANNOT be closed from inside the sleeve set on vault data — it is data-gated (real option chains, PIT panel, daily INR, post-2023 VIX — all Priority-1 pulls) and decision-gated (B4-4, batches 3+4) | **the vault's degrees of freedom are exhausted at index resolution; 251 exploratory cells booked; census +251 = 1010** |
| SW2-A1 | The idle-cash accounting correction (SW-2 rank-1): credit 4%/yr on the core's lagged idle fraction via extra_ret; one-shot, acceptance = bit-for-bit vs f15 | **c1 ACCEPTED: CAGR +11.456 (TR ~+12.76), maxDD -11.3644 — bit-for-bit vs f15's cell; ADOPTED AS THE CORRECTED BASELINE** (dCAGR +0.33pp, dDD +0.17pp vs a5; worst yr -2.3 Q1-23 stub; eras +7.89/+14.72). c2 footnote @6% repo: +11.62 (TR ~+12.92)/-11.28 (+0.49pp) — linear rescale when funding_rate lands. c3 peak-margin re-read WITH the previously-missing factor-sleeve margin line: 23.7% (hedged 2.5% on gross) to 28.2% (unhedged 10%) vs 22.2% ex-factor — bounds declared pending a principal SLB-margin convention; all inside the 30% feasibility prior. MACHINERY booked: stats_of d0/d1 slicing fixed (no booked print affected — verified); run_book gains fac_margin_rate (default None preserves pre-2026-09-08 reproduction); a shared sliced-stats helper owed to quant/stats/ | **baseline now +11.46 TR ~+12.76 / -11.36; census +3 = 1013** |

## Entry FUN-D1 (2026-09-08) — PRE-REGISTERED before running: GLOBAL BUSINESS-CYCLE
PHASE ATLAS (fundamentals track opener; principal: "start with business cycle ...
global research then indian specific"). JST r4, 18 economies, 1870-2020. PHASE
DEFINITION FROZEN: g = dlog(rgdppc); country EXPANDING median of g (min 10 obs) as
trend; quadrants: RECOVERY (below trend, rising) / EXPANSION (above, rising) /
SLOWDOWN (above, falling) / CONTRACTION (below, falling). Conditioning is REAL-TIME
HONEST: phase in year t conditions returns in year t+1 (annual publication lag);
contemporaneous reads are descriptive only. Real returns = (1+nominal_tr)/(1+dCPI)-1.
CELLS (10): p1 phase frequencies + transition stickiness (vs BC3's 77%); p2-p4 NEXT-YEAR
real equity/bond/housing returns by phase (pooled medians + share of countries agreeing);
p5 same for bills; p6 contemporaneous equity by phase (descriptive contrast); p7 the
ER-doctrine check: does EXPANSION underperform RECOVERY next-year (within-country
growth-negative timing fact, ER-D1b median -0.41 — prior says the naive rotation story
INVERTS); p8 crisisJST interaction (contraction WITH crisis vs without); p9 inflation
split (phase x high/low inflation, the L9/CI arc joined to phases); p10 post-1950 era
split. PRIOR (two-sided): recovery > expansion for next-year equity; bonds best in
contraction; if expansion is the BEST equity phase the growth-negative doctrine takes a
hit and that gets booked. Census 10. Script: scripts/analyze_fun_d1.py.

## Entry FUN-D2 (2026-09-08) — PRE-REGISTERED before running: THE EARNINGS CYCLE
(fundamentals layer 2, US 1871-2023). Shiller monthly, guard Real Price > 0; REAL
EARNINGS with a DECLARED 6-MONTH AVAILABILITY LAG on all conditioning (earnings for
month t are usable at t+6; descriptive census cells exempt and marked). CELLS (12):
e1 earnings-recession census: real-earnings peak-to-trough declines >=10% — count,
median/worst depth, median duration, recovery time; e2 price-vs-earnings lead/lag at
earnings troughs (does price bottom first, and by how many months); e3 same at peaks;
e4 next-12m real price return conditioned on earnings ABOVE vs BELOW their trailing-10y
real trend (lagged); e5 the interaction: that split WITHIN cheap/rich PE10 halves
(expanding median split); e6 next-12m return by earnings direction (rising/falling 12m,
lagged); e7 dividend smoothness: sd(d log real D)/sd(d log real E) + payout behavior in
earnings recessions; e8 depth link: earnings-recession depth vs same-window price
drawdown (rank corr); e9 the 2 deepest earnings recessions narrated from data (1921,
2008 expected — dates from data); e10 post-1950 split of e4; e11 earnings growth
persistence (AR(1) of annual real E growth); e12 the valuation bridge: PE10 at earnings
trough vs peak (median). PRIOR (two-sided): price leads earnings at troughs by 3-9m;
BELOW-trend earnings -> HIGHER next-12m returns (mean reversion + the ER staircase);
dividends 3-5x smoother; if ABOVE-trend earnings predict higher returns, the
growth-negative doctrine loses a leg and that gets booked. Census 12.
Script: scripts/analyze_fun_d2.py.

## Entry FUN-D3 (2026-09-08) — PRE-REGISTERED before running: INDIA SECTOR x CYCLE
LAYER (one-way; survivor panel 2012-2021, SEC-battery baskets reused verbatim from
scripts/analyze_sec_battery.py). India's GDP-cycle conditioning is DATA-GATED (IIP/PMI/
GST are runsheet pulls) — this partial uses MARKET-CYCLE proxies, declared as such:
state = NIFTY above/below its 12m MA x India-VIX expanding-pct >=/< 0.60 (both lagged
1 day) -> 4 states: CALM-UP / STRESSED-UP / CALM-DOWN / RISK-OFF. Sector reads are
RELATIVE to the equal-weight all-basket market (survivorship partially nets out in
relative reads; still one-way: negatives kill, positives only suggest, stated on every
line). CELLS (10): s1 state frequencies/durations; s2-s5 sector relative next-21d
returns by the 4 states (defensives FMCG/PHARMA/IT vs cyclicals METALS/AUTO/CAPGOODS/
REALTY vs financials PVTBANK/PSUBANK/NBFC — 3 group reads + full table read per state,
counted as 4); s6 the SEC-D6 consistency check: does the crisis-safety ordering
(balance sheet > demand > revenue-currency) reproduce in RISK-OFF; s7 transition trade
read: relative returns in the 3 months AFTER a RISK-OFF -> CALM-UP flip (early-cycle
cyclicality, n will be small — stated); s8 banks split: PVT vs PSU by state; s9 IT's
USD-hedge behavior in RISK-OFF (CU-D7 coupling check at sector level); s10 stability:
era halves 2012-16/2017-21. PRIOR (one-way, two-sided where testable): defensives
outperform in RISK-OFF (SEC-D6 says yes), cyclicals in CALM-UP recoveries; PSU banks
worst in RISK-OFF; IT positive-relative in RISK-OFF via USD revenue. Census 10.
Script: scripts/analyze_fun_d3.py.

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| FUN-D1 | Global business-cycle phase atlas (JST, 17 countries, 1881-2016; frozen growth-quadrant phases; real-time honest: phase t conditions returns t+1) | **THE ROTATION STORY INVERTS — the registered growth-negative prior CONFIRMED at phase level.** Next-yr real equity: RECOVERY +8.4% > CONTRACTION +7.1% > EXPANSION +5.0% > SLOWDOWN +2.5% (recovery beats expansion in 13/16 countries; post-1950 starker: CONT +12.0 / RECO +10.8 vs EXPA +5.7 / SLOW +1.2). The contrast cell p6 nails the mechanism: SAME-year equity is best in EXPANSION (+8.6) and worst in CONTRACTION (+2.1) — returns are CONCURRENT with the phase but by the time a phase is identifiable you are being paid for the NEXT one; chasing the identified phase is the losing side. p8: contraction WITH a JST crisis -> +13.8% next yr vs +6.9 without — the crisis year is the entry, not the exit (the post-spike doctrine at annual/global scale). p9 INFLATION DOMINATES PHASES: high-inflation roughly halves next-yr equity in EVERY quadrant (e.g. SLOW +1.3 vs +8.9) — the L9/CI arc holds inside the business cycle too. Bonds best in the below-trend phases (RECO +3.8/CONT +3.4 vs +1.6 both above-trend) — prior partial (recovery ties contraction). Housing is the pro-cyclical laggard (best in SLOWDOWN +8.0/EXPANSION +7.4). RUN NOTE: quadrant persistence is 28%/yr — NOT comparable to BC3's 77% (2-state definition); definitions differ, both stand | **phase-conditioned asset table booked; the cycle is PRICED — buy the identified trough, never the identified boom; census +10 = 1023** |
| FUN-D2 | The earnings cycle (US, Shiller 1871-2023; real-E>0 guard run-noted; 6m availability lag on all conditioning) | **e1 THE CENSUS: 16 real-earnings recessions in 152y (~1/decade), median depth -34%, worst -92% (2007-09), median 25m peak->trough + 34m recovery; the 1916-21 episode took 407m (34 YEARS) to recover real E.** e2/e3 THE ASYMMETRY: price bottoms ~10m BEFORE the earnings trough (price first in 75% of episodes) but does NOT reliably lead peaks (38%) — markets anticipate recoveries, not recessions. e4/e6 growth-negative in fundamentals: BELOW-trend earnings -> +5.4% next-12m vs +3.2% above; FALLING earnings -> +5.6% vs +2.9% rising. e5 the effect LIVES IN THE CHEAP HALF (below-trend+cheap PE10 +8.8% vs above-trend+cheap +5.5%; rich half compressed 2.0-2.7%) — depressed earnings + cheap multiple is the combination. **e10 HONEST DECAY: post-1950 the above/below gap vanishes (+5.2 vs +5.6)** — the earnings-level signal is pre-1950-concentrated; consistent with ER-D4b/Goyal-Welch. Mechanism cell e11: annual real-E growth AR(1) = -0.11 (anti-persistent — earnings mean-revert, prices know it). e7 dividends 2.7x smoother than earnings; in E-recessions dividends fall only 16% as much (median). e8 depth couples to price DD (rank-corr +0.70, median price DD -24%). e12 PE10 at E-troughs 16.8 vs peaks 19.5 — troughs are cheap even on CAPE | **earnings cycle mapped 1871-2023; anticipation asymmetry + smoothing + post-1950 signal decay booked; census +12 = 1035** |
| FUN-D3 | India sector x market-cycle layer (ONE-WAY survivor panel 2012-2021; declared market proxies NIFTY-vs-12mMA x VIX-pct, NOT GDP phases) | **THE TEXTBOOK SECTOR ROTATION FAILS AS A FORWARD TRADE IN INDIA — my registered prior MISSED and is booked as such.** In RISK-OFF states the DEFENSIVES lag forward (fwd-21d rel: DEF -1.76, PHARMA worst -2.07, IT -1.86) while cyclicals/financials lead (+0.57/+0.69, NBFC best +1.73) — CONSISTENT IN BOTH HALVES (s10: 2012-16 DEF -2.1 vs CYC +0.6; 2017-21 -0.75 vs +0.46). RESOLUTION vs SEC-D6 (no contradiction): SEC-D6 measured drawdowns DURING crisis episodes (defensives protect on the way down); FUN-D3 measures returns AFTER a stress state is identifiable — the rebound window, where beaten-down cyclicals recover. This is FUN-D1's inversion reproduced at sector level: by the time the state is visible, the defensive trade is done. ONE-WAY KILLS (negatives kill): 'buy defensives once risk-off is identified' DEAD; 'IT as forward USD-hedge at 21d' DEAD (s9 -1.86). s8 PSU banks are chronic: worst basket in CALM-UP (-3.67) and CALM-DOWN (-6.00), flat in RISK-OFF — underperformance is a state-independent fact 2012-21 (one-way). s7 flip-day read n=13, too small, prints kept descriptive. s1 CALM-UP 64% of days, states run short (2-8d median) | **rotation-by-identified-state killed one-way at sector level; defensives are DURING-crisis instruments, not after-crisis trades; census +10 = 1045** |

## Entry FUN-D8 (2026-09-08) — PRE-REGISTERED before running: THE REGIME-IDENTIFICATION
BATTERY (business-cycle deep-dive leg; principal: "data points and necessary key points
which can help us identify regime and alpha ... conditions we can generate out from it").
JST r4 annual, 17 economies; all conditioning states use year-t information to condition
year t+1 real returns (real = (1+nominal)/(1+dCPI)-1); country expanding medians (min 10)
for level splits; FUN-D1's frozen growth quadrants reused verbatim where phases appear.
CELLS (13): m1 SHORT-RATE DIRECTION (stir up vs down year) -> next-yr real equity (1) +
bonds (1); m2 CURVE SLOPE (ltrate - stir) country expanding terciles -> next-yr equity
(1) + bonds (1) + the MG-doctrine check: P(next-yr contraction-phase) by slope tercile
(1); m3 CREDIT ACCELERATION (d(tloans/gdp) above/below country expanding median) x
above/below-trend growth -> next-yr equity, the Borio joint cell (2: high-credit-x-boom
vs low-credit-x-slump corners + full 2x2 read); m4 INVESTMENT-SHARE (iy) high/low vs
country expanding median -> next-yr equity (1); m7 REAL-RATE LEVEL (stir - inflation)
terciles -> next-yr equity (1) + bonds (1) + housing (1); m5 THE JOINT SEASONS TABLE:
FUN-D1 phase x rate direction, next-yr equity, 8 cells printed as one read (1); m8 m5
repeated post-1950 (1). PRIOR (two-sided): falling rates > rising for next-yr equity;
inverted/flat curve -> higher contraction odds (MG says recession-odds ONLY — if slope
also RANKS equity returns monotonically that is NEW and gets flagged, not consumed);
credit-boom x above-trend growth is the WORST corner (Borio/L12 doctrine), low-credit x
slump the best (the FUN-D1 inversion compounded); high real rates hurt housing most
(DB-arc repression doctrine); if rate direction does NOT rank equity, the monetary layer
adds nothing at annual scale and that null is booked. Census 13.
Script: scripts/analyze_fun_d8.py.

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| FUN-D8 | Regime-identification battery (JST, 17 countries, 1870-2016; rate direction, curve slope, credit acceleration, investment share, real-rate level, phase x rate seasons; year-t states -> t+1 real returns) | **THE MONETARY LAYER RANKS RETURNS AT ANNUAL SCALE.** m1 falling short rates -> next-yr equity +8.0% vs rising +3.3% (bonds +3.0 vs +1.7) — prior PASS. **m2 FLAGGED NEW (per registration, not yet consumed): curve slope ranks next-yr equity MONOTONICALLY (flat/inverted +3.0 / mid +6.4 / steep +8.1) on top of the booked recession-odds channel (P(next-yr contraction) 42/34/28% by tercile)** — the MG doctrine ("slope = recession odds ONLY") needs an upgrade vote after an India/monthly verification leg. m3 PRIOR MISS booked: the Borio boom-x-above-trend corner is NOT the worst next-year cell (+5.3 vs calm-x-above +3.8; corner spread calm-slump-minus-boom-boom only +2.3pp) — at the t+1 horizon credit acceleration is pro-cyclical FUEL; the boom's damage arrives at the 2-5y crisis horizon (L12/Schularick-Taylor), NOT in next-year returns — horizon separation booked as doctrine. m4 investment share ~null (+5.8 vs +6.6, growth-negative direction). m7 REAL-RATE terciles: equity LO +3.6 / HI +8.3, bonds -0.2 / +6.7 — LOW real rates predict LOW real returns everywhere (the repression-era doctrine as a conditioning state); housing prior MISS (flat 5.7/7.3/7.0 — housing shrugs at real rates, DB-D7 mechanism note stands). **m5/m8 THE SEASONS TABLE (the actionable print): post-1950 the ONLY negative cell is SLOWDOWN x HIKING (-5.2%/yr, n=113); best cells CONTRACTION x CUTTING +13.7 and RECOVERY x HIKING +11.4** — hiking into a slowdown is the one identified state that has historically paid to avoid; both inputs are real-time observable. Both eras agree on the ordering | **monetary regime layer live; one flagged upgrade (slope), two honest prior misses (Borio timing, housing); the avoid-state named; census +13 = 1058** |

## Entry QG-D1 (2026-09-08) — PRE-REGISTERED before running: PAYOUT vs SUBSEQUENT
EARNINGS GROWTH (the growth/quality track opener; principal: "move to growth, roic,
roe, roce and earning quality"). The one firm-fundamentals-adjacent test the vault can
fund: the Arnott-Asness (2003, FAJ) aggregate test on Shiller 1871-2023. The
sustainable-growth identity g = ROE x (1 - payout) predicts LOW payout -> HIGH
subsequent growth; Arnott-Asness famously found the OPPOSITE on the S&P (high payout ->
HIGHER subsequent 10y growth) — mean-reversion of earnings + agency/empire-building
override the identity at the aggregate. Conventions: payout = D/E (Shiller nominal,
same units), 6-month availability lag (FUN-D2 convention); real-E>0 and real-D>0
guards (booked run notes); subsequent growth = annualized log real-E growth; monthly
overlapping observations FLAGGED (effective n is far smaller — no significance claims,
direction and magnitude only). CELLS (5): q1 Spearman rank-corr payout vs next-10y
real-E growth (full sample); q2 top-half vs bottom-half payout (expanding median
split) -> next-10y growth medians; q3 same at 5y; q4 q2 repeated post-1950; q5 the
mechanism read: payout level vs the CURRENT position of real E relative to its 10y
trend (is high payout just depressed-earnings state in disguise? — joins FUN-D2 e4).
PRIOR (two-sided): replicate A-A positive (high payout -> higher growth, corr ~+0.2 to
+0.4 in their sample era); if the identity side wins instead (negative corr), that is
the bookable surprise; q4 may decay post-1950 like FUN-D2 e10 — either way booked.
Census 5. Script: scripts/analyze_qg_d1.py.

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| QG-D1 | Payout vs subsequent aggregate real-E growth (Arnott-Asness 2003 re-run, Shiller 1871-2023, 6m lag, overlapping-months flagged) | **A-A REPLICATES ON THE SURFACE, AND q5 EXPOSES THE MECHANISM.** q1 rank-corr +0.17 (their era printed ~+0.39 [LIT]; direction PASS); q2 high payout -> +4.01%/yr next-10y real-E growth vs low +1.82 (+2.19pp); q3 stronger at 5y (+6.78 vs +1.45 — the mean-reversion horizon); q4 SURVIVES post-1950 (+4.96 vs +2.23 — unlike FUN-D2 e4's decay; noted). **q5 THE KILL: high-payout months are depressed-earnings months 78% of the time (vs 21% for low-payout) — payout spikes mechanically when E collapses because dividends are 2.7x smoother (FUN-D2 e7) — and WITHIN non-depressed months the gap INVERTS to -1.85pp.** So the celebrated "high payout predicts high growth" aggregate fact is substantially the depressed-earnings base effect (E mean-reverts, FUN-D2 e11 AR(1) -0.11) wearing a payout costume; the agency/empire-building interpretation [LIT A-A's own] is weakened at the aggregate (A-A's paper carries partial controls — noted, not adjudicated here). CONSUMPTION: aggregate payout is a REPACKAGED earnings-state variable, not an independent quality signal — do not spend cells on aggregate-payout timing; the firm-level payout/quality question is untouched by this print and stays with the India data legs | **A-A direction replicated, mechanism reattributed to the earnings state; census +5 = 1063** |

## Entry QG-D2 (2026-09-08) — PRE-REGISTERED before running: THE ROE/GROWTH/QUALITY
DECILE-AND-MATRIX BATTERY (principal: "rank basis roe top decile bottom and effect over
long term ... growth roe cross matrix and other 20-30 cases and matrix/decile/
segregation for factor ... alpha edge"). TWO AUTHENTICATED SOURCES, both newly vaulted
with two-pass AUTH (anchors committed first; two anchor mis-specifications recorded):
(A) firm_panel/data_ml (Coqueret-Guida, 1,207 US stocks, monthly 1998-11..2019-03;
features cross-sectionally uniformized to (0,1] -> RANK sorts only; forward returns
R1M/R12M raw; row t realizes in t+1 — declared; EQUAL-WEIGHT only; the panel is the
book's filtered sample — a survivorship/selection tilt DECLARED on every print);
(B) factors_us FF5/FF6 (1963-07..2020, ~2020 vintage) + Q5 (HXZ q-factors incl. R_ROE,
R_EG, 1967-01..2019-12). CONVENTIONS FROZEN: deciles/quintiles by the panel's own
uniformized ranks per date; ladder = one read-cell per named outcome; eras 1999-2008 /
2009-2019; up/down market = sign of the panel EW month; annualization x12 on monthly
means; no cost model (paper, declared).
CELLS (30):
 c1 Roe decile ladder, fwd-1m EW mean (D1..D10 + D10-D1);
 c2 Roe D10 vs D1 compounded (CAGR, monthly rebal) + terminal wealth ratio;
 c3 c1 by era halves; c4 D10/D1 vol, Sharpe, maxDD;
 c5 Roce ladder (does the capital-employed lens differ from Roe);
 c6 Eps_Basic_Gr (earnings growth) decile ladder — THE GROWTH QUESTION;
 c7 Capex_Sales (investment intensity) ladder — the asset-growth analog (CGS/CMA prior:
    negative);
 c8 THE ROE x GROWTH 5x5 (Roe quintile x Eps_Basic_Gr quintile, fwd-1m EW mean) — the
    principal's cross matrix; the "how much growth" read = the best column within each
    Roe row;
 c9 ROE x VALUATION 5x5 (Pb) — the profitable-value corner (Novy-Marx prior: cheap x
    high-Roe best);
 c10 ROE x MOMENTUM 5x5 (Mom_11M_Usd);
 c11 ROE x SIZE 5x5 (Mkt_Cap_12M_Usd) — the small-x-quality prior (AFIMP);
 c12 ROE x LEVERAGE 5x5 (Debtequity) — the SEC-D7 bridge at US firm level;
 c13 ROE x LOW-VOL 5x5 (Vol1Y_Usd);
 c14 quality composite ladder (mean rank of Roe, Ocf_Ta, inverse Debtequity — frozen);
 c15 within-CHEAP half (Pb below median): Roe ladder (the Piotroski-style read);
 c16 within-EXPENSIVE half: same (the Mohanram-style read);
 c17 growth WITHIN high-Roe (top-3 Roe deciles): Eps_Basic_Gr terciles — does growth
     ADD anything once quality is held;
 c18 Roe rank persistence (rank autocorr at 12m) + decile migration;
 c19 D10-D1 spread in up vs down panel months (defensiveness read);
 c20 GFC window read: D10 vs D1 cumulative 2007-10..2009-03;
 c21 fwd-12M horizon repeat of c1 (overlap FLAGGED);
 c22 RMW cumulative: CAGR/Sharpe/maxDD 1963-2020 — profitability long-term;
 c23 CMA same — the conservative-beats-aggressive growth answer;
 c24 Q5 R_ROE same (1967-2019); c25 Q5 R_EG (expected growth) same;
 c26 factor correlation matrix (MktRF/SMB/HML/RMW/CMA/UMD/R_ROE/R_EG);
 c27 RMW by decade table; c28 RMW/CMA in down-market months vs up;
 c29 50/50 HML+RMW blend vs each alone (Sharpe) — profitable value at factor level;
 c30 post-2013 (publication era) RMW/CMA vs pre — the decay read.
PRIOR (two-sided, from the dossiers): c1 positive but MODEST and NOT monotone at the
top (profitability premium is real; EW + small tilt may fatten it); c6 FLAT-TO-NEGATIVE
(LSV extrapolation); c7 NEGATIVE (CGS/CMA); c8 best cells in the HIGH-Roe row at LOW/MID
growth; c9 cheap x profitable the best corner; c11 spread biggest in small quintiles;
c19/c28 quality defensive; c25 R_EG positive and large per HXZ but its construction is
contested [LIT] — if R_EG dominates everything, flag rather than consume; c30 decay
expected. If GROWTH ladders print POSITIVE monotone, the LSV doctrine takes a hit and
that gets booked. Census 30. Script: scripts/analyze_qg_d2.py.

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| QG-D2 | The ROE/growth/quality decile-and-matrix battery: 21 firm-panel cells (data_ml, EW, 1999-2019, survivorship-tilt declared) + 9 factor cells (FF5/FF6/Q5, VW, 1963/1967-2020); 30 registered cells + 1 diagnostic run-note cell | **THE HEADLINE IS A METHODOLOGICAL KILL, BOOKED AS SUCH: c1 prior MISSED — the panel's ROE ladder printed INVERTED (D1 +29.7%/yr vs D10 +11.9, spread -17.8pp, both eras) while the SAME battery's value-weighted factor legs print profitability POSITIVE (RMW +2.8%/yr Sharpe 0.41; q R_ROE +6.3/0.75).** The run-note diagnostic resolves it: the inversion collapses to -1.3pp within the largest size quintile, and low-ROE names sit in the smallest quintile 33% of the time vs 7% for high-ROE — the "junk wins" print is an EW + smallest-cap + survivor-selection artifact (the low-ROE names that died are under-sampled; AUTH B5 declared the tilt). THE THIRD LIVE DEMONSTRATION (after the refuted low-vol core and the NSE backfill flag) that **construction dominates signal: EW survivor panels manufacture junk premia** — binding on every future India firm design (VW + delisted registry, non-negotiable). WHAT SURVIVES, cross-checked against the VW factor legs: **(1) the growth answer — DO NOT CHASE GROWTH**: EPS-growth ladder flat-to-inverted (c6), capex ladder ~flat (c7), growth WITHIN high-ROE flat (c17: terciles 11.6/9.7/10.4; c8 Q5-row best at LOW growth) — the LSV/CGS priors hold; growth adds nothing once quality is held; **(2) cheap-quality >> expensive-quality**: within the ROE-Q5 row, cheap 26.2%/yr vs expensive 9.3 (c9) and the 50/50 HML+RMW blend Sharpe 0.49 beats HML 0.32 and RMW 0.41 alone (c29) — Novy-Marx complementarity confirmed at factor level; **(3) quality is a DOWN-MARKET instrument**: RMW +9.3%/yr in down months vs -1.2 in up, CMA +12.1/-2.8 (c28); D10-D1 +17.7 in down panel months (c19) — joins SEC-D6/FUN-D3 doctrine (defensive during, never after); **(4) profitability is SLOW and sticky**: 12m rank-autocorr 0.69 (c18) — a quarterly signal, not a monthly one; **(5) post-publication decay is real**: CMA -2.5%/yr post-2013 (negative), RMW +1.1 vs +3.4 pre (c30); RMW decade table peaks in the 2000s (+8.5), prints -4.8 in the 2020s stub (c27). c25 R_EG (+10.0%/yr, Sharpe 1.49) FLAGGED per registration — contested construction, NOT consumed. c10/c13 momentum/vol within-rows contradict the VW literature -> artifact-suspect, not consumed. c20 GFC: D1 fell LESS than D10 (-30.8 vs -34.3) — survivor-selection tell, noted. c21 12m ladder same shape (overlap flagged) | **profitability real-but-modest, VW-only, defensive, decaying; growth confirmed not worth chasing; cheap-quality the combination; the EW-survivor artifact booked as doctrine; census +31 = 1094** |

## Entry QG-D3 (2026-09-08) — PRE-REGISTERED before running: ROE x HORIZON LADDER
(principal: "fwd 1y 3y 5y 10y by roe?"). firm_panel/data_ml (authenticated; EW;
survivorship tilt and the QG-D2 EW-junk artifact BOTH declared — hence every horizon is
read twice: all-panel AND largest-size-quintile only). METHOD FROZEN: per stock-month,
buy-and-hold compound forward R1M over h in {12, 36, 60, 120} months; require >=75%
month coverage else drop (attrition truncation declared — delisted paths shortened);
annualize (prod)^(12/h)-1; report per-decile MEDIAN annualized (mean secondary);
monthly OVERLAPPING formations flagged (10y has ~10 independent windows — direction
only, no significance). Formation cutoffs so full windows exist: h=120 formations end
2009-03. CELLS (10): h1-h4 all-panel ROE-decile ladders at 12/36/60/120m; h5-h8
large-cap-only (size Q5) ROE-quintile ladders at the same horizons; h9 attrition census
(share of formation rows with full coverage, by horizon x ROE D1 vs D10 — does junk
die more, truncating its compounding); h10 the summary read: D10-D1 (panel) and Q5-Q1
(large-cap) annualized spread by horizon. PRIOR (two-sided): all-panel inversion
persists or AMPLIFIES with horizon (the EW-junk artifact compounds); large-cap flat at
12m (QG-D2 diagnostic -1.3pp) with quality possibly edging ahead by 60-120m (rank
persistence 0.69 + the compounding story) — if large-cap high-ROE wins at long horizon
that is the honest quality-compounding print; if flat everywhere, quality's ABSOLUTE
edge in this era is nil and defensive-only doctrine stands alone. Census 10.
Script: scripts/analyze_qg_d3.py.

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| QG-D3 | ROE x horizon ladder: median annualized fwd 12/36/60/120m, all-panel deciles + large-cap-only quintiles, buy-and-hold, overlap flagged | **THE MEDIANS SOFTEN THE ARTIFACT AND REVEAL THE FADE.** All-panel D10-D1 by horizon: -2.3 / -2.8 / -3.9 / -3.2 pp/yr — the mean-based -17.8pp inversion (QG-D2 c1) collapses to a mild median inversion, confirming the junk "edge" is SKEW (a few EW moonshots drive the mean; the typical junk stock earns nothing special). **LARGE-CAP (the honest leg): Q5-Q1 = +1.4pp at 12m, 0.0 at 36m, -1.5 at 60m, -2.1 at 120m — and Q2 is the BEST column at EVERY horizon (10.4/7.8/7.2/5.5%/yr).** The shape is a textbook FADE signature: buying today's TOP-quintile ROE means holding through mean reversion (12m rank persistence 0.69 decays over 5-10y) at a quality-premium entry price; moderately-high ROE (Q2) — high enough to be quality, not so high as to be priced-for-perfection and fade-exposed — wins the compounding race. Joins the McKinsey fade doctrine + the quality-at-any-price trap (dossier D) with a real print. h9 ATTRITION SURPRISE: full coverage 100%/100% at every horizon — **the panel contains NO delisting truncation at all** (the book's selection filter removed death entirely); absolute levels are upper bounds everywhere; junk legs doubly flattered. PRIOR grading: all-panel persistence ✓ (branch 1); large-cap long-horizon: the prior's "quality edges ahead by 60-120m" branch MISSED — the data took the fade branch instead, booked. CONSUMPTION: for the future stock book, the ROE sort target is HIGH-BUT-NOT-EXTREME current profitability with persistence screens, never the top decile bought at any price; horizon does not rescue peak-ROE buying | **the Q2 hump + fade signature booked; top-decile-ROE-at-any-price rejected across all horizons; census +10 = 1104** |

## Entry QG-D4 (2026-09-08) — PRE-REGISTERED before running: GROWTH x HORIZON + THE
THREE CROSS-MATRICES x HORIZON (principal: "same for growth and growthxroe vs
growthxvolatility and roexvolatility 1 3 5 10y"). QG-D3 method verbatim (buy-and-hold
compound fwd 12/36/60/120m, >=75% coverage, MEDIAN annualized, overlapping formations
flagged, no-delisting upper-bound caveat carried). Axes: Eps_Basic_Gr (growth), Roe,
Vol1Y_Usd quintiles/deciles; large-cap = size Q5.
CELLS (24): g1-g4 growth decile ladder, ALL-PANEL, 4 horizons; g5-g8 growth quintile
ladder, LARGE-CAP ONLY, 4 horizons; m1-m4 ROExGROWTH 5x5 (all-panel) at 12/36/60/120m
(one read per horizon); m5-m8 GROWTHxVOL 5x5 same; m9-m12 ROExVOL 5x5 same; k1-k3
large-cap corner checks at 60m (the 4 corners of each matrix family, one read per
family — the honest-leg spot check); s1 summary: corner/edge spreads by horizon across
the three families. PRIOR (two-sided): growth inversion STRENGTHENS with horizon (LSV
extrapolation-reversal — glamour disappoints over years); ROExGROWTH: high-ROE/low-mid-
growth corner improves vs high-ROE/high-growth as horizon lengthens (fade + reversal
compound); GROWTHxVOL: the high-growth/high-vol LOTTERY corner is the worst cell at 60-
120m; ROExVOL: the 1m high-vol tilt (QG-D2 flagged artifact) should FADE with horizon —
if high-vol columns still win at 120m, that is the no-delisting flattery again and gets
flagged, not consumed; low-vol x high-ROE expected the strong large-cap corner at 60m.
Census 24. Script: scripts/analyze_qg_d4.py.

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| QG-D4 | Growth x horizon + ROExGROWTH / GROWTHxVOL / ROExVOL 5x5 at 12/36/60/120m (QG-D3 method verbatim; large-cap corner checks at 60m) | **THE MODERATION PRINCIPLE, PRINTED ACROSS EVERY MATRIX.** Growth never pays at any horizon (all-panel D10-D1: -2.9/-1.3/-2.5/-2.0; large-cap Q5-Q1: -2.8/+0.3/-2.3/-2.0 — prior ✓, LSV holds to 10y). ROExGROWTH: the best cell at EVERY horizon is ROE Q2 x growth Q2-Q3 (12.2 -> 7.8%/yr) and the worst long-horizon cell is the GLAMOUR-QUALITY corner (ROE Q5 x growth Q5: 6.5 at 1y -> **2.9%/yr at 10y**, the single worst corner) — fade + extrapolation compound exactly as registered. GROWTHxVOL: the lottery corner (high-growth x high-vol) is worst at 120m (3.3) and NEGATIVE in the large-cap 60m check (-1.8%/yr) — prior ✓. ROExVOL: **volatile "quality" is the trap** — ROE Q5 x vol Q5 is the worst cell at every horizon >=36m (3.1/2.9/2.4) and NEGATIVE in large caps at 60m (-0.7); the champion cell across horizons is ROE Q2 x LOW vol (13.0/11.7/8.9 at 12/36/120m). FLAG per registration: scattered all-panel high-vol cells still shine at 60m (e.g. lowgrowth x highvol 10.6) but the large-cap corner checks contradict them — the no-delisting flattery named in the prior; NOT consumed. SYNTHESIS (QG-D3+D4): every EXTREME corner underperforms and extremes COMPOUND each other's underperformance; the compounding cell is moderate-high profitability x low vol x modest growth — fade, extrapolation-reversal, and the lottery effect are one phenomenon at three axes. Consumption for the stock book: sort = Q2-ish ROE + persistence + low-vol + growth-indifferent; exclusion = any double-extreme (esp. high-ROE+high-growth and anything x top-vol) | **glamour-quality and lottery corners rejected at all horizons; the moderation cell named; census +24 = 1128** |

## Entry QG-D5 (2026-09-08) — PRE-REGISTERED before running: THE R_EG SPANNING TEST
(principal asked to explain the q-EG flag; the one sharpening test runnable on vaulted
data). Regress q5 R_EG monthly on the FF6 set (MktRF, SMB, HML, RMW, CMA, UMD) on the
1967-01..2019-12 overlap. CELLS (2): e1 the spanning alpha (annualized intercept + its
t-stat, Newey-West lags 6) — how much of R_EG's +10.0%/yr survives factors we already
hold; e2 the loadings read (which factors it repackages). PRIOR (two-sided): loadings
concentrate on RMW/CMA/UMD (the construction critique says expected-growth is a
repackaged profitability/investment/momentum composite); alpha shrinks materially but
likely stays positive-significant in-sample (the authors' own spanning tests claim it
does [LIT]) — an in-sample alpha does NOT lift the flag (the sample ends at
publication); only post-2019 OOS data can. Census 2. Script: inline in the ledger
interpretation (single regression; quant machinery not required by process note #6 for
a one-off OLS diagnostic — statsmodels/numpy lstsq with NW errors, stated).

| Design | What it is | Result (interpretation written AFTER the print) | Verdict |
|---|---|---|---|
| QG-D5 | R_EG spanning test: q expected-growth factor regressed on FF6 (MktRF/SMB/HML/RMW/CMA/UMD), 1967-2019, NW6 errors | **THE ALPHA IS NOT SPANNED — WHICH MAKES THE CONSTRUCTION CRITIQUE LOAD-BEARING.** Spanning alpha +8.34%/yr (t=10.9), R2 0.46; loadings RMW +0.23, CMA +0.20, UMD +0.13, SMB -0.14 — R_EG tilts toward profitability/conservative-investment/momentum big-cap, but 85% of its +9.77%/yr mean SURVIVES those controls in-sample. Per the registered prior: an in-sample alpha does NOT lift the flag — the vaulted series ends 2019-12, i.e. AT publication, so every month of this alpha was available to the authors when they specified the expected-growth forecasting model (predictors: Tobin's q, cash flow, dROE — fitted weights). A t=10.9 factor with Sharpe 1.49 and maxDD -12% over 52 years would be the best documented strategy in the literature; prior plausibility + specification-search risk say the burden of proof is OOS. FLAG STANDS: consumption requires (i) post-2019 live data, (ii) reconstruction of the signal from raw inputs under a purged protocol (firm-fundamentals-gated), (iii) an independent replication. Booked as the sharpest known example of the model-fitted-signal class | **flag retained with the mechanism quantified; census +2 = 1130** |

## Entry QG-D6 (2026-09-08) — REGISTERED-UNRUN (counts 0 until run): THE INDIA EXPECTED-
GROWTH REPLICATION, NIFTY 500 UNIVERSE, TRAILING ~10Y (principal: "run this [q-EG] basis
last 10y nifty 200/500 stock estimates top and bottom decile"). DATA-GATED on the
as-filed quarterly fundamentals pull (runsheet row live: NSE/BSE filings or XBRL,
delisted-name registry merged, 30-45d reporting-lag stamps) — the EG signal CANNOT be
built from the price-only survivor panel, and a price-proxy substitute is explicitly
FORBIDDEN by this registration (that would be the construction sin the R_EG flag names).
DESIGN FROZEN NOW, so the run is one-shot with zero post-data choices:
UNIVERSE: NIFTY 500 constituents AS OF EACH FORMATION DATE (point-in-time membership;
NIFTY 200 reported as a sub-read), monthly formations, target window 2016-01..latest.
SIGNAL (the HXZ q5 recipe, stated in full so nothing is fit to OUR sample twice):
expected 1y growth of investment-to-assets, forecast from THREE predictors only —
log Tobin's q (mcap + total debt - cash, over total assets), cash flow/assets
(CFO/TA), and dROE (4-quarter change) — with forecast weights estimated on an
EXPANDING trailing window (min 36 months) via cross-sectional Fama-MacBeth, PURGED:
each formation uses only filings known 45+ days prior. NO India-specific predictor
additions, NO weight tuning against returns (the weights fit INVESTMENT GROWTH, never
returns — this is the one construction feature that keeps the design honest).
CELLS (10): n1 top vs bottom DECILE fwd-12m (EW and VW both); n2 the full decile
ladder VW; n3 the spanning test vs IIMA MF/SMB/HML/WML (does any premium survive the
factors we hold); n4 era halves; n5 fwd-36m top/bottom; n6 NIFTY-200-only sub-read;
n7 predictor-attribution (which of q/CFO/dROE carries the forecast); n8 the realized-
growth check (does the signal actually FORECAST investment growth in India — if not,
the factor premise dies before the return question); n9 turnover/cost read at decile
rebalancing; n10 the US-flag adjudication read: India OOS is the first genuinely
post-publication test of the EG construction available to this desk — a positive n1/n3
here is REAL evidence the US flag should soften; a null is evidence the US alpha was
specification search. PRIOR (two-sided, stated now): n8 likely PASSES (the inputs
plausibly forecast investment anywhere); n1 VW likely +2 to +6%/yr, WELL below the US
+10 (haircut for specification-search inflation + India costs); n3 likely shows heavy
WML/quality overlap; if India prints Sharpe > 1 the ER-D4b-grade suspicion applies to
OUR pipeline, not celebration. Census 0 until run (10 on the day).

## Entry FUN-D9a (2026-09-09) — PRE-REGISTERED before running: THE SLOPE-RANKS-RETURNS
VERIFICATION, US MONTHLY LEG (the FUN-D8 m2 flag said the curve-slope return-ranking is
NEW vs the booked recession-odds-only doctrine and needs frequency/market verification
before consumption; India leg stays data-gated — this is the monthly-frequency half).
Data: Shiller Long Interest Rate (10y proxy) monthly 1871-2023 + FF RF (1m bill,
annualized x12) 1926-2020; US market TR = Mkt-RF + RF. Slope = GS10 - RF_ann, expanding
terciles (min 120m, lagged 1m). Fwd 12m market TR compounded (overlapping FLAGGED).
CELLS (3): v1 slope terciles -> next-12m US market TR (full overlap 1927-2019);
v2 same post-1963 (the FF5/JST-comparable era); v3 P(next-12m negative) by tercile (the
recession-odds analog without an NBER series). PRIOR (two-sided): monotone LO<MID<HI
replicating the JST annual print at monthly frequency; if FLAT, the annual finding is
panel/frequency-specific and the m2 flag HARDENS (no consumption path without India).
Census 3.

## Entry FUN-D10 (2026-09-09) — PRE-REGISTERED before running: MONETARY REGIME x FACTOR
RETURNS, US 1927/1963-2020 (the factor-level extension of FUN-D8 m1 and the
Jensen-Johnson/Conover line — the pre-verification for ever conditioning OUR WML/HML
sleeve on RBI repo direction). Regime = sign of the 12m change in the short rate
(RF annualized), lagged 1 month — real-time honest by construction. CELLS (7):
f1-f6 mean annualized return in RISING vs FALLING regimes for MktRF, SMB, HML, RMW,
CMA, UMD (FF6, 1963-2020; MktRF also read 1927- from FF3); f7 the post-1990 era repeat
of the RMW/CMA/Mkt reads. PRIOR (two-sided): Mkt materially higher in falling regimes
(FUN-D8 m1 analog); RMW/CMA relatively BETTER in rising/restrictive regimes (the
defensive-in-tightening story, Conover [LIT]); UMD unclear; if factor returns show NO
regime split, conditioning the India sleeve on repo direction dies before it is born —
booked either way. Census 7.

## Entry FUN-D9a RESULT (2026-09-09, interpretation written after the print) — THE m2
FLAG HARDENS. Runner: scripts/analyze_fun_d9a_d10.py (print-only; overlapping fwd
windows flagged at registration). Prints: v1 full 1937-2019 — LO +11.7% (med +13.8) |
MID +11.4% (med +13.4) | HI +13.5% (med +13.3); v2 post-1963 — LO +10.3% (med +14.2) |
MID +11.4% (med +14.0) | HI +13.7% (med +13.3); v3 P(next-12m negative) — LO 26% |
MID 28% | HI 14%. GRADE vs the registered prior: the MEANS show a mild HI-best tilt
(driven by the left tail, see v3) but the MEDIANS are FLAT-to-inverted (13.8/13.4/13.3
full; 14.2/14.0/13.3 post-1963) — the JST annual return-RANKING does NOT replicate at
US monthly frequency. Per the registration's own branch: "if FLAT, the annual finding
is panel/frequency-specific and the m2 flag HARDENS (no consumption path without
India)." Taken. The FUN-D8 m2 slope-ranks-returns read stays FLAGGED, now with a failed
frequency verification attached; consumption is fully India-data-gated. What DOES
survive: v3 ranks cleanly (26/28/14 — a steep slope halves the odds of a negative
next-12m), which is the recession-odds channel and is consistent with, not additive to,
the booked MG doctrine (slope as a STATE for downside odds, never a return forecast).
No parameter, book, or lesson consumes v1/v2. Census 3 (running total 1130 -> 1133).

## Entry FUN-D10 RESULT (2026-09-09, interpretation written after the print) —
REPO-DIRECTION CONDITIONING OF THE INDIA FACTOR SLEEVE DIES BEFORE REGISTRATION.
Runner: scripts/analyze_fun_d9a_d10.py. Prints (1963-2020, %/yr, RISING | FALLING |
gap=F-R): MktRF +5.20 | +7.67 | +2.47; SMB +2.04 | +4.97 | +2.93; HML +5.27 | +1.43 |
-3.84; RMW +1.67 | +4.12 | +2.45; CMA +3.74 | +3.33 | -0.41; UMD +7.75 | +8.12 |
+0.38. MktRF 1927-2024: +5.22 | +13.35. f7 post-1990: MktRF R+12.1/F+3.0 (REVERSED),
RMW R+2.6/F+5.3, CMA R+2.9/F+2.4. GRADE vs the registered prior (two-sided, graded
verbatim): (a) "Mkt materially higher in falling regimes" — HIT on the full 1927-2024
read (+8.1pp gap) and the 1963-2020 read (+2.5pp), but REVERSED post-1990 (R+12.1 vs
F+3.0): the market-level split is era-fragile, exactly the FUN-D8 f4-style
regime-instability signature. (b) "RMW/CMA relatively BETTER in rising/restrictive
regimes (Conover [LIT])" — MISSED: RMW is better in FALLING regimes in both eras
(+4.12 vs +1.67; post-1990 F+5.3 vs R+2.6); CMA is ~flat everywhere (-0.41 gap). The
defensive-in-tightening story does not survive this construction. (c) The one factor
that PREFERS rising regimes is HML (-3.84 gap, value likes tightening) — unregistered
direction, recorded as a surprise, not consumed. (d) UMD shows no split (+0.38).
VERDICT: factor-level monetary-regime splits exist in-sample but flip sign across eras
at the market level and contradict the literature prior at the factor level —
conditioning the India WML/HML/quality sleeve on RBI repo direction is REFUSED as a
design family (the registered kill branch, taken on era-fragility rather than strict
no-split). FUN-D8 m1's market-level "falling rates better" doctrine survives only as a
long-sample average with a known post-1990 reversal attached — STATE, not signal.
Census 7 (running total 1133 -> 1140).

## Entry ES-D1 (2026-09-10) — PRE-REGISTERED before running: THE REVISION-PROXY
(FUNDAMENTAL MOMENTUM) BATTERY, US FIRM PANEL. Principal directive of 2026-09-10 opens
the earnings-revision/surprise arc. STANDING CONSTRAINT: Atlas 3.5's DATA-REJECT on
India analyst consensus is UNCHANGED — no free PIT consensus exists; everything here is
a FUNDAMENTAL proxy (reported-EPS rank migration), stated as such, never sold as
analyst revisions. Data: firm_panel (data_ml, 1,207 US stocks 1999-2019; features
cross-sectionally uniformized to (0,1] so only RANK constructions are admissible;
EW-only; NO delistings — the QG-D2 junk-artifact caveat BINDS: every headline carries
its large-cap sub-read). Signal: dK(Eps) = Eps rank at t minus Eps rank at t-K per
stock (K = 3, 12 months) — rank migration in reported EPS. Forward returns via the
R{h}M_Usd columns (row t realizes t+1..t+h; the GFC-anchor forward convention of the
vault AUTH applies). CELLS (7): e1 decile ladder of d3(Eps) -> fwd-1m EW ann. mean,
D10-D1 spread; e2 same for d12(Eps); e3 large-cap control — top size quintile
(Mkt_Cap_12M_Usd q5), quintile spread Q5-Q1 for BOTH signals; e4 horizon profile:
d3 D10-D1 at fwd 1m/3m/12m (drift-vs-fade shape); e5 momentum-overlap control —
within Mom_11M_Usd quintiles, the residual d3(Eps) Q5-Q1 spread (does fundamental
momentum add beyond price momentum — Novy-Marx [LIT] says partially); e6 era split
of e1: 1999-2009 vs 2010-2019 (post-publication decay read, McLean-Pontiff [LIT]);
e7 vol interaction — d3(Eps) Q5-Q1 within low-vol vs high-vol halves (Vol1Y_Usd;
is the spread junk-concentrated?). PRIOR (two-sided, stated now): e1 positive
+2-6%/yr EW (panel small-tilt inflated); e4 fades by 12m (drift shape); e3 large-cap
spread MATERIALLY smaller (QG-D2 precedent) — if e3 ~0 the effect is a small/junk
artifact; e5 within-momentum increment is the CONSUMPTION GATE: only >= +2%/yr
residual spread AND a surviving e3 opens any India design conversation; e6 second
half weaker. If e1 itself is ~0 or negative, fundamental momentum dies on this panel
and the arc's India leg reduces to the PEAD event-study data ask (RUNSHEET row).
Census 7 on the day it runs.

## Entry SC-D1 (2026-09-10) — PRE-REGISTERED before running: SMALL-vs-LARGE
VALUATION/GROWTH SPREAD AS A TIMING SIGNAL, US FIRM PANEL 1999-2019. The principal's
"smallcap vs largecap valuation and growth comparison to predictability" — the direct
test. TL-D2 booked the LEVELS (US small pays +1.5-2.7pp/yr; India small charges
-2.9pp/yr); this is the TIMING layer. Construction (all ranks, per the vault's
uniformization): size quintiles by Mkt_Cap_12M_Usd each month; SL_{t+h} = EW mean fwd
return of Q1 (small) minus Q5 (large) at horizon h; valuation spread V_t = median Pb
rank of Q1 minus median Pb rank of Q5 (LOW = small cheap vs large); growth gap
G_t = median Eps_Basic_Gr rank of Q1 minus Q5. IN-SAMPLE DESCRIPTIVE, flagged: 240
months, terciles cut on the FULL sample — no real-time claim is available at this
length and none will be made; the print is a first-gate existence test. CELLS (5):
v1 V_t full-sample terciles -> next-12m SL (monotonicity + spread, overlapping
FLAGGED); v2 G_t terciles -> next-12m SL; v3 correlation profile corr(V_t, SL_{t+h})
and corr(G_t, SL_{t+h}) at h = 1, 12, 36m; v4 the corner read — cheap-small+
favorable-growth-gap months vs expensive-small+unfavorable months, next-12m SL gap;
v5 Pe-based repeat of v1 (robustness to the valuation measure). PRIOR (two-sided):
value-spread timing has multi-year-horizon support in the literature [Asness et al,
Cohen-Polk-Vuolteenaho, LIT] but factor timing is notoriously weak; expect v1
monotone-correct with a modest spread (+2-6pp next-12m T1-T3) and v3 rising with
horizon; G_t is the desk's own question — no strong prior, booked either way. KILL
BRANCH: if v1 AND v5 show no monotone relation even IN-SAMPLE, size-rotation timing
dies at the first gate and no India version is ever built (the NSE index-P/E
runsheet ask is then dropped). Census 5 on the day.

## Entry SC-D2 (2026-09-10) — PRE-REGISTERED before running: SMB TIME-SERIES
PREDICTABILITY, US FF MONTHLY 1926-2024. What, if anything, in SMB's own history
predicts SMB. Collision guard: CW2 (April seasonal) and FUN-D10 f2 (rate-regime
split +2.04 R / +4.97 F) are BOOKED — neither is re-run; this entry is the
time-series-of-SMB complement. Data: fff_monthly_us (SMB, Mkt-RF, RF 1926-2024).
CELLS (4): t1 SMB 12m momentum — sign of trailing-12m SMB sum -> next-12m SMB
(mean spread positive-minus-negative + hit rate); t2 multi-year reversal —
trailing-36m SMB terciles (expanding cut, min 120m, lagged) -> next-12m SMB;
t3 market-state rebound — next-12m SMB after DOWN market years (trailing-12m
Mkt-RF+RF < 0) vs after up years (the post-bear small-rebound claim); t4 era split
of t1: 1927-1980 / 1981-2000 / 2001-2024 (Banz publication 1981 [LIT]). PRIOR
(two-sided): factor momentum literature [Ehsani-Linnainmaa, LIT] says t1 mildly
positive; long-horizon reversal weak; t3 positive (small is high-beta into
recoveries); t4 attenuating. If ALL cells are ~null, the desk books "US size
rotation has no time-series handle" and the SC arc's consumption reduces to
SC-D1's valuation-spread channel only. Census 4 on the day.

## Entry SC-D3 (2026-09-10) — PRE-REGISTERED before running: INDIA SMB ANALOG,
IIMA MONTHLY 1993-2025. The India half of SC-D2, on the IIMA SMB factor (the same
series that carried TL-D2 s8's -2.9pp/yr verdict — quoted, not re-derived). CELLS
(4): i1 = t1 analog (India SMB 12m momentum -> next 12m); i2 = t2 analog (36m
expanding-tercile reversal); i3 = t3 analog (next-12m SMB after down vs up market
years, MF+RF market proxy; where MF is NA the market leg shortens — stated in the
print); i4 the regime map — rolling 5y SMB mean, dating the Indian smallcap
regimes (descriptive; the 2018 unwind and the 2023-24 froth should be visible —
if they are NOT, the IIMA factor's smallcap construction is re-interrogated before
any consumption). PRIOR (two-sided): i1 plausibly STRONGER than the US print
(retail flow persistence [LIT]); i3 positive but 2018-19 is the known
counterexample; TL-D2 doctrine caps ALL consumption here at Tier-C
monitor/reduce-only — a strong i1 print does NOT create a smallcap tilt, it
creates a registered monitor pending PIT smallcap data (the India fundamentals
handoff). Census 4 on the day.

## Entry ES-D1 RESULT (2026-09-10, interpretation written after the print) — THE PRIOR
MISSED: EPS RANK-MIGRATION IS *NEGATIVE* ON THIS PANEL. Runner: scripts/analyze_es_sc.py.
Prints: e1 d3(Eps) D10-D1 **-3.03%/yr** (prior said +2-6); e2 d12 **-6.47**; e3
large-cap d3 +1.27 (non-monotone noise) / d12 -2.17 — no large-cap effect either
direction; e4 the negative spread is FLAT across horizons (-3.03/-2.83/-2.98 ann. at
1/3/12m) — a LEVEL effect, not decaying drift; e5 within-momentum increments
+4.1/+4.9 in the two LOW-momentum quintiles but negative in high — mean +0.42, the
+2.00 consumption gate FAILED; e6 more negative 1999-2009 (-4.16) than 2010-19
(-1.72); e7 junk-concentrated (HIvol -3.47 vs LOvol -0.19). GRADE: the registered
kill branch is taken — fundamental momentum does NOT exist as a positive premium on
this panel; what the ladder actually shows is the EW-survivor REVERSAL artifact
(QG-D2's machinery: EPS-rank collapses mark beaten-down names whose no-delisting EW
returns rebound). The one mechanism-consistent pocket — fundamental improvement pays
+4-5%/yr ONLY where price momentum has not yet moved (e5 low-mom bins), the
Novy-Marx nuance [LIT] — is recorded as an observation, NOT consumed (it is inside
a failed gate on a survivor panel). CONSUMPTION: none. The India leg of this arc
reduces to the PEAD event-study route: the India fundamentals handoff P1 already
carries filing_date, so a PIT India PEAD design becomes REGISTRABLE the day the
vault authenticates (announcement-date granularity = daily; intraday timestamps
noted as a nice-to-have on the runsheet). Census 7 (1140 -> 1147).

## Entry SC-D1 RESULT (2026-09-10, interpretation after the print) — THE VALUATION
SPREAD RANKS SIZE ROTATION IN-SAMPLE; THE GROWTH GAP RUNS THE OTHER WAY. Prints:
v1 Pb-spread terciles -> next-12m small-minus-large: T1 (small cheap) **+28.78** /
T2 +13.06 / T3 +12.73 — monotone-correct, T1-T3 +16.05pp; v5 Pe repeat +16.81pp
(robust to the measure); v3 corr(V_t, SL) **-0.26 / -0.50 / -0.69** at 1/12/36m —
rising with horizon exactly as the value-spread literature says [LIT]; v2 growth-gap
terciles T1 +14.03 / T3 +23.39 (T1-T3 -9.36pp) and v3 corr(G_t, SL) +0.01/+0.08/+0.22:
small-growing-FASTER-than-large precedes small outperformance — the growth gap is a
(weak) POSITIVE conditioner, not the value-style contrarian one; v4 corners
+34.07 (n=12) vs +11.47 (n=38). GRADE vs prior: v1/v5/v3 HIT (monotone, spread well
above the +2-6pp guess); G_t booked as printed (no prior). HONEST LIMITS, as
registered: in-sample terciles on 240 overlapping months — the 2000-2005 small-cheap
episode plausibly carries much of the spread (~2 independent 36m observations); the
EW-survivor panel inflates the LEVEL of SL everywhere (every tercile positive) so
ONLY the spread is evidence; no real-time claim. CONSUMPTION: the first gate PASSES
-> the India small-vs-large valuation-spread series stays a live runsheet ask
(NSE index P/E-P/B history; methodology-change caveat to be checked at pull), and
any tradeable claim waits for that PIT data. Census 5 (1147 -> 1152).

## Entry SC-D2 RESULT (2026-09-10, interpretation after the print) — SMB MOMENTUM IS
A PRE-1981 FACT; THE POST-BEAR SMALL REBOUND IS REAL (IN THE US). Prints: t1 12m
momentum spread +4.49%/12m (62% vs 47% hit) — but t4: **+7.96 in 1927-1980, -0.37 in
1981-2000, -0.68 in 2001-2024** — the entire effect predates Banz's 1981 publication
[LIT]; t2 trailing-36m terciles LO -0.30 / MID +0.95 / HI +6.41 — CONTINUATION, not
the weak reversal the prior guessed (two-sided, booked as printed; given t4, the
long-sample continuation plausibly lives in the same pre-1981 era — stated as
interpretation, not computed); t3 after down-market years next-12m SMB +6.18 vs
+1.03 after up years (gap +5.15, n=271 overlapping) — the post-bear small rebound
prior HIT. GRADE: t1/t2 land in the era-fragility pattern FUN-D10 just booked at
the factor level — a third instance of "conditioning information that dies around
1980-1990"; t3 is the one robust-looking handle and matches the high-beta-recovery
mechanism. CONSUMPTION: none direct (US factor); t3's mechanism feeds the SC-D3
India read, where it INVERTED — see below. Census 4 (1152 -> 1156).

## Entry SC-D3 RESULT (2026-09-10, interpretation after the print) — THE POST-BEAR
SMALL REBOUND **INVERTS** IN INDIA; MULTI-YEAR REVERSAL, NOT MOMENTUM; THE IIMA
REGIME MAP PASSES ITS SANITY GATE. Prints: i1 12m momentum spread +3.99 but BOTH
sides <= 0 (-0.10 after up years, -4.09 after down) — India "SMB momentum" is only
the avoidance of smallcap after bad smallcap years; i2 trailing-36m terciles
**LO +10.32 / MID -0.51 / HI -2.50** — multi-year REVERSAL, the OPPOSITE of the US
print: three bad smallcap years precede a rebound, three good ones precede nothing;
i3 after DOWN market years next-12m SMB **-12.31** vs -0.20 after up years (gap
-12.11, n=93) — the US post-bear small rebound prior MISSED and INVERTED: after an
Indian bear year smallcaps keep LOSING to largecaps for another year; i4 the
rolling-5y map dates the regimes correctly (min -20.4 at 1999-11; max +9.9 at
2018-07 — the categorization-reform unwind peak; -4.0 at 2021-12; +8.6 at 2024-12 —
the froth SEBI intervened on; +3.3 latest) and the full-period mean -2.82%/yr
matches the TL-D2 s8 verdict on an independent construction. GRADE: i3 is the
headline — a doctrine-grade India-vs-US inversion, consistent with TL-D2
(uncompensated smallcap beta), T1b (stress keeps hitting risk assets after the
event) and FUN-D3 (the risk-off identifiability lag): in India, DOWN-CAP ROTATION
AFTER A BEAR YEAR IS THE MEASURED MISTAKE; the rebound trade that works in the US
transfers with the WRONG SIGN. i2's reversal offers the only India timing shape —
at 36m horizon, after multi-year smallcap winters — and per the registration all
consumption is capped at Tier-C monitor/reduce-only pending PIT smallcap data.
CONSUMPTION: one line into the india-regime-playbook (post-bear year: do not add
smallcap risk for at least the next 12m; the i2 winter-rebound is a watch, not a
tilt). Census 4 (1156 -> **1160**).

## Entry SC-D3a (2026-09-10) — PRE-REGISTERED before running: THE SURVIVOR-PANEL
CROSS-CHECK OF THE INDIA INVERSION (one-way partial of SC-D3; the parent's registered
prior for the mechanism quoted verbatim per process note #5: "i3 positive but 2018-19
is the known counterexample; TL-D2 doctrine caps ALL consumption here at Tier-C
monitor/reduce-only" — i3 then printed INVERTED at -12.31 vs -0.20). Data: the NIFTY500
survivor panel (n500_adjclose + n500_value_traded, daily 2012-2021, 487 names) + the
NIFTY 50 index vault for the market state. SURVIVORSHIP ONE-WAY RULE, stated now: the
panel deletes dead/delisted names, which FLATTERS smallcap returns; therefore a print
AGAINST smallcap here is admissible evidence (it survives a bias working the other
way), while a print FOR smallcap is recorded but is NOT evidence. Construction:
monthly returns from adjclose; size proxy = trailing-12m median daily value traded,
terciles per month (the TL-D2 s9 proxy); SL_t = EW mean monthly return, small tercile
minus large tercile. CELLS (3): a1 the i3 analog — next-12m SL after trailing-12m
NIFTY total-return DOWN vs UP (episodes are FEW in 2013-2021: ~2016, ~2019, COVID-2020;
n stated with the print); a2 the i2 analog — trailing-36m SL terciles (expanding where
feasible, else full-sample FLAGGED) -> next-12m SL; a3 the 2018-19 unwind anatomy,
descriptive — SL cumulative from 2018-01 peak to trough and the following 12m (the
categorization-reform episode at daily resolution; true damage is WORSE than printed,
survivor caveat). PRIOR (two-sided): a1 NEGATIVE (hardens the i3 inversion — and on a
panel that flatters small, a negative print is strong); a2 LO-tercile best (matches
i2) but any pro-smallcap reading is one-way-capped at "consistent, not evidence";
a3 trough SL cumulative <= -25pp with NO recovery inside 12m. If a1 prints POSITIVE
the inversion does NOT harden and the IIMA-vs-panel disagreement becomes its own
open question (booked, not resolved here). Census 3 on the day.

## Entry SC-D3a RESULT (2026-09-10, interpretation after the print) — a1 HARDENS THE
INVERSION DIRECTIONALLY; a2/a3 EXPOSE THE PANEL'S BLINDNESS, WHICH IS ITS OWN LESSON.
Runner: scripts/analyze_sc_d3a.py (+ the registered a2 fallback, inline). Panel SL
context: 113 months 2012-08..2021-12, mean +17.16%/yr — the survivor flattering at
full strength; context only, never evidence. Prints: **a1** next-12m SL after
NIFTY-down-12m **+13.85pp (n=20)** vs after up **+18.69pp (n=81)** — gap **-4.85pp**,
NEGATIVE as the prior required, on a panel biased the other way — ADMISSIBLE under the
one-way rule: the i3 inversion HARDENS directionally (milder than IIMA's -12.11
because the down-states here are 2015-16/2019/COVID-2020, and the 2020 state feeds
straight into the 2020-21 smallcap boom the panel over-credits). **a2** expanding
terciles INFEASIBLE at this length (usable n=6, all LO — data-insufficient, booked as
such); the registered fallback (full-sample terciles, FLAGGED, n=66) prints LO +10.50 /
MID +5.64 / HI +17.63 — NON-monotone: the panel does NOT corroborate the IIMA i2
winter rebound (prior MISSED on this panel; and any pro-smallcap shape here is
one-way non-evidence regardless). The i2 watch now rests on the IIMA print ALONE.
**a3** the 2018-19 unwind: cumulative SL 2018-01 to trough (2018-07) **-1.01pp**,
+4.69pp in the following 12m — the <= -25pp prior MISSED SPECTACULARLY, and the miss
IS the finding: a 2021-survivor panel cannot see the categorization-reform unwind
because it deleted the casualties (the ledger predicted this class of failure at TL
time: "smallcap deaths are exactly what a 2021-survivor panel deletes"). a3 is
non-evidence for smallcap health and a measured demonstration that the handoff's
delisted_registry (P3) is as load-bearing as the fundamentals file. VERDICT: the
post-bear rule stands (playbook line unchanged); the winter-rebound watch is
downgraded to IIMA-only support; no further smallcap design runs on this panel —
every remaining India ES/SC question is PIT-data-gated. Census 3 (1160 -> **1163**).

## Entry ES-D2 (2026-09-10) — PRE-REGISTERED before running: THE REVISION-PROXY
INTERACTION MATRICES (extension of ES-D1; parent constructions quoted: d3(Eps) = Eps
rank at t minus t-3 per stock via the calendar-aligned pivot; dec() = ceil(pct-rank x n)
per date; EW fwd returns from R1M/R12M columns, x1200 / x100 annualization; the
EW-survivor caveat BINDS throughout — large-cap sub-reads carry the honest weight).
Data: firm_panel. CELLS (8): m1 d3(Eps) x Pb 5x5, fwd-1m EW ann (the value-with-
catalyst map [LIT]); m2 d3 x Mom_11M 5x5 fwd-1m (the full-resolution version of
ES-D1 e5's within-momentum read — parent print quoted: increments +4.1/+4.9 low-mom,
negative high-mom, mean +0.42); m3 d3 x size (Mkt_Cap_12M) 5x5 fwd-1m (where in the
cap spectrum the negative ladder lives); m4 d3 x Roe 5x5 fwd-1m (does improvement
help quality or junk); m5 d3 x Vol1Y 5x5 fwd-1m (full resolution of e7); m6 = m1 at
fwd-12m; m7 the corner read — cheap+improving (Pb Q1-Q2 x d3 Q4-Q5) vs cheap alone
vs expensive+deteriorating, EW ann at 1m and 12m; m8 = m7 inside the top size
quintile (the implementable read). PRIOR (two-sided): the d3 main effect stays
negative (ES-D1); the cheap+improving corner beats cheap-alone by >= +2%/yr at 1m
(the catalyst story) — CONSUMPTION GATE: only if m7's corner increment >= +2%/yr AND
m8 preserves its SIGN does a "value+catalyst" flag get registered; expect m3
smallest-quintile-concentrated and m4 junk-side-concentrated (artifact signature).
Census 8 on the day.

## Entry SC-D4 (2026-09-10) — PRE-REGISTERED before running: THE SIZE-CONDITIONAL
EDGE MAP, US FIRM PANEL (the principal's "where can we have edge" question made a
matrix: WITHIN each size quintile, the Q5-Q1 EW spread for each signal — which
signals survive into the LARGE-cap end a NIFTY-750 desk can actually trade?).
Signals (all dec() n=5 per date within size quintile): Pb (value, spread = Q1-Q5 so
positive = cheap wins), Mom_11M_Usd, Vol1Y_Usd (spread = Q1-Q5, positive = low-vol
wins), Roe, Eps_Basic_Gr, d3(Eps). CELLS (12): s1-s6 the six signal spreads by size
quintile at fwd-1m EW ann; s7-s12 the same at fwd-12m (x100). PRIOR (booked-doctrine
side): low-vol spread positive everywhere, largest in small (moderation principle);
value positive, stronger small [LIT]; momentum positive, present in large [LIT];
Roe ~flat (QG-D2/D3); growth ~never pays (QG-D2); d3 negative, small-concentrated
(ES-D1). THE QUESTION CELL: which spreads keep their sign in size Q5 — prior:
momentum and low-vol survive large-cap, value weakens, growth/d3 die. Whatever
survives Q5 at BOTH horizons enters the edge list as "large-cap-implementable
(US evidence, India version data-gated)". Census 12 on the day.

## Entry SC-D5 (2026-09-10) — PRE-REGISTERED before running: THE SIZE x VALUE AND
SIZE x MOMENTUM JOINT MATRICES (the small-value / small-growth / large-value /
large-growth quadrant made explicit on this panel; FF's 25-portfolio geography [LIT]
re-measured on the vault's own data). CELLS (6): j1 size x Pb 5x5 fwd-1m EW ann;
j2 same fwd-3m (x400); j3 same fwd-12m (x100); j4 size x Mom_11M 5x5 fwd-1m;
j5 same fwd-12m; j6 the four-corner summary at 12m — small-value (size Q1-Q2 x
Pb Q1-Q2), small-growth (size Q1-Q2 x Pb Q4-Q5), large-value, large-growth, EW ann.
PRIOR (two-sided): small-value the best corner and small-growth the worst (the FF
lottery corner [LIT]; QG's "growth never pays" at panel level) — but on an
EW-survivor panel the small-value print is junk-inflated, so the honest rows are
the LARGE half: prior large-value modestly > large-growth at 12m. If small-growth
does NOT print worst, the panel's selection tilt is re-interrogated before any
consumption. NO consumption from j-cells beyond edge-list context lines — the
tradeable versions are India PIT designs. Census 6 on the day.

## Entry ES-D2 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_es_d2.py + research/notes/es_sc_matrices/es_d2.json; run by a Sonnet
agent on the frozen spec, desk spot-verified) — THE VALUE+CATALYST GATE FAILED: THERE
IS NO RESCUE FOR FUNDAMENTAL MOMENTUM ON THIS PANEL. m7 corner reads (EW ann):
cheap+improving +17.91 vs cheap-alone +19.47 at 1m — increment **-1.57** against the
>= +2.00 gate; 12m -2.35; m8 large-cap increment +0.18 at 1m / -1.24 at 12m. The
improving corner does WORSE than cheap alone. Matrix anatomy confirms the artifact
diagnosis: m1's cheap column peaks at d3 Q3 (+35.86 — NO-CHANGE names, not improvers);
m3's levels live in the smallest-size column (+26 to +35); m5's in the wildest-vol
column (+20 to +38). Grade: the ES-D1 kill is FINAL for this dataset — no interaction
(value, momentum, size, quality, vol) turns EPS rank-migration into a positive signal;
no value+catalyst flag is registered. The expensive+deteriorating corner IS avoided
ground (+11.30/+10.35 vs panel ~+15-19; large-cap +5.99/+6.36) — one avoid-list line,
consistent with the moderation principle, not a new signal. Census 8 (1163 -> 1171).

## Entry SC-D4 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_sc_d4.py + sc_d4.json; Sonnet agent, desk spot-verified szQ5 Pb +9.95
independently) — ON THIS PANEL, ONLY VALUE SURVIVES THE CAP SPECTRUM; EVERYTHING ELSE
IS SWAMPED BY THE JUNK BOUNCE. Fwd-1m spreads by size Q1(small)..Q5(large):
Pb +18.61/+4.79/+10.84/+4.76/**+9.95** — positive at EVERY size, both horizons
(12m szQ5 +8.80); Mom -24.52/../**-9.07** (losers win everywhere — the EW monthly
reversal artifact, NOT a momentum verdict); Vol -43.96/../**-2.95** (high-vol wins —
the junk bounce, fading toward large); Roe -29.47/../-4.72; Gr -12.21/../-5.97;
d3 ~0/-1 large. GRADE vs prior: "momentum and low-vol survive large-cap" MISSED — on
THIS construction (EW, survivor, monthly, arithmetic means) nothing but value
survives anywhere; the finding is a MEASUREMENT LIMIT, booked as such: this panel is
a value-and-nothing-else instrument, and the desk's momentum/low-vol/quality evidence
remains the VW factor prints (QG-D2: UMD, RMW; the moderation principle's median
construction). The one implementable-side data point this design yields: the value
spread in the LARGEST quintile, +9.95%/yr at 1m / +8.80% at 12m, monotone-ish
(j1 szQ5 row: +16.30 cheap -> +4.65 expensive). Consumption: one edge-list line
("large-cap value spread survives every construction this desk has thrown at it");
everything else defers to factor-level evidence. Census 12 (1171 -> 1183).

## Entry SC-D5 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_sc_d5.py + sc_d5.json; Sonnet agent) — THE RE-INTERROGATION BRANCH
FIRES: SMALL-GROWTH IS *NOT* THE WORST CORNER HERE (LARGE-GROWTH IS), AND THAT IS THE
PANEL'S TILT SPEAKING; THE VALUE-GROWTH GAP IS SIZE-STABLE. j6 four corners at 12m
(EW): small-value +21.02 | small-growth +15.76 | large-value +12.04 | large-growth
**+6.07** (worst). Registered branch taken: on a no-delisting EW panel the small rows
are level-inflated (j4 small-losers cell +46.47 is the tell) — the FF small-growth
lottery corner is invisible BECAUSE its casualties were deleted; declared at
registration, confirmed by print. The honest large-half read: value beats growth by
+5.97pp at 12m in LARGE caps (vs +5.26 small) — the value-growth gap is SIZE-STABLE
(~+5-6pp) on this panel, and the szQ5 value ladder is near-monotone (+16.30 ->
+4.65 at 1m). Consumption: context lines for the edge map only; the tradeable
versions are the India PIT designs (as registered). Census 6 (1183 -> **1189**).

## Entry H36-D1 (2026-09-10) — PRE-REGISTERED before running: THE 3-YEAR HORIZON
BATTERY (principal directive: "3y ideas not 1m/12m — recheck everything"). The ES/SC
arc re-read at 36m forward. WHAT ALREADY EXISTS AT 3y (recheck, quoted, NOT re-run):
QG-D3 (ROE 36m: all-panel D10-D1 -2.8pp; large-cap Q5-Q1 0.0; Q2 best at every
horizon); QG-D4 (36m matrices: champion ROE Q2 x low-vol 11.7%/yr; glamour-quality
and volatile-quality worst >= 36m; growth large-cap +0.3 at 36m); ER-D1c (dp -> 3y
+0.20 INSIDE the persistent-regressor null band — 3y index-level valuation forecasting
is null-consistent; only 20y beats the null); CU-D4iii (next-3y after a currency
crash +13.2%/yr vs +6.2 — a booked 3y entry-state); SC-D1 v3 (corr(V_t, SL) -0.69 at
36m). METHODS FROZEN (parents quoted per process note #5): panel fwd-36m = QG-D3's
convention verbatim (buy-and-hold compound of forward R1M over 36m, >=75% coverage
required, annualized); h1 uses MEDIANS (QG-D3 convention), h2-h5/h12-h13 EW MEANS
(ES-D2/SC-D4/SC-D5/SC-D1 parent convention); time-series cells use the SC-D2/D3
rolling-sum convention with next-36m sums annualized (/3); dec() as everywhere.
CELLS (13): h1 d3(Eps) deciles -> fwd-36m median ann (all-panel D10-D1 + large-cap
Q5-Q1); h2 the ES-D2 corner trio at 36m EW ann (all + large-cap repeat); h3 the
SC-D4 six signal spreads by size quintile at fwd-36m; h4 size x Pb 5x5 at fwd-36m +
the four corners; h5 the large-cap (szQ5) Pb row at fwd-60m; h6 US SMB 12m-momentum
sign -> next-36m SMB ann; h7 US trailing-36m terciles -> next-36m; h8 US post-bear ->
next-36m; h9-h11 the India IIMA analogs of h6-h8; h12 V_t terciles -> next-36m SL
ann; h13 G_t terciles -> same. PRIORS (two-sided): h1 the negative d3 spread FADES
toward 0 in medians (reversal-artifact signature); h2 expensive+deteriorating stays
worst (the avoid corner is a 3y statement), increment stays <= 0; h3 value the ONLY
positive spread across sizes; Mom/Vol/Roe/Gr spreads SHRINK vs their 12m prints in
>= 4 of 5 size bins (the junk bounce washes out); h4 the large-row value-growth gap
holds or widens vs 12m; h5 positive at 60m; h6/h9 momentum conditioning dead at 36m;
h7 the US 12m continuation flattens or reverts; h8 positive (the US rebound
compounds); h10 THE 3y IDEA CANDIDATE — the India winter rebound should be STRONGER
cumulatively at 36m if it is real mean reversion; h11 the India post-bear damage
narrows annualized but stays negative — if still <= -4pp/yr over 3y the playbook
rule extends to a 3-year statement; h12 T1-T3 wider than the 12m +16.05pp;
h13 modest positive. Census 13 on the day.

## Entry H36-D1 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_h36.py + es_sc_matrices/h36.json) — AT THREE YEARS THE NOISE WASHES
OUT AND THE MAP CHANGES: LOW-VOL EMERGES, VALUE COMPOUNDS, AND BOTH INDIA RULES
EXTEND TO 3-YEAR FACTS. Prints and grades:
h1 d3(Eps) median D10-D1 fades to **-0.84pp** (from -3.03 at 1m; large-cap -0.72) —
the reversal-artifact fade prior HIT; dead at every horizon, now with the full decay
curve booked. h2 corners: all-panel increment -0.52 (still <=0 ✓); the avoid corner
is a 3y statement — expensive+deteriorating +6.58 vs cheap-alone +10.91 all-panel,
and in LARGE caps +3.86 vs +8.09 (a 4.2pp/yr gap sustained 3 years); large-cap
increment +1.26 noted (below any gate, recorded not consumed). h3 the 36m edge map:
value positive at EVERY size (+8.55 small .. +5.18 large); Mom/Roe/Gr/d3 spreads all
SHRANK vs 12m (prior HIT, >=4 of 5 bins) — and **Vol FLIPPED SIGN in mid/large caps
(+3.29/+4.58/+2.41 at szQ3-5)**: low-vol wins at 3y once the junk bounce dies,
exactly the QG-D4 champion-cell (ROE Q2 x low vol 11.7%/yr at 36m) mechanism showing
up in an independent construction. h4 szQ5 value ladder +8.15 -> +1.69 (6.5pp/yr at
3y); corners LV-LG +3.57pp/yr (~+11pp cumulative — widens vs 12m ✓); SV-SG +4.15.
h5 the 60m large-cap value row: cheap-exp **+4.83pp/yr at five years** — persists ✓.
h6 US SMB momentum shrinks to +2.55 (era caveat stands); h7 mild continuation
persists (HI +3.73 vs LO +1.63) — no 3y reversion in the US; h8 US post-bear
+6.27 vs +1.32 ann over 36m (gap +4.95pp/yr) — the US rebound COMPOUNDS ✓.
h9 India momentum spread **-4.09** at 36m (after-strong-years -2.90) — chasing
India smallcap strength is NEGATIVE over 3y (the froth signature, worse than the
registered "nothing"). h10 THE CANDIDATE HIT: India winter terciles -> next-36m ann
**LO +8.01 / MID +2.22 / HI -3.27** (n=46/68/68 overlapping) — monotone at 3y
(~+26pp cumulative from the LO state); the winter rebound is a 3-YEAR shape, still
IIMA-only and Tier-C-capped. h11 India post-bear next-36m **-5.93 vs -0.58** ann
(gap -5.34pp/yr, ~-16pp cumulative, n=90) — the registered extension branch TAKEN:
the post-bear smallcap rule is a THREE-YEAR fact, not a one-year timing quirk
(playbook updated). h12 V_t terciles -> next-36m S-L ann T1 +31.94 / T3 +15.20
(T1-T3 +16.75pp/YR — the spread's power GROWS with horizon, matching corr -0.69 ✓).
h13 G_t at 36m NON-monotone (T2 highest; T3 n=23) — the growth-gap conditioner is
short-horizon only; booked as noise at 3y. RECHECK BASELINE (quoted, census 0):
QG-D3 36m (Q2-ROE hump 7.8%/yr, top-decile fade), QG-D4 36m matrices (champion
moderate-ROE x low-vol; glamour-/volatile-quality worst), ER-D1c (3y index-level
valuation timing is NULL-CONSISTENT — no 3y CAPE clock is ever built), CU-D4iii
(next-3y after a currency crash +13.2 vs +6.2 — the booked 3y entry state).
Census 13 (1189 -> **1202**).

## Entry VAL-D1 (2026-09-10) — PRE-REGISTERED before running: THE VALUATION-MEASURE
LADDER (the VAL arc opens; principal: "valuations as edge... methods"). Which
valuation MEASURE carries the cross-sectional edge, head-to-head, same universe, same
conventions (firm_panel; dec() n=5 per date; EW; fwd 1m x1200 / 12m x100 / 36m QG-D3
compounding; EW-survivor caveat binds; large-cap szQ5 sub-reads carry the honest
weight). Measures (cheap side stated): Pb LOW, Pe LOW, Ev_Ebitda LOW, Fcf_Yld HIGH,
Div_Yld HIGH, Bb_Yld HIGH. CELLS (8): v1-v6 one per measure — the cheap-minus-
expensive spread at 1m/12m/36m + the szQ5 12m read; v7 the COMPOSITE (equal rank-mean
of Pb, Ev_Ebitda, Fcf_Yld, signs aligned) — same profile; v8 the ladder verdict —
rank measures by szQ5 12m spread (the implementable column). PRIOR (two-sided):
FCF yield strongest recent-decade claim [LIT] and Ev/EBITDA >= Pb (Loughran-Wellman
[LIT]); Div_Yld weakest (the QG-D1 payout-state confound — quoted); composite >= best
single is the classic claim, tested not assumed; if Pb wins outright the
intangibles-era decay story is overstated on this panel. Census 8 on the day.

## Entry VAL-D2 (2026-09-10) — PRE-REGISTERED before running: THE COMPLEMENTARITY
MATRIX — which metrics ADD to value, which repackage it, which fight it. FROZEN
NUMERIC RULES (thresholds inherit the ES-D2 gate scale of 2.00%/yr — precedent, not
a new magic number): for companion X with its good side stated, (i) WCS =
within-cheap spread — among Pb Q1-Q2 names, X's good-minus-bad quintile spread,
fwd-12m EW ann; (ii) VSC = value-survival check — the mean Pb Q1-Q5 spread WITHIN X
quintiles, fwd-12m. VERDICTS: COMPLEMENTARY if WCS >= +2.00 AND VSC >= +2.00 (and
the szQ5 WCS sign agrees — else demoted to PANEL-ONLY); REDUNDANT if |WCS| < 2.00
AND VSC >= +2.00; SUBSUMING/ANTAGONISTIC if VSC < +2.00 OR WCS <= -2.00. Companions
(good side): Roe HIGH, Mom_11M HIGH, Vol1Y LOW, Debtequity LOW, Share_Turn_12M LOW
(neglect story — two-sided), Eps_Basic_Gr HIGH, Bb_Yld HIGH, d3(Eps) HIGH (the
ES-D2 corner read re-expressed under these rules for the one table). CELLS (8), one
per companion. PRIOR: momentum + quality + low-vol + Bb_Yld COMPLEMENTARY [AMP,
Novy-Marx, H36 h3, shareholder-yield LIT + the booked QG-D2 c9 cheap-quality print];
low-leverage COMPLEMENTARY (trap logic); growth REDUNDANT-to-ANTAGONISTIC (the
extrapolation error IS the harvest); d3 NOT complementary (ES-D2 booked — this cell
formalizes it); turnover genuinely two-sided. Census 8 on the day.

## Entry VAL-D3 (2026-09-10) — PRE-REGISTERED before running: VALUE-TRAP ANATOMY.
Among CHEAP names (Pb Q1, per date), split by each trap marker and print the
good-half minus bad-half fwd-12m and fwd-36m EW ann difference. Markers (bad side):
Debtequity HIGH, d12(Eps) FALLING (Eps rank at t minus t-12 below median),
Vol1Y HIGH, Roe LOW, Share_Turn_12M HIGH. CELLS (5), one per marker; the verdict is
the RANKING by 12m difference with the 36m persistence check. PRIOR: leverage and
falling-EPS the two biggest trap markers [Piotroski/distress LIT]; low-ROE third;
if NO marker clears +2.00 at 12m, "cheap is cheap" and trap-filtering is
narrative on this panel — booked either way. Census 5 on the day.

## Entry VAL-D4 (2026-09-10) — PRE-REGISTERED before running: FACTOR-LEVEL VALUE
COMPLEMENTARITY (factors_us FF6 monthly 1963-2020, VW — the construction free of the
panel's EW junk). CELLS (5): b1 the correlation row — corr(HML, x) monthly for
UMD/RMW/CMA/SMB/MktRF; b2 50/50 HML+UMD blend — ann mean, vol, Sharpe vs each alone
(monthly rebal); b3 50/50 HML+CMA (the redundancy test — CMA-as-value-in-drag);
b4 50/50 HML+SMB; b5 the crash read — worst 12m of HML alone vs HML+UMD (does the
blend truncate the value winter). The booked HML+RMW blend (QG-D2: 0.49 vs
0.32/0.41) is QUOTED, not re-run. PRIOR: corr(HML,UMD) negative [AMP LIT] and the
blend Sharpe beats both; corr(HML,CMA) strongly positive (>= +0.5) making b3 ~no
improvement (REDUNDANT); SMB adds nothing; the blend's worst-12m materially
shallower than HML's own. Census 5 on the day.

## Entry VAL-D5 (2026-09-10) — PRE-REGISTERED before running: DOES VALUATION PRICE
THE FLOOR? The distributional read the ER battery never printed. Shiller monthly
1881-2023: CAPE (PE10) expanding terciles (min 240m, lagged 1m); next-5y REAL total
return (Real Price + Real Dividend, annualized, overlapping FLAGGED). CELLS (3):
d1/d2/d3 = the CHEAP / MID / EXPENSIVE tercile's next-5y distribution — p10 / p50 /
p90. PRIOR (two-sided, written against our own ER-D1c demotion which is QUOTED):
the MEDIAN gap is expected to be null-consistent (no new timing claim will be made
regardless); the registered question is the p10 FLOOR — prior: cheap-tercile p10
exceeds expensive-tercile p10 by >= 2pp/yr (valuation prices the downside band even
where it cannot forecast the mean). If the floor gap < 2pp/yr, valuation loses even
its band role at the index level and stays ONLY an expectations qualifier
(ER-D7's corner). Census 3 on the day.

## Entry VAL-D1 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_val.py + es_sc_matrices/val.json) — P/B LEADS THE LADDER; THE
COMPOSITE TIES IT; THE "MODERN MEASURES" PRIORS MISSED ON THIS PANEL. Spreads
(cheap-minus-expensive, EW ann; 1m/12m/36m/szQ5-12m): Pb +16.08/+14.58/+8.37/**+8.80**;
Pe +4.12/+3.53/+2.70/+3.07; Ev_Ebitda +3.13/+3.24/+1.80/+4.94; Fcf_Yld
+0.59/-0.44/+1.47/+3.77; Div_Yld -4.09/-4.55/+0.42/**+5.10**; Bb_Yld
-2.59/-3.63/-1.18/+0.91; COMPOSITE +8.80/+8.60/+6.30/**+8.97**. v8 ladder (szQ5
12m): COMPOSITE ~ Pb > Div_Yld > Ev_Ebitda > Fcf_Yld > Pe > Bb_Yld. GRADE: the
FCF-yield and Ev>=Pb priors MISSED; the composite>=best-single claim lands as a TIE
(+8.97 vs +8.80 — no material composite premium once Pb is in it); the Div_Yld
SPLIT is the teaching print — negative at panel (-4.6: in small caps high yield =
distress/no-growth, the QG-D1 payout-state confound live) but +5.10 in large caps
(where yield means discipline). CAVEAT: Pb's panel dominance partly rides the junk
bounce (Pb Q1 = beaten-down); the szQ5 column is the honest rank and there Pb still
leads. CONSUMPTION: the desk's cross-sectional value instrument stays Pb-led with
an Ev/FCF composite as robustness, never Bb_Yld; measure choice re-derives on India
PIT data. Census 8 (1202 -> 1210).

## Entry VAL-D2 + VAL-D3 RESULT (2026-09-10, booked together — the same mechanism
owns both) — THE FROZEN RULES FIRED, AND WHAT THEY CAUGHT IS THE PANEL, NOT THE
DOCTRINE: WITHIN-CHEAP CONDITIONING IS UNMEASURABLE ON A NO-DELISTING PANEL.
VAL-D2 prints (WCS/VSC/szQ5-WCS -> rule verdict): Roe -15.43/+13.38/-9.13;
Mom -15.89/+12.88/-8.20; Vol(low) -21.36/+13.44/-8.87; lowDebt -3.14/+14.82/-8.44;
lowTurn -7.19/+14.57/-9.13; Gr -9.45/+12.46/-6.66; Bb_Yld -5.10/+14.38/-1.88 — ALL
"SUBSUMING/ANTAGONISTIC" by rule; d3 -1.33/+14.34 REDUNDANT. VAL-D3 prints
(good-minus-bad among Pb Q1, 12m/36m): lowDebt -1.80/-1.77; risingEPS -2.69/-0.97;
lowVol **-17.79**/-4.31; highROE -11.64/-4.17; lowTurn -4.99/+1.55 — every trap
filter NEGATIVE at 12m. INTERPRETATION (the honest one): within the cheap bucket of
an EW panel with NO deaths, the deep-distress corner mechanically outperforms —
its casualties were deleted, so "traps" cannot spring and every filter that removes
distress removes the survivor bounce instead. This is SC-D3a a3's lesson at stock
level: the WCS/trap side of the complementarity program is UNMEASURABLE here, and
the rule verdicts are booked as ARTIFACT-DRIVEN, not as doctrine (the szQ5 WCS
agreeing in sign extends the caveat into large caps on this panel — its selection
filter applies there too). WHAT SURVIVES CLEANLY: the VSC column — the VALUE SPREAD
IS +12.5 to +14.8 WITHIN EVERY companion quintile family, the single most robust
cross-sectional fact on this panel (value is not subsumed by quality, momentum,
vol, leverage, turnover, growth, payout, or revisions). CONSUMPTION: (i) VSC
robustness -> one edge-list line; (ii) the within-cheap complementarity and
trap-filter questions MOVE to the India PIT panel (delisted_registry + the P5
promoter-pledge marker are exactly what this panel lacks) — a design brief, to be
registered on arrival; (iii) QG-D2 c9 stands unchanged (it is a VSC-type fact,
consistent with today's print). Census 13 (1210 -> 1223).

## Entry VAL-D4 RESULT (2026-09-10, interpretation after the print) — VALUE+MOMENTUM
IS THE COMPLEMENT (VW, ARTIFACT-FREE); CMA IS VALUE IN DRAG; THE BLEND'S TAIL IS NOT
TRUNCATED. Prints (FF6 VW 1963-2020): b1 corr(HML, x): UMD **-0.21**, RMW +0.07,
CMA **+0.68**, SMB -0.04, Mkt -0.22. b2 50/50 HML+UMD Sharpe **0.70** vs HML 0.32 /
UMD 0.54 (+5.52%/yr) — the AMP prior HIT decisively; with QG-D2's booked HML+RMW
0.49, the value book's complements are MOMENTUM first, PROFITABILITY second.
b3 HML+CMA 0.41 vs CMA alone 0.46 — no gain, corr +0.68: CMA is largely value
repackaged (REDUNDANT, as registered). b4 HML+SMB 0.40 — diversification crumbs.
b5 PRIOR MISSED: worst-12m HML alone -35.1% vs blend **-37.4%** — the blend does
NOT truncate the tail (the momentum-crash and value-winter events are its own
tails); complementarity is a SHARPE fact, not a crash-protection fact — sizing and
the drawdown governor still own the tail. CONSUMPTION: the future India stock
book's factor pairing doctrine = value x momentum x moderate-quality, with tail
risk handled by the risk ladder, never by the blend itself. Census 5 (1223 -> 1228).

## Entry VAL-D5 RESULT (2026-09-10, interpretation after the print) — VALUATION
PRICES THE FLOOR: THE p10 GAP CLEARS ITS BAR. Prints (CAPE expanding terciles ->
next-5y REAL TR ann, 1901-2018 windows, overlapping FLAGGED): CHEAP p10 **-2.00** /
p50 +8.88 / p90 +20.97 (n=557); MID -2.45/+7.50/+16.62; EXPENSIVE p10 **-4.92** /
p50 +5.10 / p90 +13.97 (n=627). Floor gap +2.92pp/yr >= the +2.00 bar — PASS. The
whole distribution shifts, not just the mean: cheap starts raise the floor, the
median AND the ceiling. CAVEATS, stated: the ER-D1c persistent-regressor demotion
is quoted and NOT overturned — a quantile shift under overlapping windows inherits
the same null-band concern (a quantile-level null test is a legitimate future
design, not run here); therefore consumption stays exactly where the doctrine
already sits: valuation as a STATE that widens/narrows the expected BAND (floor
included) for expectations and risk budgets — never a timing signal. This print
gives the band role its first registered numeric content. Census 3 (1228 ->
**1231**).

## Entry VAL-D6 (2026-09-10) — PRE-REGISTERED before running: THE EXTENDED MEASURE x
SIZE x HORIZON ATLAS (principal: "P/S and mixing stuffs and largecap vs smallcap
which works"). DATA HONESTY FIRST, recorded now: TRUE P/S is NOT constructible on
the US firm panel — its fields are cross-sectionally uniformized ranks, so
mcap/sales cannot be rebuilt (rank of ratio != ratio of ranks); Sales_Ps is
sales-PER-SHARE rank, not a valuation multiple, and is EXCLUDED as a measure. P/S
joins the India design set (P1 revenue + shares_outstanding + price = PIT P/S).
Conventions inherited verbatim (dec(), EW, 1m x1200 / 12m x100 / QG-D3 36m
compounding). SIZE HALVES: small = szQ1-2, large = szQ4-5 (dec of Mkt_Cap_12M).
CELLS (14): x1-x7 the measure ladder BY SIZE HALF at 1m/12m/36m for Pb, Pe,
Ev_Ebitda, Fcf_Yld, Div_Yld, Bb_Yld, and NEW Ebit_Bv (EBIT/book — FLAGGED at
registration as a value-quality HYBRID, not a pure multiple: if it tops the ladder
it does so by mixing in profitability, and it is graded as a MIX, not a measure);
x8-x13 the MIXES, same profile: VAL2 = Pb+Pe rank-mean; VAL3 = Pb+Ev_Ebitda+
Fcf_Yld (the VAL-D1 composite, now sized/horizoned); VAL4 = VAL3+Div_Yld;
CQ = Pb+Roe rank-mean (cheap-quality); VM = Pb+Mom_11M rank-mean (value-momentum);
VLV = Pb+lowVol rank-mean; x14 the verdict table — per size half, the best measure
and best mix at each horizon. PRIORS (two-sided): every pure measure prints larger
in SMALL (the junk bounce inflates the cheap side) — the LARGE half is the verdict
column as established; in LARGE at 12m/36m the MIXES beat pure Pb (the factor-level
0.70/0.49 precedent says CQ and VM should top the table — the KEY registered
question; note the VAL-D2 caveat: mix spreads on this panel are measured
across-the-board sorts, NOT within-cheap conditioning, so they are NOT subject to
yesterday's within-cheap artifact in the same way, but the no-delisting flattery
still applies to levels); Ebit_Bv strong-but-hybrid (the mixing lesson made
explicit); Div_Yld's large-cap strength (VAL-D1 +5.10) persists at 36m. Runner: a
Sonnet agent on this frozen spec, desk-verified before booking. Census 14 on the
day.

## Entry VAL-D6 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_val_d6.py + es_sc_matrices/val_d6.json; Sonnet agent on the frozen
spec, desk-verified: large Pb 12m +7.30 reproduced independently to the cent) —
P/B OWNS BOTH HALVES; THE PURE-VALUATION COMPOSITE BEATS IT IN LARGE CAPS; SIGNAL-
MIXING FAILS WHERE ITS INGREDIENT IS BROKEN. Measures (small 1m/12m/36m | large):
Pb +16.56/+14.83/+7.69 | **+7.15/+7.30/+5.39**; Pe +2.4/+2.5/+1.1 | +3.7/+3.5/+3.0;
Ev_Ebitda -1.9/-0.6/-0.2 | +3.1/+3.7/+1.7; Fcf_Yld -2.6/-3.1/+0.4 | +2.8/+2.9/+3.1;
Div_Yld **-10.9/-11.6/-2.6 | +3.4/+3.9/+3.5**; Bb_Yld -3.6/-5.3/-1.9 | +4.1/+1.6/
+1.2; Ebit_Bv **-22.1/-19.5/-5.6 | +0.3/+0.8/-0.9**. Mixes: VAL2 +6.0/+5.1/+3.3 |
+7.6/+7.2/+5.2; **VAL3 +3.0/+4.1/+3.5 | +8.76/+7.80/+5.88 — the LARGE-half winner
at every horizon, beating pure Pb (+7.15/+7.30/+5.39)**; VAL4 (adds Div_Yld)
slightly worse than VAL3 in large; CQ -3.9/-6.4/-0.3 | +4.5/+3.0/+2.9;
VM -5.1/-8.2/-1.7 | **-1.2/-0.5/+1.5**; VLV -15.1/-12.7/-1.0 | +2.1/+2.6/**+5.6**.
GRADES vs the frozen priors: (i) "every pure measure larger in small" PARTIAL MISS —
only Pb inflates in small; every YIELD measure INVERTS there (Div_Yld -11.6,
Ebit_Bv -19.5: in small caps the high-yield/high-profitability side is the
NON-distressed side, and the no-delisting bounce pays distress) — the small half
inflates the low-price side specifically, not "value" generally. (ii) THE KEY
QUESTION SPLIT: the pure-valuation mix (VAL3) DOES beat Pb in large at every horizon
(the composite premium exists where sector/measure noise can be averaged) — but CQ
and VM do NOT top the table (MISS): stock-level rank-blending of momentum/quality
into value FAILS on this panel because its momentum leg is artifact-inverted (SC-D4
booked -9pp large) — a broken ingredient breaks the mix. The factor-level pairing
doctrine (HML+UMD 0.70, VW) is NOT contradicted; the lesson is LEVEL-SPECIFIC:
blend at the SLEEVE level (factor portfolios), do not rank-mix signals at the stock
level until the India PIT panel can measure the ingredients cleanly. (iii) Ebit_Bv
"strong-but-hybrid" MISSED — it is WEAK-hybrid (its quality leg is fade-flat in
large, QG-D3, and artifact-punished in small). (iv) Div_Yld's large-cap persistence
at 36m ✓ (+3.5). (v) VLV at 36m large (+5.6 ~ VAL3's +5.9) — the low-vol 3y
emergence (H36 h3) shows up inside a mix too; noted, not consumed (same panel
caveats). CONSUMPTION: the desk's cross-sectional valuation instrument = the
pure-valuation composite (Pb + Ev_Ebitda + Fcf_Yld ranks) in large caps, Pb alone
acceptable; signal-mixing deferred to sleeve level; P/S + margin-adjusted P/S +
within-industry forms all India-gated as registered. Census 14 (1231 -> **1245**).

## Entry TECH-D1 (2026-09-10) — PRE-REGISTERED before running: THE ATH & DRAWDOWN-
STATE BATTERY (Track TECH opens on principal directive: technicals — ATH, stages,
momentum conditions, market-valuation regimes; sector RS is DATA-GATED on the
Priority-1 NSE sectoral TR pull — design brief in the dossier; leverage is QUOTED
(QG-D2 c12, DB battery; margin-debt series not freely vaulted); index ratios QUOTED
(T3 rotation FAIL, SC series)). Data: NIFTY Adj Close daily 2007-2026; Shiller Real
Price + Real Dividend monthly 1871-2023 (real TR as VAL-D5); gold monthly 1833-2026
(nominal, stated). CELLS (6): a1 NIFTY drawdown-from-running-max, expanding terciles
(min 750 trading days, lagged 1d) -> fwd-12m TR by tercile (overlap FLAGGED);
a2 Shiller NEW-ATH months (real TR index at running max — parameter-free) -> next-12m
real TR mean + P(negative) vs all other months; a3 NIFTY 52w-high proximity
(close/max252 — the documented 52-week convention), expanding terciles -> fwd-12m;
a4 gold a2-analog (new nominal ATH month -> next-12m); a5 Shiller BREAKOUT events —
first new ATH after >= 24 months without one (the two-year base convention,
Weinstein [LIT]) -> next-12m vs unconditional; a6 NIFTY deep-drawdown tercile ->
fwd-36m (the entry-state read at the 3y horizon). PRIOR (two-sided): ATH-zone/new-ATH
months are NOT below-average forward (the "don't fear the high" claim [LIT]) — if
they underperform materially the buy-at-close deployment doctrine gains a registered
caveat; deep-drawdown terciles best forward (entry-state doctrine, F2/CU-D4
precedent); a5 breakouts positive vs unconditional. Census 6 on the day.

## Entry TECH-D2 (2026-09-10) — PRE-REGISTERED before running: STAGE QUADRANTS AS
STATES, NEVER RULES. COLLISION GUARD QUOTED NOW: T-CTRL1 killed the BLL MA family
as TRADING RULES (0/10 net) and T2 killed trend-on-states at both bands — this entry
promotes NOTHING; it maps mechanical stage states to forward return AND vol
(regime description; any consumption is Tier-C risk-state at most). States: the four
(price vs MA) x (MA slope) quadrants — MA = 200-day (NIFTY daily) / 10-month
(Shiller, gold), the documented Faber/Weinstein conventions [LIT]; slope = MA today
vs 21 trading days (1 month) ago; labels S2~(above,rising), S4~(below,falling),
S3~(above,falling), S1~(below,rising), lagged one bar. CELLS (5): s1 NIFTY fwd-1m
ann mean AND realized-vol by quadrant; s2 NIFTY fwd-12m by quadrant; s3 Shiller
fwd-12m real TR by quadrant (1881-2023); s4 gold fwd-12m by quadrant; s5 the
technical x valuation cross — Shiller quadrant x CAPE expanding tercile: the four
corners S2-cheap / S2-expensive / S4-cheap / S4-expensive -> fwd-12m real TR.
PRIOR (two-sided): quadrants rank VOL reliably (S4 highest) even if mean-ranking is
weak — the desk's vol-not-return trend doctrine (T2/F2); S2 highest mean is the
folk claim, tested not assumed; s5 prior: S4-expensive the worst corner; if
quadrants fail even to rank vol, the stage frame dies entirely at index level.
Census 5 on the day.

## Entry TECH-D3 (2026-09-10) — PRE-REGISTERED before running: THE MOMENTUM
CONDITION MAP (when momentum works, when it crashes, when to switch). Data: UMD
(ff_momentum_monthly 1927-2024); IIMA WML + MF + RF monthly 1993-2025; CBOE VIX
daily 1990-2026 (monthly mean); firm_panel Mom_5M/Mom_11M/Mom_Sharp_* columns.
States lagged one month throughout; expanding terciles min 120m. CELLS (10):
m1 UMD mean in post-bear state (trailing-24m market TR < 0) vs otherwise
[Daniel-Moskowitz LIT]; m2 UMD by VIX-level tercile (1990-2024); m3 factor
momentum — sign of trailing-12m UMD -> next-12m UMD (overlap FLAGGED); m4 THE
CRASH/SWITCH CELL — UMD in (post-bear AND top VIX tercile) vs all other months,
plus the three worst UMD months listed with their state flags; m5-m7 India WML
analogs of m1-m3 (market = MF+RF; vol state = trailing-12m realized vol of the
market series, expanding terciles — full 1993-2025 coverage); m8 India crash cell
(post-bear AND top-vol) + worst-3 WML months with flags; m9 stock-level lookbacks —
Mom_11M vs Mom_5M decile D10-D1 at fwd-1m/12m, panel AND szQ5 (the SC-D4 momentum-
inversion artifact QUOTED: levels are non-evidence; only the RELATIVE 11M-vs-5M
comparison is read); m10 vol-scaled momentum — Mom_Sharp_11M vs Mom_11M, same reads
(the Barroso-Santa-Clara scaling question at stock level [LIT]). PRIOR (two-sided):
m1/m5 momentum degraded post-bear; m2 worse in top-VIX tercile; m4/m8 the crash
state strongly negative — IF the state prints <= -10%/yr worse than baseline in
BOTH markets, a momentum stand-down monitor (post-bear + top-vol tercile) becomes
REGISTRABLE for the future India factor sleeve (Tier-C, reduce-only — consistent
with the T-series doctrine); m3/m7 factor momentum positive [Ehsani-Linnainmaa
LIT]; m9 11M >= 5M in szQ5 (the 12-1 standard); m10 Sharp variants strictly less
negative than raw on this panel — if vol-scaling FLIPS the panel momentum sign,
that is the panel's momentum lesson (scaling defeats part of the artifact).
Census 10 on the day.

## Entry TECH-D4 (2026-09-10) — PRE-REGISTERED before running: VALUATION-REGIME
PERSISTENCE (the "valuation clustering" question made mechanical). Shiller CAPE
1881-2023, expanding terciles (min 240m, lagged — the VAL-D5 construction quoted).
CELLS (4): c1 the monthly transition matrix cheap/mid/expensive -> next month
(P(stay) per state); c2 spell durations — median and mean months per uninterrupted
tercile spell; c3 P(same tercile 12m ahead); c4 the transition-return read —
fwd-12m real TR in the first 12m after a downgrade flip (expensive -> mid/cheap
entry) vs after an upgrade flip (cheap -> mid/expensive) vs unconditional.
PRIOR: P(stay) > 0.95 monthly and spells run YEARS (valuation is a slow clustered
state — the clustering answer); the de-rating transitions carry the damage
(post-expensive-exit months print below unconditional because exits happen BY
price falling); if spells are short/noisy the "state" framing itself weakens.
Census 4 on the day.

## Entry TECH-D1 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_tech.py + es_sc_matrices/tech.json; Sonnet agent, desk-verified —
TECH-D3 m1 reproduced to the cent; the runner's two ambiguity resolutions are
ACCEPTED and recorded: s1 vol = FORWARD 21d realized; m9 read as panel + szQ5
D10-D1) — ATHs ARE NOT TO BE FEARED, AND THE ENTRY STATE KEEPS WINNING. Prints:
a1 NIFTY drawdown terciles -> fwd-12m: LOW +9.16 / MID +14.41 / HIGH **+33.66**
(n=211, mostly 2008-09+COVID — stated); a2 Shiller new-ATH months +9.46% next-12m
vs +8.29 others, P(neg) 28.1 vs 31.7 — the don't-fear-the-high prior HIT (ATH
months slightly BETTER than average); a3 52w-high proximity: LOW +21.53 / MID
+13.63 / HIGH +10.00 — at INDEX level proximity ranks INVERSELY (this is NOT the
George-Hwang cross-sectional effect [LIT], which remains untested here); a4 gold
ATH months +3.80 vs +3.78 — nothing; a5 breakouts after >=24m bases: +9.34 vs
+8.57 unconditional (n=15) — the folk breakout edge does NOT show at index level;
a6 the 3y read: HIGH-drawdown entry +21.54%/yr ann over 36m vs LOW +10.42.
GRADE: both registered priors HIT (ATH-zone not below average; deep drawdown best
forward) — with the nuance that a3's proximity ladder makes the buy-at-close
doctrine caveat UNNECESSARY (ATH months are fine in absolute terms) while
re-confirming that drawdown states are where the entry premium lives (F2/CU-D4
doctrine, third asset class). CONSUMPTION: none new — the entry-state doctrine
gains two more prints. Census 6 (1245 -> 1251).

## Entry TECH-D2 RESULT (2026-09-10, interpretation after the print) — THE STAGE
FRAME SURVIVES AS A RISK STATE AND DIES AS A RETURN RULE FOR EQUITIES — AND GOLD IS
THE EXACT OPPOSITE; THE s5 CORNER IS THE ARC'S KEEPER. Prints: s1 NIFTY fwd-1m ann /
fwd-21d vol: S1 +21.3/18.2 | S2 +6.8/**13.7** | S3 +27.9/18.6 | S4 +18.4/**26.3** —
the VOL prior HIT exactly (S2 calmest, S4 wildest); the RETURN folk claim INVERTED
(S2 lowest forward mean). s2 NIFTY fwd-12m: S4 **+32.2** / S3 +26.4 / S1 +11.0 /
S2 +9.2 — stage-4 clusters at bottoms; the index mean-reverts (one market, strong
recoveries — stated). s3 Shiller: S3 +13.6 / S4 +10.6 / S2 +7.9 / S1 +2.6 (milder,
same direction). s4 GOLD INVERTS THE INVERSION: S2 **+11.3** / S3 +5.3 / S1 +1.9 /
S4 **+0.55** — gold is the trending asset (TS1's 12m-slow doctrine re-confirmed by
an independent construction); equities at index level are rebound assets. s5 the
technical x valuation corners (Shiller): S4-CHEAP **+14.65** / S2-CHEAP +10.91 /
S2-EXPENSIVE +6.22 / S4-EXPENSIVE **+0.27** (n=110) — the falling knife is ONLY the
expensive one: a downtrend is an entry state when cheap and dead money when
expensive. GRADE: vol prior HIT; S2-highest-mean folk claim REFUTED for equities,
CONFIRMED for gold; s5 prior HIT (S4-expensive worst). CONSUMPTION (Tier-C state
reads, no rule): (i) stage quadrants enter the regime notes as a VOL state (S4 =
26% vol regime); (ii) the s5 corner read joins the playbook — index downtrends are
entries only from cheap valuation states; (iii) gold sleeve trend-persistence
re-confirmed. T-CTRL1/T2 stand untouched — nothing here is a trading rule.
Census 5 (1251 -> 1256).

## Entry TECH-D3 RESULT (2026-09-10, interpretation after the print; m1 desk-
verified to the cent) — THE MOMENTUM CONDITION MAP PRINTS CLEAN, AND THE STAND-DOWN
GATE **FIRES IN BOTH MARKETS**. Prints: m1 US UMD post-bear **-9.30**%/yr vs +10.64
other; m2 by VIX tercile: LOW +6.68 / MID +10.04 / HIGH **-9.73**; m3 factor
momentum FAILED (+6.89 after UMD-positive years vs +8.43 after negative — single-
factor own-momentum adds nothing; Ehsani-Linnainmaa is CROSS-factor [LIT], not
this); m4 the US crash state (post-bear AND top-VIX) **-22.48%/yr (n=44)** vs
+8.55 — worst months 1932-08 (-52.6), 1932-07 (-45.7), 2009-04 (-34.3), all
post-bear as [DM LIT] says; m5 India WML post-bear +9.81 vs +14.49 (degraded but
POSITIVE — India momentum more robust post-bear than US); m6 India by vol tercile:
LOW **+20.02** / MID +2.37 / HIGH **-7.21** — the vol state is India's dominant
momentum conditioner (27pp LOW-to-HIGH; tercile n's 188/24/42 reflect the
expanding-history classification of India's secularly-declining vol — caveat
stated); m7 India factor momentum INVERTED (+12.50 after positive years vs +23.45
after negative — WML rebounds after its own bad years; chasing WML strength is the
mistake); m8 the India crash state **-27.46%/yr (n=15)** vs +15.06 — worst months
2001-11, 2009-05, 2000-04. THE REGISTERED GATE: both markets print the crash state
>= 10pp/yr below baseline (US -31pp, India -42.5pp) -> **the momentum stand-down
monitor (post-bear + top-vol tercile, Tier-C reduce-only) is now REGISTRABLE for
the India factor sleeve** — spec in the dossier's design brief; config wiring
happens when the sleeve exists (challengers.yaml lane, validator-gated). m9
lookbacks: the panel artifact owns both (11M -17.6/-21.1 panel, -11.4/-11.2 szQ5;
5M less negative everywhere) — the registered 11M>=5M prior is UNGRADEABLE as
levels are non-evidence (SC-D4 quoted); the honest read: the reversal artifact
punishes LONGER formation harder, so even the relative comparison is contaminated —
the lookback question stays answered ONLY at index level (TS1: 3m India equity,
12m gold) and goes to India PIT at stock level. m10 vol-scaling MITIGATES but does
not flip (-15.9 vs -17.6 panel 1m; -9.0 vs -11.2 szQ5 12m) — the flip branch not
reached. Census 10 (1256 -> 1266).

## Entry TECH-D4 RESULT (2026-09-10, interpretation after the print) — VALUATION
CLUSTERS IN YEARS-LONG SPELLS, AND THE DAMAGE LIVES IN THE DE-RATING TRANSITIONS.
Prints: c1 monthly P(stay): CHEAP 0.97 / MID 0.87 / EXPENSIVE 0.98 (prior >0.95
HIT for the extremes; MID is a corridor, not a state); c2 spells: EXPENSIVE median
16.5m mean 42.9m, CHEAP median 7m mean 37.1m — the means carry multi-year regimes;
c3 P(same tercile 12m later): 0.84 / 0.36 / 0.85; c4 the transition returns:
first 12m after flipping OUT of expensive **-7.21%** vs unconditional +8.57 vs out
of cheap **+16.51** (n=15 each, overlap flagged) — de-rating exits happen BY
falling and keep falling ~a year; re-rating exits keep rising. GRADE: both priors
HIT. CONSUMPTION: the clustering answer for the principal — valuation is a slow,
years-long state (which is WHY it cannot be a clock and CAN be a band/floor
instrument, VAL-D5/ER-D1c consistent); the transition asymmetry is a context line
for the regime notes (a fresh de-rating is not yet an entry; the cheap-exit rally
is real). Census 4 (1266 -> **1270**).

## Entry MOM-D1 (2026-09-10) — PRE-REGISTERED before running: THE STOCK-LEVEL
LOOKBACK ANATOMY ACROSS REGIMES (principal clarification: short 3-6m formation vs
long 6-12m in STOCKS, by regime — supersedes TECH-D3 m9's "ungradeable" with clean
constructions; m9's verdict quoted, not overwritten). CONSTRUCTION (frozen): US —
formation returns built from the R1M pivot itself, NOT the uniformized Mom columns;
window semantics in rows of the forward-return pivot (row t = the forward month):
3-1 = rows t-3..t-1 (no skip), 6-1 = t-6..t-1, 6-2 = t-6..t-2 (skip-month), 12-2 =
t-12..t-2, 12-7 = t-12..t-7 (Novy-Marx intermediate [LIT]); log1p sums; deciles per
date; EW fwd-1m x1200; large half = size Q4-5. India — the survivor panel's monthly
return matrix (SC-D3a construction quoted), same window semantics with fwd = next
calendar month; EW; tradeable half = top ADV tercile. REGIMES (lagged 1m): US market
state = sign of trailing-12m FF market TR; US vol = monthly-mean CBOE VIX expanding
terciles min 120m; India market state = sign of trailing-12m NIFTY TR; India vol =
monthly-mean India VIX terciles 2010-2021 (FULL-SAMPLE cut, FLAGGED — short span).
ONE-WAY RULE, argued and frozen now: EW no-delisting bias FLATTERS loser rebounds
and therefore DEPRESSES momentum spreads on BOTH panels — a POSITIVE momentum
spread is admissible evidence (it survives a bias working against it); a negative
one is non-evidence (SC-D4/TECH-D3 m9 quoted). CELLS (18): L1a-e the US lookback
ladder — D10-D1 fwd-1m for the five windows, panel + large half; L2a spreads by US
market state (up/down) for 6-2 and 12-7 + the (12-7 minus 6-2) difference per
state; L2b same by VIX tercile; L2c the stress-diff verdict — does the long-minus-
short difference FALL in down/high-vol states (the staleness mechanism [DM LIT]);
L3a era halves (1999-2009 / 2010-2019) for 6-2 and 12-7; L3b the size read (already
per-cell large halves; this cell = the small-vs-large lookback ordering); L4a-e the
India lookback ladder (five windows, full + top-ADV tercile); L5a India spreads by
market state; L5b India by VIX tercile (2010-21, flagged); L6 the verdict table —
best lookback per market x regime. PRIORS (two-sided): US large-half 12-2 >= 6-2
unconditionally [LIT]; 12-7 vs 6-2 genuinely open (Novy-Marx vs Goyal-Wahal [LIT]);
THE REGIME PRIOR: long lookbacks degrade MORE in down-market/high-vol states (the
stale-formation mechanism — after regime flips the 12m window still holds the old
regime's winners), so the (12-7 - 6-2) diff falls under stress; India positive
despite the bias (IIMA WML +14-15%/yr factor precedent) with the 6-month window
relatively stronger [India-lore, LIT LOW CONF]; if India prints negative everywhere
the read is non-evidence and the question is fully PIT-gated. Runner: Sonnet on
this frozen spec, desk-verified before booking. Census 18 on the day.

## Entry MOM-D1 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_mom_d1.py — built from RAW formation returns, not the panel's
Mom_* columns, per the frozen spec; desk-verified independently on two cells:
US 3-1 panel -10.9954 vs script -11.00, India 6-2 up-state +20.9905 vs +20.99;
one implementation bug found and fixed pre-verification — window_sum() closed
over the wrong array on first pass, caught because the India ladder printed all-
NaN, corrected before any number was read) — THE ARTIFACT CLOSES THE US QUESTION
AGAIN; INDIA'S SURVIVOR PANEL GIVES A CLEAN, ADMISSIBLE, ACTIONABLE ANSWER: 6-2
FORMATION, SHORTEN INTO VOLATILITY. Prints: L1a-e US ladder D10-D1 (panel | large,
%/yr): 3-1 -11.00|-7.40; 6-1 -14.41|-13.71; 6-2 -13.60|-9.54; 12-2 -19.02|-12.82;
12-7 -12.61|-5.68 — ALL NEGATIVE, both cuts, every window: non-evidence per the
one-way rule (SC-D4/TECH-D3 m9 confirmed a third time, independent construction).
L2a by market state: 6-2 down -7.68/up -19.66; 12-7 down -11.20/up -14.10; diff
(12-7-6-2) down -3.52 / up +5.56 — the registered "long degrades more when down"
prior HITS at the down-state cut only and REVERSES at the up-state cut. L2b by
VIX tercile: 6-2 LO -9.61/MID +1.16/HI -37.68; 12-7 LO -6.97/MID -6.94/HI -26.66 —
HI-vol amplifies BOTH (the crash mechanism visible even inside the artifact,
[DM LIT] pattern), but here it is the SHORTER window (6-2) that degrades MORE in
the vol cut, opposite the market-state cut's direction. L2c the stress-diff
verdict: MIXED, not clean — which lookback "degrades more" under stress depends
on which regime variable is used; no single mechanism confirmation survives both
cuts on this artifact-inverted data. L3a era halves: 6-2 -14.57 (99-09) / -12.50
(10-19); 12-7 -16.44 (99-09) / -8.52 (10-19) — the 12-7 distortion shrinks sharply
in the calmer decade. L3b the skip-month note: 6-1 (no skip) is the WORST window
in BOTH cuts (-14.41 panel / -13.71 large) — worse than its skip-month sibling 6-2
in both — a mechanistic corroboration of the skip-month convention [LIT] that
survives even though the overall sign is artifact (this is a construction
comparison, not a momentum-exists claim). US VERDICT: ungradeable as ordering
evidence (TECH-D3 m9's ruling extended); the index-level answer (TS1: 3m NIFTY,
12m gold) is what stands.
INDIA (admissible — a positive spread survives a bias that depresses it): L4a-e
ladder (full | top-ADV, %/yr): 3-1 +9.65|**-1.41**; 6-1 +14.70|+5.59; **6-2
+15.59|+5.87 — THE PEAK, BOTH CUTS**; 12-2 +14.38|+5.51; 12-7 +10.74|+5.20. The
top-ADV tercile is flat across 6-1..12-7 (+5.2 to +5.9) but 3-1 flips NEGATIVE
there (-1.41) — short-term reversal, not momentum, in the liquid names [Jegadeesh
1990 LIT], exactly the literature's warning against a no-skip short window. L5a by
NIFTY market state: 6-2 down -7.51/up **+20.99**; 12-7 down -16.70/up +17.20 — a
THIRD independent confirmation (after TECH-D3 m5, m8) of Cooper-Gutierrez-Hameed
[LIT]: India momentum is an up-market phenomenon, now shown at the individual-
stock cross-section rather than the factor series. L5b by India-VIX tercile
(2010-2021, flagged short span): 6-2 LO +26.60/MID +9.87/HI **+5.68** (weakens,
stays positive); 12-7 LO +27.57/MID +7.09/HI **-9.74** (FLIPS NEGATIVE) — the
actionable asymmetry: the LONGER window is the one that breaks under vol stress,
the SHORTER one degrades but survives. GRADE: the registered India prior (positive
despite the bias, 6-month window relatively stronger) HITS cleanly and specifically
— 6-2 is not just "relatively stronger", it is the outright peak in both
constructions and the only window still positive across every VIX tercile.
CONSUMPTION: (i) the India momentum sleeve design defaults to 6-month formation
with a 1-month skip (6-2), never a no-skip short window in liquid names; (ii) a
vol-conditioned SHORTEN rule is now registrable alongside the TECH-D3 stand-down
monitor — in rising India-VIX, shift weight AWAY from the 12-month lookback
toward 6-2, rather than standing down entirely (a refinement to Tier-C, not yet a
promoted rule); (iii) never chase pure 1-month-lagged short-term strength in
India's most liquid names — that pocket is reversal, matching the desk's booked
1m reversal work; (iv) this triangulates TECH-D3's factor-level India finding with
an independent stock-level construction — doctrine strengthens, not double-counted.
Census 18 (1270 -> **1288**).

## Entry SECTOR-GATE (2026-09-10) — NOT A TRIAL, A FORMAL GATE NOTE (principal asked
"does sector RS have any edge/alpha"). No sector/industry tag exists anywhere in the
vaulted data: not in firm_panel (US, no GICS-equivalent column), not in the India
survivor panel (ticker-level only), and no NSE sectoral TR index has been pulled
(RUNSHEET Priority-3 row, principal-machine gated). Moskowitz-Grinblatt (1999)
industry momentum [LIT] and the practitioner RS-rotation literature are dossiered
(tech-dossiers/a) with the registrable India design already specced there. Zero
cells run; zero census impact. STATUS: fully gated, unchanged since Track TECH.

## Addendum to SECTOR-GATE (2026-09-10, literature dossier complete — tech-dossiers/
c-sector-rs-deep-dive.md; zero new cells, zero census impact). Widens the literature
base (Hong-Torous-Valkanov 2007 JFE on industry-momentum transmission speed; Grundy-
Martin 2001 RFS — flagging an OPEN, UNRUN question for the desk's own work: a
meaningful share of L3/N4a's momentum leg COULD be re-expressible as undisclosed
industry momentum, not registered or run, a candidate for a future design, not a
finding) and Indian AMC/thematic-fund practitioner practice (NFO-timing-near-peaks
folklore, IT-as-currency-hedge already FAILED per FUN-D3). THE REVISED VERDICT, cross-
checking the desk's OWN already-booked prints rather than approximating sector data:
"No direct sector-index rotation edge is measurable today (the NSE sectoral TR pull
has not landed); but indirect, one-way evidence already exists that in India, once a
market-stress state is identifiable, the textbook defensive rotation has already
missed its window and cyclicals/financials lead the rebound instead (FUN-D3) —
consistent with the same contemporaneous-versus-forward inversion FUN-D1 establishes
at the country-GDP-phase level and FUN-D2 establishes at the earnings-cycle level.
This finding is booked Tier-C (one-way, survivor-panel, market-proxy states, no cost
model) and is reduce-only per CONTRACT §4: it may inform a de-risking or basket-
avoidance rule, never a positive rotation trade, until the NSE sectoral TR pull lands
and both the survivorship and turnover-cost gaps are closed." SECTOR-GATE ITSELF
STAYS FULLY GATED — this is a cross-check enrichment of the gate note, not a new
trial; zero cells, zero census impact.

## Entry RATIO-D1 (2026-09-10) — PRE-REGISTERED before running: INDEX & COMMODITY
RATIO REGIMES + THE LEVERAGE-TIMING READ (principal: copper/gold, silver/gold,
nifty/gold, smallcap/nifty ratios; when leverage is safer; vol clustering and
risk). VOL-CLUSTERING-REDUCES-RISK IS NOT RE-RUN — it is QUOTED: F2 (percentile
de-risking cut COVID DD 37%->26%), F3a (vol-managed NIFTY cuts maxDD 55%->22% at
-4.9pp/yr, Cederburg-erased in-sample-only), TS1 (3m NIFTY trend the only DD-
control pass), TL-D2 s10 (|r| autocorrelation positive thru 30 lags, vol half-life
NIFTY 82d / smallcap 42d) — the mechanism (autocorrelated |returns|) is what makes
any vol-targeting/de-risking rule work at all; nothing here re-derives that.
DATA: copper + gold monthly, IMF PCPS 1980-2017 (Copper) x gold_monthly_1833_2026
(Gold) — overlap 1980-2017; silver+gold ANNUAL 1915-2026 (debt/gold_silver_1915,
authenticated); NIFTY daily 2007-2026; IIMA SMB+MF+RF monthly 1993-2025 (small-
proxy index return = MF+RF+SMB, the standard small-minus-big reconstruction,
flagged as an approximation). CELLS (9): r1 copper/gold 12m-MA-slope state
(rising/falling, lagged 1m) -> next-12m US market TR (FF Mkt-RF+RF) — the "Dr.
Copper" growth-risk-appetite read [LIT]; r2 same state -> next-12m NIFTY TR
(shorter overlap, n stated); r3 silver/gold annual ratio, expanding terciles (min
30y, lagged) -> next-3y gold real-terms return AND next-3y silver return (does a
dear/cheap silver-vs-gold ratio mean-revert); r4 NIFTY/gold ratio (monthly) 12m-MA-
slope state -> next-12m NIFTY-minus-gold relative return (continuation or reversion
— directly actionable for the desk's equity/gold rebalance); r5 NIFTY/gold ratio
expanding percentile (CAPE-style tercile cut, min 120m, lagged) -> next-12m
relative return (a valuation-style mean-reversion read on the SAME ratio, cross-
checking r4's trend read); r6 smallcap/nifty proxy ratio (cumulative small-proxy
index / cumulative NIFTY-equivalent from MF+RF) 12m-MA-slope state -> next-12m SMB
(a LEVEL-based complement to SC-D3's return-based i1 momentum cut); r7 same ratio,
expanding percentile -> next-12m SMB (complementing SC-D3 i2's 36m tercile with a
different construction); r8 THE LEVERAGE-TIMING READ — NIFTY state = (trailing-12m
realized-vol tercile) x (drawdown-from-ATH tercile, both expanding/lagged as in
TECH-D1/D2) -> forward 126-trading-day (6m) max-drawdown by cell, all 9 corners
printed, ranked; r9 vol-clustering IN THE RATIO — autocorrelation of |monthly
Δlog(NIFTY/gold ratio)| at lags 1/3/6/12, plus the half-life (does the ratio
itself cluster, i.e. would a vol-targeted equity/gold tilt have a footing).
PRIORS (two-sided): r1/r2 copper/gold rising -> better forward growth-sensitive
returns [LIT, macro-lore hedge]; r3 the ratio mean-reverts at the extremes (both
sides); r4 the ratio TRENDS (continuation, matching the desk's general "states
persist" doctrine) while r5 the SAME ratio mean-reverts at percentile extremes —
both can be true at different horizons/mechanisms and are reported as printed, not
forced to agree; r6/r7 analogous to r4/r5 for the size ratio; r8 THE KEY QUESTION:
low-vol + low-drawdown (the "calm uptrend" cell) has materially SMALLER forward
max-DD than high-vol + high-drawdown — if the ranking is monotone in vol alone
(drawdown adds nothing), leverage-timing reduces to a pure vol-state rule; r9
clustering present (half-life weeks-to-months), grounding r8's premise. Census 9
on the day.

## Entry RATIO-D1 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_ratio_d1.py; desk-verified independently on two cells — r1 RISING
15.1085 vs script 15.11, r8 HIvol-x-LOWdd 6.3055 vs 6.31 — one date-alignment bug
found and fixed before verification: the IMF copper series uses month-START dates,
gold uses month-END, so the raw ratio was all-NaN until re-indexed) — THE LEVERAGE-
TIMING READ INVERTS THE FOLK INTUITION; COPPER/GOLD WORKS AS A GLOBAL READ, NOT AN
INDIA ONE; BOTH INDEX RATIOS TREND AND MEAN-REVERT AT DIFFERENT CUTS, AS WARNED.
r1 copper/gold 12m-MA-slope -> next-12m US market: RISING **+15.11%** (n=224) vs
FALLING +10.55% (n=212) — the "Dr. Copper" growth-read prior HITS on US data
[LIT confirmed]. r2 the same state -> NIFTY: RISING +10.62% vs FALLING +10.54%
(n=47/71) — flat; global industrial-demand sentiment does not carry an India-
specific edge on this short 1980-2017/2007-2026 overlap — MISS, recorded honestly,
not forced.
r3 silver/gold annual (1915-2026, n=79 obs): LOW(silver dear) -> gold +20.93%/yr,
silver +17.78%/yr (n=16); MID -> +4.82/+4.38 (n=29); HIGH(silver cheap) -> gold
+8.40%/yr, **silver +11.40%/yr** (n=34) — NON-monotone, no clean mean-reversion:
the ratio's own extremes do NOT cleanly predict the next 3 years for either metal;
the LOW-tercile cluster is dominated by the 1970s-80s monetary-metals bull (stated,
not detrended) — booked as a MISS on the two-sided mean-reversion prior; the
annual/n=79 sample is thin for tercile work, flagged.
r4 NIFTY/gold 12m-MA-slope -> next-12m relative return: RISING +3.23% (n=118) vs
FALLING **+5.54%** (n=81) — mild REVERSION, not continuation (prior partially
missed: the trend cut shows the ratio fading, not extending). r5 the SAME ratio by
expanding percentile: MID +27.42% (n=13, thin) vs HIGH **-6.81%** (n=79); LOW
n=0 (the ratio only entered its own historical LOW tercile in the final 4 months
of the sample — no forward window remains, a data-boundary artifact, not a null
result). r4 and r5 AGREE in direction (both show high/rising NIFTY-vs-gold states
giving BACK relative return next year) even though built differently — the
NIFTY/gold ratio is a genuine mean-reverting valuation-style state at the 12m
horizon, complementing the desk's already-booked equity/gold entry-state doctrine.
r6 smallcap/nifty proxy-ratio trend -> next-12m SMB: RISING -2.08% vs FALLING
-2.24% (n=157/203) — no differentiation, consistent with SC-D2's already-booked
era-fragility (the ratio's OWN trend carries no timing signal, corroborating
rather than contradicting). r7 the same ratio by expanding percentile: LOW +5.13%
(n=178) vs MID -4.94% (n=75); HIGH never occurs (0 observations across the full
sample) — because the proxy ratio has a PERSISTENT SECULAR DOWNTREND (it keeps
making new lows against its own history), an independent corroboration, by
construction, of TL-D2's booked -2.9%/yr India smallcap underperformance: the
ratio structurally cannot revisit its own past highs under an expanding cut.
r8 THE LEVERAGE-TIMING READ (9 corners, fwd-126d max-DD, ranked smallest first):
**HIvol x LOWdd 6.31%** (n=121) < LOvol x HIGHdd 6.43% (n=56) < HIvol x MIDdd
6.69% (n=109) < MIDvol x HIGHdd 9.03% (n=82) = LOvol x MIDdd 9.03% (n=666) <
HIvol x HIGHdd 9.18% (n=77) < MIDvol x LOWdd 10.42% (n=414) < MIDvol x MIDdd
10.60% (n=470) < **LOvol x LOWdd 10.70%** (n=1431, the WORST cell). GRADE: the
registered prior (calm-uptrend safest, monotone in vol) FAILS OUTRIGHT — the
SAFEST forward state is HIGH vol + LOW drawdown (post-spike, near-highs — a
V-shaped-recovery signature) and the MOST DANGEROUS is LOW vol + LOW drawdown
(the complacent grind-up, largest n=1431, i.e. the MODAL market state) heading
into its own future drawdown. This is the F2a "2008 shadow" mechanism from the
other direction: calm-and-near-highs is when the NEXT drawdown is least
anticipated and (on this sample) least well-flagged by the vol/DD state pair
itself — the state variables that work for STOP-LOSS timing (F2, TS1) do not
double as LEVERAGE-ADD timing; a low reading on both is not "safe," it is
unremarkable and precedes the average forthcoming drawdown, not the smallest one.
r9 vol-clustering in the ratio: |Δlog(NIFTY/gold)| autocorrelation +0.122 (1m) /
+0.170 (3m) / +0.105 (6m) / +0.102 (12m) — positive at every lag, confirming
clustering; rolling-6m smoothed autocorr(1) = +0.911, informal half-life ~6
months — the ratio's own volatility is a persistent, laddered state, grounding
r8's premise (though r8's own ranking still inverts the naive reading).
CONSUMPTION: (i) copper/gold enters the GLOBAL regime notes as a US/global growth
read, explicitly NOT an India-specific signal (r2 flat); (ii) the NIFTY/gold ratio
joins the equity/gold rebalance toolkit as a 12m mean-reverting state (r4+r5 agree:
fade extension, do not chase a rising ratio) — Tier-C, consistent with T3's prior
kill of ACTIVE equity/gold rotation (this is a rebalance-bias read, not a trading
rule); (iii) the leverage-timing read REFUSES the intuitive "calm and near-highs
is safe" framing — no leverage-timing rule is registered from this print; the
finding is negative and load-bearing (consistent with CONTRACT's no-leverage-
until-funding_rate stance — this result argues for caution about ANY state-
conditional leverage-add rule, not just the funding-rate gate); (iv) silver/gold
stays UNCONSUMED (non-monotone, thin annual sample); (v) the smallcap/nifty ratio's
own trend/level carries no NEW timing signal beyond what SC-D2/D3/TL-D2 already
established — corroboration, not addition. Census 9 (1288 -> **1297**).

## Entry EQ-D1 (2026-09-10) — PRE-REGISTERED before running: THE EARNINGS-QUALITY /
ACCRUAL-DIVERGENCE BATTERY (principal directive: earnings quality + accounting red
flags). DATA HONESTY FIRST: firm_panel's fields (Ni, Ocf, Ta, Op_Margin, Debtequity,
etc.) are ALREADY cross-sectionally uniformized to (0,1] per date (the QG-D2
provenance caveat) — they are RANKS, not dollar values, so a literal Sloan TATA =
(Ni-Ocf)/Ta in dollar terms is NOT constructible here. Every cell below uses a
RANK-DIVERGENCE PROXY (the SAME methodological move already accepted for d3(Eps) in
ES-D1/ES-D2: a difference of per-date-uniformized ranks, not a literal accounting
ratio) and is labeled as such throughout — never presented as the textbook formula.
A DISTINCT ONE-WAY ARGUMENT from VAL-D2/D3, stated now: Sloan's accrual anomaly
predicts high-accrual (earnings-without-cash) firms UNDERPERFORM via a SUBSEQUENT
unwind (restatement, guidance cut, occasionally fraud discovery or distress) — the
worst realizations of THAT mechanism are exactly the delistings this no-delisting
EW panel deletes, so the bias here WEAKENS (understates), never inverts, the
anomaly (opposite direction from the trap-filter cells, which the bias inverted
outright). A negative print, even a modest one, is therefore admissible strong
evidence; a null/positive print is ambiguous (real absence OR a masked real effect)
and is graded as inconclusive, not as a clean miss. CONSTRUCTION: TATA_proxy(t) =
Ni_rank(t) - Ocf_rank(t) (HIGH = earnings rank exceeds cash-flow rank = high-
accrual/low-quality); margin_decline(t) = Op_Margin(t-12) - Op_Margin(t) [GMI-style,
positive = margin worsened]; leverage_increase(t) = Debtequity(t) - Debtequity(t-12)
[LVGI-style]; cash_conversion_proxy(t) = Ocf_Margin(t) - Net_Margin(t) [an
independent field-pairing, the mirror framing of TATA_proxy — a robustness check,
not a second independent finding if it merely mirrors e1]. DATA-GAP STATED NOW:
DSRI (needs receivables), AQI (needs a PP&E/intangibles breakdown) and SGAI (needs
SG&A) are NOT buildable from this panel's 99 fields — the reduced composite below
is missing 3 of Beneish's 8 components; the India handoff (P1) has the SAME gap
(no receivables/PP&E-breakdown/SG&A fields) — flagged as a permanent data ask if
ever wanted. CELLS (8): e1 TATA_proxy deciles -> fwd-1m/12m/36m EW ann D10-D1,
panel + large half; e2 margin_decline deciles -> fwd-12m D10-D1; e3
leverage_increase deciles -> fwd-12m D10-D1; e4 cash_conversion_proxy deciles ->
fwd-12m D10-D1 (mirror-check of e1); e5 THE COMPOSITE (rank-mean of TATA_proxy,
margin_decline, leverage_increase) -> fwd-1m/12m/36m D10-D1, panel + large half;
e6 THE VALUE-TRAP CROSS — among CHEAP stocks (Pb Q1-2, VAL-D3 convention), composite
top-half vs bottom-half -> fwd-12m/36m EW ann (this cell is explicitly FLAGGED as
subject to the SAME within-cheap-conditioning artifact that inverted VAL-D2/D3 —
graded under THAT one-way rule, not e1-e5's); e7 era split of e1 (1999-2009 vs
2010-2019); e8 large-cap-only (szQ5) repeat of e1 at fwd-12m. PRIORS (two-sided,
graded against the STATED bias direction): e1 negative, plausibly SMALLER than the
textbook ~10%/yr Sloan spread given the dampening bias — any negative print is a
HIT; e2/e3 negative [Beneish LIT]; e4 mirrors e1 (positive) as a consistency check;
e5 composite more negative than any single component [Beneish LIT: composites add
power]; e6 the KEY test — if it inverts, that is a THIRD sighting of the within-
cheap artifact (SC-D3a's a3, VAL-D2/D3), not a trap-filter failure — graded as
such; e7 fades in the calmer recent era [McLean-Pontiff-style decay, established
pattern this session]; e8 much weaker/null (the anomaly is historically small-cap-
concentrated [LIT]). India: EVERY cell here is a proxy stand-in for the real design,
which runs on the handoff's actual dollar-value fields (P1: total_assets,
total_equity, total_debt, cash_and_equivalents, revenue, net_income, cfo) the day
it authenticates — a TRUE Sloan TATA, cash-conversion ratio, and reduced-Beneish
score, all superior to anything computable here. Census 8 on the day.

## Entry EQ-D1 RESULT (2026-09-10, interpretation after the print; runner
scripts/analyze_eq_d1.py; desk-verified independently on two cells: e1 panel 12m
-11.8808 vs script -11.88, e5 large-cap composite 12m +2.6774 vs +2.68) — THE
ACCRUAL-DIVERGENCE PROXY SURVIVES ITS OWN ADMISSIBILITY BAR; THE COMPOSITE DILUTES
RATHER THAN STRENGTHENS IT — A CLEAN, HONEST MISS OF THE BENEISH-COMPOSITE PRIOR.
e1 TATA_proxy D10-D1: panel 1m **-10.62** / 12m **-11.88** / 36m -4.43; large-cap
1m -0.69 / 12m -4.76 / 36m -1.45 — NEGATIVE at every horizon, both cuts. GRADE: HIT
under the registered admissibility bar (any negative print counts as strong
evidence, since the stated bias direction WEAKENS rather than inverts this
anomaly) — and the print is materially smaller than the textbook ~10%/yr Sloan
decile spread only at the 36m panel/large-cap horizons, matching the prior's
"plausibly smaller" branch exactly. e2 margin_decline D10-D1 fwd-12m: **+5.27**
(prior said negative — MISS); e3 leverage_increase D10-D1 fwd-12m: **+2.22** (prior
said negative — MISS). Both Beneish-style components run the WRONG way on this
panel: rising leverage and margin deterioration each PRECEDE outperformance here,
not underperformance — plausibly a mean-reversion/turnaround signature (margin-
compressed, more-levered firms rebounding) rather than the fraud-adjacent reading
Beneish intends, OR a construction artifact of using rank-differences instead of
levels (a firm moving from a low-margin decile toward the median registers the
same "decline" sign as one falling further from an already-high base — the two
are conflated in a pure rank-difference; recorded as a construction caveat for the
India re-run). e4 cash_conversion_proxy D10-D1 fwd-12m: **+7.77** — the mirror-check
of e1 HITS (good cash conversion outperforms, same direction as e1's story).
e5 THE COMPOSITE (mean rank of tata+margin_decline+lev_increase): panel 1m -2.78 /
12m -3.40 / 36m -2.49 — WEAKER than e1 ALONE at every horizon (12m: -3.40 vs
-11.88); large-cap composite **FLIPS POSITIVE** (1m +1.09 / 12m +2.68 / 36m -0.20).
GRADE: the Beneish "composites add power" prior MISSES outright — here the
composite DILUTES the signal, because two of its three ingredients (e2, e3) point
the wrong way on this panel; forcing them together with e1 cancels rather than
compounds. This is booked as the arc's central lesson: a composite is only as
good as its worst-signed ingredient, and BLINDLY porting a textbook multi-factor
score onto a new panel without checking each component's OWN sign first is exactly
the mistake this print catches. e6 THE VALUE-TRAP CROSS: among cheap stocks,
low-redflag minus high-redflag half: 12m **-1.32** (inverted — the "bad" half did
BETTER), 36m +1.20 (flips back, small, noise-level). GRADE: as pre-registered, the
12m inversion is graded under the WITHIN-CHEAP artifact rule (SC-D3a a3, VAL-D2/D3)
— a THIRD sighting, not a trap-filter failure; the 36m flip-to-near-zero is
recorded as inconclusive rather than a fourth data point either way. e7 era split:
1999-2009 **-15.95**, 2010-2019 **-6.99** — fades by more than half, matching the
registered post-publication-decay prior [HIT]. e8 large-cap-only fwd-12m: -4.76
(identical to e1's large-cap row, as expected — a construction sanity check, not
independent evidence). CONSUMPTION: (i) the raw TATA_proxy (earnings-rank minus
cash-flow-rank divergence) is the one component worth carrying forward as an
avoid-list input — cheap, robust, negative at every horizon and both cuts; (ii) the
margin-decline and leverage-increase RANK-DIFFERENCE constructions are NOT carried
forward as red-flag inputs in their current form — they run backwards on this
panel, and the construction caveat (rank-differences conflating "declining from
high" with "declining toward median") is flagged for the India re-run, where TRUE
dollar-value fields let margin/leverage changes be measured properly; (iii) DO NOT
composite red-flag scores mechanically — check each ingredient's own sign on the
target data first; (iv) the trap-filter question (e6) stays where VAL-D2/D3 left
it: unmeasurable on a no-delisting panel, PIT-gated to the India handoff (P5
promoter-pledge + P3 delisted_registry give the real test). India: the TRUE
Sloan TATA, true cash-conversion ratio, and a properly-signed reduced-Beneish
score (verifying each component's sign on Indian data before compositing — the
lesson from e2/e3/e5) are all registrable the day the handoff authenticates.
Census 8 (1297 -> **1305**).

## Addendum to EQ-D1 (2026-09-10, literature dossier complete — eq-dossiers/
a-earnings-quality-red-flags.md; zero new cells, zero census impact; cross-checked
against the booked EQ-D1 prints and the earnings-quality-atlas.html §4 buildability
table). TWO CORRECTIONS to the atlas's India buildability table: (i) the atlas listed
only 3 of Beneish's eight components as unbuildable from the P1-P6 handoff schema
(DSRI, AQI, SGAI); the dossier's precise field-by-field mapping finds a FOURTH —
DEPI (depreciation index) is also blocked, since P1 has no D&A line — so the India
ceiling is a 4-of-8 reduced score, not 5-of-8, and true CFO/EBITDA is separately
blocked for the identical reason (EBITDA needs D&A added back to EBIT, which P1
cannot supply). (ii) GMI is not a "partial" build as the atlas states — the buildable
substitute is an EBIT-margin index (ebit/revenue), a materially different, noisier
construct than the literature's true gross-margin index (which needs COGS, absent
from P1) and must be labeled explicitly as a proxy, never presented as GMI itself.
Both corrections are folded into the atlas (see build_eq_atlas.py Update section).
CITATION ADD: the "TATA as dollar values" row the atlas already lists as buildable is
properly the Hribar & Collins (2002) cash-flow-statement accrual construction —
(net_income - cfo)/average(total_assets) — which supersedes Sloan's original 1996
balance-sheet approach precisely because it avoids M&A/discontinued-operations noise;
this is the correct citation for the India rebuild, not the literal 1996 formula.
LITERATURE EXPLANATION FOR THE COMPOSITE'S FAILURE MODE: Dechow-Ge-Larson-Sloan
(2011) draw a sharp distinction the dossier flags as widely blurred in practitioner
writing — Beneish/DGLS-style components are built and validated to classify WHETHER
A FIRM IS MANIPULATING (an SEC-enforcement-label target), and only secondarily,
with markedly weaker evidence, to predict RETURNS. EQ-D1's e2/e3 wrong-signed misses
(margin-decline and leverage-increase both printing POSITIVE D10-D1, the opposite of
the registered red-flag-direction prior) are exactly the kind of gap this distinction
predicts — not a fluke of this one panel, and not evidence the components are broken,
only that "flags manipulation" and "predicts underperformance" were never the same
claim to begin with. Re-frames e5's composite dilution (booked above) as a structural,
not incidental, risk of blending detection-validated components with a return-
anomaly-validated one without checking each ingredient's OWN return-prediction
evidence first — strengthens rather than changes the already-booked CONSUMPTION line.
INDIA MARKER STRENGTHENED: promoter share pledging (P5) is confirmed as India's
cleanest red flag — a mandatory, quarterly SEBI shareholding-pattern disclosure,
genuinely point-in-time by regulatory construction (no filing-lag buffer, unlike
every accrual-based measure above), with a well-founded reflexive mechanism (pledge
→ price fall → margin call → forced sale → further price fall, independent of
underlying business performance) [LIT, directionally consistent with 2023-2025
India-focused pledging/crash-risk papers, LOW CONFIDENCE on exact magnitudes]. Widely
reported illustrations (Zee/Essel, DHFL, Yes Bank, Anil Ambani/ADAG group, Café Coffee
Day) are explicitly [CASE-STUDY LORE] — no fact about any named company is asserted,
only that the mechanism is commonly illustrated by these situations in Indian
financial media. OPEN ITEM, not resolved here: **[VERIFY: Beneish 1999 exact model
cutoff — this dossier cannot reconcile −2.22 (its own recollection of the published
paper) against −1.78 (cited in d-quality-metric-canon.md as a practitioner-circulated
threshold); check against the primary source before any cutoff is hard-coded into a
design]**. Also newly on record: the Ind-AS FY2016-17 transition is a structural
regime break (not a restatement) for every accrual/growth/margin measure spanning it —
any India accrual-family design must pre-register an explicit transition dummy or a
post-transition-only sample, not merely note the risk qualitatively. Zero cells; zero
census impact — literature and data-gap enrichment only, folded into the atlas.

## Entry SYNTHESIS-RF1 (2026-09-10) — THE RED-FLAG HORIZON MAP (principal: "give me
red flag lists and in which time frame it will work... 1m fwd may not need much...
but 12m/3y/5y may need... basis fwd looking horizon"). NOT A TRIAL — a cross-arc
synthesis citing ONLY numbers already printed in this ledger (process note #6
discipline applied to the orchestrator itself); zero new cells; zero census impact.
Draws on EQ-D1, QG-D3/QG-D4, VAL-D1/VAL-D5, H36-D1, SC-D3, TECH-D2/TECH-D3/TECH-D4,
DB-D1/DB-D3/DB-D5/DB-D6/DB-D9, CI-D1/CI-D3/CI-D4, MOM-D1, RATIO-D1, and eq-dossiers/a
(all already booked above). THE ORGANIZING FINDING: red flags on this desk sort into
three distinct horizon behaviors, not one universal "wait N months" rule —
(i) DECAYING flags, strongest immediately and fading — EQ-D1's TATA_proxy (accrual/
cash-flow divergence) panel -11.88%/yr at 12m fades to -4.43%/yr at 36m (large-cap
-4.76 -> -1.45); SC-D3's India post-bear smallcap avoid -12.31% at 12m fades to
-5.93%/yr at 36m (H36-D1 h11) — same sign, roughly half the per-year damage by 3y;
ES-D1's fundamental-momentum proxy -3.03pp at 1m fades to -0.84pp at 3y (H36-D1 h1);
(ii) GROWING flags, invisible or wrong-signed short and only real over years — QG-D3's
large-cap peak-ROE-at-any-price is +1.4pp (WRONG SIGN) at 12m, 0.0 at 36m, -1.5 at
60m, -2.1 at 120m; QG-D4's glamour-quality corner (ROE Q5 x growth Q5) is +6.5%/yr at
12m and only reads as the WORST corner in the matrix by +2.9%/yr at 120m; QG-D4's
volatile-quality trap is invisible at 12m (the QG-D2 no-delisting flattery) and only
turns negative in large caps at 60m (-0.7); the mirror-image protective spreads GROW
the same way — VAL-D1's szQ5 value spread +8.80 at 12m compounds to +6.5pp/yr at 3y
and +4.83pp/yr at 5y (H36-D1 h4/h5, VAL-D5 quoted), and low-vol only emerges as
protective once the junk-bounce artifact dies (H36-D1 h3: Vol FLIPS SIGN positive in
mid/large caps at 36m); (iii) REGIME/PROBABILITY flags, where NO fixed forward horizon
is the right frame at all — DB-D1's sovereign public-debt LEVEL shows ~zero, POSITIVE-
signed correlation to equities even at 5-10y (+0.16/+0.17) and only ever hurts BONDS
(US >=90%-debt cohort: next-10y real bonds -1.0%, 1/7 positive, DB-D9); DB-D5/DB-D3/
CI-D3 show credit BOOMS do not lower average 5y equity returns (null, +0.01) but raise
crisis probability on a 3-YEAR clock instead (15-19% vs 5-6% calm) — a probability
flag, not a magnitude-at-a-horizon flag; DB-D9 c5's debt-equity positivity is a
PRE-1980-only regime fact (+0.19 pre / -0.05 post), resolved only across decades.
A fourth class — GOVERNANCE/MECHANISM-ONLY flags (promoter pledge, RPTs, auditor
changes, restatement history, off-balance-sheet items; eq-dossiers/a §4-5) — carries
NO desk-quantified horizon at all and is better read as an always-on avoid-list gate
than a timed signal; Beneish/DGLS components are literature-validated to CLASSIFY
manipulation, not to time returns (the DGLS distinction, eq-dossiers/a §2, already
explains EQ-D1's e2/e3 misses). Full table (every flag, entry ID, exact print, tier)
built as docs/learn/artifacts/red-flag-horizon-map.html (scripts/build_rf_horizon_
atlas.py), row 60. Zero cells; zero census impact.

## Entry EQ-DOSSIER-B (2026-09-10) — LITERATURE DOSSIER, NOT A TRIAL: additional
red-flag/manipulation frameworks beyond Beneish/DGLS (principal: "any other red flag
list or manipulation etc"). eq-dossiers/b-shenanigans-scores-and-market-signals.md.
Zero cells; zero census impact; no desk numbers computed — a literature-and-data-gap
extension of eq-dossiers/a, organized into three KINDS of evidence not previously
distinguished on this desk: (i) RATIO-BASED SCORES — Altman Z-Score/Z''(EM variant)
[LIT] and Ohlson O-Score [LIT], both distress/bankruptcy predictors (a different
target than manipulation, same distinction dossier a §2 already drew for Beneish vs
DGLS's return claim); Montier's C-Score [LIT, LOW CONFIDENCE on publication], a
practitioner's independent 6-flag checklist that corroborates the SAME mechanisms
EQ-D1 already found evidence for (cash/earnings divergence, asset growth) and adds one
genuinely new ingredient not yet in this program's vocabulary — Days Sales of
Inventory (inventory building faster than sales). (ii) A TECHNIQUE CHECKLIST, not a
formula — Schilit's Financial Shenanigans (7 categories: premature/bogus revenue,
one-time gains, expense-shifting either direction, liability under-recording, big-bath
special charges) [LIT] — the practitioner canon Beneish/Montier's ratios only PARTIALLY
quantify; round-tripping, reserve-smoothing and big-bath timing specifically require
footnote-level reading no aggregate financial field (this desk's or the India handoff's)
can substitute for — stated as the honest boundary of every ratio-based score covered
across both dossiers. (iii) MARKET/BEHAVIORAL SIGNALS using no accounting ratio at all
— abnormal insider selling [LIT, Seyhun], short interest as an early fraud detector
[LIT, Dechow-Lawrence-Ryans 2016, LOW CONFIDENCE], auditor fee anomalies [LIT,
Frankel-Johnson-Nelson 2002, LOW CONFIDENCE], options-grant-timing/backdating [LIT,
Lie 2005], and earnings-call textual/vocal deception cues [LIT, Larcker-Zakolyukina
2012 + Hobson-Mayew-Venkatachalam, LOW CONFIDENCE] — all require data sources entirely
outside the P1-P6 handoff schema (insider transactions, short interest, audit fees,
ESOP grant terms, call transcripts), flagged as genuine future data asks, not
approximable from what is already specified. Also newly recorded: Benford's Law digit-
distribution forensic testing [LIT, Nigrini] as a DISTRIBUTIONAL (not ratio-based) test
kind, with an open, unresolved feasibility question — **[VERIFY: whether a pooled
cross-sectional Benford test across P1's ~8 numeric fields is a meaningfully different,
weaker claim than the literature's intended per-company/many-line-item use, or not
worth registering at all]** — recorded as explicitly declined-to-size, not silently
omitted. INDIA BUILDABILITY MAP EXTENDED (dossier b §6 summary table, all frameworks
from both dossiers in one place): of roughly a dozen major frameworks, only THREE are
fully buildable from the current P1-P6 schema (Sloan/Hribar-Collins accruals, total
asset growth, cash conversion) plus promoter pledging (P5, governance-not-ratio) —
Altman Z/O-Score and Montier's C-Score are each only PARTIALLY buildable (2-of-5, and
2-of-6 respectively) for the SAME reason dossier a found for Beneish (4-of-8): P1's
aggregation is too coarse (no receivables, inventory, current-asset/liability split,
gross PP&E/depreciation detail) for any established score to run in full — an
independent corroboration, from three unrelated frameworks, of the same schema
ceiling, not a new complaint. CONSUMPTION: none promoted (literature-and-gap dossier
only); folds into the Earnings Quality Atlas as a new section (build_eq_atlas.py).
Zero cells; zero census impact.

## Entry SYNTHESIS-FZ1 (2026-09-10) — THE INDIA FACTOR ZOO, LARGE-CAP VS SMALL-CAP
(principal: "factor zoo which all work in indian markets sorted best largecap vs
smallcap seperately"). NOT A TRIAL — a cross-arc synthesis citing ONLY numbers already
printed in this ledger; zero new cells; zero census impact. FIRST, A DATA-HONESTY
STATEMENT the synthesis itself required: this desk's largest body of factor work
(QG-D1-D6, VAL-D1-D6, ES-D1/D2, SC-D4/D5, EQ-D1) ran on the US firm_panel (data_ml,
1999-2019) as an explicit REHEARSAL for India, never India evidence — presenting those
size-quintile splits as "India large-cap vs small-cap" would have been a data-labeling
error the synthesis exists specifically to avoid. REAL India evidence is narrower:
IIMA monthly factors (SMB/HML/WML/MF/RF, 1993-2025), NIFTY index-level reads, and the
NIFTY500 survivor panel (2012-2021, one-way). LARGE-CAP/MARKET-LEVEL, best to worst:
(1) the vol-managed 50/50 WML+HML blend, +17.02%/yr standalone, the ONLY India factor
construction actually in the standing book (OP-D5/D6, +1.80%/yr contribution at 15%
weight); (2) momentum (WML), +15.06%/yr baseline but a SWITCH not a constant — the
post-bear+top-vol crash state flips it to -27.46%/yr (TECH-D3), and chasing recent WML
strength itself inverts (+23.5%/yr after WEAK vs +12.5% after strong); (3) value (HML)
alone, +8.6%/yr full-period but Sharspe only 0.09 (India RF is high) with real winters
(2015-19 growth mania, Sh -0.39) (V0-V4); (4) the leverage/vol-clustering read
(RATIO-D1) — the calm-uptrend state is the WORST forward-drawdown state, not the
safest, folk intuition inverted; (5) NIFTY entry-states (drawdown terciles, stage
quadrants) — real states, not classic factors. SMALL-CAP, best to worst: (1) the
small-vs-large VALUATION SPREAD as a rotation timer, +16.05pp T1-T3 next-12m, corr
-0.69 at 36m (SC-D1) — the one real small-cap TIMING edge, in-sample, flagged; (2)
stock-level momentum in the liquid/top-ADV tercile, +5.87%/yr peak at the same 6-2
lookback as the full panel (MOM-D1); (3) the "winter rebound" after THREE straight
down years, +10.32% next-12m / +8.01%/yr at 3y (SC-D3 i2, H36-D1 h10) — downgraded to
a WATCH since the survivor-panel cross-check (SC-D3a a2) came back non-monotone; (4)
low-volatility (T4) — INCONCLUSIVE, Sharpe 1.45 vs 1.34 but alpha t=1.88 fails
significance by a hair, and the one-way bias here FAVORS the anomaly being real, so a
near-miss is not a kill; (5) post-bear re-entry — INVERTS the US rebound trade,
-12.31% vs -0.20% next-12m (SC-D3 i3), Tier-C avoid-list for 12m; (6) the raw size
premium itself, UNCOMPENSATED at -2.9pp/yr over 32 years with worse drawdowns (-90% vs
-62%) and higher vol (1.34x) for LESS return (TL-D2 s8) — the single loudest small-cap
finding: holding the segment does not pay, only timing/selecting within it might.
READ TOGETHER (#1 and #6 above): the LEVEL of India's small-cap premium is negative,
but the SPREAD between cheap-small and expensive-small still orders relative returns
in-sample — any edge is in WHEN and WHICH small-caps, never in the segment itself.
Also newly on record: WML's skewness-ordering import from the US crowded-momentum
literature FAILS on India's own factor library (WML +0.05 skew, the mildest of the
three, not the most negative — CR1a), while the worst-single-month concentration test
still PASSES (WML -4.1sigma worst month, the fattest tail — CR1b) — momentum is not
"crowded" by the US skew signature but still owns the fattest single-month loss.
Published as docs/learn/artifacts/india-factor-zoo.html (row 61; scripts/build_india_
factor_zoo.py). Zero cells; zero census impact.

## Entry SYNTHESIS-LH1 (2026-09-10) — LOW-HERD ALPHA CANDIDATES, BEYOND THE FACTOR ZOO
(principal: "more apart from these common factors which can deliver alpha in indian
markets and lessor crowded but works good and can continue to work good in future").
NOT A TRIAL — a cross-arc synthesis citing ONLY numbers already printed in this
ledger; zero new cells; zero census impact. Reframes the question from "which
cross-sectional factor" to "which execution/timing/governance edge, and WHY should it
resist arbitrage" (the CONTRACT §5 durability test applied explicitly to each row).
CONFIRMED, real India data: (1) the overnight/intraday session split (T1) — overnight
+24.0%/yr (t=+10.5) vs intraday -12.6%/yr (t=-2.9), STRONGER post-2019 (+41.7pp gap) —
durable because it is not a tradeable arbitrage (STT kills the two-leg trade), only an
execution-timing fact nobody can compete away; T1b adds where the real risk lives: in
stress the overnight drift goes null (+9.2%/yr, t=0.66) while intraday craters
(-66.3%/yr, t=-3.3) — a structural fact about India's crisis mechanics. (2) the
currency-crash entry state (CU-D4iii) — next-3y after an INR crash +13.2%/yr vs +6.2%
others — durable because it requires holding through the crash itself, a behavioral/
career-risk barrier; CU-D5 adds that India's FX-equity coupling (-0.69) is the
opposite of the global panel's neutral +0.02, a structural India-specific fact most
imported EM templates get backwards. (3) promoter share pledging (eq-dossiers/a
S5a) — durable because the edge is in DOING THE DATA WORK (reading shareholding-
pattern filings), not information asymmetry. (4) the earnings-cycle phase inversion
(FUN-D1/D2/D3) — price leads earnings troughs ~10 months, India defensives LAG once
risk-off is identifiable — durable as long as consensus-estimate revision stays
slower than price discovery. (5) the 3-year smallcap contrarian pair (SC-D3, H36-D1)
— avoid 12m after a bear year (-12.31% cost) + the 3y winter rebound after 3 down
years (+8.01%/yr at 36m) — durable because it requires knowing the US playbook does
NOT transfer plus a multi-year contrarian hold most funds cannot stomach: patience
itself is the moat. (6) the high+rising-inflation asset ranking (CI-D1/D2, gold >
housing >> equity > bonds) — a tactical allocation overlay, not stock selection,
durable because few desks regime-condition on inflation ACCELERATION vs LEVEL
explicitly. HONESTY CHECK, one flagged as fading not durable: the turn-of-month
premium (T6-TOM) is real full-sample (+7.2bp/day, p=0.025) but SHRANK across the
SIP-era break (+12.2bp/day pre-2015 -> +3.8bp/day post-2015, p=0.29, no longer
significant) and its hypothesized SIP-flow mechanism was REFUSED — listed as a
caution (already decaying), not a candidate. REGISTERED CANDIDATES, data-gated:
H61-FLOWMULT (Inelastic Markets Hypothesis on India's SIP+FPI flow structure — flows
move prices ~5x and PERSIST, the highest-quality low-herd frame this desk's own
manager sweep found); H60-VRP (options-chain VRP conditioned on the SEBI 2024-26
retail-curbs regime break, BR4 — new because the microstructure itself is new); RC1
(index reconstitution mechanics — decayed in the US, but India's rising passive share
may still leave the window open, and CLOSING, unlike everything else on this list);
the India promoter-pledge+accrual composite quantified (needs the fundamentals
handoff); the R_EG unspanned-alpha flag's India adjudication (QG-D6). EXPLICITLY
FLAGGED AS NO LONGER LOW-HERD: VRP/option-selling (the standing book's condor engine,
the budget-day IV crush) is real but arguably the most crowded strategy in Indian
markets today — the SEBI 2024-26 curbs exist specifically because weekly-options
selling became a mass retail phenomenon, and this desk's own OP-D3b/OP-D7 grids
"honestly refused their own train winners OOS," itself evidence of live crowding.
Folded into the India Factor Zoo as a new Update section (v2, same URL). Zero cells;
zero census impact.

## Entry SNAPSHOT-1 (2026-09-10) — PRE-REGISTERED before running: THE CURRENT-STATE
READOUT (principal: "basis all these analysis... current environment and positions to
take... expected next 1y/3y returns"). NOT A HYPOTHESIS TEST — a descriptive "where are
we now" reporting exercise, no bar, no prior, because nothing is being adjudicated;
every construction is QUOTED VERBATIM from its already-booked parent design (process
note #5), applied to the LATEST available date in each vault series rather than to
history. STATED BEFORE RUNNING: several series are too stale for a true "current"
read and this will be reported as a gap, not silently patched — India VIX (vault ends
2023-04), IMF PCPS copper (vault ends 2017-06), JST (debt/credit/inflation batteries,
effectively ends ~2020) all CANNOT support a 2026 state reading; NIFTY's own vault
ends 2026-04-13 (~5 months stale vs the session date); FX/gold/CBOE-VIX/IIMA extend
closer to the session date (Aug/Jul/Aug/Dec-2025 respectively) and are used as the
freshest available proxies, stale-dated as printed. CELLS (descriptive, 7 series):
NIFTY (drawdown-from-ATH + TECH-D1 tercile-rank; trailing-12m up/down-year per SC-D3;
TECH-D2 stage quadrant via 200d MA level+slope; 52w-high proximity); GOLD (trailing-
12m return, trend vs 12m MA); NIFTY/GOLD ratio (RATIO-D1 r4/r5 convention: 12m-MA
slope + expanding percentile); IIMA factors (WML trailing 1m/3m for the own-momentum-
chasing check; SMB rolling-5y mean per SC-D3 i4/TL-D2's regime-map convention; RF
12m-change direction per FUN-D8); FX (INR/USD trailing-12m dlog, SEC-D2/CU-D5's
weak-INR-year >=+5% threshold and CU-D4's >=15% crash threshold); CBOE VIX (level +
own-history percentile, explicitly a GLOBAL not India-specific proxy, India VIX being
stale). Script: scripts/analyze_snapshot1.py. Census 0 (descriptive, no census impact
per the same convention as DB-D2's episode census).

| # | What | Result | Status |
|---|---|---|---|
| SNAPSHOT-1 | The current-state readout across 7 already-vaulted series, each construction quoted from its booked parent design (interpretation hand-appended AFTER the print; desk-verified: NIFTY drawdown-tercile-rank and FX trailing-12m dlog independently re-derived by hand, matched) | **NIFTY (as-of 2026-04-13, ~5mo stale)**: last 23,842.65 vs to-date ATH 26,328.6 — drawdown **-9.44%**, a MID-tercile read (rank 0.36); trailing-12m return **+2.19%** — an UP YEAR by the SC-D3 classification (the post-bear-avoid rule is NOT live); stage = **S4** (price BELOW its 200d MA, MA still falling) — the downtrend quadrant; per TECH-D2's own booked table this is NOT automatically bearish (S4 printed the BEST next-12m NIFTY read in-sample, +32.2%) but that finding was VALUATION-CONDITIONED (S4-cheap +14.65% vs S4-expensive +0.27%) and no India valuation percentile exists to say which S4 this is — stated as the single largest open question below; 52w-high proximity confirms the same -9.44% gap. **GOLD (as-of 2026-07, ~2mo stale)**: trailing-12m return a strong **+21.95%**, but price is BELOW its own 12m moving average — the two facts together mean gold ran hard earlier in the year (peaked ~4,587 in 2026-05) and has PULLED BACK for two straight months to 4,073 (-11.2% off the peak): a stretched, currently-correcting uptrend, not a fresh one. **NIFTY/GOLD ratio**: 12m-MA **FALLING**, percentile **0.32 (LOW)** — per RATIO-D1's r4/r5 read (FALLING state -> +5.54% mean-reversion relative-return vs RISING's +3.23%), a low/falling ratio has historically preceded NIFTY OUTPERFORMING gold over the next 12m — the historical conditional read, not a forecast, and in tension with gold's own stretched-uptrend read above. **IIMA factors (as-of 2025-12, ~9mo stale)**: WML trailing 1m **+1.30%**, trailing 3m cumulative **+8.27%** — genuinely STRONG recent momentum, which per TECH-D3's own-factor-momentum-inverts finding (average +12.5%/yr continuation after strength vs +23.5%/yr after weakness) is itself a reason for caution about chasing WML further from here, not a green light; SMB's rolling-5y mean is **+0.27%/mo (~+3.2%/yr annualized)** — POSITIVE over the trailing 5 years, in tension with TL-D2's -2.9pp/yr UNCOMPENSATED finding over the full 32-year sample — read as the recent window sitting inside a period the SC-D3 i4 regime map itself already flagged as "2023-24 froth," not evidence the 32-year base rate has reversed; RF's 12m-change is **FALLING** (0.47% vs 0.55%), which per FUN-D8 (falling-rate years +8.0%/yr vs +3.3 rising) is historically the better regime, though FUN-D9a's own hardening caveat (US monthly medians flat) is quoted against over-reading this. **FX**: trailing-12m INR/USD dlog **+8.61%** — ABOVE the +5% weak-INR-year threshold (SEC-D2/CU-D5), so India IS currently in a weak-INR year by that definition, though well below the >=15% CU-D4 crash threshold; CU-D6(d)'s own booked India read for exactly this state: weak-INR years average **-12.6% local / -20.6% USD** vs **+34.2%/+35.5%** in other years, with the NEXT year after a weak-INR year averaging **+25.5% local / +23.7% USD** — quoted as the historical conditional distribution for this exact state, not a forecast of what this specific year will do. **CBOE VIX (as-of 2026-08-31, freshest series)**: level 14.92, percentile **0.32 (LOW tercile)** — a global calm-vol regime, the opposite of the post-bear+top-vol crash state TECH-D3 warns about (that stand-down gate is NOT firing by this proxy, though it is a GLOBAL not India-specific one). **STATED GAPS, not silently patched**: no current India-VIX read (vault stale since 2023-04); no current copper/gold trend read (IMF PCPS stale since 2017-06); no current debt/credit/inflation REGIME read (JST-based DB/CI batteries stay structural-era context, not a live nowcast); no India CAPE/valuation-percentile read AT ALL exists in the vault (the NSE index-valuation runsheet row remains unpulled) — so no valuation-based statement can be made about whether NIFTY is cheap or expensive today, which is exactly the missing piece needed to read the current S4 stage per TECH-D2's own valuation-conditioned finding; named as the single largest gap in answering a positioning question | **current-state readout complete on 7 of 9 attempted series; 2 fully stale (India VIX, copper/gold) + the debt/credit/inflation batteries stay structural-context-only + no India valuation-percentile exists at all in the vault — every gap named, none patched; NIFTY is currently S4/mid-drawdown/up-year, gold is stretched-and-correcting, INR is in a weak-INR year, global vol is calm, WML has run hot; census 0 (descriptive)** |

## Addendum to SNAPSHOT-1 (2026-09-10) — THE TOP-LEVEL ALLOCATION (principal: "final
ideally best holding of reit, bond, gold, equity large mid small"). NOT A NEW TRIAL —
a construction built from already-booked findings plus explicitly-labeled general
portfolio-construction principles this program has never tested; zero new cells; zero
census impact. Distinguishes, row by row, DESK-GROUNDED from UNTESTED-DEFAULT rather
than presenting one undifferentiated number, per the same discipline as every prior
synthesis this session. Equity large-cap 50% (DESK-GROUNDED: the standing book's own
home, every real India factor edge found this session lives here); equity mid-cap 10%
(UNTESTED INTERPOLATION — this program has never run a mid-cap-specific design, only
small-vs-everything-else via SMB; sized as a reasoned midpoint, not a finding); equity
small-cap 5% (DESK-GROUNDED, DELIBERATELY UNDERWEIGHT: TL-D2's -2.9pp/yr uncompensated
32y base rate, -90% max drawdowns, and the current 5y-SMB reading sitting inside the
already-flagged "froth" window — not zero, because SC-D1's value-spread timer and
H36-D1's post-3y-bear rebound are real occasional tactical add-backs, never a
structural overweight); gold 15% (DESK-GROUNDED: CI-D2's gold-best-in-the-killer-cell
finding, the CU battery's gold-INR secular carry with hedge value concentrated at
stress horizons, T-series Sharpe 1.19 — HOLD not ADD right now, since SNAPSHOT-1 finds
gold stretched); debt/bonds 18% (GENERAL PRINCIPLE, NOT DESK-SIZED — the ballast/
liability-matching leg; this program has never run a bond-duration-specific design;
the one live read is directional only: RF is currently FALLING, a mild tailwind for
holding duration rather than staying ultra-short); REIT 2% (NOT DESK-RESEARCHED AT
ALL — zero vaulted REIT data, zero ledger entries anywhere in this program; sized on
general real-asset/income-satellite principles only, stated as the honest gap, not a
considered call). EXPLICIT DISAMBIGUATION: this top-level split is NOT the same
question as the standing book's own internal 65/20/15 (core/put-ladder-and-covered-
calls/factor-sleeve structure WITHIN the equity book) — the two 65-ish numbers are a
coincidence, not the same construction. Folded into the Positioning Note as a new
Update section (v2, same URL). Zero cells; zero census impact.

## Entry GAP-MAP-1 (2026-09-11) — THE COVERAGE GAP MAP (principal: "we have done macro
funda and technical — what else is left which can give us edge and alpha in Indian
markets"). NOT A TRIAL, NOT A FINDING — an agenda document in the manager-frontier-sweep
tradition; zero cells; zero census impact. METHOD, stated so the result can be audited:
enumerate the alpha-source space, SUBTRACT everything already booked in this ledger,
SUBTRACT everything already queued in RUNSHEET.md, report only the residual — which is
why several obvious-sounding candidates (shareholding-pattern dynamics, IPO listings,
reconstitution, results calendars, CP/CD money-market rates, FPI flows, sectoral TR,
index valuation, India CPI) do NOT appear as gaps: they were already on the runsheet.
Written to research/frontier/coverage-gap-map.md.
THE RESIDUAL, in three tiers. (i) RUNNABLE TODAY on vaulted data, no pull needed (G1-G5):
a rebalance-band/frequency grid (the desk holds static blends per T3 but has never tested
the rebalancing RULE itself), a concentration curve, cross-sectional dispersion as a STATE
variable, the India LTCG 1-year-threshold turnover asymmetry (a mechanical after-tax kink
no US-derived study can capture — it directly prices whether MOM-D1's winning 6-2 window
survives its own tax bill), and book-level vol-targeting. RATIONALE for putting these
first: the option-program sweeps already established the return gap is alpha/data-gated
while the RISK side has headroom (OP-D6 moved drawdown twice running, not CAGR) — so
construction mechanics, not another factor hunt, is where marginal effort on vaulted data
most plausibly pays, and G1/G4 attack CERTAIN costs (rebalancing drag, tax drag) rather
than hypothetical alpha. (ii) NOT ON ANY RUNSHEET — the genuine blind spots, all India-
specific, all public in principle, all blocked at this proxy: the exchange-microstructure
disclosure suite (delivery %, F&O ban list, ASM/GSM surveillance, circuit hits, bulk/block
deals, rollover/OI) — note the F&O BAN LIST is a candidate for the STOCK-LEVEL CROWDING
instrument India's factor book has now failed to find three separate times (CR1a, CR2,
CR-D2a all no-showed); the corporate-event suite beyond results (IPO LOCK-IN EXPIRY as the
cleanest dated mechanical supply shock in this market, buybacks with acceptance ratios,
demergers, open offers, delisting reverse-book-building, rights/bonus/splits, promoter
preferential allotments); the India G-SEC CURVE (2y/5y/10y/30y) — the smallest pull on the
page and it discharges an EXPLICITLY OWED verification, FUN-D8's India slope leg, which
FUN-D9a hardened on US data and which cannot run at all without it; India corporate bond
spreads + rating-migration history; GIFT Nifty basis + ADR/GDR premia (the natural
extension of T1's overnight discovery, on the same session boundary); filing/call text
analysis (flagged in eq-dossiers/b §5, never run); and AMFI SCHEME-LEVEL NAV history —
the one row bearing on the OPERATING business rather than the model (MF alpha persistence,
capacity decay, the flow-performance loop). Eight rows added to RUNSHEET.md under a
dated gap-map section. (iii) A CHEAP FIX TAKEN THIS SESSION: the breaks registry carried
BR1-BR6 with NO TAX DIMENSION at all — BR7 (LTCG on listed equity reintroduced, Budget
2018, the origin of the 1-year threshold), BR8 (DDT abolished / dividends taxed in the
recipient's hands, Budget 2020 — the single largest break for any yield-based sort, with
an explicit consumption rule that VAL-D1's Div_Yld split and QG-D1's payout finding must
NOT be read across it), BR9 (buyback taxation changed twice, 2019-07 and 2024-10, the
second landing inside the BR4 curbs window, plus the same-budget F&O STT increase) are
now registered, each press-sourced with a pin-the-notification [VERIFY] in the BR4/BR6
tradition. BR7-BR9 are deliberately registered AHEAD of their consumers so they bind the
after-tax designs before those designs exist. CONSUMPTION: nothing promoted; no booked
verdict changed; every gap-map row still owes its own pre-registration before any number
is computed. Zero cells; zero census impact.

## Entry G1-G4 (2026-09-11) — PRE-REGISTERED before running: THE CONSTRUCTION-MECHANICS
BATTERY (principal: "do the runnable today ones" — the gap map's Tier-1 rows, the only
alpha-space residual that needs no new pull). RATIONALE quoted from GAP-MAP-1: the option
sweeps established the return gap is alpha/data-gated while the RISK side has headroom
(OP-D6 moved drawdown twice running, not CAGR), so construction mechanics — which attack
CERTAIN costs (rebalancing drag, tax drag) rather than hypothetical alpha — is where
marginal effort on vaulted data most plausibly pays.
DATA, all already vaulted: NIFTY 50 daily 2007-2026 (index/, price-only — NO dividends,
stated as a level caveat that affects all four designs equally and cancels in every
WITHIN-design comparison); gold monthly 1833-2026 (commodities/) converted to INR via
fx/inr_usd_monthly (the correct construction for an India investor, the T3 "INR-gold"
convention quoted); IIMA RF monthly for the Sharpe leg (available to 2025-12 — the Sharpe
sub-window is stated separately from the CAGR window, never silently mixed); NIFTY500
survivor panel 2012-2021 (panel/, 487 names) for everything stock-level. Statutory costs
come from quant/costs/statutory.round_trip_bps(reg,'cash_delivery') — NEVER a hardcoded
rate (process note #6); tax rates from the new config/costs.yaml capital_gains_tax_india
block (press-sourced, BR7/BR9 [VERIFY] attached — no number typed into the script).
COST CONVENTION fixed now: per rebalance event, traded notional = sum|dw|/2 (selling x of
one leg and buying x of the other turns over x of notional, incurring one sell + one buy =
one round trip); cost = traded_notional * round_trip_bps/1e4.

**G1 — the rebalance-band / frequency grid (8 cells).** The desk holds static blends
(T3: the static 50/50 equity-gold beat active rotation at BOTH lookbacks) but has never
tested the rebalancing RULE itself. 50/50 NIFTY / gold-INR, monthly observation,
2007-04..2026-04. Rules: calendar {monthly, quarterly, semi-annual, annual, never} and
threshold bands {+-3pp, +-5pp, +-10pp}. Report per rule: CAGR, ann vol, maxDD, annualized
one-way turnover, and NET CAGR after statutory cost.
PRIOR (from the rebalancing literature, and from F6a's own finding that transaction
whipsaw is a rounding error at 0.02-0.28%/yr): (a) GROSS Sharpe-equivalent differences
across the whole grid are SMALL — best-minus-worst CAGR/vol spread < 0.10; (b) after cost,
LOW-frequency or WIDE-band wins — annual or +-10pp beats monthly by >= 0.20pp/yr net CAGR;
(c) turnover falls monotonically as band width rises.
BAR / KILL BRANCH stated both ways: if the NET-CAGR spread between the best and worst rule
is < 0.20pp/yr, rebalancing choice is IMMATERIAL at this blend and is booked as a
NON-DECISION — which is a useful kill, because it retires a whole class of fiddling; if
the spread is >= 0.20pp/yr the winning rule is named and enters the playbook as a
construction default (never a timing rule).

**G2 — the concentration curve (8 cells).** How many names before diversification stops
paying in India. Survivor panel monthly returns; random equal-weight draws of N names,
N in {5,10,15,20,30,50,100,200,487(all)} — 8 drawn N's plus the all-names reference;
200 draws per N, seed FIXED at 20260911 and stated; monthly rebalance to equal weight.
Report per N: median CAGR, median ann vol, median CAGR/vol, and the p10 of terminal
wealth across draws (the downside an investor actually bears, not the median).
ONE-WAY RULE, declared before the run: the survivor panel deletes failures, and it
flatters CONCENTRATED portfolios MORE than diversified ones (idiosyncratic blow-up is
exactly what was deleted, and a 5-name draw from survivors is 5 survivors). Therefore a
print saying concentration does NOT pay is ADMISSIBLE (the bias worked against it); a
print saying concentration DOES pay is recorded as NON-EVIDENCE, not a finding.
PRIOR: median CAGR/vol rises steeply to N~15-20 then flattens (the classic curve); the
p10 terminal wealth keeps improving well PAST N=20 — i.e. the TAIL, not the median, is
what argues for holding more than 20 names.
BAR: p10 terminal-wealth improvement from N=20 to N=50 >= +10% relative => the tail
argument holds and the stock book's floor is set above 20 names; < +10% => 20 names is
defensible on this panel (recorded with the one-way caveat either way).

**G3 — cross-sectional dispersion as a STATE (5 cells).** A state variable the desk has
never built. Monthly cross-sectional stdev of stock monthly returns across the panel;
expanding terciles (min 36 months, lagged 1 month — real-time by construction). Reads:
next-1m and next-12m 6-2 momentum decile spread (D10-D1, MOM-D1's winning India window
quoted verbatim), and next-1m / next-12m low-vol spread (bottom-trailing-12m-vol decile
minus top), per dispersion tercile; plus the redundancy cell — corr(dispersion state,
realized-vol state).
PRIOR: HIGH dispersion => wider momentum spread (more cross-sectional opportunity).
BAR: the HIGH tercile's momentum spread exceeds the LOW tercile's by >= 5pp/yr AND the
ladder is monotone => dispersion is a real, new conditioner.
REDUNDANCY BRANCH, pre-stated because dispersion and vol are obviously correlated: if
corr(dispersion, realized vol) >= 0.7 AND the dispersion split merely reproduces the
DIRECTION of TECH-D3's already-booked India vol split (low-vol +20.0 / high-vol -7.2),
the read is booked REDUNDANT — a repackaging of a state the desk already owns, not a new
one. Both branches are findings; only one is a new instrument.

**G4 — the India LTCG-threshold turnover asymmetry (10 cells).** The mechanical after-tax
kink no US-derived study can capture, applied to the desk's own winning India momentum
construction. Survivor panel, 6-2 formation (MOM-D1 verbatim), LONG LEG ONLY (top decile,
equal weight) — the realistic India case is a long-only tilt, not an academic long-short,
and only a long leg has a coherent tax treatment. Holding period H in {1,3,6,12,13}
months, non-overlapping, re-formed at each disposal. For each H: gross annualized return,
then AFTER-TAX annualized under both rate regimes (pre-Jul-2024 15%/10%, post-Jul-2024
20%/12.5%), taxing at each realization and compounding the after-tax proceeds:
after_tax_ann = (1 + g_H*(1-rate))^(12/H) - 1, with rate = STCG if H < 12 else LTCG.
SIMPLIFICATIONS STATED, not hidden: the annual exemption is not modelled (portfolio-level,
immaterial at book scale); no loss set-off or carry-forward; no dividend tax (the index
leg is price-only anyway); H=12 sits exactly ON the boundary and is therefore reported
under BOTH treatments so the discontinuity is visible rather than assumed away.
PRIOR: gross return FALLS as H rises (momentum decays — MOM-D1's own ladder says so), but
the after-tax ranking may INVERT at the 12-month line because the rate drops by a third.
BAR: if the 13-month hold's after-tax annualized return EXCEEDS the 1-month hold's under
EITHER rate regime, the LTCG line materially reshapes India momentum design and must be
registered into every future India momentum design (a standing construction constraint,
not a timing rule). If it does NOT, the tax line is second-order for momentum, the 6-2 /
short-hold construction stands, and that is booked as the answer. Also report the
break-even: the gross monthly spread the 1m strategy needs to match the 13m one after tax.

**G5 — REGISTERED-UNRUN, frozen spec (0 cells today).** Book-level vol-targeting vs
fixed-weight: F3a vol-managed the INDEX; nobody has vol-targeted the whole three-book
stack, and the interaction with the collar overlay is unexamined. NOT run today for a
stated reason rather than silently dropped: it requires the standing-book engine
(scripts/analyze_op_d6b.py run_book()) plus a margin/collar interaction model, and
registering bars I cannot evaluate this session would be a fake registration. Spec frozen
here in the HG1/BW1 tradition: vol-target the BOOK's realized vol to {10,12,15}% with the
collar overlay live, versus the standing 65/20/15 fixed-weight baseline; bars are the
SW2-A1 baseline's own (+11.46 CAGR / -11.36 maxDD) — a variant must beat BOTH or it is
refused, per the challenger law.
Script: scripts/analyze_gap_tier1.py. Census 31 (8+8+5+10; G5 contributes 0).

## Entry G1-G4 RESULT (2026-09-11, interpretation hand-appended AFTER the print; runner
scripts/analyze_gap_tier1.py; desk-verified independently on two cells — G1's "never" cell
re-derived from a fully standalone 50/50 buy-and-hold construction (CAGR 13.2404% vs script
13.24%, vol 10.3863% vs 10.39%, maxDD -20.6150% vs -20.62% — exact on all three) and G4's
H=1m annualisation re-derived by hand (32.8301% vs 32.84%, after-tax-pre 27.3465% vs 27.35%).
VERIFICATION-PASS NOTE, recorded as the desk records these: the FIRST verification attempt
printed a 0.6pp CAGR gap on G1's "never" cell — the error was MINE, not the script's (I
divided by the second portfolio value while using a denominator of all months, skipping the
first month's return); re-derived correctly it matches exactly. The script was not changed.)
— CONSTRUCTION MECHANICS PAY, BUT NOT WHERE THE PRIORS SAID: REBALANCING ADDS DRAWDOWN,
DIVERSIFICATION KEEPS PAYING PAST 20 NAMES, DISPERSION IS DISTINCT BUT UNUSABLE, AND THE
LTCG LINE IS REAL BUT SUB-DECISIVE.

**G1 — the rebalance grid** (50/50 NIFTY / gold-INR, 2007-10..2026-04, n=223 months;
statutory round trip 22.27bps read from the registry, not typed). Net CAGR / gross CAGR /
vol / maxDD / turnover: monthly **13.19**/13.23/11.17/-24.43/16.31%yr (223 events);
quarterly 13.39/13.42/11.21/-25.16/10.32; semi-annual **13.55**/13.57/11.28/-25.10/7.98;
annual 13.43/13.44/10.94/-23.87/4.83; **never 13.24/13.24/10.39/-20.62/0.00**; band+-3pp
13.36/13.39/11.16/-23.98/10.20; band+-5pp 13.24/13.26/11.15/-25.02/6.93; band+-10pp
13.21/13.22/11.27/-23.94/3.67. GRADING, bar by bar: the BAR's kill branch does NOT fire —
net spread best-minus-worst **0.364pp/yr >= 0.20**, so the winner is named: **semi-annual
on net CAGR**. Prior (a) "gross CAGR/vol spread < 0.10" — **MISS BY 0.002** (actual 0.102);
recorded as a boundary miss, not rounded into a pass (bars are never moved). Prior (b)
"annual or +-10pp beats monthly by >= 0.20pp net" — **HIT on the annual limb** (+0.24pp),
**MISSED on the band limb** (+0.02pp). Prior (c) turnover monotone in band width — HIT
(10.20/6.93/3.67). **THE UNREGISTERED SURPRISE, and the headline**: pure drift ("never")
delivered the BEST risk-adjusted return of the whole grid (CAGR/vol **1.275** vs 1.184-1.228
for every rebalanced rule) AND the SHALLOWEST drawdown (**-20.62%** vs -23.87..-25.16%).
Nothing in the registration anticipated that rebalancing would ADD drawdown. Mechanism
offered as interpretation, not claim: both legs trended up across this window, so periodic
rebalancing repeatedly sold the runner into the laggard, and the drifted book ends up
weighted toward whatever compounded — which over this particular window also lowered
realized portfolio vol. CONSUMPTION: the net-CAGR winner (semi-annual) and the RISK winner
(never) are DIFFERENT rules and the entire net-CAGR range is 0.36pp — small beside the
3-4pp maxDD differences. The one clearly DOMINATED choice is **monthly**: worst net CAGR,
worst turnover (16.3%/yr), and no risk benefit for it. Default lands at **semi-annual or
annual**; "never" is NOT adoptable as a rule because unbounded drift eventually breaches the
mandate's own weight bands — a constraint stated here, not measured. Not a timing rule under
any reading.

**G2 — the concentration curve** (survivor panel, 418 names with >=60 monthly obs,
2012-01..2021-12; 200 EW draws per N, seed 20260911). Median CAGR / median vol / CAGR-vol /
p10 terminal wealth: N=5 25.56/26.58/0.962/**4.596x**; N=10 26.62/23.92/1.113/5.951;
N=15 26.45/23.03/1.149/5.977; N=20 27.06/22.52/1.201/**7.393**; N=30 26.79/22.04/1.215/7.459;
N=50 27.40/21.46/1.276/**8.213**; N=100 27.27/21.23/1.285/9.397; N=200 27.48/21.10/1.302/10.005;
all-418 27.37/21.00/1.304/**11.012**. BAR: p10 terminal wealth N=20 -> N=50 = **+11.08% >=
+10%** — **the tail argument HOLDS**; the stock book's floor sits above 20 names. PRIOR
"median CAGR/vol rises steeply to N~15-20 then FLATTENS" — **MISSED on the flattening**: the
ratio keeps climbing well past 20 (1.201 -> 1.215 -> 1.276 -> 1.285 -> 1.302) and only
settles after ~100; diversification kept paying in the MEDIAN too, not just the tail. p10 is
monotone increasing at every step. ONE-WAY RULE APPLIED AS DECLARED: the panel deletes
failures and therefore flatters CONCENTRATED draws more (a 5-name draw from survivors is
five survivors) — concentration nonetheless loses on BOTH median and tail, so this print is
**ADMISSIBLE evidence in the declared direction**, the strongest form available on this
panel. Absolute levels (25-27%/yr) are survivor-absurd and are NOT evidence; only the shape
across N is. CONSUMPTION: a concentrated India stock book (<20-30 names) is not supported by
this curve; the practical floor is **50-100 names**, where median and tail have both largely
converged. STATED LIMIT: this is a RANDOM-draw (zero-skill) curve — a skilled selector's
optimal N is a different question this design does not answer, and no concentration claim for
a skilled book is made either way.

**G3 — dispersion as a state** (n=84 months after the 36-month expanding warm-up; LOW 28 /
MID 30 / HIGH 26). 6-2 momentum decile spread by dispersion tercile: fwd-1m LOW **+3.14**
MID +15.21 HIGH +13.36 (HIGH-LOW **+10.22pp**); fwd-12m LOW +5.29 MID +10.17 HIGH +9.49
(HIGH-LOW +4.20pp). GRADING: the BAR required **BOTH** ">= +5pp AND monotone" — fwd-1m
clears the gap but is **NOT monotone** (MID 15.21 > HIGH 13.36), so it is **PARTIALLY MET**
and per the registration dispersion does **NOT** qualify as a clean new conditioner; fwd-12m
fails outright (+4.20 < +5, also non-monotone). REDUNDANCY BRANCH **does NOT fire**:
corr(dispersion, panel realized vol) = **0.453 < 0.70** — so dispersion is genuinely NOT
repackaged volatility. The combined verdict is the precise one: **distinct but unusable** —
the read kills the "it's just vol in disguise" objection AND simultaneously refuses
promotion. The one piece of real content, recorded as printed rather than as a ladder: the
LOW-dispersion tercile is where India momentum is WEAKEST (+3.14 vs +13-15 in MID/HIGH) — a
floor observation, not a monotone state. The low-vol rows are NEGATIVE at every tercile
(-1.13 to -21.45, most negative in HIGH dispersion): this reproduces the known EW-survivor
junk artifact (QG-D2's inversion; SEC-D7 a6's vol-CAGR cell is already permanently
survivorship-flagged) and is **NOT evidence about low-vol** — flagged artifact-consistent
and deliberately not interpreted.

**G4 — the India LTCG-threshold turnover asymmetry** (6-2 long leg, top decile,
non-overlapping; rates read from config/costs.yaml, never typed). Per-period / gross-ann /
after-tax pre-Jul2024 / after-tax post-Jul2024, with n: H=1m n=83 2.39%/**32.84**/27.35/25.57;
H=3m n=27 8.09%/**36.52**/30.49/28.53; H=6m n=13 15.53%/33.48/28.15/26.40; H=12m n=6
24.10%/24.10/21.69/21.09 (**on-boundary, also shown as-STCG: 20.49/19.28**); H=13m n=6
28.55%/26.09/23.50/22.86. **BAR: the 13m hold does NOT beat the 1m hold after tax under
either regime** — pre-Jul2024 23.50 vs 27.35 (gap **-3.85pp/yr**), post-Jul2024 22.86 vs
25.57 (gap **-2.71pp/yr**) — so the registered branch is taken cleanly: **the tax line is
SECOND-ORDER for India momentum and the 6-2 / short-hold construction stands.** THE
QUANTIFIED NUANCE, which is the actually useful output: the Jul-2024 change narrowed the
short-hold advantage by **~1.14pp/yr** (-3.85 -> -2.71) without flipping the ranking — the
LTCG line is a real but sub-decisive drag that got materially less favourable to short holds.
Break-even: a 1m hold needs **2.088%/month** gross (pre) or **2.163%/month** (post) to match
the 13m hold after tax, against an actual 2.394%/month — so the post-2024 margin is only
~0.23pp/month, roughly **10% of the gross edge**: a degradation-risk flag, because a ~10%
decay in India momentum's gross monthly spread would flip the after-tax ranking. PRIOR
PARTIAL MISS: "gross return falls as H rises" — actual is a **HUMP**, peaking at 3 months
(32.84 -> **36.52** -> 33.48 -> 24.10 -> 26.09), not a monotone decline. UNREGISTERED
FINDING flowing from that: **within the STCG zone a 3-month hold dominated the 1-month hold
on every metric printed** (gross 36.52 vs 32.84; after-tax 30.49/28.53 vs 27.35/25.57) at the
same tax rate and a third of the turnover — turnover cost is not even modelled here, which
can only widen the gap. Recorded as a candidate refinement to the momentum sleeve's holding
period, NOT consumed (it is an unregistered comparison inside a registered design).
**THE BINDING CAVEAT, stated first among limitations**: non-overlapping periods leave n=83 /
27 / 13 / **6** / **6** — the 12m and 13m cells rest on SIX observations across a ten-year
panel. Direction only; no significance is claimed or computable. Survivor caveat carried:
absolute levels (~33%/yr gross on a long leg) are survivor-absurd per MOM-D1's own flag —
only the cross-H comparison is evidence.

**G5** stays REGISTERED-UNRUN with its spec frozen as written (book-level vol-targeting needs
the standing-book engine plus a margin/collar interaction model; not faked).
CENSUS 31 (1305 -> **1336**).

## Entry CH-D1..CH-D5 (2026-09-11) — PRE-REGISTERED before running: THE CHURN BATTERY
(principal: "i want to know more on churn and related stuff for edge"). "Churn" is read in
BOTH of its meanings, kept in separate halves because they are separate questions:
**(A) OUR churn** — turnover as a COST to be managed (CH-D1..D3, the direct continuation of
G1/G4); **(B) THE MARKET's churn** — turnover as a SIGNAL in its own right (CH-D4..D5, never
run standalone on this desk: `Share_Turn_12M` has appeared only as a VAL-D2 companion and a
VAL-D3 trap marker, both inside the family VAL-D2 RESULT booked as ARTIFACT-DRIVEN, so
neither is a turnover verdict). A THIRD reading — the fund industry's own churn (scheme
portfolio-turnover ratio vs alpha) and the exchange's delivery percentage — is DATA-GATED and
gets RUNSHEET rows, not designs, today. Cost comes from `quant/costs/statutory`
(cash_delivery round-trip, registry-driven) and tax from `config/costs.yaml
capital_gains_tax_india` — no rate is typed into the runner (process note #6).

**CH-D1 — the RANK-BUFFER (hysteresis) test on the India momentum sleeve (6 cells).** MOM-D1
named 6-2 the India peak window on a GROSS print with no turnover discipline at all. Formation
quoted verbatim from MOM-D1/G4: `form62 = lg.rolling(5).sum().shift(2)` (6-month formation,
1-month skip). EW long portfolio; a name ENTERS at percentile rank >= 0.90 and EXITS only
below (0.90 - b), b in {0.00, 0.05, 0.10, 0.20, 0.30} percentile points (b=0.00 = the
unbuffered monthly re-formation, i.e. MOM-D1's own construction, the benchmark). Per cell:
gross ann, one-way monthly turnover, net ann after the registry round-trip applied to two-way
turnover, and net-after-STCG at the post-Jul-2024 rate (the live regime; every holding here is
under 12m). Cell 6 = the verdict row. BARS: (a) PROMOTION — some b > 0 delivers net ann >= the
b=0 net ann **+0.50pp/yr**; if none does, buffering is cosmetic on this panel and the
unbuffered rule stands as booked. (b) PRIOR — turnover falls monotonically in b (registered as
a CHECK, not assumed: buffered portfolios can thin out and force replacement). (c) PRIOR —
gross DECAYS with b, but by **< 3.0pp/yr** from b=0.00 to b=0.30 (the signal is not so fast
that holding stale winners destroys it). ONE-WAY RULE, and it matters here: buffering holds
names LONGER, and this panel deleted its delistings, so holding a decaying name longer is
FLATTERED. A print that buffering HELPS is therefore NON-EVIDENCE-GRADE (flagged, not booked
as doctrine); a print that buffering does NOT help, or hurts, is admissible.

**CH-D2 — OVERLAPPING re-formation frequency: the fix for G4's n=6 (6 cells).** G4's holding
ladder was non-overlapping and bottomed out at SIX observations; the Jegadeesh-Titman
overlapping construction re-forms 1/k of the book each month and holds each tranche k months,
yielding a monthly-frequency series at every k. k in {1, 2, 3, 6, 12} (5 cells) + the verdict
row. Per cell: gross ann, ann vol, maxDD, one-way monthly turnover, net after the registry
round-trip, net after tax (each tranche's own holding length picks the rate — k >= 12 gets
LTCG, everything shorter STCG, both rate regimes printed). BARS: (a) CONFIRMATION — G4's gross
HUMP at 3 months reproduces here, i.e. k=3 gross >= k=1 gross AND k=3 gross >= k=6 gross. If
it does NOT reproduce on hundreds of observations, G4's hump is declared a small-sample
artifact and that record is corrected in place. (b) PROMOTION, the honest test of G4's
unregistered candidate now that turnover cost IS modelled: k=3 net-of-cost-and-tax >= k=1's
**+0.50pp/yr**. (c) PRIOR — one-way turnover falls roughly as 1/k, so k=3 saves materially on
cost; the registered question is only whether gross decay eats the saving.

**CH-D3 — PARTIAL ADJUSTMENT on the asset book: the G1 continuum (6 cells).** G1 tested WHEN
to rebalance (calendar, band) and found drift beat every rebalance rule on both return/vol and
drawdown while being unadoptable under the mandate's weight bands. The untested dimension is
HOW MUCH to trade. Rule: each month end, trade a fraction lambda of the distance back to the
50/50 NIFTY / INR-gold target, lambda in {0.00, 0.25, 0.50, 0.75, 1.00} (lambda=0.00 = G1's
"never", lambda=1.00 = G1's monthly — both are known anchors, so the interior cells are the
new information). Same blend, same window, same registry cost. 5 cells + the verdict row.
BARS: (a) PROMOTION — some INTERIOR lambda (0 < lambda < 1) delivers BOTH a net CAGR within
**0.20pp/yr** of the grid's best AND a maxDD no deeper than lambda=0.00's; if so, partial
adjustment is the mandate-compatible resolution of G1's dilemma and the lambda is named. If
not, nothing beats the semi-annual calendar rule G1 already named. (b) PRIOR — maxDD is
monotone INCREASING in lambda (G1's headline generalizes). (c) PRIOR — turnover is monotone
increasing in lambda and roughly proportional to it.

**CH-D4 — TURNOVER AS A SIGNAL: the lookback ladder (US firm_panel, REHEARSAL not India
evidence — the SYNTHESIS-FZ1 labelling rule binds) (5 cells).** Construction per the VAL
conventions: `dec()` n=5 per date on Share_Turn_{3M,6M,12M}; LOW-minus-HIGH turnover spread at
fwd 1m (x1200) / 12m (x100) / 36m (QG-D3 compounding) + the szQ5 large-cap 12m column (the
implementable one). 3 lookback cells each carrying that 4-column profile (VAL-D1's counting) +
1 lookback-ladder verdict + 1 INTERACTION cell (Lee-Swaminathan: within Mom_11M top quintile,
LOW-minus-HIGH turnover at fwd-12m). BARS: (a) PRIMARY, at the ES-D2/VAL-D2 gate scale of
**2.00%/yr** (precedent, not a new magic number) — the szQ5 12m LOW-minus-HIGH spread >= +2.00
for at least one lookback => the Datar-Naik-Radcliffe neglect/liquidity premium is present in
large caps here. (b) PRIOR — the spread is POSITIVE at every lookback [Datar-Naik-Radcliffe
1998; Amihud liquidity premium LIT] and STRONGER at 12M than 3M (levels beat shocks). (c)
PRIOR — the interaction clears +2.00 too: quiet winners beat loud winners. ONE-WAY RULE: this
panel deleted its delistings and high-turnover names skew toward the distressed and the
attention-driven, exactly the population whose worst outcomes were deleted — so the bias
FLATTERS HIGH turnover. A print that LOW turnover wins is admissible (it wins DESPITE the
bias); a print that HIGH turnover wins is non-evidence-grade and must be read artifact-suspect
(the EQ-D1 argument, same shape).

**CH-D5 — VOLUME SHOCK on the India panel: the real-India leg (6 cells).** CONSTRUCTION LIMIT
STATED UP FRONT, not silently dropped: the India vault has `n500_value_traded` (daily rupee
value) but NO shares outstanding and NO market cap, so the textbook turnover ratio
(volume/shares) is NOT constructible here — this is the P1/P4 gate again, and the honest
substitute is a WITHIN-STOCK measure that never needs a share count. VS = log(median value
traded over the last 21 trading days) - log(median over the prior 252) — a stock's own churn
ACCELERATION, with the size and liquidity LEVEL differenced out entirely. Terciles per date,
monthly. Cells: fwd-1m / fwd-3m / fwd-12m LOW-minus-HIGH spreads (3); the liquid-tercile
sub-read at 12m (MOM-D1's prior-year top-ADV tercile convention, quoted) (1); the momentum
interaction (within 6-2 top-decile winners, LOW-shock minus HIGH-shock at fwd-12m) (1); and a
REDUNDANCY check, pooled corr(VS rank, 6-2 rank), with the threshold registered in advance at
|corr| >= 0.50 => the volume shock is largely momentum repackaged and the design is DEMOTED
(1). BARS: (a) PRIMARY — |fwd-12m LOW-minus-HIGH| >= **4.00pp/yr** AND the sign agrees in the
liquid tercile => a real India churn signal, registrable as a Tier-C state. (4.00 is inherited
scale, not a free parameter: TL-D2's -2.9pp/yr size base rate and MOM-D1's +5.87 liquid-tercile
momentum print set the neighbourhood.) (b) PRIOR, two-sided BY CONSTRUCTION because the
literature is genuinely split: the attention/overvaluation story wants HIGH shock to
underperform (LOW-minus-HIGH positive) while the Gervais-Kaniel-Mingelgrin high-volume return
premium wants the opposite at short horizons — so the registered prior is a SIGN FLIP ACROSS
HORIZON: positive at 12m, negative or null at 1m. Same sign at both horizons = flip prior
MISSED, recorded. (c) PRIOR — the redundancy check does NOT fire. ONE-WAY RULE: as CH-D4 —
high-shock names skew event-driven and distressed, whose deaths were deleted, so the bias
flatters HIGH shock and a print favouring LOW shock is the admissible direction.

CENSUS 29 on the day (6+6+6+5+6). The third reading of churn is GATED, not designed: two
RUNSHEET rows added today (AMFI/AMC scheme-level PORTFOLIO TURNOVER RATIO disclosures, for the
fund-churn-vs-alpha question; and the NSE DELIVERY PERCENTAGE row already queued under the
gap-map microstructure suite is hereby named as the delivery-vs-speculative-churn instrument).
Neither is promoted or pre-registered here — each owes its own registration on arrival.

## Entry CH-D1..CH-D5 RESULT (2026-09-11, interpretation written AFTER the print; runner
`scripts/analyze_churn.py` + `research/churn.json`) — **THE CHURN QUESTION SPLITS CLEANLY:
OUR churn is where the money is, THE MARKET's churn is mostly UNMEASURABLE on the panels we
own.** Two runner bugs were found and fixed BEFORE any interpretation was written, both
recorded here because both would have flattered a result: (i) gross was being reported as a
geometric CAGR while net was arithmetic-compounded, which made "net > gross" appear in CH-D1/
CH-D2 — a units mismatch, not free money; both are now on the same arithmetic basis so their
difference is cost alone; (ii) CH-D2 was costing turnover with a 1/k proxy instead of actual
weight change, which overstated k=1's trading ~2.5x and therefore **biased CH-D2's own bar in
favour of k=3** — replaced with the same L1/2 weight-change measure CH-D1 uses, and the bar
(b) gain duly fell from +4.37/+4.07 to +1.67/+1.55pp/yr. DESK VERIFICATION, four cells on
deliberately different code paths: CH-D2 k=3 gross rebuilt as the mean of three staggered
independent 3-month-hold sub-strategies = **33.81% vs the script's 33.81%** (exact); CH-D1
b=0 turnover recounted as a new-name fraction = 38.66%/mo vs the script's L1/2 measure 39.40%
(the right relationship — the L1 measure also charges the weight shift on retained names);
CH-D4 Share_Turn_12M pooled = **-2.64 exact**, and the sign survives a date-equal-weighted
estimator (-2.86 panel / -2.07 szQ5); CH-D5's liquid 12m spread rebuilt with a MEAN-based
rather than MEDIAN-based shock = +4.77pp vs +4.05 (same sign and size — the measure is not
median-specific). An internal cross-validation also holds: CH-D1 b=0.00 and CH-D2 k=1 are the
same construction reached two ways and agree (gross 32.92 vs 32.88; turnover 39.40 vs 38.9%/mo).

**CH-D1 — the rank buffer. BAR (a) PASSES on the number and is NOT BOOKED, exactly as
registered.** Net (post-cost) by buffer: b=0.00 **30.21%**, b=0.05 **30.94%**, b=0.10 30.38,
b=0.20 30.24, b=0.30 28.68 — a shallow HUMP peaking at b=0.05 with a +0.73pp/yr gain, clearing
the +0.50 bar. The registered ONE-WAY RULE binds and disposes of it: buffering holds names
LONGER on a panel that deleted its delistings, so a print that buffering HELPS on return is
NON-EVIDENCE-GRADE. It is recorded, not consumed. WHAT IS ADMISSIBLE is the risk side, because
it runs the wrong way for the artifact story: vol falls monotonically 23.06 -> 21.53 and maxDD
shallows monotonically **-29.29 -> -26.15** as b widens. If deletion flattery were driving the
result, holding decaying names longer would deepen drawdowns, not shallow them. THE HONEST
CONFOUND, named: the book GROWS with b (42 -> 72 names), and G2 booked this same day that
diversification keeps paying past 20 names — so the risk gain is plausibly G2's effect
arriving through the buffer, not hysteresis per se. Priors: (b) turnover monotone in b HIT
(39.40 > 32.11 > 27.84 > 23.10 > 19.54 %/mo); (c) gross decay b=0->0.30 = **+2.92pp/yr**, HIT
under the <3.0 bar but only barely — recorded as a near-boundary hit, the mirror of G1's
boundary miss.

**THE SINGLE BIGGEST NUMBER IN THIS BATTERY, and it is a cost-model correction, not a
result:** the unbuffered 6-2 sleeve churns **472.8%/yr one-way** (39.40%/mo), and even at
b=0.30 it churns 234.4%/yr. Every cell above charges only the statutory round-trip (22.27bps),
which prices that at 1.32-2.71pp/yr. But the desk's OWN `config/costs.yaml
turnover_cost_curve` says at_100pct_liquid = 0.35-0.70%/yr and **at_500pct_throttled =
3.5-6.5%/yr**, with incremental_hurdle_500_vs_100 = 3.0-6.0pp. At ~470% one-way we sit at the
throttled end of our own curve, so **the true all-in drag on this sleeve is roughly 2-4x the
statutory-only figure used here** — which means every momentum print on this desk (MOM-D1, G4,
and these cells) understates its own cost side. Booked as a FLAG against the momentum sleeve,
and it cuts in the direction of churn reduction being worth MORE than these numbers show, not
less. No print is restated; the flag is the correction.

**CH-D2 — overlapping re-formation. BOTH BARS PASS, and this is the battery's one PROMOTABLE
result.** By k (gross / net / net-after-tax post-Jul2024 / maxDD / one-way): k=1 32.88 / 30.21
/ 23.57 / **-29.29** / 38.9%mo; k=2 33.16 / 31.29 / 24.40 / -26.48 / 27.1; **k=3 33.81 / 32.24
/ 25.12 / -25.40 / 22.6**; k=6 32.03 / 31.03 / 24.19 / -27.70 / 14.6; k=12 28.22 / 27.66 /
23.86 / **-33.54** / 8.3. BAR (a) **CONFIRMED** — G4's 3-month gross hump reproduces on 83
monthly observations per cell where G4 had 13 at H=3 and SIX at H=12/13, so **G4's hump was
real, not small-sample**, and that record stands rather than being corrected. BAR (b) PASSES
in both rate regimes (+1.67pp/yr pre-Jul-2024, **+1.55pp/yr post**), which converts G4's
UNREGISTERED 3-month candidate into a result that cleared a bar registered in advance. k=3 is
not a compromise: it has the best gross, the best net, the best after-tax, AND the shallowest
maxDD of the five. THE ARTIFACT STORY IS INTERNALLY FALSIFIED HERE, which is why this one is
promotable where CH-D1 is not: if the panel's deletions simply rewarded holding longer, k=12
would win — instead k=12 is the worst cell on gross (28.22) and by far the worst on drawdown
(-33.54). A monotone reward-for-patience is what the artifact predicts; a hump at 3 months is
not. Prior (c) HIT (turnover falls 38.9 -> 27.1 -> 22.6 -> 14.6 -> 8.3 %/mo, sub-1/k because
consecutive tranches overlap). CONSUMPTION: **the India momentum sleeve's re-formation should
be TRANCHED at k=3 (one third of the book re-formed monthly, each tranche held three months),
not re-formed whole each month** — Tier-C, wired when the India stock sleeve exists. And the
head-to-head the two designs jointly answer: CH-D2's best after-tax (25.12%) beats CH-D1's
best (24.13%), so **if you want to cut churn on this sleeve, stagger the re-formation rather
than widen the exit band** — and unlike the buffer, tranching does not depend on a
non-evidence-grade direction.

**CH-D3 — partial adjustment. BAR (a) FAILS, and the failure is the finding.** Net CAGR by
lambda: 0.00 **13.24%**, 0.25 13.35, 0.50 13.25, 0.75 13.20, 1.00 13.15 — a total spread of
**0.20pp**. maxDD by lambda: **-20.62, -23.70, -24.38, -24.49, -24.54** — a spread of 3.92pp.
No interior lambda qualifies: lambda=0.25 has the best net CAGR but its drawdown is 3.08pp
deeper than drift's, failing the DD leg as written. Priors (b) and (c) both HIT (maxDD monotone
deeper in lambda; turnover monotone rising 0.00/6.83/9.85/12.77/16.31 %/yr). THE NON-OBVIOUS
RESULT: **the drawdown penalty is FRONT-LOADED** — going from no rebalancing to a quarter-step
costs 3.08pp of the total 3.92pp penalty (79% of the damage) for 42% of the turnover, and
CAGR/vol falls monotonically 1.275 -> 1.177 across the grid. There is no gentle-rebalancing
free lunch: on this blend ANY rebalancing at all pays nearly the full drawdown price, and
trade SIZE buys essentially nothing in return (0.20pp across the whole grid). This generalizes
G1's headline from the WHEN dimension to the HOW MUCH dimension and closes the question G1
left open: partial adjustment does NOT rescue drift, so the consumption stands where G1 left
it — **rebalance as rarely as the mandate's weight bands permit, and when you do, size is not
a lever worth tuning.**

**CH-D4 — turnover as a signal (US panel, REHEARSAL, never India evidence). BAR (a) FAILS
DECISIVELY AND THE FAILURE IS NON-EVIDENCE-GRADE — the fifth sighting of the deletion
artifact, not a refutation of the literature.** LOW-minus-HIGH turnover (1m / 12m / 36m / szQ5
12m): Share_Turn_3M -4.29 / -0.64 / **+4.67** / -2.10; 6M -3.90 / -1.29 / **+4.45** / -2.76;
12M -3.65 / -2.64 / **+4.07** / -2.25. So high-turnover names OUTPERFORMED at 1m and 12m and
in large caps — and the registered one-way rule says exactly that direction is
artifact-suspect, because high-turnover names skew distressed and attention-driven, the
population whose worst outcomes this panel deleted. Prior (b) MISSED on both limbs. **THE
DATAR-NAIK-RADCLIFFE NEGLECT/LIQUIDITY PREMIUM IS THEREFORE NOT MEASURABLE HERE**, and is
recorded as unmeasurable rather than rejected. WHAT SURVIVES, both in the admissible
direction: (i) the **36m column is POSITIVE at every lookback** (+4.07 to +4.67) — low
turnover pays at three years, the same washing-out H36-D1 booked ("at 3y the junk noise
washes out"), and a within-measure sign flip between the 1m/12m and 36m columns is itself the
artifact's signature; (ii) the Lee-Swaminathan interaction cell **+4.70pp** at fwd-12m clears
the +2.00 bar — **quiet winners beat loud winners** among high-momentum names. Prior (c) HIT.
CONSUMPTION: turnover is not a standalone factor we can measure on this panel; the durable
reads are the 3-year horizon and the momentum-conditioning, both India-gated for a PIT test.

**CH-D5 — the India volume shock. BAR (a) FAILS AS WRITTEN, and the interesting cell is a
SIGN DISAGREEMENT between the panel and the tradeable part of it.** LOW-minus-HIGH shock
spreads: fwd-1m **-6.82**, fwd-3m -4.90, fwd-12m **-1.92** — same sign at all three horizons,
shrinking monotonically with horizon, so the registered SIGN-FLIP prior (b) is **MISSED** and
recorded: neither the pure attention story nor a clean Gervais-Kaniel-Mingelgrin flip
describes this panel; high-shock simply wins, most at the fast horizon. But the **liquid
tercile inverts it: +4.05pp/yr at 12m** (LOW +20.15 vs HIGH +16.10), and the mean-based
robustness rebuild gives +4.77. The bar required |panel 12m| >= 4.00 AND sign agreement with
the liquid read; it gets neither, so **NOTHING IS PROMOTED** — the exact bar-miss is recorded
rather than reinterpreted. The admissible reading, and it is only a watch: the panel-wide
high-shock win is non-evidence-grade (the deleted deaths are disproportionately illiquid
high-shock names) while the liquid-tercile print favouring the QUIET state is in the
admissible direction and is also the only third of the panel this desk could trade. Prior (c)
HIT — mean per-date rank corr(VS, 6-2) = **+0.270**, so the volume shock is genuinely NOT
momentum repackaged (the same non-redundancy G3 established for dispersion-vs-vol, and a
second instance of a construction being distinct but not yet usable). The India quiet-winners
cell prints **-9.64pp**, the opposite sign to the US rehearsal's +4.70 — non-evidence-grade
direction, so Lee-Swaminathan is booked as holding in the US rehearsal and UNMEASURABLE in
India on this panel. CONSTRUCTION LIMIT, restated because it is the binding one: the India
vault has rupee value traded but no share count and no market cap, so the textbook turnover
ratio cannot be built at all here — the volume shock is an own-history substitute, and a true
India turnover test is P1/P4-gated.

**WHAT THIS BATTERY CHANGED.** One promotion (CH-D2's k=3 tranching, on a bar registered in
advance and with the artifact story internally falsified). One closure (CH-D3 shuts the
partial-adjustment door G1 left open; rebalance size is not a lever). One cost-model flag that
touches every momentum print this desk owns (472%/yr one-way sits at the throttled end of our
own cost curve, so statutory-only understates the drag 2-4x). Two honest unmeasurables
(CH-D4's DNR premium and CH-D5's India turnover signal, both owned by the deletion artifact,
both now with a named PIT route). And one methodological note worth keeping: **the two bars
that PASSED on the number split on whether the artifact story could be internally falsified**
— CH-D1's could not and was recorded but not consumed; CH-D2's could (k=12 is the worst cell,
which a reward-for-patience bias cannot produce) and was promoted. That test, not the p-value,
did the adjudicating here.
CENSUS 29 (1336 -> **1365**).
