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
