# PART B — The India issuance-wave case record

*Issuance/sentiment-cycle monograph (atlas 3.2; ladder seat `L7_issuance_sentiment`,
`config/ladder.yaml`, Tier B, τ½ 12–24 months) · Part B · v1.0 · 2026-09-02 · Author: Claude
(research agent) for Ionic quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. This Part reads `docs/CYCLE_ATLAS.md` row 3.2 ("Issuers sell paper
when it's expensive [Baker-Wurgler] — a persistent incentive, not an information gap; SEBI's 2024
SME crackdown is the institutional confirmation"), `config/ladder.yaml`'s `L7_issuance_sentiment`
entry (Tier B, τ½ 12–24 months, `reduce_only: false`, block `valuation_sentiment`, role "sentiment
state; also sizes special-sits sleeve [froth => shrink]", indicator "NSE/BSE listings, SEBI
bulletins, bhavcopy first-day pops", `changes_if`: "India pre-registered test vs 2018/2023-24
episodes"), and the companion machinery already specified in `research/cycles/issuance-deep/
partCDEFH.md` (Parts C–H: the two-leg construction, `state_t` = availability-weighted mean of
{pct(volume/mcap), pct(median listing-day pop)}; the **IS1** Baker-Wurgler India test, **IS2** the
2018/2023-24 episode shape check, and **IS-D3** the promoter/PE-OFS third-leg candidate — all
registered there, none re-derived here). **Scope, stated once and held throughout: this Part owns
the PRIMARY-MARKET record** — verified issuance volumes and counts, the reception record
(subscription ratios, first-day pops), what the secondary market did in the 12–24 months after,
the regulatory response, and what L7's two-leg state would have read, era by era — **not** the
flow/positioning record (`research/cycles/fpi-deep/partB-cases.md` §B2 already owns the October
2007 P-note episode's FLOW side — the 9% intraday crash, the same-day ~80% recovery — cross-
referenced, never re-derived here), **not** the credit/shadow-banking mechanics of the 2018 freeze
(`research/cycles/shadow-deep/partB-cases.md` §B2 and `shadow-deep/shadow-RESULTS.md` own the
IL&FS funding-run anatomy and its SC1 factor-propagation finding, cross-referenced), **not** the
capex-cycle real-side account of the 2003–11 and 1994–97 booms (`research/cycles/capex-deep/
partB-cases.md` owns OBICUS/GFCF, the premium-issue-share statistic, and the Reliance Power
"top-tick artifact" framing this Part borrows and extends on the reception/aftermath side, cross-
referenced not re-derived), and **not** the theory (this seat's own sibling theory chapter,
`partA-theory-psychology.md`, carries the Baker-Wurgler mechanism and the
survival-argument case in full; cited here, not restated). Primary-source SEBI bulletins were not
directly queryable this session (egress blocked at the network proxy per `research/CONTRACT.md`
§7 Known Prior #11), so every figure below is cross-checked against secondary financial-press
reporting and SEBI-bulletin-derived secondary tables, exactly as this program's house style
requires.*

---

## B1. The mechanism this record tests, and what "two-leg" means for `L7`

**The claim, stated once rather than re-argued.** Baker & Wurgler (2000, *Journal of Finance*,
"The Equity Share in New Issues and Aggregate Stock Returns") find that the share of equity (vs.
debt) in aggregate US new issues from 1928–1997 is a strong, robust predictor of subsequent
aggregate stock returns: firms issue relatively more equity precisely before periods of low market
returns. Baker & Wurgler (2002, "Market Timing and Capital Structure") extend this into a
persistent-incentive mechanism rather than an information asymmetry: issuers time equity sales to
windows when their own stock (and the market generally) is priced richly, and this incentive
cannot be arbitraged away by knowing about it — the desk cannot short an issuer's own decision to
sell paper, which is precisely the survival argument `config/ladder.yaml` records for `L7`
(Tier B, not Tier C, on the strength of this global evidence) while flagging India's own
coefficients as still untested (`changes_if`).

**What "two-leg" means, precisely, per `partCDEFH.md` Part D — stated here because every case
below is read against it.** `L7`'s state is **not** issuance volume alone. It is an
availability-weighted mean of two separately percentile-ranked legs: **Leg 1**, issuance value
scaled by aggregate market capitalization (so a given rupee volume reads "hotter" against a
smaller float than a larger one — necessary given how much India's own market-cap denominator has
grown across this record's 34 years); and **Leg 2**, the *median* listing-day pop across that
window's issues (not the pop of one flagship deal — a market of one spectacular IPO and forty flat
ones is not, on this construction, in froth). The design point stated in Part D bears repeating
because several cases below turn on it: **the froth signature needs BOTH legs high** — volume
alone is capital formation (a real economy raising money to build things, `capex-deep`'s own
domain), and pops alone are scarcity (too few deals for too much demand) — and a wave that runs
one leg hot without the other is a genuinely different, and less informative, state than one that
runs both. This Part reads every era for exactly that distinction, not merely for a total-rupee
headline.

**The budget this seat sits in.** `L7` is not reduce-only (`config/ladder.yaml`:
`reduce_only: false`) — unlike most of this ladder's Tier-C seats, a hot two-leg state can add to
the `valuation_sentiment` regime score (jointly with `L8`'s value-spread — an expensive market
*and* a hot primary market is the double-confirm `partCDEFH.md` Part D names), and independently
sizes the special-situations sleeve down when froth flags (`role`: "sizes special-sits sleeve
(froth => shrink)"). Every case below is therefore read on two separate questions the design
actually asks: what did the regime score's `valuation_sentiment` block see, and what would the
special-sits sleeve's size have been cut to, in real time, at each wave's peak.

---

## B2. Seven issuance waves, case by case

### 1. 1992–1996 — the free-pricing boom, India's founding issuance-cycle lesson

**The regime change.** Facing the 1991 balance-of-payments crisis, the Government of India
abolished the Controller of Capital Issues (CCI) — the administered-pricing regime under which new
equity could only be sold at government-set, near-par prices — and gave the newly created
Securities and Exchange Board of India statutory power over primary-market pricing. The effect on
pricing freedom alone is the single cleanest statistic in this record's opening chapter: **premium
(above-par) issues rose from just 1.37% of new issues in 1991–92 to 45.90% by 1994–95**
**[Verified, cross-checked against `capex-deep/partB-cases.md`'s own citation of the identical
figure]** — a complete dismantling, in three years, of the administered-price regime for new
capital.

**The flood, dated and counted.** India's primary-equity-market mania "began towards the end of
1994 and peaked in February 1995." **January 1995 alone saw 145 equity issues open for
subscription**, including mega issues from Reliance Capital, Essar Oil, and Hindustan Petroleum;
**one week in February 1995 saw 78 companies go public**, capping a fiscal year (1994–95) that
brought roughly **1,400 issues** to market, with primary-market volume growing **32% year-on-year
in 1995 alone**. **[Verified, all figures, cross-checked against `capex-deep`'s own independent
citation of the identical statistics.]** A broader four-year compilation puts the whole 1992–1996
window at **₹86,000 crore raised through public and rights issues by roughly 4,000 companies**,
bringing **1.5 crore (15 million) new investors** into the market through IPOs for the first time.
**[Verified, per a Moneylife retrospective.]** The boom's real-economy content is genuine, not a
pure financial mania: this equity financed India's first wave of greenfield private-sector steel,
textile, and petrochemical capacity — the exact plants the 1997–98 commodity collapse then found
itself competing to sell into (`capex-deep/partB-cases.md`'s own case 1, cross-referenced not
re-derived).

**The reception.** Retail demand at the peak was, by any standard, saturating: 78 companies
listing in a single week is not a market absorbing new supply calmly — it is a market where any
priced-above-par offer found a buyer. Systematic subscription-ratio and first-day-pop data for
this pre-NSDL, pre-electronic-settlement era could not be independently reconstructed this pass
`[VERIFY: a genuine per-issue subscription/pop series for 1994–96 — bhavcopy-based reconstruction
predates NSDL's own 1996 launch and the depository system generally, exactly the data gap
`capex-deep`'s own case 1 already documents for the real-side capacity data of the same years]`;
the qualitative record is unambiguous that issues were routinely and heavily oversubscribed at the
peak, consistent with the premium-issue-share statistic above.

**The vanishing-companies scandal.** The boom's dark twin, surfacing as the bust set in: companies
raised public money in collusion with investment bankers, brokers, and (in several documented
instances) banks, then simply disappeared, filing no further returns and leaving no operating
trace. **Over 600 companies vanished from the stock markets after raising money in 1998**; SEBI
named an initial **80 companies (having raised over ₹330 crore)** in May 1998, before widening
scrutiny to more than 600; a dedicated committee subsequently and more narrowly identified **238
listed companies** as genuinely "vanishing," of which **161 were eventually traced and 77 remained
untraceable**. **[Verified, the Moneylife retrospective's figures; the 600-vs-238 gap is itself
informative — a wide net cast, a narrower core confirmed]** `[VERIFY: precise reconciliation of
the >600 initial scrutiny count against the 238-company confirmed "vanishing companies" list — the
two are not the same population and this pass's search could not fully bridge them]`. Investor-
association estimates put the total value of vanished-company capital in excess of **₹29,000
crore**, out of an era-wide ₹86,000 crore raised — on this reckoning, roughly a third of everything
the boom raised. **[VERIFY: the ₹29,000 crore estimate's own primary source and methodology.]** A
separate, later retrospective count puts the number of listed companies that disappeared from
regional stock exchanges specifically at **roughly 700** `[VERIFY: whether this 700-company regional-
exchange count is the same population as, or additive to, the 238-company "vanishing companies"
list above]` — no single reconciled national count of "vanished" issuers from this era exists on
the record this pass could locate, and this Part states that honestly rather than picking one
number and presenting it as settled.

**The turn and the 1996–98 primary-market winter.** The July 1997 Asian financial crisis (the
contagion source `capex-deep`'s own case 1 and the Asian-Tigers capex mirror both document) ended
the boom; India's own growth decelerated from 7.8% (1996–97) to 4.8% (1997–98), and global
commodity prices for exactly the sectors the 1994–96 equity wave had built (steel, petrochemicals,
textiles) fell sharply, compressing the revenues of freshly built plants before they had even
amortized their construction cost. The primary market's own collapse is precisely, and severely,
measured: **1996–97 saw 882 issues raise ₹14,275.98 crore; 1997–98 saw just 111 issues raise
₹4,569.95 crore — a decline of 87.41% in the number of issues and 68.01% in the amount raised, in
a single year.** **[Verified, per SEBI's own Annual Report 1997–98 data.]** The workout that
followed ran for a decade and a half past the crisis itself: nationalised-bank GNPA fell from
**19.05% (1997) to 12.16% (2001)**, while the Board of Industrial and Financial Reconstruction
(BIFR) — the era's actual rehabilitation venue — registered **5,471 references by 2007**, of which
only **825 revival schemes were ever sanctioned** (a ~12–15% success rate), and the Sick Industrial
Companies Act itself was not repealed until **December 2016**, nineteen years after the crisis that
overwhelmed it. **[Verified, both, cross-referenced to `capex-deep/partB-cases.md`'s own case 1,
not re-derived.]** The RBI's Corporate Debt Restructuring mechanism, born **23 August 2001**, is
this era's first institutional answer to a boom-bust cycle it had no machinery to manage in real
time.

**What L7's two-leg state would have read.** No usable two-leg percentile exists this early — the
same structural gap `fpi-deep/partB-cases.md` §B1 documents for `L14`'s ownership percentile in
the identical years: a bhavcopy-and-listing-day-pop series requires the depository and electronic-
settlement infrastructure that NSDL only brought online from 1996, and the volume/mcap Leg 1
denominator itself is barely meaningful against a market capitalization this thin and this newly
opened. What the record *does* offer, directly and without needing the percentile machinery, is the
qualitative two-leg reading `partCDEFH.md` Part H already states as an established finding: 1994–96
is the record's founding instance of a wave that ran **both legs hot simultaneously** — extreme
issuance volume (Leg 1, on any reasonable reading given 1,400 issues against 1995's market
capitalization) and, on the qualitative record, extreme reception (Leg 2) — and that the same
extremity is exactly what let the vanishing-companies fraud hide inside genuine euphoria: a market
absorbing 78 IPOs in a week has no capacity left to scrutinize any one of them.

---

### 2. 1999–2000 — the tech mini-wave

**The build.** India's software-services boom — exports crossing **US$1 billion in 1997** and
reaching **US$6.2 billion within four years** — collided with Y2K remediation demand and the
global dot-com rally to produce the decade's second issuance wave, smaller and shorter than 1994–96
but carrying the same reception signature. **Infosys listed American Depositary Receipts on
Nasdaq in March 1999**, the first Indian company to do so, and its own share price run — reported
at levels on the order of ₹8,100 by 1999 before a further climb into 2000 — is the era's own
"top-tick artifact" in miniature, a domestic tech-mania stock whose price action tracked the
Nasdaq's own bubble almost exactly. **[Verified, the Nasdaq listing date and the exports figures;
the specific Infosys price levels reported across secondary sources vary and are flagged
`[VERIFY: precise Infosys share-price series 1999–2000]`.]** At the aggregate primary-market level,
**total funds mobilised across 151 issues came to roughly ₹7,817 crore in FY1999–2000**, with
average issue size of **₹53 crore** — falling to **₹6,108 crore and an average issue size of ₹24
crore in FY2000–01** as the wave rolled over. **[Verified, though the precise per-year issue-count
split behind the 151-issue figure is not cleanly disaggregated in the source located this pass;
`[VERIFY: the exact FY1999-2000 vs FY2000-01 issue-count breakdown]`.]** Rights issues from
established software names rode the same wave, though a clean, sourced rights-issue tally
specifically for this window could not be independently pinned this pass
`[VERIFY: FY1999-2000 rights-issue volume specifically, as distinct from fresh IPO volume]`.

**The reception.** Consistent with the boom's own genuine software-sector fundamentals (real export
growth, real Y2K-driven order books) layered under a speculative multiple, tech-adjacent IPOs and
rights issues of this window are qualitatively remembered as heavily oversubscribed and strongly
popped on listing, mirroring the Nasdaq-era mania premium global tech names commanded over the same
window; a systematic, sourced subscription-ratio table specific to this wave's individual issues
was not independently reconstructed this pass `[VERIFY: per-issue subscription data, 1999-2000
tech-sector IPOs and rights issues]`.

**What the secondary market did next.** The Ketan Parekh "K-10" stock-manipulation scandal unwound
from March 2001, compounding the global Nasdaq collapse; the Sensex fell on the order of **38%
during 2001** (cross-referenced to `fpi-deep/partB-cases.md` §B1's own figure, itself flagged
`[VERIFY: precise peak-to-trough Sensex dating]` there and not re-derived here). The genuinely
striking finding this Part inherits from `fpi-deep`'s own flow-side record, worth restating because
it bears directly on the issuance-wave read: **registered FII flows stayed net positive through
both FY2000–01 and FY2001–02** even as returns collapsed by nearly 40% — a domestically generated
crash (a manipulation unwind plus a global tech-bust echo) that foreign portfolio flows did not
meaningfully participate in selling into, per `fpi-deep` §B1's own honestly-flagged finding. This
Part's own contribution is the primary-market mirror of that same divergence: issuance volume
itself had already begun rolling over ahead of the crash (FY2000–01's ₹6,108 crore below
FY1999–2000's ₹7,817 crore), consistent with issuers' own incentive to sell into strength while it
still existed, rather than issuance being the proximate trigger of the 2001 collapse.

**The regulatory response.** SEBI and the exchanges' principal institutional response to this era
belongs more to the secondary-market manipulation side of the 2000–01 crash (the Ketan Parekh
investigation and subsequent badla/carry-forward-trading reforms) than to a primary-market-specific
intervention; no dedicated issuance-side regulatory reform specific to this wave (comparable to the
CCI abolition that opened the prior era, or the SME curbs that close this record) was located this
pass `[VERIFY: whether a specific 1999–2001 primary-market regulatory response, distinct from the
Ketan Parekh secondary-market inquiry, exists]`.

**What L7's two-leg state would have read.** Leg 1 (volume/mcap) reads only moderately hot on the
verified aggregate figures — ₹7,817 crore is a fraction of 1994–95's own scale, and it arrives
against a market capitalization already inflated by the tech rally itself, which mechanically
dampens the volume/mcap percentile even during genuine euphoria (the same denominator effect
`partCDEFH.md`'s own Part D flags as a reason to percentile-rank Leg 1 rather than read raw rupee
totals). Leg 2 (median pop), on the qualitative record, likely ran hotter than Leg 1 — a
sector-concentrated mania (software/tech names specifically) can produce extreme median pops on a
comparatively modest issuance base, precisely the "pops without matching volume" asymmetry Part D's
own AND-logic is built to distinguish from genuine broad-based froth. This Part flags, rather than
resolves, whether 1999–2000 constitutes a genuine both-legs-hot instance or a Leg-2-dominant one —
the per-issue data needed to settle it was not reconstructable this pass.

---

### 3. 2004–2008 — the great wave, and Reliance Power as the top-tick artifact

**The build, by scale.** India's 2003–2007 real-economy boom (`capex-deep/partB-cases.md`'s own
case 2, the "infra supercycle") ran alongside, and was substantially financed by, the largest
sustained equity-issuance wave in the record to that point. **ONGC's March 2004 IPO** — 142.59
million shares at ₹750 (retail discount ₹712.50), aggregating **₹10,694.50 crore** — mobilised bids
worth **~₹73,000 crore, oversubscribed 6.82 times**, one of the largest public issues in Indian
history to that date. **[Verified, all figures reconciled: 6.82 × ₹10,694.5cr ≈ ₹72,940cr, matching
the ~₹73,000cr bid total independently reported.]** **DLF's June–July 2007 IPO** — 175,000,000
shares at ₹525, aggregating **₹9,187.50 crore (~US$2 billion)** — was overall subscribed **3.47
times** (the QIB portion alone 5.13 times), listing 5 July 2007; contemporaneous reporting flagged
comparatively tepid *retail* demand even as institutional demand ran hot — an early instance of the
same leg-divergence this Part's later cases (2010, 2021) repeat at larger scale. **[Verified.]**
SEBI's introduction of the **Qualified Institutional Placement (QIP)** mechanism in 2006 added an
entirely new institutional-only supply channel mid-wave, layering directly atop the IPO calendar; a
precise FY2004–FY2008 cumulative IPO-plus-QIP total could not be pinned to one primary table this
pass `[VERIFY: exact FY03–08 five-year cumulative IPO+QIP figure — annual counts (78 IPOs/$7.23bn
in 2006; a widely cited 93–103 IPOs in 2007, figures not reconciled this pass) and a 2006–07
combined primary-market total of ₹1,61,769 crore (including private placement, not IPO-only) are
the closest independently verified anchors]`.

**The reception, and the era's own IPO-allotment scandal.** Retail-allotment fraud surfaced mid-wave
in the so-called **IPO Demat Scam**: Roopalben Panchal and associates used thousands of fictitious
demat accounts to corner retail-quota shares — the December 2005 YES Bank IPO was the case that
exposed it, and SEBI's subsequent probe widened to **105 IPOs across 2003–2005**, finding
irregularities in **21** of them; SEBI ultimately issued directions against **82 financiers, 24 key
operators, 12 depository participants, and 2 depositories**, and eventually disgorged and
redistributed roughly **₹41.34 crore to some 1.27 million investors**. **[Verified.]** Academic
work on IPOs listing across 2002–2006 finds average first-day underpricing (listing performance
against the market index) on the order of **46.55%** `[VERIFY: precise study scope, sample, and
exact index-adjustment methodology behind the 46.55% figure]` — consistent with a wave running hot
reception broadly, not merely at a handful of flagship names.

**Reliance Power, January 2008 — the top-tick artifact, cross-referenced from `capex-deep`, extended
on the reception side.** `capex-deep/partB-cases.md`'s own case 2 already names Reliance Power's
IPO "the single most literal 'IPO at the top' instance this desk's entire cycle-atlas project has
yet documented" — this Part does not re-derive that finding, only extends it on the primary-market
reception side its own scope owns. The issue: **₹11,700 crore, priced at ₹450/share, opened
January 2008, oversubscribed 73 times**, for a company that at the time of its IPO had **no
operating assets and no cash flow** — pure greenfield power-capacity promise monetized at the exact
top of a six-year boom. Subscription closed within days of the **Sensex's own all-time intraday
high, 21,206.77 on 10 January 2008**. **[Verified, both.]** It listed **11 February 2008**: opened
at ₹530 (a 17% premium to issue), touched an intraday low of ₹355.05, and closed the same day at
**₹372.50** — a loss for every day-one allottee before the stock fell much further over the
following years, never regaining its issue price; by November 2017 it had made a fresh low of ₹35,
and ₹10,000 invested at the IPO was worth roughly ₹1,636 a decade on. **[Verified, all figures,
cross-checked against `capex-deep`'s own independent citation of the identical listing-day
numbers.]** A 73× oversubscription record and a same-day negative return are not, on their face,
contradictory — they are the record's cleanest single demonstration that Leg 2's *median* pop and
a flagship deal's own outcome can diverge from the mania that produced the demand in the first
place: retail and institutional money chased the *name*, not a defensible valuation, and the price
discovered on day one reflected that gap almost immediately.

**What the secondary market did next — the 2008 shutdown.** Reliance Power listed five weeks before
the Sensex began its collapse; the global financial crisis then closed the primary market almost
completely. Calendar-2008 IPO count fell to **37–38 issues, raising a combined ~US$3.8 billion**,
down from **103 (2007, `[VERIFY: exact count, a competing source puts 2007 at 93]`) and 79 (2006)**
— **three major firms formally withdrew planned IPOs** for lack of investor response, and
**FY2008–09 mobilised just ₹2,034 crore through 21 small IPOs**, a collapse on the order of 95%+
from the prior fiscal year's pace. **[Verified, the aggregate figures.]** Nifty fell from its
January 2008 peak (~6,357) to its October 2008 trough (~2,252), on the order of **60–65%**
(cross-referenced to `fpi-deep/partB-cases.md` §B2 and the credit monograph's own case #10, not
re-derived here) — the primary market's own shutdown running in lockstep with, not ahead of or
behind, the secondary-market collapse.

**The regulatory response.** The Panchal-era demat-scam enforcement (above) is this wave's own
mid-cycle institutional response, tightening retail-allotment integrity years before the wave's own
top; no comparably dedicated *post*-2008 primary-market-specific reform (distinct from SEBI's
general disclosure and QIP-eligibility tightening across the following years) was located this pass
as a direct response to the Reliance Power episode specifically `[VERIFY]`.

**What L7's two-leg state would have read.** This is the record's cleanest instance of both legs
running hot simultaneously and in the same direction — Leg 1 (record cumulative volume, a wave
running IPO and the newly available QIP channel together) and Leg 2 (73× on the era's largest
single deal, 46.55%-average underpricing across the broader 2002–06 sample) both sit at, or near,
the top of any reasonable percentile construction, exactly the AND-condition `partCDEFH.md` Part D
requires for a genuine froth flag. `partCDEFH.md` Part H's own established finding — "India's
issuance waves top-tick markets with regularity (1994–96, **2007–08**, 2021, 2024)" — is directly
grounded in this case: a two-leg-hot state arriving five weeks before the market's own all-time high
is precisely the state the seat is built to catch, and precisely the case where the special-sits
sleeve's froth-triggered shrink rule would have been earning its keep at the exact moment retail
capital was chasing a pre-revenue power developer at 73 times demand.

---

### 4. 2010–2011 — the PSU/QIP echo

**The build.** Post-GFC recapitalization first ran through the QIP channel: **2009 saw 96
companies raise a combined ₹64,750 crore through QIPs, IPOs, and rights issues together**, and
real-estate companies specifically raised **₹14,224 crore via equity offerings in 2009, rising to
₹23,914 crore in 2010** — largely QIP-routed refinancing of balance sheets stressed by the
2008 shock. **[Verified, both years' real-estate figures; the ₹64,750cr 2009 combined figure per a
Business Standard year-end compilation.]** The IPO calendar itself then delivered a new record:
**64 companies mobilised ₹37,535 crore in 2010** — a new all-time high, surpassing every prior year
in this record including 2007–08's own peak. **[Verified.]** The centerpiece: **Coal India's
October 2010 IPO** — issue size **₹15,199.40 crore**, priced at **₹245/share**, offer window 18–21
October 2010 — was subscribed **15.28 times**, listed **4 November 2010**, and stood as **India's
largest-ever IPO**, surpassing Reliance Power's own then-record ₹11,700 crore. **[Verified, all
figures.]** The wave's supply, notably, was substantially **state-engineered**: a disinvestment
calendar of PSU share sales (Coal India chief among them), not an organically arising private-sector
issuance boom — a genuinely different mechanism from 1994–96's or 2007–08's private-sector-led
mania, worth flagging explicitly because it changes what Leg 1 alone would be measuring.

**The reception.** Coal India's 15.28× subscription is a genuine, broad-based demand signature, not
merely an institutional book-building formality; but a single flagship deal's own oversubscription
is not, on `L7`'s own construction, a substitute for the *median* pop across the year's full 64-deal
slate — and the 2011 QIB-participation collapse (below) is itself circumstantial evidence that
2010's reception was considerably more concentrated in a handful of PSU/large-cap names than the
headline record-year total suggests `[VERIFY: a genuine per-issue 2010 subscription/pop
distribution, to test whether the median (not merely the Coal India outlier) ran hot]`.

**What the secondary market did next — the 2011 fade.** The wave rolled over sharply within a
single calendar year: **India's primary market shrank over 64% in January–September 2011 versus
the year-earlier period — 38 companies raised ₹6,004 crore in the first nine months of 2011,
against 50 companies and ₹16,709 crore over the same window in 2010** — an **eight-year low** for
IPO fundraising. **Roughly 28 companies called off their public-issue plans for the year**, and
**26 of 39 issues (two-thirds) failed to receive even the minimum one-time QIB subscription**.
**[Verified, all figures.]** A contemporaneous retrospective found 2011's IPO cohort had, on
average, **eroded roughly one-third of its own aggregate issue-size value** by year-end — a genuine
wealth-destruction outcome for the year's own allottees, not merely a slower pace of new supply.
**[Verified.]** The Sensex itself fell on the order of the broader 2011 global-risk-off episode
(the Eurozone crisis, domestic policy paralysis, and rupee weakness `[VERIFY: precise Sensex
2010-peak-to-2011/12-trough figure — not independently re-derived this pass, and outside this
Part's own primary-market scope]`), consistent with — though this Part does not independently
verify a precise causal lag — the record's recurring pattern of a hot issuance year giving way to
weak subsequent secondary-market conditions within twelve to twenty-four months.

**The regulatory response.** No dedicated primary-market regulatory intervention specific to the
2010–11 wave (comparable to the 2005–06 demat-scam enforcement, or the 2024 SME curbs) was located
this pass; the era's own institutional lesson is executional rather than regulatory — a
disinvestment calendar timed to a strong secondary market extracted genuine value for the exchequer
(Coal India's own scale) but arrived close enough to the wave's own top that within a year two-
thirds of the following cohort's issues could not clear even the QIB minimum.

**What L7's two-leg state would have read.** This case is the record's clearest illustration of
Part D's own AND-logic design point stated in §B1 above: **Leg 1 alone, read in isolation, would
have flagged 2010 as an unambiguous froth year** — record cumulative volume (₹37,535cr), a
record-breaking flagship deal, and a genuine acceleration off 2009's already-elevated QIP-led base.
**Leg 2, read against the *median* rather than the flagship**, plausibly confirms only partially —
a state-engineered disinvestment supply wave concentrated demand in a small number of PSU names
precisely because the government, not organic private-sector sentiment, set the calendar, and
2011's immediate two-thirds QIB-shortfall rate is circumstantial evidence the broader deal slate's
underlying reception was considerably less universal than Coal India's own headline number implies.
A design that read Leg 1 without Leg 2 here would have overstated genuine speculative excess and
under-read how much of 2010's volume was supply-side (a state seller monetizing a strong tape)
rather than demand-side (buyers bidding up scarce paper) — precisely the "volume alone is capital
formation, pops alone are scarcity" distinction `partCDEFH.md` Part D states as the reason the
construction requires both legs together.

---

### 5. 2014–2018 — the institutional wave, and the IL&FS freeze

**The build.** A second post-election institutional-issuance wave ran 2014–2017, headlined by a run
of insurance, asset-management, and exchange listings that had, in several cases, waited years for
a regulatory or promoter-strategy green light. **HDFC Life's November 2017 IPO** — 29.98 crore
shares, aggregating **₹8,695 crore** — bid 7–9 November 2017. **HDFC AMC's July 2018 IPO** —
**₹2,800.33 crore**, bid 25–27 July 2018 — was **103% subscribed on Day 1** alone
`[VERIFY: the final, full-book multi-day subscription multiple — only the Day-1 headline figure
was independently pinned this pass]`. **General Insurance Corporation's IPO — the largest single
mainboard issue of the year at ₹11,257 crore** — anchored a record calendar-2017: **36 mainboard
IPOs raised ₹67,147–68,826 crore in 2017 [figures per two closely-agreeing secondary compilations,
`[VERIFY: exact reconciled total]`]**, decisively surpassing 2010's own ₹37,535 crore record; a
broader count including SME issues puts **153 total IPOs raising US$11.6 billion for the full
calendar year**. **[Verified, all figures.]** **Seventeen of the 36 mainboard issues received more
than 10× subscription, and 18 of the 36 delivered listing-day returns above 10%** — a genuinely
broad-based, not merely flagship-concentrated, reception signature, a useful contrast with case 4's
own concentration caveat.

**The reception.** The breadth statistic above — roughly half the year's mainboard cohort both
heavily oversubscribed *and* popping double digits on debut — is the strongest median-pop evidence
this Part's own record carries for any pre-2020 era, precisely the both-legs-simultaneously-broad
signature `partCDEFH.md`'s own Part H names 2007–08 for. Against a market capitalization that had,
by 2017, grown substantially past its 2007–08 scale, the *volume/mcap* Leg 1 percentile likely ran
somewhat less extreme in relative terms than 1994–96's or 2007–08's own readings even at a larger
absolute rupee total — the exact denominator effect §B1 above names.

**What the secondary market did next — the IL&FS freeze.** The **14 September 2018 default** of
Infrastructure Leasing & Financial Services (IL&FS) — `shadow-deep/partB-cases.md` §B2's own
centerpiece, cross-referenced not re-derived here — triggered a system-wide NBFC funding freeze
whose 12-month equity-factor propagation `shadow-deep/shadow-RESULTS.md`'s own SC1 trial measures
directly: small-cap returns fell **−24.8% (18th percentile)** and the broad market fell **−20.2%
(16th percentile)** over the September 2018–August 2019 window, a finding that chapter's own honest
read states plainly — "the freeze did NOT stay contained" to NBFC-adjacent names; by the time a
12-month equity window could see it, it was "everyone's problem." This Part's own contribution is
the primary-market transmission that finding implies but does not itself measure: the pipeline of
already-SEBI-approved issuers **froze in place** rather than reaching the market. By **December
2018**, SEBI's own chairman was publicly lamenting the slow pace of IPOs reaching market despite
roughly **₹600 billion (~US$8.43 billion) of standing SEBI approvals**; by **August 2019**, nearly
**two dozen companies' SEBI approvals were set to lapse** unused, together representing a further
**₹16,500 crore** of capital that never reached the market inside its approval window. **[Verified,
both figures.]** Calendar-**2019 IPO count fell to 62 issues raising US$2.53 billion
(~₹17,899 crore)** — a **62% decline in volume and 54% decline in proceeds** versus 2018 — confirming
the freeze extended through the whole of the following calendar year, not merely the acute
September–December 2018 window. **[Verified.]**

**The regulatory response.** SEBI's own December 2018 public commentary on the slow IPO pace is
itself a regulator reading the freeze in close to real time — exactly the "a regulator acting IS a
reading" annotation `partCDEFH.md` Part E's algorithm step 4 already builds into the seat's
construction. The freeze's actual resolution ran through the credit-side institutional machinery
`shadow-deep/partB-cases.md` §B2 documents in full (the Section-241(2) board supersession, the new
management's asset-monetization program) — not a primary-market-specific reform — consistent with
this being fundamentally a credit-shock transmission into the issuance pipeline, not an issuance-
side pathology in its own right.

**What L7's two-leg state would have read.** A moderate-to-high two-leg reading through 2017 (broad
subscription and broad pops, a somewhat damped Leg 1 percentile given the larger by-then market cap)
gives way, within a year, to a state where **both legs collapse simultaneously and for the same
external reason** — not a wave that priced its own excess (as 2007–08's did) but one interrupted by
an external credit shock arriving from outside the issuance mechanism entirely. This is a
genuinely different failure mode from every other case in this record: the two-leg state correctly
reads "cold" through 2019, but a design attributing that cold reading to *sentiment having turned
of its own accord* — rather than to a credit-side external shock this seat was never built to watch
(the same single-pool blind spot `fpi-deep/partB-cases.md` §B3 documents for `L14`'s own 2013 debt-
pool miss) — would mis-attribute the mechanism even while reading the state correctly.

---

### 6. 2020–2022 — the startup wave, and the leg-decoupling at its top

**The build.** India's post-COVID new-economy issuance wave ran through 2021 at a pace this
record's earlier eras never matched in *count*: calendar-**2020 saw 43 IPOs raise US$4.09 billion**,
building through the year (**19 IPOs worth US$1.84 billion in Q4 2020 alone**), before 2021
delivered the record itself. **[Verified.]**

**The reception, at its most euphoric.** **Zomato's July 2021 IPO** (price band ₹72–76) was
subscribed **38.25 times**, opening around ₹116 — a **~52% premium to its ₹76 issue price** — and
rising further intraday. **[Verified.]** **Nykaa's November 2021 IPO** — **₹5,300 crore**, price
band ₹1,085–1,125 — drew bids for **216.59 crore shares against an offer of 2.64 crore, an 81.78×
subscription**, and opened at **₹2,018, an 80% gain** over its ₹1,125 issue price. **[Verified.]**
Both are genuine both-legs-hot instances at the level of the individual deal: heavy demand (Leg-2-
relevant subscription) *and* a large pop, arriving inside a calendar year running record aggregate
volume (Leg 1).

**Paytm, November 2021 — where the legs decoupled.** **Paytm's IPO — ₹18,300 crore — was, at the
time, India's largest-ever public issue**, comfortably surpassing Reliance Power's 2008 record.
Day-1 subscription ran to only **~18%** of the retail/non-institutional book
`[VERIFY: the final, full-book overall subscription multiple across all investor categories — this
pass located only the Day-1 headline]`. It listed **18 November 2021**: opened at **₹1,950 on the
NSE — already 9.3% *below* the top of its ₹2,080–2,150 price band** — and closed the day down
**more than 27% at ₹1,560**, the single **largest listing-day fall in Indian IPO history**, wiping
out on the order of **₹38,000 crore of investor wealth on debut alone**. **[Verified, all figures.]**
Twelve months on, the divergence from 2021's other headline listings had only widened: by **22
November 2022**, Paytm shares had fallen to an all-time intraday low of **₹476.65** (closing
₹477.1) — a decline of roughly **78% from the ₹2,150 issue price**, and market capitalization was
down some **77%** from its IPO-day peak of over **₹1.38 lakh crore**. **[Verified, both figures —
the precise magnitude (≈78% at the twelve-month mark) is somewhat larger than the "≈75%" order-of-
magnitude figure this task's own framing carries; this Part adopts the more precisely sourced ≈78%
reading and flags the gap rather than silently rounding it away.]** This is the record's single
cleanest demonstration of Part D's own design point in the opposite direction from case 4: **Leg 1
spiked to a record on the back of a single mega-issue precisely as Leg 2 (the broader pop leg) was
already cracking** — a market that had just delivered Zomato's 52% and Nykaa's 80% pops absorbed a
record-size new issue with a *negative* Day-1 return, the clearest possible signature of a wave
arriving at, or just past, its own top rather than at its build phase.

**The LIC IPO, May 2022 — the wave's damp end-marker.** **LIC's IPO — ₹21,008.48 crore, India's
largest-ever at the time**, price band ₹902–949 — subscribed **~3 times overall** (67% on Day 1
alone) — but its listing was, in the words of contemporaneous reporting, "set for a lacklustre
market debut despite oversubscription." It listed **17 May 2022** down **7.8%** on debut — **the
second-worst first-day performance among the eleven global companies that raised over US$1 billion
through an IPO anywhere in 2022** — and by **9 June 2022** had fallen a further leg to stand **24%
below its issue price**. **[Verified, all figures.]** A subscribed-but-unloved debut, arriving
seven months after Paytm's own outright crash, is this record's cleanest closing signature for a
wave: not a collapse in issuance *supply* (LIC's own size confirms issuers, or in this case the
government as seller, were still willing and able to bring the largest deal in Indian history to
market) but a collapse in the market's willingness to *reward* new supply with a pop — precisely
the Leg-2 failure that marks a wave's genuine end, as distinct from Leg 1 merely running out of
deals to bring. The retail-participation overlap this wave rode — the demat-account surge and F&O
boom `docs/CYCLE_ATLAS.md` Atlas 3.6 already owns as its own row, cross-referenced not re-derived
here — is the standing domestic bid this Part's own reception figures show arriving in size for
Zomato and Nykaa, then visibly refusing to show up in the same size for Paytm and LIC seven months
apart.

**The regulatory response.** No SEBI action specific to the Paytm listing-day collapse was located
this pass (the episode is, on the public record, a market-pricing outcome rather than a disclosure
or process failure); SEBI's broader tightening of anchor-investor lock-in and pricing-disclosure
norms across 2021–22 is contextual, not a dedicated response to this wave's own top-tick episode
`[VERIFY: any SEBI-specific post-mortem or rule change directly attributable to the Paytm/LIC
episodes]`.

**What L7's two-leg state would have read.** 2021's calendar-year aggregate reads hot on both legs
through Zomato and Nykaa's own deals — but the two-leg construction's own AND-logic is precisely
what would have flagged Paytm's arrival as a warning rather than a confirmation: a record-scale Leg
1 contribution landing with an already-negative Leg 2 outcome is the textbook divergence signature
the design is built to catch, not merely a large number that happened to disappoint. `partCDEFH.md`
Part H's own established finding lists **2021** among the record's clean top-tick instances
alongside 1994–96 and 2007–08 — this case is the concrete mechanism behind that entry: the wave's
own largest single deal is where the two legs visibly came apart, seven months before the wave's own
final, confirming, damp-reception deal (LIC) closed the era out.

---

### 7. 2023–2026 — the SME frenzy and the broadening

**The mainboard build.** **FY2023–24 (FY24): 76 mainboard IPOs raised ₹61,915 crore**, up **~19–20%**
from **FY2022–23's 37 IPOs and ₹52,116 crore** — the largest single deal, **Mankind Pharma's April
2023 ₹4,326 crore** offer-for-sale, subscribed **15.3 times** on bids worth roughly **₹50,000
crore**, followed by Tata Technologies (₹3,043 crore) and JSW Infrastructure (₹2,800 crore).
**FY2024–25 (FY25): 79–80 mainboard IPOs raised over ₹1.62 lakh crore** — roughly **2.6× FY24's
total**, one of the most active fundraising years in the market's history. **[Verified, all
figures.]** Calendar-**2024 (mainboard + SME combined): 91 public offerings raised ₹1.59 lakh
crore**; calendar-**2025: 373 total issues (103 mainboard, 270 SME) raised ₹1.95 lakh crore**, the
largest calendar-year total on record, part of a **2020–2025 cumulative IPO fundraising figure of
₹5.39 lakh crore that itself exceeds the entire 2000–2020 twenty-year cumulative total of ₹4.56
lakh crore**. **[Verified, all figures.]**

**The SME-board frenzy, the wave's own genuinely new content.** **243 SME IPOs launched in 2024
(240 having debuted), raising roughly ₹8,700 crore net of anchor books** — a small fraction of the
mainboard's own rupee total but a genuinely distinct microstructure the wave brought fully into
view for the first time at this scale. **Oversubscription records were set repeatedly through the
year: HOAC Foods India at ~1,963 times (May 2024), Magenta Lifecare at ~1,003 times (June 2024)**,
and a further cluster — Green Hitech Ventures (771×), Koura Fine Diamond Jewellery (727×), Maxposure
(697×), Medicamen Organics (688×), Slone Infosystems (642×) — with **16 of the all-time top-20
SME-oversubscription list dated to 2024 alone**; the five most-overbought SME issues of the year
drew cumulative bids exceeding **₹65,000 crore against a combined ₹59.3 crore they aimed to
raise — over 1,100× in aggregate**. **[Verified.]** A genuine *central-tendency* reading, not
merely the outlier tail, is also on record for part of the year: the segment's own **average**
subscription multiple ran to **242 times in September 2024** before cooling to **112 times by
November 2024** as the frenzy's own pace decelerated intra-year — average listing gains for the
full FY24 SME cohort exceeded **50%**, with applications running to roughly **113,000 per
IPO** on average. **[Verified — an average, not the median this Part would prefer; a genuine
median-subscription series specific to the SME board was not independently located this pass
`[VERIFY: median, as distinct from mean, SME subscription multiple, 2024]`.]** **Listing-day
breadth confirms this was not a
handful-of-outlier-deals phenomenon: across FY2023–24 and FY2024–25, over 90% of SME IPOs listed at
a premium**, with **214 of the year's SME debuts closing their maiden session in the green against
just 22 closing lower**. **[Verified, all figures.]** This is the record's single clearest
instance of Leg 2 (median pop) running hot at genuinely extreme percentile levels across an entire
sub-market's breadth, not merely at its flagship deals — the SME board's own microstructure (thin
float, small deal sizes, retail-dominated books) is precisely why `partCDEFH.md`'s own Part C keeps
the SME series *separate* from the mainboard state rather than pooling them, and precisely why Part
E's algorithm treats SME as "a satellite briefing line" rather than folding it into the primary
state — "the 2023–25 frenzy showed why," as that document's own Step 1 already states.

**The regulatory response — SEBI's 2024 interventions, the ladder's own institutional
confirmation.** SEBI's board meeting of **18 December 2024** tightened SME-IPO rules directly in
response to exactly this pattern: concerns that companies were diverting IPO proceeds to
shell entities and manipulating financials through related-party transactions. The new rules
require **positive operating profit (EBITDA) in at least two of the three preceding financial
years**; raise the **minimum retail application size from ₹1 lakh to ₹2 lakh** (explicitly to
reduce retail participation in the riskiest issues); cap **general-corporate-purpose fund
allocation at 15% of issue size or ₹10 crore, whichever is lower**; cap **offer-for-sale at 20% of
the total issue size**; mandate a **monitoring agency with quarterly utilization reports for issues
above ₹50 crore**; and extend mainboard-style **related-party-transaction norms** to SME-listed
entities. **[Verified, the full rule set.]** This is precisely the episode `docs/CYCLE_ATLAS.md`
row 3.2 and `config/ladder.yaml`'s own `L7` entry both already cite as "the institutional
confirmation" of the issuance-sentiment mechanism — a regulator, observing the same froth this
Part's own oversubscription and pop statistics document, acting to curb it directly, exactly the
"a regulator acting IS a reading" design principle `partCDEFH.md` Part E's algorithm already
encodes as Step 4.

**QIP and OFS records, the wave's institutional-supply side.** **Qualified Institutional
Placements hit an all-time high in calendar 2024: roughly ₹1,37,560–1,41,482 crore raised across
95–99 QIPs** `[VERIFY: exact reconciled total and issue count — two closely-agreeing secondary
compilations differ modestly]`, up sharply from **₹54,350 crore across 45 issues in 2023** and
**75% above the prior 2020 record of ₹80,816 crore**; **FY2024–25 QIP fundraising reached ₹1.33
lakh crore**, itself a record. **Real estate dominated 2024's QIP activity, raising ₹22,320 crore**,
led by **Godrej Properties (₹6,000 crore, December 2024) and Prestige Estate Projects (₹5,000
crore)**. **[Verified, all figures.]** Alongside fresh-capital issuance, **promoter and private-
equity selling through block/bulk deals and OFS reached record scale for three consecutive years**:
**calendar-2024: ₹1.43 lakh crore**, then **calendar-2025: over ₹1.5 lakh crore** (of which roughly
**₹1.35 lakh crore ran through block/bulk deals and a further ₹18,000 crore through IPO/OFS
routes**) — the first time promoter selling has crossed the ₹1 lakh crore threshold three years
running. **[Verified.]** Notable single exits across the window include Baring PE's ~₹7,400 crore
Coforge stake sale (2023) and a May-2024 cluster (Star Health ₹2,211 crore, Cipla-promoter ₹2,725
crore, IRB Infrastructure ₹1,445 crore, Timken India ₹1,253 crore, Aptus Value Housing Finance
₹1,347 crore, Apollo Tyres ₹1,073 crore, RR Kabel ₹950 crore); **private promoter ownership of
NSE-listed companies fell to 40.58% by June 2025, an eight-year low.** **[Verified.]** This
promoter/PE-OFS dimension is precisely the third-leg candidate `partCDEFH.md` Part F already
registers as **IS-D3** — a design proposal, classification work only at this stage, not yet folded
into `L7`'s own two-leg state.

**Where the wave stands, 2025–26.** Calendar-2025's own record (₹1.95 lakh crore, 373 issues) has
not carried cleanly into 2026: **companies raised roughly US$5.78 billion through public offerings
in the first stretch of 2026, against US$7.32 billion over the same window a year earlier**, and
several closely watched candidates — Manipal Health Enterprises, Indo-MIM, and Juniper Green Energy
among them — **cut the size of their planned offerings**, while Zepto opted for a pre-IPO
placement instead of a public issue, Sify Infinit Spaces paused its offering, and PhonePe deferred
its own listing plans. **[Verified.]** This softening arrives inside a genuinely weaker secondary-
market backdrop: the **Sensex's own intraday all-time high, 85,978, was set 27 September 2024**,
and by **early September 2026 it stood near 76,944** — a decline on the order of **10–13%** from
that peak (touching a sharper ~14.5% drawdown intraday in mid-2026); the **Nifty 50's own all-time
high, 26,373, was set 5 January 2026**, and by the same date in September 2026 it had fallen to
roughly **23,100–23,200, a 12–13% decline**. **[Verified, both index peaks and the approximate
current levels; FII outflows, decelerating corporate-earnings growth off FY21–FY24's 15–20% pace,
and elevated crude/geopolitical risk are the commonly cited drivers, cross-referenced to
`globalcycle-deep`'s own May-2026 episode and `fpi-deep`'s own CY2026 flow record, not re-derived
here.]** Despite this, investment-bank forecasters (Kotak Mahindra Capital, Goldman Sachs) still
project **2026 as a potential record year — as much as US$25 billion, from 190-plus issues,
exceeding ₹2.5 lakh crore** — a genuinely open, two-sided read this Part states rather than
resolves, consistent with this program's own "states, never dates" discipline.

**What L7's two-leg state would have read.** Both legs run hot simultaneously through 2023–25 —
record mainboard and QIP volumes (Leg 1) and, distinctively, an SME sub-market running an
essentially unprecedented Leg-2 extreme (>90% premium-listing rate, four-digit oversubscription
multiples) that the mainboard/SME separation in `partCDEFH.md`'s own Part C construction is
precisely designed to surface without letting a handful of SME outliers distort the primary
mainboard state. SEBI's own December 2024 intervention is the clearest instance in this entire
record of the regulatory-action annotation (Part E Step 4) firing in close to real time on the same
signal this Part's own oversubscription statistics independently confirm — the closest this record
comes to a regulator's own real-time read matching the seat's own construction almost exactly.
Whether the 2024–25 volume-and-pop extreme was, in fact, followed by the kind of weak 12–24-month
forward secondary-market return Baker-Wurgler's own mechanism predicts is precisely what §B3(c)
below frames as this record's own live, still-resolving validation test.

---

## B3. Synthesis

### (a) The wave table

| Wave | Peak-year volume (₹, mainboard unless noted) | Reception peak | What followed (12–24m secondary-market return) | Regulatory response | L7 two-leg read |
|---|---|---|---|---|---|
| **1992–96 free-pricing boom** | FY1994–95: ~1,400 issues (exact ₹ total not pinned `[VERIFY]`); 1996–97: 882 issues, ₹14,275.98cr | Feb 1995: 78 IPOs in one week; premium-issue share 1.37%→45.90% (1991–92→1994–95) | 1997–98: 111 issues, ₹4,569.95cr (−87.4% issues, −68.0% amount, single year); GNPA 19.05%→12.16% (1997→2001), BIFR backlog cleared for another 15y | Vanishing-companies enforcement (partial, slow); CDR mechanism born 2001 | No usable percentile (pre-NSDL); qualitative both-legs-hot per `partCDEFH.md` Part H |
| **1999–2000 tech mini-wave** | FY1999–2000: 151 issues, ~₹7,817cr | Sector-concentrated tech/software mania, Nasdaq-linked | FY2000–01: ₹6,108cr (issuance already fading); 2001: Sensex ~−38% (Ketan Parekh + Nasdaq bust) — but FII flows stayed net positive through it (`fpi-deep` §B1) | Ketan Parekh secondary-market inquiry; no dedicated issuance-side reform found `[VERIFY]` | Leg 1 moderate (denominator-damped by rally-inflated mcap); Leg 2 plausibly hotter — genuinely unresolved, per-issue data not reconstructed |
| **2004–08 great wave** | 2006: 78 IPOs, $7.23bn; 2007: ~93–103 IPOs `[VERIFY]`; ONGC (2004) ₹10,694.5cr; DLF (2007) ₹9,187.5cr; Reliance Power (Jan 2008) ₹11,700cr | ONGC 6.82×; Reliance Power 73×; ~46.55% avg first-day underpricing (2002–06 study) `[VERIFY scope]` | Reliance Power −17%→−intraday low ₹355→closed ₹372.50 day one; 2008: 37–38 IPOs, $3.8bn (from 103/79 prior years); FY08–09: ₹2,034cr/21 issues; Nifty −60–65% (Jan–Oct 2008) | IPO demat-scam enforcement 2005–06 (82 financiers, 24 operators, 12 DPs barred/penalized) | Both legs hot simultaneously — the record's cleanest froth flag (`partCDEFH.md` Part H: 2007–08 named explicitly) |
| **2010–11 PSU/QIP echo** | 2010: 64 IPOs, ₹37,535cr (record); Coal India ₹15,199.4cr; RE-sector QIP ₹23,914cr (2010, up from ₹14,224cr 2009) | Coal India 15.28× | 2011 (9m): 38 issues/₹6,004cr vs 50/₹16,709cr prior year (−64%); 28 IPOs withdrawn; 26/39 issues missed min. QIB subscription; cohort lost ~1/3 of issue value by year-end | None issuance-specific found `[VERIFY]` | Leg 1 flagged froth; Leg 2 (median, not flagship) likely overstated by Coal India alone — state-supply-driven, not demand-driven, per §B2 case 4 |
| **2014–18 institutional wave** | 2017: 36 mainboard IPOs, ₹67,147–68,826cr (record, surpassing 2010); HDFC Life ₹8,695cr; HDFC AMC ₹2,800.33cr | 17/36 issues >10× sub; 18/36 >10% listing pop | IL&FS default 14 Sep 2018 → SC1's 12m SMB −24.8%/mkt −20.2% (`shadow-deep`); ₹600bn approved-but-frozen pipeline (Dec 2018); ~₹16,500cr of approvals lapsed unused (Aug 2019); CY2019: 62 issues, $2.53bn (−62% volume, −54% proceeds) | SEBI chairman's public lament (Dec 2018); resolution ran through credit-side machinery (`shadow-deep` §B2), not issuance-specific reform | Broad both-legs-hot through 2017, then external-shock collapse of both legs together — a different failure mode (credit shock, not self-correcting sentiment) |
| **2020–22 startup wave** | 2021 record calendar (aggregate `[VERIFY exact]`); Zomato (Jul21) subscribed 38.25×; Nykaa (Nov21) ₹5,300cr, 81.78×; Paytm (Nov21) ₹18,300cr (era's largest); LIC (May22) ₹21,008.5cr | Zomato +52%→ open; Nykaa +80% open; Paytm Day-1 sub only ~18% `[VERIFY final]`; LIC ~3× overall | Paytm: −27% listing day (record fall, ~₹38,000cr wealth wiped day one), −78% at 12m (Nov22); LIC: −7.8% listing day, −24% by 9 Jun 2022 | No issuance-specific SEBI action found for this wave `[VERIFY]` | Leg 1 record on Paytm's mega-issue landing exactly as Leg 2 cracked — the clean decoupling case; `partCDEFH.md` names 2021 a top-tick instance |
| **2023–26 SME frenzy/broadening** | FY24: 76 IPOs, ₹61,915cr; FY25: 79–80 IPOs, ₹1.62L cr (~2.6× FY24); CY2025: 373 issues (103 mainboard/270 SME), ₹1.95L cr (record); QIP CY2024: ~₹1.37–1.41L cr (record, +75% vs 2020's ₹80,816cr) | SME: >90% listed at premium; HOAC Foods ~1,963× sub; 214/236 SME debuts positive | Sensex ATH 85,978 (27 Sep 2024) → ~76,944 (Sep 2026), ~10–13% off peak; Nifty ATH 26,373 (5 Jan 2026) → ~23,100–23,200 (Sep 2026), ~12–13% off peak; 2026 issuance pace softening ($5.78bn vs $7.32bn YoY, several deals cut/deferred) | SEBI SME-IPO curbs, 18 Dec 2024 (EBITDA test, ₹2L min. retail ticket, 20% OFS cap, 15%/₹10cr GCP cap, monitoring agency); promoter/PE OFS record ₹1.43L cr (2024) then >₹1.5L cr (2025), 3rd straight year >₹1L cr | Both legs hot, SME extreme on Leg 2 specifically; SEBI action = regulator-read confirmation in near-real-time; IS-D3 (OFS third leg) registered as a design candidate, not yet live |

### (b) The Baker-Wurgler scorecard for India, qualitative, wave by wave

Read across all seven waves, the record supports the mechanism with real force but not without
genuine exceptions this Part states honestly rather than smoothing over. **Four waves show the
clean Baker-Wurgler signature — heavy issuance (both legs hot) followed, within 12–24 months, by
materially weak secondary-market returns**: **1994–96** (record volume and reception → the 1997–98
primary-market collapse and a multi-year real-economy overhang); **2004–08**, with **Reliance
Power's January 2008 top-tick** the single cleanest individual-deal instance in the entire record
(a 73×-oversubscribed IPO closing lower on day one, five weeks before the broader index's own
collapse); **2020–22**, with **Paytm's November 2021 listing** the cleanest instance of the two legs
*decoupling* right at the top rather than confirming each other; and **2023–26**, whose own
12–24-month forward window is still resolving as of this writing but whose index-level backdrop —
the Sensex's own 27 September 2024 all-time high arriving inside the same window as record FY24/
FY25 issuance, followed by a 10–14% drawdown into 2026 — is, on the record available today,
directionally consistent with the same pattern. **Two waves show a genuinely different, and
instructive, failure mode**: **2010–11**, where Leg 1 (state-engineered PSU disinvestment supply)
ran hot while Leg 2's *median* reception plausibly did not confirm as strongly as the Coal India
flagship implied — a case for reading the legs separately, not for the mechanism failing outright;
and **2014–18**, where the primary market's own collapse was **triggered externally** by a credit
shock (IL&FS) rather than by the issuance wave correcting its own excess — the two-leg state read
correctly (broad hot reception through 2017, broad cold reception from late 2018) but for a reason
the seat's own construction was never built to attribute. **One wave (1999–2000) remains genuinely
unresolved** on the evidence this pass could independently verify: issuance volume itself faded
ahead of the 2001 crash (consistent with issuers selling into strength before it ended), but a
clean per-issue reception dataset to confirm or reject a genuine both-legs-hot reading was not
reconstructable this pass. The desk's own honest summary: **India's issuance record supports Baker-
Wurgler's mechanism in the majority, and in the clearest, cases — but at least two waves show the
mechanism can be confounded by a supply-side (state disinvestment) or an external (credit-shock)
driver that the two-leg construction alone cannot distinguish from genuine sentiment-driven excess**,
precisely the honest caveat `research/CONTRACT.md` §5's own survival-argument discipline requires
this Part to carry forward rather than paper over.

### (c) The two validation episodes for the data-gated IS test

`config/ladder.yaml`'s own `changes_if` clause for `L7` names exactly two episodes as the
pre-registered validation set — **"India pre-registered test vs 2018/2023-24 episodes"** — and
`partCDEFH.md` Part F already registers the design as **IS2**, "the 2018/2023-24 episode shape
check — the ladder's own `changes_if`," alongside the more general **IS1** Baker-Wurgler India test.
Neither has been run: per `research/CONTRACT.md` §12, this research phase permits no backtests, no
data acquisition, and no model code — what follows is the pre-registration this Part's own case
record is positioned to support, stated before any data is pulled, not a result.

**2018 — the credit-shock confound, stated as the test's own null-hypothesis stress case.** §B2
case 5's own record shows the two-leg state reading *correctly* cold through late 2018 and all of
2019, but for a reason (an external NBFC funding-run) the seat's own construction does not itself
observe. **IS2's own design question for this episode**: does a *pre*-2018 two-leg reading (the
2017 broad-hot state, independently confirmed on both legs above) show genuine predictive lead
before the IL&FS trigger, or does the state only turn cold *after* the freeze is already visible in
the issuance calendar itself — i.e., is `L7` a leading regime indicator here, or a coincident one
riding on the same credit-shock transmission `shadow-deep/shadow-RESULTS.md`'s own SC1 trial
already shows arrives with a roughly 12-month lag into equity factors generally? A pre-registered
test that finds `L7` merely coincident with, rather than leading, the 2018 freeze would not
falsify the seat's Tier-B status (the Baker-Wurgler mechanism's own global evidence stands
independently) but would argue for a narrower interpretation of what the India-specific coefficient
can honestly claim to add.

**2023–24 — the live, still-resolving case, stated as the test's own cleanest currently-available
instance.** §B2 case 7's own record shows both legs running hot through FY24–FY25 with no
comparable external-shock confound yet identified — the closest this record comes to an
uncontaminated Baker-Wurgler instance since 2007–08. The Sensex's own all-time closing high (27
September 2024) arrived inside the same calendar window as the FY24/FY25 record issuance pace and
the SME frenzy's own extreme Leg-2 readings; the index's subsequent 10–14% drawdown into
2026 — alongside the demonstrated early-2026 softening in fresh issuance pace itself (§B2 case 7's
own final paragraph) — is, on the evidence available as of this writing, directionally consistent
with the mechanism, but the 24-month window from the FY24/FY25 issuance peak has not yet fully
elapsed as of September 2026, and this Part deliberately declines to call the episode's own
forward-return outcome settled ahead of that window closing, consistent with this program's
"states, never dates" discipline (echoed identically by `globalcycle-deep` and `fpi-deep` for their
own live 2025–26 episodes). **IS2's own design question for this episode**: once the full
24-month window has elapsed, does the magnitude of the 2024–2026 drawdown scale with the
independently-measured two-leg extremity of the FY24/FY25 issuance peak (a genuine dose-response
test), or is the drawdown better explained by the FII-outflow and earnings-deceleration drivers
this Part cross-references to `globalcycle-deep` and `fpi-deep` without re-deriving — i.e., does
`L7` add explanatory power *on top of* the ladder's own macro/flow blocks, or is it substantially
redundant with signals the `valuation_sentiment` block already shares budget with via `L8`? Both
questions are exactly what a purged, out-of-sample IS2 trial — run only once India-specific bhavcopy
and SEBI-bulletin data are pulled per `partCDEFH.md`'s own runsheet addendum 15 — is built to
answer; this Part's own contribution is the qualitative case record, era by era, that trial will be
tested against, not a substitute for running it.

---

## References

Baker, M. & Wurgler, J. (2000). "The Equity Share in New Issues and Aggregate Stock Returns."
*Journal of Finance* 55(5): 2219–2257. · Baker, M. & Wurgler, J. (2002). "Market Timing and Capital
Structure." *Journal of Finance* 57(1): 1–32. · SEBI Annual Report 1997–98 (the 1996–97/1997–98
issuance-collapse table); SEBI board decisions, 18 December 2024 (SME-IPO rule tightening). ·
Business Standard, BusinessToday, Moneylife, TechCrunch, and other contemporaneous financial-press
reporting for every dated issuance, subscription, listing, and index figure throughout, per the
`[VERIFY]` discipline stated at each figure's first use. · `research/cycles/capex-deep/
partB-cases.md` (case 1's 1994–97 primary-market chronology, GNPA/BIFR data, and case 2's Reliance
Power "top-tick artifact" framing — cross-referenced throughout, never re-derived here). ·
`research/cycles/fpi-deep/partB-cases.md` (the October 2007 P-note FLOW episode, the 2000–01/
2001–02 flow-vs-return divergence, and the 2013 single-pool-blind-spot motif this Part's own §B2
case 5 borrows) and `research/cycles/globalcycle-deep/partB-cases.md` (the May-2026 episode
anatomy) — both cross-referenced, not re-derived. · `research/cycles/shadow-deep/partB-cases.md`
and `shadow-deep/shadow-RESULTS.md` (the IL&FS funding-run anatomy and the SC1 12-month
factor-propagation trial). · `research/cycles/issuance-deep/partCDEFH.md` (the seat's own Parts
C–H: the two-leg `state_t` construction, the IS1/IS2/IS-D3 test designs, and the SME/mainboard
split — the machinery this Part's case record is written to be tested against). ·
`docs/CYCLE_ATLAS.md` row 3.2 and `config/ladder.yaml`'s `L7_issuance_sentiment` entry. ·
`research/CONTRACT.md` §4 (evidence tiers), §5 (the signal-survival test), and §12 (research-phase
rules: no backtests, no data acquisition).

---

*Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · 2026-09-02 ·
v1.0*
