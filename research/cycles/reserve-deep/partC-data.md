# Part C — Data engineering: watching a monetary order, free

v1.0 · 2026-09-01 · Atlas 0.2 (reserve-currency / monetary-order transition), `docs/CYCLE_ATLAS.md`
entry 0.2: "~80–110y; n≈2–3 ever (guilder→sterling→dollar)... Active leg today: sanctions-driven CB
gold buying since 2022." Atlas 0.2's Parts A/B/D/E/F/H are still queued (`docs/cycles/README.md`);
this Part is delivered first because the ladder seat it feeds is already live and already partially
built: `config/ladder.yaml L15_long_wave_fiscal` names its role as **"debt/GDP level+5y slope,
negative-real-rate persistence, reserve diversification (RBI gold, COFER)"** — three legs, and
`research/cycles/debt-deep/partC-data.md` already sourced the first two (fiscal aggregates,
real-rate splice). **This Part's job is the third leg only**: the reserve-diversification /
composition input — the "CB-gold accumulation leg + COFER drift leg" the task brief names, which
is also the entirety of what `research/cycles/reserve-deep/cofer-RESULTS.md`'s RC1–RC3 trial
measured on the desk's existing 1999Q1–2023Q1 COFER mirror. L15 itself carries **no regime-score
seat** (`ladder.yaml`: "L15/L16 have NO regime-score seat") — its whole authority runs through the
`long_wave_expression` gold-floor-attribution and tail-budget bands, Tier C, reduce-only (CONTRACT
§4). Extends, not duplicates, `docs/masterplan/A-data-catalog.md` blocks **G** (G6 WSS, G7 REER,
G10 reference-rate archive), **J** (J4 COFER, J5–J8 FRED) and **K** (K1–K3 gold) — cross-referenced
by ID below — and feeds K1's dual consumer, `gold_score`'s `cb_buying_regime` input (weight
0.20–0.25, B-module-specs.md §6.5), which reads the identical WGC/RBI series this Part sources.
Consumes CONTRACT §3 (free-source mandate) and Known Prior #11 (no live network access here; RBI,
IMF, FRED, WGC, SWIFT all block direct fetch from this container — web search does not; every pull
below happens on the principal's machine against a committed fixture). Checked by web search this
pass, cross-checked across ≥2 results where feasible, nothing fetched directly; anything not so
corroborated carries **[VERIFY]**.

---

## C.1 IMF COFER — the FX-reserve composition leg

**Access.** IMF migrated its data dissemination to a new SDMX-3.0-based platform at
`data.imf.org` (superseding the legacy `dataservices.imf.org/REST/SDMX_JSON.svc` endpoint, now
being retired) during 2023–2024; COFER's live page is
`data.imf.org/en/datasets/IMF.STA:COFER` (the older `data.imf.org/en/Datasets/COFER` /
`data.imf.org/COFER` short-links still resolve but should not be treated as the canonical path
for a build script). Bulk pull is a free SDMX/CSV export, no login, no API key required. **147
reporters** currently participate (monetary authorities of IMF members, several non-members, and
other reserve-holding entities) — this count itself is a vintage-dependent fact, not a constant.

**Cadence and lag.** Quarterly, ~1-quarter publication lag — the standard the desk's mirror and
`cofer-RESULTS.md` already assume. IMF's COFER methodology note (BOPCOM 24-09) is the primary
citation for cadence and reporter mechanics.

**The allocated/unallocated split — what it is, and the China distortion specifically.**
COFER has always separated **allocated reserves** (reporters who disclose currency composition)
from **unallocated reserves** (everyone else's total FX reserves, imputed from the IMF's
International Liquidity database as a residual). Two properties made this residual large and
lumpy rather than a clean noise floor: (i) **China does not, and has not, reported the currency
composition of its reserves to COFER** — the world's largest reserve holder by a wide margin sat
entirely inside "unallocated" for most of COFER's history; (ii) the unallocated share was
correspondingly enormous early on — roughly half of world reserves in the early 2000s — and fell
mechanically as more countries began reporting, **not** because currency preferences shifted.
IMF itself dates a material step-change to **2018**, when it confirmed a broadened/improved
reporting base that materially lifted the allocated share — commonly read as at least a partial
**China phase-in of COFER-visible reporting over 2015–2018**, though whether China's own reserves
became directly visible (vs. the pool of *other* non-reporters filling in) is genuinely disputed
in the literature and is flagged **[VERIFY: whether China itself became a COFER-allocated reporter,
or the 2015–18 allocated-share rise reflects other non-reporters joining]**. A second, unrelated
suppression sits in the same window: starting **2015 Q2**, IMF stopped publishing the
advanced-economies vs. emerging-and-developing-economies breakdown of COFER, citing the risk that,
with a published list of participants, that split could allow individual-reporter disclosure —
a confidentiality-driven data cut, not a definitional one, but one more break landing in the same
2015 quarter.

**The honest splice rule.** Any USD-share (or any currency-share) time series crossing 2015–2018
is measuring two effects at once: genuine portfolio drift among *already-reporting* central banks,
and a **mechanical composition-pool change** as large non-reporters (China foremost, disputedly)
entered or exited the visible pool. The rule this forces: **never read a level break or slope
change in the COFER share series across 2015–2018 as a pure preference signal without checking the
allocated-reserves coverage ratio (allocated ÷ total) for the same window** — a jump in that ratio
is the tell that the share series moved for compositional, not behavioral, reasons. This is
identical in kind (not in date) to the 2025Q3 break below, and both breaks now sit inside the
desk's own measured window (`cofer-RESULTS.md` RC1's 1999Q1→2023Q1 span brackets 2015–2018 whole).

**The 2025Q3 break, restated for construction.** Starting **2025 Q3**, with revisions applied back
to **2000 Q1**, IMF eliminated the unallocated bucket outright, publishing a currency composition
that nets to 100% of world reserves — **10.4% of that 2025Q3 total is IMF-imputed**, not
reporter-disclosed (A-catalog J4 already flags the break; the imputed-share figure is new this
pass). This means the post-2025Q3 series is not merely a reweighting of the same allocated data to
a new denominator — a genuine model-based estimate for non-reporters (China very much included) is
now baked into the published USD share itself. **Rule**: any COFER pull spanning 2025Q3 uses the
revised series only, end to end; the pre-revision vintage is retained in the vault (never deleted)
strictly as an audit trail for exactly this kind of before/after comparison, never spliced onto the
new one mid-series.

**Table structure — claims vs. shares.** COFER ships two related objects, and a build script must
pull both, not just the shares:

| Object | Unit | What it is | Historical availability |
|---|---|---|---|
| Currency composition, **claims** | US$ millions | Level of allocated reserves held in each currency, World aggregate | 1999Q1+ (pre-2025Q3 vintage); 2000Q1+ (post-2025Q3 revised vintage) |
| Currency composition, **shares** | % of allocated reserves (pre-2025Q3) / % of total reserves (post-2025Q3) | Claims ÷ the relevant total — the series `cofer-RESULTS.md` RC1–RC3 already computed | Same as above |
| Allocated reserves, total | US$ millions | Denominator for shares (pre-2025Q3) | 1999Q1+ |
| Unallocated reserves | US$ millions | Residual (pre-2025Q3 vintage only — eliminated from 2025Q3 onward) | 1999Q1–2025Q2 |
| AE / EMDE breakdown | US$ millions, by currency | Discontinued **2015 Q2** — a level break in coverage, not in the currency definitions | 1999Q1–2015Q1 only |

The claims level matters independently of the share: a currency's share can fall purely because
total reserves grew faster in currencies the reporting pool happens to hold more of, with the
claims level in that currency flat or even rising — the level/share distinction is the same
discipline the debt monograph applies to debt stock vs. debt/GDP ratio.

**Extending the desk's 1995–2023Q1 mirror forward (principal's machine).** The existing vault file
(`ingest/vault/debt/cofer_1995_2023q1.csv`, sha256-manifested, RC0-authenticated against the
Arslanalp-Eichengreen-Simpson-Bell anchor values) is a **pre-2025Q3-methodology** vintage. It
cannot simply be appended to: a naive "pull 2023Q2-onward and concatenate" script would splice an
old-methodology (unallocated-included) history onto a new-methodology (unallocated-eliminated,
imputed) tail — precisely the error this Part's splice rule forbids. The correct procedure:

1. Pull the **entire** current COFER SDMX/CSV extract fresh (2000Q1–latest, post-2025Q3 revised
   vintage) — do not attempt a delta pull. Manifest as a **new**, distinctly named fixture
   (`cofer_2000q1_{latest}_rev2025q3.csv`); the existing 1995–2023Q1 file stays untouched.
2. Re-run `scripts/analyze_reserve_currency.py`'s RC0–RC3 trials against the new fixture in
   parallel with the old one. RC0's authentication check (USD share 1999Q1 ≈71%, 2021Q4 ≈58.8%)
   should still pass on the revised vintage *if* the revision genuinely only reallocates the
   unallocated residual — a failure there is itself informative (flags that the revision moved
   the allocated-only numbers too, not just the total).
3. Diff RC1's measured slope (−0.51pp/yr, 1999Q1→2023Q1, old vintage) against the same window
   recomputed on the revised vintage. Any material difference is the **2025Q3 revision's own
   contribution to the measured drift** — report it explicitly, never blend it silently into "the
   dollar's decline."
4. 1999Q1 itself sits **outside** the revision's 2000Q1 floor — treat it as a one-quarter orphan on
   the revised series (drop it from any revised-vintage-only construction, or keep it flagged as
   old-vintage-only in a mixed table).
5. From here forward, each new COFER release is a routine same-vintage append (both vintages remain
   fixed methodology until IMF's next break); manifest each new quarter's pull separately, keyed
   `(series_id=COFER, vintage=post-2025Q3, pull_date)`.

---

## C.2 WGC central-bank gold data — the leg COFER cannot see

**What's free.** The **Gold Demand Trends** quarterly report (`gold.org/goldhub/research/
gold-demand-trends`) — including its dedicated **Central Banks** section per edition
(`.../gold-demand-trends-q{n}-{yyyy}/central-banks`) and the standalone **country-level holdings**
page (`gold.org/goldhub/data/gold-reserves-by-country`, itself built from **IMF IFS** data, so it
overlaps J4 at a country granularity COFER itself does not expose) — is free to read as HTML/PDF.
**Free registration** ("free, quick, easy... unlimited access to all Goldhub market data")
unlocks the data-explorer's filter/date-range/download tooling; the PDF reports themselves are
open with no gate at all (A-catalog K1 already flags this split; confirmed again this pass).
**Cadence/lag**: quarterly, released roughly **4–5 weeks** after quarter-end — Q1 2026 on
2026-04-29, Q2 2026 on 2026-07-30, a consistent 4-week gap. A separate, faster **monthly**
central-bank-statistics post appears on the Goldhub blog between quarterly editions.

**The reported-vs-estimated-unreported distinction — the single largest data-honesty issue in
this section.** There is **no mandatory rule** requiring any country to report gold transactions
to the IMF. WGC's own headline "central bank net purchases" figure is **not** the IMF-reported
number — it is WGC's (via Metals Focus) own estimate, built from London OTC market flow, Swiss
refinery trade data, and other proxy indicators, explicitly designed to capture buying that never
shows up in any official disclosure. The gap between the two numbers is not a rounding matter:
**Q1 2026 IMF-reported net central-bank purchases were 16 tonnes; WGC's estimated total central-
bank demand for the same quarter was 244 tonnes — roughly 15× the officially disclosed figure**,
and Metals Focus separately estimated unreported buying at **57% of the full-year 2025 total**.
China is the largest single contributor to this gap: PBoC's officially reported 2025 purchases
were on the order of 25–41 tonnes (source-dependent; **[VERIFY]** exact figure, differs by outlet)
against SocGen's own estimate that China's true 2025 buying ran **~10× the official figure**, with
independent analyst estimates (Nieuwenhuijs; BMO Capital) putting China's **true cumulative gold
reserve** at roughly **5,000–5,200 tonnes** against an officially declared ~2,300–2,350 tonnes —
more than double. **Construction rule**: never present WGC's central-bank-purchase figure as if it
were the IMF-reported number, or vice versa; carry both, labeled, with the gap itself as an
informative series (a widening gap is itself a signal about the *opacity* of official gold
accumulation, arguably as relevant to Atlas 0.2's "active leg" as the purchase level itself).

**Tonnage vs. market-value accounting.** WGC's country-holdings table and RBI's own disclosures
both report gold in **tonnes** (a physical quantity, revision-free except for genuine
purchases/sales) alongside a **market value** in USD or local currency (tonnes × the prevailing
gold price × the FX rate, revised continuously as price/FX move with zero change in physical
holdings). A quantity series and a value series answering different questions must never be
plotted as if interchangeable — the identical trap the RBI section below documents concretely for
the May-2026 "phantom drawdown" episode.

---

## C.3 RBI's own reserves — WSS, monthly Bulletin, half-yearly gold report

| Source | Cadence | Access | What it uniquely carries |
|---|---|---|---|
| **Weekly Statistical Supplement (WSS)** | Weekly, published Fridays, reflecting the reserve position roughly one week prior (~1-week lag) | `rbi.org.in/scripts/WSSViewDetail.aspx?TYPE=Section&PARAM1=2` | FX reserves broken into Foreign Currency Assets, Gold, SDRs, Reserve Tranche Position — in both ₹ crore and US$ million; the fastest-cadence gold **value** read (A-catalog G6) |
| **RBI Bulletin monthly tables** | Monthly | `rbi.org.in` Bulletin section; DBIE-queryable | Same four-way FX-reserve split at monthly granularity, plus REER (G7) and reference-rate (G10) tables in the same document family |
| **Half-Yearly Report on Management of Foreign Exchange Reserves (HYRMFER)** | **Semi-annual** (Apr–Sep, Oct–Mar), released roughly **one month** after each half-year end — e.g. the 43rd edition (Apr–Sep 2024) was published 2024-10-30 | `rbi.org.in/scripts/HalfYearlyPublications.aspx?head=Report+on+Foreign+Exchange+Reserves` | **The only source for gold tonnage broken into domestic vs. overseas custody** — this is the input the desk's CB-buying-regime leg actually needs, and no weekly/monthly series carries it |

**The domestic-vs-custody split, and why it is the India-specific, sanctions-era signal.**

| As-of date | Total gold (tonnes) | Held domestically | Bank of England + BIS custody | Gold deposits | Domestic share |
|---|---|---|---|---|---|
| Mar-2023 | ~[VERIFY exact total] | ~301t | remainder | — | ~38% |
| Mar-2025 | 879.59t | ~[VERIFY] | ~[VERIFY] | — | ~59.2% (**[VERIFY]**, single-cluster of sources conflicts with a "60%, Jun-2024" figure in adjacent reporting — resolve on first live pull against the primary HYRMFER PDF, not secondary news) |
| Mar-2026 | 880.52t | 680.05t | 197.67t | 2.80t | **77.23%** |

The trajectory (38% → ~59–60% → 77.23% domestic, 2023–2026) is RBI's own explicit, dated response
to the 2022 Russia sanctions episode — the same freeze-of-reserves shock the Atlas 0.2 entry names
as the "active leg today." **This is the single cleanest India-specific, free, quarterly-or-better,
directly-observable proxy for the sanctions-driven-reserve-repatriation hypothesis** the whole
monograph is built around — better than any global aggregate, because it is one actor's own
disclosed balance-sheet choice, not an inferred flow.

**The May-2026 valuation-vs-quantity trap, worth naming explicitly.** RBI shifted its own gold
**revaluation** cadence from monthly to weekly (a documented methodology note), which means
week-to-week changes in the reported gold **value** can now reflect nothing more than price/FX
marking, not a change in tonnage. A May-2026 press episode inferred a gold *drawdown* from a
value-series analysis; RBI publicly denied any tonnage sale, and the tonnage figure in the next
HYRMFER confirmed no reduction — the value series moved, the quantity series did not. **Rule**:
tonnage must always be read from the primary WSS/HYRMFER tonnage line, never inferred from a
value-series delta, exactly the tonnage-vs-market-value discipline C.2 states for WGC data.

---

## C.4 Invoicing and settlement data — measuring the "how", not just the "how much"

**Academic invoicing-currency panels (Gopinath et al.).** The dominant-currency-paradigm
literature's own dataset — country-level shares of exports/imports invoiced in USD, EUR, and other
currencies — has been extended repeatedly (most recently to **132 countries, 1990–2023**, per the
newest working-paper vintage, with RMB coverage added). **No single, stable, versioned public
GitHub repository was confirmed this pass** — the practical access path is the NBER/AEA working
paper's own data appendix and the authors' institutional pages (Harvard/Princeton), not a
maintained package; **[VERIFY]** the exact current download URL and licence terms on first contact,
and treat any given vintage as a dated academic release (its own "vintage date"), not a live feed.

**RBI's own rupee-settlement mechanism data.** RBI's July-2022 framework for International Trade
Settlement in Indian Rupees requires foreign correspondent banks to open **Special Rupee Vostro
Accounts (SRVAs)**; RBI/press disclosures give periodic **counts** of the mechanism's uptake —
**156 SRVAs across 123 correspondent banks from 30 partner countries, as of February 2025**
(up from 92 accounts/20 banks in July 2023) — but **no RBI-published aggregate flow series**
(₹ value of trade actually settled through SRVAs) was found free this pass; the FEDAI-maintained
SRVA **directory** (a bank/account list, not a value time series) is the closest structured free
artifact. **Honest coverage note**: this is a **participation-count** proxy for rupee
internationalization, not a trade-value series — treat it exactly that way, the same caution the
CIPS participant count below requires.

**SWIFT RMB Tracker / Global Currency Tracker.** Free, monthly, no-login PDF
(`swift.com/products/rmb-tracker` document centre; direct edition URLs like
`swift.com/sites/default/files/files/rmb-tracker_july-2025.pdf`), covering RMB's share of SWIFT
payment-message value alongside a global-currency ranking table. RMB's share has moved from
**2.88% (Jul-2024 data) to ~3.50% (Apr-2025 data)**, sitting around 5th–6th globally across recent
editions. **Coverage caveat, stated plainly**: SWIFT-message share measures *messaging volume*
through the SWIFT network specifically — it structurally **undercounts** RMB settlement that
increasingly routes through CIPS instead of SWIFT-message rails (C.6), so a rising CIPS-participant
count alongside a flat-to-declining SWIFT RMB share is not necessarily "RMB internationalization
stalling" — it may be RMB settlement migrating off the rail SWIFT measures.

---

## C.5 Exchange-rate legs — the denominators every INR/gold/reserve series needs

| Series | Access | History | Cadence/lag | Note |
|---|---|---|---|---|
| **FRED DTWEXBGS** (Nominal Broad USD Index) | `fred.stlouisfed.org/series/DTWEXBGS`, free CSV, no login | **2006-01-02+**, rebased Jan-2006=100 | Daily, T+0/T+1 | Successor to the discontinued Major Currencies Index (DTWEXM, retired Jan-2020) and the goods-only DTWEXB — a **26-economy** trade-weighted basket including India, China, Euro Area; **any pre-2020 dollar-index series spliced onto DTWEXBGS crosses a methodology break**, identical discipline to A-catalog J5-J8's own flag |
| **BIS Effective Exchange Rate indices (NEER/REER)** | `data.bis.org/topics/EER` — migrated to the **BIS Data Portal on 2023-11-22** (supersedes the older `bis.org/statistics/eer.htm` static-file scheme); free single-file CSV bulk download, no login | India **broad** basket (64 economies): **Jan-1994+**; narrow basket (26–27 economies) also available | Monthly | The free, non-RBI, cross-country-consistent REER cross-check against RBI's own G7 series — useful precisely because RBI's 36→40-currency basket change (A-catalog G7) is an RBI-specific break that BIS's own methodology does not share, giving an independent read through that transition |
| **RBI reference-rate archive (USD/INR)** | `rbi.org.in/scripts/referenceratearchive.aspx` | Daily archive runs from **April 1995** (per this pass's search; A-catalog G10 leaves this **[VERIFY]** — resolved here) | Daily, same-day | **FBIL took over computing/disseminating the reference rate from RBI effective 2018-07-10** — a compiler change, not (per this pass) a level break in the rate itself, but the compiler-of-record fact belongs in the fixture's metadata |

---

## C.6 Complements — SDR basket weights, swap-line networks, CIPS

**IMF SDR basket weights — five-yearly reviews as dated regime markers.** Free, published on
every review (`imf.org/en/topics/special-drawing-right/sdr-valuation-basket`; the IMF's own
infographic PDF, "board-approved SDR basket currency weights at past quinquennial reviews," is the
single cleanest citation). Reviews run on a nominal five-year cycle, with one COVID-era delay:

| Review (effective date) | USD | EUR (DEM+FRF pre-1999) | JPY | GBP | RMB |
|---|---|---|---|---|---|
| 1991 (1985–89 data) | 40% | 21%+11% | 17% | 11% | — |
| 1996 | 39% | 21%+11% | 18% | 11% | — |
| 2001 | 45% | 29% | 15% | 11% | — |
| 2006 | 42.9% | 34.1% | 11.5% | 11.5% | — |
| 2011 | 41.9% | 37.4% | 9.4% | 11.3% | — |
| 2016 (eff. 2016-10-01) | 41.73% | 30.93% | 8.33% | 8.09% | 10.92% |
| 2022 (eff. 2022-08-01, delayed ~1yr for COVID) | 43.38% | 29.31% | 7.59% | 7.44% | 12.28% |
| Next (due by end-Jul-**2027**) | — | — | — | — | — |

1981/1986 review weights not independently confirmed this pass — **[VERIFY]**. The RMB's
inclusion (2016) is itself the cleanest single dated marker in the entire free-data landscape for
"the IMF formally certified a challenger currency as freely usable" — a regime-marker Atlas 0.2's
theory section (once written) should anchor directly to this table, not to a vaguer "China's rise."

**Swap-line networks — a free, trackable network measure.** The Fed maintains **five standing,
permanent** dollar-swap lines (Bank of Canada, BoE, BoJ, ECB, SNB — since 2013-10-31,
`federalreserve.gov/regreform/reform-swaplines.htm`, free) plus **temporary** lines opened and
closed around stress episodes (nine additional central banks in Mar-2020, most since lapsed) —
the New York Fed's own swap-arrangements page is the free primary source for current status. The
PBoC runs a parallel, larger, and still-*growing* bilateral network: **32 countries/regions as of
May-2025**, cited elsewhere as **42 active lines totaling ~¥3.84 trillion (~US$540bn) by
end-Q1-2026** (figures from different trackers/dates — **[VERIFY]** reconciliation; PBoC's own
page, `pbc.gov.cn`, is the primary free source, supplemented by the CFR's free **Central Bank
Currency Swaps Tracker**, `cfr.org/articles/central-bank-currency-swaps-tracker`). **As a network
measure**: track swap-line **count** and **total committed value** for both networks quarterly,
free, from primary-institution pages — a rising PBoC-network node count against a static
five-country Fed standing network is a legitimate, quantifiable proxy for "who is building
reserve-currency-adjacent crisis-liquidity infrastructure," independent of any FX-share metric.

**CIPS participant counts.** China's Cross-Border Interbank Payment System publishes participant
counts periodically via its own site (`cips.com.cn/en`) and PBoC/state-media releases — **free**,
but as **periodic disclosure, not a queryable time series**: **193 direct / 1,573 indirect
participants across 124 countries at end-2025**, rising to **210 direct / 1,619 indirect across
192 countries by end-Jun-2026** (sourced via press releases and secondary trackers this pass —
**[VERIFY]** against CIPS's own primary release page on first live pull). Pair with the SWIFT RMB
Tracker (C.4) explicitly: a rising CIPS node count with a flat SWIFT-message RMB share is the
signature of settlement infrastructure migrating off the rail SWIFT actually measures.

---

## C.7 Vintage/PIT hazard table

| Series | Revision-prone? | Two dates never to conflate | Store first-print or every vintage? |
|---|---|---|---|
| COFER shares | **Yes, twice over** — the 2015-18 reporting-pool broadening and the 2025Q3 unallocated-elimination (revised to 2000Q1) | Reporting-pool-coverage date (mechanical) vs. genuine drift date (behavioral); pre-/post-2025Q3 methodology | **Every vintage**, both the pre- and post-2025Q3 series kept distinct forever (A-catalog J4) |
| WGC central-bank purchases (WGC/Metals Focus estimate) | **Yes** — WGC's own single-quarter reading is provisional for ~1-2 subsequent quarters as more country data arrives; the reported-vs-estimated gap itself is a moving target | WGC estimate-vintage date vs. IMF-reported figure's own (separate, slower) vintage | Both series kept distinct, never merged into one "central bank buying" number |
| RBI gold (WSS/HYRMFER) | Not revision-prone in tonnage; the **value** series moves continuously on price/FX with no tonnage change | Weekly-revaluation value-change date vs. actual tonnage-change date (HYRMFER, semi-annual) | Tonnage: append-only event log; value: continuous series, always paired with the concurrent tonnage figure |
| RBI domestic/custody gold split | Semi-annual step series, not continuously revised | HYRMFER as-of date (Mar/Sep) vs. report publication date (~1 month later) | Every HYRMFER edition retained as its own dated snapshot |
| DTWEXBGS / dollar index | Structural break, not a revision | Legacy DTWEXM/DTWEXB (pre-2020) vs. DTWEXBGS (current, 26-economy) | Both kept distinct; DTWEXBGS is the only series usable post-2020 |
| BIS REER basket | Portal migration (2023-11-22), not a series break | Old static-file era vs. BIS Data Portal era — same underlying series, different access mechanics | One continuous series; only the *access path* changed |
| RBI reference rate | Compiler handover (RBI → FBIL, 2018-07-10) | Compiler-of-record date | One series; compiler recorded as metadata, not a splice point |
| SDR basket weights | Not revision-prone — each review is a dated, discrete regulatory event | Review-decision date vs. effective date (these differ, e.g. 2022 decided May, effective August) | Append-only event log, both dates recorded |
| Swap-line networks / CIPS counts | Point-in-time disclosures, not continuously revised, but **frequently stale between disclosures** | Disclosure-as-of date vs. pull date (can lag disclosure by months in secondary sources) | Append-only event log; never interpolate between disclosed counts |

---

## C.8 The quarterly pipeline — from raw pulls to L15's reserve-diversification input

Matching the debt monograph's own Part-E-shaped algorithm (grids and the reduce-only clamp are
CONTRACT-frozen, not re-derived here):

1. **Registry load.** Validate `config/ladder.yaml L15_long_wave_fiscal` against
   `config/validator.py` before any pull.
2. **Pull raw fixtures** into `data/fixtures/P_reserve_composition/{cofer,wgc_gdt,rbi_wss,
   rbi_hyrmfer,fred_dtwexbgs,bis_eer,rbi_refrate,sdr_basket,swap_lines,cips}/{vintage}/...` — a
   genuinely new fixture family; no existing `ingest/pull_*.py` script covers any of COFER, WGC,
   RBI's HYRMFER, or the swap-line/CIPS trackers (see closing note). Manifest immediately
   (`python ingest/manifest.py data/`), every file keyed `(series_id, vintage_date, pull_date)`.
3. **CB-gold accumulation leg.** Pull WGC's quarterly central-bank-purchase estimate (C.2) *and*
   the IMF-reported figure separately, never merged; pull RBI's own WSS gold tonnage weekly and
   HYRMFER domestic/custody split semi-annually (C.3). Construct the composite leg as a **rolling
   12-month trailing sum of estimated global CB net purchases**, ranked against its own expanding-
   sample percentile (Contract's ≥4-observation warm-up floor applies — no percentile emitted
   until the sample clears it), *plus* RBI's own domestic-share trajectory as a India-specific
   confirm, not a separate weighted leg.
4. **COFER drift leg.** Pull the current-vintage COFER shares (C.1); compute the trailing 5-year
   annualized USD-share slope exactly as `cofer-RESULTS.md` RC3 already does, flagged by which
   methodology vintage (pre-/post-2025Q3) generated it, and by whether the window crosses the
   2015-18 reporting-pool break (in which case the allocated-coverage-ratio check from C.1 runs
   alongside it as a validity gate, not a silent pass-through).
5. **Composite construction.** The two legs are **enriched, reduce-only, never additive** — the
   Contract's Tier-C rule (§4) applied exactly as the debt monograph's captivity input applies it:
   a rising CB-gold-accumulation percentile *and* an accelerating (more negative) COFER USD-share
   slope can only pull the `long_wave_expression` gold-floor-attribution band toward its `[0.40,
   0.50]` upper end and lift the `conditional_gold_floor_lift_pp` toward its `[1, 2]` upper end
   (`ladder.yaml`) — neither leg, alone or combined, can push the *equity* regime score, because
   L15 has no regime-score seat at all.
6. **State representation.** Log as a phase object (level, velocity, quadrant, age-in-quadrant)
   per the 2026-09-01 states-as-phase-objects decision — not a scalar — for both legs
   independently before any combination.
7. **Manifest every derived fixture** (CB-gold-percentile panel, COFER-drift panel, the combined
   long-wave-expression band) as its own versioned, checksummed artifact; corrections append a new
   vintage row, never overwrite.
8. **Recalibration triggers**: a new COFER quarter (routine, ~1-quarter lag); a new WGC Gold
   Demand Trends edition (quarterly, ~4-5wk lag); a new RBI HYRMFER edition (semi-annual, ~1mo
   lag); any further IMF COFER methodology note (2025Q3-style); a new SDR quinquennial review
   (next due by end-Jul-2027 — a hard calendar date to pre-register against); any Fed/PBoC
   standing-swap-line addition or removal (event-based, not scheduled).
9. **Monitor**: quarterly refresh; annual review re-reads `cofer-RESULTS.md` RC1-RC3 with one more
   year of COFER data, checking specifically whether RC3's "no regime break through 2023Q1" finding
   still holds once 2022-26 sanctions-era quarters are in the post-2025Q3-revised series.

---

## C.9 What cannot be measured free — the honest list

| Need | Why it's out of reach free | What we do instead |
|---|---|---|
| **True unreported central-bank gold, especially China's** | No mandatory IMF reporting rule exists; China's gap between officially declared (~2,300-2,350t) and independently estimated true holdings (~5,000-5,200t) is a >2x uncertainty band, not a rounding error; WGC's own estimate (244t, Q1 2026) already runs ~15x the IMF-reported figure (16t) for the *global* aggregate | Carry WGC's estimated figure as the working series, IMF-reported as a labeled floor, and the gap itself as an explicit, separately-tracked opacity indicator — never present a single "the" central-bank-gold-buying number |
| **Real-time reserve composition of any single central bank** (India's own included, at true real-time granularity) | COFER is quarterly with a lag and country-anonymized at the aggregate level; RBI's own gold-tonnage split is semi-annual; no central bank publishes intraday or even daily reserve-currency-composition detail, by design (confidentiality is structural to the whole reserve-management function) | Accept the quarterly/semi-annual cadence as the ceiling; never interpolate a smoother series than the primary disclosure supports |
| **Forward-looking swap-line utilization** (how much of a standing line would actually be drawn in the next stress episode) | Swap lines are contingent facilities; utilization is observed only ex post, during an actual drawdown (the 2020 Fed data is the only clean historical read); no free source publishes a forward utilization probability or capacity-stress-test result | Track the **network** (count, committed value, C.6) as the ex-ante capacity measure; treat any utilization estimate as a narrative, Stage-2-only judgment, never a Stage-1 quantitative input |
| **A single reconciled Gopinath-style invoicing-currency panel with a stable, versioned free download** | The academic dataset is real and periodically updated but distributed via working-paper appendices and author pages, not a maintained public repository or API | Treat each vintage as a dated, manually-pulled academic release; never assume continuity between editions without checking the coverage-country list and base year each time |
| **RBI's own aggregate ₹-value of trade actually settled via SRVAs** | RBI/FEDAI publish the account/participant count (a capacity proxy) but no aggregate flow-value series was found free this pass | Use the SRVA count as a participation proxy only, explicitly labeled as such, never as a trade-value substitute |

---

*End of Part C. Cross-references: `research/CONTRACT.md` §3 (free-source mandate), §4 (evidence
tiers, Tier-C reduce-only), §7 Known Prior #11 (no live network access this environment;
principal's-machine ingestion); `config/ladder.yaml` `L15_long_wave_fiscal` and
`long_wave_expression`; `research/cycles/reserve-deep/cofer-RESULTS.md` (RC0–RC3, the real-data
COFER trial this Part extends forward); `docs/CYCLE_ATLAS.md` entry 0.2; `docs/masterplan/
A-data-catalog.md` blocks G/J/K (RBI/IMF-FRED/gold — extended, not duplicated, by this Part);
`docs/masterplan/B-module-specs.md` §6.5 (`gold_score`'s `cb_buying_regime` input, the other
consumer of the WGC/RBI series sourced here); `research/cycles/debt-deep/partC-data.md` (the
sibling Part supplying L15's other two legs — debt level/slope, real-rate persistence — and the
structural PIT/vintage-table pattern this file follows).*
