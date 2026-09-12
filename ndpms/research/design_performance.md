# Performance Measurement, Attribution, Reporting & Return Accountability — ₹500 Cr NDPMS Mandate (Ionic Wealth)

Design date: 2026-09-12. Market context used for calibration: Nifty 50 closed 23,398.10 on 11-Sep-2026 [24]; RBI repo 5.25% (held 5-Aug-2026, SDF 5.00%, MSF 5.50%, stance neutral, FY27 CPI forecast 5.0%) [25][26]; 10Y G-sec approx. 6.97–7.00% in early Sep-2026 [27]. Risk-free rate for ratio metrics: 91-day T-bill, approx. 5.3% (not verified this run — use the RBI/CCIL daily cut-off in production).

## 0. Design principles and regulatory anchors

1. **One engine, many views.** A single daily-valued, transaction-level TWRR engine produces every number in every report (SEBI/APMI filings, client packs, IC scorecards). No spreadsheet forks.
2. **Regulatory floor = SEBI circular SEBI/HO/IMD/IMD-PoD-2/P/CIR/2022/172 (16-Dec-2022, effective 1-Apr-2023)** [1][2]: TWRR is the basis for Investment Approach (IA) performance; XIRR must be presented to each investor along with min/max/median XIRR across all investors in the IA; every IA is tagged to exactly one Strategy (Equity / Debt / Hybrid / Multi Asset); APMI prescribes up to 3 benchmarks per Strategy; a benchmark change requires an exit-load-free exit option and the old track record continues to be reported; marketing/communication must show relative performance vs the selected benchmark and vs other PMs in the Strategy; monthly report to SEBI and APMI within 7 working days of month-end; valuation of debt/money-market per MF norms using APMI-empanelled valuation agencies [1][2][3]. Monthly SEBI/APMI TWRR periods: 1M, 3M, 6M, 1Y, 2Y, 3Y, 4Y, 5Y and since inception [6]. APMI has a standardised ToR for firm-level performance-data audit [5]. Master Circular for Portfolio Managers dated 16-Jul-2025 consolidates these [3] (text not fetched this run — verify paragraph numbers there).
3. **Client reporting floor = PMS Regulations 2020, Regulation 22** [7][8][33]: periodic report to the client at an interval not exceeding 3 months (confirmed — Reg. 22 tightened this from the prior 6-month cycle), covering portfolio composition and value, transactions, beneficial interest received, expenses, risks, defaults/downgrades in debt, distributor commission. Fee/expense rules from SEBI circular SEBI/HO/IMD/DF1/CIR/P/2020/26 (13-Feb-2020, effective 1-Oct-2020): operating expenses ex-brokerage ≤ 0.50% p.a. of average daily AUM (confirmed), exit load ≤ 3%/2%/1% in years 1/2/3 with no exit load after year 3 (confirmed), no upfront fees, performance fee only above high-water mark (confirmed) [10][11][33].
4. **NDPMS specifics.** Non-discretionary/advisory PMs may invest up to 25% of AUM in unlisted securities [9]. Every rebalance needs consent, so *the time between IC decision and execution is a measured, budgeted, attributed cost*. SEBI's 23-Jul-2026 consultation paper (comments closed 13-Aug-2026) proposes overseas investing, pre-IPO/unlisted debt for discretionary PMs, an MF-PMS category and derivative flexibility — proposals only; design for today's rules and keep the benchmark map extensible [12][13].
5. **GIPS 2020 as the quality bar (not a certification claim):** value at least monthly and at every large external cash flow, geometrically link sub-period returns, do not annualise periods < 1 year [14][15]. We exceed the bar with daily valuation.

Feasibility tags used below: **allowed / allowed_with_consent / restricted / not_allowed / unclear_verify**; recommendation tags **MUST / SHOULD / COULD / AVOID**.

## 1. Return computation

### 1.1 Return-series hierarchy (Table 1)

| # | Series | Definition | Costs deducted | Used for | Cadence |
|---|---|---|---|---|---|
| R0 | Paper / model return | Return of the IC-approved model executed at decision-date closing prices | None | Consent-latency and implementation attribution | Daily |
| R1 | Gross-of-fees TWRR | Actual portfolio at executed fill prices (bid-ask/market impact embedded in the fill, not a separate booked line); MF/ETF TER embedded in NAV | Market impact (bid-ask) + embedded TER only — no PM fee/opex/brokerage booked yet | Attribution vs benchmark; IC scorecard | Daily |
| R2 | Net-of-fees TWRR | R1 minus PM fixed fee, GST on fee, custody/FA/audit/RTA operating expenses (≤ 0.50% cap [10]), and booked brokerage/STT/stamp duty/exchange charges (the explicit contract-note lines, distinct from the bid-ask/impact already inside R1) | All booked fees & expenses (PM fee + GST + opex + brokerage/STT/stamp/exchange) | SEBI/APMI reporting; client headline; alpha accountability | Daily |
| R3 | Post-tax realised TWRR | R2 minus taxes actually paid from the portfolio (STCG/LTCG on realised gains, tax on dividends/interest at slab or TDS) | Fees + cash taxes | Client "money in pocket"; tax-drag attribution | Daily (tax accrued on realisation) |
| R4 | Post-tax liquidation NAV | R3 basis, additionally marking a deferred-tax liability (DTL) on unrealised gains at applicable rates + surcharge + cess | Fees + cash taxes + DTL | Fair comparison across sleeves with different turnover; exit-value planning | Daily |
| X1 | Client XIRR (MWRR) | IRR of all client cash flows and terminal value | Net of fees (state basis) | Mandatory client statement with min/max/median across IA investors [1] | Monthly & quarterly |

Decision rule: **alpha is judged on R2 vs the Policy Composite; tax efficiency is judged on (R2 − R3) and (R2 − R4) vs a tax-drag budget; implementation is judged on (R0 − R1).**

### 1.2 Daily TWRR engine

Sub-period (daily) return with external cash flow CF_t:

r_t = (V_t − V_{t−1} − CF_t) / (V_{t−1} + w·CF_t), with w = 1 if funds/securities are received before 09:15 IST (start-of-day convention), w = 0 if after 15:30 IST (end-of-day convention). Cash flows received intraday default to start-of-day (conservative for inflows). Worked: V_{t−1} = ₹500.00 Cr, CF = +₹25.00 Cr, V_t = ₹527.10 Cr → r = 0.4000% (start-of-day) vs 0.4200% (end-of-day); the 2 bp difference on one day is why the convention is fixed in policy and not chosen ex post.

Chain-linking: TWRR_{0,N} = Π_{t=1..N}(1 + r_t) − 1. Annualise only if N ≥ 365 calendar days: (1 + TWRR)^{365/N} − 1 [15]. Periods < 1 year are reported as absolute (matches SEBI/APMI convention for 1M/3M/6M [6]; verify wording in [3]).

Contributions: sleeve i daily contribution c_{i,t} = w_{i,t−1} · r_{i,t}, where w uses start-of-day market values after cash-flow adjustment; Σ_i c_{i,t} = r_t (cash and accruals are a sleeve). Link contributions across days with the Carino factor (Section 3.1) so they sum to the period TWRR.

Accruals: bond coupon accrues daily (dirty price); dividends accrue on ex-date at gross (pre-TDS) amount in R1/R2 and net in R3; MF IDCW likewise. Fees accrue daily (fixed fee = rate/365 × V_t) and are debited on the billing date as a negative CF for R1 and as an expense for R2 (so R1 is truly gross).

Large cash flows: any external flow ≥ 2% of AUM (₹10 Cr) triggers a mandatory revaluation and a same-day break in the composite; the ₹500 Cr deployment period (first 8–12 weekly tranches) is reported both as a fully-invested TWRR and as an "as-deployed" TWRR with a cash-drag line.

IA aggregation for SEBI/APMI: if the mandate is one IA with several family accounts, IA TWRR is the daily asset-weighted aggregate of all accounts (pool the balance sheet, then apply the formula) — not the average of account TWRRs.

### 1.3 XIRR (money-weighted) client view

XIRR solves Σ CF_k /(1 + IRR)^{d_k/365} = 0 including terminal value. Under the ₹500 Cr staggered deployment, XIRR and TWRR will diverge materially. Worked: ₹250 Cr on day 0, ₹250 Cr at month 6; portfolio +8.0% in H1, −3.0% in H2 → TWRR = 4.76%, XIRR = 1.17%, terminal ₹504.40 Cr. Report both, always with a one-line reconciliation ("timing of your contributions cost/added X% vs the strategy return"). Report the min/median/max XIRR across the IA's investors as required [1]; if the mandate is the only investor in the IA, disclose that fact.

### 1.4 Valuation, timing and corporate-action policy (Table 2)

| Instrument | Price source & timing | Lag policy | Stale/haircut rule | Attribution treatment |
|---|---|---|---|---|
| Listed equity, ETFs, REITs/InvITs | NSE close (BSE if NSE-only-illiquid), T+0 | None | No trade for 30 days → last close with 5% haircut in R4 only | Direct-equity sleeve: factor + security attribution |
| Index / active MFs | AMFI-declared NAV of T (published night of T) | Purchases valued at cost until units allotted at realisation-day NAV (SEBI cir. SEBI/HO/IMD/DF2/CIR/P/2020/253) [16] | N/A | Manager selection vs sleeve benchmark; monthly holdings look-through |
| International FoFs / feeder ETFs | NAV declared on T+1 (underlying closes after IST) | Use latest available NAV; flag 1-day lag; no estimated NAVs | N/A | Local-market + INR/USD decomposition (Section 3.4) |
| G-sec / SDL / corporate bonds | APMI-empanelled valuation agency prices (MF-equivalent norms) [2][3]; accrued interest daily | None | Downgrade to default → per MF norms; disclose in quarterly report | Duration / credit / carry split (optional Campisi) |
| Debt MFs / target-maturity / arbitrage MFs | AMFI NAV T (liquid/overnight cut-offs 1:30 pm buy, 3:00 pm redeem [16]) | None | N/A | Cash sleeve vs Nifty 50 Arbitrage Index |
| AIF Cat III (open-ended) | Fund NAV, monthly at minimum [17] | Roll-forward: last NAV ± calls/distributions until new NAV; book revaluation on receipt date, no restatement | NAV > 100 days old → stale flag; > 180 days → 5% haircut in R4 | Manager selection vs domestic-equity benchmark, lagged one month |
| AIF Cat I / II | Independent valuation at least every 6 months (12 months if 75% of investors approve) [17]; 2026 SEBI rules on NAV reporting to depositories evolving [18] | Same roll-forward; uncalled commitment stays in the Cash/Liquid sleeve | NAV > 200 days → stale flag; unrealised marks haircut 10% in R4 | Reported separately: IRR, TVPI, DPI and Public-Market-Equivalent vs Nifty 500 TRI (Kaplan-Schoar PME) |
| Third-party PMS | Custodian-reported holdings valued at NSE close (look-through), not the manager's statement | None | Reconcile monthly to manager statement; > 0.10% NAV gap escalates | Manager selection vs Nifty 500 TRI |
| Gold / silver ETFs & physical-backed units | NSE close; sanity vs IBJA/LBMA in INR | None | N/A | Commodity sleeve vs domestic gold/silver price |
| Corporate actions | Dividend on ex-date; bonus/split quantity on ex-date; rights valued as entitlement from ex-date; buyback on acceptance; merger on effective date | None | Unmatched CA after T+3 → exception queue | Included in sleeve return; never a separate "income" line in TWRR |

### 1.5 Pre- and post-tax series

Rates used (FY 2026-27; Budget 2026 made no change to capital-gains rates [19][20]): listed equity/equity MF STCG 20% (< 12 months), LTCG 12.5% above ₹1.25 lakh aggregate exemption; debt MFs acquired on/after 1-Apr-2023 taxed at slab regardless of holding under Section 50AA, with the "specified MF" definition narrowed from FY 2025-26 to funds with > 65% in debt; gold ETFs LTCG 12.5% after 12 months, gold FoFs after 24 months [19][20][21]. Other instruments (listed bonds, REIT/InvIT distributions, AIF pass-through vs Cat III fund-level tax, surcharge caps) — apply the client's actual status; approx. until confirmed by the tax adviser.

DTL for R4: DTL_t = Σ_lots max(0, MV − cost) × rate(lot type, holding period) × (1 + surcharge) × (1 + 4% cess). Worked: unrealised gains ₹40 Cr (equity LT), ₹10 Cr (equity ST), ₹6 Cr (debt at 30% slab) with 15% surcharge → DTL ≈ ₹10.5 Cr = 2.1% of AUM. R4 = R3 adjusted for ΔDTL. Tax lots run FIFO per instrument (as required for capital-gains computation) and the engine holds the FY-wise capital-gains statement for the client's ITR (annual deliverable).

## 2. Benchmark architecture

### 2.1 Three tiers

| Tier | Benchmark | Purpose | Who fixes it |
|---|---|---|---|
| T1 Regulatory | One of the APMI-prescribed benchmarks for the Strategy the IA is tagged to (expected: Multi Asset; verify current APMI list [4]) | SEBI/APMI monthly filing, Disclosure Document, marketing peer tables [1] | Compliance; change only with exit-load-free exit offer |
| T2 Policy Composite | Sleeve-weighted composite below, reset monthly | Attribution, alpha accountability, IC scorecard; written into the client agreement as the "mandate benchmark" | IC + client; annual review |
| T3 Reference | (a) Allocate house 80% Nifty 50 TRI + 20% Nifty 50 Arbitrage; (b) APMI Multi Asset peer median; (c) Nifty Multi Asset Equity:Debt:Arbitrage:REITs/InvITs (50:20:20:10) [22] | Context for client conversations; sanity check on T2 | Performance team |

Whether a custom T2 may be shown alongside T1 in client communications is **unclear_verify** with APMI/compliance; T1 must always appear wherever performance is shown [1].

### 2.2 Policy composite (Table 3) — illustrative SAA to be replaced by the SAA layer's final weights

| Sleeve | Policy wt | ₹ Cr at ₹500 Cr | Index (TRI where it exists) | Reset | Note |
|---|---|---|---|---|---|
| Domestic equity (ETF/index 20%, active MF 12%, direct 15%, 3P PMS 5%, Cat III 3%) | 55% | 275.0 | Nifty 500 TRI | Monthly | Broad index chosen so mid/small tilts are TAA, not "selection" |
| International equity (India-listed FoF/ETF) | 7% | 35.0 | S&P 500 TRI in INR (or MSCI ACWI NR INR when the sleeve diversifies) | Monthly | Unhedged; FX is pass-through |
| Fixed income (G-sec/SDL 8%, corporate 8%, debt MF 6%) | 22% | 110.0 | Nifty Composite Debt Index | Monthly | Verify exact index name/series on niftyindices [23] |
| AIF Cat II (private credit / PE) | 4% | 20.0 | Nifty Composite Debt Index + 3.0% p.a. (private credit); Nifty 500 TRI + 3.0% (PE), 1-quarter lag | Quarterly | Absolute-return proxy; PME reported separately |
| REITs / InvITs | 4% | 20.0 | Nifty REITs & InvITs Index (TR) | Monthly | Verify TR variant availability |
| Gold 4% / Silver 1% | 5% | 25.0 | Domestic gold (IBJA/MCX spot) 80% + silver 20% | Monthly | No TRI concept; spot in INR |
| Cash / liquid / arbitrage | 3% | 15.0 | Nifty 50 Arbitrage Index (65% cash-futures arbitrage, 30% 1-month MIBOR, 5% cash; base 1-Apr-2010 = 1000) [22a] | Monthly | Same as house cash proxy |
| **Total** | **100%** | **500.0** | Composite | Monthly reset to policy weights | Bands ±3% per sleeve trigger TAA review |

Computation: within a month the composite is buy-and-hold from month-start policy weights (weights drift with sub-index returns), R_B,t = Σ_i w_{i,t−1} r_{i,t}; on the first business day of each month weights are reset (same convention as NSE hybrid indices, which reset monthly [23a]). Store daily sub-index levels; never back-fill a benchmark with a different series without a footnote and a dated version number.

Expected characteristics (approx., for calibration only): equity beta of the composite ≈ 0.62 × Nifty 500 + 0.04 × REIT beta vs ≈ 0.80 × Nifty 50 for the house 80/20; long-run reference points — Nifty 50 TRI 20-year CAGR 12.44% to 27-Feb-2026 [28]; Nifty 500 TRI 10-year CAGR approx. 14.85% [29]; arbitrage funds approx. 4–5% 1-year [22a]. Consequently the mandate composite should be expected to trail the house benchmark by roughly 1.0–1.5% p.a. in strong equity years and lead in drawdowns; state this in the client agreement so the house 80/20 is never mistaken for the target.

### 2.3 Peer group

APMI publishes IA-level TWRR by Strategy on its portal [6]; use the Multi Asset (or Hybrid) peer set for quartile ranking on 1Y/3Y/5Y. Whether NDPMS IAs are included in the peer tables is **unclear_verify**. Caveats to print with every peer table: survivorship, different cash treatment, and the ₹500 Cr mandate's tax-aware low turnover.

## 3. Attribution

### 3.1 Brinson-Fachler by sleeve, monthly, Carino-linked

Per sleeve i in month t (w = weights, R = returns, B = benchmark, P = portfolio, R_B = total benchmark return):

- Allocation (TAA): A_i = (w_i^P − w_i^B) × (R_i^B − R_B)
- Selection (manager + security): S_i = w_i^B × (R_i^P − R_i^B)
- Interaction: I_i = (w_i^P − w_i^B) × (R_i^P − R_i^B)
- Σ_i (A_i + S_i + I_i) = R_P − R_B exactly for the month.

Linking across months (Carino): k_t = [ln(1+R_P,t) − ln(1+R_B,t)] / (R_P,t − R_B,t); K = [ln(1+R_P) − ln(1+R_B)] / (R_P − R_B); linked effect = Σ_t (k_t / K) × effect_t. Check: two months with (P, B) = (+3.1%, +2.5%) and (−1.8%, −2.2%) → cumulative active 1.00%; linked A = 0.504%, S = 0.495%, I = 0.000%, sum 0.999% (rounding). Use Carino for the client pack; Menchero is acceptable for the IC but pick one and freeze it.

Worked ₹500 Cr full-year example (Table 4; illustrative returns, not forecasts):

| Sleeve | w_B | w_P (avg) | R_B % | R_P % | Allocation % | Selection % | Interaction % | Total % | ₹ Cr |
|---|---|---|---|---|---|---|---|---|---|
| Domestic equity | 55 | 57 | 10.0 | 11.6 | +0.006 | +0.880 | +0.032 | +0.918 | +4.59 |
| International equity | 7 | 6 | 14.0 | 13.2 | −0.043 | −0.056 | +0.008 | −0.091 | −0.45 |
| Fixed income | 22 | 20 | 7.5 | 7.9 | +0.044 | +0.088 | −0.008 | +0.124 | +0.62 |
| AIF Cat II | 4 | 3 | 10.5 | 11.0 | −0.008 | +0.020 | −0.005 | +0.007 | +0.04 |
| REITs/InvITs | 4 | 4 | 9.0 | 9.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.00 |
| Gold/Silver | 5 | 5 | 12.0 | 11.8 | 0.000 | −0.010 | 0.000 | −0.010 | −0.05 |
| Cash/Arbitrage | 3 | 5 | 6.5 | 6.4 | −0.064 | −0.003 | −0.002 | −0.069 | −0.35 |
| **Total** | 100 | 100 | **9.705** | **10.584** | **−0.065** | **+0.919** | **+0.025** | **+0.879** | **+4.40** |

Reading: gross active +88 bps (₹4.40 Cr) came almost entirely from selection inside domestic equity; TAA was a small negative (2% excess cash cost 6 bps).

### 3.2 Selection with look-through

Split S_domestic (+0.880%) into: direct equity vs Nifty 500 TRI (+0.46%), active MFs vs their SEBI-category TRI then vs Nifty 500 (+0.26%), third-party PMS (+0.12%), Cat III AIF lagged (+0.06%), ETF/index tracking difference (−0.02%). For MFs and Cat III AIFs, load monthly disclosed holdings (AMFI monthly portfolios; AIF quarterly holdings where provided) and compute holdings-based sector and factor exposures so "manager selection" can be further split into the manager's style tilt vs its stock picking (returns-based fallback: 36-month regression). Third-party PMS is valued and attributed on custodian holdings, so it is analysed exactly like the direct sleeve.

### 3.3 Factor attribution — direct-equity sleeve (₹75 Cr, NIFTY-750 scorecard)

Holdings-based (monthly): active exposure to factor k, x_k = Σ_j (w_j^P − w_j^B) z_{j,k} using the scorecard z-scores (quality, growth, value, momentum, macro-sensitivity) plus size and beta; factor return F_k from long-short index proxies: size = Nifty Midsmallcap 400 TRI − Nifty 100 TRI; value = Nifty 500 Value 50 TRI − Nifty 500 TRI; momentum = Nifty 500 Momentum 50 TRI − Nifty 500 TRI; quality = Nifty 200 Quality 30 TRI − Nifty 200 TRI; low-vol = Nifty 100 Low Volatility 30 TRI − Nifty 100 TRI (index names approx. — confirm availability of daily TRI series). Active return = Σ_k x_k F_k (factor) + specific (residual). Returns-based cross-check: regress 36 monthly active returns on the same factor spreads; report R², t-stats, and the residual alpha with its standard error. Decision rule: if > 60% of the sleeve's 12-month active return is explained by size/momentum, the IC classifies it as a *style bet (TAA)* and moves it to the allocation line in the scorecard.

### 3.4 Currency attribution — international sleeve (₹35 Cr)

INR return of a foreign asset: (1 + R_INR) = (1 + R_local)(1 + R_FX). Currency effect = R_FX + R_local × R_FX; local effect = R_local. Because PMS cannot hedge INR exposure via currency derivatives at present (restricted; verify under the 2026 proposals [12]) the currency line is a pass-through, but it must be shown so the IC is not credited/blamed for INR moves. Worked: 7% sleeve, USD/INR +3.0% in the year → +0.21% of portfolio return is FX, not manager skill; if the benchmark is also unhedged INR the effect nets to ≈ 0 in Brinson terms and appears only in the contribution view.

### 3.5 Cost and tax drag budget (Table 5; bps of average AUM p.a., ₹ Cr on ₹500 Cr)

| Line | Budget bps | ₹ Cr | Source of data | Owner | Escalation |
|---|---|---|---|---|---|
| PM fixed fee (assume 0.50%; negotiable for ₹500 Cr NDPMS, typical 0.25–0.75% approx.) | 50 | 2.50 | Fee schedule (Schedule IV agreement) | CIO | n/a |
| GST 18% on PM fee | 9 | 0.45 | Invoice | Finance | n/a |
| Operating expenses (custody, fund accounting, audit, RTA) — regulatory cap 50 bps [10] | 10 | 0.50 | Custodian/FA invoices | COO | > 15 bps |
| Brokerage, STT, stamp, exchange, GST on brokerage (direct sleeve turnover ≤ 40%) | 8 | 0.40 | Contract notes | Dealing | > 12 bps |
| Embedded MF TERs (direct plans mandatory in PMS — verify [3]) and ETF TERs | 25 (approx.; inside R1) | 1.25 | Scheme TER disclosures × weights | Research | > 35 bps |
| Bid-ask / market impact (arrival-price shortfall) | 5 | 0.25 | Execution vs arrival price | Dealing | > 10 bps |
| Consent-latency shortfall (Section 3.6) | 15 | 0.75 | Decision vs execution price | PM + client ops | > 25 bps |
| Cash drag during deployment (year 1 only) | 20 (approx.) | 1.00 | As-deployed vs fully-invested TWRR | PM | n/a |
| Taxes paid from portfolio (R2 − R3) | 45 (approx.; turnover-dependent) | 2.25 | Tax-lot engine | PM + tax adviser | > 70 bps |
| **Total explicit + implicit (ex-TER, ex-cash drag)** | **~97 + 45 tax** | **~4.85 + 2.25** | | | |

Worked (Table 4 year): gross gain ₹52.92 Cr (10.584% = R1, ties to Table 4's R_P); booked fees & expenses ₹3.85 Cr (77 bps = PM fee 50 + GST 9 + opex 10 + booked brokerage/STT/stamp/exchange 8, per the revised Table 1 R1→R2 bridge; bid-ask/impact and TER stay embedded in R1 and are not subtracted again here) → R2 = 9.814%; taxes ₹2.25 Cr (45 bps) → R3 = 9.364%. Policy composite 9.705% → **net alpha (R2 basis, per the decision rule in §1.1) +11 bps (₹0.55 Cr)**. Lesson the IC must internalise: 88 bps gross active is not enough; at 77 bps of fees the target gross active return must be ≥ 150–200 bps p.a. or the fee must fall.

### 3.6 Implementation shortfall and consent-latency attribution (critical for NDPMS)

For each recommended order i with recommended quantity Q_i^rec, executed quantity Q_i^exe, side s_i (+1 buy, −1 sell), decision-date close P_D (IC approval), consent-date close P_C (client consent time-stamp), arrival price P_A (order release to dealer), average fill P_E, and horizon-end price P_H (month-end):

- Consent-latency cost = s_i × (P_C − P_D) × Q_i^exe
- Dealing-delay cost = s_i × (P_A − P_C) × Q_i^exe
- Execution cost (spread + impact) = s_i × (P_E − P_A) × Q_i^exe + explicit charges
- Opportunity cost of unexecuted quantity = s_i × (P_H − P_D) × (Q_i^rec − Q_i^exe)
- Implementation shortfall (Perold) = sum of the four; report in ₹, in bps of AUM and in bps of traded value; also report latency in business days (decision→consent, consent→execution).

Worked (Table 6): monthly rebalance shifting ₹20 Cr from a Nifty 50 ETF to a midcap index fund.

| Step | Date | Business days from decision | Midcap index | Nifty 50 | Effect |
|---|---|---|---|---|---|
| IC decision (P_D) | D | 0 | 100.0 | 100.0 | — |
| Consent pack sent | D+1 | 1 | — | — | — |
| Client consent (P_C) | D+4 | 4 | 101.5 | 100.5 | Consent-latency cost = ₹20 Cr × (1.5% − 0.5%) = ₹0.20 Cr |
| Execution (P_E) | D+5 | 5 | 101.8 | 100.6 | Dealing/impact = ₹20 Cr × (0.3% − 0.1%) = ₹0.04 Cr |
| **Total shortfall** | | | | | **₹0.24 Cr = ₹24 lakh = 4.8 bps of AUM (120 bps of traded value)** |

Annualised: 12 rebalances × 4% turnover × 30 bps average adverse drift = ₹0.72 Cr = 14.4 bps p.a. — the basis of the 15 bps budget. Design levers (all **allowed_with_consent**): pre-agreed model with ±3% sleeve bands and a signed standing instruction to execute band-restoring trades where the agreement permits (**unclear_verify** how far standing instructions can go without becoming discretionary — confirm with compliance under [3]); consent pack released the same evening as IC with a 48-hour SLA; default to index/ETF vehicles for TAA legs (lower drift risk than single stocks); execute in the Thursday deployment tranche already in the house calendar. KPI: median decision→execution ≤ 3 business days; 90th percentile ≤ 6; shortfall ≤ 25 bps p.a.

### 3.7 Full realised-return decomposition (annual waterfall)

R_client(R3) = Policy composite (SAA) + TAA allocation + manager selection + security selection + interaction − fees & expenses − taxes, where the BF effects are computed on R1 (actual executed portfolio, already net of implementation shortfall relative to the R0 paper return — see the decision rule in §1.1: implementation is judged on R0 − R1 separately, not subtracted a second time here). Worked year: 9.705 − 0.065 + 0.440 (MF/PMS/AIF selection) + 0.460 (direct security selection) + 0.019 (other selection incl. FI, gold, intl) + 0.025 = 10.584% (= R1, ties to Table 4's R_P). Memo, not part of the sum above: implementation shortfall of −0.200% (of which −0.15 consent, −0.05 dealing) already sits inside this 10.584%, i.e. the R0 paper return was 10.784% before that shortfall. Continuing: 10.584 − 0.770 (fees & expenses) − 0.450 (taxes) = 9.364% = R3. Every line has a named owner (Table 10).

## 4. Risk-adjusted metrics and targets (Table 7; monthly data, rolling 36 months unless stated; R_f = 91-day T-bill, approx. 5.3%)

| Metric | Formula | Target | Amber | Red | Notes |
|---|---|---|---|---|---|
| Net alpha vs Policy Composite | R2 − R_B, annualised | ≥ +1.0% (3Y), ≥ +1.5% (5Y) | < +0.5% (3Y) | < 0 (3Y) | Primary accountability metric |
| Information ratio | (R2 − R_B) / TE | ≥ 0.40 | 0.20–0.40 | < 0.20 | Ex-post 36M |
| Tracking error (ex-ante & ex-post) | σ(R2 − R_B) × √12 | 2.5–4.5% | 4.5–6.0% | > 6.0% or < 1.5% (closet indexing) | Ex-ante from factor model weekly |
| Sharpe | (R2 − R_f)/σ_P | ≥ benchmark Sharpe + 0.10 | within ±0.10 | < benchmark − 0.10 | Level depends on regime; judge relative |
| Sortino | (R2 − R_f)/downside σ (threshold R_f) | ≥ benchmark + 0.15 | ±0.15 | < benchmark − 0.15 | |
| Max drawdown (peak-to-trough, daily) | min(V_t/peak − 1) | ≤ 1.10 × benchmark MDD | 1.10–1.25× | > 1.25× or > −18% absolute | Tail-risk dashboard owns the absolute limit |
| Calmar | annualised R2 / |MDD| (3Y) | ≥ 0.60 | 0.40–0.60 | < 0.40 | |
| Upside / downside capture | Σ P in up (down) benchmark months / Σ B | UC ≥ 95%, DC ≤ 85% | DC 85–100% | DC > 100% | Asymmetry is the multi-asset value proposition |
| Batting average | % months R2 > R_B | ≥ 55% | 45–55% | < 45% | 36M |
| TAA hit rate | % closed TAA calls with positive payoff vs policy | ≥ 55% over trailing 12 calls | 45–55% | < 45% | Also payoff ratio ≥ 1.2 |
| Active share (direct sleeve) | ½ Σ|w_P − w_B| vs Nifty 500 | 60–80% | 50–60% | < 50% | Avoid paying active fee for beta |
| Consent latency | median business days decision→execution | ≤ 3 | 4–5 | > 5 | Section 3.6 |
| Stale-priced assets | % NAV with price age > policy | ≤ 5% | 5–8% | > 8% | AIF-heavy months |

Red in any primary metric for two consecutive quarters triggers a formal IC review with a written remediation plan; red in net alpha at 3Y triggers a client-facing strategy review.

## 5. Reporting cadence, contents and dashboard

### 5.1 Calendar (Table 8)

| Report | Timing | Audience | Core contents | Regulatory hook |
|---|---|---|---|---|
| Daily NAV flash | T+1 by 10:00 IST | PM, risk, client ops (client on request) | NAV/unit; daily/MTD/FYTD R1, R2 vs T1/T2/T3; sleeve MTD contributions; cash & uncalled commitments; pending consents with age; stale-price %; corporate actions due; band breaches; top 5 movers | Internal |
| Weekly summary | Monday 09:00 | IC, client RM | Week/MTD TWRR vs benchmarks; MTD BF attribution; deployment tranche status; ex-ante TE and factor tilts; drift vs ±3% bands; consent items due this week; next Thursday tranche list | Internal |
| Monthly pack | T+5 business days (before APMI T+7 working-day filing [1]) | Client, IC | Tables: R0–R4 for 1M/3M/6M/1Y/3Y/5Y/SI; XIRR; Brinson-Fachler by sleeve with Carino link; look-through manager table; factor attribution; FX line; cost & tax drag vs budget; consent-latency log (each trade); risk metrics vs targets; holdings; transactions; fees; charts: cumulative R2 vs T1/T2/T3, drawdown, rolling 12M alpha, TE, waterfall | APMI/SEBI monthly filing data lineage |
| Quarterly client report | Within the quarter-end + 30 days (Reg. 22 caps the interval at 3 months, confirmed [7][8][33]) | Client (signed) | Composition & value; transactions; beneficial interest received; expenses; risks foreseen; debt defaults/downgrades; distributor commission; TWRR & XIRR incl. min/median/max across IA investors [1]; relative performance vs T1 and peers; open consent items; tax summary FYTD | PMS Regs 2020; SEBI Dec-2022 circular |
| Annual review | Within 60 days of FY end | Client, IC, Board | Audited performance (APMI ToR [5]); full-year decomposition waterfall; TAA post-mortems; benchmark review; fee reconciliation; FY capital-gains statement (FIFO lots) for ITR; GIPS-style composite report (COULD) | Annual audit of client accounts (verify [3]) |
| Event-driven | Same day | Client, IC | Sleeve breach of ±3% band; MDD > −10%; AIF stale > 200 days; benchmark index reconstitution; regulatory change | Internal |

### 5.2 Performance dashboard specification (Table 9)

| Panel | Metrics | Refresh | Drill-down | Palette |
|---|---|---|---|---|
| Headline | NAV, R1/R2/R3/R4 for 1D/MTD/FYTD/1Y/3Y/SI; XIRR; alpha vs T1/T2/T3 | Daily 10:00 | Series → sleeve → instrument → lot | Navy #16233B text, green #1E9E6A positive, coral #E0402F negative |
| Growth of ₹100 & drawdown | Cumulative R2 vs 3 benchmarks; drawdown; rolling 12M/36M alpha | Daily | Click period → attribution for that window | Indigo #1B27A3 portfolio, navy benchmark, amber #F2A93C reference |
| Attribution | BF allocation/selection/interaction by sleeve (MTD/QTD/FYTD, Carino-linked); look-through manager table; factor bars; FX line | Daily (final at month-end) | Sleeve → manager → holding; factor → stocks driving exposure | Diverging green/coral |
| Implementation & consent | Shortfall ₹/bps per trade; latency histogram; open consents with age; SLA compliance | Daily | Trade → timeline (decision, consent, arrival, fills) | Amber for > 3 days, coral > 5 |
| Costs & taxes | Fee/expense/tax lines vs budget; DTL; FYTD realised gains by bucket; harvest candidates | Daily | Lot level | Neutral greys + amber warnings |
| Risk-adjusted | Table 7 metrics with RAG status; ex-ante TE and factor tilts | Weekly (Fri) | Metric → time series → contributing months | RAG |
| Valuation quality | Stale-price %, unmatched corporate actions, custodian recon breaks, NAV lag by asset | Daily | Asset → source → timestamp | Coral on breaks |
| Peer & regulatory | APMI Strategy peer quartile [6]; filing status (7-working-day clock) | Monthly | IA → period | Navy |

Data lineage requirements: every figure carries its source table, as-of timestamp and benchmark version ID; reproducible by re-running the engine from custodian files; month-end lock after IC sign-off with any restatement logged.

## 6. Accountability model — "owning the returns"

### 6.1 Alpha targets by horizon (net of fees, vs Policy Composite T2)

| Horizon | Target | Tolerance (noise band) | Consequence of miss |
|---|---|---|---|
| 1 year | +1.0% | ±2.0% (TE ≈ 3.5% p.a.; band set inside 1σ by policy, not a statistical 1σ) | Explain; no structural change |
| 3 years rolling | +1.0% p.a., IR ≥ 0.40, DC ≤ 85% | ±0.7% | Red → strategy review with client; fee discussion |
| 5 years | +1.5% p.a. | ±0.5% | Mandate renewal test |
| Peer | Top third of APMI Multi Asset IAs on 3Y | — | Marketing claims constrained |

### 6.2 IC scorecard (Table 10; quarterly, points-based; example from the worked year)

| Component | Owner | Metric | Budget/Target | Worked year | Score (−2…+2) |
|---|---|---|---|---|---|
| SAA / policy portfolio | IC chair | Composite vs client objective (real return ≥ CPI + 4%, approx.) | ≥ 9.0% | 9.705% | +1 |
| TAA | CIO | Allocation effect; hit rate | ≥ +0.20%; ≥ 55% | −0.065%; 50% | −1 |
| Manager selection (MF/PMS/AIF) | Head of Research | Selection effect look-through | ≥ +0.30% | +0.44% | +1 |
| Security selection (direct) | Equity PM | Selection vs Nifty 500 TRI; factor-adjusted residual | ≥ +0.50%; residual > 0 | +0.46% | 0 |
| Implementation & consent | PM + Client Ops | Shortfall; latency | ≤ 25 bps; ≤ 3 days | 20 bps; 3.5 days | 0 |
| Costs | COO | Fees + opex + trading vs budget | ≤ 80 bps | 77 bps | +1 |
| Taxes | PM + tax adviser | R2 − R3; harvest realised | ≤ 50 bps | 45 bps | +1 |
| Valuation & reporting quality | Head of Performance | Stale %, recon breaks, filing on time | ≤ 5%, 0 late | 3%, 0 late | +2 |

Scores feed the team's variable-pay pool (COULD; needs HR design) and are published to the client in the annual review (SHOULD) — publishing the scorecard is the concrete meaning of "owning the returns".

### 6.3 TAA post-mortems

Every TAA call is logged at inception with: thesis, sleeve and size (₹ Cr and % vs policy), horizon, trigger to exit, expected payoff, downside stop. At horizon end: realised payoff vs counterfactual (policy weights) computed by the engine, classified in the decision-quality matrix (good decision/good outcome … bad/bad), latency cost of the call, and a one-paragraph lesson. Quarterly: hit rate, average win/loss, payoff ratio, and correlation of calls with momentum (to detect trend-chasing). Calls smaller than 1% of AUM (₹5 Cr) are not permitted — too small to matter, large enough to cost latency.

## 7. CAN / SHOULD / AVOID summary

- **MUST (regulation or indispensable):** daily TWRR engine with fixed cash-flow convention; XIRR with min/median/max across IA investors; T1 APMI benchmark tagging and monthly filing within 7 working days; MF-norm valuation via APMI-empanelled agencies for debt; quarterly client report with the regulation's contents; net-of-fees reporting; consent-latency log with time-stamps (NDPMS evidence and attribution); benchmark version control.
- **SHOULD (first 6 months):** Policy Composite in client agreement; Brinson-Fachler with Carino; look-through manager attribution; factor attribution for direct sleeve; cost & tax drag budget; R3/R4 post-tax series with DTL; risk-metric RAG dashboard; IC scorecard; TAA post-mortems; pre-agreed bands + standing instruction (after compliance confirms scope).
- **COULD:** GIPS-style composite report and independent verification; PME for AIFs; Campisi fixed-income attribution; SIF sleeve benchmark once a SIF is held (SIF minimum ₹10 lakh at PAN level, effective 1-Apr-2025 [30][31]).
- **AVOID:** daily attribution as a decision input (noise); reporting the house 80/20 as the headline benchmark; annualising < 1-year returns; presenting model/paper returns as performance; performance fees on unrealised AIF marks; changing T1 benchmark without an exit offer; estimating AIF/international NAVs in-house; equal-weighting account TWRRs for the IA.

## 8. Sources

[1] SEBI circular SEBI/HO/IMD/IMD-PoD-2/P/CIR/2022/172 (16-Dec-2022), APMI copy — https://www.apmiindia.org/storagebox/images/Circulars/Performance-Benchmarking-16th-Dec'22.pdf
[2] TaxGuru reproduction of the same circular — https://taxguru.in/sebi/performance-benchmarking-reporting-performance-portfolio-managers.html
[3] Master Circular for Portfolio Managers, 16-Jul-2025 (APMI copy) — https://www.apmiindia.org/storagebox/images/Circulars/Master%20Circular%20for%20Portfolio%20Managers%20-%2016th%20July'25.pdf
[4] APMI revised benchmarks (LexiBox) — https://www.lexibox.in/pms/apmi-revised-benchmarks/
[5] APMI Circular 9, standardised ToR for audit of firm-level performance data — https://www.lexibox.in/pms/standardized-terms-of-reference-tor-for-the-audit-of-firm-level-performance-data/
[6] APMI IA performance portal — https://www.apmiindia.org/apmi/welcomeiaperformance.htm ; summary of monthly reporting periods — https://aifpms.com/blog/performance-reporting-benchmarking-by-portfolio-manager/
[7] SEBI (Portfolio Managers) Regulations, 2020 (as amended 22-Aug-2022) — https://www.sebi.gov.in/legal/regulations/aug-2022/securities-and-exchange-board-of-india-portfolio-managers-regulations-2020-last-amended-on-august-22-2022-_62407.html
[8] SEBI FAQ on Portfolio Managers, 28-Oct-2020 — https://www.sebi.gov.in/sebi_data/faqfiles/oct-2020/1603946323909.pdf
[9] 25% unlisted limit for non-discretionary/advisory (Mondaq summary) — https://www.mondaq.com/securities/978948/sebi-portfolio-managers-regulation-2020
[10] SEBI circular SEBI/HO/IMD/DF1/CIR/P/2020/26 (13-Feb-2020), fees, expenses, exit load — https://www.sebi.gov.in/sebi_data/attachdocs/feb-2020/1581606214719.pdf
[11] Business Standard on the Feb-2020 expense cap — https://www.business-standard.com/amp/article/markets/sebi-puts-expense-cap-on-pms-providers-lays-down-performance-standards-120021301918_1.html
[12] SEBI PMS consultation paper 23-Jul-2026 (Cyril Amarchand Mangaldas) — https://corporate.cyrilamarchandblogs.com/2026/08/sebis-proposed-overhaul-of-the-pms-regulatory-framework/
[13] Same, Conventus Law — https://conventuslaw.com/report/india-sebis-proposed-overhaul-of-the-pms-regulatory-framework/
[14] PwC overview of GIPS 2020 — https://www.pwc.ch/en/publications/2020/PwC-GIPS-2020.pdf
[15] GIPS Guidance Statement on Calculation Methodology — https://www.gipsstandards.org/wp-content/uploads/2021/03/calculation_methodology_gs_2011.pdf
[16] SEBI NAV-on-realisation circular SEBI/HO/IMD/DF2/CIR/P/2020/253 and cut-offs (INDmoney summary) — https://www.indmoney.com/blog/mutual-funds/sebi-new-mutual-fund-cut-off-timings-explained
[17] AIF valuation frequency (Treelife) — https://treelife.in/finance/aif-valuation-in-india/
[18] SEBI AIF NAV reporting rules 2026 (K&S) — https://ksandk.com/newsletter/sebi-aif-nav-reporting-rules-2026-explained/ ; ELP note — https://elplaw.in/leadership/sebi-proposal-mandates-reporting-of-navs-by-aifs-to-depositories/
[19] LTCG/STCG FY 2026-27 (Bajaj Finserv) — https://www.bajajfinserv.in/investments/understanding-long-term-capital-gains-tax
[20] MF taxation 2026 incl. Budget 2026 no-change and Section 50AA (1% Club) — https://www.onepercentclub.io/blog/mutual-fund-taxation-india/
[21] MF taxation AY 2026-27 (Tax Garden) — https://taxgarden.in/blog/mutual-fund-taxation-india-ay-2026-27 ; FY 2025-26 (Finnovate) — https://www.finnovate.in/learn/blog/mutual-fund-taxation-india-fy-2025-26
[22] Nifty Multi Asset (50:20:20:10) index — https://www.niftyindices.com/indices/multi-asset/multi-asset-indices/nifty-multi-asset-equity-debt-arbitrage-reits-invits-(50-20-20-10) ; NSE multi-asset indices page — https://www.nseindia.com/static/products-services/multi-asset-indices
[22a] Nifty 50 Arbitrage Index methodology and factsheet — https://www.niftyindices.com/methodology/method_nifty_50_arbitrage.pdf ; https://www.niftyindices.com/Factsheet/Factsheet_Nifty_50_Arbitrage_Index.pdf
[23] Nifty fixed-income, hybrid and multi-asset methodology — https://www.niftyindices.com/Methodology/Method_NIFTY_Fixed_Income_Indices.pdf ; Composite G-sec factsheet — https://www.niftyindices.com/Factsheet/ind_debt_Nifty_Composite.pdf
[23a] NSE hybrid indices (monthly weight reset) — https://www.nseindia.com/static/products-services/indices-blended
[24] Nifty 50 close 11-Sep-2026 (5paisa) — https://www.5paisa.com/blog/post-market-update-us-futures-gain-nifty-sensex-lower-bank-nifty-gains-september-11-2026
[25] RBI August 2026 policy (Finnovate) — https://www.finnovate.in/learn/blog/rbi-august-2026-policy-repo-rate-rupee-inflation
[26] RBI MPC Aug-2026 (Forbes India live blog) — https://www.forbesindia.com/article/news/rbi-mpc-live-updates-august-2026-repo-rate-sanjay-malhotra-policy-announcement-liveblog/2996705/1 ; IndiaBonds highlights — https://www.indiabonds.com/bonduni/news/august-2026-rbi-monetary-policy-highlights/
[27] India 10Y G-sec yield (Trading Economics) — https://tradingeconomics.com/india/government-bond-yield
[28] Nifty 50 TRI 20-year CAGR 12.44% to 27-Feb-2026 (Finnovate) — https://www.finnovate.in/learn/blog/nifty-20-year-cagr-below-10-percent-history
[29] Nifty 500 TRI 10-year CAGR approx. 14.85% (The Tribune) — https://www.tribuneindia.com/partner-exclusives/nifty-500-historical-performance-returns-analysis/
[30] SEBI SIF framework (Business Standard, 28-Feb-2025) — https://www.business-standard.com/amp/markets/capital-market-news/sebi-issues-new-regulatory-framework-for-specialized-investment-funds-125022800217_1.html
[31] SIF explained 2026 (Finnovate) — https://www.finnovate.in/learn/blog/what-is-specialized-investment-fund-sif-explained ; Cyril Amarchand private-client note — https://privateclient.cyrilamarchandblogs.com/2025/06/specialized-investment-funds-new-investment-product-of-the-hour/
[32] PMS benchmarking norms industry extension request (Business Standard) — https://www.business-standard.com/article/markets/pms-benchmarking-norms-industry-players-seek-three-month-extension-123030101080_1.html
[33] TaxGuru summary of SEBI (Portfolio Managers) Regulations, 2020, Regulation 22 (3-month periodic client report, down from the prior 6-month cycle) — https://taxguru.in/sebi/sebi-portfolio-managers-regulations-2020.html

Verification note: this run additionally confirmed via live search (12-Sep-2026) three load-bearing claims previously flagged as unverified: (i) PMS Regulations 2020 Regulation 22's 3-month client-reporting ceiling [33]; (ii) SEBI circular SEBI/HO/IMD/DF1/CIR/P/2020/26's 0.50% p.a. ex-brokerage operating-expense cap, the 3%/2%/1% exit-load schedule, and the high-water-mark performance-fee rule [10][11]. Primary documents [1][3][7][8] were identified through search results but their full text could not be fetched in this run (network egress restrictions); statements attributed to them beyond the confirmed items above reflect search excerpts and should be re-read against the documents before the operating model is finalised. All figures labelled "approx." remain unverified estimates, not sourced facts.
