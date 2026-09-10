# Valuation Measures and Methods — the Full Toolkit

**Status: LITERATURE DOSSIER (2026-09-10), principal-directed. No web fetches this session —
written from training knowledge per instruction.** Complies with `research/CONTRACT.md` v0.1.
This is the TOOLKIT dossier: the ratio family, composite construction, structural adjustments and
model-based methods — ground neither existing val-dossier covers. It does **not** re-derive what
two companion dossiers own — `b-value-complementarity.md` (what combines with value, and what does
not) and `c-india-valuation.md` (India value evidence, measurement distortions, five ranked designs
on the incoming fundamentals handoff) — both cross-referenced, not repeated. `research/dossiers/
02-value-quality-lowvol.md` ("dossier 02") and `research/cycles/value-deep/partA-C` remain the
desk's deepest B/M-specific base; this dossier covers everything around and beyond B/M.

**Tags.** **[LIT]** = a published/practitioner claim, hedged in the same sentence or bracket — no
false precision invented anywhere below. **[BOOKED <entry>]** = a print actually read in
`research/register/trial-ledger.md` or `RUNSHEET.md` this session, quoted not re-derived. Per
CONTRACT §4/§9, every non-India citation is a cross-country prior, Tier B at best until purged-CV
India tests exist.

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

**P/E and its cyclical adjustment (CAPE).** Trailing or forward P/E is the most quoted multiple and
the cleanest to compute wherever quarterly EPS exists; Shiller's cyclically-adjusted P/E (Campbell
& Shiller 1988, *J. Finance*, "Stock Prices, Earnings, and Expected Dividends") smooths a decade of
real earnings to damp margin-cycle noise before dividing into price [LIT, high confidence]. At the
index level, CAPE and its cousin dp (dividend-price) are the desk's own already-tested instrument
via the ER arc, which used dp directly rather than reconstructing true CAPE (the raw Shiller
`ie_data` pull is still an owed, blocked RUNSHEET row) — §5 covers what that testing found. Here
the scope is construction only: P/E's chief weakness is denominator noise (one lumpy quarter swings
the ratio sharply), exactly what CAPE exists to damp.

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
Wall Street," factor-house year-in-reviews) report FCF-yield screens outperforming book-value
screens through roughly the same 2007–2020 window B/M struggled in [LIT, LOW CONFIDENCE — a
repeated asset-manager claim, no peer-reviewed magnitude attached]. The academic base is thinner
than B/M's: FCF yield is a hybrid of E/P and CF/P — cash-based, sidestepping some of Sloan's (1996)
accrual-quality problem (booked in `docs/fundamentals/02`) — rather than an independently
validated factor, and "FCF" is not a standardized line item; a screen's own capex/working-capital
conventions can move the ranking meaningfully, the researcher-degrees-of-freedom risk §2 flags.

**Dividend yield — and its payout-state confound.** This desk has booked the mechanism directly.
**QG-D1** (`research/register/trial-ledger.md`, 2026-09-08) re-ran Arnott & Asness (2003, *FAJ*)
on Shiller's 1871–2023 series and found "high payout → higher subsequent growth" replicates on the
surface (+4.01%/yr next-decade real-earnings growth, high-payout months, vs. +1.82%/yr low-payout)
— but its own mechanism cell shows high-payout months are **depressed-earnings months 78% of the
time** (dividends run ~2.7x smoother than earnings, so payout spikes mechanically when earnings
collapse), and the gap **inverts to −1.85pp** within non-depressed months [BOOKED QG-D1]. Aggregate
payout is a repackaged earnings-STATE variable, not an independent signal: a high yield can mean
cheap, or it can mean earnings just fell, and a level-only reading cannot tell the two apart
without an explicit payout-ratio or earnings-trend conditioner.

**Sales-based multiples.** Price/sales is the "never negative, never manipulated by one-off items"
multiple; O'Shaughnessy's long-sample work is often cited ranking P/S among the single strongest
individual value predictors historically [LIT, LOW-MEDIUM CONFIDENCE on the exact ranking]. Its
virtue is data cleanliness — revenue is essentially never restated the way earnings, book value or
cash flow can be — and, per the desk's India data-engineering read (`research/cycles/value-deep/
partC-data.md`), sales/price is one of only two multiples (with E/P) refreshing cleanly every
quarter in India with no staleness compromise, why it already sits in the desk's value composite.
Its weakness is the mirror image: it says nothing about margin or capital intensity, so a P/S
screen alone conflates a thin-margin commodity name with a high-margin compounder at the same
multiple — never proposed standalone, only as a composite leg.

**Shareholder yield (dividends + buybacks).** **Boudoukh, Michaely, Richardson & Roberts** (2007,
*J. Finance* 62(2), "On the Importance of Measuring Payout Yield") argue for total payout yield —
dividends plus net buybacks minus issuance — over dividend yield alone: since the 1980s buybacks
have substituted for dividends as the dominant US payout channel, so dividend yield alone
increasingly misses the return of capital and is bettered by the total-payout construction [LIT,
MEDIUM CONFIDENCE on direction/mechanism; LOWER on the exact predictive-regression magnitude].
Consistent with the desk's existing design (dossier 02): the value composite weights net-share-
issuance/buyback ahead of book yield because it is price-only-adjacent and restatement-immune
(Pontiff & Woodgate 2008 is the desk's own NSI anchor, cited in dossier b §5). India's catch:
buybacks are a much younger, thinner instrument than dividends, and the dividend-vs-buyback tax
arbitrage has swung repeatedly since 2016 — a total-payout construction imported wholesale from
US evidence needs its own India base-rate check before sizing.

---

## 2. Composites vs. single measures

The stronger evidence, and the practitioner consensus, favors composites. O'Shaughnessy-style
multi-factor composites (rank-averaging B/P, E/P, EV/EBITDA, FCF/P, sales/P, shareholder yield)
are marketed on the claim that combining measures dilutes the risk of any single accounting break
distorting the rank [LIT, LOW-MEDIUM CONFIDENCE — an asset-manager claim, no replicated
magnitude]. AQR's applied work is more circumspect: Asness & Frazzini's "Devil in HML's Details"
(dossier b's reference base) shows even *within* one measure, a current- vs. lagged-price
denominator changes the signal materially — current-price B/M behaves more like a momentum-tilted
signal, lagged-price B/M like a pure distress-risk signal — an argument for blending measurement
CONVENTIONS, not only different ratios.

**Rank-averaging vs. intersection.** Averaging percentile ranks across measures is the standard,
outlier-robust construction; an intersection approach (cheap on every measure simultaneously)
concentrates the portfolio into a small, often illiquid tail and typically produces noisier,
higher-turnover selections without a correspondingly larger measured premium in the practitioner
literature [LIT, LOW CONFIDENCE, no magnitude attached]. The desk's own convention — majority
weight on price-only/cash multiples, minority on lag-buffered book multiples, rank-averaged
(dossier 02) — is a composite of exactly this kind.

**The overfitting risk of metric-picking after the fact.** A composite assembled AFTER observing
which metrics "worked" in-sample is the textbook researcher-degrees-of-freedom problem the
CONTRACT's governing principle prices: McLean & Pontiff (2016) find published anomalies decay ~26%
out-of-sample and ~58% post-publication [LIT, the CONTRACT's governing citation, high confidence];
Hou, Xue & Zhang (2020) replicate ~450 anomalies and find roughly two-thirds fail careful
out-of-sample replication [LIT, MEDIUM CONFIDENCE — booked via `docs/fundamentals/02`]. A "value
composite" built by backtesting five candidate metrics and keeping the best three is not a
composite in the sense the literature validates — it is five trials wearing one costume, and
under CONTRACT §9's deflated-Sharpe standard every metric considered and discarded is a counted
trial, not a free look. The defensible order is the opposite: fix the metric list and weighting
scheme from ex-ante economic reasoning before any return is computed — §1's pre-registration
discipline applied to composite design, not only individual signals.

---

## 3. Structural adjustments

**Sector/industry neutralization.** **Asness, Porter & Stevens** ("Predicting Stock Returns Using
Industry-Relative Firm Characteristics," circulated from 1994) test ranking value characteristics
WITHIN industry rather than across the whole universe; the finding most often cited is that
industry-relative ranks perform comparably to raw cross-sectional ranks while measurably reducing
the sector-concentration/timing risk a raw universe-wide sort carries (which overweights whichever
sectors are cyclically cheap at a point in time) [LIT, MEDIUM CONFIDENCE on the finding, LOW on
magnitude — not independently verified against the paper's own tables]. For this desk,
sector-neutral value is a risk-reduction tool, not return-enhancement: CONTRACT §3 leaves sector
exposure fully active for the portfolio, but that is separate from whether the SIGNAL itself
should be industry-relative before the optimizer sees it — a raw rank conflates "this stock is
cheap" with "this stock's sector is cheap." Dossier c §4 reaches this same consequence
independently for India's mix-contaminated index series; this section supplies the literature
anchor it did not cite.

**Intangibles-adjusted book value — does it resurrect P/B?** **Peters & Taylor** (2017, *JFE*
123(2), "Intangible Capital and the Investment-q Relation") build a "Total Q" adding capitalized
R&D/SG&A-derived intangible capital to physical capital and find it materially improves the
investment-q relation [LIT, MEDIUM CONFIDENCE, LOW on magnitude]. **Eisfeldt & Papanikolaou**
(2013, *J. Finance*, "Organization Capital and the Cross-Section of Expected Returns") capitalize
SG&A into "organization capital" and find firms with high organization-capital intensity earn a
return premium, framed as compensation for a labor-mobility risk specific to knowledge-intensive
firms [LIT, MEDIUM CONFIDENCE]. Whether this resurrects P/B is exactly §1's unresolved
Arnott-vs.-Israel-Laursen-Richardson debate: partially, with the share attributable to
intangibles specifically still contested. The desk's existing decision (value-deep dossier) is
not to build a separate intangibles-adjusted-HML sub-signal until India's own intangible-intensity
profile is checked — open, not settled by assertion here.

**Accounting-regime effects.** Any book-value-, ROE- or leverage-based measure crosses a hard
accounting-regime seam in every major market: US-GAAP-vs-IFRS goodwill and R&D-expensing
conventions differ enough that a raw cross-country comparison needs an adjustment layer, and — the
India instance already booked (`docs/fundamentals/02`) — Ind-AS 116's ~2019 lease-capitalization
mandate pulls off-balance-sheet operating leases onto the balance sheet, inflating assets and
liabilities and breaking pre/post-2019 comparability for lease-heavy sectors (retail, aviation,
hospitality) absent an explicit seam flag. Dossier c §2(b) documents the fuller Ind-AS phase-in
timeline; not repeated here.

---

## 4. Model-based methods — evidence beyond ratios, or narrative?

**Residual income / Ohlson.** Ohlson (1995, *Contemporary Accounting Research*, "Earnings, Book
Values, and Dividends in Equity Valuation") expresses intrinsic value as current book value plus
the present value of expected FUTURE abnormal earnings (ROE in excess of cost of equity) —
mechanically, RIM is book value plus a forecasted-ROE-trajectory adjustment, not an input
independent of what B/P and forward-ROE forecasts already contain. **Frankel & Lee** (1998, *J.
Accounting and Economics*, "Accounting Valuation, Market Expectation, and Cross-Sectional Stock
Returns") build a V/P ratio from an RIM-based intrinsic-value estimate and find it predicts
cross-sectional returns, with some non-US corroboration [LIT, MEDIUM CONFIDENCE on the finding;
LOWER on exact magnitude/country coverage]. Verdict: RIM-based value restates the same underlying
information (book value, earnings quality, growth) through a DCF lens — evidence for that
information's value, not for RIM as an independent force — and it is analyst-forecast-hungry,
plausibly failing below roughly the top 200–300 Indian names by analyst coverage, capping RIM's
universe well short of NIFTY 750.

**Reverse-DCF / market-implied expectations (Mauboussin).** Mauboussin & Rappaport's "Expectations
Investing" inverts the standard DCF: rather than forecasting cash flows and discounting to a
price, it backs out the growth/margin/ROIC path the CURRENT price already implies, then asks
whether that path is more or less demanding than an independent view. This is explicitly a FRAME,
not a factor — no published, replicated return-predictability literature exists for "buy stocks
where implied expectations look too low" as a standalone signal; the value sits entirely in the
judgment applied to the implied-vs.-independent gap, a Stage 2 (human/AI forward-view) tool under
this program's architecture (CONTRACT §2), not a Stage 1 input. It earns its place as a NARRATIVE
check on a mechanical screen's output, never as an independently-sized signal.

**Tobin's q.** Classical Tobin's q (market value of assets over replacement cost) is, in its
simplest form, functionally an inverse valuation ratio close to inverse book-to-assets. The
Hou-Xue-Zhang "q5" family repurposes it: not as the return-predicting characteristic itself, but
as one of three inputs (with cash-flow/assets and 4-quarter ROE change) FORECASTING future
investment growth via Fama-MacBeth regression, with the forecast itself — not q directly —
becoming the traded characteristic ("R_EG," expected growth). The desk has directly engaged this.
**QG-D5** (`research/register/trial-ledger.md`, 2026-09-08) regresses the US R_EG factor on FF6
and finds the alpha is NOT spanned (+8.34%/yr, t=10.9, R² 0.46) — flagged, not celebrated, because
the vaulted sample ends exactly at the paper's own publication date, so every month of the alpha
was available when the forecasting weights were fit [BOOKED QG-D5]. **QG-D6** (same file,
registered 2026-09-08, still UNRUN pending the India fundamentals handoff) freezes the identical
recipe for a NIFTY 500 replication — log Tobin's q, CFO/assets and 4-quarter ROE change forecasting
one-year investment growth on an expanding, purged Fama-MacBeth window, decile-sorted — with the
prior that a positive India OOS print would soften the US specification-search flag while a null
confirms it, and a Sharpe above 1 is grounds for suspicion, not celebration [BOOKED QG-D6]. This is
dossier c's design #4, quoted verbatim there — cited here as the model-based method most directly
under this desk's own test, genuinely open and not yet adjudicated.

**Sum-of-parts.** No academic return-predictability literature comparable to B/M or EV/EBITDA
exists for sum-of-parts valuation — a broker technique for diversified conglomerates (value each
segment on its own peer multiple, sum, compare to the consolidated price), evidence for which is
case-based and narrative, not factor-tested. Directly relevant to India's ownership structure
(§6): promoter-group holding companies and cross-held conglomerates are exactly the setting
sum-of-parts targets, and the "holding company discount" it addresses is real and widely observed
but Tier-C pending a dedicated India build.

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
countries); only the 20-year horizon (+0.36 vs. a [−0.19, +0.32] null band) beats the null [BOOKED
ER-D1c]. In plain terms: the familiar "rising staircase" of dp's apparent forecast power through
10 years — the same shape every index-level valuation-timing chart shows — is exactly what
persistence plus overlapping-window regression manufactures under a null of NO true predictability
at all (Stambaugh 1999's persistent-regressor bias [LIT, high confidence]; the desk's design also
invokes a "BRW (2008)"-type overlapping-horizon null test [desk citation, per the ER-D1c entry
itself — authors' initials not independently re-verified]). **ER-D4b** (same file, 2026-09-05),
running the honest purged, train-only-fitted-bounds correction CONTRACT §9 requires, confirms this
from a different angle: the pooled 10-year "OOS R² > 0" read survives neither benchmark cleanly,
and its 90% bootstrap band on that R² includes zero — the correction fires, and "Goyal-Welch wins
at both horizons" is the honest read [BOOKED ER-D4b]. **ER-D7** (2026-09-05) is the constructive
residue: a real-time, non-lookahead corner spread of +5.1pp/yr (cheap+low-inflation vs.
expensive+high-inflation) PASSES its own bar, but the same entry's point-forecast cells FAIL
(−29.8%/−27.2% OOS R² at 5/10y) [BOOKED ER-D7] — index-level valuation survives ONLY as an
expectations/state qualifier, never as a return forecaster with a quantified point estimate.

The cross-section is a genuinely different mechanism, and the desk's own **SC-D1** print
(2026-09-10) is directly on point even though it targets small-vs-large rather than value-vs-growth
directly: a Pb-based valuation SPREAD across size terciles orders next-12-month relative returns
monotonically (T1 cheap-small +28.78%/yr vs. T3 +12.73%/yr, a +16.05pp spread, in-sample/
first-gate, US data), with the spread-return correlation RISING with horizon (−0.26/−0.50/−0.69 at
1/12/36 months) [BOOKED SC-D1] — the opposite signature from the index-level ladder's collapse
under the null. The divergence is not a coincidence: a cross-sectional spread does not require
forecasting where the WHOLE market's single persistent series is going — it only requires the GAP
between two contemporaneously-priced stocks to close, a trade arbitrage capital can execute
stock-by-stock without any aggregate-market view, measured across many simultaneous names (breadth
substitutes for the time series' scarcity of independent observations underlying Stambaugh bias).
This is precisely Cohen, Polk & Vuolteenaho's (2003, *J. Finance*, "The Value Spread")
construction, already anchored in dossier b §6: the spread predicts the value FACTOR's own
subsequent return — a cross-sectional object re-embedded in time — not the aggregate market's
forward return regressed on its own valuation. The desk's existing value evidence base
(Fama-French 1992/1993/1998, Asness-Moskowitz-Pedersen 2013, the India AJV HML replication, all in
dossiers b/02/value-deep) sits entirely on this cross-sectional side and is the stronger,
Tier-A-grade evidence; the index-level side is now formally demoted by three independent, purged
designs. The consequence: valuation belongs in the cross-sectional stock-selection engine (Stage
1's factor book) as a live signal, and in the cycle/regime layer only as a STATE qualifier that
sizes exposure — never as a market-timing forecast with its own claimed point estimate.

---

## 6. India specifics

Dossier c owns the full India measurement-distortion and design-build treatment (its §2 a–e: the
2021 splice, Ind-AS transition, promoter cross-holdings, banks' P/B, PSU discount; its §3
trap-marker ranking), not repeated here. Two points this dossier adds:

**The consolidated/standalone splice, restated for the toolkit.** NSE switched its published
index-level P/E from standalone to consolidated earnings in **2021-03** [RUNSHEET row,
`ingest/vault/index_valuation/`, added 2026-09-10 off SC-D1's India ask — "a splice break that
must be authenticated, not smoothed"], a genuine level break in the one continuously-published
Indian valuation series; the identical basis choice recurs at the firm level in the incoming
fundamentals handoff's `statement_basis` field. Every multiple in §1 touching book value, earnings
or leverage inherits this seam; only sales/price and pure price-based measures (dividend yield,
buyback yield) are immune to it by construction.

**The practical measure ranking for Indian data quality — by refresh cadence, not literature
pedigree.** Per the desk's India data-engineering read (`research/cycles/value-deep/
partC-data.md`): **E/P and sales/price** refresh cleanly every quarter (PAT and revenue are both
quarterly-native, no balance-sheet dependency) — the cleanest pair for an India-first construction.
**Dividend yield** is next: event-based plus quarterly, least restatement-exposed, subject to §1's
payout confound. **B/P** is a HALF-YEARLY STAIRCASE, because the Indian balance sheet is disclosed
only twice a year (September, March): Asness & Frazzini's stale-book warning is forced by the
disclosure calendar here, not an optional convention as in the US. **CF/P** inherits the same
staleness. **EV/EBITDA is the worst-behaved multiple** — it mixes cadences within one ratio
(quarterly EBITDA, semi-annual net debt), a hazard additional to its Loughran-Wellman case in §1.
Financials must be excluded from any universe-wide raw pool entirely, each reporting under its own
statutory format; P/E and P/B for these names rank only WITHIN financials — dossier c §2(d)
develops the banks NPA-adjustment problem this creates.

---

## Edge candidates for this desk

1. **Profitable-value composite** — majority price-only (E/P + sales/P + buyback/NSI), minority
   lag-buffered B/P, computed within-industry. *Mechanism*: cheap and high-quality are close to
   orthogonal (Novy-Marx, dossier b §2); industry-relative ranking (§3) isolates stock cheapness
   from sector cheapness. *Magnitude*: comparable to value-alone in global tests [LIT, MEDIUM
   CONFIDENCE]; India magnitude untested, bounded by the AJV-vs.-mirror gap dossier c flags.
   *Data needed*: quarterly PAT/revenue, semi-annual book value/CFO, delisted registry, a
   sector-classification tag (dossier c §6's own gap).
2. **Total shareholder yield** (dividend + buyback − issuance), a price-only India input.
   *Mechanism*: Boudoukh et al.'s total-payout argument (§1); shares outstanding is quarterly-
   native, essentially restatement-immune. *Magnitude*: [LIT, LOW CONFIDENCE — US evidence only,
   no India transfer]. *Data needed*: quarterly shares-outstanding + dividend declarations, among
   the cheapest signals to build.
3. **Value-spread-as-conditioner** (Cohen-Polk-Vuolteenaho), sizing not timing. *Mechanism*: §5's
   cross-sectional spread predicts the value FACTOR's own forward return; widen the value/momentum
   allocation when the spread sits in its own cheap tercile, tilt toward momentum when tight —
   explicitly not an index-level timing rule. *Magnitude*: no clean number; directionally
   supported by the desk's value-deep case studies. *Data needed*: #1's panel, live each rebalance.
4. **India small-vs-large valuation-spread size-rotation signal.** *Mechanism*: SC-D1's US first
   gate passed in-sample (§5); the India version is a registered runsheet ask once the NSE
   index-P/E-P/B pull lands with the 2021 splice authenticated (§6). *Magnitude*: US in-sample
   only — no India number yet; Tier-C/monitor per SC-D3's own consumption cap. *Data needed*: the
   NSE index P/E-P/B-yield RUNSHEET row.
5. **Explicit non-edges**, stated to prevent re-litigation (CONTRACT bars are never moved):
   index-level valuation (dp/CAPE) as MARKET-TIMING is REJECTED — ER-D1c/ER-D4b/ER-D7 (BOOKED, §5)
   show it null-consistent through 10 years; reverse-DCF/RIM are Stage-2 frames only; aggregate
   dividend-payout timing (QG-D1, BOOKED, §1) is a repackaged earnings-state variable, not a signal.

---

## Data requirements — India

1. **As-filed quarterly fundamentals with an explicit `statement_basis` field** (handoff P1) —
   unlocks E/P and sales/P at quarterly cadence and the staircase builds for B/P, CF/P, EV/EBITDA;
   the field lets a basis-switch be treated as a structural break, not noise (§6).
2. **NSE index P/E, P/B and dividend-yield daily history since ~1999, 2021-03 splice authenticated
   as two regimes** — the registered RUNSHEET row (`ingest/vault/index_valuation/`), needed for
   edge candidate #4 and as a continuously-checkable validation bench for any built panel's level.
3. **A sector/industry classification per company** — neither the handoff nor any existing pull
   carries a GICS-like tag; without one, edge candidate #1's within-industry construction (§3, §6)
   cannot be built. Dossier c §6 flags this as an ask appended to the NSE sectoral-TR RUNSHEET row.
4. **Free-float shares outstanding, separate from total** — needed for free-float-adjusted P/B and
   market cap given India's structurally high (~45–50% median) promoter blocks and the
   cross-holding distortion dossier c §2(c) documents; not its own field in the handoff today.
5. **SEBI shareholding-pattern and promoter-pledge history** — already a handoff deliverable (P5),
   point-in-time by regulatory construction; needed for the free-float adjustment above and the
   pledge-acceleration trap screen dossier c §3/§5 already designs in full.
6. **Damodaran India/EM industry vintages** (an existing RUNSHEET row) — the free source for
   sector-relative benchmarks feeding edge candidate #1's industry-neutral construction until a
   native NSE sector classification lands.
