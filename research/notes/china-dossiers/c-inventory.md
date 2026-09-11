# C-INVENTORY — China's Unsold Housing, Empty Apartments, and the Construction Cycle

Agent dossier, China property programme (Half B), covering manifest bundles `b6-inventory-vacancy`
+ `b5-starts-completions` (10 questions, dispatch row 11). Compiled 2026-09-11.

**Tooling note (binding on how to read this dossier, per CLAUDE.md / `research/frontier/china-property-plan.md` §0a):**
WebSearch only — WebFetch is EGRESS_BLOCKED for every domain in this session and was not attempted.
Every figure below is drawn from WebSearch's indexed snippets, not from a directly-fetched and
re-read primary page. URLs are real and specific (many are `stats.gov.cn` press releases) but none
were independently re-opened — treat this as a step below the desk's normal [VERIFY] bar, per §0a's
stated ceiling for Half B. Corroboration rule applied throughout: `[2-SOURCE]` = two genuinely
independent search results/outlets converged on the number; `[1-SOURCE]` = only one outlet
surfaced it; `[RECALL — unverified]` = a claim that appeared but could not be corroborated, or is
explicitly rhetorical rather than measured. **This dossier's central task is separating what is
MEASURED from what is GUESSED** — see the Estimate Comparison Table and Q3 in particular.

## Headline findings

- **China has (at least) three genuinely different "inventory" numbers, not one.** (1) The
  official NBS stock of *completed, developer-held, listed-for-sale* homes was **390.88 million
  sqm (residential) / 753.27 million sqm (all commercial buildings)** at end-2024 `[2-SOURCE]`
  — call this ~4 million unsold NEW units. (2) The private, broader "for-sale" inventory that
  CRIC/E-house monitor across 100 cities (adds presale-pipeline supply, not just completed stock)
  implies a **27.4-month destocking cycle** as of November 2025 `[2-SOURCE]`. (3) The "empty
  apartment" literature (Q3) is measuring a **third, much larger population entirely** — occupied
  or purchased-but-vacant homes already sold to households, most of them never appearing in any
  developer inventory count at all. These populations should never be added together or used
  interchangeably, which is exactly what most popular coverage does.
- **The "how many empty apartments" question has no agreed answer and the true range of
  *credible* estimates is narrower than the popularly quoted 65-150 million.** The best-documented
  academic figure is Gan Li's China Household Finance Survey (CHFS): urban vacancy rate rose
  18.4%→21.4% from 2011 to 2017, implying "more than 50 million" empty urban homes `[2-SOURCE]`.
  The widely repeated "65 million" figure traces to a single, disputed 2010-era electricity-meter
  claim by a CASS-affiliated researcher that the state grid operator publicly denied `[2-SOURCE on
  the figure and the denial]`. A "tally of economists" extends the credible range to ~90 million
  `[1-SOURCE]`. **No credible, method-stated source for "130-150 million" was found in this search
  pass** — the likely origin of such round, very-high numbers is a September 2023 rhetorical
  remark by a retired statistics official that vacant homes could hold "3 billion people," which
  he himself called "a bit much" `[2-SOURCE on the quote]` and which is arithmetically absurd as a
  unit count (~1 billion units at 3 persons/household) — this is the paradigm case of a guess
  masquerading as a statistic.
- **New housing starts have collapsed almost exactly as advertised.** Full-year floor space newly
  started fell from a **2019 peak of 2,271.54 million sqm to 587.70 million sqm in 2025**, a
  **-74.1% decline** `[2-SOURCE — NBS year totals and an independently reported "~74% below 2019
  peak" figure agree almost to the point]`. Completions fell far less because of the explicit
  保交楼 ("guarantee delivery") policy campaign launched after the 2022 mortgage-boycott crisis,
  which directed bank financing to FINISH already-presold, already-paid-for units rather than to
  start new ones — completions only fell **-53.5%** over the same window (959.42 → 603.48 million
  sqm), roughly a third of the starts decline `[2-SOURCE]`.
- **"Rotten tail" (烂尾楼) unfinished-unit estimates range from ~8 million to "at least" 60 million
  units depending entirely on definition and date**, with the best cross-checked snapshot being
  ~225-231 million sqm of stalled projects at distressed/defaulted developers in mid-2022
  `[2-SOURCE, two independent methodologies — CRIC's developer-by-developer tally and E-house's
  "3.85% of the housing market" estimate — converge within 3%]`. Nomura's ~20 million unfinished
  presold-homes figure and Bloomberg Intelligence's ~48 million presold-homes-awaiting-completion
  figure are both narrower, differently-scoped estimates, not restatements of each other.
- **Electricity-meter and night-lights vacancy studies measure different populations and neither
  supports a clean national vacancy count.** The one genuinely peer-reviewed electricity-based
  vacancy study found in this search targets RURAL housing only (5.27%/8.69% in 2014/2017)
  `[1-SOURCE]` — a different population from any of the urban headline figures. Night-lights/
  satellite studies find the "ghost city" phenomenon is real but **confined to a specific, limited
  set of smaller cities** (not a national vacancy rate), because nighttime brightness measures
  whether a whole district got occupied, not whether an individual apartment is empty `[2-SOURCE]`.
- **Own arithmetic (Q5) on "years to clear" gives sharply different answers depending on which of
  the three inventory definitions above is used** — from under 6 months (narrow, completed-stock-
  only, own calculation) to ~2-2.7 years (broader "for-sale" cycle, three independent
  analysts agree) to >10 years (the entire under-construction pipeline, Hao Hong) — see Q5 for the
  full working. The gap between these numbers is not noise; it is the reader's own choice of
  denominator, made visible.

---

## ESTIMATE COMPARISON TABLE — "how many empty apartments does China have?"

| Estimate | Source | As-of / vintage | Method | Population measured | Credibility note |
|---|---|---|---|---|---|
| ~50 million+ (urban vacancy rate 21.4% in 2017, up from 18.4% in 2011) | Gan Li / China Household Finance Survey (CHFS), Southwestern Univ. of Finance & Economics | Survey years 2011/13/15/17; reported Dec 2017 | Household survey, 40,000+ households, 364 districts/counties, 29 provinces, nationally & provincially representative | Owner-reported vacant URBAN housing units (any reason, incl. investment holdings) | **Most credible of the headline figures** — peer-reviewed-adjacent academic survey infrastructure, published methodology, replicated across 4 survey waves showing a plausible trend. `[2-SOURCE]` |
| ~64.5-65.4 million ("64 million" in most English retellings) | CASS-affiliated researcher (surname Cao, sometimes attributed via economist Yi Xianrong) | Data reportedly ~2010, recirculated in press through the 2010s-2020s | Aggregated State Grid electricity-meter readings: urban meters with zero recorded consumption over a 6-month window | Meters reading zero — **not verified as vacant homes**, could include billing/meter errors, seasonal absence, non-residential meters | **Disputed and denied by the data source (State Grid) from the outset**; "up to" was reported as "at least" in translation; no published peer-reviewed methodology found. Treat as contested, not as a measured population. `[2-SOURCE on figure + denial]` |
| ~65-90 million | "Tally of economists' estimates" (aggregator framing, exact compiler not identified in search results) | Circa 2024 press summary | Unstated / synthesis of multiple prior estimates | Ambiguous — appears to blend several of the above populations | **Low transparency** — a range-of-ranges with no single stated method; useful only as "where informed opinion clusters," not as a number. `[1-SOURCE]` |
| ~48 million pre-sold homes awaiting completion | Bloomberg Intelligence | Reported ~2023-2024 | Aggregation of presale-registered units not yet delivered | PRE-SOLD, PAID-FOR, UNDER-CONSTRUCTION units — a fundamentally different population from "vacant completed homes" | Distinct and non-comparable to the vacancy estimates above; measures the "rotten tail" stock (see Q9), not vacancy. `[1-SOURCE]` |
| ~20 million unfinished pre-sold homes | Nomura (chief China economist) | Mid-2022 estimate, "homes pre-sold 2015-2020... $448bn to complete at ~50% avg progress" | Developer/project-level financial-completion tracking | Same "rotten tail" population as above, narrower cut | Also a rotten-tail (Q9) figure, not a vacancy estimate — frequently miscited alongside the vacancy numbers. `[1-SOURCE]` |
| "3 billion people" worth of vacant homes (~implies ~1 billion units at 3/household) | He Keng, former deputy head, National Bureau of Statistics | Remark at a Dongguan forum, September 2023 | None — an off-the-cuff public remark, explicitly citing "the most extreme" outside estimates and calling the figure himself "a bit much" | Unstated / rhetorical | **Not a measurement.** Arithmetically implausible as a literal unit count. This is very likely the ultimate source of any "130-150 million+" figure circulating in casual discussion, via loose paraphrase. `[2-SOURCE on the quote itself]` |
| ~14 billion sqm "vacant tumor" | Independent blogger ("Decode China" / Medium series) | Sept 2025 blog post | Author's own back-of-envelope estimation stack (survey rates x stock x new-district construction), not an institutional source | Unstated / conflated | **Excluded from the credible range.** Non-institutional, unreviewed, and internally implies a physically implausible share of China's total housing stock. Cited here only to document how far the public range has been stretched, and explicitly flagged `[RECALL — unverified, non-credible]`. |

**No figure in the 130-150 million range with a stated, checkable method was located in this search
pass.** The task brief's framing of "the range runs from roughly 65 million to 150 million" is
best read as: ~50-90 million is where the credible, method-stated estimates cluster (survey-based
and electricity-based, disputed as the latter is); the high end of "150 million" belongs to
rhetorical/derivative citations of the He Keng remark rather than to any independent measurement.

---

## STARTS AND COMPLETIONS BY YEAR (floor space, million sqm, NBS)

| Year | New starts, TOTAL | New starts, RESIDENTIAL | Completions, TOTAL | Completions, RESIDENTIAL | Under construction, TOTAL (year-end stock) |
|---|---|---|---|---|---|
| 2015 | not cleanly sourced this pass | — | figure found (~2,657) is inconsistent with adjacent years by >2x and is **not used** — flagged `[RECALL — unverified/likely wrong series]` | — | — |
| 2016 | 1,669.28 (+8.1%) | — | 1,061.28 (+6.1%) | 984.20 | — |
| 2017 | 1,786.54 (+7.0%) | — | 1,014.86 (-4.4%) | 882.42 | — |
| 2018 | 2,093.42 (+17.2%) | 1,533.53 (+19.7%) | 935.50 (-7.8%) | 660.16 (-8.1%) | 8,223.00 (residential 5,699.87) |
| 2019 | **2,271.54 (+8.5%) — PEAK** | **1,674.63 (+9.2%) — PEAK** | 959.42 (+2.6%) | 680.11 (+3.0%) | 8,938.21 (+8.7%) |
| 2020 | not fully captured this pass (partial: Jan-Nov total 1,473.44, -2.7%) | 1,643.29 (-1.9%) | not fully captured (partial: Jan-Nov total 591.73, -7.3%) | 912.18 (-4.9%, full-year residential figure reported) | not captured |
| 2021 | 1,988.95 (-11.4%) | 1,463.79 (-10.9%) | 1,014.12 (+11.2%) | — | 9,753.87 (+5.2%; residential 6,903.19) |
| 2022 | 1,205.87 (-39.4%) | 881.35 (-39.8%) | not captured directly | — | 9,049.99 (-7.2%) |
| 2023 | ~954-960 (derived from 2024's -23.0% YoY off 738.93; NOT a directly quoted full-year total) | — | 825.0 (scope ambiguous — likely residential; -X% not captured) | — | ~8,400 (derived, not directly quoted) |
| 2024 | 738.93 (-23.0%) | — | 737.43 (-27.7%) | — | 7,332.47 (-12.7%) |
| 2025 | **587.70 (-20.4%)** | 429.84 | **603.48 (-18.1%)** | — | Jan-Oct 2025 partial: 6,529.39 (-9.4%) |

**2019 peak → 2025: starts -74.1% (total), -74.3% (residential); completions -37.1% (total, 2019→2025)
but note completions actually kept rising through 2021 (post-2019 they were 1,014 in 2021, ABOVE the
2019 figure) before falling — completions did not begin their real decline until 2022-2023, roughly
2-3 years after starts peaked, exactly the lagged relationship the 保交楼 discussion in Q7 explains.**
`[2-SOURCE]` on the -74% starts figure specifically (own arithmetic from NBS year-totals, and an
independently reported "~74% below 2019 peak" claim in December 2025 press coverage, converging to
within half a point).

Gaps in this table (2015 full-year starts; 2020/2022/2023 full totals for some columns) reflect
search-budget limits, not a claim that the data doesn't exist — NBS publishes it, and the RUNSHEET
should route any exact vault-grade retrieval through a proper principal-machine pull rather than more
WebSearch passes.

---

## Q1. Unsold housing inventory: official vs. private, sqm/units/months

**Official (NBS "floor space of commercial buildings for sale," 待售面积)** — this measures
**completed housing that developers have finished, listed, and not yet sold**, nationwide:
- End-2023: 672.95 million sqm, +19.0% YoY `[1-SOURCE]`
- End-2024: **753.27 million sqm (all commercial building types), +10.6% YoY; of which residential
  buildings for sale = 390.88 million sqm** `[2-SOURCE for the 753.27 total figure, 1-SOURCE for
  the residential-only 390.88 split]` — residential-specific inventory grew +16.2% YoY on this
  reading.
- 2025: residential unsold inventory rose a further +2.9% (vs +18% in the 2023→2024 step, i.e. the
  RATE of inventory accumulation slowed sharply) `[1-SOURCE]`; by end-March 2026 the national
  unsold-commercial-housing floor area fell -0.1% YoY, "the first such decline in 52 months"
  `[1-SOURCE, Xinhua/scio.gov.cn]` — the first tentative sign of the inventory cycle actually
  turning, though one data point.

**Units conversion**: using ~90-100 sqm as a typical new-apartment size (average private-apartment
size across Beijing/Shanghai/Shenzhen is cited at 88-98 sqm `[1-SOURCE]`), the end-2024 official
residential-unsold stock of 390.88 million sqm implies **roughly 3.9-4.3 million UNSOLD NEW UNITS**
— a figure that sounds almost reassuring next to the 65-90 million "empty apartment" range, and the
gap is exactly the point: these are different populations (see headline findings and the table).

**Private/broader inventory reads** (a materially larger population — includes presale-registered
supply that NBS's "completed and for sale" measure excludes):
- CRIC/Shanghai E-House Real Estate Research Institute's 100-city monitored destocking cycle:
  **27.4 months as of November 2025** (tier-1: 17.1 months; tier-2: 22.6 months; tier-3/4: 40.3
  months), against a "healthy" norm the same reporting frames as 12-14 months `[2-SOURCE]`. This
  cycle fell to 21.3 months by January 2025 after September 2024 stimulus, then rose again through
  2025 `[1-SOURCE]`. Morgan Stanley's own estimate has the national figure trending to 31-32 months
  by December 2025 `[1-SOURCE]`.
- Bloomberg/Chinese-researcher compilation: unsold stock across 100 major cities = 511.8 million
  sqm at "end of February" (year of that snapshot not cleanly pinned down in the search snippet)
  `[1-SOURCE]`.
- Nomura's own broader inventory estimate is reported at roughly **2.6 billion sqm** `[1-SOURCE]`,
  and a separate mention of "2.52 billion sqm as of end-July 2024" `[1-SOURCE]` is very likely the
  same underlying Nomura construction reported at two different moments — flagged as **NOT
  independent corroboration of each other** even though they agree closely. This measure is roughly
  3.5x the official residential-for-sale figure, consistent with it counting the broader
  presale-plus-completed pipeline rather than completed stock alone.

**Months of supply, stated directly by analysts** (see Q5 for the arithmetic underlying these):
Hao Hong (GROW Investment Group) puts existing (completed) inventory clearance at "about two
years" at the current sales rate, and the FULL under-construction stock at "more than 10 years"
`[1-SOURCE]`; Goldman Sachs frames saleable inventory as "more than two years of demand" as of
end-2024 `[1-SOURCE]`. These roughly bracket the CRIC 27.4-month figure, which is reassuring
internal consistency across three independent institutions on the BROADER inventory measure.

## Q2. The Beike Research Institute 2022 vacancy survey

Published by Beike (贝壳, KE Holdings' research arm) on **5 August 2022**. Findings, as originally
reported: average housing vacancy rate across **28 major/mid-tier cities = 12%**, rising
monotonically with city tier — **tier-1 average 7%, tier-2 average 12%, tier-3 average 16%**
`[2-SOURCE, English + Chinese sources converge]`. Highest individual cities: **Nanchang, Langfang,
and Foshan, all above 15%**; lowest: **Shenzhen, Beijing, and Shanghai, all below 7%** `[2-SOURCE]`;
a broad middle band (Xi'an, Zhengzhou, Kunming, Hefei, Wuxi, etc.) sat 10-15%.

**Method**: Beike surveyed its own senior real-estate agents (three-plus years' tenure "on the
platform"), who assessed properties in their own patch/neighborhood coverage area. **A home was
classified "vacant" if it had been unoccupied for three consecutive months or more** — an
agent-judgment proxy, not a metered or administrative measure `[2-SOURCE]`.

**Controversy**: the report drew wide public debate within days of release — commentary noted
China's rate compared unfavourably (i.e., HIGHER) than several developed-country reference points
cited in the report (US, Canada, France, Australia, UK) `[1-SOURCE]`. Beike then **published an
apology/retraction on its WeChat account**, stating the report "should have been internal research
material," and that the methodology led to inaccurate data: survey responses showed deviation,
"the samples and procedures were not standardized enough," coverage was incomplete, and some data
was collected incorrectly; specifically, Beike said the three-consecutive-month vacancy threshold
"does not fully reflect the real situation" `[2-SOURCE, English + Chinese sources converge on the
retraction language]`. Beike did not, in the retraction, offer a corrected alternative figure — the
report was effectively withdrawn rather than revised.

## Q3. The "how many empty apartments" estimates: 65-150 million, by method

See the Estimate Comparison Table above for the full breakdown. Summary of the method-honesty
finding the task specifically asked for:

- The single most methodologically defensible estimate is **Gan Li's CHFS household survey**
  (~50 million+, from a 21.4% urban vacancy rate as of 2017, up from 18.4% in 2011) `[2-SOURCE]` —
  a genuine survey instrument with a stated, replicated sampling frame (40,000+ households, 364
  districts, 29 provinces).
- The most widely repeated figure — **~64.5-65.4 million, rounded to "65 million" or "64 million"**
  — rests on a single electricity-meter claim from a CASS-affiliated researcher that **the data
  provider (State Grid) itself has publicly disputed**, and for which no peer-reviewed methodology
  was located `[2-SOURCE on both the figure and the dispute]`. It should be reported as contested,
  not as an established fact, however often it is repeated as one.
- The **90 million** upper bound and the vaguer "65-90 million... could be as many as 90 million"
  framing trace to an unspecified "tally of economists" `[1-SOURCE]` — useful as a sense of where
  informed opinion clusters, not as a measurement with a stated method.
- **No source for "130-150 million" with any stated method surfaced in this search.** The likely
  real-world origin of numbers in that range is loose paraphrase of He Keng's September 2023 "3
  billion people" remark — which was itself an unsourced rhetorical aside, self-qualified by its
  own speaker as excessive, and arithmetically absurd taken literally (implying roughly 1 billion
  housing units, more than triple the entire estimated national housing stock, see Q1) `[2-SOURCE
  on the quote, 0-SOURCE for anyone converting it into a serious "150 million units" estimate]`.
- **Distinct populations warning, restated**: developer-unsold NEW inventory (~4 million units,
  Q1), pre-sold UNFINISHED units awaiting construction (~8-60 million depending on source, Q9),
  and OCCUPIED-OR-PURCHASED-BUT-EMPTY homes (the 50-90 million range here) are three non-overlapping
  (or only partially overlapping) populations. A single home purchased as a store of value and
  visited twice a year belongs only in the third category; a rotten-tail shell belongs only in the
  second; an as-yet-unsold new condo in a developer's inventory belongs only in the first.

## Q4. Electricity-meter and night-lights vacancy studies

**Electricity meter, national/urban** — the ~64.5-65.4 million figure (Q3) is the only
national-urban electricity-based estimate found, and it is journalistically sourced, disputed by
the utility itself, and has no traceable peer-reviewed publication `[2-SOURCE on the dispute]`.

**Electricity meter, rural, peer-reviewed**: "Estimating Housing Vacancy Rates in Rural China Using
Power Consumption Data" (published in *Sustainability*, 2019, doi 10.3390/su11205722) piloted a
power-consumption proxy for **RURAL** housing specifically, using 2014 and 2017 data, and found
vacancy rates of **5.27% (2014) and 8.69% (2017)**, with underutilization around 10% `[1-SOURCE]`.
This is a genuinely different, and far lower, population and figure than any of the urban headline
numbers — rural houses are typically owner-occupied-or-empty due to migration, not
investment-vacant, a structurally different phenomenon.

**Night-lights/satellite studies** (academic, multiple):
- An early approach (Yao & Li, 2011) used 2009 DMSP-OLS nightlight brightness against per-sqm
  housing prices as a crude vacancy proxy; verification against population data showed high
  variance and the approach is regarded as inconclusive `[1-SOURCE]`.
- A more developed study, **"Mapping China's Ghost Cities through the Combination of Nighttime
  Satellite Data and Daytime Satellite Data"** (MDPI *Remote Sensing*, 2018, vol. 10, issue 7,
  article 1037), combined DMSP/OLS nighttime data with a daytime Normalized Difference Built-up
  Index to track newly built areas' "darkness" over time — sustained decline in nighttime light
  after construction indicates a deserted, vacant-or-unfinished area. **Finding: the ghost-city
  problem is real but confined to a specific, limited set of smaller cities** (roughly 22-25 in
  different framings of the paper's two study groups), not a nationwide phenomenon `[1-SOURCE]`.
- A related paper, **"Urbanization that hides in the dark – Spotting China's 'ghost neighborhoods'
  from space"** (*Landscape and Urban Planning*, ~2020), uses a similar nighttime-lights approach at
  the neighborhood level `[1-SOURCE]` — corroborating, from a second independent research group,
  that the nightlight method is viable for identifying SPECIFIC deserted areas but not for producing
  a national vacant-unit count `[2-SOURCE on the "confined/limited, not national" conclusion across
  the two papers]`.

**Limitations, stated plainly**: night-lights/satellite methods measure whether a BUILT-UP AREA
(district, new town, block) is populated at all — they cannot see whether any INDIVIDUAL apartment
within an otherwise-occupied building is empty, so they systematically undercount ordinary
unit-level vacancy (an empty investment unit in a lit, occupied building is invisible to this
method) while being well-suited to the specific "brand-new ghost district" phenomenon. Electricity
methods have the opposite problem: metering can in principle see unit-level vacancy, but the only
national-scale claim rests on unverified, denied data, while the one peer-reviewed application
found targets rural housing, a different question entirely.

## Q5. Years of current sales to clear the inventory — arithmetic shown

Three different answers depending on which Q1 inventory measure is used as the numerator. All
three are shown, deliberately not reconciled into one number, because they answer different
questions.

**(a) Narrowest — NBS completed-and-listed residential stock only, own calculation:**
- End-2024 residential floor space for sale: **390.88 million sqm** (Q1, `[2-SOURCE]`-adjacent).
- 2024 residential sales, DERIVED: 2025 full-year residential sales were reported at 732.99 million
  sqm, down 9.2% YoY `[1-SOURCE]` → implied 2024 residential sales = 732.99 / (1 − 0.092) ≈
  **807.4 million sqm** (own arithmetic, not directly quoted).
- **390.88 / 807.4 ≈ 0.48 years ≈ 5.8 months.** This is the narrowest possible reading and is
  almost certainly an underestimate of the real clearing time, because it divides a completed-stock
  snapshot by a sales rate that itself draws down a much larger effective pipeline (see (b)).

**(b) Broader — the CRIC/E-house "for-sale inventory" cycle, directly quoted, not computed by this
dossier**: **27.4 months (≈2.3 years) as of November 2025**, tier-1 17.1 months, tier-2 22.6
months, tier-3/4 40.3 months `[2-SOURCE]`. This measure evidently includes presale-registered
supply beyond the NBS "completed" stock, which is why it is roughly 4-5x longer than (a). It
brackets closely with Hao Hong's independently stated "about two years" for existing inventory and
Goldman Sachs's "more than two years of demand" `[1-SOURCE each]` — three separate institutions
landing in the same 2-2.7-year neighborhood on what appears to be a comparably broad definition, a
reasonable degree of convergence.

**(c) Broadest — the entire under-construction pipeline, not just for-sale supply:**
- Total floor space under construction, end-2024: **7,332.47 million sqm** (Q8) `[2-SOURCE
  adjacent]`. If residential is assumed to hold roughly the same ~70% share of under-construction
  stock as it did in 2021 (6,903.19 / 9,753.87 = 70.8%, the latest year both figures were directly
  reported `[1-SOURCE]`), residential-only under-construction stock ≈ 7,332.47 × 0.708 ≈ **5,191
  million sqm** (own estimate, ratio carried forward — flagged as an assumption, not a reported
  figure).
- 5,191 / 807.4 (2024 residential sales pace, from (a)) ≈ **6.4 years.**
- This own estimate is materially SHORTER than Hao Hong's independently stated **"more than 10
  years"** for the same under-construction concept `[1-SOURCE]`. The two are not reconciled here —
  plausible reasons for the gap include Hao Hong assuming a further-declining future sales pace
  (rather than holding 2024's pace constant, as this dossier's calculation does), a different
  residential-share assumption, or a broader definition of "under construction" that includes stock
  not yet approved for presale. **This divergence is reported honestly rather than forced to agree.**

**Net read**: "how many years to clear China's housing" does not have one right answer — it has (at
least) three right answers to three different questions, ranging from under half a year (completed
stock only) to two-plus years (the broader for-sale pipeline, three-way convergence) to a decade-
plus (the entire construction pipeline, one analyst's figure, directionally plausible but not
independently replicated in this search).

## Q6. New starts by year, 2015-2025, and the collapse from peak

See the Starts and Completions table above for the full year-by-year series. Headline: **floor
space newly started peaked in 2019 at 2,271.54 million sqm (total) / 1,674.63 million sqm
(residential), and fell to 587.70 million sqm (total) / 429.84 million sqm (residential) in 2025**
— a **-74.1% total / -74.3% residential** decline from peak to 2025 `[2-SOURCE — this dossier's own
arithmetic from full NBS year-totals matches, to within half a percentage point, an independently
reported "annual starts ~74% below the 2019 peak" figure from December 2025 press coverage]`. 2025
starts are explicitly reported as **the lowest level since at least 2000** `[1-SOURCE]`. The decline
was not smooth: 2018-2019 were still growth years (+17.2%/+8.5%), 2020 dipped only modestly
(pandemic-era, residential -1.9%), 2021 fell a further -11.4%, then the collapse accelerated sharply
in **2022 (-39.4%)** — the year of the Evergrande-driven confidence crisis and the mortgage-boycott
episode — before continuing to fall in 2023 (-implied ~2%), 2024 (-23.0%) and 2025 (-20.4%).

## Q7. Completions by year, and why they held up while starts collapsed (保交楼)

Completions fell far less than starts over the same window: **959.42 million sqm (2019) → 603.48
million sqm (2025), a -37.1% decline**, versus starts' -74.1% `[2-SOURCE]`. Completions did not even
begin declining in step with starts — **2021's completions (1,014.12 million sqm) were actually
ABOVE the 2019 level**, and the real completions decline only set in from 2022-2023 onward, roughly
2-3 years after starts had already turned down `[2-SOURCE, derived from the table]` — consistent
with a multi-year construction lag (units started ~2019-2020 were still being finished in
2021-2022).

The explicit mechanism cited for completions being defended relative to starts is the **保交楼
("guarantee delivery of homes") campaign**, launched after the second half of 2022 when developer
financial distress began directly threatening the delivery of already-presold, already-paid-for
units (the period that also produced the 2022 mortgage-boycott movement, cross-referenced to the
broader China programme) `[2-SOURCE]`. Concretely: the PBOC set up a **200 billion yuan relending
facility for banks by 31 March 2023** specifically to support 保交楼 project completion `[1-SOURCE]`;
this was layered onto later, larger "white list" project financing — by October 2024, approved
loans for white-list projects had reached **2.23 trillion yuan (~$313bn)**, expected to exceed
**4 trillion yuan** by end-2024 `[1-SOURCE]`. The policy logic is explicit: rather than start new
projects (which the market has no appetite to absorb), direct financing to FINISH units households
have already paid for — which is exactly why completions decoupled from and outlasted starts.

## Q8. Floor space under construction: the stock, and years of sales it represents

Total floor space under construction (year-end stock, real-estate-development-enterprise measure):
**8,223.00 million sqm (2018) → 8,938.21 million sqm (2019) → 9,753.87 million sqm (2021, +5.2%) →
9,049.99 million sqm (2022, -7.2%) → 7,332.47 million sqm (2024, -12.7%)**, with a partial
January-October 2025 reading of **6,529.39 million sqm (-9.4% YoY)** `[2-SOURCE across the series]`.
The stock peaked around 2021 (~9.75 billion sqm) — two years AFTER starts had already peaked in
2019, because "under construction" is a stock concept that only turns over once completions
outpace new starts, which did not happen until the 2022+ collapse in starts overtook completions.

**Years of sales represented**: see Q5(c) for the full working — using a 2024 end-year residential-
share-adjusted estimate of ~5,191 million sqm against a ~807 million sqm/year residential sales
pace, this dossier's own calculation gives **~6.4 years**; Hao Hong's independently stated figure for
the same concept is **"more than 10 years"** `[1-SOURCE]`. Both point the same direction — the
entire construction pipeline represents multiple YEARS, not months, of demand at the current
depressed sales pace — without this dossier claiming false precision on the exact multiple.

## Q9. "Rotten tail buildings" (烂尾楼): the range of estimates

Estimates vary by an order of magnitude depending on unit (sqm vs. individual units) and vintage:

- **~8 million unfinished homes**, from stalled projects covering "2.7 billion square feet (250
  million square meters)" per a Chinese financial portal (Sina) compilation `[1-SOURCE]`.
- **~20 million unfinished pre-sold homes**, per Nomura's chief China economist, alongside an
  estimate that **$448 billion** would be needed to complete homes pre-sold 2015-2020 assuming
  ~50% average construction progress (mid-2022 estimate) `[1-SOURCE]`.
- **~225-231 million sqm of stalled projects at distressed/defaulted developers, mid-2022** — this
  is the best cross-checked figure in this dossier: **CRIC's developer-by-developer tally
  (Sunac 60 million sqm, Evergrande 53 million, Greenland 26 million, plus eight further distressed
  developers) totaled 225 million sqm**, while **Shanghai E-House Real Estate Research Institute
  independently estimated stalled projects at 3.85% of the housing market ≈ 231 million sqm** for
  the same period — **two different methodologies converging within 3% of each other**
  `[2-SOURCE, genuinely independent methods]`. Note this is a SQM figure tracking specific
  distressed developers, not a nationwide units estimate — it will understate the true "rotten
  tail" population to the extent smaller/regional developers outside the tracked distressed-name
  list also have stalled projects.
- **~48 million pre-sold homes awaiting completion**, per Bloomberg Intelligence (vintage
  2023-2024) `[1-SOURCE]` — a considerably larger units figure than Nomura's ~20 million, on an
  unstated methodology difference (likely a broader "awaiting completion" definition that includes
  merely-delayed-but-progressing projects, not only fully stalled ones).
- **"At least 60 million housing units"** incomplete-or-abandoned, per one more alarmed press
  framing `[1-SOURCE]` — could not be corroborated against a second independent source in this
  pass; treat as an upper-bound claim, not a confirmed figure.
- **"120 million paid-in-full homes unfinished or not yet started"**, from a single independent
  Substack analysis `[RECALL — unverified, non-institutional source, not corroborated]` — included
  only to document the range actually circulating publicly, explicitly not treated as credible.

**Read**: the credible, cross-checked core of the rotten-tail range is **~200-230 million sqm** of
stalled projects at named distressed developers as of mid-2022 (two-source agreement), translating
to somewhere in the **8-48 million UNITS** range depending on whether the count is restricted to
fully-stalled projects (Nomura's ~20 million) or extended to all delayed pre-sold homes (Bloomberg
Intelligence's ~48 million). Claims above ~60 million units are not corroborated in this search pass.

## Q10. Construction-sector employment and the migrant-worker consequence

Before the crisis, **real estate and construction together are estimated to have supported roughly
70 million jobs** across China `[1-SOURCE]`. Within the migrant-worker population specifically
(China's ~300 million-strong rural-to-urban migrant workforce, the group most exposed to
construction-site employment):
- Construction's share of the migrant workforce fell from **22.3% (2014) to 15.4% (2023)**, with
  **more than 15 million migrant laborers leaving the construction industry over 2014-2023**
  `[1-SOURCE]`.
- Migrant workers in construction specifically **dropped by 6.5 million in 2023 alone (vs. 2022)**
  `[1-SOURCE]`.
- The decline continued into 2024: total rural migrant workers rose modestly (+0.7% to just under
  300 million), but construction's share fell further to **14.3%**, described as a **16-year low**,
  down from **19% as recently as 2021** (the year the property slump began) `[1-SOURCE]`.
- Total construction-enterprise employment (a broader measure than migrant-specific figures) stood
  at **~50.44 million in 2023** `[1-SOURCE]`, though this headline figure alone does not net out the
  offsetting migrant-outflow trend above — the two series measure overlapping but not identical
  populations (all construction employees vs. the migrant subset), and should not be treated as
  contradicting each other.
- A demographic dimension compounds the economic one: multiple sources describe an **aging
  construction workforce** with limited retirement provision, as younger migrant workers
  increasingly avoid the sector `[1-SOURCE, cross-referenced across two independent outlets
  covering the same underlying phenomenon — treated here as `[2-SOURCE]` on the qualitative
  finding, `[1-SOURCE]` on any specific figures within it]`.

**Read**: a ~70% collapse in starts (Q6) plausibly explains a meaningfully smaller (roughly
one-third) decline in the construction-linked migrant workforce share (22.3%→14.3% of migrants, or
about a 36% relative decline in construction's SHARE of migrant employment, not a 70% decline in
absolute construction employment) — consistent with completions (Q7) being defended by policy and
with construction activity on the existing under-construction stock (Q8) continuing even as new
starts stopped, cushioning the employment shock relative to the starts collapse alone.

---

## Gaps and cautions

- **Verification ceiling, stated once for the whole dossier**: every figure above came from
  WebSearch snippets only; WebFetch was not available and no primary page was directly re-read.
  Snippets can be stale, mis-dated, or reworded by the search aggregator — several instances of
  exactly this problem were caught and flagged inline above (the ambiguous-year H1 rental-yield-
  style date issues in sibling dossiers; here, the 2015 completions figure that was rejected as
  inconsistent, and the "2.6bn vs 2.52bn sqm" pair that may be one Nomura estimate double-counted).
- **2015, and parts of 2020/2022/2023, are not cleanly sourced** in the starts/completions table.
  This is a search-budget limit (this dossier used ~31 of its ~28-36 search budget), not evidence
  the data doesn't exist — NBS publishes complete historical series, and an exact retrieval belongs
  on the RUNSHEET as a principal-machine pull if the desk needs vault-grade precision rather than
  search-snippet precision.
- **Every "population measured" distinction in this dossier is the load-bearing finding, not a
  footnote.** Repeating the warning once, plainly: developer-unsold-new-inventory (~4 million
  units), rotten-tail unfinished pre-sold units (8-48 million, credible range), and
  vacant-but-already-owned homes (50-90 million, credible range) are three different populations.
  Any single number presented as "the" answer to "how many empty apartments does China have" without
  specifying which of these three it means should be treated as unreliable regardless of its
  source's authority.
- **The electricity-meter and night-lights methods are not simply lower-quality versions of the
  survey method — they measure genuinely different things** (rural vs. urban; whole-district
  darkness vs. unit-level occupancy) and cannot be used to adjudicate between the survey-based and
  disputed-electricity-based urban vacancy estimates.
- **No figure in this dossier should be read across into a trading or allocation decision** without
  a proper vault pull — per the china-property-plan.md framing, this is Half-B indicative research,
  not desk-grade evidence.
