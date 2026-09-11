# HANDOFF PROMPT — THE INDIA REAL-ESTATE PREDICTION ENGINE (v4)
Written 2026-09-11 at the close of the IN programme, for a NEW Claude Code thread.
Paste everything below the rule. Self-contained: assumes the repo, assumes no memory of the
conversation that produced it.

**v4 supersedes v3.1.** It folds in the evidence pack's audit: the §4.1 censoring identity is
corrected to a behavioural/bunching problem with a one-number day-one diagnostic, the area-basis
constant is replaced by an explicit loading factor, and §11.5 adds the twelve research modalities
nobody has swept — three of which are uncensored Indian price series. Read
`research/register/india-realestate-evidence-pack.md` alongside this.

**v3 superseded v2.** It adds the principal's four scope decisions, the cost-drag calculation that
reframes the entire exercise, the rental-data route that may resolve the yield conflict, and the
project's own "what we will not build" boundary. **v3.1 adds §0.5: run this on the desktop app, not
on the web, because the web environment cannot reach any primary Indian source.**

---

You are joining **The Cycle Program** (`/home/user/claude-demo`), a quantitative desk run for a
single principal who also advises wealth clients. Read `CLAUDE.md` and `research/CONTRACT.md` first
— binding, and nothing here overrides them.

## §0 — THE PRINCIPAL'S SCOPE DECISIONS (settled; do not re-litigate)

1. **Purpose: all three at once** — he may *invest* directly, he *recommends* to clients, and he
   wants the *research authority*. So the engine has **one panel and three output layers** (§2).
2. **Coverage: DEEP, not wide.** 4-6 cities at true locality level on the first pass. Expand
   city-by-city afterwards. Do not build a shallow national map.
3. **Segments, in this priority order:** **residential** first → **office and shop (retail)** →
   **agricultural / plotted land** → **other commercial**. Get residential fully right before
   starting the next rung. Each rung is a separate target variable, not a column.
4. **Forecast form: state-conditional distributions ONLY.** No point forecasts, no headline central
   number. Per locality and horizon: median, p10, p90, sample size, and the share of comparable
   historical states that subsequently fell 20%+.

## §0.5 — WHERE TO RUN THIS: DESKTOP, NOT WEB (settled; the reason is egress)

**Run this project in the Claude Code desktop app on the principal's own machine.** Not in
Claude on the web, and not in a remote/cloud session. The reason is not preference, it is a
measured constraint: **this project is acquisition-bound, not compute-bound**, and the remote
environment cannot reach the data it is about.

- In the remote/web environment, `WebFetch` is **EGRESS-BLOCKED for every domain** (§6.1), and
  CLAUDE.md's own environment note already lists NSE/RBI/CCIL/Kaggle/HF/FRED as blocked. Only
  `WebSearch` snippets and **GitHub** (raw/LFS/git-proxy) are live. Every primary source in §7 —
  IGR Maharashtra, NHB Residex, RBI DBIE, data.gov.in, the municipal and Bhulekh portals,
  MahaRERA — is on the wrong side of that wall. A web session can *describe* the registration
  microdata; it cannot pull a single row of it.
- The desktop app runs with the machine's ordinary internet, so `ingest/pull_*.py` can actually
  execute. It can also do the three things the portals require and a sandbox cannot: hold a
  **session cookie / form-post flow** (IGR's search is not a static URL), drive a **real browser**
  against a JS portal, and retry a long paginated crawl over hours.
- Disk and persistence. A ward-level registration panel is plausibly multi-GB; the remote
  container has a fixed per-session allowance and is **reclaimed after inactivity**, so anything
  not committed is lost. Desktop keeps the working panel across days, which is what a
  multi-session programme (§6.2) needs.
- CLAUDE.md already classifies exactly this work as **"principal-machine runsheet pulls"**. This
  project is the largest such pull the desk has ever queued. Running it anywhere else contradicts
  the runsheet's own design.

**The split that actually works.** Desktop owns acquisition, the vault, manifests and the
authentication passes — Phases 0-1 end to end. Once a vault directory is committed with its
`AUTHENTICATION.md` and sha256 manifest, the **analysis, dossier and dashboard legs are
venue-neutral** and a web session is a fine place to run them (it reads the repo, fans out agents,
publishes the artifact) — that is precisely how the CN and IN programmes were built. Do not invert
it: never let a web session promise a pull.

**Desktop setup, once per clone.** Same branch discipline (`claude/funny-faraday-r3v4aj`);
`git config core.hooksPath .githooks` so the pytest + validator gate is machinery not memory;
`PYTHONPATH=<local repo path>` for every analysis script; substitute the local clone path wherever
this brief writes `/home/user/claude-demo`. Vault files large enough to strain git go to **LFS**,
never outside the manifest.

## §1 — THE CALCULATION THAT REFRAMES THE WHOLE EXERCISE

Do this first, properly, with registry-sourced rates. A prior session computed it on indicative
rates and it changes what the project is for.

Indian residential round-trip and holding costs, indicative:

| Component | Indicative |
|---|---|
| Stamp duty (state-varying) | 5-7% |
| Registration | ~1%, often capped |
| Brokerage on buy | 1-2% |
| Legal / diligence / misc | ~0.5% |
| **Entry subtotal** | **~9%** |
| Brokerage on sale | 1-2% |
| **Round-trip, ex capital-gains tax** | **~10.5%** |
| Property tax | ~0.6%/yr |
| Maintenance / society | ~0.8%/yr |
| Vacancy allowance | ~0.8%/yr |
| **Holding, 5 years** | **~11%** |
| **TOTAL 5-YEAR COST DRAG** | **~21.5%** |

Applied to the two readings of a "20% in 5 years" ambition:

- **20% cumulative** → net **−1.5%** = **−0.30%/yr nominal** = **−4.60%/yr REAL** at 4.5% CPI.
- **20% CAGR (148.8% cumulative)** → net 127.3% = **+17.85%/yr nominal**, +12.78%/yr real. Survives
  comfortably.
- **A Mumbai-like +48% over 5.5 years** → net 26.5% = **+4.81%/yr nominal ≈ +0.30%/yr real.**
  Essentially zero after costs.

And the two hurdles that follow:

- **Gross appreciation needed merely to BREAK EVEN over five years: 21.5%.**
- **Gross appreciation needed to match the desk's standing book (11.46%/yr = 72.0% cumulative):
  93.5%.**

**What this means for the project.** Indian residential property is a high-friction asset in which
only large moves survive costs. It follows that:
1. The **low reading of any "20%" target is unclearable** — it is negative in real terms after
   costs, so the engine must never present a gross appreciation figure without its net twin.
2. **The investment layer's real question is not "will prices rise" but "will they rise more than
   93.5% over five years, or is the capital better in the book?"** That is a far higher bar than
   any city screen implies, and it is the honest frame.
3. The **advisory layer's** most valuable output is therefore often *rent vs buy* and *is what you
   own overvalued* — questions where the cost drag argues for the client's existing position rather
   than a transaction.
4. **Every forward distribution on the dashboard must be published gross AND net.** Gross-only is
   the single most misleading thing this project could ship.

Replace the indicative rates above with registry-sourced, state-specific ones in
`config/costs.yaml` under a new `property_costs_india` block, fully provenanced
(`source`/`tier`/`confidence`/`changes_if`) exactly as `capital_gains_tax_india` is. The validator
enforces it.

**Property-specific tax, which differs from equity and is decision-relevant.** Long-term capital
gains on immovable property post-23-Jul-2024 are 12.5% without indexation, with a taxpayer
*election* to use 20% with indexation for property acquired before that date — so the after-tax
comparison against equity is asset-specific and vintage-specific. Rollover reliefs exist for
property and not for equity: **Section 54** (residential-to-residential), **54F**
(other-asset-to-residential), **54EC** (bonds). Those reliefs can dominate the whole return
calculation for a client who is rolling rather than exiting, and no property model that ignores them
is advisory-grade. Source them; do not assume; and do not give tax advice — model the mechanics and
flag that the client's own adviser confirms applicability.

## §2 — ARCHITECTURE: ONE PANEL, THREE OUTPUT LAYERS

Because the principal wants all three purposes, build once and project three ways.

**The panel (shared foundation).** Locality × month, per segment, with the dependent variable from
§4 and the feature library from §6.

**Layer R — Research / market intelligence.** The published dashboard: locality→city→state→national
drill-down, state classification, forward distributions gross and net, every number sourced and
as-of stamped. This is the artefact that establishes authority.

**Layer A — Advisory.** A repeatable **per-locality client brief** generated from the panel,
answering exactly three questions in client-safe language: *should I buy here* (state + forward
distribution + n + failure rate + net-of-cost hurdle), *is what I own overvalued* (its yield and
price-to-income against the international peak/trough bands), and **rent vs buy** (the local carry
spread against the local mortgage rate). Must carry a standing disclaimer and must never emit a
point forecast.

**Layer I — Investment.** The net-of-everything hurdle calculator from §1, per locality: the gross
appreciation required to break even, to beat inflation, and to beat the standing book — plus
**exit liquidity**, which most property analysis ignores entirely. Indian residential time-on-market
runs months to well over a year, and the prior programme could not identify a cash-flow-priced exit
buyer at all for Amravati or Ayodhya. Liquidity must be a modelled field, not a footnote: days-on-
market, transaction count per 1,000 units of stock, and the buyer-type mix where sourceable.

## §3 — WHAT WE WILL *NOT* BUILD (scope discipline; state this in the plan)

- **No automated valuation model (AVM) for individual properties.** That needs comparables the
  public data does not support and it is a different product.
- **No broker-grade comps tool, no lead generation, no listing scrape as a product.**
- **No point forecasts** (§0.4), no "top 10 cities to invest" ranking (that is marketing collateral
  and every portal publishes one).
- **No agricultural-land transaction recommendations.** The segment is in scope for *research*
  (rung 3) because the black-money and land-price questions live there, but its title risk,
  conversion risk and fraud exposure make it out of scope for a recommendation layer. The prior
  session's Dholera work found documented active fraud risk including a High Court land case.
- **No model with more features than its design registered.** The desk's own single-country kitchen
  sink exploded at **−389%** out-of-sample. Feature count is a pre-registered parameter.

## §4 — THE DEPENDENT VARIABLE: THE PROJECT'S CENTRAL PROBLEM

**There is no public repeat-sales or transaction-weighted house-price index for any Indian city.**
Every circulating "+X%" is an asking-price comparison; where both were obtainable, Ulwe asking ran
**25-30% above actual registered closings**. NHB RESIDEX is coarse, lagged, city-level. RBI's HPI is
10 cities, quarterly. **You cannot model a price series you have not built.**

**Build two separate residential indices, not one.** Primary (new-build, RERA-registered,
developer-sold, bank-financed, GST-bearing, price-capped in some states) and secondary (resale) have
different cash intensity, different price formation and different data sources. Pooling them creates
a composition series disguised as a price series. The prior programme's central black-money finding
— that the *index-setting buyer was never the cash-dependent one* — only becomes testable if the two
are separated.

### §4.1 — THE INTELLECTUAL CORE: UNDER-REPORTING IS AN IDENTIFIED ECONOMETRIC PROBLEM

> **CORRECTION, 2026-09-11, and read it before the rest of §4.1.** The censoring identity below —
> registered = max(true, circle rate) — was **refuted as a mechanical structure** by the evidence
> pack's audit (`india-realestate-evidence-pack.md` §6.2 #1). Stamp duty is charged on the *higher
> of* declared price or circle rate, which constrains the **tax base**, not the **declared
> consideration**: nothing mechanically stops a deed recording below the floor, because the duty is
> identical either way. The floor binds through the income-tax deeming provisions (Sections 50C /
> 43CA / 56(2)(x)) and their 5-10-20% tolerance band — an *incentive*, not a censoring rule. So the
> pile-up at the circle rate is a **behavioural equilibrium**, and a plain Tobit likelihood assigns
> **zero probability to any observation below the floor**, which is misspecification before any
> distributional concern. **Day-one diagnostic, and it is one number: the share of registered
> declarations strictly below the local circle rate.** If it is non-trivial, the model below is
> replaced by the bunching / notch-with-plateau family — which is a *better* model, reachable with
> the same data, and identified off the statutory tolerance-band changes. Everything else in §4.1
> (the threshold is observed, ward-level and time-varying; the share at the floor estimates
> under-reporting incidence) survives unchanged.

Read this twice. It is the best idea available on this subject and it converts a data-quality
complaint into a model.

- A transaction must register at **no less than the circle rate** (stamp duty is assessed on
  `max(declared value, circle rate)`).
- A buyer and seller splitting the price into declared-plus-cash rationally declare **exactly the
  circle rate** — declaring less buys nothing, declaring more costs duty.
- Therefore the registered value is a **left-censored observation of the true price, with a known,
  observable, time-varying, ward-level censoring threshold**: the circle rate itself.

A Tobit-type censored regression with an unusually good property — **the censoring point is
observed, not estimated.** Four testable consequences:

1. **The share of transactions registering at or within ε of the circle rate is a direct estimate
   of under-reporting incidence**, by ward and month. Nobody publishes this. It would be a genuinely
   new series and is arguably the single most publishable output of the project.
2. **The censored model recovers the latent price distribution** where a naive mean or median does
   not. A naive index is biased *toward* the circle rate precisely where cash intensity is highest —
   so it **understates** appreciation in exactly the localities that matter most.
3. **Circle-rate revisions are natural experiments and traps.** An upward revision makes previously
   censored transactions uncensored, so the registered mean jumps with **no change in true prices**.
   Maharashtra's ready reckoner sat **frozen 2019-22**; Gujarat revised jantri in 2023. Any index
   ignoring this prints a spurious price rise on a tax-administration event.
4. **The formalisation question becomes locality-testable.** Across the 2016-17 stack
   (demonetisation, Benami amendment, RERA, GST, Section 269ST) all-India price growth decelerated
   ~7-8%/yr → ~3-4%/yr but **never went negative**, while launches fell **−44%** against sales
   **−12%**. Verdict: a *volume* effect, not a price effect. Test it properly with the censored spec.

Cash intensity by segment, consistent ordering across sources, **no audited figure exists anywhere**:
land/agricultural highest (~40%+) → resale and premium → branded primary lowest (bounded by RERA's
70% escrow and bank underwriting). Two named cautions: Anarock's "down 75-80% since Nov 2016" covers
*housing* not all real estate, its own mechanism is **compositional** (branded developers gaining
share) rather than a re-measurement, and Anarock is commercially aligned with the developers it
credits; LocalCircles' prevalence figures rest on one self-selected online panel. Directional, not
measurements. Corroborating: Ayodhya deed prices ran **41% to 1,235% above circle rate** by 2023,
which cannot happen under pure circle-rate registration.

### §4.2 — THE RENTAL SERIES, AND THE ROUTE THAT MAY RESOLVE THE YIELD CONFLICT

The engine needs rents, not just prices — the carry spread is the spine of Layer A and Layer I.
Indian rental data is normally considered worse than price data. **But Maharashtra requires
registration of leave-and-license agreements**, which means a genuine *rental transaction* database
may exist for the state, with the same SRO geography as the price data. Probe this early and hard:
if it lands, it is the only place in India where price and rent come from the same registry on the
same geography, and it would let you compute a **transaction-based yield** rather than a
listing-based one.

**Why that matters more than any model.** Indian city yield estimates currently split into two
irreconcilable families: portal/broker micro-market surveys (Mumbai 2.0-4.0%, Hyderabad IT corridor
2.5-4.2%, Lucknow ~3%, Ahmedabad 3.9%) versus Global Property Guide's city cut (national blend
5.16%, Delhi/Kolkata 5.8-6.3%). The desk's international base rate (CN-D2) puts historical **peaks
near 3.29% gross** and **troughs near 4.94%**. **So the first family says Indian metros are priced
where markets historically peak; the second says where they historically trough.** A 2-3pp data
disagreement decides the entire India verdict. Resolving it is worth more than the model.

Also carry forward: India's carry spread runs **−2.0pp to −5.0pp**, **wider negative than China's**
−0.9 to −1.3pp, which is not the intuitive result. Home-loan rates are **7.10-8.45%** after 125bp
of cuts through 2025 — verify, do not assume 8-9%.

## §5 — THE LOCALITY UNIVERSE AND THE CROSSWALK

"Locality level" is meaningless until the unit is fixed. Use **Census 2011 town/village codes as the
spine** (the only exhaustive, official, hierarchically-nested geography: state → district →
sub-district → town/village). The other candidates each fail as a spine: **pincodes** (~19,300) are
postal routes that cross administrative boundaries and get revised; **municipal wards** are right for
circle rates and property tax but have no national registry and shift at delimitation; **SRO
jurisdictions** are the unit your dependent variable natively arrives in.

**Build the crosswalk (SRO ↔ ward ↔ pincode ↔ Census code) as a first-class deliverable and report
its match rate honestly.** Every downstream join depends on it and a silent 30% mismatch invalidates
everything. Expect this to be harder than the modelling. Target: **30-60 localities per city across
4-6 cities**, so roughly **150-350 localities** on the first pass — a number small enough to
reconcile individually and large enough to estimate on.

**Register the selection problem now.** Localities *enter* the panel endogenously — Ulwe was not a
market in 2010, Kokapet barely existed. An unbalanced panel whose entry is caused by the very
appreciation being measured is the EW-survivor artifact this desk has hit **five times** (SC-D4,
TECH-D3, MOM-D1, VAL-D2/D3, EQ-D1) in a new guise. Declare a one-way rule per design: a bias that
flatters growth localities makes a print *against* them admissible and a print *for* them
non-evidence-grade.

## §6 — CONSTRAINTS THE LAST SESSION PAID TO DISCOVER

**6.1 WebFetch is EGRESS-BLOCKED for every domain. WebSearch works. GitHub is open.** Tested
directly, and then MEASURED: a 37-endpoint `curl` probe on 2026-09-11 (`research/notes/
re-engine-sources/_PROBE.md`) reached **1 of 37** — the GitHub control. Every international
house-price source, every Indian official portal, and the whole free geospatial stack answered
`CONNECT tunnel failed, response 403` at the gateway. This is the measurement behind §0.5. ~20 agents each lost roughly a third of their budget to calls that cannot succeed —
**tell every agent never to call it.** GitHub raw/LFS/git-proxy IS reachable, so GitHub-hosted
dataset mirrors are the one live data channel. Hunt them hard.

**6.2 Agent economics — 1,000 agents in one session is arithmetically impossible.** Measured across
~30 research agents: **150,000-195,000 tokens each**. 1,000 agents ≈ **160-195 million tokens**
against a ~15 million session budget; one session supports **70-90 at quality**. The scale is
reachable only as a **multi-session programme with durable state on disk** — `MANIFEST.md` (every
task), `DISPATCH.md` (status per bundle), a completion ledger — so session N+1 resumes and counts
genuinely accumulate. Never fake scale with thin agents; 500 well-sourced answers across 20 agents
beat 500 thin ones across 200.

**6.3 Point forecasts are forbidden and the desk's own results say why.** The ER arc's pooled
expected-return equations fail OOS at every horizon once purged and honestly benchmarked;
single-country kitchen sinks exploded at **−389%**; CN-D3 found the best-known credit early-warning
indicator carries an **87.2% false-alarm rate** at 3 years; IN-D1 found **zero of 884 post-1970
five-year windows** across 18 countries ever cleared 20%/yr real appreciation.

**6.4 ANNOUNCEMENT MOVES THE PRICE; COMPLETION MERELY CONFIRMS IT.** Three agents found it
independently. Navi Mumbai airport: Panvel +76% since 2021, mostly **before the first flight**.
Jewar: Noida belt +142-158%/5y, mostly before flying. Delhi-Dehradun Expressway: **+23% in the nine
months before opening**. Samruddhi: corridor land ≈3.7× pre-completion. Completed MMR infrastructure
then yields only a smaller continuing 8-15%/yr premium. **Corollary: every public, dated feature is
already partly in the price.** A model built on announced infrastructure will look brilliant
in-sample and predict nothing. The residual edge lives in data nobody has assembled (§4.1's
under-reporting series, satellite-observed construction) or in genuine nowcasting.

**6.5 HOT MARKETS STAY HOT — my own mean-reversion prior MISSED, and this is the most actionable
thing the desk knows about property.** IN-D1: the next five years after a ≥15%/yr real window
returned **+9.65%/yr real**, +11.16% after ≥20%/yr. Momentum beats mean reversion at five years.
Those same windows carry **~2× crash odds**. So: **ride-it-but-size-it, never in-or-out.** Build the
engine to express that.

**6.6 Units and composition will destroy this project if you let them.** Carpet vs built-up vs
super-built-up moves an Indian per-sqft figure by a **loading factor L, psf ratio = 1 + L** — a
70-80% carpet ratio gives **+25% to +43%**, and Mumbai loading is reported at **40-50%**, so L runs
to **0.50** (the earlier "20-35%" constant was arithmetically wrong and is retired; evidence pack
§6.2 #2) — and it reverses rankings; RERA mandates carpet
since 2017 but older and broker data does not. Circle rates, jantri rates and government auction
prices are **not market prices**. The prior programme caught a Chinese national land series whose
*average rose* while *every tier fell* — a pure mix shift the source itself labelled 结构性上涨.
Every index needs an explicit composition control and a stated area basis.

## §7 — DATA SOURCE INVENTORY (probe reachability before promising anything)

For each: reachable-from-here / needs-principal-machine-pull; frequency; publication lag;
granularity; and **point-in-time or revised** (a revised series used as a feature is lookahead —
booked process note).

**A. The dependent variable.** State registration portals — Maharashtra **IGR**, Telangana
**IGRS/Dharani**, Karnataka **Kaveri**, Tamil Nadu **TNREGINET**, UP **IGRSUP**, Gujarat **Garvi**,
Delhi **DORIS**, Rajasthan **e-Panjiyan**, MP **SAMPADA**. Plus **NHB RESIDEX**, **RBI HPI** via
**RBI DBIE**, RBI's Residential Asset Price Monitoring Survey, MoSPI **eSankhyiki**; and
circle-rate / ready-reckoner / **jantri** portals with history. **Maharashtra leave-and-license
registrations** for the rental series (§4.2).

**B. Government open data, API-shaped.** **data.gov.in** (documented REST API, resource IDs, free
key — the highest-value probe target); **VAHAN** vehicle registrations (district, monthly);
**UDISE+** school enrolment (household formation); **EPFO/ESIC** monthly payroll additions;
**PLFS/NSSO** microdata; **Census 2011** tables; **SECC**; **MCA21** (developer entities); **GSTN**;
**NCRB**; **CPCB** air quality; **CGWB** groundwater (a binding constraint in Bengaluru and NCR);
**IMD**; **DILRMP / Bhu-Naksha / ULPIN** land records; and state **RERA** registries (MahaRERA,
UP-RERA, TG-RERA, K-RERA) — the best public supply data in India and badly under-used.

**C. Satellite and geospatial — the genuine edge, because nobody has assembled it for India.**
**NOAA VIIRS** night-lights (monthly, free, no key); **Copernicus / Sentinel-1 and -2** and **Google
Earth Engine** (free for research) for observed built-up change; **ISRO Bhuvan**; **OpenStreetMap**
via the **Overpass API**; **Overture Maps** (AWS Open Data); **WorldPop**; Microsoft and Google open
building footprints for India. **Observed construction from satellite leads every official statistic
and is in no price.**

**D. Infrastructure as delivered, not announced.** **AAI monthly passenger traffic** by airport;
**NHAI/Bharatmala/MoRTH** progress; **MoHUA** metro status with dated milestones; port throughput;
**Grid India (POSOCO)** daily load and **CEA** state electricity; **GTFS** feeds; ward-level water
and sewerage connections.

**E. Credit and markets.** **RBI DBIE** housing-loan outstanding and disbursement; HFC/NBFC books;
ticket size; LTV; rates; mortgage-to-GDP ≈ **11-12%** (this bounds how far formal credit can
substitute for cash); **SEBI REIT filings**; NSE/BSE realty indices.

**F. Risk and quality-of-place.** **NDMA / BMTPC** hazard atlas (flood, seismic); **Coastal
Regulation Zone** boundaries; municipal property-tax collection efficiency (civic-capacity proxy);
ULB credit ratings.

## §8 — THE FEATURE LIBRARY

Organise by **causal channel**, never by data source. Every feature carries eight mandatory fields:
source · frequency · publication lag · granularity · first-available date · **point-in-time or
revised** · area basis where applicable · **and the channel hypothesis it tests**. A feature without
a hypothesis is a degree of freedom and the register deflates for those.

Channels: **supply** (RERA launches/completions/stalled, approvals, OCs, FSI/TDR policy, land-use
conversion) · **demand and demography** (Census, UDISE+, PLFS, EPFO payrolls, VAHAN, utility
connections, migration proxies) · **credit and affordability** (loan growth, ticket size, LTV, rates,
EMI-to-income, price-to-income, carry spread) · **infrastructure split into announced-date and
completed-date features** (§6.4 — and *testing whether either has residual power after the other is
the single most valuable experiment in the project*) · **satellite-observed construction** ·
**governance and risk** · **the policy and tax wedge** (stamp duty and its changes — Maharashtra's
2020-21 cut is a natural experiment nobody has run properly; circle-rate revisions; the 2016-17
stack; BR7/BR8/BR9 in `breaks-registry.md`) · **the spatial channel** (neighbour-locality price
growth, distance-to-CBD, distance-to-metro-station, travel-time isochrones) · and **the macro
overlay this desk has already booked** — FUN-D8 monetary seasons, the CU currency battery,
CI-D1..D5, DB-D1..D9. Quote those; do not re-derive them.

**Locality prices are spatially autocorrelated.** Spillover is a real feature, *and* standard errors
computed without spatial clustering will be wildly overstated. Cluster on SRO or district.

## §9 — VALIDATION, AND THE HORIZON THAT CANNOT BE VALIDATED

Pre-register every design in `research/register/trial-ledger.md` with falsifiable bars **before**
computing anything. Use `quant/stats/` machinery — `cv.py` (purged walk-forward), `preprocess.py`
(winsorization bounds fitted on train only), `dsr.py`/`census_n()` (trial-count deflation; the
register stands at **1,399** cells). Never inline re-implementations (process note #6).

**Model class discipline.** Start with panel fixed effects and the §4.1 censored specification. Do
not start with gradient boosting — the desk's kitchen-sink finding (−389% OOS) is exactly what
happens. Feature count per design is a pre-registered parameter.

**The benchmark ladder — a model must beat all five or it is not a model:**
1. Random walk on real locality prices.
2. Local CPI ("prices track inflation").
3. The city or national index (does locality selection add anything over being in India?).
4. The desk's standing book at **11.46%/yr** — the actual opportunity cost.
5. **The same four, NET of the §1 cost drag.** A model that beats the book gross and loses net has
   not beaten anything.

**The 10-year horizon cannot be validated on India data, and the dashboard must say so.**
Registration microdata realistically starts ~2010-2013 — **at most one** non-overlapping 10-year
window, and overlapping windows are not independent. So: the **3-year** view can be honestly
validated on India data; the **5-year** weakly, with overlap flagged; the **10-year** must be
borrowed from the **cross-country panel** (CN-D1..CN-D5: 48 episodes, 18 countries, 150 years) as a
base rate and labelled as such. Anyone presenting a validated 10-year India forecast off a 13-year
panel is fitting noise.

**Carry the base rates into every forward view**: median crash **−32% over 5.5 years**; bust velocity
≈ boom velocity (**0.99×**, so no gentle-deflation discount exists); a bigger boom buys a **faster**
unwind, not a deeper one; yield compresses −0.83pp into a peak and expands +1.53pp to a trough;
equities lose **−13.7pp** of excess real return in the year after a housing peak, doubled if banks
break, essentially recovered by year five.

## §10 — PHASES AND GATES

**GATE 0 — the dependent variable.** Locality-level primary and secondary residential indices exist,
sha256-manifested in `ingest/vault/india_property/` with a two-pass AUTHENTICATION.md, stated area
basis, explicit composition control, the §4.1 censored treatment applied where circle rates are
available, and the top-10 localities' 5-year changes reconciled within a stated tolerance against
two independent published figures. **If GATE 0 fails, stop and deliver the acquisition list** —
that is a successful session-one outcome. Proceeding on asking prices is not.

**GATE 1 — the feature library and the crosswalk.** All eight metadata fields for every feature; no
revised series without a vintage stamp; a published coverage matrix (localities × features ×
first-available-date) so sparsity is visible rather than silently imputed; the crosswalk with its
match rate stated.

**GATE 2 — does anything survive?** At least one channel beats all five benchmarks in a purged
walk-forward with spatially-clustered errors, deflated by trial count. **If nothing survives, that
is a publishable result** — ship the state-classifier and nowcaster rather than fitting harder. The
prior programmes' most-cited findings were failures.

**GATE 3 — the three layers.** Layer R published; Layer A generating a per-locality client brief;
Layer I computing the net-of-everything hurdle and the liquidity fields.

**GATE 4 — reproducibility and freshness.** The whole engine regenerates end-to-end from one
command. Every published view carries an **as-of stamp** and a **stated refresh cadence**, because a
prediction dashboard goes stale and the desk has a precedent for marking such work **PERISHABLE**
(SNAPSHOT-1). Decide the cadence explicitly and say what goes out of date first.

## §11 — KILL CRITERIA (state them in the plan and honour them)

- Registration microdata unreachable for **≥3 of the chosen cities** → abandon the locality tier,
  deliver a city-tier engine, say why.
- Crosswalk match rate **<70%** → the locality join is untrustworthy; fall back to SRO-native
  geography and report in SRO units.
- Circle-rate histories unobtainable for **≥3 cities** → the §4.1 censored core cannot be built;
  report the naive index *with its bias direction stated* and put the pull on the runsheet.
- No channel beats the five benchmarks after the pre-registered battery → ship the classifier; do
  **not** extend the battery hunting for significance (exactly what the 87.2% false-alarm finding
  warns against).
- Any locality index whose 5-year change cannot be reconciled to two independent sources → drop that
  locality from the published panel rather than publish an unreconciled number.

## §11.5 — TWELVE THINGS NOBODY HAS SWEPT (evidence pack §7.1 — each needs its own registration)

Ranked by what they would change. **The first three are uncensored Indian price observations**,
which matters given how much of §4 is spent engineering around censoring.

1. **Listed-developer quarterly filings** — DLF, Macrotech, Godrej Properties, Oberoi, Prestige,
   Brigade, Sobha publish audited pre-sales value and volume, **average realisation per sqft by
   city**, launches, collections, inventory and net debt. Dated, audited, per-sqft, point-in-time,
   no evasion incentive, no notified floor. **The largest single omission.**
2. **Public land auctions** — CIDCO, MHADA, HUDA/HSVP, NOIDA, DDA, state industrial corporations.
   Published, dated, plot-identified, competitively bid. The clean series to calibrate any
   under-reporting model against.
3. **Distressed sales** — SARFAESI bank e-auction notices, IBAPI reserve prices. Address-level and
   dated, and the only place the *downside* of the distribution is observable.
4. **Demography and household formation** — headship rates, formation projections, internal
   migration, age structure. **The only variable class with a claim to ten-year forecastability, and
   currently absent — so the engine has nothing where its promised horizon actually lives.**
5. **Physical-climate risk** — flood, heat, groundwater, subsidence, air quality. Locality-
   discriminating, publicly mapped, genuinely forward-looking at ten years. **The desk already owns
   a vaulted climate dataset.**
6. **The developer incentive stack as a second wedge** — subvention/CLP plans, "stamp duty paid",
   floor-rise and PLC waivers, furnishing credits. It widens in downturns while the headline rate is
   defended, so a deed-based index understates exactly the drawdown you built it to see.
7. **Dubai Land Department** — free transaction-level microdata with an open API; heavy Indian
   participation and two documented crashes. The most India-relevant open-microdata regime.
8. **Litigation as an observable** — eCourts, NCLT/IBC real-estate admissions, RERA complaint
   orders. Free, dated, text-searchable; and the pack's own finding is that litigation, not
   regulation, throttled India's supply response.
9. **District-level credit** — RBI Basic Statistical Return, district × sector outstanding: the
   finest free credit grain in India. Plus the **2019 external-benchmark (EBLR) mandate** as the
   missing monetary-transmission break in the event calendar.
10. **NRI/FX demand and gold substitution** — the desk owns the currency battery and gold to 1833,
    and CI-D2 ranks gold above housing in high-and-rising inflation. **A weak-INR year is a testable
    conditioner on NRI-heavy localities, and SNAPSHOT-1 says India is in one now.**
11. **TDR markets and society-redevelopment optionality** — Mumbai TDR is a traded read on FSI
    scarcity; cessed-building redevelopment is a genuinely India-specific value source.
12. **The advisory and publication perimeter** — SEBI adviser perimeter, RERA agent provisions,
    disclaimer form. **The project can be complete, correct and unpublishable.** Answer it first;
    it is cheap now and expensive at GATE 3.

Also missing from §4's method menu: the **state-space / hierarchical-trend repeat-sales family**
(Francke; Schulz-Werwatz; Nagaraja-Brown-Zhao) — the one family built for "tens of transactions per
cell", which is the project's binding constraint.

## §12 — AGENT ORCHESTRATION

Max **3 concurrent** (CLAUDE.md rule 6); subagent model policy is in CLAUDE.md. Each agent writes a
cited dossier **to disk** and returns ≤200 words; content never passes through the orchestrator's
context. Every research-agent prompt must state: **never call WebFetch**; two independent sources for
any load-bearing number; tag every figure `[2-SOURCE]` / `[1-SOURCE]` / `[RECALL — unverified]`;
state the as-of date; never invent a figure; name what could not be sourced; and flag composition
effects and area basis explicitly.

**Spawn these four first, before the plan is finalised — they are go/no-go probes, not background
research:**
1. **Reachability probe** — every source in §7: reachable from THIS environment or not? On desktop
   (§0.5) this is a real probe with real answers — actually request each endpoint, record status
   code, robots/ToS posture, whether it needs a session or a form post, and the response shape. On
   web it degrades to a search-snippet inventory, which is the reason §0.5 exists. Output: a
   reachable/not table plus RUNSHEET rows.
2. **Registration-microdata feasibility** — for the 4-6 chosen cities, what does each state portal
   actually expose (fields, granularity, history, bulk vs per-document, rate limits)? Verdict on
   whether §4.1 is buildable.
3. **Circle-rate history hunt** — ward-level ready-reckoner/jantri histories for the chosen states.
   Without these the §4.1 core cannot be built: go/no-go.
4. **Maharashtra leave-and-license probe** (§4.2) — does a registered rental-transaction dataset
   exist, at what granularity, with what history? If yes, it may resolve the yield conflict that
   currently decides the entire India verdict, which makes it the highest-value single probe.

## §13 — DISCIPLINE

Pre-register before running; interpretation written after the print; **bars never moved after a
print** (misses are recorded — many booked precedents); census append-only in `trial-count.md`;
both commit gates via the pre-commit hook before every commit; commit and push everything to the
designated branch; no magic numbers; free data only; every vault file sha256-manifested with
two-pass AUTHENTICATION.md. Significant work ships as a published artifact + a committed copy in
`docs/learn/artifacts/` + a README row. Corrections go into published pages as **dated update
boxes** — superseded claims stay visible. Load the `artifact-design` skill before writing the
dashboard and `dataviz` before the first chart; consider the `artifact-capabilities` skill if the
dashboard should persist a locality watchlist or accept the principal's annotations.

## §14 — PRIOR WORK IN THIS REPO: READ, DO NOT REDO

- **`research/register/india-realestate-evidence-pack.md` — the companion to this brief, and the
  first thing to read after it.** Where this document says what to build, that one says what is
  already known: the international house-price forecasting literature and its out-of-sample
  failures, the country-by-country data regimes and the four templates India could copy, the India
  source estate portal by portal, the under-reporting econometrics, the free geospatial stack, a
  measured reachability table, and its own audit scoreboard of claims that did not survive
  fact-checking. Its §00 lists the sixteen desk prints any new property work must not contradict.
- **`research/cycles/fincycle-deep/partC-data.md`** — 460 lines of India property DATA ENGINEERING
  already done: RBI HPI provenance and its live rebase break, NHB RESIDEX's two dated breaks and
  its two structurally different price concepts (never blend them), housing credit, RERA, the
  registration/stamp-duty transaction side, the circle-rate honesty note, a vintage/point-in-time
  hazard table, and an explicit list of what cannot be measured free. **Do not re-derive this.**
- **`docs/cycles/13-real-estate.md`** — the folk 18-year property clock and Kuznets swings both
  FAIL this desk's pre-registered spacing test (109 peak spacings, 17 countries, median 14y, only
  45% in [14,22]y against a >=50% bar). The mechanism is kept, inside L12; the clock is dead. If
  anyone proposes an 18-year cycle feature, this is the answer.
- `research/frontier/india-property-plan.md` — incl. §0 where "grow >20% in 5yr" is decomposed
  (cumulative = 3.71%/yr = **−0.75%/yr real** before costs, and **−4.60%/yr real after** them).
- `research/notes/india-dossiers/` — **9 cited dossiers**: Mumbai inner and outer (8 micro-markets),
  Ahmedabad+Pune, Hyderabad+Lucknow, Amravati+Ayodhya, the candidate screen, black money,
  yields/REITs/developer leverage.
- `research/notes/china-dossiers/` — **20 dossiers**. The China bust is the closest available
  out-of-sample test of any India thesis. Use it that way. Specifically for the segment ladder:
  China's **strata-titled shops fell −40 to −60%**, the worst cycle-driven outcome found, which is
  directly relevant to rung 2 (office and shop); and **offices fell further than housing** there.
- Ledger: `IN-D1..IN-D2`, `CN-D1..CN-D5`, `CN-DOSSIER`, `SNAPSHOT-1`.
- Published: **India Property Atlas** (README row 65), **China Property Crash Atlas** (row 64). The
  new dashboard supersedes row 65's forward sections; it does not duplicate them.
- `RUNSHEET.md` — five IN rows and five CN rows already name the pulls this project needs. **That is
  your Phase 0 shopping list.**
- Two India findings to carry: **Kokapet land trades above its own buildings** (₹31,500/sqft raw land
  vs ₹11,900/sqft built) — the Chinese 面粉贵过面包 pattern in India; and **all four Indian REITs
  distribute below the 7.0% G-sec** (4.8-6.2%), three at 5-11% NAV discounts, with **no residential
  REIT existing at all**.

## §15 — START HERE

1. Read `CLAUDE.md`, `research/CONTRACT.md`, `india-property-plan.md`, the five IN RUNSHEET rows.
2. **Compute §1 properly** with registry-sourced state-specific rates and write the
   `property_costs_india` block into `config/costs.yaml`. This is an hour's work and it reframes
   everything downstream, so do it before any research.
3. Write `research/frontier/india-engine-plan.md` — the phases, gates and kill criteria above,
   adapted to what you find, with the agent arithmetic and multi-session accumulation structure
   stated up front, and the 4-6 chosen cities named with a reason.
4. Spawn the four §12 probes. **Do not promise a locality panel before probes 2 and 3 report.**
5. Pre-register Phase 0's construction design, including the §4.1 censored specification, then run it.
6. Report GATE 0 honestly either way.

**Final instruction, and it is the desk's actual character: hunt the negative findings as hard as
the positive ones and publish them with equal prominence.** The most valuable outputs of the last
two programmes were negatives — no adjustment multiplier for official Chinese data exists; the
64.5m empty-homes figure was disowned by its own source; Indian REITs yield below the sovereign;
leverage ratios missed Country Garden because presale liabilities were invisible to them. On this
project the most likely and most valuable negative is that **Indian locality price data cannot
support a forecast at all** — in which case say so with the evidence, ship the nowcaster, and put the
acquisition list on the runsheet. That is a far better outcome than a confident dashboard built on
asking prices.
