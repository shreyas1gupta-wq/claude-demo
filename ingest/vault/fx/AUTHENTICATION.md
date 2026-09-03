# Vault: fx/ — authentication record (two-pass, bars before results)

## inr_usd_monthly_1973_2026.csv
Source: github.com/datasets/exchange-rates @ 41add84c40333c0a1ab089935f970425fb15372c
(the Frictionless mirror of the US Fed H.10 release), depth-1 clone through the session git
proxy 2026-09-02; the India series extracted from data/monthly.csv. Monthly averages,
1973-01..2026-08. Mirror status: third-party mirror of Fed-published data.

### PASS 1 — anchors written BEFORE checking values (format head/tail seen; these are not)
- A1: the July-1991 two-step devaluation — Jul-1991 monthly avg >= 1.10 x Jun-1991
  (documented ~19% combined devaluation across 1991-07-01/03).
- A2: the 1993 exchange-rate unification — Mar-1993 monthly avg within 29..33 (the unified
  rate settled ~31/USD, documented).
- A3: the 2013 taper stress — max monthly avg during 2013 >= 62 (INR touched 68 intraday;
  monthly averages peaked in the low-to-mid 60s, documented).
- A4: dates strictly increasing, all rates positive, 640-650 rows, no gaps > 1 month.

### PASS 2 — results (run after the bars above were committed)
Run 2026-09-02, after the bars above were committed:
- A1 PASS — Jul/Jun-1991 ratio 1.216 (the documented ~19-21% devaluation lands exactly).
- A2 PASS — Mar-1993 at 31.94 (the unification zone).
- A3 PASS — 2013 max monthly 63.65.
- A4 PASS — 644 rows, monotone, positive, no gaps.
4/4 anchors passed; admitted as a THIRD-PARTY MIRROR of Fed H.10 monthly averages (the RBI
reference-rate pull remains the India-primary series when the principal's machine runs).
