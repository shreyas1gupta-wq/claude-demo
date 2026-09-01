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
