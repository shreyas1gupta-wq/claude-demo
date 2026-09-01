# Value and Quality — Full Monograph

v1.0 · 2026-09-01 · Deep-dive #4 at the atlas depth standard. Seats: the value and quality
sleeves of the factor book + the value-spread state feeding the valuation_sentiment block (0.10).
Code: `quant/ladder/value_quality.py` (6 tests incl. the executable PIT-cheat demonstration).
Real data: India factor mirror + US Fama-French (202411), sha256-manifested. Chapter sources in
`research/cycles/value-deep/`.

Headline real-data results (Part B-RESULTS): the value-momentum correlation is materially
negative on BOTH panels (India −0.37, US −0.41) and the 50/50 combination beats both legs
(India Sharpe 0.86 vs 0.42/0.55; US 0.72 vs 0.33/0.45) — the sturdiest cross-sleeve fact we
hold; India's 2015–2019 value winter confirmed (+0.8%/yr, Sharpe −0.39) with the post-2020
thaw (+18.8%/yr, 0.82); US value winters run to 58% and 15+ years unrecovered by one
construction — patience is a rule with a lock, never a mood.

## Contents
- Part A+G — theory (FF-vs-LSV fork, expectation errors, duration view, spread state, migration,
  the quality stack, the combination math, winter anatomy) + operator psychology
- Part B — global evidence + winter case studies + India record
- Part B-RESULTS — V0–V4 computed by us
- Part C — Indian PIT fundamentals: XBRL eras, staircase balance sheets, banks' separate statute,
  Piotroski feasibility, the 12-step pipeline
- Part D/E/F/H — combination theorem with our numbers, spread math, migration accounting,
  PIT bias, algorithm, harvest + designs W1–W5, knowledge ledger

---


---

# PART A + G — Theory and operator psychology

# Value/Quality Deep Dive — Part A & Part G

Part A: Theory — why cheap wins and why good wins · Part G: Psychology of operating
value and quality · v1.0 · 2026-09-01 · Deepens `research/dossiers/02-value-quality-
lowvol.md` (D02; does not contradict it) and the factor-book rows of `docs/DESIGN.md`
§6.2 (Value 20–35%, Quality 20–35%, the value-spread conditioner, the quality
valuation kill-switch) and §10 (the decay ledger's Value and Quality rows) · Status:
theory/citations verified here; India magnitudes remain D02's Tier-B priors pending
the data phase.

This file assumes D02's frozen construct as given — a price-adjacent-majority value
composite (dividend yield, net-share-issuance, sales/price, with lag-buffered B/P and
E/P as a minority), a QMJ-style quality composite augmented with India-specific
promoter-pledge and related-party-transaction junk terms, and a value-spread
conditioner moving the value sleeve's weight within its 20–35% range off the
spread's own decile — and supplies the theoretical machine that construct compresses
into two composite ranks, honest about what stays unresolved. Part G turns to the
desk that has to *operate* those ranks through the two multi-year stretches — being
wrong on value, being too comfortable on quality — that break more factor books than
any single bad quarter.

---

## PART A — Theory: why cheap wins and why good wins

### A.1 The value fact — from Graham-Dodd to a fork in the literature

**(i) Mechanism.** Graham & Dodd's *Security Analysis* (1934) is the lineage's
origin but not yet an empirical claim: buy below a conservatively appraised
intrinsic value, with a margin of safety. **Basu (1977)** supplies the first formal
test: sorting NYSE stocks (1957–71) into quintiles by earnings-to-price, low-P/E
portfolios earn significantly positive CAPM alpha and high-P/E portfolios
significantly negative alpha — a direct challenge to the joint hypothesis of market
efficiency and CAPM. **Fama & French (1992)** generalize P/E to book-to-market and
show something stronger: sorting jointly on size and B/M **absorbs** the
cross-sectional return variation beta alone does not explain, and the beta-return
relation goes flat once both are controlled. **Fama & French (1993)** formalizes the
construct into a tradable factor, and it is at this construction step that the
literature forks into two still-unresolved readings of *why* the premium exists.

**(ii) Formal structure — the HML construction, verbatim.** Each June, stocks are
independently sorted into two size groups (Small/Big, at the **median** NYSE
market-equity breakpoint) and three B/M groups (Low/Medium/High, at the **30th/70th**
NYSE percentile breakpoints, using **December** fiscal year-end book equity over
market equity at that year-end — a ≥6-month lag between fiscal data and formation,
itself a design choice Asness & Frazzini (2013, cited in D02) show has return
consequences). The intersection forms six value-weighted portfolios — **S/L, S/M,
S/H, B/L, B/M, B/H** — held July `t` to June `t+1`. `HML_t = ½(SH_t+BH_t) −
½(SL_t+BL_t)`, size-neutralized by construction.

**The fork.** **Fama-French's reading**: HML proxies a priced, ICAPM-consistent
state variable — persistently low profitability, poor reinvestment options, and
distress cluster in high-B/M firms, and an investor who cannot diversify this away
demands compensation; the premium is real because value stocks are, in some
multi-period sense, riskier. **Lakonishok, Shleifer & Vishny (1994)** contest this on
its own ground: sorting on B/M, cash-flow/price, E/P, and past sales growth, they
test the risk story's own prediction — that value should underperform glamour in the
worst-return states — and find the **opposite**: value does not underperform glamour
in the market's or economy's worst periods. Their alternative: investors **naively
extrapolate** past growth — glamour gets priced for perpetual outperformance, value
for perpetual decline — and because growth mean-reverts (LSV show realized growth
for glamour undershoots, for value overshoots, what price implied), value beats
embedded expectations mechanically as reversion happens, no risk premium required.

**(iii) For our seats.** CONTRACT §5 requires a survival argument in one of four
categories; this fork means value's honest answer is **two categories at once** —
(iii) genuine risk premium *and* (i) a behavioral mechanism — exactly how the decay
ledger already records it (`docs/DESIGN.md` §10: "risk premium + extrapolation bias
(iii)+(i)"). Consequence: the sleeve cannot be defended as if only one story were
true. Under Fama-French, the premium should show up disproportionately paid for in
bad states; under LSV, the pain is macro-uncorrelated, a pure patience tax. Both fit
the premium's *level*; they diverge sharply on what holding it should feel like —
Part G's subject, and why the design cannot wait for the debate to resolve.

**(iv) Citations.** Graham, Benjamin & Dodd, David (1934), *Security Analysis*,
McGraw-Hill (foundational, pre-empirical). Basu, Sanjoy (1977), "Investment
Performance of Common Stocks in Relation to Their Price-Earnings Ratios," *Journal of
Finance* 32(3):663–682. **[Verified]** Fama & French (1992), "The Cross-Section of
Expected Stock Returns," *Journal of Finance* 47(2):427–465. **[Verified]** Fama &
French (1993), "Common Risk Factors in the Returns on Stocks and Bonds," *Journal of
Financial Economics* 33(1):3–56. **[Verified]** Lakonishok, Shleifer & Vishny (1994),
"Contrarian Investment, Extrapolation, and Risk," *Journal of Finance* 49(5):
1541–1578. **[Verified]**

---

### A.2 Expectation errors formalized — extrapolative growth forecasts

**(i) Mechanism.** LSV's "naive extrapolation" needed an instrument, then a formal
model. **La Porta (1996)** supplies the instrument: sorting on IBES analyst
consensus long-term (3–5yr) earnings-growth forecasts, a strategy long the
lowest-forecast decile / short the highest earns a large, significant return, with a
meaningful share of the spread materializing specifically **around subsequent
earnings announcements** — direct evidence the market itself, not merely analysts,
was surprised. **Bordalo, Gennaioli, La Porta & Shleifer (2019)** formalize *why*:
building on representativeness-based "diagnostic expectations," analysts
extrapolate recent growth news too far because it makes the corresponding future
scenario seem more representative, hence more probable, than a correct Bayesian
update allows — "fast growth predicts future Googles, but not as many as analysts
believe."

**(ii) Formal structure.** Diagnostic operator on a belief about growth `θ`,
conditioned on signal `s` relative to prior baseline `s'`: `E^θ[g|s] = E[g|s] +
θ·(E[g|s] − E[g|s'])`, `θ ≥ 0` the overreaction degree (`θ=0` recovers rational
expectations). Strong recent growth pushes forecasted long-run growth above the
rational posterior by an amount scaling with `θ`; because growth mean-reverts, the
excess corrects later — generating La Porta's pattern endogenously from one
belief-updating primitive with an estimable parameter.

**(iii) For our seats.** India's analyst-coverage panel is thin exactly where this
signal helps most — IBES-equivalent consensus forecasts are not free/broad outside
the Nifty 100–200, echoing the momentum dossier's Hong-Lim-Stein coverage tension
(`research/cycles/momentum-deep/partA-theory-psychology.md` A.2.iii). Diagnostic-
expectations theory attaches the bias to **recent growth news itself**, not to a
human forecaster, so a free proxy is buildable from trailing realized sales/earnings
growth (lag-buffered per D02's 4–6 month convention) — giving the value composite a
second lens: rank on the gap between trailing-growth rank and subsequent realized
growth, using the extrapolation mechanism as the *reason* a cheap multiple should
mean-revert, not merely an in-sample observation that it did.

**(iv) Citations.** La Porta, Rafael (1996), "Expectations and the Cross-Section of
Stock Returns," *Journal of Finance* 51(5):1715–1742. **[Verified]** Bordalo,
Gennaioli, La Porta & Shleifer (2019), "Diagnostic Expectations and Stock Returns,"
*Journal of Finance* 74(6):2839–2874. **[Verified]**

---

### A.3 The duration/discount-rate view — and its honest instability

**(i) Mechanism.** A third, non-behavioral candidate reframes value as a maturity
mismatch. **Lettau & Wachter (2007)** model value firms as claims mostly on
cash flows arriving **soon** (limited growth options) and growth firms mostly on
cash flows arriving **far** in the future — the equity analogue of short- versus
long-duration bonds. A distant cash flow's present value is far more sensitive to
the discount rate, so growth stocks should be hurt more when rates rise and helped
more when they fall — value's cheapness would then reflect priced duration risk,
no behavioral bias required. **Lettau & Wachter (2011)** extends the same
stochastic discount factor to jointly price the interest-rate term structure and
the value premium's level and rate-comovement.

**(ii) Formal structure.** By Campbell-Shiller log-linearization,
`log(P_t/D_t) ≈ Σ_h ρ^h · E_t[Δd_{t+h} − r_{t+h}]`. Define equity duration
`Dur ≡ −∂log(P_t)/∂r_t`, larger the more cash flow sits at large `h`. Growth stocks
carry longer duration in the calibration, so `HML`'s expected return should
correlate **positively** with real-rate increases — a clean, testable comparative
static.

**(iii) The honest instability.** AQR's subsequent empirical work (Asness, drawing
on Maloney-Moskowitz) tests the duration implementation across specifications and
does **not** find robust confirmation that growth stocks behave as measurably
longer-duration assets; AQR reports the realized value-minus-growth/rate-change
correlation at roughly **0.03 over 40 years** and **0.34 over the most recent 10** —
weak on average, unstable across sub-periods. Listed-real-estate studies similarly
find the relationship strengthened post-2008 but weakens once economic-state/policy
confounds are controlled — regime-dependent, not a fixed causal law. Asness's own
summary: "people say rates have to rise for value to do well; that is absolutely not
true."

**(iv) For our seats.** CONTRACT §6 ("no magic numbers") and this instability
reinforce each other: no standalone rates-conditioned value-sizing rule. A
rate/credit-regime input belongs only as one candidate regressor in a
pre-registered, purged test alongside others (D02 §4's "momentum-vs-value
conditioning variables" row, already Tier B/C, practitioner-sourced). Duration
stays a legitimate category-(iii) candidate, low-confidence, never licensing a
fixed, un-pre-registered rates threshold.

**(v) Citations.** Lettau & Wachter (2007), "Why Is Long-Horizon Equity Less Risky?
A Duration-Based Explanation of the Value Premium," *Journal of Finance* 62(1):
55–92. **[Verified]** Lettau & Wachter (2011), "The Term Structures of Equity and
Interest Rates," *Journal of Financial Economics* 101(1):90–113. **[Verified]** AQR/
Asness commentary on the duration test and 0.03/0.34 correlation figures.
**[Verified as existing AQR publication ("Is Value Just an Interest Rate Bet?") and
press coverage; Tier C, directional use only]**

---

### A.4 The value spread as a state, not a signal

**(i) Mechanism.** If value's average premium is real under either A.1 story, its
*conditional* expected return is not constant — the clearest state variable is the
spread itself. **Cohen, Polk & Vuolteenaho (2003)** decompose the cross-sectional
variance of B/M ratios and find only 20–25% reflects transitory, mispricing-relevant
variation in expected 15-year returns; the rest is legitimate variation in expected
profitability and persistence. Critically: **expected return to a value-minus-growth
strategy is unusually high precisely when the B/M spread between cheap and
expensive stocks is wide** — the spread predicts the factor's own forward return.
**Asness, Liew, Pedersen & Thapar's "Deep Value"** operationalizes this across
asset classes: episodes where the spread is wide relative to its own history are
followed by high average value returns, low market betas but elevated global-value-
factor betas, deteriorating near-term fundamentals, negative sentiment, and visible
selling pressure into the trough — deep-value episodes look and feel like exactly
the moment to abandon value, immediately **before** its best years begin.

**(ii) Formal structure.** Let `bm_i,t` be B/M at date `t`; define spread `VS_t` from
the cheap-decile vs. expensive-decile distributional gap, and its trailing (e.g.
10-year) percentile `p_t`. CPV's finding: `E_t[HML_{t+1:t+h}]` increases in `p_t` for
long `h` — a conditioning relationship on the factor's own expected return, distinct
from the A.1 mechanisms explaining the unconditional premium's existence.

**(iii) For our seats.** This is `docs/DESIGN.md` §6.2's conditioner: value weight
rises toward the top of its 20–35% range in the spread's top tercile, falls toward
the bottom in the bottom tercile — a quantile rule, never a fixed threshold. The
observable is free and India-constructible: the value composite's own cross-
sectional cheapness-dispersion percentile — the task's "valuation_sentiment" input,
identical to this conditioner. The discipline that must never be violated: the
spread conditions the sleeve's weight **within its frozen range**, never a
standalone timing trade out of equities, never sized off an in-sample threshold —
CPV's own persistence means any India "spread predicts returns" regression must be
Stambaugh-corrected before being trusted, as D02 §6 already requires.

**(iv) Citations.** Cohen, Polk & Vuolteenaho (2003), "The Value Spread," *Journal
of Finance* 58(2):609–641. **[Verified]** Asness, Liew, Pedersen & Thapar, "Deep
Value" (AQR/CEPR working paper, 2017; subsequently published in the *Journal of
Portfolio Management*). **[Verified as an existing AQR/CEPR working paper and
subsequent JPM publication; [VERIFY: exact JPM volume/page]]**

---

### A.5 Migration — where the premium actually comes from

**(i) Mechanism.** A common mistaken model treats the premium as static "cheap
stocks drift up." **Fama & French (2007)** decompose size/value premium sources into
firms that stay in their portfolio all year versus firms that **migrate** across
portfolios between formation dates. The result: a material share of HML's return
comes from **convergence** — cheap firms re-rating and migrating toward
growth/neutral (price rose, or acquired), expensive firms disappointing and
migrating down — not from a static "hold cheap and drift" mechanism. Value-stayers
still slightly outearn growth-stayers, but this residual is smaller than the
migration component.

**(ii) Formal structure.** Partition rebalance-to-rebalance return into "stayers"
(same size/B-M bucket) and "migrators," attributing aggregate HML return to each
group and migration direction. FF2007's headline: migration, not the stayers'
differential, dominates both the size and value premium.

**(iii) For our seats.** Direct implication for rebalance cadence (D02 §4's
semi-annual, NSE-index-aligned reconstitution): if the premium is substantially
convergence, turnover discipline is part of **how the sleeve harvests it at all** —
an overly wide no-trade band caps the very mechanism generating the return. This is
a second, independent reason (beyond CONTRACT Known Prior #7's restatement bias) a
**price-only-majority** value composite beats a book/earnings-heavy one in India:
migration is detected fastest through price/shares-outstanding data (free,
point-in-time), while fundamentals-heavy signals migrate a bucket only as fast as
restated financials arrive.

**(iv) Citation.** Fama & French (2007), "Migration," *Financial Analysts Journal*
63(3):48–58. **[Verified — published in the Financial Analysts Journal, not JFE]**

---

### A.6 Quality — the other side of value, and what "good" is made of

**(i) Mechanism.** If cheapness alone were sufficient, the cheapest decile would win
outright; it does not, because much "cheap" is cheap for a reason. **Novy-Marx
(2013)** shows gross profitability (gross profits/assets) predicts returns with
"roughly the same power" as B/M, and profitable firms earn **higher** returns
despite lower B/M and larger size — profitability as **"the other side of value"**:
controlling for it improves value-strategy performance, especially among large,
liquid names. **Asness, Frazzini & Pedersen's QMJ** generalizes this into four
pillars — **profitability** (gross profits/assets, ROE, ROA, cash-flow/assets, gross
margin, cash-share of earnings), **growth** (growth in each profitability measure),
**safety** (low leverage, low bankruptcy risk, low earnings/return volatility), and
**payout** (buybacks, low net issuance) — and shows a long-quality/short-junk factor
earns significant risk-adjusted returns in the US and 24 countries; high-quality
stocks trade only modestly rich to what their quality justifies — the market
**underprices** quality (peer-reviewed 2019, after a working-paper history from
2013, with a substantively revised 2018 draft). **Sloan (1996)** supplies an
earlier, narrower quality mechanism: earnings driven by **accruals** are less
persistent than earnings driven by **cash flow**; investors fixate on aggregate
earnings and overweight the accrual component, so low-accrual firms subsequently
outperform high-accrual firms — the same extrapolate-the-wrong-thing failure as
A.2, applied to earnings composition. **Piotroski (2000)** shows quality's most
load-bearing use is **inside** value: restricted to the top B/M quintile, a
9-signal F-Score separates future winners from losers — F-Score 8–9 beats the
market by +7.5%/yr, 0–1 lags by −8.3%/yr, long-high/short-low earned 23%/yr,
1976–1996 (pre-cost) — a **value-trap screen**, not a standalone factor.
**Campbell, Hilscher & Szilagyi (2008)** close the loop on leverage/distress: since
1981, financially distressed stocks (a dynamic logit failure-probability model)
deliver **anomalously low** returns despite higher volatility, beta, and size/value
loadings — the opposite of a risk-based prediction, reinforcing quality as
junk-avoidance rather than a restatement of value.

**(ii) Formal structure.** Novy-Marx: `GP/A_i = (Revenue_i − COGS_i)/Assets_i`.
QMJ (schematic): `Quality_i = z(Profitability_i) + z(Growth_i) + z(Safety_i) +
z(Payout_i)`, each pillar a standardized composite, ranked long-short like HML.
Sloan: `Accruals_i = (ΔWC_i − Dep_i)/Assets_i`, sorted into deciles. Piotroski's
F-Score: nine binary signals — profitability (ROA level/change, cash-flow accrual
quality, positive operating cash flow), leverage/liquidity (leverage change,
current-ratio change, no new issuance), operating efficiency (gross-margin and
asset-turnover change) — summed `F ∈ {0,...,9}`, applied **only within** the top B/M
quintile. CHS: a dynamic logit failure score on accounting/market variables,
whose top decile earns significantly lower, not higher, subsequent returns.

**(iii) For our seats.** Direct theoretical basis for the "quality WITHIN value"
architecture: the quality composite (imported QMJ pillars plus India-specific
promoter-pledge and RPT junk terms, D02 §4) runs its own 20–35% sleeve **and**
conditions which cheap names the value sleeve admits, mirroring Piotroski's design
intent. Accruals and distress are each constructible from Indian filing data under
the same lag-buffered, restatement-aware discipline (Known Prior #7) — but CONTRACT
§5 already notes no India-specific Sloan-style test was located; carried as an
**untested cross-country prior**, Tier B at best.

**(iv) Citations.** Novy-Marx (2013), "The Other Side of Value: The Gross
Profitability Premium," *Journal of Financial Economics* 108(1):1–28. **[Verified]**
Asness, Frazzini & Pedersen (2019), "Quality Minus Junk," *Review of Accounting
Studies* 24(1):34–112. **[Verified]** Sloan (1996), "Do Stock Prices Fully Reflect
Information in Accruals and Cash Flows about Future Earnings?," *The Accounting
Review* 71(3):289–315. **[Verified]** Piotroski (2000), "Value Investing...,"
*Journal of Accounting Research* 38 (Supplement):1–41. **[Verified]** Campbell,
Hilscher & Szilagyi (2008), "In Search of Distress Risk," *Journal of Finance*
63(6):2899–2939. **[Verified]**

---

### A.7 Why quality survives — the lottery/agency/limits story

**(i) Mechanism.** Quality's survival argument cannot simply be "the market
underprices profitability" — sophisticated capital should long since have
arbitraged that away. The sharper version extends **Frazzini & Pedersen (2014)
Betting-Against-Beta** to quality directly. BAB's mechanism: leverage- and margin-
constrained investors (pensions, retail, benchmark-constrained funds), unable to
lever a low-risk portfolio to a market-like target, instead reach for return by
overweighting high-beta, lottery-like names — bidding up their price and flattening
the security market line; a BAB factor (long leveraged low-beta, short high-beta,
equal ex-ante vol) earns significant risk-adjusted returns across US and 20
international equity markets and other asset classes. Extended to quality: the same
constrained investors overpay for expensive, glamorous, high-growth-narrative names
as their un-leverable substitute for return, systematically underpricing boring,
profitable, safe compounders. This is CONTRACT §5's category **(iv)** — an
institutional constraint, not an informational gap — durable precisely because it
needs the marginal investor to stay leverage-constrained, a standing feature of
institutional management, not a fact that erodes once published.

**(ii) Formal structure.** BAB weights: `w_i ∝ 1/β_i`, rescaled so long/short legs
carry unit ex-ante beta at formation, self-financing in beta-adjusted terms. The
effect strengthens where funding constraints bind hardest. The quality extension
(argued, not separately estimated): a parallel `w_i ∝ Quality_i`-tilted position
should earn disproportionately where benchmark-relative, unlevered mandates dominate
the marginal buyer.

**(iii) For our seats.** D02's India evidence directly corroborates this rather than
merely importing it: **Agarwalla, Jacob, Varma & Vasudevan (2014)** find India's
BAB factor dominates size, value and momentum, but its CAPM-adjusted premium is
**largely explained once a profitability/quality factor is added** — India's
low-beta effect looks like a quality effect in beta's clothing, mirroring Asness-
Frazzini-Israel-Moskowitz-Pedersen's "size matters, if you control your junk" in
reverse. This is the strongest India-specific link tying A.6's quality construct to
A.7's institutional-constraint story, and argues for treating the quality sleeve's
floor (binding tighter in late-cycle/credit-stress states) as resting on genuinely
structural ground — leverage aversion among India's own institutions — not a
temporary informational edge crowding could erode on a predictable timetable.

**(iv) Citations.** Frazzini & Pedersen (2014), "Betting Against Beta," *Journal of
Financial Economics* 111(1):1–25. **[Verified]** Agarwalla, Jacob, Varma &
Vasudevan (2014), "Betting Against Beta in the Indian Market," IIMA WP2014-07-01 /
SSRN 2464097. **[Verified per D02]**

---

### A.8 The value-momentum interaction — why it matters more for a long-only book

**(i) Mechanism.** **Asness, Moskowitz & Pedersen (2013)** document a surprising
cross-asset fact: value and momentum returns correlate **more** strongly with each
other across eight markets/asset classes than passive exposure to those markets
does, yet **within** each market, value and momentum are **negatively** correlated.
The mechanism is a difference in horizon and leg composition: value is, loosely,
long the **losers** momentum's own formation window has just punished (deep
cheapness typically follows poor recent performance), while momentum is long recent
**winners** — so a stock momentum flags short is often simultaneously flagged cheap
by value, and vice versa. The two bet on the **same reversal-versus-continuation
tension at different horizons**: momentum captures intermediate (3–12mo)
continuation before it reverses; value captures the longer-horizon reversion once
extrapolation errors correct — generating negative period-by-period correlation
without either factor being individually mispriced or redundant.

**(ii) Formal structure — the combination math.** For two zero-cost strategies with
Sharpe ratios `SR₁, SR₂` and correlation `ρ`, the optimally-weighted combination's
maximum Sharpe ratio follows from mean-variance algebra (`SR_p² = μ'Σ⁻¹μ`, two-asset
case): `SR_p² = (SR₁²+SR₂²−2ρ·SR₁·SR₂)/(1−ρ²)`. Any `ρ<1` strictly raises the
combined Sharpe above either alone; **negative** `ρ` is doubly favorable, since it
makes `−2ρ·SR₁·SR₂` positive while the `(1−ρ²)` denominator is unaffected by sign.
At AMP2013's approximate `ρ≈−0.5` with equal `SR₁=SR₂=S`: `SR_p²=(S²+S²+S²)/0.75=4S²`,
so `SR_p=2S` — the combination **doubles** either strategy's Sharpe ratio purely
from the correlation's sign, no change in either expected return required.

**(iii) For our seats.** This matters **more** for a long-only India book than for a
long-short fund: a long-only implementation of value or momentum alone captures only
the long leg, forfeiting the short leg's diversification value — but a **combined**
long-only value/quality book (`docs/DESIGN.md` §6.2) that also runs momentum as a
rank-blended modifier (§6.1: "acts only as a rank tiebreaker... inside the factor
book's quarterly turns") keeps a meaningful share of the negative-correlation
benefit **inside one long-only construction**, using momentum's rank as a tiebreak
among value/quality's admissible names rather than an independent short-eligible
sleeve. This is the specific argument for a momentum modifier despite momentum's own
unattractive turnover economics at scale (D02 §1's Israel-Moskowitz 5× turnover
finding) — the modifier earns its keep on **diversification**, not standalone
expected return, and should be sized and judged against that narrower claim.

**(iv) Citation.** Asness, Moskowitz & Pedersen (2013), "Value and Momentum
Everywhere," *Journal of Finance* 68(3):929–985. **[Verified]**

---

### A.9 Value winters — the anatomy of 1998–2000 and 2017–2020

**(i) Mechanism.** A.4's "spread widens before value's best years" claim is only
credible if the desk confronts the two episodes where the spread widened for years
with no payoff on a comfortable timetable. **1998–2000**: growth/tech multiples
expanded to extremes; a well-known value-oriented holding company underperformed the
Nasdaq by roughly 189 percentage points over a 20-month stretch before the reversal
began, and the Nasdaq's subsequent 77% peak-to-trough collapse (Mar-2000 to Oct-2002)
is the resolution — value's early-2000s outperformance vindicated the spread logic,
but only after a relative drawdown long enough to end most discretionary careers
first. **2017–2020**: value's underperformance became, per Rob Arnott, "the longest
and deepest dry spell for value ever" — a drawdown versus growth of roughly 55% by
mid-2020, running from February 2007, with the MSCI World Growth index beating Value
by roughly 170 points cumulatively 2010–2020 (34 points in 2020 alone) and the
valuation spread reaching its widest since the dot-com peak. **What happened to the
arbitrageurs**: value managers faced severe, multi-year redemption and career-risk
pressure through both episodes — the limits-to-arbitrage mechanism that keeps a
recognized mispricing from correcting quickly, and precisely what Part G must
confront for the humans running this book.

**(ii) The postmortems and the honest resolution.** **Arnott, Harvey, Kalesnik &
Linnainmaa (2021)** address "is value dead" directly, attributing 2017–2020's
underperformance to two sources: classical HML's book-to-price definition
increasingly mismeasures value as **intangible assets** (software, brands, R&D) grow
as a share of true economic value while being expensed, not capitalized, understating
book value more for the intangible-heavy (growth-labeled) firms driving the
divergence; and value's valuation relative to growth had genuinely, severely
cheapened (the spread widening exactly as A.4 predicts precedes strong returns).
Capitalizing intangibles restores a premium much closer to its historical average —
evidence a meaningful share of "value is dead" was a **measurement** problem, not the
phenomenon's death. Value's 2021–2022 recovery, alongside the rate-hiking cycle and
the unwind of extreme growth multiples, is broadly consistent with this diagnosis —
an out-of-sample resolution the earlier debate lacked.

**(iii) For our seats.** The honest summary: value winters are real, multi-year, and
career-threatening — but in both resolved episodes the spread's widening preceded
recovery rather than signaling permanent regime change, the strongest evidence *for*
running a spread-conditioned sleeve through a winter rather than abandoning it. The
intangibles lesson belongs in D02's construction discipline (book-value-only signals
progressively mismeasure an intangible-heavy economy) — but it is also,
uncomfortably, a live illustration of Part G's central risk: a fix proposed **at the
trough**, by researchers invested in value's survival, is a pattern this desk must
distinguish from legitimate progress using a **pre-registration timestamp test**, not
after-the-fact plausibility (G.2 below).

**(iv) Citations.** Arnott, Harvey, Kalesnik & Linnainmaa (2021), "Reports of
Value's Death May Be Greatly Exaggerated," *Financial Analysts Journal* 77(1):44–67.
**[Verified]** Contemporary market-data reporting on the 1998–2000 divergence and
2017–2020 spread/performance figures. **[Verified as existing, widely corroborated
reporting; Tier C for the specific percentages, practitioner/press-sourced rather
than a single peer-reviewed study — [VERIFY: precise single-source 1998–2000
relative-drawdown figures before treating as calibrated rather than illustrative]]**

---

### A.10 Synthesis — mechanism, observable, seat, and the honest gap

| Mechanism | Observable proxy (free India data) | Seat that consumes it | What no free observable captures |
|---|---|---|---|
| Cheapness (Basu, FF92-93) | B/P, E/P (lag-buffered), dividend yield, sales/price | **Value sleeve** (§6.2) | Whether the premium is risk (iii) or extrapolation error (i) — unresolved; sleeve sized for either |
| Extrapolative growth error (La Porta; BGLS) | Trailing realized growth rank (broker forecasts thin in India) | Value's growth-reversion tiebreak (proposed) | No free India consensus-forecast panel; `θ` unestimated on India data |
| Duration/discount-rate (Lettau-Wachter) | Real-rate/credit regressors (practitioner-only) | Candidate regressor only, not a standalone rule | Empirically unstable even in the US; no stable India magnitude |
| Value spread as a state (CPV; Deep Value) | Value composite's own cheapness-dispersion percentile ("valuation_sentiment") | **Value-spread conditioner** (§6.2) | Stambaugh-uncorrected India regression risk; never purged-CV-tested on India's HML |
| Migration/convergence (FF 2007) | Bucket-transition frequency of top/bottom deciles | Justifies semi-annual, NSE-aligned cadence | No India migration-decomposition study; assumed by analogy |
| Quality (Novy-Marx, QMJ, Sloan, Piotroski, CHS) | Gross profitability, ROE/D-E, accrual ratio, F-Score, distress score | **Quality sleeve** + value-trap screen | No India accrual study; India F-Score/CHS tests fragmented, short-sample |
| Institutional-constraint survival (BAB→quality) | AJV-Vasudevan's India BAB, subsumed by quality | Survival argument for quality **and** low-vol | No direct India test of BAB-to-quality; inferred from AJV |
| Value-momentum negative correlation (AMP 2013) | Cross-sectional rank correlation, value vs. momentum, India data | Momentum-as-tiebreak inside the factor book (§6.1) | India's own correlation never directly estimated; imported global prior |
| Value winters (1998–2000, 2017–2020) | Spread-percentile history through the episode | Anti-capitulation lock + spread conditioning (Part G) | No India value-winter of comparable length to study; wholly imported |

**What no free observable captures — stated honestly.** The sharpest gap is
**extrapolative-growth-error** (A.2): its best instrument (consensus long-term
growth forecasts) is exactly what India's free-data constraint cannot supply outside
the most-covered names, leaving a trailing-growth proxy motivated by the same theory
but unverified on India data. The second gap is any **India-specific value-winter
episode**: unlike momentum's two clean India crash observations (2008–09, 2020),
value's multi-year drawdown dynamics rest entirely on imported US evidence — a
genuine Tier-B ceiling on how precisely India's own anti-capitulation drawdown-depth
threshold can be calibrated, addressed only partly by Part G's structural (rather
than magnitude-dependent) countermeasures below.

---

## PART G — Psychology of operating value and quality

Part A describes two mechanisms — cheapness and quality — each defensible under
multiple, sometimes conflicting theories, each capable of being profoundly wrong for
years before the theory justifying it is vindicated. This part maps the two
symmetric operator failure modes value and quality invite — capitulating on value at
its cheapest, overpaying for quality at its safest-looking, most expensive moment —
to the countermeasures this program's governance layer already carries.

### G.1 The career-risk problem — being wrong for five years, correctly

**Mechanism.** A.9 already supplies the material: a correctly specified, correctly
sized value sleeve can underperform for **five or more consecutive years** — both
1998–2000 and 2017–2020 ran roughly that long before resolving in value's favor. The
line usually quoted here — "**markets can remain irrational longer than you can
remain solvent**" — is universally attributed to Keynes, almost certainly wrongly:
the earliest documented instance is financial analyst **A. Gary Shilling**, *Forbes*
"Scoreboard" (15 Feb 1993): "Markets can remain irrational a lot longer than you and
I can remain solvent." Keynes died in 1946; no Keynes-authored source has been
located, and the attribution appears to date only from around 1999, likely conflated
with his genuine, distinct remark that "there is nothing so disastrous as a rational
investment policy in an irrational world." The substance stands regardless of
authorship: real career risk and redemption pressure accumulate every month a
correctly-specified position is underwater, independent of eventual vindication —
value's multi-year underperformance is not a rare tail to plan around, it is the
**expected experience** of running the strategy roughly one decade in a few, per
A.9's own history.

**Countermeasure.** The value sleeve's survival argument (A.1.iii; `docs/DESIGN.md`
§10: "risk premium + extrapolation bias (iii)+(i)") carries a stated, fixed −30–40%
decay haircut applied before any sizing decision — not a number that shrinks further
because the sleeve recently underperformed. The Challenger Protocol (`docs/
PIPELINE.md` §2.11: adaptive rules live in exactly one of {shadow|challenger|
online}; frozen v1 params permanent null; promotion/demotion by pre-registered
criteria, scheduled dates only) is the mechanical answer to the Shilling problem: it
removes the in-the-moment judgment of whether five years of pain means the thesis
broke, or is simply operating on its documented 3–5yr realization horizon (CONTRACT
§1) — decided once, in advance, on a schedule, never live under the pressure
Shilling's line describes.

### G.2 Redefining value at the bottom — capitulation dressed as research

**Mechanism.** A.9 flags the pattern directly: intangibles-capitalization of HML
(Arnott-Harvey-Kalesnik-Linnainmaa 2021) is, on its merits, a genuine improvement —
accounting's treatment of intangibles has drifted from economic reality — but it was
proposed and published near the exact trough of value's worst drawdown, by
researchers invested in value's survival, and its effect is to retroactively
redefine "value" in a way that flatters the strategy's own recent performance.
Neither fact proves bad faith — but the pattern (redefine the measure at the low, in
a direction that flatters the redefiner, using hindsight-only data) is
**indistinguishable, from inside the research process, from legitimate methodological
progress** without a pre-committed discipline separating the two. This is the
highest-stakes trap here, because redefinition pressure arrives disguised as
intellectual honesty — "the old measure was flawed all along" is often *true*, which
is exactly what makes it dangerous to accept uncritically at the bottom.

**Countermeasure.** The distinguishing test is **timing, not merit**: a
methodological change to the value or quality composite is admissible only if
proposed and its adoption criteria pre-registered **before** observing whether it
would help the sleeve's recent performance — the same trial-budget discipline
(CONTRACT §9; `docs/PIPELINE.md` FL7/FL14) applies with added force here, because
the temptation peaks exactly when the existing measure looks most broken. Any
proposed construction change (e.g. an India-specific intangibles adjustment, given
Ind-AS's own treatment of intangibles) must clear the Challenger Protocol on a
scheduled review date **fixed before** the change was conceived, its hypothesis
stated without reference to the sleeve's own recent return. The anti-capitulation
lock (`docs/PIPELINE.md` §2.11: no parameter/budget/structure change may be
*initiated* while the sleeve is beyond a grid-defined drawdown depth) is the blunter
backstop — it does not distinguish good research from capitulation, it simply
forbids *initiating* any construction change mid-drawdown regardless of argument
quality. Executing an already-pre-registered rule (the spread conditioner moving
weight within its frozen range) is always permitted; changing what the composite
**measures** mid-drawdown never is.

### G.3 Quality's opposite trap — paying any price for safety

**Mechanism.** Quality's failure mode mirrors value's and is arguably more
dangerous, because it feels virtuous rather than desperate: at a euphoric top, or a
genuine flight-to-safety episode, "quality" becomes a narrative investors will pay
almost any multiple for, since overpaying for safety *feels* prudent exactly when it
is least so. D02's decay ledger documents a live instance: quality traded over one
standard deviation rich to its own valuation history in H2-2024, then gave that
richness back through 2025's "worst year for international quality relative
performance since 1999," in a "quant unwind" where quality, low-vol, and momentum
crowding unwound together — Arnott-Beck-Kalesnik-West's thesis (a factor's own
re-rating, not a repeatable premium, drives its trailing return) demonstrated live,
not merely argued historically. The mechanism runs opposite G.2's: instead of
redefining a cheap measure to excuse underperformance, the temptation is to pay any
multiple for the compounder on the reasoning "quality always wins eventually" —
treating a well-evidenced long-run tendency as if it holds at any entry valuation,
which none of the cited evidence claims.

**Countermeasure.** The quality valuation kill-switch (`docs/DESIGN.md` §6.2)
answers this directly: quality-sleeve weight is cut toward its floor — never
expanded — when the quality basket's own relative-valuation percentile sits in its
top decile against its 10-year history, mirroring the 2024–25 pattern rather than
waiting for a second live episode to believe it. Per CONTRACT §4's Tier-C
discipline, this kill-switch may only **reduce** risk, never add exposure — the
mirror-image of G.2's lock, serving the same purpose: removing the live judgment
call ("is this the time quality really is worth any price?") from the moment it is
hardest to answer, precisely when the basket is most expensive and the narrative for
paying up most compelling.

### G.4 Institutional procyclicality — Goyal-Wahal applied here

**Mechanism.** G.1 and G.3's individual biases have a direct institutional-scale
analogue. **Goyal & Wahal (2008)** study 3,400 US pension-plan sponsors' manager
hiring/firing, 1994–2003, finding sponsors systematically **hire** after large
positive excess returns and **fire** after underperformance — and in matched
round-trip fire-then-hire comparisons, the switch delivers **no** net benefit versus
staying with the fired manager. Applied here: cutting value's weight, abandoning the
intangibles-vs-classic construction debate mid-episode, or rotating toward whichever
sleeve most recently outperformed — purely *because* value has just underperformed,
with no pre-registered hypothesis — re-enacts Goyal-Wahal internally, with the
identical expected result: no net improvement, paid for in transition cost and a
track record broken exactly when patience was correct.

**Countermeasure.** Identical in structure to the momentum dossier's own treatment
of this paper: reweighting between sleeves happens only via the Challenger Protocol
on scheduled review dates fixed in advance, never in reaction to a recent relative-
performance stretch in either direction. Which sleeve is online, and at what weight,
is itself a pre-registered, dated decision — never a standing discretionary call any
single quarter can trigger.

### G.5 Countermeasures mapped

Four mechanisms already built into the governance layer do the actual work G.1–G.4
require, none asking the operator to be wiser in the moment: **(1) Pre-registration**
(CONTRACT §9; the trial ledger) — every hypothesis about changing the value/quality
construct or reweighting sleeves is dated before its outcome is known, closing G.2's
loophole by construction. **(2) The anti-capitulation lock** (`docs/PIPELINE.md`
§2.11) — no construction/weighting change may be initiated while the sleeve sits
beyond a grid-defined drawdown depth; pre-registered rules always execute. **(3)
Spread-state conditioning instead of abandonment** (A.4; §6.2's conditioner and kill-
switch) — value's weight moves within its frozen range on the spread's own
percentile, quality's cuts toward its floor on its own valuation percentile, both
pre-specified quantile rules, never a live read of "has it stopped working." **(4)
The decay ledger** (§10) — every edge's survival argument and haircut is a written,
dated commitment (value: (iii)+(i), −30–40%; quality: (i)+(iv), −25–35% on the
imported QMJ core), revisited only against its own pre-registered falsifier — never
against recent performance. The ledger is what makes G.1's five-year wait
survivable in institutional terms: the haircut was set once, in writing, and only a
pre-specified test failing can move it.

### G.6 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Career-risk capitulation on value | Value's 3–5y horizon collides with real career/redemption risk (Shilling's line, misattributed to Keynes) | Fixed decay haircut + Challenger Protocol scheduled review — judgment made once, in advance |
| Redefining value's measure at the bottom | A genuine fix (intangibles) proposed at the exact trough is indistinguishable from capitulation dressed as research | Timing-based admissibility test (pre-registered before observing performance impact); anti-capitulation lock forbids initiating construction changes mid-drawdown |
| Paying any price for quality at a euphoric top | Quality "feels" prudent to overpay for; 2024–25 shows re-rating, not premium, drove the return | Quality valuation kill-switch — reduce-only, on the basket's own valuation percentile |
| Institutional sleeve-chasing after under/over-performance | Goyal-Wahal: hire-after-outperform/fire-after-underperform, no net benefit | Sleeve/weight changes only via Challenger Protocol, pre-fixed dates |
| Treating the unresolved risk-vs-behavioral debate (A.1) as settled | Both readings remain live; sizing that assumes one is fragile if wrong | Sleeve carries both survival categories simultaneously; drawdown tolerance not conditioned on which story the operator believes |
| Ignoring the valuation state because "it still backtests well" | CPV and the 2024–25 quality episode show the state is measurable and current | Spread conditioner and kill-switch are standing, reduce/reweight-only, independent of trailing Sharpe |

None of these six countermeasures asks the operator to be braver, wiser, or more
patient than Part A's evidence justifies. Each converts a live judgment call — hold
through year four of a value drawdown, accept a flattering redefinition of
cheapness, pay up for a compounder because it feels safe, fire the sleeve that just
underperformed, pick a side in an unresolved debate, or dismiss a valuation-state
signal because the backtest still looks fine — into a structural non-decision, made
once, in writing, before the moment that would have made it hardest.


---

# PART B — The evidence record (global + India)

# PART B — The Evidence Record: Global and India

*Value/quality monograph · Part B of the deep-dive · v1.0 · 2026-09-01 · Author: Claude (research
agent) for Ionic quant desk (principal: gaurav@ionic.in)*
*Governed by `research/CONTRACT.md`. Every number below is search-verified as of Sept 2026 unless
tagged `[VERIFY: ...]`. Deepens `research/dossiers/02-value-quality-lowvol.md` ("D02 dossier"),
which this Part re-derives and extends rather than repeats. Style and evidentiary discipline follow
`research/cycles/momentum-deep/partB-evidence.md` ("momentum Part B") — the same numbers-forward,
[VERIFY]-flagged standard, applied here to value and quality. The desk holds a GitHub-mirrored copy
of the IIM-Ahmedabad monthly factor library at `ingest/vault/factors/iima_monthly_factors.csv`
(schema confirmed this session: `Date, SMB, HML, WML, MF, RF`, monthly, 1993-10 through 2025-12,
387 data rows) — per instruction, this Part references that the series **exists** and cites its
**published** statistics (Agarwalla-Jacob-Varma's own reported figures) without independently
recomputing HML/SMB summary statistics from the file; the desk computes those itself in the data
phase.*

---

## B1. Global evidence in specification detail

### B1.1 Fama & French (1992) — the value/size result that started the literature

**"The Cross-Section of Expected Stock Returns,"** *Journal of Finance* 47(2):427–465. Sorting NYSE,
AMEX and NASDAQ stocks on market equity and book-to-market equity jointly, Fama & French show that
**size and book-to-market absorb essentially all of the cross-sectional variation in average returns
that a CAPM beta sort captures** — once portfolios are formed on size and B/M, the beta-return
relation goes flat: within a size/B/M bucket, high- and low-beta stocks earn statistically
indistinguishable average returns. This is the direct empirical motivation for treating size and
value, not beta, as the priced characteristics — the foundation on which every result in this Part
sits. Verified (near-universally cross-cited; Wiley/JSTOR listing).

### B1.2 Fama & French (1993) — HML and SMB, construction in exact detail

**"Common Risk Factors in the Returns on Stocks and Bonds,"** *Journal of Financial Economics*
33(1):3–56. This is the industry-standard reference construction against which every subsequent
value-factor implementation (including India's) is measured. **Universe:** NYSE, AMEX and (from
1972) NASDAQ non-financial common stocks. **Breakpoints:** an **independent 2×3 sort** — size split
at the **median NYSE market-equity** (Small/Big), and book-to-market split at the **30th and 70th
NYSE percentiles** (Low/Medium/High), giving six value-weighted portfolios at the intersections.
Firms with **negative book equity are excluded** from the B/M breakpoints and portfolios entirely.
**Timing convention — the detail that matters most for any replication:** book equity is measured at
the **fiscal year-end of calendar year t−1**; market equity for the B/M ratio is measured at the
**end of December of year t−1**; portfolios are formed in **June of year t** and held through **May
of year t+1** — a deliberate **minimum 6-month gap** between the fiscal-year-end accounting data and
the portfolio-formation date, designed to ensure the accounting information was public knowledge
before it is traded on. **Factor construction:** `HML = ½(Small High + Big High) − ½(Small Low + Big
Low)` — the average return on the two high-B/M ("value") portfolios minus the average on the two
low-B/M ("growth") portfolios; `SMB` is built the complementary way, averaging across the B/M
dimension and differencing across the size dimension. **Sample and magnitude:** July 1963–December
1991 in the original paper (the pre-1963 book-equity data being of lower quality); both SMB and HML
carry positive, statistically significant average monthly returns over this window, with HML the
economically larger of the two `[VERIFY: this Part could not independently confirm the paper's exact
Table 1 monthly-average figures (widely cited informally as roughly 0.4–0.5%/month for HML) against
a primary-source table in this search pass — the construction details above are independently
confirmed from multiple sources, but the precise 1963–1991 magnitude should be checked directly
against the JFE table before being used for sizing]`. The full monthly series, independently
confirmed this session from a live GitHub-mirrored copy of Ken French's own file text (see side-task
section), now runs from **1926-07** to the present, revised on every CRSP database-vintage refresh —
small (typically <0.01 percentage-point) revisions appear across vintages, a fact worth carrying into
any point-in-time discipline for a replicated India series, exactly as the momentum Part B notes for
the momentum factor built from the same underlying files.

### B1.3 Fama & French (1998) — international value, the first global test

**"Value versus Growth: The International Evidence,"** *Journal of Finance* 53(6):1975–1999. Tests
value strategies (B/M, E/P, cash flow/price, dividend yield) in **13 major developed markets**,
1975–1995. **Headline magnitude:** the difference between average returns on **global** portfolios of
high- and low-book-to-market stocks is **7.68%/year** over the sample. **Breadth of the result:**
value beats growth in **12 of the 13 countries** tested; across all three of the B/M, E/P and C/P
sortings, **12 of 13 country-level value-minus-growth premiums are positive**, and **most exceed
4%/year**. **The theoretical punchline:** an international CAPM **cannot** explain the premium, but a
**two-factor model with an added relative-distress risk factor** captures it reasonably well across
markets — i.e., as early as 1998 the leading explanation on offer was a compensated-distress-risk
story, not a behavioral one, a framing this Part revisits in B1.9's Cohen-Polk-Vuolteenaho discussion
and in the D02 dossier's own "risk vs. behavioral" survival-argument split. Verified.

### B1.4 Asness, Moskowitz & Pedersen (2013) — *Value and Momentum Everywhere*

**Scope.** *Journal of Finance* 68(3):929–985. Value and momentum estimated side by side in **eight
markets and asset classes**: individual stocks in four regions (US, UK, continental Europe, Japan),
plus **equity index futures across countries, government bonds, currencies, and commodity futures**
— the broadest simultaneous cross-asset value test published to that date. **The central finding for
this monograph:** value strategies earn significant positive average returns in **every one of the
eight markets/asset classes tested**, and — the counter-intuitive part already documented in the
momentum Part B — value and momentum are **negatively correlated with each other, both within and
across markets**, more reliably than either factor is positively correlated with itself across
unrelated asset classes. **The magnitude, flagged exactly as the momentum Part B flagged it:**
secondary sources converge on describing the within-asset-class value-momentum correlation as
averaging **≈−0.49**, with the individual-stock-only figure around **≈−0.60** `[VERIFY: the exact
Table 6 correlation coefficient(s) — this Part, like the momentum Part B before it, could not
independently fetch the primary JFE table or the AQR-hosted replication dataset in this session
(aqr.com is outside the GitHub-only reachable host set); the -0.49/-0.60 range is corroborated across
multiple independent secondary descriptions but not confirmed against the primary table itself]`.
**Mechanism.** The paper rationalizes the common structure via a three-factor model in which a
**global funding-liquidity risk factor** is a partial common driver: when funding is tight, value
(long illiquid, cheap, often recently-battered names) suffers while momentum (long recent winners,
typically more liquid, better-funded names) is relatively protected, and vice versa. **Sleeve
implication, directly load-bearing for B4 below:** because the correlation is negative and robust
across markets, a **combined value+momentum sleeve diversifies far better than either factor's own
volatility would suggest** — independent confirmation, from the value side, of exactly the same
architecture point the momentum Part B derived from the momentum side.

### B1.5 Israel & Moskowitz (2013) — value's size dependence, decomposed

**"The Role of Shorting, Firm Size, and Time on Market Anomalies,"** *Journal of Financial Economics*
108(2):275–301. Decomposes size, value and momentum premia into **long** and **short** leg
contributions across **86 years of US equity data** plus **~40 years across four international
markets and five asset classes**. **Decomposition:** long positions account for **almost all of the
size premium, ~60% of the value premium, and about half of the momentum premium** — value sits
between size (almost purely a long-side effect) and momentum (roughly balanced) in how much its
measured spread depends on the short leg. **The headline finding for value's capacity, and the one
this monograph leans on hardest:** the **value premium decreases with firm size and is weak among
the largest stocks**; shorting becomes **more important for value as firm size decreases** (i.e., the
short leg matters most for value precisely in the small-cap segment where shorting is hardest to
implement in practice) — a structurally different, and less favorable, capacity profile than
momentum's own finding (B1.4 of the momentum Part B) that momentum shows **no reliable relation with
size**. **Direct design consequence:** unlike momentum, which the momentum monograph argues can be
run across the full NIFTY 750 breadth on the size evidence alone, **value's edge should be expected
to concentrate below the largest-cap names** — consistent with the D02 dossier's own observation that
Novy-Marx's profitability overlay "materially improves value-strategy performance, especially among
large, liquid stocks," i.e., value alone fades in mega-caps but a quality-conditioned value strategy
holds up better there. Verified.

### B1.6 The post-2007 US value drought and the 55% drawdown

**Arnott, Harvey, Kalesnik & Linnainmaa (2021), "Reports of Value's Death May Be Greatly
Exaggerated,"** *Financial Analysts Journal* 77(1):44–67 (SSRN 3488748). **The anchor number:** value,
as defined by the classic Fama-French HML factor, **underperformed growth from 2007 through mid-2020,
producing a drawdown of −55%** — as of June 2020, **the largest HML drawdown since the factor's July
1963 inception**, a genuinely unprecedented event by its own 57-year track record, not merely "a bad
decade." **Two candidate explanations, both examined by the same paper:** (1) classical HML's
book-value-to-price definition **fails to capture increasingly important intangible assets** (R&D,
brand, software, network effects) that never appear as book equity under US GAAP, mislabeling
asset-light "growth" firms as expensive relative to a fuller book-value measure; (2) **valuations of
value stocks relative to growth simply tumbled** — the value spread widened to historic extremes,
independent of any measurement question. The authors **capitalize intangibles** into an adjusted
book-value measure that **outperforms traditional HML by a wide margin** over the drawdown window,
and a return decomposition shows the **change in the valuation spread explains the entire drawdown,
with room to spare** — value did *not* die, it got dramatically *cheaper* relative to growth, which
by Cohen-Polk-Vuolteenaho logic (B1.7 below) is precisely the condition under which a subsequent
recovery becomes more, not less, likely.

### B1.7 The "reports of value's death" debate — both sides, specifically

The debate is not simply "for" or "against" value's survival; it is a genuine methodological
disagreement about **how much weight the intangibles-mismeasurement explanation deserves**, even
among researchers who agree on the proximate, valuation-spread-widening mechanism. **Side one — the
mismeasurement camp:** Arnott-Harvey-Kalesnik-Linnainmaa (B1.6 above) show the intangible-adjusted
HML measurably resurrects a chunk of the "lost" premium, implying classical HML is a
systematically-biased instrument in an economy with more intangible capital than in 1963–1990.
Independent, practitioner-side corroboration comes from **Sparkline Capital's "Intangible Value"**
research program (Kai Wu), which builds investable products around intangible-capitalized value
measures on the same premise. **Side two — the valuation-spread-is-the-whole-story camp:** **Israel,
Laursen & Richardson (2020), "Is (Systematic) Value Investing Dead?"** (AQR, published April 2020,
summarized by Asness May 2020) run the **same kind of return decomposition** and reach a materially
narrower conclusion: **intangibles are *not* the primary reason for value's underperformance** — the
dominant driver is the **valuation-spread widening itself**, a conclusion that converges with
Arnott et al.'s own decomposition finding (both teams find the spread-widening term dominates) while
explicitly **downplaying** the incremental explanatory power of the intangibles adjustment relative
to how much weight the "reports of value's death" narrative (and, to a real but lesser degree,
Arnott et al.'s own framing) had assigned it. **Synthesis:** both camps agree the proximate cause of 2007–2020's drawdown was a historic widening of
the cheap-versus-expensive valuation gap, not extinction of the premium; they disagree only on how
much of that widening reflects a fixable measurement flaw in book-to-price versus a real repricing a
correctly-measured HML would have suffered too. **Consequence (anticipating B4):** blend a *majority*
multiple that is less intangible-sensitive (E/P, CF/P) with a *minority* intangible-aware adjustment
where cheaply constructible, rather than betting the whole sleeve on either camp being fully right.

### B1.8 The post-2020 recovery, in numbers

**The single-day catalyst.** **9 November 2020** — the day Pfizer announced successful vaccine trial
results — produced **one of the largest single-day rotations from growth/momentum into value on
record**: the iShares Russell 1000 Value ETF jumped **over 6% intraday**, closing **up over 4%**;
Amazon (a lockdown beneficiary) **fell 5%** the same day while Vornado Realty Trust (battered
commercial real estate) **jumped 27%**. **The week.** For the week ending 13 November 2020, the
Russell 1000 Value index gained **5.6%** versus a **−1.3%** loss for the Russell 1000 Growth index —
a **6.9-percentage-point** weekly spread, **the widest weekly value-over-growth spread since the
dot-com bubble of 2000**. **The month.** The Russell 2000 (small-cap, value-tilted by construction
relative to large growth) rose **over 20% in November 2020**, on pace for **its best month ever**.
**The 2022 sequel, and its own reversal — the honest caveat this Part must attach.** Value's recovery
was not a smooth, one-way normalization: the **Russell 1000 Value beat the Russell 1000 Growth by 22
percentage points in calendar 2022** (a genuine, rate-hike-driven value renaissance — higher discount
rates compress long-duration growth cash flows disproportionately), **but Growth then beat Value by
23 percentage points in 2023**, essentially **erasing** the entire 2022 gap. **The value-spread
context.** A hypothetical, industry- and dollar-neutral, all-country value portfolio's own cheapness
was at the **94th percentile** by the end of 2022, and multiple sources place a similar reading in
the **95th percentile** by mid-2024 — i.e., even after the sharp 2020–2022 recovery, value in
aggregate remained (on this measure) close to the historic cheapness extremes last seen at the very
dot-com peak this Part's B2 case study covers, which is itself the Cohen-Polk-Vuolteenaho-style signal
(D02 dossier §1) that further mean-reversion potential remained even after the initial snap-back.
**Lesson:** the post-2020 recovery confirms HML's crash-and-rebound is genuinely two-sided, but the
2022→2023 whipsaw is direct, recent, walk-forward evidence that **a single strong year of value
outperformance does not validate a "value is back" thesis on its own** — the discipline the
value-spread conditioner (D02 dossier §4) is designed to enforce mechanically rather than by narrative.

### B1.9 Quality — Novy-Marx (2013), the "other side of value"

**"The Other Side of Value: The Gross Profitability Premium,"** *Journal of Financial Economics*
108(1):1–28. **Construction.** Gross profitability = (Revenue − Cost of Goods Sold) / Total Assets,
tested July 1963–December 2010 (AMEX inclusion from 1962, accounting data lagged to end-June of the
following year — the same 6-month convention as HML). **Magnitude:** the most profitable quintile
earns average returns **0.31%/month** higher than the least profitable quintile; a gross-profitability
long-short strategy (labeled HML9GP in some formulations) generates excess average returns of
**0.54%/month** (t-statistic 5.01) — **comparable in magnitude to the value premium itself**, despite
profitable firms tending to have **lower** book-to-market and **larger** market capitalization than
unprofitable firms (i.e., gross profitability and value are close to orthogonal characteristics, which
is exactly why combining them — the QARP logic of B1.11 below — adds rather than duplicates
information). **The paper's own framing, load-bearing for the "quality at a reasonable price"
literature:** profitable-but-expensive firms are **"the other side of value"** — good, growing
businesses the market prices richly for good reason, and controlling for profitability **materially
improves value-strategy performance, especially among large, liquid stocks** — the direct mechanism
behind B1.5's observation that a quality overlay is what keeps a value tilt working in the largest-cap
segment where naive HML fades.

### B1.10 Quality — the wider profitability/accruals/F-Score literature, magnitudes

**Sloan (1996), "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows about Future
Earnings?"** *The Accounting Review* 71(3). **Mechanism:** earnings driven by accruals are less
persistent than earnings driven by cash flow; investors naively fixate on the earnings number without
decomposing it, over-extrapolating the accrual-driven component. **Magnitude:** a hedge portfolio long
low-accrual firms and short high-accrual firms earns **approximately 10–12%/year** in the classic
1962–1991 sample (a commonly-cited first-year abnormal return of **10.4%**, with some accrual-measure
variants running as low as **10.4%** and as high as **~18%/year** depending on whether the accrual
definition is Sloan's original current-net-operating-assets change or a broader non-cash
net-operating-assets change) — a genuine, well-replicated behavioral anomaly, not a risk-based
finding, and one of the cleanest single-mechanism stories in the whole quality literature. **Piotroski
(2000), "Value Investing: The Use of Historical Financial Statement Information to Separate Winners
from Losers,"** *Journal of Accounting Research* 38 (Supplement) — already anchored in the D02
dossier: among **high-B/M (value) firms specifically**, a 9-signal fundamental F-Score separates
future winners from losers — F-Score 8–9 beats the market by **+7.5%/yr**, F-Score 0–1 lags by
**−8.3%/yr**, and a long-high/short-low F-Score strategy earned **23%/yr, 1976–1996** (pre-cost). The
critical framing point, repeated here because it governs how this desk should use F-Score: **it is a
conditioning overlay on value (a value-trap screen), not a standalone factor** — it adds the most
value precisely where naive value is weakest (avoiding "cheap for a reason" firms), which is exactly
the large-cap-fade problem B1.5/B1.9 describe from a different angle. **Ball, Gerakos, Linnainmaa & Nikolaev (2016), "Accruals, Cash Flows, and Operating Profitability in
the Cross Section of Stock Returns,"** *JFE* 121(1):28–45 — **the strongest version of the
profitability signal.** Their **cash-based operating profitability** measure (profitability purged of
the accrual component Sloan identified) **outperforms gross profitability, accrual-inclusive
operating profitability, and net income** as a return predictor in the 1963–2014 US sample, and
**subsumes/absorbs the accrual anomaly** rather than sitting alongside it — close to a unification of
Novy-Marx and Sloan into one characteristic. An investor gains more Sharpe-ratio improvement from
adding **just** cash-based profitability than from adding **both** a separate accruals factor and an
accrual-including profitability factor `[VERIFY: the exact incremental-Sharpe/return-spread magnitude
was not confirmed against the primary JFE table; the qualitative findings are corroborated across
multiple secondary sources]`. **Design consequence:** an India-tailored quality sleeve should lead
with a **cash-flow-based** operating-profitability measure over an accrual-inclusive one — aligning
with the D02 dossier's "price-only-plus-lag-buffered-fundamentals" preference, since cash-flow-
statement data is less exposed to the RPT-driven earnings-management channel B3 documents.

### B1.11 Quality Minus Junk — the global 24-country table, and the QARP literature

**Asness, Frazzini & Pedersen (2019), "Quality Minus Junk,"** *Review of Accounting Studies*
24(1):34–112 — already anchored in the D02 dossier as a Tier-A global finding. **The table detail
this Part adds:** QMJ earns a risk-adjusted return of **0.66%/month in the US** and **0.45%/month
Global**; the factor is positive (mostly significant) in **23 of 24 countries**, ranging from
**0.20%/month in Spain** to **1.02% in Hong Kong** and **1.06% in Greece** — broad international
coverage, roughly double Fama-French 1998's 13-country value test (B1.3), with a more uniformly
positive hit rate. **The mispricing framing, distinct from value's risk-premium framing:**
high-quality stocks trade only modestly rich relative to their quality — the market appears to
genuinely **underprice** quality, a behavioral explanation the D02 dossier already flags as weaker
than value's more defensible distress-risk story. **QARP — combining the two.** The concept traces at
least to **Graham & Dodd (1934)**'s dictum that "investment must always consider the price as well as
the quality of the security." The QMJ paper's own finding: **the price of quality varies over time,
and a low price of quality predicts a higher future QMJ return** — the quality-side analogue of
Cohen-Polk-Vuolteenaho's value-spread-predicts-returns finding, and the mechanism already built into
the D02 dossier's "quality valuation kill-switch." The **Xtrackers Russell 1000 QARP ETF** explicitly
tilts toward value within a quality-screened universe — unusual among quality products, most of which
carry an implicit growth tilt — confirming combining both characteristics is a recognized product
category, not merely academic.

---

## B2. Value winter case studies

Each case: the setup, the drawdown's numbers, the capitulation (where one occurred), and the payoff.

### 1. United States, 1998–2000 — the dot-com value winter, LTCM and Tiger's capitulation

**Setup.** By 1998, value managers were positioned in "old economy" cyclicals and financials, cheap
on every classical multiple, while technology and internet names ran to valuations classical value
metrics had no framework for. **The 1998 quant shock.** Russia's August 1998 devaluation/default
triggered correlated de-leveraging that punished **Long-Term Capital Management**, which **lost 44%
of its value in August 1998 alone** en route to its Fed-brokered wind-down — not a value fund, but a
canonical illustration of the liquidity-spiral mechanism Asness-Moskowitz-Pedersen (B1.4) later
formalize as a common driver of value's crash risk. **Tiger Management's capitulation.** Julian
Robertson's Tiger, running large value-oriented, short-technology positions, absorbed a **~$600
million loss on Russian ruble debt** in August 1998, then kept losing as the bubble inflated against
its short book: by August 1999 Tiger was down **~13% YTD**, over **$1 billion on ~$12 billion in
assets**, and — after **~$7.7 billion** of redemptions — **closed and returned all outside capital in
March 2000**, weeks before NASDAQ's peak. **The payoff, 2000–2002.** The technology drawdown that
followed (NASDAQ fell over 75% by October 2002) coincided with a multi-year value resurgence as
shunned "old economy" cash-generators re-rated sharply — the textbook Cohen-Polk-Vuolteenaho pattern
(B1.6/B1.8): the value spread reached dot-com-era extremes comparable to those repeated in 2020–2022,
and the payoff followed on schedule. **Lesson.** Well-resourced value investors capitulated at close
to the point of maximum opportunity, not because their thesis was wrong but because the drawdown
exceeded what their capital base could sustain — a direct argument, alongside B1.8's 2022→2023
whipsaw, for a mechanical spread-percentile sizing rule over discretionary capitulation-and-re-entry.

### 2. United States, 2017–2020 — the deepest HML drawdown on record

**The numbers, already anchored in B1.6/B1.7 above, restated as the case study's core facts.** HML
fell **−55%** from 2007 through mid-2020, the **largest drawdown in the factor's 57-year history** at
that point; over the narrower **January 2017–August 2020** window specifically, the Fama-French small
value research index returned **−13%** cumulatively while the Fama-French small growth research index
returned **+71%** — an **84-percentage-point** gap concentrated in a single technology- and
mega-cap-platform-driven bull run. **The debate this drawdown spawned** is documented in full in
B1.7: whether the drawdown reflects (i) a genuine, permanent mismeasurement of value under an
intangibles-heavy economy (Arnott-Harvey-Kalesnik-Linnainmaa; Sparkline Capital), (ii) a real but
ordinary (if extreme) valuation-spread widening that both camps' own decompositions identify as the
dominant proximate driver (Israel-Laursen-Richardson downplaying the intangibles-specific
explanation, while agreeing on the spread-widening mechanism), or (iii) — the possibility neither camp
fully resolves — a **structural** shift favoring long-duration, platform/network-effect businesses
under a multi-decade falling-and-then-zero-rate regime that a valuation-spread reading alone cannot
distinguish from ordinary mean-reverting cheapness until the regime itself changes (rates rising
again from 2022 is the natural test, and B1.8's 2022 value rebound followed by 2023's reversal is
consistent with regime-dependence rather than a clean resolution either way). **The Nov-2020
resolution, in numbers, restated from B1.8:** the 9 November 2020 vaccine-announcement rotation (R1000
Value +6% intraday), the 6.9pp weekly value-over-growth spread (widest since 2000), and the Russell
2000's best-ever monthly gain mark the point at which the drawdown's *duration* record was not
matched by a *permanent* verdict on value's survival — but the 2022→2023 whipsaw (B1.8) is direct
evidence that the resolution is not yet clean even six years after the drawdown's trough. **Lesson.**
This is, by a wide margin, the single most important case study for calibrating any value-spread-based
sizing rule: a rule that had "capitulated" on value at any point in 2019 or early 2020 (as many
discretionary and even systematic managers reportedly did, per the "value is dead" commentary wave
that peaked in exactly this window) would have missed essentially the entire subsequent recovery.

### 3. Japan — the long, good record, and the mirror image of momentum's problem

Japan is the standard exhibit **for** value's universality, the mirror image of its role as the
standard exhibit **against** momentum's universality in the momentum monograph (momentum Part B,
B1.7). **The long-run record.** Value has been the better-performing style in Japan for roughly **the
past three decades**: the MSCI Japan Value index is up **356.70%** since 1995 versus **113.72%** for
the MSCI Japan Growth index (local currency terms) — value outperforming growth by more than **three
to one** cumulatively over the period, a materially wider and more persistent gap than the US
experience over the same three decades. **The one interruption.** Japan saw a **decade-long stretch
of value underperformance following the 2009 Global Financial Crisis**, echoing (with a lag) the US's
own post-2007 pattern — but even through that stretch, the Japanese value strategy is reported to have
"comfortably outperformed" the TOPIX over the full multi-decade window, i.e., the interruption did not
erase the long-run record the way the US's 2007–2020 drawdown came close to threatening. **The recent
reversal, sharply.** Over the most recent five years (through 2026), **value has outperformed growth
in Japan by an extraordinary 19.4%/year annualized** — one of the largest sustained value-over-growth
gaps in any major developed market in this Part's evidence base, plausibly connected to the same
governance-reform tailwind (Tokyo Stock Exchange's 2023 push for listed companies to address
persistent below-book-value valuations) that is separately reshaping Japanese equity markets more
broadly. **Why this matters for the desk beyond curiosity value:** where momentum's Japan result
(near-zero standalone Sharpe, per Asness 2011) is best read, per the momentum Part B, as "a lower-tail
draw within a known [negative value-momentum correlation] distribution" that argues **against**
running momentum in isolation from value, Japan's *value* record is closer to the opposite lesson:
**value's own long-run persistence does not require the US's specific post-2007 experience to
generalize** — a market with a genuinely different multi-decade macro regime (three-plus decades of
near-zero rates, a famously conservative, cash-hoarding corporate sector, low intangible-asset
intensity relative to the US technology sector) produced one of the cleanest, longest value premia in
the developed world, which is independent corroboration that value's underperformance in the US
2007–2020 window is more plausibly a market/regime-specific episode than a universal structural break
in the value premium itself.

### 4. India, 2017–2019 — the quality-growth mania and the smallcap crash

**Setup — the two, simultaneous, opposite-direction India stories.** From January 2018, the Nifty 50
grew roughly **4%** while, over the same window, the **Nifty Midcap 100 fell ~19%** and the **Nifty
Smallcap 100 fell ~32%** — an enormous divergence in narrow large-cap breadth terms. Over the fuller
**January 2018–August 2019** window, the broad small-cap index is reported to have fallen **~40%**;
calendar-2019 alone added a further **8.5% loss for the Nifty Smallcap 250**. **The proximate triggers,
mostly non-fundamental and India-specific — a genuinely distinct mechanism from any of the US/Japan
cases above.** SEBI's **October 2017** mutual-fund re-categorization circular barred large- and
mid-cap schemes from holding small-cap names, forcing structural selling; NSE's **April 2018**
reconstitution of the Nifty Midcap 100 excluded **46 of the prior 100 constituents**, another
structural, non-fundamental supply shock; then, in **September 2018**, the **IL&FS default** (a major
infrastructure-financing NBFC) triggered a sector-wide NBFC credit crunch and liquidity scare that hit
small/midcap financials and their borrowers hardest — NBFC-sector stocks in the crisis's initial shock
window **fell over 40% in a single day** in some cases. **The mirror-image quality-growth mania,
concurrently.** While small/midcaps were being structurally and fundamentally battered, "quality"
large-cap FMCG names ran to valuations **not seen since the dot-com bubble**: by mid-2018, India's top
consumer-goods makers traded at nearly **48x earnings**, up from **41.2x** at end-March 2018, with a
typical FMCG stock trading at a **110% premium** to the broader index — explicitly described in
contemporaneous coverage as **"a valuation premium last seen in the run-up to the year 2000 dot-com
bubble."** The Nifty Midcap 100 itself had started 2018 at a **28.7x forward P/E, a 52% premium to
the Nifty 50** — i.e., even the *midcap* segment that subsequently crashed had itself been trading rich
relative to large caps immediately beforehand, a reminder that "smallcap crash" and "quality-growth
euphoria" were two faces of the same narrow-breadth, flight-to-perceived-safety regime rather than
independent events. **The "value trap" coda.** The NBFC/banking-sector fallout continued to claim
casualties through 2019–2020 — Yes Bank, valued near **₹1 lakh crore in 2017–18**, was placed under
RBI administration in **March 2020** with SBI acquiring a 49% stake at **₹10/share** — a directly
India-specific illustration of the "cheap for a reason" value-trap risk the Piotroski F-Score
(B1.10) is explicitly designed to screen against: falling multiples in the NBFC/financials complex
through 2018–2019 reflected **genuinely deteriorating fundamentals** (asset-liability mismatches,
concealed asset-quality problems), not merely a market overreaction a mechanical B/P or E/P screen
would have recognized as an opportunity. **Lesson.** This episode is the clearest India analogue to the US 1998–2000 and 2017–2020 cases in
structure (a value/broad-market segment crushed while a narrow "safety" segment re-rated to
extremes), but its *mechanism* is distinctively India-specific — regulatory reclassification and
index-reconstitution shocks compounding a genuine credit event, not a pure multiple-expansion bubble
— arguing for treating "quality re-rating extremes" (the FMCG 48x/110%-premium reading) as **its own
India-specific crowding signal** in the D02 dossier's existing conditioners, not an import of the US
episodes' calibration.

---

## B3. India evidence in full

**The AJV/IIMA factor library — what is verified, and what remains the desk's own to compute.** The
Agarwalla-Jacob-Varma India Fama-French-momentum library (2013 IIMA working paper; "Size, Value, and
Momentum in Indian Equities," *Vikalpa* 42(4), 2017) remains the closest India analogue to Ken
French's own library, and its **published** headline figure — independently re-confirmed by this
session's search, matching the D02 dossier's own citation — is **HML averaging 15.3%/year over
January 1994–December 2014**, against a market premium of 11.5%/year, momentum (WML) 21.9%/year, and
size (SMB) essentially 0%/year over the same window. **Construction differences from Fama-French,
already documented in the D02 dossier and the momentum Part B's own side-task provenance work:** the
big/small breakpoint sits at the **90th percentile** of market cap (reflecting India's far more
concentrated market-cap distribution than the US), and portfolio formation occurs in **September**
rather than June, aligned to India's March fiscal year-end. The desk's own GitHub-mirrored copy of
this library (`ingest/vault/factors/iima_monthly_factors.csv`) is confirmed present, with the correct
column schema (`Date, SMB, HML, WML, MF, RF`) and date range (1993-10 through 2025-12) — but, per
instruction, **no HML/SMB summary statistic is computed from that file in this Part**; the momentum
Part B's own independent recomputation of the *momentum* column from the same mirrored file surfaced a
**material, unresolved discrepancy** against the literature's headline WML figure (its own recomputed
~13.1%/yr versus the ~21.9%/yr literature figure), which is a direct, mirror-specific reason for the
desk to insist on computing HML/SMB statistics itself from a properly authenticated pull, rather than
importing either this session's or the literature's number uncritically.

**Sehgal and co-authors — the foundational, and more skeptical, India value literature.** Sehgal's
early work (**Kumar & Sehgal 2004** and related Connor-Sehgal studies) documents a **strong size
effect** alongside a comparatively **weak value effect**, particularly when E/P is the distress
proxy; three sources of the value effect are identified — **operating profitability, size, and
financial leverage** — anticipating the quality-overlay logic (B1.9/B1.10) by treating profitability
as *part of* what a naive value sort picks up, not an independent signal. Sehgal's book, *Asset
Pricing in Indian Stock Market*, finds a Fama-French-style model beats CAPM in India, but — more
skeptical than the AJV headline figure implies — reports that **size-, value-, reversal- and
momentum-based strategies do not provide extra-normal (risk-adjusted) returns** in his sample, a
tension with AJV's raw HML figure the desk should read as: value's *raw* premium in India is not in
serious dispute, but whether it survives risk-adjustment and costs is the harder, less settled
question — exactly the CONTRACT's own governing discipline (§5) applied to India.
**Later, decay-focused India studies.** **Harshita, Singh & Yadav (2018), "Changing Nature of the
Value Premium in the Indian Stock Market,"** *Global Business Review*, documents that the value
premium's *character* has shifted over the sample — consistent with a mutating rather than stationary
effect. **Sharma, Srikanth & Suresha (2022), "Is Industry-Specific Value Premium Declining? Evidence
from India,"** finds industry-level attenuation. **Full effect-size magnitudes for both papers are not
independently confirmed in this pass** `[VERIFY: exact decay magnitude in these two India-specific
value-decay papers, as already flagged in the D02 dossier]`. **Role of size and risk in the value
anomaly.** A more recent paper, "Role of size and risk effects in value anomaly: Evidence from the
Indian stock market" (*Cogent Economics & Finance*, 2020), directly tests whether India's value
premium survives controls for size and risk — precisely the Israel-Moskowitz-style decomposition
(B1.5) applied to India — `[VERIFY: this paper's specific conclusion and magnitude were not
independently extracted from the search snippet in this pass; flagged as a concrete data-phase
reading task rather than asserted]`.

**India quality studies.** **Agarwalla, Jacob, Varma & Vasudevan (2014), "Betting Against Beta in the
Indian Market"** (IIMA WP2014-07-01) — already anchored in the D02 dossier — finds India's BAB premium
is **largely explained once a profitability/quality factor is added**, i.e., India's low-beta effect
looks like a quality effect in beta's clothing, the same logic as Asness-Frazzini-Israel-Moskowitz-
Pedersen's "size matters if you control your junk" applied to beta instead of size. **F-Score/accruals
replications on India.** Multiple applied studies test Piotroski's F-Score directly on Indian data;
one (Agrawal, 2015, per this session's search) finds the F-Score carries genuine **default-predictive
ability** for Indian firms, and a separate applied study finds a **high-F-Score portfolio earning an
18.3%/year market-adjusted return versus 4%/year for a low-F-Score portfolio** on an Indian sample
`[VERIFY: the exact paper, sample window and universe behind the 18.3%/4% figures were not
independently and unambiguously isolated from the search snippets in this pass — the qualitative
finding (F-Score has predictive power in India, with a materially positive high-minus-low spread) is
corroborated across multiple sources, but the specific magnitude should be confirmed against the
primary paper before use]`. **No India-specific Sloan-style accrual-anomaly study was independently
located in this pass either** — carried forward, exactly as the D02 dossier already flags it, as an
untested cross-country prior for India specifically. **Recent, direct QMJ replications on India:**
**"Beyond Junk: Evaluating Quality Premium's Influence on Stock Prices and Returns in India Before and
After COVID,"** *IIMB Management Review* (ScienceDirect, S0970389626000303), finds quality firms show
**greater resilience during market crashes** than junk firms and that quality **consistently
outperforms junk stocks over any given time period** in the India sample studied, with the added
observation that liquidity concerns dominate firm-fundamentals in driving crisis-period price moves —
a direct India data point for the D02 dossier's own proposed "quality as crisis ballast" role.
**"Machine Learning-Enhanced Quality Minus Junk (QMJ) Factor and Stock Returns: Evidence from the
Indian Equity Market"** (2025, ScienceDirect) extends the replication with an ML-augmented
construction — both papers together constitute the first *direct*, dedicated QMJ-style replications on
India this Part could locate, materially strengthening the evidence base beyond the D02 dossier's
prior reliance on BAB-subsumed-by-quality as the closest India quality proxy.

**The practical India frictions — promoter accounting quality, related-party transactions, and
governance red flags as a quality input.** Multiple India-specific corporate-governance studies (e.g.
**Rasheed, Mallikarjunappa & Thomachan (2019), "Promoter Ownership, Related Party Transactions and
Firm Performance,"** *FIIB Business Review*; an IIM Bangalore working paper, "An Analysis of
Related-Party Transactions in India") document that **related-party transactions are a common,
structurally-embedded vehicle for earnings management and value extraction** in India's
business-group-dominated ownership structure, with disclosure required above materiality thresholds
under Companies Act 2013 / SEBI LODR. Practitioner due-diligence literature independently converges on
a consistent list of India-specific "red flags" that a quality screen should treat as inputs distinct
from any imported QMJ profitability/safety component: **overstated revenues, RPT-distorted
profitability, divergence between audited financials and internal management accounts, promoter share
pledging, pending tax/GST disputes, and weak or absent independent-director oversight of subsidiary
transactions specifically** (RPT studies find subsidiary-level transactions are flagged as
particularly dangerous in the absence of an independent director). This is, exactly as the D02
dossier already argues, a **structurally distinct "junk" definition component with no direct US
analogue at this scale** — US firms rarely face the same concentrated-control-block, RPT-heavy
governance structure — and it is the strongest India-specific argument in this Part for why a naive,
imported QMJ or F-Score construction is necessarily incomplete for India without a governance-flag
overlay.

**Which fundamentals are free in India versus paid.** **Free, point-in-time-friendly sources:** NSE
and BSE both mandate **XBRL-tagged filings** — BSE was "the first and only stock exchange in India to
introduce and implement XBRL-based reporting," and SEBI mandates XBRL for quarterly results, annual
financial statements, and (more recently) BRSR/ESG disclosures — so the raw structured data underlying
every signal this Part discusses is, in principle, **free and programmatically parseable** directly
from exchange filings. **Screener.in**, founded 2009, aggregates this filing data into a free-tier
product covering **4,000+ NSE/BSE stocks with 10+ years of history** (balance sheet, P&L, cash flow,
quarterly results, updated within days of filing) — usable, if rate-limited (free tier: 50 companies
followed, 10 alerts). **Paid alternatives, for contrast:** **CMIE Prowess** (AJV's own published
methodology relies on it) covers **50,000+ companies'** P&L, balance sheet, ratios, shareholding and
market data via ProwessIQ/PACE/ProwessDX; **Capitaline** covers **~35,000 companies** across **~650
fields**; **ACE Equity** covers **1,750+ data points/company**. None publish list pricing (access is
institutional/negotiated), but the coverage gap — 50,000+ firms paid versus Screener's free-tier
4,000+ — is the concrete, quantified version of the CONTRACT's no-paid-feeds constraint (§3) this desk
must close through free XBRL-plus-Screener aggregation, not assume solved.

---

## B4. Pooled conclusions, ranked by evidence strength, mapped to design implications

1. **(Strongest — Tier A globally: hundreds of country-years across the FF-1992/1993/1998 lineage,
   the 13-country and 24-country international tests, direct India replication in the ~20-year AJV
   series plus multiple independent India studies.)** A value premium — cheap stocks outperforming
   expensive ones on B/M, E/P, CF/P or sales/price — is a genuine, persistent, cross-country
   phenomenon whose leading explanations (relative-distress risk per FF98; extrapolative,
   Lakonishok-Shleifer-Vishny-style behavioral overreaction) both plausibly survive being known,
   because neither requires an information gap arbitrage can close. → **Value sleeve**: retain a
   multi-multiple composite (majority E/P + CF/P, minority B/P) as the D02 dossier already proposes;
   India's raw AJV HML figure (15.3%/yr, 1994–2014) is corroborating, but Sehgal's own
   risk-adjusted-return skepticism means the desk should not treat the raw figure as a cost- and
   risk-adjusted sizing input without its own purged-CV test.
2. **(Strong — Tier A globally: Novy-Marx's single large US panel, Ball-Gerakos-Linnainmaa-Nikolaev's
   refinement, QMJ's 24-country test; Tier B India via the BAB-subsumed-by-quality finding and the
   two direct 2024–2025 India QMJ replications.)** Profitability/quality, measured multiple ways
   (gross profitability, cash-based operating profitability, QMJ's composite), earns a premium
   **comparable in magnitude to value itself** and is close to orthogonal to value as a
   characteristic — the empirical basis for combining rather than choosing between them. → **Quality
   sleeve**: lead with a cash-flow-based operating-profitability measure (per B1.10's Ball et al.
   logic) rather than a pure accrual-inclusive earnings measure, both because it is the
   best-evidenced single characteristic and because cash-flow-statement data is comparatively less
   exposed to the RPT-driven earnings-management channel B3 documents as an India-specific risk.
3. **(Strong — a single large, multi-asset-class negative-correlation result (AMP 2013), directly
   corroborated by Japan's long-run value record standing in contrast to Japan's own weak momentum
   record.)** Value and momentum are negatively correlated across markets and asset classes, and each
   factor's own worst historical winters (this Part's B2 cases; the momentum Part B's own six crash
   case studies) do not cluster on the same calendar dates — 1998–2000 was a value winter and a
   momentum-favorable regime; 2008–09 was a momentum-crash regime and (per B1.6) mid-drawdown for
   value; 2020's rebound crashed momentum (momentum Part B, case 3) while accelerating, not
   reversing, value's own drawdown until November. → **Value-momentum combination weights prior**:
   the two sleeves should be sized as genuinely diversifying, not merely additive, exactly matching
   the momentum Part B's own conclusion reached independently from the momentum side; a combined
   value+momentum construction should expect a materially better Sharpe ratio than either sleeve's
   own volatility suggests in isolation, and the combination weight should lean *toward* momentum
   when the value spread is in its own bottom tercile (a wide, cheap value spread is value's own
   "quiet before the reward" signal, not a reason to prefer momentum).
4. **(Strong, but genuinely two-sided — Tier A magnitude evidence (the −55% HML drawdown is an
   undisputed fact), Tier B/C on *interpretation*.)** The post-2007 US value drought and post-2020
   partial recovery are the best-documented value winter/payoff pair in the global record, but the
   "why" is contested between two teams who agree on the proximate mechanism (valuation-spread
   widening) while disagreeing on how much weight intangibles-mismeasurement deserves; the 2022→2023
   whipsaw shows the question is not closed even walk-forward. → **Value-spread regime input
   (`valuation_sentiment` block)**: build the value-spread percentile as the primary conditioner (per
   Cohen-Polk-Vuolteenaho, already in the D02 dossier), but do **not** build a separate
   "intangibles-adjusted HML" sub-signal as a first-order sleeve component until the data phase can
   test whether India's accounting regime makes the intangibles concern smaller here than in the US
   case this debate is drawn from — an open, testable question this Part does not resolve by
   assertion.
5. **(Moderate-strong — Tier A globally (Israel-Moskowitz's 86-year decomposition), Tier B in India
   via Sehgal's own size/leverage decomposition of the value effect.)** Value's premium decreases
   with firm size and is weak among the largest stocks — the opposite capacity profile from momentum
   (which the momentum Part B documents as size-independent) — and a quality overlay is specifically
   what restores value's power in large, liquid names. → **Value sleeve construction, multiple
   choice by segment**: EV/EBITDA (requiring a debt figure) should be treated as a **minority,
   large-cap-weighted** component precisely because debt figures are more exposed to the
   related-party/off-balance-sheet-financing concerns B3 documents, while E/P and CF/P (requiring
   only income-statement/cash-flow-statement data, both free via XBRL) should carry the composite's
   majority weight across the full moderate-book universe, consistent with the D02 dossier's own
   "price-only-plus-lag-buffered fundamentals" preference.
6. **(Moderate — Tier B India, a single sub-literature (Sloan/Piotroski/Ball et al. lineage) with
   partial, not yet fully confirmed, India replication.)** Piotroski's F-Score shows genuine
   predictive power in at least one India study (with a materially positive but not yet fully
   pinned-down high-minus-low spread), while no dedicated India Sloan-style accrual-anomaly study was
   located at all. → **Quality sleeve, accruals component**: treat an accruals-based sub-signal as
   **untested for India** (carry the D02 dossier's own Tier-B-at-best flag forward) and prioritize the
   F-Score-style composite screen (which has at least one direct India confirmation) over a
   standalone Sloan-style accrual factor until a dedicated India accrual-anomaly test exists.
7. **(Moderate — direct, multi-source India evidence with no close US analogue, but no study yet
   quantifying its incremental power over standard QMJ.)** Promoter-linked related-party transactions
   and governance red flags (RPT-distorted profitability, pledging, audited-vs-management-account
   divergence, subsidiary transactions absent independent-director oversight) are a well-documented,
   India-specific quality-relevant risk channel distinct from the global QMJ/F-Score literature. →
   **Quality sleeve, India-tailored "junk" definition**: add a governance-red-flag term
   (RPT-disclosure intensity, promoter-pledge percentage, subsidiary-oversight flags) as a Tier-C,
   **reduce-only** input alongside standard QMJ components, mirroring the D02 dossier's existing
   pledge/RPT overlay — this Part corroborates the mechanism directionally but does not establish a
   quantified incremental-power test, so the tier stays at C.
8. **(Weakest/most tentative — a data-provenance and free-vs-paid coverage gap, not a market
   finding.)** Free India fundamentals (XBRL filings, Screener.in's free-tier aggregation) cover a
   materially narrower universe (Screener: 4,000+ names, free tier limited to 50 followed) than the
   paid alternatives this desk is barred from using (CMIE Prowess: 50,000+ firms; Capitaline: ~35,000
   firms/650 fields; ACE Equity: 1,750+ data points/firm) — a concrete, now-quantified version of the
   CONTRACT's Known Prior #7 concern. → **Action, not a design change yet**: the data phase must
   specify how a free XBRL-plus-Screener-style pipeline reaches the moderate book's full ranks-1–500
   universe (or document which names it cannot cover and why), rather than assume the free tier alone
   is sufficient — a concrete build task the D02 dossier's §6 already anticipates but does not yet
   quantify with the firm-count gap this Part surfaces.

---

## Special side-task — GitHub-hosted mirrors for value/quality data

Per the desk's 2026-09-01 mirror-authorization decision (`research/OPEN_QUESTIONS.md`), only
`raw.githubusercontent.com`, `media.githubusercontent.com`, and `objects.githubusercontent.com`
(release assets) are reachable from this environment; `aqr.com`, `mba.tuck.dartmouth.edu` and
`faculty.iima.ac.in` are blocked at the proxy (the last confirmed blocked directly in this session).
Using GitHub's own code-search index (`mcp__github__search_code`), the following were found.
**Nothing was downloaded into the ingest vault in this pass** — existence, content-shape, and a
first-pass credibility judgment only, per instructions.

1. **`YuvrajChauhan-Fin/Fama-french-India`** — `data/external/iima_monthly_factors.csv`. The desk's
   own already-ingested India HML+SMB+WML+market mirror (schema and date range re-confirmed this
   session directly against the local ingest copy: `Date, SMB, HML, WML, MF, RF`, 1993-10 to
   2025-12). **Credibility: high-but-flagged**, exactly as the momentum Part B already documented —
   internally coherent and correctly dated, but its own WML level does not match the literature
   figure on independent recomputation; the corresponding HML-level check is a data-phase task, not
   performed here per instruction.
   `https://raw.githubusercontent.com/YuvrajChauhan-Fin/Fama-french-India/15f6511865b3d5ba85cf00d6228135cfabb2b0c5/data/external/iima_monthly_factors.csv`
2. **`WhitesPhD/momentum-crashes-replication`** — `CodeBase/Data/FFF_monthly.CSV`. The official
   Fama-French 3-factor monthly series (Mkt-RF, SMB, HML, RF; 1926-07 onward, "202411 CRSP database"
   vintage) inside the published-paper replication package for Bianchi, De Polis & Petrella,
   *"Time-Varying Skewness and Momentum Crashes"* (*Review of Asset Pricing Studies*). **Credibility:
   highest of the HML/SMB mirrors found** — a peer-reviewed paper's own companion repository, not a
   hobby project.
   `https://raw.githubusercontent.com/WhitesPhD/momentum-crashes-replication/b6e7b8754c69b337e65ac2c08d8811f144b0b832/CodeBase/Data/FFF_monthly.CSV`
3. **`ZhenHaoFu810/StataFlow`** — `research/data/public/finance/fama_french/ff5/F-F_Research_Data_5_Factors_2x3.csv`.
   The full **5-factor** monthly series (Mkt-RF, SMB, HML, RMW, CMA, RF; 1963-07 onward), header text
   stating **"created using the 202602 CRSP database"** — the freshest vintage found in this search
   (February 2026). **Credibility: high** — 1963-07 values (Mkt-RF −0.39, SMB −0.48, HML −0.81, RMW
   0.64, CMA −1.15) match the canonical series to within ordinary cross-vintage rounding.
   `https://raw.githubusercontent.com/ZhenHaoFu810/StataFlow/2a6bfc5482fde172189416cefe18694842d8a222/research/data/public/finance/fama_french/ff5/F-F_Research_Data_5_Factors_2x3.csv`
4. **`QuantConnect/Tutorials`** — `Data/F-F_Research_Data_5_Factors_2x3.CSV` (also carries the plain
   3-factor file at `Data/F-F_Research_Data_Factors.CSV`, "202007 CRSP database" vintage). A second,
   independently-sourced RMW/CMA mirror for cross-checking #3. **Credibility: high** — QuantConnect is
   a well-known quant-trading platform's own official tutorials repository, not an anonymous fork.
   `https://raw.githubusercontent.com/QuantConnect/Tutorials/4a341890296f7e79e095508f06170c72ccaa629c/Data/F-F_Research_Data_5_Factors_2x3.CSV`
5. **`PaulSoderlind/ModernFinanceTheory`** — `Data/25_Portfolios_5x5.CSV`. The **primitive size×B/M
   building-block portfolios** (`SMALL LoBM … BIG HiBM`, 1926-07 onward) that HML/SMB are themselves
   averaged from — the finer (5×5, not 2×3) sort, directly useful for reconstructing or
   sanity-checking a from-scratch HML calculation against the published factor. **Credibility: high**
   — Paul Söderlind is a named finance-professor-authored teaching repository, not an anonymous
   scrape.
   `https://raw.githubusercontent.com/PaulSoderlind/ModernFinanceTheory/1c28ea9b6cb039008be24c77b68ce9276a1c38e7/Data/25_Portfolios_5x5.CSV`
6. **`pascal-schindlmeier/apt_fama_french`** — `Europe_3_Factors.csv` (Mkt-RF, SMB, HML, RF for
   Europe, header stating "created using the 202601 Bloomberg database," i.e. January 2026 vintage)
   plus a companion `Europe_25_Portfolios_ME_BE-ME.csv` referenced in the same repo's README.
   **Credibility: medium** — internally coherent and correctly formatted in Ken French's own file
   convention, but this appears to be a **personal/student reconstruction sourced from Bloomberg**
   rather than a verbatim mirror of Ken French's own official international-developed-markets file;
   `[VERIFY: whether this is a byte-for-byte copy of Ken French's own Europe file or an independent
   reconstruction before treating its exact values as authoritative for an international value
   replication]`.
   `https://raw.githubusercontent.com/pascal-schindlmeier/apt_fama_french/7e87a79a7bf31daa57d1a0bcc3a3a3a5fcf24cdf/Europe_3_Factors.csv`
7. **QMJ (AQR Quality Minus Junk) factor data — a confirmed gap, not an omission.** No GitHub-vendored
   copy of AQR's own QMJ return series (monthly or daily) was located anywhere in this search. What
   exists instead: **`Reckziegel/aqrr`** (an R package, repository name `aqqr` in its own badges) that
   **downloads** AQR's datasets live from `aqr.com` at runtime rather than vendoring them, and a
   third-party audit note (found in `hankkontakt/marketscan`'s own research-provenance file) that
   independently confirms the AQR endpoint's live structure (30 columns: date + 29 series covering the
   US plus 23 international markets and 5 regional aggregates, 792 monthly rows from 1957-07 for the
   US) without itself vendoring the data. This mirrors the momentum Part B's own finding that AQR's
   TSMOM/Century-of-Trend dataset is similarly un-mirrored on GitHub — AQR's own datasets appear to be
   systematically absent from GitHub as committed files, likely reflecting AQR's terms of use, and
   remain a principal's-machine (direct `aqr.com` pull) task for the data phase.
8. **India fundamentals panels (XBRL scrapes, screener dumps) — also a confirmed gap.** Several
   personal repositories contain **scraper scripts** targeting Screener.in and MoneyControl (e.g.
   `Shreyansh-brothers/Sentence-transformer`'s `indian_filings_dataset` scraper), but no committed,
   clearly-provenanced **data panel** (as opposed to scraping code) covering India fundamentals with
   point-in-time structure was located on GitHub. This is consistent with the momentum Part B's
   parallel finding that no clean NIFTY total-return-index history is GitHub-mirrored either — both
   remain principal's-machine tasks (direct NSE/BSE XBRL pulls, or a Screener.in free-tier API build)
   rather than GitHub-mirror tasks for the data phase.

---

## References

Fama & French (1992). "Cross-Section of Expected Stock Returns." *J. Finance* 47(2):427–465. · Fama &
French (1993). "Common Risk Factors in the Returns on Stocks and Bonds." *JFE* 33(1):3–56. · Fama &
French (1998). "Value versus Growth: The International Evidence." *J. Finance* 53(6):1975–1999. ·
Fama & French (2015). "A Five-Factor Asset Pricing Model." *JFE* 116(1):1–22. · Asness, Moskowitz &
Pedersen (2013). "Value and Momentum Everywhere." *J. Finance* 68(3):929–985. · Israel & Moskowitz
(2013). "The Role of Shorting, Firm Size, and Time on Market Anomalies." *JFE* 108(2):275–301. ·
Cohen, Polk & Vuolteenaho (2003). "The Value Spread." *J. Finance* 58(2):609–641. · Arnott, Harvey,
Kalesnik & Linnainmaa (2021). "Reports of Value's Death May Be Greatly Exaggerated." *FAJ*
77(1):44–67. · Israel, Laursen & Richardson (2020). "Is (Systematic) Value Investing Dead?" AQR. ·
Novy-Marx (2013). "The Other Side of Value: The Gross Profitability Premium." *JFE* 108(1):1–28. ·
Sloan (1996). "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows...?" *Accounting
Review* 71(3):289–315. · Piotroski (2000). "Value Investing: ... Separate Winners from Losers." *J.
Accounting Research* 38(Supp.):1–41. · Ball, Gerakos, Linnainmaa & Nikolaev (2016). "Accruals, Cash
Flows, and Operating Profitability..." *JFE* 121(1):28–45. · Asness, Frazzini & Pedersen (2019).
"Quality Minus Junk." *Review of Accounting Studies* 24(1):34–112. · Asness & Frazzini (2013). "The
Devil in HML's Details." *JPM*. · Agarwalla, Jacob & Varma (2013/2017). "Size, Value, and Momentum in
Indian Equities." *Vikalpa* 42(4); IIMA WP 2013-09-05; library at faculty.iima.ac.in/iffm/. ·
Agarwalla, Jacob, Varma & Vasudevan (2014). "Betting Against Beta in the Indian Market." IIMA
WP2014-07-01/SSRN 2464097. · Kumar & Sehgal (2004). "Company Characteristics and Common Stock
Returns." *Vision* 8(2). · Sehgal, S. *Asset Pricing in Indian Stock Market* (book). · Harshita, Singh
& Yadav (2018). "Changing Nature of the Value Premium in the Indian Stock Market." *GBR*. · Sharma,
Srikanth & Suresha (2022). "Is Industry-Specific Value Premium Declining?" · "Role of size and risk
effects in value anomaly: Evidence from India." *Cogent Econ. & Finance* (2020). · Rasheed,
Mallikarjunappa & Thomachan (2019). "Promoter Ownership, RPTs and Firm Performance." *FIIB Business
Review*. · IIM Bangalore WP 402, "An Analysis of Related Party Transactions in India." · "Beyond
Junk: ...Quality Premium... Before and After COVID." *IIMB Management Review*. · "Machine
Learning-Enhanced QMJ Factor and Stock Returns: Evidence from India" (2025). · Graham & Dodd (1934).
*Security Analysis*. · McLean & Pontiff (2016). "Does Academic Research Destroy Stock Return
Predictability?" *J. Finance* 71:5–32 (CONTRACT's governing citation). · GitHub mirror URLs per the
side-task section, confirmed via `mcp__github__search_code` this session.


---

# PART B-RESULTS — Real data: India HML mirror + US Fama-French (V0–V4)

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



---

# PART C — Data engineering (Indian fundamentals, point-in-time)

# Part C — Data engineering: Indian fundamentals for value and quality, free

v1.0 · 2026-09-01 · Extends `docs/masterplan/A-data-catalog.md`, which has **no fundamentals block
at all** (its §2 blocks A–N cover price/index/ownership/IPO/AMFI/FII/RBI/CCIL/BIS/IMF/gold/
macrohistory/demographics/election/budget — company financial statements are absent). This part
fills that gap for `config/sleeves.yaml factor_book.value` and `factor_book.quality` (moderate
book engine, Decision Q6) and for `config/ladder.yaml L8_value_spread`. It reuses, and does not
re-derive, `research/cycles/momentum-deep/partC-data.md`'s bhavcopy mechanics (§C.1 legacy↔UDiFF
crosswalk), corporate-actions math (§C.2), survivorship/PIT-universe procedure (§C.3), and the
mirror-authorization rule (`research/OPEN_QUESTIONS.md`, 2026-09-01) — cross-referenced below, not
duplicated. Consumes: `research/dossiers/02-value-quality-lowvol.md` (theory/evidence/decay),
`research/CONTRACT.md` §3 (free-source mandate), Known Prior #7 (restatement inflates backtests
150–450bps/yr). Feeds: this program's value/quality construction and the fundamentals ingest kit
(a genuine gap — see §C.8's closing note). Checked by web search this pass (snippet-level, per
Contract prior #11 — `sebi.gov.in`, `nseindia.com`, `bseindia.com`, `niftyindices.com` all
egress-blocked here; nothing fetched/parsed directly, unlike momentum Part C's one
`raw.githubusercontent.com` upgrade). Anything not corroborated by ≥2 search results carries
**[VERIFY]**.

---

## C.1 The core problem — point-in-time fundamentals in India

**Where the primary filings live (free).** Every quarterly/annual result a listed Indian company
reports under **SEBI LODR Regulation 33** is filed directly with the exchanges, not just published
in an annual report — the load-bearing fact that makes a free PIT fundamentals store possible at
all. Primary venue: `nseindia.com/companies-listing/corporate-filings-financial-results`
(search-by-company/period, CSV export, XBRL-to-Excel conversion tool); BSE mirrors the same
disclosure under its own corporate-filings/financial-results page (exact production URL
**[VERIFY]**, same caution momentum Part C already flags for BSE's corporate-actions page).
Dual-listed companies file the identical document to both exchanges simultaneously — a genuine
cross-check, analogous to the NSE-vs-BSE bhavcopy cross-check in momentum Part C §C.1.

**XBRL mandate — history, not a single date.** This did not arrive as one clean cutover; it is a
three-stage regime, and conflating the stages will silently wreck a pre-2017 pull:

| Stage | Date | What changed |
|---|---|---|
| Voluntary XBRL (financial results + shareholding pattern) | From **June 2015** (BSE) | Listed companies could optionally submit in XBRL alongside the mandatory PDF; coverage is patchy and self-selected, not universal |
| Format prescription | **SEBI Circular CIR/CFD/CMD/15/2015, 2015-11-30** (revised by a further circular, 2016-05-27, applicable for periods ended on/after 2016-03-31) | Standardizes the P&L line-item format listed entities must use — a necessary precondition for a machine-parseable panel, distinct from the XBRL-mode mandate itself |
| **Mandatory XBRL for financial results, all listed entities** | **BSE Circular DCS/COMP/28/2016-17, dated 2017-03-30, effective 2017-04-01** [VERIFY: NSE's own parallel circular number for the identical effective date] | PDF filed within 30 minutes of the board meeting concluding; XBRL filed within 24 hours of the PDF. This is the practical start of a genuinely machine-readable, exchange-sourced financial-results panel — **treat 2017-04-01 as the hard PIT-panel boundary**, exactly as 2024-07-08 is the hard boundary for bhavcopy (momentum Part C §C.1) |
| **Integrated Filing (Financials)** | Mandatory from **quarter ended 2025-03-31** (SEBI Circular SEBI/HO/CFD/CFD-PoD-2/CIR/P/2024/185, 2024-12-31; PDF-only submission via the old NEAPS "Quick Results" route discontinued 2025-04-01) | Bundles the Reg. 33 financial result, Reg. 23(9) related-party-transaction disclosure, and audit-qualification statement into **one** quarterly XBRL document — a second schema break, this one shrinking rather than growing the parsing burden (fewer, larger filings instead of several small ones per quarter) |

**Taxonomy — two different regulators, two different systems, do not conflate them.** The **MCA
C&I (Commercial & Industrial) Taxonomy** and its Ind AS variant govern **annual** filings to the
Registrar of Companies under the Companies Act (Form AOC-4 XBRL; mandated by the MCA's 2011-06-07
notification, phased by listing status / paid-up capital ≥₹5cr / turnover ≥₹100cr, i.e. this is
where the "since 2011" figure some sources quote comes from). The **NSE/BSE listing-XBRL utility**
governs the Reg. 33/23/31 filings above and is a **separate system built to the exchanges' own
utility, not a direct feed from MCA** — a company's Reg. 33 quarterly XBRL and its AOC-4 annual
XBRL are two independently-filed documents, on two different taxonomies, to two different
regulators, on two different schedules. A build script targeting "India XBRL financials" that
only knows one of these systems will silently miss the other. This program's use case (quarterly
+ annual value/quality signals at NIFTY-750 breadth) needs the **exchange-side** (NSE/BSE
Reg. 33/23/31) system as primary; MCA's AOC-4 XBRL is the fallback for a name that ever stops
exchange-filing (delisting-adjacent) or for cross-checking a disputed number.

**Exact lag, by filing type.**

| Filing | Regulation | Deadline from period-end | Applies to |
|---|---|---|---|
| Quarterly financial results (Q1–Q3) | LODR Reg. 33 | **45 days** | All listed entities (banks: separate RBI-aligned timeline, §C.3) |
| Annual/Q4 financial results | LODR Reg. 33 | **60 days** | Audited; includes Statement of Impact of Audit Qualifications if applicable |
| Shareholding pattern | LODR Reg. 31 | **21 days** | Quarterly (already catalogued: A-catalog C3) |
| Related-party transactions | LODR Reg. 23(9) | **30 days from publication of the half-year results** (not from period-end) | Half-yearly, consolidated basis |
| Auditor resignation, reasons | LODR Reg. 30 | **24 hours** | Event-based |

**Restatement behavior.** SEBI's own XBRL rules explicitly anticipate revision: "revised XBRL
filings are required in case of any mismatch with the PDF, revision of financial results, restated
financials, or voluntary corrections," with revision remarks attached. This is good news
(restatements are a first-class, filed event, not silently absorbed) and bad news for a PIT builder
(there is **no public, structured, single-page archive of "which filings were later revised, and
when"** — a revision shows up only as a second dated filing on the company's own filing-history
page, indistinguishable from a routine subsequent-quarter filing unless the parser reads the
revision-remarks field and cross-references period covered). **The construction rule this forces**:
key the fundamentals store on `(company, fiscal_period, filing_type, announcement_timestamp)`, not
on `(company, fiscal_period)` — a later row for the same fiscal period is a **revision event**, kept
as a new vintage, never overwriting the original (identical discipline to momentum Part C §C.7's
WORM rule and to `ingest/manifest.py`'s existing hash-hard-fail).

**`knowledge_time` — the exact PIT construction rule.** NSE/BSE's own filing convention already
gives the desk almost exactly what a PIT store needs for free: the PDF must be filed within **30
minutes** of the board meeting concluding, and the corporate-announcement record on the exchange
carries the filing's **exact submission timestamp** (date + time, not just date). Use that
timestamp — not the fiscal period-end, and not even the board-meeting date if the two diverge — as
`knowledge_time` for every fundamental fact the filing contains. A signal computed "as of" a
rebalance date must only see filings whose `knowledge_time <= rebalance_date`; this is the single
mechanical safeguard against the look-ahead bias Known Prior #7 already prices at 150–450bps/yr.
Two refinements worth stating: (i) the XBRL follows the PDF by up to 24 hours (pre-2025) or is
simultaneous (Integrated Filing, 2025+) — use the **PDF's** timestamp as `knowledge_time` even when
only the XBRL is machine-parsed, since the market already knew the numbers from the PDF; (ii) a
revised filing gets its **own**, later `knowledge_time` — a backtest run "as of" a date between the
original and the revision must see only the original, exactly the discipline the India-factor-
mirror validation in §C.7 depends on to be meaningful.

---

## C.2 What fields are gettable free, and at what history

**The single most consequential fact for ratio construction**: in India, the quarterly financial
result is **P&L-only plus EPS** — a full balance sheet ("Statement of Assets and Liabilities") and
a cash-flow statement are SEBI-mandated only **half-yearly and annually**, not every quarter (this
mirrors Ind AS 34's minimum interim-disclosure requirement, which the LODR format inherits). A
value/quality build that assumes quarterly balance-sheet granularity because P&L, revenue and EPS
all update quarterly will silently manufacture a false-precision book-value or leverage series that
does not exist as filed.

| Field | Frequency filed free | Source/regulation | Notes |
|---|---|---|---|
| Revenue, PAT, EPS | **Quarterly** (Q1–Q4) | LODR Reg. 33 P&L | Cleanest, highest-frequency fundamental input available |
| Book value / net worth (balance sheet) | **Half-yearly + annual only** | LODR Reg. 33 (half-year note: "Statement of Assets and Liabilities") | NOT quarterly; a Q1/Q3 "book value" is necessarily last-half-year's, stale by up to ~9 months at the worst point in the cycle |
| Cash flow statement (CFO/CFI/CFF) | **Half-yearly + annual only** | LODR Reg. 33 (half-year note: "Statement of Cash Flows") | Same staleness profile as book value; a CF/P signal cannot be a quarterly-refresh signal in India by construction |
| Shares outstanding + face value/paid-up capital | **Quarterly** (embedded in every Reg. 33 filing) **and** quarterly shareholding pattern | LODR Reg. 33; Reg. 31 (≤21 days, A-catalog C3) | Also the input to net-share-issuance (Pontiff-Woodgate), already flagged in dossier 02 §4 as the *least* restatement-exposed value-adjacent signal |
| Promoter holding % | **Quarterly** | Reg. 31 shareholding pattern (A-catalog C3) | Category-wise (promoter/promoter group/public/FII/DII) |
| Promoter pledge / encumbrance | **Event-based, ≤2 trading days (Reg. 29) / ≤7 working days (Reg. 31 SAST)** | SAST Regulations (A-catalog C1/C2 — do not re-derive; reference those blocks directly) | The event-based feed is the higher-frequency, higher-precision source; the quarterly shareholding pattern also carries a pledge-percentage column as a slower cross-check |
| Related-party transactions | **Half-yearly** (30 days post half-year-results publication) | LODR Reg. 23(9) | Consolidated-basis format prescribed by the applicable accounting standard for annual RPT disclosure |
| Auditor resignation + reasons | **Event-based, ≤24 hours** | LODR Reg. 30, Schedule III Part A ("Format B"), effective 2019-04-01 (Kotak Committee reforms) | Detailed reasons *as stated by the auditor* — a genuinely rich, free, point-in-time governance signal |
| Auditor qualification (modified opinion) | **Annual only** | LODR Reg. 33 — "Statement on Impact of Audit Qualifications" | Not a quarterly disclosure; limited-review reports on quarterly results can flag "emphasis of matter" language but a formal qualification-impact statement is an annual artifact |
| Credit rating actions | **Event-based** (≤7 working days press release post rating-committee meeting) | SEBI (Credit Rating Agencies) Regulations, 1999, as amended; CRA's own website (CRISIL/ICRA/CARE/India Ratings) | Higher-frequency proxy for leverage/distress between annual balance-sheet disclosures — §C.4 |

**Cash-flow and balance-sheet "half-yearly" in practice**: because the Indian fiscal year runs
April–March, this means fresh book-value and CFO observations land twice a year — end-September
(H1) and end-March (FY) — with Q1 (June-end) and Q3 (December-end) results carrying **no** new
balance-sheet or cash-flow data at all. Any B/P or CF/P series built naively "quarterly" is
actually a **staircase**, flat for two quarters and stepping at two — this staircase shape, not
smooth quarterly interpolation, is the honest representation and must not be smoothed away.

---

## C.3 Ratio construction under Indian constraints

**E/P — the cleanest multiple.** Trailing-4-quarter PAT ÷ current market cap is fully supported at
quarterly cadence: PAT is a P&L line (quarterly-native, §C.2), and shares outstanding for the
market-cap denominator is quarterly-native too. This is the only classic value multiple that
refreshes every quarter in India without a staleness compromise.

**B/P — annual/half-yearly book value, with a mandatory freshness-lag rule.** Book value is a
staircase input (§C.2). The construction rule already frozen in `sleeves.yaml
factor_book.value.components` (dossier 02 §4, "B/P + E/P lag-buffered ≥4–6m") generalizes directly:
apply the **last disclosed** half-year/annual book value, lag-buffered by the same 4–6 month
knowledge-time discipline as §C.1, and hold it flat between disclosure steps rather than
interpolating a smooth quarterly path that was never actually observable. The Asness-Frazzini
"Devil in HML's Details" warning already logged in dossier 02 §1 (stale-book, current-price B/P
correlates more with momentum, behaves differently in crashes) is *structurally forced* on any
India construction by the half-yearly disclosure cadence itself — it is not an optional
convention choice here the way it is in the US, where quarterly balance sheets exist and a builder
could choose otherwise.

**CF/P — annual-only, a slow-refresh signal by construction.** Because the cash-flow statement is
half-yearly/annual (§C.2), CF/P cannot be a quarterly signal in India the way it can be in markets
with quarterly cash-flow disclosure (the US SEC 10-Q requires one). Treat CF/P explicitly as a
**semi-annual-refresh input** into the value composite, not as a quarterly one masquerading as
such by forward-filling a stale number every quarter.

**EV/EBITDA — feasible, but a genuinely mixed-frequency ratio, honestly stated.** EBITDA is
reconstructable from the quarterly P&L (revenue less operating expense, with depreciation/
amortization typically its own disclosed line item in the Reg. 33 P&L format **[VERIFY: universal
across all Ind-AS-format filers, not just a subset]**) — so the numerator refreshes quarterly. Net
debt for the enterprise-value denominator needs the balance sheet — half-yearly/annual only. The
honest construction is therefore: **EBITDA updates quarterly, net debt updates twice a year**, and
any EV/EBITDA reading in the "off" quarters carries a stale net-debt component by definition, not
by parsing error. This is a feasible multiple for the moderate book's value blend, but it is the
single multiple most exposed to the staircase problem, since both its numerator components
(EBITDA, net debt) are individually fine but their *combination* mixes cadences within one ratio.

**Sales/price — the second cleanest multiple.** Revenue is quarterly-native and shares outstanding
is quarterly-native; sales/price refreshes every quarter with no staleness compromise, matching
its role in `sleeves.yaml` (already listed as a value component) and in the NSE500 Value 50 index's
own published methodology (dossier 02 §2: E/P, B/P, sales/price, dividend yield).

**Sector-relative vs. raw ranks — the banks/financials problem, a separate-treatment rule.**
Indian banks report under **Form A (balance sheet) / Form B (profit and loss)** of the **Third
Schedule to the Banking Regulation Act, 1949** — a wholly different statutory format from the
Companies Act Schedule III / Ind AS statements every non-financial filer uses. Compounding this,
**RBI indefinitely deferred Ind AS implementation for commercial banks** (one-year deferral in
April 2018, then "till further notice" on 2019-03-22, pending Banking Regulation Act amendments
not yet enacted **[VERIFY current status, 2026]**) — so banks still report on an RBI-prescribed
local-GAAP-adjacent framework, not Ind AS, while NBFCs (which *did* complete Ind AS transition,
phase III/IV below) and insurers (own IRDAI format, explicitly **exempted from XBRL filing of
financial results**, PDF-only) each sit on a **third and fourth** distinct format. **The rule this
forces**: financials (banks, NBFCs, insurers — three internally-distinct sub-groups) must be
excluded from any universe-wide raw-ratio rank built on "revenue," "EBITDA," "sales/price," or
"gross profitability" — none map cleanly onto a bank's net-interest-income-led P&L or an insurer's
premium/claims structure. P/E and P/B remain usable for financials, but **ranked within financials
only**, never pooled with non-financials on a common percentile — and even then a bank's book
value (regulatory capital, provisioning-sensitive) is structurally different from an industrial's,
so the sector-relative rank should be sized down, not treated as equivalent evidence.

| Ind AS phase | Effective | Who |
|---|---|---|
| Phase I | 2016-04-01 | Listed companies (any net worth) + unlisted companies, net worth ≥₹500cr |
| Phase II | 2017-04-01 | Listed/listing-in-process companies, net worth ₹250–500cr |
| Phase III | 2018-04-01 | Banks, NBFCs, insurers with net worth ≥₹500cr — **but banks specifically were then deferred (see above); NBFCs and insurers proceeded on their own separate formats regardless (IRDAI for insurers)** |
| Phase IV | 2019-04-01 | NBFCs, net worth ₹250–500cr |

**What our free-data value blend can honestly support at NIFTY-750 breadth.**

| Multiple | Refresh cadence achievable | Coverage caveat |
|---|---|---|
| E/P (trailing 4Q) | Quarterly | Full universe ex-financials-raw-pooling; usable for financials sector-relative |
| Sales/price | Quarterly | Full universe ex-financials (revenue concept doesn't apply cleanly) |
| B/P | Half-yearly step, 4–6m lag-buffered | Full universe; financials sector-relative only |
| CF/P | Half-yearly/annual step | Full universe ex-financials (bank CFO statements exist but mean something different — financing/operating lines dominated by deposit-taking) |
| EV/EBITDA | Quarterly EBITDA / semi-annual net debt (mixed) | Ex-financials entirely — EBITDA is not a meaningful concept for a bank or insurer |
| Dividend yield | Event-based (declaration) + quarterly (interim) | Full universe; the single least restatement-exposed value input, price-only-adjacent |

---

## C.4 Quality inputs, free

**Gross/operating profitability — itself a mixed-frequency ratio.** Novy-Marx's gross-profitability
signal (gross profit ÷ total assets) is the QMJ-lineage core input dossier 02 already anchors on.
Gross profit (revenue less cost of goods/services) is quarterly-native in the P&L; **total assets
is a balance-sheet item, half-yearly/annual only** (§C.2) — so gross profitability inherits the
identical staircase problem as EV/EBITDA's net-debt leg. State this explicitly rather than
computing a smooth quarterly series that implies a precision the underlying filings do not support.

**Accruals — needs balance-sheet deltas, annual/half-yearly only.** Sloan's accrual signal
(non-cash earnings component, from the change in working-capital balance-sheet accounts) requires
two balance-sheet snapshots to difference. Since the balance sheet is a half-yearly/annual object
in India, **the accrual signal is, at best, a half-yearly-refresh signal, and a fully clean annual
one if the half-year "note" balance sheet is judged too abridged to trust for a working-capital
breakdown [VERIFY: whether the half-yearly Statement of Assets and Liabilities carries sufficient
line-item granularity for a working-capital accrual calculation, vs. requiring the fuller annual
balance sheet]** — dossier 02 §5 already flags no India-specific accrual-anomaly study was found;
this data constraint is a plausible part of why that literature gap exists.

**Leverage — annual/half-yearly debt, with a credit-rating-action proxy for higher frequency.**
Total debt (long-term + short-term borrowings) is a balance-sheet line, same half-yearly/annual
cadence. Between two balance-sheet snapshots, **credit rating actions are the free, event-based,
higher-frequency distress proxy**: SEBI's CRA Regulations require rating agencies to continuously
monitor and periodically review every outstanding rating for the life of the security, and any
rating action (upgrade, downgrade, outlook change, withdrawal) is disseminated via press release
within **7 working days** of the rating-committee decision (with the issuer given roughly 3 working
days to seek a review first) — published free on each CRA's own website (CRISIL, ICRA, CARE,
India Ratings) and, since the action itself is a listing-agreement disclosure event, also
announced via the exchange corporate-filings feed. **[VERIFY: the exact minimum mandated review
frequency per outstanding rating — search this pass confirmed "continuous monitoring, periodic
review" language but not a single, citable "at least once every N months" figure]** — treat a
rating action's *date* as reliably free and point-in-time, and its *periodicity* as a softer,
issuer/CRA-discretion-dependent cadence, not a fixed clock the way Reg. 33 filing deadlines are.

**Piotroski F-Score — component-by-component feasibility, India-free-data version.**

| # | Signal | Needs | India free-data feasibility |
|---|---|---|---|
| 1 | ROA > 0 | Net income (qtrly) ÷ total assets (H1/annual) | **Mixed-frequency**, computable at half-yearly cadence |
| 2 | CFO > 0 | Cash flow statement | **Annual/half-yearly only** |
| 3 | ΔROA > 0 | Two ROA readings | **Half-yearly**, since ROA itself is mixed-frequency |
| 4 | CFO > net income (accrual quality) | CFO + net income, same period | **Annual/half-yearly only** (gated by #2) |
| 5 | Δ long-term-debt ratio (falling leverage) | Debt ÷ assets, two periods | **Half-yearly/annual only** |
| 6 | Δ current ratio (rising liquidity) | Current assets ÷ current liabilities, two periods | **Half-yearly/annual only** — current-asset/liability granularity itself depends on the balance-sheet note's detail level **[VERIFY]** |
| 7 | No new shares issued | Shares outstanding, two periods | **Quarterly** — computable at the highest frequency of any Piotroski component |
| 8 | Δ gross margin (rising) | Gross profit ÷ revenue, two periods | **Quarterly** — both legs are P&L items |
| 9 | Δ asset turnover (rising) | Revenue ÷ total assets, two periods | **Mixed-frequency** — revenue quarterly, assets half-yearly/annual |

Net picture: **2 of 9 signals (shares issuance, gross-margin change) are genuinely quarterly**; the
other 7 are gated by the balance sheet or cash-flow statement and are therefore **half-yearly/
annual at best** — a full India F-Score cannot be refreshed more than twice a year without either
(a) accepting stale balance-sheet inputs held flat between disclosures (the same staircase
convention as B/P), or (b) waiting for the annual filing specifically. This is a materially
different computability profile from the US, where quarterly 10-Qs make all nine signals a
quarterly-refresh construct — a fact worth stating plainly since Piotroski's original test design
(and most practitioner replications) implicitly assumes quarterly or annual-only-but-quarterly-
priced data, not India's specific half-yearly balance-sheet gap.

**Governance red flags — source and lag, one table.**

| Signal | Source | Lag |
|---|---|---|
| Promoter pledge % | SAST Reg. 29 (≥5% moves)/Reg. 31 (event) + Reg. 31 LODR shareholding pattern (quarterly cross-check) | ≤2 trading days (Reg. 29) / ≤7 working days (Reg. 31 SAST) / ≤21 days (quarterly pattern) — A-catalog C1–C3 |
| Related-party transactions | LODR Reg. 23(9) | 30 days post half-year-results publication |
| Auditor resignation | LODR Reg. 30, Format B | ≤24 hours |
| Audit qualification (modified opinion impact) | LODR Reg. 33 annual filing | Annual, with the audited results (60-day window) |
| Credit rating downgrade/withdrawal | SEBI CRA Regulations, 1999 (CRA press release) | ≤7 working days post rating-committee decision |

---

## C.5 History depth — how far back can a free PIT panel realistically go

**XBRL era (2017-04-01 onward): genuinely machine-readable, exchange-timestamped, the clean core
of the panel** — matching momentum Part C's UDiFF boundary in spirit, this is the second hard
schema/quality boundary this program's data layer must respect. **Integrated Filing (2025-04-01
onward)**: a further, welcome consolidation (fewer documents, same underlying facts) — not a
regression, but still its own schema version to track.

**Voluntary-XBRL / pre-standardized-format era (2015-06 to 2017-03-31)**: patchy, self-selected
coverage — usable as a partial pre-fill, not as a reliable panel start date. Any backtest claiming
a clean panel start before 2017-04-01 should say so explicitly.

**Pre-XBRL PDF era**: NSE's and BSE's own corporate-filings/announcements portals carry historical
PDF filings (the underlying disclosure, not a machine-readable extract) for names that were listed
and filing electronically; **[VERIFY: the exact year electronic exchange filing itself began at
scale — search evidence for NSE's own filing-portal infrastructure was inconclusive this pass,
beyond confirming the portal exists in broadly its current form by the early 2010s]**. Before
electronic filing became universal, results reached the exchanges as physical/faxed filings, with
much thinner free digital-archive depth.

**The principal-machine OCR option.** Because the Reg. 33 P&L format has been SEBI-prescribed
(and largely stable) since the 2015-11-30 circular, pre-XBRL PDF filings are **structurally
regular** — same line items, same layout, company to company and quarter to quarter — a far more
tractable OCR target than a freeform annual-report PDF. Same genre as the "principal's-machine,
genuine multi-week construction project, not a download" already flagged for corporate-action
reconstruction (A-catalog C4) and the demerger registry (momentum Part C): budget it as its own
project, gated behind confirming the exchange portals' historical PDF depth actually reaches back
far enough to justify the OCR investment.

**The honest statement for pre-XBRL backtests.** A pre-2017 India value/quality backtest built from
OCR'd PDFs can plausibly recover revenue/PAT/EPS point history reliably (the prescribed-format
regularity helps), and — because the exchange corporate-announcement record itself carries a
submission date even for a PDF-only filing — can plausibly recover a genuine `knowledge_time` for
each filing too. What it **cannot** honestly claim is a clean **restatement record**: before the
XBRL-native "revision remarks" mechanism (§C.1) existed as a structured field, a revised PDF filing
looked identical to a routine one on inspection, and confirming which historical filings were later
revised requires either a company-by-company manual audit or accepting the risk of silently
treating a revision as if it were the original. **Any pre-2017 India fundamentals backtest must
disclose this as an unresolved restatement-completeness gap, not paper over it with confidence
inherited from the cleaner post-2017 regime** — precisely the kind of honesty Known Prior #7 exists
to enforce, extended to the pre-XBRL boundary specifically. The AJV/IIMA India factor library
(momentum Part C §C.6) reaches back to 1994 on **CMIE Prowess** — a paid vendor with its own,
presumably more complete, restatement/vintage handling; our free-data panel cannot claim to match
that depth on equal footing before 2017, and should say so wherever the two are compared (§C.7).

---

## C.6 The interim shortcut and its hazard — screener.in and peers

**What it is.** Screener.in (and similar India retail-analytics sites — Tijori Finance, Trendlyne,
Tickertape) aggregates the same primary filings this Part specifies (BSE's filing repository plus
company annual reports) into a convenient, human-browsable, multi-year P&L/balance-sheet/cash-flow
table per company, with **no public API** — access is via the website itself or a rate-limited
"Export to Excel" feature, and the site's own guidance asks users to make "reasonable-rate
requests" and comply with applicable law when scripting against it **[VERIFY: exact wording of
screener.in's own Terms of Use — not independently retrieved in full this pass; treat the
"reasonable-rate, no public API" characterization as directionally confirmed, not a verbatim
quote]**.

**The hazard, precisely.** Screener (and peers) display **today's best-known, latest-restated**
figures against historical periods — there is no vintage archive, no way to ask "what did this
site show for FY2019 book value back in 2019." Pulling a 10-year fundamentals history from
screener.in **today** and backtesting against it silently reintroduces the exact restatement-
driven look-ahead bias Known Prior #7 prices at 150–450bps/yr, in a *more* concentrated form than
even a careless direct-from-filing pull, because the aggregator has already discarded whichever
vintage information it might once have carried. This is structurally the same failure mode as
trusting "current constituents" for a historical universe (momentum Part C §C.3) or applying
today's ASM/GSM band to a historical date (A-catalog A6/A7) — a snapshot standing in for a
point-in-time record.

**The rule — exploration-only, never evidence, mirroring the Kaggle/HF rule.** The 2026-09-01
mirror-authorization decision (`research/OPEN_QUESTIONS.md`) sets the house discipline for
external, non-primary data: authorized for use, but every pull sha256-manifested, authenticated
against an independent mirror or published fact before use, PIT/vintage caveats recorded, and a
mirror never outranks the primary source once the principal's-machine primary pull exists.
Screener.in and its peers earn the identical treatment, generalized from "third-party mirror of a
primary series" to "third-party aggregator of a primary filing corpus with no vintage layer": fine
for fast exploration (spot-checking a company's rough profile, sanity-testing a candidate signal,
orienting a new analyst), **never as the fixture a backtest is evaluated against**. The house's own
free-data panel — built directly from Reg. 33/23/29/31 filings with `knowledge_time` discipline
(§C.1) — is the only instrument allowed to answer this program's central question (Known Prior
#7); a screener.in-sourced backtest answers a different, easier, silently biased question.
Kaggle/HuggingFace-hosted India fundamentals datasets (several surfaced incidentally in this
pass's searches) inherit the identical rule and the identical access note already on file: both
hosts are blocked at this environment's egress proxy but authorized for the principal's machine
(`ingest/README.md`'s addendum) — same authentication-before-use discipline, not a lighter one
just because the file looks larger or more structured than a screener.in export.

---

## C.7 Validation — two acceptance gates before our constructed ratios are trusted

**Gate 1 — the India factor mirror's HML.** The desk already holds the AJV/IIMA India Fama-French-
momentum data library as the external validation benchmark for momentum (momentum Part C §C.6) and
has pulled its HML series into `value-panel-RESULTS.md` (V1–V4: India HML full-sample +8.6%/yr
ann. mean, 1994–2014 sub-period +7.1%/yr, correlation with WML **−0.37**, five documented India
"value winters," the worst — 1996-02 to 2003-06 — reaching **−59%** peak depth). **Reuse this
exact benchmark, do not build a second one**: reconstruct our own B/P-based long-short decile HML
over AJV's sample window and apply the same acceptance bar momentum Part C proposes for WML —
monthly correlation **≥0.85**, raw (pre-haircut) annualized mean within roughly **65–100% of AJV's
published HML** (a design choice, not literature-sourced, flagged as such there and carried
forward unchanged: a reconstruction landing below the haircut range means a construction gap, not
deeper decay, and must be investigated first). AJV's update cadence (3×/year) may not have stayed
current through 2025–2026 **[VERIFY, same open item as momentum Part C]** — treat any gap past its
last confirmed vintage as un-validated, not assumed-fine.

**Gate 2 — NSE's own daily-published index P/E, P/B, and dividend yield.** NSE publishes these
three ratios **daily**, for every broad-market and sectoral index it maintains, at
`nseindia.com/reports-indices-yield` (current live report) with historical depth described by
multiple independent sources as reaching back to **1999** **[VERIFY exact first-published date —
several secondary sources cite 1999 for Nifty/Sensex-family P/E history but this pass did not
independently confirm NSE's own stated inception date for the specific yield-report series]**; a
mirrored historical file also sits under `niftyindices.com/reports/historical-data` (already
catalogued for TRI pulls, B1–B4). **Cheaper and always-on relative to Gate 1**: unlike AJV's
3×/year library, NSE republishes its own index-level P/E/P/B/dividend-yield figure every trading
day, checkable continuously. The test: at each rebalance date, compute the free-float-cap-weighted
E/P and B/P across our own fundamentals panel, restricted to the point-in-time Nifty 50/500
constituent set (momentum Part C §C.3), and compare against NSE's own published index-level P/E
and P/B for the identical date/index. **Acceptance bar (design choice, flagged as such)**:
aggregate tracking difference within a few percentage points, persistently — a persistent gap
flags a coverage error (missing constituents, mis-held stale book values) or a weighting mismatch,
and must be resolved before the panel is trusted for cross-sectional ranking. This gate validates
the panel's **level**; Gate 1 validates its **cross-sectional discrimination** — complementary,
neither substitutes for the other.

---

## C.8 PIT/vintage hazard table and construction pipeline

| Source | Revision-prone? | Two dates that must never be conflated | Store first-print or latest? |
|---|---|---|---|
| Reg. 33 financial results (quarterly/annual) | **Yes, explicitly** (revised-XBRL mechanism) | Fiscal-period-end vs. `knowledge_time` (announcement/PDF-filing timestamp, §C.1) | **First-print AND every revision**, each its own vintage row keyed by `(company, period, filing_type, knowledge_time)` — never overwrite |
| Reg. 31 shareholding pattern | Format-revision-prone (integrated-filing transition), values not typically restated | As-of-quarter-end vs. filing date (≤21 days) | Latest per quarter; format version tagged (A-catalog C3) |
| Reg. 29/31 SAST (pledge) | Not revision-prone; rule-vintage matters (SAST amended multiple times since 2011) | Event date vs. disclosure date | Append-only event log (A-catalog C1/C2) |
| Reg. 23(9) RPT | Not revision-prone | Half-year-end vs. 30-day-post-publication filing date | Latest per half-year |
| Reg. 30 auditor events | Not revision-prone; event-based | Event date vs. ≤24h disclosure date | Append-only event log |
| CRA rating actions | Not revision-prone; each action is its own record | Rating-committee date vs. ≤7-working-day press-release date | Append-only event log per issuer |
| Screener.in/peer aggregators (§C.6) | **Effectively always stale to the pull date** — no vintage layer exists to store | Pull date only (no published-as-of date recoverable) | Exploration cache only, never a fixture a backtest reads |
| AJV/IIMA HML (validation) | Methodology-revision-prone (per momentum Part C §C.7) | Release-vintage vs. pull date | Every release kept, never only-latest (identical rule, same table row style as momentum Part C) |
| NSE index P/E-P/B-yield (Gate 2) | Not restated | T+0 | Latest — no PIT problem |

**Construction pipeline** (ordered, script-followable, matching momentum Part C §C.8's numbering
convention):

1. **Registry load.** Validate `config/sleeves.yaml factor_book.value`/`.quality` and
   `config/ladder.yaml L8_value_spread` against `config/validator.py` before any pull.
2. **Pull raw Reg. 33/23/29/30/31 filings** into `data/raw/{nse,bse}/financial_results/`,
   `.../rpt/`, `.../pledge/`, `.../auditor_events/`, `.../shareholding_pattern/` — **no existing
   ingest script covers any of this; this Part surfaces the gap** (see closing note below).
   Manifest every file immediately (`python ingest/manifest.py data/`).
3. **Build the XBRL-era parser** (2017-04-01 boundary) and, separately, the **Integrated-Filing
   parser** (2025-04-01 boundary) — two schema versions, per §C.1's table; normalize both into one
   internal fundamentals schema (`company, fiscal_period, filing_type, knowledge_time, field,
   value, is_revision`) before any downstream ratio touches the data.
4. **Apply the `knowledge_time` discipline** (§C.1): every fact enters the panel timestamped by its
   actual filing moment, never by fiscal period-end; a revision lands as a new row, never an
   overwrite.
5. **Build the staircase-holding logic** for half-yearly/annual-only fields (book value, cash flow,
   total assets, total debt, current assets/liabilities — §C.2): hold the last-disclosed value flat
   between disclosure dates; never interpolate a smooth quarterly path.
6. **Compute the ratio panel** per §C.3: E/P and sales/price at quarterly cadence; B/P and CF/P on
   the staircase; EV/EBITDA and gross profitability as explicitly mixed-frequency; exclude
   financials from universe-wide raw pooling, route them to a sector-relative-only P/E-P/B path.
7. **Compute the quality panel** per §C.4: the 2 genuinely-quarterly Piotroski signals at quarterly
   cadence, the 7 balance-sheet/cash-flow-gated signals on the staircase; pledge/RPT/auditor/rating
   governance flags each on their own native event cadence (§C.4's table).
8. **Cross-financials sector-relative ranking**: build the separate banks/NBFC/insurer ranking path
   (§C.3), never pooled with non-financials on a universe-wide percentile.
9. **Validate — Gate 1**: reconstruct the long-short B/P decile HML over AJV's sample window;
   check correlation ≥0.85 and magnitude within 65–100% of AJV's published HML; log any divergence.
10. **Validate — Gate 2**: compare our panel's aggregate E/P and B/P against NSE's own daily
    published index-level P/E and P/B for the same date/index; require a persistently small
    tracking difference before trusting the panel for cross-sectional ranking.
11. **Manifest every derived fixture** (fundamentals panel, ratio panel, quality panel, governance-
    flag panel) as its own versioned, checksummed artifact; corrections append a new vintage row,
    never overwrite — identical WORM discipline to momentum Part C §C.7/§C.8.
12. **Recalibration triggers**: re-run whenever (a) a new AJV/IIMA release lands; (b) a semi-annual
    balance-sheet disclosure round completes (Sept-end, March-end) and the staircase steps; (c) the
    Integrated-Filing schema is itself revised; (d) book AUM moves ±50% (existing `costs.yaml`
    trigger, unchanged).

**Impact on existing ingest scripts (a genuine gap this Part surfaces, not a re-statement of a
known one).** `ingest/README.md` and the existing `ingest/pull_*.py` scripts (bhavcopy, AMFI, FRED,
indices, NSDL FPI) cover **price, macro, and flow data only** — there is currently **no script for
company fundamentals at all**: no `pull_nse_financial_results.py`, no RPT/pledge/auditor-event
puller, no XBRL parser for either schema era. This is a materially larger gap than the two
momentum Part C already flagged (BSE bhavcopy puller, BSE/NSE corporate-actions puller) since
nothing here has even a stub — the fundamentals ingest kit for the moderate book's factor engine
must be built from this Part's specification, not patched from an existing script. Recommend
adding to `ingest/README.md`'s day-1 runsheet: a new `pull_nse_financial_results.py` (Reg. 33,
both schema eras), a `pull_nse_governance_events.py` (Reg. 23/29/30/31 combined, since they share
the same corporate-filings-portal family and access pattern), and the XBRL-to-internal-schema
parser as its own module, versioned separately per §C.1's schema-era table.

---
*End of Part C. Cross-references: `docs/masterplan/A-data-catalog.md` (no fundamentals block —
this Part is the first), `research/cycles/momentum-deep/partC-data.md` (bhavcopy/CA/survivorship
mechanics reused, not duplicated), `research/cycles/value-deep/value-panel-RESULTS.md` (India HML
mirror figures, §C.7 Gate 1), `research/dossiers/02-value-quality-lowvol.md` (theory/evidence/decay
this Part builds data for), `config/ladder.yaml` L8, `config/sleeves.yaml
factor_book.value`/`.quality`, `research/OPEN_QUESTIONS.md` (mirror-authorization note, applied to
screener.in/peers in §C.6), `research/CONTRACT.md` §3 (free-source mandate), Known Prior #7
(restatement bias), §8 (no fundamental backtest without its price-only counterpart — already
satisfied for momentum by its price-only WML; this Part's value/quality construction must be
paired against a price-only counterpart the same way before either is reported).*


---

# PART D/E/F/H — Mathematics, algorithm, harvest map, knowledge ledger

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
