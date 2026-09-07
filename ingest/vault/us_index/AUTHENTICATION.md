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
(pending)
