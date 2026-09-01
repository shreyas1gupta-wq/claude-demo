# Part D — The mathematics (value/quality-specific; shared machinery in the credit Part D)

## D1. The combination theorem our sleeve structure rests on (with our own numbers)

For two return streams with Sharpes S₁, S₂ and correlation ρ, the equal-weight combination's
Sharpe is

    S_c = (S₁ + S₂) / sqrt(2·(1 + ρ))

With ρ = −0.41 and S = 0.33/0.45 (US HML/Mom, our V3 measurements): S_c ≈ 0.78/sqrt(1.18) ≈ 0.72
— exactly what V3 measured (0.72). India: (0.42+0.55)/sqrt(2·0.63) ≈ 0.86 — again the measured
cell. The lesson is structural: **a negatively-correlated pair of modest premia beats either
premium alone by more than any optimizer could add**, and it is why value earns a sleeve seat
next to momentum even if its standalone Indian Sharpe vs RF is thin (V1: 0.09 full-period).
Long-only translation: the combination happens in the SCORE blend and the netting layer, not by
holding two long-short books.

## D2. The value spread as a state (Cohen-Polk-Vuolteenaho, operationalized)

Spread_t = log( BP_cheap-quintile,t / BP_expensive-quintile,t ). Under the LSV expectation-error
view, a wide spread = the market is paying historically extreme premia for glamour = future value
returns high (the CPV regression's positive slope). Under the risk view, a wide spread = value
risk premia are high. Both views agree on the SIGN of the conditional relation — which is all our
reduce-only consumption needs: the spread's expanding percentile feeds valuation_sentiment (0.10
budget), tilting patience (never abandonment at wide spreads, never doubling down either — the
sizing stays inside frozen caps). Our module's `value_spread` recovered a planted dispersion
episode at +0.09 log-points separation (5/5 seeds).

## D3. Migration accounting (Fama-French 2007) — where value returns actually come from

Decompose portfolio return into: drift (staying put), migration (cheap names re-rating into
neutral/growth buckets), and membership churn. FF2007's finding: the value premium is mostly
MIGRATION — convergence of price to fundamentals, not superior fundamental growth (value firms'
fundamentals actually lag). Implication for construction: holding-period and rebalance cadence
must give convergence room (our fixture's mispricing τ½ ≈ 23 months is the design intuition);
implication for monitoring: a value sleeve whose migration component dies while spreads stay wide
is broken plumbing, not a dead premium — the TC-by-constraint attribution separates these.

## D4. The PIT lag, quantified as a bias

Fundamental ratios computed with information not yet public overstate backtests two ways:
(i) the numerator effect — using quarter-end book before its announcement embeds the
announcement-window return; (ii) the crash effect — B/P computed with STALE prices during fast
markets mislabels risk as cheapness. Our test suite demonstrates (i) mechanically: the lag-0
"cheat" spread exceeds the honest lag-3 spread on every seed. The India-specific lag grid
(results filing lags; Part C's table) is therefore a first-class registry parameter, not a detail.

## D5. Quality composition without an optimizer

Quality inputs (gross profitability, accrual sign, leverage, governance flags) are combined as
fixed near-equal ranks (D11 rule). The accruals input deserves its own note: Sloan's anomaly is a
REVERSAL of the accrual component of earnings; in India, annual-only balance sheets make accruals
an annual-frequency input riding inside a quarterly sleeve — the mixed-frequency rule (annual
inputs enter as slowly-decaying levels, refreshed on filing dates) is pre-registered in Part C's
pipeline. Governance red flags (pledge %, auditor events, rating actions) are Tier-C REDUCE-ONLY:
they may only push a name's quality rank down, mirroring the credit composite's clamp.

# Part E — The algorithm

```
STEP 0  registry load; PIT universe; fundamentals store (announcement-dated, Part C pipeline)
STEP 1  ratios at date t use filings ANNOUNCED <= t (report-lag API); banks/financials ranked
        within their own group (different statements)
STEP 2  value rank: blend of E/P (trailing 4q), B/P, CF/P (annual) — sector-relative option per
        registry flag; quality rank: profitability + accrual sign + leverage + reduce-only
        governance flags; vq composite per sleeve weights (fixed grids)
STEP 3  value_spread state -> expanding percentile -> valuation_sentiment block (0.10);
        consumption: patience/tilt conditioning, reduce-only first admission
STEP 4  cost-netted alphas -> construct/ (netting vs momentum sleeve captures the negative
        correlation as reduced turnover: a name leaving momentum's shorts often enters value's
        longs — the internal crossing is the free lunch's implementation)
MONITOR monthly realized IC by sleeve; spread state on the daily page; accrual/fundamental
        freshness flags; cert: live-vs-backtest IC floor, staleness ceiling
FAILURE MODES: restatements (store first-print AND restated, signal uses first-print);
        fiscal-year changes; demergers breaking book continuity (CA rules, Part C of momentum);
        the intangibles critique (B/P mismeasurement for asset-light names) — mitigated by the
        multi-ratio blend, logged as an open research question, never patched mid-drawdown
```

# Part F — Harvest map + new designs

| # | Consumer | What it gets | Status |
|---|---|---|---|
| F-a | Value sleeve (return engine) | multi-ratio value rank, cost-netted | live design |
| F-b | Quality sleeve + quality floor | quality rank; boom-mature regimes bind the floor (credit F-f) | live design |
| F-c | valuation_sentiment block | value-spread expanding percentile (0.10 budget) | live design |
| F-d | Momentum interaction | netting/crossing benefits; combo weights prior from V3 | live design |
| F-e | Governance flags | Tier-C reduce-only quality demotions (pledge, auditor, ratings) | live design |
| F-f | Stage-2 briefing | spread state + sleeve ICs on the daily page | live design |

New pre-registered designs: **W1** own-bhavcopy+XBRL HML vs the factor-library mirror (acceptance
test, tracking-error bound pre-set); **W2** India value-spread history from index-level P/B (NSE
publishes daily index P/E-P/B — an interim spread proxy while the stock-level PIT store builds);
**W3** QMJ-lite India (profitability + accrual sign + leverage, free-data version) decile test,
purged; **W4** the 2015-2019 India growth-mania event study at stock level (did wide spreads
predict the post-2020 payoff cross-sectionally?); **W5** value+momentum blend weight grid on the
pooled panel (never India alone), with the V3 correlation as the prior.

# Part H — Knowledge ledger (value/quality)

**Established (pooled + our own real-data runs):** the value premium exists but hibernates for
YEARS (V4: US winters up to 58% and 15+ years unrecovered by one construction; India 2018-2022
50%); the value-momentum correlation is materially negative on both panels (V2: −0.37/−0.41) and
the combination beats both legs (V3) — this pair-level fact is sturdier than either premium
alone; quality premia are real and strongest in their cash-based forms; expectation-error
evidence (analyst extrapolation) supports the behavioral leg.
**Established about OUR machinery:** planted convergence, quality, dispersion-episode detection
and the PIT-cheat demonstration all recovered on every seed; the value-momentum opposition
emerges from mispricing physics alone.
**Pooled-prior, awaiting India primary [A]:** Indian HML level (the mirror's 0.09 Sharpe vs RF
carries the level caveat); the spread-state slope; QMJ-lite magnitudes; sector-relative vs raw
choice.
**Unknowable:** when a value winter ends. The spread state tells us where we are in the cold,
never the date of the thaw — patience is a RULE here (anti-capitulation lock), not a virtue.
