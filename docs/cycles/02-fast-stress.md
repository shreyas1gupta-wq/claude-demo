# Deep-dive #2 — Fast Stress (L2, the reactive switch)

v2.0 (upgraded to the full monograph standard, 2026-09-02; atlas 5.1/5.2/5.3 — the v1.0 spec below remains operative, the upgrade chapters follow it)
v1.0 · 2026-09-01 · Evidence base: D04 (+D01 crash rows, D12 microstructure) · Ladder seat:
`config/ladder.yaml L2_fast_stress` (block fast_stress 0.25 — the largest single seat) ·
Code: `quant/ladder/fast_stress.py` · Phase overlay: `quant/ladder/phase.py` (L2 is the first
customer of the 2026-09-01 phase directive) · **Results status: designs F1–F7 frozen here; RESULTS
require Phase-0 fixtures; the module and a synthetic end-to-end demo run today.**

---

## 1. Theory — why volatility clusters and why acting on it survives

1. **Volatility clusters.** Mandelbrot (1963): "large changes tend to be followed by large changes,
   of either sign, and small changes by small changes." Engle (1982) made it estimable (ARCH); it is
   arguably the single most robust empirical regularity in finance — Tier A by any count, at any
   frequency, in every market including India.
2. **Why it clusters (mechanism, not mystery):** information arrives in bursts; leverage unwinds
   force selling that begets more selling (the same forced-selling amplifier as D03's credit bust,
   at daily speed); market-makers widen and withdraw when inventory risk rises, so the same order
   flow moves prices more. Vol is high when the *machinery* of the market is impaired.
3. **The leverage/feedback asymmetry.** Falls raise vol more than rallies (French-Schwert-Stambaugh
   1987): equity falls mechanically raise leverage and margin pressure. Consequence: a fast-stress
   state is not symmetric noise — its spikes coincide with the left tail we are mandated to cut.
4. **Why acting on it isn't arbitraged away** (Contract §5, category ii + iii):
   - It is a RISK transformation, not an alpha. De-levering into high vol and re-levering after
     transfers drawdown, not expected return, so there is no "trade against it" that decays it.
   - The institutions that could crowd it are *structurally prevented*: leverage constraints bind
     hardest exactly when vol spikes (margin calls force the wrong-way trade), and daily-liquidity
     vehicles must sell into stress. Our books have no external redeemers — a genuine structural
     edge for this desk.
   - What IS contested is the *alpha* claim (see §2, Moreira-Muir vs Cederburg). We harvest the
     uncontested part (DD control — the binding constraint) and treat any Sharpe improvement as a
     bonus to be proven on India data, not assumed.
5. **What the signal is and is not:** it is a *now*-cast of market impairment (τ½ 1–3 months), not
   a forecast of direction. It arms de-risking fast and — via the phase overlay — describes when the
   storm is passing (falling-from-high = candidate re-entry regime, gated by F7). It never predicts
   the spike itself; nothing free does.

## 2. Evidence — the numbers this seat stands on

| Finding | Sample | Effect size | Source (D04/D01) |
|---|---|---|---|
| Volatility clustering / persistence | universal | |r| autocorrelation significant for months; vol forecastable at 1–21d horizons | Mandelbrot 1963; Engle 1982; Andersen-Bollerslev 1998 |
| Leverage effect | US 1928→ | negative return–vol correlation; falls raise future vol more than rallies | Black 1976; French-Schwert-Stambaugh 1987 |
| Vol targeting cuts tails | 60+ years, multi-asset | vol-targeted risk assets: lower vol-of-vol, **materially smaller max DD and left tail**, Sharpe ≈ equal or slightly better for equities | Harvey et al. 2018 (JPM) |
| Vol-managed portfolios raise Sharpe/alpha | US factors 1926–2015 | scaling by 1/σ² produces positive alpha on market and momentum factors | Moreira-Muir, JF 2017 |
| …but the alpha is fragile OOS | 103 factor-country pairs | direct real-time implementation fails for most factors; market factor most robust | Cederburg-O'Doherty-Wang-Yan, JFE 2020 [the honest counter-row] |
| Risk-managed momentum | US WML 1927→ | constant-vol WML: Sharpe ~0.53→~0.97, crashes largely eliminated | Barroso-Santa-Clara, JFE 2015 (verified) |
| Momentum crashes live in the fast-stress state | US 1927→ | WML crashes occur in panic states (high vol, post-decline) during REBOUNDS | Daniel-Moskowitz, JFE 2016 |
| Correlations spike in bear tails only | intl equities 1959–96 | exceedance correlation rises in crashes, not booms — diversification fails exactly in stress | Longin-Solnik, JF 2001; Ang-Chen 2002 |

**India-application note:** vol dynamics are Tier A on bhavcopy data (daily since the 1990s);
India VIX exists from 2008–09 (NSE archive, free) — one full crisis (2020, VIX ≈ 80s) plus a dozen
smaller spikes; episode-conditional RULES are Tier B (≈12–15 usable episodes). The Moreira-Muir
alpha claim carries the Cederburg caveat *before* any India test: F3's stated prior is "DD control
robust, alpha unproven".

## 3. India stress chronology — the episode set (pre-named for F2/F6/F7)

May 2004 (election, circuit-halt day) · May–Jun 2006 (EM selloff) · Jan 2008 (two-day crash) ·
Sep–Nov 2008 (GFC core) · Aug–Nov 2011 (EU/downgrade) · May–Sep 2013 (taper tantrum, INR to 68) ·
Aug 2015 (China deval) · Nov 2016 (demonetization week) · Feb 2018 (global Volmageddon + LTCG) ·
Sep–Oct 2018 (IL&FS) · Mar 2020 (COVID: −13.2% single day, ~−38% peak-to-trough, India VIX ~80s) ·
Feb–Mar 2022 (Russia) · Jun 4 2024 (election day −5.9%) · May 2026 (INR/FII crisis — stress episode
for L2 even though non-qualifying for the DD test per the 2026-08 verification).

**Clock-test verdict:** ~14 episodes in ~22 years — arrivals are CLUSTERED-RANDOM (no periodicity;
Poisson-like with vol-clustering), so L2 is a *recurrence state*, never a clock. Enough episodes
for Tier-B episode rules; the underlying vol dynamics are Tier A. This is the best-sampled seat on
the ladder — which is exactly why it carries the largest block budget (0.25 [C], to be swept).

## 4. The state variable — exact construction (what the module implements)

Three inputs, one composite, no clamp (all Tier B), phase on top:

1. **Realized-vol percentile** — trailing RV (window from grid {10, 21, 42}d, annualized) on the
   book benchmark index, expanding-percentile ranked. The reactive input.
2. **Drawdown-depth percentile** — distance below the expanding peak, percentile-ranked. The
   "how bad already" level input (fast analogue of credit's CD-ratio role).
3. **Confirm rank (optional weight)** — India-VIX rank / IV−RV spread / funding-flow stress
   (NSDL FPI outflow rank, CCIL repo spread) per the registry role. Tier B ⇒ symmetric weight —
   it may pull the state DOWN as well as up (contrast credit's clamped Tier-C composition).
4. **Phase overlay** — (level, velocity, quadrant, age) per `state_phase_convention`. Registry
   role kept verbatim: "any one arms R4 cuts, two confirm." Rising (U) arms cuts; falling-from-high
   (D) is the candidate re-entry regime — display/log-only until F7/H66 pass.

Output: signed state ∈ [−1, +1], higher = more stress = less risk permission, feeding the
fast_stress block (0.25 of regime score). **What moves the book:** state ≥ high grid ⇒ bucket
steps toward R4 (leverage → 0.4–0.6×, hedge → 100–150%); tail-sleeve entries pause; re-entry
follows the per-sleeve re-entry rules (Batch-2 Q8), never a reflex.

**Measured property (synthetic, seeds 0–9, logged):** detection is high but NOT total — 92/98
planted episodes ≥15d cross the 0.3 threshold (median lag 1 day); mild episodes leave no vol
signature. The draft test asserting 100% at 0.5 was falsified (73/98) and replaced with the
measured bound. Design consequence baked into F2/F6: value is measured NET of missed episodes and
false fires, on the full threshold grid, never a single cell.

## 5. Pre-registered designs (frozen here; run on fixtures)

| # | Design | Specification (fixed before data) | Decision rule |
|---|---|---|---|
| F1 | **τ½ of the composite** | Bias-corrected AR(1) (§11.2 machinery) on daily composite, rolling windows across the §3 episode set | CI → `ladder.yaml` L2 tau_half (currently [1,3]m [B]); drift feeds tau_half_drift_policy (informational band: compression watch) |
| F2 | **Episode DD improvement** | De-risk grid: bucket cut at stress pctile {0.8, 0.9, 0.95} × confirm {1-of-3, 2-of-3} × re-entry {phase-D, pctile-decay, calendar}; metric = episode-conditional max-DD delta NET of statutory costs at each book's turnover cap | Improves episode DD within the §1.1 risk-drag budget ⇒ arms the R4 mapping as registered; fails ⇒ block weight re-swept |
| F3 | **Vol-managed Nifty (two-sided)** | Moreira-Muir c/σ̂² scaling, full-period AND Cederburg real-time OOS protocol; costs in | Stated prior: DD control robust, alpha unproven. Either result documented; alpha claim may NOT be promoted from full-period evidence alone |
| F4 | **Correlation-spike increment** | Mean pairwise correlation (top-50 names, window grid) percentile; incremental episode AUROC over RV alone | Adds ⇒ enters as confirm input candidate; redundant ⇒ documented, excluded |
| F5 | **India-VIX vs RV redundancy + VRP** | IV rank vs RV rank correlation + incremental AUROC; IV−RV spread (variance-risk-premium proxy) as separate candidate | Redundant ⇒ RV stays primary (longer history); IV adds ⇒ confirm seat; VRP tested as its own pre-registration before any use |
| F6 | **Whipsaw / false-fire ledger** | Full threshold-grid table: false-fire rate, round-trip cost per false fire by book, missed-episode rate (per §4's measured-bound rule) | The de-risk rule must clear the cost-in-SR speed limit per book; Conservative likely needs the slowest cell — documented per book |
| F7 | **Phase-quadrant asymmetry (H66 fast-band)** | At matched state LEVELS: forward 1–3m returns and DD, U vs D (falling-from-high = rebound candidate per Daniel-Moskowitz panic-rebound row) | Passes ⇒ re-entry rules may condition on D via Challenger, reduce-only first; fails ⇒ phase stays display-only for L2 |

Minimum economic effect: same currency as L10 — episode-conditional DD improvement within the
risk-drag budget, judged in the M4 walk-forward, never standalone Sharpe.

## 6. What can be known today vs what awaits data

**Known today [theory/A/X]:** clustering + leverage effect (Tier A), the tail-cutting effect of
vol targeting (multi-asset, 60y), the contested status of the alpha claim (stated as a prior, not
resolved), the construction, the designs, and a working module verified on planted ground truth —
including its honest miss rate. **Awaits fixtures:** every India number — τ½, thresholds-as-grids,
detection/false-fire tables on the real episode set, VIX redundancy, F7 asymmetry.
**Never knowable:** the date of the next spike. L2 is built to react in days, not to predict.

## 7. Synthetic demonstration (runs in this repo, zero market data)

`scripts/analyze_fast_stress.py --demo` builds the two-state economy (planted calm/stress with
known boundaries), runs the exact module, and reports: stress-vs-calm state separation (≥ +0.2 on
all seeds), the detection-rate table at the full threshold grid (including the honest miss rate),
median detection lag, and the phase view of an episode (U on onset, D on decay). Demo output:
`research/cycles/02-fast-stress-DEMO.md` (marked SYNTHETIC). Tests: `tests/test_fast_stress.py`
(6, incl. the no-look-ahead truncation property and the measured detection bound).


---

# UPGRADE TO FULL STANDARD (v2.0, 2026-09-02)

# Parts A, G, B, C — fast stress at full standard (atlas 5.1/5.2/5.3 → L2)

*v1.0 · 2026-09-02 · Deepens `docs/cycles/02-fast-stress.md` (v1.0) — does not contradict its
F1–F7 designs, its §3 episode chronology, or its measured synthetic bounds (92/98 planted episodes
≥15d crossing the 0.3 threshold at median lag 1 day; the falsified 73/98-at-0.5 history) — every
one is cited here, never re-derived. Companion file: `research/cycles/faststress-upgrade/
partDH-upgrade.md` (Parts D, E, F, H — the evidence ledger, seat status, new designs FS-D1/FS-D2,
and the knowledge ledger); together the two files span the full A–H standard. This file supplies
the theory those designs test (Part A), the psychology of running the seat (Part G), the
cross-country and India case record the taxonomy is read against (Part B), and the India data
engineering the whole seat depends on (Part C). Scope: `docs/CYCLE_ATLAS.md` rows 5.1 (volatility
clustering, Tier A), 5.2 (VIX term-structure states, Tier B), 5.3 (funding-stress episodes, Tier
B) — all **REGIME (fast) → L2**. Code: `quant/ladder/fast_stress.py`, `quant/ladder/phase.py`,
`quant/ladder/exclusion_calendar.py`. Governed by `research/CONTRACT.md`; every citation below is
search-verified as of September 2026 unless tagged `[VERIFY: ...]`.*

The through-line, stated once and held throughout: **the fast layer reads risk states, never
return signals.** It is the only part of the stack permitted to act in days rather than months or
years, and its three legs — realized volatility, VIX term structure, funding stress — are three
readings of the *same* underlying impairment (market and financial "machinery" struggling to
absorb order flow and satisfy funding claims) taken at different phases of a single episode, not
three independent phenomena. Everything below formalizes, historicizes, and operationalizes that
one sentence.

---

## PART A — Theory: the full machine, formalized

### A.1 ARCH/GARCH formally — the mathematical statement of "vol clusters"

Mandelbrot's 1963 observation, already the opening citation of `docs/cycles/02-fast-stress.md`
§1.1, is a description. Engle (1982), "Autoregressive Conditional Heteroscedasticity with
Estimates of the Variance of United Kingdom Inflation," *Econometrica* 50(4): 987–1008
**[Verified]**, made it a *model*: the conditional variance of a shock is itself a function of
past squared shocks, so large shocks (of either sign) raise the variance investors should expect
of the *next* shock — an ARCH(q) process writes `σ²_t = ω + Σ_{i=1}^{q} α_i ε²_{t-i}`. Bollerslev
(1986), "Generalized Autoregressive Conditional Heteroskedasticity," *Journal of Econometrics*
31(3): 307–327 **[Verified]**, generalized this to GARCH(p,q) by letting the conditional variance
depend on its own recent past as well as on past squared shocks — parsimoniously capturing the
long, slowly-decaying memory Engle's finite-lag ARCH needed many parameters to approximate. The
canonical GARCH(1,1),

```
σ²_t = ω + α·ε²_{t-1} + β·σ²_{t-1}
```

is the object almost every applied vol-clustering claim in finance ultimately reduces to. Three
formal properties do the entire explanatory work this monograph needs from the model:

**(i) The persistence sum `α+β` is the formal content of "vol clusters."** A shock to `ε²_{t-1}`
raises `σ²_t`, which (through the `β·σ²_{t-1}` term) keeps elevating `σ²_{t+1}, σ²_{t+2}, ...`
geometrically at rate `(α+β)` — the process is covariance-stationary (a well-defined unconditional
variance `ω/(1-α-β)` exists) if and only if `α+β < 1`, and the closer `α+β` sits to 1, the longer
a vol shock's memory. This is not a metaphor for clustering — it *is* clustering, stated as a
parameter. Empirically, equity-return GARCH(1,1) fits routinely return `α+β` in the 0.95–0.99
range across markets and eras — vol is highly persistent but (almost always) mean-reverting, never
literally a permanent regime shift on the strength of one shock.

**(ii) The half-life mapping makes persistence legible as a time unit.** Because a unit shock to
`σ²_t` decays at rate `(α+β)` per period, the number of periods for half the shock's excess
variance to dissipate is

```
τ½ = ln(0.5) / ln(α+β)
```

— e.g. `α+β = 0.97` on daily data gives `τ½ ≈ 22.8` trading days (`ln0.5/ln0.97 ≈ 22.76`), squarely
inside the `tau_half_months: [1, 3]` band already frozen for L2 in `config/ladder.yaml` (sourced
there, honestly, to a single India VIX lead-lag episode — Mar-2020 — pending the multi-episode
table F1 pre-registers). This is the formal machinery underneath F1's "bias-corrected AR(1) on the
daily composite": the composite is not literally a GARCH conditional variance, but its own
persistence is estimated by the identical logic — an AR(1) coefficient `φ` on the composite plays
exactly `(α+β)`'s role, and `τ½ = ln(0.5)/ln(φ)` is the same formula applied one level up the
construction, from raw variance to the assembled stress state.

**(iii) Why persistence, not periodicity, is the right object.** A GARCH process has no
"wavelength" — it has a decay rate. This is precisely the atlas's own epistemic discipline (§0,
"persistence, not periodicity") applied at the fastest possible frequency: volatility clustering
passes the clock test's *spirit* trivially (there are effectively infinite "episodes" of clustering
in any long return series) while failing its letter in the interesting way — there is no fixed
period between spikes, only a state variable that decays with an estimable half-life. This is why
row 5.1 of the atlas is Tier **A** while row 5.3 (funding stress) is Tier **B**: the *mechanism*
(persistence in conditional variance) is estimated on effectively unlimited observations in any
market with a long return history, while the *episode-level* rules L2 actually trades (thresholds,
confirm logic, re-entry) have only the ≈14 India episodes named in `02-fast-stress.md` §3 to learn
from — the same Tier-A-mechanism/Tier-B-application split the credit-cycle monograph draws for its
own seat (`research/cycles/credit-deep/partA-theory-psychology.md` §A.12).

### A.2 Realized-volatility estimators: close-to-close vs. the range family

`fast_stress.py`'s `realized_vol()` is, honestly described, the simplest member of the estimator
family: a trailing sum of **squared close-to-close returns**, annualized —
`σ̂²_t = (252/w) Σ_{i=t-w+1}^{t} r_i²`. This is unbiased under a random-walk assumption but is
*statistically inefficient*: it uses one number (the close) per trading day and discards the
entire intraday path. Parkinson (1980), "The Extreme Value Method for Estimating the Variance of
the Rate of Return," *Journal of Business* 53(1): 61–65 **[Verified]**, showed that the day's
high-low range carries far more information about that day's diffusion variance than the
close-to-close move alone, under a continuous, driftless, zero-jump price process:

```
σ̂²_Parkinson = (1 / (4·n·ln2)) · Σ_i [ln(H_i/L_i)]²
```

— an estimator Parkinson shows is roughly **five times more statistically efficient** than the
close-to-close estimator for the same sample size (i.e., achieves the same estimation precision
with a fifth as many observations), precisely because the range captures information about the
path the close alone throws away. Garman & Klass (1980), "On the Estimation of Security Price
Volatilities from Historical Data," *Journal of Business* 53(1): 67–78 **[Verified]**, refine this
further by also using the open and close, not merely the high and low:

```
σ̂²_GK = (1/n) Σ_i [ 0.5·(ln(H_i/L_i))² − (2·ln2 − 1)·(ln(C_i/O_i))² ]
```

reporting a further efficiency gain over Parkinson alone `[VERIFY: the exact multiplier commonly
cited (~7.4× close-to-close) — figures in the literature range from roughly 6× to 8× depending on
the benchmark process assumed; treat the qualitative ordering (GK > Parkinson > close-to-close) as
the load-bearing fact, not a single point estimate]`. **Why this matters specifically for India:**
NSE bhavcopy publishes daily open/high/low/close (plus volume and deliverable-volume) for every
listed security and every index, free, back to the 1990s — the entire range family is
constructible at zero marginal data cost the moment a builder moves past `fast_stress.py`'s
current close-to-close construction. This is a stated, honest gap, not a criticism of the frozen
module: `02-fast-stress.md` §4 documents the realized-vol input as "trailing RV... on the book
benchmark index" without specifying the estimator family, and the range family is the natural
upgrade path once the data phase begins — it shrinks the estimation-noise band around the RV
percentile rank without changing a single design decision F1–F7 already froze, since the *input*
these designs consume is a percentile rank, agnostic to which unbiased-or-better estimator feeds
it. One genuine caveat travels forward to Part C §C.5: range estimators assume the observed
high-low span reflects the *true* intraday range, an assumption a circuit-halted session violates
by construction.

### A.3 The leverage effect formalized: GJR-GARCH and EGARCH

`02-fast-stress.md` §1.3 already cites French-Schwert-Stambaugh (1987) for the empirical
leverage-effect finding — falls raise future volatility more than equal-sized rallies. Symmetric
GARCH(1,1) cannot express this (variance depends on `ε²_{t-1}`, which discards the *sign* of the
shock). Two extensions supply the missing asymmetry term. Glosten, Jagannathan & Runkle (1993),
"On the Relation between the Expected Value and the Volatility of the Nominal Excess Return on
Stocks," *Journal of Finance* 48(5): 1779–1801 **[Verified]**, add an indicator-weighted term
(GJR-GARCH):

```
σ²_t = ω + α·ε²_{t-1} + γ·I_{t-1}·ε²_{t-1} + β·σ²_{t-1},   I_{t-1} = 1 if ε_{t-1} < 0, else 0
```

so a negative shock of a given size raises next-period variance by `(α+γ)` rather than merely
`α` — `γ > 0` is the formal statement of "falls raise vol more than rallies," estimated, not
assumed. Nelson (1991), "Conditional Heteroskedasticity in Asset Returns: A New Approach,"
*Econometrica* 59(2): 347–370 **[Verified]**, takes a different route (EGARCH), modeling `ln(σ²_t)`
directly as a function of both the *size* and the *sign* of the standardized shock
`z_{t-1} = ε_{t-1}/σ_{t-1}`:

```
ln(σ²_t) = ω + β·ln(σ²_{t-1}) + α·(|z_{t-1}| − E|z_{t-1}|) + γ·z_{t-1}
```

which has two practical advantages GJR lacks: modeling `ln(σ²)` guarantees `σ²_t > 0` for any
parameter values (no non-negativity constraint to enforce), and a negative `γ` again encodes the
leverage effect while additionally allowing volatility persistence and the asymmetry's *sign*
response to be estimated independently of the response's *magnitude*. **What this buys the design,
stated exactly per the "for our state variable" convention the credit-cycle monograph uses:**
neither GJR nor EGARCH is *fitted* anywhere in the frozen L2 module — `fast_stress.py`'s composite
is a percentile-ranked sum of levels, not a parametric variance forecast — but the asymmetry these
models formalize is precisely why L2's drawdown-depth input (input #2, "how bad already") is not
redundant with the realized-vol input (input #1): a symmetric-GARCH world would let RV alone infer
the fall, but the leverage effect means a fall of given magnitude typically arrives *with* a larger
vol response than an equal rally, so a state variable built from RV rank alone would under-weight
exactly the tail episodes the drawdown-ceiling constraint (`CONTRACT.md` §3) cares about — the
formal reason two structurally different inputs (a vol level and a drawdown level) belong in one
composite rather than one alone standing as a sufficient statistic for the other.

### A.4 Vol-targeting math: `c/σ̂²` vs. `c/σ̂`, the drawdown-transformation property, and the Cederburg protocol

Dossier D04 and `02-fast-stress.md` §2 already carry Moreira & Muir (2017), "Volatility-Managed
Portfolios," *Journal of Finance* 72(4): 1611–1644 **[Verified]**, and Harvey, Hoyle, Korgaonkar,
Rattray, Sargaison & van Hemert (2018), *Journal of Portfolio Management* 45(1): 14–33
**[Verified]**, as the two poles of the sizing-rule literature. What has not yet been formalized is
*which functional form* each camp actually uses, and why the difference is not cosmetic. Moreira-
Muir scale exposure by the **inverse of trailing realized variance**, `w_t = c/σ̂²_{t-1}`, choosing
`c` so the managed strategy's full-sample volatility matches the unmanaged benchmark's; the
"industry-norm" vol-targeting/risk-parity convention (as practiced by CTAs and vol-target mandates
generally) instead scales by the **inverse of trailing volatility**, `w_t = c/σ̂_{t-1}`, targeting a
constant *volatility* contribution rather than a constant *variance* contribution.

**The formal distinction, made precise.** Differentiate each rule with respect to `σ`:
`d(c/σ)/dσ = −c/σ²` (elasticity of exposure w.r.t. `σ` is exactly `−1`), while
`d(c/σ²)/dσ = −2c/σ³` (elasticity is exactly `−2`). Moreira-Muir's rule is **twice as elastic**:
it de-levers twice as fast, in percentage terms, for a given percentage rise in measured
volatility — and, the mirror-image consequence, **re-levers twice as fast** for a given percentage
*fall*, precisely in a long calm stretch. This is the formal bridge to a finding already established
in this monograph's own sibling chapter: Adrian & Shin (2010)'s VaR-budget mechanism (`credit-deep
partA` §A.8, `L ≤ (VaR-budget/z)/σ_portfolio`) is a `c/σ` rule at the institutional level, and
Brunnermeier & Sannikov (2014)'s volatility paradox (`credit-deep partA` §A.7) names exactly the
danger a *steeper* elasticity amplifies: a rule leaning harder into low measured volatility
manufactures more leverage in the calm exactly when shock-absorption capacity is quietly being used
up — the same mechanical amplifier the credit monograph documents for bank balance sheets, here
operating inside the sizing rule itself. This is not an argument against `c/σ²` — it is precisely
what raises Sharpe on the *return-factor* side, Moreira-Muir's own point — but it is the honest
reason `02-fast-stress.md` §1.4 states the alpha claim as contested while treating drawdown control
as robust: the more elastic rule buys more of both the upside and the pro-cyclical downside, the
less elastic industry norm buys less of either.

**The drawdown-transformation property, stated honestly (mechanism, not a new proof).** Both rules
share one structural limit worth stating precisely rather than assuming away: because `σ̂_{t-1}` is
estimated from *trailing* data, the rule is reactive, never anticipatory — a genuine vol spike at
`t` is sized against the *pre-spike* `σ̂_{t-1}`, so the position entering the spike is exactly the
pre-spike size, and only the *subsequent* exposure is cut. This is the same honest limit
`02-fast-stress.md` §4 states for L2 itself ("detection is high but NOT total... median lag 1
day") — a vol-scaled sizing rule and a percentile-ranked stress composite share the identical
reactive character, because both are built from the same trailing-window raw material. What the
literature shows empirically (Harvey et al.'s 60-asset, ~90-year sample; Barroso & Santa-Clara
2015's momentum-crash result, already cited in `02-fast-stress.md` §2) is that this one-period-late
cut is still enough to compress the realized left tail materially, because vol clustering (A.1)
means the *subsequent* days of an episode — typically the majority of its cumulative damage — are
faced at reduced size. The transformation is therefore a **statement about the shape of the
realized return distribution, conditional on the sizing rule having been running throughout an
episode, not a claim that the first shock is dodged.**

**The Cederburg real-time protocol, specified.** Cederburg, O'Doherty, Wang & Yan (2020), "On the
Performance of Volatility-Managed Portfolios," *Journal of Financial Economics* 138(1): 95–117
**[Verified]** — the paper `02-fast-stress.md`'s evidence table cites by author list alone; this
chapter supplies its title and the exact protocol it tests against Moreira-Muir. "Real-time" means:
at each rebalance date `t`, the scaling constant `c` (or, equivalently, any normalization applied to
match a target volatility) is calibrated using **only information available through `t`** — no
full-sample constant fitted with knowledge of when the high-vol/low-realized-return periods
occurred within the sample, which would smuggle look-ahead into the very comparison the paper
exists to make honest. Judged this way, and against a bootstrapped null accounting for
parameter-estimation uncertainty (not merely in-sample point estimates), Cederburg et al. find no
statistically or economically robust Sharpe improvement for **most** of the equity factors Moreira-
Muir test, with the **market factor** the one relatively robust exception — precisely the finding
`02-fast-stress.md` F3 already freezes as its stated prior ("DD control robust, alpha unproven") and
the reason F3 requires *both* the full-period Moreira-Muir construction *and* this real-time
protocol run side by side on India data, with "either result documented" rather than the favorable
one promoted alone.

### A.5 VIX construction formally: the model-free implied-variance integral

The object India VIX estimates is, formally, the risk-neutral expected quadratic variation of the
log-price process over a fixed horizon (30 calendar days) — not a forecast built from any single
model of how prices move, but a **price**, extracted from a static portfolio of traded options.
The theoretical result making this possible is Britten-Jones & Neuberger (2000), "Option Prices,
Implied Price Processes, and Stochastic Volatility," *Journal of Finance* 55(2): 839–866
**[Verified]**: for any continuous price process consistent with a given set of European option
prices at a single maturity, the risk-neutral expected total variance over that maturity is pinned
down *without* specifying the volatility process at all — the "model-free" property. The
replicating-portfolio intuition behind it — that a log-contract payoff (equivalently, realized
variance) can be statically replicated by a continuum of out-of-the-money puts and calls weighted
by `1/K²` — is worked out in practitioner form by Demeterfi, Derman, Kamal & Zou (1999), "More Than
You Ever Wanted to Know About Volatility Swaps," Goldman Sachs Quantitative Strategies Research
Notes (also *Journal of Derivatives* 6(4): 9–32) **[Verified]**. The discretized version the CBOE
adopted in 2003 and NSE licenses for India VIX (per the NSE white paper cross-referenced in
dossier D04 and confirmed via the NSE India VIX computation-methodology document) is, in essence,

```
σ² = (2/T) · Σ_i (ΔK_i / K_i²) · e^{RT} · Q(K_i)  −  (1/T) · [F/K₀ − 1]²
```

— `T` the time to expiry, `F` the forward index level (from put-call parity), `K₀` the first strike
at or below `F`, `K_i` each out-of-the-money strike, `ΔK_i` the strike interval, `Q(K_i)` the
midpoint of the best bid-ask quote for that strike, `R` the risk-free rate. India's NSE
implementation applies **natural cubic-spline interpolation** across the Nifty option order book's
best bid-ask quotes to fill strikes without a clean two-sided quote, computes this variance
separately for the near-month and next-month expiries, and combines the two by **linear
time-weighting to a constant 30-calendar-day maturity** — Whaley (1993), "Derivatives on Market
Volatility," *Journal of Derivatives* 1(1): 71–84 **[Verified]**, is the applied-finance paper that
first proposed exchange-traded volatility derivatives along these lines, predating the model-free
refinement by a decade and still the correct citation for the *concept* of a tradable "investor
fear gauge," distinct from Britten-Jones-Neuberger's formal justification for the specific
model-free construction. **The one-sentence design consequence:** India VIX is best understood not
as a prediction of future volatility but as **the square root of an annualized 30-day variance-swap
rate embedded in the live Nifty option chain** — a price set by whoever is currently willing to
buy and sell that variance, which is precisely why `02-fast-stress.md` §1.5 and dossier D04 both
already describe it as a same-day-to-few-days *reactive* confirm, never a multi-week early warning:
a price cannot lead the information the market pricing it already has.

### A.6 Term structure: contango, backwardation, and the variance risk premium

**Why the term structure is a distinct object from the VIX level.** In ordinary conditions, the VIX
term structure slopes upward (contango): far-dated implied variance normally prices in more
event-risk uncertainty than the near term, plus a structural variance risk premium that compounds
with horizon. Whaley (2000), "The Investor Fear Gauge," *Journal of Portfolio Management* 26(3):
12–17 **[Verified — standard attribution and title; page range cross-checked via multiple
secondary citations]**, frames the VIX *level* explicitly as a fear gauge whose spikes track
market stress contemporaneously. The **Carr-Wu lineage** of variance-swap-curve work — Carr & Wu
(2009), "Variance Risk Premiums," *Review of Financial Studies* 22(3): 1311–1341 **[Verified]** —
adds the term-structure refinement this seat's atlas row 5.2 is built on: acute stress **inverts**
the curve, because the insurance bid concentrates at the *front* of the curve (a panicking market
wants protection *now*, not in three months), while far-dated implied variance, anchored more to a
structural risk premium than to the immediate shock, rises by less. **Backwardation — near-dated
implied variance exceeding far-dated — is therefore a purer, level-independent stress signature
than the VIX level alone**, because a persistently elevated-but-flat or contango curve can simply
reflect a regime of generally higher uncertainty (post-2020's higher average VIX floor, for
instance) rather than an acute, currently-unfolding shock. This is exactly the object
`partDH-upgrade.md`'s **FS-D1** design pre-registers as distinct from F5: F5 tests whether the VIX
*level*'s rank is redundant with realized-vol rank; FS-D1 tests whether the term-structure
*backwardation flag* adds incremental information over both.

**The variance risk premium, formalized.** Define, for horizon `τ`, `VRP_t = E^Q_t[RV_{t,t+τ}] −
E^P_t[RV_{t,t+τ}]` — the gap between the risk-neutral (option-implied) expectation of future
realized variance and the physical (statistical) expectation of the same quantity. Because the true
physical expectation is unobservable, the empirical literature (Bollerslev, Tauchen & Zhou (2009),
"Expected Stock Returns and Variance Risk Premia," *Review of Financial Studies* 22(11): 4463–4492
**[Verified]**) approximates it with the **most recently realized** variance under a persistence
assumption, giving the tractable proxy `VRP_t ≈ IV²_t − RV_{t-τ,t}` — precisely the "IV−RV spread"
`02-fast-stress.md` §4 already names as a confirm-input candidate and F5 registers for its own
pre-registration before any use. BTZ's headline finding is that this VRP proxy predicts aggregate
equity returns at a roughly quarterly horizon in a way plain valuation ratios miss: a wide,
positive VRP (implied rich relative to recently realized) predicts *higher* subsequent returns,
consistent with VRP as compensation for bearing variance/tail risk that rises precisely when
risk-bearing capacity is scarce — a direct complement to A.7's funding-liquidity story below (the
price of insurance rises exactly when funding-constrained intermediaries are least able to sell
it). **This is the literature `02-fast-stress.md`'s own honest caveat gestures at without naming**
("Options / VRP... not really a decaying edge... a genuine, structural risk premium," dossier D04
§3) — it is now named, and it is a *predictive-alpha* literature distinct from and additional to
the *risk-state* use F5/FS-D1 make of the same spread; the design discipline (never promoting the
alpha use from a level not yet earned) is unchanged.

### A.7 Funding stress formally: the margin spiral and the CP-spread thermometer

Brunnermeier & Pedersen (2009), "Market Liquidity and Funding Liquidity," *Review of Financial
Studies* 22(6): 2201–2238 **[Verified]**, formalize two distinct, mutually-reinforcing feedback
loops — the correct theoretical anchor for atlas row 5.3, and the reason "funding stress" and
"market-liquidity stress" are related but formally separable objects.

**The margin spiral.** A financier sets a speculator's margin (haircut) `m_t` as an increasing
function of recent volatility or illiquidity, `m_t = f(σ̂_t)`, `f' > 0`. A price shock raises
`σ̂_t` (vol clustering, A.1), which mechanically raises the margin required, forcing deleveraging
independent of any change in the speculator's own fundamental view. This is *formally identical in
structure* to Geanakoplos's leverage-cycle mechanic already formalized for the credit seat
(`credit-deep partA` §A.6, `L = 1/h`) — here the financier moves the haircut in response to
*measured volatility* specifically, rather than to a slower-moving fundamental-risk reassessment,
which is exactly why this loop runs on a **days-to-weeks** clock rather than the credit cycle's
multi-year one.

**The loss spiral.** Forced deleveraging (from the margin spiral, or from an ordinary fundamental
loss) depresses the asset's price through price impact, which itself raises measured volatility and
widens the bid-ask/reduces depth — the market-maker-withdrawal mechanism `02-fast-stress.md` §1.2
already states in prose ("market-makers widen and withdraw when inventory risk rises") — feeding
straight back into the margin spiral. Brunnermeier-Pedersen's own formal condition for these loops
to be **destabilizing** (rather than merely reflecting risk) is that a shock to fundamental
volatility raises margins by *more* than the shock itself warrants on fundamentals alone — a
condition that binds hardest precisely when speculators/intermediaries are *already* capital-
constrained, i.e., already highly levered going in. **This is the same physics as the credit
cycle's Minsky/Kiyotaki-Moore mechanism (`credit-deep partA` §§A.2, A.4), read at a different clock
speed**: L10 asks whether balance sheets have accumulated the *vulnerability* over years; L2 asks
whether the *spiral* is actively running over days-to-weeks. The two seats are not redundant
because they are not measuring the same *stock* — L10 measures the slow-moving precondition, L2
measures the fast-moving unwind — but they are reading one underlying mechanism at two
resolutions, exactly as A.8 below formalizes for the resolution question generally.

**The CP-sovereign spread as balance-sheet thermometer.** Krishnamurthy & Muir (2017/2025), "How
Credit Cycles across a Financial Crisis" (already verified in `credit-deep partB` §B1.7), show that
credit **spreads** compress to unusually low levels while credit **quantities** simultaneously
accelerate — a "quiet before the storm" signature that is priced continuously, unlike quantities,
which are observed with a lag. The commercial-paper-to-Treasury-bill (or CP-to-CD) spread at
matched tenor is the *identical object*, read at a shorter tenor and a faster clock: a widening CP
spread over the risk-free rate is the shadow-banking sector's own external-finance premium
(Bernanke-Gertler-Gilchrist's `s = s(N/K)`, `credit-deep partA` §A.5) repricing in near-real-time
on the very instrument (short-term rollover paper) whose failure to roll *is* the crisis mechanism
in an endogenous funding freeze — the design logic `research/cycles/shadow-deep/partC-data.md`
§C.1 already builds its "freeze index" around (`z(CP spread) + z(−rollover ratio)`, both from RBI's
Weekly Statistical Supplement).

**Why funding leads equity vol in credit-transmission crises but lags in exogenous shocks — the
order-of-arrival taxonomy, formalized.** `partDH-upgrade.md` Part D already states this taxonomy as
a pre-registered *classification*, diagnostic never predictive: credit-transmission crises run
**funding → vol → drawdown** (2018: CP spreads widened before index vol); exogenous shocks run
**vol → drawdown → funding-if-at-all** (2020, 2024-election). This chapter supplies the mechanism
argument for *why* the order differs. In an **endogenous** credit-cycle bust (IL&FS 2018), the
funding stress *is* the trigger itself: an asset-liability-mismatched shadow lender's own inability
to roll commercial paper precedes, by construction, the second-order consequence (credit
contraction reaching NBFC-dependent developers, consumers, and the borrowers financed by that
paper) that eventually moves the equity index — funding necessarily leads because the shock
originates *inside* the funding market. The `shadow-deep` SC1 trial (2026-09-02, real India factor
data) measured exactly this signature on the IL&FS window: the small-cap (SMB) factor sat at the
18th percentile of all rolling 12-month windows since 1994 while the market factor sat at the 16th
— *both* legs stressed, the funding-adjacent leg marginally more so, the freeze "propagated to a
broad macro event within 12 months" rather than staying contained — the ledger's own honest reading
is that this is "the case for routing the signature to L2 (faster variables), not for equity-factor
detection," because a *monthly* construction is simply the wrong clock to resolve a days-to-weeks
lead cleanly, the identical resolution-loss lesson A.8 develops next for vol clustering itself. In
an **exogenous** shock (COVID, March 2020), the trigger arrives from *outside* any domestic balance
sheet — a global shock with no antecedent India credit boom — and hits equity volatility first and
hardest (§B.1.4); funding stress (a global dash-for-cash, the Fed's Commercial Paper Funding
Facility and Money Market Mutual Fund Liquidity Facility both stood up within a single week of the
equity trough) follows *within* the same acute window, because the loss spiral (mechanism 2 above)
runs without the margin spiral having built up first through a multi-year domestic credit boom —
everyone delevering simultaneously for the same exogenous reason, not because any one balance
sheet's own prior vulnerability was discovered. **This is a mechanism argument, not a graded
result**: the formal test on real vaulted daily data (dating each leg's first top-decile print,
episode by episode) is `partDH-upgrade.md`'s own **FS-D2**, registered and awaiting the runsheet
pulls Part C specifies; §B's case narratives are the chronology FS-D2 will be graded against, not a
substitute for that grading.

### A.8 The multi-resolution point: what our own FS-U1/FS-U2 prints teach

`research/register/trial-ledger.md`'s Entries FS-U1/FS-U2 (2026-09-02) are this seat's first prints
on real (though monthly-resolution) data, and they are cited here **verbatim, as the only desk
numbers this chapter is permitted to cite for this seat, alongside the synthetic bounds already
printed in `02-fast-stress.md`.** FS-U1 (India market factor, monthly |return|, 1993–2025): the
autocorrelation of `|ret|` at lags 1–6 runs **0.141–0.188**, all positive, with a Ljung-Box
statistic `Q(6) = 60.3`, `p = 4e-11`. FS-U2 (gold, float era, monthly |log return|, 1972–2026):
ACF(1–6) **0.170–0.245**, all positive, `Q(6) = 166.3`, `p = 3e-33`. Both pass their pre-registered,
two-legged bar (Ljung-Box `p < 0.05` on lags 1–6 **and** a positive lag-1 autocorrelation) decisively.

**What this demonstrates, exactly as the ledger frames it.** These are *monthly-resolution
demonstration trials*, not a re-estimation of anything F1–F7 need — their purpose is threefold: (a)
a **Cycle School chart**, computed by the desk itself rather than cited from elsewhere; (b) a
**library-integrity check** — a failure here would indict the vaulted return library or the
monthly-aggregation claim, not the underlying daily-frequency fact, which is Tier A globally on
data reaching back to the earliest available return series in every liquid market; and (c) an
honest **measurement of what monthly aggregation destroys**. That measurement is the number worth
sitting with: **0.15–0.19 at monthly resolution against the ~0.2–0.4 typical of daily |return|
autocorrelation** in the literature (the ledger's own framing, cited verbatim). Roughly half the
clustering signal's *magnitude* is lost by aggregating from daily to monthly, even though its
*statistical significance* survives overwhelmingly (`p` values of `4e-11` and `3e-33` are not close
calls) — the two facts are not in tension: significance is a function of sample size as well as
effect size, and a 30-year monthly series still carries hundreds of observations, enough to detect
a halved effect with high confidence even as the effect itself shrinks.

**What survives aggregation and what doesn't, stated mechanically.** A month that contains a
three-day vol spike compresses that spike's *entire internal dynamics* — the day the shock lands,
the day-after burst, the multi-day decay — into a single elevated monthly `|return|` observation.
The *coarse* persistence signature (an elevated month tends to be followed by another elevated
month) survives, because vol clustering operates at every clock speed from days to years — this is
precisely the content of Andersen & Bollerslev (1998), "Answering the Skeptics: Yes, Standard
Volatility Models Do Provide Accurate Forecasts," *International Economic Review* 39(4): 885–905
(already cited in `02-fast-stress.md` §2's evidence table), whose central finding is that GARCH-
family forecasts, dismissed as poor at short horizons by naive `R²` metrics, are in fact accurate
once judged against the right (realized-vol-based) benchmark — vol *is* forecastable, at multiple
horizons, once measured correctly. What does **not** survive is the *fine* structure — the phase
object's own **velocity** dimension (`quant/ladder/phase.py`), which distinguishes a state reached
while rising from one reached while falling, needs the daily onset-then-decay shape a monthly
aggregate erases by construction; a monthly composite could not distinguish "day 1 of a spike" from
"day 20 of its decay" even though both might land in the same elevated month. **This is the exact,
measured reason `02-fast-stress.md` §4 builds L2 at daily cadence on bhavcopy rather than at the
monthly resolution this section's own demonstration trials use** — the demonstration exists to
*prove the aggregation loss is real and quantify it*, not to argue the seat should operate at the
resolution the demonstration happens to be computed at.

---

## PART G — Operator psychology

The theory above describes a system whose own physics — margin spirals, leverage-elastic sizing
rules, reactive-by-construction estimators — punishes hesitation in one direction and impulsivity
in the other. This Part is about the desk that has to act on a state reading built entirely from
trailing data, in an environment (screaming headlines, real capital, real drawdown) engineered by
evolution and institutional incentive to make exactly the wrong response feel natural.

### G.1 Acting in days without predicting — the discipline distinction

**The temptation.** L2 is the one seat on the entire ladder explicitly licensed to move the book in
days rather than months (`02-fast-stress.md` §1.5: "it arms de-risking fast... it never predicts
the spike itself"). The felt experience of watching a percentile rank cross a threshold *feels*
like having called something — the natural human narrative is "I saw it coming," when the honest
description is "the state variable crossed a pre-registered line after the fact of the vol
clustering that produced it." A.5's own formal point (VIX is a price, not a forecast) and A.4's own
honest limit (sizing is reactive, calibrated on trailing `σ̂`) both foreclose the forecasting
narrative at the level of mathematics, not merely as a stated humility — an operator who reads a
correct de-risk signal as evidence of predictive skill is making a category error the module's own
construction cannot support, and will be tempted, the next time markets are calm, to look for the
next thing to "call" rather than wait for the next threshold crossing.

**The countermeasure.** The discipline is structural, not attitudinal: F2's decision rule fires
mechanically at a pre-registered percentile grid (0.8/0.9/0.95) with pre-registered confirm logic
(1-of-3, 2-of-3) — there is no discretionary "I think this one's different" step between the state
reading and the bucket-cut mapping. The operator's job is to execute the pre-registered rule
promptly, not to add a forecast on top of it; any temptation to override in either direction (act
early on a hunch, or delay because "this feels like noise") is precisely the discretionary
insertion the frozen-parameter design (`CONTRACT.md` §6, "no fixed thresholds... presented as
truth," read alongside §9's ban on re-testing a rejected idea with tweaked parameters) exists to
foreclose.

### G.2 The de-risk decision under screaming headlines

**The mechanism.** A genuine fast-stress episode arrives, definitionally, with headlines that
scream — that is what "fast" and "stress" mean together. The operator faces a state reading that
has crossed the pre-registered threshold *and* a stream of information (a specific news event, a
specific number, a specific narrative about why *this* episode is different from the drill) that
argues for waiting one more day "to see how this resolves." This is the identical psychological
trap G.1 of the credit-cycle monograph documents for its own seat (`credit-deep partA-theory-
psychology.md` §G.1, "this time is different") running on a compressed, days-not-years clock: the
same diagnostic-expectations mechanism (Bordalo, Gennaioli & Shleifer, already verified in
`credit-deep partA` §A.11) that makes an operator over-weight a compelling boom narrative also
makes them over-weight a compelling "wait for confirmation" narrative during an acute selloff,
because both narratives are, in the moment, *locally* plausible — headlines genuinely do carry real
information, which is exactly what makes waiting for "one more data point" feel prudent rather than
reckless.

**The countermeasure.** Pre-registered thresholds exist precisely to remove this decision from the
moment it is hardest to make well. F2's grid was frozen *before* any specific episode's headlines
existed to argue against it; F6's false-fire ledger prices the cost of acting on every threshold
crossing whether or not it turns out to have been "real" (G.4 below); the discipline is: **the rule
fires, the operator executes, the post-mortem happens on schedule, never mid-episode.** "Wait for
confirmation" is not banned as a concept — it is *already inside* the rule, as the pre-registered
1-of-3/2-of-3 confirm logic F2 specifies — the failure mode is adding a *second*, informal
confirmation layer on top of the one already frozen, which is functionally identical to the
credit-cycle monograph's G.1 override, applied at L2's own, much faster clock.

### G.3 The re-entry problem as the harder half: selling is forced, re-buying is a choice

**The asymmetry, stated precisely.** A pre-registered de-risk rule, once its threshold trips, is a
*forced* action — there is no discretion left once F2's grid says cut. Re-entry has no equivalent
forcing function: `02-fast-stress.md` §4 states plainly that re-entry "follows the per-sleeve
re-entry rules... never a reflex," and `research/OPEN_QUESTIONS.md` Q8 makes re-entry a first-class,
per-sleeve research item precisely because no single global re-entry rule exists to mechanically
trigger the way a de-risk threshold does. This is where hesitation costs compound in a way exit
costs typically do not: an exit that fires one day late costs, at most, one day's incremental
drawdown before the pre-registered rule catches up; a re-entry delayed by the *same* psychological
mechanism (waiting for one more confirming day, one more calm headline) costs the operator the
early, steepest part of a recovery — the portion of a V-shaped bounce that, by construction, cannot
be recovered later at the same price.

**The evidence this isn't merely intuition.** The trial ledger's own **J5** entry (2026-09-01,
credit-cycle H66 preliminary, cited here as a cross-seat prior rather than an L2-specific result)
found crisis probability and forward drawdown roughly *equal* between the U (rising) and D
(falling-from-high) phase quadrants at matched levels — but median forward 3-year real equity
return sat at **+22.5% for D vs. +13.1% for U**: "phase asymmetry may live in RE-RISKING (returns),
not crisis prediction" — exploratory, not yet a graded L2 result, but a directly on-point prior for
why `02-fast-stress.md` §4 already treats the D quadrant as "the candidate re-entry regime,"
gated rather than dismissed. Daniel & Moskowitz (2016), already in `02-fast-stress.md`'s own
evidence table, locate momentum crashes specifically in "panic states... during REBOUNDS" — the
same phase (falling-from-high, recovering) that is mechanically the hardest for an operator to act
in, because acting requires *buying into* a market that has just finished scaring everyone,
precisely when the "wait for confirmation" narrative (G.2) is loudest and, this time, aimed at the
opposite trade.

**The countermeasure.** Because no single mechanical re-entry rule is frozen yet (Q8 is an open
research item, not a settled default), the interim discipline is procedural rather than parametric:
phase D is logged and displayed everywhere but "may not condition any traded rule until H66–H68
pass their pre-registered tests" (the identical consumption-gate language `credit-deep partA` §G.6
documents for its own phase object) — F7 is this seat's own version of that gate, and its explicit
purpose is to convert "the storm looks like it's passing, so re-lever" from a discretionary read
into a tested one before any capital acts on it. Until F7 passes, the honest operator posture is:
hesitation on the *exit* side is a discipline failure (G.2); hesitation on the *re-entry* side, for
now, is simply what an ungated design correctly requires — the discomfort of that asymmetry is the
cost of not yet having earned a re-entry rule, not evidence one should be improvised.

### G.4 Whipsaw shame: false fires are tuition, not failure

**The mechanism.** `02-fast-stress.md` §4's own measured, synthetic detection bound is stated
honestly: 92 of 98 planted episodes ≥15 days cross the 0.3 threshold (median lag 1 day) — meaning
**6 of 98 are missed**, and the composite's design (percentile-ranked, no clamp) guarantees some
share of threshold crossings will not correspond to a genuine sustained episode at all (a false
fire). An operator who experiences a false fire — de-grossed, hedged up, and then watched the
market recover without incident — feels the sting of having "gotten it wrong," and the natural
response is to lose confidence in the rule, second-guess the *next* threshold crossing, or lobby
informally to loosen the grid — precisely the kind of ad hoc, post-hoc parameter tweaking
`CONTRACT.md` §8 and §9 both exist to foreclose ("do not tune thresholds against backtest Sharpe";
"never re-test a rejected idea with tweaked parameters").

**Why this is a category error.** F6 exists *specifically* to price this cost in advance: "the
de-risk rule must clear the cost-in-SR speed limit per book," measured across "the full
threshold-grid table: false-fire rate, round-trip cost per false fire by book, missed-episode
rate." A false fire that has already been priced into F6's own economics before any capital moved
is not a failure of the rule — it is the rule's designed, budgeted cost of doing business, exactly
as an insurance premium is not a "failure" merely because the insured event didn't occur in a given
year. The measured miss rate (6/98) cuts the same way in the opposite direction: a genuinely
missed episode is *also* not evidence the rule is broken, provided it sits inside the pre-measured
miss rate rather than representing a rate drifting away from what F6 priced.

**The countermeasure.** Whipsaw shame is neutralized the same way `credit-deep partA` §G.2
neutralizes capitulation-at-the-bottom: not by asking the operator to feel differently about a
false fire in the moment, but by having already, in writing, before any specific episode existed,
declared the false-fire rate an acceptable, budgeted cost (F6) rather than a live judgment call
each time one lands. The single sentence that should end any post-false-fire second-guessing: *the
grid was chosen knowing some fraction of its fires would be false — that fraction is F6's own
number, not a surprise.*

### G.5 "The storm is here" vs. "the storm is passing": the phase discipline

**The distinction, restated in operator terms.** A state reading that has crossed the de-risk
threshold answers one question only — *is the storm here, right now* — and the U/rising phase label
is exactly this: "any one arms R4 cuts, two confirm" (`02-fast-stress.md` §4). It answers nothing
about *when the storm passes*, and the D/falling-from-high label exists specifically to name that
different, harder question without licensing an answer to it yet. The psychological hazard is
collapsing these into one judgment — reading "the state is falling from a high level" as
self-evidently meaning "it is now safe to re-risk," which is precisely the over-reading G.3's own
Daniel-Moskowitz citation warns is the exact phase where crashes concentrate, not the phase where
they are guaranteed to be over.

**Why the desk refuses to trade phase D until F7 passes.** This is not caution for its own sake —
it is the direct consequence of A.8's resolution argument and G.3's evidence pattern read together:
a state variable's *level* falling from a high reading is consistent with several different
underlying realities (a genuine, durable de-escalation; a temporary lull inside a still-unresolved
funding freeze per A.7's order-of-arrival taxonomy; a dead-cat bounce inside a slow-bear the trend
overlay, not L2, is built to catch) that look identical at the level of L2's own scalar composite,
and only F7's own pre-registered test ("at matched state LEVELS: forward 1–3m returns and DD, U vs
D... passes ⇒ re-entry rules may condition on D via Challenger, reduce-only first; fails ⇒ phase
stays display-only") can distinguish them with evidence rather than narrative. The discipline is
therefore the mirror image of G.2's: where G.2 forecloses *waiting* past a pre-registered exit
threshold, G.5 forecloses *acting* before a pre-registered re-entry test has actually been run —
both refusals protect the same thing, a decision surface kept clear of in-the-moment judgment,
just applied to opposite sides of the same episode.

### G.6 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Reading a correct de-risk signal as predictive skill | Category error against A.4/A.5's own reactive, price-not-forecast construction | The signal is a *now*-cast, stated as such in `02-fast-stress.md` §1.5; no forecasting claim to feel validated by |
| Waiting "one more day" past a tripped threshold under screaming headlines | Diagnostic-expectations bias applied to disconfirming news, mirroring `credit-deep` G.1 at a compressed clock | Pre-registered F2 grid + confirm logic fires mechanically; confirmation is already inside the rule, not an informal layer atop it |
| Hesitating on re-entry after a forced exit | Selling is forced, re-buying is a choice — no forcing function exists yet (Q8 open); the D-phase panic-rebound pattern (Daniel-Moskowitz, J5) makes the hardest moment to buy coincide with the moment buying matters most | Phase D logged/displayed, consumption-gated behind F7; the discomfort is the correct cost of an ungated design, not evidence to improvise around |
| Whipsaw shame after a false fire | Treating a pre-budgeted cost (F6) as an unexpected failure; urge to loosen the grid post-hoc | F6's false-fire rate is frozen *before* any episode; a false fire inside the measured rate is tuition, not error |
| Collapsing "storm is here" into "storm is passing" | Over-reading a falling-from-high level as itself sufficient evidence to re-risk | F7 gates any D-conditioned trading rule; U arms cuts, D stays display-only until evidence, not narrative, promotes it |

---

## PART B — Cross-country and India cases

**Method, stated once.** Each case below is graded on the three legs — realized/spot volatility,
VIX level and term structure (where the instrument existed), funding stress — and on the *order*
in which each leg showed its own stress, read against the order-of-arrival taxonomy A.7 formalizes
and `partDH-upgrade.md` Part D pre-registers. This is a **literature-and-public-record
reconstruction**, not the same object as **FS-D2**'s own formal grading on vaulted daily India
series (India VIX archive, CCIL dailies) — FS-D2 remains the authoritative, data-gated test; these
cases are the chronology it will be graded against, offered honestly as narrative evidence, never
as a substitute finding. No desk numbers beyond FS-U1/FS-U2 and `02-fast-stress.md`'s own synthetic
bounds appear anywhere below; every historical figure is a public-record fact, search-verified this
session, tagged `[VERIFY]` where a single point figure could not be independently pinned.

### B.1 Four global cases

**1. October 19, 1987 — Black Monday: portfolio insurance as mechanical amplifier.** The Dow
Jones Industrial Average fell **22.6% in a single session** — still the largest one-day percentage
decline in the index's history — with worldwide losses estimated at roughly **$1.7 trillion**. The
Brady Commission's 1988 report concluded that **portfolio insurance** (dynamic hedging via index
futures, managing an estimated **$100 billion** in assets by mid-1987) and index arbitrage were the
central mechanical amplifiers: portfolio insurers accounted for roughly **40% of non-market-maker
futures sales** that day, and the resulting futures-cash basis dislocation drove an estimated
**$1.7 billion** of index-arbitrage stock selling — a rule-driven feedback loop (falling prices →
programmed futures selling → basis dislocation → arbitrage stock selling → falling prices) with
**no VIX to read** (the index did not exist until 1993, and its model-free version not until 2003)
and **no funding-market leg central to the narrative** — no margin call, no CP freeze, drives the
1987 story. **Order-of-arrival: realized volatility only; no VIX leg exists to order against it;
funding stress is essentially absent from the mechanism.** This is the cleanest available
historical instance of a **rule-driven, non-funding, non-informational** volatility event — the
closest global analogue to the taxonomy's later "fast vol without funding stress" pole (§B.2.7
below), and a useful reminder that mechanical amplification through automated, large-scale hedging
flows long predates VIX-linked short-vol products (§B.1.3).

**2. August 24, 2015 — the ETF flash-crash morning.** Ahead of the 9:30am open, the SPDR S&P 500
ETF Trust (SPY) traded more than **5% below its prior close**; by 9:40am it had recovered past its
opening level, eventually closing down **4.2%**. The dislocation inside the open itself was far
more severe than the closing-price move suggests: the **$65 billion iShares Core S&P 500 ETF
(IVV)** fell as much as **26%** intraday — roughly **20 percentage points below its own fair
value** — while only about **half of S&P 500 constituent stocks had opened on the NYSE by 9:35am**,
producing **1,278 trading halts across 471 different ETFs and stocks**, with **302 of 1,569 traded
ETFs (19.2%)** triggering a Limit-Up-Limit-Down pause. The trigger was the same **China devaluation
shock** already seated as CYCLE_ATLAS row 2.11's (China credit impulse) live episode: the CBOE VIX
reached an intraday high of **53.29** that Monday, part of the "largest weekly VIX spike ever" per
the 2015–16 selloff record, as the Shanghai Composite had fallen **43% in the preceding two months**
(June–August 2015). The Dow itself opened down roughly **1,000 points**, recovered nearly half of
that in the first thirty minutes, and closed down **588 points**. **Order-of-arrival: realized
volatility and VIX moved essentially contemporaneously (both are readings of the same opening
dislocation); funding stress plays no central role** — this is, formally, a pure market-liquidity
(not funding-liquidity) instance of Brunnermeier-Pedersen's loss-spiral leg (A.7) operating through
ETF authorized-participant arbitrage breaking down at the open, distinct in mechanism from a margin
spiral even though both legs of their model can, in principle, co-occur.

**3. February 5, 2018 — "Volmageddon": the canonical short-vol structure failure.** The CBOE VIX
rose from a **17.31 close the prior session to a 37.32 close** — a **115% single-day increase**,
the largest on record — while the underlying S&P 500 fell **4.1%**, its largest one-day move since
2011. The VelocityShares Daily Inverse VIX Short-Term ETN (XIV) collapsed from roughly **$1.9
billion in assets to $63 million in one session** (a **96% one-day loss**); Credit Suisse announced
XIV's termination the next day, with **February 15, 2018** as its final trading day; the ProShares
Short VIX Short-Term Futures ETF (SVXY) fell **91%**. The mechanism, per the post-mortem literature
(CFA Institute's summary of the "Volmageddon" academic record): these short-volatility exchange-
traded products' **own rebalancing rule** — buying VIX futures to stay short-delta-neutral as their
own AUM shrank intraday — created a self-reinforcing feedback loop structurally identical to 1987's
portfolio-insurance mechanic (a rule-driven amplifier, this time implemented purely through VIX
futures with no underlying credit extension anywhere in the chain), a genuinely new instance of
Geanakoplos's leverage-cycle margin logic (`credit-deep partA` §A.6) playing out entirely inside a
derivatives structure. **Order-of-arrival: the derivative (VIX) moved first and by the largest
multiple; realized (spot) volatility followed, and by comparison modestly** — the reverse of the
credit-transmission ordering A.7 formalizes, and the reason this case anchors the taxonomy's
"structural short-vol failure" archetype rather than either the funding-leads or vol-leads poles.

**4. March 2020 — the COVID global vol event.** The CBOE VIX closed at an all-time record **82.69
on March 16, 2020**, surpassing the previous record close of **80.74 set on November 21, 2008**.
The S&P 500 fell **33.9% from its February 19, 2020 peak (3,386.15) to its March 23, 2020 trough
(2,237.40)** in **23 trading days** — the fastest bear market on record. Funding stress followed the
equity/vol shock rather than preceding it: the Federal Reserve stood up the **Commercial Paper
Funding Facility on March 17, 2020** and the **Money Market Mutual Fund Liquidity Facility on March
18, 2020** — both inside the single week bracketing the VIX's record close — as part of a rapid
sequence of emergency facilities responding to a dash-for-cash that reached even normally-liquid
US Treasuries. **Order-of-arrival: realized/implied volatility moved first and hardest; drawdown
followed within days; funding stress (globally) followed within the same acute week, as an
exogenous-shock loss spiral (A.7, mechanism 2) ran without a prior domestic margin-spiral
buildup.** This is the taxonomy's clean global anchor for "vol → drawdown → funding-if-at-all,"
against which India's own March 2020 experience (§B.2.6) is directly comparable.

### B.2 Eight India cases (double length)

**1. January 21–22, 2008 — the two-day crash: the levered-retail margin spiral.** On **January 21,
2008** ("Manic Monday"), the Sensex plunged **1,408 points (a 7.4% fall)**, with the index shedding
as much as **2,273 points intraday** within the first minute of trading before the lower circuit
was breached; on **January 22**, the NSE reported trading halted after the Nifty itself breached
its 10% circuit level — the market's then-new circuit-breaker infrastructure activated on a major
global shock for one of its earliest live tests. The proximate trigger was the US subprime crisis's
global transmission, but the amplifying mechanism inside India was domestic and mechanical: heavily
levered retail and HNI positions built through 2007's bull run met margin calls as prices gapped
down, forcing further selling into an already-thin market — a textbook Geanakoplos-style margin
spiral (A.7) operating on retail leverage rather than institutional balance sheets, running purely
through domestic equity margin financing with essentially no funding-market (CP/repo) leg to the
story at this stage — the credit-cycle-linked funding freeze was still nine months away. By
year-end the index had fallen roughly 60% from its January peak. **Order-of-arrival: realized
volatility (the crash itself) leads; no India VIX-derived term-structure read exists this early in
its own archive (VIX historical data begins March 2, 2009, per Part C below — this episode predates
usable India VIX history entirely); funding stress is a retail-margin, not a wholesale-funding,
phenomenon and shows no independent lead.** This is squarely a **realized-vol-only** case at the
level of what our current data architecture can even observe, and — read alongside `02-fast-stress.
md` §3's own listing of this episode — the honest reason the module's construction cannot lean on
a VIX-derived confirm leg for anything before March 2009.

**2. September–November 2008 — the GFC core: FII outflows and call-rate stress.** Through **October
2008**, FIIs sold a net **₹14,249 crore** of Indian equities — the highest FII outflow share of
total BSE market capitalization recorded to that point — as the Lehman collapse (15 September 2008)
forced simultaneous, global de-leveraging; the Sensex fell from a January 2008 peak above **21,000
to roughly 8,000–8,500 by late October 2008**, a peak-to-trough decline on the order of **60%**.
India VIX (whose historical archive begins **March 2, 2009**, right at this episode's edge) reached
an **all-time-high reading of 92.5 in November 2008**, the highest print in its entire history,
confirming the acute-stress read from the archive's earliest available window. The rupee
depreciated sharply as outflows intensified, and money-market conditions tightened alongside the
global dollar-funding freeze `research/cycles/globalcycle-deep/partB-cases.md`'s own GFC case
already documents at the level of the global financial cycle (Atlas row 2.8), read here through
L2's equity-and-vol lens rather than L9's flow lens. **Order-of-arrival: realized volatility and the
nascent, edge-of-archive VIX read move together at the acute peak; the funding leg (global
dollar-funding stress plus domestic FII-driven rupee/liquidity tightening) is contemporaneous with,
rather than clearly leading, the equity stress** — the transmission of an exogenous shock rather
than an endogenous India credit-cycle bust, even though its magnitude in India was severe.

**3. May–August 2013 — the taper tantrum: funding and currency stress, INR to 68.** Following
Fed Chairman Bernanke's **22 May 2013** congressional testimony raising the prospect of QE
tapering, the rupee depreciated roughly **28% between April and August 2013**, from about ₹54 to a
then-lifetime low of **₹68.85 on 28 August 2013**; the Nifty fell from an intraday high near
**5,808.50 (1 August 2013)** to an intraday low of **5,118.85 (28 August 2013)** — a peak-to-trough
decline of roughly **15–18%**, already independently confirmed in this program's own verification
log and `credit-deep partB` §B1's cross-country record. This is the canonical **funding/currency
transmission** case: the shock originated entirely outside India (a US monetary-policy-expectations
repricing), and its India transmission ran through the **capital account** — FII outflows, rupee
depreciation, pressure on India's then-large current-account deficit (the "Fragile Five," Morgan
Stanley's James Lord, already documented in `globalcycle-deep partA` §A.3iii) — rather than through
a pre-existing domestic funding freeze. RBI's own defense (the 15 July 2013 MSF corridor hike to an
effective 10.25%, Governor Rajan's 4 September 2013 FCNR(B) swap window raising roughly **$34
billion**) is `docs/cycles/20-mp-cycle.md`'s own documented case, cross-referenced not re-derived
here. **Order-of-arrival: currency/funding stress and equity realized volatility move essentially
together over the acute window, both downstream of a single external trigger** — a "quiet-triad-
turns-loud" episode in L9's own vocabulary (`globalcycle-deep partB` §B1.4), and the direct
historical analogue the May-2026 episode (case 8) explicitly replays.

**4. February 2018 — global Volmageddon and the LTCG Budget, disentangled.** Two shocks landed in
India inside the same eight-day window, and disentangling them is itself the design lesson. On
**1 February 2018**, Finance Minister Arun Jaitley's Union Budget reintroduced long-term capital
gains tax on equities (10% above ₹1 lakh, no indexation); the Sensex fell as much as **463 points
intraday** in a knee-jerk reaction, recovering most of the loss to close down just **58 points**,
before selling pressure intensified the next session (**2 February**: Sensex −572.72 points/−1.60%,
Nifty −168.25 points/−1.53%) — a **domestic, policy-driven, fully anticipated-timing** shock (Atlas
row 4.1, "Union Budget window... timing fixed by law, direction unknowable"). Four days later, on
**5 February 2018**, the global "Volmageddon" event (§B.1.3 above) landed — a shock with **zero
India-specific origin**, transmitted into Indian markets purely through the global vol-derivative
channel. The two shocks are mechanistically unrelated (one a domestic fiscal-policy surprise inside
a pre-scheduled calendar window per Atlas 4.1; the other a global short-vol structural failure), and
conflating them — reading the whole week's Nifty weakness as "the market didn't like the Budget," or
alternatively as "Volmageddon hit India hard" — would misattribute either shock's own magnitude.
**Order-of-arrival, kept separate per leg and per shock:** the Budget shock shows realized volatility
moving first (the announcement itself is the information event; no funding or VIX-term-structure
leg is implicated) on a fully anticipated calendar date; the Volmageddon shock, four sessions later,
shows the VIX/derivatives leg moving first and by the largest multiple (per §B.1.3's own global
ordering), with India's own realized equity vol responding as a smaller, transmitted echo rather
than an independent domestic event — precisely the discipline Atlas row 3.7/4.1 already builds into
L5 ("mandate-clarity re-lever rule," "direction is surprise... timing scheduling only, never a
directional bet"): a calendar-scheduled vol-widening window (the Budget) must never be conflated,
in the episode record, with an unrelated global shock that happens to land inside the same
fortnight.

**5. September–October 2018 (IL&FS) plus the June 2019 DHFL aftershock — the funding-leads-equity
case.** Infrastructure Leasing & Financial Services first showed strain in **June 2018** (a delayed
₹450 crore inter-corporate-deposit repayment to SIDBI), defaulted on a few hundred crore of
commercial paper in **late August 2018** (repaid two days later), then defaulted on a **₹1,000
crore term loan** and failed to meet CP redemption obligations due **14 September 2018** — the
acceleration point, after which IL&FS Financial Services was barred from the CP market until March
2019. Total IL&FS-group defaults reached **₹46.4 billion** by November 2018. The Sensex moved
comparatively modestly by this record's standards — dossier D04's verified figure puts the
**Nifty 50** drawdown at roughly **−15%** (August→October 2018) while the **Midcap** index fell
**19–30%** and the **Smallcap** index fell as much as **~32%**, roughly double the headline index —
the funding freeze transmitted into equities through the **credit-supply** channel to NBFC-dependent
borrowers well before it showed up as a headline-level shock, the mechanism A.7 formalizes and this
program's own **SC1** trial (2026-09-02) measures on real India factor data (small-cap at the 18th
percentile of its own rolling-window history in the crunch window, market at the 16th — both
stressed, the funding-adjacent leg marginally more so). The aftershock arrived roughly nine months
later: **Dewan Housing Finance Corporation (DHFL)** defaulted on **₹1,000 crore of bonds** in
**early June 2019**, with **CRISIL and ICRA downgrading its commercial paper to 'default' (D)** the
same week — direct confirmation the funding freeze IL&FS triggered had not resolved within the
shadow-banking sector nine months on, and that CP-market stress continued to lead further
NBFC-sector deterioration rather than merely echoing it. **Order-of-arrival: funding stress (CP
defaults, the CP-market ban) leads by weeks to months; the mid/small-cap drawdown follows, larger
than the headline index; the broad Nifty 50 "confirmation" is smallest and last-arriving** — the
cleanest India instance of the credit-transmission ordering A.7 formalizes, and the case
`partDH-upgrade.md`'s FS-D2 design names as its own pre-stated shape check.

**6. March 2020 — the COVID crash: −13.2% single day, India VIX in the 80s, the circuit-breaker
session.** On **23 March 2020**, the Sensex fell **3,935 points (13%)** to close at 25,981 and the
Nifty fell **1,135 points (13%)**; a **10% decline triggered a market-wide circuit breaker at
9:58am**, halting trading for **45 minutes** — the second such coordinated halt inside ten days.
India VIX **rose to 71.56** that session `[D04's own independently-verified figure cites an
intraday extreme nearer 80–87 the same date; both are retained together rather than reconciled,
consistent with D04's own treatment]`, and over the full February–March episode the Nifty fell
**~38.4% peak-to-trough over 69 trading days** (D04's verified figure), recovering over the
following 231 days. Of 2,401 BSE-traded stocks that session, **2,036 declined against only 233
advances**. Unlike IL&FS, no domestic credit-cycle precondition drove this episode: the trigger (a
global pandemic and the resulting lockdowns) arrived entirely exogenously, and equity
realized/implied volatility moved first and hardest, mirroring the global case (§B.1.4). Funding
stress in India followed within the same acute window rather than leading it — RBI's own
interventions (LAF operations, TLTRO) arrived alongside, not ahead of, the equity collapse —
consistent with the exogenous-shock ordering A.7 formalizes and `partDH-upgrade.md` Part D states
as its own pre-registered shape check for this exact episode. **Order-of-arrival: realized
volatility and India VIX move together and first; drawdown is the largest and most persistent leg;
funding stress is contemporaneous, not leading.**

**7. June 4, 2024 — election day: fast vol without funding stress, the taxonomy's clean contrast.**
Exit polls released **1 June 2024** had pointed to a comfortable National Democratic Alliance
majority, and the Sensex crossed **76,700** with the Nifty above **23,300** — both record highs —
on **3 June 2024**, the session before results. When counting on **4 June 2024** showed the BJP
would require coalition support rather than the outright majority markets had priced, the Sensex
fell nearly **4,390 points (5.7%)** and the Nifty declined more than **1,379 points (5.9%)** by the
close, with an **intraday fall exceeding 6,200 Sensex points** and the Nifty touching an intraday
low of **21,281**, briefly breaking below the 22,000 level — one of the largest single-day falls in
Indian market history, concentrated in the railway, defence, PSU, infrastructure and power stocks
that had rallied hardest on the pre-result NDA-majority expectation. This is a pure **domestic
political-surprise** shock (Atlas row 3.7's own "direction is surprise" verdict, independently
re-confirmed on real India factor data by the trial ledger's **PL1** entry — pre-window sign
predicted the result-month sign in only 3 of 8 general elections, at or below coin-flip) with **no
funding-market precondition and no funding-market transmission at all**: no CP spread widened, no
NBFC rollover failed, no credit-supply channel was implicated anywhere in the mechanism — the shock
was a pure, one-day repricing of political-majority expectations, over within the session, with the
market recovering materially within the following two trading days. **Order-of-arrival: realized
volatility is the entire story; no funding leg exists to order against it at all.** This is
precisely the clean contrast case the taxonomy needs: proof that "fast vol" and "funding stress"
are genuinely separable phenomena, not two names for one thing, and the closest India-domestic
analogue to 1987's own vol-without-funding archetype (§B.1.1).

**8. May 2026 — the INR/FII episode, as already documented and verified in this program's own
record.** Per `docs/cycles/02-fast-stress.md` §3 (a "stress episode for L2 even though non-
qualifying for the DD test per the 2026-08 verification") and the fuller reconstruction already
verified in `research/cycles/globalcycle-deep/partB-cases.md` §B9 and `research/register/
verification-log.md` §4 (Bloomberg, "Rupee Plunge Sees India Turn to 2013 Taper Tantrum Playbook:
INR/USD," 22 May 2026), USD/INR swung from a low of **89.86 in early January 2026** to an intraday
record high of **96.84 on 20 May 2026** (an acute window of roughly **₹96.6–96.8/$ between 19–21
May 2026**), before a partial recovery to roughly **94.35** by late H1 2026. Three forces
compounded: sustained **FPI equity outflows** (**₹32,963 crore in May 2026 alone**, part of a
cumulative **₹2.25 lakh crore CY2026 outflow** already exceeding all of CY2025's ₹1.66 lakh crore);
a **Brent crude spike from $70/bbl to $95–105/bbl** on Strait of Hormuz disruption; and a lingering
US-India tariff overhang. RBI (Governor Sanjay Malhotra) was reported weighing an FCNR(B)-style
emergency NRI-deposit scheme, echoing the 2013 playbook (case 3 above). **What makes this episode
instructive precisely by being unusual:** the equity impact was comparatively mild — Nifty 50 shed
roughly **4% over four acute sessions** and closed the month down only **≈1.87%** (Sensex ≈−2.78%)
— and **India VIX rose only to ≈18.6**, nowhere near a fast-crisis print (contrast case 6's 71+
reading). **Order-of-arrival: the currency/FII-flow leg** (this seat's funding-adjacent confirm
input, per `02-fast-stress.md` §4 — "NSDL FPI outflow rank... may pull the state DOWN as well as
up") **moved first and carried nearly the entire episode's signature; realized equity volatility
and India VIX stayed comparatively quiet throughout.** This is the mirror image of case 5 (IL&FS):
a genuine funding/flow-side stress episode that never propagated into an equity-vol event at all —
a properly-constructed funding/flow confirm leg would register this episode as elevated even while
RV alone would have missed it almost entirely, the cleanest case in this record for why L2 reads
all three legs jointly rather than treating realized vol as a sufficient statistic for stress.

### B.3 What the twelve cases say, read against the taxonomy

Ordering the twelve cases by which leg moved first reproduces `partDH-upgrade.md`'s own two-bucket
taxonomy cleanly, with one genuinely new nuance the India record adds. **Funding-leads cases**
(IL&FS/DHFL, case 5) show the CP/rollover leg moving weeks to months ahead of the equity
confirmation, the mid/small-cap tail bearing roughly double the headline index's damage — a
credit-transmission signature. **Vol-leads, funding-absent-or-lagging cases** (1987, COVID globally
and in India, June 2024 election day) show realized/implied volatility moving first and largest,
funding stress either entirely absent (1987, June 2024) or a same-window echo (COVID). **The
genuinely new nuance** sits in cases 3 and 8 (2013 taper, May 2026): both are **currency/flow-
leading, vol-lagging** episodes — a third pattern the two-bucket taxonomy's "funding-if-at-all"
catch-all does not yet name separately, in which the external funding-adjacent leg (FII flows, the
rupee) carries an episode's entire signature while domestic equity realized vol stays
comparatively contained — the honest implication being that L2's funding-adjacent confirm input
and L9's global-cycle seat are reading closely related, in these two cases nearly overlapping,
objects, a genuine design question for FS-D2's own grading rather than one this chapter resolves.
February 2018 (case 4) stands as the record's own worked lesson in *not* conflating two independent
shocks landing in one calendar window — a discipline Atlas rows 3.7/4.1 already build into L5.

---

## PART C — India data engineering

### C.1 India VIX: the daily archive and its 2008–09 launch history

NSE launched **India VIX in April 2008**, using computation methodology licensed from CBOE
(itself trademark-authorized by the Chicago Board Options Exchange and Standard & Poor's), adapted
for the NIFTY option order book via natural cubic-spline interpolation across best bid-ask quotes
(A.5's formula). **Historical India VIX data is available free from NSE's own archive starting
2 March 2009** — a roughly eleven-month gap between the index's actual launch and the start of its
publicly downloadable historical series, which is the operative constraint for any backtest: **case
1 in Part B (January 2008) and the bulk of case 2 (the September–October 2008 acute window) predate
usable India VIX history entirely**, and only the *tail end* of case 2 (India VIX's own all-time-
high reading of 92.5 in November 2008) sits inside the archive's earliest window. This is not a
data-engineering inconvenience to work around quietly — it is a hard, honest boundary: **any
India-VIX-conditioned rule (F5, FS-D1) has a real, usable history beginning only in March 2009**,
roughly seventeen years before this writing, materially shorter than the bhavcopy-based realized-vol
series (available since the 1990s) that L2's primary RV input already draws on, and the reason
`02-fast-stress.md` §2's own India-application note treats the VIX record as "one full crisis (2020)
plus a dozen smaller spikes" rather than a longer, deeper sample. Free source: `nseindia.com`'s
historical-VIX report page (`nseindia.com/reports-indices-historical-vix`), daily close, downloadable
in bulk.

### C.2 VIX futures, the option-chain IV-RV surface, and what must be self-archived

**VIX futures — documented honestly, not oversold.** NSE listed India VIX futures on **26 February
2014**, three weekly contracts expiring every Tuesday alongside standard F&O hours. Liquidity never
developed at scale, and NSE **discontinued India VIX futures in 2017** for low participation. Any
FS-D1 construction wanting a genuine, market-priced *term-structure* read (near vs. far implied
variance, rather than a single 30-day constant-maturity level) therefore has **no continuously-
available, exchange-traded term instrument** for most of the sample — the honest fallback, as
`partDH-upgrade.md`'s own FS-D1 registration states, is to reconstruct the slope directly from the
**Nifty option chain**: near- and next-month implied variances are already computed separately
inside the India VIX methodology (A.5's formula) before being time-weighted to constant maturity —
the raw material exists inside NSE's own computation, but the **two component variances are not
separately published** as a standard daily series; extracting them requires either NSE's own
occasional working-paper disclosures of intermediate values `[VERIFY: whether published routinely
or only in methodology illustrations]`, or reconstructing both legs from raw option-chain snapshots
(strike-level best bid-ask, live and free every session but **not archived historically by NSE in
bulk** — a genuine free-vs-self-archive boundary): a multi-year historical option-chain series
usable for a backtest does not exist as a ready-made download and must be built prospectively,
snapshot by snapshot, exactly the forward-only constraint `CONTRACT.md` §7 Known Prior #11 already
states for this program's network limits. **A separate, prospective 2026 development** (Business
Standard, 20 July 2026, "NSE plans new volatility index with revised methodology; pilot launch
soon") reports NSE piloting a **new, differently-methodologized volatility index** — explicitly
**not** a replacement for India VIX, still in pilot testing, requiring fresh SEBI approval for any
derivatives — flagged as **not yet a usable data source** `[VERIFY: pilot status as of any later
read]`.

### C.3 Funding data: CCIL, TREPS/repo/call rates, CP issuance rates, NSDL FPI flows

This program's own `shadow-deep` chapter (`research/cycles/shadow-deep/partC-data.md` §C.1–C.3,
cited here rather than rebuilt, per the desk's standing rule against duplicating a seat's own
evidence base across monographs) already engineers the core funding-freeze surface L2's confirm
leg draws on: **CP outstanding and issuance** from RBI's Weekly Statistical Supplement and Bulletin
"Money Market" tables (weekly, ~1-week lag); **CP/CD primary rates by rating and tenor** from the
RBI Bulletin (monthly) and FBIL money-market benchmarks (daily, `[VERIFY: exact free-access history
depth of the FBIL CP curve]`); **CP/CD secondary trades** from CCIL's F-TRAC public dissemination
(daily, T+0, likely proxy-blocked from this remote environment per `CONTRACT.md` §7 Known Prior #11
— a runsheet item for the principal's own machine); and the **91-day T-bill** rate (weekly, RBI
WSS/auction results) as the spread's risk-free leg. The freeze-index construction that Part
`shadow-deep`'s own SC2 design registers — `z(CP spread, 3m tenor, top-rated) + z(−rollover ratio)`,
both legs on expanding-percentile windows — is the direct, ready-to-wire input for L2's funding-flow
confirm leg once vaulted; nothing about that construction needs restating here beyond noting the
integration point explicitly: **L2's `role` field in `config/ladder.yaml` already names "CCIL,
NSDL FPI" as `indicator` sources for exactly this leg**, so the shadow-credit chapter's freeze index
and L2's own confirm input are, by design, the same object viewed from two chapters. **CCIL's own
TREPS (Tri-Party Repo) and call-money rate data** (daily, via CCIL's own published market summaries)
supply the *system-liquidity* leg distinct from the CP-market *credit-spread* leg — a widening
TREPS-vs-repo-corridor spread or a call-rate spike above the repo corridor's ceiling is the
classical, decades-old signature of an acute overnight funding squeeze, complementary to but
mechanically distinct from the CP market's own term-funding stress (the two can, and historically
do, decouple — an overnight squeeze on a statutory drain date, C.4 below, is exactly the mechanical,
non-informative case the H58 quarantine exists to catch). **NSDL's daily FPI/FII net-flow figure**
(published every evening, free, the same series `fpi-deep partA` §A.2 already documents as "the
single most repeated data point in Indian financial media") is the flow leg — already, per
`02-fast-stress.md` §4's own construction, licensed to "pull the state DOWN as well as up" since all
L2 inputs are Tier B with no clamp, in contrast to the credit composite's Tier-C clamped
composition input.

### C.4 The H58 drain-date quarantine — already wired into L2's role

`quant/ladder/exclusion_calendar.py` implements the mechanical calendar this program's own H58
pre-registration (`docs/CYCLE_ATLAS.md` §8, row H58) requires, and it is already load-bearing in
L2's own registry entry: `config/ladder.yaml`'s `L2_fast_stress` block states its `role` text
explicitly — "funding-leg fires inside statutory drain windows (advance-tax s.211 dates, GST due
20th) are quarantined as mechanical per H58." The mechanism, read against A.7's own margin-spiral
formalization, is precisely why this quarantine belongs to the *funding* leg specifically and not
to realized vol or VIX: advance-tax instalment dates (Income-tax Act s.211: 15 June, 15 September,
15 December, 15 March) and the monthly GST due date (the 20th) drain system liquidity by **statute**,
producing a mechanical, calendar-certain call-rate or TREPS-spread spike that has **nothing to do
with any margin spiral, loss spiral, or genuine funding-market impairment** — it is a scheduled
plumbing event, not a signal. `exclusion_calendar.py`'s `drain_window_mask()` function computes,
for any date series, whether each date sits inside a business-day window (default ±2 business days
before, +1 after) around any statutory drain date in the relevant years, using `numpy.busday_offset`
against an optionally-supplied holiday list; the consuming rule (L2's funding-leg trigger) treats a
drain-window fire as **flagged mechanical, requiring the OTHER confirm legs to independently agree**
— the mask can only *suppress* a trigger, per the module's own docstring ("reduce-only in spirit:
the mask can only SUPPRESS a trigger, never create one"), never manufacture one. Grading this
quarantine's own value is `partDH-upgrade.md`'s (and the trial ledger's) own **H58-D1** design,
data-gated on L2's real daily trigger history: "count funding-stress fires landing inside statutory
drain windows... vs outside; the exclusion earns its keep if drain-window fires are ≥2x the base
rate AND ≥80% of them mean-revert within 5bd (mechanical, not stress)" — registered, not yet run,
exactly the two-pass discipline this program applies everywhere a bar is set before data lands.

### C.5 Construction pitfalls

**VIX methodology revision history.** Searched this session for any documented methodology
revision to India VIX's own calculation between its 2008 launch and the present: none was located
beyond the 2026 pilot of a **separate, new** index (C.2 above, explicitly not a revision to India
VIX itself). The honest statement is therefore that **India VIX's own construction (CBOE-licensed,
cubic-spline, near/next-month time-weighted to 30 days) appears to have run without a documented
methodology break across its full 2008/2009–2026 history** `[VERIFY: this is a search-based
absence-of-evidence finding, not a confirmed absence-of-revision finding — a builder should re-check
NSE's own methodology-document version history directly before relying on splice-free continuity for
any long-window statistical test]`. This matters because it is the *opposite* failure mode from the
credit-cycle monograph's own AQR/GNPA lesson (`credit-deep partB` §B2.10, "a measurement break, not
a new credit event") — where that seat must actively guard against reading a reporting-methodology
jump as a fresh shock, this seat's own honest finding is that no comparable splice risk appears to
exist in the VIX series itself, a genuinely different, and better, data-quality position than L10's.

**Expiry-week IV artifacts.** As a near-month option contract approaches its own expiry, its
time-to-maturity `T` shrinks toward zero, and the model-free variance formula's own `(2/T)` scaling
term (A.5) becomes numerically unstable for any small pricing noise in the remaining quotes —
compounded by naturally thinning liquidity and widening bid-ask spreads in a contract's final
sessions, which is exactly where the cubic-spline interpolation (filling strikes with no clean
quote) is asked to do the most work with the least reliable input. The standard, well-documented
practitioner response (echoed in NSE's own switch to the next-month contract as the "near" leg once
the current near-month sits inside a specified number of days to expiry) is to **roll the near-month
leg forward before expiry week** rather than let the constant-maturity blend lean on a near-expired
contract's degraded quotes — a construction detail any FS-D1 term-structure read built directly from
raw option-chain data (rather than from NSE's own already-blended India VIX print) must replicate
explicitly, or inherit spurious expiry-week noise that has nothing to do with genuine stress.

**The 2020 circuit-halt sessions: a truncation bias in range-based RV estimators, direction stated.**
A.2's Parkinson/Garman-Klass range estimators assume the observed daily high-low span reflects the
*true* intraday range of a continuously-traded process. A coordinated market-wide circuit halt
(case 6, §B.2: the 23 March 2020 45-minute halt, one of two inside ten days) **mechanically
truncates that observed range**: trading is suspended before the session's true extreme is
necessarily reached, and because the halt triggers on a 10% *decline* specifically, the truncation
is **asymmetric**, curtailing exactly the downside tail a range estimator exists to measure. **The
resulting bias is unambiguous: a range-based RV estimator computed naively on a halt-session's
reported high-low will systematically UNDERSTATE that session's true realized variance**, precisely
where true variance is highest — the opposite of what intuition (a halt session "should" read as
maximally stressed) predicts. The **close-to-close estimator does not share this bias**: the
session still closes at an actual traded price (the halt pauses trading, it does not cancel the
session), so the close-to-close return still captures the full realized move from the prior close,
even though the closing price itself may still understate the session's true, unobserved intraday
extreme. **The construction consequence**: any range-estimator upgrade to `fast_stress.py`'s current
close-to-close `realized_vol()` (per A.2) must flag circuit-halt sessions explicitly and either
fall back to close-to-close on those sessions or apply a documented, pre-registered correction,
rather than silently averaging a downward-biased range observation into a rolling window exactly
when the window most needs an accurate read.

**Holiday alignment across CCIL/NSE calendars.** NSE's equity-trading holiday calendar and CCIL's
money-market (RBI-linked) holiday calendar are **not identical** — certain days are RBI/CCIL
holidays (some state-specific banking holidays, RBI-designated settlement holidays) on which NSE
equity trading proceeds normally, and vice versa for a small number of exchange-specific closures.
A construction that assumes a single shared calendar across the RV leg (NSE bhavcopy), the funding
leg (CCIL/RBI money-market data), and the VIX leg (NSE options) will silently misalign dates on
exactly the sessions where the misalignment is most likely to matter — a statutory-drain-adjacent
date, or a settlement holiday sitting beside a genuine market-stress session. `exclusion_calendar.
py`'s own design already anticipates this precisely: every window-mask function accepts an explicit,
**separately-supplied** `holidays` parameter per calendar rather than assuming NSE's own trading-day
index doubles as the money-market calendar — the correct discipline, per that module's own docstring
("exchange holiday lists are a supplied refinement, not assumed"), is to source and maintain **two
distinct holiday lists** (NSE's own trading-holiday calendar and CCIL/RBI's settlement-holiday
calendar) and join the RV, VIX, and funding series on their respective native calendars before any
composite computation, rather than forcing all three onto one assumed-shared trading-day index — a
one-line-sounding requirement whose violation would quietly misdate exactly the funding-leg
observations the H58 quarantine (C.4) and the FS-D2 order-of-arrival grading (A.7) both depend on
being dated correctly.


---

# Parts D–H (upgrade addendum) — fast stress at full standard (atlas 5.1/5.2/5.3 → L2)

The v1.0 entry's designs F1–F7 and its measured synthetic bounds STAND UNCHANGED (that
document's §4–§5 remain the operative pre-registrations). This addendum records what the
upgrade adds and how atlas 5.2/5.3 formally fold into the seat they always fed.

## Part D — What the upgrade adds to the evidence

**FS-U1/FS-U2 (our first real-data prints for this seat).** Monthly |return| autocorrelation
0.141–0.188 (India MF, LB(6) p=4e-11) and 0.170–0.245 (gold float era, p=3e-33). Two uses,
both honest: the Tier-A fact now has a print computed from OUR vault (library integrity),
and the magnitudes quantify the aggregation loss — monthly clustering at ~0.15–0.25 versus
the ~0.2–0.4 lag-1 range typical of daily |returns| in the literature. The fast layer's
daily-resolution design requirement is thereby MEASURED, not asserted: the resolution
theorem (CW1/CR2) applied in reverse — the phenomenon survives aggregation but its
usable sharpness does not.

**The order-of-arrival taxonomy (pre-registered as a classification, never fitted).** The
three legs see impairment in a stated order that differs by shock type: credit-transmission
crises run funding → vol → drawdown (2018: CP spreads widened weeks before index vol);
exogenous shocks run vol → drawdown → funding-if-at-all (2020, 2024-election). The
taxonomy's use is diagnostic (which playbook page), NOT predictive weighting; any
leg-weighting change must come from F2/F5's grids, and the classification is falsifiable
episode-by-episode as daily data lands (FS-D2).

## Part E — Seat status

Module seated and tested since v1.0 (planted-truth suite incl. the honest 92/98 detection
bound and no-look-ahead truncation). Upgrade-era wiring: the H58 statutory-drain quarantine
now lives in ladder.yaml L2's role text (funding-leg fires inside drain windows are flagged
mechanical, two-of-three confirmation overrides — exclusion_calendar.py, tested). Phase
overlay unchanged: U arms cuts, D is display-only until F7 passes.

## Part F — Designs (additions only; F1–F7 unchanged)

- **FS-D1 (VIX term-structure state, atlas 5.2):** distinct from F5 (which tests IV LEVEL
  redundancy). Object: backwardation flag — near/far implied-variance ratio > 1 (near-month
  India VIX vs 2-3 month, from NSE VIX futures history where listed, else the option-chain
  IV term slope). Bar at registration when the archive is vaulted: episode AUROC of the
  backwardation flag must ADD over the RV-rank leg alone on the §3 episode set (incremental,
  purged); a redundant flag is documented and excluded like any other.
- **FS-D2 (order-of-arrival, atlas 5.3):** on the vaulted daily set (CCIL spreads, India
  VIX, index RV): for each §3 episode, date each leg's first top-decile print; the 2018
  funding-led and 2020 vol-led orderings are the pre-stated shape checks; a taxonomy that
  fails them dies as a classification (the legs stay, unordered).
Both data-gated; runsheet pulls (India VIX archive, CCIL dailies, VIX-futures history).

## Part H — Knowledge ledger (upgrade)

**Established (our prints):** monthly-resolution clustering on the vault (FS-U1/U2), with
the aggregation loss quantified. **Established (synthetic, v1.0):** the module's detection
bound (92/98 at 0.3, median lag 1d) and its falsified-then-corrected 100%-claim history.
**Pooled-prior (Tier A/B):** clustering + leverage effect (A); vol-targeting DD control
(60y multi-asset); the CONTESTED alpha claim (Moreira-Muir vs Cederburg — prior unchanged:
DD control robust, alpha unproven); backwardation-as-stress (Whaley lineage, B);
funding-leads-vol in credit-transmission crises (Brunnermeier-Pedersen + the 2018 India
record, B). **Awaits India data:** F1–F7 in full, FS-D1/FS-D2. **Unknowable:** the next
spike's date — the seat reacts in days; it never predicts, and the monograph's every claim
is resolution-stamped.


---

## Post-assembly addendum (2026-09-02, same day): three of this monograph's designs printed

Run on the vaulted NIFTY daily mirror the same day this upgrade was assembled (full prints:
research/cycles/daily-batch/daily-RESULTS.md; ledger entries F2-index, F7a, FS-D3):
- **F2 (bounded index run):** 3/18 grid cells supportive, all at trigger 0.80 + 1-of-2
  confirm; the "any one arms" asymmetry measured; shortlist {calendar, decay} re-entry.
- **F7 (first real print, F7a):** FAIL (63bd forward returns U vs D at matched high state,
  p=0.653) — per this document's own frozen rule, **phase is display-only for L2**; the
  phaseD grid dominance was re-attributed to re-entry earliness (doctrine: levels, not
  directions). F2c (direction-free calendar-21bd) registered.
- **FS-D3 (interim global-VIX confirm leg):** REFUSED — symmetric averaging diluted domestic
  detection (lost the 2024 episode) while accelerating global-origin crises (2011 lag
  91→13bd); FS-D4 (arm-only) registered, deferred to full F2.
None of these bounded prints arms the R4 mapping; the full F2 (three legs, book costs, M4
walk-forward) remains the registered adjudicator.

**Same-day update (F1b, F2-WF — the M4 harness's first runs):** the corrected tau_half is
3.18 months, CI [2.39, 5.72] (config stands under drift hysteresis; lengthening watch set);
and the walk-forward DISQUALIFIED both adoptable shortlist cells (drag within budget in only
2 of 4 eras each — the full-period drags were flattered by the quiet 2009-2018 decade; the
COVID-era payout, DD 37%→26%, against 2.5-4pp/yr premiums in whipsaw-rich eras, is the
insurance economics the full F2 must price at book level). The index-level shortlist is
EMPTY; nothing is armed.

---

**Dated addendum (2026-09-03) — F5a: the domestic implied leg refused, like the global one.**
The India VIX mirror (ingest/vault/vix/, 6/6 anchors, 2010-2023) let F5's daily-close partial
run as registered (F5a, ledger 2026-09-03). Neither bar fired: Spearman rank correlation of
the IV and RV expanding percentiles is 0.763 (below the 0.80 redundancy bar), and the IV
percentile is a slightly WORSE episode classifier than the RV percentile (AUROC 0.770 vs
0.786, 2,866 joint days, 8 frozen episodes) — so the parent's fallback governs: **RV stays
primary; the composite buys no confirmation from implied vol.** Taken with FS-D3's refusal of
the CBOE leg, both implied-vol candidates (global and domestic) have now failed to add over
realized vol at index resolution — implied indexes are rank-echoes of RV for episode
detection. The VRP proxy printed positive on 85.4% of days (mean +0.0076 annualized
variance): the premium exists, is documented, and remains unconsumed pending its own
registration (the parent's own rule). The FULL F5 (NSE primary series + M4 adjudication)
stays owed; FS-D1 (term structure) still needs option chains.

---

**Dated addendum (2026-09-03, late) — F3a: the vol-managed lure, priced on the index.**
F3's partial ran on the index vault as registered, and every clause of the design's prior
got a number. Full-period Moreira-Muir (uncapped): alpha +5.76%/yr at t=1.67 — the classic
seduction, positive but unproven — with maxDD 26% vs 55% (DD control robust, as stated).
Cederburg's real-time protocol then does what it did in the US: the out-of-sample Sharpe
improvement vanishes (0.60 vs 0.62; the return difference's CI spans zero) — full-period
evidence flattered by hindsight-calibrated scaling, exactly why the parent forbade promotion
from it. The desk-feasible cell (capped at 1, net of costs) surprised the registered prior:
maxDD 22%, BETTER than the F2-index fast-trigger survivors — but at −4.86%/yr net drag,
roughly double their whipsaw-era premium, because continuous de-risking holds 0.73 average
exposure through every rally. The doctrine line sharpens: **speed is the seatbelt, and
continuity is a more expensive seatbelt** — episode-triggered rules buy most of the
protection at half the premium; the full F2/F3 adjudicates that trade at book level under
M4. Nothing arms; the desk's no-leverage constraint also removes MM's entire levered side.

**Same-day addendum (2026-09-03) — F4a: the third echo refused.** The correlation-spike leg
ran as a survivor-panel partial (one-way reading declared at registration): mean pairwise
correlation of the real-time-safe top-50 is NOT rank-redundant with realized vol (Spearman
0.765/0.649 at 21/63d) yet classifies the frozen episodes WORSE than RV at both windows
(AUROC 0.716 and 0.663 vs RV's ~0.75) — excluded as a confirm input per F4's own rule, and
decisively-leaning even under survivorship flattery. The tally: cross-sectional correlation
(F4a), domestic implied vol (F5a), and global implied vol (FS-D3) have each been offered as
confirmation for the fast-stress composite and each measured as an echo or worse. The RV
spine stands three-for-three; the full F4 on PIT data remains registered but the burden has
visibly shifted.

**Same-day addendum (2026-09-03) — F6a: the premium decomposed.** The false-fire ledger ran
on the F2-index grid verbatim and settled where the insurance premium actually lives:
transaction whipsaw across all 18 cells costs 0.02-0.28%/yr at index-futures rates — a
rounding error — so the 2.5-4pp/yr drags the walk-forward measured are almost entirely
EXPOSURE drag, the price of standing de-risked while the market rises. False-fire discipline
behaves exactly as designed (58%→0% share as trigger and confirm tighten; the phaseD
re-entry family re-fires pathologically and remains excluded), and the speed trade-off's far
end could not be convicted: with GFC warm-up-untestable, the single testable deep episode
(COVID) was caught even by the slowest cell — n=1, recorded, not concluded. Decision B3-1
sharpens accordingly: the budget being set is an exposure-drag budget; transaction cost
needs no line at this scale.
