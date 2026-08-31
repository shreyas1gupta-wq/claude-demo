# Workstream 09 — Estimation and Validation Protocol

Status: RESEARCH ONLY, per `CONTRACT.md` and `OPEN_QUESTIONS.md` (defaults assumed throughout).
Scope: the estimation and validation rulebook the *data phase* must follow — filters, bias
corrections, out-of-sample conventions, cross-validation mechanics, overfitting-adjusted
performance statistics, small-sample regime-switching limits, cross-country pooling for India's
short credit-cycle history, overlapping-window inference, paired Stage-1-vs-Stage-2 tests,
pre-registration, and a phase-by-phase validation gate list. This chapter proposes no alpha
signal and estimates no parameter on data; it specifies the machinery Workstreams 01–08's
candidate signals and CONTRACT §9's estimation standards must be run through before any number
enters the `config/` registry.

**Methodological note, stated up front per CONTRACT §12's honesty requirement.** This session's
`WebSearch` budget was already exhausted before this workstream ran — every call returns "this
session has used its web search budget (200 of 200 WebSearch calls)" — and `WebFetch` to every
domain tested (NBER, Wikipedia, Google) returns `EGRESS_BLOCKED` at the network proxy, consistent
with CONTRACT §7 Known Prior #11 ("this remote environment has no market-data network access…
web search works" — that escape hatch was closed for this run, exactly as Workstream 08 recorded).
Every citation below is therefore drawn from trained knowledge, not live verification, and is
tagged **(recalled, high/moderate confidence)** where I am confident of author/venue/year, or
**[VERIFY: …]** naming exactly what needs checking once search access is restored. This is the
methods chapter of the whole program — it should be prioritized for re-verification alongside
Workstream 08, both because it is citation-dense and because several parameters below (embargo
length, block length, deflated-Sharpe trial count) get *used* by every other workstream's eventual
data-phase validation and should not carry silent citation errors into the registry.

---

## 1. Findings and literature

**F1. Hamilton, James D. (2018), "Why You Should Never Use the Hodrick-Prescott Filter,"
*Review of Economics and Statistics* 100(5), 831–843 (recalled, high confidence).** Shows the HP
filter (i) introduces spurious dynamic relationships not present in the underlying data (the
filtered series can exhibit business-cycle-like autocorrelation even when applied to pure white
noise, because the two-sided smoothing is a specific — and for economic data, poorly justified —
linear filter), (ii) uses future data to compute the "trend" at any past date, so no economically
meaningful interpretation of the endpoint value survives revision, and (iii) the customary
smoothing parameter (λ=1600 quarterly) has no statistical justification tying it to any data
frequency in a principled way. Proposes an alternative: regress the series h periods ahead on a
constant and p of its own lags at the *current* date, and treat the residual (actual minus fitted
projection) as the cyclical component. This uses only information available in real time (no
two-sided smoothing, no endpoint problem) and Hamilton's own applied recommendation for quarterly
U.S. real GDP is **h = 8 quarters (2 years ahead), p = 4 lags**. This is the CONTRACT's own named
replacement for the banned HP filter (§8 traps) and is the anchor citation for this entire section.

**F2. Hamilton (2018), monthly/higher-frequency scaling [VERIFY: exact monthly recommendation —
recalled with moderate confidence].** The paper's headline illustration is quarterly; the commonly
applied practitioner adaptation to monthly data scales both h and p by the ratio of frequencies
(12/4 = 3×), giving **h = 24 months, p = 12 lags**, so the projection horizon stays fixed at "2
years" in calendar time regardless of sampling frequency, and the lag order stays fixed at "1
year" of own-history. I recall this scaling being the standard applied convention in replication
code and follow-on practitioner notes, not a second explicit table in Hamilton's own paper — flag
for direct confirmation before it is frozen into `config/`.

**F3. Stambaugh, Robert F. (1999), "Predictive Regressions," *Journal of Financial Economics*
54(3), 375–421 (recalled, high confidence).** When a predictor y is itself persistent (AR(1)
coefficient ρ near 1) and its innovations are correlated with the return-equation innovations
(the standard "leverage"/valuation-ratio case), the OLS slope in a predictive regression of returns
on lagged y is biased **in the same direction as the small-sample downward bias in ρ̂** — i.e., a
genuinely near-zero predictive slope can appear spuriously significant with the "wrong-looking"
small-sample properties working in the predictor's favor. Stambaugh derives the exact small-sample
bias under joint normality and proposes subtracting the estimated bias (built from the AR(1) bias,
itself approximable by the classical Kendall/Marriott-Pope first-order correction, F13 below) from
the OLS point estimate. Later refinements offering easier implementations: **Amihud & Hurvich
(2004), "Predictive Regressions: A Reduced-Bias Estimation Method," *Journal of Financial and
Quantitative Analysis* 39(4), 813–841** [VERIFY: exact pages, moderate confidence] (an augmented-
regression trick that adds the AR(1) residual as a regressor to absorb the bias directly); **Lewellen
(2004), "Predicting Returns with Financial Ratios," *Journal of Financial Economics* 74(2), 209–235**
[VERIFY: moderate confidence] and **Campbell & Yogo (2006), "Efficient Tests of Stock Return
Predictability," *Journal of Financial Economics* 81(1), 27–60** (moderate-high confidence) build
confidence-interval and test-statistic corrections for the near-unit-root case specifically.

**F4. Goyal, Amit & Welch, Ivo (2008), "A Comprehensive Look at The Empirical Performance of
Equity Premium Prediction," *Review of Financial Studies* 21(4), 1455–1508 (recalled, high
confidence).** Re-examines essentially every published U.S. equity-premium predictor against a
common out-of-sample yardstick — the historical (expanding-window) mean return — and finds most
predictors that look significant in-sample deliver **negative out-of-sample R²** against that naive
benchmark across most sample splits, i.e., they would have made an investor worse off than simply
using the trailing average. This is the paper that established out-of-sample R² *against the
historical mean, never against zero or against in-sample fit*, as the field's standard yardstick —
directly the convention CONTRACT §9 invokes ("out-of-sample R² judged against the historical-mean
benchmark, never in-sample").

**F5. Campbell, John Y. & Thompson, Samuel B. (2008), "Predicting Excess Stock Returns Out of
Sample: Can Anything Beat the Historical Average?," *Review of Financial Studies* 21(4), 1509–1531
(recalled, high confidence, same RFS issue as F4 — a well-known paired publication).** Shows that
imposing economically motivated sign restrictions — (i) the fitted equity-premium forecast is
truncated at zero (never allow a negative expected excess return, since arbitrageurs would not hold
the market otherwise under most models), and (ii) the estimated regression slope is truncated to
carry its theoretically expected sign — flips **most of Goyal-Welch's negative out-of-sample R²
values to modestly positive** (order of magnitude: monthly OOS R² moving from roughly −2% to +0.5%
to +1% for several predictors [VERIFY: exact figures per predictor]), without any in-sample
retuning. This is the CONTRACT-compliant way to add a prior without breaking the "no magic
numbers" rule: the restriction is a *sign* rule, not a fitted threshold.

**F6. Rapach, David E., Strauss, Jack K. & Zhou, Guofu (2010), "Out-of-Sample Equity Premium
Prediction: Combination Forecasts and Links to the Real Economy," *Review of Financial Studies*
23(2), 821–862 (recalled, high confidence).** Shows that simple **combination forecasts** — e.g.
the equal-weighted average of many individual univariate predictive regressions — deliver
consistently positive and statistically/economically significant out-of-sample R² even when most
of the individual predictors do not, because combination diversifies away each predictor's
idiosyncratic estimation noise while retaining shared signal. Directly informs how the CONTRACT's
tau_half-ordered ladder of state variables should be *combined* (simple, out-of-sample-robust
combination as the baseline Stage-1 benchmark model to beat) rather than tested one at a time.

**F7. López de Prado, Marcos (2018), *Advances in Financial Machine Learning*, Wiley, Ch. 7
"Cross-Validation in Finance" (recalled, high confidence on substance and chapter number).**
Formalizes **purged K-fold cross-validation**: because financial labels are frequently constructed
from a forward-looking window (e.g., a return over the next H periods, or a triple-barrier label),
any training observation whose label window overlaps in time with a test observation's label
window leaks information across the split and must be **purged** from the training fold. Adds an
**embargo**: even non-overlapping training observations immediately following a test fold can still
be correlated with it through the serial dependence of features and labels, so an additional
embargo window is removed from training after each test fold. López de Prado's own worked default
sets the embargo as a small fixed fraction of the total sample (he mentions on the order of 1%
[VERIFY: exact fraction, recalled with only moderate confidence]) — this dossier proposes replacing
that fixed-fraction default with an embargo tied explicitly to each signal's own `tau_half` (§4),
which is both more principled and CONTRACT-compliant (no magic numbers).

**F8. Bailey, David H. & López de Prado, Marcos (2014), "The Deflated Sharpe Ratio: Correcting for
Selection Bias, Backtest Overfitting, and Non-Normality," *Journal of Portfolio Management* 40(5),
94–107 (recalled, high confidence on title/venue/year).** Formalizes the **Deflated Sharpe Ratio
(DSR)**: given N trials (configurations tested, whether or not all N are reported), the *expected
maximum* Sharpe ratio achievable by chance alone under a true-zero-Sharpe null rises with N (via
extreme-value-theory order statistics of correlated/independent normal draws); DSR tests the
achieved Sharpe against that inflated benchmark rather than against zero, and further adjusts the
Sharpe ratio's own sampling variance for skewness and kurtosis (a non-normal-return correction
building on **Mertens (2002)** [VERIFY: exact citation for the skew/kurtosis-adjusted Sharpe
variance — recalled with only moderate confidence] rather than the classical normal-return Sharpe
standard error). Companion: **Bailey, Borwein, López de Prado & Zhu**, "The Probability of Backtest
Overfitting," circulated 2014, published in the *Journal of Computational Finance* [VERIFY: exact
year of print publication, I recall ~2017 for the print version though the working paper is 2014] —
combinatorially-symmetric cross-validation (CSCV) estimate of the probability that the
in-sample-best configuration underperforms out-of-sample, a natural companion metric to DSR for a
whole parameter sweep.

**F9. Bailey, David H. & López de Prado, Marcos (2012), "The Sharpe Ratio Efficient Frontier,"
*Journal of Risk* 15(2), 3–44 [VERIFY: exact volume/issue/pages, moderate confidence] (recalled,
moderate-high confidence on substance).** Derives the **Minimum Track Record Length (MinTRL)**: the
number of observations needed, given an *observed* (skew/kurtosis-adjusted) Sharpe ratio and a
target confidence level, before one can assert with that confidence that the *true* Sharpe exceeds
a benchmark (e.g., zero, or a hurdle rate). Directly answers "how long must our paper-trading /
early-live track record run before we can even statistically distinguish it from luck" — a
mandatory gate before any book's capital is scaled up (§4, §6 below).

**F10. Harvey, Campbell R., Liu, Yan & Zhu, Heqing (2016), "…and the Cross-Section of Expected
Returns," *Review of Financial Studies* 29(1), 5–68 (recalled, high confidence).** Surveys roughly
300+ factors published in the cross-sectional asset-pricing literature and argues that, given this
scale of collective multiple testing across the whole field (not just one paper's own sweep), the
conventional t>1.96 significance bar is far too permissive; proposes a **minimum t-statistic of
approximately 3.0** for a newly proposed factor to be taken seriously, with a Bayesian framework
formalizing how the bar should rise further as the number of factors ever tested keeps growing.
This is the CONTRACT-referenced "Harvey-Liu-Zhu t>3 standard."

**F11. Harvey, Campbell R. (2017), "Presidential Address: The Scientific Outlook in Financial
Economics," *Journal of Finance* 72(4), 1399–1440 (recalled, high confidence on title/venue/year,
moderate on exact pages).** Extends F10 into a broader critique of empirical asset-pricing practice
— p-hacking, HARKing (hypothesizing after results are known), and the "garden of forking paths" —
and explicitly proposes finance adopt **pre-registration** (as in medicine/psychology's registered-
reports movement) as the structural fix, since post-hoc significance thresholds alone cannot
distinguish a genuinely pre-specified test from a selected one. This is the direct citation behind
CONTRACT §9's "pre-register every hypothesis… never re-test a rejected idea with tweaked
parameters," and behind §6's pre-registration template below.

**F12. Politis, Dimitris N. & Romano, Joseph P. (1994), "The Stationary Bootstrap," *Journal of the
American Statistical Association* 89(428), 1303–1313 (recalled, high confidence).** Proposes
resampling blocks of **geometrically distributed random length** (mean block length 1/p, for a
tuning parameter p) rather than fixed-length blocks, which — unlike the fixed-block bootstrap —
produces a resampled series that is itself exactly stationary, avoiding edge artifacts at block
boundaries. This is the CONTRACT-referenced mechanism for **block bootstrap of drawdown
distributions**: resampling blocks (not single days) preserves the vol-clustering / regime-
persistence structure that drives real drawdowns, which an iid bootstrap of daily returns would
destroy (an iid bootstrap systematically understates tail drawdown risk because it cannot generate
a run of consecutive bad days at the empirically observed rate).

**F13. Politis, Dimitris N. & White, Halbert (2004), "Automatic Block-Length Selection for the
Dependent Bootstrap," *Econometric Reviews* 23(1), 53–70, with correction by **Patton, Andrew,
Politis, Dimitris N. & White, Halbert (2009), *Econometric Reviews* 28(4), 372–375** [VERIFY: exact
pages both papers, recalled with moderate confidence].** Gives a data-driven plug-in formula for the
optimal (MSE-minimizing) mean block length for the stationary/circular bootstrap, based on an
estimate of the series' own spectral density near frequency zero (equivalently, its own
autocorrelation decay). This is the rigorous fallback this dossier proposes alongside a simpler,
CONTRACT-consistent heuristic tying block length directly to `tau_half` (§4).

**F14. Kendall, Maurice G. (1954), "Note on Bias in the Estimation of Autocorrelation," *Biometrika*
41(3/4), 403–404, and independently Marriott, F.H.C. & Pope, J.A. (1954), "Bias in the Estimation
of Autocorrelations," *Biometrika* 41(3/4), 390–402 [VERIFY: exact titles/pages, recalled with
moderate confidence].** Derive the classical first-order small-sample bias of the OLS AR(1)
coefficient: **E[ρ̂] − ρ ≈ −(1+3ρ)/T**. This is the same bias term underlying Stambaugh's (F3)
correction, and is the direct tool for correcting `tau_half` estimates (§4) computed from AR(1)
fits on short Indian samples, where the naive estimate is biased toward *understating* persistence
(and hence understating half-life). For ρ close to 1 (the long-cycle end of the ladder) the
first-order approximation itself degrades and a fuller correction is warranted: **Andrews, Donald
W.K. (1993), "Exactly Median-Unbiased Estimation of First Order Autoregressive/Unit Root Models,"
*Econometrica* 61(1), 139–165** (recalled, moderate-high confidence) gives an exact median-unbiased
mapping from ρ̂ to a bias-corrected ρ across the full [−1,1] range including near-unit-root; **Hansen,
Bruce E. (1999), "The Grid Bootstrap and the Autoregressive Model," *Review of Economics and
Statistics* 81(4), 594–607** [VERIFY: moderate confidence] gives a bootstrap-based confidence
interval that remains valid near the unit root, where standard asymptotic normal intervals do not.

**F15. Hansen, Lars Peter & Hodrick, Robert J. (1980), "Forward Exchange Rates as Optimal Predictors
of Future Spot Rates: An Econometric Analysis," *Journal of Political Economy* 88(5), 829–853
(recalled, high confidence).** Establishes that an h-period-ahead overlapping regression (each
observation shares h−1 periods with its neighbors) induces an MA(h−1) error structure under the
null of no predictability purely from the overlap mechanics, so ordinary OLS standard errors are
badly downward-biased (inflating apparent t-statistics) unless corrected. Practically superseded in
routine use by **Newey, Whitney K. & West, Kenneth D. (1987), "A Simple, Positive Semi-Definite,
Heteroskedasticity and Autocorrelation Consistent Covariance Matrix," *Econometrica* 55(3), 703–708
(recalled, high confidence)**, whose kernel-weighted HAC estimator generalizes Hansen-Hodrick,
guarantees a positive-semi-definite covariance matrix, and is the default correction this dossier
recommends for every overlapping-window regression in the program (bandwidth ≥ h−1, chosen via
Newey-West's own automatic-bandwidth rule or set conservatively to the overlap length).

**F16. Diebold, Francis X. & Mariano, Roberto S. (1995), "Comparing Predictive Accuracy," *Journal
of Business & Economic Statistics* 13(3), 253–263 (recalled, high confidence).** Tests whether two
competing forecasts (or, by direct extension, two competing portfolio construction rules'
period-by-period realized loss/utility) have equal expected accuracy, using the HAC-corrected mean
of the paired loss differential. **Harvey, David, Leybourne, Stephen & Newbold, Paul (1997),
"Testing the Equality of Prediction Mean Squared Errors," *International Journal of Forecasting*
13(2), 281–291** [VERIFY: exact pages, moderate-high confidence] provide a small-sample correction
factor and recommend Student-t (not normal) critical values — essential here because India's
paired Stage-1-vs-Stage-2 evaluation window will realistically be well under 100 monthly
observations for years (§4, §6).

**F17. Jobson, J. Dave & Korkie, Bob M. (1981), "Performance Hypothesis Testing with the Sharpe and
Treynor Measures," *Journal of Finance* 36(4), 889–908 (recalled, high confidence).** Original test
for whether two portfolios' Sharpe ratios differ significantly, accounting for the fact that the
two return series are typically correlated (same underlying market exposure) rather than
independent. **Memmel, Christoph (2003), "Performance Hypothesis Testing with the Sharpe Ratio,"
*Finance Letters* 1, 21–23** [VERIFY: exact venue/pages, moderate confidence — an obscure venue for
what is now a standard formula] corrects an error in the original test statistic's asymptotic
variance. The corrected "Jobson-Korkie-Memmel" test is the standard tool for exactly the CONTRACT's
Stage-1-vs-Stage-2 and sub-signal-vs-sub-signal comparisons (§4, §6).

**F18. Psaradakis, Zacharias & Sola, Martin (1998), "Finite-Sample Properties of the Maximum
Likelihood Estimator in Autoregressive Models with Markov Switching," *Journal of Econometrics*
86(2), 369–386 [VERIFY: exact title/pages, moderate confidence — a less mainstream citation
recalled with lower certainty than F1–F17].** Monte Carlo evidence that Markov-switching MLE/EM
estimates — transition probabilities in particular — are severely biased and unstable in small
samples and few observed regime transitions, with confidence intervals routinely too narrow to be
trusted. Consistent broader literature point (folklore, not a single paper): **Hamilton, James D.
(1989), "A New Approach to the Economic Analysis of Nonstationary Time Series and the Business
Cycle," *Econometrica* 57(2), 357–384** (recalled, high confidence) — the founding Markov-switching
paper — was itself estimated on a long U.S. NBER-dated recession sample with many transitions;
survey **Ang, Andrew & Timmermann, Allan (2012), "Regime Changes and Financial Markets," *Annual
Review of Financial Economics* 4, 313–337** [VERIFY: moderate confidence] discusses the general
small-sample fragility of fitted regime-switching models in finance applications. Together these
are the literature basis for CONTRACT's hard trap (§8): "Do NOT fit regime-switching models without
≥10 observed transitions."

**F19. Jordà, Òscar (2005), "Estimation and Inference of Impulse Responses by Local Projections,"
*American Economic Review* 95(1), 161–182 (recalled, high confidence).** Estimates impulse
responses via a sequence of horizon-specific single regressions of the outcome h periods ahead on
the shock/state today plus controls, rather than inverting a VAR — more robust to model
misspecification, and trivially allows state-dependent (nonlinear) impulse responses by
interacting the regressor with an indicator for the state (e.g., "credit boom" vs "not"). This is
the template method for India credit-cycle parameter estimation (§4). Jordà, Schularick & Taylor
extend the same local-projection method on their jointly built **Jordà-Schularick-Taylor (JST)
Macrohistory Database** (annual panel, ~17–18 advanced economies, 1870–present, ~150 years) across
several papers: **Schularick, Moritz & Taylor, Alan M. (2012), "Credit Booms Gone Bust: Monetary
Policy, Leverage Cycles, and Financial Crises, 1870–2008," *American Economic Review* 102(2),
1029–1061** (recalled, high confidence) — establishes credit growth as a leading indicator of
financial crises across the panel; **Jordà, Schularick & Taylor (2013), "When Credit Bites Back,"
*Journal of Money, Credit and Banking* 45(s2), 3–28** [VERIFY: exact pages, moderate-high
confidence] — state-dependent local projections showing recoveries are slower and deeper after
credit-fueled expansions; **Jordà, Schularick & Taylor (2017), "Macrofinancial History and the New
Business Cycle Facts," *NBER Macroeconomics Annual* 31(1), 213–263** [VERIFY: exact volume/pages,
moderate confidence] — the broadest synthesis, explicitly proposed here as the cross-country panel
to partially pool India's own thin credit-cycle sample against (§4).

**F20. Partial pooling / hierarchical shrinkage — Efron, Bradley & Morris, Carl (1975), "Data
Analysis Using Stein's Estimator and Its Generalizations," *Journal of the American Statistical
Association* 70(350), 311–319** (recalled, moderate-high confidence); **DerSimonian, Rebecca &
Laird, Nan (1986), "Meta-Analysis in Clinical Trials," *Controlled Clinical Trials* 7(3), 177–188**
(recalled, moderate-high confidence) — the random-effects meta-analysis formula (inverse-variance-
weighted pooling of a group-specific estimate and a global estimate, weight determined by the
group's own sampling variance versus the cross-group heterogeneity variance) is mathematically the
same empirical-Bayes/James-Stein shrinkage recipe applicable to "India's credit-cycle slope vs the
JST panel's pooled slope" (§4); textbook treatment: **Gelman, Andrew & Hill, Jennifer (2007), *Data
Analysis Using Regression and Multilevel/Hierarchical Models*, Cambridge University Press**
(recalled, high confidence as a textbook, exact citation of the specific edition not critical).

**F21. Ferson, Wayne, Sarkissian, Sergei & Simin, Timothy (2003), "Spurious Regressions in
Financial Economics?," *Journal of Finance* 58(4), 1393–1414 (recalled, moderate-high
confidence).** Shows that a persistent (but economically unrelated) "fundamental-looking" regressor
combined with persistent returns can generate spurious in-sample predictive R² even with no true
relationship, reinforcing why out-of-sample validation (F4–F6) rather than in-sample fit is
non-negotiable for anything on the tau_half ladder.

**F22. Brier, Glenn W. (1950), "Verification of Forecasts Expressed in Terms of Probability,"
*Monthly Weather Review* 78(1), 1–3 (recalled, high confidence).** The proper scoring rule behind
Open Question #7's "Brier-scored override ledger" for every Stage-2 discretionary call — squared
error between a stated probability and the realized binary outcome, minimized in expectation only
by honest probability statements, giving a calibration audit trail independent of the paired
Diebold-Mariano test on realized portfolio outcomes.

---

## 2. India-specific evidence

Every technique above is validated on U.S./international data far deeper than anything free and
point-in-time in India offers, so this section is about *consequences for application*, not new
India-specific statistical findings — none of F1–F22 are India studies, and this dossier does not
manufacture an India citation where none exists. Per CONTRACT's "India first" instruction, the
honest statement is: **all of §1 is a cross-country/methodological prior (Tier B at best where it
touches an empirical magnitude, Tier A as pure statistical method)**, and this section states what
that means once applied to India's actual data footprint.

**Sample depth.** Free-source Indian data usable for any of the above starts, in practice, in the
early-to-mid 1990s: NSE bhavcopy (post-1994/95 electronic trading), RBI DBIE monthly series
(several — WPI/CPI, non-food bank credit growth, monetary aggregates — extend further back annually
but monthly regularity is a 1990s-onward phenomenon), AMFI NAV history (mutual funds, mid-1990s
onward), CCIL data (later still). That gives roughly **30–32 years, ~370–385 monthly observations**
by 2026 for the best-covered series — enough for Hamilton-filter estimation (needs only p+1
regressors, trivially satisfied) but thin for anything requiring multiple *independent* cycles.
Per CONTRACT §7 Known Prior #1, only 5 of 32 candidate cycles survived the clock test at all, and
CONTRACT §9 states outright that "India alone offers <2 cycles" for panel purposes on at least the
credit/financial cycle — this dossier does not re-derive that count (it is Workstream 03's and
08's job) but takes it as the binding input to §4's pooling recipe: with n<4 independent domestic
observations, CONTRACT's own tier ladder places any India-only credit-cycle parameter at **Tier B
at best, frozen at inception**, which is exactly why partial pooling on JST (F19–F20) is not
optional color but the *only* CONTRACT-compliant route to a data-driven number at all — the
alternative is Tier C narrative with no fitted parameter.

**Structural breaks compound the depth problem.** India's ~30-year usable sample straddles at least
four regime-shifting events that plausibly break stationarity of any AR(1)/tau_half or
Hamilton-filter estimate run on the full span: 1991 liberalization/opening of capital account
(pre-1991 data is a different economy and should not be pooled with post), the 2003–08 structural
bull market and FII-flow liberalization, 2016 demonetization + GST rollout (a joint monetary/fiscal
regime shift), and the 2020 COVID shock. A single full-sample AR(1) fit spanning all of these
conflates genuine mean-reverting dynamics with slow drift across regimes. This dossier adds an
India-specific gate not explicitly named in CONTRACT §9 but implied by its own "no magic numbers"
and honesty standards: **every tau_half / AR(1) estimate must also be reported on a rolling or
recursive window and checked for gross instability across these known break dates before being
trusted at full-sample precision** — a cheap, non-parametric robustness check (not a formal
Bai-Perron break test, which itself needs more data than we may have per subsample) appropriate to
a program this data-constrained.

**Effective sample after purge+embargo shrinks further.** With ~380 monthly observations, a purge
window equal to a 12-month label horizon plus an embargo of one `tau_half` (say 12–24 months for a
mid-frequency state variable, §4) removes on the order of 24–48 months around *each* fold boundary.
A conventional 10-fold purged CV would leave several folds with only a couple of dozen usable
training months adjacent to the test fold — too little to estimate anything beyond the simplest
sign/quantile rule CONTRACT already favors. The recommended fix is **fewer, wider folds (4–6
purged folds, not 10)** for any India-only monthly series, explicitly reported as a lower-power
test than a textbook 10-fold CV would suggest, rather than silently keeping 10 folds and accepting
degraded purge/embargo discipline to make the fold count look standard.

**Egress constraint feeds directly into the Phase-0 gate (§6).** Per Known Prior #11, the data
phase runs on the principal's machine with no live network access from this environment; every
indicator must resolve against a **committed, checksummed fixture**. That is not a caveat on the
statistical methods above — it is a prerequisite for reproducing purged CV folds, block-bootstrap
draws, and DSR trial counts identically across runs, which is why §6 makes fixture-pinning a
formal pre-condition of every later gate rather than an implementation detail.

---

## 3. Decay and crowding assessment

CONTRACT §5 asks every *alpha signal* for a decay-survival argument. The techniques in this
dossier are not alpha signals; they are the discipline that prevents an alpha claim from decaying
the moment it meets real money — but the mapping is close enough, and instructive enough, to make
explicit signal-by-signal below. The residual risk in each row is exactly the failure mode the
CONTRACT's own traps (§8) exist to close.

| Technique | Decay/overfitting mechanism it defends against | Residual risk if misapplied |
|---|---|---|
| Hamilton regression filter (not HP) | HP's phantom cyclicality and endpoint revision would make a state variable look mean-reverting purely as a filter artifact — an edge that "decays" the moment real-time data (no future lookback) replaces the backtest's two-sided smoothing | Wrong h/p for the frequency band (§4) reintroduces the same look-ahead the filter exists to remove |
| Stambaugh/Kendall bias correction | A near-unit-root predictor's OLS slope looks significant purely from the AR(1) small-sample bias, not genuine predictability — vanishes once bias-corrected, i.e., it was never a real edge | Applying the first-order Kendall correction to a truly near-unit-root series (ρ→1) under-corrects; needs Andrews/Hansen exact methods there |
| OOS R² vs historical mean (Goyal-Welch) | The single largest documented decay mechanism in return prediction: in-sample R² is routinely positive where OOS R² is negative — this is McLean-Pontiff's mechanism made operational as a pass/fail test | A predictor can clear this bar in one sample split by chance; must be checked across multiple non-overlapping OOS windows, not one |
| Campbell-Thompson sign restrictions | Guards against a *fitted* threshold masquerading as an economic prior — the restriction must be argued from theory *before* seeing the data, never chosen because it improves the backtest | If the sign restriction itself is chosen post-hoc from the data, it is exactly the "tune thresholds against backtest Sharpe" trap (§8) with an extra step |
| Purged + embargoed CV | Leakage from overlapping labels/features is the single most common source of an "edge" that is pure look-ahead bias, dissolving completely in live trading | Embargo too short relative to `tau_half` leaves residual leakage; too long needlessly shrinks an already-thin India sample (§2) |
| Deflated Sharpe Ratio / true trial count | Directly formalizes "how much of your Sharpe ratio is just how many things you tried" — the central mechanism behind McLean-Pontiff/Harvey-Liu-Zhu decay | An **undercounted** trial ledger (counting only the "final" configuration, not every point actually compared during a sweep) silently defeats the entire correction — see the worked example, §4 |
| Harvey-Liu-Zhu t>3 / Harvey 2017 pre-registration | As more factors get tested industry-wide over time, any *fixed* significance bar itself decays in stringency — Harvey's own argument is that the bar should rise, not stay at t>3 forever | Treating t>3 as sufficient (rather than necessary) once the field's cumulative trial count keeps growing is itself a decaying safeguard; this program's own cumulative trial ledger (§4) must be tracked over its full life, not reset per workstream |
| Block bootstrap for drawdown (Politis-Romano) | An iid bootstrap of daily returns cannot generate a realistic run of consecutive bad days, so it systematically understates tail drawdown — directly relevant to the CONTRACT's binding drawdown constraint | Block length too short collapses back toward iid (understates DD tails); too long leaves too few effectively independent blocks to resample meaningfully in a ~30-year India sample |
| ≥10-transition floor for regime-switching | Fitted Markov-switching transition probabilities with few transitions are Monte-Carlo-documented (Psaradakis-Sola) to be unstable and overconfident — a "regime edge" from 2 transitions is usually one anomalous episode dressed up as a structural state | The floor itself could be gamed by defining "a transition" loosely (e.g., counting sub-episodes within one crisis); CONTRACT's clock-test logic for cycles (≥4 complete periods) should anchor the *same* discipline for transition-counting |
| Partial pooling on JST panel | Without pooling, an India-only credit-cycle parameter is fit to essentially 1–2 data points and would overfit certainly — pooling is the direct antidote, not an optional refinement | Pooling toward a panel of *advanced*-economy crises risks importing a mechanism (developed-market bank leverage cycles) that may not transplant to India's more administered banking system; the shrinkage weight (§4) must be justified, not just computed |
| Diebold-Mariano / Jobson-Korkie-Memmel paired tests | Prevents Stage-2 "looking better" purely from a lucky sample path rather than genuine incremental skill — directly operationalizes Open Question #7's stay-on gate | Small-T India live-track bias (§2) requires the Harvey-Leybourne-Newbold small-sample correction (F16); the plain asymptotic DM test overstates significance at our realistic sample sizes |

---

## 4. Proposed parameters

| Name | Value/range | Source | Tier | Confidence | Decay assumption | What would change it |
|---|---|---|---|---|---|---|
| Hamilton filter, quarterly-equivalent state variables (credit/business-cycle band) | h = 8 quarters, p = 4 lags | Hamilton (2018), F1 | A (method) | High | N/A — mechanical filter, no decay | If Hamilton (2018) itself is superseded by a later refinement in the literature |
| Hamilton filter, monthly state variables (flow/liquidity band) | h = 24 months, p = 12 lags | Practitioner scaling of Hamilton (2018), F2 | B (application) | Moderate | N/A | Direct confirmation of the paper's own monthly guidance once search access returns |
| Hamilton filter, annual/long-wave band | h = 2 years, p = 2 lags — **illustrative/monitoring only**, never fitted or backtested | Scaling of F1; CONTRACT §4 consequence #6 caps long-wave influence | C (narrative) | Low | N/A | Never promoted past Tier C per CONTRACT's own 200-year-cycle ruling |
| Stambaugh/Kendall bias correction | Apply to **every** ladder-listed AR(1)/predictive-regression estimate, not gated by an arbitrary ρ cutoff | Stambaugh (1999), F3; Kendall (1954)/Marriott-Pope (1954), F14 | A (method) | High | N/A | Andrews (1993)/Hansen (1999) exact correction substituted whenever ρ̂ > ~0.9 (near-unit-root regime where first-order approximation degrades) |
| OOS R² benchmark | Expanding-window historical mean; report even when negative | Goyal-Welch (2008), F4 | A (method) | High | N/A | Never — this is the field standard the CONTRACT itself invokes |
| Sign/theory restrictions on fitted signals | Apply Campbell-Thompson-style restrictions only where an ex-ante theoretical sign exists; report both restricted and unrestricted OOS R² | Campbell & Thompson (2008), F5 | A (method) | High | N/A | If a restriction cannot be argued before seeing data, it is not eligible |
| Combination benchmark | Equal-weight combination across all Tier A/B ladder state variables as the model every individual signal must beat | Rapach, Strauss & Zhou (2010), F6 | A (method) | High | N/A | Weighted-combination variants only after equal-weight is shown insufficient, pre-registered |
| Purge window | = signal's label/forecast horizon H (deterministic from label construction) | López de Prado (2018), F7 | A (method) | High | N/A | N/A — mechanical requirement |
| Embargo window | ≥ 1× `tau_half` of the signal (2× for Tier B/C signals, given their wider measurement uncertainty) | This dossier's adaptation of López de Prado (2018) F7, tied to CONTRACT's own tau_half construct instead of a fixed % | B (application) | Moderate | N/A | Any evidence the underlying serial dependence decays faster/slower than the point tau_half estimate (i.e., non-exponential ACF) |
| CV fold count, India-only monthly series | 4–6 purged folds (not a default 10) | This dossier, §2 sample-depth argument | B (application) | Moderate | N/A | Recompute once effective post-purge sample per fold is quantified in the data phase |
| Deflated Sharpe Ratio, trial count N | = full size of every grid actually compared, cumulative across the whole research program (e.g., 7-point hedge sweep × R regime states × F factor-weight grid points; see worked example below) | Bailey & López de Prado (2014), F8; CONTRACT §9 | A (method) | High | N/A | N never decreases; only grows as more sweeps run |
| Significance bar for Tier-A promotion | t > 3 **and** DSR > 0 (both required, not either/or) | Harvey, Liu & Zhu (2016), F10; Bailey & López de Prado (2014), F8 | A (method) | High | N/A | Raise further if the program's own cumulative trial count grows large relative to the number of genuinely distinct hypotheses (Harvey 2017 argument, F11) |
| Minimum Track Record Length | Computed per book at its claimed skew/kurtosis-adjusted Sharpe and a 95% confidence target before any capital-scale-up milestone | Bailey & López de Prado (2012), F9 | A (method) | Moderate-high | N/A | Exact formula pinned against the source paper in the data phase before being hard-coded |
| Block bootstrap mean block length (drawdown distributions) | ≈ 2–4× `tau_half` of the return series under test; Politis-White plug-in as rigorous fallback | Politis & Romano (1994), F12; Politis & White (2004)/Patton-Politis-White (2009), F13 | B (application) | Moderate | N/A | Plug-in spectral estimate substituted once enough data exists to estimate it reliably (needs more than our shortest India series offer) |
| Regime-switching minimum observed transitions | ≥ 10 (hard floor; below this, use continuous quantile-rank state variables, not fitted Markov-switching) | CONTRACT §8 trap; Psaradakis & Sola (1998), F18 | A (method) | High | N/A | Never relaxed below 10 for India-only fits; may be reached sooner via the JST-pooled route (below) if pooled transitions count toward power, though the *India-specific* transition-matrix estimate still needs its own 10 |
| JST partial-pooling shrinkage weight | w = τ²/(τ² + σ²_India), empirical-Bayes/James-Stein weight; τ² = cross-country dispersion of country-specific slopes in the JST panel local projections, σ²_India = India's own small-n sampling variance | Efron & Morris (1975), DerSimonian & Laird (1986), F20; local-projection method Jordà (2005)/Jordà-Schularick-Taylor, F19 | B (n<4 domestic obs, ≥10 cross-country analogues) | Moderate | N/A | Recompute whenever a new India credit cycle completes (raises n, lowers σ²_India, raises w toward India-specific) |
| DM small-sample correction | Always apply Harvey-Leybourne-Newbold correction and use Student-t(T−1) critical values (never assume T is large) | Harvey, Leybourne & Newbold (1997), F16 | A (method) | Moderate-high | N/A | Irrelevant once paired evaluation T comfortably exceeds ~200 (unlikely inside this program's 3–6 month timeline) |
| Sharpe-difference test (Stage-1 vs Stage-1+2, sub-signal vs sub-signal) | Jobson-Korkie-Memmel corrected variance test | Jobson & Korkie (1981); Memmel (2003), F17 | A (method) | Moderate (exact formula [VERIFY]) | N/A | Pin exact Memmel (2003) variance formula before hard-coding |
| Pre-registration stop rule | A hypothesis that fails its pre-registered minimum effect at its pre-registered significance is retired permanently in the registry; reopening requires a **new mechanism argument**, entered as a new registry item with its own trial count | Harvey (2017), F11; CONTRACT §9 | A (method) | High | N/A | Never — this is the structural fix, not a tunable parameter |
| Structural-break rolling-stability check (India-specific addition) | Report every tau_half/AR(1)/Hamilton-filter estimate on rolling/recursive windows spanning 1991, 2003, 2008, 2016, 2020 break dates; flag gross instability before trusting the full-sample point estimate | This dossier, §2 | B (application) | Moderate | N/A | Formal Bai-Perron break test once enough post-break data exists per subsample |

**Worked example — honest trial counting entering the Deflated Sharpe Ratio.** Suppose the hedge-
ratio sweep (7 points: 0/25/50/75/100/125/150%, per CONTRACT §3) is evaluated **jointly** with a
regime grid of R states (drawn from Workstream 04's drawdown-control regime matrix) and a
factor-weight grid of F discretized combinations (drawn from Workstream 02's value/quality/low-vol
weighting scheme). The naive (and CONTRACT-forbidden) approach counts N=1 — "we only report the one
configuration we shipped." The honest approach counts **N = 7 × R × F**, because the *selection* of
that one configuration — even an informal visual comparison across the grid before choosing a
functional form — is exactly the mechanism that inflates the expected maximum Sharpe ratio
achievable by chance under a true-zero-Sharpe null (F8). The DSR itself is [VERIFY: exact formula
recalled with moderate confidence, structure believed correct]:

```
DSR = Φ( (SR_hat − SR*) · sqrt(T−1) / sqrt(1 − γ3·SR_hat + ((γ4−1)/4)·SR_hat²) )
SR* ≈ sqrt(Var[SR_n]) · [ (1−γ)·Φ⁻¹(1 − 1/N) + γ·Φ⁻¹(1 − 1/(N·e)) ]
```

where γ ≈ 0.5772 (Euler-Mascheroni constant), γ3/γ4 are the strategy return distribution's skewness
and excess kurtosis, and Var[SR_n] is the cross-trial variance of Sharpe ratios actually observed
across the grid (a simplifying approximation when trials are not fully independent). **N must be
the cumulative count across the whole research program's sweeps that share the same underlying
return series**, not reset to zero each time a new workstream reports a result — a hedge-ratio point
already compared in Workstream 04 counts again here if this workstream re-examines the same grid.

---

## 5. Evidence-tier recommendations

Grading here is of the *validation methods themselves*, distinct from the alpha signals they will
be applied to (those are graded in Workstreams 01–08). Most methods below are Tier A as pure
statistical technique — decades of applied econometrics, effectively unlimited "observations" of
their own validity across fields — but **their application to India's specific short history** is
frequently constrained to Tier B regardless of the method's own pedigree, and that distinction is
kept explicit in every row.

| Method | Method's own evidentiary tier | India-application constrained tier | Observation-count context |
|---|---|---|---|
| Hamilton regression filter | A | A (mechanical, works on any T > p+1) | No India-specific degradation; only the monthly h/p scaling (F2) is Tier B pending direct confirmation |
| Stambaugh/Kendall bias correction | A | A (mechanical) | Same |
| OOS R² vs historical mean, Campbell-Thompson restrictions, combination forecasts | A | **B** for India series specifically | Method universal; but with ~380 India monthly obs, splitting into train/OOS windows leaves each OOS window short — report multiple non-overlapping splits, not one |
| Purged + embargoed CV | A | **B** | Fold count must drop to 4–6 given India's post-purge effective sample (§2) |
| Deflated Sharpe Ratio, MinTRL | A | A (mechanical once T and N are known) | Formula validity doesn't depend on India-specific data; only the *magnitude* of N (trials) is program-specific |
| Harvey-Liu-Zhu t>3, Harvey 2017 pre-registration | A | A (a research-discipline standard, not a data-fitted parameter) | N/A |
| Block bootstrap (stationary bootstrap) | A | **B** | Politis-White plug-in block length needs more data than India's shortest relevant series offer; tau_half-based heuristic substituted (§4) |
| Regime-switching ≥10-transition floor | A (as a documented small-sample warning) | **C for India-only fits on the 7–11y credit cycle** (fewer than 10 transitions observed domestically per CONTRACT/Workstream 03/08's own counts) | Must use continuous quantile-rank state, not fitted Markov-switching, until pooled evidence (below) changes this |
| JST partial pooling for India credit-cycle parameters | A (meta-analysis/hierarchical shrinkage is standard, ≥30 country-year observations in the JST panel) | **B** (India's own n<4, ≥10 cross-country analogues — meets CONTRACT's explicit Tier-B definition) | ~17–18 countries × ~150 years in JST gives ample pooled power; India's own weight in the shrinkage stays small until more domestic cycles complete |
| DM / Jobson-Korkie-Memmel paired tests | A (method); small-sample correction A | **B** given realistic paired-evaluation T for Stage-1-vs-Stage-2 | Always apply the Harvey-Leybourne-Newbold correction (F16); do not assume asymptotic validity |

---

## 6. Research method for the data phase

**Phase 0 — Data & fixture gate.** Every free-source series (bhavcopy, RBI DBIE, AMFI, CCIL, World
Gold Council, etc.) is pulled once on the principal's machine, checksummed, and committed as a
fixture (per Known Prior #11); every later estimate must be reproducible against that pinned
vintage with no live network call. Point-in-time integrity is checked explicitly (Known Prior #7:
restated fundamentals bias backtests 150–450bps/yr upward) — a price-only version of every fixture
is built alongside any fundamentals-based one, and the fundamentals result is never reported
without its price-only counterpart (CONTRACT §8 trap).

**Phase 1 — Signal/state-variable discovery gate (per candidate).** Before any fitting: (a) a
pre-registration entry is filed (template below); (b) a written decay-survival argument is on file
(CONTRACT §5's four acceptable answers, or an explicit numeric haircut); (c) the clock test is
applied — ≥4 complete observed periods to claim "cycle" status, else it is a state variable ordered
by `tau_half`; (d) `tau_half` itself is estimated via bias-corrected AR(1) on overlapping windows
(Kendall/Marriott-Pope first-order correction, or Andrews/Hansen exact correction near the unit
root) with Newey-West/Hansen-Hodrick-consistent standard errors reported alongside the point
estimate; (e) any trend/cycle decomposition uses the Hamilton filter at the frequency-band-specific
h/p from §4, never HP.

**Phase 2 — Out-of-sample validation gate.** Purged + embargoed walk-forward CV (embargo ≥ 1×
`tau_half`, 4–6 folds for India-only monthly series); OOS R² computed against the expanding-window
historical mean (Goyal-Welch convention) and reported even when negative; Campbell-Thompson sign
restrictions applied and reported both with and without; the signal is also tested inside the
equal-weight combination benchmark (Rapach-Strauss-Zhou) to check it adds value jointly, not just
alone.

**Phase 3 — Statistical significance gate.** t-statistic and Deflated Sharpe Ratio computed with
the program's **cumulative, honestly-counted trial ledger** (a single running total maintained
across every workstream's sweeps, never reset); promotion to Tier A requires **both** t>3 and
DSR>0; Minimum Track Record Length is computed and compared against elapsed OOS/paper-trading
history before any capital-scale-up milestone; block-bootstrap (stationary bootstrap, block length
per §4) is run on the resulting portfolio's drawdown distribution, and the mandate's 30–35% ceiling
is checked against the bootstrap distribution's upper tail (95th/99th percentile), not just the
point-estimate historical max drawdown.

**Phase 4 — Regime/nonlinearity gate (only where a design proposes regime-conditional
parameters).** Count observed transitions; below 10, the design must fall back to a continuous
quantile-rank or sign rule (no fitted Markov-switching); where the count is India-only and thin
(<4 independent observations, ≥10 cross-country analogues), the JST partial-pooling recipe (§4) is
mandatory before any number is frozen, and the resulting parameter is marked Tier B, frozen at
inception, per CONTRACT §4.

**Phase 5 — Stage-1 completeness gate.** Stage 1 is run alone (no Stage-2 input) across the full
walk-forward history and must emit a complete, mandate-compliant portfolio at every rebalance date
— every hard constraint (leverage ≤1.5x, debt ≤70%, gold ≤50%, name entry/drift caps, options
notional caps, turnover caps) checked to bind without Stage-2 intervention, operationalizing the
architecture's "self-sufficiency is load-bearing" requirement.

**Phase 6 — Stage-2 incremental-value gate.** Paired evaluation of Stage-1-only vs Stage-1+Stage-2,
period by period, on net IR and episode-conditional drawdown (Open Question #7's default metric
pair); Diebold-Mariano test with the Harvey-Leybourne-Newbold small-sample correction as the
primary test, Jobson-Korkie-Memmel Sharpe-difference test as a secondary confirmatory test; every
discrete Stage-2 override scored on the Brier scale and logged to the override ledger; Stage-2
remains switched on only while it clears its pre-registered minimum effect at its pre-registered
significance — failing that, it reverts to advisory-only or is switched off entirely, per the
architecture's explicit "switchable off at any time."

**Phase 7 — Sweep/overfitting gate.** Before any parameter sweep (hedge ratio × regime grid,
factor-weight grid, or any future grid) is allowed to inform a frozen config value, its full grid
size enters the cumulative trial ledger (§4's worked example); the Probability of Backtest
Overfitting (CSCV, Bailey-Borwein-López de Prado-Zhu) is computed across the grid before any single
cell is selected; a result that only clears its significance bar because the ledger under-counted
prior sweeps is void and must be recomputed against the corrected N.

**Phase 8 — Registry/CI gate (CONTRACT §10).** Every parameter that survives Phases 1–7 lands in
the versioned `config/` registry with full provenance (paper/panel/argument, tier, confidence,
decay assumption); CI validates evidence-tier caps, Tier-C reduce-only, per-bucket budget
containment, 3σ aggregation inside mandate caps, turnover caps, and DAG acyclicity; a registry
violating its own stated budget fails to load, by construction.

**Phase 9 — Live/paper monitoring gate (post-launch, ongoing).** Realized OOS metrics tracked
against each pre-registered minimum effect on a rolling basis; a pre-specified stop rule (not a
silent re-tune) triggers review if a live signal underperforms its pre-registered floor for a
pre-specified number of consecutive periods; `tau_half` and transition counts are re-estimated as
more data accrues, with an explicit promotion path from Tier B to Tier A once the observation count
crosses CONTRACT's 30-independent-observation threshold — and, symmetrically, a demotion path back
to Tier B/C if a previously Tier-A effect's rolling significance decays (operationalizing McLean-
Pontiff's own finding that this is the normal fate of a real, once-significant anomaly).

**Pre-registration template (fields, per Harvey 2017/F11 and CONTRACT §9):**

1. **Hypothesis** — stated directionally, with the decay-survival mechanism (CONTRACT §5 (i)–(iv))
   named explicitly; "it backtests well" is not an admissible hypothesis statement.
2. **Sample** — exact date range, universe (which book/rank band), frequency, and named free data
   source(s) and fixture version, fixed before any result is examined.
3. **Metric** — primary (e.g., net IR, OOS R², episode-conditional drawdown) and any secondary
   metrics, named before running.
4. **Minimum economically meaningful effect** — a threshold sourced from the program's own cost
   stack (e.g., Workstream 05's ~3.3pp/yr incremental hurdle for high-turnover signals), never a
   round number chosen for convenience.
5. **Stop rule** — the fixed sample/test window is run once; if the pre-registered minimum effect
   is not cleared at the pre-registered significance (t>3 and DSR>0, or the relevant paired test),
   the hypothesis is marked REJECTED in the registry and is never re-tested with tweaked
   parameters — only a genuinely new mechanism argument may reopen the question, as a new registry
   entry carrying its own trial count.
6. **Decision rule** — the exact statistical test and threshold that will be used to accept/reject,
   named before the test is run.

---

## 7. Open questions and [VERIFY] items

- **[VERIFY]** Hamilton (2018)'s own explicit monthly-frequency h/p recommendation (F2) — this
  dossier's h=24/p=12 is a practitioner scaling convention, not confirmed as the paper's own stated
  number.
- **[VERIFY]** Exact deflated Sharpe Ratio formula constants (F8, §4 worked example) — structure
  recalled with moderate confidence, exact symbols/constants need pinning against the source paper.
- **[VERIFY]** Bailey & López de Prado (2012) exact venue/volume/pages for Minimum Track Record
  Length (F9).
- **[VERIFY]** Politis & White (2004)/Patton-Politis-White (2009) exact pages (F13).
- **[VERIFY]** Kendall (1954) and Marriott & Pope (1954) exact titles/pages (F14).
- **[VERIFY]** Hansen (1999) grid bootstrap exact venue/pages (F14).
- **[VERIFY]** Harvey, Leybourne & Newbold (1997) exact pages (F16).
- **[VERIFY]** Memmel (2003) exact venue/pages — an obscure citation for what is now a standard
  formula; verify the formula itself directly against a secondary source if the primary is
  unreachable (F17).
- **[VERIFY]** Psaradakis & Sola (1998) exact title/journal/pages (F18) — the paper is recalled
  with only moderate confidence and should be either confirmed or replaced with a more precisely
  recalled small-sample Markov-switching reference before this citation is relied upon in a
  document leaving this research phase.
- **[VERIFY]** Jordà, Schularick & Taylor (2013, 2017) exact volume/pages (F19).
- **[VERIFY]** Amihud & Hurvich (2004) exact pages (F3).
- **[VERIFY]** Ang & Timmermann (2012) exact venue/pages (F18).
- **[VERIFY]** Mertens (2002) citation underlying the skew/kurtosis-adjusted Sharpe ratio variance
  used inside DSR (F8) — recalled as existing but not confirmed by author/year with confidence.
- **Open methodological question for the principal**: whether the cumulative trial ledger (§4, §6
  Phase 7) should be a single program-wide count across all workstreams' sweeps from day one, or
  whether distinct sweep *families* (e.g., hedge-ratio/regime grids vs factor-weight grids) may be
  ledgered separately on the argument that they test economically distinct hypotheses. This
  dossier's default (single cumulative ledger, conservative) should be treated as the working
  assumption per CONTRACT §11 until the principal rules otherwise.
- **Open question**: exact value of R (regime-grid cardinality) and F (factor-weight grid
  cardinality) feeding the deflated-Sharpe trial count worked example in §4 — these are owned by
  Workstreams 02 and 04 respectively and were not re-derived here; this dossier's N formula is
  structural (N = 7×R×F) and must be populated once those workstreams' grids are finalized.
- **Open question**: whether India's own credit-cycle transition count (feeding the ≥10-transition
  floor, §4/§5) should be counted purely domestically or whether a transition observed in a
  sufficiently similar emerging-market analogue inside the JST-adjacent panel may contribute to the
  *pooled* count even though the India-specific transition matrix still needs its own 10 — this
  dossier takes the conservative reading (India-specific matrix needs its own 10, unaffected by
  pooling) and flags the alternative as an open design choice.
