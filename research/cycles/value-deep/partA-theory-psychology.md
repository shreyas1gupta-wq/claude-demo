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
