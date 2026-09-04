# Can a rules-based dual-engine model reproduce Demeter's record?

**Short answer: no.** The recommended model returns **17.59% a year** out of sample
(Jul 2012 – Jan 2026) with a **-20.17% drawdown** and about **9 position
changes a year**. Demeter's published record over the same window is **31.33% at -13.65%**,
rebalanced daily. The gap is roughly 13.74% of annual return and
7 points of drawdown.

The interactive version of this note, with charts, is `report/index.html` (built by `build_report.py`).

## Method

* **Signal contract.** A model maps daily market data to a target leverage in [0, 3] for the next session.
  0 is the cash engine earning the 3-month T-bill; 3 is three times the S&P 500 total return over the T-bill.
* **Causality is tested, not assumed.** Every model is re-run on truncated histories at five cut-off dates
  (`engine.lookahead_check`); a model whose signal changes is rejected. All six candidates pass.
* **Development vs out-of-sample.** Parameters were chosen on data ending **30 June 2012**, checked for a plateau
  against the longer 1950–2012 sample, then frozen. Out-of-sample results were computed once per model.
* **Costs.** 2 bp of notional per unit of leverage traded; financing sensitivity to 50 bp a year on borrowed
  exposure. Cash earns the actual T-bill rate — Demeter books cash at 0%.
* **Data.** 35,289 daily rows, 1885-03-20 to
  2026-02-11; see `data/PROVENANCE.md`.

## The central finding: the rule that only works after 2012

The best-fitting archetype for Demeter's record is "hold 3× while VIX is below its 10-day average, else cash".

| Window | Annualised | Sharpe | Max drawdown |
|---|---|---|---|
| Development 1990 – Jun 2012 | -5.68% | -0.25 | -92.3% |
| Out of sample Jul 2012 – 2026 | 18.29% | 0.74 | -34.0% |
| Full history 1990 – 2026 | 4.13% | 0.09 | -92.3% |

Buying when implied volatility has just fallen is buying after up days: a tailwind in a fourteen-year bull market,
a whipsaw machine through 2000–02 and 2008. A study that began its backtest in 2012 would have shipped this model.

## Leaderboard

| Candidate | Family | OOS annualised | OOS Sharpe | OOS max DD | Changes/yr | DEV annualised | DEV Sharpe | DEV max DD | Corr. with Demeter |
|---|---|---|---|---|---|---|---|---|---|
| baseline volregime | volatility-regime + trend (reference baseline) | 22.89% | 0.87 | -30.0% | 10.1 | 10.75% | 0.41 | -37.6% | 0.30 |
| **final model fewtrades** | trend hysteresis + volatility tier, weekly decisions (low turnover) | 17.59% | 0.76 | -20.2% | 9.2 | 10.71% | 0.45 | -24.5% | 0.38 |
| trend vol fewtrades | trend + volatility tier, deliberately low turnover | 19.16% | 0.75 | -31.7% | 11.0 | 9.66% | 0.37 | -36.1% | 0.34 |
| vix dissipation | implied-volatility dissipation + volatility-regime leverage tier | 18.29% | 0.74 | -34.0% | 43.2 | -5.68% | -0.25 | -92.3% | 0.43 |
| final model | trend hysteresis + volatility-tiered leverage + shock override | 16.57% | 0.68 | -34.2% | 11.7 | 10.23% | 0.40 | -28.6% | 0.26 |
| shock reentry | volatility-shock exit + mean-reversion re-entry | 17.24% | 0.63 | -43.7% | 21.3 | -3.68% | -0.14 | -80.9% | 0.43 |
| *Demeter (published)* | the target | 31.33% | 1.27 | -13.7% | daily | — | — | — | 1.00 |
| *SPY buy & hold* | passive reference | 14.71% | 0.95 | -23.9% | 0 | — | — | — | — |

Note that SPY's own Sharpe over this window (0.95) exceeds every model's. The models add return
through leverage, not through a better risk-adjusted profile.

## The recommended model — `signals/final_model_fewtrades.py`

1. **Trend hysteresis.** Enter above the 100-day average; exit below the 200-day average; in between, hold.
2. **Shock override.** Force cash for 5 sessions after any daily loss worse than three trailing standard deviations.
3. **Volatility tier.** While invested: 3× below 10% realised volatility, 2× below 15%, otherwise 1×.
4. **Weekly, sticky decisions.** The level is read on the last trading day of each week and held at least 20 sessions.

Parameters: `ma_fast=100, ma_slow=200, rv_lo=0.1, rv_hi=0.15, min_days=20, shock_days=5` (plus a fixed `shock_z=3.0`).

### Head to head, Jul 2012 – Jan 2026

| | Recommended | Daily variant | Demeter | SPY |
|---|---|---|---|---|
| Annualised return | 17.59% | 16.57% | 31.33% | 14.71% |
| Annualised std. dev. | 0.22 | 0.25 | 0.22 | 0.14 |
| Sharpe | 0.76 | 0.68 | 1.27 | 0.95 |
| Sortino | 1.23 | 1.11 | 3.59 | 1.51 |
| Calmar | 0.87 | 0.48 | 2.30 | 0.61 |
| Maximum drawdown | -20.17% | -34.19% | -13.65% | -23.93% |
| % positive months | 67.68% | 64.02% | 72.39% | 71.17% |
| Beta to SPY | 1.04 | 1.23 | 0.54 | 1.00 |
| Correlation to SPY | 0.64 | 0.69 | 0.34 | 1.00 |
| Up capture | 133.14% | 142.13% | 113.59% | 100.00% |
| Down capture | 145.81% | 169.63% | 22.87% | 100.00% |
| Growth of $1,000 | $9,153 | $8,132 | $40,523 | $6,449 |

The shortfall is entirely on the downside: up-capture 133% against Demeter's
114%, but down-capture **146% against 23%**.

### Calendar years

| Year | Model | Demeter | SPY |
|---|---|---|---|
| 2012 | 0.95% | 10.84% | 5.64% |
| 2013 | 72.26% | 32.60% | 32.27% |
| 2014 | 9.13% | 12.93% | 13.58% |
| 2015 | -11.52% | 9.95% | 1.30% |
| 2016 | 27.18% | 21.94% | 11.87% |
| 2017 | 46.78% | 33.27% | 21.74% |
| 2018 | 9.28% | 23.35% | -4.47% |
| 2019 | 33.37% | 17.10% | 31.37% |
| 2020 | -1.75% | 165.14% | 18.27% |
| 2021 | 51.00% | 40.97% | 28.62% |
| 2022 | -15.06% | 19.24% | -18.19% |
| 2023 | 0.69% | 25.33% | 26.17% |
| 2024 | 36.23% | 22.41% | 24.90% |
| 2025 | 13.32% | 42.26% | 17.78% |
| 2026 | 2.58% | -2.75% | 1.44% |

### The months that define the record

| Month | SPY | Demeter | Model |
|---|---|---|---|
| 2020-02 | -8.24% | -13.65% | -15.75% |
| 2020-03 | -12.36% | 55.32% | 8.64% |
| 2020-04 | 12.81% | 29.65% | 0.01% |
| 2022-04 | -8.73% | 0.00% | -9.05% |
| 2022-06 | -8.26% | 0.00% | 0.12% |
| 2022-10 | 8.09% | 10.04% | 0.31% |
| 2018-12 | -9.04% | -1.63% | 0.18% |
| 2015-08 | -6.04% | -4.79% | -15.15% |

March 2020 is the whole story: a trend gate cannot be levered long in a month when the index spends every session
below its 200-day average, and a volatility tier cannot lever into 80% realised volatility.

### Across eras (same frozen parameters)

| Period | Model | SPY | Model Sharpe | SPY Sharpe | Model max DD | SPY max DD | Changes/yr |
|---|---|---|---|---|---|---|---|
| 1950–1989 | 19.82% | 12.40% | 0.65 | 0.52 | -32.2% | -42.7% | 5.7 |
| 1990–2011 | 10.88% | 8.09% | 0.46 | 0.36 | -24.5% | -50.8% | 7.1 |
| 2012–2019 | 22.46% | 14.43% | 1.01 | 1.24 | -19.9% | -13.5% | 9.1 |
| 2020–2026 | 11.93% | 14.85% | 0.48 | 0.75 | -20.2% | -23.9% | 9.4 |
| 2012–2026 | 17.59% | 14.62% | 0.76 | 0.94 | -20.2% | -23.9% | 9.2 |

## Sensitivity

| Cost (bp) | Financing (bp p.a.) | Annualised | Sharpe | Max drawdown |
|---|---|---|---|---|
| 0 | 0 | 17.87% | 0.78 | -20.0% |
| 0 | 50 | 17.31% | 0.75 | -20.2% |
| 1 | 0 | 17.73% | 0.77 | -20.1% |
| 1 | 50 | 17.17% | 0.75 | -20.3% |
| 2 | 0 | 17.59% | 0.76 | -20.2% |
| 2 | 50 | 17.03% | 0.74 | -20.4% |
| 5 | 0 | 17.16% | 0.75 | -20.5% |
| 5 | 50 | 16.60% | 0.73 | -20.7% |
| 10 | 0 | 16.45% | 0.72 | -21.1% |
| 10 | 50 | 15.90% | 0.70 | -21.3% |

| Variant | Annualised | Sharpe | Max drawdown |
|---|---|---|---|
| Out-of-sample from 2005 (includes 2008) | 11.24% | 0.50 | -34.2% |
| 40 bp financing spread | 16.04% | 0.66 | -34.8% |
| Traded on E-mini S&P futures (to Mar 2024) | 18.28% | 0.76 | -29.5% |
| Traded on NASDAQ-100 futures (to Mar 2024) | 30.99% | 0.97 | -32.5% |

## Limitations

* Six models were built and each evaluated out of sample: the best of six flatters itself even with frozen parameters.
* The design process saw Demeter's published record, which covers the out-of-sample window — no parameter was fitted
  to it, but the choice of ingredients was informed by it.
* One market, one fourteen-year regime. The 2005-start variant is the closest thing here to an independent stress test
  and it returns materially less.
* Costs are modelled, not measured: no slippage on gap days, no margin mechanics at 3× leverage, no roll or tax effects.
* Demeter's returns are as published by the manager, not audited. The manager's four-quadrant day counts sum to 3,477
  against a stated total of 3,219.
* The last 35 daily rows are extrapolated, the T-bill is held flat after 2025-12-19, and futures data ends 2024-03-28.

## Next steps that would actually move the answer

1. Intraday and options data — the re-entry that produced March 2020 happened within a day of the low; daily closes
   cannot see it. VIX futures term structure and the variance risk premium are the obvious next inputs.
2. A walk-forward across 1950–2012 with re-selection every decade, plus a forward paper-traded period.
3. A crash exit triggered by consecutive multi-sigma days plus an implied-volatility jump, rather than a trailing
   volatility threshold — that is the mechanism separating the model's 146% down-capture
   from Demeter's 23%.
