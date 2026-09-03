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
