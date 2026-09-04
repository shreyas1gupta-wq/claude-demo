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

## Deviations
(none yet)
