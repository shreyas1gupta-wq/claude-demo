# Part C — Data engineering: measuring India's commodity exposure and terms-of-trade state, free

Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)
v1.0 · 2026-09-01

Extends `docs/CYCLE_ATLAS.md` row 1.3 (commodity supercycle → **H53**: context + sector-tilt
conditioner + L9 enrichment, Tier C until researched) and row 2.11/2.12 (H54 China credit impulse,
oil inside L9 via Kilian decomposition — Brent + Kilian activity index + PPAC import bill). Consumes
`research/CONTRACT.md` §3 (free-source mandate), §4 (evidence tiers, Tier-C reduce-only), §6 (no
magic numbers), §8 (Hamilton filter only, never HP), Known Prior #11 (no live network access from
this container; ingestion runs on the principal's machine, every indicator resolves against a
committed fixture). Feeds `config/ladder.yaml` **L9_global_financial_cycle**'s `indicator` field
(which already carries "Kilian index" as an enrichment precedent — H53 is a candidate for the same
slot, not a new ladder entry; per Atlas §8 governance, "none touches the ladder or the registry
until [researched]"). Structure follows `research/cycles/fincycle-deep/partC-data.md` (the style
bar this Part matches). **This Part builds on, and does not re-pull or restate, the already-vaulted
world-price side**: `ingest/vault/commodities/` holds Jacks real commodity prices 1850–2015 (40
series, annual, World, 1900=100), Clio-Infra/USGS metal production 1850–2015, IMF PCPS monthly
1980–2017 (63 series, GitHub `datasets/commodity-prices` mirror), and EIA Brent/WTI monthly
1987–2026.07 — all sha256-manifested and authenticated (`ingest/vault/commodities/
AUTHENTICATION.md`, five cross-lineage bars, all passed 2026-09-01). This chapter's job is the
**India side and the joins**: the import-basket weight vector, the basket-weighted ToT state built
entirely from what is already vaulted, the passthrough validation, the macro/equity harvest legs,
and the pipeline that wires them together. Checked by web search this pass (snippet-level,
cross-checked across ≥2 results where feasible; nothing fetched directly, per Known Prior #11).
Anything not so corroborated carries **[VERIFY]**.

---

## C.1 India's commodity import exposure — the weights

**The goal, restated precisely.** H53's design intent (Atlas 1.3) is that a commodity supercycle
hurts India's terms of trade because it is a net *importer* of most of what a supercycle inflates.
The regime-relevant object is therefore not "the world commodity price index" but **that index
filtered through India's own import mix** — a weight vector `w = {crude, gold, coal, edible_oils,
fertilizer, gas, metals}` that must be (a) free, (b) updateable annually without a live subscription,
and (c) built from a *published* breakdown, not hand-guessed shares.

**Primary source — DGCI&S Tradestat.** The Directorate General of Commercial Intelligence and
Statistics (DGCI&S, Kolkata), an attached office of the Ministry of Commerce & Industry, compiles
India's official merchandise trade statistics from customs bills-of-entry (imports) and shipping
bills (exports) and publishes them through the **Tradestat / Export-Import Data Bank** portal at
`tradestat.commerce.gov.in`. Three query modules matter here: **"Chapter-wise all commodities
Import"** (`.../eidb/chapter_wise_all_commodities_import`) — the fastest route to a weight vector,
since ITC-HS chapters map almost one-to-one onto the basket lines (Ch.27 mineral fuels: crude,
petroleum products, coal, LNG; Ch.71 pearls/precious stones/gold; Ch.31 fertilizers; Ch.15 animal/
vegetable fats and oils; Ch.26 ores/concentrates and Ch.72–83 base metals); **"Commodity-wise all
countries Import"** (`.../eidb/commodity_wise_all_countries_import`) for finer ITC-HS 4/6/8-digit
cuts inside a chapter (e.g., splitting Ch.71 into gold vs. diamonds/pearls, or Ch.27 into crude vs.
coal vs. LNG); and DGCI&S Kolkata's own periodic **"A Quick View of India's Trade Scenario"** snapshot
PDF (`dgciskol.gov.in`), which already publishes chapter-level import *shares* directly — the
cheapest free path to a weight vector when it is current. **[VERIFY]** the portal's confirmed
bulk-queryable history window: search-result metadata for the EIDB/MEIDB modules describes data
"from January 2018 onward" for several query types; DGCI&S's own underlying annual "Foreign Trade
Statistics" publication almost certainly extends decades further, but only as scanned/PDF volumes,
not a structured online query — budget the pre-2018 window as a PDF-transcription task if the
weight vector's own history (not just its current value) is ever needed, e.g., for a pre-2018
robustness check on H53's basket definition.

**Refining the crude/gas/coal split — PPAC and the Coal Controller.** DGCI&S's Ch.27 bundles crude
oil, refined products, coal, and gas into one chapter — too coarse for a basket that wants crude,
coal, and gas as separate lines (Atlas 2.12 treats oil separately via Kilian decomposition; coal and
gas move on different world-price and India-policy cycles). Two supplementary free sources split it:
**PPAC** (Petroleum Planning & Analysis Cell, Ministry of Petroleum & Natural Gas, `ppac.gov.in`)
publishes the daily **"Indian crude basket"** price (a weighted average of Dubai/Oman sour crude and
Brent sweet crude, in the proportions India's refineries actually process — not a generic world
benchmark) and a monthly **"Snapshot of India's Oil & Gas Data"** carrying crude + product import
volume (MMT), import value (₹ crore / US$ million), and **crude import dependency** — a record
**88.7% in FY2025–26** (up from 85.5% in FY2021–22 as domestic output continues to decline)
[VERIFY: figure sourced via press coverage of Petroleum Ministry parliamentary answers/PPAC data
this pass, not fetched from ppac.gov.in directly], plus a comparable **~50% natural-gas import
dependency** (LNG now ~50% of total gas availability, up from ~41% a decade ago) [VERIFY, same
caveat]. Publication lag for the monthly Snapshot: **[VERIFY exact SLA]**; the daily crude-basket
price itself is same-day. **Ministry of Coal / Coal Controller's Organisation** (`coalcontroller.gov.in`)
publishes monthly **"Provisional Coal Statistics"** with grade-wise (coking / non-coking / thermal)
import figures, the free source for isolating coal out of DGCI&S's bundled Ch.27 total —
**[VERIFY]** exact cadence/lag, not independently pinned this pass.

**Gold — two lineages that will not agree, by design.** DGCI&S's Ch.71 customs-value import line and
**RBI's Balance-of-Payments "Gold" memo item** (published inside the quarterly BoP press-release
tables, §C.4) measure overlapping but not identical things: customs statistical value vs.
BoP-adjusted valuation, with known divergences around bonded-warehouse/SEZ re-export treatment and
bullion-bank consignment flows. **Recommendation, stated not hedged**: use DGCI&S Ch.71 (finer —
separates gold from diamonds/pearls) for the *weight-vector* share, and RBI's BoP gold line
(already isolated, already valuation-consistent with the CAD channel) for the *macro-validation*
input in §C.4 — never blend the two into one series; a persistent gap between them is a data-quality
fact to log, not an inconsistency to average away (the same discipline fincycle-deep §C.2 applies to
RESIDEX's assessment-vs-market price legs).

**Fertilizer.** DGCI&S Ch.31 (fertilizers) gives the import-value weight directly; the Department of
Fertilizers (`fert.nic.in`) publishes urea/DAP/MOP volume-specific import statistics under its P&K
subsidy-scheme reporting — **[VERIFY]** exact portal path and cadence, not confirmed this pass; this
is the basket's smallest weight and lowest engineering priority.

**Construction rule.** `w_i(FY) = DGCI&S_chapter_import_value_i(FY) / DGCI&S_total_merchandise_
import_value(FY)`, recomputed **once a year** (India's fiscal year, April–March) from the same
Chapter-wise release, finalized a few months after fiscal year-end — annual refresh is
appropriate because weights are structurally slow-moving (Atlas: this is a weight vector, an input
to a state, not itself a state variable). Illustrative order-of-magnitude shares, **[VERIFY all,
FY2024–25/25–26 vintage, materially oil-price-sensitive year to year]**:

| Basket line | Illustrative weight (share of total merchandise imports) | Primary free source |
|---|---|---|
| Crude oil + refined products | ~25–28% | PPAC (volume/value), DGCI&S Ch.27 |
| Gold | ~6–8% | DGCI&S Ch.71 (weight); RBI BoP (macro validation) |
| Coal (all grades) | ~3–4% | Coal Controller, DGCI&S Ch.27 sub-cut |
| Natural gas / LNG | ~2–3% | PPAC, DGCI&S Ch.27 sub-cut |
| Edible oils (palm/soy/sunflower) | ~2–3% | DGCI&S Ch.15 |
| Fertilizer & inputs | ~1.5–2% | DGCI&S Ch.31, fert.nic.in |
| Base/non-ferrous metals & ores | ~4–6% | DGCI&S Ch.26, 72–83 |
| **Commodity basket total** | **~45–55%** of total merchandise imports | — |

Mineral fuels alone (HS Ch.27, the bundled crude+products+coal+gas cut) ran **~27–34%** of total
imports across recent years per press coverage of Commerce Ministry trade data [VERIFY], and pearls/
precious-stones/jewelry (Ch.71, gold-dominated) around **~14%** [VERIFY] — both consistent in order
of magnitude with the split above. The remainder of India's import bill (electronics, machinery,
chemicals, plastics) is non-commodity and outside this basket by construction.

---

## C.2 The India-weighted commodity ToT state — construction from what's already vaulted

**The design's one load-bearing claim**: India's commodity terms-of-trade state can be built
**entirely from the already-vaulted world-price data**, weighted by §C.1's basket — no blocked
source (World Bank, FRED, BIS) needed for the state itself, only for cross-checks.

**Series mapping — basket line → vaulted proxy.**

| Basket line | Long leg (Jacks, annual, 1850–2015, World, 1900=100) | Modern leg (IMF PCPS, monthly, 1980–2017) | Post-2017 splice |
|---|---|---|---|
| Crude oil | `Petroleum` | `Crude Oil petroleum` / `Crude Oil - petroleum - Dated Brent light blend` | EIA `brent_monthly_eia.csv` (1987–2026.07, already vaulted) |
| Coal | `Coal` | `Coal` | **gap — no vaulted post-2017 monthly source** |
| Gold | `Gold` | **absent from the IMF PCPS panel** (confirmed: not among its 62 columns) | **gap — no vaulted post-2015 leg at all**, long or modern |
| Base/non-ferrous metals | `Aluminum, Copper, Lead, Nickel, Tin, Zinc, Chromium, Manganese` | `Aluminum, Copper, Lead, Nickel, Tin, Zinc` + `Metals Price Index` | **gap** — same as coal |
| Iron ore | `Iron ore` | `China import Iron Ore Fines 62% FE spot` | **gap** |
| Edible oils | `Palm oil` (+ `Peanuts`, `Cottonseed` — narrower than modern India's actual mix) | `Palm oil, Soybean Oil, Soybean Meal, Sunflower oil, Rapeseed oil` | **gap** |
| Fertilizer inputs | `Phosphate, Potash, Sulfur` | **absent from IMF PCPS** (no Urea/DAP/Potash column) | **gap, long AND modern** |
| Natural gas | `Natural gas` | three regional gas columns (Russia→Germany, Indonesia→Japan, Henry Hub) — none is an India-relevant Asia-LNG spot proxy | **gap** |

Two genuine, honestly-flagged construction gaps fall out of this table immediately, carried
forward to §C.9/§C.10 rather than papered over: **(1) gold has no modern (post-2015) monthly leg
vaulted at all** — a real problem given gold is the basket's second-largest line; **(2) every
non-crude line has no vaulted source past IMF PCPS's 2017-06 end-date** — only crude (via the
separately-vaulted EIA Brent/WTI) currently splices cleanly into 2026. The oil leg is the one line
this Part can build end-to-end today; everything else runs on the long Jacks history only until a
new pull lands.

**Composite construction, not raw index reuse.** The state is **not** Jacks' own "World" index
used as-is — that mixes in lines (beef, hides, wool, tea, tobacco, rubber) irrelevant to India's
import basket and would dilute the ToT signal with noise India doesn't actually face. Instead:
build a **basket-weighted sub-composite** using only the Jacks/IMF-PCPS columns matching §C.1's
lines, weighted by §C.1's shares (re-normalized across whichever lines are covered in a given era
— e.g., pre-1980 excludes nothing since Jacks covers every long-leg line except fertilizer's modern
granularity; post-2017 effectively degrades toward crude-only until the gaps close).

**USD-real vs. INR-terms — recommendation and justification.** Build the **primary state in
USD real terms**, not INR. Three reasons: (i) every basket commodity is priced globally in USD
(crude, gold, base metals all quote on USD-denominated world markets) — a USD-real index isolates
the pure commodity-price cycle without conflating it with INR's own secular depreciation trend,
which is a *separate* mechanism the design already reads elsewhere (Atlas 0.4 golden constant, L9's
own dollar-cycle sub-face, L15's real-rate persistence) — mixing the two into one score would
double-count the currency channel across ladder seats, the same "one mechanism, one budget seat"
discipline fincycle-deep §C.3 applies to the HFC/NBFC overlap; (ii) it matches how the vaulted long
history is *already* built — Jacks' index is itself real (1900=100), not INR-denominated; (iii) the
academic commodity-supercycle literature (Jacks himself; Erten-Ocampo) works in real-USD-index
terms, so India's state stays comparable to the global one it is a conditioner on. **Deflation
choice**: deflate the nominal-USD modern legs (IMF PCPS, EIA Brent/WTI) by US CPI-U to match Jacks'
own convention, then **ratio-splice at the overlap** (`k = new(t0)/old(t0)`, the identical
pre-registered rule debt-deep and fincycle-deep use for base transitions) — a ratio splice absorbs a
level-scaling mismatch between deflator vintages provided the deflator's *growth rate* near the
splice date is consistent, so the exact deflator Jacks used need not be resolved first. **[VERIFY
Jacks' own deflator]** — `AUTHENTICATION.md` already flags this open ("US-CPI-deflated per source
docs — [VERIFY] against the Cliometrica paper"); this Part inherits that flag rather than resolving
it. **INR-terms variant** (secondary, derived downstream, never the primary ranking input): the
USD-real state × the USD/INR path (FBIL/RBI reference-rate archive, §C.4) ÷ Indian CPI-Combined
(already spliced across its own base transitions per debt-deep §C.9, not re-derived here) — this
variant is what speaks most directly to actual rupee cost pressure and is the natural input to the
§C.3 passthrough regression, but it must never be substituted for the primary percentile ranking
itself, or the currency channel does double duty inside one score.

**The expanding-Hamilton + expanding-percentile machinery — pointer, no new code.** Both legs reuse
the exact shared functions every other ladder seat already calls: `quant/stats/hamilton.py`'s
`hamilton_filter(y, h, p, mode="expanding", min_obs=5*(p+1))` and `quant/ladder/credit_cycle.py`'s
`expanding_percentile(x, min_obs=24)` (re-exported via `quant/ladder/__init__.py`) — no bespoke
filter for H53. **Parameter choice — reused, not invented**: the commodity supercycle sits in Atlas
Band 1 (15–60y) alongside the real-estate/financial cycle (L12, `tau_half_months: [60, 96]`),
whose price leg fincycle-deep already fixed at h=5y, p=1 for a Band-1 monthly series — H53 reuses
that identical (h, p) rather than fitting a new one: **h=60 months, p=1** for the monthly modern
leg; **h=5 (years), p=1** for the annual long leg — the same convention scaled to annual cadence,
no magic number invented for this chapter.

**Warm-up arithmetic.** *Annual leg (Jacks, from 1850)*: `hamilton_filter`'s own default
`min_obs=5·(p+1)=10` years is trivial this early given 166 years of history; the binding constraint
is the **percentile's** own floor. A 15–20y cycle needs roughly two cycle-lengths of history before
a rank is not dominated by one partial cycle — mirroring fincycle-deep's "48-month floor ≈ the
Contract's ≥4-observations Tier-B floor, scaled to cadence" logic, this Part sets the annual-leg
floor at **`min_obs=40` years**. First trustworthy annual percentile: **≈1850 + 10 (Hamilton) + 40
(percentile floor) ≈ 1900** — coincidentally (not by construction) exactly Jacks' own 1900=100
anchor year, and a genuinely useful result: it means the state's *own* operating window (1900–2015)
covers **all four** of the historical supercycles Atlas 1.3 names (1900s, 1930s–50s, 1970s, 2000s),
satisfying the clock test on the state's own evidence, not by assumption. *Monthly modern leg (IMF
PCPS crude, from 1980-02)*: Hamilton's first output lands at `p-1+h = 60` months in (≈1985-02);
adding the same **48-month percentile floor** fincycle-deep already established for a comparable
Band-1 monthly leg (again reused, not invented) gives a **first trustworthy monthly percentile
≈1989** for the crude leg — the only line with a full modern splice today. Every other basket line's
monthly percentile is either absent (gold, fertilizer) or stops at 2017-06 pending a new pull
(§C.9/§C.10), so **the combined modern-era state is presently crude-dominated by data availability,
not by design intent** — a fact to disclose inline, not to quietly let the state imply.

---

## C.3 WPI/CPI passthrough measurement

**WPI.** Compiled by the Office of the Economic Adviser (OEA), DPIIT, Ministry of Commerce &
Industry — **not** MoSPI (A-catalog H2's own correction, inherited here) — at `eaindustry.nic.in`,
current base **2011-12=100**, three major groups: Primary Articles, **Fuel & Power** (weight **~13.15–13.2%**,
down from 14.9% under the prior 2004-05 base [VERIFY exact current figure]), and Manufactured
Products (~64.2%), inside which **Basic Metals** is a named sub-group **[VERIFY exact weight — not
independently pinned this pass, order-of-magnitude ~9–10%]**. Provisional release on the **14th of
each month** (next working day if a holiday), ~2-week lag, later revised (standard two-vintage
practice). **The 2011-12→2022-23 rebase** (effective from the **2026-06** release, back-data from
April 2023) is already the live in-flight break A-catalog H2 documents — inherited, not
re-derived, but directly load-bearing here: any Fuel & Power / Basic Metals series spanning
2026-06 needs the identical splice discipline as §C.2. **Longer-term structural note**: WPI is
scheduled for discontinuation after ~5 years of parallel publication alongside a new Producer Price
Index — a sunset to track, not just a rebase.

**CPI.** MoSPI, current base **2012=100**, transitioning to base **2024 / COICOP-2018** from the
**2026-02-12** release (A-catalog H1, inherited) — the relevant sub-index here is CPI-Combined's
**"Fuel and Light"** group (**[VERIFY exact 2012-base weight, order-of-magnitude ~6–7%]**), the
direct energy-CPI cross-check.

**Passthrough regression design — explicitly a VALIDATION, not a new seat.** Regress WPI Fuel &
Power (and, separately, Basic Metals) on §C.2's world/India ToT state at lags {0, 1, 2, 3, 6}
months, purged/embargoed per Contract §9, judged out-of-sample against the historical-mean
benchmark — the question this answers is narrow and disciplined: *does the state's rank show up
where it should, in India's own price data, before H53 earns any tier promotion or L9-enrichment
status?* This is **not** an independent ladder input and draws no regime-score budget of its own —
it validates §C.2's construction the way fincycle-deep §C.8 uses the L10 credit/GDP gap as a
cross-check on L12's housing-credit leg, never as a substitute computation. One design complication
to log rather than paper over: WPI's mineral-oil sub-items sit partly on **administered prices**
(retail petrol/diesel/LPG pricing has a government-directed component, discussed further in §C.5's
OMC wedge) — where feasible, prefer WPI sub-items closer to refinery-gate/wholesale pricing over
retail-adjacent ones for a cleaner passthrough read; where not separable, the administered-price
wedge is an expected, structural dampener on the estimated passthrough coefficient, not a modeling
failure to chase away.

---

## C.4 The macro channel data — CAD, INR, reserves

**RBI Balance of Payments.** Quarterly, released via RBI Press Releases ("Developments in India's
Balance of Payments during Q_ FY__–__") and DBIE, at a **~10–13-week lag** past quarter-end
[VERIFY exact SLA; consistent with the general RBI-quarterly cadence already established for HPI in
fincycle-deep §C.1, and with the Q2 FY2025-26 CAD figure — a **narrowing to USD 12.3bn / 1.3% of
GDP** — appearing in RBI's December-2025 release, ~3 months after the September quarter-end].
**The genuinely useful free fact**: RBI's own BoP press-release tables already break out **oil
imports, gold imports, and non-oil-non-gold imports** as distinct memo lines inside the merchandise
trade balance — this is the CAD-channel input §C.1 asked for, already decomposed by the source, not
something this chapter needs to construct. **Revision behavior**: BoP data is provisional at first
release and revised as customs/banking-channel data completes; **[VERIFY exact revision cadence and
typical magnitude]** — not independently confirmed this pass; treat every vintage as provisional
until a later release confirms it, the identical discipline A-catalog H4 applies to GDP/NAS.

**RBI reference rate / FBIL — a genuine source-transition break.** RBI computed and published its
own daily USD/INR reference rate through **2018-07-09**; from **2018-07-10**, **FBIL** (Financial
Benchmarks India Pvt Ltd, `fbil.org.in`) took over computation and dissemination under an RBI
February-2018 policy announcement — confirmed via RBI's own press-release archive. RBI's historical
archive (`rbi.org.in/scripts/referenceratearchive.aspx`) still hosts the pre-transition series;
FBIL's site carries the post-transition one — **two sources, not one continuous download**, a fact
A-catalog G10's own "reference rate archive" framing predates and this Part adds.

**REER.** RBI's 36-currency (through ~2020) → 40-currency (from ~2020) trade-weighted REER,
monthly, RBI Bulletin / DBIE — already A-catalog G7 ("keep both basket vintages distinct... no
synthetic splice exists or should be built"), inherited verbatim.

**Forex reserves.** RBI's Weekly Statistical Supplement (WSS), every Friday, essentially T+0/T+1 —
already A-catalog G6, inherited — the CAD-financing counterpart that closes the mechanism chain this
whole macro-channel section documents: a commodity-driven CAD widening shows up, with a lag, as
either reserve drawdown or INR pressure (or both), observable in WSS and REER respectively.

---

## C.5 The equity harvest side — sector indices

**Confirmed methodology (web-verified this pass).** **Nifty Metal**: ≤15 stocks, free-float
market-cap weighted, single-stock cap 33%, top-3 cumulative cap 62%, semi-annual rebalance. **Nifty
Energy**: 40 constituents, single-stock cap 10%, industry cap 25%, semi-annual rebalance. **Nifty
Commodities**: 30 constituents, per-name cap 10%, semi-annual rebalance with January-31/July-31
cutoff dates. **Nifty Oil & Gas**: methodology document confirms the same general free-float family
construction; **[VERIFY exact constituent count and caps — not independently pinned this pass]**.
All four: `niftyindices.com`, free daily.

**What extends the desk's existing pullers — read, not guessed.** `ingest/pull_nse_bhavcopy.py`
already handles the full cash/derivatives price history including the 2024-07-08 UDiFF boundary —
nothing sector-specific needed there. `ingest/pull_indices.py`, read directly for this Part, today
does **exactly two things**: (1) pulls **current-only** constituent CSVs for four indices —
`nifty50`, `nifty500`, `niftytotalmarket`, `niftymicrocap250` — via a `CONSTITUENT_CSVS` dict keyed
to `niftyindices.com/IndexConstituent/ind_<name>list.csv`; (2) its own inline `NOTE` flags TRI
**history** as unresolved ("Backpage.aspx/getHistoricaldatatabletoString POST endpoint [VERIFY]") —
i.e., **no historical index-level series is currently pulled for any index, sector or otherwise**,
only today's constituent snapshot. Two concrete extensions follow directly: **(a)** add the four
sector-index constituent CSVs to `CONSTITUENT_CSVS`, pattern-matching the existing naming
convention — `ind_niftymetal_list.csv`, `ind_niftyenergy_list.csv`, `ind_niftycommodities_list.csv`,
`ind_niftyoilgas_list.csv` **[VERIFY exact filenames — not confirmed against the live portal this
pass]**; **(b)** actually resolve and implement the TRI-history endpoint the script's own `NOTE`
already names as its top open item — without it there is **no historical sector-index level series
to condition on at all**, only a present-day name list, which blocks §C.8's sector-conditioner step
entirely until closed (named explicitly as a hard blocker there, not a soft one).

**Reconstitution hazard.** Semi-annual, confirmed for all four. The same PIT/survivorship concern
`pull_indices.py`'s own `NOTE` already flags for Total Market/Microcap ("pre-2023 membership is
reconstructed, not published") applies identically here: a name entering or leaving Nifty Metal on a
reconstitution date changes the index's realized metals beta discontinuously; a backtest that
projects *today's* constituent list backward silently manufactures a survivorship-clean-looking but
not point-in-time-clean history — the press-release archive (same one `pull_indices.py` already
notes for the four core indices) is the free source for the actual change dates, not yet pulled for
the sector family.

**The administered-price wedge — the design concern, quantified as far as free data allows.**
Nifty Energy's 40-name, 25%-industry-cap construction is built to include Oil Marketing Companies
(IOC, BPCL, HPCL) — whose retail fuel-marketing margins are historically government-influenced
(price freezes ahead of state elections are a recurring, documented pattern [VERIFY exact episode
dates/magnitudes]) — alongside upstream crude-linked names (ONGC, Oil India) and gas/power/telecom-
diversified conglomerates (Reliance Industries' O2C-plus-retail-plus-telecom structure likely makes
it the index's single largest weight by a wide margin [VERIFY exact current weight — semi-annually
rebalanced, not independently pinned this pass]). The mechanism this dilutes: an OMC's near-term
profitability can move **opposite** to crude direction during a margin-squeeze episode (crude up,
retail price frozen by policy → OMC margins compress even as the "energy" index's fundamental
upstream driver is bullish) — so **Nifty Energy's raw correlation to Brent/Kilian-oil will
understate the "clean" oil-cycle beta** an H53 sector-tilt conditioner actually wants to harvest.
Design implication, stated as a decision to make explicitly rather than default into silently:
prefer **Nifty Metal** (no comparable administered-price mechanism) and, once its methodology is
confirmed, a **narrower Nifty Oil & Gas** cut over Nifty Energy for a clean commodity-beta read, or
decompose Nifty Energy's own constituents into administered vs. market-priced buckets before using
it as a conditioner input. **[VERIFY: index weights]** applies throughout this section — exact
current weights rebalance semi-annually and were not live-pulled this pass.

---

## C.6 China demand-side proxies (H54 adjacency) — scope discipline, kept short

**BIS — the free source, and the honest mirror-hunt result.** BIS's own Data Portal
(`data.bis.org/topics/CREDIT_GAPS/data`) publishes credit-to-GDP gap series including China,
free, no login, quarterly — the standard source Atlas 2.11 already names. Per this desk's
established pattern (World Bank/FRED confirmed blocked at this container's proxy, `ingest/README.md`
addendum 5; Known Prior #11 groups FRED among the blocked hosts for this environment specifically),
treat BIS as **[VERIFY]**-blocked here too and reachable only from the principal's machine, same as
every other live host in this program. **GitHub-mirror hunt, reported honestly per this chapter's
own instruction**: the one relevant repository found this pass, `github.com/expersso/BIS`, is a
**client library** (an R package) that calls BIS's own SDMX/API endpoints programmatically — it
hosts no cached copy of the data, so it does **not** bypass a proxy block; running it from a
blocked network fails identically to a direct pull. **No usable static GitHub mirror of BIS
China credit-gap data is known as of this pass** — recorded as a genuine gap, not glossed as
solved.

**Scope discipline — what this chapter's pipeline must NOT duplicate.** H54 (China credit impulse)
is its own Atlas candidate with its own eventual data chapter. H53/1.3's pipeline should, at most,
consume a **single published reading** of the BIS China credit gap (or its best free substitute) as
**one enrichment input feeding L9**, exactly as Atlas 2.11 already frames it ("L9 enrichment
input") — it must not re-derive a China credit gap from scratch here, must not stand up a parallel
China iron-ore-import or steel-PMI scraper independent of whatever H54's own chapter eventually
builds (China customs iron-ore import volumes and Caixin/S&P Global China PMI are both free to
*read* monthly but carry the same exploration-only, no-vintage-layer caveat fincycle-deep §C.4 and
value-deep §C.6 already establish for scraped secondary aggregators — inherited, not re-derived
here), and must not let China-demand enthusiasm leak into the metals/energy sector-tilt conditioner
as a second, unbudgeted channel alongside H53's own ToT-state channel. One mechanism (China's
stimulus pulse moving global commodity demand), one eventual seat (inside L9's `global_cycle`
block), never double-counted across an H53 sector conditioner and a same-named H54 input.

---

## C.7 Vintage/PIT hazard table

| Source | Publication lag | Revision policy | Break / date | Backtest hazard |
|---|---|---|---|---|
| DGCI&S Tradestat | Provisional monthly (~weeks), finalized annually [VERIFY exact SLA] | Provisional → final, standard customs-data revision cycle [VERIFY magnitude] | Portal bulk-query window confirmed only from ~2018 [VERIFY pre-2018 access path] | Weight vector built on a provisional monthly print may shift on finalization; use annual finalized chapter-wise data for the weight vector itself |
| PPAC crude basket / Snapshot | Daily (price); monthly (Snapshot) [VERIFY monthly SLA] | Not typically revised (price); Snapshot aggregates [VERIFY] | — | Basket-price series stable; import-dependency % is a slow-moving stat, low hazard |
| Coal Controller monthly imports | [VERIFY, not pinned this pass] | [VERIFY] | — | Coal leg of C.1/C.2 least-verified this pass |
| IMF PCPS (GitHub mirror) | N/A — static historical file | **Never revised in place**: a refresh is a full new-vintage file (WORM rule), per `AUTHENTICATION.md` | **Ends 2017-06 hard stop** — no later vintage exists in this mirror | Any post-2017 use requires a new pull, not an extrapolation of this file |
| EIA Brent/WTI monthly | Already vaulted (1987–2026.07) | [VERIFY EIA's own revision policy for historical monthly averages] | — | Only basket line with a confirmed 1850→2026 continuous splice path (via Jacks Petroleum) |
| Jacks 1850–2015 | N/A — static academic dataset | Not revised (fixed academic release) | 1900=100 base is fixed by construction, not a break | Deflator convention **[VERIFY]** — inherited open flag from `AUTHENTICATION.md` |
| WPI | Provisional on the 14th, ~2-week lag; later revised | Two-vintage (provisional → revised), standard OEA practice [VERIFY exact revision window] | **2011-12→2022-23 rebase, effective 2026-06 release** (A-catalog H2, inherited) | Any Fuel & Power/Basic Metals series crossing 2026-06 needs the ratio-splice discipline of §C.2 |
| CPI | ~2-week lag | [VERIFY] | **2012→2024/COICOP-2018 rebase, effective 2026-02-12** (A-catalog H1, inherited) | Same splice discipline for Fuel & Light group |
| RBI BoP | ~10–13 weeks [VERIFY exact SLA] | Provisional → revised across subsequent quarters [VERIFY exact cadence/magnitude] | — | Every vintage provisional until a later release confirms it; never overwrite |
| RBI reference rate / FBIL | Daily, T+0 | Not revised | **2018-07-10**: RBI's own reference-rate press release discontinued; FBIL computes/publishes from this date | Two-source splice across the transition date, not one continuous archive |
| REER (RBI) | Monthly, ~1 month | [VERIFY] | 36-currency → 40-currency basket change (~2020, A-catalog G7) | Keep both basket vintages distinct; no synthetic splice, per A-catalog's own ruling |
| Forex reserves (WSS) | Weekly, ~T+0/T+1 | Not typically revised | — | Low hazard, one of RBI's most stable releases |
| Nifty sector indices (constituents) | Current-only (no history pulled yet) | Constituent list mutates every semi-annual reconstitution | Semi-annual (Jan-end/Jul-end cutoffs confirmed for Commodities; presumed same family-wide) | Pre-history-endpoint-build: **no PIT membership record exists in the pipeline at all** — the single largest gap in §C.5 |
| BIS China credit gap | Quarterly [source cadence] | [VERIFY] | — | Access itself [VERIFY]-blocked at this container; principal's-machine-only like the rest of the program |

---

## C.8 The full H53 pipeline

**Framing, stated first.** `ladder.yaml` carries **no H53 entry** — it is an Atlas candidate, not a
registry line, and per Atlas §8's own governance rule ("each needs its Appendix-C row... a
pre-registration file... Tier-C treatment until earned. None touches the ladder or the registry
until then"), this Part must **not** propose editing `ladder.yaml`. What follows produces (a) an
enrichment reading that, once researched and argued, is a *candidate* for L9's existing `indicator`
field (which already names "Kilian index" as a precedent for exactly this kind of enrichment-not-
new-seat treatment), and (b) a sector-tilt conditioner with no regime-score budget of its own.

1. **Registry load.** Validate `config/ladder.yaml` against `config/validator.py` before any pull —
   the same gate every other pipeline uses; H53 touches no registry field yet, so this is a
   no-op check that the ladder itself still loads clean.
2. **Pull raw fixtures** into `data/fixtures/P_commodity/{dgcis_tradestat_chapterwise,
   ppac_crude_basket,ppac_snapshot,coal_controller_imports,rbi_bop_memo_lines,wpi_fuel_metals,
   cpi_fuel_light,rbi_reer,rbi_wss_reserves,rbi_refrate_archive,fbil_refrate,
   nifty_{metal,energy,commodities,oilgas}_constituents}/{vintage}/...` — a new fixture family
   (no existing `ingest/pull_*.py` script covers any India-side commodity source; see §C.10).
   Manifest immediately (`python ingest/manifest.py data/`).
3. **STEP 1 — world real supercycle state.** (a) *Annual long-history leg*: build the
   basket-weighted composite from Jacks columns per §C.2's mapping, weighted by §C.1's shares
   (renormalized to whichever lines Jacks covers — everything except fertilizer's modern
   granularity); Hamilton filter (h=5y, p=1, expanding); `expanding_percentile(min_obs=40)` —
   trustworthy from **≈1900**. (b) *Monthly modern splice*: identical construction from IMF PCPS
   (1980-02→2017-06) plus the EIA Brent/WTI extension for the crude line only (1987→2026);
   Hamilton filter (h=60mo, p=1); `expanding_percentile(min_obs=48)` — trustworthy from **≈1989**
   for the crude-dominated modern composite; every other line's monthly percentile is either
   absent or frozen at 2017-06 until §C.10's new pulls land. **Splice rule**: ratio-at-overlap
   (`k = new(t0)/old(t0)`) applied to the basket-weighted composite level at the last mutual
   annual observation — register this as its own named entry (`commodity_basket_splice_2017`)
   once it lands in the registry, per the same naming discipline debt-deep/fincycle-deep use for
   their own base-transition splices.
4. **STEP 2 — India ToT state.** §C.1's weight vector applied to STEP 1's composite; **USD-real is
   primary** (§C.2's recommendation); the INR-terms variant computed downstream (FBIL/RBI rate ×
   CPI-Combined deflation), never substituted for the primary ranking.
5. **STEP 3 — WPI/CPI passthrough validation.** §C.3's lagged regression, run against both the
   world and India-weighted states, purged/embargoed — a pass/fail gate on whether the state is
   measuring what it claims to, not a scored input.
6. **STEP 4 — sector-conditioner outputs.** Map the ToT state's *per-line* sub-percentiles
   (metals sub-percentile, energy sub-percentile) to Nifty Metal / Nifty Oil & Gas / Nifty
   Commodities relative-return conditioning, with Nifty Energy carrying the explicit
   administered-price-wedge caveat from §C.5 logged alongside its output, never silently
   corrected for. **CONFIRM-only pattern** (mirroring how Atlas frames H60 breadth as "a CONFIRM
   input... regime only"): the conditioner may inform an existing sector-tilt decision, never
   generate a standalone alpha claim, until purged-CV clears it.
7. **STEP 5 — L9 enrichment candidate.** Package the world ToT state's percentile as a candidate
   reading for L9's `indicator` field, alongside Kilian-decomposed oil (already there) — submission
   only, not activation; L9 itself is **not** `reduce_only` in `ladder.yaml` (tier B, additive
   inside `global_cycle`), so an eventual H53→L9 enrichment that could *add* through that block
   requires its own pre-registered argument before it can do so — this pipeline does not make that
   argument, it only produces the candidate reading.
8. **Failure modes.** DGCI&S portal-navigation fragility (the same class of friction fincycle-deep
   §C.1 already documents for DBIE-family portals); PPAC page-structure drift; **gold's missing
   modern monthly leg** — must fail loud (a stale/absent flag) rather than silently interpolate
   a fabricated gold-price path; **the Nifty sector-index TRI-history endpoint simply not existing
   yet** — a hard blocker on STEP 4, not a soft one, since there is no historical index level to
   condition against until `pull_indices.py`'s own flagged gap (§C.5) is closed.
9. **Manifest every derived fixture** (basket weight vector by fiscal year, world composite
   gap/percentile, India ToT gap/percentile, passthrough regression outputs, sector-conditioner
   panel) as its own versioned, checksummed artifact; corrections append a new vintage row, never
   overwrite.
10. **Monitor cadence.** Weight vector (§C.1): **annual**, at DGCI&S's fiscal-year finalization.
    World/India ToT state: **monthly**, bound by the slowest currently-binding leg (crude-only
    modern splice today; degrades further, not less, once other lines' 2017+ gaps close and their
    own cadence becomes binding). Passthrough validation: **quarterly**, or re-run at each WPI/CPI
    base transition. Sector-conditioner correlation: **semi-annual**, matched to the Nifty
    reconstitution cadence so a name is never scored against a defunct index composition.
11. **Tier-C discipline.** Per Contract §4 and Atlas 1.3's own framing ("Tier C until researched"):
    H53's sector-tilt output may only **reduce** a sector's regime permission — cap metals/energy
    leverage or concentration when the ToT state signals a late, extended commodity boom pressuring
    CAD/INR — never add sector conviction on its own. The L9-enrichment leg inherits whatever tier
    and reduce/additive status L9's own registry entry carries **only after** its own
    pre-registered argument clears (STEP 5); until then, H53 is CONTEXT + reduce-only sector
    conditioning, exactly as Atlas 1.3 states, and this pipeline does not pre-empt that argument.

---

## C.9 What cannot be measured free — the honest list

| Need | Why it's out of reach free | What we do instead |
|---|---|---|
| **Modern (2017→) monthly world gold price mirror** | IMF PCPS panel carries no gold column at all; FRED's LBMA-fix mirror is [VERIFY]-blocked at this container | Long Jacks leg only until a new pull (FRED `GOLDPMGBD228NLBM` on the principal's machine, or WGC/MCX gold as an interim proxy) lands — §C.10 item 32; flag the state as stale on the gold line until closed |
| **Modern global fertilizer input prices** (Urea/DAP/Potash) | Absent from IMF PCPS entirely; World Bank Pink Sheet carries a fertilizer sub-index but the source is blocked and no GitHub mirror was found this pass | Jacks' `Phosphate`/`Potash`/`Sulfur` long leg only, no modern splice; smallest-weight basket line, lowest priority to close |
| **A true landed (CIF) India import cost, vs. world FOB price** | Freight/insurance cycles (e.g., Baltic Dry-type indices) are a separate, freight-driven wedge between world commodity prices and India's actual paid price; not measured by a world-price × basket-weight construction at all | Disclose the FOB-only limitation inline; the wedge is a known, unquantified source of state error, not correctable free |
| **China's own true credit impulse, granularly** | Out of scope by design (§C.6) — belongs to H54's own eventual data chapter | A single published BIS (or best free substitute) reading consumed as one L9 enrichment input, never re-derived here |
| **OMC-specific administered-margin history, structured and bulk** | Government press releases on fuel-price freezes/under-recoveries exist but no centrally published, fine-grained bulk series of marketing-margin history post-2010 deregulation was found free this pass [VERIFY] | The administered-price wedge is disclosed qualitatively (§C.3, §C.5) rather than quantified from a missing series |
| **Pre-2018 DGCI&S Tradestat bulk online history** | Portal bulk-query modules confirmed only from ~2018; earlier years exist only as scanned annual "Foreign Trade Statistics" PDF volumes [VERIFY] | Budget a PDF-transcription project only if the weight vector's own pre-2018 history is ever needed for a robustness check, not for Phase-0 |

---

## C.10 Runsheet additions (addendum 6)

No existing `ingest/pull_*.py` script covers any India-side commodity-exposure source — the same
"genuinely new fixture family" finding fincycle-deep records for real estate and value-deep records
for fundamentals. Numbered as extensions past fincycle-deep's own runsheet (which ended at step 24)
to avoid collision with the other Part Cs' own numbered extensions:

| Order | Task | Series | Est. hours | Why this order |
|---|---|---|---|---|
| 25 | Pull DGCI&S Tradestat chapter-wise (Ch.15/26/27/31/71/72–83) + commodity-wise import data; confirm the portal's real bulk-query date range | §C.1 | 4–6 | The weight vector is the foundation every downstream leg depends on; confirm the 2018-vs-earlier access question here rather than discovering it mid-pipeline |
| 26 | Pull PPAC Indian crude basket daily archive + monthly Snapshot/Ready-Reckoner (volume/value/dependency %) | §C.1, §C.2 | 2–3 | Small, high-value; the crude leg is the only one with a full modern splice today, so keep it that way |
| 27 | Pull Ministry of Coal / Coal Controller monthly grade-wise import statistics | §C.1 | 2 | Cheap; resolves this Part's most-[VERIFY]-tagged cadence gap |
| 28 | Pull RBI BoP quarterly press-release tables, full available history, oil/gold/non-oil memo lines, flag provisional vs. revised vintages | §C.4 | 3–4 | Piggybacks the DBIE scraper credit-deep's own runsheet already budgets — same portal family |
| 29 | Pull WPI (both bases, Fuel & Power + Basic Metals sub-series) and CPI (both bases, Fuel & Light sub-series) | §C.3 | 2–3 | Piggybacks A-catalog H1/H2's own already-scheduled pulls; two more sub-lines on the same source |
| 30 | Pull RBI reference-rate archive (pre-2018-07-10) + FBIL daily reference rate (post-2018-07-10); confirm the splice at the transition date | §C.4 | 2 | Small, mechanically easy, resolves a genuine two-source break cleanly before it surprises a later INR-terms computation |
| 31 | **Extend `ingest/pull_indices.py`**: add the four sector-index constituent CSVs to `CONSTITUENT_CSVS`; resolve and implement the TRI-history endpoint the script's own `NOTE` already flags unresolved | §C.5 | 4–6 | The single largest new-code item here; blocks §C.8 STEP 4 entirely until closed — do not defer |
| 32 | New pull: modern (2017→) monthly world gold price mirror (FRED `GOLDPMGBD228NLBM` once reachable; WGC/MCX gold as an interim free proxy) | §C.2, §C.9 | 2–3 | Closes the single largest state-construction gap (gold, ~6–8% basket weight, currently long-history-only) |
| 33 | New pull: exploratory hunt for a modern fertilizer-input price mirror (GitHub search for a World Bank Pink Sheet re-publication with Urea/DAP/Potash columns) | §C.2, §C.9 | 3–5 | Smallest-weight line; may legitimately return empty — budget as exploratory, not guaranteed |
| 34 | `config/` registry + CI validator smoke-test against the newly-pulled H53-adjacent fixtures | all above | 2 | Confirms the pull satisfies the "every module runs on fixtures with zero live data" gate, unchanged from every other Part C's own closing step |

**Total estimated incremental effort: ~24–33 hours**, on top of A-catalog's existing ~45–60-hour
Phase-0 estimate and the other Part Cs' own already-budgeted extensions — driven mainly by step 31
(the sector-index TRI-history build, the one item here with no existing scraper to extend) and the
two exploratory new-pull items (32, 33) closing the gold/fertilizer gaps §C.9 names honestly.

---

*End of Part C. Cross-references: `research/CONTRACT.md` §3 (free-source mandate), §4 (evidence
tiers, Tier-C reduce-only), §6 (no magic numbers — h/p reuse argued in §C.2), §8 (Hamilton filter
only), Known Prior #11 (no live network access; principal's-machine ingestion); `config/ladder.yaml`
L9_global_financial_cycle (candidate enrichment slot, §C.8 STEP 5 — no registry edit made here);
`quant/stats/hamilton.py` (`hamilton_filter`), `quant/ladder/credit_cycle.py`
(`expanding_percentile`, re-exported via `quant/ladder/__init__.py`) — the shared machinery §C.2
points to, not reimplements; `ingest/vault/commodities/` (Jacks, Clio-Infra/USGS, IMF PCPS, EIA
Brent/WTI, `AUTHENTICATION.md`) — the already-vaulted world-price side this Part builds on and does
not restate; `ingest/pull_indices.py`, `ingest/pull_nse_bhavcopy.py` (read directly, §C.5 — exact
extensions specified, not guessed); `ingest/README.md` addendum 5 (the pre-1.3 commodity-data probe
this chapter's vaulting inherits) and this chapter's own addendum 6 (§C.10); `docs/CYCLE_ATLAS.md`
row 1.3 (H53), row 2.11 (H54 — scope boundary, §C.6), row 2.12 (oil/Kilian, inherited into L9);
`research/cycles/fincycle-deep/partC-data.md` (the style bar this Part matches: splice-rule
convention, warm-up-arithmetic method, PIT-hazard-table format, exploration-only rule for scraped
aggregators); `docs/masterplan/A-data-catalog.md` H1/H2 (CPI/WPI base transitions, inherited not
duplicated), G6/G7/G10 (WSS, REER, reference rate, inherited), §4 (Phase-0 runsheet, extended in
§C.10).*
