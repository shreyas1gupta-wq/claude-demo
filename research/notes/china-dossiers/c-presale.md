# C-PRESALE — The presale model and household mortgage debt: the liability that does not look like debt

*Dossier `c-presale` (CN programme, Half B). Compiled 2026-09-11. Direct motivation, stated by the
desk: `c-developers.md` established that presale/contract liabilities were **29.6% of Evergrande's**
peak total liabilities (≈CNY 721.5bn of CNY 2,437.4bn, end-2022) but **46.6% of Country Garden's**
(≈CNY 668bn of CNY 1,435bn) — and that this mechanical difference is a large part of why Country
Garden's Three Red Lines status stayed "Yellow" for years while Evergrande was "Red" from the
policy's own 2020 introduction. This dossier documents the mechanism in full: how presale actually
works, how big the liability is sector-wide, exactly how (and whether) it was excluded from each of
the Three Red Lines ratios, the 2021 escrow tightening, the August 2026 overhaul, unfinished units,
the 2022 mortgage strike, household debt levels, the mortgage-balance decline, and the 2022-23
prepayment wave.*

**Method, unchanged from the rest of Half B**: WebSearch only — **WebFetch is EGRESS_BLOCKED for
every domain** (plan §0a). Every figure below is a search-result-snippet reconstruction, not a
primary-document read. Corroboration rule applied throughout: load-bearing figures are tagged
`[2-SOURCE]`, `[1-SOURCE]`, `[RECALL — unverified]`, or `[DERIVED]` (a number this dossier computed
from two sourced inputs, not itself quoted anywhere). No figure is invented; where sources disagree
or a figure could not be pinned down, that is stated as a gap, not smoothed over. Today's date is
2026-09-11; every figure states its own as-of date. ~34 searches used against the ~30-38 budget.

---

## Headline findings

- **The Three Red Lines were blind to presale liabilities by explicit design, not by accident.**
  All three ratios are constructed so that advance receipts (contract liabilities) either get
  subtracted out or were never inside the definition to begin with (see the accounting table below).
  A developer could grow its presale book without limit and without moving a single one of the three
  ratios — the policy's debt-growth caps (0/5/10/15%/yr depending on how many lines are breached)
  bind only interest-bearing borrowing `[2-SOURCE]`.
- **Country Garden vs Evergrande is a real, quantified instance of that gap being used differently**,
  not just a theoretical possibility: 46.6% vs 29.6% presale share, "Yellow" vs "Red" status for
  years, comparable underlying distress once presale liabilities are added back `[2-SOURCE, this
  session + carried from `c-developers.md`]`.
- **Sector-wide, presale/contract liabilities are large and have been shrinking hard, not growing**:
  a 171-firm listed-developer sample held **CNY 4.17tn** in contract liabilities at end-2023 (down
  **22.7%** y/y, 22.1% of that sample's total debt); the same series peaked near **CNY 5.8tn in
  mid-2021** and had fallen to **≈CNY 3.6tn by mid-2024** (-38% from peak) `[1-SOURCE — a single
  Chinese brokerage/financial-media report syndicated across two outlets, not independently
  cross-checked against a second research house — see Gaps]`.
- **The August 2026 reform is real, dated, and already moving land-auction behaviour** — it raises
  the presale trigger to full main-structure completion and, critically, delays *both* escrow release
  *and mortgage-loan disbursement* until the project is completed and registered, closing the two
  channels (developer's own escrow draws, and incoming buyer mortgage cash) that funded construction
  under the old model `[2-SOURCE]`.
- **China's first-ever decline in outstanding mortgage-loan balances happened in Q2 2023** (-0.7% y/y
  to CNY 38.6tn, "the first quarter a year-on-year decline has been registered since central bank
  records began in 2004") and the balance has kept falling since, to **CNY 36.72tn by Q1 2026**
  `[1-SOURCE for the "first-ever" framing itself; the multi-year declining trend is corroborated
  across several independent data points — see §9]`.
- **Household debt/GDP and household debt/disposable-income tell different stories and this dossier
  keeps them separate**: debt/GDP has moved in a 58-63% band since 2020 and is *down* from its
  ~2023-24 peak; debt/disposable-income was last directly measured at essentially 100% (2018-vintage,
  possibly recycled in later reporting — see gaps), which is mechanically far higher than the GDP
  ratio because disposable income is itself a much smaller share of GDP than GDP is of GDP (obviously)
  — a distinction repeatedly collapsed in casual coverage.

---

## The Three Red Lines — where presale liabilities sit in each ratio (the crux)

| # | Ratio (Chinese name) | Formula | Threshold | Where do presale/contract liabilities (advance receipts, 预收款/合同负债) sit? |
|---|---|---|---|---|
| 1 | Liability-to-asset ratio **excluding advance receipts** (剔除预收款后资产负债率) | (Total liabilities − advance receipts) ÷ (Total assets − advance receipts) | ≤ 70% | **Explicitly subtracted from both numerator and denominator.** This is the *only* one of the three ratios presale liabilities touch at all, and they are touched by being **removed**, not counted against the developer `[2-SOURCE]`. |
| 2 | Net gearing ratio (净负债率) | (Interest-bearing debt − cash) ÷ Total equity | ≤ 100% | **Never enters.** Contract liabilities are not interest-bearing debt, so they were never inside this ratio's definition — not netted out, structurally absent `[2-SOURCE]`. |
| 3 | Cash-to-short-term-debt ratio (现金短债比) | Cash ÷ Short-term **interest-bearing** debt | ≥ 1x | **Never enters**, same reason as #2 `[2-SOURCE]`. |

**The gameability, stated precisely.** Because none of the three ratios responds to the *size* of a
developer's presale book, and because the policy's entire enforcement mechanism is a cap on how fast
*interest-bearing* liabilities may grow (15%/yr if compliant on all three, 10%/5%/0% for one/two/three
breaches) `[2-SOURCE]`, a developer facing the same growth ambition had a clean substitution
available: raise the money as buyer deposits (presale) rather than as bonds or bank loans, and none
of it moves any red line. This was not a hypothetical loophole discovered later — regulators
**designed ratio #1 to explicitly exclude advance receipts** on the theory that deferred revenue for
an unbuilt apartment is not the same as owing a bank or bondholder cash `[2-SOURCE]`, and the
Evergrande/Country Garden contrast (above) is the clearest available real-world instance of that
design choice separating two firms with comparably weak underlying balance sheets into different
Red-Lines colours for years. **What this dossier cannot claim more strongly than the evidence
supports**: whether firms *consciously* re-weighted toward presale financing specifically to avoid
red-line breaches (a causal claim about developer intent) versus presale simply being the cheapest
capital available to a leveraged developer regardless of the ratio's design (a demand-side
explanation) is not separately disentangled by anything sourced this session — both are consistent
with the same balance-sheet data, and the honest answer is that the *accounting made the substitution
free*, not that a specific memo proves anyone chose it for that reason.

**Sector-average evidence that the ex-advance-receipts ratio ran hot even while presale also
grew** `[1-SOURCE, Chinese-language financial press, this session — not independently
cross-checked against a second outlet]`:
- H1 2021 (listed-developer sample): **Red 19 / Orange 24 / Yellow 76 / Green 73** firms.
- Q2 2022 (an 80-firm sample): **35 firms** still breached the >70% ex-advance liability-to-asset
  test (down from 40/80 in Q2 2020); average cash-to-short-debt ratio **1.47**, with 36 firms still
  non-compliant on that test.
- End-2022 (top-100 listed developers): green-status rate still **under 30%**; average net gearing
  **174.8%**; average ex-advance-receipts liability-to-asset ratio **73%** — i.e., **above** the 70%
  threshold *on average across the top 100*, three years after the policy began.
- Context: authorities **quietly stopped requiring the monthly Three-Red-Lines reporting** in
  late January 2026 `[1-SOURCE — Trivium China]`, roughly contemporaneous with the August 2026
  presale overhaul — the whole framework appears to be winding down as the presale reform takes over
  as the sector's live regulatory lever.

---

## Household debt by year — GDP basis vs disposable-income basis (kept separate per the task's own instruction)

| As-of | Household debt / GDP | Source note | Household debt / disposable income |
|---|---|---|---|
| Dec-2008 | 17.6-20.6% (two vintages disagree) `[2-SOURCE, but the two figures don't reconcile — flagged]` | record low on this series | not sourced this far back |
| 2018 | 52.6% `[1-SOURCE]` | | **99.9%**, up from 93.4% in 2017 `[1-SOURCE, TradingEconomics]` |
| End-2020 | ≈62.2% `[1-SOURCE]` | CEIC-style vintage | not sourced |
| End-2022 | **61.9%** `[2-SOURCE — directly quoted by SCMP citing NIFD, and re-referenced in the 2023/2024 trend line]` | NIFD (PBoC-adjacent institution) | ~99.9% still being cited in 2023-dated coverage — **unclear if this is an updated figure or a recycled 2018 number** (see Gaps) |
| Q2-2023 | **63.5%** `[1-SOURCE, direct NIFD quote via SCMP]` | described as "approaching" the IMF's informal 65% household-debt-to-GDP warning line | — |
| ~Q1 2024 | peak, reported as **60.9-62.3%** depending on tracker (CEIC/TradingEconomics-style aggregators) `[2-SOURCE for "peaked around this point," decimal varies by tracker — flagged, not resolved to one number]` | | — |
| FY2024 | **61.4%** `[1-SOURCE, NIFD]` | | — |
| Q3 2025 | 59-59.7% (trackers vary) `[2-SOURCE]` | | — |
| Q4 2025 / end-2025 | **58-59.4%** (trackers vary) `[2-SOURCE]` | | — |
| Sep-2025 | 60.4% (a different tracker) `[1-SOURCE]` | broadly consistent with the high-50s/low-60s range above | — |

**Reading this table honestly**: the exact decimal for any given quarter varies by 1-3 percentage
points depending on which aggregator (CEIC, TradingEconomics, NIFD directly, or a press citation of
NIFD) is quoted, almost certainly reflecting GDP-base revisions and vintage differences rather than
real disagreement about direction. The *direction* is corroborated across every source found this
session: **a rise from roughly 20% (2008) to a peak somewhere in the 61-63% band (2023-2024), then a
mild, multi-quarter decline to roughly 58-60% (late 2025)** — i.e., household deleveraging is real and
recent, not merely asserted. **A directly-quoted BIS table cell was not obtained this session** — BIS
publishes a comparable "credit to households, % of GDP" series but `data.bis.org` could not be
fetched (WebFetch blocked), so every figure above is PBoC-adjacent (NIFD) or a commercial aggregator
citing PBoC flow-of-funds data, not a BIS print itself. This is stated as a gap, not disguised.

**Debt-to-disposable-income is the far weaker leg of this table.** The only concrete figure found
this session is **99.9%** — first seen dated to 2018 (TradingEconomics), and the same 99.9% figure
also appears in a 2023-dated SCMP piece alongside genuinely fresh 2023 GDP-ratio numbers, which
raises a real possibility that outlets are recycling the 2018 figure rather than reporting an updated
one. **No confirmed 2022-2025 update to the debt/disposable-income ratio was found** — a named gap,
not filled by guessing. A **derived, explicitly-labelled, non-quoted** cross-check: China's household
disposable income is commonly on the order of 43-45% of GDP (households' final consumption alone was
39.57% of GDP in 2023 per World Bank data, and consumption is necessarily less than disposable income
since some income is saved) `[1-SOURCE for the consumption share]`; mechanically, if debt/GDP sits
near 60% and disposable-income/GDP sits near 44%, debt/disposable-income should sit near
**60/0.44 ≈ 136%** `[DERIVED — not a quoted figure, illustrative only, do not cite as sourced fact]`.
This is offered only to show *why* the two ratios diverge as much as they do, not as a real 2025
data point.

---

## 1. How Chinese presale actually works

China's presale ("commodity housing pre-sale," 商品房预售) system dates to the **1990s**, adapted
from a Hong Kong-style off-plan sales model, and let developers fund rapid expansion by selling
homes before they were built `[2-SOURCE]`. At its peak, in **2020-21, presales accounted for nearly
90% of residential floor-space sales** nationally `[1-SOURCE — the figure recurred verbatim across
searches, likely one underlying analysis, so treated cautiously as 1-source despite repetition]`.
That share has fallen substantially since: **roughly two-thirds of new homes in 2025 were still sold
under construction** `[1-SOURCE]`, corroborated by a second, independently-worded figure putting
**presales at 68% of new-home sales by floor space in 2025** `[1-SOURCE]` — together treated as
`[2-SOURCE]` for "roughly two-thirds/68% in 2025." Separately, the **share of new homes sold as
completed units rose from 10.4% in 2021 to 32.5% in early 2024**, with over 30 cities running
completed-sales pilots since late 2022 `[1-SOURCE — Caixin, June 2025]` — consistent with, and the
mirror image of, the declining presale share above.

**Escrow rules as written.** Presale proceeds have been required by rule to be deposited into
government-supervised escrow accounts since the 1990s, with a commonly cited minimum retention of
**at least one-third of presale revenue** reserved for construction `[1-SOURCE]`. Critically,
**escrow supervision is administered locally (city/county level), not by one national rule with one
national percentage** `[2-SOURCE — this local-administration point is corroborated by both the
"cities tighten escrow access" reporting and the general framing that this is "an institutional
crisis" of overlapping local regimes]`; this is why actual practice varied so widely by city and
period (see §4).

**Legal and illegal access.** Legally, developers could apply to release escrowed funds against
verified construction progress (e.g., on reaching certain build milestones, or historically once a
project "topped out"). Illegally and systematically, **developers routinely diverted escrowed
presale cash into new land acquisition instead of completing the housing already sold**, aided by lax
local supervision and, in many documented cases, local-government tolerance of the practice as it
supported land-sale revenue `[2-SOURCE]`. This land-speculation channel intensified after roughly
2013 and is described as a *sector-wide, not firm-specific* practice — "all Chinese property
developers have systematically misappropriated large parts of customer prepayments to secure
landbanks" `[1-SOURCE]`.

---

## 2. The size of presale contract liabilities (合同负债) across the sector

**Firm-level anchors** (carried forward from `c-developers.md`, re-confirmed this session):
Evergrande ≈CNY 721.5bn (29.6% of total liabilities, end-2022); Country Garden ≈CNY 668bn (46.6%,
FY2022/2023 — independently re-confirmed via Statista this session, `[2-SOURCE]`); Vanke ≈CNY 408bn
(≈1/3 of total, Sep-2023).

**Sector-level (best available, not a full-sector figure)**: a sample of **171 listed developers**
held **CNY 4.17tn** in contract liabilities at **end-2023**, down **22.7% y/y**, equal to **22.1%**
of that sample's total debt (sample total liabilities: CNY 18.9tn, down 8.2% y/y); operating revenue
for the same sample was CNY 5.24tn (+2.0% y/y) `[1-SOURCE — a Chinese brokerage/financial-media
report, republished by two portals (Jiemian, Sina) that both appear to draw on the same original
research, so treated as one source, not two]`. The same series shows contract liabilities **peaking
near CNY 5.8tn in mid-2021** and falling to **≈CNY 3.6tn by mid-2024** (-38% from peak) `[same
1-SOURCE family`]. The stated drivers of the decline: the sales downturn eroding new bookings, and
the "guarantee delivery" (保交楼) policy pushing more completions-and-revenue-recognition through the
books, which converts contract liabilities into recognized revenue faster than new presales replace
them `[1-SOURCE]`. A supplementary metric from the same report: by end-2023, contract liabilities
covered only **0.80x** of that year's revenue recognized from completed sales (down from 1.05x the
year before) — i.e., **developers' forward revenue cushion from presales has fallen below 1x**,
flagged there as a warning sign of a thinning order book, not (on its own) a leverage metric.

**Flow-side context, not a stock figure**: developers raised **over CNY 6.6tn (≈$1tn) from deposits
and presales in 2020 alone** `[1-SOURCE]` — a single-year *flow*, not the outstanding *stock* of the
liability, and not to be confused with it. Separately, broader property-development-sector debt (not
presale-specific) was **CNY 33.5tn (≈$5.2tn) as of June 2021** per Nomura `[1-SOURCE]`.

**A true whole-of-sector (not just the 171 largest listed firms) stock figure for aggregate
presale/contract liabilities was not found this session** — the same gap `c-developers.md` recorded.
The 171-firm sample above is the best proxy obtained and is stated with that caveat rather than
presented as a sector total.

---

## 3. Why presale liabilities flattered reported leverage (see the accounting table above for the full mechanics)

Beyond the ratio mechanics already laid out: a contract liability (advance receipt) is booked as
**deferred revenue** when a customer pays before delivery — an obligation to deliver a completed
apartment, not a financial obligation to repay borrowed cash `[2-SOURCE, standard revenue-recognition
treatment]`. This is the accounting-theory justification regulators used for excluding it from ratio
#1's liability side. The practical consequence, stated by multiple sources independently: **a
headline "total liabilities" figure that includes presale liabilities (as most reported developer
totals do) systematically overstates what banks and bondholders are actually owed, while
simultaneously understating a very real, largely uncollateralized obligation to hundreds of thousands
of individual households** — an obligation invisible to any conventional leverage screen (including
all three red lines) until construction physically stops, at which point it surfaces all at once as
unfinished units, not as a debt-market default. This is precisely why Country Garden's headline
balance sheet read as safer than Evergrande's for years despite comparable underlying fragility once
presale liabilities are counted.

---

## 4. The post-2021 escrow tightening and the liquidity crunch it arguably caused

**Trigger and mechanism.** In **H2 2021**, as fears of contagion from Evergrande's distress spread,
many **local governments (city/county authorities) sharply tightened withdrawal rules on presale
escrow accounts** `[2-SOURCE]`. Because escrow is locally administered (§1), this tightening was
uneven but widespread. **Before the crisis, escrow typically held 50-70% of a developer's presale
funds** `[1-SOURCE, RBA-context sourcing]`; **after the tightening, senior executives at two named
developers reported 80-90%+ of their cash trapped in escrow**, versus roughly **30%** before mid-2021
`[1-SOURCE — an "exclusive" Reuters-sourced report]`. Regulators later acknowledged the overshoot: a
subsequent regulatory framework was designed explicitly to **"correct over-tightening" of escrow
accounts by city/county authorities** `[1-SOURCE]`.

**Why this is the mechanism the task names.** The escrow tightening arrived on top of, not instead
of, the Three Red Lines financing caps (Aug 2020) and the near-simultaneous freezing of the offshore
bond market to distressed developers — a three-way, near-simultaneous liquidity shock. The specific
irony: escrow rules exist to *protect* homebuyers' pre-paid deposits from being diverted (§1's
land-speculation problem); tightening them in 2021 did stop the diversion, but for developers already
dependent on recycling escrowed cash into ongoing construction and land purchases, the same tightening
cut off a working-capital channel they had structurally come to rely on — arguably *precipitating* the
very wave of stalled, "rotten tail" construction (§6) that strict escrow enforcement was meant to
prevent. This causal framing is the desk's own synthesis of the sourced facts above (the trapped-cash
percentages and the later "correct over-tightening" admission); no single source stated it in exactly
these words, and that is flagged rather than presented as a direct quotation.

---

## 5. The August 2026 presale-model overhaul

On **28 August 2026**, three national bodies — the Ministry of Housing and Urban-Rural Development,
the Ministry of Natural Resources, and the National Financial Regulatory Administration — jointly
issued new rules `[2-SOURCE — Caixin (two separate pieces) + CGTN + China Daily, converging on the
same date and bodies]`. The changes:

1. **Higher presale trigger**: developers must now complete the building's **main structure**
   (foundation, concrete flooring, and roof) — "topping out" — before presales may begin at all, a
   higher bar than the previous, looser standard.
2. **Escrow release delayed to full completion**: presale funds (down payments and mortgage
   proceeds together) must be deposited into supervised project accounts and are **not released to
   the developer until the project passes final inspection/completion** — previously, developers
   could already access these funds once the building topped out.
3. **Mortgage-loan disbursement delayed to completion**: personal housing loans for presale units are
   now to be issued **only after project completion is registered** — a direct closure of the second
   channel (incoming buyer mortgage cash, not just the developer's own escrowed deposit) that
   previously financed ongoing construction.
4. **Grandfathering**: projects with **planning permits obtained before 28 August 2026 are exempt**
   from the new threshold `[1-SOURCE]`.

**Is this a move to a completed-sales model?** Not by mandate — presale remains legal and the
existing pilot-city completed-sales programme (§1, 10.4%→32.5% completed-sales share 2021→early
2024) continues to expand gradually rather than being made compulsory nationwide. But the 2026 rules
push presale's *economics* much closer to a completed-sale model: a developer under the new regime
gets essentially no cash advantage from presale versus waiting for completion, since both escrow
release and mortgage disbursement now wait for the same trigger. This is a **de facto**, not **de
jure**, shift toward completed sales `[2-SOURCE for the overall characterization]`.

**Early market reaction**: at Beijing's first residential land auction after the rule change
(early September 2026), one parcel drew a competitive bidding war — China Resources Land paid nearly
CNY 8.3bn (≈$1.2bn) after 174 rounds, 17.4% above the reserve — while a second parcel was **abruptly
suspended** after two of three registered bidders failed to appear, attributed to developers
recalculating project economics under the new financing-timing rules `[1-SOURCE — Caixin]`. A
separate SCMP opinion piece explicitly warns the new rules risk **prolonging the sector downturn**,
since delaying developer cash access further reduces the incentive to launch new projects while land
sales revenue is already down 30.8% y/y (Jan-Jul 2026) `[1-SOURCE]`.

---

## 6. "Rotten tail buildings" (烂尾楼) — unfinished pre-sold units

The most-cited professional estimate, from **Nomura's Ting Lu**: **≈20 million units** of
unconstructed/delayed pre-sold homes nationwide, needing **≈CNY 3.2tn (≈$440bn)** to complete
`[2-SOURCE — this figure recurred independently in this session's search results and separately in
`c-developers.md`'s own sourcing of "20 million units and $446bn funding gap," a close but not
identical restatement, treated as corroborating]`. **Evergrande alone** is estimated to have left
**≈800,000 pre-sold homes unfinished** (a Wall Street Journal figure, via search synthesis)
`[1-SOURCE]`. By **end-2024, more than 1,660 Chinese developers had filed for bankruptcy**
`[1-SOURCE]`.

**A distinct, much larger number must not be conflated with the above**: developers pre-sold
**≈20 billion sqm** of floor space between September 2006 and December 2023 but had completed only
**≈12 billion sqm**, leaving **≈7.9 billion sqm** (≈100 million housing-unit equivalents) still to be
delivered `[1-SOURCE]`. This is the stock of **all pre-sold-but-not-yet-delivered** floor space,
including projects still on a normal construction timetable — **not** a "rotten tail" (stalled)
figure. Conflating the ~100 million normal-pipeline figure with Nomura's ~20 million genuinely-stalled
figure would overstate the crisis by roughly 5x; this dossier keeps them separate deliberately.

Government's own claimed remediation: **more than 1.65 million pre-sold units delivered** under the
national "guarantee delivery" (保交楼) programme `[1-SOURCE, carried from `c-developers.md`, itself
cross-referenced there against `c-facts.md`]`. **A lower-quality outlet's claim of "120 million"
unfinished/unstarted paid-in-full homes** was also found; this figure is materially inconsistent with
every professional estimate above and is flagged as unreliable rather than incorporated
`[1-SOURCE, low-reliability outlet — explicitly not adopted]`.

---

## 7. The 2022 mortgage-payment strike (停贷)

**Organizing.** Buyers of stalled, pre-sold projects coordinated primarily online — open letters,
and a crowdsourced tracking page (reported to be hosted on GitHub) listing affected projects — publicly
threatening to stop paying mortgages on unfinished homes unless construction resumed by a stated
deadline (one project group cited 20 October 2022) `[2-SOURCE]`.

**Scale.** At its peak, **more than 300 project/location boycott letters** were tallied nationwide,
spreading to **roughly 100 cities within about a month** of the first letters `[2-SOURCE — RFA +
NBC/other]`. Illustrative city-level counts cited: 12 projects in Chongqing, 7 in Shanghai, 8 in
Guangdong, 9 in Nanning, 10 in Taiyuan, with "hundreds of other locations" reported.

**State handling.** The response combined: (a) direct financial support — special loans from policy
banks earmarked for project completion, an onshore bond-guarantee scheme for selected developers,
state-owned enterprises taking over stalled projects, and local "bailout funds"; (b) monetary easing
— a PBOC policy-rate cut and lower mortgage-rate floors; (c) regulatory messaging — the banking
regulator (then CBIRC) telling banks to meet developers' "reasonable" financing needs `[2-SOURCE for
the financial-support package]`. **Not independently verified this session**: reports (widely
repeated in Western press at the time) that online organizing trackers and posts were subject to
censorship/takedowns — this dossier did not source that claim directly and flags it as a gap rather
than adopting it on recall.

---

## 8. China household debt as a share of GDP and of disposable income — see the table above

Full time series, sourcing, and the GDP-vs-disposable-income distinction are given in the dedicated
table above rather than repeated here. Two summary points: (i) the debt/GDP series **peaked in the
61-63% band around 2023-2024** and has since declined to roughly **58-60%** by late 2025 — genuine,
multi-quarter deleveraging, not a single data blip; (ii) the debt/disposable-income series is the
weaker leg of the evidence — the only concrete figure found (**99.9%**) may be a 2018-vintage number
still being recycled in 2023-dated coverage, and no confirmed fresh reading was found this session.

---

## 9. Outstanding residential mortgage balance in CNY trillion, and the first-ever decline

**Level and trajectory** (personal/individual housing mortgage loans specifically — not to be
confused with the broader "property loans" aggregate, which includes developer lending and ran at
**CNY 51.7tn** at end-March-2026, down 3.4% y/y `[1-SOURCE]`, a materially larger and distinct
figure):

| As-of | Outstanding personal mortgage balance | Change | Source |
|---|---|---|---|
| ~Q1 2023 | ≈CNY 38.94tn (reported all-time high on this series) | peak | `[1-SOURCE]` |
| Q2 2023 | CNY 38.6tn | **-0.7% y/y — the first y/y decline since PBOC records began in 2004** | `[1-SOURCE]` |
| FY2023 | CNY 38.17tn | -1.6% vs 2022 | `[1-SOURCE]` |
| FY2025 | — | -1.8% (further decline) | `[1-SOURCE]` |
| Q1 2026 | **CNY 36.72tn** | -0.8% further; -3.1% y/y | `[2-SOURCE]` |

**The "first-ever decline" claim itself** rests on one clearly-dated, clearly-attributed citation —
SCMP reporting the PBOC's own Q2-2023 quarterly lending report, explicitly stated as the first
year-on-year decline in personal mortgage loans "since central bank records began in 2004"
`[1-SOURCE, but a specific, dated, named-source claim rather than a vague recollection]`. The
subsequent multi-year decline (through FY2023, FY2025, and Q1 2026 above) is corroborated across
several independent data points converging on the same direction and rough magnitude, even though no
single source supplied the whole trajectory. **Cumulative decline, peak to Q1-2026**: roughly
CNY 38.9tn → CNY 36.72tn ≈ **-CNY 2.2tn, about -5.6%** over three years `[DERIVED from the sourced
peak and trough figures above — not itself a quoted "total decline" figure]`. Demand-side driver
named across sources: homebuyers took fewer new loans from Q1 2022 onward (zero-COVID disruption to
sales), and loan growth stayed weak even after reopening amid the broader economic slowdown
`[1-SOURCE]`.

---

## 10. The 2022-2023 mortgage prepayment wave, and negative equity

**Scale.** Total 2022 prepayments are put at **≈CNY 4.68-4.7tn** (≈$700-827bn depending on the
FX-rate and exact period used), equal to roughly **12%** (one source) or **14%** (a second) of the
**≈CNY 38.8tn** outstanding mortgage base at the time `[2-SOURCE for the CNY-denominated figure and
its rough order of magnitude; the exact percentage (12 vs 14) and USD conversion are not reconciled
between the two — flagged]`. Prepayments reportedly surged further, to an estimated **11.5%** rate,
by early 2023 as the economy reopened `[1-SOURCE]`.

**Why.** The core driver, cited consistently: a growing gap between the **rate on existing
mortgages** (sticky, often originated at 5.26-5.72% between Q4-2017 and Q1-2022 — a cohort covering
nearly half of all then-outstanding mortgages, ≈CNY 17.7tn) and both the **falling 5-year LPR
benchmark** and **falling returns on household savings/wealth-management products**. The gap between
the average existing mortgage rate and the LPR widened from **≈0.12pp (Oct-2019) to a peak ≈0.57pp
(2022)** `[2-SOURCE]`. With few better uses for savings, many households used their **own cash**
(not refinancing) to prepay — a genuine voluntary-deleveraging episode, working against the intent of
the era's rate cuts `[2-SOURCE]`.

**Response.** The PBOC intervened around **31 August 2023**, narrowing the existing-vs-new mortgage
rate gap to near zero (an economy-wide repricing of back-book mortgages) `[1-SOURCE]`. Separately, a
**dynamic adjustment mechanism** for first-time-buyer mortgage rates, established **January 2023**,
let individual cities lower their mortgage-rate floors, with many dropping below 4% `[1-SOURCE]`.

**Negative equity.** The only quantified projections found are from **UBS research**: negative-equity
housing units estimated to rise from **≈700,000 in 2025** (≈10% of that year's new-home sales) to
**≈1.8 million in 2026** (≈28%) to **≈3.3 million by 2027** (≈55%), with associated bank mortgage
losses rising from **≈RMB 34bn (2025)** to **≈RMB 232bn (2027)**; a related UBS estimate puts
potential foreclosures/repossessions at up to **2.4 million by 2027** `[2-SOURCE — reported
independently by two outlets (SCMP and Longbridge) with matching figures, though both cite the same
underlying UBS report, so this is one primary source confirmed by two independent re-reportings, not
two independent analyses]`. **No official (PBoC or NBS) negative-equity estimate was found** — this
remains bank-research territory only, a named gap.

---

## Gaps and cautions

- **No true whole-sector (beyond the largest ~171-300 listed firms) stock figure for aggregate
  presale/contract liabilities was found.** The 171-firm sample (§2) is the best proxy obtained, not
  a sector total, and it rests on one Chinese financial-media report family, not two independent
  research houses.
- **No BIS table cell was directly retrieved.** Every household-debt/GDP figure in §8's table is
  PBoC/NIFD-sourced or a commercial aggregator (CEIC/TradingEconomics) citing PBoC flow-of-funds
  data — `data.bis.org` could not be fetched under this session's WebFetch block. The task asked for
  figures "sourced to BIS or PBoC"; this dossier delivers the PBoC half solidly and flags the BIS half
  as unconfirmed rather than guessing at BIS's own published number.
- **The household debt-to-disposable-income ratio has no confirmed post-2018 reading.** The 99.9%
  figure may be stale and recycled rather than an updated 2022-2025 measurement; the ~136% figure
  offered in §8 is explicitly this dossier's own derived illustration, not a quoted fact, and must not
  be cited onward as if it were.
- **The exact original (1990s) escrow retention percentage was not pinned down precisely** — "at
  least a third" is the commonly cited figure, but sourcing could not confirm whether this was the
  literal original rule or a later refinement, and escrow administration is locally set in any case.
- **The causal strength of the "escrow tightening triggered the crunch it was meant to prevent"
  framing (§4) is this dossier's synthesis of sourced facts (trapped-cash percentages, the later
  "correct over-tightening" admission), not a single source's own stated causal claim** — presented
  as such, not smuggled in as a direct quotation.
- **Whether developers deliberately re-weighted toward presale financing specifically to game the
  Three Red Lines (a causal/intent claim) versus presale simply being the cheapest capital available
  regardless (a demand-side explanation) is not disentangled by anything sourced this session** — see
  §"the crux" discussion. The accounting fact (the ratios are structurally blind to presale liability
  size) is solid; the behavioral-intent claim is not separately proven here.
- **2022 mortgage-strike resolution outcomes** (how many of the 300+ projects were actually completed
  vs refunded vs still stalled, and any reports of organizer censorship) were not deeply researched
  this session and are not claimed.
- **The 12% vs 14% prepayment-share discrepancy (§10) and the several slightly different
  household-debt/GDP decimals across trackers (§8) were not resolved to one number** — presented as
  ranges with the disagreement stated, per the corroboration rule's instruction to record a genuine
  gap rather than force two sourced figures to agree.
- **The "120 million unfinished homes" figure (§6) was explicitly checked and rejected** as
  inconsistent with every professional estimate found, sourced only to a low-reliability outlet —
  named here so it is not mistaken for an oversight if it resurfaces elsewhere in the programme.
