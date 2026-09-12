# Strategic Asset Allocation, House-View Implementation and Portfolio Construction — ₹500 Cr NDPMS Mandate

*Ionic Wealth (Angel One) · Design note for the CIO/PM team · As of 12 Sep 2026. Verified facts carry a bracketed source number; anything marked "approx." is an estimate or an unverified figure.*

## 0. Design stance in one paragraph

The mandate is ₹500 Cr under **non-discretionary** PMS: we recommend, the client consents, we execute. That single constraint drives everything below. We therefore (a) build the portfolio from a **pre-agreed Model Master with rebalance bands** so that the monthly consent pack is a short list of band-restoring and tilt trades rather than a fresh debate; (b) favour instruments that are **cheap to hold, cheap to trade and slow-moving** (index funds, ETFs via APs, target-maturity debt, quality-tilted direct stocks, listed REITs/InvITs) and keep high-turnover ideas inside vehicles where the manager holds the discretion (Cat III AIF, SIF long-short, third-party PMS); (c) use the NDPMS-only privilege of **up to 25% of client AUM in unlisted securities** (AIF units, unlisted debt) [1][2] deliberately but not fully — 9% Moderate / 12% Aggressive — to leave headroom; and (d) own the outcome with a **composite benchmark that is investable and matches the sleeve weights**, with the Allocate 80/20 house benchmark retained as a secondary reference.

Market context that matters for CMAs and deployment today: Nifty 50 ~23,200–23,500, a three-month low, trailing P/E ~19.8–20.2 vs a 10-yr median ~23.3 [23][24][25][26]; FY27E Nifty EPS growth consensus 15–17% but skewed to the downside on crude [27]; 10-yr G-sec 6.96% with repo at 5.25% [21][22]; USD/INR ~95.7 [42]; 10-yr AAA spread over G-sec ~221 bps and 3-yr ~111 bps per one tracker [30][31] (dealers quote AAA PSU 10–60 bps, AAA NBFC 50–140 bps, AA 100–260 bps [32]) — so the term-premium-plus-credit stack is unusually generous relative to the last five years.

---

## 1. Capital-market assumptions (10-year forward, INR, pre-tax, gross of our fees)

Method: forward equity return = dividend yield (~1.2%) + real earnings growth + inflation (~4.5%) ± valuation drift; Nifty 50 at ~20× trailing vs 23× median implies roughly +1% p.a. of valuation tailwind over 10 years, which we net against a slower nominal GDP path than the last decade. Bonds = current YTM ± roll. Gold = INR depreciation (~3.5% approx.) + real-rate/central-bank demand premium. Alternatives = manager target IRR net of fees, haircut 200–300 bps for selection risk. Correlations are to Nifty 50 TRI and are approx. unless sourced.

| Asset class (proxy) | Historical anchor (verified) | Fwd 10-yr E[R] | Fwd vol | Hist. max DD | Corr to Nifty 50 (approx.) | Notes |
|---|---|---|---|---|---|---|
| Indian large cap (Nifty 50 / 100 TRI) | Nifty 50 TRI 12.41% since inception (Jun-2026 factsheet), 12.44% 20-yr to Feb-2026; SD 20.7%, max DD −59.9% (2008) [16] | **11.0%** | 17% | −60% | 1.00 | Valuation now ~8% below 5-yr median [26] |
| Mid cap (Nifty Midcap 150) | 10-yr CAGR 19.2% (Feb-2026) [17]; −60.8% worst 12-mo (2008-09) [20]; 5-yr vol 19.0% vs 18.9% Nifty 100 [19] | **12.5%** | 21% | −65% approx. | 0.85 | Highest Sharpe of the three cap buckets historically (0.45 vs 0.29 Nifty) [17] |
| Small cap (Nifty Smallcap 250) | 10-yr CAGR 16.1% (Feb-2026) [17]; −69.1% in 2008; 2018-20 DD −46%, 591 trading days to recover [18] | **13.0%** | 25% | −70% | 0.78 | Loses to Midcap 150 in ~80% of 5-yr rolling windows [17] |
| Factor: Low Vol (Nifty 100 LV30) | Long-run premium vs Nifty 50 narrowed to lows in 2024-25 (approx.) | 10.5% | 14% | −45% approx. | 0.85 | Defensive; underperforms in sharp beta rallies |
| Factor: Momentum (Nifty 200 Mom 30) | Index fund 5-yr CAGR 11.6%, 1-yr ~+4% to −1% [51] | 13.0% | 21% | −60% approx. | 0.80 | Highest turnover (~semi-annual rebalance), crash-prone at turns |
| Factor: Quality (Nifty 200 Q30) | ETF 5-yr 9.66%, 1-yr −3.2% (Aug-2026) [52] | 11.0% | 16% | −50% approx. | 0.90 | Cheap now after 3-yr lag; fits "large-cap quality" house view |
| Factor: Value (Nifty 500 Value 50) | Nifty 500 TR 5-yr 12.4%, 1-yr −1.7% (Jun-2026) [53] | 12.0% | 19% | −60% approx. | 0.90 | Cyclical/PSU-heavy; pairs with Quality |
| Short duration / money market (1–3 yr) | Liquid fund 1-yr 6.4% (Sep-2026) [50]; SDL 1.5-yr index YTM ~6.0% (2025) | 6.6% | 1.2% | ~0 | 0.05 | Slab-taxed |
| Target maturity 3–5 yr (AAA PSU/SDL) | Bharat Bond 2030 5-yr 6.83% (Jul-2026) [56] | 6.9% | 2.5% | −4% approx. | 0.05 | Hold-to-maturity; slab-taxed |
| 10-yr G-sec | Nifty 10-yr G-sec index 1-yr 5.17%, 3-yr 7.80%, 5-yr 5.51% [54][55]; YTM 6.96% [21] | 7.0% | 5.5% | −10% approx. | 0.10 | Duration lever for house view |
| AAA corporate 3–5 yr | 3-yr AAA spread ~111 bps [31] | 7.1% | 2.5% | −4% approx. | 0.05 | Prefer via TMF/index funds for scale |
| AA corporate credit | AA spread 100–260 bps [32] | 8.2% | 3.5% | −8% approx. | 0.15 | Concentration limits; 4% cap Moderate |
| Arbitrage / liquid / overnight | Kotak Equity Arbitrage 1-yr 6.72% (Sep-2026), AUM ₹74,399 Cr [48][49] | 6.2% | 0.7% | ~0 | 0.05 | Equity-taxed (12.5% LTCG) — the parking asset |
| Gold (INR) | 10-yr CAGR ~11.1% to ~15% depending on window [33][34]; ATH ₹1,69,349/10g Mar-2026 [34] | 8.0% | 15% | −25% approx. (2013-15 INR) | −0.10 | Gold ETF AUM ₹1.85 lakh Cr May-2026 [47] |
| Silver (INR) | SD 26.6%, max DD −54% (Motilal study) [35]; ₹2,36,860/kg Aug-2026 [36]; 1-yr +78% to Oct-2025 | 8.5% | 27% | −54% | 0.20 | Cap at 1%; ETF outflows ₹2,133 Cr May-2026 on profit booking [47] |
| REIT / InvIT (Nifty REITs & InvITs) | Index 1-yr +22.1% (Apr-2026); Embassy dist. yield ~6.5%, IndiGrid 9–10% [37][38] | 9.5% | 14% | −40% approx. (2020) | 0.35 | Yield 6–10% of which part is tax-free return of capital |
| International DM equity in INR (S&P 500 / MSCI World) | S&P 500 10-yr 15.2% USD (Aug-2026) [39]; MSCI World 10-yr 15.6% net USD (Jun-2026) [40]; MO S&P 500 fund 5-yr 17.6% INR [41]; INR ~66→95.7 over 10 yrs ≈ 3.7% p.a. approx. [42] | 10.5% | 16% | −35% approx. in INR | 0.45 | Access constrained by USD 7 bn industry cap [28][29] |
| Cat II private credit AIF | Net 12–16% historically; 12–15% target senior secured [57][58] | 11.5% net pre-tax | 4% (smoothed; economic ~10%) | −15% approx. | 0.20 | Pass-through; interest at slab ~39% [14] |
| Cat III long-short AIF / SIF hybrid LS | Trust-level tax up to ~42.7% [15]; SIF AUM ₹13,814 Cr May-2026, 76% in hybrid LS [10] | 10.0% net pre-tax | 9% | −20% approx. | 0.40 | Buys us discretion inside a wrapper |
| Pre-IPO / PE (Cat II) | Target IRR 18–22% gross approx.; J-curve 3–4 yrs | 15.0% | 25% | −40% approx. | 0.50 | Aggressive only, 3% |

**Reading the table.** The house risk asset (large cap) is priced to deliver ~11% nominal; the "extra" for mid/small is +150–200 bps for +4–8 points of vol and much deeper drawdowns — worth owning through the cycle but sized, not chased. Bonds at 6.6–7.1% with near-zero equity correlation give a 4–5-point carry deficit to equity, the lowest in a decade, so the Moderate book can hold 24% fixed income without a large return sacrifice. Gold's expected 8% is below its trailing 11–15% because the last three years front-loaded the central-bank bid.

---

## 2. Sleeve architecture and instrument-choice logic

### 2.1 Five sleeves

| Sleeve | Purpose | Moderate | Aggressive | Instruments | Rebalance band |
|---|---|---|---|---|---|
| **Core beta** | Cheap, capacity-unlimited exposure to Indian large cap + factor tilts | 32% | 37% | Nifty 50/100 ETFs (AP creation), index funds; factor index funds (Quality, Low Vol, Momentum) | ±5% sleeve / ±2% per factor |
| **Satellite alpha** | Where we own stock/manager selection: NIFTY-750 scorecard direct stocks, active mid/small MFs, 1 third-party PMS, international | 33% | 44% | Direct stocks 20–25 names; 2–3 active MFs; 1 PMS (₹10–15 Cr); 1–2 international index funds | ±3% sleeve / ±1.5% per line |
| **Alternatives** | Return sources not available in listed markets; manager discretion inside wrapper | 9% | 12% | Cat II private credit (2 funds), Cat III long-short or SIF hybrid LS (1–2), pre-IPO/PE (Aggressive) | ±2%; no forced rebalancing (illiquid) |
| **Stabilisers** | Drawdown control and carry | 24% (FI) + 4% (REIT/InvIT) + 6% (gold/silver) | 8% + 2% + 5% | TMF index funds, 10-yr G-sec ETF/dynamic fund, AA credit via debt funds, gold ETF, silver ETF, 4–5 REIT/InvITs | ±3% FI / ±1.5% gold / ±1% REIT |
| **Liquidity** | Fee/tax/consent-latency buffer, deployment parking | 2% | 2% | Arbitrage fund (equity-taxed), overnight fund | 1–4% hard range |

### 2.2 Instrument decision matrix

Score each candidate 1–5 on six criteria; weight cost 20%, tax 20%, liquidity 15%, capacity 15%, alpha evidence 15%, NDPMS consent friction 15%. Anything <3.0 is not used.

| Vehicle | Cost (TER/impact, bps p.a.) | Tax treatment | Liquidity | Capacity at ₹500 Cr | Alpha evidence needed | NDPMS consent friction | Use case verdict |
|---|---|---|---|---|---|---|---|
| Index ETF via AP creation unit | 3–10 TER + 5–15 impact | Equity: 12.5% LTCG >12m [12][13] | T+1 on-screen; T+2 creation | Unlimited (Nifty BeES AUM ₹66,777 Cr; CU = 50,000 units) [43][44] | None | Low — one instruction per tranche | **Core beta, gold** |
| Index fund (direct plan) | 10–20 TER, zero impact | Same as ETF | T+2/T+3 redemption | Unlimited | None | Lowest — NAV order, no price risk in consent lag | **Core beta, factor, international** |
| Active MF (direct plan) | 60–110 TER | Equity 12.5%/20% | T+2/T+3 | Scheme-size watch: our ticket ≤1% of scheme AUM | 3-yr rolling alpha >150 bps net in ≥60% of windows | Low | **Active mid/small only** |
| Third-party PMS | 100–250 + perf fee | Pass-through of stock trades in client name; STCG churn risk | 1–4 weeks | Min ₹50 lakh [1][2]; manager capacity | 5-yr live track, information ratio >0.4, style stable | Low once onboarded; high to change | **One concentrated manager, ≤3%** |
| Direct stocks (in-house scorecard) | 0 TER; 15–40 impact; brokerage | 12.5%/20%; we control realisation | 1–3 days at 20% ADV | Position ≤1% of float, ≤20% ADV | Scorecard evidence (live Allocate record) | **Highest** — every trade is a line item in the consent pack | **8–12% cap; low turnover names** |
| AIF Cat II | 150–200 + carry | Pass-through; interest at slab ~39% [14] | Locked 3–7 yrs, close-ended min 3 yrs [60][61] | Min ₹1 Cr per fund [7]; unlisted cap 25% NDPMS [1][2] | Manager DPI/IRR history, default record | Low after commitment (drawdowns pre-consented) | **Private credit, PE** |
| AIF Cat III | 150–250 + perf | Fund-level tax up to ~42.7% [15] | Monthly/quarterly, soft lock 1–3 yrs [61] | Min ₹1 Cr [7] | Net-of-tax Sharpe > 0.8 | Low | **Long-short, hedged** |
| SIF (MF platform) | 100–150 approx. | MF taxation by category (equity-oriented hybrid LS → equity rates likely; verify per scheme) | Daily–quarterly, notice ≤15 working days [11] | Min ₹10 lakh [9]; nascent AUM ₹13,814 Cr [10] | 12–18 months live track minimum | Low | **Prefer over Cat III LS once track exists — cheaper tax** |
| Bonds direct (G-sec/SDL/corporate) | 0 TER; 5–25 bps bid-offer | Coupon at slab; LTCG 12.5% >12m listed | G-sec T+1 deep; corporate patchy | Fine for G-sec; corporate lots ₹1–5 Cr | None | Medium — each ISIN a line item | **10-yr G-sec direct; corporate via funds** |
| REIT/InvIT listed | 0 TER; 10–30 impact | Dividend part exempt, interest at slab, LTCG 12.5% >12m | 1–5 days | 4–5 names, each ≤₹6 Cr | None | Low | **Stabiliser yield** |

**Decision rule for active vs passive.** Passive unless the sleeve passes all three: (i) documented persistence of manager alpha in that segment (Indian mid/small yes; large cap no), (ii) our ticket ≤1% of scheme AUM so we do not move the manager's book, (iii) the net-of-tax expected alpha exceeds the TER differential by ≥100 bps.

---

## 3. Model portfolios sized to ₹500 Cr

### 3.1 Moderate / balanced (target: house-benchmark return at ~70% of its risk)

| Sleeve / line | % | ₹ Cr | Instrument | # lines | E[R] contrib (pp) | Risk contrib (%) | Days to liquidate at 20% ADV | Band |
|---|---|---|---|---|---|---|---|---|
| Nifty 50 / Nifty 100 passive | 22 | 110 | 2 ETFs via AP + 1 index fund | 3 | 2.42 | 37.6 | 1–2 (creation route) | ±5 |
| Factor blend (Quality 5 / Low Vol 3 / Momentum 2) | 10 | 50 | Index funds | 3 | 1.15 | 16.4 | 2–3 | ±2 each |
| Active mid cap | 7 | 35 | 2 active MFs | 2 | 0.88 | 13.4 | 3 | ±1.5 |
| Active small cap | 3 | 15 | 1 active MF or PMS | 1 | 0.39 | 6.4 | 3–10 | ±1 |
| Direct stocks (scorecard, quality tilt) | 8 | 40 | 20–25 names, avg ₹1.6–2 Cr | 22 | 1.00 | 14.5 | 1–3 | ±3 sleeve / 50 bps per name |
| International DM (S&P 500 / MSCI World) | 5 | 25 | 1–2 index funds / FoF | 2 | 0.52 | 4.1 | 3–5 (if open) | ±1.5 |
| Short duration / money market | 3 | 15 | 1 fund | 1 | 0.20 | 0.0 | 1 | ±1 |
| Target maturity 3–5 yr AAA/SDL | 11 | 55 | 2 TMF index funds/ETFs | 2 | 0.76 | 0.3 | 2 | ±3 |
| 10-yr G-sec / dynamic duration | 6 | 30 | Direct G-sec + 1 ETF | 2 | 0.42 | 0.6 | 1 | ±2 |
| AA corporate credit | 4 | 20 | 1–2 credit-risk/corporate bond funds | 2 | 0.33 | 0.3 | 3–5 | ±1 |
| Arbitrage / overnight | 2 | 10 | 1 arbitrage fund | 1 | 0.12 | 0.0 | 1–2 | 1–4 |
| Gold | 5 | 25 | 1 gold ETF (AP route) | 1 | 0.40 | 0.0 | 1 | ±1.5 |
| Silver | 1 | 5 | 1 silver ETF | 1 | 0.08 | 0.8 | 1 | ±0.5 |
| REIT / InvIT | 4 | 20 | 4–5 listed trusts | 5 | 0.38 | 3.0 | 2–5 | ±1 |
| Cat II private credit AIF | 5 | 25 | 2 funds | 2 | 0.58 | 0.5 | Locked 3–5 yrs | n/a |
| Cat III long-short / SIF hybrid LS | 4 | 20 | 1–2 | 2 | 0.40 | 1.9 | 30–90 | n/a |
| **Total** | **100** | **500** | | **~52** | **10.03** | **100** | 80% of book in ≤5 days | |

Unlisted exposure = 9% (AIF units) vs 25% NDPMS ceiling [1][2]. Equity-like beta to Nifty ≈ 0.55.

### 3.2 Aggressive / growth (target: beat house benchmark by ≥100 bps at ≤ its risk)

| Sleeve / line | % | ₹ Cr | Instrument | # lines | E[R] contrib (pp) | Risk contrib (%) | Days to liquidate | Band |
|---|---|---|---|---|---|---|---|---|
| Nifty 50 / 100 passive | 25 | 125 | 2 ETFs + 1 index fund | 3 | 2.75 | 33.0 | 1–2 | ±5 |
| Factor blend (Quality 5 / Momentum 4 / Low Vol 3) | 12 | 60 | Index funds | 3 | 1.38 | 15.2 | 2–3 | ±2 each |
| Active mid cap | 10 | 50 | 2 MFs + 1 PMS (₹15 Cr) | 3 | 1.25 | 14.9 | 3–20 | ±2 |
| Active small cap | 5 | 25 | 1–2 MFs | 2 | 0.65 | 8.4 | 3–5 | ±1.5 |
| Direct stocks (scorecard) | 12 | 60 | 25 names, avg ₹2.4 Cr | 25 | 1.50 | 16.9 | 1–4 | ±3 / 60 bps per name |
| International DM | 7 | 35 | 2 index funds/FoF | 2 | 0.74 | 4.5 | 3–5 | ±2 |
| Short duration | 2 | 10 | 1 fund | 1 | 0.13 | 0.0 | 1 | ±1 |
| Target maturity | 4 | 20 | 1 TMF | 1 | 0.28 | 0.1 | 2 | ±1.5 |
| 10-yr G-sec | 2 | 10 | Direct | 1 | 0.14 | 0.1 | 1 | ±1 |
| Arbitrage / overnight | 2 | 10 | 1 | 1 | 0.12 | 0.0 | 1–2 | 1–4 |
| Gold | 4 | 20 | 1 ETF | 1 | 0.32 | −0.2 | 1 | ±1.5 |
| Silver | 1 | 5 | 1 ETF | 1 | 0.08 | 0.5 | 1 | ±0.5 |
| REIT / InvIT | 2 | 10 | 3 | 3 | 0.19 | 1.1 | 2–5 | ±1 |
| Cat II private credit | 4 | 20 | 2 | 2 | 0.46 | 0.3 | Locked | n/a |
| Cat III LS / SIF | 5 | 25 | 2 | 2 | 0.50 | 1.9 | 30–90 | n/a |
| Pre-IPO / PE Cat II | 3 | 15 | 1–2 | 2 | 0.45 | 3.3 | Locked 5–7 yrs | n/a |
| **Total** | **100** | **500** | | **~53** | **10.94** | **100** | 75% in ≤5 days | |

Unlisted = 12%. Beta ≈ 0.72.

### 3.3 Portfolio-level statistics vs benchmarks (model outputs on the CMAs above; correlations approx.)

| Metric | Allocate 80/20 house benchmark | Moderate | Aggressive | Proposed composite (Mod) | Proposed composite (Agg) |
|---|---|---|---|---|---|
| E[R] (pre-tax, gross fees) | 10.0% | 10.0% | 10.9% | 9.5% | 10.5% |
| Vol | 13.6% | 9.7% | 12.5% | 9.9% | 13.6% |
| Sharpe (Rf 6.0%) | 0.30 | 0.42 | 0.39 | 0.35 | 0.33 |
| Beta to Nifty 50 | 0.80 | 0.55 | 0.72 | 0.58 | 0.79 |
| 1-yr 95% VaR (parametric) | −12.4% | −5.9% | −9.7% | | |
| Heuristic expected max DD (≈2.6×vol) | −35% | −25% | −33% | | |
| GFC-type shock (2008 asset-class moves) | −42.6% | −29.5% | −39.8% | −29.2% | −42.7% |
| COVID-type shock (Feb–Mar 2020) | −29.4% | −19.7% | −26.8% | −19.5% | −28.7% |
| 2022 rate/inflation shock | −7.2% | −5.4% | −7.8% | −5.2% | −8.1% |
| Tracking error vs 80/20 | — | 4.8% | 3.2% | | |
| Tracking error vs own composite | — | 1.5% | 2.1% | | |
| Expected alpha vs own composite | — | +55 bps | +45 bps | | |

**Composite benchmark proposal.** Moderate: **55% Nifty 500 TRI + 5% S&P 500 TRI (INR) + 25% CRISIL Composite Bond Fund Index + 5% domestic gold price + 10% Nifty 50 Arbitrage Index**. Aggressive: **75% Nifty 500 TRI + 7% S&P 500 TRI (INR) + 8% CRISIL Composite Bond + 5% gold + 5% Nifty 50 Arbitrage**. Rationale: investable, published daily, weights match the SAA, and it prices the alternatives sleeve at its public-market equivalent (private credit → bond index + our target 300 bps hurdle reported separately; long-short → arbitrage + 50% Nifty). Keep the Allocate 80/20 as a secondary line on every report so clients and RMs can compare with the Allocate book; a Moderate book that matches the 80/20 return at 70% of its vol is the honest story, not "beat 80/20".

---

## 4. Capacity and liquidity at ₹500 Cr

| Item | Constraint | Number | Implication for us |
|---|---|---|---|
| ETF on-screen vs creation | All-ETF ADV ₹4,200 Cr (Apr-25–Feb-26) but equity ETFs only ~₹745 Cr/day, commodity ~₹2,700 Cr [45] | A ₹50 Cr Nifty ETF tranche = ~7% of equity-ETF ADV | Route any ETF order >₹5 Cr via AP/creation unit (Nifty BeES CU 50,000 units ≈ ₹1.2 Cr approx.) [43]; on-screen only for <₹2 Cr top-ups |
| Direct stock position | ≤20% of 20-day ADV per day; ≤1% of free float; min ADV ₹20 Cr for inclusion | ₹2 Cr avg position → 1 day at ADV ₹10 Cr | NIFTY-750 universe filtered to ~450 names with ADV ≥₹20 Cr (approx.); no stock >3% of book |
| MF scheme size | Our ticket ≤1% of scheme AUM; ≤5% for TMF/index (passive) | ₹25 Cr mid-cap fund → scheme AUM ≥₹2,500 Cr | Excludes boutique small-cap funds; use PMS for boutique exposure |
| AIF minimums | ₹1 Cr per investor per fund [7]; Cat I/II close-ended ≥3 yrs [60]; LVF ₹25 Cr [7] | 6–8 AIF commitments of ₹5–15 Cr | Client is the unit-holder (PMS invests in client name); accredited-investor status (₹5 Cr securities-assets route proposed Aug-2026) may lower thresholds [8] |
| Unlisted cap (NDPMS) | 25% of client AUM incl. AIF units, REITs/InvITs only if unlisted [1][2] | ₹125 Cr ceiling; we use ₹45–60 Cr | Headroom for opportunistic pre-IPO or unlisted debt; SEBI Jul-2026 consultation may add overseas + 10% unlisted debt for discretionary PMS [5][6] |
| Third-party PMS | ₹50 lakh minimum [1][2] | 1 manager at ₹10–15 Cr | Concentrated mid/small specialist; avoid 3+ PMS (reporting sprawl) |
| International | Industry cap USD 7 bn, per-AMC USD 1 bn, USD 1 bn ETF sub-pool; several AMCs paused inflows May-2026 [28][29] | ₹25–35 Cr needed | Build 2 feeder routes + 1 international ETF; be ready to hold as arbitrage if windows shut |
| Corporate bonds direct | Lots ₹1–5 Cr, patchy secondary | ₹20 Cr AA sleeve | Use funds, not direct paper, below ₹50 Cr sleeve |
| Line-item count | Consent-pack readability; ops reconciliation | 50–55 lines Moderate, 53 Aggressive | Hard cap 60; every line must be ≥₹1.5 Cr (30 bps) except silver |

Liquidity ladder (Moderate): 42% same/next day (ETFs, G-sec, arbitrage, gold), 38% in 2–5 days (funds, stocks, REITs), 4% in 30–90 days (Cat III/SIF), 9% locked, 7% TMF (liquid but with mark-to-market if pre-maturity).

---

## 5. Translating the monthly house view into TAA

### 5.1 Framework

1. **SAA is the contract.** Model Master weights + bands are in the IPS schedule the client signs at onboarding. Band-restoring trades need only a confirmation, not a deliberation.
2. **TAA is the IC's monthly vote**, expressed as conviction scores C ∈ {−3…+3} per "view axis" (large vs mid/small; quality vs value/momentum; duration; credit; gold; international; alternatives pace).
3. **Sizing rule:** tilt (pp) = C × unit, where unit = TE budget ÷ (Σ|C| × view vol), capped by the sleeve band. With TE budget 2.0% (Moderate) / 3.0% (Aggressive) vs own composite, and typical view vols, a unit is ~1.0 pp Moderate / 1.5 pp Aggressive.
4. **Evidence bar to move:** a view must clear at least two of three — (a) valuation z-score |z| ≥1 vs 10-yr history, (b) earnings/macro revision breadth in the direction of the view for ≥2 months, (c) scorecard pillar spread (quality/momentum) in top or bottom quintile. A C=±3 requires all three plus IC unanimity.
5. **Decay:** each tilt carries a 6-month review; if not reaffirmed it halves automatically at the next consent pack.

### 5.2 Worked example (Moderate, September 2026 IC): overweight large-cap quality (+2), underweight small cap (−2), duration long (+2), gold neutral (0)

| View axis | C | Unit (pp) | Tilt (pp) | From → To | ₹ Cr moved | Instrument | Band check |
|---|---|---|---|---|---|---|---|
| Large-cap quality | +2 | 1.0 | +2.0 | Quality factor 5 → 7 | +10 | Nifty 200 Quality 30 index fund | within ±2 |
| Small cap | −2 | 1.0 | −2.0 | Active small 3 → 1 | −10 | Redeem small-cap MF | within ±1… breach → cap at −1 (₹5 Cr) and take remaining −1 from mid cap |
| Duration | +2 | 1.0 | +2.0 | 10-yr G-sec 6 → 8; TMF 11 → 9 | +10 / −10 | Direct 7.xx% 2036 G-sec | within ±2 |
| Gold | 0 | — | 0 | 5 → 5 | 0 | — | — |
| Net | | | | | ~₹35 Cr gross turnover ≈ 7% | | Estimated TE added ≈ 0.6% |

Consent pack for that month therefore has **5 lines of TAA + band restorations**, all executable on the Thursday deployment cycle.

### 5.3 Governance thresholds

| Item | Threshold |
|---|---|
| Max aggregate active weight vs SAA | 10 pp Moderate / 15 pp Aggressive |
| Max TAA turnover per month | 10% of NAV (tax and consent-latency discipline) |
| TE budget vs composite | 2.0% / 3.0% ex-ante; hard stop 3.0% / 4.5% |
| Minimum trade size | ₹1 Cr (20 bps) — smaller drifts wait for next month |
| Tilt review | 6 months, auto-halve if not reaffirmed |
| Emergency (intra-month) | Only band breaches >1.5× band or a tail-risk trigger (Nifty −10% from 20-day high, India VIX >25, 10-yr yield ±50 bps in a month) → ad-hoc consent request within 2 business days |

---

## 6. Deployment plan for fresh ₹500 Cr

**Baseline: 12 weekly Thursday tranches for equity-like sleeves, 4 for fixed income, alternatives on manager drawdown schedules over 6–18 months.** All undeployed equity money sits in an arbitrage fund (6.2% E[R], equity-taxed) rather than liquid (slab-taxed) — the tax choice alone is worth ~15 bps on the parked balance for a 39%-slab client.

| Week | Equity-like (60% Mod = ₹300 Cr) | Fixed income (24% = ₹120 Cr) | Alternatives (9% = ₹45 Cr) | Parked in arbitrage (approx.) |
|---|---|---|---|---|
| 0 (T) | ₹25 Cr (8.33%) | ₹30 Cr | Commitments signed | ₹445 Cr |
| 1–3 | ₹25 Cr/wk | ₹30 Cr/wk (done by wk 3) | — | ₹340 → ₹280 Cr |
| 4–11 | ₹25 Cr/wk | — | Drawdowns as called (typ. 25%/qtr) | ₹255 → ₹55 Cr |
| 12 | Final ₹25 Cr | — | — | ₹45 Cr (= alt commitments + 2% buffer) |

**Acceleration rules (pre-consented in the deployment schedule so no fresh instruction is needed):**
- Nifty 50 closes ≥5% below the level at T: pull forward one extra tranche (₹25 Cr) that week.
- ≥10% below: pull forward two extra tranches; ≥15%: deploy all remaining equity within 2 weeks.
- India VIX >22 for 3 consecutive days: same as −5% trigger.
- Conversely, if Nifty is ≥8% above T, do **not** decelerate — stick to schedule (asymmetric rule avoids chasing).
- Fixed income: if 10-yr yield rises ≥25 bps from T, pull forward the duration tranche.

**Expected cash drag (model):** equity-like sleeve deployed linearly over 12 weeks carries an average 6.5 weeks of the ~5-point gap between equity E[R] and arbitrage → **≈ ₹2.0 Cr Moderate / ₹2.5 Cr Aggressive** (40–50 bps of NAV, one-off). Fixed income drag ≈ ₹0.05 Cr. Alternatives drag ≈ ₹1.2–1.6 Cr (committed but undrawn for ~6 months on average). Compressing to 8 weeks cuts equity drag to ₹1.4–1.7 Cr but raises timing variance; at today's 20× P/E and a market already −6% off highs, the IC should choose 8 weeks with the acceleration rules armed.

---

## 7. NDPMS feasibility map (CAN / SHOULD / AVOID)

| Element | Status | Note |
|---|---|---|
| Pre-agreed Model Master + bands in IPS schedule | **SHOULD** (allowed with consent) | Turns rebalancing into confirmation |
| Standing instruction for band-restoring trades within ±X% | **UNCLEAR — verify** | Reg 22(1) requires a written agreement [3]; whether a pre-authorised execution matrix meets "on client instruction" needs legal opinion; design the pack so it works without it |
| Monthly batched consent pack (Thursday cycle) | **MUST** | The operating heartbeat |
| Index funds/ETFs via AP | **CAN / SHOULD** | Lowest friction, no price risk during consent lag |
| Active MF direct plans | **CAN** | Master Circular requires direct plans for PM-routed MF investments [4] (verify clause) |
| Direct stocks, 20–25 names, low turnover | **CAN, sized ≤12%** | Each trade a consent line; keep turnover <30% p.a. |
| Third-party PMS (1 manager) | **CAN** | Client signs PMS agreement directly; we monitor |
| AIF Cat II/III up to 25% | **CAN (NDPMS privilege)** | Discretionary PMS cannot [1][2]; we use ≤12% |
| SIF hybrid long-short | **CAN, small** | ₹10 lakh min [9]; track record still <18 months |
| Unlisted pre-IPO | **CAN, Aggressive only 3%** | Valuation/reporting burden |
| Intraday, HFT, options overwriting in client account | **AVOID / not feasible** | Consent latency makes them uneconomic; do inside Cat III/SIF wrappers instead |
| Momentum factor as >5% standalone | **AVOID (Moderate)** | Turnover and crash risk at turns; fine at 2–4% |
| Silver >1%, single-stock >3%, single AIF >4% | **AVOID** | Concentration |
| Overseas direct stocks | **Not allowed today**; SEBI Jul-2026 consultation proposes to allow [5][6] | Revisit when final |
| Pooled account / omnibus execution | **Not allowed** | Client-name holding; per-client ISIN tracking |

---

## 8. Costs and taxes that we own (bps p.a. of NAV, Moderate)

| Layer | Estimate | Comment |
|---|---|---|
| Weighted TER (passive 8 bps × 37%, active MF 80 × 10%, alts 180 × 9%, FI funds 25 × 20%, others 0) | ~40 bps | vs ~60 bps for an all-active book |
| Trading impact + brokerage (7% TAA + 10% band turnover + 3% direct-stock churn) | ~8 bps | |
| Consent latency cost (avg 3-day lag × 20% of NAV traded p.a. × 17% vol × √(3/252)) | ~6 bps expected, ±30 bps at 1σ | The NDPMS tax — design around it |
| Realised tax drag (equity LTCG 12.5% on ~8% turnover gains; slab on FI coupons; ~39% on private-credit interest) | 60–80 bps approx. | Largest owned cost — governs turnover discipline |
| Cash drag (steady state 2% arbitrage vs equity) | ~10 bps | |
| **Total controllable** | **~125–145 bps** | Report monthly against this budget |

Tax reference (verified): equity LTCG 12.5% above ₹1.25 lakh, STCG 20%, >12-month holding [12][13]; debt fund units bought after 1-Apr-2023 taxed at slab; "specified mutual fund" narrowed from 1-Apr-2026 to >65% debt [13]; Cat II pass-through with interest at slab ~39% for top-bracket investors [14]; Cat III taxed at fund level up to ~42.7% [15].

---

## 9. Build sequence (first 6 months)

1. **Week 0–2:** Sign IPS with Model Master, bands, deployment schedule + acceleration rules, composite benchmark. Legal opinion on standing-instruction scope.
2. **Week 0–4:** Open AP relationships for Nifty/gold ETFs; select 2 TMF funds, 2 mid-cap funds, 1 small-cap fund, 2 international feeders (+1 backup), 4–5 REIT/InvITs; run scorecard for the 22-name direct book.
3. **Week 0–12:** Execute deployment per §6; first monthly consent pack in week 5.
4. **Month 2–3:** Complete AIF diligence (2 private credit, 1 long-short, 1 SIF); sign commitments; unlisted-cap monitor live.
5. **Month 3:** First TAA cycle with conviction scoring; TE attribution vs composite live in the dashboard.
6. **Month 6:** Review CMAs, bands and line count; decide on standing instructions if legal opinion supports; decide on PMS/SIF additions.

---

## Sources

[1] SEBI FAQ – Portfolio Managers (Oct 2020): https://www.sebi.gov.in/sebi_data/faqfiles/oct-2020/1603946323909.pdf
[2] Shardul Amarchand Mangaldas – SEBI (Portfolio Managers) Regulations 2020: https://www.amsshardul.com/insight/sebi-portfolio-managers-regulations-2020/
[3] SEBI (Portfolio Managers) Regulations, 2020 [amended 03-Sep-2025]: https://www.sebi.gov.in/legal/regulations/sep-2025/securities-and-exchange-board-of-india-portfolio-managers-regulations-2020-last-amended-on-september-03-2025-_96560.html
[4] APMI – Master Circular for Portfolio Managers (7 Jun 2024): https://www.apmiindia.org/storagebox/images/Circulars/Master%20Circular%20for%20Portfolio%20Managers%20-%207th%20June'24.pdf
[5] Moneylife – SEBI PMS reform consultation (Jul 2026): https://www.moneylife.in/article/sebi-unveils-sweeping-reforms-for-portfolio-managers-proposes-overseas-investing-simplified-regulations-and-new-mfpms-framework/81148.html
[6] WealthMunshi – SEBI PMS overhaul 2026: https://wealthmunshi.com/sebi-pms-overhaul-2026-mf-pms-nri-impact/
[7] ElementOne – SEBI AIF Regulations 2026 guide: https://elementone.fund/sebi-aif-regulations-2026-guide/
[8] Rurash – SEBI accredited investor review 2026: https://rurashfin.com/sebi-accredited-investor-review-2026/
[9] Groww – SEBI SIF framework: https://groww.in/blog/specialised-investment-funds
[10] Finnovate – SIF explained (2026): https://www.finnovate.in/learn/blog/what-is-specialized-investment-fund-sif-explained
[11] Cyril Amarchand – SIF new product: https://privateclient.cyrilamarchandblogs.com/2025/06/specialized-investment-funds-new-investment-product-of-the-hour/
[12] Bajaj AMC – LTCG on mutual funds 2026: https://www.bajajamc.com/knowledge-centre/common-things-to-know-about-ltcg-on-mutual-funds
[13] WealthMunshi – Capital gains tax on MFs 2026: https://wealthmunshi.com/capital-gains-tax-on-mutual-funds-india-2026/
[14] GreenPortfolio – AIF taxation 2026: https://greenportfolio.co/blog/aif-taxation-india-2026-category-1-2-3-comparison/
[15] Finnovate – Cat III AIF: https://www.finnovate.in/learn/blog/aif-category-iii-india
[16] Bajaj AMC – Nifty 50 historical returns: https://www.bajajamc.com/knowledge-centre/nifty-50-historical-returns
[17] PersonalFinancePlan – Nifty 50 vs Midcap 150 vs Smallcap 250 (2005–2026): https://personalfinanceplan.in/nifty-50-vs-midcap-150-vs-smallcap-250-vs-nifty-500-cap-based-indices-performance-comparison-2005-2026/
[18] Zerodha In the Money – Nifty 500 / Midcap 150 / Smallcap 250: https://inthemoneybyzerodha.substack.com/p/nifty-500-midcap-150-smallcap-250
[19] Zerodha Fund House – Nifty LargeMidcap 250 factsheet: https://assets.zerodhafundhouse.com/indices/NIFTY_LargeMidcap_250/factsheet.pdf
[20] bmsmoney – Nifty Midcap performance trends: https://www.bmsmoney.com/article/full/nifty-midcap-index-performance-trends/
[21] Trading Economics – India 10Y: https://tradingeconomics.com/india/government-bond-yield
[22] India Macro Indicators – 10Y G-sec: https://indiamacroindicators.co.in/economic-indicators/10y-g-sec-yield
[23] Kotak Neo – Market update 7 Sep 2026: https://www.kotakneo.com/news/market-news/stock-market-update-7september-2026-sensex-nifty/
[24] Univest – Nifty 50 prediction 7 Sep 2026: https://univest.in/blogs/nifty-50-prediction-for-monday-7-september-2026
[25] India Macro Indicators – Nifty 50 P/E: https://indiamacroindicators.co.in/key-economic-indicators/nifty-50-pe-ratio
[26] IndexPE – Nifty 50: https://indexpe.in/nifty-50
[27] Business Standard – JM Financial Q4FY26 / FY27 EPS: https://www.business-standard.com/markets/news/nifty50-earnings-outlook-deep-dive-hits-misses-of-q4fy26-earnings-season-jm-financial-126061101166_1.html
[28] Vested – SEBI overseas limits: https://vestedfinance.com/in/globed/accessing-global-markets/global-investing-through-domestic-funds-and-etfs/sebi-limits-on-overseas-investment-by-mutual-funds/
[29] MFReturns – USD 7 bn cap 2026: https://mfreturns.com/blog/why-international-mutual-funds-closed-sebi-cap-2026/
[30] India Macro Indicators – AAA vs G-sec 10Y spread: https://indiamacroindicators.co.in/economic-indicators/10-year-credit-spread-aaa-rated-bonds-g-sec
[31] India Macro Indicators – AAA vs G-sec 3Y spread: https://indiamacroindicators.co.in/economic-indicators/3-year-credit-spread-aaa-rated-bonds-g-sec
[32] BondScanner – Corporate bond rates 2026: https://bondscanner.com/blog/corporate-bond-interest-rates-india-2026
[33] OroPocket – Gold 10-yr CAGR: https://blog.oropocket.com/return-on-gold-in-last-10-years-cagr-year-by-year-table-what-it-means-for-2026/
[34] ClearTax – Gold price history India: https://cleartax.in/s/gold-history-in-india
[35] Business Standard – Silver volatility (Motilal Oswal study): https://www.business-standard.com/finance/personal-finance/silver-shows-similar-volatility-to-indian-stocks-says-motilal-oswal-report-124112501341_1.html
[36] Aditya Birla Capital – Silver returns history: https://www.adityabirlacapital.com/abc-of-money/silver-returns-over-years-historical-data
[37] IndexScreener – Nifty REITs & InvITs: https://indexscreener.in/indices/reits-and-invits
[38] Univest – REITs in India 2026: https://univest.in/blogs/best-reit-stocks-in-india-2026
[39] ChartRow – S&P 500 trailing returns: https://chartrow.com/sp500/trailing-returns
[40] MSCI – World 100 Index factsheet: https://www.msci.com/documents/10199/255599/msci-world-100-index-usd-net.pdf
[41] Tickertape – Motilal Oswal S&P 500 Index Fund: https://www.tickertape.in/mutualfunds/motilal-oswal-sp-500-index-fund-M_MOTA
[42] Federal Reserve H.10 – INR: https://www.federalreserve.gov/releases/h10/hist/dat00_in.htm
[43] Nippon India – Nifty BeES product note: https://mf.nipponindiaim.com/FundsAndPerformance/ProductNotes/NipponIndia-ETF-Nifty-BeES.pdf
[44] Tickertape – NIFTYBEES: https://www.tickertape.in/etfs/nippon-india-nifty-50-bees-etf-NBES
[45] Sahi – ETF investing guide 2026: https://www.sahi.com/blogs/etf-investing-guide-india
[46] BusinessToday – Gold ETF AUM FY26: https://www.businesstoday.in/personal-finance/investment/story/can-gold-etfs-sustain-record-inflows-after-aum-surged-191-in-fy26-528200-2026-04-30
[47] EquityResearchIndia – Gold ETF AUM Jul 2026: https://www.equityresearchindia.com/post/gold-fund-and-gold-etf-aum-trends-amid-recent-gold-price-volatility-july-2026
[48] Kotak MF – Kotak Arbitrage Fund: https://www.kotakmf.com/mutual-funds/hybrid-funds/kotak-arbitrage-fund/dir-g
[49] Paytm Money – Kotak Equity Arbitrage: https://www.paytmmoney.com/mutual-funds/scheme/kotak-equity-arbitrage-fund-direct-growth/inf174k01lc6
[50] Fincash – Kotak Liquid Fund: https://www.fincash.com/l/mutual-funds/kotak-liquid-fund
[51] Groww – UTI Nifty200 Momentum 30: https://groww.in/mutual-funds/uti-nifty200-momentum-30-index-fund-direct-growth
[52] Value Research – SBI Nifty 200 Quality 30 ETF: https://www.valueresearchonline.com/funds/38348/sbi-nifty-200-quality-30-etf/
[53] Wikipedia – NIFTY 500: https://en.wikipedia.org/wiki/NIFTY_500
[54] Value Research – SBI Nifty 10 yr G-Sec ETF: https://www.valueresearchonline.com/funds/32486/sbi-nifty-10-yr-benchmark-g-sec-etf/
[55] Anand Rathi – Nifty 10 Yr Benchmark G-Sec: https://anandrathi.com/indices/nifty-10-yr-benchmark-g-sec
[56] Value Research – Bharat Bond ETF Apr 2030: https://www.valueresearchonline.com/funds/40483/bharat-bond-etf-april-2030/
[57] ElementOne – Private credit vs high yield 2026: https://elementone.fund/private-credit-vs-high-yield-bonds-india-2026/
[58] Altport – Private credit India 2026: https://www.altportfunds.com/what-is-private-credit-india-2026/
[59] Rurash – India private credit H1 2026: https://rurashfin.com/india-private-credit-market-2026-investor-risks/
[60] Treelife – AIF framework: https://treelife.in/finance/alternative-investment-funds-in-india/
[61] Steptrade – AIF lock-in periods: https://steptrade.capital/aif-lock-in-period/
[62] Chhota CFO – LVF reforms 2025: https://www.chhotacfo.com/blog/large-value-funds-sebi-reforms-2025/
[63] Nifty 50 Arbitrage Index factsheet (mirror): https://www.scribd.com/document/848529111/Factsheet-Nifty-50-Arbitrage-Index
[64] Ionic – AIF categories & tax guide: https://ionic.in/blogs/aif-categories-india-tax-guide-hni
