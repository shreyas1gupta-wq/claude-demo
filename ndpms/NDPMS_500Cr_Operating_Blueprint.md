# ₹500 Cr NDPMS Mandate — Operating Blueprint: what we CAN do, what we SHOULD do, what to AVOID

Ionic Wealth (Angel One) · CIO/PM operating blueprint · Status date 12 September 2026 · Version 1.1 — FINAL (consolidates seven domain designs, two verified data packs, four adversarial critiques and the completeness review; corrections adopted are listed in §13, with the v1.1 reconciliation pass at the end of §13). The companion data pack blueprint_data.json v1.1 is canonical for allocation %, ₹ Cr, limits, costs, KPIs, the deployment ladder and the return waterfall; every table below has been tied to it.

Conventions: ₹ Cr = ₹ crore (₹10 million); "approx." = not verified against a primary source this cycle; "verify" = must be confirmed against the primary SEBI/RBI/IT text before it enters a client document; feasibility tags: allowed / allowed_with_consent / restricted / not_allowed / unclear_verify. All portfolio figures are sized to ₹500 Cr = NAV 500. Market snapshot used throughout: Nifty 50 23,398.10 (close 11-Sep-2026, verified), trailing P/E 19.8–20.2 vs 10-yr median 23.3, India VIX 12.4, 10-yr G-sec ≈7.0% (10-month high), repo 5.25% (4th hold, neutral), USD/INR 95.79, gold ₹1,52,650/10 g, Brent ≈$110 (all verified from 11-Sep-2026 search snippets; see Appendix A, Table A4).

---

## 0. TL;DR

The mandate is non-discretionary: we recommend, the client directs, we execute. Nothing trades without an evidenced, time-stamped client instruction. Every design choice below exists to make that instruction cheap to obtain, fast to act on, and impossible to mistake for discretion.

**The 12 decisions**

| # | Decision | One-line rule |
|---|---|---|
| 1 | LVAI onboarding for every investing entity | Accredit each entity and sign ≥ ₹10 Cr per entity; bespoke agreement (Schedule IV not mandatory) with eight annexes. LVAI buys commercial flexibility and unlisted headroom; it does **not** settle the consent-mechanics question (corrected, §13). |
| 2 | One omnibus monthly Rebalance Proposal Pack (RPP) is the routine consent instrument | E-signed as a whole or line-by-line; 2-business-day consent SLA, 48-hour escalation; 10-trading-day validity; unexecuted lines lapse; one-page executive summary + full appendix. |
| 3 | Standing Instructions are narrow, mechanical, revocable — and all trigger-based de-risking is consent-generating until counsel clears it | Seven-item register (cash sweep, distribution routing, CA default, approved-tranche execution, hedge auto-roll, AIF capital-call funding, deployment-ladder acceleration). Any sell-side or trigger-based action generates a pre-drafted one-click mini-RPP (24-hour SLA), not a self-executing trade, until a legal opinion / SEBI Informal Guidance says otherwise. |
| 4 | One canonical Model Master per variant (Moderate / Aggressive), sized to ₹500 Cr, with bands | Moderate: 50% domestic equity, 5% international, 24% fixed income, 2% arbitrage, 6% gold/silver, 4% REIT/InvIT, 9% alternatives (AIF/SIF). Third-party PMS sits **outside** NDPMS AUM. AA credit trimmed to 2% so the book passes its own credit floor on day one. |
| 5 | Three-tier benchmark with a single Policy Composite (T2) as the accountability yardstick | T1 = APMI-prescribed Multi-Asset benchmark (regulatory filing); T2 = 9-component sleeve-weighted composite (contractual "mandate benchmark"); T3 = Allocate 80/20 house benchmark as reference only. |
| 6 | Instrument logic is cost- and tax-form-led | Index funds / ETFs via AP for beta; active MFs only in mid/small cap (direct plans, ≤1% of scheme AUM); SIF preferred over Cat III where both exist; TMF funds + direct 10-yr G-sec for fixed income; arbitrage funds for cash held >1 month; gold via ETF only (no SGB); international 5% in-AUM via Indian-listed vehicles at ≤1% premium, balance via family LRS/IFSC outside AUM. |
| 7 | Hybrid rebalancing (Strategy H) | Monthly band review, trade only breaching lines, trade to the inner band edge (to target only where a regulatory/IPS ceiling binds), event overlay for tail moves; minimum ticket ₹1 Cr; liquid-book turnover budget 15–25%/yr; budget ≈ 10–14 bps p.a. of cost+tax for rebalancing. |
| 8 | Tax architecture is set before the first trade | Three purpose-segregated demat accounts (Core / Tactical / Harvest) because FIFO applies per demat account; cash-flow-first rebalancing; no equity STCG realised to rebalance unless the switch clears an 8.97-point hurdle; March harvesting pack; separate MF folios by purpose. |
| 9 | Pre-loaded risk framework | 14-limit two-tier framework (plus a separate monitored-metric band table); daily parametric + historical VaR, EWMA vol, TE vs T2, drawdown with an absolute −18% trigger; 12-indicator early-warning board; partial tail hedge (25–40% of equity sleeve, 95/85 put spreads, premium ≤ 1% of AUM p.a.) added when India VIX < 15. |
| 10 | One TWRR engine, R0–R4 series, consent-latency attribution | Daily transaction-level TWRR; Brinson-Fachler with Carino linking; Perold implementation shortfall with a consent-latency line; fee 0.30% fixed + 10% of outperformance over T2 with HWM; net-alpha accountability reset to a realistic ladder (≥ 0 floor; +50 bps at 3Y; +75 bps at 5Y). |
| 11 | Operations built as inspection evidence | Every OMS order carries an rpp_id / standing_instruction_id foreign key; WORM consent ledger (10-year retention); 11 reconciliations; five-tab dashboard suite on the existing house pipeline; build sequenced custodian → OMS rules → AP relationship; BCP tabletop before the first live cycle; team 7.7–8.7 FTE in year 1. |
| 12 | Deployment of fresh ₹500 Cr in 8 weeks (equity-like ₹300 Cr + ₹25 Cr stabiliser closing tranche), 4 weeks (fixed income ₹120 Cr), 6–18 months (alternatives ₹45 Cr) | Thursday tranches of ₹37.5 Cr equity-like; acceleration on −5%/−10%/VIX>22 via pre-drafted one-click mini-RPPs; mid-deployment re-confirmation at week 4; parked cash in arbitrage funds, not liquid funds. Expected one-off cash drag ≈ ₹1.4–1.7 Cr. |

**The 5 things to avoid**

1. **Discretion in practice.** Open-ended standing instructions ("rebalance whenever drift exceeds band"), PM-timed execution off a generic approval, or self-executing de-risking triggers before legal clearance. SEBI's 26-May-2026 First Global order treats quantities, timing and client-level execution as investment decisions.
2. **Anyone else's investment decision inside NDPMS AUM.** No third-party model feeds, no third-party PMS as a line item in the client's NDPMS account (Reg 24(10) bar on investing on another entity's advice). Third-party PMS is a separate client contract, reported look-through only.
3. **Leverage, naked shorts, intraday/HFT, or a full-notional put programme.** Prohibited today (the 2026 draft is not law) and uneconomic under consent latency; a 100%-notional rolling put costs ≈ ₹14.5 Cr/yr for payoffs only in sharp crashes.
4. **Tax-blind instrument choices.** Liquid funds for cash parked > 1 month (use arbitrage), secondary-market SGBs (exemption gone for non-primary holders after Budget 2026), Cat III AIF where a comparable SIF exists, realising equity STCG to close a band, one undifferentiated demat account.
5. **Misstating what we manage to.** Reporting the 80/20 house benchmark as the headline target, presenting R0 paper returns as performance, annualising sub-1-year returns, relying on the July-2026 SEBI consultation paper as if notified.

---

## 1. Mandate & NDPMS constraints

### 1.1 What changes versus discretionary PMS

| Dimension | Discretionary PMS (Allocate today) | NDPMS (this mandate) | Operating consequence |
|---|---|---|---|
| Legal basis of a trade | PM "individually and independently manages" client funds (PMS Regs 2020, Reg 2 definitions) | PM manages "in accordance with the directions of the client" (Reg 2; Reg 24) | No trade without an evidenced, dated, retrievable client direction; the direction is the first link of the Master Circular audit trail |
| Rebalance timing | PM chooses | Client consents; PM executes within the consent window | Monthly cadence with one omnibus consent; latency between recommendation and execution becomes a budgeted risk |
| Universe | Listed securities, MF direct plans, money-market; **no unlisted** | Same plus **up to 25% of AUM in unlisted securities** (AIF units, unlisted REIT/InvIT, unlisted debt; ≤10% of AUM in unlisted unrated debt of non-associates); no below-investment-grade listed paper (SEBI circular SEBI/HO/IMD/DF1/CIR/P/2020/26, consolidated in the 16-Jul-2025 Master Circular) | Alternatives sleeve is the structural edge of NDPMS; cap and buffer it |
| Derivatives | Hedging/rebalancing only, exposure ≤ portfolio funds, no leverage | Same, plus each hedge needs a specific instruction or a pre-approved Hedge Protocol annex | Tail hedge is a monthly RPP line; auto-roll at same notional is a standing instruction |
| Speed | Intraday possible | Days | No HFT, no intraday, no options overwriting in the client account; anything needing same-day judgement lives inside a fund wrapper (SIF / Cat III) where the manager holds discretion |
| Accountability | PM owns outcome | PM still owns outcome (mandate: alpha vs benchmark, slippage, costs, taxes) | Must measure the "as-recommended vs as-executed" gap (R0 − R1) and own the rest |
| Agreement form | Schedule IV prescribed contents | For a Large Value Accredited Investor (LVAI: accredited + ≥ ₹10 Cr agreement) Schedule IV is not mandatory; exit load bilateral | Bespoke annexes for consent protocol, standing instructions, hedge protocol |

### 1.2 Regulatory perimeter (verified status as of 12-Sep-2026)

| Item | Rule | Status | Source |
|---|---|---|---|
| Client-direction requirement | NDPMS = funds managed per client directions; no independent discretion | verified (Reg 2, Reg 24) | SEBI PMS Regs 2020 [S1] |
| Unlisted securities | NDPMS/advisory ≤ 25% of AUM (AIF units, unlisted REIT/InvIT, unlisted debt, pre-IPO); ≤ 10% of AUM in unlisted unrated debt/hybrid of non-associates; LVAI: cap may be lifted to 100% by bilateral terms with Disclosure Document disclosure; discretionary PMS: listed only | verified (Feb-2020 circular 2020/26 via Master Circular); LVAI 100% partially_verified | [S2][S3][S6] |
| Below-investment-grade listed | Prohibited for NDPMS | verified | [S2] |
| Derivatives | Hedging/rebalancing; total exposure ≤ portfolio funds; PM shall not leverage; custodian before commodity derivatives | verified | [S1][S3] |
| Short selling / borrowing / margin | Not allowed (2026 draft proposes unhedged shorts ≤ 50% AUM within 1.25× exposure, option premium ≤ 10% — **not notified**) | verified as pipeline only | [S11] |
| Securities lending | Only via exchange SLB; client authorisation annex under NDPMS | verified | [S1] |
| Foreign securities inside PMS AUM | Not permitted today (2026 draft proposes "specified foreign securities") | verified as pipeline only | [S11] |
| Third-party PMS inside AUM | Not investable: a PMS is a service contract, not a security; Reg 24(10) bars investing on another entity's advice; First Global order (26-May-2026, ₹42 lakh penalty, 21-day onboarding bar) extends "investment decision" to quantities, timing and client-level execution | verified | [S12] |
| Outsourcing of investment decisions / model feeds | Prohibited | verified | [S12] |
| Associate / related-party securities (Angel One group) | One-time prior positive consent in Annexure A format; equity ≤ 15% single / 25% all associates; debt+hybrid ≤ 15% / 25%; combined ≤ 30% of AUM; no unrated associate debt; MF units excluded from the cap; alert-based monitoring; disclosure in every periodic report | verified (circular SEBI/HO/IMD/IMD-I/DOF1/P/CIR/2022/112, 26-Aug-2022) | [S4] |
| MF units | Direct plans only; no distribution-related fee to the client | verified | [S2] |
| Fees | No upfront fee; opex (ex-brokerage) ≤ 0.50% p.a. of average daily AUM; brokerage at actuals; exit load ≤ 3% / 2% / 1% in years 1/2/3, nil after; performance fee only on HWM basis; fee illustration (Annexure 4A) and typed fee acknowledgement at onboarding; MITC document mandatory (new clients from 1-Oct-2024). No SEBI cap on the headline fee % itself | verified | [S2][S3][S8] |
| Custodian | Mandatory for every PM except advisory-only (Reg 30). The pre-2020 ₹500 Cr AUM exemption no longer exists | verified (corrected, §13) | [S1] |
| Client reporting | Periodic report at an interval **not exceeding 3 months** (Reg 31), covering composition & value, transactions, beneficial interest received, expenses, risks, debt defaults/downgrades, associate exposure and distributor commission | verified: **Regulation 31** (not Reg 22 — corrected, §13) | [S1][S31] |
| Monthly regulatory report | To SEBI and APMI within 7 working days of month-end; TWRR per Investment Approach; IA tagged to one Strategy (Equity / Debt / Hybrid / Multi-Asset); ≤ 3 APMI benchmarks per Strategy; benchmark change requires exit-load-free exit; XIRR per investor with min/median/max across IA investors | verified (circular SEBI/HO/IMD/IMD-PoD-2/P/CIR/2022/172, effective 1-Apr-2023) | [S9] |
| Firm-level performance audit | Annual, DPMS + NDPMS combined; confirmation to SEBI within 60 days of FY-end; APMI standard ToR from 1-Oct-2023 | verified | [S10] |
| Debt / money-market valuation | Daily, MF-equivalent norms, APMI-empanelled agencies (CRISIL, ICRA Analytics, NSE Indices) | verified | [S9][S32] |
| Corporate-bond RFQ | ≥ 10% of secondary corporate-bond trades by value via exchange RFQ, rolling basis, since 1-Apr-2022 | verified | [S26] |
| Dealing-room controls | Time-stamping of order placement/execution/allocation; board-approved dealing-room policy; recorded communications; automated OMS mandatory at AUM ≥ ₹1,000 Cr (we build to it anyway) | verified (Master Circular) | [S3] |
| Draft PMS Regulations 2026 | Consultation paper 23-Jul-2026; comments closed 13-Aug-2026; not notified | verified as draft | [S11] |
| Block deals | ₹25 Cr minimum; windows 08:45–09:00 (prior close reference) and 14:05–14:20 (VWAP 13:45–14:00); ±3% band; compulsory delivery | verified | [S13] |
| Bulk-deal disclosure | > 0.5% of listed shares in a scrip in a day → same-day disclosure | approx. (not re-verified against primary) | [S14] |
| ETF direct-with-AMC | Orders ≥ ₹25 Cr may transact directly with the AMC at intraday NAV; exchange route compulsory below; ≥ 2 market makers per ETF (circular 2022/145, effective 1-May-2023) | verified | [S10b] |
| Settlement | Equity T+1 mandatory; optional T+0 for top-500 stocks; G-sec/SDL T+1; corporate bonds T+0 to T+2 via RFQ/CBRICS | verified | [S14] |

### 1.3 Consent design

The Rebalance Proposal Pack (RPP) is the legal "direction of the client". Its contents and mechanics are contractual (Annex B of the agreement):

| Element | Specification |
|---|---|
| Content per line | ISIN/scheme code, instrument, side, quantity **or** ₹ amount, execution channel (on-screen / block / AP-AMC / MFU-BSE StAR), participation or limit rule, execution window, one-line rationale, estimated cost (bps), estimated tax (STCG/LTCG flag and ₹), band-compliance flag, unlisted/associate headroom before-after |
| Format | Page 1: drift table, top 5–8 changes, total cost/tax, compliance annex summary, "Approve all" block. Appendix: full line list (hard cap 60 lines; every line ≥ ₹1.5 Cr except silver) |
| Approval | Aadhaar e-Sign / DSC on the portal (primary); OTP-authenticated email from registered IDs (fallback, flagged); recorded call + written confirmation within 24 h (escalation only) |
| Record | {rpp_id, client_id, line_items[], decision, channel, IST timestamp (NTP), signer, IP, device, SHA-256 of the PDF shown}, appended to a WORM ledger; 10-year retention |
| Validity | 10 trading days; unexecuted lines lapse; amendments require a new (partial) pack |
| SLA | Viewed within 4 business hours; decided within 2 business days; RM call at 48 h; CIO call at 72 h; escalation clock runs in business hours, holiday-adjusted, with a named on-call rotation |
| Entities | Individuals: e-Sign. HUF/trust/company: standing board/trustee resolution naming two authorised signatories plus a backup, refreshed annually; distinct sub-workflow with a 3-business-day SLA. Every individual signatory also executes the succession/incapacity annex (Annex D, below) at onboarding |
| Walkthrough | T-1 call sized at 45–60 minutes (not 30); engagement depth (questions raised, lines modified) tracked as a KPI so "approve all" does not degrade into a rubber stamp |
| Lapse clause | Every ad-hoc mini-RPP states: "Absent a response by [time], the recommendation lapses and current positioning continues unchanged" — silence is never implied consent |

Signatory succession and incapacity (Annex D — new; closes the gap between the 72-hour "unreachable" protocol and the entity-level backup-signatory rule):

| Event | Who may direct the portfolio | What runs automatically | What stops | Time limit / exit |
|---|---|---|---|---|
| Sole individual signatory temporarily unavailable (> 72 h, tail event) | nobody beyond signed standing instructions (§3.6) | SIs #1–#6 | all RPPs lapse on their own clock | until contact resumes |
| Incapacity (certified by two registered medical practitioners, or court order) | the **registered alternate**: a notarised, specific financial power-of-attorney holder named at onboarding per individual (PoA lodged with custodian, RTA and Ionic; KYC'd; refreshed every 2 years). Whether a PoA holder's direction satisfies Reg 24 is **unclear_verify** — covered by the same legal opinion as standing instructions (§10, 0–30 days) | SIs #1–#6 | nothing else until the alternate is activated (target ≤ 5 business days from certification) | alternate acts until recovery or death; IC minute records activation |
| Death of an individual holder | nobody until transmission: nominee holds as trustee for legal heirs (SEBI circular 19-Sep-2025 on nominee → legal-heir transmission; reporting code "TLH" — verified via secondary source), then executor / succession certificate / registered will; new agreement or novation with the heir/estate | **preservation mode**: SI #1 cash sweep, #2 distribution routing to the liquid fund only, #3 CA default (no action), #6 AIF capital calls (a contractual obligation of the estate — funded to avoid PPM default, executor notified same day) | no new RPPs; hedges are allowed to expire (no premium spend without a live instruction); deployment ladder frozen | if no competent instruction-giver exists within 30 days the account stays in preservation mode; disclosed in the next periodic report; if the heir is not accredited, LVAI terms revert to Schedule IV-compliant terms after the 90-day cure (§1.4) |
| HUF karta / trustee / director change | next karta by law; trustee per trust deed; fresh board resolution | as per resolution | RPP sub-workflow paused until resolution lodged | 3-business-day SLA restarts |

Tax and records on transmission: inheritance is not a transfer (cost and acquisition date carry to the heir — verified rule); nominee registration is mandatory on every demat account and MF folio; the WORM ledger records the PoA/transmission documents as consent-chain artefacts. Nothing in Annex D gives Ionic discretion: preservation mode is the *absence* of new directions, not a defensive mandate.

Standing Instructions Register (Annex C) — each item fully specified (trigger, instrument, quantity rule, maximum ₹, validity, revocable on the portal):

| # | Instruction | Trigger | Rule | Max ₹ | Status |
|---|---|---|---|---|---|
| 1 | Idle-cash sweep | Bank balance > ₹50 lakh at EOD | 100% of excess into the named overnight/liquid fund | uncapped (mechanical) | allowed_with_consent |
| 2 | Distribution routing | Dividend / coupon / AIF distribution received | Into the most under-target sleeve's named instrument, else the liquid fund | amount received | allowed_with_consent |
| 3 | Corporate-action default | Voluntary CA (rights, buyback, OFS) | Default = no action unless approved in an RPP or CA mini-RPP (rights subscriptions are "active" unlisted-cap events) | — | allowed |
| 4 | Approved tranche execution | Already-approved RPP line in its validity window | Exact ₹/quantity from the RPP, Monday redemption / Thursday deployment cadence | as per RPP | allowed |
| 5 | Hedge auto-roll | Approved put/put-spread within 5 trading days of expiry | Same notional, same moneyness, next monthly/quarterly series | premium ≤ 1% AUM p.a. | allowed_with_consent |
| 6 | AIF capital-call funding (new) | Drawdown notice from an IC-approved fund within disclosed commitment | Sweep from overnight/arbitrage sleeve up to committed-but-undrawn amount; client notified same day | committed-undrawn ₹ (disclosed in IPS) | allowed_with_consent |
| 7 | Deployment-ladder acceleration (new) | Nifty ≥ 5% / 10% / 15% below deployment-start level, or India VIX > 22 for 3 sessions | Phase 1: generates a pre-drafted one-click mini-RPP (24 h SLA). Phase 2 (post legal opinion): pull forward 1 / 2 / all remaining tranches into the named instruments | remaining approved tranches | unclear_verify → consent-generating until cleared |

Not in the register, ever: any instruction that lets the PM pick a new security, change a sleeve target, or choose timing/size after a generic approval. Trigger-based sell-side de-risking (band ≥ 1.5×, 200-DMA break, VaR breach) is consent-generating (pre-drafted mini-RPP) until counsel or SEBI Informal Guidance confirms a self-executing form is compatible with Reg 24. Legal opinion is a Phase 0–30 gating deliverable (§10).

Consent latency, stated correctly: for a mis-weight W at daily vol σ over d trading days, the 1-sigma **dispersion** of the delay's P&L is W × σ × √d. On ₹25 Cr at 1% daily vol: ₹25 lakh (1 day), ₹35 lakh (2 days), ₹56 lakh (5 days), ₹79 lakh (10 days). This is risk, not expected loss; the expected directional cost is (2 × IC hit rate − 1) × expected excess move × W — at a 55% hit rate and 0.5% expected move over a 3-day lag it is ≈ ₹1.25 lakh. We therefore budget latency as a risk (2-day SLA, standing instructions) and measure the realised cost trade-by-trade in the Perold decomposition (§6.3).

### 1.4 Accredited-investor route

| Question | Answer | Status |
|---|---|---|
| Thresholds (individual/HUF/family trust) | Income ≥ ₹2 Cr, or net worth ≥ ₹7.5 Cr (≥ 50% financial), or income ≥ ₹1 Cr + net worth ≥ ₹5 Cr (≥ 50% financial); corporates/non-family trusts: net worth ≥ ₹50 Cr; partners each qualify | verified |
| Proposed new route | ₹5 Cr securities-market assets (individual) / ₹20 Cr (corporate); manager-led accreditation — proposed Aug/Sep-2025, not notified | verified as proposal |
| Who accredits | BSE/NSE/NSDL/CDSL subsidiaries; CA net-worth certificate in the Jan-2026 format (circular 9-Jan-2026) | verified (format), validity 1–2 years approx. |
| LVAI | Accredited + PMS agreement ≥ ₹10 Cr per entity → Schedule IV not mandatory; bilateral fee/exit-load terms; unlisted cap may be raised (we self-cap at 15%) | verified |
| Collateral benefits | AIF ₹1 Cr minimum waived; SIF ₹10 lakh PAN minimum waived; eligible for CIV co-investment schemes (Reg 17A, Sep-2025) and Large Value Fund schemes (₹25 Cr minimum, down from ₹70 Cr) | verified |
| Lapse contingency (new) | Agreement clause: if accreditation is not renewed, the bespoke terms revert to Schedule IV-compliant terms after a 90-day cure; renewal tracker fires 120 days before expiry | design |
| Entity structuring (open) | The ₹500 Cr will likely sit across individuals, HUF, family trust and possibly a holding company. Each entity must independently accredit and sign ≥ ₹10 Cr; tax rate (39% slab vs 25.17% company), LRS vs OPI route, SIF/AIF minimums and the per-PAN LTCG exemption all depend on the split. **Decision for client counsel before IPS sign-off** (§12) | open |

### 1.5 Tax framework FY2026-27 (Income-tax Act 2025 in force from 1-Apr-2026; rates unchanged by Budget 2026; s.112A→198, s.111A→196)

Resident individual/HUF, top slab, new regime: surcharge 25% on slab income but capped at 15% on capital gains and dividends; cess 4%. Company under s.115BAA: 25.17% on income; capital-gains rates apply with the lower surcharge.

| Instrument | LTCG holding | LTCG (effective) | STCG (effective) | Income component | Transaction taxes | Status |
|---|---|---|---|---|---|---|
| Listed equity, equity MF/ETF (≥ 65% domestic equity), equity-oriented SIF, arbitrage funds | 12 m | 12.5% above ₹1.25 lakh/FY (14.95%) | 20% (23.92%) | Dividend at slab (35.88%); TDS 10% > ₹10,000 | STT 0.1% each leg (delivery); 0.001% on MF/ETF unit sale; stamp 0.015% buy (equity) / 0.005% (units) | verified |
| Debt / "specified" MF (> 65% debt, bought ≥ 1-Apr-2023), incl. TMF funds, liquid, short-duration, credit funds | none | none | slab (39.0%), any holding period, **on redemption** (deferral while held) | — | stamp 0.005% units | verified |
| Listed bonds, G-secs, SDLs | 12 m | 12.5% (14.95%) on price gain only | slab | Coupon at slab (39.0%) every year | stamp ≈ 0.0001% approx.; G-sec nil approx. | verified (rates) |
| Unlisted bonds / MLDs | none | none | slab, any holding | slab | — | verified |
| Gold / silver ETF (listed units) | 12 m | 12.5% (14.95%) | slab | — | stamp 0.005% | verified |
| Gold FoF / international FoF (unlisted units) | 24 m | 12.5% (14.95%) | slab | — | stamp 0.005% | verified |
| Indian-listed international ETF | 12 m | 12.5% (14.95%) | slab | — | stamp 0.005% | verified |
| SGB — primary subscriber to 8-yr maturity | 8 y | exempt (narrowed by Budget 2026 to original subscribers) | — | 2.5% coupon at slab | — | verified; no new issuance since Feb-2024 |
| SGB — secondary purchase or exchange sale | 12 m | 12.5% (14.95%) | slab | coupon at slab | — | verified |
| REIT / InvIT units | 12 m | 12.5% (14.95%) | 20% (23.92%) | Interest and rental at slab (TDS 10%); dividend exempt from 1-Apr-2026 under the Taxation and Other Laws (Amendment) Bill 2026 — **pending enactment, verify**; return-of-capital reduces cost | STT on units: treat as 0.1% until broker confirms (verify) | partially_verified |
| AIF Cat I / II | pass-through (s.115UB): taxed as if held directly; interest at slab (39.0%); TDS 10% u/s 194LBB; Finance Act 2025 deems fund securities capital assets | as underlying | as underlying | — | verified |
| AIF Cat III | fund-level: LTCG 12.5% + surcharge (≤ 15%) + cess; STCG 20% +; business/F&O income at MMR ≈ 42.7%; F&O STT from 1-Apr-2026: futures 0.05%, options premium 0.15% | fund-level | fund-level | investor receives post-tax NAV | verified |
| SIF (hybrid long-short, equity-oriented) | MF taxation by scheme category — equity-oriented → 12.5%/20%; verify per scheme | — | — | — | partially_verified |
| PMS fees | 18% GST; deductibility against capital gains contested (Devendra Kothari line disallows; contrary rulings exist) — model as **non-deductible** in R3/R4 | — | — | — | verified (contested) |

Rules derived from the table (each is a design rule, not commentary): (i) FIFO applies per demat account (s.45(2A); CBDT Circular 768) and specific identification is not available — account structure is the only lever; (ii) no wash-sale rule, so LTCG-exemption harvesting (sell and rebuy) is legal, but s.94(7)/(8) dividend- and bonus-stripping windows (3 m before / 3–9 m after) apply; (iii) STCL offsets any capital gain, LTCL only LTCG, carry-forward 8 years with on-time ITR; (iv) coupon income is slab-taxed whether held directly or via a fund — the fund wrapper's advantage in fixed income is **deferral** (tax on redemption) plus diversification, the direct bond's advantage is the 12.5% LTCG on price gain only; (v) in-specie transfer-in is not a transfer — capture cost and acquisition date at the custodian on day 1.

### 1.6 RBI / FEMA and the international sleeve

| Route | Cap | Status FY2026-27 | ₹500 Cr implication |
|---|---|---|---|
| MF industry overseas limit | USD 7 bn industry + USD 1 bn overseas-ETF pool; ≈ USD 1 bn per AMC | Near-exhausted through 2026; several AMCs paused lump sums; no increase announced (verified) | Fresh FoF subscriptions intermittent; Indian-listed international ETFs trade at 5–15% premiums when creations pause (approx.) — buy only at ≤ 1% premium to iNAV |
| LRS | USD 250,000 per resident individual per FY; TCS 20% above ₹10 lakh (creditable) | Unchanged | ≈ ₹2.39 Cr per adult at 95.79; 5 adults ≈ ₹12 Cr/yr; ≈ ₹2.4 Cr TCS locked until ITR credit; sits **outside** NDPMS AUM |
| GIFT-IFSC outbound funds | Within LRS for individuals | ≈ 5 outbound retail funds (min ≈ USD 5,000); IFSC PMS min ≈ USD 75,000 (approx.) | Preferred LRS destination; IFSCA-regulated |
| OPI by an Indian company | Listed company ≤ 50% of net worth; unlisted entity via IFSC fund units (Schedule V) | Unchanged | Scalable only if the family has a corporate vehicle |
| Inside NDPMS AUM | Foreign securities not permitted today | 2026 draft pending | In-AUM international = Indian-listed international index funds / FoFs / ETFs only |

Design: in-AUM international target 5% (₹25 Cr) with a 2.5–7.5% band; household look-through target 7.5–10% including the advised LRS/IFSC sleeve outside AUM; report both, tagged "inside AUM" vs "advised". An LRS-utilisation and TCS-credit tracker per family member is part of the consolidated client dashboard (§8).

NRI / FEMA branch (outline design — activates for any beneficial owner who is a non-resident; residency is confirmed for every entity on day 1 of the roadmap):

| Dimension | Resident base case (this blueprint) | NRI branch | Status |
|---|---|---|---|
| Eligibility and accounts | resident bank + 3 purpose demat accounts | NRIs may hold PMS; funds via NRE (repatriable) or NRO (non-repatriable) bank accounts; PIS permission from the designated AD bank for listed equity on a repatriation basis; ₹50 lakh PMS minimum applies (LVAI ≥ ₹10 Cr unchanged) | verified (secondary) |
| Custody structure | Core / Tactical / Harvest | the same purpose split **per repatriation status** (NRE-PIS and NRO demats cannot be mixed) → up to 6 accounts; FIFO per account unchanged | design |
| Listed-equity caps | none beyond PMS limits | individual NRI ≤ 5% of a company's paid-up capital on repatriation basis; aggregate NRI ≤ 10% (24% by special resolution) — FEMA NDI Rules, Schedule 3 | approx. — verify current schedule text |
| MF / index funds / ETFs / SIF | direct plans | permitted; US/Canada persons only via FATCA-compliant AMCs (several restrict) | verified (practice) |
| AIF / REIT / InvIT units | ≤ 15% IPS unlisted | permitted for NRIs on a repatriation basis under the NDI Rules schedule for investment vehicles | verify |
| G-sec / SDL | NDS-OM via custodian | via the Fully Accessible Route / NRO route | verify |
| International sleeve | 5% in-AUM + LRS outside AUM | LRS does not apply to NRIs; the outside-AUM international sleeve is funded directly from foreign assets (or GIFT-IFSC); in-AUM 5% via Indian-listed vehicles unchanged | verified (principle) |
| Tax | slab / 14.95% / 23.92% | same capital-gains rates and ₹1.25 lakh s.112A exemption; **TDS at source on every gain and on dividends (s.195 / s.196)** — a cash-flow drag the R3 engine must model; DTAA relief and TRC per residence country; slab surcharge rules as for residents | verified (rates); DTAA verify per country |
| Repatriation | n/a | NRE proceeds freely repatriable; NRO ≤ USD 1 million per FY after tax | verified (secondary) |
| Consent channel | Aadhaar e-Sign | Aadhaar e-Sign frequently unavailable → DSC primary, OTP e-mail + recorded video call fallback; SLA clock runs in the client's local business hours (+1 business day on the 2-bd SLA) | design |
| Reporting | Reg 31 pack | plus PIS reporting by the designated bank; TDS certificates (Form 16A) in the annual tax pack | design |

Rule: an NRI entity is a separate agreement and IA account within the same Investment Approach; its SAA is the same Model Master, but its RPP is generated separately (different demat routing, TDS-aware tax lines) and its lines never net against resident entities. If the NRI share of the ₹500 Cr exceeds 25%, the international sleeve and gold weights are revisited (the household already carries USD exposure outside AUM).

---

## 2. Investment architecture

### 2.1 Capital-market assumptions (10-yr forward, INR, pre-tax, gross of our fee)

Method: equity = dividend yield (~1.2%) + real earnings growth + inflation (~4.5%) ± valuation drift (Nifty at ~20× trailing vs 23.3× 10-yr median → ≈ +1% p.a. tailwind, netted against slower nominal growth); bonds = YTM ± roll; gold = INR depreciation (~3.5% approx.) + real-rate/central-bank premium; alternatives = manager target net of fees, haircut 200–300 bps for selection risk. Correlations are approx. (Appendix A, Table A3) and must be re-estimated from downloaded TRI histories before IC sign-off.

| Asset (proxy) | Historical anchor | Fwd E[R] | Fwd vol | Hist. max DD | Corr to Nifty 50 | Note |
|---|---|---|---|---|---|---|
| Indian large cap (Nifty 50/100 TRI) | Nifty 50 TRI 20-yr CAGR 12.44% to Feb-2026 (verified); 10-yr ≈ 13.7–14.0% (approx.); max DD −59.9% (2008) | 11.0% | 17% | −60% | 1.00 | valuation ≈ 15% below 10-yr median P/E |
| Mid cap (Nifty Midcap 150 TRI) | 10-yr CAGR ≈ 18% (approx.); −14% Jan–May 2026, new peak 21-Jul-2026 (verified) | 12.5% | 21% | −73% approx. (2008-09) | 0.85 | highest Sharpe of the cap buckets historically |
| Small cap (Nifty Smallcap 250 TRI) | 10-yr ≈ 15% (approx.); −61% Jan-2018→Mar-2020 (verified); ~25% of 3-yr windows negative | 13.0% | 25% | −78% approx. | 0.75 | loses to Midcap 150 in ~80% of 5-yr windows |
| Factor: Quality (Nifty 200 Q30) | SI ≈ 16–17% approx.; lagged 2021–24 | 11.0% | 16% | −55% approx. | 0.90 | cheap after 3-yr lag; fits house view |
| Factor: Low Vol (Nifty 100 LV30) | SI ≈ 16% approx.; beta ≈ 0.75 | 10.5% | 14% | −50% approx. | 0.85 | defensive |
| Factor: Momentum (Nifty 200 Mom 30) | SI ≈ 19–20% approx.; 2008 ≈ −70%; turnover 100–150%/yr | 13.0% | 22% | −70% approx. | 0.80 | crash-prone at turns; cap 2–4% |
| Factor: Value (Nifty 500 Value 50) | P/E 10.37 (verified); Jan-18→Mar-20 ≈ −60% | 12.0% | 25% | −75% approx. | 0.90 | PSU/cyclical heavy |
| Short duration / money market | Liquid fund 1-yr ≈ 6.4%; CRISIL Liquid 10-yr ≈ 6.3% approx. | 6.6% | 1.2% | ~0 | 0.05 | slab-taxed |
| Target maturity 3–5 yr AAA PSU/SDL | Bharat Bond 2030 5-yr 6.83% to Jul-2026; YTM ≈ 7.0–7.4% approx. | 6.9% | 2.5% | −4% approx. | 0.05 | hold to maturity; slab on redemption |
| 10-yr G-sec | YTM ≈ 7.0% (verified); 2013: +200 bp in 3 months | 7.0% | 5.5% | −10% approx. | 0.10 | duration lever; positively correlated with USD/INR shocks |
| AA corporate credit | AA spread 100–260 bps approx.; 10-yr AAA–G-sec ≈ 221 bps (15-Aug-2026) | 8.2% | 3.5% | −8% approx. | 0.15 | capped 2% of AUM |
| Arbitrage | Nifty 50 Arbitrage Index ≈ 4–8.5%/yr; 1-yr SD 1.41% | 6.2% | 0.7% | ~0 | 0.05 | equity-taxed parking asset |
| Gold (INR) | 20-yr ≈ 15%, 10-yr ≈ 18% (approx.); 2025 ≈ +74% approx.; ₹1,52,650/10 g | 8.0% | 15% | −25% approx. (2013–15) | 0.00 | hedge value via USD/INR channel; failed in Mar-2020 liquidity crunch |
| Silver (INR) | SD ≈ 26.6%; max DD −54%; Oct-2025 ETF premiums 8–10% on creation pauses | 8.5% | 27% | −54% | 0.20 | tactical only, cap 1% |
| REIT / InvIT | Index 1-yr +22% (Apr-2026); Embassy yield ≈ 6.5%, IndiGrid 9–10% | 9.5% | 14% | −40% approx. | 0.35 | multi-component tax |
| International DM equity (S&P 500 TRI in INR) | MO S&P 500 fund 5-yr 17.6% INR (verified); INR −3.5 to −4%/yr | 10.5% | 16% | −35% approx. (INR) | 0.45 | access-constrained |
| Cat II private credit AIF | net 12–16% (approx., low confidence); rising default chatter 2026 | 11.5% net pre-tax | 4% smoothed (≈ 10% economic) | −15% approx. | 0.20 | interest at slab |
| Cat III long-short AIF | fund-level tax; trust MMR on business income | 10.0% net pre-tax | 9% | −20% approx. | 0.40 | use only where SIF unavailable |
| SIF hybrid long-short | category AUM ₹13,814 Cr (May-2026); < 18 months live | 10.0% net pre-tax | 9% | −20% approx. | 0.40 | investor-level equity tax; **separate row (corrected)** |
| Pre-IPO / PE (Cat II) | target 18–22% gross approx.; J-curve 3–4 yrs | 15.0% | 25% | −40% approx. | 0.50 | Aggressive only, 3% |

Uncertainty bands on the illiquid CMAs (new, per critique): Cat II private credit 8–14% (downside = 2 defaults in a 10-name senior book); Cat III / SIF 5–12%; pre-IPO 5–20%. Size alternatives on the downside case, not the point estimate.

### 2.2 Sleeve design (corrected five-sleeve summary — foots to 100%)

| Sleeve | Purpose | Moderate | Aggressive | Instruments | Band |
|---|---|---|---|---|---|
| Core beta | cheap, capacity-unlimited Indian large-cap + factor tilts | 32% | 37% | Nifty 50/100 ETFs via AP + index fund; Quality / Low Vol / Momentum index funds | ±5 sleeve; ±2 per factor |
| Satellite alpha | where we own selection: active mid/small MFs, NIFTY-750 direct book, international | 23% | 34% | 2 mid-cap + 1–2 small-cap MFs; 20–30 direct names; 1–2 international index funds/FoF + 1 ETF backup | ±3 sleeve; ±1.5 per line |
| Alternatives | return sources not in listed markets; manager discretion inside wrapper | 9% | 12% | 2 Cat II private credit; 1 Cat III LS; 1 SIF hybrid LS; (Agg) 1–2 pre-IPO Cat II | ±2; no forced rebalancing |
| Stabilisers | drawdown control and carry | 34% (24 FI + 4 REIT/InvIT + 6 gold/silver) | 15% (8 + 2 + 5) | TMF funds, direct 10-yr G-sec, AA credit fund, short-duration fund; 4–5 listed REIT/InvITs; gold ETF; silver ETF | ±3 FI; ±1 REIT; ±1.5 gold; ±0.25 silver |
| Liquidity | fee/tax/latency buffer, deployment parking | 2% | 2% | arbitrage fund (equity-taxed); overnight fund for < 1 week | 1–4% hard range |
| **Total** | | **100%** | **100%** | | |

Third-party PMS (one concentrated mid/small specialist, ₹10–15 Cr) is **outside** the sleeve tables and outside NDPMS AUM: separate client–PM contract, own demat/bank, reported look-through in the consolidated client view, with Ionic's distributor commission (if any) disclosed under the same conflicts protocol as group products.

### 2.3 Instrument-choice logic

Score each candidate 1–5 on cost (20%), tax form (20%), liquidity (15%), capacity (15%), alpha evidence (15%), NDPMS consent friction (15%); nothing below 3.0 is used. Passive unless the segment passes all three: documented manager-alpha persistence (Indian mid/small yes; large cap no), our ticket ≤ 1% of scheme AUM, net-of-tax expected alpha ≥ TER differential + 100 bps.

| Vehicle | Cost (bps p.a.) | Tax form | Liquidity | Capacity at ₹500 Cr | Consent friction | Verdict |
|---|---|---|---|---|---|---|
| Index ETF via AP / AMC-direct (≥ ₹25 Cr) | 3–10 TER + 4–6 execution | equity 12.5% LTCG | T+1; creation T+2 | unlimited (SBI Nifty 50 ETF > ₹2 lakh Cr; NIFTYBEES ₹66,777 Cr AUM on 9-Sep-2026 — verified, conflict closed) | low | core beta, gold |
| Index fund (direct plan) | 10–20 TER, zero spread | equity | T+2/T+3 | unlimited | lowest (NAV order; no price risk in consent lag) | core beta, factors, international, monthly-rebalanced sleeves |
| Active MF (direct) | 60–110 TER | equity | T+2/T+3 | ticket ≤ 1% of scheme AUM → scheme ≥ ₹2,500 Cr for a ₹25 Cr line | low | mid/small only |
| Third-party PMS | 100–250 + performance | client-level trades | 1–4 weeks | ₹50 lakh minimum; manager capacity | low after onboarding | outside AUM; one manager, ≤ 3% look-through |
| Direct stocks (NIFTY-750 scorecard) | 0 TER; 12–15 execution incl. impact | we control realisation | 1–3 days at 20% ADV | ≤ 1% of float; ADV ≥ ₹20 Cr | highest (every trade a consent line) | 8–12%; turnover < 30% |
| AIF Cat II | 150–200 + carry | pass-through; interest at slab | locked 3–7 yrs | ₹1 Cr minimum (waived for AI); counts in 25% unlisted cap | low after commitment | private credit, PE |
| AIF Cat III | 150–250 + performance | fund-level, up to MMR | monthly/quarterly; soft lock 1–3 yrs | ₹1 Cr | low | only where no SIF equivalent |
| SIF | 100–150 approx. | investor-level equity tax (scheme-dependent) | daily–quarterly; notice ≤ 15 working days | ₹10 lakh PAN minimum (waived for AI) | low | preferred long-short wrapper; cap 3–5% until 2027-28 track record |
| Direct G-sec / SDL | 0 TER; 3–8 bid-offer | coupon slab; LTCG 12.5% on price | T+1 deep (NDS-OM via custodian/PD) | fine | medium (each ISIN a line) | 10-yr duration lever |
| TMF index funds / ETFs (Bharat Bond, SDL-dated) | 15–20 TER | slab on redemption (deferred) | NAV route (Bharat Bond ETFs trade ₹2–10 Cr/day — never on screen for size) | fine | low | laddered AAA/SDL core |
| Corporate bonds direct | 0 TER; 5–25 spread; RFQ ≥ 10% | coupon slab | patchy | lots ₹1–5 Cr | medium | not below a ₹50 Cr sleeve → funds |
| REIT / InvIT (listed) | 0 TER; 15–30 spread | multi-component | 1–5 days | 4–5 names, ≤ ₹6 Cr each | low | stabiliser yield |
| Arbitrage fund | 35 TER | equity-taxed | T+1/T+2 | unlimited (Kotak Arbitrage ≈ ₹74,000 Cr) | low | cash > 1 month, deployment parking |

### 2.4 The two canonical model portfolios (₹500 Cr)

**Moderate (target: match the 80/20 house benchmark's return at ≈ 70% of its volatility; beat the Policy Composite net of fees)**

| Line | % | ₹ Cr | Instrument (# lines) | E[R] contrib (pp) | Days to liquidate at 20% ADV | Band |
|---|---|---|---|---|---|---|
| Nifty 50 / 100 passive | 22 | 110 | 2 ETFs via AP + 1 index fund (3) | 2.42 | 1–2 | ±5 |
| Factor blend Quality 5 / Low Vol 3 / Momentum 2 | 10 | 50 | index funds (3) | 1.15 | 2–3 | ±2 each |
| Active mid cap | 7 | 35 | 2 MFs (2) | 0.88 | 3 | ±1.5 |
| Active small cap | 3 | 15 | 1 MF (1) | 0.39 | 3–5 | ±1 |
| Direct stocks (scorecard, quality tilt) | 8 | 40 | 20–25 names, avg ₹1.6–2.0 Cr | 1.00 | 1–3 | ±3 sleeve; 50 bps per name |
| International DM (S&P 500 / MSCI World) | 5 | 25 | 1–2 index funds/FoF + ETF backup (2–3) | 0.52 | 3–5 if windows open | 2.5–7.5 |
| Short duration / money market | 3 | 15 | 1 fund (1) | 0.20 | 1 | ±1 |
| Target maturity 3–5 yr AAA/SDL | 13 | 65 | 2 TMF index funds/ETFs (2) | 0.90 | 2 (NAV route) | ±3 |
| 10-yr G-sec / dynamic duration | 6 | 30 | direct G-sec + 1 ETF (2) | 0.42 | 1 | ±2 |
| AA corporate credit | 2 | 10 | 1 corporate-bond/credit fund (1) | 0.16 | 3–5 | ±1 |
| Arbitrage / overnight | 2 | 10 | 1 arbitrage fund (1) | 0.12 | 1–2 | 1–4 |
| Gold | 5 | 25 | 1 gold ETF via AP (1) | 0.40 | 1 | ±1.5 |
| Silver | 1 | 5 | 1 silver ETF, iNAV-limit orders only (1) | 0.09 | 1 | ±0.25 |
| REIT / InvIT | 4 | 20 | 4–5 listed trusts (5) | 0.38 | 2–5 | ±1 |
| Cat II private credit AIF | 5 | 25 | 2 funds (2) | 0.58 | locked 3–5 yrs | 0–7.5, no forced trades |
| Cat III long-short AIF | 2 | 10 | 1 fund (1) | 0.20 | 30–90 | n/a |
| SIF hybrid long-short | 2 | 10 | 1 strategy (1) | 0.20 | 15–45 | n/a |
| **Total** | **100** | **500** | **≈ 50 lines** | **10.00** | 80% of book in ≤ 5 days | |

Checks: domestic equity 50%, unlisted 9% (AIF units) vs 25% legal / 15% IPS; AA credit = 2/24 = 8.3% of the FI sleeve (< 10% — credit floor satisfied); beta to Nifty 50 ≈ 0.55; ex-ante vol ≈ 9.7%; Sharpe (10.0 − 6.0)/9.7 = 0.41; 1-yr 95% VaR ≈ −5.9%; every line ≥ ₹1.5 Cr except silver. These 17 lines are exactly the `sample_allocation` array of blueprint_data.json v1.1 (short-duration 3% + arbitrage 2% appear there as one 5% cash row).

**Aggressive (target: beat the Policy Composite by ≥ 75 bps net at ≤ its risk)**

| Line | % | ₹ Cr | Instrument (# lines) | E[R] contrib (pp) | Band |
|---|---|---|---|---|---|
| Nifty 50 / 100 passive | 25 | 125 | 2 ETFs + 1 index fund (3) | 2.75 | ±5 |
| Factor blend Quality 5 / Momentum 4 / Low Vol 3 | 12 | 60 | index funds (3) | 1.38 | ±2 each |
| Active mid cap | 10 | 50 | 2–3 MFs (3) | 1.25 | ±2 |
| Active small cap | 5 | 25 | 1–2 MFs (2) | 0.65 | ±1.5 |
| Direct stocks (scorecard) | 12 | 60 | 25–30 names, avg ₹2.0–2.4 Cr | 1.50 | ±3; 60 bps per name |
| International DM | 7 | 35 | 2 index funds/FoF + ETF backup (3) | 0.74 | 4–10 |
| Short duration | 2 | 10 | 1 fund | 0.13 | ±1 |
| Target maturity | 4 | 20 | 1 TMF | 0.28 | ±1.5 |
| 10-yr G-sec | 2 | 10 | direct | 0.14 | ±1 |
| Arbitrage / overnight | 2 | 10 | 1 fund | 0.12 | 1–4 |
| Gold | 4 | 20 | 1 ETF | 0.32 | ±1.5 |
| Silver | 1 | 5 | 1 ETF | 0.09 | ±0.25 |
| REIT / InvIT | 2 | 10 | 3 trusts | 0.19 | ±1 |
| Cat II private credit | 4 | 20 | 2 funds | 0.46 | 0–6 |
| Cat III LS AIF 2 / SIF hybrid LS 3 | 5 | 25 | 2 | 0.50 | n/a |
| Pre-IPO / PE Cat II | 3 | 15 | 1–2 funds | 0.45 | n/a |
| **Total** | **100** | **500** | **≈ 52 lines** | **10.94** | |

Checks: domestic equity 64%; unlisted 12%; beta ≈ 0.72; vol ≈ 12.5%; 1-yr 95% VaR ≈ −9.7%.

Portfolio statistics (model outputs; correlations approx.; stress rows now taken from the risk engine as the single canonical source — corrected):

| Metric | Allocate 80/20 | Moderate | Aggressive |
|---|---|---|---|
| E[R] pre-tax, gross fee | 10.0% | 10.0% | 10.9% |
| Vol | 13.6% | 9.7% | 12.5% |
| Sharpe (Rf 6.0%) | 0.29 | 0.41 | 0.39 |
| Beta to Nifty 50 | 0.80 | 0.55 | 0.72 |
| 1-day VaR 95% / 99% | 1.41% / 1.99% (₹7.1 / ₹10.0 Cr) | 1.00% / 1.42% (₹5.0 / ₹7.1 Cr) | 1.30% / 1.84% (₹6.5 / ₹9.2 Cr) |
| 1-month VaR 95% / 99% | 6.46% / 9.14% | 4.59% / 6.49% | 5.95% / 8.42% |
| GFC-type shock (2008-09 re-priced) | ≈ −47% (data pack) | −32.0% (−₹160 Cr) | −43.0% (−₹215 Cr) |
| COVID-type shock (Feb–Mar 2020) | ≈ −30% | −22.8% (−₹114 Cr) | −28.8% (−₹144 Cr) |
| 2022 rate shock | ≈ −14% | −10.0% (−₹50 Cr) | −13.6% (−₹68 Cr) |
| Ex-ante TE vs T2 composite | — | 1.5–2.0% | 2.0–2.5% |
| Ex-ante TE vs 80/20 | — | 4.8% | 3.2% |
| CMA-implied gross alpha vs T2 | — | ≈ +55 bps | ≈ +45 bps |

### 2.5 Composite benchmark (T2) — single canonical definition

| Component (index, TRI where it exists) | Moderate | Aggressive | Reset | Note |
|---|---|---|---|---|
| Nifty 500 TRI | 50% | 64% | monthly | broad index so mid/small tilts count as TAA, not selection |
| S&P 500 TRI in INR (unhedged) | 5% | 7% | monthly | FX pass-through shown separately |
| Nifty Composite Debt Index (fallback: CRISIL Composite Bond Fund Index) | 24% | 8% | monthly | verify exact series name on niftyindices |
| Nifty REITs & InvITs Index (TR if available) | 4% | 2% | monthly | REITs benchmarked to REITs, not arbitrage (corrected) |
| Domestic gold spot (IBJA/MCX) | 5% | 4% | monthly | |
| Domestic silver spot | 1% | 1% | monthly | |
| Nifty 50 Arbitrage Index | 2% | 2% | monthly | house cash proxy |
| Private-credit proxy: Nifty Composite Debt + 300 bps p.a. | 5% | 4% | quarterly, 1-q lag | PME (Kaplan-Schoar vs Nifty 500 TRI) reported separately |
| Long-short proxy: 50% Nifty 50 Arbitrage + 50% Nifty 500 TRI | 4% | 5% | monthly | Cat III + SIF |
| PE proxy: Nifty 500 TRI + 300 bps p.a. | — | 3% | quarterly, 1-q lag | Aggressive only |
| **Total** | **100%** | **100%** | | buy-and-hold within month, reset to policy weights on first business day |

T1 (regulatory): the IA is tagged Multi-Asset and one of APMI's three prescribed Multi-Asset benchmarks is selected (the current list could not be fetched this cycle — **verify** on apmiindia.org before the Disclosure Document). T3 (reference): 80% Nifty 50 TRI + 20% Nifty 50 Arbitrage Index (Allocate) and the Nifty Multi Asset 50:20:20:10 index. Expected behaviour to be written into the agreement: the Moderate book is designed to deliver the 80/20's long-run return at ~70% of its volatility and will **trail 80/20 by 1–2 pp in strong equity years** and lead in drawdowns. Whether T2 may appear next to T1 in client marketing is unclear_verify with APMI/compliance; T1 always appears wherever performance is shown.

### 2.6 Capacity and liquidity at ₹500 Cr

| Constraint | Number | Rule |
|---|---|---|
| ETF on-screen depth | all-ETF ADV ≈ ₹4,200 Cr but equity ETFs ≈ ₹745 Cr/day; NIFTYBEES ₹200–400 Cr/day (approx.) | any ETF leg ≥ ₹25 Cr goes AP/AMC-direct; ≥ ₹5 Cr goes AP; on-screen only for top-ups < ₹5 Cr; anything with ADV < ₹50 Cr/day never on screen |
| Direct stock | ≤ 10–15% of 20-day ADV per session; ≤ 1% of free float; inclusion ADV ≥ ₹20 Cr; ≤ 3% of NAV per name | ~450 NIFTY-750 names qualify (approx.); ₹2 Cr position vs ₹20 Cr ADV = 0.5 day |
| MF scheme size | ticket ≤ 1% of scheme AUM (≤ 5% for passive) | ₹25 Cr mid-cap ticket → scheme ≥ ₹2,500 Cr; boutique small caps via the outside-AUM PMS |
| AIF | ₹1 Cr minimum (waived for AI); Cat I/II close-ended ≥ 3 yrs; single fund ≤ 5% of AUM, ≤ 2 funds per manager | 4–6 commitments of ₹5–15 Cr; drawn over 6–18 months |
| Unlisted cap | 25% legal (₹125 Cr); IPS 15% (₹75 Cr); alert at 18% | AIF NAV lag mechanically lifts the ratio in equity drawdowns (12% → ≈ 16% in a −30% equity move) |
| International | USD 7 bn cap; per-AMC USD 1 bn | 2 feeder routes + 1 ETF backup; hold in arbitrage if windows shut |
| Line count | 50–52 lines; hard cap 60; each ≥ ₹1.5 Cr except silver | consent-pack readability |
| Liquidity ladder (Moderate) | 44% same/next day; 36% in 2–5 days; 4% in 15–90 days (Cat III/SIF); 5% locked; 13% TMF (liquid via NAV, MTM if pre-maturity) | ≥ 80% liquidable in ≤ 5 days; ≥ 95% in ≤ 10 days |
| Client-side redemption stress (new) | a ₹100 Cr (20%) redemption is met from arbitrage 2% + passive equity + TMF pro-rata; alternatives ratio rises from 9% to ≈ 11%; a ₹250 Cr redemption pushes alternatives to 18% and needs a consent cycle to reset SAA | agreement states liquidity terms: up to 20% of AUM in T+5 business days, up to 80% in 30 days, balance on AIF liquidity |

### 2.7 House view → TAA translation rules

1. SAA is the contract (Model Master weights + bands in the IPS schedule). Band-restoring trades need confirmation, not deliberation.
2. TAA is the IC's monthly vote: conviction C ∈ {−3…+3} per axis (large vs mid/small; quality vs value/momentum; duration; credit; gold; international; alternatives pace).
3. Sizing: tilt (pp) = C × unit; unit = TE budget ÷ (Σ|C| × view vol); with TE budget 2.0% Moderate / 3.0% Aggressive vs T2, unit ≈ 1.0 pp / 1.5 pp; capped by the sleeve band.
4. Evidence bar: at least two of (a) valuation z-score |z| ≥ 1 vs 10-yr history, (b) revision breadth in the view's direction ≥ 2 months, (c) scorecard pillar spread in top/bottom quintile. C = ±3 needs all three plus IC unanimity.
5. Decay: every tilt carries a 6-month review; unreaffirmed tilts halve automatically in the next RPP.
6. Thresholds: aggregate active weight ≤ 10 pp Moderate / 15 pp Aggressive; TAA turnover ≤ 10% of NAV per month; minimum trade ₹1 Cr; every TAA call ≥ ₹5 Cr; TE hard stop 3.5% / 4.5%.

Worked September-2026 example (Moderate): large-cap quality +2, small cap −2, duration +2, gold 0 → Quality fund 5 → 7 (+₹10 Cr); small-cap MF 3 → 2 (−₹5 Cr, band-capped) and mid cap 7 → 6 (−₹5 Cr); direct 10-yr G-sec 6 → 8 (+₹10 Cr) funded from TMF 13 → 11 (−₹10 Cr). Gross turnover ≈ ₹40 Cr (8% of NAV); TE added ≈ 0.6%; five RPP lines plus band restorations, all executable on Thursday tranches.

### 2.8 Deployment plan for the fresh ₹500 Cr

Baseline (three tracks, mirrored line-for-line in `deployment_plan` of the data pack): **8 weekly Thursday tranches of ₹37.5 Cr** for the ₹300 Cr equity-like core (domestic equity ₹250 Cr + international ₹25 Cr + gold ₹25 Cr), a **₹25 Cr stabiliser closing tranche** in week 8 (REIT/InvIT ₹20 Cr + silver ₹5 Cr on iNAV-limit orders), **4 tranches of ₹30 Cr** for fixed income (₹120 Cr, weeks 0–3), **alternatives ₹45 Cr** committed in week 0 and drawn on manager schedules over 6–18 months, and the permanent **₹10 Cr (2%) arbitrage sleeve**: 325 + 120 + 45 + 10 = ₹500 Cr. At ~20× trailing P/E with Nifty ≈ 8–10% off its 2026 peak the IC's call is 8 weeks with acceleration armed; 12 weekly equity tranches of ₹25 Cr is the conservative alternative (cash drag ≈ ₹2.0–2.5 Cr vs ≈ ₹1.4–1.7 Cr). All undeployed money sits in an arbitrage fund (equity-taxed), not a liquid fund (slab-taxed) — worth ≈ 15 bps post-tax on the parked balance for a 39%-slab client.

| Week | Equity-like (₹300 Cr + ₹25 Cr closing) | Fixed income (₹120 Cr) | Alternatives (₹45 Cr committed) | Cumulative deployed | Parked in arbitrage |
|---|---|---|---|---|---|
| 0 | ₹37.5 Cr (tranche 1 of 8; first RPP also carries the 95/85 put-spread hedge at VIX 12.4) | ₹30 Cr (1 of 4) | commitments signed, undrawn | 13.5% | ₹432.5 Cr |
| 1–3 | ₹37.5 Cr/week (tranches 2–4) | ₹30 Cr/week — complete at end of week 3 | — | 54.0% | ₹230.0 Cr |
| 4 | ₹37.5 Cr (tranche 5); **mid-deployment re-confirmation by client (one click)** | — | first capital call ≈ ₹5 Cr funded via SI #6 | 62.5% | ₹187.5 Cr |
| 5–7 | ₹37.5 Cr/week (tranches 6–8; equity-like ₹300 Cr complete at week 7) | — | — | 85.0% | ₹75.0 Cr |
| 8 | closing tranche ₹25 Cr (REIT/InvIT ₹20 Cr + silver ₹5 Cr) and band true-up; ladder closed | — | — | 90.0% | ₹50.0 Cr = ₹40 Cr undrawn commitments + ₹10 Cr (2%) arbitrage sleeve |
| months 3–18 | — | — | ≈ ₹40 Cr drawn as called (≈ 25%/quarter) via SI #6 | 98% + undrawn | ₹10 Cr (target sleeve) |

Acceleration rules (pre-drafted mini-RPPs, 24-hour SLA in Phase 1; standing instruction #7 in Phase 2): Nifty ≥ 5% below the week-0 level → one extra tranche; ≥ 10% → two extra; ≥ 15% → deploy all remaining equity within 2 weeks; India VIX > 22 for 3 sessions counts as −5%; 10-yr yield ≥ 25 bps above week-0 → pull forward the duration tranche. Never decelerate on rallies. Expected one-off cash drag: equity ≈ ₹1.4–1.7 Cr (8 weeks) vs ₹2.0–2.5 Cr (12 weeks); fixed income ≈ ₹0.05 Cr; alternatives (committed-undrawn) ≈ ₹0.8–1.6 Cr over the drawdown period. In-specie transfer-in of legacy holdings (if any) is mapped to the model on day 1 with cost/date capture; legacy regular-plan MF units are switched to direct plans only via a tax-aware schedule in the RPP.

---

## 3. Operating cadence

All times IST. "T0" is the first Thursday of the month (consent day); Thursday is the house deployment day and Monday the redemption day. Owners: PM (dedicated portfolio manager), RA (research analyst), Risk, Dealing, Ops (ops/fund accounting), Compl (compliance), RM (relationship manager), Data (pipeline engineer), IC (investment committee), CIO.

### 3.1 Daily

| Time (IST) | Task | Owner | Output / control |
|---|---|---|---|
| 01:00 | Ingest: AMFI NAVs, NSE/BSE bhavcopy and index files, custodian EOD holdings/cash/transactions, RTA folio feed, APMI-empanelled debt valuations, CCIL G-sec data, depository corporate-action file, RBI reference FX, IBJA gold/silver | Data (automated) | raw files archived with checksums |
| 01:30 | Validate: schema, stale-feed flags, holdings row-count vs ledger, NAV day-over-day outliers (> 0.5% on a debt instrument = alert) | Data (automated) | validation log |
| 02:00 | Compute: daily TWRR R0–R4 (client, sleeve, T1/T2/T3), IPS drift, VaR/CVaR/EWMA/TE/drawdown, 14-limit utilisation and metric bands, liquidity ladder, recon break detection, fee accruals, consent-tracker status | Data (automated) | computed dataset (parquet) |
| 02:30 | Publish: regenerate the five HTML dashboards (IPS drift, deployment, attribution/TWRR, tail-risk, consent tracker) + cost/tax and recon boards | Data (automated) | static build to internal host |
| 06:00 | Feed-recovery SLA: any feed still stale → Ops pulls the prior validated file, flags it, notifies Risk/PM | Ops | flagged dashboard, no silent gaps |
| 06:30 | Pre-market check: recon exceptions, CA calendar and election deadlines, cash ladder for the day's tranche, MF cut-off plan, block-window candidates | Ops + Dealing | day sheet |
| 07:30 | Risk read: 1-day/1-month VaR, EWMA vol, TE, drawdown vs −18% trigger, early-warning board (any Red → same-day IC e-mail; ≥ 2 Ambers → IC flag), limit grid (> 90% utilisation = amber) | Risk | risk flash to CIO/PM |
| 08:30 | Block-deal window candidates (≥ ₹25 Cr single lines) queued for 08:45–09:00 | Dealing | pre-trade compliance stamp |
| 09:15–15:30 | Execute approved-and-live RPP lines per participation rules (≤ 10–15% ADV per session; VWAP/TWAP > 2% ADV); MF orders before 13:30 (liquid/overnight) and 15:00 (others) cut-offs; iNAV check on every ETF order (abort if |premium| > 15 bps, route AMC-direct) | Dealing | fills time-stamped in OMS with rpp_id |
| 10:00 | NAV flash: NAV, daily/MTD/FYTD R1/R2 vs T1/T2/T3, sleeve contributions, pending consents with age, stale-price %, band breaches, top movers | Ops/Performance | daily flash to PM, Risk, RM |
| 15:30–17:00 | Idle-cash sweep (standing instruction #1); distribution routing (#2); post-close fills reconciled into OMS; T+1 settlement queue built; consent ledger integrity (every order has a valid FK) | Ops + Dealing | zero unmatched orders |
| 17:00 | Corporate-action processing (dividends, bonus, splits per default instruction); CA needing election → CA mini-RPP triggered (RM contact within 4 business hours) | Ops + RM | CA log |
| 17:30 | Cash, holdings, MF-folio, CA, dividend/interest, fee-accrual and benchmark-data recons (T+1 AM for bank) — breaks > ₹10 lakh resolved same day | Ops | break tickets |
| event | Any single Red on the early-warning board, band breach ≥ 1.5×, VaR/drawdown breach: tail-event playbook §5.7 (first-hour confirmation, mini-RPP, client call within 2 hours) | Risk → CIO → RM | consent-latency log entry |

### 3.2 Weekly

| Day / time | Task | Owner |
|---|---|---|
| Monday 09:00 | Weekly summary to IC/RM: week/MTD TWRR vs T1/T2/T3, MTD Brinson, tranche status, ex-ante TE and factor tilts, drift vs bands, consents due, Thursday tranche list | Performance/PM |
| Monday 09:30 | Ops stand-up: tranche status, cash ladder, CA calendar, recon break ageing (> ₹25 lakh or > 5 days → Compliance and IC pack) | Ops |
| Monday | Redemption leg of the current RPP (sells) | Dealing |
| Tuesday | Risk stand-up: VaR/drawdown vs limits, early-warning board, hedge book, event-trigger screen (band ≥ 1.5×, equity aggregate > 3 pp, VIX/drawdown), rolling 60-day correlation | Risk |
| Wednesday | ADV/liquidity refresh for the direct-stock sleeve and ETF screen depth; AIF/PMS capital-call and distribution calendar | Risk/Dealing + Ops |
| Thursday | Deployment leg (buys), AP creations, MF purchases | Dealing |
| Friday | Risk-adjusted metric refresh (Table §6.5) with RAG; consent-latency roll-up; informal drift snapshot (monitoring only) | Performance + Risk |

### 3.3 Monthly cycle (see §4.1 for the T-minus calendar)

| Step | Day | Owner |
|---|---|---|
| Data close and golden EOD snapshot | T-5 | Ops |
| Drift report v1 (sleeve and line vs bands; unlisted %, associate %, derivative notional, credit floor, duration band) | T-5 | Risk/Compl |
| IC house-view meeting (last Wednesday): pillar scorecard, SAA drift, TAA conviction vote, RPP v0 | T-5/T-4 | IC |
| RPP v1 build (trades, ₹, channel, cost, tax, headroom) + pre-trade compliance sign-off | T-3 | PM + Compl |
| Client walkthrough (45–60 min) | T-1 | RM + PM |
| Consent (first Thursday) | T0 | Client |
| Execution window (Mon/Thu tranches) | T0 to T+7 | Dealing |
| Post-trade recon: fills vs RPP, realised slippage, Perold shortfall, cost/tax booked, weights vs SAA | T+8 | Ops + Performance |
| Monthly client statement (Reg 31 content, delivered monthly by commitment) and monthly pack | month-end + 5 business days | Ops/Compl/RM |
| SEBI/APMI monthly report (TWRR by IA, AUM, clients) | month-end + 7 working days | Compl |
| Cost/tax dashboard, attribution/TWRR refresh, manager look-through load (AMFI portfolios), consent-latency log review, model-version diff check | month-end + 5 | PM/Performance |
| LRS/TCS utilisation update per family member (quarterly minimum, monthly preferred) | month-end | RM |

### 3.4 Quarterly

| Task | Owner |
|---|---|
| IC scorecard (SAA, TAA, manager selection, security selection, implementation & consent, costs, taxes, valuation quality; −2…+2) | IC |
| Manager watchlist re-score (active MF semi-annual formal, quarterly capacity trigger; PMS; AIF ODD refresh); redemption recommendations queued to next RPP | PM/RA |
| Quarterly client report (Reg 31 content, signed; TWRR + XIRR with IA min/median/max) and review call | RM/Compl |
| Best-execution TCA: Angel One brokerage vs second broker; **group-instrument bucket reported separately** (every order tagged `group_instrument=true`; test: slippage ≤ non-group median + 3 bps; any miss → Compliance review + IC minute; §4.5) | Dealing/Compl |
| Compliance/audit: associate-limit audit, standing-instruction usage audit, AML/KYC refresh sample, SCORES/grievance log review | Compl |
| Index reconstitution pass-through check (Nifty 50/500 semi-annual, factor indices) | PM |
| TAA post-mortems (decision-quality matrix; hit rate; payoff ratio; correlation of calls with momentum) | CIO/PM |
| Hedge programme review (premium spend YTD vs 1% AUM budget; VIX regime) | Risk |
| Accreditation validity check (all entities); board/trustee resolutions for signatories | RM/Compl |

### 3.5 Annual

| Task | Timing | Owner |
|---|---|---|
| FY-end tax pack: LTCG exemption harvesting (₹1.25 lakh per PAN, coordinated with the client's personal book), loss harvesting and cross-sleeve netting, s.94(7)/(8) window check, FY capital-gains statement (FIFO lots) for ITR | Jan–Mar; statement by 30 Apr | PM + tax adviser |
| Firm-level performance audit (APMI ToR) and confirmation to SEBI within 60 days of FY-end | Apr–May | Compl |
| IPS/SAA and band-width review vs realised turnover, TE, cost, tax; CMA and benchmark refresh; model-version bump | Apr–Jun | IC |
| Annual client review: audited performance, full-year decomposition waterfall, TAA post-mortems, fee reconciliation, IC scorecard published to client | within 60 days of FY-end | CIO/RM |
| BCP drill (tail event + custodian outage); delegation-of-authority refresh; PI insurance renewal | H2 | Ops/Compl |
| Disclosure Document update; MITC re-issue if terms change; Annexure A associate consent refresh if the associate list changes | as required | Compl |
| Accreditation renewal (each entity), LVAI status confirmation | 120 days before expiry | RM |
| **Merge / IPS reconciliation (new, recurring)**: automated cross-check of Model Master YAML vs blueprint_data.json vs IPS PDF vs OMS/RMS limit config vs T2 weights vs TCO vs return waterfall (11-item `reconciliation_checklist` in the data pack: sums, ₹ Cr, limit values, fee bps, TE bands, single as-of snapshot, ladder totals, limit count, engine diffs, approx./verify labels); two-person sign-off; runs at every model-version bump, CMA refresh and before any client document — not only at FY-end | Apr–Jun with the CMA refresh; event-driven | Data + Risk (second reviewer) |
| **Stress-library validation (new)**: for every Nifty drawdown ≥ 5% in the year, realised NAV drawdown ÷ Nifty drawdown vs model-predicted capture on live weights (Moderate median 54%, Aggressive 71%; ±10 pp tolerance); after ≥ 3 episodes re-estimate sleeve betas/correlations and re-run §5.3 | per episode; annual review | Risk |
| Tax-adviser and index-licence/data-vendor engagement renewals (scope refreshed for law changes: IT Act 2025 rules, REIT dividend enactment, PMS Regulations 2026) | Mar | COO + Compl |

### 3.6 Event-driven

| Event | Response | SLA | Consent mode |
|---|---|---|---|
| Band breach ≥ 1.5× normal band; equity aggregate drift > 3 pp | Pre-drafted trim mini-RPP to the outer band edge (de-risk only) | same/next business day | consent-generating (Phase 1); standing instruction if cleared (Phase 2) |
| Nifty ≥ 5% below 20-day high or VIX > 22 for 3 sessions | Pull-forward of scheduled buys (deployment ladder); no sells without consent | 1 business day | mini-RPP / SI #7 |
| Nifty ≥ 10% below 20-day high or VIX > 25 | Tail-event playbook: one-page recommendation (hedge activation, accelerated deployment or trim) | client call within 2 hours; decision within 24 hours | ad-hoc mini-RPP with lapse clause |
| Large inflow > ₹10 Cr | Sweep to overnight same day; deploy 20%/week over 3 Thursdays into pre-approved mix | same day / 3 weeks | SI #1 + approved ladder |
| Redemption request | Fund from arbitrage/overnight first, then pro-rata trims away from under-target sleeves | 2 business days for the trim list | ad-hoc consent (amounts only) |
| AIF drawdown notice | Fund from overnight/arbitrage up to committed-undrawn | same day | SI #6 |
| Corporate action with election (rights, buyback, merger) | CA mini-RPP; "no response = no action" | RM contact within 4 business hours; decision within 3 business days | ad-hoc consent — never a standing instruction |
| Credit downgrade below AA− on any holding | Mandatory exit proposal | 5 trading days | mini-RPP |
| Client unreachable > 72 hours in a live tail event | Execute only what a signed standing instruction covers; IC emergency session documents "unable to act — no instruction" as the compliant outcome; disclose in next report | 72 hours | none beyond SIs (unclear_verify boundary; legal opinion) |
| Regulatory change (e.g., PMS Regulations 2026 notified) | Change-in-law clause: IC review within 30 days, re-paper consent scope | 30 days | client re-consent |

---

## 4. Monthly rebalance & execution policy

### 4.1 Cycle calendar

| Step | Day | What | Owner | SLA / output |
|---|---|---|---|---|
| 1 Data close | T-5 | NAV, holdings, accruals, CA frozen; ADV refresh | Ops | golden snapshot |
| 2 Drift report | T-5 | actual vs SAA by sleeve/line; breaches; unlisted/associate/derivative/credit/duration checks | Risk/Compl | drift v1 |
| 3 IC view | T-5/T-4 | tilts with conviction scores within governance thresholds | IC | signed tilt sheet |
| 4 RPP build | T-3 | every line with channel, rule, window, cost, tax, headroom; cash-flow-first netting applied before any sell | PM + Compl | RPP v1, pre-trade sign-off |
| 5 Walkthrough | T-1 | 45–60 min; engagement KPI logged | RM + PM | client Q&A closed |
| 6 Consent | T0 (1st Thursday) | e-sign whole/line-item; 10-trading-day validity | Client | hashed record |
| 7 Execution | T0 to T+7 | Mon redemption / Thu deployment; algo rules | Dealing | slippage ≤ 15 bps vs arrival |
| 8 Settlement | T+1 equity; T+1/T+2 MF; T+1 G-sec | pay-in/out, allotments | Ops/Custodian | zero fails |
| 9 Post-trade recon | T+8 | fills vs RPP; Perold shortfall; tax booked; weights | Ops/Performance | recon pack |
| 10 Statement | month-end + 5 bd | Reg 31 content monthly | Ops/Compl | statement |

Consent arrival vs tranches: if consent lands on T0, four Mon/Thu legs fit inside the 10-trading-day window; if it lands at the 48-hour escalation point only two do. Rule: lines unexecuted at window close lapse and are re-issued as a partial RPP the next business day (no extension), and the desk compresses to two tranches when consent arrives after T0+2.

### 4.2 Band design and the quantified policy comparison

Design choices: absolute (pp) bands for large/liquid sleeves; relative bands of 20–25% of target for small sleeves (silver 1% → ±0.25 pp; REIT 4% → ±1 pp); no tradable band for locked sleeves (drift tracked for reporting; managed by sizing new commitments); trade to **target** only where a regulatory/IPS ceiling binds (unlisted %, associate %, credit floor), otherwise trade to the **inner band edge**; minimum ticket ₹1 Cr (20 bps); liquid-book turnover budget 15–25%/yr, reviewed annually.

Monte Carlo (10-yr weekly paths, 1,500 runs, house CMAs, 16-line Moderate SAA; one-way costs 1–13 bps by sleeve; LTCG 14.95% equity-like, slab 39% debt-like). Read only the turnover/cost/tax columns as reliable relative signals: the runs used independent random paths, not common random numbers, so the CAGR and TE columns carry simulation noise (the non-monotonic TE-vs-turnover pattern between E/F and G/H is very likely noise — corrected). Rebuild with common random numbers before board sign-off.

| Strategy | Turnover %/yr | Trades/yr | Cost bps | Tax bps | Cost + tax bps | ₹ Cr/yr | Avg drift (pp, summed) |
|---|---|---|---|---|---|---|---|
| A Monthly calendar, full to target | 26.0 | 96 | 2.8 | 49.7 | 52.5 | 2.63 | 4.3 |
| B Quarterly calendar | 15.1 | 39 | 1.7 | 36.1 | 37.8 | 1.89 | 5.1 |
| C Annual calendar | 7.7 | 12 | 0.9 | 23.5 | 24.4 | 1.22 | 7.3 |
| D Band-only, continuous, to target | 6.5 | 4 | 0.5 | 13.4 | 13.9 | 0.70 | 11.6 |
| E Hybrid monthly, breach → target | 6.1 | 4 | 0.5 | 13.1 | 13.6 | 0.68 | 11.9 |
| F Hybrid monthly, breach → inner edge | 4.0 | 4 | 0.3 | 10.1 | 10.4 | 0.52 | 12.4 |
| G Hybrid + event overlay, to target | 8.2 | 7 | 0.7 | 17.7 | 18.4 | 0.92 | 8.6 |
| **H Hybrid + event overlay, inner edge (adopted)** | **4.4** | **14** | **0.4** | **11.6** | **12.0** | **0.60** | **10.0** |

Decision: Strategy H, chosen on turnover, cost and tax (≈ 4–5× cheaper than monthly-to-target for a comparable drift profile), with the event overlay catching excursions a monthly check would miss for up to 30 days. Budget ≈ ₹0.5–0.7 Cr/yr (10–14 bps) for rebalancing cost + tax on the liquid book. Note that D (continuous band-only) is incompatible with NDPMS: "whenever" needs either standing discretion or constant ad-hoc consent.

Band table (Moderate): passive ±5; factor ±2 each; active mid ±1.5; active small ±1; direct ±3 (50 bps per name); international 2.5–7.5; short duration ±1; TMF ±3; G-sec ±2; AA credit ±1 (hard ceiling 2.4% = 10% of FI sleeve); arbitrage 1–4; gold ±1.5; silver ±0.25; REIT ±1; alternatives 0–7.5 Cat II / no band Cat III–SIF; total unlisted alert 18%, IPS cap 15%, legal 25%.

### 4.3 Tax-aware rules

| Rule | Mechanics | ₹500 Cr effect |
|---|---|---|
| Three demat accounts before the first trade | Core (strategic, rarely traded), Tactical (RPP trims/adds), Harvest (Q4 loss/gain harvesting). FIFO runs per account, so choosing the account approximates lot selection | retrofitting is impossible once a mixed-cost position exists in one account |
| Separate MF folios by purpose | same logic for folio-level FIFO | — |
| Cash-flow first | inflows, coupons, dividends, AIF distributions to the most under-target sleeve before any sell line is drafted | closes a large share of monthly drift at zero tax |
| STCG hurdle | no equity STCG realised to rebalance unless expected alpha of the switch > (23.92% − 14.95%) × unrealised gain ÷ proceeds; RPP flags any line that sells through LTCG lots into STCG | every 1% of AUM realised as STCG costs ≈ 24 bps of NAV vs ≈ 15 bps as LTCG |
| LTCG exemption harvesting | March: sell and rebuy the oldest small-gain lots up to ₹1.25 lakh gain per PAN (shared with the client's personal book) | small but zero-risk |
| Loss harvesting and netting | pull the client-level cumulative gain/loss ledger before 31 March; STCL against anything, LTCL only against LTCG; 8-year carry-forward; respect s.94(7)/(8) windows | avoids stranded losses |
| Fixed-income tax form | coupon is slab-taxed either way; TMF/debt funds defer slab tax to redemption (deferral value ≈ 39% × 6.9% × years held); direct G-sec pays slab on coupon annually but is the clean duration lever; listed-bond 12.5% LTCG applies to price gain only | choose funds for the laddered core, direct G-sec for duration |
| Cash tax form | arbitrage (equity-taxed) for cash > 1 month; overnight/liquid for < 1 month | ≈ 15–19 pts of tax on gains saved |
| Dividend policy | equity ETFs/index funds (dividends reinvested inside the fund) preferred over direct stocks for beta — direct-stock dividends are taxed at 35.88% | direct-stock sleeve carries ≈ 43 bps/yr dividend tax |
| Fee non-deductibility | model the PMS fee as non-deductible in R3/R4 (contested case law) | ≈ 0.30% × 14.95–39% ≈ 4–12 bps/yr sensitivity |

### 4.4 Transaction-cost model

Cost stack (one-way unless stated; STT/stamp/exchange verified; brokerage/impact negotiated/approx.):

| Instrument | STT | Stamp | Exchange + SEBI + GST | Brokerage | Spread / impact | Round trip ex-impact |
|---|---|---|---|---|---|---|
| Direct equity (delivery) | 0.1% each leg (20 bps RT) | 0.015% buy (1.5 bps) | ≈ 0.3 bps/leg + GST ≈ 1.5 bps RT | 3–5 bps/leg | by % ADV (5–15 bps large cap) | ≈ 27–31 bps + impact |
| ETF on screen | 0.001% sell | 0.005% units | as equity | 3 bps/leg | 3–15 bps spread | ≈ 10–14 bps + spread |
| ETF via AP / AMC-direct (≥ ₹25 Cr) | 0.001% sell | none | none | AP fee 2–3 bps | basket impact 2–4 bps | ≈ 5–7 bps |
| Index / active MF (direct plan) | 0.001% on redemption | 0.005% units | none | none | none (NAV) | ≈ 0–1 bp (+ exit load ≤ 1% if < 12 m) |
| Listed G-sec / SDL / corporate bond | none | ≈ 0.0001% approx. | minimal | dealer spread | 3–8 bps | ≈ 4–9 bps |
| REIT / InvIT | treat as 0.1% equity (verify) | as equity | as equity | as equity | 15–30 bps | ≈ 35–55 bps |
| AIF Cat II / III | none | none | — | — | — | commitment/lock-up drag instead |

Worked example A — ₹15 Cr trim of a large-cap direct name (sell): STT ₹15.0 lakh (10 bps) + exchange/SEBI ₹0.5 lakh (0.3 bps) + brokerage ₹6.0 lakh (4 bps) + GST ₹1.2 lakh (0.8 bps) = explicit ≈ ₹22.6 lakh (15 bps); impact 8–12 bps ≈ ₹12–18 lakh; all-in ≈ ₹35–41 lakh (23–27 bps). LTCG at a 40% embedded-gain ratio: 12.5% × 40% × ₹15 Cr = ₹75 lakh (50 bps) — tax is ≈ 2× the execution cost even at the lower LTCG rate.

Worked example B — ₹40 Cr switch between two Nifty-linked vehicles (rebuilt with self-check; corrected):

| Route | STT (sell 0.001%) | Brokerage / AP fee (2 legs) | Exchange + SEBI + GST | Spread / impact (2 legs) | Total ₹ | Total bps |
|---|---|---|---|---|---|---|
| On-screen | ₹0.04 lakh (0.1 bp) | 3 bps × 2 = ₹2.4 lakh (6 bps) | ≈ ₹0.4 lakh (1 bp) | 10 bps × 2 = ₹8.0 lakh (20 bps) | **≈ ₹10.8 lakh** | **≈ 27 bps** |
| AP / AMC-direct | ₹0.04 lakh (0.1 bp) | AP fee 3 bps × 2 = ₹2.4 lakh (6 bps) | none | basket impact 3 bps × 2 = ₹2.4 lakh (6 bps) | **≈ ₹4.8 lakh** | **≈ 12 bps** |
| Saving | | | | | **≈ ₹6.0 lakh** | **≈ 15 bps** |

Self-check: Σ component bps = total bps; ₹ total ÷ ₹40 Cr × 10,000 = bps total. If the switch crystallises gains at a 25% embedded-gain ratio, LTCG = 12.5% × 25% × ₹40 Cr = ₹1.25 Cr (312 bps) — twenty times the routing saving; evaluate every like-for-like switch post-tax first.

Annual owned-cost budget (Moderate; cash basis; corrected TCO in §7.9): trading impact + brokerage ≈ 8 bps; consent-latency shortfall ≤ 15 bps (measured, §6.3); realised tax ≈ 80 bps (dominated by Cat II interest, G-sec coupons and direct-stock dividends/LTCG); cash drag ≈ 10 bps steady state; weighted TER ≈ 40 bps; PM fee + GST ≈ 35 bps; opex ≈ 10 bps.

### 4.5 Execution policy

| Parameter | Rule |
|---|---|
| Participation | ≤ 10–15% of 20-day ADV per session per stock; tickets > 2% of ADV split VWAP/TWAP over 2–5 sessions inside T0–T+7; randomised intra-window timing to avoid a predictable Thursday footprint |
| Order type | limit orders referenced to arrival ± cost-model band; no market orders in illiquid names |
| Slippage budget | ≤ 15 bps vs arrival price per RPP; breach → RM/IC escalation |
| Block deals | any single-line direct-equity ticket ≥ ₹25 Cr via the 08:45–09:00 or 14:05–14:20 window (±3%, compulsory delivery); bulk-deal disclosure check for any line near 0.5% of listed shares (approx. threshold — verify with the exchange before the first such ticket) |
| ETF routing | ≥ ₹25 Cr AMC-direct; ≥ ₹5 Cr AP creation; < ₹5 Cr on screen at |premium| ≤ 15 bps; empanel at least one AP before go-live (Phase 0–30 deliverable) |
| MF timing | orders before 13:30 (liquid/overnight) / 15:00 (others); NAV on realisation of funds — confirm each AMC/RTA clock before the order calendar is built |
| Bonds | G-sec via NDS-OM (custodian/PD) or exchange segment; corporate bonds ≥ 10% via RFQ (regulatory floor); rating floor AA; single issuer ≤ 3% of FI sleeve |
| Cash ladder | overnight (< 1 week), liquid (1 week–1 month), arbitrage (> 1 month); overnight buffer sized to the largest weekly net redemption in trailing 12 months |
| Broker | Angel One at actuals, rate card benchmarked quarterly; ≥ 10% of listed-equity flow through a second, non-group broker in year 1 for TCA (budgeted, §8.11) |
| Group-instrument trades (new) | Any order in an Angel One group security or scheme (Angel One Ltd shares; any Angel One AMC ETF/index fund/SIF or Angel One AIF, where such products exist — list maintained by Compliance, approx.) is tagged `group_instrument=true` in the OMS. Routing: listed group securities 100% via the second, non-group broker (Angel One never executes its own group's listed paper for this client); group MF/ETF units via NAV/AP route (no broker). Per-trade TCA vs arrival and VWAP; separate quarterly table; test slippage ≤ non-group median + 3 bps; disclosure in the periodic report's associate-exposure section alongside the Annexure A consent and the IC best-selection minute |
| Derivatives | only lines approved in the RPP or the Hedge Protocol annex; exposure ≤ portfolio funds; lot size 65 (Nifty, since Jan-2026); options STT 0.15% on premium |
| Compliance engine | every order must carry a valid rpp_id or standing_instruction_id; pre-trade checks for unlisted headroom (15% IPS / 25% legal), associate headroom (10% / 15-25-30%), derivative notional, no short, no leverage, direct-plan flag, demat-account routing, credit floor; every override logged with reason and second sign-off |

---

## 5. Risk & tail-risk framework

Under NDPMS risk control must be pre-authorised: limits, hedge protocols and de-risk triggers exist inside the RPP/standing-instruction machinery because a risk manager cannot cut equity at 14:00 on a crash day. Latency is a risk factor and is measured (§6.3). We still own the P&L.

### 5.1 Limit framework (two-tier: house/IPS target vs legal ceiling; passive breach = cure, active breach = blocked pre-trade)

| # | Limit | House / IPS (₹500 Cr) | Legal ceiling | Action |
|---|---|---|---|---|
| 1 | Sleeve bands | per §4.2 | n/a | passive: RPP restore; active: blocked |
| 2 | Single direct stock | 3% of AUM (₹15 Cr) target cap; 5% hard (₹25 Cr) | none for PMS | 3–5%: no buys, IC review; > 5%: trim in next RPP |
| 3 | Sector | ≤ 25% of equity sleeve (≈ ₹60–80 Cr) | n/a | block new sector buys; trim within 10 trading days if price-driven |
| 4 | Single AIF / Cat II / Cat III fund | ≤ 5% of AUM (₹25 Cr); ≤ 2 funds per manager | unlisted 25% (100% LVAI) | commitments blocked at cap; NAV-driven excess tracked, no forced exit |
| 5 | Single AMC / manager group (look-through across MF + AIF + SIF + PMS) | ≤ 15% of AUM (₹75 Cr) | n/a | no new subscriptions; requires an aggregation system before go-live |
| 6 | Third-party PMS (outside AUM) | ≤ 3% look-through (₹15 Cr), one manager | n/a | annual review |
| 7 | Credit floor | AAA/AA+ ≥ 90% of FI sleeve; AA is the minimum issuer rating (Moderate AA line 2% = 8.3% of FI sleeve — passes; corrected) | no below-investment-grade listed paper (NDPMS); ≤ 10% of AUM unlisted unrated (non-associate) | downgrade below AA− → exit proposal in 5 trading days |
| 8 | Duration | blended modified duration 2.5–4.5 yrs (Moderate); ≤ 6.5 yrs on the 10-yr line | n/a | restore in next RPP; no daily duration trading |
| 9 | Illiquid/unlisted aggregate | 15% of AUM (₹75 Cr); alert 18% | 25% (₹125 Cr); 100% LVAI | 15–25%: IC sign-off for new commitments; > 25% active breach = hard block, no cure window assumed (corrected — the "90-day cure" figure is dropped) |
| 10 | Derivative notional (hedge only) | ≤ 25% of AUM (₹125 Cr); premium ≤ 1% of AUM p.a. (₹5 Cr) | exposure ≤ portfolio funds; no leverage | every hedge an RPP line or protocol-annex roll; premium > 0.75% run-rate → IC. Pipeline (not law): 1.25× exposure, 50% unhedged shorts — watch-list only |
| 11 | Liquidity | ≥ 80% liquidable in ≤ 5 days; ≥ 95% in ≤ 10 days (20% ADV) | n/a | pause new illiquid commitments |
| 12 | Unhedged FX | ≤ 15% of AUM (₹75 Cr) | none (access capped by USD 7 bn gate) | no international top-ups; FX hedge discussion (currency derivatives inside PMS: restricted — verify) |
| 13 | Associate / group securities | ≤ 10% of AUM (₹50 Cr); alert at 80% of cap | 15% / 25% / 30% | Annexure A consent; real-time alert; IC best-selection minute |
| 14 | Absolute drawdown | −18% from peak NAV (Moderate); −25% (Aggressive) | n/a | escalation trigger → mini-RPP with de-risk options; not a hard stop (client decision) |

### 5.2 Daily metrics

| Metric | Formula / method | Model baseline (Moderate / Aggressive) | Band |
|---|---|---|---|
| Parametric VaR | σ²ₚ = wᵀΣw; VaR = z × σₚ × √(h/252) × NAV; equity cluster ρ ≈ 0.75, bond cluster 0.6, gold-silver 0.75, cross-asset β-implied | 1-day 95% 1.00% (₹5.0 Cr) / 1.30% (₹6.5 Cr); 99% 1.42% / 1.84%; 1-month 95% 4.59% / 5.95% | amber if 1-month 95% VaR > 6% / 7.5% |
| Historical VaR / CVaR | re-price current weights over ~1,500 daily sleeve-proxy returns (≈ 6 years); CVaR = mean beyond the percentile | ES 97.5% 1-day 1.42% / 1.85% | runs alongside parametric (fat left tail) |
| EWMA vol | σ²ₜ = 0.94 σ²ₜ₋₁ + 0.06 r²ₜ₋₁ | a −5.9% day lifts daily vol 0.76% → 1.62% (≈ 12% → 26% annualised) | > 1.5× 60-day realised = amber |
| Beta | wᵀΣe₁ / σ²_Nifty | 0.55 / 0.72 | ± 0.10 of SAA beta |
| Tracking error vs T2 | √[(wₚ − w_b)ᵀΣ(wₚ − w_b)] | 1.5–2.0% / 2.0–2.5% | green 1.5–3.5% (Mod), 2.0–4.5% (Agg); amber to 4.5% / 6.0%; red > 4.5% / > 6.0% or < 1.0% / < 1.5% (closet indexing). Bands reset to what the SAA can deliver (corrected) |
| Drawdown | Vₜ / max V − 1 on post-fee NAV | — | green ≤ 1.10× benchmark MDD; amber to 1.25×; red > 1.25× or −18% absolute |
| Consent-latency dispersion | position × daily vol × √days (1-σ) | ₹50 Cr de-risk: ₹0.60 / ₹0.85 / ₹1.34 / ₹1.90 Cr at 1/2/5/10 days (normal 1.2% vol); ₹1.25 / ₹1.77 / ₹2.80 / ₹3.95 Cr stressed (2.5%) | any ad-hoc item > 5 days = red |
| Factor exposures | holdings-based x_k = Σ(wₚ − w_b) z_k on scorecard z-scores + size/beta; 36-month returns regression cross-check on Nifty factor spreads | — | > 60% of 12-month active return from size/momentum → reclassify as TAA |
| Correlation regime | rolling 60-day mean pairwise correlation across 8 sleeves | ≈ 0.3–0.4 normal | > 0.60 = red; widen VaR by a stress multiplier |
| Look-through | monthly decomposition of MF/AIF/SIF wrappers; Cat III shown at **gross notional** (leverage up to 2× NAV) feeding limits #5 and #9 (corrected — new) | — | AIF disclosure > 45 days old = "stale" flag |
| Model validation (new) | Kupiec/traffic-light back-test of VaR once 250 live days exist; common-random-number rebuild of the rebalancing Monte Carlo; second-reviewer sign-off on any engine change; **capture-ratio validation**: realised NAV drawdown ÷ Nifty drawdown logged for every Nifty drawdown ≥ 5% against the model capture on live weights (±10 pp tolerance; re-estimate betas/correlations after 3 episodes or any miss) | — | per episode; annual |

Taxonomy (fixed in v1.1): the **14 hard limits** of §5.1 are the `risk_limits` array; the monitored bands in this table (1-day/1-month VaR, EWMA, TE, drawdown-vs-benchmark, correlation regime, consent latency, capture validation) are the `risk_metric_bands` array; no-leverage / no-short / direct-plan / consent-FK / group-instrument routing are `pre_trade_hard_blocks`. A band breach is a review trigger; a limit breach is a blocked trade or a cure.

### 5.3 Historical stress library (₹ Cr P&L, Moderate / Aggressive; asset-class moves approx. except [V])

| Episode | Window | Nifty 50 | Midcap 150 | Smallcap 250 | 10Y yield Δ | Gold INR | USD/INR | VIX peak | Mod ₹ Cr (%) | Agg ₹ Cr (%) | Nifty recovery |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GFC | Jan-08–Mar-09 | −60% [V] | −73% | −78% (CY2008 −73% [V]) | 400 bp swing | +25–40% | +32% | ≈ 85 | −160 (−32.0%) | −215 (−43.0%) | ≈ 34 months (price), sources disagree 3–5 yrs |
| 2011 EU / RBI tightening | Nov-10–Dec-11 | −28% | −38% | −47% | +50 bp | +35% | +20% | ≈ 37 | −72 (−14.4%) | −99 (−19.8%) | ≈ 37 months |
| Taper tantrum | May–Aug-13 | −15% | −24% | −32% [V] | +200 bp | +27% | +25% | ≈ 32 | −48 (−9.6%) | −56 (−11.2%) | ≈ 5 months |
| Demonetisation | Nov–Dec-16 | −7.5% | −11% | −13% | −60 bp | −8% | +2.7% | ≈ 23 | −20 (−4.0%) | −28 (−5.6%) | ≈ 2 months |
| IL&FS | Sep–Oct-18 | −15% | −24% | −36% (CY) [V] | +30 bp | +7% | +6% | ≈ 21 | −47 (−9.4%) | −61 (−12.2%) | ≈ 7 months |
| COVID | Feb–Mar-20 | −38.4% [V] | −42% | −44% [V] | −40 to −80 bp | ≈ +2% (−8% mid-Mar) | +8% | 86.64 [V] | −114 (−22.8%) | −144 (−28.8%) | 231 days [V] |
| 2022 rate shock | Oct-21–Jun-22 | −17% | −21% | −30% | +125 bp | +7% | +4% | ≈ 34 | −50 (−10.0%) | −68 (−13.6%) | ≈ 13.5 months |
| Election day | 4-Jun-24 | −5.9% [V] | −8% | −8% | +9 bp | flat | +0.5% | 26.7 close | −17 (−3.4%) | −21 (−4.2%) | 3 sessions |
| Tariff shock | Sep-24–Apr-25 | −16% | −22% | −26% | −30 bp | +23% | +5% | 22.8 | −33 (−6.6%) | −53 (−10.6%) | ≈ 14 months |
| 2026 oil / rupee | Jan-26–date | ≈ −10% (8% below peak 12-Aug [V]) | −14% [V] then new peak | ≈ −18% | +50 bp | +14.6% YTD | +6.8% YTD [V] | 27.2 (now 12.4 [V]) | −30 (−6.0%) | −40 (−8.0%) | in progress |

Capture ratios stated honestly (corrected): Moderate captures 39–63% of the Nifty move across the ten episodes (median 54%); Aggressive 62–81% (median 71%). The high end comes from credit events and single-day shocks where bonds and gold do not help; plan for the high end.

### 5.4 Hypothetical scenarios

| Scenario | Assumptions | Moderate | Aggressive | Liquidity need |
|---|---|---|---|---|
| Equity −25% (mid −32%, small −38%, intl −15%, VIX 40) | broad de-rating | −₹72.6 Cr (−14.5%) | −₹96.0 Cr (−19.2%) | none forced; a 10% de-risk needs ₹50 Cr liquid inside the SLA |
| Rates +200 bp parallel | REIT −15%, equity −12% | −₹44.9 Cr (−9.0%) | −₹48.3 Cr (−9.7%) | FI MTM only; hold-to-maturity option |
| INR −10% (FPI exodus) | Nifty −8%, intl +9%, gold +9% | −₹21.0 Cr (−4.2%) | −₹26.1 Cr (−5.2%) | TCS cash-lock if LRS topped up mid-shock |
| Oil +50% | yields +60 bp, Nifty −10% | −₹28.5 Cr (−5.7%) | −₹35.2 Cr (−7.0%) | gold is the offset |
| Credit event, one Cat II fund −40% | ₹12.5 Cr fund (half the single-fund cap); AA book −8% | −₹6.6 Cr (−1.3%) | −₹4.0 Cr (−0.8%) | zero (locked); pure MTM; IC same day, client within 24 h |
| Credit event at full cap (new) | ₹25 Cr fund −40% | −₹11.6 Cr (−2.3%) | −₹9.0 Cr (−1.8%) | as above |
| FPI outflow ₹1 lakh Cr/month | Nifty −12%, mid −18%, INR −4%, yields +40 bp | −₹35.1 Cr (−7.0%) | −₹44.9 Cr (−9.0%) | ADV halves: direct-book liquidation time doubles |
| Client redemption ₹100 Cr (new) | 20% of AUM in 5 days | alternatives 9% → 11%; TE +0.3% | 12% → 15% | met from arbitrage + passive + TMF; consent cycle to reset SAA |

Liquidity arithmetic: days = position ÷ (0.20 × ADV). ₹1.8 Cr vs ₹20 Cr ADV = 0.45 days; ADV halved = 0.9 days; a ₹3 Cr small-cap line vs ₹5 Cr stressed ADV = 3 days. The binding constraint in a real stress is consent latency, not market liquidity.

### 5.5 Hedge menu with costs (₹300 Cr equity-like sleeve; Black-Scholes, S = 23,400, r 6.2%, q 1.2%, T = 0.25; lot 65; India VIX 12.4 vs 52-week range 8.7–28.9 — near the cheap end)

| Instrument (3M) | IV assumed | Cost / qtr | ₹ Cr/yr on ₹300 Cr | bps p.a. of sleeve | Regime |
|---|---|---|---|---|---|
| 5% OTM put (K 95%) | 14.5% | 0.73% | 8.8 | ≈ 292 | sharp crashes |
| 5% OTM put, stressed roll | 20–30% | 1.5–3.2% | 18–39 | 612–1,284 | never initiate after a spike |
| 95/85 put spread (default) | 14.5 / 17.5% | 0.66% | 7.9 | ≈ 265 | most drawdowns ≤ 15% |
| 95P/105C collar | 14.5 / 12% | net credit | ≈ +3.5 received | ≈ −116 | de-risk after a rally without selling |
| 10% OTM put | 16% | 0.23% | 2.8 | ≈ 94 | tail-only cover |
| Gold overweight +2–3 pp | — | opportunity cost only (E[R] 8% vs 11%) | ≈ 0.3–0.45 | — | INR/geopolitical shocks (no derivatives, normal RPP line) |
| Long-vol / market-neutral Cat III or SIF 1–2% | — | fee + fund-level tax | — | — | grinding regimes where puts lose |
| 2% arbitrage buffer | — | ≈ 4–5 pp carry deficit on ₹10 Cr ≈ ₹0.45 Cr | — | — | funds day 1 of any consent gap |

Payoff of a rolling 5% OTM put on the full sleeve across the library: GFC +₹112 Cr net, COVID +₹102 Cr, IL&FS +₹28 Cr, taper +₹31 Cr, 2022 +₹1.5 Cr, election day +₹0.5 Cr, tariff shock −₹1.8 Cr, West Asia −₹10.7 Cr (no payoff, pure premium). Decision: standing partial cover — 95/85 put spreads on 25–40% of the equity sleeve (₹75–120 Cr notional, ≈ 500–800 lots), premium budget ≤ 1% of AUM p.a. (₹5 Cr), initiated via RPP when India VIX < 15, auto-rolled via standing instruction #5, sized up only through a fresh RPP. Full-notional cover (≈ ₹14.5 Cr/yr on ₹500 Cr) is an AVOID. Actual execution IV must be read off the live options chain; the 14.5% is a working assumption. USD/INR hedge for the international sleeve — costed, not just "unavailable": the instrument would be exchange-traded USD/INR futures/options (currency-derivative use inside PMS AUM for hedging: restricted — verify with custodian/exchange). Cost driver is the forward premium: 12M USD/INR ≈ 2.82% annualised (Capera curve, 10-Jul-2026 print — approx. for today; source live from CCIL/FBIL) → hedging ₹25 Cr costs ≈ ₹0.70 Cr/yr ≈ **14 bps of AUM p.a.** plus roll/margin operations, and removes ≈ ₹1.4 Cr of 1-σ annual dispersion (USD/INR vol ≈ 5.5%). Because equity–USD/INR correlation is ≈ −0.35 (Table A3), the unhedged sleeve is a natural FPI-outflow hedge and hedging it slightly *raises* portfolio vol while forfeiting the ≈ 3.5% p.a. INR-depreciation carry embedded in the CMA. Decision: leave unhedged; the sleeve size (5%, band 2.5–7.5%) is the hedge; the annual review states the ≈ 14 bps p.a. saved by that choice; revisit if household look-through USD exposure exceeds 10% or SEBI notifies specified foreign securities.

### 5.6 Early-warning board (12 indicators; single Red = same-day IC e-mail; two Ambers = IC flag)

| Indicator | Current (11–12-Sep-2026) | Green | Amber | Red | Action on Red |
|---|---|---|---|---|---|
| India VIX | 12.4 [V] | < 15 | 15–22 | > 22 | IC hedge review; propose puts in next RPP |
| Nifty breadth (A/D, 20-day) | — | > 1.2 | 0.8–1.2 | < 0.8 for 5 sessions | trend-filter check |
| FPI net equity flow (monthly, NSDL) | CY2026 net sell ≈ ₹1.9–2.5 lakh Cr approx. | net buy or < ₹10k Cr out | ₹10–40k Cr out | > ₹40k Cr out | de-risk RPP drafted (not executed) |
| 10Y AAA – G-sec spread | ≈ 221 bp (15-Aug) | < 180 | 180–260 | > 260 | credit-floor review; no AA adds |
| AA − AAA spread (3–5Y corporate) | live daily series not yet stored; 2026 range prints put AAA at 50–140 bp and AA at 100–260 bp over G-sec (approx.) → AA − AAA ≈ 50–120 bp | < 100 bp (provisional) | 100–150 bp (provisional) | > 150 bp (provisional); replaced by 60-day mean + 1σ / + 2σ once 60 readings exist (roadmap day 45) | trim AA toward AAA; no AA adds |
| 10Y G-sec yield | ≈ 7.0% [V], 10-month high | ± 25 bp of 3-month avg | 25–75 bp move in a month | > 75 bp | duration review |
| USD/INR | 95.79 [V] (corrected from ₹88) | < 1% monthly move | 1–3% | > 3% | intl-sleeve and gold check |
| Real 10Y rate (yield − CPI) | ≈ 2.0% (CPI forecast 5.0%) | > 1.5% | 0.5–1.5% | < 0.5% | inflation-hedge assets to IC |
| US VIX | — | < 18 | 18–28 | > 28 | imported-vol warning |
| Brent | ≈ $110 [V] → **Red today** | < $75 | $75–95 | > $95 | re-run oil +50% scenario live |
| Nifty 50 forward P/E percentile (10-yr) | ≈ 17–18× fwd approx.; trailing 19.8–20.2 vs median 23.3 → low percentile | < 60th | 60–85th | > 85th | no large-cap adds; tilt to Value/Quality |
| Nifty vs 200-DMA | — | above, rising | ± 3% | below, falling | dynamic de-risk mini-RPP |
| Rolling 60-day sleeve correlation | — | < 0.40 | 0.40–0.60 | > 0.60 | widen VaR multiplier |

Note: on today's readings Brent is Red and the 10Y is at a 10-month high while VIX is 12.4 — options are cheap relative to the macro stress, which is exactly the set-up in which the partial put-spread programme should be initiated in the first RPP.

### 5.7 Tail-event playbook (NDPMS)

Decision tree: (1) covered by a signed standing instruction → execute same day, log; (2) an already-consented RPP line inside its window → execute; (3) anything new (fresh hedge, off-cycle de-risk, new name, resizing) → same-day mini-RPP (1–3 lines, ₹ impact from §5.3/5.4, cost estimate, lapse clause) pushed through portal, OTP e-mail and recorded call.

| Horizon | Owner | Action |
|---|---|---|
| Hour 1 | Risk → CIO/PM | confirm trigger is real (not a data error); size P&L; standing instruction or mini-RPP? |
| Hour 1 | CIO → Compliance | pre-clear the mini-RPP against all 14 limits |
| Hour 2 | PM → client / RM | phone call; written mini-RPP follows; timestamps logged (this is the audit trail and the latency-cost evidence) |
| Day 1–2 | PM → IC | formal note: trigger, proposal, client decision, execution, residual risk |
| Week 1 | Compliance | SEBI-reportable event check; no active-breach crossed |
| Week 1 | Performance | tag the episode in the TWRR engine (as-recommended vs as-instructed gap) |

Client note template: "[Date] — Trigger: [indicator]. Impact if unhedged: ≈ ₹[Z] Cr ([%] NAV) per [scenario]. Recommendation: [trade, ₹, instrument]. Estimated cost/tax: ₹[A] Cr. Under our non-discretionary mandate this requires your consent — APPROVE / MODIFY / DECLINE by [time]. Absent a response the recommendation lapses and positioning continues unchanged."

Client unreachable > 72 hours: execute only standing instructions; IC documents "unable to act — no client instruction" as the compliant outcome; any broader "defensive, reversible-only" action is refused until counsel/Informal Guidance defines the boundary (unclear_verify).

### 5.8 Tail-risk dashboard spec (fifth tab of the existing house suite; palette navy #16233B, indigo #1B27A3, green #1E9E6A, coral #E0402F, amber #F2A93C)

| Panel | Metrics | Source | Refresh | Alert | Colour rule |
|---|---|---|---|---|---|
| Risk strip | 1-day/1-month VaR & CVaR (95/99), EWMA vol, beta, TE vs T2 | risk engine on daily position + NAV | daily 07:30 | TE outside band | green/amber/coral chips on navy |
| Drawdown & recovery | NAV, peak, DD, DD ÷ benchmark DD, days since peak | TWRR engine (shared) | daily | > 1.25× or −18% | coral fill below −18% |
| Limit grid | 14 limits, live utilisation % | position + look-through | daily | > 90% amber, breach coral | |
| Stress panel | 10 historical + 8 hypothetical re-priced on live weights | nightly risk batch | daily | any scenario > −15% NAV | coral bars |
| Hedge book | open derivatives, notional %, premium YTD vs 1% budget, payoff to date | OMS/custodian ledger | daily | run-rate > 0.75% amber, 1.0% coral | |
| Early-warning board | 12 indicators, 30-day sparklines, RAG chips | market feeds (NSE, NSDL, RBI, CCIL) | daily (VIX intraday optional) | per §5.6 | |
| Look-through concentration | name / sector / AMC / rating across wrappers; Cat III gross notional | factsheets, AIF disclosures | monthly (AIF), daily (direct + MF) | any limit breach look-through | grey "stale" flag > 45 days |
| Consent-latency log | each ad-hoc RPP: trigger, response, execution time, 1-σ dispersion, realised Perold cost | RPP ledger | event-driven, weekly roll-up | > 5 trading days | coral row |
| Liquidity ladder | % liquidable in 1/5/10/30/90 days, normal vs ADV −50% | position × ADV | daily | < 80% in 5 days | coral |

The dashboard is a monitor, not a trading system: it displays and logs; it never originates an order. Red alerts are pushed (e-mail/Slack) to CIO, PM, Risk and Compliance, not only displayed.

---

## 6. Performance, attribution & accountability

### 6.1 Return series and methods

One daily-valued, transaction-level TWRR engine produces every number in every report (SEBI/APMI filing, client pack, IC scorecard). No spreadsheet forks.

| Series | Definition | Costs deducted | Use |
|---|---|---|---|
| R0 paper | IC-approved model executed at decision-date closes | none | consent-latency and implementation attribution only; never shown as performance |
| R1 gross | actual portfolio at fill prices; MF/ETF TER embedded in NAV | impact/spread (in fills), embedded TER | attribution vs T2; IC scorecard |
| R2 net | R1 − PM fee − GST − opex (custody, FA, audit, RTA; ≤ 0.50% cap) − booked brokerage/STT/stamp/exchange | all booked fees and expenses | SEBI/APMI reporting; client headline; alpha accountability |
| R3 post-tax realised | R2 − taxes paid from the portfolio (realised STCG/LTCG, TDS on dividends/interest at slab); PMS fee treated as non-deductible | fees + cash taxes | client "money in pocket" |
| R4 post-tax liquidation | R3 with a deferred-tax liability (DTL) on unrealised gains at lot-specific rates (capital-gains surcharge cap 15% on equity lots; full slab surcharge on debt lots — corrected) | fees + cash tax + DTL | cross-sleeve comparison; exit planning |
| X1 client XIRR | IRR of all client cash flows and terminal value, net of fees | — | mandatory per investor with IA min/median/max |

Daily TWRR: rₜ = (Vₜ − Vₜ₋₁ − CFₜ) / (Vₜ₋₁ + w·CFₜ), w = 1 for flows received before 09:15 IST, 0 after 15:30, intraday defaults to start-of-day. Worked: V₀ ₹500.00 Cr, CF +₹25.00 Cr, V₁ ₹527.10 Cr → 0.4000% (start-of-day) vs 0.4200% (end-of-day); the convention is fixed in policy. Chain-link Π(1 + rₜ) − 1; annualise only for N ≥ 365 days; 1M/3M/6M reported absolute. Contributions cᵢ,ₜ = wᵢ,ₜ₋₁ rᵢ,ₜ, Carino-linked. Any external flow ≥ 2% of AUM (₹10 Cr) forces revaluation; the deployment period is reported both fully-invested and as-deployed with a cash-drag line. IA aggregation across family accounts is asset-weighted on the pooled balance sheet, never an average of account TWRRs; per-account custody stays segregated (no pooling of assets) — only the return is aggregated.

XIRR vs TWRR under staggered deployment: ₹250 Cr day 0, ₹250 Cr month 6, +8.0% H1, −3.0% H2 → TWRR 4.76%, XIRR 1.17%, terminal ₹504.40 Cr. Both are reported with a one-line reconciliation; a TWRR–XIRR gap > 2 pp after the deployment window ends triggers a client conversation (new threshold). If this client is the only investor in the IA, the min/median/max disclosure degenerates to one number — say so explicitly.

Valuation policy: listed at NSE close (T+0); MFs at AMFI NAV (purchases at cost until allotment at realisation-day NAV); international FoFs at T+1 NAV flagged; debt at APMI-empanelled agency prices with daily accrual; Cat III at fund NAV rolled forward (> 100 days stale flag, > 180 days 5% haircut in R4); Cat I/II independent valuation every 6 months (> 200 days stale flag; 10% haircut on unrealised marks in R4); uncalled commitments stay in the cash sleeve; third-party PMS on custodian holdings (> 0.10% NAV gap vs manager statement escalates); corporate actions on ex-date; unmatched CA after T+3 → exception queue.

### 6.2 Benchmark

T1 APMI Multi-Asset (regulatory), T2 Policy Composite (§2.5, contractual, monthly reset, versioned sub-index levels never spliced without a dated version ID), T3 Allocate 80/20 and Nifty Multi Asset 50:20:20:10 (reference). Alpha is judged on **R2 vs T2**; tax efficiency on (R2 − R3) and (R2 − R4) vs budget; implementation on (R0 − R1). Expected relationship stated in the agreement: T2 trails 80/20 by 1–2 pp in strong equity years and leads in drawdowns.

### 6.3 Attribution: Brinson-Fachler + look-through + consent slippage

Per sleeve i, month t: allocation Aᵢ = (wᵢᴾ − wᵢᴮ)(Rᵢᴮ − Rᴮ); selection Sᵢ = wᵢᴮ(Rᵢᴾ − Rᵢᴮ); interaction Iᵢ = (wᵢᴾ − wᵢᴮ)(Rᵢᴾ − Rᵢᴮ); Σ = Rᴾ − Rᴮ exactly. Months are Carino-linked: kₜ = [ln(1 + Rᴾₜ) − ln(1 + Rᴮₜ)] / (Rᴾₜ − Rᴮₜ); K likewise for the period; linked effect = Σₜ (kₜ / K) × effectₜ. Menchero acceptable for IC use; one method, frozen.

Worked full year (illustrative returns, R1 basis; verified cell-by-cell by two independent critiques):

| Sleeve | w_B | w_P | R_B % | R_P % | Allocation % | Selection % | Interaction % | Total % | ₹ Cr |
|---|---|---|---|---|---|---|---|---|---|
| Domestic equity | 55 | 57 | 10.0 | 11.6 | +0.006 | +0.880 | +0.032 | +0.918 | +4.59 |
| International | 7 | 6 | 14.0 | 13.2 | −0.043 | −0.056 | +0.008 | −0.091 | −0.45 |
| Fixed income | 22 | 20 | 7.5 | 7.9 | +0.044 | +0.088 | −0.008 | +0.124 | +0.62 |
| AIF Cat II | 4 | 3 | 10.5 | 11.0 | −0.008 | +0.020 | −0.005 | +0.007 | +0.04 |
| REIT/InvIT | 4 | 4 | 9.0 | 9.0 | 0 | 0 | 0 | 0 | 0 |
| Gold/silver | 5 | 5 | 12.0 | 11.8 | 0 | −0.010 | 0 | −0.010 | −0.05 |
| Cash/arbitrage | 3 | 5 | 6.5 | 6.4 | −0.064 | −0.003 | −0.002 | −0.069 | −0.35 |
| **Total** | 100 | 100 | **9.705** | **10.584** | **−0.065** | **+0.919** | **+0.025** | **+0.879** | **+4.40** |

(The worked year uses the performance design's illustrative 7-sleeve weights; the live engine runs on the canonical T2 weights of §2.5.) Look-through split of the +0.880% domestic selection: direct equity vs Nifty 500 TRI +0.46; active MFs vs category TRI then vs Nifty 500 +0.26; third-party PMS (look-through, outside AUM, reported as pass-through) +0.12; Cat III lagged +0.06; ETF/index tracking difference −0.02. Factor attribution of the direct sleeve uses scorecard z-scores against Nifty factor-spread indices (size = Midsmallcap 400 − Nifty 100; value = Nifty 500 Value 50 − Nifty 500; momentum = Nifty 500 Momentum 50 − Nifty 500; quality = Nifty 200 Quality 30 − Nifty 200; low-vol = Nifty 100 LV30 − Nifty 100) with a 36-month returns regression cross-check; > 60% of 12-month active return explained by size/momentum → reclassified as TAA. Currency: (1 + R_INR) = (1 + R_local)(1 + R_FX); a 3% INR move on a 7% sleeve is +0.21% of portfolio return that is not skill.

Consent-slippage (Perold) per order: consent-latency cost = s(P_C − P_D)Q; dealing delay = s(P_A − P_C)Q; execution = s(P_E − P_A)Q + explicit charges; opportunity cost of unexecuted quantity = s(P_H − P_D)(Q_rec − Q_exe). Worked: ₹20 Cr from a Nifty 50 ETF to a mid-cap index fund; decision D; consent D+4 (mid-cap +1.5%, Nifty +0.5%) → latency cost ₹0.20 Cr; execution D+5 (+0.3% vs +0.1%) → ₹0.04 Cr; total ₹0.24 Cr = 4.8 bps of AUM = 120 bps of traded value. Annualised at 12 cycles × 4% turnover × 30 bps adverse drift ≈ ₹0.72 Cr ≈ 14 bps — the 15 bps budget line. KPIs: median decision→execution ≤ 3 business days, 90th percentile ≤ 6, shortfall ≤ 25 bps p.a.

Full waterfall (worked year): T2 9.705 − 0.065 TAA + 0.440 manager selection + 0.460 security selection + 0.019 other selection (nets the −0.02 tracking difference) + 0.025 interaction = 10.584% (R1; R0 was 10.784% before −0.20% implementation shortfall, a memo item, not subtracted twice) − 0.534 fees & expenses (fee 30 + GST 5.4 + opex 10 + booked trading 8 bps) = 10.05% (R2) − 0.45 cash taxes = 9.60% (R3). Net alpha on R2 = +35 bps (₹1.7 Cr) — with the fee fixed at 0.30% rather than the 0.50% used in one design (corrected).

Waterfall arithmetic as coded in the data pack (`return_decomposition`, `summed_in_waterfall` flags): −6.5 + 44.0 + 46.0 − 2.0 + 3.9 + 2.5 = **+87.9 bps** (R1 − T2); − 35.4 − 10.0 − 8.0 = **+34.5 bps** (R2 − T2, the accountability metric); − 45.0 = **−10.5 bps** (R3 − T2). The −20 bps implementation shortfall is R0 − R1 and is already inside the R1-basis effects; it is a memo row and is never subtracted again (the v1.0 data pack summed it a second time to −30.5 bps — corrected).

Later-phase measurement specs (COULD → specified so they can be built when scheduled):

| Method | Formula | Worked example (₹ Cr) | Use / cadence |
|---|---|---|---|
| Kaplan-Schoar PME for AIF sleeves | PME = [Σ Dₜ·(I_T/Iₜ) + NAV_T] ÷ Σ Cₜ·(I_T/Iₜ), I = Nifty 500 TRI (PE) or Nifty Composite Debt + 300 bps (private credit); Direct Alpha ≈ ln(PME)/T (approx.) | ₹25 Cr commitment; calls ₹10 (index 100), ₹10 (110), ₹5 (105); distribution ₹4 (120); NAV ₹26 at index 130 → PV calls 13.00 + 11.82 + 6.19 = 31.01; PV distributions 4.33 + 26.00 = 30.33; **PME 0.978**, Direct Alpha ≈ −0.55% p.a.; fund IRR ≈ 6.1% vs index 6.8% CAGR — under-performed the public equivalent despite a positive IRR | quarterly with each AIF statement; reported next to IRR/TVPI/DPI; PME < 1.0 for 8 consecutive quarters → no re-up with that manager |
| Campisi fixed-income attribution | R_FI = income (carry) + treasury effect (−D_mod × Δy_G-sec) + spread effect (−D_spread × Δspread) + selection residual; same decomposition on the T2 debt component | ₹120 Cr sleeve, D 3.5: carry 7.1% (+₹8.52 Cr); G-sec +40 bp → −1.40% (−₹1.68 Cr); spread −10 bp → +0.35% (+₹0.42 Cr); realised 6.30% → residual +0.25% (+₹0.30 Cr); total +₹7.56 Cr | quarterly once the bond module reports duration by line; separates the duration call (TAA) from issuer selection |
| GIPS-style composite (no compliance claim) | one single-client "NDPMS Multi-Asset Moderate" composite = the IA; monthly valuation minimum (we value daily), geometric linking, no annualisation < 1 yr, gross and net series, fee schedule and composite description disclosed; presentation-only — GIPS treats client-restricted non-discretionary portfolios as excludable, so this is a **format**, not a claim | — | annual review pack; feeds the second-mandate marketing once ≥ 12 months exist |

### 6.4 Risk-adjusted targets (net of fees, vs T2; rolling 36M; R_f = 91-day T-bill ≈ 5.3% approx., to be sourced daily from RBI/CCIL)

Reset of the accountability ladder (corrected): the CMA-implied gross alpha of the constructed book is ≈ +55 bps (Moderate) / +45 bps (Aggressive) against ≈ 53 bps of R1→R2 load, so ex-ante net alpha is ≈ 0. A +100 bps net target would require ≥ 155 bps of gross active return — achievable only by lifting selection weight (direct 8 → 12%, active 10 → 14%) with TE rising toward 3%. The IC must choose (a) the realistic ladder below at the current SAA, or (b) the higher-selection SAA with a +100 bps target; the blueprint adopts (a) for year 1–3 and revisits at the 3-year review.

Worked comparison of the two SAAs the IC must choose between (§12 item 6). Expected gross sleeve alpha vs the T2 component, base case (approx., house priors): direct book +2.5% p.a. pre-cost, active mid/small MF +1.5% net of TER, factor funds +0.5%, passive −0.1% (tracking difference), TAA/other +17 bps (the residual that reconciles the CMA-implied +55 bps at SAA (a)). Option (b) moves 6 pp out of passive and 2 pp out of factors into direct (+4 pp), active mid (+2 pp) and active small (+2 pp); domestic equity stays 50%.

| Metric (Moderate) | (a) Current SAA: passive 22 / factor 10 / mid 7 / small 3 / direct 8 | (b) Higher-selection SAA: passive 16 / factor 8 / mid 9 / small 5 / direct 12 |
|---|---|---|
| Gross active return, base case | 20 + 15 + 5 − 2.2 + 17.2 = **+55 bps** | 30 + 21 + 4 − 1.6 + 17.2 = **+71 bps** |
| Gross, optimistic (direct +4%, active +2.5%, factor +0.75%) | +80 bps | +105 bps |
| Gross, downside (direct 0%, active +0.5%, factor +0.25%) | +23 bps | +25 bps |
| R1 → R2 load (fee 30 + GST 5.4 + opex 10 + booked trading) | 53 bps | 54 bps (trading +1) |
| Net alpha vs T2 (R2): base / optimistic / downside | **≈ +2 / +27 / −30 bps** | **≈ +17 / +51 / −29 bps** |
| Ex-ante TE vs T2 (approx.; direct-sleeve TE 10%, active-MF 7%, factor 7%, other 1.2%, ρ direct–active 0.4) | ≈ 1.9% (band 1.5–2.0%) | ≈ 2.3% (range 2.2–2.8%) |
| Information ratio, base / optimistic | 0.01 / 0.14 | 0.07 / 0.21 |
| Cash TCO pre-PM-layer (§7.9 per-sleeve rates) | 141 bps | ≈ 149 bps (+8.4: direct +7.0, active +5.8, passive/factor −4.4) → all-in ≈ 194 bps |
| Line count / monthly consent friction | ≈ 50 lines; 20–25 direct names | 56–58 lines (cap 60); 28–30 direct names; +5–8 consent lines per RPP; direct turnover ≈ 3.6% of NAV vs 2.4% |
| Gross alpha required for +100 bps net | 153 bps → direct sleeve would need ≈ **+12% p.a.** | 154 bps → direct sleeve would need ≈ **+8% p.a.** with active +2.5% and factor +0.75% |

Reading: option (b) roughly adds +15 bps of expected net alpha in the base case and +25 bps in the optimistic case for ≈ +0.4% TE, +8 bps TCO and 6–8 extra consent lines; neither SAA reaches +100 bps net at a 0.30% fee without a direct-sleeve alpha that no Indian multi-cap record supports persistently. Decision rule written into the IPS: adopt (a) for years 1–3; migrate to (b) at the 3-year review if the direct sleeve's factor-adjusted residual is ≥ +2% p.a. and manager selection ≥ +30 bps over the trailing 36 months; a +100 bps net target is only put to the IC together with a fee proposal (each −10 bps of fixed fee = +11.8 bps net incl. GST).

| Metric | Formula | Target | Amber | Red |
|---|---|---|---|---|
| Net alpha vs T2 | R2 − R_T2 annualised | ≥ 0 (1Y floor); ≥ +50 bps (3Y); ≥ +75 bps (5Y) | 3Y between −25 and +25 bps | 3Y < −25 bps |
| Information ratio | (R2 − R_T2) / TE | ≥ 0.25 (3Y); ≥ 0.35 (5Y) | 0.10–0.25 | < 0.10 |
| Tracking error | σ(R2 − R_T2)√12 | 1.5–3.5% (Mod), 2.0–4.5% (Agg) | to 4.5% / 6.0% | > 4.5% / > 6.0% or < 1.0% / < 1.5% |
| Sharpe | (R2 − R_f)/σ | ≥ T2 Sharpe + 0.10 | ± 0.10 | < T2 − 0.10 |
| Sortino | downside σ, threshold R_f | ≥ T2 + 0.15 | ± 0.15 | < T2 − 0.15 |
| Max drawdown | daily NAV | ≤ 1.10× T2 MDD | 1.10–1.25× | > 1.25× or −18% absolute |
| Calmar (3Y) | R2 / |MDD| | ≥ 0.60 | 0.40–0.60 | < 0.40 |
| Up / down capture vs T2 | Σ up / Σ down months | UC ≥ 95%, DC ≤ 85% | DC 85–100% | DC > 100% |
| Vs 80/20 (T3) risk-adjusted | (R2 − R_f)/σ vs 80/20's | ≥ 80/20 Sharpe + 0.10; return ≥ 80/20 return × 0.85 over 5Y | | return < 0.75× over 5Y |
| Batting average | % months R2 > T2 | ≥ 55% | 45–55% | < 45% |
| TAA hit rate | closed calls with positive payoff | ≥ 55% of trailing 12, payoff ratio ≥ 1.2 | 45–55% | < 45% |
| Active share (direct sleeve vs Nifty 500) | ½Σ|wₚ − w_b| | 60–80% | 50–60% | < 50% |
| Consent latency | median business days decision→execution | ≤ 3 | 4–5 | > 5 |
| Stale-priced assets | % NAV beyond price-age policy | ≤ 5% | 5–8% | > 8% |
| Tax drag (R2 − R3) | bps p.a. | ≤ 80 | 80–110 | > 110 |

Two consecutive red quarters on a primary metric → written IC remediation plan; red net alpha at 3Y → client-facing strategy and fee review.

### 6.5 Reporting cadence and contents

| Report | Timing | Audience | Contents | Hook |
|---|---|---|---|---|
| Daily NAV flash | T+1 10:00 | PM, Risk, RM | NAV; 1D/MTD/FYTD R1/R2 vs T1/T2/T3; sleeve MTD contributions; cash and uncalled commitments; pending consents with age; stale %; CAs due; band breaches; top 5 movers | internal |
| Weekly summary | Monday 09:00 | IC, RM | week/MTD TWRR; MTD Brinson; tranche status; ex-ante TE and factor tilts; drift; consents due; Thursday list | internal |
| Monthly pack and statement | month-end + 5 bd | client, IC | R0–R4 for 1M/3M/6M/1Y/3Y/5Y/SI (sub-year absolute); XIRR; Brinson by sleeve (Carino); look-through manager table; factor and FX lines; cost & tax vs budget; consent-latency log per trade; risk RAG; holdings; transactions; fees; charts (growth of ₹100 vs T1/T2/T3, drawdown, rolling 12M alpha, TE, waterfall); associate exposure and distributor commission (Reg 31 content delivered monthly) | Reg 31; APMI data lineage |
| SEBI/APMI filing | month-end + 7 wd | regulator | TWRR by IA, AUM, clients, T1 benchmark | circular 2022/172 |
| Quarterly report and call | quarter-end + 30 days | client (signed) | Reg 31 content; TWRR and XIRR with IA min/median/max; peers vs T1; open consents; FYTD tax summary; IC scorecard extract | Reg 31 (≤ 3 months) |
| Annual review | FY-end + 60 days | client, IC, board | audited performance (APMI ToR); full-year waterfall; TAA post-mortems; benchmark review; fee reconciliation; FY capital-gains statement (FIFO lots); IC scorecard published; GIPS-style composite (COULD) | annual audit |
| Event-driven | same day | client, IC | band breach ≥ 1.5×; MDD > −10%; AIF stale > 200 days; benchmark reconstitution; regulatory change; error trade | internal |

### 6.6 Performance dashboard spec

| Panel | Metrics | Refresh | Drill-down | Palette |
|---|---|---|---|---|
| Headline | NAV; R1–R4 for 1D/MTD/FYTD/1Y/3Y/SI; XIRR; alpha vs T1/T2/T3 | daily 10:00 | series → sleeve → instrument → lot | navy text; green positive; coral negative |
| Growth and drawdown | cumulative R2 vs T1/T2/T3; drawdown; rolling 12M/36M alpha | daily | period → attribution window | indigo portfolio, navy benchmark, amber reference |
| Attribution | Brinson by sleeve MTD/QTD/FYTD (Carino); look-through manager table; factor bars; FX line | daily (final at month-end) | sleeve → manager → holding | diverging green/coral |
| Implementation & consent | Perold shortfall ₹/bps per trade; latency histogram; open consents with age; SLA compliance | daily | trade → timeline (decision, consent, arrival, fills) | amber > 3 days, coral > 5 |
| Costs & taxes | fee/opex/tax lines vs budget; DTL; FYTD realised gains by bucket; harvest candidates; fee-deductibility sensitivity | daily | lot level | greys + amber |
| Risk-adjusted | §6.4 table with RAG; ex-ante TE and tilts | weekly (Friday) | metric → series → months | RAG |
| Valuation quality | stale %, unmatched CAs, recon breaks, NAV lag by asset | daily | asset → source → timestamp | coral on breaks |
| Peer & regulatory | APMI Multi-Asset quartile (NDPMS inclusion unclear_verify); filing clock | monthly | IA → period | navy |

Data lineage: every figure carries source table, as-of timestamp and benchmark version ID; reproducible from custodian files; month-end lock after IC sign-off with restatements logged.

### 6.7 Return-decomposition scorecard (quarterly IC scorecard; published to the client annually)

| Component | Owner | Metric | Budget / target | Worked year | Score (−2…+2) |
|---|---|---|---|---|---|
| SAA / policy portfolio | IC chair | T2 return vs client objective (CPI + 4% real ≈ 9.0%) | ≥ 9.0% | 9.705% | +1 |
| TAA | CIO | allocation effect; hit rate | ≥ +20 bps; ≥ 55% | −6.5 bps; 50% | −1 |
| Manager selection (MF/AIF/SIF; PMS look-through memo) | Head of Research | look-through selection | ≥ +30 bps | +44 bps | +1 |
| Security selection (direct) | Equity PM | vs Nifty 500 TRI; factor-adjusted residual > 0 | ≥ +50 bps | +46 bps | 0 |
| Implementation & consent | PM + client ops | Perold shortfall; latency | ≤ 25 bps; ≤ 3 days | 20 bps; 3.5 days | 0 |
| Costs | COO | fee + GST + opex + booked trading | ≤ 60 bps | 53 bps | +1 |
| Taxes | PM + tax adviser | R2 − R3; harvest realised | ≤ 80 bps | 45 bps | +1 |
| Valuation & reporting quality | Head of Performance | stale %, breaks, filings on time | ≤ 5%; 0 late | 3%; 0 | +2 |

TAA post-mortems: every call logged at inception (thesis, size ≥ ₹5 Cr, horizon, exit trigger, expected payoff, stop) and closed against the policy-weight counterfactual in a good/bad decision × good/bad outcome matrix; quarterly hit rate, payoff ratio, correlation with momentum. Scores feed variable pay (COULD; HR design needed).

---

## 7. Instrument & manager selection

### 7.1 ETFs and index funds

| Screen | Threshold at ₹500 Cr |
|---|---|
| Tracking difference (1Y) | ≤ 25 bps equity; ≤ 15 bps debt index |
| Tracking error (daily TD, annualised) | ≤ 50 bps large cap; ≤ 100 bps mid/small/factor |
| Scheme AUM | ≥ ₹1,000 Cr for any ticket > ₹15 Cr |
| On-screen ADV | ticket ≤ 20% of 5-day cumulative ADV; ADV < ₹50 Cr/day → never on screen |
| Bid-ask | ≤ 10 bps Nifty/Sensex; ≤ 25 bps factor/international |
| iNAV premium/discount | |x| ≤ 15 bps at order time, else AMC-direct / index fund |
| Replication | physical only; SLB on the basket only if fully collateralised and disclosed |
| Expense ratio | equity index/ETF BER ≤ 20 bps (MF Regulations 2026: BER replaces TER from 1-Apr-2026; cash brokerage cap 6 bps from an effective ≈ 8.6 bps, derivatives 2 bps — verified; exit-load cap change approx.) |

ETF vs index fund break-even years = ETF round-trip cost ÷ (index-fund TER − ETF TER): 12 ÷ (18 − 4) ≈ 0.86 years. Rule: ETF (AP/AMC-direct) for positions held > 1 year and tickets ≥ ₹25 Cr; index fund for sub-threshold tickets, monthly-rebalanced sleeves (zero spread; 1-day NAV risk ≈ ₹25 lakh 1-σ on a ₹25 Cr tranche) and SIP-like deployment. Routing costs for a ₹25 Cr Nifty tranche: on-screen ≈ 15 bps; AP creation ≈ 6–7 bps; AMC-direct ≈ 4–6 bps; index fund 0 bps + NAV risk.

### 7.2 Active mutual funds (100-point scorecard; onboard ≥ 65 with no factor < 40; re-score semi-annually; capacity alert quarterly; < 50 or manager change → redemption recommendation in the next RPP)

| Factor | Weight | Rule |
|---|---|---|
| Rolling 3Y alpha consistency | 20 | % of rolling 3Y windows (5Y history) beating category benchmark |
| Rolling 5Y alpha consistency | 15 | same, longer window |
| Up/down capture | 15 | UC ≥ 100%, DC ≤ 85% (ratio ≥ 1.15) |
| Active share | 10 | ≥ 60%; hard fail if < 60% and TER > 100 bps |
| Size vs capacity | 15 | penalise AUM > 1.5× stated capacity; our ticket ≤ 1% of scheme AUM |
| Manager tenure | 10 | ≥ 3 years on this scheme; reset on change |
| Direct TER | 10 | large/flexi ≤ 70; mid ≤ 90; small ≤ 100 bps |
| Concentration / style drift | 5 | top-10 ≤ 45%; 8-quarter style consistency |

House stance: large cap passive; flexi/multi-cap active selectively; mid cap active, capacity-capped; small cap active, tightly capped; factor exposure via index funds. Hurdle: required net alpha = TER gap + churn-cost gap + 100 bps; mid-cap example 60 + 30 + 100 = 190 bps ≈ ₹66.5 lakh/yr on a ₹35 Cr sleeve.

### 7.3 Third-party PMS (outside AUM; one manager; ≤ 3% look-through)

Eight checks × 12.5 points, onboard ≥ 80 with zero red flags on capacity or valuation independence: APMI-disclosed TWRR ≥ 3Y; live (not back-tested) record with the annual firm-level audit certificate; strategy tag and benchmark history (no benchmark-hop without exit offer); IA capacity and AUM growth; fee structure with HWM (model: pure fixed 2.5% → 12.05% net after GST at 15% gross; 1.0% + 20% over 10% → 12.64%; 0% + 20% over 8% → 13.35%); concentration; APMI-empanelled valuation; SEBI-registered custodian with per-client segregation. Structure: client contract with the external PM, own accounts; Ionic recommends size, client consents; data-delivery SLA (statement ≤ 10 business days after month-end) is a condition of onboarding; Ionic's distributor commission disclosed and subject to the conflicts protocol.

### 7.4 AIFs (Cat II / Cat III) — ODD checklist scored 1–5, flag ≤ 2

Team stability across cycles; single-LP concentration ≤ 20%; fee stack (1.5–2.5% + 10–20% carry, hurdle 8–12%, catch-up, GST); drawdown schedule (10–15 business days notice → standing instruction #6); lock-in (Cat I/II ≥ 3 yrs close-ended; Cat III open-ended 1–3 yr soft lock); leverage (Cat III ≤ 2× NAV with daily SEBI reporting — read the PPM's own ceiling; feed gross notional into look-through); valuation independence (Cat I/II 6-monthly; Cat III monthly/quarterly); tax structure (Cat I/II pass-through, Cat III fund-level); demat units. Sizing: Cat II private credit 5% (₹25 Cr, 2 managers, ₹10–15 Cr each, ≤ 20% from one LP); Cat III 2% (1 manager); undrawn-commitment drag ≈ ₹0.83 Cr on ₹25 Cr drawn over 15 months at a 5.3 pp yield gap (linear approximation; re-model on actual call schedules). Illiquid + semi-liquid (Cat II + Cat III + SIF + REIT/InvIT) ≤ 15% of AUM. LVF (₹25 Cr minimum) and CIV co-investment (Reg 17A) are options for concentrated ideas once accreditation is in place.

### 7.5 SIF

₹10 lakh PAN-level minimum per AMC (waived for AI); AMC eligibility ≥ ₹10,000 Cr 3-yr AUM or CIO-experience route; unhedged shorts ≤ 25% of net assets; redemption daily–quarterly, notice ≤ 15 working days; category AUM ₹13,814 Cr (May-2026), 76% hybrid long-short; standardised compliance reporting from Jan-2026. Post-tax comparison at 12% gross: Cat III ≈ 1.75% + 15% over 10% → 9.95% net of fee → ≈ 7.16% after a blended 28% fund-level tax (the 28% corresponds to an income mix of ≈ 30% LTCG at 14.95% / 35% STCG at 23.92% / 35% business income at MMR 42.74% = 27.8% — corrected: the v1.0 text quoted a 60/25/15 mix that would give 21.4%, not 28%); SIF ≈ 1.25% fee → 10.75% → 9.14% post 14.95% LTCG on exit: **+1.98 pp/yr in SIF's favour ≈ ₹39.6 lakh/yr per ₹20 Cr**. Rule: SIF over Cat III wherever both exist at comparable quality; cap SIF at 3–5% of AUM until 2027-28 track records exist; require ≥ 12–18 months live.

Income-mix sensitivity (12% gross, same fee stacks; Cat III net of fee 9.95%, SIF net of fee 10.75%; SIF taxed at investor level 14.95% on exit if equity-oriented ≥ 65% domestic equity):

| Cat III income mix (LTCG / STCG / business) | Blended fund-level rate | Cat III post-tax | SIF (equity-oriented) post-tax | SIF edge, pp/yr | ₹ lakh/yr per ₹20 Cr |
|---|---|---|---|---|---|
| 100 / 0 / 0 (low-turnover long-biased) | 14.95% | 8.46% | 9.14% | **+0.68** | 13.6 |
| 60 / 25 / 15 (capital-gains-heavy) | 21.4% | 7.82% | 9.14% | **+1.32** | 26.4 |
| 30 / 35 / 35 (base case) | ≈ 28% | 7.16% | 9.14% | **+1.98** | 39.6 |
| 15 / 25 / 60 (business-income-heavy, active F&O) | 33.9% | 6.58% | 9.14% | **+2.56** | 51.2 |
| 0 / 0 / 100 (pure F&O / arbitrage book) | 42.74% | 5.70% | 9.14% | **+3.44** | 68.8 |
| Reversal case: SIF **not** equity-oriented (debt/hybrid < 65% equity → slab 39% on redemption) | — | 7.16% (base Cat III) | 6.56% | **−0.60** | −12.0 |

Reading: more business income in the Cat III *widens* the SIF edge (the MMR bites at fund level); the edge narrows to +0.7–1.3 pp only for capital-gains-heavy Cat III funds, where the 50 bps fee gap is most of the advantage and manager quality decides. The genuine reversal is a SIF whose scheme category is not equity-oriented — so the ODD adds two questions: the Cat III's 3-year realised income mix from its tax audit, and the SIF's category/equity-orientation test, before any commitment.

### 7.6 Direct equity (NIFTY-750 scorecard sleeve)

Sizing: base weight = 4% + 2% × (score − 70)/30, capped 6%; liquidity cap = min(20% × 5-day ADV × 5 ÷ sleeve size, 8%); final = min(base, cap); always run on trailing ADV. Example on a ₹40 Cr sleeve: score 85 / ADV ₹60 Cr → 5.0% = ₹2.0 Cr (40 bps of AUM); score 72 / ADV ₹25 Cr → 4.1% = ₹1.65 Cr. Construction: 20–25 names Moderate (₹40 Cr), 25–30 Aggressive (₹60 Cr) — name count = sleeve ÷ ₹1.6–2.4 Cr average, floor 20, cap 30 (reconciled); sector ≤ 25% of sleeve or benchmark weight + 5 pp; entry only after 2 consecutive monthly scorecard passes (accept the 4–8 week lag; disclose it as structural); exits immediate on hard triggers (rating/accounting red flag, promoter-pledge spike) via out-of-cycle mini-RPP; monthly overlap report vs active MF top-20 holdings — trim the direct line first when combined exposure breaches the single-name cap; turnover < 30% p.a.

### 7.7 Fixed income

Direct vs fund: direct G-sec/SDL for ≥ ₹10–15 Cr per issue, hold to maturity, duration lever (NDS-OM via custodian/PD; RBI Retail Direct is retail-scale only); funds/TMF for laddered AAA/SDL diversification and tax deferral; corporate bonds only via funds below a ₹50 Cr sleeve. Rating floor AA (BBB only inside a dedicated high-yield AIF); single issuer ≤ 3% of FI sleeve; ≥ 10% of secondary corporate-bond value via RFQ (regulatory floor). Entry-spread floors (approx., 2026): AAA PSU 10–60 bps, AAA NBFC 50–140 bps, AA 100–260 bps; 10-yr AAA–G-sec ≈ 221 bps. Duration within ±1 year of the T2 debt index; curve views via TMF/SDL-dated indices, not single issuers. Tax counsel review item: after-tax comparison of direct listed bonds vs TMF units for this client's entity mix.

### 7.8 Gold, silver, REIT/InvIT, international

Gold: ETF via AP/creation for tranches ≥ ₹20–25 Cr (GOLDBEES ≈ ₹58,000 Cr+ AUM; spreads 2–5 bps); no new SGBs (none issued since Feb-2024; exemption narrowed); legacy SGBs checked position-by-position. Silver: ≤ 1% (tactical), iNAV-limit orders only (Oct-2025 premiums 8–10% on creation pauses). REIT/InvIT: 4–5 names ≤ ₹6 Cr each; tax read from each unit's Form 64B; dividend exemption from 1-Apr-2026 pending enactment — model both cases (≈ 41 bps/yr of sleeve return at stake); STT on units verify. International: Indian-listed index funds/FoF first (NAV route for ≥ ₹25 Cr), Indian-listed ETF only at ≤ 1% premium (MON100-type premiums of 5–15% in 2022–24 when the cap bound), GIFT-IFSC feeders via LRS outside AUM when domestic windows shut; LRS/TCS tracked per family member.

### 7.9 Total cost of ownership (corrected — Moderate, cash basis, bps p.a. of sleeve; DTL accrual shown as memo)

The original TCO run carried a 100× unit-scaling bug in the tax-drag lines for gold, silver, arbitrage and REITs and assumed full annual realisation for hold-to-maturity sleeves; both are corrected here (§13). Cash tax = tax actually paid in the year at design turnover/income; DTL memo = tax that accrues on unrealised gains and crystallises on exit (R4 basis).

| Sleeve | Wt % | ₹ Cr | TER/mgmt | Embedded fund cost | Our txn | Cash tax p.a. | Illiquidity/latency | **Total cash TCO (bps)** | ₹ Cr/yr | Memo: DTL accrual (bps) |
|---|---|---|---|---|---|---|---|---|---|---|
| Nifty 50/100 ETF (AP) + index fund | 22 | 110 | 8 | 3 | 2 | 22 | 3 | **38** | 0.42 | 120 |
| Factor index funds | 10 | 50 | 30 | 25 | 2 | 45 | 3 | **105** | 0.53 | 110 |
| Active mid-cap MF | 7 | 35 | 70 | 35 | 1 | 26 | 2 | **134** | 0.47 | 140 |
| Active small-cap MF | 3 | 15 | 80 | 45 | 1 | 26 | 2 | **154** | 0.23 | 150 |
| Direct stocks | 8 | 40 | 0 | 0 | 12.6 | 155 (dividend 43 + realised LTCG 112) | 8 | **176** | 0.70 | 60 |
| International index fund/ETF | 5 | 25 | 65 | 15 | 3 | 30 | 10 | **123** | 0.31 | 110 |
| Short-duration / MM fund | 3 | 15 | 25 | 5 | 0 | 130 (50% churn at slab) | 0 | **160** | 0.24 | 130 |
| Target-maturity AAA/SDL funds | 13 | 65 | 18 | 5 | 1 | 0 (deferred) | 0 | **24** | 0.16 | 269 |
| 10-yr G-sec direct | 6 | 30 | 0 | 0 | 3 | 273 (coupon at slab) | 0 | **276** | 0.83 | 0 |
| AA credit via funds | 2 | 10 | 70 | 10 | 1 | 0 (deferred) | 0 | **81** | 0.08 | 320 |
| Arbitrage fund | 2 | 10 | 35 | 10 | 1 | 19 | 0 | **65** | 0.07 | 58 |
| Gold ETF | 5 | 25 | 60 | 5 | 2 | 12 | 2 | **81** | 0.20 | 108 |
| Silver ETF | 1 | 5 | 55 | 10 | 3 | 25 | 5 | **98** | 0.05 | 100 |
| Listed REIT/InvIT | 4 | 20 | 0 | 0 | 6 | 160 (interest/rent at slab) | 5 | **171** | 0.34 | 20 |
| Cat II private credit (×2) | 5 | 25 | 175 | 0 | 0 | 468 (interest at slab) | 40 | **683** | 1.71 | 0 |
| Cat III LS AIF | 2 | 10 | 190 | 30 | 0 | 308 (fund-level) | 15 | **543** | 0.54 | 0 |
| SIF hybrid LS | 2 | 10 | 125 | 30 | 0 | 0 (deferred) | 15 | **170** | 0.17 | 165 |
| **Weighted portfolio** | **100** | **500** | **39** | **10** | **2.6** | **83** | **5.2** | **≈ 141 bps** | **≈ ₹7.0 Cr** | **≈ 119** |

Add the PM layer: fee 0.30% (₹1.50 Cr) + GST (₹0.27 Cr) + opex ≈ 10 bps (₹0.50 Cr) = ₹2.27 Cr (45 bps). **All-in cash TCO ≈ 186 bps ≈ ₹9.3 Cr/yr** (was wrongly stated as ≈ 424 bps / ₹21.2 Cr). Reading: cash tax (83 bps) is still the largest single line but is concentrated in three places — Cat II interest (23 bps of portfolio TCO), G-sec coupons (16 bps) and direct-stock dividends/realised gains (12 bps) — so the levers are the size of the private-credit sleeve for a 39%-slab entity (a 25.17% company entity changes this), the balance between direct G-sec and TMF, and dividend-light beta vehicles. Non-tax TCO ≈ 57 bps (₹2.9 Cr) is where manager selection and execution quality earn their keep.

**Aggressive variant (same per-sleeve rates; pre-IPO row new and approx.; cash basis, bps p.a. of sleeve)** — built so the IC has a reconciled cost table if the client picks Aggressive (§12 item 2); both totals are now the `cost_bps` fields of the data pack:

| Sleeve | Wt % | ₹ Cr | Total cash TCO (bps) | ₹ Cr/yr | Memo: DTL accrual (bps) |
|---|---|---|---|---|---|
| Nifty 50/100 ETF (AP) + index fund | 25 | 125 | 38 | 0.47 | 120 |
| Factor index funds | 12 | 60 | 105 | 0.63 | 110 |
| Active mid-cap MF | 10 | 50 | 134 | 0.67 | 140 |
| Active small-cap MF | 5 | 25 | 154 | 0.39 | 150 |
| Direct stocks | 12 | 60 | 176 | 1.05 | 60 |
| International index fund/ETF | 7 | 35 | 123 | 0.43 | 110 |
| Short-duration / MM fund | 2 | 10 | 160 | 0.16 | 130 |
| Target-maturity AAA/SDL funds | 4 | 20 | 24 | 0.05 | 269 |
| 10-yr G-sec direct | 2 | 10 | 276 | 0.28 | 0 |
| Arbitrage fund | 2 | 10 | 65 | 0.07 | 58 |
| Gold ETF | 4 | 20 | 81 | 0.16 | 108 |
| Silver ETF | 1 | 5 | 98 | 0.05 | 100 |
| Listed REIT/InvIT | 2 | 10 | 171 | 0.17 | 20 |
| Cat II private credit (×2) | 4 | 20 | 683 | 1.37 | 0 |
| Cat III LS AIF | 2 | 10 | 543 | 0.54 | 0 |
| SIF hybrid LS | 3 | 15 | 170 | 0.26 | 165 |
| Pre-IPO / PE Cat II (mgmt 200 + illiquidity 50; cash tax 0 — pass-through gains realised only on exit; approx.) | 3 | 15 | 250 | 0.38 | 150 |
| **Weighted portfolio** | **100** | **500** | **≈ 142 bps** (TER 47 + embedded 13 + txn 3 + cash tax 73 + illiquidity 7) | **≈ ₹7.1 Cr** | **≈ 109** |

Add the same PM layer (₹2.27 Cr, 45 bps): **All-in cash TCO ≈ 188 bps ≈ ₹9.4 Cr/yr** — within 2 bps of Moderate, because the higher equity TER/impact (non-tax TCO ≈ 70 bps vs 57) is offset by a smaller slab-taxed G-sec/Cat II book (cash tax 73 bps vs 83). The v1.0 data-pack figures of 118 / 130 bps were unreconciled and are retired; KPI ceiling "≤ 190 bps all-in" applies to both variants.

### 7.10 Fee-layering rules

| Wrapper | PM fee on this sleeve | Distribution fee | Rule |
|---|---|---|---|
| MF / index fund / SIF | portfolio-level fee only; direct plan mandatory | prohibited | automated direct-plan check at onboarding and on every in-specie transfer |
| ETF | portfolio-level fee only | n/a | — |
| Third-party PMS | portfolio-level fee on the allocation and monitoring only; the external PM's fee is charged in the client's separate account | Ionic's distributor commission disclosed in every periodic report; IC best-selection minute vs non-fee-paying alternatives | no economic "fee on fee" without disclosed value-add |
| AIF Cat II/III | portfolio-level fee only; AIF fee/carry separate and disclosed in the fee illustration | n/a | — |
| Direct equity / bonds | portfolio-level fee; brokerage at actuals | n/a | Angel One rate card ≤ non-group rate; quarterly TCA |
| Group products (Angel One AMC/AIF/SIF) | as above; ≤ 10% of AUM (IPS) within 15/25/30% SEBI; Annexure A consent; real-time 80%-of-cap alert | n/a | IC minute must show the group product scored ≥ top-2 non-group alternatives |

---

## 8. Governance, operations, technology & automation

### 8.1 Investment Committee

Five voting members (corrected from "six voting"): CIO (chair), dedicated PM, Head of Risk, Head of Compliance, one independent senior advisor (tie-break); Head of Trading/Ops attends non-voting. Quorum 4 of 5 including at least one non-investment vote (Risk or Compliance). Owns: house view, model-version approval, RPP approval before it reaches the client, watchlist/exception decisions, quarterly scorecard. Decision log fields: date, ID, present, motion, vote, dissent, rationale, effective date, linked artefact (model hash, rpp_id); retained 10 years. Ad-hoc tail-event IC convenes at ≤ 4 hours' notice.

### 8.2 IPS contents (single master PDF + machine-readable YAML twin; semantic version; every SAA/band change is a minor version, IC-approved, client-notified)

1 Client entities, residency status of every beneficial owner (NRI branch if any), accreditation refs and validity dates, minimum-investment confirmations, authorised signatories and backups (board/trustee resolutions), succession/incapacity annex (Annex D: nominees, registered PoA alternates, preservation-mode rules), risk-tolerance questionnaire scores and the IC suitability minute (below). 2 Objective (CPI + 4% real, approx.), horizon, risk tolerance (explicit acknowledgement of a −32% Moderate / −43% Aggressive GFC-type outcome), liquidity needs (redemption terms: ≤ 20% of AUM T+5 bd; ≤ 80% in 30 days; balance on AIF liquidity), exclusions. 3 Canonical SAA table (§2.4) with bands, ₹ Cr, line-count cap. 4 Benchmarks T1/T2/T3 with the stated expected relationship to 80/20. 5 Consent Protocol (Annex B) and Standing Instructions Register (Annex C). 6 Eligible universe and hard limits (unlisted 15% IPS / 25% legal / LVAI terms; associates 10% IPS; derivatives; credit floor; §5.1). 7 Fees (0.30% + 10% over T2 with HWM, annual crystallisation, AIF sleeve at cost until independent NAV/distribution; GST; opex cap; exit load nil with 30-day notice under LVAI), fee illustration, MITC. 8 Hedge Protocol (Annex F), SLB authorisation (G), associate consent Annexure A (E), in-specie schedule, deployment schedule with acceleration triggers, tax-account structure. 9 Reporting pack list and cadence; grievance route (SEBI SCORES / ODR portal). 10 Change-in-law clause and accreditation-lapse clause. 11 Version history.

Risk-tolerance questionnaire and IC suitability minute (new; answered by the decision-maker of every investing entity; re-scored annually and after any life/liquidity event):

| # | Question | 1 | 3 | 5 | Type |
|---|---|---|---|---|---|
| 1 | Horizon for ≥ 80% of this capital | < 3 yrs | 5–7 yrs | > 10 yrs | capacity |
| 2 | Planned withdrawals over the next 3 years (% of AUM) | > 30% | 10–20% | < 5% | capacity |
| 3 | This ₹500 Cr as a share of the family's liquid net worth | > 75% | 25–50% | < 10% | capacity |
| 4 | Largest 12-month loss acceptable before changing course | −5% (₹25 Cr) | −15% (₹75 Cr) | −35% (₹175 Cr) | willingness |
| 5 | Reaction to a −20% move in three months | exit | hold | add on IC recommendation, pre-authorised ladder | willingness |
| 6 | Dependence on portfolio distributions for spending | full | partial (≤ 2% p.a.) | none | capacity |
| 7 | Experience with AIFs, PMS, derivatives, drawdowns lived through | none | one cycle | > 10 yrs incl. 2008/2020 | willingness |
| 8 | Return objective | CPI + 1% | CPI + 3% | CPI + 5% or more | willingness |
| 9 | Leverage / contingent liabilities elsewhere (pledges, guarantees) | heavy | moderate | none | capacity |
| 10 | Expected residency / entity / succession changes within 5 years | likely | possible | none | capacity |

Scoring: total 10–50; **capacity** (Q1, 2, 3, 6, 9, 10) and **willingness** (Q4, 5, 7, 8) are scored separately and the *lower* governs. ≤ 28 → Moderate (or flag a more conservative bespoke SAA); 29–35 → Moderate, Aggressive satellites only by IC exception; ≥ 36 → Aggressive eligible. Knock-outs: any "1" on Q1 or Q2 → Aggressive ineligible regardless of total; any "1" on Q4 → the −18% drawdown trigger is lowered to −12% and the hedge programme becomes a MUST. IC suitability minute (template fields): date; entities and respondents; scores by dimension; variant recommended and rationale in the client's words; explicit acknowledgement of the GFC-type outcome (−32% / −43%, ₹160 / ₹215 Cr) and of the illiquid sleeve's lock-ups; liquidity terms accepted; dissent (if any); signatures of IC chair, Head of Compliance and RM; re-score date. The minute is filed with the IPS version it justifies and is the first document produced in any inspection or dispute.

### 8.3 Consent workflow controls

| Control point | Maker | Checker | Tooling |
|---|---|---|---|
| RPP trade list | PM/RA | Compliance (pre-trade engine) | OMS rule engine |
| Order entry | dealer | second dealer / Ops match to RPP | two-factor release; rpp_id FK mandatory |
| Standing-instruction trigger | system | Ops daily exception report | RMS batch |
| Cash movement / RTGS | Ops | CFO / fund accountant | custodian dual authorisation |
| NAV / valuation override | fund accountant | Risk/Compliance | exception log |
| Model version change | PM | IC + Risk | git-style diff |
| Consent capture | RM | Compliance hash check | e-sign platform log |
| Engine code change (risk_calc, tco, rebalancing MC, TWRR) | Data | second reviewer + reconciliation vs prior run | change-control ticket (new) |
| Document/IPS merge (model version bump, CMA refresh, band reset, data-pack refresh) | PM/Data | Risk (second reviewer) runs the automated `reconciliation_checklist` cross-check; zero open items before release | reconciliation script + signed checklist (new, recurring) |

Consent-ledger record schema and 10-year WORM retention per §1.3; voice recordings (WAV + transcript) indexed by client and rpp_id; daily encrypted cross-region backup; monthly hash re-verification. PII (KYC, accreditation certificates) segregated under the DPDP Act 2023 with access control separate from market-data compute (new).

### 8.4 OMS / RMS / custody

| Instrument | Route | System of record | Settlement |
|---|---|---|---|
| Listed equity, ETFs, REIT/InvIT, gold/silver ETF | NSE/BSE via broker OMS; algo/DMA; block window ≥ ₹25 Cr; AP/AMC-direct for ETFs ≥ ₹25 Cr | OMS → client-name demat (3 purpose accounts) | T+1 |
| MF / index fund / SIF (direct plan) | MFU or BSE StAR MF, direct-plan flag enforced | OMS MF module → RTA folios by purpose | T+1 to T+3 |
| AIF Cat II/III | contribution agreement + drawdown notices; capital-call ledger | AIF tracker (committed / called / distributed; IRR, DPI, TVPI) | per PPM |
| G-sec / SDL | NDS-OM via custodian/PD or exchange segment | OMS bond module | T+1 |
| Corporate bonds | RFQ ≥ 10%; direct placement for large lots | OMS bond module | T+0–T+2 |
| Third-party PMS | outside OMS; consolidated-reporting feed | look-through DB | n/a |

Pre-trade rule engine (hard blocks, logged overrides only): unlisted headroom, associate headroom, derivative notional, no short/leverage, direct-plan flag, demat-account routing, credit floor, single-name/sector/AMC caps, valid unexpired consent FK. RMS enforces the same hard limits independently (defence in depth). Order time-stamping (placement, release, ack, fill; NTP) and a recorded dealing room are built now although the automated-OMS mandate binds only at ₹1,000 Cr AUM.

Custodian: SEBI-registered, PMS + AIF servicing, daily SFTP/API feed for equity, MF, AIF and bond legs, independent of the Angel One group; contract must carry SLA credits/penalties for late NAV/CA processing and an escalation path (Ops → CFO → contractual remedy) (new). Contingency (new): RFPs to ≥ 3 non-group custodians by day 5, decision by day 20; if no full-stack (equity + MF + AIF + bond/G-sec) custodian is signed by day 30, go live on a listed-only interim custody (equity/MF — served by every PMS custodian) with bonds and AIF commitments added when the full-stack custodian is live; the deployment-ladder start is tied to custodian go-live, never to the calendar; a group custodian is never used. Group-instrument routing (§4.5) is configured in the OMS before the first order. Cost ≈ 3–8 bps (₹15–40 lakh/yr approx.). Fund accounting: daily NAV T+1 morning; fee accrual daily; performance fee at HWM crystallisation. Broker: Angel One at actuals with quarterly TCA; ≥ 10% of listed flow via a second broker in year 1 (its OMS connectivity, settlement instructions and dual contract-note recon are budgeted, not "optional").

### 8.5 Reconciliations (11 types)

| Recon | Frequency | Compares | Break SLA | Escalation |
|---|---|---|---|---|
| Cash | daily T+1 AM | custodian bank statement vs ledger | same day > ₹10 lakh | Ops → CFO at 2 days |
| Holdings | daily | CDSL/NSDL + custodian file vs internal book | same day | Ops → Compliance > ₹25 lakh or > 2 days |
| MF folios | daily | CAMS/KFintech units and NAV vs ledger | T+1 | RTA ticket; escalate T+3 |
| AIF statements | monthly | units/NAV/capital account vs tracker | 5 bd of receipt | PM → fund IR |
| Corporate actions | daily / ex-date | depository CA feed vs entitlement vs credit | T+1 ex-date; T+3 credit | Ops → custodian |
| Dividends / interest | daily | bank credit vs entitlement | T+2 | Ops |
| Fee accruals | daily (mgmt), event (perf) | computed vs custodian/FA | monthly close T+3 | FA → Compliance |
| Benchmark data | daily | NSE Indices / AMFI / CRISIL feed vs stored series (version ID) | T+1 | Data |
| Composite/model deviation | monthly + weekly interim | actual weights vs Model Master, composite rules | house SLA | PM/Ops |
| Deployment tranches | weekly | planned vs executed | same week | Dealing |
| Attribution/TWRR | monthly | engine vs custodian-confirmed valuations | T+5 bd | PM/Risk |

Break ticket schema: type, date, amount, ageing, owner, root cause (timing, CA unprocessed, booking error, RTA/custodian error, valuation source), resolution, closed date. Weekly ageing report; > ₹25 lakh or > 5 business days → Compliance and IC pack. The existing house cash-recon automation is extended with (i) the AIF capital-call ledger, (ii) the bond/G-sec settlement leg, (iii) the third-party PMS look-through line (reported, not reconciled).

### 8.6 Data architecture and job schedule

Feeds: NSE/BSE bhavcopy and NSE Indices (EOD; intraday VIX optional); AMFI NAVs (nightly); custodian EOD (SFTP/API); RTA (CAMS/KFintech); APMI-empanelled debt valuations (CRISIL/ICRA Analytics/NSE Indices); CCIL NDS-OM/F-TRAC; depository CA file; RBI reference FX; IBJA/MCX gold and silver; international index/iNAV vendor; AIF administrator statements (PDF/Excel, manual ingest with a negotiated ≤ 10-business-day delivery SLA); regulatory watch (SEBI/APMI circulars, accreditation registry). Pipeline (Python, house pattern): 01:00 ingest → 01:30 validate → 02:00 compute → 02:30 publish → 06:00 recovery SLA → 06:30 pre-market check → 09:00 execution → 17:00 post-close fills and T+1 queue. Storage: append-only transactions/holdings ledger with rpp_id / standing_instruction_id FK (the schema's defining feature); columnar time-series store (parquet) for prices/NAVs/benchmarks; document store for RPPs, consents, IC minutes; PII segregated. Dashboards are static HTML regenerated by the pipeline and hosted internally with group access control; client-facing extracts are branded exports of the same computed dataset, never re-keyed.

### 8.7 Dashboards inventory

| Dashboard | Purpose | Owner | Refresh | Audience |
|---|---|---|---|---|
| IPS / allocation drift (extends existing) | actual vs model, bands, composite rules | PM/Ops | daily compute, weekly publish | IC, Ops, Compliance |
| Deployment tracker (extends existing) | Mon/Thu tranches for the ₹500 Cr and ongoing flows | Dealing | weekly | IC, Ops |
| Attribution / TWRR (extends existing) | Brinson, alpha vs T1/T2/T3, cost/tax | PM/Performance | monthly (daily internal) | IC, RM (client extract) |
| Tail-risk (new; §5.8) | VaR, drawdown, limits, stress, hedge book, early-warning | Risk | daily | IC, Risk, CIO |
| Consent tracker (new) | RPP status, SLA breaches, standing-instruction log, engagement KPI | Compliance/RM | daily | Compliance, RM, IC |
| Liquidity (new) | days-to-liquidate, AIF lock-ups/windows, cash ladder, capital-call calendar | Ops/Risk | weekly | IC, Ops |
| Cost / tax (new) | realised cost bps, tax drag STCG vs LTCG, DTL, fee vs cap, TCS receivable, harvest candidates | PM/FA | monthly | IC, CFO |
| Manager watchlist (new) | scorecards vs hurdle, style drift, capacity, notice status | PM/RA | quarterly | IC |
| Recon break board (new) | live breaks and ageing across 11 recons | Ops | daily | Ops, Compliance |
| Corporate-action calendar (new) | CAs, election deadlines, default status, CA mini-RPP clock | Ops | daily | Ops, PM, RM |
| Client consolidated view (new, client-facing) | NDPMS AUM + third-party PMS + LRS/IFSC sleeve look-through; LRS utilisation per member | RM | monthly | client |

### 8.8 Team and RACI (year 1, sized for build + run; corrected upward)

| Role | FTE | Core responsibility | Named backup |
|---|---|---|---|
| CIO / IC chair | 0.2 | house view, accountability | independent advisor (chair only) |
| PM (dedicated) | 1.0 | model, RPP authoring, manager selection | designated backup PM (rehearsed pre-go-live) |
| Research analyst | 1.0 | NIFTY-750 scorecard, manager/AIF DD, macro pillar | PM |
| Risk manager | 0.5–1.0 | VaR, limits, stress, hedge design, model validation | Head of Risk |
| Dealing | 1.0 | execution, participation discipline, AP/block routing | second dealer |
| Ops / fund accounting | 2.0–2.5 | 11 recons, NAV oversight, CAs, custodian/RTA/AIF liaison | Ops lead |
| Compliance (dedicated) | 1.0 | pre-trade engine, associate monitoring, consent audit, SEBI/APMI filing, AML/KYC, SCORES | designated backup officer |
| RM / client servicing | 0.5–1.0 | walkthroughs, consents, entity signatories, LRS tracking | second RM |
| Data / pipeline | 0.5 | pipeline, dashboards, change control | shared house team |
| **Total** | **7.7–9.2** | ≈ ₹55–65 Cr AUM per FTE in year 1 | |

| Activity | CIO | PM | Risk | Ops | Compl | RM |
|---|---|---|---|---|---|---|
| House view / IC sign-off | A | R | C | I | C | I |
| RPP authoring | I | R/A | C | I | C | I |
| Pre-trade compliance | I | C | I | I | R/A | I |
| Consent capture / SLA | I | I | I | C | A | R |
| Execution | I | C | I | R/A | I | I |
| Daily recon | I | I | C | R/A | I | I |
| Daily risk monitoring | I | C | R/A | I | I | I |
| Tail-event escalation | A | R | R | C | C | R |
| Monthly statement | I | C | I | R | A | R |
| SEBI/APMI filing | I | I | I | C | R/A | I |
| Model version change | A | R | C | I | C | I |
| AML/KYC/PMLA, SCORES | I | I | I | C | R/A | R |

### 8.9 Controls, BCP, client communication

Error trades: any order without a valid consent FK or outside RPP parameters is frozen, disclosed same day with a remedy (unwind at no cost or ratify), root-caused, reported to Compliance/IC within 24 hours; firm-borne losses go to a segregated error account funded by PI insurance plus a reserve (new cost line). AML/KYC/PMLA (new): beneficial-ownership capture for every entity, source-of-funds documentation for the ₹500 Cr inflow, enhanced due diligence, STR/CTR monitoring; grievance redressal via SEBI SCORES / ODR with a 21-day response SLA disclosed in the MITC. BCP: OMS/custodian outage → manual slips with dual sign-off and custodian direct confirmation, compliance checks replicated manually from the last validated dataset; feed failure → prior-day value with flag, never unflagged stale data; key-person → named backups; consent-ledger integrity incident → read-only lockdown, hash verification, client notification within 72 hours; a tabletop drill **before the first live monthly cycle**, full drill annually. Client-side succession and incapacity follow Annex D (§1.3): registered PoA alternate, nominee-as-trustee transmission, preservation mode with no new RPPs. Client documents: RPP (monthly + ad hoc), monthly statement, tail-event note, quarterly review, annual review and IPS refresh, cost & tax summary (April), Disclosure Document updates, grievance route, suitability minute and questionnaire re-score (annual).

### 8.10 Build-vs-buy

| Component | Decision | Rationale |
|---|---|---|
| OMS/RMS core | buy (licensed multi-asset OMS) + build the Reg-24 rule layer and consent-FK linkage | connectivity/algos are solved; the rule engine is house IP |
| Custodian / fund accounting | buy | regulated, mandatory |
| e-sign | buy (Aadhaar eSign / DSC API) + build RPP workflow/UI | legality needs a licensed provider |
| Dashboards | build (extend the house HTML suite) | core competency; encodes IPS/Reg-24 logic |
| Pipeline / recon | build (extend house Python pattern and cash-recon automation) | fastest path to daily VaR/TWRR |
| AIF/PMS tracker | build (lightweight v1 → module by day 90) | low volume, high specificity |
| CRM / portal | buy or extend RM tooling | not core |

### 8.11 Indicative annual operating cost (₹ lakh/yr, approx.)

| Item | ₹ lakh/yr | Basis |
|---|---|---|
| Custodian + fund accounting | 15–40 | 3–8 bps |
| OMS/RMS licence | 15–35 | mid-tier multi-asset |
| e-sign / consent platform | 3–8 | per-transaction |
| Data feeds and index licences (incl. APMI valuation, CCIL) | 10–20 | |
| Data/dashboard engineering | 8–12 | 0.5 FTE + hosting |
| Team (7.7–9.2 FTE; role-specific loaded cost: PM/Risk/RA ₹40–70 lakh, Ops/RM/Dealing ₹15–30 lakh) | 190–260 | corrected from a blended ₹18–25 lakh/FTE |
| Second-broker onboarding and TCA | 3–6 | new line |
| PI insurance / error reserve | 8–15 | new line |
| Audit, legal (APMI ToR audit, LVAI documentation, legal opinion / Informal Guidance), tax counsel | 12–20 | includes the standing-instruction opinion |
| Contingency / BCP | 5–8 | |
| **Total** | **≈ 270–425** | vs fee income ≈ ₹150 lakh fixed + performance fee (10% of outperformance; ≈ ₹25 lakh at +50 bps net) |

The single-mandate economics are negative-to-breakeven on the fixed fee alone; the build is justified only as a platform onto which a second NDPMS/DPMS mandate is onboarded within 12–18 months, or with a higher fixed fee (each +10 bps = +₹50 lakh/yr). Break-even platform AUM at 0.30% fixed ≈ ₹270–425 lakh ÷ 0.30% ≈ **₹900–1,400 Cr** (approx., before performance fees) — i.e., one further ₹400–900 Cr mandate. Pipeline ownership (new): Head of Wealth with the CIO; target profile = accredited family offices ≥ ₹100 Cr wanting control (NDPMS) or existing Allocate DPMS clients ≥ ₹50 Cr; milestones 3 qualified prospects by month 6, term sheet by month 12, signed by month 18; reported quarterly to the IC as a KPI (§11).

---

## 9. CAN vs SHOULD vs AVOID matrix

Verdict legend: MUST (regulatory or indispensable), SHOULD (do in phase), COULD (optional), AVOID. Feasibility: allowed / allowed_with_consent (AWC) / restricted / not_allowed / unclear_verify. Effort and impact: L/M/H. Phase: 0–30 / 30–90 / 90–180 days / later.

| # | Item | Domain | Verdict | NDPMS feasibility | Effort | Impact | Cadence | Phase | Why |
|---|---|---|---|---|---|---|---|---|---|
| 1 | LVAI onboarding for every entity; accreditation-lapse clause | Regulatory | MUST | allowed | M | H | one-time / annual renewal | 0–30 | bespoke agreement, unlisted headroom, AIF/SIF minimum waivers |
| 2 | Omnibus monthly RPP with e-sign, 2-bd SLA, 10-td validity | Regulatory/Ops | MUST | allowed | H | H | monthly | 0–30 (manual) → 30–90 (portal) | the legal client direction, batched |
| 3 | Narrow standing-instruction register (7 items) | Regulatory/Ops | SHOULD | unclear_verify | M | H | event | 0–30 draft; 30–90 live after opinion | removes friction from mechanical actions |
| 4 | Legal opinion / SEBI Informal Guidance on standing instructions and triggers | Regulatory | MUST | unclear_verify | M | H | one-time | 0–30 | gates every self-executing element |
| 5 | Self-executing sell-side de-risk triggers before clearance | Rebalancing/Risk | AVOID | restricted | L | H | — | — | disguised discretion; First Global precedent |
| 6 | Consent-generating mini-RPPs for all triggers (Phase 1) | Rebalancing/Risk | MUST | AWC | M | H | event | 0–30 | compliant bridge until counsel clears SIs |
| 7 | Canonical Model Master (Moderate/Aggressive) with bands in IPS | Allocation | MUST | AWC | M | H | one-time / annual | 0–30 | turns rebalancing into confirmation |
| 8 | Third-party PMS as separate client contract outside AUM | Regulatory/Selection | MUST | not_allowed inside AUM | M | M | one-time | 30–90 | PMS is a service, Reg 24(10) |
| 9 | Third-party model feeds inside NDPMS | Regulatory | AVOID | not_allowed | L | H | — | — | outsourcing prohibition |
| 10 | Core beta via ETFs (AP/AMC-direct) + index funds | Allocation/Selection | MUST | allowed | L | H | monthly | 0–30 | 3–10 bps, no price risk in consent lag |
| 11 | Factor index funds Quality/Low Vol/Momentum (momentum ≤ 4%) | Allocation | SHOULD | allowed | L | M | monthly | 0–30 | cheap structured active |
| 12 | Momentum > 5% standalone (Moderate) | Allocation | AVOID | allowed | L | L | — | — | turnover, −70% drawdowns |
| 13 | Active MFs mid/small only, direct plans, ≤ 1% of scheme AUM, scorecard ≥ 65 | Selection | SHOULD | allowed | M | M | quarterly | 0–30 | alpha persistence only there |
| 14 | Direct-equity sleeve 8–12%, 20–30 names, liquidity-capped, 2-month entry rule | Allocation/Selection | SHOULD | AWC | H | M | monthly | 0–30 | owned alpha; every trade a consent line |
| 15 | Cat II private credit 4–5% across 2 managers, downside-case sizing | Allocation/Selection | SHOULD | AWC | H | H | quarterly | 30–90 | NDPMS structural edge; slab tax noted |
| 16 | SIF over Cat III wherever both exist; SIF ≤ 3–5% | Selection | SHOULD | allowed | M | M | quarterly | 30–90 | +1.98 pp post-tax |
| 17 | High-leverage / high-churn Cat III | Selection | AVOID | restricted | L | H | — | — | MMR tax erases edge |
| 18 | Pre-IPO 3% (Aggressive only) | Allocation | COULD | AWC | H | L | quarterly | later | valuation burden |
| 19 | Fixed income: TMF ladder + direct 10-yr G-sec; AA ≤ 2%; corporate bonds via funds | Allocation/Selection | SHOULD | allowed | L | M | monthly | 0–30 | deferral + duration lever; credit floor |
| 20 | Debt MFs as default long-duration vehicle without deferral logic | Rebalancing | AVOID → nuanced | allowed | L | M | — | — | slab tax; use TMF for deferral, direct G-sec for duration |
| 21 | Arbitrage fund for cash > 1 month | Allocation | MUST | allowed | L | L | daily | 0–30 | equity taxation |
| 22 | Gold via ETF (AP); silver ≤ 1% iNAV-limit | Allocation | SHOULD | allowed | L | M | monthly | 0–30 | cheapest tail hedge; silver vol |
| 23 | New SGB purchases | Selection | AVOID | restricted | L | M | — | — | discontinued; exemption narrowed |
| 24 | International 5% in-AUM at ≤ 1% premium; LRS/IFSC outside AUM; per-member LRS/TCS tracker | Allocation/Regulatory | SHOULD | restricted | M | M | monthly | 30–90 | USD 7 bn cap |
| 25 | Overseas direct securities inside PMS | Regulatory | AVOID (until notified) | not_allowed | — | — | — | watch | 2026 draft only |
| 26 | Composite T2 (9 components) in agreement; T1 APMI; T3 80/20 reference | Performance | MUST | allowed | L | H | monthly | 0–30 | accountability yardstick |
| 27 | 80/20 as headline benchmark | Performance | AVOID | allowed | — | H | — | — | misstates target |
| 28 | Hybrid Strategy H rebalancing; ₹1 Cr min ticket; turnover budget | Rebalancing | MUST | AWC | M | H | monthly | 0–30 | 4–5× cheaper than calendar |
| 29 | Continuous band-only or quarterly-calendar-only rebalancing | Rebalancing | AVOID | AWC | L | M | — | — | incompatible with consent gate / worst of both |
| 30 | Three purpose demat accounts + purpose folios before first trade | Rebalancing/Ops | SHOULD | allowed | M | H | one-time | 0–30 | FIFO per account |
| 31 | Cash-flow-first rebalancing; STCG hurdle; March harvesting/netting pack | Rebalancing | MUST | AWC | L | H | monthly / annual | 0–30 | zero-tax drift closure |
| 32 | Rights subscription via standing instruction | Rebalancing | AVOID | restricted | L | M | — | — | active unlisted-cap event |
| 33 | Block window ≥ ₹25 Cr; AP ≥ ₹5 Cr; AMC-direct ≥ ₹25 Cr; participation ≤ 10–15% ADV | Execution | SHOULD | allowed | M | M | monthly | 0–30 | 10–15 bps saved per switch |
| 34 | Time-stamped OMS with consent FK ahead of the ₹1,000 Cr mandate | Ops | MUST | allowed | H | H | one-time | 0–30 | the inspection proof |
| 35 | 14-limit two-tier framework with passive/active breach logic | Risk | MUST | allowed | M | H | daily | 0–30 | one document to pre-clear RPPs |
| 36 | Daily parametric + historical VaR, EWMA, TE, drawdown, correlation regime; Kupiec back-test | Risk | MUST | allowed | M | H | daily | 30–90 | fat tails |
| 37 | Nightly stress library on live weights; hypothetical suite incl. client redemption | Risk | SHOULD | allowed | M | H | daily/monthly | 30–90 | static tables go stale |
| 38 | Partial tail hedge (95/85 spreads, 25–40% of equity sleeve, ≤ 1% AUM premium) when VIX < 15 | Risk | SHOULD | AWC | M | H | quarterly | 0–30 (first RPP) | cheap now; grinding-regime cost bounded |
| 39 | Full-notional put programme | Risk | AVOID | AWC | H | L | — | — | ≈ ₹14.5 Cr/yr running cost |
| 40 | Relying on 2026 derivative/short proposals | Risk | AVOID | not_allowed | — | H | — | — | not notified |
| 41 | 12-indicator early-warning board with pushed Red alerts | Risk | MUST | allowed | M | H | daily | 30–90 | disciplined triggers |
| 42 | Cat III gross-notional look-through; stale flags | Risk | SHOULD | allowed | H | H | monthly | 30–90 | hidden leverage/concentration |
| 43 | Daily TWRR engine R0–R4; XIRR with IA min/median/max; benchmark versioning | Performance | MUST | allowed | H | H | daily | 0–30 | regulatory floor + accountability |
| 44 | Brinson-Fachler + Carino; look-through and factor attribution; Perold consent-latency log | Performance | SHOULD | allowed | H | H | monthly | 30–90 | separates skill, luck, latency |
| 45 | Realistic net-alpha ladder (≥ 0 / +50 / +75 bps) at current SAA; revisit at 3Y | Performance | MUST | allowed | L | H | annual | 0–30 | CMA-implied alpha ≈ fee load |
| 46 | Fee 0.30% + 10% over T2 with HWM; perf fee never on unrealised AIF marks | Regulatory/Performance | MUST | allowed | L | M | one-time | 0–30 | alignment; HWM rule |
| 47 | GIPS-style composite, PME for AIFs, Campisi FI attribution | Performance | COULD | allowed | M–H | L | annual/quarterly | later | credibility extras |
| 48 | Daily attribution as a decision input; annualising < 1Y; presenting R0 as performance | Performance | AVOID | allowed | — | M–H | — | — | noise and misstatement |
| 49 | Five voting-member IC, 4-eyes controls, versioned Model Master, decision log | Governance | MUST | allowed | L | H | monthly | 0–30 | provenance of every decision |
| 50 | Associate cap 10% IPS, Annexure A consent, 80% alert, IC best-selection minute; extend to any distributor-fee product | Governance | MUST | AWC | L | M | event | 0–30 | captive-arm conflicts |
| 51 | Client-name accounts under custodian, no pooling | Ops | MUST | allowed | M | H | daily | 0–30 | segregation |
| 52 | Pooled/omnibus execution or netting against Allocate books | Ops | AVOID | not_allowed | — | H | — | — | breach |
| 53 | 11 recons with break SLAs; AIF ledger and bond leg added | Ops | MUST | allowed | M | H | daily | 30–90 | multi-instrument book |
| 54 | Standing instruction for AIF capital-call funding | Ops | SHOULD | AWC | L | H | event | 30–90 | avoids PPM default |
| 55 | CA-election fast-track SLA (4 bh contact, 3 bd decision, no response = no action) | Ops | SHOULD | allowed | L | M | event | 0–30 | rights windows close |
| 56 | Custodian SLA with credits/penalties; data-delivery SLAs for AIF/PMS statements | Ops | SHOULD | allowed | M | M | one-time | 0–30 | T+5 monthly close depends on it |
| 57 | Team 7.7–9.2 FTE; named tested backups for PM and Compliance | Ops | MUST | allowed | H | H | one-time | 0–30 | 1.5 Ops / 0.5 Compliance was too thin |
| 58 | Engine change control (second reviewer + reconciliation) | Ops/Risk | MUST | allowed | L | H | event | 0–30 | a 100× bug was caught in design |
| 59 | PI insurance / error reserve; AML/KYC/PMLA workstream; SCORES process; DPDP controls | Ops/Compliance | MUST | allowed | M | M | one-time / annual | 0–30 | absent from original designs |
| 60 | Sequenced build custodian → OMS rules → AP; BCP tabletop before first live cycle | Ops | MUST | allowed | M | H | one-time | 0–30 | dependency gating |
| 61 | Executive-summary RPP format, 45–60 min walkthrough, engagement KPI | Ops/RM | SHOULD | allowed | L | H | monthly | 0–30 | prevents rubber-stamping |
| 62 | Entity-specific consent sub-workflow (board/trustee resolutions) | Ops/RM | MUST | allowed | M | M | one-time | 0–30 | HUF/trust/company signatories |
| 63 | Second-mandate-ready platform | Ops | SHOULD | allowed | H | H | one-time | 90–180 | economics need scale |
| 64 | SLB on core holdings (≤ 20% of a position) | Regulatory | COULD | AWC | M | L | monthly | later | 0.5–3% on lent lots approx. |
| 65 | CIV co-investment alongside Cat II | Regulatory/Selection | COULD | AWC | H | L | event | later | deal-level access |
| 66 | Holding-company OPI into IFSC funds | Regulatory | COULD | not_allowed inside AUM | H | M | one-time | later | bypasses LRS ceiling |
| 67 | Intraday, HFT, options overwriting, leverage, naked shorts in the client account | All | AVOID | not_allowed | — | H | — | — | prohibited / uneconomic |
| 68 | Signatory succession/incapacity annex (nominee, registered PoA alternate, executor path, preservation mode) | Regulatory/Ops | MUST | allowed (PoA-direction under Reg 24: unclear_verify) | M | H | one-time / annual | 0–30 | no one can otherwise approve an RPP after a sole signatory's death/incapacity |
| 69 | Group-instrument best-execution control (`group_instrument` tag, second-broker/NAV routing, separate quarterly TCA bucket) | Execution/Compliance | MUST | allowed | L | M | daily / quarterly | 0–30 | Angel One is group and broker; inspections probe exactly this |
| 70 | Tax-adviser (day 15) and index-licence/data-vendor (day 20) engagement letters as dated gating deliverables | Ops/Compliance | MUST | allowed | L | H | one-time | 0–30 | load-bearing tax calls and T2 rights cannot stay "review items" |
| 71 | Realised drawdown-capture validation of the stress library (±10 pp per episode) | Risk | SHOULD | allowed | L | M | per episode / annual | 90–180 | capture ratios are single-pass model output until validated |
| 72 | FX-hedge decision costed (≈ 2.8% forward premium ≈ ₹0.7 Cr/yr on ₹25 Cr) and left unhedged by design | Risk | COULD | restricted | L | L | annual | 30–90 | IC sees the bps cost of leaving currency open |
| 73 | Recurring merge/IPS reconciliation with automated cross-check and two-person sign-off | Governance/Ops | MUST | allowed | L | H | event + annual | 0–30 | the stale-JSON/double-count error class recurs at every FY-end reset otherwise |
| 74 | Cat III income-mix and SIF equity-orientation tests in ODD (rate grid 14.95% → 42.7%) | Selection | SHOULD | allowed | L | L | per fund | 30–90 | SIF edge ranges +0.7 to +3.4 pp and reverses for a non-equity SIF |
| 75 | NRI/FEMA branch (PIS/NRE/NRO custody, TDS u/s 195, DSC consent, local-hours SLA) for any non-resident holder | Regulatory | MUST (conditional) | AWC | M | H | one-time | 0–30 | one NRI holder changes custody, withholding and consent channel |
| 76 | Higher-selection SAA option (b) quantified end-to-end; migration rule at 3-year review | Allocation/Performance | SHOULD | AWC | L | M | one-time / 3Y | 0–30 | both SAAs now carry alpha, TE, cost, IR and friction numbers |
| 77 | Risk-tolerance questionnaire (10 questions, capacity vs willingness, knock-outs) and IC suitability minute | Regulatory/Governance | MUST | allowed | L | H | one-time / annual | 0–30 | the first document an inspection or dispute asks for |
| 78 | Custodian contingency (≥ 3 RFPs by day 5, decision day 20, listed-only interim custody, ladder tied to custodian go-live) | Ops | SHOULD | allowed | M | H | one-time | 0–30 | a slow search must not pull the ladder onto an unready stack |
| 79 | Second-mandate pipeline with named owner and milestones; break-even ≈ ₹900–1,400 Cr platform AUM | Governance | SHOULD | allowed | M | H | quarterly | later | the platform's cost case has an accountable owner |
| 80 | Aggressive-variant TCO table (≈ 142 / ≈ 188 bps) reconciled to the data pack | Selection/Costs | SHOULD | allowed | L | M | annual | 0–30 | IC can cost the Aggressive choice |
| 81 | PME (Kaplan-Schoar, Direct Alpha), Campisi and GIPS-style composite specified with formulas and worked examples | Performance | COULD | allowed | M | L | quarterly / annual | later | named deliverables have a build spec |

---

## 10. Roadmap

| Window | Deliverable | Owner | Dependency | Verdict |
|---|---|---|---|---|
| **0–30 days** | Legal-entity structuring proposal from client counsel (entities, PANs, signatories); accreditation applications filed (Jan-2026 certificate format) | RM + Compliance + client counsel | none | MUST |
| | LVAI NDPMS agreement drafted with annexes A–H, canonical SAA/bands, T1/T2/T3, fee schedule, MITC, Annexure A consent, change-in-law and accreditation-lapse clauses, liquidity terms | Compliance + PM | entity structure | MUST |
| | Legal opinion commissioned on standing instructions, trigger-based actions and the unreachable-client protocol; decision on SEBI Informal Guidance | Compliance | agreement draft | MUST (gating) |
| | Custodian selected and contract signed with SLA credits; three demat accounts + purpose folios opened; AML/KYC/PMLA file complete | Ops + Compliance | entity structure | MUST |
| | OMS/RMS rule configuration started (needs custodian feed spec); consent-ledger schema live (e-mail/OTP consent acceptable interim, hashed) | Data + Compliance | custodian | MUST |
| | AP / AMC-direct relationships signed for Nifty and gold ETFs; second-broker onboarding started | Dealing | custodian settlement instructions | MUST |
| | Selection complete: 2 Nifty ETFs + 1 index fund, 3 factor funds, 2 mid-cap + 1 small-cap MF, 2 TMF, 2 international routes + backup, 4–5 REIT/InvITs, 22-name direct book, arbitrage/overnight funds | PM + RA | scorecards | SHOULD |
| | Daily pipeline: AMFI, NSE, custodian, RTA ingest; IPS/deployment/attribution dashboards extended with NDPMS placeholders; engine change-control adopted; TCO and rebalancing MC rebuilt (common random numbers) | Data | feeds | SHOULD |
| | Deployment schedule (8 weeks) with acceleration mini-RPP templates; first RPP includes the partial put-spread hedge (VIX 12.4) | PM + Risk | agreement signed | MUST |
| | BCP tabletop (tail event + custodian outage), backup-signatory rehearsal | Ops + Compliance | OMS/consent ledger | MUST |
| | **Day 5**: RFPs to ≥ 3 non-group custodians (equity + MF + AIF + bond/G-sec servicing); **day 20**: decision; contingency if unsigned by day 30 — listed-only interim custody, bonds/AIF added later, deployment start tied to custodian go-live | Ops + Compliance | none | MUST |
| | **Day 15**: tax-adviser engagement letter (scope: TMF vs direct listed bond after-tax by entity, REIT/InvIT dividend treatment pending enactment, fee deductibility, entity-mix rates, NRI withholding) — gates IPS §7 and §7.7; **day 20**: index-licence/data-vendor letters (NSE Indices: Nifty 500 TRI, Composite Debt, REITs & InvITs, Arbitrage; S&P DJI: S&P 500 TR; CRISIL fallback; IBJA; APMI-empanelled valuation agency; CCIL) — gates T2 publication in the agreement | COO + Compliance | agreement draft | MUST (gating) |
| | Risk-tolerance questionnaire scored for every entity; IC suitability minute signed before IPS sign-off | RM + Compliance + IC | entity structure | MUST |
| | Annex D executed: nominee on every demat/MF folio, registered PoA alternate per individual, executor path, preservation-mode rules; residency confirmed for every beneficial owner (any NRI → NRI/FEMA branch) | RM + Compliance + client counsel | entity structure | MUST |
| | Group-instrument tag and routing rule configured in the OMS; separate TCA bucket defined | Dealing + Compliance | OMS rules | MUST |
| | Data-pack reconciliation closed (Nifty BeES ₹66,777 Cr verified 9-Sep-2026; Sharpe 0.41/0.39/0.29; 14 limits; ladder totals) and the recurring `reconciliation_checklist` adopted as the release gate for every model/IPS version | Data + Risk | — | MUST |
| **30–90 days** | Consent portal v1 (Aadhaar eSign/DSC, OTP fallback), consent-tracker dashboard, standing-instruction register configured per legal opinion (Phase 2 conversion where cleared) | Data + Compliance | legal opinion | MUST |
| | AIF diligence and commitments (2 private credit, 1 Cat III, 1 SIF); capital-call ledger and SI #6 live; data-delivery SLAs signed | PM + Ops | accreditation | SHOULD |
| | Third-party PMS onboarding as a separate contract; look-through feed | RM + PM | client consent | SHOULD |
| | Tail-risk dashboard live (daily VaR/ES/EWMA/TE, limits, stress, hedge book, early-warning with pushed alerts); bond and AIF recon legs | Risk + Data | pipeline | SHOULD |
| | First full live monthly cycle end-to-end (RPP → consent → execution → recon → statement) dry-run audited by Compliance; SEBI/APMI filing with T1 tag | All | portal | MUST |
| | First TAA cycle with conviction scoring; Brinson/Carino and Perold logs live | PM + Performance | TWRR engine | SHOULD |
| | **Day 45**: live AA − AAA spread series stored; provisional 100/150 bp thresholds replaced by 60-day mean + 1σ / + 2σ; FX-hedge cost memo to IC with forward premium sourced live (CCIL/FBIL) | Risk + Data | feeds | SHOULD |
| | Cat III income-mix and SIF equity-orientation questions added to ODD before any alternatives commitment | PM + RA | AIF diligence | SHOULD |
| **90–180 days** | Full automation of the 01:00–02:30 pipeline; manager watchlist scorecard; quarterly TCA report; liquidity, cost/tax and CA dashboards; client consolidated view with LRS/TCS tracker | Data + PM + RM | prior phases | SHOULD |
| | Kupiec back-test framework ready for month 12; PME for AIFs; fee-deductibility sensitivity in R3/R4 | Risk + Performance | 250 live days | COULD |
| | Capture-ratio validation log opened (every Nifty drawdown ≥ 5%: realised vs model capture, ±10 pp); PME (Kaplan-Schoar, Direct Alpha) on first Cat II statements; Campisi prototype on the ₹120 Cr FI sleeve | Risk + Performance | live NAV history; AIF statements | SHOULD / COULD |
| | First quarterly IC scorecard and TAA post-mortems; 6-month review of CMAs, bands, line count, standing-instruction usage; decision on SIF/PMS additions | IC | 2 quarters of data | SHOULD |
| | Documented BCP with full drill; second-mandate onboarding playbook; cost review vs ₹270–425 lakh budget | Ops + CIO | — | SHOULD |
| **Later (6–18 months)** | Second-mandate pipeline (owner: Head of Wealth with CIO): 3 qualified prospects by month 6, term sheet by month 12, signed by month 18; break-even ≈ ₹900–1,400 Cr platform AUM at 0.30% (approx.) | Head of Wealth + CIO | platform ready | SHOULD |
| | FY-end merge/IPS reconciliation run with the CMA refresh and band reset (automated cross-check, two-person sign-off) before any client document | Data + Risk + IC | — | MUST |

---

## 11. KPIs for owning the returns

| KPI | Target | Cadence | Owner |
|---|---|---|---|
| Net alpha vs T2 (R2 basis) | ≥ 0 (1Y); ≥ +50 bps (3Y); ≥ +75 bps (5Y) | monthly reported, quarterly judged | CIO |
| Risk-adjusted vs 80/20 (T3) | Sharpe ≥ 80/20 + 0.10; 5Y return ≥ 0.85× 80/20 at ≤ 0.75× its vol | quarterly | CIO |
| Information ratio (3Y) | ≥ 0.25 | quarterly | CIO |
| Tracking error vs T2 | 1.5–3.5% Moderate / 2.0–4.5% Aggressive | weekly | Risk |
| Down capture vs T2 | ≤ 85% | quarterly | PM |
| Max drawdown | ≤ 1.10× T2; never worse than −18% without a client decision on record | daily | Risk |
| TAA hit rate / payoff ratio | ≥ 55% / ≥ 1.2 | quarterly | CIO |
| Direct-sleeve selection vs Nifty 500 TRI (factor-adjusted residual) | ≥ +50 bps p.a., residual > 0 | quarterly | Equity PM |
| Manager-selection effect (look-through) | ≥ +30 bps p.a. | quarterly | Head of Research |
| Implementation shortfall (Perold) | ≤ 25 bps p.a.; consent-latency component ≤ 15 bps | monthly | PM + Ops |
| Consent latency | median ≤ 3 bd, 90th pct ≤ 6 bd; zero lapsed RPPs from house delay | monthly | RM |
| Client engagement | ≥ 1 substantive question or modification per RPP on average; walkthrough attendance ≥ 90% | monthly | RM |
| Slippage vs arrival | ≤ 15 bps per RPP | monthly | Dealing |
| Liquid-book turnover | 15–25%/yr | annual | PM |
| Cost lines vs budget | fee + GST + opex + booked trading ≤ 60 bps; weighted TER ≤ 45 bps | monthly | COO |
| Tax drag (R2 − R3) | ≤ 80 bps; STCG realised for rebalancing = 0 unless hurdle cleared; harvesting executed every March | monthly / annual | PM + tax adviser |
| Cash TCO (§7.9) | ≤ 190 bps all-in | annual | COO |
| Limit breaches | zero active breaches; passive breaches cured within policy | daily | Compliance |
| Recon breaks | none > ₹25 lakh or > 5 bd open at month-end | daily | Ops |
| Valuation quality | stale-priced ≤ 5% NAV; zero unflagged stale data | daily | Performance |
| Regulatory | 100% on-time SEBI/APMI filings; audit confirmation ≤ 60 days; zero inspection findings on consent evidence | monthly / annual | Compliance |
| Error trades | zero unauthorised orders (no valid FK) | daily | Compliance |
| Group-instrument execution quality | slippage on Angel One group-instrument trades ≤ non-group median + 3 bps; 100% of listed group securities via the second broker or NAV/AP route | quarterly | Dealing/Compliance |
| Suitability currency | questionnaire re-scored and IC minute refreshed annually and after any life/liquidity event; zero RPPs issued against an expired minute | annual | RM/Compliance |
| Merge/IPS reconciliation | automated `reconciliation_checklist` passes with zero open items before every model-version bump, CMA refresh and client document | event + annual | Data + Risk |
| Stress-model validity | realised capture within ±10 pp of model for every Nifty drawdown ≥ 5% | per episode | Risk |
| Platform economics | second mandate: 3 qualified prospects by month 6, term sheet by month 12, signed by month 18 (owner: Head of Wealth); opex/AUM ≤ 0.85% by year 2 | quarterly / annual | CIO/COO |

---

## 12. Open decisions for the client / IC

1. **Entity structure**: which entities hold the ₹500 Cr (individual/HUF/family trust/holding company), each accrediting and signing ≥ ₹10 Cr; determines tax rate (39% vs 25.17%), LRS vs OPI, SIF/AIF minimums, per-PAN exemption and signatory workflow. Any NRI member triggers the NRI/FEMA branch outlined in §1.6 (PIS/NRE/NRO custody, TDS at source, DSC consent, local-hours SLA) — residency is confirmed for every beneficial owner on day 1.
2. **Variant**: Moderate or Aggressive (or a blend), decided by the 10-question capacity/willingness questionnaire and IC suitability minute of §8.2 (lower of capacity and willingness governs; knock-outs on horizon/withdrawals); explicit acknowledgement of a −32% / −43% GFC-type outcome; reconciled cost tables for both variants in §7.9 (≈ 186 vs ≈ 188 bps all-in).
3. **Consent mechanics**: omnibus e-sign vs line-by-line; 2-business-day SLA; who signs, backups, board/trustee resolutions; portal vs fallback channels.
4. **Standing instructions**: which of the seven the client pre-authorises now; whether to seek SEBI Informal Guidance before converting any trigger to self-executing.
5. **Benchmark and fee**: T2 composite as primary with the stated 80/20 relationship; 0.30% + 10% over T2 with HWM (annual crystallisation; AIF sleeve at cost); performance-fee base pre-tax; exit load nil with 30-day notice.
6. **Alpha ladder**: accept ≥ 0 / +50 / +75 bps net at the current SAA (a), or adopt the higher-selection SAA (b) (direct 12%, active 14%; worked in §6.4: base-case net alpha ≈ +17 vs +2 bps, TE ≈ 2.3% vs 1.9%, TCO +8 bps, 6–8 extra consent lines); note that +100 bps net is not reachable under either SAA at a 0.30% fee without an implausible direct-sleeve alpha — the recommendation is (a) with the 3-year migration rule.
7. **Unlisted cap**: 15% IPS (recommended) vs using LVAI headroom for a larger private-credit/PE programme; downside-case sizing accepted.
8. **International route**: 5% in-AUM plus family LRS/IFSC (≈ ₹12 Cr/yr for 5 adults, ₹2.4 Cr TCS lock) vs holding-company OPI; look-through reporting of outside-AUM sleeves.
9. **Group products and third-party PMS**: 10% IPS cap and Annexure A consent; whether any third-party PMS is wanted, with distributor commission disclosed.
10. **Hedge programme**: standing partial put-spread cover with ≤ 1% AUM premium budget, initiated now at VIX 12.4; SLB authorisation.
11. **Tax structure**: three demat accounts and purpose folios; sharing of the personal-book gain/loss ledger and LTCG exemption usage; tax adviser sign-off on the TMF-vs-direct-bond and REIT/InvIT positions.
12. **Liquidity terms**: ≤ 20% of AUM in T+5 bd, ≤ 80% in 30 days, balance on AIF liquidity; planned withdrawals over 3 years.
13. **Deployment speed**: 8 weeks with acceleration (recommended) vs 12 weeks; mid-deployment re-confirmation at week 4; treatment of any in-specie legacy holdings and regular-plan units.
14. **Reporting**: monthly statement (house commitment) vs quarterly regulatory minimum; pushed Red alerts to the client or IC only.
15. **Regulatory change**: automatic adoption of PMS Regulations 2026 provisions via the change-in-law clause, or re-consent each time.
16. **Platform economics**: firm commitment to a second mandate within 18 months (owner: Head of Wealth with the CIO; milestones 3 prospects / term sheet / signed at months 6 / 12 / 18; break-even ≈ ₹900–1,400 Cr platform AUM), or a higher fixed fee.
17. **Succession and NRI status**: execution of Annex D (nominees, registered PoA alternates, preservation mode) by every individual signatory, and confirmation of residency for every beneficial owner.

---

## 13. Corrections adopted from the critique

- Client-reporting clause: the performance design cited "Regulation 22"; **Regulation 31** of the PMS Regulations 2020 governs the ≤ 3-month client report (Reg 22 is the client agreement clause). Verified; used consistently.
- Custodian: the regulatory design's "historic < ₹500 Cr exemption binds anyway" was wrong; under Reg 30 a custodian is mandatory for every PM except advisory-only. The AUM framing is dropped.
- Third-party PMS inside the sleeve tables: removed from the in-AUM Model Master; structured as a separate client contract outside NDPMS AUM, look-through only, with the distributor-commission conflict brought under the group-product protocol.
- Five-sleeve summary summed to 110%: Satellite alpha corrected to 23% (Moderate) / 34% (Aggressive); table now foots to 100%.
- Four competing SAA / Policy Composite versions: one canonical Moderate and Aggressive table (§2.4) and one 9-component T2 composite (§2.5); the regulatory design's §5.3 band table and the performance design's Table 3 are retired; international resolved at 5% in-AUM (7.5–10% household look-through); REITs benchmarked to the Nifty REITs & InvITs Index, not arbitrage.
- Credit floor breach: Moderate AA credit was 16.7% of the FI sleeve against a 10% ceiling; trimmed to 2% of AUM (8.3% of FI), TMF raised to 13%.
- Stress numbers: two different GFC/COVID losses existed; the risk engine's re-pricing is canonical (Moderate −32.0% / −22.8%; Aggressive −43.0% / −28.8%). Capture ratios restated as min–median–max (39–63%, median 54%; 62–81%, median 71%) instead of a single band.
- TCO tax-drag bug: gold, silver, arbitrage and REIT rows carried a 100× unit error (1,196 / 2,542 / 1,914 / 1,624 bps); corrected to 12 / 25 / 19 / ≈ 160 bps. Full-annual-realisation was replaced by cash-tax vs DTL-accrual columns. All-in cash TCO is ≈ 186 bps (₹9.3 Cr), not 424 bps (₹21.2 Cr); "tax is the biggest lever" survives only in the narrower form stated in §7.9.
- Worked example B arithmetic (₹59 lakh ≠ 15 bps): rebuilt from the cost stack with a self-check — on-screen ≈ ₹10.8 lakh (27 bps) vs AP ≈ ₹4.8 lakh (12 bps).
- Gross alpha vs fee load: CMA-implied gross alpha (+55 / +45 bps) is below a +100 bps net target; fee fixed at 0.30% (not 0.50% in one design), R1→R2 load ≈ 53 bps, and the accountability ladder reset to ≥ 0 / +50 / +75 bps with the higher-selection alternative put to the IC.
- Tracking-error governance: constructed ex-ante TE (1.5–2.0% / 2.0–2.5%) sat below the old "green" floor (2.5% / 4.5%); bands reset to 1.5–3.5% / 2.0–4.5% with closet-indexing red at < 1.0% / < 1.5%.
- Self-executing 1.5× band de-risk trigger marked "must": downgraded to consent-generating (mini-RPP) until legal opinion / Informal Guidance; the deployment-ladder acceleration is now a named seventh standing instruction subject to the same gate, with a week-4 re-confirmation.
- LVAI framed as the fix for consent mechanics: corrected — LVAI relaxes agreement form, fees, exit load and unlisted cap; it does not change the Reg 24 client-direction test. An accreditation-lapse clause and renewal tracker were added.
- USD/INR anchored at ≈ ₹88 in the risk board and LRS maths: replaced with the verified 95.79 (LRS ≈ ₹2.39 Cr per adult; ≈ ₹12 Cr/yr for five). The 10-yr G-sec anchor updated to ≈ 7.0%; the Nifty level used is the verified 11-Sep-2026 close 23,398.10 (the data pack's 23,914.45 was the 2-Sep close).
- Consent-latency "cost": relabelled as 1-σ dispersion; expected directional cost is quantified separately from the IC hit rate.
- Monte Carlo TE column: flagged as simulation noise (no common random numbers); Strategy H is adopted on turnover/cost/tax grounds only; rebuild scheduled.
- Cat III and SIF conflated in one CMA row: split into two rows with distinct tax treatment; the Cat III 28% blended rate now states its income-mix assumption.
- Credit-event scenario mislabelled "5% cap fully used" at ₹12.5 Cr: relabelled as half the cap and a full-cap ₹25 Cr variant added.
- Cat III leverage invisible in look-through: gross-notional column added, feeding the single-manager and illiquid limits.
- DTL worked example applied the 15% surcharge cap to debt lots: R4 now applies the capital-gains cap only to equity lots and full slab surcharge to debt.
- "Cure window approx. 90 days" for an active unlisted breach: unsourced; dropped. Active breach = hard block.
- IC "six voting members" named five voters: corrected to five voting, quorum 4 incl. a non-investment vote.
- Team sizing 1.5 Ops / 0.5 Compliance and a blended ₹18–25 lakh/FTE: raised to 2.0–2.5 Ops, 1.0 dedicated Compliance, role-specific costs; total 7.7–9.2 FTE, opex ₹270–425 lakh.
- Roadmap parallelised custodian, OMS rules and AP onboarding with a BCP drill at 90–180 days: sequenced with dependencies; tabletop drill moved before the first live cycle.
- Missing items added: AIF capital-call standing instruction; CA-election SLA; custodian SLA teeth; entity-specific consent sub-workflow; LRS/TCS tracker; engine change control; PI insurance/error reserve; AML/KYC/PMLA; SCORES/ODR grievance route; DPDP controls; client-side redemption stress and stated liquidity terms; in-specie/legacy-holdings transition; executive-summary RPP and engagement KPI; second-broker budget; consent-arrival-dependent tranche rule; feed-recovery SLA; illiquid-CMA uncertainty bands; TWRR–XIRR divergence threshold.
- Inconsistent minor items unified: minimum trade size ₹1 Cr; direct-stock name count 20–25 (Moderate) / 25–30 (Aggressive) by sleeve size; a single dated market snapshot (Appendix A4) cited everywhere; PMS Regulations cited as the consolidated text last amended 10-Feb-2025 (verify for later amendments); MF Regulations 2026 brokerage cap stated as 6 bps cash (from an effective ≈ 8.6 bps) / 2 bps derivatives, with the exit-load figure marked approx.
- Fee non-deductibility: modelled as a sensitivity in R3/R4 and the cost dashboard.
- REIT/InvIT dividend exemption: carried as "pending enactment" at every point of use, both cases modelled.
- 2026 proposal figures: moved out of hard-limit rows into watch-list notes.

**v1.1 reconciliation pass (completeness review, 12-Sep-2026) — data pack and narrative tied together**

- blueprint_data.json: AA credit 4% / ₹20 Cr → **2% / ₹10 Cr**; target-maturity 11% / ₹55 Cr → **13% / ₹65 Cr**; the "4%-of-AUM AA line" cross-reference deleted; sleeves re-asserted to 100% / ₹500 Cr for both variants.
- Credit floor standardised at **AAA/AA+ ≥ 90% of the FI sleeve** (the 80% variant in the data pack deleted); single-name direct-stock cap standardised at **3% target / 5% hard** (the 5% / 8% variant deleted) before either is coded into the OMS rule engine.
- Limit taxonomy fixed: **14 hard limits** everywhere (TL;DR typo "13-limit" corrected; §5.1, §9 item 35, `risk_limits`); the five monitored bands that had been merged into the data-pack limit array (1-day VaR, TE, correlation regime, consent latency, leverage) moved to `risk_metric_bands` / `pre_trade_hard_blocks`; TE band in the data pack aligned to 1.5–3.5% / 2.0–4.5%.
- Deployment plan: the data pack's single 10-week ₹50 Cr/week ladder (AIF first call at week 8) replaced by the three-track ladder of §2.8 (8 × ₹37.5 Cr equity-like + ₹25 Cr REIT/silver closing tranche; 4 × ₹30 Cr fixed income; ₹45 Cr alternatives over 6–18 months; ₹10 Cr arbitrage sleeve); §2.8 table made arithmetically exact (parked cash ₹432.5 → ₹230 → ₹187.5 → ₹75 → ₹50 Cr; the week-8 "closing tranche" is now the ₹25 Cr stabiliser leg, not a ninth equity tranche); matrix and roadmap "10 weekly tranches" wording corrected.
- Return waterfall: the data pack subtracted the −20 bps implementation shortfall a second time (net −30.5 bps); rebuilt with `summed_in_waterfall` flags so R1 − T2 = +87.9, R2 − T2 = **+34.5**, R3 − T2 = **−10.5 bps**, matching §6.3.
- Costs: data-pack `cost_stack` replaced by the §7.9 per-sleeve cash-TCO rows (both variants); `portfolio_stats.cost_bps` 118 / 130 retired in favour of the reconciled **≈ 186 (Moderate) / ≈ 188 (Aggressive) bps all-in** (≈ 141 / ≈ 142 pre-PM-layer); an Aggressive TCO table added to §7.9.
- Sharpe: narrative 0.42 / 0.30 corrected to the arithmetic **0.41 / 0.29** ((10.0 − 6.0)/9.7; (10.0 − 6.0)/13.6); Aggressive 0.39 unchanged.
- Rebalancing comparison in the data pack carried a 10× unit error (525 for 52.5 bps) and mislabelled average drift as tracking error; rebuilt with rows A–H, correct units and the common-random-number caveat.
- Hedge menu / matrix: the data pack and matrix item 45 still made the 5% OTM put the "should"; aligned to the adopted 95/85 put-spread default (5% OTM put retained as the costing reference).
- Matrix item 6 (self-executing sell-side trigger) was still "should" in the data pack → **AVOID until cleared**; item 8 "Core/Tactical/Income" → Core/Tactical/Harvest; item 32 ticket floor "₹75 lakh–1 Cr" → ₹1 Cr; item 71 IC wording aligned to five voting + one non-voting; KPI targets (IR, TE, shortfall, tax drag, controllable cost, turnover, unlisted alert) aligned to §11.
- Nifty BeES AUM conflict closed: **₹66,777 Cr on 9-Sep-2026 (verified)** replaces the ₹53,989 Cr pack figure in §2.3 and Appendix A5.
- Cat III blended-tax statement corrected: 28% corresponds to ≈ 30/35/35 LTCG/STCG/business, not 60/25/15 (which gives 21.4%); full income-mix grid added (§7.5).
- Early-warning board: the AA − AAA indicator now ships with provisional thresholds (100 / 150 bp, derived from 2026 range prints, approx.) and a day-45 replacement rule, so all 12 indicators can fire from go-live.
- Open critic items closed in this pass: client-signatory succession/incapacity (Annex D, §1.3/§8.9); group-instrument best-execution control (§3.4/§4.5/§8.4); dated tax-adviser and index-licence engagement letters (§10); capture-ratio validation plan (§3.5/§5.2); costed FX-hedge decision (§5.5); business-income-heavy Cat III scenario (§7.5); NRI/FEMA branch outline (§1.6); recurring merge/IPS reconciliation (§3.5/§8.3, `reconciliation_checklist`); higher-selection SAA worked end-to-end (§6.4); risk-tolerance questionnaire and IC minute (§8.2); custodian contingency (§8.4/§10); second-mandate owner and pipeline (§8.11/§10/§11/§12); Aggressive TCO (§7.9); PME/Campisi/GIPS specs with formulas and worked examples (§6.3).
- Still open and labelled: PoA-holder direction under Reg 24 (unclear_verify — inside the legal opinion); FEMA schedule text for NRI caps and AIF/REIT units (verify); 12M forward premium is a July-2026 print (approx.); pre-IPO TCO row (approx.); APMI Multi-Asset benchmark list (verify).

---

## Appendix A: Data tables

Accuracy legend: **verified** = read from a primary/secondary source dated 2026 (search snippets; most primary pages were egress-blocked); **partially_verified** = headline cells verified, remainder reconstructed; **approx.** = analyst reconstruction from public NSE/CRISIL/RBI data, tolerance ±1 pp on returns, ±1% on levels, ±0.3 on FX. Re-pull from niftyindices.com, CRISIL, RBI and NSDL before client use.

### A1. Calendar-year total returns (%, INR) — partially_verified

| Year | Nifty 50 TRI | Midcap 150 TRI | Smallcap 250 TRI | Nifty 500 TRI | Gold INR | CRISIL Composite Bond | CRISIL Liquid | S&P 500 TR (USD) | USD/INR Δ | S&P 500 TR in INR (derived) | Nifty 50 Arbitrage |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2006 | +41.9 | +30.4 | +27.6 | +36.0 | +21.1 | +4.5 | +6.5 | +15.8 | −1.8 | +13.7 | n/a |
| 2007 | +56.8 | +78.4 | +97.0 | +64.0 | +16.3 | +7.0 | +7.6 | +5.5 | −10.9 | −6.0 | n/a |
| 2008 | **−51.3 [V]** | −64.9 | −68.6 (max DD −73 [V]) | −56.5 | +26.2 | +9.9 | +8.8 | −37.0 | +22.9 | −22.6 | n/a |
| 2009 | **+77.6 [V]** | +114.0 | +117.0 | +90.0 | +24.4 | +3.5 | +4.9 | +26.5 | −3.7 | +21.9 | n/a |
| 2010 | +19.2 | +20.0 | +17.6 | +15.3 | +23.2 | +5.0 | +5.4 | +15.1 | −4.0 | +10.5 | n/a |
| 2011 | −23.8 | −31.0 | −35.1 | −26.4 | +31.9 | +6.9 | +8.2 | +2.1 | +18.9 | +21.4 | +7.5 |
| 2012 | +29.4 | +46.7 | +39.8 | +33.5 | +12.1 | +9.4 | +8.5 | +16.0 | +2.8 | +19.3 | +8.5 |
| 2013 | +8.1 | −1.3 | −6.4 (max DD −32 [V]) | +4.8 | −4.9 | +3.8 | +9.0 | +32.4 | +13.0 | +49.6 | +8.5 |
| 2014 | +32.9 | +62.7 | +71.7 | +39.3 | −7.6 | +14.3 | +9.2 | +13.7 | +1.8 | +15.8 | +8.3 |
| 2015 | −3.0 | +9.7 | +11.3 | +0.2 | −6.7 | +8.6 | +8.2 | +1.4 | +4.9 | +6.4 | +7.6 |
| 2016 | +4.4 | +6.5 | +1.4 | +5.1 | +11.2 | +12.9 | +7.5 | +12.0 | +2.7 | +15.0 | +6.6 |
| 2017 | +30.3 | +55.7 | +58.5 | +37.7 | +5.4 | +4.7 | +6.7 | +21.8 | −6.0 | +14.5 | +5.6 |
| 2018 | +4.6 | −12.6 | −26.1 (max DD −36 [V]) | −2.1 | +7.5 | +5.9 | +7.6 | −4.4 | +9.3 | +4.5 | +6.2 |
| 2019 | +13.5 | +0.6 | −7.3 (max DD −22 [V]) | +9.0 | +23.7 | +10.7 | +6.9 | +31.5 | +2.1 | +34.3 | +6.2 |
| 2020 | +16.1 | **+25.6 [V]** | **+26.5 [V]** (max DD −44 [V]) | +17.9 | +28.3 | +12.3 | +4.6 | **+18.4 [V]** | +2.5 | +21.4 | +4.1 |
| 2021 | +25.6 | **+48.2 [V]** | **+63.3 [V]** | +31.6 | −3.9 | +3.4 | +3.6 | **+28.7 [V]** | +1.7 | +30.9 | +4.0 |
| 2022 | +5.7 | **+3.9 [V]** | **−2.6 [V]** | +4.3 | +13.9 | +3.0 | +5.1 | **−18.1 [V]** | +11.3 | −8.8 | +4.6 |
| 2023 | +21.3 | **+44.6 [V]** | **+49.1 [V]** | +26.9 | +15.1 | +7.3 | +7.1 | **+26.3 [V]** | +0.6 | +27.0 | +7.4 |
| 2024 | +10.1 | **+24.5 [V]** | **+27.2 [V]** | +16.2 | +21.0 | +8.8 | +7.3 | **+25.0 [V]** | +2.9 | +28.6 | +7.8 |
| 2025 | +11 to +12 | **+6.0 [V]** | **−5.5 [V]** | +8 to +9 | +74.1 (end ₹1,33,195 [V]) | +7.5 | +6.6 | **+17.9 [V]** | +4.8 | +23.5 | +6.7 |
| 2026 YTD (11-Sep) | ≈ −8 to −10 (8% below peak on 12-Aug [V]) | positive (−14% Jan–May, new peak 21-Jul [V]) | negative to flat | n/v | **+14.6 [V]** (₹1,52,650) | low single digit (10Y +50 bp) | ≈ +4.0 | n/v | **+6.8 [V]** (95.79) | n/v | ≈ +4.5 |

Unmarked cells approx. Readings: Nifty 50 TRI negative in 3 of 20 years (2008, 2011, 2015); Smallcap 250 negative in 7; gold negative in 4 (2013–15, 2021) and 2025 was its largest year; CRISIL Composite Bond never negative but ≈ 3% in 2013, 2021, 2022; S&P 500 in INR beat Nifty 50 TRI in 10 of 20 years; arbitrage 4–8.5% with low years (2020–22) at repo 4.0%.

### A2. Long-run CAGR and volatility — approx. (computed from A1; verified cross-checks: Nifty 50 TRI 20Y 12.44% to 27-Feb-2026; MO S&P 500 Index Fund 5Y 17.64% INR to 1-Sep-2026; Nifty 50 Arbitrage 1Y SD 1.41%)

| Series | 10Y CAGR (2016–25) | 15Y (2011–25) | 20Y (2006–25) | SD of annual returns 10Y / 15Y | Annualised daily vol |
|---|---|---|---|---|---|
| Nifty 50 TRI | 14.0 | 11.5 | 13.1 | 9.0 / 14.7 | ≈ 16 (10Y), 21–22 SI |
| Midcap 150 TRI | 18.3 | 16.3 | 16.2 | 23.1 / 27.4 | ≈ 19–20 / 23–24 |
| Smallcap 250 TRI | 14.8 | 13.2 | 13.7 | 31.0 / 33.2 | ≈ 22 / 26 |
| Nifty 500 TRI | 14.9 | 12.4 | 13.4 | 13.0 / 17.9 | ≈ 16–17 / 22 |
| Gold INR | 18.2 | 13.2 | 15.4 | 21.3 / 20.7 | ≈ 13–15 |
| CRISIL Composite Bond | 7.6 | 7.9 | 7.4 | 3.5 / 3.5 | ≈ 2.5–3.5 |
| CRISIL Liquid | 6.3 | 7.1 | 7.0 | 1.4 / 1.6 | ≈ 0.3–0.5 |
| S&P 500 TR in INR | 18.4 | 19.5 | 14.9 | 13.2 / 13.8 | ≈ 15–16 |
| Nifty 50 Arbitrage | 5.9 | 6.6 | n/a | 1.3 / 1.5 | ≈ 1.4 |

Rolling-window floors (daily windows Jan-2006–Aug-2026, approx.): Nifty 50 TRI 3Y min −5.5% (≈ 9% of windows negative), 10Y min 5.0% (none negative); Midcap 150 3Y min −15%, 10Y min 6.5%; Smallcap 250 3Y min −25% (≈ 25% negative), 10Y min 2%; 60/40 blend 10Y min 7.5%; house 80/20 3Y min −3% (≈ 5% negative).

### A3. Drawdown episodes and correlation matrix

Episodes: see §5.3 (Nifty −60% GFC [V], −38.4% COVID in 69 days with 231-day recovery [V], Smallcap 250 −61% Jan-2018→Mar-2020 [V], Midcap 150 −14% Jan–May 2026 [V]; other magnitudes approx.). Recovery times are price-index; TRI recovers 6–12 months sooner in long episodes; 2008 and 2011 took ≈ 3 years to regain the peak — plan liquidity and consent cadence for 3-year recoveries.

Approximate correlation matrix, monthly INR returns, Sep-2016–Aug-2026 (approx.; regime-dependent — equity–gold turned positive in Mar-2020; equity–USD/INR is ≈ −0.5 in FPI-outflow regimes such as 2013, 2018, 2022, 2026):

| | Nifty 50 | Midcap 150 | Smallcap 250 | Gold INR | India bonds | S&P 500 INR | USD/INR |
|---|---|---|---|---|---|---|---|
| Nifty 50 TRI | 1.00 | 0.85 | 0.75 | 0.00 | 0.10 | 0.45 | −0.35 |
| Midcap 150 TRI | 0.85 | 1.00 | 0.92 | −0.05 | 0.10 | 0.40 | −0.35 |
| Smallcap 250 TRI | 0.75 | 0.92 | 1.00 | −0.05 | 0.05 | 0.35 | −0.30 |
| Gold INR | 0.00 | −0.05 | −0.05 | 1.00 | 0.15 | 0.15 | 0.35 |
| India bonds (CRISIL Composite) | 0.10 | 0.10 | 0.05 | 0.15 | 1.00 | 0.05 | −0.15 |
| S&P 500 INR | 0.45 | 0.40 | 0.35 | 0.15 | 0.05 | 1.00 | 0.25 |
| USD/INR | −0.35 | −0.35 | −0.30 | 0.35 | −0.15 | 0.25 | 1.00 |

Diversification arithmetic: 55/15/20/10 Nifty / S&P-INR / bonds / gold ≈ 10.5% vol vs 16% for Nifty alone. Unhedged international and gold (both long USD) are the natural hedges to the FPI-outflow pattern.

### A4. Current market snapshot (11–12 Sep 2026) — the single dated snapshot every section cites

| Metric | Value | As of | Accuracy |
|---|---|---|---|
| Nifty 50 close | 23,398.10 (−79.70, −0.34%); day range 23,231–23,448 | 11-Sep-2026 | verified (5paisa) |
| Nifty 50 vs 2026 peak | ≈ 8% below peak on 12-Aug-2026 (peak ≈ 25,900–26,300, unverified) | 12-Aug-2026 | verified (snippet) |
| Nifty 50 trailing P/E | 19.78 (Trendlyne, 11-Sep) / 20.20 (IndexPE, 4-Sep) vs 5Y median 22.0, 10Y 23.3 | Sep-2026 | verified |
| Forward P/E | ≈ 17–18× | Sep-2026 | approx. |
| P/B | 3.17 (17-Jun); ≈ 3.0–3.1 | Jun-2026 | partially_verified |
| India VIX | 12.42 (52-week range 8.72–28.90; ATH 86.64 Mar-2020) | 11-Sep-2026 | verified |
| 10Y G-sec | > 7.00%, ≈ 10-month high | 11-Sep-2026 | verified |
| Repo | 5.25% (4th hold, neutral; SDF ≈ 5.00%, MSF ≈ 5.50% approx.); path 6.50% → 5.25% via Feb/Apr/Jun-25 and ≈ Dec-25 cuts | Aug-2026 | verified (rate) |
| USD/INR | 95.79 (record low rupee) | 11-Sep-2026 | verified |
| Gold 24K | ₹1,52,650/10 g spot; MCX ₹1,52,075; COMEX $4,388.70/oz; ≈ +40% 1Y | 11-Sep-2026 | verified |
| Silver | ₹2,33,120/kg | 11-Sep-2026 | verified |
| Brent / US 10Y | ≈ $110 / ≈ 5.0% | 11-Sep-2026 | verified |
| FPI equity flows CY2026 | net sell ≥ ₹1.75 lakh Cr by 25-Apr; ₹1,87,439 Cr by May; Sep YTD ≈ ₹2.0–2.5 lakh Cr | May-2026 | partially_verified |
| 10Y AAA − G-sec spread | ≈ 221 bp; 3Y ≈ 111 bp | 15-Aug-2026 | verified (tracker) |
| Nifty 500 Value 50 P/E | 10.37 | Sep-2026 | verified |
| NSE Nifty 50 impact cost (₹50 lakh basket) | 0.02% | Mar-2026 | verified |
| RBI FY27 CPI forecast | 5.0% | Aug-2026 | verified |

### A5. ETF liquidity — partially_verified (AUM prints from 2025-26 sources with dates not always visible; ADV/spreads approx.)

| ETF | Underlying | AUM ₹ Cr | ADV ₹ Cr | Bid-ask bps | TER % | Rule for ₹500 Cr |
|---|---|---|---|---|---|---|
| SBI Nifty 50 ETF | Nifty 50 TRI | > 2,00,000 (2026) | 50–150 | 3–10 | 0.04 | EPFO-dominated; creation units via AP at iNAV ± 2–5 bps |
| Nippon Nifty 50 BeES | Nifty 50 TRI | **66,777 (9-Sep-2026, verified — tickertape; the ₹53,989 Cr data-pack figure was a stale print, conflict closed)** | 200–400 | 1–3 | 0.04 | most liquid on screen; ₹25–50 Cr clips workable; CU 50,000 units |
| UTI Nifty 50 ETF | Nifty 50 TRI | ≈ 65,000 | 20–60 | 5–15 | 0.05 | creation route |
| ICICI Pru Nifty 50 ETF | Nifty 50 TRI | ≈ 25,000 | 20–60 | 3–10 | 0.03 | lowest TER |
| Nippon Gold BeES | domestic gold | 58,453 (2025-26); likely > 70,000 now | 300–600 | 2–5 | 0.79 | deepest gold ETF; premium usually < 20 bps |
| Other gold ETFs (SBI, ICICI, HDFC, Kotak, Axis) | domestic gold | 10,000–20,000 each | 30–150 | 5–15 | 0.5–0.8 | spread AMC concentration |
| Silver ETFs (Nippon, ICICI, HDFC, Tata, Axis, Kotak) | domestic silver | category 30,000–40,000; Nippon ≈ 10,000 | 100–300 | 5–15 (500–1,000 in Oct-2025 squeeze) | 0.5–0.6 | ≤ 1% of AUM; iNAV-limit orders |
| Liquid BeES / growth liquid ETFs | Nifty 1D Rate | 15,000–18,000 | 400–800 | 0–2 | 0.69 (growth variants cheaper) | margin/cash parking only |
| Bharat Bond ETFs 2030–2033 | Nifty Bharat Bond TMI (AAA PSU) | 40,000–45,000 combined | 2–10 per series | 20–50 | 0.0005 | never on screen; FoF / creation / TMF index funds; YTM ≈ 7.0–7.4% approx. |
| Midcap 150 ETFs (Nippon, Motilal, ICICI, Mirae) | Midcap 150 TRI | 2,500–3,500 (Nippon) | 15–30 | 10–25 | 0.15–0.21 | index funds for ≥ ₹20 Cr |
| Junior BeES / Next 50 ETFs | Nifty Next 50 TRI | 6,927 (Nippon) | 40–80 | 5–15 | 0.17 | ₹5–10 Cr clips; index fund for larger |
| CPSE ETF | Nifty CPSE TRI | 27,874 | 100–200 | 5–10 | 0.05 | not core |
| Bank ETFs (Kotak, Nippon) | Nifty Bank TRI | 6,342 / ≈ 8,000 | 50–150 | 3–10 | 0.15–0.19 | tactical only |
| MON100 / MAFANG | Nasdaq-100 / FANG+ (USD) | ≈ 10,000 / ≈ 3,000 | 50–100 / 20–50 | 20–200 (premium episodes 5–15% in 2022–24) | 0.5–0.6 | buy only at ≤ 1% premium to iNAV |
| Motilal Oswal S&P 500 Index Fund | S&P 500 TR (USD) | 5,000–6,000 | NAV-based | — | ≈ 0.5 direct | NAV route for ≥ ₹25 Cr, subject to overseas-cap windows |
| Nifty 50 constituents (direct) | Nifty 50 | — | 30,000–40,000 cash ADV | 3–8 bps for ₹5–25 Cr per stock | brokerage 1–5 bps + STT 0.1% + stamp 0.015% | ₹100 Cr basket ≈ 0.3% of ADV; slice over 3–5 days |

Execution budget for the initial build (approx.): ₹175 Cr Nifty exposure over 5 sessions ≈ 8–12 bps (₹14–21 lakh); gold ₹25 Cr via GOLDBEES/creation at 2–5 bps; a monthly rebalance of ₹10–15 Cr costs ≈ 5–10 bps of traded value ≈ 1–3 bps of NAV — smaller than a one-day consent delay on 10% of NAV at a 1% move (10 bps), which is the design point for standing instructions.

---

## Appendix B: Sources (URLs)

Regulatory and market-structure
- [S1] SEBI (Portfolio Managers) Regulations, 2020, consolidated (last amended 10-Feb-2025): https://www.sebi.gov.in/legal/regulations/feb-2025/securities-and-exchange-board-of-india-portfolio-managers-regulations-2020-last-amended-on-february-10-2025-_92413.html ; Regulation 31 text: https://indiankanoon.org/doc/31059892/ ; Regulation 30 (custodian) via https://indiankanoon.org/doc/65782188/ and https://www.amsshardul.com/insight/sebi-portfolio-managers-regulations-2020/
- [S2] SEBI circular SEBI/HO/IMD/DF1/CIR/P/2020/26 (13-Feb-2020) — fees, expenses, exit load, unlisted 25% for non-discretionary, direct plans: https://www.sebi.gov.in/sebi_data/attachdocs/feb-2020/1581606214719.pdf ; summaries https://vinodkothari.com/2020/02/sebi-brings-in-revised-norms-for-portfolio-managers/ ; https://taxguru.in/sebi/sebi-notifies-compliance-ensured-portfolio-managers.html
- [S3] SEBI Master Circular for Portfolio Managers, 16-Jul-2025: https://www.sebi.gov.in/legal/master-circulars/jul-2025/master-circular-for-portfolio-managers_95347.html ; APMI mirror https://www.apmiindia.org/storagebox/images/Circulars/Master%20Circular%20for%20Portfolio%20Managers%20-%2016th%20July'25.pdf
- [S4] SEBI circular SEBI/HO/IMD/IMD-I/DOF1/P/CIR/2022/112 (26-Aug-2022) — associate/related-party limits and Annexure A consent: https://www.apmiindia.org/storagebox/images/Circulars/Related-Party-Circular-26thAug'22.pdf ; https://www.taxmann.com/post/blog/portfolio-managers-can-invest-up-to-30-of-clients-portfolio-in-securities-of-their-own-associates-sebi/
- [S5] SEBI circular on PMS for accredited investors (21-Dec-2021): https://compfie.aparajitha.com/circular-on-portfolio-management-services-for-accredited-investors-dated-21-12-2021-sebi/ ; https://taxguru.in/sebi/portfolio-management-services-accredited-investors.html
- [S6] SEBI Board memorandum, PMS amendments (Oct-2021): https://www.sebi.gov.in/sebi_data/meetingfiles/oct-2021/1633416546235_1.pdf
- [S7] SEBI Board memo on accredited investors (Sep-2025): https://www.sebi.gov.in/sebi_data/meetingfiles/sep-2025/1758513313676_1.pdf ; Jan-2026 net-worth certificate change: https://www.harunraaj.com/blog/net-worth-certificate-sebi-accredited-investor-january-2026
- [S8] SEBI digital-onboarding / MITC circular SEBI/HO/IMD/IMD-PoD-1/P/CIR/2024/35: https://www.apmiindia.org/storagebox/images/Circulars/Facilitating%20ease%20in%20digital%20on-boarding%20process%20for%20clients%20and%20enhancing%20transparency%20-%202nd%20May'24.pdf
- [S9] SEBI circular SEBI/HO/IMD/IMD-PoD-2/P/CIR/2022/172 (16-Dec-2022) — performance benchmarking, TWRR, XIRR: https://www.apmiindia.org/storagebox/images/Circulars/Performance-Benchmarking-16th-Dec'22.pdf ; https://taxguru.in/sebi/performance-benchmarking-reporting-performance-portfolio-managers.html ; APMI Circular 2 benchmarking: https://www.apmiindia.org/storagebox/images/Circulars/APMI-Circular-2-BENCHMARKING.pdf ; APMI IA portal: https://www.apmiindia.org/apmi/welcomeiaperformance.htm
- [S10] SEBI circular SEBI/HO/IMD/IMD-PoD-1/P/CIR/2023/133 — firm-level performance audit: https://compfie.aparajitha.com/circular-on-audit-of-firm-level-performance-data-of-portfolio-managers-dated-02-08-2023-sebi/
- [S10b] SEBI ETF direct-with-AMC ₹25 Cr threshold (circular 2022/145): https://www.business-standard.com/amp/india-news/after-two-deferments-exchange-route-compulsory-for-sub-rs-25-cr-etf-deals-123050100756_1.html
- [S11] SEBI consultation paper, comprehensive review of PMS Regulations (23-Jul-2026): https://taxguru.in/sebi/sebi-invites-comments-comprehensive-review-portfolio-managers-regulations-2026.html ; https://corporate.cyrilamarchandblogs.com/2026/08/sebis-proposed-overhaul-of-the-pms-regulatory-framework/ ; https://informistmedia.com/MoneyWire/55628/Consultation-Paper-SEBI-issues-consultation-paper-on-comprehensive-review-of-PMS-norms
- [S12] SEBI order, First Global Finance (26-May-2026): https://www.sebi.gov.in/sebi_data/attachdocs/may-2026/1779810509185.pdf ; https://www.moneylife.in/article/sebi-slaps-42-lakh-fine-on-first-global-finance-for-outsourcing-core-pms-functions-and-decisions-bars-from-taking-new-clients-for-21-days/80583.html ; https://corporate.cyrilamarchandblogs.com/2026/06/sebi-order-penalises-outsourcing-of-core-functions-structuring-lessons-for-asset-management-industry/
- [S13] Block-deal framework 2026: https://www.angelone.in/news/market-updates/sebi-tightens-block-deal-rules-raises-minimum-trade-size-to-25-crore ; https://www.taxmann.com/post/blog/sebi-revises-block-deal-framework-minimum-order-size-rs-25-crore
- [S14] Settlement, bulk deals, RFQ, NDS-OM: https://moneylife.in/article/sebi-introduces-optional-t0-settlement-for-top500-stocks/75841.html ; https://www.nseclearing.in/clearing-settlement/corporate-bond/settlement-schedule ; https://www.business-standard.com/amp/markets/news/rbi-opens-nds-om-platform-for-stock-brokers-to-boost-retail-participation-125020701711_1.html ; https://www.equityresearchindia.com/post/block-deals-and-bulk-deals-why-big-institutional-trades-move-sentiment
- [S26] PMS 10% RFQ mandate: https://www.business-standard.com/amp/article/markets/pms-to-undertake-10-transactions-in-corp-bonds-via-rfq-platform-sebi-121120901140_1.html
- [S31] Regulation 31 / PMS Regs summaries: https://taxguru.in/sebi/sebi-portfolio-managers-regulations-2020.html ; https://www.mondaq.com/securities/978948/sebi-portfolio-managers-regulation-2020 ; https://cskruti.com/reporting-by-sebi-registered-portfolio-managers/
- [S32] APMI-empanelled valuation agencies: https://www.lexibox.in/pms/performance-benchmarking-and-reporting-of-performance-by-portfolio-managers/ ; https://aifpms.com/blog/performance-reporting-benchmarking-by-portfolio-manager/
- AIF: CIV framework https://corporate.cyrilamarchandblogs.com/2025/09/beyond-cpms-route-sebi-unlocks-co-investment-schemes-for-aifs/ ; LVF/AI-only schemes Dec-2025 https://www.sebi.gov.in/legal/circulars/dec-2025/modalities-for-migration-to-ai-only-schemes-and-relaxations-to-large-value-funds-for-accredited-investors-under-sebi-alternative-investment-funds-regulations-2012_98244.html ; AIF 2026 guide https://elementone.fund/sebi-aif-regulations-2026-guide/ ; valuation https://treelife.in/finance/aif-valuation-in-india/ ; lock-ins https://steptrade.capital/aif-lock-in-period/
- SIF: https://www.business-standard.com/amp/markets/capital-market-news/sebi-issues-new-regulatory-framework-for-specialized-investment-funds-125022800217_1.html ; https://www.finnovate.in/learn/blog/what-is-specialized-investment-fund-sif-explained ; https://privateclient.cyrilamarchandblogs.com/2025/06/specialized-investment-funds-new-investment-product-of-the-hour/
- MF Regulations 2026 (BER, brokerage caps): https://www.moneylife.in/article/sebi-announces-major-overhaul-of-mutual-fund-rules-effective-april-2026/79422.html ; https://upstox.com/news/personal-finance/mutual-funds/sebi-mutual-funds-regulations-2026-highlights-lower-expense-ratios-revised-brokerage-limits/article-186377/ ; exit-load report https://www.businesstoday.in/mutual-funds/story/exiting-mutual-funds-may-get-cheaper-as-sebi-cuts-maximum-exit-load-cap-to-3-547787-2026-08-07
- MF overseas cap: https://mfreturns.com/blog/why-international-mutual-funds-closed-sebi-cap-2026/ ; https://www.oquilia.com/news/sebi-international-fund-overseas-investment-limit-7bn
- MF cut-offs: https://www.indmoney.com/blog/mutual-funds/sebi-new-mutual-fund-cut-off-timings-explained
- Custodian rule background: https://www.anandrathipms.com/blog/role-of-custodian-in-pms.php

Tax and FEMA
- Capital gains FY2026-27 / IT Act 2025: https://finlecture.in/indian-tax-system/capital-gains-tax-fy-2026-27/ ; https://taxguru.in/income-tax/capital-gains-income-tax-act-2025-tax-period-2026-27.html ; https://www.bajajfinserv.in/investments/understanding-long-term-capital-gains-tax ; https://taxgarden.in/blog/capital-gains-tax-rates-asset-class-ready-reckoner-india-ay-2026-27 ; https://tax2win.in/guide/section-112a-income-tax-ltcg-exemption
- s.50AA / ETF taxation: https://taxguru.in/income-tax/amendment-specified-mutual-fund-definition-section-50aa-budget-2024.html ; https://www.finnovate.in/learn/blog/etf-taxation-india
- REIT/InvIT: https://upstox.com/news/personal-finance/tax/reit-in-vit-dividend-income-what-is-tax-free-under-the-taxation-and-other-laws-amendment-bill-2026/article-198414/ ; https://taxgarden.in/blog/reit-invit-taxation-india-ay-2026-27-section-115ua-distributions-capital-gains
- AIF taxation: https://www.finnovate.in/learn/blog/aif-taxation-india ; https://www.lexology.com/library/detail.aspx?g=a8345261-0ec2-4031-b2e1-211c964e83cd ; https://treelife.in/taxation/category-iii-aif-taxation-in-india/
- STT incl. Budget 2026 F&O hike: https://cleartax.in/s/securities-transaction-tax-stt ; https://upstox.com/news/personal-finance/tax/explained-how-the-stt-hike-on-equity-futures-and-options-affects-traders-and-investors/article-189260/ ; stamp duty https://groww.in/help/stocks,-f&o,-ipo-&-mtf/sx-pricing/what-is-stamp-duty
- SGB Budget 2026: https://www.caalley.com/news-updates/budget-2026/budget-2026-changes-sgb-tax-rules-ends-blanket-capital-gains-exemption ; https://goldenpi.com/blog/bond-news/sovereign-gold-bond-scheme-discontinued-for-new-issues/
- FIFO (s.45(2A), Circular 768): https://www.incometaxindia.gov.in/w/768-circular-no.-768-dated-24-6-1998-1 ; https://taxguru.in/income-tax/fifo-wins-cherry-picked-shares-mumbai-itat-calls-selective-share-identification-colourable-device-tax-avoidance.html
- Loss set-off, dividend stripping: https://cleartax.in/s/set-off-carry-forward-capital-losses ; https://learn.quicko.com/dividend-stripping-section-94-7-income-tax-act
- PMS fee deductibility: https://bcajonline.org/journal/allowability-of-portfolio-management-fees-in-computing-capital-gains/
- Transmission of securities nominee → legal heir (SEBI circular 19-Sep-2025, TLH code): https://moneylife.in/article/sebi-simplifies-transferring-securities-from-nominee-to-legal-heir/78346.html ; https://www.lexology.com/library/detail.aspx?g=336f36ba-2998-473f-a2db-50f519900d72
- NRI PMS / FEMA (PIS, NRE/NRO, NRO repatriation ≤ USD 1 mn/FY): https://www.nobroker.in/nri/guides/pms-for-nri/ ; https://www.wrightresearch.in/blog/pms-for-nri-hni-india/ ; https://www.kalviroventures.com/pms-for-nris/
- Surcharge caps: https://cleartax.in/s/marginal-relief-surcharge ; https://www.taxmann.com/post/blog/tax-rates-surcharge-cess
- LRS/TCS: https://cleartax.in/s/tax-on-foreign-remittance ; https://www.swatikandco.com/tcs_foreign_remittance_2026_27.html ; OI Rules 2022: https://rbidocs.rbi.org.in/rdocs/notification/PDFs/NT110B29188F1C4624C75808B53ADE5175A88.PDF ; GIFT City routes: https://www.valueresearchonline.com/stories/226923/indians-get-new-route-worlds-markets-gift-city/

Market data
- Nifty 50 close 11-Sep-2026: https://www.5paisa.com/blog/post-market-update-us-futures-gain-nifty-sensex-lower-bank-nifty-gains-september-11-2026
- India VIX, 10Y, USD/INR, Brent (11-Sep-2026): https://hdfcsky.com/news/india-vix-rises-4-66percent-to-12-42-as-oil-rupee-and-global-yields-pressure-indian-markets-september-11-2026 ; VIX range https://trendlyne.com/equity/178701/NIFTYVIX/india-vix/
- Nifty P/E: https://indexpe.in/nifty-50 ; https://trendlyne.com/equity/PE/NIFTY/1887/nifty-50-price-to-earning-ratios/ ; Value 50 P/E https://indexpe.in/nifty500-value-50
- Nifty vs peak, Midcap recovery: https://www.business-standard.com/finance/personal-finance/nifty-50-needs-8-rebound-to-reclaim-peak-but-midcaps-are-almost-back-126081200474_1.html
- Repo: https://cleartax.in/s/repo-rate ; RBI Aug-2026 policy https://www.finnovate.in/learn/blog/rbi-august-2026-policy-repo-rate-rupee-inflation
- Gold/silver: https://startuptalky.com/news/gold-silver-prices-today-india-11-september-2026-both-metals-slip/ ; https://cleartax.in/s/gold-history-in-india
- 10Y yield: https://tradingeconomics.com/india/government-bond-yield ; credit spreads: https://indiamacroindicators.co.in/economic-indicators/10-year-credit-spread-aaa-rated-bonds-g-sec ; https://bondscanner.com/blog/corporate-bond-interest-rates-india-2026
- Nifty 50 TRI history: https://www.bajajamc.com/knowledge-centre/nifty-50-historical-returns ; https://www.finnovate.in/learn/blog/nifty-20-year-cagr-below-10-percent-history ; cap indices: https://personalfinanceplan.in/nifty-50-vs-midcap-150-vs-smallcap-250-vs-nifty-500-cap-based-indices-performance-comparison-2005-2026/ ; https://inthemoneybyzerodha.substack.com/p/nifty-500-midcap-150-smallcap-250
- Drawdowns: https://www.wrightresearch.in/blog/what-history-tells-us-about-indian-stock-market-corrections/ ; https://moneyvesta.com/nifty-50-drawdowns-and-recoveries/
- Nifty 50 Arbitrage Index: https://www.niftyindices.com/Factsheet/Factsheet_Nifty_50_Arbitrage_Index.pdf ; Nifty Multi Asset 50:20:20:10: https://www.niftyindices.com/indices/multi-asset/multi-asset-indices/nifty-multi-asset-equity-debt-arbitrage-reits-invits-(50-20-20-10) ; REITs & InvITs index: https://www.niftyindices.com/Factsheet/Factsheet_REITs_InvITs.pdf ; factor factsheets: https://www.niftyindices.com/Factsheet/Factsheet_Nifty200_Momentum30.pdf ; https://www.niftyindices.com/Factsheet/Nifty100_LowVolatility30.pdf ; https://www.niftyindices.com/Factsheet/Factsheet_NIFTY200_Quality30.pdf ; https://www.niftyindices.com/Factsheet/FactsheetNIFTY500Value50.pdf
- CRISIL indices: https://www.crisil.com/en/home/what-we-do/financial-products/indices/historical-factsheets.Indian.Composite-Indices.CRISIL-Composite-Bond-Fund-Index.html
- S&P 500 in INR: https://www.motilaloswalmf.com/mutual-funds/motilal-oswal-s-and-p-500-index-fund ; https://www.slickcharts.com/sp500/returns ; India–US correlation: https://www.spglobal.com/spdji/en/documents/research/research-from-zero-to-hero-the-indian-case-for-global-equity-diversification.pdf
- ETFs: NSE impact cost https://www.nseindia.com/static/products-services/indices-nifty50-index ; ETF industry https://www.businesstoday.in/personal-finance/investment/story/can-gold-etfs-sustain-record-inflows-after-aum-surged-191-in-fy26-528200-2026-04-30 ; Nifty BeES https://mf.nipponindiaim.com/FundsAndPerformance/ProductNotes/NipponIndia-ETF-Nifty-BeES.pdf ; https://cafemutual.com/news/passives/27947-meet-the-etfs-with-highest-aum ; gold ETF AUM https://www.equityresearchindia.com/post/gold-fund-and-gold-etf-aum-trends-amid-recent-gold-price-volatility-july-2026
- FPI flows: https://www.fpi.nsdl.co.in/Reports/Yearwise.aspx?RptType=6 ; https://www.multibagg.ai/market-pulse/articles/fii-fpi-india-2026-flows-cmoihcj2us18tp30j229mjvsc
- Private credit: https://www.ey.com/en_in/insights/strategy-transactions/onwards-and-upwards-a-positive-outlook-for-private-credit-in-india ; https://rurashfin.com/india-private-credit-market-2026-investor-risks/
- Nifty lot size 65 (Jan-2026): https://www.venturasecurities.com/blog/nifty-bank-nifty-lot-size-changes-january-2026-know-how-it-impacts-traders/
- Nifty BeES AUM ₹66,777.21 Cr (9-Sep-2026): https://www.tickertape.in/etfs/nippon-india-nifty-50-bees-etf-NBES
- USD/INR forward premia curve (12M ≈ 2.82% annualised, 10-Jul-2026 print; live from CCIL): https://capera.co/data/India/usdinr-forwards ; https://www.ccilindia.com/client-usd-inr-forwards
- AAA/AA/A spreads over G-sec 2026 (AAA 50–140 bp, AA 100–260 bp): https://altifi.ai/blogs/bonds/aaa-vs-aa-vs-a-spreads ; https://bondscanner.com/blog/corporate-bond-interest-rates-india-2026 ; AA spread series: https://indiamacroindicators.co.in/economic-indicators/aa-rated-bonds-yield-spread-1-year-5-year

Methodology
- GIPS 2020: https://www.pwc.ch/en/publications/2020/PwC-GIPS-2020.pdf ; https://www.gipsstandards.org/wp-content/uploads/2021/03/calculation_methodology_gs_2011.pdf

Internal inputs consolidated: design_regulatory / allocation / rebalancing / risk / performance / selection / operations (.md/.json), data_market, data_facts, critique_compliance / cio / quant / ops, completeness.md, sel/tco.json, blueprint_data.json v1.1 (canonical data pack; v1.0 retained as blueprint_data_v1_backup.json) — all in the ndpms scratchpad folder.
