# PART B — The FPI positioning-era case record: five eras, one capacity mechanism

*FII/FPI flow-cycle monograph (atlas 2.13; ladder seat `L14_fii_positioning`, `config/ladder.yaml`,
Tier C, reduce-only, positioning `tau_half` 12–36 months) · Part B · v1.0 · 2026-09-02 · Author:
Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. This Part reads `docs/CYCLE_ATLAS.md` row 2.13 ("Flows FOLLOW returns
[Griffin-Nardari-Stulz; Chakrabarti] — flow *momentum* is the decayed, excluded signal. What
survives is *positioning extremes*: unwinding an extreme foreign-ownership stock takes real capital
and time [capacity mechanism]"), `config/ladder.yaml`'s `L14_fii_positioning` entry ("float-scaled
FII ownership percentile extremes; risk-off only"), and this record's own house style
(`research/cycles/fincycle-deep/partB-cases.md`: numbers-forward, every figure sourced, `[VERIFY]`
where a search pass could not pin a primary table, interpretation written honestly after the numbers
rather than fitted to a thesis). **Scope, stated once and held throughout: this Part owns the
FLOW/POSITIONING record** — verified flow magnitudes, the ownership-share arc, what returns did
*before* the flows in each era, and the unwind mechanics where applicable — **not the global-episode
anatomy** several of these same windows also carry, which belongs to a sibling chapter and is
cross-referenced by name, never re-derived: `research/cycles/globalcycle-deep/partB-cases.md` owns
the 2008, 2013, 2020, and 2022 GLOBAL triggers in full — the VIX/dollar/US-rate triad, the trigger
dating, the swap-line hierarchy — this Part borrows only the dates and cites the flow-relevant
figures already verified there rather than re-deriving them; `research/cycles/mpcycle-deep/
partB-cases.md` case 4 and `research/cycles/shadow-deep/partB-cases.md` §B5 own the 2013 domestic
rates defense (the MSF corridor inversion, the FCNR(B) swap window, the rates-not-credit signature)
in full, cross-referenced not re-derived. This Part carries no theory of its own beyond what grounds
each era's flow chronology; the formal flows-follow-returns argument and the capacity-mechanism
survival case belong to this seat's own sibling theory chapter (`partA-theory-psychology.md`, if/when
written), cited here, not restated. Primary-source RBI/SEBI/NSDL series were not directly queryable
this session (egress blocked at the network proxy per `research/CONTRACT.md` §7 Known Prior #11 —
confirmed again this pass: `www.sebi.gov.in` returned an EGRESS_BLOCKED result), so every figure below
is cross-checked against secondary financial-press and SEBI/NSDL-sourced-but-secondarily-reported
tables, exactly as this program's house style requires.*

---

## B0. The empirical anchor, before the eras

**The mechanism this whole record tests.** Griffin, Nardari & Stulz's cross-country finding — that
foreign investors are, on average, positive-feedback traders whose flows follow past returns rather
than lead them — and Chakrabarti's India-specific finding that the relationship strengthened
structurally after the 1997–98 Asian crisis (domestic equity returns becoming, on his reading, close
to the *sole* statistically robust driver of subsequent FII flows) are both already cited, not
re-derived, in `config/ladder.yaml`'s own `L14_fii_positioning` entry as the reason the design
excludes flow-momentum outright (`docs/CYCLE_ATLAS.md` §7's rejected list: *"FII flow momentum
(directional) — flows follow returns; published, decaying, and DII/SIP growth absorbs it"*)
`[VERIFY: exact venue/year for Chakrabarti's paper — a 2001 ICRA Bulletin: Money & Finance piece,
"FII Flows to India: Nature and Causes," is the best-matching title this pass's search located,
consistent with the citation already standing in the ladder and atlas, but not independently
re-opened and re-read this session]`. **What survives instead is a positioning-extreme, capacity-based
signal**: when foreign ownership of a name (or the market) sits at an extreme percentile of free
float, unwinding that position — should sentiment turn — requires a domestic (or other foreign) buyer
to absorb real size inside a real time window; that absorption capacity is what `L14` is built to read,
never a bet on which direction flows will move next. `config/ladder.yaml` encodes this literally:
Tier C, `reduce_only: true`, `block: tierC_overlay`, role *"float-scaled FII ownership percentile
extremes; risk-off only"* — consistent with `research/CONTRACT.md` §4's own governing rule that
Tier-C signals (fewer than four observed complete periods; positioning `tau_half` here is a 12–36
month prior, not a clock) may only **reduce** risk, never add it. Every era below is read against
this single design question: what did the ownership-share arc actually do, what did returns do
*before* the flows that moved it, and — where an unwind occurred — what absorbed it.

**The budget the seat sits in, stated once for the whole record.** `config/ladder.yaml` places
`L14_fii_positioning` inside `block: tierC_overlay`, governed by a single `tierC_overlay_cap: 0.10` —
a **negative-only** shift of at most 10 percentage points off the regime score `R`, shared with every
other Tier-C reduce-only seat on the ladder (`L1` 1-month reversal, `L13` household debt, `L15` the
long-wave fiscal arc). `L14` never competes for budget against the Tier A/B REGIME blocks
(`fast_stress`, `trend_tsmom`, `macro_credit_block`, `global_cycle`, `valuation_sentiment`, `calendar`
— together summing to the remaining 1.0 of additive budget); it can only pull the aggregate score
*down*, and only by a bounded amount, no matter how extreme its own percentile reading. This is the
concrete budget mechanics behind the "Tier-C signals may only reduce risk" rule (`research/
CONTRACT.md` §4) — worth stating explicitly here because §B5's own honest question (whether a LOW
positioning extreme should ever push exposure *up*) is, read against this budget architecture, not
merely a design preference but a hard structural constraint: there is no positive-direction lever for
`L14` to pull even if the argument for one existed.

**A comparability note, stated once rather than repeated five times.** These five eras are not five
draws from one stationary process. India's capital account was a metered, single-digit-cap valve in
1993 and is a considerably deeper (though still managed) one in 2026; the *ownership-share* series
this Part tracks is therefore not comparable across its own full length in the way a percentile rank
implicitly assumes — precisely the same caution `globalcycle-deep/partB-cases.md`'s own B0 states
about its parallel GF-series, and precisely why `L14`'s own percentile construction should be read,
per `partCDEFH`-style design discipline elsewhere in this ladder, against a rolling or era-aware
baseline rather than a single 1993–2026 constant.

---

## B1. 1993–2002 — the arrival era: ownership building from zero

**The entry framework, cross-referenced not re-derived.** SEBI's September 1992 guidelines opened
Indian equity and debt markets to registered Foreign Institutional Investors for the first time, under
a deliberately staged design — per-company investment caps starting in the single-digit percentage
range of paid-up capital, a small number of registered custodians, and an overwhelming equity (not
debt) tilt — the full framework is `globalcycle-deep/partB-cases.md` §B1's own subject; this Part's
contribution is what that valve actually pushed through, in flow and ownership terms, across its
first decade.

**The build, month by month at first, then year by year.** FII net investment stood at **₹2,595 crore
in 1993**, with monthly net inflows rising from **$0.18 million (Jan 1993) to roughly $400 million
within a year**. **[Verified, cross-checked against `globalcycle-deep`'s own citation of the same
figures.]** The pace kept building for three more years: **1996–97 net FII investment reached
US$2,431.9 million, the highest yearly level since FIIs began investing** — with **April 1996 alone
recording the highest monthly net investment, US$433.6 million, of any month since entry**.
**[Verified, SEBI Annual Report data.]** By this point the arrival era's ownership-building had a
first genuine growth narrative behind it (India's own mid-1990s reform-led growth acceleration,
alongside a global emerging-market allocation wave) — a returns-led-flows pattern already visible in
miniature: 1996's record year followed, rather than preceded, the market's own 1993–94 post-reform
rally.

**The first mini-exodus, precisely dated.** **1997–98 net FII investment fell to US$1,650.1 million,
a 32% decline from 1996–97** — and, more tellingly, **monthly net FII investment turned negative for
the first time in the record, in November 1997, December 1997, and January 1998**, with net sales of
**US$372.6 million** across those three months. **[Verified, SEBI data.]** This is the Asian-crisis/
Pokhran-overlay window `globalcycle-deep/partB-cases.md` §B2 dates and reads for its GLOBAL and
domestic-rates-defense content (the Bank Rate 9%→11% move, the Pokhran sanctions) in full; this
Part's own contribution is that the negative-flow window did not, on the annual print, stay contained
inside FY1997–98 — it deepened into the **following** fiscal year: **1998–99 recorded a full-year net
FII OUTFLOW of ₹1,584.5 crore**, the arrival era's only complete fiscal year of net foreign selling.
**[Verified.]** This is the more precise dating of the task's own "1997–98 mini-exodus" framing: the
negative monthly window opened in November 1997, but it was FY1998–99 — spanning the Pokhran
sanctions' persisting overhang and continued regional contagion — that closed the books net negative.
The reversal was sharp and immediate: **1999–2000 net FII investment rebounded to ₹10,121.93 crore**,
a swing on the order of ₹11,700 crore in one fiscal year, and cumulative FII net investment since
September 1992 **crossed the US$10 billion mark on 8 December 1999**, reaching **US$11.23 billion by
31 March 2000**. **[Verified, both.]** The 1999–2000 rebound is itself a returns-led-flows exhibit:
it tracks India's own IT-and-reform-led 1999 rally (and the broader global dot-com-era risk appetite)
rather than preceding it — flows arriving once the rally was already visibly underway, the same
lag structure the era's whole record will keep confirming.

**The second "mini-exodus" that the data does not, in fact, show as a full-year outflow — an honest
finding, not a forced fit.** The task's own framing names a "2000–01 mini-exodus" alongside 1997–98,
and the qualitative history supports the label: the Ketan Parekh "K-10" stock-manipulation scandal
unwound from March 2001, compounding the global dot-com bust (NASDAQ's own collapse), and the Sensex
fell on the order of **38% during 2001** `[VERIFY: precise peak-to-trough Sensex dating for the 2001
crash — the 38% figure recurs across secondary retrospectives but a primary-index daily series was
not independently re-derived this pass]`. What this pass's search could verify at the **flow** level,
however, is more nuanced than a clean second exodus: **April 2000–January 2001, the ten months this
pass could pin, show a cumulative net FII inflow of roughly US$1,378.8 million**, with isolated
negative months inside that window (**June 2000: −US$218.1 million; July 2000: −US$317.3 million**)
rather than a full-year net outflow; **April 2001–January 2002 shows a similar pattern, roughly
US$1,295.0 million net inflow over the ten-month window, with September 2001 negative (−US$88.2
million)**, plausibly compounded by the global post-9/11 risk-off shock landing in the same month as
the still-unwinding Ketan Parekh fallout. **[Verified, both windows, per an Economic Survey table
citing SEBI.]** The honest read this Part owes the record: registered FII **flows** stayed net
positive through both fiscal years even as **returns** collapsed by nearly 40% — a genuinely different
pattern from 1998–99's (where both flows and, on the qualitative record, returns turned negative
together) and from every later crisis in this record (2008, 2013, 2020, 2022), where flows and
returns moved together on the way down. `[VERIFY: whether a fuller monthly series across the missing
February–March windows of both fiscal years would flip either full year to net negative — this
pass's search located only the ten-month sub-windows above]`. If this holds up under a fuller data
pull, 2000–01/2001–02 is best read not as a flow exodus at all but as a **domestically-generated**
crash (a market-manipulation unwind plus a global tech-bust echo) that foreign portfolio flows did
not meaningfully participate in selling into — a finding worth carrying into the data phase's own
pre-registered FL1 trial rather than asserted here as settled.

**Ownership arc, arrival era.** No usable float-scaled ownership-percentile series exists this early:
the capital account was too newly opened, and too thin in absolute rupee terms relative to the
domestic float, for a meaningful "extreme" reading to exist — the identical finding
`globalcycle-deep/partB-cases.md` §B1 reaches for `L9` in 1994. **What L14's state would have read**:
nothing, for the same structural reason — a seat built to read positioning *extremes* has no
percentile to compute against when the underlying stock of foreign holdings is itself still being
built from a near-zero base across the whole decade. The one genuine "reading" this era offers is a
directional one, not a percentile one: ownership was rising net, decade over decade, off a standing
start, interrupted by exactly one full-year reversal (1998–99) that recovered within a single
subsequent fiscal year.

---

## B2. 2003–2008 — the great inflow wave: P-note mania and the flows-follow-returns exhibit par excellence

**The build.** India's 2003–2007 bull run coincided with — and was substantially financed by — the
decade's largest sustained FII inflow wave to that point. This pass's search could independently
verify the **2004–2007 window's cumulative figure: FIIs poured US$46.4 billion into Indian markets**
across those four years. **[Verified.]** A precise FY2003–04-through-FY2007–08 five-year cumulative
total (spanning slightly wider than the 2004–2007 figure above) could not be independently pinned this
pass to a single primary table `[VERIFY: the exact FY04–FY08 five-fiscal-year cumulative figure —
the $46.4bn 2004–2007 calendar-year figure is the closest independently verified anchor; a fuller
FY03–08 total plausibly runs somewhat higher once FY2007–08's own record year is folded in]`, but the
order of magnitude is not in serious dispute across the retrospective literature this pass surveyed:
this is, on any reasonable accounting, the largest cumulative FII inflow wave in the record to that
point, roughly quadrupling the entire 1992–2000 cumulative stock (US$11.23 billion) inside a single
four-to-five-year window.

**Returns led this wave, not the reverse — stated plainly because it is the era's central lesson.**
India's own growth acceleration (the capex-and-credit boom `research/cycles/capex-deep/` and the
fincycle monograph's own India case document from the real-side and property-side respectively) and
a broadly re-rating Sensex/Nifty were already running before the inflow wave reached its own record
pace — the Sensex crossed 10,000 in February 2006 and kept climbing through 2007, the market's own
re-rating substantially preceding, not following, the peak years of the FII inflow figures above; the
wave's own composition — increasingly routed through Participatory Notes (offshore derivative
instruments issued by registered FIIs against underlying Indian securities, letting unregistered
foreign funds and hedge funds gain India exposure without direct SEBI registration) — is itself
evidence of return-chasing capital arriving *because* the rally was already visible and liquid enough
to write derivatives against, not capital that manufactured the rally from a standing start.

**The October 2007 P-note episode — the flows-follow-returns exhibit named in the task, reconstructed
in full.** By 2007, **Participatory Notes accounted for roughly 50% of total FII investment in Indian
equities** `[Verified, per contemporaneous reporting]` — the clearest single statistic of how far
return-chasing, indirect foreign capital had penetrated the market by the wave's peak. On **16 October
2007**, SEBI floated a **draft** proposal to curb PN issuance, citing concerns that PNs obscured the
true identity of underlying beneficial owners and could channel unregulated, potentially destabilizing
hedge-fund flows into Indian equities. **[Verified.]** The draft's own **lack of clarity on scope and
transition** — not a change in any fundamental — triggered a **pure regulatory-shock crash the very
next trading session**: on **17 October 2007**, within roughly one minute of the opening bell, the
Sensex fell **1,744 points, on the order of 9% of its value — the largest intraday points fall in
Indian stock-market history to that date** — automatically triggering a **one-hour trading halt**.
**[Verified.]** After the Finance Minister issued same-day clarifications that the government was
"not against FIIs" and was not immediately banning PNs, the market staged a **remarkable same-day
recovery**, closing at **18,715.82, down just 336.04 points (roughly 1.8%) from the prior close** —
having touched an intraday low of **17,307.90**. **[Verified, all figures.]** SEBI's board finalized
the actual regulation on **25 October 2007**: FIIs and sub-accounts were barred from issuing or
renewing PNs with **derivatives as the underlying** with immediate effect, existing such exposures had
to be wound down within **18 months**, and total PN issuance was capped at **40% of an FII's assets
under management**. **[Verified.]** A partial rollback of some restrictions reportedly followed in
**October 2008** amid the separate, much larger GFC-driven exodus `[VERIFY: the exact terms and date
of the 2008 "SEBI rolls back P-Note curbs" episode — a contemporaneous headline confirms the event but
this pass did not independently re-open and verify the article's own dated specifics]`.

**Why this episode is the record's cleanest flows-follow-returns exhibit, stated explicitly.** No
fundamental changed on 16–17 October 2007 — no earnings surprise, no macro data print, no global
shock. What moved was a **regulatory proposal about the flow-delivery mechanism itself**, and the
market's own reaction split cleanly into two legs that together make the whole record's point: (i) the
**initial 9% crash** shows how much of the 2007 rally's *marginal* buying pressure had come to depend
on PN-routed capital specifically — remove clarity about that channel's future and the market's own
domestic price-discovery mechanism briefly failed to find a bid; (ii) the **same-day ~80% recovery of
the initial loss** shows that even in 2007 — with the domestic institutional/retail base far shallower
than it is by the 2020s (§B5 below) — real domestic buying interest existed and reasserted itself
within hours once the policy uncertainty was clarified, not days or weeks later. The episode is,
in miniature, the entire flows-follow-returns thesis: a wave of capital that had followed an
already-visible rally into an ever-more-derivative-routed structure, reacting violently to a threat
against its *own delivery mechanism*, not to any change in the return prospects the capital had
originally followed in.

**The 2008 exodus — the unwind, with returns leading down as violently as they had led up.** The full
GLOBAL-trigger anatomy (Lehman, 15 September 2008; the VIX's all-time 89.53 intraday high; the Fed's
sprint to the zero bound; the swap-line exclusion) is `globalcycle-deep/partB-cases.md` §B3's own
subject, cross-referenced not re-derived. This Part's own flow-and-ownership record: **FIIs withdrew
an estimated US$13 billion from Indian equities in calendar 2008, a cumulative ~US$15.4 billion across
January 2008–March 2009** — the figure this Part adopts, cross-checked against `globalcycle-deep`'s
own independent citation of the same two numbers, in preference to a commonly circulated but less
precisely sourced **"~US$12 billion"** figure this task's own framing initially carried
`[VERIFY: the ~$12bn figure recurs in some secondary retrospectives but this pass's search could not
independently anchor it to a primary total distinct from the $13bn/$15.4bn pair both this Part and
`globalcycle-deep` independently verified; treated here as the same order-of-magnitude estimate under
a different accounting window, not a contradiction requiring reconciliation]`. Nifty's fall from its
January 2008 peak (~6,357) to its October 2008 trough (~2,252) — on the order of 60–65%
`[VERIFY: exact levels, per `globalcycle-deep` §B3's own flag]` — is the clean confirmation that
**returns collapsed in lockstep with the outflow**, not ahead of or behind it, the mirror image of the
wave's own build. **The unwind mechanics**: with India's own domestic institutional base (mutual funds,
insurers) still a fraction of its later-decade size, and with no Fed swap line extended to India
(`globalcycle-deep` §B3's own finding), the exodus met essentially no absorbing counterweight — FII
selling pressure transmitted close to one-for-one into both the rupee (₹39.27→₹52.1, a FY09
depreciation of 21.9%) and the equity index, a genuinely different unwind arithmetic from the one
§B5 below documents for FY22. The reversal, once it came, was equally violent and equally
returns-led-not-leading: **FIIs poured US$60.31 billion into Indian equities from March 2009 to
November 2010**, arriving once the market had already begun its own V-shaped recovery from the March
2009 trough, not before it.

**Ownership arc, 2003–2008.** The float-scaled ownership percentile this era built is precisely the
one `L14`'s own construction is meant to flag: a genuinely fast climb from the arrival-era's low base
toward what §B4 below documents as the record's eventual all-time peak (reached a few years later, in
2015, once the 2008 unwind and the 2009–10 rebuild are both netted through). **What L14's state would
have read**: a rising, then extreme-high, ownership percentile through the 2007 P-note peak — the
correct regime read ahead of a genuine capacity-constrained unwind, though (consistent with this
ladder's own "states, never dates" discipline, echoed identically in `globalcycle-deep` and
`fincycle-deep`) a percentile extreme by itself would have said nothing about **when** October 2007's
regulatory shock, specifically, would arrive, nor that the far larger 2008 unwind was still a year
away.

---

## B3. 2009–2014 — the QE-era return: the equity/debt split lesson

**The global liquidity backdrop, named because this era's own label depends on it.** The Federal
Reserve ran three successive large-scale asset-purchase programs across this era: **QE1 (25 November
2008–31 March 2010)**, **QE2 (3 November 2010–29 June 2011, $600 billion in Treasuries)**, and **QE3
(13 September 2012–29 October 2014, open-ended, $85 billion/month at launch)**. **[Verified, all
three.]** This is the dollar-liquidity supply side of the global financial cycle `globalcycle-deep/
partB-cases.md`'s own GF1–GF3 trials and B0 discussion already ground in full (Rey's dilemma-not-
trilemma framing, cited there not restated here); this Part's own contribution is only that the era's
two record FII inflow years (§B3 below) and the 2013 taper stress both sit inside, and are plausibly
substantially explained by, this same three-program QE arc — the record inflow years arriving during
QE1/QE2's active windows and immediately after QE3's launch, the taper stress arriving the moment
markets priced QE3's own eventual withdrawal, a background liquidity mechanism this Part borrows
rather than re-derives.

**The build, restated in flow terms.** **2009–10 net FII inflows totaled US$29,048 million**, and
**2010–11 added a further US$29,422 million** — together consistent with, and the annual-year
decomposition of, the US$60.31 billion March-2009–November-2010 cumulative figure already verified in
§B2 above and in `globalcycle-deep`'s own §B3. **[Verified, both years.]** This is the clean
continuation of the flows-follow-returns pattern: the record inflow pace of 2009–10 followed, rather
than preceded, the market's own recovery, which had already begun from the March 2009 trough before
the inflow wave reached its own peak monthly pace.

**2013 — the equity/debt split, the era's central lesson, cross-referenced not re-derived for its
domestic-defense mechanics.** The full GLOBAL trigger (Bernanke's 22 May 2013 taper testimony, the
Fragile Five grouping) belongs to `globalcycle-deep/partB-cases.md` §B4; the domestic rates-defense
mechanics (the 15 July 2013 MSF hike to an effective 10.25%, the FCNR(B) swap window mobilizing
~US$26 billion directly and ~US$34 billion in aggregate September–November 2013) belong to
`mpcycle-deep/partB-cases.md` case 4 and the NBFC-side negative control belongs to
`shadow-deep/partB-cases.md` §B5 — none re-derived here. **This Part's own contribution is the
flow-composition lesson those chapters' own headline rupee-collapse figures obscure**: 2013's stress
was **overwhelmingly a DEBT-side FPI event, not an equity-side one**. **Net FII inflows for the full
fiscal year 2013–14 were a comparatively modest US$5,009 million** — positive on the year, not a full
equity exodus — **[Verified]**, even as the rupee fell some 28% (₹55→₹68.85) over the acute April–
August 2013 window and the MSF/FCNR(B) defenses were mounted specifically against **debt-market and
FX pressure**, not an equity-ownership unwind. The precise FPI-debt-outflow magnitude for the
April–August 2013 window specifically could not be independently pinned to a primary figure this pass
`[VERIFY: a precise FPI-debt-outflow total for the acute 2013 window — `globalcycle-deep` §B4 flags
the identical gap]`, but the qualitative shape is unambiguous and independently corroborated across
both this Part's own search and the cross-referenced chapters: **India's own capital-account
architecture treats FPI debt and FPI equity as distinct pools with distinct limits and distinct
investor bases (sovereign-and-corporate-bond-focused fixed-income funds on the debt side, equity
long-onlys and hedge funds on the equity side)**, and 2013 is the record's cleanest demonstration that
a global rates shock can hit one pool hard while leaving the other comparatively undisturbed — the
same lesson `globalcycle-deep` §B4 draws for the **triad** (rates/dollar-led, VIX quiet) restated here
for the **flow composition** specifically: an `L14` construction built on **equity** ownership
percentiles alone, as `config/ladder.yaml`'s own indicator list specifies (float-scaled ownership,
quarterly shareholding patterns), would have substantially **under-read** 2013's actual stress, because
the stress landed predominantly in a pool the seat is not built to watch — directly analogous to the
sanctions-driven gap `globalcycle-deep` §B2 documents for `L9` in 1997–98, and to the oil-channel gap
its §B9 documents for the May-2026 episode. This is not a design flaw unique to `L14`; it is the same
general lesson this ladder's own cross-episode record keeps returning: a single-pool, single-leg seat
reads its own pool correctly and says nothing reliable about an adjacent one.

**The 2014 election-year wave.** **Net FII inflows for FY2014–15 surged to US$40,923 million**, a
more-than-eightfold jump from FY2013–14's US$5,009 million. **[Verified.]** The proximate trigger —
the May 2014 general election delivering a single-party parliamentary majority for the first time in
three decades, read by foreign allocators as a mandate-clarity event — sits in this ladder's own
`L5_calendar_windows` and Atlas 3.7's domain (timing is law, direction is the surprise: 2004's
election delivered a −15.5% shock, 2009's a +10.7% relief rally, 2024's a −5.9% mild disappointment
`[figures per Atlas 3.7, cited not re-derived]`); this Part's own contribution is only the flow
magnitude, and the same returns-led-flows shape recurs once more: **the market's own post-election
rally began on results day (16 May 2014) and the record inflow figure is a full-fiscal-year total that
necessarily includes, rather than precedes, that rally** — flows following a return event whose
direction and rough magnitude were themselves the news, not flows anticipating it.

**Ownership arc, 2009–2014.** The 2009–10 rebuild pushed ownership back toward, and past, its
pre-2008 percentile; 2013's debt-side stress left the equity-ownership percentile comparatively
undisturbed (consistent with the flow-composition finding above); 2014's post-election wave then
pushed the percentile toward what §B4 documents as the record's eventual peak, reached the following
year. **What L14's state would have read**: a HIGH-and-rising equity-ownership percentile through
2014, correctly flagging a maturing positioning extreme even as the seat's own construction would have
said nothing distinctive about 2013's actual (debt-pool) stress specifically — the single clearest
illustration in this Part's own record of why the seat's role is capped at REGIME (reduce-only) rather
than treated as a complete account of "foreign-flow stress" in a given year.

---

## B4. 2014–2019 — the plateau and the FPI regime: peak ownership, then the DII counterweight's first appearance

**The reclassification.** SEBI notified the **Foreign Portfolio Investors (FPI) Regulations on
7 January 2014**, repealing the 1995-vintage FII Regulations; the new FPI regime, merging the FII and
Qualified Foreign Investor (QFI) categories into a single harmonized investor class, **commenced on
1 June 2014**, with legacy FII/sub-account registrations processed under the old rules through a
transition window extending to 30 June 2014; the RBI separately replaced the Portfolio Investment
Scheme with a new Foreign Portfolio Investment scheme under FEMA the same year. **[Verified, the full
sequence.]** The 2014 regulations sorted registrants into **three risk-graded categories** (roughly:
sovereign/regulated entities, regulated but broader funds, and unregulated/high-risk entities);
SEBI collapsed this to **two categories on 23 September 2019**, folding government/government-related
investors, pension and university funds, and — notably — all regulated insurance entities and
FATF-member-country-regulated funds into a single **Category I**, with the residual (unregulated
managers from non-FATF jurisdictions) in **Category II**, explicitly to ease registration and cut
redundant compliance friction. **[Verified, both the 2014 three-tier structure and the 2019
simplification.]** The reclassification is a nomenclature and registration-architecture change, not a
break in the underlying flow or ownership series this Part tracks — every figure in §B3 above and §B5
below spans the FII-to-FPI relabeling without a discontinuity, and this record follows the same
convention, using "FII" and "FPI" as the contemporaneous sources themselves do rather than imposing a
hard cutover date on the flow series. The 2019 simplification is itself a minor structural echo of the
era's own larger theme: a regulatory apparatus steadily lowering friction for foreign capital to
enter and exit even as, per this era's own ownership-arc finding below, that capital's *share* of the
market was already past its peak and beginning a decade-long retreat — regulatory ease and ownership
share moving in opposite directions across the same years.

**Peak ownership, precisely dated.** **FPI holding value in NSE-listed companies reached a record
₹19.4 lakh crore in the March 2015 quarter**, and — on a free-float basis, the metric this ladder's
own `L14` construction targets — **FPI ownership peaked at 22.5% in March 2015**, the highest reading
anywhere in this record's full 1993–2026 span. **[Verified, both figures.]** The FII-to-DII ownership
ratio reached **1.99 in the same March 2015 quarter** — also the record's own peak reading on that
ratio. **[Verified.]** This is the concrete number behind the task's own "~20%+ of float?" framing:
verified, at 22.5%, materially above the 20% threshold and — as §B5 documents — never approached again
across the subsequent decade. Consistent with §B3's own flow-led-not-flow-anticipating pattern, the
March 2015 ownership peak arrived on the back of the 2014 election-year inflow wave and the market's
own post-election re-rating (Nifty and Sensex both posting strong 2014 calendar-year gains ahead of the
ownership percentile's own peak print) — the peak is a lagging confirmation of a returns event that had
already happened, not a leading indicator of one still to come.

**The 2018 outflow year.** **FIIs recorded a net outflow of ₹95,071 crore in calendar year 2018 — the
largest calendar-year outflow in the record to that point**, and the fiscal-year framing (2018–19)
shows a comparable **₹44,500 crore net outflow**. **[Verified, both.]** Within the year, **October
2018 alone saw a record ₹38,906 crore single-month outflow**, with **September 2018 adding a further
₹21,035 crore** — the acute window overlapping precisely with the IL&FS funding-freeze episode
`shadow-deep/partB-cases.md` §B2's own subject, and with the global dollar-squeeze/EM-FX-rout episode
`globalcycle-deep/partB-cases.md` §B6's own subject; neither is re-derived here. **What returns did
before this outflow**: Nifty had already begun its own decline from its August 2018 peak (~11,760)
before the October outflow figure crystallized, the rupee's own >11% year-to-date fall by end-August
preceding the single largest monthly outflow print by roughly six weeks — a pattern consistent with,
though not as cleanly dated as, the record's other returns-lead-flows episodes. **The DII counterweight's
first clean appearance in this record.** Mutual-fund equity inflows crossed the **₹1 lakh crore mark
for calendar 2018** for the first time `[Verified — a Business Standard headline confirms the ₹1
trillion CY18 milestone; exact terminal figure for the full year not independently re-pinned this
pass]`, the direct institutional legacy of the **SIP culture's structural expansion following
November 2016 demonetization** — a shift already documented in this ladder's own Atlas 4.10 (SIP
debit clustering, ₹20,000+ crore/month by the mid-2020s) and Atlas 3.6 (the retail-participation
wave). 2018 is the first year in this Part's own record where a domestic flow counterweight of
genuine, non-trivial scale existed *simultaneously* with a record FII/FPI outflow — a structural
precondition, not yet the full absorption event, for what §B5 documents fully in FY22.

**Ownership arc, 2014–2019.** From the March 2015 peak (22.5%), the ownership percentile began a
multi-year decline that, per the sequence §B5 documents in full, never reverses for the remainder of
this record. **What L14's state would have read**: a HIGH-but-already-declining percentile through the
2018 outflow year — the episode arrives off the peak, not at a fresh extreme, a genuinely different
positioning-state signature from 2008's (which arrived near the era's own then-record high) and a
useful reminder that `L14`'s own reduce-only design is meant to flag *elevated* readings generally, not
only readings at a series' single all-time maximum.

---

## B5. 2020–2026 — the round trips and the structural shift

**March 2020 — the fastest exodus on record, in flow terms.** The full GLOBAL trigger (the WHO's
11 March 2020 pandemic declaration, the VIX's 82.69 all-time intraday high, the swap-line exclusion
repeating 2008's structural finding) is `globalcycle-deep/partB-cases.md` §B7's own subject,
cross-referenced not re-derived. This Part's own flow record: **FPIs net withdrew a record ₹1.1 lakh
crore in March 2020 alone (₹61,973 crore from equities, ₹56,211 crore from debt) — roughly US$16.5
billion net sold in a single month, the single largest monthly outflow in this entire 1993–2026
record.** **[Verified, all figures, cross-checked against `globalcycle-deep`'s own independent
citation of the same numbers.]** The equity/debt split here — roughly even between the two pools —
is itself a useful contrast with 2013's debt-dominant composition (§B3 above): a genuine
liquidity/margin-call-driven global stop sells everything indiscriminately, in both pools at once,
where a rates-differential-driven episode like 2013 can concentrate almost entirely in one.

**FY21 — the record inflow reversal, precisely dated for the first time in this record.** **FPI net
equity inflows for FY2020–21 (April 2020–March 2021) totaled ₹2.74 lakh crore (≈US$37.39 billion) —
the largest financial-year *equity* inflow in the record**, exceeding 2009–10's US$29.048 billion on a
like-for-like equity basis, though sitting below FY2014–15's US$40.923 billion **all-instrument** total
— a comparison this Part flags rather than resolves as a clean ranking, since an equity-only breakout
for FY2014–15 specifically was not independently pinned this pass `[VERIFY: FY2014–15's equity-only
share of its US$40.9bn total]`. Overall net FPI inflow across all segments for FY21 was **₹2.6 lakh crore
(≈US$35.41 billion)**, netting a **₹24,070 crore (≈US$3.28 billion) debt outflow** against the record
equity inflow and a **₹10,238 crore (≈US$1.39 billion) hybrid-instrument inflow**. **[Verified, the
full breakdown — resolving the `[VERIFY]` `globalcycle-deep/partB-cases.md` §B7 itself flags for "a
precise FY21 aggregate FPI-equity-inflow figure," which that chapter located only directional
confirmation of "record" inflows for, not the primary total this Part's own search independently
pinned.]** Once again, the wave followed rather than led the market's own return path: Nifty had
already regained its pre-COVID high by January 2021, and the FY21 inflow total is a full-fiscal-year
figure necessarily encompassing a recovery that was substantially already in train.

**FY22 — the record exodus, and THE structural exhibit named in the task.** **FPIs were net sellers of
₹1.4 lakh crore (≈US$18–19 billion) in Indian equities in FY2021–22 — more than double the sum of all
prior outflow years combined, the largest FY outflow in the record.** **[Verified, independently, and
consistent with the task's own "~₹1.4 lakh crore" framing — the same order of magnitude
`globalcycle-deep/partB-cases.md` §B8 verifies on a *calendar*-year basis for CY2022 specifically
(~₹1.14–1.21 lakh crore), the fiscal-vs-calendar-year framing difference that chapter itself flags as
plausibly explaining most of the gap between the two windows.]** **What absorbed it — the exhibit
itself**: **mutual-fund equity inflows exceeded ₹1.7 lakh crore over the same window**, more than
fully offsetting the FPI outflow in rupee terms. **[Verified.]** **FPI ownership fell from 23.25% of
NSE-listed companies (March 2021) to 21.01% (March 2022)** — a real, measurable positioning retreat —
**while Nifty closed calendar 2022 only modestly positive to flat**, not the double-digit crash a
comparable outflow scale would have produced against the 2008 or even the 2013 unwind arithmetic.
**[Verified, the ownership figures; the Nifty 2022 outcome cross-referenced to `globalcycle-deep` §B8,
not re-derived.]** **This is the unwind-arithmetic change the task names**: in 2008, a
roughly-comparable-scale outflow (in real, inflation-adjusted terms, the two episodes are of a similar
order) met essentially no absorbing counterweight and transmitted close to one-for-one into both INR
and equity; in FY22, a nominally larger outflow met a domestic mutual-fund/SIP base large enough to
absorb it *more than fully* in rupee terms, leaving the index roughly flat rather than crashed. The
mechanism is structural, not a one-off coincidence of timing: `docs/CYCLE_ATLAS.md` Atlas 4.10's own
SIP-flow figure (₹20,000+ crore/month by the mid-2020s) and Atlas 3.6's retail-participation wave both
describe the same standing domestic bid that §B4 above first observed appearing, at smaller scale, in
2018.

**2023–24 — the return, with a different INR signature.** **FPIs poured ₹1.71 lakh crore into Indian
equities across calendar 2023** — a sharp reversal from 2022's outflow. **[Verified, cross-checked
against `globalcycle-deep` §B8's own independent citation of the identical figure.]** The rupee,
notably, **stayed comparatively range-bound (₹82–83) through this flow reversal rather than sharply
re-appreciating** — a genuinely different post-episode currency signature from 2009's or 2020's own
V-shaped INR recoveries, itself circumstantial evidence that the currency's marginal price-setter is no
longer as exclusively foreign-flow-driven as it was in the record's earlier eras.

**2025–26 — the tariff-era outflows, the ownership crossover, and the live positioning-extreme test
case.** The GLOBAL and bilateral-tariff/Strait-of-Hormuz trigger anatomy for the May-2026 episode is
`globalcycle-deep/partB-cases.md` §B9's own subject in full, cross-referenced not re-derived; this
Part's own flow-and-ownership record for the surrounding window: **cumulative CY2026 FPI equity
outflows had reached ₹2.23–2.25 lakh crore as of late August/early September 2026 — already exceeding
the entire ₹1.66 lakh crore withdrawn across all of CY2025**, itself already a substantial outflow
year. **[Verified, both cumulative figures, cross-checked against `globalcycle-deep` §B9's own
independent citation of the CY2026/CY2025 pair — the small ₹2.23-lakh-crore-vs-₹2.25-lakh-crore gap between
this Part's own separately-sourced figure and that chapter's is treated as reporting-date variance
within the same month, not a contradiction requiring reconciliation.]** Within CY2026, **May 2026 alone
recorded a ₹32,963 crore outflow** (cross-ref `globalcycle-deep` §B9), consistent with the currency
episode that window also carries. **A reversal began mid-year**: **FPIs turned net buyers for two
consecutive months — ₹20,200 crore in July 2026 and ₹27,186 crore in August 2026, the latter the
highest single-month inflow since September 2024** — described in contemporaneous reporting as "the
first indication of a possible trend reversal" after what the same reporting calls the worst
six-month stretch in years. **[Verified, both monthly figures and the framing.]** Per this record's
own standing discipline (echoed identically in `globalcycle-deep` §B9's and `mpcycle-deep` case 8's
own refusals to forecast their respective live episodes' endpoints), this Part declines to say whether
July–August 2026 marks a durable turn or a two-month pause inside a still-deepening outflow year — the
honest position, not a forecast dressed as one.

**The ownership crossover — a structural milestone, not merely an absorption episode.** Against this
outflow backdrop, FPI ownership share fell to successive multi-year lows through 2024–2025: **17.23%
in the December 2024 quarter (a 12-year low at the time)**, **17.22% in the March 2025 quarter**,
**17.04% in the June 2025 quarter**, and **16.71% in the September 2025 quarter (a 13-year low)**.
**[Verified, the full declining sequence.]** Simultaneously, **DII ownership rose to successive record
highs**: **17.8% by the August 2025 reporting round, 18.26% in the September 2025 quarter (the highest
on record), and 19.0% in the December 2025 quarter** — with **DIIs overtaking FPIs in NSE-listed-company
ownership for the first time since 2009 in the March 2025 quarter (DII 17.62% vs. FPI 17.22%)**, a
lead DIIs then **extended for five consecutive quarters through December 2025**, with DII holding
value (₹71.76 lakh crore as of March 2025) running roughly 2% above FPI holding value by the same
date. **[Verified, the full sequence.]** This is no longer only an *absorption* story (a large enough
domestic bid meeting a given year's foreign outflow, as in FY22) — it is a **standing ownership-share
crossover**, the domestic institutional base now the *larger* of the two blocs in aggregate, for the
first time in sixteen years.

**The honest question the task poses, argued rather than merely stated.** Does a LOW positioning
extreme (17%, then sub-17%, the record's own lowest readings) carry information symmetrical to a HIGH
one (22.5% in March 2015), or is `L14`'s reduce-only design — `config/ladder.yaml`: `reduce_only: true`
— correctly asymmetric, a risk-off-only seat by construction rather than by convenience? **The argument
for asymmetry, not merely the assertion of it.** A HIGH-ownership-percentile reading rests on a real,
forward-looking, near-mechanical capacity constraint: if a large share of a name's (or the market's)
float sits with foreign holders and sentiment turns, the *identical* quantum of shares must find a
buyer inside a domestic-liquidity window that has not grown to match it — a crowding risk that is
observable *ex ante*, from the ownership stock alone, without needing to know *why* sentiment will
turn or *when*. This is precisely the capacity-mechanism survival argument `docs/CYCLE_ATLAS.md` row
2.13 states for why the positioning-extreme signal survives being known even as the flow-momentum
variant does not (`research/CONTRACT.md` §5's own required survival test, answer (ii): "a capacity
limit that keeps large capital out" — here, a capacity limit on how fast large capital can be
*absorbed on the way out*). **A LOW-ownership-percentile reading has no comparably mechanical mirror.**
An under-owned name or market does not face a symmetric "capacity constraint on the way in" — there is,
definitionally, ample float capacity available to absorb *new* foreign buying precisely because so
little of it is currently foreign-held; the binding constraint on whether that buying actually arrives
is not a capacity limit at all, but **investor decision-making that this record's own flows-follow-
returns finding places downstream of a returns event, not upstream of one**. Treating a low-ownership
percentile as a "risk-on, add exposure" trigger would therefore not be reading a capacity constraint at
all — it would be reading a bet that foreign flows are about to reverse and arrive, which is precisely
the excluded, decaying, DII-absorbed flow-momentum construct `docs/CYCLE_ATLAS.md` §7 already rejects
(`excluded: fii_flow_momentum, reason: "published, decaying, DII absorption (D08)"`), re-admitted
through the ownership-level back door rather than the flow-level front door it was actually excluded
through. **A second, independent argument, specific to this era's own finding.** Even setting the
capacity-symmetry argument aside, this record's own §B4–§B5 evidence is that the DII/SIP base has grown
large enough to be a standing, continuous marginal buyer regardless of the FPI-ownership level — the
2018 first appearance, the FY22 full absorption, and the 2025 ownership crossover all point the same
direction: **the domestic bid today is less conditional on a low FPI-ownership "headroom" existing than
it was in any earlier era**, meaning a low-FPI-ownership reading is, if anything, *less* informative
about future foreign-flow-driven upside now than a naive reading of the raw percentile alone would
suggest, precisely because domestic flow has structurally reduced how much of the market's marginal
price-setting still depends on foreign capital arriving at all. **The design conclusion, stated plainly**:
`L14`'s reduce-only asymmetry is not a modeling shortcut — it reflects a genuine, argued difference in
mechanism between the two tails of the same percentile, and the record's own 2020–2026 era, arriving at
its lowest-ever readings just as this question is asked, is the correct live test of exactly that
asymmetry rather than evidence the seat is under-using information it should be reading both ways.

---

## B6. Synthesis

### (a) The era table

| Era | Cumulative flows (verified) | Ownership arc | Returns-led-flows evidence | Unwind episodes | L14 read |
|---|---|---|---|---|---|
| **1993–2002 arrival** | 1993: ₹2,595cr; cumulative crosses $10bn (8 Dec 1999), $11.23bn (Mar 2000); 1996–97 peak $2,431.9mn; FY98–99 full-year outflow ₹1,584.5cr (the record's only complete-FY reversal this era) | Building from ~0%; no usable percentile this early | 1996 record year followed the post-1991-reform rally already in train; 1999–2000 ₹10,122cr rebound followed the 1999 IT/reform rally, not preceded it | FY98–99 (₹1,584.5cr, full-year); Nov97–Jan98 (−$372.6mn, 3mo); **2000–01/2001–02: flows stayed net POSITIVE through the Ketan Parekh/dot-com 38% crash on the windows this pass could verify** `[VERIFY: full-year totals]` | No percentile exists — the seat has nothing to read (mirrors L9's 1994 finding) |
| **2003–2008 great wave** | 2004–2007: $46.4bn; FY03–08 total order-of-magnitude larger `[VERIFY exact]`; 2008 exodus $13bn (CY) / $15.4bn (Jan08–Mar09) | Climbing fast from arrival-era base toward the record's eventual 2015 peak | Sensex re-rating (10,000 by Feb 2006) preceded the wave's own record years; PN share ~50% of FII AUM by 2007 is return-chasing capital arriving after the rally, not before it | Oct 2007 P-note crash (9% intraday, 1-hr halt, ~80% same-day recovery) — pure regulatory-shock, zero fundamental change; 2008 GFC exodus, returns collapsing in lockstep (Nifty ~60–65%, `[VERIFY exact]`) | Rising→extreme-high percentile into 2007–08; correct regime direction, no timing power (states not dates) |
| **2009–2014 QE return** | 2009–10 $29.048bn; 2010–11 $29.422bn ($60.31bn cumulative Mar09–Nov10); FY13–14 only $5.009bn (equity); FY14–15 $40.923bn | Rebuilding past pre-2008 levels; 2013 debt-pool stress leaves equity percentile comparatively undisturbed | 2009–10 wave followed the Mar-2009 recovery already underway; 2014 wave is a full-FY total necessarily including the post-election rally it's dated against | 2013 taper — **debt-side, not equity-side** (MSF 300bp, FCNR(B) $26–34bn, cross-ref mpcycle case 4/shadow §B5); equity FII stayed net positive the full FY | Would under-read 2013 specifically — the stress landed in a pool L14's equity-ownership construction doesn't watch |
| **2014–2019 plateau/FPI regime** | FPI regime from 1 Jun 2014; CY2018 outflow ₹95,071cr (then-record); FY18–19 ₹44,500cr | **Peak: 22.5% free-float, March 2015** (₹19.4 lakh cr; FII:DII ratio 1.99, both record highs); declining thereafter, never regained | 2018 outflow followed Nifty's own Aug-2018 peak and INR's own >11% YTD fall by ~6wk | CY2018 (₹95,071cr; Oct alone ₹38,906cr record month) — overlaps IL&FS + global dollar squeeze (cross-ref shadow §B2, globalcycle §B6); **first year DII (>₹1 lakh cr MF inflow, post-2016 SIP culture) absorbs alongside, not yet fully offsetting** | HIGH-but-already-declining percentile — episode arrives off the peak, not at a fresh extreme |
| **2020–2026 round trips/structural shift** | Mar 2020 −₹1.1 lakh cr (record month, $16.5bn); FY21 +₹2.74 lakh cr equity (record FY); FY22 −₹1.4 lakh cr (record FY, absorbed by >₹1.7 lakh cr MF inflow); CY2023 +₹1.71 lakh cr; CY2025 −₹1.66 lakh cr; CY2026 YTD −₹2.23–2.25 lakh cr (already > all CY2025), reversing to +₹20,200cr (Jul) / +₹27,186cr (Aug) | 23.25%→21.01% (FY22 alone); grinding to 17.23%→17.22%→17.04%→16.71% (Dec24–Sep25 quarters, successive multi-yr lows); **DII overtakes FPI ownership Mar-2025 quarter (first time since 2009)**, DII reaches 19.0% by Dec 2025 | FY21 record inflow followed the Jan-2021 all-time-high recovery, not preceded it | Mar-2020 fastest-ever monthly exodus (even equity/debt split, unlike 2013); **FY22 THE structural exhibit — comparable-scale outflow to 2008, Nifty flat not crashed, because DII/SIP base now absorbs more than fully** | Grinding to record-low readings — **reduce-only design means the seat is silent here, not bullish; the low-extreme question is argued in §B5, not merely flagged** |

### (b) The flows-follow-returns scorecard, qualitative

Read across all five eras, one pattern holds without a clean counterexample this Part's own search
surfaced: **every major inflow wave in the record (1996, 1999–2000, 2003–2008, 2009–10, 2014,
FY21, 2023) arrived after, not before, a return event was already visibly in train** — a post-reform
rally, a post-crash V, a post-election re-rating, a post-COVID recovery. **Every major outflow wave
(1998–99, 2008, FY22, CY2025–26) arrived in step with, not ahead of, a return reversal**, with the
single, honestly-flagged exception of 2000–01/2001–02, where the verified flow windows show continued
net positive registered FII inflows through a ~38% domestic crash — a genuine anomaly in the record
(pending the fuller-data check §B1 names) rather than a confirming case, and worth carrying into the
data phase's own FL1 trial as a specific, falsifiable sub-hypothesis (does a domestically-generated
crash — manipulation unwind, not a global or flow-driven shock — show a different flow signature than
a globally-transmitted one?) rather than smoothed over here. The desk's own pre-registered, data-gated
FL1 trial is where this scorecard gets quantified (lead-lag correlation, Granger-style ordering, purged
out-of-sample); this Part's own contribution is the qualitative record that trial will be tested
against, era by era, not a substitute for running it.

### (c) The DII-counterweight honest read

**The counterweight's own growth, quantified once rather than asserted.** Monthly SIP contributions
rose from **₹3,122 crore in April 2016 to ₹31,961 crore by July 2026** — roughly a **tenfold** increase
across the decade this record's §B4–§B5 eras span — with **FY2024–25 alone recording ₹2,89,352 crore
in total SIP collections, a 45% year-on-year jump**, and SIP-linked assets under management growing
from **₹9.96 lakh crore (December 2023) to ₹13.63 lakh crore (December 2024), a 36.9% rise in a single
year**. **[Verified, all figures.]** This is the mechanical substrate behind every DII-absorption
episode this Part documents — the 2018 first appearance (§B4), the FY22 full offset (§B5), and the
2025 ownership crossover (§B5) are not three independent discoveries of the same fact; they are three
successive readings of one continuously compounding domestic flow, each one larger, in absolute rupee
terms, than the one before it because the underlying SIP/retail base itself kept compounding across
the whole decade. **What it changes for the capacity mechanism.** The FY22 exhibit (§B5) and the 2025 ownership
crossover (§B5) together show a structural change in the unwind arithmetic itself: a given-scale FPI
outflow now meets a domestic (mutual-fund/SIP-led, retail-participation-wave-fed — Atlas 3.6, 4.10)
buying capacity large enough to absorb it more than fully in rupee terms, and — as of the 2025 ownership
data — a domestic ownership base that is now the *larger* of the two blocs on a standing basis, not
only during acute outflow episodes. This is a genuine change to the mechanism `L14`'s own
capacity-constraint argument rests on: the "real capital and time" required to absorb an unwind of a
given ownership-percentile extreme is larger, all else equal, in 2026 than it was in 2008, because the
counterparty capable of absorbing it has grown. **What it does not change.** It does not make a HIGH
foreign-ownership percentile a *safe* reading — 2018 and FY22 both still produced measurable index and
FX stress even with a growing domestic counterweight in place, and the counterweight's own size is
itself a state variable (SIP flows can decelerate; mutual-fund redemptions are not structurally
impossible) rather than a permanent, uncapped absorption capacity. Nor does it license reading a LOW
foreign-ownership percentile as a buy signal, for the two independent reasons argued in full in §B5:
the capacity-constraint mechanism that justifies a HIGH-side reduce-only signal has no mechanical mirror
on the low side, and a larger, more continuous domestic bid makes foreign-ownership *level* less, not
more, informative about future foreign-driven upside specifically. The honest summary: DII growth has
changed how much damage a given FPI outflow can do; it has not changed, and structurally cannot change,
`L14`'s own design mandate as a risk-off-only seat reading a genuinely one-sided mechanism.

---

## References

Griffin, Nardari & Stulz — the cross-country returns-lead-flows finding already cited, not
re-derived, in `config/ladder.yaml`'s `L14_fii_positioning` entry and `docs/CYCLE_ATLAS.md` row 2.13.
· Chakrabarti, R. — India-specific FII-flows-follow-returns finding, also already standing in the
ladder/atlas citation `[VERIFY: exact venue/year — see B0]`. · SEBI Annual Reports (1996–97 through
1999–2000 vintages) and Economic Survey tables citing SEBI — the arrival-era (§B1) monthly/annual FII
figures, accessed via secondary aggregation this session (`www.sebi.gov.in` itself EGRESS_BLOCKED this
pass, confirmed directly). · Business Standard, Business Today, and other contemporaneous financial-
press reporting for every dated flow, ownership, and P-note figure throughout, per the `[VERIFY]`
discipline stated at each figure's first use. · `research/cycles/globalcycle-deep/partB-cases.md`
(the GLOBAL-episode anatomy for 2008 §B3, 2013 §B4, 2020 §B7, 2022 §B8, and the May-2026 episode §B9 —
cross-referenced throughout, never re-derived). · `research/cycles/mpcycle-deep/partB-cases.md` case 4
(the 2013 MSF/FCNR(B) domestic defense) and `research/cycles/shadow-deep/partB-cases.md` §B5 (the 2013
NBFC-side negative control) — both cross-referenced, not re-derived. · `research/cycles/fincycle-deep/
partB-cases.md` (house style for this series: numbers-forward, sourced, `[VERIFY]`-disciplined). ·
`docs/CYCLE_ATLAS.md` row 2.13 and §7 (the rejected flow-momentum finding). · `config/ladder.yaml`
(`L14_fii_positioning` entry, and the `excluded: fii_flow_momentum` entry). · `research/CONTRACT.md`
§4 (evidence tiers; Tier-C reduce-only rule) and §5 (the signal-survival test).

---

*Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in) · 2026-09-02 ·
v1.0*
