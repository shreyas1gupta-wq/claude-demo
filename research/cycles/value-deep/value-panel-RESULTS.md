# Value real-data results — India HML mirror + US Fama-French factors

Sources/authentication per file header. India levels carry the mirror [VERIFY]
caveat from M0/M1; shapes and correlations are the primary objects here.
Generated 2026-09-01; trials V0-V4 ledgered.

## V0 — Authentication (US HML chronology must match published history)

| Worst months | HML % | Best months | HML % |
|---|---|---|---|
| 2020-03 | -13.9 | 1932-07 | +35.6 |
| 1932-11 | -13.1 | 1932-08 | +34.2 |
| 1933-09 | -11.7 | 1939-09 | +22.2 |
| 2009-01 | -11.3 | 1933-04 | +19.6 |
| 1934-07 | -10.7 | 1933-05 | +19.2 |

US FF3 span: 1926-07 → 2024-11 (1181 months, 202411 CRSP vintage).

## V1 — India HML: level and sub-periods (mirror)

| Window | ann. mean (x12) | ann. vol | Sharpe vs RF | n |
|---|---|---|---|---|
| full 1993-2025 | +8.6% | 20.3% | 0.09 | 387 |
| 1994-2014 | +7.1% | 22.4% | -0.00 | 252 |
| 2015-2019 (the growth mania) | +0.8% | 14.4% | -0.39 | 60 |
| post-2020 | +18.8% | 16.6% | 0.82 | 72 |

## V2 — The value-momentum correlation (AMP's diversification claim)

- India (mirror, 386 months): corr(HML, WML) = **-0.37**
- US (French, 1175 months since 1927): corr(HML, Mom) = **-0.41**
- Rolling 60m correlations exported to the lesson charts. Published AMP claim:
  materially negative within every market they studied [exact table cell VERIFY].

## V3 — The combination (why negative correlation is the free lunch)

| Portfolio | ann. mean | ann. vol | Sharpe (raw) |
|---|---|---|---|
| US HML | +4.1% | 12.4% | 0.33 |
| US Mom | +7.4% | 16.3% | 0.45 |
| US 50/50 | +5.7% | 8.0% | 0.72 |
| India HML | +8.6% | 20.3% | 0.42 |
| India WML | +13.4% | 24.5% | 0.55 |
| India 50/50 | +11.0% | 12.7% | 0.86 |

The 50/50 Sharpe exceeding BOTH legs on both panels is the diversification
arithmetic our sleeve-weighting prior rests on (D11 fixed-weights rule).

## V4 — Value winters (HML drawdowns > 20%, peak depth, recovery)

| Panel | Start | End (recovered<2%) | Max depth |
|---|---|---|---|
| US | 1930-12 | 1932-07 | 33% |
| US | 1932-11 | 1933-05 | 33% |
| US | 1934-07 | 1937-03 | 44% |
| US | 1938-03 | 1943-01 | 37% |
| US | 1980-10 | 1982-02 | 28% |
| US | 1991-09 | 1993-02 | 26% |
| US | 1999-09 | 2001-02 | 42% |
| US | 2009-01 | **not recovered at sample end (2024-11)** | 58% |
| India (mirror) | 1996-02 | 2003-06 | 59% |
| India (mirror) | 2006-03 | 2007-08 | 22% |
| India (mirror) | 2012-07 | 2014-05 | 31% |
| India (mirror) | 2015-03 | 2016-11 | 25% |
| India (mirror) | 2018-09 | 2022-01 | 50% |

Note the last US row: by this HML construction the post-2009 drawdown was still open at the 202411 vintage — 'value's recovery' since 2020 is a partial climb inside a historic hole, not a round trip. The US winters and India's 2018-2022 and any Indian analogues,
are the empirical basis for the SPREAD-CONDITIONED patience rule (never abandonment,
never doubling down — the valuation_sentiment block consumes the spread state).

