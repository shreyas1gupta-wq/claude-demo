# Demeter Dual-Engine — overview and replication study

Research package on Demeter Tactical Investments' *Dual-Engine Quantitative Equity Strategy* (levered long
S&P 500 / NASDAQ futures **or** cash, rebalanced daily at 3:59 PM NY, live since July 2012).

## Layout

| Path | What it is |
|---|---|
| `data/monthly_returns.csv` | The 168 published monthly returns (Jul 2012 – Jun 2026) for the strategy (Share Class B) and SPY, transcribed from the factsheet tables. Every published year-to-date figure is reproduced within 0.02 pp. |
| `data/stated_figures.json` | The factsheet's statistics table (four windows × strategy / SPY / S&P 500 price), quadrant day counts and strategy facts, as published. |
| `data/tb3ms_monthly.csv` | 3-month T-bill proxy for FRED TB3MS (monthly mean of daily rates), used for Sharpe / Sortino. |
| `build_analytics.py` → `analytics.json` | Recomputes growth, drawdowns, calendar years, rolling windows, capture ratios, distributions and reconciles 144 published statistics (142 within tolerance; the 2 misses are rounding drift on SPY total growth). |
| `build_overview.py` + `overview/template.html` → `overview/index.html` | The interactive overview page (charts + tables, light/dark). `python3 build_overview.py [--model-url URL]`. |
| `build_workbook.py` → `Demeter_Dual_Engine_Overview.xlsx` | Excel export: monthly returns, year × month matrix, calendar years, statistics by window, drawdowns, best/worst months, quadrants, growth series with native charts. |
| `model/` | Replication study: `data/` (market dataset + provenance), `engine.py` (dual-engine backtest engine), `features.py` (causal features), `evaluate.py` (standardised evaluator), `signals/` (six candidate models), `results/` (evaluation JSONs + the Demeter inference report), `RESULTS.md` (research note), `build_report.py` + `report/` (interactive study page). |

## Regenerating

```bash
cd demeter
python3 build_analytics.py          # -> analytics.json, data/tb3ms_monthly.csv
python3 build_overview.py           # -> overview/index.html
python3 build_workbook.py           # -> Demeter_Dual_Engine_Overview.xlsx
cd model/data && python3 build_dataset.py   # -> market_daily.csv (from raw/ mirrors; see PROVENANCE.md)
cd .. && python3 evaluate.py signals/final_model_fewtrades.py   # -> results/<model>.json
python3 build_report.py             # -> report/index.html, RESULTS.md figures
```

Python 3.11 with pandas, numpy (and scikit-learn / statsmodels / hmmlearn for the statistical models).

## Data caveats

* Market data comes from GitHub / PyPI mirrors of Yahoo, FRED, CBOE and CME sources because the primary hosts
  were unreachable from the build environment; see `model/data/PROVENANCE.md` for coverage, checks and gaps
  (daily S&P 500 data ends 2026-02-11, so model-versus-Demeter comparisons use Jul 2012 – Jan 2026).
* The factsheet quotes 3,219 trading days for its four-quadrant analysis while the four quadrant counts sum to
  3,477; both figures are preserved and flagged.

## Headline result of the replication study

The recommended model (`model/signals/final_model_fewtrades.py`: trend hysteresis, volatility-tiered leverage,
shock override, weekly sticky decisions) returns **17.6% a year out of sample** at a **−20.2% drawdown** with about
**9 position changes a year**, against Demeter's published **31.3% at −13.65%** rebalanced daily. The gap is entirely
on the downside — down-capture 146% versus Demeter's 23%.

The study's most useful finding is negative: the rule that best fits Demeter's record after 2012 ("3× while VIX is
below its 10-day average, else cash") returns **+18.3% a year out of sample and −5.7% a year with a 92% drawdown
across 1990–2012**. Selecting on the recent window alone would have shipped it. See `model/RESULTS.md`.
