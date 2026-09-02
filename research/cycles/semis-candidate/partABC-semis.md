# H59 — The Global Semiconductor Cycle as India IT-Sector Context

*Monograph #37 in the cycle-research series · v1.0 · 2026-09-02 · Author: Claude (research agent)
for Ionic quant desk (principal: gaurav@ionic.in) · governed by `research/CONTRACT.md`.*

**Verdict up front.** `docs/CYCLE_ATLAS.md` §8 registers H59 — "Global semiconductor cycle (~4y,
SIA shipments) as IT-sector context" — with a stated prior already attached: **"weak-priority: does
it condition IT-sector exposure at all? sector context (likely CONTEXT only)."** This monograph
argues the candidate to its strongest form before accepting that prior, because H59 is genuinely
unusual among this atlas's rejects and context-only entries: unlike Kondratieff waves or Elliott
wave counts, the global semiconductor cycle is not a pattern-matching fiction. The mechanism is
real (§A.1), textbook-documented across five decades, and — on the WSTS billings series alone —
the phenomenon has produced on the order of ten complete peak-to-trough-to-peak swings since 1976,
comfortably clearing Contract §4's four-period clock test that only five of this program's original
32 cycle candidates managed to clear (atlas §7, known prior #1). If the mandate were "does the
global semiconductor cycle exist as a cycle," H59 might be one of the easiest yeses in the whole
register. **The mandate is not that.** The mandate — stated plainly in the atlas's own one-line
verdict and restated in this monograph's brief — is whether that real, well-evidenced shipment
cycle transmits to the return stream of an instrument this desk can actually hold: India's listed
IT-services complex (TCS, Infosys, HCL Technologies, Wipro, Tech Mahindra — the NIFTY IT
constituents), a business that sells services, applications, and BFSI-facing outsourcing hours, not
silicon. Argued honestly and at length (Part B), that transmission story fails at every point it is
tested against the public record: the two years the global chip cycle and Indian IT growth moved
together (2001, 2008-09) did so through a shared macroeconomic shock that hit both sectors
independently, not through a chip-to-services channel; and the most recent, most dramatic test case
— fiscal 2026, the single largest semiconductor upgrade in WSTS's history landing in the same twelve
months as TCS's first-ever year-on-year dollar revenue decline — is the sharpest available
falsification of a naive "chips up, IT stocks up" read-through. One narrower, genuinely
chip-linked channel does exist (semiconductor engineering-design services, §B.12) and one
genuinely future channel is dated but unrealized (the India Semiconductor Mission, §B.13). Neither
disturbs the verdict for the tradable, index-level object this program actually holds. **The
atlas's "likely CONTEXT only" prior does not merely survive this research pass — it emerges more
strongly grounded than before, because the pass surfaces a 2026 falsification the atlas's original
one-line verdict did not yet have on file.**

**Cross-reference discipline.** This chapter does not re-derive material three sibling monographs
already own. The global-financial-cycle mechanism (Rey's single global factor; VIX/dollar/US-policy
transmission to EM flows) belongs to L9 and its own dossier lineage; the China credit-impulse
candidate (H54) and the commodity-supercycle/terms-of-trade candidate (H53) are this atlas's other
two "global industrial state as India sector-conditioner" candidates and share H59's *family*
structure — a real global mechanism, an open question of whether it transmits to a *specific* Indian
sector — argued at comparable length in `research/cycles/china-deep/` and the commodity monograph;
this chapter borrows their family framing but not their content. The verdict taxonomy this chapter
applies (evidence-reject / fold / **context** / data-reject, plus the pass-adopt/pass-refuse split)
was completed in `research/cycles/calendar-context/partABC-context.md` Part A.4 and is reused here,
not re-derived. Every figure below not sourced to `research/cycles/semis-candidate/DATA-PROBE.md` —
this program's only desk record on H59, cited exactly as written, with **no desk numbers existing
beyond it** — is search-verified as of September 2026 or tagged `[VERIFY: ...]`.

---

## Part A — Theory, with the math

### A.1 The capacity-investment lag: cobweb theory applied to fabs

The semiconductor industry's cyclicality is not a metaphor borrowed loosely from agriculture; it is
the same formal mechanism. **Kaldor, Nicholas (1934), "A Classificatory Note on the Determinateness
of Equilibrium,"** *Review of Economic Studies* 1(2): 122–136 **[Verified]**, coined the cobweb
theorem's name and gave its general statement: when supply responds to a *lagged* price signal while
demand clears at the *current* price, a market can oscillate rather than converge. **Ezekiel,
Mordecai (1938), "The Cobweb Theorem,"** *Quarterly Journal of Economics* 52(2): 255–280
**[Verified]**, gave the model its canonical two-equation form and its most famous empirical
application — the hog cycle, in which the production lag is the biological gestation period between
a farmer's breeding decision (made when prices are high) and the litter's arrival at market (when
prices may have already fallen because every other farmer bred at the same signal). Formally: let
supply respond to the prior period's price, `Q^s_t = a + b·P_{t-1}`, and demand clear at the current
price, `Q^d_t = c − d·P_t`; market-clearing (`Q^s_t = Q^d_t`) generates a first-order difference
equation in price whose oscillation is **divergent, constant, or convergent depending on whether
b/d is greater than, equal to, or less than one** — the ratio of supply's price-elasticity to
demand's. Ezekiel's own sharper insight, the one that matters for dating a cycle rather than just
describing its shape: **the resulting cycle's period is twice the production lag itself** — a
mechanical consequence of a lagged-supply, current-demand clearing structure, not an assumption.

The semiconductor fab is the cobweb's modern high-fixed-cost incarnation. A leading-edge fab is a
multi-billion-dollar, multi-year commitment — DRAM fabs today run **$15–20 billion and 2–3 years**
from breaking ground to volume output, and logic fabs at the leading edge are comparable or larger
— so a capacity decision is, structurally, a bet placed on today's demand signal that will not clear
the market until years later, by which point every other fab operator who saw the same signal has
made the same bet. **Liu, Wen-Hsien (2005), "Determinants of the Semiconductor Industry Cycles,"**
*Journal of Policy Modeling* 27(7): 853–866 **[Verified]**, formalizes this with a twelve-variable
VAR and finds industry overcapacity — not demand collapse alone — as the primary driver of the
cycle's downswings; **Aubry, Mathilde & Renou-Maissant, Patricia**, in a pair of companion papers,
**"Investigating the semiconductor industry cycles,"** *Applied Economics* 45(21): 3058–3067 (2013)
**[Verified]** and **"Semiconductor industry cycles: Explanatory factors and forecasting,"**
*Economic Modelling* 39: 221–231 (2014) **[Verified]**, confirm with a twelve-variable VAR of their
own that **inventory levels and fab-capacity utilization jointly signal the industry's forward
state** — the cobweb's lag made empirically visible as a measurable inventory/utilization channel
rather than an assumed constant. Applying Ezekiel's period-equals-twice-the-lag result to a
construction-plus-ramp lag on the order of 2–3 years yields a natural period on the order of **4–6
years** — consistent with the industry's own measured record: **TechInsights' Chip Insider counts
14 recessive growth periods since the integrated-circuit market's emergence in 1963, averaging one
every 4.4 years**, with the further, honestly complicating observation that **cycles have become
more frequent over time while swings have grown less severe** — a pattern a naive fixed-lag cobweb
model does not obviously predict on its own (a lengthening capital cost per fab, if anything, should
lengthen the lag and the period, not shorten it), which this monograph flags as an open empirical
tension rather than resolving it: better demand-sensing, financial hedging, and business-model
diversification across memory/logic/foundry are candidate stabilizers, none confirmed here.

### A.2 Bullwhip amplification through the supply chain

The cobweb's capacity-side lag is compounded by a *demand-signal* distortion moving in the opposite
direction up the chain. **Lee, Hau L., Padmanabhan, V. & Whang, Seungjin (1997), "Information
Distortion in a Supply Chain: The Bullwhip Effect,"** *Management Science* 43(4): 546–558
**[Verified]**, identifies four causes of amplifying order variance as information moves from
retailer to manufacturer: demand-signal processing, the **rationing game** (buyers over-order when
a shortage is feared, expecting only partial fulfillment), order batching, and price variation. The
semiconductor chain — end-device OEM → module maker → distributor → fabless design house → foundry
→ OSAT — is an unusually long one for this mechanism to travel through, and the 2021–22 global chip
shortage is a textbook, dated instance of the rationing-game channel specifically: by one industry
estimate, **automotive Tier-1 suppliers and OEMs placed 2022 orders sized for roughly 120 million
vehicle-equivalent chip sets against an actual sales forecast near 83 million units**, and the
industry is estimated to have lost **8.2 million vehicles of production in 2021 alone** to the
underlying scarcity that triggered the over-ordering in the first place. The subsequent 2022–23
cancellation wave — automakers and electronics OEMs unwinding "phantom orders" once true demand
became visible — is the same mechanism's whiplash unwind, and it is not a coincidence that it lands
in the same window as §B.6's 2023 inventory correction: the bullwhip's amplification and the
cobweb's capacity lag are compounding, not competing, explanations of the same downturn.

### A.3 The WSTS billings series and the clock-test arithmetic

The World Semiconductor Trade Statistics organization's Historical Billings Report is the canonical
measure of this cycle for the same reason WSTS is this program's stated but currently unreachable
data source (`DATA-PROBE.md`): it is **monthly, back to 1976, free (Excel/PDF, no login), covering
four regions (Americas, Europe, Japan, Asia Pacific)**, with the granular 205-category "Blue Book"
layer introduced in 1991. Restated honestly and without embellishment: this environment's proxy
blocks wsts.org (host not allowlisted); the report itself is free in principle, so the free-source
rule (Contract §3) is satisfied; the pull is a **runsheet item for the principal's machine**, not a
desk failure, and the only fragment probed inside this environment — a public GitHub gist with SIA
regional billings for 2008-01 through 2014-02 (73 months) — was correctly judged insufficient for
any cycle claim (roughly 1.5 alleged periods against a four-period bar) and **left unvaulted**,
exactly as `DATA-PROBE.md` records; nothing in this monograph treats that fragment as evidence.
On the WSTS series' full nearly-fifty-year span, however, the clock test is not remotely in doubt:
counting distinct WSTS-measured downturns inside the 1976-present window alone (1985, 1990–91,
1996–98, 2001, 2008–09, 2011–12, 2015–16, 2018–19, 2019–20 as a shallow secondary dip, 2022–23) puts
the observed-complete-period count comfortably above ten — one of the very few atlas candidates that
could plausibly clear Contract §4's ≥4-period bar on the existence question alone, a status this
program's known priors (atlas §7: five of 32 candidates cleared) make genuinely rare. The clock test
answers "is this a cycle." It does not, and cannot, answer "does this cycle move an Indian
IT-services stock" — that is a transmission question, and it is the one this monograph is actually
tasked with (Part B).

### A.4 Memory versus logic: the cyclical amplifier, in numbers

Not every semiconductor product category cycles with equal violence. Memory (DRAM and NAND flash)
is a near-commodity: largely fungible across suppliers, price-elastic on the demand side, and
supply-inelastic in the short run because a memory fab's output is fixed by process node and
utilization, not by product mix — the purest expression of §A.1's capacity-lag mechanism. Logic
(processors, ASICs, analog) is comparatively differentiated, design-cycle-driven, and structurally
smoother. Memory's *share* of total WSTS billings is therefore a rough dial on how violent the
current cycle should be expected to run: **WSTS/Statista data put memory at 22.8% of total
semiconductor billings in 2006** `[VERIFY: full multi-decade share series — only the 2006 point was
independently located this session]`, a level broadly consistent with memory's historical 20–30%
range across the cycles catalogued in Part B. The 2024–26 AI-driven supercycle (§B.7) makes the
amplifier visible at a scale with no precedent in the free record: **WSTS's own 2026 forecast was
revised from $760.7 billion to $1.51 trillion within twelve months, and the organization attributes
roughly 79% of that entire revision to the memory segment alone**, with **memory revenue projected
to grow ~250% year-on-year to over $800 billion in 2026** — pushing memory's *share* of total
billings toward roughly half, from a historical quarter-to-third. The mechanism (§A.1) has not
changed; its current amplitude, on this one data point, has moved further from its historical range
than this monograph can find a prior instance of.

### A.5 The AI-capex era: an honest unknown

Whether the 2023–26 datacenter buildout breaks the historical cycle shape cannot be honestly settled
in September 2026, and Contract §1 explicitly reserves forward-looking judgement of this kind for
Stage 2, not Stage 1 — this monograph states the unknown rather than resolving it. The case for
genuine structural difference: hyperscaler capital expenditure crossed **$100 billion in a single
quarter for the first time in Q3 2025**, and the four largest hyperscalers are projected to raise
2026 capex **roughly 70% year-on-year to approximately $600 billion** — a demand base funded by a
handful of balance-sheet-rich enterprises pursuing a platform-level technology shift, closer in kind
to atlas entry 1.5's Perez-style "installation phase" analogy (already flagged CONTEXT-only
elsewhere in this register) than to the historically PC- and mobile-cycle-driven memory demand of
the 2010s. The case for "this is the same mechanism wearing a new label": every prior memory
supercycle was, at its own peak, described by contemporaries as structurally different from what
preceded it — 1995's PC-attach boom, 2017–18's first cloud-capex wave, 2021's chip-shortage
scramble — and every one of them still rolled over (§B.2, §B.5, §B.6) once the capacity committed at
the peak arrived. The **~$185 billion of industry capex committed in 2025** is capacity that lands
in fabs in 2027–2029 — precisely the multi-year window in which every historical supercycle
catalogued in Part B has rolled over. Whether AI-datacenter demand is a genuine step-change in the
underlying demand *level* or the latest instance of the same double-ordering dynamic (an "HBM
shortage" playing the role the "auto chip shortage" played in 2021) is not answerable from the
public record available at the time of writing, and this monograph does not attempt to answer it.

---

## Part G — Operator psychology (brief)

Every other cycle this atlas rejects or contains does so for the *opposite* reason H59 must be
watched for: the atlas's recurring warning (§0, and named explicitly in the calendar-context
monograph's own Part G) is that **regime permission gets dressed up as direct alpha** — "cycle
alpha" wearing a costume. H59 inverts the failure mode. Here the temptation is not to oversell a
weak mechanism; it is to grant a seat to a mechanism that is **unusually, almost seductively real**
— §A.1–A.4 establish a textbook cobweb dynamic, a documented bullwhip amplifier, and one of this
register's few candidates that could pass the clock test on existence alone — purely because it
*is* real, without the argument ever completing its own sentence: real *for what instrument*. Call
this the **existence fallacy**: a cycle's ontological reality is necessary but nowhere near
sufficient for a budgeted seat; Contract §12's own discipline (every proposed indicator must name
its free data source *and* — this program's India-first mandate — its transmission to an Indian,
tradable object) exists precisely to stop an argument that proves "the semiconductor cycle exists"
and quietly treats that as though it had proven "the semiconductor cycle moves NIFTY IT."

The atlas's taxonomy (§0; formalized in the calendar-context monograph's Part A.4) already gives the
discipline its name: H59, if it stays **CONTEXT**, sits in the bucket of objects that were *never a
candidate for a tradable seat to begin with* — the mechanism is real, the object (global chip
shipments) is real, but the claim on the table (a *price-timing signal for Indian IT equities*) is a
different object entirely, one this research pass could not connect it to. That is a different
bucket from **pass-refuse** (an object that clears its bar but is declined on cost or capacity
grounds — 4.10's turn-of-month SIP flow is that chapter's own exhibit) and a different bucket again
from **evidence-reject** (a claim tested and failed — Kondratieff, the US presidential cycle). A
sector-context conditioner, this discipline implies, **may** attach itself to the specific instrument
or revenue line where a named mechanism actually runs (§B.12's VLSI/design-services channel, should
it ever be built out at the segment level); it **may not** be smeared across an entire diversified
index merely because the index carries a label ("IT") that sounds industrially adjacent to
"semiconductors." This is the atlas's own "projection principle" (Part II §14), applied here rather
than re-derived: most sector cycles decompose into states this program already holds, and the
discipline of checking that decomposition *before* granting a seat is what stops a real mechanism
from being smuggled into an index where it has no purchase.

The concrete, dated failure mode to name is the **hardware read-through fallacy** — the sell-side
and financial-media habit of quoting a strong WSTS or SIA print as a bullish "read-through" for
Indian IT-services stocks, the same shape of error the calendar-context monograph calls "trading the
weather": a real, vivid, easily quoted fact (chip billings are up) substituting for the actual
transmission argument the fact would need to complete. Section B.11 below is this fallacy's sharpest
available rebuttal: the same fiscal year WSTS logged its largest forecast upgrade in the free
record, TCS logged its first-ever revenue decline — a coincidence the "chips up, IT up" narrative
has no room for, and precisely the kind of dated falsification a desk's immune system (the
calendar-context monograph's own phrase) should keep on file rather than re-argue from a headline
each earnings season.

---

## Part B — Evidence: the global record and the India transmission question

### B.1 — 1985: the demand slump that was also a trade war

By 1985 — described by contemporary industry accounts as **"the most painful year ever" for the US
semiconductor industry**, and attributed not to the general economy but to Japan — US firms'
share of the DRAM market had collapsed from **roughly 70% in 1978 to roughly 20% by 1986**, while
Japan's share rose from under 30% to about 75% over the same span. June 1985 brought a Section 301
complaint from the Semiconductor Industry Association; December 1985 brought a Commerce Department
antidumping self-initiation on 256K-and-future DRAMs; the sequence culminated in the **1986
US-Japan Semiconductor Agreement**. The structural detail worth carrying forward: Japanese
producers had invested through the *prior* late-1970s slump rather than pulling back, which left
them better positioned to expand into the mid-1980s downturn than their more strictly
demand-following US counterparts — a first, dated instance of §A.1's own point that investment
timing, not just demand level, decides who a downturn actually hurts. The 1985 case is included
here specifically to warn against treating "the semiconductor cycle" as one homogeneous mechanism:
this instance is inseparable from a bilateral trade shock, not a pure capacity cobweb.

### B.2 — 1996–98: the DRAM glut compounded by the Asian Financial Crisis

DRAM prices, having peaked in late 1995, fell **roughly 51% in 1996 and a further ~65% in 1997**,
with fab utilization sliding from **95% to 86%** — industry forecasters at the time flagged
1996–97 as the first back-to-back-decline pair in DRAM history. The downturn then compounded with
the **1997–98 Asian Financial Crisis**, which hit the balance sheets of Korean, Taiwanese,
Singaporean, and Malaysian semiconductor firms directly — financial distress layered on top of, not
merely coincident with, the industrial glut. As with 1985, the lesson to carry forward is that the
"pure" cobweb rarely runs alone; a currency/credit shock riding the same downturn is closer to the
historical norm than the exception.

### B.3 — 2000-01: the deepest downturn, four causes at once

Worldwide semiconductor sales fell **32% in 2001** — from **$204 billion in 2000 to $139 billion**
— the sharpest single-year decline in the industry's history at the time it was recorded, reversing
the record gains of 2000 entirely. The SIA's own contemporaneous diagnosis is worth quoting for its
precision: for the first time, the industry faced **all four classic downturn causes
simultaneously** — a global recession, an inventory surplus, over-capacity, and a decline in
underlying electronic-systems sales. This is the textbook "everything aligned" case, and its
severity is the reason this monograph treats 2001 as the sharpest available test of whether a
common macro shock (not a chip-specific channel) is doing the work when Indian IT growth also
slowed the same year (§B.10).

### B.4 — 2008-09: the financial crisis, with source variance stated honestly

Global semiconductor sales fell a comparatively modest **2.8% in 2008** (from $255.6bn to $248.6bn),
though the intra-year collapse was sharp — **December 2007's $22.3bn monthly billings had fallen to
$17.4bn by December 2008, a 22% year-on-year decline** entirely within the crisis's acute phase.
2009's full-year figure carries genuine source variance worth stating rather than silently
resolving: the SIA's own year-end tally showed **-9% to $226.3 billion**, while **WSTS's autumn 2009
forecast** had projected a steeper **-11.5% to $220.1 billion** `[VERIFY: reconcile forecast vs.
actual — the gap is plausibly a forecast/outturn difference rather than a data error, not
independently confirmed this session]`. Either figure marks 2008-09 as a credit-crisis-driven global
demand collapse, hitting semiconductor billings and (§B.10) Indian IT services in the same twelve
months through the same common cause.

### B.5 — 2018-19: the memory downturn, cobweb-textbook with a trade-war amplifier

Following record revenues in both 2017 and 2018, cloud operators had over-ordered memory through
2017; purchases steadily throttled back through 2018 as inventories swelled, and 2019 became "a
historical down cycle for both DRAM and NAND" — **NAND prices fell roughly 60% and DRAM roughly
40%** peak-to-trough. The US-China trade war, then in its early phase, compounded the demand
destruction on top of the pure inventory-driven cobweb dynamic (§A.1) — capex ramped when customers
were "clamoring for the components," creating oversupply exactly as demand fell away, the same
mechanism Liu (2005) and Aubry-Renou-Maissant (2013, 2014) formalize.

### B.6 — 2023: the bullwhip's unwind, closing §A.2's loop

The Global Semiconductor Market contracted **10.3% in 2023** as consumer demand cooled under
inflation and recession fears; **IDM and fabless inventory drawdowns suppressed fab utilization**
well below first-half-2023 levels, exactly the rationing-game unwind §A.2 describes — the
2021-22 double-ordering (§A.2's 120-million-vs-83-million auto-chip estimate) landing as
cancellations roughly two years later, precisely the lag Ezekiel's own cobweb arithmetic would
predict for an order-book distortion of that scale working through inventory.

### B.7 — 2024-26: the AI boom, dated not predicted

2024 chip revenue reached **$626 billion (+18% YoY)**; 2025 reached **$795.6 billion**; and — as
detailed in §A.4-A.5 — 2026's WSTS forecast was raised from **$760.7 billion to $1.51 trillion**
within twelve months, ~79% memory-attributed, DRAM alone projected near **$418.6 billion**. This is
the open, unresolved chapter; §A.5 states the honest uncertainty rather than forecasting its
resolution.

### B.8 — The India question, stated cleanly, and the honest limit on answering it

Every case above establishes that the global semiconductor shipment cycle is real, well-measured,
and — per §A.3 — old enough to have cleared this program's own clock test several times over. None
of it, on its own, says anything about whether that cycle moves an Indian IT-services stock. The
question this program actually needs answered — **does Indian listed IT-services revenue growth
(TCS/Infosys constant-currency guidance history above all) correlate with the WSTS cycle at all** —
has, so far as this research pass could locate, **no formal correlation study in the free
literature**, and Contract §12's research-only mandate for this phase (no data acquisition, no
backtests) means this monograph does not compute one either; the case below is argued from the
qualitative public record, sequence by sequence, exactly as Part B's global cases were, and states
its limits rather than papering over them with an invented number.

### B.9 — What Indian listed IT actually sells, and what actually drives it

TCS, Infosys, HCL Technologies, Wipro, and Tech Mahindra — together the overwhelming majority of the
NIFTY IT index's weight — sell **application development and maintenance, business-process
outsourcing, systems integration, and digital-transformation consulting**, billed in person-hours
and project fees to enterprise clients concentrated in Banking/Financial Services & Insurance
(BFSI), retail, manufacturing, telecom, and healthcare. NASSCOM's own driver language for the
industry is explicit and names none of these mechanisms as chip-shipment-linked: **"USA and BFSI
resurface as the key growth drivers, with APAC, Telecom, Retail and Healthcare emerging as the other
key growth markets."** The correct macro aggregate this business tracks — loosely, and imperfectly
— is **enterprise IT/digital-transformation spending**, not semiconductor unit shipments: Gartner's
own worldwide enterprise IT spending series projects **~$4.7 trillion in 2026, up 9.3% year-on-year**
against a broader $6.37 trillion total-IT-spending figure. Even at this *one remove* from
semiconductors — enterprise software and services spend, not chip billings — the correlation is
looser than a first glance suggests: **India's own IT-BPM export growth for FY26 (through February
2026) was reported at roughly 5.6% year-on-year**, against enterprise IT spending growing at roughly
9.3% — Indian IT is growing at *roughly half* the rate of the demand aggregate it is supposed to
track most directly, a decoupling worth flagging honestly before even reaching the semiconductor
question, because it establishes that the transmission chain has real friction at every link, not
just at the specific link (chips→services) this monograph is asked to test.

### B.10 — 2001 and 2008-09: a shared macro shock, not a chip channel

Both years in which global chip billings collapsed most severely also coincide with visible
deceleration in the (then much younger, and now much larger) Indian IT-export industry — but the
public record supports a **common-cause** reading, not a chip-to-services **channel**. In 2001, the
same US recession and dot-com collapse that produced the SIA's "four simultaneous causes" (§B.3)
also froze US corporate discretionary IT budgets and, for several Indian vendors, exposed
telecom-client concentration built up during the bubble — the shared cause is the collapse in US
corporate technology *capital expenditure and hiring budgets*, which shows up as reduced device
shipments on one side of the economy and reduced services demand on the other, as two independent
consequences of one recession, not chip shipments causing services demand or the reverse. In
2008-09, the pattern is sharper still because the crisis's epicenter — global banking and financial
services — is also Indian IT's single largest client vertical: Infosys guided FY2010 revenue to
decline **6.7% to 3.1%** before ultimately beating that guidance with **+3.0% growth to $4,804
million**, and TCS, still posting a record **$6 billion, +23% FY09** print before the crisis's full
weight landed, moved to markedly more cautious FY10 commentary; contemporaneous trade coverage names
the actual shock explicitly — a Business Standard headline from the period reads, plainly, **"TCS:
the BFSI blues are gone"** (2009) — with the sector-level framing throughout that period running via
banking-client budgets, never via a semiconductor-market frame. Both years, in short, are consistent
with H59 having zero *independent* explanatory power once the shared macro shock is accounted for —
exactly the reading a chip-services transmission theory would need to survive, and exactly the
reading it fails to survive on this record.

### B.11 — Fiscal 2026: the sharpest available falsification

The clearest, most recent, and most uncomfortable test case for a naive "semiconductor boom reads
through to Indian IT" story is not a historical episode at all — it is happening in the same fiscal
year this monograph is written. **TCS's fiscal year 2026 (ended March 2026) closed with the
company's first-ever year-on-year decline in US-dollar revenue — down 0.5% in USD terms and 2.4% in
constant currency** — landing in *precisely* the twelve months in which WSTS recorded the largest
single-year forecast upgrade in its history (§A.4: $760.7bn to $1.51 trillion), driven overwhelmingly
by an AI-fueled memory supercycle. The stated proximate causes, as reported in contemporaneous
analyst commentary, were **BFSI clients' continued caution with flat deal bookings, subdued
discretionary technology spending more broadly, and — the sharper point for this monograph — AI
itself compressing the value of traditional outsourcing work**, described in the same coverage as
**"AI-led revenue deflation"** as productivity gains from AI tooling compress the billable hours
inside application-managed-services contracts. This is not proof of a *negative* causal channel
running from chips to Indian IT services — TCS's own dominant stated causes are BFSI caution and
discretionary-spending softness, general demand-side factors, with AI-driven billing compression
named as one of three factors rather than isolated as *the* cause — but it is the cleanest available
falsification of the *naive positive* transmission story, and it belongs on this record for exactly
the reason the operator-psychology section above states: the very technology wave that is filling
WSTS's order book (AI infrastructure, memory, GPUs) is, in the same fiscal year, associated with
softening — not strengthening — the core revenue engine of the Indian IT-services business this
program would need to see move in the *other* direction for H59 to earn any allocation authority.

### B.12 — The one honest channel that does run through chips: VLSI and engineering-design services

The transmission story is not *entirely* absent from the record — it is narrower and differently
shaped than a naive shipment-billings read-through would suggest. Wipro, HCL Technologies, Tata
Elxsi, LTTS (L&T Technology Services), and Capgemini's India operations all run genuine
**semiconductor engineering-services** practices — RTL/ASIC/SoC design, verification, physical
design, and post-silicon validation — sold as outsourced design capacity to global fabless and IDM
clients, with several global chipmakers (Intel, Qualcomm, Nvidia, AMD among them) also running design
centers directly in India. This is the closest thing to a genuine chip-industry-linked revenue line
this desk's universe contains, and the discipline required to handle it honestly has three parts.
First, this revenue sits inside **engineering-R&D (ER&D)** segments that are a minority slice of
these companies' total revenue, and a smaller slice still of the NIFTY IT index's aggregate weight —
promoting a mechanism this narrow to an index-level conditioner would repeat exactly the
projection-principle error §G warns against. Second, and more importantly, **its own demand driver
is design activity — R&D headcount planning, new tape-out and design-win cycles, fabless firms'
multi-year product roadmaps — which correlates with client CAPEX/OPEX planning horizons, not with
month-to-month WSTS shipment billings**; a design-services contract signed *during* a shipment
trough (when fabless firms have every incentive to shift fixed design cost to variable, outsourced
capacity) can plausibly expand rather than contract, the opposite sign from what a naive
billings-linked story predicts. Third, **no free, granular, India-segment-level time series exists**
to test any of this quantitatively — this is a genuine data gap, not merely an unexplored angle, and
this monograph flags it `[VERIFY: whether LTTS, Tata Elxsi, or Wipro publish a standalone,
long-enough semiconductor/ER&D segment revenue series free of charge — not confirmed this session]`
rather than treating a plausible-sounding channel as though it were a measured one.

### B.13 — The India Semiconductor Mission: a dated, future channel, not a present one

India's own semiconductor manufacturing ambitions are real and well-funded, and honestly belong in
this record as a **dated** reason the transmission channel might strengthen someday — never as a
present-tense reason to promote H59 now. The **India Semiconductor Mission (ISM)** was established
in **December 2021** under a **Rs 76,000 crore (~$9-10 billion)** incentive framework, offering
fiscal support up to 50% of project cost for silicon fabs, compound-semiconductor units, and
ATMP/OSAT (assembly-test-mark-package/outsourced-assembly-and-test) facilities. **Tata
Electronics**, partnered with Taiwan's PSMC, announced an **~$11 billion (₹91,000 crore) fab at
Dholera, Gujarat**; **Micron Technology** committed a cumulative **~$2.75 billion** ATMP facility at
Sanand, Gujarat, backed by a **70% capital subsidy**; press reporting describes government
consideration of a further "**Semiconductor Mission 2.0**" incentive package near **$20 billion**
`[VERIFY: not confirmed as finalized government policy at the time of this search]`. The honest,
dated argument this creates: **if** these facilities reach volume production and India begins
generating its own domestically manufactured semiconductor shipment data — or, separately, if a
Tata Electronics or comparable entity becomes a separately listed, index-eligible manufacturing
company — a genuine, direct shipment-cycle channel to an Indian semiconductor-*manufacturing*
sector could emerge for the first time in this program's investable universe. As of this writing,
neither condition holds: the Dholera and Sanand facilities are pre-revenue or early-ramp, Tata
Electronics is a private Tata Sons subsidiary with no separate NSE listing, and Micron itself trades
on Nasdaq, not the NSE — meaning even a fully successful ISM outcome, today, creates a channel this
program's NIFTY 750 equity universe (Contract §1) has no instrument to hold. This is a reason to
**revisit** H59 at a future design review, not a present reason to promote it.

### B.14 — Conclusion of the India angle

Every honest attempt to connect the global semiconductor shipment cycle to India's listed,
tradable IT-services book fails on the public record. The two years in which global chip billings
and Indian IT growth moved in the same direction (2001, 2008-09) did so through a common
macroeconomic shock — collapsing US corporate technology budgets and, in 2008-09, a crisis
epicentered in Indian IT's own largest client vertical — not through a chip-shipment channel. The
most recent and most dramatic test available, fiscal 2026, delivers the sharpest possible
falsification of the naive positive read-through: the largest semiconductor forecast upgrade on
record coinciding with TCS's first-ever revenue decline, attributed in part to the very same AI wave
compressing the billable-services model. The one channel genuinely linked to chips (VLSI/ER&D design
services, §B.12) is real but structurally too small, too design-cycle-driven, and too data-poor to
test at the index level, and would in any case need to attach to a specific revenue line, never to
NIFTY IT as a whole. The one channel that could someday matter (the India Semiconductor Mission,
§B.13) is real, well-funded, and entirely outside this program's present investable universe. The
atlas's "likely CONTEXT only" verdict is not weakened by arguing H59 to its strongest form — it is
strengthened, because the strongest form was tried, and it still failed.

---

## Part C — India data engineering (brief)

Every object this chapter names resolves to a free pipeline or is flagged unavailable, per Contract
§3 and §12; naming a pipeline here creates no build obligation, in the same spirit the
calendar-context monograph states for its own CONTEXT entries. **WSTS Historical Billings Report**
(wsts.org/67/Historical-Billings-Report): free, monthly, back to 1976 (granular Blue Book categories
from 1991), Excel/PDF, no login — blocked at this environment's proxy per `DATA-PROBE.md`, a
runsheet pull for the principal's machine, not a desk failure. **SIA monthly press releases**
(semiconductors.org) are the lower-frequency, narrative update path between Blue Book pulls — free
in principle, though not itself proxy-tested inside this session `[VERIFY: reachability from this
environment specifically — not attempted this session]`. **NIFTY IT** (niftyindices.com factsheet):
free-float market-capitalization methodology, base date **January 1, 1996 = 1000**, ten constituents
(Infosys, TCS, HCL Technologies, Wipro, Tech Mahindra, Info Edge, LTIMindtree, Mphasis, Coforge, and
one further name depending on the current factsheet vintage), semi-annual (March/September)
rebalance — the correct India-side instrument for any future transmission test, and already this
program's stated IT-sector benchmark object.

**The pre-registration shape a transmission test would need — H59-D1, stated so it need never be
re-argued from a headline.** Conditioning variable: WSTS trailing-12-month billings YoY growth
state (sign, or a tercile/quintile rank, never a single magic threshold per Contract §6). Tested
object: NIFTY IT return **relative to Nifty 500 TRI** (Contract §10's benchmark convention for
sector/signal research). Method: purged and embargoed cross-validation per Contract §9, embargo
width scaled to the semiconductor cycle's own multi-year half-life rather than to NIFTY IT's own
turnover. **The stated prior, going in, honestly: FAILS** — §B.8-B.14's qualitative record gives no
mechanism a purged test would be confirming, only a common-macro-shock confound (2001, 2008-09) a
naive test could easily mistake for a signal if the confound is not explicitly modeled out, and a
2026 data point that argues the opposite sign. Per Contract §12's own decay-survival discipline, "no
mechanism found" is a poor foundation for admitting a signal regardless of what a raw correlation
might print. A secondary robustness note for if H59-D1 is ever run: any positive result should be
cross-checked against §B.12's narrower semiconductor-engineering-services channel at the individual
segment-disclosure level (e.g., LTTS's own reported segment revenue, where it exists) **before**
being read as a genuine index-wide effect — exactly the atlas's own projection-principle discipline,
applied so a real-but-small mechanism is never smuggled into an index-level verdict through an
under-specified test. Nothing above is a commitment. As the calendar-context monograph's own closing
note puts it: **a candidate registered to die is still knowledge** — H59-D1 belongs in the register
specifically so nobody re-argues "chips are booming, buy IT" from a media headline without the
register's one-line rebuttal, and this monograph's own §B.11, already on file.
