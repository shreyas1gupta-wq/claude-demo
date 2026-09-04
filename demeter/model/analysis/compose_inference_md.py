#!/usr/bin/env python3
"""Assemble results/demeter_inference.md from results/demeter_inference.json + the markdown tables produced by infer_demeter.py,
and add the (f) conclusions / design constraints to the JSON."""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
JP = HERE / "results" / "demeter_inference.json"
TP = Path(sys.argv[1]) / "tables.json"
J = json.load(open(JP)); T = json.load(open(TP))
e = J["e_summary"]; D = J["d_daily_inference"]; H = J["headline_verification_2012_07_2026_01"]
r_all, r_ex = e["regressions_all_months"], e["regressions_ex_2020_02_to_04"]
q = e["quadrant_fingerprint"]; vs = e["vix_split_median"]; cs = J["c_down_months"]["summary"]
mar, feb, apr, may, nov = (D["months"][k] for k in ["2020-03", "2020-02", "2020-04", "2020-05", "2020-11"])
fmt = lambda v, d=2: "n/a" if v is None else f"{v:.{d}f}"

ranked = [
    {"rank": 1, "ingredient": "Fast, asymmetric de-levering on a downside volatility shock (leverage effect + volatility clustering)",
     "evidence": [f"Feb-2020: all 79 matching paths keep the strategy invested through the month at a mean 1.5-2.1x (constant-equivalent 1.72x), i.e. the two consecutive -3% days on 24-25 Feb were absorbed levered; but 3x was NOT held into the -4.5% 27-Feb day (3x through 27-Feb = -22.4%, 3x through 25-Feb then 1x = -14.1%, record -13.65%). The de-levering came one to two days after the first shock, on the second/third -3% day.",
                  "Jan-2022: every matching path is invested 3-11 Jan and in cash 14-31 Jan (exit at the 11/13-Jan close after the -1.9% 5-Jan and -1.4% 13-Jan days; the 18-27 Jan slide of -7% was avoided). Dec-2022: never invested 15-21 Dec (post-FOMC drop). Oct-2018: never invested 5-11 Oct (the -3.2%/-2.2% days). Dec-2018: cash 3-17 Dec. Feb-2018: cash 1-7 Feb (VIX 13.5 -> 37). Counter-examples that bound the trigger: Aug-2019 held 2-3x through the -3.0% 5-Aug day in every path, and Feb-2025 is consistent with 3x for essentially the whole month (daily moves of -0.4 to -1.7% did not fire it) -- the exit needs a genuine vol shock (repeated -2/-3% days, VIX > ~25), not a single bad day.",
                  f"SPY months below -3% (n={cs['n']}): median implied exposure {cs['median_exposure']:.2f}x, Demeter beat SPY in {cs['n_beat_spy']} of {cs['n']}, was positive in {cs['n_positive']}, fully in cash in {cs['n_full_cash']}. Down-capture 22.9% (36-month rolling median 34%).",
                  f"Piecewise regression ex Feb-Apr 2020: up-beta {r_ex['up_beta']:.2f} vs down-beta {r_ex['down_beta']:.2f}; all months up-beta {r_all['up_beta']:.2f} vs down-beta {r_all['down_beta']:.2f}."]},
    {"rank": 2, "ingredient": "Re-entry driven by short-horizon mean reversion + implied-vol DISSIPATION (VIX falling from its peak / variance-risk-premium collapsing), not by a low vol level",
     "evidence": [f"Mar-2020: every minimal path is in cash 6-20 Mar and 3x on 24-26 Mar. Entering 3x at the 23-Mar close (the low: RSI(2) 8, drawdown -34%, VIX 61.6 after 5 straight declines from the 82.7 peak, VIX/SMA10 0.92, 10-day realised vol 103%) and holding gives +49%; 3x on 24-26 Mar only gives +56.1%; entering one day later gives +17%, one day earlier +38%.",
                  f"Apr-2020: 2.3x constant-equivalent with VIX between 31 and 57 and realised vol 40%; 3x from 7-Apr to month-end = +29.4% (record +29.65%); at least 14 of 21 days at 3x in every 1-switch solution. May-2020 2.1x (VIX 27-37). Nov-2020 1.5x (VIX 38 -> 21).",
                  f"Spearman correlation of implied exposure with the within-month VIX change: {e['exposure_correlates_spearman']['vs_vix_change_within_month_(reaction)']:.2f}; with the VIX level at the start of the month: {e['exposure_correlates_spearman']['vs_vix_start_(causal)']:+.2f}.",
                  "Archetype check: '3x when VIX < its 10-day SMA, else cash' reproduces the 2020 signature (Feb +1.9, Mar +37.6, Apr +36.1) whereas VIX-level, realised-vol-level and 200-day-SMA gates all return ~0% in Mar and Apr 2020."]},
    {"rank": 3, "ingredient": "Leverage tier scaled by the volatility regime: 3x in calm markets, ~1x ('sometimes unlevered') when vol is elevated, with a separate crisis-rebound mode at 2-3x",
     "evidence": [f"2022 (VIX avg 25.6): implied exposure 0.9x (Sep), 1.16x (Jul), 1.24x (Oct), 0.95x (Nov), 1.5x (Mar); 2017 (VIX avg 11.1): median 2.2x; 2025 median 1.9x.",
                  f"VIX-average bins: mean implied exposure {e['vix_bins']['<13']['mean exposure']:.2f}x below 13, {e['vix_bins']['13-16']['mean exposure']:.2f}x at 13-16, {e['vix_bins']['16-20']['mean exposure']:.2f}x at 16-20, {e['vix_bins']['20-25']['mean exposure']:.2f}x at 20-25, {e['vix_bins']['25-30']['mean exposure']:.2f}x at 25-30; the >30 bin (crisis rebounds) has median {e['vix_bins']['>30']['median exposure']:.2f}x.",
                  f"Volatility-implied leverage when invested (50% cash days): {e['vol_implied_leverage']['lev_when_invested_if_50pct_days_random']:.1f}x over all months, {e['vol_implied_leverage']['ex_2020_02_04']['lev_when_invested_if_50pct_days_random']:.1f}x excluding Feb-Apr 2020."]},
    {"rank": 4, "ingredient": "Persistence / hysteresis: once out, stay out for weeks (whole months in cash), re-enter only on confirmation",
     "evidence": [f"Three months at exactly 0.00% (Jan-2016 SPY -4.97, Apr-2022 -8.73, Jun-2022 -8.26) and Feb-2022 (+0.16 vs -3.00) are constant-cash months. Demeter's own quadrant counts: 883 'gain sacrifice' days vs 804 'loss avoidance' days -- cash spells sat through more up days than down days, so exits were not reversed on the first rebound day.",
                  f"P(market up | in cash) = {q['P_market_up_given_cash']:.1f}% vs P(market up | invested) = {q['P_market_up_given_invested']:.1f}%: a ~5-point directional edge only; returns come from magnitude timing, not day-ahead direction."]},
    {"rank": 5, "ingredient": "Short-horizon (days to ~3 weeks) timing at 3x inside calm regimes -- the source of BOTH tails, including the whipsaw losses",
     "evidence": [f"27 months have a constant-leverage equivalent above 3 or below 0 (impossible for any fixed long-only position): e.g. Jan-2025 L*=5.96 (either 3x on 15-22 Jan only, or 3x all month except the 24-27 Jan DeepSeek drop), Jul/Aug-2025 (3.3x/4.2x), Feb-2013 4.4x, Sep-2018 3.4x; and sign flips in {len(e['sign_flip_months'])} months (Feb-2018 +2.42 vs SPY -3.69: cash 1-7 Feb (or 1-12 Feb) then 2x from 8-Feb (or 1x from 13-Feb)).",
                  "8 of the 12 worst Demeter months occurred when SPY fell only 0.3-2.7% (Jun-2015 -10.65 vs SPY -1.94; Oct-2020 -6.92; Feb-2025 -6.35; Dec-2014 -6.19; Oct-2023 -5.74; Aug-2019 -5.62; Oct-2024 -4.92) with month-start VIX 13-19. Jun-2015 requires 3x on 1-5 Jun AND 24-30 Jun in every path, with either cash 8-23 Jun (exit after the first dip, re-enter after the recovery, get hit by the 29-Jun Greece day at 3x) or 3x nearly all month but out precisely on the 10-11 Jun up days; 3x buy-and-hold would have lost only 6.3%.",
                  "The record's losses are therefore whipsaw losses at high leverage in choppy low-vol months, not crash losses -- the signature of a quick-exit / quick-re-entry rule."]},
    {"rank": 6, "ingredient": "Long-or-cash only, discrete leverage {0,1,2,3}, daily decision, cash booked at 0%",
     "evidence": [f"Every month Jul-2012..Jan-2026 is reproducible with a {{0,1,2,3}} path and at most 2 intra-month switches (0 switches: 28 months, 1: 128, 2: 7); no shorting is needed even for Mar-2020.",
                  "The three 0.00% months coincide with T-bill months of +0.02%, +0.06% and +0.13%: published cash months earn nothing (our engine credits T-bills; expect our cash months to print small positives).",
                  "Lower bound on position changes: >=142 intra-month switches in 163 months (>=10.4/yr) plus month-boundary changes; the whipsaw months and the daily framing imply materially more (plausibly 30-80/yr)."]},
]
ruled_out = [
    {"item": "A slow trend filter (e.g. 200-day SMA) as the invest/cash gate",
     "why": f"SPX closed below its 200-day SMA on 20 of 22 trading days in Mar-2020 (all days from 5-Mar), 21 of 21 in Apr-2020, 20 of 20 in Jul-2022, 21 of 21 in Oct-2022 and 20 of 21 in Nov-2022, yet Demeter earned +55.3%, +29.7%, +10.6%, +10.0% and +5.3% in those months. A 3x-above/cash-below SMA200 rule returns -17.9%, 0.0%, 0.0%, 0.0%, 0.0%. Re-entry is fast (days), not trend-confirmed (months)."},
    {"item": "Absolute volatility-LEVEL gating (invest only when VIX < X or realised vol < Y), or leverage as a monotone decreasing function of the vol level",
     "why": f"Apr-2020 ran 2.3x with VIX 31-57 and realised vol 40%; the 23-Mar-2020 re-entry happened at 10-day realised vol 103% and VIX 61.6. 'VIX<20', 'VIX<30', 'RV21<15/25%' gates all return ~0% in Mar and Apr 2020 (VIX<40 gate: -12%/-4%). Conversely the worst months came from low-vol starts (VIX 13-19), so a low level did not protect. Implied exposure vs month-start VIX has Spearman {e['exposure_correlates_spearman']['vs_vix_start_(causal)']:+.2f}."},
    {"item": "Constant or monthly-set exposure (levered buy-and-hold, monthly regime allocation, or any rule that cannot change exposure within a month)",
     "why": f"27 months have constant-leverage equivalents >3 or <0; {len(e['sign_flip_months'])} months have the opposite sign to SPY; Mar-2020 needs >=2 intra-month switches; Feb-2020 needs 2. Monthly skew {r_all['skew_demeter']:.1f} vs SPY {r_all['skew_spy']:.1f}; up-beta {r_all['up_beta']:.2f} vs down-beta {r_all['down_beta']:.2f}; convexity term t={r_all['quad_convexity_t']:.1f} (t={r_ex['quad_convexity_t']:.1f} ex-2020). 3x buy-and-hold would have lost 62% peak-to-trough."},
    {"item": "(also) Un-gated 1-day mean reversion at 3x, and 'always 3x when invested'",
     "why": "Pure 'long 3x after a down day' gives -29% in Feb-2020 and -36% in 2022 (record -13.65% and +19.2%); mean reversion must sit behind a vol/crash gate. 2022's invested months ran at 0.9-1.5x, so the levered tier is conditional, not constant."},
]
constraints = {
    "cash_share_pct": "48-52% of days (Demeter: 48.5%)",
    "leverage_when_invested": "mix of 1x and 3x; vol-implied average 1.5-2.2x; ~1x when VIX 25-30, 2-3x when VIX < 16 or in a post-crash rebound",
    "monthly_capture_targets": "up-capture >= 100% (Demeter 114%), down-capture <= 40% (Demeter 23%; 12m rolling median 39%)",
    "convexity_targets": "up-beta 1.0-1.4, down-beta <= 0.45 (ex-2020 record: 1.01 / 0.42); positive monthly skew",
    "crash_exit": "from 2-3x to <=1x within 1-2 days after two consecutive -3% days (Feb-2020: de-lever at the 25/26-Feb close; month -13.65%, not -22%); but tolerate a single -3% day in a calm regime (Aug-2019) and -0.5 to -1.7% days at 3x (Feb-2025)",
    "crash_reentry": "back to 2-3x within +-1 day of the low while VIX > 50 and realised vol > 80%, triggered by VIX falling from its peak + oversold (23-Mar-2020); then >=14 of 21 days at 3x in the following month with VIX 31-57",
    "grinding_bear": "whole months in cash when SPY falls 8% in a month with VIX 20-34 (Apr/Jun-2022) but ~1x participation in the Jul/Oct/Nov-2022 rallies while below the 200-day SMA",
    "accepted_pain": "whipsaw months of -5% to -11% when SPY is only -0.3% to -2.7% (8 such months in 168); worst month -13.65%",
    "trade_count": "lower bound ~10.4 intra-month switches/yr from the record; realistic 30-80/yr; hysteresis so cash spells last weeks",
    "cash_accounting": "Demeter books cash at 0%; our engine credits T-bills (adds roughly 0.5%/yr on average over 2012-2026, more after 2022)",
}
J["f_ranked_ingredients"] = ranked
J["f_ruled_out"] = ruled_out
J["design_constraints_for_rule_builders"] = constraints
J["oos_disclosure"] = {"evaluate_py_runs": 0, "note": "No evaluate.py runs were made. Section 8 / Appendix C computes coarse un-tuned archetype rules through engine.run over Demeter's live window purely to FINGERPRINT the record; these numbers must not be used to tune model parameters."}
J["key_numbers"] = {
    "n_months": 168, "n_months_with_daily_data": 163, "cagr_pct_2012_07_2026_01": round(H["annualized_return_pct"], 2), "sharpe": round(H["sharpe"], 3), "beta": round(H["beta_to_spy"], 3),
    "up_capture_pct": round(H["up_capture_pct"], 1), "down_capture_pct": round(H["down_capture_pct"], 1),
    "share_months_exposure_gt_1.5_pct": round(e["share_exposure_gt_1.5"], 1), "share_months_exposure_0.5_1.5_pct": round(e["share_exposure_0.5_to_1.5"], 1), "share_months_exposure_near_0_pct": round(e["share_exposure_near_0"], 1),
    "mean_exposure_up_months": round(e["exposure_in_up_months"]["mean"], 2), "mean_exposure_down_months": round(e["exposure_in_down_months"]["mean"], 2),
    "mean_exposure_low_vix": round(vs["low_vix"]["mean_exposure"], 2), "mean_exposure_high_vix": round(vs["high_vix"]["mean_exposure"], 2), "vix_median_split": round(vs["median_vix_avg"], 1),
    "mar2020_days_at_3x_min_max": mar["days_3x_range"], "mar2020_cash_days_min_max": mar["days_cash_range"], "mar2020_3x_from_24mar_to_eom_pct": D["mar2020_enter_3x_and_hold"]["3x from 03-24 to month-end"],
    "apr2020_days_at_3x_min_max": apr["days_3x_range"], "apr2020_L_const": apr["L_const"], "feb2020_L_const": feb["L_const"],
    "months_needing_intra_month_switch": 135, "months_constant_level": 28, "months_L_const_impossible": len(e["months_L_const_gt_3_or_negative"]),
    "P_up_given_invested_pct": round(q["P_market_up_given_invested"], 1), "P_up_given_cash_pct": round(q["P_market_up_given_cash"], 1),
    "up_beta_all": round(r_all["up_beta"], 2), "down_beta_all": round(r_all["down_beta"], 2), "up_beta_ex2020": round(r_ex["up_beta"], 2), "down_beta_ex2020": round(r_ex["down_beta"], 2),
}
json.dump(J, open(JP, "w"), indent=1, default=str)

# ------------------------------------------------------------------------------------------------------ markdown
def bl(items): return "\n".join(f"- {x}" for x in items)
md = []
md.append(f"""# Demeter "Dual-Engine" strategy: what the daily rule must have been doing

*Inference from the published monthly record (Jul-2012 .. Jun-2026, 168 months) and our daily market data (`model/data/market_daily.csv`, full months Jul-2012 .. Jan-2026 = 163 months). Produced by `model/analysis/infer_demeter.py` (+ `compose_inference_md.py`); machine-readable companion: `results/demeter_inference.json`.*

**OOS disclosure.** `evaluate.py` was run 0 times for this note. Section 8 / Appendix C runs coarse, un-tuned archetype rules through `engine.run` over Demeter's live window purely to fingerprint the record; nothing here was used to tune model parameters and nothing here should be.

## 0. Headline verification and conventions

Recomputing Demeter's factsheet numbers from `monthly_returns.csv` over Jul-2012..Jan-2026 reproduces them exactly: CAGR {H['annualized_return_pct']:.2f}%, annualised std {H['annualized_std_dev']:.3f}, max drawdown {H['max_drawdown_pct']:.2f}% (monthly), Sharpe {H['sharpe']:.3f}, beta {H['beta_to_spy']:.3f}, correlation {H['correlation_to_spy']:.3f}, up-capture {H['up_capture_pct']:.1f}%, down-capture {H['down_capture_pct']:.1f}%, {H['pct_positive_months']:.1f}% positive months. Our S&P 500 total-return series matches Demeter's SPY column month by month (corr {H['spy_ours_vs_demeter_spy_corr']:.4f}, mean abs diff {H['spy_ours_vs_demeter_spy_mad_pct']:.2f} pp), so daily-path arguments below are on the same footing as the published record.

Conventions: *implied exposure* = Demeter / SPY monthly return where |SPY| > 2% (109 of 168 months; the ratio is meaningless for small SPY moves). *L\\** = the constant daily leverage that would reproduce the month from our daily data with cash earning 0 (compounding-consistent; values above 3 or below 0 are impossible for any fixed long-only position and therefore prove intra-month timing). *Minimum switches* = the smallest number of intra-month position changes among {{0,1,2,3}}-leverage paths (decided at the prior close, 2 bp per unit notional traded) that reproduce the published month within max(0.25 pp, 2% of |return|).

**Cash is booked at 0%.** The three months printed as exactly 0.00% (Jan-2016, Apr-2022, Jun-2022) coincide with 3-month T-bill accruals of +0.02%, +0.06% and +0.13%. The published series therefore does not credit T-bill interest on cash days (consistent with Demeter's statement that only 1022 of ~3477 days had a positive return, i.e. cash days are zeros). Our engine credits T-bills, so its cash months will print small positives; over 2012-2026 that is worth roughly 0.5%/yr to our engine, more after 2022.

## 1. (a) Month-by-month implied exposure

Full 168-row table in Appendix A. Yearly digest (implied exposure over the months with |SPY| > 2%; `cash_months` = months printed as exactly 0.00%):

{T['a_yearly']}

Reading: the typical implied exposure is about 1x (mean {e['mean_exposure_all']:.2f}, median {e['median_exposure_all']:.2f}), NOT 2-3x. Years of 2x-plus behaviour are the calm low-VIX years (2012 H2, 2017, 2025) and the crisis-rebound year (2020 median 1.4x); in the high-VIX years (2018, 2022) exposure averaged 0.5-0.6x and in 2014/2019 (whipsaw years) it was 0.4-0.7x. Full-cash months: {', '.join(f"{k} (SPY {v:+.2f})" for k, v in J['a_implied_exposure']['full_cash_months_spy'].items())}; in addition Feb-2022 (+0.16% vs SPY -3.00%) is constant-cash to within rounding.

## 2. (b) Rolling 12- and 36-month beta and up/down capture

Semi-annual snapshots (full monthly series in the JSON, keys `b_rolling.rolling_12m` / `rolling_36m`).

**12-month windows**

{T['b_r12']}

**36-month windows**

{T['b_r36']}

**Extremes of the 12-month windows**

{T['b_ext']}

Summary: 12-month beta ranges from {J['b_rolling']['summary_12m']['beta_min']:.2f} ({J['b_rolling']['summary_12m']['beta_min_month']}) to {J['b_rolling']['summary_12m']['beta_max']:.2f} ({J['b_rolling']['summary_12m']['beta_max_month']}), median {J['b_rolling']['summary_12m']['beta_median']:.2f}; {J['b_rolling']['summary_12m']['pct_windows_beta_lt_0.5']:.0f}% of windows have beta < 0.5 and {J['b_rolling']['summary_12m']['pct_windows_beta_gt_1']:.0f}% have beta > 1. Median 12-month up-capture {J['b_rolling']['summary_12m']['up_capture_median']:.0f}% vs down-capture {J['b_rolling']['summary_12m']['down_capture_median']:.0f}%; 36-month medians {J['b_rolling']['summary_36m']['up_capture_median']:.0f}% / {J['b_rolling']['summary_36m']['down_capture_median']:.0f}%. Three regimes are visible: (i) 2013-2015: no consistent asymmetry yet (12-month down-capture swings between -9% and 150%, beta 0.3-0.9); (ii) 2016-2019: strong asymmetry (up-capture 100-180%, down-capture near zero or negative in most windows); (iii) 2020-2022 windows dominated by Mar-2020 (negative beta, negative down-capture), then 2023-2026 reverting to beta 0.7-1.4 with 12-month down-capture of 60-130% -- since 2023 the strategy has behaved much more like a ~1x market exposure with little downside protection than the full-period averages suggest. Designers should not expect a rule to deliver 23% down-capture in every sub-period; the 36-month windows since 2023 show 29-98%.

## 3. (c) Behaviour in SPY-down months worse than -3% and in the rebounds

{T['c_down']}

*`SPY 1st/2nd half` = SPY return over the first/second half of the month's trading days; `trough day` = calendar day of the intra-month low.*

Rebounds that followed (`next`/`next2` = the following two months; `exp` = implied exposure where |SPY| > 2%):

{T['c_rebound']}

Named episodes with SPY between -1% and -3% (not in the table above), showing where the big *losses* actually came from:

{T['c_named_mild']}

Episode notes (dates are trading days; "must be" statements come from the set of all minimal-switch paths that reproduce the month):

- **2015-08 / 09.** Aug: -4.79 vs -6.04 (0.79x). Every matching path is invested 10-31 Aug (the crash week 20-25 Aug included) at ~1x -- the rule was NOT out during the 24-Aug flash-crash but was unlevered (VIX 12.6 at month start); the mild loss reflects 1x, not avoidance. Sep: +0.61 vs -2.48 (sign flip; invested 2-10 Sep in every path, then out for the late-month slide). Oct rebound (+8.43) captured at 1.07x.
- **2016-01.** Exactly 0.00%: fully in cash for the whole month (SPY -4.97, VIX 18 -> 28). Feb-2016 -2.35 vs -0.14 (whipsaw at re-entry), Mar-2016 rebound (+6.78) caught at 1.21x.
- **2018-02.** +2.42 vs -3.69: the only 1-switch paths are cash 1-7 Feb then 2x from 8-Feb, or cash 1-12 Feb then 1x from 13-Feb (the VIX spike from 13.5 to 37 on 5-6 Feb was sat out entirely; the exit must have happened at the 31-Jan close or earlier, after the -0.7%/-1.0% days of 29-30 Jan lifted VIX from 11 to 15). Re-entry within 1-4 days of the 8-Feb low, at 1-2x. Mar-2018 -0.68 vs -2.55 (0.27x); Apr +5.69 vs +0.38 (timing gain).
- **2018-10 / 12.** Oct: -0.76 vs -6.84 (0.11x): never invested 5-11 Oct (the -3.2%/-2.2% days on 10-11 Oct); either 1x on 1-4 Oct then cash (exit at the 4-Oct close, after only -0.8% but with VIX up from 12 to 14), or cash until 11-Oct then 1x for the rest of the month. Nov: 1.02x. Dec: -1.63 vs -9.04 (0.18x): cash 3-17 Dec, 1x from 18/19-Dec (i.e. re-entered a few days BEFORE the 24-Dec low and held through it at 1x). Jan-2019 rebound (+8.01) at 0.96x, Feb 1.12x -- unlevered participation, no 3x.
- **2019-05.** -3.89 vs -6.36 (0.6x): ~1x for roughly half the month (e.g. 1x until 15-May then cash, or cash until 20-23 May then 1x). Jun-2019 rebound (+7.04) at 0.67x.
- **2020-02 / 03 / 04.** See section 4. Feb 1.66x (levered ~1.5-2x throughout, de-levered only after 25/26-Feb), Mar +55.32 (cash 6-20 Mar, 3x for 3-6 days from 24-Mar, possibly also on 2-5 Mar), Apr 2.31x (>=14 of 21 days at 3x), May 2.03x.
- **2022 (monthly).** Jan -2.48 vs -5.18: invested 3-11 Jan (1-2x), cash 14-31 Jan. Feb +0.16 vs -3.00: constant cash. Mar +5.54 vs +3.70 (1.5x): invested 18-30 Mar (post-FOMC rally) in every path; either ~1x all month or cash until 17-Mar then 2x. Apr 0.00: cash all month (SPY -8.73). May +0.71 vs +0.18: mostly cash. Jun 0.00: cash all month (SPY -8.26). Jul +10.64 vs +9.21 (1.16x): the minimal paths disagree -- either ~1x all month with 2x-3x only late (27-29 Jul must be invested), or cash until 26-Jul and 2x for the last three days -- but none has sustained 3x. Aug -0.41 vs -4.09 (0.1x): minimal paths range from '1x on 1-Aug only' to '3x through 19-Aug then 1x'; the common feature is no leverage during the 22-31 Aug slide (-6.5%). Sep -8.16 vs -9.22 (0.89x): either ~1x all month or cash until 19-Sep then 1x for the 20-30 Sep slide; in every path the rule was long 1x through the 20-27 Sep post-FOMC decline -- it did not avoid the September bear leg. Oct +10.04 vs +8.09 (1.24x): either 1x with a 3x burst around 18-Oct, or cash until 17-Oct and 2x for the second half. Nov +5.28 vs +5.58: 1x all month (0 switches). Dec -2.03 vs -5.77 (0.35x): never invested 15-21 Dec; 1x before, cash after.
- **2023-08 / 09 / 10.** Aug +1.14 vs -1.60 (sign flip): invested 14-31 Aug in every path (cash during the 1-11 Aug slide, back in for the second-half recovery). Sep -2.25 vs -4.77 (0.47x): ~1x for about half the month. Oct -5.74 vs -2.11 (L* 2.14; 3x buy-and-hold would have lost 8.1%): 2-3x levered into the 18-20 Oct drop (-1.3, -0.9, -1.2%) in every path, with VIX 17-22 -- a whipsaw loss at high leverage in a calm regime, not a crash loss.
- **2025-02 / 03.** Feb -6.35 vs -1.31 (L* 3.71): every path is invested 20-27 Feb at 2-3x (the late-month slide of -0.4, -1.7, -0.5, -0.5, +0.1, -1.6%), and the month is consistent with 3x for essentially the whole month (3x buy-and-hold = -5.0%; 3x through 27-Feb then 2x = -6.5%). Daily moves of that size, with VIX 15-21, did not trigger a de-levering. Mar -7.55 vs -5.64 (1.34x): ~1x-2x for most of the month, no full exit despite VIX 20-28. Apr-2025 +4.94 vs -0.69: cash 1-14 Apr in every path (the tariff crash AND the +9.5% 9-Apr rebound both missed), then 2x from 15-Apr or 1x from 21/23-Apr -- re-entry came about a week after the 8-Apr low (VIX 52 -> 30), much slower than the same-day re-entry of Mar-2020.

Pattern: in {cs['n_beat_spy']} of {cs['n']} months below -3% the strategy beat SPY (mean implied exposure {cs['mean_exposure']:.2f}x, median {cs['median_exposure']:.2f}x); the exit is fast (within 1-3 days of the first -2%/-3% day) and re-entry in the following rebound month is at about 1x (median {cs['next_month']['median_exp_when_next_spy_gt_2']:.2f}x when the next month's SPY > 2%) -- the 2-3x rebound leverage of Apr/May/Nov-2020 is the exception, not the norm. The costly months are not the crash months but choppy months with mild SPY losses where the rule was 2-3x levered (section 6).

## 4. (d) What a daily rule had to do in 2020 and 2022

### Feb / Mar / Apr 2020

{T['d_2020']}

*`1x/2x/3x` = return of that constant leverage all month; `3x up-days only` = perfect-foresight upper bound.*

**Feb-2020 (-13.65%, SPY -8.24%).** No single-switch path reproduces the month; 79 two-switch paths do, and they agree that the strategy was invested on every day of the month at a mean leverage of 1.5-2.1x (constant-equivalent 1.72x), including the first two crash days 24-25 Feb (-3.3% and -3.0%), and that 3x was not held into 27-Feb. The cleanest family -- 3x through the top (SPY +5.2% to 19-Feb, VIX 14) and through 24-25 Feb (-10.0% and -9.1% daily at 3x), then de-levered -- shows the arithmetic:

| scenario | Feb-2020 return |
|---|---|
| 3x through 21-Feb, cash after | {D['feb2020_3x_until_close_of_D_then_cash']['3x through 02-21, cash after']:+.1f}% |
| 3x through 24-Feb, cash after | {D['feb2020_3x_until_close_of_D_then_cash']['3x through 02-24, cash after']:+.1f}% |
| 3x through 25-Feb, cash after | {D['feb2020_3x_until_close_of_D_then_cash']['3x through 02-25, cash after']:+.1f}% |
| 3x through 25-Feb, 1x after | {D['feb2020_3x_until_close_of_D_then_1x']['3x through 02-25, 1x after']:+.1f}% |
| 3x through 26-Feb, 1x after | {D['feb2020_3x_until_close_of_D_then_1x']['3x through 02-26, 1x after']:+.1f}% |
| 3x through 27-Feb, cash after | {D['feb2020_3x_until_close_of_D_then_cash']['3x through 02-27, cash after']:+.1f}% |
| 3x all month | {D['feb2020_3x_until_close_of_D_then_cash']['3x through 02-28, cash after']:+.1f}% |
| 2x through 25-Feb, cash after | {D['feb2020_2x_until_close_of_D_then_cash']['2x through 02-25, cash after']:+.1f}% |
| **published** | **-13.65%** |

The record sits between "3x through 25-Feb then cash" (-9.3%) and "3x through 25-Feb then 1x" (-14.1%): the rule cut from 3x to about 1x at the close of 25 or 26 Feb -- after two consecutive -3% days (10-day realised vol jumped from ~10% to ~30%, VIX 28) -- and did **not** hold 3x into the -4.5% day on 27-Feb (that alone would have made the month -22%). Equivalent 2x stories ("2x through 27-Feb then cash" = -15.1%) sit just outside tolerance. Fast, but one to two days late relative to the first shock: a realised-vol / repeated-shock trigger, not a VIX-level trigger (VIX had already jumped from 17 to 25 on 24-Feb and the rule stayed levered).

**Mar-2020 (+55.32%, SPY -12.36%).** The month had 10 up days summing to +47.5% and 12 down days summing to -57.5%; 3x buy-and-hold = -46%, perfect foresight (3x on up days only) = +270%. Only six {{0,1,2,3}} paths with <= 2 switches reproduce +55.3%, and they agree on the essentials:

- **in cash on every day from 6-Mar to 20-Mar** (the crash core: -7.8%, -9.6%, -10.9% days but also the +9.3% 13-Mar and +6.0% 17-Mar rebounds were all missed),
- **3x on 24, 25 and 26 March** (+9.1%, +1.5%, +5.8% = +56.1% compounded at 3x), i.e. the 3x position was put on at the close of Monday 23-Mar, the exact low, in five of the six paths (the sixth puts it on at the 20-Mar close, VIX/SMA10 = 1.00, and eats the -2.6% 23-Mar day at 3x),
- optionally 3x on 2-Mar (+4.3%) and/or 30-Mar (+3.3%), with cash on 27-Mar / 31-Mar.

Total: **3 to 10 days at 3x (3-6 of them in the 24-31 Mar rebound, the remainder, if any, on 2-5 Mar before the crash core), 12 to 19 days in cash, average leverage 0.4-1.4x** for a +55% month. The "enter 3x and hold to month-end" ladder shows how knife-edge the entry date is:

| 3x from (held to 31-Mar) | 19-Mar | 20-Mar | 23-Mar | **24-Mar** | 25-Mar | 26-Mar | 27-Mar |
|---|---|---|---|---|---|---|---|
| Mar-2020 return | {D['mar2020_enter_3x_and_hold']['3x from 03-19 to month-end']:+.1f}% | {D['mar2020_enter_3x_and_hold']['3x from 03-20 to month-end']:+.1f}% | {D['mar2020_enter_3x_and_hold']['3x from 03-23 to month-end']:+.1f}% | **{D['mar2020_enter_3x_and_hold']['3x from 03-24 to month-end']:+.1f}%** | {D['mar2020_enter_3x_and_hold']['3x from 03-25 to month-end']:+.1f}% | {D['mar2020_enter_3x_and_hold']['3x from 03-26 to month-end']:+.1f}% | {D['mar2020_enter_3x_and_hold']['3x from 03-27 to month-end']:+.1f}% |

What the indicators looked like at the 23-Mar close, when the decision was taken (this is the profile a re-entry trigger must fire on):

{T['d_mar2020_vix_path']}

At the 23-Mar close: SPX -34% from its high, RSI(2) = 8 (deeply oversold), 10-day realised vol 103% (a realised-vol gate would have forbidden entry), VIX 61.6 -- extremely high in level but 25% below its 16-Mar peak, below its 10-day average (VIX/SMA10 0.92 after five consecutive down days in VIX while price made a new low). The re-entry signal is therefore **"implied vol dissipating from an extreme + price oversold"** -- Demeter's variance-risk-premium and mean-reversion ingredients -- and explicitly not "vol is low again". Contrast rules over the same month: 3x-when-VIX<30 = 0.0%, 3x-when-VIX<40 = -12.0%, 3x-when-above-SMA200 = -17.9% (SPX was below its 200-day SMA all month), 1-day mean reversion at 3x (long after every down day) = +44.3% but with 12 invested days and a -28.7% February; 3x-when-VIX<its-10d-SMA = +37.6%.

**Apr-2020 (+29.65%, SPY +12.81%).** Constant-leverage equivalent 2.35x. One switch suffices; every 1-switch solution has **at least 14 of 21 days at 3x** and is invested on 7-14 Apr; e.g. cash 1-6 Apr (missing the -4.5% 1-Apr and the +6.7% 6-Apr) then 3x from 7-Apr to month-end = +29.4%; or 3x from 1-Apr through 14-Apr then cash = +29.8%; or 3x through 21-Apr then 1x = +30.2%. VIX was 57 -> 34 (never below 31) and realised vol 40% all month: the strategy was at maximum leverage in a VIX-40 environment because vol was *falling*. May-2020: 2.08x (VIX 37 -> 27; at least 5 days at 3x, 22-29 May in every path). Nov-2020: 1.52x (VIX 38 -> 21).

### 2022 (+19.24%, SPY -18.19%)

{T['d_2022']}

*`days<SMA200` = trading days in the month with SPX below its 200-day SMA.*

Which months in cash: **Feb (whole month, to within 0.16%), Apr (whole), Jun (whole)**, plus the second half of Jan (cash from 14-Jan), most of Aug after ~10-Aug, and 15-21 Dec. Which rallies caught: the 15-29 Mar post-FOMC rally (invested 18-30 Mar in every path, 1-2x), the July rally (~1x; 2-3x only 27-29 Jul), the October rally (~1x with a 3x burst around 18-Oct) and all of November at 1x. What went wrong: September (-8.16%) -- the rule stayed ~1x long for 18-20 of 21 days including the 20-27 Sep post-FOMC slide; December's early decline was taken at 1x. Note the leverage tier: in 2022 the invested state was **1x (occasionally 2x), never sustained 3x** -- consistent with "sometimes unlevered" in a VIX-25 regime. Also note that SPX was below its 200-day SMA on every day of Jul and Oct 2022 and on 20 of 21 days in Nov 2022, and yet the strategy was fully invested: the invest/cash decision is not a long-term trend filter.

### How many intra-month switches does the whole record need?

Across the 163 full months, the minimum number of {{0,1,2,3}} position changes that reproduces each month is 0 for 28 months (incl. the cash months), 1 for 128 and 2 for 7 (Sep-2014, Jan-2015, Jun-2015, Oct-2016, Feb-2020, Mar-2020, Jan-2025); no month needs 3+. That is a hard lower bound of 142 intra-month switches over 13.6 years (10.4/yr) *before* counting month-boundary changes; the whipsaw months and the daily decision framing imply the true count is several times higher.

## 5. (e) Quantitative summary

**Distribution of implied exposure (109 months with |SPY| > 2%)**

| bucket | share of months |
|---|---|
| exposure > 1.5x | {e['share_exposure_gt_1.5']:.1f}% (>2x: {e['share_exposure_gt_2']:.1f}%) |
| 0.5x .. 1.5x | {e['share_exposure_0.5_to_1.5']:.1f}% |
| 0.25x .. 0.5x | {e['share_exposure_0.25_to_0.5']:.1f}% |
| near 0 (|exposure| < 0.25) | {e['share_exposure_near_0']:.1f}% |
| negative (< -0.25, sign flip) | {e['share_exposure_negative_lt_-0.25']:.1f}% |

Mean {e['mean_exposure_all']:.2f}x, median {e['median_exposure_all']:.2f}x. In SPY up months > +2% (n={e['exposure_in_up_months']['n']}): mean {e['exposure_in_up_months']['mean']:.2f}x, median {e['exposure_in_up_months']['median']:.2f}x, {e['exposure_in_up_months']['share_gt_1.5']:.0f}% above 1.5x, {e['exposure_in_up_months']['share_lt_0.5']:.0f}% below 0.5x. In SPY down months < -2% (n={e['exposure_in_down_months']['n']}): mean {e['exposure_in_down_months']['mean']:.2f}x, median {e['exposure_in_down_months']['median']:.2f}x, {e['exposure_in_down_months']['share_gt_1']:.0f}% above 1x, {e['exposure_in_down_months']['share_lt_0.25']:.0f}% near zero, {e['exposure_in_down_months']['share_negative']:.0f}% negative. The compounding-consistent L\\* over all 136 solvable months: mean {e['L_const_distribution']['mean']:.2f}, median {e['L_const_distribution']['median']:.2f}; {e['L_const_distribution']['share_gt_3']:.0f}% of months have L\\* > 3 and {e['L_const_distribution']['share_negative']:.0f}% have L\\* < 0 -- both impossible without intra-month timing.

**Exposure by VIX regime (VIX averaged over the month's trading days; 163 months)**

{T['e_vixbins']}

Split at the median monthly-average VIX ({vs['median_vix_avg']:.1f}): low-VIX months mean implied exposure {vs['low_vix']['mean_exposure']:.2f}x (median {vs['low_vix']['median_exposure']:.2f}, mean L\\* {vs['low_vix']['mean_L_const']:.2f}); high-VIX months {vs['high_vix']['mean_exposure']:.2f}x (median {vs['high_vix']['median_exposure']:.2f}, mean L\\* {vs['high_vix']['mean_L_const']:.2f}). Average Demeter return {vs['low_vix']['mean_demeter_ret']:.2f}%/month in low-VIX months vs {vs['high_vix']['mean_demeter_ret']:.2f}% in high-VIX months, while SPY averaged {vs['low_vix']['mean_spy_ret']:.2f}% vs {vs['high_vix']['mean_spy_ret']:.2f}%: **the entire excess return over SPY was earned in the high-VIX half of the sample**, and in the calm half the strategy merely matched a ~1x SPY exposure. Exposure declines from ~1.2x (VIX < 13) to ~0.7x (VIX 20-30), but the VIX > 30 months (the 2020 rebound) carry the highest constant-equivalent leverage (median L\\* {e['vix_bins']['>30']['median L_const']:.2f}), so exposure is not a monotone function of the vol level.

Same split by the VIX close on the last day of the *previous* month (the causally available level):

{T['e_vixstart']}

**What implied exposure correlates with (Spearman, 106 months with |SPY|>2% and VIX data)**: VIX change within the month {e['exposure_correlates_spearman']['vs_vix_change_within_month_(reaction)']:+.2f}; realised vol in the month {e['exposure_correlates_spearman']['vs_realised_vol_(contemporaneous)']:+.2f}; VIX average {e['exposure_correlates_spearman']['vs_vix_avg_(contemporaneous)']:+.2f}; VIX at month start {e['exposure_correlates_spearman']['vs_vix_start_(causal)']:+.2f}; prior-month SPY {e['exposure_correlates_spearman']['vs_prior_month_spy_(causal)']:+.2f}; same-month SPY {e['exposure_correlates_spearman']['vs_spy_same_month']:+.2f}. Exposure responds to the *change* in vol during the month (de-lever when VIX rises, lever when it falls), not to the level that prevailed when the month started. After a prior month below -3% the median exposure is {e['exposure_after_prior_month']['prior_spy_lt_-3']['median_exp']:.2f}x (n={e['exposure_after_prior_month']['prior_spy_lt_-3']['n']}) vs {e['exposure_after_prior_month']['prior_spy_-3_to_3']['median_exp']:.2f}x after a flat month and {e['exposure_after_prior_month']['prior_spy_gt_3']['median_exp']:.2f}x after a month above +3% -- re-entry after a bad month is at about 1x, and exposure is *lower* after strong up months.

**Strong up months (SPY > +5%, n={e['strong_up_months_spy_gt_5']['n']})**: mean implied exposure {e['strong_up_months_spy_gt_5']['mean_exposure']:.2f}x, median {e['strong_up_months_spy_gt_5']['median_exposure']:.2f}x, only {e['strong_up_months_spy_gt_5']['share_gt_1.5']:.0f}% above 1.5x. Rebounds are captured at roughly market weight; the 114% up-capture comes from the many +2..+5% months at 1.5-2.5x in calm regimes plus Apr/Nov-2020, not from levering every rally.

{T['e_strong_up']}

**Convexity.** Regressing Demeter's monthly return on SPY: all months beta {r_all['beta']:.2f}, up-beta {r_all['up_beta']:.2f} (t={r_all['up_beta_t']:.1f}) vs down-beta {r_all['down_beta']:.2f} (t={r_all['down_beta_t']:.1f}), quadratic convexity coefficient {r_all['quad_convexity']:.3f} (t={r_all['quad_convexity_t']:.1f}), skew {r_all['skew_demeter']:.1f} vs SPY {r_all['skew_spy']:.1f}. Excluding Feb-Apr 2020: beta {r_ex['beta']:.2f}, up-beta {r_ex['up_beta']:.2f} vs down-beta {r_ex['down_beta']:.2f}, convexity t={r_ex['quad_convexity_t']:.1f}, skew {r_ex['skew_demeter']:.2f} vs SPY {r_ex['skew_spy']:.2f}, R^2 {r_ex['r2']:.2f}. The asymmetry survives without the 2020 outliers, at a more modest 1.0x-up / 0.4x-down.

**Sign-flip months** (Demeter and SPY of opposite sign with |SPY| > 2%): {len(e['sign_flip_months'])} months; each is explained by the month's two halves having opposite signs and the strategy being in for one half only:

{T['e_flip']}

**Daily quadrant fingerprint (Demeter's own counts: 804 loss-avoidance, 883 gain-sacrifice, 1022 amplified-gain, 768 amplified-loss days = {q['demeter_total_days']} days, {q['demeter_pct_cash']:.1f}% cash).** P(market up | invested) = {q['P_market_up_given_invested']:.1f}% vs P(market up | cash) = {q['P_market_up_given_cash']:.1f}% (unconditional {q['P_market_up_overall_demeter']:.1f}%; our data 2012-07..2026-02: {q['our_data_2012_07_to_2026_02']['pct_up']:.1f}% up days). P(invested | up day) = {q['P_invested_given_up_day']:.1f}% vs P(invested | down day) = {q['P_invested_given_down_day']:.1f}%. The day-ahead directional edge is only ~5 points; the 31% CAGR must come from being levered on *large* up days and flat on *large* down days (Mar-Apr 2020 alone: three days at 3x = +56%). Cash spells contained more up days than down days -- consistent with staying out through the first days of a rebound.

**Volatility-implied leverage.** Monthly std {e['vol_implied_leverage']['monthly_std_demeter']:.2f}% vs SPY {e['vol_implied_leverage']['monthly_std_spy']:.2f}%: if invested on a random half of days at constant L, L would be about {e['vol_implied_leverage']['lev_when_invested_if_50pct_days_random']:.1f}x (all months) or {e['vol_implied_leverage']['ex_2020_02_04']['lev_when_invested_if_50pct_days_random']:.1f}x (ex Feb-Apr 2020). Together with the ~1x medians above, the invested state is a mix of ~1x and ~3x, averaging roughly 1.5-2x.

## 6. Where the losses came from (worst and best months)

Worst 12 Demeter months:

{T['c_worst']}

Best 12 Demeter months:

{T['c_best']}

Eight of the twelve worst months happened with SPY down only 0.3-2.7% and month-start VIX of 13-19; in all of them the constant-leverage equivalent is 2-5x (Jun-2015 L\\* 4.96, Feb-2025 3.71, Oct-2024 3.49, Aug-2019 2.60, Oct-2020 2.55, Oct-2023 2.14), i.e. the rule was 2-3x levered during the down days and, in the L\\*>3 cases, *out* during some of the up days -- the classic whipsaw of a quick-exit/quick-re-entry rule in a choppy, low-vol month. By contrast the genuine crash months (Aug-2015, Oct/Dec-2018, Apr/Jun-2022, Mar-2020) were handled at 0-1x. The best months mirror this: with the exception of the 2020 rebounds they are calm months (VIX 14-21, falling) in which 3x was held on the big up days and avoided on the worst one or two days (Jan-2025 L\\* 5.96: either 3x on 15-22 Jan only, or 3x all month except the 24-27 Jan DeepSeek drop; Jul/Aug-2025 L\\* 3.3/4.2).

## 7. (f) Ranked rule ingredients most consistent with the record, and what the record rules out

**Six ingredients, ranked by how much of the record they explain**

""")
for r in ranked:
    md.append(f"**{r['rank']}. {r['ingredient']}**\n\n" + bl(r["evidence"]) + "\n")
md.append("**Ruled out**\n")
for i, r in enumerate(ruled_out, 1):
    md.append(f"{i}. **{r['item']}.** {r['why']}\n")
md.append(f"""
## 8. Quantitative constraints a candidate rule should satisfy (targets for the rule designers)

| dimension | constraint from the record |
|---|---|
""" + "\n".join(f"| {k.replace('_', ' ')} | {v} |" for k, v in constraints.items()) + f"""

Archetype fingerprint (coarse un-tuned rules run through `engine.run`, Jul-2012..Jan-2026, 2 bp costs; descriptive only -- see OOS disclosure):

{T['f_archetypes']}

No single archetype reproduces the record. The two with the highest monthly correlation are 1-day mean reversion (0.70, but -29% in Feb-2020 and -36% in 2022) and VIX dissipation (0.63, CAGR 32.5%, Sharpe 1.06, but max DD -29% and 51 changes/yr). Level-based gates (VIX<20, RV<15/25%, SMA200, the baseline) sit at 0.26-0.38 because they return ~0 in Mar/Apr-2020 and mis-time 2022. The record therefore points to a *composite*: a vol-shock exit (ingredient 1) protecting a mean-reversion / vol-dissipation re-entry (2), with the levered tier gated by the vol regime (3) and enough hysteresis to sit out whole months (4).

## Appendix A. Month-by-month table (implied exposure where |SPY| > 2%; VIX avg from daily data)

{T['a_full']}

## Appendix B. Daily detail, Feb / Mar / Apr 2020 (`3x day ret` = 3 x excess return that day)

**February 2020**

{T['d_daily_2020-02']}

**March 2020**

{T['d_daily_2020-03']}

**April 2020**

{T['d_daily_2020-04']}
""")
out = HERE / "results" / "demeter_inference.md"
out.write_text("\n".join(md))
print("wrote", out, len("\n".join(md)), "chars")
