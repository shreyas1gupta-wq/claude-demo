# Vault: globalvol/ — authentication record (two-pass, bars before results)

## cboe_vix_daily_1990_2026.csv
Source: github.com/datasets/finance-vix @ ea80ff6fda1abbd3601641c3607dac85dd67b44c
(the Frictionless "datasets" org's maintained mirror of CBOE's published VIX history),
depth-1 clone through the session git proxy 2026-09-02. Daily OHLC 1990-01-02..2026-08-31.
Mirror status: third-party mirror of CBOE data; authenticated below.

### PASS 1 — anchors written BEFORE checking the file (2026-09-02)
- A1: 2020-03-16 close = 82.69 ± 0.01 (the all-time closing high; web-verified: CNBC/Macroption).
- A2: 2017-11-03 close = 9.14 ± 0.01 (the all-time closing low; web-verified: Macroption).
- A3: 2008-11-21 close = 80.74 ± 0.5 (the GFC peak close; web-verified: Macroption).
- A4: dates strictly increasing, no duplicates; closes in (5, 100) for all rows.
- A5: coverage 245-255 rows per full year 1991-2025.

### PASS 2 — results (run after the bars above were committed to file)
Run 2026-09-02, after the bars above were committed:
- A1 PASS — 82.69 exactly (2020-03-16).
- A2 PASS — 9.14 exactly (2017-11-03).
- A3 **MISS as written** — the file prints 72.67 on 2008-11-21. Dissection: the anchor was
  mis-specified from a garbled secondary summary; the file shows 80.86 on 2008-11-20, which
  IS the widely-documented pre-2020 record close. The anchor's own error is the miss; the
  file is consistent with the primary record. Bar not moved; recorded per the A6-gold
  precedent (an anchor that misses stays a miss even when the dissection exonerates the data).
- A4 PASS — monotone, no duplicates, closes within (5,100).
- A5 **MISS** — 2022-2025 carry 256-259 rows/year vs the 245-255 bar: ~5-8 extra WEEKDAY
  rows per year (no weekend rows), consistent with upstream including some market holidays
  with carried values. Quantified; percentile-rank uses are insensitive to a few stale rows,
  and any day-count-sensitive use must de-duplicate against an exchange calendar first.
ADMISSION: admitted with the two recorded misses (one anchor-side, one upstream-quirk),
exact passes on the two most-cited records (82.69 / 9.14) supporting genuineness.
