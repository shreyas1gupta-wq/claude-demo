# Part C — Data engineering: Indian fundamentals for value and quality, free

v1.0 · 2026-09-01 · Extends `docs/masterplan/A-data-catalog.md`, which has **no fundamentals block
at all** (its §2 blocks A–N cover price/index/ownership/IPO/AMFI/FII/RBI/CCIL/BIS/IMF/gold/
macrohistory/demographics/election/budget — company financial statements are absent). This part
fills that gap for `config/sleeves.yaml factor_book.value` and `factor_book.quality` (moderate
book engine, Decision Q6) and for `config/ladder.yaml L8_value_spread`. It reuses, and does not
re-derive, `research/cycles/momentum-deep/partC-data.md`'s bhavcopy mechanics (§C.1 legacy↔UDiFF
crosswalk), corporate-actions math (§C.2), survivorship/PIT-universe procedure (§C.3), and the
mirror-authorization rule (`research/OPEN_QUESTIONS.md`, 2026-09-01) — cross-referenced below, not
duplicated. Consumes: `research/dossiers/02-value-quality-lowvol.md` (theory/evidence/decay),
`research/CONTRACT.md` §3 (free-source mandate), Known Prior #7 (restatement inflates backtests
150–450bps/yr). Feeds: this program's value/quality construction and the fundamentals ingest kit
(a genuine gap — see §C.8's closing note). Checked by web search this pass (snippet-level, per
Contract prior #11 — `sebi.gov.in`, `nseindia.com`, `bseindia.com`, `niftyindices.com` all
egress-blocked here; nothing fetched/parsed directly, unlike momentum Part C's one
`raw.githubusercontent.com` upgrade). Anything not corroborated by ≥2 search results carries
**[VERIFY]**.

---

## C.1 The core problem — point-in-time fundamentals in India

**Where the primary filings live (free).** Every quarterly/annual result a listed Indian company
reports under **SEBI LODR Regulation 33** is filed directly with the exchanges, not just published
in an annual report — the load-bearing fact that makes a free PIT fundamentals store possible at
all. Primary venue: `nseindia.com/companies-listing/corporate-filings-financial-results`
(search-by-company/period, CSV export, XBRL-to-Excel conversion tool); BSE mirrors the same
disclosure under its own corporate-filings/financial-results page (exact production URL
**[VERIFY]**, same caution momentum Part C already flags for BSE's corporate-actions page).
Dual-listed companies file the identical document to both exchanges simultaneously — a genuine
cross-check, analogous to the NSE-vs-BSE bhavcopy cross-check in momentum Part C §C.1.

**XBRL mandate — history, not a single date.** This did not arrive as one clean cutover; it is a
three-stage regime, and conflating the stages will silently wreck a pre-2017 pull:

| Stage | Date | What changed |
|---|---|---|
| Voluntary XBRL (financial results + shareholding pattern) | From **June 2015** (BSE) | Listed companies could optionally submit in XBRL alongside the mandatory PDF; coverage is patchy and self-selected, not universal |
| Format prescription | **SEBI Circular CIR/CFD/CMD/15/2015, 2015-11-30** (revised by a further circular, 2016-05-27, applicable for periods ended on/after 2016-03-31) | Standardizes the P&L line-item format listed entities must use — a necessary precondition for a machine-parseable panel, distinct from the XBRL-mode mandate itself |
| **Mandatory XBRL for financial results, all listed entities** | **BSE Circular DCS/COMP/28/2016-17, dated 2017-03-30, effective 2017-04-01** [VERIFY: NSE's own parallel circular number for the identical effective date] | PDF filed within 30 minutes of the board meeting concluding; XBRL filed within 24 hours of the PDF. This is the practical start of a genuinely machine-readable, exchange-sourced financial-results panel — **treat 2017-04-01 as the hard PIT-panel boundary**, exactly as 2024-07-08 is the hard boundary for bhavcopy (momentum Part C §C.1) |
| **Integrated Filing (Financials)** | Mandatory from **quarter ended 2025-03-31** (SEBI Circular SEBI/HO/CFD/CFD-PoD-2/CIR/P/2024/185, 2024-12-31; PDF-only submission via the old NEAPS "Quick Results" route discontinued 2025-04-01) | Bundles the Reg. 33 financial result, Reg. 23(9) related-party-transaction disclosure, and audit-qualification statement into **one** quarterly XBRL document — a second schema break, this one shrinking rather than growing the parsing burden (fewer, larger filings instead of several small ones per quarter) |

**Taxonomy — two different regulators, two different systems, do not conflate them.** The **MCA
C&I (Commercial & Industrial) Taxonomy** and its Ind AS variant govern **annual** filings to the
Registrar of Companies under the Companies Act (Form AOC-4 XBRL; mandated by the MCA's 2011-06-07
notification, phased by listing status / paid-up capital ≥₹5cr / turnover ≥₹100cr, i.e. this is
where the "since 2011" figure some sources quote comes from). The **NSE/BSE listing-XBRL utility**
governs the Reg. 33/23/31 filings above and is a **separate system built to the exchanges' own
utility, not a direct feed from MCA** — a company's Reg. 33 quarterly XBRL and its AOC-4 annual
XBRL are two independently-filed documents, on two different taxonomies, to two different
regulators, on two different schedules. A build script targeting "India XBRL financials" that
only knows one of these systems will silently miss the other. This program's use case (quarterly
+ annual value/quality signals at NIFTY-750 breadth) needs the **exchange-side** (NSE/BSE
Reg. 33/23/31) system as primary; MCA's AOC-4 XBRL is the fallback for a name that ever stops
exchange-filing (delisting-adjacent) or for cross-checking a disputed number.

**Exact lag, by filing type.**

| Filing | Regulation | Deadline from period-end | Applies to |
|---|---|---|---|
| Quarterly financial results (Q1–Q3) | LODR Reg. 33 | **45 days** | All listed entities (banks: separate RBI-aligned timeline, §C.3) |
| Annual/Q4 financial results | LODR Reg. 33 | **60 days** | Audited; includes Statement of Impact of Audit Qualifications if applicable |
| Shareholding pattern | LODR Reg. 31 | **21 days** | Quarterly (already catalogued: A-catalog C3) |
| Related-party transactions | LODR Reg. 23(9) | **30 days from publication of the half-year results** (not from period-end) | Half-yearly, consolidated basis |
| Auditor resignation, reasons | LODR Reg. 30 | **24 hours** | Event-based |

**Restatement behavior.** SEBI's own XBRL rules explicitly anticipate revision: "revised XBRL
filings are required in case of any mismatch with the PDF, revision of financial results, restated
financials, or voluntary corrections," with revision remarks attached. This is good news
(restatements are a first-class, filed event, not silently absorbed) and bad news for a PIT builder
(there is **no public, structured, single-page archive of "which filings were later revised, and
when"** — a revision shows up only as a second dated filing on the company's own filing-history
page, indistinguishable from a routine subsequent-quarter filing unless the parser reads the
revision-remarks field and cross-references period covered). **The construction rule this forces**:
key the fundamentals store on `(company, fiscal_period, filing_type, announcement_timestamp)`, not
on `(company, fiscal_period)` — a later row for the same fiscal period is a **revision event**, kept
as a new vintage, never overwriting the original (identical discipline to momentum Part C §C.7's
WORM rule and to `ingest/manifest.py`'s existing hash-hard-fail).

**`knowledge_time` — the exact PIT construction rule.** NSE/BSE's own filing convention already
gives the desk almost exactly what a PIT store needs for free: the PDF must be filed within **30
minutes** of the board meeting concluding, and the corporate-announcement record on the exchange
carries the filing's **exact submission timestamp** (date + time, not just date). Use that
timestamp — not the fiscal period-end, and not even the board-meeting date if the two diverge — as
`knowledge_time` for every fundamental fact the filing contains. A signal computed "as of" a
rebalance date must only see filings whose `knowledge_time <= rebalance_date`; this is the single
mechanical safeguard against the look-ahead bias Known Prior #7 already prices at 150–450bps/yr.
Two refinements worth stating: (i) the XBRL follows the PDF by up to 24 hours (pre-2025) or is
simultaneous (Integrated Filing, 2025+) — use the **PDF's** timestamp as `knowledge_time` even when
only the XBRL is machine-parsed, since the market already knew the numbers from the PDF; (ii) a
revised filing gets its **own**, later `knowledge_time` — a backtest run "as of" a date between the
original and the revision must see only the original, exactly the discipline the India-factor-
mirror validation in §C.7 depends on to be meaningful.

---

## C.2 What fields are gettable free, and at what history

**The single most consequential fact for ratio construction**: in India, the quarterly financial
result is **P&L-only plus EPS** — a full balance sheet ("Statement of Assets and Liabilities") and
a cash-flow statement are SEBI-mandated only **half-yearly and annually**, not every quarter (this
mirrors Ind AS 34's minimum interim-disclosure requirement, which the LODR format inherits). A
value/quality build that assumes quarterly balance-sheet granularity because P&L, revenue and EPS
all update quarterly will silently manufacture a false-precision book-value or leverage series that
does not exist as filed.

| Field | Frequency filed free | Source/regulation | Notes |
|---|---|---|---|
| Revenue, PAT, EPS | **Quarterly** (Q1–Q4) | LODR Reg. 33 P&L | Cleanest, highest-frequency fundamental input available |
| Book value / net worth (balance sheet) | **Half-yearly + annual only** | LODR Reg. 33 (half-year note: "Statement of Assets and Liabilities") | NOT quarterly; a Q1/Q3 "book value" is necessarily last-half-year's, stale by up to ~9 months at the worst point in the cycle |
| Cash flow statement (CFO/CFI/CFF) | **Half-yearly + annual only** | LODR Reg. 33 (half-year note: "Statement of Cash Flows") | Same staleness profile as book value; a CF/P signal cannot be a quarterly-refresh signal in India by construction |
| Shares outstanding + face value/paid-up capital | **Quarterly** (embedded in every Reg. 33 filing) **and** quarterly shareholding pattern | LODR Reg. 33; Reg. 31 (≤21 days, A-catalog C3) | Also the input to net-share-issuance (Pontiff-Woodgate), already flagged in dossier 02 §4 as the *least* restatement-exposed value-adjacent signal |
| Promoter holding % | **Quarterly** | Reg. 31 shareholding pattern (A-catalog C3) | Category-wise (promoter/promoter group/public/FII/DII) |
| Promoter pledge / encumbrance | **Event-based, ≤2 trading days (Reg. 29) / ≤7 working days (Reg. 31 SAST)** | SAST Regulations (A-catalog C1/C2 — do not re-derive; reference those blocks directly) | The event-based feed is the higher-frequency, higher-precision source; the quarterly shareholding pattern also carries a pledge-percentage column as a slower cross-check |
| Related-party transactions | **Half-yearly** (30 days post half-year-results publication) | LODR Reg. 23(9) | Consolidated-basis format prescribed by the applicable accounting standard for annual RPT disclosure |
| Auditor resignation + reasons | **Event-based, ≤24 hours** | LODR Reg. 30, Schedule III Part A ("Format B"), effective 2019-04-01 (Kotak Committee reforms) | Detailed reasons *as stated by the auditor* — a genuinely rich, free, point-in-time governance signal |
| Auditor qualification (modified opinion) | **Annual only** | LODR Reg. 33 — "Statement on Impact of Audit Qualifications" | Not a quarterly disclosure; limited-review reports on quarterly results can flag "emphasis of matter" language but a formal qualification-impact statement is an annual artifact |
| Credit rating actions | **Event-based** (≤7 working days press release post rating-committee meeting) | SEBI (Credit Rating Agencies) Regulations, 1999, as amended; CRA's own website (CRISIL/ICRA/CARE/India Ratings) | Higher-frequency proxy for leverage/distress between annual balance-sheet disclosures — §C.4 |

**Cash-flow and balance-sheet "half-yearly" in practice**: because the Indian fiscal year runs
April–March, this means fresh book-value and CFO observations land twice a year — end-September
(H1) and end-March (FY) — with Q1 (June-end) and Q3 (December-end) results carrying **no** new
balance-sheet or cash-flow data at all. Any B/P or CF/P series built naively "quarterly" is
actually a **staircase**, flat for two quarters and stepping at two — this staircase shape, not
smooth quarterly interpolation, is the honest representation and must not be smoothed away.

---

## C.3 Ratio construction under Indian constraints

**E/P — the cleanest multiple.** Trailing-4-quarter PAT ÷ current market cap is fully supported at
quarterly cadence: PAT is a P&L line (quarterly-native, §C.2), and shares outstanding for the
market-cap denominator is quarterly-native too. This is the only classic value multiple that
refreshes every quarter in India without a staleness compromise.

**B/P — annual/half-yearly book value, with a mandatory freshness-lag rule.** Book value is a
staircase input (§C.2). The construction rule already frozen in `sleeves.yaml
factor_book.value.components` (dossier 02 §4, "B/P + E/P lag-buffered ≥4–6m") generalizes directly:
apply the **last disclosed** half-year/annual book value, lag-buffered by the same 4–6 month
knowledge-time discipline as §C.1, and hold it flat between disclosure steps rather than
interpolating a smooth quarterly path that was never actually observable. The Asness-Frazzini
"Devil in HML's Details" warning already logged in dossier 02 §1 (stale-book, current-price B/P
correlates more with momentum, behaves differently in crashes) is *structurally forced* on any
India construction by the half-yearly disclosure cadence itself — it is not an optional
convention choice here the way it is in the US, where quarterly balance sheets exist and a builder
could choose otherwise.

**CF/P — annual-only, a slow-refresh signal by construction.** Because the cash-flow statement is
half-yearly/annual (§C.2), CF/P cannot be a quarterly signal in India the way it can be in markets
with quarterly cash-flow disclosure (the US SEC 10-Q requires one). Treat CF/P explicitly as a
**semi-annual-refresh input** into the value composite, not as a quarterly one masquerading as
such by forward-filling a stale number every quarter.

**EV/EBITDA — feasible, but a genuinely mixed-frequency ratio, honestly stated.** EBITDA is
reconstructable from the quarterly P&L (revenue less operating expense, with depreciation/
amortization typically its own disclosed line item in the Reg. 33 P&L format **[VERIFY: universal
across all Ind-AS-format filers, not just a subset]**) — so the numerator refreshes quarterly. Net
debt for the enterprise-value denominator needs the balance sheet — half-yearly/annual only. The
honest construction is therefore: **EBITDA updates quarterly, net debt updates twice a year**, and
any EV/EBITDA reading in the "off" quarters carries a stale net-debt component by definition, not
by parsing error. This is a feasible multiple for the moderate book's value blend, but it is the
single multiple most exposed to the staircase problem, since both its numerator components
(EBITDA, net debt) are individually fine but their *combination* mixes cadences within one ratio.

**Sales/price — the second cleanest multiple.** Revenue is quarterly-native and shares outstanding
is quarterly-native; sales/price refreshes every quarter with no staleness compromise, matching
its role in `sleeves.yaml` (already listed as a value component) and in the NSE500 Value 50 index's
own published methodology (dossier 02 §2: E/P, B/P, sales/price, dividend yield).

**Sector-relative vs. raw ranks — the banks/financials problem, a separate-treatment rule.**
Indian banks report under **Form A (balance sheet) / Form B (profit and loss)** of the **Third
Schedule to the Banking Regulation Act, 1949** — a wholly different statutory format from the
Companies Act Schedule III / Ind AS statements every non-financial filer uses. Compounding this,
**RBI indefinitely deferred Ind AS implementation for commercial banks** (one-year deferral in
April 2018, then "till further notice" on 2019-03-22, pending Banking Regulation Act amendments
not yet enacted **[VERIFY current status, 2026]**) — so banks still report on an RBI-prescribed
local-GAAP-adjacent framework, not Ind AS, while NBFCs (which *did* complete Ind AS transition,
phase III/IV below) and insurers (own IRDAI format, explicitly **exempted from XBRL filing of
financial results**, PDF-only) each sit on a **third and fourth** distinct format. **The rule this
forces**: financials (banks, NBFCs, insurers — three internally-distinct sub-groups) must be
excluded from any universe-wide raw-ratio rank built on "revenue," "EBITDA," "sales/price," or
"gross profitability" — none map cleanly onto a bank's net-interest-income-led P&L or an insurer's
premium/claims structure. P/E and P/B remain usable for financials, but **ranked within financials
only**, never pooled with non-financials on a common percentile — and even then a bank's book
value (regulatory capital, provisioning-sensitive) is structurally different from an industrial's,
so the sector-relative rank should be sized down, not treated as equivalent evidence.

| Ind AS phase | Effective | Who |
|---|---|---|
| Phase I | 2016-04-01 | Listed companies (any net worth) + unlisted companies, net worth ≥₹500cr |
| Phase II | 2017-04-01 | Listed/listing-in-process companies, net worth ₹250–500cr |
| Phase III | 2018-04-01 | Banks, NBFCs, insurers with net worth ≥₹500cr — **but banks specifically were then deferred (see above); NBFCs and insurers proceeded on their own separate formats regardless (IRDAI for insurers)** |
| Phase IV | 2019-04-01 | NBFCs, net worth ₹250–500cr |

**What our free-data value blend can honestly support at NIFTY-750 breadth.**

| Multiple | Refresh cadence achievable | Coverage caveat |
|---|---|---|
| E/P (trailing 4Q) | Quarterly | Full universe ex-financials-raw-pooling; usable for financials sector-relative |
| Sales/price | Quarterly | Full universe ex-financials (revenue concept doesn't apply cleanly) |
| B/P | Half-yearly step, 4–6m lag-buffered | Full universe; financials sector-relative only |
| CF/P | Half-yearly/annual step | Full universe ex-financials (bank CFO statements exist but mean something different — financing/operating lines dominated by deposit-taking) |
| EV/EBITDA | Quarterly EBITDA / semi-annual net debt (mixed) | Ex-financials entirely — EBITDA is not a meaningful concept for a bank or insurer |
| Dividend yield | Event-based (declaration) + quarterly (interim) | Full universe; the single least restatement-exposed value input, price-only-adjacent |

---

## C.4 Quality inputs, free

**Gross/operating profitability — itself a mixed-frequency ratio.** Novy-Marx's gross-profitability
signal (gross profit ÷ total assets) is the QMJ-lineage core input dossier 02 already anchors on.
Gross profit (revenue less cost of goods/services) is quarterly-native in the P&L; **total assets
is a balance-sheet item, half-yearly/annual only** (§C.2) — so gross profitability inherits the
identical staircase problem as EV/EBITDA's net-debt leg. State this explicitly rather than
computing a smooth quarterly series that implies a precision the underlying filings do not support.

**Accruals — needs balance-sheet deltas, annual/half-yearly only.** Sloan's accrual signal
(non-cash earnings component, from the change in working-capital balance-sheet accounts) requires
two balance-sheet snapshots to difference. Since the balance sheet is a half-yearly/annual object
in India, **the accrual signal is, at best, a half-yearly-refresh signal, and a fully clean annual
one if the half-year "note" balance sheet is judged too abridged to trust for a working-capital
breakdown [VERIFY: whether the half-yearly Statement of Assets and Liabilities carries sufficient
line-item granularity for a working-capital accrual calculation, vs. requiring the fuller annual
balance sheet]** — dossier 02 §5 already flags no India-specific accrual-anomaly study was found;
this data constraint is a plausible part of why that literature gap exists.

**Leverage — annual/half-yearly debt, with a credit-rating-action proxy for higher frequency.**
Total debt (long-term + short-term borrowings) is a balance-sheet line, same half-yearly/annual
cadence. Between two balance-sheet snapshots, **credit rating actions are the free, event-based,
higher-frequency distress proxy**: SEBI's CRA Regulations require rating agencies to continuously
monitor and periodically review every outstanding rating for the life of the security, and any
rating action (upgrade, downgrade, outlook change, withdrawal) is disseminated via press release
within **7 working days** of the rating-committee decision (with the issuer given roughly 3 working
days to seek a review first) — published free on each CRA's own website (CRISIL, ICRA, CARE,
India Ratings) and, since the action itself is a listing-agreement disclosure event, also
announced via the exchange corporate-filings feed. **[VERIFY: the exact minimum mandated review
frequency per outstanding rating — search this pass confirmed "continuous monitoring, periodic
review" language but not a single, citable "at least once every N months" figure]** — treat a
rating action's *date* as reliably free and point-in-time, and its *periodicity* as a softer,
issuer/CRA-discretion-dependent cadence, not a fixed clock the way Reg. 33 filing deadlines are.

**Piotroski F-Score — component-by-component feasibility, India-free-data version.**

| # | Signal | Needs | India free-data feasibility |
|---|---|---|---|
| 1 | ROA > 0 | Net income (qtrly) ÷ total assets (H1/annual) | **Mixed-frequency**, computable at half-yearly cadence |
| 2 | CFO > 0 | Cash flow statement | **Annual/half-yearly only** |
| 3 | ΔROA > 0 | Two ROA readings | **Half-yearly**, since ROA itself is mixed-frequency |
| 4 | CFO > net income (accrual quality) | CFO + net income, same period | **Annual/half-yearly only** (gated by #2) |
| 5 | Δ long-term-debt ratio (falling leverage) | Debt ÷ assets, two periods | **Half-yearly/annual only** |
| 6 | Δ current ratio (rising liquidity) | Current assets ÷ current liabilities, two periods | **Half-yearly/annual only** — current-asset/liability granularity itself depends on the balance-sheet note's detail level **[VERIFY]** |
| 7 | No new shares issued | Shares outstanding, two periods | **Quarterly** — computable at the highest frequency of any Piotroski component |
| 8 | Δ gross margin (rising) | Gross profit ÷ revenue, two periods | **Quarterly** — both legs are P&L items |
| 9 | Δ asset turnover (rising) | Revenue ÷ total assets, two periods | **Mixed-frequency** — revenue quarterly, assets half-yearly/annual |

Net picture: **2 of 9 signals (shares issuance, gross-margin change) are genuinely quarterly**; the
other 7 are gated by the balance sheet or cash-flow statement and are therefore **half-yearly/
annual at best** — a full India F-Score cannot be refreshed more than twice a year without either
(a) accepting stale balance-sheet inputs held flat between disclosures (the same staircase
convention as B/P), or (b) waiting for the annual filing specifically. This is a materially
different computability profile from the US, where quarterly 10-Qs make all nine signals a
quarterly-refresh construct — a fact worth stating plainly since Piotroski's original test design
(and most practitioner replications) implicitly assumes quarterly or annual-only-but-quarterly-
priced data, not India's specific half-yearly balance-sheet gap.

**Governance red flags — source and lag, one table.**

| Signal | Source | Lag |
|---|---|---|
| Promoter pledge % | SAST Reg. 29 (≥5% moves)/Reg. 31 (event) + Reg. 31 LODR shareholding pattern (quarterly cross-check) | ≤2 trading days (Reg. 29) / ≤7 working days (Reg. 31 SAST) / ≤21 days (quarterly pattern) — A-catalog C1–C3 |
| Related-party transactions | LODR Reg. 23(9) | 30 days post half-year-results publication |
| Auditor resignation | LODR Reg. 30, Format B | ≤24 hours |
| Audit qualification (modified opinion impact) | LODR Reg. 33 annual filing | Annual, with the audited results (60-day window) |
| Credit rating downgrade/withdrawal | SEBI CRA Regulations, 1999 (CRA press release) | ≤7 working days post rating-committee decision |

---

## C.5 History depth — how far back can a free PIT panel realistically go

**XBRL era (2017-04-01 onward): genuinely machine-readable, exchange-timestamped, the clean core
of the panel** — matching momentum Part C's UDiFF boundary in spirit, this is the second hard
schema/quality boundary this program's data layer must respect. **Integrated Filing (2025-04-01
onward)**: a further, welcome consolidation (fewer documents, same underlying facts) — not a
regression, but still its own schema version to track.

**Voluntary-XBRL / pre-standardized-format era (2015-06 to 2017-03-31)**: patchy, self-selected
coverage — usable as a partial pre-fill, not as a reliable panel start date. Any backtest claiming
a clean panel start before 2017-04-01 should say so explicitly.

**Pre-XBRL PDF era**: NSE's and BSE's own corporate-filings/announcements portals carry historical
PDF filings (the underlying disclosure, not a machine-readable extract) for names that were listed
and filing electronically; **[VERIFY: the exact year electronic exchange filing itself began at
scale — search evidence for NSE's own filing-portal infrastructure was inconclusive this pass,
beyond confirming the portal exists in broadly its current form by the early 2010s]**. Before
electronic filing became universal, results reached the exchanges as physical/faxed filings, with
much thinner free digital-archive depth.

**The principal-machine OCR option.** Because the Reg. 33 P&L format has been SEBI-prescribed
(and largely stable) since the 2015-11-30 circular, pre-XBRL PDF filings are **structurally
regular** — same line items, same layout, company to company and quarter to quarter — a far more
tractable OCR target than a freeform annual-report PDF. Same genre as the "principal's-machine,
genuine multi-week construction project, not a download" already flagged for corporate-action
reconstruction (A-catalog C4) and the demerger registry (momentum Part C): budget it as its own
project, gated behind confirming the exchange portals' historical PDF depth actually reaches back
far enough to justify the OCR investment.

**The honest statement for pre-XBRL backtests.** A pre-2017 India value/quality backtest built from
OCR'd PDFs can plausibly recover revenue/PAT/EPS point history reliably (the prescribed-format
regularity helps), and — because the exchange corporate-announcement record itself carries a
submission date even for a PDF-only filing — can plausibly recover a genuine `knowledge_time` for
each filing too. What it **cannot** honestly claim is a clean **restatement record**: before the
XBRL-native "revision remarks" mechanism (§C.1) existed as a structured field, a revised PDF filing
looked identical to a routine one on inspection, and confirming which historical filings were later
revised requires either a company-by-company manual audit or accepting the risk of silently
treating a revision as if it were the original. **Any pre-2017 India fundamentals backtest must
disclose this as an unresolved restatement-completeness gap, not paper over it with confidence
inherited from the cleaner post-2017 regime** — precisely the kind of honesty Known Prior #7 exists
to enforce, extended to the pre-XBRL boundary specifically. The AJV/IIMA India factor library
(momentum Part C §C.6) reaches back to 1994 on **CMIE Prowess** — a paid vendor with its own,
presumably more complete, restatement/vintage handling; our free-data panel cannot claim to match
that depth on equal footing before 2017, and should say so wherever the two are compared (§C.7).

---

## C.6 The interim shortcut and its hazard — screener.in and peers

**What it is.** Screener.in (and similar India retail-analytics sites — Tijori Finance, Trendlyne,
Tickertape) aggregates the same primary filings this Part specifies (BSE's filing repository plus
company annual reports) into a convenient, human-browsable, multi-year P&L/balance-sheet/cash-flow
table per company, with **no public API** — access is via the website itself or a rate-limited
"Export to Excel" feature, and the site's own guidance asks users to make "reasonable-rate
requests" and comply with applicable law when scripting against it **[VERIFY: exact wording of
screener.in's own Terms of Use — not independently retrieved in full this pass; treat the
"reasonable-rate, no public API" characterization as directionally confirmed, not a verbatim
quote]**.

**The hazard, precisely.** Screener (and peers) display **today's best-known, latest-restated**
figures against historical periods — there is no vintage archive, no way to ask "what did this
site show for FY2019 book value back in 2019." Pulling a 10-year fundamentals history from
screener.in **today** and backtesting against it silently reintroduces the exact restatement-
driven look-ahead bias Known Prior #7 prices at 150–450bps/yr, in a *more* concentrated form than
even a careless direct-from-filing pull, because the aggregator has already discarded whichever
vintage information it might once have carried. This is structurally the same failure mode as
trusting "current constituents" for a historical universe (momentum Part C §C.3) or applying
today's ASM/GSM band to a historical date (A-catalog A6/A7) — a snapshot standing in for a
point-in-time record.

**The rule — exploration-only, never evidence, mirroring the Kaggle/HF rule.** The 2026-09-01
mirror-authorization decision (`research/OPEN_QUESTIONS.md`) sets the house discipline for
external, non-primary data: authorized for use, but every pull sha256-manifested, authenticated
against an independent mirror or published fact before use, PIT/vintage caveats recorded, and a
mirror never outranks the primary source once the principal's-machine primary pull exists.
Screener.in and its peers earn the identical treatment, generalized from "third-party mirror of a
primary series" to "third-party aggregator of a primary filing corpus with no vintage layer": fine
for fast exploration (spot-checking a company's rough profile, sanity-testing a candidate signal,
orienting a new analyst), **never as the fixture a backtest is evaluated against**. The house's own
free-data panel — built directly from Reg. 33/23/29/31 filings with `knowledge_time` discipline
(§C.1) — is the only instrument allowed to answer this program's central question (Known Prior
#7); a screener.in-sourced backtest answers a different, easier, silently biased question.
Kaggle/HuggingFace-hosted India fundamentals datasets (several surfaced incidentally in this
pass's searches) inherit the identical rule and the identical access note already on file: both
hosts are blocked at this environment's egress proxy but authorized for the principal's machine
(`ingest/README.md`'s addendum) — same authentication-before-use discipline, not a lighter one
just because the file looks larger or more structured than a screener.in export.

---

## C.7 Validation — two acceptance gates before our constructed ratios are trusted

**Gate 1 — the India factor mirror's HML.** The desk already holds the AJV/IIMA India Fama-French-
momentum data library as the external validation benchmark for momentum (momentum Part C §C.6) and
has pulled its HML series into `value-panel-RESULTS.md` (V1–V4: India HML full-sample +8.6%/yr
ann. mean, 1994–2014 sub-period +7.1%/yr, correlation with WML **−0.37**, five documented India
"value winters," the worst — 1996-02 to 2003-06 — reaching **−59%** peak depth). **Reuse this
exact benchmark, do not build a second one**: reconstruct our own B/P-based long-short decile HML
over AJV's sample window and apply the same acceptance bar momentum Part C proposes for WML —
monthly correlation **≥0.85**, raw (pre-haircut) annualized mean within roughly **65–100% of AJV's
published HML** (a design choice, not literature-sourced, flagged as such there and carried
forward unchanged: a reconstruction landing below the haircut range means a construction gap, not
deeper decay, and must be investigated first). AJV's update cadence (3×/year) may not have stayed
current through 2025–2026 **[VERIFY, same open item as momentum Part C]** — treat any gap past its
last confirmed vintage as un-validated, not assumed-fine.

**Gate 2 — NSE's own daily-published index P/E, P/B, and dividend yield.** NSE publishes these
three ratios **daily**, for every broad-market and sectoral index it maintains, at
`nseindia.com/reports-indices-yield` (current live report) with historical depth described by
multiple independent sources as reaching back to **1999** **[VERIFY exact first-published date —
several secondary sources cite 1999 for Nifty/Sensex-family P/E history but this pass did not
independently confirm NSE's own stated inception date for the specific yield-report series]**; a
mirrored historical file also sits under `niftyindices.com/reports/historical-data` (already
catalogued for TRI pulls, B1–B4). **Cheaper and always-on relative to Gate 1**: unlike AJV's
3×/year library, NSE republishes its own index-level P/E/P/B/dividend-yield figure every trading
day, checkable continuously. The test: at each rebalance date, compute the free-float-cap-weighted
E/P and B/P across our own fundamentals panel, restricted to the point-in-time Nifty 50/500
constituent set (momentum Part C §C.3), and compare against NSE's own published index-level P/E
and P/B for the identical date/index. **Acceptance bar (design choice, flagged as such)**:
aggregate tracking difference within a few percentage points, persistently — a persistent gap
flags a coverage error (missing constituents, mis-held stale book values) or a weighting mismatch,
and must be resolved before the panel is trusted for cross-sectional ranking. This gate validates
the panel's **level**; Gate 1 validates its **cross-sectional discrimination** — complementary,
neither substitutes for the other.

---

## C.8 PIT/vintage hazard table and construction pipeline

| Source | Revision-prone? | Two dates that must never be conflated | Store first-print or latest? |
|---|---|---|---|
| Reg. 33 financial results (quarterly/annual) | **Yes, explicitly** (revised-XBRL mechanism) | Fiscal-period-end vs. `knowledge_time` (announcement/PDF-filing timestamp, §C.1) | **First-print AND every revision**, each its own vintage row keyed by `(company, period, filing_type, knowledge_time)` — never overwrite |
| Reg. 31 shareholding pattern | Format-revision-prone (integrated-filing transition), values not typically restated | As-of-quarter-end vs. filing date (≤21 days) | Latest per quarter; format version tagged (A-catalog C3) |
| Reg. 29/31 SAST (pledge) | Not revision-prone; rule-vintage matters (SAST amended multiple times since 2011) | Event date vs. disclosure date | Append-only event log (A-catalog C1/C2) |
| Reg. 23(9) RPT | Not revision-prone | Half-year-end vs. 30-day-post-publication filing date | Latest per half-year |
| Reg. 30 auditor events | Not revision-prone; event-based | Event date vs. ≤24h disclosure date | Append-only event log |
| CRA rating actions | Not revision-prone; each action is its own record | Rating-committee date vs. ≤7-working-day press-release date | Append-only event log per issuer |
| Screener.in/peer aggregators (§C.6) | **Effectively always stale to the pull date** — no vintage layer exists to store | Pull date only (no published-as-of date recoverable) | Exploration cache only, never a fixture a backtest reads |
| AJV/IIMA HML (validation) | Methodology-revision-prone (per momentum Part C §C.7) | Release-vintage vs. pull date | Every release kept, never only-latest (identical rule, same table row style as momentum Part C) |
| NSE index P/E-P/B-yield (Gate 2) | Not restated | T+0 | Latest — no PIT problem |

**Construction pipeline** (ordered, script-followable, matching momentum Part C §C.8's numbering
convention):

1. **Registry load.** Validate `config/sleeves.yaml factor_book.value`/`.quality` and
   `config/ladder.yaml L8_value_spread` against `config/validator.py` before any pull.
2. **Pull raw Reg. 33/23/29/30/31 filings** into `data/raw/{nse,bse}/financial_results/`,
   `.../rpt/`, `.../pledge/`, `.../auditor_events/`, `.../shareholding_pattern/` — **no existing
   ingest script covers any of this; this Part surfaces the gap** (see closing note below).
   Manifest every file immediately (`python ingest/manifest.py data/`).
3. **Build the XBRL-era parser** (2017-04-01 boundary) and, separately, the **Integrated-Filing
   parser** (2025-04-01 boundary) — two schema versions, per §C.1's table; normalize both into one
   internal fundamentals schema (`company, fiscal_period, filing_type, knowledge_time, field,
   value, is_revision`) before any downstream ratio touches the data.
4. **Apply the `knowledge_time` discipline** (§C.1): every fact enters the panel timestamped by its
   actual filing moment, never by fiscal period-end; a revision lands as a new row, never an
   overwrite.
5. **Build the staircase-holding logic** for half-yearly/annual-only fields (book value, cash flow,
   total assets, total debt, current assets/liabilities — §C.2): hold the last-disclosed value flat
   between disclosure dates; never interpolate a smooth quarterly path.
6. **Compute the ratio panel** per §C.3: E/P and sales/price at quarterly cadence; B/P and CF/P on
   the staircase; EV/EBITDA and gross profitability as explicitly mixed-frequency; exclude
   financials from universe-wide raw pooling, route them to a sector-relative-only P/E-P/B path.
7. **Compute the quality panel** per §C.4: the 2 genuinely-quarterly Piotroski signals at quarterly
   cadence, the 7 balance-sheet/cash-flow-gated signals on the staircase; pledge/RPT/auditor/rating
   governance flags each on their own native event cadence (§C.4's table).
8. **Cross-financials sector-relative ranking**: build the separate banks/NBFC/insurer ranking path
   (§C.3), never pooled with non-financials on a universe-wide percentile.
9. **Validate — Gate 1**: reconstruct the long-short B/P decile HML over AJV's sample window;
   check correlation ≥0.85 and magnitude within 65–100% of AJV's published HML; log any divergence.
10. **Validate — Gate 2**: compare our panel's aggregate E/P and B/P against NSE's own daily
    published index-level P/E and P/B for the same date/index; require a persistently small
    tracking difference before trusting the panel for cross-sectional ranking.
11. **Manifest every derived fixture** (fundamentals panel, ratio panel, quality panel, governance-
    flag panel) as its own versioned, checksummed artifact; corrections append a new vintage row,
    never overwrite — identical WORM discipline to momentum Part C §C.7/§C.8.
12. **Recalibration triggers**: re-run whenever (a) a new AJV/IIMA release lands; (b) a semi-annual
    balance-sheet disclosure round completes (Sept-end, March-end) and the staircase steps; (c) the
    Integrated-Filing schema is itself revised; (d) book AUM moves ±50% (existing `costs.yaml`
    trigger, unchanged).

**Impact on existing ingest scripts (a genuine gap this Part surfaces, not a re-statement of a
known one).** `ingest/README.md` and the existing `ingest/pull_*.py` scripts (bhavcopy, AMFI, FRED,
indices, NSDL FPI) cover **price, macro, and flow data only** — there is currently **no script for
company fundamentals at all**: no `pull_nse_financial_results.py`, no RPT/pledge/auditor-event
puller, no XBRL parser for either schema era. This is a materially larger gap than the two
momentum Part C already flagged (BSE bhavcopy puller, BSE/NSE corporate-actions puller) since
nothing here has even a stub — the fundamentals ingest kit for the moderate book's factor engine
must be built from this Part's specification, not patched from an existing script. Recommend
adding to `ingest/README.md`'s day-1 runsheet: a new `pull_nse_financial_results.py` (Reg. 33,
both schema eras), a `pull_nse_governance_events.py` (Reg. 23/29/30/31 combined, since they share
the same corporate-filings-portal family and access pattern), and the XBRL-to-internal-schema
parser as its own module, versioned separately per §C.1's schema-era table.

---
*End of Part C. Cross-references: `docs/masterplan/A-data-catalog.md` (no fundamentals block —
this Part is the first), `research/cycles/momentum-deep/partC-data.md` (bhavcopy/CA/survivorship
mechanics reused, not duplicated), `research/cycles/value-deep/value-panel-RESULTS.md` (India HML
mirror figures, §C.7 Gate 1), `research/dossiers/02-value-quality-lowvol.md` (theory/evidence/decay
this Part builds data for), `config/ladder.yaml` L8, `config/sleeves.yaml
factor_book.value`/`.quality`, `research/OPEN_QUESTIONS.md` (mirror-authorization note, applied to
screener.in/peers in §C.6), `research/CONTRACT.md` §3 (free-source mandate), Known Prior #7
(restatement bias), §8 (no fundamental backtest without its price-only counterpart — already
satisfied for momentum by its price-only WML; this Part's value/quality construction must be
paired against a price-only counterpart the same way before either is reported).*
