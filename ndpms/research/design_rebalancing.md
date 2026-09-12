# NDPMS ₹500 Cr Mandate — Monthly Rebalancing, Execution and Trading Design

Status date: 12 September 2026. This note sits alongside the regulatory design note (mandate architecture, consent legal structure, SAA bands) and the allocation design note (CMAs, sleeve weights) already produced for this mandate — figures here reuse the Moderate model's ₹500 Cr sleeve weights and bands so all three documents tie out. This note goes one layer deeper: the actual monthly operating calendar, the quantitative case for a hybrid band design, event-driven playbooks, tax-lot mechanics, a bps-level transaction-cost model with two worked ₹500 Cr trades, execution-desk policy (participation limits, block-deal/AP routing, MF cut-offs), and the daily/weekly/monthly task split.

**Governing constraint.** Under NDPMS the PM proposes; the client's dated, evidenced instruction is the only thing that authorises a trade (SEBI (Portfolio Managers) Regulations 2020, Reg 24 read with Reg 2 definitions of discretionary/non-discretionary) [1]. Every design choice below is built to make that instruction cheap to obtain (one omnibus monthly consent) without becoming, in substance, a standing discretion.

---

## 1. The monthly rebalance cycle

The house already runs a weekly deployment cadence (Monday redemption / Thursday deployment). NDPMS does not change that execution rhythm — it inserts one consent gate before the month's trades are allowed to enter that weekly pipeline. The monthly cycle below is the execution-desk expansion of the consent calendar already fixed in the mandate design (T-5 IC sign-off → T-3 pack build → T-1 client walkthrough → T0 consent → T0–T+7 execution → T+8 post-trade report → month-end+5 statement → month-end+7 working days SEBI/APMI report) [2].

| Step | Day | What happens | Owner | Output / SLA |
|---|---|---|---|---|
| 1. Data close | T-5 (last business day before IC week) | NAV, holdings, corporate actions, accruals frozen for the month; ADV/liquidity refresh for direct-stock sleeve | Ops | Golden EOD snapshot, time-stamped |
| 2. Drift report | T-5 | Actual vs SAA target by sleeve and by line; band-breach flags; unlisted-%, associate-%, derivative-notional checks against IPS ceilings | Risk/Compliance | Drift report v1 |
| 3. IC view | T-5 to T-4 | House monthly view (over/underweight tilts) applied to targets; tilt magnitude capped by governance thresholds already fixed in the allocation note | IC | Signed tilt sheet |
| 4. Proposal pack (RPP) build | T-3 | Every trade: ISIN/scheme, side, ₹ amount or quantity, execution channel (on-screen/block/AP/AMC-direct), limit or participation rule, execution window, cost estimate (bps model, §5), tax estimate (realised gain, LTCG/STCG split, exemption headroom), band-compliance flag | PM + Compliance | RPP v1, pre-trade compliance sign-off |
| 5. Client walkthrough | T-1 | 30-minute call/portal walkthrough of the pack, cost and tax numbers, any flagged unlisted/associate items | RM | Client Q&A closed |
| 6. Client consent | T0 (1st Thursday of month, aligned to the existing deployment Thursday) | Client e-signs (Aadhaar e-sign/DSC) the pack as a whole, or line-item, on the portal; validity 10 trading days | Client | Hashed consent record in OMS audit trail |
| 7. Execution window | T0 to T+7 | Trades released into the existing weekly Mon-redeem/Thu-deploy pipeline, staggered per §6; algo/participation rules applied | Dealing | Slippage vs arrival price ≤ 15 bps target |
| 8. Settlement | T+1 (equity, CDSL/NSDL) to T+2/T+3 (MF, category-dependent) | Pay-in/pay-out, demat credit/debit, MF unit allotment | Ops/Custodian | Zero settlement fails |
| 9. Post-trade recon | T+8 | Fills vs RPP, realised slippage, actual cost/tax booked, updated weights vs SAA | Ops | Recon pack, exceptions escalated same day |
| 10. Client confirmation | Month-end + 5 business days | Monthly statement (Reg 31 content: composition, transactions, expenses, risk) | Ops/Compliance | Statement issued |

**Compressing consent friction.** Three design choices do the work:
- **One omnibus pack, not N separate approvals** — the RPP bundles the month's entire trade list into a single e-signed instruction; line-item override is available but the default flow is "approve all."
- **A Standing Instructions Register (Annex C of the agreement)** carries mechanical, revocable, fully-parameterised actions that never need a fresh consent each month: idle-cash sweep (>₹50 lakh into a named liquid/overnight fund, daily), dividend/coupon reinvestment routing, execution of an already-approved multi-week tranche schedule, and hedge-roll at the same notional. Anything that changes an asset-class weight or introduces a new security stays inside the RPP.
- **Pre-agreed bands function as the "reason code"** for each trade line — the RPP does not re-litigate the model each month, it only asks the client to confirm the specific ₹ amounts computed off already-approved targets and bands.

Latency cost is real and must be underwritten explicitly, not waved away: expected tracking cost of a delay ≈ (undeployed weight) × (daily vol) × √(days). On ₹500 Cr, a 5% (₹25 Cr) equity underweight left unresolved for 10 days at ~1% daily index vol costs ≈ ₹79 lakh of 1-sigma tracking risk; cutting the consent SLA from 10 to 2 business days cuts that to ≈ ₹35 lakh [3]. This is why the SLA table above targets a 2-business-day consent turnaround with a 48-hour escalation call.

---

## 2. Band design: calendar vs threshold vs hybrid

### 2.1 Three designs, and why hybrid wins

| Design | Rule | Pro | Con |
|---|---|---|---|
| **Calendar** | Trade every sleeve fully back to target on a fixed date, regardless of drift size | Simple to consent (same date every month); predictable ops load | Trades even when drift is inside noise; highest turnover, tax and cost for the least control of tracking error |
| **Threshold (band-only)** | Trade only sleeves that have breached their band, whenever that happens, checked continuously | Lowest turnover/cost/tax for a given tracking-error tolerance | Under NDPMS, "whenever" is not compatible with a monthly consent gate — needs either standing pre-authorisation (discretion risk) or constant ad hoc consent (friction) |
| **Hybrid (recommended)** | Check every sleeve against its band on the fixed monthly review date; trade **only the breaching lines**, inside the single monthly RPP; add a narrow pre-authorised event sleeve (§3) for genuine tail moves between reviews | Matches the mandate's monthly consent cadence exactly; captures most of the threshold design's cost/tax efficiency | Requires the client to accept that some months have zero trades and others have many — needs to be set as an expectation up front |

### 2.2 Absolute vs relative bands, and where to trade to

- **Large/liquid sleeves (equity core, target-maturity debt, cash/arbitrage): absolute (percentage-point) bands.** A ±1pp band on a 2% sleeve is unworkable (50% relative tolerance is too tight to avoid noise trading); a ±5pp band on a 22% sleeve is proportionate (~23% relative).
- **Small sleeves (silver, REIT, active small-cap): relative bands, 20–25% of target.** A 1% target sleeve gets a ±0.20–0.25pp band, not a flat ±1pp (which would be a 100%+ relative swing before any trade triggers).
- **Illiquid/locked sleeves (AIF Cat I/II, Cat III/SIF hybrid LS): no tradable band** — they cannot be rebalanced by selling (lock-in), only by sizing new commitments and letting the liquid sleeves flex around them. Track drift for reporting only.
- **Trade to target vs trade to the inner band edge:** trading fully back to **target** removes drift risk but forces a slightly larger trade every time a line breaches, which raises turnover for lines that oscillate around the edge. Trading to the **inner edge of the band** (i.e., only enough to bring the line back inside tolerance) cuts turnover and lets the position "ride" naturally; the cost is a permanently wider realised tracking error. **Recommendation: trade to target for sleeves with regulatory/IPS hard ceilings (unlisted %, associate %) and trade to the inner edge for everything else** — this is strategy F/H below and is the best cost/TE trade-off in the simulation.
- **Minimum trade size.** Set a floor of **₹75 lakh–₹1 Cr (≈15–20 bps of AUM)** per line before a trade is released, even if the band is technically breached — below this, transaction cost and bid-ask spread exceed the tracking-error benefit of trading. (Used as the noise floor in the simulation below.)
- **Turnover budget.** Set an IPS-level annual turnover ceiling for the *liquid* book (ex-AIF/PMS) of **15–25%/yr** for Moderate, reviewed annually against realised cost and tax drag.

### 2.3 Quantified comparison for the ₹500 Cr Moderate book

Monte Carlo simulation (10-yr weekly paths, 1,500 runs, house CMAs and correlations from the allocation note, 16-line Moderate SAA and bands exactly as designed there) comparing calendar, band-only and hybrid designs. **Modelling note: each strategy row uses an independent random path (not common random numbers), so the CAGR columns carry simulation noise and should not be read as "strategy X beats the market" — only the turnover/cost/tax/TE columns, which are the object of this comparison, are reliable relative signals.** Assumptions: one-way transaction cost 3–35 bps by sleeve (ETF 2, factor index 2, active MF 1, direct stock 12.6 incl. impact, international 3, debt 0–3, arbitrage 1, gold/silver 2–3, REIT 6, illiquid AIFs 0 (untraded)); tax on realised gains at LTCG 12.5% for equity-like sleeves >12m and slab (~39%) for debt-like sleeves; ₹1 Cr minimum ticket.

| Strategy | Turnover %/yr | Trades/yr | Cost bps p.a. | Tax bps p.a. | Total cost+tax bps p.a. | ₹ Cr/yr on ₹500 Cr | TE vs SAA %/yr | Avg \|drift\| (pp, summed across 16 lines) |
|---|---|---|---|---|---|---|---|---|
| A. Monthly calendar, full to target | 26.0 | 95.8 | 2.8 | 49.7 | **52.5** | 2.63 | 0.28 | 4.3 |
| B. Quarterly calendar, full to target | 15.1 | 38.9 | 1.7 | 36.1 | 37.8 | 1.89 | 0.38 | 5.1 |
| C. Annual calendar, full to target | 7.7 | 11.8 | 0.9 | 23.5 | 24.4 | 1.22 | 0.57 | 7.3 |
| D. Band-only, continuous monitoring, trade to target | 6.5 | 4.1 | 0.5 | 13.4 | 13.9 | 0.70 | 0.89 | 11.6 |
| E. Hybrid: monthly review, breach → target | 6.1 | 3.7 | 0.5 | 13.1 | 13.6 | 0.68 | 0.89 | 11.9 |
| **F. Hybrid: monthly review, breach → inner band edge** | **4.0** | **4.4** | **0.3** | **10.1** | **10.4** | **0.52** | 0.78 | 12.4 |
| G. Hybrid + event overlay (1.5× band any day, + equity-aggregate 3pp trigger) | 8.2 | 6.8 | 0.7 | 17.7 | 18.4 | 0.92 | 0.79 | 8.6 |
| H. Hybrid + event overlay, inner edge | 4.4 | 13.6 | 0.4 | 11.6 | 12.0 | 0.60 | 0.61 | 10.0 |

**Reading it:** monthly-calendar-full-rebalance (A) costs **~4-5x** more in tax+cost than a disciplined hybrid (F/H) for a *narrower* average drift band — most of that cost is realised gains tax from selling lines that were only marginally off target. **Recommendation: Strategy H — monthly review with breach-to-inner-edge trading, plus the pre-authorised event overlay (§3) for tail moves** — gives the best combination of low turnover (4.4%/yr), low realised tax (11.6 bps), and the *tightest* tracking error of the threshold family (0.61%) because the event overlay catches the large excursions that a pure monthly check would otherwise miss for up to 30 days. Budget **≈₹0.5–0.7 Cr/yr** (10–14 bps) of cost+tax drag for rebalancing the liquid book at this design point, separate from the PM fee and the sleeve-level TER/TCO already quantified in the allocation note.

---

## 3. Event-driven rebalances (not HFT)

Event triggers exist to catch moves too large or too fast to wait for the monthly review — they are pre-authorised playbook responses, not discretionary trading, and not intraday.

| Trigger | Threshold | Pre-authorised action (Standing Instruction) | Consent mode | Max response time |
|---|---|---|---|---|
| Sleeve band breach ≥1.5× the normal band | e.g. equity core >27.5% (band ±5, 1.5× = ±7.5) | De-risk only: trim the breaching line back to the *outer* normal band edge (not full target) | Pre-authorised in IPS; executed, then reported at next monthly cycle | Same/next business day |
| Equity-aggregate drift | Sum of equity sleeves vs target equity >3pp | Same as above, sized proportionally across equity lines | Pre-authorised | 1 business day |
| Drawdown/vol regime | Nifty 50 closes ≥5% below its 20-day high, or India VIX >22 for 3 consecutive days [4] | Pull forward the next scheduled deployment tranche; do not sell into the drawdown without fresh consent | Pre-authorised for the *buy* side; ad hoc consent required for any *sell*-side de-risking beyond the 1.5×-band trim above | 1 business day |
| Severe tail event | Nifty ≥10% below 20-day high, or VIX >25 | Ad hoc: RM calls client same day with a specific one-page recommendation (e.g. tail-hedge activation, or accelerated deployment) | Ad hoc consent, verbal-then-e-sign within 24h with a follow-up written confirmation | 2 business days |
| Large inflow (>₹10 Cr, e.g. dividend from listed holding, maturity proceeds) | — | Sweep to liquid/overnight same day; deploy per the pre-agreed staggered ladder (below) without a fresh full-pack consent, since the *instrument and ratio* were pre-approved | Pre-authorised (Standing Instruction) | Same day sweep; ladder per §6 |
| Large outflow (redemption request) | — | Fund from cash/liquid first, then pro-rata trim across sleeves *away* from anything currently under-target | Ad hoc consent for the specific trim list (amounts only, not instrument selection, since sizing formula is pre-agreed) | 2 business days |
| Corporate action requiring an active election (rights issue, buyback, scheme merger) | Any | **No standing instruction** — a rights subscription is an "active" unlisted-cap event and must go through the RPP or an ad hoc consent | Ad hoc consent required | Before the corporate-action deadline |
| Index reconstitution / benchmark rebalance (Nifty 50/500 quarterly changes) | — | Passive sleeves follow automatically inside the fund/ETF; direct-stock sleeve additions/deletions flagged for the next RPP | Next monthly RPP (not urgent) | Monthly |

Deployment ladder for a large inflow (illustrative, ₹25 Cr fresh capital): 40% into liquid/overnight day 1; 20%/week into the pre-approved instrument mix over the next 3 weeks via the existing Thursday deployment slot — this reuses the house's staggered-tranche logic rather than inventing a new one for NDPMS.

---

## 4. Tax-aware and cost-aware rebalancing

### 4.1 Lot selection: FIFO is mandatory, not a choice, for demat holdings

Section 45(2A) of the Income-tax Act (framework carried into the Income-tax Act, 2025) provides that for securities held in dematerialised form, cost of acquisition and period of holding are determined on a **first-in-first-out (FIFO)** basis; CBDT Circular No. 768 (24-June-1998) clarifies that where an investor holds the *same* security across **multiple demat accounts**, FIFO is applied **account-by-account**, not pooled across accounts [5]. Specific identification (picking an arbitrary high-cost lot to sell) is **not permitted** within a single demat account and has been rejected by tribunals as a "colourable device" when attempted [5].

**Operational consequence — the only lever available is account structure, not lot choice within an account.** Run the mandate across **2–3 purpose-segregated demat accounts** (e.g., (i) Core/strategic direct-equity book, rarely traded; (ii) Tactical/rebalancing book, where the monthly RPP trims and adds; (iii) a small tax-lot/harvesting book used only in Q4/Jan-Mar for loss or gain harvesting). Because FIFO applies *per account*, choosing **which account** to sell out of is economically equivalent to a coarse form of specific identification — sell from the account whose oldest lot has the tax profile you want (long-held small gain to harvest the exemption; long-held large loss to harvest against other gains), leaving the other accounts' lots undisturbed. **This decision must be made before the first trade** — retrofitting account segregation after a single demat account already holds a mixed-cost position does not help.

### 4.2 LTCG exemption harvesting

Listed equity/equity-MF LTCG is taxed at **12.5% above an annual exemption of ₹1.25 lakh per FY** (aggregated across all such gains for the investor, not per security) [6]. India has **no wash-sale rule** — a security can be sold to crystallise a gain (or loss) and immediately repurchased at the same price to step up the cost basis, with no minimum holding-period restriction on the repurchase. **Do this every FY, near year-end, on the oldest long-held lots with the largest embedded gain that still fits under the ₹1.25 lakh exemption** (per PAN, and this exemption is shared with the client's own personal book outside the PMS — coordinate with the client/RM). On a ₹500 Cr book with an 8–12% direct-equity sleeve, this is a small but recurring, zero-cost-basis-risk tax saving that should be a **standing, pre-authorised** March instruction, not a fresh ad hoc consent each year.

### 4.3 Avoiding STCG, and why FIFO actually helps

STCG on STT-paid listed equity is taxed at **20%** vs LTCG's 12.5% [6] — an 8pp difference that should drive trade sequencing whenever a sleeve has both a >12-month and a <12-month lot outstanding and only a partial trim is needed. Convenient side-effect: **FIFO sells the oldest lot first by construction**, which is usually the long-held (LTCG-eligible) lot — so the mandatory tax-lot rule is *already* biased toward the tax-efficient outcome for a steadily-accumulating position. The exception to watch: a sleeve that has just received a large fresh purchase (e.g., post-inflow deployment) now has its *newest* shares at the front of the FIFO queue in economic terms but at the *back* of the literal FIFO order (oldest-first) — so a forced sell shortly after a big top-up will still hit old, LTCG lots first, which is fine, but means the desk cannot "protect" the old lots by choice; it is automatic. Where a full band-breach requires selling *through* the LTCG lots into STCG territory, flag this explicitly in the RPP cost/tax estimate line so the client sees the STCG hit before consenting.

### 4.4 Use inflows and income to rebalance before selling

Every month, before generating any sell-side RPP lines: (i) sweep matured coupons/dividends/distributions and (ii) any fresh client inflow toward the **most underweight** sleeve(s) first. This closes drift without realising any gain at all on the overweight side. Only after this cash-flow-based rebalancing is exhausted should the RPP include actual sells of overweight lines. This single rule is typically responsible for closing a large share of monthly drift on a growing/income-generating book at no tax or transaction cost.

### 4.5 Netting across sleeves

- **STCG losses** can be set off against **any** capital gain — STCG or LTCG, equity or debt-fund (Sec 50AA deemed-STCG income counts) [6][7].
- **LTCG losses** can only be set off against **LTCG gains** — an LTCG loss cannot shelter an STCG or debt-fund gain.
- **Unused capital losses carry forward 8 assessment years** — track them at the client level (not per sleeve) so a loss realised trimming, say, the small-cap MF sleeve in a down month is available to net against an equity direct-stock gain realised six months later in a different sleeve.
- Before any FY-end (31 March) harvesting instruction, Ops must pull the client's **cumulative realised gain/loss ledger across all sleeves** — netting decisions are wrong if made sleeve-by-sleeve.

---

## 5. Transaction cost model (bps, ₹500 Cr scale)

### 5.1 Cost stack by instrument (one-way, steady state; verified components cited, spread/impact and brokerage are negotiated/approx.)

| Instrument | STT | Stamp duty | Exchange + SEBI charges | Institutional brokerage | GST (18% on brokerage+exch+SEBI) | Bid-ask / impact | MF exit load / AIF terms | Round-trip total (ex-impact, ex-tax) |
|---|---|---|---|---|---|---|---|---|
| Direct listed equity (delivery) | 0.1% each leg = 20 bps RT [8] | 0.015% buy-side only ≈1.5 bps [9] | ≈0.3 bps/leg (NSE) + 0.01 bps/leg (SEBI turnover fee, ₹10/crore) [9] | ~3–5 bps/leg (negotiated, institutional) | ~18% × (brokerage+exch+SEBI) ≈1.5 bps RT | function of %ADV (§6.1) — separate | — | **≈27–31 bps** + impact |
| ETF, on-screen secondary market | 0.001% sell-side (MF-unit-sale rate) [8] | as equity, buy-side | as equity | as equity, often tighter | as equity | bid-ask spread, 3–15 bps depending on ETF liquidity | — | ≈10–14 bps + spread |
| ETF, via AP / direct-with-AMC (≥₹25 Cr) [10] | 0.001% sell-side only | none (not an exchange trade) | none | AMC/AP handling fee ~2–3 bps approx. | minimal | basket/creation impact ~2–4 bps approx. | none (no exit load on ETFs) | **≈5–7 bps** |
| Index fund (direct plan) | 0.001% on redemption | none | none | none | none | none (NAV-based) | none typically | **≈0–1 bp** (embedded TER separately, see allocation note) |
| Active MF (direct plan) | 0.001% on redemption | none | none | none | none | none | exit load now capped at 3% max, typically 0–1% after 12m for equity funds [11] | **0–1 bp** if held >12m; up to 100 bps if redeemed early |
| Listed G-sec / SDL / corporate bond | none (STT does not apply to debt securities) | ~0.005% approx. (unverified this session) | minimal | dealer spread embeds cost | — | bid-offer 3–8 bps approx. | — | **≈4–9 bps** |
| REIT/InvIT (listed units) | applicability to REIT/InvIT units is **unclear_verify** this session — treat as equity-like (0.1%) until confirmed | as equity | as equity | as equity | as equity | wider spread, 15–30 bps approx. (lower float) | — | ≈35–55 bps, verify STT line |
| AIF Cat I/II | none (private placement) | none | — | — | — | — | no exit (locked, 3–7 yr close-ended tenure) [12] | n/a — commitment-drawdown drag instead (see allocation note) |
| AIF Cat III (open-ended) | none | none | — | — | — | — | soft lock-in ~1–3 yr + exit load approx. 1–2% within window [12] | n/a |

### 5.2 Worked example A — ₹15 Cr trim of a large-cap direct-equity name

| Component | Basis | ₹ | bps of trade |
|---|---|---|---|
| STT (sell only, delivery) | 0.1% × ₹15 Cr | ₹15.0 lakh | 10.0 |
| Exchange charges | 0.00297% × ₹15 Cr | ₹0.45 lakh | 0.3 |
| SEBI turnover fee | 0.0001% × ₹15 Cr | ₹0.015 lakh | 0.01 |
| Brokerage (institutional) | 4 bps × ₹15 Cr | ₹6.0 lakh | 4.0 |
| GST @18% on brokerage+exch+SEBI | 18% × (4.0+0.3+0.01) bps | ₹1.2 lakh | 0.8 |
| **Explicit cost subtotal** | | **≈₹22.6 lakh** | **≈15 bps** |
| Market impact (participation-based, large-cap, ADV comfortably >₹100 Cr) | 8–12 bps approx. | ₹12–18 lakh | 8–12 |
| **All-in execution cost** | | **≈₹35–41 lakh** | **≈23–27 bps** |
| **LTCG tax, illustrative 40% embedded gain ratio** | 12.5% × 40% × ₹15 Cr | **≈₹75 lakh** | **≈50 bps** |

**The lesson this example is built to teach:** tax dominates. Execution cost on a routine trim is ~25 bps; the tax on the same trim, at a plausible embedded-gain ratio, is ~2x that even at the *lower* LTCG rate. This is why §4 (sequencing, netting, harvesting) is worth materially more to net-of-tax return than shaving another few bps off execution.

### 5.3 Worked example B — ₹40 Cr ETF switch (e.g., rebalancing between two Nifty-linked ETF/index vehicles)

| Route | STT | AP/AMC handling | Spread/impact | Brokerage+GST | **Total** |
|---|---|---|---|---|---|
| **AP / direct-with-AMC** (order ≥₹25 Cr threshold) [10] | ₹0.4 lakh (0.1 bp) | ₹12 lakh (3 bps) | ₹8 lakh (2 bps) | — | **≈₹20 lakh (≈5 bps)** |
| **On-screen secondary market** | ₹0.4 lakh (0.1 bp) | — | ₹40 lakh (10 bps, crossing the book on both legs) | ₹19 lakh (16+3 bps incl. GST) | **≈₹59 lakh (≈15 bps)** |
| **Saving from routing via AP/AMC** | | | | | **≈₹39 lakh (≈10 bps)** |

Plus, if the switch crystallises gains: illustrative 25% embedded-gain ratio → LTCG tax ≈ 12.5% × 25% × ₹40 Cr ≈ **₹1.25 Cr** — again an order of magnitude larger than the execution-routing saving, reinforcing that **any switch between two similar vehicles should be evaluated post-tax**, and that the ₹25 Cr AP threshold (§6) is a hard rule for any ETF order at or above that size.

---

## 6. Execution policy

### 6.1 Participation limits and algo execution

| Parameter | Rule | Basis |
|---|---|---|
| Max participation rate, direct-stock order | ≤10–15% of that stock's trailing 20-day ADV per session | Standard institutional practice; ties to the ≥20% ADV/5-day liquidity assumption already used to size direct-stock lines in the allocation note |
| Multi-day staggering | Any ticket >2% of ADV is split via VWAP/TWAP over 2–5 sessions inside the T0–T+7 execution window | Keeps within participation limit without missing the window |
| Order type | Limit orders referenced to arrival price ± a cost-model band; no market orders on illiquid names | Controls slippage; matches the RPP's stated cost estimate |
| Slippage budget | ≤15 bps vs arrival price (from the monthly calendar SLA, §1) | Escalate to RM/IC if breached |

### 6.2 Block-deal and bulk-deal windows

- **Block deal window** (current framework): minimum order size **₹25 Cr** (raised from ₹10 Cr) [13]; **morning window 8:45–9:00 AM**, reference price = previous day's close; **afternoon window 2:05–2:20 PM**, reference price = VWAP of trades 1:45–2:00 PM; orders must be within **±3%** of the reference price; trades result in **compulsory delivery** — no same-window square-off [13][14]. **Use this window for any single-line direct-equity ticket ≥₹25 Cr** (large concentrated adds/trims, e.g. an IC-directed initiation) — it avoids the on-screen impact-cost curve entirely for a size that would otherwise move the market.
- **Bulk deal disclosure** threshold (percentage-of-listed-shares trigger requiring same-day exchange disclosure) — **unclear_verify this session** (web search budget exhausted before this could be re-confirmed); treat any single-line trade near **0.5% of a company's listed shares** as needing a bulk-deal disclosure check before release, and verify the exact current threshold with the exchange before the first ticket of this size.
- Below ₹25 Cr, a direct-equity ticket goes through the normal VWAP/TWAP on-screen process of §6.1.

### 6.3 ETF creation/redemption via Authorised Participants

Orders of **₹25 Cr or more** in a single ETF may transact **directly with the AMC** (in-kind creation/redemption via an Authorised Participant, or cash creation) instead of the exchange order book; below ₹25 Cr, the exchange route is compulsory [10]. Nippon India ETF Nifty BeES, illustratively, has a direct-purchase creation-unit size of 50,000 units (exchange-traded in single units) [15]. **Design rule: any ETF rebalancing leg ≥₹25 Cr must route through the AP/AMC-direct channel** (worked example B, §5.3, shows the ~10 bps saving); the mandate should empanel at least one AP relationship before go-live so this is available on day one rather than defaulting to on-screen execution by omission.

### 6.4 Mutual fund cut-off and settlement timing

Cut-off and NAV-applicability rules differ materially by fund category — **liquid/overnight funds** cut off earlier in the day than equity/other funds, and above the SEBI large-transaction threshold NAV applicability turns on when funds are actually realised by the AMC, not on submission time (approx., general industry practice — not re-verified this session; confirm the current cut-off clock and threshold with each AMC/RTA before building the order calendar). **Settlement/credit timing is category-dependent** — overnight/liquid funds settle fastest (approx. T+1), equity/hybrid and debt funds typically T+1 to T+3 depending on category and AMC — again approx., to be pinned down operationally rather than assumed, since a mis-timed MF order can leave a one-day cash or exposure mismatch against the RPP's execution-window SLA.

### 6.5 Cash management ladder

| Horizon | Vehicle | Purpose |
|---|---|---|
| Overnight / <1 week | Overnight fund or bank sweep | Idle cash from redemptions/inflows pending deployment |
| 1 week – 1 month | Liquid fund | Redemption-pending and short deployment-pipeline cash |
| >1 month, <12 months | Arbitrage fund | Equity taxation (12.5% LTCG >12m) beats liquid fund's slab-taxed gains for cash the desk expects to hold a few months; standing instruction sweeps here once a liquid-fund balance has been idle >30 days |
| Redemption/settlement mismatch buffer | Overnight fund, sized to the largest single week's net redemption in the trailing 12 months | Covers the gap between a client's T+1 cash need and a T+2/T+3 MF/AIF settlement on the asset being sold to fund it |

### 6.6 Stagger schedules

The monthly RPP's approved trades enter the **existing weekly Monday-redemption / Thursday-deployment cadence** — this both reuses house infrastructure and naturally staggers execution over up to four weekly tranches inside the 10-trading-day consent validity window, rather than concentrating the whole month's flow into a single day (which would both breach participation limits on the larger tickets and create a predictable, front-runnable pattern).

---

## 7. Daily / weekly / monthly task split

| Cadence | Task | Owner | CAN / SHOULD / AVOID |
|---|---|---|---|
| Daily | NAV/valuation checks, price/corporate-action feed validation | Ops | SHOULD |
| Daily | Corporate-action processing (dividends, bonus, splits) per standing instruction | Ops | SHOULD |
| Daily | Idle-cash sweep >₹50 lakh into named liquid/overnight fund | Dealing (auto/standing instruction) | CAN (pre-authorised) |
| Daily | Settlement/fails monitoring, demat reconciliation | Ops | MUST (non-negotiable control) |
| Daily | Risk dashboard: VaR, drawdown, VIX/regime trigger monitor | Risk | SHOULD |
| Daily | Any discretionary trade outside an approved RPP or Standing Instruction | Dealing | **AVOID / not_allowed** — the core NDPMS boundary |
| Daily | Intraday trading, F&O speculation, naked shorting | Dealing | **AVOID / not_allowed** |
| Weekly | Execute the week's tranche of the current RPP (Mon redemption / Thu deployment) | Dealing | SHOULD (core cadence) |
| Weekly | ADV/liquidity refresh for the direct-stock sleeve | Risk/Dealing | SHOULD |
| Weekly | Informal drift snapshot (no trading action, monitoring only) | Risk | CAN |
| Weekly | AIF/PMS capital-call and distribution tracking | Ops | SHOULD |
| Weekly | Event-trigger screen (band ≥1.5×, equity-aggregate 3pp, VIX/drawdown) | Risk | MUST |
| Monthly | Full drift report, RPP build, consent cycle, execution window, post-trade recon, client statement | PM/RM/Ops/Compliance | MUST (core cadence) |
| Monthly | SEBI/APMI regulatory report | Compliance | MUST |
| Quarterly | Index reconstitution pass-through check for passive sleeves | PM | SHOULD |
| Quarterly | AIF/third-party PMS manager due-diligence refresh | PM | SHOULD |
| Annual (Q4/Jan–Mar) | LTCG exemption harvesting and loss-netting review across all sleeves and demat accounts | PM/Compliance | MUST (recurring tax alpha) |
| Annual | IPS/SAA and band-width reset review against realised turnover, TE and cost | IC | SHOULD |
| Annual | CMA and benchmark refresh (feeds the allocation note) | IC | SHOULD |
| Ad hoc | Rights issue / scheme-merger corporate action needing an active election | RM/PM | Ad hoc consent required — **never** via standing instruction |
| Ad hoc | Large inflow/outflow deployment or redemption ladder | Dealing | CAN (pre-authorised sizing; ad hoc consent only for outflow instrument selection) |

---

## Sources

[1] SEBI (Portfolio Managers) Regulations, 2020, Reg 2/24 (discretionary vs non-discretionary; client-directed trading) — as summarised in the mandate's regulatory design note; primary SEBI hosts were egress-blocked this session.
[2] Internal cross-reference: this mandate's regulatory design note, §5.2 ("Consent SLA and monthly calendar") and §5.3 ("SAA bands and hard limits").
[3] Internal cross-reference: regulatory design note §5.2, latency-cost formula and worked ₹500 Cr numbers (§6).
[4] Internal cross-reference: allocation design note, event triggers (Nifty −5%/−10% from 20-day high, India VIX >22/>25); Nifty 50 closed 23,398.10 on 11-Sep-2026 — https://www.5paisa.com/blog/post-market-update-us-futures-gain-nifty-sensex-lower-bank-nifty-gains-september-11-2026
[5] FIFO for dematerialised securities, Sec 45(2A)/CBDT Circular 768 (24-6-1998), and ITAT ruling rejecting selective-lot identification — https://taxguru.in/income-tax/fifo-wins-cherry-picked-shares-mumbai-itat-calls-selective-share-identification-colourable-device-tax-avoidance.html ; https://www.incometaxindia.gov.in/w/768-circular-no.-768-dated-24-6-1998-1 ; https://www.incometaxindia.gov.in/w/section-45-64
[6] LTCG 12.5% above ₹1.25 lakh/FY, STCG 20% (Sec 111A), FY2026-27 unchanged by Budget 2026 — https://www.bajajfinserv.in/investments/understanding-long-term-capital-gains-tax ; https://taxgarden.in/blog/capital-gains-tax-rates-asset-class-ready-reckoner-india-ay-2026-27
[7] Debt mutual funds acquired on/after 1-Apr-2023 taxed as deemed short-term under Sec 50AA at slab, regardless of holding period — https://taxgarden.in/blog/capital-gains-tax-india-ltcg-stcg-ay-2026-27
[8] STT: equity delivery 0.1% both legs; MF/ETF unit sale 0.001% — https://cleartax.in/s/securities-transaction-tax-stt ; https://bigul.co/blog/market-update/stt-increase-in-fo-what-every-trader-must-know-before-april-1-2026
[9] Stamp duty 0.015% (equity delivery, buyer-side), NSE transaction charge ≈0.00297%, SEBI turnover fee 0.0001% (₹10/crore), GST 18% on brokerage+transaction+SEBI charges — https://www.angelone.in/smart-money/trading-courses/list-of-all-trading-fees-and-charges ; https://www.nseindia.com/static/invest/first-time-investor-sebi-turnover-fees-stt-other-levies
[10] SEBI circular permitting direct AMC transactions for ETF orders ≥₹25 Cr (in-kind/cash creation-redemption); exchange route compulsory below that — https://www.business-standard.com/amp/india-news/after-two-deferments-exchange-route-compulsory-for-sub-rs-25-cr-etf-deals-123050100756_1.html
[11] SEBI (Mutual Funds) Regulations, 2026 — exit-load cap cut from 5% to 3%; BER/TER restructuring; brokerage caps cut to 6 bps (cash)/2 bps (derivatives), effective 1-Apr-2026 — https://www.businesstoday.in/mutual-funds/story/exiting-mutual-funds-may-get-cheaper-as-sebi-cuts-maximum-exit-load-cap-to-3-547787-2026-08-07 ; https://www.businesstoday.in/mutual-funds/story/sebi-overhauls-mutual-fund-rules-changes-made-to-ter-framework-check-details-507113-2025-12-17
[12] AIF Category I/II close-ended, minimum 3-year tenure from final closing; Category III open- or close-ended, open-ended soft lock-in ~1–3 years with exit load — https://elementone.fund/sebi-aif-regulations-2026-guide/ ; https://www.finnovate.in/learn/blog/aif-category-iii-india
[13] SEBI revised block-deal framework: minimum order size raised to ₹25 Cr; morning window 8:45–9:00 AM (previous close reference); afternoon window 2:05–2:20 PM (1:45–2:00 PM VWAP reference); ±3% price band; compulsory delivery — https://www.angelone.in/news/market-updates/sebi-tightens-block-deal-rules-raises-minimum-trade-size-to-25-crore ; https://www.taxmann.com/post/blog/sebi-revises-block-deal-framework-minimum-order-size-rs-25-crore
[14] Same block-deal framework, corroborating summary — https://www.caalley.com/news-updates/indian-news/sebi-raises-minimum-block-deal-size-to-rs-25-crore-mandates-delivery-only-trades-check-key-takeaways
[15] Nippon India ETF Nifty BeES creation-unit structure (50,000-unit direct creation size; single-unit exchange trading) — search-result summary of https://mf.nipponindiaim.com/FundsAndPerformance/ProductNotes/NipponIndia-ETF-Nifty-BeES.pdf (direct PDF fetch was egress-blocked; facts taken from indexed search summary, verify against the live factsheet before operational use)

**Modelling disclosure:** the §2.3 turnover/cost/tax/TE comparison is a Monte Carlo simulation built for this note (10-yr weekly paths, 1,500 iterations, house CMAs/bands from the allocation note), not a market data source — treat the relative ranking as the finding, and the exact bps as illustrative/approx. pending a common-random-number rebuild before board sign-off. Two items in this note are explicitly flagged **unclear_verify** (bulk-deal disclosure threshold; REIT/InvIT STT applicability) because this session's web-search budget was exhausted before they could be pinned to a primary source — resolve both before the first trade in either category.
