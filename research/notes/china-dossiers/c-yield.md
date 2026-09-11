# C-YIELD — Chinese Residential Rental Yields and Rents, Pre-Crash vs Now

Agent dossier, China property programme (Half B), covering manifest bundles `b4-resi-yield-national`
+ `b4-rents-falling` (9 questions). Compiled 2026-09-11.

**Tooling note (binding on how to read this dossier, per CLAUDE.md §0a):** WebSearch only —
WebFetch is EGRESS_BLOCKED for every domain in this session and was not attempted. Every figure
below is drawn from WebSearch's indexed snippets, not from a directly-fetched and re-read page.
URLs are real and specific but none were independently re-opened. This is a step below the
dossier's own [VERIFY] bar in rigor, per §0a's stated ceiling for Half B — treat accordingly.
Corroboration rule applied throughout: `[2-SOURCE]` = two genuinely independent outlets/searches
converged on the number; `[1-SOURCE]` = only one outlet/search surfaced it (including cases where
the same number recurred across several search snippets that all trace to one underlying
primary — that is flagged explicitly as NOT independent corroboration); `[RECALL — unverified]` =
not found in any search result, stated with that label only where necessary for context.

## Headline findings

- **China's tier-1 residential gross rental yield is now ~2.0-2.6%, roughly 0.4-0.8pp higher
  than 2021's ~1.7-1.8%** `[2-SOURCE]` (direction) but this is NOT because rents rose — cumulative
  price declines have run well ahead of cumulative rent declines, so the yield rose mechanically
  even as the rent numerator itself has been falling since 2024 `[2-SOURCE]`.
- **The carry spread (yield minus mortgage cost) is still NEGATIVE both then and now, but has
  compressed sharply**: roughly **-2.95pp in 2021** (yield 1.7% vs 5-yr LPR 4.65%) to roughly
  **-1.3pp now** (yield 2.2% vs 5-yr LPR 3.5%), or **-0.9pp** using the actual effective mortgage
  rate (~3.1%) instead of the LPR benchmark. Unlevered residential property in China has gotten
  much closer to break-even against borrowing cost but has not crossed it `[2-SOURCE]` on the rate
  side, `[1-SOURCE]` on the precise yield levels used.
- **National residential rents ARE falling in nominal terms**, not just decelerating: a 50-city
  index fell cumulatively -1.37% in H1 2025 and -3.04% cumulative Jan-Nov 2025 (49 of 50 cities
  down, only Urumqi +0.76%) `[1-SOURCE, one primary institute reported by multiple wire pickups]`.
- **Tier-1 cities are the LEAST bad on rent**, not the worst — first-tier rents fell only -0.56%
  in H1 2025 vs -1.83% (tier-2) and -1.47% (tier-3/4) `[1-SOURCE]`, mirroring the price-decline
  tier gap already booked in the b1 dossiers.
- **China's tier-1 yields (~2-3%) sit at the bottom of the Asia-Pacific/global comparison set**,
  well below Mumbai (~5%), Tokyo (~4.3-4.5%) and Seoul/Hong Kong/Singapore (~3-4.3% on the most
  widely used comparator, though Seoul's number is sharply contested across sources — see §5) —
  and below even Manhattan's ~2-3%, though NOT below the rest of New York City, where cap rates
  run 6-7%+ `[2-SOURCE, cross-city ranking]`.
- **Falling rents are driven by a genuine demand-side hit (record youth unemployment + migrant
  outpopulation from tier-1 cities) colliding with a genuine supply-side glut (unsold homes and
  state-programme units both being pushed into the rental market)** — both sides of the
  scissors are independently sourced `[2-SOURCE]` each.

---

## Q1. National average gross rental yield: now vs 2015 vs 2021, with method

Two distinct series exist and disagree on level (not direction), because they measure different
things — this is itself a finding, not noise:

- **Global Property Guide (GPG)**, the most widely cited international comparator: methodology is
  **(median monthly asking rent × 12) ÷ median asking purchase price**, for 1/2/3-bedroom units,
  sourced from a local listing platform, updated biannually. GPG's headline **national average
  gross yield is 2.63% (Q2 2025)**, up from **2.62% (Q4 2024)** `[1-SOURCE]`. This is an
  ASKING-PRICE-BASED yield (see caveat below), and GPG's own city breakdown (§2) shows its
  individual city figures running noticeably higher (2.6-2.7% for Beijing/Shanghai/Shenzhen) than
  other trackers' figures for the identical cities — suggesting GPG's sample or period differs
  from the domestic press's "big-4 tier-1" framing.
- **Domestic press framing (yicaiglobal, citing a China-based economist/institute), a narrower
  "big cities" aggregate**: **the average annual rental yield in China's major cities climbed to
  2.03% in H1** — sourced snippets gave this as "a new high since 2019" in two different search
  passes that disagreed on whether the year was 2024 or 2025 for that H1 print; flagged explicitly
  as a **date ambiguity in the underlying snippet, not resolved** `[1-SOURCE, date uncertain]`.
  Separately, the same reporting gives **"1.79% in the first half of the year" for the four
  first-tier cities specifically** (Beijing/Shanghai/Shenzhen/Guangzhou) — closer to the
  1.48-1.75% city-level figures in §2 than to GPG's 2.6%+ city figures.
- **2021 baseline**: GPG's China rental-yield page shows the (asking-based) national average
  gross yield at **1.7% in June 2021** `[1-SOURCE]`.
- **2015 baseline — NOT CLEANLY SOURCED**. Search surfaced only an undated "China's rental yield
  is an average of 2.66 percent" fragment and a separate claim that Beijing high-end compound
  yields were 9.5-13% "a few years ago" versus below 2.5% "today" (no year given for either
  endpoint) `[RECALL — unverified / not usable as a 2015 point estimate]`. **This is a genuine
  gap**: no source in this search pass gave a dated, method-stated 2015 China rental-yield figure.
  Directionally, yields were almost certainly LOWER in 2015 than in 2021 or now, because 2015-2021
  was the steepest phase of China's home-price appreciation while rents rose far more slowly — but
  that is inference from the price/rent decomposition literature (§4), not a sourced 2015 number.

**Net read**: on every source, the national/major-city yield is higher now than in 2021 (roughly
+0.3 to +0.9pp depending on which series), and 2015 was very likely lower still, but no dossier
question here can put a sourced number on 2015 specifically.

## Q2. City-level rental-yield table (the widely cited ~1.5-2% tier-1 claim)

| City | Yield | As-of | Source / method | Tag |
|---|---|---|---|---|
| Beijing | 1.48% | May 2024 | domestic press aggregate, asking-based | `[1-SOURCE]` |
| Beijing | 2.63-2.66% | 2025 (GPG page) | GPG, asking-rent/asking-price ratio | `[1-SOURCE]` |
| Shanghai | 1.75% | May 2024 | domestic press aggregate | `[1-SOURCE]` |
| Shanghai | 2.68% | 2025 (GPG page) | GPG | `[1-SOURCE]` |
| Shenzhen | 1.64% | May 2024 | domestic press aggregate | `[1-SOURCE]` |
| Shenzhen | 2.64% | 2025 (GPG page) | GPG | `[1-SOURCE]` |
| Guangzhou | 1.68% | May 2024 | domestic press aggregate | `[1-SOURCE]` |
| 4 tier-1 combined | 1.79% | H1 (year ambiguous, see Q1) | domestic press aggregate | `[1-SOURCE]` |
| Tier-1 (all 4), 2025 | 2.2-2.5% | 2025 | secondary aggregator, un-named primary | `[1-SOURCE]` |
| Tier-1 (all 4), 2023 | 1.8-2.0% | 2023 | same aggregator, same caveat | `[1-SOURCE]` |
| Chongqing / Chengdu / Dongguan / Foshan / Wuhan / pockets of Xi'an, Tianjin | ~4-6% | 2025 | investment-advisory site, "efficient apartments" | `[1-SOURCE]`, corroborated only **directionally** by two other sources describing tier-2 yields as clearly above tier-1 |

**Read this table as two families of numbers, not one**: the ~1.5-1.8% figures are the ones
matching the "widely cited ~1.5-2% in tier-1" framing in the question; the ~2.6-2.7% GPG figures
for the identical four cities are a full percentage point higher on what appears to be the same
basic ratio-of-asking-prices method, and **no source explains the gap** (candidate explanations —
different unit-size mix, different neighbourhoods, different exact months — were not resolved by
search). **All of the above are LISTING/ASKING-PRICE-BASED, not transaction-based** — flagged per
the task's binding instruction; no transaction-price-based China rental yield series was located.
Tier-2 cities (Chongqing, Chengdu, Wuhan, Xi'an, Tianjin, Dongguan, Foshan) running roughly double
tier-1 yields is the most robust cross-city pattern in this search pass — cheaper capital values
against comparably sticky rents.

## Q3. Rental yield vs the 5-year LPR / mortgage rate — the carry spread, then vs now

**Rates, sourced:**
- 5-year LPR, July 2021 fixing: **4.65%** (unchanged for 15 straight months at that point)
  `[2-SOURCE: fxstreet + seekingalpha, both reporting the same PBOC fixing independently]`.
- 5-year LPR, current (Aug 2026, held since a May 2025 cut): **3.50%** `[2-SOURCE: investinglive
  + cnbc/biggo, independently reporting the same PBOC fixing]`.
- Actual weighted-average rate on newly issued personal mortgage loans, current: **~3.1%** (July
  2026) / **~3.06%** (March 2026, a separate reading) `[2-SOURCE, consistent across two
  independent data-provider snippets]` — i.e., effective mortgage pricing now runs BELOW the 5-yr
  LPR benchmark (banks pricing under the reference rate), unlike in 2021.
- Actual average first-home mortgage rate for 2021 was NOT cleanly sourced as a single figure —
  one snippet gave "~4.5% average mortgage rate early 2021" `[1-SOURCE]`, close to but below the
  5-yr LPR itself, which is implausible for a first-home rate (typically LPR + a bank spread) and
  is flagged as **possibly conflating the LPR with the effective rate**; a separate figure — "the
  spread between the MLF rate and the average effective mortgage rate peaked at 2.68pp in December
  2021" `[1-SOURCE]` — describes a different spread (vs MLF, not vs LPR) and cannot be
  algebraically combined with the LPR cleanly without the MLF level, which was not pulled in this
  pass. **Given the ambiguity, the computation below uses the 5-yr LPR benchmark rate as the
  cleanest sourced, like-for-like comparator across both periods**, with the effective-rate
  version shown only for "now" where it is well sourced.

**The arithmetic (shown explicitly, per the task instruction):**

```
CARRY SPREAD = gross rental yield − cost of mortgage debt

2021:
  yield (national, GPG, Jun-2021)         =  1.70%
  5-yr LPR (Jul-2021 fixing)              =  4.65%
  carry spread                             =  1.70% − 4.65%  =  −2.95 pp

NOW (2025/2026):
  yield (tier-1 aggregate, 2025)          =  2.20%   (midpoint of the 2.2-2.5% range)
  5-yr LPR (current)                      =  3.50%
  carry spread (LPR basis)                 =  2.20% − 3.50%  =  −1.30 pp

  yield (tier-1 aggregate, 2025)          =  2.20%
  effective mortgage rate (current, ~mid) =  3.08%   (midpoint of 3.06-3.10%)
  carry spread (effective-rate basis)      =  2.20% − 3.08%  =  −0.88 pp

CHANGE IN CARRY SPREAD, 2021 -> now (LPR basis):
  −1.30 pp − (−2.95 pp)  =  +1.65 pp narrowing
```

**Read**: the carry spread has been NEGATIVE at both dates — a leveraged buyer's mortgage cost has
exceeded the gross rental yield throughout, i.e., property has never been "cash-flow positive on
day one" against a mortgage at either date in this comparison — but the gap has narrowed by
roughly 1.6-2.1 percentage points, driven by LPR cuts (4.65% -> 3.50%, a much bigger move than the
yield's own ~0.5pp rise). This is the single cleanest "is it cheap yet" read available from this
search pass: **closer to break-even, not yet at or past it**, and the improvement is overwhelmingly
a RATES story, not a yields story (see the LPR move of -115bp vs the yield move of roughly
+30-50bp).

## Q4. Has the yield risen because rents rose or because prices fell? Decomposition

**Prices fell more than rents fell — the yield's rise is a price-side, not a rent-side,
phenomenon** `[2-SOURCE independently making the same qualitative claim]`:
- "Both rental and housing prices have been sliding in 50 key Chinese cities in recent years,
  with property price declines being much greater than rental price declines" — directly stated
  in reporting on the China Index Academy's own 50-city series.
- Consistent with Q1/Q3: the yield only rose ~0.3-0.9pp over a period (2021-now) in which
  cumulative new-home price declines are independently documented elsewhere in this programme at
  well over 10-20% in most cities (b1 dossiers) while the rent index itself (Q6) has been
  DECLINING, not rising, since 2024. A yield rising while its own numerator (rent) is falling is
  only arithmetically possible if the denominator (price) is falling faster — which is exactly
  what both series show.
- There IS a partial rent-side offset in some readings: one 2025 comparison stated "rents up
  3-5% year-over-year in major cities" alongside the 2.2-2.5% tier-1 yield figure `[1-SOURCE]` —
  this conflicts with the CIA-sourced tier-1 figure of rents DOWN -0.56% in H1 2025 (Q6). The two
  cannot both be describing the same cities/period; flagged as an unresolved source conflict
  rather than silently picking one. The CIA figure is preferred here because it names its
  institute and a specific cumulative window, whereas the "+3-5%" claim's primary source could not
  be identified in the search snippet.

## Q5. International comparison: China tier-1 vs Tokyo, Seoul, Singapore, Hong Kong, Mumbai, New York

| City | Gross yield | Source | Tag |
|---|---|---|---|
| Mumbai | 5.09-5.16% (one GPG-linked cut) | GPG-family ranking | `[1-SOURCE]` |
| Mumbai | 3.84% (ranking) or 2.44% (a separate figure in the same result) | novyy | `[1-SOURCE, internally inconsistent]` |
| Tokyo | 4.55% | GPG | `[1-SOURCE]` |
| Tokyo | 4.5% (Novyy's own figure) | novyy | `[2-SOURCE — the only city where GPG and novyy closely agree]` |
| Seoul | 4.31% | GPG | `[1-SOURCE]` |
| Seoul | 1.18% (city centre) / 1.39% (outside centre) | novyy | `[1-SOURCE, SHARPLY CONTRADICTS the GPG figure — flagged, unresolved]` |
| Hong Kong | 3.55% | GPG | `[1-SOURCE]` |
| Hong Kong | "2-3% in designated locations" | novyy | `[2-SOURCE, roughly consistent]` |
| Singapore | 3.06-3.13% | GPG | `[1-SOURCE]` |
| China (Beijing, GPG cut) | 2.63-2.66% | GPG | `[1-SOURCE]` |
| China tier-1 (domestic press cut) | 1.5-2.0% (see §2) | domestic press | `[1-SOURCE]` |
| New York State (GPG, all NY) | 7.52% | GPG | `[1-SOURCE]` |
| United States national | 6.71% (Q2 2026) / 6.56% (Q4 2025) | GPG | `[1-SOURCE]` |
| Manhattan specifically | 2-3% cap rate | SFR Analytics / NYC investment-advisory | `[2-SOURCE, independent]` |
| Bronx | ~6.1% cap rate | NYC investment-advisory | `[1-SOURCE]` |

**Read**: on the single most-used comparator (GPG), China's tier-1 cities sit at the bottom of
this group, below every other market shown except on the (contested) Seoul figure — and Manhattan,
not China, is the actual global outlier at the low end once "New York" is disaggregated by
borough. The Seoul discrepancy (4.31% vs 1.18-1.39%) is large enough that it should be treated as
a methodology/definition conflict (net vs gross, jeonse deposit-lease system vs monthly rent — the
Korean jeonse system materially complicates any yield comparison and was not resolved in this
search pass) rather than a real data point either way.

## Q6. China residential RENT index by year and city tier — is nominal rent actually falling?

Primary series located: **China Index Academy (CIA / China Index Research Institute), 50-city
residential rent index** (all figures `[1-SOURCE]` in the sense that they trace to one primary
institute, even though picked up by several separate wire/aggregator articles independently):

| Period | Metric | Value |
|---|---|---|
| H1 2025 | cumulative change, 50-city average | **-1.37%** |
| H1 2025 | tier-1 cities | **-0.56%** |
| H1 2025 | tier-2 cities | **-1.83%** |
| H1 2025 | tier-3/4 cities | **-1.47%** |
| Jul 2025 | level, 50-city average | 31.94 yuan/sqm/month |
| Jul 2025 | MoM | -1.51% |
| Jul 2025 | YoY | -4.42% |
| Jan-Nov 2025 | cumulative, 50-city average | **-3.04%** (49 of 50 cities down; Urumqi the sole riser, +0.76%) |
| 2024 (full year) | Beijing | -0.1% |
| 2024 (full year) | Hangzhou | -0.6% |
| 2024 (full year) | Guangzhou | -2.3% |
| 2024 (full year) | Shenzhen | -3.5% |
| Dec 2025 | broader CPI-adjacent rent-inflation reading | -0.30% YoY, described as negative "since early 2024" after averaging +1.2%/yr in the pre-pandemic decade |

**Yes — nominal rent is falling, not merely decelerating**, across essentially every one of the
50 tracked cities by late 2025, with the decline WIDENING over the course of 2025 (H1 cumulative
-1.37% roughly doubling to -3.04% by November) rather than stabilizing. Tier-1 is the mildest
tier, not the worst — consistent with the price-side tier gap already booked elsewhere in this
programme.

## Q7. The Beike / Anjuke rent indices for tier-1 cities: peak and latest

**This could not be sourced as asked — a genuine gap, not an oversight.** Search surfaced:
- Beike (KE Holdings)'s **"graduation season rental index"**, most recent cut: average monthly
  rent in first-tier cities **CNY 4,394 (~USD 678)**, ranking Beijing top, then Shanghai,
  Shenzhen, Hangzhou, Guangzhou `[1-SOURCE]` — a level, not a peak-vs-latest series.
- The **58 Anjuke Real Estate Research Institute**'s finding that **80.5% of new college
  graduates rent** (not a rent-price index at all) `[1-SOURCE]`.
- No search result produced a Beike- or Anjuke-branded rent PRICE index with an identifiable 2021
  peak value and a comparable latest value for named tier-1 cities. The CIA 50-city index (Q6) is
  the closest substitute located and is domestic-institute-branded, not Beike/Anjuke-branded.
  **Flagged in Gaps & Cautions.**

## Q8. Why are rents falling — unemployment, migrant outflow, unsold-unit conversion

**Demand side — graduate/youth unemployment** `[2-SOURCE, independent outlets]`:
- China's 16-24 (ex-student) youth unemployment rate hit a record **18.9% in August 2025**
  (Caixin/Vision Times reporting), against **12.22 million new graduates** that year.
- Job postings aimed at graduates fell **-22% in H1 2025** while job seekers rose **+8%** —
  a genuine demand/supply mismatch in the graduate labour market that feeds directly into rental
  demand, since new graduates are one of the largest renter cohorts (see Q7's 80.5% figure).

**Demand side — migrant/non-resident population outflow from tier-1 cities** `[2-SOURCE,
independent outlets citing the same underlying official bulletin]`:
- Shanghai's non-resident (migrant) population: **10.48m (2020 peak) -> 10.32m (2021) -> 10.06m
  (2022) -> 10.07m (2023) -> 9.83m (2024)** — the first sub-10-million reading in recent years,
  a net decline of ~640,000 from the 2020 peak, sourced to Shanghai's own 2024 statistical
  bulletin and reported independently by Chinascope and Vision Times.
- Explicitly linked in reporting to reduced demand for migrant labour amid the slowing economy —
  migrant workers and young professionals are named as the chief drivers of urban rental demand.

**Supply side — unsold units and state-purchased stock entering the rental market**
`[2-SOURCE, independent outlets]`:
- Shanghai's Minhang district government **acquired 7,500 sqm of unsold housing stock in June
  2025 and converted it to rentals** — one concrete, dated instance of the mechanism.
- More broadly: **"China's unsold apartments in small cities are becoming cheap rentals"** as
  oversupply and population decline collide, per two independently-reported pieces (Seoul
  Economic Daily's "new towns turn into cut-rate rental zones" + Caixin's reporting on the
  destocking push).
- The destocking cycle itself is documented as NOT resolved: progress reversed and inventory
  began rising again in Q2 2025, prompting a renewed policy push at the Central Economic Work
  Conference.

**Net read**: this is a genuine demand-and-supply scissors, each half independently sourced —
fewer young/migrant renters chasing more available units (both organically unsold and
policy-converted) is a textbook explanation for a falling rent level, and it does not require
invoking any one factor alone.

## Q9. Affordable rental housing (保障性租赁住房) programme: units delivered, effect on market rent

- **Target**: 14th Five-Year Plan (2021-2025) target of **8.7 million units** of government-
  subsidised rental housing `[1-SOURCE primary — a Reuters explainer wire, syndicated across
  Yahoo Finance, Business Standard/investing.com and Wall Street Observer; these are the SAME
  underlying wire report, not independent corroboration, and are labelled accordingly]`.
- **Progress**: "two-thirds delivered by end of 2023" per the same wire reporting; a separate,
  differently-worded snippet described "construction and preparation commenced on 1.8 million
  units (rooms) nationwide" across affordable-housing categories in 2024 `[1-SOURCE]` — the two
  figures are not reconcilable into one clean delivered-vs-target number from this search pass.
- **Program design**: units capped at ≤70 sqm, explicitly removing hukou (household-registration)
  restrictions so migrant workers and young non-local workers can access them — a deliberate
  break from earlier public-housing schemes `[1-SOURCE]`.
- **S&P Global estimate**: affordable/social housing was **~8% of primary sales in major cities
  in 2023**, projected to reach **~20% by 2026** `[1-SOURCE]` — if directionally correct, this is
  a large and growing share of new supply competing directly with private rentals.
- **Effect on market rent — direct evidence of undercutting**: in Changsha, public-housing rents
  are required to be **at least 30% below market rate**; reporting explicitly states that
  large-scale affordable-rental supply in Beijing, Shanghai, Shenzhen, Hangzhou and Chengdu is
  now large enough to be **"drawing many potential renters away from the private market"**
  `[1-SOURCE]`, i.e. a direct, named channel by which the programme is suppressing private-market
  rents in exactly the cities this dossier covers.
- **Important counter-finding, academic**: a peer-reviewed piece on Shenzhen's "centralized
  leasing" implementation is explicitly titled **"Making affordable rental housing unaffordable"**
  — evidence that at least one major city's implementation has NOT delivered the intended discount
  in practice `[1-SOURCE]`, a caution against reading the programme's headline design as its
  realized effect everywhere.

---

## Gaps and cautions

1. **No clean, dated 2015 national rental-yield figure was located** (Q1) — the single largest
   sourcing gap against the task's explicit ask. Only an undated "2.66%" fragment and an undated
   "9.5-13% a few years ago" Beijing high-end anecdote surfaced; neither carries a usable year tag.
2. **City-level yields (Q2) split into two families roughly a full point apart** (domestic-press
   ~1.5-1.8% vs GPG ~2.6-2.7%) for the SAME cities in roughly the SAME period, with no source
   explaining the gap. Both are reported here rather than picking one, per the "never round-trip"
   rule.
3. **All yield figures in this dossier (GPG's, the domestic-press aggregate's, and the tier-2
   figures) are LISTING/ASKING-PRICE-based**, not transaction-based — flagged per the task's
   binding instruction. No transaction-price China rental-yield series was found in this pass.
4. **The 2021 mortgage-rate side of the carry-spread calculation (Q3) rests on the 5-yr LPR
   benchmark, not a confirmed effective first-home rate** — a "4.5%" effective-rate snippet for
   early 2021 looked implausible (below the LPR itself) and was not used; if the true 2021
   effective first-home rate was meaningfully above the 4.65% LPR (as is typical, via a bank
   spread), the true 2021 negative carry was DEEPER than -2.95pp, making the narrowing to now even
   larger than stated. This is a conservative-direction gap, not a random one.
5. **Q4's decomposition has one unresolved internal conflict**: a "rents up 3-5% YoY in major
   cities" claim contradicts the CIA-sourced "-0.56% H1 2025 tier-1" figure for what appears to be
   the same cities/period. Not reconciled here; the CIA figure is preferred as better-attributed.
6. **Q5's Seoul figure is a genuine, large, unresolved discrepancy** (4.31% vs ~1.2-1.4%),
   plausibly a gross/net or a jeonse-system definitional difference; treat any Seoul number in
   this dossier with caution.
7. **Q7 (Beike/Anjuke rent INDEX, peak-vs-latest) could not be sourced as asked** — a genuine gap.
   What exists (Beike's graduation-season rent level, Anjuke's renter-share statistic) is not the
   requested index.
8. **Q9's "8.7 million units" delivery figures come from what is very likely a single syndicated
   Reuters wire story**, not independent primary reporting, despite appearing across several
   outlets — labelled `[1-SOURCE]` accordingly rather than `[2-SOURCE]` on that basis alone.
9. Every figure in this dossier is a WebSearch-snippet reading, per the binding tooling note —
   none were confirmed by opening the source page directly.
