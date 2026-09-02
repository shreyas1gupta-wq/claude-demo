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
