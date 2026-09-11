# HANDOFF PROMPT — THE INDIA REAL-ESTATE PREDICTION ENGINE (v2)
Written 2026-09-11 at the close of the IN programme, for a NEW Claude Code thread.
Paste everything below the rule. Self-contained: assumes the repo, assumes no memory of the
conversation that produced it. v2 supersedes v1 — it adds the identified econometric model for the
black-money problem, the real data-source inventory, the locality universe, the validation ladder,
and the project's own kill criteria.

---

You are joining **The Cycle Program** (`/home/user/claude-demo`), a quantitative desk running an
Indian multi-asset book for a single principal. Read `CLAUDE.md` and `research/CONTRACT.md` first —
binding, and nothing here overrides them.

## THE MISSION

Build the **India Real-Estate Prediction Engine**: a locality→city→state→national panel of Indian
property prices and their drivers; a validated model of what moves them; state-conditional 3y/5y/10y
forward distributions; and a published dashboard. Then make it answer the three questions a wealth
principal is actually asked — *should I buy in X, is what I own overvalued, and does renting beat
buying here* — because an engine that cannot answer those is an academic exercise.

## WHAT "BEST OF THE BEST" MEANS HERE, CONCRETELY

Not volume. The previous two programmes established that 500 well-sourced answers across 20 agents
beat 500 thin ones across 200. Excellence on this project looks like exactly five things:

1. **A defensible dependent variable where none currently exists publicly.** If you deliver only
   this, the project is a success.
2. **An identified treatment of the under-reporting problem** (see §3 — this is the intellectual
   core and it is a solved econometric problem that nobody has applied to Indian property).
3. **Features nobody else has assembled** — satellite-observed construction, ward-level circle-rate
   histories, registration microdata — rather than re-read press releases.
4. **An honest validation ladder** with the 10-year horizon's *impossibility* stated rather than
   faked.
5. **Negative findings published with equal prominence.** The most valuable outputs of the last two
   programmes were negatives: no adjustment multiplier for official Chinese data exists; the
   64.5m empty-homes figure was disowned by its own source; Indian REITs yield below the sovereign;
   leverage ratios missed Country Garden because presale liabilities were invisible to them.

Mediocrity on this project looks like: a beautiful dashboard built on portal asking prices, a
gradient-boosted model with 200 features and an in-sample R², a "top 10 cities" ranking, and a point
forecast. All four are easy and all four are worthless. Do not produce them.

## §1 — SEVEN CONSTRAINTS THE LAST SESSION PAID TO DISCOVER

**1.1 THERE IS NO DEPENDENT VARIABLE YET. This is the central problem of the project.**
No Indian city has a public repeat-sales or transaction-weighted house-price index. Every circulating
"+X%" is an **asking-price** or listed-rate comparison; where both were obtainable, Ulwe asking ran
**25-30% above actual registered closings**. NHB RESIDEX is coarse, lagged, city-level. RBI's HPI is
10 cities, quarterly. **You cannot model a price series you have not built.** Phase 0 is
construction of the target variable and its gate forbids proceeding on asking prices.

**1.2 WebFetch is EGRESS-BLOCKED for every domain. WebSearch works. GitHub is open.**
Tested directly. ~20 agents on the prior programme each lost roughly a third of their budget to
WebFetch calls that cannot succeed — **tell every agent explicitly never to call it.** GitHub raw/LFS/
git-proxy IS reachable, so GitHub-hosted dataset mirrors are the one live data channel. Hunt them hard.

**1.3 AGENT ECONOMICS — 1,000 agents in one session is arithmetically impossible.**
Measured across ~30 research agents: **150,000-195,000 tokens each**. 1,000 agents ≈ **160-195
million tokens** against a ~15 million session budget. One session supports **70-90 at quality**.
The requested scale is reachable only as a **multi-session programme with durable state on disk** —
`MANIFEST.md` (every task), `DISPATCH.md` (status per bundle), a completion ledger — so session N+1
resumes and the counts genuinely accumulate. Never fake scale with thin agents.

**1.4 POINT FORECASTS ARE FORBIDDEN, and the desk's own results say why.**
Booked: the ER arc's pooled expected-return equations fail OOS at every horizon once purged and
honestly benchmarked; single-country kitchen sinks exploded at **−389%** OOS; CN-D3 found the
best-known credit early-warning indicator carries an **87.2% false-alarm rate** at 3 years; IN-D1
found **zero of 884 post-1970 five-year windows** across 18 countries ever cleared 20%/yr real
appreciation. The product is a **state-conditional distribution**: given this locality's observable
state, here is the forward distribution for comparable states, with n and the failure rate attached.

**1.5 ANNOUNCEMENT MOVES THE PRICE; COMPLETION MERELY CONFIRMS IT.**
Three agents found it independently. Navi Mumbai airport: Panvel +76% since 2021, mostly **before the
first flight**. Jewar: Noida belt +142-158%/5y, mostly before flying. Delhi-Dehradun Expressway:
**+23% in the nine months before opening**. Samruddhi: corridor land ≈3.7x pre-completion. Completed
MMR infrastructure then yields only a smaller continuing 8-15%/yr premium. **Corollary: every public,
dated feature is already partly in the price.** A model built on announced infrastructure will look
brilliant in-sample and predict nothing.

**1.6 HOT MARKETS STAY HOT — my own mean-reversion prior MISSED, and this is the most actionable
thing the desk knows about property.** IN-D1: the next five years after a ≥15%/yr real window
returned **+9.65%/yr real**, and +11.16% after a ≥20%/yr window. Momentum beats mean reversion at
the 5-year horizon. Simultaneously those windows carry **~2× crash odds**. So the correct treatment
is **ride-it-but-size-it**, never in-or-out. Build the engine to express that, not a buy/avoid flag.

**1.7 UNITS AND COMPOSITION WILL DESTROY THIS PROJECT IF YOU LET THEM.**
Carpet vs built-up vs super-built-up moves an Indian per-sqft figure **20-35%** and reverses
rankings; RERA mandates carpet since 2017 but older and broker data does not. Circle rates, jantri
rates and government auction prices are **not market prices**. And the prior programme caught a
Chinese national land series whose *average rose* while *every tier fell* — a pure mix shift read as
a price move, which the source itself labelled 结构性上涨. Every index you build needs an explicit
composition control and a stated area basis.

## §2 — THE LOCALITY UNIVERSE (define this before anything else)

"Locality level across India" is meaningless until the unit is fixed. Candidates, in descending
order of usefulness:

- **Census 2011 town/village codes** — the only exhaustive, official, hierarchically-nested
  geography (state → district → sub-district → town/village). ~640 districts, ~7,900 towns,
  ~640,000 villages. This should be the **spine**, because everything official keys to it.
- **Pincodes** (~19,300) — the unit portals and delivery data actually use, but they are postal
  routes, they cross administrative boundaries, and they are revised.
- **Municipal wards** — the right unit for circle rates and property tax, but there is no national
  ward registry and boundaries change at every delimitation.
- **Sub-registrar office (SRO) jurisdictions** — the unit registration microdata arrives in, and
  therefore the unit your dependent variable will natively have.

**Do this**: build an explicit crosswalk table (SRO ↔ ward ↔ pincode ↔ Census town/village), treat
it as a first-class deliverable, and record its match rate honestly. Every later join depends on it
and a silent 30% mismatch will invalidate everything downstream. Expect this to be harder than the
modelling.

**And register the selection problem now, because it is the desk's oldest artifact in a new guise.**
Localities *enter* the panel endogenously — Ulwe was not a market in 2010; Kokapet barely existed.
An unbalanced panel where entry is caused by the very price appreciation you are measuring is the
EW-survivor artifact the desk has now hit five times (SC-D4, TECH-D3, MOM-D1, VAL-D2/D3, EQ-D1).
Declare a one-way rule per design: a bias that flatters growth localities makes a print *against*
them admissible and a print *for* them non-evidence.

## §3 — THE INTELLECTUAL CORE: UNDER-REPORTING IS AN IDENTIFIED ECONOMETRIC PROBLEM, NOT A COMPLAINT

This is the most valuable idea in this document. Read it twice.

The standard framing — "Indian property data is unreliable because of cash" — is a dead end that
produces hand-waving. The correct framing is this:

- A transaction must be registered at **no less than the circle rate** (stamp duty is assessed on
  `max(declared value, circle rate)`).
- Where a buyer and seller split the price into declared-plus-cash, the rational declared value is
  **exactly the circle rate** — declaring less buys nothing, declaring more costs stamp duty.
- Therefore the registered value is a **left-censored observation of the true price, with a known,
  observable, time-varying, ward-level censoring threshold**: the circle rate itself.

That is a textbook censored-regression (Tobit-type) setup with an unusually good property — **the
censoring point is observed, not estimated**. Consequences, all of them testable:

1. **The share of transactions registering at or within ε of the circle rate is a direct estimate of
   under-reporting incidence**, by ward and by month. Nobody publishes this. It is computable from
   registration microdata plus circle-rate tables, and it would be a genuinely new series.
2. **The censored model recovers the latent true-price distribution** where a naive mean or median
   of registered values does not. A naive index is biased toward the circle rate exactly where cash
   intensity is highest — i.e. it *understates* appreciation in the localities you most care about.
3. **Circle-rate revisions are natural experiments.** When a ward's circle rate is revised upward,
   previously-censored transactions become uncensored and the registered mean jumps *without any
   change in true prices*. Any index that ignores this will print a spurious price rise on a tax
   administration event. Maharashtra's ready reckoner sat **frozen 2019-22** and Gujarat revised
   jantri in 2023 — both are identification opportunities and both are traps.
4. **The desk's prior finding becomes testable at locality level.** The last session concluded that
   removing cash is a *volume* effect not a *price* effect — across the 2016-17 formalisation stack
   (demonetisation, Benami amendment, RERA, GST, Section 269ST) all-India price growth decelerated
   from ~7-8%/yr to ~3-4%/yr but **never went negative**, while launches fell **−44%** against sales
   down only **−12%**. The mechanism: the marginal, index-setting buyer became the formal
   bank-financed end-user — the *least* cash-exposed participant — while cash-heavy resale, land and
   premium absorbed the hit in transaction volume. Test that properly with the censored model.
5. **Corroborating evidence that formalisation is real**: Ayodhya deed prices were registering
   **41% to 1,235% above circle rate** by 2023. Under pure circle-rate registration that cannot
   happen. It is evidence of substantial (not complete) formalisation, with the caveat that it does
   not prove the registered value equals the full price.

**Cash intensity by segment** — consistent ordering across sources, and no audited figure exists
anywhere: land and agricultural highest (~40%+), then resale and premium, then branded primary and
bank-financed lowest (structurally bounded by RERA's 70% escrow and bank underwriting). Treat every
circulating percentage as directional. Specifically: Anarock's "black money in housing down 75-80%
since Nov 2016" covers *housing* not all real estate, its own stated mechanism is **compositional**
(branded developers gaining share) rather than a re-measurement of cash per transaction, and Anarock
is commercially aligned with the developers the claim credits. LocalCircles' prevalence figures rest
on a single self-selected online panel. Both directionally useful; neither a measurement.

## §4 — DATA SOURCE INVENTORY (probe reachability from THIS environment before promising anything)

Grouped by channel. For each, record: reachable-from-here / needs-principal-machine-pull; update
frequency; publication lag; granularity; and whether the series is **revised** (a revised series used
as a feature is lookahead — there is a booked process note on exactly this error).

**A. The dependent variable**
- State registration portals — Maharashtra **IGR**, Telangana **IGRS/Dharani**, Karnataka **Kaveri**,
  Tamil Nadu **TNREGINET**, UP **IGRSUP**, Gujarat **Garvi**, Delhi **DORIS**, Rajasthan **e-Panjiyan**,
  MP **SAMPADA**. These are the prize. Scrape-shaped; most likely principal-machine.
- **NHB RESIDEX** (city composite, quarterly). **RBI HPI** (10 cities, quarterly, via **RBI DBIE**).
  RBI's Residential Asset Price Monitoring Survey. MoSPI **eSankhyiki**.
- Circle rate / ready reckoner / **jantri** portals, per state, with history.

**B. Government open data, API-shaped**
- **data.gov.in** — has a documented REST API with resource IDs and a free API key. The single
  highest-value probe target; it carries census extracts, housing, urban, and infrastructure tables.
- **VAHAN** vehicle registrations (district-granular, monthly — a strong income/household proxy).
- **UDISE+** school enrolment (district, annual — household formation).
- **EPFO / ESIC** monthly payroll additions by state — genuinely high-frequency formal-job demand.
- **PLFS / NSSO** microdata; **Census 2011** downloadable tables; **SECC**.
- **MCA21** (developer entity data), **GSTN**, **NCRB** (crime), **CPCB** (air quality),
  **CGWB** (groundwater — a binding constraint in Bengaluru and NCR), **IMD** (rainfall).
- **DILRMP / Bhu-Naksha / ULPIN** land records and cadastral maps.
- State **RERA** registries — MahaRERA, UP-RERA, TG-RERA, K-RERA and peers publish searchable
  project registrations with launch, completion and stalled status. This is the best public supply
  data in India and it is under-used.

**C. Satellite and geospatial — the genuine edge, because nobody has assembled it for India**
- **NOAA VIIRS night-lights** (monthly, free, no key) — the workhorse.
- **Copernicus / Sentinel-1 and -2** (free) and **Google Earth Engine** (free for research) —
  observed built-up-area change and construction activity.
- **ISRO Bhuvan**; **OpenStreetMap** building footprints and road growth via the **Overpass API**;
  **Overture Maps** (AWS Open Data); **WorldPop**; **Microsoft/Google building footprints** (both
  published open India layers).
- **Observed construction from satellite is a supply measure that leads every official statistic and
  is in no price.** If §1.5 is right, this is where the residual edge lives.

**D. Infrastructure, as delivered rather than announced**
- **AAI monthly passenger traffic** by airport (delivered demand, not a press release).
- **NHAI / Bharatmala / MoRTH** project progress; **MoHUA** metro line status with dated milestones;
  major port throughput; **Grid India (POSOCO)** daily load and **CEA** electricity data by state.
- **GTFS** transit feeds where published; ward-level water and sewerage connections.

**E. Credit, affordability, markets**
- **RBI DBIE** housing-loan outstanding and disbursements; HFC/NBFC books; sectoral deployment.
- Home-loan rates — **7.10-8.45% as of 2025 after 125bp of cuts; verify, do not assume 8-9%.**
- Mortgage-to-GDP ≈ **11-12%** (this bounds how much formal credit can substitute for cash).
- **SEBI REIT filings** (Embassy, Mindspace, Brookfield, Nexus); NSE/BSE realty indices.

**F. Risk and quality-of-place**
- **NDMA / BMTPC** hazard atlas (flood, seismic); **Coastal Regulation Zone** boundaries; municipal
  property-tax collection efficiency (a civic-capacity proxy); ULB credit ratings.

## §5 — THE FEATURE LIBRARY

Organise by **causal channel**, never by data source. Every feature carries seven mandatory fields:
source · update frequency · publication lag · granularity · first-available date · **point-in-time
or revised** · and the **channel hypothesis it tests**. A feature without a hypothesis is a
degree of freedom, and the register deflates for those.

Channels: **supply** (RERA launches/completions/stalled, approvals, OCs, FSI/TDR policy, land-use
conversion) · **demand and demography** (Census, UDISE+, PLFS, EPFO payrolls, VAHAN, electricity and
water connections, migration proxies) · **credit and affordability** (loan growth, ticket size, LTV,
rates, EMI-to-income, price-to-income, and the **carry spread**) · **infrastructure, split into
announced-date and completed-date features** (§1.5) · **satellite-observed construction** ·
**governance and risk** · **the policy and tax wedge** (stamp duty, circle-rate revisions, the
2016-17 stack, BR7/BR8/BR9 in `breaks-registry.md`) · and the **macro overlay this desk has already
booked** — FUN-D8 monetary seasons, the CU currency battery, CI-D1..D5, DB-D1..D9. Do not re-derive
those; quote them.

**Add the spatial channel explicitly**: neighbour-locality price growth, distance-to-CBD,
distance-to-nearest-metro-station, and travel-time isochrones. Locality prices are spatially
autocorrelated, which means two things — spillover is a real *feature*, and **standard errors
computed without spatial clustering will be wildly overstated.** Cluster on SRO or district.

## §6 — THE VALIDATION LADDER, AND THE HORIZON THAT CANNOT BE VALIDATED

Pre-register every design in `research/register/trial-ledger.md` with falsifiable bars **before**
computing anything. Use `quant/stats/` machinery — `cv.py` for purged walk-forward, `preprocess.py`
for winsorization bounds fitted on train only, `dsr.py`/`census_n()` for trial-count deflation.
Never inline re-implementations (process note #6).

**The benchmark ladder — a model must beat all four or it is not a model:**
1. Random walk on real locality prices (no change).
2. Local CPI (i.e. does it beat "prices track inflation"?).
3. The national or city index (does locality selection add anything over just being in India?).
4. The desk's own standing book at **11.46%/yr** — the actual opportunity cost of the capital.

**The 10-year horizon cannot be validated on India data, and you must say so on the dashboard.**
Registration microdata realistically starts ~2010-2013. That is **at most one** non-overlapping
10-year window, and overlapping windows are not independent observations. So:
- the **3-year** view can be honestly validated on India data;
- the **5-year** view can be validated weakly, with overlapping windows flagged;
- the **10-year** view must be borrowed from the **cross-country panel** (`CN-D1..CN-D5`, 48 episodes,
  18 countries, 150 years) as a base rate, and labelled as such. It is a base rate, never an India
  forecast.
Anyone who presents a validated 10-year India forecast from a 13-year panel is fitting noise.

**Carry the base rates into every forward view**: median crash −32% over 5.5 years; bust velocity ≈
boom velocity (0.99×, so no gentle-deflation discount exists); a bigger boom buys a **faster**
unwind not a deeper one; yield compresses −0.83pp into a peak and expands +1.53pp to a trough;
equities lose −13.7pp of excess real return in the year after a housing peak, doubled if banks break,
essentially recovered by year five.

**The yield conflict is the project's highest-stakes single number.** Indian city yield estimates
split into two irreconcilable families: portal/broker micro-market surveys (Mumbai 2.0-4.0%,
Hyderabad IT corridor 2.5-4.2%, Lucknow ~3%, Ahmedabad 3.9%) versus Global Property Guide's city cut
(national blend 5.16%, Delhi/Kolkata 5.8-6.3%). CN-D2 puts historical peaks near **3.29%** gross and
troughs near **4.94%**. **The first family says Indian metros are priced at a historical peak; the
second says a historical trough.** Resolving it with registration microdata plus rental listings is
worth more than any model. Note also that India's carry spread (−2.0pp to −5.0pp) is **wider negative
than China's** (−0.9 to −1.3pp), which is not the intuitive result.

## §7 — PHASES AND GATES

**GATE 0 — the target variable.** A locality-level panel exists, is sha256-manifested in
`ingest/vault/india_property/` with a two-pass AUTHENTICATION.md, uses a stated area basis, carries
a composition control, applies the §3 censored treatment where circle rates are available, and its
top-10 localities' 5-year changes reconcile within a stated tolerance against two independent
published figures. **If GATE 0 fails, stop and deliver the acquisition list.** That is a successful
session-one outcome; proceeding on asking prices is not.

**GATE 1 — the feature library.** All seven metadata fields populated for every feature; no revised
series used without a vintage stamp; a published coverage matrix (localities × features ×
first-available-date) so sparsity is visible rather than silently imputed; the SRO↔ward↔pincode↔Census
crosswalk with its match rate stated.

**GATE 2 — does anything survive?** At least one channel beats all four benchmarks in a purged
walk-forward with spatially-clustered errors, deflated by trial count. **If nothing survives, that
is a publishable result** and the engine ships as a state-classifier and nowcaster rather than a
forecaster. Say so rather than fitting harder. The prior programme's most-cited findings were
failures.

**GATE 3 — the product.** The three client questions answerable end-to-end for any locality in the
panel: *should I buy here* (state + forward distribution + n + failure rate), *is what I own
overvalued* (its yield and price-to-income against the peak/trough bands), and **rent vs buy** (the
carry spread against the local mortgage rate — the most-asked question in Indian wealth management
and directly computable from what the desk already has).

## §8 — THE PROJECT'S OWN KILL CRITERIA

State these in the plan and honour them. A project without kill criteria becomes a sunk cost.
- Registration microdata unreachable for **≥3 of the top 8 cities** → abandon the locality tier,
  deliver a city-tier engine, and say why.
- Crosswalk match rate **<70%** → the locality join is not trustworthy; fall back to SRO-native
  geography and report in SRO units.
- No channel beats the four benchmarks after the pre-registered battery → ship the classifier, do
  not extend the battery hunting for significance (that is exactly what the 87.2% false-alarm finding
  warns against).
- Any locality index whose 5-year change cannot be reconciled to two independent sources → drop that
  locality from the published panel rather than publishing an unreconciled number.

## §9 — AGENT ORCHESTRATION

Max **3 concurrent** (CLAUDE.md rule 6); subagent model policy is in CLAUDE.md — follow it. Each
agent writes a cited dossier **to disk** and returns ≤200 words; content must never pass through the
orchestrator's context. Every research-agent prompt must state: **never call WebFetch**; two
independent sources for any load-bearing number; tag every figure `[2-SOURCE]` / `[1-SOURCE]` /
`[RECALL — unverified]`; state the as-of date; never invent a figure; name what could not be sourced;
and flag composition effects and area basis explicitly.

**Spawn these three first, before any planning is finalised:**
1. **Reachability probe** — for each source in §4, is it reachable from THIS environment? Hunt
   GitHub-hosted mirrors specifically (NHB RESIDEX, Census ward tables, VIIRS extracts, OSM India,
   RERA scrapes). Output: a reachable / not-reachable table, and RUNSHEET rows for the rest.
2. **Registration-microdata feasibility** — for the top 8 cities, what does each state portal
   actually expose (fields, granularity, history, bulk vs per-document, rate limits)? Output: a
   per-state field map and a verdict on whether the §3 censored model is buildable.
3. **Circle-rate history hunt** — ward-level ready-reckoner/jantri histories for Maharashtra,
   Gujarat, UP, Telangana, Karnataka. Without these the §3 core cannot be built at all, so this is a
   go/no-go probe, not background research.

## §10 — DISCIPLINE

Pre-register before running; interpretation written after the print; **bars never moved after a
print** (misses are recorded — there are many booked precedents); census append-only in
`trial-count.md` (currently 1,399); both commit gates via the pre-commit hook before every commit;
commit and push everything to the designated branch; no magic numbers; free data only; every vault
file sha256-manifested. Significant work ships as a published artifact + a committed copy in
`docs/learn/artifacts/` + a README row. Corrections go into published pages as **dated update
boxes** — superseded claims stay visible.

## §11 — PRIOR WORK IN THIS REPO: READ, DO NOT REDO

- `research/frontier/india-property-plan.md` — incl. §0, where "grow >20% in 5yr" is decomposed
  (cumulative = 3.71%/yr = **−0.75%/yr real**; CAGR = 148.8% and unprecedented post-1970).
- `research/notes/india-dossiers/` — **9 cited dossiers**: Mumbai inner and outer (8 micro-markets),
  Ahmedabad+Pune, Hyderabad+Lucknow, Amravati+Ayodhya, the candidate screen, black money,
  yields/REITs/developer leverage.
- `research/notes/china-dossiers/` — **20 dossiers**. The China bust is the closest available
  out-of-sample test of any India thesis you form. Use it that way.
- Ledger: `IN-D1..IN-D2`, `CN-D1..CN-D5`, and the `CN-DOSSIER` / `SNAPSHOT-1` notes.
- Published: **India Property Atlas** (README row 65) and **China Property Crash Atlas** (row 64).
  The new dashboard should supersede row 65's forward sections, not duplicate them.
- `RUNSHEET.md` — five IN rows and five CN rows already name the pulls this project needs. **That is
  your Phase 0 shopping list.**
- Two India findings worth carrying: **Kokapet land trades above its own buildings** (₹31,500/sqft
  raw land vs ₹11,900/sqft built) — the Chinese 面粉贵过面包 pattern appearing in India; and
  **Indian REITs all distribute below the 7.0% G-sec** (4.8-6.2%), three at 5-11% NAV discounts,
  with no residential REIT existing at all.

## §12 — START HERE

1. Read `CLAUDE.md`, `research/CONTRACT.md`, `india-property-plan.md`, and the five IN RUNSHEET rows.
2. Write `research/frontier/india-engine-plan.md` — the phases, gates and kill criteria above,
   adapted to what you find, with the honest agent/task arithmetic stated up front and the
   multi-session accumulation structure defined.
3. Spawn the three §9 probes. **Do not promise a locality panel before probe 2 and 3 report.**
4. Pre-register Phase 0's construction design, including the §3 censored specification, then run it.
5. Report GATE 0 honestly either way.

Final instruction, and it is the desk's actual character: **hunt the negative findings as hard as
the positive ones, and publish them with equal prominence.** On this project the most likely and
most valuable negative is that Indian locality price data cannot support a forecast at all — in
which case say so with the evidence, ship the nowcaster, and put the acquisition list on the
runsheet. That is a better outcome than a confident dashboard built on asking prices.
