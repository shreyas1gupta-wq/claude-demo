# Small-cap vs Large-cap: What Predicts the Relative Return

*Literature dossier, Track ES (equity size), 2026-09-10. No live data access this session
(egress blocked outside GitHub) — literature-only, from training knowledge, no web
verification possible. Every quantitative literature claim carries **[LIT]**; where the
magnitude is recalled with less confidence than the citation itself, **[LIT, LOW
CONFIDENCE]**. Desk numbers are quoted verbatim from `research/register/trial-ledger.md`
entry TL-D2 and marked **[DESK, TL-D2]** — they are not re-derived here. This dossier is
the timing/predictability layer on top of TL-D2's already-booked verdict: the US small
premium is positive and durable (+1.5–2.7pp/yr across 1/5/10/20y horizons, 1.32x the
market's vol) while the Indian smallcap segment at factor level *underpaid* (-2.9pp/yr
over 32 years on the IIMA market+SMB proxy, 1.34x vol, -90% vs -62% max drawdown)
**[DESK, TL-D2]** — "the smallcap money in India is selection inside the segment, never
the segment" **[DESK, TL-D2]**. Per CONTRACT §4, every citation below is cross-country/US
evidence unless stated India-specific, so Tier B at best for this program until an India
replication exists.*

## 1. The size premium itself: discovery, death, and contested resurrection

Banz (1981, *Journal of Financial Economics*, "The Relationship Between Return and Market
Value of Common Stocks") is the origin point **[LIT]**: on NYSE common stocks 1936–1975,
the smallest-market-cap quintile earned risk-adjusted (CAPM-residual) returns
meaningfully above the largest quintile, with the effect concentrated and nonlinear —
most of it lived in the smallest decile, not spread evenly across the size spectrum
**[LIT]**. Banz himself flagged the finding as unstable across sub-periods and likely
proxying for something else the one-factor CAPM omitted, not a clean "small beats big"
law **[LIT]** — a caution the literature spent the next four decades chasing. Reinganum
(1981) **[LIT]** produced a contemporaneous, independent confirmation and, jointly with
Keim (1983, *JFE*, "Size-Related Anomalies and Stock Return Seasonality") **[LIT]**,
established that the size effect was disproportionately a **January** effect — a large
share of the annual small-minus-large spread realized in the first two weeks of January,
consistent with tax-loss-selling pressure unwinding **[LIT]**. This seasonal
concentration became the first crack in "size" as a clean risk premium: a true priced
risk factor should not care what month it is.

The premium's post-publication history is the textbook case for CONTRACT §5's governing
principle. Dimson & Marsh (1999, *Journal of Portfolio Management*, sometimes cited as
"Murphy's Law and Market Anomalies") documented the **reverse size effect** **[LIT]**:
UK (and, in companion work, US) small caps materially *underperformed* large caps
through most of the decade following the size literature's popularization (roughly 1987
into the late 1990s), the opposite sign of Banz **[LIT, LOW CONFIDENCE on exact
magnitude]**. Horowitz, Loughran & Savin (2000, *Research in Economics*, "The
Disappearing Size Effect") independently found the US size premium statistically
indistinguishable from zero once past the original discovery sample **[LIT]**. Van Dijk
(2011, *Journal of Banking & Finance*, "Is Size Dead? A Review of the Size Effect in
Equity Returns") is the standard survey verdict **[LIT]**: the premium is small,
sign-unstable, and highly sensitive to design choices — equal- vs value-weighting,
NYSE-only vs all-exchange breakpoints, microcap inclusion, and sample start date all
flip the answer **[LIT]**. Crain (2011) reaches the same conclusion independently
**[LIT, LOW CONFIDENCE on specific figures]**.

Two methodological corrections matter for anyone re-running "size" on any market,
including India. First, **delisting bias**: Shumway (1997, *Journal of Finance*, "The
Delisting Bias in CRSP Data") showed that databases (CRSP, and by extension most
free/derived series) frequently record no return, or an incomplete one, for stocks that
delist — disproportionately small, failing firms — and that this missing-return problem
biases measured small-cap returns *upward*, because the worst outcomes (bankruptcy,
forced delisting at a fraction of last traded price) are undercounted **[LIT]**; Shumway
& Warther (1999) extended this to NASDAQ, where the bias is larger given the heavier
small-cap concentration **[LIT]**. Second, **microcap dominance of naive decile tests**:
Fama & French repeatedly note that the smallest NYSE-equivalent decile is roughly 1–3% of
US market capitalization but a large majority of the *number* of listed names **[LIT,
LOW CONFIDENCE on exact share]**, so equal-weighted "size effect" tests are effectively
tests of microcap behavior, contaminated by wide bid-ask spreads, stale/non-synchronous
pricing, and poor tradability — this is the same mechanism the desk's own TL-D2 s9 cell
flagged in India's survivor-tercile daily series (illiquidity AR(1) signature)
**[DESK, TL-D2]**.

The modern resurrection argument is Asness, Frazzini, Israel, Moskowitz & Pedersen
(2018, *Journal of Financial Economics*, "Size Matters, If You Control Your Junk")
**[LIT]**: they show the raw size premium's instability is largely explained by small-cap
portfolios' heavier average tilt toward **junk** — low profitability, high investment,
high distress risk, high leverage, low quality by their QMJ score — relative to
large-cap portfolios. Once you hold quality/junk exposure constant (long small-quality,
short large-quality, or equivalently a size premium purged of the junk tilt), the size
premium is large, statistically strong, stable across sub-periods back to 1926, and
replicates across ~20 non-US developed markets and within tighter size bands (i.e., not
purely a microcap-liquidity artifact) **[LIT]**. This is the single most important paper
for this desk's India puzzle: it reframes "does size pay" as "does *quality-controlled*
size pay," and implies the raw negative India print in TL-D2 could partly be a junk-tilt
effect rather than a pure size effect — a hypothesis to test explicitly on India data,
not assume transfers (§6 below).

Finally, construction matters mechanically. The Fama-French SMB factor is built from an
independent 2x3 (or later 2x3x3/2x2x2x2) sort on size **and** book-to-market using NYSE
breakpoints, value-weighted within cells, long small/short big averaged across the
value-tilt dimension **[LIT]** — this is a world away from a naive smallest-decile-minus-
largest-decile spread. SMB is deliberately *not* a pure size bet (it nets out some value
tilt by construction) and is value-weighted (so it is not dominated by the tiniest
names the way an equal-weighted decile spread is) **[LIT]**. This desk's own US-small
proxy in TL-D2 (market + SMB, from the vaulted FF3 file) inherits SMB's construction
discipline **[DESK, TL-D2]** — which is precisely why TL-D2 flagged its own
proxy-vs-true-ME-decile gap explicitly (s4: the -90% ME-decile 1929-32 prior missed at
-85%, "proxy artifact stated" because market+SMB compresses true bottom-decile depth)
**[DESK, TL-D2]**. Pure decile tests and SMB-based tests are answering related but
distinct questions, and conflating them is a standing trap for this program.

## 2. Timing the size factor: does valuation-spread conditioning work

The template for factor timing via valuation spreads comes from the value literature and
was explicitly extended to size early on. Asness, Friedman, Krail & Liew (2000, *Journal
of Portfolio Management*, "Style Timing: Value vs Growth") **[LIT]** show that the
**value spread** — the valuation gap between the value and growth legs of a style
portfolio — has some in-sample power to forecast subsequent value-minus-growth returns:
wide spreads (value very cheap relative to growth) tend to precede stronger value
performance **[LIT, LOW CONFIDENCE on out-of-sample magnitude]**. The natural analogue
for size is the *size value-spread*: the valuation gap between small and large (e.g.,
big-cap median P/B or P/E minus small-cap median), used as a timing signal for when to
overweight the small side. This size-specific version is far less studied in the
peer-reviewed literature than the value-vs-growth spread itself — most of what exists is
practitioner overlay work (e.g., desks using the Russell 2000-vs-1000 or S&P 600-vs-500
relative P/E as a tactical size tilt) rather than a settled academic result **[LIT, LOW
CONFIDENCE]**.

Cohen, Polk & Vuolteenaho (2003, *Journal of Finance*, "The Value Spread") is the
essential caution on this whole family of signals **[LIT]**: decomposing what a wide
value spread actually forecasts, they find it is dominated by *rationally justified*
expected cash-flow (growth) differences between the cheap and expensive legs, not by a
mispricing that must correct through *returns* **[LIT]**. Applied to size: if the small
side trades cheap relative to large mostly because the market correctly expects small
firms' fundamentals to disappoint (financing risk, distress, weaker moats), a wide size
spread is not automatically a "buy small" signal — it may just be efficient pricing of a
genuine growth-differential forecast, and the naive timing trade earns nothing extra for
the risk taken **[LIT]**. This is the load-bearing kill condition on every valuation-
spread-based size-timing idea below.

The broader factor-timing skepticism is best summarized in the AQR line of work usually
cited as Asness, Ilmanen, Israel & Moskowitz, "Contrarian Factor Timing is Deceptively
Difficult" (~2016–2017, practitioner/working-paper venue) **[LIT, LOW CONFIDENCE on
exact venue/year]**: valuation-spread-based factor timing (applied to value, and by
extension size) looks compelling largely because of one or two large episodes (dot-com
value cheapness/richness being the dominant one), the effective sample of independent
timing "calls" is tiny once overlap/autocorrelation are accounted for, and out-of-sample
results are far weaker than in-sample backtests suggest **[LIT]**. This is
directly convergent with CONTRACT §5's governing principle (McLean & Pontiff decay,
Chordia-Subrahmanyam-Tong attenuation) and with the Arnott, Beck, Kalesnik & West line
(Research Affiliates, ~2016, "How Can 'Smart Beta' Go Horribly Wrong?" and the related
"revaluation alpha" debate) **[LIT]**: a large share of what look like factor-timing wins
or size/value premia historically is **valuation re-rating** (multiple expansion) rather
than a repeatable structural premium, meaning a size-timing rule that fires "small is
cheap, buy small" during a period that later re-rates further downward (rather than
mean-reverting) has no floor under it — the spread being wide does not bound how much
wider it can get. Arnott's camp and Asness's camp disagree on how much of realized factor
returns are "real" vs re-rating, but both agree the practical implication is the same:
treat any size-timing signal as a weak, noisy tilt, never a switch.

Net read for this desk: valuation-spread conditioning of size has a plausible mechanism
and a respectable pedigree (the value-timing template), but (a) it is far less validated
specifically for size than for value, (b) the Cohen-Polk-Vuolteenaho decomposition is a
real threat to the "it's mispricing" story, and (c) the Asness/Arnott timing-fragility
debate applies with at least equal force. Any size-spread timing signal this desk builds
needs the CONTRACT §5 survival argument in writing before it earns budget.

## 3. State dependence: recessions, credit, liquidity, rates, and the January decay

**Recovery/credit-state conditioning** has the strongest, most specific academic anchor
in this whole dossier: Perez-Quiros & Timmermann (2000, *Journal of Finance*, "Firm Size
and Cyclical Variations in Stock Returns") **[LIT]**. They model small-firm excess
returns as regime-dependent on credit conditions (a default-spread/short-rate-based
state variable) and find small firms behave like high-beta, credit-sensitive assets:
excess returns and volatility both spike when credit conditions are tight and then ease,
producing the sharp small-cap outperformance episodes seen coming out of recessions and
credit crunches **[LIT]** — consistent with the general "small caps rebound hardest off
troughs" practitioner observation catalogued in surveys such as Ilmanen (2011, *Expected
Returns*) **[LIT, LOW CONFIDENCE on precise multiplier]**. Mechanically this is a
leverage/financing-constraint story: small firms carry proportionally more short-term,
floating-rate, and bank-dependent financing, so their equity is a levered, high-beta
claim on the same macro cash flows large firms hold more safely financed — credit easing
disproportionately re-rates the small side. This is the cleanest state-dependence
candidate to actually build (§6), but CONTRACT §8 bans fitting regime-switching models
with fewer than 10 observed transitions, and high-conviction Indian credit-cycle turns
at the needed frequency almost certainly fall short of that bar — so it is a Tier-C
state variable (reduce risk, do not size alpha to it) until transition counts are
checked.

**Liquidity state**: Amihud (2002, *Journal of Financial Markets*, "Illiquidity and
Stock Returns: Cross-Section and Time-Series Effects") **[LIT]** establishes both that
illiquidity is priced in the cross-section (concentrated in small/illiquid names) and
that aggregate illiquidity is itself time-varying and spikes in downturns **[LIT]** —
meaning the small-cap illiquidity premium is not a constant, it widens exactly when
funding/liquidity conditions are worst, which is also when investors can least afford to
hold an illiquid asset (a "premium you can't easily collect" caution, echoed in this
desk's own TL-D2 s9 illiquidity/stale-price flag on the India survivor-tercile daily
series **[DESK, TL-D2]**).

**January effect decay**: having been discovered and published (Keim 1983 **[LIT]**),
the January seasonal in size returns is a direct test case for CONTRACT §5's decay
doctrine. Subsequent literature (e.g., work following Mehdian & Perry into the 1990s-
2000s U.S. sample, generally cited under "the declining January effect") documents the
January size seasonal weakening substantially after it became well known and after
1986 Tax Reform Act changes altered US tax-loss-selling incentives **[LIT, LOW
CONFIDENCE on the exact decay curve/paper]** — a clean, if dated, empirical instance of
McLean-Pontiff-style post-publication attenuation, and a reason not to build any India
size-timing rule around a calendar effect without first checking whether it has already
been arbitraged away in the sample used to discover it.

**Rate regimes**: less rigorously isolated in the academic literature specifically for
size (most rate-regime factor work is done on value/momentum), but the financing-cost
mechanism above implies falling-rate regimes should favor small caps via cheaper
rollover/floating-rate cost and via the same credit-easing channel Perez-Quiros &
Timmermann identify **[LIT, LOW CONFIDENCE, inferred rather than directly cited]**. This
converges directionally with this desk's own FUN-D8 finding (falling-rate regimes higher
mean return, slope ranks returns) but that finding was booked for the market factor, not
size specifically — do not transplant it to size without a dedicated test.

## 4. Growth differentials: do small caps actually grow faster, and does the gap predict returns

The naive small-cap growth story ("small companies are young and grow into large ones")
is weaker in the data than the narrative suggests. Fama & French (1995, *Journal of
Finance*, "Size and Book-to-Market Factors in Earnings and Returns") **[LIT]** is the key
paper: they show that small, low-book-to-market ("small growth") firms as a group have
persistently *low or negative* profitability relative to what their price multiples
imply, and that this weak-earnings characteristic is durable, not a transient
post-IPO phase **[LIT]**. In other words, the market prices many small-growth firms for
fundamental growth that then fails to show up — a realized-vs-priced-in growth gap that
is systematically negative for this cell, not noise around zero.

This shows up directly in return sorts. In the Fama-French 25 size-by-B/M portfolios,
the small-cap, low-B/M ("small growth") corner is the worst-performing cell of the
grid, historically underperforming every other size-value combination by a wide margin
**[LIT]** — the "lottery ticket" corner referenced in the task brief. Kumar (2009,
*Journal of Finance*, "Who Gambles in the Stock Market?") **[LIT]** supplies the
behavioral mechanism: stocks with small size, high idiosyncratic volatility, and high
positive skew (the statistical profile of a lottery payoff) are disproportionately
bought by retail/individual investors with gambling preferences, bid up beyond
fundamentals, and subsequently underperform **[LIT]** — a demand-side explanation for
why the small-growth cell keeps disappointing rather than a supply-side (fundamentals)
one alone; the two reinforce each other.

**Dilution** is the second half of the growth-gap story and is, if anything, more
mechanical. Fama & French (2008, *Journal of Finance*, "Dissecting Anomalies") **[LIT]**
identify net share issuance as one of the strongest return-predictive anomalies in US
data, with the effect concentrated in small-cap names: firms that issue equity
(follow-ons, private placements, warrant/ESOP overhangs) subsequently underperform,
firms that buy back outperform, and small-growth firms are disproportionately serial
issuers because they are cash-flow-negative and rely on capital markets rather than
retained earnings to fund growth **[LIT]**. The mechanism is direct: whatever
revenue/asset growth a small firm delivers, per-share (EPS, book value per share)
growth is diluted below the headline number by the share count expansion needed to fund
that growth — so the "small caps grow faster" claim can be true at the enterprise level
and still false, or reversed, at the per-share level an equity holder actually owns.
This is exactly the sense in which "growth" at small caps is frequently a mirage for the
public shareholder: the operating story can be real while the per-share economics are
not, and net issuance is the observable proxy for the gap between the two.

Net conclusion for this section: the realized/priced-in growth gap is a real and
persistent predictor of the *worst*-performing size-value-growth cell, and dilution is
its most mechanical channel — which argues for building any India small-cap "growth"
signal around per-share, dilution-adjusted growth (and net issuance itself as a
predictor) rather than headline revenue or profit growth, and treating "small-cap
growth" narratives with structural skepticism by default.

## 5. India specifically

**The 2017-18 SEBI categorization reform.** SEBI's October 2017 mutual fund scheme
categorization/rationalization circular fixed strict market-cap-rank buckets for equity
scheme categories — large cap defined as roughly the top 100 listed companies by market
capitalization, mid cap roughly ranks 101–250, small cap everything below rank 250
**[LIT]**. Because AMFI/AMCs had to reclassify every existing large-cap, mid-cap, and
small-cap scheme against these hard rank cutoffs, funds whose actual holdings sat near a
boundary were forced into mechanical buying/selling to conform, and this coincided with
(and is widely cited as a contributing supply shock to) the sharp 2018 correction in
Indian mid- and small-cap indices **[LIT, LOW CONFIDENCE on the reform's precise causal
share of the drawdown, which also coincided with the IL&FS default and a broader EM
risk-off]**. The IL&FS default (September 2018) triggered an NBFC funding-stress episode
that hit small- and mid-cap names disproportionately hard, since many were themselves
financing-dependent or held pledged-promoter-share collateral chains running through
the same stressed NBFC lenders **[LIT]** — the categorization reshuffle and the credit
event are best read as compounding, not competing, explanations for the 2018-19 India
smallcap bust.

**Index construction issues specific to India smallcap.** Four separate problems
compound here, each independently documented in market-structure literature and
practitioner commentary: (i) **survivorship** — a smallcap index's historical return
series, as commonly distributed, reflects the *current* constituent set's history more
than a true point-in-time-reconstituted history unless the index provider explicitly
preserves historical membership, meaning naive backtests overstate returns by excluding
names that failed and were dropped **[LIT, LOW CONFIDENCE — general index-methodology
point, not a specific paper]**, precisely the mechanism this desk's own TL-D2 flagged as
"maximum severity" in its survivor-tercile proxy **[DESK, TL-D2]**; (ii) **illiquidity**
— a large share of Nifty Smallcap 250 / BSE Smallcap constituents trade thin, with wide
bid-ask spreads and low daily turnover, so index-level returns computed off last-traded
prices can diverge materially from what is actually realizable at size **[LIT, LOW
CONFIDENCE, qualitative market-structure consensus]**; (iii) **circuit filters** — many
Indian smallcap stocks trade under 5/10/20% daily price bands, and in stress episodes
names lock at the lower circuit with no further trades — the index print for that day
understates the true clearing-price move because sellers are rationed, not because the
stock was worth that price **[LIT, LOW CONFIDENCE, market-structure consensus, not one
paper]**; and (iv) **promoter pledging** — concentrated promoter ownership with a
meaningful pledged-share fraction is disproportionately a small/midcap phenomenon in
India, and forced pledge-unwind sales triggered by lender margin calls have produced
some of the sharpest single-name smallcap crashes on record, a distinct, largely India-
specific tail risk with no large-cap analogue at comparable severity **[LIT, LOW
CONFIDENCE, well-documented market-structure fact, magnitude not quantified here]**. All
four push the same direction: India smallcap index-level statistics (returns, vol,
drawdowns) are systematically friendlier to look at than what a real portfolio could
have realized — a caution that applies with extra force on top of TL-D2's own stated
proxy limitations.

**The retail-flow / SIP era.** Systematic monthly SIP flows into Indian equity mutual
funds grew sharply from roughly 2016-17 onward, and small-cap-category fund AUM in
particular expanded by a large multiple over the subsequent years as retail investors
chased the segment's post-2013 and post-2020 returns **[LIT, LOW CONFIDENCE — a
compositional/flow-based claim, not a single citable paper, but a well-attested
practitioner/regulatory fact pattern]**. Because SIP flows are largely price-insensitive
(scheduled, not valuation-triggered) and concentrated in schemes with capped/gated
new-inflow policies at times of froth, this plausibly compresses the smallcap segment's
valuation cheapness during good return runs independent of any change in underlying
fundamentals — a flow-driven valuation-cycle amplifier layered on top of the
fundamental cycle, not a substitute for it.

**Valuation cycles, described qualitatively, no invented precision.** The pattern across
episodes: 2003-07 saw Indian smallcap valuations (relative to largecap) expand well
beyond their historical relationship, consistent with broad retail/IPO-driven froth
typical of that cycle globally **[LIT, LOW CONFIDENCE, qualitative]**; 2008 compressed
the relative multiple sharply below largecap, consistent with the segment's higher beta
and credit-sensitivity (Perez-Quiros-Timmermann's mechanism playing out in India) **[LIT,
LOW CONFIDENCE]**; 2013-17 rebuilt a smallcap premium, coincident with a strong SIP-flow
buildup and broad EM recovery; the SEBI-categorization-plus-IL&FS 2018-19 episode
compressed it again; and 2023-24 saw renewed froth, pronounced enough that SEBI directed
AMCs in March 2024 to run and disclose stress tests on small- and mid-cap scheme
liquidity (how fast a scheme could liquidate a defined portfolio fraction under stress),
given regulatory concern that valuations and one-way retail inflows had outrun realizable
liquidity **[LIT]** — a direct regulatory acknowledgment of the illiquidity/circuit-filter
mechanism in (ii)-(iii), and the closest thing here to an India-specific, dated, citable
valuation-cycle marker. The consistent shape across all five episodes: India's
small-vs-large relative valuation is a **flow-and-credit-amplified cycle**, wider swings
than the US analogue, with busts disproportionately triggered by a credit or
regulatory-structure shock rather than pure valuation mean-reversion — arguing for
conditioning any India size-spread signal on credit-state and flow-state jointly, not
valuation level alone.

## 6. Edge candidates for this desk

| Candidate | Mechanism | Horizon | Expected size | Kill condition |
|---|---|---|---|---|
| **E1 — Size value-spread mean reversion (India)** | Small-vs-large relative P/E or P/B at a rank extreme (small cheap) → forward relative-return tilt, per the Asness-Friedman-Krail-Liew value-timing template applied to size | 1–3y | Modest; international value-timing analogues suggest low-single-digit-to-mid-single-digit pp/yr tilts **[LIT, LOW CONFIDENCE]** — no India-specific number exists | Cohen-Polk-Vuolteenaho: if the spread is shown to forecast realized *growth* differences rather than mispricing, it is not a return-timing signal — kills the trade outright |
| **E2 — Credit-state conditioning of size (Perez-Quiros-Timmermann analog)** | Small caps behave as high-beta, credit-sensitive assets; overweight small only when a credit-spread/funding-stress state variable is easing from tight | 3–12m (regime turns) | International analog: large swings around turns; no sized India estimate | CONTRACT §8 bans regime-switching fits with <10 observed transitions — check the India credit-cycle transition count first; if <10, this is Tier-C (reduce-only), not an alpha source |
| **E3 — Quality-controlled size tilt (Asness et al. "Size Matters" analog)** | Within India smallcap, long quality/low-junk names only, avoiding the low-profitability/high-leverage tilt AFIMP show explains the US premium's instability | Strategic/structural | International quality-controlled size premium is large and stable **[LIT]**; TL-D2 shows India's *raw* segment premium is **-2.9pp/yr [DESK, TL-D2]**, so any positive result here must be earned on India data, not assumed | If a junk-filtered India smallcap subset still underperforms the market, this is not a new segment-level edge — it confirms the desk's already-booked verdict that India smallcap money is pure stock-selection, not segment beta |
| **E4 — Growth-gap / dilution short (small-growth "lemons")** | Small-cap, low-B/M, high-net-issuance names systematically disappoint priced-in growth (Fama-French 1995/2008) | ~1y, annually rebalanced | US 25-portfolio and issuance-anomaly literature shows large negative spreads in the extreme cell **[LIT]**; not sized for India | Needs free, point-in-time Indian share-issuance data (rights/QIP/warrant records) — if unobtainable PIT, cannot be built; also kill if subsumed by an already-booked quality/junk factor (redundant) |
| **E5 — Post-crash size rebound (event-conditioned)** | High-beta mechanical rebound + short-covering + credit easing after a large trailing-drawdown state (quantile-ranked, not a fixed threshold, per CONTRACT §6) | 3–6m tactical | International recovery-episode literature: high single-digit to double-digit pp outperformance over the rebound window **[LIT, LOW CONFIDENCE]**; untested for India | TL-D2 shows India smallcap crashes **deeper** (-90% vs -62% maxDD) **[DESK, TL-D2]** — if the rebound's risk-adjusted payoff doesn't exceed the incremental crash depth taken to get there, net edge is zero or negative once properly sized |

Every candidate above still needs its CONTRACT §5 survival argument written before
sizing: E1 and E2 lean on (iii) genuine risk premium (credit/liquidity risk someone must
be paid to bear); E3 leans on (i) a structural/behavioral mechanism (junk-avoidance)
argued to persist under crowding; E4 leans on (iv) an institutional constraint (small
firms' structural dependence on external equity financing); E5 is the weakest of the
five on survival grounds — it is close to "it backtests well" unless the credit/beta
mechanism is stated explicitly and shown to survive being known.

## 7. Data requirements — India

A genuinely point-in-time small-vs-large valuation-spread series needs four components,
none of which reduce to "download the current index P/E history":

1. **PIT constituent membership** at every historical rebalance date for both the
   large-cap and small-cap universes — not today's constituent list projected
   backward. Rank-250/rank-100 style cutoffs (post-2017 SEBI categorization) make this
   at least well-defined going forward, but pre-2017 membership must be reconstructed
   from historical index factsheets/rebalance announcements, not inferred.
2. **PIT trailing EPS/BVPS as originally reported**, not restated. This is the same
   restatement problem already flagged as known prior #7 in CONTRACT — free Indian
   fundamentals carry no knowledge-date stamp and bias backtests upward by a stated
   150-450bps/yr — and it applies with at least equal force to a size valuation-spread
   built off restated aggregates.
3. **PIT free-float market-cap weights** matching the index methodology in force at
   each date (methodology itself has changed — free-float transitions, rebalance
   frequency changes, the 2017 categorization-driven reconstitutions), so that
   aggregation weights are replicable independently rather than trusted as a black box.
4. **A stated, replicable aggregation method** (NSE's convention is a float-market-cap-
   weighted harmonic mean of constituent P/E) so a reconstructed series can be checked
   against the published one rather than assumed equivalent.

**Is NSE's published index P/E-P/B history methodologically PIT-usable?** Partially, and
the caveat matters. NSE publishes long daily P/E, P/B, and dividend-yield history for
Nifty 50, Nifty 500, Nifty Smallcap 250/100, and related indices, and that series is
*internally consistent* — NSE recomputes and republishes it under one stated
methodology, not a random stitch. But two problems survive: first, the underlying
constituent EPS figures feeding the ratio are the *currently known* (post-restatement)
trailing earnings at the time NSE computes the series, not the as-originally-filed
numbers investors saw in real time — the same restatement bias as known prior #7,
embedded silently inside an index-level aggregate, which makes it *harder* to correct
for than a firm-level fundamentals file. Second, the smallcap-specific indices are young
as live instruments (Smallcap 100 mid-2000s vintage, Smallcap 250 only from 2016) — no
native NSE-published smallcap P/E history reaches back to the 2003-07 or most of the
2008 episode in §5; any such reconstruction must be built bottom-up from constituent
data and reinherits the PIT-membership problem in point 1. Net verdict: NSE's published
smallcap valuation series is usable as a **directional, qualitative** signal from
roughly its live-index inception onward, but is **not** rigorous point-in-time backtest
input without an independent EPS-vintage reconstruction — consistent with CONTRACT's
trap against reporting a fundamental backtest without its price-only counterpart. That
price-only counterpart should be built regardless: a **relative-price** series (smallcap
index level ÷ largecap index level) is PIT-clean by construction — no restated
fundamentals needed — and carries the mean-reversion/momentum-state signal on its own,
exactly the instrument known prior #7 calls for.

Free-source inventory for this build: NSE index P/E-P/B-yield historical files (partial-
PIT, as above); NSE/BSE bhavcopy for a from-scratch relative-price series (fully PIT);
AMFI scheme-category NAV and AUM histories (a flow-state proxy, not a valuation series,
but usable for the SIP-flow conditioning in §5); RBI DBIE / CCIL for the credit-spread
state variable needed by E2; BSE Smallcap as an independent cross-check series against
Nifty Smallcap 250 where their live histories overlap.
