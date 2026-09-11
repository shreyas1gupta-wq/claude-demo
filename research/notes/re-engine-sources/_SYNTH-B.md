## COUNTRY PATTERNS: THE DATA REGIMES, AND WHAT HAPPENS WHEN A COUNTRY FORCES DISCLOSURE

**What a country's house-price data looks like is decided by the legal event that generates the
price, not by the country's income level.** Where the state made the transacted price a registrable
legal fact — England & Wales, Ireland, the Netherlands, Korea, Taiwan — free address-level microdata
exists. Where the state only ever needed a number to tax, the public record is an administrative
valuation roll and the market price is unobserved: Thailand, Pakistan, Turkey, India. Income does not
predict the side a country lands on — Japan publishes a voluntary survey while Korea publishes
named-building, named-floor microdata through a free API. **India's problem is not a technology gap:
India built a valuation roll and a registration system and never joined the two into an index.**

**The binding evidence limitation.** The six dossiers behind this section (`B1`-`B6`) were written
with the shared WebSearch budget exhausted (200/200) and `WebFetch` egress-blocked. **Not one
external claim in them was checked against a primary page, and the audit (`_AUDIT-2`) independently
reproduced the same exhaustion and could not check them either.** Every external claim below is
`[RECALL — unverified]`; the only evidence-grade material is `[DESK PRINT]` and `[VAULT-VERIFIED]`.
The audit refuted sixteen claims from the vault, desk documents, run scripts or internal
contradiction, each struck below or carried with its correction visible. **It also found four
dossiers converting `_PROBE.md`'s gateway-level CONNECT refusals into URL "attestation" — a
fabricated hostname returns byte-identical output — so no URL here is described as verified.**

---

### 1. THE HOUSE-PRICE DATA REGIME, COUNTRY BY COUNTRY

**Three jurisdictions reach a free address-level price; roughly six reach a locality; most emerging
markets stop at a city or national index.** All cells `[RECALL — unverified]` unless tagged; per the
audit this is a reading map, not a fact table.

| Country | Producer / product | Method | Finest FREE geography | Licence / access |
|---|---|---|---|---|
| US | **Case-Shiller** (S&P DJI/CoreLogic) | Repeat-sales, 3-stage weighted; 3-month trailing average | 20 metros; no free county/ZIP/tract | Levels free (FRED); microdata proprietary |
| US | **FHFA HPI** — all-transactions / purchase-only / expanded-data | Repeat-sales; all-transactions pools repeat *appraisals* | ~3,000 counties; experimental annual ZIP and **tract** `[start-year uncertain]` | Public domain, bulk CSV |
| US | **Zillow** ZHVI/ZORI; Redfin; Realtor.com | AVM over the housing *stock*; MLS activity rollups | ZIP; neighbourhood in large metros | Free bulk CSV; Zillow restricts commercial reuse |
| US | Census **BPS**, **ACS B25077**, **HMDA** | Permit census; self-reported values; loan-level register | Place/county; **tract** (ACS, self-reported); **tract** (HMDA) | Public domain, bulk + API |
| US | Recorders — Cook, King, NYC **ACRIS**; **Texas** + ~a dozen non-disclosure states | Deed-level stated consideration; **no price on the deed** in non-disclosure states | **Address/parcel**; transfer only in TX | Free portals |
| England & Wales | HMLR **Price Paid Data**, from 1-Jan-1995 | Census of full-market-value registered sales; ~29-30m rows | **Address** (PAON/SAON + postcode) | **OGL v3.0, free bulk CSV, no key** |
| England & Wales | **UK HPI** (HMLR/RoS/LPS/ONS, unified ~2016) | Hedonic, mix-adjusted | Local authority district | Open |
| Scotland / N. Ireland | Registers of Scotland; LPS/NISRA NI HPI | NI runs **quarterly** inside a "monthly" UK HPI | Local authority | Open |
| Ireland | PSRA **RPPR**, from 1-Jan-2010 → CSO **RPPI** | Census of sales filed for **stamp duty** — a tax filing, not a title registration; "Not Full Market Price" flag | **Address** | Free, search + download |
| Netherlands | Kadaster (notarial deed) + **WOZ** universal annual valuation (~8m dwellings) | **SPAR** — sale price over assessed value | Address (WOZ lookup ~2016) | Aggregate open; **per-record deed fee believed** |
| Nordics | DK Tinglysningsretten (~2009)/StatBank; SE Lantmäteriet/SCB; NO SSB + Eiendom Norge; FI Statistics Finland + NLS **HTJ** (~2019) | Registry-sourced DK/SE; **agent-reported NO/FI — SSB believed built on the faster agent feed, not the registry; Finnish apartments are housing-company *shares*, so agent reporting is mandatory** | Address via DK portals; municipality otherwise | Statistics agencies open |
| Japan | MLIT **Real Estate Information Library**; Koji Chika (1970-), Kijun-chi, **Rosenka** (≈80% of Koji Chika) | **A voluntary survey, not a registry extract**; **none of the other three is a transacted price** | City/ward + district; area **banded**; date to **quarter** | Free; **REST/JSON API** |
| Korea | MOLIT **RTMS** (apartments from ~Jan 2006); K-REB survey vs **KB Liiv On** | Census tied to mandatory actual-price reporting; also **jeonse/wolse** leases | **Complex + dong + floor + exclusive area + exact date** | **Free API**; account + dataset application |
| Taiwan | MOI **實價登錄**, 1-Aug-2012; 2.0 ~1-Jul-2021 | Mandatory actual-price registration | Address-range → **address** (2.0) | Free |
| Singapore | **HDB Resale Flat Prices** (to ~1990); URA **REALIS**; URA PPPI | HDB a census of public-housing resales; REALIS **caveat-level**, ahead of completion | **Block + street + storey band** | HDB free bulk + API; **REALIS paid** |
| Hong Kong | RVD indices; Land Registry **Land Search**; Centaline **CCL** weekly | RVD construction **unresolved**; CCL provenance **contradicted** | Region + size class free; address at **fee per record** | Free aggregates; fee-per-deed |
| China | **NBS 70-city** (2011 revision); CREIS; Beike; **Fang-Gu-Xiong-Zhou** microdata | Administrative, **window guidance (窗口指导) recalled 2021-23**; private listing indices; one bank's loan file, 120 cities 2003-2013 | 70 cities / city | Free; mixed (private) |
| Brazil | **FipeZap** (~2011); BCB **IVG-R**; IBGE **SINAPI** | FipeZap **asking**; IVG-R appraisal/collateral; **SINAPI is construction cost, not prices** | City | Free |
| Mexico | **SHF** (~2005); INEGI role `[VERIFY]` | Mortgage **appraisal** values (SHF + Infonavit + Fovissste + banks) | State | Free |
| Turkey | TCMB **Konut Fiyat Endeksi** (~2010=100) | Hedonic on bank **appraisal** valuations; **real series published alongside nominal** | City + Istanbul | Free |
| South Africa | **Lightstone**; Absa HPI; FNB HPI | Full Deeds Office census vs **single-lender book** | Suburb (commercial) | Bank indices free |
| Poland | NBP **BaRN** | **OFFER and TRANSACTION prices for the same cities and quarters** — the only paired design found | ~7 cities + voivodeship capitals | Free, quarterly report |
| Russia | Rosstat avg price/sqm; **SberIndex**/DomClick | Simple regional averages; **secondary-leg provenance is a flagged recall conflict** | Federal subject | Free |
| Thailand | BoT RPPI; GHB **REIC** | **Treasury Department valuation roll** (a registration-fee floor, structurally a circle rate) plus bank collateral `[VERIFY]` | National/Bangkok | Free |
| Indonesia | BI **SHPR/IHPR** | Quarterly **survey of developers' primary-market list prices** | Major metros | Free |
| Philippines | BSP **RREPI** (~2016-) | Newly granted bank loans; **financed transactions only** | NCR vs outside NCR | Free |
| Vietnam / Nigeria | MoC commentary, Savills/CBRE, batdongsan; Nigeria none identified | Asking-price city reports only | City | **Negative findings: no robust free official index** |
| Colombia / Chile / Kenya | DANE and/or Banco de la República; INE **IPV** (~2018-19); **HassConsult** (~2000-, houses **plus a land index**) | **Colombian and Chilean institutional splits `[VERIFY]` above anything else in the pack** | National/city; Nairobi | Free summaries |
| **India** (comparator) | RBI HPI; NHB RESIDEX; state IGR portals | RBI HPI quarterly, ten cities, **from registration authorities**, Q1:2010-11, base 2010-11=100 `[DESK-VERIFIED]`; RESIDEX carries **two different price legs** and **three dated bases** (2007; FY2012-13; FY2017-18) | City index; registration **counts** free monthly, prices not | Free aggregates, no bulk |

**Two cells the audit touched hardest.** **Zillow's ZHVI tier band** — `B1` prints 35th-65th while
citing a file named `tier_0.33_0.67`; ingestion must take the cut from the filename, and neither
number may be published until the methodology page settles it (`R13`). **Centaline's CCL** — two
contradictory provenances, so it is **not classifiable into a construction type** (`R15`).

**The four construction types, and why the taxonomy precedes any pooling.** Two of the four are not
market prices at all. **Asking/listing** (FipeZap, HassConsult, CREIS/Beike; India's portals) is
downward-sticky, so declines are understated. **Appraisal/collateral** (SHF, TCMB, BSP, Absa, FNB,
IVG-R; India's bank sanction data and RESIDEX's assessment leg) is **blind to cash purchases** and
smooths turns. **Registered transaction/deed** (HMLR PPD, RPPR, RTMS, 實價登錄, Lightstone; India's
IGR/NGDRS) carries whatever the recorded consideration understates. **Developer primary survey**
(Indonesia SHPR; India's RERA filings) is self-reported list prices.

---

### 2. THE FOUR TEMPLATES INDIA COULD COPY

**Verdict first: only the SPAR template is buildable by this desk from data that already exists, and
only in a corrected form the source dossier got wrong.** The open register needs a statute;
statutory disclosure a statute plus an enforcement chain; mortgage microdata a lender's loan book.
SPAR needs a join.

| Template | What India has of it | Verdict / cost |
|---|---|---|
| **1. HM Land Registry open register** — publish the registered consideration for every sale, address-level, open licence; a statistics office builds a hedonic index on top | Registration yes; an honest recorded consideration **no** (§3); a publishing mandate **no** | **Not achievable by this desk — a policy ask, not a build.** What *is* free today is the counts layer: Maharashtra's IGR publishes daily/monthly registration counts and stamp-duty revenue, and Knight Frank India republishes Mumbai's within days of month-end `[DESK-VERIFIED, partC-data.md §C.5]` |
| **2. Netherlands/NZ SPAR on assessed values** — index sale price over an existing universal official valuation | A price at every stamp-duty deed, yes; a universal official valuation (the circle rate covers essentially every parcel), yes; **a controllable assessment vintage, no — revisions follow no fixed schedule** | **THE PRIMARY CANDIDATE, conditional on the vintage problem.** Cost: a join plus an assessment-vintage control; no new pull |
| **3. Japan/Korea statutory disclosure** — force the actual price onto a public record by statute, with a filing window and a reason for the filer to be honest (Korea tied registration itself to the reported price) | Nothing | **Not achievable by this desk — the reform template.** Japan's half is a warning, not a model: its flagship is a voluntary survey, so "free transaction-level API" and "transaction census" are different claims |
| **4. Fang-Gu-Xiong-Zhou mortgage microdata** — a constant-quality hedonic index off one lender's origination file, bypassing the official chain | No public analogue; **no Indian register discloses loan-level originations with geocoded property value**, and there is no HMDA | **Achievable only via a lender partnership; Tier-C at best per `CONTRACT.md §4`.** Its lesson cuts both ways: FGXZ found true quality-adjusted appreciation **larger** than officially reported |

**The SPAR correction, because publishing `B2`'s version would have built the wrong estimator.**
`B2` §8 gives the denominator as "that same property's most recent WOZ value"; the audit refuted
that (`R11`) and `D1` §6 has the correct form, `r_i,t = SalePrice_i,t / AssessedValue_i` with the
assessed value **fixed at a base date**. A most-recent-assessment denominator lets each revaluation
enter the ratio, so the index moves when the assessor moves — and **in India circle rates follow no
fixed calendar, so every ready-reckoner revision would print as a price move.** The reference `B2`
left open while `D1` already answered it: **de Vries, de Haan, van der Wal & Mariën, "A House Price
Index Based on the SPAR Method," *Journal of Housing Economics*, ~2009** `[RECALL — unverified]`;
**New Zealand** (Quotable Value council rating "CV") is a second adopter, undercutting the
Dutch-origin framing.

---

### 3. UNDER-REPORTING AND TRANSFER-TAX EVASION

**Not one quantified evasion estimate in this pack survived audit as citable, and the flagship
nine-paper citation set was named the pack's highest-priority verification batch precisely because
recall confidence on canonical papers was high.** `B4` calls this "the most well-trodden literature
of any B-series dossier" — the audit's candidate for the most dangerous sentence in the file, since
high recall confidence is the condition under which a wrong year or journal survives review. **The
direction is load-bearing; every coefficient is a lead.**

**Second finding, and it changes the estimator: the circle-rate floor is not a censoring identity.**
`D2` modelled `observed = max(true_price, circle_rate)` as left-censoring; the audit refuted it
(`R9`) against `A5`'s own `[2-SOURCE]` mechanics — **duty is charged on the higher of declared price
or circle rate, which constrains the tax base, not the declared consideration.** Nothing prevents a
deed recording a price below the floor, so the pile-up is a **behavioural equilibrium** while `D2`'s
likelihood assigns it zero probability. **The share of declarations strictly below the local circle
rate is a day-one diagnostic; if it is non-zero, plain Tobit is misspecified.**

**Taiwan 2012 is the central natural experiment, and its value is a distinction rather than a
number.** Before 2012, tax ran off announced assessed values (公告現值 for land, 房屋評定現值 for
buildings), both recalled as well below market with no ratio trusted. **實價登錄**, effective
**1 Aug 2012** and recalled as an amendment to the 平均地權條例, required the actual price registered
within a window (recalled 30 days), published free at transaction level with the street number
**masked to a range**; **2.0** (~1 Jul 2021) closed the **pre-sale (預售屋)** loophole, required
registration of contract assignments (合約轉讓) and moved to the **actual building number**. The
tax-base fix came separately — **房地合一稅**, an actual-gain capital gains tax, **2016** and
**2021**. **The lesson survives even if every date is wrong: disclosure reform and tax-base reform
are two independent levers, and they need not move measured prices, reported volumes and tax revenue
together.** Taiwan pulled them four years apart; India already separates a stated stamp-duty
valuation from whatever the deed says, so an Indian reform has the same two levers and must have its
price-dispersion and revenue effects modelled separately. **The honest gap: this pack holds no
trustworthy post-2012 or post-2016 Taiwanese volume, dispersion or revenue figure** — `B3` declined
to invent one, which makes it the first search-enabled session's top target.

**Every quantified evasion estimate in the pack.** The content of the table is how little of it is a
number.

| Claim | Source | Tag / audit status |
|---|---|---|
| Best & Kleven (2018) UK SDLT notch semi-elasticity; Besley-Meads-Surico (2014) stamp-duty-holiday pass-through %; Fisman & Wei (2004) evasion per tariff point | `B4` §1-2 | All `[RECALL]`, **no magnitude trustworthy.** What survives is architectural: notch bunching is reporting/price adjustment, not real response, and pass-through to sellers is partial |
| UK pre-Dec-2014 SDLT slab schedule (0/1/3/4/5%) | `B4` §2 | `[RECALL, INCOMPLETE]` — the top gained further bands inside Best-Kleven's own sample window; quote from the paper or drop the numbers |
| Kopczuk & Munroe (2015) NY mansion-tax missing mass at $1m | `B4` §2 | `[RECALL]` on magnitude. **The structural point needs no number: whether notch bunching is real repricing or fraud depends on how verifiable the recorded price is** — loose wherever the recorded price *is* the number under the evasion incentive |
| Montalvo, Piolatto & Raya (~2020): share of Spanish transactions with a material appraisal-vs-declared gap, and mean gap size | `B4` §3 | `[1-SOURCE → RECALL]`; authors and design held above year/venue, **both headline numbers need a primary check.** The design transfers: pair the tax-exposed declared price with an independently-incentivised valuation and read the whole **distribution** of the gap |
| Pakistan DC rates "a third or less of market"; floor percentages for Greece, Italy, Portugal, Turkey, Egypt, Colombia, Mexico; Spain's "Ley 11/2021" number | `B4` §3-4 | All `[RECALL]`, self-flagged. Mechanisms carry moderate confidence, percentages and statute numbers none |
| India: circle-rate gap "up to ~2x in parts of Mumbai, ~30% in Delhi"; LocalCircles "2 in 3 paid part cash, 1 in 4 over half off-books" | `A5` §7 | **Downgraded to `[RECALL]` by `_AUDIT-1` D-21.** Cross-dossier tension not to be hidden: `A2` reports the primary/developer gap **narrowing from >100% in 2015 to as low as ~6%**. Both may hold for different segments; the engine picks wrong unless the segment is stated |
| India: **Section 50C**, Income Tax Act (via Finance Act 2002) — deems the higher of circle rate or declared price as taxable consideration | `A5` §7 | **`[2-SOURCE]` for mechanics and purpose — the one India-side item above recall grade** |
| India: 43CA/50C/56(2)(x) tolerance band 5% (FA2018) → 10% (FA2020) → temporary 20% (Nov-2020-Jun-2021) | `D2` §5, `C4` §A7 | `[RECALL]`, and **explicitly: two dossiers from the same model with search unavailable agreeing is correlated recall, not corroboration.** Conditional on the band existing, the mechanics hold — a *proportional* band predicts a **plateau**, not a spike, so any excluded window must span the whole band |

**The floor systems, and four variants worth keeping apart.** The plain rule — duty on the **higher
of** declared price or an administrative value — is India's, Portugal's (valor patrimonial
tributário), Mexico's (the **greater of** price, cadastral value or appraisal) and Turkey's (tapu
harcı against the municipal **rayiç değer**). **Pakistan** runs a **three-tier stack** (provincial DC
rate < federal FBR tables from ~2016 < market) — two floors moving at different speeds, the closest
analogue to India's sub-district heterogeneity. **Greece**'s αντικειμενικές αξίες drift stale in
**both directions** — below market in prime zones, above it in post-2008 depressed areas — so a
floor's staleness has a sign set by the cycle phase. **Italy** inverts the design: **prezzo-valore**
(2006) lets the buyer elect tax on the *lower* cadastral value **conditional on stating the true
price honestly**, while the **OMI** zone bands are an **audit-risk trigger, not a hard floor**.
**Spain**'s **valor de referencia** (Jan 2022) *introduced* a floor where one barely existed. **Egypt**
shows a different failure mode: the margin was not under-declaring but not registering at all
(informal "orfi" contracts), addressed by small fixed fees ~2006.

**Why a floor is geometrically different from a notch.** A **notch** produces excess mass below and
a hole above — two-sided, with an internal shape the Kleven integration constraint reads an
elasticity off. A **floor** produces a **single mass point**, mixing transactions whose true price is
genuinely below it with those whose true price is far above it but which declare the floor anyway.
**The mass point has no internal shape, so the registered-price distribution alone cannot separate
the two groups** — which is why the discrepancy design, not the bunching design, transfers to India.
The one regularity supported without a coefficient: **under-declaration rises with the size of the
tax wedge**, so India's uneven revision cadence should leave a *time-varying* evasion signature, not
a flat proportional discount.

---

### 4. EMERGING-MARKET MEASUREMENT LESSONS

**The sharpest lesson sits one level upstream of where anyone looks for it: the deflator itself can
be the contested variable, not just the index.** TCMB's Konut Fiyat Endeksi publishes a CPI-deflated
real series alongside the nominal one — necessary because Turkish CPI ran from ~15-20% in 2020 to a
peak recalled around **85% in Oct 2022**, staying 40-70%+ through 2023-24 `[RECALL — unverified,
directional]`, making nominal YoY prints above 100% routine and meaningless undeflated. But Turkey
*also* has a recalled dispute between TÜİK's official CPI and an independent group (recalled as
**ENAG**, `[VERIFY]` on the name) publishing higher estimates. **That is China's NBS problem one
layer removed: not "is the index honest" but "is the deflator honest."**

**The desk's own print complicates the naive reading of a high-inflation nominal series.**
`[DESK PRINT, IN-D2]`: on hyperinflation-clean windows of the JST panel, a 20%/yr nominal five-year
property run has typically meant about **+12%/yr real** (mean real +12.42 vs nominal +23.17%/yr;
inflation supplied **46%** of the headline; only **2.3%** of hot nominal windows were real-negative).
The desk's registered money-illusion prior **missed**. The rule is "deflate anyway, because the
exceptions are currency events": the nominal leg without that exclusion averaged +962.71%/yr.

**The asking-versus-transaction gap has been measured, by design, in exactly one country.** NBP's
**BaRN** collects offer *and* transaction prices for the same Polish cities and quarters; the
recalled gap is offer above transaction by a **single-digit to low-double-digit percent** in ordinary
conditions, narrowing or flipping in tight seller's markets (~2021-22) `[RECALL — unverified,
approximate range only, not a plug-in]`. FipeZap, HassConsult, CREIS/Beike and India's portals all
lack a published companion transaction series, so **no confident percentage-point gap exists
anywhere else.** **Hence a prohibition: do not import a foreign asking-vs-transaction haircut into
India** — BaRN's paired-collection design is the template, so measure the gap rather than borrow
it.

**Official smoothing, and what the desk's own China programme adds.** `B5` gives the mechanism
(local statistical bureaus answering to local governments with a fiscal stake in land revenue;
recalled 2021-23 window guidance) and the corrective (Fang, Gu, Xiong & Zhou's one-bank loan file).
The CN programme sharpens it three ways: **the consensus path lands on the base rate** (official
-24.6% plus Goldman's further ~10% compounds to **-32.1%** against the desk's modern-era median
**-32.00%**, `[DESK PRINT, CN-D1]`); **no adjustment multiplier for official Chinese data exists**
(`c-datatrust`: practice is **substitution, not haircutting**), and the **official-vs-private ~2x
measurement gap is the binding uncertainty** of the whole China analysis; and an unadjusted average
is demonstrably unsafe, since Chinese land *price* fell only **-23%** while land *volume* fell
**-66%** and revenue **-52.3%** — a **composition artifact** as distressed lower-tier parcels
stopped transacting. Indian ward markets are thin enough for the same shift.

**Two biases that must never be netted.** Appraisal and bank-book indices all **miss cash
transactions**, large at the high end and in less-banked areas; in India that compounds with a
*separate* bias — stamp-duty-minimising understatement toward the circle rate — pointing a different
way for a different population. South Africa gives the staging path: bank-book proxy first,
full-registry census second (Lightstone), and the gap between them read as the diagnostic.

---

### 5. THE LONG-RUN BASE RATES, AND WHERE INDIA AND CHINA SIT

**The base rates here are `[DESK PRINT]`, not literature. `B6` recommended sizing the India stress
scenario at -20% to -30% real over 4-5 years from unverified recall of two external papers, when
this desk's own pre-registered print from the same JST panel is -34.22% over 6.5 years. The audit
refuted it (`R6`): a `[RECALL]` figure was allowed to override a `[DESK PRINT]`, in the milder
direction, inside a recommendation block.** Even the mildest quartile of the desk's distribution
(-27.52%) sits at the bottom edge of `B6`'s band.

| Long-run real appreciation | Span | Figure | Tag |
|---|---|---|---|
| Knoll, Schularick & Steger, "No Price Like Home," *AER* 107(2), 2017 | 1870-2012, 14 advanced economies | **~1%/yr** full sample; **~1.5-2%/yr** post-1950 | `[RECALL]`, but **consistent with the desk's `[Verified]` statement**: a real tripling since 1950 implies 1.79%/yr over 62 years, 0.77%/yr over 143 |
| Eichholtz, Herengracht Index, *Real Estate Economics*, 1997 | Amsterdam 1628-1973 | **close to zero**, with huge multi-decade swings around a flat trend | `[RECALL]` |
| Ambrose, Eichholtz & Lindenthal, "House Prices and Fundamentals: 355 Years of Evidence," ***JMCB* 45(2-3):477-491** | Amsterdam 1650-2005 | Price-rent correction runs through **prices** and takes **decades** | **`[2-SOURCE]`** — the one citation the pack could firm up; the title is **355**, not 350 |
| Shiller US real house prices | 1890- | **flat/cyclical to the mid-1990s**, then the 1996-2006 runup | `[RECALL]` |

Three independent series converge: **absent an identifiable structural break, long-run real house
prices are not a reliably compounding asset.** "Housing does 5-7%/yr real" is a recency artifact of
the post-1950 (or post-1996 US) window.

**Two corrections to the source account of KSS, both binding (`R3`).** The land mechanism is
**transport costs**, not scarcity: falling transport costs expanded the effective supply of
commutable land until mid-century, when that stopped and land-use regulation tightened. And the
figure of record is that **land price increases explain roughly 80% of the aggregate global
house-price rise since WWII** (desk-`[Verified]`) — **not** the "six-fold real rise in land since
1950" or the "third toward half" land-share path `B6` printed, neither of which appears on desk.
`B6`'s recalled 14-country sample list is struck entirely: the cross-check built to validate it
discards Finland (from 1905) and Switzerland (1901) as "too late" for an 1870-2012 panel while
keeping Italy (**1970**) and Spain (**1971**) `[VAULT-VERIFIED]`.

**The drawdown distribution — `[DESK PRINT, CN-D1]`.** 48 completed episodes, 18 countries,
1870-2020; the definition was frozen before the run as a real peak followed by a **≥20%** decline
to trough, peaks ≥10 years apart, trough on or before 2020.

| Statistic | Full sample (n=48) | Modern, peaks from 1970 (n=24, 16 countries) |
|---|---|---|
| Median peak-to-trough **real** decline | **-34.22%** (p25 -49.96, p75 -27.52) | **-32.00%** (p25 -39.43, p75 -29.19) |
| Median duration | **6.5 years** (p25 4.75, p75 12.25) | **5.5 years** |
| Median decline velocity | **-6.95%/yr** | **-7.41%/yr** |
| Median pre-crash 5y appreciation | **+5.60%/yr** | **+6.21%/yr** |
| Velocity ratio (bust ÷ boom speed) | **1.12x** — the registered "busts are slower" bar **MISSED** | **0.99x**, parity |
| Rental yield, peak → trough | 3.78% → 5.23% (**+1.41pp**), compressing **-0.83pp** into the peak over the final five years | 3.29% → 4.94% (**+1.53pp**) |

**There is no gentle-deflation discount in the base rate.** Three archetypes bracket any forecast:
**Japan 1991** (-47.3% over 18 years at -3.50%/yr, ratio 0.57 — the slow grind), **Ireland 2006**
(-55.7% over 6 years at -12.70%/yr, ratio 1.55 — the worst modern bust) and **Finland 1989**
(-14.87%/yr, the fastest in the panel): same destination, three times the speed. And
`[DESK PRINT, CN-D4]`, **a bigger boom buys SPEED, not depth** — depth gap 3.8pp, unwind 3.5pp/yr
faster — so the exit plan matters more than the entry level.

| Frequency of 20%+ real declines | Value | Basis |
|---|---|---|
| P(a ≥20% real crash peak begins within 5 years of any 5-year window) | **13.0%** | `[DESK PRINT, IN-D1]`, 1,934 overlapping windows, 18 countries |
| Episode census | **48 / 18 countries / 1870-2020** | `[DESK PRINT, CN-D1]` |
| Implied rate | **one episode per ~43.7 country-years ≈ 0.23 per country-decade** | Derived arithmetic on two desk prints (2,097 panel country-years from the `[VAULT-VERIFIED]` `hpnom` start years). **Not itself a registered print**; it independently agrees with IN-D1's 13.0% per 5y window (≈0.26/decade) |
| Crash-odds lift after a hot window | **~2x** (2.02x at ≥10%/yr real, 2.03x at ≥20%; the ≥15 rung printed 1.03x and is recorded as a **MISS**, not smoothed) | `[DESK PRINT, IN-D1]` |
| Best-known credit early warning | Mortgage-credit growth lifts 3y crash odds **1.72x** with an **87.2% false-alarm rate**; public-debt growth reads **backwards** (0.23x — it rises *after* busts) | `[DESK PRINT, CN-D3]` |

**`B6`'s "roughly one country-decade in six to ten sees a 20%+ real decline" does not appear above
and must not enter any published table in any form, tagged or not.** It was self-labelled a
synthesis, not a reported statistic; the audit ruled it inadmissible; and the desk's own
recomputation from the same vaulted panel is roughly twice as frequent.

**Where India and China sit.** India is **absent from every long panel** — JST R6 is 18 advanced
economies, 1870-2020, with **no India and no China** `[VAULT-VERIFIED]`, as are KSS, JKKST,
Herengracht and Shiller by construction. India's horizon is post-2010 and administrative, and the
**current RBI HPI vintage is an 18-city base-2022-23 series whose history starts in 2022-23**, not a
backward extension of the ten-city base-2010-11 series `[DESK-VERIFIED, partC-data.md]`. **The
documented rule is to treat the two bases as distinct vintages and never fit a Hamilton gap or a
percentile rank through the break**, refuting `B6`'s recommendation to build a live India valuation
percentile off a BIS mirror (`R16`); India has **no valuation percentile anywhere in the vault**.
India's own base-rate reads `[DESK PRINT, IN-D1]`: a sustained 20%/yr real boom has **never happened**
in the modern era of the panel (**0.00% of 884** post-1970 five-year windows; the post-1970 maximum
is **Ireland 1999 at +17.25%/yr real**, and Ireland 2006 is the worst modern bust at -55.7% — same
country, seven years apart), yet **hot markets stay hot at five years**, at **+9.65%/yr** real after
a ≥15%/yr window and **+11.16%/yr** after ≥20%, with roughly 2x crash odds: **ride-it-but-size-it,
never in-or-out**. What binds is the cost wedge — **~21.5% over five years**, so a locality doing 20%
cumulative nets **-0.30%/yr nominal, -4.60%/yr real** `[DESK PRINT]`. **Both folk clocks fail their
own pre-registered tests**: 109 real peak spacings across 17 JST countries give median **14y**, IQR
10-17y, only **45%** inside the pre-declared [14,22]y window against a ≥50% bar, and Kuznets swings
fail cleanly (median 11y, **25%** in-window) `[DESK PRINT, RE1/RE2]` — so **`B6`'s endorsement of the "classic ~15-20yr
Kuznets/long-swing housing cycle" is struck (`R7`)**. For China, tier-3 has taken a
**full** base-rate crash while tier-1 has taken about a third of one, and tier-1's 2021 peak rental
yield of ~1.7-1.8% was the **second-lowest peak yield in 150 years**, behind only Spain 2007 at
1.49%, which then fell 42.9%; **for any single Chinese city the national base rate is the optimistic
frame** (Wenzhou -63.1%, Hainan ≈-87%). One last `B6` claim not repeated here: `housing_tr` and
`housing_rent_yd` are **not "vaulted and unused" — both are already consumed**, by CN-D2 and the CI
battery respectively (`R5`).

---

### WHAT THIS SECTION CHANGES ABOUT THE PLAN

1. **Build SPAR with a base-date-fixed denominator plus an explicit assessment-vintage control** —
   `B2`'s wording would make every ready-reckoner revision print as a price move (§2, `R11`).
2. **Make the share of declarations strictly BELOW the local circle rate a day-one diagnostic,
   before an estimator is chosen** — if it is non-zero, plain Tobit is misspecified (§3, `R9`).
3. **Size the India stress scenario off CN-D1 (-34.22% real / 6.5y; -32.00% / 5.5y modern; p25
   -49.96%) and delete the -20% to -30% band** (§5, `R6`); per CN-D4 the exit rule is the design
   object, not the entry level.
4. **Classify every Indian source into the four-way construction taxonomy before pooling any two,
   and never net the appraisal cash blind spot against registration under-declaration** (§1, §4).
5. **Measure the Indian asking-vs-transaction gap directly, BaRN-style, and hard-block any imported
   haircut** — only Poland measures it by design, and approximately (§4).
6. **Build the IGR counts-and-revenue layer first and the price layer second** — counts are free,
   monthly and already cleaned, while registered *prices* are the contaminated series (§2).
7. **Deflate every long Indian nominal series, and test the deflator separately** — the TÜİK/ENAG
   precedent makes it a candidate contested variable (§4).
8. **Do not build an India valuation percentile off RBI HPI or a BIS mirror of it** — a percentile
   rank through the 2022-23 rebase is forbidden on desk; treat the gap as named (§5, `R16`).
9. **Register the tax-parameter history as breaks-registry entries ahead of their consumers** —
   BR1-BR9 hold no circle-rate, 43CA, 50C or stamp-duty entry, and a proportional band predicts a
   plateau, so any excluded window must span it whole (§3).
10. **Queue the Taiwan post-2012/post-2016 volume, dispersion and revenue figures, and `B4`'s
    nine-paper citation batch, first in the next search-enabled session** — both currently empty
    rather than wrong (§3).
