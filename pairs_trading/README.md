# Pairs trading on NIFTY 50 stocks

A walk-forward cointegration study of every pair inside the NIFTY 50, answering one
question: is there a tradeable mean-reversion edge between Indian large caps, and what
is it worth after costs?

**Result.** Yes, but thin. Screening all 1,081 pairs each quarter, trading the 10 most
strongly cointegrated on a 60-day rolling z-score and charging 10 bps per leg per side
gives a **Sharpe of 0.54** on 4.4% volatility across 6.9 out-of-sample years (2.3% CAGR
unlevered, 5.3% at a 10% vol target), with 0.04 beta to the index and an 8.8% maximum
drawdown. It breaks even at 20 bps per leg (80 bps round trip) and is not significant at
95% (bootstrap Sharpe CI −0.21 to +1.29).

The textbook variant — a z-score fixed on the formation window, as in Gatev et al. —
**loses money** on this universe (Sharpe −0.72). Making the z-score trailing is the
single change that flips the sign.

## Layout

| File | What it does |
|---|---|
| `fetch_data.py` | Downloads daily adjusted closes for the 50 constituents (2012–2021) into `data/` |
| `pair_engine.py` | Screening (Engle–Granger, ADF, half-life, crossings), the base backtest, performance stats |
| `variants.py` | Fourteen signal-construction variants: static vs rolling z-score, static vs rolling hedge ratio, re-screening cadence, thresholds, book width |
| `final_run.py` | Best configuration with full diagnostics, cost sensitivity, per-pair P&L, cointegration census, bootstrap significance |
| `prep_dashboard_data.py` | Compresses `results/` into one JSON payload for the dashboard |
| `dashboard_template.html` | The dashboard source, with a `__DATA__` placeholder |
| `dashboard.html` | Published dashboard (template + injected data) |
| `results/` | Every CSV and JSON the scripts emit |

## Running it

```bash
pip install pandas numpy statsmodels openpyxl
python fetch_data.py          # writes data/<SYMBOL>.csv
python pair_engine.py         # base walk-forward backtest
python variants.py            # the 14-variant study
python final_run.py           # best config + robustness (a few minutes)
python prep_dashboard_data.py # rebuild the dashboard payload
```

Scripts read prices from `$PAIRS_DATA_DIR` (default `data/`) and write to `results/`.

## Method

- **Universe** 47 of the 50 constituents. HDFCLIFE and SBILIFE listed in late 2017 and
  cannot support a three-year formation window early in the sample; NESTLEIND is absent
  from the source dataset.
- **Walk-forward** 756-day formation window, 63-day trading window, rolled forward. Pair
  selection, hedge ratio and spread calibration use formation data only.
- **Screen** log-price correlation > 0.70, Engle–Granger in both orientations keeping the
  stronger, ADF p < 0.05 on the residual, OU half-life 5–60 days, ≥ 12 mean crossings per
  formation year, positive hedge ratio.
- **Signal** trailing 60-day z-score of the spread. Enter |z| > 2.0, exit |z| < 0.5, stop
  |z| > 3.5, force-close after 60 days or at the re-screening boundary.
- **Costs** 10 bps per leg per side (40 bps per completed round trip across both legs).
  The short leg assumes stock futures — cash-market shorts cannot be carried overnight in
  India.
- **Benchmark** equal-weight buy-and-hold of the same 47 names over identical dates.

## Known limitations

Survivorship bias (the universe is the index as constituted at the end of the sample,
back-filled); fills at closing prices with no borrow, roll or basis cost; the data stops
at 31 December 2021; and the reported configuration was selected by looking at the same
out-of-sample period it is scored on — the honest headline is the variant family's median
Sharpe of roughly 0.45, not the best cell in the grid.

Research only. Not investment advice.
