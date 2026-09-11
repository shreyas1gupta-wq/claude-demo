# Indian Rental Yields, REITs, and the Unlisted-Developer-Leverage Gap

Agent dossier, India property programme (Half B), the yields/REITs/leverage cross-cutting leg —
per the plan (`research/frontier/india-property-plan.md` §0), the leg that connects the city work
to the desk's actual portfolio (SNAPSHOT-1's REIT allocation, CU/DB/CI batteries, the CN
programme's one named unknown). Compiled 2026-09-11.

**Tooling note (binding, per CLAUDE.md and §0a):** WebSearch only — WebFetch is EGRESS_BLOCKED for
every domain and was not attempted. Every figure below comes from WebSearch's indexed snippets,
not a directly re-fetched primary page; URLs are named but none were independently re-opened.
Corroboration rule applied throughout: `[2-SOURCE]` = two genuinely independent
outlets/searches converged on the number (including a same-direction figure from a different
named outlet); `[1-SOURCE]` = only one outlet surfaced it; `[RECALL — unverified]` = not found
in any search this session, stated only where necessary for context. Where a number is *this
dossier's own arithmetic* on sourced inputs (a spread, a discount-to-NAV, a distribution yield
computed from a company-reported per-unit distribution and an independently-sourced market
price), it is marked **[COMPUTED]** and the arithmetic is shown. All dates are as-of the date
named next to the figure; today is 2026-09-11 and several figures are already 1-3 months stale
at the source.

---

## Headline findings

- **India's rental-yield map is not one number but two irreconcilable families, exactly like the
  CN programme found for China.** Global Property Guide's own city cut has **Delhi (5.81%) and
  Kolkata (5.79%) as India's HIGHEST-yielding major cities**, above Bangalore and Hyderabad
  (~3.6-4.6%) and far above Mumbai (3.84%) `[2-SOURCE, GPG + a second aggregator both rank
  Delhi/Kolkata highest, though the second gives 6.19%/6.32%]` — the opposite of the "cheap
  tier-2/3 yields more" pattern the sibling city dossiers document at the micro-market level
  (Mumbai 2.0-4.0%, Hyderabad IT-corridor 2.5-4.2%, Ahmedabad 3.9%, Kochi 4.6-6%, Indore up to
  8%). Both are real; they are measuring different housing stock (see §1).
- **The carry spread is structurally far wider negative than China's**, but the exact number is
  sensitive to which yield and which mortgage rate is used: on a representative urban
  prime-residential yield (~3.0-4.0%) against a realistic current effective home-loan rate
  (~8.0-8.5%), the spread is **[COMPUTED] roughly −4.5 to −5.5pp**; on the national GPG blended
  yield (5.16%) against the best advertised rate (7.10%), it narrows to **[COMPUTED] about
  −2.0pp**. Either way it sits well below the CN programme's own China figure of **−1.3pp** (LPR
  basis) / **−0.9pp** (effective-rate basis) `[booked, c-yield.md Q3]`. Indian home-loan rates
  have also fallen sharply — 125bp of RBI cuts through 2025 leave best rates at **7.10-8.45%**
  `[2-SOURCE]`, materially below the 8-9% this task's own brief assumed.
- **Four large listed REITs' current [COMPUTED] distribution yields on market price run
  4.8%-6.2%** (Mindspace lowest, Brookfield highest) — **below India's 10-year G-sec (6.96-7.10%,
  Sep-2026)** `[2-SOURCE]`, i.e. a *negative* running-yield spread versus the risk-free rate,
  the same shape China's C-REITs showed against its own bond market. Three of four trade at a
  **discount to NAV (−5% to −11%)**; only Nexus (retail) trades at a small **premium (+2.1%)**
  `[COMPUTED from company-reported NAV + market price, both 1-SOURCE inputs]`.
- **No residential or retail-residential REIT exists in India** — confirmed, not merely repeated
  from an earlier leg `[2-SOURCE]`. All four large REITs plus the new fifth (Knowledge Realty
  Trust, listed Aug-2025) are office or retail; all three listed SM REIT schemes found are single
  commercial-office assets.
- **Total-return-since-listing figures for the REITs conflict by wide, unreconciled margins** —
  most sharply for Nexus, where three sourced figures (+39% price-only-style, +80% cumulative
  with distributions, +29.3%/yr annualized) cannot all be true simultaneously (29.3%/yr over the
  ~3.3 years since May-2023 listing compounds to roughly +120%, not +39% or +80%). None is
  preferred here; this is flagged, not resolved, per the task's own instruction.
- **What is knowable about unlisted tier-2/3 developer leverage is an aggregate, not a segment**:
  RBI publishes bank-system commercial-real-estate credit (₹6.7 lakh crore, +21.5% YoY, Jul-2026)
  and system-wide NPA ratios (near multi-decadal lows), and ICRA/CRISIL publish leverage ratios
  for their **rated** developer universe (debt/CFO <3x) — but no source in this pass segments
  any of that by listed-vs-unlisted or tier-1-vs-tier-2/3, confirming rather than closing the CN
  programme's named gap: the segment most analogous to China's defaulted developers is exactly
  the one with no public aggregate.

---

## PART 1 — CITY YIELD TABLE (gross residential, unless marked)

| City | Gross yield | As-of | Method / source | Tag |
|---|---|---|---|---|
| **India, national average** | **5.16%** (up from 5.09% Q4-2025) | Q2 2026 | Global Property Guide (GPG): median annual asking rent ÷ median asking purchase price, biannual, 1/2/3-BR units | `[1-SOURCE]` |
| Delhi | 5.81% (GPG) / 6.19% (2nd aggregator) | 2026 | GPG asking-price ratio; 2nd figure same method, different sample cut | `[2-SOURCE, direction; point estimate differs 5.81 vs 6.19]` |
| Kolkata | 5.79% (GPG) / 6.32% (2nd aggregator) | 2026 | GPG; South/East Kolkata micro-markets (Salt Lake, New Town, Ballygunge) cited at 5-7% | `[2-SOURCE, direction; point estimate differs]` |
| Bengaluru | 4.45% (Anarock, Q1 2024) → est. 4.6-5.0% (2025/26); citywide 3.6%→4.6% (2019→Q2'26, GPG-derived) | 2024-2026 | Anarock survey; GPG city trend | `[2-SOURCE]` |
| Hyderabad | citywide 2.6%→3.6% (2019→Q2'26, GPG-derived); IT-corridor (Gachibowli/Kondapur) 3.8-4.2% | 2026 | GPG trend; portal/news IT-corridor estimate — matches sibling dossier's 2.5-4.2% | `[2-SOURCE]` |
| Pune | citywide 3.0-4.3% (several cuts); Hinjewadi/Kharadi IT corridor 4.0-4.4% (one cluster) vs 5.5-6% (another) | 2024-2026 | Portal aggregates; sibling dossier flags the same IT-corridor split as unresolved | `[1-2 SOURCE, internally conflicting — see ahmedabad-pune.md §8]` |
| Chennai | 4.05-4.16% (Magicbricks OND'25 topped the index at 4.16%, up from 3.78% OND'24) | Q4 2025 | Magicbricks Rental Index | `[1-SOURCE]` |
| Mumbai (citywide) | 3.84% (GPG) | 2026 | GPG; sibling dossiers give the micro-market spread this citywide figure sits inside: SoBo/Malabar Hill 2.0-3.0%, Bandra West 2.0-2.5%, Powai/Chembur 3.0-3.5%, Malad/Goregaon corridor 4-5% | `[2-SOURCE]` |
| Gurugram | 4.1% | 2024/25 | News-syndicated developer/broker survey | `[1-SOURCE]` |
| Noida | 3.7% | 2024/25 | Same survey family as Gurugram | `[1-SOURCE]` |
| Ahmedabad (citywide) | 3.9% — cited as the **highest of any major Indian city** in this particular survey | 2024 | Magicbricks / Business Standard — already booked in `ahmedabad-pune.md` | `[2-SOURCE, in-programme]` |
| Lucknow (Gomti Nagar) | ~3% | 2025/26 | Already booked in `hyderabad-lucknow.md` | `[2-SOURCE, in-programme]` |
| Kochi (Kakkanad IT belt) | 4.6-6% | 2025/26 | Already booked in `candidate-screen.md` §13 | `[1-SOURCE, in-programme]` |
| Indore (Nipania / Super Corridor) | up to 8% (one of the more credible high-yield prints in the whole screen) | 2025/26 | Already booked in `candidate-screen.md` §13 | `[1-SOURCE, in-programme]` |

**Read this table exactly the way c-yield.md read China's**: it is **two families of numbers, not
one**. GPG's own asking-price-ratio method puts Delhi and Kolkata — cities with a large stock of
older, lower-capital-value housing — at the TOP of the national ranking, while portal/broker
surveys of the specific micro-markets investors actually buy into (Gurugram, Bengaluru IT belt,
Mumbai suburbs) cluster distinctly lower (2-5%). No source in this pass reconciles the gap;
the most defensible explanation, not itself sourced, is that GPG's sample (median asking
rent/median asking price across a city's full listing set) is diluted toward older/cheaper units
with a structurally higher rent-to-price ratio, while portal city-averages for "the" rental yield
are usually built from the newer, higher-capital-value stock that dominates transaction volume and
media coverage — the same kind of sample-composition gap the CN dossier flagged between GPG and
domestic-press China figures.

## PART 2 — REIT TABLE

| Name | Type | Distribution yield [COMPUTED on price] | NAV premium/discount [COMPUTED] | Occupancy | WALE | Total return since listing | Source(s) |
|---|---|---|---|---|---|---|---|
| **Embassy Office Parks REIT** | Office | FY26 distrib. ₹25.28/unit ÷ price ₹439.6 (10-Sep-26) = **5.75%** (5.14% on NAV ₹491.62) | ₹439.6 vs NAV ₹491.62 = **−10.6%** discount | 90% (FY27 guided 95-96%) | 8.5y | +24% price-only since Apr-2019 `[1-SOURCE]`; annualized total-return-incl-distributions NOT isolated in this pass (only a cross-REIT "11-29%" range found) | Company earnings release Q4FY26, indmoney, wealthease-style aggregator |
| **Mindspace Business Parks REIT** | Office | FY26 distrib. ₹24.09/unit ÷ price ₹498.3-499.6 (2-3 Sep-26) = **4.83%** (4.57% on NAV ₹527.0) | ₹499 vs NAV ₹527.0 = **−5.4%** discount | 95.3% committed (Q3FY26); 91.9% proforma post-acquisition | 6.9-7.4y (recent cut 7.4y) | +18% price-only since Aug-2020 `[1-SOURCE]`; **CONFLICTING** total-return-incl-distributions: 16.1%/yr annualized `[1-SOURCE]` vs a separate "CAGR 8.85%, 5y total return >52%" `[1-SOURCE]` — not reconciled | Mindspace FY26 annual report, company press releases, two different return aggregators |
| **Brookfield India Real Estate Trust** | Office | FY26 distrib. ₹21.40/unit ÷ price ₹342.7-343.6 (24-25 Aug-26) = **6.24%** (5.53% on NAV ₹386.7) | ₹343 vs NAV ₹386.7 = **−11.2%** discount | 96% committed FY26; ~93% on enlarged Jun-2026 portfolio (32.6 msf) | 6.7y (Jun-2026) | "+6%" price-only since Feb-2021 cited `[1-SOURCE]` — **but this dossier's own check** (listing price ₹279 vs current ~₹343 = +23%) does not match that figure; flagged as an unresolved source error, not adopted | Company Q1FY27 update, screener.in, business-standard listing-day report |
| **Nexus Select Trust** | Retail | FY26 distrib. ₹9.081/unit ÷ price ₹167.5 (8-Sep-26) = **5.42%** (5.54% on NAV ₹164.00) | ₹167.5 vs NAV ₹164.00 = **+2.1% PREMIUM** — the only one of the four | 97.2% (FY25) | not found this pass — gap | **THREE CONFLICTING figures since May-2023 listing**: "+39%" (implied price-only) `[1-SOURCE]`; "+80% total returns, ₹19.853/unit distributed" `[1-SOURCE]`; "+29.3%/yr annualized incl. distributions" `[1-SOURCE]` — internally inconsistent (29.3%/yr compounds to ~+120% over 3.3y, not +39% or +80%); none adopted | Nexus FY26 results, distribution-history page, two separate return aggregators |
| Knowledge Realty Trust (new, 5th REIT) | Office | too new for a meaningful trailing yield — ₹1.56/unit first (partial-period) distribution against a ₹103 listing price | not computed (single data point) | 92% H1FY26 (city split: Hyderabad 99%, GIFT City 98%, Chennai 95%, Mumbai/Bengaluru/Gurugram ~88%) | not found | Listed 18-Aug-2025 at ₹103 (+3% listing pop from ₹100 IPO price); largest office REIT by GAV (~₹62,000 cr) `[1-SOURCE]` | IPO/listing coverage, Q2FY26 press release |

**Read across the four established REITs**: distribution yields on current price cluster
**4.8-6.2%**, all below the current 10-year G-sec (6.96-7.10%, Sep-2026) — a **negative** running
yield spread to the risk-free rate `[COMPUTED, both legs sourced]`. Three of four trade at a
meaningful discount to their own disclosed NAV (−5% to −11%); only the retail REIT (Nexus) trades
at a small premium. The total-return-since-listing figures are the least reliable numbers in this
whole dossier — every one of the four has at least one internally-inconsistent or unreconciled
figure in this search pass, and Brookfield's own "+6% since listing" fails this dossier's own
arithmetic check against its ₹279 debut price. Treat every since-listing total-return figure above
as directional only.

---

## 1. City-by-city gross residential rental yield table, with method

See the table above. The two-family split (GPG-style asking-ratio vs portal/broker "the yield in
this city" figures) is the central finding, not a footnote — anyone quoting "India's rental
yield" needs to say which family. **National GPG blended: 5.16% (Q2-2026), up from 5.09% (Q4-2025)
and 1.7%-equivalent-scale-irrelevant** (compare with China's own asking-based national yield of
~2.6% on the same GPG methodology, `[booked, c-yield.md]` — India's GPG national figure runs
roughly double China's on a like-for-like method). No India-specific 2015 or 2019 GPG baseline was
retrieved this pass to build a multi-year national GPG series (a gap, matching the CN dossier's
own inability to source a 2015 China baseline).

## 2. Are Indian yields rising or falling? The decomposition

Two things are true at once, at two different time horizons, and they should not be blended into
one sentence:

- **Multi-year (2021-2025), PRICES won**: Anarock reports capital values in India's top housing
  markets rose ~128% cumulative 2021-2024 in aggregate `[1-SOURCE]`, and separately that rents in
  many micro-markets "lagged significantly" over the same window, continuing into late 2025 in
  Bengaluru, Delhi-NCR and Hyderabad specifically `[1-SOURCE]` — i.e. **yield compression** at the
  micro-market level even where rents were also rising in absolute terms (the sibling dossiers'
  own observation that IT-corridor rents rose sharply post-2021 is consistent with this: rents
  rose, prices rose faster). NHB RESIDEX's own 50-city house price index shows this is not
  uniform — Delhi +14.9% YoY, Bengaluru/Chennai/Pune +10-16% YoY, Kolkata **−6.6%** (a genuine
  contraction) in the most recent read (Q1 FY26) `[1-SOURCE]` — so "prices rose faster than rents"
  is a hot-metro statement, not a national one.
- **Latest quarter (Q4-2025), a small reversal shows up in the aggregate GPG series**: national
  property values +2.2% QoQ against rental demand −2.4% QoQ `[1-SOURCE]` — a genuine, if small,
  yield-compressing quarter — while the GPG *yield* series itself actually ticked UP 5.09%→5.16%
  over roughly the same window `[1-SOURCE]`. These two facts sit in tension (a compressing quarter
  should show up as a falling yield) and were not reconciled by any single source in this pass;
  read the GPG yield uptick as the more reliable aggregate signal (it is the yield series itself,
  not a derived price-vs-rent inference) and the "prices up/rents down" quarterly read as the
  weaker, unreconciled data point.
- **Net-net**: over the multi-year window that matters for a portfolio decision, **capital values
  have out-run rents in the hot metro corridors** (yield compression, consistent with the
  micro-market yield figures the sibling dossiers already document), while the **national blended
  yield has actually drifted up slightly** in the last 1-2 years — because the national blend is
  increasingly diluted by cheaper, higher-yielding stock (older Delhi/Kolkata housing) even as the
  premium segment compresses. This is the same shape as several already-booked desk findings
  (VAL-D6's "every yield measure inverts in small caps," the EW-survivor artifact family) —
  a blended aggregate can move opposite to its own best-known constituents.

## 3. Yield versus the mortgage rate — the carry spread, computed explicitly

```
Current home-loan rates (Sep-2026), sourced:
  best advertised rate (top public-sector banks)   =  7.10% p.a.
  SBI / HDFC representative                        =  7.20-8.45% p.a.
  RBI repo rate (Apr-2026, unchanged)               =  5.25% (125bp of cuts through 2025)

CARRY SPREAD = gross rental yield − home-loan rate

(a) National blended yield vs best advertised rate:
    5.16% (GPG national, Q2'26) − 7.10% (best rate)      = −1.94pp  [COMPUTED]

(b) National blended yield vs a realistic representative rate (mid-band, not the teaser floor):
    5.16% − 8.0% (mid of 7.2-8.45% band)                  = −2.84pp  [COMPUTED]

(c) Representative urban PRIME residential yield (the figure most investors actually face —
    Mumbai/Bengaluru/Hyderabad-type stock, not the GPG national blend) vs the same mid-band rate:
    ~3.0-4.0% (this dossier's own city table, prime segment) − 8.0%   = −4.0 to −5.0pp  [COMPUTED]

For comparison, the CN programme's own China figure (booked, c-yield.md Q3):
    2021: 1.70% − 4.65% (5yr LPR)           = −2.95pp
    now:  2.20% − 3.50% (5yr LPR)           = −1.30pp
    now:  2.20% − 3.08% (effective rate)    = −0.88pp
```

**Read**: depending on which Indian yield is used, the carry spread runs from about **−2.0pp**
(optimistic: national blended yield, best advertised rate) to **−5.0pp** (realistic: prime urban
residential yield, representative effective rate) — in every framing, **wider negative than
China's current −0.9 to −1.3pp**, and even wider than China's own 2021 pre-crash reading
(−2.95pp) once the realistic Indian inputs are used. The gap is NOT primarily a rate-side story
the way China's improvement was (India's rates have also fallen — 125bp of cuts through 2025,
now 7.10-8.45% vs a materially higher pre-cut level, and below this task brief's own assumed
8-9%) — it is a **yield-side** story: India's yields, even at the high (national-blended) end,
sit near where China's sat only in the most stressed post-crash reading of its yield series.
This is the single most portfolio-relevant number in Part 1: unlevered Indian residential property
purchased with a mortgage has a materially worse running cash-carry than China's property market
does even today, post-crash.

## 4. Net versus gross yield

Sourced tax/cost mechanics `[2-SOURCE, tax-guide sites converge on the statutory mechanics]`:
- **Section 24(a) standard deduction**: a flat **30% of Net Annual Value** (rent minus municipal/
  property tax), regardless of actual expenses — no separate deduction for repairs or
  maintenance is allowed on top of it.
- **Society/maintenance charges are NOT deductible** beyond the 30% standard deduction when paid
  to a society (not a local authority) — a materially different (worse) tax treatment than many
  investors assume.
- **Vacancy allowance**: rent actually foregone due to vacancy is excluded from Gross Annual
  Value for the vacant period — softens, but does not eliminate, the cash cost of an empty unit.
- A rental-yield-calculator source gives representative CASH cost assumptions used in practice:
  maintenance ~1-2%/yr of property value, plus society charges, property tax, an assumed 5-10%
  vacancy loss, insurance and tenant-finding brokerage `[1-SOURCE]`.

**[COMPUTED], this dossier's own build, using the above sourced inputs — not itself a sourced
single figure**: starting from a representative **4.0% gross** yield (a mid-city, non-outlier
figure from the table above):
- less society/maintenance + property tax + vacancy allowance (roughly 1.2-1.6pp of property
  value/yr on the cited assumptions) → a **cash net yield of roughly 2.4-2.8%** before any income
  tax;
- income tax then applies to 70% of Net Annual Value at the owner's marginal slab (30% flat
  deduction, no depreciation shield) — for a top-bracket taxpayer this removes a further
  meaningful slice of the already-reduced cash flow, landing an **all-in, after-tax, in-pocket
  yield in the rough neighbourhood of 2.0-2.4%** on a 4.0% gross starting point.
This is a back-of-envelope construction on sourced statutory mechanics and cost assumptions, not
a sourced single "Indian net yield" figure — no source in this pass published one directly, which
is itself worth naming as a gap: **the net/gross gap for Indian residential property is
computable but not, as far as this search pass found, published as a single headline number
anywhere**, unlike the REIT distribution-yield-vs-NAV-yield distinction which IS explicitly
published (§5-8 below).

## 5. Embassy, Mindspace, Brookfield, Nexus — resolved and unresolved

See the REIT TABLE above for the full comparison. Summary of what this leg specifically
**resolves** versus what SNAPSHOT-1's programme flagged as a 2-4pp conflict:
- **Distribution yields computed here on same-week price + latest company-reported per-unit
  distribution** (Embassy 5.75%, Mindspace 4.83%, Brookfield 6.24%, Nexus 5.42%) are internally
  consistent with each other (same method, same rough date, same primary-source distribution
  figures) and can be treated as the dossier's best resolution of the "distribution yield"
  question specifically — narrower spread (4.8-6.2%) than the ~2-4pp conflict the earlier leg
  flagged.
- **What remains genuinely unresolved**: (i) total-return-since-listing figures, where three of
  four REITs carry internally-inconsistent numbers across sources (worst on Nexus, see table);
  (ii) NAV growth-rate framing for Mindspace (a "+22% YoY" NAV claim and a separate "+9% in six
  months" claim do not obviously share a base period); (iii) a generic "REITs yield 6-9%,
  Brookfield/Nexus 7.5-9% vs Embassy/Mindspace 7-8%" claim from one blog-style aggregator
  `[1-SOURCE]` that **contradicts this dossier's own [COMPUTED] figures outright** (actual
  computed range is 4.8-6.2%, and Brookfield — not the aggregator's claimed "7-8%" pair — is
  the highest at 6.2%, not Nexus) — flagged as a likely stale or issue-price-based secondary
  claim, not adopted.

## 6. The SM REIT / fractional-ownership regime

SEBI notified the SM REIT (Small and Medium REIT) framework in **March 2024** `[2-SOURCE]`,
regulating fractional-ownership platforms (FOPs) that pool investors into SPVs holding single or
few commercial assets valued **₹50-500 crore**, mandating exchange listing, 95% cash-flow
distribution, an independent trustee, and a **₹10 lakh minimum lot size**. What has actually
listed, per Property Share (the platform running all schemes found this pass):
- **PropShare Titania** (listed Aug-2025): a 0.45 million sq ft Grade-A+ office asset in Thane,
  Mumbai; projected distribution yield **~9.0% FY26-FY28**, compressing to **8.7% FY29**
  `[1-SOURCE]`.
- **PropShare Platina** (IPO opened Jul-2025, ₹473 crore, 1.61x subscribed) `[1-SOURCE]`.
- **PropShare Celestia** (listed Apr-2026, India's 3rd SM REIT scheme): a 0.21 million sq ft
  Grade-A office asset in Ahmedabad; projected distribution yield **8.1% FY26 rising to 8.9%
  FY29**; one headline describes it as having "listed at a discount" `[1-SOURCE]`.
- Aggregate: the three schemes have distributed **>₹68 crore** cumulatively and combined AUM has
  **tripled to ₹1,070 crore** `[1-SOURCE]`.

**Every SM REIT asset located in this search is single-asset COMMERCIAL OFFICE, not residential**
— the framework exists and is being used, but not (yet) for residential exposure. Projected
yields (8-9%) are meaningfully above the large listed REITs' [COMPUTED] 4.8-6.2%, consistent with
a smaller, single-asset, thinner-liquidity vehicle needing to price in an illiquidity/concentration
premium — but these are **prospectus-style projections, not multi-year realized track records**
(the oldest scheme is roughly one year old), a materially weaker evidence standard than the large
REITs' several years of reported history.

## 7. Is there a residential or retail-residential REIT in India?

**Confirmed: no.** `[2-SOURCE]` As of Sep-2026 there are five large listed REITs (Embassy,
Mindspace, Brookfield, Nexus, and the newly-listed Knowledge Realty Trust — Aug-2025) — four
office-focused and one (Nexus) retail — plus three SM REIT schemes, all single commercial-office
assets. No source in this pass named any residential or mixed retail-residential REIT structure,
listed or in registration; one outlook piece explicitly frames residential REITs as a future,
unrealized possibility, not a current category. This corrects nothing from the earlier SNAPSHOT-1 /
CN-programme leg — it independently reconfirms the same negative finding on a fresh search pass.

## 8. REIT yields vs direct-property yields vs the G-sec — the actual investment question

```
Direct residential (Part 1):        national blended 5.16% (GPG); realistic prime-urban 3.0-4.0%
Large listed REITs [COMPUTED]:      4.8% (Mindspace) to 6.2% (Brookfield); cluster ~5.0-6.0%
SM REIT (PropShare), projected:     8.1-9.0%
India 10-year G-sec (Sep-2026):     6.96-7.10%  [2-SOURCE]
```

**Read**: the four large listed REITs currently offer a running yield **below the risk-free
rate** — a negative spread of roughly **−0.7 to −2.2pp to the G-sec**, [COMPUTED] on the figures
above — which only makes sense if held for the NOI-growth/re-rating case (double-digit NOI growth
across the sector this leg found, 15-37% YoY by REIT) and the NAV-discount margin of safety
(three of four trade 5-11% below disclosed NAV). Direct residential property, even at the
optimistic national-blended yield, sits at or below that same REIT range and well below the
G-sec — i.e., **on pure running income, both direct residential property and the large listed
REITs currently pay less than a risk-free government bond**; only the SM REIT segment's projected
8-9% clears the G-sec with a positive spread, and that comes with single-asset concentration risk,
a sub-two-year track record, and a much thinner secondary market that a G-sec comparison does not
otherwise price in. **This is the actual investment question the SNAPSHOT-1 gap left open, and the
answer this leg finds is: none of India's investable property-income vehicles currently clear the
risk-free rate on a like-for-like running-yield basis, except the newest and least-tested one.**

*Cross-country anchor, applying the desk's own already-booked base rate (CN-D2, not re-run here):*
the JST 18-country panel's rental yield through property boom-bust cycles has a median **peak
yield of 3.29% (modern era) / 3.78% (full sample)** and a median **trough yield of 4.94% (modern) /
5.23% (full sample)** `[booked, trial-ledger.md CN-D2]`. India's own national blended yield
(5.16%) already sits **above** that panel's trough band — i.e., by this single cross-country
yardstick, Indian residential property nationally is priced more like a post-bust trough than a
pre-bust peak. But the hot metro/IT-corridor micro-markets this leg and the sibling dossiers
document (Mumbai 3.84%, Bangalore/Hyderabad prime 3.5-4.2%) sit close to the panel's **peak**
band — the specific segment the JST panel treats as a compressing-yield warning marker is the
premium urban segment, not India as a whole. This is a descriptive cross-check against an
already-registered base rate, not a new trial and not a forecast — consistent with the ER-arc's
standing doctrine against point forecasts.

## 9. What is actually knowable about unlisted developer leverage

- **Bank credit to commercial real estate**: ₹6.7 lakh crore outstanding (Jul-2026), **+21.5%
  YoY**; banks added ₹42,142 crore Mar-Jul 2026 while NBFC commercial-real-estate credit
  **contracted** ₹4,284 crore over the same window — banks, not NBFCs, are now the marginal
  financier of this segment `[1-SOURCE, Sep-2026 report]`. Real estate + infrastructure together
  are ~25% of total bank credit exposure, a level RBI itself has flagged as a concern
  `[1-SOURCE]`.
- **System-wide asset quality is at multi-decadal strength** — gross NPA 1.8-2.15% (Jun-2026 /
  Sep-2025); public-sector-bank gross NPA fell from 9.11% (Mar-2021) to 2.58% (Mar-2025), credited
  to the combined effect of IBC, SARFAESI enforcement and recapitalisation `[2-SOURCE]`. **No
  source in this pass isolates a real-estate-developer-specific or unlisted-tier-2/3-specific NPA
  figure** — construction/real estate appears only folded into an undifferentiated "top-100
  defaulters" statement alongside manufacturing and energy. This is the direct, confirmed answer
  to the question: the aggregate is public and healthy-looking; the segment the CN programme
  flagged as unknown remains, in this pass, genuinely unmeasured, not merely unresearched.
- **Post-IL&FS legacy book**: roughly **₹3.5 lakh crore (~$50bn)** of developer loans were still
  on NBFC/HFC books as of the (2019-2020-vintage) sourcing found this pass, being run down via
  sales to special-situation funds; after the 2018 IL&FS shock, developer borrowing costs from
  NBFCs rose 200-300bp (to 18-19%), with private equity/AIF lenders filling the gap at up to 23%
  `[1-SOURCE, dated]`. **No current (2025/2026) updated figure for the size of this legacy book
  was found** — a named, specific gap, not an assumption.
- **Rating-agency leverage coverage exists but is architecturally the wrong universe**: ICRA's
  own commentary puts its rated developers' total debt/CFO at **below 3x** through FY26-27
  `[1-SOURCE]`, and CRISIL projects the debt-recovery rate on *stressed* realty assets improving
  from 22% (FY25) to 38% (FY26) `[1-SOURCE]` — but a rated universe is, by construction, the
  larger and more capital-markets-connected end of the developer population; it structurally
  excludes the true unlisted tier-2/3 firms that never issue rated paper, which is precisely the
  segment named as unknown. This is the same shape of ceiling the desk's own Earnings Quality
  Atlas found for India fundamentals data (a schema limitation, not a one-off gap) — now
  confirmed for developer credit specifically.
- **A systemic transmission channel, sector-non-specific but relevant**: RBI's Dec-2025 Financial
  Stability Report flags banks now acquiring roughly **80% of NBFC-originated assets** via
  co-lending/direct-assignment/securitisation, with **acquired pools showing weaker credit
  performance than banks' own originations** at public-sector banks specifically `[1-SOURCE]` —
  a channel through which NBFC-sourced risk (potentially including real-estate-adjacent exposure)
  can transmit into bank balance sheets without a clean public trail back to the original
  developer segment.
- **SARFAESI/IBC case counts specific to real estate were not isolated** — general NCLT/IBC data
  (1,898 ongoing CIRP cases system-wide, average resolution time now ~9 months/688 days, a recent
  Supreme Court ruling framing IBC as "a forum of last resort... not a debt-recovery tool" for
  real estate specifically) was found, but no sector-segmented count of real-estate CIRP or
  SARFAESI-enforcement cases was located this pass — another named, specific gap.

**Bottom line on Q9**: the aggregate is knowable and currently benign-looking (bank exposure
growing, system NPAs low); the specific unlisted tier-2/3 developer-leverage segment the CN
programme flagged remains, after a dedicated search pass, exactly as unknown as it was — this
leg narrows the gap to precisely where it lives (no rated-agency, no RBI, no NCLT source
segments by listed-status or by tier) rather than closing it.

## 10. How concentrated has Indian development become?

Every cut of the data agrees on **direction**, but the cuts use different metrics and bases, so no
single number should be read as "the" consolidation ratio:

| Cut | FY17/FY20 | FY21 | FY25/26 |
|---|---|---|---|
| Top-8 listed developers' share of **unit sales**, top-7 cities | **6%** (FY17) | **22%** (FY21) | — |
| Listed developers' share of **sales value** | 13.1% (FY20) | — | **20%** (FY25) |
| Listed/Grade-A developers' share of **new launches** | — | — | NCR 66%→70%, Bengaluru 53%→57%, MMR 24%→26% (FY26→FY27 Q1) |
| Top-11 listed developers' combined **pre-sales** | — | — | ₹1.49 lakh cr (FY26) → ₹1.82 lakh cr targeted (FY27), +22.3% YoY |

`[1-SOURCE per row; each row a different Anarock/CREDAI-style report]`. **Read**: organized/listed
developers went from a low-single-digit-to-low-double-digit share of the market (FY17-20) to
roughly a fifth to a quarter of it by FY25/26 across every metric tried — a genuine, multi-year
consolidation — but the exact multiple depends entirely on which metric (units/value/launches) and
which developer cohort (top-8/top-11/"listed and Grade-A") is used, so this leg reports direction
and rough order of magnitude (roughly 3-4x over eight years), not a single precise ratio. As the
plan itself frames it: **this consolidation is RERA-driven** (compliance costs and buyer
preference for RERA-registered, larger sponsors), not default-driven the way China's was — a
structurally different mechanism reaching a broadly similar destination.

## 11. Stalled/delayed projects — India's closest analogue to China's unfinished pre-sold units

Every aggregate figure found this pass is **internally non-reconciling** — presented as a range
with the conflict named, not resolved, per this dossier's own rule:

- **6.29 lakh homes, ₹5.05 lakh crore**, stalled or badly delayed, top-7 cities `[1-SOURCE]` —
  within which NCR alone accounts for 3.28 lakh homes/₹2.50 lakh cr and Mumbai 1.49 lakh homes/
  ₹1.52 lakh cr.
- **1,626 residential projects, ~4.32 lakh homes, 15 major locations, ₹10.79 lakh crore** buyer
  money stuck, at an average ticket size of **₹2.5 crore/unit** `[1-SOURCE, a different report]`.
- **27.6 lakh homebuyer families**, ₹12.44 lakh crore locked, at an average of **₹45 lakh/family**
  `[1-SOURCE, yet another report]` — note the average ticket size here (₹45 lakh) is roughly
  **1/5th to 1/6th** of the previous bullet's ₹2.5 crore figure; these two "stalled project"
  reports are very unlikely to be describing the same population, and neither is preferred here.
- **4.8 lakh units delayed 3+ years** nationally, a separate framing again `[1-SOURCE]`.
- **NCR specifically: 2,10,200 units** stuck in construction since 2013 — the single largest
  regional count found `[1-SOURCE]`.
- **Geographic concentration is the one internally consistent finding**: Maharashtra
  (Mumbai+Pune) = **49.7% of delayed projects by volume, 59.9% by value**, nationally
  `[1-SOURCE]`; the southern metros (Bengaluru, Chennai, Hyderabad combined) = only **~10%** of
  incomplete units `[1-SOURCE]` — both figures come from the same underlying report and are
  mutually consistent, unlike the national totals above.
- **The government's own remediation scale implies a smaller working number than the "crisis"
  headlines**: SWAMIH Fund-1 has completed 50,000 units with another 40,000 targeted in 2025, and
  a further SWAMIH Fund-2 (₹15,000 crore) targets 1 lakh MORE units — i.e., the funded,
  addressable population the government is actually underwriting is on the order of **1-2 lakh
  units**, well below the 4-6 lakh headline aggregates above `[1-SOURCE]`.
- CRISIL's debt-recovery framing (22%→38% projected FY25→FY26) is a **lender-side, stressed-asset**
  metric, not a homebuyer/unit count, and should not be blended with the counts above.

**Bottom line on Q11**: stalled/delayed housing is real, large, and geographically concentrated
(NCR and Maharashtra dominate on every consistent cut), but the sector has **no single agreed
aggregate** — headline national totals disagree by a factor of roughly 2-3x depending on source,
in a way this dossier could not resolve and does not attempt to adjudicate.

---

## Gaps and cautions

1. **Every figure in this dossier is WebSearch-snippet-sourced, not re-fetched from a primary
   page** — the same standard as the rest of this programme's Half B, one rung below this desk's
   own [VERIFY] bar.
2. **The Delhi/Kolkata GPG "highest yield" result should not be read as an investment signal** —
   it most likely reflects sample composition (older/cheaper stock), not an actual arbitrage; no
   source in this pass tested that hypothesis directly.
3. **Total-return-since-listing figures for all four established REITs are the weakest numbers in
   this dossier** — genuinely conflicting across sources, worst for Nexus (three irreconcilable
   figures). Do not quote any single since-listing total-return number from this dossier without
   the caveat attached in §5 and the REIT table.
4. **The net-residential-yield build in §4 is this dossier's own arithmetic on sourced statutory
   mechanics and generic cost assumptions — it is not a published single figure.** Treat it as
   illustrative, not measured.
5. **No India-specific 2015 or 2019 GPG-methodology national yield baseline was retrieved** —
   the multi-year national yield TREND (as opposed to the current level and the 2021-2025
   price-vs-rent read in §2) cannot be built cleanly from this pass.
6. **Unlisted tier-2/3 developer leverage remains, after this dedicated search, an unmeasured
   segment** — not merely unresearched. Every aggregate found (bank credit, system NPA, rated-
   developer debt/CFO) is either economy-wide or specific to the RATED (larger, more
   capital-markets-connected) developer population. A principal-machine pull of RBI's sectoral
   NPA breakdown (if disclosed at that granularity), NHB/NAREDCO developer-finance surveys, or a
   named-issuer bond/CP database would be the concrete next step, not another WebSearch pass.
7. **Stalled-project aggregates disagree by 2-3x across sources with no shared methodology** —
   the NCR/Maharashtra geographic concentration is the one number worth carrying forward as
   reasonably solid; none of the national totals should be quoted as *the* figure.
8. **WALE for Nexus Select Trust was not found this pass** — a specific, named gap in an
   otherwise fairly complete REIT table.
9. **The SM REIT yields (8-9%) are prospectus PROJECTIONS on <2-year-old schemes, not realized
   multi-year track records** — do not compare them to the large REITs' [COMPUTED] trailing
   distribution yields as if they were the same evidence grade.
