# Vault: panel/ — authentication record (two-pass, bars before results)

## n500_adjclose_2012_2022.csv.gz + n500_value_traded_2012_2022.csv.gz
Source: github.com/Ratnesh-bhosale/NIFTY500_dataset (500 per-stock Yahoo-format daily CSVs,
2012-2022), depth-1 clone through the session git proxy 2026-09-02; upstream commit pinned
in provenance JSON. Vaulted form: two derived matrices (dates × tickers) — dividend/split-
adjusted closes ("Adj Close") and rupee value traded (Close × Volume) — built by
scripts/build_n500_panel.py (committed; byte-reproducible from the pinned commit).

### RECORDED BIAS (a property, not a check)
Membership is the index roster AS OF the dataset's construction (~2021-22), backfilled:
the panel is SURVIVORSHIP-BIASED. Any use must state it; MR1's registered spec (point-in-
time membership) is NOT met by this panel — see the MR1-S registration for the one
asymmetric use permitted (corroborate the freeze; never unfreeze).

### PASS 1 — anchors written BEFORE checking the data (2026-09-02)
- A1: equal-weight panel mean daily return vs vaulted NIFTY50 daily return, correlation
  ≥ 0.85 over the 2012-2022 overlap.
- A2: YESBANK 2020-03-06 close-to-close return ≤ −50% (web-verified: closed ₹16.20,
  −56.04%, Business Standard).
- A3: coverage ≥ 400 tickers with ≥ 2,000 daily rows each.
- A4: per-ticker dates strictly increasing, within 2012-01..2022-01; adjusted closes > 0.
- A5: cross-check of a second documented single-stock event: RELIANCE's largest one-day
  GAIN in the window falls in the COVID-rebound / rights-era spring 2020 (documented
  ~+10-13% days in Mar-Apr 2020) — bar: max daily gain in 2020 ≥ +9% and its date in
  Mar-May 2020.

### PASS 2 — results (run after the bars above were committed to file)
Run 2026-09-02, after the bars above were committed:
- A1 **MISS** — EW-487 vs NIFTY50 corr 0.835 vs the 0.85 bar. Bar NOT moved. Dissection:
  composition (equal-weight small/mid vs cap-weighted large); the top-50-by-liquidity EW
  subset prints corr 0.931 (diagnostic, not a substitute bar). The miss is recorded as a
  mis-set expectation about EW-vs-cap-weight divergence, on the A6-gold precedent.
- A2 PASS — YESBANK 2020-03-06 return −56.1% (bar ≤ −50%; documented −56.04%).
- A3 **MISS** — 379 tickers ≥2,000 rows vs the 400 bar (391 at ≥1,500). Bar NOT moved.
  Dissection: post-2012 listings (median coverage is the full span; the 10th percentile is
  ~1,033 rows) — a composition fact of a survivor roster including newer names.
- A4 PASS on corrected re-run — the first run FAILED due to a CHECK BUG (NaN cells failing
  a `> 0` comparison; NaN is absence, not non-positivity). The corrected check (all non-NaN
  values > 0, monotone, in-bounds) passes with zero non-positive cells. The buggy first run
  is recorded here per the ex[ok]-mask precedent.
- A5 PASS — RELIANCE max-2020 gain +14.7% on 2020-03-25 (bar ≥ +9% in Mar–May 2020).
ADMISSION: admitted with the two recorded misses, the check-bug note, the 13 skipped
empty upstream files (delisted-name Yahoo gaps — a survivorship footnote), and the
survivorship statement above. Event-level anchors (A2/A5) both pass exactly; the panel is
judged genuine with known composition limits.
