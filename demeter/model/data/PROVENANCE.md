# Market data provenance

All series were assembled on 2026-09-03 inside a sandbox whose egress policy blocks Yahoo Finance, FRED,
Stooq, CBOE, Nasdaq, Kaggle and Hugging Face. Only PyPI and GitHub (git clone + raw.githubusercontent.com)
were reachable, so every input below is a GitHub- or PyPI-hosted mirror of a primary source. Treat this as
research-grade data: good enough for regime/timing model design, not for trade-level accounting.

| File in `raw/` | Primary source (via mirror) | Coverage | Notes |
|---|---|---|---|
| `steelcerberus_us_market_data.csv` | github.com/SteelCerberus/us-market-data (commit 2025-12-21). Yahoo/FRED-derived S&P 500 price index, dividends added to approximate SPY total return (0.0945% ER applied), 3-month T-bill (FRED DTB3/TB3MS), CPI, LETF swap rate | daily 1885-03-20 .. 2025-12-19 | Before 1927-12-30 the "S&P 500" is a Dow Jones composite proxy (flagged `spx_quality=dow_composite_proxy`). Risk-free before 1954 is 1-month bills (1926-1953) or an approximation (pre-1926). Since 2023-06-16 the close is SPY-derived. Monthly total returns Jul 2012-Dec 2025 match Demeter's published SPY column with correlation 0.9998 and mean absolute difference 0.05%. |
| `fred_sp500_daily_2016_2026.csv` | FRED series SP500 (S&P Dow Jones Indices), archived in github.com/datasets/s-and-p-500 (`archive/fred_sp500.csv`, commit 2026-09-01) | daily 2016-02-12 .. 2026-02-11 | Used only to extend the price series from 2025-12-22 to 2026-02-11 (35 rows). Total return over the extension = price return + trailing 12-month dividend yield accrual (1.51% p.a.); T-bill held at 3.53%. Rows flagged in `spx_src`/`rf_src`. Overlap check vs the SteelCerberus series 2016-2025: daily-return correlation 0.997 (differences are SPY ex-dividend days). |
| `cboe_vix_daily.csv` | CBOE `VIX_History.csv`, mirrored by github.com/datasets/finance-vix (commit 2026-09-02) | daily 1990-01-02 .. 2026-09-01 | Open/high/low/close. |
| `pysystemtrade_SP500_daily.csv` | CME E-mini S&P 500 futures, back-adjusted (Panama) prices from github.com/robcarver17/pysystemtrade `data/futures` (data snapshot ends 2024-03-28) | daily 1982-09-14 .. 2024-03-28 | Daily settlements until 2013-10-15; afterwards sparse, irregular hourly bars (often 1-5 bars a day at random hours) reduced to the last bar at or before 16:15 New York time by `extract_pysystemtrade.py`. `es_ret = d(adj)/prev actual price`. Versus synthetic futures (S&P TR minus T-bill): daily-return correlation 0.989 in the daily era (1990-2013) but only 0.90 in the hourly era (weekly 0.97, monthly 0.99), so the futures series is a cross-check, not the primary backtest asset. Futures lag TR-minus-T-bill by about 0.3-0.5% a year (implied financing spread), which motivates the 25-50 bp financing-spread sensitivity in the model study. |
| `pysystemtrade_NASDAQ_daily.csv` | CME E-mini NASDAQ-100 futures, same source | daily 1999-12-14 .. 2024-03-28 | `nq_ret` as above. Correlation with NASDAQ Composite daily changes 2000-2018 = 0.95. |
| `pysystemtrade_FED_daily.csv`, `pysystemtrade_SOFR_daily.csv`, `pysystemtrade_VIX_daily.csv` | 30-day Fed funds futures, Eurodollar/SOFR 3-month futures, VIX futures, same source | 1990/1984/2006 .. 2024-03 | `ff_implied_pct = 100 - price` (cross-check of the T-bill series: mean gap -0.35 pp 1990-2024). |
| `arch_yahoo_nasdaq_composite_1999_2018.csv`, `arch_yahoo_sp500_1999_2018.csv` | Yahoo Finance dumps bundled in the `arch` PyPI package (`arch.data.nasdaq`, `arch.data.sp500`) | daily 1999-01-04 .. 2018-12-31 | Cross-checks only. |
| `skfolio_sp500_index_1990_2022.csv` | S&P 500 index closes bundled in the `skfolio` PyPI package | daily 1990-01-02 .. 2022-12-28 | Cross-check only. |
| `shiller_sp500_monthly.csv` | Robert Shiller's monthly S&P data (Yale) via github.com/datasets/s-and-p-500 | monthly 1871-01 .. 2026-08 | Monthly average prices; dividends/earnings to 2023-06. Reference only. |

`build_dataset.py` joins everything on NYSE trading dates into `market_daily.csv` (35,289 rows, 1885-03-20 .. 2026-02-11)
and writes `dataset_checks.json` with the validation statistics quoted above.

## Known gaps

* No daily S&P 500 data after 2026-02-11 and no T-bill data after 2025-12-19 in any reachable mirror. Demeter's
  factsheet runs to 2026-06, so model-vs-Demeter comparisons use Jul 2012 - Jan 2026 (163 full months).
* NASDAQ futures end 2024-03-28; no NASDAQ index history before 1999 was reachable. NASDAQ is therefore a
  secondary leg in the model study.
* T-bill on days 2025-12-22 .. 2026-02-11 is held at the last observation (3.53%).
