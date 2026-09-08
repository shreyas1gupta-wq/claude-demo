# AUTHENTICATION — firm_panel (data_ml, Coqueret-Guida ML-for-factor-investing panel)
Source: GitHub mirror `JustinMShea/ExpectedReturns` data/data_ml.RData (shallow clone
2026-09-08); the public teaching dataset of Coqueret & Guida, "Machine Learning for
Factor Investing" (2020). US(-dominated) stocks, monthly.

## PASS 1 — anchors (committed BEFORE any value check)
B1 shape: 283,380 rows x 99 columns; stock_id count = 1,207 (the book's stated panel).
B2 span: 1998-11-30 .. 2019-03-31 monthly (book-stated).
B3 features are CROSS-SECTIONALLY UNIFORMIZED to (0,1] by date (book construction) —
   ranges of Roe/Roce/Eps_Basic_Gr/Capex_Sales must lie in [0.005, 1.0]; suitable for
   decile/rank sorts ONLY; raw levels are NOT available.
B4 forward returns R1M/R3M/R6M/R12M_Usd are RAW total returns (R1M mean ~+1.3%/mo,
   sd ~0.18 — pass 2 records exact).
B5 DECLARED LIMITS (carried on every downstream print): the panel is the book's
   FILTERED sample (names with sufficient data history — a survivorship/selection tilt
   the authors acknowledge); anonymized ids (no tickers/sectors); EW analyses only
   (Mkt_Cap features are rank-scaled); US-dominated but not an index universe; forward
   returns overlap at >1M horizons (overlap flagged in any such read).
B6 pass-2 value checks: (i) per-date stock count between 400 and 1,207 for all months;
   (ii) monthly EW mean of R1M_Usd correlates >= 0.85 with the vaulted US market factor
   (fff Mkt-RF + RF) on the overlap — the panel must move with the US market;
   (iii) 2008-10 and 2008-11 EW R1M_Usd prints negative (GFC months).

## PASS 2 — verification results (2026-09-08, after the anchors commit)
(i) per-date stock count 552..1196 PASS. (ii) EW forward-1m (shifted one month) vs the
vaulted US market: corr 0.884 (245m) PASS. (iii) the GFC anchor AS WRITTEN failed on
its second month — **ANCHOR MIS-SPECIFIED (forward-return indexing), recorded**: R1M at
row-date t realizes in t+1, so the crash rows are 2008-09-30 (= Oct-08, prints -0.204)
and 2008-10-31 (= Nov-08, -0.075), both negative — the corrected read PASSES; the row
dated 2008-11-30 carries the positive Dec-08 bounce (+0.069), consistent with the
record. VERDICT: panel authenticated; forward-return convention (row t -> month t+1)
is now the DECLARED convention for every downstream use.
