# C-DATATRUST — How much can any of these numbers be trusted, and who actually called the crash

*Dossier `c-datatrust` (CN programme, Half B, dispatch row 28 — `b9-data-reliability` +
`b9-who-got-it-right`). Compiled 2026-09-11. Method: WebSearch only — **WebFetch is
EGRESS_BLOCKED for every domain** (plan §0a). Every figure below is a search-result-snippet
reconstruction of a primary or press source, not a primary-document read — this dossier's own
subject (measurement reliability) makes that ceiling unusually load-bearing, and it is stated
here rather than hidden. Corroboration rule: load-bearing figures are tagged `[2-SOURCE]`,
`[1-SOURCE]`, or `[RECALL — unverified]`. No figure is invented; no prediction is attributed
without a date and a link. Today's date 2026-09-11; every figure states its own as-of/vintage
date. Web-sourced — not vault data, not sha256-manifested, not a trial-ledger entry (plan §0/§5).
Question 7-9 (named calls) are reported as fairly as the search record allows: what was said and
when, not what reads well in hindsight, and the people who were wrong are named without
editorializing.*

## Headline findings

- **The NBS 70-city index understates declines through four documented, distinct mechanisms**
  (registered-price caps that hold the *contract* price sticky while off-book discounts do the
  real adjusting; the "reference/guidance price" (指导价) system, cleanest-documented in Shenzhen's
  Feb 2021 secondhand scheme; a quality-mix/matching-model bias that a peer-reviewed methodology
  paper attributes to new transactions migrating toward cheaper outer rings; and NBS's own 2017
  admission of "new challenges and difficulties" in the methodology) `[2-SOURCE]` on the general
  understatement finding, `[1-SOURCE]` on each individual mechanism's magnitude.
- **Local price-floor mechanisms are dated and named, and they flipped direction as the cycle
  turned** — at least 8 cities including Zhuzhou (Hunan) and Huizhou summoned developers over
  "excessively cheap" pricing in Sept 2021 `[2-SOURCE]`; by mid-2022 the same mechanism was being
  *petitioned away* by developers (Guangdong, Jun 2022) and *relaxed* by regulators (Guangzhou
  allowing cuts up to 20% vs a prior 6% ceiling, Sept 2022; national land-premium caps rescinded
  2023) `[1-SOURCE]` per instance. The floor was a crash-management tool, not a permanent price
  control, and it was dismantled once it started blocking recovery rather than blocking decline.
- **No single, sourced, transferable "adjustment multiplier" exists.** What professionals
  actually do, per trade-press reporting, is substitute a private secondhand series (chiefly
  Beike-derived) for the segments where it matters, not apply a fixed haircut to the NBS number.
  Any generic "multiply official by 1.5-2x" rule circulating informally is **folklore** on this
  search record — not traced to a stable, repeatable source.
- **The most-quoted extreme vacancy figure was disowned by its own speaker in the same breath it
  was cited** — He Keng, a former deputy head of China's statistics bureau, told a Sept 2023
  Dongguan forum that the most extreme estimates put current vacant stock enough to house 3
  billion people, then immediately added "that estimate might be a bit much, but 1.4 billion
  people probably can't fill them" `[2-SOURCE]`. This is distinct from — and should not be
  conflated with — Prof. Gan Li's own 21-22%/~50-65 million-unit vacancy estimate (China
  Household Finance Survey, 2017-18), which this search record found **no evidence** Gan Li
  himself ever retracted.
- **The callers who got the timing right were reading balance sheets and cash flows, not the
  price index.** UBS's John Lam issued a rare SELL on Evergrande roughly 11 months before its
  Sept 2021 default `[2-SOURCE]`; the PBoC/MOHURD "Three Red Lines" (Aug 2020) targeted
  developer leverage and liquidity ratios directly; Rhodium's Logan Wright and Rogoff-Yang's NBER
  paper both worked from structural demand/demographic models, not a price series. The perennial
  bears (Chanos 2010, Chang 2001, Bass 2016) worked from a macro-thesis with no dated
  balance-sheet trigger, and were each years-to-decades early.
- **Independent, non-price cross-checks corroborate the direction but not a single magnitude**:
  cement output fell to a ~20-year low in 2022 `[1-SOURCE]`; steel demand tied to property (~1/3
  of consumption) fell in 2021-2022 on schedule with the bust `[1-SOURCE]`; satellite nightlight
  studies find the "ghost city" phenomenon real but **geographically confined** (one peer-reviewed
  study: ~22 smaller cities show the signature) — i.e., independent remote-sensing evidence
  actively *contradicts* the more extreme "hundreds of millions of empty homes nationwide" framing
  `[1-SOURCE, single study]`; and the July 2022 mortgage-boycott event is a genuine independent
  buyer-behavior signal (spread from ~30 to 300+ projects within weeks) `[2-SOURCE]` that moved in
  the same direction as the price data without being derived from it.

---

## DATA SOURCE TABLE

| Source | Coverage | Lag | Known bias | Trusted by whom |
|---|---|---|---|---|
| **NBS 70-city index** (国家统计局) | 70 medium/large cities, new-build + secondhand, monthly, official | ~2 weeks after month-end | Uses *registered/contract* prices, which price caps and reference-price systems hold artificially sticky; excludes off-book discounts, rebates, decoration allowances; matching-model methodology built for secondary markets, applied to primary listings, historically criticized as failing to control for new sales migrating to cheaper outer rings `[2-SOURCE general criticism]`; NBS itself (deputy director Li Xiaochao, 2017) acknowledged "new challenges and difficulties" `[1-SOURCE]` | The official reference series everyone must quote; foreign press and banks cite it but routinely flag it as a floor, not the real number |
| **China Index Academy (CIA) / CREIS** | ~100-city listing/hedonic/transaction index descended from Soufun/CREIS/China Villa Index System, 21/111/321-tier database structure; land + residential + commercial | Monthly, some sub-indices faster | Descended from a real-estate services/portal business; claims cooperative ties to NBS and the State Housing Bureau, raising an independence question even as it's the most-cited private alternative `[1-SOURCE]` | Most widely cited private cross-check in Western financial press; used as the de facto "100-city index" benchmark |
| **Beike / KE Holdings (Beike Research Institute)** | Dominant online+offline brokerage platform; "Housing Dictionary" of 300M+ property records; secondhand listings + closed transactions via its own brokerage network | Near real-time (own platform flow) | Broker/platform-observed, weighted toward markets where Beike has brokerage penetration; increasingly the standard secondhand-market benchmark in press coverage of prime-city declines (Shanghai, Shenzhen, Hangzhou) `[1-SOURCE]` | Fortune, S&P and other outlets cite Beike-derived figures specifically for secondhand-market divergence from the NBS series |
| **CRIC / E-house** | New-home + land transaction data across dozens of cities (56 cities per a 2009-vintage description; expanded since); merged 2012 | Monthly | Works directly with developers, the China Real Estate Research Association and China Real Estate Association — a similar commercial-tie caveat to CIA/CREIS `[1-SOURCE]` | Developer investor-relations decks; some sell-side research |
| **Wind** | Financial-data terminal, "the domestic Bloomberg equivalent," 8M+ macro/industry indicators, city/county drill-down for 3,000+ regions | Varies — inherits the lag of whatever underlying source it re-publishes | Purely an **aggregator** — not a primary collector; it inherits NBS/PBoC/CREIS bias wholesale, adds none of its own beyond standardization `[1-SOURCE]` | Virtually every mainland-facing institutional desk |
| **CEIC** | China Premium Database — provincial/municipal/county macro + real estate + socio-demographic data, 200+ cities | Varies by underlying series | Same aggregator caveat as Wind; its own "Real Estate Climate Index" is itself an NBS-family composite, not an independent read `[1-SOURCE]` | International institutional research desks without mainland terminal access |

---

## CALLS TABLE

| Who | Date | What exactly was said | How specific | Outcome |
|---|---|---|---|---|
| Jim Chanos (Kynikos Associates) | Jan 2010 (public, incl. Charlie Rose interview) | China property = "Dubai times 1,000" or worse; shorted developers, banks, infrastructure names and the Hang Seng broadly; expected the bubble to burst "late 2010 or early 2011" `[2-SOURCE]` | Specific magnitude language, specific (if loose) timing | **WRONG on timing** — the actual bust did not arrive until 2021, roughly a decade after the stated window; whether the short position was later profitable on a different timeline is not resolved by this search |
| Kyle Bass (Hayman Capital) | Early 2016 | Massive short against the yuan; argued Chinese banking-system "imbalances" would force a ~30% devaluation `[2-SOURCE]` | Specific magnitude and mechanism | **WRONG as positioned** — the trade lost money as PBoC clamped down on capital outflows; Bass closed the position at a loss by May 2019 `[2-SOURCE]`, before any subsequent yuan weakness could have vindicated the direction |
| Gordon Chang | 2001 (book, "The Coming Collapse of China") | China's economic model / CCP rule would collapse within a decade — later stated explicitly as by 2011, then revised to 2012 `[2-SOURCE]` | Highly specific dated prediction, twice | **WRONG twice** — named to a "10 worst predictions of the year" list on both dates `[1-SOURCE]`; the prediction, in revised forms, has run for 20+ years and is the textbook case this dossier's rules ask to be distinguished from a genuine specific call |
| Kenneth Rogoff & Yuanchen Yang | Aug 2020 (NBER Working Paper 27697, "Peak China Housing") | A decades-long housing boom had produced severe price misalignment and regional mismatches; the sector (~29% of GDP by their input-output estimate) was vulnerable to a sustained growth shock that could cut cumulative output 5-10% over several years `[2-SOURCE]` | Specific quantified macro-drag estimate, not an explicit "developer default imminent" call | **Directionally CORRECT**, published ~13 months before Evergrande's Sept 2021 default; the paper's claim was about macro drag and structural mismatch, not a price-crash timing call, so it should not be over-credited as predicting the specific 2021 trigger |
| Anne Stevenson-Yang / J Capital Research | 2017 (quote resurfaced via a Sept 2021 social-media repost) and Jan 16, 2022 (Forbes) | 2017: Evergrande as "the biggest pyramid scheme the world has yet seen" `[1-SOURCE — a 2021 repost of a 2017 quote, not an original contemporaneous document found in search]`; Jan 2022 Forbes: "scant evidence" China's property "soft landing" was actually under way `[1-SOURCE]` | Specific, named-company call ~4 years ahead of Evergrande's default; second call timed almost exactly at the point the downturn accelerated | **CORRECT** on both, though the 2017 dating rests on a single retrospective source |
| John Lam (UBS) | ~Oct 2020 (dated as "three years ago" by an Apr 2024 Bloomberg piece) | A rare SELL rating on China Evergrande Group `[2-SOURCE]` | Specific, single-name, dated | **CORRECT** — roughly 11 months ahead of the Sept 2021 default; the most precisely-timed named call in this record |
| Logan Wright (Rhodium Group) | Sept 2021 (contemporaneous with the Evergrande news break) | Developers would be forced to scale back construction sharply, meaningfully reducing GDP growth, with official data likely understating the true hit; urban household formation was structurally decelerating (~9-10mn/decade prior vs ~5-7mn/decade forward) `[2-SOURCE]` | Specific structural argument | **CORRECT**, though the call is dated to the same month the crisis was already public — not meaningfully ahead of the news itself, unlike Lam's or Stevenson-Yang's earlier calls |
| PBoC / MOHURD ("Three Red Lines" architects) | Aug 2020 | Explicit quantitative caps on developer liability/asset ratio (<70%), net-debt/equity (<100%), cash/short-term-debt (>=1x) `[2-SOURCE]` | A policy, not a "prediction," but it is the most precisely dated and quantified pre-crisis intervention on record | The policy directly precipitated the liquidity stress it was designed to manage — Evergrande and others defaulted within the following year; whether this counts as "calling" the crash or *causing* it is a fair question this dossier does not resolve |
| He Keng (ex-deputy head, NBS) | Sept 2023 (Dongguan forum) | Cited, then disowned, the most extreme vacancy estimate: "enough for 3 billion people... that might be a bit much, but 1.4 billion probably can't fill them" `[2-SOURCE]` | Not a forecast — a data-quality admission from an official source | Directly evidences the "disowned statistic" pattern the desk asked about |

---

## 1. How the NBS 70-city index understates declines

Four distinct, separately documented mechanisms, not one:

1. **Registered/contract-price stickiness under price caps.** Chinese cities have long operated
   presale-permit price ceilings (限价) — a developer cannot register a contract price above the
   local cap for a project's presale permit, regardless of what it takes to actually clear units.
   The consequence for the index: the *headline* registered price the NBS series is built from can
   stay near the cap even as developers give ground through channels the registered price does not
   capture (see mechanism 4). The land-side analogue of this cap (a 15% premium ceiling on land
   auctions, introduced 2021) was itself rescinded by the Ministry of Natural Resources in 2023 to
   "revive land sales" `[1-SOURCE, SCMP]` — direct evidence the cap mechanism existed and was
   binding enough to require an explicit policy reversal.
2. **The "reference/guidance price" (指导价) system.** Shenzhen became the first mainland city to
   publish a secondhand-housing reference-price list, Feb 8, 2021, covering 3,500+ residential
   communities `[2-SOURCE]`. The reference price is set "once a year in principle" — deliberately
   sticky — and is used both to cap intermediary listing prices and to set mortgage loan-to-value
   ratios `[2-SOURCE]`. Because it updates annually while true market prices move continuously, it
   mechanically lags both up-legs and down-legs. Shenzhen scrapped the reference price's use in
   mortgage-qualification specifically in Feb 2023 to help *revive* transaction volume `[1-SOURCE,
   SCMP]` — again showing the tool was loosened once it began suppressing recovery.
3. **Sample composition / quality-mix drift.** A peer-reviewed methodology paper on Chinese house
   price index construction found the standard approach — a matching model developed for secondary
   markets, applied to the newly-built sector — fails to properly control for newly transacted
   units migrating toward cheaper outer-ring locations over time, producing a downward bias in the
   *quality-adjusted* comparison even before any true price movement is considered `[1-SOURCE,
   Journal of Real Estate Finance and Economics]`.
4. **Exclusion of discounts and incentives.** Developer-offered decoration allowances, cash
   rebates, extended payment terms and other off-book concessions do not appear in the registered
   contract price the NBS series draws on. Fortune (Aug 2023) reported industry insiders and
   economists saying China's official home-price indexes were "likely understating the depth of
   the downturn, in part because of longstanding methodologies that struggle to capture market
   turning points" `[1-SOURCE, but the general theme of official/private divergence appears
   independently across CNBC, SCMP and Bloomberg reporting — treat the mechanism claim as
   [2-SOURCE], the specific magnitudes below as [1-SOURCE]]`. The same piece quantified: official
   new-home prices down only 2.4% from the Aug 2021 high, existing-home prices down 6% (as of Aug
   2023), while private data showed existing-home prices down at least 15% in prime Shanghai/
   Shenzhen neighborhoods and in more than half of tier-2/tier-3 cities, with Hangzhou secondhand
   homes near Alibaba's headquarters down ~25% from late-2021 highs `[1-SOURCE]`.

NBS itself has acknowledged the problem in general terms: deputy director Li Xiaochao said in 2017
the methodology had met "new challenges and difficulties" and pledged improvement `[1-SOURCE]` —
evidence the understatement critique is not purely an external one.

## 2. Local governments banning price cuts / setting price floors — dated, named instances

- **Zhuzhou, Hunan, Sept 2021**: housing authorities summoned executives of four local developers
  and several agencies after residents posted online that units in three downtown projects were
  priced at ~5,000 yuan/sqm against an area average near 7,600 yuan/sqm; developers were told to
  stop pricing "obviously lower than market level" and end discount gimmicks `[2-SOURCE, SCMP]`.
- **At least 8 cities total by Sept 2021**, spanning from Zhuzhou to Huizhou in the Greater Bay
  Area, adopted similar measures against "excessively cheap" new-home pricing `[2-SOURCE, SCMP]`.
- **Guangdong province, June 2022**: developers petitioned the local government to relax the very
  restrictions barring them from cutting prices, as sales weakness made the floor unworkable
  `[1-SOURCE, Caixin]` — the clearest documented instance of the mechanism being fought from the
  supply side once conditions reversed.
- **Guangzhou, reported Sept 2022**: allowed price cuts of up to 20%, versus a prior 6% ceiling —
  described as the biggest relaxation by any top-tier Chinese city at that point `[1-SOURCE, Yicai
  via search summary]`.
- **Suzhou**: had maintained price-cut limits; by 2023 reporting describes the government as no
  longer meaningfully restricting cuts `[1-SOURCE]`.
- **National land-premium cap**: a 15% ceiling on developer land-auction premiums, in force since
  2021, was rescinded by Ministry of Natural Resources directive in 2023, returning plots to
  highest-bidder auctions; average land premiums in 22 major cities subsequently ran near 20% for
  four straight months versus the 5-10% range typical in 2024 `[1-SOURCE, SCMP]`.
- **Shenzhen** separately relaxed land-purchase caps for developers around the same reform wave,
  after the cap had "sent real estate auctions into a tailspin" `[1-SOURCE, SCMP headline
  characterization; exact date not independently pinned in this search]`.
- **Beijing**: subsequently removed its own land-sale price cap altogether, reported by SCMP as
  "signalling a property-market shift" `[1-SOURCE; the article's own date was not resolved
  precisely from the snippet — flagged as a gap]`.

## 3. The gap between asking, reference, and actual transaction prices

- **Shenzhen reference vs. owner-listed asking price** (2021, first year of the scheme): search
  reporting describes the reference price as running well below owner asking prices for most
  ordinary secondhand stock, with one specific example unit (a "Marriott House" community) priced
  at 130,000 yuan/sqm under the reference system `[1-SOURCE]` — the general-discount-range figure
  reported ("about 70% to 20% off" listing) is ambiguously phrased in the source material itself
  and should be read as "reference prices ran a wide, property-specific range below owner asking
  prices," not as a single clean percentage `[1-SOURCE, flagged for imprecision]`.
- **Share of transactions closing below the Shenzhen reference price**: only ~5% in the scheme's
  first year (2021); reported as having "increased significantly" by 2023, without a specific
  number given in the source `[1-SOURCE]` — directional only.
- **Prime-neighborhood secondhand vs. national official index** (as of Aug 2023): private data
  showed at least -15% in prime Shanghai/Shenzhen neighborhoods and in more than half of tier-2/
  tier-3 cities, against an official secondhand-price decline of only -6% nationally over the same
  window since the Aug 2021 peak `[1-SOURCE, Fortune]`.
- **Hangzhou specific case**: secondhand homes near Alibaba's headquarters down ~25% from late-2021
  highs, versus the ~2.4% new-home national official decline reported for a comparable period
  `[1-SOURCE]` — the largest single documented asking/official gap found in this search.

No search in this set produced a clean, general "asking price is X% above transaction price"
national constant; every quantified figure found is city- or segment-specific and dated.

## 4. Which private data sources professionals actually trust

See the DATA SOURCE TABLE above for the full comparison. In narrative: **China Index Academy/
CREIS** is the most frequently cited private cross-check in Western financial press and is the
closest thing to an industry-standard "second opinion" on new-build prices, despite its own
service-industry lineage raising an independence question `[1-SOURCE]`. **Beike/KE Holdings** has
become the de facto benchmark specifically for the *secondhand* market, where the NBS series is
most criticized, because its data derives directly from live brokerage transaction flow rather
than developer-registered contracts `[1-SOURCE]`; it is the source underlying most of the
prime-city divergence figures reported by Fortune and cited by S&P. **CRIC/E-house** plays a
similar role to CREIS for new-home and land transactions, with the same commercial-tie caveat.
**Wind and CEIC are not independent sources at all** — they are aggregation terminals that
institutional desks use to access NBS, PBoC and the above private series through one interface;
neither collects primary real-estate data itself, so neither can correct for any of the biases
named in §1 `[1-SOURCE each]`.

## 5. The practical adjustment rule

**No universal, sourced, transferable adjustment rule was found in this search set, and that
absence is itself the most useful answer to this question.** What the trade press documents is a
practice, not a formula: professionals substitute a private, segment-appropriate series (chiefly
Beike-derived for secondhand, CREIS/CRIC for new-build) for the NBS number in the specific
city/segment they care about, rather than applying a fixed percentage haircut to the national
index. Where a single national comparison number does exist — this desk's own `c-velocity.md`
carries an official cumulative real bust of -24.6% against a private estimate near -40%
(`research/notes/china-dossiers/c-velocity.md`) — it is explicitly tagged there as `[1-SOURCE]` on
the private leg, and should NOT be read as a stable multiplier applicable to other cities, other
time windows, or other property segments. Any "multiply the official number by roughly 1.5-2x"
rule of thumb circulating informally is, on this search record, **folklore** — repeated in
commentary but not traced to a specific, citable, methodologically transparent study that derives
and validates a constant conversion factor across time and geography.

## 6. Independent cross-checks: satellite, electricity, mobility, shipping, cement, mortgage data

- **Cement**: output fell to ~2.13 billion tonnes in 2022, a decline reported as roughly -10.5% to
  -15% depending on the framing used, described as the biggest fall in at least two decades; 2023
  H1 output was roughly flat versus 2022 H1 `[1-SOURCE]`. Property/construction is cement's primary
  end-use in China, so this tracks the bust's real-economy footprint independently of any price
  series.
- **Steel**: property accounts for roughly one-third of Chinese steel consumption; a government-
  linked industry consultancy forecast steel demand down 4.7% in 2021 and a further 0.7% in 2022
  `[1-SOURCE, S&P Global, Feb 2021 — an ex-ante forecast, flagged as such rather than a realized
  figure]`; new-construction floor-space starts fell more than a fifth in both 2022 and 2023 and a
  further ~24% in 2024 `[1-SOURCE]`.
- **Satellite nightlights**: multiple studies (a 2018 remote-sensing paper combining nighttime and
  daytime satellite imagery; an earlier 2011-era study using DMSP-OLS nightlight brightness as a
  vacancy proxy) find the "ghost city" phenomenon **real but geographically confined** — one
  study's own stated result: the problem is "confined to 22 smaller cities" `[1-SOURCE]`. This is
  a genuinely independent measure that **contradicts the more extreme viral framing** of a
  nationwide vacancy crisis, while still confirming a real, bounded phenomenon.
- **Mortgage/buyer-behavior data — the 2022 mortgage boycott**: a list of unfinished projects whose
  buyers refused to keep paying mortgages grew from ~30 to 300+ within about two weeks in July
  2022, spreading across dozens of cities (12 projects in Chongqing, 7 in Shanghai, 8 in Guangdong,
  9 in Nanning, 10 in Taiyuan, and more) `[2-SOURCE]`. Loans at risk were estimated as high as ~2
  trillion yuan (~$296bn) `[1-SOURCE]`; 16 banks disclosed a collective ~$414 million in overdue
  loans specifically tied to the boycotted projects `[1-SOURCE]`. Independent estimates of the
  scale of undelivered presale housing varied widely — Reuters-canvassed analysts put unfinished
  projects at 5-20% of the national total, while Nomura estimated only ~60% of homes presold
  between 2013-2020 had actually been delivered `[1-SOURCE]` — a genuinely independent,
  buyer-behavior-based stress signal, not derived from any price index.
- **Not found in this search set** (named as a gap rather than guessed at): dedicated
  shipping/dry-bulk freight-rate cross-checks and a property-specific (as opposed to economy-wide)
  electricity-consumption series. The Li Keqiang Index (electricity consumption 40%, bank loans
  40%, rail freight 20%) is a general economic-activity proxy, not a property-sector-specific one,
  and should not be cited as a dedicated real-estate cross-check `[2-SOURCE on the index's general
  construction]`.

## 7. Named analysts, academics and investors with dated, specific calls

See the CALLS TABLE. The key discipline this question demands: **"China property is a bubble,"
repeated annually for a decade, is not a call** — it is the genre Gordon Chang's *Coming Collapse
of China* (2001) exemplifies, revised and republished across missed deadlines (2011, then 2012)
and surviving every one of them `[2-SOURCE]`. A genuine call needs a date, a named mechanism, and
ideally a magnitude. On that bar: **Rogoff-Yang (Aug 2020)** offered a quantified macro-drag
estimate ~13 months ahead of Evergrande's default; **Stevenson-Yang/J Capital** offered a specific,
named-company thesis (2017) years ahead, plus a second dated call (Jan 2022) at the point the
downturn was visibly accelerating; **John Lam/UBS** offered the single most precisely-timed named
call (a SELL rating ~11 months ahead of default). Each of these is treated in this dossier as
*specific*, not *perennial*, because each carries a date, a mechanism and (for Rogoff-Yang and
Lam) a magnitude or an unambiguous single-name target.

## 8. Short sellers and trades that actually worked

The cleanest documented example of a call that worked and can be dated precisely is **John Lam's
UBS SELL rating on Evergrande** (~Oct 2020, ~11 months ahead of the Sept 2021 default) `[2-SOURCE]`
— though this is a published equity research rating, not a disclosed proprietary short position
with a stated realized return. The **magnitude of the trade that would have worked** is
well-documented on the equity side: Evergrande shares fell -99%, from a peak of HK$31 to under two
cents, before its Aug 2025 Hong Kong delisting `[2-SOURCE]`; Country Garden Services fell -71% in
2023 and Longfor Group -49% in 2023 `[1-SOURCE]`. On the **offshore high-yield bond** side, JPMorgan
estimated roughly 50 developers defaulted on about $100 billion of offshore bonds over the
subsequent two years `[1-SOURCE]` — real, large-scale distress that a distressed-debt buyer could
in principle have monetized, but **no search result in this set surfaced a specific named
hedge fund with a disclosed, realized profit figure from either the Evergrande equity short or the
offshore-bond distress trade** — this is stated as an honest gap rather than filled with an
unsourced number. Jim Chanos's Jan 2010 short (developers, banks, infrastructure, the Hang Seng)
did **not** work on the timeline he stated (crash expected late 2010/early 2011; the actual bust
came roughly a decade later); whether the position was maintained and eventually profitable on a
different horizon is not something this search record resolves.

## 9. Prominent forecasts wrong in both directions

**Perma-bears early by years to decades**: Jim Chanos (Jan 2010, expected imminent crash, actual
bust arrived ~2021); Kyle Bass (early 2016 yuan short, closed at a loss by May 2019, before any
subsequent currency move could have vindicated the direction) `[2-SOURCE]`; Gordon Chang (2001
book, specific collapse dates of 2011 then 2012, both wrong, a genre that has run over two decades)
`[2-SOURCE]`. **Bulls who dismissed the risk in advance**: this dossier searched specifically and
twice for named 2020-2021 bullish dismissals of Chinese property risk and **did not find one** —
what the search record contains instead is *later* re-bullish positioning after the worst appeared
to have passed (UBS's own John Lam turning positive again in Apr 2024; Goldman Sachs, UBS and BNP
turning "more positive" on Chinese equities generally ahead of the July 2024 plenum) `[1-SOURCE
each]`. These are recovery calls made well after the crisis was underway, not pre-crisis dismissals
of the risk, and this dossier flags the distinction explicitly rather than presenting a recovery
call as if it were an earlier mistaken bullish forecast.

## 10. What did the successful callers actually use as their indicator

The pattern across every call graded CORRECT in the table above is consistent: **none of them were
reading the price index.** UBS's John Lam and the PBoC/MOHURD "Three Red Lines" architects (Aug
2020) both centered on **developer balance-sheet ratios** — liability-to-asset, net-debt-to-equity,
cash-to-short-term-debt — i.e., leverage and liquidity metrics on named companies, not a market-wide
price series `[2-SOURCE]`. Rhodium's Logan Wright and Rogoff-Yang's NBER paper both worked from
**structural demand/demographic models** — decelerating urban household formation, an oversized
real-estate share of GDP and bank credit — producing a macro-drag argument rather than a price
call `[2-SOURCE each]`. The genuinely independent signals that moved ahead of or alongside the
official price series — land-auction failure/cancellation rates (tracked by CICC and financial
press since at least 2018), the July 2022 mortgage-boycott event, and presale-delivery-rate
estimates (Nomura's ~60% figure) — are all **cash-flow, completion-rate, or leverage proxies**,
deliberately upstream of the contested price index rather than a refinement of it. The practical
lesson for this desk: **the professionals who got the timing right were reading solvency and
completion data, not the price series** — directly consistent with this desk's own already-booked
finding (CI-D1..D5) that credit conditions lead property outcomes rather than the reverse.

---

## Gaps and cautions

- **WebFetch was not available for this dossier** (plan §0a) — every figure above is a
  search-snippet reconstruction, not a primary-document read; Chinese-language primary sources
  (the original 指导价/限价 municipal notices, MOF/MOHURD circulars) were inaccessible in English-
  language search and are named as a gap rather than approximated.
- **Gan Li's vacancy-rate methodology** was searched for direct criticism/retraction and none was
  found in this session; the only clearly-documented "disowning" event in this record is He Keng's
  Sept 2023 self-correction of the more extreme "3 billion people" figure, and the two should not
  be conflated.
- **No named hedge fund's realized, disclosed profit** from either the Evergrande equity collapse
  or the offshore-bond distress wave was found — a real gap, not filled with an invented number.
- **No pre-crisis (2020-2021) named bullish dismissal of China property risk** was found despite
  two dedicated search attempts; only post-crisis re-bullish positioning (2024) was located, and
  the two should not be conflated in any retrospective "bulls vs bears" scorecard.
- **Several individual figures rest on a single source** and are tagged accordingly throughout:
  the Shenzhen reference-price discount range, the "increased significantly" (unquantified) share
  of Shenzhen transactions closing below reference by 2023, the Hangzhou -25% figure, the cement
  output percentage (reported variously as ~10.5% and ~15% depending on framing), and the exact
  dates of the Shenzhen and Beijing land-cap relaxations.
- **The desk's own headline "-24.6% official vs ~-40% private" comparison** (`c-velocity.md`) is
  reaffirmed here as directionally consistent with everything found in this dossier, but its
  private leg remains `[1-SOURCE]` and should continue to be treated as a single point-in-time
  press comparison, not a validated, repeatable conversion constant — this dossier found no study
  that would upgrade it to `[2-SOURCE]` or turn it into a general rule.
