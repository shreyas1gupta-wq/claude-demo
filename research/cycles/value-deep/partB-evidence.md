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
