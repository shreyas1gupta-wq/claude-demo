# vix_vrp — L2 verification (Overfit & plateau)

Verifier: adversarial L2, pass 2. Candidate: `signals/vix_vrp.py` (original, reinstated after `vix_vrp_v2` was refuted
— see PREREG.md "Verification outcomes"). Scope: L2 only (rank/plateau, sub-sample stability, DEV bet count,
low-exposure artefact check, expected OOS range). No `evaluate.py` run, no `results/` touched, no params proposed.

Evidence sources: `dev_results/vix_vrp.json` (harness), `dev_results/vix_vrp_VERIFY.json` (battery), `dev_results/
vix_vrp_gridA_grid.csv` (210 combos), `dev_results/vix_vrp_gridB_grid.csv` (225 combos), `dev_results/
vix_vrp_DESIGN_NOTE.md` Part 1 (the pass-2 auditor's read of these same grids — cross-checked, not taken on faith),
`dev_results/vix_vrp_v2_ablation_all.csv` rows V1_calm3x / V0c_panic2 (post-hoc, run after freezing).

## 1. Rank / plateau in grids A and B

Recomputed independently from the CSVs (`gate_check.py` bar Sharpe>0.425 used as the G2 proxy):

| grid | n | min | p10 | median | p90 | max | frozen (0.6084) rank | frozen percentile |
|---|---|---|---|---|---|---|---|---|
| A (v_calm×v_panic×hyst, rv_win/vrp_min@default) | 210 | 0.240 | 0.378 | 0.500 | 0.617 | 0.728 | 28 / 210 | top 13.3% |
| B (rv_win×vrp_min×hyst×v_calm, v_panic@default) | 225 | — | — | 0.494 | — | 0.688 | 13 / 225 | top 5.8% |

Share of grid A passing the G2 proxy (Sharpe>0.425): 75.2%. Share passing G2+G3 (maxDD>-30%): 74.3%. Grid B: G2 76.4%,
G2+G3 71.6%. Matches the design note's own figures (independently reproduced, not just copied).

**Local neighbourhood (grid A, hyst held at the frozen 0.12, varying v_calm/v_panic only):** frozen point (15.5/30)
ranks 7th of the ~12 cells in this slice, sandwiched between 0.660/0.662 (v_calm 15.0) and 0.573/0.611 neighbours —
a genuine shoulder, not an isolated spike; moving v_calm from 15.5→15.0 (a plausible alternative round number) would
have scored *higher* (0.660 vs 0.608), which argues against cherry-picking the maximum.

**One-step perturbation battery** (`dev_1990.plateau_dev_1990`): 20/20 within 25% tolerance on all five declared
params, including the two params that barely matter operationally (see §3). This is a real local plateau.

**Caveat on all of the above:** grids A/B were run by the pass-2 auditor in 2026-09 as a check on an already-frozen
point (per coordinator's note), not as pass-1's actual search process — no design note exists for the original's
1990-vintage selection. So this evidence answers "how flat is the surface around the frozen point today," not "how
many trials pass-1 actually ran to get there." Treat the rank/percentile numbers as a lower bound on selection
exposure, not proof of restraint. (Disclosure ownership: L1's true-tunable-count finding; noted here because it
directly weakens the confidence of the haircut in §5.)

**Finding (MATERIAL):** the frozen point is not the peak of either audited grid — it sits at the 87th (A) /
94th (B) percentile, with a same-family neighbour (v_calm=15.0, all else equal) scoring materially higher
(0.660 vs 0.608) — but because the actual pass-1 selection process is undocumented, this cannot be confirmed as
evidence that pass 1 avoided peak-picking; it only shows today's local surface is not knife-edge.

## 2. Lag sensitivity

`vix_vrp_VERIFY.json.lag_test_dev_1990`: base Sharpe 0.6084 → lag1 0.4862 (−20.1%) → lag2 0.4153 (−31.7%). CAGR
10.61% → 8.85% → 7.94%; maxDD widens −19.78% → −28.31% → −32.50%.

Unlike `sticky_tier` (lag-robust: 0.612 / 0.610 / 0.604, ≈flat) or `vix_vrp_v2` (sign-inverting: +0.68 → −0.06 at
lag1, decisive for that refutation), `vix_vrp` neither stays flat nor inverts — it decays substantially but stays
solidly positive and above 0.4 even at lag2. Mechanistically this is explicable: leverage steps are discrete (0/1/2x)
and hysteresis holds the position, so a shifted decision date does not just delay a smooth signal, it moves the
specific calendar day on which a 0→2x or 0→1x jump happens — and with only ~57 leveraged spells in 22.5 years, a
non-trivial share of the annual Sharpe is earned on the handful of days immediately around those jumps (entering a
rebound one day earlier/later, or catching a −7% day inside PANIC one day differently). The maxDD widening under lag
(−19.8% → −32.5%) confirms some of the frozen point's drawdown control specifically depends on same-day timing.

**Finding (MATERIAL):** the strategy is meaningfully — not catastrophically — sensitive to execution-day timing: a
one-session delay costs ~20% of Sharpe and ~8.5 points of maxDD, and a two-session delay costs ~32% of Sharpe and
~13 points of maxDD. Any OOS or paper accounting must either replicate same-day-close execution exactly or expect a
Sharpe closer to 0.42–0.49 than to the 0.608 headline. This also means the docstring's "the 16-minute VIX-timing gap
is ignored, as the literature does" is a reasonable approximation for the *hysteresis levels* (a few tenths of a VIX
point rarely flips a wide band) but is not license to be casual about *decision-to-execution* lag more broadly — the
two are different kinds of delay and only the second was tested here.

## 3. Are all five declared tunables actually doing work?

`vix_vrp_DESIGN_NOTE.md` (Part 1, audit): the VRP filter overrides the regime-implied leverage on only **53 of
~5,670 DEV days (0.9%), all inside PANIC, never inside CALM**, over 22.5 years. Grid B confirms `vrp_min` is flat
across its entire audited range (−0.25..−0.05 → 0.47–0.51, essentially noise) and `rv_win` is flat for 10–21 (≈0.52)
with only rv_win=5 a cliff (mean 0.374, whipsaw). So of the 5 declared tunables, 2 (`rv_win`, `vrp_min`) have almost
no realised effect on the frozen backtest — the "variance-risk-premium crash filter" that gives the file half its
name and its stated mechanism is, on the DEV record, a rarely-firing tail rule bolted onto what is functionally a
3-parameter VIX-level state machine (`v_calm`, `v_panic`, `hyst`).

This cuts two ways for overfitting risk: (a) it *reduces* the effective search dimensionality that produced the
0.608 headline — fewer knobs that can have been tuned to noise; (b) it means the plateau evidence in §1, which
formally spans a 5-D declared space, is really only testing robustness in 3 live dimensions plus 2 dimensions that
were always going to look flat because they rarely bind. The audited grids do not materially change this conclusion
because A and B both hold most of the near-inert params fixed while varying the live ones.

**Finding (MINOR, context for §5):** treat the effective tunable count for haircut purposes as ~3 live parameters
(v_calm, v_panic, hyst), not 5 — this is a *smaller* multiple-testing exposure than the file's own G7 count implies,
which is a point in the candidate's favour, but it also means the audited grids' "435 combinations" figure
overstates independent trials by roughly the ratio of live to declared dimensions.

## 4. Sub-sample stability and how many DEV bets the Sharpe rests on

`vix_vrp_VERIFY.json.subsamples`:
* Halves — 1990-01→2001-03: Sharpe **0.839**; 2001-04→2012-06: Sharpe **0.402**. The second half is 48% of the first.
* Thirds — 1990-97: 0.634; 1997-04: 0.830; 2005-12: 0.420. Not a monotonic decay: the strong middle third is the
  2000-02 bear (where cash protection paid off hugely, +15.1% vs SPY −47.2%) and the weak last third carries the
  2007-09 GFC (model −15.7%, its worst episode). So this is not "the edge is decaying with time," it is "the last
  third happens to contain the one episode (GFC) where the PANIC leg lost money" — a single-episode effect, not a
  trend, but the practical consequence for an OOS expectation is the same: **the last available ~7.5 DEV years scored
  0.42, not 0.61.**

`dev_1950` vs `dev_1990` (0.362 vs 0.608) is not a genuine contradiction either: `signal_coverage.pct_cash_1950_1989
= 100.0%` — the model is in forced cash for the entire 1950-1989 stretch (no VIX regime signal exists before ~1990),
so `dev_1950`'s Sharpe is just T-bill-for-40-years diluting the real 22.5-year record, not an independent earlier-era
test. Reporting a "dev_1950" number invites the reader to think the rule has been checked against 1962/1973-74/1987
— it has not; `gate_check.py` correctly marks those eras N/A rather than pass/fail, but the headline JSON still
prints a blended Sharpe that looks like a longer, more reassuring sample than it is.

**How many DEV bets:** state-machine occupancy (design note): CALM 26 spells, ELEVATED 58 spells (0x, not a bet),
PANIC 31 spells — 57 economically active (non-zero-leverage) spells over 22.5 years. But `stress_episodes` shows the
practical drivers cluster into roughly 8-10 distinct macro episodes (1990 Kuwait, 1994-97 calm-bull run(s), 1998
LTCM, 2000-02 bear, 2002-03 recovery, 2007-09 GFC, 2009 recovery, 2010 flash, 2011 debt) — the 31 PANIC spells and
some CALM spells are hysteresis-driven fragments of these same handful of episodes, not independent draws. A more
honest estimate is **~10-15 independent regime-episodes** underlying the 0.608 Sharpe, the same order of magnitude
as `sticky_tier`'s disclosed "~10 decisions in 22.5 years" (which held). More concentrated still: the design note's
own PANIC-leg-removal test (setting `LEV_PANIC=0`) collapses Sharpe to 0.271 — **more than half of the strategy's
entire risk-adjusted return comes from the 13.6%-of-days PANIC state alone.**

**Finding (MATERIAL):** the 0.608 DEV Sharpe rests on a small number (order 10-15) of correlated macro episodes, and
over half of it is attributable to the PANIC leg (13.6% of days, 31 hysteresis spells clustering into perhaps 5-6
genuinely distinct panics). An OOS sample with a different mix or fewer VIX>30 episodes than 1990-2012 had would
mechanically produce a materially different Sharpe even with a perfectly-generalising rule.

**Finding (MINOR):** the "dev_1950" figure quoted in RESULTS-facing material should be labelled explicitly as
"1950-1989 forced-cash / T-bill, no signal available" rather than presented alongside dev_1990 as if it were a
second, independent validation window.

## 5. Low-exposure / cash-heavy Sharpe artefact check

Not applicable as a flaw here — checked and it comes out clean. `reference_bh_1x.dev_1990.sharpe = 0.3851` (unlevered
buy-and-hold SPY) vs the model's `0.6084` at `avg_leverage = 0.588`. If the model were merely "SPY scaled down to
~0.6x," its Sharpe would be statistically indistinguishable from SPY's own Sharpe (Sharpe is scale-invariant to
leverage on the same asset, up to financing-cost drag). Instead the model's Sharpe is **58% higher** than SPY's at
*lower* average exposure — real risk-adjusted improvement, not a low-exposure artefact. (up/down-capture 60%/30% is
consistent with this: it participates more in up days than down days, which is the intended effect of the regime
gate, not noise.)

## 6. Expected OOS Sharpe range and reasoning

Inputs: DEV headline 0.608 (top 13% of a 210-cell local grid, top 6% of a 225-cell local grid, but only ~3 live
tunables); one-step-perturbation plateau clean (20/20 within 25%); lag1/lag2 decay to 0.486/0.415; halves 0.839/0.402;
worst third 0.420; unknown true pass-1 trial count (grids are post-hoc); >50% of the edge concentrated in a PANIC
leg drawn from ~5-6 distinct episodes.

Reasoning (informal Bailey–López de Prado-style deflation, not a formal PSR/DSR computation — insufficient
information on the true historical trial count to do that rigorously, which is itself part of the finding):
* The audited local grids put the median of a plausible search neighbourhood at ~0.49-0.50 with the frozen point at
  the ~90th percentile of that neighbourhood. If the true pass-1 process resembled this search intensity, a fair
  single-point anchor is closer to the grid median (~0.50) than to the frozen point's own value, discounted further
  because grid A/B jointly probe only 3 live dimensions (less multiple-testing exposure than 5 declared params would
  imply — a mitigating factor) but the true N is unverifiable (an aggravating factor for confidence, not for the
  point estimate).
* The lag-adjusted numbers (0.486 / 0.415) are a reasonable proxy for "Sharpe under slightly-less-than-perfect
  execution," which every live/paper implementation will have to some degree.
* The weakest third of DEV (0.420, containing the GFC) is a plausible floor if OOS delivers one comparably hard
  panic episode without a compensating clean rebound; the strongest half (0.839) is not a realistic OOS anchor since
  it is dominated by the unusually clean 1990s bull + one favourable positioning through the 2000-02 bear.

**expected_oos_sharpe_range: 0.30 – 0.55**, central tendency around 0.40-0.45 — i.e. expect roughly a 25-45% haircut
off the 0.608 DEV headline, with the low end driven by lag/execution realism and a GFC-like episode, and the high end
capped by the local-grid median rather than the frozen point's own (not-quite-peak but above-median) value. This is
a plateau-supported estimate, not a peak-supported one — the candidate does not fail L2 outright, but the DEV Sharpe
should not be quoted as the OOS expectation without this haircut stated alongside it.

## Summary of findings

| # | Tag | Finding |
|---|---|---|
| 1 | MATERIAL | Frozen point is not the peak of either audited grid (87th/94th percentile); a same-family neighbour scores higher (0.660 vs 0.608) — but the real pass-1 search process is undocumented, so this shows today's local flatness, not historical restraint. |
| 2 | MATERIAL | One-session execution lag costs ~20% of Sharpe (0.608→0.486) and ~8.5pts of maxDD; two-session lag costs ~32% (→0.415) and ~13pts of maxDD — meaningful timing sensitivity from the discrete leverage jumps, not lookahead, but real for any OOS/paper implementation. |
| 3 | MINOR | 2 of the 5 declared tunables (rv_win, vrp_min) have near-zero realised effect on DEV (VRP filter fires 53/5,670 days) — reduces effective search dimensionality (favourable) but means grids A/B test only 3 live params despite spanning a nominal 5-D space. |
| 4 | MATERIAL | DEV Sharpe rests on ~10-15 correlated macro episodes in 22.5 years, and >50% of total Sharpe is attributable to the PANIC leg alone (13.6% of days; removing it collapses Sharpe to 0.271) — an OOS sample with a different panic mix will move the Sharpe mechanically, independent of rule quality. Sub-sample halves (0.839 vs 0.402) and the weakest third (0.420, GFC-laden) bound a realistic range. |
| 5 | MINOR | The "dev_1950" figure is 100% forced-cash/T-bill for 1950-1989 diluting a blended number; should be labelled as no-signal-available rather than presented as a second validation window. |
| — | (checked, clean) | Not a low-exposure artefact: model Sharpe 0.608 at avg leverage 0.59 vs unlevered SPY Sharpe 0.385 — a genuine risk-adjusted edge, not scaled beta. |

No SEVERE finding under L2. `refuted = false` from this lens.
