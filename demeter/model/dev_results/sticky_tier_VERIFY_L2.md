# sticky_tier — L2 verification (Overfit & plateau)

Lens 2 of 3, adversarial pass on the frozen candidate. DEV only; no `results/`, no `evaluate.py`, no data past
2012-06-30 touched. All numbers below are copied from `dev_results/sticky_tier_VERIFY.json`,
`dev_results/sticky_tier.json`, `dev_results/sticky_tier_grid.csv` (= grid C1, 144 rows), and the four grid spec
files (`sticky_tier_grid{A,B,C1,C2}_spec.json`), cross-checked with small scripts (no large-file reads).

## 1. Reconciling n_iterations=13 vs the 144-row grid CSV — MATERIAL

`sticky_tier_RETURN.json` reports `"n_iterations": 13`. The grid CSV the frozen point was chosen from
(`sticky_tier_grid.csv`) has 144 rows and is confirmed byte-identical to `sticky_tier_gridC1_grid.csv`
(`diff` = no output). The design note's "Files" section correctly discloses this identity. But 144 is itself
only ONE of four sequential grids actually run:

| grid | spec file | combos (recomputed from spec) | matches design note |
|---|---|---|---|
| A | `sticky_tier_gridA_spec.json` (content only recoverable from the unlettered `sticky_tier_grid_spec.json`, see §5) | 4·4·4·3·2 = 384 | yes |
| B | `sticky_tier_gridB_spec.json` | 5·3·3·3 = 135 | yes |
| C1 | `sticky_tier_gridC1_spec.json` | 4·3·3·4 = 144 | yes |
| C2 | `sticky_tier_gridC2_spec.json` | 1·2·1·2·4·4 = 64 | yes |
| **total** | | **727** | matches design note's "727 combinations" exactly |

Independently reconstructed combo counts from the spec files (not just trusting the design note's arithmetic)
match 727 exactly. `n_iterations: 13` in RETURN.json is a count of **harness invocations** (4 grids run once
each + ~9 single/smoke/diag runs, per the design note's "Iteration count" section), not a count of parameter
combinations examined. **727 (or ~735 including single diagnostic runs) is the correct number to use for any
selection-haircut / multiple-testing discussion, not 13.** This is disclosed honestly in the design note text
itself (which spells out "Total parameter sets touched: 735") but NOT in the machine-readable RETURN.json, which
is the file most likely to be read programmatically for a later meta-analysis across all six candidates — a
reader of RETURN.json alone would understate the search breadth by ~55x.

## 2. Plateau vs peak — grid audit — mitigating evidence

From `sticky_tier_VERIFY.json.grid_audit` (recomputed independently from the CSV, matches exactly):
* `grid_max_sharpe` = 0.6808, `grid_median_sharpe` = 0.5037, std (recomputed) = 0.0853, n=144.
* `frozen_sharpe` = 0.6116, `frozen_rank` = 15 of 144, `frozen_percentile` = 0.903.
* `share_grid_sharpe_ge_0.425` (G2 bar alone) = 0.792; `share_grid_passing_G2_G3_G4` (all three core gates) = 0.556.
* One-step neighbourhood (7 points): min 0.5137, max 0.6779, 100% within 25% of frozen.

The frozen point is at the 90th percentile of Sharpe within C1, not the argmax (0.68), and 55.6% of the
144-combo grid passes all three core risk/return gates simultaneously — a wide basin, not a narrow peak. This is
genuine evidence against knife-edge selection **within the C1 grid**. Caveat: C1's ranges (target_vol 0.12-0.15,
hl 16-26, long_mult 4-12) were chosen *after* seeing grid B's results — i.e. this is a sequentially-narrowed
(adaptive) grid, not a single-shot search over the originally plausible range (target_vol 0.12-0.20 in B, hl
5-20 in A). Reported plateau/pass-rate statistics on an already-zoomed-in grid are optimistic relative to what
an equivalent non-adaptive search over the full original ranges would show — standard for iterative research,
but it means the 55.6%/90th-percentile figures overstate robustness to the *initial* modelling choices, only
understating robustness to the *final* parameter choices given the structure was fixed.

## 3. Sub-sample stability — is 0.61 a calm-decade-filter artefact? — MATERIAL, mechanism clarified

`subsamples` in VERIFY.json:

| split | period | Sharpe | CAGR | chg/yr |
|---|---|---|---|---|
| half 1 | 1990-01 – 2001-03 | **0.793** | 11.9% | 0.71 |
| half 2 | 2001-04 – 2012-06 | **0.358** | 3.0% | 0.18 |
| third 1 | 1990-01 – 1997-06 | 0.982 | 15.4% | 1.06 |
| third 2 | 1997-07 – 2004-12 | **NaN** | 3.4% | **0.00** |
| third 3 | 2005-01 – 2012-06 | 0.439 | 3.7% | 0.27 |

The middle third (7.5 years, 1997-07 to 2004-12) has `max_dd_pct=0.0`, `changes_per_year=0.0`: the model is in
cash for the *entire* period, so both the numerator and denominator of the Sharpe ratio collapse to ~0 and it is
undefined — confirmed against the design note's own account ("cash from 1997-03-31 to 2005-02-07"). The
coordinator's framing ("calm-decade-filter artefact") is not quite the right mechanism, though — see §4 for why —
but the underlying concern is correct and independently confirmed: **the whole-period 0.612 Sharpe is the
weighted outcome of one strong invested spell (0.98), one inert cash spell (NaN, contributes nothing but its
T-bill accrual), and one weak invested/mostly-cash spell (0.44) that is itself dominated by sitting out the GFC.**
The halves split shows a >50% in-sample decay already (0.79 → 0.36) with no OOS data involved at all. With only
10 total position changes in 22.5 years, this is a small-effective-sample-size problem, not primarily a
selection-bias-in-the-grid problem (§2 shows the grid itself is not narrowly peaked). The design note's own
Honest Weakness #2 says almost exactly this ("0.61 should be read as avoided 2000-02 and 2007-09, not as a
repeatable timing edge") — this section independently confirms it with the subsample numbers and elevates it to
a formal disclosure requirement.

## 4. T-bill accounting: affects CAGR, not the reported Sharpe — MATERIAL (correction)

`engine.py::monthly_stats` computes Sharpe as `mean(monthly excess over TB3MS) * 12 / (std(monthly excess) *
sqrt(12))`. On a 100%-cash day the model's raw return equals `rf`, so its **excess** return is ~0 (net of the
negligible financing/cost terms, which are zero when leverage is 0) — cash days contribute ~nothing to either
the mean or the variance of the Sharpe calculation. Therefore **the reported Sharpe of 0.612 is not inflated by
harvesting the risk-free rate** — it is already computed net of it. The design note's disclosure that "2.1 of
7.4 CAGR points are T-bill interest" is real and correctly flagged, but it is a **raw-CAGR / Demeter-comparison**
issue (Demeter books cash at 0%, so the fair CAGR to compare is 5.31%, not 7.38%), not a Sharpe-inflation
mechanism. RESULTS.md should keep these two statements separate: the CAGR-vs-Demeter comparison needs the
T-bill-zeroed column (5.31% dev_1990, correctly provided), but the Sharpe figure needs no such adjustment.
Conflating them would double-count the same caveat or misapply it to the wrong metric.

## 5. Stress episodes: zero live decisions in any of the nine DEV crises — MATERIAL

`dev_results/sticky_tier.json.stress_episodes` (not surfaced as a table in the design note, and not present in
`sticky_tier_VERIFY.json` — `verify_tools.py` does not compute a `stress_episodes` field at all; it exists only
in the main harness JSON). Full read of all nine episodes:

| episode | avg_leverage | pct_days_cash | n_changes | model total % | SPX total % |
|---|---|---|---|---|---|
| 1987 crash | 0.0 | 100% | 0 | +2.17 | -24.97 |
| 1990 Kuwait | 0.0 | 100% | 0 | +3.43 | -8.57 |
| 1998 LTCM | 0.0 | 100% | 0 | +2.11 | +4.86 |
| 2000-02 bear | 0.0 | 100% | 0 | +9.66 | -47.20 |
| 2002-03 recovery | 0.0 | 100% | 0 | +1.31 | +45.52 |
| 2007-09 GFC | 0.0 | 100% | 0 | +2.20 | -54.77 |
| 2009 recovery | 0.0 | 100% | 0 | +0.11 | +67.41 |
| 2010 flash | 0.0 | 100% | 0 | ~0.04 | (per design note -8.4%) |
| 2011 debt | 0.0 | 100% | 0 | (per design note 0.0%) | -5.6% |

Every single one of the nine named DEV stress episodes shows `n_changes=0` and `pct_days_cash=100%`: the model
was **already** in cash before each window opened and made no decision inside any of them (confirmed consistent
with `turnover_clustering`: 10 total changes, 0% of them on top-decile-vol days). This matches, and sharpens
with a complete count, the design note's own admission for 1987/2008 ("the frozen rule was already in cash for
regime reasons... the cost of stickiness shows up instead as late RE-levering"). The implication for RESULTS.md:
**sticky_tier has never, in 62.5 years of DEV data, been observed to make a live risk-reducing decision during a
crisis** — its entire "de-levers in genuine stress" character (as it might be summarised loosely) is
pre-positioning taken 2 months to 8 years in advance, not a tested reaction. G4 ("no ruinous era") is passed
honestly, but it tests "was the model positioned correctly going in," never "does it react correctly to a live
shock" — a materially different and untested claim.

## 6. G6 plateau: meaningful for parameter-space robustness, not for effective-bet-count — answering the
coordinator's question directly

G6 (90% of 20 perturbations within 25% of base Sharpe, bar 50%) is a real, independently-recomputed pass (see
raw rows in `sticky_tier.json.plateau_dev_1990`: only `target_vol` at -15%/-30% fail, at 0.364/0.367, "the rule
goes to ~85% cash" per the design note — confirmed). It is meaningful evidence that the frozen point is not a
knife-edge in the five-dimensional parameter space: nearby parameter settings still produce roughly the same
handful of regime-timing decisions (same rough dates for the 1987/1997/2007 exits and 1992/2005 re-entries), so
the strategy's qualitative behaviour is not a coincidence of the exact frozen values. **But G6 cannot and does
not detect the separate fragility identified in §3 and §5**: a rule can be arbitrarily robust to ±30% parameter
perturbation while still deriving its entire track record from ~2-3 multi-year, binary regime calls (10 position
changes total) rather than a large sample of quasi-independent bets. Perturbing `target_vol`/`h`/`hl`/`long_mult`
mostly re-tests whether the *same* few calls still fire near the *same* dates — it is a test of local sensitivity,
not of sample size. Both statements should stand together in any writeup: "not knife-edge tuned" AND "thin
effective sample, dominated by whether ~3 historical vol-regime shifts were caught."

Separately, confirmed the designer's own flagged observation on integer-parameter rounding: the `P` perturbation
rows for step -0.30 and -0.15 are **literally identical** (`value=4`, `sharpe=0.5891925045271199` both times) in
`plateau_dev_1990.rows`. Of the 20 reported perturbations, only 19 are distinct evaluations; recomputed on
distinct configs the share-within-tolerance is ~17/18 (94%) rather than 18/20 (90%) — doesn't change the G6
pass/fail (bar is 50%) but the reported plateau statistic contains one duplicate row exactly as disclosed.

## 7. Expected OOS Sharpe — reasoning

Inputs: grid-interior estimate (C1, adaptive-narrowed) mean 0.505 / std 0.085, frozen point at the 90th
percentile (not argmax) → within-C1 selection bias is modest since the frozen point was chosen for robustness,
not performance (z ≈ 1.28σ above the grid mean, consistent with an "interior of the plateau" choice rather than
a peak). Applying an extreme-value-style haircut for the true multiple-testing exposure (N≈727 combinations
across 4 sequential grids, σ≈0.085): E[max of N draws] − true ≈ σ·√(2·ln N) ≈ 0.085·3.63 ≈ 0.31, which would
pull the grid's own reported *maximum* (0.68) down to ≈0.37 — the frozen point (0.612) is already below that
argmax so this specific correction matters less for it directly, but it calibrates how much of the 0.68-0.61
range in this grid is noise.

Against that base case, three DEV-internal facts argue for shading the range further down, not up:
(a) the in-sample half-split already shows 0.79→0.36, a real decay with zero new data;
(b) the entire "crash protection" record is untested reaction (§5) — OOS (2012-2026) contains a fast V-shaped
shock (Mar-2020) that the design note itself names as the mechanism's known failure mode ("a recovery that
starts while vol is still high... is missed in full... the opposite of what the record shows in Mar/Apr-2020");
(c) the adaptive/sequential grid search (§1, §2) has an unquantified additional overfitting component beyond the
local within-C1 statistics.

**Expected OOS Sharpe range: 0.10–0.35**, materially below both the DEV headline (0.612) and the pre-registered
OOS acceptance bar (0.73). Central risk: whether the slow (160-session) EWMA happens to be in cash exactly
through Feb–Apr 2020 and again correctly re-enters the subsequent multi-year bull run — the same kind of binary,
low-n bet that generated the DEV record — makes this closer to a coin-flip on a couple of episodes than a
estimate with a tight confidence interval.

## 8. Minor documentation findings

* Design note's "Iteration count" section says "5 grids" but lists four lettered grids (A/B/C1/C2) summing to
  727 (independently verified exact); it also says "8 single runs" while listing 9 items (smoke, 4×diag2, final,
  3×diag3). Neither error changes any gate result or the verified 727-combination total; both are small
  arithmetic slips in the note's own prose.
* `dev_results/sticky_tier_grid_spec.json` (unlettered) is a leftover filename holding grid A's original spec
  (`v_lo/gap/h/hl/floor`, 384 combos) from before the A/B/C1/C2 naming convention was adopted — there is no
  `sticky_tier_gridA_spec.json` on disk. Confirmed this is not a hidden fifth grid: its content and combo count
  match the design note's description of grid A exactly.
* `stress_episodes` (named in VERIFY_BRIEF.md as a field to consult) is not produced by `verify_tools.py` and is
  absent from `sticky_tier_VERIFY.json`; it exists only in the main harness output `dev_results/sticky_tier.json`.

## Verdict

No SEVERE finding. The design note is unusually candid and already argues against its own strategy in several
places (Honest Weaknesses §1-6); the grid audit independently reconciles; the plateau is real; no evidence of
hidden cherry-picking. The MATERIAL findings above (true trial count, small-effective-bet-count fragility,
T-bill/Sharpe clarification, untested-stress-reaction, adaptive-grid caveat on G6) do not individually invalidate
the candidate but must all be carried into RESULTS.md; together they justify treating sticky_tier's OOS prospects
as weak (well under the 0.73 bar) even though it passes every DEV gate.
