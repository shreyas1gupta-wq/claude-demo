# Instrument & Manager Selection — Due Diligence Frameworks and Total Cost of Ownership
### Ionic Wealth · ₹500 Cr NDPMS mandate · design date 2026-09-12

This is the selection layer beneath the Allocate IPS/Model Master. It answers, for every rupee the Model Master says goes into an asset class: **which specific instrument or manager, at what size, screened how, monitored how, and at what all-in cost** — inside the constraint that NDPMS means every trade is a recommendation the client must consent to, not a discretionary click.

---

## 0. NDPMS design constraints on the selection layer

- **No intraday/HFT selection logic.** Every screen must produce a recommendation batch consumable in the monthly (core) or weekly-tranche (deployment) consent cycle. Anything that needs same-day execution to work (index-arb capture, momentum chasing at the margin) is disqualified by the operating model, not by the instrument's own merit.
- **Consent latency is a cost, not a nuisance.** A recommendation issued Day T is typically executed Day T+2 to T+5 (client review + signed instruction + order placement). Every liquidity/impact-cost screen below must price in this lag, not just point-in-time ADV.
- **Fee-layering discipline.** SEBI's Feb 2020 PMS circular (SEBI/HO/IMD/DF1/CIR/P/2020/26, eff. 1-Oct-2020) caps opex ex-brokerage at 0.50% p.a. of average daily AUM, bars upfront fees, and mandates MF investment **only via direct plans with no distribution fee** [19]. The Master Circular consolidation of 16-Jul-2025 carries these forward [20]. This means: the PM's fee is charged once, at the portfolio level; it is **not** layered again inside the MF/AIF wrapper beyond what that wrapper's own manager charges its own investors.
- **PM cannot outsource discretion.** Reg. 24(10)-type prohibition bars investing "on the advice of any other entity" [25]; a May-2026 SEBI enforcement order confirmed this extends to trade sizing/timing/execution, not just model selection [25]. Practical effect: a third-party PMS allocation must be structured as the **client's own separate account** with that PM — our house recommends and the client consents to the allocation size — never as us delegating our NDPMS mandate to them.

---

## 1. ETFs and Index Funds

### 1.1 Screening dimensions and thresholds

| Metric | Definition | Pass threshold at ₹500 Cr scale | Data source / cadence |
|---|---|---|---|
| Tracking difference (TD) | Fund return − index TR return, trailing 1Y | ≤ 25 bps (equity), ≤ 15 bps (debt index) | Monthly, from factsheet |
| Tracking error (TE) | Annualised SD of daily TD | ≤ 50 bps (large-cap equity), ≤ 100 bps (mid/small/factor) | Monthly |
| Scheme AUM | — | ≥ ₹1,000 Cr for any ticket > ₹15 Cr (see §1.3 rule) | Monthly |
| On-screen ADV (3-month) | NSE+BSE combined | Ticket ≤ 20% of 5-day cumulative ADV | Daily/weekly |
| Bid-ask spread | Screen-quoted, mid-session | ≤ 10 bps (Nifty/Sensex ETFs), ≤ 25 bps (factor/international) | Sampled at order time |
| iNAV discount/premium | (Price − iNAV)/iNAV | Abs ≤ 15 bps at order time; abort/route to AMC if breached | Real-time at execution |
| Replication | Physical (full/optimised sampling) vs synthetic | Physical only — no swap-based ETFs for this mandate | One-time |
| Securities lending | AMC's SLB policy on the ETF's underlying basket | Accept only if fully collateralised and disclosed in SID; avoid uncollateralised or opaque SLB | One-time DD |
| Expense ratio (BER from 1-Apr-2026) | AMC's base fee, ex-statutory levies | Equity index/ETF ≤ 20 bps; the regulatory cap itself was cut to 0.90% BER for index funds/ETFs on the 2026 MF overhaul [31] | Annual |

**Key regulatory facts (verified):**
- SEBI's Feb-2020-vintage ETF liquidity circular lets any investor transact **directly with the AMC at intraday NAV for orders ≥ ₹25 Cr**, bypassing the exchange spread entirely; APs/market-makers are exempt from the threshold (SEBI/HO/IMD/DOF2/P/CIR/2022/145, 28-Oct-2022, effective 1-May-2023) [1].
- From 1-Apr-2026, SEBI's MF Regulations 2026 replace TER with a **Base Expense Ratio (BER)**: statutory levies (STT, stamp duty, GST, SEBI fee, exchange charges) are now billed separately/at actuals, and cash-market brokerage caps were cut from 12 bps to 6 bps (derivatives 5→2 bps) [31]. This narrows the AMC-controllable cost further but does **not** remove STT/stamp duty from your transaction bill.
- NSE's own published impact cost for a ₹50 lakh Nifty 50 basket was ~0.02% (Mar-2026) [3] — trivial at basket level, but our tranches are 40–80× that size, so impact cost must be modelled off the ETF's own ADV, not the index's basket impact cost.

### 1.2 Liquid Indian ETFs by category (approx., verify AUM at time of trade — figures below are dated Sept 2026)

| Category | Representative ETF(s) | AUM (₹ Cr, approx.) | Notes |
|---|---|---|---|
| Nifty 50 | Nippon India ETF Nifty BeES | ~66,777 (9-Sep-2026) [2] | Deepest liquidity of any Indian ETF; creation unit 50,000 units [2] |
| Bank Nifty | Nippon India ETF Nifty Bank BeES | ~8,379 (9-Sep-2026) [2] | Sector-concentrated — not core beta |
| Gold | Nippon/HDFC/SBI/ICICI Gold ETFs (industry) | Industry Gold ETF AUM ~₹1.71–1.85 lakh Cr (Mar–May 2026), +191–195% YoY [4][5] | AP creation-unit route recommended above ~₹20–25 Cr ticket |
| Silver | Nippon/ICICI Silver ETFs | Industry inflow-led growth through 2025, net outflow ~₹2,133 Cr in May-2026 (profit booking) [4] | Wider spreads than gold; treat as tactical sleeve |
| International (India-listed) | Motilal Oswal Nasdaq 100, etc. | Constrained by SEBI's industry-wide USD 7 bn overseas MF cap (near-exhausted through 2026; ETF sub-cap USD 1 bn) [35] | Expect premiums to iNAV / subscription pauses — budget 10 bps premium risk |
| Target-maturity (debt) | Bharat Bond ETF/FOF series (2030/2031/2032/2033) | Multi-thousand-crore series AUM; 5Y return ~6.83% p.a. (Apr-2030 series, to Jul-2026) [29] | Best vehicle for laddered AAA/SDL exposure at this ticket size |

**Overall market context:** India's ETF industry AUM had crossed ~₹8.75–10 lakh Cr with ~260 schemes by early 2026, and average daily ETF turnover rose from ₹237 Cr (FY21) to over ₹4,200 Cr (Apr-2025–Feb-2026) — an 18x rise — though commodity-ETF turnover (~₹2,700 Cr/day) now exceeds equity-ETF turnover (~₹745 Cr/day) [4]. **Implication:** equity-ETF secondary liquidity, while vastly improved, is still thinner than gold/silver ETF liquidity in relative terms — size equity ETF tickets conservatively against ADV even though AUM looks large.

### 1.3 ETF vs index fund — when to prefer which

**Decision rule (break-even holding period):**
```
Break-even years = ETF round-trip cost (bps) / (Index fund TER − ETF TER, bps)
```
Worked example: ETF TER 4 bps, round-trip (spread + brokerage + STT) ≈ 12 bps, comparable index fund TER 18 bps →
Break-even ≈ 12 / (18 − 4) = **0.86 years**.

**Rule of thumb for the ₹500 Cr book:**
- **Use the ETF (AP/AMC-direct route)** for any position expected to be held **> 1 year** and where the ticket is ≥ the creation-unit-equivalent size (typically ≥ ₹25 Cr, qualifying for direct-AMC dealing under [1]) — captures the lower running cost and avoids exchange spread on entry via the AP route.
- **Use the index fund** for (a) tickets below the AMC-direct threshold where on-screen ETF impact cost would exceed the TER differential, (b) any sleeve subject to **frequent monthly rebalancing** (tilt/band rebalancing churns an ETF's bid-ask/impact cost repeatedly, whereas the index fund's NAV-based transaction has zero spread — only 1 day of NAV/settlement risk, budgeted at ≈ 1-day × portfolio volatility, ≈ ₹25 lakh 1-sigma on a ₹25 Cr tranche), and (c) any sleeve intended for **SIP-like systematic monthly investing** where at-NAV dealing removes execution risk entirely.
- **Never** use an ETF that trades at a persistent iNAV premium/discount > 15 bps intraday for size — route to AMC-direct or switch to the index fund.

### 1.4 Execution routing table (₹25 Cr Nifty tranche, illustrative)

| Route | Modelled cost | When to use |
|---|---|---|
| On-screen (exchange) | ~15 bps (impact ~12 bps + brokerage/charges ~3 bps) | Tickets < ₹25 Cr, or when AP/AMC route unavailable same-day |
| AP creation-unit route | ~6–7 bps (basket impact ~3–4 bps + AP fee ~3 bps) | Tickets ≥ creation-unit size, held > 1Y |
| Direct-with-AMC (≥ ₹25 Cr) | ~4–6 bps, intraday NAV-based [1] | Any qualifying large tranche — default route above threshold |
| Index fund at NAV | 0 bps transaction cost, T+1 NAV risk ≈ 1-day vol | Monthly tranche/rebalance sleeves; sub-₹25 Cr tickets |

---

## 2. Active Mutual Funds

### 2.1 Scoring template (100-point weighted scorecard)

| Factor | Weight | Pass / scoring rule |
|---|---|---|
| Rolling 3Y alpha consistency | 20 | % of monthly rolling 3Y windows (trailing 5Y history) beating category benchmark; score = that % (e.g., 65% hit-rate → 65/100 on this factor) |
| Rolling 5Y alpha consistency | 15 | Same methodology, longer window; weights toward genuine cycle-tested skill |
| Up-capture / down-capture ratio | 15 | Target: up-capture ≥ 100%, down-capture ≤ 85%, i.e., ratio ≥ 1.15; score scaled linearly, 0 below ratio 1.0 |
| Active share | 10 | ≥ 60% for a fund charging active fees; below 60% is "closet indexing" — hard fail if also charging > 100 bps direct TER |
| Fund size vs. strategy capacity | 15 | Penalise if scheme AUM > 1.5× the manager's stated/historic capacity for that style (esp. small/mid-cap); hard cap our ticket at ≤ 1% of scheme AUM regardless |
| Manager tenure on this scheme | 10 | ≥ 3 years managing this specific scheme; reset score to 0 on manager change in trailing 12 months pending re-underwrite |
| Direct-plan TER | 10 | Large/flexi-cap ≤ 70 bps good, mid-cap ≤ 90 bps, small-cap ≤ 100 bps (direct); score inversely to TER within band |
| Concentration / style drift | 5 | Top-10 holdings ≤ 45% (unless explicitly concentrated mandate); sector/style consistency vs stated mandate over 8 rolling quarters |

**Selection gate:** onboard only funds scoring ≥ 65/100 with **no factor below 40/100**; re-score every 6 months; a fund dropping below 50/100 or losing its manager triggers a **redemption recommendation** in the next monthly cycle (not an immediate sale — NDPMS requires the consent step).

### 2.2 Active vs passive by category — the house rule

| Category | House stance | Rationale |
|---|---|---|
| Large-cap / Nifty 50-100 | **Passive** (index fund/ETF) core, ≤ 10% satellite active only for a scorecard-verified alpha-consistent manager | Large-cap active alpha persistence is weak and expensive net of TER; index cost ~4–20 bps vs active ~70–100+ bps |
| Flexi-cap / multi-cap | **Active**, selectively (2–3 managers, scorecard-screened) | Genuine benchmark-agnostic mandates can add value; but screen hard for closet-large-cap behaviour |
| Mid-cap | **Active**, capacity-capped | Persistent, capacity-constrained alpha exists; cap ticket ≤ 1% of scheme AUM and watch AUM growth quarterly |
| Small-cap | **Active**, tightly capacity-capped, smaller allocation | Highest alpha potential but also highest capacity risk and highest embedded trading-cost drag (~40–45 bps) — size down |
| Factor/smart-beta (quality, low-vol, momentum) | **Passive index fund**, used as the "structured active" substitute | Delivers persistent factor premia at 20–40 bps vs 70+ bps for a discretionary equivalent; momentum funds carry the highest embedded rebalancing cost (~25 bps) of the factor set — size accordingly |

### 2.3 Active-MF hurdle rate (does the manager earn their fee?)

```
Required net alpha (bps p.a.) = (Active TER − comparable index TER)
                                + (embedded fund-level churn-cost differential)
                                + margin of safety (100 bps)
```
Worked example (mid-cap active vs a mid-cap index fund, ₹35 Cr sleeve): TER gap 60 bps + churn-cost gap 30 bps + 100 bps margin = **190 bps p.a. hurdle**, i.e. the manager must beat the passive alternative by ≈ ₹66.5 lakh/year on this sleeve before the active bet is judged to be earning its keep. Track trailing-3Y realised alpha against this hurdle at every semi-annual re-score.

---

## 3. Third-Party PMS Strategies

### 3.1 Due-diligence checklist and scoring

| Check | What to verify | Data source |
|---|---|---|
| APMI-disclosed firm TWRR | Strategy-level TWRR, ≥ 3Y history where available, per APMI's Dec-2022 benchmarking circular [21] | APMI performance portal (apmiindia.org) |
| Live vs back-tested | Confirm the disclosed track record is **live client money**, not a model/back-test; APMI mandates an **annual firm-level performance audit** covering all DPMS+NDPMS+IA books combined (SEBI/HO/IMD/IMD-PoD-1/P/CIR/2023/133, 2-Aug-2023) [22] — ask for the audit certificate | Firm's compliance team |
| Benchmark & strategy tagging | Strategy = Equity/Debt/Hybrid/Multi-asset, ≤ 3 APMI-prescribed benchmarks; confirm no benchmark-hop history without exit-load-free client option [21] | Disclosure Document |
| Capacity | AUM in this specific Investment Approach (IA) vs the manager's own stated capacity ceiling; check AUM growth trend (rapid growth post-good-year = capacity risk) | Monthly APMI filing |
| Fee structure | Fixed (25–250 bps), performance (10–20% over hurdle), high-water-mark mandatory [19]; model 3–4 fee scenarios (see §9 table) | Client Agreement / MITC |
| Concentration | Top-10 holdings %, single-stock cap, sector cap vs house limits | Monthly portfolio statement |
| Valuation independence | Confirms use of APMI-empanelled valuation agencies for debt/MM instruments (NSE Indices Ltd, ICRA Analytics, CRISIL) [23] | Valuation policy doc |
| Custodian | SEBI-registered custodian in place, client funds/securities segregated per-client (no pooling) | Custodian confirmation |

**Score:** 8 checks × 12.5 pts; onboard only strategies scoring ≥ 80/100 with **zero red flags** on capacity or valuation independence.

### 3.2 Fee-structure economics (₹500 Cr context, illustrative gross return 15%)

| Structure | Fixed | Perf. | Hurdle | Total fee | Net-of-fee (pre-GST) | Net after 18% GST on fee |
|---|---|---|---|---|---|---|
| Pure fixed | 2.5% | — | — | 2.50% | 12.50% | 12.05% |
| Hybrid, low hurdle | 1.5% | 15% | 10% | 2.25% | 12.75% | 12.35% |
| Hybrid, standard | 1.0% | 20% | 10% | 2.00% | 13.00% | 12.64% |
| Pure performance | 0% | 20% | 8% | 1.40% | 13.60% | 13.35% |

Performance fee is charged strictly on **new gains above the high-water mark** [19] — model every proposed strategy against this table before allocating, and reject any structure charging performance fee without a documented HWM mechanism.

### 3.3 Legal structuring vs the NDPMS mandate, and reporting consolidation

- A third-party PMS allocation is **not** a security the house PM holds in the client's NDPMS account — it is a **separate contractual relationship** between the client and the third-party portfolio manager, with its own separate bank/demat/custodian accounts (SEBI mandates per-client segregation, no pooling). Ionic recommends the allocation size and strategy (subject to client consent, consistent with the NDPMS model), but does not itself exercise trading discretion inside that account — this is what keeps the structure outside the Reg. 24(10) "advice of another entity" prohibition [25] rather than inside it.
- **Consolidation:** pull the third-party PMS's monthly client statement (holdings + TWRR) via a data-sharing agreement (or the client's own statement) and reconcile it into the house TWRR/attribution dashboard as a distinct "asset class = Third-Party PMS, Strategy = X" line, using the third-party's own APMI-reported TWRR as the return series and the house's own weighting logic for blended-portfolio attribution. Do **not** let the third-party PM's reported number silently become "our" alpha — attribute it as pass-through with an explicit selection/monitoring value-add note.

---

## 4. Alternative Investment Funds (Cat II / Cat III)

### 4.1 ODD checklist (score 1–5 per item, flag any ≤ 2)

| Dimension | What to check |
|---|---|
| Manager pedigree & team stability | Track record of key investment personnel across cycles, not just fund since-inception |
| Firm-level AUM & concentration | Single-LP concentration in the fund (avoid > 20% from one family/institution) |
| Fee stack | Management fee (1.5–2.5%), carry (10–20%), hurdle (8–12%), catch-up clause, GST on fees |
| Drawdown/capital-call schedule | Commitment period, capital-call notice period (typically 10–15 business days), penalty for default |
| Lock-in / liquidity terms | Cat I/II: close-ended, **minimum 3-year tenure** from final close, hard lock-in except secondary transfer [10]; Cat III: open or close-ended — open-ended typically carries a **soft lock-in of 1–3 years with exit load** [10] |
| Leverage | Cat III leverage reportedly capped at **~2x NAV with daily reporting to SEBI** post the 2025 amendments — **verify against the current AIF Regulations text before relying on this as a hard limit**, sources conflict on whether this is a blanket cap or a disclosed fund-specific ceiling [11] |
| Valuation independence | Cat I/II: independent valuer every 6 months (or 12 months with 75%-by-value investor consent); Cat III: NAV monthly (open-ended) / quarterly (close-ended), computation independent of the fund-management function [12] |
| Tax structure | Cat I/II pass-through under Sec. 115UB (non-business income taxed in investor's hands, character preserved); Cat III taxed at fund level — LTCG 12.5%+surcharge(cap 15%)+cess, STCG 20%+surcharge+cess, business income at MMR ≈ 42.74% for an indeterminate trust [14] |
| Dematerialisation | All new AIF units must be issued in demat form (2025 amendment) — confirm compliance |

### 4.2 Category economics and sizing at ₹500 Cr

| | Cat II Private Credit | Cat III Long-Short / Market-Neutral |
|---|---|---|
| Typical gross yield/return | 16–20% gross portfolio yield; 12–16% net to investor after fees [13] | Strategy-dependent; historically high-single to low-double digits net |
| Fee stack | 1.5–2.0% mgmt + 10–15% carry over hurdle (blended ≈ 150–200 bps) | 1.5–2.0% mgmt + 15–20% perf. |
| Tax treatment | Pass-through; interest taxed at investor slab (~39% incl. surcharge/cess for top-bracket HNI) [13] | Fund-level tax; effective drag can approach MMR on business income, or 12.5–20% on genuine capital gains if structured/taxed as a determinate trust [14] |
| Minimum ticket | ₹1 Cr per investor (₹25 lakh for fund employees/directors); waived for Accredited Investors [8] | Same |
| Suggested ₹500 Cr sizing | ~5% (₹25 Cr) across 2 managers, ₹10–15 Cr per ticket | ~3–4% (₹15–20 Cr), 1–2 managers |
| Undrawn-commitment drag | Material — a ₹25 Cr commitment drawn over 15 months at a ~5.3pp cash-vs-target yield gap costs ≈ **₹0.83 Cr** in foregone return over the drawdown period (linear-draw approximation) | N/A (typically funded on subscription) |

**Illiquidity budget:** Cat II + Cat III + REIT/InvIT (semi-liquid) together should not exceed **≈ 12–15% of the ₹500 Cr book** given NDPMS's consent-latency constraint on any rebalancing that would require unwinding illiquid sleeves under stress.

### 4.3 Newer AIF structuring options
- **Large Value Funds (LVF):** minimum now ₹25 Cr per accredited investor (cut from ₹70 Cr under the Nov-2025 Third Amendment) [9] — relevant if the client later wants a bespoke single-strategy vehicle rather than a commingled fund.
- **Co-Investment Vehicles (CIV):** Sept-2025 framework lets accredited investors of a Cat I/II AIF co-invest alongside the main fund in a specific deal via a ring-fenced, no-leverage CIV scheme under Reg. 17A [16] — worth using selectively for concentrated conviction ideas sourced through an existing Cat II manager, subject to client accreditation and consent.

---

## 5. Specialized Investment Funds (SIF) — new since April 2025

SIFs sit **between mutual funds and PMS**: a mutual-fund-regulated vehicle (SEBI (MF) Regulations, 1996, as amended) offering PMS-like strategy flexibility at a much lower ticket than PMS's ₹50 lakh floor.

| Feature | Detail |
|---|---|
| Effective date | 1-Apr-2025 (framework issued Feb-2025, clarified further through 2025–26) [17] |
| Minimum investment | **₹10 lakh per investor, at the PAN level across all SIF strategies of one AMC** (not per strategy); waived for Accredited Investors [17] |
| AMC eligibility | ≥ ₹10,000 Cr average AUM for 3 years, or an alternate CIO/fund-manager-experience route |
| Strategy categories | Equity-oriented, Debt-oriented, Hybrid — including named long-short variants (equity LS, sector-rotation LS, debt LS, hybrid LS, active-asset-allocator LS, etc.) |
| Derivative/short exposure | Up to **25% of net assets** in unhedged short exposure via exchange-traded derivatives (not just hedging/rebalancing) [17] |
| Redemption | Daily to quarterly depending on strategy, notice period up to ~15 working days |
| Market growth (approx.) | AUM ≈ ₹2,010 Cr (Oct-2025) → ≈ ₹9,711 Cr (Feb-2026) → ≈ ₹13,814 Cr (May-2026); hybrid long-short strategies ≈ 76% of total SIF AUM [17] — this is still a **small, young category**: treat as tactical/satellite, not core, until 2–3 years of live track record accumulate |

### 5.1 SIF vs Cat III AIF — post-tax comparison (gross return 12%, illustrative)

| | Cat III AIF | SIF |
|---|---|---|
| Fee | ≈1.75% + 15% over 10% hurdle ≈ 1.75%+0.30% = 2.05% (worked: net-of-fee ≈ 9.95%) | ≈1.25% BER-style fee (net-of-fee ≈ 10.75%) |
| Tax | Fund-level, blended ≈ 28% (mix of LTCG/STCG/MMR exposure) → net ≈ 7.16% | Investor-level equity-fund taxation, LTCG 12.5% → net ≈ 9.14% |
| **Post-tax, post-fee gap** | — | **≈ +1.98 percentage points** in the SIF's favour on this illustrative return, ≈ ₹39.6 lakh/yr on a ₹20 Cr ticket |

**Rule:** for any strategy available in **both** a SIF and a Cat III AIF wrapper at comparable quality, **default to the SIF** on post-tax economics and the far lower ₹10 lakh ticket friction — reserve Cat III AIF allocation for strategies (e.g., higher-leverage, more illiquid, longer track record) not yet offered in SIF form. Given the category's youth, cap combined SIF exposure at ≈ 3–5% of AUM until 2027–28 track records mature.

---

## 6. Direct Equity — the NIFTY-750 Scorecard Sleeve

### 6.1 Sizing framework
```
Base weight (%)   = 4% + 2% × (Score − 70) / 30   [capped at 6%]
Liquidity cap (%) = min( 20% × 5-day ADV × 5 days / Sleeve size , 8% )
Final weight      = min(Base weight, Liquidity cap)
```
(20% of ADV per day, over a 5-day execution window, is the standard "we will not move the stock" constraint; consent latency argues for using a **trailing** ADV, not a spot one.)

| Score | 5-day ADV (₹ Cr) | Base wt | Liquidity cap | Final wt | ₹ Cr (₹40 Cr sleeve) | bps of AUM |
|---|---|---|---|---|---|---|
| 85 | 60 | 5.0% | 8.0% (uncapped) | 5.0% | 2.00 | 40 |
| 72 | 25 | 4.1% | 8.0% | 4.1% | 1.65 | 33 |
| 78 | 8 | 4.5% | 8.0%* | 4.5% | 1.81 | 36 |

*At small ADV the liquidity formula can bind well below 8% for larger sleeves — always run the sleeve-specific number, not the illustrative cap.

### 6.2 Portfolio construction rules
- **25–35 names** (30 as base case): enough for single-name idiosyncratic diversification, few enough that the NIFTY-750 quality/growth/value/momentum/macro composite score remains a meaningful differentiator per name.
- **Sector cap:** house rule ≤ 25% per NIC/GICS sector (tighter than the composite benchmark's own sector weight + 5pp, whichever is lower).
- **Entry/exit rules synced to monthly cadence:** a name enters the recommendation list only if it has cleared the composite-score threshold for **2 consecutive monthly scorecard runs** (avoids one-month score noise triggering a churn that then needs a consent round-trip); exits are immediate on a **hard trigger** (rating downgrade below investment grade equivalent proxy, accounting red flag, promoter-pledge spike) even mid-month, escalated as an out-of-cycle consent request — everything else queues to the next monthly cycle.
- **Overlap control vs active MFs:** run a monthly overlap report (% of direct-equity sleeve names also held in the top-20 of each active MF the book holds); flag any name where combined direct + look-through MF exposure exceeds the house single-stock cap, and prefer trimming the **direct** position first (it is the cheaper lever to adjust without disturbing the active manager's own book).

---

## 7. Fixed Income

### 7.1 Direct vs fund — decision rule

| Consideration | Favours **direct** G-sec/SDL/corp bond | Favours **fund/index/target-maturity** |
|---|---|---|
| Ticket size per issue | ≥ ₹10–15 Cr (achievable diversification even direct) | < ₹10 Cr per issuer |
| Intended hold | To maturity, laddered | Rolling/duration-managed |
| Issuer count achievable | ≥ 8–10 distinct issuers within the sleeve | Fewer — diversification needs a fund wrapper |
| Tax view | Slab-taxed coupon is unavoidable either way for direct debt; a **listed target-maturity ETF's LTCG at 12.5% (>12m)** vs a bond's slab-taxed coupon can create a meaningful after-tax gap — **model faces genuine complexity here and should be reviewed by tax counsel per client**, flagged as unverified planning position, not a house-wide rule | Sub-₹10 Cr issuer tickets, or when the manager's stated capacity to source at scale is the limiting factor |

- **G-sec/SDL:** use **RBI Retail Direct** for primary auctions (free, no distributor fee, T+1 settlement) [27] and **NDS-OM** (via a bank/PD) for secondary-market trades, which settle near-real-time to T+1 [27]. At ₹500 Cr this account almost certainly needs a custodian/bank NDS-OM/CSGL relationship rather than the retail-facing Retail Direct portal for size.
- **Corporate bonds:** rating floor **AA and above** for the core sleeve (BBB carve-out, if any, only via a dedicated high-yield AIF, never direct); single-issuer cap ≤ 3% of the fixed-income sleeve; **≥ 10% of secondary corporate-bond trades by value must go through the RFQ platform** — this is a regulatory floor for PMS, not a house choice, rolling 3-month basis [26].
- **Spread targets (2026, approx.):** AAA PSU 10–60 bps over G-sec, AAA private NBFC 50–140 bps, AA 100–260 bps [28]; 10-year AAA-vs-G-sec spread ≈ 2.21%, 3-year ≈ 1.11% (as of 15-Aug-2026) [28]. Use these as the entry-spread floor below which a corporate-bond purchase needs an explicit override rationale.
- **Duration policy:** keep the core sleeve duration within ±1 year of the house fixed-income benchmark duration; use target-maturity funds/ETFs (Bharat Bond series, Nifty-SDL-dated indices) to express curve views without single-issuer risk — SDL index yields were running ≈ 5.96–5.99% on ~1.5-year maturity buckets through 2025–26 [30].

---

## 8. Gold/Silver, REITs/InvITs, International

- **Gold:** **Sovereign Gold Bonds are discontinued for new issuance** since Feb-2024, and Budget 2026 further restricted the maturity capital-gains exemption to original PRIMARY subscribers who hold to the full 8-year maturity — secondary-market SGB buyers get **no** capital-gains exemption even if held to maturity [6]. **Use Gold ETF via the AP/creation-unit route for any new gold allocation** — the SGB era for this mandate is effectively over except for legacy positions the client may already hold. Gold ETF AUM industry-wide grew ~191–195% YoY to ≈ ₹1.71–1.85 lakh Cr through Mar–May 2026 [4][5], confirming ample liquidity for our ticket sizes.
- **Silver:** volatility comparable to Indian equities (~26–27% SD, drawdowns to ~54%) [historical, approx.] — size as a **tactical**, not core, sleeve (house guide ≤ 1–2% of AUM), and expect wider ETF spreads than gold.
- **REITs/InvITs:** the Nifty REITs & InvITs index carried a ~2.17% dividend yield with 1-year CAGR ≈ 22% as of Apr-2026 [7]; individual constituents range from Embassy REIT (~6.5% distribution yield) to IndiGrid (~9–10%) [7]. **Taxation is multi-component and must be read off each unit's own Form 64B statement** — interest and (per an amendment effective 1-Apr-2026) most dividend distributions are treated differently, rental income and "repayment of debt" distributions have their own separate treatment, and unit-level capital gains taxation and the applicable holding-period threshold for business-trust units should be **independently verified against the current Section 115UA framework before being relied on for portfolio tax planning** — this is flagged explicitly as an **open item for tax counsel**, not a settled house number.
- **International:** three routes — (a) India-listed international ETFs/FoFs, subject to the industry-wide **USD 7 bn** SEBI overseas-investment cap (with a USD 1 bn ETF sub-cap) that has been running near-exhausted through 2026, causing intermittent subscription pauses at several AMCs [35]; (b) **GIFT City** structures (IFSC-based feeder funds), which sit outside the domestic MF overseas cap; (c) client-level **LRS** (Liberalised Remittance Scheme) direct overseas investment, which is a client (not PM) instrument and would need to sit outside the NDPMS account as a separate reportable holding. **House default:** try the domestic FoF/ETF route first; when subscriptions are paused, move to GIFT City feeders for size, and treat LRS as a client-directed parallel holding to be captured in consolidated reporting only, not as an NDPMS-executed instruction.

---

## 9. Total Cost of Ownership — ₹500 Cr Moderate-model illustration

TCO = TER/management fee + embedded fund-level trading cost + our own transaction cost + tax drag + illiquidity/consent-latency cost, all expressed in bps of NAV and ₹ Cr/yr. (Full computation in `sel/tco.py`; figures below are the base run.)

| Sleeve | Wt % | ₹ Cr | TER/mgmt (bps) | Embedded fund cost (bps) | Our txn cost (bps) | Tax drag (bps) | Illiquidity/latency (bps) | **Total (bps)** | **₹ Cr/yr** |
|---|---|---|---|---|---|---|---|---|---|
| Nifty 50/100 ETF+index fund | 22 | 110.0 | 8 | 3 | 2.0 | 22 | 3 | **38** | 0.42 |
| Factor index funds (quality/low-vol/momentum) | 10 | 50.0 | 30 | 25 | 2.0 | 45 | 3 | **105** | 0.52 |
| Active mid-cap MF (direct) | 7 | 35.0 | 70 | 35 | 1.0 | 26 | 2 | **134** | 0.47 |
| Active small-cap MF (direct) | 3 | 15.0 | 80 | 45 | 1.0 | 26 | 2 | **154** | 0.23 |
| Direct equity (NIFTY-750 scorecard) | 8 | 40.0 | 0 | 0 | 12.6 | 155 | 8 | **176** | 0.70 |
| International FoF/ETF | 5 | 25.0 | 65 | 15 | 3.0 | 30 | 10 | **123** | 0.31 |
| Short-duration/money-market fund | 3 | 15.0 | 25 | 5 | 0.0 | 257 | 0 | **287** | 0.43 |
| Target-maturity AAA/SDL funds/ETFs | 11 | 55.0 | 18 | 5 | 1.0 | 269 | 0 | **293** | 1.61 |
| 10-yr G-sec (direct) | 6 | 30.0 | 0 | 0 | 3.0 | 273 | 0 | **276** | 0.83 |
| AA corporate credit (via funds) | 4 | 20.0 | 70 | 10 | 1.0 | 320 | 0 | **401** | 0.80 |
| Arbitrage fund (cash sleeve) | 2 | 10.0 | 35 | 10 | 1.0 | 1,914 | 0 | **1,960** | 1.96 |
| Gold ETF (AP route) | 5 | 25.0 | 60 | 5 | 2.0 | 1,196 | 2 | **1,265** | 3.16 |
| Silver ETF | 1 | 5.0 | 55 | 10 | 3.0 | 2,542 | 5 | **2,615** | 1.31 |
| Listed REITs/InvITs | 4 | 20.0 | 0 | 0 | 6.0 | 1,624 | 5 | **1,635** | 3.27 |
| Cat II private credit AIF (×2) | 5 | 25.0 | 175 | 0 | 0.0 | 468 | 40 | **683** | 1.71 |
| Cat III LS AIF / SIF hybrid | 4 | 20.0 | 190 | 30 | 0.0 | 308 | 15 | **543** | 1.09 |
| **Weighted portfolio total** | **100** | **500.0** | **41** | **11** | **3** | **317** | **5** | **376 bps** | **18.82** |

Add the PM's own fee layer: a 0.30% fixed fee ≈ ₹1.50 Cr + 18% GST ≈ ₹0.27 Cr + ~12 bps opex ≈ ₹0.60 Cr → **₹2.37 Cr (47 bps)**. **All-in TCO ≈ 424 bps ≈ ₹21.2 Cr/yr on ₹500 Cr.**

**Read:** the **tax-drag line dominates** the TCO at 317 of 376 bps pre-PM-fee — this is a portfolio-construction signal, not just a cost-accounting one: every instrument choice above (arbitrage vs liquid, ETF vs SGB, Cat III AIF vs SIF, direct bond vs fund) should be re-examined first through this tax lens, because non-tax TCO (TER + embedded cost + our txn cost + illiquidity) is only **60 bps (₹3.0 Cr/yr)** — the manager-selection and execution-quality work earns real money, but the biggest single lever available is **instrument-tax-form selection**, not manager alpha or spread-shaving.

### 9.1 Fee-layering rules — what the PM may charge on each wrapper

| Wrapper | PM management fee on this sleeve | Distribution fee | Notes |
|---|---|---|---|
| MF (any) | Charged only at the PM's overall portfolio-fee rate — **no separate layer**; must be a **direct plan**, zero distribution fee to the PM [19] | **Prohibited** [19] | Double-charging (PM fee + regular-plan trail) is exactly what the direct-plan mandate exists to prevent |
| ETF | Same — PM's overall fee only | N/A (no distributor in an ETF) | — |
| 3rd-party PMS | PM's own portfolio fee on the **allocation decision and monitoring**, not a second full management fee on top of the third-party PM's own fee (that fee is charged by the third-party PM directly to the client's separate account) | N/A | Avoid economically "fee on fee" without disclosed value-add |
| AIF (Cat II/III) | PM's fee at portfolio level only; AIF's own management/carry fee is separate and charged by the AIF | N/A | Disclose the AIF's full fee stack in the MITC illustration |
| SIF | Same principle as MF — PM's own fee only, SIF's BER-style fee is separate | N/A | — |
| Direct equity/bonds | PM's fee only; brokerage charged **at actuals** [19] | N/A | — |

---

## 10. CAN / SHOULD / AVOID — condensed

**CAN (regulatorily permitted, fits NDPMS):** direct-with-AMC ETF dealing ≥₹25 Cr; index funds/factor funds as passive/structured-active core; capacity-screened active MFs via direct plans; third-party PMS as a separate consented account; Cat II/III AIF and SIF allocation (accredited-investor exemptions where applicable); direct equity via the NIFTY-750 scorecard; RBI Retail Direct/NDS-OM for G-secs; RFQ-routed corporate bonds; Gold ETF (AP route); REITs/InvITs; GIFT City/LRS for international when domestic caps bind.

**SHOULD (do in first 6 months):** build the AMC-direct ETF execution relationship; formalise the active-MF and PMS scorecards into the monthly recommendation-pack workflow; size the illiquid (AIF/REIT) sleeve to the 12–15% cap; stand up the target-maturity-fund ladder; build the direct-equity liquidity-capped sizing tool; wire third-party PMS statements into the house TWRR dashboard.

**AVOID:** new SGB purchases (discontinued, and the tax-exemption carve-out no longer follows secondary buyers) [6]; Cat III AIF exposure to strategies also available in cheaper/more tax-efficient SIF form once the SIF has an adequate track record; any structure where the PM's own fee is layered on top of a regular (non-direct) MF plan; outsourcing trade sizing/timing to a third-party PMS or vendor beyond model-level advice (2026 enforcement risk) [25]; over-sizing silver given its equity-like volatility with weaker liquidity than gold.

---

## Sources consulted

[1] SEBI ETF direct-with-AMC ₹25 Cr threshold — https://www.business-standard.com/amp/india-news/after-two-deferments-exchange-route-compulsory-for-sub-rs-25-cr-etf-deals-123050100756_1.html
[2] Nifty BeES AUM/creation unit — https://etf.nipponindiaim.com/Funds/details/14 ; https://www.tickertape.in/etfs/nippon-india-nifty-50-bees-etf-NBES
[3] NSE Nifty 50 impact cost — https://www.nseindia.com/static/products-services/indices-nifty50-index
[4] ETF industry AUM/turnover, gold ETF AUM growth — https://www.businesstoday.in/personal-finance/investment/story/can-gold-etfs-sustain-record-inflows-after-aum-surged-191-in-fy26-528200-2026-04-30
[5] Gold/silver ETF inflows FY26 — https://www.indmoney.com/blog/mutual-funds/gold-silver-etf-inflows-fy26-india
[6] SGB discontinuation and Budget 2026 tax change — https://goldenpi.com/blog/bond-news/sovereign-gold-bond-scheme-discontinued-for-new-issues/ ; https://www.taxscan.in/top-stories/sovereign-gold-bond-tax-rules-for-itr-ay-2026-27-interest-redemption-capital-gains-and-reporting-1448954
[7] REIT/InvIT index yield and 2026 dividend-tax amendment — https://www.niftyindices.com/Factsheet/Factsheet_REITs_InvITs.pdf ; https://www.business-standard.com/amp/finance/personal-finance/reit-invit-dividend-tax-break-experts-explain-what-changes-and-the-catch-126080701364_1.html
[8] AIF minimum ticket / accredited investor thresholds — https://www.incorpx.io/blog/aif-registration-sebi-categories-india ; https://www.business-standard.com/amp/article/markets/what-are-accredited-investors-the-eligibility-criteria-and-benefits-121022500517_1.html
[9] Large Value Fund ₹25 Cr (Nov-2025 Third Amendment) — https://elementone.fund/sebi-aif-regulations-2026-guide/
[10] AIF tenure/lock-in by category — https://treelife.in/finance/alternative-investment-funds-in-india/ ; https://www.pmsaifworld.com/aif-category-3/
[11] Cat III leverage cap (approx., verify) — https://elementone.fund/sebi-aif-regulations-2026-guide/
[12] AIF valuation frequency — https://treelife.in/finance/aif-valuation-in-india/
[13] Cat II private credit yields/tax — https://www.ey.com/en_in/insights/strategy-transactions/onwards-and-upwards-a-positive-outlook-for-private-credit-in-india ; https://rurashfin.com/india-private-credit-market-2026-investor-risks/
[14] Cat III AIF taxation, MMR — https://www.finnovate.in/learn/blog/aif-taxation-india
[15] Finance Act 2025, Sec. 2(14) Cat I/II capital-asset clarification — https://www.lexology.com/library/detail.aspx?g=a8345261-0ec2-4031-b2e1-211c964e83cd
[16] AIF Co-Investment Vehicle framework (Sept-2025) — https://corporate.cyrilamarchandblogs.com/2025/09/beyond-cpms-route-sebi-unlocks-co-investment-schemes-for-aifs/
[17] SIF framework — https://www.impriindia.com/insights/policy-update/a-new-asset-class/ ; https://groww.in/blog/specialised-investment-funds ; https://upstox.com/news/business-news/financial-regulations/sebi-framework-for-specialized-investment-funds-si-fs-10-lakh-entry-sector-caps-and-more/article-149031/ ; https://www.business-standard.com/markets/news/sebi-clarifies-regulatory-framework-for-specialized-investment-funds-125040901078_1.html
[19] SEBI PMS fee/expense circular 2020 — https://www.business-standard.com/amp/article/markets/sebi-puts-expense-cap-on-pms-providers-lays-down-performance-standards-120021301918_1.html
[20] PMS Master Circular consolidation 16-Jul-2025 — https://www.lexibox.in/pms/master-circular-for-portfolio-managers-2025/
[21] APMI TWRR/benchmarking circular Dec-2022 — https://taxguru.in/sebi/performance-benchmarking-reporting-performance-portfolio-managers.html
[22] APMI firm-level performance audit Aug-2023 — https://taxguru.in/sebi/sebi-circular-portfolio-managers-firm-level-performance-data-audit.html
[23] APMI empanelled valuation agencies — https://www.gktoday.in/sebi-new-benchmarking-norms-for-portfolio-managers/
[24] PMS unlisted-securities 25% cap — https://www.business-standard.com/amp/article/markets/pms-players-had-to-change-plans-after-restrictions-on-unlisted-securities-120010700492_1.html
[25] PM prohibited from investing on another entity's advice; 2026 outsourcing enforcement — https://corporate.cyrilamarchandblogs.com/2026/06/sebi-order-penalises-outsourcing-of-core-functions-structuring-lessons-for-asset-management-industry/
[26] PMS 10% RFQ corporate-bond rule — https://www.business-standard.com/amp/article/markets/pms-to-undertake-10-transactions-in-corp-bonds-via-rfq-platform-sebi-121120901140_1.html
[27] RBI Retail Direct / NDS-OM — https://primeinvestor.in/reports/buy-g-secs-on-rbi-retail-direct-platform/
[28] AAA/AA credit spreads 2026 — https://indiamacroindicators.co.in/economic-indicators/10-year-credit-spread-aaa-rated-bonds-g-sec
[29] Bharat Bond / Nifty 10Y G-sec ETF returns — https://www.valueresearchonline.com/funds/41060/bharat-bond-etf-april-2031/
[30] SDL yield — https://www.niftyindices.com/Factsheet/Nifty_SDLSep2026V1Index_Factsheet.pdf
[31] SEBI MF Regulations 2026 (BER/TER overhaul) — https://www.businesstoday.in/mutual-funds/story/exiting-mutual-funds-may-get-cheaper-as-sebi-cuts-maximum-exit-load-cap-to-3-547787-2026-08-07
[35] SEBI overseas MF USD 7bn cap — https://www.oquilia.com/news/sebi-international-fund-overseas-investment-limit-7bn

*(Note: several primary SEBI/APMI PDF circulars were blocked by the network egress proxy during research; facts drawn from them are sourced instead via secondary summaries of those same circulars (taxguru, business-standard, lexibox, etc.) as cited above, and higher-stakes figures are flagged "approx./verify" in the text where the underlying circular text could not be directly confirmed.)*
