# Part D — The mathematics and econometrics, from zero to working code

Everything in this part is implemented in `quant/stats/` and validated on synthetic ground truth
(`research/montecarlo/RESULTS.md`) before it is allowed near real data. Each section: the problem,
the math with every symbol defined, why the naive alternative fails, and where it lives in code.

## D1. Detrending: why the HP filter is banned, with the actual math

**The problem.** To say "credit is above trend" we must estimate the trend of the credit/GDP
ratio. Call the series y_t. The industry default — used by the BIS for the official Basel
credit gap — is the Hodrick–Prescott (HP) filter, which chooses a trend τ_t minimizing

    Σ (y_t − τ_t)²  +  λ · Σ [(τ_{t+1} − τ_t) − (τ_t − τ_{t−1})]²

λ is a smoothness penalty (BIS uses λ = 400,000 on quarterly data — a one-sided variant). The
first sum rewards fitting the data; the second punishes the trend for bending.

**Hamilton's 2018 demolition, in three points:**
1. **Spurious cycles.** The HP filter is a two-sided moving average in disguise. Slutzky (1927)
   showed moving averages of pure noise LOOK cyclical (Lesson 1, Fig 0.1). Hamilton proves the HP
   "cycle" has dynamics largely manufactured by the filter itself — you can feed it a random walk
   (which has no cycle by construction) and get a beautiful, publishable "cycle" out.
2. **End-point problem.** In the interior of the sample, τ_t is estimated using data on BOTH
   sides. At the end of the sample — the only point where money is at stake — half the window is
   missing, the filtered value is the least reliable, and it gets REVISED as new data arrives.
   Your backtest then contains a history that never existed in real time.
3. **λ is a magic number.** 1,600 for business cycles, 400,000 for credit — chosen by convention,
   not estimated, and the "cycle" you find is a function of the λ you chose.

**Hamilton's replacement** is an OLS regression (Part 2.1 of Lesson 1 teaches OLS from zero).
Regress the future value on a constant and the p most recent values known h periods earlier:

    y_{t}  =  α + β₁·y_{t−h} + β₂·y_{t−h−1} + ... + β_p·y_{t−h−p+1} + gap_t

The residual gap_t IS the cyclical component: "how far is y from where its own history, h periods
ago, would have projected it?" No λ, no two-sided window, and the parameters (h, p) have economic
meaning: h is the horizon over which departures count as "cycle" (we pre-register h ∈ {16–24}
quarters for credit; Hamilton's own choice for cyclical analysis of quarterly data is h=8, p=4 —
credit cycles are slower, hence the longer grid, design R4), and p=4 captures within-year dynamics.

**Our one addition — expanding mode.** Even Hamilton's regression, fit on the FULL sample, lets
month 250's gap be computed with coefficients that saw month 480 (look-ahead). Our
`hamilton_filter(..., mode="expanding")` refits the regression at every t using data through t
only. The measured consequence (verification log, 2026-08-31): the expanding gap is an
**acceleration/turn detector**, not a level gap — it fires in the boom's build-out, decays as the
expanding fit absorbs the boom, and posts its cycle-largest negative reading at the bust onset.
The full-sample gap is retained ONLY as a hindsight descriptive tool, never inside a signal.
Code: `quant/stats/hamilton.py` (no-look-ahead property test in `tests/`).

## D2. Levels into ranks: the expanding percentile

Any threshold on a raw level ("de-risk when credit/GDP gap > 9%") is a magic number, and levels
drift as economies financially deepen. The expanding percentile replaces levels with
self-referenced ranks:

    pct_t  =  (1/N_t) · #{ s ≤ t : y_s < y_t }

"Where does today sit against ALL history known so far?" Three properties we prove in tests:
bounded in [0,1]; no look-ahead by construction (truncating the future never changes the past);
warm-up noise (short reference windows make early ranks unreliable — hence the min_obs mask, and
the honest note in Lesson 1 that we refuse assertions about the earliest months).
Code: `quant/ladder/credit_cycle.py::expanding_percentile`.

## D3. Persistence and the half-life τ½, with the small-sample bias fix

**Why we care.** τ½ orders the entire ladder: how long a state's information lasts sets the
rebalance band, the CV embargo, the bootstrap block length, and which seats may share a budget.

**The model.** Fit AR(1) on the state: x_t = c + ρ·x_{t−1} + ε_t. Persistence ρ ∈ (0,1) converts
to a half-life via

    τ½ = ln(0.5) / ln(ρ)        (the time for a shock's expected effect to halve)

**The trap: OLS ρ̂ is biased DOWN in small samples.** Kendall (1954) / Marriott–Pope:

    E[ρ̂] − ρ ≈ −(1 + 3ρ)/T

With T=120 monthly observations and true ρ=0.95 the bias is ≈ −0.032: you'd estimate τ½ ≈ 8.4
months when the truth is 13.5. Slow cycles get systematically UNDER-estimated exactly when the
sample is short — the dangerous direction (you'd re-tune too fast). We apply the bias correction,
then build the confidence interval by **parametric pivot bootstrap**: simulate thousands of AR(1)
series at ρ̂ (using `ar1_series`, vectorized via scipy lfilter), re-estimate on each, and invert
the distribution of (ρ̂* − ρ̂) to get the CI. Method history, kept on the record: our first
implementation used a moving-block bootstrap CI whose measured coverage at ρ ≥ 0.9 was 0–7%
(catastrophic); the Monte Carlo caught it and the parametric pivot replaced it (coverage 57–92%,
still imperfect at the near-unit-root edge — flagged whenever ρ̂ > 0.9 via the Andrews
near-unit-root flag). Code: `quant/stats/tau_half.py`; evidence: `research/montecarlo/RESULTS.md`.

## D4. Crisis prediction: the logit, and AUROC as a Mann–Whitney statistic

**The logit** (Schularick–Taylor's tool). When the outcome is binary (crisis within k years: 1/0),
OLS can predict probabilities below 0 or above 1. The logit fixes this by modeling

    P(crisis) = 1 / (1 + e^{−(a + b·x)})

b is read like an OLS slope but in log-odds units; the headline "+1σ credit growth ⇒ +2.8pp crisis
probability" is the marginal effect of b evaluated at the sample base rate.

**AUROC** (Lesson 1, Fig 2.2, hover version). Formally, AUROC = P(score_crisis > score_safe) for a
randomly drawn crisis/safe pair — which is exactly the Mann–Whitney U statistic divided by
(n₁·n₀). Two consequences we use: (i) AUROC is rank-based, so it is invariant to any monotone
transform of the score — our percentile transform costs nothing; (ii) its standard error can be
computed from the U-statistic structure, but with overlapping windows (a "crisis within 3y" label
is shared by adjacent months) the effective sample is far smaller than the row count — which is
why R1 mandates purged CV and uniqueness weighting rather than the textbook SE.

## D5. Persistent-regressor bias (Stambaugh) — why credit-state return regressions overstate

Forward-return regressions r_{t+1} = a + b·x_t + e use a regressor x (our state) that is highly
persistent and whose innovations correlate with returns. Stambaugh (1999):

    E[b̂ − b] ≈ γ · E[ρ̂ − ρ],   γ = cov(e, ν)/var(ν)

where ν are the AR(1) innovations of x. The AR(1) downward bias in ρ̂ (D3) leaks into an UPWARD
bias in b̂ when γ < 0 (the usual case for valuation-like states). Every R2-style design therefore
carries the Stambaugh correction plus Newey–West standard errors with h−1 lags (overlapping
horizons make errors autocorrelated by construction).

## D6. Pooling across countries: empirical Bayes shrinkage

India offers 1–2 credit down-legs; the JST panel offers ~90 crises. Neither "use only India"
(hopeless variance) nor "use the pool raw" (India isn't Denmark) is defensible. The empirical
Bayes compromise estimates India's parameter as

    θ_India^EB = w·θ̂_India + (1−w)·θ̄_pool,    w = τ² / (τ² + σ²_India)

where σ²_India is the variance of India's own estimate (huge, tiny sample ⇒ w near 0 initially)
and τ² is the cross-country dispersion of the true parameter (how much countries genuinely
differ). As Indian episodes accumulate, σ²_India falls and w rises — the model *earns* domestication.
The pooled-prior discipline: we import SIGN and approximate magnitude, never point estimates;
cross-country sign-consistency is the admission gate for any new cycle rule (pipeline v2).

## D7. Honest validation: purged K-fold CV with embargo

Random-shuffle CV is look-ahead for time series twice over: (i) training folds contain the
future; (ii) overlapping labels leak across the fold boundary (a "crisis within 3y" label at
Dec-2007 shares its outcome with Jan-2008 in another fold). The fix (López de Prado):
**purge** — drop training observations whose label windows overlap the test fold; **embargo** —
additionally drop a buffer AFTER the test fold (≥ 1×τ½ in our standard) so serial correlation
cannot leak backward. With India's sample we pre-register 4–6 folds. Code: `quant/stats/cv.py`
(`purged_kfold`, `assert_no_leakage`).

## D8. Multiple testing: the deflated Sharpe and the trial ledger

Try N strategies on the same data and the best backtest Sharpe grows like √(2·ln N) even under
the null of zero skill (expected-max formula, implemented in `quant/stats/dsr.py`). The deflated
Sharpe ratio (Bailey–López de Prado) re-benchmarks an observed Sharpe against that expected
maximum given the TRUE number of trials, non-normality (skew, kurtosis), and track length. The
binding discipline is organizational, not mathematical: the trial count must be REAL — hence the
trial ledger (every grid cell, every abandoned attempt, counted) and pipeline v2's rule that the
recorder IS the ledger, with DSR trial counts derived by query, never self-reported.

## D9. Drawdown distributions: why the bootstrap must respect time

A drawdown is a path property — it depends on the ORDER of returns, not just their distribution.
The iid bootstrap (resample returns independently) destroys volatility clustering and
autocorrelation. Measured on our synthetic fixtures (RESULTS.md, MC3 — including the falsified
first reading, kept on the record): for AUTOCORRELATED returns the iid bootstrap understates
drawdown tails in 7–8 of 8 seeds; for pure vol clustering the direction is seed-dependent — so the
design rule is "stationary (block) bootstrap by default because it preserves the dependence
structure (verified via ACF preservation), not because iid is always optimistic."
Politis–Romano stationary bootstrap: resample in blocks of geometric random length L (E[L] tied
to τ½), which keeps clustering while still mixing. Code: `quant/stats/bootstrap.py`.

## D10. Duration analysis for H68 (age-in-quadrant)

The discrete-time hazard: h(a) = P(quadrant exits at age a | survived to a). Estimated by logit
of exit on age (and controls) over quadrant-spells, pooled across the JST panel. Duration
dependence = the age coefficient's sign: positive for business/credit cycles per
Diebold–Rudebusch's classic finding on US expansions [their object: NBER phases]. Our use is
strictly Tier-B pooled: India contributes spells but never its own fitted hazard.

## D11. The composite: weighted signed ranks, and why not "optimal" weights

The L10 composite is w_gap·(2·G−1) + w_cd·(2·C−1) + clamp(...) — a LINEAR rule with
pre-registered weight grids, not an optimized combination. The estimation-theory reason: with
1–2 domestic episodes, any weight optimizer would fit noise (D8's expected-max problem in
miniature); a fixed near-equal weighting of positively-correlated, individually-validated inputs
captures most of the attainable combination benefit (the 1/N logic — DeMiguel-Garlappi-Uppal 2009
for portfolios, same mathematics for signals) while adding zero fitted parameters. Weight grids
get swept ONLY in the pooled panel (R1/R5), never on India alone.
