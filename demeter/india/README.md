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

## Files

| Path | What it is |
|---|---|
| `data/build_india_dataset.py` → `india_daily.csv` | Nifty Midcap Select, Midcap 50/100/150, Nifty 50, India VIX, Nifty 1D Rate Index (the cash engine) and the Nifty 50 Futures Index, joined on NSE trading days from Feb 2012. The futures index is used to *measure* the carry a futures holder receives rather than assume a dividend yield. |
| `costs.py` | The Indian derivative cost model: statutory rates in force from 1 April 2026, Black-Scholes pricing, and cost per unit of delta exposure for futures and ten option structures. `python3 costs.py` prints the tables. |
| `run_india.py` | The US-frozen model applied unchanged to Indian indices — a genuine out-of-sample test in a different market. |
| `tune_india.py` | India-specific re-tuning of the same family (development: Midcap 50, 2012–2019). |
| `crash_overlay.py` | The opposite posture: always invested, volatility-sized, crash exits only. |
| `build_india_report.py` + `report/` | The interactive study page. |

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
