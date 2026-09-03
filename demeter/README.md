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
| `model/` | Replication study: `data/` (market dataset + provenance), `engine.py` (dual-engine backtest engine), `features.py` (causal features), `evaluate.py` (standardised evaluator), `signals/` (candidate models), `results/` (evaluation JSONs), `RESULTS.md` (research note). |

## Regenerating

```bash
cd demeter
python3 build_analytics.py          # -> analytics.json, data/tb3ms_monthly.csv
python3 build_overview.py           # -> overview/index.html
cd model/data && python3 build_dataset.py   # -> market_daily.csv (from raw/ mirrors; see PROVENANCE.md)
cd .. && python3 evaluate.py signals/<model>.py   # -> results/<model>.json
```

Python 3.11 with pandas, numpy (and scikit-learn / statsmodels / hmmlearn for the statistical models).

## Data caveats

* Market data comes from GitHub / PyPI mirrors of Yahoo, FRED, CBOE and CME sources because the primary hosts
  were unreachable from the build environment; see `model/data/PROVENANCE.md` for coverage, checks and gaps
  (daily S&P 500 data ends 2026-02-11, so model-versus-Demeter comparisons use Jul 2012 – Jan 2026).
* The factsheet quotes 3,219 trading days for its four-quadrant analysis while the four quadrant counts sum to
  3,477; both figures are preserved and flagged.
