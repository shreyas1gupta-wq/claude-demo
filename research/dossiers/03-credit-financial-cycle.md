# Workstream 03 — Credit Cycle and Medium-Term Financial Cycle

Status: RESEARCH ONLY, per `CONTRACT.md` and `OPEN_QUESTIONS.md` (defaults assumed throughout).
Scope: evidence base for the 7–11y credit cycle and 15–20y medium-term financial cycle; predictive
content of credit growth / credit-to-GDP gap for equity returns and crash risk; India credit-cycle
chronology; constructible free-data state variables; Hamilton-filter settings; `tau_half` estimation;
influence caps; the credit-cycle block of the ladder.

---

## 1. Findings and literature

**F1. Borio/Drehmann/Tsatsaronis, "Characterising the Financial Cycle: Don't Lose Sight of the
Medium Term!"** (BIS Working Paper 380, 2012; Drehmann, Borio & Tsatsaronis; SSRN 2084835).
Using turning-point analysis and frequency-based (band-pass) filters on quarterly credit, credit/GDP,
house-price and equity-price series for seven advanced economies since 1960 (equity/house-price data
often starting later), they identify the "financial cycle" with the **medium-term co-movement of
credit and property prices** — equity prices "do not fit this picture well" internationally. Average
duration **16 years** across the full sample, but **~11 years pre-1998** and **~20 years post-1998**
(the cycle has lengthened and grown in amplitude since the mid-1980s liberalisation wave). Financial-
cycle peaks coincide closely with financial crises; recessions that overlap a financial-cycle
contraction are markedly deeper. **Verified** (BIS WP 380; SSRN 2084835).

**F2. Schularick & Taylor, "Credit Booms Gone Bust: Monetary Policy, Leverage Cycles, and Financial
Crises, 1870–2008"** (*American Economic Review* 102(2), 2012, pp. 1029–61; NBER WP 15512). Panel of
14 advanced economies, annual, 1870–2008 (the seed of the Jordà-Schularick-Taylor, "JST", database).
Central result: **a one-standard-deviation rise in real credit growth over the prior year raises the
predicted probability of a financial crisis over the subsequent five years by ~2.8 percentage points**
(logit/panel-probit). Credit growth dominates money-growth and current-account measures as a crisis
predictor. Summers (2017, *J. Applied Econometrics*, replication) confirms the qualitative result but
shows the marginal effect is heterogeneous across countries — a caution against a single pooled
coefficient. **Verified** (AEA 10.1257/aer.102.2.1029; Summers replication, Wiley 10.1002/jae.2554).

**F3. Jordà, Schularick & Taylor, "When Credit Bites Back: Leverage, Business Cycles, and Crises"**
(*J. Money, Credit and Banking* 45(s2), 2013; NBER WP 17621). Over **200 recession episodes**, 14
countries, 1870–2008: the credit-intensity of the preceding expansion (change in private-credit/GDP)
predicts the **depth and slowness of the following recession**, in both crisis and "normal" recessions,
using local projections with macro controls. **Verified** (Wiley 10.1111/jmcb.12069; NBER WP 17621).

**F4. Jordà, Schularick & Taylor, "Leveraged Bubbles"** (*J. Monetary Economics* 76(S), 2015, pp.
S1–S20; NBER WP 21486). 17 countries, house-price and equity-price bubbles since 1870: **credit-
financed** asset bubbles — especially real estate — are far more dangerous than equity bubbles or
unleveraged bubbles of either kind; their collapse is followed by deeper recessions and slower
recoveries. **Verified** (ScienceDirect 10.1016/j.jmoneco.2015.07.001).

**F5. Baron & Xiong, "Credit Expansion and Neglected Crash Risk"** (*Quarterly Journal of Economics*
132(2), 2017, pp. 713–64; NBER WP 22695). **20 developed countries, 1920–2012.** Bank credit
expansion predicts (i) elevated **crash risk** in bank-equity and broad-equity indices — crash defined
as quarterly log excess return < −30% within the following 1–3 years — and, despite that elevated
risk, (ii) **lower mean forward returns**: conditional on bank-credit expansion exceeding its **95th
percentile**, the predicted **3-year excess return on the bank-equity index is −37.3%**. The authors
argue bank-equity investors systematically **neglect** the crash risk building up during the boom
(overoptimism/extrapolation), rather than being compensated for bearing it. A separate specification
in the paper (credit expansion >1.5σ → −19.3% over the next 8 quarters) is reported in secondary
summaries but I could not independently confirm its exact wording against primary text; **tag
[VERIFY: Baron & Xiong 1.5σ / 8-quarter / −19.3% figure vs. the confirmed 95th-percentile / 3-year /
−37.3% headline]**. Country count itself (20) is verified against the NBER abstract. **Mechanism =
behavioural (neglected risk) + limits to arbitrage**, not a compensated risk premium. **Verified**
(Oxford 10.1093/qje/qjx011; NBER WP 22695).

**F6. Greenwood & Hanson, "Issuer Quality and Corporate Bond Returns"** (*Review of Financial
Studies* 26(6), 2013, pp. 1483–1525; orig. NBER WP 17197, "Issuer Quality and the Credit Cycle").
Credit quality of corporate debt **issuers** deteriorates during credit booms; the **share of high-
yield issuance in total issuance** is a more reliable, more timely signal of "credit-market
overheating" than aggregate credit growth, and forecasts **low, often negative, excess corporate-bond
returns** in the following 1–2 years, because credit-risk repricing hits low-quality issuers hardest.
**Verified** (Oxford RFS 10.1093/rfs/hht012; Harvard DASH copy).

**F7. Greenwood, Hanson, Shleifer & Sørensen, "Predictable Financial Crises"** (*Journal of Finance*
77(2), 2022, pp. 863–921; orig. HBS/NBER WP 27396, 2020). **42 countries, 1950–2016.** Construct an
"R-zone" indicator: a country enters the business R-zone when trailing-3-year non-financial-business
credit growth is in the **top quintile** of the full sample and trailing-3-year equity returns are in
the **top tercile**, simultaneously. Conditional on R-zone entry, the probability of a systemic
financial crisis within 3 years is **~40%**, versus **~7% unconditionally**. The combination of rapid
credit growth *and* asset-price growth is what does the work — either alone is much weaker. Explicitly
frames crises as **Kindleberger-Minsky predictable boom-busts**, not "bolts from the sky." **Verified**
(Wiley 10.1111/jofi.13105; NBER WP 27396).

**F8. Mian, Sufi & Verner, "Household Debt and Business Cycles Worldwide"** (*Quarterly Journal of
Economics* 132(4), 2017, pp. 1755–1817; NBER WP 21581). **30 (mostly advanced) countries, 1960–2012.**
A rise in the household-debt-to-GDP ratio over a 3-year window predicts **lower GDP growth 3–4 years
later**, higher unemployment, and systematically **negative growth-forecast errors** by professional
forecasters at the end of household-debt booms (flawed expectations, not just a mechanical debt-
overhang accounting identity). Effect is stronger under tighter monetary-policy constraints (fixed
exchange rate, ZLB proximity, external funding dependence) — all *more* relevant to India's exchange-
rate-managed regime than to the median advanced economy in the sample. **Verified** (Oxford
10.1093/qje/qjx017; NBER WP 21581).

**F9. Drehmann & Juselius, "Evaluating Early Warning Indicators of Banking Crises: Satisfying Policy
Requirements"** (*International Journal of Forecasting* 30(3), 2014; BIS WP 421). **26 economies,
quarterly since 1980.** The **credit-to-GDP gap** is the best-performing single early-warning
indicator at 3–5-year horizons (**AUROC 0.83–0.85**, only degrading toward 0.80 in the final year
before a crisis); a **debt-service ratio (DSR)** dominates it at <2-year horizons. Basel III's
countercyclical-capital-buffer framework is built on this result. **Verified** (BIS WP 421;
ScienceDirect 10.1016/j.ijforecast.2013.10.001).

**F10. Hamilton, "Why You Should Never Use the Hodrick-Prescott Filter"** (*Review of Economics and
Statistics* 100(5), 2018, pp. 831–43; NBER WP 23429). The HP filter introduces spurious dynamics with
no basis in the data-generating process, mishandles trend/cycle at the endpoint (exactly the "endpoint
revision" problem the CONTRACT bans it for), and its conventional smoothing parameter has no principled
statistical justification. Proposed alternative: regress y at date *t* on the **four most recent
values as of date *t − h*** (i.e., an *h*-step-ahead local-projection residual serves as the "cycle").
For **quarterly U.S. GDP**, Hamilton recommends **p = 4 lags, h = 8 quarters** — a choice tied
explicitly to the ~2-year modal length of a U.S. business-cycle contraction, i.e., *h* is chosen to be
about as long as the phenomenon you want to treat as transitory, not a universal constant. **Verified**
(MIT Press 10.1162/rest_a_00706; econweb.ucsd.edu/~jhamilton/hp.pdf).

**F11. Quast & Wolters, "Reliable Real-Time Output Gap Estimates Based on a Modified Hamilton
Filter"** (*J. Business & Economic Statistics* 40(1), 2022; Kiel WP 2158). Shows the vanilla Hamilton
filter is itself sensitive to *h* and to large shocks in real time; proposes a rolling-window
modification (best performance found with a **~15-year rolling window**) for reliability. Confirms
the general point from F10: *h* and the estimation window are design choices that must be tuned to
the horizon of interest, and naive defaults transfer poorly across different cyclical objects (output
gap vs. credit gap vs. financial cycle). **Verified** (Taylor & Francis 10.1080/07350015.2020.1795099).

---

## 2. India-specific evidence

**I1. Behera & Sharma, "Does Financial Cycle Exist in India?"** (RBI Working Paper Series, WPS
(DEPR) 03/2019, July 2019) and its peer-reviewed version **"Characterizing India's Financial Cycle"**
(*Journal of Emerging Market Finance*, Sage, 2022; DOI 10.1177/09726527221077727). Quarterly data on
bank credit, equity prices, house prices and the real effective exchange rate; individual series from
**1960Q1** (credit) where available, PCA-aggregated financial-cycle index constructed over
**1996Q2–2018Q4** (constrained by equity/house-price data start dates); turning-point analysis,
spectral analysis and band-pass filters. Findings: strong co-movement across credit, equity and (since
the mid-2000s) house prices supports a well-defined aggregate financial cycle in India; **the overall
financial cycle is driven mainly by credit and equity, not house prices** — a genuine departure from
the international (BIS) finding that equity "does not fit" the cycle, plausibly reflecting India's
bank-dominated but retail/FII-active equity market. **Average business-cycle duration ≈ 5 years vs.
average credit-cycle duration ≈ 15 years** in the post-reform sample. Critically for the CONTRACT's
clock test: **the aggregate PCA financial-cycle series shows only one clear peak and one clear trough
over 1996–2018** — i.e., **fewer than one complete domestic cycle observed**. **Verified** (RBI WPS
03/2019; Sage 10.1177/09726527221077727).

**I2. A second RBI-linked study** (reached only via secondary summaries; **[VERIFY: exact title/
author — could not fetch rbidocs.rbi.org.in directly, network egress to rbidocs.rbi.org.in is blocked
in this environment per CONTRACT §7 Known Prior #11]**) uses an NBER-style turning-point dating
procedure on **1950-51 to 2020-21** annual data and reports: average business/investment-cycle
duration **≈ 8 years**; average **"short" credit cycle ≈ 7 years**; average **"medium" credit cycle
≈ 17 years**, with **contraction phases of the credit cycle more prolonged than expansions**, and
cycle length **lengthening since the early-1990s reforms**. This is directionally consistent with I1
(credit cycle ~3× business-cycle length) and with the international 16–20y estimate (F1), and is the
likely source of the "7–11y credit / ~16y financial cycle" framing in the workstream brief. Given the
inability to verify the primary document, treat the specific "7y / 17y" point estimates as **Tier-C-
confidence numbers pending primary-source confirmation**, while the *qualitative* pattern (credit
cycle ≈ 2–3× business cycle; medium financial cycle in the mid-teens to ~20 years) is well corroborated
by I1 and F1 independently.

**I3. Garg & Sah, "Cyclical Dynamics and Co-Movement of Business, Credit, and Investment Cycles:
Empirical Evidence from India"** (*Humanities and Social Sciences Communications* 11, 2024, art.
612; Palgrave/Springer Nature). **Annual data, 1980–2021**, cycles extracted with the **Hodrick-
Prescott filter** (a methodology the CONTRACT bans for our own construction — cited here only as a
literature data point, never as a design input), SVAR + Granger causality. Reports **business cycle
≈ 4 years, credit cycle ≈ 3 years** — three to five times *shorter* than I1/I2. **Verified** as a
publication (Nature 10.1057/s41599-024-03021-5), but the magnitude gap versus I1/I2 is itself the
finding for our purposes: **reported "cycle length" for India varies by a factor of ~3–5× depending
on filter choice, data frequency (annual vs. quarterly) and sample window** (1980–2021 annual HP vs.
1960/1996–2018 quarterly band-pass/turning-point). This is direct empirical support for the CONTRACT's
insistence on the clock test and `tau_half` ordering rather than any single "the credit cycle is N
years" point estimate — the number is not robust to method, only the *ordering* (business < credit <
financial-cycle) is.

**I4. Saini, Ahmad & Bekiros, "Understanding the Credit Cycle and Business Cycle Dynamics in
India"** (*International Review of Economics & Finance* 76, 2021, pp. 988–1006). Firm-level data over
30+ years: finds the **business cycle leads the credit cycle** in India (repo rate, broad money, real
exchange rate and industrial output explain business-credit dynamics), the reverse of the
textbook Minsky/Kindleberger causal direction assumed in most of the international literature above.
Credit destruction is more volatile than credit creation; excess reallocation is countercyclical.
**Verified** (ScienceDirect 10.1016/j.iref.2021.08.010). *Design implication*: do not import the
international "credit leads, equities/output follow" causal ordering uncritically into the Indian
model without allowing for the reverse or bidirectional linkage found domestically.

**I5. India credit-cycle chronology (compiled from RBI Financial Stability Reports, RBI DBIE, the
Economic Survey 2016-17, and contemporaneous financial press; observation count discussed below).**

| Phase | Approx. dates | Character | Key free-data marker |
|---|---|---|---|
| Post-liberalisation NPA cleanup (tail of a pre-1997 build-up, not a fresh crisis) | 1992–2002 | New (1992-committee-recommended) NPA recognition norms bite; nationalised-bank GNPA falls from **19.05% (1997) to 12.16% (2001)**; India largely insulated from the 1997–99 Asian financial crisis (few of the external/BOP vulnerabilities other Asian economies had) | RBI FSR / annual report GNPA series |
| Credit boom | 2003–08 | Bank credit compounds at >25–30%/yr in the peak years; infra & real-estate lending surge; GNPA falls to a multi-decade low (~2% by FY08-09) as the boom masks quality | RBI DBIE non-food credit growth |
| GFC pass-through + reacceleration | 2008–11 | Brief slowdown, fiscal/monetary stimulus, credit growth re-accelerates; many infra projects sanctioned on optimistic assumptions that seed the next downturn | RBI DBIE, sectoral deployment |
| Twin Balance Sheet (TBS) problem | 2011–15 | Corporate over-leverage (stalled projects, land/environmental delays, cost overruns, rupee depreciation) plus rising restructured/stressed bank assets; Economic Survey 2016-17 estimates stressed assets (NPA + restructured) near **12% of loans** | Economic Survey ch.4 (2016-17); RBI FSR |
| Asset Quality Review (AQR) — recognition shock | 2015–18 | RBI (Governor Rajan) forces reclassification of restructured/disguised-standard assets; GNPA jumps **5.1% (Sep-15) → 7.6% (Mar-16) → 9.3% (FY17) → 11.2% (FY18)** | RBI FSR biannual GNPA series |
| IL&FS default / NBFC-shadow-banking crisis | Jun–Sep 2018 | IL&FS defaults on commercial paper (Jun 2018), rating cut AAA→junk overnight (Sep 2018), NCLT supersedes board (Oct 2018); **~$34bn of NBFC/HFC debt** maturing Oct-18–Mar-19 triggers a system-wide funding freeze for shadow banks, transmitting to real estate and MSME credit even though **bank** non-food credit growth barely wobbled — the shock originated **outside** the RBI's headline bank-credit series | Contemporaneous press (Business Standard, Quartz); RBI FSR NBFC chapter |
| COVID shock | 2020 | Non-food credit growth collapses to the **~6% range**; RBI moratorium/restructuring forbearance temporarily masks recognition | RBI DBIE, RBI FSR |
| Post-COVID unsecured-retail credit upswing | 2021–24 | Non-food credit growth **16.0% (Aug-22) → 20.2% (Mar-24)**, disproportionately unsecured personal loans/NBFC exposure; credit-deposit ratio hits an **all-time high ~80% (Mar-24, highest since 2005)** | RBI DBIE credit growth; RBI DBIE credit-deposit ratio |
| Macroprudential tightening | Nov 2023 | RBI raises risk weights on unsecured consumer credit and bank-to-NBFC exposure by **25 percentage points** (100%→125%), explicitly to slow retail/NBFC credit growth it judged to be overheating | RBI press release, 16-Nov-2023 |
| Current state (as of this writing) | 2024–25 | GNPA at a **decadal-best 2.15% (Sep-25)**; credit-deposit ratio still elevated (~78–80%); household debt/GDP risen to **~42% (end-2024) from 26% (2015)** per RBI FSR — still below the emerging-market average of ~46.6% but the fastest-rising component of the credit stack | RBI FSR; PIB press release |

**Observation count for the clock test.** Counting genuine domestic **down-legs** since the 1991
reforms (the only period with a reasonably consistent statistical/regulatory regime): (i) the tail of
the pre-1997 NPA cleanup (arguably pre-dates the "post-reform" regime and is a resolution, not a fresh
bust), (ii) the 2011–18 TBS/AQR/IL&FS episode (best read as **one** prolonged downturn with two
compounding shocks — corporate distress, then a banking recognition shock, then a shadow-banking
funding shock — rather than three independent cycles), and (iii) the COVID shock (very short,
policy/forbearance-driven, arguably not a "credit cycle" trough at all in the Minsky sense). **That is
at most 1–2 completed, unambiguous domestic credit-cycle down-legs since 1991** — a hard fail of the
CONTRACT's "≥4 observed complete periods" clock test. **This settles the classification question:
India's credit/financial cycle is a STATE VARIABLE for allocation purposes, not a periodic cycle to be
timed by calendar** — exactly the CONTRACT's own framework (§4), and it must be **pooled onto the
JST/BIS cross-country panel** (§9) for any parameter that needs more than a handful of India
observations to estimate.

**I6. BIS credit-to-GDP gap, India series** (BIS Data Portal, `data.bis.org`, topic `CREDIT_GAPS`,
series `Q.IN.P.A.A`; free). Methodology note (important tension with our mandate): the **official BIS
gap is computed with a one-sided HP filter, λ = 400,000** — precisely the filter the CONTRACT bans for
our own signal construction (BCBS 2010 guidance; BIS WP; ESRB WP). **Recommendation:** use the BIS
series only as a free **external cross-check / sanity benchmark**, never as the model's internal
credit-cycle signal; reconstruct the equivalent quantity for India from RBI DBIE credit and MOSPI GDP
using the **Hamilton (2018) regression filter** instead (see §4/§6). Historically, India's BIS gap
**turned negative from 2012** (post-2003-08-boom corporate deleveraging) and reached **≈ −2.9 in
Q1 2016** — the lowest among the BRIC group at that date — which lines up with the AQR-era GNPA
trough-into-recognition-shock chronology in I5. **Verified** (BIS statistics; contemporaneous press
citing BIS comparative data), though the exact −2.9 figure is via secondary press citation, not a
direct pull of the BIS series (blocked in this environment) — **tag [VERIFY: −2.9 Q1-2016 BIS
credit-to-GDP gap figure against the primary BIS data-portal series once network access allows]**.

**I7. Credit-deposit (CD) ratio** (RBI DBIE / Handbook of Statistics on the Indian Economy, monthly,
free, back to 1969). Long-run average **≈ 67.4%** (Mar-1969–2024), range **51.6% (1994 low) to ≈ 80%
(2024 high)**. A simple, free, monthly, GDP-vintage-independent alternative/complement to the credit-
to-GDP gap — attractive because it sidesteps India's GDP-data lag/revision problems (a real
constructability advantage the international literature's GDP-denominator gap does not have to deal
with). **Verified** (RBI DBIE description via CEIC/press aggregation).

**I8. RBI Financial Stability Report (FSR) series** (biannual since 2010, free PDF). Publishes the
GNPA/NNPA time series, CRAR, and two composite indices: the **Banking Stability Indicator (BSI)** (a
distress-dependency measure across soundness/asset-quality/liquidity/profitability) and the
**Systemic Risk Survey (SRS)** (a qualitative 5-point survey of market participants across
global/financial/macroeconomic/institutional/general risk categories). Both are **free** but have a
**short history (since ~2010–12)** and are **index-level composites**, not raw series with an
estimable long-run distribution — appropriate only as a **Tier-C, reduce-only overlay** per CONTRACT
§4, never a primary driver.

**I9. Sectoral deployment of gross bank credit** (RBI, monthly, free — `rbi.org.in/Scripts/
Data_Sectoral_Deployment.aspx`; covers ~93% of non-food credit via a select-bank sample). Enables an
India-specific **borrower/issuer-quality composition analogue** to Greenwood-Hanson (F6) — e.g., the
share of incremental credit growth flowing to unsecured personal loans vs. productive/secured sectors.
Notably, **RBI's own November-2023 macroprudential action (I5) is direct institutional evidence that
the regulator treats this composition signal as material**, even though no published India-specific
academic study quantifies its forward-return predictive power (Tier C — see §3).

**I10. CCIL / FIMMDA corporate-bond spread data** (CCIL market-update and quarterly Debt Market
Report, free to view on ccilindia.com; FIMMDA daily valuation matrix requires member login, so **not
fully free at the finest granularity**; aggregator sites such as indiamacroindicators.co.in republish
tenor-wise AAA-vs-G-Sec spreads). This is the closest India analogue to Greenwood-Hanson's (F6)
credit-spread/issuance-quality mechanism, but India's **corporate bond market is bank-dominated and
shallow** relative to the U.S. high-yield market the original study uses — a structural reason to
expect a **muted** signal until the market deepens. One aggregator-reported figure ("10-year AAA vs.
G-Sec spread = 2.21" as of 15-Aug-2026) is almost certainly a **units/formatting error** in the
secondary source (percentage points vs. basis points) — **tag [VERIFY: exact CCIL/FIMMDA AAA-G-Sec
spread figures against a primary CCIL PDF, not an aggregator page]** — use this channel qualitatively
(direction/level relative to own history) rather than for a specific bps threshold, consistent with
the CONTRACT's no-magic-numbers rule regardless.

**I11. NBFC-specific data** (RBI FSR NBFC chapter, RBI "Basic Statistical Returns", free). The 2018
IL&FS episode (I5) demonstrates that **bank non-food credit alone would have missed the shock's
origin** — it began and transmitted through the commercial-paper/shadow-banking channel. **Design
implication: the India credit-cycle state variable must be a bank + NBFC combined credit aggregate**,
not RBI's headline "non-food bank credit" series alone, or the next NBFC-centred stress episode
(plausibly seeded by the 2021-24 unsecured-retail/NBFC boom in I5) will again be invisible to a
bank-only signal until it is systemic.

---

## 3. Decay and crowding assessment

**Edge A — Aggregate credit growth / credit-to-GDP gap predicts elevated crash risk and depressed
forward equity returns** (F2, F5, F9; I5, I6). *Survival argument*: **(i) behavioural mechanism under
crowding** — Baron-Xiong's own contribution is precisely that this signal has been visible and
published for decades (their sample runs to 1920) and **still shows up out-of-sample through 2012**,
because the agents who would need to trade against it (bank-equity holders, universal-owner index
funds) are structurally extrapolative during the boom and the "short the banking system" trade is a
multi-year, negative-carry, career-risk position that few institutions can hold to completion — this
is also **(ii) a capacity/limits-to-arbitrage argument**: shorting an entire banking sector or de-
grossing a whole equity book ahead of a systemic bust is expensive and slow to implement at any real
size, doubly so under our mandate's hedge-only constraint (index derivatives only, no unlimited single-
name shorting) and India's circuit-limit/ASM-GSM surveillance regime, which explicitly caps how fast
large directional bets can be built or unwound in stressed names. *Decay treatment*: this is a **macro/
tail-timing signal, not a cross-sectional stock anomaly**, so the McLean-Pontiff 26%/58% decay
figures (which describe published cross-sectional anomalies) do not mechanically apply. Nonetheless,
in the absence of an India-specific decay estimate, I apply a **conservative judgment haircut**: treat
the international AUROC 0.83–0.85 (F9) as an **upper bound**, and expect a **live India AUROC materially
lower (order 0.65–0.75)** once implemented, given (a) pooling dilution from cross-country transfer, (b)
a shorter, thinner domestic sample, and (c) regime differences (capital controls, administered rates
pre-1991, bank-dominated system). This is a **stated assumption pending data-phase validation**, not a
literature-derived number — flagged explicitly as such in §4.

**Edge B — Issuer/borrower-quality deterioration during a credit boom predicts poor forward risk-
asset returns** (F6; I9, I10). *Survival argument*: **(i) structural/behavioural** — composition-of-
credit signals require flow-level data that most market participants do not process in real time
(unlike a price signal, which is immediately visible), so the correction is necessarily lagged and
systemic rather than instantly arbitraged away; **(iv) institutional constraint** — in India this
mechanism is *literally enforced* by the regulator (RBI's Nov-2023 risk-weight action, I5), meaning the
"correction" is a regulatory/credit-repricing event with a long fuse, not a market-clearing trade that
crowds quickly. *Decay treatment*: Greenwood-Hanson is a genuine capital-markets finding with **no
India replication**. Because it is fundamentally a spread/quality-based signal in the same family as
studied cross-sectional anomalies, I apply the **generic McLean-Pontiff 26% (out-of-sample) / 58%
(post-publication) haircut band** as the default conservative prior on its effect size, pending an
India-specific estimate — this is an explicit, stated haircut, not "it backtests well."

**Edge C — Household-debt-cycle expansion predicts a subsequent growth/consumption slowdown**
(F8; I5 household-debt figures). *Survival argument*: **(iii) genuine risk premium / behavioural
combination** — credit-supply-driven debt booms plus systematically biased professional forecasts
(Mian-Sufi-Verner's own contribution) is a structural, not merely statistical, finding. *For India
specifically*: household debt/GDP has risen from 26% (2015) to 42% (end-2024) — the country's **newest
and least-tested** credit-cycle limb, with **zero completed India down-legs** observed (the 2021-24
upswing has only just met a policy response, not a bust). **Tier C, reduce-risk-only** per CONTRACT §4:
this signal may tighten our risk posture as household leverage rises, but must **never be used to add
directional exposure**, since we have no domestic evidence it resolves the way the 30-country panel
says it should, and India's household debt/GDP (42%) still sits **below** the emerging-market average
(~46.6%) — the level itself is not yet extreme by cross-country standards, only the **rate of change**
(the actual Mian-Sufi-Verner variable) is.

**Edge D — The 16–20y medium-term financial cycle as a periodic, timeable object.** *This edge does
not survive as a cycle at all, by design of the CONTRACT's own clock test.* At the **India-only**
level: 1–2 observed down-legs since 1991 (I5), a single peak/trough pair in the PCA-aggregate series
(I1) — an unambiguous clock-test failure. At the **pooled international** level (F1: 7 advanced
economies since 1960; broader JST/BIS panels): each economy contributes at most 3–4 complete medium-
term cycles over ~60 years, aggregating to on the order of 20–30 country-cycle observations across the
BIS sample — this clears the **Tier-B threshold (4–30)** but **not** Tier A (≥30 independent
observations). **Recommendation: treat the medium-term financial cycle as a Tier-B, cross-country-
pooled *prior on phase length and amplitude* that informs the uncertainty band around India's presumed
current phase — never as a specific "next peak/trough in year X" forecast.** This is consistent with
the CONTRACT's stated consequence for the (much longer, much thinner) 200-year debt cycle: long,
low-observation-count cycles buy a **structural floor/tail-hedge posture**, not a timed allocation
call.

**Edge E — The Basel "2 percentage point" credit-to-GDP-gap trigger for countercyclical capital
buffers.** This is an **institutional/regulatory convention** (BCBS 2010), not a discovered empirical
optimum — its survival is guaranteed by regulatory mandate (Tier of "institutional constraint"), but
that is a reason it persists as a *bank-capital* rule, **not** a reason to adopt "2pp" as an alpha-
generating threshold in our own model. Per CONTRACT §6 (no magic numbers), we use the **continuous
gap value or its percentile rank**, never a fixed 2pp cutoff, in any of our own signal constructions.

---

## 4. Proposed parameters

| Name | Value / range | Source | Tier | Confidence | Decay assumption | What would change it |
|---|---|---|---|---|---|---|
| Medium-term financial-cycle typical duration (prior, pooled) | 16–20y (11y pre-1998 / 20y post-1998 split) | F1 (BIS WP 380) | B | Medium | None assumed — used only as a phase-uncertainty prior, never a timing forecast | A longer post-1998 BIS/JST update sample, or an India-specific 2nd/3rd completed cycle once observed |
| India credit-cycle length (post-reform) | ≈ 15y (I1) vs. "7y short / 17y medium" (I2, [VERIFY]) vs. ≈ 3y (I3, HP-filter, excluded methodology) | I1/I2/I3 | B (I1), C (I2 pending primary verification), excluded (I3) | Low-Medium | Treat only the **ordering** (business < credit < financial cycle) as reliable; do not trust the point estimate | Primary-source confirmation of I2; a 2nd domestic completed cycle |
| India credit/GDP-gap crisis-prediction AUROC (assumed, pre-validation) | 0.65–0.75 (haircut from international 0.83–0.85) | Judgment haircut on F9, per §3 Edge A | B (methodology) / C (numeric haircut, judgment not literature) | Low | Explicit, stated haircut — not literature-derived; supersede with actual India backtest once data phase runs | First purged/embargoed India-conditioned AUROC estimate |
| Credit-growth 1σ → 5y crisis-probability sensitivity (pooled prior) | +2.8pp per 1σ rise in real credit growth (F2), heterogeneous across countries per Summers replication | F2 | A (pooled, ≥30 country-year obs) / B for India-specific transfer | Medium | Country heterogeneity noted in replication — shrink toward panel mean, do not apply India-raw | India-specific re-estimate via pooled/partial-pooling regression once data phase runs |
| R-zone-style joint credit+asset-price overheating indicator | Credit growth in top quintile AND equity return in top tercile (trailing 3y), by full-sample rank, not fixed % | F7 | B (pooled, 42-country panel; India-only n<4) | Medium | Percentile/rank form avoids a magic-number threshold per CONTRACT §6 | India-specific joint distribution once ≥1 more completed episode observed |
| Issuer/borrower-quality composition signal (share of incremental credit to unsecured retail/NBFC) | Percentile rank of trailing 12m share, not a fixed % | F6 (mechanism) + I9 (India construction) + I5 (RBI's own Nov-2023 action as institutional confirmation) | C (no India-specific quantified study) | Low | McLean-Pontiff 26%/58% generic haircut band applied as placeholder (§3 Edge B) | First India-specific pre-registered backtest against the 2018 IL&FS and 2023-24 tightening episodes |
| Household debt/GDP change (3y) | Reduce-risk trigger only, rank-based, not sized for upside | F8; I5 (26%→42%, 2015→2024) | C | Low | Tier-C reduce-only per CONTRACT §4 — cannot add positive tilt | First completed India household-debt down-leg |
| Credit-deposit ratio percentile rank | Long-run range 51.6%–~80% (1969–2024); use percentile rank of trailing series, not fixed % | I7 | B | Medium | Faster-updating, GDP-vintage-independent complement to the credit/GDP gap; likely correlated, not independent — do not double-count in the composite | A structural break in deposit-mobilisation patterns (e.g., large-scale disintermediation to capital markets) |
| GNPA ratio (level + trend) | RBI FSR biannual series, 1997–present | I5/I8 | B | Medium-High (well-measured, but *lagging* by construction — AQR shows recognition itself can be a multi-year-delayed regime shift) | Confirmatory/lagging use only — never a leading timing signal; treat as a de-risking confirmation, not an entry trigger | A future recognition-norm change (as AQR was) would break series comparability again |
| Bank + NBFC combined credit aggregate | Construct from RBI DBIE bank non-food credit + RBI FSR/BSR NBFC credit; India lacks a single free consolidated series today | I11 | Construction task (no tier yet — a data-engineering deliverable, not an estimated parameter) | — | N/A | Availability of a consolidated free series in the data phase |
| CCIL/FIMMDA AAA–G-Sec spread (issuer-quality analogue) | Directional/percentile use only, exact bps figures [VERIFY] | I10 | C | Low | Muted signal expected given shallow/bank-dominated Indian corporate-bond market; McLean-Pontiff band as placeholder | Market depth increase; an India-specific event study |
| BIS-style credit-to-GDP gap for India, **our own construction** | Hamilton-filtered (never HP), percentile-ranked, not a fixed pp threshold | I6 (benchmark only) + F10 (method) | B (methodology inherited from Tier-A international literature; India-specific numeric output starts at B pending validation) | Medium | Reconstruct, do not adopt BIS's HP-filtered series as the live signal (CONTRACT §8 bans HP filter) | Any structural break in RBI credit-series definitions (has happened historically, e.g., NBFC reclassifications) |
| Hamilton filter, short credit-cycle band | p = 4 lags; h ≈ 16–24 quarters (4–6y) | Reasoned extension of F10's own guidance ("*h* as long as the phenomenon you want treated as transitory") applied to a 7–11y target cycle | B (methodological choice) | Medium | Re-tune *h* via purged/embargoed out-of-sample AUROC grid search once data loaded, not by in-sample fit (CONTRACT §9) | Actual India credit-series length and noise properties once ingested |
| Hamilton filter, medium financial-cycle band | p = 4 lags; h ≈ 32–40 quarters (8–10y) | Same reasoning, applied to a 15–20y target cycle (F1) | B (methodological choice) | Medium | Same as above | Same as above |
| `tau_half` estimation approach | Fit AR(1) to the Hamilton-filtered gap over overlapping windows; `tau_half = ln(0.5)/ln(ρ)`; expect order-of-magnitude 3–6y for a 7–11y full-cycle band (half-life ≈ ¼–⅓ of full period for a quasi-cyclical AR process) | Methodological proposal, not yet estimated | C (placeholder; becomes B/A once estimated on real data with a reported confidence interval) | Low (explicitly a placeholder) | To be superseded entirely by the data-phase estimate | First real `tau_half` estimate from ingested RBI DBIE series |
| Influence cap, credit-cycle block, Tier-A-sourced-but-India-Tier-B components | ≤25% of the credit-cycle block's total regime-score weight | Reasoned analogy to CONTRACT's own stated examples (200y debt cycle ≈1.5pp of book; short lookbacks get the most authority) — credit cycle sits between these in observation count and confidence | B (design recommendation) | Medium | Revisit once the data-phase purged-CV Sharpe/AUROC is in hand | A validated India-specific AUROC materially above or below the 0.65–0.75 assumed range |
| Influence cap, Tier-C composition/household/spread satellites | Reduce-only; 0% positive-tilt budget; capped negative-tilt contribution (e.g., ≤10% of block risk-off signal) | CONTRACT §4 (Tier-C reduce-only rule), applied here | C by rule | High (this is a hard rule, not an estimate) | N/A — this is a constraint, not a decaying edge | Promotion to Tier B only after ≥4 India observations or ≥10 validated cross-country analogues with matching institutional structure |

---

## 5. Evidence-tier recommendations

- **Tier A candidates exist only on the pooled JST/BIS international panel**, not for any India-only
  estimate in this workstream. "Credit growth → crisis probability" (F2) and "credit-to-GDP gap →
  crisis AUROC" (F9) both clear ≥30 independent country-year observations internationally (14–26
  economies over decades, several dozen crisis episodes in the JST crisis chronology — **exact crisis
  count [VERIFY: precise JST/BIS systemic-crisis count for the 1870–present sample]**). **Recommendation:
  treat the *methodology* as Tier A, but the *India-actionable coefficient* as Tier B**, because
  transferring a pooled international coefficient to a structurally different economy (capital
  controls historically, bank-dominated system, promoter-concentrated equity market, administered
  rates pre-1991) is itself an assumption that needs its own (Stambaugh-corrected, shrinkage-pooled)
  estimate before it earns Tier-A confidence for sizing India risk.
- **Tier B**: India's own financial-cycle characterization (I1, n=1 domestic peak/trough, but backed
  by a ≥10-cross-country-analogue clause via F1's BIS sample); the R-zone joint credit+asset-price
  indicator (F7, pooled 42-country panel, India-only n<4 but methodology transfers cleanly); the
  credit-deposit ratio and GNPA series as **measurement**, not effect-size, Tier B (well-measured, long
  series, but GNPA is explicitly lagging); the Hamilton-filter design choices (methodological Tier B).
- **Tier C**: sectoral-composition/issuer-quality analogue for India (I9/I10, no quantified India
  study — observation count for a *quantified* domestic effect = 0); household-debt-cycle signal for
  India (I5/F8, zero completed India down-legs); corporate-bond-spread issuer-quality analogue (I10,
  shallow market, no clean long series). All three are **reduce-risk-only** per CONTRACT §4 until
  either ≥4 India observations accumulate or a ≥10-cross-country-analogue argument is made explicit
  and defended (which I have not attempted here for I9/I10 because the institutional structure — bank-
  dominated credit system, shallow corporate-bond market — differs enough from the Greenwood-Hanson
  U.S.-HY-bond setting that a clean transfer argument is not credible without further work).

---

## 6. Research method for the data phase

1. **Series construction** (on the principal's machine — this environment's egress to rbidocs.rbi.org.in,
   data.rbi.org.in/DBIE, and other RBI/FRED/Kaggle endpoints is blocked, per CONTRACT §7 Known Prior
   #11): pull RBI DBIE non-food bank credit (monthly, back to ~1970s) and NBFC credit/AUM (RBI FSR/BSR
   tables) to build the **bank+NBFC combined credit aggregate** (I11); pull MOSPI nominal GDP with
   vintage flags where available (point-in-time, not the latest-revised series, to avoid the same
   look-ahead bias the CONTRACT flags for fundamentals data — Known Prior #7 applies structurally here
   too, since GDP is also restated).
2. **Filtering**: apply the **Hamilton (2018) regression filter only** (never HP, per CONTRACT §8), at
   two horizon bands — *h* ≈ 16–24 quarters for the short (7–11y) credit cycle, *h* ≈ 32–40 quarters for
   the medium (15–20y) financial cycle (F10, F11) — with *p* = 4 lags. Select the exact *h* within each
   band via **purged and embargoed cross-validation** (embargo ≥ *h*, per CONTRACT §9) against a
   **pooled** (India + JST/BIS panel) crisis/severe-drawdown label set, not by in-sample fit to India's
   own thin sample.
3. **`tau_half` estimation**: fit AR(1) to the Hamilton-filtered gap series over overlapping windows;
   report `tau_half = ln(0.5)/ln(ρ)` with a confidence interval (not a point estimate) given the short
   sample; use it **only** to place the credit-cycle block in the CONTRACT's `tau_half`-ordered ladder,
   never to assert a specific periodicity.
4. **Stambaugh-bias correction**: the credit-to-GDP gap and CD ratio are highly persistent regressors
   in a short sample — apply a standard bias correction (e.g., Amihud-Hurvich or a block-bootstrap) to
   any in-sample predictive-regression coefficient before it is trusted, per CONTRACT §9.
5. **Pooling protocol**: for every India-specific coefficient (crisis-probability sensitivity, AUROC,
   R-zone joint-threshold percentiles), compute a **precision-weighted (inverse-variance) or empirical-
   Bayes shrinkage estimate** between (a) the India-only OLS/logit estimate and (b) the JST/BIS pooled-
   panel estimate, with the weight on (a) governed by India's own observation count (currently ≤2
   complete down-legs ⇒ heavy shrinkage toward the pooled estimate). This directly operationalises
   CONTRACT §9's "pool on the JST panel where India alone offers <2 cycles" instruction — India
   currently sits exactly at that threshold.
6. **Out-of-sample validation**: report R² only against the **historical-mean benchmark**, never
   in-sample; **pre-register** the exact test specification for known events — specifically the 2011-15
   TBS episode and the 2018 IL&FS/NBFC episode — as held-out validation targets *before* looking at
   whether any candidate indicator would have flagged them, to avoid the obvious hindsight-bias trap of
   building an indicator that "detects" two events it was tuned to detect.
7. **Trial-count discipline**: log every element of the *h*-grid sweep (5 candidate values in each of
   two bands = 10), every pooling-weight specification tried, and every composition-signal
   parameterization in the **shared trial registry**, so the eventual deflated-Sharpe calculation
   (CONTRACT §9) reflects the true number of specifications searched across this workstream, not just
   the one that is finally reported.
8. **Registry entry**: every indicator above gets a `research/register/` entry with its free source
   URL, update frequency, known access constraints (e.g., FIMMDA member-login gate on I10's finest
   granularity), evidence tier, and the influence cap it is subject to — validated in CI per CONTRACT
   §10 (tier caps, tier-C reduce-only, budget containment).

---

## 7. Open questions and [VERIFY] items

1. **[VERIFY]** Baron & Xiong (F5): resolve the "95th percentile / 3-year / −37.3%" headline
   (confirmed against the NBER/QJE abstract) versus the "1.5σ / 8-quarter / −19.3%" figure surfaced in
   secondary summaries — likely both appear in the paper as different specifications/tables, but I
   could not independently confirm the second against primary text in this pass.
2. **[VERIFY]** The "7y short / 17y medium credit cycle, NBER dating, 1950-51 to 2020-21" study (I2):
   could not fetch the primary RBI PDF (rbidocs.rbi.org.in is egress-blocked in this environment);
   author/exact title unconfirmed. Directionally consistent with I1 and F1, but the point estimates
   should be re-verified against the primary document before being loaded into `research/register/`
   with anything above Tier-C confidence.
3. **[VERIFY]** BIS credit-to-GDP gap for India, "≈ −2.9 in Q1 2016" (I6): sourced via secondary press
   citation of BIS data, not a direct pull of the BIS series (also egress-blocked here). Re-verify
   against `data.bis.org` directly once network access allows, in the data phase.
4. **[VERIFY]** CCIL/FIMMDA AAA-vs-G-Sec spread figures reported by aggregator sites (I10) — the
   specific "2.21" figure is very likely a units error (percentage points reported where basis points,
   or vice versa, was intended); do not load any specific bps number into the registry without
   confirming against a primary CCIL PDF.
5. **[VERIFY]** Exact count of systemic banking-crisis episodes in the JST/Schularick-Taylor crisis
   chronology (used only qualitatively above as "several dozen" — needed if a hard Tier-A observation
   count is to be defended in the register rather than asserted qualitatively).
6. **Open design question**: how exactly should the bank+NBFC combined credit aggregate (I11) be
   constructed given that RBI does not publish one consolidated free series today? This is a data-
   engineering deliverable for the data phase, not resolvable in research-only mode.
7. **Open design question**: the pre-1991 Indian credit data reflects an administered-interest-rate,
   capital-controlled regime — a structural break from the post-1991 sample. Should pre-1991 data be
   pooled into "cycle length" estimates at all, or only used (if at all) as a separate, clearly-labeled
   regime? This affects both I1/I2's "post-reform" framing and any attempt to extend the domestic
   sample further back to improve the clock-test observation count.
8. **Open design question**: CONTRACT Known Prior #3 states the cycle stack is the RISK system, not
   the return system. This workstream's natural output is therefore a **regime multiplier / leverage-
   and-hedge-ratio state variable**, not a stand-alone alpha signal — I have written §4's parameters on
   that assumption throughout (reduce-only Tier-C satellites, lagging-confirmation framing for GNPA,
   percentile-rank rather than point-forecast framing for the medium-cycle prior). This should be
   explicitly reconciled with the other cycle-workstream dossiers (business/monetary/flow cycles; the
   multi-century debt arc) when the full ladder is assembled, since several of these state variables
   (credit-to-GDP gap, CD ratio, GNPA) plausibly correlate with state variables proposed in adjacent
   workstreams and must not be double-counted in the composite regime score's budget.
9. **Open design question (OPEN_QUESTIONS.md linkage)**: Q6 sets the moderate book as the anchor
   (factor book is the engine); this workstream's regime output feeds leverage/hedge-ratio state across
   all three books but with different consequences per book's leverage ceiling (contract §3) — the
   aggressive book's higher turnover cap and satellite sleeve (Q10) plausibly warrant a *faster*-updating
   credit-cycle proxy (CD ratio, I7) as the dominant input, while the conservative book (capacity-
   constrained, lower turnover) is better served by the slower-moving, better-measured GNPA/credit-to-
   GDP-gap combination — this book-level weighting split is proposed here as a hypothesis, not resolved.
