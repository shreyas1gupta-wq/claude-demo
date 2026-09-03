# Design decisions — batch 1 (asked and ANSWERED 2026-08-31)

Status: RESOLVED. This file is now the decision record. Research agents must honor the
**Decision** column; where a decision opens a new research question, it is listed in §2.

## 1. Decisions

| # | Question | Decision (principal, 2026-08-31) | Design consequence |
|---|---|---|---|
| 1 | Alpha / factor-efficacy benchmark | **Nifty 500 TRI for all books** (signal research and alpha accounting). Nifty 50 TRI remains the drawdown reference, as frozen. | One yardstick; per-book beta handled in the risk model. |
| 2 | Short side | **Base is hedge-only via index derivatives, PLUS a tactical single-name short sleeve**: Nifty 100 constituents only, via single-stock futures, put spreads, and defined-risk multi-leg option combos; very limited — **≤ ~25% of the total short-side sleeve**. | Design must pin the sleeve denominator precisely; shorts are tactical, not a symmetric factor book. |
| 3 | Leverage instrument | **Margin funding on cash names** (not index futures). | `funding_rate` becomes a first-class config parameter; the leverage-state function must clear expected-return > funding-rate. Margin leverage levers the held (high-beta) names and faces margin calls in stress — the risk stack must tighten leverage permission earlier than the futures-overlay arithmetic assumed. Principal to confirm actual funding cost (retail MTF ~9–12% vs prop/internal near MIBOR). |
| 4 | Hedge implementation | **De-grossing first ("mostly stocks"): hedging primarily by cutting stock exposure and margin; option BUYING is rare** — reserved, budgeted, for tail regimes. | The 0–150% hedge sweep applies mostly to net-equity reduction. The prior-pass fast-crash claim (Mar-2020 to ~−20%) relied on options; with rare option use the irreducible fast-crash floor must be re-derived — either the rare option buying is systematically rule-triggered, or the floor is honestly restated upward. |
| 5 | Drawdown violation / flash-crash exclusion | **Persistence-and-materiality test, not episode exclusion**: the relative constraint applies only when portfolio MDD > 20%; a violation requires the portfolio drawdown to exceed the Nifty 50 drawdown (same window) by more than a small margin ε for more than K consecutive trading days, K ≈ 10–20. Brief/slight excursions due to volatility are tolerated. Absolute ceiling 30–35% unchanged. | ε and K are derived parameters (ε plausibly tied to expected tracking vol over K days), with sensitivity analysis. Flash crashes are handled automatically: they produce only transient excursions. |
| 6 | Anchor book | **Moderate** — designed and built first; conservative derived as its capacity-constrained projection; aggressive adds fast/tail sleeves on top. | Matches middle-out build order. |
| 7 | Stage-2 stay-on gate | **Advisory-only until proven**: Stage 2 never touches the traded book until a pre-registered paired test (net IR + episode DD, with minimum effect) passes at a high bar. Shadow book + scored ledger from day one. | Stage-1 self-sufficiency is total by construction. |
| 8 | Cash-call re-entry rule | **Per-sleeve, to be derived in research** — no single global form. Candidate families: calendar tranches, hysteresis state rules, volatility-target-implied re-levering; match the family to each sleeve's signal half-life and failure mode. | Re-entry is a first-class research-agenda item, per sleeve, with equal precision to the exit. |
| 9 | LLM role in Stage 2 | **All three channels**: (a) structured checklist scorer with hard caps; (b) adversarial red team of Stage-1 output; (c) tactical thesis / buy-call generator with human veto. All logged and Brier-scored; all advisory-only until the Q7 gate passes. | Ledger schema must cover all three channels. |
| 10 | Special situations / IPOs | **Capped Tier-B satellite sleeve, aggressive book only**, event rules frozen at inception; size from evidence tier + capacity (likely single-digit % NAV). | Clean attribution; contained blast radius. |

## 2. New research questions opened by these decisions

1. **Funding-cost curve** (Q3): actual margin funding cost available to this desk vs MIBOR;
   leverage-state hurdle as a function of it. If funding is retail-priced (9–12%), average
   leverage ~1.10–1.15x rarely clears the hurdle — the leverage feature may be worth little.
2. **De-grossing-first fast-crash floor** (Q4): re-derive the irreducible fast-crash drawdown
   without standing options; specify the rule that triggers the *rare* option buying (it must be
   a rule, not discretion, to live in Stage 1).
3. **Tactical short sleeve** (Q2): evidence for index/single-name tactical shorts adding value
   after borrow/roll costs in India; sleeve sizing; interaction with the 1.5x gross cap.
4. **ε and K for the DD violation test** (Q5): derive from tracking-vol arithmetic + episode
   evidence; sensitivity sweep.
5. **Per-sleeve re-entry families** (Q8): map each sleeve to calendar / hysteresis / vol-target
   re-entry with evidence.

---

## Batch 3 — Pipeline v2 sign-offs (2026-09-01, from docs/PIPELINE.md §6)

Ten questions opened by the pipeline-v2 synthesis; none block the current deep-dive track, all
block the Q1 migration build. See docs/PIPELINE.md §6 for full wording: (1) grid sign-offs
(vol-target grid, probation-length grid, trial budget, archive K, dead-man T, overlay influence
grid, PBO threshold); (2) legal/compliance posture on automated capture + FutEq limits + permitted
option-spread hedges; (3) Conservative-book TC stance; (4) degraded-mode tolerance grid;
(5) availability/dead-man escalation; (6) GDP base-year revision treatment; (7) v1/v2 parallel-run
length and first migrating book (suggest Aggressive); (8) year-2 priority (chrono-LLM audit vs
flow-signal cycle vs meta-label accrual); (9) fix the Challenger review calendar a year ahead;
(10) pre-declared cut order if the attention budget is violated.

---

## Decision (principal, 2026-09-01): states are phase objects, not scalars

Directive: a scalar state discards the trail — 0.6 rising (0→0.2→0.4→0.6) and 0.6 falling
(1→0.9→0.8→0.7→0.6) are different regimes; notation 0.6U / 0.6D; richer-than-1D scoring wanted.

Implementation: business-cycle-clock representation (Eurostat/OECD CLI practice) — every ladder
state becomes (level, velocity, quadrant ∈ {recovery, boom, slowdown, downturn}, age-in-quadrant).
Quadrant boundaries deterministic (slope sign × level vs midpoint), NEVER fitted (no conflict with
the <10-transitions rule); direction has rank-based hysteresis (dead-band = expanding percentile of
|slope|, grid {0.15, 0.25, 0.35}); slope horizon and smoothing from grids per band. Module
`quant/ladder/phase.py`; convention `ladder.yaml state_phase_convention`; tests
`tests/test_phase.py` (7, incl. the 0.6U-vs-0.6D scenario and no-look-ahead truncation).

Consumption gate: phase is computed/logged/displayed everywhere, but NO traded rule branches on
quadrant or age until H66–H68 pass their pre-registered tests; first admissions reduce-only via
the (proposed) Challenger path. Opens H66 (quadrant asymmetry at matched levels), H67 (grid
stability: responsiveness-vs-flip-rate frontier), H68 (duration dependence of quadrant exit).

---

## Decision (principal, 2026-09-01): external data mirrors authorized "whenever required, freely"

Kaggle / HuggingFace / GitHub and similar hosts are authorized as data sources for research.
Discipline that STILL applies (unchanged): every pull is sha256-manifested into ingest/vault
(WORM); mirror data must be AUTHENTICATED against an independent mirror and/or published facts
before use (the JST R6 procedure is the template); PIT/vintage caveats recorded; mirrors never
outrank the primary source for India-critical series once the principal's-machine pulls exist.
Connectivity from this container (probed 2026-09-01): raw.githubusercontent.com,
media.githubusercontent.com (LFS), objects.githubusercontent.com (release assets) = OPEN;
huggingface.co, kaggle.com, zenodo.org, mba.tuck.dartmouth.edu (Ken French) = BLOCKED at the
egress proxy. Consequence: GitHub-hosted mirrors are pulled here; Kaggle/HF datasets go on the
principal's-machine runsheet (ingest/README.md).

---

## Decision (principal, 2026-09-01): monograph series proceeds in CYCLE ATLAS order, 30+ pages each

From the top of the atlas (Band 0, entry 0.1 debt supercycle) to the end, one at a time, every
aspect (theory/math/cross-country/India/data/econometrics/algorithm/psychology/real data/lesson).
Queue of record: docs/cycles/README.md. Existing monographs: credit (58pp) and momentum (52pp)
meet the bar; fast stress is queued for upgrade at its atlas position; value/quality completes in
flight.

---

# Batch 3 — questions the data-phase remote legs opened (asked 2026-09-02, AWAITING the principal)

The remote legs ran ~20 pre-registered trials on mirror data and built the Stage-1
machinery; five decisions now sit with the principal. None blocks current work; all shape
the full F2 / data-phase runs.

| # | Question | Context (the print that opened it) | Options on the table |
|---|---|---|---|
| B3-1 | Is the risk-drag budget PER-ERA or PROGRAM-AVERAGE? | F2-WF disqualified both index shortlist cells under a per-era <=2pp/yr bar; the DESIGN table reads as a program average. The choice decides how the full F2 adjudicates whipsaw-rich eras vs the COVID payout (37%->26%). | (a) per-era (strict, what F2-WF used); (b) program-average with a per-era ceiling (e.g. <=2x budget); (c) episode-conditional only |
> **Desk note (2026-09-03, post-F6a) — the budget you are setting is an EXPOSURE-drag
> budget.** The false-fire ledger measured transaction whipsaw at 0.02-0.28%/yr across the
> entire de-risk grid at index-futures costs — a rounding error. The 2.5-4pp/yr era drags
> the walk-forward measured are the price of standing de-risked, not of trading. Friction
> needs no budget line at this scale; the B3-1 options are unchanged, but the quantity they
> govern is exposure drag. (F3a adds a bound: the always-on capped vol-managed variant costs
> ~4.9pp/yr for maxDD 22% — the continuous end of the same trade.)

| B3-2 | L2 tau_half band: keep [1,3]m or widen the top? | F1b (Kendall 3.18m, CI [2.39,5.72]) and F1c (Andrews 3.19m, [2.19,4.63]) agree the estimate sits AT/above the band top; the drift policy's hysteresis kept the config value, lengthening watch set. | (a) keep [1,3] until full F1 on PIT data; (b) widen to [1,4] now (everything keyed to tau re-derives mechanically) |
| B3-3 | Approve the challenger review calendar? | config/challengers.yaml fixed quarterly dates (Dec-1-2026 onward) + annual (Sep-1-2027); the validator refuses 'online' outside them. Dates were set by the desk; the principal should own them. | (a) approve as set; (b) supply preferred dates (one edit; the gate machinery is date-agnostic) |
| B3-4 | Priority order for the Priority-1 pulls? | Pullers are ready with auth skeletons (pull_india_vix.py, pull_ccil.py, pull_nse_bhavcopy.py). PIT bhavcopy unblocks the most (full F2/MR1/CR-D2); India VIX unblocks CW-D1/F5/FS-D1; CCIL unblocks H58-D1/FS-D2. | (a) bhavcopy first (default recommendation); (b) VIX+CCIL first (smaller pulls, faster wins) |
| B3-5 | The two standing inputs | funding_rate unset; ADV table PROVISIONAL — the validator warns on every run and every cost number carries the stamp. | provide values / confirm brokers' terms; the leverage feature stays dark until then |

Recommendation recorded (desk view, not a decision): B3-1(b), B3-2(a), B3-3(a), B3-4(a).
