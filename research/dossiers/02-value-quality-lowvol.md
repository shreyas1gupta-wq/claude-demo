# Dossier 02 — Value, Quality, Low-Volatility, Size (Moderate Book Factor Engine)

Workstream owner: research analyst (Claude), cycle-stack program. Status: RESEARCH ONLY, complies
with `research/CONTRACT.md` v0.1 and assumes all `OPEN_QUESTIONS.md` defaults (notably Q1: Nifty 500
TRI as the signal-research benchmark; Q6: moderate book is the anchor/engine).

---

## 1. Findings and literature

**Fama & French (1992), "The Cross-Section of Expected Stock Returns," *Journal of Finance* 47(2).**
Size and book-to-market jointly absorb the cross-sectional variation in average returns that beta
alone does not explain; the beta-return relation goes flat once size is controlled. Foundational —
this is the origin of both the size and value factors used everywhere since. Verified (Wiley/JSTOR
listing, widely cross-cited).

**Fama & French (2015), "A Five-Factor Asset Pricing Model," *Journal of Financial Economics* 116(1).**
Adds profitability (RMW) and investment (CMA) factors; **value (HML) becomes statistically redundant**
once profitability and investment are included — i.e., a large share of the historical value premium
is explainable by (or overlapping with) a profitability/quality tilt. Effect: the model materially
improves average pricing errors versus the 3-factor model but still misses low-return, high-investment
small stocks. Verified.

**Asness & Frazzini (2013), "The Devil in HML's Details," *Journal of Portfolio Management*.**
The standard academic HML uses lagged book value matched with 6-month-stale price (frozen until next
annual rebalance), which mismeasures current cheapness. Using current price (HML-Devil) materially
changes the factor's properties — it correlates more with momentum, has different crash behavior, and
loses some of the "distinct from momentum" character of classic HML. Direct methodological warning for
any value construction: **the price-staleness convention is itself a design choice with return
consequences**, not a neutral default. Verified (AQR + SSRN + Journal of Portfolio Management listing).

**Cohen, Polk & Vuolteenaho (2003), "The Value Spread," *Journal of Finance* 58(2).**
Decomposes cross-sectional book-to-market variance: only ~20–25% of the dispersion in B/M reflects
transitory mispricing-relevant variation in expected long-horizon (15-year) returns; the rest reflects
differences in expected long-run profitability and the persistence of valuation levels. Critically:
**the expected return to a value-minus-growth strategy is unusually high precisely when the
book-to-market spread between cheap and expensive stocks is wide** — the value spread predicts the
value factor's own forward return. This is the direct evidentiary basis for using the value spread as
a factor-weight conditioner. Verified.

**Novy-Marx (2013), "The Other Side of Value: The Gross Profitability Premium," *Journal of Financial
Economics* 108(1).** Gross profits-to-assets predicts returns with "roughly the same power" as
book-to-market; profitable firms earn higher average returns despite lower B/M and larger size.
Controlling for profitability materially improves value-strategy performance, especially among large,
liquid stocks. Effect size: comparable in magnitude to the value premium itself. Verified.

**Asness, Frazzini & Pedersen (2019), "Quality Minus Junk," *Review of Accounting Studies* 24(1),
34–112.** Defines quality via profitability, growth and safety; a QMJ long-short factor earns
significant risk-adjusted returns in the US and across 24 countries. High-quality stocks trade at only
modestly higher prices than their quality would justify — i.e., the market underprices quality, which
is the behavioral/mispricing half of the story. Verified.

**Piotroski (2000), "Value Investing: The Use of Historical Financial Statement Information to
Separate Winners from Losers," *Journal of Accounting Research* 38 (Supplement).** Among high
book-to-market (value) firms, a 9-signal fundamental F-Score separates future winners from losers:
F-Score 8–9 beats the market by +7.5%/yr; F-Score 0–1 lags by −8.3%/yr; a long high-F-Score /
short low-F-Score strategy earned 23%/yr, 1976–1996 (pre-cost). This is a *conditioning* overlay on
value (screens out "cheap for a reason" value traps), not a standalone factor. Verified.

**Sloan (1996), "Do Stock Prices Fully Reflect Information in Accruals and Cash Flows about Future
Earnings?" *The Accounting Review* 71(3).** Earnings driven by accruals is less persistent than
earnings driven by cash flow; investors overweight accruals when forming expectations, producing the
accrual anomaly — low-accrual firms outperform high-accrual firms. Mechanism is a specific,
well-documented behavioral bias (naive fixation on earnings, not its components). Verified.

**Ang, Hodrick, Xing & Zhang (2006), "The Cross-Section of Volatility and Expected Returns," *Journal
of Finance* 61(1).** High idiosyncratic volatility (relative to Fama-French 3-factor residuals)
predicts abysmally *low* future returns — a >1%/month spread between low- and high-idio-vol quintiles,
unexplained by aggregate volatility risk exposure. Labeled by the authors themselves "a substantive
puzzle" — the low-vol effect is not comfortably a risk premium. Verified.

**Frazzini & Pedersen (2014), "Betting Against Beta," *Journal of Financial Economics* 111(1).**
Leverage- and margin-constrained investors bid up high-beta assets, flattening (or inverting) the
security market line; a BAB factor (long leveraged low-beta, short high-beta) earns significant
risk-adjusted returns across US equities, 20 international equity markets, Treasuries, credit, and
futures. **This is the cleanest available structural/institutional-constraint mechanism in the whole
low-risk literature** — it names a specific, persistent reason (leverage aversion) that does not
require the anomaly to be "unknown" to survive. Verified — one of the most-cited JFE papers of the
decade per the search results.

**Blitz & van Vliet (2007), "The Volatility Effect: Lower Risk Without Lower Return," *Journal of
Portfolio Management* (Fall).** Global low-vol decile beats high-vol decile by ~12%/yr in
risk-adjusted (alpha) terms, 1986–2006, replicated separately in US, Europe, Japan; not explained by
size or value. Attributes effect to leverage restrictions, two-step (benchmark-then-tilt) institutional
processes, and behavioral overpayment for lottery-like high-vol names. Verified.

**Arnott, Beck, Kalesnik & West (2016), "How Can 'Smart Beta' Go Horribly Wrong?" Research
Affiliates.** Warns that a strategy's *own* multiple expansion (valuation re-rating) — not a repeatable
premium — explains much of its trailing outperformance; the more a factor/strategy has re-rated
upward, the worse its forward return, i.e., **factors themselves have value spreads that mean-revert.**
Companion piece Arnott, Beck & Kalesnik (2017), "Timing 'Smart Beta' Strategies? Of Course! Buy Low,
Sell High!" (SSRN 3040956) formalizes a contrarian, relative-valuation-based factor-timing rule and
finds it adds value versus trend-chasing. [The task brief attributes a "Shakernia" co-authorship to
this stream; every retrievable citation instead shows **Beck, Kalesnik, West** as Arnott's co-authors on
these two papers — flagged `[VERIFY: no Arnott/Kalesnik/Shakernia-coauthored paper matching this title
was found; treating the Beck/Kalesnik/West authorship as correct]`.] Companion caution: Arnott, Beck &
Kalesnik, "Forecasting Factor and Smart Beta Returns (Hint: History Is Worse than Useless)" argues
naive historical-average factor forecasts are actively harmful — valuation-based timing, not
performance-chasing, is the only defensible conditioning approach. Verified (SSRN listings).

**Lou & Polk, "Comomentum: Inferring Arbitrage Activity from Return Correlations" (working
paper/AQR Insight Award; published as Lou & Polk 2020ish in *Journal of Political Economy* lineage —
long-standing working paper, LSE).** Constructs a crowding proxy from the *excess pairwise return
correlation* among stocks that share a momentum rank — when winners start moving together more than
their characteristics justify, a common (crowded) investor base is inferred, and this "comomentum"
measure predicts subsequent momentum crashes. Methodologically important beyond momentum: **the same
excess-correlation-inside-the-basket technique could be built for value, quality or low-vol baskets as
a forward-looking, factor-agnostic crowding early-warning signal** — this is not literature-backed for
non-momentum factors yet, so it is a proposed *construct*, not an established finding. Verified
(multiple LSE/AQR mirror copies).

**Pontiff & Woodgate (2008), "Share Issuance and Cross-Sectional Returns," *Journal of Finance* 63(2).**
Net share issuance predicts returns with statistical power exceeding size, B/M or momentum
individually, post-1970 in the US. Mechanically important here: **NSI is constructible from price and
shares-outstanding data alone** (no income-statement or balance-sheet line item), making it one of the
least restatement-exposed value-adjacent signals available. Verified.

**Asness, Frazzini, Israel, Moskowitz & Pedersen (2018), "Size Matters, If You Control Your Junk,"
*Journal of Financial Economics* 129(3), 479–509.** Answers essentially every historical objection to
the size premium (weak, concentrated in January/microcaps, price-based only, international weakness) by
showing that **controlling for quality/junk resurrects a size premium of comparable economic magnitude
to value and momentum**, stable through time, robust in 30 industries and 24 international markets, and
present in non-price-based size measures too. Verified. `[VERIFY: could not confirm from search results
whether India is among the 24 non-US markets tested in this specific paper — treat the India
application as an untested cross-country extrapolation until checked directly against the paper's
country list in the data phase]`.

**Israel & Moskowitz (2012/2020 updated), "How Tax-Efficient Are Equity Styles?" (NBER/SSRN 2089459).**
Direct, load-bearing quantitative confirmation of the prior pass's "value/quality run ~5× momentum's
half-life" claim: the paper states explicitly that **momentum has roughly five times the turnover of
value**, while both factors face similar overall tax burdens because value's exposure is
dividend/income-heavy while momentum's is capital-gains-heavy (and momentum generates offsetting
short-term losses). This is the strongest available quantitative anchor for Known Prior #10 and #6 in
the CONTRACT — treat it as Tier B (single paper, robust methodology, US data) rather than "assumed."
Verified.

**McLean & Pontiff (2016), "Does Academic Research Destroy Stock Return Predictability?" *Journal of
Finance* 71(1).** 97 cross-sectional return predictors decay 26% out-of-sample (pre-publication,
i.e., pure statistical/regime effects) and 58% post-publication (informed trading effect ≈ 32
incremental points). Post-publication decline is largest for predictors with the highest in-sample
returns and for those concentrated in illiquid/high-idiosyncratic-risk names — this is exactly the
small-cap/illiquid corner of the size and low-vol literatures. Verified — this is the CONTRACT's own
governing citation (§5), re-confirmed here.

**Jacobs & Müller (2020), "Anomalies Across the Globe: Once Public, No Longer Existent?" *Journal of
Financial Economics* 135(1).** Tests 241 anomalies in 39 markets: **the US is the only country with a
reliable post-publication decline**; other markets show a mostly insignificant post-publication decay,
attributed to segmented markets and higher barriers to arbitrage abroad. This *raises*, not lowers, the
prior for India-specific persistence of value/quality/low-vol relative to a naive US-decay assumption —
but the paper's own interpretation is that non-US persistence reflects arbitrage frictions (a real
capacity/institutional-constraint story, tier iv in the CONTRACT's decay-survival taxonomy), not that
the effects are somehow larger risk premia. Verified.

**Chordia, Subrahmanyam & Tong, "Have Capital Market Anomalies Attenuated in the Recent Era of High
Liquidity and Trading Activity?"** Anomaly-strategy average returns roughly halved post-decimalization
in the US as liquidity and arbitrage capital (hedge fund AUM, short interest, turnover) increased.
Directionally consistent with McLean-Pontiff but mechanistically different (liquidity/capital-driven,
not publication-driven). A published follow-up disputes the international robustness of this specific
liquidity channel. Verified, with the caveat noted.

---

## 2. India-specific evidence

**Agarwalla, Jacob & Varma (2013/2017), "Four Factor Model in Indian Equities Market" (IIMA WP) /
"Size, Value, and Momentum in Indian Equities," *Vikalpa* 42(4), 2017.** The standing India Fama-French
+ momentum data library (CMIE Prowess-based, survivorship-corrected, illiquid-name-excluded,
July–June fiscal alignment to avoid look-ahead bias). Jan 1994–Dec 2014: momentum (WML) avg 21.9%/yr,
value (HML) avg 15.3%/yr, size (SMB) ≈ 0%/yr, market premium 11.5%/yr. **Two load-bearing facts for
this workstream: (i) India's raw, unconditional size premium is essentially zero over 20 years — this
alone answers "is there a size premium in India" in the negative for the *naive* factor; (ii) value in
India has *not* shown the "momentum is 5× the turnover, so 1/5 the cost" advantage empirically diluted
— HML's average return is actually higher than the market premium itself in this sample**, though this
is a raw-return not risk-adjusted or cost-adjusted comparison. Verified; maintained and updated at
jrvarma.in.

**Agarwalla, Jacob, Varma & Vasudevan (2014), "Betting Against Beta in the Indian Market" (IIMA
WP2014-07-01 / SSRN 2464097).** A BAB factor earns significant positive returns in India and **its
returns dominate size, value and momentum in this sample** — but CAPM-adjusted BAB premia are largely
explained once a profitability/quality factor is added, i.e., **India's low-beta effect looks like a
quality effect in beta's clothing**, echoing Asness-Frazzini-Israel-Moskowitz-Pedersen's US/global
"size matters if you control your junk" logic in reverse (here: "beta matters, if you control your
junk"). Verified.

**Harshita, Singh & Yadav (2018), "Changing Nature of the Value Premium in the Indian Stock Market,"
*Global Business Review*.** Documents that the value premium's character has shifted over the sample —
consistent with a decaying-and-mutating effect rather than a stationary one. Sharma, Srikanth &
Suresha (2022), "Is Industry-Specific Value Premium Declining? Evidence from India," similarly finds
industry-level attenuation. Both verified by title/journal search; full effect sizes not independently
confirmed — `[VERIFY: exact decay magnitude in these two India-specific value-decay papers]`.

**India size-premium practitioner literature (Incwert annual "India Size Premium Study," 2021–2025
editions).** NSE-listed-firm data from 1995 onward; finds mid/small/micro-cap betas-adjusted returns
exceed CAPM-predicted returns, i.e., **a positive size premium net of beta**, and states the Indian
size premium is larger than typical US estimates. This is a valuation-industry (not peer-reviewed
academic) series aimed at discount-rate practice, so it is methodologically closer to a size-tilted
excess-return audit than a factor-model test; it does **not** decompose size from illiquidity or from
quality, which is exactly the ambiguity the CONTRACT's question is asking about. Tier and confidence
downgraded accordingly (see §5). `[VERIFY: Incwert's precise premium magnitudes and break-point
methodology — not independently re-derivable from search snippets]`.

**Illiquidity premium in India (multiple 2010s–2020s papers using Amihud-type measures).** The Indian
illiquidity premium is found to be larger than in developed and many other emerging markets, and — as
in the US/global small-cap literature — the effect is concentrated in the extreme smallest-cap
quintile, which is economically tiny (well below 1% of market cap). **This is the direct evidence that
"size" and "illiquidity" are conflated in raw India size studies**: AJV's near-zero raw SMB (large
universe, illiquid names excluded) versus Incwert's positive size premium (unfiltered universe,
CAPM-beta-only control) is consistent with the premium living almost entirely in the illiquid tail that
AJV's methodology deliberately excludes. For the **moderate book** (ranks ~1–500, i.e., excluding the
illiquid micro tail that lives in ranks 500–750), this means: **do not expect to harvest a distinct,
liquidity-free size premium inside the moderate book's own universe** — any size premium the aggressive
book captures in ranks 500–750 is substantially an illiquidity premium, which is a capacity-limited,
not free, source of return (relevant to CONTRACT Known Prior #3's "return system" framing).

**Promoter share pledging (multiple 2023–2025 India papers, e.g. "Promoter Share Pledging and Downside
Risk: Evidence from Indian Listed Firms").** Pledging is positively associated with future stock-price
crash risk and negatively with financial performance; pledging firms show worse CVaR/VaR, deeper
drawdowns, more negative minimum returns. This is an **India-specific, structurally distinct quality
signal** with no direct US analogue at this scale (US firms rarely pledge control-block shares against
personal margin loans the way Indian promoters do) — it belongs in a India-tailored "junk" definition,
not just imported QMJ components. Pledge data is disclosed under SAST/takeover-code rules (5%/10% etc.
thresholds) and is available from exchange/company filings — a genuinely free, India-specific,
point-in-time-friendly quality signal. Verified directionally; magnitude not independently re-derived.

**Related-party transactions and earnings management (multiple India papers, e.g. IIMA WP "An Analysis
of Related Party Transactions in India").** RPTs are a documented, common vehicle for earnings
management and value extraction in India's business-group-dominated ownership structure, with
disclosure required under Companies Act 2013 / SEBI LODR for transactions above thresholds. This is
direct India-specific support for the CONTRACT's "restated fundamentals" concern: **earnings and
book-value-adjacent metrics in India carry an additional, structurally motivated distortion channel
(promoter-linked RPTs) beyond ordinary restatement**, on top of the accounting-standard-transition
noise from the Ind-AS rollout (mandatory for large listed cos from FY2016-17, phased by size — full
comparative restatement is required in transition year filings). Verified qualitatively;
`[VERIFY: no single study found quantifying India-specific restatement magnitude in bps terms — the
150–450bps figure in CONTRACT Known Prior #7 is carried forward from the prior pass, not independently
re-derived here]`.

**NSE/BSE live strategy indices — the closest thing to a walk-forward, real-money-tested India factor
track record:**
- **Nifty200 Quality 30** — base date 1-Apr-2005 (base 1000), **launched 2018** (business-standard,
  April 2018). Score = ROE, D/E, 5-yr earnings-growth variability; weight = quality-score ×
  free-float-mcap, capped 5%/stock; semi-annual reconstitution. ~8 years of live (non-backtested)
  history by 2026 → **Tier B by the CONTRACT's own observation-count rule** (4–30 obs), not Tier A.
- **Nifty500 Value 50** — **launched 24-Oct-2018**. Score = E/P, B/P, sales/price, dividend yield;
  semi-annual rebalance (May/Nov cutoffs). ~8 years live → Tier B.
- **Nifty Alpha Low-Volatility 30** — base date 1-Apr-2005, **launched 10-Jul-2017**; selects 30 of the
  top-150 large/midcaps by a blend of trailing-1y Jensen's alpha and low realized volatility, 5% stock
  cap. ~9 years live → Tier B, and notably this is a **momentum-tilted** low-vol construct (alpha +
  low-vol jointly), not a pure defensive low-vol index — a design detail that matters if the moderate
  book wants low-vol as *crisis ballast* rather than as a return-enhancer, since alpha-tilted low-vol
  baskets can still be crowded/expensive going into a drawdown.
- **Nifty500 Low Volatility 50** and **Nifty500 Quality 50** — **launched only ~23-Dec-2024**
  (Business Standard). By Aug-2026 these carry under 2 years of live history — **Tier C by the
  CONTRACT's own rule ("<4 observations")**; any factsheet-quoted "since-inception CAGR" for these two
  is a backtest-extension artifact for anything before launch and must be treated as such.
  `[VERIFY: exact base dates/backtest-start dates for these two — niftyindices.com and bseindices.com
  are both egress-blocked in this environment per CONTRACT Known Prior #11; confirm on the principal's
  machine in the data phase]`.
- Fund-level "since inception" CAGR figures quoted by AMCs for these index funds (e.g., a UTI Nifty 500
  Value 50 fund citing 32%+ CAGR) reflect a short, post-2023 bull-market launch window and are **not**
  usable as a factor-premium estimate — they are single-path realizations over a period too short and
  too favorable to generalize (this is precisely the "it backtests well" trap the CONTRACT forbids).

**Smart-beta crowding in India — AUM evidence.** Indian smart-beta index-fund AUM grew roughly
160× from ~₹290cr (2020) to ~₹46,000cr (end-2025), ~12% of passive equity AUM; **low-volatility funds
carry the second-largest AUM segment (~₹7,400cr as of Aug-2024)** and minimum-volatility/multi-factor
products were flagged as the largest driver of new smart-beta flows through 2025. This is *fast-growing
but still small in absolute terms* relative to the moderate book's own ₹1,000–2,500cr size — capacity
is not yet obviously binding at this book's scale, but the growth *rate* (not yet the level) is the
crowding signal to monitor going forward, and it argues for building an explicit AUM-growth trigger
into any low-vol/quality sleeve's ongoing evidence review (see §6). Verified (Cafemutual / industry
AUM reporting).

**Low-volatility anomaly in India — academic evidence is genuinely mixed**, unlike the developed-market
literature. Pandey (2001–2011, Nifty 500 constituents) and a follow-on Pandey & Prachetas (2000–2012,
51 NSE stocks) both find low-vol outperformance on a risk-adjusted basis. A separate study using the
S&P CNX 100 (2001–2014) **does not find a significant low-volatility anomaly** and instead finds the
high-volatility quintile outperforming. This directly conflicts and should not be smoothed over: India's
low-vol edge is less settled in the academic literature than the live-index track record (NIFTY Alpha
Low-Vol 30, 2017–2026) suggests. Verified as a genuine literature split, not a single clean finding.

**STT, ASM/GSM, and SAST as India-specific structural facts relevant to factor construction:**
- **STT** (0.05%/leg futures, 0.15%/leg options as of the April-2026 hike; ~0.1% delivery equity) is a
  turnover-linear, unavoidable cost baked into any factor rebalance — it mechanically favors low-
  turnover factors (value, quality, low-vol at semi-annual rebalance) over high-turnover ones (momentum,
  reversal), reinforcing rather than merely coexisting with the "5× turnover" cost asymmetry from
  Israel-Moskowitz.
- **ASM/GSM** (Additional/Graded Surveillance Measures) impose reduced price bands, higher margins, and
  T2T (trade-to-trade, no netting) status on stocks showing unusual price/volume behavior; entry into
  even Stage 1 GSM has a documented "significant impact" on price. This mechanically dampens realized
  momentum and inflates realized volatility (via wider effective spreads and forced settlement
  frictions) for the exact small/mid-cap names most likely to appear in aggressive-book momentum or
  micro-cap value/size baskets — a genuine, India-specific institutional friction absent from any
  US/global factor paper, and a reason the moderate book (large/mid-cap, ranks 1–500) is structurally
  cleaner ground for factor investing than the aggressive book's tail.
- **SAST (Takeover Code) 5%/10%/14% disclosure thresholds** make promoter/large-holder stake changes and
  pledge status a free, point-in-time, exchange-filed data source — directly usable for a price-adjacent
  "junk" signal (§4) without touching restated financials.

---

## 3. Decay and crowding assessment

**Value (B/P, E/P, sales/price, dividend yield composite).** *Survival argument*: (iii) genuine risk
premium (distress/financial-leverage risk, still argued in Fama-French lineage) blended with (i) a
behavioral mechanism — extrapolation of past growth/decline (Lakonishok-Shleifer-Vishny-style, not
separately re-verified here but foundational to the whole value literature) — that plausibly persists
under crowding because it is rooted in how humans forecast, not in a temporary information gap. Global
decay evidence: McLean-Pontiff's 26%/58% is an average across 97 predictors, not value-specific, but
value is one of the oldest, most crowded-into anomalies in the sample, so it should sit toward the
*higher* end of that decay range for the pure "cheap minus expensive" signal, while Jacobs-Müller's
finding of insignificant post-publication decay **outside the US** cuts the other way for India
specifically. **Numeric haircut: 30–40% off any in-sample India value effect size, applied as Tier B**
(cross-country prior blended with India's own ~20-year AJV series), revisited when India-specific
purged-CV estimates exist. Crowding measure: the value spread itself (Cohen-Polk-Vuolteenaho) — track
its own percentile as a live crowding gauge, not AUM flows (AUM data for value-specific products in
India is not cleanly separable from quality/multi-factor products in the smart-beta AUM figures found).

**Quality/profitability (ROE, D/E, earnings stability, gross profitability, pledge-adjusted junk
score).** *Survival argument*: (i) behavioral under-reaction to profitability persistence (Novy-Marx,
QMJ) plus, in India specifically, (iv) an institutional constraint unique to the market — promoter
pledging and RPT-driven earnings management are *structural*, ownership-concentration-linked frictions
that a quality filter is pricing, not a fad that arbitrage competes away, because the underlying
governance risk does not disappear when more capital chases quality names. Countervailing crowding
evidence: quality traded >1 std-dev rich relative to its own long-run valuation in H2-2024, then gave
back that richness through 2025's "worst year for international quality relative performance since
1999," with a documented "quant unwind" in mid-2025 driven partly by quality/low-vol/AI-momentum
crowding unwinding together. **This is a live, recent (2024–2025) demonstration of Arnott-Beck-Kalesnik's
thesis that a factor's own re-rating, not a repeatable premium, drove its trailing return — exactly the
"revaluation alpha" trap.** **Numeric haircut: 25–35%**, Tier B, with an explicit valuation-based
kill-switch (see §4) rather than a static discount, because the 2024–25 episode shows the crowding is
time-varying and detectable in relative valuation before it unwinds.

**Low-volatility.** *Survival argument*: (iv) institutional constraint — Baker-Bradley-Wurgler-style
benchmark-relative mandates plus explicit leverage aversion (Frazzini-Pedersen's BAB mechanism) are the
cleanest, most literature-supported "why does this survive being known" answer in the whole factor set,
because the constraint is structural (fund mandates, career risk against tracking error) rather than
informational. Countervailing note found in the search: **hedge funds, which are not leverage- or
short-constrained, have been shown to bet *against* low-vol** — i.e., the least-constrained arbitrageurs
do not uniformly validate the anomaly, which tempers confidence that the effect is a pure, permanent
structural giveaway. India overlay: the mixed academic evidence (§2) plus rapidly growing (if still
modest-level) India smart-beta AUM concentrated in min-vol products argues for treating India low-vol as
**less settled than the developed-market literature**, not more. **Numeric haircut: 30–40%**, Tier B
(India live-index observation count is 8–9 years, squarely inside the CONTRACT's 4–30 Tier-B band), with
an AUM-growth-rate trigger (§6) as the live crowding monitor since no long India value-spread-style
series exists yet for low-vol specifically.

**Size (raw vs. quality-controlled).** *Survival argument for the raw effect*: essentially none — AJV's
~20-year India SMB average is ≈0%, consistent with the CONTRACT's own instinct to be skeptical of
"it backtests well" claims; a size tilt with no controls is not admissible on the India evidence
gathered here. *Survival argument for the quality-controlled version*: (ii) capacity limit (small/mid
caps have genuinely less capacity, keeping large capital thinner there) combined with (iii) a residual
risk premium once the "junk contamination" (financially fragile small caps that mechanically drag down
the naive small-cap basket) is filtered out — this is the Asness-et-al-2018 mechanism, not yet directly
tested on India data. **Because this specific construct is unverified for India** (Tier C for the
India-specific claim, Tier A only for the global/US evidence it is imported from), it should enter the
moderate book, if at all, as a small satellite weight with an explicit note that it is a cross-country
extrapolation pending direct India testing in the data phase — **not** as a core sleeve. The distinct,
larger, and better-evidenced India small-cap effect is the **illiquidity premium**, which the moderate
book's own ranks-1–500 universe substantially screens out by construction (that premium lives in ranks
500–750, i.e., the aggressive book).

**Cross-cutting crowding note (Lou-Polk mechanism, generalized).** No literature exists (found in this
pass) applying comomentum-style excess-correlation crowding detection to value, quality or low-vol
baskets specifically. Proposed as a forward research *construct*, not an established finding: compute
the pairwise return-correlation-in-excess-of-characteristics inside each factor's top-decile basket,
by sleeve, as a factor-agnostic, real-time, price-only crowding early-warning signal, complementing the
factor's own valuation-spread-based timing signal from Arnott et al. This is Tier C until built and
tested — but it is fully constructible from free bhavcopy price data alone, which fits the "price-only
instrument" mandate directly.

---

## 4. Proposed parameters — moderate book factor set

| Name | Value/range | Source | Tier | Confidence | Decay assumption | What would change it |
|---|---|---|---|---|---|---|
| Core factor set (moderate book) | Value + Quality + Low-Vol + Size(quality-controlled, satellite) — no momentum as a core sleeve (momentum lives in its own workstream/book by turnover economics) | Fama-French 1992/2015; Novy-Marx 2013; QMJ 2019; Blitz-van Vliet 2007; AJV 2017 (India) | B (India-specific weighting), A (global existence of each factor) | Medium | 25–40% haircut per factor, see §3 | India-specific purged-CV factor-return estimates in the data phase; a clean India test of quality-controlled size |
| Value sleeve weight | 20–35% of factor-composite risk budget | Cohen-Polk-Vuolteenaho 2003 (spread-conditioning); FF 2015 (partial redundancy vs. quality) | B | Medium | 30–40% | Value-spread percentile (see next row); FF-2015-style redundancy check against the quality sleeve in India data |
| Value-spread conditioner | **Quantile rule, not a fixed threshold**: raise value-sleeve weight toward the top of its range when the factor's own trailing (10y-anchored) B/P-spread percentile is in its own top tercile; cut toward the bottom of the range in the bottom tercile | Cohen-Polk-Vuolteenaho 2003; Asness-Moskowitz-Pedersen 2013 (IC vs. valuation spread); Arnott-Beck-Kalesnik 2017 | B | Medium | Not separately haircut — a conditioning rule, not a premium claim | Purged/embargoed CV test of whether India's own value-spread percentile forecasts India value-factor forward returns (pre-register before running) |
| Quality sleeve weight | 20–35% of factor-composite risk budget, with a **floor, not a ceiling**, that binds tighter in the cycle-workstream's late-cycle/credit-stress regime states (crisis-ballast role) | QMJ 2019; 2008 crisis evidence (quality −38% vs mkt −56%); India pledge/RPT evidence | B | Medium | 25–35%, with an explicit valuation kill-switch (below) | Direct India test of QMJ-analogue drawdown behavior in India's own >20% Nifty-fall episodes (per the DD-constraint definition) |
| Quality valuation kill-switch | Cut quality-sleeve weight toward its floor when the quality basket's own relative-valuation percentile (vs. its 10y history) is in its top decile — mirrors the 2024–25 crowding episode | Arnott-Beck-Kalesnik-West 2016; 2025 "quant unwind" evidence | C (single recent episode) | Low-Medium | N/A — a switch, not a premium | A second live crowding-then-unwind episode, in the US or India, to confirm the pattern is not a one-off |
| Low-vol sleeve weight | 15–25% of factor-composite risk budget; explicitly **not** the alpha-tilted NIFTY-Alpha-Low-Vol-30 construct if the intended role is crisis ballast — prefer a pure realized-vol rank (price-only) over the alpha-blended index | Blitz-van Vliet 2007; Frazzini-Pedersen 2014 (BAB mechanism); India mixed evidence (§2, §3) | B | Medium | 30–40% | A resolved (not conflicting) India-specific low-vol study; AUM-growth trigger below |
| Low-vol crowding trigger | Reassess sleeve sizing if India smart-beta AUM in min-vol products grows materially faster than passive-equity AUM overall for 2+ consecutive years (rate-of-change trigger, not a level threshold) | Cafemutual/industry AUM series (2020–2025) | C | Low-Medium | N/A — a monitor, not a premium | Direct, cleaner AUM-by-factor data (current figures are industry-aggregated, not sleeve-attributed) |
| Size (quality-controlled) sleeve weight | 0–15%, satellite only, sized down from a "core" range because the India-specific construct is untested | Asness-Frazzini-Israel-Moskowitz-Pedersen 2018 (global); AJV 2017 (raw India SMB ≈0) | C (India-specific), A (global) | Low | Treat as fully unproven until tested; do not size as if Tier A | A direct pre-registered India test of quality-controlled SMB, purged/embargoed, before any weight above the satellite range |
| Price-only value sub-weight | Majority (>50%) of the value composite's weight from dividend yield + net-share-issuance/buyback + sales-to-price, with book/earnings yield as a minority, lag-buffered cross-check | Pontiff-Woodgate 2008 (NSI); CONTRACT Known Prior #7 (150–450bps restatement bias) | B | Medium | N/A — a construction rule | A completed price-only-vs-fundamental India backtest pair (mandatory per CONTRACT §8 traps) |
| Fundamental-signal reporting lag | Apply a conservative 4–6 month lag from fiscal period-end before any Indian fundamental (ROE, B/P, D/E, accruals) enters a live signal, aligned to the July–June AJV convention | AJV methodology note (July-June alignment to avoid look-ahead); RPT/Ind-AS restatement evidence | B | Medium | N/A — a construction rule | Confirmed India filing-deadline data (SEBI LODR timelines) in the data phase |
| Quality "junk" definition (India-tailored) | Standard QMJ profitability/growth/safety components, **plus** a promoter-pledge-intensity term and an RPT-disclosure-flag term, both price/filing-adjacent and largely restatement-free | QMJ 2019; India promoter-pledging papers (2023–2025); RPT literature | B (pledge/RPT terms), A (core QMJ components, globally) | Medium | 25–35% on the imported QMJ core; treat the India-specific terms as additive, unhaircut until tested | A direct test of whether the pledge/RPT terms add incremental explanatory power over standard QMJ in India |
| Momentum-vs-value conditioning variables | Tilt away from value / toward momentum when: (a) the value spread is in its bottom tercile, (b) credit spreads are widening + rates rising simultaneously (rate/credit regime overlap with value's typical outperformance window, per 2022 experience) | Asness-Moskowitz-Pedersen 2013 (value/momentum −0.50 correlation); 2022 rate-hike rotation evidence | B/C (the 2022 macro-regression figures are practitioner-sourced, not peer-reviewed — see §7) | Low-Medium | N/A — a conditioning rule | A pre-registered, purged-CV India test of credit-spread/term-spread/inflation-breakeven regressors against India's own value-minus-momentum spread |
| Turnover budget implication | Value/quality/low-vol sleeve turnover should track NSE strategy-index practice (semi-annual reconstitution, historically well inside 100% one-way/yr) — leaves ample headroom under the moderate book's 200% one-way cap for a momentum/tactical overlay owned elsewhere | NSE index methodology documents (semi-annual, May/Nov cutoffs); Israel-Moskowitz (momentum ≈5× value turnover) | B | Medium-High | N/A — a budgeting fact, not a premium | Actual India turnover measurement once point-in-time data exists |

---

## 5. Evidence-tier recommendations

- **Value (global existence):** Tier A. Hundreds of independent country-years across FF-1992-lineage
  studies; ≥30 observations comfortably met when pooled internationally. **Value (India-specific
  magnitude/decay):** Tier B — AJV's single-country series spans ~20 annual observations (1994–2014,
  now extended), below the 30-observation Tier-A bar on its own; pool with the global panel per the
  CONTRACT's JST-pooling instruction (§9) for any parameter that needs more than India alone can supply.
- **Quality/profitability (global):** Tier A — Novy-Marx (single large US panel, decades of monthly
  cross-sections) and QMJ's 24-country test both comfortably clear 30 independent observations.
  **Quality (India-specific, incl. pledge/RPT overlay):** Tier B at best — a handful of dedicated
  India studies (2020s vintage), n well under 30 country-years; the pledge/RPT overlay specifically is
  Tier C until a dedicated long-sample test exists.
- **Low-volatility (global):** Tier A (Blitz-van Vliet's multi-decade, multi-region replication; Ang et
  al.'s US decades of monthly cross-sections). **Low-volatility (India):** Tier B by the CONTRACT's own
  count rule using the live NIFTY Alpha Low-Vol 30 index (2017–2026, ~9 annual observations) — but the
  *academic* India evidence is genuinely conflicting (one study finds it, one does not), so treat the
  live-index Tier-B classification as an upper bound on confidence, not a settled Tier-A-in-waiting.
- **Size (raw, global and India):** Tier B-to-C. Even globally, the raw size premium is contested
  (weak, concentrated in microcaps, criticized on multiple fronts pre-2018); India's raw SMB is ≈0%
  over ~20 obs. **Size (quality-controlled, global):** Tier A (24-country test, 30 industries).
  **Size (quality-controlled, India):** Tier C — no direct test found; an unverified cross-country
  extrapolation (see §7).
- **BAB/low-beta (global):** Tier A (US + 20 international markets + multiple asset classes).
  **BAB (India):** Tier B — single dedicated paper (AJV-Vasudevan 2014), ~20 annual observations,
  finding largely subsumed by a quality/profitability control.
- **Accruals (Sloan, global):** Tier A (multi-decade US panel, widely replicated internationally in
  other markets). **Accruals (India):** not independently found in this search pass —
  `[VERIFY: no India-specific accrual-anomaly study located; treat as an untested cross-country prior,
  Tier B at best, until confirmed]`.
- **Piotroski F-Score (global):** Tier A/B border — the original 1976–1996 US sample is ~20 annual
  cross-sections (many independent stock-bets per year, so effectively far more than 20 independent
  observations in the cross-section, but only 20 non-overlapping years) — treat as Tier A for the
  screening logic, Tier B for the specific 23%/yr magnitude. **Piotroski (India):** Tier B — multiple
  applied studies exist but on shorter, more fragmented samples.

---

## 6. Research method for the data phase

1. **Point-in-time reconstruction is the precondition, not an afterthought.** Per CONTRACT Known Prior
   #7, every fundamental-based signal (quality's ROE/D/E, value's B/P/E/P) must be paired with a
   price-only counterpart before either is reported, and every fundamental input must carry a
   reporting-lag stamp (proposed default: 4–6 months post fiscal-period-end, per §4) rather than being
   available as-of the fiscal period-end itself. This alone is expected to explain a meaningful share of
   any India value/quality backtest's apparent edge and must be measured, not assumed away.
2. **Stambaugh-bias correction on the value spread.** Because the value-spread conditioner (§4) is a
   highly persistent (autocorrelated) predictor of a return series, apply the standard Stambaugh
   correction before trusting any in-sample "value spread predicts value returns" regression coefficient
   on India data — the effect in Cohen-Polk-Vuolteenaho is well-powered on US data but India's shorter
   sample makes this bias proportionally larger.
3. **Purged and embargoed cross-validation, embargo scaled to signal half-life.** Value/quality
   half-lives are long (per Israel-Moskowitz's turnover evidence, ~5× momentum's), so the embargo window
   around any purged-CV fold for value/quality signals should be materially longer than whatever
   embargo is used for momentum in the parallel workstream — a specific, numeric embargo choice (e.g.,
   in months) should be derived from the measured India autocorrelation half-life of each candidate
   signal, not copied from the momentum workstream's setting.
4. **Pre-register before testing, in this order:** (a) India-specific quality-controlled size effect
   (currently Tier C — the single most valuable test this phase could run, since it would upgrade or
   kill a full sleeve); (b) the value-spread-as-conditioner rule on India's own AJV-style HML series;
   (c) the promoter-pledge/RPT "junk" overlay's incremental power over standard QMJ components in
   India; (d) whether low-vol's India conflict (§2/§3) resolves once the AJV illiquid-name-exclusion
   methodology is applied consistently (the two conflicting papers used different universes — Nifty 500
   vs. S&P CNX 100 — which may itself explain the disagreement).
5. **Out-of-sample R² vs. historical mean, never in-sample.** Applies directly to the value-spread
   conditioner and to any quality-valuation kill-switch calibration — a rule that "explains" India's
   2020–22-style value comeback in-sample is worthless without an honest historical-mean benchmark.
6. **Deflated Sharpe with the true trial count.** Every item in the §4 provenance table that involves a
   choice (sub-signal weights inside value, the lag length, the embargo length, the AUM-growth trigger
   threshold) is a trial; the data phase must log all of them so the eventual deflated-Sharpe
   calculation for the moderate book's factor engine counts every sweep, not just the ones that "worked."
7. **Free-data sourcing plan, factor by factor:** price-only components (dividend declarations, shares
   outstanding/buybacks, realized volatility, 52-week-high proximity, beta) — NSE/BSE bhavcopy plus
   corporate-action filings, fully free and point-in-time by construction. Fundamental components (ROE,
   D/E, accruals, F-Score inputs) — company filings/exchange disclosures (free, but require the lag
   discipline above); promoter-pledge and SAST-threshold data — exchange/company disclosure filings
   (free, point-in-time by regulatory design). No paid vendor (CMIE Prowess, Capitaline, Bloomberg) is
   assumed available; where AJV's own published methodology relied on CMIE Prowess, the data phase must
   find or construct a free substitute (bhavcopy-derived price signals plus free filing-based
   fundamentals) and flag any gap explicitly rather than silently substituting a paid source.
8. **Tier-C discipline enforced mechanically.** The quality-valuation kill-switch and the quality-
   controlled-size sleeve are both Tier C per §5; per CONTRACT §4, they may only be used to *reduce*
   risk (cut a sleeve toward its floor / keep the satellite weight capped), never to add exposure, until
   they earn a tier upgrade through the pre-registered tests above.

---

## 7. Open questions and [VERIFY] items

- `[VERIFY]` The task brief's "Arnott-Beck-Kalesnik-Shakernia" attribution could not be confirmed;
  all retrievable sources show **Arnott, Beck, Kalesnik & West** as the authors of "How Can 'Smart
  Beta' Go Horribly Wrong?" (2016) and **Arnott, Beck & Kalesnik** as the authors of "Timing 'Smart
  Beta' Strategies?" (2017). Findings are used under this corrected attribution.
- `[VERIFY]` Whether India is among the 24 international markets tested in Asness-Frazzini-Israel-
  Moskowitz-Pedersen (2018) "Size Matters, If You Control Your Junk" — not confirmed from search
  snippets; this materially affects whether the quality-controlled size sleeve is Tier B (tested,
  cross-country) or Tier C (fully untested for India) as currently classified in §5.
- `[VERIFY]` No India-specific accrual-anomaly (Sloan-style) study was located in this search pass;
  the accruals signal is carried as an untested cross-country prior only.
- `[VERIFY]` The 2022 "term spread / credit spread / breakeven-inflation explain 27%/33.7%/45.3% of
  value-factor variability" figures came from a practitioner source (omegapoint.ai factor-spotlight
  content), not a peer-reviewed paper — treat as illustrative of the *direction* (rate/credit regime
  conditions value-vs-growth performance) rather than as a calibrated regression to import directly.
- `[VERIFY]` Exact base dates, launch dates and any pre-launch backtest-extension methodology for
  Nifty500 Low Volatility 50 and Nifty500 Quality 50 (both ~Dec-2024 launch) — niftyindices.com and
  bseindices.com are egress-blocked in this research environment (CONTRACT Known Prior #11); confirm
  directly on the principal's machine before relying on any of these two indices' quoted long-history
  returns.
- `[VERIFY]` The CONTRACT's own 150–450bps India fundamental-restatement-bias figure (Known Prior #7)
  is carried forward as given; this pass did not find an independent India-specific study quantifying
  restatement bias in basis-points terms — the qualitative evidence (Ind-AS transition restatement
  requirements, RPT-driven earnings management prevalence) is directionally supportive but not a
  direct re-derivation of the number itself.
- **Open question for the principal/next pass:** the low-volatility academic evidence for India is
  genuinely split (§2, §3) in a way that a single research pass cannot resolve without re-running the
  two conflicting studies' methodologies on a common, current, survivorship-corrected universe. This
  should be an explicit pre-registered task in the data phase, not resolved by picking whichever result
  is more convenient.
- **Open question:** whether the comomentum-style crowding-detection technique (Lou-Polk, §1/§3) can be
  meaningfully generalized to value/quality/low-vol baskets is untested anywhere in the literature
  found here — flagged as a genuine research construct for the data phase, not an established or even
  Tier-C finding yet.
- **Open question:** the quality sleeve's crisis-ballast role assumes India's own >20%-Nifty-fall
  episodes (per the DD-constraint's own definition, CONTRACT §3) show a quality-basket drawdown
  advantage analogous to 2008's US −38% vs. −56%; this has not been directly tested on India episodes
  and should be an early data-phase task given how directly it bears on the binding drawdown constraint.
