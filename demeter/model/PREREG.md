# Pre-registration — pass 2 of the Demeter dual-engine study

Written 2026-09-04 (Asia/Kolkata) BEFORE any new candidate touched the out-of-sample window. Governs everything in
this pass. Any deviation is recorded in the "Deviations" section at the bottom, never silently.

## What is fixed before we start

* **Development window (all design and tuning):** data ending **2012-06-30**, accessed only through `dev_harness.py`,
  which hard-truncates the market data before the signal function is called. Primary DEV = 1990-01-01..2012-06-30
  (VIX exists from 1990). Secondary DEV = 1950-01-03..2012-06-30 for every ingredient that does not need VIX.
* **Out-of-sample window:** 2012-07-01..2026-02-11 (model-vs-Demeter comparison Jul 2012 – Jan 2026, 163 full months).
* **Headline cost case:** 3 bp per unit of leverage traded + 60 bp p.a. financing spread on the levered leg
  (1.5x the measured 2 bp / 40 bp). Secondary: 2 bp / 40 bp. Stress: 6 bp / 90 bp.
* **Parameter budget:** at most 6 tunable parameters per candidate. Structural constants (e.g. the {0,1,2,3} leverage
  grid, a fixed 21-day realised-vol window used only as a scale) are declared as constants in the signal file and
  named in its docstring.
* **Panel size:** SIX new candidates, one per pre-assigned lens (below), plus the pre-existing but never-evaluated
  `signals/vix_vrp.py` (found in the repo with no results file and no mention in RESULTS.md — disclosed here).
  No further candidates are added after the design phase closes.

## Lenses (one candidate each — fixed before design starts)

| # | file | lens |
|---|---|---|
| 1 | `signals/crash_exit_dual.py` | Two separate decisions: an "am I in the market?" state machine whose EXIT is a genuine crash trigger (consecutive multi-sigma down days and/or an implied-vol jump), and an independent "how much leverage?" rule. Default = stay in. |
| 2 | `signals/dissipation_reentry.py` | Re-entry that is NOT a trend filter: VIX down a set fraction from its trailing maximum while still absolutely high, plus an oversold measure; explicitly tested for spurious firing in 2000-02 and 2007-09. |
| 3 | `signals/volmanaged.py` | The literature's robust result (Moreira–Muir 2017 volatility-managed portfolio): leverage inversely proportional to trailing realised variance, capped at 3x, with a no-trade band / weekly cadence to hold turnover down. Minimal gating. |
| 4 | `signals/sticky_tier.py` | Whipsaw minimiser: discrete {0,1,2,3} tiers from a vol regime with wide hysteresis bands, minimum holding periods and a "do nothing unless the evidence is strong" default. |
| 5 | `signals/vix_vrp.py` (existing) → DEV-validated, possibly `vix_vrp_v2.py` | Variance-risk-premium lens: implied-vs-realised vol as the shock detector and re-entry trigger, VIX-level regimes with hysteresis for the tier. |
| 6 | `signals/composite_dual_engine.py` | The inference note's §7 composite: shock exit (ingredient 1) protecting a dissipation re-entry (2), leverage tiered by vol regime (3), hysteresis long enough to sit out whole months (4). The "reproduce Demeter" attempt. |

## DEV gates — a candidate earns ONE out-of-sample look only if it passes ALL of these on `dev_harness.py` at 3 bp / 60 bp

| gate | rule |
|---|---|
| G1 causality | `lookahead_check` ok at all five DEV cut-offs (1995-12-29, 2000-06-30, 2005-12-30, 2008-06-30, 2010-12-31). |
| G2 risk-adjusted | dev_1990 Sharpe ≥ **0.425** (the incumbent `final_model_fewtrades` scores 0.42528 on the same window and costs; the bar is that value floored to three decimals so the incumbent itself passes). |
| G3 drawdown | dev_1990 monthly max drawdown no worse than **−30%**. |
| G4 no ruinous era | every era with ≥ 60 days of signal (1990-1999, 2000-2012H1; and 1950-1969, 1970-1989 for non-VIX rules) has CAGR > 0 and max drawdown better than −40%. |
| G5 turnover | dev_1990 position changes ≤ **25 per year**. |
| G6 plateau | ≥ **50%** of single-parameter ±15%/±30% perturbations keep dev_1990 Sharpe within 25% of base. |
| G7 budget | ≤ 6 tunable parameters. |

Candidates failing any gate are reported as failures with their DEV numbers and are **never** run through `evaluate.py`.

## Out-of-sample look budget

* One `evaluate.py` run per gate-passing candidate at 3/60, then re-runs of the SAME frozen signal at 2/40 and 6/90.
  Costs do not alter the signal, so this is **one signal look, three cost rows**. `evaluate.py` also writes its own
  OOS parameter-perturbation table; that table is a robustness disclosure, not a selection input, and no parameter
  changes after the first OOS run (a changed parameter = a new candidate = a new disclosed look).
* The **recommended model is chosen on DEV, before OOS is seen**: highest dev_1990 Sharpe among gate-passers, tie → lower
  dev_1990 drawdown. OOS then tells us whether that pre-chosen model beats the incumbent. If a different candidate has
  the best OOS Sharpe, that is reported as exactly what it is — the best of N flattering itself.

## Acceptance (from NEXT_SESSION_PROMPT.md, unchanged), evaluated on the OOS window at 3 bp / 60 bp

OOS Sharpe > **0.73** AND OOS monthly max drawdown no worse than **−20.5%** AND position changes < ~25/yr AND not
ruinous in 1990-2012 / 1950-2012 AND the edge survives at 6 bp / 90 bp (or the cost level where it dies is stated).

## Things we will subtract or stress before claiming anything

1. **T-bill asymmetry.** Demeter books cash at 0%; the engine credits the T-bill on cash days. We report each model's
   CAGR/Sharpe with the T-bill zeroed on cash days as a separate column before any comparison with Demeter.
2. **Clustered slippage.** A stress row where per-trade cost scales with trailing realised vol: cost_bps × max(1, RV21/15%).
3. **The 1950–2012 and 1990–2012 eras** are reported for every candidate, gate-passer or not.

## Pre-OOS selection record (written before any out-of-sample run)

2026-09-11 22:55 IST — DEV ranking of gate passers by dev_1990 Sharpe at 3/60 (from `dev_results/PASS2_DEV_TABLE.md`):
vix_vrp_v2 0.678 (maxDD −19.8%) > sticky_tier 0.612 (−14.3%) > volmanaged 0.495 (−19.8%) > dissipation_reentry 0.447
(−12.4%). Gate failures: crash_exit_dual (G3/G4). Pending: composite_dual_engine (designer continuing from banked
files) and the three-lens verification of every passer. **Provisional DEV-chosen recommendation: vix_vrp_v2**, to be
confirmed or replaced ONLY by (a) the composite finishing above 0.678 with all gates, or (b) a SEVERE verification
finding against vix_vrp_v2. Whatever the OOS look shows afterwards does not change this selection.

## Verification outcomes (2026-09-12 02:10 IST — still before any out-of-sample run)

Three independent Sonnet verifiers per gate passer (L1 causality & code, L2 overfit & plateau, L3 mechanism &
execution; `VERIFY_BRIEF.md`; reports `dev_results/<name>_VERIFY_L*.md`, digest `dev_results/PASS2_VERIFICATION_SUMMARY.md`).
A SEVERE finding blocks the OOS look. Applied as written:

| candidate | DEV Sharpe | verdict | decisive finding |
|---|---|---|---|
| composite_dual_engine | 0.543 | **REFUTED** (L1) | LEV_REB fixed at 3x by comparing 3x/2x/1x on DEV → 7 tunables; six "borrowed" constants are other candidates' DEV-tuned values (13 DEV-selected values in all). |
| dissipation_reentry | 0.447 | **REFUTED** (L1, L2) | flat-1x default chosen against the 3/2/1 tier on DEV → 7 tunables; G2 cleared only by 7 dated bursts (base gate 0.389 < bar); grid max is a single-trade artefact; deflation puts 0.447 inside the noise band of ~8–10 independent bets. |
| volmanaged | 0.495 | **REFUTED** (L1, L2, L3) | POWER/EST/DISCRETE/WEEKLY each fixed by DEV comparison → 9 tunables; the Sharpe edge over SPY reverses sign on 1950–2012 (0.36 vs 0.47) and decays to 0.09 in the last DEV third; the asymmetric band froze leverage at 0.14x for 6.6 years (1997–2004) and 0.20x for 3.75 years (2008–2012). |
| vix_vrp_v2 | 0.678 | **REFUTED** (L1, L2, L3) | LEV_CALM (2 vs 3) and LEV_PANIC (1 vs 2) chosen on DEV → 8 tunables; the +0.07 edge over the original is under one SD of its own 216-cell grid and inverts to −0.06 under a one-session delay; no v2 design note or consolidated grid file exists. **Consequence: the pre-committed retirement of `vix_vrp` was applied on an unmet precondition and is VOID — the original is reinstated as the lens-5 candidate and goes through the same three-lens verification before any look.** |
| sticky_tier | 0.612 | **holds** (0 severe) | true tunables 6 exactly (FLOOR chosen on DEV — at the ceiling, not over); 735 parameter sets not 13; lag-robust (0.612/0.610/0.604); edge rests on 10 decisions in 22.5 years — MATERIAL disclosures carried into RESULTS.md. |

Two harness limitations exposed by the verifiers, disclosed rather than patched after the fact: `gate_check.py`'s G7 counts
only `DEFAULT_PARAMS` (the true count is a reading task, done by L1); `dev_harness.plateau` rounds integer perturbations
so small integer parameters get asymmetric or duplicated steps. `verify_tools.constants()` missed tuple assignments and
is fixed in the same commit as this note (it changes no result).

**Pre-OOS selection, revised under the rules above:** eligible = sticky_tier (verified) + vix_vrp (pending its own
verification). DEV ranking: sticky_tier 0.612 > vix_vrp 0.608. **DEV-chosen recommendation = sticky_tier**, unless its
own re-check fails. Refuted candidates receive **no** OOS look in this pass; their DEV records and verifier findings are
reported in full. An exploratory OOS look at the refuted panel would be a separate, Principal-authorised, clearly
labelled appendix — it is not run here because a look cannot be un-taken.

**vix_vrp (reinstated original), verified 2026-09-12 02:35:** **REFUTED** (L1; L2 and L3 hold with MATERIAL findings).
Decisive: the three leverage constants (2x calm / cash elevated / 1x panic) have no documented provenance — pass 1 left
no design note, neither audited grid varies them, and the docstring says the regime→leverage mapping was read off a
DEV conditional-Sharpe table — so the true count is 8 (G7 breach); and the same docstring says the OOS window "was looked
at only through the final evaluate.py runs", which pass 1 never recorded (no results file, no mention in RESULTS.md) —
an unresolvable contradiction that defaults to refuted. Material: a one-session execution lag cuts DEV Sharpe 0.608→0.486
and widens maxDD −19.8%→−28.3%; more than half the DEV Sharpe comes from the 1x PANIC leg (13.6% of days, ~5–6 panics);
halves 0.84 / 0.40. **No OOS look.**

## Outcome of the look budget (final)

| candidate | earned a look? | looked? | result at 3/60 |
|---|---|---|---|
| sticky_tier | yes (gates + verification) | **1 signal look, 3 cost rows** (2026-09-12 02:08) | OOS Sharpe 0.24, CAGR 3.23%, maxDD −17.9%, 73% cash, 10 changes in 13.6 years — **fails acceptance** |
| vix_vrp, vix_vrp_v2, volmanaged, dissipation_reentry, composite_dual_engine | no (refuted) | no | — |
| crash_exit_dual | no (gate failure) | no | — |
| pass-1 panel (6 models) | already evaluated in pass 1 | re-run at the three cost rows only (tags `_p2*`), not new looks | see RESULTS.md leaderboard |

Total new out-of-sample looks in pass 2: **one**. Total candidates with OOS numbers across both passes: **seven** (six from
pass 1, one from pass 2). The DEV-chosen recommendation of pass 2 (sticky_tier) failed out of sample; the pass-1 incumbent
`final_model_fewtrades` remains the recommended model.

## Deviations
1. **2026-09-04, session-usage limit.** The six-designer workflow lost five agents to the account's usage cap after 64
   minutes (`dissipation_reentry` returned; `crash_exit_dual` and `volmanaged` had banked a final harness JSON, a signal
   file and a design note but died before returning; `sticky_tier` had only a reference script; `vix_vrp` and
   `composite_dual_engine` never started). Re-launched 2026-09-10 with two agents at a time: a finisher completes the
   two banked notes from the banked artifacts WITHOUT re-tuning (crash_exit_dual stays a gate failure at its frozen
   point; volmanaged's frozen point passes all gates), and the three unstarted lenses run fresh. No out-of-sample file
   was created or read between the two launches (`results/` unchanged since commit 9ec0bb3; `OOS_LOOK_LOG.md` absent).
2. **2026-09-10, model-specific usage cap.** Round 2 lost the `vix_vrp` and `composite_dual_engine` designers to the
   Fable model's cap. Both had banked work: `vix_vrp` had completed the audit, built and gate-tested `vix_vrp_v2`,
   written the full design note and its return JSON (so it is treated as complete; the pre-committed retirement rule
   applies — v2 replaces the original); `composite_dual_engine` had banked the mechanism note, the parameter budget,
   the planned ablations, the signal file and one smoke run (Sharpe 0.43, maxDD −34.7% at an unfrozen point). A
   round-3 launch on 2026-09-11 briefed fresh designers as if nothing existed; it was stopped within a minute of
   starting and no file was written by it. Round 4 (2026-09-11) continues the composite from its banked files with
   an Opus designer and runs the three-lens verification on every gate passer with Sonnet verifiers, three agents at
   a time (Principal instruction of 2026-09-11).
