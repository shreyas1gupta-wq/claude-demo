# Vault: us_index/ — authentication record (two-pass, anchors BEFORE values)

## sp500_shiller_monthly_1871.csv
Source: github.com/datasets/s-and-p-500 (datahub core mirror of Robert Shiller's ie_data,
monthly 1871-). Pulled 2026-09-07 via raw.githubusercontent (primary econ.yale.edu is
proxy-blocked — the runsheet row for the primary stands; this mirror carries the same
Shiller construction: monthly AVERAGES of daily closes).

### RECORDED PROPERTY (stated before use)
Shiller prices are MONTHLY AVERAGES, not month-end closes: 1-month returns are smoothed
(positive autocorrelation induced, 1m volatility understated). Any 1-month distribution
read must carry this flag; horizons >= 1y are materially unaffected.

### PASS 1 — anchors written BEFORE checking the data (2026-09-07)
- A1: span starts 1871-01; ends >= 2017-12.
- A2: Sep-1929 SP500 (monthly avg) in [30, 33].
- A3: Jul-1932 in [4.0, 5.2] (the Depression trough).
- A4: Dec-1999 in [1350, 1500].
- A5: PE10 (CAPE) Dec-1999 in [40, 46] (the all-time valuation peak).
- A6: CPI Jan-1913 in [9.5, 10.2] (BLS series start-era level).

### PASS 2 — results (filled AFTER the pull; bars never moved)
- A1 span 1871-01 .. 2026-08 (1,868 rows) — PASS (mirror is CURRENT, beyond the 2017 bar).
- A2 Sep-1929 = 31.30 — PASS. A3 Jul-1932 = 5.01 — PASS. A4 Dec-1999 = 1428.68 — PASS.
- A5 PE10 Dec-1999 = 44.20 — PASS. A6 CPI Jan-1913 = 9.80 — PASS.
All six anchors passed on the first check; nothing re-tried. Vault AUTHENTICATED
(sha256 in manifest.json, WORM).

## 2026-09-07 additions — US DAILY series (two-pass, anchors BEFORE values)

### djia_daily_1980_2012.csv
Source: Rdatasets mirror (vincentarelbundock/Rdatasets, csv/AER/DJIA8012.csv) of the AER
R package's "Dow Jones Industrial Average (DJIA) index" daily series, ~1980-2012.

### sp500_fut_adjusted_daily.csv + sp500_fut_multiple_daily.csv
Source: robcarver17/pysystemtrade (master), data/futures/{adjusted_prices_csv,
multiple_prices_csv}/SP500.csv — back-adjusted S&P 500 futures daily from 1982-09 and the
unadjusted per-contract prices. RETURN CONVENTION declared NOW: futures daily return =
diff(adjusted price) / lag(UNADJUSTED current-contract PRICE) — percentage returns taken
directly on a back-adjusted level are biased early in the sample (additive splicing), so
the diff/unadjusted construction is the only permitted form.

### PASS 1 — anchors written BEFORE checking any value (2026-09-07)
- B1 (DJIA): 1987-10-19 daily return <= -20% (Black Monday, published -22.6%).
- B2 (DJIA): 2008-10-13 daily return >= +9% (published +11.1%).
- B3 (DJIA): span covers 1981-01..2011-12; row count in [7900, 9000]; levels in 1980
  near [750, 1100] and in 2011 near [10500, 13000].
- B4 (SPX futures): 1987-10-19 return (declared construction) <= -15%.
- B5 (SPX futures): 2020-03-16 return <= -7%; span reaches >= 2024-06.
- B6 (SPX futures): unadjusted PRICE in mid-2024 within [4500, 6500].

### PASS 2 — results (filled AFTER the pull; bars never moved)
(pending)
