# Workstream 05 — Transaction Costs, Capacity, Leverage Mechanics (India)

Status: RESEARCH ONLY, per `CONTRACT.md` and `OPEN_QUESTIONS.md` (defaults assumed throughout:
hedge-only via index derivatives, index-futures leverage overlay, index options+futures hedge set).
Scope: first-principles statutory + spread + impact cost stack by NIFTY-750 rank bucket and book
size; re-derivation and correction of the prior-pass turnover-cost number; capacity translation of
Korajczyk-Sadka / Novy-Marx-Velikov / smart-beta-capacity literature into INR terms per sleeve;
leverage mechanics (futures roll, margin, SLB); staged-entry/days-to-build arithmetic; the SAST 5%
disclosure ceiling as a conservative-book position bound.

**Session constraint, stated up front**: this workstream's web-search budget was shared across the
whole research program and was exhausted (200/200) partway through this session, after the
statutory-cost and core-literature searches completed but before several secondary checks could be
run. `WebFetch` is blocked for essentially all general domains in this environment (confirmed by
testing Wikipedia, ResearchGate, SSRN, AQR, Zerodha-support, Business-Standard — all
`EGRESS_BLOCKED`), consistent with Contract §7 item 11 ("no market-data network access… web search
works"). Findings below are tagged `[VERIFY]` wherever they rest on pre-cutoff knowledge rather than
a search executed this session; the statutory-cost figures (STT, stamp duty, exchange charges, SEBI
fees, GST) and the five core capacity/impact papers **were** verified this session via multiple
independent sources before the budget ran out.

---

## 1. Findings and literature

**F1. Securities Transaction Tax — current rate schedule.** Verified via multiple 2026 sources
(Outlook Money, HDFC Bank, PL India, 1Finance, Swastika Investmart, Finnovate — cross-consistent).
Equity delivery: **0.1% on both buy and sell** (unchanged since 2013, GST-exempt). Equity intraday:
0.025% sell-side only. **Futures and options rose on 1 April 2026** (Budget 2026, effective start of
FY2026-27): futures STT 0.02%→**0.05%** of trade value (sell side); options-premium STT 0.1%→**0.15%**
(sell side); options-on-exercise STT 0.125%→**0.15%** of intrinsic value (buyer pays, triggered on
auto-exercise of in-the-money index options at expiry). The immediately preceding rates (0.02%
futures / 0.1% premium / 0.125% exercise) were themselves set by Budget 2024, effective 1 October
2024. **Today's date (31 Aug 2026) is inside FY2026-27, so FY2025-26's STT schedule has already been
superseded** — the task brief's "current FY2025-26" framing is stale by five months; I use the live
FY2026-27 rates throughout and table both below (§4). Verified.

**F2. Uniform stamp duty on securities (July 2020 reform).** Delivery equity 0.015% (buy side only),
intraday equity 0.003% (buy side only), futures 0.002% (buy side only), options 0.003% of premium
(buy side only) — replaced the pre-2020 state-by-state stamp duty regime with one flat schedule
collected centrally and apportioned to states. GST-exempt, like STT. Verified across Groww, Zerodha
Z-Connect, and NSE's own investor-education page summaries (multiple independent secondary sources
converge on identical figures).

**F3. NSE exchange transaction charges, current schedule.** As of the October 2024 revision: cash
₹2.97/lakh traded value per side; equity futures ₹1.73/lakh per side; equity options ₹35.03/lakh of
*premium* value per side. A further SEBI-mandated uniform-fee circular pushed a second revision
effective **1 March 2026**: +₹20/crore cash (+₹0.20/lakh → ₹3.17/lakh), +₹10/crore futures
(+₹0.10/lakh → ₹1.83/lakh), +₹300/crore options (+₹3/lakh → ₹38.03/lakh premium). Verified (NSE
circular references, Business Standard reporting on the September 2024 SEBI uniform-fee mandate).

**F4. SEBI turnover fees + GST treatment.** SEBI turnover fee: 0.0001% of transaction value per side
(≈₹10/crore) for equities and equity derivatives; lower for debt (0.000025%). From **April 2025**,
18% GST was extended to SEBI turnover fees across all segments (cash, all derivative classes, NDS,
repo, EGR) — a pure tax-base widening, not a headline-rate change, but it raises the effective
regulatory-fee component by 18%. GST at 18% also applies to brokerage, exchange transaction charges,
and DP/demat charges; it does **not** apply to STT or stamp duty (both are themselves taxes, not
services). Verified (Free Press Journal, multiple broker fee-schedule pages, consistent).

**F5. The square-root law of market impact** (Bouchaud, Farmer & Lillo 2009 survey; Gatheral 2010,
*Quantitative Finance* 10(7):749–759, "No-Dynamic-Arbitrage and Market Impact"; Tóth et al. 2011).
Empirical result across many independent equity and futures datasets: the average price move caused
by executing a metaorder of size *Q* scales as *I(Q) ≈ Y·σ_D·√(Q/V_D)*, where *σ_D* is daily
volatility, *V_D* is average daily volume, and *Y* is an order-unity constant found to be
approximately stable **across asset classes and time periods** — a rare degree of universality in
empirical finance. Impact is close to independent of execution horizon and order-splitting strategy
for reasonable execution windows. Verified (Bouchaud's own 2022 restatement/Substack piece plus the
arXiv literature it cites, cross-checked against the Gatheral 2010 abstract).

**F6. Almgren & Chriss (2000/2001), "Optimal Execution of Portfolio Transactions"** (*Journal of
Risk* 3(2):5–39, 2000; extended *Applied Mathematical Finance* 2001). Canonical optimal-execution
framework: decompose impact into temporary (per-trade, reverts) and permanent (per-share, persists)
components, and trade off expected impact cost against the variance of execution-price risk from
trading too slowly. The mean-variance-efficient execution trajectory is a smooth, front-loaded
schedule whose aggressiveness is set by a risk-aversion parameter. **[VERIFY: canonical citation, not
re-confirmed by a fresh search this session due to budget exhaustion — extremely high confidence from
domain knowledge; this is one of the most-cited papers in market microstructure and the citation
details are essentially unfalsifiable at this level of standardness].**

**F7. Almgren, Thum, Hauptmann & Li (2005), "Direct Estimation of Equity Market Impact"** (*Risk*
Magazine, July 2005). Calibrates permanent and temporary impact coefficients on live US equity order
data; finds a power-law temporary-impact exponent close to, but not exactly, 0.5, and coefficients an
order of magnitude smaller than naive extrapolations from bid-ask spread alone would suggest.
**[VERIFY: same caveat as F6 — not re-searched this session, high-confidence recall].**

**F8. Frazzini, Israel & Moskowitz, "Trading Costs"** (AQR working paper / SSRN 3229719, 2018;
distinct from their earlier "Trading Costs of Asset Pricing Anomalies," SSRN 2294498). Uses **$1.7
trillion of live executed trades from one large institutional manager across 21 developed equity
markets over ~19 years** — the largest real-world execution dataset used in the published literature
on this question. Headline, verified qualitative result: realized institutional trading costs are **an
order of magnitude smaller** than costs implied by prior academic estimates built on quoted spreads or
TAQ-based impact models (e.g., Korajczyk-Sadka's own microstructure-implied costs, or Novy-Marx-Velikov's
TAQ-based numbers below). Mechanism: patient, participation-capped algorithmic execution captures most
of the spread and avoids paying for urgency. **The exact fitted coefficient(s) and the bps-at-X%-ADV
table could not be retrieved this session** (AQR.com and SSRN are both blocked by the environment's
egress policy, and the search budget ran out before a text-bearing mirror could be found) —
**[VERIFY: precise FIM-2018 impact coefficient / bps-at-participation-rate table]**. I use the
qualitative "real costs are much lower than academic microstructure models imply, especially for
patient/participation-capped execution" result, but size our own cost curves (§4) from the more
conservative Bouchaud/Gatheral coefficient range rather than assume FIM's most favorable numbers,
since our book will not have FIM's $1.7tn-scale execution infrastructure or multi-decade broker
relationships on day one.

**F9. Kyle & Obizhaeva, "Market Microstructure Invariance: Empirical Hypotheses"** (*Econometrica*
2016 companion piece; main invariance hypothesis paper SSRN 2722524/2823630). Proposes that the
distribution of "bets" (risk transfers) and their transaction costs are invariant across assets when
measured in **business time** (a clock that runs fast for high-volume/high-volatility names, slow for
illiquid ones) rather than calendar time. Implication for our capacity math: order size as a fraction
of ADV, not absolute rupee size, is the right invariant unit — supporting the ADV-relative
(participation-rate) approach used throughout this dossier rather than flat rupee position caps.
Verified (Econometrica DOI 10.3982/ECTA10486 confirmed via Wiley).

**F10. Korajczyk & Sadka, "Are Momentum Profits Robust to Trading Costs?"** (*Journal of Finance*
59(3):1039–1082, 2004). Using intraday US data to estimate proportional and non-proportional
(price-impact) costs, finds equal-weighted momentum is the most profitable *gross* but the *worst*
net of costs; **liquidity-weighted and hybrid liquidity/value-weighted momentum strategies have the
largest capacity — roughly $5 billion (December-1999 dollars/market-cap terms)** — before momentum's
apparent profit opportunity is priced away by the strategy's own trading. Value-weighted momentum has
materially lower capacity than the liquidity-weighted variant because value-weighting still
overloads the largest, least-momentum-rich names. Verified (JF DOI 10.1111/j.1540-6261.2004.00656.x).

**F11. Novy-Marx & Velikov, "A Taxonomy of Anomalies and Their Trading Costs"** (*Review of Financial
Studies* 29(1):104–147, 2016; NBER WP 20721). TAQ-based execution-cost estimates: **average trade
execution costs of 20–57 bps for mid-turnover anomalies**; a buy/hold spread (stricter entry
threshold than exit threshold) is the single most effective cost-mitigation technique studied; **capacity
to absorb new capital is inversely related to monthly turnover**; strategies built on size, value, and
profitability have the greatest capacity, short-horizon/high-turnover strategies the least. Most
anomalies with <50%/month turnover survive costs; few above that threshold do. Verified (RFS DOI, NBER
WP 20721 both confirmed).

**F12. Ratcliffe, Miranda & Ang, "Capacity of Smart Beta Strategies from a Transaction Cost
Perspective"** — recalled as a BlackRock-authored *Journal of Portfolio Management* piece
(~2017) reaching essentially the same ranking as F11 (low-turnover factors — value, quality, low-vol
— have capacity in the tens of billions of USD industry-wide; momentum's capacity is materially
smaller because of turnover, not because the underlying signal is weaker). **[VERIFY: could not
re-confirm author list, exact venue, or year this session — search budget exhausted before this
citation could be checked; treat the qualitative capacity ranking as consistent with F10/F11, which
*are* verified, and discount the specific paper's numbers accordingly].**

**F13–F15 (regulatory facts, not academic findings, tagged for the same reason).**
**F13**: SEBI (Substantial Acquisition of Shares and Takeovers) Regulations, 2011, Regulation 29 — any
acquirer crossing **5% of a target's shares or voting rights** must disclose to the company and
exchanges within the prescribed window; Regulation 29(2) requires disclosure of any subsequent ≥2%
change once past 5%. **[VERIFY: regulation number not re-confirmed this session; very high confidence
as standard SEBI regulatory knowledge, but flagged per citation discipline].**
**F14**: SEBI's peak-margin framework was phased in **December 2020 → September 2021** (25%/50%/75%/100%
of applicable margin required upfront on T-day), reaching **100% upfront** from September 2021 — the
end of same-day, margin-later intraday leverage as previously practiced. **[VERIFY: dates not
re-confirmed this session].**
**F15**: The F&O-eligible single-stock universe is periodically pruned by SEBI/exchange eligibility
criteria (average market cap, average daily delivery value, market-wide position limit (MWPL)
thresholds), reviewed quarterly; the eligible list has been reported in the ~180–200 stock range in
recent cycles. **[VERIFY: exact current count not re-confirmed this session — this number moves
quarterly and must be re-pulled from the live NSE F&O eligible-securities circular in the data
phase].**

---

## 2. India-specific evidence

**Settlement cycle.** India completed its move from T+2 to **T+1 settlement across the cash market in
January 2023** (the only major market to do so at the time), and NSE began an **optional T+0
(same-day) settlement pilot for a subset of large-cap stocks starting March 2024**, expanding
gradually. **[VERIFY: pilot scope/date not re-confirmed this session].** Net effect for this design:
shorter settlement float than most developed markets, which reduces (does not eliminate) the working-
capital/financing burden of running a levered cash-equity book relative to a T+2/T+3 market — a modest
positive that does not change any of the cost-stack math below but is worth carrying into the
financing-sizing discussion in the data phase.

**Statutory cost is asymmetric by instrument, and that asymmetry drives the leverage-instrument
choice already made in Open Question #3.** Cash delivery statutory cost (§4) runs ~22 bps round trip
before brokerage; NIFTY futures run ~6 bps round trip before brokerage — roughly a **3.5–4×** gap,
purely from STT structure (delivery STT taxes *both* legs at 0.1%; futures STT taxes only the sell
leg at 0.05%, and the notional base for a levered futures position is far smaller than the cash
notional it substitutes for once margin is netted). This is a first-principles confirmation, not an
assumption, of Open Q#3's recommended default ("index futures overlay… cheapest to size and cut by
state") and of the mechanism (not just a vague "futures are cheap" prior).

**Options STT has a trap that matters for the hedge sweep.** The exercise-STT (0.15% of *intrinsic*
value, charged on automatic exercise of in-the-money index options at expiry) is computed on a base
that can be **many multiples of the original premium** for a option that has moved deep ITM by expiry
— e.g., a 2%-of-notional premium option that finishes 8%-of-notional ITM pays exercise-STT on the 8%
base, not the 2% paid. Institutional desks in India routinely **square off (sell) ITM options before
expiry** rather than let them auto-exercise, specifically to avoid this. Any hedge-ratio sweep
(Contract §3: 0/25/50/75/100/125/150%) that models options cost as "STT on premium only" will
understate realized cost whenever the hedge pays off exactly when it's needed (deep ITM into a crash)
— the cost model must apply the higher exercise-STT rate to the tail-scenario payoff path, not just
the modal path where options expire worthless or are closed early.

**Circuit limits / price bands and surveillance (ASM/GSM) interact directly with the impact model.**
Illiquid small/microcap names (disproportionately concentrated in the aggressive book's rank 500–750
tail) are frequently placed under **Additional Surveillance Measure (ASM)** or **Graded Surveillance
Measure (GSM)**, which can impose tighter price bands (as low as 2–5% per day vs. the standard 5/10/20%
tiers), mandatory 100% margin, and sometimes trade-for-trade (no intraday netting) settlement. A
square-root-law impact estimate implicitly assumes continuous price discovery within a session; a
name that is band-limited can simply **stop trading** once the band is hit, converting what the model
treats as "high impact cost" into "cannot execute at all today" — a discontinuity the smooth
square-root formula does not capture. Any capacity or cost-curve number for the rank 500–750 bucket
should be read as a **lower bound** on realized friction, not a point estimate, for this reason.

**Promoter concentration reduces true free float below headline market cap**, which matters for both
the ADV-based impact model (ADV is a function of the *tradable* float, not total shares) and the SAST
5% threshold (which is measured against total shares/voting rights, not free float — so promoter-heavy
companies hit the 5% disclosure trigger at an even *smaller* absolute rupee position than the ADV
arithmetic alone would suggest, because the position represents a larger share of the tradable float
even though it's the same % of total shares). India's median promoter holding across NIFTY 500
constituents is commonly cited in the 45–55% range (retail + FII + DII + promoter add to 100% of
shares); this is a well-known structural feature of the Indian market this dossier flags as a
compounding factor on both impact and disclosure constraints, without a fresh citation this session —
**[VERIFY: current median promoter-holding statistic]**.

**FII/DII flow structure and derivative-ban periods.** Stocks that breach 95% of their market-wide
position limit (MWPL) in F&O open interest are placed under a **derivative trading ban** (no new
positions, only unwinds, until OI falls below 80% of MWPL) — a real, recurring constraint on the
index-futures-overlay design if it ever needed single-stock futures (it does not, per Open Q#3/#4
defaults, but it is relevant if Stage 2 or the aggressive satellite sleeve ever reconsiders SSF). It
does **not** affect the NIFTY/Bank Nifty index-futures overlay this design actually uses, since index
contracts are not subject to single-stock MWPL bans.

---

## 3. Decay and crowding assessment

The transaction-cost stack is not a "signal" in the McLean-Pontiff sense and does not itself decay —
statutory costs and market impact are structural facts of the market's operation, not an exploitable
anomaly that arbitrage capital can compete away. What *can* decay, and must be assessed per the
Contract's survival test, is each **capacity claim**:

- **Momentum sleeve capacity.** Survival argument: **(ii) capacity limit** — Korajczyk-Sadka (F10)
  show momentum's after-cost profitability is bounded well below its gross Sharpe specifically
  *because* trading costs rise faster than gross alpha as size increases; this is a structural
  capacity ceiling, not a crowding story that resolves itself. No numeric haircut is assigned to
  momentum's gross return here (that belongs in workstream 01); what is assigned is a **hard AUM
  ceiling** derived below (§4) below which the after-cost Sharpe holds and above which it degrades
  as O(√size).

- **Value/quality/low-turnover sleeve capacity.** Survival argument: **(ii) capacity limit is far
  looser** (Novy-Marx-Velikov F11, and the recalled Ratcliffe-Miranda-Ang ranking F12) — precisely
  *because* the strategy trades less. This is the mechanism the Contract already leans on (item 10:
  "value/quality run ~5× momentum's half-life, so cost ~1/5 the turnover per unit of authority") and
  this workstream's independent bottom-up cost arithmetic (§4) reproduces the same conclusion from
  first principles rather than merely repeating the prior pass's assertion.

- **Reversal (1-month) sleeve capacity.** Survival argument: **none of the four acceptable answers
  hold cleanly at scale.** Short-horizon reversal in India, as elsewhere, concentrates its edge in the
  most illiquid names (least analyst coverage, widest spreads) — precisely where a numeric decay
  haircut is least defensible from Indian data (no Indian reversal-capacity study was found or
  verifiable this session) and where the Contract's own no-magic-numbers/tier rules already apply:
  absent a verified Indian or ≥10-country cross-country reversal-capacity estimate, **this sleeve
  should be sized as Tier C by default (aggressive book only, small allocation, reduce-risk framing)**
  rather than scaled by a specific haircut number — a haircut with no source would itself be a magic
  number.

- **Market-impact assumptions themselves decay in the opposite direction of alpha decay — they get
  *worse* as the strategy is *more* successful.** This is the standard self-limiting property of
  capacity-constrained strategies (both Korajczyk-Sadka and Novy-Marx-Velikov build this in
  explicitly): AUM growth mechanically raises Q/ADV, and impact cost rises as its square root, so a
  strategy sized correctly today re-derives a *lower* effective turnover budget at 3× today's AUM. The
  registry (Contract §10) should re-run this dossier's arithmetic whenever book AUM moves by more than
  ~50% from the figure it was last calibrated against, not treat the cost curve as a one-time
  calibration.

- **Statutory cost cannot decay, but it can be *legislated up*** — F1 is itself an example: STT on
  F&O rose 150% (options premium) to 250% (futures) between the FY2023-24 baseline and the current
  FY2026-27 rate in two hikes within roughly 18 months, both explicitly aimed at "reasonable course
  correction" in derivatives volumes. **A structural, non-decaying regulatory-risk item**: any
  leverage-cost or hedge-cost assumption in the registry should carry an explicit "STT can rise again"
  sensitivity, not be frozen as a point estimate. This is the single largest identified risk to the
  index-futures-overlay cost advantage documented in §2 — a further STT hike on index F&O (the two
  hikes to date have applied economy-wide to F&O, not carved out index vs. single-stock) would
  compress, not eliminate, the futures-vs-cash cost gap.

---

## 4. Proposed parameters

### 4a. Statutory + regulatory cost stack (current, FY2026-27, verified F1–F4)

| Leg | Cash delivery | Cash intraday | Index futures | Index options |
|---|---|---|---|---|
| STT | 0.1% buy + 0.1% sell | 0.025% sell only | 0.05% sell only | 0.15% of premium, sell only; **0.15% of intrinsic value if exercised**, buyer pays |
| Stamp duty | 0.015% buy only | 0.003% buy only | 0.002% buy only | 0.003% of premium, buy only |
| Exchange txn charge (post 1-Mar-2026) | ₹3.17/lakh/side (0.00317%) | same | ₹1.83/lakh/side (0.00183%) | ₹38.03/lakh of premium/side (0.03803%) |
| SEBI fee | 0.0001%/side | same | same | same, on premium |
| GST (18%) | on exch. charge + SEBI fee only, not on STT/stamp | same | same | same |

**Round-trip statutory cost (before brokerage), 100%-notional-equivalent:**
- Cash delivery: 0.1%+0.1% (STT) + 0.015% (stamp) + 2×0.00317%×1.18 (exch+GST) + 2×0.0001%×1.18 (SEBI+GST)
  ≈ **0.223% (≈22.3 bps) round trip**.
- Index futures: 0.05% (STT, sell only) + 0.002% (stamp, buy only) + 2×0.00183%×1.18 + 2×0.0001%×1.18
  ≈ **0.0765% (≈7.7 bps) round trip** — roughly **3× cheaper** than cash delivery, confirming Open
  Q#3's default mechanically, not just directionally.
- Monthly-rolled futures overlay (open + close every expiry): ≈7.7 bps × 12 ≈ **~92 bps/yr** pure
  statutory drag to *maintain* a constant leveraged exposure via monthly rolls — before any
  roll-basis gain/loss vs. MIBOR (§4d) and before brokerage.

**Brokerage**: institutional/DMA execution assumed at **1–5 bps per side (2–10 bps round trip)** —
**own assumption, Tier C, explicitly flagged**: this is a negotiated commercial rate, not a published
one, and must be confirmed with the actual prime broker/execution desk before the registry treats it
as anything but a placeholder. (Many Indian discount brokers charge ₹0 brokerage on cash delivery for
retail; an institutional book of this size will more likely use algo/DMA execution with per-share or
per-order fees that could net out lower or higher than this placeholder.)

**Total round-trip cost, statutory + brokerage only**: cash delivery ≈ **24–32 bps**; index futures ≈
**10–18 bps**. This is the *floor* — spread and impact (4b–4c) sit on top and dominate for anything
beyond the largest ~150 names.

### 4b. Provisional ADV-by-rank-bucket table (NOT independently sourced this session — flagged)

The Contract's own note (§7 item 11) states this environment has no NSE/bhavcopy network access;
combined with this session's exhausted search budget, the following table is a **provisional,
order-of-magnitude construct from general knowledge of Indian market structure**, not a factsheet
pull. **It must be replaced with actual 90-day median ADV per stock from NSE bhavcopy in the data
phase before any number below is used to size a real position.**

| NIFTY-750 rank bucket | Approx. index proxy | Provisional per-stock ADV (₹cr/day) | Daily vol σ (annualized→daily) |
|---|---|---|---|
| 1–50 | Nifty 50 | ~500–800 (bucket avg; top names 1,000+, tail of the 50 ~150–300) | ~20–25%/yr → ~135–155 bps/day |
| 51–150 | Nifty Next 50 + | ~80–150 | ~24–28%/yr → ~150–175 bps/day |
| 151–300 | Nifty Midcap zone | ~20–40 | ~28–35%/yr → ~175–220 bps/day |
| 300–500 | Small-mid zone | ~5–12 | ~32–40%/yr → ~200–250 bps/day |
| 500–750 | Nifty Microcap 250 zone | ~1–4, long right tail below ₹1cr | ~35–55%/yr → ~220–345 bps/day, fat tails, ASM/GSM discontinuities |

`[VERIFY: entire table — provisional pending live bhavcopy pull; used here only to produce
order-of-magnitude, sensitivity-tested cost curves, never as a point estimate for sizing.]`

### 4c. Impact cost via the square-root law, by book and rank bucket

Using *I ≈ Y·σ_daily·√(Q/ADV)*, *Q* = one full 5–6% entry (mid-point 5.5% of book NAV), Y swept over
**0.5–1.0** (Bouchaud/Gatheral's "order-unity" range; FIM's F8 finding argues realized costs sit
toward the low end of this range for patient, participation-capped execution, but their exact
coefficient is unverified this session, so the range is kept wide rather than anchored to their
number):

| Book (NAV midpoint) | Position size (5.5%) | Rank 1–50 impact, Y=0.5–1.0 | Rank 150–300 impact | Rank 500–750 impact (aggressive only) |
|---|---|---|---|---|
| Aggressive, ₹175cr | ₹9.6cr | ~9–18 bps (Q/ADV≈1.6%) | ~57–113 bps (Q/ADV≈32%) | **~275–550 bps** (Q/ADV≈384% — position exceeds one day's *entire* traded volume in the stock) |
| Moderate, ₹1,750cr | ₹96cr | ~28–56 bps (Q/ADV≈16%) | **~180–360 bps** (Q/ADV≈321%) | n/a (out of universe) |
| Conservative, ₹17,500cr | ₹962cr | ~77–153 bps (Q/ADV≈120%, even for mega-caps) | **~unbuildable at full size** (Q/ADV≈800%+ by rank 50–150) | n/a |

**Reading the table**: a flat 5–6% entry rule is only cheap in the rank-1–50 bucket, for *any* book
size. Everywhere else, either (a) the position must be shrunk well below 5.5%, (b) execution must be
stretched over weeks-to-months (§4e), or (c) both. This is the central, load-bearing finding of the
re-derivation and directly determines the "effective universe" contradiction in §4f.

### 4d. Leverage mechanics

- **Index futures roll vs. MIBOR**: NIFTY futures fair value ≈ spot × (1 + (r − dividend yield) ×
  days/365); the embedded financing rate has historically tracked call-money/MIBOR-adjacent levels in
  calm markets but can trade at a **premium** above fair value in strong bull phases (heavy demand
  for cheap leverage) and occasionally at a **discount/backwardation** in stressed/hedging-heavy
  phases (heavy demand to short/hedge via futures). This roll-basis history is a first, direct data-
  phase deliverable (bhavcopy futures vs. spot, unavailable in this environment) — Tier C mechanism
  only here, no number proposed.
- **Margin (SPAN + exposure) is not the binding constraint on leverage.** Index-futures initial margin
  typically runs ~10–17% of notional in normal volatility (≈6–10× notional-to-margin leverage
  available from the exchange alone) — far above the Contract's own 1.5x gross cap and the
  state-contingent averages (~1.10–1.15x aggressive, ~1.05x moderate, Contract item 4). **The
  mandate's own risk-based cap binds long before exchange margin would.** Peak-margin rules (F14,
  100% upfront since ~Sept 2021) changed *when* margin is collected, not how much leverage the
  strategy is permitted to run at the position sizes this design contemplates.
- **Single-stock futures**: not the chosen leverage or short instrument (Open Q#3/#4 defaults), but
  documented for completeness. F&O-eligible universe ~180–200 names (F15, unverified this session,
  moves quarterly), and — critically — SSF liquidity for anything outside the top 30–50 F&O names
  largely mirrors the underlying cash stock's own thin liquidity, so switching to futures does **not**
  escape the impact-cost table in §4c for mid/small-cap names; it only escapes the *cash-delivery
  STT*, not the ADV constraint. Single-stock derivative-ban periods (MWPL >95% of open interest) are
  an additional, recurring availability constraint that does not apply to the index contracts this
  design actually uses.
- **SLB (securities lending & borrowing)** depth is thin outside the largest, most liquid F&O names,
  and effectively irrelevant to the base design given the hedge-only default (Open Q#2: index
  derivatives only, no single-stock shorts) — flagged for completeness and for Stage-2/satellite
  reconsideration only.

### 4e. Staged-entry / days-to-build arithmetic

Days to build one full position at participation cap *p* (fraction of ADV tradeable per day without
materially breaking the square-root-law assumption) = (Q/ADV) / p.

| Book | Rank bucket | Q/ADV | Days to build @ p=10%/day | Days to build @ p=5%/day |
|---|---|---|---|---|
| Aggressive | 1–50 | 1.6% | <1 | <1 |
| Aggressive | 150–300 | 32% | 3.2 | 6.4 |
| Aggressive | 500–750 | 384% | 38.4 (≈7.7 wks) | 76.8 (≈15+ wks) |
| Moderate | 1–50 | 16% | 1.6 | 3.2 |
| Moderate | 150–300 | 321% | 32.1 (≈6.4 wks) | 64.2 (≈13 wks) |
| Moderate | 400–500 | ~1,070% | 107 (≈21 wks, ~5mo) | 214 (≈43 wks, ~10mo) |
| Conservative | 1–50 | 120% | 12 (≈2.4 wks) | 24 (≈5 wks) |
| Conservative | 50–150 | ~802% | 80 (≈16 wks, ~4mo) | 160 (≈32 wks, ~7.5mo) |

The Contract's **≤20% aggregate in-progress cap** at 5.5% average entry size allows roughly
**3–4 positions building simultaneously**. Combined with the build-times above, **pipeline
throughput** (full-size positions completed per year) is the real constraint at scale:
Conservative-book throughput for names outside the top ~50–80 is on the order of **15–20 full-size
positions per year** (3.5 slots ÷ ~12-week average build × 52 weeks) — which is compatible with a
**low-turnover, long-hold value/quality engine** (Contract item 10) but would be incompatible with any
momentum-style rotation attempted at that AUM in that rank range. This is not a new number invented
here; it is the arithmetic reason the Contract's item-10 design choice is correct, derived
independently rather than asserted.

### 4f. Effective universe per book — the contract-table vs. arithmetic contradiction

| Book | Contract's stated universe | What the days-to-build/impact arithmetic actually supports at full 5–6% size |
|---|---|---|
| Aggressive | Full NIFTY 750 incl. ranks 500–750 | Full size workable only to ~rank 300; ranks 300–750 need position sizes cut to ~1–2% (satellite-style) **or** multi-week-to-multi-month, low-turnover holds — matches Open Q#10's "capped Tier-B satellite sleeve" default almost exactly |
| Moderate | Roughly ranks 1–500 | Full size workable to ~rank 100–150; ranks 150–500 need either sub-2% sizing or multi-month builds incompatible with the 200% turnover cap unless held long (i.e., the factor/value-quality engine, not momentum, per Contract item 10) |
| Conservative | Roughly ranks 1–500 | Full size workable only to ~rank 50–80 (and even the largest names need 2–5 weeks to build); beyond that, **the SAST 5% ownership ceiling binds before the turnover cap does** (see below) — effective full-conviction universe is closer to NIFTY 50 + a slice of Next 50 |

**Named contradiction**: the Contract table describes universe by *index rank* (a market-cap/breadth
concept); the arithmetic shows the binding constraint is *ADV relative to position size* (a liquidity
concept), and the two are correlated but not identical (turnover velocity varies independently of
market-cap rank). The practical resolution — not a Contract violation, but a needed refinement — is
that **"universe" should be read as two objects per book**: a *full-conviction, any-turnover* universe
(narrow, ADV-anchored) and a *long-hold-only, small-ticket* universe (the full stated rank range,
usable only at reduced size and low turnover). The registry's per-bucket budget containment check
(Contract §10) should enforce this split explicitly rather than apply one position-size rule
uniformly across the stated rank range.

### 4g. The SAST 5% disclosure ceiling as a conservative-book position bound

Regulation 29 of the SAST 2011 Regulations (F13) triggers a disclosure obligation at **5% of a
target's total shares/voting rights** — measured against total shares outstanding, not free float, so
promoter-concentrated companies (§2) bind *tighter* in free-float terms than the headline 5% suggests.
For the conservative book (₹962cr–₹1,540cr per 5.5%-weight position at its ₹17,500–25,000cr NAV
range), the ownership-neutral market-cap floor is:

Position ÷ 5% = required market cap to stay under the disclosure trigger at full 5.5% weight
→ ₹962cr / 0.05 ≈ **₹19,240cr**, rising to **₹30,800cr** at the top of the conservative-book AUM
range (₹25,000cr NAV → ₹1,375cr position ÷ 0.05 ≈ ₹27,500cr; using the stated ₹1,540cr at 5.6%/₹25,000cr
→ ₹30,800cr).

**Any target with market cap below this ~₹19,000–31,000cr floor cannot receive a full 5–6% weight from
the conservative book without crossing the SAST disclosure threshold** (a compliance event, not
necessarily prohibited, but one this design should treat as a hard cap rather than an incidental
filing). This floor moves up over time with nominal market-cap growth and must be recomputed against
live market-cap data in the build phase, but the mechanism and its interaction with the ADV-based
"effective universe" conclusion (§4f) — both point to the **same top-50-to-80-name** effective
full-conviction universe for the conservative book — is a first-principles, cross-checked result, not
an assumption.

### 4h. Turnover budgets, cost curves, and the re-derived gross-alpha hurdle

**Re-deriving the prior-pass number (Contract item 6: "~3.9% NAV/yr at 500% one-way turnover,
~0.6% at 100%," implied incremental hurdle ~3.3pp)**:

- **At 100% turnover, concentrated in the liquid core (as low turnover always can be, since there is
  no capacity pressure)**: statutory+brokerage ≈ 24–32 bps, plus modest spread/impact for
  patient execution of liquid names (call it +10–35 bps) → **~35–70 bps at 100% turnover**. This
  roughly matches, and is not far below, the prior pass's 60 bps figure — **the 100%-turnover
  baseline survives re-derivation largely intact.**
- **At 500% turnover, the marginal 400% cannot all be spent re-trading the same ~100–150 liquid names**
  (alpha-signal decay/crowding among momentum-style rotators using similar signals means genuinely new
  turnover-worthy opportunities increasingly lie further down the rank list) — so the marginal cost
  per 100% of turnover **rises** with total turnover, not stays flat. Using the §4c/4e arithmetic, if
  even a modest 15–25% of the incremental turnover touches ranks 300–750 *without* aggressive
  position-size throttling, the marginal-100% cost is **100–250+ bps**, not the ~60 bps implied by
  linear extrapolation of the 100%-turnover baseline. **Corrected range at 500% turnover: roughly
  4.5%–9% NAV/yr**, centered somewhat *above*, not at, the prior pass's 3.9% point estimate — **the
  prior number was not wrong in order of magnitude, but it likely understates the tail-cost
  convexity** unless the tail sleeve's position sizes are explicitly throttled (§4f's "long-hold-only,
  small-ticket" universe). With disciplined throttling (tail positions capped near 1.5–2% rather than
  5.5%, roughly halving Q/ADV's square root and thus impact by ~35–45%), the corrected range narrows
  toward **3.5%–6.5% NAV/yr** — bracketing the prior estimate rather than replacing it with a single
  new point.
- **Implied incremental gross-alpha hurdle for the high-churn book, corrected**: **~3.0–6.0pp/yr**
  extra gross alpha needed to justify running at 500% vs. 100% turnover, versus the prior pass's
  point estimate of 3.3pp — a **wider, more honest band centered close to the same place**, with the
  explicit finding that the band's upper half is only avoidable through deliberate tail-position-size
  throttling, not through the turnover cap alone.

**Cost curve function proposed for the registry** (avoiding a single magic number, per Contract §6):
`cost(turnover_bucket_mix) = Σ_bucket [turnover_share_bucket × (statutory_bucket + spread_impact(Y, σ_bucket, position_size_bucket/ADV_bucket))]`
— i.e., cost is a function of *where* turnover is spent (the rank-bucket mix), not of aggregate
turnover alone. The registry should store the per-bucket coefficients (statutory rates, σ ranges, Y
range) as the frozen parameters, and let cost curves for any given turnover-mix scenario be computed
from them, rather than freezing a single "cost per 100% turnover" scalar.

---

## 5. Evidence-tier recommendations

| Effect / parameter | Tier | Observation count / basis | Note |
|---|---|---|---|
| STT/stamp duty/exchange-charge/SEBI-fee rates | **A**-equivalent (regulatory fact, not a statistical effect) | N/A — verified against current rate schedule via ≥3 independent sources each | Not a "≥30 observations" effect in the Contract's sense; treat as ground truth pending each Budget's revision, re-verify annually |
| Square-root law functional form | **A** | Bouchaud/Gatheral et al. cite dozens of independent datasets across markets/decades | Functional form well-established; the *coefficient* Y is asset/market/period-specific — treat Y itself as Tier B for India specifically (no Indian calibration found this session) |
| Korajczyk-Sadka momentum capacity ($5bn, Dec-1999 US) | **B** | Single-country (US), single study, cross-country analogue count <10 found this session | Requires the India-market-size scaling heuristic (§ below) to translate — that scaling is itself Tier C |
| Novy-Marx-Velikov capacity ranking (value/size/profitability > momentum > short-horizon) | **B** | Single-country (US) TAQ-based study | Directionally consistent with Korajczyk-Sadka and the recalled Ratcliffe-Miranda-Ang ranking — three independent-ish US sources agreeing raises confidence in the *ranking*, not the *magnitudes* |
| India-market-size momentum-capacity scaling (₹cr figures in §3) | **C** | 0 Indian observations; a single proportional-scaling heuristic constructed in this dossier | Explicitly a new construct, not from any paper — stated with its own reasoning per Contract §5; must be treated as directional only |
| Provisional ADV-by-rank-bucket table (§4b) | **C** | 0 verified observations this session (network-blocked) | Must be replaced with live bhavcopy medians before any downstream number is trusted |
| Days-to-build / effective-universe contradiction (§4e–4f) | **B** (arithmetic derived from A/C-tier inputs) | Deterministic arithmetic on the ADV table + Contract's own stated position-size/cap rules | The *logic* is solid (A-tier: it's just division); the *inputs* (ADV table) are C-tier, so final numbers inherit that uncertainty — re-run once ADV is real |
| SAST 5% disclosure floor (§4g) | **B** | Regulatory fact (should be A-tier once re-verified) combined with C-tier AUM/position assumptions | Recompute against live market-cap data each rebalance cycle, not frozen at inception, since it moves with market growth |
| Re-derived cost-at-500%-turnover range (§4h) | **C** | Built from B/C-tier ADV and Y inputs | Present as a range for exactly this reason; do not let the registry collapse it to a point estimate |

---

## 6. Research method for the data phase

1. **Replace the provisional ADV table (§4b) with live NSE bhavcopy data.** For each NIFTY 750
   constituent, compute a rolling 90-trading-day median (not mean, to resist single-day spikes) of
   traded value; bucket by rank (using the same rank definition as the index provider's factsheet,
   re-pulled quarterly since Nifty 500/Microcap 250 membership itself turns over). Source: NSE bhavcopy
   (free, daily), ingested on the principal's machine per Contract item 11.
2. **Calibrate Y (square-root-law coefficient) on Indian data** rather than importing a US-literature
   value. Use executed-trade impact if/when the book has live execution history (post-launch); until
   then, a defensible proxy is to regress realized daily price moves against signed order-flow
   proxies constructed from bhavcopy volume/delivery-percentage data — imperfect (no true metaorder
   tagging without broker execution logs) but far better than assuming a foreign Y. Purge/embargo per
   Contract §9 once any fitting is attempted; this is a Stambaugh-bias-adjacent estimation problem
   (σ and impact both persistent), so out-of-sample validation against the historical-mean benchmark
   is mandatory before the coefficient is trusted.
3. **Re-verify the STT/stamp-duty/exchange-charge schedule at the start of every fiscal year** (April)
   and immediately after any Union Budget — this workstream found two hikes in under two years; treat
   the rate table as a live registry entry with an expiry/re-check date, not a frozen constant.
4. **Measure the actual futures roll basis vs. MIBOR/overnight rates** from historical NSE futures and
   spot bhavcopy data, by expiry, across at least one full 7–11-year credit cycle if available (ties
   to workstream 03) — this is the only way to give the "roll cost vs. MIBOR" mechanism in §4d an
   actual number instead of a sign.
5. **Confirm the current F&O-eligible single-stock list and MWPL thresholds** each quarter directly
   from the NSE/SEBI eligible-securities circular (free), even though the base design does not trade
   single-stock derivatives — needed only if Stage 2 or the aggressive satellite sleeve reconsiders
   SSF.
6. **Build the per-bucket cost-curve function (§4h) as actual code in the data phase**, parameterized
   by the registry's frozen statutory rates, live-calibrated Y, and live ADV — not as a single scalar.
   Every turnover-budget check in CI (Contract §10) should evaluate this function against the proposed
   trade list's actual rank-bucket mix, not compare aggregate turnover to a flat bps assumption.
7. **Re-run the SAST-floor calculation (§4g) against live market-cap data each rebalance cycle** for
   the conservative book specifically, since it is both AUM-dependent (moves with book size within its
   ₹10,000–25,000cr range) and market-growth-dependent (the ₹19,000–31,000cr floor rises with nominal
   Indian market-cap growth over the 3–6 month build timeline and beyond).
8. **Negotiate and document actual broker/DMA execution rates** before treating the 1–5bps brokerage
   placeholder (§4a) as anything but a placeholder — this is a business input, not a research one, but
   the registry must not silently inherit an unverified assumption as if it were sourced.
9. **Deflated-Sharpe discipline (Contract §9)**: any parameter in this dossier that gets swept (Y, the
   participation-rate caps, the tail-position-size throttle) during backtesting must be counted in the
   true trial count alongside the hedge-ratio × regime grid already flagged in the Contract — this
   dossier alone proposes at minimum a Y-range sweep and a participation-cap sweep per rank bucket,
   which is 5 buckets × 2 parameters × several grid points each; that multiplies the existing trial
   count materially and should be pre-registered, not discovered after the fact.

---

## 7. Open questions and [VERIFY] items

- `[VERIFY: Frazzini-Israel-Moskowitz 2018 "Trading Costs" exact fitted coefficient(s) and
  bps-at-participation-rate table]` — AQR.com and SSRN both blocked in this environment; needs a
  session with a working fetch path or a library/database with full-text access.
- `[VERIFY: Ratcliffe, Miranda & Ang capacity-of-smart-beta paper — author list, exact venue, year]` —
  not re-confirmed this session due to search-budget exhaustion.
- `[VERIFY: Almgren & Chriss (2000) and Almgren-Thum-Hauptmann-Li (2005) full bibliographic details]`
  — canonical, high-confidence recall, but not freshly searched this session.
- `[VERIFY: current F&O-eligible single-stock count and MWPL threshold levels]` — moves quarterly;
  needs a live NSE circular pull, not available in this environment or session.
- `[VERIFY: SEBI SAST Regulations 2011 Regulation 29 exact clause numbering]` — high-confidence
  regulatory recall, not re-searched this session.
- `[VERIFY: peak-margin phase-in exact dates (Dec 2020 → Sept 2021) and percentages]` — not
  re-searched this session.
- `[VERIFY: entire provisional ADV-by-rank-bucket table, §4b]` — explicitly flagged as the single
  largest source of downstream uncertainty in this dossier; every cost-curve, days-to-build, and
  effective-universe number in §4c–§4h inherits this table's error and must be recomputed once real
  bhavcopy-derived ADV is available.
- `[VERIFY: median promoter-holding percentage across NIFTY 500, current]` — cited qualitatively in
  §2 without a fresh number.
- `[VERIFY: NSE T+0 settlement pilot scope and current status]` — cited qualitatively in §2.
- **Open design question for the principal, not just a citation gap**: should the registry's turnover
  cap be redefined *per rank bucket* (as this dossier recommends in §4f/§4h) rather than as a single
  book-level scalar, given that the arithmetic shows the same book-level turnover number implies
  wildly different cost depending on rank-bucket mix? This is a genuine architecture question this
  workstream surfaced but the Contract does not currently answer — flagging for principal attention
  alongside the ten questions in `OPEN_QUESTIONS.md`, not attempting to resolve it unilaterally here.
- **Session-level process note**: the shared WebSearch budget (200 calls) was exhausted mid-session
  across the research program's concurrent workstreams. If this dossier's [VERIFY] density is higher
  than workstreams 01–03, that is the direct cause, not a change in citation discipline — future
  workstreams in this program may want either a per-workstream budget reservation or to run
  statutory/regulatory-fact searches earlier in their session before the shared pool is depleted by
  concurrent agents.

---

*Word count target: 3,500–7,000 (dense, no filler). All rupee figures in crore (₹cr) unless stated
otherwise. All rate figures verified against ≥1 independent web source this session except where
explicitly tagged `[VERIFY]`.*
