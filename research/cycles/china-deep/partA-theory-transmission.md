# China Credit Impulse Deep Dive — Part A & Part G

Part A: Theory and transmission — the policy pulse an importer reads twice · Part G: Operator
psychology · v1.0 · 2026-09-02 · Atlas entry 2.11 (`docs/CYCLE_ATLAS.md` row 87, Band 2 — the
business-credit band); candidate **H54** (`docs/CYCLE_ATLAS.md` §8, row H54) — an **enrichment
input to L9** (`config/ladder.yaml`, `L9_global_financial_cycle`, `global_cycle` block, 20% of
regime-score budget), never a standalone ladder seat and never a separate budget line: the same
"measurement enrichment, no new seat" treatment the atlas already gives H53's terms-of-trade state
and the REER-stretch percentile (`docs/CYCLE_ATLAS.md` §15–§16). Complements, never duplicates:
`research/cycles/globalcycle-deep/partA-theory-psychology.md` (the L9 monograph this candidate
would feed — its dollar/VIX/US-real-rate triad, Kilian oil decomposition, and GF1–GF3 results are
inherited wholesale, never re-derived here); `docs/cycles/01-credit-cycle.md` (the L10 credit-
cycle monograph, whose own §7 China case — the largest credit boom in the JST-comparable record,
still unresolved as of 2026 — is cited by reference for the *balance-sheet* object this chapter's
*flow* object is explicitly not); `docs/cycles/17-shadow-credit.md` (the shadow-credit monograph's
own B8, China's trust/WMP mirror case and the 2018 asset-management rules — cited, never
re-derived); `docs/cycles/14-commodity-supercycle.md` (the commodity-supercycle monograph, whose
case 5 — China 2001–2011 — is this chapter's best-documented instance of the demand engine
described in A.2, and whose own §C.6 records the BIS-blocked, no-usable-GitHub-mirror data reality
this chapter's A.4 inherits rather than re-litigates). Evidence base: this file plus
`research/register/trial-ledger.md` (entries **CI1a–CI1b**, pre-registered and run 2026-09-02,
cited with their actual results below) and this program's own
`research/cycles/china-deep/china-RESULTS.md` and `research/cycles/china-deep/partCDEFH.md` (data
engineering, mathematics, algorithm and harvest-ledger — sibling parts to this file, cited by
reference for the runsheet and design items this Part does not re-litigate). Cases — the pulse
chronology since 2008 — are a sibling document (Part B) not yet drafted at this pass; this file
cites headline facts the atlas and this program's own commodity/credit/shadow monographs already
establish, and never invents episode detail belonging to that chapter. Style and depth calibrated
to `research/cycles/fincycle-deep/partA-theory-psychology.md`. Author: Claude (research agent) for
Ionic quant desk (principal: gaurav@ionic.in). Date: 2026-09-02.

This file assumes the ladder's frozen posture as given (`research/CONTRACT.md` §4): Tier-C
candidates may only reduce risk, and H54 has not yet earned even that seat — it is a **researched
hypothesis**, not a ladder entry, until a pre-registered incremental test runs on data this desk
does not yet hold (A.3–A.4). Part A supplies the theoretical object, its transmission machinery,
and an honest ranking of India's exposure channels; Part G turns to the desk reading a policy
instrument from an administratively managed economy that has every reason not to want this desk
reading it cleanly.

---

## PART A — Theory: a policy pulse, read through someone else's window

### A.1 The object

**(i) Definition, precisely.** The "China credit impulse" is not the level of Chinese credit, nor
even its growth rate — it is the **change in the flow** of new credit as a percentage of GDP: if
`F_t` is new credit extended during period `t` and `Y_t` is nominal GDP, the *flow* ratio is
`F_t/Y_t`, and the **impulse** is `I_t = (F_t/Y_t) − (F_{t-1}/Y_{t-1})`, a **second derivative** of
the credit stock (the stock's first derivative is the flow; the impulse is the flow's own
derivative). **Biggs, Michael; Mayer, Thomas & Pick, Andreas**, "Credit and Economic Recovery:
Demystifying Phoenix Miracles" (SSRN, posted 15 March 2010; an earlier 2009 De Nederlandsche Bank
working-paper version is referenced in the secondary literature as DNB Working Paper No. 218)
**[Verified — SSRN abstract_id=1595980; DNB-2009 antecedent corroborated by secondary citation,
exact title match across the two versions not independently confirmed this session — VERIFY]**
introduce the construction to explain "creditless" and "credit-fueled" recoveries: their finding,
stated in the paper's own terms, is that GDP growth depends on whether the *flow* of new borrowing
is accelerating or decelerating, not on the *level* of debt outstanding — a country can carry a
large, stable stock of credit and still see growth stall the moment new lending stops
*accelerating*, because the flow itself (not merely its existence) had been adding to demand. The
metaphor is literal: an "impulse" in physics is a change in momentum, not momentum itself, and the
object here inherits exactly that acceleration-not-velocity reading. The specific, China-labelled
popularization of this construction — most visibly the market-media **Bloomberg China Credit
Impulse Index**, built from new aggregate financing as a share of GDP and cited routinely across
sell-side and data-aggregator commentary (MacroMicro, TS Lombard, Bloomberg's own "China Credit
Tracker" graphics page) as a leading indicator running some six to twelve months ahead of China's
manufacturing cycle **[Verified — the index's existence and general construction via secondary
aggregator citation (MacroMicro, market commentary); Bloomberg's own primary methodology note was
not independently located this session — VERIFY]** — is widely credited to sell-side China
strategists working in Biggs's own analytical lineage, with **UBS** repeatedly named in market
commentary as an early, prominent house applying the construction specifically to China
**[VERIFY: a precise first-note attribution (author, house, date) for the China-specific
application was not located this session; the underlying credit-impulse concept's attribution to
Biggs-Mayer-Pick is solid, its *China popularization's* exact provenance is not]**. None of this
attribution detail changes the object itself, which this chapter treats as settled: a flow-of-flow
construction, not a level or a gap.

**(ii) Why an impulse, not a gap, for this specific object.** L10's own anchor construction
(`config/ladder.yaml`, `L10_credit_block`; `docs/cycles/01-credit-cycle.md`) is a **gap**: bank+NBFC
credit divided by nominal GDP, Hamilton-filtered against its *own* trailing trend, asking whether
the **stock** of credit relative to the economy sits unusually high or low — the right question for
a slow-building balance-sheet imbalance whose crash risk accumulates over years (Schularick-Taylor's
own +1σ-credit-growth-⇒-+2.8pp-five-year-crisis-probability finding, already the ladder's own
citation for L10). China's own credit *stock* is exactly this kind of object at the decade scale —
non-financial-sector debt/GDP roughly doubling from ~135% (2008) to ~269% (2020) and standing near
~296% as of Q3 2025, the largest credit boom in the JST-comparable historical record, per the
credit-cycle monograph's own §7 case, cited here by reference and not recomputed. But atlas row
2.11's own object is different in kind: a **~3–4-year policy pulse**, not a multi-decade balance-
sheet arc, and a gap construction applied at that frequency would smear a sequence of discrete,
Beijing-engineered easing-and-tightening decisions into a single, slow-moving stock reading that
never resolves into anything the desk could act on inside its own rebalancing cadence — precisely
the credit-cycle monograph's own honest caveat about its China case (§7): an administratively
managed system's *stock* keeps climbing in one direction for years without producing the
market-discovered peaks and troughs the gap machinery is built to date. The impulse construction
instead asks the frequency-matched question — is the *flow* of new financing accelerating or
decelerating *right now*, relative to a year ago — which is exactly what tracks a discrete easing or
tightening decision's transmission into real activity over the next two to four quarters, the
window Biggs-Mayer-Pick's own recovery-prediction exercise targeted and the window this chapter's
A.2 needs. H54 therefore sits in the same atlas Band (2, the 3–11-year business-credit band, beside
L10's own 7–11-year credit cycle) while running at a materially faster clock — a reminder, worth
stating plainly, that table position by band is an organizing convenience, never a claim that two
neighboring rows share a mechanism or a frequency.

**(iii) The aggregate: Total Social Financing / AFRE, and why its own composition moves under
foot.** The People's Bank of China began publishing **Total Social Financing (TSF)** — now also
styled **Aggregate Financing to the Real Economy (AFRE)** in the PBoC's own English releases
**[VERIFY: exact date of the AFRE relabeling]** — in **November 2010**, precisely to capture credit
creation the earlier bank-loan-only aggregates were missing as shadow intermediation grew
**[Verified — PBoC official history, corroborated across secondary sourcing]**. TSF/AFRE is a
flow aggregate covering RMB loans, foreign-currency loans, entrusted loans, trust loans,
undiscounted bankers' acceptances, corporate bond financing, local-government special-purpose
bonds, and domestic equity financing by non-financial firms — a genuinely broad measure, and the
correct denominator for the impulse construction precisely because its component list is not
stable. The shadow-banking legs (entrusted loans, trust loans, undiscounted bankers' acceptances)
rose to roughly **30% of funds raised by non-financial corporates by 2013** at their peak, then show
a recorded, multi-year **contraction from 2018 onward** — the direct consequence of the **27 April
2018** joint PBoC/CBIRC/CSRC/State Administration of Foreign Exchange "Guiding Opinions on
Regulating the Asset Management Business of Financial Institutions," which banned implicit
guarantees on newly issued wealth-management and trust products **[Verified — the shadow-credit
monograph's own B8, `docs/cycles/17-shadow-credit.md`, documents this episode in full: the rule
date, the joint-regulator authorship, and the Evergrande WMP web it eventually helped unwind;
cross-referenced here, never re-derived]**. A second, distinct composition shift ran alongside it:
a **2015–2018 local-government bond-swap program**, sized around **RMB 18 trillion (≈25% of 2015
GDP)** with roughly **RMB 15 trillion** of debt-swap bonds actually issued, converted local-
government-financing-vehicle (LGFV) bank debt, non-bank debt, and LGFV bonds into formal local-
government bonds **[Verified — IMF Working Paper WP/18/219; Reserve Bank of Australia, June 2019
bulletin]**. Both episodes moved large stocks of credit **between** TSF's own component buckets —
shadow to bank-and-bond, LGFV-loan to government-bond — without that credit leaving the system,
which is exactly why any impulse construction built on a *sub-component* of TSF (loans only, or
shadow only) rather than the full aggregate risks mistaking a regulatorily engineered migration for
a genuine deceleration. Part G's own §G.3 returns to this as a live Goodhart hazard rather than a
closed historical footnote; this chapter's own eventual construction (A.4) is written to consume
the **full** TSF/AFRE total for exactly this reason.

---

### A.2 The policy-credit machinery

**(i) Why China's credit is a policy instrument, not a market outcome.** Every mechanism L10 reads
for India — bank risk appetite, borrower demand, collateral value — exists inside China's system
too, but overlaid with direct administrative levers with no close Indian analogue. **Window
guidance** is the clearest: the PBoC communicates target lending quotas, pace, and sectoral
direction directly to commercial banks as "moral suasion" rather than binding law, and compliance is
close to universal in practice — a mechanism the literature attributes partly to Communist Party
hierarchy itself (the PBoC governor's own Party rank sits above individual bank heads', a
structural feature market-economy central banks simply do not have) **[Verified — window guidance's
existence and general operation via multiple academic secondary sources (HKIMR, comparative
central-banking literature); the precise hierarchy claim is corroborated across several secondary
accounts but not independently confirmed against a primary PBoC organizational document this
session — VERIFY]**. This means a China credit *deceleration* can be a **choice** — banks told to
slow lending to a specific sector, or an economy-wide quota tightened — in a way a deceleration in
India's own bank+NBFC aggregate essentially never is (L10's own India construction reads an
emergent outcome of decentralized lender and borrower decisions, not a quota).

**(ii) The PBoC's own toolkit.** The **reserve requirement ratio (RRR)** is the workhorse: a cut
releases liquidity permanently and directly (each 50-basis-point RRR cut is commonly estimated to
free on the order of **RMB 1 trillion** **[VERIFY: this figure recurs across market commentary but
was not traced to a specific PBoC or BIS primary statement this session]**), historically used to
sterilize foreign-exchange inflows and, in the easing-pulse era this chapter concerns itself with,
used repeatedly and visibly as the PBoC's most direct lever — RRR cuts are the announcement the
market-narrative cycle (Part G) watches for at every Politburo-adjacent meeting. Since **17 August
2019**, the PBoC has run a reformed **Loan Prime Rate (LPR)** mechanism: eighteen quoting banks
submit LPR bids linked to the **medium-term lending facility (MLF)** rate plus a spread, at one-year
and (from 2019) over-five-year tenors, replacing the older benchmark lending rate as the reference
for new bank loans **[Verified — PBoC 17 August 2019 announcement; Reserve Bank of Australia,
November 2019 Statement on Monetary Policy, Box A]**. This reform matters for how this chapter's
eventual construction must be built, not merely as background: it is a genuine **transmission-
regime break** — the linkage between PBoC policy rates and bank lending rates tightened materially
after August 2019 — meaning any impulse or rate-based state spanning 2019 needs the same structural-
break discipline this program already applies elsewhere to definitional splices (the WPI/CPI 2026
rebase caveats §16 flags for H61 are the nearest in-house analogue, cited for the *discipline*, not
the specific series). Beyond RRR and MLF/LPR, the PBoC runs a growing suite of **structural tools** — targeted RRR cuts
for SME and agricultural lending, and, most relevantly for A.2(iii)'s property amplifier, **Pledged
Supplementary Lending (PSL)**: a facility under which the PBoC lends directly and collateralized to
policy banks, who then fund designated projects. PSL injected roughly **RMB 740 billion** into
infrastructure through policy banks in 2022, and was ramped up sharply again in **December 2023**
with a fresh **RMB 350 billion** tranche explicitly earmarked for affordable housing, urban-village
redevelopment, and public facilities — the largest monthly PSL net injection since November 2022,
taking the outstanding PSL balance to roughly **RMB 3.25 trillion** by year-end 2023 **[Verified —
PBoC's own "Introduction to Structural Monetary Policy Instruments" (pbc.gov.cn, as of end-June
2023); Caixin Global, 10 January 2024, on the December 2023 RMB 350bn tranche and the RMB 3.25
trillion balance]**. PSL is worth naming specifically rather than folding into a generic "structural
tools" residual: unlike RRR or the LPR (economy-wide, price- or liquidity-based levers), PSL is a
**directed** instrument — the PBoC choosing which projects get funded, through which banks, at
what pace — making it the cleanest single illustration of A.2(i)'s own claim that China's credit
supply is a policy choice rather than an emergent market outcome, and a further, complete instrument
list is not claimed here **[VERIFY: PSL and the RRR/MLF/LPR trio are the best-verified instruments
this session located; the PBoC's own structural-tool roster is larger and evolves continuously]**.

**(iii) The LGFV/local-government investment nexus and the property amplifier.** Barred from direct
borrowing until a 2014 Budget Law revision opened a narrow, still-limited bond-market channel, local
governments built **local government financing vehicles (LGFVs)** as an off-books workaround,
borrowing against land-sale revenue to fund infrastructure — reaching an estimated **~51% of GDP
(~$10.4 trillion, IMF)** by 2025, per the credit-cycle monograph's own §7 case, cited by reference
here rather than recomputed. The **property sector**, together with construction and its supply
chain, is the mechanism's amplifier: property-related activity (direct plus indirect, through
construction and supply-chain sectors such as machinery and equipment) reached roughly **28% of
GDP in 2021** (down from a cited peak near **35% in 2016**), with the direct construction share
alone around **6.8% of GDP in 2023**; over **50% of China's steel demand** comes from construction
and real estate specifically, with property alone accounting for roughly **30–35% of total steel
consumption** **[Verified via secondary sourcing — CaixaBank Research, Statista, S&P Global
Commodity Insights; the exact GDP-share methodology varies somewhat across these secondary sources
and no single primary NBS breakdown was independently pinned this session — VERIFY]**. This is why
an easing decision reaches metals demand so directly: LGFV-funded infrastructure and property-
sector credit are, structurally, construction orders waiting on a financing decision.

**(iv) The pulse anatomy, link by link.** An easing decision — an RRR cut, a window-guidance
loosening of LGFV lending quotas, a relaxation of property-sector rules such as mortgage down-
payment ratios or purchase restrictions — surges TSF/AFRE within one to two quarters (new loans,
LGFV bond issuance, and property-linked trust/bond financing all accelerate together, precisely
because A.2(i)–(iii)'s levers point at the same channel simultaneously). The financing surge
converts into **construction, property, and infrastructure orders** — land purchases, project
starts, LGFV-funded infrastructure approvals — which convert into **metals demand**: the iron-ore,
copper, steel, and aluminum orders A.2(iii)'s steel-intensity numbers make almost mechanical. Metals
demand feeds **EM terms-of-trade**: commodity-exporting economies' export revenue and currencies
strengthen (the same channel the commodity-supercycle monograph's own case 5 — China 2001–2011 —
documents at decade scale: GDP growth averaging **~10.5%/year (2002–2011)**, infrastructure spending
rising from **$200 billion/year (2000) to over $1 trillion/year (2010)**, steel production from
**130 million tonnes (2000) to 820 million tonnes (2014)**, copper from the low-$1,000s to over
**$10,000/tonne (Feb 2011)**, and a documented capex lag — BHP's own capital-and-exploration
spending rising **76.5% from $12.9bn (FY2011) to $22.7bn (FY2012)**, a full year *after* the 2011
price peak — cited here by reference, never recomputed, per that monograph's own scope discipline).
Finally, a China growth scare or relief rally feeds **global risk appetite**, the same VIX/dollar/
EM-flow variables L9 already tracks. The case-5 verdict is worth repeating in this chapter's own
words because it is the bridge between the two atlas rows: "the same demand engine driving both a
decade-scale supercycle [1.3/H53] and a faster, ~3–4-year policy-pulse cycle [2.11/H54], two
different atlas entries reading two different frequencies off the same underlying economy"
(`docs/cycles/14-commodity-supercycle.md`, case 5's own closing line).

**(v) The 3–4-year cadence's driver.** The rhythm is political economy, not physics: Beijing eases
when growth threatens to miss its own targets (the annual GDP growth target set each March at the
National People's Congress, and the Five-Year Plans behind it) or when financial or social
stability is visibly threatened, then re-tightens once growth stabilizes and leverage or asset-
bubble concerns retake the policy conversation — producing a recurring stimulus-then-restraint
alternation rather than a smooth path. The record since 2008, read against this alternation: the
**November 2008** RMB 4 trillion stimulus, followed by 2010–11 tightening; a **September 2012**
roughly RMB 1 trillion infrastructure mini-stimulus, followed by a 2013–14 shadow-banking crackdown;
a **late-2015–2016** stimulus combining supply-side structural reform with property easing and the
local-debt-swap program (A.1(iii)), followed by the 2016–2018 deleveraging campaign and the **August
2020** "three red lines" policy — explicit thresholds (liability-to-asset ≤70%, net debt-to-equity
≤100%, cash covering short-term debt) that compressed developer borrowing capacity and fed directly
into the Evergrande-led default wave the shadow-credit monograph's own B8 documents **[Verified —
Caixin Global, November 2020, on the three-red-lines announcement and thresholds]**; an **August
2022** roughly RMB 1.1 trillion package responding to the post-zero-COVID growth trough; and a
**September 2024** RMB 2 trillion special-sovereign-bond-plus-50bp-RRR-cut package **[Verified —
South China Morning Post and Chatham House coverage, 2024]**. That is roughly **five** discernible
easing pulses since 2008 — matching atlas row 2.11's own "n≈4–5 since 2008" count — each followed,
with a lag of one to three years, by a tightening or reform campaign that sets up the next pulse.

---

### A.3 Transmission to India, specifically

**(i) Three channels, ranked.** **Commodity terms-of-trade** is the first and most quantifiable
channel, and it is explicitly **two-signed** for India — the identical structure atlas row 1.3/H53
already states for the broader commodity supercycle, inherited here rather than re-derived: as a
net commodity importer, a China-driven metals/energy price upswing is an unambiguous **input-cost
and current-account-deficit headwind** at the macro level (higher import bills for iron ore, coal,
base metals, and — via the broader commodity complex — oil, worsening the CAD and pressuring the
rupee through the same channel L9 already reads via its Kilian-decomposed oil leg); simultaneously,
it is a **sector tailwind** for India's own metals producers (Tata Steel, JSW Steel, Vedanta,
Hindalco, NMDC and peers), whose realizations rise directly with global prices China's demand is
pulling up. This is a **sector-tilt conditioner**, never an index-level directional call — the same
discipline the commodity-supercycle monograph insists on when naming Nifty Metal (rather than Nifty
Energy, distorted by administered pricing) as the cleanest available India-side beta proxy, and
exactly the atlas's own "projection principle" verdict for the sector: "Metals / mining: commodity
supercycle (H53) + China (H54) — pure projection" (`docs/CYCLE_ATLAS.md` §14). **Global risk
appetite / EM flows** is the second channel and the one that gives H54 its proper home: a China
growth scare or stimulus-relief rally moves the same VIX, broad-dollar, and NSDL-FPI-flow variables
L9's own triad already reads, not because China directly moves India's fundamentals but because
global asset allocators trade India's own beta inside an "EM growth" basket large enough that China
is a dominant constituent of the narrative even when it is not a dominant constituent of India's own
trade or investment flows. This is precisely the logic the atlas already uses to fold the dollar
cycle (2.9) and the Fed cycle (2.10) **inside** L9 rather than granting either a separate seat: H54
does not add new economics to the ladder, it potentially sharpens the **attribution and timing** of
moves the existing triad already registers. **Trade competition** is the third channel and the
narrowest: India and China compete directly in a limited set of manufactured and light-industrial
export categories to third markets, but — as the next paragraph documents — India's own trade
relationship with China is so overwhelmingly import-heavy that a competition channel large enough to
matter at the ladder's scale is not evident **[VERIFY: a dedicated, quantified India–China
third-market export-overlap coefficient was not located this session; the general finding that
commodity-exporting economies carry low export overlap with China is well documented, and India's
own overlap — while plausibly somewhat higher given its manufacturing ambitions — is not itself
pinned by a specific number here]**.

**(ii) Why India's direct exposure is structurally smaller than Brazil's, Australia's, or Korea's.**
The contrast is the asymmetry between an **export basket** and an **import basket**. Brazil sold
China roughly **$31.6 billion of soybeans and $20 billion of iron ore in 2024** alone — China
sources some **60% of its soybean imports** from Brazil and Brazil sends roughly **63% of its total
iron-ore exports** to China **[Verified — trade-data secondary sourcing, 2024 figures]**. Australia's
exports to China exceeded **$212 billion in 2023–24** against **$325 billion** of two-way trade, with
iron ore the single dominant category (Australia exported **$93.2 billion of iron ore in 2023** alone
— close to three times Brazil's comparable figure) **[Verified — secondary trade-data sourcing;
one aggregator's framing of iron ore as "over 150% of goods exports to China" is very likely an
artifact of that source's own category definitions rather than a literal ratio — VERIFY, flagged
rather than repeated as fact]**. Korea's exports to China have run in a **roughly 20–27% share of
Korea's total exports across 2018–2026**, with semiconductors alone accounting for **roughly a
quarter to over 40% of Korea's total exports** in recent prints and semiconductor shipments making up
close to **half of Korea's own China-bound exports** **[Verified via secondary sourcing across
several 2026-dated releases — treat the specific percentages as a recent range, not a single fixed
point, and note this session's search itself returned figures dated as current as mid-2026, i.e.
inside this program's own "as of" window rather than a stable historical constant — VERIFY]**. India,
by contrast, exported just **$16.65 billion** to China in FY2023-24 against **$101.75 billion** of
imports — a trade deficit of roughly **$85 billion**, widening further to a record **$99.2 billion**
in FY2024-25 as India's own exports to China *fell* 14.5% even as imports of electronics, batteries,
and solar cells rose **[Verified — Outlook Business, Statista, Business Standard reporting on
Ministry of Commerce data]**. Where Brazil, Australia, and Korea each send a large, GDP-material
slice of their own output directly to China — such that a China growth acceleration mechanically
lifts a substantial share of their own export revenue in a first-order, direct channel — India sells
China very little, and less every year. A China pulse reaches India almost entirely through the
**global commodity price** and **global risk-appetite** channels (i)–(ii) above, never through a
direct "China buys more of what India sells" channel, because that channel is structurally thin.
This is the precise, structural reason H54 is properly an **L9 enrichment candidate**, never a
standalone India driver in its own right: India lacks the direct bilateral transmission belt that
would justify treating China's own cycle as an independent India-specific seat the way it plainly
would for a Brazil- or Australia-focused book.

**(iii) What H54's own hypothesis-register test requires, stated honestly.** Atlas row H54's own
first-test line (`docs/CYCLE_ATLAS.md` §8) is precise: **"Incremental AUROC/loading inside the L9
factor, pooled."** This is a strictly *incremental* test — it does not ask whether China's credit
cycle matters in isolation (A.2's mechanism already makes that presumptively true), it asks whether
a China-credit-impulse reading improves L9's own read of India's global-cycle exposure **over and
above** what the existing dollar/VIX/US-real-rate/NSDL-FPI/Kilian-oil triad already captures — the
same incremental bar the atlas already holds every other candidate enrichment to (REER stretch,
LAF net liquidity) before it enters L9's construction, and structurally analogous to GF2's own
India-transfer regression (`research/cycles/globalcycle-deep/global-RESULTS.md`) rather than a
freestanding claim. Running that test requires an actual multi-year **TSF/AFRE flow-to-GDP series,
differenced** (A.1(i)'s own construction) — regressed or ranked against L9's existing state and
against India's own realized returns or stress dates — a construction this chapter's own proxy work
(A.4 below) deliberately does not attempt, because a commodity-relative-price proxy is a shadow of
the *demand* channel A.2(iv) describes, not a measurement of the credit impulse itself, and cannot
substitute for the real series inside an incremental AUROC/loading test. The proxy can inform a
Tier-C prior; it cannot be the regressor the actual pre-registered test needs. This is exactly why
the test remains **unrun** as of this pass, and why H54's promotion path runs through the runsheet
(A.4), not through further proxy refinement.

---

### A.4 The data reality and the proxy discipline

**(i) BIS blocked, no usable mirror.** The BIS Data Portal (`data.bis.org/topics/CREDIT_GAPS/data`)
publishes a China credit-to-GDP gap series free, with no login, quarterly — the source atlas row
2.11 itself names. Per the commodity-supercycle monograph's own §C.6, and consistent with this
program's established pattern (World Bank and FRED confirmed blocked at this container's proxy;
`research/CONTRACT.md` §7 Known Prior #11 groups these hosts as blocked for this environment
specifically), BIS is treated as **[VERIFY]-blocked here too**, reachable only from the principal's
own machine. The commodity monograph's own mirror-hunt found exactly one relevant GitHub
repository, `github.com/expersso/BIS` — a client library (an R package) that calls BIS's own SDMX/
API endpoints programmatically, hosting no cached copy of the data itself, so it fails identically
to a direct pull from a blocked network. **No usable static GitHub mirror of BIS China credit-gap
data is known as of this pass** — a genuine gap, not glossed as solved, and this chapter inherits
that finding by reference rather than re-running the search, per the commodity monograph's own
scope-discipline instruction.

**(ii) PBoC direct, untested.** The PBoC's own website publishes TSF/AFRE monthly statistical
releases free, in both Chinese and English, and China's National Bureau of Statistics (NBS)
publishes the nominal-GDP denominator — in principle a fully free primary-source pair that would let
this desk build the Biggs-Mayer-Pick construction directly (`Δ(12-month TSF flow / GDP)`, the
Bloomberg-lineage construction) rather than relying on any commercially licensed index. Whether
these hosts are reachable from this specific container is **untested this pass — [VERIFY access]**
— and, absent evidence otherwise, presumptively subject to the same block pattern already
established for BIS, FRED, and every other official-statistics host this program has tried from
this environment. Resolving this is a runsheet item for the principal's own machine
(`research/cycles/china-deep/partCDEFH.md` Part C, addendum items 61–64: TSF monthly backfill with a
component-migration-breaks registry, NBS GDP, the impulse assembly itself, and H54's own acceptance
registration before any look), not a claim this session can settle either way.

**(iii) The desk's options, honestly ranked.** **(a) Runsheet pulls on the principal's machine** —
PBoC TSF/AFRE plus NBS nominal GDP, replicating the impulse construction directly from free primary
sources, is the only path that can ever satisfy the free-data rule (`research/CONTRACT.md` §7, §12)
for the *real* object; a scraped or subscription copy of Bloomberg's own index would not. **(b) The
metals-vs-ags relative-price proxy** this desk's pre-registered trial tests, described in full
below. **(c) What a proxy can and cannot license** — stated plainly at the end of this section.

**(iv) The CI1 trial, its construction, and its actual results.** `research/register/trial-ledger.md`
entries **CI1a–CI1b** (script `scripts/analyze_china_impulse.py`, pre-registered before running,
per the program's two-pass rule) construct **`metals_rel`** — the mean log real price of a metals
basket {iron ore, copper, steel, zinc, nickel, aluminum} minus the mean log real price of an
agriculture basket {grains, softs, animal products} — on the vaulted Jacks (1850–2015) annual panel,
with an IMF monthly analogue (Metals Price Index minus Agricultural Raw Materials + Food, 1980–2017)
for the higher-frequency leg. Confounds were named **at registration**, before any result was seen:
**energy** (metals' own energy-intensive extraction and smelting link their prices to oil
independently of China demand), **dollar** (a broad dollar move re-prices all USD-denominated
commodities together, metals and agriculture alike, contaminating a *relative*-price read with a
pure FX effect the L9 dollar leg already reads separately), and **global industrial production** (a
broad global manufacturing upswing lifts industrial-metals demand for reasons having nothing to do
with China specifically). **CI1a** asked whether the "China era" (2000–2015) shows a materially
different metals-vs-ags dynamic than a fifty-year pre-2000 baseline: the standard deviation of the
three-year change in `metals_rel` runs **0.145 (1950–1999)** versus **0.318 (2000–2015)** — a
**2.19×** ratio against a pre-registered bar of ≥1.5×, a clear **PASS**. **CI1b** ran a named-pulse
sign check, tiny by design (n=2): cumulative `metals_rel` log change across **[2008-11..2010-12]**
(the 2008–09 stimulus pulse) came in at **+0.339**, and across **[2016-01..2017-06]** (the 2015–16
supply-side-reform/property-easing pulse) at **+0.161** — positive in **2/2** windows against a 2/2
bar, also a **PASS**. Read honestly, as `research/cycles/china-deep/china-RESULTS.md` itself
records: CI1a is the cleaner result — the variance of metals-vs-ags relative dynamics more than
doubled entering the China era, consistent with (not proof of) the China-demand channel A.2
describes; CI1b's 2/2 is real but thin — the 2008–11-to-2010–12 window also contains a global
reflation and a falling dollar, and the 2016-01-to-2017–06 window also contains a *supply-side*
capacity-closing rally, not pure demand — and neither window isolates the China-demand term from
its confound-list fellow-travelers.

**(v) What the passes license — and do not.** Both CI1 passes license exactly one thing: the
metals-vs-ags relative state qualifies as an **L9 enrichment CANDIDATE input**, Tier C, inside the
H54 lane — a computable shadow of the China pulse, usable as a Stage-2 briefing line ("China-pulse
shadow: `<state>`, confounds unresolved") and nothing stronger. They do **not** license a standalone
China signal; they do **not** license a claim that the proxy separates demand pulses from their
supply, dollar, and global-IP confounds; and they do **not** license H54's own graduation — the
hypothesis-register test A.3(iii) names (incremental AUROC/loading inside the L9 factor, pooled, on
the *real* TSF series) still waits on the principal's-machine pulls. This is the general pattern
this desk intends for every future data-blocked candidate, stated once here for reuse: a proxy
built and pre-registered honestly, with its confounds named **before** the result is seen, can earn
a Tier-C research candidacy; it cannot, on its own, ever earn a ladder seat.

**(vi) The mechanism-to-seat synthesis.** Assembling A.1–A.4 into one table — mechanism by
mechanism, exactly the discipline the fincycle-deep style bar's own §A.8 models and the L9
monograph's own A.4 applies to its five-series construction — makes the honest gaps as visible as
the confirmed content, here for a candidate built on two free series (one real, one proxy) rather
than L9's five.

| Mechanism | Free observable (or its proxy) | How H54 would use it | What remains an honest gap |
|---|---|---|---|
| Credit impulse, defined (A.1i–ii) | PBoC TSF/AFRE (monthly) ÷ NBS nominal GDP (quarterly), first-differenced | The real regressor for the incremental AUROC/loading test (A.3iii) | Both hosts untested from this container; free but **[VERIFY access]** — a runsheet item, not yet pulled |
| BIS China credit-to-GDP gap | `data.bis.org` credit-gap series | Would serve only as a cross-check on the *level* object, never the impulse itself (A.1ii's own gap/impulse distinction) | **[VERIFY]-blocked** here; no usable GitHub mirror found (commodity partC §C.6, inherited) |
| Policy-pulse mechanism (A.2i–iv) | RRR announcements, PSL tranches, LPR resets, LGFV/property policy changes (PBoC/NBS/press, all free to *read*) | Frames *why* an impulse construction, never a gap, is the right object; dates the ~5 pulses since 2008 | A quantified India-facing pass-through coefficient per pulse has never been estimated — the case chronology (sibling Part B) supplies dates, not magnitudes |
| Metals-vs-ags proxy (A.4iv–v) | Jacks annual (1850–2015) + IMF monthly (1980–2017) commodity panels, both already vaulted | CI1a/CI1b's own PASS results (2.19×; 2/2) license Tier-C L9-enrichment candidacy | Confounds (energy, dollar, global IP) are *named*, not purged — the proxy cannot isolate a China-specific term algebraically |
| India's three channels, ranked (A.3i) | Nifty Metal (bhavcopy), NSDL FPI + FRED VIX/dollar (already inside L9), DGCI&S trade data | Channel (i) sector-tilts alongside H53; channel (ii) is why H54 would live inside L9 at all; channel (iii) stays unweighted | No decomposition yet separates a "China" component of Nifty Metal's own return from the broader ToT/H53 state it already shares |
| India's structurally thin bilateral exposure (A.3ii) | DGCI&S/Ministry of Commerce trade data (India–China); comparator trade data (Brazil/Australia/Korea, secondary sourcing) | Grounds the "L9 enrichment, never standalone" verdict in an asymmetry, not an assertion | The export-competition channel's own India sign under a future China growth-model shift is a named open design item (CN-D3, `partCDEFH.md`), not yet tested |
| The incremental test itself (A.3iii) | — (requires the real TSF series) | The only licensed promotion path to a ladder seat | Cannot run at all until the runsheet items (A.4ii; `partCDEFH.md` Part C, steps 61–64) land on the principal's machine |

---

## PART G — Operator psychology

Part A documents an object the desk cannot observe directly at this pass — no live TSF series, no
live BIS mirror — and can only approach through a proxy whose own confound list is longer than its
signal. That combination — a genuinely real mechanism (A.2), an administratively managed data
source with every institutional incentive to obscure rather than reveal its own credit decisions,
and a sell-side research industry that produces a fresh wave of anticipatory commentary at every
policy-adjacent meeting — is exactly the setup that turns a legitimate research candidate into
either dismissed noise or over-traded gospel. This Part maps both failure directions to the
countermeasures A.1–A.4 already build in.

### G.1 The two-directional China-data skepticism trap

**Mechanism.** The credit-cycle monograph's own §7 case makes an honest, damaging point: an
administratively managed credit system suppresses the market-based signals (bond spreads, equity
drawdowns) this desk otherwise relies on to date a bust in real time. It is a short step from that
correct observation to an *incorrect* generalization — dismissing **all** Chinese official data,
including TSF/AFRE itself, as unusable or fabricated, and discarding the runsheet items A.4(iii)
names before they are even attempted. This is the wrong lesson: TSF/AFRE is not a survey-based
sentiment index vulnerable to the same falsification channel as, say, a confidence print — it is
built from ledger-level loan, bond, and equity-issuance entries across the banking and bond-market
system, in principle cross-checkable in aggregate against the PBoC's own balance sheet. Caixin
Global's own 2019 opinion piece critiquing "the growing problems with China's Total Social
Financing indicator" **[VERIFY: this session's search retrieved the piece's headline, outlet,
date (23 July 2019) and general framing, but not its full argument or every specific example — the
critique is consistent with a definitional/component-migration concern (A.1(iii)), not a
fabrication claim, but the full text was not independently confirmed]** is best read as a
composition-instability critique, not evidence the aggregate should be discarded wholesale. The
**opposite** trap is equally costly: trading TSF/AFRE prints as if they were clean, market-
discovered signals — reading a TSF beat the way a desk would read a US ISM beat — without carrying
the same monograph's own caveat that the *identical* print can mean something different in a state-
directed system (a surge can reflect a **policy decision** to lend more, per A.2(i), rather than an
organic acceleration in private-sector credit demand) than the equivalent print would mean in a
market economy.

**Countermeasure.** Read TSF/AFRE and its impulse as evidence of a **policy decision** — exactly
what A.1(i)'s "impulse," not "gap," framing already commits this chapter to — never as a market-
discovered signal of private-sector credit demand the way L10's own bank+NBFC aggregate is read for
India. Neither direction of the trap survives holding that distinction explicitly.

### G.2 The "China stimulus" narrative cycle in sell-side research

**Mechanism.** Each Politburo meeting, Central Economic Work Conference, or National People's
Congress session generates its own wave of anticipatory sell-side notes forecasting "big-bang
stimulus," reliably followed by a second wave of "disappointment" commentary when the announced
package under-delivers relative to the built-up expectation — a real, repeatedly documented pattern
rather than a one-off. The **24 July 2023** Politburo meeting's rare mention of "boosting the
capital market" stoked speculation of a stamp-duty cut and same-day (T+0) trading; neither was
delivered, and Bloomberg's own coverage — filed the same day, in advance of the disappointment it
then reported — carried the headline "China's Top Leaders Likely to Disappoint on Big Bang
Stimulus" **[Verified — Bloomberg, 24 July 2023; South China Morning Post coverage of the same
episode and its aftermath]**. The pattern repeated in **December 2024**: China skipped its usual
post-Politburo readout entirely while "investors awaited stimulus clues," per Bloomberg's own
headline **[Verified — Bloomberg, 2 December 2024]**. The cycle does eventually deliver real pulses
— **September 2024**'s RMB 2 trillion special-sovereign-bond-plus-RRR-cut package (A.2(v)) is the
proof — but the trap is not that stimulus never arrives; it is that **every** easing-adjacent
meeting generates the same anticipatory note regardless of whether that specific meeting is the
real pulse point, which makes sell-side stimulus enthusiasm itself a close-to-worthless timing
signal **[VERIFY: a systematic count of sell-side-note frequency against realized-pulse frequency
was not run this session; the 2023 and 2024 episodes are documented illustrations, not a quantified
base-rate study]** — if every meeting gets the identical note, the note carries no information about
which meeting is the one that matters.

**Countermeasure.** This is precisely why H54, even once fully researched, is designed as an
**incremental, pooled loading test against L9's existing triad** (A.3(iii)) and never as a
discretionary "read the Politburo readout" event trade — the same refusal L9's own A.4 already
states for the Fed ("What L9 refuses... forecasting the Fed"), applied here symmetrically to the
PBoC and the Party's own economic-policy calendar.

### G.3 Goodhart dynamics on TSF itself

**Mechanism.** Goodhart's Law applies to TSF with unusual force because TSF is simultaneously the
object regulators actively manage (via the window guidance and structural tools A.2 names) **and**
the object outside analysts read as a market signal — and each time a specific component of TSF
becomes a policy target, credit tends to **migrate** to a different component rather than
disappearing, changing TSF's own composition without necessarily changing the underlying credit
intensity an impulse construction is meant to track. A.1(iii) already names both concrete instances:
the 2015–2018 local-government bond-swap program (~RMB 15 trillion issued, converting LGFV bank and
non-bank debt into government bonds) and the 2018 asset-management rules' shadow-banking
suppression (the shadow-credit monograph's own B8). Both moved large credit stocks **between**
TSF's buckets rather than out of the system — a naive impulse reading built on a loans-only or
shadow-only sub-aggregate spanning either episode would misread a regulatorily engineered migration
as a genuine deceleration.

**Countermeasure.** Any eventual India-desk construction must consume the **full** TSF/AFRE
aggregate, never a sub-component — the same "own the aggregate, never a component that can be
gamed" discipline L10 already applies domestically (bank+NBFC combined, never bank-only, the
explicit IL&FS lesson the ladder's own L10 entry names), transposed here to a system where the
migration is administratively engineered rather than merely arbitrage-driven.

### G.4 The desk's own two traps

**Trap 1 — reading every metals rally as a China pulse.** CI1's own pre-registered confound list
(energy, dollar, global industrial production — A.4(iv)) is the operational checklist: a metals
rally that coincides with a broad dollar selloff, an oil spike, or a global PMI upswing is **not**
evidence of a China-specific pulse until those alternatives are checked, and CI1b's own bar (2/2 on
an n=2 sign check) was deliberately registered as a weak, non-discriminating test precisely because
a stronger claim was not — and is still not — supportable on a proxy this thin.

**Trap 2 — stale-cadence assumptions.** A.2's 3–4-year rhythm was measured across an era
(2008–2020ish) when property-linked construction was the dominant belt carrying a PBoC easing
decision through to metals demand — A.2(iii)'s own >50%-of-steel-demand fact. As China's property
sector winds down under three-red-lines-era deleveraging (still an unresolved, multi-year
adjustment per the credit-cycle monograph's own §7 case) and Beijing's own stated pivot toward
manufacturing- and technology-led rather than property-and-infrastructure-led growth continues, the
**channel** through which a future easing pulse reaches metals demand specifically may be
structurally weakening even if the policy-pulse cadence itself persists. This program's own
harvest-ledger (`research/cycles/china-deep/partCDEFH.md`, Part H) already states the honest 2021–26
question rather than resolving it: does a stimulus pulse shaped like September 2024's — aimed more
at local-government fiscal stress and household consumption than at a 2008-style infrastructure and
construction wave — still transmit to metals demand with A.2(iv)'s full strength, or has the
property-linked amplifier itself become a smaller share of the transmission than it was in
2008–2020? A further, structurally distinct possibility the same ledger names as a design item
(**CN-D3**): if China's own growth model shifts further toward export-competitive manufacturing,
the dominant India-facing channel could shift from **commodities** (A.3(i), where India's own sign
is mixed — importer headwind, producer tailwind) toward **trade competition** (A.3(i)'s third,
currently thin channel) — a shift that could plausibly **flip** India's own net sign on a China
pulse rather than merely weaken its current one. None of this is resolved by narrative confidence in
either direction; it is logged as an open question, annually re-asked as each new data vintage
lands, for exactly the same reason atlas §17's own cadence-drift discipline treats every ladder
`tau_half` as a living estimate rather than a frozen constant — H54 is not yet a ladder seat, but the
same epistemic humility applies before it becomes one.

### G.5 Countermeasures mapped

Five structural features carry this Part's actual work, and it is worth naming each once, plainly,
rather than leaving them scattered across G.1–G.4. **(1) The impulse-not-gap framing itself**
(G.1) — reading TSF/AFRE as evidence of what Beijing chose to do, never as a market-discovered
demand surprise, is not merely A.1's theoretical preference; it is the operator's own defense
against both skepticism traps at once, because a "policy decision" reading survives being told the
data might be managed (it is *supposed* to be managed) in a way a "market signal" reading does not.
**(2) The incremental-test, never-event-trade design** (G.2) — H54's own promotion path (A.3iii)
runs through a pooled loading regression, not a discretionary Politburo-readout call, which removes
the sell-side narrative cycle's main hook before the desk is ever tempted to grab it. **(3) The
full-aggregate-only consumption rule** (G.3) — never a loans-only or shadow-only TSF sub-series —
which makes a component migration invisible to the construction rather than mistakable for a
deceleration. **(4) CI1's own named confound checklist** (G.4, Trap 1) — energy, dollar, global
industrial production, registered before the print was seen — which gates every future "metals
rally = China pulse" temptation with a fixed, pre-committed list rather than an in-the-moment
judgment call. **(5) The open-question treatment of cadence and channel drift** (G.4, Trap 2) —
logging the property-era transmission question and the export-competition sign-flip possibility as
unresolved, annually re-asked items rather than resolving either from narrative conviction. None of
the five asks the operator to out-think Part A's own evidence in real time; each converts a
judgment call — is this print real, is this meeting the pulse, has this component simply moved
house, is this rally China or the dollar, does the old channel still carry — into a rule decided
here, in the registry, before the moment that would have made it hardest.

### G.6 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Dismissing all Chinese data as fabricated | Conflates the credit-cycle monograph's own finding (an administratively managed system suppresses *market-discovered* signals) with a claim about TSF's own data integrity; TSF is ledger-built, not survey-based | Treat TSF/AFRE as policy-decision evidence, cross-checkable against the PBoC's own balance sheet; Caixin's critique is a composition concern, not a fabrication claim |
| Trading TSF prints as if market-discovered | Ignores that a TSF beat can reflect a **policy choice** to lend more, not an organic private-sector demand surprise | Read the impulse as "what Beijing chose to do" (A.1(i)/A.2(i)), never as a demand-side surprise the way a US ISM print is read |
| Treating every Politburo/CEWC/NPC meeting as a live stimulus signal | Sell-side base-rate problem: every meeting generates the same anticipatory note (July 2023, December 2024 both documented) regardless of whether it is a real pulse point | H54 is designed as an incremental, pooled loading test (A.3(iii)), never an event trade; the same refusal L9 already applies to "forecasting the Fed" |
| Reading a TSF deceleration as tightening when it is component migration | The 2015–18 debt-swap program (~RMB 15 trillion) and the 2018 asset-management rules both moved credit **between** TSF buckets, not out of the system | Consume the full TSF/AFRE aggregate only, never a loans-only or shadow-only sub-series — the same aggregate-only discipline L10 applies domestically |
| Reading every metals rally as a China pulse | CI1's own construction is unpurged of energy, dollar, and global-IP confounds, named at registration | CI1's confound checklist gates any "metals rallying = China easing" read; the proxy licenses candidacy, never a standalone call |
| Assuming the 3–4y cadence and its metals-transmission strength are stable as property's GDP share shrinks | A.2's mechanism was measured in a property-heavy transmission era; three-red-lines-era deleveraging may be structurally shrinking that specific channel, and an export-competition-led China could flip India's own sign | Logged as an open, annually re-asked question (partCDEFH Part H); H54 stays Tier C, research-candidate-only, until a post-property-era subsample and the real TSF series can both be tested |
| Treating H54 as a standalone India driver | India's export basket to China is small and shrinking (A.3(ii)), unlike Brazil's, Australia's, or Korea's | H54 enters only as an L9 enrichment candidate, never a parallel seat; the incremental-loading test (A.3(iii)) is the only licensed promotion path |

None of these seven countermeasures asks the operator to be wiser in the moment than Part A's own
evidence justifies. Each converts a live judgment call — decide whether this month's TSF print is
real or manufactured, decide whether this Politburo meeting is finally the stimulus one, decide
whether a metals rally is China or the dollar, decide whether the old transmission channel still
holds as the property era ends — into a structural non-decision, made once, here, before the moment
that would have made it hardest. H54 leaves this chapter exactly where atlas row 2.11 and the
knowledge ledger both already place it: a real mechanism, a proxy that passed its own two honest
pre-registered tests, and a hypothesis still waiting for its actual data.

---

*China credit impulse monograph (atlas 2.11) · Part A & Part G · v1.0 · 2026-09-02 · Author:
Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in). Governed by
`research/CONTRACT.md`. Every figure above is search-verified as of September 2026 unless tagged
`[VERIFY: ...]`.*
