# Commodity Supercycle Deep Dive — Part A & Part G

Part A: Theory — extraction capacity, decade-scale demand, and why the desk tests the "supercycle"
label rather than assuming it · Part G: Operator psychology · v1.0 · 2026-09-01 · Atlas entry 1.3
(`docs/CYCLE_ATLAS.md` row 64, Band 1 "multi-decade"). Candidate ladder seat **H53** (context +
sector-tilt conditioner + L9 enrichment, Tier C until researched), alongside sibling candidates
**H54** (China credit impulse, row 87) and the atlas's existing commitment on oil (row 2.12,
"Kilian decomposition — never raw price level"). Evidence base: this file + this program's own
pre-registered trials **CS1–CS4** (`research/cycles/commodity-deep/commodities-RESULTS.md`) run on
the vaulted Jacks (2016/2019, *Cliometrica*) real commodity price panel, 1850–2015, 40 series,
1900=100, cross-checked against Clio-Infra/USGS world metal production (same vault), with the IMF
monthly commodity panel (1980–2017) and EIA Brent/WTI monthlies (to 2026) held for the live-state
construction once the design register opens. Complements, never duplicates, `docs/cycles/
06-reserve-currency.md` and `research/cycles/reserve-deep/` (the dollar/commodity and dollar/INR
channel, cited by reference, not recomputed here) and D07 (`research/dossiers/07-long-waves.md`,
the program's general epistemics on manufactured periodicity). Status: theory and citations
verified here; CS1–CS4 already ran and are cited with their actual numbers throughout — this is a
post-print, not a forthcoming-trial, chapter, and its honesty is calibrated to what those trials
actually found, not to what the literature claims.

This file assumes the Contract's frozen posture as given (`research/CONTRACT.md` §4–§8): cycles
have persistence, not periodicity; anything without ≥4 observed complete periods is a state
variable, not a cycle (the clock test); Tier-C signals may only reduce risk; the HP filter is
banned outright and Hamilton's (2018) regression filter is the mandated substitute — never a
two-sided band-pass, anywhere, for anything that trades. H53's own atlas row already frames the
commodity supercycle as a **capacity-limit mechanism** sitting in the same 15–20-year band as the
financial cycle (1.1) and the real-estate cycle (1.2), explicitly downgraded from the literature's
own 30–40-year framing — Part A explains why that downgrade was already the honest prior, and
reports what CS1–CS4 found when the desk actually tested it. Part G turns to the psychology of a
desk on the *importing* side of this cycle, for whom every reading carries a non-neutral temptation.

---

## PART A — Theory: extraction capacity, decade-scale demand, and what survives testing

### A.1 The object: what a commodity supercycle is claimed to be — and what CS1/CS2 found when tested

**(i) The claim, in its two canonical statements.** **Erten, Bilge & Ocampo, José Antonio (2013),
"Super Cycles of Commodity Prices Since the Mid-Nineteenth Century"** (*World Development* 44:
14–30) apply a band-pass filter to a non-fuel real commodity price index spanning 1865–2010 and
report **four super-cycles**, each running roughly **30–40 years** trough-to-trough or peak-to-peak,
with the upward phase of each led by a *different* demand source (the paper's own framing places
successive upswings against late-19th-century industrialization, the World Wars/reconstruction era,
and — the cycle live when the paper was written — China's 2000s industrialization) [VERIFY: exact
turning-point years per cycle — this session's network access to the UN DESA working-paper mirror
and the World Bank's own hosted copy of the article were both blocked at the proxy per CONTRACT §7
Known Prior #11; the four-cycles/30–40-year/demand-led-upswings framing itself is independently
corroborated across multiple secondary citations of the paper and is not in doubt]. **Cuddington,
John T. & Jerrett, Daniel (2008), "Super Cycles in Real Metals Prices?"** (*IMF Staff Papers* 55(4):
541–565) run the closer methodological antecedent: an asymmetric Christiano-Fitzgerald band-pass
filter extracting the **20–70-year** frequency band from roughly 150 years of annual real prices
for the six London Metal Exchange base metals (aluminum, copper, lead, nickel, tin, zinc), finding
evidence consistent with **three completed super-cycles** and — as of their 2008 vintage — the
**early phase of a fourth**, the same China-driven upswing Erten-Ocampo's paper closes on.

**(ii) Why the desk refuses band-pass filters for real-time use — restated, not re-argued.** Both
papers share the property CONTRACT §8 already bans for exactly this reason: a band-pass filter
(Christiano-Fitzgerald, Baxter-King, or the HP filter it is a cousin of) computes its mid-sample
value using the *entire* series, including years that had not happened yet at any historical
decision date. **Hamilton, James D. (2018), "Why You Should Never Use the Hodrick-Prescott
Filter"** (*Review of Economics and Statistics* 100(5): 831–843) makes this argument for the HP
filter specifically — spurious end-of-sample dynamics, a smoothing parameter at odds with principled
statistical justification, and filtered values near the sample end that revise sharply as new data
arrives, precisely where a live desk needs the reading stable. That argument transfers unchanged to
a 20–70-year band-pass window: a filter built to isolate a supercycle **needs decades of future data
to tell you where in the supercycle you currently sit** — a look-ahead machine by construction. This
is the *same* reasoning L12 already states (`research/cycles/fincycle-deep/
partA-theory-psychology.md` §A.2) and the same reasoning that keeps Elliott Wave and Gann out
entirely (CONTRACT §8; atlas §11) — the desk is not rejecting Erten-Ocampo or Cuddington-Jerrett as
scholarship, it is refusing to run their *method* live. Both papers are respected here as
**historiography**: honest accounts of what happened, told with the benefit of knowing what
happened next — exactly what this chapter needs and exactly what a real-time state cannot use.

**(iii) CS1/CS1b — testing the claim on its own terms, without a band-pass filter at all.** The
desk's own pre-registered check does not merely distrust band-pass filtering; it asks whether the
literature's specific **count-and-length claim** (3–4 supercycles, troughs 30–40 years apart)
survives a plain **turning-point** method — the same real-time-honest family of tool L12 already
uses in place of Drehmann-Borio-Tsatsaronis's own band-pass measurement (fincycle-deep §A.2ii). CS1
built an aggregate real-price index from the Jacks 40-series panel two ways — an equal-weight level
("plain") and a chain-linked growth aggregate ("chained") — and located local minima with a
15-year minimum spacing, starting from 1870. The two constructions returned **identical trough
years**: 1879, 1897, 1913, 1931, 1949, 1970, 1986, 2001 — spacings of 18, 16, 18, 18, 21, 16, and
15 years, **median 18 years**, against a pre-registered bar of 3–5 troughs with a median spacing
inside [25,45] years. The pre-registered bar's verdict: **FAIL**, on both constructions, for the
same reason — the aggregate index does not turn over three or four times in 150 years, it turns
over **seven or eight times**, at roughly **half** the literature's claimed periodicity.

**(iv) What this does and does not overturn.** This is not evidence against Erten-Ocampo or
Cuddington-Jerrett's own scholarship on their own filtered series — a band-pass filter targeting
20–70-year cycles will, by construction, suppress the ~15–20-year rhythm CS1's turning-point method
finds and report whatever longer-period residual survives the filter, which is a different
statistical object from "how often does the raw aggregate actually turn." It **is** direct evidence
that the specific number "3–4 supercycles, 30–40 years" is a **filter artifact relative to this
panel**, not a robust count-and-length fact that survives a simpler, real-time-honest method — the
same lesson D07 §1G already teaches generically (Slutzky 1937, Granger 1966: smoothing manufactures
periodicity that raw persistence does not contain) now demonstrated on this specific data. Read
against Band 1's own neighbors, the result is not a null finding — it is a **relocation**: an
18-year median trough-to-trough spacing sits almost exactly inside Borio's 8–20-year financial-cycle
band (1.1: avg ~16y) and the 10–20-year real-estate range (1.2), not in a longer band distinctly its
own. This is precisely why atlas row 1.3 already carries a **15–20-year** prior rather than the
literature's 30–40-year figure — CS1 is the desk earning that prior rather than assuming it, and the
honest number to carry forward is: **commodities move on the same decade-and-a-half-to-two-decade
clock as the rest of Band 1, roughly twice as often as "supercycle" language implies.**

**(v) CS2 — is there a common object at all? Breadth, tested.** A count-and-length failure does not
by itself mean there is no shared macro object underneath — it could mean the *label* is wrong
while a genuine common factor still moves many commodities together on a decade scale (the
demand-object claim A.3 develops). CS2 tests this directly: pairwise correlations of 10-year
log-changes across the Jacks panel's ~40 series, split into **within-group** pairs (both series
inside the same commodity family — e.g. two base metals, two grains) and **across-group** pairs
(spanning unrelated families — e.g. a metal against a soft, or an energy series against a grain).
**329 within-group pairs** return a **median +0.42**; **451 across-group pairs** return a **median
+0.30, with 89% of pairs positive**. Against the pre-registered bar (across-group median > 0 AND
≥50% positive), CS2 **PASSES**, and decisively — the fact that *unrelated* commodities (tin and
cocoa; copper and wheat) co-move positively at decade scale nearly nine times in ten is the honest
empirical content behind "supercycle" as a *breadth* claim, even where the specific turning-point
count and length the word usually implies does not survive CS1. **The word survives partially, not
wholesale**: there is a real, broad, decade-scale common factor (CS2); it does not organize itself
into 3–4 discrete 30–40-year arcs (CS1) so much as a shorter, more frequent rhythm shared with the
rest of Band 1.

**(vi) Prebisch-Singer — the trend the cycle oscillates around, not the cycle itself.** A separate,
older claim needs to be kept apart from the supercycle question entirely: **Prebisch, Raúl (1950)**
and **Singer, Hans (1950)**, independently, argued primary-commodity prices suffer **secular
deterioration** relative to manufactured goods — a one-way trend, not a cycle. The modern long-data
verdict, run with techniques built to distinguish trend from cycle rather than conflate them:
**Harvey, David I.; Kellard, Neil M.; Madsen, Jakob B. & Wohar, Mark E. (2010), "The Prebisch-Singer
Hypothesis: Four Centuries of Evidence"** (*Review of Economics and Statistics* 92(2): 367–377)
test 25 commodities from the 17th to 21st centuries, allowing for multiple endogenous structural
breaks, and find a **significant downward trend in roughly 11 of the 25 series** over all or part
of the sample — real, but **commodity-specific and break-laden**, not a uniform law, and small
relative to supercycle-scale swings at any investable horizon. **For our seat**: this is why H53's
design intent is explicitly a **cyclical state**, never a bet on secular deterioration — the two
claims answer different questions (where in a 15–20-year swing are we, versus is there a
multi-century downward drift under all these swings) and this chapter addresses only the former.

**(vii) Citations.** Erten, Bilge & Ocampo, José Antonio (2013), "Super Cycles of Commodity Prices
Since the Mid-Nineteenth Century," *World Development* 44: 14–30 **[Verified — turning-point years
per cycle VERIFY, network-blocked this session]**. Cuddington, John T. & Jerrett, Daniel (2008),
"Super Cycles in Real Metals Prices?," *IMF Staff Papers* 55(4): 541–565 **[Verified]**. Hamilton,
James D. (2018), "Why You Should Never Use the Hodrick-Prescott Filter," *Review of Economics and
Statistics* 100(5): 831–843 **[Verified — already CONTRACT §8's own citation]**. Prebisch, Raúl
(1950), *The Economic Development of Latin America and Its Principal Problems*, UN ECLA; Singer,
Hans W. (1950), "The Distribution of Gains between Investing and Borrowing Countries," *American
Economic Review* 40(2): 473–485 **[Verified — canonical joint attribution]**. Harvey, David I.;
Kellard, Neil M.; Madsen, Jakob B. & Wohar, Mark E. (2010), "The Prebisch-Singer Hypothesis: Four
Centuries of Evidence," *Review of Economics and Statistics* 92(2): 367–377 **[Verified]**.

---

### A.2 The mechanism, strongest form: capacity takes a decade — and what CS3/CS4 found when tested

**(i) The capex-lag mechanism, stated in full.** The strongest form of the supercycle mechanism is
a genuine capacity constraint, structurally identical in kind to the housing supply-lag argument
L12 already relies on (Glaeser-Gyourko-Saiz, fincycle-deep §A.3) but running on a much longer clock.
**Kydland, Finn E. & Prescott, Edward C. (1982), "Time to Build and Aggregate Fluctuations"**
(*Econometrica* 50(6): 1345–1370) formalized the general principle: when building productive
capital requires **more than one period**, investment decisions today are locked in and cannot
respond to information that arrives before the capital is finished — built for the US business
cycle broadly, not extraction specifically, but the mechanism (a multi-period, non-reversible
construction pipeline) is exactly what makes mine and oilfield development a textbook time-to-build
asset, at a far longer horizon than Kydland-Prescott's own quarterly calibration. **S&P Global
Market Intelligence's** own tracking of the mine-development
pipeline gives the current, verified magnitude: across **127 mines** studied, the average lead time
from **discovery** to **commercial production** is **15.7 years** (range 6–32 years), a figure that
has itself been **lengthening** — mines starting production in **2005–2009** averaged **12.7
years**; mines starting in **2020–2023** averaged closer to **18 years**. The bulk of that time sits
in exploration, permitting and studies (S&P Global attributes roughly 12 of a typical 16 years to
this leg); the **feasibility-to-first-production** leg specifically — the part that responds most
directly to a price signal, since the deposit is already known — runs a shorter **5–7 years** for
greenfield projects. Two verified individual cases anchor this concretely: **Escondida** (Chile,
BHP/Rio Tinto) was discovered in March 1981 (the "Pozo 6" borehole), construction began in 1988, and
first concentrate shipped in November 1990 — roughly **9–10 years discovery-to-production**, with a
**2-year** construction-to-first-shipment leg once the investment decision was made. **Oyu Tolgoi**
(Mongolia, Rio Tinto/Turquoise Hill) was discovered via its key drill hole in 2001, construction
began in 2010, and the first copper shipment left the mine on 9 July 2013 — roughly **12 years**
discovery-to-production, with a **3-year** construction leg. Oil megaprojects (deepwater, Arctic,
oil-sands) run on a comparable multi-year sanction-to-first-oil clock, though this chapter has not
independently re-verified individual project timelines this session and states that class of
evidence as a directional prior, not a re-derived figure.

**(ii) Investment-pipeline convexity — the choreography that turns a price signal into a glut.**
The mechanism's dangerous property is not the lag alone but its **convexity**: at low prices, almost
no one sanctions new capacity (returns don't clear the hurdle, and boards that got burned in the
last bust are risk-averse specifically about *this* capex class) — so a demand boom meets a supply
curve that is, for years, close to vertical. Prices spike, sanctioning decisions flip **en masse**
because everyone is reading the same price signal and the same peer behavior at the same time
(Kydland-Prescott's time-to-build plus an ordinary, undramatic coordination effect — no conspiracy
required, just correlated incentives), and because the *decision* leg is short relative to the
*build* leg, a wave of nearly-simultaneous sanctioning decisions matures into a wave of nearly-
simultaneous first production, years later, regardless of what demand is doing by the time it
arrives. This is the textbook capex-lag story, and it is why the literature ties commodity
supercycles to boom-bust capex more than to any single price-forecasting failure.

**(iii) Hotelling's rule, and why the data never behaved as it predicted.** **Hotelling, Harold
(1931), "The Economics of Exhaustible Resources"** (*Journal of Political Economy* 39(2): 137–175)
derives the canonical benchmark: under competitive extraction of a fixed, known stock, the
resource's **net price** (price minus marginal extraction cost) must rise at the **rate of
interest** — otherwise it pays to extract faster, or hold reserves longer. The empirical record has
never cooperated: real commodity prices have **not** shown the predicted exponential climb over any
century-scale window, and the literature's own diagnosis is directly relevant to H53's design —
**technology** (extraction cost falls faster than scarcity should allow) and **reserve growth**
(proven reserves expand with exploration and price-induced technology investment faster than
depletion draws them down, so the "fixed known stock" premise does not hold over investable
horizons). **For our seat**: Hotelling is why this chapter frames the mechanism as
**capacity-cycle**, not **depletion-arc** — reading a construction-lag oscillation around a cost/
technology trend that itself evolves, not a bet that resources are running out.

**(iv) Storage theory — Deaton-Laroque: explains the high-frequency spikes, explicitly not the
decade arc.** **Deaton, Angus & Laroque, Guy (1992), "On the Behaviour of Commodity Prices"**
(*Review of Economic Studies* 59(1): 1–23) fit the standard rational-expectations competitive-
storage model — inventory holders buy low and sell high subject to a non-negativity constraint on
stocks — to thirteen commodities, and find the pure IID-shock version of the model **cannot** match
the **high autocorrelation** actually observed in commodity prices; **Deaton, Angus & Laroque, Guy
(1996), "Competitive Storage and Commodity Price Dynamics"** (*Journal of Political Economy* 104(5):
896–923) fix this by allowing serially correlated supply/demand shocks. The mechanism this pair of
papers formalizes — storage smooths ordinary fluctuations but cannot smooth away a large enough
shock once inventories hit their floor, producing the price's characteristic asymmetry (long calm
stretches, occasional violent spikes when stocks run out) — is genuinely important, and genuinely
**a different clock** from A.1's decade-scale object: storage theory is built to explain
**month-to-month and year-to-year** price behavior (autocorrelation, spike timing conditional on
inventory levels), and says essentially nothing about *why* the multi-year capacity cycle in (i)–(ii)
exists at all. The desk keeps these two mechanisms explicitly separate rather than letting storage
dynamics quietly stand in for the capacity story — a stockout can *trigger* the price spike that
starts a capex wave, but it is the capex wave's own multi-year build time, not the stockout, that
sets the supercycle's clock.

**(v) Convenience yield, backwardation, and the futures-curve evidence — Keynes to Gorton-
Rouwenhorst to the post-2008 erosion.** **Keynes, John Maynard (1930)**, in *A Treatise on Money*,
proposed **normal backwardation**: because commodity producers are natural hedgers (short forward)
and speculators must be paid to take the other side, futures prices should sit **below** expected
future spot prices on average — a genuine risk premium, structurally distinct from the storage
mechanism above (it is about who bears price risk between now and delivery, not about physical
inventory dynamics, though the two interact through convenience yield — the value of holding the
physical good rather than the futures contract, which itself varies with the storage cycle).
**Gorton, Gary B. & Rouwenhorst, K. Geert (2006), "Facts and Fantasies about Commodity Futures"**
(*Financial Analysts Journal* 62(2): 47–68) test this on an equal-weighted commodity futures index,
July 1959–December 2004: fully collateralized commodity futures earned **equity-like returns and
Sharpe ratios** over the sample, **negatively correlated** with equity and bond returns, and
**positively correlated with inflation** — a genuine, diversifying risk premium, not a Hotelling-
style price-appreciation story, and the paper's own headline evidence for treating commodities as
an investable asset class rather than a pure macro read. **The honest complication, and the one
this desk's alpha-decay discipline (CONTRACT §5) requires stating plainly**: **Tang, Ke & Xiong,
Wei (2012), "Index Investment and the Financialization of Commodities"** (*Financial Analysts
Journal* 68(6): 54–74) document that as commodity-index investment grew rapidly through the 2000s,
non-energy commodity futures became **increasingly correlated with oil** and with each other —
"financialization" — most pronounced for commodities inside the popular indices, and a documented
contributor to the **2008 volatility spike**. The mechanism is the same one CONTRACT §5 already
names generically: a genuine risk premium, once packaged into a scalable, widely distributed index
product, draws in enough capital that the premium itself compresses and the correlation structure
that made commodities a diversifier degrades — **this is alpha decay, priced into an asset class
rather than a factor**, and it is the desk's own stated reason the futures-roll strategy is
explicitly **not harvestable** (A.5 below), independent of anything else in this chapter.

**(vi) CS3 — testing the mechanism's first leg: does a price boom actually predict the next
decade's capacity?** The strongest-form mechanism above makes a specific, testable prediction: a
decade of rising real price should be followed by a decade of rising production, as the capacity
sanctioned during the boom finally comes online. CS3 tests exactly this on the Jacks/Clio-USGS
panel — correlating each metal's 10-year log-change in real price against **the following**
decade's log-change in world production:

| Metal | corr(10y Δlog price, next-10y Δlog production) |
|---|---|
| Bauxite | +0.23 |
| Lead | +0.18 |
| Aluminum | +0.13 |
| Manganese | +0.11 |
| Copper | +0.11 |
| Silver | +0.06 |
| Zinc | −0.02 |
| Gold | −0.03 |
| Nickel | −0.08 |
| Iron ore | −0.09 |
| Tin | −0.27 |

Against the pre-registered bar (sign-consistency ≥70% positive across the metals panel), the result
is **55% positive — FAIL**, and not narrowly: the correlations that *are* positive (bauxite,
lead, aluminum, manganese, copper) sit in the +0.11 to +0.23 range — real, but modest — while tin
sits at a startling **−0.27**, and gold, nickel, iron ore and zinc show no reliable relationship at
all in either direction. **The honest read**: the price → next-decade-capacity leg of the textbook
mechanism is present for a subset of base/bulk metals (plausibly the ones with the shortest,
most price-responsive feasibility-to-production legs per (i)) but does **not** generalize across
the metals panel as a whole — this is a considerably weaker empirical foundation than the
mechanism's frequent citation in the sector-tilt/allocator literature would suggest.

**(vii) CS4 — testing the mechanism's second leg: does the capacity surge actually produce the
glut?** The mirror-image test — does a decade of rising world production predict the **following**
decade's real price **decline**, the "glut" half of the boom-bust story:

| Metal | corr(10y Δlog production, next-10y Δlog real price) |
|---|---|
| Nickel | −0.42 |
| Lead | −0.19 |
| Aluminum | −0.17 |
| Manganese | −0.10 |
| Copper | −0.10 |
| Zinc | −0.03 |
| Gold | −0.08 |
| Silver | +0.08 |
| Bauxite | +0.06 |
| Iron ore | +0.18 |
| Tin | +0.24 |

Against the same 70% sign-consistency bar (this leg predicts **negative**), the result is **64%
negative — FAIL**, but the closer miss of the two legs, and directionally coherent for the metals
where the underlying capacity-lag story is most physically plausible: nickel's **−0.42** is the
single strongest reading in either table, and lead, aluminum, manganese and copper all cluster in
the −0.10 to −0.19 range exactly where the "capacity finally arrives and prices give it back" story
predicts. Tin (+0.24) and iron ore (+0.18) run the wrong way, keeping the panel-wide bar unmet.

**(viii) What CS3/CS4 together mean for how this mechanism gets used.** Read together with A.1's
CS1/CS2 results, the honest synthesis is specific, not vague: **there is a real, broad, decade-scale
common factor across commodities (CS2 passes decisively)**, and **the capacity-arrives-and-prices-
give-it-back leg of the mechanism has real, if sub-bar, directional support, concentrated in the
industrial base metals (CS4 — close miss, right sign 64% of the time)** — but **the price-triggers-
next-decade-capacity leg does not clear even a lenient bar (CS3 — 55%, barely above a coin flip)**,
and neither leg is strong enough, individually or combined, to license the mechanism as a
**forecasting** tool: predicting *when* a price boom will translate into capacity, or *when* a
capacity surge will translate into a bust, is not something this program's own numbers support
doing. What survives is the mechanism as **narrative texture for a state variable that is built and
scored some other way** (A.5) — exactly the distinction CONTRACT §6 draws between an explicit
economic argument (real, worth keeping) and a fitted timing rule (not licensed by this evidence).

**(ix) Citations.** Kydland, Finn E. & Prescott, Edward C. (1982), "Time to Build and Aggregate
Fluctuations," *Econometrica* 50(6): 1345–1370 **[Verified]**. S&P Global Market Intelligence,
mine lead-time research series ("Discovery to production averages 15.7 years for 127 mines";
"From 6 years to 18 years: the increasing trend of mine lead times"; "Average lead time almost 18
years for mines started in 2020–23") **[Verified — S&P Global Market Intelligence published
research, headline figures cross-confirmed across multiple of the firm's own releases this
session]**. Escondida discovery/construction/production chronology (Utah International/Getty Oil
geochemical program from 1978; "Pozo 6" discovery hole, 14 March 1981; BHP/Rio Tinto Zinc/JECO/
World Bank JV formed 1985; construction from 1988; Los Colorados concentrator start-up and first
concentrate shipment, November 1990) **[Verified]**. Oyu Tolgoi discovery/construction/production
chronology (key discovery hole OTD-150, July 2001; construction from 2010; first copper shipment,
9 July 2013) **[Verified]**. Hotelling, Harold (1931), "The Economics of Exhaustible Resources,"
*Journal of Political Economy* 39(2): 137–175 **[Verified]**. Deaton, Angus & Laroque, Guy (1992),
"On the Behaviour of Commodity Prices," *Review of Economic Studies* 59(1): 1–23 **[Verified]**;
Deaton, Angus & Laroque, Guy (1996), "Competitive Storage and Commodity Price Dynamics," *Journal
of Political Economy* 104(5): 896–923 **[Verified]**. Keynes, John Maynard (1930), *A Treatise on
Money*, Macmillan **[Verified — canonical source for normal backwardation]**. Gorton, Gary B. &
Rouwenhorst, K. Geert (2006), "Facts and Fantasies about Commodity Futures," *Financial Analysts
Journal* 62(2): 47–68 **[Verified]**. Tang, Ke & Xiong, Wei (2012), "Index Investment and the
Financialization of Commodities," *Financial Analysts Journal* 68(6): 54–74 **[Verified]**.

---

### A.3 Demand side: why supercycles are demand objects — and how the atlas already commits oil to a different treatment

**(i) The China shock, 2001–2011, as the canonical modern driver.** If CS2 (A.1) establishes that a
broad, cross-commodity common factor genuinely exists, the natural next question is what drives it,
and the modern literature's answer is close to unanimous: **demand**, concentrated in one country's
industrialization. China's steel intensity of GDP followed the inverted-U (S-curve) pattern already
documented for Japan (1950s–1970s) and Korea (1970s onward) — rising steel consumption per unit of
GDP through heavy-industrialization and urbanization, declining once the built environment matures
and the economy shifts toward services [VERIFY: precise peak-intensity income threshold — secondary
academic review, not independently re-derived]. Crude steel production tracks this directly: from
roughly 32 million tonnes in 1978 to over **683 million tonnes in 2011**, near **9.7%/year**
compound growth — a scale of sustained industrial demand with no comparable precedent in this
panel's record, and the most frequently cited reason Erten-Ocampo's "fourth supercycle" and
Cuddington-Jerrett's "early fourth cycle" both close on the same country. Copper tells the same
story from the intensity side: China's copper intensity of GDP has itself already passed its peak
on current estimates, projected to decline from roughly **638 to 393 kilograms per US$1 million of
GDP** as the economy matures [VERIFY: precise figures — secondary academic source] — the S-curve's
downward leg, now underway, is itself a live, testable implication of this demand-object framing.

**(ii) Why supply-driven spikes are a different object entirely — and why the atlas already treats
oil this way.** A price spike driven by a **demand** boom (steel demand outrunning iron-ore
capacity) and a price spike driven by a **supply** shock (a wartime embargo, a sanctioned exporter,
an invasion) look identical on a raw price chart and have **opposite** portfolio implications for a
net-importing economy: a demand-driven boom raises India's import bill *and* its exporters' revenue
in roughly offsetting proportion to how exposed its own economy is to the same global growth impulse
(a genuine, if imperfect, natural hedge — the same growth that lifts commodity prices usually lifts
Indian goods and services demand too); a **supply**-driven spike raises the import bill with **no**
offsetting growth impulse at all — pure terms-of-trade damage, straight through to the current
account and the currency. This is precisely why atlas row 2.12 already commits the desk's oil
treatment to **Kilian's decomposition**, never a raw price level. **Kilian, Lutz (2009), "Not All
Oil Price Shocks Are Alike: Disentangling Demand and Supply Shocks in the Crude Oil Market"**
(*American Economic Review* 99(3): 1053–1069) decomposes oil-price variation into three structurally
distinct shocks — **oil supply shocks**, **shocks to global demand for all industrial
commodities** (the aggregate-activity channel this chapter's demand-object argument runs through),
and **precautionary demand shocks specific to the oil market** (fear of future supply disruption,
priced in before any physical shortage occurs) — and shows the three carry materially different
consequences for importing-economy macro aggregates, which is exactly why regressing anything on
the raw oil price alone produces the unstable, sign-flipping relationships the applied literature
has long struggled with.

**(iii) The design consequence: H53 does not duplicate L9's oil treatment, it generalizes its
logic.** The commodity supercycle's H53 seat is explicitly **not** a re-litigation of the oil
question atlas row 2.12 already settled — it is the same demand/supply-decomposition discipline
**extended to the broader metals-and-materials complex** CS2 shows moves together with oil at
decade scale. A metals/energy price move that is broad (many unrelated commodities up together,
CS2's own signature) and persistent (sitting at a high multi-year percentile, not a single-month
spike) reads as the demand-object case A.1–A.3 develop; a move confined to one or two commodities
with an identifiable supply-side trigger (an export ban, a mine strike, a conflict) reads as the
opposite case and should condition the desk's interpretation oppositely — this is a **state-read
discipline**, not a new indicator, and it is why H53's design intent explicitly frames the seat as
an **L9 enrichment** rather than a standalone regime layer: it adds interpretive texture to the same
terms-of-trade/CAD/INR channel L9 already carries, never a parallel budget.

**(iv) The dollar channel — priced by reference, not recomputed.** Commodities trade in
dollar-denominated markets, and the well-documented inverse dollar-commodity relationship (a weaker
dollar mechanically raises dollar-priced commodity values for non-dollar buyers, among several
compounding channels) is already this program's territory, carried in full by `research/cycles/
reserve-deep/` and `docs/cycles/06-reserve-currency.md` — this chapter does not re-derive it. **For
an INR-based desk specifically, the channel is double, not single**: a supercycle upswing
coinciding with **dollar weakness** compounds favorably for Indian import costs, while one
coinciding with **dollar strength** compounds unfavorably twice over — the same L9 dollar-cycle
state (atlas row 2.9) that already conditions the desk's FII/flow reading is the correct place to
read this interaction, which is why H53 names it an L9 enrichment rather than a standalone view.

**(v) Citations.** China crude steel production, 1978–2011 (secondary compilation citing NBS-based
figures) **[Verified in outline; precise annual series not independently re-pulled this
session]**. China steel-intensity and copper-intensity S-curve estimates **[VERIFY: precise
threshold and intensity figures — secondary academic sources]**. Kilian, Lutz (2009), "Not All Oil
Price Shocks Are Alike: Disentangling Demand and Supply Shocks in the Crude Oil Market," *American
Economic Review* 99(3): 1053–1069 **[Verified — already atlas row 2.12's own citation]**.

---

### A.4 The energy-transition metals thesis, honestly

**(i) The 2020s claim, given its strongest form.** The current cycle's version of the demand-object
argument is the electrification thesis: copper, lithium, nickel and cobalt demand from EVs, grid
build-out and renewables capacity is claimed to be structurally larger and more persistent than any
prior industrial-demand wave, arriving against a supply pipeline A.2's own 15–18-year discovery-to-
production lag cannot possibly clear in time. The **IEA's Global Critical Minerals Outlook** series
gives this claim its best-sourced current form: the **2024** edition finds announced mine-supply
projects meet only around **70% of projected 2035 copper demand** and roughly **50%** of projected
lithium demand under its scenario set; the **2025** edition, updating the gap, puts the implied
**2035 shortfall at roughly 30% for copper and 40% for lithium**. The investment side of the same
report is the honest complication even inside the bull case: **real** investment in critical-mineral
development (adjusted for cost inflation) grew only about **2%** in 2024, down from stronger growth
in 2023, exploration spending for nickel, cobalt and zinc specifically **declined**, and — the
sharpest tension in the whole picture — **prices for key energy-transition minerals fell through
2024–25** (lithium down over 80% from its 2023 level) even as the IEA's own supply-gap arithmetic
widened, meaning **today's price signal is not currently providing the investment incentive the
capex-lag mechanism (A.2) needs to close the gap it identifies.**

**(ii) The honest counter: every supercycle peak has generated exactly this literature.** The
desk's own posture requires stating the pattern-match plainly rather than treating this cycle's
claim as structurally different in kind. The **1970s–1980** peak generated its own "running out of
everything" literature (the Club of Rome's *Limits to Growth*-adjacent resource-scarcity narrative,
oil and metals together) immediately before two decades of real price decline. The mid-2000s boom
generated its own durable catchphrase — mining executives and sell-side commentary through roughly
2004–2008 routinely framed the China-driven demand wave as **"stronger for longer,"** the specific
claim that this cycle's demand growth was structural, not cyclical, and would not mean-revert the
way prior booms had [VERIFY: precise attribution/first use — widely associated with BHP
Billiton-era mining commentary of the period, exact coiner not independently confirmed this
session]. **Peak oil**, the supply-side cousin of the same instinct, dominated energy commentary
from roughly 2005 (The Oil Drum's founding; a Hubbert-linearization revival by geologists including
Colin Campbell and Jean Laherrère) through 2008 — killed within a decade by the **shale
revolution**: fracking and horizontal drilling, commercially proven from 2008, more than **doubled
US crude output between 2008 and 2018**, converting "unrecoverable" resource into proven reserves
faster than any 2005-era forecast admitted possible. The **2011** and **2021–2022** vintages of
"commodity supercycle" calls (Goldman Sachs flagged a renewed supercycle thesis in October 2020,
turned "extremely bullish" by January 2022, its commodities-research head projecting a
**decade-long** cycle) sit in the same lineage — and the **capex evidence from the previous
cycle's own peak is the sharpest available check on how such calls resolve**: **BHP's** capex ran
**US$20.2bn in FY2012** and **US$20.9bn in FY2013**; **Rio Tinto's** accelerated to **US$12.3bn in
2011** before falling to **under US$8.5bn by 2014** — both majors' spending peaked in the **same
12–24 months** the price cycle itself peaked, exactly the capex-lag mechanism's own prediction
(A.2ii), and exactly what a "stronger for longer" narrative cannot price in, because believing the
narrative is what produces the synchronized capex peak that then produces the glut.

**(iii) Substitution and thrifting — the recurring rebuttal, with a live 2020s instance.** Every
extended price spike also generates its own demand-side release valve, and both major 2020s
examples are already underway, not merely theorized. **Aluminum-for-copper substitution** in
electrical applications has direct historical precedent: the early-1960s North American housing
boom, facing a copper price spike, saw a first wave of aluminum building wire — a substitution that
initially went badly (connection failures led to new safety standards, then redesigned AA-8000-series
alloys) but that established the pattern: **manufacturers revisit the substitution every time copper
spikes, and retooling costs are what slow it, not economics**. Today's instance is already measured:
J.P. Morgan estimates aluminum substitution currently displaces roughly **2% of global copper
demand**, projected to reach **roughly 6% by 2030**. **LFP-for-NMC substitution** in EV battery
chemistry is the second live instance, and larger in magnitude: NMC held roughly **60%** of the
global EV battery market in 2022; by 2023 LFP had reached **roughly 40%** as NMC fell to about 50%,
and by 2024 LFP's share had risen further, to **roughly 40% of GWh globally** and **59% within
China** — a cost-driven shift (LFP cells running **$80–100/kWh** against NMC's **$100–130/kWh**)
that mechanically **removes nickel and cobalt demand** from a large, growing share of the
electrification curve the bull case in (i) is built on, while leaving lithium and copper intact.

**(iv) The desk's posture, stated once and held.** None of (i)–(iii) resolves whether the 2020s
electrification wave will, in the end, look more like a genuine structural break or another
"stronger for longer" instance that substitution and a capex response eventually deflate — and the
desk does not need to resolve it, because H53's design intent never asks the seat to. This section
exists as **context for sector tilts under H53**, feeding the metals/mining and energy/OMCs sector
projections atlas §14 already maps (row: "Metals/mining: commodity supercycle (H53) + China (H54) —
pure projection"), and it is never permitted to become a **date claim** — no "the shortage arrives
by 20XX," no sizing decision that depends on the bull case resolving in a particular direction
within a particular window. The honest, load-bearing takeaway carried forward to A.5 is narrower and
more useful: the bull case gives the desk a reason metals/energy sector tilts should have *some*
mechanism-backed upside asymmetry when the state variable reads elevated-and-broad (CS2's own
signature); the "every peak generates this literature" counter-history gives the desk an equally
mechanism-backed reason that asymmetry should never be read as a standing structural tilt, and
should decay exactly like every other signal in this program once the state itself mean-reverts.

**(v) Citations.** IEA, *Global Critical Minerals Outlook 2024* and *Global Critical Minerals
Outlook 2025*, International Energy Agency **[Verified — headline supply-gap and investment
figures directly reported by the IEA's own published executive summaries, cross-confirmed across
multiple secondary reports this session]**. Peak-oil chronology (The Oil Drum, founded 2005;
Hubbert-linearization revival, Campbell & Laherrère; shale/fracking commercial proof from 2008; US
crude output roughly doubling 2008–2018) **[Verified]**. BHP capital expenditure, FY2012–FY2013;
Rio Tinto capital expenditure, 2011 and 2014 **[Verified — company-reported figures via SEC/company
filings, cross-confirmed this session]**. Goldman Sachs commodity-supercycle research calls, October
2020 and January 2022 **[Verified — reported via Bloomberg and Goldman Sachs' own published
research]**. Aluminum building-wire substitution history (early 1960s) and current substitution
share (~2% of global copper demand, ~6% projected by 2030, J.P. Morgan estimate) **[Verified]**.
LFP/NMC EV battery chemistry market-share figures, 2022–2024 **[Verified — cross-confirmed across
IEA Global EV Outlook 2023, Adamas Intelligence, and industry-tracker figures this session]**.
"Stronger for longer" phrase **[VERIFY: precise attribution/first use]**.

---

### A.5 What the desk can and cannot harvest

**(i) H53's design intent, restated against what A.1–A.4 actually found.** Atlas row 1.3 frames
H53 as **context + sector-tilt conditioner + L9 enrichment**, Tier C until researched — and CS1–CS4
are that research. The verdict across four pre-registered trials is neither a clean pass nor a
clean rejection, and the honest composite is: **a real, broad, decade-scale common factor exists
(CS2 PASS)**; **its specific "3–4 supercycles at 30–40 years" periodicity does not survive a
real-time-honest turning-point test — the aggregate instead turns over roughly every 15–21 years,
median 18, matching Band 1's own financial- and real-estate-cycle length rather than a longer band
of its own (CS1 FAIL)**; **the textbook price→capacity leg of the mechanism is weak and not
sign-consistent across the metals panel (CS3 FAIL, 55%)**; **the capacity→glut leg is directionally
right but falls short of the pre-registered bar (CS4 FAIL, 64% against a 70% bar)**. This is a
genuinely weaker empirical foundation than "commodity supercycle" carries as a piece of financial-
market vocabulary — and it is precisely the honest foundation Tier C, and Tier C alone, is built for:
narrative-grade evidence that may **reduce** risk, never add it (CONTRACT §4).

**(ii) What a STATE looks like — never a date.** The harvestable object is a **level-and-momentum
state**, built the same way L12's own composite is built (fincycle-deep §A.5iv): an **expanding-
window percentile** of a broad real commodity price aggregate (the World Bank Pink Sheet real index
is the atlas's own named free, continuously updated series for the live construction going forward;
the Jacks/Clio-USGS/IMF-PCPS panels this chapter's trials ran on supply the historical depth needed
to test the mechanism, not the going-forward feed) plus an **impulse** term — how fast the
percentile has moved over the trailing window, capturing CS2's breadth signature (a genuine
common-factor move shows up across many unrelated series at once; an idiosyncratic single-commodity
move does not) without ever asking the state to name which numbered "supercycle" the desk is
supposedly inside. No peak-calling, no trough-calling, no claimed date for when the state turns —
CS1's own result forecloses that use as firmly as FC3 forecloses peak-dating for L12 (fincycle-deep
§A.5iv), for the identical reason: a tool that cannot locate the historical turning points reliably
after the fact has no business claiming to locate the next one in real time.

**(iii) The consumers — where the state's reading actually lands.** Per atlas §14's own sector-
projection principle, the state has two direct homes and one enrichment role, **never a standalone
allocation**. **Sector projection**: metals/mining and energy/OMCs are, per the atlas's own table,
"pure projection[s]" of this state (plus H54's China-credit-impulse candidate for metals/mining
specifically) — an elevated, broad reading conditions those sectors' relative tilt inside the
existing sector-exposure framework, with A.4's substitution evidence as the explicit reason that
tilt should never be sized as a standing structural overweight. **L9 enrichment**: the India-
transfer channel (terms-of-trade, CAD, INR pressure for a net-importing economy — atlas row 1.3's
own framing) reads the state alongside L9's existing dollar-cycle and (candidate) China-impulse
inputs, per A.3's demand/supply-decomposition discipline — a broad, demand-led elevated reading
reads differently from a narrow, supply-shock-driven spike, and the state's job is to help make that
distinction, not to move the L9 budget on its own. **Hedge-scheduling interplay**: an elevated,
persistent commodity state that coincides with INR pressure is exactly the kind of macro
confirmation the desk's existing hedge-ratio sweep (CONTRACT §3, the 7-point 0–150% grid, swept
jointly with regime per §9's deflated-Sharpe discipline) is built to condition on — again a reading
that feeds an existing mechanism, never a new one.

**(iv) What is explicitly not harvestable, stated as plainly as the futures-roll case.** Three
things this chapter's own evidence rules out directly. **Futures roll strategies** — Tang-Xiong's
own financialization finding (A.2v) is this program's stated reason the collateralized-roll-yield
premium Gorton-Rouwenhorst documented pre-2004 has compressed as index capital arrived; CONTRACT
§5's own decay-survival test (why does this signal survive being known?) has no honest answer for a
strategy built on a premium the literature itself documents eroding, and it is not proposed here.
**Physical storage plays** — Deaton-Laroque's own mechanism (A.2iv) is a professional storage/
convenience-yield business running on inventory data, financing costs and physical logistics this
desk has no edge in and no data feed for; it is explicitly a different clock from the one H53 reads
and is not proposed here. **Timing supercycle turns** — CS1's own result (i above) is the direct,
first-party reason: a method that cannot reliably locate the historical turning points on 150 years
of data with the benefit of hindsight has no basis for claiming it can locate the next one without
it. H53 remains, and should remain, exactly what atlas row 1.3 named it before CS1–CS4 ever ran:
**context, a sector-tilt conditioner, and an L9 enrichment — Tier C, reduce-only until a
purged-cross-validated test earns it more.**

---

## PART G — Operator psychology

Part A's honest finding — a genuine, broad, decade-scale common factor (CS2) whose specific
periodicity and mechanism legs mostly do not clear this program's own pre-registered bars (CS1, CS3,
weak-CS4) — is, if anything, a *harder* psychological object to sit with than a clean confirmation
or a clean rejection would have been. A clean confirmation would license conviction; a clean
rejection would license indifference. What CS1–CS4 actually deliver is a real signal, weaker and
shorter-cycled than its own name implies, sitting inside a desk whose home economy is structurally
on the losing side of every upswing this state reads as elevated. That combination — genuine
mechanism, honestly modest statistical support, and a desk with a non-neutral stake in which way
the reading goes — is exactly the setup this Part exists to map.

### G.1 Extrapolation at peaks — the desk's own citation list is also its own warning list

**Mechanism.** A.4's historical review is, read a second time, a catalogue of one repeating failure:
**"stronger for longer"** (mid-2000s mining commentary, claiming a demand wave was structural, not
cyclical); **peak oil** (2005–2008, killed within a decade by shale); the **2011** and **2021–2022**
"commodity supercycle" vintages, the second complete with a sell-side commodities-research head
projecting a **decade-long** cycle in January 2022. Each shares the same structure: real short-run
evidence (a genuine demand shock, a genuine capacity constraint) extrapolated past what the evidence
supports, exactly when high current prices and media saturation make extrapolation most compelling
and least justified — the general finding behind why trend-following works at intermediate horizons
and fails at long ones, applied here to a narrative rather than a price series.

**Countermeasure.** H53's construction (A.5ii) makes extrapolation structurally harder to act on
than it would be in a discretionary read: the state is an **expanding-window percentile plus
impulse**, re-estimated mechanically at every observation, never a narrative the desk authors and
then defends. A percentile cannot be talked into "this time is different" — it reports where the
current reading sits against its own full history, full stop, and CS1's own result (the aggregate
turns over roughly every 15–21 years, not 30–40) is itself now part of the desk's institutional
memory specifically so that the next "decade-long supercycle" narrative gets read against a shorter,
better-tested prior than the literature's own headline number would supply.

### G.2 Producer-side herding — sovereign budgets are procyclical by default; Chile is the
disciplined exception, not the rule

**Mechanism.** Commodity-exporting governments face the same capex-convexity problem A.2ii
describes for mining companies, at sovereign scale: royalty and tax revenue rises with the price,
spending commitments (and political pressure to spend) rise with revenue, and — because spending
commitments are far stickier downward than revenue — a budget built around a cyclically elevated
price becomes a fiscal crisis the moment the state mean-reverts. **Chile's structural balance rule**
is the desk's own best-documented counter-example, worth naming precisely because it is the
exception, not the norm: adopted in 2001 on a copper stabilization fund dating to the late 1980s,
the rule computes a **structural** fiscal balance using a **10-year copper price** and a trend-GDP
estimate set by **independent expert panels insulated from the political process** — between
**2003 and 2007**, when real copper prices rose **220%**, Chile's structural balance averaged a
modest **1.1% of GDP** even as its **effective** surplus ran **4.2% of GDP**, banking the windfall
rather than spending against it; the accumulated buffer then funded a **2.8%-of-GDP** countercyclical
stimulus in 2009 [VERIFY: exact stimulus composition — secondary IMF/IDB sourcing]. **Frankel,
Jeffrey A. (2011), "A Solution to Fiscal Procyclicality: The Structural Budget Institutions
Pioneered by Chile"** is the academic case study, and its lesson is the one worth carrying: the
rule works **because it removes the discretionary decision**, not because Chilean policymakers are
more disciplined than commodity-exporting peers — most of whom spend the windfall as it arrives and
face the adjustment when it reverses.

**Countermeasure.** For this desk, the relevance is not fiscal (India is a net importer, not a
commodity-revenue government) but **structural**: H53 is built the same way Chile's rule is —
mechanical, expanding-window, explicitly designed to prevent a discretionary read from overriding it
in the moment prices are most extreme. The producer-herding lesson generalizes directly: **any**
actor whose near-term incentives are strongest exactly when the state is most extended (a producer
government facing a windfall; an analyst facing a strong recent trend; a desk facing pressure to
call the next leg) needs the decision removed from the moment it would be hardest to make well — the
same design principle fincycle-deep's Part G names for L12 (G.1–G.5 there), applied here to a
different set of actors on the other side of the same trade.

### G.3 The analyst's asymmetric-loss problem

**Mechanism.** Calling a supercycle that does not materialize costs an analyst a quiet, forgettable
embarrassment — one call among many, correctable next quarter. **Missing** a genuine supercycle —
staying cautious through a multi-year commodity boom everyone else called correctly — is a
career-defining, visible, repeatedly-referenced failure, disproportionate to the actual forecasting
error involved. **Scharfstein, David S. & Stein, Jeremy C. (1990), "Herd Behavior and Investment"**
(*American Economic Review* 80(3): 465–479) formalizes exactly this asymmetry as a reputational
model: an agent concerned with being perceived as a skilled forecaster rationally prefers to **fail
conventionally** (miss the same way everyone else misses) over **failing unconventionally** (being
right alone, or wrong alone) — because reputational damage from an unconventional wrong call is far
larger than from a conventional one, the equilibrium is herding on the consensus view regardless of
private information to the contrary. Applied to commodity supercycle calls specifically: once a
critical mass of sell-side and buy-side commentary has called "supercycle," the individually
rational move for any single analyst is to call it too, independent of the analyst's own read of the
underlying evidence — which is precisely how "stronger for longer" and "decade-long supercycle"
become consensus phrases at the exact moments A.4's own historical review shows they were least
reliable.

**Countermeasure.** This program's own register already carries the structural antidote, stated in
`research/register/heuristics-lane.md`'s judging convention: candidates are graded by **"sign-
consistency across decades/regimes... not t-stat maximization"** — precisely the discipline CS1–CS4
applied to H53 itself, with FAIL verdicts on the periodicity claim and both mechanism legs, delivered
and recorded regardless of what consensus commentary was saying about commodities when the trials
were pre-registered. A desk whose promotion criterion is a written, pre-registered sign-consistency
bar rather than "does this match what everyone else believes" has no reputational cost to reading a
FAIL as a FAIL — the asymmetric-loss problem Scharfstein-Stein describes requires a discretionary
call to bite on; a mechanical bar removes the call.

### G.4 Anchoring on nominal prices — the oil "$100" (and "$140") problem

**Mechanism.** Round, salient nominal price levels ("$100 oil," "$4 copper," "$2,000 gold") become
psychological reference points independent of what they mean in real, inflation-adjusted terms — the
general anchoring mechanism (Tversky-Kahneman) applied to a recurring commodity-market habit.
Brent's **nominal** all-time high, **$147.50 on 11 July 2008**, is worth roughly **$210 in 2026
dollars** — so a "$140 oil" headline in any year after 2008 (including the March 2022 post-invasion
spike to **$139**, widely reported as "the highest since 2008") describes a materially **smaller**
real shock than the number alone suggests, and a desk anchored on the nominal figure will
systematically overstate how extreme a level actually is relative to history. The failure compounds
for percentile-based construction specifically **because** anchoring operates on the headline
number, not on the percentile the state actually reports — an operator who has internalized "$100
oil is expensive" from one decade can misread a state correctly showing that same nominal level at
a moderate real-terms reading a decade later.

**Countermeasure.** H53's construction is real-terms by design (A.5ii: a real commodity price index,
percentile-scored against its own expanding history) — the anchoring bias has structurally nothing
to attach to, because the state variable never surfaces a nominal price level to the desk at all,
only where the real, inflation-adjusted reading sits against its own history. This is the same
discipline the debt-deep and fincycle-deep monographs already document for money illusion and
"property never falls" respectively (G.2 in each): a mechanical, real-terms, expanding-window
computation has no surface for a nominal-anchoring bias to land on.

### G.5 The desk's own trap: net-importer motivated reasoning, and the guards already in place

**Mechanism.** This is the trap specific to this desk that none of G.1–G.4 fully capture, and it
deserves to be named without euphemism. Every reading this state variable produces has a
**second-order consequence for the desk's own book**: an elevated commodity state is bad news for a
net-importing economy (worse terms of trade, CAD pressure, INR risk — A.3, A.5iii) and, read purely
as macro context independent of the sector tilt it also feeds, an operator whose broader analytical
priors are optimistic about India's growth story has a quiet incentive to **read the state as lower,
or more transient, than the mechanical computation would show** — not through conscious bias, but
through the ordinary human tendency to scrutinize unwelcome readings harder than welcome ones,
demand more confirmation before accepting them, and reach for the substitution/thrifting counter-
argument (A.4iii) a beat too readily whenever the state happens to be elevated. The mirror-image
version — reading the state as more elevated and more threatening than warranted, because a
commodity scare makes for a more compelling risk narrative to defend a cautious stance — is equally
live and equally unexamined if left to discretion. **Rooting for low commodities, because the desk's
home economy benefits from low commodities, is a motivated-reasoning risk that sits inside the state
read itself, not just inside the sector tilt it produces.**

**Countermeasure — what CONTRACT and the register already provide, made concrete for this seat.**
Four structural features remove this decision from the moment it would be hardest to make honestly,
none written for H53 specifically but all binding on it. **(1) Tier-C reduce-only** (CONTRACT §4):
whatever the desk's own priors about India's growth story, H53 is **structurally incapable of
adding risk** — it can only trim exposure, never add it, so the optimistic-reading failure mode
(waving away an elevated state to protect a bullish India view) cannot smuggle *additional* risk
into the book even if the read itself is biased; the worst it can do is fail to trim risk that
should have been trimmed, a strictly bounded failure next to what an EDGE-tier seat would risk.
**(2) Pre-registration, already exercised**: CS1–CS4 were specified, including their pass/fail
bars, before they ran (`commodities-RESULTS.md`'s own header: "pre-registered... before this ran;
interpretation written AFTER the print") — the desk cannot read the state as more or less elevated
after seeing which reading is convenient, because the construction and its thresholds were fixed
first. **(3) Sign-consistency bars over t-stat maximization** (`research/register/
heuristics-lane.md`): the same discipline G.3 names against consensus-chasing works equally against
home-bias reasoning — a bar written as "≥70% sign-consistent across the metals panel" has no slot
for "except when inconvenient for our other views." **(4) The seat's home is fixed by design, not
mood**: A.5iii names exactly where a reading lands (sector projection, L9 enrichment, hedge
scheduling) before any particular reading exists — an operator cannot quietly reroute an
inconvenient reading away from the hedge-scheduling interplay it is supposed to inform, because the
routing was specified in the design chapter, not decided fresh each time the state moves.

### G.6 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Extrapolating a boom into "this time it's structural" | Repeated historical pattern: stronger-for-longer (2000s), peak oil (2005–08), supercycle calls (2011, 2021–22) — each a real short-run signal over-extended past its evidence | Mechanical expanding-percentile-plus-impulse construction; CS1's own 15–21y (not 30–40y) finding now part of institutional memory against the next decade-long-cycle claim |
| Producer-style procyclical spending against a windfall read as permanent | Sovereign/corporate incentives strongest exactly when the state is most extended (capex-convexity, A.2ii); Chile's structural rule is the documented exception, not the norm | Same design principle as Chile's rule: the read is mechanical and expanding-window, removing the discretionary decision from the moment it is hardest to make |
| Herding into consensus "supercycle" calls to avoid the asymmetric cost of missing one alone | Scharfstein-Stein reputational herding: unconventional wrong calls cost more than conventional ones, so agents herd regardless of private signal | Register's sign-consistency-over-decades bar (heuristics-lane.md), already applied to H53 itself with recorded FAIL verdicts on CS1/CS3/CS4 independent of prevailing commentary |
| Anchoring on nominal price levels ("$100 oil," "$140 oil") | Tversky-Kahneman anchoring on salient round nominal figures; 2008's real peak (~$210 in 2026 terms) dwarfs 2022's nominal-comparable $139 | Real-terms, percentile-scored construction by design — no nominal price level ever surfaces to the desk as the state's own reading |
| Reading an elevated commodity state as lower/more-transient than computed, because the desk's own priors favor a benign-import-bill story (or the mirror-image: reading it as more threatening than computed, to justify caution) | Net-importer motivated reasoning: every reading has a second-order consequence for the desk's own book, on both sides of a bullish or bearish India prior | Tier-C reduce-only ceiling bounds the damage of either bias; pre-registration (already exercised on CS1–CS4) fixes the read before the convenient interpretation is known; fixed routing (sector/L9/hedge) prevents ad hoc rerouting of an inconvenient reading |

None of these five countermeasures asks the operator to be more disciplined in the moment than
Part A's own evidence justifies. Each converts a live judgment call — decide whether this boom is
finally the structural one, decide whether to spend against a windfall that might reverse, decide
whether to be the lone cautious voice against a consensus supercycle call, decide whether "$140 oil"
is really as extreme as it sounds, decide whether an inconvenient elevated reading deserves the
scrutiny a convenient one would not get — into a structural non-decision, made once, in the
pre-registered trial and the tier assignment, before the moment that would have made it hardest.

---

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in). 2026-09-01. v1.0.
