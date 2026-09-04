# Nifty Midcap Select — dual-engine feasibility study

Can the Demeter dual-engine architecture be run on Indian midcaps, and what is the cheapest way to hold
the exposure? Companion to `../model` (the US replication study).

## Answer in one paragraph

The timing engine does not transfer: on Nifty Midcap Select (Sep 2021 – Aug 2026) the US model returns
8.4% a year net against 14.2% for simply staying invested, with twice the drawdown, and re-tuning it for
Indian volatility does not rescue it. What does transfer is the cost arithmetic. Because securities
transaction tax and exchange charges fall on **notional** for futures but on **premium** for options,
holding MIDCPNIFTY through an at-the-money option synthetic (long call + short put, same strike) costs
**1.18% a year at 1× exposure against 2.52% through futures** — a saving of 1.34% at 1× and 2.68% at 2×
that requires no forecasting skill. Deep in-the-money selling does the opposite: premium approaches
notional, so it costs 5.11% a year, roughly double the futures it was meant to replace.

## The model

`india_model.py` builds and tests the recommended strategy. Chosen on Nifty Midcap 50, May 2014 – Dec 2019;
tested on Midcap 50 from 2020 and Midcap Select from Sep 2021.

**Hold 0.75x Nifty Midcap Select as an at-the-money option synthetic, and sell a 6% out-of-the-money call
against it every month. Do not time the market.**

Out of sample on Midcap Select (Sep 2021 – Aug 2026), against the same index held 1x through futures:

| | Model | Futures buy & hold |
|---|---|---|
| Annualised return | **16.85%** | 13.97% |
| Volatility | **14.2%** | 18.6% |
| Sharpe | **0.75** | 0.48 |
| Maximum drawdown | **-13.66%** | -25.44% |
| Calmar | **1.23** | 0.55 |
| Exposure changes a year | 0.2 | 0 |

Attribution: the synthetic wrapper is worth +1.59% a year, the covered-call overlay +4.59%, and cutting
exposure to 0.75x costs -3.30% of return while halving the drawdown.

**The load-bearing assumption** is that midcap implied volatility is about 1.35x India VIX (the ratio of
their realised volatilities). At 1.0x the overlay contributes nothing and the model underperforms plain
synthetic buy-and-hold. One day of MIDCPNIFTY option quotes settles it — see the model report.

## Files

| Path | What it is |
|---|---|
| `data/build_india_dataset.py` → `india_daily.csv` | Nifty Midcap Select, Midcap 50/100/150, Nifty 50, India VIX, Nifty 1D Rate Index (the cash engine) and the Nifty 50 Futures Index, joined on NSE trading days from Feb 2012. The futures index is used to *measure* the carry a futures holder receives rather than assume a dividend yield. |
| `costs.py` | The Indian derivative cost model: statutory rates in force from 1 April 2026, Black-Scholes pricing, and cost per unit of delta exposure for futures and ten option structures. `python3 costs.py` prints the tables. |
| `run_india.py` | The US-frozen model applied unchanged to Indian indices — a genuine out-of-sample test in a different market. |
| `tune_india.py` | India-specific re-tuning of the same family (development: Midcap 50, 2012–2019). |
| `crash_overlay.py` | The opposite posture: always invested, volatility-sized, crash exits only. |
| `explore_core.py` | Seven timing families tested on the Indian development window. All seven reduced the Sharpe ratio versus staying invested. |
| `vrp_overlay.py` | Measures India's variance risk premium (India VIX against subsequent realised volatility) and simulates monthly option-selling overlays settled on the actual index path. |
| `india_model.py` | The model: development selection including constant-leverage variants, out-of-sample tests, and the implied-volatility sensitivity. |
| `build_india_report.py` + `report/` | The feasibility study page (cost arithmetic, why timing fails). |
| `build_model_report.py` + `model_report/` | The model specification page. |

## Key numbers

| Holding 1× MIDCPNIFTY exposure for a year | Cost |
|---|---|
| Futures, twelve monthly rolls | 2.52% |
| 30-day at-the-money synthetic, twelve rolls | 1.18% |
| 90-day synthetic, four rolls (liquidity permitting) | 1.05% |
| 10% in-the-money structure | 5.11% |

All costs include the full statutory stack (STT 0.05% on futures notional / 0.15% on option premium from
1 April 2026, exchange charges, stamp duty, SEBI fee, GST, brokerage) plus assumed bid-ask spreads, times
a 1.5 margin of safety.

Hedging midcap with Nifty options removes only ~42% of the position's volatility, and midcap beta to Nifty
rises from 1.10 to 1.27 on Nifty-down days, so a full-sample-beta hedge under-protects in stress.

## Constraints the design must respect

* MIDCPNIFTY weekly expiries were withdrawn from 20 November 2024 — monthly only, last Tuesday.
* Contract sizes were raised to roughly ₹15–20 lakh.
* An in-the-money option allowed to expire attracts 0.125% STT on its full intrinsic settlement value:
  always square off, never exercise.
