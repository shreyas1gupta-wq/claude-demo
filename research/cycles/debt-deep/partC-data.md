# Part C — Data engineering: measuring the fiscal-dominance state, free

v1.0 · 2026-09-01 · Extends this monograph's `partDEFH-math-algo-harvest-ledger.md` (Part E names
the three quarterly L15 inputs this Part must source: debt level+slope percentile, real-rate
persistence gauge, captivity/composition Tier-C input) and `jst-debt-RESULTS.md` (DS1–DS4, the
pooled priors India's own gauges are compared against). Extends, not duplicates,
`docs/masterplan/A-data-catalog.md` blocks **G** (RBI), **H** (MOSPI), **J** (IMF/BIS/FRED/World
Bank) and **K** (gold), cross-referenced by ID below (G3 policy rates, G6 WSS, J1–J4 IMF/BIS/
COFER, K1–K3 gold). This Part's job is the gap the catalog leaves: **no catalog entry exists at
all for centre/state debt stocks, the Status Paper on Government Debt, the State Finances report,
SLR/CRR history, or the Chinn-Ito index** — the same first-build gap value-deep Part C found for
company fundamentals. Consumes `research/CONTRACT.md` §3 (free-source mandate) and Known Prior #11
(no live network access — RBI, IMF, FRED, DEA, indiabudget.gov.in all block direct fetch here; web
search does not — ingestion happens on the principal's machine, every indicator against a
committed fixture). Feeds `config/ladder.yaml L15_long_wave_fiscal`. Checked by web search this
pass (snippet-level, cross-checked across ≥2 results where feasible; nothing fetched directly).
Anything not so corroborated carries **[VERIFY]**.

---

## C.1 The core problem — centre debt is not general government debt, and neither is "the" debt ratio

Every headline "India's debt/GDP" number conceals a choice among at least four different
aggregates, and the choice moves the number by 20–25 points of GDP:

| Aggregate | ≈FY26 level | What's in it | What's left out |
|---|---|---|---|
| Centre government debt (Budget/Status Paper definition) | **~58%** of GDP (FY26 RE, missing the government's own 55.6–56.1% target by ~200bp per press reporting **[VERIFY exact bp figure, single-source]**) | Dated G-secs, T-bills, external loans at book value, small savings/provident-fund liabilities booked to the Centre | State debt, PSU debt, RBI's own liabilities, contingent guarantees |
| State + UT debt (RBI State Finances aggregate) | **~28.5%** of GDP (end-March 2024) | Market borrowings (SDLs), loans from Centre, NSSF-funded securities, provident funds, reserve funds | Centre debt; municipal/local-body debt; off-budget SPV debt |
| **General government debt** (Status Paper's own consolidated figure) | **~80–81%** of GDP (end-March 2024) | Centre + states, **netting out** inter-government transactions (Centre's loans to states, states' NSSF-funded securities, states' T-bill holdings with the Centre) | Still excludes PSUs, quasi-sovereign SPVs, and contingent liabilities (§C.13) |
| IMF/BIS cross-country "general government gross debt" | Close to, but not identical to, the Status Paper's own general-government figure — different consolidation conventions (GFSM 2014 vs. India's own budget accounting) can diverge by a few points of GDP | IMF/BIS apply a standardized cross-country methodology, not India's own consolidation rule | Same as above, plus whatever GFSM-vs-India definitional gaps exist — **[VERIFY]** the exact reconciliation, not found this pass |

**The rule this forces on every downstream construction**: never plot "India debt/GDP" from a
single series without stating which of these four it is. L15's debt-level-and-slope input (Part E
STEP 1) must be built on the **general government** aggregate — the fiscal-dominance question is
about the sovereign's aggregate claim on real resources, and a centre-only series would understate
the true state by ~20+ points of GDP precisely because state borrowing has been the faster-growing
leg (states' debt/GSDP rose from 16.7% in 2013-14 to 23.0% in 2022-23 per CAG's own decadal
report, more than doubling in rupee terms). A centre-only series is acceptable only as a
**faster-updating proxy** between general-government publication dates (§C.12 pipeline step 3).

---

## C.2 Global debt stocks — the five free cross-country sources

| Source | Access path | History | Cadence / lag | India-specific quirk |
|---|---|---|---|---|
| **IMF WEO database** | `data.imf.org/en/datasets/IMF.RES:WEO` (SDMX bulk); per-edition vintage pages at `imf.org/en/publications/weo/weo-database/{year}/{april\|october}` | **1980+** | Twice yearly, **April and October**; each edition is itself a distinct, dated vintage | WEO's `GGXWDG_NGDP` (general government gross debt, % GDP) is the standard India pull; **pull and retain every historical vintage, never only the latest** — this is IMF's own explicit "Changes to the Database" practice (`data.imf.org/en/Datasets/WEO/Changes-to-the-Database`), and the design's PIT discipline is defeated if only the current, most-revised edition is kept (identical to A-catalog J2) |
| **IMF Fiscal Monitor** | `imf.org/en/Publications/FM`; data cut via `data.imf.org` | Modern editions; the GDD (next row) grew out of its Oct-2016 edition | Twice yearly, alongside WEO | Carries India's fiscal-deficit and primary-balance path at general-government and central-government granularity in the same document — the natural cross-check against the Status Paper's own numbers |
| **IMF Global Debt Database (GDD)** | `imf.org/external/datamapper/datasets/GDD`; annual **Global Debt Monitor** PDF (e.g. `imf.org/external/datamapper/GDD/2025 Global Debt Monitor.pdf`) | **1950+**, unbalanced panel, 190 economies | Annual | The GDD's headline value is its **private+public split** — India's private-nonfinancial-sector debt/GDP alongside general-government debt/GDP in one consistent series (Mbaye/Moreno-Badia/Chae 2018 methodology, WP/18/111) — this is the free source for the "is this a public-debt problem or an economy-wide leverage problem" cross-check the fiscal-dominance state needs before over-attributing to the sovereign alone |
| **IMF Historical Public Debt Database (HPDD) vs. Public Finances in Modern History (FPP)** | HPDD: `imf.org/external/datamapper/datasets/DEBT`; FPP: `imf.org/external/datamapper/datasets/FPP` | **Two different products.** HPDD (Abbas et al., 2010, IMF WP/10/245) covers 174 countries from **1880** (G-7 + a few others) or **1920** (rest) — NOT 1800. FPP ("Public Finances in Modern History"), 151 countries, **1800–2024**, also carries primary-balance data | Annual; HPDD's recent tail links to WEO | **The task brief's "1800→" names FPP, not HPDD** — a script pulling HPDD's `DEBT` id under an "1800" assumption silently grabs the wrong, shorter-history product |
| **BIS credit to government** | `data.bis.org/topics/TOTAL_CREDIT` dashboard; India slice `data.bis.org/topics/TOTAL_CREDIT/BIS,WS_TC,2.0/Q.IN.G.A.N.770.A`; methodology `bis.org/statistics/totcredit/credgov_doc.pdf` | Government-credit series "cover on average 20 years" per BIS's own note — **[VERIFY]** India's exact start; the sibling private-sector series (A-catalog J1) starts 1951 Q2, so comparable depth is plausible | Quarterly, "adjusted for breaks" (BIS's own methodology, itself periodically revised) | A **credit-financing** concept (all lenders' claims on general government), distinct from WEO/GDD's debt-stock definition — a level cross-check, not a substitute |

**The centre-vs-general-government trap, restated globally**: WEO's `GGXWDG_NGDP` and the Status
Paper's own "General Government Debt" line are both *general-government* concepts, but IMF applies
GFSM-2014 consolidation rules while India's Status Paper applies its own netting convention (loans
to states, NSSF securities, T-bill holdings — §C.5) — a discrepancy between them is a methodology
difference to document, never a data error to "fix" by picking whichever number is convenient.

---

## C.3 India centre debt in detail — Budget documents and the Status Paper

| Source | Access path | Cadence | What it defines |
|---|---|---|---|
| **Receipt Budget, Annex "Debt Position of the Government of India"** | `indiabudget.gov.in/doc/rec/annex9.pdf` (current numbering; confirm annex number each year, it has shifted) | **Annual**, released at Budget presentation (1 Feb) | The Centre's own book-value debt position — internal debt (marketable: dated securities + T-bills; non-marketable: special securities, National Small Savings, GPF) and external debt (at historical exchange rate, per Budget convention — a genuine valuation quirk vs. the Status Paper and RBI's own external-debt report, which use current exchange rates, §C.6) |
| **Status Paper on Government Debt** | `dea.gov.in/budget-division/474` (landing page); PDF pattern `dea.gov.in/files/public_debt_management_documents/Status Paper on Government Debt for {yyyy-yy}.pdf` | **Annual**, DEA/Ministry of Finance, historically a multi-month lag (2018-19 edition released 2020-05-22, a 13-month-plus lag; recent editions shorter — confirm on first live pull) | The single most complete free document: Centre, State/UT, **and** General Government debt on one consistent definitional basis, plus — since FY2016-17 — the **Medium Term Debt Management Strategy (MTDS)**, the government's own forward-looking cost/risk target for debt composition |
| **PIB "Government Debt Status and Road Ahead"** | `dea.gov.in/files/press_release_documents/govt_debt.pdf` | Ad hoc, press-triggered | Condensed public summary of the Status Paper's own figures — a fast cross-check, not a primary source |

**The valuation quirk worth flagging explicitly**: the Receipt Budget's external-debt line is
carried at the historical (contracted) exchange rate, a Budget-accounting convention, while the
Status Paper and RBI's external-debt reports (§C.6) mark to the current exchange rate — a rupee
depreciation mechanically inflates the *current-rate* figure with no new borrowing, exactly the
valuation-vs-real-borrowing distinction the debt identity in Part D (Δb = (r−g)b − pb + sfa)
already isolates as a stock-flow adjustment (`sfa`) term, not a primary-balance one.

---

## C.4 India state debt — the RBI State Finances report

| Field | Detail |
|---|---|
| **Publication** | RBI's annual **"State Finances: A Study of Budgets"** |
| **Access path** | `rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3A+A+Study+of+Budgets` |
| **History** | First edition covered FY2004-05 budgets, published 2005 — the series has run **annually since 2005-06** (~20 editions by 2026) |
| **Cadence / lag** | Annual, typically released **December** of the following calendar year (2024-25 edition, "Fiscal Reforms by States," released ~December 2024) — a multi-quarter lag, since it consolidates all 28 states' + UTs' Budget/RE/actuals documents into one primary-disaggregated panel |
| **What it carries** | Capital receipts, composition of outstanding liabilities (SDLs, loans from Centre, NSSF, provident/reserve/contingency funds), share in central taxes, grants — **state-wise and consolidated** |
| **Latest confirmed level** | States' combined outstanding liabilities: **28.5% of GDP at end-March 2024**, down from a pandemic-era 31.0% (2021) but above pre-pandemic 25.3% (2019); CAG's decadal report separately puts FY2022-23 at **~23.0% of GSDP** — states' own denominator, not national GDP, another honest-measurement trap |
| **PIT/vintage hazard** | State-wise data comes from each state's own Budget/RE/actuals cycle on no common release date — a "same-quarter" cross-state panel necessarily mixes provisional and actual figures; the RBI report's own annual vintage is the only reconciliation point |

---

## C.5 The general-government consolidation trap — the honest measurement problem

This is the section the task brief calls out by name, and it deserves to be stated as a list of
concrete failure modes, not an abstract caveat:

1. **Centre's loans to states** are an asset on the Centre's balance sheet and a liability on the
   state's — summing "Centre debt + state debt" naively double-counts this leg. The Status Paper's
   own General Government figure nets it out; a naive WEO-vs-RBI cross-check that doesn't will
   overstate the true stock.
2. **NSSF (National Small Savings Fund)** securities: states borrow from the NSSF (a Public Account
   instrument, not a Budget/fiscal-deficit line for the Centre) and the resulting state liability
   is a Centre *asset* — the same netting requirement as #1, with an added wrinkle: NSSF's own
   on-lending to entities like the **Food Corporation of India** (to fund the food-subsidy bill)
   is a genuinely **off-budget** liability that never appears in the Centre's own fiscal-deficit
   number, because Public Account transactions sit outside the Consolidated Fund of India by
   construction — not a loophole exploited once, a standing structural feature of how the FRBM
   Act's own fiscal-deficit definition is drawn.
3. **Extra-budgetary resources (EBRs) / off-budget borrowing**, more broadly: government-guaranteed
   or PSU-issued bonds whose debt service is effectively borne by the Budget (FCI bonds for food
   subsidy, oil-marketing-company bonds historically, power-sector recapitalization bonds) sit on
   the issuing entity's balance sheet, not the sovereign's — CAG's July 2019 assessment pegged
   FY2017-18's *true* fiscal deficit at **5.85% of GDP** against the reported **3.46%**, almost
   entirely on this basis; off-budget borrowing exceeded **₹2.35 lakh crore in FY2020-21** alone.
   The **2021 Budget's reform** (bringing several EBRs onto explicit accounting from FY2020-21)
   narrowed the gap going forward but does not restate the pre-2021 series — flag the boundary as
   a **level break**, identical discipline to a GDP/CPI/WPI base-year change.
4. **PSU and quasi-sovereign SPV debt** (bank recapitalization bonds, DFI-style vehicles, state
   power-distribution-company debt under UDAY-style restructurings): not on the Status Paper's
   General Government balance sheet at all — the largest genuinely un-consolidated piece, treated
   as unmeasurable-free rather than approximated (§C.13).

**The construction rule**: treat the Status Paper's "General Government Debt" line as the primary,
already-netted figure for #1–#2 (never re-derive the netting from raw Centre+state series — that
risks a second, uncross-checked convention); treat #3 as a dated, flagged level-break; treat #4 as
outside the free-data perimeter entirely (§C.13), never silently absorbed as if included.

---

## C.6 External vs. domestic split, and who reports which quarter

| Reporting quarter | Compiler | Access path |
|---|---|---|
| **March-end, June-end** | **Reserve Bank of India** | RBI Bulletin (`rbi.org.in`, "India's External Debt" article, current issue) and RBI press releases |
| **September-end, December-end** | **Ministry of Finance (DEA)** | `dea.gov.in/files/external_debt_documents/Ex Debt Report {yyyy-yy}_Final.pdf` (the annual **"India's External Debt: A Status Report"**, published alongside the Q2/Q3 quarterly releases) |

**Why this split matters for a build script**: a naive "one source, one URL" scraper only ever
finds half the quarters — the alternating RBI/MoF compiler responsibility (long-standing, not a
recent change) means the fixture-build needs two pull routines, unified into one series downstream.
**Latest confirmed level**: external debt **US$762.8bn at end-March 2026** (RBI), external-debt/GDP
rising 19.8%→20.8% year-on-year — RBI attributed most of the rise to USD appreciation against the
rupee (a valuation effect, the `sfa` term from Part D's identity, not new borrowing).

The **domestic** leg is, by construction, everything in §C.3/§C.4 minus this external stock — no
separate series needs sourcing; it is the residual once external debt is subtracted.

---

## C.7 Maturity and ownership profile — the captivity metrics L15 needs

**Source**: the **Quarterly Report on Public Debt Management**, published by the **Public Debt
Management Cell (PDMC)** — formerly the "Middle Office," housed physically at RBI but organizationally
part of the Budget Division, **Department of Economic Affairs, Ministry of Finance** — not an RBI
publication in its own right, despite common attribution. Access path: `dea.gov.in/public-debt-
management-documents` (filename pattern `Quarterly Report on Public Debt Management for the
quarter {Month-Month yyyy}.pdf`); also press-released via PIB. **History**: running **since Q1
(April-June) FY2010-11** — 60+ editions by 2026. **Cadence/lag**: quarterly, released with an
approximate 8–10 week lag after quarter-end (exact figure **[VERIFY]**).

**What it carries, and why it is exactly the L15 Tier-C captivity input**: each edition tabulates
the **ownership pattern of outstanding dated government securities** by holder category — banks,
insurers, provident/pension funds, mutual funds, RBI, FPIs. This is the direct, quarterly, free
measurement of Reinhart-Sbrancia "liquidation rate" captivity (Part D §D2): how much of the
government's own debt is held by entities captive — bound by regulation, not free choice — to it.

| Holder | Approx. share of outstanding dated G-secs | Captivity mechanism | Vintage |
|---|---|---|---|
| Commercial banks | **~38–39%** | SLR (§C.8) — statutory minimum holding requirement, the explicit repression-apparatus rule this seat's whole India-specific rationale rests on | end-June 2020: 39.0%; end-Sep 2022: 38.3% — broadly stable in this band across recent editions |
| Insurance companies | **~26%** | IRDAI Investment Regulations — life insurers must hold **≥25%** of controlled fund assets in government/approved securities (with a further ≥25% tier in gov't-or-approved securities); general insurers ≥20% (+10% further tier); reinsurers ≥20% (+10%) — a second, independent, explicit captive-holding rule | end-June 2020: 26.2% |
| RBI (own holdings, via OMO/secondary-market operations) | **~14%**, declining | Not a captivity rule in the SLR/IRDAI sense — RBI's own balance-sheet choice, but relevant to the "who absorbs supply" story and to COFER/gold-leg balance-sheet context (§C.9) | end-March 2023: 14.3%; end-June 2023: 13.8% |
| FPIs | **~3.3%** | RBI investment-limit caps (General Route + Fully Accessible Route) — **not** a captivity floor but a captivity *ceiling*, capping foreign ownership rather than mandating domestic ownership | May 2026: 3.34% of stock (₹3.75 lakh cr of ₹112.42 lakh cr); FY2025-26 limit ~6%, utilization ~22% as of April 2025 — **[VERIFY]**, moves fast on flow data |
| Provident/pension funds, mutual funds, others | Residual | EPFO/pension mandates carry their own minimum-G-sec rules (a further captivity leg, not separately quantified — **[VERIFY]** exact EPFO mandate %) | — |

**The composite captivity score for L15 Tier C** (Part E STEP 3): construct as banks' SLR-bound
share + insurers' IRDAI-bound share, tracked as a **trajectory**, not a level — the design already
frames this as "SLR trajectory" because *direction* matters more than level: a rising captive share
under negative real rates is the Reinhart-Sbrancia liquidation mechanism re-arming; a falling
captive share (SLR itself has fallen, §C.8) with FPI-driven yields is a less-repressed regime. This
is why the input is Tier C, clamped, reduce-only (Contract §4): the level is observable with
confidence every quarter, but fewer than four full SLR tightening/loosening cycles exist post-1991
to fit any stronger claim to.

**Maturity profile**: the same report also carries new-issuance weighted-average maturity and the
outstanding stock's maturity-bucket distribution — a free, complementary pull from the same document.

---

## C.8 The repression apparatus — SLR and CRR history

| Instrument | Statutory basis | 1990-91 peak | Deregulation path | 2026 level |
|---|---|---|---|---|
| **SLR** (Statutory Liquidity Ratio) | Banking Regulation Act 1949, §24 | **38.5%** | Reduced to the then-statutory floor of 25% by **1997** (post-Narasimham Committee I, 1991); the **Banking Regulation (Amendment) Act, 2007** removed the 25% statutory floor entirely, giving RBI full discretion to set SLR anywhere up to a 40% ceiling; subsequently reduced well below the old floor over the 2010s–2020s | **18.00%** [VERIFY current figure against RBI's live circular — search-corroborated for 2026 but not independently fetched] |
| **CRR** (Cash Reserve Ratio) | RBI Act 1934, §42(1) | **15%** | The **RBI (Amendment) Act, 2006** (effective 2006-06-22) removed both the 3% floor and the 20% ceiling on CRR, giving RBI unrestricted discretion; automatic ad-hoc Treasury Bill monetization of the fiscal deficit — the practice CRR had originally been calibrated to offset — was itself abandoned in **1994** | **3.00%** [VERIFY current figure, same caveat] |

**Why both instruments moved together, historically**: pre-1991, RBI automatically monetized the
Centre's fiscal deficit via ad-hoc Treasury Bills, and the high CRR+SLR combination existed
specifically to **offset** that monetary expansion — "only 35% of the increment in bank deposits
was actually available for commercial [private-sector] advances" under the pre-reform regime, per
the standard account. This is the cleanest illustration in the whole India dataset of Part D's
repression mechanism as **standing, legislated infrastructure** rather than an emergency measure —
SLR is not a metaphor for repression here, it is repression's statutory instrument, with a fully
dated three-decade unwind trajectory (38.5% → 25% → today's much lower figure) that is itself the
India-specific input DB1 (Part F) calls for.

**Interest-rate deregulation milestones** (the companion series to SLR/CRR — when the "captive
buyer, administered price" system gave way to a market-determined one):

| Date | Event |
|---|---|
| 1989 | Ceiling on (non-SLR) interest rates withdrawn; Certificates of Deposit introduced |
| 1990 | Commercial Paper introduced — money-market instruments begin pricing off market rates |
| 1991 (Nov) | Narasimham Committee I report — the founding document of the deregulation program |
| 1994 (Oct) | RBI abolishes the minimum lending rate; banks set their own Prime Lending Rate |
| 1991–2002 | Lending rate declines from ~19.0% (1991-92) to ~10.5–11.0% (2001-02) as the system re-prices |
| 2000 | Liquidity Adjustment Facility (LAF) framework established (interim LAF from April 1999), repo/reverse-repo become the operative signaling rates |
| 2016 | Monetary Policy Committee (MPC) era begins — repo formally the sole policy rate, price-stability-mandated |

**The pre-1991 honesty note — real "market" rates are structurally unobservable, and the gauge
must say so, not paper over it.** Before the 1989–94 deregulation sequence, deposit and lending
rates were RBI-administered, not market-clearing — a computed "real rate" for this period (nominal
administered rate minus inflation) measures the *gap the administered price left unarbitraged*,
not a market-clearing signal the way the post-2000 repo-CPI construction is. The design's own
repression gauge (Part E STEP 2: repo − CPI, rolling share of trailing 36m negative) is **only
meaningfully comparable to itself post-2000** — a pre-1991 reading is a different, cruder object
(closer to JST's own repression-era readings, DS2's 1945-80 44% negative-real-rate share, than to
a genuine market signal), and DB1 (Part F) must carry this caveat inline every time it is shown.

**Capital-control indicator — the Chinn-Ito (KAOPEN) index.**

| Field | Detail |
|---|---|
| Source | Chinn & Ito (2006), maintained at `web.pdx.edu/~ito/Chinn-Ito_website.htm` |
| Construction | Principal-components index built from the IMF's own **Annual Report on Exchange Arrangements and Exchange Restrictions (AREAER)** binary capital-control indicator tabulation |
| Coverage | 1970–2022 (latest confirmed update, per the "2022 Update," described in Ito & Chinn 2025), ~181–182 countries, India included |
| Cadence | **Annual, but released with a ~2–3 year lag** — the "2022 Update" itself was published May 2025; treat any KAOPEN value for the most recent 2–3 years as not-yet-available, not zero/missing-by-error |
| Format | Free Excel/Stata download, no login |
| India relevance | A single free, standardized, cross-country-comparable annual score for how open India's capital account is at any point since 1970 — the natural companion to the SLR/CRR domestic-repression series, since capital controls and domestic captive-holding rules are the two legs of the same repression apparatus (a captive domestic buyer is a much weaker tool if capital is free to flee to a better-yielding foreign asset instead) |

---

## C.9 The real-rate gauge — building one continuous series from three different rate regimes

**Policy-rate splice rule** (India leg):

| Regime | Rate | Window | Free source |
|---|---|---|---|
| Longest series | **Call money rate** (overnight uncollateralized interbank rate) | Available at least from the early 1970s (CRR was as low as 3% and SLR 25% in the early 1970s per historical accounts, implying an active call market already) | RBI Handbook of Statistics on the Indian Economy (annual, stable, small file — A-catalog G3); DBIE for the queryable modern tail |
| Pre-LAF signaling rate | **Bank Rate** | From **1935-07-04** (RBI's first-ever announced Bank Rate, 3.5%) through the 1990s | Same Handbook — the single cleanest long, clean, rate-change-dated table in the whole catalog (A-catalog G3) |
| Modern operative rate | **Repo rate** (LAF framework) | From **2000** (interim LAF from April 1999, full LAF 2000); MSF added 2011; MPC-era repo-centric framework from **2016** | DBIE current-rate tables; Handbook for the historical rate-change-date ledger |

**The splice rule, stated precisely**: use Bank Rate pre-2000 (or call money where a purer
market-clearing series is wanted, accepting its own pre-1991-94 administered-era caveat), repo
2000-onward, with the **regime label itself carried as a column** (`rate_regime ∈
{bank_rate_administered, call_money, repo_laf, repo_mpc}`) rather than silently concatenating
levels — the identical discipline A-catalog G3 already flags for this exact series.

**CPI splice — the input side of the real-rate calculation:**

| Series | Base | Window | Source |
|---|---|---|---|
| CPI-IW (Industrial Workers) | 1949→1960→1982→2001→**2016** (current, effective Sept 2020) | Longest continuously-revised retail-price series, Labour Bureau | `labourbureau.gov.in/CPI` |
| CPI-Combined (Rural+Urban) | **2011=100** | The MOSPI headline "CPI" since 2011, the standard real-rate deflator input (A-catalog H1) | `esankhyiki.mospi.gov.in`, `cpi.mospi.gov.in` |
| CPI-Combined, new series | **2024=100**, COICOP 2018 classification | Released starting **2026-02-12**, replacing the 2011 base, driven by the 2023-24 Household Consumption Expenditure Survey's updated weights | Same portals, new series tagged distinctly |

**The construction rule (already the catalog's own rule, restated for this seat specifically)**:
any real-rate series spanning **2026-02** must decide, per historical date, which CPI base is in
force, and splice across the break rather than concatenate — precisely Part E's own named
"FAILURE MODE: CPI regime break (2026 rebase splice)". Pre-2011, CPI-IW is the only continuously-
available retail index; a genuinely long real-rate series for India therefore itself needs an
**internal CPI-IW→CPI-Combined splice** around 2011-12, a second, nested splice problem beneath
the 2026 one.

**US leg**: **DFII10** (10-year TIPS real yield, FRED, `fred.stlouisfed.org/series/DFII10`) from
**2003-01-02** — already on the principal-machine runsheet as J7 (A-catalog). **Pre-TIPS proxy**:
TIPS only began issuance in 1997, and FRED's constant-maturity series starts 2003; for the
1970s-1990s window, Part D's DS1-DS4 panel already covers the need at JST-panel level (nominal
short rate minus realized CPI, the same "ex-post real rate" JST itself uses) rather than requiring
a separate US proxy — **no clean pre-2003 US market-priced real rate exists free**; FRED's own
`REAINTRATREARAT10Y` is *model-implied* (nominal 10Y minus a survey/model inflation estimate, not
a traded instrument) and must be labeled as such, never given DFII10's market-price confidence.

---

## C.10 The gold leg

| Series | Access | History | Cadence/lag | Note |
|---|---|---|---|---|
| RBI gold reserves (tonnage) | Weekly Statistical Supplement, `rbi.org.in/scripts/WSSView.aspx` (weekly, Friday) + monthly Bulletin gold/forex table (A-catalog G6) | WSS format exists since the 1950s (evolving); tonnage reporting began with liberalization-era reserve accumulation | Weekly | RBI shifted revaluation from **monthly to weekly**, a documented methodology note — value changes can reflect this, not only price/quantity moves; a **2026-05 press controversy** inferred a tonnage drawdown from WSS-derived analysis that RBI's own statements denied, illustrating why tonnage must be read from the primary series, not inferred from valuation deltas — confirmed level **~880.5 tonnes, Q2 2026** [VERIFY, single-cluster of sources] |
| WGC central-bank purchases | `gold.org/goldhub/research/gold-demand-trends` (quarterly report + central-banks cut); country holdings `gold.org/goldhub/data/gold-reserves-by-country` (built from IMF IFS) | Multi-year quarterly + full-year back-catalog | Quarterly, **~4–5 weeks after quarter-end** (Q1 2026: 2026-04-29; Q2 2026: 2026-07-30) | Free registration required for data-explorer/download tables; PDF reports unambiguously open (A-catalog K1) |
| COFER (USD reserve share) | `data.imf.org/en/datasets/IMF.STA:COFER` | 1999 Q1+ | Quarterly, ~1-quarter lag | **2025 Q3 break**: "unallocated reserves" bucket eliminated, revised back to 2000 Q1 — use the revised series only (A-catalog J4) |
| Gold price, USD | FRED `GOLDPMGBD228NLBM` (LBMA PM fix mirror) | **1968-04+**, daily | T+1 | Sidesteps LBMA's paid-licence wall entirely (A-catalog K2) |
| USD/INR | RBI reference-rate archive, `rbi.org.in/scripts/referenceratearchive.aspx` | **[VERIFY]** exact start; daily for many years | Daily, same-day | A-catalog G10 |
| **INR gold, constructed** | USD gold × USD/INR — never a single pre-built INR series | Full history from 1968-04, limited by the USD/INR archive's own start | Daily | Decomposition is a frozen design rule (A-catalog K); **2013 duty hikes and the 2024-07-23 duty cut are LEVEL BREAKS, never fit through** |
| IBJA domestic gold rate | `ibjarates.com` (AM/PM benchmark, national reference for SGB-era issue pricing) | Multi-year daily archive | Daily, twice (AM/PM) | Domestic cross-check against the constructed USD×FX series — a persistent gap flags a duty/premium regime shift, not a data error |

---

## C.11 Vintage/PIT hazard table — what gets stored, what gets spliced

| Series | Revision-prone? | Two dates never to conflate | Store first-print or every vintage? |
|---|---|---|---|
| IMF WEO (debt/GDP) | **Yes, materially** — GDP rebases (Nigeria's 2019 rebase raised GDP levels 40.8%; India's 2026 rebase, below) flow straight through the denominator | WEO edition date (Apr/Oct) vs. reference year | **Every vintage**, never overwrite (A-catalog J2) |
| India GDP (MOSPI National Accounts) | **Yes** — base-2022-23 series (replacing base-2011-12) released **2026-02-27**; FY26 nominal GDP revised **down ~3.3%** even as real growth was revised up to 7.6% — a textbook denominator shrink worsening every debt/GDP ratio with no new borrowing | Release/vintage date vs. reference fiscal year; provisional→first-revised→final, ~2-year cycle | Every vintage (A-catalog H4) |
| India CPI-Combined | **Yes** — base-2024/COICOP-2018 series from **2026-02-12** | Release date vs. reference month | Both bases kept distinct (A-catalog H1) |
| CAG/RBI debt-to-GDP, different denominators | Not a revision, but functionally identical in effect: a debt/GSDP figure (CAG) and a debt/GDP figure (RBI) reading "23%" and "28.5%" are not comparable without checking the denominator | Denominator identity (GDP vs. GSDP-sum, centre vs. general government) | Tag every stored ratio with its exact numerator+denominator definition |
| Fiscal year vs. calendar year | Structural mismatch, not a revision. India's FY runs **April–March**; WEO/BIS report **calendar-year**, sometimes footnoted, sometimes silently relabeled | FY-ending label ("2024" = FY2023-24, ending March) vs. calendar-year label (2024 = Jan-Dec) | Carry the exact period-end date, never a bare year, in any cross-country panel |
| Centre-vs-general-government reporting lag | Structural | Centre debt (Budget, same-day) vs. general government (Status Paper, months-later; State Finances, ~9-month-plus lag) | Use Centre debt as a flagged fast proxy, never presented as the general-government figure |
| Off-budget/EBR accounting-treatment change | A one-time, dated **regime break** | Pre-2021 (EBRs excluded from headline deficit) vs. post-2021 (several brought onto explicit accounting) | Flag the 2021 boundary on any fiscal-deficit series crossing it |
| COFER USD share | Yes, one dated break | Pre-/post-2025 Q3 ("unallocated reserves" elimination, revised to 2000 Q1) | Revised series only, post-break (A-catalog J4) |
| SLR/CRR level | Not revision-prone — each change is a dated regulatory event | RBI notification effective date vs. any later news-report date | Append-only event log, dated by RBI's effective date |

---

## C.12 The quarterly pipeline — from raw pulls to the three L15 inputs

Matching Part E's algorithm (STEP 1–5) exactly; grids and masks named where the design already
fixes them.

1. **Registry load.** Validate `config/ladder.yaml L15_long_wave_fiscal` against
   `config/validator.py` before any pull — same gate every other seat's pipeline uses.
2. **Pull raw fixtures** into `data/fixtures/P_debt_fiscal/{weo,fiscal_monitor,gdd,fpp,bis_credit_gov,
   status_paper,receipt_budget,state_finances,pdmr_quarterly,ext_debt}/{vintage}/...` — a genuinely
   new fixture family this Part surfaces (no existing `ingest/pull_*.py` script covers any centre/
   state debt-stock or PDMC-report source; see closing note). Manifest immediately
   (`python ingest/manifest.py data/`), every file keyed `(series_id, vintage_date, pull_date)`.
3. **STEP 1 build — debt level & slope.** Take the Status Paper's General Government Debt/GDP
   series (§C.1/§C.3/§C.4) as the primary India input, WEO's `GGXWDG_NGDP` (every vintage, §C.2)
   as the pooled-JST-percentile cross-country comparable; compute the **expanding percentile**
   against India's own history (spliced across FY-vs-calendar-year and rebase breaks, §C.11) and
   the **5-year slope sign**; between annual Status Paper vintages, roll forward on the Centre-only
   Budget series (§C.3) as a flagged fast proxy, reconciled at each new Status Paper release.
   Warm-up mask: no percentile emitted until the sample clears the Contract's ≥4-observation floor.
4. **STEP 2 build — real-rate persistence.** Splice the policy-rate series (§C.9: Bank Rate
   pre-2000 / repo 2000+, regime-labeled) against the CPI splice (CPI-IW pre-2011-12, CPI-Combined
   2011-base to 2026-02, 2024-base thereafter); compute the rolling trailing-36-month share of
   negative-real-rate months (matching DS2's construction so India is comparable to the pooled
   44%/76% eras); pair with US DFII10 (2003+, FRED) as the global leg, honest gap flagged pre-2003.
   Pre-1991 India readings carry the administered-rate caveat inline, every time (§C.8).
5. **STEP 3 build — captivity/composition (Tier C, clamped).** Pull the PDMC's ownership-pattern
   table (§C.7) each quarter; construct the composite captive-share trajectory (banks' SLR-bound +
   insurers' IRDAI-bound share, as a slope); pull SLR's own rate-change history (§C.8) as the
   regulatory-intent leg; pull WGC central-bank-purchase data (K1) and RBI's WSS gold tonnage
   (§C.10) for the CB-buying sub-input; pull COFER's post-2025Q3 USD share for reserve-
   diversification. Enrich, reduce-only, never add — the Contract's Tier-C rule.
6. **STEP 4 — state.** Fiscal-dominance dummy = (debt percentile high) AND (repression gauge ON);
   log as a phase object (level, velocity, quadrant, age-in-quadrant) per the 2026-09-01
   states-as-phase-objects decision, not a scalar.
7. **STEP 5 — expression.** Feed the gold-floor attribution and tail-budget bands (Part D §D4);
   no code here, purely a consumer of the three constructed inputs above.
8. **Manifest every derived fixture** (debt-percentile, real-rate-gauge, captivity-composite
   panels) as its own versioned, checksummed artifact — corrections append a new vintage row,
   never overwrite.
9. **Recalibration triggers**: a new WEO vintage (April/October); a new Status Paper or State
   Finances edition; a new PDMC quarterly report; a GDP/CPI base-year rebase (2026's is the first
   live test); SLR/CRR changes (event-based); annual DS1-DS4 refresh per Part F's DB3 tracker.
10. **Monitor**: quarterly refresh with the Ilmanen dashboard; annual review re-reads DS1-DS4 with
    one more year of data; the 2030 design review re-reads the whole seat — unchanged from Part E.

---

## C.13 What cannot be measured free — the honest list

| Need | Why it's out of reach free | What we do instead |
|---|---|---|
| **True consolidated public-sector balance sheet** (Centre + states + all PSUs + bank recap bonds + DFI-style vehicles) | No free document consolidates general government with the PSU/quasi-sovereign perimeter mark-to-market; CAG audits individual PSUs, not a consolidated whole | Use the Status Paper's General Government figure as the measured floor; name the PSU/recap-bond gap wherever the fiscal-dominance state is discussed |
| **Contingent liabilities** (state guarantees to discoms, Centre guarantees to PSUs/NBFCs, UDAY-style takeovers) | Disclosed at issuance/invocation in Budget/CAG documents, but no free, structured, continuously-updated *stock* of outstanding exposure exists | A known-unknown in the Stage-2 narrative layer (Part F's red team), never a Stage-1 quantitative input |
| **Real-time state-government borrowing intent** | States announce SDL auction calendars a short window ahead; forward borrowing intent beyond that is not published in structured form | RBI/CCIL auction calendars as the nearest proxy; medium-term shifts observable only after the fact, via the next State Finances report |
| **A pre-1991 India real-market-rate series with genuine confidence** | The administered-rate regime makes any computed "real rate" a measure of unarbitraged gap, not a market-clearing signal (§C.8) | Present with the caveat inline every time, never silently spliced onto the post-2000 gauge as if continuous |
| **A single IMF-vs-Status-Paper-reconciled "general government debt" definition** | GFSM-2014 and India's own consolidation rule are independently-built; no published bridge document was found this pass | Report both figures side by side when they diverge, flagged by source |

---

*End of Part C. Cross-references: `research/CONTRACT.md` §3 (free-source mandate), §4 (evidence
tiers, Tier-C reduce-only), §7 Known Prior #11 (no live network access this environment;
principal's-machine ingestion); `research/cycles/debt-deep/partDEFH-math-algo-harvest-ledger.md`
(Parts D/E/F/H — the math, algorithm, harvest map and knowledge ledger this Part supplies data
for); `research/cycles/debt-deep/jst-debt-RESULTS.md` (DS1–DS4, the pooled priors); `docs/
masterplan/A-data-catalog.md` blocks G/H/J/K (RBI/MOSPI/IMF-BIS-FRED/gold — extended, not
duplicated, by this Part); `research/cycles/value-deep/partC-data.md` (the sibling Part this
file's structure and PIT/vintage discipline follow); `research/OPEN_QUESTIONS.md` (2026-09-01
external-mirror authorization; 2026-09-01 states-as-phase-objects decision, applied in §C.12
step 6).*
