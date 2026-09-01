# Part C — Data engineering: building the Indian credit series

v1.0 · 2026-09-01 · Extends `docs/masterplan/A-data-catalog.md` §2 blocks G (RBI), I (CCIL/FBIL),
J (BIS/IMF/World Bank) — that appendix is the source of truth for access paths, priorities, and
the fixture-governance rules (WORM manifest, vintage tagging); this part goes one level deeper on
the four L10 inputs specifically: exact table/series names, splice and interpolation conventions
named and pre-registered, and the construction-grade detail a build script needs that a source
catalog does not carry. Consumes: `config/ladder.yaml L10_credit_block`. Feeds: Part D's
`hamilton_filter` and `expanding_percentile` (the math), Part E's STEP 1–3 pipeline (the code) —
this part is the specification those steps implement. Everything below was checked this pass by
web search (snippet-level only, per Contract prior #11 — no live fetch, no file in hand); anything
not independently confirmed carries `[VERIFY]`.

---

## C.1 Bank credit — the exact RBI/DBIE series

The base layer is a single legal instrument wearing several publication names. **Section 42(2) of
the RBI Act, 1934** obliges every scheduled bank to file a fortnightly return — the **"Form A"
return, Statement of Fortnightly Position"** — reporting its demand-and-time liabilities and cash
reserves as at the close of business on alternate Fridays, within seven days. The **RBI Scheduled
Banks' Regulations, 1951** (in force 1951-11-01) is the operative regulatory instrument that
formalized the return's content; this is almost certainly the source of the "~1951" date the task
brief carries, but it dates the *regulation*, not the earliest *published, DBIE-queryable* time
series — those two dates are not the same and should never be conflated in a fixture header.

Four public products are cut from this one filing stream, at different granularities and lags:

| Product | Exact name (as published) | Source / path | First available | Frequency | Pub. lag |
|---|---|---|---|---|---|
| Fast vintage | Weekly Statistical Supplement — "Scheduled Commercial Banks' Business in India" (aggregate credit, deposits, C-D ratio, cash-reserve ratio) | `rbi.org.in/Scripts/BS_ViewWss.aspx` (WSS, weekly, every Friday); mirrored in DBIE | format exists since the 1950s (evolved); the specific aggregate-credit/deposit table is a stable multi-decade cut | weekly (last reported fortnight) | same week |
| Growth headline | "Non-food credit" / "Bank credit" growth, y-o-y and outstanding | DBIE → Financial Sector → Money & Banking; also RBI press release "Sectoral Deployment of Bank Credit" (same filing feeds both) | modern standardized monthly series ~1998+; older annual data further back [VERIFY exact pre-1998 vintage] | monthly | ~3 weeks post month-end |
| Granular annual | **Basic Statistical Return (BSR)-1** — "Credit by Scheduled Commercial Banks (including RRBs)"; **BSR-2** — "Deposits with Scheduled Commercial Banks"; BSR-3 — branch-level statistics | `rbi.org.in/Scripts/AnnualPublications.aspx?head=Basic+Statistical+Return...` | **BSRs introduced 1972** (standardised bank-level/account-level data collection) | historically annual (as-of end-March); **RBI has since moved BSR-1 data collection to a quarterly cadence internally, with the public release still framed as an annual as-of-March publication** [VERIFY exact public cadence — a 2026 RBI social post still labels the release "BSR-1 ... March 2026", i.e. annual-labeled] | published well after fiscal year-end; treat as a lagged annual anchor, not a monthly input |
| Aggregate cross-check | "Quarterly Statistics on Deposits and Credit of Scheduled Commercial Banks" (QSDC) | `rbi.org.in/Scripts/QuarterlyPublications.aspx?head=Quarterly+Statistics+on+Deposits+and+Credit...` | long-running quarterly publication | quarterly | ~1 quarter |

**Portal note (task-flagged item — DBIE after the 2024–25 revamp).** The domain moved from
`dbie.rbi.org.in` / `cimsdbie.rbi.org.in` to **`data.rbi.org.in/DBIE/`**, effective close of
business **2024-06-21** (old domains redirect; do not rely on the redirect indefinitely — hardcode
the new domain in any scraper). The underlying data-warehouse rebuild is the **Centralised
Information Management System (CIMS)**, which went live in **June 2023** and is described by RBI
as the "next generation" of its data-warehousing infrastructure — CIMS is the back-end name, the
portal keeps the DBIE brand. RBI also shipped a first-party **"RBIDATA" mobile app (Feb 2025,
11,000+ series)** as a confirmed alternative export channel if the web query-builder proves
brittle to script. **[VERIFY]** whether any individual credit series was re-defined (not merely
re-hosted) as part of the CIMS migration — the domain change itself is confirmed, a
series-definition change is not.

**Sectoral deployment — start date and the real break.** The monthly "Sectoral Deployment of Bank
Credit" release (standalone page `rbi.org.in/Scripts/Data_Sectoral_Deployment.aspx`, also a
recurring RBI press release and Economic Survey Statistical Appendix Table 32, "Deployment of
Gross Bank Credit by Major Sectors") is standardized-monthly from roughly **1998+**. The genuine
measurement break in this series is **January 2019**, when RBI revised the sectoral-deployment
reporting format — sub-sector definitions (including how NBFC lending is bucketed within
Services) changed at that point; any pre-/post-Jan-2019 comparison of a sub-line needs the same
splice discipline as a GDP base-year change. **The November 2023 risk-weight circular is explicitly
not this kind of break** — see C.5.

## C.2 NBFC + shadow credit

Bank-only credit is blind to the exact channel that froze in 2018 (IL&FS) — the design's own
chronology names this ("invisible in bank-only credit → the bank+NBFC aggregate rule",
`docs/cycles/01-credit-cycle.md` §3). Two free sources cover the shadow layer, at much lower
frequency than bank credit:

| Source | Exact product | Frequency | Lag | Note |
|---|---|---|---|---|
| RBI Financial Stability Report | NBFC chapter — sector-wide consolidated balance sheet, GNPA, capital-adequacy of the NBFC sector, stress-test results | biannual (June, December editions) | publication is the data (no interim); ~edition date only | **[VERIFY exact chapter number/title per edition]** — content confirmed (search finds recurring NBFC balance-sheet commentary in the June 2026, June 2024, June 2019 editions), a stable chapter numbering across editions was not independently pinned down this pass |
| RBI Bulletin — recurring NBFC statistical tables | "Consolidated Balance Sheet of NBFCs", "Deposits Mobilised by NBFC Sector", "Selected Financial Parameters of Non-Deposit-Taking Systemically Important NBFCs (NBFCs-ND-SI)" | typically an annual/semi-annual Bulletin article citing quarter-end data | ~1–2 quarters | Same underlying regulatory return (NBFC supervisory returns), narrated rather than published as a clean flat file — hand-transcription, same discipline as GNPA (C.6) |
| CCIL / F-TRAC | Commercial Paper and Certificate of Deposit primary + secondary market data (F-TRAC is CCIL's RBI-designated Trade Repository for CP/CD/corporate-bond-repo reporting; members must report within 15 minutes of trade) | market-watch pages appear to render publicly at `ftrac.co.in` (e.g. `CP_SEC_MEM_MARK_WATC_VIEW.aspx`, `CD_SEC_MEM_MARK_WATC_VIEW.aspx`) | near-real-time on the page; bulk historical download **[VERIFY — login wall not confirmed either way this pass]** | NBFCs are the dominant CP issuer, so CP-issuance volume is the fastest available proxy for shadow-credit funding stress (2018 IL&FS showed up here first, in spreads, weeks before any FSR NBFC chapter recognized it) |
| RBI WSS (fallback) | "Money Market Operations" — weighted-average CP/CD rates | weekly (Friday) | same week | Coarser than F-TRAC (rate only, not volume) but unambiguously free and stable; the fallback if F-TRAC access proves gated |

**Building the bank+NBFC aggregate the design requires, and the approximation error that
remains.** The construction is `credit_total = credit_bank + credit_nbfc`, but the two legs are
neither same-frequency nor independent:

1. **Frequency mismatch.** Bank credit is monthly (~3-week lag); NBFC credit is FSR-anchored
   (biannual, June/December, itself lagging its reference date by weeks). The combined series can
   only be as fresh as its NBFC leg unless NBFC credit is upsampled — see the interpolation
   convention in C.10 (piecewise-linear in log-level between successive NBFC reference dates, with
   a staleness mask once a new FSR edition is overdue).
2. **Double-counting risk.** Bank credit *to NBFCs* already appears inside `credit_bank` (as a
   named sub-line of Sectoral Deployment, "NBFCs" under Services — see C.5). If `credit_nbfc` is
   read as NBFCs' *total* balance-sheet credit outstanding (which is itself partly funded by bank
   borrowing), naively summing double-counts the bank-to-NBFC leg. **The construction must net
   bank credit *to* NBFCs out of the NBFC total before summing** — i.e.
   `credit_total = credit_bank + (credit_nbfc_total − bank_credit_to_nbfcs)` — or accept the
   double-count as a *known, bounded, one-directional* upward bias and document its size
   (bank credit to NBFCs was a large and growing share of Services credit through 2021–24; leaving
   it unnetted overstates `credit_total` by roughly that sub-line's magnitude, which the sectoral
   deployment table itself reports monthly, so the correction is at hand, not a data gap).
3. **Residual approximation error after both fixes**: NBFC funding *outside* bank credit and
   market CP/CD (e.g. inter-NBFC lending, foreign borrowing, retained-earnings-funded growth) is
   not separately observable from these free sources at monthly frequency — the aggregate is a
   **lower bound update frequency, upper-bound-correctable level**, and this residual should be
   named in the module's own docstring, not silently absorbed.

## C.3 Denominators — nominal GDP

| Layer | Source | Start | Frequency | Lag |
|---|---|---|---|---|
| Annual National Accounts (back series) | MOSPI National Accounts Statistics | **1950-51** | annual | provisional → first-revised → final over ~2 years (standard NAS practice) |
| Quarterly GDP/GVA | MOSPI (CSO), press notes on `mospi.gov.in` | **introduced 30-06-1999**, with the published series starting from reference quarter **Q1 1996-97** — the task brief's "~1996-97" is the correct anchor for the *reference period*, not the *announcement date* | quarterly | ~2 months (Q4 + provisional-annual estimate released together, per the standard NAS cycle) |

**Base-year history (confirmed this pass, with exact transition dates):**

| Old base → new base | Effective from | Driver |
|---|---|---|
| 1980-81 → 1993-94 | February 1999 | post-liberalization structural change |
| 1993-94 → 1999-2000 | January 2006 | services/IT-sector weight update |
| 1999-2000 → 2004-05 | January 2010 | — |
| 2004-05 → 2011-12 | 30 January 2015 | company-financials-based value-added methodology (2015 rebasing) |
| 2011-12 → **2022-23** | **27 February 2026** | the announced ~2026 revision the task brief flags; a "Sources and Methods" methodology note was due ~August 2026 — **pull it the moment it appears; it will state MOSPI's own splicing instruction for this transition** |

**Splicing method — the two options and which the design pre-registers.** MOSPI's own historical
practice: *"for years prior to [the anchor base], estimates were compiled by adopting the splicing
method, retaining the same growth rates of aggregates as in the old series"* — i.e., MOSPI's own
back-series convention is a **growth-splice** (chain the old series' period-over-period growth
rates onto the new series' level at the overlap point), not a single ratio.

Two candidate methods for our own construction:

- **Ratio-splice at the overlap period**: compute `k = GDP_new(t0) / GDP_old(t0)` at the single
  quarter/year both vintages report, then rescale the *entire* old-vintage history by the constant
  `k`. One multiplication, transparent, auditable in one line — but assumes the old/new
  relationship is stable at exactly the one overlap point and propagates any noise in that single
  ratio across every prior decade.
- **Growth-splice (chain-linking)**: keep the old series' own period-over-period growth rates and
  re-level them so the *chained* series matches the new vintage going forward. Matches MOSPI's own
  official back-series method, so any published "back series" MOSPI itself releases can be
  ingested directly without re-deriving it — but requires the old series' growth rates at every
  period, and is more fragile to a single bad print in the old series (an error compounds forward
  through the chain rather than being contained to one ratio).

**Pre-registered choice (this design, per `Part E STEP 2`): ratio-splice at the overlap period.**
Argument: (i) it is a single, auditable scale factor per base-year transition — five transitions
in the sample, five recorded ratios, trivially inspectable in a review; (ii) MOSPI's own official
back series, when and if released for the 2026 transition, can still be ingested as a
*cross-check* against our ratio-splice, not a replacement for it — divergence between the two
methods becomes a documented data-quality flag rather than a silent discrepancy; (iii) growth-splice
requires trusting the old series' growth rates at every historical point equally, which is a
stronger assumption than trusting one ratio, given the AQR-style and CIMS-style break history this
appendix has already catalogued elsewhere in the macro block. **Departure note (Contract §1, "state
the departure explicitly"): this differs from MOSPI's own preferred method — documented, not
hidden.**

**Monthly interpolation for the monthly credit/GDP ratio.** There is no monthly GDP release, but
L10's Hamilton filter (Part D) wants a monthly denominator to match `credit_bank + credit_nbfc`'s
monthly grid. **Convention (Part E STEP 3, restated precisely here): cubic-spline interpolation on
the *log* of quarterly GDP**, producing a smooth monthly path that reproduces the exact quarterly
values at quarter-ends. This is flagged everywhere downstream as a **convention, not data** — the
interpolated months carry no new information and must never be treated as an independent
observation in any effective-sample-size count (purged CV, AUROC computation) that assumes monthly
data has monthly information content.

## C.4 CD ratio — construction and why it dodges the GDP problem

The credit-deposit ratio is cut from the *same* Section 42(2) filing stream as C.1 — no separate
collection instrument. RBI publishes it as **"Deposit and Credit Ratio of Scheduled Commercial
Banks"** in the Handbook of Statistics on the Indian Economy (a stable table across editions) and
as a queryable DBIE Banking Statistics series; recent readings are also carried directly in press
commentary (CD ratio reported at **78.1% end-March 2024 — "highest since 2005"** per RBI-sourced
press reporting, corroborating the design's own chronology note in `docs/cycles/01-credit-cycle.md`
§3 that flags 2021–24 as "CD ratio ~80%, highest since 2005").

The **monthly history back to 1969** already assumed in the L10 construction
(`docs/cycles/01-credit-cycle.md` §4: "monthly, 1969→; long-run range ~51.6%–~80%") is corroborated
this pass only indirectly — multiple RBI Handbook tables are confirmed to carry data reaching back
to 1969-70 in general, but the *exact* first published fortnight/month of the CD-ratio cut itself
was not independently pinned down. **[VERIFY]** the precise first observation on first live DBIE
contact; treat 1969 as the working assumption, not a confirmed fact, until then.

**Why this input is genuinely cleaner than the credit/GDP gap.** It needs:
- no GDP denominator (so none of C.3's base-year, splicing, or interpolation machinery applies);
- no cross-agency alignment (both numerator and denominator come from the identical fortnightly
  filing, at the identical reporting entity level);
- no revision-vintage bookkeeping beyond the ordinary bank-level revision cycle already handled by
  DBIE's own vintage support.

This is precisely why the design's own R5 test (`docs/cycles/01-credit-cycle.md` §5) asks whether
the CD ratio should become the *primary* level input and the Hamilton gap merely its cross-check,
rather than the reverse — a question this data-engineering layer cannot answer (it is an
econometric spanning test, Part D/R5's job) but can now say is at least *operationally* justified:
the CD ratio is the cheaper, more robust build of the two.

## C.5 Composition input — sectoral deployment shares

The "hot" composition signal (unsecured retail + NBFC on-lending share of incremental credit) is
read off named sub-lines of the same Sectoral Deployment release as C.1:

| Sub-series (as published) | Parent category | Note |
|---|---|---|
| "Personal Loans" → "Consumer Durables", "Credit Card Outstanding", "Other Personal Loans" | Personal Loans | credit-card sub-line is separately broken out — the fastest-turning unsecured proxy |
| "Housing (Including Priority Sector Housing)" | Personal Loans | **secured** — excluded from the "hot" composition numerator by construction |
| "Vehicle Loans", "Education" | Personal Loans | secured/quasi-secured — excluded |
| "NBFCs" | Services | the bank-to-NBFC leg also needed for the C.2 double-count correction |
| "Industry", "Agriculture and Allied Activities" | (top-level) | denominator context, not part of the hot numerator |

**Start date**: standardized monthly from ~1998+ (same filing as C.1); older annual cuts exist
further back but at coarser sector granularity — do not assume sub-line comparability before the
modern monthly series begins.

**Breaks, named precisely (task's own framing, confirmed by this pass's search):**
- **January 2019 reporting-format revision** — a genuine measurement break; sub-sector
  definitions changed (search confirms "with effect from January 2019, sectoral credit data are
  based on [a] revised format"). Splice discipline applies exactly as it does to the GDP base-year
  changes: two segments, a documented ratio at the transition, never a trend fit through it.
- **November 2023 risk-weight circular** (RBI/2023-24/85, DOR.STR.REC.57/21.06.001/2023-24,
  dated **2023-11-16**, +25pp risk weight on unsecured consumer-credit exposures of banks and NBFCs
  to 125%, compliance by 2024-02-29; explicitly excludes housing/vehicle/education/gold/microfinance
  loans) is **not a measurement break** — the series definition did not change, only the economic
  incentive to originate this credit did. Per the task's own framing this is a **marker**: the
  regulator's own policy response *confirming* the design's composition signal was reading
  something real, exactly analogous to how the design already treats the AQR (C.6) as a
  recognition event rather than a fresh deterioration. Do not splice across it; do treat its
  aftermath (credit-card growth decelerating sharply into 2024–25, per the same sectoral-deployment
  release) as an out-of-sample readout of whether the composition input actually led the
  regulator — this is exactly design R7's pre-named validation target
  (`docs/cycles/01-credit-cycle.md` §5).

## C.6 Confirm inputs — GNPA, rating-agency defaults, and the CMIE non-option

**GNPA.** RBI Financial Stability Report editions (biannual, June/December, series from ~2010) are
the primary narrative source; DBIE additionally carries a queryable asset-quality time series
(third-party compilations citing `dbie.rbi.org.in` as source show public-sector-bank GNPA data
back to 1995 [VERIFY — not independently confirmed against a primary RBI table this pass, but
consistent with the AQR-era literature's usual starting point for PSB GNPA charts]). The **2015
Asset Quality Review (AQR)** is, per the data catalog's own characterization, "the single largest,
best-documented regime break in this entire catalog": system GNPA moved from **5.0% (March 2015)
to 14.6% (March 2018)**, purely from RBI's withdrawal of forbearance on restructured-asset
recognition, not a fresh wave of borrower defaults. **Handling rule (already fixed by the design,
restated here for the data layer): treat 2015–2018 as two segments joined by a documented
recognition event, never one continuously-defined series; the module's GNPA input is a lagging
confirm-only dummy, so this break cannot leak into a leading signal by construction — but it can
still corrupt a naive descriptive chart if plotted through without annotation.**

**Rating-agency default/downgrade counts.** Both major domestic agencies publish an annual,
citable, genuinely free study:

| Agency | Exact publication | Cadence | Access | Note |
|---|---|---|---|---|
| CRISIL Ratings | **"Default and Rating Transition Study"** (e.g. "...up to fiscal 2025") | annual | direct, stable PDF URL pattern: `crisilratings.com/content/dam/crisil/our-analysis/publications/default-study/crisil-ratings-annual-default-and-ratings-transition-study-fy-{yyyy}.pdf` (confirmed for FY2020–FY2025 editions) | Methodology moved to **monthly static-pool** with the **2009 edition** (finer intra-year default/transition granularity than a simple annual static pool); FY2025 annual default rate reported at **0.7%, a 17-year low**, down from 1.30% in FY2024 — directly usable as a default-rate time series once several editions are hand-collected |
| ICRA | **"Performance of ICRA-Assigned Ratings in FY{yyyy}"** | annual | PDF exists and is free, but served via an ID-keyed download link off `icra.in/Rating/Methodology?Page=RatingPerformance` rather than a stable filename pattern — **[VERIFY]** a durable per-year URL scheme before scripting; re-discover the link each year if not | FY2025 reported **301 upgrades vs. 150 downgrades** — a rating-momentum (upgrade/downgrade ratio) series, complementary to CRISIL's default-rate series |

Both are genuinely free (no paywall, no registration observed in the fetched links), which answers
the task's own question directly: **yes**, free PDFs exist for both agencies; the construction cost
is annual hand-transcription (same discipline as GNPA and FSR — no bulk historical file exists for
either).

**CMIE — explicitly not free.** CMIE's Prowess/CMDB/Economic Outlook products (which would
otherwise be the natural source for firm-level default and distress data, and for a cross-check on
credit growth) are a **paid subscription service** and are excluded outright by Contract §3's
free-source rule. No substitute is needed for the *credit-cycle* inputs specifically — the design
already resolves the general CMIE-shaped capex-tracking gap elsewhere (RBI OBICUS + MOSPI
IIP-capital-goods + GFCF, per `docs/masterplan/A-data-catalog.md` §6) — and for defaults/downgrades
specifically, the CRISIL+ICRA free studies above are the complete substitute. This should be stated
plainly wherever a future contributor might reach for CMIE out of habit: **do not**.

## C.7 Cross-checks (external, free) — never primary

Every series in this section is bound by the same rule: **cross-check only.** The design's own
credit-to-GDP gap is Hamilton-filtered, own-construction; BIS's competing gap is explicitly banned
as a substitute (Contract §8 trap list: "Do NOT use the HP filter anywhere").

| Source | Exact product | URL pattern | History | Freq. | Lag |
|---|---|---|---|---|---|
| BIS Data Portal | Credit-to-GDP gaps (India) | `data.bis.org/topics/CREDIT_GAPS/data` (bulk CSV, no login) | gap computable wherever the underlying level series exists | quarterly | ~1 quarter |
| BIS Data Portal | Total credit to private non-financial sector (India), levels, "adjusted for breaks" | `data.bis.org/topics/TOTAL_CREDIT/data` | **Q2 1951 → present** — but **Q2 1951–Q1 1970 is BIS's own estimate using M3 as a proxy for credit**, not measured credit; only from **Q2 1970** is it a directly-observed credit aggregate | quarterly | ~1 quarter |
| IMF | Global Debt Database (GDD) | `data.imf.org/en/datasets/IMF.FAD:GDD`; datamapper mirror at `imf.org/external/datamapper/datasets/GDD` | panel dating to 1950 in principle (190-economy unbalanced panel); **exact India start year [VERIFY] — not independently confirmed this pass** | annual | at release (methodology traces to the October 2016 Fiscal Monitor) |
| World Bank | Global Financial Development Database (GFDD) — private-credit-to-GDP family (`GFDD.DI.02`, `GFDD.DI.12`), mirrored in WDI as `FS.AST.PRVT.GD.ZS` (domestic credit to private sector, %GDP) and `FD.AST.PRVT.GD.ZS` (same, banks only) | `databank.worldbank.org` / `data.worldbank.org/indicator/{code}?locations=IN` | from **1960** | annual | ~1 year; sourced from IMF IFS + national data, so it inherits every India-specific break (the 2026 GDP rebase included) with the World Bank's own additional lag on top |

**BIS methodology, confirmed and directly relevant to the ban.** BIS derives its published trend
with a **one-sided (backward-looking) Hodrick-Prescott filter, smoothing parameter λ = 400,000 on
quarterly data**. One-sided avoids the classic two-sided look-ahead problem, but Hamilton's (2018)
critique — the design's own stated reason for the ban (Part D, §D1) — targets the filter mechanism
itself (spurious cyclicality manufactured by the moving-average structure, a magic-number λ), not
merely its two-sided variant. BIS's own gap therefore remains banned as a *substitute* for the
design's own construction even in its (better-behaved) one-sided form; it is retained purely as an
independent, differently-flawed cross-check — a second opinion built on a method the design has
already rejected on its merits, which is exactly what makes divergence between the two
informative.

## C.8 Market-price complements — the fast layer

| Instrument | Exact index/series | Source | History | Freq. | Note |
|---|---|---|---|---|---|
| Bank Nifty | "Nifty Bank Index" | NSE Indices, `niftyindices.com/Factsheet/ind_nifty_bank.pdf` | base date **2000-01-01** (=1000); **launched 2003-09-15** | daily | the base-date/launch-date gap (base predates launch by ~3.7 years) is a standard NSE Indices convention, not a data anomaly — do not read the base date as the first tradeable observation |
| Broader financials | Nifty Financial Services Index | NSE Indices | **[VERIFY exact base/launch date — not confirmed this pass]** | daily | wider than Bank Nifty (includes NBFCs, insurers, housing finance) — arguably the better single-index proxy for *shadow*-credit-sensitive equity, given C.2's NBFC-visibility problem |
| Corporate bond spreads | FIMMDA "Corporate Bond Spread Matrix" / "Yield Matrix" (tenor-, rating-, industry-classification-wise) | `fimmda.org` | matrices published on the last working day of each month (post valuation-committee vetting), plus a fortnightly cut | monthly (+fortnightly) | **[VERIFY]** whether bulk historical download is open or requires member sign-in — the *current* matrix is confirmed reachable without an obvious paywall in the fetched links, historical depth was not confirmed |
| Corporate bond issuance/outstanding | SEBI corporate-bonds statistics | `sebi.gov.in/statistics/corporate-bonds.html` | **[VERIFY exact history start]** | monthly | regulator-published, complements FIMMDA's price-side cut with a volume-side cut |
| CP rates (fast, free fallback) | RBI WSS "Money Market Operations" — weighted-average CP/CD rates | `rbi.org.in/Scripts/BS_ViewWss.aspx` | multi-decade | weekly | coarser than F-TRAC (rate only) but unambiguously free; use if F-TRAC's login status resolves unfavorably |

**Framing.** These are the design's Krishnamurthy–Muir-style fast complement: bond spreads and CP
funding rates move at weekly/daily frequency and lead bank-level credit tightening by weeks to a
couple of months, exactly filling the gap between the ~3-week-lagged monthly bank-credit print and
the ~2-quarter-lagged NBFC print (C.2). They are **not** a fifth L10 input — the design's own
four-input construction (§4 of `docs/cycles/01-credit-cycle.md`) is frozen — but they are the
natural fast-stress (L2) cross-feed and the natural early-warning readout for the C.2 approximation
gap: a spread/CP-rate spike between two FSR editions is the free, weekly-frequency signal that the
NBFC leg of `credit_total` is already stale.

## C.9 Vintage / point-in-time discipline

The governing rule is already fixed at the repository level (`ingest/manifest.py`,
`ingest/README.md`): **every raw pull is checksummed into a manifest; a refresh is a new
vintage-dated file, never an in-place overwrite** (the manifest script hard-fails if a file's hash
changes under an existing entry — "content changed under an existing manifest entry ... refreshes
must land as NEW vintage-named files"). Two dates are mandatory on every row: `vintage_date` (the
date the figure was *as-of*/published) and `pull_date` (when this program fetched it) — this is
the WORM (write-once-read-many) discipline the task brief asks after.

| Series | Revision-prone? | Backfilled? | Announcement lag | Store first-print or latest? | Why |
|---|---|---|---|---|---|
| SCB fortnightly credit/deposits (C.1) | Low (bank-level filing revisions are rare and small) | No | ~3 weeks | Latest (with vintage tag) | Revision risk is minor relative to the CIMS/domain-migration risk; the real discipline need is capturing *which portal generation* served a given pull |
| Sectoral deployment (C.1/C.5) | Break-prone (Jan-2019 format change), not revision-prone | No | ~3 weeks | Latest, both format-vintages kept distinct across the Jan-2019 break | A format break is not a revision — never merge the two sides into one column |
| BSR-1/2 (C.1) | Low | No | multi-month | Latest | Small, stable, infrequent |
| Nominal GDP, quarterly + annual (C.3) | **High** — provisional → first-revised → final over ~2 years, plus five base-year regime changes across the sample | **Yes, structurally** — every base-year transition is itself a controlled backfill | ~2 months (quarterly cut) | **Every vintage, as a new row — never overwritten** | This is the textbook "GDP revisions" case the task brief names directly; a single-vintage pull silently look-ahead-biases anything using GDP as of a past date |
| CD ratio (C.4) | Low (same filing as C.1, no denominator revision channel) | No | ~2–4 weeks | Latest | Structurally the cleanest series in this appendix — the reason C.4 argues for its promotion to primary |
| NBFC credit (FSR/Bulletin, C.2) | Low print-to-print, but **structurally stale between editions** | No | edition-date only (no interim) | Latest, with an explicit `stale_after` flag once a new edition is overdue | The "revision" risk here is really a *staleness* risk, not a restatement risk — flag accordingly, don't conflate with GDP's revision problem |
| GNPA (C.6) | **Break-prone** (AQR 2015), not revision-prone in the ordinary sense | No | edition-date only | Latest, two-segment-annotated across AQR | Same discipline as sectoral deployment's Jan-2019 break — a recognition event, never smoothed through |
| CRISIL/ICRA default studies (C.6) | Methodology-revision-prone (CRISIL's 2009 move to monthly static pool) | Partially (later editions sometimes restate prior-year figures under the newer methodology) | edition-date only, annual | Latest edition's own restated figures, tagged with which methodology vintage | Same edition-based discipline as FSR — no bulk historical file exists for either agency |
| BIS credit-to-GDP gap / total credit (C.7) | Revision-prone — BIS periodically revises its own break-adjustment methodology | Yes (pre-1970 India figures are themselves an M3-based estimate, not measured credit) | ~1 quarter | Latest, with the pull's BIS-methodology-vintage noted | Cross-check only — a stale cross-check is a minor risk, but the pre-1970 M3-proxy caveat must travel with the series everywhere it is plotted |
| IMF WEO/GDD, World Bank GFDD (C.7) | Revision-prone (WEO explicitly; GDD/GFDD inherit India's own NAS revisions with a lag) | Yes | biannual (WEO)/annual (GDD, GFDD) | **Every WEO vintage kept, never only the latest** (already the data catalog's own J2 rule) | The single cleanest point-in-time macro-forecast archive available free — wasted if only the current vintage is kept |
| Market-price complements (C.8) | Low (prices are not restated) | No | T+0/T+1 | Latest (there is no "first print" distinct from the traded price) | The one category in this table with no PIT problem at all |

## C.10 Construction pipeline — ordered, script-followable

This restates and completes Part E's STEP 1–3 at data-engineering precision; steps 0–3 are this
part's responsibility, steps 4 onward hand off to Part D's math and Part E's own numbering.

1. **Registry load.** Validate `config/ladder.yaml` (must pass `config/validator.py` with 0
   errors) before any pull — the pipeline never runs against an un-validated registry.
2. **Pull, per series, into `data/raw/<org>/...`** (directory layout per
   `docs/masterplan/A-data-catalog.md` §5): SCB fortnightly credit + deposits (DBIE, monthly cut);
   sectoral deployment (DBIE/RBI press release, monthly); CD ratio (Handbook/DBIE, monthly);
   quarterly + annual nominal GDP, every base-year vintage kept distinct (MOSPI); NBFC credit (FSR
   NBFC chapter + RBI Bulletin NBFC tables, biannual, hand-transcribed); GNPA (FSR + DBIE);
   CRISIL/ICRA default studies (annual PDF, hand-transcribed); BIS/IMF/World Bank cross-checks
   (bulk CSV, every vintage for WEO). Every pull is followed immediately by
   `python ingest/manifest.py data/` — an unmanifested file does not exist for the pipeline.
3. **Splice across structural breaks, per series, before anything is merged:**
   - GDP: **ratio-splice at the single overlap period** for each of the five base-year
     transitions (1993-94→1999-2000→2004-05→2011-12→2022-23), per C.3's pre-registered choice;
     record each transition's ratio in the manifest as its own auditable constant.
   - Sectoral deployment: **two segments across January 2019** — never merge sub-line
     definitions across the format change.
   - GNPA: **two segments across the 2015 AQR** — annotate inline, never fit a trend through
     March-2015-to-March-2018.
   - COFER/WEO-style vintage series (used only in cross-checks, C.7): keep the pulled vintage
     explicit; never silently prefer "latest" when the question is "what was known as of date X."
4. **Align to a common monthly grid:**
   - `credit_bank`: native monthly, no interpolation needed.
   - `credit_nbfc`: native biannual/quarterly (FSR/Bulletin) → **piecewise-linear interpolation
     in log-level** between successive reference dates (proposed convention, extending Part E
     STEP 3 — pending registry sign-off), **with a `stale_after` mask**: once more than one
     reporting cycle has elapsed since the last NBFC print without a new one landing, months
     beyond that point are held flat and flagged `stale`, not silently interpolated forward as if
     new information existed.
   - `credit_total = credit_bank + (credit_nbfc − bank_credit_to_nbfcs)` — the C.2 double-count
     correction, netting the named "NBFCs" sub-line of sectoral deployment out of the NBFC total
     before summing.
   - Nominal GDP: **cubic-spline interpolation on log quarterly GDP** to monthly, per C.3 —
     flagged everywhere downstream as a convention, not an observation; excluded from any
     effective-sample-size count.
   - CD ratio: native monthly (or finer, collapsed to monthly by last-fortnight-of-month), no
     interpolation needed — this is the whole point of C.4's construction argument.
5. **Compute the four L10 inputs** (Part D's math, referenced here only for completeness):
   `gap_t = hamilton_filter(credit_total / gdp_monthly, h ∈ {16,20,24}q pre-registered grid, p=4,
   mode="expanding")`; `G_t = expanding_percentile(gap_t)`; `C_t = expanding_percentile(cd_ratio)`;
   `Q_t = expanding_percentile(hot_composition_share)` (unsecured personal + NBFC on-lending share
   of incremental sectoral-deployment credit, per C.5, **clamped to `min(0, reading)`** per the
   Tier-C rule); `N_t` = GNPA-trend confirm dummy (lagging only, never leading).
6. **Warm-up masks.** Every `expanding_percentile` and `expanding`-mode Hamilton filter carries a
   `min_obs` floor — early-sample readings before the reference window is long enough are masked
   `NaN`, not silently reported as if reliable; the mask boundary is itself a pre-registered
   constant (Part D §D2), not tuned after seeing results.
7. **Composite + phase.** `state_t = credit_state_composite(G_t, C_t, Q_t; weights from the
   registry's pre-registered grid)`; `phase_t = phase_state(state_t; grids from
   `state_phase_convention`)` — both per Part E STEP 6–7, unchanged by this data layer.
8. **Break-registry side effects.** Any of: a source series discontinued/renamed; the 2026 GDP
   rebase landing (dual-vintage parallel run until spliced); a sectoral-deployment redefinition —
   trips the same failure-mode handling already named in Part E ("capture-health flag, run on
   last-good + de-risk rung"; Tier-C composition zeroed to safe-default with a compensating
   one-notch hedge-floor hold, preserving the reduce-only asymmetry).
9. **Recalibration triggers.** Re-run the h-grid/weight sweep (R1, R4) annually on the grown
   sample; re-check the GDP splice ratios whenever MOSPI's own back-series documentation for the
   2022-23 base is finally published (expected ~August 2026 per its own press note; pull it,
   compare against this pipeline's independently-derived ratio-splice constants, and log any
   divergence as a data-quality flag rather than silently adopting MOSPI's number in its place).

---
*End of Part C. Cross-references: `docs/masterplan/A-data-catalog.md` §2 blocks G/I/J (access
paths, priorities, fixture governance), `docs/cycles/01-credit-cycle.md` §3–4 (the chronology and
the four-input construction this part builds data for), Part D (`partD-econometrics.md`, the math
consuming these series), Part E (`partEFH-algo-extraction-ledger.md`, the pipeline this part
specifies), `ingest/README.md` + `ingest/manifest.py` (the WORM/manifest rule), `research/
CONTRACT.md` §3 (free-source mandate), §8 (HP-filter ban).*
