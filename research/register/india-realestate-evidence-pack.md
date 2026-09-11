# THE INDIA REAL-ESTATE EVIDENCE PACK
### Sources, literature and country patterns — the head start for the prediction-engine thread

**Written 2026-09-11 · The Cycle Program · principal gaurav@ionic.in · governed by
`research/CONTRACT.md` · ledger entry `RE-SOURCES` (zero run cells, census unchanged at 1,399)**

**What this is.** The companion to `research/register/handoff-prompt-india-realestate-engine.md`
(v3.1). The handoff prompt says *what to build and in what order*. This says **what is already
known** — the international forecasting literature and its honest failures, the country-by-country
data regimes and the four templates India could copy, the India source estate portal by portal, the
under-reporting econometrics, and the free geospatial stack. Read this first and you start at the
research frontier; skip it and you will spend a fortnight rediscovering that the 18-year property
cycle fails its own test and that Zillow lost money buying houses with its own model.

**What this is not.** Not a roadmap, not a plan, not a task list — those live in the handoff prompt
and in `research/frontier/india-property-plan.md`. Nothing here is a commitment to build anything.

---

## §0 — THE EVIDENCE STANDARD, AND HOW TO READ THE TAGS

**Binding, and identical to the standard the CN programme published under.** `WebFetch` is
EGRESS-BLOCKED for every domain in the environment this pack was assembled in. Only `WebSearch`
worked. **Every external claim in §§1-4 therefore rests on search-result snippets that could not be
checked against a primary page.** Thirty agents produced it: 22 wrote cited dossiers, 3 attacked
those dossiers adversarially, 4 synthesised, 1 asked what was missing.

| Tag | Means | How to treat it |
|---|---|---|
| `[DESK PRINT]` | Computed by this desk from a vaulted dataset, pre-registered, desk-verified. Carries a ledger entry ID. | **The only evidence-grade material in this document.** Citable as a print. |
| `[2-SOURCE]` | Two independent search results agreed. | Good enough to design on. Verify before publishing a number. |
| `[1-SOURCE]` | One source. | Treat as a lead, not a fact. |
| `[RECALL — unverified]` | From a model's memory; search did **not** confirm it. | **Assume it may not exist.** Chase it or drop it. Never cite it. |

**The pack carries its own corrections.** §6 is the audit scoreboard: claims the fact-checkers
refuted or downgraded, left visible rather than silently edited out, per the preservation rule.
Anything the auditors refuted has been removed from §§1-4 or corrected in place — but it stays
listed in §6 so a reader can see what the first draft got wrong.

**One structural warning about a pack like this.** The highest-probability error is not a wrong
number, it is a **citation that does not exist** — a plausible author-year-journal triple invented
by a language model and then repeated with confidence. That is why a third of the agent budget here
went to adversarial citation checking before a word of synthesis was written, and why §6 exists.

---

## §0.1 — CONTENTS, AND THE ONE FINDING THAT CHANGES THE DESIGN

| § | Section | Grade |
|---|---|---|
| §00 | What this desk already knows about property — sixteen prints | **desk** |
| §1 | The international evidence: what is known about predicting house prices | snippet |
| §2 | Country patterns, and what happens when a country forces disclosure | snippet |
| §3 | The India source estate and the India literature | snippet |
| §4 | Method: how to build and how to judge | snippet |
| §5 | Reachability, measured rather than assumed | **measured** |
| §6 | The audit scoreboard, and the verification queue | **audit** |
| §7 | What was never swept, and the three ways this fails | **critique** |
| §8 | The fifteen things to read first | — |
| §9 | How this pack connects to the handoff prompt | — |

**If you read one paragraph of this document, read this one.** The handoff prompt's intellectual
core is a censored regression: registered price = max(true price, circle rate), with the circle rate
as an observed, time-varying, ward-level censoring threshold. **The audit refuted that as a
mechanical identity.** Stamp duty is charged on the *higher of* declared price or circle rate, which
constrains the **tax base**, not the **declared consideration** — so nothing mechanically stops a
deed recording below the floor, because duty is identical either way. What makes the floor bind is
the income-tax deeming machinery (Sections 50C / 43CA / 56(2)(x)) and its 5-10-20% tolerance band,
which is an *incentive*, not a censoring rule. The pile-up at the circle rate is therefore a
**behavioural equilibrium**, and a plain Tobit likelihood assigns zero probability to any observation
below the floor — misspecified before any distributional question, if such rows exist. **The
day-one diagnostic is one number: the share of registered declarations strictly below the local
circle rate.** If it is non-trivial, the correct model is the bunching/notch family, not Tobit. That
is a better model, reachable with the same data, and §§4 and 6 say how. Full statement in §6.2 #1.

## §00 — WHAT THIS DESK ALREADY KNOWS ABOUT PROPERTY

**Read this section before the literature.** The desk has been working on property since the atlas
phase. Four on-desk documents outrank everything in §§1-4 because they are desk-grade rather than
snippet-grade, and one of them has already done most of the India data engineering.

### The documents of record, in reading order

1. **`research/cycles/fincycle-deep/partC-data.md`** (460 lines) — *"Data engineering: measuring
   India's property cycle, free."* **This is the single most valuable file in the repo for the new
   thread and it already exists.** It covers: RBI HPI provenance and the 2022-23/18-city rebase
   break sitting inside it now; NHB RESIDEX's two dated breaks and its **two structurally different
   price concepts** (an assessment-price leg that is a lender's number and a market-price leg that
   is not, which must never be blended with RBI HPI into one series); bank-plus-HFC housing credit;
   RERA and the supply side; registration counts and stamp duty as the transaction-side series; the
   circle-rate honesty note; a **vintage/point-in-time hazard table**; the L12 India pipeline; and
   §C.9, an explicit list of what cannot be measured free. Do not re-derive any of this.
2. **`docs/cycles/13-real-estate.md`** — the real-estate-cycle merge monograph. Kills the folk clock
   (see below), keeps the mechanism.
3. **`docs/cycles/12-financial-cycle.md`** (seat L12) — the credit-property cycle, seated, with the
   India degradation path designed and tested for a short HPI.
4. **`docs/learn/artifacts/india-property-atlas.html`** (README row 65) and
   **`china-property-crash-atlas.html`** (row 64), with their plans in `research/frontier/` and
   their dossiers in `research/notes/india-dossiers/` and `china-dossiers/`.

### The prints any new property work must not contradict or rediscover

Every row is `[DESK PRINT]` with its ledger entry. These are the desk's own numbers, computed from
vaulted data and desk-verified on a second code path.

| # | Print | Entry |
|---|---|---|
| 1 | **The 18-year property cycle FAILS its own pre-registered test.** 109 real house-price peak spacings across 17 JST countries: median **14y**, IQR 10-17y, full range 8-45y, and only **45%** land in the pre-declared [14,22]y window against a ≥50% bar — on a construction deliberately biased *toward* the claim. Kuznets 15-25y building swings fail cleanly too (investment/GDP spacings median 11y, 25% in-window). The slowness is real; the *clock* is not. | RE1, RE2 |
| 2 | **Credit-property amplification is the cleanest sign-consistency pass in the whole project** — 17/17 countries, median correlation **+0.40**. Cycle length lengthened 11y→13y post-1985. But crisis-at-peak *dating* is weak on a real-time construction (1.2-1.3x), which is the seat's own evidence for **states, never dates**. | FC1-FC3 |
| 3 | **A sustained 20%/yr real property boom has never happened in the modern era of the JST panel.** Post-1970: **0.00% of 884** five-year windows cleared 20%/yr real; 0.45% cleared 15%/yr. The post-1970 panel maximum is **Ireland 1999 at +17.25%/yr real** — and Ireland 2006 is the worst modern bust in the episode list at **-55.7%**. The fastest modern boom and the worst modern bust are the same country, seven years apart. | IN-D1 |
| 4 | **Hot markets stay hot at five years, which refuted the desk's own mean-reversion prior.** Next-5y real return after a ≥15%/yr real window: **+9.65%/yr**; after ≥20%/yr: **+11.16%/yr**. Those same windows carry roughly **2x** crash odds (2.02x at ≥10, 2.03x at ≥20; the ≥15 rung prints 1.03x on 45 windows and is recorded as a miss, not smoothed). Consumption: **ride-it-but-size-it, never in-or-out.** | IN-D1 |
| 5 | **Indian nominal property talk is mostly real, not money illusion** — the opposite of the registered prior. On hyperinflation-clean windows, 20%/yr nominal has typically meant about **+12%/yr real** (mean real +12.42 vs nominal +23.17%/yr; inflation supplied 46% of the headline; only **2.3%** of hot nominal windows were real-negative). | IN-D2 |
| 6 | **The base rate for a property crash: median -34.2% real over 6.5 years** across 48 episodes, 18 countries, 1870-2020; modern era **-32.0% over 5.5y**. | CN-D1 |
| 7 | **Busts are NOT slower than booms** — the registered "gentle deflation" bar missed. Velocity ratio **1.12x** full sample, **0.99x** modern. There is no slow-deflation discount. | CN-D1 |
| 8 | **A bigger boom buys SPEED, not depth.** Depth gap only **3.8pp** between big and small booms, but the unwind runs **3.5pp/yr faster**. So the *exit plan* matters more than the entry level. | CN-D4 |
| 9 | **Rental yield is the placement instrument.** It compresses **-0.83pp** into the peak and expands **+1.53pp** to the trough — which is how the desk placed tier-1 China at roughly a third of a crash when the price index alone was ambiguous. | CN-D2 |
| 10 | **The best-known credit early-warning indicator has an 87.2% false-alarm rate.** Mortgage-credit growth lifts 3-year crash odds **1.72x** — and cries wolf 87.2% of the time. Public-debt growth reads *backwards* (0.23x; it rises *after* busts). Anyone selling you a property-crash predictor is selling you this. | CN-D3 |
| 11 | **Equities lose -13.7pp excess real in the first year of a housing bust**, double if banks break, and are recovered by year five — reproducing CI-D5 on a different construction. Property busts are an equity-book event, not only a property-book event. | CN-D5, CI-D5 |
| 12 | **In the high-and-rising-inflation state, housing is the second-best asset and equities are the worst**: gold **+9.6** > housing **+6.8** >> equity **-3.0** > bonds **-5.6** (%/yr real). This is the one macro state where an Indian property overweight has desk support. | CI-D2 |
| 13 | **Announcement moves the price; completion merely confirms it.** Panvel **+76%** since 2021, mostly *before* the first flight at Navi Mumbai; the Jewar belt **+142-158%/5y**, mostly before flying; Delhi-Dehradun Expressway **+23% in the nine months before opening**; Samruddhi corridor land ≈**3.7x** pre-completion. Completed MMR infrastructure then yields only a smaller continuing **8-15%/yr** premium. **Corollary: every public, dated feature is already partly in the price.** | IN dossiers |
| 14 | **Every listed Indian REIT yields below the 10-year G-sec, and no residential REIT exists in India at all.** India's property carry is *more* negative than China's was at its peak. | IN dossiers |
| 15 | **The cost drag is the whole game.** Entry ~9% (stamp duty 5-7%, registration ~1%, brokerage 1-2%, diligence), exit ~1.5%, round trip **~10.5%**, holding ~2.2%/yr → **~21.5% over five years**. So: a locality doing 20% cumulative over five years nets **-0.30%/yr nominal, -4.60%/yr real**; break-even needs **21.5% gross**; matching the desk's own standing book (+11.46% CAGR) needs **93.5% gross**. Every forward distribution this project publishes must be shown **gross and net**. | handoff §1 |
| 16 | **Point forecasts are forbidden, and the desk's own results say why.** The ER-arc pooled expected-return equations failed out-of-sample at every horizon once purged and honestly benchmarked; single-country kitchen sinks exploded at **-389%**; Goyal-Welch binds fully. | ER-D4b, ER-D7 |

**How prints 3, 4 and 15 fit together, because together they are the project's actual thesis.** A
20%/yr five-year Indian property call is a *bubble-velocity* call, not a growth forecast — it has
never happened in the modern panel in real terms. A hot micro-market should nonetheless not be
dismissed on mean-reversion grounds, because at five years the base rate says it keeps running, at
roughly double the crash odds. And whatever it returns, the investor keeps it only after a ~21.5%
five-year cost wedge. **"Will prices rise?" is the wrong question. "Will prices rise enough to beat
21.5% plus the alternative?" is the question, and it has a much smaller yes-set.**


---

## THE INTERNATIONAL EVIDENCE: WHAT IS KNOWN ABOUT PREDICTING HOUSE PRICES

House prices are forecastable at one to four quarters and essentially not forecastable beyond that. That is the record. The mechanisms are well identified — extrapolation, a valuation anchor, credit supply, supply elasticity, speculative microstructure — but identifying a mechanism is not a forecast, and this literature's out-of-sample tests stop where an investment horizon begins. Its most expensive failure was not theoretical: it was a model with good average validated error committing capital to a narrow forward slice.

**Tag convention, and it binds everything below.** `_AUDIT-1` established that **not one of the roughly 120 external citations in dossiers A1–A6 was checked against a primary source** — WebFetch is egress-blocked and the session's WebSearch budget was exhausted before the audit ran. Its ruling: the honest ceiling for this pack is `[1-SOURCE]`, with `[2-SOURCE]` reserved for claims corroborated by the desk's own ledger and atlases. Tags below are stated at that audit-corrected level, not the level the dossiers claimed. `[RECALL — unverified]` means model memory with zero retrieval; all of §3 is in that class by its own disclosure, which the audit endorsed as exemplary rather than discounted.

### 1. THE PREDICTABILITY RECORD BY HORIZON

**Every genuinely out-of-sample house-price forecast evaluation retrieved sits at one to four quarters, and no retrieved study demonstrates a real-time expanding-window beat of a random walk at three, five or ten years.** The audit confirmed this absence as the best-constructed conclusion in the pack (C-10). Report the absence as the finding.

| Horizon | Beats a random walk? | Best evidence | Quality |
|---|---|---|---|
| 1–2 quarters | **Yes.** ML and time-series models beat a random-walk-with-drift on Australia's real HPI | Milunovich (2020), *J. Forecasting* 39(7) | [1-SOURCE] |
| 1–4 quarters | **Yes.** BVARs best-performing in **19 of 20** US states; signalled the coming downturn in **18 of 19**. Estimated 1976Q1–1994Q4, evaluated 1995Q1–2006Q4 | Gupta & Das (2010), *JREFE* 41(3) | [1-SOURCE] |
| 1–4 quarters | **Yes.** Dynamic factor models beat VARs in most cases, five South African metros, 282 series, 1980Q1–2006Q4 — the only EM out-of-sample evaluation retrieved | Das, Gupta & Kabundi (2011) | [1-SOURCE] |
| 1–4 quarters | **Yes, conditionally.** Letting predictor set *and* coefficients vary over time beats equal-weighted combination across 50 US states; the most volatile states need the most model change | Bork & Møller (2015), *IJF* 31(1) | [1-SOURCE] |
| 1–4 quarters, **India** | **Yes, short-term only.** U-MIDAS on digital-payment value, CPI and a financial-stress index beats ARIMAX against quarterly RBI HPI, Oct 2019–Sep 2024 | Singh & Shanmugam (2026), *PLOS ONE* | [1-SOURCE]; a 2026 paper, unverifiable here by construction |
| 4–8 quarters | **No.** Outperformance is no longer statistically significant — the cleanest horizon-decay result retrieved | Milunovich (2020) | [1-SOURCE] |
| 3 years | **Not tested OOS.** In-sample, the rent-price ratio predicts real rent and price changes over 12 quarters — with bootstrap distributions, because the regression is biased when price has a unit root but is not an exact random walk | Gallin (2008), *REE* 36(4) | [1-SOURCE], in-sample only |
| 5 years | **Not tested OOS anywhere retrieved.** Theory *calibrates* reversion near this horizon; that is calibration, not a forecast beat | Glaeser & Nathanson (2017) | [1-SOURCE]; §1.1 — first-party evidence points the other way |
| 10 years | **Not tested.** Nothing retrieved attempts it | — | — |
| Nonlinear, any horizon | **No.** Regime-switching is detectable in-sample for regional growth; out-of-sample "the evidence in favor of nonlinear models was virtually non-existent" | Balcilar et al., secondary description only | [RECALL — unverified] |

Two caveats bind even the short end. **Predictability is time-varying**: Rapach & Strauss (2009), on the 20 largest US states over 1995Q1–2006Q4, conclude it is "difficult to choose *a priori* a consistently effective predictor set," and find **coastal states systematically harder to forecast than interior states** [1-SOURCE] — the forecastability mirror of §2.4. **And index-level significance does not survive to the unit level**: Case & Shiller (1989), on 39,210 repeat-sold homes in four US metros 1970–1986, found annual real city-index changes positively autocorrelated at roughly one-quarter to one-half the prior year's magnitude and the market not weak-form efficient, while reporting individual-home R² **never above 0.04** [1-SOURCE via one HUD review; the audit downgraded this and instructed it stop being called the pack's single most important caveat on one secondary document]. It remains a real warning for any per-property engine.

#### 1.1 The momentum-versus-mean-reversion crossover, and where the desk's own evidence overrides it

The literature's canonical crossover is **momentum at roughly one year, mean reversion at roughly five**, plus excess long-run volatility — all three generated jointly by Glaeser & Nathanson's (2017) extrapolative model, in which buyers read past prices as if they reflected only contemporaneous demand [1-SOURCE]. Guren (2018) sits between the anchors: positive autocorrelation persisting **two to three years** post-shock, **median US city annual AR(1) near 0.60** [1-SOURCE; the audit flagged conflicting tags across dossiers and a page range duplicating Head-Lloyd-Ellis-Sun's start page — verify both]. Cutler, Poterba & Summers (1991) is the cross-asset version: high-frequency positive serial correlation, long-horizon negative serial correlation, predictive power in deviations from fundamental-value proxies [1-SOURCE] — **but no real-estate-specific reversal horizon from that paper was retrievable, so any housing reversal horizon attributed to it is [RECALL — unverified].**

**The five-year reversal limb of that consensus is refuted by the best evidence this desk owns.** Pre-registered entry **IN-D1** (2026-09-11, desk-verified exact on a second code path) ran 1,934 overlapping five-year windows across 18 countries and ~150 years of the JST panel.

| Trailing 5y real appreciation | Window frequency | Countries | **Next-5y real return** | Crash-odds lift |
|---|---|---|---|---|
| ≥5%/yr | 20.94% | 18 | +2.06%/yr | 1.77x |
| ≥10%/yr | 5.12% | 14 | +5.05%/yr | 2.02x |
| ≥15%/yr | 2.33% | 7 | **+9.65%/yr** | 1.03x |
| ≥20%/yr | 0.98% | 3 | **+11.16%/yr** | 2.03x |
| Unconditional | — | 18 | — | P(≥20% crash peak begins within 5y) = **13.0%** |

Hot property markets stayed hot. The registered prior was mean reversion; it **MISSED**, and the miss is recorded rather than the bar moved. The 2.0x crash bar also **MISSED at the ≥15% rung** (1.03x), non-monotonically — 2.02x and 2.03x bracket it on 45 and 19 windows across 7 and 3 countries — so the honest reading is **roughly 2x crash odds at high appreciation with the named rung failing on small-sample noise**, not rounded into a pass. Registered limits stand: JST is 18 advanced economies, no India, nothing at India's income or urbanisation stage; windows overlap, so frequencies are exposure shares and no p-value is claimed; these are national indices, and the CN programme established that city dispersion exceeds national dispersion (Wenzhou −63%, Hainan ≈−87%), making these frequencies a **floor** on city-level extremes, not a cap. Post-1970, **0.00% of 884 windows** cleared 20%/yr real and only **0.45%** cleared 15%/yr; the post-1970 maximum is **Ireland 1999 at +17.25%/yr real, and Ireland 2006 is the worst modern bust at −55.7%** — fastest modern boom and worst modern bust, same country, seven years apart. The longest run is **Japan, 15 consecutive years** above 15%/yr trailing real, the episode CN-D1 booked as **−47.3% over 18 years**. [2-SOURCE — first-party, trial ledger IN-D1; `docs/learn/README.md` row 65; C-02]

**The operative correction (`_AUDIT-1` R13): a price-reversal overlay at five years is not supported by the best evidence this desk owns, and A1's recommendation of one is dropped.** What rises with trailing appreciation is **crash probability, not an expected negative return**. Consumption is ride-it-but-size-it: treat high trailing appreciation as a state lifting tail probability from a 13.0% base toward roughly 26%. Under CLAUDE.md rule 6, first-party prints outrank snippet-grade calibration.

### 2. THE FIVE MECHANISM FAMILIES

#### 2.1 Momentum and extrapolation

**The mechanism is now measured in beliefs, not only prices.** Ma (2020) is the cleanest cross-check: household subjective expectations **capture the momentum component but not the reversion-to-fundamentals component** [1-SOURCE] — the belief structure Glaeser-Nathanson assume. Case, Shiller & Thompson, surveying four US metros in 1988 and annually from 2003, find **one-year expectations if anything underreact** while **ten-year expectations reached extremes relative to mortgage rates right at the 2000s peak** [1-SOURCE]. Piazzesi & Schneider (2009) reconcile them: Michigan Survey cluster analysis isolates a **small cluster who buy specifically because prices will rise further**, whose share **roughly doubled toward the end of the boom**, and in their search model a small minority moves aggregate prices because the *marginal*, not average, buyer sets price under search frictions [1-SOURCE].

| Mechanism | Effect size | Study | Quality |
|---|---|---|---|
| City-index autocorrelation | Next-year change same direction, ¼–½ the magnitude | Case & Shiller (1989) | [1-SOURCE] |
| Annual AR(1), median US city | **≈0.60**, persisting 2–3 years post-shock | Guren (2018), *JPE* 126(3) | [1-SOURCE] |
| Strategic complementarity | **2–3x** amplification of search-friction momentum, via a concave demand curve (pricing above average sharply cuts sale probability; below barely helps) | Guren (2018) | [1-SOURCE] |
| Search/liquidity channel, distinct from price-setting | "Substantial quantitative improvement" over a no-search benchmark, 106 US cities | Head, Lloyd-Ellis & Sun (2014), *AER* 104(4) | [1-SOURCE]; magnitude of "substantial" [RECALL — unverified] |
| Social-network contagion | A **5pp** larger friend-experienced gain over 24 months → **+3.1pp** renter-to-owner probability, **1.7%** larger house, **3.3%** more paid | Bailey, Cao, Kuchler & Stroebel (2018), *JPE* 126(6) | [1-SOURCE]; the "7% larger down payment" limb downgraded separately (D-22) |

**Correction (R4):** A5 merged NBER WP 12810, Piazzesi & Schneider's "Inflation Illusion, Credit, and Asset Prices," with "Money Illusion and Housing Frenzies" as alternate titles of one paper. They are two papers by different authors — the latter is **Brunnermeier & Julliard**, *RFS* 21(1), 2008 — making a *different* claim (falling inflation drives the frenzy) rather than the symmetric both-tails prediction attributed to the merged cite. Split both and re-derive which supports which. The desk holds a first-party print here: **IN-D2** found JST nominal property gains are mostly real, not money illusion — excluding windows touching any year with CPI above 50%, ≥20%/yr nominal windows delivered **+8.38%/yr** next-5y real, inflation supplied **46%** of the headline, and only **2.3%** were real-negative. **20%/yr nominal has typically meant roughly 12%/yr real**, which strengthens the informational content of Indian nominal price talk [2-SOURCE — first-party].

#### 2.2 The valuation anchor

**The folk anchor fails a formal test.** Gallin (2006), on 95 US metros over 23 years with bootstrap-corrected panel cointegration, **fails to reject no-cointegration between house prices and income** [1-SOURCE]. What carries signal is the rent-price ratio, at long horizons and in-sample only.

**The user-cost framework's own disconfirming episode goes first.** Himmelberg, Mayer & Sinai (2005), applying UC = (1−τ)(i+p) + d + risk premium − expected appreciation to 46 US metros over 1980–2004, concluded owning had grown dearer relative to renting but **in most metros not to overvalued levels**; US prices then fell more than 30% into 2008–2012 [1-SOURCE; the attribution of that framing to a Fed retrospective is [RECALL] and unnecessary to the critique, D-14]. The mechanism of the miss is the model's own: Verbrugge (2008) shows rents and ex-ante user costs diverge markedly for years in the five largest US cities, and that **divergence size is extremely sensitive to the appreciation proxy** — a forecast of actual future appreciation produces large divergence, while substituting expected CPI inflation collapses most of it [1-SOURCE]. Rising prices mechanically lower measured user cost.

| Finding | Magnitude | Study | Quality |
|---|---|---|---|
| Prices and income not cointegrated | Fails to reject no-cointegration, 95 metros / 23 years | Gallin (2006), *REE* 34(3) | [1-SOURCE] |
| What moves the rent-price ratio | Expected rent growth explains a small share; real rates and a time-varying housing premium explain most. **65%** of the 1997–2007 decline attributed to a falling premium; a 1997 regime break turned the rates/premium correlation from offsetting to compounding | Campbell, Davis, Gallin & Martin (2009), *JUE* 66(2), 23 metros | [1-SOURCE]; audit instructed the 65% not be headlined (D-12) |
| How much of the boom is explainable | Rates, lending standards and incomes explain **roughly half** the 1995–2006 price-rent rise | Sommer, Sullivan & Verbrugge (2013) | [1-SOURCE] |
| Correction channel and duration | Runs through **prices, not rents**, and "can take decades" | Ambrose, Eichholtz & Lindenthal (2013) — Amsterdam, **355** years | [1-SOURCE] |
| Half-life of deviations | **No reliable number exists.** Reversion speed varies with city size, income and population growth, and construction costs | Capozza, Hendershott, Mack & Mayer (2002/2004), 62 metros | [1-SOURCE]; a "3–6 year median-metro half-life" is [RECALL — unverified] and must not be cited |
| Cap rates and returns, commercial | Forecast up to **~30%** of realised-return variance for apartments, retail and industrial — **but not offices**; much of the cap rate is orthogonal to local fundamentals | Plazzi, Torous & Valkanov (2010), *RFS* 23(9) | [1-SOURCE]; the pack carries **no title** for this citation and one must be added (D-15) |
| Within-city dispersion | The ratio differs systematically by unit size and neighbourhood inside one city | Bracke (2015), Central London | [1-SOURCE] |

How far compression can run without resolving: Shanghai community ratios printed **78–79 raw in 2016Q4/2017Q1**, over **90% of communities at 50–80 in 2018** — gross yields of roughly **1.25–2.0%** [1-SOURCE; conversions check exactly, C-05]; Prime London ran prices **+180% since 2005 against rents +40%**, halving yields to **3–4%** [1-SOURCE, C-06]. The sharper instrument is first-party: the CN programme printed **median peak gross yield 3.29%**, busts **ending near 5.2%**, yield **compressing −0.83pp into the peak and expanding +1.53pp to the trough**, and China tier-1's 2021 peak yield of ~1.7–1.8% as the **second-lowest peak yield in 150 years** behind only Spain 2007 at 1.49%, which then fell 42.9% [2-SOURCE — first-party, row 64]. An "~8% equilibrium gross yield" for Ireland 2006, carried in A2, is implausible against that record, was downgraded to [RECALL — unverified] and is marked not-to-be-repeated (D-13).

#### 2.3 Credit

**Credit is what makes a housing bubble dangerous, and it is the family with the best instruments and the worst precision as a timing device.** Jordà, Schularick & Taylor's "Leveraged Bubbles" (17 countries, 140 years) found an equity bubble *without* a credit boom has "virtually no effect" on recession depth or recovery, while one *with* a credit boom adds **one extra year** of recession and about **3 percentage points** of cumulative GDP-per-capita drag at five years; adding credit growth to a crisis-classification baseline raised AUC from **0.61 to 0.71** [1-SOURCE]. **No credit-fuelled-*housing*-bubble-specific depth figure was retrieved** — [RECALL — unverified], the highest-priority chase in this family. Schularick & Taylor (2012) report a baseline **AUROC 0.717** [1-SOURCE]; the audit warns these are plausibly the same statistic and must not be presented as independent corroboration (D-08).

| Channel | Effect size | Study | Quality |
|---|---|---|---|
| Home-equity extraction | **25–30 cents per dollar** of equity gain extracted; **$1.25tn** added to household debt 2002–08; explains **≥39%** of new defaults 2006–08 | Mian & Sufi (2011), *AER* 101(5) | [1-SOURCE] |
| Credit supply → prices | Price-to-loan-volume elasticity **0.134** over one year; "explains up to one half" of 1994–2005 price growth; smaller where supply is elastic | Favara & Imbs (2015), *AER* 105(3) | Mechanism [1-SOURCE]; **both magnitudes [RECALL — unverified]** — they came via a secondary citation, never the paper (D-05) |
| Credit supply → prices, 2nd instrument | **11%** rise in annual lending → **3.3%** rise in annual price growth, **2.2%** nontradable-employment expansion, reversing after; the same expansion **cut delinquencies in the boom and raised them in the bust** | Di Maggio & Kermani (2017) | [1-SOURCE] |
| Which constraint binds | **PTI/DTI (cash flow), not LTV (collateral)** — they move in opposite directions on a rate shock. PTI rate-elasticity **~8**; PTI liberalisation alone explains **42%** of the US price-rent rise and **51%** of the debt/income rise | Greenwald, MIT job-market paper | [1-SOURCE]; no published venue anywhere in the pack (D-06) |
| Does credit reach price | Yes, via rental-market segmentation: the price-rent ratio responds **≥4x more** than homeownership to an identified credit shock; credit standards explain **34–55%** of the 2000s price-rent rise | Greenwald & Guren, NBER WP 29391 | Magnitude [1-SOURCE]; the *AER* Oct-2025 placement is [RECALL] (D-04) |
| Speculation as transmission | PLS-exposed zip codes saw volume surges driven almost entirely by flippers — **under 1% of the adult population** in 2005–06; the credit shift appears even in the most elastic MSAs but is stronger where supply is inelastic, so **elasticity moderates, it does not trigger** | Mian & Sufi, "Credit Supply and Housing Speculation," *RFS* 35(2), 2022 | [1-SOURCE]. **The pack's "Mian, Sufi & Matvos" is a likely fabricated third author (R3); Matvos is dropped here and authorship must be verified before republication** |
| Housing wealth → consumption | Elasticity to housing net worth **0.6–0.8**; MPC **5–7 cents per dollar**, higher in poorer, more-levered zips | Mian, Rao & Sufi (2013) | [1-SOURCE] |

The macroprudential record is candid about its own failures, and that is the part an India engine should read. Kuttner & Shim (57 economies, 30+ years, nine tools) find housing-*credit* growth responds to several tools in conventional panels but under stricter mean-group and event-study methods **only DSTI limits survive**; on house *prices*, **only transaction-tax changes** are robust; DSTI tightening decelerates credit growth **4–7pp** over the following year [1-SOURCE]. Cerutti, Claessens & Laeven (119 countries, 2000–13) associate LTV/DTI caps with **~1.5pp** lower household credit growth and **~1.2pp** lower real price growth, partly offset by cross-border leakage [1-SOURCE]. Country experiments repeat the collateral-versus-cash-flow split: **Sweden's 2010 LTV cap alone had no measurable price effect while the 2016 amortisation rule is associated with roughly −7%**; **New Zealand's 2013 LVR restrictions carried an RBNZ expectation of 1–2pp lower price inflation and the 2021 reintroduction had "little impact"**; Israel's 2010 risk-weight measure moved affected-unit prices about **−2.5pp**; Canada's B-20 stress test mechanically cuts the maximum qualifying mortgage **~20–25%**; Hong Kong LTV caps are followed by declining high-end volume growth after about **one year** and total volume growth after **1.5–2 years** — volume moves before price, separably [1-SOURCE each].

India's only directly-applicable credit numbers are **Bhupal Singh, IMF WP/20/291 (2020)**, on NHB RESIDEX city data: LTV, risk weights and provisioning all detectably dampen city prices, and the **LTV effect is size-differentiated — elasticity 0.40–0.59 small-ticket versus 1.10–1.14 large-ticket**, making India's LTV lever disproportionately a premium-segment tool [**[1-SOURCE]** — re-tagged from 2-SOURCE because the "two independent sources" were two hosting mirrors of one manuscript, R12/D-02]. Context: India mortgage-to-GDP has risen from ~3.4% (2001) to roughly **11–12.5% (FY24/25)** against US ~51–76% and China ~28% [1-SOURCE trend; every household-leverage *point* estimate in the pack, including the 45.5%-of-GDP Sep-2025 print and the 28.6% housing composition share, was downgraded to [RECALL — unverified] as forward-dated snippet-channel figures, D-09]. **The pack's statement of India's own LTV/risk-weight schedule is internally contradictory and cannot be coded from** — it caps 90% LTV at loans ≤₹20 lakh while defining a 50% risk weight for the 80–90% LTV band on loans ≤₹30 lakh (R11).

The honest calibration of credit as an early-warning instrument is the desk's own: **mortgage-credit growth lifts three-year crash odds 1.72x with an 87.2% false-alarm rate**, while public-debt growth reads backwards at 0.23x — it rises *after* busts [2-SOURCE — first-party, row 64]. That is consistent with the BIS convention, which by design minimises noise-to-signal **subject to catching at least two-thirds of crises**; reference thresholds are a credit-to-GDP gap of **2–6pp** and a real property-price gap of **15–25%**, with the debt-service ratio dominating short horizons and the credit gap long ones [1-SOURCE]. The exact noise-to-signal figure comparable to 87.2% was not retrievable; publish no numeric comparison.

#### 2.4 Supply elasticity

**Elasticity is why identical demand shocks produce different price paths, and the field's best-known amplitude figure is Glaeser, Gyourko & Saiz (2008): mean price growth in the 1980s US boom was 29% in the most inelastic metros against 3.4% in the most elastic, with elastic-city booms short when they occur** [1-SOURCE]. The same paper carries the correction that stops "inelastic = bad" from being the read: **the welfare cost of a bubble can be larger in elastic cities, because they overbuild more** — low price amplitude substitutes vacancy and capital-stock risk for price risk rather than removing risk [1-SOURCE].

| Finding | Magnitude | Study | Quality |
|---|---|---|---|
| Boom amplitude by elasticity | **29%** (most inelastic) vs **3.4%** (most elastic), 1980s US | Glaeser, Gyourko & Saiz (2008), *JUE* 64(2) | [1-SOURCE] |
| Measuring elasticity geographically | Land-unavailability index from satellite terrain/water within 50km of **269** US metro centres; elasticity is jointly geographic and regulatory and the two are endogenous. San Francisco **≈0.66** | Saiz (2010), *QJE* 125(3) | [1-SOURCE]; per-metro Houston/Dallas/Atlanta figures are [RECALL] (D-23) |
| Elasticity conditions the crossover | Serial correlation **higher** where income growth, population growth and real construction costs are higher; reversion **faster** in large, faster-growing, lower-cost metros. High correlation plus low reversion produces overshoot (Boston, NY, SF, LA, San Diego) | Capozza, Hendershott, Mack & Mayer (2002/2004) | [1-SOURCE] |
| Regulation beats topography | Regulatory constraint substantively raises the price/earnings elasticity; land-scarcity effects confined to highly urbanised areas. South East England prices ~**25%** lower in 2008, ~**30%** lower by 2015 under North East rules | Hilber & Vermeulen (2016), 353 English planning authorities, 1974–2008 | [1-SOURCE] |
| Where elasticity actually varies | Tract-level floor-space **≈0.5**, units **≈0.3**, with **within-metro variation exceeding between-metro**; new construction is only ~50% of the unit-supply response | Baum-Snow & Han (2024), *JPE* | [1-SOURCE] (re-tagged, R12) |
| The regulatory tax, concretely | Manhattan prices at **more than twice physical construction cost**, attributed to a "zoning tax" | Glaeser, Gyourko & Saks (2003/2005) | [1-SOURCE] |
| Supply-side speculation inverts the safety read | Land speculation is easier than housing speculation (no rental-yield drag on raw land), so it amplifies booms **most in cities with intermediate or ample undeveloped land** — the ones the base model calls safe | Nathanson & Zwick, "Arrested Development" | [1-SOURCE]; the pack cites a conference PDF with a malformed URL, understating the standing (likely *J. Finance* 73(6), 2018 — [RECALL]). The brief's "Buchler" matched no paper (R16) |
| Macro cost of constraint | Constraints in high-productivity cities lowered aggregate US GDP **growth** by **36%**, 1964–2009 | Hsieh & Moretti (2015/2019), 220 metros | [1-SOURCE] on the growth effect. **The median-regulation counterfactual number must not be published: A4's ~2% matches neither 3.7% (*AEJ:Macro* 2019) nor 9.5% (2015 NBER WP)** (R5) |

**India's one causally-identified supply magnitude, and immediately after it the negative finding that qualifies it.** Nagpal & Gandhi, on a granular panel exploiting spatial and time variation in a Mumbai FAR relaxation, print **+17% FAR utilisation → +58% units supplied in treated areas → −24% prices in treated areas**, no average size change but smaller units where relaxation was greatest [**[1-SOURCE]** — re-tagged from 2-SOURCE because the three cited URLs are a landing page, an event page and the authors' own PDF for one unrefereed manuscript; D-03 notes −24% is a very large effect to anchor on from one working paper]. Against it: **Dutta, Gandhi & Green find the ULCRA repeal did *not* deliver the supply growth theory predicts**, because unresolved property-rights disputes over the frozen "surplus" parcels triggered fresh litigation that kept construction frozen, diff-in-diff across 200+ cities [1-SOURCE]. **Deregulation therefore splits into two non-interchangeable categories: raising a floor-space cap on clean-titled plots (worked) versus releasing legally-encumbered land (largely did not).** Compounding both, Gandhi, Tandel, Tabarrok & Ravi, across ~3,000 Mumbai projects, find **27.3% of projects and 42.9% of built-up space under litigation, average construction 8.5 years, litigated projects ~20% slower, and delay raising total cost by ≥30%** [1-SOURCE]. Mumbai's effective elasticity is lower than its nominal FSI implies, and that gap is close to unmeasurable from FSI data alone. The pack's FSI comparator table (Manhattan ≈15, Tokyo ≈20, Singapore ≈25; Mumbai island 1.33, Hyderabad uncapped at 6–7) is **[RECALL — unverified]** trade press that blends base, premium and TDR-loaded FSI inconsistently, so the Hyderabad-to-Mumbai city amplitude ranking built on it is a **hypothesis to pre-register, not a finding** (D-23); same for the Brueckner-Sridhar ₹106m welfare figure and "Mumbai ≈2.9 sqm per person" (D-24).

#### 2.5 Speculation and microstructure

**Sellers anchor on nominal purchase price, and it is the best-measured behavioural effect in housing.** Genesove & Mayer (2001), on 1990s downtown Boston condo sellers, find owners facing a nominal loss **set list prices 25–35% of the loss amount higher, realise 3–18% of the loss in higher final prices, and have a substantially lower hazard of sale** [1-SOURCE]. Their 1997 companion isolates the separate equity channel: **high-LTV sellers set higher asks, take longer, and get higher prices if they sell**, because the down-payment requirement faces purchasers, not incumbent owners [1-SOURCE]. Stein (1995) is the theory both test: a minimum down payment ties the ability to move to current equity, so a price shock that erodes equity mechanically cuts volume and the volume drop further depresses prices — a multiplier producing volatility beyond fundamentals and, in some parameterisations, multiple equilibria [1-SOURCE].

**The finding that limits all of it belongs here, not at the end.** Bokhari & Geltner (2011), extending loss aversion to US commercial property, find the effect **roughly the same order of magnitude** as residential, **larger and more experienced institutional investors showing equal or greater loss aversion**, the effect **strongest at the 2007 peak and "virtually ineffective" in the 2008–09 crash** — and **the aggregate market cycle only mildly affected** once the individual-level bias is aggregated [1-SOURCE]. A well-measured micro bias does not automatically become a macro forecasting signal.

| Finding | Magnitude | Study | Quality |
|---|---|---|---|
| Speculators vs middlemen | Middlemen buy low and sell high across the cycle; **speculators enter mostly in the boom, transact near market price on both legs, show no price-timing skill.** Speculative activity was strongly associated with subsequent bubbles at metro and neighbourhood level | Bayer, Geissler, Mangum & Roberts, *RFS* 33(11), 2020, LA 1988–2009 | [1-SOURCE] |
| Misinformed out-of-town buyers | Out-of-town second-home purchases predict future appreciation **and** future appreciation in the implied-to-actual rent ratio (a pure-mispricing proxy); worse exit timing than local second-home buyers | Chinco & Mayer (2016), *RFS* 29(2) | [1-SOURCE] |
| Speculation and bust severity | Cities with larger speculative booms had **larger price booms, sharper unsold-listing increases at the turn, and more severe busts**; predictable price increases disproportionately attract short-horizon buyers who amplify volume | DeFusco, Nathanson & Zwick, *JFE* 146(1), 2022, **50 million** US sales | [1-SOURCE] |
| Speculation into the real economy | Cross-state capital-gains-tax variation as instrument: more speculation → more appreciation, expansion and construction 2004–06, and **more severe downturns 2007–09** | Gao, Sockin & Xiong (2020) | [1-SOURCE] |
| Agency wedge in listings | Agent-owned homes sell for **~3.7% more** and sit **~9.5 days longer** than comparable client-owned homes | Levitt & Syverson (2008), *ReStat* 90(4) | [1-SOURCE]; one of the few exact numeric pairs the audit would let through (C-09) |
| Vacancy → time-on-market → price | Vacancy sets expected time-on-market, which sets both parties' reservation prices; higher vacancy → longer TOM → lower reservation prices → lower transaction prices | Wheaton (1990), *JPE* 98(6) | [1-SOURCE] — the basis for every months-of-unsold-inventory indicator |
| Very-long-run discount rates | 100-year leaseholds price **>10% below** identical freeholds, implying discount rates **below ~2.6%** on very-long-run housing claims | Giglio, Maggiori & Stroebel (2015), UK and Singapore | [1-SOURCE] |

**The price-volume lead-lag is genuinely unresolved and the audit requires that be said plainly.** Clayton, Miller & Peng report that in an average-relationship test **price tends to unilaterally lead volume**; that the link is **asymmetric** (price decreases reduce volume, increases barely affect it); that **volume becomes informative specifically when price is rigid**; and that **volume Granger-causes price mainly where supply is inelastic** [1-SOURCE; the citation is incomplete in the pack and the companion "US 1999–2015 study" is unnamed, D-19]. The first limb directly contradicts the pack's own recommendation that volume is the first-moving variable. Separately, an unnamed study of Norwegian transactions 1850–2019 finds **the fraction of repeat sales at exactly zero nominal price change rises specifically during downturns** — evidence of *price* rigidity [1-SOURCE at best; a 2-SOURCE tag on an unnamed paper is unauditable, D-18]. **The inference from that to "busts appear as collapsing volume before falling prices" requires Stein's mechanism to carry it and is not established by the rigidity finding alone.** Treat volume-leads-price as regime-conditional, not settled.

### 3. NOWCASTING AND ALTERNATIVE DATA

**Every claim in this subsection is `[RECALL — unverified]`.** Dossier A6 returned zero search results — the budget was exhausted (200 of 200) before it ran, and WebFetch is egress-blocked — and the audit verified that disclosure independently and called the tagging exemplary (C-11, D-30). Nothing here may size a parameter, enter the trial ledger, or be quoted in a lesson before a search-enabled re-verification pass.

| Instrument | Recalled record | Notes |
|---|---|---|
| Google search volume | A housing search index **Granger-causes future home sales more strongly than future prices** — intent shows in volume before price — with recalled OOS error reduction **~20–25% for sales**, materially less for prices (Wu & Brynjolfsson) | Venue possibly a chapter in *Economic Analysis of the Digital Economy*, not a journal |
| Search volume, MSA level | Effect concentrated **1–2 quarters ahead** and **stronger around turning points than in trending markets** — a regime detector, not a continuous forecaster (Beracha & Wintoki, c. 2013) | — |
| Search volume, Europe | **Weaker and less stable** outside the US — the "works best where it was discovered" pattern (Dietzel/Braun/Schäfers, c. 2014) | Author set low confidence |
| The standing failure case | **Google Flu Trends over-predicted prevalence badly after 2011–12**: silent platform algorithm changes altered the input series, media-driven spikes decoupled from prevalence, and the model was never re-estimated against ground truth (Lazer, Kennedy, King & Vespignani, *Science* 343(6176), 1203–1205, 2014) | High confidence it exists as described |
| Listings-based nowcast | Asking prices, price cuts and time-on-market nowcast a repeat-sales index ahead of its ~2-month publication lag, and **detected the 2006–07 turning point materially earlier** than Case-Shiller/FHFA in real time (Anenberg & Laufer) | Audit correction candidate: title is "**A More Timely House Price Index**", *ReStat* 99(4), 2017, with **no "Using Zillow Data"**; the listings source needs checking (D-29) |
| Industry high-frequency series | Days-on-market, price-cut share, months of supply, sale-to-list, weekly to monthly; a rising price-cut share was an early tell of the 2018–19 US cooling | Practitioner-grade, no peer-reviewed lead-lag magnitude. "Above ~6 months a buyer's market" is industry folklore, not a study |
| Nightlights | DMSP-OLS intensity as an activity proxy, lights-vs-GDP-growth elasticity on the order of **~0.3**, with a blended lights-plus-official estimator beating official statistics **where statistical capacity is weakest** (Henderson, Storeygard & Weil, *AER* 102(2), 994–1028, 2012) | High confidence |
| Sensor discontinuity | DMSP-OLS is ~1km-class, 6-bit, **saturates over bright urban cores** (cannot separate central Mumbai from central Delhi once both max out), uncalibrated across satellites, and blooms. VIIRS Day/Night Band (from ~2012) is ~500–750m with monthly cloud-free composites and less saturation, at the cost of flare/fire/moonlight noise. **The two are not splice-comparable without explicit inter-calibration** | Same caveat class as the desk's own 2021 NSE index splice |
| Built-up-area grids | JRC Global Human Settlement Layer: built-up area and volume from multi-decade Landsat and Sentinel-2, epochs recalled near 1975/1990/2000/2014–15/2020 | Epochs and resolutions unverified |

**The AVM error record.** Zillow's self-reported Zestimate median absolute percentage error is recalled running from **double digits (~13–15%) at the 2006 launch** to roughly **7–8% off-market and 5% or under on-market** by the mid-2010s, with a further claimed step down after a production neural model around 2019 (press coverage recalled at ~1.9% on-market — the dossier's least-trusted figure). **The shape is more trustworthy than any figure in it: large early gains, diminishing later gains, and off-market persistently 2–3x harder than on-market.** The Zillow Prize — a Kaggle competition c. 2017–2019 to predict the log-error of the existing Zestimate, recalled at a ~$1.2m pool with a $1m grand prize — matters for its *structure*: a public leaderboard round then **final judging on a private, later time window**, engineered because the public leaderboard was known to be gameable. Winner and production improvement are deliberately not named, to avoid fabrication.

**Zillow Offers is the load-bearing negative finding of this subsection and arguably of the pack.** Zillow's iBuying arm used the Zestimate-derived engine to make cash offers, buy, lightly renovate and relist. In Q3/Q4 2021, in a market that appreciated fast then decelerated on rates, the algorithm was — by the company's own admission — buying homes it could not profitably resell, compounded by contractor shortages slowing the flip cycle and swelling inventory. Zillow paused purchases and in **November 2021** announced a full wind-down, a workforce cut recalled at **~25% (~2,000 jobs)**, and an inventory write-down recalled at **~$300 million for Q3 2021** ("$304 million" specifically recalled, flagged for re-verification), with cumulative losses on the ~7,000–9,000 unsold homes reported at the time running toward and by some tallies past **$500–900 million** into the 2022 wind-down. The stated explanation was that the model's error bands were too wide for the flipping business's thin margins. **A widely-benchmarked AVM whose aggregate error looked good failed at committing capital to a narrow, forward-looking, single-asset decision in a regime-shifting market — not at the task it was validated for.**

**The mechanism is the random-split-versus-time-split trap, and it is the one point in A6 that stands independent of any citation.** A random train/test split puts transactions from the same market period — same rate environment, same price level, same lending conditions — into both training and test sets, so a boosted tree interpolates within a regime it has already seen and reports large gains versus a linear hedonic baseline; the recalled range is **20–40% error reduction versus OLS under random splits**. A chronological split forces extrapolation to a price level and macro regime never seen, which tree-based averaging structurally cannot do while a hedonic with a time trend can at least extrapolate linearly. **The recalled pattern is that the ML-over-hedonic advantage shrinks sharply and can invert under a true temporal holdout, especially across a regime break** — the AVM-literature version of the desk's own purged-CV rule, and why the Zillow Prize was built with a forward private round.

**One correction that must not be quietly dropped.** A6 recommended the satellite stack as a live runsheet candidate because "no egress block applies to satellite data providers already in the free-data universe." **That is refuted by the desk's own measurement the same day**: `_PROBE.md` probed NOAA-VIIRS (`eogdata.mines.edu/products/vnl/`) and JRC-GHSL (`human-settlement.emergency.copernicus.eu`) and **both returned `000 0` — curl error 56, CONNECT tunnel failed, gateway 403, `kind=connect_rejected`** — alongside Overpass, Geofabrik, Google Open Buildings and WorldPop. **36 of 37 endpoints blocked; only the GitHub control answered.** Nightlights and built-up grids remain an attractive untried construction-supply nowcast, but they are a principal-machine pull like everything else on the runsheet. [2-SOURCE — first-party, `_PROBE.md`, `_TAIL-PROBE.md` §5]

### 4. TRANSFERABLE COEFFICIENT MAGNITUDES AN INDIA MODEL SHOULD EXPECT A PRIORI

Priors, not parameters. The mechanisms are plausibly portable; the magnitudes come from mature, high-mortgage-penetration, thick-rental-market economies and are not shown to transfer. Every row is a pre-registration candidate and the transfer verdict is the load-bearing column.

| Parameter | International magnitude | Quality | India transfer verdict |
|---|---|---|---|
| Annual AR(1), city price growth | ≈0.60 median US city, persistence 2–3y | [1-SOURCE] | **Re-estimate, do not import** — per city or convergence club |
| Momentum → reversal crossover | Momentum ~1y, reversal ~5y (calibration) | [1-SOURCE] | **Reject the 5y reversal limb.** IN-D1: next-5y real after a ≥15%/yr window is **+9.65%/yr**. Carry roughly **2x crash odds** off a **13.0%** base instead |
| Boom amplitude, inelastic vs elastic | 29% vs 3.4% (1980s US) | [1-SOURCE] | Directionally portable; the India city ranking rests on unverified trade-press FSI and is a hypothesis only |
| Tract-level supply elasticity | Floor-space ≈0.5, units ≈0.3; within-metro > between-metro | [1-SOURCE] | Portable as a *structure* rule: ward/zone proxies, not one city number (Mumbai's island/suburb/MHADA tiers already show it) |
| FAR relaxation → supply, price | India: **+17%** utilisation → **+58%** units, **−24%** prices (Mumbai) | [1-SOURCE], one unrefereed manuscript | The only causally-identified India magnitude. **Mumbai-specific, not a national constant** |
| Credit volume → price elasticity | 0.134 over one year (US) | [RECALL — unverified] | Do not import. US mortgage/GDP ~51–76% vs India ~11–12.5% |
| LTV elasticity of prices, India | **0.40–0.59** small-ticket; **1.10–1.14** large-ticket | [1-SOURCE] | The only directly-applicable India credit numbers retrieved. **Segment by ticket size, not just city** |
| Which credit constraint binds | PTI/DTI, not LTV; PTI rate-elasticity ~8; 42% of the US price-rent rise | [1-SOURCE] | Portable as a *choice of variable*: prefer DSR/EMI-to-income over the LTV level |
| Macroprudential tightening | DSTI −4 to −7pp credit growth/yr; LTV/DTI caps ~−1.5pp credit, ~−1.2pp real price growth | [1-SOURCE] | An order of magnitude for RBI risk-weight and LTV events. Expect cash-flow tools to bite and pure collateral caps to disappoint (Sweden 2010, NZ 2021) |
| Home-equity extraction | 25–30 cents per dollar of equity gain | [1-SOURCE] | **Expect far lower** — India's equity-withdrawal infrastructure barely exists; treat as near-zero until measured |
| Credit boom → 3y crash odds | **1.72x lift, 87.2% false-alarm rate** | [2-SOURCE — first-party] | Usable as a probability shift. Never as a point call |
| Early-warning discrimination | AUC 0.61→0.71 adding credit growth; AUROC 0.717 | [1-SOURCE]; plausibly the **same statistic** double-counted | Modest-to-fair. Set India expectations here, not higher |
| Crash depth and duration | Median real crash **−34.2% over 6.5y**; modern **−32.0% over 5.5y**; velocity ratio **0.99x modern** — busts are **not** slower than booms | [2-SOURCE — first-party, CN-D1] | The base rate to size against. A bigger boom buys **speed, not depth** (depth gap 3.8pp; 3.5pp/yr faster) |
| Yield at the turn | Median peak gross yield **3.29%**; busts end near **5.2%**; compresses **−0.83pp** into the peak, expands **+1.53pp** to the trough | [2-SOURCE — first-party] | The most usable valuation-anchor calibration available, and it is the desk's own. India portal yields must first be reconciled across two irreconcilable source families |
| Equity spillover from a housing bust | **−13.7pp** excess real equity return in year one, double if banks break, recovered by year five | [2-SOURCE — first-party, CN-D5] | Relevant to the standing book independent of any India price model |
| Loss-averse seller anchoring | List +25–35% of the nominal loss; realise 3–18%; lower hazard of sale | [1-SOURCE] | Plausibly *stronger* in India (thin resale, high stamp duty and brokerage) but **[RECALL]** — no India study exists. Registrable once transaction-level holding-period and purchase-price fields exist |
| AVM error, off-market | ~7–8% MAPE, ~2–3x on-market error | [RECALL — unverified] | The **optimistic** ceiling for India, where comparable-sales density and price truthfulness are both worse |
| ML gain over hedonic | 20–40% under random splits; shrinks or inverts under a chronological split | [RECALL] on range; mechanism robust | **Only the chronological-split number counts** |
| Area-basis measurement noise | Carpet-to-super-built-up loading | [1-SOURCE] | **Retire the pack's "20–35%" constant.** A 70–80% carpet ratio implies **+25% to +43%** per sqft; Mumbai loading is independently reported at **40–50%**. Carry a loading factor L with psf ratio = 1+L (R14) |

### 5. THE HONEST CEILING

**Long horizons.** No retrieved study demonstrates a genuine real-time out-of-sample beat of a random walk at three, five or ten years, and the literature largely does not attempt it. Where horizon is explicitly tested, significance is gone by four to eight quarters — the *shortest* end of the range a multi-year engine needs.

**Timing, at any horizon.** Correction through prices "can take decades" on 355 years of Amsterdam data [1-SOURCE]; Shanghai has sat near 1.25–2.0% gross yields for years with no forced resolution date [1-SOURCE]. The desk's CN programme reached the same conclusion by five independent routes — **the structure was knowable and the timing was not** — and CN-D4 saw **both** registered priors miss: a bigger boom buys speed rather than depth, and the "busts are slower than booms" bar missed outright at a modern velocity ratio of **0.99x**, so there is no gentle-deflation discount to assume [2-SOURCE — first-party]. A valuation signal is a state, not a clock. Nor is there a half-life to build a clock from: no reliable cross-study figure survived search, and Capozza et al. establish that reversion speed *varies* with city size, growth and construction costs, which is why no constant exists.

| Failure | What was claimed | What happened | Quality |
|---|---|---|---|
| **Zillow Offers, 2021** | An AVM with steadily improving published MAPE, used to make binding cash offers | Wound down Nov 2021; ~25% workforce cut; ~$300m Q3-2021 write-down; cumulative losses reported toward $500–900m. Error bands too wide for thin flipping margins | [RECALL — unverified]; top re-verification priority |
| **Himmelberg, Mayer & Sinai (2005)** | User cost across 46 US metros, 1980–2004: owning dearer relative to renting but **in most metros not to overvalued levels** | US prices fell more than 30% into 2008–2012. The appreciation term was fed by the boom, so rising prices mechanically lowered measured user cost | [1-SOURCE] |
| Google Flu Trends | Search volume as a real-time prevalence nowcast | Large over-prediction after 2011–12: platform algorithm drift, media-driven spikes, no real-time error correction | [RECALL — unverified] |
| Gallin (2006) | Prices track income in the long run | Panel cointegration **fails to reject no-cointegration**, 95 metros, 23 years | [1-SOURCE] |
| Balcilar et al. | Nonlinear regime-switching for regional price growth | In-sample detectable; out-of-sample "virtually non-existent" | [RECALL — unverified] |
| RBNZ LVR, 2021 reintroduction | A tool with a stated 1–2pp price-inflation effect in 2013 | "Little impact" on repeat application; benefit reframed as system resilience, not price control | [1-SOURCE] |
| Sweden's 2010 LTV cap | A collateral cap to restrain prices | No measurable price effect; the 2016 *amortisation* rule is the one associated with roughly −7% | [1-SOURCE] |
| ULCRA repeal, India | Land-ceiling repeal would release urban land and deliver formal supply | Did not, across 200+ cities: property-rights disputes over the frozen surplus parcels triggered litigation that kept construction frozen | [1-SOURCE] |
| Micro bias as a macro signal | Loss aversion moves prices | Real at the unit level, but **the aggregate cycle was only mildly affected** once aggregated, and the effect was "virtually ineffective" in the 2008–09 crash | [1-SOURCE] |
| Case & Shiller (1989) at the unit level | Index-level serial correlation as a pricing signal | Individual-home R² **never more than 0.04** | [1-SOURCE], one secondary review |

**Crash prediction is high-recall and low-precision by construction, not by accident.** The desk's own print is 1.72x on three-year crash odds with an **87.2% false-alarm rate**, and the BIS convention alongside it deliberately chooses thresholds to minimise noise-to-signal *subject to catching at least two-thirds of crises*. Discrimination in this family tops out in the modest-to-fair band (AUC ≈0.71). Specify, review and report any India early-warning module as a probability shift with an explicit false-alarm budget; a module presented as a call is misspecified.

**And the ceiling on this evidence pack itself.** `_AUDIT-1`'s structural finding is that **zero of roughly 120 external citations across A1–A6 have been checked against a primary source.** It documents two dossiers double-sourcing mutually exclusive facts about the same index base year (R7), one paper counted twice through hosting mirrors to manufacture a `[2-SOURCE]` tag (R12), a contradiction relabelled as a convergence (R9), a likely fabricated third author on one of the most-cited papers in housing finance (R3), an index level arithmetically impossible against its own stated base year (R6), and an unsold-inventory series whose own unit counts contradict its own stated direction (R8). This is a high-quality research lead list. It is not yet an evidence base.

### WHAT THIS SECTION CHANGES ABOUT THE PLAN

1. **Scope the engine to one to four quarters and pre-register it as a state-conditional distribution engine, not a point-forecast engine.** Every credible out-of-sample beat lives at 1–4 quarters and significance is gone by 4–8; write the horizon cap into the registration rather than discovering it later. (§1)
2. **Drop the five-year mean-reversion overlay before it is built and replace it with a crash-probability sizing rule.** IN-D1 prints **+9.65%/yr** next-5y real after a ≥15%/yr window and **+11.16%/yr** after ≥20%/yr, crash odds roughly 2x off a 13.0% base, and the 2.0x bar recorded as a MISS at the ≥15% rung. Hot markets stay hot: size against the tail, do not forecast the reversal. (§1.1)
3. **Make the momentum estimate India-native and city-or-club level.** Do not import the 0.60 AR(1), the 2–3-year persistence, or the 29%/3.4% amplitude. India's club-convergence evidence plus Capozza et al.'s finding that aggregation masks the heterogeneity driving predictability both rule out a single national model. (§1.1, §2.4)
4. **Build the credit module on a cash-flow variable (DSR / EMI-to-income) with ticket-size segmentation, and pull the RBI Master Circular before anything else in it.** Greenwald, Sweden 2010-vs-2016, NZ 2021 and Kuttner-Shim all point the same way; Bhupal Singh's 0.40–0.59 versus 1.10–1.14 split makes ticket size first-order; and the pack's own LTV/risk-weight schedule is internally contradictory (R11) and cannot be coded from. (§2.3)
5. **Add developer/construction finance as a distinct module rather than folding it into mortgage credit.** India's identified credit-supply shock is the 2018–19 NBFC/HFC contraction on the supply side, not a household-mortgage shock, and RERA escrow raised per-project external-financing dependence. Model it as a leading indicator for launches and completions. (§2.3)
6. **Score supply elasticity on three layers and register the city ranking as a hypothesis, not an input.** Legal FSI/FAR cap; title and litigation friction (27.3% of Mumbai projects, 42.9% of built-up space, 8.5-year average build, ≥30% cost from delay); physical land availability. Anchor Mumbai to +17%/+58%/−24% as a single-source working-paper estimate, flagged as such. (§2.4)
7. **Retire the "20–35%" area-basis constant and replace it with an explicit loading factor.** Carry L with psf ratio = 1+L; a 70–80% carpet ratio gives +25% to +43%, and Mumbai's reported 40–50% loading means the old constant understates the worst case in the primary market by up to 15pp. Every per-sqft series needs an area-basis field and a RERA-status flag and must never be pooled across that boundary. (R14, §4)
8. **Mandate a chronological, purged holdout spanning at least one regime break for every valuation or ML component, and publish off-market error separately from on-market.** A random k-fold number is not evidence of anything the engine will face. Expect off-market error at 2–3x on-market and treat ~7–8% MAPE as an optimistic ceiling. (§3)
9. **Treat volume-leads-price as a regime-conditional hypothesis and reconcile the unsold-inventory series before wiring it.** Clayton-Miller-Peng's own average-relationship test has price leading volume, and the Norwegian rigidity finding needs Stein's mechanism to reach a volume conclusion (D-18, D-19). The 55→32→20→"rising" path also fails its own arithmetic: 600,000 units against the quoted sales run-rate implies ~17.7 months, *below* the reported 20-month five-year low (R8). Fix stock-versus-months and city-coverage definitions first. (§2.5, §5)
10. **Re-plan the satellite leg as a principal-machine runsheet pull, and put the A6 re-verification queue ahead of any nowcasting build.** NOAA-VIIRS and JRC-GHSL both returned `connect_rejected` in the desk's own probe — 36 of 37 endpoints blocked — so the "no egress block applies" premise is refuted (R2). The whole nowcasting subsection is `[RECALL]` and needs a search-enabled pass before a single figure sizes a parameter. (§3)

---

## COUNTRY PATTERNS: THE DATA REGIMES, AND WHAT HAPPENS WHEN A COUNTRY FORCES DISCLOSURE

**What a country's house-price data looks like is decided by the legal event that generates the
price, not by the country's income level.** Where the state made the transacted price a registrable
legal fact — England & Wales, Ireland, the Netherlands, Korea, Taiwan — free address-level microdata
exists. Where the state only ever needed a number to tax, the public record is an administrative
valuation roll and the market price is unobserved: Thailand, Pakistan, Turkey, India. Income does not
predict the side a country lands on — Japan publishes a voluntary survey while Korea publishes
named-building, named-floor microdata through a free API. **India's problem is not a technology gap:
India built a valuation roll and a registration system and never joined the two into an index.**

**The binding evidence limitation.** The six dossiers behind this section (`B1`-`B6`) were written
with the shared WebSearch budget exhausted (200/200) and `WebFetch` egress-blocked. **Not one
external claim in them was checked against a primary page, and the audit (`_AUDIT-2`) independently
reproduced the same exhaustion and could not check them either.** Every external claim below is
`[RECALL — unverified]`; the only evidence-grade material is `[DESK PRINT]` and `[VAULT-VERIFIED]`.
The audit refuted sixteen claims from the vault, desk documents, run scripts or internal
contradiction, each struck below or carried with its correction visible. **It also found four
dossiers converting `_PROBE.md`'s gateway-level CONNECT refusals into URL "attestation" — a
fabricated hostname returns byte-identical output — so no URL here is described as verified.**

---

### 1. THE HOUSE-PRICE DATA REGIME, COUNTRY BY COUNTRY

**Three jurisdictions reach a free address-level price; roughly six reach a locality; most emerging
markets stop at a city or national index.** All cells `[RECALL — unverified]` unless tagged; per the
audit this is a reading map, not a fact table.

| Country | Producer / product | Method | Finest FREE geography | Licence / access |
|---|---|---|---|---|
| US | **Case-Shiller** (S&P DJI/CoreLogic) | Repeat-sales, 3-stage weighted; 3-month trailing average | 20 metros; no free county/ZIP/tract | Levels free (FRED); microdata proprietary |
| US | **FHFA HPI** — all-transactions / purchase-only / expanded-data | Repeat-sales; all-transactions pools repeat *appraisals* | ~3,000 counties; experimental annual ZIP and **tract** `[start-year uncertain]` | Public domain, bulk CSV |
| US | **Zillow** ZHVI/ZORI; Redfin; Realtor.com | AVM over the housing *stock*; MLS activity rollups | ZIP; neighbourhood in large metros | Free bulk CSV; Zillow restricts commercial reuse |
| US | Census **BPS**, **ACS B25077**, **HMDA** | Permit census; self-reported values; loan-level register | Place/county; **tract** (ACS, self-reported); **tract** (HMDA) | Public domain, bulk + API |
| US | Recorders — Cook, King, NYC **ACRIS**; **Texas** + ~a dozen non-disclosure states | Deed-level stated consideration; **no price on the deed** in non-disclosure states | **Address/parcel**; transfer only in TX | Free portals |
| England & Wales | HMLR **Price Paid Data**, from 1-Jan-1995 | Census of full-market-value registered sales; ~29-30m rows | **Address** (PAON/SAON + postcode) | **OGL v3.0, free bulk CSV, no key** |
| England & Wales | **UK HPI** (HMLR/RoS/LPS/ONS, unified ~2016) | Hedonic, mix-adjusted | Local authority district | Open |
| Scotland / N. Ireland | Registers of Scotland; LPS/NISRA NI HPI | NI runs **quarterly** inside a "monthly" UK HPI | Local authority | Open |
| Ireland | PSRA **RPPR**, from 1-Jan-2010 → CSO **RPPI** | Census of sales filed for **stamp duty** — a tax filing, not a title registration; "Not Full Market Price" flag | **Address** | Free, search + download |
| Netherlands | Kadaster (notarial deed) + **WOZ** universal annual valuation (~8m dwellings) | **SPAR** — sale price over assessed value | Address (WOZ lookup ~2016) | Aggregate open; **per-record deed fee believed** |
| Nordics | DK Tinglysningsretten (~2009)/StatBank; SE Lantmäteriet/SCB; NO SSB + Eiendom Norge; FI Statistics Finland + NLS **HTJ** (~2019) | Registry-sourced DK/SE; **agent-reported NO/FI — SSB believed built on the faster agent feed, not the registry; Finnish apartments are housing-company *shares*, so agent reporting is mandatory** | Address via DK portals; municipality otherwise | Statistics agencies open |
| Japan | MLIT **Real Estate Information Library**; Koji Chika (1970-), Kijun-chi, **Rosenka** (≈80% of Koji Chika) | **A voluntary survey, not a registry extract**; **none of the other three is a transacted price** | City/ward + district; area **banded**; date to **quarter** | Free; **REST/JSON API** |
| Korea | MOLIT **RTMS** (apartments from ~Jan 2006); K-REB survey vs **KB Liiv On** | Census tied to mandatory actual-price reporting; also **jeonse/wolse** leases | **Complex + dong + floor + exclusive area + exact date** | **Free API**; account + dataset application |
| Taiwan | MOI **實價登錄**, 1-Aug-2012; 2.0 ~1-Jul-2021 | Mandatory actual-price registration | Address-range → **address** (2.0) | Free |
| Singapore | **HDB Resale Flat Prices** (to ~1990); URA **REALIS**; URA PPPI | HDB a census of public-housing resales; REALIS **caveat-level**, ahead of completion | **Block + street + storey band** | HDB free bulk + API; **REALIS paid** |
| Hong Kong | RVD indices; Land Registry **Land Search**; Centaline **CCL** weekly | RVD construction **unresolved**; CCL provenance **contradicted** | Region + size class free; address at **fee per record** | Free aggregates; fee-per-deed |
| China | **NBS 70-city** (2011 revision); CREIS; Beike; **Fang-Gu-Xiong-Zhou** microdata | Administrative, **window guidance (窗口指导) recalled 2021-23**; private listing indices; one bank's loan file, 120 cities 2003-2013 | 70 cities / city | Free; mixed (private) |
| Brazil | **FipeZap** (~2011); BCB **IVG-R**; IBGE **SINAPI** | FipeZap **asking**; IVG-R appraisal/collateral; **SINAPI is construction cost, not prices** | City | Free |
| Mexico | **SHF** (~2005); INEGI role `[VERIFY]` | Mortgage **appraisal** values (SHF + Infonavit + Fovissste + banks) | State | Free |
| Turkey | TCMB **Konut Fiyat Endeksi** (~2010=100) | Hedonic on bank **appraisal** valuations; **real series published alongside nominal** | City + Istanbul | Free |
| South Africa | **Lightstone**; Absa HPI; FNB HPI | Full Deeds Office census vs **single-lender book** | Suburb (commercial) | Bank indices free |
| Poland | NBP **BaRN** | **OFFER and TRANSACTION prices for the same cities and quarters** — the only paired design found | ~7 cities + voivodeship capitals | Free, quarterly report |
| Russia | Rosstat avg price/sqm; **SberIndex**/DomClick | Simple regional averages; **secondary-leg provenance is a flagged recall conflict** | Federal subject | Free |
| Thailand | BoT RPPI; GHB **REIC** | **Treasury Department valuation roll** (a registration-fee floor, structurally a circle rate) plus bank collateral `[VERIFY]` | National/Bangkok | Free |
| Indonesia | BI **SHPR/IHPR** | Quarterly **survey of developers' primary-market list prices** | Major metros | Free |
| Philippines | BSP **RREPI** (~2016-) | Newly granted bank loans; **financed transactions only** | NCR vs outside NCR | Free |
| Vietnam / Nigeria | MoC commentary, Savills/CBRE, batdongsan; Nigeria none identified | Asking-price city reports only | City | **Negative findings: no robust free official index** |
| Colombia / Chile / Kenya | DANE and/or Banco de la República; INE **IPV** (~2018-19); **HassConsult** (~2000-, houses **plus a land index**) | **Colombian and Chilean institutional splits `[VERIFY]` above anything else in the pack** | National/city; Nairobi | Free summaries |
| **India** (comparator) | RBI HPI; NHB RESIDEX; state IGR portals | RBI HPI quarterly, ten cities, **from registration authorities**, Q1:2010-11, base 2010-11=100 `[DESK-VERIFIED]`; RESIDEX carries **two different price legs** and **three dated bases** (2007; FY2012-13; FY2017-18) | City index; registration **counts** free monthly, prices not | Free aggregates, no bulk |

**Two cells the audit touched hardest.** **Zillow's ZHVI tier band** — `B1` prints 35th-65th while
citing a file named `tier_0.33_0.67`; ingestion must take the cut from the filename, and neither
number may be published until the methodology page settles it (`R13`). **Centaline's CCL** — two
contradictory provenances, so it is **not classifiable into a construction type** (`R15`).

**The four construction types, and why the taxonomy precedes any pooling.** Two of the four are not
market prices at all. **Asking/listing** (FipeZap, HassConsult, CREIS/Beike; India's portals) is
downward-sticky, so declines are understated. **Appraisal/collateral** (SHF, TCMB, BSP, Absa, FNB,
IVG-R; India's bank sanction data and RESIDEX's assessment leg) is **blind to cash purchases** and
smooths turns. **Registered transaction/deed** (HMLR PPD, RPPR, RTMS, 實價登錄, Lightstone; India's
IGR/NGDRS) carries whatever the recorded consideration understates. **Developer primary survey**
(Indonesia SHPR; India's RERA filings) is self-reported list prices.

---

### 2. THE FOUR TEMPLATES INDIA COULD COPY

**Verdict first: only the SPAR template is buildable by this desk from data that already exists, and
only in a corrected form the source dossier got wrong.** The open register needs a statute;
statutory disclosure a statute plus an enforcement chain; mortgage microdata a lender's loan book.
SPAR needs a join.

| Template | What India has of it | Verdict / cost |
|---|---|---|
| **1. HM Land Registry open register** — publish the registered consideration for every sale, address-level, open licence; a statistics office builds a hedonic index on top | Registration yes; an honest recorded consideration **no** (§3); a publishing mandate **no** | **Not achievable by this desk — a policy ask, not a build.** What *is* free today is the counts layer: Maharashtra's IGR publishes daily/monthly registration counts and stamp-duty revenue, and Knight Frank India republishes Mumbai's within days of month-end `[DESK-VERIFIED, partC-data.md §C.5]` |
| **2. Netherlands/NZ SPAR on assessed values** — index sale price over an existing universal official valuation | A price at every stamp-duty deed, yes; a universal official valuation (the circle rate covers essentially every parcel), yes; **a controllable assessment vintage, no — revisions follow no fixed schedule** | **THE PRIMARY CANDIDATE, conditional on the vintage problem.** Cost: a join plus an assessment-vintage control; no new pull |
| **3. Japan/Korea statutory disclosure** — force the actual price onto a public record by statute, with a filing window and a reason for the filer to be honest (Korea tied registration itself to the reported price) | Nothing | **Not achievable by this desk — the reform template.** Japan's half is a warning, not a model: its flagship is a voluntary survey, so "free transaction-level API" and "transaction census" are different claims |
| **4. Fang-Gu-Xiong-Zhou mortgage microdata** — a constant-quality hedonic index off one lender's origination file, bypassing the official chain | No public analogue; **no Indian register discloses loan-level originations with geocoded property value**, and there is no HMDA | **Achievable only via a lender partnership; Tier-C at best per `CONTRACT.md §4`.** Its lesson cuts both ways: FGXZ found true quality-adjusted appreciation **larger** than officially reported |

**The SPAR correction, because publishing `B2`'s version would have built the wrong estimator.**
`B2` §8 gives the denominator as "that same property's most recent WOZ value"; the audit refuted
that (`R11`) and `D1` §6 has the correct form, `r_i,t = SalePrice_i,t / AssessedValue_i` with the
assessed value **fixed at a base date**. A most-recent-assessment denominator lets each revaluation
enter the ratio, so the index moves when the assessor moves — and **in India circle rates follow no
fixed calendar, so every ready-reckoner revision would print as a price move.** The reference `B2`
left open while `D1` already answered it: **de Vries, de Haan, van der Wal & Mariën, "A House Price
Index Based on the SPAR Method," *Journal of Housing Economics*, ~2009** `[RECALL — unverified]`;
**New Zealand** (Quotable Value council rating "CV") is a second adopter, undercutting the
Dutch-origin framing.

---

### 3. UNDER-REPORTING AND TRANSFER-TAX EVASION

**Not one quantified evasion estimate in this pack survived audit as citable, and the flagship
nine-paper citation set was named the pack's highest-priority verification batch precisely because
recall confidence on canonical papers was high.** `B4` calls this "the most well-trodden literature
of any B-series dossier" — the audit's candidate for the most dangerous sentence in the file, since
high recall confidence is the condition under which a wrong year or journal survives review. **The
direction is load-bearing; every coefficient is a lead.**

**Second finding, and it changes the estimator: the circle-rate floor is not a censoring identity.**
`D2` modelled `observed = max(true_price, circle_rate)` as left-censoring; the audit refuted it
(`R9`) against `A5`'s own `[2-SOURCE]` mechanics — **duty is charged on the higher of declared price
or circle rate, which constrains the tax base, not the declared consideration.** Nothing prevents a
deed recording a price below the floor, so the pile-up is a **behavioural equilibrium** while `D2`'s
likelihood assigns it zero probability. **The share of declarations strictly below the local circle
rate is a day-one diagnostic; if it is non-zero, plain Tobit is misspecified.**

**Taiwan 2012 is the central natural experiment, and its value is a distinction rather than a
number.** Before 2012, tax ran off announced assessed values (公告現值 for land, 房屋評定現值 for
buildings), both recalled as well below market with no ratio trusted. **實價登錄**, effective
**1 Aug 2012** and recalled as an amendment to the 平均地權條例, required the actual price registered
within a window (recalled 30 days), published free at transaction level with the street number
**masked to a range**; **2.0** (~1 Jul 2021) closed the **pre-sale (預售屋)** loophole, required
registration of contract assignments (合約轉讓) and moved to the **actual building number**. The
tax-base fix came separately — **房地合一稅**, an actual-gain capital gains tax, **2016** and
**2021**. **The lesson survives even if every date is wrong: disclosure reform and tax-base reform
are two independent levers, and they need not move measured prices, reported volumes and tax revenue
together.** Taiwan pulled them four years apart; India already separates a stated stamp-duty
valuation from whatever the deed says, so an Indian reform has the same two levers and must have its
price-dispersion and revenue effects modelled separately. **The honest gap: this pack holds no
trustworthy post-2012 or post-2016 Taiwanese volume, dispersion or revenue figure** — `B3` declined
to invent one, which makes it the first search-enabled session's top target.

**Every quantified evasion estimate in the pack.** The content of the table is how little of it is a
number.

| Claim | Source | Tag / audit status |
|---|---|---|
| Best & Kleven (2018) UK SDLT notch semi-elasticity; Besley-Meads-Surico (2014) stamp-duty-holiday pass-through %; Fisman & Wei (2004) evasion per tariff point | `B4` §1-2 | All `[RECALL]`, **no magnitude trustworthy.** What survives is architectural: notch bunching is reporting/price adjustment, not real response, and pass-through to sellers is partial |
| UK pre-Dec-2014 SDLT slab schedule (0/1/3/4/5%) | `B4` §2 | `[RECALL, INCOMPLETE]` — the top gained further bands inside Best-Kleven's own sample window; quote from the paper or drop the numbers |
| Kopczuk & Munroe (2015) NY mansion-tax missing mass at $1m | `B4` §2 | `[RECALL]` on magnitude. **The structural point needs no number: whether notch bunching is real repricing or fraud depends on how verifiable the recorded price is** — loose wherever the recorded price *is* the number under the evasion incentive |
| Montalvo, Piolatto & Raya (~2020): share of Spanish transactions with a material appraisal-vs-declared gap, and mean gap size | `B4` §3 | `[1-SOURCE → RECALL]`; authors and design held above year/venue, **both headline numbers need a primary check.** The design transfers: pair the tax-exposed declared price with an independently-incentivised valuation and read the whole **distribution** of the gap |
| Pakistan DC rates "a third or less of market"; floor percentages for Greece, Italy, Portugal, Turkey, Egypt, Colombia, Mexico; Spain's "Ley 11/2021" number | `B4` §3-4 | All `[RECALL]`, self-flagged. Mechanisms carry moderate confidence, percentages and statute numbers none |
| India: circle-rate gap "up to ~2x in parts of Mumbai, ~30% in Delhi"; LocalCircles "2 in 3 paid part cash, 1 in 4 over half off-books" | `A5` §7 | **Downgraded to `[RECALL]` by `_AUDIT-1` D-21.** Cross-dossier tension not to be hidden: `A2` reports the primary/developer gap **narrowing from >100% in 2015 to as low as ~6%**. Both may hold for different segments; the engine picks wrong unless the segment is stated |
| India: **Section 50C**, Income Tax Act (via Finance Act 2002) — deems the higher of circle rate or declared price as taxable consideration | `A5` §7 | **`[2-SOURCE]` for mechanics and purpose — the one India-side item above recall grade** |
| India: 43CA/50C/56(2)(x) tolerance band 5% (FA2018) → 10% (FA2020) → temporary 20% (Nov-2020-Jun-2021) | `D2` §5, `C4` §A7 | `[RECALL]`, and **explicitly: two dossiers from the same model with search unavailable agreeing is correlated recall, not corroboration.** Conditional on the band existing, the mechanics hold — a *proportional* band predicts a **plateau**, not a spike, so any excluded window must span the whole band |

**The floor systems, and four variants worth keeping apart.** The plain rule — duty on the **higher
of** declared price or an administrative value — is India's, Portugal's (valor patrimonial
tributário), Mexico's (the **greater of** price, cadastral value or appraisal) and Turkey's (tapu
harcı against the municipal **rayiç değer**). **Pakistan** runs a **three-tier stack** (provincial DC
rate < federal FBR tables from ~2016 < market) — two floors moving at different speeds, the closest
analogue to India's sub-district heterogeneity. **Greece**'s αντικειμενικές αξίες drift stale in
**both directions** — below market in prime zones, above it in post-2008 depressed areas — so a
floor's staleness has a sign set by the cycle phase. **Italy** inverts the design: **prezzo-valore**
(2006) lets the buyer elect tax on the *lower* cadastral value **conditional on stating the true
price honestly**, while the **OMI** zone bands are an **audit-risk trigger, not a hard floor**.
**Spain**'s **valor de referencia** (Jan 2022) *introduced* a floor where one barely existed. **Egypt**
shows a different failure mode: the margin was not under-declaring but not registering at all
(informal "orfi" contracts), addressed by small fixed fees ~2006.

**Why a floor is geometrically different from a notch.** A **notch** produces excess mass below and
a hole above — two-sided, with an internal shape the Kleven integration constraint reads an
elasticity off. A **floor** produces a **single mass point**, mixing transactions whose true price is
genuinely below it with those whose true price is far above it but which declare the floor anyway.
**The mass point has no internal shape, so the registered-price distribution alone cannot separate
the two groups** — which is why the discrepancy design, not the bunching design, transfers to India.
The one regularity supported without a coefficient: **under-declaration rises with the size of the
tax wedge**, so India's uneven revision cadence should leave a *time-varying* evasion signature, not
a flat proportional discount.

---

### 4. EMERGING-MARKET MEASUREMENT LESSONS

**The sharpest lesson sits one level upstream of where anyone looks for it: the deflator itself can
be the contested variable, not just the index.** TCMB's Konut Fiyat Endeksi publishes a CPI-deflated
real series alongside the nominal one — necessary because Turkish CPI ran from ~15-20% in 2020 to a
peak recalled around **85% in Oct 2022**, staying 40-70%+ through 2023-24 `[RECALL — unverified,
directional]`, making nominal YoY prints above 100% routine and meaningless undeflated. But Turkey
*also* has a recalled dispute between TÜİK's official CPI and an independent group (recalled as
**ENAG**, `[VERIFY]` on the name) publishing higher estimates. **That is China's NBS problem one
layer removed: not "is the index honest" but "is the deflator honest."**

**The desk's own print complicates the naive reading of a high-inflation nominal series.**
`[DESK PRINT, IN-D2]`: on hyperinflation-clean windows of the JST panel, a 20%/yr nominal five-year
property run has typically meant about **+12%/yr real** (mean real +12.42 vs nominal +23.17%/yr;
inflation supplied **46%** of the headline; only **2.3%** of hot nominal windows were real-negative).
The desk's registered money-illusion prior **missed**. The rule is "deflate anyway, because the
exceptions are currency events": the nominal leg without that exclusion averaged +962.71%/yr.

**The asking-versus-transaction gap has been measured, by design, in exactly one country.** NBP's
**BaRN** collects offer *and* transaction prices for the same Polish cities and quarters; the
recalled gap is offer above transaction by a **single-digit to low-double-digit percent** in ordinary
conditions, narrowing or flipping in tight seller's markets (~2021-22) `[RECALL — unverified,
approximate range only, not a plug-in]`. FipeZap, HassConsult, CREIS/Beike and India's portals all
lack a published companion transaction series, so **no confident percentage-point gap exists
anywhere else.** **Hence a prohibition: do not import a foreign asking-vs-transaction haircut into
India** — BaRN's paired-collection design is the template, so measure the gap rather than borrow
it.

**Official smoothing, and what the desk's own China programme adds.** `B5` gives the mechanism
(local statistical bureaus answering to local governments with a fiscal stake in land revenue;
recalled 2021-23 window guidance) and the corrective (Fang, Gu, Xiong & Zhou's one-bank loan file).
The CN programme sharpens it three ways: **the consensus path lands on the base rate** (official
-24.6% plus Goldman's further ~10% compounds to **-32.1%** against the desk's modern-era median
**-32.00%**, `[DESK PRINT, CN-D1]`); **no adjustment multiplier for official Chinese data exists**
(`c-datatrust`: practice is **substitution, not haircutting**), and the **official-vs-private ~2x
measurement gap is the binding uncertainty** of the whole China analysis; and an unadjusted average
is demonstrably unsafe, since Chinese land *price* fell only **-23%** while land *volume* fell
**-66%** and revenue **-52.3%** — a **composition artifact** as distressed lower-tier parcels
stopped transacting. Indian ward markets are thin enough for the same shift.

**Two biases that must never be netted.** Appraisal and bank-book indices all **miss cash
transactions**, large at the high end and in less-banked areas; in India that compounds with a
*separate* bias — stamp-duty-minimising understatement toward the circle rate — pointing a different
way for a different population. South Africa gives the staging path: bank-book proxy first,
full-registry census second (Lightstone), and the gap between them read as the diagnostic.

---

### 5. THE LONG-RUN BASE RATES, AND WHERE INDIA AND CHINA SIT

**The base rates here are `[DESK PRINT]`, not literature. `B6` recommended sizing the India stress
scenario at -20% to -30% real over 4-5 years from unverified recall of two external papers, when
this desk's own pre-registered print from the same JST panel is -34.22% over 6.5 years. The audit
refuted it (`R6`): a `[RECALL]` figure was allowed to override a `[DESK PRINT]`, in the milder
direction, inside a recommendation block.** Even the mildest quartile of the desk's distribution
(-27.52%) sits at the bottom edge of `B6`'s band.

| Long-run real appreciation | Span | Figure | Tag |
|---|---|---|---|
| Knoll, Schularick & Steger, "No Price Like Home," *AER* 107(2), 2017 | 1870-2012, 14 advanced economies | **~1%/yr** full sample; **~1.5-2%/yr** post-1950 | `[RECALL]`, but **consistent with the desk's `[Verified]` statement**: a real tripling since 1950 implies 1.79%/yr over 62 years, 0.77%/yr over 143 |
| Eichholtz, Herengracht Index, *Real Estate Economics*, 1997 | Amsterdam 1628-1973 | **close to zero**, with huge multi-decade swings around a flat trend | `[RECALL]` |
| Ambrose, Eichholtz & Lindenthal, "House Prices and Fundamentals: 355 Years of Evidence," ***JMCB* 45(2-3):477-491** | Amsterdam 1650-2005 | Price-rent correction runs through **prices** and takes **decades** | **`[2-SOURCE]`** — the one citation the pack could firm up; the title is **355**, not 350 |
| Shiller US real house prices | 1890- | **flat/cyclical to the mid-1990s**, then the 1996-2006 runup | `[RECALL]` |

Three independent series converge: **absent an identifiable structural break, long-run real house
prices are not a reliably compounding asset.** "Housing does 5-7%/yr real" is a recency artifact of
the post-1950 (or post-1996 US) window.

**Two corrections to the source account of KSS, both binding (`R3`).** The land mechanism is
**transport costs**, not scarcity: falling transport costs expanded the effective supply of
commutable land until mid-century, when that stopped and land-use regulation tightened. And the
figure of record is that **land price increases explain roughly 80% of the aggregate global
house-price rise since WWII** (desk-`[Verified]`) — **not** the "six-fold real rise in land since
1950" or the "third toward half" land-share path `B6` printed, neither of which appears on desk.
`B6`'s recalled 14-country sample list is struck entirely: the cross-check built to validate it
discards Finland (from 1905) and Switzerland (1901) as "too late" for an 1870-2012 panel while
keeping Italy (**1970**) and Spain (**1971**) `[VAULT-VERIFIED]`.

**The drawdown distribution — `[DESK PRINT, CN-D1]`.** 48 completed episodes, 18 countries,
1870-2020; the definition was frozen before the run as a real peak followed by a **≥20%** decline
to trough, peaks ≥10 years apart, trough on or before 2020.

| Statistic | Full sample (n=48) | Modern, peaks from 1970 (n=24, 16 countries) |
|---|---|---|
| Median peak-to-trough **real** decline | **-34.22%** (p25 -49.96, p75 -27.52) | **-32.00%** (p25 -39.43, p75 -29.19) |
| Median duration | **6.5 years** (p25 4.75, p75 12.25) | **5.5 years** |
| Median decline velocity | **-6.95%/yr** | **-7.41%/yr** |
| Median pre-crash 5y appreciation | **+5.60%/yr** | **+6.21%/yr** |
| Velocity ratio (bust ÷ boom speed) | **1.12x** — the registered "busts are slower" bar **MISSED** | **0.99x**, parity |
| Rental yield, peak → trough | 3.78% → 5.23% (**+1.41pp**), compressing **-0.83pp** into the peak over the final five years | 3.29% → 4.94% (**+1.53pp**) |

**There is no gentle-deflation discount in the base rate.** Three archetypes bracket any forecast:
**Japan 1991** (-47.3% over 18 years at -3.50%/yr, ratio 0.57 — the slow grind), **Ireland 2006**
(-55.7% over 6 years at -12.70%/yr, ratio 1.55 — the worst modern bust) and **Finland 1989**
(-14.87%/yr, the fastest in the panel): same destination, three times the speed. And
`[DESK PRINT, CN-D4]`, **a bigger boom buys SPEED, not depth** — depth gap 3.8pp, unwind 3.5pp/yr
faster — so the exit plan matters more than the entry level.

| Frequency of 20%+ real declines | Value | Basis |
|---|---|---|
| P(a ≥20% real crash peak begins within 5 years of any 5-year window) | **13.0%** | `[DESK PRINT, IN-D1]`, 1,934 overlapping windows, 18 countries |
| Episode census | **48 / 18 countries / 1870-2020** | `[DESK PRINT, CN-D1]` |
| Implied rate | **one episode per ~43.7 country-years ≈ 0.23 per country-decade** | Derived arithmetic on two desk prints (2,097 panel country-years from the `[VAULT-VERIFIED]` `hpnom` start years). **Not itself a registered print**; it independently agrees with IN-D1's 13.0% per 5y window (≈0.26/decade) |
| Crash-odds lift after a hot window | **~2x** (2.02x at ≥10%/yr real, 2.03x at ≥20%; the ≥15 rung printed 1.03x and is recorded as a **MISS**, not smoothed) | `[DESK PRINT, IN-D1]` |
| Best-known credit early warning | Mortgage-credit growth lifts 3y crash odds **1.72x** with an **87.2% false-alarm rate**; public-debt growth reads **backwards** (0.23x — it rises *after* busts) | `[DESK PRINT, CN-D3]` |

**`B6`'s "roughly one country-decade in six to ten sees a 20%+ real decline" does not appear above
and must not enter any published table in any form, tagged or not.** It was self-labelled a
synthesis, not a reported statistic; the audit ruled it inadmissible; and the desk's own
recomputation from the same vaulted panel is roughly twice as frequent.

**Where India and China sit.** India is **absent from every long panel** — JST R6 is 18 advanced
economies, 1870-2020, with **no India and no China** `[VAULT-VERIFIED]`, as are KSS, JKKST,
Herengracht and Shiller by construction. India's horizon is post-2010 and administrative, and the
**current RBI HPI vintage is an 18-city base-2022-23 series whose history starts in 2022-23**, not a
backward extension of the ten-city base-2010-11 series `[DESK-VERIFIED, partC-data.md]`. **The
documented rule is to treat the two bases as distinct vintages and never fit a Hamilton gap or a
percentile rank through the break**, refuting `B6`'s recommendation to build a live India valuation
percentile off a BIS mirror (`R16`); India has **no valuation percentile anywhere in the vault**.
India's own base-rate reads `[DESK PRINT, IN-D1]`: a sustained 20%/yr real boom has **never happened**
in the modern era of the panel (**0.00% of 884** post-1970 five-year windows; the post-1970 maximum
is **Ireland 1999 at +17.25%/yr real**, and Ireland 2006 is the worst modern bust at -55.7% — same
country, seven years apart), yet **hot markets stay hot at five years**, at **+9.65%/yr** real after
a ≥15%/yr window and **+11.16%/yr** after ≥20%, with roughly 2x crash odds: **ride-it-but-size-it,
never in-or-out**. What binds is the cost wedge — **~21.5% over five years**, so a locality doing 20%
cumulative nets **-0.30%/yr nominal, -4.60%/yr real** `[DESK PRINT]`. **Both folk clocks fail their
own pre-registered tests**: 109 real peak spacings across 17 JST countries give median **14y**, IQR
10-17y, only **45%** inside the pre-declared [14,22]y window against a ≥50% bar, and Kuznets swings
fail cleanly (median 11y, **25%** in-window) `[DESK PRINT, RE1/RE2]` — so **`B6`'s endorsement of the "classic ~15-20yr
Kuznets/long-swing housing cycle" is struck (`R7`)**. For China, tier-3 has taken a
**full** base-rate crash while tier-1 has taken about a third of one, and tier-1's 2021 peak rental
yield of ~1.7-1.8% was the **second-lowest peak yield in 150 years**, behind only Spain 2007 at
1.49%, which then fell 42.9%; **for any single Chinese city the national base rate is the optimistic
frame** (Wenzhou -63.1%, Hainan ≈-87%). One last `B6` claim not repeated here: `housing_tr` and
`housing_rent_yd` are **not "vaulted and unused" — both are already consumed**, by CN-D2 and the CI
battery respectively (`R5`).

---

### WHAT THIS SECTION CHANGES ABOUT THE PLAN

1. **Build SPAR with a base-date-fixed denominator plus an explicit assessment-vintage control** —
   `B2`'s wording would make every ready-reckoner revision print as a price move (§2, `R11`).
2. **Make the share of declarations strictly BELOW the local circle rate a day-one diagnostic,
   before an estimator is chosen** — if it is non-zero, plain Tobit is misspecified (§3, `R9`).
3. **Size the India stress scenario off CN-D1 (-34.22% real / 6.5y; -32.00% / 5.5y modern; p25
   -49.96%) and delete the -20% to -30% band** (§5, `R6`); per CN-D4 the exit rule is the design
   object, not the entry level.
4. **Classify every Indian source into the four-way construction taxonomy before pooling any two,
   and never net the appraisal cash blind spot against registration under-declaration** (§1, §4).
5. **Measure the Indian asking-vs-transaction gap directly, BaRN-style, and hard-block any imported
   haircut** — only Poland measures it by design, and approximately (§4).
6. **Build the IGR counts-and-revenue layer first and the price layer second** — counts are free,
   monthly and already cleaned, while registered *prices* are the contaminated series (§2).
7. **Deflate every long Indian nominal series, and test the deflator separately** — the TÜİK/ENAG
   precedent makes it a candidate contested variable (§4).
8. **Do not build an India valuation percentile off RBI HPI or a BIS mirror of it** — a percentile
   rank through the 2022-23 rebase is forbidden on desk; treat the gap as named (§5, `R16`).
9. **Register the tax-parameter history as breaks-registry entries ahead of their consumers** —
   BR1-BR9 hold no circle-rate, 43CA, 50C or stamp-duty entry, and a proportional band predicts a
   plateau, so any excluded window must span it whole (§3).
10. **Queue the Taiwan post-2012/post-2016 volume, dispersion and revenue figures, and `B4`'s
    nine-paper citation batch, first in the next search-enabled session** — both currently empty
    rather than wrong (§3).

---

## THE INDIA SOURCE ESTATE AND THE INDIA LITERATURE

**The six dossiers behind this section ran with the shared WebSearch budget exhausted (200/200) and
`WebFetch` egress-blocked, so all six self-declare `[RECALL — unverified]` throughout — and the
audit (`_AUDIT-3`) then refuted twenty-one of their load-bearing claims, almost none for bad
tagging and almost all because five of its eight files never opened a desk document.** The desk's
`research/cycles/fincycle-deep/partC-data.md` already covers RBI HPI provenance, RESIDEX's two
dated breaks, the registration-count channel and the supply side at desk grade; it answered those
questions differently and it wins. This section is written desk files first, dossiers second — the
reverse of how the dossiers were written.

One tag is added here and defined only here: **`[DESK FILE]`** means a fact recorded in an on-desk
document of record (`partC-data.md`, `india-dossiers/*`, `trial-ledger.md`, `_PROBE.md`) written
when search access existed. Per `_HEAD.md` §00 it outranks every snippet claim in this pack. It is
not an upgrade of an external tag but a separate, higher class. Everything else keeps the tag its
source gave it; nothing is promoted. Bare `R`/`D`/`C` codes below are `_AUDIT-3` row references.

---

### 1. THE OFFICIAL INDEX ESTATE

**RBI's House Price Index is the only official Indian series built from registered transaction
prices and is the correct anchor — but the vintage every dossier here describes was superseded on
10 October 2025.** `partC-data.md` §C.1: RBI published the HPI for **Q1:2025-26 on 2025-10-10** on a
**new base (2022-23 = 100)** with coverage **expanded from ten cities to eighteen** (the ten plus
Hyderabad, Thiruvananthapuram, Pune, Ghaziabad, Thane, Gautam Buddha Nagar, Chandigarh, Nagpur),
back-series from Q1:2022-23 — so the new base's native history *starts* in 2022-23 `[DESK FILE]`,
corroborated `[1-SOURCE]` (A2 §64). **C1 and C5 both call the 10-city / 2010-11 vintage current, and
C1 tells the engine to anchor on it** (R1, R20). An engine built on that trains a city panel through
a documented level break with eight cities silently appearing mid-sample. The repair is
pre-registered: 10-city / 2010-11 as the long history 2010-2025, 18-city / 2022-23 as the tail from
Q1:2025-26, spliced `k = HPI_new(t0)/HPI_old(t0)` `[DESK FILE]`.

| Series | Price concept | Geography | Cadence / lag | Revisions | Access |
|---|---|---|---|---|---|
| **RBI HPI** | **Registered sale-deed prices** from state Registration/Stamps Departments; chain-linked, three floor-space classes (**carpet bands ≤60 / 60-110 / >110 sqm**), averaged per class per **ward**, weights fixed at the Apr-2010–Mar-2011 mix `[DESK FILE]`+`[1-SOURCE]` | **City** (10 legacy, 18 current) + all-India on **fixed 2011 Census population weights**; ward strata exist upstream, unpublished | Quarterly; Q1:2026-27 released **2026-08-24**, ~8wk; earlier 10-12. Range **8-13wk** `[DESK FILE]` | **No RBI policy found on the desk's own pass** `[DESK FILE, VERIFY]`; registration-lag backfill is a structural risk, not a fact | DBIE + Bulletin; no known API `[RECALL]` |
| **RESIDEX @ Assessment** | **Bank/HFC valuation at loan sanction** — a lender's collateral number `[DESK FILE]` | 50 cities (18 capitals + 37 smart cities, overlapping) | Quarterly; Mar-2024 quarter released **2024-06-11**, ~10wk | **Two base breaks**: Jul-2017 relaunch at **FY2012-13=100**, rebased from the **Apr-Jun 2018 quarter to FY2017-18=100** `[DESK FILE]` | Web tool, per-query export `[RECALL]` |
| **RESIDEX @ Market** | Primary and secondary **listing/deal** data `[DESK FILE]` | **Same 50-city panel** — C1's "~18 cities" is the capital-city component of the 50, misread as a ceiling (R4) | Same | Same | Same |
| **MoSPI CPI Housing** | **Rent**; urban-only pre-reform. Weight **21.67% urban / 10.07% combined** `[1-SOURCE]`, matching C1 (C-04) | State/UT, all-India — **not city** | Monthly, provisional then revised | **The rent input is not monthly**: **bi-annual, urban-only** until the 2025-26 reform to monthly rural-and-urban on HCES 2023-24 `[1-SOURCE]`. Pre-2025 prints are largely interpolation; the reform is itself a break (R21) | Release + probable data.gov.in mirror `[RECALL]` |
| **CPI-IW House Rent** | **Rent**, industrial centres; base 2016=100 (prior 2001=100) | ~78 centres on the 2001 base, ~88 on 2016 `[RECALL]` | Monthly | Rents collected by **periodic surveys, interpolated between rounds** — most monthly prints carry no new information `[RECALL]` (C-05) | PDF note `[RECALL]` |
| **RBI RAPMS** | Sanction-time valuation, financed segment only `[RECALL]` | City groupings in FSR boxes `[RECALL]` | Unknown | Unknown | **May not exist as a public series** |

**Four negatives, which matter more here than the positives.** (i) **RAPMS may not be citable** — no
file here and no desk document establishes any public output beyond aggregated LTV charts in the
Financial Stability Report `[RECALL]`. Design nothing around it. (ii) **The "1-4 quarters
provisional" window does not exist**: C1 invented it and built an operational rule on it (D-01);
the desk found no documented policy and prescribes **differencing successive vintages of the same
reference quarter**. (iii) **Ward granularity is a publication ceiling, not a structural one** (R7)
— the index is *constructed* per ward per quarter before aggregation `[DESK FILE]`, making an RTI or
data-sharing request for the existing strata the highest-value acquisition route on this page.
(iv) **RESIDEX is active, not superseded** (R5): quarterly releases continue through at least Q1
2026 `[DESK FILE]`. One correction runs the other way — **RBI HPI does have a carpet-area size
stratification**, which C5 denied (R6).

**Closest to a transaction-price index: RBI HPI, because its input is a registered sale deed.**
RESIDEX's assessment leg is a lender's sanction valuation, its market leg draws on listings, CPI and
CPI-IW measure rent, RAPMS (if public) is a sanction valuation over financed purchases only.
**Binding rule: neither RESIDEX version may be blended with RBI HPI** — three different questions,
and a persistent gap is a divergence to log, not an error to average away `[DESK FILE]`.

**Registered is not transacted, and the bias has a direction.** A sale below the state's minimum
registerable value is deemed to occur at that floor for stamp-duty and capital-gains purposes,
backstopped by Section 56(2)(x) (any gap above ₹50,000 taxed as buyer income). Where cash rides on
top, **registered prices run below true prices and the gap widens when informal-premium behaviour
is most active — late-cycle. Every registration-based gauge understates cycle amplitude, worst at
peaks** `[DESK FILE]`. Primary/developer circle-rate gaps narrowed from >100% in 2015 to as low as
~6% while **resale is where under-reporting concentrates** `[1-SOURCE]` — never pool the two.

**The non-price estate, and its staleness.** Census H-series is the finest official geography that
exists (village/ward, exhaustive) but is **2011 vintage, the 2021 round postponed and its status
unconfirmed** `[RECALL]` — ~15 years stale, and nothing else reaches that grain. NSS 76th Round
(2018) is a one-off condition survey with unconfirmed microdata access terms `[RECALL]`. **PMAY-U's
MIS is a live administrative database, not a release** — snapshot and hash per pull date `[RECALL]`.
NHB's annual *Trend and Progress of Housing* is the under-exploited HFC credit leg but gives
**outstanding stock, not gross disbursal**, with a lineage break at **2019-08-09** (HFC supervision
NHB→RBI). RBI Sectoral Deployment's Housing and Commercial Real Estate sub-lines are the fast,
long-history credit legs both price series lack — monthly, 40 select banks (~93% of SCB non-food
credit), with a **January 2019 format break** `[DESK FILE]` for both.

---

### 2. THE ACQUISITION MAP

**Start with the correction, because it changes the build order: the blanket claim that no state
exposes any bulk registration data is too wide, and the desk already has the free feed for the part
that matters most.** C2 and C6 both wrote the unqualified negative, and C6 then routed "the single
highest-value India probe" through a CAPTCHA scrape (R18). `partC-data.md` §C.5: Maharashtra records
**over 10 lakh registrations annually, Mumbai ~30%**, the IGR portal **exposes a daily/monthly
registration-count and revenue e-search facility**, and **Knight Frank India's monthly Mumbai/Pune
notes are built from the Department of Registrations and Stamps' own published figures, republished
within days of month-end** `[DESK FILE]`. **The negative survives only for transaction-level
microdata — and separately for the rent side, where no aggregate has been confirmed by any pass.**

**The four-tier architecture, common to almost every state** `[RECALL]`:

| Tier | Gate | What it yields |
|---|---|---|
| 0 | Free, no login | Notified-valuation lookup — a zone/ward administrative band by property type. Never a parcel's transaction |
| 1 | Login/OTP + CAPTCHA, nominal fee | Index-II search by village + survey/CTS/khasra number and year: parties, description, **consideration value**, notified value used for duty, duty paid, date |
| 2 | Paid, per document | Certified copies and **Encumbrance Certificates** — 13- or 30-year charge history per parcel, the closest thing India publishes online to a chain of title |
| 3 | — | **Bulk export or API: does not exist for microdata in any major state** |

| State | System | Notified value | Grain | Note |
|---|---|---|---|---|
| **Maharashtra** | IGR (SARITA lineage); eSBTR; **Aadhaar e-KYC leave-and-license e-registration** | **Annual Statement of Rates**, annual | **Zone/sub-zone, cross-walked to CTS numbers in Mumbai** — finest here | Only state with compulsory rent-agreement registration on the sale-deed geography. The free e-search year band is `[RECALL — low]` and is a build-or-no-build parameter (D-12) |
| Karnataka | Kaveri 2.0 + Bhoomi (rural RTC) | Guidance value | Village+survey no.; urban street | EC as a signed PDF — test whether EC text parses cheaper than index scraping |
| Tamil Nadu | TNREGINET | Guideline value | Street/village | EC recalled digitised from ~1987 `[RECALL — low-mod]`; revisions periodic, not annual |
| Gujarat | Garvi | **Jantri** | Village/zone | **Frozen ~2011, revised mid-April 2023, reported roughly doubling statewide, non-uniformly** `[RECALL]`; the auditor's own recall matches all three limbs (C-06). A dated break to register |
| Telangana | IGRS (urban) + **Dharani** (agri, ~Oct 2020), successor announced post-Dec-2023 | Guideline value | Village/ward | **Avoid as first target**: breaks at the 2020 launch and the 2024-25 replacement sit inside the training years |
| Delhi | DORIS | Circle rate, **categories A-H** | **Eight bins per property type** | Resolution-capped at ~8 levels — the coarsest instrument here (C-07) |
| Uttar Pradesh | IGRSUP + UP Bhulekh | Circle rate | District→tehsil→mohalla | District review cycles, no fixed calendar |
| Haryana | — (Jamabandi for records) | **Collector rate** | Numbered Gurugram sectors | "Jamabandi" is Haryana's brand, Punjab's brand and the generic record name — do not conflate |
| Rajasthan / MP / Kerala / W. Bengal | IGRS Rajasthan / Sampada 2.0 / — / e-Nathikaran, Banglarbhumi | **DLC rate** / collector guideline rate / **Fair Value** / — | Zone-colony / — / village+survey no., land in **cents** (1/100 acre) / **mouza** | Kerala's cents and Bengal's mouza are further normalisation steps `[RECALL — low]` |
| Punjab, HP, Jharkhand, Manipur, Puducherry, small UTs | **NGDRS** adopters `[RECALL — low, incomplete]` | — | — | **NGDRS is a shared codebase, not a shared database.** No national portal exposes registered transactions |

**The national layer, and the one fact to verify first.** DILRMP runs record-of-rights
computerisation, registration linkage and modern survey with a progress dashboard; Bhulekh and
Bhu-Naksha are the text and cadastral-map layers, state by state under shared brands but never
federated; SVAMITVA drone-maps previously unsurveyed rural inhabited land. **ULPIN — "Bhu-Aadhaar",
a 14-digit parcel identifier piloted from about 2021 — is the single highest-value item** `[RECALL]`,
because a working parcel key is exactly what a repeat-sales index needs and India otherwise lacks:
survey, khasra, CTS and gat numbers do not compose. Coverage is unknown; no figure asserted.

**The area-basis trap as a formula, not a remembered band.** The pack-wide "20-35%" constant is
arithmetically wrong and twice refuted (`_AUDIT-1` R14; R19): a carpet-to-super-built ratio of
70-80% implies **+25% to +43%**, and Mumbai loading is reported at **40-50%** `[1-SOURCE]`. Carry a
loading factor **L** per series and city, **psf ratio = 1 + L, L up to 0.50 for Mumbai**.

**Verdict — first target Maharashtra, on four grounds stronger than C2's.** (i) The free, cleaned,
monthly registration-count and stamp-revenue channel already exists for Mumbai and Pune `[DESK
FILE]`, so the whole scraping budget goes to the price side. (ii) The ASR publishes annually at
zone/sub-zone grain cross-walked to CTS numbers — exactly the cadence and grain a
sale-price-to-notified-value ratio series needs. (iii) 10 lakh-plus registrations a year reaches a
usable locality-month sample soonest. (iv) It is the only state whose compulsory rent registration
sits on the sale-deed geography, the only Indian route to a **transaction-based** yield. **Next
three: Karnataka** (Kaveri 2.0 and Bhoomi maturity, Bengaluru volume, EC as a cheap per-parcel
history); **Tamil Nadu** (Chennai volume, street-grain guideline value, longest recalled
digitisation); **Gujarat** — not for volume but because the 2011-to-2023 jantri freeze-then-double
is the cleanest dated notified-value shock in India, and therefore a natural experiment on the
circle-rate bunching question. Telangana is deferred despite Hyderabad's size.

---

### 3. THE SUPPLY PIPELINE AND THE PRIVATE ESTATE

**Access degrades as you move upstream, the opposite of the intuition that data improves nearer the
statute.** Building permit → RERA registration → quarterly progress report → OC/CC → registered
sale: RERA registration is the most accessible free rung, permits and OC/CC the least digitised,
registered sales the richest and hardest to obtain in bulk.

**RERA is a launch-and-intent register, not a transaction feed, and there is no national bulk
database.** Every portal is a project-by-project search interface, not a documented API — confirmed
on the desk's own pass for Maharashtra and Karnataka, `[VERIFY]` elsewhere `[DESK FILE]`. Aggregators
(`reradetails.in`, `rerawebsite.in`, `realatic.com`) already scrape several states, which evidences
scrapability, not a free feed. **Budget a state-wise RERA build as a multi-week scraping project**,
Maharashtra first, then Karnataka, Telangana, UP, Gujarat `[DESK FILE]`. The statutory schema
carries registration number, promoter, precise location, land area, tower and unit counts with
**carpet areas** (the Act's defining disclosure reform), the **proposed and any revised completion
date** — each extension its own filing, so delay is directly observable — the 70% escrow account,
and a **quarterly progress report** with percentage completion and units booked `[RECALL]`.
**Whether QPR history is publicly retained or only the latest report shown is unresolved, and the
delay-trajectory feature depends on it.** Separately the record is **status-mutable**: developers
live-update it, so today's snapshot is not the record as of any past date and no upstream vintage
archive exists — snapshot and hash every pull, dated `[DESK FILE]`.

**Permits and completion certificates are the weakest rung.** Mumbai's BPMS and the statewide
AutoDCR lineage (Mumbai, Pune, Nagpur, Thane), BBMP's Bengaluru system and Telangana's **TG-bPASS**
(deemed/self-certified approval below a size threshold) all read as submitter-facing workflow
portals with no recalled public bulk view `[RECALL]`. **OC/CC issuance is the cleanest
pipeline-to-completed-stock event — a certified fact rather than the stated intent of a RERA
revised-completion filing — and the least accessible datapoint in the chain.** Municipal
property-tax portals (MCGM, BBMP SAS, GHMC PTIN) are per-property lookup and payment systems; ward
aggregates circulate only in annual budget books, and assessed value is a formula on locality zone
and declared area, not a market valuation `[RECALL]`.

| Vendor | Underlying data | Bias direction |
|---|---|---|
| Anarock, Knight Frank India, JLL, CBRE, Colliers, Cushman & Wakefield | Each firm's **proprietary tracked-project universe** — a sample of organised launches, not a census | **Coverage bias plus fee-driven optimism.** Fee-earning brokerages; free research skews constructive, and the same city-quarter differs between firms because tracked universes differ |
| Knight Frank / **CREDAI-MCHI** joint Mumbai notes | The state's own published IGR figures | **Closest free thing to volume ground truth** `[DESK FILE]`; CREDAI-MCHI is the developer body — advocacy bias on interpretation, not on the counts |
| **Liases Foras** (Pankaj Kapoor) | Site surveys plus RERA and registration data; subscription research, no brokerage arm | **Bearish** on MMR oversupply. Independent of leasing fees — the adversarial check on the consultancy consensus |
| PropEquity | Project-level primary-sales database sold to lenders, PE funds, developers | Sold to allocators rather than given away for deal flow — a weak argument for less narrative bias, not evidence |
| **Propstack**, **CRE Matrix** | Scraped/licensed **IGR registration microdata** plus analytics | **The only private layer claiming actual transacted consideration.** Their existence evidences what IGR holds: the bottleneck is interface, not data. Commercial — the free-data mandate bites |
| **Magicbricks PropIndex** | Active listings; quarterly free PDF with **locality-level** price and rent for prime micro-markets | **Asking price**, and the asking-to-transacted gap widens in falling markets. One of very few free sub-city India series |
| Housing.com / PropTiger *Real Insight* | Listings plus some advisory-arm transaction visibility | Asking-price base, partially transaction-informed — the "partially" unconfirmed |
| 99acres | Largest listings inventory; research less systematic | Asking price; marketing-oriented cadence |
| NoBroker | Owner-direct, no-brokerage listings | A distinct **sample-selection** bias (cost-conscious owners, salaried tech-hub tenants) atop the asking-price bias |

**The disqualifying property is shared by all of them, and it is not bias — it is the absence of a
vintage layer.** A pull today shows today's snapshot, not what the site showed at any past date, so
a backtest on scraped history silently reintroduces look-ahead bias this desk already prices at
**150-450bps/yr** for fundamentals. **Exploration-only, never the fixture a signal is evaluated
against** `[DESK FILE]`. The demonstration is on desk: H1 2026 unsold inventory across eight major
markets is **~5.26 lakh units** on Knight Frank's count and **~6.16 lakh** on Anarock's, different
city sets and methods `[DESK FILE]` — two respected houses ~17% apart on the headline
supply-overhang number, which is why neither is fixture-grade.

---

### 4. THE EVENT CALENDAR

**Announcement and commissioning are kept in separate columns because this desk's own finding is
that announcement moves the price and completion merely confirms it.** Panvel **+76%** since 2021,
mostly before the first flight at Navi Mumbai; the Jewar belt **+142-158%/5y**, mostly before
flying; the Delhi-Dehradun Expressway **+23% in the nine months before opening**;
Samruddhi-corridor land at ~**3.7x** its 2015 level by 2022-23, two-plus years before the final
stretch opened; completed MMR infrastructure then yields a smaller continuing **8-15%/yr** premium
`[DESK FILE]`. **The corollary belongs at the top: every public, dated feature is already partly in
the price.** C4 attributed this framing to the equity-side TECH-D1 entry state and left the desk's
own dated evidence uncited (R9/R10 severity note).

| # | Event | Announcement | Effective | Why it matters |
|---|---|---|---|---|
| P1 | RERA 2016 `[RECALL]`, all limbs matching the auditor's recall (C-08) | Passed 10 and 15 Mar 2016 | **~59 of 92 enabling sections 1 May 2016; registration, escrow, carpet-area 1 May 2017** | Formal supply becomes observable. **Use each state's own notification date — the gap can exceed a year** |
| P2 | Benami Amendment Act 2016 `[RECALL]` | Passed ~Jul-Aug 2016 | **1 Nov 2016** | Cash-deal risk armed **one week before** demonetisation — a separate dummy, different mechanism |
| P3 | Demonetisation `[RECALL]`, date high confidence, **no magnitude asserted** | **8 Nov 2016** | Same day; exchange window to late Dec 2016 | Liquidity shock to a cash-intensive market |
| P4 | GST introduction `[RECALL]`; 18%×2/3 = 12.0 and 12%×2/3 = 8 check exactly (C-09) | — | **1 Jul 2017** | Under-construction **12% with ITC**, affordable **8% with ITC**; **ready property with an OC is outside GST**, so OC issuance is itself a tax break |
| P5 | GST rate cut `[RECALL]` | Council 33rd/34th meetings, Feb-Mar 2019 | **1 Apr 2019** | **5% and 1%, both without ITC** — a developer net-cost change, not a buyer-price cut; a one-time old/new election gave the same date **heterogeneous project-level effects** |
| P6 | Homebuyers as IBC financial creditors `[RECALL]` | Ordinance ~6 Jun 2018 | Amendment Act ~Aug 2018; Section 7 tightened to 100 allottees or 10% in 2019-20 | Developer default becomes a national insolvency event — the break for stalled-project features |
| P7 | **Maharashtra stamp-duty holiday** `[RECALL]` | — | **2% 1 Sep-31 Dec 2020; 3% 1 Jan-31 Mar 2021; standard from 1 Apr 2021** | The cleanest natural experiment available — **but the April 2021 payback is confounded with the COVID second wave**; control for lockdown severity by month. **No registration count in this pack is usable**: C4's own is `[RECALL — LOW]` and `_AUDIT-1` D-20 found the pack's Mumbai IGR series unreliable (two months each called a "14-year high"; a projection carried at `[2-SOURCE]`) |
| P8 | **Sections 43CA / 50C safe-harbour band** `[RECALL]`; the auditor's recall matches every rung and calls this the best-reasoned item in the eight files (C-10) | FA 2018; FA 2020; **Aatmanirbhar Bharat 3.0 announced 12 Nov 2020**, legislated FA 2021 | **5% from AY 2019-20; 10% from AY 2021-22; 20% for primary residential sales by builders only, ~₹2 crore cap, ~12 Nov 2020-30 Jun 2021** | **The free parameter of the censored-regression design.** A fixed band across a multi-year sample misspecifies the model. Capture both steps — press-conference relief, legislation months later. **Verify first of everything here** |
| P9 | Section 194-IA TDS `[RECALL]`, low confidence on both later dates | FA 2013 | **1 Jun 2013** (1% where consideration ≥ ₹50 lakh); ~1 Apr 2022 the **higher of** consideration or stamp-duty value; ~1 Oct 2024 threshold on **aggregate** consideration | Three dates, each changing how much of the transaction universe leaves a tax trail. Interacts with P8 |
| P10 | Capital-gains overhaul `[RECALL]` | Budget **23 Jul 2024** | Finance (No. 2) Act 2024; grandfathering ~6-7 Aug 2024 | **12.5% without indexation**, resident individuals and HUFs electing the **lower of** 12.5% without or 20% with indexation for property acquired before 23 Jul 2024 — **not for companies or trusts.** Model the option, not a flat rate |
| P11 | Equity comparators `[RECALL]`: LTCG reintroduced (Sec 112A, 1 Feb 2018, FMV step-up 31 Jan 2018); DDT abolished 1 Apr 2020 | — | As dated | Only for the after-tax property-versus-equity hurdle. Already on desk as **BR7-BR9** |

**The breaks registry has no property-tax dimension at all**: `_AUDIT-2` C8 found BR1-BR9 with **no
circle-rate, 43CA, 50C or stamp-duty entry** `[DESK FILE]`. P7, P8 and the Gujarat jantri revision
are three registrable breaks, each owing a pin-the-notification `[VERIFY]` per BR4/BR6 precedent.

| Project | Announcement / approval | Commissioning | Status |
|---|---|---|---|
| Navi Mumbai Int'l Airport | Conceived 1990s; Adani takeover ~2021 | **Commercial ops 25-Dec-2025** (domestic); 24-hour Feb-2026; **international 15-Jul-2026** | **C4's "unresolved" refuted** `[2-SOURCE, DESK FILE]` (R9). The Dec-2024 trial flight is not the event zero |
| Noida Int'l Airport (Jewar) | Foundation **25 Nov 2021** | **Inaugurated 28-Mar-2026; first commercial flight 15-Jun-2026** | Refuted likewise (R10). **Two distinct commissioning events**, finer than C4's own framework carries |
| Samruddhi Mahamarg | Approved ~2015-16 | Ph.1 **11 Dec 2022**; **fully complete 5-Jun-2025** (Vadpe link open mid-2026) | C4's "Mumbai end ~mid-2024" wrong by ~a year (R11) |
| Mumbai Coastal Road | Tendering ~2017-18 | Staged 2024 openings; **Ph.1 fully 24/7 from Aug-2025**; **Ph.2 (Bandra-Dahisar) targeted Dec-2028** | C4 understated Ph.1 by ~14 months and omitted Ph.2 (R12) |
| Atal Setu / MTHL; Metro 2A & 7 | Foundation ~Dec 2016; construction ~2015-16 | **Jan-2024**; **Ph.1 Apr-2022** | Both survive contact with the desk record (C-11) |
| Mumbai Metro Line 3 (Aqua) | Contracts ~2016-17; Aarey dispute 2020-22 | Aarey-BKC **early Oct 2024** — C4 says the 3rd, the auditor recalls inauguration the 5th, service the 7th | **Do not use a day-precise zero** (D-11) |
| Mumbai-Ahmedabad HSR | Foundation **14 Sep 2017** | **No confirmed section open** | The only one of C4's three "unresolved" claims that stands |
| Delhi-Mumbai Expressway; Delhi-Meerut RRTS | Sohna foundation ~Mar 2019; NCRTC mid-2010s | Delhi-Dausa-Lalsot ~Feb 2023, Mumbai end unresolved; Sahibabad-Duhai **20 Oct 2023**, then ~Mar-2024, ~Aug-2024, Delhi side ~Jan-2025 | Section- and corridor-specific, never one date `[RECALL]` |
| Bengaluru Metro Ph.2; Hyderabad Metro and ORR; Pune, Ahmedabad Metro | Sanctions 2019-21; ~2012-14 and staged from ~2008; ~Dec 2016; mid-2010s | Whitefield ~Mar 2023; IT corridor from ~Nov 2017 with Old City ~2023-24, ORR ~Mar 2018; ~6 Mar 2022; ~Mar 2019 then Ph.1 ~30 Sep 2022 | **Corridor gaps of years sit inside one nominal project — a citywide metro dummy is wrong.** Use the stretch relevant to the geography priced |
| **Bengaluru Peripheral Ring Road; Chennai Metro Ph.2** | Repeatedly proposed since the early 2000s, revival ~2022-24; Cabinet approval **year disputed — C4 says ~Aug 2020, the auditor recalls 2024** | **None** | **Right-censored, not missing** — the repeated-announcement pattern is itself informative about how much value front-loads on approval. Chennai's date is unusable as stated (D-10) |
| Bharatmala Pariyojana | Union Cabinet ~24 Oct 2017 (~34,800 km Ph.1) | Not a project | A national capex-regime marker; corridors get their own pairs |

---

### 5. THE LITERATURE: ESTABLISHED VERSUS CONSULTANT ASSERTION

**Established, reached independently three ways: Mumbai's price level is a regulatory outcome, not a
land-scarcity fact.** Bertaud's *Mumbai FSI Conundrum* (2004, updated ~2011) names four compounding
constraints — topography, restrictive land-use legislation, muddled property rights, deficient
infrastructure — and identifies the second, a pure policy choice, as the largest `[1-SOURCE, venue
unconfirmed]`; the mechanism recurs in *Order Without Design* (MIT Press, 2018). Brueckner and
Sridhar (2012), *Regional Science and Urban Economics* 42, find CBD FAR at most 3.5 in Mumbai,
Delhi and Chennai and below 1.5 in Mumbai and Chennai specifically, against 10-plus in other world
CBDs `[1-SOURCE — re-tagged from 2-SOURCE, `_AUDIT-1` R12: two hosting locations for one article is
one source]`. Bertaud and Brueckner on Bangalore height limits put the welfare cost at 3-6% of
household consumption, footprint shrinking 191→159 km² absent the restriction `[1-SOURCE]`.

**India's one causally-identified supply magnitude — single-sourced and unrefereed, said in the same
breath.** Nagpal and Gandhi, *Relaxing Floor Area Ratio: Housing Supply and Affordability in India*
(CEPR/STEG WP), exploiting spatial and time variation in a Mumbai FAR relaxation: **+17% FAR
utilisation → +58% units supplied in treated areas → −24% prices in treated areas**, no average
size change but smaller units where relaxation was greatest `[1-SOURCE — downgraded from 2-SOURCE,
`_AUDIT-1` D-03; −24% is a very large effect to anchor on from one working paper]`. **C5 was asked
for exactly this cluster and never cites it** (D-14) — the clearest instance of the process failure
this section is written around.

**Equal prominence to the negative finding: deregulation on paper did not deliver supply where the
land was legally encumbered.** Dutta, Gandhi and Green, *Is Land-Use Deregulation Enough to Deliver
Housing?*, *Real Estate Economics*, on the ULCRA (1976) repeal — a 500-2,000 sqm cap on
individually held vacant urban land in ~70 cities with "surplus" surrendered below market, repealed
federally in 1999 and adopted state by state to 2008 (Maharashtra only 2007). Diff-in-diff across
200-plus cities: **the repeal did not produce the supply growth theory predicts, because unresolved
property-rights disputes over the frozen surplus parcels triggered fresh litigation that kept
construction frozen** `[1-SOURCE]`. Compounding it, Gandhi, Tandel, Tabarrok and Ravi, *Too Slow for
the Urban March*, *Journal of Urban Economics* (2021), across ~3,000 Mumbai projects: **27.3% of
projects and 42.9% of built-up space under litigation, average construction 8.5 years, litigated
projects ~20% slower, delay raising total cost by 30% or more** `[1-SOURCE]`. **Deregulation splits
into two non-interchangeable categories — raising a floor-space cap on clean-titled plots (worked)
versus releasing legally encumbered land (largely did not) — and Mumbai's effective elasticity is
lower than its nominal FSI implies by an amount close to unmeasurable from FSI data alone.**

**The FSI comparator table everyone quotes is unverified trade press and must not carry a city
ranking.** Manhattan ≈15, Hong Kong ≤12, Tokyo ≈20, Singapore ≈25; Mumbai island 1.33 (suburbs
0.5-1.0, MHADA to 2.5), Delhi 1.2-3.5, Bengaluru 1.5-2.75 residential, Chennai 1.5-2.0, Hyderabad
uncapped with built projects at 6-7 — industry blogs that **blend base, premium and TDR-loaded FSI
inconsistently** `[RECALL — downgraded from 1-SOURCE, `_AUDIT-1` D-23]`. The implied
Hyderabad-to-Mumbai amplitude ranking is a **hypothesis to pre-register, not a finding**. Record the
FSI concept alongside every number, exactly as with area basis.

**Rent control is the second structural mechanism, with a measured consequence.** The Bombay Rents,
Hotel and Lodging House Rates Control Act, 1947 froze rents on a large pre-1940s tenancy stock
indefinitely, removing maintenance and redevelopment incentive and producing Mumbai's cessed
buildings; the informal **pagdi** market — a lump sum for the tenancy right itself, nominal rent
frozen — is the unrecorded response, so recorded rent for that stock does not measure scarcity. The
Maharashtra Rent Control Act, 1999 replaced the 1947 Act but grandfathered existing controlled
tenancies `[RECALL]`. The empirical statement is Tandel, Patel, Gandhi, Pethe and Agarwal, *Decline
of Rental Housing in India: The Case of Mumbai*, *Environment and Urbanization* 28(1), 2016
`[2-SOURCE]`. Measured independently beside it: **~11.1 million vacant urban units in 2011, ~12.4%
of urban stock** (from 1.83m in 1971), reaching ~19% in Gujarat and ~16% in Maharashtra
`[2-SOURCE]` — landlords preferring empty units to formal renting under weak enforcement.

**Established: registered and circle-rate values are a systematically low, time-varying proxy for
market value, and two independent routes agree.** Chakravorty, *The Price of Land: Acquisition,
Conflict, Consequence* (OUP, ~2013) argues Indian land value is set by an administered-price gap
rather than an efficient market, kept wide by chronic under-revision and the state's dual interest
as acquirer and taxer, reading Singur, Nandigram, POSCO and Bhatta Parsaul as symptoms rather than
one-offs `[RECALL, moderate-high]`. The legislative admission of the same gap is **RFCTLARR 2013**,
whose compensation is a multiple of registered value (~1x urban to 2x rural plus 100% solatium,
giving the quoted 2x urban / 4x rural) plus R&R entitlements, with consent (~80/70%) and Social
Impact Assessment for private and PPP acquisition `[RECALL]`. **The multiplier is in part an
explicit statutory correction for a known distortion — so registered values near a compensation
event are a lower bound with an unquantified offset.**

**Established: a large share of Indian urban housing never enters the register the official series
are built from.** Slums housed on the order of 65-70 million people, roughly 17% of urban
population, on Census-2011-era definitions `[RECALL, low confidence; definitions vary across
notified/recognised/identified]`; Delhi's unauthorised colonies are a distinct category, on the
order of 1,700 settlements, whose residents were granted conditional ownership and registration
rights by the NCT of Delhi (Recognition of Property Rights of Residents in Unauthorized Colonies)
Act, 2019 — an admission that a very large stock sat outside registration for decades `[RECALL]`.
Partha Mukhopadhyay's CPR work with Marie-Hélène Zerah on **subaltern urbanisation** documents the
settlement-level version: much urban growth occurs in small and medium towns and census towns
without statutory urban-local-body status, while every official price series is metro-concentrated
`[RECALL]`. **A denominator problem, not noise: the engine's universe is the registered formal
market, and that is scope to state, not bias to correct.**

**Consultant assertion, and the most consequential gap in the India literature: there is no
recoverable peer-reviewed Indian hedonic estimate of an infrastructure premium.** The circulating
figures — "15-25% within 500m-1km of a metro corridor" — come from consultancy output with no
published method, no confounding-trend control and no stated area basis `[RECALL]`; C5 rightly
refused to name authors or magnitudes rather than risk fabricating them. **These are exactly the
coefficients an engine wants to import from "the literature", and the literature cannot supply
one.** Estimate them from scratch on acquired transaction data, or run a dedicated refereed search
city by city.

**Thin or unverifiable, listed so it is not mistaken for absence of evidence** — all `[RECALL]`, no
titles asserted: RBI DEPR house-price working papers (Snehal Herwadkar recalled as an author);
NIPFP on property taxation, municipal fiscal health and land value capture (Simanti Bandyopadhyay);
ICRIER on FDI, housing finance and REITs; the RBI Household Finance Committee report (2017, chaired
Tarun Ramadorai) and its finding that Indian household wealth is overwhelmingly physical with a
strikingly low financial-asset share; the HPEC urban-infrastructure report (chaired Isher Judge
Ahluwalia, ~2011; a 20-year need recalled near ₹35-40 lakh crore over 2012-2031, low confidence);
Bimal Patel's Gujarat **Town Planning Schemes** as the land-pooling alternative to eminent domain;
Annapurna Shaw's *Indian Cities* (~2012); Gilles Duranton on Indian city size and market access;
the World Bank's *Leveraging Urbanization in South Asia* (~2015). One naming flag: **do not present
Piyush Tiwari and the IIM Bangalore Real Estate Research Initiative as one item** — the auditor
places Tiwari at the University of Melbourne (D-14).

---

### 6. THE YIELD QUESTION

**Every Indian yield estimate this programme found belongs to one of two families that disagree by
2-3 percentage points and rank cities differently, and which family is right decides whether Indian
metros look priced at a historical top or a historical bottom.** The anchor is the desk's own print:
across the JST 18-country panel, property-boom **peak** rental yields ran a median **3.29% in the
modern era** (3.78% full sample) and **trough** yields **4.94% modern** (5.23% full) `[DESK PRINT,
CN-D2]`, verified verbatim against the ledger (C-14).

| Estimate | Level | As-of | Method | Family | Tag |
|---|---|---|---|---|---|
| India national | **5.16%** (from 5.09%) | Q2 2026 | Global Property Guide: median asking **rent** ÷ median asking **price**, full listing stock | 1 | `[1-SOURCE]` |
| Delhi; Kolkata | 5.81% / 6.19%; 5.79% / 6.32% | 2026 | GPG, plus a second aggregator on the same method, different cut | 1 | `[2-SOURCE on direction; points differ]` |
| Bengaluru | 4.45% (2024) → est. 4.6-5.0%; citywide 3.6%→4.6% 2019→Q2'26 | 2024-26 | Anarock survey; GPG city trend | 1+2 | `[2-SOURCE]` |
| Hyderabad | citywide 2.6%→3.6%; **IT corridor 3.8-4.2%** | 2026 | GPG trend; portal corridor estimate | 1+2 | `[2-SOURCE]` |
| **Mumbai citywide** | **3.84%** | 2026 | **GPG — a Family-1 figure** | **1** | `[2-SOURCE]` |
| **Mumbai premium corridors** | **2.0-4.0%** (SoBo/Malabar Hill 2.0-3.0, Bandra West 2.0-2.5, Powai/Chembur 3.0-3.5, Malad/Goregaon 4-5) | 2025-26 | Portal/broker micro-market surveys | **2** | `[1-SOURCE each]` |
| Pune | citywide 3.0-4.3%; Hinjewadi/Kharadi **4.0-4.4% one cut, 5.5-6% another** | 2024-26 | Portal aggregates | 2 | `[1-2 SOURCE, conflicting — unresolved]` |
| Chennai | 4.05-4.16% (from 3.78% a year earlier) | Q4 2025 | Magicbricks Rental Index | 2 | `[1-SOURCE]` |
| Ahmedabad; Gurugram; Noida; Lucknow (Gomti Nagar) | 3.9% (cited highest of any major city in that survey); 4.1%; 3.7%; ~3% | 2024-26 | Magicbricks/Business Standard; one syndicated broker-survey family; in-programme dossier | 2 | `[2-SOURCE]`; `[1-SOURCE]`; `[1-SOURCE]`; `[2-SOURCE, in-programme]` |
| Kochi (Kakkanad); Indore (Nipania / Super Corridor) | 4.6-6%; up to 8% (Super Corridor ~6%) | 2025-26 | In-programme screen §13 | 2 | `[1-SOURCE, in-programme]` |
| Surat (Sachin / Surat North) | 11-12% — **rejected, not adopted** | 2025-26 | The same portal prints 3-4% for other Surat localities; a 3-4x internal spread read as artefact | 2 | `[1-SOURCE, discarded]` |
| Numbeo | **no figure** | — | **No Numbeo India number survived any search pass**, and none is stated | — | omitted deliberately |
| Comparators | Taiwan ~1.9-2.3%; Singapore ~3.1%; China GPG ~2.6%; Shanghai price-rent 78-79 raw implying ~1.3-2%; prime London 3-4% | various | Same-method or cited | — | `[1-SOURCE]` each; India's GPG figure is **~2.0x China's** like-for-like `[COMPUTED]`. Philippines, Indonesia, Brazil, South Africa and Turkey did not surface and are deliberately absent |

**The verdict sentence has to be rebuilt, because the source version is a family blend — and fixing
it strengthens the warning.** C6's headline filed "Family 2's premium-corridor numbers (Mumbai
3.84%...)" near the peak band, but **3.84% is the GPG Family-1 citywide figure**, correctly filed as
such in C6's own opening paragraph (R13). The honest Family-2 Mumbai range is **2.0-4.0%**, which
does not sit near the modern peak band of 3.29% — it **straddles and undercuts it**. So: **the
micro-markets Indian investors actually transact in are priced at or through the level at which
property booms have historically topped out, while the national asking-price blend of 5.16% sits
above the level at which busts have historically ended.** Both readings come from the same country
in the same quarter, which is why no single "Indian rental yield" may be quoted without its family.

**Why they diverge, and the selection problem under both.** The most defensible unsourced
explanation is composition: GPG's median-of-listings method is diluted toward older, cheaper stock
with a structurally higher rent-to-price ratio, while portal city yields are built from newer,
higher-capital-value stock dominating transaction volume — the same gap the China programme found
between GPG and domestic-press figures. Beneath both: **NSSO found 71% of Indian rentals have no
written contract (2012) and only ~5% used formal agreements (2008-09), about a quarter of those
registered, with some states above 90% informal (AP and Telangana ~94%, Bihar ~92%)** `[2-SOURCE,
two rounds converging]`, and the **11-month lease is a deliberate registration and rent-control
workaround** `[2-SOURCE]`. Observed contract-bearing rents are a small, non-representative slice.

**Gross to net: no source has published an India net yield, so this waterfall is `[COMPUTED]` on
stated assumptions — illustrative, not measured.** Gross 4.0% on a value of 100, rent R = 4.0.

| Line | Units of value | Basis |
|---|---|---|
| Gross yield | **+4.00** | Representative prime-urban Family-2 level |
| Society / maintenance | −0.30 | ~7.5% of rent; **no separate tax deduction beyond the flat 30%** `[2-SOURCE]` |
| Property tax | −0.20 | **The weakest line.** 0.2% is a single Pune capital-value worked example, **not a national average**; the defensible read is **sub-1% of capital value**, so the true span runs to ~0.80 `[1-SOURCE]` |
| Vacancy | −0.30 | 7.5% of rent, practitioner cost-calculator input |
| Repairs / upkeep | −0.75 | **Illustrative, with no source at all — and the largest single deduction, 19% of gross rent** |
| Brokerage | −0.36 worst case | One month's rent at every 11-month renewal = 9.09% of R; ~0.14 amortised over a ~2.5-year tenancy |
| **Cash net, pre-tax** | **2.09** / **2.32** amortised | |
| Income tax | −0.76 | Section 24(a) allows a flat **30%** of Net Annual Value (rent minus municipal tax) **with no separate repairs deduction** `[2-SOURCE]`. Vacancy-adjusted NAV = (3.70 − 0.20) × 0.70 = 2.45; at 31.2%, tax = 0.764 |
| **After-tax, in-pocket** | **1.33** / **1.56** amortised | |

Two audit corrections are applied: C6 **deducted vacancy as a cash loss and then taxed the full
gross rent** (R14), and **31.2% is the no-surcharge rate** — the profile modelled, an unlevered
owner of a prime-urban investment flat, plausibly has income above ₹50 lakh and faces a 10/15/25%
surcharge tier, giving ~34.3-39% effective and an after-tax figure of roughly **1.18 down to 1.05**
`[RECALL, must-verify]` (D-09). C6 also called brokerage the most assumption-sensitive line; it is
third. **Property tax (span to ~0.80) and repairs (0.75, unsourced) are half the total deduction;
brokerage's 0.22 span is 19% of it** (R15). **Bounded verdict: on a 4.0% gross start an unlevered
top-bracket landlord nets roughly 1.0-1.6% of value per year after tax; a lower-bracket owner, one
amortising brokerage over a real tenancy, or one sheltering income through Section 24(b)'s uncapped
interest deduction on let-out property lands nearer the pre-tax cash 2.1-2.3%.** No line in that
range is an empirical measurement.

**Commercial: every listed Indian REIT yields below the 10-year G-sec on the same date, and this is
the best-sourced material in the India yield file.** The 10-year G-sec traded **6.96-7.10% in
September 2026** `[2-SOURCE]`.

| REIT | Type | Distribution yield on price | On NAV | Price vs NAV | Occupancy | WALE |
|---|---|---|---|---|---|---|
| Embassy Office Parks | Office | **5.75%** (FY26 ₹25.28 ÷ ₹439.6, 10-Sep-26) | 5.14% (NAV ₹491.62) | **−10.6%** | 90% (FY27 guided 95-96%) | 8.5y |
| Mindspace Business Parks | Office | **4.83%** (₹24.09 ÷ ~₹499, 2-3 Sep-26) | 4.57% (NAV ₹527.0) | **−5.4%** | 95.3% committed Q3FY26 | 6.9-7.4y |
| Brookfield India | Office | **6.24%** (₹21.40 ÷ ~₹343, 24-25 Aug-26) | 5.53% (NAV ₹386.7) | **−11.2%** | 96% committed FY26; ~93% enlarged Jun-2026 | 6.7y |
| Nexus Select Trust | Retail | **5.42%** (₹9.081 ÷ ₹167.5, 8-Sep-26) | 5.54% (NAV ₹164.00) | **+2.1% premium** — the only one | 97.2% (FY25) | not found |
| Knowledge Realty Trust | Office | Too new: ₹1.56 partial-period distribution on a ₹103 listing (18-Aug-2025), ~₹62,000 cr GAV | — | — | 92% H1FY26 (Hyderabad 99%, GIFT City 98%, Chennai 95%, Mumbai/Bengaluru/Gurugram ~88%) | not found |

Each leg `[1-SOURCE]`, yields `[COMPUTED]`; the audit recomputed every figure exactly and calls
this the most reliable section in the eight files (C-12). **Spread to the sovereign: −0.72pp at best
(6.24 − 6.96) to −2.27pp at worst (4.83 − 7.10)** `[COMPUTED]` (C-13) — **a starker negative carry
than China's own C-REIT-versus-bond gap at the top of its cycle.**

**Four limits, all pointing the same way.** (i) **The NAV-based yield is not a cap rate** — NAV nets
debt and a distribution is not NOI, so 4.57-5.54% is directional only; **NOI, gross asset value,
in-place-versus-market rent and market cap were not found for any of the five REITs in any pass**, a
gap cheaply closed from each trust's investor presentation. (ii) **Since-listing total returns are
the least reliable numbers in the file** — three of four carry internally inconsistent figures
(Brookfield's cited "+6%" fails arithmetic against its ₹279 debut; Nexus has three irreconcilable
figures), none adopted. (iii) **No residential or retail-residential REIT exists in India**
`[2-SOURCE, two independent legs]` — no listed residential proxy, so no residential cap-rate test is
possible at all. (iv) **Only SM REITs clear the G-sec, on prospectus projections.** SEBI notified
the framework in **March 2024** `[2-SOURCE]` — SPVs over single or few commercial assets of ₹50-500
crore, mandatory listing, 95% cash-flow distribution, ₹10 lakh minimum lot; every scheme found is
single-asset commercial office, projected **8.1-9.0%**, combined AUM "tripled to ₹1,070 crore"
`[1-SOURCE]`. Sub-two-year track records, never comparable to the large REITs as equivalent
evidence. **Publish no SM REIT scheme date or size from this pack**: the auditor recalls Platina as
India's first scheme (IPO December 2024, ~₹353 crore) with the Jul-2025 / ₹473 crore / 1.61x triple
belonging to Titania, which would make C6's own section internally impossible (D-04).

**Two literature findings bear on reading any of it.** Plazzi, Torous and Valkanov (2010), *Review
of Financial Studies*, find cap rates forecast realised returns well for apartments, retail and
industrial but **not offices, even in-sample** `[2-SOURCE via A2]` — and India's REIT sector is
almost entirely office. And Himmelberg, Mayer and Sinai (2005), *Journal of Economic Perspectives*,
the standard user-cost defence of a low-yield level, **failed a real out-of-sample test**: applied to
46 US metros before 2008 it judged most markets not overvalued immediately before a 30%-plus crash,
because its expected-appreciation input was fed by the bubble it was meant to test `[1-SOURCE via
A2]`. **A user-cost argument that India's compressed yields are justified carries the identical
self-referential failure and must not be the reason to dismiss the yield signal.**

**The route that could resolve this.** Maharashtra's registered leave-and-license system is the only
India source that could produce a transaction-based, locality-grain yield: rent registration is
compulsory and runs on the sale-deed sub-registrar geography, with Aadhaar e-KYC and no office visit
`[RECALL]`, and rent-agreement duty is low so under-declaration incentive is weaker than on sales
(an interpretation, not a source). **The sale-side half is already solved** by the free monthly
count-and-revenue channel `[DESK FILE]` (R18). **What remains genuinely unconfirmed is the rent side
— no published aggregate of counts, median rent, tenure or deposit has been located by any pass, and
no bulk route is known.** That gap, not the sale side, is the highest-value state-specific runsheet
row here.

---

### 7. WHAT IS NOT AVAILABLE ANYWHERE — THE RUNSHEET ROWS

| # | Gap | Cheapest route |
|---|---|---|
| 1 | A ward- or locality-level official price index (RBI HPI computes ward strata, publishes cities) | RTI or data-sharing request to RBI or a state Stamps department for the existing strata |
| 2 | Bulk or API access to registered-transaction microdata in any state | Per-record scripted retrieval on the principal's machine, ward by ward; or RTI |
| 3 | A persistent parcel identifier (survey, khasra, CTS, gat numbers do not compose) | Confirm ULPIN / Bhu-Aadhaar coverage |
| 4 | Any published leave-and-license rental aggregate | Maharashtra IGR, direct |
| 5 | RBI HPI's revision policy | Difference successive vintages of the same reference quarter |
| 6 | Whether RAPMS is a public series at all | One targeted check of RBI FSR and DBIE |
| 7 | QPR history retention on state RERA portals | One portal check per state |
| 8 | Bulk OC/CC issuance records | Municipal departments, city by city |
| 9 | Any peer-reviewed Indian infrastructure-premium hedonic coefficient | Estimate from scratch, or a dedicated refereed search |
| 10 | REIT NOI, GAV, in-place-versus-market rent, market cap | Each trust's own investor presentation |
| 11 | Census 2021 housing tables (the finest-grained stock data is ~15 years stale) | Confirm whether the round has been conducted or scheduled |
| 12 | Free gross home-loan disbursal data (only outstanding stock is free) | Use the Sectoral Deployment growth rate as a net-flow substitute, stated as such |

**The environmental gap governing all twelve: on 2026-09-11 the desk probed 37 endpoints from this
session and 36 were blocked at the proxy — every Indian official portal (data.gov.in, RBI DBIE, RBI
main, NHB RESIDEX, IGR Maharashtra, NGDRS, DILRMP, MahaRERA, Bhuvan, MoSPI), every private India
source probed (Magicbricks, Housing.com, Knight Frank India), and every international and
geospatial source. Only the GitHub control answered** `[DESK FILE, measured]`. Acquisition runs on
the principal's machine — a measurement, not a judgement call.

---

### WHAT THIS SECTION CHANGES ABOUT THE PLAN

1. **Build the RBI HPI dependent variable as two spliced series, not one**: 10-city / 2010-11 as the
   long history to 2025, 18-city / 2022-23 as the tail from Q1:2025-26, spliced
   `k = HPI_new(t0)/HPI_old(t0)`, both bases stored as separate vintages, never a Hamilton gap or
   percentile rank across the join. Delete every "ten cities, base 2010-11" description (§1).
2. **Replace "lag the last 2-3 quarters" with a vintage-differencing test** — store every vintage of
   every reference quarter from the first pull; no RBI revision policy is documented and the window
   in the dossiers was invented (§1).
3. **Write two ingestion constraints as hard rules**: the three price concepts never merge (RBI HPI
   registered, RESIDEX @ Assessment lender-valuation-at-sanction, RESIDEX @ Market listing/deal),
   with RESIDEX's two base breaks as separate vintages; and every series carries a loading factor L
   per city, **psf ratio = 1 + L, L up to 0.50 for Mumbai**, replacing the twice-refuted pack-wide
   "20-35%" constant (§1, §2).
4. **Re-order the Maharashtra build: the sale-side volume series is already free and cleaned, so
   spend the scraping budget on the ASR-to-consideration price ratio and the leave-and-license rent
   side** (§2, §6).
5. **Make every infrastructure feature a two-column event with the corrected dates, and mark
   Bengaluru PRR and Chennai Metro Phase 2 right-censored** — NMIA 25-Dec-2025, Jewar two zeros
   (28-Mar-2026, 15-Jun-2026), Samruddhi 5-Jun-2025, Coastal Road Ph.1 Aug-2025 with Ph.2 targeted
   Dec-2028; never a citywide metro dummy where corridor openings are years apart (§4).
6. **Make the 43CA/50C tolerance band time-varying — 5%, then 10%, then the 20% primary-sale-only
   window — verify it before anything else on the calendar, and register it as a break** alongside
   the Maharashtra 2020-21 stamp-duty holiday and the Gujarat 2023 jantri revision, in a registry
   that currently has no property-tax dimension at all (§4, §2).
7. **Score city supply elasticity on three layers — legal FSI cap, title and litigation friction,
   physical land availability — and treat the trade-press FSI ranking as a hypothesis.** Anchor
   Mumbai to Nagpal-Gandhi's +58% units / −24% prices only with its `[1-SOURCE]` unrefereed tag
   attached, carrying the ULCRA negative finding beside it with equal weight (§5).
8. **Estimate infrastructure and metro premia from scratch; import no consultancy percentage** — no
   peer-reviewed Indian hedonic coefficient was recoverable and the circulating "15-25% within
   500m-1km" figures have no published method (§5).
9. **Report every yield with its family, method and as-of date; publish the two-family conflict as
   the headline rather than a reconciled average, and always gross beside net.** Family-2 Mumbai
   corridors at 2.0-4.0% straddle and undercut the modern peak band of 3.29% while the Family-1
   national 5.16% sits above the modern trough band of 4.94%; on the net side, label property tax
   (one Pune worked example, true span to ~0.8% of value) and repairs (unsourced, the largest single
   deduction) as the two weakest lines, and state the after-tax band as ~1.0-1.6% for a top-bracket
   unlevered owner once the surcharge tiers are named (§6).
10. **Treat the whole India source estate as unreachable from any web session** — 36 of 37 probed
    endpoints were blocked at the proxy, so every acquisition step above is a principal's-machine
    task, and the twelve gap rows in §7 are the runsheet that task works from (§7).

---

## METHOD: HOW TO BUILD AND HOW TO JUDGE

*Sourcing status, once. The dossiers behind this section (`D1`–`D4`) ran **zero** live searches — the
session's shared WebSearch budget returned `200 of 200 used` before their first queries executed — and
`WebFetch` is egress-blocked. Every external claim carries **[RECALL — unverified]**; desk documents carry
**[FIRST-PARTY]**. `_AUDIT-3` is binding and applied: it corrected the pinball-loss formula (R16), the
CRPS constant (D-08), the carpet-loading factor (R19) and the Geltner venue (D-07), and established that
most of `D3`'s proposed protocol **already exists as desk machinery** (R17). Where `_AUDIT-3` gives its own
recollection as basis it labels that `[MODEL-MEMORY]` and calls it circular in its own basis table;
agreement between two model memories is noted below as concurrence, never verification.*

---

### 1. INDEX CONSTRUCTION FOR THIN CELLS

**No classical method survives a ward-quarter of tens of transactions, and the construction that does
survive is the one RBI already uses and does not publish.** RBI's House Price Index is a chain-linked
stratified index built from transaction-level data supplied by state Registration/Stamps Departments: **for
each ward/administrative zone and quarter**, properties are bucketed into three floor-space-area classes, a
simple average price per square metre is computed **per class per ward**, and classes recombine at weights
fixed to the April 2010–March 2011 transaction mix `[FIRST-PARTY:
research/cycles/fincycle-deep/partC-data.md §C.1]`. Carpet-area cut points are ≤60 / 60–110 / >110 sqm
`[1-SOURCE, A2.md §64]`. Ward strata therefore exist upstream of every number RBI prints, and `_AUDIT-3` R7
rules that calling sub-city granularity a *structural* ceiling is wrong — it is a **publication** ceiling.
An RTI or data-sharing request for strata already being computed is the highest-value acquisition route on
this engine, and it reframes the build as **replication at a finer grain, not invention**, with a free
validation target: an engine ward index aggregated at RBI's own weights must reproduce RBI's published city
index to within sampling error, or the replication is wrong.

#### 1.1 The method menu and the failure mode that binds

| Method | Reference `[all RECALL]` | Nets out | The failure mode binding at ward scale | Verdict |
|---|---|---|---|---|
| Repeat sales (BMN) | Bailey, Muth & Nourse (1963), *JASA* | Time-invariant unobserved quality | **Small-N starvation** — pairs are a subset of an already-small count; at ~30 sales/ward-quarter the within-window subset is near zero. Selects toward flipped/renovated stock | City cross-check only |
| Weighted repeat sales | Case & Shiller (1987 WP / 1989 *AER* 79(1):125–137) | + holding-period heteroskedasticity, 3-stage GLS | All of BMN's, plus a **revision problem**: a third sale re-anchors published history, so no vintage is final | Not backtestable |
| Hedonic, time-dummy | Rosen (1974), *JPE*; Hill survey (venue uncertain) | Measured characteristics, shadow prices fixed | Rigid — one set of implicit prices across the sample | **The pooling layer** |
| Hedonic imputation, per period | same | Prices free each period | DoF exhaust; one gated-community dummy perfectly separates; size/floor/age/transit collinear | **Never at ward level alone** |
| Raw median / mean | — | Nothing | **Composition** — a mix shift with zero appreciation moves the print | Forbidden as sole output |
| Stratified / mix-adjusted median | ABS RPPI (sub-region × dwelling type); UK ONS–HM Land Registry pre-hedonic | Composition, at **fixed** base-period weights | Strata themselves go thin; trades composition bias for sampling noise | **The floor**, per RPPI Handbook |
| Hybrid: pooled hedonic + RS time effect | Quigley (1995) (venue uncertain); an unnamed Case-coauthored companion | Both, from the whole sample | Inherits repeat-sales selection in the time effect only | **Fallback if linkage fails** |
| SPAR (sale price / assessed value) | de Vries, de Haan, van der Wal & Mariën (~2009), *JHE*; Clapp & Giaccotto (1992) | Size, location, quality already in the assessment; **no repeat match needed** | **Denominator staleness is the whole ballgame** — and in India the denominator is also the censoring threshold | **Primary candidate** |
| Fay–Herriot shrinkage | Fay & Herriot (1979), *JASA* | Sampling noise in the direct estimate | Shrinks real local moves toward the city mean; a bad prior is a bias | **A layer, never a rival** |
| Spatial SAR / spatial error | Pace & Gilley; Pace, Barry & Sirmans (particulars unconfirmed) | Spatially autocorrelated micro-amenity | Needs per-transaction geocoding India lacks; **W is a free parameter** | Later, W registered |
| GWR | Fotheringham, Brunsdon & Charlton (~2002) | Coefficients varying over space | **Bandwidth is a free parameter** — the researcher-degrees-of-freedom the no-magic-numbers rule forbids | Only with a registered bandwidth |

#### 1.2 The composition trap, proved on desk rather than argued

**This desk has already caught an unadjusted average hiding a crash.** The China Property Crash Atlas (row
64, CN-D programme) found China's national land-price series down only **~−23% from a 2023 peak** against
land-transaction **volume −66%** and **revenue −52.3%** in the same episode, and booked the shallow print
explicitly as **a composition artifact**: as distressed lower-tier parcels stopped transacting, the
surviving mix tilted toward better land `[INTERNAL, DESK-VERIFIED]`. That is the ward-median mechanism at
national scale. **Transaction count belongs in the same row as every price figure**, and mix-adjustment at
*fixed* base-period weights is the floor, not an option.

#### 1.3 SPAR on circle rate, fatal objection first

**The objection before the case: in India the SPAR denominator is the same administrative number the
numerator is censored at, so the ratio is contaminated by the evasion it would measure.** Circle rate /
ready reckoner / guidance value is functionally an assessed value for essentially every registrable parcel,
and declared consideration has historically clustered at or near it with a cash component absorbing the gap
`[RECALL — unverified as to magnitude]`. The ratio's *level* is jointly a price and a compliance signal.
Build it anyway, because the contamination is separable and the separation is the most valuable output
here — one linkage, **two** series:

| Output | Construction | Measures | Consumer |
|---|---|---|---|
| **S1 — price index** | Ratio index on the **uncensored region only** (clear of the local safe-harbour band, §2.6), assessment-vintage controlled | Price movement conditional on clearing the floor | The forecasting engine |
| **S2 — compliance index** | Excess mass in and below the band, per ward-year, normalised as in §2.5 | Evasion intensity and its regime shifts | The bunching estimator; the breaks registry; **the reliability weight on S1** |

S2 is not a by-product. It is the only defence against the failure `D2` identifies: the floor **mechanically
compresses observed variance**, so a naive model shows *low residual variance and high apparent fit exactly
in the heaviest-evading wards* `[RECALL, first-principles]` — any selection rewarding fit prefers the worst
data. SPAR's statistical case for thin cells is that ratio dispersion σ_r is smaller than price dispersion
σ_p (the assessment has absorbed size and location), so a precision target is reachable at smaller n —
entirely conditional on a current denominator, which in India it frequently is not:

| Jurisdiction | Denominator | Revision behaviour | Consequence | Tag |
|---|---|---|---|---|
| Netherlands (the SPAR template) | WOZ tax valuation | **Annual** | The precondition that makes SPAR work there | `[RECALL]` |
| New Zealand | Council rating valuation (QV) | Periodic revaluation | SPAR-like, weaker currency | `[RECALL, low]` |
| Maharashtra | Annual Statement of Rates | Broadly annual, skipped years | Best Indian case | `[RECALL]` |
| Gujarat | Jantri | **Frozen ~2011 for a decade; revision effective mid-April 2023, reported as roughly doubling statewide, non-uniformly by area** | A ~2x denominator step inside the sample — any ratio series crossing it without an era split is broken | `[RECALL]`, concurred `[MODEL-MEMORY]` (C-06) |
| Delhi | Circle rate, **eight categories A–H** | Infrequent | A **step function over ~8 bins** per property type — resolution-capped before staleness bites | `[RECALL]`, concurred `[MODEL-MEMORY]` (C-07) |
| Karnataka | Guidance value | Ward-level, irregular | Finer than Delhi, harder linkage | `[RECALL]` |

Hence a mandatory assessment-vintage field on every ratio record. `_AUDIT-3` C-06 also establishes a live
gap: `research/register/breaks-registry.md` carries BR1–BR9 with **no circle-rate, 43CA/50C or stamp-duty
entry at all** `[FIRST-PARTY]`.

#### 1.4 The recommended construction, and the smallest defensible cell

1. **Linkage layer** — match each transaction to its schedule cell (ward × property type × FSA band ×
   effective-date vintage). `D1` is right that this, not the statistics, is the primary engineering problem:
   India lacks a unified parcel ID `[RECALL]`.
2. **Mandatory fields before any computation** — area basis; assessment vintage date; registration date *and*
   transaction date separately; transaction channel (private resale vs. RERA-disclosed
   builder-to-first-buyer). The last is what §2.5's segmentation needs and cannot be reconstructed later.
3. **Base method** — SPAR ratio index within ward × FSA band, chain-linked at fixed base-period weights:
   RBI's own construction with the ratio substituted for the level.
4. **Shrinkage layer** — Fay–Herriot empirical Bayes toward the city/zone prediction, strength set by each
   ward's own sampling variance. **Suppression**: cells below the registered N threshold are shrunk and
   flagged or rolled up, **never published raw**. **Two outputs always** — S1, S2, and the count column.
5. **Splice discipline** — anchoring to RBI HPI uses the rule already written: legacy 10-city / 2010-11 base
   as the long history (native start **June 2010**, Q1:2010-11, ~61 quarters to Q1:2025-26); 18-city /
   2022-23 base as the current tail from the **2025-10-10** release for Q1:2025-26; splice by
   ratio-at-overlap `k = HPI_new(t0)/HPI_old(t0)` `[FIRST-PARTY: partC-data.md §C.1]`. **Never fit a
   Hamilton gap or a percentile rank through the break**, at which eight cities silently appear (Hyderabad,
   Thiruvananthapuram, Pune, Ghaziabad, Thane, Gautam Buddha Nagar, Chandigarh, Nagpur).
6. **Lag and vintages** — treat **8–13 weeks** as the working range, not a point figure (Q1:2026-27, quarter
   ended 2026-06-30, released 2026-08-24, ~8 weeks) `[FIRST-PARTY]`. **No RBI revision policy is
   documented**; difference successive vintages of the same reference quarter and measure it. `_AUDIT-3`
   D-01 deletes the "last 2–3 quarters are provisional" rule of thumb as an invented window.
7. **Never blend price concepts.** NHB RESIDEX publishes **two structurally different indices in parallel** —
   HPI @ Assessment Prices (bank/HFC valuation, a lender's loan-sanction number) and HPI @ Market Prices
   (primary under-construction and secondary resale listing/deal data) — over **50 cities (18 State/UT
   capitals plus 37 "smart cities", with overlap)**, and it is **active, not discontinued**, quarterly
   through at least Q1 2026 `[FIRST-PARTY: partC-data.md §C.2]`. Neither leg may be blended with RBI's
   registration-price-only HPI, and a persistent gap between the legs is **a divergence to log, not an
   inconsistency to reconcile away**.

**Smallest defensible cell.** `D1` declines to state any agency's published minimum and flags it as an open
question `[RECALL]`; inventing one breaches the no-magic-numbers rule. Make it a function of a
pre-registered precision target: for a cell log-mean, SE ≈ σ/√n, so n ≥ (σ/s\*)².

| Within-cell log dispersion σ | s\* = 2% | s\* = 3% | s\* = 5% |
|---|---|---|---|
| 0.25 | 156 | 69 | 25 |
| 0.35 | 306 | 136 | 49 |
| 0.45 | 506 | 225 | 81 |

**σ is itself unmeasured** and must come off the first linked extract before the threshold is fixed. But the
shape is already clear: at any plausible σ a **ward × quarter × FSA-band** cell is never publishable alone.
The smallest defensible *published* unit is a **ward × rolling-four-quarter window, FSA bands recombined at
fixed weights, n ≥ 50, count printed**; thinner cells live in the model as shrunk latent quantities. SPAR's
smaller σ_r is what makes n ≥ 50 reachable.

**Area basis, as a gate.** Carpet-to-super-built-up loading is **~25–35% typically, 40–50% in Mumbai**
`[1-SOURCE, A2.md §72]`. `_AUDIT-3` R19 refutes the "~1.2–1.4x" rule of thumb `D4` carried — understating
the primary market by up to ~10pp at the top — and prescribes **psf ratio = 1+L, L up to 0.50 for Mumbai**.
RERA (2016) mandates carpet-area disclosure for registered primary projects; resale and pre-RERA stock still
quote super-built-up `[RECALL on scope]`. An unstated basis switch alone moves a per-square-foot figure by
up to half.

---

### 2. THE CENSORED-REGRESSION AND BUNCHING TOOLKIT

**The tractable feature is that the censoring point is observed; the intractable one is that it is
endogenous.** `observed = max(true_price, c_it)`, where `c_it` is a real, published, ward-and-time-varying
Sub-Registrar schedule, not a latent threshold to be estimated. Every estimator below exploits that and
every one assumes `c_it` is **exogenous once observed** — while circle rates are typically set by
extrapolating from *past registered*, already-censored, transactions `[RECALL]`. That floor-chasing-floor
dynamic is assumed away by Tobin, Powell, Honoré and the bunching literature alike and is the largest
unhandled risk here; test whether revisions Granger-cause or merely lag past bunching mass before trusting
any of it forward.

#### 2.1 The likelihood with an observed, time-varying threshold

With `y*_it = x_it'β + u_it`, `u_it ~ N(0,σ²)` i.i.d., `c_it` observed without error, `y_it = max(y*_it, c_it)`:

```
ln L(β,σ) = Σ_{uncensored} [ −ln σ + ln φ( (y_it − x_it'β)/σ ) ]
          + Σ_{censored}   ln Φ( (c_it − x_it'β)/σ )
```

— textbook Tobit with the fixed limit `0` replaced **everywhere** by `c_it`. This is Amemiya's Type I with a
unit-varying limit; Amemiya (1984), *Journal of Econometrics* 24 is explicit that the censoring point need
not be zero or constant `[RECALL]`. Founding case Tobin (1958), *Econometrica* 26(1):24–36; variable-limit
treatment in Maddala (1983), *Limited-Dependent and Qualitative Variables in Econometrics*, CUP, ~ch. 6
`[RECALL, chapter uncertain]`. Two notes change what gets reported. **Wooldridge's "corner solution"
justification does not apply** — no seller optimally chooses the circle rate; it is a legal artifact
`[RECALL]` — which is why §2.4 is live: the engine borrows Tobit's mechanics and none of its behavioural
rationale. And raw `β_j` is the effect on **latent** `y*`; McDonald & Moffitt (1980) decompose
`∂E(y|x)/∂x_j = Φ(x'β/σ)·β_j` into extensive and intensive margins `[RECALL]`. **This cuts favourably** —
the target *is* true price, so the unscaled `β_j` is wanted; the trap bites only if a fitted Tobit is reused
to predict *registered* price (a stamp-duty-revenue forecast) without rescaling.

#### 2.2 Why plain Tobit MLE is fragile, and the ladder

Tobit MLE is efficient only under i.i.d. normal homoskedastic errors. Real-estate dispersion scales with
price level, and the true-price-versus-circle-rate gap is the object of interest — a bad thing to assume the
shape of upfront. The whole quantile family follows from one line: the median commutes with censoring, so
`median(max(y*,c)|x) = max(median(y*|x), c)`.

| Estimator | Reference `[all RECALL]` | Assumption | Identified | Breaks on |
|---|---|---|---|---|
| Tobit MLE | Tobin (1958) | i.i.d. normal, homoskedastic | `β`, `σ` | Heteroskedasticity and fat tails, both near-certain |
| CLAD | Powell (1984), *J.Econometrics* 25(3):303–325 | **Conditional median only**, `median(u\|x)=0` | `β` at the median | **Fails where over half a ward-period sits at or below its own circle rate** — the median is itself censored and unidentified |
| Censored quantile regression | Powell (1986), *J.Econometrics* 32(1):143–155 | Conditional quantile restriction | `β_θ` wherever `Q_θ(y*\|x) > c_it` | Only quantiles clearing the **local** censoring share; a heavily-evading ward yields the upper tail only |
| Three-step CQR | Chernozhukov & Hong (2002), *JASA* 97(458):872–882 | As Powell (1986) | Same, at realistic scale | Fixes non-convexity of Powell's objective; the classification step is a design choice |
| Trimmed LAD/LS, fixed effects | Honoré (1992), *Econometrica* 60(3):533–565 | `u_it` exchangeable across `t` within `i` given `(x_i,α_i)`; **not** normal | `β`, with `α_i` differenced away | ≥2 transactions/ward across different circle-rate regimes; no closed-form SEs (bootstrap) |
| Two-limit probit | Rosett & Nelson (1975), *Econometrica* `[lowest confidence]` | — | Both-sided limits | Reserved for §2.4's buyer-side structure |

#### 2.3 The fixed-effects problem and Honoré's answer

Ward fixed effects plus censoring is a textbook **incidental-parameters problem**: with fixed `T` and `N→∞`
wards, dummying out every `α_i` in a Tobit MLE is inconsistent, because more wards add no information about
any single `α_i`. Honoré (1992) solves it semiparametrically — using **pairs of periods within the same
ward**, assuming only exchangeability of `u_it` across `t` within `i`, he builds a trimmed objective over
censored/uncensored pair comparisons whose expectation depends on `β` but **not** `α_i` `[RECALL]`.
**The open question is load-bearing**: `D2` records that the canonical exposition, to its recollection,
normalises the censoring point to a constant, and that extending it to a genuinely period-varying `c_it` is
a natural but nontrivial extension rather than something the 1992 paper states `[RECALL]`. The schedule
*moves* by design, and in Gujarat it moved ~2x (§1.3). Either the result already covers a freely
time-varying threshold and the ward-FE design lifts directly, or it needs its own methods note. **This is
the single highest-value item on the verification queue.**

#### 2.4 Selection is a different animal from censoring

**Decide this in writing before code, because no estimator above will flag a wrong choice.** In Tobit one
latent index determines both whether the uncensored value is observed and what it is; in Heckman (1979),
*Econometrica* 47(1):153–161 two equations — participation and outcome — are linked through their errors'
joint distribution `[RECALL]`. The `max(true,c)` structure is pure Tobit **only if** under-reporting is
driven by the same unobservables as true price. It plausibly is not: evasion depends on seller liquidity,
unaccounted buyer funds, enforcement intensity, and whether the sale is RERA-disclosed builder-to-first-buyer
(hard to under-report) or private resale (easy). If those correlate with the true-price error the honest
structure is two-equation, needing an exclusion restriction — RERA-disclosure status, or an
enforcement-regime change, as a determinant of evasion but arguably not of value.

#### 2.5 Bunching: the mass at the floor as an evasion measure

**The excess density at the floor is an estimator, not a nuisance.** Saez (2010), *AEJ: Economic Policy*
2(3):180–212 showed excess mass at a tax kink identifies the reporting elasticity without an external
experiment — the kink *is* the experiment — and that bunching is large among the self-employed, who control
their own reported income, and small among third-party-reported wage employees `[RECALL]`. **Private resale
versus RERA-disclosed builder sale is the India analogue**, and must be a field from the first extract.

Recipe, India modification at step 2: (1) **normalise to each unit's own threshold** —
`z_it = (observed − c_it)/c_it` or `log(observed/c_it)` — re-centring every ward-year's notch to zero before
pooling, per Kleven (2016), *Annual Review of Economics* 8:435–464 on heterogeneous notches `[RECALL]`; (2)
choose an excluded window wide enough for the spike, the dominated region above it, **and the entire
proportional safe-harbour band** (§2.6); (3) fit a flexible polynomial (commonly order 5–7) to bin counts
*outside* the window; (4) predict counterfactual counts inside from the polynomial alone; (5) excess mass =
observed − counterfactual over the window; (6) normalise by average counterfactual density near `z*=0` to
get `b` in bin-width units; (7) bootstrap residuals for standard errors `[RECALL as description; the
substance is widely-replicated methodology]`. Chetty, Friedman, Olsen & Pistaferri (2011), *QJE*
126(2):749–804 formalise the counterfactual density and show **optimisation frictions** mean observed
bunching **understates** the frictionless response `[RECALL]` — a seller may not know the current rate, or
the deal is struck in round numbers. **So S2 is a lower bound and must be reported as one.**

**Circle-rate registration is a notch, not a kink.** Kleven & Waseem (2013), *QJE* 128(2):669–723
distinguish a notch (a jump in *total* liability) from a kink (a jump in the *marginal* rate), show a notch
creates a theoretically empty **dominated region** just above it, and use bunching mass plus
dominated-region occupancy to separate elasticity from frictions `[RECALL]`. 43CA/50C/56(2)(x) impose a
discrete liability jump, so **occupancy just above the danger zone reads as frictions, not as "no
evasion."** Two precedents bound the design: Best & Kleven (2018), *Review of Economic Studies*
85(1):157–193 — UK Stamp Duty Land Tax notches, sharp bunching below each threshold, a stimulus-driven
threshold change used to identify the reporting elasticity — is structurally the closest external analogue
in the toolkit; and Kopczuk & Munroe (2015), *AEJ: Economic Policy* 7(2):214–257 on New York's $1m mansion
tax documents **transaction splitting** (personal property carved into a side contract) and **reduced
volume** near the notch, not merely relocated prices `[RECALL]` — a mechanism that biases **any
registered-price-only source**, not just the floor mass. **One placebo nobody has designed**: Indian circle
rates are set in round per-square-foot units and prices independently heap at round numbers (₹50 lakh, ₹1
crore), so where a ward's rate sits near a round number heaping and bunching are hard to separate
`[RECALL, general inference]`. Test bunching intensity in wards whose rate is **not** near a round number.

#### 2.6 What the safe-harbour band does to the shape

**A hard notch predicts a spike; India's proportional tolerance band predicts a plateau — so a notch-width
excluded window contaminates the counterfactual with real plateau mass and understates excess mass.**
43CA/50C deem the circle-rate value to be the consideration when actual consideration is lower, **unless**
actual consideration is not less than a tolerance band below it; 56(2)(x) mirrors it on the buyer's side
`[RECALL, mechanism at moderate confidence]`. The ladder is **time-varying**:

| Rung | Tolerance | Scope | Instrument | Tag |
|---|---|---|---|---|
| 1 | ~5% | General | Finance Act 2018 | `[RECALL]`, concurred `[MODEL-MEMORY]` (C-10) |
| 2 | ~10% | General | Finance Act 2020 | same |
| 3 | **~20%** | **Primary sales of residential units by builders only, ~₹2 crore cap** | 12 Nov 2020 ("Aatmanirbhar Bharat 3.0") to 30 Jun 2021, legislated in Finance Act 2021 | same |

`_AUDIT-3` C-10 calls this the best-reasoned item in its eight-file scope because it identifies a statutory
parameter as **the free parameter of the econometric design**. **A fixed band across a multi-year sample
misspecifies the design.** Three consequences: the excluded window must span the full band, edge to edge,
per ward-year at that year's tolerance; **the plateau's width should shift with the tolerance at each change
date** — a clean quasi-event study the desk gets for free and has not designed; and **rung 3 is a
triple-difference by construction** (builder primary sales only, under a ₹2 crore cap, eight months), the
sharpest identification here if the dates verify. Pin every percentage and date to a Finance Act section
first, per the BR4/BR6/BR7 precedent `[FIRST-PARTY]`.

#### 2.7 What is recoverable, and what is not

| Object | Recoverable? | By what | Binding limit |
|---|---|---|---|
| True-price distribution **above** the local threshold | Yes | Powell CQR / Chernozhukov-Hong; Honoré with ward FE | Only at quantiles clearing the **local** censoring share |
| Ward-FE-purged slopes | Yes | Honoré (1992) | ≥2 transactions/ward across regimes; bootstrap SEs; the §2.3 question |
| Aggregate excess mass; an implied evasion elasticity | Yes | Saez / Kleven-Waseem, under structure | **A lower bound**, because of frictions |
| The **median or below** where local censoring exceeds 50% | **No** | — | Unidentified by CLAD/CQR; the recoverable region may sit far up the tail, not at the "typical price" the engine wants |
| Any **individual** censored transaction's true price | **No** | — | These estimators identify functions — a quantile, a slope — never a latent individual value |

Individual truth needs an anchor outside the toolkit: matched bank/HFC loan-sanction valuations (carrying
RESIDEX's Assessment-leg bias, §1.4 item 7), RERA-filed builder price lists for the same unit, or a
structural evasion model with its own untestable exclusion restriction. **And the bias from ignoring this is
directional, not noise.** Classical measurement error in the dependent variable is *free* in slope terms —
only residual variance grows `[RECALL, standard textbook]` — which is why "noisy data" intuitions are
dangerously optimistic. Circle-rate censoring is **one-sided** and **mean-dependent on X in a structured
way**: `E[y_obs − y_true|X] = E[max(0, c(X,t) − y_true)|X]`, largest exactly where X implies a true price far
below its own ward's circle rate. A naive model is **flattened and shifted toward `c(X,t)` precisely in the
fast-moving, under-assessed micro-markets the desk most wants right** `[RECALL, first-principles]`.

---

### 3. THE EVALUATION PROTOCOL

**The famous result that failed out-of-sample, and the reason this section exists: Goyal & Welch (2008),
*RFS* 21(4):1455–1508 found virtually every textbook equity predictor fails OOS against the historical mean
`[RECALL]` — and this desk reproduced the same failure on its own work.** The ER-arc's pooled five-factor
equation printed 26.7% in-sample at 10y then **failed OOS at both horizons** once purged and honestly
benchmarked (ER-D4b correction box); single-country kitchen sinks exploded to **−389%**; the 10y "survives"
claim was **WITHDRAWN** `[FIRST-PARTY]`. House prices need a **stricter** standard, because the target is far
more autocorrelated and naive benchmarks are correspondingly easier to beat by accident.

**The machinery already exists — do not re-specify it.** `_AUDIT-3` R17 binds: `D3` presented
purged-and-embargoed CV and the deflated Sharpe ratio as **new discipline to adopt**; both are already on
disk, and process note #6 makes using them mandatory — *"use `quant/stats/` machinery, never inline
re-implementations."*

| Need | Desk module `[FIRST-PARTY]` | What it encodes that `D3` never stated |
|---|---|---|
| Purged, embargoed K-fold CV | `quant/stats/cv.py` — `purged_kfold()`, `assert_no_leakage()` | **Embargo ≥ 1× tau_half, 2× for Tier B/C, passed from the registry** ("this module never chooses it"); **4–6 folds for India-only monthly series, NOT a textbook 10** |
| Walk-forward folds | `quant/validation/walkforward.py` — `walkforward_folds()` | Expanding train; boundaries **deterministic** from (n, n_folds, min_train, embargo), so placement cannot be tuned toward a result |
| Trial-count-aware significance | `quant/stats/dsr.py` — `deflated_sharpe_ratio()`, `census_n()` | `census_n()` reads the cumulative trial count **programmatically from `trial-ledger.md`, never typed by hand**. Its own header carries a `[VERIFY]` — constants not yet pinned to Bailey & López de Prado (2014), *JPM* 40(5):94–107 — so **read DSR as a selection-bias-aware screen, not a precision p-value** |
| Train-only preprocessing | `quant/stats/preprocess.py` | Process note #8, booked after the 2026-09-05 audit found full-sample clip bounds in legs labelled "no-lookahead" |
| The embargo parameter | `quant/stats/tau_half.py` | Derived from signal half-life, not chosen |

#### 3.1 The numbered procedure this desk will be held to

| # | Step | Authority `[all RECALL unless marked]` | Why it binds here |
|---|---|---|---|
| 1 | Pre-register three benchmarks before any locality number is computed: unconditional mean (**soft — report, never lead with**), **random walk / no-change (binding)**, naive own-history AR(1) | — | Benchmark choice is the snooping axis the ledger does not yet police |
| 2 | **Never report accuracy against the unconditional mean alone** | Case & Shiller (1989), *AER* 79(1):125–137 (positive serial correlation); Geltner (1989) on appraisal-based real estate return risk — `_AUDIT-3` D-07 **drops the *Real Estate Economics* limb** (that journal did not exist under the name until the 1995 *AREUEA Journal* renaming); check the AREUEA limb | Indices are mechanically **smoothed**, manufacturing spurious serial correlation on top of genuine persistence. A model echoing last period scores well while forecasting nothing |
| 3 | Fix the rolling-window length by pre-registration | Rossi & Inoue (2012), *JBES* 30(3):432–453 (sup statistic if sensitivity must be examined) | Results flip on window length; reporting the best is snooping over window size |
| 4 | Spatial blocking (whole cities/states) **crossed with** purged-and-embargoed temporal folds. **Random k-fold banned** | Roberts et al. (2017), *Ecography* 40(8):913–929; López de Prado (2018), *Advances in Financial Machine Learning* | A held-out point's neighbours stay in training — that tests interpolation, not extrapolation. Purging/embargo closes a **different** channel; both are needed. Implement via the modules above |
| 5 | **Clark & West (2007), *J.Econometrics* 138(1):291–311 — not plain DM — whenever the benchmark is nested**, which the random walk always is | Clark-West (2007); West (1996), *Econometrica* 64(5):1067–1084 | Under MSE loss estimation noise biases plain Diebold-Mariano **against** the larger model even under an equal-accuracy null. The most load-bearing citation here |
| 6 | Apply the small-sample correction by default: scale by `sqrt[(T+1−2h+h(h−1)/T)/T]`, use **t(T−1)** not normal | Harvey, Leybourne & Newbold (1997), *IJF* 13(2):281–291 | DM over-rejects at short samples and longer horizons; per-locality India histories are short |
| 7 | Use a conditional test for every state-conditional claim | Giacomini & White (2006), *Econometrica* 74(6):1545–1578 | DM/CW ask an unconditional question; "beats the RW only in post-bust states" is a different question |
| 8 | Control multiple testing; **publish the expected false-discovery count beside any "N localities beat the benchmark" headline** | Benjamini & Hochberg (1995), *JRSS-B* 57(1):289–300 (exploratory screen); Romano & Wolf (2005), *Econometrica* 73(4):1237–1282, Hansen (2005), *JBES* 23(4):365–380, White (2000), *Econometrica* 68(5):1097–1126 (FWER before any headline); Hansen, Lunde & Nason (2011), *Econometrica* 79(2):453–497 (Model Confidence Set) | Arithmetic, not a citation: 300 localities at α=0.05 under a global null gives an **expected 15** significant results, **30** at α=0.10 — and shared regional shocks make the realised count more volatile and clustered than that binomial baseline |
| 9 | Plot the cumulative SSE-difference curve `Σ_{s≤t}[e²_bench,s − e²_model,s]` for every promoted model | Goyal & Welch (2008) | Their own diagnostic showed apparent predictability concentrated in one or two episodes and erasable in a short stretch. **A "beats the RW" number carried by one boom quarter is not skill** |
| 10 | Impose sign and plausibility restrictions **before** evaluation, never as a post-hoc rescue | Campbell & Thompson (2008), *RFS* 21(4):1509–1531 | A −40%/+60% YoY locality forecast is a model red flag, not a delivered number |
| 11 | Score distributionally: pinball across a quantile grid, plus CRPS. **`QL_τ(q̂,y) = τ(y−q̂)` if `y ≥ q̂`, `(1−τ)(q̂−y)` if `y < q̂`; compact `(y−q̂)(τ − 1{y<q̂})`; `CRPS = 2∫₀¹ QL_τ dτ`** | Gneiting & Raftery (2007), *JASA* 102(477):359–378; corrections per `_AUDIT-3` R16 and D-08 | `D3`'s published pinball formula had a sign error making it **not a loss function** — negative loss below the quantile, rewarding over-prediction. The factor of 2 in CRPS is not optional. Point forecasts are forbidden here (ER-arc doctrine; SNAPSHOT-1's refusal of a 1y/3y number) `[FIRST-PARTY]` |
| 12 | Publish a PIT histogram with a uniformity test for every promoted model | Gneiting, Balabdaoui & Raftery (2007), *JRSS-B* 69(2):243–268 | Maximise **sharpness subject to calibration**. **U-shaped = overconfident; hump = underconfident; sloped = biased.** Excellent mean accuracy coexists routinely with badly miscalibrated intervals |
| 13 | Reconcile locality/city/state/national levels via **MinT** before publication | Wickramasuriya, Athanasopoulos & Hyndman (2019), *JASA* 114(526):804–819; Hyndman, Ahmed, Athanasopoulos & Shang (2011), *CSDA* 55(9):2579–2589 | Independent level forecasts do not sum coherently. Free bonus: a locality forecast inconsistent with its own city aggregate is flagged by construction |
| 14 | Deflate any risk-adjusted or timing statistic via `dsr.py`, `census_n()` supplying the count | Bailey & López de Prado (2014) | The desk's own grids (OP-D3b, OP-D7, sweep 2) **each refused their train winners OOS** `[FIRST-PARTY]` — that is the base rate to expect |

`_AUDIT-3` C-16 found all twenty of `D3`'s citations matching its own recollection on author, year, journal,
volume, issue and pages, with the HLN factor, the BH step-up rule, the multiple-testing arithmetic and the
PIT reading structurally correct and **no fabrication signature anywhere** — the cleanest citation file
across three audited packs. That is two model memories agreeing, not verification; everything above stays
`[RECALL — unverified]`. One candidate upgrade: `D3`'s weakest item, the ~2024 Goyal-Welch extension with an
unconfirmed third author, is most likely **Goyal, Welch & Zafirov, "A Comprehensive 2022 Look at the
Empirical Performance of Equity Premium Prediction," *Critical Finance Review* (2024)** `[RECALL; C-17 calls
this an under-claim and a candidate upgrade, not a refutation]`. It matters because it says the OOS collapse
is not a one-decade fluke later data reversed.

---

### 4. THE FREE GEOSPATIAL STACK

**The trap is the point-in-time column, and three products fail it in the same direction — stale or
model-extrapolated information under a recent-looking label.** `_AUDIT-3` C-19 names those channels as
`D4`'s strongest contribution: Microsoft's footprints carry mixed imagery vintage tile by tile, OSM "first
appears" dates are edit dates not construction dates, and WorldPop/HRSL *levels* are census-anchored to 2011
under a recent vintage label.

| Product (publisher) | Resolution | Temporal coverage | Licence | PIT vs revised snapshot — the trap |
|---|---|---|---|---|
| **GHS-BUILT-S / -V** (EU JRC, GHSL) | 100m; a ~10m Sentinel-2 layer for one epoch (~2018) only | 5-yr epochs **1975–2030** | **CC BY 4.0**, cleanest here | **True series**, each epoch dated. **Trailing 2025/2030 epochs are partly model-projected — exclude from as-of features.** -V is a volume/height proxy, still not saleable area |
| **GHS-POP** (JRC) | 100m / 1km | Same epochs | CC BY 4.0 | **Derived from the built-up layer** — not an independent population source; pairing it with BUILT-S as separate regressors risks collinearity |
| **GHS-SMOD / GHS-UCDB** (JRC) | Grid / vector table | Same epochs | CC BY 4.0 | Urban/cluster/rural labels independent of India's inconsistent urban definitions; UCDB gives a city-level India panel with no raster work |
| **OpenStreetMap** (Overpass; Geofabrik daily India `.pbf`) | Vector | Panel buildable from successive dated extracts | **ODbL**; share-alike attaches to the database, statistical outputs generally treated as an exempt "produced work" — **get counsel** | Dated extract is a genuine snapshot, but **edit date lags construction by years**. Density tracks **mapper population**, not settlement; HOT mapathons (2018 Kerala floods, Bihar) create local halos |
| **WorldPop** (Southampton); **Meta-CIESIN HRSL** (HDX) | 100m–1km; ~30m | Multiple annual products; snapshot | Generally CC BY 4.0; Meta D4G terms | **Levels stale-anchored** to the underlying census (almost certainly 2011); the embedded *growth pattern* is the more trustworthy signal |
| **Google Open Buildings** | Polygon + confidence | Africa ~2021; South/SE Asia expansion ~2023. **India inclusion and vintage NOT confirmed** | `D4` recalled CC BY 4.0; **D-06 recalls dual CC BY 4.0 *and* ODbL — if so the Google-vs-Microsoft licensing contrast is weaker than `D4` claims** | **Not a series** — mixed-vintage patchwork |
| **Microsoft Global ML Building Footprints** | Polygon | Country-by-country; India recalled included | **ODbL** — matters more than for OSM, this being machine-generated data fed straight into a model | **The strongest trap here: vintage is mixed and imagery-source-dependent. Do not date it by the GitHub release date** |
| **VIIRS DNB** (EOG, Colorado School of Mines / Payne) | ~500m | Annual & monthly composites, ~2012→ | Open | **Among the cleanest true series here** — dated, essentially non-revised. **Except** that any *harmonized* pre/post-2013 value uses both sensor eras to fit its calibration |
| **DMSP-OLS** | ~1km | 1992–2013 | Open | Saturates in bright cores; **not concatenable** with VIIRS without an explicit intercalibration model |
| **Sentinel-1/-2** (ESA/EU Copernicus); **Landsat** (USGS) | 10m SAR / 10–60m optical; 30m | 2014/15→; continuous since the early 1980s | Free open Copernicus; free via **EarthExplorer** since the ~2008 policy change | Scene-dated, clean. Copernicus access moved from the decommissioned Open Access Hub to the **Copernicus Data Space Ecosystem** |
| **SRTM / ASTER GDEM / Copernicus DEM** | 30m / ~30m / 30–90m | **SRTM is a single mission flown February 2000**; ASTER v2/v3; CopDEM from TanDEM-X imagery ~early-mid 2010s | Open (GLO-30 fully open only after an initially restricted period) | **All static snapshots, not series. Cannot detect new construction or grading** — that job belongs to GHSL and the footprint layers |
| **ESA WorldCover** | 10m, 11 classes | **Two epochs only (2020, 2021)** | CC BY 4.0 | **Two-snapshot comparison, not a dense series.** D-16 concurs from memory but flags this as a **negative claim about a live product made from a Jan-2026 cutoff — a 2022+ release would change the recommendation. Cheap to check** |
| **Google/WRI Dynamic World** | 10m, 9 probabilistic classes | Near-continuous, ~every Sentinel-2 scene (~5-day), back to **~June 2015** | Via Earth Engine | Clean if the scene date is used correctly. **This is the dense land-cover series; WorldCover is the two-snapshot check** |
| **ISRO Bhuvan** (NRSC) | LULC national ~1:250,000, finer for select cities | Unclear | Indian government | **Access is the weak point, not content** — much is view-only tiles; higher-resolution layers historically needed registration with stated purpose and approval delay. Vintage often unstated |
| **Census of India** (DCHB Town/Village Directory) | Village / town / ward | **Frozen at 2011 — Census 2021 postponed and, to recollection, not conducted** | Government | **15-year-stale levels.** Worse: **municipal wards are redrawn by state delimitation tied to local-body elections, unsynchronised with the Census**, so a Census-era ward shapefile may not match the governing geometry |
| **SHRUG** (Asher, Lunt, Matsuura, Novosad / Development Data Lab) | Village / town | Links Indian administrative units across Census years under a stable identifier; bundles nightlights + Census indicators | Unconfirmed | **Close to a ready-made answer to the crosswalk problem** — try it before hand-rolling. C-20 calls it the highest-value item in `D4` if it verifies |
| **data.gov.in / `api.data.gov.in`** (NIC/MeitY, NDSAP 2012) | Varies | Varies | Open data, free rate-limited key | **Treat any dataset as a static one-time upload unless its metadata states a cadence** — the "revised snapshot masquerading as a live feed" risk |
| **India Post Pincode Directory**; **DataMeet** polygons | Flat table, **no geometry**; community shapefiles | — | Government; community | **India Post has never published official pincode polygons.** Every circulating boundary is derived — Voronoi around post-office points, aggregation of finer units, or vendor hulls — and they disagree at the margins. Pincodes are delivery catchments, not nested in wards |
| **City GTFS** (BMTC, Chennai MTC, Kochi; Delhi and Mumbai BEST less consistent) + OpenTripPlanner / R5 | Route/stop | Nominally current; **feeds go stale silently** | Varies | **Stamp every isochrone with the feed's vintage date** — a stale feed understates accessibility exactly where transit is newly expanding and value rising. Check the **Mobility Database** |
| **CPCB CAAQMS / OpenAQ**; ward election / water / electricity | Station level; — | Continuous; — | Government; open | CPCB skews to large cities. Ward-level election, water and electricity are **effectively unavailable as free feeds** — elections run through separate State Election Commissions, often as static PDFs; no national ward-granular DISCOM or water dataset. A gap, not a locked door |

*Every row `[RECALL — unverified]` except where a `[MODEL-MEMORY]` audit note is named.*

Three flags that are not rows. **The unit mismatch that precedes everything**: a built-up-surface pixel or ML
footprint measures **plinth/roof coverage (2D footprint)** — not carpet, not built-up, not super-built-up.
Reaching a high-rise's saleable area multiplies by floor count (FSI/FAR) then by (1+L), L up to 0.50 in
Mumbai (§1.4) — a **compounding** distortion, worse than the price-side area swing (R19 confirms the
direction while replacing `D4`'s understated factor). **Earth Engine licensing**: `D4` recalled a commercial
tier from ~2021; D-05 recalls instead that **GEE became commercially available on Google Cloud around
February 2023, and before that commercial use was not offered at all** `[MODEL-MEMORY, must-verify]` —
stricter, and ~2 years later. The advice survives either version: get a real licensing read before committing
production architecture to GEE, and prefer direct downloads from JRC, the Copernicus Data Space Ecosystem
and EarthExplorer. **Liberalisation, dates unverified**: DST's geospatial guidelines (~**February 2021**)
replacing blanket security clearance with a negative list, and a **National Geospatial Policy 2022**
(~December 2022) superseding the 2005 National Map Policy `[RECALL]`.

**One negative that changes a data plan.** The blanket claim that no Indian state exposes public registration
data is **too wide on the counts-and-revenue limb**: Maharashtra records over 10 lakh registrations annually
with Mumbai ~30%, the IGR portal exposes a **daily/monthly registration-count and revenue e-search
facility**, and **Knight Frank India's monthly Mumbai/Pune notes republish the Department of Registrations
and Stamps' own figures within days of month-end** `[FIRST-PARTY: partC-data.md §C.5; R18]`. The negative
stands for transaction-level **microdata** only. Given §1.2's count requirement this is the volume series to
wire first, and it needs no scrape. D-12 separately deletes the remembered "mid-1980s to early-2000s"
free-e-search year band as an unverified parameter a build-or-no-build decision was resting on.

---

### 5. MODEL-CLASS DISCIPLINE

**Panel fixed effects and hierarchical shrinkage come before any gradient boosting, and the argument is
evidential, not aesthetic: every structural feature of this problem is one a tree ensemble handles badly and
a panel model handles by construction.**

| Structural feature | What the panel model does | What boosting does instead |
|---|---|---|
| **Censoring at an observed floor** (§2.1) | A censored likelihood or censored-quantile objective encodes the floor | The floor **compresses observed variance in the heaviest-bunching wards**, so in-sample fit is best where the data is worst; a tree selected on held-out MSE allocates capacity to exactly those wards |
| **Ward effect as a high-dimensional nuisance** (§2.3) | Honoré differences `α_i` away under exchangeability, without estimating it | Handed a ward identifier it **memorises** the nuisance parameter — with tens of observations, it memorises noise, then extrapolates that level forward as signal |
| **N per cell in the tens** (§1.1) | Fay–Herriot weights the direct estimate by **that cell's own sampling variance** — not a tuning knob | Regularisation (depth, learning rate, subsample) is global, tuned on a validation set, blind to which ward-quarter had 12 transactions and which 400. The grid also inflates the trial count `census_n()` must absorb |
| **The desk's own base rate** `[FIRST-PARTY]` | — | Two optimisation grids (OP-D3b, OP-D7) and a 21-agent adversarially verified sweep **all refused their train winners OOS**; the ER-arc pooled equation failed OOS at both horizons; kitchen sinks hit **−389%**; era-fragility is a repeated finding across independent arcs. The flexible-model failure rate on this desk's record is close to total |

| Stage | Model class | Gate before proceeding |
|---|---|---|
| 0 | Random walk / no-change per ward | The binding benchmark; everything is measured against it |
| 1 | Pooled hedonic or SPAR index + ward FE, censored objective | Beat stage 0 on Clark-West with the HLN correction, on purged spatially-blocked folds |
| 2 | Stage 1 + Fay–Herriot shrinkage | Beat stage 1 **and** improve PIT calibration, not only point loss |
| 3 | Stage 2 + spatial structure (SAR/GWR), **pre-registered** W or bandwidth | Beat stage 2; the free parameter registered before the print |
| 4 | Gradient boosting **on stage-2 residuals only** | Full hyperparameter grid counted in `census_n()`; beat stage 2/3 on Clark-West without degrading PIT |

Boosting on the *residuals* of a correctly-specified panel is defensible — the structure is already handled,
the flexible model attacks only what is left, the trial count stays honest. Boosting on raw registered price
is the one construction this section rules out outright.

---

### WHAT THIS SECTION CHANGES ABOUT THE PLAN

1. **Reframe the ward index as replication, not invention, and put an RTI/data-sharing request to RBI and the
   state Stamps departments at the top of the acquisition list.** RBI already computes ward × FSA-band
   strata; the ceiling is publication, not construction (§1, R7).
2. **Build one linkage and ship two series: S1, the price index on the uncensored region with an
   assessment-vintage control, and S2, the excess-mass compliance index.** Never fold S2's level into S1 —
   S2 is the reliability weight on S1 and the input to the bunching estimator (§1.3).
3. **Set the publication threshold as n ≥ (σ/s\*)² against a pre-registered precision target, measure σ on
   the first linked extract, and adopt ward × rolling-four-quarter × n ≥ 50 as the smallest defensible
   published cell** (§1.4). Print transaction count in the same row as every price figure — the China land
   case is the desk's own proof a shallow price print can be pure composition (§1.2).
4. **Make four fields mandatory before any computation**: area basis; assessment vintage date; registration
   date separate from transaction date; transaction channel (private resale vs. RERA-disclosed builder sale).
   The last cannot be reconstructed later and is what the Saez segmentation requires (§1.4, §2.5).
5. **Register two breaks-registry entries before pre-registering any censored or bunching design** — the
   43CA/50C/56(2)(x) safe-harbour ladder (~5% FA2018 → ~10% FA2020 → ~20% builder-primary-only under a ~₹2
   crore cap, 12 Nov 2020–30 Jun 2021) and the state guideline-value calendar (Gujarat Jantri frozen ~2011,
   doubled effective mid-April 2023; Delhi's 8-bin A–H structure). BR1–BR9 carry no circle-rate dimension at
   all (§1.3, §2.6).
6. **Size the bunching excluded window to the full proportional band per ward-year at that year's tolerance,
   treat each tolerance change as a free plateau-width quasi-event study, and read rung 3 as a
   triple-difference.** A notch-width window contaminates the counterfactual and understates excess mass;
   report S2 as a lower bound per Chetty et al.'s frictions result (§2.5, §2.6).
7. **Resolve the Honoré time-varying-threshold question before committing to the ward-fixed-effects
   specification, and decide in writing whether the structure is one- or two-equation.** The first determines
   whether the design is a citation or a research project away; the second cannot be diagnosed after the fact
   by any estimator in the toolkit (§2.3, §2.4).
8. **Implement the protocol against `quant/stats/cv.py`, `quant/validation/walkforward.py`,
   `quant/stats/dsr.py` and `quant/stats/preprocess.py` — write no new CV, embargo, deflation or
   winsorization code.** The modules already encode rules `D3` never stated: embargo ≥ 1× tau_half from the
   registry, 4–6 folds for India-only monthly series not a textbook 10, deterministic fold placement,
   `census_n()` reading the ledger. Report DSR as a screen, not a p-value (§3).
9. **Fix the scoring code before it is written: pinball loss is `(y−q̂)(τ − 1{y<q̂})` and CRPS carries a
   factor of 2.** `D3`'s published formula was not a loss function and would have rewarded biased forecasts
   (§3.1 item 11). Every promoted model ships pinball across a quantile grid, CRPS, a PIT histogram with a
   uniformity test, and a cumulative SSE-difference plot.
10. **Adopt GHSL as the built-environment backbone, try SHRUG before hand-rolling any crosswalk, stamp a
    vintage flag on every geospatial feature at ingestion, and wire Maharashtra's free monthly
    registration-count feed as item 3's volume series.** Exclude GHSL's projected 2025/2030 epochs; never
    date Microsoft's footprints by their release date; use WorldPop/HRSL growth patterns but not levels; do
    not build on Census-era ward shapefiles without checking each city's current delimitation (§4). **Stage
    the model classes 0→4 and admit gradient boosting only as a residual model with its grid counted in
    `census_n()`** — boosting on raw registered price selects for the most corrupted wards (§5).

---

## §5 — REACHABILITY, MEASURED RATHER THAN ASSUMED

**This section is the only part of §§1-5 that is a measurement rather than a literature claim, and
it is the most operationally important thing in the pack.** On 2026-09-11 the desk probed 37
candidate endpoints directly from the remote/web session with `curl` — every major international
house-price source, every Indian official portal, and the free geospatial stack.

**Result: 36 of 37 blocked. The only endpoint that answered was the GitHub control.**

| Class | Probed | Reachable |
|---|---|---|
| GitHub raw (control) | 1 | **1** |
| International official (BIS, Dallas Fed, OECD, IMF, FHFA, FRED, US Census, HM Land Registry, Ireland PPR, Kadaster, NBP, MLIT Japan, data.go.kr, data.gov.sg, URA) | 15 | 0 |
| India official (data.gov.in, RBI DBIE, RBI main, NHB RESIDEX, IGR Maharashtra, NGDRS, DILRMP, MahaRERA, Bhuvan, MoSPI) | 10 | 0 |
| Geospatial / free bulk (JRC GHSL, Overpass, Geofabrik, Google Open Buildings, WorldPop, NOAA VIIRS) | 6 | 0 |
| Private India (Magicbricks, Housing.com, Knight Frank India) | 3 | 0 |
| US private bulk (Zillow research CSVs) | 1 | 0 |

The failure mode is identical in every case and it is not a site problem: `curl` error 56,
*CONNECT tunnel failed, response 403*, and the agent proxy's own log records
`kind: connect_rejected`, `detail: "gateway answered 403 to CONNECT (policy denial or upstream
failure)"`. It is a network-policy denial at the gateway, not a robots rule, not a rate limit, and
not something a different user agent or a retry will fix. Raw output and the probe script are in
`research/notes/re-engine-sources/_PROBE.md` and `_PROBE.sh` — re-run it on the desktop machine and
the same table becomes an acquisition plan.

**Three consequences, all binding.**

1. **The venue decision in the handoff prompt (§0.5) is now measured, not inferred.** Acquisition
   must run on the principal's own machine. A web session cannot pull one row of any source this
   project needs — not even the free, open, no-login ones like HM Land Registry Price Paid or the
   JRC built-up surface rasters.
2. **GitHub is the one live channel, so GitHub-hosted mirrors are the only data this environment can
   ever land.** That is exactly how the desk's existing ten vaults were built. Worth a dedicated
   hunt: several of the international series in §2 are mirrored in academic and replication
   repositories, and the JST panel — already vaulted here — is one of them.
3. **Everything in §§1-4 of this pack is snippet-grade for a structural reason, not a stylistic
   one.** No agent could open a primary page. Treat the pack as a map of where the evidence lives,
   then verify on the machine that can actually reach it. The `[RECALL — unverified]` tags are the
   honest edge of what was possible here.


---

## §6 — THE AUDIT SCOREBOARD, AND THE VERIFICATION QUEUE

Three adversarial fact-checkers read the 22 dossiers with instructions to find what was wrong before
the desk published it. They returned **53 refutations and 71 downgrades**. Their verdicts were
binding on the four syntheses above, and §§1-4 have been written accordingly — but the refutations
stay listed here rather than being silently edited away, because a pack that hides its own first
draft cannot be audited by the next reader.

### 6.1 The audit's own limitation, stated first

**WebSearch hit its 200-call session ceiling before audits 2 and 3 ran their first query.** Three
files independently reproduced the exhaustion. So for clusters B, C and D2-D4, the two axes that
mattered most — *does this paper exist* and *does this endpoint exist* — **were not audited**. Those
auditors pivoted to the checks still available to them: internal arithmetic, cross-dossier
contradiction, direct reads of the vaulted JST workbook, and comparison against the desk's own
documents of record. That pivot turned out to be the most productive axis in the whole leg, but it
does not substitute for citation verification. **Treat every citation in §§2-4 as unverified.**
Cluster A's citations were audited and 16 refutations came back, which is the base rate you should
assume applies to the unaudited three-quarters.

### 6.2 The six corrections that change the design

1. **The circle rate may not censor the recorded price at all — and this is the most consequential
   finding of the leg.** The whole censored-regression core rests on `observed = max(true, c_it)`.
   Audit 2 (R9) refuted that as a *mechanical* identity using the pack's own mechanics: stamp duty
   is charged on the **higher of declared price or circle rate**, which constrains the **tax base**,
   not the **declared consideration**. Nothing mechanically stops a deed recording below the floor —
   duty is identical either way. What makes the floor bind is the income-tax deeming machinery
   (Sections 50C / 43CA / 56(2)(x)) with its 5-10-20% tolerance band, which is an *incentive*, not a
   censoring rule. **Consequence: the pile-up at the floor is a behavioural equilibrium, and plain
   Tobit assigns zero probability to any observation below `c` — misspecified before any
   distributional concern if such rows exist.** Day-one diagnostic, which the dossier never stated:
   **measure the share of declarations strictly below the local circle rate.** If that share is
   non-trivial, the correct model is the bunching/notch-with-plateau family (§4.2), not Tobit. This
   is a better model than the one the handoff prompt specified, and it is reachable with the same
   data. *(Note on provenance: the cluster-D synthesis was mis-wired to read audit 3 rather than
   audit 2, so it never saw this refutation. My scripting error, recorded rather than smoothed.)*
2. **The "20-35%" area-basis constant is arithmetically wrong and is retired.** A 70-80% carpet
   ratio implies **+25% to +43%** per square foot, and Mumbai loading is independently reported at
   **40-50%**. Carry an explicit loading factor **L** with **psf ratio = 1 + L**, L up to **0.50**
   for Mumbai. The old constant understated the worst case in the primary market by up to 15pp. It
   had propagated into five dossiers and into the handoff prompt, which is now corrected.
3. **The five-year mean-reversion overlay is dropped.** The literature's canonical crossover is
   momentum at ~1 year, reversion at ~5 (Glaeser & Nathanson 2017). The five-year limb is refuted by
   the best evidence the desk owns: IN-D1 prints **+9.65%/yr** real over the next five years after a
   ≥15%/yr window. First-party desk evidence outranks snippet-grade calibration. Size against the
   **~2x crash-odds lift off a 13.0% base** instead of forecasting a reversal.
4. **A fabricated co-author was caught.** "Mian, Sufi & Matvos" on *Credit Supply and Housing
   Speculation* — the third name does not belong, and the alphabetically impossible ordering is the
   tell. Also caught: two distinct Piazzesi-Schneider papers presented as alternate titles of one;
   Hsieh & Moretti's GDP figure given as ~2% when the published AEJ:Macro version says **3.7%** (the
   2015 working paper said 9.5%); Anenberg's venue wrong; a malformed URL. **This is the
   hallucination class the audit existed to catch, and it caught it in the one cluster it could
   check.**
5. **`[2-SOURCE]` was being awarded to one paper found at several hosting locations.** Bhupal Singh,
   Nagpal-Gandhi and Baum-Snow & Han were each tagged two-source on the strength of a preprint
   mirrored across CEPR, an author page and a repository. **One paper on three servers is one
   source.** Every India-specific magnitude in this pack traces back through that error, including
   the only causally identified Indian supply elasticity and the only Indian credit elasticities.
6. **A majority of model memories does not outvote a desk document.** Audit 1 instructed that the
   RBI HPI's 18-city / 2022-23 rebase be pulled from §00 because three dossiers and its own recall
   said 10 cities / 2010-11. Audit 3 refuted its sibling: the rebase is documented on desk with a
   release date (2025-10-10), a reference quarter (Q1:2025-26), eight named new cities and a
   pre-registered splice rule. §00 stands; the dossiers carry the error. **The evidence hierarchy
   held under pressure, which is the more important result than either number.**

### 6.3 The verification queue — what the next session must verify, ordered by design dependency

Nothing below is optional. Each row is load-bearing: a build decision changes if it resolves the
other way. Ordered so that a `no` answer kills the least work.

| # | Verify | Why it is load-bearing | If it fails |
|---|---|---|---|
| 1 | The share of registered declarations strictly **below** the local circle rate | Decides Tobit versus bunching (§6.2 #1) | The censoring core is replaced by a notch model |
| 2 | The **43CA/50C/56(2)(x) tolerance ladder** — the 5% → 10% → 20% sequence, its dates and the ~₹2cr primary-sale cap | It is the *free identifying variation* in the whole design: a statutory change in the tolerance band with a known date | No policy discontinuity to identify off |
| 3 | Whether **Honoré (1992)** extends to a genuinely period-varying threshold, or normalises it to a constant | The only route to ward fixed effects under censoring | Censored quantile regression becomes primary |
| 4 | Whether RBI computes **ward × floor-space-band strata** upstream of its published HPI | Reframes the project from invention to replication at finer grain, and sets the top acquisition ask (an RTI for existing strata) | The free validation target disappears |
| 5 | The Maharashtra IGR **free e-search year band**, and whether any bulk or aggregate export exists | Decides whether a locality panel is buildable at all | FM1 fires; fall back to RBI HPI grain |
| 6 | Which of the two **India yield families** is right — asking-over-asking ~5.2% national, or portal/broker 2.0-4.0% Mumbai | CN-D2 makes yield *the* placement instrument; the two families place India on opposite sides of the pre-crash mode | No placement is possible; the India verdict is unresolvable |
| 7 | The **cost wedge**, recomputed from registry-sourced state-specific rates | Every published distribution is shown net of it; two of five benchmark rungs are functions of it | The project's central bar is wrong |
| 8 | **ULPIN / Bhu-Aadhaar coverage** for the chosen cities | The parcel key both SPAR and repeat-sales need; survey, khasra, CTS and gat numbers do not compose | No panel identity; index method forced to stratified median |
| 9 | Whether **any leave-and-license rent aggregate** exists or is obtainable | The only India route to a *transaction-based* yield rather than an asking-based one | Row 6 stays unresolved permanently |
| 10 | Gujarat's **2023 jantri revision** — effective date and the actual multiple by zone | The cleanest dated notified-value experiment in India; currently two model memories agreeing, which is concurrence and not verification | Lose the natural experiment |
| 11 | **RERA QPR history** — whether past quarterly progress reports are retained or overwritten | Decides whether the supply pipeline is a point-in-time series or a single revised snapshot (the lookahead trap) | Supply features become unusable as features |
| 12 | The **SPAR denominator** convention — base-date assessed value or most recent | Two dossiers contradict each other; it changes the estimator | Re-derive before any index is built |
| 13 | Whether the **BIS India series** is the RBI HPI, and its exact city list and start | The only standing route to a *live India valuation percentile* — the gap SNAPSHOT-1 named as its single biggest | No valuation state variable for India |

Rows 1-3 gate the dependent variable, 4-5 gate whether a locality panel exists, 6-7 gate whether the
answer means anything economically. **Resolve 1, 5 and 7 before writing a line of model code.**


---

## §7 — WHAT WAS NEVER SWEPT, AND THE THREE WAYS THIS FAILS

A final agent read the four syntheses adversarially and asked what a hostile expert would say. Its
output is the most useful part of this pack, because everything above is what 22 agents *did* look
at and this is what none of them did.

### 7.1 The modalities nobody swept — and four of them are better than what was swept

Ranked by what they would change. The first three are **uncensored price observations**, which is
remarkable given that §§4.1-4.2 of the handoff prompt spend their length engineering around
censoring.

| Gap | Why it matters | Grade |
|---|---|---|
| **Listed-developer quarterly filings** — DLF, Macrotech, Godrej Properties, Oberoi, Prestige, Brigade, Sobha publish audited pre-sales value and volume, **average realisation per sqft by city**, launches, collections, inventory and net debt, every quarter | A dated, audited, per-sqft price series with **no evasion incentive and no notified floor** — and it is already public, already quarterly, and already point-in-time. The single largest omission in the pack | **Highest value** |
| **Public land auctions** — CIDCO, MHADA, HUDA/HSVP, NOIDA, DDA, state industrial corporations | Published, dated, plot-identified, competitively bid, **no under-reporting incentive and no floor to bunch at**. The clean comparison series the censoring model needs to calibrate against | **Highest value** |
| **Distressed sales** — SARFAESI bank e-auction notices, IBAPI reserve prices | Address-level, dated, and the one place the *downside* of the distribution is observable in a market whose registered prices are floored | High |
| **Demography and household formation** — headship rates, household-formation projections, internal migration, age structure | **The only variable class with any claim to ten-year forecastability, and it is entirely absent.** Credit, momentum and evasion are all short-horizon mechanisms, so the pack has nothing in the place where its promised horizon actually lives | **Highest value for the 10y layer** |
| **Physical-climate risk** — flood, heat, groundwater, subsidence, air quality | Locality-discriminating, publicly mapped, and unlike momentum genuinely forward-looking at ten years. Chennai 2015, Mumbai flooding, Bengaluru 2022 lake-bed inundation, NCR air quality. **The desk already owns a vaulted climate dataset** | High |
| **The developer incentive stack as a second wedge** — subvention and CLP plans, "stamp duty paid", floor-rise and PLC waivers, parking, club membership, furnishing credits | The pack models one wedge (cash under-reporting, widening late-cycle) and misses the second, which **widens in downturns while the headline rate is defended**. Two wedges moving in opposite cycle phases is a different measurement problem entirely | High |
| **Dubai Land Department** — free transaction-level microdata with an open API | An emerging market with two documented crashes, heavy Indian participation, and the most India-relevant **open-microdata** regime in the world. §2 lists ~25 countries and omits it, which is what a coverage list looks like versus an evidence list | Medium-high |
| **Litigation as an observable** — eCourts, NCLT/IBC real-estate admissions, RERA complaint orders | The pack carries the finding that *litigation, not regulation*, throttled India's supply response, then proposes no way to measure it. Free, dated, text-searchable | Medium |
| **District-level credit** — RBI Basic Statistical Return, district × sector outstanding | The finest free credit grain in India. The credit module as specified is national Sectoral Deployment only. Also missing: the **2019 external-benchmark (EBLR) mandate** as a monetary-transmission break, absent from an event calendar carrying eleven tax and RERA dates | Medium |
| **NRI / FX demand and gold substitution** | The desk owns a full currency battery (PPP +0.94, weak-INR year behaviour, a 71-episode crash anatomy) and gold to 1833, plus CI-D2 ranking gold above housing in high-and-rising inflation. None of it is connected to property demand anywhere. **A weak-INR year is a testable conditioner on NRI-heavy localities** — and SNAPSHOT-1 says India is in one now | Medium |
| **TDR markets and fiscal capitalisation** | Mumbai TDR is a traded instrument whose price is a direct read on FSI scarcity. Also absent: the Oates-lineage literature on tax and amenity capitalisation, land value capture, and society-redevelopment optionality (cessed buildings) — a genuinely India-specific source of value | Medium |
| **Thin-market index methods the menu omits** — hierarchical-trend and state-space repeat-sales (Francke; Schulz-Werwatz; Nagaraja-Brown-Zhao) | §4 lists eleven methods, rules out five in its own verdict column, and omits **the one family built precisely for "tens of transactions per cell"** | Medium |
| **Exit liquidity** | CN-D4 established that the exit plan matters more than the entry level, and the architecture promises a liquidity output — with no time-on-market or months-to-sell measurement specified for India | Medium |
| **The advisory and publication perimeter** — SEBI adviser perimeter, RERA agent provisions, disclaimer form | A locality-level forward distribution delivered to wealth clients is a different regulatory object from an equity research note. **The project can be complete, correct and unpublishable.** Cheap to answer now, expensive at the last gate | Do it first |

### 7.2 The three objections that would be made by people who know

**An RBI research economist:** *"Your states are not identified, so your conditional distributions
are not conditional on anything you observed."* India has roughly 61 quarters of a ten-city
registered-price index with a documented rebase and coverage change inside it, and **zero completed
domestic crash episodes** — at most one and a half national upcycles and no downcycle. Every p10 and
every "share of comparable states that subsequently fell 20%+" is therefore borrowed from an 18-country
advanced-economy panel and relabelled as an Indian conditional.

**A Mumbai developer's CFO:** *"You are measuring the gross number on the deed, and the gross number
is the one thing we hold constant in a downturn."* Primary sales clear at headline price minus an
undisclosed incentive stack. In a soft market the printed rate is defended and the stack widens. A
deed-based index will therefore **understate the drawdown precisely when the drawdown is what you
need** — the inverse of the error everyone worries about.

**A US quant housing researcher:** *"Your benchmark and your outcome are the same artifact, and your
effective sample size is one."* You construct the index, forecast the index, and benchmark against a
random walk on the index. Repeat-sales and appraisal-style indices are mechanically smoothed
(Geltner), manufacturing exactly the autocorrelation a momentum stage will harvest. Hundreds of
localities in one country in one era is **one** macro draw, not hundreds of independent observations.

### 7.3 The three ways this fails, ranked, each with the probe that detects it early

**FM1 — Acquisition never reaches locality grain, and the engine degrades into what RBI HPI and
RESIDEX already are.** Highest probability, and the pack establishes every precondition: no state
exposes bulk microdata, the free rungs are captcha-gated per-record lookups, and no parcel key
composes across systems. *Probe: attempt 200 real e-search retrievals for one Mumbai ward on the
desktop machine and measure the per-record cost in seconds and in blocks.*

**FM2 — The dependent variable gets built and is a compliance index wearing a price index's label.**
Three independent routes to it: the censoring model is structurally wrong (§6.2 #1), the tolerance
band changes declaration behaviour on dates unrelated to value, and the incentive stack moves
counter-cyclically. *Probe: the below-floor share (queue row 1), plus a placebo — does the index
jump at the 43CA tolerance-change dates?*

**FM3 — Something survives, it is the artifact, and it ships under the desk's name to clients.**
Third by probability, **first by cost.** The desk has hit this exact pattern five times already
(SC-D4, TECH-D3, MOM-D1, VAL-D2/D3, EQ-D1), and here the ingredients are all present: localities
enter the panel *because* they appreciated (Ulwe, Kokapet), the index is smoothed, and the reward
for a confident answer is high. *Probe: declare the one-way rule at registration — a bias that
flatters the finding makes a print for it non-evidence-grade — and run the entry-date placebo before
any result is written up.*

### 7.4 The critic's methodological complaint, which is upheld

**Four syntheses each carrying the other three's conclusions manufactures the appearance of
corroboration.** The loading factor appears in six places, the RBI rebase splice rule in five, the
reachability probe in four, the crash base rates in five. Repetition inside one pack written by one
model family is **not** independent confirmation, and this desk has a name for that failure. Read
§§1-4 as one document with four authors, not four documents that agree.


---

## §8 — THE FIFTEEN THINGS TO READ FIRST

Ranked by what changes your design per hour spent. On-desk documents come first because they are the
only desk-grade material available; external items carry their tag.

| # | Read | What it gives you |
|---|---|---|
| 1 | `research/cycles/fincycle-deep/partC-data.md` §§C.1-C.10 **[DESK]** | The India property data estate already engineered: RBI HPI provenance and its live rebase, RESIDEX's two breaks and two price concepts, the vintage/point-in-time hazard table, and §C.9's list of what cannot be measured free. Saves a fortnight |
| 2 | §6 of this pack, rows 1-3 of the verification queue | Whether your dependent variable is a censored regression or a bunching problem. Everything downstream forks here |
| 3 | `docs/cycles/13-real-estate.md` headline **[DESK]** | The 18-year clock is dead on this desk's own pre-registered test. Read before anyone proposes a cycle-phase feature |
| 4 | Trial ledger entries **IN-D1..IN-D2** and **CN-D1..CN-D5** **[DESK]** | The only quantified base rates you have: crash depth and duration, boom-to-bust velocity parity, the yield-placement instrument, the 87.2% false-alarm rate, and "hot markets stay hot" |
| 5 | §7.1 of this pack, rows 1-4 | The three uncensored Indian price series nobody swept — listed-developer per-sqft realisations, public land auctions, SARFAESI e-auctions — plus demography, the only class with a claim to ten-year forecastability |
| 6 | Glaeser & Nathanson (2017), *An Extrapolative Model of House Price Dynamics*, JFE 126 **[1-SOURCE, audited]** | The cleanest single statement of momentum, reversion and excess volatility from one behavioural primitive. Read it for the mechanism, not the five-year limb (§6.2 #3) |
| 7 | Case & Shiller (1989), AER 79(1) **[2-SOURCE, audited]** | The founding result *and* its own caveat: serial correlation significant at the city-index level, R² ≤ 0.04 at the individual-home level, and never an out-of-sample test |
| 8 | Kleven's bunching review, plus Best & Kleven on UK stamp duty **[unaudited]** | The estimator that turns the mass sitting at the circle rate into an under-reporting measure, and the notch-versus-kink distinction the 43CA tolerance band forces |
| 9 | The *Handbook on Residential Property Price Indices* (Eurostat/ILO/IMF/OECD/UN/World Bank, 2013) **[unaudited]** | The standard reference on what to do when cells are thin, and the sanctioned methods a regulator would recognise |
| 10 | Statistics Netherlands / New Zealand **SPAR** method **[unaudited; and see queue row 12]** | Sale-price-appraisal-ratio indexing: built for markets where every property carries an official assessed value and transactions are sparse. That is India with circle rates, and it is the most transferable idea in §2 |
| 11 | Korea **MOLIT RTMS** via data.go.kr, and Japan **MLIT Real Estate Information Library** **[searched]** | Two working free transaction-level APIs at sub-city grain. The existence proof that a country can go from opaque to open, and the template to hold your Indian ask against |
| 12 | Taiwan's **actual price registration** reform (2012, strengthened 2021) **[unaudited]** | The natural experiment India has not run: what happens to measured prices, volumes and revenue when under-declaration is forced out by statute |
| 13 | Saiz (2010), QJE, on geographic supply constraint; with Glaeser-Gyourko-Saiz on bubbles **[audited]** | Why inelastic places get bigger booms and shorter busts — the mechanism that should order your city list before any data arrives |
| 14 | Mian & Sufi on credit supply and housing speculation **[audited: two authors, not three]** | The best-identified demand channel, and the one whose Indian analogue (district credit, queue row 9 of §7.1) nobody has assembled |
| 15 | §7.2 of this pack | The three objections your work will actually face. If you cannot answer the CFO's, the deed-based index understates exactly the drawdown you built it to see |

**If you read only two things:** item 1, because it is already done, and item 2, because it decides
whether the project's core is a Tobit or a notch.


---

## §9 — HOW THIS PACK CONNECTS TO THE HANDOFF PROMPT

The two documents are meant to be read together and they do different jobs. Nothing here overrides
`research/CONTRACT.md` or `CLAUDE.md`.

| Handoff prompt section | What this pack supplies |
|---|---|
| §0.5 run it on desktop, not web | §5 — the measured 36-of-37 blackout. The decision is no longer a judgement call. |
| §1 the cost-drag calculation | §00 print 15, plus §2's international yield and transaction-cost comparisons for context on how unusual India's wedge is. |
| §4 the dependent variable | §3's provenance table for every official index, and §4's index-construction menu with the SPAR-on-assessed-values route treated as a first-class option rather than a footnote. |
| §4.1 the censored-regression core | §4's econometric toolkit — the left-censoring likelihood with an observed time-varying threshold, Honoré's fixed-effects answer, the censored-quantile alternative, and the bunching estimator that turns the mass sitting at the circle rate into an evasion measure. Plus §2's international evasion estimates as priors on the magnitude, with Taiwan's 2012 actual-price registration as the natural experiment. |
| §4.2 the rental/yield route | §3's yield table and the Maharashtra leave-and-license evidence; §1's price-rent literature on what a yield can and cannot forecast. |
| §5 the locality universe | §4's smallest-defensible-cell analysis and the hierarchical-shrinkage literature — the honest answer to "how few transactions can support a locality index". |
| §7 the data source inventory | §§2, 3 and 5 together replace the inventory's guesswork: what exists, where, under what licence, and whether it can be reached at all. |
| §8 the feature library | §1's transferable coefficient magnitudes and §4's free geospatial table with the point-in-time-versus-revised-snapshot flag, which is the lookahead trap. |
| §9 validation and the 10-year impossibility | §4's evaluation protocol — random-walk and no-change benchmarks, purged and spatially blocked CV, Diebold-Mariano and Clark-West, multiple-testing control across hundreds of localities, and proper scoring rules for the distributional forecasts this project is required to produce. §1 supplies the reason: the honest out-of-sample record for house-price forecasting is far worse than the in-sample literature suggests. |
| §11 kill criteria | §7 — the critic's ranked failure modes and the probe that would detect each one early. |
| §12 the four go/no-go probes | §5 turns probe 1 into a finished measurement for every global source and a desktop to-do list for the Indian ones. Probes 2-4 stand. |

**The one thing to carry forward if nothing else survives the read.** The international literature
(§1) says house prices are forecastable in the short run mostly through momentum, in the long run
mostly through a valuation anchor, and almost never in a way that beats a random walk at the
horizons a buyer actually cares about. This desk's own prints (§00) say the same thing in Indian
terms: hot markets keep running for five years at double the crash odds, the credit early-warning
signal cries wolf 87.2% of the time, the folk 18-year clock fails its own test, and a ~21.5%
five-year cost wedge eats a 20% cumulative gain whole. **So build a state classifier and a
cost-aware hurdle calculator, and publish distributions. Do not build a price predictor.** Every
section below is here to make that instruction concrete rather than merely cautious.

---

*Assembled by the RE-SOURCES leg, 2026-09-11. Dossiers, audits, syntheses, the probe script and its
raw output: `research/notes/re-engine-sources/`. Ledger entry `RE-SOURCES`. Census unchanged at
1,399 — this leg computed nothing and claims nothing as a print.*
