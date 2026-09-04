# Demeter "Dual-Engine" strategy: what the daily rule must have been doing

*Inference from the published monthly record (Jul-2012 .. Jun-2026, 168 months) and our daily market data (`model/data/market_daily.csv`, full months Jul-2012 .. Jan-2026 = 163 months). Produced by `model/analysis/infer_demeter.py` (+ `compose_inference_md.py`); machine-readable companion: `results/demeter_inference.json`.*

**OOS disclosure.** `evaluate.py` was run 0 times for this note. Section 8 / Appendix C runs coarse, un-tuned archetype rules through `engine.run` over Demeter's live window purely to fingerprint the record; nothing here was used to tune model parameters and nothing here should be.

## 0. Headline verification and conventions

Recomputing Demeter's factsheet numbers from `monthly_returns.csv` over Jul-2012..Jan-2026 reproduces them exactly: CAGR 31.33%, annualised std 0.219, max drawdown -13.65% (monthly), Sharpe 1.275, beta 0.543, correlation 0.344, up-capture 113.6%, down-capture 22.9%, 72.4% positive months. Our S&P 500 total-return series matches Demeter's SPY column month by month (corr 0.9998, mean abs diff 0.06 pp), so daily-path arguments below are on the same footing as the published record.

Conventions: *implied exposure* = Demeter / SPY monthly return where |SPY| > 2% (109 of 168 months; the ratio is meaningless for small SPY moves). *L\** = the constant daily leverage that would reproduce the month from our daily data with cash earning 0 (compounding-consistent; values above 3 or below 0 are impossible for any fixed long-only position and therefore prove intra-month timing). *Minimum switches* = the smallest number of intra-month position changes among {0,1,2,3}-leverage paths (decided at the prior close, 2 bp per unit notional traded) that reproduce the published month within max(0.25 pp, 2% of |return|).

**Cash is booked at 0%.** The three months printed as exactly 0.00% (Jan-2016, Apr-2022, Jun-2022) coincide with 3-month T-bill accruals of +0.02%, +0.06% and +0.13%. The published series therefore does not credit T-bill interest on cash days (consistent with Demeter's statement that only 1022 of ~3477 days had a positive return, i.e. cash days are zeros). Our engine credits T-bills, so its cash months will print small positives; over 2012-2026 that is worth roughly 0.5%/yr to our engine, more after 2022.

## 1. (a) Month-by-month implied exposure

Full 168-row table in Appendix A. Yearly digest (implied exposure over the months with |SPY| > 2%; `cash_months` = months printed as exactly 0.00%):

| year | strat_yr | spy_yr | cash_months | vix_avg | n(|SPY|>2%) | exp mean | exp median | exp min | exp max |
|---|---|---|---|---|---|---|---|---|---|
| 2012 | 10.84 | 5.64 | 0 | 16.47 | 2 | 2.18 | 2.18 | 1.36 | 3.00 |
| 2013 | 32.60 | 32.27 | 0 | 14.23 | 9 | 0.90 | 1.12 | 0.03 | 1.62 |
| 2014 | 12.93 | 13.58 | 0 | 14.15 | 7 | 0.39 | 0.40 | -0.80 | 1.50 |
| 2015 | 9.95 | 1.30 | 0 | 16.68 | 6 | 0.73 | 0.81 | -0.32 | 2.24 |
| 2016 | 21.94 | 11.87 | 1 | 15.92 | 4 | 0.76 | 0.92 | -0.00 | 1.21 |
| 2017 | 33.27 | 21.74 | 0 | 11.10 | 5 | 1.82 | 2.20 | 0.19 | 2.42 |
| 2018 | 23.35 | -4.47 | 0 | 16.74 | 9 | 0.54 | 0.32 | -0.66 | 1.77 |
| 2019 | 17.10 | 31.37 | 0 | 15.37 | 8 | 0.70 | 0.64 | -0.32 | 2.11 |
| 2020 | 165.14 | 18.27 | 0 | 29.08 | 10 | 0.79 | 1.41 | -4.48 | 2.59 |
| 2021 | 40.97 | 28.62 | 0 | 19.72 | 9 | 0.91 | 1.16 | -0.65 | 1.82 |
| 2022 | 19.24 | -18.19 | 2 | 25.62 | 11 | 0.60 | 0.48 | -0.05 | 1.50 |
| 2023 | 25.33 | 26.17 | 0 | 16.84 | 9 | 1.11 | 1.00 | 0.44 | 2.72 |
| 2024 | 22.41 | 24.90 | 0 | 15.54 | 9 | 1.04 | 0.48 | -0.10 | 3.47 |
| 2025 | 42.26 | 17.78 | 0 | 18.97 | 8 | 2.20 | 1.89 | 0.65 | 4.43 |
| 2026 | 6.11 | 10.15 | 0 | 17.10 | 3 | 0.89 | 0.90 | 0.81 | 0.95 |

Reading: the typical implied exposure is about 1x (mean 0.96, median 0.95), NOT 2-3x. Years of 2x-plus behaviour are the calm low-VIX years (2012 H2, 2017, 2025) and the crisis-rebound year (2020 median 1.4x); in the high-VIX years (2018, 2022) exposure averaged 0.5-0.6x and in 2014/2019 (whipsaw years) it was 0.4-0.7x. Full-cash months: 2016-01 (SPY -4.97), 2022-04 (SPY -8.73), 2022-06 (SPY -8.26); in addition Feb-2022 (+0.16% vs SPY -3.00%) is constant-cash to within rounding.

## 2. (b) Rolling 12- and 36-month beta and up/down capture

Semi-annual snapshots (full monthly series in the JSON, keys `b_rolling.rolling_12m` / `rolling_36m`).

**12-month windows**

| month | beta | corr | up_capture | down_capture | Demeter 12m % | SPY 12m % |
|---|---|---|---|---|---|---|
| 2013-06 | 0.87 | 0.52 | 126.10 | 150.38 | 24.98 | 20.18 |
| 2013-12 | 0.66 | 0.59 | 101.40 | 104.50 | 32.60 | 32.27 |
| 2014-06 | 0.44 | 0.66 | 100.30 | -9.36 | 33.72 | 24.51 |
| 2014-12 | 0.32 | 0.27 | 73.17 | 31.00 | 12.93 | 13.58 |
| 2015-06 | 0.77 | 0.48 | 47.60 | 145.87 | -5.98 | 7.31 |
| 2015-12 | 0.89 | 0.70 | 111.22 | 63.85 | 9.95 | 1.30 |
| 2016-06 | 0.81 | 0.85 | 153.58 | 16.17 | 31.14 | 3.91 |
| 2016-12 | 0.62 | 0.63 | 118.40 | 25.49 | 21.94 | 11.87 |
| 2017-06 | 0.37 | 0.32 | 77.74 | -32.24 | 15.93 | 17.80 |
| 2017-12 | 1.25 | 0.55 | 146.57 |  | 33.27 | 21.74 |
| 2018-06 | 0.64 | 0.59 | 182.34 | -27.49 | 45.27 | 14.29 |
| 2018-12 | 0.37 | 0.67 | 118.55 | 3.13 | 23.35 | -4.47 |
| 2019-06 | 0.49 | 0.89 | 79.49 | 28.33 | 22.04 | 10.32 |
| 2019-12 | 0.81 | 0.81 | 71.67 | 118.84 | 17.10 | 31.37 |
| 2020-06 | -0.43 | -0.15 | 145.91 | -119.58 | 102.54 | 7.39 |
| 2020-12 | -0.08 | -0.03 | 155.70 | -105.41 | 165.14 | 18.27 |
| 2021-06 | 1.09 | 0.84 | 121.93 | 46.91 | 60.20 | 40.70 |
| 2021-12 | 0.74 | 0.77 | 101.26 | -35.47 | 40.97 | 28.62 |
| 2022-06 | 0.46 | 0.73 | 95.42 | 1.10 | 20.96 | -10.70 |
| 2022-12 | 0.74 | 0.91 | 120.32 | 29.70 | 19.24 | -18.19 |
| 2023-06 | 0.96 | 0.97 | 121.86 | 61.03 | 42.07 | 19.47 |
| 2023-12 | 0.84 | 0.82 | 93.29 | 85.86 | 25.33 | 26.17 |
| 2024-06 | 0.76 | 0.73 | 80.29 | 71.01 | 20.81 | 24.44 |
| 2024-12 | 0.94 | 0.62 | 90.72 | 90.74 | 22.41 | 24.90 |
| 2025-06 | 1.15 | 0.64 | 130.42 | 128.66 | 20.05 | 15.07 |
| 2025-12 | 1.44 | 0.75 | 187.58 | 122.32 | 42.26 | 17.78 |
| 2026-06 | 0.89 | 0.79 | 110.06 | 59.21 | 29.08 | 22.20 |

**36-month windows**

| month | beta | corr | up_capture | down_capture | Demeter 36m ann % | SPY 36m ann % |
|---|---|---|---|---|---|---|
| 2015-06 | 0.74 | 0.53 | 95.34 | 95.34 | 16.26 | 17.10 |
| 2015-12 | 0.72 | 0.60 | 96.11 | 62.39 | 18.08 | 15.02 |
| 2016-06 | 0.72 | 0.63 | 102.43 | 51.00 | 18.14 | 11.56 |
| 2016-12 | 0.70 | 0.59 | 100.37 | 47.93 | 14.83 | 8.78 |
| 2017-06 | 0.73 | 0.59 | 95.23 | 59.62 | 12.65 | 9.52 |
| 2017-12 | 0.82 | 0.66 | 125.94 | 52.59 | 21.35 | 11.32 |
| 2018-06 | 0.69 | 0.67 | 139.07 | 0.81 | 30.23 | 11.84 |
| 2018-12 | 0.47 | 0.57 | 128.29 | 8.46 | 26.09 | 9.17 |
| 2019-06 | 0.50 | 0.66 | 107.49 | 13.31 | 27.14 | 14.09 |
| 2019-12 | 0.51 | 0.61 | 103.43 | 34.20 | 24.40 | 15.17 |
| 2020-06 | 0.01 | 0.00 | 128.10 | -42.69 | 53.13 | 10.63 |
| 2020-12 | 0.19 | 0.09 | 118.00 | -31.10 | 56.46 | 14.07 |
| 2021-06 | 0.17 | 0.08 | 115.46 | -31.38 | 58.20 | 18.57 |
| 2021-12 | 0.14 | 0.06 | 113.18 | -49.91 | 63.58 | 25.96 |
| 2022-06 | 0.20 | 0.10 | 123.96 | -37.03 | 57.74 | 10.50 |
| 2022-12 | 0.38 | 0.21 | 129.59 | -22.06 | 64.57 | 7.56 |
| 2023-06 | 0.81 | 0.85 | 116.57 | 28.67 | 40.15 | 14.50 |
| 2023-12 | 0.70 | 0.83 | 103.59 | 32.89 | 28.19 | 9.91 |
| 2024-06 | 0.72 | 0.81 | 100.93 | 34.79 | 27.57 | 9.91 |
| 2024-12 | 0.71 | 0.77 | 100.13 | 46.53 | 22.30 | 8.84 |
| 2025-06 | 0.94 | 0.78 | 109.50 | 80.09 | 27.25 | 19.60 |
| 2025-12 | 1.00 | 0.70 | 118.11 | 98.05 | 29.71 | 22.89 |
| 2026-06 | 0.91 | 0.69 | 104.03 | 89.33 | 23.25 | 20.50 |

**Extremes of the 12-month windows**

| month | note | beta | corr | up_capture | down_capture | strat_ann | spy_ann |
|---|---|---|---|---|---|---|---|
| 2020-03 | min 12m beta | -1.28 | -0.43 | 58.86 | -78.55 | 43.07 | -7.07 |
| 2021-03 | max 12m beta | 1.57 | 0.86 | 149.10 | 46.91 | 108.06 | 56.24 |
| 2021-02 | min 12m down-capture | -0.55 | -0.23 | 155.24 | -210.10 | 211.89 | 31.19 |
| 2015-07 | max 12m down-capture | 0.89 | 0.51 | 66.73 | 169.16 | -1.49 | 11.10 |
| 2025-12 | max 12m up-capture | 1.44 | 0.75 | 187.58 | 122.32 | 42.26 | 17.78 |
| 2015-05 | min 12m up-capture | 0.44 | 0.40 | 46.70 | 38.15 | 6.08 | 11.69 |

Summary: 12-month beta ranges from -1.28 (2020-03) to 1.57 (2021-03), median 0.73; 28% of windows have beta < 0.5 and 17% have beta > 1. Median 12-month up-capture 116% vs down-capture 39%; 36-month medians 114% / 34%. Three regimes are visible: (i) 2013-2015: no consistent asymmetry yet (12-month down-capture swings between -9% and 150%, beta 0.3-0.9); (ii) 2016-2019: strong asymmetry (up-capture 100-180%, down-capture near zero or negative in most windows); (iii) 2020-2022 windows dominated by Mar-2020 (negative beta, negative down-capture), then 2023-2026 reverting to beta 0.7-1.4 with 12-month down-capture of 60-130% -- since 2023 the strategy has behaved much more like a ~1x market exposure with little downside protection than the full-period averages suggest. Designers should not expect a rule to deliver 23% down-capture in every sub-period; the 36-month windows since 2023 show 29-98%.

## 3. (c) Behaviour in SPY-down months worse than -3% and in the rebounds

| month | SPY | Demeter | exposure | L_const | SPY 1st half | SPY 2nd half | trough day | VIX start | VIX max | VIX end |
|---|---|---|---|---|---|---|---|---|---|---|
| 2014-01 | -3.46 | 1.51 | -0.44 | -0.43 | -0.02 | -3.51 | 29 | 13.72 | 18.41 | 18.41 |
| 2015-01 | -3.01 | 0.96 | -0.32 | -0.33 | -3.17 | 0.22 | 15 | 19.20 | 22.39 | 20.97 |
| 2015-08 | -6.04 | -4.79 | 0.79 | 0.79 | -0.51 | -5.61 | 25 | 12.12 | 40.74 | 28.43 |
| 2016-01 | -4.97 | 0.00 | -0.00 | -0.00 | -5.86 | 0.93 | 20 | 18.21 | 27.59 | 20.20 |
| 2018-02 | -3.69 | 2.42 | -0.66 | -0.72 | -5.64 | 2.12 | 08 | 13.54 | 37.32 | 19.85 |
| 2018-10 | -6.84 | -0.76 | 0.11 | 0.11 | -5.61 | -1.37 | 29 | 12.12 | 25.23 | 21.23 |
| 2018-12 | -9.04 | -1.63 | 0.18 | 0.18 | -5.51 | -3.49 | 24 | 18.07 | 36.07 | 25.42 |
| 2019-05 | -6.36 | -3.89 | 0.61 | 0.59 | -3.05 | -3.43 | 31 | 13.12 | 20.55 | 18.71 |
| 2020-02 | -8.24 | -13.65 | 1.66 | 1.72 | 4.76 | -12.10 | 28 | 18.84 | 40.11 | 40.11 |
| 2020-03 | -12.36 | 55.32 | -4.48 |  | -19.04 | 8.09 | 23 | 40.11 | 82.69 | 53.54 |
| 2020-09 | -3.81 | 3.42 | -0.90 |  | -2.62 | -1.16 | 23 | 26.41 | 33.60 | 26.37 |
| 2021-09 | -4.66 | -1.37 | 0.29 | 0.29 | -0.81 | -3.88 | 30 | 16.48 | 25.71 | 23.14 |
| 2022-01 | -5.18 | -2.48 | 0.48 | 0.47 | -2.16 | -3.19 | 27 | 17.22 | 31.96 | 24.83 |
| 2022-04 | -8.73 | 0.00 | -0.00 | -0.00 | -3.07 | -5.89 | 29 | 20.56 | 33.52 | 33.40 |
| 2022-06 | -8.26 | 0.00 | -0.00 | -0.00 | -9.46 | 1.34 | 16 | 26.19 | 34.02 | 28.71 |
| 2022-08 | -4.09 | -0.41 | 0.10 | 0.10 | 4.09 | -7.85 | 31 | 21.33 | 26.21 | 25.87 |
| 2022-09 | -9.22 | -8.16 | 0.89 | 0.86 | -1.28 | -8.07 | 30 | 25.87 | 32.60 | 31.62 |
| 2022-12 | -5.77 | -2.03 | 0.35 | 0.33 | -2.03 | -3.81 | 28 | 20.58 | 25.00 | 21.67 |
| 2023-09 | -4.77 | -2.25 | 0.47 | 0.43 | -1.20 | -3.58 | 26 | 13.57 | 18.94 | 17.52 |
| 2024-04 | -4.09 | -1.98 | 0.48 | 0.44 | -3.56 | -0.49 | 19 | 13.01 | 19.23 | 15.65 |
| 2025-03 | -5.64 | -7.55 | 1.34 | 1.28 | -5.28 | -0.31 | 13 | 19.63 | 27.86 | 22.28 |
| 2026-03 | -4.99 | -4.74 | 0.95 |  |  |  |  |  |  |  |

*`SPY 1st/2nd half` = SPY return over the first/second half of the month's trading days; `trough day` = calendar day of the intra-month low.*

Rebounds that followed (`next`/`next2` = the following two months; `exp` = implied exposure where |SPY| > 2%):

| month | SPY | Demeter | next SPY | next Demeter | next exp | next2 SPY | next2 Demeter | next2 exp |
|---|---|---|---|---|---|---|---|---|
| 2014-01 | -3.46 | 1.51 | 4.57 | 3.36 | 0.74 | 0.83 | 2.78 |  |
| 2015-01 | -3.01 | 0.96 | 5.74 | 4.78 | 0.83 | -1.59 | -0.36 |  |
| 2015-08 | -6.04 | -4.79 | -2.48 | 0.61 | -0.25 | 8.43 | 8.99 | 1.07 |
| 2016-01 | -4.97 | 0.00 | -0.14 | -2.35 |  | 6.78 | 8.19 | 1.21 |
| 2018-02 | -3.69 | 2.42 | -2.55 | -0.68 | 0.27 | 0.38 | 5.69 |  |
| 2018-10 | -6.84 | -0.76 | 2.03 | 2.08 | 1.02 | -9.04 | -1.63 | 0.18 |
| 2018-12 | -9.04 | -1.63 | 8.01 | 7.65 | 0.96 | 3.20 | 3.59 | 1.12 |
| 2019-05 | -6.36 | -3.89 | 7.04 | 4.75 | 0.67 | 1.43 | 0.37 |  |
| 2020-02 | -8.24 | -13.65 | -12.36 | 55.32 | -4.48 | 12.81 | 29.65 | 2.31 |
| 2020-03 | -12.36 | 55.32 | 12.81 | 29.65 | 2.31 | 4.75 | 9.66 | 2.03 |
| 2020-09 | -3.81 | 3.42 | -2.67 | -6.92 | 2.59 | 10.94 | 16.87 | 1.54 |
| 2021-09 | -4.66 | -1.37 | 7.00 | 8.46 | 1.21 | -0.70 | 3.45 |  |
| 2022-01 | -5.18 | -2.48 | -3.00 | 0.16 | -0.05 | 3.70 | 5.54 | 1.50 |
| 2022-04 | -8.73 | 0.00 | 0.18 | 0.71 |  | -8.26 | 0.00 | -0.00 |
| 2022-06 | -8.26 | 0.00 | 9.21 | 10.64 | 1.16 | -4.09 | -0.41 | 0.10 |
| 2022-08 | -4.09 | -0.41 | -9.22 | -8.16 | 0.89 | 8.09 | 10.04 | 1.24 |
| 2022-09 | -9.22 | -8.16 | 8.09 | 10.04 | 1.24 | 5.58 | 5.28 | 0.95 |
| 2022-12 | -5.77 | -2.03 | 6.28 | 9.65 | 1.54 | -2.45 | -2.44 | 1.00 |
| 2023-09 | -4.77 | -2.25 | -2.11 | -5.74 | 2.72 | 9.12 | 4.31 | 0.47 |
| 2024-04 | -4.09 | -1.98 | 4.95 | 5.91 | 1.19 | 3.58 | 7.13 | 1.99 |
| 2025-03 | -5.64 | -7.55 | -0.69 | 4.94 |  | 6.29 | 4.11 | 0.65 |
| 2026-03 | -4.99 | -4.74 | 10.48 | 8.48 | 0.81 | 5.26 | 4.73 | 0.90 |

Named episodes with SPY between -1% and -3% (not in the table above), showing where the big *losses* actually came from:

| month | SPY | Demeter | L_const | 3x all month | min switches | must be invested | must be cash | VIX start | VIX end | RV % |
|---|---|---|---|---|---|---|---|---|---|---|
| 2015-09 | -2.48 | 0.61 | -0.26 | -8.60 | 1 | 09-02, 09-03, 09-04, 09-08, 09-09, 09-10... |  | 28.43 | 24.50 | 22.50 |
| 2023-08 | -1.60 | 1.14 | -0.56 | -6.55 | 1 | 08-14, 08-15, 08-16, 08-17, 08-18, 08-21... |  | 13.63 | 13.57 | 12.30 |
| 2023-10 | -2.11 | -5.74 | 2.14 | -8.14 | 1 | 10-19, 10-20 |  | 17.52 | 18.14 | 14.00 |
| 2025-02 | -1.31 | -6.35 | 3.71 | -5.03 | 1 | 02-20, 02-21, 02-24, 02-25, 02-26, 02-27 |  | 16.43 | 19.63 | 13.10 |
| 2020-10 | -2.67 | -6.92 | 2.55 | -8.31 | 1 | 10-28, 10-29, 10-30 |  | 26.37 | 38.02 | 20.40 |
| 2019-08 | -1.59 | -5.62 | 2.60 | -6.72 | 1 | 08-01, 08-02, 08-05, 08-06, 08-07, 08-08... |  | 16.12 | 18.98 | 23.00 |
| 2014-12 | -0.26 | -6.19 |  | -1.35 | 1 | 12-01, 12-02, 12-03, 12-04, 12-05, 12-08... | 12-15, 12-16, 12-17, 12-18, 12-19, 12-22... | 13.33 | 19.20 | 15.40 |
| 2024-10 | -0.92 | -4.92 | 3.49 | -4.17 | 1 | 10-18, 10-21, 10-22, 10-23, 10-24, 10-25... |  | 16.73 | 23.16 | 11.10 |

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

Pattern: in 20 of 22 months below -3% the strategy beat SPY (mean implied exposure 0.09x, median 0.24x); the exit is fast (within 1-3 days of the first -2%/-3% day) and re-entry in the following rebound month is at about 1x (median 1.09x when the next month's SPY > 2%) -- the 2-3x rebound leverage of Apr/May/Nov-2020 is the exception, not the norm. The costly months are not the crash months but choppy months with mild SPY losses where the rule was 2-3x levered (section 6).

## 4. (d) What a daily rule had to do in 2020 and 2022

### Feb / Mar / Apr 2020

| month | SPY | Demeter | exposure | L_const | min switches | 3x days (min-max) | 1x | 2x | 3x | 3x up-days only | VIX first | VIX last | RV % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2020-01 | -0.05 | 2.81 |  |  |  |  | -0.17 | -0.45 | -0.86 | 19.54 | 12.50 | 18.80 | 12.20 |
| 2020-02 | -8.24 | -13.65 | 1.66 | 1.72 | 2 | 0-16 | -8.02 | -15.83 | -23.40 | 19.09 | 18.00 | 40.10 | 24.90 |
| 2020-03 | -12.36 | 55.32 | -4.48 |  | 2 | 3-10 | -12.51 | -28.71 | -46.28 | 270.04 | 33.40 | 53.50 | 89.70 |
| 2020-04 | 12.81 | 29.65 | 2.31 | 2.35 | 1 | 5-17 | 12.69 | 25.31 | 37.58 | 121.31 | 57.10 | 34.10 | 40.40 |
| 2020-05 | 4.75 | 9.66 | 2.03 | 2.08 | 1 | 1-17 | 4.75 | 9.31 | 13.62 | 49.94 | 37.20 | 27.50 | 22.40 |
| 2020-06 | 1.98 | 2.15 |  |  |  |  | 1.76 | 2.79 | 3.03 | 56.94 | 28.20 | 30.40 | 28.70 |
| 2020-09 | -3.81 | 3.42 | -0.90 |  |  |  | -3.75 | -7.82 | -12.17 | 40.44 | 26.10 | 26.40 | 24.50 |
| 2020-10 | -2.67 | -6.92 | 2.59 | 2.55 |  |  | -2.50 | -5.28 | -8.31 | 33.64 | 26.70 | 38.00 | 20.40 |
| 2020-11 | 10.94 | 16.87 | 1.54 | 1.52 | 1 | 0-2 | 10.87 | 22.62 | 35.28 | 53.53 | 37.10 | 20.60 | 16.30 |

*`1x/2x/3x` = return of that constant leverage all month; `3x up-days only` = perfect-foresight upper bound.*

**Feb-2020 (-13.65%, SPY -8.24%).** No single-switch path reproduces the month; 79 two-switch paths do, and they agree that the strategy was invested on every day of the month at a mean leverage of 1.5-2.1x (constant-equivalent 1.72x), including the first two crash days 24-25 Feb (-3.3% and -3.0%), and that 3x was not held into 27-Feb. The cleanest family -- 3x through the top (SPY +5.2% to 19-Feb, VIX 14) and through 24-25 Feb (-10.0% and -9.1% daily at 3x), then de-levered -- shows the arithmetic:

| scenario | Feb-2020 return |
|---|---|
| 3x through 21-Feb, cash after | +10.8% |
| 3x through 24-Feb, cash after | -0.2% |
| 3x through 25-Feb, cash after | -9.3% |
| 3x through 25-Feb, 1x after | -14.1% |
| 3x through 26-Feb, 1x after | -14.7% |
| 3x through 27-Feb, cash after | -22.4% |
| 3x all month | -23.4% |
| 2x through 25-Feb, cash after | -6.0% |
| **published** | **-13.65%** |

The record sits between "3x through 25-Feb then cash" (-9.3%) and "3x through 25-Feb then 1x" (-14.1%): the rule cut from 3x to about 1x at the close of 25 or 26 Feb -- after two consecutive -3% days (10-day realised vol jumped from ~10% to ~30%, VIX 28) -- and did **not** hold 3x into the -4.5% day on 27-Feb (that alone would have made the month -22%). Equivalent 2x stories ("2x through 27-Feb then cash" = -15.1%) sit just outside tolerance. Fast, but one to two days late relative to the first shock: a realised-vol / repeated-shock trigger, not a VIX-level trigger (VIX had already jumped from 17 to 25 on 24-Feb and the rule stayed levered).

**Mar-2020 (+55.32%, SPY -12.36%).** The month had 10 up days summing to +47.5% and 12 down days summing to -57.5%; 3x buy-and-hold = -46%, perfect foresight (3x on up days only) = +270%. Only six {0,1,2,3} paths with <= 2 switches reproduce +55.3%, and they agree on the essentials:

- **in cash on every day from 6-Mar to 20-Mar** (the crash core: -7.8%, -9.6%, -10.9% days but also the +9.3% 13-Mar and +6.0% 17-Mar rebounds were all missed),
- **3x on 24, 25 and 26 March** (+9.1%, +1.5%, +5.8% = +56.1% compounded at 3x), i.e. the 3x position was put on at the close of Monday 23-Mar, the exact low, in five of the six paths (the sixth puts it on at the 20-Mar close, VIX/SMA10 = 1.00, and eats the -2.6% 23-Mar day at 3x),
- optionally 3x on 2-Mar (+4.3%) and/or 30-Mar (+3.3%), with cash on 27-Mar / 31-Mar.

Total: **3 to 10 days at 3x (3-6 of them in the 24-31 Mar rebound, the remainder, if any, on 2-5 Mar before the crash core), 12 to 19 days in cash, average leverage 0.4-1.4x** for a +55% month. The "enter 3x and hold to month-end" ladder shows how knife-edge the entry date is:

| 3x from (held to 31-Mar) | 19-Mar | 20-Mar | 23-Mar | **24-Mar** | 25-Mar | 26-Mar | 27-Mar |
|---|---|---|---|---|---|---|---|
| Mar-2020 return | +20.6% | +19.9% | +37.6% | **+49.1%** | +17.2% | +12.2% | -4.5% |

What the indicators looked like at the 23-Mar close, when the decision was taken (this is the profile a re-entry trigger must fire on):

| date | SPY ret % | VIX | VIX SMA10 | VIX/SMA10 | RV10 ann % | DD from high % | RSI(2) |
|---|---|---|---|---|---|---|---|
| 2020-03-09 | -7.81 | 54.46 | 37.29 | 1.46 | 59.22 | -18.95 | 6.38 |
| 2020-03-10 | 5.17 | 47.30 | 39.24 | 1.21 | 67.23 | -14.75 | 51.10 |
| 2020-03-11 | -4.87 | 53.90 | 41.87 | 1.29 | 70.30 | -18.91 | 26.25 |
| 2020-03-12 | -9.57 | 75.47 | 45.50 | 1.66 | 80.84 | -26.67 | 9.32 |
| 2020-03-13 | 8.55 | 57.83 | 47.27 | 1.22 | 95.89 | -20.40 | 55.60 |
| 2020-03-16 | -10.94 | 82.69 | 52.20 | 1.58 | 103.44 | -29.11 | 22.99 |
| 2020-03-17 | 5.40 | 75.91 | 56.11 | 1.35 | 110.29 | -25.28 | 49.18 |
| 2020-03-18 | -5.06 | 76.45 | 60.56 | 1.26 | 106.66 | -29.07 | 29.41 |
| 2020-03-19 | 0.21 | 72.00 | 63.79 | 1.13 | 107.29 | -28.91 | 31.60 |
| 2020-03-20 | -4.31 | 66.04 | 66.20 | 1.00 | 107.84 | -32.38 | 13.03 |
| 2020-03-23 | -2.56 | 61.59 | 66.92 | 0.92 | 103.49 | -34.10 | 8.21 |
| 2020-03-24 | 9.06 | 61.67 | 68.36 | 0.90 | 112.29 | -28.13 | 74.18 |
| 2020-03-25 | 1.50 | 63.95 | 69.36 | 0.92 | 111.33 | -27.06 | 79.49 |
| 2020-03-26 | 5.84 | 61.00 | 67.91 | 0.90 | 103.86 | -22.80 | 92.20 |
| 2020-03-27 | -2.98 | 65.54 | 68.68 | 0.95 | 95.47 | -25.10 | 55.24 |

At the 23-Mar close: SPX -34% from its high, RSI(2) = 8 (deeply oversold), 10-day realised vol 103% (a realised-vol gate would have forbidden entry), VIX 61.6 -- extremely high in level but 25% below its 16-Mar peak, below its 10-day average (VIX/SMA10 0.92 after five consecutive down days in VIX while price made a new low). The re-entry signal is therefore **"implied vol dissipating from an extreme + price oversold"** -- Demeter's variance-risk-premium and mean-reversion ingredients -- and explicitly not "vol is low again". Contrast rules over the same month: 3x-when-VIX<30 = 0.0%, 3x-when-VIX<40 = -12.0%, 3x-when-above-SMA200 = -17.9% (SPX was below its 200-day SMA all month), 1-day mean reversion at 3x (long after every down day) = +44.3% but with 12 invested days and a -28.7% February; 3x-when-VIX<its-10d-SMA = +37.6%.

**Apr-2020 (+29.65%, SPY +12.81%).** Constant-leverage equivalent 2.35x. One switch suffices; every 1-switch solution has **at least 14 of 21 days at 3x** and is invested on 7-14 Apr; e.g. cash 1-6 Apr (missing the -4.5% 1-Apr and the +6.7% 6-Apr) then 3x from 7-Apr to month-end = +29.4%; or 3x from 1-Apr through 14-Apr then cash = +29.8%; or 3x through 21-Apr then 1x = +30.2%. VIX was 57 -> 34 (never below 31) and realised vol 40% all month: the strategy was at maximum leverage in a VIX-40 environment because vol was *falling*. May-2020: 2.08x (VIX 37 -> 27; at least 5 days at 3x, 22-29 May in every path). Nov-2020: 1.52x (VIX 38 -> 21).

### 2022 (+19.24%, SPY -18.19%)

| month | SPY | Demeter | exposure | L_const | min switches | n paths | 3x days (min-max) | cash days (min-max) | 1x all month | 3x all month | VIX first | VIX last | RV % | days<SMA200 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2022-01 | -5.18 | -2.48 | 0.48 | 0.47 | 1 | 2 | 0-0 | 11-13 | -5.29 | -15.74 | 16.60 | 24.80 | 18.70 | 6 |
| 2022-02 | -3.00 | 0.16 | -0.05 | -0.06 | 0 | 1 | 0-0 | 19-19 | -2.98 | -9.67 | 22.00 | 30.10 | 22.40 | 9 |
| 2022-03 | 3.70 | 5.54 | 1.50 | 1.53 | 1 | 9 | 0-4 | 0-13 | 3.72 | 9.98 | 33.30 | 20.60 | 23.30 | 16 |
| 2022-04 | -8.73 | 0.00 | -0.00 | -0.00 | 0 | 1 | 0-0 | 20-20 | -8.83 | -25.43 | 19.60 | 33.40 | 24.90 | 16 |
| 2022-05 | 0.18 | 0.71 |  |  | 1 | 7 | 0-4 | 0-20 | 0.14 | -1.95 | 32.30 | 26.20 | 31.30 | 21 |
| 2022-06 | -8.26 | 0.00 | -0.00 | -0.00 | 0 | 1 | 0-0 | 21-21 | -8.36 | -24.78 | 25.70 | 28.70 | 29.70 | 21 |
| 2022-07 | 9.21 | 10.64 | 1.16 | 1.17 | 1 | 5 | 0-7 | 0-17 | 9.02 | 28.39 | 26.70 | 21.30 | 19.20 | 20 |
| 2022-08 | -4.09 | -0.41 | 0.10 | 0.10 | 1 | 6 | 0-15 | 0-22 | -4.31 | -13.28 | 22.80 | 25.90 | 19.30 | 23 |
| 2022-09 | -9.22 | -8.16 | 0.89 | 0.86 | 1 | 4 | 0-0 | 1-12 | -9.48 | -27.00 | 25.60 | 31.60 | 23.90 | 21 |
| 2022-10 | 8.09 | 10.04 | 1.24 | 1.29 | 1 | 7 | 0-19 | 0-11 | 7.80 | 22.92 | 30.10 | 25.90 | 27.90 | 21 |
| 2022-11 | 5.58 | 5.28 | 0.95 | 1.02 | 0 | 1 | 0-0 | 0-0 | 5.20 | 14.36 | 25.80 | 20.60 | 27.90 | 20 |
| 2022-12 | -5.77 | -2.03 | 0.35 | 0.33 | 1 | 3 | 0-0 | 11-18 | -6.10 | -17.89 | 19.80 | 21.70 | 18.00 | 19 |

*`days<SMA200` = trading days in the month with SPX below its 200-day SMA.*

Which months in cash: **Feb (whole month, to within 0.16%), Apr (whole), Jun (whole)**, plus the second half of Jan (cash from 14-Jan), most of Aug after ~10-Aug, and 15-21 Dec. Which rallies caught: the 15-29 Mar post-FOMC rally (invested 18-30 Mar in every path, 1-2x), the July rally (~1x; 2-3x only 27-29 Jul), the October rally (~1x with a 3x burst around 18-Oct) and all of November at 1x. What went wrong: September (-8.16%) -- the rule stayed ~1x long for 18-20 of 21 days including the 20-27 Sep post-FOMC slide; December's early decline was taken at 1x. Note the leverage tier: in 2022 the invested state was **1x (occasionally 2x), never sustained 3x** -- consistent with "sometimes unlevered" in a VIX-25 regime. Also note that SPX was below its 200-day SMA on every day of Jul and Oct 2022 and on 20 of 21 days in Nov 2022, and yet the strategy was fully invested: the invest/cash decision is not a long-term trend filter.

### How many intra-month switches does the whole record need?

Across the 163 full months, the minimum number of {0,1,2,3} position changes that reproduces each month is 0 for 28 months (incl. the cash months), 1 for 128 and 2 for 7 (Sep-2014, Jan-2015, Jun-2015, Oct-2016, Feb-2020, Mar-2020, Jan-2025); no month needs 3+. That is a hard lower bound of 142 intra-month switches over 13.6 years (10.4/yr) *before* counting month-boundary changes; the whipsaw months and the daily decision framing imply the true count is several times higher.

## 5. (e) Quantitative summary

**Distribution of implied exposure (109 months with |SPY| > 2%)**

| bucket | share of months |
|---|---|
| exposure > 1.5x | 25.7% (>2x: 13.8%) |
| 0.5x .. 1.5x | 39.4% |
| 0.25x .. 0.5x | 22.0% |
| near 0 (|exposure| < 0.25) | 12.8% |
| negative (< -0.25, sign flip) | 7.3% |

Mean 0.96x, median 0.95x. In SPY up months > +2% (n=79): mean 1.22x, median 1.14x, 32% above 1.5x, 22% below 0.5x. In SPY down months < -2% (n=30): mean 0.28x, median 0.28x, 13% above 1x, 30% near zero, 27% negative. The compounding-consistent L\* over all 136 solvable months: mean 1.22, median 1.02; 9% of months have L\* > 3 and 13% have L\* < 0 -- both impossible without intra-month timing.

**Exposure by VIX regime (VIX averaged over the month's trading days; 163 months)**

| vix_bin | n months | n |SPY|>2% | mean exposure | median exposure | mean L_const | median L_const | mean Demeter % | mean SPY % | std Demeter % | std SPY % | full-cash months |
|---|---|---|---|---|---|---|---|---|---|---|---|
| <13 | 24 | 14 | 1.24 | 1.23 | 1.30 | 1.27 | 2.28 | 2.18 | 2.58 | 1.66 | 0 |
| 13-16 | 58 | 35 | 1.00 | 0.95 | 1.22 | 1.10 | 2.38 | 2.09 | 3.08 | 2.72 | 0 |
| 16-20 | 44 | 25 | 1.14 | 1.02 | 1.43 | 1.06 | 0.88 | 0.41 | 5.25 | 3.72 | 0 |
| 20-25 | 23 | 21 | 0.73 | 0.83 | 0.84 | 0.79 | 2.60 | 0.50 | 5.30 | 5.85 | 2 |
| 25-30 | 8 | 7 | 0.69 | 0.78 | 0.94 | 0.81 | -0.10 | -2.18 | 5.02 | 5.23 | 1 |
| >30 | 6 | 4 | 0.28 | 1.64 | 1.91 | 2.08 | 18.63 | 2.43 | 20.40 | 8.65 | 0 |

Split at the median monthly-average VIX (15.9): low-VIX months mean implied exposure 1.07x (median 0.95, mean L\* 1.25); high-VIX months 0.87x (median 0.95, mean L\* 1.20). Average Demeter return 2.35%/month in low-VIX months vs 2.59% in high-VIX months, while SPY averaged 2.12% vs 0.33%: **the entire excess return over SPY was earned in the high-VIX half of the sample**, and in the calm half the strategy merely matched a ~1x SPY exposure. Exposure declines from ~1.2x (VIX < 13) to ~0.7x (VIX 20-30), but the VIX > 30 months (the 2020 rebound) carry the highest constant-equivalent leverage (median L\* 2.08), so exposure is not a monotone function of the vol level.

Same split by the VIX close on the last day of the *previous* month (the causally available level):

| vix_start_bin | n months | n |SPY|>2% | mean exposure | median exposure | mean L_const | mean Demeter % | mean SPY % | full-cash months |
|---|---|---|---|---|---|---|---|---|
| <13 | 26 | 13 | 1.11 | 0.92 | 1.26 | 1.54 | 1.15 | 0 |
| 13-16 | 49 | 24 | 0.68 | 0.55 | 1.02 | 1.20 | 0.75 | 0 |
| 16-20 | 50 | 36 | 1.27 | 1.12 | 1.50 | 1.59 | 1.00 | 1 |
| 20-25 | 18 | 15 | 0.80 | 1.02 | 0.98 | 3.66 | 2.20 | 1 |
| 25-30 | 11 | 10 | 0.70 | 0.86 | 0.87 | 1.96 | 0.65 | 1 |
| >30 | 9 | 8 | 0.80 | 1.50 | 1.58 | 15.15 | 4.06 | 0 |

**What implied exposure correlates with (Spearman, 106 months with |SPY|>2% and VIX data)**: VIX change within the month -0.30; realised vol in the month -0.21; VIX average -0.12; VIX at month start +0.03; prior-month SPY -0.12; same-month SPY +0.25. Exposure responds to the *change* in vol during the month (de-lever when VIX rises, lever when it falls), not to the level that prevailed when the month started. After a prior month below -3% the median exposure is 0.99x (n=18) vs 1.08x after a flat month and 0.65x after a month above +3% -- re-entry after a bad month is at about 1x, and exposure is *lower* after strong up months.

**Strong up months (SPY > +5%, n=26)**: mean implied exposure 1.07x, median 1.05x, only 19% above 1.5x. Rebounds are captured at roughly market weight; the 114% up-capture comes from the many +2..+5% months at 1.5-2.5x in calm regimes plus Apr/Nov-2020, not from levering every rally.

| date | Demeter | SPY | exposure | prior SPY | vix_start | vix_end | VIX chg % |
|---|---|---|---|---|---|---|---|
| 2013-01 | 0.16 | 5.17 | 0.03 | 0.90 | 18.02 | 14.28 | -20.75 |
| 2013-07 | 5.71 | 5.08 | 1.12 | -1.35 | 16.86 | 13.45 | -20.23 |
| 2015-02 | 4.78 | 5.74 | 0.83 | -3.01 | 20.97 | 13.34 | -36.39 |
| 2015-10 | 8.99 | 8.43 | 1.07 | -2.48 | 24.50 | 15.07 | -38.49 |
| 2016-03 | 8.19 | 6.78 | 1.21 | -0.14 | 20.55 | 13.95 | -32.12 |
| 2018-01 | 5.26 | 5.72 | 0.92 | 1.10 | 11.04 | 13.54 | 22.64 |
| 2019-01 | 7.65 | 8.01 | 0.96 | -9.04 | 25.42 | 16.57 | -34.82 |
| 2019-06 | 4.75 | 7.04 | 0.67 | -6.36 | 18.71 | 15.08 | -19.40 |
| 2020-04 | 29.65 | 12.81 | 2.31 | -12.36 | 53.54 | 34.15 | -36.22 |
| 2020-07 | 4.41 | 5.63 | 0.78 | 1.98 | 30.43 | 24.46 | -19.62 |
| 2020-08 | 7.44 | 7.18 | 1.04 | 5.63 | 24.46 | 26.41 | 7.97 |
| 2020-11 | 16.87 | 10.94 | 1.54 | -2.67 | 38.02 | 20.57 | -45.90 |
| 2021-04 | 6.88 | 5.33 | 1.29 | 4.37 | 19.40 | 18.61 | -4.07 |
| 2021-10 | 8.46 | 7.00 | 1.21 | -4.66 | 23.14 | 16.26 | -29.73 |
| 2022-07 | 10.64 | 9.21 | 1.16 | -8.26 | 28.71 | 21.33 | -25.71 |
| 2022-10 | 10.04 | 8.09 | 1.24 | -9.22 | 31.62 | 25.88 | -18.15 |
| 2022-11 | 5.28 | 5.58 | 0.95 | 8.09 | 25.88 | 20.58 | -20.48 |
| 2023-01 | 9.65 | 6.28 | 1.54 | -5.77 | 21.67 | 19.40 | -10.48 |
| 2023-06 | 7.54 | 6.60 | 1.14 | 0.43 | 17.94 | 13.59 | -24.25 |
| 2023-11 | 4.31 | 9.12 | 0.47 | -2.11 | 18.14 | 12.92 | -28.78 |
| 2024-02 | 8.88 | 5.33 | 1.67 | 1.67 | 14.35 | 13.40 | -6.62 |
| 2024-11 | 1.21 | 5.86 | 0.21 | -0.92 | 23.16 | 13.51 | -41.67 |
| 2025-05 | 4.11 | 6.29 | 0.65 | -0.69 | 24.70 | 18.57 | -24.82 |
| 2025-06 | 10.08 | 5.08 | 1.98 | 6.29 | 18.57 | 16.73 | -9.91 |
| 2026-04 | 8.48 | 10.48 | 0.81 | -4.99 |  |  |  |
| 2026-05 | 4.73 | 5.26 | 0.90 | 10.48 |  |  |  |

**Convexity.** Regressing Demeter's monthly return on SPY: all months beta 0.56, up-beta 1.39 (t=7.9) vs down-beta -0.48 (t=-2.3), quadratic convexity coefficient 0.115 (t=8.0), skew 3.9 vs SPY -0.4. Excluding Feb-Apr 2020: beta 0.76, up-beta 1.01 vs down-beta 0.42, convexity t=3.1, skew 0.04 vs SPY -0.35, R^2 0.49. The asymmetry survives without the 2020 outliers, at a more modest 1.0x-up / 0.4x-down.

**Sign-flip months** (Demeter and SPY of opposite sign with |SPY| > 2%): 11 months; each is explained by the month's two halves having opposite signs and the strategy being in for one half only:

| month | SPY | Demeter | SPY 1st half % | SPY 2nd half % | VIX start | VIX end |
|---|---|---|---|---|---|---|
| 2014-01 | -3.46 | 1.51 | -0.02 | -3.51 | 13.72 | 18.41 |
| 2014-10 | 2.43 | -1.94 | -5.38 | 8.17 | 16.31 | 14.03 |
| 2015-01 | -3.01 | 0.96 | -3.17 | 0.22 | 19.20 | 20.97 |
| 2015-09 | -2.48 | 0.61 | 0.40 | -2.94 | 28.43 | 24.50 |
| 2018-02 | -3.69 | 2.42 | -5.64 | 2.12 | 13.54 | 19.85 |
| 2019-12 | 3.01 | -0.97 | 0.96 | 1.93 | 12.62 | 13.78 |
| 2020-03 | -12.36 | 55.32 | -19.04 | 8.09 | 40.11 | 53.54 |
| 2020-09 | -3.81 | 3.42 | -2.62 | -1.16 | 26.41 | 26.37 |
| 2021-07 | 2.37 | -1.55 | 1.56 | 0.86 | 15.83 | 18.24 |
| 2022-02 | -3.00 | 0.16 | -2.10 | -0.87 | 24.83 | 30.15 |
| 2024-12 | -2.39 | 0.23 | 0.28 | -2.67 | 13.51 | 17.35 |

**Daily quadrant fingerprint (Demeter's own counts: 804 loss-avoidance, 883 gain-sacrifice, 1022 amplified-gain, 768 amplified-loss days = 3477 days, 48.5% cash).** P(market up | invested) = 57.1% vs P(market up | cash) = 52.3% (unconditional 54.8%; our data 2012-07..2026-02: 55.0% up days). P(invested | up day) = 53.6% vs P(invested | down day) = 48.9%. The day-ahead directional edge is only ~5 points; the 31% CAGR must come from being levered on *large* up days and flat on *large* down days (Mar-Apr 2020 alone: three days at 3x = +56%). Cash spells contained more up days than down days -- consistent with staying out through the first days of a rebound.

**Volatility-implied leverage.** Monthly std 6.28% vs SPY 4.06%: if invested on a random half of days at constant L, L would be about 2.2x (all months) or 1.5x (ex Feb-Apr 2020). Together with the ~1x medians above, the invested state is a mix of ~1x and ~3x, averaging roughly 1.5-2x.

## 6. Where the losses came from (worst and best months)

Worst 12 Demeter months:

| date | Demeter | SPY | exposure | vix_start | vix_avg | VIX chg % | RV ann % |
|---|---|---|---|---|---|---|---|
| 2020-02 | -13.65 | -8.24 | 1.66 | 18.84 | 19.63 | 112.90 | 24.95 |
| 2015-06 | -10.65 | -1.94 |  | 13.84 | 14.34 | 31.72 | 11.12 |
| 2022-09 | -8.16 | -9.22 | 0.89 | 25.87 | 27.41 | 22.23 | 23.92 |
| 2025-03 | -7.55 | -5.64 | 1.34 | 19.63 | 21.84 | 13.50 | 20.71 |
| 2020-10 | -6.92 | -2.67 | 2.59 | 26.37 | 29.44 | 44.18 | 20.36 |
| 2025-02 | -6.35 | -1.31 |  | 16.43 | 17.05 | 19.48 | 13.13 |
| 2014-12 | -6.19 | -0.26 |  | 13.33 | 16.29 | 44.04 | 15.44 |
| 2023-10 | -5.74 | -2.11 | 2.72 | 17.52 | 18.89 | 3.54 | 13.98 |
| 2019-08 | -5.62 | -1.59 |  | 16.12 | 18.98 | 17.74 | 23.04 |
| 2024-10 | -4.92 | -0.92 |  | 16.73 | 19.96 | 38.43 | 11.12 |
| 2015-08 | -4.79 | -6.04 | 0.79 | 12.12 | 19.43 | 134.57 | 26.77 |
| 2026-03 | -4.74 | -4.99 | 0.95 |  |  |  |  |

Best 12 Demeter months:

| date | Demeter | SPY | exposure | vix_start | vix_avg | VIX chg % | RV ann % |
|---|---|---|---|---|---|---|---|
| 2020-03 | 55.32 | -12.36 | -4.48 | 40.11 | 57.74 | 33.48 | 89.65 |
| 2020-04 | 29.65 | 12.81 | 2.31 | 53.54 | 41.45 | -36.22 | 40.40 |
| 2020-11 | 16.87 | 10.94 | 1.54 | 38.02 | 25.00 | -45.90 | 16.25 |
| 2025-01 | 12.31 | 2.78 | 4.43 | 17.35 | 16.75 | -5.30 | 13.94 |
| 2022-07 | 10.64 | 9.21 | 1.16 | 28.71 | 24.87 | -25.71 | 19.17 |
| 2025-06 | 10.08 | 5.08 | 1.98 | 18.57 | 18.21 | -9.91 | 9.94 |
| 2022-10 | 10.04 | 8.09 | 1.24 | 31.62 | 30.01 | -18.15 | 27.89 |
| 2020-05 | 9.66 | 4.75 | 2.03 | 34.15 | 30.90 | -19.44 | 22.41 |
| 2023-01 | 9.65 | 6.28 | 1.54 | 21.67 | 20.20 | -10.48 | 16.59 |
| 2015-10 | 8.99 | 8.43 | 1.07 | 24.50 | 16.79 | -38.49 | 12.60 |
| 2024-02 | 8.88 | 5.33 | 1.67 | 14.35 | 13.94 | -6.62 | 12.14 |
| 2026-04 | 8.48 | 10.48 | 0.81 |  |  |  |  |

Eight of the twelve worst months happened with SPY down only 0.3-2.7% and month-start VIX of 13-19; in all of them the constant-leverage equivalent is 2-5x (Jun-2015 L\* 4.96, Feb-2025 3.71, Oct-2024 3.49, Aug-2019 2.60, Oct-2020 2.55, Oct-2023 2.14), i.e. the rule was 2-3x levered during the down days and, in the L\*>3 cases, *out* during some of the up days -- the classic whipsaw of a quick-exit/quick-re-entry rule in a choppy, low-vol month. By contrast the genuine crash months (Aug-2015, Oct/Dec-2018, Apr/Jun-2022, Mar-2020) were handled at 0-1x. The best months mirror this: with the exception of the 2020 rebounds they are calm months (VIX 14-21, falling) in which 3x was held on the big up days and avoided on the worst one or two days (Jan-2025 L\* 5.96: either 3x on 15-22 Jan only, or 3x all month except the 24-27 Jan DeepSeek drop; Jul/Aug-2025 L\* 3.3/4.2).

## 7. (f) Ranked rule ingredients most consistent with the record, and what the record rules out

**Six ingredients, ranked by how much of the record they explain**


**1. Fast, asymmetric de-levering on a downside volatility shock (leverage effect + volatility clustering)**

- Feb-2020: all 79 matching paths keep the strategy invested through the month at a mean 1.5-2.1x (constant-equivalent 1.72x), i.e. the two consecutive -3% days on 24-25 Feb were absorbed levered; but 3x was NOT held into the -4.5% 27-Feb day (3x through 27-Feb = -22.4%, 3x through 25-Feb then 1x = -14.1%, record -13.65%). The de-levering came one to two days after the first shock, on the second/third -3% day.
- Jan-2022: every matching path is invested 3-11 Jan and in cash 14-31 Jan (exit at the 11/13-Jan close after the -1.9% 5-Jan and -1.4% 13-Jan days; the 18-27 Jan slide of -7% was avoided). Dec-2022: never invested 15-21 Dec (post-FOMC drop). Oct-2018: never invested 5-11 Oct (the -3.2%/-2.2% days). Dec-2018: cash 3-17 Dec. Feb-2018: cash 1-7 Feb (VIX 13.5 -> 37). Counter-examples that bound the trigger: Aug-2019 held 2-3x through the -3.0% 5-Aug day in every path, and Feb-2025 is consistent with 3x for essentially the whole month (daily moves of -0.4 to -1.7% did not fire it) -- the exit needs a genuine vol shock (repeated -2/-3% days, VIX > ~25), not a single bad day.
- SPY months below -3% (n=22): median implied exposure 0.24x, Demeter beat SPY in 20 of 22, was positive in 5, fully in cash in 3. Down-capture 22.9% (36-month rolling median 34%).
- Piecewise regression ex Feb-Apr 2020: up-beta 1.01 vs down-beta 0.42; all months up-beta 1.39 vs down-beta -0.48.

**2. Re-entry driven by short-horizon mean reversion + implied-vol DISSIPATION (VIX falling from its peak / variance-risk-premium collapsing), not by a low vol level**

- Mar-2020: every minimal path is in cash 6-20 Mar and 3x on 24-26 Mar. Entering 3x at the 23-Mar close (the low: RSI(2) 8, drawdown -34%, VIX 61.6 after 5 straight declines from the 82.7 peak, VIX/SMA10 0.92, 10-day realised vol 103%) and holding gives +49%; 3x on 24-26 Mar only gives +56.1%; entering one day later gives +17%, one day earlier +38%.
- Apr-2020: 2.3x constant-equivalent with VIX between 31 and 57 and realised vol 40%; 3x from 7-Apr to month-end = +29.4% (record +29.65%); at least 14 of 21 days at 3x in every 1-switch solution. May-2020 2.1x (VIX 27-37). Nov-2020 1.5x (VIX 38 -> 21).
- Spearman correlation of implied exposure with the within-month VIX change: -0.30; with the VIX level at the start of the month: +0.03.
- Archetype check: '3x when VIX < its 10-day SMA, else cash' reproduces the 2020 signature (Feb +1.9, Mar +37.6, Apr +36.1) whereas VIX-level, realised-vol-level and 200-day-SMA gates all return ~0% in Mar and Apr 2020.

**3. Leverage tier scaled by the volatility regime: 3x in calm markets, ~1x ('sometimes unlevered') when vol is elevated, with a separate crisis-rebound mode at 2-3x**

- 2022 (VIX avg 25.6): implied exposure 0.9x (Sep), 1.16x (Jul), 1.24x (Oct), 0.95x (Nov), 1.5x (Mar); 2017 (VIX avg 11.1): median 2.2x; 2025 median 1.9x.
- VIX-average bins: mean implied exposure 1.24x below 13, 1.00x at 13-16, 1.14x at 16-20, 0.73x at 20-25, 0.69x at 25-30; the >30 bin (crisis rebounds) has median 1.64x.
- Volatility-implied leverage when invested (50% cash days): 2.2x over all months, 1.5x excluding Feb-Apr 2020.

**4. Persistence / hysteresis: once out, stay out for weeks (whole months in cash), re-enter only on confirmation**

- Three months at exactly 0.00% (Jan-2016 SPY -4.97, Apr-2022 -8.73, Jun-2022 -8.26) and Feb-2022 (+0.16 vs -3.00) are constant-cash months. Demeter's own quadrant counts: 883 'gain sacrifice' days vs 804 'loss avoidance' days -- cash spells sat through more up days than down days, so exits were not reversed on the first rebound day.
- P(market up | in cash) = 52.3% vs P(market up | invested) = 57.1%: a ~5-point directional edge only; returns come from magnitude timing, not day-ahead direction.

**5. Short-horizon (days to ~3 weeks) timing at 3x inside calm regimes -- the source of BOTH tails, including the whipsaw losses**

- 27 months have a constant-leverage equivalent above 3 or below 0 (impossible for any fixed long-only position): e.g. Jan-2025 L*=5.96 (either 3x on 15-22 Jan only, or 3x all month except the 24-27 Jan DeepSeek drop), Jul/Aug-2025 (3.3x/4.2x), Feb-2013 4.4x, Sep-2018 3.4x; and sign flips in 11 months (Feb-2018 +2.42 vs SPY -3.69: cash 1-7 Feb (or 1-12 Feb) then 2x from 8-Feb (or 1x from 13-Feb)).
- 8 of the 12 worst Demeter months occurred when SPY fell only 0.3-2.7% (Jun-2015 -10.65 vs SPY -1.94; Oct-2020 -6.92; Feb-2025 -6.35; Dec-2014 -6.19; Oct-2023 -5.74; Aug-2019 -5.62; Oct-2024 -4.92) with month-start VIX 13-19. Jun-2015 requires 3x on 1-5 Jun AND 24-30 Jun in every path, with either cash 8-23 Jun (exit after the first dip, re-enter after the recovery, get hit by the 29-Jun Greece day at 3x) or 3x nearly all month but out precisely on the 10-11 Jun up days; 3x buy-and-hold would have lost only 6.3%.
- The record's losses are therefore whipsaw losses at high leverage in choppy low-vol months, not crash losses -- the signature of a quick-exit / quick-re-entry rule.

**6. Long-or-cash only, discrete leverage {0,1,2,3}, daily decision, cash booked at 0%**

- Every month Jul-2012..Jan-2026 is reproducible with a {0,1,2,3} path and at most 2 intra-month switches (0 switches: 28 months, 1: 128, 2: 7); no shorting is needed even for Mar-2020.
- The three 0.00% months coincide with T-bill months of +0.02%, +0.06% and +0.13%: published cash months earn nothing (our engine credits T-bills; expect our cash months to print small positives).
- Lower bound on position changes: >=142 intra-month switches in 163 months (>=10.4/yr) plus month-boundary changes; the whipsaw months and the daily framing imply materially more (plausibly 30-80/yr).

**Ruled out**

1. **A slow trend filter (e.g. 200-day SMA) as the invest/cash gate.** SPX closed below its 200-day SMA on 20 of 22 trading days in Mar-2020 (all days from 5-Mar), 21 of 21 in Apr-2020, 20 of 20 in Jul-2022, 21 of 21 in Oct-2022 and 20 of 21 in Nov-2022, yet Demeter earned +55.3%, +29.7%, +10.6%, +10.0% and +5.3% in those months. A 3x-above/cash-below SMA200 rule returns -17.9%, 0.0%, 0.0%, 0.0%, 0.0%. Re-entry is fast (days), not trend-confirmed (months).

2. **Absolute volatility-LEVEL gating (invest only when VIX < X or realised vol < Y), or leverage as a monotone decreasing function of the vol level.** Apr-2020 ran 2.3x with VIX 31-57 and realised vol 40%; the 23-Mar-2020 re-entry happened at 10-day realised vol 103% and VIX 61.6. 'VIX<20', 'VIX<30', 'RV21<15/25%' gates all return ~0% in Mar and Apr 2020 (VIX<40 gate: -12%/-4%). Conversely the worst months came from low-vol starts (VIX 13-19), so a low level did not protect. Implied exposure vs month-start VIX has Spearman +0.03.

3. **Constant or monthly-set exposure (levered buy-and-hold, monthly regime allocation, or any rule that cannot change exposure within a month).** 27 months have constant-leverage equivalents >3 or <0; 11 months have the opposite sign to SPY; Mar-2020 needs >=2 intra-month switches; Feb-2020 needs 2. Monthly skew 3.9 vs SPY -0.4; up-beta 1.39 vs down-beta -0.48; convexity term t=8.0 (t=3.1 ex-2020). 3x buy-and-hold would have lost 62% peak-to-trough.

4. **(also) Un-gated 1-day mean reversion at 3x, and 'always 3x when invested'.** Pure 'long 3x after a down day' gives -29% in Feb-2020 and -36% in 2022 (record -13.65% and +19.2%); mean reversion must sit behind a vol/crash gate. 2022's invested months ran at 0.9-1.5x, so the levered tier is conditional, not constant.


## 8. Quantitative constraints a candidate rule should satisfy (targets for the rule designers)

| dimension | constraint from the record |
|---|---|
| cash share pct | 48-52% of days (Demeter: 48.5%) |
| leverage when invested | mix of 1x and 3x; vol-implied average 1.5-2.2x; ~1x when VIX 25-30, 2-3x when VIX < 16 or in a post-crash rebound |
| monthly capture targets | up-capture >= 100% (Demeter 114%), down-capture <= 40% (Demeter 23%; 12m rolling median 39%) |
| convexity targets | up-beta 1.0-1.4, down-beta <= 0.45 (ex-2020 record: 1.01 / 0.42); positive monthly skew |
| crash exit | from 2-3x to <=1x within 1-2 days after two consecutive -3% days (Feb-2020: de-lever at the 25/26-Feb close; month -13.65%, not -22%); but tolerate a single -3% day in a calm regime (Aug-2019) and -0.5 to -1.7% days at 3x (Feb-2025) |
| crash reentry | back to 2-3x within +-1 day of the low while VIX > 50 and realised vol > 80%, triggered by VIX falling from its peak + oversold (23-Mar-2020); then >=14 of 21 days at 3x in the following month with VIX 31-57 |
| grinding bear | whole months in cash when SPY falls 8% in a month with VIX 20-34 (Apr/Jun-2022) but ~1x participation in the Jul/Oct/Nov-2022 rallies while below the 200-day SMA |
| accepted pain | whipsaw months of -5% to -11% when SPY is only -0.3% to -2.7% (8 such months in 168); worst month -13.65% |
| trade count | lower bound ~10.4 intra-month switches/yr from the record; realistic 30-80/yr; hysteresis so cash spells last weeks |
| cash accounting | Demeter books cash at 0%; our engine credits T-bills (adds roughly 0.5%/yr on average over 2012-2026, more after 2022) |

Archetype fingerprint (coarse un-tuned rules run through `engine.run`, Jul-2012..Jan-2026, 2 bp costs; descriptive only -- see OOS disclosure):

| archetype | monthly corr with Demeter | corr ex Feb-Apr 2020 | same-sign months % | RMSE % | CAGR % | Sharpe | maxDD % | % cash days | changes/yr | Feb-20 | Mar-20 | Apr-20 | 2022 % |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A. 3x buy-and-hold | 0.30 | 0.69 | 78.53 | 12.10 | 34.09 | 0.87 | -62.20 | 0.00 | 0.00 | -23.31 | -46.27 | 37.59 | -55.93 |
| B. 1x buy-and-hold | 0.34 | 0.69 | 79.75 | 6.33 | 14.71 | 0.95 | -23.93 | 0.00 | 0.00 | -7.92 | -12.49 | 12.70 | -18.18 |
| C. 1-day mean reversion: 3x after a down day, cash after an up day | 0.70 | 0.57 | 76.07 | 6.33 | 14.63 | 0.55 | -53.14 | 55.75 | 127.73 | -29.02 | 43.06 | 32.55 | -35.57 |
| D. 1-day momentum: 3x after an up day, cash after a down day | -0.14 | 0.45 | 61.35 | 11.76 | 1.43 | 0.19 | -67.06 | 44.57 | 127.88 | 7.01 | -63.13 | 2.09 | -42.61 |
| E. Realised-vol gate: 3x if RV21<15%, 1x if <25%, else cash | 0.38 | 0.55 | 78.53 | 7.99 | 27.88 | 0.99 | -25.95 | 7.64 | 7.45 | -8.26 | 4.33 | 0.01 | -20.06 |
| F. VIX level gate: 3x if VIX<20 else cash | 0.29 | 0.47 | 73.01 | 9.07 | 17.41 | 0.64 | -40.11 | 24.69 | 14.76 | -0.15 | 0.03 | 0.01 | -26.55 |
| G. VIX dissipation: 3x if VIX < its 10d SMA else cash | 0.63 | 0.54 | 69.94 | 6.58 | 32.49 | 1.06 | -29.36 | 43.81 | 51.29 | 1.91 | 37.60 | 36.11 | -16.05 |
| H. 200d SMA trend: 3x above, cash below | 0.26 | 0.54 | 74.85 | 9.93 | 24.83 | 0.79 | -46.96 | 16.19 | 5.61 | -22.37 | -17.91 | 0.01 | -39.85 |
| I. Baseline volregime (trend AND vol): 3x RV<15 & trend, 1x RV<25 & trend | 0.30 | 0.47 | 74.85 | 8.29 | 23.10 | 0.86 | -30.02 | 17.36 | 9.74 | -7.88 | 0.03 | 0.01 | -16.72 |

No single archetype reproduces the record. The two with the highest monthly correlation are 1-day mean reversion (0.70, but -29% in Feb-2020 and -36% in 2022) and VIX dissipation (0.63, CAGR 32.5%, Sharpe 1.06, but max DD -29% and 51 changes/yr). Level-based gates (VIX<20, RV<15/25%, SMA200, the baseline) sit at 0.26-0.38 because they return ~0 in Mar/Apr-2020 and mis-time 2022. The record therefore points to a *composite*: a vol-shock exit (ingredient 1) protecting a mean-reversion / vol-dissipation re-entry (2), with the levered tier gated by the vol regime (3) and enough hysteresis to sit out whole months (4).

## Appendix A. Month-by-month table (implied exposure where |SPY| > 2%; VIX avg from daily data)

| date | Demeter % | SPY % | implied exp. | VIX avg | flag |
|---|---|---|---|---|---|
| 2012-07 | -0.15 | 1.13 |  | 17.57 | |SPY|<=2%: n/a |
| 2012-08 | 6.73 | 2.24 | 3.00 | 15.69 | >1.5x |
| 2012-09 | 3.50 | 2.58 | 1.36 | 15.28 |  |
| 2012-10 | -1.27 | -1.85 |  | 16.28 | |SPY|<=2%: n/a |
| 2012-11 | -2.31 | 0.57 |  | 16.70 | |SPY|<=2%: n/a |
| 2012-12 | 4.19 | 0.90 |  | 17.31 | |SPY|<=2%: n/a |
| 2013-01 | 0.16 | 5.17 | 0.03 | 13.51 | ~0 (cash-dominated) |
| 2013-02 | 4.67 | 1.35 |  | 14.07 | |SPY|<=2%: n/a |
| 2013-03 | 4.86 | 3.74 | 1.30 | 13.03 |  |
| 2013-04 | 2.70 | 1.92 |  | 13.97 | |SPY|<=2%: n/a |
| 2013-05 | 3.53 | 2.33 | 1.52 | 13.49 | >1.5x |
| 2013-06 | -3.53 | -1.35 |  | 17.27 | |SPY|<=2%: n/a |
| 2013-07 | 5.71 | 5.08 | 1.12 | 13.97 |  |
| 2013-08 | -0.90 | -2.90 | 0.31 | 14.21 |  |
| 2013-09 | 1.40 | 3.13 | 0.45 | 14.69 |  |
| 2013-10 | 2.06 | 4.59 | 0.45 | 15.41 |  |
| 2013-11 | 4.93 | 3.04 | 1.62 | 12.92 | >1.5x |
| 2013-12 | 3.37 | 2.52 | 1.34 | 14.19 |  |
| 2014-01 | 1.51 | -3.46 | -0.44 | 14.24 | SIGN FLIP (intra-month timing) |
| 2014-02 | 3.36 | 4.57 | 0.74 | 15.47 |  |
| 2014-03 | 2.78 | 0.83 |  | 14.84 | |SPY|<=2%: n/a |
| 2014-04 | 1.05 | 0.73 |  | 14.20 | |SPY|<=2%: n/a |
| 2014-05 | 3.52 | 2.34 | 1.50 | 12.48 | >1.5x |
| 2014-06 | 0.81 | 2.06 | 0.39 | 11.54 |  |
| 2014-07 | -0.08 | -1.39 |  | 12.30 | |SPY|<=2%: n/a |
| 2014-08 | 3.80 | 3.99 | 0.95 | 13.49 |  |
| 2014-09 | 2.98 | -1.41 |  | 13.47 | |SPY|<=2%: n/a |
| 2014-10 | -1.94 | 2.43 | -0.80 | 18.06 | SIGN FLIP (intra-month timing) |
| 2014-11 | 1.07 | 2.68 | 0.40 | 13.41 |  |
| 2014-12 | -6.19 | -0.26 |  | 16.29 | |SPY|<=2%: n/a |
| 2015-01 | 0.96 | -3.01 | -0.32 | 19.12 | SIGN FLIP (intra-month timing) |
| 2015-02 | 4.78 | 5.74 | 0.83 | 15.90 |  |
| 2015-03 | -0.36 | -1.59 |  | 14.81 | |SPY|<=2%: n/a |
| 2015-04 | -0.67 | 0.95 |  | 13.49 | |SPY|<=2%: n/a |
| 2015-05 | 1.21 | 1.28 |  | 13.34 | |SPY|<=2%: n/a |
| 2015-06 | -10.65 | -1.94 |  | 14.34 | |SPY|<=2%: n/a |
| 2015-07 | 4.69 | 2.09 | 2.24 | 14.35 | >1.5x |
| 2015-08 | -4.79 | -6.04 | 0.79 | 19.43 |  |
| 2015-09 | 0.61 | -2.48 | -0.25 | 24.38 | ~0 (cash-dominated) |
| 2015-10 | 8.99 | 8.43 | 1.07 | 16.79 |  |
| 2015-11 | 1.89 | 0.29 |  | 16.21 | |SPY|<=2%: n/a |
| 2015-12 | 4.28 | -1.59 |  | 18.03 | |SPY|<=2%: n/a |
| 2016-01 | 0.00 | -4.97 | -0.00 | 23.72 | FULL CASH (0.00) |
| 2016-02 | -2.35 | -0.14 |  | 22.52 | |SPY|<=2%: n/a |
| 2016-03 | 8.19 | 6.78 | 1.21 | 15.85 |  |
| 2016-04 | 0.94 | 0.38 |  | 14.30 | |SPY|<=2%: n/a |
| 2016-05 | 1.90 | 1.79 |  | 14.85 | |SPY|<=2%: n/a |
| 2016-06 | 3.92 | 0.25 |  | 17.77 | |SPY|<=2%: n/a |
| 2016-07 | 4.03 | 3.68 | 1.10 | 13.16 |  |
| 2016-08 | -0.01 | 0.13 |  | 12.40 | |SPY|<=2%: n/a |
| 2016-09 | 2.67 | 0.01 |  | 14.22 | |SPY|<=2%: n/a |
| 2016-10 | 0.59 | -1.83 |  | 14.59 | |SPY|<=2%: n/a |
| 2016-11 | 2.76 | 3.70 | 0.75 | 15.24 |  |
| 2016-12 | -2.18 | 1.97 |  | 12.47 | |SPY|<=2%: n/a |
| 2017-01 | 3.24 | 1.89 |  | 11.61 | |SPY|<=2%: n/a |
| 2017-02 | 0.75 | 3.96 | 0.19 | 11.53 | ~0 (cash-dominated) |
| 2017-03 | 0.52 | 0.11 |  | 11.90 | |SPY|<=2%: n/a |
| 2017-04 | 2.52 | 1.02 |  | 13.14 | |SPY|<=2%: n/a |
| 2017-05 | 2.37 | 1.40 |  | 10.86 | |SPY|<=2%: n/a |
| 2017-06 | -2.16 | 0.62 |  | 10.51 | |SPY|<=2%: n/a |
| 2017-07 | 4.26 | 2.05 | 2.08 | 10.26 | >1.5x |
| 2017-08 | 0.22 | 0.30 |  | 11.98 | |SPY|<=2%: n/a |
| 2017-09 | 4.57 | 2.06 | 2.22 | 10.44 | >1.5x |
| 2017-10 | 5.63 | 2.33 | 2.42 | 10.13 | >1.5x |
| 2017-11 | 6.74 | 3.06 | 2.20 | 10.54 | >1.5x |
| 2017-12 | 0.76 | 1.10 |  | 10.26 | |SPY|<=2%: n/a |
| 2018-01 | 5.26 | 5.72 | 0.92 | 11.06 |  |
| 2018-02 | 2.42 | -3.69 | -0.66 | 22.46 | SIGN FLIP (intra-month timing) |
| 2018-03 | -0.68 | -2.55 | 0.27 | 19.02 |  |
| 2018-04 | 5.69 | 0.38 |  | 18.27 | |SPY|<=2%: n/a |
| 2018-05 | 4.24 | 2.40 | 1.77 | 14.12 | >1.5x |
| 2018-06 | -0.79 | 0.61 |  | 13.68 | |SPY|<=2%: n/a |
| 2018-07 | 1.19 | 3.71 | 0.32 | 13.15 |  |
| 2018-08 | 3.08 | 3.25 | 0.95 | 12.55 |  |
| 2018-09 | 1.40 | 0.56 |  | 12.91 | |SPY|<=2%: n/a |
| 2018-10 | -0.76 | -6.84 | 0.11 | 19.35 | ~0 (cash-dominated) |
| 2018-11 | 2.08 | 2.03 | 1.02 | 19.39 |  |
| 2018-12 | -1.63 | -9.04 | 0.18 | 24.95 | ~0 (cash-dominated) |
| 2019-01 | 7.65 | 8.01 | 0.96 | 19.57 |  |
| 2019-02 | 3.59 | 3.20 | 1.12 | 15.23 |  |
| 2019-03 | 1.21 | 1.94 |  | 14.49 | |SPY|<=2%: n/a |
| 2019-04 | 1.90 | 4.04 | 0.47 | 12.95 |  |
| 2019-05 | -3.89 | -6.36 | 0.61 | 16.72 |  |
| 2019-06 | 4.75 | 7.04 | 0.67 | 15.84 |  |
| 2019-07 | 0.37 | 1.43 |  | 13.31 | |SPY|<=2%: n/a |
| 2019-08 | -5.62 | -1.59 |  | 18.98 | |SPY|<=2%: n/a |
| 2019-09 | 3.07 | 1.86 |  | 15.56 | |SPY|<=2%: n/a |
| 2019-10 | 4.56 | 2.16 | 2.11 | 15.47 | >1.5x |
| 2019-11 | 0.04 | 3.62 | 0.01 | 12.52 | ~0 (cash-dominated) |
| 2019-12 | -0.97 | 3.01 | -0.32 | 13.76 | SIGN FLIP (intra-month timing) |
| 2020-01 | 2.81 | -0.05 |  | 13.94 | |SPY|<=2%: n/a |
| 2020-02 | -13.65 | -8.24 | 1.66 | 19.63 | >1.5x |
| 2020-03 | 55.32 | -12.36 | -4.48 | 57.74 | SIGN FLIP (intra-month timing) |
| 2020-04 | 29.65 | 12.81 | 2.31 | 41.45 | >1.5x |
| 2020-05 | 9.66 | 4.75 | 2.03 | 30.90 | >1.5x |
| 2020-06 | 2.15 | 1.98 |  | 31.12 | |SPY|<=2%: n/a |
| 2020-07 | 4.41 | 5.63 | 0.78 | 26.84 |  |
| 2020-08 | 7.44 | 7.18 | 1.04 | 22.89 |  |
| 2020-09 | 3.42 | -3.81 | -0.90 | 27.65 | SIGN FLIP (intra-month timing) |
| 2020-10 | -6.92 | -2.67 | 2.59 | 29.44 | >1.5x |
| 2020-11 | 16.87 | 10.94 | 1.54 | 25.00 | >1.5x |
| 2020-12 | 4.91 | 3.84 | 1.28 | 22.37 |  |
| 2021-01 | 0.26 | -1.02 |  | 24.91 | |SPY|<=2%: n/a |
| 2021-02 | 4.16 | 2.78 | 1.50 | 23.14 |  |
| 2021-03 | 3.61 | 4.37 | 0.83 | 21.84 |  |
| 2021-04 | 6.88 | 5.33 | 1.29 | 17.42 |  |
| 2021-05 | 0.36 | 0.69 |  | 19.76 | |SPY|<=2%: n/a |
| 2021-06 | 4.25 | 2.33 | 1.82 | 16.96 | >1.5x |
| 2021-07 | -1.55 | 2.37 | -0.65 | 17.60 | SIGN FLIP (intra-month timing) |
| 2021-08 | 3.52 | 3.03 | 1.16 | 17.47 |  |
| 2021-09 | -1.37 | -4.66 | 0.29 | 19.82 |  |
| 2021-10 | 8.46 | 7.00 | 1.21 | 17.87 |  |
| 2021-11 | 3.45 | -0.70 |  | 18.50 | |SPY|<=2%: n/a |
| 2021-12 | 3.30 | 4.47 | 0.74 | 21.35 |  |
| 2022-01 | -2.48 | -5.18 | 0.48 | 23.18 |  |
| 2022-02 | 0.16 | -3.00 | -0.05 | 25.75 | ~0 (cash-dominated) |
| 2022-03 | 5.54 | 3.70 | 1.50 | 26.97 |  |
| 2022-04 | 0.00 | -8.73 | -0.00 | 24.37 | FULL CASH (0.00) |
| 2022-05 | 0.71 | 0.18 |  | 29.45 | |SPY|<=2%: n/a |
| 2022-06 | 0.00 | -8.26 | -0.00 | 28.10 | FULL CASH (0.00) |
| 2022-07 | 10.64 | 9.21 | 1.16 | 24.87 |  |
| 2022-08 | -0.41 | -4.09 | 0.10 | 22.17 | ~0 (cash-dominated) |
| 2022-09 | -8.16 | -9.22 | 0.89 | 27.41 |  |
| 2022-10 | 10.04 | 8.09 | 1.24 | 30.01 |  |
| 2022-11 | 5.28 | 5.58 | 0.95 | 23.44 |  |
| 2022-12 | -2.03 | -5.77 | 0.35 | 21.78 |  |
| 2023-01 | 9.65 | 6.28 | 1.54 | 20.20 | >1.5x |
| 2023-02 | -2.44 | -2.45 | 1.00 | 20.06 |  |
| 2023-03 | 5.51 | 3.66 | 1.51 | 21.64 | >1.5x |
| 2023-04 | 1.06 | 1.55 |  | 17.82 | |SPY|<=2%: n/a |
| 2023-05 | 0.84 | 0.43 |  | 17.64 | |SPY|<=2%: n/a |
| 2023-06 | 7.54 | 6.60 | 1.14 | 13.99 |  |
| 2023-07 | 2.21 | 3.20 | 0.69 | 13.94 |  |
| 2023-08 | 1.14 | -1.60 |  | 15.85 | |SPY|<=2%: n/a |
| 2023-09 | -2.25 | -4.77 | 0.47 | 15.24 |  |
| 2023-10 | -5.74 | -2.11 | 2.72 | 18.89 | >1.5x |
| 2023-11 | 4.31 | 9.12 | 0.47 | 14.08 |  |
| 2023-12 | 1.98 | 4.54 | 0.44 | 12.72 |  |
| 2024-01 | -2.91 | 1.67 |  | 13.40 | |SPY|<=2%: n/a |
| 2024-02 | 8.88 | 5.33 | 1.67 | 13.94 | >1.5x |
| 2024-03 | 1.42 | 3.21 | 0.44 | 13.79 |  |
| 2024-04 | -1.98 | -4.09 | 0.48 | 16.14 |  |
| 2024-05 | 5.91 | 4.95 | 1.19 | 13.09 |  |
| 2024-06 | 7.13 | 3.58 | 1.99 | 12.68 | >1.5x |
| 2024-07 | -1.89 | 1.21 |  | 14.47 | |SPY|<=2%: n/a |
| 2024-08 | 8.40 | 2.42 | 3.47 | 19.31 | >1.5x |
| 2024-09 | 0.08 | 2.13 | 0.04 | 17.77 | ~0 (cash-dominated) |
| 2024-10 | -4.92 | -0.92 |  | 19.96 | |SPY|<=2%: n/a |
| 2024-11 | 1.21 | 5.86 | 0.21 | 16.12 | ~0 (cash-dominated) |
| 2024-12 | 0.23 | -2.39 | -0.10 | 15.87 | ~0 (cash-dominated) |
| 2025-01 | 12.31 | 2.78 | 4.43 | 16.75 | >1.5x |
| 2025-02 | -6.35 | -1.31 |  | 17.05 | |SPY|<=2%: n/a |
| 2025-03 | -7.55 | -5.64 | 1.34 | 21.84 |  |
| 2025-04 | 4.94 | -0.69 |  | 31.97 | |SPY|<=2%: n/a |
| 2025-05 | 4.11 | 6.29 | 0.65 | 20.46 |  |
| 2025-06 | 10.08 | 5.08 | 1.98 | 18.21 | >1.5x |
| 2025-07 | 6.42 | 2.24 | 2.87 | 16.33 | >1.5x |
| 2025-08 | 6.46 | 2.02 | 3.20 | 15.75 | >1.5x |
| 2025-09 | 4.87 | 3.64 | 1.34 | 15.77 |  |
| 2025-10 | 4.19 | 2.33 | 1.80 | 18.09 | >1.5x |
| 2025-11 | -2.80 | 0.24 |  | 19.90 | |SPY|<=2%: n/a |
| 2025-12 | 1.10 | 0.05 |  | 15.55 | |SPY|<=2%: n/a |
| 2026-01 | -2.75 | 1.44 |  | 16.05 | |SPY|<=2%: n/a |
| 2026-02 | 0.99 | -0.77 |  | 18.16 | |SPY|<=2%: n/a |
| 2026-03 | -4.74 | -4.99 | 0.95 |  |  |
| 2026-04 | 8.48 | 10.48 | 0.81 |  |  |
| 2026-05 | 4.73 | 5.26 | 0.90 |  |  |
| 2026-06 | -0.17 | -0.96 |  |  | |SPY|<=2%: n/a |

## Appendix B. Daily detail, Feb / Mar / Apr 2020 (`3x day ret` = 3 x excess return that day)

**February 2020**

| date | SPY ret % | cum SPY % | VIX | 3x day ret % |
|---|---|---|---|---|
| 2020-02-03 | 0.74 | 0.74 | 17.97 | 2.21 |
| 2020-02-04 | 1.52 | 2.28 | 16.05 | 4.55 |
| 2020-02-05 | 1.15 | 3.46 | 15.15 | 3.45 |
| 2020-02-06 | 0.34 | 3.81 | 14.96 | 0.99 |
| 2020-02-07 | -0.53 | 3.25 | 15.47 | -1.62 |
| 2020-02-10 | 0.75 | 4.03 | 15.04 | 2.22 |
| 2020-02-11 | 0.17 | 4.21 | 15.18 | 0.50 |
| 2020-02-12 | 0.64 | 4.88 | 13.74 | 1.91 |
| 2020-02-13 | -0.11 | 4.76 | 14.15 | -0.34 |
| 2020-02-14 | 0.16 | 4.93 | 13.68 | 0.46 |
| 2020-02-18 | -0.26 | 4.66 | 14.83 | -0.79 |
| 2020-02-19 | 0.48 | 5.16 | 14.38 | 1.42 |
| 2020-02-20 | -0.41 | 4.73 | 15.56 | -1.25 |
| 2020-02-21 | -1.03 | 3.65 | 17.08 | -3.11 |
| 2020-02-24 | -3.32 | 0.21 | 25.03 | -9.97 |
| 2020-02-25 | -3.03 | -2.82 | 27.85 | -9.11 |
| 2020-02-26 | -0.37 | -3.18 | 27.56 | -1.12 |
| 2020-02-27 | -4.49 | -7.53 | 39.16 | -13.49 |
| 2020-02-28 | -0.42 | -7.92 | 40.11 | -1.28 |

**March 2020**

| date | SPY ret % | cum SPY % | VIX | 3x day ret % |
|---|---|---|---|---|
| 2020-03-02 | 4.33 | 4.33 | 33.42 | 12.98 |
| 2020-03-03 | -2.86 | 1.34 | 36.82 | -8.60 |
| 2020-03-04 | 4.20 | 5.60 | 31.99 | 12.60 |
| 2020-03-05 | -3.32 | 2.09 | 39.62 | -9.98 |
| 2020-03-06 | -1.65 | 0.40 | 41.94 | -4.96 |
| 2020-03-09 | -7.81 | -7.44 | 54.46 | -23.43 |
| 2020-03-10 | 5.17 | -2.65 | 47.30 | 15.52 |
| 2020-03-11 | -4.87 | -7.39 | 53.90 | -14.63 |
| 2020-03-12 | -9.57 | -16.25 | 75.47 | -28.71 |
| 2020-03-13 | 8.55 | -9.09 | 57.83 | 25.64 |
| 2020-03-16 | -10.94 | -19.04 | 82.69 | -32.83 |
| 2020-03-17 | 5.40 | -14.67 | 75.91 | 16.20 |
| 2020-03-18 | -5.06 | -18.99 | 76.45 | -15.19 |
| 2020-03-19 | 0.21 | -18.82 | 72.00 | 0.64 |
| 2020-03-20 | -4.31 | -22.32 | 66.04 | -12.93 |
| 2020-03-23 | -2.56 | -24.30 | 61.59 | -7.67 |
| 2020-03-24 | 9.06 | -17.44 | 61.67 | 27.18 |
| 2020-03-25 | 1.50 | -16.21 | 63.95 | 4.49 |
| 2020-03-26 | 5.84 | -11.32 | 61.00 | 17.52 |
| 2020-03-27 | -2.98 | -13.96 | 65.54 | -8.94 |
| 2020-03-30 | 3.25 | -11.16 | 57.08 | 9.74 |
| 2020-03-31 | -1.49 | -12.49 | 53.54 | -4.47 |

**April 2020**

| date | SPY ret % | cum SPY % | VIX | 3x day ret % |
|---|---|---|---|---|
| 2020-04-01 | -4.50 | -4.50 | 57.06 | -13.50 |
| 2020-04-02 | 2.31 | -2.30 | 50.91 | 6.92 |
| 2020-04-03 | -1.45 | -3.71 | 46.80 | -4.34 |
| 2020-04-06 | 6.72 | 2.76 | 45.24 | 20.15 |
| 2020-04-07 | 0.10 | 2.86 | 46.70 | 0.30 |
| 2020-04-08 | 3.36 | 6.32 | 43.35 | 10.07 |
| 2020-04-09 | 1.52 | 7.93 | 41.67 | 4.56 |
| 2020-04-13 | -0.91 | 6.95 | 41.17 | -2.74 |
| 2020-04-14 | 2.95 | 10.10 | 37.76 | 8.85 |
| 2020-04-15 | -2.12 | 7.76 | 40.84 | -6.38 |
| 2020-04-16 | 0.48 | 8.28 | 40.11 | 1.45 |
| 2020-04-17 | 2.70 | 11.21 | 38.15 | 8.10 |
| 2020-04-20 | -1.76 | 9.25 | 43.83 | -5.29 |
| 2020-04-21 | -3.04 | 5.93 | 45.41 | -9.11 |
| 2020-04-22 | 2.22 | 8.28 | 41.98 | 6.66 |
| 2020-04-23 | -0.01 | 8.28 | 41.38 | -0.02 |
| 2020-04-24 | 1.39 | 9.78 | 35.93 | 4.18 |
| 2020-04-27 | 1.44 | 11.37 | 33.29 | 4.32 |
| 2020-04-28 | -0.46 | 10.86 | 33.57 | -1.38 |
| 2020-04-29 | 2.62 | 13.76 | 31.23 | 7.85 |
| 2020-04-30 | -0.93 | 12.70 | 34.15 | -2.79 |
