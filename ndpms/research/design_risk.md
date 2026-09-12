# Risk Management Framework & Tail-Risk Dashboard — ₹500 Cr NDPMS Mandate

Basis: ₹500 Cr (NAV = 500), house Moderate/Aggressive sleeve weights as built in the allocation design (`design_allocation.md`), composite benchmarks defined there, and the current SEBI (Portfolio Managers) Regulations, 2020 as amended, cross-checked against the July-2025 Master Circular and the July-2026 consultation paper [1]–[6]. All figures not cited are model outputs of `risk_calc.py` (this session) using the same vol/beta/correlation assumptions as the allocation design, and are labelled "model" or "approx." — never presented as market fact.

## 0. Risk philosophy under NDPMS

Under NDPMS the portfolio manager (PM) **cannot** act at its own discretion — Regulation 24 read with the client agreement makes every trade an execution of the client's instruction [1][2]. Three consequences shape the whole risk architecture:

1. **Risk control must be pre-authorised, not improvised.** Limits, hedge protocols and de-risking triggers have to exist as *standing instructions* or *pre-agreed bands* inside the Rebalance Proposal Pack (RPP) machinery already defined in the regulatory design (Annexes B/C) — a risk manager cannot unilaterally cut equity at 2pm on a crash day.
2. **Latency is a risk factor in its own right.** The gap between "IC recommends de-risking" and "client consents and PM executes" is real ₹ cost (Section 2.7, Section 7) and must be sized, budgeted and reported like any other risk.
3. **We still own the P&L.** NDPMS removes discretion, not accountability — the mandate explicitly makes the team accountable for alpha, slippage, cost and tax vs the house benchmark. So the risk framework has to be *pre-loaded* (limits, hedge protocols, standing instructions) precisely because it cannot be improvised later.

## 1. Limit framework

All limits are two-tier: an **IPS/house limit** (tighter, what we target) and a **regulatory/legal ceiling** (harder, what we cannot cross even with consent delays). Breach action always distinguishes a **passive breach** (market move, redemption, corporate action — must be cured, not urgent) from an **active breach** (a new trade would create it — blocked pre-trade by compliance).

| # | Limit | House/IPS level (₹500 Cr) | Legal ceiling | Action on breach |
|---|---|---|---|---|
| 1 | Sleeve band (each of Core beta / Satellite / Alternatives / Stabilisers / Liquidity) | ±3–5 pp of SAA (Section 3, allocation design) | n/a | Passive: flag in monthly drift report, propose restoring trade in next RPP. Active: blocked pre-trade |
| 2 | Single-name direct stock | 5% of AUM (₹25 Cr) target cap, 8% hard cap (₹40 Cr) | No SEBI single-issuer cap for PMS (unlike MF's 10% rule) — house-only discipline | 5–8%: no new buys, IC review. >8%: mandatory trim proposed in next RPP (5 trading-day SLA) |
| 3 | Sector/industry (NSE sector classification) | 25% of equity sleeve (≈ ₹50–60 Cr Moderate) | n/a | >25%: block new sector buys; if breach from price move, trim proposed within 10 trading days |
| 4 | Single AIF / Cat II / Cat III fund | 5% of AUM (₹25 Cr) per fund; ≤ 2 funds per manager | Unlisted aggregate 25% of AUM (Reg 24(4)); 100% for LVAI [1][2] | New commitments blocked once fund-level cap hit; existing over-cap (NAV appreciation) tracked, no forced redemption (illiquid) |
| 5 | Single-manager / AMC (across MF + PMS + AIF, look-through) | 15% of AUM (₹75 Cr) per AMC/manager group | n/a | >15%: no new subscriptions to that AMC; diversify next tranche |
| 6 | Third-party PMS manager | 3% of AUM (₹15 Cr), 1 manager only | Structured as a separate contract, outside NDPMS AUM look-through reporting only [12] | Cap reached → no top-up; review manager annually |
| 7 | Credit floor — corporate bonds/NCDs | AAA/AA+ only, min 90% of FI sleeve; AA min issuer rating (no sub-AA) | NDPMS: **no investment in below-investment-grade listed securities**; ≤10% of AUM in unlisted **unrated** debt (within the 25% unlisted cap) [1][2][6] | Any downgrade below AA- → mandatory exit proposed within 5 trading days; below investment grade → immediate block, exit at next liquidity window |
| 8 | Duration band — fixed-income sleeve | Modified duration 2.5–4.5 yrs (Moderate blended); ≤ 6.5 yrs on the 10Y G-sec line alone | n/a | Outside band: rebalancing trade proposed in the next monthly RPP; no daily duration trading (NDPMS + cost) |
| 9 | Illiquid / unlisted aggregate (AIF + unlisted debt + pre-IPO) | 15% of AUM (₹75 Cr) house target | 25% of AUM (₹125 Cr) NDPMS ceiling; 100% for LVAI [1][2] | House 15–25%: IC sign-off for further commitments. >25%: hard block (active breach is non-compliance) |
| 10 | Derivative notional (hedge only — no leverage permitted) | ≤ 25% of AUM notional (₹125 Cr) for tail hedges | Exposure ≤ portfolio funds placed with PM (i.e. ≤100% notional); PM "shall not leverage" [1][2]. 2026 proposal (not yet notified): 1.25× total exposure, unhedged shorts ≤50% AUM via equity ETD, option premium ≤10% AUM [6] | Any derivative trade requires the pre-approved Derivatives/Hedging Protocol annex + RPP line item; premium spend >1% of AUM p.a. escalated to IC |
| 11 | Liquidity floor — days-to-liquidate at 20% ADV | ≥ 80% of book liquidable in ≤ 5 trading days; ≥ 95% in ≤ 10 days | n/a (house discipline; feeds redemption-readiness) | Breach → new illiquid commitments paused until ratio restored |
| 12 | Currency / unhedged FX exposure (international equity, offshore funds) | ≤ 15% of AUM unhedged (₹75 Cr) | No PMS-specific FX cap today; international access itself is capped by the industry-wide USD 7 bn overseas MF/ETF gate, not a per-client SEBI rule [design_regulatory.md §1.2] | >15%: no further international top-ups; consider partial USDINR forward/NDF hedge (client consent required) |
| 13 | Associate/group securities (Angel One group) | 10% of AUM (₹50 Cr) house target | Equity ≤15%/25% combined; equity+debt+hybrid ≤30% of AUM [design_regulatory.md §1.4][4] | One-time positive client consent required before first purchase; alert-based real-time monitoring mandated by the 2022 amendment [4] |

**Worked ₹500 Cr read:** at the house target, illiquid sleeve ≤ ₹75 Cr, single AIF ≤ ₹25 Cr → minimum 3 AIF lines to reach the illiquid target without breaching #4; single-name equity cap ₹25–40 Cr against a ~₹160–220 Cr direct-stock book (Section 3 of the allocation design) implies 6–9 direct names minimum, consistent with the ~20–25 name scorecard book already assumed there.

## 2. Daily risk metrics

Computed once daily (T+1 morning, after NAV strike) from the look-through position file. All formulas below use daily simple returns `r_t`, decimal weights `w`, and are annualised with √252 unless noted.

**2.1 Parametric (variance-covariance) VaR.** Portfolio variance σ²_p = wᵀΣw, where Σ is the sleeve covariance matrix (annualised, decimal²) built from sleeve vols and a correlation matrix with three regimes — equity-cluster ρ ≈ 0.75 (large/mid/small-cap ex-international), cross-asset β-implied ρ = β_i·β_j elsewhere, bond-cluster ρ ≈ 0.6, gold–silver ρ ≈ 0.75. VaR_{h,c} = z_c · σ_p · √(h/252) · NAV, z_95=1.645, z_99=2.326.

**2.2 Historical VaR/CVaR.** Re-price the current weight vector against each of the trailing ~1,500 daily return vectors (≈6 years) of the sleeve proxies; VaR_h = the (1−c) percentile of the P&L distribution; CVaR (Expected Shortfall) = mean of losses beyond that percentile. Historical VaR should run *alongside* parametric because Indian equity/credit return distributions are fat-tailed and left-skewed (2020, 2018 IL&FS) — parametric alone understates tail risk by construction.

**2.3 Model baseline (today's book, `risk_calc.py`):**

| Metric | 80/20 house benchmark | Moderate | Aggressive |
|---|---|---|---|
| Annualised vol (parametric) | 13.6% | 9.7% | 12.5% |
| Beta to Nifty 50 | 0.80 | 0.55 | 0.72 |
| 1-day parametric VaR 95% / 99% | 1.41% (₹7.1 Cr) / 1.99% (₹10.0 Cr) | 1.00% (₹5.0 Cr) / 1.42% (₹7.1 Cr) | 1.30% (₹6.5 Cr) / 1.84% (₹9.2 Cr) |
| 1-month parametric VaR 95% / 99% | 6.46% (₹32.3 Cr) / 9.14% (₹45.7 Cr) | 4.59% (₹22.9 Cr) / 6.49% (₹32.4 Cr) | 5.95% (₹29.8 Cr) / 8.42% (₹42.1 Cr) |
| 1-day parametric ES (97.5%, ≈ CVaR) | 2.00% | 1.42% | 1.85% |
| Tracking error vs own composite (ex-ante) | — | 1.5–2.0% (model) | 2.0–2.5% (model) |

These are ex-ante, model-based figures (same vol/beta assumptions as the allocation design) — the live dashboard replaces them daily with realised-covariance numbers once 12 months of NAV history exist; until then, parametric VaR is the primary daily read and historical VaR runs on the sleeve *proxy index* history (available from day 1).

**2.4 Realised vol — EWMA.** σ²_t = λσ²_{t-1} + (1-λ)r²_{t-1}, λ = 0.94 (RiskMetrics daily). Example: a −5.9% single-day shock (election-day-scale) moves daily vol from 0.76% (≈12% annualised) to 1.62% (≈25.7% annualised) — i.e. an EWMA vol spike of ~2× overnight, which is exactly the signal the early-warning board (Section 6) should catch same-day.

**2.5 Beta and tracking error vs composite.** Beta_p = (wᵀΣe₁)/σ²_{Nifty}; TE = √[(w_p−w_b)ᵀΣ(w_p−w_b)] where w_b is the *composite* benchmark defined in the allocation design (55/5/25/5/10 Moderate; 75/7/8/5/5 Aggressive), not the legacy 80/20. **Reuse the same TE bands already set for performance reporting** — green 2.5–4.5% (Moderate)/4.5–6.0% (Aggressive) target range, amber up to the next 1.5 pp, red >6.0% or <1.5% (closet-indexing) — so the risk dashboard and the attribution dashboard never disagree on what "in control" means.

**2.6 Drawdown from peak.** DD_t = V_t/max(V_{0..t}) − 1, computed on the daily NAV series (post-fee). Reuse the performance-dashboard bands: green ≤1.10× benchmark MDD, amber 1.10–1.25×, red >1.25× **or** an absolute breach of −18% (whichever binds first) — the tail-risk dashboard owns enforcement of the absolute −18% trigger.

**2.7 Consent-latency cost.** Because NDPMS de-risking cannot happen same-day, every VaR number is shadowed by a "cost of the consent gap": ΔP&L ≈ position size × daily vol × √(days-to-consent). Worked (₹50 Cr, i.e. 10% equity de-risk, at normal 1.2% daily vol vs stressed 2.5%):

| Days to consent & execute | Normal-regime 1-σ cost | Stressed-regime 1-σ cost |
|---|---|---|
| 1 day | ₹0.60 Cr | ₹1.25 Cr |
| 2 days | ₹0.85 Cr | ₹1.77 Cr |
| 5 days | ₹1.34 Cr | ₹2.80 Cr |
| 10 days | ₹1.90 Cr | ₹3.95 Cr |

This is the single most important NDPMS-specific number in the whole risk framework: it is why pre-agreed bands and standing instructions (Section 7) exist — every day of avoidable consent latency during a stress event costs of the order of ₹0.6–1.3 Cr of unhedged 1-σ exposure on just a 10% equity trim.

**2.8 Factor exposures.** Monthly holdings-based regression (reuses the attribution engine's factor set): active exposure x_k = Σ_j(w_j^P − w_j^B)z_{j,k} on size, value, momentum, quality, low-vol z-scores from the NIFTY-750 scorecard; cross-check with a 36-month returns-based regression of active return on the same factor-spread indices (size = Midsmallcap 400 − Nifty 100; value = Nifty 500 Value 50 − Nifty 500; momentum = Nifty 500 Momentum 50 − Nifty 500; quality = Nifty 200 Quality 30 − Nifty 200; low-vol = Nifty 100 Low Vol 30 − Nifty 100), same index proxies as the performance-attribution design so factor numbers reconcile between the two dashboards.

**2.9 Correlation regime (rolling 60-day).** Track the rolling 60-day average pairwise correlation across the 8 sleeve return series. A jump from the ~0.3–0.4 "normal" regime average to >0.6 is the standard "correlations go to 1 in a crisis" signal — treat a 60-day average >0.6 as itself an early-warning trigger (Section 6), independent of any single asset's level.

**2.10 Look-through for MF/AIF holdings.** VaR, factor and sector exposures must decompose fund wrappers into underlying stock/bond exposure monthly (AIF Cat II/III report holdings quarterly at best — use the fund's last disclosed portfolio, aged, and flag it as "stale look-through" in the dashboard rather than silently treating the wrapper as a black box). Cat III AIFs using leverage/derivatives internally should be shown at **gross** notional exposure in the look-through, not just NAV, since the fund's own leverage is invisible in the raw NAV return.

## 3. Historical stress library

Ten episodes, calibrated to Nifty 50, scaled to the current Moderate/Aggressive books using each sleeve's assumed beta/duration sensitivity (`risk_calc.py`). **Nifty/Midcap/Smallcap/Gold/VIX figures marked [V] are verified for the two most recent episodes via live search this session; older episodes use approx. consensus magnitudes from public retrospectives and are labelled "approx."** — treat the exact decile of every pre-2020 number as indicative, not certified.

| Episode | Window | Nifty 50 | Midcap 150 | Smallcap 250 | 10Y G-sec yield Δ | Gold (INR) | USDINR Δ | India VIX peak | Mod ₹ Cr | Agg ₹ Cr | Time to recover (Nifty) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GFC | Jan-08 to Mar-09 | −60% | −72% approx. | −78% approx. | −60 bp then +150 bp swing | +38% | +32% | ~85 approx. | −₹160 Cr | −₹215 Cr | ~34 months to regain Jan-08 high (Nov-10) approx. |
| Aug-11 downgrade | Nov-10 to Dec-11 | −28% approx. | −35% approx. | −45% approx. | +90 bp | +30% | +22% | ~37 approx. | −₹72 Cr | −₹99 Cr | ~14 months approx. |
| Taper tantrum | May–Aug 13 | −16% approx. | −25% approx. | −28% approx. | +210 bp | +22% | +24% | ~32 approx. | −₹48 Cr | −₹56 Cr | ~3 months approx. |
| Demonetisation | Nov–Dec 16 | −7.5% approx. | −11% approx. | −13% approx. | −60 bp | −8% | +2.7% | ~23 approx. | −₹20 Cr | −₹28 Cr | ~2 months approx. |
| IL&FS credit event | Sep–Oct 18 | −15% approx. | −22% approx. | −35% approx. | +30 bp | +7% | +6% | ~21 approx. | −₹47 Cr | −₹61 Cr | ~9–14 months approx. |
| COVID crash | Feb–Mar 20 | −39.6% | −41% approx. | −46% approx. | −40 bp | +7% | +8% | 86.64 [V] | −₹114 Cr | −₹144 Cr | ~8 months (new high Nov-20) approx. |
| 2022 rate shock | Oct-21 to Jun-22 | −18% approx. | −22% approx. | −30% approx. | +125 bp | +8% | +5% | ~34 approx. | −₹50 Cr | −₹68 Cr | ~7 months approx. |
| Election-day crash | 4-Jun-24 (1 day) | −5.9% [V] | −8% approx. | −8% approx. | +7 bp | flat | +0.5% | ~27 close/~32 intraday approx. [V] | −₹17 Cr | −₹21 Cr | ~2 weeks approx. |
| Tariff shock | Sep-24 to Apr-25 | −17% approx. | −22% approx. | −26% approx. | −30 bp | +30% | +3% | ~23 approx. | −₹33 Cr | −₹53 Cr | partial; several months |
| West Asia / INR shock (2025–26) | ~Feb-26 to date | −12% approx. | −15% approx. | −18% approx. | +50 bp | −5% | +12% | 27.17 [V]≈52-wk high 28.90 | −₹30 Cr | −₹40 Cr | in progress — India VIX back to ~12.3 as of 12-Sep-26 [V], suggesting the acute phase has passed |

**Reading it:** the Moderate book's structural de-risking (lower beta, 24%+ fixed income/gold, arbitrage sleeve) cuts a GFC-scale shock from −60% (Nifty) to ≈−32% NAV and a COVID-scale shock from −39.6% to ≈−23% NAV — roughly 45–55% of headline Nifty drawdown captured across the stress set, consistent with the book's 0.55–0.72 beta. Aggressive captures more (≈65–75% of Nifty's move) by design.

## 4. Hypothetical scenarios

| Scenario | Key assumptions | Mod ₹ Cr / % | Agg ₹ Cr / % | Liquidity needed (redemption-readiness) |
|---|---|---|---|---|
| Equity −25% (mid −32%, small −38%, intl −15%, VIX→40) | Broad de-rating, no credit event | −₹72.6 Cr / −14.5% | −₹96.0 Cr / −19.2% | None forced; if client instructs a 10% de-risk, need ₹50 Cr liquid within consent SLA |
| Rates +200 bp parallel | REIT/InvIT −15%, equity −12% (higher discount rate) | −₹44.9 Cr / −9.0% | −₹48.3 Cr / −9.7% | FI sleeve MTM only; no forced sales — hold to maturity option on TMF/G-sec |
| INR −10% (FII exodus) | Nifty −8%, international +9% (FX translation), gold +9% | −₹21.0 Cr / −4.2% | −₹26.1 Cr / −5.2% | Watch LRS/TCS cash-lock if int'l sleeve is topped up mid-shock |
| Oil +50% | CAD/inflation shock, yields +60 bp, Nifty −10% | −₹28.5 Cr / −5.7% | −₹35.2 Cr / −7.0% | None; gold sleeve is the natural offset |
| Credit event: one Cat II fund marks −40% | ₹12.5 Cr AIF exposure (5% single-fund cap fully used) marked to a distressed NAV; AA-book −8% | −₹6.6 Cr / −1.3% | −₹4.0 Cr / −0.8% | Fund is locked (3–7 yr close-ended) — **zero** incremental liquidity available; this is a pure mark-to-market hit, escalate to IC same day, client comms within 24h |
| FII outflow spike (₹1 lakh Cr/month) | Nifty −12%, mid −18%, INR −4%, yields +40 bp | −₹35.1 Cr / −7.0% | −₹44.9 Cr / −9.0% | Stress-test ADV halving (Section 1 liquidity floor) — direct-stock book liquidation time roughly doubles |

**Worked liquidity math (20% ADV rule):** days = position ÷ (0.20 × ADV). A ₹1.8 Cr position against ₹20 Cr ADV = 0.45 days; the same position if ADV halves under stress (₹10 Cr) = 0.9 days; a smaller-cap ₹3 Cr position against ₹10 Cr ADV stressed to ₹5 Cr ADV = 3.0 days. The ₹300 Cr aggregate equity sleeve, split across ~745 Cr ADV-equivalent liquidity assumptions used in the allocation design, liquidates in well under a week even at 20% ADV in a normal regime — the binding constraint in a real stress event is **consent latency (Section 2.7), not market liquidity**.

## 5. Tail hedging menu

**5.1 What NDPMS actually permits.** Exchange-traded index derivatives are allowed **only for hedging and portfolio rebalancing**, with total derivative exposure capped at the portfolio funds placed with the PM (i.e. no leverage) [1][2]. Every hedge trade needs a **specific client instruction or a pre-approved standing Hedge Protocol annex** (auto-roll of an already-consented hedge into the next monthly series at the same notional is a valid standing instruction; initiating a *new* hedge, or resizing one, is not — it goes into the RPP). A 2026 consultation paper would raise the ceiling to 1.25× AUM total exposure with unhedged shorts to 50% of AUM via equity ETDs and a 10% AUM cap on option premium — **not yet notified; do not rely on it operationally** [6].

**5.2 Cost of a rolling 5% OTM 3-month Nifty put, ₹300 Cr equity sleeve.** India VIX is currently ~12.3 (12-Sep-2026), well inside its 52-week range of 8.72–28.90 [7][8] — i.e. **near the cheap end of the hedge-cost cycle**, which is exactly when the IC should be adding convexity rather than after a spike. Using Black-Scholes with S=23,500 (Nifty spot, ~10-Sep-2026 close 23,478 [9]), lot size 65 (revised Jan-2026 [10]), r=6.2%, dividend yield 1.2%, T=0.25:

| Instrument (3M tenor) | Assumed IV | Cost | ₹ Cr/yr on ₹300 Cr sleeve | Annualised bps |
|---|---|---|---|---|
| 5% OTM put (K=95%) | 14.5% (≈2 pts over spot VIX for term + skew) | 0.73%/qtr | ₹8.8 Cr | ~292 bps |
| 5% OTM put, stressed roll | 20–30% | 1.5–3.2%/qtr | ₹18–39 Cr | 612–1,284 bps |
| 95/85 put spread | 14.5% / 17.5% | 0.66%/qtr | ₹7.9 Cr | ~265 bps |
| 95P/105C collar (zero/negative cost) | put 14.5% / call 12% | net credit | ~+₹3.5 Cr received | −116 bps (net **credit**) |
| 10% OTM put (cheaper tail-only cover) | 16% | 0.23%/qtr | ₹2.8 Cr | ~94 bps |
| Lots needed for ₹300 Cr notional | — | — | ~1,960 lots (65-share lot, ₹15.3 lakh/lot notional) | — |

**Payoff in the stress library** (rolling 5% OTM put programme, premium 0.73% first roll / 1.5% on stressed re-strikes, on the ₹300 Cr sleeve, ignoring basis/skew mark-to-market gains mid-drawdown):

| Episode | Unhedged sleeve loss | Put payoff | Premium paid | Net hedge result |
|---|---|---|---|---|
| GFC (5 quarters) | −₹180 Cr | +₹126 Cr | ₹13.8 Cr | **+₹112 Cr net benefit** |
| COVID (1 quarter, sharp) | −₹119 Cr | +₹104 Cr | ₹2.2 Cr | **+₹102 Cr net benefit** |
| IL&FS (1 quarter) | −₹45 Cr | +₹30 Cr | ₹2.2 Cr | +₹28 Cr net benefit |
| Taper tantrum (1 quarter) | −₹48 Cr | +₹33 Cr | ₹2.2 Cr | +₹31 Cr net benefit |
| 2022 rate shock (3 quarters, grind) | −₹54 Cr | +₹12 Cr | ₹10.4 Cr | +₹1.5 Cr — grinding declines are the weak case for a rolling put |
| Election-day (1-day, small) | −₹18 Cr | +₹2.7 Cr | ₹2.2 Cr | +₹0.5 Cr — small moves rarely justify the running premium |
| Tariff shock (3 quarters, choppy) | −₹51 Cr | +₹8.7 Cr | ₹10.4 Cr | **−₹1.8 Cr — the programme loses money** |
| West Asia (recent, 3 quarters, shallow) | −₹36 Cr | ₹0 | ₹10.7 Cr | **−₹10.7 Cr — pure cost, no payoff (Nifty never closed 5% down at any single roll date)** |

**Reading it:** a rolling OTM put programme is a strong payoff in sharp, fast drawdowns (GFC, COVID, IL&FS, taper) and a **running cost with no payoff** in grinding, choppy, or shallow-decline regimes — which is most years. Running cost at ~290 bps p.a. (₹8.8 Cr/yr on the equity sleeve, ≈1.8 bps/yr on the whole ₹500 Cr book) is the right order of magnitude for a **standing, small, always-on** protection line, not a full-notional programme; size it to the equity sleeve's *tail* (25–40% notional coverage, i.e. ₹75–120 Cr), not 100%.

**5.3 The rest of the menu:**

| Method | NDPMS mechanics | Approx. annual cost | Best regime |
|---|---|---|---|
| Nifty put spread (95/85) | Cheaper than outright put, caps payoff at 10% | ~265 bps p.a. on notional hedged | Moderate, capital-efficient default |
| Collar (buy 95 put, sell 105 call) | Can be zero-cost to net-credit; caps upside | ~0 to negative cost | When IC also wants to trim upside participation (post-rally de-risk without selling) |
| Gold overweight (tactical +2–3 pp vs SAA) | Already inside the fund-level rebalance band (no derivatives, no extra consent friction beyond normal RPP line) | Opportunity cost only (gold's lower expected return, ~8% vs 11% equity) | INR-devaluation and geopolitical-shock regimes specifically (Section 3: gold +30–38% in GFC and tariff-shock windows) |
| Long-vol / market-neutral Cat III AIF or SIF hybrid long-short (1–2% allocation) | Already inside Alternatives sleeve; manager holds trading discretion inside the wrapper — the one place NDPMS's no-discretion rule doesn't bind day-to-day | Fund-level tax up to ~42.7% [design_regulatory.md] partly offsets the diversification benefit | Grinding/choppy regimes where a static put programme loses money (Section 5.2's tariff-shock/West-Asia rows) |
| Dynamic de-risking rules (trend + vol trigger) | Must be pre-consented as a Standing Instruction with a fully specified trigger, instrument, and max ₹ — not free-form "PM discretion to de-risk" | Turnover/tax cost of the trims themselves | Confirmed trend break (200-DMA, Section 6) |
| Cash / arbitrage buffer | 2% of AUM (₹10 Cr) always-on liquidity sleeve, already in the SAA | Opportunity cost ≈ equity E[R] − arbitrage yield (~4–5 pp) on the buffer only | Funds the first days of any consent-latency gap without touching the AIF/equity book |

## 6. Early-warning indicator board

| Indicator | Green | Amber | Red | Action on Red |
|---|---|---|---|---|
| India VIX (spot ~12.3, 12-Sep-26 [7]) | <15 | 15–22 | >22 (52-wk high 28.9 [8]) | Trigger IC review of hedge sizing same day; propose adding OTM puts in next RPP |
| Nifty breadth (advance/decline, 20-day avg) | >1.2 | 0.8–1.2 | <0.8 sustained 5 sessions | Flag momentum-filter check (200-DMA below) |
| FII net flows (monthly, NSDL) | Net buy or <₹10k Cr outflow | ₹10–40k Cr monthly outflow | >₹40k Cr monthly outflow (approx. 2022/2025 stress scale) | Standing-instruction cash sweep review; prep de-risk RPP draft (not executed until consent) |
| AAA–10Y G-sec spread (currently ~221 bp, 15-Aug-26 [11]) | <180 bp | 180–260 bp | >260 bp | Credit floor review (Section 1 #7); no new AA-rated adds |
| AA–AAA spread (approx. 100–260 bp range [design_allocation.md]) | <150 bp | 150–260 bp | >260 bp | Same as above; consider trimming AA sleeve toward AAA |
| 10Y G-sec yield (current ~6.95–7.0% [design_allocation.md]) | ±25 bp of 3-month avg | ±25–75 bp move in a month | >75 bp move in a month | Duration-band review (Section 1 #8); propose shortening duration in next RPP |
| USDINR (spot ~₹88 [design_allocation.md]) | <1% monthly move | 1–3% monthly move | >3% monthly move | International-sleeve FX-hedge discussion; gold-sleeve check |
| Real rates (10Y G-sec − CPI YoY) | >1.5% | 0.5–1.5% | <0.5% or negative | Flag inflation-hedge assets (gold, TIPS-equivalent) for next IC |
| US VIX | <18 | 18–28 | >28 | Correlate with India VIX — a US-led spike with India VIX lagging is itself a warning of imported volatility |
| Brent crude (USD/bbl) | <$75 | $75–95 | >$95 | Re-run the "Oil +50%" hypothetical (Section 4) live |
| Valuation percentile — Nifty 50 forward P/E vs 10-yr history | <60th percentile | 60th–85th | >85th percentile | No new large-cap adds; tilt toward Value/Quality factor sleeves |
| Nifty 50 vs 200-DMA (trend filter) | >200-DMA, DMA rising | Within ±3% of DMA | <200-DMA and DMA falling | Momentum/trend-break trigger for the dynamic de-risking standing instruction (Section 5.3) |
| Rolling 60-day average pairwise sleeve correlation (Section 2.9) | <0.40 | 0.40–0.60 | >0.60 | "Correlations→1" regime flag; diversification benefit assumed in VaR is degrading — widen VaR by a stress multiplier until it normalises |

Colour rule for the dashboard: any **single Red** = same-day IC escalation email; **two or more Ambers** simultaneously = same-day IC flag even if none is individually Red (regime-change signal, not indicator-specific).

## 7. Tail-event playbook under NDPMS

**7.1 Standing instructions vs ad-hoc consent — the decision tree.**

1. Is the proposed action **already** inside a signed Standing Instruction (Section 1's Annex C register — cash sweep, distribution reinvestment, pre-approved tranche schedule, hedge auto-roll)? → **Execute same day**, log in the audit trail, no new consent needed.
2. Is it a **pre-agreed band-restoring trade** inside the current month's already-consented RPP (e.g., a rebalance the client approved 3 weeks ago that has simply not yet been executed)? → Execute within the RPP's validity window (10 trading days), no new consent needed.
3. Is it a **new** action — a fresh hedge, an off-cycle de-risk, a name outside the approved list, or any resizing? → **Ad-hoc consent required.** Draft a same-day mini-RPP (1–3 lines, plain-language rationale, cost estimate) and push it through every available consent channel (portal e-sign, phone confirmation logged and followed by email, RM in-person for the largest relationship) — do not wait for the normal monthly cycle.

**7.2 Who calls whom.**

| Horizon | Owner | Action |
|---|---|---|
| First hour | Risk desk → CIO/PM lead | Confirm the trigger is real (not a data error), size the P&L impact using Sections 2–4, decide if it needs ad-hoc consent or fits a standing instruction |
| First hour | CIO/PM lead → Compliance | Pre-clear the proposed mini-RPP against every limit in Section 1 before it goes to the client |
| Same day | PM lead → Client / family office / RM | Phone call within 2 hours of the trigger confirmation; follow with the written mini-RPP; log timestamps (this *is* the NDPMS audit trail and also the evidence used in Section 2.7's latency-cost reporting) |
| Day 1–2 | PM lead → IC | Formal IC note: what happened, what was proposed, what the client decided, what executed, residual risk |
| Week 1 | Compliance | File any SEBI-reportable event; check no active-breach limit was crossed intra-week |
| Week 1 | Attribution/Performance | Tag the episode in the TWRR engine so the "as-instructed" vs "as-recommended" gap is measurable (this is the direct evidence of NDPMS execution discipline for regulatory inspection) |

**7.3 Communication template (same-day client note).**
"[Date] — Trigger: [indicator, e.g. India VIX closed at X, +Y% day-on-day / Nifty broke 200-DMA]. Portfolio impact if unhedged: approx. ₹[Z] Cr ([%] of NAV) based on [scenario/stress reference]. Recommendation: [specific trade(s), ₹ amount, instrument]. Estimated cost/tax: ₹[A] Cr. This requires your consent under our non-discretionary mandate — please reply APPROVE / MODIFY / DECLINE via the portal or this email by [time]. Absent a response by [SLA], the recommendation lapses and current positioning continues unchanged." — the explicit lapse clause is what keeps "we recommended, they didn't answer" from being recharacterised as implied discretion.

**7.4 Legal note.** A playbook that pre-authorises "the PM may de-risk up to X% if indicator Y breaches Z" without a specific per-instance client consent risks recharacterisation as discretionary management on inspection — the design_regulatory.md finding stands here too (status: **unclear_verify**, get a legal opinion / consider SEBI Informal Guidance before treating any trigger-based rule as self-executing rather than consent-generating).

## 8. Dashboard specification

| Panel | Metrics | Source | Refresh | Alert threshold | Colour rule |
|---|---|---|---|---|---|
| Risk summary strip | 1-day/1-month VaR & CVaR (95/99), realised EWMA vol, beta, TE vs composite | `risk_calc` engine on daily position + NAV file | Daily (T+1 AM) | TE outside 2.5–6.0% (Mod) / TE <1.5% or >6% any sleeve | Navy background, green/amber/coral #E0402F number chips |
| Drawdown & recovery | NAV, peak, current DD, DD vs benchmark ratio, days since peak | TWRR engine (shared with performance dashboard) | Daily | >1.25× benchmark MDD or >−18% absolute | Coral fill below −18% line |
| Limit compliance grid | All 13 Section-1 limits, live utilisation % | Position + look-through file | Daily | Any limit >90% utilised (amber), breach (red) | Amber #F2A93C at 90%, coral at breach |
| Stress test panel | Section 3 historical + Section 4 hypothetical, applied to *today's* live weights (not the static table) | `risk_calc` re-run nightly on current weights | Daily (overnight batch) | Any scenario >−15% NAV | Bar chart, coral bars beyond −15% |
| Hedge book | Open derivative positions, notional %, running premium spend YTD vs 1% AUM budget, payoff-to-date | OMS/custodian derivative ledger | Daily | Premium spend >1% AUM p.a. run-rate | Amber at 0.75%, coral at 1.0% |
| Early-warning board | Section 6's 12 indicators, current value, 30-day sparkline, green/amber/red chip | Market data feed (NSE, NSDL FII data, RBI, CCIL) | Daily (indices), intraday optional for India VIX | Per Section 6 | Chip colours per Section 6 |
| Look-through concentration | Single-name, sector, AMC/manager, issuer-rating look-through across MF/AIF wrappers | Fund factsheets/portfolio disclosures (monthly lag for AIF) | Monthly (AIF), daily (direct + MF) | Any Section-1 limit breach on a look-through basis | Grey "stale" flag if AIF look-through >45 days old |
| Consent-latency log | Every ad-hoc RPP: trigger time, client response time, execution time, Section-2.7 cost estimate | RPP audit trail | Event-driven, rolled up weekly | Any single item >5 trading days to consent | Coral row highlight |
| Liquidity ladder | % liquidable in 1/5/10/30/90 days, stressed (ADV −50%) vs normal | Position file × ADV feed | Daily | <80% liquidable in 5 days | Coral |

**CAN:** build this as one HTML dashboard sharing the house palette and the same TWRR/position data pipeline as the IPS/attribution/deployment dashboards already in production — a fifth tab on the existing suite, not a new system. **SHOULD:** wire the early-warning board to push a same-day alert (email/Slack) on any Red, not just display it passively. **AVOID:** building a separate options-pricing or portfolio-construction system inside the dashboard — it is a monitor, not a trading system; all it should ever do is display numbers and log consent-latency, never originate an order.

## Sources

[1] SEBI (Portfolio Managers) Regulations, 2020, as last amended — https://www.sebi.gov.in/legal/regulations/feb-2025/securities-and-exchange-board-of-india-portfolio-managers-regulations-2020-last-amended-on-february-10-2025-_92413.html
[2] Vinod Kothari Consultants, "SEBI brings in revised norms for Portfolio Managers" — https://vinodkothari.com/2020/02/sebi-brings-in-revised-norms-for-portfolio-managers/
[3] SEBI Master Circular for Portfolio Managers, 16-Jul-2025 (via APMI) — https://www.apmiindia.org/storagebox/images/Circulars/Master%20Circular%20for%20Portfolio%20Managers%20-%2016th%20July'25.pdf
[4] SEBI circular SEBI/HO/IMD/IMD-I/DOF1/P/CIR/2022/112 (related-party investment limits and consent) — https://www.apmiindia.org/storagebox/images/Circulars/Related-Party-Circular-26thAug'22.pdf
[5] TaxGuru summary, SEBI (Portfolio Managers) Regulations, 2020 — https://taxguru.in/sebi/sebi-portfolio-managers-regulations-2020.html
[6] TaxGuru / Conventus Law / Cyril Amarchand Mangaldas summaries of the July-2026 SEBI consultation paper on comprehensive review of PMS Regulations (derivatives exposure to 1.25× AUM, unhedged shorts to 50% via equity ETD, 10% option-premium cap) — https://taxguru.in/sebi/sebi-invites-comments-comprehensive-review-portfolio-managers-regulations-2026.html ; https://corporate.cyrilamarchandblogs.com/2026/08/sebis-proposed-overhaul-of-the-pms-regulatory-framework/
[7] HDFC Sky, India VIX intraday update, 11/12-Sep-2026 — https://hdfcsky.com/news/india-vix-rises-4-66percent-to-12-42-as-oil-rupee-and-global-yields-pressure-indian-markets-september-11-2026
[8] Trendlyne / 5paisa India VIX profile (52-week range 8.72–28.90) — https://trendlyne.com/equity/178701/NIFTYVIX/india-vix/ ; https://www.5paisa.com/share-market-today/india-vix
[9] Kotak Neo market update, Nifty 50 close 10-Sep-2026 (23,477.80) — https://www.kotakneo.com/news/market-news/stock-market-update-7september-2026-sensex-nifty/
[10] Nifty lot-size change effective Jan-2026 (65 units) — https://www.venturasecurities.com/blog/nifty-bank-nifty-lot-size-changes-january-2026-know-how-it-impacts-traders/ ; https://algotest.in/blog/nifty-lot-size/
[11] India Macro Indicators, 10-year AAA vs G-sec credit spread, 15-Aug-2026 (2.21%) — https://indiamacroindicators.co.in/economic-indicators/10-year-credit-spread-aaa-rated-bonds-g-sec
[12] design_regulatory.md and design_allocation.md (this engagement, same session) — internal design documents, sleeve weights, composite benchmark definitions, TE/drawdown bands, and cited SEBI sources reused here for cross-document consistency.
