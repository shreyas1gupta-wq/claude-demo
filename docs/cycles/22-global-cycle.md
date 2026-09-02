# The Global Financial Cycle — Full Monograph (Atlas 2.8, seat L9)

**Version 1.0 · 2026-09-02 · Ionic quant desk (principal: gaurav@ionic.in) · governed by research/CONTRACT.md**

**Verdict up front:** L9 confirmed at its seat (global_cycle block, 0.20; episode τ½ 3-9m —
the ladder's fastest macro seat) with its transfer premise now measured in-house, one bar
failed productively, and its named live exam graded honestly.

**Headline results (trials GF1–GF3, pre-registered):**
- **GF1 PASS — the register's cleanest regime change:** median pairwise co-movement of national
  equity markets +0.28 (1900-1989) → +0.77 (1990-2015). STANDING CAVEAT born: pre-1990
  analogue evidence discounts on transfer to today's India.
- **GF2 PASS:** India loads +0.57 on the global equal-weight factor (1994-2015) — the L9
  transfer premise, measured (partially serving the seat's changes_if).
- **GF3 FAIL (69% vs 75%):** global downs pull ~2/3 of countries, not ≥3/4 — the licensed
  sentence is "one cycle, most places, most of the time"; partial insulation is real ex post,
  never assumable ex ante.

**The live exam (May-2026 INR episode, the atlas's own test case):** verified against the
log's Bloomberg record and the case chapter's search pass — USD/INR record ~96.8 (19-21 May
2026), driven by the tariff overhang, CY2026 FPI outflows and a Hormuz oil spike — a
CURRENCY/RATES crisis, and the triad was QUIET going in: an honest finding that L9's classic
global-risk signature does not cover tariff/oil-idiosyncratic INR events (routed to L9's oil
conditioner + the gold-INR mechanics, and to design GF-D3 for the data-vaulted re-grade).

**Assembled from:** partA-theory-psychology.md · partB-cases.md · global-RESULTS.md ·
partCDEFH.md.

---

# PART A + G — Theory (Rey, the triad's machinery, India inside the cycle) and operator psychology

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

---

# PART B — Nine episodes, 1994-2026, and the growing transfer

# PART B — The global-episode case record: nine transfers, one factor

*Global-financial-cycle monograph (atlas 2.8; ladder seat `L9_global_financial_cycle`,
`config/ladder.yaml`, Tier B, episode `tau_half` 3–9 months) · Part B · v1.0 · 2026-09-02 · Author:
Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. This Part reads `docs/CYCLE_ATLAS.md` row 2.8 ("Rey: one global
factor — VIX/dollar/US policy — drives EM flows regardless of exchange-rate regime... a
compensated, undiversifiable exposure for India, not an anomaly that decays"), `config/ladder.yaml`'s
`L9_global_financial_cycle` entry, and this directory's own `global-RESULTS.md` (the desk's
pre-registered GF1–GF3 trials, cited directly throughout, never recomputed) and `partCDEFH.md`
(the seat's data engineering, mathematics, algorithm, harvest map and knowledge ledger — cited by
name for every design/measurement question, never re-derived here). **Scope, stated once and held
throughout: this Part owns the GLOBAL-EPISODE anatomy** (the trigger, the VIX/dollar/US-rate triad's
direction, the breadth of the EM-wide flow event) **and India's specific transfer** (FPI flows, the
INR path, the equity drawdown) **in each of nine episodes, 1994–2026** — not the domestic policy
mechanics several of these episodes also carry, which belong to sibling chapters and are cross-
referenced by name, never re-derived: `research/cycles/mpcycle-deep/partB-cases.md` episode 4 owns
the 2013 rates defense (the MSF corridor inversion, the FCNR(B) swap) in full; `research/cycles/
shadow-deep/partB-cases.md` owns the 2013 NBFC-side negative control (§B5) and the 2018 IL&FS
funding-run anatomy (§B2) in full; `docs/cycles/06-reserve-currency.md` owns the dollar-system frame
— the four-role split, the network-inertia argument, and the swap-line hierarchy this Part borrows
for the 2008 and 2020 episodes below. This Part carries no theory of its own beyond what grounds
each episode's dating; the formal Rey / Miranda-Agrippino-Rey argument lives in dossier 08 (§F3–F4)
and this seat's own sibling theory chapter, cited, not restated. Style follows `research/cycles/
fincycle-deep/partB-cases.md` (numbers-forward, every figure sourced, `[VERIFY]` where a search pass
could not pin the primary series).*

---

## B0. The empirical anchor, before the cases

`global-RESULTS.md`'s three pre-registered trials (GF1–GF3) are the numbers every episode below is
read against, so they are stated once, up front, rather than re-argued nine times. **GF1** (the
factor's rise): median pairwise correlation of annual real equity returns across the 16-country JST
panel was **+0.28 pre-1990** and **+0.77 post-1990** — a **+0.49** jump against a **+0.10** bar,
**PASS**. This is the cleanest regime change in the desk's own register: the "global financial cycle"
Rey names is not a constant feature of markets, it is a **post-1990s phenomenon** — capital-account
liberalization across the developing world (India's own 1991–93 opening among the more consequential
single cases) is the plausible mechanism, and every pre-1990 analogue in the literature carries a
standing discount for exactly this reason. **GF2** (India's loading): the correlation between India's
annual compounded market-factor return and the equal-weight JST-panel mean, 1994–2015 (n=22), is
**+0.57** against a **+0.30** bar, **PASS** — India is measurably, not marginally, inside the global
factor once its own capital account opened, the seat's own transfer premise confirmed on the desk's
first in-house estimate. **GF3** (breadth): in the 18 post-1950 years where the pooled JST mean real
return was negative, the median share of countries individually negative was **69%**, against a
**≥75%** bar — **FAIL**. This is the number this Part is licensed to say about insulation, and the
only one: partial insulation from a global down-year **exists, ex post, roughly three years in ten**,
but a design that assumed it **ex ante** — that some country, in some down-year, would decouple by
default — would be fitting a coin-flip. `partCDEFH.md` calls this "the licensed insulation sentence,"
and every episode-level insulation claim below is disciplined against it explicitly, never asserted
free of it.

The mechanism itself, briefly, because every case below reads three legs jointly rather than any
one alone: Rey's (2013) "dilemma not trilemma" argument and Miranda-Agrippino & Rey's (2020)
dynamic-factor extraction both find a single global factor — proxied by the VIX (risk appetite), the
broad dollar (funding conditions), and US policy/real rates (the push variable) — driving cross-
border bank and portfolio flows into and out of the entire developing world essentially regardless of
a receiving country's own exchange-rate regime. The three legs do **not** always move together, and
several episodes below are precisely the cases where they diverge — the design reason `partCDEFH.md`
Part D builds L9 as a joint percentile of all three, never a single-leg proxy.

A comparability note before the cases, stated once rather than repeated nine times: the nine episodes
below are not nine draws from an identical process. GF1's own regime-change finding means the
pre-1990 episode (§B1) sits on one side of a structural break the remaining eight sit on the other
side of, and even among the post-1990 eight, India's own capital-account depth changed materially
between 1997 and 2008 and again between 2008 and 2013 — so a rising India-transfer magnitude across
this record's chronology is only partly a statement about the global factor's own behavior; it is
also, and inseparably, a statement about how much of India's financial system there was for the
factor to move. This is precisely why GF2's own transfer-coefficient estimate (+0.57) is dated
1994–2015 rather than assumed constant back to 1991, and why this Part reads each episode's India
transfer against the capital-account-openness baseline the episode itself sat inside, not against a
single time-invariant "India's sensitivity to the global cycle" constant.

---

## B1. 1994 — the Tequila/Fed shock: the baseline before the transfer existed

**The trigger and the triad.** Led by Chairman Alan Greenspan, the FOMC raised the federal funds rate
from **3.00% (Feb 1994) to 6.00% (Feb 1995)** — a doubling in twelve months, the fastest tightening of
the Volcker-Greenspan era to that point — driving the 10-year Treasury yield from **5.4% to 7.8%**, a
**240bp** move dubbed the "Great Bond Massacre," with paper losses on global bond portfolios estimated
above **$1 trillion**. **[Verified.]** On **20 December 1994**, the newly inaugurated Zedillo
administration devalued the Mexican peso roughly **15%**, unleashing the "Tequila Crisis"; Mexico's
economy contracted **5.9%** in 1995. **[Verified.]** This is the purest **rates-led** episode in the
entire record — the VIX index itself was only newly introduced (1993, on the older VXO methodology)
and no reliable, continuously-published India-relevant reading exists this early `[VERIFY: a usable
1994 VIX/VXO level — not independently located this pass]`; the transmission channel here is the
classic Calvo–Reinhart–Leiderman "push factor" — a US rate shock reversing capital that had flowed to
Latin America and other emerging markets during the preceding easy-money years — not a VIX-led
risk-off wave.

**The EM-wide flow event.** Contagion spread from Mexico through Argentina, Brazil, and other Latin
American markets within weeks (the "Tequila effect"); emerging-market bond spreads — the asset class
whose modern benchmark indices were only then being assembled — widened sharply across the region.

**India's transfer — the baseline for what GREW.** India's own capital account had barely begun to
open: FII registration started **September 1992**, and net portfolio investment into India rose from
**$4 million in FY1991–92 to $3,824 million in FY1994–95** — continuing to *grow* straight through the
Tequila window, not reversing. **[Verified.]** FII net investment stood at **₹2,595 crore in 1993**,
with monthly net inflows rising from **$0.18 million (Jan 1993) to roughly $400 million within a
year**. **[Verified.]** The rupee, unified onto a market-determined rate in March 1993, traded in the
low-to-mid ₹30s through 1994–95 with no Tequila-scale depreciation event `[VERIFY: a precise
1994–95 INR daily series — not independently pinned this pass]`. This is not resilience earned by
policy skill; it is **structural absence of the transfer mechanism itself** — a capital account too
thin for foreign positioning to move INR or Indian equities at the scale a "transfer" implies. The
seat's own FPI/NSDL-style indicator family (`config/ladder.yaml`'s `L9` inputs) has, for India
specifically, no meaningful observations this early: there was not yet enough foreign capital in the
system for a global-cycle episode to register a domestic footprint.

**The FII-entry framework itself, briefly, because it is the whole reason the transfer was absent.**
SEBI's September 1992 guidelines opened Indian equity and debt markets to registered foreign
institutional investors for the first time, but under a deliberately staged design: FII investment was
capped per company (initially in the single-digit percentage range of paid-up capity, raised only
gradually over the following decade), routed through a small number of registered custodians, and
denominated overwhelmingly in equity rather than debt — India had, in effect, built a narrow, metered
valve rather than an open capital account, precisely the "gradualist" sequencing later cross-country
literature (Kaminsky-Schmukler, among others) would credit with reducing hot-money vulnerability
relative to the Latin American economies Mexico's own crisis exposed. **Policy response.** None
specific to the Tequila episode itself; India's own 1991–93 reform program (fiscal consolidation,
current-account discipline, the phased FII-entry framework above) was already the standing policy, not
a reactive defense mounted *because of* this episode.

**Episode length.** The EM-wide acute window ran roughly **December 1994 to mid-1995** (a US-led $50
billion Mexico rescue package assembled by January 1995); India's own window is best described as a
**non-event** — no distinct domestic drawdown or currency-defense episode is dateable against this
trigger.

**What L9's state would have read.** Nothing — and that is the finding. A seat built to read India's
transfer through FPI flows, INR, and equity drawdown has no usable domestic signal to read in 1994
because the transfer channel had not yet been built by policy; L9's own construction (`partCDEFH.md`
Part E) would show an episode-armed flag on the global triad's US-rate leg alone, with zero
corresponding India-side confirmation — the cleanest illustration in this record of GF1's own finding
that the global factor's *rise* (median pairwise correlation +0.28 pre-1990, the years immediately
surrounding this episode) had not yet reached the amplitude the post-1990s panel would show.

---

## B2. 1997–98 — the Asian crisis, LTCM/Russia, and the Pokhran overlay

**The trigger and the triad.** Thailand floated the baht on **2 July 1997**, the conventional start
date of the Asian financial crisis; contagion spread through Indonesia, Korea, Malaysia, and the
Philippines over the following year, with regional currencies falling **30–80%** (the Thai baht
roughly **−40%**, the Indonesian rupiah as much as **−80%**, the Korean won near **−50%**)
`[VERIFY: precise peak-to-trough figures by currency — order-of-magnitude widely corroborated, exact
percentages not independently re-derived this pass]` and regional equity markets falling **50–75%**.
A second leg arrived thirteen months later: Russia devalued the rouble and defaulted on GKO debt in
**August 1998**, and the hedge fund Long-Term Capital Management collapsed in **September 1998**,
requiring a **$3.6 billion** Fed-orchestrated private-sector bailout. **[Verified — the broad
chronology and LTCM bailout scale.]** The triad here is instructive precisely because its three legs
did **not** move in one direction: the VIX/VXO spiked sharply around both the October 1997 Asian
sell-off and the August–October 1998 LTCM/Russia window `[VERIFY: precise 1997–98 VIX/VXO levels]`,
and the broad dollar strengthened on safe-haven flows throughout — but the Fed **eased**, not
tightened, cutting the funds rate **25bp three times, September–November 1998**, an explicit
crisis-insurance response to the Russia/LTCM contagion. A tightening-triggered episode (VIX up,
dollar up) paired with an **easing** US rate leg is a genuinely different triad signature from every
other case in this record, and the common factor uniting it is risk appetite and dollar funding
conditions, not the US policy-rate direction Rey's baseline framing emphasizes.

**The EM-wide flow event.** The 1997–98 window is the sudden-stop taxonomy's founding case: currency
board and pegged-regime economies across Asia broke in sequence, each break widening regional risk
premia and triggering the next — Thailand's own float forcing Indonesia's a month later, then
Korea's by year-end, each devaluation making the next country's own peg look less defensible to the
same pool of international capital rather than more, a genuinely contagious mechanism rather than
nine independent country shocks. The LTCM episode a year later added a second, structurally distinct
lesson this record's own reserve-currency monograph (`docs/cycles/06-reserve-currency.md`) touches
from the other direction: the Fed's willingness to orchestrate a **private-sector** ($3.6bn,
no public money) rescue of a single hedge fund, on the stated ground that its unwind risked the
entire dollar-funding system, is an early instance of the same asymmetric-backstop logic behind the
swap-line hierarchy this Part documents formally from 2008 onward (§B3, §B7) — a preview, in 1998, of
who gets treated as systemically consequential to the dollar system and who does not.

**India's transfer — the counterfactual for what openness later cost/bought.** India's own capital
account remained substantially closed (the rupee non-convertible on the capital account, FII/NRI the
only open channels), and RBI mounted an explicit exchange-rate defense: **Bank Rate raised 9%→11%
effective 17 January 1998**, alongside a 1-point CRR hike and a short-dated repo-style instrument
pushed to 9% (full mechanics cross-referenced, not re-derived, in `mpcycle-deep/partB-cases.md` case
1) — the rupee stabilizing near **₹38.9/USD** by late January 1998 and a **₹39.5** band by March 1998.
**[Verified, per the mp-cycle monograph's own citation.]** Layered on top, **India tested nuclear
devices at Pokhran on 11 and 13 May 1998**, triggering US and other Western sanctions — a
country-specific geopolitical shock with no counterpart anywhere else in this nine-episode record,
arriving in the *middle* of the regional contagion window. Contemporary accounts of the resulting FX
pressure carry two different windows and magnitudes that this pass could not fully reconcile: RBI's
own retrospective describes an **18% permitted depreciation** across the crisis broadly, while a
separate academic account puts the rupee's own **13.1% fall specifically between April and September
1998**, trading **₹42.25–42.38/USD** by period's end `[VERIFY: reconciling the two cited windows —
both are sourced, the gap plausibly reflects different start/end dates rather than a contradiction]`.
Equity: Indian markets fell through 1998 on the combined Asian-contagion/Pokhran-sanctions overlay,
though a precise, independently-verified Sensex peak-to-trough figure for this specific window could
not be pinned this pass `[VERIFY: 1998 Sensex/Nifty drawdown magnitude]`.

India's own relative standing inside the region is worth stating plainly rather than left implicit:
against Thailand, Indonesia, and Korea's 30–80% currency collapses and IMF-programme entries, India
required no IMF assistance, no currency-board abandonment (it had none), and no banking-system
recapitalization on the scale the region's own crisis economies needed — the counterfactual the task
names is precisely this gap between a ~10–18% managed depreciation inside a still-largely-closed
capital account and a 50–80% collapse inside a fully open one, the two ends of the same spectrum
this record's later episodes (2008, 2013, 2018) show India moving steadily toward as its own capital
account opened further.

**Policy response.** The Bank Rate/CRR defense above (cross-ref `mpcycle-deep` case 1, not
re-derived); the capital-account closedness itself — an unconvertible rupee — was the standing
structural policy already in place, not a reaction to this specific episode.

**Episode length.** The regional Asian crisis ran **July 1997 to roughly mid-1999** (~2 years);
India's own acute window, bookended by the January 1998 rate defense and the May 1998 Pokhran
sanctions, is best dated **January–October 1998** (~9–10 months).

**What L9's state would have read.** A closed capital account meant the transfer showed up almost
entirely through the **rates/FX defense channel** (RBI's own Bank Rate move) rather than through a
foreign-flow-driven equity crash — the partial-insulation counterfactual the task names, and the
direct predecessor of GF3's own ex-post finding. But L9 alone, reading only VIX/dollar/US-rates,
would have **under-read** India's own 1998 stress: a meaningful share of the year's pressure was
sanctions-driven (Pokhran), a country-specific shock with no representation in any of the triad's
three legs — the clearest episode in this record for the general design lesson that a global-cycle
seat must be read jointly with country-specific state variables, never as a complete account of a
given year's India-specific stress on its own.

---

## B3. 2008–09 — the full transfer arrives

**The trigger and the triad.** Lehman Brothers filed for bankruptcy on **15 September 2008**
(full domestic-policy chronology cross-referenced, not re-derived, in `mpcycle-deep/partB-cases.md`
case 3), triggering a global dollar-funding freeze. The VIX reached an **all-time intraday high of
89.53 on 24 October 2008**, an end-of-month peak of **59.89 (October)**, and a daily peak of
**80.86 on 20 November 2008**. **[Verified.]** The broad dollar rallied sharply through the panic — a
classic "dash for dollars" even though the crisis originated in the US itself — while the Fed cut the
funds rate from **2.00% (Apr 2008) to the 0–0.25% zero bound (Dec 2008)**, the fastest arrival at the
zero lower bound in the modern record.

**The EM-wide flow event and the swap-line hierarchy.** On **29 October 2008**, the Federal Reserve
extended **$30 billion** temporary swap lines each to **Brazil, Mexico, Korea, and Singapore** —
alongside the five standing advanced-economy lines (Canada, UK, ECB, Japan, Switzerland) — explicitly
to backstop dollar liquidity in "systemically important" emerging markets. **[Verified.]** **India was
not among the recipients**, in either the standing five or the emerging four. This is the hierarchy
lesson the task names, and `docs/cycles/06-reserve-currency.md`'s own four-role framework (A.1) is the
direct grounding: dollar-funding-backstop access in a crisis extends along alliance/systemic-importance
lines the reserve-currency monograph documents as a distinct "funding currency" role, not universally —
India, without a swap line, had to self-insure through its own reserve stock rather than access one.

**India's transfer — the full arrival.** FIIs withdrew an estimated **$13 billion** from Indian
equities in calendar 2008, a cumulative **~$15.4 billion** outflow across **January 2008–March 2009**.
**[Verified, both figures, though the calendar-year vs. cumulative-window framing differs by
source.]** The rupee fell from a **2007 high near ₹39.27/USD** to **₹40.4 (end-March 2008)**, crossed
**₹50.1 on 27 October 2008**, and touched a low of **₹52.1 on 5 March 2009** — a fiscal-year (FY09)
depreciation of **21.9%**. **[Verified.]** Equity: Nifty fell from its **8 January 2008** intraday
high (**~6,357**) to a **27 October 2008** low (**~2,252**) — a decline on the order of **60–65%**
`[VERIFY: exact index levels/dates — this pass's search returned inconsistent secondary figures for
the precise peak/trough; the ~60–65% magnitude is the widely-cited order and is independently
corroborated by the recovery figure below]`. The subsequent reversal is the cleanest confirmation of
the trough level: FIIs poured **$60.31 billion** into Indian equities from **March 2009 to November
2010**, lifting the Nifty from **around 2,500 to 6,300** — the "2009 V" this record's own mp-cycle
monograph (case 3) independently dates from the domestic-policy side.

**A second transmission channel worth naming, beyond portfolio flows.** Indian corporates that had
borrowed abroad through External Commercial Borrowings (ECBs) and Foreign Currency Convertible Bonds
(FCCBs) during the 2003–08 boom (the same credit-and-capex expansion `research/cycles/capex-deep/` and
the fincycle monograph's own India case document from the domestic side) found the global dollar-
funding freeze closing that market simultaneously with the FII equity exodus — a second, corporate-
balance-sheet leg of the same global-cycle transfer, layered on top of the portfolio-flow leg this
Part's own table tracks, and a direct structural precursor to the "twin balance sheet" problem
(`research/cycles/credit-deep/partB-cross-country.md` case #10) that would surface fully only years
later as some of this same external debt proved harder to refinance or repay than boom-era
underwriting assumed `[VERIFY: a precise 2008–09 India ECB/FCCB refinancing-stress figure — not
independently located this pass; flagged as a plausible, not fully evidenced, second channel]`.

**Policy response.** RBI's crisis easing (repo 9.00%→4.75%, CRR 9%→5%, SLR 25%→24%, all within months)
is cross-referenced in full to `mpcycle-deep/partB-cases.md` case 3, not re-derived here; on the
external side, India's own reserve stock (in excess of **$300 billion** at the time
`[VERIFY: precise late-2008 figure]`) was the self-insurance instrument in place of a swap line.

**Episode length.** The acute global window ran **September 2008–March 2009** (~7 months); India's
own drawdown-to-new-high arc ran considerably longer, **January 2008 (peak) to November 2010 (new
highs)** — the deepest and, on a peak-to-recovery basis, one of the longest episodes in this record.

**What L9's state would have read.** Every leg of the triad moved in the textbook direction
simultaneously — VIX to an all-time high, dollar sharply up, US rates to zero — the single cleanest,
most unambiguous "episode armed" reading in the entire nine-case record. The swap-line exclusion is
the first of two identical instances in this record (the second is 2020, §B7 below): a systemically
important, but non-allied-in-the-narrow-sense, emerging market self-insures through reserves rather
than a Fed backstop — a structural fact about the dollar system, not a policy failure, and one L9's
own construction cannot see directly (the seat reads VIX/dollar/rates, not swap-line access), which is
exactly why the reserve-currency monograph's own four-role hierarchy is the right cross-reference for
interpreting *why* the transfer landed on India's reserves and currency rather than on a backstop
facility.

---

## B4. 2013 — the taper tantrum, India at double length

**The GLOBAL anatomy.** In Congressional testimony on **22 May 2013**, Fed Chairman Ben Bernanke
signaled that the pace of quantitative-easing bond purchases could soon be reduced — the "taper"
that gave the episode its name. **[Verified.]** The reaction was concentrated in the rates leg of the
triad: the 10-year Treasury yield rose sharply over the following months (from roughly the low-2%
area toward 3% by September 2013) `[VERIFY: precise daily 10Y path]`, while the VIX itself stayed
comparatively unremarkable through most of the window — a taper tantrum was, distinctively among this
record's nine episodes, a **rates-and-dollar-led, not VIX-led**, event `[VERIFY: precise 2013 VIX
levels — recalled as staying mostly below 20 even through the acute FX-stress weeks, a materially
lower reading than 2008/2015/2018/2020]`. Morgan Stanley coined the **"Fragile Five"** — Brazil,
India, Indonesia, South Africa, and Turkey — grouping them by the shared vulnerability of financing
sizable current-account deficits with foreign capital inflows against comparatively thin reserves.
**[Verified.]**

**India's summer, cross-referenced not re-derived.** The domestic rates-defense mechanics — the
**15 July 2013** Marginal Standing Facility hike to an effective **10.25%** (300bp above the 7.25%
repo rate), and the **FCNR(B) swap window** launched under incoming Governor Raghuram Rajan
(from 4 September 2013) that mobilized roughly **$26 billion** directly and contributed to a
**$34 billion** aggregate raised September–November 2013 — are `mpcycle-deep/partB-cases.md` case 4's
own subject in full; the NBFC-side negative control (why the funding-cost spike here shows **no**
credit-quality event, unlike 2018) is `shadow-deep/partB-cases.md` §B5's own subject in full; neither
is re-derived here. This Part's own contribution is the **global-episode** framing around those
domestic facts: the rupee fell from roughly **₹55 to a lifetime low of ₹68.85 on 28 August 2013** — a
**~28% depreciation, April–August 2013** — the FPI debt-outflow scale that forced it running to
several billion dollars over the acute window `[VERIFY: a precise FPI-debt-outflow figure for the
Apr–Aug 2013 window specifically — not independently pinned this pass]`.

**What distinguished the recoverers.** India and Indonesia stabilized in the shortest time among the
Fragile Five — roughly **seven months** — through a combination of the rates defense, the FCNR(B)
swap, and a subsequent narrowing of the current-account deficit; **India exited the "Fragile Five"
grouping** within roughly a year of the shock. **[Verified.]**

**Episode length.** The global episode ran **May 2013 (Bernanke testimony) to the Fed's actual taper
announcement in December 2013**; India's own acute window ran **April–September 2013** (~5–6 months),
with full stabilization by roughly **January 2014** (~7 months from onset, consistent with the
cited recovery figure).

**What L9's state would have read.** This is the second episode (after 1997–98) where the triad's
three legs moved with **markedly different amplitudes** — dollar and US-rates loud, VIX quiet — and
the clearest evidence in the whole record that L9's own joint-percentile construction, rather than
any single-leg proxy, is the correct design: a VIX-only reading of 2013 would have substantially
under-armed the episode relative to what the FX and debt markets were actually pricing.

---

## B5. 2015–16 — the China devaluation and the first Fed hike

**The trigger and the triad.** On **11 August 2015**, the People's Bank of China devalued the
reference rate for the yuan by **1.9% in a single day**, the steepest one-day move in at least two
decades, after China's own domestic equity market (the SSE Composite) had already fallen **~43% in
just over two months (June–August 2015)**. **[Verified.]** The VIX spiked to roughly **40 on
"Black Monday," 24 August 2015** `[VERIFY: exact intraday print]`; the broad dollar rose modestly
through the year on building expectations of Fed "liftoff"; the Fed delivered its **first rate hike
since 2006** on **16 December 2015** (25bp, to 0.25–0.50%) even as the 10-year Treasury yield **fell**
on flight-to-quality demand — a bull-flattening move, the rate leg's direction diverging from the
funds-rate leg's own tightening.

**The EM-wide flow event.** Commodity-linked emerging-market currencies (the South African rand, the
Brazilian real, the Malaysian ringgit among them) fell sharply through the window, and MSCI Emerging
Markets recorded a broad bear-market year in 2015 `[VERIFY: exact full-year MSCI EM 2015 return]`.

**India's transfer.** FIIs pulled a then-**record ₹17,000 crore (≈$2.56 billion)** out of Indian
equities in **August 2015 alone**, the highest monthly outflow on record to that date. **[Verified.]**
The rupee depreciated comparatively mildly against the scale of the global shock — roughly
**₹64 to ₹68** across 2015–16 `[VERIFY: exact daily path]` — a materially smaller move than 2013's
28% or 2018's 11%+ (§B6 below); Nifty fell from around **9,000 (March 2015) to roughly 6,825
(February 2016)**, on the order of a **24% decline** over the window `[VERIFY: precise index
levels/dates]`.

**The oil offset — India's relative resilience.** Brent crude collapsed from roughly **$115/barrel
(mid-2014) to ~$27/barrel (January 2016)** `[VERIFY: precise trough date/level]`, an enormous
terms-of-trade windfall for 85%-import-dependent India that ran directly against the FPI-outflow drag:
the current-account deficit narrowed sharply, headline inflation fell, and RBI's own sustained
disinflationary easing — **125bp of cuts across calendar 2015**, the Rajan-era campaign
`mpcycle-deep/partB-cases.md` case 5 documents in full — was itself partly *enabled* by this same
oil-driven disinflation, the two episodes (global-cycle stress and domestic monetary-policy easing)
overlapping in time rather than running independently. The oil leg belongs to L9's own construction as
a Kilian-decomposed sub-input (never the raw price level, per `config/ladder.yaml`); a fuller
supply/demand decomposition of this specific window is cross-referenced to `research/cycles/
commodity-deep/`, not re-derived here.

**Policy response.** RBI's 2015 easing campaign (cross-ref `mpcycle-deep` case 5, not re-derived).

**Episode length.** The acute global window ran roughly **August 2015–February 2016** (~7 months,
with a Chinese equity/FX reprise in January 2016); India's own drawdown ran a similar 7–11-month
window.

**What L9's state would have read.** This is the clearest documented case in the record of the
triad's legs **netting against each other through the oil sub-input specifically**: the VIX/dollar
legs pointed toward a risk-off regime read, while the Kilian-decomposed oil leg — a supply-glut-driven
price collapse, not a demand-destruction one — fed *positively* into India's own terms of trade. A
composite L9 score reading all inputs jointly would show a materially milder regime reading than the
raw VIX spike alone would suggest — the empirical justification, in a single episode, for why the
seat decomposes oil rather than reading its level directly.

---

## B6. 2018 — QT, the dollar squeeze, and India's double cycle

**The trigger and the triad.** The Fed's balance-sheet runoff (begun October 2017) accelerated through
2018 alongside four 25bp rate hikes (March, June, September, December), taking the funds rate to
**2.25–2.50%** by year-end; the broad dollar rose steadily on US growth outperformance and the hiking
cycle; the 10-year Treasury yield reached **~3.24% in October 2018**, a seven-year high
`[VERIFY: exact print/date]`. The VIX stayed comparatively contained for most of the year but spiked
twice sharply — briefly above **50 intraday during the early-February 2018 "Volmageddon"** episode
(the XIV inverse-VIX-ETN collapse) `[VERIFY: exact intraday print]`, and again to roughly **36 during
the Q4 2018 global equity sell-off** `[VERIFY: exact print]`.

**The EM-wide flow event.** The Turkish lira fell **more than 40% year-to-date by August 2018**, and
hit a record low on **9 August 2018**; the Argentine peso fell **~45% across 2018 (~24% in August
alone)**, forcing Argentina to seek an accelerated **$50 billion** IMF facility. **[Verified, both.]**
The rout spread to the Indonesian rupiah, the South African rand, and the Brazilian real; MSCI
Emerging Markets recorded a broad bear-market year `[VERIFY: exact full-year 2018 MSCI EM return]`.

**India's transfer, and the double cycle.** India's own rupee fell **more than 11% from the start of
2018** by end-August, a then-record low, driven by the same dollar-strength/EM-rout dynamic.
**[Verified.]** Layered directly on top — in the same quarter, not a separate window — **IL&FS
defaulted on 14 September 2018**, the domestic shadow-credit funding-run this record's own sibling
chapter (`shadow-deep/partB-cases.md` §B2) narrates in full: the ratings cliff from AAA to 'D' inside
five weeks, the 1 October 2018 NCLT board supersession, the autumn CP-market seizure. Nifty fell
roughly **15% from its August 2018 peak (~11,760) to an October 2018 trough (~10,000)**;
**[Verified.]** Nifty Bank lost **11% in a single month**, one of its worst since the 2008 crisis, and
DHFL fell **~60% intraday on 21 September 2018** on pure contagion fear. **[Verified, both, per the
shadow-deep monograph's own citations.]** Recovery took roughly **eight months**, Nifty reaching new
highs by mid-2019.

**The interaction lesson.** A global-cycle stress (the dollar squeeze, the TRY/ARS-led EM-FX rout) and
a domestic-cycle stress (the IL&FS funding freeze) hit **in the same quarter**, each plausibly
amplifying the other's transmission channel: the global dollar shortage raised the cost of NBFC
wholesale and external-commercial-borrowing funding at precisely the moment IL&FS's own default froze
domestic CP rollover, while the domestic credit event likely deepened the FII selloff beyond what the
global EM-FX rout alone would have produced. Neither the ladder's `L9` (global) nor its `L2`/`L10`
(domestic fast-stress/credit) seats, read alone, would fully account for the joint severity — a
co-occurrence test between L9's regime score and L2/L10's own readings across August–September 2018 is
flagged here as a data-phase task, not resolved in this Part.

The mechanism linking the two legs runs, plausibly, through wholesale funding costs directly: Indian
NBFCs and HFCs had grown increasingly reliant on commercial paper (rolled over continuously, per
`shadow-deep/partB-cases.md`'s own funding-run anatomy) and, for the larger names, on external
commercial borrowing whose rupee cost embeds the same global dollar-funding conditions this Part's
own triad tracks — meaning a rising DXY and a widening EM dollar-funding premium through mid-2018 was
already raising the *marginal* cost of exactly the rollover IL&FS's own September default then made
suddenly unavailable at *any* price. Cause and confirmation are not fully separable in the data this
pass could assemble `[VERIFY: an isolated NBFC-wholesale-funding-cost series showing the global-squeeze
contribution net of IL&FS's own idiosyncratic default — not independently constructed this pass]`,
but the *timing* coincidence — the global dollar squeeze building through Q2–Q3 2018, IL&FS defaulting
in the same window — is itself the empirical basis for treating 2018 as a genuine interaction case
rather than two unrelated shocks that happened to share a calendar quarter.

**Policy response.** RBI's October 2018 stance (initially declining a dedicated NBFC liquidity
window, then delivering system-wide OMOs) and the 2019 Partial Credit Guarantee Scheme are the
subject of `shadow-deep/partB-cases.md` §B2.8 in full, cross-referenced not re-derived.

**Episode length.** The global TRY/ARS-led stress ran **April–September 2018** (~6 months), extending
into a broader Q4 2018 DM/EM equity sell-off through December; India's own double-cycle acute window
ran **August–October 2018** (~3 months) with an ~8-month recovery tail into mid-2019.

**What L9's state would have read.** The clearest documented instance in this record of L9 (global)
and the domestic credit-stress seats **both flashing at once** — the empirical case the ladder's
shared `macro_credit_block` budget (`config/ladder.yaml`) is structurally built to absorb without
double-counting, and the strongest single argument in the record for actually testing that
co-occurrence rather than assuming the shared-budget design handles it correctly by construction.

---

## B7. 2020 — COVID, the fastest stop on record

**The trigger and the triad.** Following the WHO's pandemic declaration (11 March 2020) and
synchronized global lockdowns, the VIX reached an **all-time intraday high of 82.69 on 16 March 2020**
and an end-of-month peak of **53.54**. **[Verified.]** The broad dollar spiked initially on a "dash
for cash" before falling through the remainder of the year as the Fed eased aggressively: two
emergency cuts (3 and 15 March 2020) took the funds rate to **0–0.25%**, followed by unlimited
quantitative easing announced **23 March 2020**.

**The EM-wide flow event and the backstop.** The initial weeks produced the fastest, most synchronized
emerging-market portfolio outflow on record `[VERIFY: a precise aggregate EM outflow figure —
industry estimates in the $80–100bn range circulated at the time, not independently re-verified this
pass]`. The Fed reactivated and expanded its swap-line network to **14 countries** — the five standing
advanced economies plus temporary lines to **Australia, Brazil, Denmark, Korea, Mexico, New Zealand,
Norway, Singapore, and Sweden** — on **19 March 2020**. **[Verified.]** **India was again not among
the recipients** — the identical hierarchy finding as 2008 (§B3), now a second independent data point
for the same structural conclusion. The Fed's global backstop then reflated risk assets worldwide
within weeks, compressing what would classically have been a multi-quarter global-cycle down-leg into
a matter of weeks — the fastest full round trip (shock to reflation) in this entire nine-episode
record.

**India's transfer.** FPIs net withdrew a **record ₹1.1 lakh crore in March 2020** (₹61,973 crore from
equities, ₹56,211 crore from debt) — roughly **$16.5 billion** net sold that month. **[Verified.]**
The rupee hit successive record lows: **₹74.5 (13 March)**, **₹76.34 (8 April)**, and **₹76.87
(16 April 2020)**. **[Verified.]** Nifty fell from **12,430 (20 January 2020) to 7,511 (23 March
2020)** — a **38% decline in 45 trading days**, the fastest bear-market decline in this entire record
by a wide margin. **[Verified.]**

**The risk-on wave, FY21.** RBI's own domestic response — the 75bp repo cut on 27 March 2020, TLTROs,
the G-SAP bond-purchase programme — is cross-referenced in full to `mpcycle-deep/partB-cases.md`
case 7, not re-derived here. Nifty regained its pre-COVID high by **January 2021** — a complete
recovery within roughly twelve months — on the back of a record FY21 FPI equity inflow wave
`[VERIFY: a precise FY21 aggregate FPI-equity-inflow figure — this pass located directional
confirmation of "record" inflows but not an independently pinned single primary total]`.

**Episode length.** The stop itself ran roughly **four to six weeks** (20 January–23 March 2020 for
equities; FX stress extending through mid-April); the reflation wave ran the length of **FY21**
(April 2020–March 2021, ~12 months) — genuinely the fastest full shock-to-recovery round trip in this
record.

**What L9's state would have read.** VIX and dollar spiked in textbook fashion, but US rates moved the
**opposite** direction from the classic taper-tantrum-style script — cut to zero rather than raised —
because the trigger was a real-economy/liquidity shock transmitted *through* the dollar-funding and
risk-appetite legs even as the rate leg eased. The swap-line exclusion repeats 2008's exact structural
lesson: India's own pre-COVID reserve stock (near **$475 billion** `[VERIFY: precise February–March
2020 figure]`) was again the self-insurance cushion in place of a Fed backstop, reinforcing rather
than merely repeating the 2008 finding.

---

## B8. 2022–23 — the hiking wave

**The trigger and the triad.** Post-COVID inflation, sharpened by the Russia-Ukraine war's energy and
food-price shock (from February 2022), drove the fastest Fed tightening cycle since Volcker: the
funds rate rose from **0–0.25% (March 2022) to 4.25–4.50% (December 2022)**, including four
consecutive **75bp** hikes (June–November 2022). The broad dollar index (DXY) peaked at
**114.78 on 27 September 2022**, a 20-year high, before easing roughly 10% by year-end to **~103.5**.
**[Verified, both.]** The VIX, by contrast, stayed comparatively contained relative to 2008 or 2020,
peaking in the mid-to-high 30s during the worst equity-selloff weeks `[VERIFY: exact 2022 VIX peak]`;
the 10-year Treasury yield rose from roughly **1.5% (early 2022) to ~4.25% (October 2022)**
`[VERIFY: exact path]`.

**The EM-wide flow event.** Essentially every major currency fell against the dollar through 2022 —
the yen, euro, and sterling alongside emerging-market currencies broadly — with a distinct
developed-market echo in the UK gilt crisis (September 2022, the "mini-budget" episode); US equities
recorded a sharp bear-market year (S&P 500 roughly **−19%**, Nasdaq Composite roughly **−33%**, in
2022) `[VERIFY: exact full-year figures]`.

**India's transfer.** FPIs recorded a record equity exodus through this window — **~₹1.14–1.21 lakh
crore** net outflow by the CY2022 calendar-year count is the figure this pass could independently
verify `[VERIFY: the task's own framing of "~₹1.4 lakh crore" for FY22 (April 2021–March 2022)
specifically was not independently reconciled this pass against the ₹1.14–1.21 lakh crore CY2022
figure that was verified — the two windows (fiscal vs. calendar year) plausibly explain most of the
gap, and both orders of magnitude recur across sources]** — its largest on record to that point. The
rupee touched a **record low of ₹83.06/USD on 19–20 October 2022**. **[Verified.]** Nifty, by
contrast, closed 2022 modestly positive to flat while global peers fell sharply
`[VERIFY: precise full-year Nifty 2022 return]` — the "outperformance-in-a-bear" this record's own
task explicitly asks to be revisited honestly, below.

**The partial-insulation debate, revisited honestly.** Two readings compete, and neither should be
asserted alone. The favorable reading: a smaller current-account deficit than in 2013, a domestic
DII/SIP flow base large enough to absorb FPI selling — the atlas's own rejected "FII flow momentum"
finding (`docs/CYCLE_ATLAS.md` §7) already documents DII/SIP growth as the standing absorption
mechanism — and an earnings/growth narrative sufficiently decoupled from the US rate shock that
foreign selling did not translate one-for-one into an equity crash. The honest counter-reading: the
calm was **partly bought, not free**. RBI's own reserves fell from an all-time high of
**$642.45 billion (3 September 2021) to $524.52 billion (21 October 2022)** — an **~$118 billion**
decline — defending the rupee through active intervention, though Governor Das himself attributed
**67% of that fall to dollar-strength revaluation rather than intervention**. **[Verified, both
figures.]** The rupee's own fall (₹75→83, roughly **10%**) was genuinely more orderly than 2013's
₹55→69 (~28%) or 2018's 11%+, even against a **larger** dollar move (DXY 114.78 in 2022 vs. a more
modest 2013 dollar move) — evidence for a *degree* of improved insulation, but not evidence that the
insulation was structural or free of active defense. GF3's own licensed sentence applies here without
softening: partial insulation from a given global down-year is real roughly seven times in ten, never
assumable in advance.

**The 2023–24 return of flows.** FPIs poured **₹1.71 lakh crore** into Indian equities across
calendar 2023 — a sharp reversal from 2022's outflow — a genuinely different post-episode INR path
than 2013's own subsequent round trip: the rupee stayed comparatively range-bound (₹82–83) through the
flow reversal rather than sharply re-appreciating. **[Verified.]**

**Policy response.** RBI's own 250bp hiking campaign (May 2022–February 2023) is cross-referenced in
full to `mpcycle-deep/partB-cases.md` case 7, not re-derived here; no MSF-corridor-style emergency
defense (2013's own instrument) was required this time.

**Episode length.** The global hiking wave ran **March 2022–July 2023** (the last hike, ~16 months);
India's own acute INR/FPI stress window ran roughly **February–October 2022** (~9 months), with flows
already reversing by early 2023.

**What L9's state would have read.** DXY at 114.78 is the single loudest "dollar" leg reading in this
entire nine-episode record, yet the VIX and US-rate legs told a comparatively muted story relative to
2008 or 2020 — dollar amplitude far exceeding the other two legs, the reverse ordering from 2020's
VIX-dominant signature and a third distinct triad-asymmetry pattern (after 1997–98's mixed-direction
case and 2013's rates-and-dollar-led case) in this record, reinforcing why the seat reads all three
jointly.

---

## B9. 2024–2026 — the current regime, and the May-2026 test case

**The easing turn.** The Fed began cutting in **September 2024** (50bp), continuing with **three
further 25bp cuts in September, October, and December 2025**, taking the funds rate to
**3.50–3.75%**, where it has held through **July 2026** (its fifth consecutive unchanged meeting).
**[Verified.]** RBI's own parallel easing turn — repo **6.50%→5.25%, February–December 2025**, the
"most aggressive easing cycle in six years" by its own characterization — is `mpcycle-deep/
partB-cases.md` case 8's own subject in full, cross-referenced not re-derived.

**The 2025 tariff/trade-war shocks.** US tariffs on Indian goods escalated from **25% to 50%
by August 2025**, explicitly cited by RBI as a reason for its own August/October 2025 policy pause
(cross-ref `mpcycle-deep` case 8). By 2026, the situation partially reversed: Trump and Modi agreed to
cut tariffs on Indian goods from 50% to **18%**, removing an earlier 25-point add-on duty — before the
US Supreme Court struck down the emergency-tariff authority the original escalation had relied upon,
followed by a **temporary 15% levy** on imports more broadly. **[Verified, the full sequence, via this
pass's search.]**

**The May-2026 INR episode — the atlas's own live test case, honestly reconstructed.** Public
reporting on this episode is considerably thinner than on any of the prior eight — far less time has
passed for post-mortem analysis, and the figures below are the verifiable window this pass could
assemble, not a completed narrative. **USD/INR swung from a low of 89.86 in early January 2026 to an
all-time record high of 96.84 on 20 May 2026**, before a partial recovery to roughly **94.35** by late
H1 2026. **[Verified.]** Three factors compound in contemporary reporting, rather than one dominant
trigger organizing the whole episode as in every prior case in this record: **(i)** the lingering
50% US tariff overhang from mid-2025 continuing to weigh on export competitiveness even as the
bilateral rate cut was being negotiated; **(ii)** sustained FPI equity outflows — **₹32,963 crore in
May 2026 alone**, part of a cumulative **₹2.25 lakh crore CY2026 outflow already exceeding the entire
₹1.66 lakh crore withdrawn across all of CY2025** — with the weakening rupee itself cited as a
self-reinforcing driver of further outflows (a weaker INR compounding foreign investors' own
dollar-denominated losses); and **(iii)** a Brent crude spike from the **$70/barrel range to
$95–105/barrel** on **Strait of Hormuz** disruption, widening both the import bill and the current-
account deficit for an 85%-import-dependent economy. **[Verified, all three, via this pass's
search.]** The recovery to ~94.35 is attributed in contemporary reporting to RBI intervention, falling
crude, and "a coordinated package of capital-account reforms" `[VERIFY: this phrase recurs across
secondary sources without a specific, itemized description of the reform package this pass could
independently confirm]`.

**What the triad showed going in.** Contemporaneous readings place the **DXY near 99 in early-to-mid
2026** — down roughly 10% from a January 2025 peak above 109, and far below 2022's 114.78 — and the
**VIX near 16**, a comparatively quiet reading well under every other episode's acute-window level in
this record. **[Verified, both, though precise May-2026-specific daily prints were not independently
pinned this pass.]** The Fed itself was already easing (funds rate 3.50–3.75%, three cuts already
delivered in 2025), not tightening. **This is the honest finding this Part owes the ladder**: going
into May 2026, **none of the three classic triad legs was flashing the tightening/risk-off signature
every prior episode in this record shows in some combination** — the shock arrived instead through a
**bilateral tariff channel** (US-India specific, not a broad-dollar move) and a **regional oil-supply
shock** (Strait of Hormuz, not a demand-driven global slowdown), both largely outside the triad's core
three-variable construction, though the oil leg is *partially* visible to L9 through its own
Kilian-decomposed sub-input (`config/ladder.yaml`; cross-ref §B5 above for the mechanism) — meaning a
correctly-built L9 would have registered *some* signal from the oil-supply shock specifically, even
while its VIX/dollar/rate core stayed quiet.

**What the state would have conditioned.** Per `partCDEFH.md` Part D's own stated design — "the seat
detects episodes, refuses forecasts" — L9 is not built to have predicted a bilateral tariff
negotiation or a Strait of Hormuz disruption in advance, and this Part does not claim it should have.
What the state *would* have conditioned, honestly: a quiet VIX/dollar/rate reading going into the
episode should have licensed **more**, not less, leverage/concentration permission under the ladder's
own regime-score logic (`config/ladder.yaml` budgets) — precisely the design's own accepted risk,
stated plainly in the Contract's own governing discipline (§7, Known Prior #8): a global-cycle seat
reading calm conditions cannot itself protect against a shock that arrives through a channel the seat
was never built to watch. This is `partCDEFH.md`'s own **GF-D3** design — "the May-2026 test case
re-grade on real data" — named as the atlas's own live exam, and this Part's honest contribution is
to state, before that re-grade runs, that the test case is likely to show a **quiet-triad, high-
transfer** episode: exactly the pattern the seat's own design should be judged capable of flagging
(via the oil sub-input) rather than one it should be expected to have called outright.

**Episode length.** As of this writing (2 September 2026), the episode's own eventual length is not
yet determinable — the partial INR recovery to ~94.35 by late H1 2026 suggests the acute window (low
89.86 to peak 96.84) ran roughly **January–May 2026** (~4–5 months) with a still-ongoing partial
unwind, but per this record's own design discipline (echoing `mpcycle-deep` case 8's identical
refusal for the current rate-easing plateau), this Part declines to forecast whether May 2026 marked
the episode's own trough or merely its most recent stop.

**A Stage-2 note, stated for completeness and nowhere else.** The Contract's own architecture
(`research/CONTRACT.md` §2) reserves forward-looking judgement that cannot be backtested for Stage 2,
never Stage 1 — and a bilateral-tariff-negotiation outcome or a Strait-of-Hormuz risk premium are
precisely the kind of judgement calls this record's own quiet-triad finding above implies a Stage-1,
rules-only L9 cannot make. This Part's own honest position, consistent with that architecture, is
that the May-2026 episode is better read as evidence **for** a Stage-2 overlay's narrow, advisory
value in exactly this kind of channel-outside-the-triad scenario (a shadow-book, human-vetoed
tactical read of an idiosyncratic bilateral or geopolitical risk) than as evidence the Stage-1 seat
itself needs redesigning — L9's job, per `partCDEFH.md`, is to detect the *global* factor's episodes,
not to substitute for every possible source of India-specific currency stress, a distinction this
record's own §B2 (Pokhran) and §B9 (the tariff/Hormuz overlay) both independently illustrate.

---

## B10. Synthesis

**Three cross-episode patterns, stated before the table rather than only inside it.** First, a
**triad-asymmetry typology**: no two episodes in this record share the identical triad signature.
1994 and 2013 are rates-and-dollar-led with a comparatively quiet VIX; 1997–98 is the record's only
mixed-direction case (VIX and dollar both up while the Fed *eased*); 2008 and 2020 are the only two
full-alignment cases (all three legs moving together at extreme readings); 2015–16 is the record's
clearest netting case, where a fourth, decomposed leg (oil) pulls against the other three; and 2022
is dollar-dominant with the other two legs comparatively muted. A design that read any single leg as
"the" global-cycle indicator would have missed, or badly mistimed, at least five of these nine
episodes — the standing argument, repeated once more at the record's close, for L9's own joint-
percentile construction. Second, a **swap-line hierarchy** repeats exactly twice, in 2008 and 2020,
with India absent both times from a Fed backstop extended to a named cohort of "systemically
important" or allied emerging markets — not a one-off exclusion but a structural feature of the
dollar system this record's own reserve-currency monograph grounds formally, and the direct reason
India's own reserve-adequacy framework (a policy choice, not a passive fact) carries the weight a
swap line carries for its recipients. Third, **episode length has not obviously shortened over this
record's 32-year span** in the way a naive "the world moves faster now" prior might predict: 2020's
own stop-to-reflation round trip was genuinely the fastest, but that speed is attributable
specifically to the Fed's own within-weeks global backstop (unlimited QE, swap-line reactivation),
not to a general compression of episode dynamics — 2018's double-cycle recovery (~8 months) and
2022–23's own multi-quarter unwind (India's flows not fully reversing until 2023, a ~9–16 month arc)
sit closer to 2008's own multi-quarter pattern than to 2020's multi-week one, meaning the controlling
variable across this record is less "how fast is the world" than "how fast, and how large, is the
policy-backstop response" — a genuinely different, and more specific, claim than a blanket
compression narrative would offer.

| Episode | Global trigger | Triad signature | EM breadth | India transfer (flows / INR / equity) | Episode length | L9 read | Policy response |
|---|---|---|---|---|---|---|---|
| **1994 Tequila/Fed** | Fed funds 3%→6% in 12mo (+240bp 10Y); Mexico devalues 15% (20 Dec 1994) | Rates-led; VIX data unusable this early; dollar up | Latin America contagion (Argentina, Brazil); India's channel too thin to register | Portfolio inflow *grew* $4mn→$3,824mn (FY92→FY95); INR stable low-₹30s; no dateable equity event | EM ~Dec1994–mid1995; India: non-event | No India-side signal exists — the baseline before the transfer existed | None (standing 1991–93 reform program only) |
| **1997–98 Asian + LTCM/Russia** | Baht float 2 Jul 1997; Russia default + LTCM collapse Aug–Sep 1998 | VIX up, dollar up, **US rates cut** (Sep–Nov 1998) — mixed-direction triad | Asian currencies −30 to −80%; regional equities −50 to −75% | Bank Rate 9%→11% (17 Jan 1998) defense; rupee ~₹39.5 stabilized; Pokhran sanctions overlay (May 1998) compounds; `[VERIFY]` equity drawdown | EM ~2yr; India ~9–10mo (Jan–Oct 1998) | Under-read: sanctions shock invisible to VIX/dollar/rates | Bank Rate/CRR defense (cross-ref mpcycle case 1) |
| **2008–09 GFC** | Lehman 15 Sep 2008 | VIX all-time high 89.53 (24 Oct 2008); dollar sharply up; Fed to zero (Dec 2008) | Fed swap lines to Brazil/Mexico/Korea/Singapore (29 Oct 2008) — **India excluded** | FII outflow ~$13–15.4bn; INR ₹39.27→₹52.1 (FY09 −21.9%); Nifty ~6,357→~2,252 (~60–65%, `[VERIFY exact]`) | EM ~7mo (Sep08–Mar09); India peak-to-recovery Jan08–Nov10 | Textbook full-triad alignment; swap-line hierarchy lesson #1 | Repo 9%→4.75%, CRR 9%→5% (cross-ref mpcycle case 3) |
| **2013 taper tantrum** | Bernanke testimony 22 May 2013 | Rates/dollar-led, **VIX quiet** | Fragile Five sorted by CAD (Brazil/India/Indonesia/S.Africa/Turkey) | INR ₹55→₹68.85 (28 Aug 2013, −28%); MSF 300bp defense; FCNR(B) $34bn (cross-ref mpcycle case 4, shadow-deep §B5) | EM May–Dec 2013; India ~5–6mo, stable by ~Jan2014 (~7mo) | Second asymmetric-triad case; joint-percentile design vindicated | MSF corridor + FCNR(B) swap (cross-ref, not re-derived) |
| **2015–16 China deval** | PBOC deval 11 Aug 2015; Fed liftoff 16 Dec 2015 | VIX ~40 (24 Aug); dollar up; **10Y fell** despite hike | EM currencies + equities broad bear 2015 | FII −₹17,000cr record month (Aug 2015); INR ~₹64→68 (mild); Nifty ~9,000→6,825 (~24%) | ~7mo acute | Oil sub-input **nets against** VIX/dollar — milder composite than raw VIX implies | RBI 125bp 2015 easing enabled by oil disinflation (cross-ref mpcycle case 5) |
| **2018 QT + dollar squeeze** | Fed QT + 4 hikes to 2.25–2.50%; DXY up | VIX spikes twice (Feb "Volmageddon," Q4 selloff); dollar up; 10Y ~3.24% (Oct) | TRY −40%+, ARS −45% (2018); broad EM bear | INR −11%+ YTD; **+ IL&FS 14 Sep 2018 double cycle**; Nifty ~11,760→~10,000 (~15%); DHFL −60% intraday | Global ~6mo (Apr–Sep); India double-cycle ~3mo acute, 8mo recovery | Both L9 (global) and L2/L10 (domestic credit) flash simultaneously — the interaction case | RBI OMOs + PCG scheme (cross-ref shadow-deep §B2.8) |
| **2020 COVID** | WHO pandemic 11 Mar 2020 | VIX all-time high 82.69 (16 Mar); dollar spikes then falls; Fed to zero + QE | Fed swap lines to 14 countries (19 Mar 2020) — **India excluded again** | FPI −₹1.1 lakh cr record month; INR ₹74.5→76.87; Nifty 12,430→7,511 (−38%, 45 days) | Stop ~4–6wk; FY21 reflation ~12mo | Fastest full round trip on record; swap-line hierarchy lesson #2 | Repo −75bp, TLTRO, G-SAP (cross-ref mpcycle case 7) |
| **2022–23 hiking wave** | Fed 0.25%→4.50% (fastest since Volcker) | DXY 114.78 (27 Sep 2022, 20yr high); VIX comparatively muted; 10Y ~1.5%→4.25% | Broad DM/EM FX weakness; UK gilt crisis | FPI record CY2022 outflow ~₹1.14–1.21 lakh cr (`[VERIFY vs task's ~₹1.4 lakh cr FY22 framing]`); INR →₹83.06 (19–20 Oct 2022); Nifty ~flat 2022 | Global ~16mo (Mar22–Jul23); India ~9mo acute | Dollar-dominant triad asymmetry (third pattern); insulation partly *bought* (reserves $642bn→$524bn) | RBI 250bp hikes (cross-ref mpcycle case 7) |
| **2024–26 current regime** | Fed easing turn (Sep 2024+); 2025 tariff escalation 25%→50%; May-2026 INR episode | **DXY ~99, VIX ~16 — quiet triad going in**; Fed already easing | Bilateral tariff shock + Strait of Hormuz oil spike, not a broad EM wave | FPI CY2026 outflow ₹2.25 lakh cr (>all of CY2025's ₹1.66 lakh cr); INR 89.86→96.84 (20 May 2026)→~94.35; equity `[not separately verified this pass]` | Acute ~Jan–May 2026 (~4–5mo), unwind ongoing, terminal point not yet determinable | Quiet-triad, high-transfer — the honest gap: L9's core three legs did not flag this episode; the oil sub-input partially did | RBI intervention + falling crude + unspecified capital-account reforms `[VERIFY]` |

**The one-line synthesis.** GF1's own finding — the global factor's rise is a post-1990s phenomenon —
is visible case by case in this table as India's transfer growing from *non-existent* (1994) to
*full and immediate* (2008 onward); GF2's +0.57 loading is the number underneath every "India transfer"
column from 2008 forward; and GF3's 69%-median-breadth finding, the desk's own licensed insulation
sentence, is the discipline behind every "partial insulation" claim in this table — real in several
episodes (1994's structural absence, 1997–98's capital-account closedness, 2022's smaller CAD and
deeper domestic-flow base), never assumable before the fact. The triad's three legs move together only
sometimes — 2008 and 2020 show full alignment, while 1997–98, 2013, 2015–16, and 2022 each show a
different asymmetric pattern — which is the standing design argument, restated once more at the close
of this record, for why L9 reads VIX, dollar, and US rates jointly rather than through any single leg,
and why the seat (per `partCDEFH.md`'s own closing language) detects episodes and refuses forecasts,
including — honestly, per §B9 above — the one the atlas itself names as the desk's live test case.

---

## References

Rey, Hélène (2013), "Dilemma not Trilemma: The Global Financial Cycle and Monetary Policy
Independence," Jackson Hole Economic Policy Symposium (dossier 08 §F3, cross-referenced not
restated). · Miranda-Agrippino, Silvia & Rey, Hélène (2020), "US Monetary Policy and the Global
Financial Cycle," *Review of Economic Studies* (dossier 08 §F4). · This directory's own
`global-RESULTS.md` (GF1–GF3, pre-registered, cited throughout, never recomputed) and `partCDEFH.md`
(data engineering, mathematics, algorithm, harvest map, knowledge ledger — cross-referenced by name
throughout, never re-derived). · `research/cycles/mpcycle-deep/partB-cases.md` (cases 1, 3, 4, 5, 7,
8 — domestic monetary-policy mechanics for 1997–98, 2008–09, 2013, 2015–16, 2020, 2024–26,
cross-referenced not re-derived). · `research/cycles/shadow-deep/partB-cases.md` (§B2 IL&FS
funding-run anatomy; §B5 the 2013 NBFC negative control — cross-referenced not re-derived). ·
`docs/cycles/06-reserve-currency.md` (the dollar-system frame; the four-role split; the swap-line
hierarchy applied to 2008 and 2020 above). · `docs/CYCLE_ATLAS.md` row 2.8 and §7 (the rejected
FII-flow-momentum finding, cited for the DII/SIP absorption mechanism in §B8). · `config/ladder.yaml`
(`L9_global_financial_cycle` entry). · Federal Reserve press releases, 29 Oct 2008 and 19 Mar 2020
(swap-line announcements, both verified). · Morgan Stanley's "Fragile Five" framing (2013, widely
reported contemporaneously). · Business Standard, CNBC, Business Today, Reuters/Investing.com,
TradingEconomics, and other contemporaneous financial-press reporting for the dated FX/FPI/equity
figures throughout, per the `[VERIFY]` discipline stated at each figure's first use; primary-source
RBI/SEBI/NSDL/FRED series were not directly queryable this session (egress restrictions, per
`research/CONTRACT.md` §7 Known Prior #11) and every figure above is therefore cross-checked against
secondary reporting rather than a primary release, exactly as this program's own house style requires.

---

# PART B-RESULTS — The desk's own numbers (GF1–GF3, pre-registered)

# Atlas 2.8 — global financial cycle: GF1-GF3 (pre-registered)

## GF1 — the factor's rise (pairwise co-movement, annual real equity)

- Pre-1990 median pairwise corr **+0.28** (120 pairs); post-1990 **+0.77** (120 pairs); difference **+0.49** (bar ≥ +0.10): **PASS**.

## GF2 — India's loading (annual, 1994-2015, n=22)

- corr(India market factor, equal-weight JST mean) = **+0.57** (bar ≥ 0.30): **PASS**.

## GF3 — breadth of global down-years (post-1950)

- 18 global-down years; median share of countries negative **69%** (bar ≥ 75%): **FAIL**.
- Down years: [1957, 1962, 1965, 1966, 1970, 1974, 1976, 1977, 1987, 1990, 1992, 1994, 2000, 2001, 2002, 2008, 2011, 2018]

## Honest read (written AFTER the print)

- **GF1 is one of the cleanest results in the project:** median pairwise co-movement of
  national equity markets nearly TRIPLED across 1990 (+0.28 → +0.77). The "one global cycle"
  premise isn't imported from Rey — it's on our own panel, and its RISE is why pre-1990
  analogue evidence about diversification and insulation must be discounted when transferred
  to today's India (a standing caveat for every cross-era claim in this register).
- **GF2 confirms the seat's transfer premise:** India's market factor loads at +0.57 on the
  equal-weight global factor over 1994-2015 — materially inside the cycle, exactly what a
  0.20-budget global seat presumes. n=22 annual observations, stated.
- **GF3 FAILS its bar honestly (69% vs 75%):** global-down years pull a median of ~2/3 of
  countries negative, not the ≥3/4 the bar demanded. The claim "one cycle, EVERYWHERE" is
  too strong even post-globalization; the accurate sentence is "one cycle, in most places,
  most of the time" — which slightly WEAKENS the undiversifiable-exposure framing at the
  margin and is recorded as such (partial insulation is real sometimes; the desk just never
  gets to ASSUME it in advance). Bar unmoved.

---

# Parts C–H — data engineering, math, algorithm, harvest, ledger (atlas 2.8; seat L9)

## Part C — Data engineering (compact, in-house; the triad's free-access reality)

| Leg | Primary (blocked here) | Free path for the desk | Cadence/lag |
|---|---|---|---|
| VIX / risk appetite | CBOE via FRED | India VIX (NSE archive — already in the L2 pull family); CBOE publishes VIX history on cboe.com [VERIFY access from principal's machine]; datahub mirror hunt at pull time | daily |
| Broad dollar | FRED DTWEXBGS | FRED blocked → principal's machine (ingest/pull_fred.py EXISTS); fallback: DXY from free mirrors (stooq) with a declared index-substitution note (DXY ≠ broad — bias stated) | daily |
| US real yields | FRED DFII10 | principal's machine via pull_fred.py; fallback: nominal 10y minus survey CPI (constructed, flagged) | daily |
| FPI flows | NSDL | ingest/pull_nsdl_fpi.py EXISTS (untested live) | daily/weekly |
| INR | RBI/FBIL reference rate | mp-cycle partC C.2's pull family — cross-ref, no duplication | daily |
| Kilian activity index | Kilian's site | updated index publicly posted [VERIFY current host]; annual re-pull | monthly |

PIT hazards: VIX methodology 2003 revision (backfilled series — vintage note); broad-dollar
index reweights (FRED publishes revisions — vintage per pull); NSDL categry reclassifications
(FPI/FII regime change 2014 — breaks registry); the DXY-vs-broad substitution bias whenever
the fallback is active (flag travels with every derived state).
Runsheet addendum 10 (steps 57-60): 57 FRED triad via pull_fred.py + vintages (~2h);
58 NSDL FPI first live run + 2014 break rules (~2-3h); 59 India-VIX archive backfill (~2h);
60 L9 state assembly + GF re-run wiring (~3-4h). Total ~9-11h.

## Part D — The mathematics

L9's state: expanding percentiles of the triad legs (dollar level+impulse, VIX level, US real
yield impulse) combined per the registered block rules; episode τ½ 3-9m makes this the ladder's
FASTEST macro seat — the state is an EPISODE detector, not an era classifier (contrast L6). The
measured base: GF1's regime change (+0.28→+0.77) grounds the pooled-Tier-A grade and creates
the STANDING CAVEAT that pre-1990 analogue evidence discounts on transfer (now cited wherever
old panels feed India claims). GF2 (+0.57) is the transfer coefficient's first in-house
estimate — the ladder's changes_if ("India factor-loading estimate") is now partially served;
the monthly-frequency loading with proper controls remains design GF-D1. GF3's fail bounds the
claim: median 69% breadth means partial insulation EXISTS ex post; the seat's job is refusing
to assume it ex ante (the decoupling trap, Part G of the theory chapter).

## Part E — The algorithm (L9, daily/weekly)

```
STEP 1  triad legs -> expanding percentiles (shared grids); Kilian-decomposed oil enters as
        the demand/supply-split conditioner (never raw price; commodity monograph D3)
STEP 2  episode state: dollar-up + VIX-up + real-yield-up co-movement percentile (the Rey
        signature); n_legs degradation when a leg's feed is stale (DXY fallback flagged)
STEP 3  consumption: global_cycle block (0.20) conditions India book size; hedge scheduling
        reads episode ARMED; sector projection reads the oil decomposition
STEP 4  FPI flows enter as CONFIRM only (flows follow returns — atlas 2.13's finding);
        never as a leading leg
MONITOR annual GF1-GF3 re-run; the May-2026 INR episode file (cases chapter) re-graded when
        NSDL/INR data is vaulted — the seat's named live test case
FAILURE MODES: fallback-index bias (flagged state); swap-line/backstop regime changes
        (2020's Fed backstop compressed episode length — regime note); decoupling narratives
        entering through the briefing layer (countermeasure: GF3's number is the ONLY
        licensed insulation sentence)
```

## Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| global_cycle block (0.20) | the episode state (triad percentiles) |
| Hedge scheduling | episode-armed flag (τ½ 3-9m — the fastest macro input) |
| L9 oil conditioner | Kilian split (commodity monograph cross-ref) |
| Registry | the pre-1990-discount standing caveat (GF1); the licensed insulation sentence (GF3) |
| Cycle School | Lesson 22: the cycle that globalized; passes, and an honest miss |

Designs: **GF-D1** monthly India loading with world-factor + oil + INR controls (needs the
FRED triad vaulted; acceptance registered at pull). **GF-D2** episode catalog validation: L9's
armed dates vs the cases chapter's nine episodes (event-matched, registered before the look).
**GF-D3** the May-2026 test case re-grade on real data (the atlas's own live exam).

## Part H — Knowledge ledger (atlas 2.8)

**Established (our runs):** the global cycle's RISE (+0.28→+0.77 pairwise, GF1 — the register's
cleanest regime change); India inside it at +0.57 (GF2); breadth bounded at ~69% median (GF3
fail — insulation exists ex post, never assumable ex ante). **Established (record):** nine
episodes 1994-2026 with India's transfer growing as the capital account opened (cases chapter).
**Unknowable:** the next episode's trigger and the Fed's reaction function; the seat detects
episodes, refuses forecasts. **Process:** GF3's fail refined the seat's language rather than
its structure — bars that fail productively are the register working as designed.
