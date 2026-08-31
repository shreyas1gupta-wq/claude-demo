# Appendix A — Data Engineering Catalog

Version 0.9 · 2026-08-31 · Owner: principal + Claude. Companion to `docs/DESIGN.md` (source of
truth), `config/*.yaml` (machine-readable registry), `research/dossiers/01-12`, and
`research/register/{consistency-audit,verification-log}.md` (corrections already applied —
honored throughout: futures statutory cost **5.7bps** not 7.7; SAST disclosure floor
**₹11,000–30,000cr** not ₹19,000–31,000cr; anchor-exit is **gradual** (~3.2%@30d, ~17.3%@90d,
Aug-2026 SEBI study) not a prompt sell-down; **May-2026 was an INR/FII-outflow crisis**
(Nifty ≈−4% acute/−1.9% month, VIX ~18.6), not a qualifying equity drawdown episode).

Environment note (Contract prior #11): this remote research environment has **no live market-data
network access** — NSE/RBI/FRED/Kaggle all 403 at the agent proxy; only web *search* (snippet-level)
worked, confirming URL schemes, portal names, and break dates below, never fetching or
checksumming an actual file. **Every access path in this appendix is unexecuted** — verified by
search description only, one level short of "downloaded and checksummed." The principal's machine
does the actual Phase 0 pull (§12 below); this catalog is the runbook, not proof of a completed
pull. Anything not independently confirmed by ≥1 search is tagged **[VERIFY]**.

---

## 0. How to read this appendix

- **§1** is the master index — one row per series, all columns needed to triage a pull.
- **§2** is the detail blocks, grouped by domain (A–N), one block per series (or a tight sibling
  cluster sharing one access path) with all 8 required facts: consumes / source+path /
  history-freq-lag / PIT caveats / pull method+size / fixture spec / priority / access risks.
- **§3** ties every catalog entry to the `config/*.yaml` field(s) it feeds — the traceability the
  registry's own `provenance` blocks require but cannot self-declare for raw inputs.
- **§4** is the Phase-0 runsheet — what the principal pulls on day 1, in order, with hours.
- **§5** is fixture governance (directory layout, checksums, vintage tags, refresh cadence).
- **§6** is the gap list — series the design needs with no clean free source, and the fallback.

**Priority key.** **P0** = Phase-0 blocker: either named in the task brief's own P0 list
(bhavcopy cash+F&O, index constituents/TRI, India VIX, NSDL FPI, RBI DBIE core, CCIL, AMFI) **or**
named in DESIGN §12's actual Phase-0 deliverable text ("bhavcopy, RBI DBIE, NSDL, AMFI, India-VIX,
**WGC, FRED, IMF/BIS**") — the two lists differ (DESIGN's is wider); both are honored as P0 here,
with the source noted per row. **P1** = needed by Phase 2–4 (risk system, factor book, aggressive
sleeves). **P2** = Phase 5–6 or context-only (zero allocation authority, e.g. L16 demographics).

---

## 1. Master index

| ID | Series | Consumes (config ref) | Source org | Priority | History start | Freq | Pub lag |
|---|---|---|---|---|---|---|---|
| A1 | NSE cash bhavcopy (UDiFF) | L1,L2,L3,momentum,value,low_vol,factor_book | NSE | **P0** | 1994 (old fmt); UDiFF from 2024-07 | daily | T+0 (EOD) |
| A2 | NSE F&O bhavcopy (UDiFF) | L4,L9 futures leg,leverage,tactical_short | NSE | **P0** | 2000 (old fmt); UDiFF from 2024-07 | daily | T+0 (EOD) |
| A3 | NSE delivery %/security deliverable data | momentum liquidity filter, impact model | NSE | P1 | ~1999 | daily | T+0/T+1 |
| A4 | BSE cash bhavcopy (cross-check/fallback) | A1 fallback, corp-action cross-check | BSE | P1 | 1997+ | daily | T+0 |
| A5 | India VIX historical | L2 fast_stress, L5 calendar vol-scheduling | NSE | **P0** | 2008-04 (some sources 2008-03) | daily | T+0 |
| A6 | Price-band / circuit master (embedded in bhavcopy + daily report) | tail_neglect band-lock filter, momentum liquidity_rules | NSE | P1 | ~2001 | daily | T+0 |
| A7 | ASM list (stage 1–4) | momentum/tail exclusion rule, sleeves.yaml liquidity_rules | NSE (SEBI framework) | P1 | list: current only; circulars: 2017+ | daily list, event circulars | T+0 |
| A8 | GSM list (stage 1–6) | same | NSE (SEBI framework, Mar-2017) | P1 | list: current only; circulars: 2017+ | daily list, event circulars | T+0 |
| A9 | F&O eligibility list + selection criteria | universe def for tactical_short, leverage instrument choice | NSE Clearing | P1 | current + circular history | monthly review | T+0 |
| A10 | MWPL / F&O ban list | leverage/short-sleeve execution constraint | NSE Clearing | P1 | current + archive via circulars | daily | T+0 |
| A11 | Bulk/block deals (+short-selling) | L14 FII positioning (context), special_situations bulk_block_pit_following | NSE (BSE mirror) | P1 | ~2004 (site); older via archives | daily | T+0/T+1 |
| B1 | Nifty 50 constituents+TRI | drawdown benchmark, DESIGN §10 conventions | NSE Indices | **P0** | 1996-04 (base 1995-11-03) | daily; semi-annual reconst. | T+0 (TRI same-day) |
| B2 | Nifty 500 constituents+TRI | alpha/signal benchmark (Decision Q1), moderate/conservative universe | NSE Indices | **P0** | 1996-07 (nifty 500 series) [VERIFY exact] | daily; semi-annual | T+0 |
| B3 | Nifty Total Market constituents+TRI | aggressive book stated universe (NIFTY 750) | NSE Indices | **P0** | recent launch (post-2023) [VERIFY exact] | daily; semi-annual | T+0 |
| B4 | Nifty Microcap 250 constituents+TRI | aggressive tail sleeve universe | NSE Indices | **P0** | base 2005-04-01; index launched 2023 [VERIFY launch] | daily; semi-annual | T+0 |
| B5 | Nifty200 Momentum 30 | L3 momentum cross-check/crowding monitor | NSE Indices | P1 | base 2005-04-01 | daily; semi-annual | T+0 |
| B6 | Nifty Alpha Low-Volatility 30 | low_vol crowding/AUM-growth trigger (must NOT be used as construct itself — sleeves.yaml explicit) | NSE Indices | P1 | base 2009-01-01 [VERIFY] | daily; semi-annual | T+0 |
| B7 | Nifty500 Value 50 / Nifty200 Quality 30 | value/quality crowding cross-checks | NSE Indices | P1 | recent launches [VERIFY] | daily; semi-annual | T+0 |
| B8 | NSE equity-indices methodology doc | reconstitution-pop fade rule, index-effect sleeve | NSE Indices | P1 | current version only (revised periodically) | as revised | — |
| C1 | SAST Reg. 29 disclosures (≥5% acquisition/disposal, incl. pledge-as-encumbrance) | capacity_bounds.sast_disclosure_mcap_floor_cr, universe splits | NSE/BSE (SEBI SAST) | P1 | 2015+ (Reg 29 current regime; earlier under 1997 regs) | event-based, ≤2 trading days | T+0/T+2 |
| C2 | SAST Reg. 31 event-based (promoter pledge/encumbrance) | quality sleeve pledge/RPT junk terms | NSE/BSE (SEBI SAST) | P1 | 2015+ | event-based, ≤7 working days | T+7 |
| C3 | Quarterly shareholding pattern | L14 FII float-scaled ownership percentile | NSE/BSE (SEBI LODR Reg 31) | P1 | ~2009+ | quarterly | ≤21 days post quarter-end |
| C4 | Corporate actions (splits/bonus/buyback/demerger/delisting) | price-adjustment factors (all sleeves), special_situations demergers/buybacks | NSE/BSE | P1 | 1994+ (patchy pre-2000) | event-based | T+0/T+1 announce |
| C5 | PIT (insider trading) disclosures Reg 7 SEBI PIT | special_situations bulk_block_pit_following | NSE/BSE (SEBI PIT 2015) | P2 | 2015+ | event-based | ≤2 trading days |
| D1 | DRHP/RHP + anchor allotment disclosure | special_situations lockin_expiry_windows, IPO exclusion note | SEBI (primary), Chittorgarh (structured) | P2 | SEBI filings: 1990s+ scanned, structured ~2010s+; Chittorgarh: 2004+ | per-IPO, one-time | T+0 (filing date) |
| D2 | Post-listing bhavcopy for lock-in event study | special_situations lockin_expiry_windows test | NSE (=A1 subset) | P2 | = A1 | daily | = A1 |
| D3 | Index-reconstitution announcement history | special_situations index_inclusion_exclusion decay re-estimate | NSE Indices / MSCI / FTSE | P2 | Nifty 50 semi-annual since 1996; MSCI/FTSE since inclusion | semi-annual/quarterly | 4-week prior notice |
| E1 | AMFI daily NAV (NAVAll.txt + history portal) | AMFI-flow inputs (context, no direct ladder entry named but Contract §3 lists it) | AMFI | **P0** | 2006-04 (AMFI standardized) | daily | T+0 |
| E2 | AMFI scheme-wise AUM | fund-flow context, capacity cross-checks | AMFI | **P0** | ~2000 (limited), standardized ~2012+ | monthly (avg AUM) | ~5 days post month-end |
| E3 | AMFI monthly SIP contribution data | L7 issuance/sentiment context, retail-flow regime | AMFI | **P0** | 2016-04 (standardized monthly note) | monthly | 8th–10th working day of next month |
| F1 | NSE FII/DII daily provisional cash-market activity | L2 fast_stress funding/flow-stress rank (same-day proxy) | NSE | **P0** | ~2000s [VERIFY exact] | daily | T+0 (provisional) |
| F2 | NSDL FPI monthly/fortnightly (sector-wise, AUC) | L9 global_financial_cycle, L14 FII positioning | NSDL (fpi.nsdl.co.in) | **P0** | current regime 2014-06+ (FII→FPI merger); legacy FII data pre-2014 via SEBI archive | monthly/fortnightly | ~1 week post period-end |
| G1 | RBI non-food credit + sectoral deployment | L10 credit_block | RBI DBIE | **P0** | 1970s (levels), modern monthly series ~1998+ | monthly | ~3 weeks post month-end |
| G2 | RBI credit-deposit (CD) ratio | L10 credit_block | RBI DBIE (BSR/Section 42 return) | **P0** | 1970s+ | fortnightly/monthly | ~2–4 weeks |
| G3 | RBI policy rates (repo/MSF/CRR/SLR) history | L6 monetary_stance, leverage funding_hurdle context | RBI (Handbook of Statistics + DBIE) | **P0** | 1935 (Bank Rate); repo modern regime 2000+ | event-based (rate-change dates) | T+0 (announcement) |
| G4 | RBI House Price Index (HPI) | L12 realestate_medium_cycle | RBI DBIE | P1 | 2010 (old base 2010-11); new base 2022-23 from Q2 FY2025-26 release | quarterly | ~10–12 weeks post quarter-end |
| G5 | RBI M3 (broad money) | L10/context, M3 in Contract's free-source list | RBI DBIE / WSS | P1 | 1970s+ | weekly (WSS)/monthly | 1 week (WSS Friday) |
| G6 | RBI Weekly Statistical Supplement (incl. gold+forex reserves) | L15 long_wave_fiscal reserve-diversification input | RBI | **P0** | 1950s (format evolved) | weekly (every Friday) | T+0 |
| G7 | RBI REER/NEER (36-currency, now 40-currency) | L15 long_wave_fiscal, L9 context | RBI DBIE / RBI Bulletin | P1 | 2004-05 base (36-ccy); 2015-16 base (40-ccy) from ~2020 | monthly | ~1 month |
| G8 | RBI Financial Stability Report (GNPA, BSI) | L10 credit_block lagging confirm | RBI | **P0** | 2010 (FSR series began); GNPA regime break 2015 AQR | biannual (Jun/Dec) | publication is the data (no interim) |
| G9 | RBI OBICUS | L11 capex_cycle | RBI | P1 | 2008 Q1+ | quarterly | ~1 quarter lag |
| G10 | RBI reference rate archive (USD/INR) | gold INR decomposition (§6.5), all INR-denominated series | RBI | **P0** | [VERIFY exact start; long archive exists] | daily | T+0 |
| H1 | MOSPI CPI (base 2012, transitioning to base 2024/COICOP-2018) | real-rate input (gold §6.5), L8 deflators | MOSPI (esankhyiki + cpi.mospi.gov.in) | P1 | 2011 (base-2012 series); new series released 2026-02-12 | monthly | ~2 weeks post month-end |
| H2 | WPI (base 2011-12, transitioning to base 2022-23) | context/cross-check inflation | Office of Economic Adviser, DPIIT (eaindustry.nic.in) — **not MOSPI** | P2 | 2004-05 (earlier bases exist); new series from 2026-06 (data back to Apr-2023) | monthly (provisional 14th) | ~2 weeks |
| H3 | IIP + capital-goods sub-index (base 2011-12, transitioning to 2022-23) | L11 capex_cycle | MOSPI (esankhyiki) | P1 | 1994 (base 1993-94 earliest common); base revisions since; new series from 2026-05 | monthly | ~6 weeks post month-end |
| H4 | GFCF / National Accounts Statistics (base 2011-12 → 2022-23) | L11 capex_cycle | MOSPI | P1 | 1950-51 (NAS back series); new base from 2026-02-27 | annual + quarterly | ~2 months (quarterly), longer for annual |
| H5 | PLFS (employment/unemployment) | L16 demographics translation context | MOSPI (microdata.gov.in NADA) | P2 | 2017-18 | annual report; quarterly urban CWS | ~6–12 months |
| I1 | CCIL repo/TREPS/CP-CD rates | L2 fast_stress funding-rank, leverage funding_rate benchmarking | CCIL | **P0** | TREPS from 2014-ish; money-market data longer | daily | T+0/T+1, but bulk history behind sign-in |
| I2 | CCIL G-sec historical trades / yields | L10 macro context, cost-of-carry | CCIL (sign-in) / FBIL (free, 7-day lag) | **P0** | CCIL: 2000s+; FBIL par curve: current+lagged only | daily | T+0 (login) / T+7 (FBIL free) |
| J1 | BIS credit-to-GDP gap (India) | L10 credit_block cross-check ONLY (never replaces Hamilton-own construction) | BIS Data Portal | **P0** | 1951 Q2 (India total-credit series) | quarterly | ~1 quarter |
| J2 | IMF WEO database | L15 long_wave_fiscal (debt trajectory), macro context | IMF | **P0** | 1980+ | biannual (Apr/Oct) | at release |
| J3 | IMF Fiscal Monitor | L15 long_wave_fiscal | IMF | **P0** | ~2000s (varies by series) | biannual | at release |
| J4 | IMF COFER (reserve currency composition) | L15 reserve-diversification input | IMF | **P0** | 1999 Q1 | quarterly | ~1 quarter; **2025-Q3 methodology break** |
| J5 | FRED VIXCLS | L9 global_financial_cycle | FRED (CBOE source) | **P0** | 1990-01-02 | daily | T+0/T+1 |
| J6 | FRED DTWEXBGS (broad USD index) | L9 global_financial_cycle | FRED (Fed Board source) | **P0** | 2006-01-02 (post-2020 methodology; pre-2020 TWEXB discontinued) | daily/weekly→now daily since 2020 | T+1 |
| J7 | FRED DFII10 (10y TIPS yield) | L15 long_wave_fiscal (negative real-rate persistence), gold real-rate input | FRED (Treasury source) | **P0** | 2003-01-02 | daily | T+0/T+1 |
| J8 | FRED DCOILBRENTEU (Brent crude) | L9 context, Kilian-decomposition input | FRED | **P0** | 1987-05-20 | daily | T+1 |
| J9 | World Bank WDI (India macro) | general macro cross-check, no direct ladder binding | World Bank | P2 | 1960+ (varies) | annual | ~1 year |
| K1 | WGC gold demand trends + central bank purchases | L15 CB-buying regime input, gold §6.5 cb_buying_regime | World Gold Council | **P0** | full-year series back to 2000s; quarterly modern | quarterly | ~6 weeks post quarter-end |
| K2 | Gold price (LBMA PM fix, via FRED mirror) | gold §6.5 all price-return construction | FRED GOLDPMGBD228NLBM (mirrors LBMA); LBMA direct behind license | P1 | 1968-04 | daily | T+1 |
| K3 | MCX gold futures (INR gold) | gold §6.5 INR decomposition, futures tactical instrument | MCX | P1 | MCX launched 2003-11; gold contract from inception | daily | T+0 |
| L1 | Jordà-Schularick-Taylor macrohistory panel | Contract §9.4 partial pooling (credit cycle, L10/L12) | macrohistory.net (UC Davis/Bonn/Cambridge) | P1 | 1870 (18 advanced economies — **India NOT included**) | annual | static releases (v6 current) |
| L2 | Kilian real economic activity index | L9 oil/global-cycle decomposition (never raw oil level) | Dallas Fed (successor to Kilian's own site) | P1 | 1968-01 | monthly | ~1 month |
| M1 | UN World Population Prospects | L16 demographics (data Tier A) | UN Population Division | P2 | 1950+ (est.), to 2100 (proj.) | biennial (2024 edition current) | at release |
| M2 | SRS (Sample Registration System) | L16 demographics (fertility/mortality granularity) | Office of Registrar General, India | P2 | 1969-70 | annual bulletins, ~biennial statistical reports | 2–3 year lag, PDF-only |
| M3 | NFHS (National Family Health Survey) | L16 demographics translation (labor/health context) | IIPS / MoHFW | P2 | 1992-93 (NFHS-1); rounds ~5–7yr apart | irregular (6 rounds to date) | rolling factsheet release over ~1–2yrs |
| N1 | ECI election calendar | L5 calendar_windows | Election Commission of India | P1 | 1951-52 (Lok Sabha); state assemblies vary | event-based (fixed 5-yr cycle + state calendar) | announced ~1 month pre-poll |
| N2 | indiabudget.gov.in Budget archive | L5 calendar_windows, STT/Finance-Bill rate source for costs.yaml | Ministry of Finance | **P0** | 1947+ (modern PDF archive from ~2000) | annual (+ interim/special budgets) | at Budget-day presentation |
| N3 | SEBI circulars/studies (Oct-2024 F&O curbs, SME-IPO tightening, anchor 30/90 split, Aug-2026 anchor-exit study, IPO-flipping study) | multiple: leverage/short-sleeve rules, special_situations, tactical_short_sleeve MWPL | SEBI | P2 | circulars: dated individually; corpus browsable 1990s+ | event-based (as issued) | at issuance |

---

## 2. Detail blocks

### A. NSE/BSE core market data

**A1 — NSE cash-market bhavcopy (UDiFF).**
- *Consumes*: nearly every price-only signal — L1 (bhavcopy), L2 (bhavcopy vol), L3 momentum,
  factor_book value/quality/low_vol price-only components, `tail_neglect_sleeve`, cost/impact
  model (`costs.yaml` ADV table), episode-table rebuild (§5.6).
- *Source & path*: NSE. **Old format (discontinued)**: `https://nsearchives.nseindia.com/content/
  historical/EQUITIES/{yyyy}/{MON}/cm{DD}{MON}{yyyy}bhav.csv.zip` — ran until 2024-07-05 in
  parallel, fully discontinued 2024-07-08 per **NSE Circular No. 62424, dated 2024-06-12**
  ("Standardization of Exchange to Member Interface files in Unified Distilled File Formats").
  **New format (current, UDiFF)**: `https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_
  0_0_0_{yyyymmdd}_F_0000.csv.zip`. Landing/browse page: `nseindia.com/all-reports/`.
- *History/freq/lag*: cash-market data exists from NSE's 1994 launch; the old CSV bhavcopy format
  itself dates to the late 1990s. Daily, EOD same-day.
- *PIT/restatement*: **the July-2024 UDiFF switch is a schema break, not a values break** — column
  names/layout changed (security-level fields expanded), so any parser built against the old
  format silently breaks on post-2024-07 files; there is no announced retroactive re-issue of old
  dates in the new schema — **treat 2024-07-08 as a hard parser-version boundary in the fixture
  manifest.** ISIN/symbol continuity across renames/mergers is not guaranteed by the file alone —
  cross-check against corporate-actions (C4).
- *Pull method & size*: bulk daily download, ~1 file/day, low KB–few MB compressed; ~25 years ×
  ~250 trading days ≈ 6,250 files if pulled per-day (script a range-loop; do not attempt one giant
  request). Total corpus likely tens of GB uncompressed for full history across all series types.
- *Fixture spec*: raw `.csv.zip` per date, unmodified; SHA-256 checksum per file; vintage tag =
  pull date; store both pre-/post-UDiFF eras in separate subdirectories with a documented schema
  version per era (see §5).
- *Priority*: **P0**.
- *Access risks*: **NSE's URL scheme is notorious for changing** (this is the second scheme in the
  program's living memory — old CSV → UDiFF, 2024-07). Cloudflare/bot-detection on nseindia.com
  frequently 403s naive `requests`/`curl` pulls without realistic browser headers and a warmed
  session cookie (a known pain point across every third-party NSE-scraping tool surfaced in
  search — `nser` R package, `jugaad-data`, `nsepython`). Budget for a resilient scraper
  (session bootstrap + retry/backoff), not a bare URL loop. **[VERIFY]** exact retention window of
  the pre-2024 archive path (whether NSE prunes old-format files after some horizon) — if pruned,
  the fallback third-party mirrors (getbhavcopy.com, GitHub `bhav-copy`/`nser` caches, Kaggle NSE
  datasets) become load-bearing, not just convenient.

**A2 — NSE F&O bhavcopy (UDiFF).**
- *Consumes*: L4 TSMOM index/gold, L9 global-cycle futures leg, `leverage_function` (futures-
  overlay alternative costing), `tactical_short_sleeve` (single-stock futures), options premium
  budget sizing (§5.5).
- *Source & path*: same UDiFF regime as A1. New: `https://nsearchives.nseindia.com/content/fo/
  BhavCopy_NSE_FO_0_0_0_{yyyymmdd}_F_0000.csv.zip`. Old (discontinued 2024-07-08): analogous
  `fo{DD}{MON}{yyyy}bhav.csv.zip` path under `.../historical/DERIVATIVES/...`.
- *History/freq/lag*: derivatives segment from 2000 (index futures), stock F&O from 2001; daily.
- *PIT/restatement*: same UDiFF schema break as A1, 2024-07-08. Contract specifications
  (lot sizes, expiry calendars) change periodically and are NOT embedded in the bhavcopy file
  itself — must be cross-referenced against NSE circulars for historical lot-size changes when
  reconstructing historical notional exposure.
- *Pull method & size*: bulk daily; larger than cash bhavcopy (many more instrument rows: strikes
  × expiries × underlyings). Multi-year full pull likely tens of GB.
- *Fixture spec*: as A1; additionally store a lot-size/contract-spec crosswalk table (built once
  from circulars) alongside the raw files, since lot sizes are not self-describing historically.
- *Priority*: **P0**.
- *Access risks*: same bot-detection/scheme-change risk as A1. **Weekly-expiry weekday reassignment
  is a live, recent break**: effective 2025-09-01, NSE moved Nifty 50 weekly-options expiry from
  Thursday to **Tuesday**; BSE moved Sensex weekly expiry to **Thursday** — any expiry-calendar
  logic hardcoded to "Thursday" for Nifty will silently misalign contracts from that date forward.
  Also folds in the **SEBI 2024-10-01 index-derivatives circular** (SEBI/HO/MRD/TPD-1/P/CIR/2024/
  132): single weekly-expiry benchmark per exchange (eff. 2024-11-20), contract-size hike to
  ₹15–20L (eff. 2024-11-20), upfront options-premium collection (eff. 2025-02-01), intraday
  position-limit monitoring (eff. 2025-04-01) — each is a regime break for cost/liquidity
  modeling of the tactical short sleeve and hedge stack, not just a documentation footnote.

**A3 — NSE delivery %/security-deliverable data.**
- *Consumes*: momentum liquidity discipline (`sleeves.yaml` liquidity_rules — genuine-demand vs.
  intraday-churn filter), impact-model calibration (`costs.yaml` Y coefficient).
- *Source & path*: bundled historically as "Full Bhavcopy and Security Deliverable data" /
  `sec_bhavdata_full` report on `nseindia.com/all-reports/`; under UDiFF, delivery data is a
  **separate file type** from the plain CM bhavcopy — **[VERIFY]** exact UDiFF delivery-file
  naming convention (not independently confirmed by search; treat as its own schema to reverse-
  engineer on first live pull, distinct from A1's price file).
- *History/freq/lag*: delivery-position reporting exists from ~1999 (post-rolling-settlement
  introduction); daily.
- *PIT/restatement*: none material beyond the shared UDiFF schema transition (2024-07-08).
- *Pull method & size*: bulk daily, small per-file.
- *Fixture spec*: raw file + checksum + vintage date, same convention as A1.
- *Priority*: P1 (feeds sleeve-construction filters, not the Phase-0 bhavcopy blocker itself).
- *Access risks*: shares A1/A2's bot-detection risk; the **[VERIFY]** UDiFF naming gap means the
  first live pull should budget extra reconnaissance time, not assume symmetry with A1's path.

**A4 — BSE cash bhavcopy (cross-check/fallback).**
- *Consumes*: cross-validation of A1 (corporate-action price-adjustment cross-check, coverage for
  any NSE-only gaps), BSE-listed-only small/micro names if NSE's Total Market/Microcap definition
  ever diverges from BSE-only listings.
- *Source & path*: `https://www.bseindia.com/static/markets/equity/EQReports/downloads.aspx`
  ("Archives of Daily/Monthly Reports (EQ)" and Historical Data section).
- *History/freq/lag*: BSE's own archive typically reaches back to 1997ish for daily bhavcopy; daily.
- *PIT/restatement*: BSE has its own, independent scrip-code system (not NSE symbols) — building a
  clean ISIN-level join across NSE/BSE is itself a data-engineering task, not a free lookup.
- *Pull method & size*: bulk daily download from BSE's own portal; comparable size to A1.
- *Fixture spec*: raw file + checksum + vintage date; store alongside an NSE-symbol↔BSE-scrip-code
  ↔ISIN crosswalk (build once, maintain via corporate-action feed).
- *Priority*: P1.
- *Access risks*: lower profile than NSE for bot-detection in search results, but unverified in
  this pass — **[VERIFY]** on first live pull.

**A5 — India VIX historical.**
- *Consumes*: L2 fast_stress (backwardation trigger), L5 calendar vol-scheduling, `risk.yaml`
  hedge-effectiveness/option-budget calibration, episode-table VIX levels (§5.6).
- *Source & path*: `https://www.nseindia.com/reports-indices-historical-vix` (official); mirrored
  identically by Yahoo Finance (`^INDIAVIX`) and Investing.com for a low-friction cross-check.
- *History/freq/lag*: launched 2008-04 by NSE under a CBOE-licensed methodology (Nifty-50-options-
  based, 30-calendar-day expected volatility); daily, same-day.
- *PIT/restatement*: no announced methodology break found in this pass; the underlying options
  chain it derives from changed materially post the 2024-10-01 SEBI derivatives-curbs circular
  (weekly-expiry consolidation) — treat pre-/post-2024-11-20 India-VIX term-structure readings as
  **not strictly comparable** (fewer weekly series to construct term structure from).
- *Pull method & size*: bulk daily download, small file, full history in one pull.
- *Fixture spec*: raw file + checksum + vintage date; keep the Yahoo/Investing.com mirror as a
  cross-check copy, not a substitute primary source.
- *Priority*: **P0**.
- *Access risks*: low relative to bhavcopy (smaller, more stable page); still subject to NSE's
  general bot-detection posture.

**A6 — Price-band/circuit master.**
- *Consumes*: `tail_neglect_sleeve` band-lock-frequency filter (D12's proposed per-stock,
  per-month statistic), momentum liquidity_rules (exclude circuit≥20%-of-days names).
- *Source & path*: the applicable band (2/5/10/20%) per security is **embedded per-row in the
  daily bhavcopy itself** (A1) under UDiFF; the standalone page `nseindia.com/static/products-
  services/equity-market-price-bands` and `nseindia.com/regulations/daily-price-bands-reports`
  give the current-day master and a "daily review" report but **not a clean historical bulk file**
  — the band-lock-frequency statistic must be *derived* from A1's historical closing-vs-band
  data (D12 §6 item 4), it is not purchasable pre-built.
- *History/freq/lag*: bands assignable since price-band regime began (~2001); F&O names carry a
  dynamic, SEBI-defined band with no fixed % (post the 2024-10-01 circular's changes to margin/
  spread treatment on expiry day, this dynamic mechanism itself changed — re-derive, don't assume
  a static rule).
- *PIT/restatement*: a name's assigned band changes over time (surveillance escalation, ASM/GSM
  entry can tighten bands to 2–5%) — the band-lock statistic is therefore itself point-in-time
  sensitive and must be built from the band **as it stood on each historical date**, not today's
  band applied retroactively.
- *Pull method & size*: derived, not pulled — computed from A1 + A7/A8 history once those are in
  hand; zero incremental network pull beyond A1/A7/A8.
- *Fixture spec*: the derived per-stock/per-month band-lock-frequency table itself becomes a
  committed fixture (with its generating script version-tagged, since it is a *construction*, not
  a raw pull).
- *Priority*: P1.
- *Access risks*: none beyond A1's; the real risk is silently computing the statistic against
  today's band-table instead of the historical one (a look-ahead bug, not an access risk, but
  worth flagging here since it originates at this data source).

**A7 — ASM list.** **A8 — GSM list.**
- *Consumes*: exclusion filters for momentum (`sleeves.yaml` liquidity_rules: "exclude ASM/GSM
  stage≥2"), tail sleeve (`GSM≥2/T2T excluded`).
- *Source & path*: ASM — `nseindia.com/reports/asm` (CSV download, current list). GSM —
  `nseindia.com/regulations/graded-surveillance-measure` (current list; FAQ PDF at
  `nsearchives.nseindia.com/web/sites/default/files/inline-files/FAQs - Graded Surveillance
  Measure (GSM)_15.4.25.pdf` confirms mechanics). GSM introduced by SEBI, March 2017.
- *History/freq/lag*: **both pages show the current list only — there is no bulk historical
  archive of ASM/GSM membership with entry/exit dates.** Reconstructing point-in-time membership
  (essential — a name clean today can enter GSM with a month's lag, D12 explicitly) requires
  scraping the dated **circulars** that announce each addition/removal (`nsearchives.nseindia.com/
  content/circulars/...`, or the sharekhan/brokerage mirrors search surfaced as secondary copies),
  not the live list page.
- *PIT/restatement*: **membership additions are not loosening over time — the opposite** (per D12,
  workstream cross-verified): ASM/GSM criteria have been tightened, not relaxed, over the program's
  research period — treat any historical-membership reconstruction as needing the *contemporaneous*
  criteria version, not today's.
- *Pull method & size*: current-list = daily CSV scrape (trivial size); historical membership =
  circular-by-circular scrape (labor-intensive, dozens to low hundreds of circulars/year across
  both frameworks) — this is a genuine data-engineering build, not a one-shot download.
- *Fixture spec*: (a) daily current-list snapshots going forward from Phase 0 (cheap, start now);
  (b) a backward-reconstructed membership-history table (built once from circulars, versioned,
  re-validated whenever a gap is found).
- *Priority*: P1.
- *Access risks*: the historical-reconstruction piece is the real risk — budget it as a distinct,
  multi-day sub-task, not folded into "download the list."

**A9 — F&O eligibility list + selection criteria.** **A10 — MWPL/F&O ban list.**
- *Consumes*: universe definition for `tactical_short_sleeve` (Nifty-100-only is a *subset*
  constraint layered on top of F&O eligibility), leverage-instrument choice context (futures-
  overlay alternative needs to know which names even have futures), execution-risk modeling
  ("ban-period risk (MWPL 95% blocks new positions)" — `sleeves.yaml` short-sleeve costs note).
- *Source & path*: eligibility criteria — `nseindia.com/static/products-services/equity-
  derivatives-selection-criteria` (current rolling-6-month criteria: top-500 by ADV mcap+value,
  median-quarter-sigma-order-size ≥₹75L, MWPL ≥₹1,500cr, ADDV ≥₹35cr). Ban list —
  `nseindia.com/static/products-services/equity-derivatives-risk-management-sec-ban` (daily CSV,
  securities crossing 95% MWPL; reopens below 80%).
- *History/freq/lag*: eligibility reviewed monthly on a rolling basis; ban list published daily,
  pre-session.
- *PIT/restatement*: the **₹75L/₹1,500cr/₹35cr thresholds themselves have been revised over time**
  (they are nominal-rupee thresholds in a growing market — a name eligible at 2015 thresholds may
  not have been at today's) — **[VERIFY]** the historical threshold-change dates before building
  a point-in-time eligible-universe reconstruction; do not apply today's thresholds retroactively.
- *Pull method & size*: daily CSV scrape, small; eligibility-criteria historical values need a
  circular-archive scrape (same style as A7/A8).
- *Fixture spec*: daily list snapshots + one-time-built threshold-history table.
- *Priority*: P1.
- *Access risks*: same NSE bot-detection posture as A1.

**A11 — Bulk/block deals (+ short-selling).**
- *Consumes*: L14 FII-positioning context (large-holder moves), `special_situations`
  bulk_block_pit_following (ranks 500–750 sign/quantile signal, D12 §6 item 5).
- *Source & path*: `nseindia.com/report-detail/display-bulk-and-block-deals` (interactive,
  symbol/date-range CSV export); historical flat files reportedly at `archives.nseindia.com/
  content/equities/bulk.csv` and `.../block.csv` — **[VERIFY]** whether these flat files still
  serve full history or only a recent rolling window (unconfirmed by this pass); an internal API
  endpoint (`nseindia.com/api/snapshot-capital-market-largedeal`) exists but is session-cookie-
  gated, the classic pattern behind several third-party "nsepython"-style wrapper libraries.
- *History/freq/lag*: bulk/block-deal disclosure regime dates to the early 2000s; daily, next-
  day-ish.
- *PIT/restatement*: none material found; deal classification thresholds (bulk = ≥0.5% of
  shares in a single trade; block = separate window, minimum-value threshold) have been revised
  periodically by SEBI — **[VERIFY]** threshold-change history before treating "bulk deal" as a
  constant-definition series across the full sample.
- *Pull method & size*: interactive-export scrape or API pull; per-day file is small, but a full
  multi-year pull needs to page through many date ranges — pre-register the exact pre-test design
  (event window, direction rule, rank-bucket split) **before** looking at ranks 500–750 returns,
  per D12's own instruction, to avoid re-testing a rejected idea with tweaked parameters.
- *Fixture spec*: raw CSV per pull-window + checksum + vintage date.
- *Priority*: P1.
- *Access risks*: cookie/session gating on the API path; the flat-file path's history depth is
  unconfirmed [VERIFY] — treat as the primary risk item for this series.

---

### B. Index data (constituents, TRI, strategy indices, methodology)

**B1–B4 — Nifty 50 / Nifty 500 / Nifty Total Market / Nifty Microcap 250: constituents + TRI.**
- *Consumes*: B1 = frozen drawdown benchmark (Contract §10, "Nifty 50 TRI only for the frozen
  drawdown constraint"); B2 = alpha/signal benchmark for ALL books (Decision Q1) and the moderate/
  conservative stated universe (ranks 1–500); B3 = the aggressive book's *stated* universe
  (NIFTY 750 = Nifty 500 + Microcap 250); B4 = the aggressive tail/neglect sleeve's outer bound
  (ranks 500–750, §6.3).
- *Source & path*: NSE Indices (`niftyindices.com`). Historical TRI: `niftyindices.com/reports/
  historical-data`; a documented (if unofficial) API endpoint
  `niftyindices.com/Backpage.aspx/getTotalReturnIndexString` accepts the exact internal index
  name (broad-market names spaced-uppercase, e.g. "NIFTY 50"; strategy-index names compact, e.g.
  "NIFTY100 LOW VOLATILITY 30" — get the exact string from each factsheet before scripting a pull).
  Factsheets (constituents + methodology summary), one PDF per index: `niftyindices.com/Factsheet/
  Factsheet_NiftyTotalMarket.pdf`, `.../Factsheet_Nifty_Microcap_250_Index.pdf`, etc.; NSE's own
  mirror at `nsearchives.nseindia.com/content/indices/Factsheet_Nifty_Microcap_250_Index.pdf`.
- *History/freq/lag*: **Nifty 50** — base date 1995-11-03 (base value 1000), launched 1996-04-22.
  **Nifty 500** — [VERIFY exact base/launch date; not independently confirmed this pass, widely
  cited as ~1996]. **Nifty Total Market** — a genuinely recent NSE Indices construct (post-2023
  per search evidence and the whitepaper framing); **[VERIFY]** exact launch date before treating
  any pre-launch "history" as anything other than a **back-computed/back-tested series**, not a
  live, point-in-time-published index — this matters directly for the design's own point-in-time
  discipline (prior #7). **Nifty Microcap 250** — base date **2005-04-01** (base value 1000), but
  the index itself was only **launched in 2023** per NSE's own whitepaper framing found in search
  — same back-computed-history caveat as Total Market applies. Daily levels; semi-annual
  reconstitution (last trading day of March/September, aligned across the whole family, "four
  weeks' prior notice" for any replacement).
- *PIT/restatement*: **the single most important caveat in this block**: for Total Market and
  Microcap 250, "history back to base date" is a **backfilled/back-tested construction published
  at a much later launch date** — it did NOT exist, tradable and quoted, before actual launch.
  Any backtest using pre-launch history for these two indices must be flagged as **not
  point-in-time** (survivorship + hindsight bias exactly analogous to prior #7's fundamentals
  problem, but for the benchmark/universe itself) — the moderate/conservative books can rely on
  Nifty 500 (older, presumably genuinely live longer), but the *aggressive* book's stated universe
  (NIFTY 750 = Nifty 500 + Microcap 250) inherits this caveat directly. Separately: **semi-annual
  reconstitution is itself a scheduled index-composition break** — any backtest must apply
  membership *as of each historical rebalance date*, never today's membership retroactively (a
  standard survivorship trap, explicitly why the design needs its own point-in-time universe
  build rather than trusting "current constituents" lists).
- *Pull method & size*: bulk API/CSV pull per index; small-to-moderate size (daily levels ×
  history), fast.
- *Fixture spec*: raw TRI history file + constituents-as-of-each-rebalance-date snapshot (built
  from factsheet PDFs archived per revision, or NSE Indices' periodic constituent-change
  announcements) + checksum + vintage date; **explicitly tag the pre-launch portion of Total
  Market / Microcap 250 history as "back-computed, not point-in-time"** in the fixture metadata.
- *Priority*: **P0** (B1/B2 unconditionally; B3/B4 P0 too since the aggressive book cannot be
  built without them, but their pre-launch segment carries the PIT caveat above and should not
  gate Phase-0 completion on resolving the exact launch date — pull what's available, flag it).
- *Access risks*: niftyindices.com's unofficial POST-based API endpoint is not a stable public
  contract — treat as fragile, verify response shape on every pull; the factsheet PDFs are the
  more stable fallback for constituents (if less convenient for full daily TRI history).

**B5–B7 — Strategy indices (Nifty200 Momentum 30, Nifty Alpha Low-Volatility 30, Nifty500 Value
50, Nifty200 Quality 30).**
- *Consumes*: `sleeves.yaml` crowding/AUM-growth monitors for momentum and low_vol (explicitly
  **not** as the sleeve's own construction — low_vol's own note is emphatic: "pure realized-vol
  rank, NOT the alpha-blended Nifty Alpha-Low-Vol-30 construct"); value/quality crowding
  cross-checks are contextual, not construction inputs either.
- *Source & path*: same niftyindices.com factsheet + historical-data mechanism as B1–B4.
  Confirmed exact names: **Nifty200 Momentum 30** (6m/12m vol-adjusted momentum score, factor-tilt
  weighting), **Nifty Alpha Low-Volatility 30** (alpha+low-vol blended score, 5% single-stock cap
  — the blended construct the design explicitly avoids replicating), **Nifty500 Value 50**,
  **Nifty200 Quality 30**.
- *History/freq/lag*: each index's own base date (varies, generally 2005–2009-ish per the low-vol
  base-date convention search surfaced; **[VERIFY]** each individually before use) — all
  materially younger tracked series than Nifty 50 itself; semi-annual reconstitution.
- *PIT/restatement*: same back-computed-pre-launch caveat as B3/B4 likely applies to some of
  these — **[VERIFY]** each index's actual launch date vs. base date before using pre-launch
  segments as anything but illustrative.
- *Pull method & size*: as B1–B4, smaller (fewer, narrower indices).
- *Fixture spec*: as B1–B4.
- *Priority*: P1 (crowding-monitor inputs, not Phase-0 blockers).
- *Access risks*: as B1–B4.

**B8 — NSE equity-indices methodology document.**
- *Consumes*: `special_situations.index_inclusion_exclusion` (announcement-to-effective window
  sizing), the reconstitution-pop fade-window rule (`sleeves.yaml` momentum liquidity_rules).
- *Source & path*: `nsearchives.nseindia.com/content/indices/Method_NIFTY_Equity_Indices.pdf`
  (also mirrored at `niftyindices.com/Methodology/Method_NIFTY_Equity_Indices.pdf`).
- *History/freq/lag*: single current document, revised periodically by NSE Indices (no fixed
  cadence) — **each revision is itself a point-in-time artifact**: the eligibility/weighting rules
  that applied to a 2015 reconstitution are not necessarily the rules in the document today.
- *PIT/restatement*: **methodology revisions are exactly the kind of break the index-effect
  decay re-estimate (D12 §6 item 2) needs to segment by era** — archive every version pulled,
  dated, rather than overwriting.
- *Pull method & size*: manual PDF download, small, infrequent (check quarterly for a new
  version).
- *Fixture spec*: PDF + checksum + vintage date (the date OF PULL, cross-referenced against the
  document's own "last revised" line if present).
- *Priority*: P1.
- *Access risks*: none beyond general NSE domain fragility.

---

### C. Ownership, disclosure, and corporate-action filings

**C1 — SAST Regulation 29 disclosures.**
- *Consumes*: `costs.yaml capacity_bounds.sast_disclosure_mcap_floor_cr` (**correct value:
  ₹11,000–30,000cr**, per the consistency audit's correction of D05's arithmetic — do NOT use the
  earlier, wrong ₹19,000–31,000cr figure that still sits in `config/books.yaml`'s comment field
  pending a registry fix), the two-universe split (`books.yaml` full-conviction vs. small-ticket
  cohorts, §2.1).
- *Source & path*: `nseindia.com/companies-listing/corporate-filings-regulation-29` (per-company,
  per-date filing list; BSE mirrors the same disclosures under its own corporate-filings portal).
  Regulation 29 treats share pledges as acquisitions/disposals for disclosure purposes (with an
  exemption for banks/PFIs/HFCs/systemically-important NBFCs holding as pledgees in the ordinary
  course of lending).
- *History/freq/lag*: current SAST (Substantial Acquisition of Shares & Takeovers) Regulations
  2011 regime; disclosure trigger crosses defined ownership thresholds; disclosed within
  prescribed short windows (a few trading days).
- *PIT/restatement*: the SAST Regulations themselves have been amended multiple times since 2011
  (thresholds, exemptions) — treat rule-vintage as part of the point-in-time record, not a fixed
  constant across the full sample.
- *Pull method & size*: scrape the per-company filing index (structured list), then parse the
  underlying disclosure PDFs for the actual %-holding figures — the list page alone typically
  gives filer/date/company, not the numeric detail, which lives in the attached document.
- *Fixture spec*: filing-index CSV + linked PDFs, checksummed, vintage-tagged; a derived numeric
  panel (company × date × %-holding) as a separate versioned fixture once parsed.
- *Priority*: P1.
- *Access risks*: PDF-parsing overhead is the dominant cost here (heavier than a plain CSV pull);
  format of the underlying disclosure document is not perfectly standardized across filers.

**C2 — SAST Regulation 31 event-based disclosures (promoter pledge/encumbrance).**
- *Consumes*: `sleeves.yaml factor_book.quality` India junk terms (promoter-pledge intensity),
  the pledge-cascade crash-risk overlay (D02/D12).
- *Source & path*: `nseindia.com/companies-listing/corporate-filings-regulation-31-event`.
  Regulation 31(1) requires promoters/PACs to disclose encumbrance (including pledge) to the
  company and exchanges within **7 working days**; the requirement doesn't apply if the
  encumbrance is created within the depository system itself (a genuine coverage gap to note).
- *History/freq/lag*: current regime since the 2011 SAST Regulations (as periodically amended);
  event-based, ≤7 working days lag.
- *PIT/restatement*: this is the exact data D12 §6 item 3 flags as the highest-value build for
  testing the pledge-invocation-cascade mechanism specifically (as distinct from steady-state
  high-pledge levels) — the registry's own note is blunt: "a case count is not a measured effect
  size" (red-team finding) — the ~10–15 cited episodes (Zee, CCD, Cox & Kings, Vakrangee, 2015–23)
  are a starting list, not a completed census.
- *Pull method & size*: same PDF-parsing overhead as C1; per-company, per-event.
- *Fixture spec*: filing-index + PDFs + derived (company × date × pledge-%-of-holding × event-type
  [creation/invocation/release]) panel as its own versioned fixture.
- *Priority*: P1.
- *Access risks*: as C1; additionally, invocation events (the economically loaded ones) are not
  flagged distinctly from routine creation/release in the raw filing type — the derived panel must
  encode this distinction itself, it is not free from the source.

**C3 — Quarterly shareholding pattern.**
- *Consumes*: L14 FII float-scaled ownership-percentile (Tier C, reduce-only).
- *Source & path*: `nseindia.com/companies-listing/corporate-filings-shareholding-pattern`
  (also `...-shareholding-pattern-sdd` for the newer "integrated filing" format).
- *History/freq/lag*: quarterly, due within 21 days of quarter-end per SEBI LODR Regulation 31;
  standardized structured filings from roughly 2009 onward.
- *PIT/restatement*: SEBI's shareholding-pattern disclosure format itself has been revised (most
  recently toward an "integrated filing" combining multiple LODR disclosures) — treat the format
  version as part of the vintage tag, since field names/granularity differ across the transition.
- *Pull method & size*: per-company, per-quarter scrape; moderate volume across the ~750-name
  universe × ~quarters since 2009.
- *Fixture spec*: raw filing + checksum + vintage; derived float-scaled-FII-ownership panel
  (company × quarter) as its own fixture.
- *Priority*: P1.
- *Access risks*: format-transition parsing (as above); otherwise standard NSE-portal risk.

**C4 — Corporate actions (splits/bonus/demergers/buybacks/delistings).**
- *Consumes*: price-adjustment factors needed by every price-only sleeve (a raw, unadjusted
  bhavcopy price series is wrong across any split/bonus without this), `special_situations`
  demergers/buybacks/delisting-arb event rules, the demerger event registry (D12 §6 item 1,
  "the single highest-value new data-build in this dossier").
- *Source & path*: no single clean bulk historical file was confirmed by this pass. NSE's
  corporate-filings/announcements portal (`nseindia.com/companies-listing/corporate-filings-
  announcements`) carries the underlying disclosures; BSE's downloads page likely carries a more
  usable historical corporate-action file (**[VERIFY]** — not directly confirmed, inferred from
  BSE's generally more complete historical-download culture per search results). An internal NSE
  API (`corporates-corporateActions`-style endpoint referenced by several scraping tools) exists
  but is session-gated, unconfirmed as stable.
- *History/freq/lag*: corporate-action disclosure regime effectively as old as listed-company
  regulation itself (1990s+), patchier pre-2000 in machine-readable form; event-based, announced
  ahead of record date.
- *PIT/restatement*: **this is the exact build D12 flags as needing a dedicated event registry**:
  demerger record date, parent/spinco identifiers, relative size (spun-off mcap ÷ parent mcap
  pre-demerger), and 3/6/12/24/36-month forward returns for both entities vs. a matched benchmark
  — 20–40 candidate India events, 2000–2025, is D12's own estimate of the available sample; this
  does not exist pre-built anywhere free and must be constructed from raw filings.
- *Pull method & size*: scrape + manual reconciliation; a genuinely labor-intensive build, not a
  bulk download — budget accordingly (this is called out explicitly in the runsheet, §4).
- *Fixture spec*: raw per-event filings (checksum + vintage) plus the constructed demerger/spinoff
  event-registry table as its own versioned, append-only fixture (never overwritten — corrections
  append a new vintage row, per §11's point-in-time discipline).
- *Priority*: P1 (adjustment factors gate every sleeve); the demerger-registry sub-build is
  correctly P2/Phase-4 per DESIGN §12's own build sequence.
- *Access risks*: the biggest single labor-cost item in this whole catalog outside the IPO/anchor
  build (D2/D1) — treat as its own mini-project, not a line item.

**C5 — PIT (insider trading) disclosures, SEBI PIT Regulations 2015, Regulation 7.**
- *Consumes*: `special_situations.bulk_block_pit_following` (ranks 500–750 only).
- *Source & path*: same NSE corporate-filings portal family as C1–C3 (insider-trading disclosure
  sub-section); NSDL also runs a "system-driven disclosures" portal
  (`issuer.nsdl.com/systemdrivendisclosure.html`) for the automated PIT/SAST trade-disclosure
  pipeline introduced to reduce manual filing lag.
- *History/freq/lag*: SEBI PIT Regulations, 2015 regime; disclosure within ≤2 trading days of the
  transaction for "connected persons"/designated persons.
- *PIT/restatement*: the system-driven-disclosure (SDD) mechanism itself was phased in gradually
  (not universal from day one of the 2015 regulations) — earlier-period disclosures may be
  manually filed and less structured than later SDD-era ones; treat as a soft regime break.
- *Pull method & size*: scrape, per-company per-event; overlaps operationally with C1/C2.
- *Fixture spec*: as C1/C2.
- *Priority*: P2 (this signal is explicitly "C→B pending test," lowest-priority special-sits
  input per `sleeves.yaml`).
- *Access risks*: as C1–C3.

---

### D. IPO / primary market / anchor and lock-in data

**D1 — DRHP/RHP filings + anchor investor allotment disclosure.**
- *Consumes*: `special_situations.lockin_expiry_windows` (the risk-reduction-only, no-adds rule
  around disclosed 30/90-day anchor unlocks), and the explicit exclusion of IPO-allotment as a
  scalable sleeve (`ipo_allotment: excluded`).
- *Source & path*: **primary, authoritative, free**: `sebi.gov.in/filings/public-issues.html` —
  every DRHP/RHP is filed here, per-company, per-issue, as a dated page linking the actual PDF
  prospectus (confirmed live in this pass with real recent examples). **This is NOT a structured,
  tabular, bulk-downloadable dataset** — it is one page per IPO with a PDF attachment; anchor
  allocation tables (investor names, quantities, prices) live *inside* the RHP/anchor-allocation-
  letter PDF, not as a separate machine-readable field anywhere on sebi.gov.in.
  **Structured secondary source**: Chittorgarh's "Anchor Investor" reports
  (`chittorgarh.com/report/anchor-investors-list/133/` and `.../mainboard-ipos-anchor-investors/
  163/`) tabulate anchor-investor-wise allocation across IPOs by year, browsable free (their
  "IPOMatrix" paid tier packages this as a structured historical database since 2004 — **the free
  tier is browse-only, not bulk-exportable**, a genuine access constraint).
- *History/freq/lag*: SEBI's DRHP filing page has entries stretching back through the 2010s in
  this pass's search results (structured, per-filing pages); anchor-investor lock-in as a distinct
  30/90-day-split disclosure regime dates specifically to **SEBI's ICDR amendment notified
  2022-01-14, effective for IPOs opening on/after 2022-04-01** (Schedule XIII Part A, ICDR
  Regulations 2018) — before that date the anchor lock-in structure was different (a single,
  shorter tranche), so any cross-period anchor-exit analysis must segment at 2022-04-01.
- *PIT/restatement*: **this is the single most consequential correction already in the register
  and must not be reintroduced**: a **~August 2026 SEBI study** (242 mainboard IPOs, April
  2022–October 2025) found anchor exit is **gradual**, not a prompt sell-down — weighted exit only
  ~3.2% at the 30-day unlock, ~8% by 60 days, ~17.3% by 90 days (167-IPO one-year subset: 34.4%
  by 180 days, 50.7% by 365 days; FPIs sold ~60% within a year vs. ~38% for mutual funds, which in
  over 100 of the 242 IPOs did not exit at all beyond day 30). This is the opposite of the
  "anchors sell promptly" framing an earlier draft carried — the design's own `lockin_expiry_
  windows` rule already carries the corrected `evidence_note` in `sleeves.yaml`; this catalog
  entry exists so the *data build* also reflects it, since D12 §6 item 7 explicitly calls for an
  India-specific pre/post-unlock event test using exactly this RHP+bhavcopy combination — build
  it against the corrected null hypothesis (gradual exit), not the US Field-Hanka analogy.
- *Pull method & size*: manual/scrape hybrid — per-IPO PDF download from SEBI (primary, always
  available even if slow) cross-checked against Chittorgarh's tabulated summary (faster, but
  browse-only on the free tier, so still manual transcription for anything beyond spot-checks).
  Genuinely labor-intensive for a multi-year panel (the D12-recommended registry build).
- *Fixture spec*: raw RHP/anchor-allocation PDFs (checksum + vintage = filing date) + a derived
  structured panel (IPO × anchor-investor × allocation × lock-in-tranche-dates), append-only,
  version-tagged against the 2022-04-01 regime boundary.
- *Priority*: P2 (Phase 4/6 per DESIGN §12's own build sequence — special-sits sleeve).
- *Access risks*: no clean free bulk API exists (§6 gap list); this is a genuine multi-week
  construction project, not a download.

**D2 — Post-listing bhavcopy for lock-in event study.** Identical to A1, subset by listing date +
lock-in windows; no separate pull. *Priority*: P2 (paired with D1).

**D3 — Index-reconstitution announcement history.**
- *Consumes*: `special_situations.index_inclusion_exclusion` rising-decay re-estimate ("India ≈
  US-1990s today" — must be re-estimated every cycle, never frozen).
- *Source & path*: NSE Indices' own semi-annual reconstitution announcements (four-weeks'-prior-
  notice press releases, on `niftyindices.com`/`nseindia.com`); for the broader cross-index test
  (D12 §6 item 2) also MSCI India and FTSE India semi-annual/quarterly review announcements
  (msci.com, ftserussell.com index-review pages — both publish free review-result press releases,
  though not always a clean bulk historical file).
- *History/freq/lag*: Nifty-family reconstitution since 1996 (semi-annual, March/September);
  MSCI/FTSE reviews on their own independent calendars.
- *PIT/restatement*: D12's proposed test explicitly segments by **calendar era (pre-2015 vs.
  post-2020)** to test the "rising decay as passive AUM grows" hypothesis directly rather than
  assume it — this era-segmentation is itself the point of the build, not an afterthought.
- *Pull method & size*: scrape of periodic press releases/circulars, moderate labor.
- *Fixture spec*: announcement PDF/press-release + derived event table (index × date × add/drop ×
  announcement-to-effective lag), versioned.
- *Priority*: P2.
- *Access risks*: MSCI/FTSE announcement pages are outside the India-exchange domain family and
  were not stress-tested for access in this pass — **[VERIFY]**.

---

### E. Mutual funds (AMFI)

**E1 — AMFI daily NAV.**
- *Consumes*: general fund-flow/AUM context (Contract §3 names AMFI explicitly as a free source);
  no single ladder entry binds to it directly, but it is a Phase-0-named fixture (DESIGN §12).
- *Source & path*: `portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx` (date-range history
  download); current-day snapshot at `amfiindia.com/spages/NAVAll.txt`. Confirmed free bulk
  mirrors exist (a rebuilt full-history dataset, ~37M+ rows since April 2006, in Parquet/CSV/
  SQLite, refreshed multiple times daily from AMFI directly by a third party) — useful as a
  cross-check, not a substitute primary pull.
- *History/freq/lag*: standardized AMFI reporting from **2006-04**; daily, same-day.
- *PIT/restatement*: scheme mergers/renames/NFO-to-open-ended transitions change scheme codes over
  time — a raw NAV series is not automatically a clean, continuous return series without a
  scheme-code crosswalk (AMFI does not publish one cleanly; build from scheme-master history).
- *Pull method & size*: bulk range-download; full-history corpus is large (tens of thousands of
  schemes × two decades of daily NAVs) but manageable as flat CSV/Parquet.
- *Fixture spec*: raw daily NAV files + checksum + vintage; scheme-master crosswalk as a separate,
  periodically-refreshed fixture.
- *Priority*: **P0** (DESIGN §12 Phase-0 deliverable names AMFI explicitly).
- *Access risks*: low — AMFI's portal is comparatively stable and not behind the aggressive
  bot-detection NSE runs; the main risk is the scheme-code discontinuity noted above.

**E2 — AMFI scheme-wise AUM.**
- *Consumes*: capacity/flow context; no direct ladder binding.
- *Source & path*: AMFI's monthly average-AUM disclosure (part of the same amfiindia.com
  ecosystem; scheme-wise average AUM published quarterly per SEBI norms, industry-level AUM
  monthly).
- *History/freq/lag*: standardized industry AUM reporting from ~2012+ in clean machine-readable
  form (earlier data exists but less standardized); monthly/quarterly.
- *PIT/restatement*: category reclassifications (SEBI's 2017 mutual-fund product-categorization
  circular materially re-bucketed scheme categories) are a real break — pre-/post-2017 category
  labels are not directly comparable without a crosswalk.
- *Pull method & size*: bulk monthly/quarterly download, small.
- *Fixture spec*: raw file + checksum + vintage; category crosswalk fixture across the 2017 break.
- *Priority*: **P0** (Phase-0 named).
- *Access risks*: low.

**E3 — AMFI monthly SIP contribution data.**
- *Consumes*: L7 issuance/sentiment context (retail-flow regime proxy); no direct ladder cap.
- *Source & path*: AMFI's monthly industry note PDF, published on the **8th–10th working day of
  the following month** on `amfiindia.com` (e.g. `amfiindia.com/Themes/Theme1/downloads/
  AMFIMonthlyNote_{Month}{Year}.pdf`); third-party compilations (RightAdvise, Vrid, RupeeTools)
  tabulate the same figures back to **2016-04** in spreadsheet-friendly form.
- *History/freq/lag*: standardized monthly SIP reporting from **2016-04**; ~1 month lag.
- *PIT/restatement*: none material found beyond normal methodology refinements; SIP definitions
  (registered vs. contributing vs. discontinued accounts) have been reported with increasing
  granularity over time — earlier months may lack the full breakdown later months carry.
- *Pull method & size*: PDF download + table extraction (the primary source is a PDF, not CSV) —
  budget parsing effort; third-party CSV compilations reduce this if cross-checked against source.
- *Fixture spec*: raw monthly PDF + checksum + vintage; derived monthly CSV panel as its own
  versioned fixture.
- *Priority*: **P0** (Phase-0 named, AMFI generally).
- *Access risks*: PDF-table-extraction fragility (AMFI's note layout has changed across years);
  low network-access risk otherwise.

---

### F. FII/FPI

**F1 — NSE FII/DII daily provisional cash-market activity.**
- *Consumes*: L2 fast_stress same-day funding/flow-stress proxy (NSDL's own data below lags by
  design; this is the intended same-day substitute).
- *Source & path*: NSE's FII/DII trading-activity page (part of the standard reports family,
  `nseindia.com`) — **[VERIFY]** exact current URL (multiple legacy paths surfaced in search,
  e.g. `archives.nseindia.com/content/fo/fii_stats.xls`-style historical files, but the live page
  path was not pinned down precisely this pass).
- *History/freq/lag*: provisional, same-day (T+0), figures are subsequently reconciled/revised by
  the final NSDL numbers (F2) — **explicitly provisional, not final**, by NSE's own framing.
- *PIT/restatement*: **the provisional-vs-final gap is itself the point-in-time record** — a
  signal built on same-day NSE figures should log both the provisional value used at the time AND
  the later-revised NSDL figure, to measure how much the provisional number typically moves (a
  genuine estimation-quality question, not just a data nicety).
- *Pull method & size*: daily scrape, tiny file.
- *Fixture spec*: raw daily file + checksum + vintage; store both provisional (F1) and final (F2)
  values against the same date, distinctly labeled.
- *Priority*: **P0** (feeds the fast-trigger layer, which is itself Phase-2 but the pull mechanics
  are cheap enough to establish in Phase 0 alongside NSDL).
- *Access risks*: **[VERIFY]** exact URL; general NSE bot-detection risk.

**F2 — NSDL FPI monthly/fortnightly (sector-wise, AUC).**
- *Consumes*: L9 global_financial_cycle (India-transfer factor loading), L14 FII positioning
  (float-scaled ownership extremes, paired with C3's shareholding-pattern data).
- *Source & path*: `fpi.nsdl.co.in` — main reports listing at `Reports/ReportsListing.aspx`;
  fortnightly sector-wise investment at `web/Reports/FPI_Fortnightly_Selection.aspx`; "daily
  trends" (NOT same-day-provisional like F1 — this is NSDL's own, more delayed, cut of daily
  figures) at `Reports/Latest.aspx`; annual/calendar-year net-investment summaries at
  `Reports/Yearwise.aspx?RptType=5` (FY) and `RptType=6` (CY).
- *History/freq/lag*: **the current FPI regime dates to SEBI's Foreign Portfolio Investors
  Regulations, 2014** (notified 2014-01-07, effective 2014-06-01), which merged the prior FII +
  sub-account + Qualified Foreign Investor (QFI) categories into a single FPI class. **Data before
  2014-06 is under the old "FII" nomenclature/regime and lives in a different historical archive
  (SEBI's own legacy FII statistics), not on the NSDL FPI portal** — this is a genuine regime
  break, not just a rename, and must be documented as such in any series spanning it. Fortnightly/
  monthly cadence, ~1 week lag from period-end.
- *PIT/restatement*: sector classification within the fortnightly sector-wise data has itself been
  revised periodically (sector-taxonomy updates) — treat as a soft break requiring a crosswalk if
  splicing across taxonomy versions.
- *Pull method & size*: bulk periodic download, small-to-moderate.
- *Fixture spec*: raw file + checksum + vintage per report type; explicitly separate pre-2014-06
  legacy-FII data (if pursued) into its own labeled fixture set rather than concatenating silently.
- *Priority*: **P0**.
- *Access risks*: low relative to NSE; contact channel (`fpiassist@nsdl.com`) exists if scraping
  proves unreliable, per NSDL's own published support contact.

---

### G. RBI (DBIE, FSR, OBICUS, WSS, reference rate)

**G1 — Non-food credit + sectoral deployment.** **G2 — Credit-deposit (CD) ratio.**
- *Consumes*: L10 credit_block (the design's own Hamilton-filtered credit/GDP gap construction —
  never BIS's HP-filtered version, per the trap list).
- *Source & path*: RBI's Database on Indian Economy — **current canonical URL `data.rbi.org.in/
  DBIE/`** (the domain was formally changed from `dbie.rbi.org.in`/`cimsdbie.rbi.org.in` effective
  close of business **2024-06-21**; both legacy domains now redirect). Navigate: Statistics →
  Real Sector / Financial Sector → "Sectoral Deployment of Bank Credit" (also mirrored at the
  standalone page `rbi.org.in/Scripts/Data_Sectoral_Deployment.aspx`) for G1; Basic Statistical
  Returns (BSR)/Section-42-return-derived CD ratio for G2. RBI's own **"RBIDATA" mobile app**
  (launched **2025-02**, 11,000+ series) is a confirmed alternative export channel if the web
  portal proves brittle to scrape.
- *History/freq/lag*: modern standardized monthly sectoral-deployment series from roughly 1998+
  (older annual data exists further back); non-food-credit growth reported monthly, ~3-week lag.
- *PIT/restatement*: the **CIMS (Centralised Information Management System) integration, June
  2023**, is itself a platform-level break (data model/reporting-frequency changes may accompany
  it for some series) — **[VERIFY]** whether any specific credit series was re-based or
  re-defined as part of CIMS integration, beyond the confirmed URL change.
- *Pull method & size*: DBIE's own export tool (Excel/CSV/PDF); bulk multi-series export is
  supported but the portal's query-builder UI is not a simple flat-file endpoint — budget for a
  scripted-UI or documented-API approach, not a bare URL loop.
- *Fixture spec*: raw export + checksum + vintage per series/vintage-date; DBIE itself supports
  vintage/revision history for some series — capture the **as-published** vintage, not only the
  latest revised value, wherever DBIE exposes it.
- *Priority*: **P0**.
- *Access risks*: portal UI complexity (not a simple REST endpoint); the 2024-06 domain migration
  means any hardcoded old-domain reference in a scraper is now dead (redirects work today but
  should not be relied on indefinitely).

**G3 — RBI policy rates (repo/MSF/CRR/SLR) history.**
- *Consumes*: L6 monetary_stance (lagged ~1y transmission regime input), `risk.yaml` leverage
  funding-rate context (funding benchmarked against repo/MIBOR, per Decision Q3's open item).
- *Source & path*: RBI's **"Handbook of Statistics on the Indian Economy"** (annual publication,
  carries a full historical rate-change table with effective dates back to the Bank Rate era) is
  the single cleanest source for a *long, clean, rate-change-dated* series — cross-referenced
  against DBIE's own current-rate tables for the live end of the series.
- *History/freq/lag*: Bank Rate history extends to 1935; the modern repo-rate-centric LAF
  (Liquidity Adjustment Facility) framework dates to 2000; MSF introduced 2011; event-based
  (rate-change announcement dates), immediate.
- *PIT/restatement*: **the operative monetary-policy instrument itself has changed over the
  sample** — pre-1998 RBI targeted multiple instruments with CRR/SLR as the primary levers;
  post-1998 (and especially post-2016 MPC-era) repo is the primary signaling rate — treat this as
  a regime break in *which rate matters*, not merely a level series, when constructing L6's
  transmission-lag logic.
- *Pull method & size*: manual PDF pull (Handbook is annual, small, stable); DBIE export for
  the live/current tail.
- *Fixture spec*: PDF (per annual edition) + checksum + vintage; a hand-built master rate-change-
  date table as its own versioned fixture (this is a small, high-value, one-time build).
- *Priority*: **P0**.
- *Access risks*: low — this is one of the more stable, well-archived RBI publications.

**G4 — RBI House Price Index (HPI).**
- *Consumes*: L12 realestate_medium_cycle (phase-uncertainty prior on the medium financial cycle).
- *Source & path*: DBIE → Real Sector → Prices & Wages; RBI press releases give the same figures
  ahead of the DBIE update.
- *History/freq/lag*: RBI's HPI covers ~18 major cities, quarterly, historically on a **2010-11
  base**; **the base year was changed to 2022-23**, with the new-base release appearing around
  the **Q2 FY2025-26** reporting cycle (i.e., very recently, within the design's own "current
  date" horizon) — quarterly, roughly 10–12 weeks lag from quarter-end.
- *PIT/restatement*: **this base-year change is a genuine level break** — old-base and new-base
  HPI readings are not directly comparable without a splice; document the exact transition quarter
  once the principal's live pull confirms it, and never fit a trend line through the break
  (mirrors the design's own explicit "2013 duty hikes... are LEVEL BREAKS, never fit through" rule
  for gold — the same discipline applies here).
- *Pull method & size*: DBIE export, small (18 cities × quarters).
- *Fixture spec*: raw export (both base-year vintages, kept distinct) + checksum + vintage.
- *Priority*: P1.
- *Access risks*: as G1/G2 (DBIE portal mechanics).

**G5 — RBI M3 (broad money).** **G6 — Weekly Statistical Supplement (incl. gold/forex reserves).**
- *Consumes*: G5 = macro context (Contract §3 names M3 explicitly); G6 = L15 long_wave_fiscal
  reserve-diversification input (RBI's own gold-buying pattern, a component of the design's
  structural gold-floor attribution, §6.5's `cb_buying_regime`).
- *Source & path*: `rbi.org.in/SCRIPTs/WSSViewDetail.aspx?TYPE=Section&PARAM1=2` (WSS, published
  every Friday) for both; DBIE carries the same M3 series in a queryable time-series form.
- *History/freq/lag*: WSS format has existed since the 1950s (evolving); M0/M1/M2/M3 levels and
  growth rates are DBIE-queryable; weekly (Friday) for WSS, essentially same-week lag.
- *PIT/restatement*: monetary-aggregate definitions (M1/M2/M3 composition) have been revised by
  RBI at least once historically — **[VERIFY]** exact revision date(s) before treating M3 as a
  single continuously-defined series across multiple decades.
- *Pull method & size*: weekly PDF/table pull (WSS), small; DBIE bulk export for history.
- *Fixture spec*: raw WSS PDF (or DBIE export) + checksum + vintage, weekly cadence.
- *Priority*: **P0** (WSS specifically, since it is the free source for RBI's own gold reserves —
  a direct input to §6.5's CB-buying-regime score, distinct from and complementary to WGC's global
  central-bank data, K1).
- *Access risks*: low; WSS is one of RBI's most stable, long-running publications.

**G7 — RBI REER/NEER.**
- *Consumes*: L15 long_wave_fiscal (context), L9 global-cycle context (INR competitiveness).
- *Source & path*: DBIE (External Sector → Exchange Rate); also periodically re-published inside
  RBI Bulletin articles ("Effective Exchange Rate Indices of the Indian Rupee").
- *History/freq/lag*: monthly; the design's own required series is named "REER 36-currency," but
  **RBI has since expanded/updated its basket to a 40-currency index with base year 2015-16
  (replacing the older 2004-05-based 36-currency basket)** — **[VERIFY]** the exact transition
  date, but the direction of the change (36→40 currencies, base year shift) is confirmed by
  multiple independent search results.
- *PIT/restatement*: **this is exactly the kind of index-composition break the appendix brief asks
  to name explicitly** — the 36-currency series the design cites should be treated as the
  *legacy* series; any live pull should capture both the 36-currency (for continuity with any
  historical citation using that name) and the current 40-currency index, clearly labeled, rather
  than silently substituting one for the other.
- *Pull method & size*: DBIE export or RBI Bulletin table extraction; small.
- *Fixture spec*: both basket vintages as distinct, labeled series; checksum + vintage each.
- *Priority*: P1.
- *Access risks*: as G1/G2.

**G8 — RBI Financial Stability Report (GNPA, BSI).**
- *Consumes*: L10 credit_block's lagging-confirm role (GNPA "as lagging confirm only" per
  `ladder.yaml`).
- *Source & path*: `rbi.org.in` publications page (biannual, June and December); no separate
  time-series API — **the PDF itself is the data**, released twice a year, each edition
  self-contained (no interim updates).
- *History/freq/lag*: FSR series began ~2010 (Issue tracking suggests early issues from that era);
  biannual; the report itself IS the release (no separate lag beyond publication).
- *PIT/restatement*: **the single largest, best-documented regime break in this entire catalog**:
  the **2015 Asset Quality Review (AQR)** — RBI withdrew regulatory forbearance on delinquency
  recognition for restructured assets that had been in place since 2008 — caused system-wide GNPA
  (public-sector banks) to rise from **5.0% (March 2015) to 14.6% (March 2018)**, with the
  system-wide peak around **11.18% (2018)**, purely from **transparent recognition of pre-existing
  stress**, not a sudden new wave of defaulting loans. The **Insolvency and Bankruptcy Code (IBC),
  2017** simultaneously introduced a structural resolution mechanism that changed how (and how
  fast) recognized NPAs get worked out. **Any GNPA time series spanning 2015–2018 must carry this
  break explicitly** — a naive reading of "GNPA tripled" as a credit-cycle deterioration signal
  would be a measurement artifact, not the underlying economic event; this is precisely why the
  design already treats GNPA as a "lagging confirm only," never a leading input.
- *Pull method & size*: manual PDF download per edition (small, infrequent); GNPA/BSI figures must
  be hand-transcribed from each edition's tables into a time series — no bulk historical file
  exists.
- *Fixture spec*: PDF per edition + checksum + vintage (edition date); hand-built GNPA/BSI time
  series as its own versioned, append-only fixture, with the 2015 AQR break explicitly annotated
  inline (not just in a README).
- *Priority*: **P0** (Phase-0 named per DESIGN §12, and the AQR break must be understood before
  any credit-block coefficient estimation begins).
- *Access risks*: low (stable RBI publication); the real cost is the manual-transcription labor
  across editions, not access friction.

**G9 — RBI OBICUS.**
- *Consumes*: L11 capex_cycle (order-books/inventory/capacity-utilization percentile ranks).
- *Source & path*: `rbi.org.in` (Statistics → Surveys) — **[VERIFY]** exact direct download URL;
  not independently pinned down this pass (third-party aggregators like CEIC mirror it, but that
  is a paid service, not the free primary source). Navigation path: RBI's main site → Publications
  → Statistics → Data Releases → Surveys → "Order Books, Inventories and Capacity Utilisation
  Survey."
- *History/freq/lag*: quarterly since **2008** (survey launched that year); ~1-quarter lag.
- *PIT/restatement*: a voluntary-response survey of manufacturing firms — sample composition can
  drift over time (firms entering/exiting the panel); no formal "base year" break, but treat panel
  composition as a soft continuity caveat.
- *Pull method & size*: quarterly PDF/Excel release, small.
- *Fixture spec*: raw release + checksum + vintage, quarterly.
- *Priority*: P1.
- *Access risks*: **[VERIFY]** exact URL is the main risk here — budget reconnaissance time on
  first live pull.

**G10 — RBI reference rate archive (USD/INR).**
- *Consumes*: gold's INR decomposition (§6.5: "INR gold = USD gold + INR depreciation, decomposed
  always"), and implicitly every INR-denominated series that needs a USD cross-check.
- *Source & path*: `rbi.org.in/scripts/referenceratearchive.aspx` (also mirrored by exchanges,
  e.g. MSEI's `msei.in/markets/currency/historical-data/rbireferenceratearchives`).
- *History/freq/lag*: **[VERIFY]** exact start date of the archive (RBI has published a daily
  reference rate for USD/INR for many years; the precise archive-coverage start was not pinned
  down this pass); daily, same-day.
- *PIT/restatement*: none material identified; a genuinely stable series definition.
- *Pull method & size*: bulk daily download by date-range, small.
- *Fixture spec*: raw file + checksum + vintage.
- *Priority*: **P0** (needed the moment any INR-denominated cross-asset comparison begins, which
  is essentially Phase 0/1 for the gold and global-cycle blocks).
- *Access risks*: low.

---

### H. MOSPI / DPIIT (CPI, WPI, IIP, GFCF, PLFS)

**H1 — CPI.**
- *Consumes*: real-rate input to gold's §6.5 score (`real_rate` weight), general deflator use.
- *Source & path*: `esankhyiki.mospi.gov.in/macroindicators?product=cpi`-style portal (analogous
  confirmed path for IIP) and the dedicated `cpi.mospi.gov.in` micro-site for historical PDFs/
  base-2012 series documentation.
- *History/freq/lag*: base-2012 series runs effectively from **2011**; monthly, ~2-week lag.
- *PIT/restatement*: **a major, imminent break, already underway as of the design's own current
  date**: MOSPI's **new CPI series (base year 2024, adopting COICOP 2018 classification)** was
  released starting **2026-02-12**, replacing the base-2012 series — driven by updated weights
  from the 2023–24 Household Consumption Expenditure Survey. **Any CPI-based real-rate or
  deflator construction must decide, explicitly, which base series a given historical date uses,
  and build a splice across 2026-02 rather than silently concatenating two differently-weighted
  series.**
- *Pull method & size*: bulk portal export + PDF cross-check for historical documentation; small.
- *Fixture spec*: both base-2012 and base-2024 series kept distinct, checksum + vintage each;
  a documented splice/crosswalk methodology as its own fixture once built.
- *Priority*: P1.
- *Access risks*: portal-navigation complexity (esankhyiki is a relatively new consolidated MOSPI
  data platform); low outright access-denial risk.

**H2 — WPI.**
- *Consumes*: cross-check inflation context (not itself a named ladder input, but listed in the
  task brief).
- *Source & path*: **correcting an organizational assumption**: WPI is compiled and released not
  by MOSPI but by the **Office of the Economic Adviser (OEA), Department for Promotion of Industry
  and Internal Trade (DPIIT), Ministry of Commerce & Industry** — `eaindustry.nic.in`.
- *History/freq/lag*: current base-2011-12 series; provisional monthly release on the **14th of
  each month** (next working day if a holiday); ~2-week lag.
- *PIT/restatement*: **another live, in-flight break**: the new WPI series (base year **2022-23**)
  became effective from the **2026-06** release (May-2026 data), with back-data provided from
  April 2023 onward. Longer-term: **WPI itself is scheduled for discontinuation after ~5 years of
  parallel publication alongside a new Producer Price Index (PPI)**, per the government's own
  transition announcement — a structural sunset, not just a rebasing, to track going forward.
- *Pull method & size*: bulk portal export, small.
- *Fixture spec*: both base-2011-12 and base-2022-23 series kept distinct; checksum + vintage.
- *Priority*: P2 (context/cross-check only per the design's own indicator list — WPI is not
  named as an input to any specific ladder entry, only listed among free sources generally).
- *Access risks*: low.

**H3 — IIP + capital-goods sub-index.**
- *Consumes*: L11 capex_cycle.
- *Source & path*: `esankhyiki.mospi.gov.in/macroindicators?product=iip` (confirmed live path);
  `mospi.gov.in/iip`.
- *History/freq/lag*: current base-2011-12 series; monthly, released ~6 weeks after the reference
  month.
- *PIT/restatement*: **third member of the same 2026 base-year-revision wave**: the new IIP
  series (base year **2022-23**, aligned with the GDP rebase) is scheduled for release from
  **May-2026** — essentially concurrent with this appendix's own writing date (2026-08-31), so
  the new series should already be live by the time of the Phase-0 pull; confirm on first live
  contact which base is being served by default and pull both if the portal still exposes the
  legacy base-2011-12 series in parallel.
- *Pull method & size*: bulk portal export, small.
- *Fixture spec*: both vintages, distinct, checksum + vintage each.
- *Priority*: P1.
- *Access risks*: low.

**H4 — GFCF / National Accounts Statistics.**
- *Consumes*: L11 capex_cycle.
- *Source & path*: MOSPI National Accounts Statistics annual publication (`mospi.gov.in/
  publication/national-accounts-statistics-{year}`) and the GFCF-specific data page
  (`mospi.gov.in/gross-capital-formation-gross-fixed-capital-formation-net-capital-stock-
  economic-activity-current`).
- *History/freq/lag*: National Accounts back-series to **1950-51**; annual with quarterly GDP-
  expenditure-side estimates; the quarterly GFCF cut specifically lags ~2 months, annual figures
  longer (provisional → revised → final over ~2 years, standard NAS practice).
- *PIT/restatement*: **the fourth, and largest, member of the 2026 base-year wave**: the new GDP/
  National-Accounts series (base year **2022-23**, replacing base 2011-12) was released
  **2026-02-27**, per MOSPI's own press note — this is the anchor rebase that CPI/IIP/WPI are all
  aligning around; a "Sources and Methods" documentation release was scheduled for **August 2026**
  (i.e., essentially now, at this appendix's own writing date) — pull that documentation as soon
  as it appears, since it will specify exactly how the old and new GFCF series should be spliced.
  **GDP/NAS revisions generally (not just this base change) are also routinely restated across
  provisional → first-revised → final estimates over a ~2-year cycle** — treat any single vintage
  pull as provisional until confirmed against a later release, and keep every vintage rather than
  overwriting (this is the textbook "GDP revisions" caveat the task brief names directly).
- *Pull method & size*: annual PDF/Excel publication pull, small; the quarterly release cycle adds
  incremental small pulls.
- *Fixture spec*: every vintage (provisional/revised/final) kept as a distinct fixture row, dated
  by *release* date, not just reference period — this is the single clearest point-in-time
  discipline requirement in the whole macro block.
- *Priority*: P1.
- *Access risks*: low; the discipline burden (vintage-keeping) is the real cost here, not access.

**H5 — PLFS.**
- *Consumes*: L16 demographics translation context (zero allocation authority).
- *Source & path*: `microdata.gov.in/NADA/index.php/catalog/PLFS` (microdata catalog, free
  registration typically required for unit-level extracts; summary reports free without
  registration on `mospi.gov.in`).
- *History/freq/lag*: annual since **2017-18**; quarterly urban Current Weekly Status (CWS)
  estimates within each round; annual reports lag ~6–12 months from the survey period.
- *PIT/restatement*: methodology has evolved somewhat since inception (2017-18 was itself a new
  survey design replacing the older quinquennial Employment-Unemployment Survey) — treat pre-2017
  employment data as a different, non-comparable series.
- *Pull method & size*: annual report PDF/Excel pull, small; microdata extracts larger if pursued.
- *Fixture spec*: raw annual report + checksum + vintage.
- *Priority*: P2 (context-only ladder entry).
- *Access risks*: microdata portal may require free account registration; summary tables do not.

---

### I. CCIL / FBIL (money market, G-sec)

**I1 — CCIL repo/TREPS/CP-CD rates.**
- *Consumes*: L2 fast_stress (funding/CP-spread stress rank), leverage `funding_rate` benchmarking
  (Decision Q3's open item — the principal must confirm actual desk funding cost against this).
- *Source & path*: `ccilindia.com` — TREPS daily settlement volumes at `web/ccil/treps-daily-
  settlement-volumes`; broader "Data & Statistics" section referenced in search results as
  requiring **sign-in** for bulk/trade-level downloads; CCIL also publishes narrative weekly
  "Market Update" PDFs (`ccilindia.com/documents/...`) that are openly downloadable without
  sign-in but are **not a structured time series** (narrative + selected charts only).
- *History/freq/lag*: TREPS/CROMS money-market data from roughly the mid-2010s in the current
  reporting form; daily.
- *PIT/restatement*: **the TREPS mechanism itself replaced the older CBLO (Collateralized
  Borrowing and Lending Obligation) market** — a genuine instrument-level regime break in India's
  collateralized money market; a CP-CD-rate series spanning the CBLO→TREPS transition needs this
  flagged, not spliced silently.
- *Pull method & size*: sign-in-gated bulk download (registration process **[VERIFY]** whether
  free or requiring an institutional relationship — CCIL's own site states it "does not authorize
  commercial use... without written permission," a genuine terms-of-use constraint on downstream
  use, not just an access mechanic).
- *Fixture spec*: raw export + checksum + vintage, once access is confirmed.
- *Priority*: **P0** (named explicitly in the task brief's own P0 list).
- *Access risks*: **the sign-in/terms-of-use wall is the single most concrete access risk in this
  whole catalog for a P0 series** — resolve registration status on day 1 of the Phase-0 pull
  (§4) precisely because a "P0 blocker" that turns out to need an institutional relationship
  changes the Phase-0 timeline materially; see the fallback in §6.

**I2 — CCIL G-sec historical trades/yields.**
- *Consumes*: macro-context yield curve, cost-of-carry inputs.
- *Source & path*: CCIL's own `web/ccil/g-sec-historical-trades` (sign-in gated, same as I1);
  **free fallback**: **FBIL** (Financial Benchmarks India Pvt Ltd, `fbil.org.in`) publishes a
  daily par-yield curve (G-sec/SDL valuations) — **live rates are subscription-only, but a
  7-day-lagged (168-hour) version is free** per FBIL's own published access policy. RBI's own WSS
  (G6) also carries selected G-sec yield reference points as a lighter-weight cross-check.
- *History/freq/lag*: CCIL trade data reportedly from the 2000s; FBIL's own published curve is
  daily, current + 7-day-lag-free / real-time-subscription.
- *PIT/restatement*: none specific beyond the general G-sec-market microstructure changes over
  two decades (dematerialization, NDS-OM electronic trading platform's own rollout, etc. — context,
  not a numbered break).
- *Pull method & size*: FBIL free 7-day-lag daily pull (small); CCIL sign-in pull if the
  relationship is secured.
- *Fixture spec*: raw file + checksum + vintage; label explicitly whether a given day's yield came
  from the free-lagged FBIL feed or a subscription/CCIL source, since they may not always agree
  to the basis point.
- *Priority*: **P0** (paired with I1 under the task brief's "CCIL" P0 designation, satisfiable in
  practice via the FBIL free-lag fallback if CCIL registration stalls).
- *Access risks*: as I1; FBIL's lag makes it unsuitable for any same-day signal, fine for the
  design's own monthly/quarterly macro-block cadence.

---

### J. Cross-country / global reference (BIS, IMF, FRED, World Bank)

**J1 — BIS credit-to-GDP gap (India).**
- *Consumes*: L10 credit_block — **cross-check only, never a substitute** for the design's own
  Hamilton-filtered construction (the trap list explicitly forbids using BIS's HP-filtered gap
  as the design's own signal).
- *Source & path*: BIS Data Portal, `data.bis.org/topics/CREDIT_GAPS/data` (free, no login,
  single CSV bulk download confirmed by search); India-specific slice at
  `data.bis.org/topics/CREDIT_GAPS/BIS,WS_CREDIT_GAP,1.0/Q.IN.P.A.A`.
- *History/freq/lag*: India's total-credit-to-private-non-financial-sector series runs from
  **1951 Q2**; quarterly, ~1-quarter lag.
- *PIT/restatement*: BIS's own credit series are explicitly **"adjusted for breaks"** (their own
  series-naming convention) — i.e., BIS has already done break-adjustment work on India's credit
  data; document which BIS methodology vintage was pulled, since BIS itself periodically revises
  its break-adjustment methodology across releases.
- *Pull method & size*: single free CSV bulk download, small.
- *Fixture spec*: raw file + checksum + vintage.
- *Priority*: **P0** (DESIGN §12 Phase-0 deliverable explicitly bundles "IMF/BIS").
- *Access risks*: low — confirmed free, no-login, single-file bulk download.

**J2 — IMF WEO.** **J3 — IMF Fiscal Monitor.**
- *Consumes*: L15 long_wave_fiscal (debt trajectory level+slope), general fiscal/macro context.
- *Source & path*: `data.imf.org/en/datasets/IMF.RES:WEO` (SDMX format, entire-dataset download);
  historical vintage-specific database pages also exist per edition
  (`imf.org/en/publications/weo/weo-database/{year}/{april|october}`) — useful because **WEO
  vintages themselves are a point-in-time record** (each edition's forecasts/estimates for a given
  year differ from later editions' revised figures for that same year) — pulling only the latest
  vintage would silently look-ahead-bias any "what did the IMF believe about 2015 debt/GDP, as of
  2015" question. Fiscal Monitor similarly at `data.imf.org/en?sk=4be0c9cb-...`.
- *History/freq/lag*: WEO data from **1980+**, published **April and October** each year; Fiscal
  Monitor on a similar biannual cadence.
- *PIT/restatement*: **pull and retain every historical WEO vintage, not just the current one** —
  this is the single cleanest free source of genuinely point-in-time macro forecasts/estimates in
  this entire catalog, and the design's own point-in-time discipline (prior #7) is wasted if only
  the latest, most-revised vintage is kept.
- *Pull method & size*: bulk SDMX/CSV per vintage; each vintage is a moderate-size file, dozens of
  vintages accumulate to a manageable total.
- *Fixture spec*: one fixture per vintage-edition, checksum + vintage = the WEO edition date
  (April/October + year), never overwritten by a later edition.
- *Priority*: **P0**.
- *Access risks*: low — IMF's data portal is stable and license-free for this kind of use.

**J4 — IMF COFER.**
- *Consumes*: L15 reserve-diversification input (alongside RBI's own WSS gold-reserve data, G6,
  and WGC's central-bank-purchase data, K1).
- *Source & path*: `data.imf.org/en/datasets/IMF.STA:COFER`.
- *History/freq/lag*: quarterly, from **1999 Q1**; ~1-quarter lag.
- *PIT/restatement*: **a very recent, explicit methodology break**: starting **2025 Q3**, with
  revisions applied back to **2000 Q1**, the IMF eliminated the "unallocated reserves" bucket from
  COFER, so every currency's reported share of "100% of world reserves" changed definition at that
  point — **any COFER series spanning 2025 Q3 must use the revised, unallocated-eliminated
  version consistently, not splice an old-definition pre-2025Q3 series onto the new one.**
- *Pull method & size*: bulk quarterly CSV, small.
- *Fixture spec*: raw file + checksum + vintage; note explicitly which COFER methodology vintage
  (pre-/post-2025Q3-revision) a given pull reflects.
- *Priority*: **P0**.
- *Access risks*: low.

**J5–J8 — FRED (VIXCLS, DTWEXBGS, DFII10, DCOILBRENTEU).**
- *Consumes*: J5/L9 (global VIX regime), J6/L9 (dollar-strength regime), J7/L15 (negative real-
  rate persistence, gold real-rate input), J8/L9 (oil context feeding the Kilian decomposition,
  L2's data-source list).
- *Source & path*: individual FRED series pages (`fred.stlouisfed.org/series/{ID}`) each support
  a no-login CSV download; the FRED API (`fred.stlouisfed.org/docs/api/fred/`) supports scripted
  bulk pulls with a free API key.
- *History/freq/lag*: VIXCLS from **1990-01-02**; DTWEXBGS from **2006-01-02** (current
  methodology — see PIT note); DFII10 from **2003-01-02**; DCOILBRENTEU from **1987-05-20**. All
  daily, T+0/T+1 update lag.
- *PIT/restatement*: **DTWEXBGS is itself the successor to a discontinued series** — the older
  "Trade Weighted U.S. Dollar Index: Broad, Goods" (`TWEXB`) was discontinued and replaced by the
  current `DTWEXBGS`/`DTWEXAFEGS` family around **2020**, with a revised currency-weighting
  methodology (the broad index today weights 26 economies including India, Euro Area, China,
  etc., by bilateral-trade share) — a series analyst splicing pre-2020 TWEXB onto post-2020
  DTWEXBGS must treat this as a methodology break, not a seamless continuation.
- *Pull method & size*: trivial — small CSV per series, full history in one request.
- *Fixture spec*: raw CSV per series + checksum + vintage (FRED series are themselves revised
  occasionally for definitional reasons — re-pull periodically and keep each pull's vintage).
- *Priority*: **P0** (DESIGN §12 Phase-0 deliverable names "FRED" explicitly).
- *Access risks*: minimal — FRED is one of the most stable, permissive free data sources
  available; no login required for CSV download, API key is free and instant.

**J9 — World Bank WDI (India).**
- *Consumes*: general macro cross-check; not bound to any specific ladder entry.
- *Source & path*: `data.worldbank.org/country/india`; bulk via DataBank
  (`databank.worldbank.org`) or the Indicators API (`datahelpdesk.worldbank.org` docs — no API
  key required per current documentation).
- *History/freq/lag*: varies by indicator, generally from **1960+**; most series annual, ~1-year
  lag to final figures (WB itself sources much of this from national statistical offices, so
  India-specific breaks — e.g. the 2026 GDP rebase, H4 — propagate into WDI with WB's own lag).
- *PIT/restatement*: inherits every India-specific national-accounts break named elsewhere in this
  catalog (GDP base-year change) plus WB's own periodic WDI methodology revisions.
- *Pull method & size*: API/bulk CSV, small.
- *Fixture spec*: raw file + checksum + vintage.
- *Priority*: P2 (no direct ladder binding; general-purpose supplementary source).
- *Access risks*: minimal.

---

### K. Gold (WGC, LBMA/FRED mirror, MCX)

**K1 — WGC gold demand trends + central bank purchases.**
- *Consumes*: gold §6.5 `cb_buying_regime` score input (weight 0.20–0.25, the single largest
  weighted input to the tactical gold band) and the L15 reserve-diversification narrative.
- *Source & path*: `gold.org/goldhub/research/gold-demand-trends` (quarterly reports, e.g.
  "Gold Demand Trends: Q2 2026"); central-bank-specific cut at
  `gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2025/central-banks`;
  country-level reserve holdings at `gold.org/goldhub/data/gold-reserves-by-country` (built from
  IMF IFS data, so overlaps partially with J4 but at country-granular level IMF's own COFER does
  not expose).
- *History/freq/lag*: Gold Demand Trends reports run back many years (full-year + quarterly
  cadence, current through **Q2 2026** per search results); quarterly, ~6-week lag post
  quarter-end. Central-bank monthly statistics posts (a separate, faster cadence than the
  quarterly GDT report) appear roughly monthly on the Goldhub blog.
- *PIT/restatement*: WGC's own central-bank-purchase figures are themselves subject to revision as
  more countries' reserve data becomes available with a lag — treat any single-quarter reading as
  provisional for ~1–2 subsequent quarters.
- *Pull method & size*: PDF report download (quarterly) + some data-table pages that may require
  a free Goldhub login to filter/export ("login to filter countries by characteristic... download
  data" per search) — **[VERIFY]** whether the specific tables needed (India-relevant central-
  bank purchase series) require registration or are open.
- *Fixture spec*: raw PDF + checksum + vintage (quarterly); any exported data table similarly
  checksummed.
- *Priority*: **P0** (DESIGN §12 Phase-0 deliverable names "WGC" explicitly).
- *Access risks*: possible free-registration wall on some data-explorer tables (not confirmed
  either way this pass) — budget for it; the PDF reports themselves are unambiguously open.

**K2 — Gold price (LBMA PM fix via FRED mirror).**
- *Consumes*: gold §6.5's entire price-return construction (USD gold leg of "INR gold = USD gold
  + USDINR, decomposed always").
- *Source & path*: **do not attempt LBMA's own historical bulk data** — the LBMA/IBA "MyLBMA
  Portal" requires a paid licence for historical benchmark data (confirmed explicitly by search:
  "a licence from IBA is required in order to obtain, use or redistribute historical benchmark
  data"). **Use the free FRED mirror instead**: `fred.stlouisfed.org/series/GOLDPMGBD228NLBM`
  ("Gold Fixing Price 3:00 P.M. (London time) in London Bullion Market, based in U.S. Dollars"),
  which republishes the identical LBMA PM-fix values for free, no login, daily benchmark since
  **1968-04**. LBMA's own live JSON feed (`prices.lbma.org.uk/json/gold_pm.json`) is free for
  current/near-term values if a same-day cross-check is ever needed, but is not a historical bulk
  source.
- *History/freq/lag*: 1968-04+ via the FRED mirror; daily, ~T+1 lag.
- *PIT/restatement*: none specific to the fixing methodology found in this pass (the AM/PM fix
  mechanism itself has been stable; note the 2015 transition from the historic five-member-bank
  "London Gold Fixing" telephone process to the current electronic ICE Benchmark Administration/
  LBMA auction process as a *mechanism* change worth flagging, even if the FRED-mirrored price
  series itself is presented as continuous).
- *Pull method & size*: trivial FRED CSV pull, full history in one request.
- *Fixture spec*: raw CSV + checksum + vintage.
- *Priority*: P1 (needed for §6.5's gold function, a Phase-5 deliverable per DESIGN §12, though
  the pull itself is trivial and cheap enough to do in Phase 0 alongside J5–J8).
- *Access risks*: none via the FRED mirror — this entirely sidesteps LBMA's licence wall.

**K3 — MCX gold futures (INR gold).**
- *Consumes*: gold §6.5's futures-tactical instrument (Contract §3: "Gold via ETF and futures
  only"), and the INR-gold-return decomposition's domestic-price leg (cross-checked against
  K2 × G10's USD/INR rate).
- *Source & path*: `mcxindia.com/market-data/historical-data` (official, exchange-hosted).
- *History/freq/lag*: MCX itself launched **2003-11**, with gold futures among its founding
  contracts; daily, same-day.
- *PIT/restatement*: **gold import-duty changes are level breaks in the INR-gold basis, not in
  the futures price series' continuity per se** — specifically the **2013 duty hikes** and the
  **2024-07-23 Union Budget cut (basic customs duty + AIDC on gold/silver reduced from 15% to
  6%)** are the two dated breaks the design's own `sleeves.yaml` already names ("2013 duty hikes
  and Jul-2024 duty cut are LEVEL BREAKS — never fit through") — this catalog entry exists so the
  fixture-build captures the duty-rate-change dates as metadata alongside the price series itself,
  not only as a design-document footnote. Separately: **Sovereign Gold Bonds (SGBs) are
  confirmed discontinued for new issuance** (last tranche 2023-24 Series IV, February 2024; no
  FY2024-25/25-26/26-27 tranches; government confirmed no near-term revival plans) — relevant
  context if any SGB-linked series was ever considered as a gold proxy (it should not be, given
  discontinuation, but worth noting for completeness).
- *Pull method & size*: bulk historical download from the official MCX portal; small-to-moderate.
- *Fixture spec*: raw file + checksum + vintage; duty-rate-change-date metadata table as a small,
  separate, one-time-built fixture.
- *Priority*: P1.
- *Access risks*: MCX's own historical-data section was described in search results as offering
  only "basic" free historical data, with fuller depth behind third-party paid feeds — **[VERIFY]**
  on first live pull whether MCX's own free section covers the full multi-decade history needed,
  or whether a third-party cross-check (Investing.com's MCX ICOMDEX Gold series) is needed to
  fill gaps.

---

### L. Long-wave / cross-country panels

**L-JST1 — Jordà-Schularick-Taylor macrohistory panel.**
- *Consumes*: Contract §9.4's partial-pooling requirement ("Pool on the Jordà–Schularick–Taylor
  panel where India alone offers <2 cycles"), used for L10/L12's empirical-Bayes shrinkage
  methodology.
- *Source & path*: `macrohistory.net/database/` (free, Creative Commons license, confirmed no
  login required for bulk CSV/Stata/Excel download); documentation PDF at
  `macrohistory.net/app/download/9834516169/JST_documentationR6.pdf`.
- *History/freq/lag*: **18 advanced economies, annual, from 1870** — release-based (current
  "Release 3"/v6-era per search), not continuously updated; **India is NOT one of the 18 countries
  in this panel** (it covers MSCI-World-style advanced economies) — the design uses it purely as
  a *cross-country prior* to pool India's own thin (<2-cycle) domestic sample against, never as a
  direct India data source.
- *PIT/restatement*: this is a static, versioned research dataset (not a live feed) — pin the
  exact release/version pulled, since JST periodically issues revised releases with corrected or
  extended series.
- *Pull method & size*: single bulk download (CSV/Stata), small-to-moderate (45 variables ×
  18 countries × ~150 years).
- *Fixture spec*: raw release file + checksum + vintage = the JST release/version number.
- *Priority*: P1 (needed once credit-block/real-estate-cycle Bayesian shrinkage estimation begins,
  Phase 2, not a bhavcopy-style Phase-0 blocker).
- *Access risks*: none — free, static, stable academic dataset.

**L-KIL1 — Kilian real economic activity index.**
- *Consumes*: L9 global_financial_cycle's oil-decomposition rule ("includes Kilian-decomposed
  oil, never raw price level" — `ladder.yaml` L9 indicator note).
- *Source & path*: **the officially maintained, updated version** is now hosted by the **Federal
  Reserve Bank of Dallas**, `dallasfed.org/research/igrea` (monthly updates; Kilian's own
  personal academic site, `sites.google.com/site/lkilian2019/research/data-sets`, hosts the
  original historical series and documentation but is not the actively-updated source going
  forward).
- *History/freq/lag*: monthly, from **1968-01**; ~1-month update lag; expressed as percent
  deviation from trend (a global bulk dry-cargo-shipping-rate-based index, a proxy for global
  industrial-commodity shipping volume).
- *PIT/restatement*: the index is *retrospectively revised* each time it is recomputed (it is
  detrended against the full available sample, so a value for, say, 2010 can shift slightly with
  every subsequent monthly release, since the trend estimate itself uses all data through the
  current month) — **this is a genuine, structural point-in-time hazard**: a backtest using
  "today's" Kilian index value for a 2010 date is using information not available in 2010. Any
  point-in-time-faithful use must snapshot the index vintage-by-vintage, not use the latest
  release's full-history recompute.
- *Pull method & size*: monthly ASCII/Excel download, small.
- *Fixture spec*: **snapshot the full published series at each pull date, keep every vintage
  distinct** — a single "final" file is not point-in-time-safe here, unusually among the series in
  this catalog.
- *Priority*: P1.
- *Access risks*: low — Dallas Fed is a stable, free, permissive source; the PIT/revision hazard
  above is a methodology risk, not an access risk.

---

### M. Demographics (context only, zero allocation authority)

**M1 — UN World Population Prospects.**
- *Consumes*: L16 demographics (the "data Tier A" half of the entry — age-structure levels).
- *Source & path*: `population.un.org/wpp`; bulk CSV/Excel via the WPP online data portal;
  Our World in Data hosts an equivalent zipped-CSV mirror.
- *History/freq/lag*: estimates from 1950, projections to 2100; **biennial** editions (2024 is
  the current/28th edition per search; next expected ~2026).
- *PIT/restatement*: each biennial edition revises historical estimates as well as projections
  (new census data, methodology refinements) — treat as vintage-sensitive like WEO (J2), though
  lower-stakes given L16's zero-allocation-authority role.
- *Pull method & size*: bulk CSV, moderate size (many country-years), trivial for India-only slice.
- *Fixture spec*: raw file + checksum + vintage = WPP edition year.
- *Priority*: P2.
- *Access risks*: none.

**M2 — SRS (Sample Registration System).**
- *Consumes*: L16 demographics (finer within-India fertility/mortality granularity than WPP).
- *Source & path*: `srs.census.gov.in` (Office of the Registrar General & Census Commissioner,
  Ministry of Home Affairs); reports also indexed on `censusindia.gov.in`'s NADA catalog.
- *History/freq/lag*: launched **1964–65** pilot, fully operational **1969–70**; annual SRS
  Bulletins, roughly biennial full SRS Statistical Reports — with a **2–3 year publication lag**
  typical for the full statistical reports (the 2020 report, for instance, appears in the catalog
  well after 2020).
- *PIT/restatement*: sample design/state-coverage has been periodically expanded since the 1960s
  pilot — treat pre-1970 figures (if ever needed) as a different, less-comparable regime.
- *Pull method & size*: PDF-only reports, manual download and (for any granular figure) manual
  transcription — no structured bulk API found.
- *Fixture spec*: raw PDF + checksum + vintage per report.
- *Priority*: P2.
- *Access risks*: PDF-only, multi-year lag; low outright access-denial risk, but low convenience.

**M3 — NFHS (National Family Health Survey).**
- *Consumes*: L16 demographics translation context (labor/health conditions relevant to the
  demographic-dividend argument).
- *Source & path*: `rchiips.org/nfhs` (nodal: International Institute for Population Sciences,
  IIPS) and the newer `nfhsiips.in` portal; full report PDFs also mirrored by the DHS Program
  (`dhsprogram.com`) which is the standard international access point for microdata requests.
- *History/freq/lag*: six rounds to date — **NFHS-1 (1992-93)** through **NFHS-6 (2023-24)**,
  roughly 5–7 years apart (irregular, not a fixed cadence); factsheets for a given round release
  on a rolling basis over ~1–2 years as state-level fieldwork completes.
- *PIT/restatement*: survey methodology/questionnaire content evolves materially round-to-round
  (comparability caveats are standard in NFHS's own documentation) — treat cross-round comparisons
  as needing the survey's own harmonization notes, not a naive splice.
- *Pull method & size*: PDF factsheets/reports, free; unit-level microdata requires a (free)
  registration/request process via the DHS Program.
- *Fixture spec*: raw PDF + checksum + vintage per round/factsheet.
- *Priority*: P2.
- *Access risks*: low for summary PDFs; microdata access requires a request/approval step.

---

### N. Calendar, budget, and regulatory-document sources

**N1 — ECI election calendar.**
- *Consumes*: L5 calendar_windows (election-window timing/vol-scheduling).
- *Source & path*: `eci.gov.in` (the primary site is **India-geo-restricted** per search —
  confirm the principal's own machine/location resolves it; if not, PIB press releases
  (`pib.gov.in`) and well-maintained secondary compilations (Wikipedia's own election-date tables,
  cross-checked) are a workable substitute for the *dates themselves*, which are public-record
  facts, not a proprietary dataset).
- *History/freq/lag*: Lok Sabha general elections on a nominal 5-year cycle since 1951–52; state
  assembly elections on their own staggered calendars; schedule for a given election is announced
  roughly a month ahead of polling.
- *PIT/restatement*: none — this is a fixed historical/scheduled-event record, not a revised
  statistical series; the only "PIT" consideration is that a scheduled future election's exact
  date can shift right up to the ECI's formal announcement (not a data problem, a real-world one).
- *Pull method & size*: **one-time manual compilation** of the full historical election-date
  table (small, a few dozen rows); trivial ongoing maintenance (add one row per future election
  once ECI announces it).
- *Fixture spec*: a single hand-built, versioned table (election × date × type); no raw-file
  pull needed beyond the sources used to compile it.
- *Priority*: P1.
- *Access risks*: geo-restriction on the primary ECI site (workaround via PIB/secondary sources,
  as above); otherwise trivial.

**N2 — indiabudget.gov.in Budget archive.**
- *Consumes*: L5 calendar_windows (Budget-day timing/vol-scheduling), and — separately and more
  importantly — **the primary source for the STT-rate schedule feeding `config/costs.yaml`**
  (STT is set via the annual Finance Bill/Act, not a SEBI circular; correcting an implicit
  attribution risk — the task brief groups "FY2026-27 STT schedule" under "SEBI circulars," but
  the rate itself is a **Finance Ministry/CBDT** instrument, published via the Budget documents,
  not SEBI).
- *Source & path*: `indiabudget.gov.in/budget_archive/` (Budget Speech, Finance Bill, Annual
  Financial Statement, Receipt/Expenditure Budget, all prior years' documents); the specific
  FY2026-27 STT schedule (already verified in the register: cash delivery 0.1% both legs
  unchanged; futures 0.05% sell-side, up from 0.02%; options premium 0.15% sell-side, up from
  0.1%; options-on-exercise 0.15% of intrinsic, up from 0.125% — all effective 2026-04-01) traces
  to the Finance Bill 2026 text on this site.
- *History/freq/lag*: annual (+ occasional interim/special budgets); all documents uploaded at
  Budget-day presentation, free PDF, no registration.
- *PIT/restatement*: **STT has been hiked twice in ~18 months per the design's own note** —
  the rate table in `costs.yaml` is explicitly "a live registry entry with an expiry date"; this
  source is where the next hike (if any) will first appear, at the next Union Budget.
  Fiscal-deficit/debt-trajectory figures in the Budget documents themselves feed L15's long-wave
  fiscal-trajectory input, and are of course revised (RE→BE→actuals) across the fiscal year and
  subsequent budgets — same GDP-revision-style caveat as H4.
- *Pull method & size*: manual PDF download, small, annual.
- *Fixture spec*: raw PDF (Finance Bill + Budget-at-a-Glance) + checksum + vintage per fiscal
  year; the derived STT-rate table as its own versioned fixture (already partially built in
  `config/costs.yaml`, cross-reference rather than duplicate).
- *Priority*: **P0** (the cost-curve function is explicitly a Phase-0 deliverable per DESIGN §12,
  and it cannot be coded correctly without this primary rate source).
- *Access risks*: none.

**N3 — SEBI circulars/studies.**
- *Consumes*: `risk.yaml` hedge-stack/leverage-instrument context (Oct-2024 F&O curbs circular),
  `sleeves.yaml special_situations` (SME-IPO tightening, anchor 30/90-day lock-in split, the
  Aug-2026 anchor-exit study, the Sep-2024 IPO-flipping study).
- *Source & path*: `sebi.gov.in/legal/circulars` (browsable by year/category, free PDF, no
  login); the specific items already resolved by the verification-log with exact references:
  - **SEBI/HO/MRD/TPD-1/P/CIR/2024/132, dated 2024-10-01** — index-derivatives-framework curbs.
  - **SME-IPO tightening**: SEBI board approvals through 2024 (profitability requirement — min.
    ₹1cr EBITDA in 2 of the last 3 years; OFS capped at 20% of issue size and 50% of pre-issue
    holding; minimum application size raised; RPT norms extended to SME-listed entities), with
    the SME-to-mainboard **migration framework** revised at the **2024-12-18** board meeting and
    formally notified **March 2025**.
  - **Anchor lock-in 30/90-day split**: ICDR amendment notified **2022-01-14**, effective for
    IPOs opening **on/after 2022-04-01** (Schedule XIII Part A, ICDR Regulations 2018).
  - **IPO-flipping study**: SEBI press release, **2024-09-02**, "54% of IPO Shares allotted to
    Investors (excluding anchor investors) are sold within a week" (144 IPOs, Apr-2021–Dec-2023).
  - **~Aug-2026 anchor-exit study**: press-release-level coverage confirmed (242 mainboard IPOs,
    Apr-2022–Oct-2025) but **the primary SEBI document/URL was not located in this pass** — the
    verification-log itself flags this as unresolved and recommends pulling it directly from
    `sebi.gov.in` press releases (or DERA working papers) once live network access is available;
    this catalog inherits that same **[VERIFY]** status.
- *History/freq/lag*: circulars corpus browsable back through the 1990s; individual items dated
  as issued; no ongoing lag (the document is the record).
- *PIT/restatement*: none beyond the events being, by nature, one-off regulatory dates rather than
  a revised statistical series — but each is a genuine **regime-change date** that must gate any
  backtest crossing it (e.g., anchor-exit event studies must segment at 2022-04-01; F&O-cost
  modeling must segment at each 2024-11-20/2025-02-01/2025-04-01 phase-in date).
- *Pull method & size*: manual PDF download per circular/study, small, low-frequency (event-based).
- *Fixture spec*: raw PDF + checksum + vintage per circular; a hand-built master "regulatory
  event calendar" cross-referencing every date above against the specific ladder/sleeve entry it
  gates, as its own small, high-value, versioned fixture.
- *Priority*: P2 (reference documents, not time series — low pull effort, but gates Phase 4/6
  special-sits work specifically, so not a Phase-0 blocker).
- *Access risks*: low, except the one **[VERIFY]** item (Aug-2026 anchor-exit study primary URL)
  which should be the first thing chased down once live network access exists, given how directly
  it bears on a frozen design rule (`lockin_expiry_windows`).

---

## 3. Traceability: catalog → registry

| Config field | Catalog series feeding it |
|---|---|
| `ladder.yaml` L1 (reversal) | A1 |
| `ladder.yaml` L2 (fast_stress) | A1 (vol), A5, I1, F1/F2 |
| `ladder.yaml` L3 (momentum_composite) | A1 |
| `ladder.yaml` L4 (tsmom_index_gold) | A2, K2, K3 |
| `ladder.yaml` L5 (calendar_windows) | N1, N2, A5 |
| `ladder.yaml` L6 (monetary_stance) | G3 |
| `ladder.yaml` L7 (issuance_sentiment) | D1, N3, A1 (first-day pops) |
| `ladder.yaml` L8 (value_spread) | A1, C1/C3-style filings |
| `ladder.yaml` L9 (global_financial_cycle) | J5, J6, F2, G10, L-KIL1, J8 |
| `ladder.yaml` L10 (credit_block) | G1, G2, G8, J1 (cross-check), I1 |
| `ladder.yaml` L11 (capex_cycle) | G9, H3, H4 |
| `ladder.yaml` L12 (realestate_medium_cycle) | G4, C4 (housing credit context) |
| `ladder.yaml` L13 (household_debt) | G8 (FSR), J1-style BIS household series |
| `ladder.yaml` L14 (fii_positioning) | F2, C3 |
| `ladder.yaml` L15 (long_wave_fiscal) | J2, J3, J4, J7, G6, G7, K1 |
| `ladder.yaml` L16 (demographics) | M1, M2, H5 |
| `sleeves.yaml` momentum | A1, A6, A7, A8, B5 (crowding cross-check) |
| `sleeves.yaml` factor_book.value | A1, C1 |
| `sleeves.yaml` factor_book.quality | C1, C2 (pledge/RPT) |
| `sleeves.yaml` factor_book.low_vol | A1, B6 (crowding cross-check ONLY) |
| `sleeves.yaml` factor_book.size_quality_controlled | A1, L-JST1 (cross-country, India excluded) |
| `sleeves.yaml` tail_neglect_sleeve | A1, A6, A7, A8 |
| `sleeves.yaml` special_situations.* | D1, D2, D3, C4, A11, C5, N3 |
| `sleeves.yaml` gold | K1, K2, K3, G6, G7, G10 |
| `sleeves.yaml` policy_portfolio | (no direct data feed — construction rule, frozen) |
| `costs.yaml` statutory rates | N2 (Finance Bill), N3 (SEBI derivatives circular for margin/expiry mechanics) |
| `costs.yaml` adv_by_rank_bucket_cr | A1, A3 (replaces the provisional table, Phase 0) |
| `costs.yaml` sast_disclosure_mcap_floor_cr | C1, B1/B2 (live mcap) |
| `books.yaml` universe splits | B1–B4, A9, C1 |
| `risk.yaml` leverage_function.funding_rate | I1 (CCIL), G3 (repo/MIBOR context) — **principal to confirm actual desk rate; no free source substitutes for this** |
| `mandate.yaml` drawdown_violation_test | A1 (daily NAV proxy via benchmark), B1 |

---

## 4. Phase-0 pull-order runsheet

Ordered for dependency and risk (resolve access-gated items first; cheap/stable items can run
unattended in parallel once scripted). Hours are rough, single-operator estimates (the principal,
per Contract §7 team size), assuming a competent scripter but zero pre-existing NSE-scraping code.

| Order | Task | Series | Est. hours | Why this order |
|---|---|---|---|---|
| 1 | Confirm CCIL registration status (free vs. institutional) | I1, I2 | 1–2 | **Resolve the one genuine "P0 might not be free" risk first** — everything else in this runsheet is confirmed free; if CCIL requires a relationship, switch immediately to the FBIL-lag + RBI-WSS fallback (§6) rather than losing days waiting on CCIL. |
| 2 | Build resilient NSE session/scraper (headers, cookie warm-up, retry/backoff) | A1, A2, A3, A5, A7–A11, B1–B8 | 4–6 | One robust scraper serves the whole NSE domain family; building it once up front is cheaper than debugging bhavcopy pulls ad hoc later. |
| 3 | Pull NSE cash + F&O bhavcopy, full available history (both old-format archive and UDiFF) | A1, A2 | 6–10 | The single largest, most load-bearing pull; everything price-based downstream depends on it. Budget for the format-boundary handling (2024-07-08). |
| 4 | Pull India VIX full history | A5 | 0.5 | Small, high-value, low-risk — quick win. |
| 5 | Pull Nifty 50/500/Total Market/Microcap 250 constituents + TRI, and the four strategy indices | B1–B7 | 3–4 | Confirm the niftyindices.com API/factsheet mechanics; flag Total Market/Microcap 250 pre-launch history per the PIT caveat (§2 B1–B4) immediately, don't discover it later. |
| 6 | Pull delivery %, ASM/GSM current lists, F&O eligibility + MWPL ban, bulk/block deals (current-forward snapshots; historical reconstruction deferred) | A3, A7–A11 | 3–4 | Cheap, start the forward-collecting snapshot habit from day 1 even though full historical reconstruction (circular-scraping) is a later, separate task. |
| 7 | Pull AMFI NAV, AUM, SIP data | E1–E3 | 2–3 | Stable, low-risk portal; do it early to bank a P0 item with near-zero access friction. |
| 8 | Pull NSDL FPI (monthly/fortnightly) + confirm NSE provisional FII/DII page URL | F1, F2 | 2–3 | Confirm the F1 URL gap ([VERIFY]) here rather than letting it linger. |
| 9 | Pull RBI DBIE core: credit/CD-ratio, policy-rate history (Handbook), WSS (gold+forex), reference-rate archive | G1, G2, G3, G6, G10 | 5–7 | DBIE's UI is the least "one script" friendly source in the whole P0 set — budget the most time here; confirm the 2024-06 domain-migration redirects still work. |
| 10 | Pull RBI FSR editions (manual PDF, hand-transcribe GNPA/BSI time series) | G8 | 3–4 | Small file count but manual transcription; do it once, thoroughly, annotate the 2015 AQR break inline. |
| 11 | Pull BIS credit gap, IMF WEO (every vintage), Fiscal Monitor, COFER | J1–J4 | 3–5 | All free, no-login, single-file-per-series — mechanically easy, but the WEO **every-vintage** requirement multiplies the file count; don't shortcut to "latest only." |
| 12 | Pull FRED series (VIXCLS, DTWEXBGS, DFII10, DCOILBRENTEU, GOLDPMGBD228NLBM) | J5–J8, K2 | 1 | Trivial — batch via the FRED API in one script run. |
| 13 | Pull WGC Gold Demand Trends (current + recent back-issues) + central-bank-purchase data | K1 | 2–3 | Confirm whether any Goldhub table needs free registration; PDF reports are unambiguously open. |
| 14 | Pull MCX gold futures history | K3 | 1–2 | Confirm free-tier depth vs. needing a third-party cross-check fill. |
| 15 | Cost-curve function coding (uses A1/A3-derived ADV table + N2's confirmed statutory rates) | costs.yaml | 3–4 | Explicitly named as a Phase-0 deliverable in DESIGN §12; depends on steps 3 and the already-confirmed N2 rate table. |
| 16 | `config/` registry + CI validator smoke-test against the newly-pulled fixtures | all P0 | 2 | Confirms the whole Phase-0 pull actually satisfies "every module runs on fixtures with zero live data" (§11's gate). |

**Total estimated Phase-0 pull effort: ~45–60 hours**, consistent with DESIGN §12's own "weeks
1–3" Phase-0 window for a two-person team where data acquisition is one of several concurrent
workstreams. Items explicitly deferred out of this runsheet (not Phase-0 blockers, tracked in §1
as P1/P2): ASM/GSM/eligibility historical circular-reconstruction, SAST Reg. 29/31 filing-PDF
parsing, corporate-actions/demerger-registry build, IPO/anchor-lock-in registry build, RBI OBICUS,
MOSPI CPI/WPI/IIP/GFCF/PLFS, CCIL-vs-FBIL final resolution if step 1 finds a wall, JST/Kilian,
UN WPP/SRS/NFHS, ECI/Budget/SEBI-circular compilation.

---

## 5. Fixture governance

**Directory layout** (proposed, mirrors the catalog's category letters):
```
data/fixtures/
  A_nse_bse_core/{cash_bhavcopy,fo_bhavcopy,delivery,bse_bhavcopy,india_vix,asm,gsm,
                  fo_eligibility,mwpl_ban,bulk_block}/{pre_udiff,udiff}/{yyyy}/{mm}/{dd}.csv.zip
  B_indices/{nifty50,nifty500,total_market,microcap250,momentum30,alpha_lowvol30,
             value50,quality30}/{tri_history.csv, constituents_asof_{yyyymmdd}.csv, factsheet_
             vintage_{yyyymmdd}.pdf}
  C_ownership_corpactions/{reg29,reg31_pledge,shareholding_pattern,corp_actions,pit}/raw/...
                          + derived/{panel_name}_v{n}.parquet
  D_ipo_primary/{drhp_rhp,anchor_allotment,index_recon}/raw/... + derived/anchor_registry_v{n}.parquet
  E_amfi/{nav,aum,sip}/...
  F_fpi/{nse_provisional,nsdl_monthly}/...
  G_rbi/{credit,cd_ratio,policy_rates,hpi,m3,wss,reer,fsr,obicus,refrate}/{vintage}/...
  H_mospi_dpiit/{cpi,wpi,iip,gfcf,plfs}/{base_2011_12|base_2022_23|...}/...
  I_ccil_fbil/{treps,gsec}/...
  J_global/{bis,imf_weo,imf_fm,imf_cofer,fred}/{vintage}/...
  K_gold/{wgc,gold_price_fred,mcx}/...
  L_panels/{jst,kilian}/{release_version}/...
  M_demographics/{unwpp,srs,nfhs}/{edition}/...
  N_calendar_docs/{eci,budget,sebi_circulars}/...
  MANIFEST.csv          # one row per committed file: path, sha256, series_id, vintage_date,
                         # pull_date, pull_operator, schema_version, notes
```

**Checksum manifest.** Every committed raw file gets a SHA-256 in `MANIFEST.csv`, keyed by its
catalog `ID` (§1) plus a `vintage_date` (see below) — this is what makes "every module testable
with zero live data" (prior #11) verifiable rather than assumed: CI can re-hash committed fixtures
against the manifest on every run and fail loudly on drift.

**Vintage tagging — two distinct dates, never conflated.** (1) `vintage_date` = the date the
underlying figure was *published/as-of* (e.g., a GDP estimate's release date, a WEO edition's
edition-date, a bhavcopy's trading date); (2) `pull_date` = the date *this program* actually
fetched it. For any series with known revisions (GDP/NAS, WEO, Kilian, WPI/CPI/IIP/GDP base
changes, FSR editions) **both dates are mandatory columns**, and a later, revised value is a
**new row, never an overwrite** — this is the single non-negotiable rule in this section, since
half the point-in-time caveats catalogued in §2 exist specifically to be defeated by silent
overwriting.

**Refresh cadence per series** (drives a simple cron/checklist, not a proposal for live trading
infrastructure — the design runs on committed fixtures, refreshed periodically):
| Cadence | Series |
|---|---|
| Daily | A1, A2, A3, A5, A7–A11, F1, G10, J5–J8, K2, B1–B8 (levels) |
| Weekly | G6 (WSS) |
| Fortnightly/monthly | E1–E3, F2, G1, G2, H1, H2, H3, I1, I2, K1 (partial) |
| Quarterly | G4, G9, H4 (quarterly cut), J1, J4, K1 (report) |
| Biannual | G8 (FSR), J2, J3 |
| Annual | H4 (annual cut), H5, N2 |
| Irregular/event-based | A4 (as-needed cross-check), C1–C5, D1–D3, N1, N3 |
| Static/release-based | L-JST1 (re-pull only on a new JST release), M1 (biennial edition) |

Recalibration triggers already stated elsewhere in the registry apply here too: re-run the ADV
table (A1/A3-derived) and the SAST mcap-floor check (C1 vs. B1/B2 live mcap) whenever book AUM
moves ±50% (`costs.yaml capacity_bounds.recalibration_trigger`); re-check the whole statutory
cost stack (N2) at every Union Budget.

---

## 6. Gap list — no clean free source, and the fallback

| Need | Why there's a gap | Fallback adopted |
|---|---|---|
| CCIL bulk historical repo/TREPS/G-sec trade data | Sign-in gated; terms of use bar undisclosed commercial redistribution; free-tier depth unconfirmed | **FBIL's free 7-day-lagged par-yield curve** (I2) for G-sec yields; **RBI WSS** (G6) for a lighter money-market cross-check; treat CCIL access as a day-1 confirmation item (runsheet step 1), not an assumption. |
| LBMA historical gold-price bulk data | MyLBMA Portal requires a paid IBA licence for historical benchmark data | **FRED's `GOLDPMGBD228NLBM` mirror** republishes the identical LBMA PM-fix series for free back to 1968 — fully resolves this gap, not merely a partial workaround. |
| Structured, bulk, free anchor-investor allotment dataset | SEBI's own DRHP portal is one-PDF-per-IPO, not tabulated; Chittorgarh's structured "IPOMatrix" database is a paid tier (free tier is browse-only) | Build the registry in-house from RHP/anchor-allocation-letter PDFs (D12 §6 item 1's own recommendation), cross-checked against Chittorgarh's free browse pages for spot-verification; budget this as a genuine multi-week construction project (§2 D1), not a download. |
| Quantified promoter-pledge-invocation event-study dataset | No pre-built free dataset exists; only a case-count list (~10–15 named episodes) | Build from SAST Reg. 31 raw filings (C2) — the design's own registry already discounts the pledge/RPT junk-terms weight to 50% "pending the episode study" for exactly this reason; the fixture-build IS the resolution path, already scheduled at Phase 1–4. |
| India demerger/spinoff event registry | No exchange or vendor publishes this pre-built, free | Build from raw NSE/BSE corporate-action filings (C4/D3), per D12 §6 item 1 — again, the build itself is the answer, already in the plan (DESIGN §12 Phase 4). |
| Historical ASM/GSM point-in-time membership (not just today's list) | NSE's live pages show current membership only | Reconstruct from dated circulars (A7/A8) — labor-intensive but fully free; start the forward-snapshot habit (runsheet step 6) immediately so at least the going-forward record never has this gap again. |
| Pre-2024-07 NSE bhavcopy if the old-format archive is ever pruned | NSE's retention policy for the discontinued CSV format is unconfirmed [VERIFY] | Third-party mirrors already hold cached copies (getbhavcopy.com, GitHub `bhav-copy`/`nser`-adjacent repos, Kaggle NSE historical datasets) — cross-checksum against these if the primary archive path ever 404s; do not treat any single third-party mirror as authoritative without a spot cross-check against a period where the primary NSE archive is still confirmed live. |
| CMIE / other paid high-frequency India activity trackers (e.g., proprietary business-resumption indices) | Paid, and explicitly excluded by Contract §3's free-source rule | **Deliberate, not a real gap**: DESIGN §13 already names the substitute — RBI OBICUS + MOSPI IIP-capital-goods + GFCF stand in for capex/activity tracking; no fallback needed beyond what's already in the ladder. |
| SEBI's ~Aug-2026 anchor-exit study, primary document/URL | Only press-level coverage located this pass; the verification-log itself flags the primary source as unresolved | Re-attempt directly from `sebi.gov.in` press releases / DERA working papers once live network access exists (first item on the N3 access-risk list); until then, the design already treats the finding at press-coverage confidence, not primary-source confidence — do not silently upgrade its tier without finding the primary document. |
| RBI OBICUS exact direct-download URL | Not independently pinned down this pass — RBI's own survey-publication page structure is not as search-transparent as DBIE | Navigate manually (RBI site → Publications → Statistics → Data Releases → Surveys) on first live pull; CEIC mirrors it but that is a paid service, not to be relied on as the primary source. |
| A single, continuously-defined REER series across the 36→40-currency basket change | RBI changed the basket composition and base year; no vendor publishes a pre-spliced continuous series | Keep both basket vintages distinct (G7) rather than attempting a synthetic splice — the design's own point-in-time discipline treats a level break as something to document, not paper over. |

---
*End of Appendix A. Cross-references: `docs/DESIGN.md` §4 (ladder), §5.6 (episode table), §6.5
(gold), §9 (costs/capacity), §11 (estimation protocol), §12 (build sequence); `config/ladder.yaml`,
`config/sleeves.yaml`, `config/costs.yaml`, `config/books.yaml`; `research/dossiers/12-india-
microstructure-specials.md` §6; `research/register/consistency-audit.md`,
`research/register/verification-log.md`.*
