# Vault: index/ — authentication record (two-pass, bars before results)

## nifty50_daily_2007_2026.csv
Source: github.com/kalilurrahman/NIFTY_50_STOCK_DATA (file NIFTY50_stock_history.csv),
sparse-cloned through the session git proxy 2026-09-02. Upstream provenance: Yahoo Finance
^NSEI daily history (format signature: "Adj Close" == "Close", Volume 0 for the index).
Span observed at format inspection: 2007-09-17 .. 2026-04-13 (~4,554 rows).
Mirror status: THIRD-PARTY MIRROR of exchange data — authenticated against independently
documented values below; the principal-machine NSE pull remains the runsheet item of record
and supersedes this file when it lands.

### PASS 1 — anchors written BEFORE checking the file (2026-09-02)
- A1: 2020-03-23 close = 7,610 ± 1 AND close-to-close return ≤ −12.5%
  (web-verified: StockEdge/Threads/BusinessToday — "closed at 7,610", "~13% single day").
- A2: 2008-01-21 close-to-close return ≤ −7.0%
  (web-verified Black Monday; Sensex −1,408 pts documented; exact Nifty close not pinned,
  so the bar is a return bound, stated as such).
- A3: 2024-06-04 close = 21,884.50 ± 1 AND return ≈ −5.9% ± 0.2pp
  (verified in this program's own political-close monograph, Band-3 agent web pass).
- A4: coverage 240–252 rows per full calendar year 2008–2025, no year missing.
- A5: dates strictly increasing, no duplicates; all closes > 0.
- A6: the sample's single worst close-to-close return IS 2020-03-23 (consistency with A1).

### PASS 2 — results (run after the bars above were committed to file)
Run 2026-09-02, after the bars above were written to this file:
- A1 PASS — close 7,610.25, return −12.98%.
- A2 PASS — return −8.70% (close 5,208.80, matching the folk-memory figure the web pass
  could not pin — recorded as corroboration, not as a bar).
- A3 PASS — close 21,884.50, return −5.93%.
- A4 PASS — 240–250 rows per full year 2008–2025, no missing year.
- A5 PASS — strictly increasing, no duplicates, all closes positive.
- A6 PASS — the sample's worst day is 2020-03-23 at −12.98%.
6/6 anchors passed; the mirror is admitted to the vault as a THIRD-PARTY MIRROR (the NSE
pull remains the runsheet item of record).
