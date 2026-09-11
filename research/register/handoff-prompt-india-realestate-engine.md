# HANDOFF PROMPT — THE INDIA REAL-ESTATE PREDICTION ENGINE
Written 2026-09-11 at the end of the IN programme, for a NEW Claude Code thread.
Paste everything below the line. It is self-contained: it assumes the new session has this
repository and no memory of the conversation that produced it.

---

You are joining **The Cycle Program** (`/home/user/claude-demo`), a quantitative desk running an
Indian multi-asset book. Read `CLAUDE.md` and `research/CONTRACT.md` first — they are binding and
nothing in this prompt overrides them.

## THE MISSION

Build the **India Real-Estate Prediction Engine**: a locality → city → state → national panel of
Indian property prices and their drivers, a validated model of what moves them, and a published
dashboard giving 3-year, 5-year and 10-year forward views with honest uncertainty. This is intended
to be the most complete piece of work this desk has produced on Indian real estate.

## READ THIS BEFORE YOU PLAN — FIVE CONSTRAINTS THE LAST SESSION PAID TO DISCOVER

Do not rediscover these. Each one cost real budget.

**1. THERE IS NO DEPENDENT VARIABLE YET. This is the central problem of the project.**
No Indian city has a public repeat-sales or transaction-weighted house-price index. Every "+X%"
figure in circulation — portals, brokerages, consultancies — is an **asking-price** or listed-rate
comparison, and where both were obtainable the gap was large: Ulwe asking prices ran **25-30% above
actual registered closings**. NHB RESIDEX exists but is coarse, lagged and city-level only.
**You cannot build a price-prediction model before you have built a price series.** Phase 0 is
therefore construction of the target variable, not modelling. Anyone who starts with features is
building on sand.

**2. WebFetch is EGRESS-BLOCKED for every domain in this environment. WebSearch works.**
Tested directly, not assumed. Twenty agents on the previous programme each lost roughly a third of
their budget to WebFetch calls that cannot succeed. **Tell every agent explicitly not to call
WebFetch even once.** GitHub (raw, LFS, git-proxy) is open, so GitHub-hosted mirrors of datasets ARE
reachable — that is the one live data channel and it should be hunted hard. NSE/RBI/NHB/MoSPI/state
portals are blocked and are principal-machine pulls.

**3. AGENT ECONOMICS: 1,000 agents in one session is not possible. Here is the real arithmetic.**
Measured over ~30 research agents: **150,000-195,000 tokens each**. So 1,000 agents ≈ **160-195
million tokens**, against a session budget of roughly 15 million. One session supports **70-90
agents at quality**. The requested scale IS reachable — but only as a **multi-session programme with
durable state on disk**, which is exactly how to build it: a task manifest, a completion ledger, and
resumable phases, so session N+1 picks up where N stopped and the counts accumulate. Do not fake the
scale by spawning thin agents; the previous programme's finding was that 500 well-sourced answers
across 20 agents beat 500 thin ones across 200.

**4. THE DESK FORBIDS POINT FORECASTS, AND THE BASE RATE SAYS WHY.**
Booked entries: the ER arc found that pooled expected-return equations fail out-of-sample at every
horizon once purged and honestly benchmarked, and single-country kitchen sinks explode at −389% OOS.
CN-D3 found that the best-known credit early-warning indicator has an **87.2% false-alarm rate** at
a 3-year horizon. IN-D1 found that **zero of 884 post-1970 five-year windows** across 18 countries
ever cleared 20%/yr real house-price appreciation. A "3y/5y/10y price prediction" that emits a single
number will be wrong and the desk will not ship it. **What it WILL ship is a state-conditional
distribution**: given this locality's current observable state, here is the historical distribution
of forward outcomes for comparable states, with the sample size and the failure rate attached. Build
that. It is more useful and it is defensible.

**5. THE FINDING THAT MOST CONSTRAINS THE PRODUCT: announcement moves the price, completion merely
confirms it.**
Three agents established it independently. Navi Mumbai airport: Panvel +76% since 2021, mostly
**before the first flight**. Jewar: Noida belt +142-158%/5yr, mostly before flying. Delhi-Dehradun
Expressway: +23% in the **nine months before** opening. Samruddhi: corridor land ≈3.7x
pre-completion. Completed MMR infrastructure then yields only a smaller continuing 8-15%/yr premium.
**Corollary: any feature that is public and dated is already partly in the price.** A model built on
announced-infrastructure features will look brilliant in-sample and predict nothing forward. The
engine's edge must come from (a) data that is public but *nobody has assembled* — registration
microdata, ward-level circle rates, satellite-observed construction — or (b) genuine nowcasting of
the *current* state faster than the market prices it, not from re-reading press releases.

## PRIOR WORK IN THIS REPO — READ, DO NOT REDO

- `research/frontier/india-property-plan.md` — the IN programme plan, incl. §0 where the
  "grow >20% in 5yr" bar is decomposed (cumulative = 3.71%/yr = −0.75%/yr real; CAGR = 148.8%).
- `research/notes/india-dossiers/` — **nine cited dossiers**: Mumbai inner and outer (8
  micro-markets), Ahmedabad+Pune, Hyderabad+Lucknow, Amravati+Ayodhya, the candidate screen,
  black money and formalisation, yields/REITs/developer leverage.
- `research/notes/china-dossiers/` — **twenty dossiers** on the China property bust. Use these: the
  China work is the closest thing to an out-of-sample test of any India thesis you form.
- Trial ledger entries `IN-D1..IN-D2` (the appreciation-threshold base rate) and `CN-D1..CN-D5` (the
  property-crash base rate: median crash −32% over 5.5y; bust velocity ≈ boom velocity at 0.99x;
  yield compresses −0.83pp into the peak and expands +1.53pp to the trough; equities −13.7pp excess
  in year one after a housing peak).
- Published dashboards: **India Property Atlas** (README row 65) and **China Property Crash Atlas**
  (row 64). The new dashboard should supersede row 65's forward-looking sections, not duplicate them.
- `research/register/RUNSHEET.md` — the five IN rows and five CN rows already name the pulls this
  project needs. **Those rows are your Phase 0 shopping list.**

## PHASE PLAN, WITH GATES

Each phase has a gate. Do not start the next phase until the gate passes, and record the gate
result in the trial ledger.

### PHASE 0 — BUILD THE TARGET VARIABLE (the phase everyone skips and the reason projects like this fail)
Goal: a locality-level Indian property price panel with a defensible construction.
- **IGR / state sub-registrar registration microdata** is the prize: transaction counts and
  consideration values, ideally by taluka/ward, monthly. This is the only genuinely point-in-time
  Indian property dataset. Maharashtra (IGR), Telangana (IGRS/Dharani), Karnataka (Kaveri), Delhi
  (DORIS), Tamil Nadu (TNREGINET), UP (IGRSUP), Gujarat (Garvi) all publish something.
- **NHB RESIDEX** full history, all cities, composite + city series.
- **RBI House Price Index** (10-city, quarterly) and RBI's Residential Asset Price Monitoring Survey.
- **Circle-rate / ready-reckoner / jantri histories by ward** — the denominator for everything, and
  the black-money incentive is measurable only with it.
- Construct, and document, a **hedonic or repeat-sales index** from registration microdata where the
  data supports it; where it does not, say so and fall back to median-price-per-sqft with an explicit
  composition control (the previous programme found China's national land series was contaminated by
  exactly this — a mix shift read as a price move).
- **GATE 0**: a locality-level panel exists, is sha256-manifested in `ingest/vault/india_property/`,
  has a written AUTHENTICATION.md, and its top-10 localities' 5-year changes reconcile to within a
  stated tolerance against at least two independent published figures. If GATE 0 fails, the project
  stops and reports what data is missing. **Do not proceed to modelling on asking prices.**

### PHASE 1 — THE FEATURE LIBRARY (the "100s of metrics")
Organise by causal channel, not by data source. Every feature carries: source, update frequency,
publication lag, geographic granularity, first available date, and **whether it is
point-in-time or revised** (a revised series used as a feature is lookahead — the desk has a booked
process note on exactly this error).

**A. Supply**
RERA project registrations, launches and completions by locality (state RERA portals: MahaRERA,
UP-RERA, TG-RERA, K-RERA all have searchable registries); unsold inventory and months-of-supply;
stalled-project counts; building-plan approvals; occupancy certificates; floor-space-index/TDR
policy changes; land-use conversion notifications; new municipal ward creation.

**B. Demand and demography**
Census 2011 (and 2027 when it lands) at ward level; SECC; UDISE+ school enrolment as a
household-formation proxy at district level; PLFS employment; EPFO/ESIC payroll additions by state
(monthly, a genuinely high-frequency demand proxy); migration proxies; marriage registrations;
electricity new-connection counts; LPG/water/sewer connections; vehicle registrations (VAHAN, open
and granular).

**C. Credit and affordability**
RBI DBIE housing-loan outstanding and disbursement; HFC/NBFC books; average ticket size; LTV
distributions; home-loan rates (7.10-8.45% as of 2025 after 125bp of cuts — verify, do not assume);
mortgage-to-GDP (~11-12%); price-to-income by city; EMI-to-income; the **carry spread** (gross yield
minus mortgage rate — currently −2.0pp to −5.0pp, *wider negative than China's* −0.9 to −1.3pp).

**D. Infrastructure — but see constraint 5**
Metro line status by station with **dated** milestones (approval / tender / construction start /
commissioning); NHAI/Bharatmala/expressway progress; airport status and **AAI monthly passenger
traffic** (a delivered-demand measure, not an announcement); port throughput; water and sewerage
network extension; power reliability. **Model announcement dates and completion dates as separate
features and test whether either has residual predictive power after the other.** That test is the
single most valuable experiment in the project.

**E. Satellite and alternative data — the genuine edge, because nobody has assembled it**
VIIRS night-lights (monthly, free, NOAA); Sentinel-1/2 via Copernicus and Google Earth Engine for
observed construction and built-up-area change; Bhuvan/ISRO; OpenStreetMap building footprints and
road-network growth; WorldPop; Overture Maps. **Observed construction from satellite is a supply
measure that leads every official statistic and is not in any price.** Build it.

**F. Governance, risk and quality-of-place**
CPCB air quality; NDMA/BMTPC flood and seismic hazard maps; Coastal Regulation Zone boundaries;
municipal property-tax collection efficiency (a proxy for civic capacity); ULB credit ratings;
crime statistics (NCRB); GTFS transit feeds where published; water-table depth (CGWB) — a real
constraint in Bengaluru and NCR.

**G. Policy and the tax wedge**
Stamp duty by state and its changes (Maharashtra's 2020-21 cut is a natural experiment nobody has
run properly); circle-rate revisions; the 2016-17 formalisation stack (demonetisation, Benami
amendment, RERA, GST, Section 269ST); GST rate changes on construction; PMAY allocations;
capital-gains and the breaks already registered as BR7/BR8/BR9 in `breaks-registry.md`.

**H. The macro overlay already booked by this desk** — do not re-derive: FUN-D8 monetary seasons,
the CU currency battery, CI-D1..D5 credit/inflation, DB-D1..D9 debt.

**GATE 1**: every feature in the library has all seven metadata fields populated, no feature is a
revised series used without a vintage stamp, and the panel's feature coverage by locality is
reported as a matrix (localities × features × first-available-date) so sparsity is visible rather
than silently imputed.

### PHASE 2 — WHAT ACTUALLY MOVES PRICES
Pre-register every design in `research/register/trial-ledger.md` with falsifiable bars BEFORE
computing anything. This is non-negotiable desk discipline and the register is append-only.
Suggested first battery (each gets its own entry):
- The **announcement-vs-completion** decomposition (constraint 5). Bars on residual predictive power.
- **Supply elasticity**: does locality-level completion volume predict subsequent price change, and
  with what sign and lag? China's answer was that starts collapsed 74% while completions held.
- **Credit channel**: does housing-credit growth lead locality prices, and what is its
  **false-alarm rate**? Register the false-alarm rate as a headline output, not a footnote — CN-D3's
  87.2% is the precedent.
- **The yield question that decides everything**: Indian city yield estimates split into two
  irreconcilable families — portal/broker micro-market surveys (Mumbai 2.0-4.0%) versus Global
  Property Guide's city cut (national blend 5.16%, Delhi/Kolkata 5.8-6.3%). CN-D2 puts historical
  peaks near 3.29% gross and troughs near 4.94%. **Which family is right decides whether Indian
  metros are priced at a historical peak or a historical trough.** Resolve it with registration
  microdata plus rental listings, and treat it as the project's highest-stakes number.
- **Satellite-observed construction** as a leading supply indicator, against official completions.
- **The formalisation natural experiment**: registration value-per-unit against circle rate through
  2016-17 and through Maharashtra's stamp-duty cut. The previous session's answer was "sideways, not
  crash — a volume effect, because the index-setting buyer was never the cash-dependent one"
  (launches −44% against sales −12%, prices decelerated 7-8%→3-4%/yr but never went negative).
  Test it properly at locality level.

**GATE 2**: at least one channel survives a purged, honestly-benchmarked walk-forward. Use
`quant/stats/` machinery (`cv.py`, `preprocess.py`, `dsr.py` for the trial-count deflation) — never
inline re-implementations. If nothing survives, that is a publishable result and the dashboard
becomes a state-classifier rather than a forecaster. Say so rather than fitting harder.

### PHASE 3 — THE ENGINE
- **Not** a point forecast. For each locality and each horizon (3y/5y/10y), classify the current
  observable state and emit the **historical forward distribution for comparable states**: median,
  p10, p90, n, and the share of comparable states that went on to fall ≥20%.
- Carry the base rates explicitly: median crash −32% over 5.5y; bust velocity ≈ boom velocity;
  post-1970 nobody sustained 20%/yr real; hot markets DO stay hot at five years (+9.65%/yr real
  after a 15%/yr window) while carrying ~2x crash odds. That last pair is the most actionable thing
  the desk knows: **ride-it-but-size-it, not in-or-out.**
- Deflate every claim by trial count via `census_n()`. The register is currently at 1,399 cells and
  rising; a Sharpe or hit-rate claim that ignores it is not admissible.

### PHASE 4 — THE DASHBOARD
Published artifact + committed copy in `docs/learn/artifacts/` + a README row (the preservation rule).
Requirements: locality → city → state → national drill-down; the evidence standard stated **on the
page's face**, with vault-grade and snippet-grade content visually separated (rows 64 and 65 do this
— follow them); every number carrying its source and as-of date; and the forward view presented as
distributions with sample sizes, never as a single number. Load the `artifact-design` skill before
writing it and the `dataviz` skill before the first chart.

## AGENT ORCHESTRATION

- **Max 3 concurrent** (CLAUDE.md rule 6). Subagent model policy is in CLAUDE.md — follow it.
- Each agent writes a cited dossier **to disk** and returns ≤200 words. Content must never pass
  through the orchestrator's context.
- Every research agent prompt must say: **do not call WebFetch**; two independent sources for any
  load-bearing number; tag every figure `[2-SOURCE]` / `[1-SOURCE]` / `[RECALL — unverified]`; state
  the as-of date; never invent a figure; and name what could not be sourced.
- **Watch for composition effects and units.** Carpet vs built-up vs super-built-up moves an Indian
  per-sqft figure 20-35% and can reverse a ranking. Circle rates and government auction prices are
  not market prices. The previous programme caught a Chinese land series whose average *rose* while
  every tier fell, purely on mix.
- Maintain `MANIFEST.md` (every task), `DISPATCH.md` (status per bundle) and name what you did NOT
  run rather than dropping it silently. That is what makes the multi-session scale-up honest.

## DISCIPLINE

Pre-register before running; interpretation written after the print; bars never moved after a print
(misses are recorded — there are many booked precedents); census append-only in `trial-count.md`;
both commit gates (`python3 -m pytest tests/ -q` and `python3 config/validator.py`, via the
pre-commit hook) before every commit; commit and push everything to the designated branch; no magic
numbers; free data only; every vault file sha256-manifested with two-pass AUTHENTICATION.md.

## START HERE, CONCRETELY

1. Read `CLAUDE.md`, `research/CONTRACT.md`, `research/frontier/india-property-plan.md`, and the
   five IN rows in `RUNSHEET.md`.
2. Write `research/frontier/india-engine-plan.md`: the phase plan above, adapted to what you find,
   with the honest agent/task arithmetic stated up front.
3. **Probe data availability before promising anything.** Spend the first agents hunting
   GitHub-hosted mirrors of NHB RESIDEX, IGR registration data, Census ward data, VIIRS night-lights
   and OSM India extracts — GitHub is the one open channel. Report what is actually reachable from
   THIS environment versus what needs a principal-machine pull, and put the latter on the RUNSHEET.
4. Then, and only then, pre-register Phase 0's construction design and run it.
5. Report GATE 0 honestly. If the target variable cannot be built from reachable data, say so
   plainly and deliver the acquisition list instead — that is a successful outcome for session one,
   and pretending otherwise wastes the whole programme.

One more thing, and it is the spirit of the desk: **the most valuable outputs of the last two
programmes were the negative findings** — that no adjustment multiplier for official Chinese data
exists, that the 64.5m empty-homes figure was disowned by its own source, that Indian REITs yield
below the sovereign, that leverage ratios missed Country Garden because presale liabilities were
invisible to them. Hunt for those as hard as for the positive ones, and publish them with equal
prominence.
