# Valuation Measures and Methods — the Full Toolkit

**Status: LITERATURE DOSSIER (2026-09-10), principal-directed. No web fetches this session —
written from training knowledge per instruction.** Complies with `research/CONTRACT.md` v0.1.
This is the TOOLKIT dossier: the ratio family, composite construction, structural adjustments and
model-based methods, at a level neither existing val-dossier addresses head-on. It does **not**
re-derive what two companion dossiers already own — `b-value-complementarity.md` (what combines
with value, and what does not) and `c-india-valuation.md` (India value evidence, measurement
distortions, five ranked designs on the incoming fundamentals handoff) — both cross-referenced,
not repeated. `research/dossiers/02-value-quality-lowvol.md` ("dossier 02") and
`research/cycles/value-deep/partA-C` remain the desk's deepest B/M-specific evidence base; this
dossier covers everything around and beyond B/M.

**Tags.** **[LIT]** = a published or practitioner claim; every one carries a confidence hedge in
the same sentence or the bracket itself — **[LIT, LOW CONFIDENCE]** where the direction is solid
but the magnitude is recalled loosely, and I do not invent false precision anywhere below.
**[BOOKED <entry>]** = a print actually read in `research/register/trial-ledger.md` or
`research/register/RUNSHEET.md` this session, quoted rather than re-derived. Per CONTRACT §4/§9,
every non-India citation below is a cross-country prior, Tier B at best for this program until a
purged-CV India test exists.

---

## 1. The ratio family, head to head

**P/B — the original, and its intangibles-era decay debate.** Fama & French's HML construction
(1992/1993) remains the reference value measure globally and in India [LIT, high confidence on
construction; dossiers 02/value-deep already anchor India's AJV HML at +15.3%/yr raw, 1994–2014,
against the desk's own real-data mirror at a materially lower +8.6%/yr — an unreconciled gap
flagged in dossier c]. Its measurement crisis is live: **Lev & Srivastava** (NYU Stern
working-paper line, "Explaining the Recent Failure of Value Investing," c. 2019) argue book value
increasingly misses capitalized R&D, brand and software investment, mislabeling asset-light
"growth" firms as expensive and structurally eroding the observed premium as the economy's capital
mix shifted toward intangibles [LIT, MEDIUM CONFIDENCE — the thesis and authorship I hold with
reasonable confidence; not the exact erosion figures]. **Arnott, Harvey, Kalesnik & Linnainmaa**
(2021, *Financial Analysts Journal* 77(1), "Reports of Value's Death May Be Greatly Exaggerated")
quantify it directly: classical HML fell **−55%** from 2007 through mid-2020, its worst drawdown
in 57 years, and an intangibles-capitalized book value resurrects a material share of that loss
[LIT, MEDIUM-HIGH CONFIDENCE on −55%; MEDIUM on the share recovered]. The counter-camp — **Israel,
Laursen & Richardson** (2020, AQR, "Is (Systematic) Value Investing Dead?") — run the identical
decomposition and find the value **spread widening to historic extremes** is the dominant driver,
downplaying intangibles' incremental weight [LIT, MEDIUM CONFIDENCE]. Both camps agree on the
proximate mechanism; they disagree only on how much a fuller book-value measure would have
avoided. Net for this desk: P/B is not dead, but is the multiple most exposed to accounting-regime
and intangible-intensity drift, and belongs in a composite as a minority, lag-buffered leg — the
construction choice dossiers 02/c already made and this dossier does not revisit.

**P/E and its cyclical adjustment (CAPE).** Trailing or forward P/E is the most quoted multiple
and the cleanest to compute wherever quarterly EPS exists; Shiller's cyclically-adjusted P/E
(Campbell & Shiller 1988, *J. Finance*, "Stock Prices, Earnings, and Expected Dividends") smooths
a decade of real earnings to damp margin-cycle noise before dividing into price [LIT, high
confidence — a standard, widely-verified citation]. At the index level, CAPE and its close cousin
dp (dividend-price) are the desk's own already-tested instrument via the ER arc, which used dp
directly rather than reconstructing true CAPE (the raw Shiller `ie_data` pull is still an owed,
blocked RUNSHEET row). Section 5 is entirely about what that testing found; here the scope is
construction only — P/E's chief weakness is denominator noise (one lumpy quarter swings the ratio
sharply), exactly what CAPE exists to damp.

**EV/EBITDA — the practitioner favorite.** **Loughran & Wellman** (2011, *Journal of Financial
and Quantitative Analysis*, "New Evidence on the Relation between the Enterprise Multiple and
Average Stock Returns") show the enterprise multiple predicts US cross-sectional returns robustly
across size and book-to-market groups, with the low-multiple decile outperforming the high by an
economically large annual spread [LIT, LOW-MEDIUM CONFIDENCE on the exact spread; direction and
cross-subgroup robustness held with more confidence than any number]. Their claim is that the
enterprise multiple carries information beyond a re-parameterization of B/M or E/P, chiefly
because it is capital-structure-neutral where E/P is not — a highly levered cheap-P/E stock can be
an expensive-EV/EBITDA stock. Also the multiple most exposed to India's data-cadence staircase (§6).

**FCF yield — the recent-decade winner claim.** Practitioner sources (O'Shaughnessy/"What Works on
Wall Street," several factor-house year-in-reviews) report FCF-yield screens outperforming
book-value screens through roughly the same 2007–2020 window B/M struggled in [LIT, LOW
CONFIDENCE — a repeated asset-manager claim, no single peer-reviewed magnitude attached]. The
academic base is thinner than B/M's: FCF yield is a hybrid of E/P and CF/P — cash-based, so it
sidesteps some of the accrual-quality problem Sloan (1996) identifies (already booked in
`docs/fundamentals/02`) — rather than an independently validated factor, and "FCF" is not a
standardized line item; a screen's own capex/working-capital conventions can move the ranking
meaningfully, the researcher-degrees-of-freedom risk §2 flags.

**Dividend yield — and its payout-state confound.** This desk has booked the mechanism directly.
**QG-D1** (`research/register/trial-ledger.md`, 2026-09-08) re-ran Arnott & Asness (2003, *FAJ*)
on Shiller's 1871–2023 series and found the celebrated "high payout → higher subsequent growth"
result replicates on the surface (+4.01%/yr next-decade real-earnings growth in high-payout
months vs. +1.82%/yr low-payout) — but its own mechanism cell shows high-payout months are
**depressed-earnings months 78% of the time** (dividends are smoothed ~2.7x relative to earnings,
so payout spikes mechanically when earnings collapse), and the gap **inverts to −1.85pp** within
non-depressed months [BOOKED QG-D1]. Aggregate payout is a repackaged earnings-STATE variable, not
an independent valuation or quality signal — the mechanism every dividend-yield-as-value claim
must clear: a high yield can mean cheap, or it can mean earnings just fell, and a level-only yield
reading cannot tell the two apart without an explicit payout-ratio or earnings-trend conditioner.

**Sales-based multiples.** Price/sales is the "never negative, never manipulated by one-off items"
multiple; O'Shaughnessy's long-sample work is often cited ranking P/S among the single strongest
individual value predictors historically [LIT, LOW-MEDIUM CONFIDENCE on the exact ranking]. Its
virtue is data cleanliness — revenue is essentially never restated the way earnings, book value or
cash flow can be — and, per the desk's own India data-engineering read (`research/cycles/value-
deep/partC-data.md`), sales/price is one of only two multiples (with E/P) that refresh cleanly
every quarter in India with no staleness compromise, which is why it already sits inside the
desk's existing value composite. Its weakness is the mirror image: it says nothing about margin or
capital intensity, so a P/S screen alone conflates a thin-margin commodity name with a high-margin
compounder at the same multiple — never proposed standalone in the literature, only as a composite
leg.

**Shareholder yield (dividends + buybacks).** **Boudoukh, Michaely, Richardson & Roberts** (2007,
*J. Finance* 62(2), "On the Importance of Measuring Payout Yield") argue for total payout yield —
dividends plus net buybacks minus issuance — over dividend yield alone: since the 1980s buybacks
have substituted for dividends as the dominant US payout channel, so a dividend-yield-only measure
increasingly misses the return of capital and is bettered as a predictor by the total-payout
construction [LIT, MEDIUM CONFIDENCE on direction and mechanism; LOWER on the exact predictive-
regression magnitude]. This is consistent with the desk's own existing design choice (dossier 02,
already read): the value composite weights net-share-issuance/buyback ahead of book yield
precisely because it is price-only-adjacent and restatement-immune (Pontiff & Woodgate 2008 is the
desk's own anchor for net-share-issuance, already cited in dossier b §5). India's specific catch:
buybacks are a much younger, thinner instrument than dividends here, and the dividend-vs-buyback
tax arbitrage has swung repeatedly since 2016 — a total-payout construction imported wholesale
from US evidence needs its own India base-rate check before sizing, not an assumed transfer.

---

## 2. Composites vs. single measures

The stronger evidence, and the practitioner consensus, favors composites. O'Shaughnessy-style
multi-factor composites (rank-averaging B/P, E/P, EV/EBITDA, FCF/P, sales/P and shareholder yield)
are marketed on the claim that combining measures dilutes the risk of any single accounting break
or one-off item distorting the rank [LIT, LOW-MEDIUM CONFIDENCE — an asset-manager claim, not an
independently replicated magnitude]. AQR's applied work is more academically anchored and more
circumspect: Asness & Frazzini's "Devil in HML's Details" (already in dossier b's reference base)
shows that even *within* one measure, using a current- vs. lagged-price denominator changes the
signal's behavior materially — current-price B/M behaves more like a momentum-tilted signal,
lagged-price B/M more like a pure distress-risk signal — an argument for blending measurement
CONVENTIONS, not only different ratios.

**Rank-averaging vs. intersection.** Averaging percentile ranks across measures is the standard,
more outlier-robust construction; an intersection approach (cheap on every measure simultaneously)
concentrates the portfolio into a small, often illiquid tail and typically produces noisier,
higher-turnover selections without a correspondingly larger measured premium in the practitioner
literature [LIT, LOW CONFIDENCE — a common practitioner finding, no magnitude attached]. The
desk's own convention — majority weight on price-only/cash multiples, minority on lag-buffered
book multiples, a rank-average (dossier 02, already read) — is a composite of exactly this kind.

**The overfitting risk of metric-picking after the fact.** This is the sharper discipline point.
A composite assembled AFTER observing which individual metrics "worked" in-sample is the textbook
researcher-degrees-of-freedom problem the CONTRACT's governing principle already prices: McLean &
Pontiff (2016) find published anomalies decay ~26% out-of-sample and ~58% post-publication [LIT,
the CONTRACT's own governing citation, high confidence]; Hou, Xue & Zhang's (2020) replication of
~450 anomalies finds roughly two-thirds fail careful out-of-sample replication [LIT, MEDIUM
CONFIDENCE — already booked via `docs/fundamentals/02`]. A "value composite" built by backtesting
five candidate metrics and keeping the three with the best in-sample Sharpe is not a composite in
the sense the literature validates — it is five trials wearing one costume, and under CONTRACT
§9's deflated-Sharpe standard every metric considered and discarded is a counted trial, not a free
look. The defensible order is the opposite: fix the metric list and weighting scheme from ex-ante
economic reasoning (which statements are cleanest, least restated, least capital-structure-
confounded for THIS market) before any return is computed — CONTRACT §1's pre-registration
discipline applied to composite design specifically, not only to individual signals.

---

## 3. Structural adjustments

**Sector/industry neutralization.** **Asness, Porter & Stevens** ("Predicting Stock Returns Using
Industry-Relative Firm Characteristics," circulated from 1994) test ranking value (and other)
characteristics WITHIN industry rather than across the whole universe; the finding most often
cited is that industry-relative ranks perform comparably to raw cross-sectional ranks for return
prediction while measurably reducing the sector-concentration and implicit sector-timing risk a
raw universe-wide sort carries (a raw sort inevitably overweights whichever sectors are cyclically
cheap at a point in time) [LIT, MEDIUM CONFIDENCE on the qualitative finding, LOW on any specific
magnitude — not independently verified against the paper's own tables this session]. For this
desk, sector-neutral value is a risk-reduction tool, not a return-enhancement one: CONTRACT §3
explicitly leaves sector exposure fully active for the portfolio as a whole (no neutrality
requirement), but that is a separate question from whether the underlying value SIGNAL should be
computed industry-relative before the optimizer sees it — a raw rank conflates "this stock is
cheap" with "this stock's sector is cheap," and only the industry-relative construction isolates
the former. Dossier c's §4 already reaches this same construction consequence independently for
India's sector-mix-contaminated index series; this section supplies the literature anchor it did
not cite.

**Intangibles-adjusted book value — does it resurrect P/B?** **Peters & Taylor** (2017, *JFE*
123(2), "Intangible Capital and the Investment-q Relation") build a "Total Q" adding capitalized
R&D/SG&A-derived intangible capital to physical capital and find it materially improves the
investment-q relation over a physical-capital-only construction [LIT, MEDIUM CONFIDENCE on the
qualitative finding, LOW on exact magnitude]. **Eisfeldt & Papanikolaou** (2013, *J. Finance*,
"Organization Capital and the Cross-Section of Expected Returns") capitalize SG&A into
"organization capital" and find firms with high organization-capital intensity relative to
physical capital earn a return premium, framed as compensation for a labor-mobility risk specific
to knowledge-intensive firms [LIT, MEDIUM CONFIDENCE]. Whether this resurrects P/B as a factor is
exactly §1's unresolved Arnott-vs.-Israel-Laursen-Richardson debate: partially, with the share
attributable to intangibles specifically (rather than to ordinary valuation-spread mean reversion)
still contested by researchers who agree on every other fact. This desk's existing decision
(value-deep dossier, already read) is not to build a separate intangibles-adjusted-HML sub-signal
as a first-order sleeve component until India's own intangible-intensity profile is checked — an
open, testable, currently unresolved question this dossier does not settle by assertion.

**Accounting-regime effects.** Any book-value-, ROE- or leverage-based measure crosses at least
one hard accounting-regime seam in every major market: US-GAAP-vs-IFRS goodwill and R&D-expensing
conventions differ enough that a raw cross-country B/M or ROE comparison needs an adjustment layer,
and — the India instance the desk has already booked (`docs/fundamentals/02`) — Ind-AS 116's ~2019
lease-capitalization mandate pulls previously off-balance-sheet operating leases onto the balance
sheet, inflating both assets and liabilities and breaking pre/post-2019 comparability for any
lease-heavy Indian sector (retail, aviation, hospitality) absent an explicit seam flag. Dossier c's
§2(b) already documents the fuller Ind-AS phase-in timeline for India specifically; not repeated
here.

---

## 4. Model-based methods — evidence beyond ratios, or narrative?

**Residual income / Ohlson.** The Ohlson (1995, *Contemporary Accounting Research*, "Earnings,
Book Values, and Dividends in Equity Valuation") model expresses intrinsic value as current book
value plus the present value of expected FUTURE abnormal earnings (ROE in excess of cost of
equity) — mechanically, RIM is book value plus a forecasted-ROE-trajectory adjustment, not an
economic input independent of what B/P and forward-ROE forecasts already contain. **Frankel &
Lee** (1998, *J. Accounting and Economics*, "Accounting Valuation, Market Expectation, and
Cross-Sectional Stock Returns") build a V/P ratio from an RIM-based intrinsic-value estimate and
find it predicts cross-sectional returns, with some non-US corroboration [LIT, MEDIUM CONFIDENCE
on the qualitative finding; LOWER on exact spread magnitude and country coverage]. The honest
verdict: RIM-based value restates the same underlying information (book value, earnings quality,
growth expectations) through a discounted-cash-flow lens — it is evidence for that information's
value, not for RIM as an independent economic force — and it is data-hungry (analyst-forecast
inputs feed the abnormal-earnings path), a condition that plausibly fails below roughly the top
200–300 Indian names by analyst coverage, capping RIM's addressable universe well short of the
NIFTY 750 the moderate/aggressive books need.

**Reverse-DCF / market-implied expectations (Mauboussin).** Mauboussin & Rappaport's "Expectations
Investing" inverts the standard DCF: instead of forecasting cash flows and discounting to a price,
it backs out the growth/margin/ROIC path the CURRENT price already implies, then asks whether that
implied path is more or less demanding than an independent view. This is explicitly a FRAME, not a
factor — there is no published, replicated return-predictability literature for "buy stocks where
implied expectations look too low" as a standalone systematic signal; the entire value of the
exercise sits in the judgment applied to the implied-vs.-independent gap, which is a Stage 2
(human/AI forward-view) tool under this program's own architecture (CONTRACT §2), not a Stage 1
systematic input. It earns its place as a NARRATIVE check on a mechanical screen's output — e.g.
confirming a stock flagged "cheap" is not implicitly pricing a growth collapse the desk's forward
view disagrees with — not as an independently-sized signal.

**Tobin's q.** Classical Tobin's q (market value of assets over replacement cost) is, in its
simplest form, functionally an inverse valuation ratio close to inverse book-to-assets. The
Hou-Xue-Zhang "q5" family repurposes it differently: not as the return-predicting characteristic
itself, but as one of three inputs (with cash-flow/assets and 4-quarter ROE change) FORECASTING
future investment growth via Fama-MacBeth regression, with the forecast itself — not q directly —
becoming the traded characteristic ("R_EG," expected growth). The desk has directly engaged this
construction. **QG-D5** (`research/register/trial-ledger.md`, 2026-09-08) regresses the US R_EG
factor on FF6 and finds the alpha is NOT spanned (+8.34%/yr, t=10.9, R² 0.46) — flagged, not
celebrated, in the register's own words, because the vaulted sample ends exactly at the paper's
own publication date, so every month of the alpha was available to the model's authors when the
forecasting weights were fit, and a t=10.9/Sharpe-1.49/max-drawdown-−12% factor over 52 years would
be the best documented strategy in the literature if genuine [BOOKED QG-D5]. **QG-D6** (same file,
registered 2026-09-08, still UNRUN pending the India fundamentals handoff) freezes the identical
recipe for a NIFTY 500 replication — log Tobin's q, CFO/assets and 4-quarter ROE change forecasting
one-year investment growth on an expanding, purged Fama-MacBeth window, decile-sorted — with the
registration's own stated prior that a positive India OOS print would be the first genuinely
post-publication test available to this desk and would soften the US specification-search flag,
while a null print would confirm it; the register frames a Sharpe above 1 in India as grounds for
"ER-D4b-grade suspicion," not celebration [BOOKED QG-D6]. This is dossier c's design #4, quoted
verbatim there; cited here only as the model-based method most directly under this desk's own
test — a genuinely open, pre-registered, not-yet-adjudicated question either way.

**Sum-of-parts.** No academic return-predictability literature comparable to B/M, EV/EBITDA or
gross profitability exists for sum-of-parts valuation — it is a broker/practitioner technique for
diversified conglomerates and holding companies (value each segment on its own peer multiple, sum,
compare to the consolidated market price), and its evidence base is case-based and narrative, not
factor-tested. It is directly relevant to India's ownership structure (§6): promoter-group holding
companies and cross-held conglomerate structures are exactly the setting sum-of-parts targets, and
the "holding company discount" it addresses is a real, widely observed, but Tier-C (narrative,
fewer than four documented systematic tests) input pending a dedicated India build.

---

## 5. Valuation at the INDEX level vs. the CROSS-SECTION

The same word, "valuation," names two statistically different objects, and conflating them is the
single most consequential error a systematic desk can make. At the INDEX level, a valuation ratio
(dp, P/E, CAPE) is one highly autocorrelated time series — the aggregate number persists for years
because the market's overall cheapness or richness does not reset every month. At the
CROSS-SECTION, a valuation spread is a rank comparison across hundreds of simultaneously-priced
stocks, refreshed with genuinely new relative-price information every period, even when the
AGGREGATE level of that same ratio barely moves.

This desk has already run the index-level test to its conclusion, and the result is
null-consistent, not merely inconclusive. **ER-D1c** (`research/register/trial-ledger.md`,
2026-09-05) is the direct mechanism demonstration: fitting an AR(1) to each JST-panel country's dp
series and simulating a null world with genuinely ZERO predictability, then asking whether the
OBSERVED dp→forward-return correlation ladder sits inside or outside that null's 95% band, finds
the ladder **INSIDE** the null band at 1, 3, 5 and 10 years (median AR(1) phi 0.71 across 15
countries); only the 20-year horizon (+0.36 observed vs. a [−0.19, +0.32] null band) beats the
null [BOOKED ER-D1c]. In plain terms: the familiar "rising staircase" of dp's apparent forecast
power through 10 years — the same shape every index-level valuation-timing chart shows — is
exactly what persistence plus overlapping-window regression manufactures under a null of NO true
predictability at all (Stambaugh 1999's persistent-regressor bias [LIT, high confidence, the
canonical citation]; the desk's own design additionally invokes a "BRW (2008)"-type
overlapping-horizon null test [desk citation, per the ER-D1c register entry itself — I have not
independently re-verified the authors' initials beyond the desk's own text]). **ER-D4b** (same
file, 2026-09-05), running the honest purged, train-only-fitted-bounds correction CONTRACT §9's
estimation standards require, confirms this from a different angle: the pooled 10-year "OOS R² > 0"
read that looked like a genuine forecast survives neither benchmark cleanly, and its 90% bootstrap
band on that R² includes zero — the registered correction fires, and "Goyal-Welch wins at both
horizons" is the honest read [BOOKED ER-D4b]. **ER-D7** (2026-09-05) is the constructive residue: a
real-time, non-lookahead corner spread of +5.1pp/yr (cheap+low-inflation vs. expensive+
high-inflation states) PASSES its own bar, but the same entry's point-forecast cells FAIL (−29.8%/
−27.2% OOS R² at 5/10y) [BOOKED ER-D7] — so index-level valuation survives ONLY as an
expectations/state qualifier (is the market cheap-and-calm or expensive-and-hot), never as a
return forecaster with a quantified point estimate.

The cross-section is a genuinely different mechanism, and the desk's own **SC-D1** print
(2026-09-10) is directly on point even though it targets small-vs-large rather than value-vs-growth
directly: a Pb-based valuation SPREAD across size terciles orders next-12-month relative returns
monotonically (T1 cheap-small +28.78%/yr vs. T3 +12.73%/yr, a +16.05pp spread, in-sample/
first-gate, US data), with the spread-return correlation RISING with horizon (−0.26/−0.50/−0.69 at
1/12/36 months) [BOOKED SC-D1] — the opposite signature from the index-level ladder's collapse
under the null. The mechanism divergence is not a coincidence: a cross-sectional value spread does
not require forecasting where the WHOLE market's single persistent series is going — it only
requires that the GAP between two contemporaneously-priced stocks closes, a trade arbitrage
capital can execute stock-by-stock without any aggregate-market view, and it is measured across
many simultaneous names (breadth substitutes for the time series' scarcity of independent
observations, the very problem underlying Stambaugh bias). This is precisely Cohen, Polk &
Vuolteenaho's (2003, *J. Finance*, "The Value Spread") construction, already anchored in dossier
b's §6: the value spread predicts the value FACTOR's own subsequent return — a cross-sectional
object re-embedded in time — not the aggregate market's forward return regressed on the aggregate
market's own valuation. The desk's existing value evidence base (Fama-French 1992/1993/1998,
Asness-Moskowitz-Pedersen 2013, the India AJV HML replication, all in dossiers b/02/value-deep)
sits entirely on this cross-sectional side and is correspondingly the stronger, Tier-A-grade
evidence; the index-level side is now formally demoted by three independent, purged designs. The
design consequence: valuation belongs in the cross-sectional stock-selection engine (Stage 1's
factor book) as a live signal, and belongs in the cycle/regime layer only as a STATE qualifier
that sizes exposure — never as a market-timing forecast with its own claimed point estimate.

---

## 6. India specifics

Dossier c already owns the full India measurement-distortion and design-build treatment (its §2
distortions a–e: the 2021 splice, Ind-AS transition, promoter cross-holdings, banks' P/B, PSU
discount persistence; its §3 trap-marker ranking) and is not repeated here. Two points this
dossier adds that dossier c's design-focused treatment does not:

**The consolidated/standalone splice, restated for the toolkit.** NSE switched its published
index-level P/E from standalone to consolidated earnings in **2021-03** [RUNSHEET row,
`ingest/vault/index_valuation/`, added 2026-09-10 off SC-D1's India ask — "a splice break that
must be authenticated, not smoothed," quoted from the row itself], a genuine level break in the
one continuously-published Indian valuation series, and the identical basis choice recurs at the
firm level in the incoming fundamentals handoff's own `statement_basis` field (per
`research/register/handoff-prompt-india-fundamentals.md`). Every multiple in §1 that touches book
value, earnings or leverage inherits this seam; only sales/price (revenue-based) and pure price-
based measures (dividend yield, buyback yield) are immune to it by construction.

**The practical measure ranking for Indian data quality — by refresh cadence, not by literature
pedigree.** Per the desk's own India data-engineering read (`research/cycles/value-deep/
partC-data.md`, already read for this dossier): **E/P and sales/price** refresh cleanly every
quarter (PAT and revenue are both quarterly-native P&L items with no balance-sheet dependency) —
the cleanest pair for an India-first construction. **Dividend yield** is next: event-based
(declaration) plus quarterly (interim), the single least restatement-exposed input, subject to
§1's payout-state confound. **B/P** is a HALF-YEARLY STAIRCASE, not a smooth quarterly series,
because the Indian balance sheet is disclosed only twice a year (September H1-end, March FY-end):
Asness & Frazzini's stale-book warning is not an optional convention choice in India the way it can
be in the US — it is forced by the disclosure calendar itself. **CF/P** inherits the identical
half-yearly-only staleness. **EV/EBITDA is the worst-behaved multiple by this metric specifically**
because it mixes cadences within one ratio — quarterly EBITDA against semi-annual net debt — a
genuine construction hazard distinct from, and additional to, its Loughran-Wellman academic case
in §1. Financials (banks, NBFCs, insurers) must be excluded from any universe-wide raw multiple
pool entirely, each reporting under its own statutory format; P/E and P/B for these names are
usable only ranked WITHIN financials, never pooled with non-financial ranks on a common percentile
— dossier c's §2(d) develops the banks-specific NPA-adjustment problem this creates.

---

## Edge candidates for this desk

1. **Profitable-value composite, majority price-only (E/P + sales/P + buyback/NSI), minority
   lag-buffered B/P, computed within-industry.** *Mechanism*: cheap and high-quality are close to
   orthogonal characteristics (Novy-Marx, dossier b §2); industry-relative ranking (§3, Asness-
   Porter-Stevens) isolates stock-specific cheapness from sector-cyclical cheapness. *Magnitude*:
   comparable-to-value-alone premium in global tests [LIT, MEDIUM CONFIDENCE]; India magnitude
   untested and bounded by the AJV-vs.-desk-mirror discrepancy already flagged in dossier c.
   *Data needed*: quarterly PAT/revenue, semi-annual book value/CFO (staircase), delisted registry,
   a sector-classification tag (a genuine gap dossier c's §6 already names).
2. **Total shareholder yield (dividend + buyback − issuance) as a price-only India value input.**
   *Mechanism*: Boudoukh et al.'s total-payout argument (§1); India-specific: shares outstanding is
   quarterly-native and essentially restatement-immune, unlike book value. *Magnitude*: [LIT, LOW
   CONFIDENCE on India transfer — US evidence only, no India replication read]. *Data needed*:
   quarterly shares-outstanding history plus dividend declarations — no balance-sheet dependency,
   among the cheapest signals to build.
3. **Value-spread-as-conditioner (Cohen-Polk-Vuolteenaho), sizing not timing.** *Mechanism*: §5's
   cross-sectional spread predicts the value FACTOR's own forward return; widen the value/momentum
   allocation when the spread sits in its own cheap tercile, tilt toward momentum when it is tight
   — explicitly not an index-level timing rule. *Magnitude*: no single clean number; directionally
   supported by the desk's already-read value-deep case studies. *Data needed*: the same
   fundamentals panel as #1, computed live at every rebalance.
4. **India small-vs-large valuation-spread size-rotation signal.** *Mechanism*: SC-D1's US first
   gate passed in-sample (§5); the India version is a registered runsheet ask once the NSE
   index-P/E-P/B pull lands with the 2021 splice authenticated (§6). *Magnitude*: US in-sample
   only so far — no India number exists yet; Tier-C/monitor per the desk's own SC-D3 doctrine on
   Indian size-rotation consumption caps. *Data needed*: the NSE index P/E-P/B-yield RUNSHEET row.
5. **Explicit non-edges, stated to prevent re-litigation** (CONTRACT bars are never moved):
   index-level valuation (dp/CAPE) as a MARKET-TIMING forecast is REJECTED at this desk —
   ER-D1c/ER-D4b/ER-D7 (all BOOKED, §5) show it is null-consistent through 10 years and survives
   only as a coarse expectations qualifier; reverse-DCF/expectations-investing and RIM are Stage-2
   narrative frames only, with no independent return-predictability evidence distinct from
   ratio-repackaging; aggregate dividend-payout timing (QG-D1, BOOKED, §1) is a repackaged
   earnings-state variable, not a signal.

---

## Data requirements — India

1. **As-filed quarterly fundamentals with an explicit `statement_basis` field** (the incoming
   handoff's P1) — unlocks E/P and sales/P at quarterly cadence and the staircase builds for B/P,
   CF/P and EV/EBITDA; the field is what lets a basis-switch be treated as a structural break
   rather than noise (§6).
2. **NSE index P/E, P/B and dividend-yield daily history since ~1999, with the 2021-03
   standalone-to-consolidated splice authenticated as two regimes** — the already-registered
   RUNSHEET row (`ingest/vault/index_valuation/`), needed both for edge candidate #4 and as a
   continuously-checkable validation bench for any constructed fundamentals panel's aggregate level.
3. **A sector/industry classification per company** — neither the fundamentals handoff nor any
   existing pull carries a GICS-like tag; without one, edge candidate #1's within-industry
   construction (§3, §6) cannot be built. Dossier c's §6 already flags this as an ask worth
   appending to the NSE sectoral-TR RUNSHEET row rather than a new pull.
4. **Free-float shares outstanding, separate from total shares outstanding** — needed to compute
   free-float-adjusted P/B and market cap distinct from raw, given India's structurally high
   (~45–50% median) promoter blocks and the cross-holding distortion dossier c's §2(c) documents;
   not currently specified as its own field in the fundamentals handoff.
5. **SEBI shareholding-pattern and promoter-pledge history** — already a handoff deliverable (P5),
   genuinely point-in-time by regulatory construction; needed for both the free-float adjustment
   above and the pledge-acceleration trap screen dossier c's §3/§5 already designs in full.
6. **Damodaran India/EM industry vintages** (an existing RUNSHEET row) — the free source for
   sector-relative multiple benchmarks feeding the industry-neutral construction in edge candidate
   #1, until a native NSE sector classification lands.
