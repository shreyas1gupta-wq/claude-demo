# L2 verification — vix_vrp_v2 (Overfit & plateau)

Verifier: adversarial L2, pass-2 three-lens review. Scope: is the frozen point a plateau or a peak; selection
haircut given the iteration count; sub-sample stability; low-exposure-artifact check. No parameters proposed, no
`evaluate.py`, no `results/` touched, nothing in `signals/` edited.

## Files examined
`signals/vix_vrp_v2.py` (full read), `dev_results/vix_vrp_v2.json`, `dev_results/vix_vrp_v2_VERIFY.json`,
`dev_results/vix_vrp_v2_RETURN.json`, `dev_results/vix_vrp_DESIGN_NOTE.md` (the only design note that exists — see
L1 Finding 3; it contains the v2 "Part 2" sections in full so it is the substantive record used here),
`dev_results/vix_vrp_v2_gridC_grid.csv` (216 rows), `dev_results/vix_vrp_v2_gridD_grid.csv` (72 rows),
`dev_results/vix_vrp_v2_ablation_all.csv` (21 rows), `dev_results/vix_vrp_v2_ablation_round2.csv` (16 rows),
`dev_results/vix_vrp_v2_map.csv` (malformed/truncated export — cross-checked against the design note's own printed
Round-3 table instead), `dev_results/vix_vrp_VERIFY.json` (original, for the lag-test comparison), `features.py`
(`realized_vol`), `engine.py` (`run`, `pos = lev.shift(1)`), `PREREG.md`, `DESIGN_BRIEF.md` §"What the record says".
Two throwaway scripts were written to independently recompute claims rather than take them on faith (`scratch_l2_gridC.py`,
`scratch_l2_legcheck.py`, both in the model dir, not part of the deliverable set) — outputs reproduced below.

---

## Finding 1 — SEVERE — the entire +0.07 Sharpe edge is not distinguishable from the noise of the search that found it

`dev_results/vix_vrp_DESIGN_NOTE.md` reports the new ELEVATED-VRP-gate leg fires on 132 of ~5,670 days (2.3%), mean
+19.8 bp/day at 18.5% annualised vol, "leg t-stat ≈ 1.9." I independently rebuilt this from the signal function
(`signals/vix_vrp_v2.py::vix_regime` + `features.realized_vol`), correctly lagging the day-t decision to its day-t+1
execution per `engine.run`'s `pos = lev.shift(1)` convention (the first attempt, without the lag, gave the *opposite*
sign — a reminder of how easy it is to get this backwards):

```
n_leg_days = 132
leg mean daily excess = +19.99 bp, ann vol = 18.60%, day-level t-stat = 1.960
spell-level (54 spells, median length 1 day, max 13):  t-stat = 1.795
```

This confirms the design note's own number is computed correctly. But the context that number sits in is not
reassuring:

* **The candidate's own final calibration grid has a standard deviation almost as large as the whole claimed edge.**
  `dev_results/vix_vrp_v2_gridC_grid.csv` (216 combos, the grid that picked `vrp_elev`): dev_1990 Sharpe mean
  **0.6270**, median 0.6302, **SD 0.0699**, range 0.4614–0.8118 (recomputed directly from the CSV). The claimed v2-vs-
  original improvement is **+0.070** (0.6783 vs the original's frozen 0.6084) — i.e. the entire headline improvement
  is smaller than **one standard deviation** of the Sharpe dispersion across the candidate's own neighbouring
  parameterisations. A number that size cannot be told apart from where-you-happen-to-land-in-the-grid noise.
* **The frozen point is not the grid's peak (a mitigating fact) but the search that produced it is wide.** The
  frozen point (v_calm 15.5/v_panic 30/hyst 0.12/vrp_elev 0.12) ranks 53rd of 216 in Grid C (24.5% of cells score
  higher; the grid max is 0.8118 at v_calm 14/hyst 0.08/vrp_elev 0.10). Separately, `vix_vrp_v2_ablation_round2.csv`
  row `R2_hold5_a0.10` (a 5-day-minimum-hold functional form) posts Sharpe **0.7564** — higher than the frozen
  "raw-gate" default — and was not adopted (the design note argues the hold/smooth/band forms worsen the bear and
  GFC outcomes on average, which is a legitimate qualitative reason, but it means the +0.07 number was not the
  result of taking the best of the search; it was one qualitatively-preferred point among many that beat the
  original by varying, and sometimes larger, margins). Between the ablation rounds (21 + 16 + 42-cell map, ~35 net
  new) and grids C+D (288), roughly 360 DEV configurations were evaluated in Part 2 alone hunting for a way to make
  the ELEVATED regime pay. A day-level t of 1.96 (spell-level 1.80) surviving that scale of directed search does not
  clear any reasonable multiple-testing-adjusted bar — a Bonferroni correction for even a conservative ~40 effectively
  distinct hypotheses (the threshold x functional-form space alone) would require |t| ≈ 3.2-3.4, not 1.9-2.0.
* **The edge's sign is not even stable to one extra session of execution delay.** `dev_results/vix_vrp_v2_VERIFY.json`
  `lag_test_dev_1990` (independently re-read, matches the coordinator's numbers and L1's Finding 2 exactly): v2-vs-
  original is **+0.070** at the harness's exact next-day-open convention, **−0.064** with one extra session of delay,
  and +0.016 with two. A plateau claim that only holds at one exact execution-timing convention, and flips sign one
  session away, is a peak in the timing dimension even though it is a genuine (and separately verified, see grid
  perturbation table below) plateau in the six declared *parameter* dimensions — the G6 battery tests the latter, not
  the former, so gate-passing does not certify this axis.
* **The point is already short of the study's own bar even with zero degradation.** `PREREG.md`'s acceptance
  criterion is OOS Sharpe **> 0.73**; the frozen DEV Sharpe is 0.678. Unless OOS *improves* on DEV (uncommon, and not
  what any of the above evidence suggests), the candidate needs the full DEV number to hold up with no shrinkage at
  all just to clear a bar it does not clear on DEV.

Given "default to refuted when the evidence is ambiguous," and that the sole basis for preferring v2 over the
already-accepted original (per the pre-committed selection rule) is an effect this analysis cannot separate from the
search's own noise floor, I rate this SEVERE.

## Finding 2 — MATERIAL (cross-lens) — retirement rule depends on a gate L1 reports as failed

The design note's pre-committed rule is explicit: "v2 replaces the original only if it beats the original's dev_1990
Sharpe with maxDD no worse than −25% and passes all seven gates." On the numbers as self-reported (Sharpe 0.6783 >
0.6084; maxDD −19.78% vs the −25% bar; `gate_check.py` prints `ALL GATES PASS`) the rule is satisfied. However, L1's
independent review of this same candidate reports `G7_param_budget` as actually failing (true tunable count 8 —
`LEV_CALM` and `LEV_PANIC` were each value-compared against an alternative on DEV per the ablation CSVs and rejected,
which the brief's own standard classifies as tuned, not structural). I did not re-derive the tunable count myself
(out of L2's scope), but if L1's finding stands, "passes all seven gates" is false and the retirement of `vix_vrp` in
favour of `vix_vrp_v2` proceeded on an unmet precondition. This is recorded here because it is exactly the kind of
process-integrity check L2 is asked to make ("check that the retirement rule was applied correctly") and it changes
whether Finding 1's grid/plateau analysis is even auditing the candidate that was supposed to survive to this stage.

## Finding 3 — MATERIAL — the design note overstates the new leg's cross-period consistency; the arithmetic does not close

The design note's Honest-weaknesses §1 states the leg is "positive in 5 of 7 sub-periods, negative in 1990-94, the
2000-02 bear and 2009." Three named negative periods out of seven arithmetically leaves **four** positive, not five.
My independent per-period reconstruction (same lagged leg definition as Finding 1, periods matching the design
note's own Part-1 table) confirms exactly 4 of 7 positive and reproduces the day-counts and the aggregate magnitude
almost exactly:

| period | n days | leg sum excess (bp) | sign |
|---|---|---|---|
| 1990-1994 | 25 | −299.5 | − |
| 1995-1999 | 48 | +1191.9 | + |
| 2000-02 bear | 12 | −233.2 | − |
| 2003-2007 | 4 | +717.5 | + |
| 2007-09 GFC | 24 | +979.6 | + |
| 2009 recovery | 18 | −49.7 | − |
| 2010-2012H1 | 20 | +576.3 | + |

(4 positive / 7; day-total 151 vs the note's 132 because a handful of days fall on period boundaries by my period
cut vs the note's — immaterial to the sign count.) Two things follow: (a) the note's own "5 of 7" framing is simply
wrong and overstates how broadly the effect held up across history — a small but real error in the exact sentence
used to argue the thin leg is not a fluke, and it should be corrected before this is cited further; (b) the
"2003-2007" period contributes only 3-4 leg-days out of a ~1,250-day period — far too few to count as one of the
seven independent confirmations the "X of 7" framing implies. Effective sample coverage for the cross-period claim
is closer to 5 usable periods (1990-94, 1995-99, 2000-02, GFC, 2009-rec, 2010-12H1 all have ≥12 days; 2003-2007 does
not), of which 3 are positive and 2-3 negative depending how the near-zero 2009-recovery print (−49.7 bp over 18
days) is read.

## Finding 4 — MATERIAL — headline Sharpe is front/middle-loaded; the most recent third is the weakest and closest to "no edge"

`dev_results/vix_vrp_v2_VERIFY.json` `subsamples` (read directly, not estimated):

| split | window | Sharpe |
|---|---|---|
| half 1 | 1990-01 .. 2001-03 | **0.844** |
| half 2 | 2001-04 .. 2012-06 | **0.530** |
| third 1 | 1990-01 .. 1997-06 | 0.637 |
| third 2 | 1997-07 .. 2004-12 | **0.892** |
| third 3 | 2005-01 .. 2012-06 | **0.551** |

The 0.678 headline is not evenly earned: the middle third (1998 LTCM through the 2000-02 bear and the 2002-03
recovery) drives the strongest sub-period Sharpe (0.892); the most recent third (2005-2012H1, which contains the
GFC and 2009 recovery) is the weakest at 0.551 — barely above the *original's* un-improved 0.6084 headline and well
below the study's 0.73 acceptance bar. The sub-period closest in calendar terms and market-structure terms to the
coming OOS window is the one where this family's edge is thinnest. (`dev_1950` cannot serve as an independent
before/after check here: no VIX exists before 1990, so both v2 and the original are ~86% cash/T-bill in that window
— this is a structural non-finding common to the whole family, not v2-specific, listed for completeness only.)

## Finding 5 — cleared — not a low-exposure/leverage-scaling artifact

`dev_results/vix_vrp_v2.json` `reference_bh_1x.dev_1990.sharpe` = **0.3851** (buy-and-hold 1x SPY, same window, zero
cost). The model's average leverage is 0.61 (1.61 when invested; `leverage_distribution_dev_1990`: 0x 61.9%, 1x
15.0%, 2x 23.1%). Scaling a benchmark's exposure by a constant factor leaves its Sharpe roughly unchanged (numerator
and denominator scale together), so a 0.61x-exposure version of buy-and-hold would still show a Sharpe near 0.385,
not 0.678. The model's Sharpe is well above that reference, meaning the result is not simply "cash is safe" dressed
up as skill — the regime-timing (concentrated in the inherited CALM/PANIC legs per the Part-1 audit) is doing real
work, independent of anything Finding 1-4 say about how much of the *incremental* v2 edge specifically will hold up.

## Finding 6 — MATERIAL (required disclosure, restated from the design note) — the candidate is below the study's own OOS acceptance bar on DEV alone

`PREREG.md` requires OOS Sharpe > 0.73 for acceptance. The frozen DEV Sharpe is 0.6783 (3/60), 0.642 (6/90), 0.692
(2/40) — every one of the three cost rows is already below 0.73. This is not a new number (it follows directly from
files already in the record) but it belongs in `RESULTS.md` explicitly: this candidate cannot pass acceptance
without OOS performance *exceeding* its own DEV performance, which the selection-noise analysis in Finding 1 gives
no reason to expect.

## Minor

* Grid C's own maximum (0.8118, v_calm 14/hyst 0.08/vrp_elev 0.10, 24.5% of the 216-cell grid beats the frozen
  point) and the round-2 hold5 variant (0.7564, not adopted) show the designer did not chase the argmax — a point in
  the process's favour — but they also show the plateau's own width (0.46-0.81, a ~0.35 Sharpe range) dwarfs the
  +0.07 claimed edge, so quoting 0.678 as "the" answer overstates the precision this family of rules actually
  supports. Not blocking on its own; folded into Finding 1's SEVERE for the haircut estimate.
* Most of the model's *absolute* Sharpe (not the v2-specific increment) is carried by three episodes — 1998 LTCM
  (+24.0%), 2002-03 recovery (+28.1%), 2009 recovery (+43.6%) — all on the inherited, unchanged 1x PANIC leg, not
  the new gate. Already disclosed in the Part-1 audit of the original; restated here only because "which single
  episodes drive it" is an explicit L2 checklist item.
* `dev_results/vix_vrp_v2_map.csv` is malformed (a single "hyst03" column header repeated, not the six gate-form
  columns the design note's own printed table shows) — I cross-checked the round-3 numbers against the design
  note's inline table instead, which is internally consistent with `vix_vrp_v2_ablation_round2.csv`'s raw-gate rows
  (a=0.07..0.20 match exactly). Same "artifact filed under a name that degrades independent audit" pattern L1 noted
  for the missing `_grid.csv` and `_DESIGN_NOTE.md` files — noted, not re-litigated.

---

## Summary for JSON output

* `refuted = true` (Finding 1 is SEVERE on its own; Finding 2 cross-references an independent SEVERE from L1).
* Expected OOS Sharpe for `vix_vrp_v2`: given (a) the DEV point (0.678) is already below the 0.73 acceptance bar,
  (b) the incremental +0.07 over the already-accepted original is smaller than one SD (0.070) of the candidate's own
  calibration-grid dispersion and does not survive a one-session-slower fill, and (c) the most recent DEV third
  (2005-2012H1) posts only 0.551 — I expect the *increment* to shrink to roughly zero out of sample (plausibly
  slightly negative, as the lag test already shows at lag1) and the *candidate's* OOS Sharpe to land close to what
  the plain VIX-level machine alone would be expected to deliver: **range 0.35-0.55**, i.e. materially below both the
  DEV headline (0.678) and the acceptance bar (0.73).
