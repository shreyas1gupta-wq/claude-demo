# Part C — Data engineering: measuring India's property cycle, free

v1.0 · 2026-09-01 · Extends `jst-fincycle-RESULTS.md` (FC1–FC3: the combined financial-cycle state
as the mean of expanding percentiles of the credit/GDP and real-house-price Hamilton gaps, h=5y,
p=1, parameter-free per country) and `docs/masterplan/A-data-catalog.md` block **G4** — the *only*
existing catalog line touching this cycle at all (RBI HPI). This Part's job is the gap the catalog
leaves, the same first-build gap credit-deep Part C found for the NBFC layer and debt-deep Part C
found for centre/state debt stocks: **no catalog entry exists for NHB RESIDEX, housing-finance-
company (HFC) credit, RERA project registrations, stamp-duty/registration counts, or a housing-
specific construction-materials proxy** — this Part supplies all five, corrects one date A-catalog
G4 got wrong, and adds the city-expansion detail G4 did not have. Consumes `research/CONTRACT.md`
§3 (free-source mandate), §4 (evidence tiers, Tier-C reduce-only), §8 (no HP filter — Hamilton 2018
only), Known Prior #11 (no live network access here; ingestion on the principal's machine, every
indicator against a committed fixture). Feeds `config/ladder.yaml` **L12_realestate_medium_cycle**
(tier B, `reduce_only: false`, `block: macro_credit_block`, `inputs: [L10_credit_block]`). Structure
follows `research/cycles/debt-deep/partC-data.md` (the style bar this Part matches); the bank+NBFC
aggregation method follows `research/cycles/credit-deep/partC-data.md` §C.2, mirrored below to
bank+HFC. Checked by web search this pass (snippet-level, cross-checked across ≥2 results where
feasible; nothing fetched directly). Anything not so corroborated carries **[VERIFY]**.

---

## C.1 RBI House Price Index — the primary series, and the break sitting inside it right now

**Coverage, base, methodology (legacy series, 2010–2025).** The Reserve Bank compiles a quarterly
house price index (HPI, base **2010-11=100**) for **ten** major cities — Mumbai, Delhi, Chennai,
Kolkata, Bengaluru, Lucknow, Ahmedabad, Jaipur, Kanpur and Kochi. Construction is a chain-linked
stratified index built from **transaction-level data supplied by state Registration/Stamps
Departments** (actual registered sale-deed prices, not listings or valuations): for each
ward/administrative zone and quarter, properties are bucketed into three floor-space-area (FSA)
classes (small/medium/large); a simple average price per square metre is computed per class per
ward; classes are combined using weights fixed at the **base-period transaction mix (April
2010–March 2011)**; successive quarters chain-link onto the base rather than re-basing each time.
Data exists from **June 2010** (reference quarter Q1:2010-11) onward. The **all-India composite**
is a weighted average of the ten city indices, weighted by each city's **2011 Census population** —
a fixed weight, never re-estimated between Census years, a genuine if minor source of composite
drift as city populations diverge from their 2011 shares over a 15-year span.

**Publication lag.** NHB's comparably-constructed RESIDEX (§C.2) runs ~10–13 weeks; RBI's HPI is on
the faster end — Q1:2026-27 (quarter ended 2026-06-30) was released **2026-08-24**, an ~8-week lag;
earlier editions ran closer to 10–12 weeks (A-catalog G4's estimate). **[VERIFY]** any stated RBI
SLA; treat 8–13 weeks as the working range, not a point figure.

**Revision behavior — [VERIFY], a structural risk, not a confirmed fact.** The index is built from
registration-authority filings, and registration itself can lag the underlying transaction by weeks
(a statutory registration window applies) — a quarter's first print could in principle be revised
upward as late filings for that quarter are folded in. **No RBI documentation of an explicit
revision policy was found this pass**; a build script should difference successive vintages of the
same reference quarter to detect the answer empirically rather than assume either "never revised"
or "revised like GDP."

**The break sitting inside the series right now — base changed to 2022-23, coverage expanded to 18
cities, October 2025.** A-catalog G4 flagged this transition as "appearing around the Q2 FY2025-26
reporting cycle" without a confirmed date; that guess is corrected here. RBI released the HPI for
**Q1:2025-26** (reference quarter Apr–Jun 2025) on **2025-10-10**, on a **new base year (2022-23
=100)** and **expanded coverage to eighteen cities** — the original ten plus **Hyderabad,
Thiruvananthapuram, Pune, Ghaziabad, Thane, Gautam Buddha Nagar, Chandigarh and Nagpur**. A
retrospective back-series was published from Q1:2022-23, i.e., the **new-base series' own native
history starts in 2022-23**, not a backward extension of the 2010-11-base series. **This is a
genuine level break, identical in kind to NHB RESIDEX's own 2018 break (§C.2) and this monograph's
debt-deep Part C's documented 2026 CPI/GDP/IIP rebase wave** — never fit a Hamilton gap or a
percentile rank through it. Construction rule: treat the **2010-11-base, 10-city series as the long
history (2010–2025)**; treat the **2022-23-base, 18-city series as the current-vintage tail from
Q1:2025-26 forward**; splice with a ratio-at-overlap using the legacy series' last reported quarter
(`k = HPI_new(t0)/HPI_old(t0)`), the same pre-registered choice and argument credit-deep Part C
§C.3 makes for GDP base transitions. **[VERIFY]** whether the 18-city composite re-weights by a
newer population base or extends 2011 Census weights arithmetically to the eight new cities — not
confirmed either way this pass.

| Field | Legacy series (2010-25) | Current series (2025→) |
|---|---|---|
| Base | 2010-11 = 100 | 2022-23 = 100 |
| Cities | 10 | 18 (+8) |
| Native history | June 2010 → ~Q1:2025-26 | Back-series from Q1:2022-23; live from Q1:2025-26 |
| First live print under this base | (was itself new once, ~2011) | 2025-10-10, for Q1:2025-26 |
| Weighting | 2011 Census city population, fixed | **[VERIFY]** — population-base unconfirmed |

---

## C.2 NHB RESIDEX — the 2018 break, two price concepts, and current status (not discontinued)

**History.** NHB RESIDEX launched **July 2007**, base year 2007, for **five** cities (Bengaluru,
Bhopal, Delhi, Kolkata, Mumbai), gradually expanded to **26 cities**, then **stopped updating after
March 2015** (a multi-year gap, not a discontinuation announcement). It was **revamped and
relaunched in July 2017**, republished quarterly with base year **FY2012-13=100**. **The genuine
methodology break**: from the **April–June 2018 quarter**, the base shifted again, to
**FY2017-18=100** — a second rebase inside one year of relaunch, the one the task brief's "2018
methodology overhaul" names. **Current coverage: 50 cities** (18 State/UT capitals plus 37 "smart
cities," with overlap). **Status: active, not discontinued** — quarterly releases continue through
at least Q1 2026 [VERIFY exact latest print at first live pull; corroborated into 2025–2026 across
≥2 independent sources, but the most recent point value came from a single tertiary aggregator
(TradingEconomics), so treat that specific number as single-source].

**Two structurally different price concepts, not two cuts of one dataset.** RESIDEX publishes both:

| Version | Data source | What it actually measures |
|---|---|---|
| **HPI @ Assessment Prices** | Valuation data supplied by **banks and HFCs** | The price lenders assign to a property for loan-sanctioning purposes — a conservative, loan-to-value-anchored figure, not a transaction price |
| **HPI @ Market Prices** | Primary (under-construction) and secondary (resale) market listing/deal data | Closer to an actual asking/transacted price, for both new-launch and resale segments |

This is a genuinely different construction from RBI's HPI (§C.1), which is registration-price-only:
RESIDEX's assessment-price leg is a *lender's* number, not a market number, and its market-price leg
draws partly on listing data with the same asking-vs-transacted gap flagged for aggregators
generally (§C.6). **Neither RESIDEX version should be blended with RBI's HPI into one series** —
they answer different questions (bank collateral valuation vs. registered transaction price vs.
market listing/deal price) and any cross-check between them is a divergence to log, not an
inconsistency to reconcile away.

**Publication lag.** Quarter ended March 2024 → released **2024-06-11**, an ~10-week lag, in line
with RBI HPI's own range (§C.1). A **2013 ambition to move RESIDEX to a monthly cadence** was
reported at the time but the headline release remains quarterly through 2024–2026 per every source
checked this pass — **[VERIFY]** whether any individual-city sub-series ever went monthly; treat the
composite as quarterly-only until confirmed otherwise.

---

## C.3 Housing credit — the longer, faster proxy, and the bank+HFC aggregate

Both price series above are short (RBI HPI's usable native history is 15 years; RESIDEX's is
shorter still after the 2015 gap and 2018 rebase). Housing **credit** is the faster-updating,
longer-history leg the design needs to carry L12 through the years the price legs cannot cover
(§C.8's warm-up arithmetic makes this precise).

**Bank housing credit — RBI Sectoral Deployment of Bank Credit.** "Housing (Including Priority
Sector Housing)" is a named sub-line under the **Personal Loans** major head of the monthly
Sectoral Deployment release (`rbi.org.in/Scripts/Data_Sectoral_Deployment.aspx`; same filing stream
documented at A-catalog G1 and credit-deep Part C §C.1 — **not re-derived here**, only extended to
the housing-specific sub-line). Two facts this Part adds to the credit-deep base layer:

1. **Sample, not census.** Compiled from **40 select scheduled commercial banks**, ~93% of total
   non-food credit of all SCBs — a high-coverage proxy, but a proxy; the ~7% gap is unlikely
   housing-concentrated but is unquantified free of charge.
2. **The same January 2019 reporting-format break credit-deep Part C §C.1 names for the NBFC-in-
   Services sub-line applies to Housing and Commercial Real Estate too** — sub-sector definitions
   changed at that boundary; **[VERIFY]** the exact delta for Housing specifically (confirmed for
   NBFCs, not independently re-confirmed for Housing this pass).

**Commercial real estate / developer credit — the supply-side leg, same release.** "Commercial Real
Estate" is a separate named sub-line under **Services** in the same Sectoral Deployment release
(recent prints show ~16% y-o-y growth in this line) — this is the free, monthly, developer-side
credit proxy the task asks for, sourced from the identical filing as the household-side Housing
line, same publication lag (~3 weeks post month-end), same Jan-2019 format-break caveat.

**Housing Finance Companies (HFCs) — the shadow-credit leg, and a regulatory-lineage break of its
own.** HFCs were **NHB-regulated** from NHB's founding (1988) until the **Finance (No. 2) Act,
2019** amended the National Housing Bank Act; HFC regulatory power transferred to the **RBI**
effective **2019-08-09**, and HFCs are now formally classified as **one category of NBFC**. This is
a genuine data-lineage break: pre-Aug-2019 HFC prudential data flowed through NHB's own supervisory
returns; post-Aug-2019 through RBI's NBFC-HFC statistical returns — same entities, a different
regulator collecting the numbers, a documented date to flag on any HFC series crossing it. Two free
publications carry HFC aggregates:

| Source | What it carries | Cadence / lag |
|---|---|---|
| **NHB "Report on Trend and Progress of Housing in India"** | Sector-wide housing credit picture: HFC total loan portfolio, housing vs. non-housing split, PLI (Primary Lending Institution) performance, individual-housing-loans-outstanding aggregate (banks + HFCs combined) | Annual, released with a long lag — the FY2024-25 edition was hosted under a 2026-02 upload path, i.e., roughly an **11-month-plus lag** past FY-end (March) |
| **RBI Financial Stability Report, NBFC chapter** | HFCs as a sub-category of the NBFC sector's consolidated balance sheet, GNPA, capital adequacy (same chapter credit-deep Part C §C.2 already documents for NBFCs generally) | Biannual (June/December editions) |

Illustrative levels (both flagged as third-party-repeated NHB/ICRA figures, not this Part's own
computation): individual housing loans outstanding (banks + HFCs) **₹33.53 lakh crore at end-Sept
2024** (+14% y-o-y, NHB); HFCs' total loan portfolio **₹9.57 trillion at end-March 2024** (+14.36%
y-o-y; housing loans within that +11.88%, non-housing — loan-against-property, developer/construction
finance — +21%, ICRA industry estimate, **[VERIFY, commercial third-party, not primary NHB data]**).

**The bank+HFC aggregate — mirroring credit-deep Part C §C.2's bank+NBFC rule exactly, with one
added nuance.** Construction: `housing_credit_total = housing_credit_bank + (hfc_credit_total −
bank_credit_to_HFCs)`, netting bank lending *to* HFCs out of the HFC leg before summing, for the
identical double-counting reason credit-deep Part C documents (bank credit to HFCs already sits
inside `housing_credit_bank`'s parent Sectoral Deployment aggregate as part of bank credit *to
NBFCs*, since HFCs are now formally an NBFC sub-category — post-Aug-2019 this netting is literally
the same netting operation credit-deep's L10 construction already performs, not a second,
independent one to re-derive). **Frequency mismatch, same discipline**: bank housing credit is
monthly (~3-week lag); HFC credit is NHB-Trend-and-Progress-anchored (annual, ~11-month lag) or
RBI-FSR-anchored (biannual) — the combined series can only be as fresh as its slowest leg unless
upsampled by piecewise-linear log-interpolation between successive HFC reference dates, with a
staleness mask once a new edition is overdue, identical to credit-deep Part C §C.10's convention.

**The shared-block awareness this construction owes L10.** Because HFCs are now formally an NBFC
sub-category, L12's housing-credit leg is a *subset* of L10's own bank+NBFC aggregate, not an
independent measurement — `ladder.yaml`'s own comment on `macro_credit_block` ("shared by
L6+L10+L11+L12, de-duplication rule §4.2") already anticipates this overlap. Rule: **build the
housing-specific credit leg from Sectoral Deployment's own Housing/CRE sub-lines directly, never by
re-slicing L10's already-aggregated total** — the sub-line data is separately published at the same
source, so no re-derivation is required, but the two seats' outputs are not independent draws and
should never both be cited as separately-corroborating evidence of one underlying credit expansion.

---

## C.4 Supply-side free data — RERA, listings, and the classic materials proxies

**RERA state portals — genuinely scrapable, genuinely not a bulk download.** Every state runs its
own Real Estate Regulatory Authority under the central RERA Act, 2016 (MahaRERA, Karnataka RERA,
UP-RERA, TS-RERA, Gujarat RERA, etc.) — **there is no central, unified, bulk-downloadable national
RERA database**; each portal is a project-by-project search interface (by registration number or
project name), not a documented public API (**[VERIFY]** for all 28 states/UTs — confirmed this
pass only for Maharashtra and Karnataka). Third-party aggregators (`reradetails.in`, `rerawebsite.in`,
`realatic.com`) already scrape multiple state portals into unified search tools — evidence the
underlying sites are technically scrapable, not evidence a free bulk feed exists. **Budget a
state-wise RERA project-registry build as a genuine multi-week scraping project** (identical framing
to A-catalog's own IPO-anchor-registry item), starting with the five largest markets by
registration volume — Maharashtra, Karnataka, Telangana, Uttar Pradesh, Gujarat.

**Listing aggregators (99acres, MagicBricks, Housing.com/PropTiger, NoBroker) and industry-report
inventory data (ANAROCK, Knight Frank, JLL, CBRE) — exploration-only, mirroring the screener.in
rule.** These sources carry launches, unsold inventory, and asking prices at a city/micro-market
level, none behind a documented free bulk API, and — the disqualifying property, per the
2026-09-01 mirror-authorization decision (`research/OPEN_QUESTIONS.md`, applied identically in
value-deep Part C §C.6 to screener.in) — **no vintage layer**: a pull today shows today's
best-known snapshot, not what the site showed at any past date, so a backtest built on a scraped
history silently reintroduces the look-ahead bias Known Prior #7 already prices at 150–450bps/yr
for fundamentals. **Fine for fast exploration, never as the fixture a signal is evaluated against.**
Illustrative numbers (context only, not admissible evidence): unsold inventory across eight major
markets **~5.26 lakh units, H1 2026** (Knight Frank) vs. **~6.16 lakh units** on ANAROCK's own count
for the same broad period, a different city set and methodology — the two disagreeing by that much
is itself demonstration of why neither is a fixture-grade series.

**Cement production — Index of Eight Core Industries (ICI).** Cement carries a **5.37% weight**
within the ICI (itself ~40.27% of overall IIP weight), compiled by the **Office of the Economic
Adviser (OEA), DPIIT, Ministry of Commerce & Industry** — the same body that compiles WPI
(A-catalog H2). Released monthly on the **last working day of the following month** (~4-week lag),
first provisional, later revised — the standard two-vintage cadence RBI/MOSPI series generally
carry. **A base-year rebase is itself in-flight**: OEA released a revised Core Industries series
with base year **2022-23** around **2026-07-20**, the same 2026 rebase wave debt-deep Part C §C.11
documents for GDP/CPI/WPI/IIP — cement's ICI sub-index inherits that break.

**Steel consumption — Joint Plant Committee (JPC), Ministry of Steel.** JPC publishes monthly
finished-steel apparent-consumption bulletins (`jpcsteel.co.in`) — the classic construction-demand
cross-check alongside cement, at the same monthly cadence; **[VERIFY]** exact publication lag (not
independently pinned this pass; industry commentary implies a similar ~3–4 week lag to the ICI).

**Construction GVA — quarterly national accounts.** MOSPI's quarterly GDP/GVA release (already
documented at credit-deep Part C §C.3 — series from reference quarter Q1:1996-97, ~2-month lag) 
breaks the economy into three broad sectors; **Construction sits in the Secondary sector**
(alongside Manufacturing and Electricity/Gas/Water), at **~8% of nominal GVA in FY2025-26**, second
only to Manufacturing within that sector — this is the free, official, quarterly supply-side
building-activity flow. **Do not confuse it with "Real Estate, Ownership of Dwelling & Professional
Services,"** a *Tertiary*-sector GVA category dominated by imputed owner-occupied rent, a
stock/asset-services concept, not a construction-activity flow — the two categories are adjacent in
every press release table and easy to conflate; only "Construction" answers the supply-side
question this section is built for. Same 2026 rebase wave applies (base 2011-12 → 2022-23, per
debt-deep Part C §C.11's already-documented GDP transition), inherited without re-derivation here.

| Series | Compiler | Cadence | Lag | Weight/share | 2026 rebase status |
|---|---|---|---|---|---|
| Cement production (ICI) | OEA, DPIIT | Monthly | ~4 weeks | 5.37% of ICI | New base 2022-23, ~2026-07-20 |
| Finished-steel apparent consumption | JPC, Min. of Steel | Monthly | **[VERIFY]** | — | Not confirmed rebased this pass |
| IIP "Infrastructure/Construction Goods" (use-based) | MOSPI | Monthly | ~6 weeks | ~12.3% of IIP | New base 2022-23 from May-2026 (per A-catalog H3) |
| Construction GVA | MOSPI (National Accounts) | Quarterly | ~2 months | ~8% of nominal GVA | New base 2022-23 from 2026-02-27 |

---

## C.5 Transaction-side — registration counts, stamp duty, and home-loan disbursals

**Property registration counts and stamp duty collections.** The primary free source is each
state's own Registration/Stamps department portal; **Maharashtra's IGR** (`igrmaharashtra.gov.in`)
is the standard reference case — Maharashtra records over 10 lakh property registrations annually,
Mumbai alone contributing roughly 30%, and the portal exposes a daily/monthly registration-count and
revenue e-search facility. In practice the free, already-cleaned, ready-to-use version of this data
is **Knight Frank India's monthly Mumbai/Pune registration notes**, which state explicitly that they
are built from Maharashtra's Department of Registrations and Stamps' own published figures — i.e.,
Knight Frank does the state-portal scraping already, and republishes it monthly with a short lag
(within days of month-end for Mumbai; the underlying IGR data is available directly, if scraped
independently, essentially in near-real time). **[VERIFY]** the equivalent portal quality and
release cadence for the next-largest markets (Karnataka's Kaveri Online, Delhi's e-registration
system, Telangana's IGRS) — Maharashtra's IGR is confirmed as the best-documented case this pass,
not necessarily representative of every state.

**State budget documents.** Every state's own Budget "Receipts" annex carries stamp-duty-and-
registration-fee collections as a distinct revenue head, annual, with the same multi-month
publication lag general state fiscal data carries (debt-deep Part C §C.4's State Finances caveats
apply identically here) — useful as an annual cross-check on the monthly IGR-style flow data, not a
substitute for it.

**Home-loan disbursal data.** No free, structured, economy-wide *disbursal* (vs. *outstanding-
balance*) series was found this pass — Sectoral Deployment and NHB's Trend and Progress report both
give **outstanding stock** and its growth rate, a close but distinct concept from gross disbursal
(new loans originated, gross of repayments/prepayments). CRIF High Mark and Care/ICRA sector reports
carry disbursal-level detail but are paid products outside the Contract's free-source mandate — flag
**out of free reach**; the Sectoral Deployment growth rate is the free substitute, understood as a
*net* flow, not the gross figure a lender-side dataset would show.

---

## C.6 Price cross-checks — listing indices, and the circle-rate honesty note

**Listing-portal price indices** (99acres' own "Insite" index, MagicBricks' "PropIndex," Housing.com's
price trackers) exist and are free to view, but inherit the identical exploration-only rule §C.4
already states for inventory data — asking prices, not transacted prices, with no vintage archive
and no documented free bulk API. Use them only as a directional cross-check against RBI HPI/RESIDEX
movements in the same quarter (do the signs agree?), never as an input series.

**The circle-rate / ready-reckoner honesty note — bias direction stated, not hedged.** Every state
sets a minimum registerable transaction value (Maharashtra: "Ready Reckoner Rate";
Delhi/UP/Haryana/Punjab: "Circle Rate"/"Collector Rate"); a sale priced below this floor is deemed to
occur *at* the circle rate for stamp-duty and capital-gains purposes regardless of the actual
consideration paid — backstopped by Section 56(2)(x) of the Income Tax Act (any gap above ₹50,000
between declared price and circle rate is taxed as income to the buyer). The direction this forces
on every registration-based series (RBI HPI, RESIDEX's assessment leg, any IGR-derived stamp-duty
series): **where a cash/"black" component still rides on top of the registered price, circle rates
put a floor under what gets *reported*, so registered prices systematically run below true
transacted prices, and the gap widens exactly when informal-premium behavior is most active —
late-cycle, speculative phases.** The design's registration-price-based gauges therefore carry a
**structural downward bias in cycle amplitude, concentrated at peaks** — a documented narrowing of
the circle-rate/market-value gap in recent years reduces but does not eliminate this bias, and its
size is not independently quantifiable free. State this bias direction inline wherever the L12 price
leg is shown, the same discipline debt-deep Part C §C.8 applies to the pre-1991 administered-rate
caveat: a known, dated, one-directional distortion to disclose, not silently correct for.

---

## C.7 Vintage/PIT hazard table

| Series | Revision-prone? | Two dates never to conflate | Store first-print or every vintage? |
|---|---|---|---|
| RBI HPI | **Yes, structurally** — 2022-23/18-city rebase (2025-10-10, first print for Q1:2025-26); registration-lag revision risk within a base unconfirmed [VERIFY] | Base-transition date vs. reference quarter; within-base first-print vs. any later revision | Both bases kept distinct, checksum + vintage each; never overwrite |
| NHB RESIDEX | Yes — two dated breaks (2015 series lapse/2017 relaunch at FY2012-13 base; April–June 2018 quarter rebase to FY2017-18) | Relaunch date vs. rebase date — two separate events, both level breaks | Every base-year vintage kept distinct |
| RBI Sectoral Deployment — Housing/CRE sub-lines | Format break, not a value revision | January 2019 reporting-format change (confirmed for NBFC-in-Services, [VERIFY] for Housing/CRE specifically) | Old-format (pre-2019) and new-format series kept distinct |
| HFC credit (NHB Trend & Progress / RBI FSR) | Regulatory-lineage break, not a value revision | 2019-08-09 (HFC regulation transferred NHB→RBI; HFCs reclassified as an NBFC sub-category) | Flag pre-/post-2019-08-09 on any HFC-specific series |
| Cement (ICI), IIP Infra/Construction Goods, Construction GVA | Yes — all three inherit the 2026 base-2022-23 rebase wave (debt-deep Part C §C.11) | Rebase effective date (ICI ~2026-07-20; IIP May-2026; GVA 2026-02-27) vs. reference period | Both bases kept distinct per series |
| RERA project registrations | Not revision-prone in the GDP sense, but **status-mutable** — a project's registration record (timeline, completion %) is live-updated by the developer, so "today's snapshot" ≠ "the record as of any past date" | Snapshot-pull date vs. project's own last-updated date | Snapshot each pull, dated — no vintage archive exists upstream to rely on |
| Listing-aggregator inventory/price data | No vintage layer upstream at all (§C.4/§C.6) | N/A — exploration-only, never stored as a fixture for evaluation | Do not build a backtest-grade fixture from this source |
| IGR/stamp-duty registration counts | Not typically revised once posted, but state-specific cadence/format varies | Portal posting date vs. actual registration date (can lag by the statutory registration window) | Monthly snapshot, dated; cross-check against annual state Budget figures |
| Circle rate / ready reckoner rate | Event-based (rate-revision notifications), not a data revision | Notification effective date vs. any later news-report date | Append-only event log, dated by the state notification's effective date — same discipline debt-deep Part C §C.11 applies to SLR/CRR |

---

## C.8 The L12 India pipeline — from raw pulls to the two-leg state

**A design tension to resolve first, explicitly.** `ladder.yaml`'s L12 entry carries `inputs:
[L10_credit_block]` — a DAG edge to the *total* bank+NBFC credit/GDP gap L10 already builds — while
its own `indicator` field names `"RBI HPI, housing credit, RBI FSR"`, and this Part's brief calls
for a **housing-credit-specific** long leg (§C.3), not a re-use of L10's economy-wide aggregate.
JST's pooled construction (`jst-fincycle-RESULTS.md`'s header) uses generic, not sector-specific,
credit — that is what the global panel offers. **Resolution, argued**: build L12's credit leg from
the Sectoral Deployment Housing+CRE sub-lines directly (§C.3) — a more precise read of the
housing-driven leg than total credit, which mixes in unrelated industry lending — and retain the
L10 DAG edge strictly as a **validation cross-check**: confirming FC1's co-movement finding
(corr(Δcredit/GDP, Δlog real house prices), median +0.40, 17/17 countries) holds when India's own
housing-specific credit gap is compared against its house-price gap, never as a substitute
computation. Per Contract §5, this departure from the pooled paper's literal construction is
recorded with its argument, not silently substituted.

1. **Registry load.** Validate `config/ladder.yaml` L12 against `config/validator.py` before any
   pull, same gate every other seat's pipeline uses.
2. **Pull raw fixtures** into `data/fixtures/P_realestate/{rbi_hpi_legacy,rbi_hpi_2022base,
   nhb_residex,sectoral_deployment_housing,sectoral_deployment_cre,nhb_trend_progress,rbi_fsr_nbfc,
   rera_state_{state},igr_maharashtra,ici_cement,jpc_steel,iip_construction_goods,
   construction_gva}/{vintage}/...` — a genuinely new fixture family (no existing `ingest/pull_*.py`
   script covers any of these; see closing note). Manifest immediately
   (`python ingest/manifest.py data/`), every file keyed `(series_id, vintage_date, pull_date)`.
3. **STEP 1 — credit leg (the long leg).** Build `housing_credit_total = housing_credit_bank +
   (hfc_credit_total − bank_credit_to_HFCs)` per §C.3; apply Hamilton's (2018) regression filter
   (h=5y=60 months, p=1 lag, monthly — never the HP filter, Contract §8) to the credit/GDP ratio
   (nominal GDP denominator per credit-deep Part C §C.3's own ratio-splice convention); compute the
   **expanding percentile** against India's own history from the series' effective start
   (**[VERIFY]** exact month the Housing sub-line begins — bracket ~1998–2007; A-catalog G1 anchors
   the parent Sectoral Deployment release at ~1998). Warm-up: h+p=61 months lost before the first
   gap, plus a 48-month min-obs floor (mirroring the Contract's own "≥4 observations" Tier-B floor,
   scaled to monthly cadence) — first trustworthy credit-leg percentile lands **≈2003–2012**
   depending on the confirmed start date, comfortably ahead of the price leg.
4. **STEP 2 — price leg (short leg, warm-up stated honestly).** Splice the RBI HPI legacy (2010-11
   base) and current (2022-23 base) series per §C.1's ratio-splice rule; apply the same Hamilton
   filter (h=5y=20 quarters, p=1) to the real house-price level (deflated by CPI-Combined, itself
   spliced across its own 2011/2024/2026 base changes per debt-deep Part C §C.9 — not re-derived
   here). Warm-up: h+p=21 quarters lost from the June-2010 start → first gap **≈2015–2016**; a
   16-quarter min-obs floor → first trustworthy price-leg percentile **≈2019–2020** — the "supports
   ranks only from ~2020" fact the brief names, derived here, not assumed.
5. **STEP 3 — combine, with the India-length Tier-C clamp.** Before the price leg clears warm-up
   (pre-~2020): `L12_state = credit_leg_percentile` alone — the price leg is masked, not defaulted
   to neutral. From ~2020 onward: `L12_state` remains `credit_leg_percentile` as the primary read
   (the credit leg independently qualifies for Tier B via the Contract §4 "n<4 domestic + ≥10
   cross-country analogues" branch — Claessens-Kose-Terrones' panel, per `ladder.yaml`'s own L12
   provenance), and the **price-leg percentile is routed through the existing `tierC_overlay`
   mechanism** (`budgets.tierC_overlay_cap: 0.10`, negative-only shift of regime score R — the same
   generic channel L1/L13/L14 already use, no bespoke L12-only overlay invented): when the
   price-gap percentile is *also* extreme (>0.8) and the credit-gap is elevated, it can pull the
   score down within that existing budget; it can never push L12's contribution up beyond what the
   credit leg alone shows. **This is a deliberate departure from JST's symmetric mean-of-two-
   percentiles construction**, justified because India's house-price series has **zero completed
   domestic cycles** (n=0, stricter than L12's own "India n=1" credit-leg citation) and no
   cross-country-analogues branch rescues a country-specific *rank* the way it rescues the
   *existence* of the underlying concept — per Contract §4, an input this thin may only reduce
   risk, never add it. `changes_if`: revisit a full symmetric 50/50 mean once RBI HPI carries
   ~25–30 years of native history — not before the mid-2030s at the earliest.
6. **STEP 4 — supply/transaction-side context, not scored.** Cement (ICI), steel (JPC), IIP
   Infra/Construction Goods, and Construction GVA (§C.4) feed a **narrative supply-tightness
   cross-check** alongside the scored two-leg state — none carries enough India-specific cyclical
   history on its own to earn a ladder seat; they inform the Stage-2 narrative layer (red team) the
   way debt-deep Part C routes contingent liabilities there (§C.9 below).
7. **STEP 5 — state as a phase object.** Log L12 as (level, velocity, quadrant, age-in-quadrant) per
   the 2026-09-01 states-as-phase-objects decision (`research/OPEN_QUESTIONS.md`), not a scalar —
   identical discipline to debt-deep Part C §C.12 step 6.
8. **STEP 6 — regime-score expression.** Feed `macro_credit_block` (0.20 of the regime-score budget,
   shared with L6/L10/L11 per `ladder.yaml`'s own de-duplication rule §4.2) — L12 is additive here,
   unlike L15/L16, which have no regime-score seat at all.
9. **Manifest every derived fixture** (credit-leg and price-leg gap/percentile, combined-state
   panel) as its own versioned, checksummed artifact; corrections append a new vintage row, never
   overwrite.
10. **Recalibration triggers**: a new RBI HPI base/coverage change (already happened once, 2025-10);
    a new NHB RESIDEX base change; a Sectoral Deployment reporting-format change; a CPI/GDP rebase
    flowing into the deflator/denominator; a Core-Industries/IIP rebase flowing into the
    supply-side context series; the first India-domestic completed medium-cycle leg (unlocks
    re-arguing the credit leg's own frozen parameters, per `ladder.yaml`'s own `changes_if`).
11. **Grids** (per `state_phase_convention`, unchanged for L12): `slope_horizon_grid_periods:
    [3, 6, 12]`, `smoothing_grid_periods: [1, 3, 6]`, `deadband_percentile_grid: [0.15, 0.25, 0.35]`
    — pre-registered, chosen once by tau_half (60–96 months), then frozen.
12. **Monitor**: quarterly refresh (bound by the price leg, the slower leg); annual review re-reads
    FC1–FC3 with one more year of India data; the 2030 design review re-reads the whole seat,
    unchanged in cadence from debt-deep Part C §C.12 step 10.

---

## C.9 What cannot be measured free — the honest list

| Need | Why it's out of reach free | What we do instead |
|---|---|---|
| **True transaction prices** (vs. registered prices) | Circle-rate floors and any residual cash component are unobservable in any public document by construction (§C.6) | Registration-based HPI/RESIDEX as the measured floor, bias direction (understated amplitude, worst at peaks) stated inline |
| **Unsold inventory, precisely and nationally** | No government census exists free; NHB itself was reported (Dec 2021) *seeking an external agency* to build one — confirmation the gap is real | ANAROCK/Knight Frank/PropTiger city-level estimates, exploration-only (§C.4), cross-checked for rough magnitude, never scored |
| **Developer leverage, granularly** (project debt, cost overruns, presales funding) | RERA discloses project *status and timelines*, not *balance sheets*; developer financials sit behind the same constraints value-deep Part C documents for listed names, and most developers are unlisted | Commercial Real Estate credit growth (§C.3) as an aggregate, sector-wide leverage-direction proxy only |
| **Land banks** (developer-held undeveloped land, valuation) | No free, structured disclosure exists outside listed-developer annual-report footnotes (inconsistent, unaggregated) | Named as a known-unknown in the Stage-2 narrative layer, identical framing to debt-deep Part C §C.13's contingent-liabilities treatment |
| **A single reconciled "the" house-price series** | RBI HPI, RESIDEX@Assessment, RESIDEX@Market, and listing indices measure four different things (registered / bank-valuation / market / asking price), no published bridge | Report each with source and construction stated; a persistent gap is a regime signal (§C.2), not a data error to average away |

---

## C.10 Runsheet additions for the principal's machine

No existing `ingest/pull_*.py` script covers any real-estate or housing-credit source — a larger
first-build gap than credit-deep Part C's NBFC layer, closer in scale to value-deep Part C's "no
fundamentals script exists at all" finding. Proposed additions to A-catalog §4's Phase-0 runsheet
(numbered as extensions past its existing 16 steps):

| Order | Task | Series | Est. hours | Why this order |
|---|---|---|---|---|
| 17 | Pull RBI HPI, both bases (legacy 10-city 2010-11, current 18-city 2022-23); confirm overlap window for the ratio-splice | §C.1 | 3–4 | Small, DBIE-adjacent (same portal family as G4), highest-priority price leg |
| 18 | Pull NHB RESIDEX, both post-2017 base vintages (FY2012-13, FY2017-18), both price concepts (Assessment/Market) | §C.2 | 3–4 | Second price cross-check; confirm current publication status live (this pass's confidence is search-only) |
| 19 | Pull Sectoral Deployment Housing + Commercial Real Estate sub-lines, full monthly history, both format eras (pre-/post-Jan-2019) | §C.3 | 2–3 | Piggybacks on the DBIE scraper credit-deep Part C's own runsheet step already budgets — same portal, two more sub-lines |
| 20 | Pull NHB "Trend and Progress of Housing in India" (all available annual editions) and RBI FSR NBFC chapters (HFC-specific tables), hand-transcribe | §C.3 | 3–4 | Manual PDF transcription, same discipline as credit-deep's own FSR/GNPA step |
| 21 | Build one state's RERA scraper end-to-end (Maharashtra MahaRERA first) as a template; confirm scrapability and rate-limit behavior before committing to a multi-state build | §C.4 | 6–10 | Genuinely new construction, not a download — start with one state to de-risk the approach before scaling to Karnataka/Telangana/UP/Gujarat |
| 22 | Pull cement (ICI), IIP Infrastructure/Construction Goods, finished-steel consumption (JPC), Construction GVA — all four, both pre-/post-2026-rebase vintages where applicable | §C.4 | 2–3 | Cheap, stable, mechanically easy; batch with the existing MOSPI/OEA pulls credit-deep Part C's runsheet already schedules |
| 23 | Build the Maharashtra IGR scraper (or confirm Knight Frank's own monthly notes are a sufficient free proxy before building one) | §C.5 | 4–6 | Confirm the cheaper substitute (Knight Frank's republished IGR data) covers the need before budgeting the heavier direct-portal scrape |
| 24 | `config/` registry + CI validator smoke-test against the newly-pulled L12 fixtures | all above | 2 | Confirms the pull satisfies the "every module runs on fixtures with zero live data" gate, same as A-catalog's own step 16 |

**Total estimated incremental effort: ~25–36 hours**, on top of A-catalog's existing ~45–60-hour
Phase-0 estimate — driven mainly by step 21's RERA build, the one item here with no existing scraper
to extend and no structured free bulk source to fall back on.

---

*End of Part C. Cross-references: `research/CONTRACT.md` §3 (free-source mandate), §4 (evidence
tiers, Tier-C reduce-only), §5 (survival argument for the JST-construction departure in §C.8), §8
(no HP filter), Known Prior #11 (no live network access; principal's-machine ingestion);
`config/ladder.yaml` L12_realestate_medium_cycle (tier B, macro_credit_block, inputs:
[L10_credit_block]), `budgets.tierC_overlay_cap`, `state_phase_convention` grids;
`research/cycles/fincycle-deep/jst-fincycle-RESULTS.md` (FC1–FC3, the combined-state definition this
Part sources data for); `research/cycles/credit-deep/partC-data.md` (bank+NBFC method mirrored to
bank+HFC in §C.3; Sectoral Deployment base layer, extended not duplicated); `research/cycles/
debt-deep/partC-data.md` (structure/PIT discipline this Part follows; the 2026 rebase wave, inherited
in §C.4/§C.7); `research/cycles/value-deep/partC-data.md` (exploration-only rule, mirrored to
listing aggregators in §C.4/§C.6); `docs/masterplan/A-data-catalog.md` block G4 (RBI HPI — extended,
corrected, not duplicated) and §4 (Phase-0 runsheet, extended in §C.10); `research/OPEN_QUESTIONS.md`
(2026-09-01 mirror-authorization decision, §C.4/§C.6; states-as-phase-objects decision, §C.8 step 7).*
