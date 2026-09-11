# Can a rules-based dual-engine model reproduce Demeter's record? — pass 2

**Short answer: still no, and pass 2 did not beat pass 1's model either.** Six new candidates were designed under a
pre-registered, development-only protocol (data hard-truncated at 30 June 2012, seven gates, one out-of-sample look per
survivor, three adversarial verifiers per survivor). Five passed the gates. Verification refuted four of them — every one
on the same defect: "structural constants" whose values had in fact been chosen by comparing development results, so
the true parameter count was 7 to 13 against a budget of 6. The one survivor, `sticky_tier`, took its single
out-of-sample look and failed it: **3.23% a year, Sharpe 0.24, 73% of days in cash** (Jul 2012 – Jan 2026, 3 bp per
unit traded and 60 bp financing). The pass-1 incumbent `final_model_fewtrades` remains the recommended model at
**16.78% a year, Sharpe 0.73, −20.5% drawdown** on the same costs. Demeter's published record over the window is
**31.33% a year, Sharpe 1.27, −13.65%**, and SPY's Sharpe (0.95) is still above every model built in either pass.

The interactive version of this note is `report/index.html` (rebuilt by `build_report.py`).

## What changed since pass 1, and why

| | Pass 1 (2026-09-03) | Pass 2 (2026-09-04 → 09-12) |
|---|---|---|
| Cost basis of every headline number | 2 bp, no financing spread | **3 bp / 60 bp** (1.5× the measured 2 bp / 40 bp); 2/40 as a secondary row; 6/90 as stress |
| Development access | evaluator run on the full history, parameters "chosen on data ending 2012-06-30" by the designer's discipline | `dev_harness.py` **hard-truncates the data at 2012-06-30 before the signal is called**; the out-of-sample window is structurally invisible during design |
| Gates | none pre-registered | `PREREG.md`: causality at 5 cut-offs, DEV Sharpe ≥ incumbent, DEV maxDD ≥ −30%, no ruinous era, ≤ 25 changes/yr, plateau ≥ 50%, ≤ 6 tunables — written before any candidate existed |
| Out-of-sample discipline | "computed once per model" | `oos_final.py` refuses ungated modules and second looks and writes every look to `results/OOS_LOOK_LOG.md` |
| Recommendation rule | best DEV Sharpe | best DEV Sharpe among **verified** gate passers, recorded in `PREREG.md` before the look |
| Verification | none | three independent Sonnet verifiers per passer (causality & code; overfit & plateau; mechanism & execution), a SEVERE finding blocks the look |
| Asymmetries the engine grants us | noted | quantified: T-bill on cash days zeroed (Demeter's convention), and per-trade cost scaled by trailing volatility (`compare_final.py`) |
| Disclosure | six models reported | a **seventh pass-1 file, `signals/vix_vrp.py`, was found built but never evaluated or mentioned**; it was audited and its docstring turns out to claim an out-of-sample look pass 1 never recorded |

Two process incidents are logged in `PREREG.md` §Deviations: the design workflow was killed twice by account usage caps
(2026-09-04 and 09-10) and re-launched from banked files; a third launch on 09-11 briefed designers wrongly and was
stopped within a minute. No out-of-sample file was created or read between launches.

## Method (pass 2)

* **Signal contract** unchanged: daily market data → target leverage in [0, 3] for the next session; cash earns the
  3-month T-bill; the engine, features and evaluator are pass 1's, reused unmodified (no bugs found in them by six
  designers and fifteen verifiers across ~6,100 signal evaluations).
* **Development window** 1990-01-01..2012-06-30 (VIX exists from 1990), cross-checked on 1950-01-03..2012-06-30 for
  rules that do not need VIX; four eras and nine dated stress episodes reported for every candidate
  (`dev_results/<name>.json`).
* **Six lenses, fixed in advance** (`PREREG.md`): a two-decision architecture with a real crash exit; a re-entry on
  volatility dissipation that is not a trend filter; the literature's volatility-managed leverage; a whipsaw minimiser;
  the variance-risk-premium file; the inference note's §7 composite.
* **Panel size**: six new signal files, plus the reinstated pass-1 `vix_vrp`. Designers evaluated 5,652 distinct
  parameter sets on the development window (crash_exit_dual 1,326; composite 1,125; dissipation_reentry 864;
  volmanaged 806; vix_vrp_v2 796; sticky_tier 735) plus a 435-combination audit around `vix_vrp`. Every set is in
  `dev_results/*_grid.csv`.
* **Out-of-sample looks in pass 2: one** (`sticky_tier`, 2026-09-12 02:08 IST, one signal, three cost rows). The pass-1
  panel was re-run at the three pass-2 cost rows for a uniform leaderboard (`results/*_p2*.json`); those are not new looks.

## The development gauntlet

All numbers 1990-01..2012-06 at 3 bp / 60 bp unless noted; SPY buy-and-hold on the same window: Sharpe 0.39, CAGR
8.34%, maxDD −50.8%. Full table with eras, stress episodes and iteration counts: `dev_results/PASS2_DEV_TABLE.md`.

| Candidate | Lens | Tunables declared → true | DEV Sharpe | DEV CAGR | DEV maxDD | Chg/yr | Cash % | Avg lev. invested | 2000-02 bear | GFC | 2009 recovery | Gates | Verification | OOS look |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| final_model_fewtrades (incumbent) | pass 1 | 6 | 0.43 | 10.14% | −25.1% | 7.1 | 32 | 2.03 | −21.1% | −8.6% | +6.6% | pass | not re-verified | pass 1 |
| crash_exit_dual | 1 | 6 | 0.45 | 11.19% | −52.8% | 12.0 | 13 | 1.81 | −54.2% | −42.5% | +53.8% | **FAIL** G3 G4 | — | no |
| dissipation_reentry | 2 | 6 → 7 | 0.45 | 7.86% | −12.4% | 3.9 | 52 | 1.04 | +2.8% | −0.6% | +0.5% | pass | **REFUTED** L1 L2 | no |
| volmanaged | 3 | 5 → 9 | 0.49 | 7.39% | −19.8% | 1.8 | 0 | 0.63 | −0.1% | −19.8% | +11.4% | pass | **REFUTED** L1 L2 L3 | no |
| sticky_tier | 4 | 5 → 6 | 0.61 | 7.38% | −14.3% | 0.4 | 67 | 1.18 | +9.7% | +2.2% | +0.1% | pass | holds | **yes** |
| vix_vrp (pass-1 file) | 5 | 5 → 8 | 0.61 | 10.61% | −19.8% | 6.0 | 64 | 1.65 | +15.1% | −15.7% | +44.4% | pass | **REFUTED** L1 | no |
| vix_vrp_v2 | 5 | 6 → 8 | 0.68 | 11.71% | −19.8% | 10.6 | 62 | 1.61 | +12.9% | −9.5% | +43.6% | pass | **REFUTED** L1 L2 L3 | no |
| composite_dual_engine | 6 | 6 → 7 (13 DEV-selected values) | 0.54 | 11.41% | −25.6% | 5.5 | 42 | 1.81 | −14.4% | +3.4% | +0.1% | pass | **REFUTED** L1 | no |

Three things stand out before any out-of-sample number is seen.

1. **Every gate passer is a cash-heavy or de-levered rule.** Cash 42–67% of days, or an average exposure of 0.63×.
   Two independent designs (`sticky_tier`, `vix_vrp`) converged on "cash about two thirds of the time, 1× otherwise" at
   DEV Sharpe 0.61. The development window contains the 2000-02 and 2007-09 bears; sitting them out is worth more Sharpe
   there than anything a levered rule can earn in the intervening bulls.
2. **Nothing holds 2–3× in calm years and survives the bears.** The composite is the only 3×-in-calm configuration to
   pass all seven gates (23.6% of DEV days at 3×), and its designer's own diagnostic shows a 2× calm tier scores higher
   (0.568 vs 0.543). `sticky_tier` never held 3× in 22 years; every setting that did failed the era gate through 1962 and
   1973-74. `volmanaged` averaged 0.63×.
3. **Every DEV Sharpe was earned in one decade.** Sub-sample thirds of 1990–2012: composite 0.88 / 0.32 / 0.36;
   volmanaged 0.87 / 0.40 / 0.09; sticky_tier 0.98 / undefined (all cash 1997–2004) / 0.44; vix_vrp halves 0.84 / 0.40;
   dissipation_reentry 0.69 / 0.30 / 0.39. The last third of the development window, closest in time and market
   structure to the out-of-sample period, was the weakest for every candidate.

## What the verifiers found (why four passers were refused a look)

Reports: `dev_results/<name>_VERIFY_L1.md`, `_L2.md`, `_L3.md`; digest `dev_results/PASS2_VERIFICATION_SUMMARY.md`.

* **The shared defect — hidden parameters.** `DESIGN_BRIEF.md` said a constant whose value is chosen by comparing
  development results is a tuned parameter. Every designer did exactly that and declared the result "structural":
  `composite` fixed its re-entry leverage at 3× after comparing 3×/2×/1× (and borrowed six other candidates' DEV-tuned
  values as constants); `dissipation_reentry` chose a flat 1× default over the incumbent's 3/2/1 tier by comparing Sharpe
  and the era gate; `volmanaged` fixed the exponent (1 vs 2), the estimator (three forms), continuous vs discrete and
  daily vs weekly by comparison; `vix_vrp_v2` chose 2× over 3× calm and 1× over 2× panic by comparison; `vix_vrp`'s three
  leverage constants have no documented provenance at all. True counts 7, 7, 9, 8, 8 against a budget of 6. The
  mechanical gate (`gate_check.py`) counts only `DEFAULT_PARAMS` and passed all of them; only a reader caught it.
* **volmanaged** (Moreira–Muir inverse-variance leverage): the Sharpe edge over SPY (+0.11 on 1990–2012) reverses sign on
  1950–2012 (0.36 vs SPY 0.47) and loses to a constant-leverage portfolio at its own average exposure on the long sample;
  the asymmetric no-trade band has an absorbing floor — once held leverage falls to or below the down-band (0.30) it can
  never de-lever again — so leverage sat frozen at 0.14× for 6.6 years (1997–2004) and at 0.20× for 3.75 years
  (Sep-2008 to the end of the window). Sharpe decays 0.87 → 0.40 → 0.09 across the window's thirds.
* **dissipation_reentry**: the base rule (1× while 21-day realised vol < 15%, cash above) scores 0.389, below the gate
  bar and equal to buy-and-hold; the entire margin comes from seven dated 3× bursts in 22.5 years; the grid's own maximum
  is a single trade (19-Dec-2008); a Bailey–López de Prado deflation over the ~8–10 genuinely independent bets puts the
  expected noise maximum at ≈0.45 — the candidate's 0.447. The realised-vol threshold is a cliff (Sharpe 0.19–0.30 at
  0.17–0.20) and G6 passed only because the other five parameters are flat.
* **vix_vrp_v2**: the +0.07 Sharpe over the original is smaller than one standard deviation (0.070) of its own 216-cell
  calibration grid; it rests on a leg open 132 days in 22.5 years (t ≈ 1.9 before any multiple-testing correction); and it
  **inverts to −0.06 under a one-session execution delay** (0.678 → 0.422 vs the original's 0.608 → 0.486). Its
  pre-committed retirement of the original was therefore void, and the original was verified in its place.
* **vix_vrp** (the never-reported pass-1 file): 8 true parameters; no design note; the docstring says "the OOS window
  2012-07..2026-02 was looked at only through the final evaluate.py runs" although no result file exists and RESULTS.md
  never mentioned it — either pass 1 looked and did not record it, or the sentence is boilerplate; both readings fail
  the study's ambiguity standard. Material: a one-day lag costs 20% of Sharpe and widens maxDD from −19.8% to −28.3%;
  more than half the Sharpe comes from the 1× panic leg (13.6% of days, five or six panics); 2.4 CAGR points a year are
  T-bill accrual on cash days.
* **composite_dual_engine**: all seven gates, the first 3×-in-calm passer, positive through the GFC window (+3.4%), but
  0.135 Sharpe behind `vix_vrp_v2` on the same window and refuted on the parameter count. Its ablations are the pass's
  most useful engineering result: the hysteresis (minimum hold) is what makes it work (+0.08 Sharpe, GFC −11% → +3%); the
  pre-registered shock exit is Sharpe-negative alone (−0.04; it buys drawdown only); the strict dissipation re-entry adds
  +0.07 at 3× and fires three times in the two bears at 33% negative. It sits out the whole 2009 recovery: VIX's 2009
  minimum (19.47) missed the stressed-exit level (19.32) by 0.15 points, and the divergence burst cannot fire when
  implied vol peaks on the day of the price low (9-Mar-2009).
* **sticky_tier** (survived): true count exactly 6 (the cash floor was chosen on DEV; it sits at the ceiling, not over);
  735 parameter sets, not the 13 batches its return file reported; robust to a one-day lag (0.612 / 0.610 / 0.604). The
  material findings were carried, verbatim, into the next section — they are the reasons it failed.

## The one out-of-sample look: `sticky_tier`

Rule in one sentence: discrete tiers {0, 1, 2, 3} from the larger of a 20- and a 160-session EWMA volatility, with
inverse-variance boundaries (1× below 14% vol, 2× below 9.9%, 3× below 8.1%), 20% hysteresis, five-session persistence,
weekly re-levering; cash otherwise. Five tunables plus the DEV-chosen cash floor. Frozen on 1990–2012; parameter set
735 of 735 evaluated on DEV only.

| Jul 2012 – Jan 2026, 3 bp / 60 bp | sticky_tier | Incumbent | Demeter | SPY |
|---|---|---|---|---|
| Annualised return | 3.24% | 16.92% | 31.33% | 14.71% |
| Annualised std. dev. | 0.08 | 0.23 | 0.22 | 0.14 |
| Sharpe | 0.24 | 0.74 | 1.27 | 0.95 |
| Sortino | 0.32 | 1.18 | 3.59 | 1.51 |
| Calmar | 0.18 | 0.82 | 2.30 | 0.61 |
| Maximum drawdown | −17.89% | −20.55% | −13.65% | −23.93% |
| % positive months | 91.41% | 66.87% | 72.39% | 71.17% |
| Beta to SPY | 0.19 | 1.04 | 0.54 | 1.00 |
| Up capture | 26% | 131% | 114% | 100% |
| Down capture | 29% | 147% | 23% | 100% |
| Growth of $1,000 | $1,543 | $8,357 | $40,523 | $6,449 |
| Days in cash | 73% | 21% | ~50% | 0 |
| Position changes, total | 10 | 125 | daily | 0 |
| Monthly correlation with Demeter | 0.13 | 0.38 | 1.00 | 0.34 |

What happened: ten position changes in 13.6 years, the last on 28 February 2020 — the rule went to cash and the
160-session slow leg never fell back below 14% for long enough to re-lever, so **from March 2020 to the end of the window
it was in cash on 97% of days** (2020–2026 Sharpe −0.41). Before 2020 it was a 1×-or-cash filter (2012–2019: 53% cash,
CAGR 4.7%, Sharpe 0.44). It met exactly one of the record's quantitative targets (down-capture ≤ 40%) and missed the rest
by a wide margin (cash 73% vs 48–52%; up-capture 26% vs ≥ 100%). Acceptance criteria: Sharpe > 0.73 **fails** (0.24);
maxDD ≥ −20.5% passes (−17.9%); < 25 changes/yr passes (0.7); not ruinous 1950–2012 passes (worst era −48% in 1950–89, i.e.
fails the −40% era test on the pre-VIX sample it never used — disclosed); edge at 6/90 **fails** (0.24). **Not a success.**

| Year | sticky_tier | Incumbent | Demeter | SPY |
|---|---|---|---|---|
| 2012 (6 mo) | 0.05% | 0.62% | 10.84% | 5.64% |
| 2013 | 2.82% | 70.67% | 32.60% | 32.27% |
| 2014 | 13.46% | 8.14% | 12.93% | 13.58% |
| 2015 | −6.94% | −12.11% | 9.95% | 1.30% |
| 2016 | 4.84% | 26.33% | 21.94% | 11.87% |
| 2017 | 25.65% | 45.21% | 33.27% | 21.74% |
| 2018 | −5.95% | 8.52% | 23.35% | −4.47% |
| 2019 | 5.18% | 32.36% | 17.10% | 31.37% |
| 2020 | −7.48% | −2.14% | 165.14% | 18.27% |
| 2021 | 0.05% | 49.70% | 40.97% | 28.62% |
| 2022 | 2.05% | −15.10% | 19.24% | −18.19% |
| 2023 | 5.16% | 0.19% | 25.33% | 26.17% |
| 2024 | 5.09% | 35.02% | 22.41% | 24.90% |
| 2025 | 4.11% | 12.67% | 42.26% | 17.78% |
| 2026 (1 mo) | 0.28% | 2.49% | −2.75% | 1.44% |

The months that define Demeter's record, for both models:

| Month | SPY | Demeter | Incumbent | sticky_tier |
|---|---|---|---|---|
| 2020-02 | −8.24% | −13.65% | −15.80% | −7.55% |
| 2020-03 | −12.36% | 55.32% | 8.61% | 0.03% |
| 2020-04 | 12.81% | 29.65% | 0.01% | 0.01% |
| 2022-04 | −8.73% | 0.00% | −9.06% | 0.06% |
| 2022-06 | −8.26% | 0.00% | 0.12% | 0.12% |
| 2022-10 | 8.09% | 10.04% | 0.31% | 0.31% |
| 2018-12 | −9.04% | −1.63% | 0.18% | 0.18% |
| 2015-08 | −6.04% | −4.79% | −15.20% | −10.00% |
| 2025-04 | −0.69% | 4.94% | 0.35% | 0.35% |

Neither model was invested at the close of 23 March 2020, 13 October 2022, 26 December 2018 or 8 April 2025 — the
re-entry dates the record implies. No candidate in either pass has fired on them; `dissipation_reentry`'s trigger was
built to, and was refused its look.

Out-of-sample parameter perturbations of `sticky_tier` (±15%/±30%, 21 variants, computed by `evaluate.py` after the
look as a disclosure, not a selection input) span Sharpe 0.08–0.53: the frozen point is mid-range, so this is not a
knife-edge failure — the whole neighbourhood fails.

## Leaderboard — both passes, one cost basis (3 bp / 60 bp)

Out of sample Jul 2012 – Jan/Feb 2026, S&P 500 total return over T-bill, cash at the T-bill rate.

| Candidate | Pass | OOS annualised | OOS Sharpe | OOS max DD | Changes/yr | Cash % | Down-capture | DEV Sharpe | DEV max DD | Corr. Demeter |
|---|---|---|---|---|---|---|---|---|---|---|
| baseline_volregime | 1 | 21.70% | 0.83 | −30.9% | 10.1 | 17 | 173% | 0.37 | −38.2% | 0.30 |
| **final_model_fewtrades** (recommended) | 1 | **16.78%** | **0.73** | **−20.5%** | 9.2 | 21 | 147% | 0.43 | −25.1% | 0.38 |
| trend_vol_fewtrades | 1 | 18.07% | 0.72 | −31.9% | 11.0 | 19 | 178% | 0.33 | −36.5% | 0.34 |
| vix_dissipation (the trap) | 1 | 16.31% | 0.67 | −37.2% | 43.2 | 39 | 123% | −0.31 | −93.5% | 0.43 |
| final_model | 1 | 15.59% | 0.65 | −35.4% | 11.7 | 20 | 171% | 0.37 | −28.8% | 0.26 |
| shock_reentry | 1 | 15.63% | 0.58 | −45.1% | 21.3 | 24 | 186% | −0.19 | −82.9% | 0.43 |
| sticky_tier | 2 | 3.23% | 0.24 | −17.9% | 0.7 | 73 | 29% | 0.61 | −14.3% | 0.13 |
| *Demeter (published)* | | 31.33% | 1.27 | −13.7% | daily | ~50 | 23% | — | — | 1.00 |
| *SPY buy & hold* | | 14.71% | 0.95 | −23.9% | 0 | 0 | 100% | — | — | 0.34 |

Seven candidates now carry out-of-sample numbers across two passes; the recommendation was chosen on development
evidence in both passes, and in pass 2 the development choice was wrong. The pass-1 leaderboard order is unchanged by the
move from 2 bp / 0 bp to 3 bp / 60 bp; every pass-1 model loses 0.5–1.5 points of annual return and 0.02–0.08 of Sharpe.

### Cost rows

| Candidate | 2 bp / 40 bp | 3 bp / 60 bp (headline) | 6 bp / 90 bp (stress) | Where the edge dies |
|---|---|---|---|---|
| final_model_fewtrades | 17.14% / 0.75 | 16.78% / 0.73 | 16.02% / 0.70, maxDD −21.0% | survives 6/90; Sharpe 0.70 |
| baseline_volregime | 22.23% / 0.85 | 21.70% / 0.83 | 20.59% / 0.79, −31.9% | survives; drawdown is the problem, not cost |
| trend_vol_fewtrades | 18.54% / 0.73 | 18.07% / 0.72 | 17.13% / 0.68, −32.2% | survives |
| final_model | 16.04% / 0.66 | 15.59% / 0.65 | 14.64% / 0.61, −36.7% | survives |
| vix_dissipation | 17.86% / 0.73 | 16.31% / 0.67 | 12.11% / 0.52, −43.6% | 43 changes/yr: loses 5.8 CAGR points between 2/40 and 6/90 |
| shock_reentry | 16.58% / 0.61 | 15.63% / 0.58 | 13.32% / 0.51, −47.5% | 21 changes/yr: loses 3.3 points |
| sticky_tier | 3.24% / 0.24 | 3.23% / 0.24 | 3.20% / 0.24, −18.0% | cost-insensitive (10 trades); dead at every cost |

### The two asymmetries in our favour, subtracted

| Candidate (3/60) | As engineered | T-bill zeroed on cash days (Demeter's convention) | T-bill on cash days, %/yr | Per-trade cost × max(1, RV21/15%) |
|---|---|---|---|---|
| final_model_fewtrades | 16.78% / Sharpe 0.73 | 16.34% / 0.72 | 0.38 | 16.74% / 0.73 |
| sticky_tier | 3.23% / 0.24 | 1.74% / 0.05 | 1.47 | 3.23% / 0.24 |

The incumbent's claim to beat SPY on return survives Demeter's cash convention (16.3% vs 14.7%); its Sharpe does not
beat SPY's under either convention. `sticky_tier`'s return is nearly half T-bill interest. Clustered slippage is
immaterial for both because neither trades often; the verifiers measured it at 1.3–1.5× the flat cost for the
high-turnover VIX-level machines that were refused a look (30–57% of their position changes fall on |return| > 2% days).

## The recommended model — unchanged, `signals/final_model_fewtrades.py`

1. **Trend hysteresis.** Enter above the 100-day average; exit below the 200-day average; in between, hold.
2. **Shock override.** Force cash for 5 sessions after any daily loss worse than three trailing standard deviations.
3. **Volatility tier.** While invested: 3× below 10% realised volatility, 2× below 15%, otherwise 1×.
4. **Weekly, sticky decisions.** The level is read on the last trading day of each week and held at least 20 sessions.

Parameters `ma_fast=100, ma_slow=200, rv_lo=0.10, rv_hi=0.15, min_days=20, shock_days=5` plus a fixed `shock_z=3.0`.
It was not re-verified by the pass-2 lenses; by their standard `shock_z` and the weekly-cadence choice are DEV-selected
constants and its true count is 7–8. Across eras at 3/60: 1950–89 CAGR 19.1% (SPY 12.4%), Sharpe 0.63 (0.52), maxDD
−32.6%; 1990–2011 10.3% (8.1%), 0.43 (0.36), −25.1%; 2012–19 21.5% (14.4%), 0.97 (1.24), −20.0%; 2020–26 11.3% (14.9%),
0.46 (0.75), −20.5%. Out-of-sample perturbations: 22 of 24 within 25% of the base Sharpe. Its failure is the one pass 1
named — down-capture 147% against Demeter's 23% — and pass 2 has not found a rule that fixes it without giving up the
upside.

## What failed and why — the lessons that generalise

1. **The development window has its own regime bias.** Pass 1's trap was a rule that only works after 2012 (VIX below
   its 10-day mean: +18%/yr out of sample, −93% drawdown before). Pass 2's survivors are the mirror image: rules that only
   work before 2012, because 1990–2012 contains two grinding bears and rewards being in cash. A rule that works in both
   windows was not found with daily closes. Using both windows for selection is the obvious fix and the obvious way to
   over-fit; the honest version is a walk-forward with decade-by-decade re-selection, which remains unrun.
2. **"Structural constants" are parameters.** Every designer, given a budget of six, made three to seven further choices
   by comparing development results and declared them structural. A pre-registration that caps parameters must
   enumerate every discrete design choice as one, and a mechanical gate cannot enforce it — a reader must.
3. **Sub-sample thirds and a lag test are cheap and decisive.** Every candidate's DEV Sharpe was concentrated in one third
   of the window; the VIX-level machines lost 20–40% of their Sharpe with a one-session delay (`vix_vrp` 0.61 → 0.49,
   `vix_vrp_v2` 0.68 → 0.42, and the v2's advantage inverted). `sticky_tier` was lag-robust and still failed: robustness
   to timing is necessary, not sufficient.
4. **The record's ingredients do not transfer as rules.** A crash exit alone rides grinding bears (−52.8% drawdown). The
   strict dissipation re-entry that reproduces the 23-Mar-2020 profile fires seven times in 22 years and cannot catch the
   1998, 2002 or 2009 lows because implied volatility peaked on the low day in each. The composite's hysteresis, not its
   exit or re-entry, was what earned its Sharpe. The three named re-entry dates in the live window were not fired on by any
   model in either pass.
5. **Selection deflation at this trial count is real.** With 700–1,300 parameter sets per candidate on a 22.5-year window,
   the expected maximum Sharpe from noise is roughly 0.45–0.65 (standard error ≈ 0.21). Every pass-2 DEV Sharpe (0.45–0.68)
   sits inside that band. The verifiers' expected out-of-sample ranges — 0.10–0.35 for `sticky_tier`, 0.20–0.40 for the
   composite, 0.05–0.35 for `dissipation_reentry`, 0.00–0.25 for `volmanaged`, 0.30–0.55 for `vix_vrp` — were written
   before the look; the one realised value (0.24) fell inside its range.

## Limitations

* Seven candidates now have out-of-sample numbers across two passes and the recommendation is the best of the pass-1
  six chosen on development evidence: it still flatters itself. Pass 2's refusal to look at refuted candidates limits the
  count but also means their fate is unknown; the verifiers' pre-look estimates say they would not have reached 0.73.
* The design process saw the record in both passes; the ingredients, not the parameters, were informed by 2012–2026.
* One market, one fourteen-year regime out of sample; `sticky_tier`'s post-2020 all-cash spell is one regime call.
* Costs are modelled, not measured: constant 3 bp per unit of leverage traded, a flat financing spread, no margin
  mechanics at 3×, no roll or tax effects; the volatility-scaled slippage row is a stress, not a measurement.
* Demeter's returns are the manager's published figures, unaudited; the published four-quadrant day counts sum to 3,477
  against a stated 3,219 trading days.
* Data seams: the last 35 daily rows are extrapolated, the T-bill is held flat after 2025-12-19, futures end 2024-03-28;
  VIX begins 1990, so every VIX rule's "1950–2012" figure is forty years of forced cash plus 22.5 years of signal.
* `gate_check.py` G7 counts declared tunables only; `dev_harness.plateau` rounds integer perturbations so small integer
  parameters get asymmetric or duplicated steps; `verify_tools.constants()` missed tuple assignments until fixed on
  2026-09-12 (no result depends on it). All three were found by the verifiers and are disclosed rather than patched
  retrospectively.

## Next steps that would actually move the answer

1. **Data, not cleverness.** The re-entry that made Demeter's March 2020 happened within a day of the low at VIX 61; daily
   closes cannot see it, and no daily rule in either pass fired on it. VIX futures term structure, daily put/call or skew,
   and intraday S&P bars remain the only inputs that could change this conclusion. None was reachable in pass 1's sandbox;
   this pass did not attempt to source them.
2. **A walk-forward across 1950–2012 with decade-by-decade re-selection**, so that the regime bias of any single
   development window (lesson 1) is measured rather than assumed.
3. **If the Principal wants it: an exploratory, clearly labelled out-of-sample look at the five refuted candidates.** It
   is not run here because a look cannot be un-taken and the pre-registration forbade it; the verifiers' pre-look ranges
   are on file to be checked against.
4. **Pre-register every discrete design choice as a parameter** in any pass 3, and write the sub-sample-thirds and
   one-day-lag tests into the gates.

## Honesty counts

* Candidates built in pass 2: six new signal files plus a v2 of the reinstated pass-1 file (seven files); development
  parameter sets evaluated: 5,652 (+435 audit). Gate passers: five of seven. Verified: one. Out-of-sample looks: **one**.
* Every out-of-sample number above carries its cost assumption. The headline basis is 3 bp / 60 bp; 2 bp / 40 bp and
  6 bp / 90 bp are shown for every model with a look.
* "This model reproduces Demeter": no model does — monthly correlation with the record is 0.38 for the incumbent and 0.13
  for `sticky_tier`. "This model is a good strategy in its own right": the incumbent beats SPY on return with lower
  drawdown and loses to it on Sharpe; `sticky_tier` is not.
* Files: `PREREG.md` (gates, look budget, verification outcomes, deviations), `results/OOS_LOOK_LOG.md` (every look),
  `dev_results/PASS2_DEV_TABLE.md`, `dev_results/PASS2_VERIFICATION_SUMMARY.md`, `dev_results/<name>_DESIGN_NOTE.md`
  (mechanism written before the first run, every grid, every iteration), `results/pass2_summary.json`.
