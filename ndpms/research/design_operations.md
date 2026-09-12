# NDPMS ₹500 Cr Mandate — Governance, Operations, Technology, Data and Automation

Status date: 12 September 2026. This note is the operating-model layer that sits under the regulatory design note (mandate architecture, Reg 24/31 perimeter, LVAI route, consent legal structure) [R1], the allocation note (CMAs, sleeve weights), the selection note (instrument due diligence) and the rebalancing/risk/performance notes (monthly cycle, band design, TWRR/attribution) already produced for this mandate. Figures here reuse those documents' ₹500 Cr sleeve weights, consent SLA and cadence so all six notes tie out. Where a fact is SEBI/RBI-sourced it carries the bracketed source used in the regulatory note (re-verified here); house-specific numbers (FTE, cost, dashboard refresh) are our own design and marked "approx." where not independently verifiable.

**Design thesis.** NDPMS moves the cost of ownership from *decision* to *process*: the PM cannot out-trade the market with speed, so alpha must come from house-view quality, tax/cost discipline and low consent-friction execution — and the team must be able to *prove*, at every stage, that the client directed each trade (Reg 24/2 read together) [R1][1]. Everything below is built to make that proof cheap and the friction small.

---

## 1. Governance

### 1.1 Investment Committee (IC) — composition and mandate
Six voting members, quorum 4, at least one non-investment (compliance/risk) vote required for quorum: CIO (chair), Head of Research/PM for the mandate, Head of Risk, Head of Compliance, Head of Trading/Ops (non-voting, present for feasibility), one independent/senior advisor (non-executive, tie-break). The IC owns: house view sign-off, model-portfolio version approval, Rebalance Proposal Pack (RPP) approval before it goes to the client, watchlist/exception decisions, and the quarterly IC scorecard (defined in the performance note) [R1].

### 1.2 Calendar

| Cadence | Forum | Agenda | Output |
|---|---|---|---|
| Monthly (last Wed) | IC house-view meeting | Macro/pillar scorecard review, SAA drift vs bands, TAA tilt (±2 discretion band per the allocation note), RPP draft review | Signed house view memo; RPP v0 |
| Monthly (T-3, 2 biz days later) | Pre-RPP compliance gate | Reg 24 unlisted/associate checks, pre-trade compliance, cost/tax estimate | RPP v1 (client-ready) |
| Weekly (Mon/Thu) | Ops stand-up | Deployment tranche status, cash ladder, corporate actions, recon breaks | Break log update |
| Weekly | Risk stand-up | VaR/drawdown vs limits, early-warning board, hedge book status | Risk flag list |
| Quarterly | IC scorecard + manager review | Attribution vs benchmark, cost/tax drag, active-manager watchlist scoring | IC scorecard; manager actions |
| Quarterly | Compliance/Audit | Reg 24 associate-limit audit, AML/KYC refresh sample, standing-instruction usage audit | Audit note |
| Annual | Firm-level performance audit (APMI ToR) | Full NDPMS book audit, confirmation to SEBI within 60 days of FY-end | Audit report to SEBI [R1] |
| Ad hoc (≤4h notice) | Tail-event IC | Any daily risk breach (Section 2 of the risk note) or client-unreachable escalation | Emergency directive log |

### 1.3 Decision log and IPS document structure
Every IC decision is logged with: date, decision ID, members present, motion, vote, dissent (if any), rationale (1 paragraph), effective date, and linked artifact (model version hash, RPP ID). Retained 8 years minimum (aligns with SEBI recordkeeping practice under the PMS Regs) [R1]. IPS document structure for this mandate (single master PDF + machine-readable YAML twin for the pipeline):

1. Client identity, accreditation status (LVAI certificate ref, validity date), minimum-investment confirmation.
2. Objective, horizon, risk profile, liquidity needs, ESG/exclusion list (if any).
3. Strategic Asset Allocation table — sleeve, target %, band, ₹ Cr at ₹500 Cr (from the allocation note).
4. Benchmark: house composite for the mandate + per-sleeve reference index.
5. Consent Protocol (Annex B of the agreement) — RPP format, SLA, standing-instruction register.
6. Eligible-universe and hard-limit table (unlisted 25%/LVAI 100%, associate 15/25/30%, derivative exposure ≤ portfolio funds) [R1].
7. Fee schedule, HWM definition, exit-load schedule.
8. Reporting pack list and cadence.
9. Version history (semantic version, e.g. IPS v1.3; every SAA/band change is a new minor version, IC-approved, client-notified).

### 1.4 Model-portfolio governance and version control
Model Master (existing house artifact) gets an NDPMS-specific branch: `model/ndpms-500cr-moderate-vX.Y`. Every change — CMA update, sleeve reweight, new fund added to the eligible list — is a pull-request-style change: proposed by PM, reviewed by Risk, approved by IC, tagged with effective date, diffed against prior version in the recon pipeline (Section 4) so drift reports always compare against the *currently effective* version, not a stale one. Version changes >1 percentage point on any sleeve require full IC minute; <1pp (rebalancing within band) is logged but not re-voted.

### 1.5 Conflicts policy — group products
Angel One group products (AMC schemes, group AIF/SIF, Angel One as broker) sit under a standing conflicts protocol, not case-by-case waivers:
- One-time client consent at onboarding in the prescribed Annexure A format for associate investment, refreshed if the associate list changes [R1][4].
- Self-imposed IPS cap 10% of AUM per associate product family (tighter than the SEBI 15/25/30% ceiling) [R1][4].
- IC best-selection minute required every time a group product is chosen over a non-group alternative — must show the group product scored ≥ the top 2 non-group alternatives on the relevant due-diligence scorecard (selection note).
- Angel One as executing broker: brokerage must be demonstrably at or below the rate card available to a non-group client of similar size; quarterly best-execution report benchmarks our achieved slippage against a TCA (transaction-cost-analysis) peer set.
- Real-time alert (not monthly review) the moment any associate exposure crosses 80% of its cap — 2022 SEBI amendment requires alert-based monitoring [R1][4].

### 1.6 Four-eyes controls
| Control point | Maker | Checker | Tooling |
|---|---|---|---|
| RPP trade list | PM/Analyst | Compliance (pre-trade) | OMS compliance rule engine |
| Order entry | Dealer | Second dealer / Ops (input match to RPP) | OMS 2-factor release |
| Standing-instruction trigger | System (automated) | Ops (daily exception report) | RMS batch job |
| Cash movement / RTGS | Ops | CFO/Fund accountant | Custodian dual-authorization |
| NAV/valuation override | Fund accountant | Risk/Compliance | Valuation exception log |
| Model version change | PM | IC + Risk | Git-style model versioning |
| Client consent capture | RM | Compliance (audit trail hash check) | e-sign platform log |

---

## 2. NDPMS consent workflow

### 2.1 Design principle
Under NDPMS the client's dated, evidenced instruction is the *only* thing that authorises a trade (Reg 24 read with Reg 2 definitions) [R1][1]. The workflow below turns that into one omnibus monthly approval instead of per-trade friction, while keeping every element specific enough that it is a direction, not a discretion (SEBI's 26-May-2026 order against First Global — outsourcing/discretion recharacterisation risk is real and enforced) [R1][12].

### 2.2 Proposal-pack (RPP) template — contents
1. Cover: client name, account, IPS version referenced, month, IC house-view summary (3 lines).
2. Drift table: current vs target weight per sleeve, band status (green/amber/red).
3. Trade list: ISIN/scheme code, instrument name, side, quantity **or** ₹ amount, execution window (dates), participation-rate rule, limit-price/NAV-cutoff rule, rationale (1 line), estimated cost (bps), estimated tax impact (STCG/LTCG flag).
4. Compliance annex: unlisted-cap headroom before/after, associate-exposure headroom before/after, derivative notional check.
5. Cost/tax summary: total estimated transaction cost (₹), estimated tax drag (₹), net expected benefit of the rebalance.
6. Consent block: "Approve all" single click, or line-item approve/reject with a mandatory reason if rejecting; validity window (10 trading days, then lapses — new pack required) [R1].
7. Signature block: e-sign (Aadhaar eSign/DSC) or OTP-authenticated portal click-through, each with device/IP/timestamp metadata.

### 2.3 Digital consent mechanism — design and legal basis
- **Primary channel**: client web/app portal, Aadhaar e-Sign (Section 3A, IT Act 2000, recognised electronic signature) or class-2/3 DSC for HUF/trust/corporate signatories; SEBI's digital-onboarding circular (effective 1-Oct-2024) permits fully digital PMS onboarding and consent artifacts [R1][8].
- **Secondary/fallback channel**: OTP-authenticated email reply from the registered email ID on file, OTP sent to the registered mobile — used only when the portal is unavailable; logged with a distinct "fallback channel used" flag for audit.
- **Tertiary (escalation only)**: recorded voice call (Section 2.5) — used solely for the "client unreachable in a tail event" path, never as the default channel.
- Every consent event writes an immutable record: `{rpp_id, client_id, line_items[], approve/reject, channel, timestamp (IST, NTP-synced), signer_identity, IP, device_fingerprint, document_hash (SHA-256 of the exact RPP PDF shown)}`. Store in an append-only ledger (WORM S3-equivalent object lock or a hash-chained table) — this is the audit trail an inspection will pull.
- **Retention**: minimum 8 years (aligned to SEBI recordkeeping norms under the PMS Regs and IT Rules); we recommend 10 years given the mandate size.

### 2.4 SLA and escalation

| Stage | Target | Escalation trigger | Action |
|---|---|---|---|
| RPP sent → client viewed | 4 business hours | Not viewed by T+1 | RM call |
| Client viewed → approved/rejected | ≤ 2 business days (per regulatory note's latency-cost model) | Not actioned by 48h | RM call + CIO email |
| No response | 72h | — | Escalation call from CIO; if still unreachable, invoke Section 2.5 |
| Rejected line items | Same day | — | PM revises, re-issues affected lines only (partial RPP) within 1 business day |
| Consent expiring (day 8 of 10) | — | 2 days before lapse | Auto-reminder; unexecuted lines lapse automatically at day 10 [R1] |

Quantified rationale: a 5% (₹25 Cr) equity under/over-deployment at ~1% daily index vol costs approx. ₹79 lakh of 1-sigma tracking risk over 10 days of delay vs approx. ₹35 lakh over 2 days — this is why the 2-business-day SLA is the design target, not a courtesy (regulatory note, Section 5.2) [R1].

### 2.5 Client unreachable during a tail event
1. Attempt all three channels (portal push, OTP email/SMS, recorded call) at T, T+4h, T+24h.
2. If a **standing instruction** already covers the situation (e.g., "auto-de-risk equity by X% if house VaR breach persists 2 consecutive days" — pre-approved, mechanical, revocable), execute it and notify the client on all channels simultaneously; log as a standing-instruction execution, not a fresh consent.
3. If no standing instruction covers it and the client remains unreachable beyond 72 hours during a live tail event: the IC convenes an emergency session, documents the risk (VaR/drawdown numbers from the risk note's early-warning board), and may take a **defensive, capital-preserving, reversible-only** action (e.g., buying an index put, moving to already-approved liquid sleeve **only up to the standing sweep limit**) under the narrowest possible reading of pre-existing consent; anything broader is refused and logged as "unable to act — no client instruction," which is the compliant position, not a failure, under Reg 24 [R1][1]. This boundary should be reviewed with external counsel/an SEBI Informal Guidance request before go-live — status: unclear_verify (regulatory note flags the same open point) [R1].
4. Every unreachable-client event, action taken (or not taken) and its rationale go into the decision log (Section 1.3) and are disclosed to the client in the next monthly report.

### 2.6 Standing-instruction design (narrow, mechanical, revocable — carried from the regulatory note) [R1]
| # | Instruction | Trigger | Instrument/quantity rule | Max ₹ | Revocable |
|---|---|---|---|---|---|
| 1 | Cash sweep | Idle cash > ₹50 lakh, daily | Named liquid/overnight fund, 100% of excess | Uncapped (mechanical) | Yes, portal toggle |
| 2 | Distribution reinvestment | Dividend/interest received | Same instrument or liquid fund per pre-set rule | Amount received | Yes |
| 3 | Corporate-action default | Voluntary CA (rights/buyback) | Default = no action unless in an approved RPP | — | Yes |
| 4 | Approved tranche execution | Already-approved RPP line | Exact ₹/qty from RPP, Mon/Thu cadence | As per RPP | Auto-lapses at RPP expiry |
| 5 | Hedge auto-roll | Approved hedge nearing expiry | Same notional, next monthly series | ≤ 1% AUM premium budget/yr | Yes |
| 6 | Tail de-risk (if adopted) | 2-day sustained VaR/drawdown breach per risk note | Reduce equity sleeve by pre-agreed X pp to a pre-agreed floor | Pre-agreed ₹ ceiling | Yes, reviewed quarterly |

Anything that changes a sleeve's *target* weight or introduces a new security stays in the RPP — standing instructions never expand scope, they only execute what's already been directed.

### 2.7 Recording and storage
- Voice: call-recording system (telephony compliance recorder) retaining WAV + transcript, indexed by client ID and RPP ID, 8-year retention.
- Documents: RPP PDFs, signed consent artifacts, and IC minutes in a document-management system with version control and legal hold capability.
- Backup: daily encrypted backup of the consent ledger to a separate cloud region; monthly integrity check (hash re-verification of a sample of records).

---

## 3. Order and portfolio management (OMS/RMS)

### 3.1 Multi-instrument book — routing map

| Instrument class | Execution venue/route | System of record | Settlement |
|---|---|---|---|
| Listed equity, ETFs | Exchange (NSE/BSE) via broker OMS, algo/DMA for size | OMS → demat (client-name) | T+1 |
| Direct MF (incl. index, active, SIF) | MFU (MF Utility) or BSE StAR MF, direct-plan flag mandatory [R1] | OMS/MF order module → RTA folio | T+1 (equity)/T+1-2 (debt) |
| AIF Cat I/II/III | Subscription via contribution agreement + drawdown notices; no exchange | Manual/portal subscription tracker, capital-call calendar | Per PPM (T+3 to T+10 typical, approx.) |
| Bonds/G-secs/SDLs/corp bonds | NSE/BSE RFQ platform (for retail-lot corp bonds), NDS-OM/RFQ (G-sec, via custodian/PD), direct placement for large lots | OMS bond module | T+1/T+2 |
| Third-party PMS | Outside NDPMS OMS — client signs directly with the external PM; we track via a consolidated-reporting feed only | Consolidated reporting DB (look-through) | N/A to our book |
| REIT/InvIT (listed) | Exchange | OMS | T+1 |
| Gold/silver ETF, SGB (secondary) | Exchange | OMS | T+1 |
| International (Indian-listed ETF/FoF) | Exchange/AMC, premium-to-iNAV check pre-trade | OMS | T+1/T+3 (FoF) |

### 3.2 OMS/RMS requirements
- **Pre-trade compliance engine**: hard-coded rules for (a) unlisted-cap headroom (25% NDPMS / self-cap 15% IPS), (b) associate-exposure headroom (15/25/30% SEBI / 10% IPS), (c) derivative notional ≤ portfolio funds, (d) no short sale, (e) no leverage/margin, (f) MF direct-plan flag, (g) demat-account routing (purpose-segregated accounts per the rebalancing note's FIFO design). Every order blocked by a rule requires an explicit compliance override with a logged reason — never a silent bypass.
- **Order timestamping**: order placement, release, exchange ack, fill — all NTP-synced, immutable log; SEBI's Master Circular requires time-stamping and (for AUM ≥ ₹1,000 Cr) an automated OMS — at ₹500 Cr we are below that automatic threshold but build to the same standard from day one since we intend to scale and because the audit trail is the actual defence for NDPMS [R1][3].
- **Linkage to consent**: every order in the OMS carries an `rpp_id` (or `standing_instruction_id`) foreign key; an order cannot be released without a valid, unexpired, matching consent record — this is the single most important control in the whole book.
- **AIF/PMS-sleeve tracker**: not an OMS object (no exchange order) but a capital-call and NAV tracker with drawdown notices, capital-call SLA (typically 10 business days, approx., per PPM), and a rolling "committed vs called vs distributed" ledger (for IRR/DPI/TVPI computation on the AIF sleeve).
- **RMS**: real-time position and exposure limits feeding the risk note's daily VaR/drawdown/liquidity metrics; hard block on any order that would breach a hard limit (associate cap, unlisted cap, derivative notional) at the RMS layer, independent of the OMS pre-trade check (defence in depth).

### 3.3 Custodian selection and fund accounting
- Custodian is mandatory for PMs (and mandatory before any commodity-derivative use) [R1][3]. Selection criteria: SEBI-registered custodian with PMS/AIF servicing experience, NAV computation SLA, corporate-action processing SLA, API/SFTP connectivity for the daily data pipeline (Section 5), and independence from Angel One group (avoids a second-order conflict).
- Fund accounting: daily NAV computation (T+1 morning), reconciled against the recon engine (Section 4); accrual-basis fee computation (management fee daily accrual, performance fee at HWM crystallisation dates).
- Cost: custodian + fund-accounting fees run approx. 3–8 bps p.a. of AUM in the Indian market for a book this size and complexity (industry-typical range; not independently verified for a specific vendor quote) — on ₹500 Cr that is approx. ₹15–40 lakh/yr, consistent with the regulatory note's operating-expense-cap illustration (0.50% cap = ₹2.50 Cr/yr ceiling, custody a sub-component) [R1].

### 3.4 Brokerage arrangement — Angel One as broker
Governed by the conflicts policy (Section 1.5): brokerage at actuals, rate card benchmarked quarterly, best-execution TCA report to the IC, and a standing option (disclosed to the client) to route a minority of flow through a second, non-group broker for benchmarking — recommended at ≥10% of listed-equity flow in year 1 purely as a TCA control, reviewed after 6 months.

---

## 4. Reconciliations

### 4.1 Recon matrix

| Recon | Frequency | Compares | Break SLA (resolve by) | Escalation |
|---|---|---|---|---|
| Cash (bank vs internal ledger) | Daily (T+1 AM) | Custodian bank statement vs OMS/ledger cash position | Same day for >₹10 lakh breaks; T+1 for smaller | Ops lead → CFO if unresolved 2 days |
| Holdings (custodian/depository vs internal book) | Daily | CDSL/NSDL statement + custodian holding file vs internal position | Same day | Ops → Compliance if >₹25 lakh or >2 days |
| MF folios vs RTA | Daily (CAMS/KFintech feed) | Folio-level units/NAV vs internal MF ledger | T+1 | Ops → RTA helpdesk ticket; escalate at T+3 |
| AIF statements | Monthly (per fund's NAV statement) | Units/NAV/capital account vs internal AIF tracker | 5 business days of receipt | PM → fund's investor-relations desk |
| Corporate actions | Daily (announcement) / on ex-date | Depository CA feed vs entitlement computed vs credited | T+1 of ex-date; T+3 of credit due date | Ops → custodian if credit delayed |
| Dividends/interest | Daily | Bank credit vs entitlement | T+2 | Ops |
| Fee accruals | Daily (mgmt fee), event-driven (perf fee/HWM) | Computed accrual vs custodian/fund-accountant statement | Monthly close, T+3 | Fund accountant → Compliance |
| Benchmark data | Daily | NSE Indices/AMFI feed vs internal benchmark series | T+1 | Data team |
| Composite/model deviation (extends existing house cash-recon skill) | Monthly (+ weekly interim) | Actual weights (Portfolio Appraisal) vs Model Master IPS targets, composite rules (FI+ESS caps etc.) | Per existing house SLA | PM/Ops |
| IPS drift / allocation vs model (extends existing IPS dashboard) | Daily compute, published weekly | Client-level allocation vs model + band | Amber at band edge, red flag to IC same day | PM |
| Deployment tranche tracking (extends existing deployment tracker) | Weekly (Mon/Thu cadence) | Planned tranche vs executed | Same week | Trading desk |
| Attribution/TWRR (extends existing attribution dashboard) | Monthly | Computed TWRR/contribution vs custodian-confirmed valuations | T+5 business days of month-end | PM/Risk |

### 4.2 Break-resolution workflow
Every break gets a ticket: `{recon_type, date, amount, ageing, assigned_to, root_cause_category, resolution, closed_date}`. Root-cause categories: timing (T+1 lag), corporate action unprocessed, trade-booking error, RTA/custodian data error, FX/valuation source mismatch. Weekly break-ageing report to Ops head; any break >₹25 lakh or aged >5 business days escalates to Compliance and appears on the monthly IC pack. This mandate's size (₹500 Cr, multi-instrument) means the existing single-strategy cash-recon automation needs three extensions: (i) an AIF/capital-call ledger it doesn't currently carry, (ii) a bond/G-sec settlement leg, (iii) a look-through line for the third-party PMS sleeve (reported, not reconciled, since it sits outside our custody).

---

## 5. Data architecture

### 5.1 Feeds

| Data | Source | Frequency | Format/access |
|---|---|---|---|
| Equity/ETF prices, indices (Nifty 50 TRI, Nifty Arbitrage, sector indices) | NSE/BSE, NSE Indices | EOD (+ intraday for risk) | Bhavcopy/API, licensed index-data feed |
| MF NAVs | AMFI | Daily (post ~9 PM IST) | AMFI NAVAll.txt / API |
| AIF NAV/capital statements | Fund administrator/AMPI-empanelled valuer | Monthly (some quarterly) | PDF/Excel, manual ingest |
| Debt valuation (bonds, G-secs, SDLs, MM) | APMI-empanelled valuation agencies (CRISIL, ICRA Analytics, NSE Indices) | Daily | File feed [R1][32] |
| G-sec/SDL trade & yield data | CCIL (NDS-OM, F-TRAC), RBI | Daily | CCIL data feed |
| FX, gold/silver reference | RBI reference rate, MCX/LBMA-linked domestic benchmark | Daily | RBI/MCX feed |
| Overseas index/ETF data (for international sleeve) | Index provider + Indian-listed ETF iNAV | Daily | Vendor feed |
| Corporate actions | Depository (CDSL/NSDL) CA file, exchange announcements | Daily | Depository API |
| Benchmark constituents (Nifty 50 TRI, Nifty Arbitrage) | NSE Indices | On rebalance (semi-annual/quarterly per index methodology) | NSE Indices file |
| Custodian holdings/cash/transactions | Custodian | Daily (EOD) | SFTP/API |
| RTA (MF folios) | CAMS/KFintech | Daily | RTA API/file |
| Regulatory reference (SEBI/APMI circulars, accreditation registry) | SEBI/APMI/registered accreditation agencies | Event-driven | Manual monitoring + periodic pull |

### 5.2 Pipeline design (Python) — ingest → validate → compute → publish

```
01:00 IST  Ingest: pull AMFI NAV, NSE/BSE bhavcopy, custodian EOD file, RTA feed,
           APMI debt valuation, CCIL G-sec data, corporate-action file, FX/gold ref.
01:30 IST  Validate: schema check, stale-file check (flag if a feed hasn't updated),
           cross-check custodian holdings vs internal ledger row counts, NAV
           day-over-day change outlier flag (>X% move on a debt instrument = alert).
02:00 IST  Compute: daily TWRR (per client, per sleeve, per composite benchmark),
           IPS drift %, VaR/drawdown/liquidity metrics (risk note engine),
           recon break detection (Section 4), fee accrual roll-forward.
02:30 IST  Publish: regenerate HTML dashboards (static build, house pattern —
           same pipeline family as the existing IPS-monitoring, attribution/TWRR
           and deployment-tracker dashboards), push to internal hosting
           (GitHub Pages / internal static host per house convention), archive
           the day's computed dataset (parquet/CSV) to the data lake.
06:30 IST  Ops desk pre-market check: recon exceptions, corporate-action
           calendar, cash ladder for the day's Mon/Thu tranche if applicable.
09:00 IST  Market open — trading desk executes any approved-and-live RPP lines
           per participation-rate rules (rebalancing note, Section 6).
17:00 IST  Post-close: fills reconciled into OMS, T+1 settlement queue built.
```

### 5.3 Storage
- Transaction/holdings store: append-only ledger (client_id, instrument, date, qty, price, side, rpp_id/standing_instruction_id) — this FK to consent is the schema's defining feature for NDPMS.
- Time-series store for prices/NAVs/benchmarks (columnar, e.g., parquet on object storage) — cheap, fast for the daily compute job.
- Document store for RPPs, consent artifacts, IC minutes (Section 2.7).
- All PII (client identity, KYC, accreditation certificates) segregated with access control distinct from the market-data/compute layer.

### 5.4 Dashboard hosting
Same pattern as the house's existing HTML dashboards (IPS monitoring, attribution/TWRR, deployment tracking): static HTML regenerated by the daily/monthly pipeline job, hosted internally (GitHub Pages-equivalent or internal static host), access-controlled to the IC/Ops/Compliance/RM group; client-facing extracts are a separate, simplified, branded export (house palette navy #16233B / indigo #1B27A3 / green #1E9E6A / coral #E0402F / amber #F2A93C) generated from the same computed dataset, not re-keyed.

---

## 6. Dashboards portfolio

| Dashboard | Purpose | Owner | Refresh | Audience |
|---|---|---|---|---|
| IPS/allocation drift (extends existing IPS dashboard) | Actual vs model weights, band breaches, composite-rule checks | PM/Ops | Daily compute, published weekly | IC, Ops, Compliance |
| Deployment tracker (extends existing) | Mon redemption/Thu deployment tranche status for fresh ₹500 Cr and ongoing flows | Trading desk | Weekly | IC, Ops |
| Attribution/TWRR (extends existing) | Brinson-Fachler contribution, alpha vs benchmark, cost/tax drag | PM/Risk | Monthly | IC, RM (client extract) |
| Tail-risk dashboard (new — per risk note Section 8) | VaR/drawdown vs limits, stress scenarios, early-warning board, hedge book | Risk | Daily | IC, Risk, CIO |
| Liquidity dashboard (new) | Days-to-liquidate by sleeve, AIF lock-up/redemption-window calendar, cash ladder | Ops/Risk | Weekly | IC, Ops |
| Consent tracker (new) | RPP status (sent/viewed/approved/rejected/lapsed), SLA breach flags, standing-instruction execution log | Compliance/RM | Daily | Compliance, RM, IC |
| Cost/tax dashboard (new) | Realised transaction cost bps, tax drag (STCG vs LTCG), fee accrual vs cap | PM/Fund accountant | Monthly | IC, CFO |
| Manager watchlist (new) | Active MF/PMS/AIF manager scorecard vs hurdle, style drift, redemption-notice status | PM/Research | Quarterly | IC |
| Reconciliation break board (new) | Live break count/ageing across all 10 recon types (Section 4) | Ops | Daily | Ops, Compliance |
| Corporate-action calendar (new) | Upcoming CAs, election deadlines, default-instruction status | Ops | Daily | Ops, PM |
| Client consolidated view (new, client-facing) | Look-through across NDPMS AUM + third-party PMS sleeve + LRS/IFSC sleeve advised outside AUM | RM | Monthly | Client |

---

## 7. Team and RACI

### 7.1 Roles and approx. FTE for ₹500 Cr NDPMS (single large mandate, multi-instrument)

| Role | FTE (approx.) | Core responsibility |
|---|---|---|
| CIO / IC chair | 0.2 (shared) | House view, IC chair, accountability for alpha |
| PM (dedicated) | 1.0 | Model portfolio, RPP authoring, manager selection |
| Research analyst | 1.0 | NIFTY-750 scorecard, manager/AIF due diligence, macro pillar |
| Risk manager | 0.5 | VaR/drawdown, limits, stress testing, hedge design |
| Trading/dealing desk | 1.0 | Order execution across venues, participation-rate discipline |
| Ops/fund accounting | 1.5 | Recon (Section 4), NAV oversight, corporate actions, custodian liaison |
| Compliance officer | 0.5 (dedicated slice of a shared role) | Pre-trade checks, associate-limit monitoring, consent-audit, SEBI/APMI reporting |
| RM/client servicing | 0.5–1.0 (depends on # of underlying entities in the mandate) | Consent walkthroughs, escalations, client reporting |
| Data/pipeline engineer | 0.5 (shared across house dashboards) | Daily pipeline, dashboard builds |
| **Total** | **≈ 6.7–7.2 FTE** | — |

At ₹500 Cr this is a rich staffing ratio (approx. ₹70 Cr AUM/FTE) versus a typical scaled PMS book (₹150–300 Cr/FTE, approx.) — justified in year 1 by the build effort (Section 9) and the multi-instrument/NDPMS consent overhead; expect the ratio to improve as automation matures and if a second mandate is onboarded onto the same infrastructure.

### 7.2 RACI (abbreviated — key activities)

| Activity | CIO | PM | Risk | Ops | Compliance | RM |
|---|---|---|---|---|---|---|
| House view / IC sign-off | A | R | C | I | C | I |
| RPP authoring | I | R/A | C | I | C | I |
| Pre-trade compliance check | I | C | I | I | R/A | I |
| Consent capture/SLA tracking | I | I | I | C | A | R |
| Order execution | I | C | I | R/A | I | I |
| Daily recon | I | I | C | R/A | I | I |
| Daily risk monitoring | I | C | R/A | I | I | I |
| Tail-event escalation | A | R | R | C | C | R |
| Monthly client report | I | C | I | R | A | R |
| SEBI/APMI monthly filing | I | I | I | C | R/A | I |
| Model version change | A | R | C | I | C | I |

### 7.3 Operating calendar (summary)
Daily: recon (all 10 types), risk monitoring, cash/CA processing, NAV oversight, consent-tracker check. Weekly: deployment tranches (Mon/Thu), ops/risk stand-ups, break-ageing report. Monthly: IC house view + RPP cycle (Section 2), client reporting, SEBI/APMI filing, cost/tax dashboard, attribution/TWRR refresh. Quarterly: IC scorecard, manager watchlist review, compliance/audit review, best-execution TCA review. Annual: firm-level performance audit, IPS full review, accreditation re-certification check, BCP drill (Section 8).

---

## 8. Controls, incident, BCP and client communication

### 8.1 Error-trade policy
Any trade executed without a valid matching consent record, or outside RPP-specified parameters (wrong quantity/side/instrument), is an error trade: (i) immediate freeze of the position, (ii) same-day disclosure to the client with proposed remedy (unwind at no cost to client, or ratify if the client prefers to keep it and it's within their interest), (iii) root-cause logged, (iv) reported to Compliance/IC within 24 hours, (v) if the loss is borne by the firm, booked to a segregated error-account, never netted against client P&L.

### 8.2 Incident and BCP playbooks
- **System outage (OMS/custodian feed down)**: fallback to manual order slips with dual sign-off, custodian direct-dial confirmation; no RPP execution proceeds without the compliance engine's checks being replicable manually from the last-validated dataset.
- **Data feed failure (NAV/price)**: use prior-day validated value with a flag, do not publish a dashboard on stale-but-unflagged data; if AIF/RTA feed is late, hold the recon open rather than guess.
- **Key-person unavailability**: documented delegation of authority (PM → designated backup PM; Compliance officer → designated backup) for RPP approval-gate sign-off, refreshed quarterly.
- **Cyber/consent-ledger integrity incident**: immediate read-only lockdown of the consent ledger, forensic hash-verification against the last known-good backup, client notification per the incident-response SLA (target: within 72 hours, aligned to typical breach-notification practice).
- **BCP drill**: annual, simulating a T0 tail event plus simultaneous custodian outage; measures time-to-restore trading capability and time-to-notify clients.

### 8.3 Client communication cadence and documents
| Document | Cadence | Trigger |
|---|---|---|
| RPP | Monthly (+ ad hoc for event-driven rebalances per the rebalancing note) | House-view cycle |
| Monthly portfolio statement (Reg 31 content, monthly not quarterly by our own commitment) | Monthly | Month-end |
| Tail-event notification | Ad hoc | Risk breach / unreachable-client protocol |
| Quarterly review call | Quarterly | Calendar |
| Annual review + IPS refresh | Annual | Calendar / material change |
| Cost & tax summary | Annual (ahead of ITR season) | March/April |
| Disclosure Document update notice | On material change | Filed change |

---

## 9. Build roadmap, build-vs-buy and cost

### 9.1 Roadmap

| Phase | Days | Deliverables | CAN/SHOULD/AVOID |
|---|---|---|---|
| 0–30 | Legal/compliance foundation | LVAI agreement + all annexes signed; custodian selected and onboarded; OMS pre-trade compliance rules configured; consent-ledger schema live (even if UI is manual/email-based initially) | MUST/SHOULD |
| 0–30 | Data foundation | Daily feed ingestion (AMFI, NSE, custodian) live; existing house dashboards (IPS, attribution, deployment tracker) extended with a placeholder NDPMS/AIF/bond ledger | SHOULD |
| 30–90 | Consent portal v1 | E-sign/OTP RPP workflow live (even a lightweight portal beats email-only); consent tracker dashboard; standing-instruction register configured | MUST |
| 30–90 | Risk & recon build-out | Tail-risk dashboard live; AIF capital-call ledger; bond/G-sec settlement leg added to recon | SHOULD |
| 30–90 | First live monthly cycle | Run one full RPP → consent → execution → recon → report cycle end-to-end, dry-run audited by Compliance | MUST |
| 90–180 | Automation maturity | Full daily pipeline (Section 5.2) automated, dashboards auto-publish; manager watchlist scorecard live; best-execution TCA report automated | SHOULD |
| 90–180 | Scale-readiness | Documented BCP, completed first drill; process ready to onboard a second NDPMS mandate on the same infrastructure | COULD |

### 9.2 Build-vs-buy

| Component | Build vs Buy | Rationale |
|---|---|---|
| OMS/RMS core | Buy (licensed OMS with PMS/multi-instrument support) + build compliance-rule layer on top | Exchange connectivity/algo execution is a solved problem; the Reg-24 rule engine and consent-FK linkage is our IP |
| Custodian/fund accounting | Buy (SEBI-registered custodian) | Mandatory, specialised, regulated function |
| Consent/e-sign platform | Buy (e-sign API, e.g. Aadhaar eSign/DSC provider) + build the RPP workflow/UI in-house | Signature legality needs a licensed provider; workflow logic is house-specific |
| Dashboards (IPS, attribution, deployment, risk, consent) | Build | Already the house's core competency (existing HTML dashboard family); extending is cheaper than buying a generic BI tool that won't encode Reg-24/IPS logic |
| Data pipeline (ingest/validate/compute/publish) | Build (Python, on top of existing house pipeline pattern) | Same reasoning; also the fastest path to daily VaR/TWRR specific to this mandate |
| Recon engine | Build (extend existing cash-recon automation) | House already owns this; extending beats a generic recon SaaS for the composite-rule logic |
| AIF/PMS capital-call and look-through tracker | Build (spreadsheet/lightweight app v1, proper module by day 90) | Low transaction volume, high specificity; not worth a vendor contract at this scale |
| CRM/client portal | Buy or extend existing RM tooling | Not core IP |

### 9.3 Indicative annual cost (₹ lakh/yr, approx. — order-of-magnitude, not vendor-quoted)

| Item | ₹ lakh/yr (approx.) | Basis |
|---|---|---|
| Custodian + fund accounting | 15–40 | 3–8 bps × ₹500 Cr (Section 3.3) |
| OMS/RMS licence | 15–35 | Mid-tier multi-asset OMS for a book this size, India market, approx. |
| E-sign/consent platform | 3–8 | Per-transaction e-sign API cost at monthly RPP volume |
| Data feeds (index/benchmark licences, valuation agency, CCIL) | 10–20 | APMI-empanelled valuation + index data licence, approx. |
| Data/dashboard engineering (0.5 FTE-equivalent + hosting) | 8–12 | Internal allocation, approx. |
| Team (6.7–7.2 FTE, blended fully-loaded cost approx. ₹18–25 lakh/FTE) | 120–180 | Section 7.1 |
| Audit/legal (annual performance audit, LVAI documentation, Informal Guidance if sought) | 8–15 | APMI ToR audit + counsel |
| Contingency/BCP (backup systems, drill costs) | 5–8 | — |
| **Total** | **≈ 184–318** | **Against fee income of ≈ ₹1.5–2.5 Cr fixed fee + performance fee (Section 6, regulatory note) — a tight but workable economics story only if a second mandate is layered onto the same build within 12–18 months** |

This cost stack is the single strongest argument for treating this as a platform build, not a one-off account: at ₹500 Cr alone, fixed operating cost (₹1.8–3.2 Cr) approaches or exceeds the 0.30% fixed-fee revenue (₹1.5 Cr) before performance fees, so the business case depends on this infrastructure serving multiple NDPMS mandates going forward.

---

## Sources
[R1] Ionic Wealth NDPMS Regulatory Design Note (this project, 12-Sep-2026) — synthesises and cites: SEBI (Portfolio Managers) Regulations 2020 (as amended) https://www.sebi.gov.in/legal/regulations/feb-2023/securities-and-exchange-board-of-india-portfolio-managers-regulations-2020-last-amended-on-february-07-2023-_69223.html ; SEBI Master Circular for Portfolio Managers, 16-Jul-2025 https://www.sebi.gov.in/legal/master-circulars/jul-2025/master-circular-for-portfolio-managers_95347.html ; SEBI related-party circular (2022) on associate-investment limits https://www.apmiindia.org/storagebox/images/Circulars/Related-Party-Circular-26thAug'22.pdf ; SEBI digital-onboarding circular (2024) https://www.apmiindia.org/storagebox/images/Circulars/Facilitating%20ease%20in%20digital%20on-boarding%20process%20for%20clients%20and%20enhancing%20transparency%20-%202nd%20May'24.pdf ; SEBI performance-benchmarking circular (2022) https://www.apmiindia.org/storagebox/images/Circulars/Performance-Benchmarking-16th-Dec'22.pdf ; SEBI firm-level performance audit circular (2023) https://compfie.aparajitha.com/circular-on-audit-of-firm-level-performance-data-of-portfolio-managers-dated-02-08-2023-sebi/ ; SEBI order, First Global Finance, 26-May-2026 https://www.sebi.gov.in/sebi_data/attachdocs/may-2026/1779810509185.pdf ; APMI valuation-agency references https://www.lexibox.in/pms/performance-benchmarking-and-reporting-of-performance-by-portfolio-managers/ ; Regulation 31 (client reporting) text https://indiankanoon.org/doc/31059892/. Full source list [1]-[34] retained in the regulatory design note.
[1] SEBI (Portfolio Managers) Regulations, 2020 — as above.
[2] Ionic Wealth NDPMS Rebalancing Design Note (this project) — monthly consent-to-execution calendar.
[3] SEBI Master Circular for Portfolio Managers, 16-Jul-2025 — as above (custodian, OMS/dealing-room, time-stamping requirements).
[4] SEBI related-party/associate-investment circular (2022) — as above.
[8] SEBI digital-onboarding circular, effective 1-Oct-2024 — as above.
[12] SEBI order against First Global Finance, 26-May-2026 — as above (outsourcing/discretion recharacterisation precedent).
[32] APMI-empanelled valuation agencies reference — as above.
Additional this-session check: PMS fee/cost structure background — https://scripbox.com/wealth/portfolio-management-services-pms-fees-and-charges/ ; https://www.fincart.com/blog/pms-charges (custodian/demat charge line items, management-fee range, confirms 0.50% opex cap and exit-load-to-3% figures independently).
