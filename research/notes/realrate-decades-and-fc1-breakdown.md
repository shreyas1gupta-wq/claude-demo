# Real long rates by decade × equity returns + FC1 per-country breakdown

**Status: CONTEXT NOTE, descriptive. No hypothesis, no bars, no census consumption. Decade
panel desk-computed from JST R6 (`scripts/analyze_realrate_decades.py`, run 2026-09-03);
FC1 per-country values are the PERSISTED prints from the original Atlas 1.1 run
(2026-09-01, `scripts/analyze_financial_cycle.py`) — not recomputed. Written on principal
request following the repression-era note.**

## Median real long rate by decade, 18 JST economies (ex-post: (1+ltrate)/(1+infl)−1)

| Decade | Real long rate | Real equity CAGR (median) |
|---|---|---|
| 1870s | +4.8 | +9.4 |
| 1880s | +4.7 | +7.2 |
| 1890s | +3.7 | +5.6 |
| 1900s | +2.6 | +4.8 |
| 1910s | **−4.4** | −4.1 |
| 1920s | +6.2 | +5.3 |
| 1930s | +5.2 | +3.6 |
| 1940s | **−3.1** | +0.1 |
| 1950s | +1.1 | +11.0 |
| 1960s | +2.4 | +3.9 |
| 1970s | **−0.1** | −2.1 |
| 1980s | +3.9 | +13.9 |
| 1990s | +5.0 | +11.4 |
| 2000s | +2.3 | −1.2 |
| 2010s | +0.4 | +7.6 |

## The relation (pooled country-decades, 1870s-2010s)

- **Same decade: strongly POSITIVE** — Pearson +0.60, Spearman +0.49 (n=222). By tercile,
  monotone: repressed decades (median real rate −1.2%) → equity median **+1.9%/yr**;
  high-real-rate decades (+5.2%) → equity median **+8.9%/yr**. Mechanism read: mostly the
  COMMON DENOMINATOR — an inflation surprise crushes bonds and stocks in the same decade
  (1910s, 1970s), disinflation rewards both (1980s-90s). Not "high rates are good for
  stocks"; the inflation shock owns both signs.
- **Next decade: the sign FLIPS** — Pearson −0.23 (p=0.001), Spearman −0.19 (n=212).
  Repressed decades were historically followed by BETTER equity decades (1940s→1950s,
  1970s→1980s): the escape from repression pays equity holders, entering a decade at high
  real rates precedes modestly worse ones. Weak (~0.2), decade-scale, 18 economies — a
  context regularity, not a signal; consistent with states-never-dates.

## FC1 per-country breakdown — corr(5y Δcredit/GDP, 5y Δlog real house prices)

Persisted prints behind the published median +0.40, 17/17 positive (JST R6, full sample):
Japan +0.69, UK +0.63, Switzerland +0.56, Spain +0.50, Netherlands +0.50, Sweden +0.48,
Canada +0.48, Finland +0.43, Germany +0.40, Belgium +0.40, France +0.33, Denmark +0.33,
USA +0.32, Italy +0.24, Australia +0.21, Ireland +0.19, Norway +0.06.

**India: NOT COMPUTABLE on the desk today.** India is not in JST; the two inputs (RBI/NHB
house-price index, BIS credit-to-private-non-financial/GDP) live on blocked hosts —
runsheet row added (principal-machine pull). Literature read meanwhile (Behera-Sharma,
RBI WPS 03/2019 / J. Emerging Market Finance 2022): a financial cycle EXISTS in India,
credit-cycle duration ~15y vs ~5y business cycle post-reforms, driven by credit and equity
prices with the HOUSE-PRICE contribution rising since the mid-2000s — i.e., India's cell
is expected positive and strengthening, but the desk number waits on the pull.
