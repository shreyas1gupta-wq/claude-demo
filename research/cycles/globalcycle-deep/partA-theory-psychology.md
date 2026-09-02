# Global Financial Cycle Deep Dive — Part A & Part G

Part A: Theory — the one factor an India book cannot diversify away · Part G: Operator psychology
· v1.0 · 2026-09-02 · Atlas entry 2.8 (`docs/CYCLE_ATLAS.md` row 84, Band 2 — the business-credit
band); ladder seat `L9_global_financial_cycle` (`config/ladder.yaml`), Tier **A (pooled methodology)
/ B (India transfer)**, τ½ 3–9 months (episode, not era), drawing its own dedicated **20% of
regime-score budget** (`global_cycle` block) — the single largest seat on the ladder alongside
fast-stress (25%) and trend/TSMOM (20%), and the only Band-2 seat that does **not** share the
macro-credit block with L6/L10/L11/L12. Complements, never duplicates: `docs/cycles/20-mp-cycle.md`
(the monetary-policy-cycle monograph, whose own 2011–2014 case owns the RBI **rates**-side defense
of the 2013 episode in full — this chapter owns the **global** trigger and transmission only, and
does not re-derive the MSF/FCNR(B) mechanics); `docs/CYCLE_ATLAS.md` row 89 (2.13, FII/FPI flow
cycle, seat L14 — the flows-follow-returns finding is cross-referenced, never re-derived here);
`docs/cycles/14-commodity-supercycle.md` (the Kilian oil-decomposition machinery L9 consumes, not
reproduces); and this program's own `research/cycles/globalcycle-deep/global-RESULTS.md` (GF1–GF3,
the desk's own pre-registered checks on the Rey / Miranda-Agrippino-Rey claim, run on the JST panel)
and `research/cycles/globalcycle-deep/partCDEFH.md` (data engineering, algorithm, harvest map — this
file supplies the mechanism and psychology those parts compress into a state machine). Cases —
the nine-episode chronology including 2013 and May-2026 — are a sibling document; this file cites
their headline facts where the atlas names them as evidence, never re-builds the episode table.
Style and depth calibrated to `research/cycles/fincycle-deep/partA-theory-psychology.md`. Evidence
base: `research/dossiers/08-india-mid-cycles.md` (D08, §F3–F6, F8, F13, I6, I11).

This file assumes the ladder's frozen construct as given: L9 is a **risk-state conditioner**, never
a forecast of the Fed or a directional currency bet — it reads the dollar/VIX/US-real-rate triad
(FRED) plus NSDL FPI flows and INR against its 20% regime-score budget, Tier A on the pooled
cross-country mechanism and Tier B on India's own transfer coefficient, `reduce_only: false` (it can
add and subtract regime score, unlike the ladder's Tier-C reduce-only entries), and consumes a
Kilian-decomposed oil input specifically because a raw price level is structurally blocked by the
module's own unit test (`partCDEFH.md` Part E: `test_kilian_decomposition_rejects_raw_price_only_
input`). Part A supplies the theoretical machine that construct compresses into five free series;
Part G turns to the desk operating the one seat on the ladder whose defining property is that no
amount of India-specific skill diversifies it away.

---

## PART A — Theory: the one factor an India book cannot diversify away

### A.1 The object

**(i) Mundell-Fleming's corner solution, and why Rey calls it dead.** International macroeconomics'
oldest organizing device is the **trilemma**: a country can hold at most two of (a) a fixed exchange
rate, (b) free capital mobility, and (c) an independent monetary policy — the textbook corollary
being that an emerging market willing to float its currency and keep capital mobile *buys back* full
monetary independence, the canonical "corner solution" every open-economy macro course still
teaches. **Rey, Hélène (2013), "Dilemma not Trilemma: The Global Financial Cycle and Monetary Policy
Independence"** (prepared for the Jackson Hole Economic Policy Symposium, Federal Reserve Bank of
Kansas City, August 2013; circulated as NBER Working Paper 21162, May 2015) **[Verified — NBER
w21162; presented at Jackson Hole Aug 2013 per the paper's own front matter]** argues the corner
solution is a fiction under modern financial globalization. Her claim, stated as sharply as the
title: there exists **one global factor** in risky-asset prices and gross capital flows — driven by
center-country (US) monetary policy and the risk appetite/leverage cycle of global financial
intermediaries — that binds **regardless of exchange-rate regime**. A floating currency does not
insulate a country from the global cycle; it only changes *how* the shock arrives (via the exchange
rate and asset prices rather than via a fixed peg's forced reserve loss). The trilemma's implied
"dilemma" is therefore starker than the textbook version: independent monetary policy in the full
sense requires **managing the capital account** — not merely floating — because the global factor
transmits through bank leverage and portfolio-flow channels that a flexible exchange rate does not
block. This is the object atlas row 2.8 names, and it is the reason the ladder treats L9 as
qualitatively different from every other Band-2 entry: L6, L10, L11 and L12 are all, in their own
ways, phenomena the *Indian* policy and credit system generates and could in principle out-manage
with better domestic policy; L9 is a shock that arrives from outside India's own institutional
choices, floating rupee or not.

**(ii) Why the atlas grades this "A (pooled) / B (transfer)" — the factor itself.** **Miranda-
Agrippino, Silvia & Rey, Hélène (2020), "U.S. Monetary Policy and the Global Financial Cycle,"**
*Review of Economic Studies* 87(6): 2754–2776 **[Verified — RES 87(6):2754-2776; NBER WP 21722]**
operationalizes Rey's claim into an estimable object: extracting the **first principal component**
of a large cross-section of risky-asset returns (equities, corporate bonds, commodities) across
many countries and asset classes, they show one factor — correlated with implied and realized
volatility (VIX) and interpretable as the risk-taking capacity of global financial intermediaries —
explains a material share of the common variation in that cross-section, and that this factor
**tightens significantly following a contractionary US monetary policy shock**, transmitted through
the leverage of global banks and asset managers rather than through interest-rate parity alone. The
headline "how much variance" figure that the wider literature (including several of the paper's own
companion pieces, e.g. Miranda-Agrippino & Rey's earlier "World Asset Markets and the Global
Financial Cycle" work) reports for a single global factor in a broad risky-asset cross-section
clusters in the **roughly 20–25% range** **[VERIFY: exact reported variance-share figure and
sample — this session's search access could confirm the paper's headline claim and venue precisely
but not extract the specific point estimate from the published table itself; treat 20–25% as the
literature's own consensus band, not a number pulled from the primary source this session]**. This
is the basis for the atlas's **Tier A "pooled"** grade: the *methodology* — factor-model extraction
of a global common component from a large multi-country asset panel — rests on a well-replicated,
large-cross-section empirical regularity, exactly the kind of evidence base the Contract's tier
system means by "≥30 independent observations" when the observations are asset-return series rather
than discrete crisis events.

**(iii) The skeptical counter-read, presented honestly.** The atlas does not present the
Miranda-Agrippino-Rey factor as uncontested, and neither does this chapter. **Cerutti, Eugenio; Claessens, Stijn & Rose, Andrew K.
(2019), "How Important Is the Global Financial Cycle? Evidence from Capital Flows,"** *IMF Economic
Review* 67(1): 24–60 **[Verified — IMF Econ Rev 67(1):24-60]** run the harder test directly on
**capital flows themselves** — the object a country's policymaker actually cares about, one step
removed from asset *prices* — across a large panel of 85 countries and multiple decades of quarterly
flow data disaggregated by direction and instrument type. Their finding, stated in the paper's own
terms: evidence for a single, dominant "Global Financial Cycle" in **capital flows specifically** is
considerably weaker than the asset-price literature suggests — combined global factors **rarely
explain more than a quarter of the variation in capital flows**, with substantial heterogeneity by
country, instrument, and time period, and idiosyncratic/regional factors carrying real independent
weight. This is not a rejection of Rey's core claim about *asset prices and risk appetite*; it is a
sober correction to any temptation to read "one global factor moves risky asset prices" as
equivalent to "one global factor mechanically dictates how much capital flows into or out of any
given emerging market on any given quarter." **For our seat**, this is precisely why the ladder
grades the *methodology* Tier A but India's own **transfer coefficient** — how strongly India's
market specifically loads on the pooled factor, and how cleanly that loading shows up in flows
rather than just prices — Tier B: the pooled evidence licenses believing the factor exists and
matters; it does not by itself license assuming any particular country, India included, transmits
it at any particular strength without checking.

**(iv) The desk's own check — GF1–GF3.** Rather than import the transfer coefficient from a foreign
panel the way L10 borrows JST-pooled credit-crisis coefficients, this program pre-registered three
tests on its own vaulted data (`research/register/trial-ledger.md`, entries GF1–GF3;
`research/cycles/globalcycle-deep/global-RESULTS.md`) before running them, and the results are now
in. **GF1** (has the global factor itself *risen* — the pairwise co-movement of national equity
markets, pre- vs. post-1990, on the 16-country JST panel): **PASS**, decisively — median pairwise
correlation of annual real equity returns moved from **+0.28 pre-1990 (120 country-pairs) to +0.77
post-1990 (120 pairs)**, a difference of +0.49 against a ≥0.10 bar, described in the results file's
own words as "one of the cleanest results in the project." **GF2** (India's own loading on the
pooled factor, annual, 1994–2015, n=22 matched years): **PASS** — India's compounded market-factor
return correlates at **+0.57** with the equal-weight JST-panel mean real return against a ≥0.30 bar,
the seat's transfer premise measured in-house rather than merely asserted. **GF3** (breadth: in
years the pooled panel is down, what share of individual countries are also down, post-1950):
**FAIL** against its own ≥75% bar — median breadth is **69%** across 18 global-down years (1957,
1962, 1965, 1966, 1970, 1974, 1976, 1977, 1987, 1990, 1992, 1994, 2000, 2001, 2002, 2008, 2011,
2018). This third result matters as much for what it *refuses* to license as GF1–GF2 matter for
what they confirm — Part G returns to it directly, because a failed bar that lands at 69% rather
than 30% is not the same kind of finding as Cerutti-Claessens-Rose's "rarely more than a quarter":
it says the global factor is real, has risen, and transfers to India specifically, but is not
totalizing even now — "one cycle, in most places, most of the time," never "everywhere, always,"
and the desk is not licensed to assume in advance which years belong to the 69% and which to the
residual.

**(v) Synthesis — why the tier label is exactly right.** Reading (ii)–(iv) together explains the
atlas's precise phrasing, "A (pooled) / B (transfer)," better than either half read alone. The
factor's *existence and rise* (Miranda-Agrippino-Rey; GF1) is Tier-A-grade evidence — a large,
replicated, cross-country empirical regularity nobody on this desk needs to re-derive from scratch.
Its *transfer to India specifically* (Cerutti-Claessens-Rose's honest skepticism about flows;
GF2's confirming +0.57; GF3's honest breadth ceiling) is Tier-B-grade — good enough to build a
20%-budget ladder seat on, not good enough to assume without the desk's own check, and explicitly
not good enough to license a "this time India is decoupled" read in either direction.

### A.2 The machinery of transmission

**(i) The triad, and the fourth leg added post-2013.** The seat's construction (`ladder.yaml
L9_global_financial_cycle`, `indicator: "FRED VIX+dollar+DFII10, NSDL FPI, INR, Kilian index"`)
reads three market-observable legs jointly rather than any one alone, plus a fourth added
specifically because the pre-2013 triad under-specified the object once unconventional US monetary
policy made the term structure itself informative: **(a) VIX / risk appetite** — the CBOE
volatility index, the standard market-observable proxy for the risk-bearing capacity Miranda-
Agrippino-Rey's factor loads on; **(b) the broad (trade-weighted) US dollar index** — FRED's broad
dollar series, the balance-sheet-channel variable A.2(iii)–(iv) below makes precise; **(c) the US
policy rate / short-end path** — the direct Rey-Miranda-Agrippino-Rey monetary-shock channel; and
**(d) DFII10** — the 10-year US Treasury Inflation-Protected Security yield (FRED), a **real** yield
rather than a nominal one, added to the triad because after 2013 (the taper-tantrum year itself,
A.3(iii)) the *real* long rate — not merely the policy rate — became the variable global investors
watched for the marginal cost of US-dollar-denominated safety, and a nominal-rate-only construction
would have missed the 2013 episode's own defining feature: yields moved on **expectations of
balance-sheet normalization**, a real-rate phenomenon, well before any policy-rate hike actually
occurred. Each leg is read as its own expanding percentile (per the ladder's shared construction
discipline — no HP filter, no full-sample look-ahead), and the composite state is the co-movement
of dollar-up + VIX-up + real-yield-up — the literal Rey signature, per `partCDEFH.md` Part E's own
algorithm sketch.

**(ii) The leverage channel — Bruno-Shin.** Why should the dollar's *level* itself matter, rather
than only US rates? **Bruno, Valentina & Shin, Hyun Song (2015), "Cross-Border Banking and Global
Liquidity,"** *Review of Economic Studies* 82(2): 535–564 **[Verified — RES 82(2):535-564]**,
alongside the companion **Bruno, Valentina & Shin, Hyun Song (2015), "Capital Flows and the
Risk-Taking Channel of Monetary Policy,"** *Journal of Monetary Economics* 71: 119–132 **[Verified —
JME 71:119-132]**, supply the mechanism: global banks' balance-sheet leverage is **procyclical** —
when funding conditions ease (a weakening dollar, falling VIX, easy US policy), global banks'
own risk metrics (measured volatility, value-at-risk) read as more accommodating, so *the same
risk-management rule* that governs their lending mechanically permits **more** balance-sheet
expansion, and that expansion is disproportionately extended cross-border into higher-yielding EM
credit and portfolio flows. Tightening runs the identical mechanism in reverse, and reverses fast:
a dollar appreciation (or VIX spike) is not merely a price that EM borrowers passively suffer, it is
the **signal that triggers the deleveraging** in the lending institutions whose balance sheets fund
EM cross-border credit and portfolio positions in the first place — leverage of the *intermediary*,
not merely the price of the currency, is the transmission mechanism. **Avdjiev, Stefan; Bruno,
Valentina; Koch, Catherine & Shin, Hyun Song (2019), "The Dollar Exchange Rate as a Global Risk
Factor: Evidence from Investment,"** *IMF Economic Review* 67: 151–173 **[Verified — IMF Econ Rev
67:151-173]** extends this directly to the broad dollar index itself: a stronger dollar tightens the
effective credit conditions facing dollar-borrowing EM firms and banks (raising the implied
value-at-risk on dollar-denominated loan books, from the lender's own perspective), which is
precisely why the dollar enters L9's triad as a **risk-state variable in its own right**, not merely
as the flip side of a rate differential.

**(iii) The balance-sheet channel — Gabaix-Maggiori.** **Gabaix, Xavier & Maggiori, Matteo (2015),
"International Liquidity and Exchange Rate Dynamics,"** *Quarterly Journal of Economics* 130(3):
1369–1420 **[Verified — QJE 130(3):1369-1420]** formalizes why exchange rates themselves move on
intermediary balance-sheet capacity rather than purely on trade flows or textbook interest-rate
parity: in their model, financial intermediaries with limited risk-bearing capacity must be
compensated to absorb the imbalance between the supply of and demand for assets denominated in
different currencies, so a shift in *capital flows* — driven by anything that changes intermediaries'
willingness or ability to hold currency risk, including the Bruno-Shin leverage cycle itself — moves
the exchange rate directly, and moves it by more, and more persistently, when intermediary
risk-bearing capacity is itself constrained (precisely a VIX-spike, funding-stress environment).
This is the theoretical bridge between "global bank leverage falls" (Bruno-Shin's mechanism) and
"the rupee falls" (the observable India cares about): the exchange rate is not a passive residual of
trade and rate differentials, it is itself a **price set by constrained intermediaries**, which is
why INR sits inside L9's own indicator list rather than being treated as a downstream consequence
computed elsewhere.

**(iv) The convenience yield / safe-asset-shortage leg.** DFII10's inclusion (i above) has a second,
complementary justification beyond the taper-tantrum real-rate story: **Krishnamurthy, Arvind &
Vissing-Jorgensen, Annette (2012), "The Aggregate Demand for Treasury Debt,"** *Journal of Political
Economy* 120(2): 233–267 **[Verified — JPE 120(2):233-267]** document that US Treasury securities
carry a measurable **convenience yield** — investors accept a lower yield for the liquidity and
collateral value Treasuries uniquely provide, a "safe-asset shortage" premium that widens when
global demand for safety rises (risk-off episodes) and narrows when it falls. A widening convenience
yield is functionally a second face of the same VIX/dollar risk-off signature: global capital
seeking safety bids US real yields down (or, in acute stress, compresses the convenience-yield
component even as headline yields move on other forces) at precisely the moments EM assets are
being sold — the same episode, read from the safe-asset side rather than the leveraged-intermediary
side. This is not a separate ladder input; it is the theoretical reason DFII10 is read as a **risk
signal**, not a discount-rate input, inside L9's own construction.

**(v) Sudden stops — Calvo.** **Calvo, Guillermo A. (1998), "Capital Flows and Capital-Market
Crises: The Simple Economics of Sudden Stops,"** *Journal of Applied Economics* 1(1): 35–54
**[Verified — JAE 1(1):35-54]** names the acute end-state the triad is built to flag ahead of:
a **sudden, sharp reduction in international capital inflows** to an economy that had been running a
current-account deficit financed by exactly those inflows, severe enough to force an abrupt
current-account reversal — a real-side adjustment (import compression, output contraction), not
merely a portfolio-price event — precisely because the financing that had been sustaining the
deficit simply stops arriving. Calvo's own motivating cases (Mexico 1994–95, the 1997–98 Asian
crisis) share the structural feature every "Fragile Five"-style EM shares (A.3(iii) below): a
current-account deficit is not itself a crisis, but it is a **standing exposure to a capital-flow
sudden stop** whenever the global factor turns, and the size of that standing exposure is set by
domestic policy (the deficit's size, its financing mix, reserve buffers) even though the *timing* of
the stop is set by the global factor L9 reads.

**(vi) The taxonomy — Forbes-Warnock.** **Forbes, Kristin J. & Warnock, Francis E. (2012), "Capital
Flow Waves: Surges, Stops, Flight, and Retrenchment,"** *Journal of International Economics* 88(2):
235–251 **[Verified — JIE 88(2):235-251]** supply the vocabulary this program's own indicator list
(NSDL FPI) is built to classify episodes against: a **surge** is a sharp *increase* in gross
capital inflows (foreigners buying more); a **stop** is a sharp *decrease* in gross inflows
(foreigners buying less, not necessarily selling); **flight** is a sharp *increase* in gross
outflows (domestic residents moving capital out); **retrenchment** is a sharp *decrease* in gross
outflows (domestics repatriating). The distinction matters for L9's design because "FII selling"
in Indian financial-press usage conflates several of these — a genuine foreign sudden stop (an
inflow *stop*) reads very differently from domestic capital flight compounding it, and Forbes-
Warnock's own central empirical finding is that **global risk factors (their own VIX-adjacent
measure) are significantly associated with extreme episodes in all four categories**, but with
different strength and timing — directly corroborating Rey's global-factor claim from the flow side,
while giving the desk the taxonomy needed to read NSDL data correctly rather than treating every
net-outflow print as the same event.

**(vii) The EM policy menu, and the IMF's own evolving view of it.** Faced with a stop or a sudden
surge, an EM policymaker's toolkit is not merely "let the currency move" or "defend a peg" — the
binary the old trilemma implied. The modern menu spans **FX intervention** (spot and forward,
smoothing rather than defending a level), **macroprudential measures** (countercyclical capital
buffers, loan-to-value limits, external-borrowing norms), and **capital-flow management measures**
(CFMs — taxes, quantitative limits, or administrative measures on cross-border flows themselves).
The **IMF's own "Institutional View" on the liberalization and management of capital flows**,
adopted in 2012 and formally reviewed and updated in March 2022 **[Verified — IMF Institutional
View adopted 2012; Executive Board concluded its review 21 March 2022]**, itself evolved over this
window: the 2012 framework treated capital flows as a last-resort tool, permissible mainly during
acute surges or disruptive outflow episodes and never as a substitute for necessary macroeconomic
adjustment; the 2022 review — informed by the IMF's own Integrated Policy Framework research and an
Independent Evaluation Office assessment — more explicitly recognizes CFMs that are simultaneously
macroprudential in character (CFM/MPMs) as a standing part of the toolkit rather than a purely
exceptional one, a genuine loosening of the institutional orthodoxy since Rey's own 2013 paper was
first presented. **India's own toolkit specifically** spans all three menu items and has used each:
FX intervention via RBI's own reserve operations (A.3(ii) below); macroprudential and CFM tools
including External Commercial Borrowing (ECB) norms, FPI investment-limit ceilings on government
and corporate debt (a **captivity ceiling**, capping foreign ownership rather than mandating
domestic ownership — `docs/cycles/05-debt-supercycle.md`'s own figure has FPIs at roughly **3.3% of
outstanding G-sec stock as of May 2026** **[VERIFY — figure moves fast on flow data, already flagged
in its own source file]**), and — at the acute end, deployed exactly once in this program's own
evidence base — the emergency non-resident deposit swap window `docs/cycles/20-mp-cycle.md` (the
mp-cycle monograph) documents in full for 2013; this chapter does not re-derive that mechanism, only
notes that it exists as the toolkit's deepest instrument and that its 2013 deployment is the
canonical India illustration of the menu's outer edge.

**(viii) Why the exposure is "compensated and undiversifiable" — the honest limit of what L9 buys.**
The atlas's own phrasing is doing real work and deserves to be taken literally rather than read as a
rhetorical flourish: EM equities, India's included, carry a **structural, priced risk premium**
precisely because they are exposed to this common, undiversifiable global factor — an investor who
holds EM equity is *paid*, on average and over time, for bearing exposure to episodes like the ones
GF1–GF3 and the cases chapter document, in the same sense an investor in any systematically risky
asset class is paid for bearing a factor they cannot diversify away by holding more names within the
same asset class. This is the single most important thing L9 is honest about that a naive reading of
"hedge the global cycle" would miss: **you cannot hedge the global factor out of an India equity book
and keep earning India equity returns** — the risk premium and the exposure are the same object,
priced together, and a book that fully neutralized its global-factor loading would, by the same
stroke, give up the compensation for holding it. What L9 actually does, and all it claims to do, is
**condition the size of that exposure** — how much leverage, concentration, and hedge budget the book
runs — against the read state of the factor, larger when the state is calm, smaller when the triad
signals stress, never eliminating the loading itself. This is precisely why L9's decay assessment in
`ladder.yaml` reads `"compensated risk factor - none"`: unlike a crowdable anomaly, there is no
"decay" scenario to haircut for, because nobody arbitrages away a genuine risk premium by knowing
about it — the premium exists *because* the risk is real and undiversifiable, not despite investors
knowing the mechanism.

### A.3 India inside the cycle

**(i) FPI flow mechanics — the transfer's observable, and the caution that travels with it.** NSDL's
own daily/monthly aggregate FPI equity-and-debt flow data is the seat's primary India-side
observable, alongside quarterly shareholding-pattern filings for the float-scaled positioning read
L14 (Tier C, reduce-only) separately consumes. This chapter does not re-derive the finding
`docs/CYCLE_ATLAS.md` row 89 (2.13) and D08's own F8/I6 already establish in full: **flows follow
returns, not the reverse** — **Griffin, John M.; Nardari, Federico & Stulz, René M. (2004), "Are
Daily Cross-Border Equity Flows Pushed or Pulled?,"** *Review of Economics and Statistics* 86(3)
**[Verified via D08's own citation — cross-referenced here, not re-verified independently this
session]** find foreign equity flows across several markets respond to **past local returns**
(a "pulled," return-chasing pattern) more than they predict future returns; **Chakrabarti, Rajesh
(2001), "FII Flows to India: Nature and Causes,"** *Money & Finance* (ICRA Bulletin) **[VERIFY: exact
venue — D08 itself flags this with the same qualifier]** finds the identical direction on India's own
early FII-era data. The practical consequence, already the ladder's own design decision rather than
something this chapter re-argues: **FII flow *momentum*** — buying because trailing flows are
positive — has **no independent survival argument** and is explicitly excluded (`ladder.yaml
excluded: fii_flow_momentum`); what survives, and what L9's own algorithm consumes NSDL data for
(`partCDEFH.md` Part E, Step 4), is flows entering **as a confirming layer only**, read *after* the
triad's own dollar/VIX/real-rate state has already set the risk read — never as a leading input in
its own right. A desk that reverses this ordering — treating an FPI outflow print as the primary
signal rather than the triad's confirmation — is reintroducing the exact decayed, published pattern
the ladder already excluded once.

**(ii) INR as shock absorber versus reserves-defense episodes — RBI's revealed preference.** India's
own exchange-rate regime is neither a clean float nor a hard peg but a **managed float**: RBI
intervenes in spot and forward FX markets not to defend a target level (which the post-2016
inflation-targeting framework — already dated in this program's own fincycle-deep monograph, A.1iii
— does not commit to) but, in its own long-stated and widely
documented practice, to **smooth excess volatility** — leaning against disorderly moves in either
direction rather than resisting a trend. The revealed-preference pattern the atlas names (row 84,
"REGIME") shows up asymmetrically across the cycle's two phases: **during global-cycle surges** (the
factor calm, capital flowing in), RBI's own behavior is to **accumulate reserves** rather than let
the rupee appreciate freely — buying dollars, building the buffer that gets drawn down later — a
pattern visible in India's reserve trajectory building to multi-hundred-billion-dollar levels across
the 2020s, and echoed in the reserve-currency monograph's own finding (`docs/cycles/06-reserve-
currency.md`) that RBI's gold-and-FX reserve posture has itself shifted toward greater domestic
custody and diversification since 2022 as part of a broader reserve-management stance; **during
stops**, the same institution engages in **measured, resisted depreciation** — selling reserves and
using forwards to slow the rupee's fall, never attempting to hold a fixed level against a
determined global-factor move, and accepting a weaker rupee as the adjustment channel rather than
exhausting reserves defending an unsustainable one. This asymmetric pattern — buy aggressively in
calm, sell reluctantly and gradually in stress — is itself informative for the ladder: it means INR
alone, read without the reserve and forward-market context, **understates** the true stress state
during an acute episode, because RBI's own intervention is actively damping the observable exchange-
rate move the triad would otherwise register more sharply — one further reason the seat reads INR
alongside the dollar/VIX/DFII10 triad rather than treating INR's own move as a sufficient state
variable on its own.

**(iii) The 2013 taper tantrum and the "Fragile Five" anatomy — the canonical transfer event, global
side owned here.** On **22 May 2013**, then-Federal Reserve Chairman Ben Bernanke's congressional
testimony raised the possibility of tapering the Fed's asset-purchase program — a US **monetary-
policy-expectations** shock, the purest possible instance of Rey's own mechanism, transmitted
globally within weeks. The rupee depreciated roughly **28% between April and August 2013** (from
approximately ₹54 to a then-lifetime low of **₹68.85 on 28 August 2013**), and Nifty fell from an
intraday high near **5808.50 (1 August 2013)** to an intraday low of **5118.85 (28 August 2013)** —
a peak-to-trough decline of roughly **15–18%** (this program's own verification log confirms these
figures against the dossier's illustrative framing, `research/register/verification-log.md` §4).
Morgan Stanley currency analyst James Lord coined the term **"Fragile Five"** in an August 2013
research note grouping **Brazil, India, Indonesia, South Africa and Turkey** **[Verified — the
term's Morgan Stanley/James Lord origin and country membership are independently well documented]**
— the shared anatomy across all five being large **current-account deficits financed by portfolio
capital inflows**, elevated inflation, and comparatively thin reserve buffers relative to those
financing needs: precisely Calvo's (A.2v) sudden-stop precondition, present simultaneously in five
economies that had little in common **except** that standing exposure. The episode is the cleanest
available illustration of Rey's transmission mechanism operating on an emerging-market bloc that
shared no policy regime, no exchange-rate arrangement, and no direct trade linkage to one another —
only the shared vulnerability to a single global trigger. **This chapter's scope stops at the global
trigger and transmission mechanics** — the *rates*-side defense India itself mounted (the 15 July
2013 MSF corridor hike to an effective 10.25%, incoming Governor Rajan's 4 September 2013 FCNR(B)
swap window that raised roughly $34bn and is widely credited with moving India out of the Fragile
Five grouping by 2014) is `docs/cycles/20-mp-cycle.md`'s own, already-documented case (seat L6) and
is cross-referenced, not re-derived, here — the desk's own **standing rule against duplicating a
seat's own evidence base across monographs** applies exactly as it does for the macro-credit block's
shared budget (`fincycle-deep partA` §A.6).

**(iv) The May-2026 INR episode — the atlas's own live test case, verified.** `docs/CYCLE_ATLAS.md`
row 84 names this episode explicitly as L9's live test; this program's own verification log
(`research/register/verification-log.md` §4, sourced to **Bloomberg, "Rupee Plunge Sees India Turn
to 2013 Taper Tantrum Playbook: INR/USD," 22 May 2026**) confirms what actually happened, and it is
worth stating precisely because the episode's own shape is the chapter's best concrete illustration
of what L9 is and is not built to catch. The rupee fell to an intraday record low of **approximately
₹96.6–96.8/$ between 19–21 May 2026**, driven by three concurrent forces squarely inside this
chapter's own machinery: **Brent crude above $100/bbl** on US-Iran tensions (a Kilian-relevant
supply-side oil shock, feeding L9's own oil-decomposition leg — cross-ref `docs/cycles/14-commodity-
supercycle.md`, never re-derived here), **FPI outflows** running ahead of 2025's already-elevated
full-year pace (2025 full-year outflows near **$19bn**, with 2026 year-to-date already exceeding
that figure by the episode's peak), and **broad dollar strength** — precisely the triad's three legs
moving together, the literal Rey signature this chapter's own construction is built to register.
RBI (under Governor Sanjay Malhotra) was reported weighing an **FCNR(B)-style emergency NRI-deposit
scheme**, explicitly echoing the 2013 playbook A.3(iii) documents. **What is equally important, and
the reason this episode is instructive precisely by being unusual**: the equity impact was
comparatively mild — Nifty 50 shed roughly **4% over four acute sessions** and closed the month down
only **≈1.87%** (Sensex ≈−2.78%), and **India VIX rose only to ≈18.6**, nowhere near a fast-crisis
print (contrast March 2020's VIX path from the mid-20s through the 60s to the 80s). This is precisely
why `docs/DESIGN.md` §5.6 and this program's own episode detector (`partCDEFH.md`'s own cross-
reference to the module catalog) classify May-2026 as **non-qualifying for the equity-drawdown
machinery** but as the **designed live test case for L9 and the gold-INR mechanics** instead: the
episode's signature sat almost entirely in the currency and FPI-flow legs of the triad, not in
realized equity volatility, which is exactly the scenario a seat that reads the dollar/VIX/real-rate/
flow state **jointly**, rather than inferring global stress from equity vol alone, is built to catch
and a purely fast-stress (L2) or purely equity-vol-based system would have under-read. **What the
seat should have shown, stated as the honest design claim rather than a backtest not yet run on live
data**: a properly constructed L9 state — dollar-up, an FPI-outflow print running ahead of the prior
year's full pace, and a supply-side oil shock feeding the Kilian conditioner — should have registered
as an **armed, elevated risk state** through the currency/flow legs specifically, even while the VIX
leg itself stayed comparatively calm at ≈18.6, precisely demonstrating why the composite is built
from **all** the triad's legs jointly rather than any single one (a VIX-only design would have missed
most of this episode; a construction that reads dollar strength, FPI acceleration and the oil shock
together would not have). Confirming this design claim against the live NSDL/FRED data once vaulted
is exactly `partCDEFH.md`'s own pending design item **GF-D3** — logged there, not re-run here.

### A.4 What L9 does and refuses

**What L9 does.** Conditions India book size — leverage permission, concentration tolerance, hedge
budget — against a read of the dollar/VIX/US-real-rate risk state, inside its own dedicated **20%**
of regime-score budget, `reduce_only: false` (it moves the score in both directions, unlike the
Tier-C overlay). Consumes oil **only** through the **Kilian (2009) demand/supply decomposition**,
never a raw price level — a design choice this chapter inherits rather than re-derives
(`docs/cycles/14-commodity-supercycle.md`; D08 §F13/I11's own justification: a supply-driven oil
shock is an unambiguous cost/terms-of-trade hit for an 85%-import-dependent economy, while a demand-
driven shock partly self-hedges through the export/growth channel it accompanies — collapsing both
into one "oil up = bad" rule is exactly the magic-number-style oversimplification the Contract bans).
Runs its own episode τ½ at **3–9 months** — deliberately the ladder's **fastest** macro-block-adjacent
seat, faster than L6's 12–24 months or L10's 36–72 — because the object genuinely is an **episode**,
not an era: GF1's own finding (the factor's co-movement rose from +0.28 to +0.77 across 1990) is a
level-of-integration fact about the *world*, not a claim that any one episode of elevated stress
persists for years; episodes arrive, run their course over a matter of months, and resolve (via
policy response, a Fed pivot, or simple exhaustion of the shock), and a τ½ calibrated to years would
systematically lag the very events — 2013, May-2026 — the seat exists to catch.

**What L9 refuses.** **Forecasting the Fed** — the triad reads the *current* state of US policy,
risk appetite and real yields, never a forward call on the next FOMC decision or taper announcement;
G.3 below returns to why this refusal is load-bearing rather than merely modest. **Trading FPI flow
momentum** — the decayed, explicitly excluded pattern (A.3(i); `ladder.yaml excluded:
fii_flow_momentum`); flows enter only as a lagging confirmation of a state the triad has already set.
**Decoupling narratives** — "this time India is insulated from the global cycle," the recurring
sell-side product Part G below names directly; GF3's own 69% breadth finding is the *only* number
this program licenses in that direction, and it licenses a probabilistic, ex-post observation
("roughly two in three global-down-years are also India-down-years"), never an ex-ante assumption
that any specific *forthcoming* episode belongs to the insulated third. **Dollar-cycle or Fed-cycle
DATING** — atlas rows 2.9 (the ~7–10-year dollar cycle) and 2.10 (the 3–5-year Fed cycle) are folded
sub-faces of this same seat, explicitly listed in the atlas as living "inside L9," never separately
dated or forecast: the ladder's own discipline is to **state** the current triad reading, never to
call when the dollar cycle "should" turn or when the next Fed easing cycle "should" begin — the same
refusal that keeps every other long, phase-uncertain cycle on this ladder honest (Atlas §0's own
epistemics: persistence, not periodicity) applied here to the fastest seat on the macro side of the
ladder rather than only the slowest ones.

**The mechanism-to-seat synthesis.** Assembling A.1–A.4 into one table, mechanism by mechanism,
makes the honest gaps as visible as the confirmed content — exactly the discipline the fincycle-deep
style bar's own A.8 models, applied here to a seat built from five free series rather than two
price indices.

| Mechanism | Free observable consumed | How L9 uses it | What remains an honest gap |
|---|---|---|---|
| Dilemma-not-trilemma (A.1i, Rey) | None directly — the theoretical premise | Frames the seat's existence: no exchange-rate-regime escape clause is assumed anywhere else on the ladder | Whether India's own capital-account openness (the FPI debt-ceiling captivity structure, ECB norms) meaningfully dampens transfer relative to a fully open capital account — never isolated as its own test |
| Global factor's rise (A.1ii; GF1) | JST panel, annual real equity, pairwise corr | Standing caveat: pre-1990 analogue evidence is discounted wherever an old cross-country panel feeds an India claim elsewhere on this ladder | The exact modern variance-share point estimate for a broad risky-asset cross-section is a literature-consensus band (20–25%), not a figure this session pulled from the primary source `[VERIFY]` |
| India's transfer (GF2) | India MF (iima factors) vs. JST panel, 1994–2015 annual, n=22 | The `changes_if` condition ("India factor-loading estimate") is now partially served — the in-house +0.57 read | Only one annual-frequency estimation window has been run; the monthly-frequency loading with world-factor/oil/INR controls (design item **GF-D1**) is still open |
| Breadth ceiling (GF3) | JST panel, post-1950 global-down years | The only licensed insulation sentence (G.1 below) | Nothing yet distinguishes, ex ante, which future episodes fall inside the ~31% non-conforming share — by construction, this cannot be resolved before the fact |
| Leverage + balance-sheet channels (A.2ii–iii, Bruno-Shin/Gabaix-Maggiori) | FRED broad dollar index, VIX | Triad legs (a)–(b) | An India-specific estimate of how strongly FPI flows respond to intermediary-leverage shifts *specifically*, isolated from the pooled global estimate, has not been run |
| Convenience yield (A.2iv, Krishnamurthy-Vissing-Jorgensen) | FRED DFII10 | Triad leg (d), read as a risk signal, never a discount rate | No India-specific test of whether DFII10's risk-signal content differs across the pre-/post-2013-taper regime |
| Kilian oil decomposition (A.4) | Kilian's public index; Brent/WTI (FRED); PPAC import bill | Oil enters only via the demand/supply split; a raw-level-only call is structurally blocked (unit test, `partCDEFH.md` Part E) | An India-specific pass-through re-estimate post the 2022 discounted-Russian-crude regime shift — already flagged as open by D08 itself |
| Flows-follow-returns (A.3i, Griffin-Nardari-Stulz/Chakrabarti) | NSDL FPI (equity + debt) | Confirm-only, lagging layer — never a leading input | Whether the confirm layer's own incremental value *over the triad alone* has been measured is design item **GF-D2** (episode-catalog validation), pending |
| 2013 taper tantrum, global side (A.3iii) | Bloomberg/press chronology; this program's own verification log | The canonical illustration of Calvo's sudden-stop precondition binding an EM bloc sharing no policy regime | A quantified India-specific pass-through coefficient from the 2013 episode specifically — a verified qualitative case, no regression run |
| May-2026 episode (A.3iv) | Bloomberg, 22-May-2026; verification log | The atlas's own live test case; routed to L9 + gold-INR mechanics, explicitly not the equity-drawdown machinery | Design item **GF-D3** — the seat's own re-grade against live vaulted NSDL/FRED data for this specific window — has not yet run |

---

## PART G — Operator psychology

Part A documents a factor the desk cannot personally out-manage: the global cycle transmits through
center-country monetary policy and the leverage of institutions no India-based operator sits inside,
its transfer to India is real but bounded (GF2's +0.57, GF3's 69% ceiling), and its compensation is
inseparable from its risk — hedging it away costs the very premium the seat exists to let the book
keep collecting. That combination — a real, undiversifiable, *externally* triggered factor, arriving
on an irregular multi-year rhythm (GF-episode literature: roughly twice a decade, per the atlas's own
"irregular 5–10y episodes" framing) rather than a clock an operator can build calendar discipline
around — is exactly the setup that produces two opposite and equally costly failure modes: treating
a real, priced exposure as something a clever desk can diversify away, and treating a real, priced
exposure as something a clever narrative proves has stopped applying. This Part maps both, and the
subtler psychological traps around them, to the countermeasures Part A's construction already builds
in.

### G.1 The decoupling narrative's seduction

**Mechanism.** "This time India is different — insulated from the global cycle by its domestic
consumption story / its reform momentum / its demographic dividend / its digital-payments stack" is
one of the most durable products the India sell-side research complex generates, and it clusters
specifically at the moments the global factor's own state (per this chapter's own construction)
is **calm** — precisely when a genuinely diversifying, insulated-India thesis would be cheapest to
sell and hardest to disconfirm in the near term, and precisely the moment before the next episode
(by definition unpredictable in timing, per A.4's own refusal) tests it **[VERIFY: specific named
examples of pre-2013 "India decoupling" sell-side research — this session's search access did not
locate a citable, individually-named report matching the general and well-documented 2010–2012
"decoupling" commentary cycle that preceded the 2013 taper tantrum; the pattern itself — that
decoupling narratives proliferate during calm risk-appetite windows and are tested by the next
episode — is the atlas's and this program's own honest read, stated as a pattern rather than
attributed to any specific unverified source]**. The mechanism generating the narrative's
persistence is straightforward and does not require bad faith: during a genuinely calm risk-state
(the triad reading low across all three legs), India's *domestic* drivers — earnings growth,
consumption, reform execution — are, correctly, doing more of the work in returns than the global
factor is, which is a **true, verifiable, in-sample observation** at exactly the moment it gets
over-extrapolated into "the global factor no longer applies to India," a **different and unverified
claim** the calm period's own data cannot distinguish from the alternative (the global factor is
simply quiescent, not gone) until the next episode arrives and settles the question the hard way.
GF3's own honest 69%-versus-75% finding is the discipline against this specific temptation: it
proves partial insulation is **real, some of the time, ex post** — which is exactly the true
observation the decoupling narrative correctly starts from — while refusing to license the leap to
assuming **any specific future episode** falls into that minority, which is exactly the false step
the narrative makes next.

**Countermeasure.** GF3's own number is, in this program's own words (`partCDEFH.md` Part E's
failure-mode note), **"the ONLY licensed insulation sentence"**: the desk may say "roughly two in
three global-down-years are also India-down-years, so a meaningful minority of episodes see India
diverge" — a probabilistic, ex-post, honestly bounded statement — and may **never** say "India is
decoupled from this cycle" as a forward-looking design premise. L9's own budget allocation (20%,
`reduce_only: false`) is built to keep applying *before* any particular episode reveals which side
of the 69%/31% split it falls on, which is the structural point: the seat's permission never asks
the operator to first decide whether "this one" is a decoupling episode before conditioning size —
that decision is exactly the one no one can make reliably in advance, and the registry removes it
by never asking.

### G.2 Home bias inversions — foreign flows as validation-seeking

**Mechanism.** A related but distinct trap runs the opposite direction on *sentiment*, not on the
insulation claim itself: because India's own household and even much institutional capital carries
a strong home bias (the debt-supercycle and financial-cycle monographs' own G-sections document the
household-balance-sheet version of this for property and gold), a **sustained FPI inflow surge**
easily gets read, informally, as external validation — "foreign money agrees with the domestic
bull case" — precisely the moment A.3(i)'s own flows-follow-returns finding says the causality runs
the other way: the foreign flow is very often simply **chasing** the domestic rally that has already
happened, not independently confirming it. An operator primed by home bias to want external
validation of a domestically-generated conviction is exactly the audience least likely to
spontaneously apply Griffin-Nardari-Stulz's own finding in the moment it would matter — at the top
of a surge, not in a textbook aside.

**Countermeasure.** The ladder's own construction removes this temptation structurally rather than
relying on the operator to remember the causality direction under pressure: NSDL flow data enters
L9's algorithm **only as a lagging confirm of a state the triad has already set** (A.3(i);
`partCDEFH.md` Part E, Step 4), and flow *momentum* specifically is excluded outright
(`ladder.yaml excluded: fii_flow_momentum`) — there is no path by which a flow print, however framed
as validation, can independently move the regime score without the dollar/VIX/real-rate triad
having already moved first.

### G.3 The "Fed pivot" prediction industry

**Mechanism.** Because the global factor's dominant driver is US monetary policy and its
expectations (A.1(i)–(ii)), an entire market-commentary industry exists to forecast the **next** Fed
move — when the tightening cycle ends, when cuts begin, how many, how fast — and India-desk
commentary imports these calls wholesale as a timing input for EM risk-on/risk-off positioning. The
psychological pull is specific and understandable: a genuine Fed pivot is, empirically, one of the
most reliable episode-**ending** triggers the global cycle has (loosening the exact leverage
constraint Bruno-Shin's mechanism ties to Fed tightening), so correctly calling one early would be
genuinely valuable — which is exactly what makes the temptation to try so persistent, and exactly
why the industry forecasting it never goes away despite a mixed public track record of doing so
accurately.

**Countermeasure.** L9 is built to **read the current triad state**, never to forecast the Fed's
next move — A.4's own refusal, restated here as the psychological discipline rather than merely the
technical one: the seat's job is to have correctly registered elevated risk **once the triad
actually moves**, fast (τ½ 3–9 months, the ladder's quickest macro-adjacent seat), not to have called
the move in advance. An operator who successfully resists trading a Fed-pivot forecast personally
still benefits from the fast τ½ doing the pivot-detection job after the fact rather than before —
the seat is deliberately built to make the forecasting temptation unnecessary rather than merely
forbidden.

### G.4 Crisis-frequency asymmetry — the recency-decay trap

**Mechanism.** The atlas's own framing — "irregular 5–10y episodes" — means an India-focused
operator lives through a genuine global-cycle episode of the 2013 or May-2026 kind perhaps **twice
per decade**, an order of magnitude less often than the fast-stress layer's (L2) weekly-to-monthly
rhythm or even the credit cycle's own multi-year-but-still-more-frequent cadence. Low event
frequency is precisely the condition under which human risk perception decays fastest between
occurrences — each additional quiet year between episodes erodes the vividness of the last one and
narrows the operator's felt sense of the seat's relevance, right up until the next episode arrives
and (per G.1) gets read, in real time, as either a genuine surprise or as evidence the mechanism
itself no longer applies, rather than as the un-timed but entirely expected member of an irregular-
but-real class of events.

**Countermeasure.** The registry-level fix is the same one the ladder applies to every long-clock
phenomenon: L9's 20% budget is a **standing allocation**, not a discretionary one the operator must
remember to re-activate before each episode — it is drawn continuously from the regime-score
construction regardless of how recently the last episode ran, so a multi-year quiet stretch cannot
silently zero out the seat's influence through simple inattention. The desk's own practice discipline
this chapter recommends alongside the structural fix: treat the **cases chapter's own nine-episode
chronology** (1994–2026, per `partCDEFH.md` Part H) as the operator's substitute for lived experience
— reviewing it periodically is the cheapest available countermeasure to an event frequency too low
for memory alone to keep calibrated.

### G.5 The desk's two symmetric traps

**Over-hedging the compensated factor away.** A.2(viii)'s own honest framing is also this Part's
sharpest psychological warning: because the global factor is *visible*, *nameable*, and *discussed
constantly* in market commentary, it is an unusually tempting target for a desk wanting to feel it
has "done something" about a risk everyone is talking about — buying protection specifically against
dollar strength or VIX spikes, sized against the *headline* rather than against the budget the
registry actually allows. Doing so at scale destroys exactly the risk premium the book is paid to
hold (A.2(viii)): an India book that fully neutralizes its global-factor loading has, by construction,
given up the compensation for bearing an undiversifiable risk, converting a *priced* exposure into an
*unpriced hedging cost* for no offsetting benefit, since the premium and the exposure are the same
object. **Countermeasure**: the hedge ratio is a swept config parameter jointly with the regime that
selects it (Contract §3) — L9's own reading conditions *how much* permission the book has, inside a
capped 20% budget, never an instruction to hedge the factor to zero regardless of state.

**Under-weighting the factor in euphorias.** The mirror-image trap, and the one G.1's decoupling
narrative directly enables: in a calm-triad, strong-domestic-narrative window, the temptation is to
treat L9's own quiet reading as *permission to forget the seat exists* — running leverage and
concentration as though the 20%-budget global-cycle seat were zero-weighted rather than merely
currently-calm, precisely the setup GF1's own finding (post-1990 co-movement of +0.77) says should
worry a desk most, because the world the seat operates in is **more**, not less, globally integrated
than it was before 1990. **Countermeasure**: the seat's `reduce_only: false` status means it can and
does add to the regime score when the triad is genuinely calm — the desk is meant to run *more*
freely in a low reading, never to treat "L9 currently reads low" as equivalent to "L9 no longer
matters" — the distinction G.1 already names as the decoupling trap's own root confusion, restated
here as a portfolio-construction discipline rather than a narrative one.

### G.6 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| "This time India is decoupled" — reading a calm-window domestic narrative as proof the global factor no longer applies | Decoupling commentary clusters in calm risk-state windows precisely because domestic drivers correctly dominate returns then — a true observation over-extrapolated into a false forward claim; GF3's own 69% breadth finding shows partial insulation is real ex post, never assumable ex ante | GF3's number is the ONLY licensed insulation sentence (probabilistic, ex post); L9's 20% budget applies continuously, never conditioned on first classifying an episode as "decoupled" or not |
| Reading a foreign-inflow surge as external validation of a domestic bull case | Home bias primes the operator to want validation exactly where Griffin-Nardari-Stulz/Chakrabarti say the causality runs backward (flows follow returns, not the reverse) | NSDL flow data enters L9 only as a lagging confirm; flow momentum excluded outright (`ladder.yaml`) — no path for a flow print to move regime score independently |
| Trading a personal or imported "Fed pivot" call | The pivot is genuinely one of the cycle's most reliable episode-enders, making the temptation to forecast it early persistently attractive despite a mixed track record | L9 reads the CURRENT triad state at a fast τ½ (3-9m); never a forward Fed call — the fast read substitutes for the forecast rather than requiring the operator to resist making one |
| Losing the seat's salience between episodes (recency decay) | Genuine global-cycle episodes hit India roughly twice a decade — an unusually low frequency for a live regime input, well below the fast-stress or even credit-cycle cadence | Standing 20% budget applies continuously regardless of how long since the last episode; periodic review of the cases chapter's own nine-episode chronology substitutes for lived memory |
| Over-hedging the factor to zero because it is visible and widely discussed | The factor's public salience makes it a tempting target for headline-sized protection, but the premium and the exposure are the same object — full neutralization destroys the compensation the book is paid to hold | Hedge ratio is a swept parameter jointly with the selecting regime (Contract §3), capped inside the 20% budget — never an instruction to zero the loading regardless of state |
| Treating a calm L9 reading as "the seat doesn't matter right now" and running leverage as though global-cycle risk were absent | GF1's own finding — post-1990 co-movement nearly tripled (+0.28→+0.77) — means the world is MORE globally integrated than before, not less; a calm reading is a favorable state, not an absent one | `reduce_only: false`: L9 both adds and subtracts regime score; a low reading licenses MORE permission, it never licenses forgetting the seat exists |
| Confusing the 2013/May-2026 episodes' RATES-side defense with this seat's own claim | The mp-cycle monograph's own L6 case (MSF hike, FCNR(B) window) is a distinct, already-documented seat; conflating it with L9 double-counts one mechanism as two | L9 stays scoped to the GLOBAL trigger and transmission (dollar/VIX/real-rate/flows); the domestic rates defense is cross-referenced, never re-derived, exactly as the macro-credit block's own de-duplication rule requires elsewhere on the ladder |

None of these seven countermeasures asks the operator to be wiser under pressure than Part A's own
evidence already justifies. Each converts a live judgment call — decide whether this quiet window is
finally the one where India really has decoupled, decide whether this inflow surge really does
validate the domestic thesis, decide whether to call the Fed's next move, decide whether a two-per-
decade risk still deserves this year's attention, decide whether visible risk deserves a bigger hedge
than the budget allows, decide whether a calm reading means the seat can be ignored, decide whether
the global and domestic sides of one episode are one seat or two — into a structural non-decision,
made once, in the registry, before the moment that would have made it hardest.

---

**Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)**
**Date: 2026-09-02 · v1.0**
