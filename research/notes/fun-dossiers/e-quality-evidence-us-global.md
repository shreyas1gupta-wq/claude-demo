# Dossier E — Empirical Evidence: Profitability, Quality, Growth as Return Predictors (US + First-World)

*Growth/ROIC/quality deep-dive, 2026-09-08; Sonnet research agent, adversarially
consumed. Knowledge synthesis; every claim [LIT], magnitudes approximate. Firm-level
fundamentals NOT yet vaulted — TEST notes state what each claim needs.*

## 1. US core evidence

- **Novy-Marx (2013 JFE)** gross profitability GP/Assets: high-minus-low ~0.3%/mo
  (~4-5%/yr), 1963-2010, value-comparable Sharpe. The payload is COMPLEMENTARITY: GP
  near-orthogonal (slightly negative corr) to HML — cheap+profitable roughly doubles the
  Sharpe of value alone and screens out cheap-for-a-reason distress. Profitability is
  "the other side of value." TEST: direct on Ken French library (pending pull) — double
  sorts pre-tabulated, no re-implementation (process note #6).
- **Fama-French 5-factor (2015 JFE)**: RMW ~0.25-0.3%/mo, CMA ~0.2-0.25%/mo (half HML's
  size, comparable t-stats). REDUNDANCY DEBATE: HML statistically redundant in FF5
  spanning regressions — contested, sample-dependent (post-2007 value slump muddies it).
  TEST: re-run the spanning regression on the French pull; flag post-2007 separately.
- **Hou-Xue-Zhang q-factor (2015 RFS; q5 ~2021)**: quarterly ROE factor ~0.5%+/mo
  (faster construction beats annual RMW); q vs FF5 horse race unresolved — each alphas
  the other in sub-samples [LIT, LOW CONFIDENCE on verdict]. No vaulted q-source —
  runsheet gap.
- **QMJ (Asness-Frazzini-Pedersen 2019 RAS)**: 4 pillars — profitability, GROWTH IN
  PROFITABILITY (not assets!), safety, payout. US ~0.4-0.5%/mo (~5-6%/yr), Sharpe
  ~0.4-0.6, higher pooled across ~24 countries. Load-bearing extra: the PRICE of
  quality varies and predicts QMJ's own forward return (cheap quality → higher QMJ).
  AQR data not vaulted — runsheet gap.
- **Sloan (1996)** accruals: ~10%/yr original (1962-91, raw, no-cost, decile-extreme);
  substantial post-publication decay. Gated on fundamentals.
- **Piotroski F-score (2000)**: ~23%/yr high-minus-low WITHIN the value quintile
  (1976-96) — largest quality-in-value spread; concentrated small/micro-cap; attenuates
  in large-cap/post-publication samples.
- **Stambaugh-Yu-Yuan (2012/2015)**: anomaly returns concentrate in high-sentiment
  states, asymmetric (the junk SHORT leg is the hard-to-arbitrage side) — quality as a
  limits-to-arbitrage story. Needs borrow-cost data (not vaulted).
- **Ball-Gerakos-Linnainmaa-Nikolaev (2016 JFE)** CASH-based operating profitability:
  dominates BOTH Novy-Marx GP and accrual measures — larger, more robust, unifies
  Sloan+Novy-Marx into one clean characteristic. **The single highest-value
  fundamentals construction once firm data lands.**

## 2. Growth as a firm-level predictor — honestly

- **Cooper-Gulen-Schill (2008 JF)** asset growth: HIGH asset growth → LOW returns,
  low-minus-high ~8%/yr (1968-2003), robust to size/B-M/momentum. CMA independently
  corroborates the sign — one of the most robust facts in the literature.
- **Lakonishok-Shleifer-Vishny (1994 JF)**: chased past sales/earnings growth (glamour)
  loses ~10-11%/yr to value; explicitly behavioral (extrapolation).
- **THE RECONCILIATION (the dossier's most important paragraph): the market OVERPAYS
  for GROWTH (forward-looking, promised, extrapolated — assets, sales, narrative) and
  UNDERPAYS for PROFITABILITY (backward-looking, realized, hard to fake).**
  Growth-as-asset-expansion and growth-as-narrative predict NEGATIVELY;
  growth-IN-profitability (QMJ's pillar) predicts positively because it confirms
  quality rather than promising scale. [Mechanistically consistent with the booked
  macro growth-negative doctrine — same fade/dilution physics at different scales.]

## 3. First-world / global ex-US

- QMJ positive in the large majority of ~24 developed markets; per-country smaller and
  noisier; pooled global Sharpe higher.
- Gross profitability replicates NA/Europe/APAC-ex-Japan; **weaker in Japan**.
- Accruals internationally: substantially a common-law/high-discretion-accounting
  phenomenon; weak in code-law regimes [LIT, LOW CONFIDENCE].
- F-score replicates (Australia/UK/Europe/EM) with attenuation; strongest in
  small/uncovered universes — an information-frictions story.
- **Japan, the factor graveyard**: value and momentum notoriously weak; the quality
  family (profitability/safety composites) is what survives best, muted [LIT, LOW
  CONFIDENCE].
- Verdict ex-US: real but smaller/noisier per-country; pooling helps; costs bite harder.

## 4. Interactions and timing

- **Flight to quality**: QMJ (Safety pillar) defensive in downturns — complements, but
  is not identical to, the booked post-stress-entry doctrine (relative vs timing).
- **Greenblatt Magic Formula**: consistent in spirit with profitable-value; as an
  implementation, academic verdicts mixed — edge not much beyond value alone under
  controls; live vehicles underperformed the book's backtest badly.
- **"Size Matters, If You Control Your Junk" (Asness et al. ~2018)**: the size premium
  REVIVES controlling for quality — junky smalls drag the raw premium; small+quality is
  real. Directly relevant to any NIFTY-750 small/mid sleeve: never unconditional size.
- **McLean-Pontiff (2016 JF)**: average ~−58% post-publication decay across 97
  anomalies. QMJ's authors argue quality decays less (safety demand + short frictions)
  — same-team defense, discount it [LIT, LOW CONFIDENCE].

## 5. The honest negatives

Sloan accruals superseded (decay + Ball et al. dominance); asset-growth weaker
post-2000s OOS; F-score/Magic-Formula attenuate outside small-cap and are
implementation-sensitive; **Harvey-Liu-Zhu (2016)**: t>3.0 is the right bar post
factor-zoo — only the broad families (profitability, value, momentum) survive it;
**Hou-Xue-Zhang "Replicating Anomalies" (2020 RFS)**: ~2/3 of ~450 anomalies fail
careful replication (investment/growth anomalies hit hard); quality crowding since
mid-2010s — the quality valuation spread compressed (the mirror of "cheap quality
predicts QMJ"), and the junk short leg is capacity-constrained by borrow.

## 6. Synthesis table

| Signal | Direction | US magnitude (era) | Ex-US | Post-pub | Data needs |
|---|---|---|---|---|---|
| Gross profitability | + | ~4-5%/yr (1963-2010) | yes, weak Japan | moderate decay; complementarity robust | firm fundamentals |
| RMW | + | ~3%/yr (1963-2013) | FF intl sets | HML-redundancy contested | French pull |
| CMA / low investment | + | ~2.5-3%/yr | corroborated | ROBUST (cross-method) | French pull |
| q ROE factor | + | ~6%/yr quarterly-built | thin | contested vs FF5 | no source — gap |
| QMJ | + | ~5-6%/yr | ~24 mkts | authors claim persistence [LOW CONF] | AQR data — gap |
| Sloan accruals | − high accruals | ~10%/yr (1962-91) | common-law mainly | LARGE decay | fundamentals |
| F-score (within value) | + | ~23%/yr within-quintile (1976-96) | attenuated | attenuates | fundamentals |
| Cash op. profitability | + dominates | largest/cleanest (1963-2014) | not yet re-tested [LOW CONF] | newest, least decay data | full statements |
| Asset growth | − | ~8%/yr (1968-2003) | thin | weaker OOS, sign robust | fundamentals |
| LSV glamour | − | ~10-11%/yr (1968-90) | — | value-debate-linked | growth history |
| Size × quality | + small+quality | revives size | thin | recent | fundamentals |

**Cross-cutting TEST note:** everything bottom-up is gated on the firm-fundamentals
pull; the runnable-now pieces are the French factor series (pending) and NSE strategy
indices (pending) at index level. Priority construction once data lands: Ball et al.
cash-based operating profitability — one clean characteristic replacing two noisy ones.
