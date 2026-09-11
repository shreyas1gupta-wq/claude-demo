## THE INDIA SOURCE ESTATE AND THE INDIA LITERATURE

**The six dossiers behind this section ran with the shared WebSearch budget exhausted (200/200) and
`WebFetch` egress-blocked, so all six self-declare `[RECALL — unverified]` throughout — and the
audit (`_AUDIT-3`) then refuted twenty-one of their load-bearing claims, almost none for bad
tagging and almost all because five of its eight files never opened a desk document.** The desk's
`research/cycles/fincycle-deep/partC-data.md` already covers RBI HPI provenance, RESIDEX's two
dated breaks, the registration-count channel and the supply side at desk grade; it answered those
questions differently and it wins. This section is written desk files first, dossiers second — the
reverse of how the dossiers were written.

One tag is added here and defined only here: **`[DESK FILE]`** means a fact recorded in an on-desk
document of record (`partC-data.md`, `india-dossiers/*`, `trial-ledger.md`, `_PROBE.md`) written
when search access existed. Per `_HEAD.md` §00 it outranks every snippet claim in this pack. It is
not an upgrade of an external tag but a separate, higher class. Everything else keeps the tag its
source gave it; nothing is promoted. Bare `R`/`D`/`C` codes below are `_AUDIT-3` row references.

---

### 1. THE OFFICIAL INDEX ESTATE

**RBI's House Price Index is the only official Indian series built from registered transaction
prices and is the correct anchor — but the vintage every dossier here describes was superseded on
10 October 2025.** `partC-data.md` §C.1: RBI published the HPI for **Q1:2025-26 on 2025-10-10** on a
**new base (2022-23 = 100)** with coverage **expanded from ten cities to eighteen** (the ten plus
Hyderabad, Thiruvananthapuram, Pune, Ghaziabad, Thane, Gautam Buddha Nagar, Chandigarh, Nagpur),
back-series from Q1:2022-23 — so the new base's native history *starts* in 2022-23 `[DESK FILE]`,
corroborated `[1-SOURCE]` (A2 §64). **C1 and C5 both call the 10-city / 2010-11 vintage current, and
C1 tells the engine to anchor on it** (R1, R20). An engine built on that trains a city panel through
a documented level break with eight cities silently appearing mid-sample. The repair is
pre-registered: 10-city / 2010-11 as the long history 2010-2025, 18-city / 2022-23 as the tail from
Q1:2025-26, spliced `k = HPI_new(t0)/HPI_old(t0)` `[DESK FILE]`.

| Series | Price concept | Geography | Cadence / lag | Revisions | Access |
|---|---|---|---|---|---|
| **RBI HPI** | **Registered sale-deed prices** from state Registration/Stamps Departments; chain-linked, three floor-space classes (**carpet bands ≤60 / 60-110 / >110 sqm**), averaged per class per **ward**, weights fixed at the Apr-2010–Mar-2011 mix `[DESK FILE]`+`[1-SOURCE]` | **City** (10 legacy, 18 current) + all-India on **fixed 2011 Census population weights**; ward strata exist upstream, unpublished | Quarterly; Q1:2026-27 released **2026-08-24**, ~8wk; earlier 10-12. Range **8-13wk** `[DESK FILE]` | **No RBI policy found on the desk's own pass** `[DESK FILE, VERIFY]`; registration-lag backfill is a structural risk, not a fact | DBIE + Bulletin; no known API `[RECALL]` |
| **RESIDEX @ Assessment** | **Bank/HFC valuation at loan sanction** — a lender's collateral number `[DESK FILE]` | 50 cities (18 capitals + 37 smart cities, overlapping) | Quarterly; Mar-2024 quarter released **2024-06-11**, ~10wk | **Two base breaks**: Jul-2017 relaunch at **FY2012-13=100**, rebased from the **Apr-Jun 2018 quarter to FY2017-18=100** `[DESK FILE]` | Web tool, per-query export `[RECALL]` |
| **RESIDEX @ Market** | Primary and secondary **listing/deal** data `[DESK FILE]` | **Same 50-city panel** — C1's "~18 cities" is the capital-city component of the 50, misread as a ceiling (R4) | Same | Same | Same |
| **MoSPI CPI Housing** | **Rent**; urban-only pre-reform. Weight **21.67% urban / 10.07% combined** `[1-SOURCE]`, matching C1 (C-04) | State/UT, all-India — **not city** | Monthly, provisional then revised | **The rent input is not monthly**: **bi-annual, urban-only** until the 2025-26 reform to monthly rural-and-urban on HCES 2023-24 `[1-SOURCE]`. Pre-2025 prints are largely interpolation; the reform is itself a break (R21) | Release + probable data.gov.in mirror `[RECALL]` |
| **CPI-IW House Rent** | **Rent**, industrial centres; base 2016=100 (prior 2001=100) | ~78 centres on the 2001 base, ~88 on 2016 `[RECALL]` | Monthly | Rents collected by **periodic surveys, interpolated between rounds** — most monthly prints carry no new information `[RECALL]` (C-05) | PDF note `[RECALL]` |
| **RBI RAPMS** | Sanction-time valuation, financed segment only `[RECALL]` | City groupings in FSR boxes `[RECALL]` | Unknown | Unknown | **May not exist as a public series** |

**Four negatives, which matter more here than the positives.** (i) **RAPMS may not be citable** — no
file here and no desk document establishes any public output beyond aggregated LTV charts in the
Financial Stability Report `[RECALL]`. Design nothing around it. (ii) **The "1-4 quarters
provisional" window does not exist**: C1 invented it and built an operational rule on it (D-01);
the desk found no documented policy and prescribes **differencing successive vintages of the same
reference quarter**. (iii) **Ward granularity is a publication ceiling, not a structural one** (R7)
— the index is *constructed* per ward per quarter before aggregation `[DESK FILE]`, making an RTI or
data-sharing request for the existing strata the highest-value acquisition route on this page.
(iv) **RESIDEX is active, not superseded** (R5): quarterly releases continue through at least Q1
2026 `[DESK FILE]`. One correction runs the other way — **RBI HPI does have a carpet-area size
stratification**, which C5 denied (R6).

**Closest to a transaction-price index: RBI HPI, because its input is a registered sale deed.**
RESIDEX's assessment leg is a lender's sanction valuation, its market leg draws on listings, CPI and
CPI-IW measure rent, RAPMS (if public) is a sanction valuation over financed purchases only.
**Binding rule: neither RESIDEX version may be blended with RBI HPI** — three different questions,
and a persistent gap is a divergence to log, not an error to average away `[DESK FILE]`.

**Registered is not transacted, and the bias has a direction.** A sale below the state's minimum
registerable value is deemed to occur at that floor for stamp-duty and capital-gains purposes,
backstopped by Section 56(2)(x) (any gap above ₹50,000 taxed as buyer income). Where cash rides on
top, **registered prices run below true prices and the gap widens when informal-premium behaviour
is most active — late-cycle. Every registration-based gauge understates cycle amplitude, worst at
peaks** `[DESK FILE]`. Primary/developer circle-rate gaps narrowed from >100% in 2015 to as low as
~6% while **resale is where under-reporting concentrates** `[1-SOURCE]` — never pool the two.

**The non-price estate, and its staleness.** Census H-series is the finest official geography that
exists (village/ward, exhaustive) but is **2011 vintage, the 2021 round postponed and its status
unconfirmed** `[RECALL]` — ~15 years stale, and nothing else reaches that grain. NSS 76th Round
(2018) is a one-off condition survey with unconfirmed microdata access terms `[RECALL]`. **PMAY-U's
MIS is a live administrative database, not a release** — snapshot and hash per pull date `[RECALL]`.
NHB's annual *Trend and Progress of Housing* is the under-exploited HFC credit leg but gives
**outstanding stock, not gross disbursal**, with a lineage break at **2019-08-09** (HFC supervision
NHB→RBI). RBI Sectoral Deployment's Housing and Commercial Real Estate sub-lines are the fast,
long-history credit legs both price series lack — monthly, 40 select banks (~93% of SCB non-food
credit), with a **January 2019 format break** `[DESK FILE]` for both.

---

### 2. THE ACQUISITION MAP

**Start with the correction, because it changes the build order: the blanket claim that no state
exposes any bulk registration data is too wide, and the desk already has the free feed for the part
that matters most.** C2 and C6 both wrote the unqualified negative, and C6 then routed "the single
highest-value India probe" through a CAPTCHA scrape (R18). `partC-data.md` §C.5: Maharashtra records
**over 10 lakh registrations annually, Mumbai ~30%**, the IGR portal **exposes a daily/monthly
registration-count and revenue e-search facility**, and **Knight Frank India's monthly Mumbai/Pune
notes are built from the Department of Registrations and Stamps' own published figures, republished
within days of month-end** `[DESK FILE]`. **The negative survives only for transaction-level
microdata — and separately for the rent side, where no aggregate has been confirmed by any pass.**

**The four-tier architecture, common to almost every state** `[RECALL]`:

| Tier | Gate | What it yields |
|---|---|---|
| 0 | Free, no login | Notified-valuation lookup — a zone/ward administrative band by property type. Never a parcel's transaction |
| 1 | Login/OTP + CAPTCHA, nominal fee | Index-II search by village + survey/CTS/khasra number and year: parties, description, **consideration value**, notified value used for duty, duty paid, date |
| 2 | Paid, per document | Certified copies and **Encumbrance Certificates** — 13- or 30-year charge history per parcel, the closest thing India publishes online to a chain of title |
| 3 | — | **Bulk export or API: does not exist for microdata in any major state** |

| State | System | Notified value | Grain | Note |
|---|---|---|---|---|
| **Maharashtra** | IGR (SARITA lineage); eSBTR; **Aadhaar e-KYC leave-and-license e-registration** | **Annual Statement of Rates**, annual | **Zone/sub-zone, cross-walked to CTS numbers in Mumbai** — finest here | Only state with compulsory rent-agreement registration on the sale-deed geography. The free e-search year band is `[RECALL — low]` and is a build-or-no-build parameter (D-12) |
| Karnataka | Kaveri 2.0 + Bhoomi (rural RTC) | Guidance value | Village+survey no.; urban street | EC as a signed PDF — test whether EC text parses cheaper than index scraping |
| Tamil Nadu | TNREGINET | Guideline value | Street/village | EC recalled digitised from ~1987 `[RECALL — low-mod]`; revisions periodic, not annual |
| Gujarat | Garvi | **Jantri** | Village/zone | **Frozen ~2011, revised mid-April 2023, reported roughly doubling statewide, non-uniformly** `[RECALL]`; the auditor's own recall matches all three limbs (C-06). A dated break to register |
| Telangana | IGRS (urban) + **Dharani** (agri, ~Oct 2020), successor announced post-Dec-2023 | Guideline value | Village/ward | **Avoid as first target**: breaks at the 2020 launch and the 2024-25 replacement sit inside the training years |
| Delhi | DORIS | Circle rate, **categories A-H** | **Eight bins per property type** | Resolution-capped at ~8 levels — the coarsest instrument here (C-07) |
| Uttar Pradesh | IGRSUP + UP Bhulekh | Circle rate | District→tehsil→mohalla | District review cycles, no fixed calendar |
| Haryana | — (Jamabandi for records) | **Collector rate** | Numbered Gurugram sectors | "Jamabandi" is Haryana's brand, Punjab's brand and the generic record name — do not conflate |
| Rajasthan / MP / Kerala / W. Bengal | IGRS Rajasthan / Sampada 2.0 / — / e-Nathikaran, Banglarbhumi | **DLC rate** / collector guideline rate / **Fair Value** / — | Zone-colony / — / village+survey no., land in **cents** (1/100 acre) / **mouza** | Kerala's cents and Bengal's mouza are further normalisation steps `[RECALL — low]` |
| Punjab, HP, Jharkhand, Manipur, Puducherry, small UTs | **NGDRS** adopters `[RECALL — low, incomplete]` | — | — | **NGDRS is a shared codebase, not a shared database.** No national portal exposes registered transactions |

**The national layer, and the one fact to verify first.** DILRMP runs record-of-rights
computerisation, registration linkage and modern survey with a progress dashboard; Bhulekh and
Bhu-Naksha are the text and cadastral-map layers, state by state under shared brands but never
federated; SVAMITVA drone-maps previously unsurveyed rural inhabited land. **ULPIN — "Bhu-Aadhaar",
a 14-digit parcel identifier piloted from about 2021 — is the single highest-value item** `[RECALL]`,
because a working parcel key is exactly what a repeat-sales index needs and India otherwise lacks:
survey, khasra, CTS and gat numbers do not compose. Coverage is unknown; no figure asserted.

**The area-basis trap as a formula, not a remembered band.** The pack-wide "20-35%" constant is
arithmetically wrong and twice refuted (`_AUDIT-1` R14; R19): a carpet-to-super-built ratio of
70-80% implies **+25% to +43%**, and Mumbai loading is reported at **40-50%** `[1-SOURCE]`. Carry a
loading factor **L** per series and city, **psf ratio = 1 + L, L up to 0.50 for Mumbai**.

**Verdict — first target Maharashtra, on four grounds stronger than C2's.** (i) The free, cleaned,
monthly registration-count and stamp-revenue channel already exists for Mumbai and Pune `[DESK
FILE]`, so the whole scraping budget goes to the price side. (ii) The ASR publishes annually at
zone/sub-zone grain cross-walked to CTS numbers — exactly the cadence and grain a
sale-price-to-notified-value ratio series needs. (iii) 10 lakh-plus registrations a year reaches a
usable locality-month sample soonest. (iv) It is the only state whose compulsory rent registration
sits on the sale-deed geography, the only Indian route to a **transaction-based** yield. **Next
three: Karnataka** (Kaveri 2.0 and Bhoomi maturity, Bengaluru volume, EC as a cheap per-parcel
history); **Tamil Nadu** (Chennai volume, street-grain guideline value, longest recalled
digitisation); **Gujarat** — not for volume but because the 2011-to-2023 jantri freeze-then-double
is the cleanest dated notified-value shock in India, and therefore a natural experiment on the
circle-rate bunching question. Telangana is deferred despite Hyderabad's size.

---

### 3. THE SUPPLY PIPELINE AND THE PRIVATE ESTATE

**Access degrades as you move upstream, the opposite of the intuition that data improves nearer the
statute.** Building permit → RERA registration → quarterly progress report → OC/CC → registered
sale: RERA registration is the most accessible free rung, permits and OC/CC the least digitised,
registered sales the richest and hardest to obtain in bulk.

**RERA is a launch-and-intent register, not a transaction feed, and there is no national bulk
database.** Every portal is a project-by-project search interface, not a documented API — confirmed
on the desk's own pass for Maharashtra and Karnataka, `[VERIFY]` elsewhere `[DESK FILE]`. Aggregators
(`reradetails.in`, `rerawebsite.in`, `realatic.com`) already scrape several states, which evidences
scrapability, not a free feed. **Budget a state-wise RERA build as a multi-week scraping project**,
Maharashtra first, then Karnataka, Telangana, UP, Gujarat `[DESK FILE]`. The statutory schema
carries registration number, promoter, precise location, land area, tower and unit counts with
**carpet areas** (the Act's defining disclosure reform), the **proposed and any revised completion
date** — each extension its own filing, so delay is directly observable — the 70% escrow account,
and a **quarterly progress report** with percentage completion and units booked `[RECALL]`.
**Whether QPR history is publicly retained or only the latest report shown is unresolved, and the
delay-trajectory feature depends on it.** Separately the record is **status-mutable**: developers
live-update it, so today's snapshot is not the record as of any past date and no upstream vintage
archive exists — snapshot and hash every pull, dated `[DESK FILE]`.

**Permits and completion certificates are the weakest rung.** Mumbai's BPMS and the statewide
AutoDCR lineage (Mumbai, Pune, Nagpur, Thane), BBMP's Bengaluru system and Telangana's **TG-bPASS**
(deemed/self-certified approval below a size threshold) all read as submitter-facing workflow
portals with no recalled public bulk view `[RECALL]`. **OC/CC issuance is the cleanest
pipeline-to-completed-stock event — a certified fact rather than the stated intent of a RERA
revised-completion filing — and the least accessible datapoint in the chain.** Municipal
property-tax portals (MCGM, BBMP SAS, GHMC PTIN) are per-property lookup and payment systems; ward
aggregates circulate only in annual budget books, and assessed value is a formula on locality zone
and declared area, not a market valuation `[RECALL]`.

| Vendor | Underlying data | Bias direction |
|---|---|---|
| Anarock, Knight Frank India, JLL, CBRE, Colliers, Cushman & Wakefield | Each firm's **proprietary tracked-project universe** — a sample of organised launches, not a census | **Coverage bias plus fee-driven optimism.** Fee-earning brokerages; free research skews constructive, and the same city-quarter differs between firms because tracked universes differ |
| Knight Frank / **CREDAI-MCHI** joint Mumbai notes | The state's own published IGR figures | **Closest free thing to volume ground truth** `[DESK FILE]`; CREDAI-MCHI is the developer body — advocacy bias on interpretation, not on the counts |
| **Liases Foras** (Pankaj Kapoor) | Site surveys plus RERA and registration data; subscription research, no brokerage arm | **Bearish** on MMR oversupply. Independent of leasing fees — the adversarial check on the consultancy consensus |
| PropEquity | Project-level primary-sales database sold to lenders, PE funds, developers | Sold to allocators rather than given away for deal flow — a weak argument for less narrative bias, not evidence |
| **Propstack**, **CRE Matrix** | Scraped/licensed **IGR registration microdata** plus analytics | **The only private layer claiming actual transacted consideration.** Their existence evidences what IGR holds: the bottleneck is interface, not data. Commercial — the free-data mandate bites |
| **Magicbricks PropIndex** | Active listings; quarterly free PDF with **locality-level** price and rent for prime micro-markets | **Asking price**, and the asking-to-transacted gap widens in falling markets. One of very few free sub-city India series |
| Housing.com / PropTiger *Real Insight* | Listings plus some advisory-arm transaction visibility | Asking-price base, partially transaction-informed — the "partially" unconfirmed |
| 99acres | Largest listings inventory; research less systematic | Asking price; marketing-oriented cadence |
| NoBroker | Owner-direct, no-brokerage listings | A distinct **sample-selection** bias (cost-conscious owners, salaried tech-hub tenants) atop the asking-price bias |

**The disqualifying property is shared by all of them, and it is not bias — it is the absence of a
vintage layer.** A pull today shows today's snapshot, not what the site showed at any past date, so
a backtest on scraped history silently reintroduces look-ahead bias this desk already prices at
**150-450bps/yr** for fundamentals. **Exploration-only, never the fixture a signal is evaluated
against** `[DESK FILE]`. The demonstration is on desk: H1 2026 unsold inventory across eight major
markets is **~5.26 lakh units** on Knight Frank's count and **~6.16 lakh** on Anarock's, different
city sets and methods `[DESK FILE]` — two respected houses ~17% apart on the headline
supply-overhang number, which is why neither is fixture-grade.

---

### 4. THE EVENT CALENDAR

**Announcement and commissioning are kept in separate columns because this desk's own finding is
that announcement moves the price and completion merely confirms it.** Panvel **+76%** since 2021,
mostly before the first flight at Navi Mumbai; the Jewar belt **+142-158%/5y**, mostly before
flying; the Delhi-Dehradun Expressway **+23% in the nine months before opening**;
Samruddhi-corridor land at ~**3.7x** its 2015 level by 2022-23, two-plus years before the final
stretch opened; completed MMR infrastructure then yields a smaller continuing **8-15%/yr** premium
`[DESK FILE]`. **The corollary belongs at the top: every public, dated feature is already partly in
the price.** C4 attributed this framing to the equity-side TECH-D1 entry state and left the desk's
own dated evidence uncited (R9/R10 severity note).

| # | Event | Announcement | Effective | Why it matters |
|---|---|---|---|---|
| P1 | RERA 2016 `[RECALL]`, all limbs matching the auditor's recall (C-08) | Passed 10 and 15 Mar 2016 | **~59 of 92 enabling sections 1 May 2016; registration, escrow, carpet-area 1 May 2017** | Formal supply becomes observable. **Use each state's own notification date — the gap can exceed a year** |
| P2 | Benami Amendment Act 2016 `[RECALL]` | Passed ~Jul-Aug 2016 | **1 Nov 2016** | Cash-deal risk armed **one week before** demonetisation — a separate dummy, different mechanism |
| P3 | Demonetisation `[RECALL]`, date high confidence, **no magnitude asserted** | **8 Nov 2016** | Same day; exchange window to late Dec 2016 | Liquidity shock to a cash-intensive market |
| P4 | GST introduction `[RECALL]`; 18%×2/3 = 12.0 and 12%×2/3 = 8 check exactly (C-09) | — | **1 Jul 2017** | Under-construction **12% with ITC**, affordable **8% with ITC**; **ready property with an OC is outside GST**, so OC issuance is itself a tax break |
| P5 | GST rate cut `[RECALL]` | Council 33rd/34th meetings, Feb-Mar 2019 | **1 Apr 2019** | **5% and 1%, both without ITC** — a developer net-cost change, not a buyer-price cut; a one-time old/new election gave the same date **heterogeneous project-level effects** |
| P6 | Homebuyers as IBC financial creditors `[RECALL]` | Ordinance ~6 Jun 2018 | Amendment Act ~Aug 2018; Section 7 tightened to 100 allottees or 10% in 2019-20 | Developer default becomes a national insolvency event — the break for stalled-project features |
| P7 | **Maharashtra stamp-duty holiday** `[RECALL]` | — | **2% 1 Sep-31 Dec 2020; 3% 1 Jan-31 Mar 2021; standard from 1 Apr 2021** | The cleanest natural experiment available — **but the April 2021 payback is confounded with the COVID second wave**; control for lockdown severity by month. **No registration count in this pack is usable**: C4's own is `[RECALL — LOW]` and `_AUDIT-1` D-20 found the pack's Mumbai IGR series unreliable (two months each called a "14-year high"; a projection carried at `[2-SOURCE]`) |
| P8 | **Sections 43CA / 50C safe-harbour band** `[RECALL]`; the auditor's recall matches every rung and calls this the best-reasoned item in the eight files (C-10) | FA 2018; FA 2020; **Aatmanirbhar Bharat 3.0 announced 12 Nov 2020**, legislated FA 2021 | **5% from AY 2019-20; 10% from AY 2021-22; 20% for primary residential sales by builders only, ~₹2 crore cap, ~12 Nov 2020-30 Jun 2021** | **The free parameter of the censored-regression design.** A fixed band across a multi-year sample misspecifies the model. Capture both steps — press-conference relief, legislation months later. **Verify first of everything here** |
| P9 | Section 194-IA TDS `[RECALL]`, low confidence on both later dates | FA 2013 | **1 Jun 2013** (1% where consideration ≥ ₹50 lakh); ~1 Apr 2022 the **higher of** consideration or stamp-duty value; ~1 Oct 2024 threshold on **aggregate** consideration | Three dates, each changing how much of the transaction universe leaves a tax trail. Interacts with P8 |
| P10 | Capital-gains overhaul `[RECALL]` | Budget **23 Jul 2024** | Finance (No. 2) Act 2024; grandfathering ~6-7 Aug 2024 | **12.5% without indexation**, resident individuals and HUFs electing the **lower of** 12.5% without or 20% with indexation for property acquired before 23 Jul 2024 — **not for companies or trusts.** Model the option, not a flat rate |
| P11 | Equity comparators `[RECALL]`: LTCG reintroduced (Sec 112A, 1 Feb 2018, FMV step-up 31 Jan 2018); DDT abolished 1 Apr 2020 | — | As dated | Only for the after-tax property-versus-equity hurdle. Already on desk as **BR7-BR9** |

**The breaks registry has no property-tax dimension at all**: `_AUDIT-2` C8 found BR1-BR9 with **no
circle-rate, 43CA, 50C or stamp-duty entry** `[DESK FILE]`. P7, P8 and the Gujarat jantri revision
are three registrable breaks, each owing a pin-the-notification `[VERIFY]` per BR4/BR6 precedent.

| Project | Announcement / approval | Commissioning | Status |
|---|---|---|---|
| Navi Mumbai Int'l Airport | Conceived 1990s; Adani takeover ~2021 | **Commercial ops 25-Dec-2025** (domestic); 24-hour Feb-2026; **international 15-Jul-2026** | **C4's "unresolved" refuted** `[2-SOURCE, DESK FILE]` (R9). The Dec-2024 trial flight is not the event zero |
| Noida Int'l Airport (Jewar) | Foundation **25 Nov 2021** | **Inaugurated 28-Mar-2026; first commercial flight 15-Jun-2026** | Refuted likewise (R10). **Two distinct commissioning events**, finer than C4's own framework carries |
| Samruddhi Mahamarg | Approved ~2015-16 | Ph.1 **11 Dec 2022**; **fully complete 5-Jun-2025** (Vadpe link open mid-2026) | C4's "Mumbai end ~mid-2024" wrong by ~a year (R11) |
| Mumbai Coastal Road | Tendering ~2017-18 | Staged 2024 openings; **Ph.1 fully 24/7 from Aug-2025**; **Ph.2 (Bandra-Dahisar) targeted Dec-2028** | C4 understated Ph.1 by ~14 months and omitted Ph.2 (R12) |
| Atal Setu / MTHL; Metro 2A & 7 | Foundation ~Dec 2016; construction ~2015-16 | **Jan-2024**; **Ph.1 Apr-2022** | Both survive contact with the desk record (C-11) |
| Mumbai Metro Line 3 (Aqua) | Contracts ~2016-17; Aarey dispute 2020-22 | Aarey-BKC **early Oct 2024** — C4 says the 3rd, the auditor recalls inauguration the 5th, service the 7th | **Do not use a day-precise zero** (D-11) |
| Mumbai-Ahmedabad HSR | Foundation **14 Sep 2017** | **No confirmed section open** | The only one of C4's three "unresolved" claims that stands |
| Delhi-Mumbai Expressway; Delhi-Meerut RRTS | Sohna foundation ~Mar 2019; NCRTC mid-2010s | Delhi-Dausa-Lalsot ~Feb 2023, Mumbai end unresolved; Sahibabad-Duhai **20 Oct 2023**, then ~Mar-2024, ~Aug-2024, Delhi side ~Jan-2025 | Section- and corridor-specific, never one date `[RECALL]` |
| Bengaluru Metro Ph.2; Hyderabad Metro and ORR; Pune, Ahmedabad Metro | Sanctions 2019-21; ~2012-14 and staged from ~2008; ~Dec 2016; mid-2010s | Whitefield ~Mar 2023; IT corridor from ~Nov 2017 with Old City ~2023-24, ORR ~Mar 2018; ~6 Mar 2022; ~Mar 2019 then Ph.1 ~30 Sep 2022 | **Corridor gaps of years sit inside one nominal project — a citywide metro dummy is wrong.** Use the stretch relevant to the geography priced |
| **Bengaluru Peripheral Ring Road; Chennai Metro Ph.2** | Repeatedly proposed since the early 2000s, revival ~2022-24; Cabinet approval **year disputed — C4 says ~Aug 2020, the auditor recalls 2024** | **None** | **Right-censored, not missing** — the repeated-announcement pattern is itself informative about how much value front-loads on approval. Chennai's date is unusable as stated (D-10) |
| Bharatmala Pariyojana | Union Cabinet ~24 Oct 2017 (~34,800 km Ph.1) | Not a project | A national capex-regime marker; corridors get their own pairs |

---

### 5. THE LITERATURE: ESTABLISHED VERSUS CONSULTANT ASSERTION

**Established, reached independently three ways: Mumbai's price level is a regulatory outcome, not a
land-scarcity fact.** Bertaud's *Mumbai FSI Conundrum* (2004, updated ~2011) names four compounding
constraints — topography, restrictive land-use legislation, muddled property rights, deficient
infrastructure — and identifies the second, a pure policy choice, as the largest `[1-SOURCE, venue
unconfirmed]`; the mechanism recurs in *Order Without Design* (MIT Press, 2018). Brueckner and
Sridhar (2012), *Regional Science and Urban Economics* 42, find CBD FAR at most 3.5 in Mumbai,
Delhi and Chennai and below 1.5 in Mumbai and Chennai specifically, against 10-plus in other world
CBDs `[1-SOURCE — re-tagged from 2-SOURCE, `_AUDIT-1` R12: two hosting locations for one article is
one source]`. Bertaud and Brueckner on Bangalore height limits put the welfare cost at 3-6% of
household consumption, footprint shrinking 191→159 km² absent the restriction `[1-SOURCE]`.

**India's one causally-identified supply magnitude — single-sourced and unrefereed, said in the same
breath.** Nagpal and Gandhi, *Relaxing Floor Area Ratio: Housing Supply and Affordability in India*
(CEPR/STEG WP), exploiting spatial and time variation in a Mumbai FAR relaxation: **+17% FAR
utilisation → +58% units supplied in treated areas → −24% prices in treated areas**, no average
size change but smaller units where relaxation was greatest `[1-SOURCE — downgraded from 2-SOURCE,
`_AUDIT-1` D-03; −24% is a very large effect to anchor on from one working paper]`. **C5 was asked
for exactly this cluster and never cites it** (D-14) — the clearest instance of the process failure
this section is written around.

**Equal prominence to the negative finding: deregulation on paper did not deliver supply where the
land was legally encumbered.** Dutta, Gandhi and Green, *Is Land-Use Deregulation Enough to Deliver
Housing?*, *Real Estate Economics*, on the ULCRA (1976) repeal — a 500-2,000 sqm cap on
individually held vacant urban land in ~70 cities with "surplus" surrendered below market, repealed
federally in 1999 and adopted state by state to 2008 (Maharashtra only 2007). Diff-in-diff across
200-plus cities: **the repeal did not produce the supply growth theory predicts, because unresolved
property-rights disputes over the frozen surplus parcels triggered fresh litigation that kept
construction frozen** `[1-SOURCE]`. Compounding it, Gandhi, Tandel, Tabarrok and Ravi, *Too Slow for
the Urban March*, *Journal of Urban Economics* (2021), across ~3,000 Mumbai projects: **27.3% of
projects and 42.9% of built-up space under litigation, average construction 8.5 years, litigated
projects ~20% slower, delay raising total cost by 30% or more** `[1-SOURCE]`. **Deregulation splits
into two non-interchangeable categories — raising a floor-space cap on clean-titled plots (worked)
versus releasing legally encumbered land (largely did not) — and Mumbai's effective elasticity is
lower than its nominal FSI implies by an amount close to unmeasurable from FSI data alone.**

**The FSI comparator table everyone quotes is unverified trade press and must not carry a city
ranking.** Manhattan ≈15, Hong Kong ≤12, Tokyo ≈20, Singapore ≈25; Mumbai island 1.33 (suburbs
0.5-1.0, MHADA to 2.5), Delhi 1.2-3.5, Bengaluru 1.5-2.75 residential, Chennai 1.5-2.0, Hyderabad
uncapped with built projects at 6-7 — industry blogs that **blend base, premium and TDR-loaded FSI
inconsistently** `[RECALL — downgraded from 1-SOURCE, `_AUDIT-1` D-23]`. The implied
Hyderabad-to-Mumbai amplitude ranking is a **hypothesis to pre-register, not a finding**. Record the
FSI concept alongside every number, exactly as with area basis.

**Rent control is the second structural mechanism, with a measured consequence.** The Bombay Rents,
Hotel and Lodging House Rates Control Act, 1947 froze rents on a large pre-1940s tenancy stock
indefinitely, removing maintenance and redevelopment incentive and producing Mumbai's cessed
buildings; the informal **pagdi** market — a lump sum for the tenancy right itself, nominal rent
frozen — is the unrecorded response, so recorded rent for that stock does not measure scarcity. The
Maharashtra Rent Control Act, 1999 replaced the 1947 Act but grandfathered existing controlled
tenancies `[RECALL]`. The empirical statement is Tandel, Patel, Gandhi, Pethe and Agarwal, *Decline
of Rental Housing in India: The Case of Mumbai*, *Environment and Urbanization* 28(1), 2016
`[2-SOURCE]`. Measured independently beside it: **~11.1 million vacant urban units in 2011, ~12.4%
of urban stock** (from 1.83m in 1971), reaching ~19% in Gujarat and ~16% in Maharashtra
`[2-SOURCE]` — landlords preferring empty units to formal renting under weak enforcement.

**Established: registered and circle-rate values are a systematically low, time-varying proxy for
market value, and two independent routes agree.** Chakravorty, *The Price of Land: Acquisition,
Conflict, Consequence* (OUP, ~2013) argues Indian land value is set by an administered-price gap
rather than an efficient market, kept wide by chronic under-revision and the state's dual interest
as acquirer and taxer, reading Singur, Nandigram, POSCO and Bhatta Parsaul as symptoms rather than
one-offs `[RECALL, moderate-high]`. The legislative admission of the same gap is **RFCTLARR 2013**,
whose compensation is a multiple of registered value (~1x urban to 2x rural plus 100% solatium,
giving the quoted 2x urban / 4x rural) plus R&R entitlements, with consent (~80/70%) and Social
Impact Assessment for private and PPP acquisition `[RECALL]`. **The multiplier is in part an
explicit statutory correction for a known distortion — so registered values near a compensation
event are a lower bound with an unquantified offset.**

**Established: a large share of Indian urban housing never enters the register the official series
are built from.** Slums housed on the order of 65-70 million people, roughly 17% of urban
population, on Census-2011-era definitions `[RECALL, low confidence; definitions vary across
notified/recognised/identified]`; Delhi's unauthorised colonies are a distinct category, on the
order of 1,700 settlements, whose residents were granted conditional ownership and registration
rights by the NCT of Delhi (Recognition of Property Rights of Residents in Unauthorized Colonies)
Act, 2019 — an admission that a very large stock sat outside registration for decades `[RECALL]`.
Partha Mukhopadhyay's CPR work with Marie-Hélène Zerah on **subaltern urbanisation** documents the
settlement-level version: much urban growth occurs in small and medium towns and census towns
without statutory urban-local-body status, while every official price series is metro-concentrated
`[RECALL]`. **A denominator problem, not noise: the engine's universe is the registered formal
market, and that is scope to state, not bias to correct.**

**Consultant assertion, and the most consequential gap in the India literature: there is no
recoverable peer-reviewed Indian hedonic estimate of an infrastructure premium.** The circulating
figures — "15-25% within 500m-1km of a metro corridor" — come from consultancy output with no
published method, no confounding-trend control and no stated area basis `[RECALL]`; C5 rightly
refused to name authors or magnitudes rather than risk fabricating them. **These are exactly the
coefficients an engine wants to import from "the literature", and the literature cannot supply
one.** Estimate them from scratch on acquired transaction data, or run a dedicated refereed search
city by city.

**Thin or unverifiable, listed so it is not mistaken for absence of evidence** — all `[RECALL]`, no
titles asserted: RBI DEPR house-price working papers (Snehal Herwadkar recalled as an author);
NIPFP on property taxation, municipal fiscal health and land value capture (Simanti Bandyopadhyay);
ICRIER on FDI, housing finance and REITs; the RBI Household Finance Committee report (2017, chaired
Tarun Ramadorai) and its finding that Indian household wealth is overwhelmingly physical with a
strikingly low financial-asset share; the HPEC urban-infrastructure report (chaired Isher Judge
Ahluwalia, ~2011; a 20-year need recalled near ₹35-40 lakh crore over 2012-2031, low confidence);
Bimal Patel's Gujarat **Town Planning Schemes** as the land-pooling alternative to eminent domain;
Annapurna Shaw's *Indian Cities* (~2012); Gilles Duranton on Indian city size and market access;
the World Bank's *Leveraging Urbanization in South Asia* (~2015). One naming flag: **do not present
Piyush Tiwari and the IIM Bangalore Real Estate Research Initiative as one item** — the auditor
places Tiwari at the University of Melbourne (D-14).

---

### 6. THE YIELD QUESTION

**Every Indian yield estimate this programme found belongs to one of two families that disagree by
2-3 percentage points and rank cities differently, and which family is right decides whether Indian
metros look priced at a historical top or a historical bottom.** The anchor is the desk's own print:
across the JST 18-country panel, property-boom **peak** rental yields ran a median **3.29% in the
modern era** (3.78% full sample) and **trough** yields **4.94% modern** (5.23% full) `[DESK PRINT,
CN-D2]`, verified verbatim against the ledger (C-14).

| Estimate | Level | As-of | Method | Family | Tag |
|---|---|---|---|---|---|
| India national | **5.16%** (from 5.09%) | Q2 2026 | Global Property Guide: median asking **rent** ÷ median asking **price**, full listing stock | 1 | `[1-SOURCE]` |
| Delhi; Kolkata | 5.81% / 6.19%; 5.79% / 6.32% | 2026 | GPG, plus a second aggregator on the same method, different cut | 1 | `[2-SOURCE on direction; points differ]` |
| Bengaluru | 4.45% (2024) → est. 4.6-5.0%; citywide 3.6%→4.6% 2019→Q2'26 | 2024-26 | Anarock survey; GPG city trend | 1+2 | `[2-SOURCE]` |
| Hyderabad | citywide 2.6%→3.6%; **IT corridor 3.8-4.2%** | 2026 | GPG trend; portal corridor estimate | 1+2 | `[2-SOURCE]` |
| **Mumbai citywide** | **3.84%** | 2026 | **GPG — a Family-1 figure** | **1** | `[2-SOURCE]` |
| **Mumbai premium corridors** | **2.0-4.0%** (SoBo/Malabar Hill 2.0-3.0, Bandra West 2.0-2.5, Powai/Chembur 3.0-3.5, Malad/Goregaon 4-5) | 2025-26 | Portal/broker micro-market surveys | **2** | `[1-SOURCE each]` |
| Pune | citywide 3.0-4.3%; Hinjewadi/Kharadi **4.0-4.4% one cut, 5.5-6% another** | 2024-26 | Portal aggregates | 2 | `[1-2 SOURCE, conflicting — unresolved]` |
| Chennai | 4.05-4.16% (from 3.78% a year earlier) | Q4 2025 | Magicbricks Rental Index | 2 | `[1-SOURCE]` |
| Ahmedabad; Gurugram; Noida; Lucknow (Gomti Nagar) | 3.9% (cited highest of any major city in that survey); 4.1%; 3.7%; ~3% | 2024-26 | Magicbricks/Business Standard; one syndicated broker-survey family; in-programme dossier | 2 | `[2-SOURCE]`; `[1-SOURCE]`; `[1-SOURCE]`; `[2-SOURCE, in-programme]` |
| Kochi (Kakkanad); Indore (Nipania / Super Corridor) | 4.6-6%; up to 8% (Super Corridor ~6%) | 2025-26 | In-programme screen §13 | 2 | `[1-SOURCE, in-programme]` |
| Surat (Sachin / Surat North) | 11-12% — **rejected, not adopted** | 2025-26 | The same portal prints 3-4% for other Surat localities; a 3-4x internal spread read as artefact | 2 | `[1-SOURCE, discarded]` |
| Numbeo | **no figure** | — | **No Numbeo India number survived any search pass**, and none is stated | — | omitted deliberately |
| Comparators | Taiwan ~1.9-2.3%; Singapore ~3.1%; China GPG ~2.6%; Shanghai price-rent 78-79 raw implying ~1.3-2%; prime London 3-4% | various | Same-method or cited | — | `[1-SOURCE]` each; India's GPG figure is **~2.0x China's** like-for-like `[COMPUTED]`. Philippines, Indonesia, Brazil, South Africa and Turkey did not surface and are deliberately absent |

**The verdict sentence has to be rebuilt, because the source version is a family blend — and fixing
it strengthens the warning.** C6's headline filed "Family 2's premium-corridor numbers (Mumbai
3.84%...)" near the peak band, but **3.84% is the GPG Family-1 citywide figure**, correctly filed as
such in C6's own opening paragraph (R13). The honest Family-2 Mumbai range is **2.0-4.0%**, which
does not sit near the modern peak band of 3.29% — it **straddles and undercuts it**. So: **the
micro-markets Indian investors actually transact in are priced at or through the level at which
property booms have historically topped out, while the national asking-price blend of 5.16% sits
above the level at which busts have historically ended.** Both readings come from the same country
in the same quarter, which is why no single "Indian rental yield" may be quoted without its family.

**Why they diverge, and the selection problem under both.** The most defensible unsourced
explanation is composition: GPG's median-of-listings method is diluted toward older, cheaper stock
with a structurally higher rent-to-price ratio, while portal city yields are built from newer,
higher-capital-value stock dominating transaction volume — the same gap the China programme found
between GPG and domestic-press figures. Beneath both: **NSSO found 71% of Indian rentals have no
written contract (2012) and only ~5% used formal agreements (2008-09), about a quarter of those
registered, with some states above 90% informal (AP and Telangana ~94%, Bihar ~92%)** `[2-SOURCE,
two rounds converging]`, and the **11-month lease is a deliberate registration and rent-control
workaround** `[2-SOURCE]`. Observed contract-bearing rents are a small, non-representative slice.

**Gross to net: no source has published an India net yield, so this waterfall is `[COMPUTED]` on
stated assumptions — illustrative, not measured.** Gross 4.0% on a value of 100, rent R = 4.0.

| Line | Units of value | Basis |
|---|---|---|
| Gross yield | **+4.00** | Representative prime-urban Family-2 level |
| Society / maintenance | −0.30 | ~7.5% of rent; **no separate tax deduction beyond the flat 30%** `[2-SOURCE]` |
| Property tax | −0.20 | **The weakest line.** 0.2% is a single Pune capital-value worked example, **not a national average**; the defensible read is **sub-1% of capital value**, so the true span runs to ~0.80 `[1-SOURCE]` |
| Vacancy | −0.30 | 7.5% of rent, practitioner cost-calculator input |
| Repairs / upkeep | −0.75 | **Illustrative, with no source at all — and the largest single deduction, 19% of gross rent** |
| Brokerage | −0.36 worst case | One month's rent at every 11-month renewal = 9.09% of R; ~0.14 amortised over a ~2.5-year tenancy |
| **Cash net, pre-tax** | **2.09** / **2.32** amortised | |
| Income tax | −0.76 | Section 24(a) allows a flat **30%** of Net Annual Value (rent minus municipal tax) **with no separate repairs deduction** `[2-SOURCE]`. Vacancy-adjusted NAV = (3.70 − 0.20) × 0.70 = 2.45; at 31.2%, tax = 0.764 |
| **After-tax, in-pocket** | **1.33** / **1.56** amortised | |

Two audit corrections are applied: C6 **deducted vacancy as a cash loss and then taxed the full
gross rent** (R14), and **31.2% is the no-surcharge rate** — the profile modelled, an unlevered
owner of a prime-urban investment flat, plausibly has income above ₹50 lakh and faces a 10/15/25%
surcharge tier, giving ~34.3-39% effective and an after-tax figure of roughly **1.18 down to 1.05**
`[RECALL, must-verify]` (D-09). C6 also called brokerage the most assumption-sensitive line; it is
third. **Property tax (span to ~0.80) and repairs (0.75, unsourced) are half the total deduction;
brokerage's 0.22 span is 19% of it** (R15). **Bounded verdict: on a 4.0% gross start an unlevered
top-bracket landlord nets roughly 1.0-1.6% of value per year after tax; a lower-bracket owner, one
amortising brokerage over a real tenancy, or one sheltering income through Section 24(b)'s uncapped
interest deduction on let-out property lands nearer the pre-tax cash 2.1-2.3%.** No line in that
range is an empirical measurement.

**Commercial: every listed Indian REIT yields below the 10-year G-sec on the same date, and this is
the best-sourced material in the India yield file.** The 10-year G-sec traded **6.96-7.10% in
September 2026** `[2-SOURCE]`.

| REIT | Type | Distribution yield on price | On NAV | Price vs NAV | Occupancy | WALE |
|---|---|---|---|---|---|---|
| Embassy Office Parks | Office | **5.75%** (FY26 ₹25.28 ÷ ₹439.6, 10-Sep-26) | 5.14% (NAV ₹491.62) | **−10.6%** | 90% (FY27 guided 95-96%) | 8.5y |
| Mindspace Business Parks | Office | **4.83%** (₹24.09 ÷ ~₹499, 2-3 Sep-26) | 4.57% (NAV ₹527.0) | **−5.4%** | 95.3% committed Q3FY26 | 6.9-7.4y |
| Brookfield India | Office | **6.24%** (₹21.40 ÷ ~₹343, 24-25 Aug-26) | 5.53% (NAV ₹386.7) | **−11.2%** | 96% committed FY26; ~93% enlarged Jun-2026 | 6.7y |
| Nexus Select Trust | Retail | **5.42%** (₹9.081 ÷ ₹167.5, 8-Sep-26) | 5.54% (NAV ₹164.00) | **+2.1% premium** — the only one | 97.2% (FY25) | not found |
| Knowledge Realty Trust | Office | Too new: ₹1.56 partial-period distribution on a ₹103 listing (18-Aug-2025), ~₹62,000 cr GAV | — | — | 92% H1FY26 (Hyderabad 99%, GIFT City 98%, Chennai 95%, Mumbai/Bengaluru/Gurugram ~88%) | not found |

Each leg `[1-SOURCE]`, yields `[COMPUTED]`; the audit recomputed every figure exactly and calls
this the most reliable section in the eight files (C-12). **Spread to the sovereign: −0.72pp at best
(6.24 − 6.96) to −2.27pp at worst (4.83 − 7.10)** `[COMPUTED]` (C-13) — **a starker negative carry
than China's own C-REIT-versus-bond gap at the top of its cycle.**

**Four limits, all pointing the same way.** (i) **The NAV-based yield is not a cap rate** — NAV nets
debt and a distribution is not NOI, so 4.57-5.54% is directional only; **NOI, gross asset value,
in-place-versus-market rent and market cap were not found for any of the five REITs in any pass**, a
gap cheaply closed from each trust's investor presentation. (ii) **Since-listing total returns are
the least reliable numbers in the file** — three of four carry internally inconsistent figures
(Brookfield's cited "+6%" fails arithmetic against its ₹279 debut; Nexus has three irreconcilable
figures), none adopted. (iii) **No residential or retail-residential REIT exists in India**
`[2-SOURCE, two independent legs]` — no listed residential proxy, so no residential cap-rate test is
possible at all. (iv) **Only SM REITs clear the G-sec, on prospectus projections.** SEBI notified
the framework in **March 2024** `[2-SOURCE]` — SPVs over single or few commercial assets of ₹50-500
crore, mandatory listing, 95% cash-flow distribution, ₹10 lakh minimum lot; every scheme found is
single-asset commercial office, projected **8.1-9.0%**, combined AUM "tripled to ₹1,070 crore"
`[1-SOURCE]`. Sub-two-year track records, never comparable to the large REITs as equivalent
evidence. **Publish no SM REIT scheme date or size from this pack**: the auditor recalls Platina as
India's first scheme (IPO December 2024, ~₹353 crore) with the Jul-2025 / ₹473 crore / 1.61x triple
belonging to Titania, which would make C6's own section internally impossible (D-04).

**Two literature findings bear on reading any of it.** Plazzi, Torous and Valkanov (2010), *Review
of Financial Studies*, find cap rates forecast realised returns well for apartments, retail and
industrial but **not offices, even in-sample** `[2-SOURCE via A2]` — and India's REIT sector is
almost entirely office. And Himmelberg, Mayer and Sinai (2005), *Journal of Economic Perspectives*,
the standard user-cost defence of a low-yield level, **failed a real out-of-sample test**: applied to
46 US metros before 2008 it judged most markets not overvalued immediately before a 30%-plus crash,
because its expected-appreciation input was fed by the bubble it was meant to test `[1-SOURCE via
A2]`. **A user-cost argument that India's compressed yields are justified carries the identical
self-referential failure and must not be the reason to dismiss the yield signal.**

**The route that could resolve this.** Maharashtra's registered leave-and-license system is the only
India source that could produce a transaction-based, locality-grain yield: rent registration is
compulsory and runs on the sale-deed sub-registrar geography, with Aadhaar e-KYC and no office visit
`[RECALL]`, and rent-agreement duty is low so under-declaration incentive is weaker than on sales
(an interpretation, not a source). **The sale-side half is already solved** by the free monthly
count-and-revenue channel `[DESK FILE]` (R18). **What remains genuinely unconfirmed is the rent side
— no published aggregate of counts, median rent, tenure or deposit has been located by any pass, and
no bulk route is known.** That gap, not the sale side, is the highest-value state-specific runsheet
row here.

---

### 7. WHAT IS NOT AVAILABLE ANYWHERE — THE RUNSHEET ROWS

| # | Gap | Cheapest route |
|---|---|---|
| 1 | A ward- or locality-level official price index (RBI HPI computes ward strata, publishes cities) | RTI or data-sharing request to RBI or a state Stamps department for the existing strata |
| 2 | Bulk or API access to registered-transaction microdata in any state | Per-record scripted retrieval on the principal's machine, ward by ward; or RTI |
| 3 | A persistent parcel identifier (survey, khasra, CTS, gat numbers do not compose) | Confirm ULPIN / Bhu-Aadhaar coverage |
| 4 | Any published leave-and-license rental aggregate | Maharashtra IGR, direct |
| 5 | RBI HPI's revision policy | Difference successive vintages of the same reference quarter |
| 6 | Whether RAPMS is a public series at all | One targeted check of RBI FSR and DBIE |
| 7 | QPR history retention on state RERA portals | One portal check per state |
| 8 | Bulk OC/CC issuance records | Municipal departments, city by city |
| 9 | Any peer-reviewed Indian infrastructure-premium hedonic coefficient | Estimate from scratch, or a dedicated refereed search |
| 10 | REIT NOI, GAV, in-place-versus-market rent, market cap | Each trust's own investor presentation |
| 11 | Census 2021 housing tables (the finest-grained stock data is ~15 years stale) | Confirm whether the round has been conducted or scheduled |
| 12 | Free gross home-loan disbursal data (only outstanding stock is free) | Use the Sectoral Deployment growth rate as a net-flow substitute, stated as such |

**The environmental gap governing all twelve: on 2026-09-11 the desk probed 37 endpoints from this
session and 36 were blocked at the proxy — every Indian official portal (data.gov.in, RBI DBIE, RBI
main, NHB RESIDEX, IGR Maharashtra, NGDRS, DILRMP, MahaRERA, Bhuvan, MoSPI), every private India
source probed (Magicbricks, Housing.com, Knight Frank India), and every international and
geospatial source. Only the GitHub control answered** `[DESK FILE, measured]`. Acquisition runs on
the principal's machine — a measurement, not a judgement call.

---

### WHAT THIS SECTION CHANGES ABOUT THE PLAN

1. **Build the RBI HPI dependent variable as two spliced series, not one**: 10-city / 2010-11 as the
   long history to 2025, 18-city / 2022-23 as the tail from Q1:2025-26, spliced
   `k = HPI_new(t0)/HPI_old(t0)`, both bases stored as separate vintages, never a Hamilton gap or
   percentile rank across the join. Delete every "ten cities, base 2010-11" description (§1).
2. **Replace "lag the last 2-3 quarters" with a vintage-differencing test** — store every vintage of
   every reference quarter from the first pull; no RBI revision policy is documented and the window
   in the dossiers was invented (§1).
3. **Write two ingestion constraints as hard rules**: the three price concepts never merge (RBI HPI
   registered, RESIDEX @ Assessment lender-valuation-at-sanction, RESIDEX @ Market listing/deal),
   with RESIDEX's two base breaks as separate vintages; and every series carries a loading factor L
   per city, **psf ratio = 1 + L, L up to 0.50 for Mumbai**, replacing the twice-refuted pack-wide
   "20-35%" constant (§1, §2).
4. **Re-order the Maharashtra build: the sale-side volume series is already free and cleaned, so
   spend the scraping budget on the ASR-to-consideration price ratio and the leave-and-license rent
   side** (§2, §6).
5. **Make every infrastructure feature a two-column event with the corrected dates, and mark
   Bengaluru PRR and Chennai Metro Phase 2 right-censored** — NMIA 25-Dec-2025, Jewar two zeros
   (28-Mar-2026, 15-Jun-2026), Samruddhi 5-Jun-2025, Coastal Road Ph.1 Aug-2025 with Ph.2 targeted
   Dec-2028; never a citywide metro dummy where corridor openings are years apart (§4).
6. **Make the 43CA/50C tolerance band time-varying — 5%, then 10%, then the 20% primary-sale-only
   window — verify it before anything else on the calendar, and register it as a break** alongside
   the Maharashtra 2020-21 stamp-duty holiday and the Gujarat 2023 jantri revision, in a registry
   that currently has no property-tax dimension at all (§4, §2).
7. **Score city supply elasticity on three layers — legal FSI cap, title and litigation friction,
   physical land availability — and treat the trade-press FSI ranking as a hypothesis.** Anchor
   Mumbai to Nagpal-Gandhi's +58% units / −24% prices only with its `[1-SOURCE]` unrefereed tag
   attached, carrying the ULCRA negative finding beside it with equal weight (§5).
8. **Estimate infrastructure and metro premia from scratch; import no consultancy percentage** — no
   peer-reviewed Indian hedonic coefficient was recoverable and the circulating "15-25% within
   500m-1km" figures have no published method (§5).
9. **Report every yield with its family, method and as-of date; publish the two-family conflict as
   the headline rather than a reconciled average, and always gross beside net.** Family-2 Mumbai
   corridors at 2.0-4.0% straddle and undercut the modern peak band of 3.29% while the Family-1
   national 5.16% sits above the modern trough band of 4.94%; on the net side, label property tax
   (one Pune worked example, true span to ~0.8% of value) and repairs (unsourced, the largest single
   deduction) as the two weakest lines, and state the after-tax band as ~1.0-1.6% for a top-bracket
   unlevered owner once the surcharge tiers are named (§6).
10. **Treat the whole India source estate as unreachable from any web session** — 36 of 37 probed
    endpoints were blocked at the proxy, so every acquisition step above is a principal's-machine
    task, and the twelve gap rows in §7 are the runsheet that task works from (§7).
