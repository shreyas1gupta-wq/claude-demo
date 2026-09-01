# PART B — The India capex-cycle case record

*Capex/infrastructure-supercycle monograph (atlas 1.6, seat L11) · Part B · v1.0 · 2026-09-01 ·
Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)*

*Governed by `research/CONTRACT.md`. Every figure below is search-verified as of September 2026
unless tagged `[VERIFY: ...]`. This Part reads `config/ladder.yaml`'s `L11_capex_cycle` entry
(τ½ 36–60 months, **Tier C**, `reduce_only: true`, `contribution_clamp: non_positive`, shared
`macro_credit_block` budget with L6/L10/L12) as its governing design and `docs/CYCLE_ATLAS.md`
row 1.6 as its brief: "Balance-sheet repair after an overbuild takes years of deleveraging no
information flow can shortcut (capacity limit)." The desk's pre-registered analogue trials
IN1–IN3 now live in `research/cycles/capex-deep/capex-RESULTS.md` — that file existed by the
time this Part was finished and its numbers are cited directly below, never recomputed. **This
is the India seat**: unlike the property-cycle and credit monographs, where India supplies one
thin domestic instance against eight-to-ten rich cross-country cases, here India **is** the case
record — three full domestic episodes plus a live fourth — and the three international mirrors
(Asian Tigers, China, US shale) serve only to calibrate what "fast" and "slow" repair look like
elsewhere, never to substitute for India's own evidence. India's **credit-side mechanics** —
bank+NBFC aggregation, sectoral deployment, GNPA chronology, AQR, IL&FS — are already covered in
full in `research/cycles/credit-deep/partB-cross-country.md` (its own case #10, "India
2003–2018") and `research/dossiers/03-credit-financial-cycle.md`; this Part cross-references
those figures by name and does not re-derive them. India's **property-cycle** side (RERA, the
2021–2026 residential upcycle, IL&FS→developer-financing freeze) is fully covered in
`research/cycles/fincycle-deep/partB-cases.md` §B3; again cross-referenced, not duplicated. This
Part's own job is narrower and real-side: what India's investment rate, capacity utilization,
and capital-goods order books actually did across four episodes, in numbers.*

---

## B1. Why the India instance is thin evidence and OBICUS is younger than the cases it measures

CYCLE_ATLAS.md's own honest count is n≈2–3 (2003–08, the 2011–20 "drought," 2021+), and this
Part adds a fourth, older episode (1994–97→2002) that the Atlas's own dossier work (D08,
`research/dossiers/08-india-mid-cycles.md`, §I4) already flags but does not treat as fully
separate from the credit cycle's own chronology — "this dossier's capex-cycle state variable and
Workstream 03's credit-cycle/GNPA state variable are likely highly correlated, not independent."
That warning holds throughout what follows: every case below sits on top of a credit event this
desk's credit monograph already dates, and the two must never both be weighted at full strength
in the composite regime score (ladder.yaml already enforces this via the shared
`macro_credit_block` budget, not an additive one).

**The measurement-honesty problem this desk owes itself, stated up front (the direct capex
analogue of the property monograph's own §B3 admission).** RBI's Order Books, Inventories and
Capacity Utilisation Survey (OBICUS) — the cleanest, highest-frequency, free capacity-utilization
series India has — has been conducted only since 2008. That means **OBICUS did not exist for
case 1 (1994–2002) and covers only the tail end of case 2's boom (2003–2011)** — the two
episodes with the sharpest booms in this record are the two the desk's best instrument cannot
see in real time. MOSPI's IIP capital-goods sub-index runs further back (current base year
2011–12, after a revision from an earlier 2004–05 base `[VERIFY: exact revision year — dossier
08 flags this same uncertainty]`) but is itself subject to periodic base-year splices that
demand the same discipline the ladder's `tau_half_drift_policy` and the property monograph's
2026-rebase warnings already apply elsewhere. Quarterly GFCF/GDP (MOSPI National Accounts) is
the longest-running of the three free proxies and the only one that reaches back cleanly into
case 1, but it is a *ratio*, not a *rate of capacity use* — it tells you how much of GDP went
into fixed investment, not whether that investment was chasing genuine excess demand or
running into an already-glutted sector. The free substitute triad the credit-side dossier
already names — **OBICUS + IIP capital goods + GFCF/GDP** — is the correct free construction
(CMIE's project-level Capex database, the field's best-known tracker of stalled/announced/
completed projects, is a **paid** source and is used below only where a public news report has
already reproduced a specific CMIE-sourced figure, each flagged accordingly per the Contract's
free-data rule).

---

## B2. Four India case studies

### 1. India 1994–97 → 2002 — the first liberalization capex boom and bust

**Setup — what 1991 actually removed.** Facing a 1991 balance-of-payments crisis, the Government
of India dismantled the industrial licensing regime ("License Raj"), formally empowered SEBI as
market regulator, established the National Stock Exchange, and opened Indian equities to foreign
institutional investors. The immediate capital-markets effect was on *pricing freedom*: premium
(above-par) issues, which were just **1.37% of new issues in 1991–92**, rose to **45.90% by
1994–95** — the single cleanest statistic of how completely the pre-liberalization administered-
price regime for new capital had been dismantled in three years.

**The boom, dated precisely.** India's primary-equity-market mania "began towards the end of
1994 and peaked in February 1995." **January 1995 alone saw 145 equity issues open for
subscription**, including "mega issues" from Reliance Capital, Essar Oil, Jindal Vijaynagar
(now JSW Steel's predecessor), and Hindustan Petroleum. **In one week in February 1995, 78
companies went public**, capping a fiscal year (1994–95) that saw roughly **1,400 issues** hit
the market; year-on-year primary-market growth in 1995 alone ran at **32%**. This was the
capital that funded India's first wave of greenfield private-sector steel, textile, and
petrochemical capacity — the boom's real-economy content, distinct from a pure financial mania,
is that the equity actually financed physical plant that came onstream over the following
several years, exactly the capacity the 1997–98 commodity collapse then found itself competing
to sell into.

**The turn.** The boom halted with the July 1997 Asian financial crisis (the desk's own Asian
Tigers mirror, case 5 below, is the direct contagion source). India's own growth decelerated
from 7.8% (1996–97) to **4.8% in 1997–98**, recovering only partially to 6.5% the following
year; the rupee depreciated **13.1% between April and September 1998** as the crisis's regional
currency pressure reached India even though India's own trade exposure to Asia was modest (Asia-
directed exports were under 2% of GDP `[source: IMF ADBI working paper]`). Global commodity
prices — steel, petrochemicals, textiles chief among them — fell sharply through 1997–98,
directly compressing the revenues of the plants the 1994–96 equity wave had just built; a
precise, sourced capacity-utilization series for Indian steel/petrochem/textiles in this specific
window could not be independently confirmed this pass and is flagged `[VERIFY: sector-level
utilization data 1997–2001 — pre-OBICUS era, likely only recoverable from CII/FICCI/industry-
association archives or contemporary RBI Annual Reports, not a modern online database]` — this
is precisely the §B1 measurement gap in its starkest form: the boom whose bust this desk most
wants a utilization number for is the one era with no free, machine-readable series at all. The
Annual Survey of Industries (ASI, MOSPI) does run continuously back through this period and in
principle carries sector-level output and capacity data, but ASI's own multi-year publication lag
and its unit of observation (registered factories, not a use-based capacity-utilization percentage
comparable to OBICUS) make it a poor substitute for a real-time cycle read even after the fact;
contemporary industry-association commentary (CII, FICCI) from 1997–2001 is qualitatively
consistent with widespread steel/textile/petrochemical overcapacity but was not aggregated into
any single, citable, free index this pass could locate. The honest conclusion for the data phase:
**case 1 can be dated and sized on its financial side (equity issuance, GNPA) but not on its
real-capacity side** — any future purged backtest that tries to condition L11 on a full,
uniformly-measured 1994–2020+ history should expect its effective sample to begin no earlier than
MOSPI's IIP capital-goods series (itself base-year-spliced) or, cleanly, OBICUS in 2008 — meaning
roughly the first decade of this four-episode case record sits outside what any India-only L11
backtest could actually condition on, reinforcing why the ladder already treats cross-country
analogue pooling (as in `capex-RESULTS.md`'s IN1–IN3) as the only route to a Tier-B graduation.

**The NPA overhang, verified.** The banking system's own aggregate is the best-measured proxy
for the bust's severity. Total gross NPAs across the banking sector stood at **₹34,428 crore, or
roughly 14.4% of gross advances, in 1998**; GNPA growth ran at roughly 11% in 1999 before turning
negative after 2002. For nationalised banks specifically, the GNPA ratio fell from **19.05%
(1997) to 12.16% (2001)** — a genuine, multi-year improvement, but one that itself confirms how
extreme the starting point was: a system-wide NPA ratio in the high teens is the direct legacy of
the 1994–97 lending-and-equity boom meeting the 1997–98 commodity bust, still being worked off
five years later.

**CDR, born 2001.** The RBI's Corporate Debt Restructuring mechanism — the desk's first
institutional answer to exactly this kind of overhang — was formally issued via detailed
guidelines on **23 August 2001**: a voluntary, non-statutory, three-tier structure (CDR Standing
Forum, CDR Empowered Group, CDR Cell) built explicitly on the UK/Thailand/Korea/Malaysia
precedent, binding a minimum ₹100 million exposure once creditors representing 75% of value
agreed. CDR is the direct institutional ancestor of the SDR/5:25/S4A "alphabet" case 3 below
documents in more detail for the next cycle's bust — the mechanism type (restructure-in-place
rather than liquidate) recurs across both India busts even as the specific tools evolve.

**SICA/BIFR — the era's actual workout venue, and its weak record.** The Sick Industrial
Companies (Special Provisions) Act, 1985 (SICA) — predating this boom, born of 1980s industrial
sickness on the Tiwari Committee's recommendation — established the Board of Industrial and
Financial Reconstruction (BIFR) as the formal rehabilitation venue that absorbed much of the
1997–2002 overhang. By 2007, BIFR had registered **5,471 references** since inception, of which
**1,337 were recommended for winding up and only 825 revival schemes were ever sanctioned** — a
revival success rate of roughly **12–15%**. Roughly **4,700 cases were referred to BIFR across
its full 1987–2016 life** `[the two counts — 5,471 registered by 2007 vs. ~4,700 total referred
over 1987–2016 — are not fully reconciled by this pass; likely reflects registered-vs-referred
definitional differences; VERIFY]`. SICA was formally repealed effective **1 December 2016** (via
the Sick Industrial Companies Repeal Act, itself dated 2003 but implemented only in 2016) —
meaning the *legal machinery* born to handle the 1994–2002 bust remained the nominal venue for
industrial distress for another 14 years after the crisis it was built for had already passed,
right up until IBC 2016 (case 3 below) replaced it entirely. **L11 lesson.** This is the record's
cleanest demonstration that an India capex bust's *institutional* repair lags its *financial*
repair by a wide margin — GNPA improved from 19% to 12% over 1997–2001, but BIFR kept clearing a
backlog of the same era's sick companies for another decade and a half, a workout-venue lag this
desk should expect to recur (and, per case 3, did recur, in a different institutional form).

### 2. India 2003–2011 — the infra supercycle

**The GFCF/GDP arc — verified directionally, contested precisely.** Multiple sourcing passes
converge on the *shape* — a sustained investment-rate climb from the low-to-mid 20s (% of GDP) in
the early 2000s to a clear multi-year peak around 2007–08 — but not on one clean number, and the
gap is itself informative in the same way the fincycle monograph's US price-to-income
reconciliation gap was: one widely cited compilation puts GFCF near **27% of GDP by 2007–08**, up
from roughly 10% in the 1980s; a separate practitioner framing places the Manmohan Singh-era
peak closer to **30–35% of GDP**, and RBI's own historical Gross *Capital* Formation series
(which, unlike GFCF, includes inventory change and is therefore structurally higher) is the
likely source of readings nearer **36–38%** for the same peak year `[VERIFY: reconcile GFCF
(excludes inventories) vs. Gross Capital Formation (includes inventories) as the source of this
9–11-point spread — the task's own "~26% FY03 to ~36% FY08" framing sits inside this same
reconciliation gap and should not be read as a single authoritative print until the data phase
pulls the primary MOSPI National Accounts series directly]`. What is not contested: the direction
and the order of magnitude — a rise on the order of **10–15 percentage points of GDP over five
to six years**, among the largest sustained investment-rate accelerations this record documents
for any economy at any point (compare the Asian Tigers' own 30%+ decade below, case 5) — and a
peak concentrated in 2007–08, precisely the year OBICUS itself (once it starts in 2008) opens at
its own all-time high.

**Power — Ultra Mega Power Projects and merchant-power mania.** Of nine originally proposed
4,000 MW-scale UMPPs, **four were actually awarded**: **Mundra** (Gujarat, Tata Power, the first
UMPP commissioned, 4,000 MW), **Sasan** (Madhya Pradesh, handed to Reliance Power **7 August
2007**, 3,960 MW), **Krishnapatnam** (Andhra Pradesh, handed to Reliance Power **29 January
2008**, at a levelised tariff of ₹2.33/kWh), and **Tilaiya** (Jharkhand, handed to Reliance Power
**7 August 2009**, though ultimately never commissioned `[VERIFY: Tilaiya's final status]`). The
five unawarded UMPPs are themselves a data point — a scheme conceived at nine-project scale that
delivered four is the boom's first, quiet capacity-versus-ambition gap, well before the more
famous 2011–20 stalls (case 3). **Coal linkages** were the structural fault line power capacity
kept running into throughout this boom and into the next decade: fuel-supply-agreement
uncertainty for plants built without secured, long-term domestic coal linkage is the direct
through-line from this era's overbuild into case 3's 2011–13 stalls.

**Roads — NHDP, phase by phase.** The National Highways Development Project, launched **1998**
under PM Vajpayee, ran through this boom as India's flagship road-capex program, ultimately
covering **~49,260 km**: Phase I (Golden Quadrilateral, 5,846 km, declared complete as a
four-lane network **January 2012**), Phase II (North-South/East-West corridors, 7,142 km), Phase
III (**approved 12 April 2007**, 12,109 km on a Build-Operate-Transfer basis), Phase IV
(**approved 18 June 2008**, 20,000 km of non-Phase-I/II/III widening), Phase V (6,500 km
six-laning), Phase VI (**approved November 2006**, 1,000 km of expressways), Phase VII
(**approved December 2007**, ring roads/bypasses/flyovers). The clustering of Phase III, IV, VI,
and VII approvals in the 2006–08 window is itself a direct capex-cycle signature — four of seven
NHDP phases were greenlit inside a three-year span sitting exactly at this boom's peak, before
the program was eventually subsumed into Bharatmala around 2018 (spanning case 3's repair
years).

**Telecom — spectrum, administratively priced.** Following India's 2001 spectrum auction, the
government abandoned auction-based allocation in favor of **administrative allocation at fixed,
un-escalated prices**; in 2008, **122 new 2G licenses** were issued first-come-first-served at
**2001-era prices**, which the Comptroller and Auditor General later estimated cost the exchequer
on the order of **$40 billion** in foregone revenue (a separate estimate puts the associated
investment outflow at **₹2,90,000 crore, roughly $47 billion**) `[figures per CAG audit and
contemporary reporting; the precise reconciliation between the "$40bn exchequer loss" and
"₹2.9 lakh crore investment outflow" framings is not attempted here — VERIFY if the distinction
matters for a future dossier]`. This is a capex-*adjacent* rather than capex-proper episode — the
spectrum scandal is fundamentally a rent-allocation story, not an investment-rate one — but it
belongs in this chronology because the underpriced spectrum directly subsidized the huge
build-out of GSM network capacity (towers, base stations, backhaul) that *was* real capex, timed
squarely inside this same 2003–2011 window.

**SEZs — the land-mania leg.** Special Economic Zones approvals concentrated almost entirely in
this window: **235 SEZs formally approved in 2006** alone; of the **54 notified in 2006**, 51
were operational; of **96 notified in 2007**, 75 were operational; by **December 2008, 181
notified SEZs existed for IT alone**, 66% of the total SEZ count at that date. The UPA government
eventually cleared **576 SEZs covering 60,375 hectares**, of which **392 (45,636 hectares) were
formally notified by March 2014** — meaning even the *approval* pipeline (as distinct from actual
build-out) kept running for years after this boom's peak. The land-acquisition backlash —
**Nandigram, West Bengal, 2007**, the era's most politically consequential single episode — is
the direct institutional-memory link this desk should carry into how it reads any *future*
India land-intensive capex wave: SEZ-scale land acquisition triggered enough political cost that
no comparably aggressive SEZ program has been attempted since.

**The IPO/QIP funding wave and Reliance Power as the top-tick artifact.** The boom's financing
side ran overwhelmingly through public and quasi-public equity — precisely the 1994–97
mechanism recurring at ten times the scale. The single cleanest artifact in this entire case
record is the **Reliance Power IPO**: **₹11,700 crore**, priced at **₹450/share**, opened
**January 2008**, oversubscribed **73×**, for a company that at the time of its IPO had **no
operating assets and no cash flow** — pure greenfield power-capacity promise monetized at the
absolute top of a six-year boom. It listed **11 February 2008**: opened at ₹530 (a 17% premium
to issue), then closed the same day at **₹372** — a loss for day-one allottees before the stock
went on to fall much further over the following years. The date is not incidental: Reliance
Power's IPO closed for subscription within days of the Sensex's own then-all-time closing high
(January 2008) `[VERIFY: exact Sensex peak date and level in January 2008 — recalled as ~21,000
on 8 January 2008 with moderate confidence, not independently re-confirmed this pass]` — the
single most literal "IPO at the top" instance this desk's entire cycle-atlas project has yet
documented, a domestic Indian analogue to what the property monograph's own Ciudad Real airport
and golf-membership-index artifacts do for Spain and Japan respectively.

**Capital-goods order books as the cycle thermometer.** BHEL's own multi-year trajectory tracks
the boom-to-bust arc directly: the stock **peaked during the 2007–08 bull cycle**, then entered a
multi-year decline whose order-book evidence is covered in more detail under case 3 below (BHEL's
order book fell 7.3% YoY to ₹1,46,500 crore by December 2012, with a negative quarterly order
inflow around the same time) — the same capital-goods names that thermometer the boom's peak in
this case thermometer its bust in the next one, a single continuous instrument spanning both
episodes.

**The 2008 interruption and the 2009–11 last leg.** The global financial crisis interrupted, but
did not end, this boom: the Sensex fell **~60–64% between January and October 2008** (figure per
the credit monograph's own case #10, not recomputed here), but fiscal stimulus and continued
infra spending sustained real capex into **2009–11** — the boom's genuine "last leg," visible
most clearly in OBICUS's own opening years: capacity utilization reached an **all-time series
high of 83.2% in March 2011**, the single highest print OBICUS has ever recorded, arriving
*after* the 2008 interruption rather than before it. That print is this Part's cleanest example
of a textbook late-cycle utilization peak: the highest capacity-use reading in the whole 18-year
OBICUS history sits at the exact hinge between this boom and case 3's decade-long drought,
exactly the kind of signal L11's non-positive contribution clamp is designed to act on only in
its *falling* leg, never to chase on its way up.

### 3. India 2011–2020 — the twin-balance-sheet decade

**Framing — cross-referenced, not re-derived.** The credit-side chronology of this decade —
GNPA's masked-then-forced-disclosure arc, the AQR shock, IL&FS, the GNPA peak and trough — is
already fully documented in `research/cycles/credit-deep/partB-cross-country.md`'s own case #10
("India 2003–2018") and in the Economic Survey 2016-17's own Chapter 4, **"The Festering Twin
Balance Sheet Problem"** (already cited in that monograph's references). This Part's job is the
*real-side* record those credit-side numbers sit on top of: what capex, capacity use, and the
capital-goods order pipeline actually did across the nine years the credit monograph's own GNPA
cycle spans "roughly a decade: AQR (2015) → decadal low (2.15%, 2025)."

**2011–13: the stall begins, before AQR even forces recognition.** The proximate trigger long
predates 2015's formal reckoning. Coal-linkage, land-acquisition, and environmental-clearance
bottlenecks — the fault lines case 2's own UMPP and power-sector build-out had already exposed —
seized up broadly: an estimated **$45 billion of investment was held up** by clearance and
land-acquisition bottlenecks; **154 Coal India projects (210 million tonnes of production
potential)** sat awaiting environment/forest clearances, with delays projected to cost roughly
**190 million tonnes of lost output by March 2012**; individual projects stalled visibly and
publicly — the **Nabinagar Super Thermal Power Project (1,980 MW)** halted for 15 days in
February 2012 alone over farmer land disputes. CMIE's own project database — a **paid** source
under this Contract's free-data rule, cited here only via public reporting of its headline
figures — recorded new-project announcements collapsing to a **14-year low**, with roughly
**₹1 lakh crore of new projects launched in one quarter versus ₹4 lakh crore at the start of the
same year**, and new private-sector project announcements falling **62% quarter-on-quarter** at
one point in the decline `[VERIFY: exact reference quarter/year for this specific CMIE-sourced
figure — recovered from a secondary news compilation, not CMIE's primary release]`. Among stalled
projects broadly, **power accounted for 35.4%** and **manufacturing over 29%** — the two sectors
this Part's case 2 identifies as the boom's own two largest legs are also its two largest stall
categories, a direct overbuild-to-stall mapping.

**The restructuring alphabet, 2001→2016.** CDR (born 2001, case 1 above) proved insufficient for
this decade's scale; three further RBI mechanisms followed in quick, escalating succession:

| Mechanism | Date | Core feature |
|---|---|---|
| **CDR** (Corporate Debt Restructuring) | Guidelines 23 Aug 2001 | Voluntary, non-statutory; 75%-by-value creditor vote binds all; three-tier structure |
| **5:25 scheme** | Dec 2014 | Infra/core-sector loans >₹500 cr; tenor extendable to 25 years, refinanced every 5 years |
| **SDR** (Strategic Debt Restructuring) | 8 Jun 2015 | Lenders convert debt (incl. unpaid interest) into ≥51% equity; must sell ≥26% to a new promoter with right of first refusal |
| **S4A** (Scheme for Sustainable Structuring of Stressed Assets) | 13 Jun 2016 | Debt bifurcated into "sustainable" (≥50% of exposure, serviceable from current cash flow) and "unsustainable" (converted to optionally convertible debentures) |
| **IBC** (Insolvency and Bankruptcy Code) | Enacted 2016 | Time-bound (originally 180+90 day) resolution or liquidation via NCLT, replacing SICA/BIFR entirely |

Each successive mechanism tried to buy the restructured borrower more time or more creditor
control without forcing recognition or a change of control — and each was judged, within one to
three years, to have been insufficiently forceful, which is precisely why the sequence escalated
to statutory liquidation-backed resolution (IBC) rather than stopping at any earlier station.

**The AQR recognition shock, August 2015, and the RBI circular that followed.** Cross-referencing
the credit monograph directly: the AQR forced banks to reclassify previously obscured stressed
loans, a **measurement break, not a fresh credit event** (that monograph's own words). On top of
IBC, RBI issued a further circular on **12 February 2018** mandating banks to refer any account
with exposure over **₹2,000 crore** to IBC if unresolved within 180 days of default — a blanket,
size-triggered rule with no case-by-case discretion. The Supreme Court struck this circular down
as **ultra vires** the Banking Regulation Act in ***Dharani Sugars and Chemicals Ltd. v. Union of
India***, decided **2 April 2019** — RBI's Section 35AA power, the Court held, did not extend to
issuing directions for *all* cases without considering specific defaults; every action taken
under the circular, including Section 7 IBC applications already filed, was declared **non-est**.
**L11/credit-interface lesson.** A blanket administrative resolution mandate — the same
instinct behind Japan's 1990 MOF quantity controls and China's 2020 "three red lines" (see case 7
below and the fincycle monograph's own China case) — was tried in India too, and was the one
tool in this entire cross-country record to be **judicially invalidated** rather than merely
phased out or superseded; the desk should read India's institutional capacity to check its own
regulator, even mid-crisis, as a structural feature distinguishing this repair from several of
the mirror cases.

**The 12 large accounts, the second list, and the steel-vs-power resolution gap.** RBI directed
lenders on **13 June 2017** to refer a first list of **12 large stressed accounts** — Essar Steel, Bhushan
Steel, Electrosteel Steels, Amtek Auto, Bhushan Power and Steel, Alok Industries, Monnet Ispat,
Lanco Infra, Era Infra, Jaypee Infratech, ABG Shipyard, and Jyoti Structures — together
accounting for roughly **a quarter of the system's then ₹8 trillion of NPAs**. The two steel
resolutions were the record's cleanest successes: **Essar Steel** recovered **92% of ₹49,000
crore** owed, after an 850-day process that went all the way to the Supreme Court, with
ArcelorMittal ultimately taking control from the Ruia family; **Bhushan Power & Steel** recovered
roughly **41% of ₹47,000 crore** owed (₹19,350 crore realized), with JSW Steel completing the
takeover in **March 2021**. **Power's resolution ran on a dramatically longer, still-incomplete
clock.** The Ministry of Power classified **34 coal-based thermal plants (40.1 GW, ₹1.7 trillion
of debt, ~$23bn) as "stressed" in March 2018**; more broadly, roughly **66 GW of conventional
generation capacity** sat under some degree of financial stress (54,805 MW coal across 44
assets, 6,831 MW gas across 9 assets, 4,571 MW hydro across 13 assets). Thirty-four stressed
power projects (~40,000 MW) were expected at insolvency courts as RBI's referral deadline
arrived in August 2018 — yet **as of April 2023, only 26 of those 34 had been resolved fully or
partially, with strategic buyers acquiring just 11** `[VERIFY: precise current 2026 resolution
count — this pass located the April 2023 figure only]`. RBI followed the June 2017 list with a
**second letter to lenders, dated 28 August 2017**, naming **28 further large stressed accounts**
— together roughly **40% of a ~₹4 trillion bad-loan pool** — with a self-resolve deadline of
**13 December 2017** and a hard NCLT-referral deadline of **31 December 2017**; banks ultimately
referred **23 of the 28** to insolvency proceedings once the deadline passed. The two-list
structure (12, then 28 — 40 large accounts in total across roughly six months) is itself a data
point on how the regulator's own confidence in voluntary restructuring (CDR/SDR/5:25/S4A) had
collapsed by late 2017: a mechanism list that had taken **sixteen years to build** (2001→2016,
the table above) was, within eighteen months of IBC's enactment, effectively set aside in favor
of time-bound statutory referral for the system's largest defaulters. Set against Essar Steel's
850-day (2.3-year) full resolution, power's own referral-to-partial-resolution arc already ran past **five
years** for barely three-quarters of the cohort — the single clearest sector-level confirmation
in this whole India record that a capex bust's *physical and regulatory* complexity (tariff
regulation, fuel-linkage disputes, state-discom payment risk — none of which apply to a steel
mill in the same way) governs repair speed independent of the credit-side resolution machinery
available to it.

**IL&FS, September 2018, and the second leg down.** Cross-referencing the credit monograph
directly: IL&FS's default (debt of ₹91,091 crore, ~$13bn) triggered a system-wide NBFC funding
freeze. This Part's own addition, cross-referencing the fincycle monograph's own §B3: by the
mid-2010s NBFCs/HFCs had become **developers' primary — often sole — source of construction and
land finance** (NBFC real-estate exposure ~₹1.65 trillion, 7.5% of the sector's book, as of March
2018), so the September 2018 freeze hit real-estate and infrastructure capex with particular
force precisely because both sectors had grown so dependent on the single channel banks had
already largely exited post-AQR. **DHFL and YES Bank, 2019–20, the crisis's final leg.** DHFL's
own default fed directly into **YES Bank's** subsequent collapse — YES Bank had been a large
DHFL creditor — culminating in the RBI imposing a 30-day moratorium on **5 March 2020**,
superseding the bank's board, capping withdrawals at ₹50,000 per depositor, and drafting the
**"Yes Bank Ltd. Reconstruction Scheme, 2020"** the following day; the State Bank of India
ultimately infused ₹7,250 crore for a 45% stake. YES Bank's stock, which had traded near ₹404 at
its own peak `[VERIFY: exact peak date — one source recalls August 2019, though the more commonly
cited all-time high is August 2018; not reconciled this pass]`, fell to a record low of **₹5.65
in March 2020** — a >98% collapse from peak, and the decade's final, and in equity terms most
violent, single credit event before COVID arrived days later.

**Nine years of repair — the measured India instance of IN2's claim.** `capex-RESULTS.md`'s own
pre-registered IN2 trial (18-country JST panel, capacity-state "regaining its peak") finds a
**median repair length of 4 years**, passing its own pre-set bar (median ≥4y) "exactly at the
bar," with a wide IQR of 1–12 years across 195 peak spells. India's own 2011–2020 episode — nine
years from the 2011 GFCF/OBICUS peak to what most measures treat as the decade's real trough —
sits toward the **long end** of that pooled distribution, not at its median: a genuinely severe,
not merely typical, repair by the panel's own cross-country yardstick, consistent with IN2's own
note that the median is itself pulled down by "many iy peaks [that] are shallow local maxima, not
overbuilds" — 2011's OBICUS all-time-high print (case 2 above) was emphatically not a shallow
local maximum.

**What utilization/IIP-capgoods/GFCF actually printed.** OBICUS fell from its **March 2011
all-time high of 83.2%** to a **record low of 47.3% in June 2020** (the COVID trough, not a
"pure" capex-cycle print on its own, but the terminal point of a decade already in decline before
COVID arrived). GFCF/GDP fell from its **~34–35% 2007–08 boom peak** to roughly **28–29% through
the 2011–2020 "capex winter"** `[figures per dossier 08's own recollection-level estimate;
VERIFY against primary MOSPI data before any backtest use]`. IIP capital-goods and capital-goods
order books moved in the same direction across the same window: BHEL's order book fell **7.3%
year-on-year to ₹1,46,500 crore by December 2012**, with a negative quarterly order inflow
(~−₹1,800 crore) around the same date; L&T similarly cut its own FY16 fresh-order growth guidance
from an initial 15% down to 0–5% by December 2015, with FY16 order flow ultimately declining 12%
— a mid-decade order-book air-pocket sitting squarely inside the drought's second half, well
after the AQR shock had already begun forcing recognition, evidence that the real-side repair
lagged even the credit-side recognition event by several further years. **L11 lesson.** Every
free real-side proxy this desk can construct — capacity use, capital-goods orders, the investment
ratio itself — moved in the same direction, for the same nine years, as the credit-side GNPA
cycle the sibling monograph already documents; the two are not independent confirmations of one
underlying process, which is exactly why ladder.yaml's shared macro-credit-block budget (rather
than two additive seats) is the correct design and why L11's own `inputs: [L10_credit_block]`
dependency edge in the DAG is not decorative.

### 4. India 2021–2026 — the public-capex era

**The central capex budget arc, verified.** Union Budget capital expenditure allocations rose
sharply and consistently across this window:

| Fiscal year | Capex (Budget Estimate) | YoY / note |
|---|---|---|
| FY21 | ₹4.12 lakh crore | pre-PLI baseline |
| FY22 | ₹5.54 lakh crore | +34% |
| FY23 | ₹7.5 lakh crore | +35% |
| FY24 | ₹10.0 lakh crore | +39% |
| FY25 | ₹11.11 lakh crore (BE); ₹10.18 lakh crore (RE) | RE well below BE — the first visible execution gap |
| FY26 | ₹11.21 lakh crore | **only +0.9% vs. FY25 RE — a sharp deceleration** |
| FY27 | ₹12.21 lakh crore | +9% |

The **FY22–FY27 CAGR is ~19.4%**, and capex/GDP sits near **3.1%** by FY27 (BE) — but the FY25
RE-vs-BE shortfall and FY26's near-flat sequential growth are the arc's own honest caveat: the
public-capex engine that drove the first four years of this episode was already decelerating
before the private-capex-revival debate (below) had even resolved itself.

**PLI, verified.** Production-Linked Incentive schemes across **14 sectors** carry a combined
outlay of **₹1.97 lakh crore** (~$26bn) `[one PIB release cites ₹1.91 lakh crore for essentially
the same 14-sector count — the two-figure spread is not reconciled this pass, VERIFY]`. By
March 2024, **755 applications had been approved**, with **₹1.23 lakh crore of investment
attracted**; by December 2025, the cumulative count had grown to **836 applications approved**,
**over ₹2.16 lakh crore of cumulative investment**, **over ₹20.41 lakh crore of cumulative
sales**, **over ₹8.3 lakh crore of cumulative exports**, and **more than 14.39 lakh direct and
indirect jobs**. PLI is this episode's clearest example of *directed* private capex — incentive-
contingent, sector-targeted, and (unlike the 2003–11 boom's IPO-financed greenfield building)
explicitly manufacturing-export-oriented from inception.

**Corporate deleveraging, completed before this episode began, not during it.** The listed-
corporate debt/equity ratio fell from **0.73 (FY20) to 0.59 (FY21)** — "the lowest in six years"
— with roughly **750 companies reducing gross debt by a combined ₹3 trillion in FY21 alone**.
Net debt-equity had, in fact, already improved for **three consecutive years by FY18**,
meaning the deleveraging cycle this episode's private-capex-revival debate depends on had been
running for the better part of a decade before 2021, not as a response to it — a sequencing
point directly relevant to how much of 2021+'s capex should be read as balance-sheet-enabled
rather than newly demand-driven.

**Bank balance sheets cleaned, verified with a precise trend.** Gross NPA for scheduled
commercial banks has fallen for **six consecutive years** since its 2017–18 peak of 11.2%: **2.8%
by March 2024** (RBI Financial Stability Report), **2.6% for 37 SCBs by September 2024**, and a
**historic low of 2.15% (domestic operations) by September 2025** — explicitly lower than the
system's own 2010–11 level, i.e. below the level that prevailed even before case 2's own boom
had finished building the assets that eventually soured into case 3's crisis.

**The "private capex revival" debate, year by year, with the tension made explicit.** Private
capex rose sharply on one widely cited measure — **+67% year-on-year to ₹7.7 lakh crore**
(manufacturing ₹3.8 lakh crore, roughly half, led by metals/autos/chemicals; services ₹3.1 lakh
crore, led by trading/communications/IT) — described in contemporary coverage as "the strongest
investment revival in over a decade." Aggregate capex reported by **1,899 listed non-financial
companies grew 11% to ₹9.4 trillion in FY25**. Set directly against that: CMIE recorded
**₹14.3 lakh crore of project withdrawals in a single quarter in late 2025** — a reminder,
in the credit monograph's own house idiom, that "the boardroom can say 'approved' while the
construction site is still waiting for the bulldozer." L&T's own chairman stated in August 2025
that private capex is now "substantial" in the company's order book, the same capital-goods-
order-book thermometer cases 2 and 3 already establish as this record's most reliable
real-time gauge — but a single large contractor's order book is not, on its own, a system-wide
private-capex confirmation. **OBICUS, the free arbiter, sits right at the practitioner
threshold this desk's own dossier already flags as a magic-number trap:** **76.8% (Q4 FY24,
March 2024)**, **77.7% (Q4 FY25, up from 75.4% the prior quarter)**, **75.6% (Q3 FY26, December
2025, up from 74.3% in September 2025)** — a series oscillating in the mid-to-high 70s for two
full years, consistent with the "~75%" heuristic threshold at which practitioners claim fresh
private capex "switches on," but doing so as a *level*, not a *trend break* — exactly why
CONTRACT §6 and dossier 08 both insist on the *percentile rank* of this series as the correct
construction, never the fixed 75% number itself.

**Real-estate and power-demand upcycle.** The residential-property side of this episode is fully
covered in the fincycle monograph's own §B3 ("The 2021–2026 upcycle": record 302,867 unit sales
in 2024, the luxury/affordable divergence, RERA/GST as the structural reset) and is not
re-derived here. This Part's own free-standing addition is the power-demand side: India's peak
electricity load rose from **148 GW (2014) to 250 GW (2024), a 68% increase**, then to an
**all-time high of ~256 GW**, surpassing the prior 250 GW record set 30 May 2024. Air-conditioning
is the single largest marginal driver — **14 million AC units sold in 2024, up 27% from 11
million in 2023** — with cooling load estimated at **~60 GW of the 2024 peak**, projected toward
**one-third of total peak load by 2030**. Rising power demand is this episode's most demand-side-
driven capex trigger (as distinct from PLI's supply-side, incentive-driven capex), and the two
sit uneasily on the same "is this a real supercycle" question the next paragraph makes explicit.

**The honest open question, and why L11's clamp means the desk need not resolve it.** Is
2021+ arc #3 — a genuine repeat of case 2's investment-rate supercycle — or a public-spending
plateau that has not yet, and may never, hand off cleanly to broad-based private capex? The
evidence that would distinguish the two: (i) GFCF/GDP durably re-crossing back toward the
~34–36% 2007–08 peak rather than plateauing in the 31–33% range dossier 08 already estimates
for 2022–23 onward; (ii) OBICUS's percentile rank, not its level, breaking cleanly into its own
historical top quartile rather than oscillating near a round-number heuristic; (iii) private
capex broadening past PLI-eligible and large-conglomerate order books into the CMIE-tracked
project-announcement base *net* of the withdrawal rate already documented above; (iv) whether the
FY26 budget's near-flat capex growth (+0.9%) is a one-year pause or the start of the public-
spending engine's own rolloff without a private handoff underneath it. **The desk does not need
to answer this before the model can be built.** `capex-RESULTS.md`'s own IN3 trial found that a
hot capex state does not order forward five-year returns monotonically at all — the top-quintile
capex-state country-years produced *lower* pooled forward returns (+0.242, log) than the
bottom-quintile (+0.287), with the *middle* quintile lowest of the three (+0.202) — precisely
the "weakly informative, never monotonic" signature that ladder.yaml's `contribution_clamp:
non_positive` already encodes: L11 is built to matter only when the capex/utilization state is
extreme and hot, and only ever to *subtract* permission from the shared macro-credit-block
budget in that state, never to *add* on the strength of a plausible-sounding "arc #3" narrative.
Whether 2021+ eventually resolves as a supercycle or a plateau, the clamp guarantees the reading
can never do more than fail to fire — the one design choice in this entire monograph that turns
a genuinely unresolvable forecasting question into a non-issue for portfolio construction.

---

## B3. Three international mirrors — analogue calibration only

### 5. Asian Tigers 1990s — the overinvestment-plus-currency-mismatch benchmark

**The boom.** Domestic saving and investment rates in Thailand, Indonesia, Korea, and Malaysia
averaged **more than 30% of GDP across 1986–1996** (Radelet-Sachs), with the task's own framing
of "35–40%+" for individual peak years/countries consistent with, though not independently
re-derived to decimal precision by, this search pass `[VERIFY: country-by-country World Bank GFCF
series for the precise 1996 peaks by country]`. Crucially, unlike either of India's own booms
(cases 1 and 2, funded overwhelmingly in domestic-currency bank credit and domestic equity), a
large share of this investment was financed through **short-term, unhedged foreign-currency
debt** — the structural fault line India's own capex cycles have never carried at comparable
scale.

**The 1997 crisis.** The Thai baht floated **2 July 1997**, triggering contagion across Indonesia,
Korea, and Malaysia; **net private capital flows to the five crisis economies reversed by roughly
$105 billion between mid-1997 and early 1998 — about 10% of their combined GDP** (Radelet-Sachs,
independently verified this pass). Korea's IMF-led rescue was agreed **3 December 1997** at
**$58–58.4 billion** of standby financing (IMF plus World Bank, Asian Development Bank, and
bilateral creditors) — **the largest IMF rescue package in history at the time**, conditioned on
fiscal and financial austerity, high interest rates, chaebol-group dissolution/restructuring,
layoffs, and a floating exchange-rate regime; Indonesia's crisis compounded into a political
crisis (President Suharto's resignation, May 1998), the one instance in this entire cross-country
record where a capex/credit bust directly precipitated a head-of-state's fall.

**The Young/Krugman TFP debate, in one paragraph.** Paul Krugman's 1994 "The Myth of the Asian
Miracle" argued — building directly on Alwyn Young's earlier empirical growth-accounting work —
that East Asian growth had been overwhelmingly **input-driven** (capital and labor accumulation)
rather than productivity-driven, an explicit echo of the Soviet growth experience. Young's own
estimates, independently verified this pass: total factor productivity growth of **2.3%/year
(Hong Kong), −0.3%/year (Singapore), 1.6%/year (Korea), and 1.9%/year (Taiwan)** — modest to
negative TFP contributions underneath headline growth rates of 6–9%/year. The debate matters to
L11 directly: it is the strongest available academic argument that a *sustained, high investment
rate alone* — exactly the metric case 2's own GFCF/GDP arc tracks for India — is not, by itself,
evidence of durable, self-sustaining growth; capital can be accumulated well past the point
where its marginal product still justifies the accumulation, and the 1997 crisis is the
mechanism by which that overhang was eventually forced into the open.

**Repair lengths.** Korea's macro recovery was comparatively fast — a return to growth by 1999
`[VERIFY: precise 1999 GDP growth print]` — but banking-sector NPA cleanup and corporate
restructuring (the *chaebol* debt-equity unwind specifically) ran considerably longer, on the
order of **5–7 years** `[VERIFY]`. Thailand and especially Indonesia repaired more slowly, with
Indonesia's political transition adding a further, non-economic repair dimension no other case
in this record carries. **L11 lesson.** The mirror's clearest contribution is *negative*: it
argues for why none of India's own three completed booms produced an Asian-crisis-style
currency-collapse leg — India's capex has been financed in domestic-currency bank credit and
domestic equity throughout, never at the short-term unhedged FX-debt scale this mirror's crisis
mechanism required. This is a structural difference in funding channel, not evidence that Indian
capex busts are milder — cases 1 and 3 show they are not — only that they resolve through a
different, slower, domestic-currency-denominated channel (CDR/SICA/IBC) rather than a fast,
currency-triggered one.

### 6. China 2009–2015 — the state-directed capex wave and what it does differently

**The stimulus.** Premier Wen Jiabao's government announced a **RMB 4 trillion (~$585 billion)
stimulus program in November 2008**, explicitly targeting 8% GDP growth for 2009; **81% (RMB
3.25 trillion) went to infrastructure**, consuming enormous quantities of steel, nonferrous
metals, and cement. The financing channel was **state-directed bank lending and local-government
financing vehicles (LGFVs)**, not market capital — the single largest structural difference from
every case in this record so far: local-government debt rose from **RMB 5.6 trillion (2008) to
RMB 10.7 trillion (2012)**.

**SOE overcapacity, precisely measured by 2015.** By 2015, six industries were operating under
severe overcapacity: **steel at 67% utilization, coal at 64.9%, cement at 73.8%, flat glass at
68.0%, electrolytic aluminum at 75.4%, and shipbuilding at 69%** — steel production alone
exceeded demand by **roughly 200 million tonnes annually** by that year. These utilization
figures sit meaningfully *below* even India's own 2011–2020 "capex winter" OBICUS range
(roughly 65–75%, per dossier 08's own recollection-level figures), a useful cross-check on how
severe an administratively-driven overbuild can get relative to a market-cycle-driven one.

**Supply-side structural reform, 2016–17.** Xi Jinping proposed strengthening "supply-side
structural reform" in 2015, formalized through 2016–17 with five explicit tasks: cut
overcapacity, reduce inventory, deleverage, lower costs, and address weak areas. China cut
**115 million tonnes of steel capacity and over 400 million tonnes of coal capacity across
2016–2017 combined**; 2016 alone accounted for **65 million tonnes of outdated steel capacity**
and **290+ million tonnes of coal capacity**, with **700,000 laid-off workers retrained or
re-employed** the same year. This is the same administrative-mandate tool this Part's case 3
already flags as structurally similar to the (judicially invalidated) RBI Feb-2018 circular and
to Japan's 1990 MOF quantity controls (fincycle monograph) — and, later, to China's own 2020
"three red lines" property-sector deleveraging mandate (also fincycle monograph) — a recurring
pattern of governments reaching for direct capacity/lending caps once market-based signals have
been judged too slow or too politically costly to rely on.

**What a state-directed capex cycle does differently.** Three things distinguish this mirror
sharply from every India case above: (i) the **financing channel** is administratively directed
bank credit and LGFV debt rather than market capital, so market-based early-warning signals
(bond spreads, equity drawdowns, currency pressure) are systematically muted — the same
observation the fincycle monograph's own China property case (§7) makes for the 2021+ real-estate
unwind; (ii) the **capacity-cut response** is itself administratively mandated on a multi-year
government-plan timetable rather than a market-clearing bankruptcy/restructuring process, so
"repair" here means a *policy-paced* reduction rather than the demand-and-supply-driven repair
this record's other cases document; (iii) precisely because of (i) and (ii), China supplies **no
usable analogue for L11's own construction** (OBICUS/IIP-capgoods/GFCF are all market-economy
capacity-signal proxies with no reliable Chinese equivalent this desk can access free) — China's
relevance to this book runs entirely through the **global financial cycle / China credit impulse
channel (L9, candidate H54)**, never through L11 itself.

### 7. US shale 2010–2020 — the fastest private capex cycle on record

**The boom and its first bust, 2010–2016.** US shale capital spending accelerated sharply from
2010, peaking in **2014**; as oil prices fell from **$93/barrel (2014) to $43/barrel (2016)**,
the industry slashed capex just as sharply, with **nearly 300 shale-focused companies filing for
bankruptcy from 2016 onward**. The underlying business-model problem, stated plainly in
contemporary industry commentary: operators were spending roughly **two dollars for every dollar
of cash brought in**, prioritizing production growth over free cash flow — precisely the
overinvestment dynamic this record's other cases (Asian Tigers, China) also document, but
compressed here into a **two-year bust** rather than a multi-year one.

**The 2020 collapse, the sharpest single-year capex contraction in this record.** COVID demand
destruction drove the US oil-rig count from **847 rigs (July 2019) to 225 (July 2020) — an 85%
collapse — bottoming at 172 rigs in August 2020**. Oil prices fell from **$60/barrel (December
2019) to $17/barrel (April 2020)**, briefly trading **negative** on the futures market the same
month. US crude production fell from a peak of nearly **13 million barrels/day (November 2019)**
to average **11.3 million b/d across 2020**. Shale operators reinvested **less than 50% of cash
flow into new drilling in 2020** — an explicit shift into "maintenance capex" mode.

**Capital discipline, 2021+.** Rather than re-accelerating capex once prices recovered, the
industry structurally shifted toward maximizing free cash flow over production growth: **global
upstream oil-and-gas capex reached only ~$514 billion in 2022** — despite the demand recovery and
the Russia-Ukraine war's energy-price shock — **still roughly $70 billion below the 2011 peak**,
the clearest evidence in this entire monograph that a capital-markets-enforced discipline regime,
once adopted, can persist through a subsequent price upcycle rather than reverting to the old
growth-at-all-costs pattern.

**Why repair was fast, and why that speed does not transfer to India.** Three structural features
distinguish shale from every case above and explain the gap between its ~12–18-month repair
cadence and India's own multi-year-to-decade one: (i) **asset short-cyclicality** — a shale well's
production decline curve is steep (front-loaded output, rapid payback, typically well under two
years), so a capex cut translates into a supply response within quarters, not years, unlike a
UMPP-scale power plant or a multi-hundred-kilometre highway corridor with a multi-year
construction gestation regardless of financing availability; (ii) **no land-acquisition,
environmental-clearance, or fuel-linkage gestation lag comparable to Indian infrastructure** —
US shale drilling permits and private mineral-rights leasing move on a timescale of months, not
the multi-year land/clearance chronology case 3 documents for Indian coal-linked power; (iii)
**market, not administrative, capital discipline** — high-yield bond and public-equity investors
directly repriced growth-over-returns shale operators' cost of capital after 2014–16, forcing
discipline through the price of capital itself, whereas India's captive PSU-bank-dominated
lending system kept extending and restructuring credit (CDR→5:25→SDR→S4A) through most of the
2011–2020 decade without ever forcing an equivalent capital-markets repricing on the borrowers
themselves. **L11 lesson, the mirror's single most important contribution.** L11's own 36–60
month τ½ prior (ladder.yaml) is not a property of "capex cycles" as a category — it is calibrated
specifically to **India's own gestation-heavy asset mix** (power plants, highways, steel mills,
telecom towers), and this mirror proves that mix, not the "capex cycle" label, is what determines
repair speed: a hypothetical short-cycle, low-gestation Indian capex signal (there is none at
scale today) would need a materially shorter τ½ than L11's own India-calibrated prior, and this
desk should never import a shale-style "fast repair" expectation into any India-specific capex
read.

---

## B4. Synthesis

### The table

| Episode | Boom length | Funding channel | Repair length | What L11's three legs would have shown | Verdict, 10–15y/n≈2–3 framing |
|---|---|---|---|---|---|
| **India 1994–97→2002** | ~3y (1994–97 primary-market mania) | Public equity (IPO mania, premium-issue share 1.4%→46%) + bank project finance | ~5y to 2002 (GNPA 19%→12% by 2001); BIFR backlog cleared for another decade-plus | Pre-OBICUS/pre-IIP-2011-base era — **no usable free real-side series exists**; only GFCF/GDP and GNPA proxy the whole episode | Full round trip ≈8y (1994–2002) — **shorter** than the Atlas's 10–15y band, and the desk's own best instrument (OBICUS) cannot see it at all |
| **India 2003–2011** | ~5–6y to the 2007–08 peak, extended to 2011 by the fiscal-stimulus "last leg" | Public/QIP equity (2007 power IPOs, Reliance Power the top-tick), infra project debt, SEZ land, spectrum-subsidized telecom capex | N/A (this *is* the boom leg; 2008 was a 1-year interruption, not the repair) | **OBICUS all-time high 83.2%, March 2011** — the cleanest late-cycle utilization peak this desk has recorded anywhere in the atlas | The record's single cleanest full-amplitude boom — but note it does not cleanly separate from case 3 below; the two together span 2003–2020 |
| **India 2011–2020** | N/A — this episode *is* case 2's repair leg | (repair of case 2's funding) | **9y** (2011 OBICUS/GFCF peak → 2020 COVID trough); IN2's own pooled median is 4y (IQR 1–12y) — India sits toward the long end | OBICUS 83.2%→47.3% (COVID trough); GFCF/GDP ~34–35%→~28–29%; BHEL order book −7.3% YoY by Dec 2012; power-sector resolution still incomplete 5+ years after 2018 referral | The best-measured leg in the whole record — directly validates L11's 36–60mo τ½ as a **floor, not a ceiling** |
| **India 2021–2026** | 5y so far, ongoing, unresolved arc-vs-plateau | Central capex budget (₹4.12→₹11.21 lakh cr, FY21→FY26) + PLI (₹1.97 lakh cr outlay) + reviving private capex on cleaned balance sheets (GNPA 11.2%→2.15%) | N/A — boom phase, outcome undetermined | OBICUS 75–78% band (2024–26), oscillating at the practitioner "switches on" heuristic, not yet breaking to a new percentile regime; GFCF/GDP recovering toward ~31–33%, not yet back to the 34–36% 2007–08 peak | **Genuinely open** — and IN3's own non-monotonic quintile result is exactly why the clamp means the desk does not need to close it |
| **Mirror: Asian Tigers 1990s** | ~10y (1986–96) | Bank-intermediated + **short-term unhedged FX debt** (the fault line India never carried) | Korea macro-fast (~1999 growth resumption); banking/chaebol cleanup slower, ~5–7y `[VERIFY]`; Indonesia slowest, complicated by 1998 political transition | N/A (mirror only) | Argues India's booms never carried the FX-mismatch mechanism that made this crisis fast and currency-driven — a funding-channel difference, not a severity difference |
| **Mirror: China 2009–2015** | ~7y stimulus-fueled (2009–15), arguably to 2021 pre-property-bust | **State-directed bank credit + LGFV debt** — not market capital | Formal SSSR program ~2y (2016–17); underlying overcapacity/debt overhang arguably still unwinding into the 2020s (fincycle monograph's own China property case) | N/A (mirror only; no free market-based Chinese proxy exists for L11's own construction) | Argues capex-cycle repair speed under administrative direction is policy-paced, not market-paced — no transferable τ½ for L11 |
| **Mirror: US shale 2010–2020** | ~4–5y per leg (2010–14; 2017–19), genuinely short-cycle and repeating | High-yield corporate debt + public equity, continuously market-repriced | **~12–18 months per bust** — 2014–16 bust resolved by 2017; 2020 rig-count trough (Aug 2020) to discipline-era normalization by 2021–22 | N/A (mirror only) | The counterexample proving L11's long τ½ is **asset-mix-specific, not category-specific** — short-cycle, low-gestation capital repairs in quarters; India's gestation-heavy mix does not |

### The verdict on the Atlas's own "10–15y; n≈2–3" framing, stated honestly

Tested directly against the four India cases above, the Atlas's own row-1.6 framing survives in
spirit but not at face value. **On "n≈2–3":** the case record supports three named windows
(1994–2002, 2003–2020, 2021+) plus this Part's own addition of an even earlier partial instance —
but only the middle window (2003–2011 boom feeding directly into 2011–2020 repair) is measured
by more than one free real-side proxy across its *entire* length; case 1 predates every one of
this desk's usable capex series, and case 4 is incomplete by definition. On strict clock-test
terms (CONTRACT §4: ≥4 observed complete periods to earn even Tier-B "cycle" status), this record
delivers **at most one fully measured complete cycle** (2003→2020, boom-to-repair) plus two
partial or historically-thin analogues — which is *more conservative* than the Atlas's own n≈2–3,
not less, and directly explains why ladder.yaml already carries L11 at **Tier C**, not Tier B.
**On "10–15y":** the label fits a *single leg* (case 2's boom ran 5–6y; case 3's repair ran 9y,
each individually inside or near the stated band) but badly undercounts a *full* boom-to-repair
cycle measured start-to-finish — 2003 to 2020 is **17 years**, and even a narrower peak-to-peak
reading (OBICUS's own March-2011 high to whatever future print eventually re-tests it) is still
running past a decade and a half with no completed re-test as of this writing. The Atlas's
"10–15y" is best read as describing the *repair* leg alone (case 3's 9 years sits comfortably
inside it, with room to spare against IN2's own pooled 4y median-but-12y-IQR-upper-tail), not the
full cycle — and this Part recommends the next revision of `docs/CYCLE_ATLAS.md` row 1.6 make
that distinction explicit rather than quoting one span number for two different things. None of
this changes L11's design: a Tier-C, reduce-only, non-positive-clamped seat inside the shared
macro-credit-block budget was already the correct construction before this case record was
written, and every case above — the pre-OBICUS blind spot in case 1, the textbook late-cycle
peak in case 2, the nine-year repair in case 3, the unresolved arc-vs-plateau question in case 4,
and all three mirrors' confirmation that repair speed is asset-mix-specific rather than
category-specific — argues for keeping it exactly where it already sits, never for promoting it.

---

## References

RBI, Corporate Debt Restructuring (CDR) Mechanism guidelines, 23 August 2001. · Sick Industrial
Companies (Special Provisions) Act, 1985; BIFR registration/resolution statistics (various
compilations). · National Highways Authority of India, *About NHDP*; PIB releases on NHDP phase
approvals (2006–2008). · Government of India, Ministry of Power, *Ultra Mega Power Projects*
status notes; Central Electricity Authority, UMPP status reports. · Reliance Power Ltd., IPO
prospectus and listing-day trading data (11 February 2008); contemporary financial press (Forbes,
Bloomberg, Moneylife) on the IPO and its listing crash. · SEZ India (Ministry of Commerce and
Industry), Board of Approval agenda documents; ISID working papers on SEZ location and land
utilisation. · RBI, Strategic Debt Restructuring Scheme circular (8 June 2015); RBI, 5:25 scheme
circular (December 2014); RBI, Scheme for Sustainable Structuring of Stressed Assets (S4A)
circular (13 June 2016); RBI circular RBI/2017-18/131 (12 February 2018) and *Dharani Sugars and
Chemicals Ltd. v. Union of India* (Supreme Court of India, 2 April 2019). · Insolvency and
Bankruptcy Code, 2016; IBBI media coverage on the 12-large-accounts cohort and Essar
Steel/Bhushan Power & Steel resolutions. · Ministry of Power stressed-asset classification (March
2018); IEEFA, *NPAs in the Indian power sector and strategies for resolving them*. · RBI,
*Financial Stability Report* (various issues, GNPA trend); PIB press release on GNPA reaching
2.15% (September 2025). · RBI, Order Books, Inventories and Capacity Utilisation Survey (OBICUS),
quarterly since 2008; CEIC/Mirrority OBICUS series compilations. · Union Budget documents, FY21–
FY27 (capital expenditure allocations); PIB and IBEF coverage of PLI scheme outlays and cumulative
performance. · CMIE, CapEx database (paid source; cited only via secondary public reporting of
specific figures, each flagged). · Radelet & Sachs (1998), "The East Asian Financial Crisis:
Diagnosis, Remedies, Prospects," *Brookings Papers on Economic Activity*. · Krugman, P. (1994),
"The Myth of the Asian Miracle," *Foreign Affairs*; Young, A., underlying TFP growth-accounting
estimates (Hong Kong, Singapore, Korea, Taiwan). · Government of China, State Council reports on
the 2008–09 stimulus and 2016–17 supply-side structural reform; IMF Working Paper 18/216, "China's
Capacity Reduction Reform and Its Impact on Producer Prices." · Dallas Fed, *Oil and gas industry
shows discipline on capex, but risks remain* (2025); World Bank, *What triggered the oil price
plunge of 2014–2016*; contemporary reporting on the April 2020 negative-oil-price episode and the
2020 US shale rig-count collapse. · `research/CONTRACT.md`; `docs/CYCLE_ATLAS.md` row 1.6;
`config/ladder.yaml` (`L11_capex_cycle` entry); `research/dossiers/08-india-mid-cycles.md`
(house style; free-data-triad framing; CMIE paid-source flag); `research/cycles/capex-deep/
capex-RESULTS.md` (IN1–IN3 pre-registered analogue trials, cited directly throughout);
`research/cycles/credit-deep/partB-cross-country.md` (case #10, India 2003–2018 — credit-side
mechanics cross-referenced, never duplicated); `research/cycles/fincycle-deep/partB-cases.md`
(§B3, India's property-cycle record — cross-referenced, never duplicated; house style for this
series).
