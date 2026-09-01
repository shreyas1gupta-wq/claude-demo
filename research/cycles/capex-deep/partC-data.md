# Part C — Data engineering: measuring India's capex cycle, free (L11)

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)
v1.0 · 2026-09-01

Extends `docs/CYCLE_ATLAS.md` row 1.6 (infrastructure/capex supercycle, "10–15y; n≈2–3 (2003–08,
drought 2011–20, 2021+)... OBICUS utilization percentile, IIP capital goods, GFCF/GDP (post-2026
rebase splice!)... **REGIME (clamped reduce-only)** → L11 inside macro block; **C→B via
analogues**") and `config/ladder.yaml`'s already-seated `L11_capex_cycle` entry (`tier: C`,
`reduce_only: true`, `contribution_clamp: non_positive`, `block: macro_credit_block`,
`inputs: [L10_credit_block]`, `indicator: "RBI OBICUS, MOSPI IIP + GFCF"`). Consumes
`research/CONTRACT.md` §3 (free-source mandate), §4 (Tier-C reduce-only), §6 (no magic numbers),
§8 (Hamilton filter only, never HP), Known Prior #11 (no live network access from this container;
ingestion runs on the principal's machine, every indicator resolves against a committed fixture).
**This Part is the India-official-series data-engineering companion to `research/cycles/capex-deep/
capex-RESULTS.md`** (the JST-panel analogue trials IN1–IN3, already run and reported) — those
results and their interpretation are not restated here; this Part answers a different question
("how does the desk build L11 from India's own free data") and the two meet only at the
`contribution_clamp` design the analogue trials' IN3 already informs (§C.6 inherits that finding,
does not re-derive it). Structure follows `research/cycles/commodity-deep/partC-data.md` (the style
bar this Part matches: per-source sections, exact series names, cadence/lag, break registry,
PIT-hazard table, pipeline, runsheet addendum). **Scope discipline, stated first**: RBI's Sectoral
Deployment of Bank Credit (including its "Industry"/"Infrastructure" sub-lines), WPI, and RBI's
Balance of Payments are built in full elsewhere — `research/cycles/credit-deep/partC-data.md` §C.1/
§C.5 (sectoral deployment), `research/cycles/commodity-deep/partC-data.md` §C.3 (WPI) and §C.4
(BoP) — and are consumed here only as named cross-checks, never rebuilt. Cement (ICI), IIP
Infrastructure/Construction Goods, and finished-steel consumption (JPC) are already vaulted as L12
Tier-C supply-side confirms in `research/cycles/fincycle-deep/partC-data.md` §C.4; this Part points
to that construction rather than duplicating it. Checked by web search this pass (snippet-level,
cross-checked across ≥2 results where feasible; nothing fetched directly, per Known Prior #11).
Anything not so corroborated carries **[VERIFY]**.

---

## C.1 OBICUS — the utilization leg

**What it is.** The Order Books, Inventories and Capacity Utilisation Survey (OBICUS), run by RBI's
Department of Statistics and Information Management (DSIM), is a quarterly survey of manufacturing
companies collecting new orders received, opening/pending order backlog, finished-goods/work-in-
progress/raw-material inventory levels, and item-wise production quantity/value **against installed
capacity** — the last of these is the source of the headline "capacity utilisation" (CU) print RBI
folds into its monetary-policy commentary. Primary confirmed page:
`rbi.org.in/Scripts/QuarterlyPublications.aspx?head=Quarterly+Order+Books,+Inventories+and+Capacity+
Utilisation+Survey` (per-round PDF/press release); the modern DBIE bulk-query path for a queryable
CU time series is `data.rbi.org.in/DBIE/` under Statistics → Surveys — **[VERIFY]** the exact table
name/ID, not independently pinned down this pass (A-catalog's own G9 entry carries the identical
flag; inherited, not resolved here). Third-party aggregators (CEIC) mirror the series but are a
paid service, not the free primary source.

**History.** The survey was launched in **2008** and has run quarterly since; search evidence this
pass (a CU series "averaging 74.6% from Jun 2008 to Dec 2025, 71 observations," and RBI's own
"71st round... Q2:2025-26 (Jul–Sep 2025)" framing) is internally consistent with a **Q1 2008-09
(Apr–Jun 2008) launch** — 70 quarters between round 1 and round 71 is 17.5 years, which lands
almost exactly on Q2 FY2025-26. **[VERIFY]** the exact first reference quarter; the task brief's
own "Q1 2008-09" figure is consistent with, but not independently confirmed against, a primary RBI
statement this pass.

**Sample and the response-rate caveat.** RBI's own survey description covers **over 2,500** public
and private manufacturing companies in the sampling frame [VERIFY — search-derived, not confirmed
against a primary RBI methodology note this pass]. The desk's own working figure of **~750
responding companies** per round (per the task brief, tracing to the Atlas's own citation) is best
read as the *responding* panel, not the frame — a large gap between frame and response is exactly
what a voluntary survey produces, and it matters for more than sample-size arithmetic: **response is
almost certainly not missing at random**. A firm mid-distress is a worse responder than a firm
mid-boom, so a downturn quarter's CU print plausibly carries a mild *upward* self-selection bias at
precisely the moment the state variable most needs to read low — a caveat to log against the state,
not something a percentile transform fixes. **[VERIFY]** the exact current per-round responding N;
RBI's own round announcements do not always headline it.

**Seasonality — the Q4 spike, unadjusted.** OBICUS is published **not seasonally adjusted**. India's
fiscal Q4 (Jan–Mar) carries a well-known mechanical order-book/utilisation push — year-end capital-
budget spending, dealer/distributor stocking ahead of the fiscal close, and calendar-quarter demand
patterns in several manufacturing sub-sectors — so a naive quarter-over-quarter CU comparison is
contaminated by *which fiscal quarter* a reading falls in, not only by genuine cycle position.
**[VERIFY]** the exact magnitude of the Q4 effect; not independently quantified this pass, but its
existence is widely enough referenced in Indian macro commentary that the construction rule below
(§C.6) treats it as a design requirement, not a hypothesis to re-test. This is precisely the sort of
break a fixed threshold would launder silently — another argument, alongside Contract §6's general
rule, for ranking the series rather than reading any single quarter's level.

**Level vs. percentile — is 75% "high"?** The most recent reported reading this pass is **75.6%
(quarter ending Dec 2025)**, against a **2008–2025 historical average of ~74.6%** [VERIFY, both
figures search-derived, CEIC-mirror confidence]. Read as a level, 75% sounds high in absolute terms
— "three-quarters of installed capacity in use" — but read against the series' *own* history it sits
barely above the long-run mean, nowhere near either tail. This is the Atlas's own point stated in
data: **"high" is a percentile statement, never a level statement**, and it is the direct,
concrete argument for why L11's OBICUS leg must be built as an `expanding_percentile` rank (§C.6),
never compared to a fixed CU threshold (a "75% = overheating" rule would be exactly the kind of
magic number Contract §6 bans, and this single data point shows why: 75% is unremarkable against
2008–2025 history).

**Publication lag.** ~1 quarter after the reference quarter, timed to land alongside — and feed
into the commentary of — RBI's Monetary Policy Committee resolutions; OBICUS results are routinely
cited in the MPC's own "state of the economy" framing. This is a genuine construction convenience
(the release calendar is public and stable) but also a genuine construction hazard: an OBICUS print
released the same week as an MPC decision can be hard to disentangle, in press coverage, from the
MPC's own framing of it — the raw survey numbers, not RBI's narrative gloss on them, are what §C.6's
pipeline consumes.

---

## C.2 IIP capital goods + related use-based legs

**Source and structure.** MoSPI's Index of Industrial Production (IIP), current base **2011-12**
(launched **2017-05-12**, per the search-confirmed MoSPI IIP manual), classifies output by
**use-based category**: Primary Goods (**34.05%** weight), Capital Goods (**8.22%**), Intermediate
Goods (17.22%), Infrastructure/Construction Goods (**12.34%**), and Consumer Goods split into
durables (~12.84%) and non-durables (~12.83%) [VERIFY exact current-base weights; search-derived,
order-of-magnitude confidence, not independently reconciled against a primary MoSPI weight table
this pass]. Infrastructure/Construction Goods was **added as a distinct use-based category from the
2011-12 base** (the earlier 2004-05-base series did not carry it as a separate head) — Atlas 1.6's
own parenthetical ("added in 2011-12 base") is confirmed by this base-year structure, not merely
asserted. Portal: `esankhyiki.mospi.gov.in/macroindicators?product=iip` (confirmed live path per
A-catalog H3) and `mospi.gov.in/iip`.

**Base-year history and the live 2026 break.** IIP's base year has been revised repeatedly — 1946,
1951, 1956, 1960, 1970, 1980-81, **1993-94** (introduced 1998-05-27, 543 items), **2004-05** (682
items, broader coverage including mobile phones), **2011-12** (launched 2017-05-12) — a revision
roughly every 5–7 years by design (UNSD recommends every five). **The next break is not "coming" —
it has already happened**: MoSPI's new IIP series, **base year 2022-23**, became effective from the
**2026-06-01** release (per PIB's own "FIRST PRESS RELEASE OF ALL INDIA INDEX OF INDUSTRIAL
PRODUCTION OF NEW SERIES WITH BASE YEAR 2022-23," and MoSPI's own May-2026 embargo advisory), i.e.
**three months before this chapter's own writing date**. Atlas 1.6's "post-2026 rebase splice!"
flag is therefore live *now*, not a future risk to plan for: any capital-goods or infra/construction
series a builder pulls today already needs the **base-2011-12 (legacy) and base-2022-23 (new) series
kept distinct**, spliced by the same ratio-at-overlap discipline this program uses everywhere else
(never fit a trend through the break) — [VERIFY] the exact overlap window MoSPI's new release
exposes for a clean splice point. **[VERIFY]** whether the new base changed the use-based category
weights materially (a rebase this large plausibly does) — not independently confirmed this pass.

**Capital goods' notorious volatility.** MoSPI's own IIP manual documents a structural reason
capital-goods prints swing hard month to month: many capital-goods items have production spans
**longer than one month**, so the series captures them on a **"work-in-progress" basis** specifically
to manage this — an acknowledgment, in the methodology itself, that capital goods is a lumpy,
concentrated basket. Item selection is done at the 3-digit NIC-2008 level from ASI data, covering
**≥80% of each group's output** — a relatively narrow set of large items/firms can dominate a given
month's print. The popular-press shorthand the task brief itself invokes ("rubber insulated cable
era problems" — a single large, irregularly-timed order swinging the y-o-y capital-goods number)
**[VERIFY — the specific item is not independently confirmed this pass]** is exactly the kind of
single-print artifact this structural fact predicts; the design implication is unambiguous and does
not depend on confirming the specific anecdote: **L11 must never react to one month's print** —
only the Hamilton-filtered, expanding-percentile-ranked series (§C.6), which is precisely the
discipline that turns a lumpy, single-item-dominated index into a usable cycle read.

**Infrastructure/Construction goods and Primary goods — pointer, not rebuild.** The
Infrastructure/Construction Goods leg (cement-, steel-, and construction-materials-linked items,
**12.34%** of the 2011-12-base index) is already built as an L12 Tier-C supply-side confirm in
`fincycle-deep` §C.4, alongside cement's own ICI index and JPC finished-steel consumption — that
construction is not duplicated here. L11 is a different consumer of largely the same underlying
physical reality: where L12 reads construction-goods output as a *supply-lag* signal (how fast new
housing/commercial stock can be built), L11's own role (per `ladder.yaml`, "sector-level tilt
confirmation only") would read the same series as an *investment-heat* signal — the design should
draw the identical fincycle-deep-vaulted series for this purpose rather than standing up a second,
parallel construction-materials percentile inside L11 (the §4.2 de-duplication rule, applied one
level down). Primary Goods (34.05% weight — mining, electricity, basic-materials output) is the
IIP's largest category but is a general activity/nowcast series, not a capex-specific one; Atlas 1.6
lists it among the row's source names but it plays no distinct construction role in L11 beyond
general macro context already captured elsewhere (business-cycle nowcasting, Atlas 2.3) — noted for
completeness, not built as a fourth leg.

**Cadence, lag, revision.** Monthly, released **~6 weeks** after the reference month (A-catalog H3).
Standard IIP practice publishes a **Quick Estimate** that is subsequently **revised** (typically at
+1 and +2 months, converging toward a "final" figure) — treat every single-month pull as provisional
until at least two later releases confirm it, the same discipline this program applies to every
other MoSPI/RBI series with a first/final revision cycle.

---

## C.3 GFCF — the share leg

**Source and structure.** MoSPI's National Accounts Statistics (NAS) publishes Gross Fixed Capital
Formation two ways relevant to L11: (i) **quarterly current & constant-price GFCF** as part of the
expenditure-side GDP release (`esankhyiki.mospi.gov.in`, ~2-month lag, matching the general quarterly
GDP release cadence), and (ii) **annual GFCF by institutional sector** — Public non-financial
corporations, Private corporate sector, Household sector (including unincorporated enterprises and
NPISH), and General government — published in the annual NAS volume and the dedicated GFCF data page
(`mospi.gov.in/gross-capital-formation-gross-fixed-capital-formation-net-capital-stock-economic-
activity-current`, per A-catalog H4). **This institutional-sector split is the object the task
brief's own "~18-month lag" figure names** — [VERIFY exact lag; this pass's own search corroborates
only an older "~10-month" figure from a 2014 MoSPI publication note, not independently reconciled
with 18 months — budget confirming the *current* lag as a first-live-pull task, and treat the split
as arriving materially later than the quarterly aggregate GFCF figure regardless of the exact number].

**The 2011-12→2022-23 base — live now, not "post-2026."** GDP/GFCF's base-2022-23 series (replacing
base-2011-12) was released via MoSPI's own Press Note on **2026-02-27** — the anchor rebase every
other 2026 base change (CPI, WPI, IIP) aligns to, per this program's own repeated cross-references
(A-catalog H4; `debt-deep` §C.9: "FY26 nominal GDP revised **down ~3.3%**even as real growth was
revised **up to 7.6%**"). By this chapter's own writing date, the new base is not a future event to
plan a splice around — it is the *current* reality: **Q1 FY2026-27 GFCF was already published on the
new base at 11.9% real growth**, against **Q1 FY2025-26's 5.8%** (both figures per press coverage
this pass, [VERIFY against a primary MoSPI press note]). The Atlas's "post-2026 rebase splice!" flag
is triggered *today*: any GFCF pull for this project needs both base-2011-12 (legacy) and base-2022-23
(new) series kept distinct, spliced by the same ratio-at-overlap discipline used throughout this
program, never fit through as one continuous line.

**Back-series controversy — a PIT-hazard precedent, not a one-off.** The 2011-12 base itself (adopted
2015, replacing 2004-05) came bundled with a **methodology change**, not merely a reweighting — the
CSO began using the MCA-21 corporate database as an input, and the resulting GDP jump for 2013-14
(old methodology ~5.0% growth vs. new methodology ~6.4%) drew sustained, cross-ideological
skepticism, partly because GDP growth on the new series often diverged from other activity proxies
(industrial credit growth, two-wheeler sales) that commentators expected to track it. The
controversy did not end with the rebase: a **National Statistical Commission-appointed committee
released a "back-series" in November 2018** recomputing pre-2011-12 GDP on the new methodology,
revising UPA-era growth rates *downward* — a release contested partly on procedural grounds (it was
a committee output, not a standard CSO release) [VERIFY exact committee composition and sequence;
press-coverage confidence, not primary-document confidence, this pass]. **The design lesson for L11
is explicit and generalizable**: a GFCF/GDP back-series revision in India has historically been a
*politically* contested event, not merely a technical footnote — this program's own discipline
(keep every vintage, never silently adopt a single "official" retrospective series, annotate every
splice inline) is not excess caution here; it is the minimum response to a documented precedent, and
the 2022-23 rebase should be assumed capable of producing a comparably contested back-series before
one is confirmed either way.

**The institutional-sector split — why it matters for "private capex revival" claims.** Aggregate
GFCF/GDP looked healthy in recent readings (**~30.5% in H1 FY26**, per press coverage this pass,
[VERIFY]) — comfortably inside the range Indian macro commentary treats as "healthy" (commonly cited
as >30%). But the *institutional-sector split* tells a materially different story: the **private
corporate sector's share of total GFCF fell to a decade-low of ~33% in FY24**, while **public capex
has roughly tripled since FY20** under PM GatiShakti / the National Infrastructure Pipeline / PLI-
linked outlays [VERIFY both figures; press-coverage confidence this pass]. A rising GFCF/GDP headline
can therefore coexist with continued private-sector capex weakness if it is being carried by
government spending — which is exactly why L11's other two legs matter as a cross-check: OBICUS and
IIP capital goods both read **private manufacturing-sector** activity fairly directly, so a state
built only from the GFCF aggregate (without OBICUS/IIP confirmation) risks reading a public-capex-led
GFCF print as evidence of the *broad-based* capex upcycle the Atlas row is actually trying to detect.
This is a substantive argument for the three-leg design (§C.6), not merely a data-availability one.

---

## C.4 Project-pipeline proxies (free)

**RBI "Private Corporate Investment: Growth Trends" article.** RBI's Department of Economic and
Policy Research publishes an annual RBI Bulletin article on private corporate investment intentions,
constructed from the **phasing of the total cost of projects sanctioned by banks and financial
institutions during the year** — the closest free analogue this program has to CMIE CapEx's
project-tracking database, though materially coarser (aggregate sanctioned cost/count by year, not
project-level microdata). Recent editions confirmed by search this pass: **"Private Corporate
Investment: Growth in 2024-25 and Outlook for 2025-26"** (RBI Bulletin, ~August 2025), reporting
private corporate investment intentions up **~54% to ~₹2.45 lakh crore in FY2024-25**, an FY2025-26
outlook of **+21.5% to ~₹2.67 lakh crore**, and **greenfield projects at ~89% of total sanctioned
cost** [VERIFY all figures; press-coverage confidence]. A 2026-vintage edition covering FY2025-26
actuals / FY2026-27 outlook is very likely already published or imminent given this program's own
current date (2026-09-01) but was not independently pinned to an exact publication date this pass —
**[VERIFY]**. Access: RBI Bulletin archive (`rbi.org.in/scripts/BS_ViewBulletin.aspx`); **[VERIFY]**
a stable, predictable per-edition URL pattern (credit-deep §C.6 found CRISIL's default-study PDFs
follow one, ICRA's do not — RBI Bulletin articles' own pattern is unconfirmed this pass, budget
re-discovery each edition if none exists). No bulk historical file exists; this is an **annual
hand-transcription** project, the same discipline credit-deep §C.6 applies to GNPA and the CRISIL/
ICRA default studies.

**MoSPI/DPIIT infra project monitoring — stalled and overrun projects.** MoSPI's Infrastructure and
Project Monitoring Division (IPMD) tracks central-sector infrastructure projects costing **₹150
crore and above** via the Online Computerised Monitoring System (OCMS), now consolidating onto the
**PAIMANA** platform (`paimana-proj.mospi.gov.in`, confirmed live this pass; the legacy portal is
described at `ipm.mospi.gov.in/AboutUs/AboutIPMD`) [VERIFY exact migration completeness/date]. IPMD
publishes a **monthly "Flash Report on Central Sector Projects"** flagging time and cost overruns —
genuinely free, genuinely monthly, covering roughly **1,700–1,800 projects across ~17–20 central
ministries**. A July-2026 reading found in search this pass: **cumulative cost overrun of ~₹3.4 lakh
crore across 1,775 projects** (original combined sanctioned cost ~₹33.70 lakh crore, revised to
~₹37.11 lakh crore), with **road transport & highways carrying the most delayed projects (407)**,
followed by railways (114) and petroleum (86) [VERIFY all figures, press-coverage confidence]. This
is a **stock/overrun measure, not a flow** — it tells the design about *execution friction* on an
already-committed pipeline, not about new capex being initiated, so its correct L11 role is a
stalled-projects confirm/context input, never a capex-level component in its own right.

**Banks' capex-linked credit — cross-reference, no duplication.** RBI's Sectoral Deployment of Bank
Credit already carries "Industry" and "Infrastructure" sub-lines at monthly cadence, fully built and
break-annotated (the January-2019 reporting-format revision) in `credit-deep` §C.1/§C.5. L11 reads
this only as a lagging, financing-side confirm of a capex upswing already visible in OBICUS/IIP — the
same "confirm, never re-derive" discipline `commodity-deep` §C.6 applies to the China credit gap and
§C.4 applies to BoP. No new pull is proposed here.

**CGA monthly central capex — the fastest free public-capex flow in the whole catalog.** The
Controller General of Accounts (CGA), Department of Expenditure, publishes the Union government's
own monthly actuals — including a distinct **capital-expenditure line separate from revenue
expenditure** — via the interactive **"Union Government Monthly Accounts Dashboard"**
(`cga.nic.in/MonthDashboardReport/Published/list.aspx`, confirmed live this pass, interactive from
FY2015-16 onward) and the underlying ministry-wise **Monthly Report** tables
(`cga.nic.in/MonthlyReport/Published/...`), with the capital-account series itself running, per
search this pass, from **April 1997**. This is genuinely **monthly**, essentially **T+30–45 days**
— materially faster than OBICUS (quarterly, ~1-quarter lag), IIP capgoods (monthly, ~6-week lag), or
GFCF (quarterly, ~2-month lag for the aggregate; far longer for the institutional split). It is
**not one of L11's three named legs** (Atlas 1.6 names only OBICUS/IIP-capgoods/GFCF), but it is the
public-capex complement to all three — and, per §C.3's own finding that public capex is presently
doing much of the GFCF headline's work, an unusually valuable free monthly context series for
distinguishing a public-capex-led print from a broad-based one.

**State capex — CAG monthly accounts, a genuine construction cost, not a one-line pull.** Each
state's Accountant General (Accounts & Entitlement) office publishes **Monthly Civil Accounts**
covering April-to-date capital expenditure by major head, at per-state pages under the CAG portal
(confirmed pattern this pass: `cag.gov.in/ae/<state>/en/ae-state-accounts?cat=792`, e.g. Assam,
Madhya Pradesh). **No single, consolidated, all-India monthly state-capex file exists free** — this
would be a 28-state-plus-UT hand-aggregation project, each state page structured independently
[VERIFY whether page structure is consistent enough across states to script once]. CAG's own annual
**State Finances Audit Reports** (one PDF per state per year, `cag.gov.in`) are the more usable, if
far lower-frequency, free consolidated view — already the source A-catalog and `debt-deep` §C.1 draw
on for states' debt/GSDP context. Budget the monthly, all-state build as an **exploratory pilot** on
a handful of the desk's highest-priority states (§C.9 step 41), not a Phase-0 commitment.

---

## C.5 Corporate-side confirms

**Listed-company capex from disclosures — the aggregator-tier limit.** Quarterly results (Reg. 33)
and annual-report fixed-asset/capex schedules are free at source (NSE/BSE filings, company
investor-relations pages), but **no free source bulk-tabulates aggregate listed-company capex**
across the universe. Screener.in-type aggregators expose per-company capex/fixed-asset line items on
their free tier for casual, single-name lookups, but rate-limit or paywall bulk/API-scale access —
not usable as a systematic L11 input at the free tier. This is the identical gap `ingest/README.md`'s
own Addendum 2 already names for the desk's fundamentals pipeline generally (**no fundamentals
puller exists in `ingest/` at all yet**; `pull_nse_financial_results.py` is the eventual free source,
per that addendum's own plan). L11's corporate-capex confirm should ride on that pull once built,
not stand up a second, parallel fundamentals scraper here.

**BHEL/L&T order books — free, quarterly, genuinely useful thermometers.** Both companies report
explicit order-inflow and order-book figures with every quarterly result, straight from exchange
filings/company press releases — zero construction cost beyond reading the results. Search this pass
found: **L&T Q3 FY26 order inflows ~₹1.36 lakh crore, order book ~₹7.3+ lakh crore**; **BHEL FY26
order inflows ~₹75,000 crore, order book ~₹2.4 lakh crore** [VERIFY exact figures every quarter —
these are genuinely quarter-refreshed numbers, cited here as an existence proof, not a static fact].
Both are useful **qualitative** cross-checks — L&T is diversified across infra/defence/IT-services,
BHEL is power-equipment-concentrated, so each carries a different sector lens — but a
comparability problem across two structurally different, decades-spanning companies makes an
expanding-percentile construction of order-book growth an **open, unresearched question**, not a
decided design choice: use both as narrative/sanity confirms on the OBICUS/IIP/GFCF-based state
(§C.6), never as a fourth ranked leg, until that question is separately pre-registered and tested.

**Cement/steel volumes — cross-reference, no duplication.** Physical construction-materials demand
(cement ICI, JPC finished-steel consumption) is already vaulted as an L12 Tier-C supply-side confirm
in `fincycle-deep` §C.4; the *world-price*/equity-market lens on the same names (Nifty Metal sector
methodology) is built in `commodity-deep` §C.5. L11 draws on neither construction independently —
it is the same underlying physical-demand and equity-market reality those two Parts already read,
and a parallel L11-specific construction-materials percentile would violate the ladder's own
de-duplication rule (§4.2) at one remove. The design answer here is explicit non-duplication.

---

## C.6 The L11 pipeline

**Three legs, one composite, the shared machinery.** L11's construction mirrors L12's own
`financial_cycle_state` pattern (`quant/ladder/financial_cycle.py`) almost exactly, extended from two
legs to three: each leg is independently Hamilton-filtered (`quant/stats/hamilton.py`,
`mode="expanding"`, never HP) and `expanding_percentile`-ranked (`quant/ladder/credit_cycle.py`), the
three percentile ranks are converted to a signed `[-1,+1]` scale and combined as an **n_legs-aware
mean** — a date with all three legs present gets a full-confidence reading; a date with only one or
two legs present (necessarily true for most of India's history, since OBICUS starts 2008) gets a
**degraded** reading, flagged by `n_legs`, exactly as `financial_cycle_state` already flags a
short-HPI date for L12. **B-module-specs' own M16 spec already names the target function signature**:
`capex_cycle_clamped(obicus, iip_capgoods, gfcf) -> Series` — this Part's job is to specify the three
inputs that function consumes and the construction discipline around them, not to write the module.

**Warm-up arithmetic — when does each leg's own rank mature?** Reusing this program's established
convention (never inventing a new grid; commodity-deep and fincycle-deep both anchor a Band-1
monthly series at h=60 months/p=1/min_obs=48 months, treating the Contract's "≥4 observations"
Tier-B/C floor as ≈4 years scaled to the series' own cadence) and applying the same scaling logic to
L11's own faster registry tau_half prior (`[36, 60]` months, per `ladder.yaml`):

| Leg | Cadence | h, p (reused convention) | min_obs (≈4 obs, scaled) | Usable start | First trustworthy percentile |
|---|---|---|---|---|---|
| OBICUS (CU) | quarterly | 20q (5y), p=1 | 16q (4y) | 2008-Q2 | **≈2017** (2008 + 5y warm-up + 4y floor) |
| IIP capital goods | monthly | 60mo (5y), p=1 | 48mo (4y) | 2011-04 (current base only) | **≈2020** (naive, single-base window) |
| IIP capital goods | monthly | 60mo (5y), p=1 | 48mo (4y) | **~1994** (if ratio-spliced across 1993-94→2004-05→2011-12→2022-23) | **≈2003** (chained-history window) |
| GFCF/GDP | annual | 5y, p=1 | 4y | 1950-51 in principle; usable comparability **[VERIFY]** decade | mature well before this program's build (decades of runway either way) |

**GFCF matures earliest by a wide margin; OBICUS matures latest** — exactly the ordering the Atlas's
own "n_legs degradation design (GFCF longest, OBICUS shortest)" framing anticipates, now with actual
dates attached. The IIP capital-goods row shows a genuinely useful design fork: read naively (current
base only, since 2011), its own percentile does not mature until ~2020; but this program's own
established splice discipline (ratio-at-overlap chaining across all four IIP base vintages —
1993-94→2004-05→2011-12→2022-23, the same technique commodity-deep chains Jacks→IMF-PCPS→EIA) would
push its usable start back to ~1994 and its maturity to ~2003 — a materially more mature leg. This
Part **recommends** the chained approach (consistent with program practice elsewhere) but does not
build the four-vintage splice here — it is a genuine, nontrivial construction task, budgeted as
§C.9 step 36. **The exact (h, p, min_obs) triple for L11 is not yet fixed in `ladder.yaml`** (only
the `tau_half_months` prior is stored) — per Contract §6, this Part states the reused-convention
candidate above as the recommended default, not a unilateral decision; it is a pre-registration item
for the data phase, exactly as commodity-deep and fincycle-deep both flagged their own (h,p) choices
as reused-not-invented rather than silently final.

**The non_positive clamp — applied at consumption, not baked into the state.** Per the
consistency-audit's own C2 finding (`research/register/consistency-audit.md`) and its fix (now
encoded in `ladder.yaml`'s `contribution_clamp: non_positive` and enforced by `config/validator.py`),
a hot L11 reading must never *add* regime-score budget through the shared `macro_credit_block`
average — Tier-C may only reduce. **The correct place to apply that clamp is at block aggregation,
not inside L11's own state function.** Concretely: the three-leg composite above should be exposed
as a **raw signed state** in `[-1, +1]` (the exact `financial_cycle_state` pattern — no clamp inside
that function), and `capex_cycle_clamped(...)` should be a thin wrapper applying `min(0, raw)` **only
at the point `macro_credit_block` combines L6+L10+L11+L12** — the same split M16's own module spec
already implies by naming `capex_cycle_clamped` as a distinct function from whatever raw composite it
wraps. **Why this ordering matters, stated explicitly (the task's own question):** collapsing the
clamp into the state itself would make a raw reading of +0.05 (barely hot) and +0.85 (a dangerously
extended overbuild) both silently disappear to 0 the moment they are stored — correct for regime-
score purposes, but destructive for anything downstream that legitimately wants the *magnitude* of a
positive reading, not just its sign. L11's own registry role is explicitly **"sector-level tilt
confirmation"**, not only regime-score input: a rule deciding how hard to lean against cement/
capital-goods/infra sector weight (or, on the H62 capital-cycle candidate's own logic, Atlas 2.15/
13's asset-growth conditioner) needs to distinguish a mild overbuild from an extreme one, and that
distinction is only available if the raw signed state — not its clamped shadow — is what the module
stores and exposes. The clamp belongs exactly where Contract §4's rule actually binds: the one shared
regime-score aggregation point, and nowhere earlier in the pipeline.

**Splice/rebase handling.** OBICUS carries only a soft continuity caveat (panel-composition drift,
no formal base-year break). IIP capital goods and GFCF **both** crossed a hard base-year break within
the same six-month window in 2026 (IIP: 2026-06-01; GFCF/GDP: 2026-02-27) — meaning L11 is, at this
moment, the single seat inside `macro_credit_block` most directly exposed to the "2026 base-year
revision wave" this program repeatedly names, with **two of its three legs** breaking almost
simultaneously. Each leg's splice must be applied **independently, at its own overlap point** — never
a single joint correction that conflates the IIP break with the GFCF break, even though they landed
months apart in the same calendar year.

**Failure modes.** OBICUS response-rate collapse in a stress quarter (self-selection bias exactly
when the signal is most needed, §C.1); a single lumpy capital-goods print swinging a raw month-over-
month read (mitigated structurally by ranking the Hamilton-filtered series, never a raw MoM/YoY
number, §C.2); a contested GFCF back-series revision recurring at the 2022-23 rebase, echoing the
2015/2018 precedent (§C.3) — mitigated by keeping every vintage, never silently adopting the latest;
a joint multi-source stale-data risk if a MoSPI/RBI portal migration delays several releases inside
the same block at once (worth naming since L11 shares `macro_credit_block` with three other
multi-source composites, any one of which stalling degrades the shared aggregate).

**Monitor cadence.** OBICUS: quarterly (bound by its own ~1-quarter lag). IIP capital goods: monthly
(~6-week lag — nominally the freshest-refreshing leg, though, per the warm-up table above, presently
the *least* mature rank under the naive single-base window — a genuine tension between freshness and
trustworthiness worth carrying forward, not resolving by fiat). GFCF: quarterly for the aggregate
(~2-month lag), with the annual institutional-sector split treated as a slower **confirm-only**
input, never the primary ranking signal (mirroring how `commodity-deep` treats its own INR-terms
variant as downstream/secondary, never a substitute for the primary ranking). The composite should
recompute whenever any leg refreshes, with `n_legs` communicating partial updates — the exact
refresh-scheduling rule is a data-phase implementation detail this Part specifies the *inputs* for,
not the final code.

---

## C.7 Vintage/PIT hazard table

| Source | Publication lag | Revision policy | Break / date | Backtest hazard |
|---|---|---|---|---|
| RBI OBICUS | ~1 quarter | Not typically revised after release [VERIFY] | Soft panel-composition drift only; no formal base year | Voluntary-survey self-selection may bias stress-quarter readings upward (§C.1); no seasonal adjustment — Q4 spike contaminates raw QoQ reads |
| MoSPI IIP (capital goods, infra/construction) | ~6 weeks | Quick Estimate → revised (+1, +2 months) | **2011-12 → 2022-23, effective 2026-06-01** (already live); prior breaks 1993-94/2004-05/2011-12 | Any series crossing 2026-06 needs ratio-splice discipline; single-print volatility from lumpy WIP-basis items — never react to one month |
| MoSPI GFCF (aggregate, quarterly) | ~2 months | Provisional → first-revised → final, ~2-year cycle (standard NAS practice) | **2011-12 → 2022-23, effective 2026-02-27** (already live) | Splice discipline as IIP; treat every vintage as provisional until confirmed |
| MoSPI GFCF (institutional-sector split, annual) | **~10–18 months [VERIFY exact current lag]** | Same NAS revision cycle as aggregate | Same 2026-02-27 break | Confirm-only input, never primary ranking; 2015/2018 back-series precedent — assume any future back-series is contestable until independently confirmed |
| RBI "Private Corporate Investment" article | Annual (RBI Bulletin) | Not revised in the ordinary sense — a fresh edition each year | None identified | Hand-transcription-only, no bulk file; a coarse aggregate, not project-level — do not over-read precision |
| MoSPI/DPIIT IPMD Flash Report | Monthly | Cumulative overrun figures restated as projects re-report | OCMS → PAIMANA platform migration [VERIFY exact date] | Stock/overrun measure, not a flow — context only, never a capex-level input |
| CGA Monthly Accounts (capex line) | ~T+30–45 days | Actuals; not typically revised at the monthly cadence | None identified | The fastest, lowest-hazard series in this chapter — public capex only, not the whole capex cycle |
| CAG state Monthly Civil Accounts | Monthly, per-state | State-specific [VERIFY] | None identified at the series level | No consolidated free file exists; per-state page-structure consistency unconfirmed — a construction-cost hazard, not a data-quality one |
| BHEL/L&T order books | Quarterly (results date) | Not revised | None (company-level, continuous disclosure) | Two-name, structurally non-comparable thermometer — qualitative confirm only, never a ranked input |

---

## C.8 What cannot be measured free — the honest list

| Need | Why it's out of reach free | What we do instead |
|---|---|---|
| **CMIE CapEx / Prowess project-level private investment database** | Paid subscription, explicitly excluded by Contract §3 | RBI's "Private Corporate Investment: Growth Trends" article (§C.4) — an aggregate, annual, coarser substitute (sanctioned cost/count/greenfield-share, not project-level microdata); this is the design's own already-named substitute (per `docs/masterplan/A-data-catalog.md` §6's gap-list entry, "DESIGN §13 already names the substitute") |
| **Project-level (not aggregate) sanctioned-investment microdata, free** | No free Indian source publishes this at the project level; CMIE is the only known product that does, and it is paid | Aggregate RBI article + IPMD's project-level *overrun* data (which covers execution status, not new sanctioning) — a partial, not a full, substitute; project-level *initiation* microdata remains genuinely unmeasured free |
| **Under-construction vs. commissioned capacity-by-vintage cut** | No free source publishes installed capacity broken out by vintage/commissioning date at an economy-wide level | OBICUS's own CU reading is the closest free proxy, but it reads utilization of *existing* capacity, not the vintage structure behind it |
| **Bulk, free, aggregate listed-company capex/fixed-asset time series** | No free aggregator bulk-tabulates this across the universe (screener-type sources rate-limit/paywall bulk access) | Wait on the desk's own eventual `pull_nse_financial_results.py` (ingest/README.md Addendum 2) rather than building a second scraper here |
| **A single, consolidated, free, all-India monthly state-capex file** | Each state's Accountant General publishes its own Monthly Civil Accounts independently; no central aggregator exists | Pilot a handful of priority states (§C.9 step 41) before committing to a 28-state-plus-UT build; fall back to CAG's lower-frequency annual State Finances Audit Reports for a consolidated, if far slower, view |
| **A stable per-edition URL pattern for the RBI Private Corporate Investment article** | RBI Bulletin's per-article URL scheme is not confirmed stable this pass (contrast CRISIL's confirmed stable pattern, credit-deep §C.6) | Re-discover the link each year if no pattern holds, the same discipline credit-deep already applies to ICRA's ID-keyed download links |

---

## C.9 Runsheet addendum 7

Continuing the global step numbering `commodity-deep` Part C's own runsheet (`ingest/README.md`'s
own addendum 6, §C.10) established through **step 34** — no existing `ingest/pull_*.py` script
covers any of L11's three named series or its project-pipeline proxies, so this is, like every
predecessor Part C, a genuinely new fixture family.

| Order | Task | Series | Est. hours | Why this order |
|---|---|---|---|---|
| 35 | Pull RBI OBICUS: all available rounds (PDF/Excel per round from the confirmed QuarterlyPublications page); confirm the exact DBIE bulk-query table path and the current per-round responding N | §C.1 | 3–4 | The shortest, latest-maturing leg (§C.6) — start it first so its warm-up clock is running while other legs are pulled |
| 36 | Pull MoSPI IIP capital goods + infrastructure/construction goods: both base-2011-12 (legacy) and base-2022-23 (new, effective 2026-06) full history; confirm the splice overlap window; **also attempt the four-vintage ratio-splice chain (1993-94→2004-05→2011-12→2022-23)** the §C.6 warm-up arithmetic recommends, piggybacking on whatever base-year documentation the fincycle-deep IIP pull (its own runsheet step 22) already retrieves | §C.2, §C.6 | 4–6 | The chained-vs-naive maturity-date gap (2003 vs 2020, §C.6) makes this the single highest-leverage pull in this addendum |
| 37 | Pull MoSPI GFCF: quarterly current+constant (both bases) plus the annual institutional-sector-split table, full available vintage history from the NAS annual publication and the GFCF-specific data page; hand-transcribe pre-digital-portal years if the bulk export does not reach far enough back | §C.3 | 4–6 | The longest-history, earliest-maturing leg, but the institutional-sector table's own format/lag makes it the most labor-intensive single pull here |
| 38 | Pull RBI "Private Corporate Investment: Growth Trends": every available annual RBI Bulletin edition; hand-transcribe sanctioned-cost/count/greenfield-share into a time series (no bulk file exists) | §C.4 | 3–4 | Same hand-transcription discipline as GNPA/FSR/CRISIL/ICRA (credit-deep §C.6) — small, high-value, no bulk shortcut available |
| 39 | Pull MoSPI/DPIIT IPMD Flash Report on Central Sector Projects: full available monthly history from OCMS/PAIMANA; confirm whether historical months are queryable or only the latest is exposed | §C.4 | 3–4 | Confirms whether this is a genuine time series or a single current snapshot before it is relied on as a monthly context input |
| 40 | Pull CGA Monthly Accounts Dashboard + ministry-wise Monthly Report: full available history (interactive dashboard from FY2015-16; capital-account series back toward April 1997 via the archive pages); isolate the capital-expenditure line | §C.4 | 2–3 | Cheap, high-value, the fastest-refreshing public-capex series in the whole catalog — do not defer |
| 41 | Pilot CAG state Monthly Civil Accounts on 3–5 priority states (set to be confirmed against the desk's own equity sector-tilt priorities); confirm whether the per-state page structure is consistent enough to script once before committing to a full 28-state-plus-UT build | §C.4 | 5–8 | Exploratory — may legitimately not scale to all states within budget; treat as a pilot, not a Phase-0 commitment |
| 42 | Pull BHEL + L&T quarterly results (order-inflow/order-book figures): full available quarterly history from investor-relations pages/exchange filings; piggyback on whatever bulk Reg. 33 results puller the desk eventually builds (ingest/README.md Addendum 2) rather than a bespoke two-name scraper | §C.5 | 1–2 | Small, cheap, qualitative-confirm-only — low priority relative to the three ranked legs |
| 43 | `config/` registry + CI validator smoke-test against the newly-pulled L11-adjacent fixtures; confirm the three-leg `n_legs` degradation logic runs clean across the pre-2008 (OBICUS-absent) period of the combined fixture set, and that `capex_cycle_clamped` reproduces `min(0, raw)` against the raw-state fixture | §C.6 | 2–3 | Confirms the pull satisfies the "every module runs on fixtures with zero live data" gate, unchanged from every other Part C's own closing step; also the first executable check on the raw-vs-clamped split §C.6 argues for |

**Total estimated incremental effort: ~27–40 hours**, on top of A-catalog's existing ~45–60-hour
Phase-0 estimate and the other Part Cs' own already-budgeted extensions — driven mainly by step 37
(GFCF's institutional-sector split, the most format-awkward single pull) and step 36's optional but
recommended four-vintage IIP splice chain, with step 41 (state capex) carrying the widest cost range
given its explicitly exploratory, may-not-scale framing.

---

*End of Part C. Cross-references: `research/CONTRACT.md` §3 (free-source mandate), §4 (evidence
tiers, Tier-C reduce-only), §6 (no magic numbers — the (h,p,min_obs) reuse argued in §C.6), §8
(Hamilton filter only), Known Prior #11 (no live network access; principal's-machine ingestion);
`config/ladder.yaml` L11_capex_cycle (tier C, reduce_only, `contribution_clamp: non_positive`,
`block: macro_credit_block`, `inputs: [L10_credit_block]`) — no registry edit made here;
`docs/masterplan/B-module-specs.md` M16 (`capex_cycle_clamped(obicus, iip_capgoods, gfcf) -> Series`,
the target this Part specifies inputs for); `research/register/consistency-audit.md` C2 (the
non_positive-clamp finding §C.6 inherits and explains the raw/clamped split for); `research/cycles/
capex-deep/capex-RESULTS.md` and `research/register/trial-ledger.md` (the JST-panel analogue trials
IN1–IN3 — not restated here); `quant/stats/hamilton.py` (`hamilton_filter`), `quant/ladder/
credit_cycle.py` (`expanding_percentile`), `quant/ladder/financial_cycle.py`
(`financial_cycle_state` — the exact pattern this Part's three-leg composite extends); `research/
cycles/credit-deep/partC-data.md` §C.1/§C.5 (sectoral deployment — inherited, not duplicated),
§C.6 (GNPA/CRISIL/ICRA hand-transcription discipline, reused for the RBI PCI article);
`research/cycles/commodity-deep/partC-data.md` §C.3 (WPI), §C.4 (BoP), §C.6 (China-credit scope
discipline, the "confirm, never re-derive" pattern §C.4 applies to sectoral deployment) — the style
bar this Part matches; `research/cycles/fincycle-deep/partC-data.md` §C.4 (cement ICI, IIP
Infrastructure/Construction Goods, JPC steel — inherited, not duplicated); `docs/masterplan/
A-data-catalog.md` G9 (OBICUS), H3 (IIP), H4 (GFCF), §6 (the CMIE-substitute gap-list entry this
Part's §C.8 restates with sourcing); `ingest/README.md` addenda 1–6 (existing pull scripts and gaps
— sectoral deployment, WPI, and BoP already covered elsewhere, not duplicated here) and this
chapter's own addendum 7 (§C.9).*
