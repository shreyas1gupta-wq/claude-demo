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
