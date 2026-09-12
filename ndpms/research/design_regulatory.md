# NDPMS ₹500 Cr Mandate — Regulatory Perimeter, Mandate Design and Tax Framework

Status date: 12 September 2026. Governing law: SEBI (Portfolio Managers) Regulations, 2020 ("PMS Regs") as amended, plus the Master Circular for Portfolio Managers dated 16 July 2025 (SEBI/HO/IMD/IMD-POD-1/P/CIR/2025/104) [1][3]. SEBI's consultation paper of 23 July 2026 proposing draft PMS Regulations 2026 (comments closed 13 Aug 2026) is NOT notified as far as we could verify; treat every item marked "2026 proposal" as pipeline, not law [11]. Primary SEBI/APMI hosts were unreachable from this environment; facts below were verified through secondary extracts of the primary documents and are cited; anything we could not pin down is marked "approx." or "verify".

## 1. Regulatory perimeter for NON-DISCRETIONARY PMS (NDPMS)

### 1.1 What NDPMS is, legally
- Discretionary PM "individually and independently manages" client funds; a non-discretionary PM "manages the funds in accordance with the directions of the client" (PMS Regs, Reg 2 definitions; Reg 24(1)-(2)) [1][2]. SEBI has not prescribed the form of a client direction. The regulatory floor is: no trade without a client direction that is evidenced, time-stamped and retrievable at inspection.
- Audit trail is mandatory for all PMs: time-stamping of order placement, execution and allocation; board-approved dealing-room policy; recorded dealing-room communications; automated order-management systems for PMs with AUM ≥ ₹1,000 Cr (Master Circular, dealing-room and order-placement chapter) [3]. For NDPMS the client instruction is the first link of that chain and must be captured in the same system.
- A PM "shall not invest client funds based on the advice of any other entity" (Reg 24, reported as 24(10)) and may not outsource core investment functions. SEBI's order of 26 May 2026 against First Global Finance (₹42 lakh penalty, 21-day onboarding bar) held that "investment decisions" include quantities, timing and client-level execution, not just model approval [12]. Implication: Ionic's own IC must own every recommendation in the NDPMS pack; third-party model feeds cannot drive the NDPMS book.

### 1.2 Eligible universe and hard limits (current law)

| Asset | NDPMS status | Rule / limit | Source |
|---|---|---|---|
| Listed equity, ETFs (equity, debt, gold, silver, international, liquid), listed REIT/InvIT, listed bonds/G-secs/SDLs, T-bills, CPs/CDs, money-market | Allowed | Core "listed securities and money-market instruments" universe; no cap | [1][2] |
| Mutual fund units (incl. index funds, active funds, FoFs, SIF units — SIFs sit under Chapter VI-C of the MF Regulations, min ₹10 lakh per PAN per AMC, live since 1-Apr-2025) | Allowed | Direct plans only; no distribution-related fee may be charged to the client on MF units; management fee per agreement is permitted | [3][16][33] |
| Unlisted securities: AIF units (Cat I/II/III), unlisted REIT/InvIT units, unlisted debt, pre-IPO/unlisted shares, warrants | Allowed, capped | ≤ 25% of the client's AUM for NDPMS/advisory (Reg 24(4)); discretionary PMS may not hold unlisted at all. "Active" breach (incl. subscribing to a rights issue) is non-compliance; "passive" breach (price move/redemption) must be cured — cure window approx. 90 days, verify | [1][2] |
| Same, for a Large Value Accredited Investor (LVAI) | Allowed up to 100% | Cap lifted for LVAI clients, subject to Disclosure Document disclosure and bilateral terms | [6][7] |
| Exchange-traded derivatives (equity index/stock F&O, commodity derivatives) | Allowed, restricted | Only for hedging and portfolio rebalancing; total derivative exposure ≤ portfolio funds placed with the PM; PM "shall not leverage" the portfolio; custodian required before commodity derivatives | [3][2] |
| Short selling / naked shorts | Not allowed | No unhedged short exposure today (2026 proposal: ≤ 50% of AUM via equity ETDs, within a 1.25x total-exposure cap and 10% option-premium cap, with explicit client consent — not notified) | [11] |
| Securities lending | Allowed | Lending only through the SEBI SLB mechanism (Reg 24 carve-out); requires client direction under NDPMS | [1][2] |
| Borrowing / margin / leverage | Not allowed | PM shall not borrow on behalf of clients; "invest, not borrow" | [2][3] |
| Foreign securities (direct US/UK stocks, offshore funds) | Not allowed inside PMS AUM today | 2026 proposal would permit "specified foreign securities" (listed equity, listed debt, regulated funds) — pipeline only. Route today: client's own LRS/OPI outside NDPMS AUM | [11] |
| Third-party PMS strategies | Not investable inside NDPMS AUM | A PMS is a service contract, not a "security"; plus Reg 24 bar on investing on another entity's advice. Structure outside AUM (see 1.4) | [1][12] |
| Securities of Angel One group / associates | Allowed with one-time prior positive consent | Equity ≤ 15% single associate / 25% all; debt+hybrid ≤ 15% / 25%; combined equity+debt+hybrid ≤ 30% of client AUM; no unrated associate debt; hybrid = REIT/InvIT/convertibles; MF units excluded from the cap; disclosure in every periodic report | [4] |
| Gold/silver: ETFs, SGBs (secondary), gold MF/FoF | Allowed | Listed instruments; no PMS-specific cap | [1] |
| Cash / liquid / overnight / arbitrage funds | Allowed | Client funds in a separate scheduled-bank account; liquid/arbitrage via direct plans | [2][3] |

### 1.3 Fees, expenses and exit loads (current law)
- No upfront fee, directly or indirectly. Brokerage at actuals. Operating expenses (excluding brokerage) ≤ 0.50% p.a. of average daily AUM. Exit load ≤ 3% / 2% / 1% of redeemed amount in years 1/2/3, nil after 3 years. Performance fee only on a high-water-mark basis over the life of the investment; hurdle optional. Fee illustration (Master Circular Annexure 4A) and separately signed fee annexure with the client's typed/handwritten acknowledgement are mandatory at onboarding (digital mode allowed from 1-Oct-2024) [3][8][33].
- LVAI relaxations: Schedule IV (prescribed agreement contents) does not apply; exit-load quantum and manner are bilaterally negotiated [5][6]. Whether the 0.50% operating-expense cap and no-upfront-fee rule are also relaxed for LVAI is not explicit in the sources we could read — verify; our design assumes they still bind.
- GST 18% on management and performance fees; fees are generally NOT deductible against the client's capital gains (Mumbai ITAT, Devendra Kothari; contrary Pune/Delhi/Kolkata rulings; unsettled) [26].

### 1.4 Third-party PMS, group products and conflicts — how to actually structure
1. Third-party PMS sleeve: client signs directly with the external PM (own PMS agreement, own demat/bank sub-account). Ionic may be paid as distributor or advise via its advisory registration; distributor commission must be disclosed in the client's periodic report (Reg 31 report must show distributor commission) [31]. The sleeve sits OUTSIDE NDPMS AUM and outside our TWRR; it enters our "house book" only for consolidated risk/attribution reporting.
2. Where the strategy exists as an AIF Cat III or SIF, prefer the wrapper: units are securities and investable inside NDPMS (Cat III units count toward the 25% unlisted cap; SIF units are MF units and do not) — interpretation, verify with compliance.
3. Angel One group products (AMC schemes, any group AIF/SIF): stay inside the 15/25/30% associate limits with the Annexure A one-time consent; self-impose a tighter IPS cap (we recommend 10% of AUM) and require IC minutes evidencing best-in-class selection each time.

### 1.5 Custody, fund accounting, reporting obligations

| Obligation | Cadence / deadline | Notes | Source |
|---|---|---|---|
| Custodian for securities | Standing | Mandatory for PMs (historic <₹500 Cr AUM exemption; at ₹500 Cr+ it binds anyway); mandatory before commodity derivatives | [1][3] |
| Client funds in separate scheduled-bank account; securities not in PM's name | Standing | Client-name demat + bank; no pooling for this mandate | [3] |
| Report to client | ≤ every 3 months (Reg 31); we commit monthly | Composition/valuation, transactions, income received, expenses, risks, associate investments, distributor commission | [31][4] |
| Monthly report to SEBI (and APMI) | Within 7 working days of month-end | AUM, clients, performance by IA | [9] |
| Performance benchmarking | Monthly / per IA | TWRR per Investment Approach; APMI-listed benchmark per strategy tag; from 1-Apr-2023 | [9] |
| Firm-level performance audit | Annual; confirmation to SEBI within 60 days of FY-end | Covers DPMS and NDPMS; APMI standard ToR from 1-Oct-2023 | [10] |
| Debt/MM valuation | Daily | Prices from APMI-empanelled agencies (CRISIL, ICRA Analytics, NSE Indices) | [32] |
| Disclosure Document | Filed with SEBI; updated on material change; CA-certified | Must disclose unlisted-to-100% LVAI terms, associate exposure, derivatives use | [1][7] |
| Digital onboarding | Standing | E-signed agreement; typed fee acknowledgement; APMI standard procedure | [8] |
| Alert-based monitoring of associate limits | Real-time | Required by 2022 amendment | [4] |

### 1.6 2025–2026 changes that matter here
- Co-investment: AIF (Second Amendment) Regs 2025 + circular SEBI/HO/AFD/AFD-POD-1/P/CIR/2025/126 (9-Sep-2025) allow Co-Investment Vehicle (CIV) schemes inside the AIF, restricted to accredited investors, one scheme per investment, ring-fenced, no leverage; the older Co-investment Portfolio Manager (CPMS) route under PMS Regs (Nov 2021) remains [13][34]. Accreditation is therefore the key to co-investing.
- Accredited-investor framework: income ≥ ₹2 Cr, or net worth ≥ ₹7.5 Cr (≥ ₹3.75 Cr financial), or income ≥ ₹1 Cr + net worth ≥ ₹5 Cr (≥ ₹2.5 Cr financial); SEBI (Sept 2025 board memo) proposed a ₹5 Cr securities-market-assets route for individuals and ₹20 Cr for corporates/trusts and manager-led accreditation; Jan 9, 2026 circular changed net-worth certificate format [15]. LVF minimum proposed to fall from ₹70 Cr to ₹25 Cr; Dec 2025 circular gives AI-only scheme relaxations [14].
- Digital onboarding eased (May 2024, effective 1-Oct-2024) [8]. PMS business-transfer framework (Oct 2025) [3].
- 2026 consultation (23-Jul-2026): to-be-listed securities; discretionary PMS up to 10% in investment-grade unlisted debt; specified foreign securities; MF-PMS tier (₹25 lakh ticket, ₹2 Cr net worth) managing only direct MF plans incl. ETFs and SIFs; derivatives to 1.25x with unhedged shorts to 50% and option premium 10%; independent fund managers under registered PMs [11]. No change to the NDPMS 25% cap or to consent mechanics was reported.

## 2. Large-value accredited investor route — on-board under it

| Question | Answer |
|---|---|
| Threshold | Accredited investor + agreement ≥ ₹10 Cr with the PM = LVAI [5][6] |
| Who accredits | BSE, NSE, NSDL, CDSL subsidiaries; CA net-worth certificate in the Jan-2026 format; validity 1–2 years approx., verify [15] |
| Relaxations for PMS | Unlisted up to 100% (we self-cap at 20%); Schedule IV agreement contents not mandatory (bespoke mandate, consent SLA, standing-instruction annex); exit load bilateral [5][6][7] |
| Collateral benefits | Eligible for CIV co-investment schemes and LVF/AI-only AIF schemes [13][14] |
| Entity-level | Each investing entity (individual, HUF, family trust, holding company) must accredit separately and each sign ≥ ₹10 Cr |
| Decision | Must. It is the only route that lets a bespoke NDPMS agreement carry the monthly-consent machinery we need without fighting Schedule IV boilerplate |

## 3. Tax framework FY2026-27 (Income-tax Act, 2025 in force from 1-Apr-2026; rates unchanged by Budget 2026; sections renumbered — 112A→198, 111A→196, 194→393) [17][24]

Effective rates below are for a resident individual/HUF/AOP in the top bracket, new regime: surcharge 25% on slab income, capped at 15% on capital gains under old 111A/112/112A and on dividends; cess 4% [23]. For a domestic company under 115BAA: 22% + 10% + 4% = 25.17%; capital-gains rates + 10% + 4%. Old-regime top slab MMR 42.744%.

| Instrument | Holding for LTCG | LTCG | STCG | Income/distribution | Transaction taxes | Effective top rate (individual) | Src |
|---|---|---|---|---|---|---|---|
| Listed equity, equity MF/ETF (≥65% domestic equity), equity SIF | 12 m | 12.5% above ₹1.25 lakh/yr | 20% | Dividend at slab (surcharge cap 15%); TDS 10% above ₹10,000 | STT 0.1% buy + 0.1% sell delivery; 0.001% on equity MF redemption; stamp 0.015% buy | LTCG 14.95%; STCG 23.92%; dividend 35.88% | [17][21][22][24] |
| Debt MF (>65% debt), liquid, arbitrage? — arbitrage funds are equity-oriented (≥65% equity) → equity treatment | n/a for debt | Debt MF bought after 1-Apr-2023: all gains deemed STCG at slab (old s.50AA) | slab | — | Stamp 0.005% on units | 39.0% (new regime) / 42.74% (old) | [18] |
| Listed bonds, G-secs, SDLs, listed corporate bonds | 12 m | 12.5% | slab | Coupon at slab | Stamp approx. 0.0001% (debentures); G-sec nil approx. | LTCG 14.95%; coupon 39.0% | [17][22] |
| Unlisted bonds/debentures, MLDs | none | deemed STCG regardless of holding | slab | slab | — | 39.0% | [18] |
| Gold/silver ETF, gold FoF (listed units) | 12 m listed / 24 m unlisted units | 12.5% | slab | none | Stamp 0.005% units | 14.95% / 39.0% | [18] |
| SGB — primary subscriber held to RBI maturity | 8 y | Exempt (Budget 2026 narrowed: primary subscription + continuous holding only) | — | 2.5% coupon at slab | — | 0% on redemption; coupon 39.0% | [25] |
| SGB — bought in secondary market / sold on exchange | 12 m | 12.5% | slab | coupon at slab | — | 14.95% | [25] |
| International FoF / Indian-listed international ETF | listed units 12 m; unlisted FoF 24 m | 12.5% | slab | — | Stamp 0.005% | 14.95% / 39.0% | [18] |
| REIT / InvIT units (listed) | 12 m | 12.5% | 20% | Interest & rent: slab, TDS 10%; dividend: exempt — from 1-Apr-2026 even where SPV opted for concessional rate (Taxation and Other Laws (Amendment) Bill 2026, verify enactment); "repayment of debt" reduces cost, excess over cost taxed as other income | STT 0.1% delivery approx. | Interest 39.0%; LTCG 14.95% | [19] |
| AIF Cat I / II | Pass-through (s.115UB): investor taxed as if direct; TDS 10% (194LBB); Finance Act 2025: fund's securities are capital assets → capital gains, not business income; business income taxed at fund level; losses (except business) pass through after 12 m | as underlying | as underlying | as underlying | — | as underlying | [20] |
| AIF Cat III | Fund-level tax; investor receives post-tax NAV. LTCG 12.5% + surcharge (15% cap) + cess; STCG 20%; F&O/business income at MMR ~39–42.7% | fund-level | fund-level | fund-level | STT on fund's trades embedded (F&O STT up from 1-Apr-2026: futures 0.05%, options 0.15% premium) | approx. 14.95% / 23.92% / 42.74% | [20][21] |
| Third-party PMS / our NDPMS | Client-level; each trade a client tax event; fees mostly not deductible; GST 18% on fees | as instrument | as instrument | as instrument | as instrument | — | [26] |
| Cash / bank / overnight | — | — | slab | interest at slab | — | 39.0% | — |

Reported (verify): Finance Act 2026 removed a 20% deduction against dividend/MF-unit income that had appeared in the new Act's drafting [25 — angelone key changes]. Not material to our rates above.

Rebalancing implications:
1. Turnover cost, delivery equity round trip ≈ STT 20 bps + stamp 1.5 bps + brokerage 3–5 bps + exchange/SEBI/GST 1 bps ≈ 26–28 bps approx. On ₹500 Cr with 30% annual two-way turnover: ₹150 Cr × 0.27% ≈ ₹40 lakh/yr.
2. Tax drag: every 1% of AUM realised as STCG costs 23.92 bps of NAV vs 14.95 bps as LTCG; slab-taxed debt gains cost 39 bps. Rule: never realise equity STCG to rebalance unless expected alpha of the switch > 9 bps × (gain/proceeds) hurdle; prefer flows-based rebalancing (deploy new cash, redirect distributions) before sells.
3. Lot selection: Indian law imposes FIFO per demat account (s.45(2A) of the 1961 Act, carried into the 2025 Act — verify new section); specific-ID is not available. Workaround: run 2–3 client demat accounts by "book" (Core long-only; Tactical/rebalance; Income) so that rebalance sells come from the tactical account's newest-but-already-LTCG lots. MF folio-level FIFO similarly argues for separate folios per purpose.
4. In-specie transfer-in of existing holdings is not a transfer; cost and holding period carry over — capture both at custodian on Day 1.
5. Loss harvesting: LTCL sets off only against LTCG; STCL against both; 8-year carry-forward requires on-time ITR. Run a March harvesting pack.
6. Debt sleeve: since debt MF gains are slab-taxed, prefer listed bonds/G-secs/SDLs held > 12 m (12.5%) or target-maturity ETFs/index funds (listed units, 12 m) — note target-maturity MFs bought as MF units fall under the >65% debt rule → slab; the ETF form gets listed-unit treatment only if the unit is not a "specified mutual fund" — verify; many advisers treat all debt-heavy MF/ETF units as slab-taxed.

## 4. RBI / FEMA and international exposure

| Route | Who | Cap | FY2026-27 status | What it means for ₹500 Cr |
|---|---|---|---|---|
| MF industry overseas limit | AMCs | USD 7 bn industry + USD 1 bn overseas-ETF pool; approx. USD 1 bn per AMC (RBI-set, SEBI-administered) | Nearly exhausted again by May–Jun 2026; Nippon, Axis, Kotak among AMCs pausing lump sums; AMFI request to raise pending; no announced increase | Fresh subscriptions to international FoFs largely closed; Indian-listed international ETFs trade at premiums when creations are suspended (premium 5–15% at times, approx.) | [27] |
| LRS | Resident individuals | USD 250,000 per individual per FY (≈ ₹2.2 Cr at ~₹88/USD approx.); TCS 20% above ₹10 lakh (creditable) | Unchanged | 4–6 adult family members → ₹9–13 Cr/yr; cumulative ₹45–65 Cr over 5 years; sits outside NDPMS AUM | [28][30] |
| GIFT-IFSC outbound funds | Residents via LRS | Within LRS | 5 outbound retail funds from 4 AMCs as of Jul 2026 (e.g., Parag Parikh IFSC S&P 500 / Nasdaq 100 FoFs), USD 5,000 minimum; IFSC PMS minimum USD 75,000 | Preferred LRS destination (INR-to-USD fund, IFSCA-regulated); LRS to IFSC counts within the USD 250k | [29] |
| OPI by Indian entity | Listed company: ≤ 50% of net worth; unlisted company: OPI permitted in IFSC fund units (Schedule V) | Net-worth based | Unchanged (OI Rules 2022; IFSC liberalisation) | If the family owns a holding company, IFSC fund units are the scalable route; a listed group company can do 50% net worth OPI | [30] |
| Inside NDPMS AUM | PM | Foreign securities not permitted today | 2026 proposal pending | Only Indian-listed international ETFs/FoFs qualify inside the mandate |

Realistic international sleeve: target 7.5% (₹37.5 Cr). Year-1 achievable: ₹10–15 Cr via Indian-listed international ETFs bought only at ≤ 1% premium to iNAV plus any open FoF windows (inside AUM); ₹9–13 Cr via family LRS into IFSC funds (outside AUM, advised); balance via holding-company OPI if available. Report the total sleeve on a look-through basis against the IPS but tag "inside AUM" vs "advised".

## 5. Mandate design: IPS and NDPMS agreement that runs monthly without per-trade friction

### 5.1 Legal architecture
1. LVAI NDPMS Agreement (bespoke; Schedule IV not mandatory) with annexes: (A) IPS and SAA bands; (B) Consent Protocol; (C) Standing Instructions Register; (D) Fee annexure with SEBI illustration; (E) Associate-investment consent (SEBI Annexure A format); (F) Derivatives/hedging protocol; (G) SLB authorisation; (H) Reporting pack spec.
2. Consent Protocol (Annex B): the monthly Rebalance Proposal Pack (RPP) is the "direction of the client". It lists every trade (ISIN, side, quantity or ₹ amount, limit/participation rule, execution window, rationale, cost and tax estimate). The client approves the pack as a whole or line-by-line by e-sign (Aadhaar/DSC) on the portal, or by email from registered IDs. Validity: 10 trading days; unexecuted lines lapse. Amendments require a new approval. All approvals are hashed and stored with the OMS audit trail.
3. Standing Instructions Register (Annex C) — narrow, mechanical, revocable, each with trigger, instrument, quantity rule, validity and maximum ₹: (i) sweep idle cash > ₹50 lakh into a named liquid/overnight fund daily; (ii) reinvest distributions into the same instrument or the liquid fund; (iii) default corporate-action elections (dividend reinvest off; rights subscribe only if pre-approved in RPP because a rights subscription is an "active" unlisted-cap event); (iv) execute already-approved tranche schedules (e.g., ₹20 Cr/week into a named ETF for 5 Thursdays); (v) auto-roll of an approved hedge into the next monthly series at same notional. Anything that changes asset-class weights or names a new security stays in the RPP.
4. Legal risk: a "pre-approved model with bands where the PM picks timing/size" drifts toward discretion and risks recharacterisation at inspection. Mitigation: standing instructions are limit-order-like (fully specified), client can revoke on the portal, and we obtain a legal opinion and consider SEBI Informal Guidance before go-live. Status: unclear_verify.

### 5.2 Consent SLA and monthly calendar

| Day | Step | Owner | SLA |
|---|---|---|---|
| T-5 (last Wed of month) | IC signs off house view + model targets; NDPMS drift report (actual vs SAA bands) | IC / PM | — |
| T-3 | RPP drafted: trades, ₹, costs, tax estimate, band compliance, associate/unlisted checks | PM + Compliance | pre-trade compliance sign-off |
| T-1 | RPP sent to client via portal; 30-min walkthrough | RM | client ack |
| T0 (1st Thursday) | Client e-approves | Client | ≤ 2 business days target; escalation call at 48 h |
| T0 to T+7 | Execution window; weekly tranches Mon redemption / Thu deployment as per house cadence | Dealing | slippage vs arrival price ≤ 15 bps target |
| T+8 | Post-trade report: fills, slippage, cost, updated weights | Ops | within 1 day of window close |
| Month-end + 5 | Client monthly statement (Reg 31 content, monthly not quarterly) | Ops | 5 business days |
| Month-end + 7 wd | SEBI/APMI monthly report | Compliance | 7 working days |

Latency cost model: expected cost of delay = |target − actual| weight × daily vol × sqrt(days). With ₹500 Cr, a 5% (₹25 Cr) equity under-deployment at 1% daily index vol for 10 days costs ~₹79 lakh of tracking risk (1-sigma); a 2-day SLA cuts it to ~₹35 lakh. Design the SLA around this.

### 5.3 SAA bands and hard limits for the agreement (illustrative for the Moderate house model; sized to ₹500 Cr)

| Sleeve | Target % | ₹ Cr | Band | Regulatory ceiling | Vehicle preference (tax + rule aware) |
|---|---|---|---|---|---|
| Indian equity — direct stocks (NIFTY-750 scorecard) | 25 | 125 | ±5 | none | Direct; tactical demat separate |
| Indian equity — index funds/ETFs/active MF/SIF | 25 | 125 | ±5 | direct plans only | Index ETFs for beta, active/SIF for alpha |
| International equity | 7.5 | 37.5 | 0 to +2.5 | inside AUM only via Indian-listed ETFs/FoFs | Cap premium ≤1%; rest via LRS/IFSC outside AUM |
| Fixed income — G-sec/SDL/listed corp bonds/target-maturity | 15 | 75 | ±5 | none | Listed paper > 12 m for 12.5% LTCG; avoid unlisted debt (slab) |
| Cash/liquid/arbitrage | 7.5 | 37.5 | 2.5 to 15 | separate bank account | Arbitrage (equity taxation) for > 6 m parking; overnight for < 1 m |
| REIT/InvIT (listed) | 5 | 25 | ±2.5 | hybrid within associate rule if group-issued | Listed only; unlisted InvIT counts in 25% cap |
| Gold/silver ETFs, SGB secondary | 7.5 | 37.5 | ±2.5 | none | Gold ETF; SGB secondary only if yield-to-maturity beats ETF cost |
| AIF Cat I/II (private credit, PE, infra) | 5 | 25 | 0 to 7.5 | Unlisted cap 25% NDPMS / 100% LVAI; IPS cap 20% total unlisted | Cat II pass-through; commitments drawn over 3–4 yrs |
| AIF Cat III / long-short | 2.5 | 12.5 | 0 to 5 | Unlisted cap | Fund-level tax; use only for uncorrelated strategies |
| Derivatives (hedge only) | 0 notional target | up to 25% notional | Tail hedge ≤ 1% premium p.a. | exposure ≤ portfolio funds; no leverage | Put spreads on Nifty, approved in RPP |
| Group/associate securities (all sleeves) | ≤ 10 (IPS) | ≤ 50 | — | 15/25/30% SEBI | One-time consent + IC best-selection minute |
| Total unlisted | ≤ 15 (IPS) | ≤ 75 | — | 25% (100% LVAI) | Keep 10-pt buffer for passive breach |

### 5.4 CAN / SHOULD / AVOID in this domain
- CAN: invest across every listed class, MF/ETF/SIF direct plans, AIFs to 25% (100% under LVAI), hedge with F&O within 1x exposure, lend via SLB, hold securities in the client's own demat under our custodian, report monthly, charge fixed + HWM performance fees, negotiate exit load and agreement form under LVAI.
- SHOULD: on-board every entity as LVAI; build the RPP e-consent portal with hashed audit trail; run 2–3 purpose-segregated demat accounts for FIFO management; keep unlisted ≤ 15% and associates ≤ 10% by IPS; pre-approve tail-hedge protocol monthly; get legal opinion/informal guidance on standing instructions; adopt APMI benchmark tagging and compute NDPMS TWRR daily; book the third-party PMS and LRS sleeves outside AUM with look-through reporting; run a March tax-loss/lot review; file for CIV eligibility via accreditation.
- AVOID: any discretion "in practice" (PM choosing names/sizes after a generic approval); executing third-party model feeds inside NDPMS; debt MFs for long-horizon fixed income (slab tax); unlisted debt; naked shorts or leverage; upfront fees; distribution fees on MF units; buying international ETFs at > 1% premium; letting rights issues push unlisted over 25% ("active" breach); intraday/high-frequency anything; pooling this client's assets with others.

## 6. Worked ₹500 Cr numbers

| Item | Formula | ₹ |
|---|---|---|
| Fixed fee 0.30% + performance 10% over house benchmark with HWM | 500 Cr × 0.30% | ₹1.50 Cr/yr fixed; GST ₹27 lakh |
| Operating expense cap | 0.50% × 500 Cr | ≤ ₹2.50 Cr/yr (custody ~3–5 bps = ₹15–25 lakh; audit, valuation feeds, RTA) |
| Round-trip transaction cost, equity | 27 bps × turnover | 30% turnover → ₹40 lakh/yr |
| Tax drag if 5% of AUM realised as equity STCG vs LTCG | 5% × (23.92% − 14.95%) × gain ratio 20% | ≈ ₹22 lakh saved per year by waiting past 12 m |
| Unlisted headroom (NDPMS non-LVAI) | 25% × 500 Cr | ₹125 Cr legal; ₹75 Cr IPS cap |
| Associate headroom | 30% combined; IPS 10% | ₹150 Cr legal; ₹50 Cr IPS |
| Derivative notional ceiling | ≤ 100% of portfolio funds | ₹500 Cr legal; IPS 25% = ₹125 Cr |
| Tail-hedge budget | 1% of AUM p.a. | ₹5 Cr/yr; options STT 0.15% on premium ≈ ₹75,000 |
| LRS capacity | USD 250k × ₹88 × N adults | N=5 → ₹11 Cr/yr; TCS 20% → ₹2.2 Cr blocked till ITR credit |
| Consent latency risk | 25 Cr × 1% × sqrt(days) | 10 days ₹79 lakh; 2 days ₹35 lakh (1-sigma) |

## 7. Risks and pitfalls (see structured list)
Recharacterisation of standing instructions as discretion; Reg 24 outsourcing breach via third-party feeds; active unlisted breach through rights/CIV drawdowns; associate-limit breach through group ETFs bought in size; consent latency during drawdowns; international ETF premium collapse; MF overseas cap closures stranding the sleeve; FIFO destroying tax-aware plans if one demat is used; SGB secondary purchases losing exemption after Budget 2026; TCS cash drag; Cat III fund-level MMR on F&O income; 2026 regulations changing derivative and foreign-securities rules mid-mandate; fee-deductibility disputes; monthly SEBI reporting errors on NDPMS TWRR.

## Sources
[1] SEBI (Portfolio Managers) Regulations, 2020 (as amended) — https://www.sebi.gov.in/legal/regulations/feb-2023/securities-and-exchange-board-of-india-portfolio-managers-regulations-2020-last-amended-on-february-07-2023-_69223.html
[2] Vinod Kothari, SEBI revised norms for Portfolio Managers (2020) — https://vinodkothari.com/2020/02/sebi-brings-in-revised-norms-for-portfolio-managers/
[3] SEBI Master Circular for Portfolio Managers, 16 Jul 2025 — https://www.sebi.gov.in/legal/master-circulars/jul-2025/master-circular-for-portfolio-managers_95347.html ; APMI mirror https://www.apmiindia.org/storagebox/images/Circulars/Master%20Circular%20for%20Portfolio%20Managers%20-%2016th%20July'25.pdf
[4] SEBI circular SEBI/HO/IMD/IMD-I/DOF1/P/CIR/2022/112 (related parties) — https://www.apmiindia.org/storagebox/images/Circulars/Related-Party-Circular-26thAug'22.pdf ; Taxmann summary https://www.taxmann.com/post/blog/portfolio-managers-can-invest-up-to-30-of-clients-portfolio-in-securities-of-their-own-associates-sebi/
[5] SEBI circular on PMS for accredited investors, 21 Dec 2021 — https://compfie.aparajitha.com/circular-on-portfolio-management-services-for-accredited-investors-dated-21-12-2021-sebi/
[6] Taxguru, Portfolio Management Services for Accredited Investors — https://taxguru.in/sebi/portfolio-management-services-accredited-investors.html
[7] SEBI Board memorandum, Amendments to PMS Regulations (Oct 2021) — https://www.sebi.gov.in/sebi_data/meetingfiles/oct-2021/1633416546235_1.pdf
[8] SEBI circular SEBI/HO/IMD/IMD-PoD-1/P/CIR/2024/35 digital onboarding — https://www.apmiindia.org/storagebox/images/Circulars/Facilitating%20ease%20in%20digital%20on-boarding%20process%20for%20clients%20and%20enhancing%20transparency%20-%202nd%20May'24.pdf ; https://www.business-standard.com/markets/news/sebi-streamlines-digital-onboarding-for-portfolio-managers-clients-124050300515_1.html
[9] SEBI circular SEBI/HO/IMD/IMD-PoD-2/P/CIR/2022/172 performance benchmarking — https://www.apmiindia.org/storagebox/images/Circulars/Performance-Benchmarking-16th-Dec'22.pdf ; https://taxguru.in/sebi/performance-benchmarking-reporting-performance-portfolio-managers.html
[10] SEBI circular SEBI/HO/IMD/IMD-PoD-1/P/CIR/2023/133 firm-level performance audit — https://compfie.aparajitha.com/circular-on-audit-of-firm-level-performance-data-of-portfolio-managers-dated-02-08-2023-sebi/
[11] SEBI consultation paper 23 Jul 2026 — https://taxguru.in/sebi/sebi-invites-comments-comprehensive-review-portfolio-managers-regulations-2026.html ; https://corporate.cyrilamarchandblogs.com/2026/08/sebis-proposed-overhaul-of-the-pms-regulatory-framework/ ; https://informistmedia.com/MoneyWire/55628/Consultation-Paper-SEBI-issues-consultation-paper-on-comprehensive-review-of-PMS-norms ; https://www.tribuneindia.com/news/business/sebi-proposes-foreign-investments-unhedged-short-positions-for-portfolio-managers/amp
[12] SEBI order 26 May 2026 (First Global) — https://www.sebi.gov.in/sebi_data/attachdocs/may-2026/1779810509185.pdf ; https://www.moneylife.in/article/sebi-slaps-42-lakh-fine-on-first-global-finance-for-outsourcing-core-pms-functions-and-decisions-bars-from-taking-new-clients-for-21-days/80583.html ; https://corporate.cyrilamarchandblogs.com/2026/06/sebi-order-penalises-outsourcing-of-core-functions-structuring-lessons-for-asset-management-industry/
[13] SEBI CIV circular SEBI/HO/AFD/AFD-POD-1/P/CIR/2025/126 — https://bcasonline.org/wp-content/uploads/2025/09/Framework-for-AIFs-to-make-co-investment-within-the-AIF-structure-under-SEBI.pdf ; https://corporate.cyrilamarchandblogs.com/2025/09/beyond-cpms-route-sebi-unlocks-co-investment-schemes-for-aifs/
[14] SEBI circular Dec 2025, AI-only schemes and LVF relaxations — https://www.sebi.gov.in/legal/circulars/dec-2025/modalities-for-migration-to-ai-only-schemes-and-relaxations-to-large-value-funds-for-accredited-investors-under-sebi-alternative-investment-funds-regulations-2012_98244.html
[15] SEBI Board memo Sept 2025 on accredited investors — https://www.sebi.gov.in/sebi_data/meetingfiles/sep-2025/1758513313676_1.pdf ; Jan 2026 net-worth certificate change https://www.harunraaj.com/blog/net-worth-certificate-sebi-accredited-investor-january-2026
[16] SIF framework — https://www.business-standard.com/amp/markets/capital-market-news/sebi-issues-new-regulatory-framework-for-specialized-investment-funds-125022800217_1.html ; https://upstox.com/news/business-news/financial-regulations/sebi-framework-for-specialized-investment-funds-si-fs-10-lakh-entry-sector-caps-and-more/article-149031/
[17] Capital gains FY2026-27 — https://finlecture.in/indian-tax-system/capital-gains-tax-fy-2026-27/ ; https://www.samco.in/knowledge-center/articles/ltcg-tax-after-budget-2026-why-long-term-capital-gains-are-back-in-focus/ ; https://taxguru.in/income-tax/capital-gains-income-tax-act-2025-tax-period-2026-27.html ; https://www.bajajfinserv.in/investments/section-112a-income-tax-act
[18] s.50AA and ETF/debt/gold/international taxation — https://www.finnovate.in/learn/blog/etf-taxation-india ; https://taxguru.in/income-tax/amendment-specified-mutual-fund-definition-section-50aa-budget-2024.html
[19] REIT/InvIT taxation and 2026 amendment — https://upstox.com/news/personal-finance/tax/reit-in-vit-dividend-income-what-is-tax-free-under-the-taxation-and-other-laws-amendment-bill-2026/article-198414/ ; https://www.casahuja.com/2026/08/reit-invit-taxation-in-2026-spvs-tax.html ; https://taxgarden.in/blog/reit-invit-taxation-india-ay-2026-27-section-115ua-distributions-capital-gains
[20] AIF taxation — https://www.finnovate.in/learn/blog/aif-taxation-india ; https://www.lexology.com/library/detail.aspx?g=a8345261-0ec2-4031-b2e1-211c964e83cd ; https://treelife.in/taxation/category-iii-aif-taxation-in-india/
[21] STT incl. Budget 2026 — https://cleartax.in/s/securities-transaction-tax-stt ; https://upstox.com/news/personal-finance/tax/explained-how-the-stt-hike-on-equity-futures-and-options-affects-traders-and-investors/article-189260/ ; https://www.angelone.in/news/personal-finance/key-financial-changes-from-april-1-2026-income-tax-act-overhaul-sgb-rule-shift-lower-mf-costs
[22] Stamp duty — https://groww.in/help/stocks,-f&o,-ipo-&-mtf/sx-pricing/what-is-stamp-duty ; https://www.prostocks.com/stamp-duty-charges.html
[23] Surcharge caps — https://cleartax.in/s/marginal-relief-surcharge ; https://www.taxmann.com/post/blog/tax-rates-surcharge-cess
[24] Dividend TDS, s.393 of IT Act 2025 — https://blog.tdsman.com/2026/05/tds-on-dividend-section-3931-section-194/
[25] SGB Budget 2026 — https://www.caalley.com/news-updates/budget-2026/budget-2026-changes-sgb-tax-rules-ends-blanket-capital-gains-exemption ; https://www.taxscan.in/top-stories/sovereign-gold-bond-tax-rules-for-itr-ay-2026-27-interest-redemption-capital-gains-and-reporting-1448954
[26] PMS fee deductibility — https://bcajonline.org/journal/allowability-of-portfolio-management-fees-in-computing-capital-gains/ ; https://taxguru.in/income-tax/portfolio-management-fees-allowability-section-48-capital-gains-tax.html
[27] MF overseas cap — https://mfreturns.com/blog/why-international-mutual-funds-closed-sebi-cap-2026/ ; https://www.equityresearchindia.com/post/the-usd-7-billion-wall-why-indian-mutual-funds-keep-pausing-their-overseas-schemes ; https://www.oquilia.com/news/sebi-international-fund-overseas-investment-limit-7bn
[28] LRS and TCS — https://cleartax.in/s/tax-on-foreign-remittance ; https://www.swatikandco.com/tcs_foreign_remittance_2026_27.html
[29] GIFT City routes — https://www.business-standard.com/amp/finance/personal-finance/gift-city-outbound-funds-with-international-funds-closing-down-for-sip-126072901039_1.html ; https://www.valueresearchonline.com/stories/226923/indians-get-new-route-worlds-markets-gift-city/ ; https://gift.treelife.in/portfolio-management-services-in-gift-city/
[30] FEMA OI Rules/Directions 2022 and IFSC OPI — https://rbidocs.rbi.org.in/rdocs/notification/PDFs/NT110B29188F1C4624C75808B53ADE5175A88.PDF ; https://www.menonverma.com/mv-update/13/1/Amendments-to-the-Foreign-Exchange-Management-(Overseas-Investment)-Directions,-2022-Enhanced-scope-of-Overseas-Portfolio-Investments ; https://indiacorplaw.in/2022/12/05/what-the-odi-opi-holds-for-indian-entities/
[31] Regulation 31 text — https://indiankanoon.org/doc/31059892/
[32] APMI valuation agencies — https://www.lexibox.in/pms/performance-benchmarking-and-reporting-of-performance-by-portfolio-managers/ ; https://aifpms.com/blog/performance-reporting-benchmarking-by-portfolio-manager/
[33] Fee rules (Oct 2020) — https://cafemutual.com/news/industry/31-sebi-redefines-and-refines-the-pms-fee ; https://pmsbazaar.com/Blogs/Portfolio-Managers-get-time-till-October-1-to-comply-with-new-SEBI-norms
[34] Co-investment Portfolio Manager (2021) — https://corporate.cyrilamarchandblogs.com/2021/11/sebi-prescribes-new-registration-requirement-for-cat-i-ii-aif-managers-facilitating-co-investments/ ; https://legalitysimplified.com/2021/11/11/sebi-notifies-portfolio-managers-fourth-amendment-regulations-2021/
