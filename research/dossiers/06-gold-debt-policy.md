# Dossier 06 — Gold Weight Function, Debt Sleeve, Policy Portfolio

Workstream: (a) what should drive the gold weight function and what ceiling the evidence actually
supports against the mandate's generous 50% cap; (b) why a flat 10% debt-sleeve assumption breaks
every optimizer (contract prior #5) and what a policy-portfolio construction rule looks like
instead; (c) Brinson-Hood-Beebower / Ibbotson-Kaplan correctly interpreted, so the design does not
over- or under-claim what asset allocation does.

**Process note, stated up front for honesty about provenance this pass.** This subagent's web
search budget was exhausted (200/200 used by earlier workstreams in this research program) before
any fresh query could run for this dossier, and WebFetch returned `EGRESS_BLOCKED` for every
domain tested (SSRN, Wikipedia, gold.org, rbi.org.in, nseindia.com, bis.org) — consistent with
contract known-prior #11 ("no market-data network access... web search works") except that here
the search channel was also unavailable. Every citation below is therefore drawn from trained
recall, not a fresh verification search, and is marked accordingly: **[recall-verified]** for
citations I hold with high confidence on author/title/venue/year (well-known, widely-replicated
papers), and **[VERIFY: ...]** for anything numeric, dated, or India-specific enough that it needs
a live confirmation pass once search access is restored — per the contract's own instruction to
keep the finding and tag it rather than drop it or invent false certainty. Section 7 collects every
tag. This is a process deviation the principal should be aware of; it does not change the
analytical structure below, which is built to be robust to the exact numbers being off by the
margin a data-phase pull will correct.

---

## 1. Findings and literature

**Gold's valuation anchor and the real-rate link**

1. Erb & Harvey (2013), "The Golden Dilemma," *Financial Analysts Journal* 69(4): 10–42 (also
   circulated as NBER Working Paper 18706) **[recall-verified]**. Builds on Jastram's (1977) *The
   Golden Constant* observation that gold's *real* (CPI-deflated) price is stationary only over
   century-plus horizons — at any shorter horizon (a decade, even several decades) it can sit far
   above or below its long-run anchor, so "gold preserves purchasing power" is a truth about
   100+ year windows, not an investable multi-decade thesis. Central empirical finding: over their
   sample, the real gold price is strongly **negatively** correlated with the U.S. real (TIPS)
   yield — low or negative real rates raise the relative attractiveness of a zero-yield asset and
   coincide with higher real gold prices, and vice versa. Gold's correlation with realized/expected
   inflation is weak and unreliable at 5–10 year horizons (gold is a poor *short-to-medium-run*
   inflation hedge despite the popular narrative); the inflation-hedge property only shows up over
   century-scale windows. The paper's title names its real point: unlike equities (dividend yield +
   growth) or bonds (coupon + duration), gold has **no cash-flow-based valuation anchor**, so any
   allocation is implicitly a bet on future price appreciation/store-of-value demand, not a claim
   on a modeled expected return. This is the load-bearing citation for treating gold as a
   diversification instrument sized for its correlation properties, not as a return-forecastable
   asset sized off a model of its own expected return. Effect size: correlation coefficients on the
   order of −0.5 to −0.8 for real gold price vs. real yield depending on sub-sample (I recall the
   direction and rough magnitude with confidence; exact point estimates need re-extraction from the
   text — [VERIFY: exact correlation coefficients and sub-sample windows]).

2. Post-2022 partial breakdown of the real-rate link — **[VERIFY: no fresh citation retrievable
   this session; stated as a well-documented market fact from trained knowledge, not a specific
   paper]**. From 2022 onward, gold rallied to repeated nominal all-time highs *while* global real
   rates (US 10y TIPS yield) rose sharply through the Fed's hiking cycle — the opposite of the
   Erb-Harvey-era relationship. The dominant explanation offered by market commentary and by World
   Gold Council (WGC) demand-trends releases is a structural shift in the marginal buyer: record
   official-sector (central bank) gold purchases starting 2022, widely linked to reserve
   diversification away from USD-denominated assets after the Feb-2022 freezing of Russian central
   bank reserves demonstrated the political risk of dollar reserves to non-aligned central banks
   (China, several EM/Gulf central banks named in commentary). **This is a state-variable
   observation, not a fitted regime-switching model** — the distinction matters under contract
   Section 8 ("do not fit regime-switching models without ≥10 observed transitions"): we are not
   proposing to fit a switch, only to condition on an exogenously published series (WGC quarterly
   central-bank net purchases) the same way the design already conditions on other macro state
   variables. Because this regime is <4 years old as of 2026, it is Tier C on its own persistence
   (no clock-test passes) even though the underlying mechanism (sanctions-driven reserve
   diversification) has an intelligible institutional-constraint logic. **Design implication: do
   not delete the real-rate input, halve its weight** and let a second, independently-sourced input
   (the WGC buying-regime state) carry the rest, so the gold function degrades gracefully if either
   mechanism itself decays rather than betting the whole tactical signal on one relationship that
   has already shown it can go quiet for years at a time.

**Safe-haven / crisis-hedge literature**

3. Baur & Lucey (2010), "Is Gold a Hedge or a Safe Haven? An Analysis of Stocks, Bonds and Gold,"
   *Financial Review* 45(2): 217–229 **[recall-verified]**. Introduces the now-standard definitional
   split: a **hedge** is an asset uncorrelated or negatively correlated with another asset *on
   average*; a **safe haven** is uncorrelated or negatively correlated only *in times of market
   stress* (a weaker, conditional property, and the more decision-relevant one for a drawdown-bound
   mandate). Using US, UK and German data, finds gold is both a hedge and a safe haven for stocks,
   but the safe-haven property is **time-limited** — roughly the first ~15 trading days after an
   extreme negative equity shock — after which the relationship can revert; gold is not a safe
   haven for bonds. Effect size: reports negative/insignificant gold-equity correlation
   coefficients specifically in the tails of the return distribution, contrasted with small positive
   average correlation [direction verified from recall; exact coefficients — VERIFY].

4. Baur & McDermott (2010), "Is Gold a Safe Haven? International Evidence," *Journal of Banking &
   Finance* 34(8): 1886–1898 **[recall-verified]**. Extends the test internationally and finds gold
   was a strong hedge/safe haven for **major developed markets (US, several European markets)**
   especially through the 2008 global financial crisis, but the safe-haven property is markedly
   **weaker or largely absent for Australia, Canada, Japan and for the large emerging markets they
   test (the BRIC bloc, which includes India)**. This is the single most important caution for our
   India-specific design: the headline "gold is a safe haven" result in the literature is
   substantially a developed-market, USD/EUR-denominated finding. For an INR-based mandate this
   matters two ways — (i) do not assume the USD-gold-vs-BRIC-equity safe-haven effect transfers at
   full strength; (ii) but the relevant object for us is not USD-gold vs. INR-equity, it is
   **INR-gold vs. INR-equity**, and INR depreciation during EM/India stress episodes (Section 2)
   can restore a meaningful hedge even where the USD-gold-vs-BRIC-equity channel is weak. The two
   effects are separable and the second is the more India-relevant one.

5. O'Connor, Lucey, Batten & Baur (2015), "The Financial Economics of Gold: A Survey,"
   *International Review of Financial Analysis* 41: 186–205 **[recall-verified]**. Survey covering
   gold pricing determinants (real rates, USD, inflation, geopolitical risk proxies), the
   hedge/safe-haven literature, and gold market microstructure/lease-rate dynamics. Useful mainly as
   the aggregator that turns Baur-Lucey/Baur-McDermott-style country-by-country tests into a
   cross-country panel with well over ten market/episode combinations — this is what licenses
   treating the safe-haven property as **Tier B via the contract's cross-country-analogue clause**
   (n<4 India-specific episodes, but ≥10 cross-country analogues in the survey's own citation base)
   rather than Tier C.

**Momentum and factor-decay literature (already load-bearing for the gold tactical input)**

6. Moskowitz, Ooi & Pedersen (2012), "Time Series Momentum," *Journal of Financial Economics*
   104(2): 228–250 **[recall-verified]**. Documents trend-following (sign of trailing 1–12 month
   own return) working across 58 liquid futures markets including commodities (gold among them),
   equity indices, bonds and currencies, with a common-factor structure across asset classes. This
   is the standing survival argument for a gold momentum tilt: institutional-constraint /
   capacity-limit persistence via managed-futures/CTA capital, not a gold-specific anomaly needing
   its own argument. Caution: CTA/trend Sharpe ratios are widely reported to have compressed since
   the 2010s (partial decay already realized), so this should enter as a modest tilt weight, not a
   primary driver, and should carry a McLean-Pontiff-style haircut by default (below).

7. Jacobs & Müller (2020), "Anomalies Across the Globe: Public Sources of Common Risk?," *Journal
   of Financial Economics* 135(3): 213–230 **[recall-verified]**. Tests McLean-Pontiff's US
   post-publication decay result outside the US and finds non-US anomaly returns **did not**
   shrink after publication the way US anomalies did — i.e., international markets show materially
   less arbitrage-driven decay, consistent with thinner arbitrage capital and higher frictions
   outside the largest, most liquid market. Direct implication for this workstream: India-specific
   or India-observed edges (including gold-related ones) should **not** automatically receive the
   full McLean-Pontiff 26%/58% haircut calibrated on US data; the correct prior is a smaller haircut
   with wide uncertainty, to be re-estimated once genuine India time series exist, not assumed away
   to zero either.

8. Chordia, Subrahmanyam & Tong (2014), "Have Capital Market Anomalies Disappeared?," *Journal of
   Accounting and Economics* 58(1): 41–58 **[recall-verified, exact volume/page — VERIFY]**.
   Documents attenuation of anomaly returns as arbitrage capital and trading volume/liquidity
   increase over time — the mechanism (not just the fact) behind McLean-Pontiff's decay estimate,
   already load-bearing in the contract's governing principle (Section 5).

**Asset-allocation attribution literature**

9. Brinson, Hood & Beebower (1986), "Determinants of Portfolio Performance," *Financial Analysts
   Journal* 42(4): 39–44 **[recall-verified]**. The famous "asset allocation explains ~93.6% of
   performance" result. **What it actually shows**: decomposing the *time series* of a fund's
   quarterly total return into a policy-mix (buy-and-hold benchmark) component and an active
   (timing + selection) component, the policy component explains ~93.6% of the **variance of that
   one fund's own quarterly returns over time**. It says nothing about (a) the variance of returns
   *across different funds* (a cross-sectional question), (b) the *level* of return achieved, or
   (c) whether active management adds value — a fund with a fixed 60/40 policy earns ~93.6% of its
   own return-variance explanation from that policy almost by construction, regardless of whether
   the manager is skilled. This is the single most commonly misquoted finance result and the
   contract's own workstream question flags it correctly.

10. Ibbotson & Kaplan (2000), "Does Asset Allocation Policy Explain 40, 90, or 100 Percent of
    Performance?," *Financial Analysts Journal* 56(1): 26–33 **[recall-verified]**. Directly
    disambiguates three different questions that BHB's headline number gets collapsed into: (i) how
    much of a **typical single fund's return variance over time** does its policy mix explain →
    confirms BHB, ~90%; (ii) how much of the **variance of returns across different funds**
    (cross-sectional) is explained by their differing policy mixes → only **~40%**; (iii) how much
    of the **level** of a fund's return is explained by simply holding its passive policy weights
    (i.e., how much value did active timing+selection add on average) → **roughly 100%** on average
    across their sample — meaning the *average* fund's active decisions added close to zero net
    value relative to its own passive policy replication, though with wide dispersion across
    individual funds (some added a lot, some subtracted a lot). This third result is the one most
    often dropped when people cite "BHB": it is evidence about the *average* manager, not a
    statement that active management cannot work — the dispersion around that zero average is
    exactly the space a decay-aware, evidence-tiered process is trying to sit on the right side of.

11. Michaud (1989), "The Markowitz Optimization Enigma: Is Optimized Optimal?," *Financial Analysts
    Journal* 45(1): 31–42 **[recall-verified]**. The classical demonstration that mean-variance
    optimization is an "error-maximizing" machine: small input errors (especially in expected
    returns) produce extreme, unstable, corner-heavy allocations, because the optimizer chases
    whichever asset has the best *assumed* Sharpe ratio without regard to how uncertain that
    assumption is. This is the general mechanism behind contract prior #5's corner solutions
    (MVO wanting 70% debt, risk parity wanting 67%) — not an India-specific quirk but the textbook
    behavior of any variance-based optimizer fed a near-certain high-Sharpe input, which is exactly
    what a flat, assumed 10% debt return with implicitly near-zero assumed variance is.

---

## 2. India-specific evidence

**INR gold return decomposition.** The identity is exact and needs no estimation: for USD gold
return `r_g` and USDINR return `r_fx` (INR depreciation positive), INR gold return
`r_INR = (1+r_g)(1+r_fx) − 1 ≈ r_g + r_fx + r_g·r_fx`. Over multi-decade horizons INR has
depreciated against USD essentially continuously (current-account-deficit and inflation-differential
driven, a very high-observation-count macro fact, easily Tier A by observation count even though it
is a trend rather than a risk premium in the academic sense) — so the **INR-denominated gold return
has historically exceeded the USD-denominated gold return by roughly the pace of INR depreciation**,
a genuine structural tailwind for INR gold holders distinct from anything about gold itself. This
decomposition is why India-specific gold-return backtests must never be run on USD gold series
translated at a single spot rate; the depreciation component is large enough over a 10–20 year
window to change conclusions about gold's role in an INR portfolio (data-phase requirement, Section
6).

**Crisis episodes, INR terms (illustrative, from macro-historical recall — magnitudes to be
recomputed from free bhavcopy/WGC archives in the data phase, not treated as backtested facts
here):**

- **2008 GFC.** Nifty fell roughly 55–60% peak-to-trough (Jan–Oct/Nov 2008). USD gold itself fell
  sharply in the acute Sep–Oct 2008 liquidity panic (a "sell everything, including the hedge"
  window — consistent with Baur-Lucey's caveat that the safe-haven property can fail in the most
  extreme, most correlated days) before recovering. INR depreciated materially over the same window
  (roughly ₹39/USD to ₹50/USD, order of 25%+). Over the **full episode window** INR gold ended up
  materially positive for the year while Nifty was down heavily — a genuine cushion on a
  quarter-to-year view, but with its own intra-episode drawdown that would have shown up in a
  daily-mark drawdown calculation. [illustrative — VERIFY exact levels/dates in data phase]

- **2013 taper tantrum.** USD gold was already in its own 2013 bear market (2013 was gold's worst
  USD year since 1981, roughly −28%), so the taper tantrum months (May–Aug 2013) combined a falling
  USD gold price with a sharply depreciating INR (roughly ₹55/USD to ₹68/USD, ~19% over a few
  months). The depreciation partially offset the USD gold decline, but the net effect was INR gold
  roughly flat to mildly negative through the acute window — a materially **weaker** hedge episode
  than 2008 or 2020, and the clearest illustration in Indian market history that gold's own bear
  market can overwhelm the INR-depreciation cushion. Important discipline point: this episode alone
  should prevent the design from treating "INR depreciation always rescues gold's INR return in a
  crisis" as a reliable rule. [illustrative — VERIFY]

- **2020 COVID crash.** Nifty fell ~38% in about five weeks. USD gold *also* fell sharply for a few
  days in the mid-March 2020 "dash for cash" (a second real-world instance of the extreme-day
  correlation-breakdown Baur-Lucey flag), then rallied to new nominal all-time highs by August 2020
  as real rates collapsed toward zero (Fed cuts + QE) — a textbook Erb-Harvey real-rate response.
  INR depreciation was comparatively modest this episode (~₹74/USD to ~₹76/USD). INR gold ended 2020
  up roughly high-20s percent, a strong hedge over the recovery window despite the shared bad day at
  the trough. [illustrative — VERIFY]

- **2022.** Not a qualifying >20% Nifty episode under the frozen drawdown definition, but relevant
  for the real-rate-breakdown question: USD gold was roughly flat on the year despite the sharpest
  global rate-hiking cycle in decades — itself evidence for finding #2's real-rate decoupling — while
  INR depreciated (~₹74/USD to ~₹82/USD, ~10%), so INR gold posted a modest positive return with no
  equity crisis to hedge against. [illustrative — VERIFY]

- **2024–25.** As of this research date no Nifty episode in this window clearly clears the frozen
  >20% bar (a 2024Q4–2025 mid/smallcap-led correction is widely discussed but its magnitude at the
  Nifty-50 level needs data-phase confirmation against the episode definition). Separately, gold had
  one of its strongest runs on record through this window, commonly attributed in market commentary
  to continued record central-bank buying, US fiscal/debt-sustainability concerns, and elevated
  geopolitical risk premia. Because this is recent and not yet a settled academic data point, treat
  as **directionally correct, magnitude unverified** [VERIFY].

**Import duty and the INR-gold "wedge."** India is structurally an import-dependent, price-taking
gold market: the domestic price = international USD price × USDINR + import duty + GST + a local
demand/supply premium-or-discount. Two policy facts materially distort any naive backtest that spans
them: (i) duty was raised sharply (to defend the currency during the 2013 current-account-deficit
crisis, alongside the "80:20" export-obligation scheme) — a genuine regime shift in the constant
"wedge," not noise; (ii) the July-2024 Union Budget cut customs duty on gold and silver substantially
(commonly reported as a cut from ~15% total duty to a materially lower single-digit rate), producing
a one-time, policy-driven step-down in the domestic-vs-international price wedge that any INR-gold
return series spanning that date must treat as a level break, not a return — exactly analogous to
the contract's warning about restated-fundamentals look-ahead bias (prior #7): a naive return
calculation across the duty-change date would misattribute a policy step to a market move.
**[VERIFY: exact pre/post duty rates and effective date — could not confirm this session]**. This is
important enough that the data-phase build should explicitly flag the July-2024 date (and the 2013
duty-hike dates) as regime breaks in the INR-gold series, not fit through them.

**Seasonality (demand-side, not price-timing).** India's gold demand has well-documented seasonal
structure — Akshaya Tritiya, Dhanteras/Diwali, the Oct–Feb wedding season, and post-harvest rural
buying tied to Rabi-crop cash flows (a pattern WGC's quarterly India demand-trends releases track).
This is a *demand-flow* seasonality, not necessarily a *price-predictability* signal for a
price-taking global market; it belongs in the design as context for local-premium/discount behavior
and physical-market liquidity conditions, not as a standalone tactical timing input (no evidence
reviewed here supports fitting a calendar-return signal to it, and the contract's Section 8
explicitly forbids fixed-period calendar cycles).

**Implementation: ETF vs. futures vs. the now-closed SGB channel.**

- **Sovereign Gold Bonds (SGBs)**, issued by RBI on the government's behalf since November 2015,
  were until recently the dominant Indian-specific gold vehicle: no expense ratio, no storage cost,
  a 2.5% p.a. coupon (positive carry on top of the gold price return), and capital-gains-tax-free
  redemption for individuals holding to the 8-year maturity — a genuinely dominant instrument versus
  ETFs/futures whenever available. Market commentary through 2024–2025 describes the government
  **pausing or effectively discontinuing new SGB issuance**, with the fiscal cost of a gold-price-linked
  redemption liability (worsened by gold's rally) cited as the rationale. **[VERIFY: exact
  discontinuation date, whether any tranche calendar remains open, and the official rationale —
  could not confirm this session; treat as unconfirmed until an RBI/Finance-Ministry press-release
  pull in the data phase]**. Practically this is moot for the design: the contract already restricts
  gold exposure to **ETF and futures only** (Section 3), so SGB availability does not change the
  instrument menu — but it is worth recording *why* that restriction is sensible even independent of
  the contract's choice: the best pre-2024 vehicle may no longer be issuing, so ETF/futures were
  already becoming the load-bearing channel regardless.

- **Gold ETFs** (exchange-traded, physically backed, e.g., the long-standing Nippon India ETF Gold
  BeES and several newer/cheaper entrants): expense ratios in Indian gold ETFs are commonly cited in
  roughly a 0.4%–0.8% p.a. range with newer funds undercutting older ones, small tracking error given
  physical backing, good exchange liquidity for the larger funds, no leverage, no roll management.
  **[VERIFY: current AMC-by-AMC expense ratios and tracking-error statistics — need an AMFI/scheme-
  document pull in the data phase, not a recalled number]**.

- **MCX gold futures** (1 kg contracts, plus Gold Mini/Guinea/Petal for smaller lot sizes): allow
  embedded leverage via margin (which must be delta/notional-accounted toward the 1.5x gross cap per
  the contract's leverage conventions, Section 10), require active roll management with a
  cost driven by the domestic interest-rate/lease-rate calendar spread, no storage cost, and are
  priced off international spot converted at USDINR plus the duty/GST/local-premium wedge described
  above (so futures roll cost estimation must separately account for wedge changes, e.g. around the
  July-2024 duty cut, not treat roll P&L as pure cost-of-carry). **[VERIFY: measured historical roll
  cost in basis points per roll and typical margin percentage — illustrative "20–40 bps per roll"
  figures exist in market commentary but were not independently confirmable this session]**. A
  further institutional point worth flagging: SEBI's framework for portfolio managers to access
  commodity derivatives (reportedly opened up via a circular around 2017 allowing SEBI-registered
  portfolio managers to also register on commodity exchanges) governs whether/how a PMS-style vehicle
  can hold MCX futures directly rather than only ETFs. **[VERIFY: exact SEBI circular reference and
  any conditions/limits attached — could not confirm this session]**.

- **Net implementation read**: ETFs are the simpler, lower-operational-complexity default for the
  structural floor (all three books); futures are the natural venue for the *tactical* band's
  incremental exposure precisely because they carry embedded leverage cheaply and can be sized up
  and down fast without touching the floor's ETF holding — but every basis point of assumed roll
  cost and tracking error needs a data-phase measurement before it enters any cost model, not an
  assumption carried from this dossier.

---

## 3. Decay and crowding assessment

| Edge / input | Survival argument | Decay/haircut applied |
|---|---|---|
| Real-rate ↔ gold link (pre-2022 form) | (iii) genuine opportunity-cost mechanism: a zero-yield asset's relative attractiveness is mechanically tied to the yield foregone by holding it — this is arithmetic, not an arbitraged-away anomaly, so it should not decay to zero. But its *dominance* as the marginal driver has visibly weakened since 2022. | Halve the naive weight (~50% haircut) rather than remove; redistribute to the buying-regime state input. Numeric haircut is judgment-based, not literature-derived — flagged Tier C on the haircut's own size, to be re-estimated once ≥4 years of post-2022 data exist. |
| Central-bank buying-regime state | (iv) institutional constraint: this is sovereign reserve-management behavior driven by geopolitical risk aversion, not return-chasing capital, so it is not subject to the usual crowding-out-by-arbitrageurs mechanism — but it is also not proven persistent (a policy reversal, e.g. reserve rebalancing back toward USD, could end it abruptly). | Treat as a state variable with **zero assumed persistence beyond the observed series** (no forecast that buying continues); Tier C by the clock test (<4 yrs history), so it may only add to the structural floor modestly, never justify removing the floor. |
| INR depreciation / REER tilt | (iii) genuine risk premium-adjacent: a structural current-account/inflation-differential depreciation trend, and (iv) an institutional constraint (capital controls limit fast arbitrage of currency misvaluation). Rogoff (1996), "The Purchasing Power Parity Puzzle," *Journal of Economic Literature* 34(2): 647–668 **[recall-verified]**, documents a widely cited ~3–5 year consensus half-life for real exchange-rate deviations from PPP — a genuinely persistent, slow-moving mean-reversion property, not an anomaly that decays under crowding. | No McLean-Pontiff-style haircut applied (mechanism is macro/structural, not a discovered cross-sectional anomaly); size modestly because FX timing precision is inherently low (±20% timing uncertainty class per contract Section 1, similar in spirit to the long-cycle caveat). |
| Gold momentum (12m/6m sign or rank) | (ii) capacity limit / (iv) institutional constraint: managed-futures/CTA capital is the natural arbitrageur and is itself capacity-constrained and does not fully compete away commodity TSMOM (Moskowitz-Ooi-Pedersen). But CTA Sharpe compression since the 2010s is widely reported — partial decay has already happened. | Apply the contract's default McLean-Pontiff post-publication haircut (~58%) as the conservative prior for the *US/global* commodity-momentum literature, but note Jacobs-Müller's finding that non-US anomalies decay less — since gold momentum as applied here is measured substantially through an India-facing (INR) lens even though gold itself is a global asset, split the difference: haircut in the ~35–45% range as a working assumption, low confidence, to be replaced by a directly measured India-period half-life in the data phase. |
| Safe-haven / crisis kicker | (i) structural/behavioural: flight-to-quality is a well-documented behavioral response (portfolio insurance demand spikes in stress), not a price-based arbitrage relationship, so it is not expected to decay from crowding — more capital chasing safety in a crisis does not eliminate the safety premium. Caveat from Baur-McDermott: effect size for BRIC/EM equities specifically is **weaker** than for developed markets in USD terms, though the INR-depreciation channel is separable and can restore effect size in local-currency terms. | No decay haircut for the mechanism; instead a **magnitude discount** for India specifically (do not assume US/European-market safe-haven magnitudes transfer 1:1) — recommend sizing the India crisis-kicker at roughly half the magnitude implied by developed-market studies until India-specific episodes (Section 2) are formally measured. |
| Structural gold floor (long-wave / monetary-debasement thesis) | Explicitly **Tier C, narrative only**, per contract Section 4 — fewer than four complete observations of a fiat-regime devaluation/reserve-diversification cycle exist in the modern floating-FX era (candidates: 1933 devaluation, 1971 Bretton Woods collapse, and an arguably-ongoing 2020s dedollarization episode — at most 2–3 completed instances, clock test fails). Per contract's own rule, **Tier-C signals may only reduce risk, never add** — so this cannot be sized as a return bet; it must be framed purely as the reason a *non-zero floor* is held at all times as a standing diversifier, never as a reason to raise gold above its floor+tactical ceiling. | No haircut applicable (it is not a decaying empirical signal); the discipline instead is a **hard cap on its own influence** — it may only justify the floor's existence and size, never the tactical band's upper reach. |
| Policy-portfolio construction rule itself (fixed weights, no asset-mix optimization) | Not an empirical edge subject to decay at all — it is a design principle grounded in Michaud (1989)'s well-replicated optimizer-fragility result and in Ibbotson-Kaplan's variance decomposition. Its "survival" is logical/structural, not arbitrage-dependent. | N/A — no haircut; the only way this changes is a principal-level architecture override (contract Section 2 already reserves this decision). |

---

## 4. Proposed parameters

| Name | Value/range | Source | Tier | Confidence | Decay assumption | What would change it |
|---|---|---|---|---|---|---|
| Gold structural floor — conservative book | 8–12% of book NAV | Baur-Lucey/Baur-McDermott safe-haven mechanism + Tier-C long-wave floor argument (Section 3); cross-country analogue via Harry Browne-style "Permanent Portfolio" 25% heuristic as an upper-bound sanity check, not a target [VERIFY: exact Permanent Portfolio attribution/date] | B (mechanism) / C (sizing itself, narrative) | Medium | None on the floor's existence; the *size* should shrink only if ≥10 independent stress episodes (cross-country analogue count) show gold-equity correlation turning reliably positive in the relevant regime | Evidence of sustained positive gold-equity correlation across ≥10 independent stress episodes (i.e., safe-haven property itself breaking), or a cheaper/more liquid India tail-hedge instrument dominating gold on a risk-adjusted basis |
| Gold structural floor — moderate book | 4–7% of book NAV | Same as above, scaled down because the moderate/anchor book's primary hedge is the factor-book's own lower-beta construction (per other dossiers), gold is a secondary diversifier | B/C | Medium | Same as above | Same as above |
| Gold structural floor — aggressive book | 2–4% of book NAV | Same mechanism, sized lowest because the aggressive book's primary tail protection is options/leverage cuts (established in the drawdown-control workstream), gold is tertiary | B/C | Medium | Same as above | Same as above |
| Gold tactical band ceiling — conservative | Floor + up to ~10–12pp (total ceiling ~20–24%) | No non-sponsor-affiliated study reviewed supports a strategic gold weight materially above ~20–25% even in tail-risk-budgeted frameworks; WGC's own "optimal allocation" studies (routinely citing higher, e.g. 10–20%+) carry an acknowledged sponsor conflict of interest (WGC exists to promote gold demand) and are excluded as a parameter source here | C (construction) | Low-medium | N/A (a ceiling, not a decaying signal) | A published, non-industry-funded optimization study using India-specific covariances that robustly clears ~25% |
| Gold tactical band ceiling — moderate | Floor + up to ~14–18pp (total ceiling ~20–25%) | Same reasoning, book widened slightly because the anchor book's regime-conditioning signals (real-rate, buying-regime, crisis kicker) are richer inputs to lean on | C | Low-medium | N/A | Same as above |
| Gold tactical band ceiling — aggressive | Floor + up to ~10–14pp (total ceiling ~15–18%) | Narrower because options already carry the primary convex-hedge role; gold tactical band mainly a diversifier-of-diversifiers | C | Low-medium | N/A | Same as above |
| Real-rate input weight in composite | ~0.15–0.20 (post-2022 haircut from a naive ~0.35) | Erb-Harvey mechanism + observed post-2022 decoupling (Section 1, finding #2) | C (haircut size) | Low | Re-weight upward if the real-rate/gold correlation re-establishes over a fresh ≥4-year window | ≥4 consecutive quarters of net central-bank *selling* without a real-rate fall, which would argue the old link is dead rather than supplemented |
| Central-bank buying-regime weight | ~0.20–0.25 | WGC Gold Demand Trends quarterly central-bank net purchases (free, quarterly) | C | Low-medium | State variable, no decay assumed; persistence itself is the open question | Regime ending (≥4 quarters of net selling) or WGC methodology change |
| INR depreciation / REER tilt weight | ~0.20–0.25 | RBI DBIE 36-currency REER index; Rogoff (1996) PPP half-life literature | B | Medium | Low decay (macro mean-reversion, not an arbitraged anomaly) | Structural change in India's current-account/inflation-differential regime (e.g., sustained current-account surplus) |
| Gold momentum tilt weight (12m/6m rank) | ~0.15–0.20, haircut 35–45% vs. naive TSMOM sizing | Moskowitz-Ooi-Pedersen (2012); Jacobs-Müller (2020) for the reduced-decay-outside-US adjustment | B | Medium-low | 35–45% haircut per Section 3 | A directly measured India-period gold-momentum half-life from the data phase, replacing the assumed haircut |
| Crisis/vol-regime kicker weight | ~0.15–0.20, magnitude at ~50% of developed-market Baur-McDermott estimates | Baur-Lucey; Baur-McDermott (BRIC caveat); O'Connor et al. survey (cross-country analogue clause) | B | Medium | No crowding-decay; India-specific magnitude discount instead | Formal measurement of India-specific gold-equity tail correlation across the 2008/2013/2020/2022 episode set once data phase runs |
| Debt-sleeve realistic-return shadow estimate | ~6.0–7.5% nominal, vs. frozen 10% bookkeeping assumption | RBI DBIE repo/T-bill/reverse-repo series (well-observed short-rate history; general logic Tier A, specific current level unverified this session) | A (logic) / needs fresh pull (level) | Medium | N/A (rate level, not an anomaly) | Actual RBI policy-repo path over the design horizon |
| Policy-portfolio construction rule | Fixed weights per book × regime state; debt = 100% − equity policy weight − gold weight(book,t); never optimizer output | Michaud (1989); Ibbotson-Kaplan (2000); contract Section 2 (Stage 3 optimizes equity cross-section only) | A (rule logic) | High | N/A | Only a principal-level architecture override |
| Gold ETF expense ratio (cost input) | ~0.4–0.8% p.a., illustrative | Market commentary on Indian gold ETF AMCs | C (unverified) | Low | N/A | AMFI/scheme-document pull, data phase |
| MCX gold futures roll cost (cost input) | ~20–40 bps/roll, illustrative | Market commentary | C (unverified) | Low | N/A | Measured roll-cost series from MCX contract history, data phase |

---

## 5. Evidence-tier recommendations

- **Real-rate ↔ gold link (pre-2022 regime)**: Tier B. The underlying opportunity-cost mechanism
  is arithmetic and old (decades of monthly TIPS-era data since 1997 give well over 30 monthly
  observations, but the economically relevant unit is independent real-rate *cycles/regimes*, of
  which the TIPS era offers roughly 4–6 — e.g., 2000s low-rate era, 2004–07 tightening, 2008–15
  ZIRP, 2015–18 tightening, 2020–21 ZIRP, 2022–23 hiking). That puts it at 4–30 independent
  regime-level observations — squarely Tier B, parameters frozen at inception per contract Section
  4.
- **Post-2022 real-rate/gold decoupling and central-bank-buying regime**: Tier C. One regime
  observation (n=1, <4 years), clock test fails outright; correctly treated as narrative/state
  variable, not fitted, per contract Section 8's ≥10-transition rule for regime-switching models
  (we are not fitting a switch, only conditioning on an exogenous published series).
- **Safe-haven/crisis-hedge property of gold**: Tier B via the cross-country-analogue clause — India
  itself offers only 3–4 qualifying crisis episodes (2008, 2013, 2020, arguably 2022), but the
  O'Connor et al. survey and the Baur-Lucey/Baur-McDermott country panels give well over ten
  independent market/episode combinations globally.
- **INR depreciation trend**: Tier A on the observation-count of the depreciation fact itself
  (decades of monthly USDINR data, essentially a continuous trend since managed/floating regimes
  began) though it is better described as a well-documented macro regularity than a risk-premium
  "effect" in the academic anomaly sense; Tier B on the *exploitable half-life* claim (Rogoff's
  3–5 year PPP half-life is itself a cross-country consensus estimate, not a single-country fitted
  number).
- **Gold momentum**: Tier B. Moskowitz-Ooi-Pedersen's cross-asset TSMOM result spans 58 markets and
  decades — comfortably ≥30 independent market-years by any reasonable count — but the
  India-specific/INR-denominated application has far fewer independent observations, so Tier B (not
  A) is the honest India-facing tier, consistent with the contract's instruction to mark
  cross-country priors as Tier B at best.
- **Structural gold floor / long-wave thesis**: Tier C, explicitly, exactly as the contract already
  frames it (Section 4's own worked example). Reduce-risk-only.
- **Policy-portfolio construction rule (fixed weights, no asset-mix optimization)**: Not a
  classical "effect" with an observation count — it is a design principle. The supporting evidence
  for the *principle* (optimizer fragility under near-certain-return inputs) is abundant and
  decades-replicated (Michaud 1989 plus a large subsequent robust-optimization literature), so treat
  the principle itself as resting on Tier-A-strength support even though no single "observation
  count" applies to a construction rule.
- **BHB/Ibbotson-Kaplan variance decomposition**: Tier A. Replicated across many subsequent fund
  studies over decades with large N of both funds and time periods; the three-way disambiguation
  (time-series variance vs. cross-sectional variance vs. level-of-return) is itself well
  established in the subsequent literature, not a one-off result.

---

## 6. Research method for the data phase

- **Real-rate/gold link, recalibration.** India's own inflation-linked bond history (capital-indexed
  bonds / IINSS-C) is short and illiquid, so the primary real-rate series should be the US 10y TIPS
  yield (FRED, free, series `DFII10`), with an India real-short-rate proxy (RBI policy repo rate
  from RBI DBIE minus MOSPI CPI y/y expected inflation) as a secondary confirming state variable, not
  the primary input. Test the pre/post-2022 sub-sample split with a simple structural-break test
  (e.g., a Chow-type test on the rolling correlation) — this is a **break test on an existing
  relationship**, not a regime-switching model fit, so it does not trigger the contract's ≥10-
  transition prohibition (Section 8). Where India alone cannot support the test (too few independent
  real-rate cycles), pool with the broader cross-country real-rate/gold panel the way the contract
  already directs pooling on the JST panel for cycle-scarce questions (Section 9).
- **Central-bank buying-regime state.** Read directly from WGC Gold Demand Trends quarterly reports
  (free download) as an exogenous conditioning variable — explicitly not fitted, per the
  regime-switching prohibition. No statistical estimation needed beyond correctly parsing the
  published series; the open question is persistence, which by construction cannot be resolved
  until more history accumulates (documented as an open question in Section 7, not forced by
  premature model-fitting).
- **INR depreciation / return decomposition.** Pure data hygiene, not estimation: pull WGC/LBMA USD
  gold price and RBI DBIE reference USDINR rate (both free), compute the exact identity
  `r_INR ≈ r_g + r_fx + r_g·r_fx` period by period, and explicitly flag the 2013 duty-hike and
  July-2024 duty-cut dates as wedge-level breaks to be excluded from any return-continuity
  calculation (not fit through, per the contract's restated-fundamentals look-ahead-bias caution,
  prior #7, applied here by analogy).
- **Gold momentum tilt.** Purged and embargoed walk-forward validation on quantile-ranked trailing
  return (test 1m/3m/6m/12m lookbacks together, since all four are "the true trial count" per
  contract Section 9 — deflate the Sharpe accordingly), embargo width scaled to the measured
  autocorrelation half-life of the chosen lookback (measure `tau_half` first, per contract Section
  4's cycle-authority ordering, rather than assuming a fixed embargo). Apply Stambaugh correction if
  a persistent quantile-scaled predictor is used. Judge out-of-sample R² against the historical-mean
  benchmark, never in-sample.
- **Crisis/vol kicker.** Validate against the frozen India >20%-fall episode set (per OPEN_QUESTIONS
  #5's flash-crash-exclusion default) **plus** cross-country analogue episodes (other EM
  equity-crisis / local-currency-gold-return pairs drawn from the Baur-McDermott/O'Connor country
  panels) to build a pseudo-sample of ≥10 observations, honoring the Tier-B cross-country-analogue
  allowance rather than fitting a switching model on India's 3–4 native episodes alone.
- **Debt-sleeve realistic-return shadow estimate.** Pull RBI DBIE repo/reverse-repo/T-bill series,
  CCIL TREPS overnight-rate history, and AMFI overnight/liquid-fund NAV history (all free) to build
  a running, continuously-updated estimate of achievable net debt-sleeve yield, and track the gap to
  the frozen 10% bookkeeping assumption explicitly every period (a monitored gap, not a one-time
  guess) so the ~400bps override stays visible and auditable rather than silently baked in.
- **Policy-portfolio equity/gold/debt split per regime state.** Not optimized, per the architecture
  (contract Section 2, Trap list item 1: "do not optimize the asset mix"). Validated only by
  simulating realized portfolio vol/drawdown under the fixed policy weights across historical
  regime-state sequences — a scenario/stress test, not a fit — cross-checked jointly with the
  leverage/regime parameters set in the drawdown-control workstream so the two designs are
  consistent rather than independently re-deriving the same regime taxonomy.
- **Implementation costs (ETF expense ratio, tracking error, MCX roll cost).** Pull AMFI
  scheme-document expense-ratio disclosures and MCX exchange circulars/contract roll-history (both
  free, exchange filings) to replace every illustrative cost figure in Section 4 with a measured
  series before any cost model is finalized — none of the specific cost numbers in this dossier
  should be treated as backtest-ready.
- **Every gold-related regime read (buying-regime state, crisis kicker) must be logged as an
  exogenous conditioning variable in the versioned config registry (contract Section 10) with its
  own provenance entry**, distinct from the fitted-parameter entries, so CI validation can enforce
  the reduce-risk-only Tier-C budget cap on the structural floor separately from the Tier-B tactical
  band weights.

---

## 7. Open questions and [VERIFY] items

1. Exact correlation coefficients and sub-sample windows in Erb & Harvey (2013) — not re-extracted
   from the source text this pass.
2. No specific citable paper found/recalled for the "post-2022 real-rate/gold breakdown" claim
   (finding #2) — treated as a well-documented market fact from commentary, not an academic source;
   recommend a targeted search once budget resets, including any Erb-Harvey follow-up commentary
   updating their own 2013 framework for the post-2022 period.
3. Exact page/volume for Chordia, Subrahmanyam & Tong (2014) — high recall confidence on the
   substance, not re-verified this session.
4. Illustrative crisis-episode return magnitudes (2008/2013/2020/2022, Section 2) — directionally
   confident from macro-historical recall, not recomputed from any price series this pass; must be
   rebuilt from free bhavcopy/WGC archives in the data phase before use in any parameter.
5. Exact July-2024 (and 2013) import-duty rates and effective dates — could not confirm this session;
   material because it changes how any INR-gold return series must be spliced.
6. Sovereign Gold Bond discontinuation — exact date, whether any tranche calendar remains active, and
   the official stated rationale — could not confirm this session. Practically moot given the
   contract already restricts gold to ETF/futures, but worth confirming for completeness and because
   it affects any argument about why ETF/futures became the load-bearing implementation channel.
7. Current Indian gold ETF expense ratios and measured tracking error by AMC — not verified this
   session; needs an AMFI/scheme-document pull.
8. MCX gold futures measured roll cost (bps/roll) and typical margin percentage — not verified this
   session; the "20–40bps" figure is market commentary, not a measured statistic.
9. SEBI's exact circular/rule set governing portfolio-manager access to commodity derivatives
   (reportedly opened ~2017) — not confirmed this session; relevant to whether/how the futures leg
   can be held directly.
10. Whether the central-bank buying regime can ever be promoted past Tier C given how slow-moving
    sovereign reserve-allocation behavior is — flagged as a structurally hard research question
    (may take a decade to accumulate a second independent regime observation), not resolvable by
    more data alone in the near term.
11. No India-specific academic paper was recalled with confidence that directly tests gold's
    safe-haven property against the Nifty (as opposed to BRIC-aggregate tests in Baur-McDermott) —
    flagged as a literature gap; recommend a targeted search once budget resets rather than assuming
    one doesn't exist.
12. **Process flag for the orchestrator**: this entire dossier was produced with the session's web
    search budget already exhausted and WebFetch blocked for every domain attempted. Recommend a
    dedicated verification pass over this dossier's citation list once search capacity is available,
    before any parameter here is promoted from a proposal to a frozen registry entry.
