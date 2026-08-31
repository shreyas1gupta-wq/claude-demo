# Workstream 11 — Optimizer, Name Count, Bands, Sizing (Stage 3: Equity Cross-Section)

Status: RESEARCH ONLY, per `CONTRACT.md` and `OPEN_QUESTIONS.md` (defaults assumed throughout).
Scope: Stage 3 optimizes ONLY the equity cross-section (asset mix is policy, per Contract
Architecture §2 and Workstream 06's policy-portfolio finding). This dossier derives the optimizer
form, a name-count formula per book (as a function of equity weight and cross-sectional
dispersion), signal-half-life-conditioned no-trade band widths, and position-sizing rules
(justifying/amending the frozen 5–6% entry / 10% drift / 20% in-progress caps), all from the
named literature plus first-principles arithmetic cross-referencing Workstream 05's cost/capacity
stack.

**Session constraint, stated up front.** This session's shared `WebSearch` budget (200/200) was
already exhausted before this workstream began, and `WebFetch` returns `EGRESS_BLOCKED` for every
domain tested (Wikipedia confirmed this session), consistent with Workstreams 05/08/09's identical
finding. Every citation below is drawn from trained knowledge, not live verification this session,
and tagged **(recalled, high/moderate confidence)** or **[VERIFY: …]** per the citation-discipline
rule. Nothing here is fabricated; where I am not confident of an exact volume/page/date I say so
explicitly rather than inventing precision. Several of the papers below (DeMiguel-Garlappi-Uppal,
Grinold-Kahn, Garleanu-Pedersen, Cremers-Petajisto, Bessembinder) are among the most-cited works in
their subfields and I hold high confidence on author/venue/year for all of them; the softer edges
are exact page numbers, a few secondary/extension citations, and one practitioner (non-peer-reviewed)
source.

---

## 1. Findings and literature

**F1. DeMiguel, Garlappi & Uppal (2009), "Optimal Versus Naive Diversification: How Inefficient Is
the 1/N Portfolio Strategy?," *Review of Financial Studies* 22(5), 1915–1953 (recalled, high
confidence).** Evaluates 14 mean-variance-family optimizers (including Bayesian shrinkage
approaches in the spirit of Ledoit-Wolf, Black-Litterman-style Bayesian combinations, and several
constrained variants) against naive 1/N across 7 empirical datasets, out-of-sample. **Headline
result: no sophisticated optimizer robustly and reliably beats 1/N out-of-sample on Sharpe ratio,
certainty-equivalent return, or turnover**, because estimation error in expected returns (μ) — far
more than in the covariance matrix (Σ) — swamps the theoretical gains from optimizing over
Markowitz's mean-variance frontier. The paper computes the estimation-window length a mean-variance
optimizer would need before it reliably beats 1/N for a portfolio of N assets; for a 25-50 asset
universe this comes out to **several hundred to several thousand months of stationary data**
— multiple decades to centuries — far beyond any realistic estimation sample. **[VERIFY: exact
window-length figures per N — recalled with moderate confidence on order of magnitude, high
confidence on the qualitative "far longer than any usable sample" conclusion].** This is the single
most load-bearing citation for Stage 3's optimizer-form decision (§4a).

**F2. Ledoit & Wolf (2003, 2004), shrinkage covariance estimation.** Ledoit, O. & Wolf, M. (2003),
"Improved Estimation of the Covariance Matrix of Stock Returns with an Application to Portfolio
Selection," *Journal of Empirical Finance* 10(5), 603–621; Ledoit & Wolf (2004), "Honey, I Shrunk
the Sample Covariance Matrix," *Journal of Portfolio Management* 30(4), 110–119 (recalled, high
confidence on both). Proposes shrinking the noisy sample covariance matrix toward a
lower-dimensional, low-estimation-error target (e.g., a constant-correlation or single-factor
structure), with the optimal shrinkage intensity derived analytically to minimize expected
Frobenius-norm loss. **Later refinement: Ledoit & Wolf (2012, 2017), "nonlinear shrinkage"** applies
asset-specific rather than uniform shrinkage to each eigenvalue of the sample covariance matrix
**[VERIFY: exact venues — recalled as appearing in *Annals of Statistics* and *Journal of Financial
Econometrics* across several papers, moderate confidence on precise placement]**. Ledoit-Wolf
shrinkage was itself one of the "sophisticated" methods DeMiguel et al. (F1) benchmarked and found
did not robustly beat 1/N **when it was still paired with historically-estimated expected
returns** — the distinction that matters for §4a is that L-W shrinkage is a genuinely strong,
low-estimation-error **risk-model** input; its failure in DGU is a failure of the *return* side of
mean-variance, not the covariance side.

**F3. Best & Grauer (1991), "On the Sensitivity of Mean-Variance-Efficient Portfolios to Changes in
Asset Means," *Review of Financial Studies* 4(2), 315–342 (recalled, high confidence); Michaud
(1989), "The Markowitz Optimization Enigma: Is Optimized Optimal?," *Financial Analysts Journal*
45(1), 31–42 (recalled, high confidence).** Best-Grauer show mean-variance-optimal weights are
extremely, discontinuously sensitive to small perturbations in the expected-return input vector —
literally an "error maximizer": the optimizer routes the largest weights to precisely the assets
whose expected return is *most* mis-estimated, since it cannot distinguish genuine edge from noise.
Michaud coins this "estimation-error maximization" and proposes resampled efficiency (bootstrap the
efficient frontier and average) as a partial fix. Together these are the mechanism-level
explanation for why F1's empirical finding holds.

**F4. Jagannathan & Ma (2003), "Risk Reduction in Large Portfolios: Why Imposing the Wrong
Constraints Helps," *Journal of Finance* 58(4), 1651–1684 (recalled, high confidence).** Shows that
imposing a no-short-sale constraint on minimum-variance portfolio optimization **improves**
out-of-sample performance even when the unconstrained solution "truly" wants to short some assets,
because the constraint acts as an implicit shrinkage on the noisy estimated covariance matrix.
Directly validates, from an independent angle, that the mandate's own long-only-cash-equities
design (Open Q#2 default) is not merely a simplification but likely *improves* the achievable risk
model versus an unconstrained alternative.

**F5. DeMiguel, Garlappi, Nogales & Uppal (2009), "A Generalized Approach to Portfolio
Optimization: Improving Performance by Constraining Portfolio Norms," *Management Science* 55(5),
798–812 (recalled, moderate-high confidence).** The constructive follow-up to F1: shows that
constraining the norm of the portfolio-weight vector (equivalent to a gross-exposure/leverage cap,
and shown to nest several shrinkage estimators as special cases) **does** improve mean-variance
optimization's out-of-sample performance relative to the unconstrained version studied in F1. This
is the direct evidence that the mandate's own hard caps (5–6% entry, 10% drift, 1.5x gross leverage)
are not merely risk-control conveniences but are independently supported as a *performance*
mechanism — they are a norm constraint of exactly the kind F5 shows helps.

**F6. Black & Litterman (1992), "Global Portfolio Optimization," *Financial Analysts Journal*
48(5), 28–43 (recalled, high confidence).** Combines a market-equilibrium (reverse-optimized CAPM)
prior with sparse, uncertain investor "views" in a Bayesian framework, producing more stable,
intuitive portfolio weights than feeding raw historical means into a mean-variance optimizer.
Designed for, and almost exclusively used in practice for, **asset-allocation problems with a
handful of assets/asset classes** where a defensible equilibrium prior exists (e.g., global
sovereign bond/equity/currency allocation) — not for a several-hundred-name equity cross-section,
where a single-stock CAPM equilibrium prior is itself weak (beta explains little of the
cross-section) and specifying "views" per name re-imports estimation error at scale.

**F7. Brandt, Santa-Clara & Valkanov (2009), "Parametric Portfolio Policies: Exploiting
Characteristics in the Cross-Section of Equity Returns," *Review of Financial Studies* 22(9),
3411–3447 (recalled, high confidence).** Proposes modeling portfolio weight directly as a function
of a stock's own characteristics — `w_i = w_benchmark,i + (1/N)·θ'·x_i` for normalized
characteristics x_i (e.g., value, momentum, size percentile ranks) — and choosing the coefficient
vector θ by maximizing realized investor utility directly, **without ever estimating an expected-
return vector or inverting a covariance matrix for the return-forecasting step**. This sidesteps
DeMiguel et al.'s (F1) core problem entirely: there is no μ vector to mis-estimate, because
portfolio choice and return forecasting are fused into one step, characteristic to weight. This is
the literature's name for "characteristic portfolios," the fourth optimizer option the workstream
brief names explicitly, and is the primary building block for §4a's recommended Stage-3 form.

**F8. Grinold (1989), "The Fundamental Law of Active Management," *Journal of Portfolio Management*
15(3), 30–37; Grinold & Kahn, *Active Portfolio Management* (McGraw-Hill, 1st ed. 1995, 2nd ed.
2000) (recalled, high confidence on both).** `IR ≈ IC × √BR`: the achievable Information Ratio
scales with the Information Coefficient (correlation between forecast and realized outcome) times
the square root of Breadth (the number of independent bets placed per year). The square-root
scaling is the mechanical reason breadth has *diminishing* marginal value — doubling the number of
independent bets only raises achievable IR by a factor of √2, not 2. Grinold-Kahn's own book
benchmarks a "good" institutional-quant IC at roughly **0.05**, with 0.10 described as very good
**[VERIFY: exact benchmark figures — recalled with moderate confidence, a widely repeated
practitioner heuristic from this book]**.

**F9. Clarke, de Silva & Thorley (2002), "Portfolio Constraints and the Fundamental Law of Active
Management," *Financial Analysts Journal* 58(5), 48–66 (recalled, high confidence).** Extends the
Fundamental Law with the **Transfer Coefficient (TC)**: the correlation between a manager's
theoretically optimal *unconstrained* active weights and the actual, *constrained* active weights
the mandate permits. Refined law: `IR ≈ TC × IC × √BR`. Position caps, long-only constraints,
sector limits, and drift bands all push TC below 1, degrading realized IR relative to the
theoretical maximum — the exact mechanism through which Stage 3's own hard caps (5–6%/10%/20%)
have a **measurable, quantifiable cost** in IR terms, not merely a qualitative one.
**[VERIFY: follow-on breadth-correlation-adjustment literature — I recall Buckle (2004), "How to
Calculate Breadth: An Evolution of the Fundamental Law of Active Portfolio Management," *Journal of
Asset Management* 4, 393–405, and a Qian & Hua treatment of "strategy risk"/correlated bets, both
with only moderate confidence on exact citation — the substantive point, that naive BR=N×(bets/yr)
overstates true breadth when bets are cross-sectionally correlated (e.g., many quant managers
running similar signals), is well established regardless of the exact secondary citation].**

**F10. Evans & Archer (1968), "Diversification and the Reduction of Dispersion: An Empirical
Analysis," *Journal of Finance* 23(5), 761–767 (recalled, high confidence).** Classic result:
portfolio variance from randomly selected stocks falls steeply from N=1 to roughly N=10–15, with
sharply diminishing marginal reduction beyond that — the origin of the "10–20 stocks is enough"
folk number for naive diversification.

**F11. Statman (1987), "How Many Stocks Make a Diversified Portfolio?," *Journal of Financial and
Quantitative Analysis* 22(3), 353–363 (recalled, high confidence).** Re-examines Evans-Archer with
transaction costs included in the calculus (the marginal cost of adding another position against
the marginal diversification benefit) and concludes a well-diversified, borrowing-investor portfolio
needs **at least 30–40 stocks**, materially more than the earlier "10–15" folk number, once costs
are honestly counted. **Campbell, Lettau, Malkiel & Xu (2001), "Have Individual Stocks Become More
Volatile?," *Journal of Finance* 56(1), 1–43 (recalled, high confidence)**, documents that
firm-level idiosyncratic volatility has *risen* over recent decades relative to market volatility,
implying the Evans-Archer/Statman diversification-floor N should be read as a **rising**, not fixed,
number over time — the Statman-era 30–40 is itself likely conservative for a book with meaningful
exposure to India's more volatile small/microcap tail.

**F12. Bessembinder (2018), "Do Stocks Outperform Treasury Bills?," *Journal of Financial
Economics* 129(3), 440–457 (recalled, high confidence).** Since 1926, only about the top **4% of
listed US common stocks account for the entire net wealth creation** of the US stock market above
Treasury bills; more than half of all listed stocks *underperform* T-bills over their full
lifetimes. Return distributions are extremely positively skewed: a strategy that concentrates too
narrowly risks structurally missing the rare, ex-ante-unidentifiable compounders that generate
essentially all of the market's excess wealth creation. **Bessembinder, Chen, Choi & Wei extend this
globally** (I recall a paper along the lines of "Do Global Stocks Outperform US Treasury Bills?" /
"Long-Run Shareholder Returns," published c. 2019–2023) **[VERIFY: exact title/venue/year]**,
finding the concentration of global wealth creation in a small fraction of firms is similar to, or
more extreme than, the US result. This is the direct counterweight to the concentration arguments
below — the "cost of missing winners."

**F13. Cohen, Polk & Silli, "Best Ideas," working paper (first circulated c. 2005, revised through
the 2010s) **[VERIFY: current publication status/venue — recalled as a long-circulating NBER/SSRN
working paper; I am not confident it was ever placed in a top journal under this exact title,
moderate confidence only].** Finds that a fund manager's single largest active over/underweight
position — the "best idea" — significantly and persistently outperforms both the market and the
rest of the manager's own portfolio, by several percentage points per year gross
**[VERIFY: exact magnitude]**, evidence that managers possess genuine stock-selection skill that is
*diluted* by over-diversification (attributed to benchmark-hugging/career-risk incentives, not lack
of skill). Directly supports the case for genuine concentration where conviction is real.

**F14. Cremers & Petajisto (2009), "How Active Is Your Fund Manager? A New Measure That Predicts
Performance," *Review of Financial Studies* 22(9), 3329–3365 (recalled, high confidence).** Defines
**Active Share** (the fraction of holdings that differ from the benchmark) and shows funds with
high Active Share combined with high tracking error ("Concentrated Stock Pickers") significantly
outperform their benchmarks net of fees, while low-Active-Share, low-tracking-error funds ("Closet
Indexers") underperform net of fees. **Petajisto (2013), "Active Share and Mutual Fund
Performance," *Financial Analysts Journal* 69(4), 73–93** (recalled, moderate-high confidence)
extends the dataset and finds Concentrated Stock Pickers the best-performing category over the full
sample. Together with F13, this is the strongest evidence base for deliberate concentration in the
aggressive book specifically.

**F15. Garleanu & Pedersen (2013), "Dynamic Trading with Predictable Returns and Transaction
Costs," *Journal of Finance* 68(6), 2309–2340 (recalled, high confidence) — THE key reference for
§4c.** With quadratic transaction costs and a mean-reverting (AR(1)) alpha signal, the optimal
policy is **not** to trade all the way to the frictionless (Markowitz) target each period, nor to
never trade, but to trade a *fraction* of the way toward a moving "aim portfolio" each period — the
aim portfolio being a weighted average of today's signal-implied optimal portfolio and the signal's
*expected future* optimal portfolios, discounted by how fast the signal itself decays. The optimal
trading speed is governed by the ratio of the transaction-cost parameter to risk-aversion, **and by
the signal's own mean-reversion/decay rate**: a slowly-decaying (long half-life) signal's aim
portfolio barely moves from one period to the next, so it is efficient to trade toward it *slowly*
(a wide effective no-trade region costs little, since the target is barely moving); a fast-decaying
signal's aim portfolio moves quickly, so failing to trade promptly forfeits most of the transient
alpha before it decays (a narrower effective no-trade region is efficient, cost permitting). This is
the direct mechanism this dossier uses to derive the band-width-per-half-life mapping (§4c) and
independently reproduces, from first principles, Contract item 10's already-stated qualitative
finding ("value/quality run ~5× momentum's half-life, so cost ~1/5 the turnover per unit of
authority") — a useful cross-check that GP logic and the prior pass's data-derived finding agree.

**F16. Constantinides (1986), "Capital Market Equilibrium with Transaction Costs," *Journal of
Political Economy* 94(4), 842–862 (recalled, high confidence).** Establishes, in a continuous-time
proportional-transaction-cost model, that the width of the optimal no-trade region around a target
portfolio weight scales as the **cube root** of the proportional transaction cost — a famous,
highly favorable scaling: even a fairly large increase in trading costs only modestly widens the
optimal no-trade band, because the cost elasticity of the band is just 1/3. Combined with F15/F17,
this gives the cost-side half of the band-width mapping proposed in §4c.

**F17. Davis & Norman (1990), "Portfolio Selection with Transaction Costs," *Mathematics of
Operations Research* 15(4), 676–713 (recalled, high confidence).** The canonical continuous-time
derivation (via free-boundary/HJB methods) of the "no-trade region" itself: with proportional
costs, it is optimal to hold a position and do nothing while it sits inside a wedge around the
frictionless Merton-optimal weight, and to trade only enough to reach the *boundary* of the wedge
(not all the way back to the target) once the position drifts outside it — the origin of the
"partial trade back to the band edge, not a full snap to target" logic this dossier applies to the
drift-cap mechanics (§4c/§4d).

**F18. MacLean, Thorp & Ziemba (eds.), *The Kelly Capital Growth Investment Criterion: Theory and
Practice* (World Scientific, 2011) (recalled, high confidence as a compiled reference volume);
MacLean, Ziemba & Blazenko (1992), "Growth Versus Security in Dynamic Investment Analysis,"
*Management Science* 38(11), 1562–1585 (recalled, moderate-high confidence).** Full Kelly sizing
(`f* = μ/σ²` for an approximately log-normal single bet) maximizes long-run geometric growth but at
the cost of extreme path variance and drawdown risk (folklore-level result in this literature: full
Kelly commonly carries on the order of a 50% probability of at least a 50% peak-to-trough drawdown
over a long horizon under realistic parameter uncertainty). **Fractional Kelly** — betting a
fraction f of the full-Kelly size — trades this off favorably: for the standard quadratic-in-leverage
growth-rate approximation `G(k) = μk − ½σ²k²` (maximized at k*=μ/σ²), the growth rate achieved at
`k=f·k*` is `G(f·k*)/G(k*) = f(2−f)` **(derived here directly from the growth-rate function; I
present this as a self-verifying identity, attributed to the general Kelly-fraction literature this
volume represents, rather than claiming a specific page citation)**. At f=0.5 (half-Kelly): 75% of
maximum growth at (since variance of leveraged log-wealth growth scales as f²) 25% of full-Kelly's
variance. At f=0.25 (quarter-Kelly): ~44% of maximum growth at 1/16th the variance. This quadratic
asymmetry is *why* practitioner convention almost never runs full Kelly, and why running well below
half-Kelly still retains a meaningful fraction of achievable growth (§4d).

**F19. Grossman & Zhou (1993), "Optimal Investment Strategies for Controlling Drawdowns,"
*Mathematical Finance* 3(3), 241–276 (recalled, high confidence); companion: Cvitanić & Karatzas
(1995), "On Portfolio Optimization Under Drawdown Constraints," in *Mathematical Finance* (IMA
volume) (recalled, moderate-high confidence) [VERIFY: exact venue/pages for Cvitanić-Karatzas].**
Derives, in continuous time, the optimal portfolio for an investor subject to a hard drawdown
constraint (wealth must never fall below a fixed fraction of its running maximum): the solution is
**state-contingent** — risky exposure must be scaled down mechanically as wealth approaches the
drawdown floor, in proportion to the remaining "cushion" (current wealth minus floor, relative to
current wealth) — structurally identical to Constant Proportion Portfolio Insurance (CPPI). This is
the formal justification for treating every sizing cap in this design (§4d) as a function of
*current drawdown relative to the mandate's ceiling*, not a static number, directly operationalizing
Contract item 4's already-adopted principle that "leverage must be state-contingent permission."

**F20. Gorman, Sapra & Weigand, "The Cross-Sectional Dispersion of Stock Returns, Alpha, and the
Information Ratio," *Journal of Investing* (c. 2010) **[VERIFY: exact volume/issue/pages — recalled
with moderate confidence on the paper's existence, authorship, and thesis; lower confidence on
exact bibliographic details].** Argues that the Information Ratio achievable by a given level of
stock-selection skill (fixed IC) itself scales with the cross-sectional dispersion of returns
available in the investable universe at a point in time: when dispersion is high, a given IC
translates into more realizable edge per bet (more differentiation between winners and losers to
exploit); when dispersion compresses (a highly correlated, "risk-on/risk-off" market), stock-picking
adds less value regardless of underlying skill, and broader diversification dominates concentration.
This is the direct mechanism this dossier uses to make name count a function of the dispersion
regime, not just of book/mandate (§4b).

**F21. Almgren & Chriss (2000/2001), "Optimal Execution of Portfolio Transactions" (recalled, high
confidence, canonical citation — see Workstream 05 F6 for full details, not re-derived here);
Almgren, Thum, Hauptmann & Li (2005), "Direct Estimation of Equity Market Impact" (see Workstream 05
F7).** Referenced here only for the staged-entry execution-schedule implication (§4e): the
mean-variance-efficient execution trajectory under linear temporary/permanent impact is smooth and
**front-loaded** (more aggressive early, tapering later), not the naive equal-tranche-per-day
schedule; this dossier proposes equal-tranching as the *starting* design (simpler, no execution
infrastructure yet) with an explicit note that an Almgren-Chriss-style front-loaded schedule is the
natural refinement once live execution data exists.

**F22. Hoffstein et al. (Newfound Research), "Rebalance Timing Luck" research (c. 2018–2019, a blog
/ practitioner research series, not peer-reviewed) [VERIFY: exact title(s), co-author list, and
publication dates — recalled with moderate confidence; Corey Hoffstein is the lead author I am
confident of].** Shows that the arbitrary choice of *which calendar date* a systematic strategy
rebalances on creates material dispersion in realized returns purely from timing luck, unrelated to
skill, and recommends **tranching/staggering** rebalance execution (and, separately, signal-
measurement dates) across multiple days rather than acting on one fixed date — the direct source
for this dossier's rebalance-tranching recommendation (§4e).

---

## 2. India-specific evidence

None of F1–F22 is an India study; per the Contract's "India first" instruction, this section states
what applying a purely cross-country literature means for Stage 3's specific numbers, and layers in
the genuinely India-specific institutional facts that change the answer (several already established
in Workstream 05, referenced rather than re-derived).

**The SAST 5% disclosure ceiling (Workstream 05, F13/§4g) is a hard, mechanical floor on name count
for the conservative book.** Any full 5–6% weight position requires the target's market cap to
exceed roughly ₹19,000–31,000cr across the conservative book's AUM range, which per Workstream 05's
independent arithmetic limits the full-conviction universe to roughly the top 50–80 names by rank.
Below that cap, positions must shrink in size — which, to deploy the same aggregate equity weight,
mechanically *requires more names*, independent of any alpha or diversification argument. This is
the single most important India-specific fact shaping the conservative book's name-count formula
(§4b): its N floor is driven by **capacity and disclosure law**, not diversification theory.

**Circuit limits, ASM/GSM, and derivative-ban periods (Workstream 05 §2) mean a stuck position
cannot always be resized on demand.** This has two consequences for this workstream specifically:
(i) the Garleanu-Pedersen no-trade-band logic (§4c) implicitly assumes continuous ability to trade
toward the band edge at will; a banded name can simply stop trading, converting a "wide but
tradeable" band into a forced hold at whatever level the last trade left it — the registry should
treat GP-derived band widths for ASM/GSM-flagged names as a lower bound on realized drift, not a
point estimate. (ii) A larger number of smaller positions in the illiquid tail (rank 500–750, the
aggressive book's satellite universe) reduces the NAV fraction stuck in any single band/circuit
event relative to concentrating the same aggregate tail exposure into fewer, larger positions — a
genuine risk-management argument for a higher N floor in the tail bucket, independent of and
additive to the diversification argument from F10/F11.

**Promoter concentration is a caveat on the Evans-Archer/Statman diversification math, which assumes
independent idiosyncratic risk.** India's NIFTY 500 median promoter holding is commonly cited in the
45–55% range (Workstream 05, flagged `[VERIFY]` there and here). Governance/related-party risk in
promoter-heavy companies is plausibly *correlated* across similarly-structured small/midcap names
(shared legal/regulatory environment, similar related-party-transaction incentives) in a way the
classic US-data-based diversification curves do not model — an argument for reading the
Evans-Archer/Statman floor (already a US-data, cross-country-prior, Tier-B-at-best number) as a
**lower bound** for India's small/microcap tail specifically, not a point estimate. No Indian study
was found or is verifiable this session quantifying this correlation directly — `[VERIFY: Indian
diversification-curve study, if one exists]` — this dossier's treatment is Tier C narrative on this
specific point.

**Retail/FII/DII flow structure plausibly raises idiosyncratic volatility in the small/microcap
tail beyond even the Campbell-Lettau-Malkiel-Xu (F11) trend.** India's retail participation is
concentrated disproportionately in small/midcap names (a widely observed, if not freshly cited this
session, feature of NSE cash-market volume composition); higher noise-trading intensity there is a
plausible amplifier of idiosyncratic volatility specifically in the aggressive book's rank 500–750
universe, reinforcing (directionally, not quantitatively) the case for a higher diversification
floor in that bucket than the US-literature numbers alone would suggest. Tier C, no direct citation.

**The F&O-eligible universe (~180–200 names, Workstream 05 F15) bounds where options-implied risk
data exists.** For the large majority of the NIFTY 750 universe (everything past roughly the top
150–200 names by liquidity), there is no listed options market to derive implied volatility or
implied correlation from — the risk model for Stage 3's covariance input must rely on **historical
realized covariance with Ledoit-Wolf-style shrinkage** (F2) for essentially the whole moderate and
conservative books' universes, not any options-market-implied alternative. This is independent
support (from data availability, not just DGU's estimation-error argument) for the shrinkage-
covariance recommendation in §4a.

**Sector concentration in Indian benchmark indices (financials, IT, energy historically dominant in
NIFTY weightings) interacts with the mandate's "fully active, no sector-neutrality requirement"
(Contract §3).** Because Stage 3's characteristic-based weight-tilting (§4a) operates name-by-name,
many correlated single-name tilts within a dominant sector can silently accumulate into a large
aggregate sector bet that no single hard cap catches. The mandate does not require sector
neutrality, and this dossier does not propose adding one — but the Ledoit-Wolf-shrunk covariance
matrix used for risk budgeting (§4a) is exactly the instrument that should *surface* this
concentration (as a risk-contribution report to Stage 2/human review), consistent with "fully
active" meaning not *forced* neutrality, not blindness to concentration.

**Statutory cost asymmetry (Workstream 05 §4a: cash delivery ≈22–32bps round trip vs. index futures
≈10–18bps) matters for the transaction-cost parameter Λ that the Garleanu-Pedersen mechanism (§4c)
uses to set trading speed.** Because Stage 3 trades the cash equity cross-section itself (leverage
and hedging are separate, index-futures-based sleeves per Open Q#3/#4, out of Stage 3's scope), the
relevant Λ for the equity book's own no-trade bands is the **cash-delivery, rank-bucket-specific**
cost curve from Workstream 05 §4b–4c, not the cheaper futures-overlay cost — a reminder that the
band-width formula (§4c) must be parameterized per rank bucket, exactly mirroring Workstream 05's
own finding that a single book-level cost scalar understates the tail's true friction.

---

## 3. Decay and crowding assessment

Most of this dossier's content is methodology (how to size, band, and count positions), not an
alpha signal — per Workstream 05/09's precedent, methodology does not itself decay, but each
*empirical claim* embedded in it must still clear the Contract's survival test.

- **DeMiguel-Garlappi-Uppal's estimation-error finding (F1).** Survival argument: **not an
  arbitrage-competed anomaly at all** — it is an estimation-theoretic fact (finite-sample noise in a
  mean vector swamps a theoretically-larger optimization gain) that cannot be arbitraged away by
  more capital entering the market, because it concerns the difficulty of *forecasting*, not a
  mispricing. No decay haircut needed; it does not get weaker as more managers learn about it
  (indeed, if anything, the opposite: more managers reaching for the same 1/N-adjacent, constraint-
  heavy heuristics because of this finding creates a mild crowding concern of its own — see below).

- **Diversification benefit (Evans-Archer/Statman, F10/F11).** Survival argument: **(iii) a
  mathematical/statistical fact about the variance of a sum of imperfectly correlated risks**, not a
  priced anomaly. Does not decay. The *numeric* floor (30–40, or higher per CLMX) is an empirical
  regularity tied to the level of idiosyncratic volatility in the market at a point in time, and
  should be periodically re-estimated (not frozen), but the underlying mechanism is permanent.

- **Concentration/Best-Ideas/Active-Share edge (Cohen-Polk-Silli F13, Cremers-Petajisto F14).**
  Survival argument: **(iv) institutional constraint, reinforced by (i) a structural/behavioural
  mechanism.** The documented edge is diluted specifically by *career-risk-driven closet indexing*
  at typical institutional managers (redemption risk, tracking-error mandates, quarterly performance
  review against a benchmark) — frictions a proprietary, permanent-capital book explicitly does not
  face. This gives a genuine, not-easily-arbitraged reason our book can run higher Active Share than
  the mutual-fund universe these papers studied: the edge isn't crowded away by other proprietary
  books adopting it (few exist with comparable mandates), and it cannot be competed away by
  benchmark-constrained institutions adopting it, because their own mandates structurally prevent
  them from doing so. **Caveat/decay channel worth naming explicitly**: this argument weakens if a
  large share of proprietary/family-office capital *also* moves toward concentrated, high-Active-
  Share strategies — plausible over a multi-year horizon as the "closet indexing" critique becomes
  more widely acted on; no numeric haircut proposed given no direct evidence of this happening at
  pace in India, but flagged as a five-year-horizon watch item.

- **Skewness/missing-winners caution (Bessembinder F12).** This is not itself an edge to size but a
  **constraint on how far concentration can go** — a structural, non-decaying statistical fact about
  the shape of the return distribution (persistent positive skewness in equity returns, essentially
  unchanged across the 1926–2016 US sample and, per the global extension, elsewhere too). Functions
  here as a floor under the aggressive book's minimum name count (§4b), not as a signal to size.

- **Grinold-Kahn Fundamental Law / Transfer Coefficient (F8/F9).** A **mechanical identity under
  stated assumptions** (approximate independence of bets), not an empirical claim subject to
  arbitrage — does not decay on its own terms. Its assumption *can* be eroded by crowding, however:
  **as more quant managers run correlated signals on the same cross-section, the effective breadth
  the Fundamental Law promises shrinks even though each individual forecast still looks
  "independent" in isolation**, because bets become correlated across market participants (not just
  across names within one book). This is a genuine, named decay channel for the *breadth* input to
  IR — not a haircut on IC, but on the achievable BR — and is the reason this dossier treats
  Grinold-Kahn arithmetic as a sanity check on name count (§4b), never as the primary tool: it
  requires an assumed IC as input, and IC is exactly the quantity most exposed to the McLean-Pontiff
  overconfidence problem the whole Contract exists to guard against.

- **No-trade-band mechanics (Garleanu-Pedersen F15, Constantinides F16, Davis-Norman F17).**
  Survival argument: **(iv) institutional/structural constraint** — transaction costs are a real,
  structural market feature, not a mispricing; the *methodology* for trading efficiently around them
  does not decay. What can and does change is the specific cost parameters (Workstream 05 documents
  two statutory-cost hikes within under two years) and each signal's own `tau_half` (subject to the
  cycle-ladder's own re-estimation per Contract §9) — so the band-width *formula* (§4c) is durable,
  its plugged-in numeric anchors are not, and must be re-run whenever either input moves materially
  (mirroring Workstream 05's own re-run trigger for its cost-curve function).

- **Kelly-fraction sizing (MacLean-Thorp-Ziemba F18, Grossman-Zhou F19).** The sizing *formula* is a
  mathematical result, not an empirical claim — it does not decay. Its *output*, however, is only as
  good as the μ (expected edge) fed into it, and that μ is exactly the alpha estimate subject to
  every decay argument made in Workstreams 01/02/03 for the underlying signals. This dossier
  proposes explicitly feeding **decay-haircut** alpha (not raw backtested alpha) into the Kelly
  sizing formula (§4d) — making position sizing "decay-aware by construction": if a signal's alpha
  is later revised down (McLean-Pontiff-style), the Kelly-implied position size shrinks
  automatically without a separate policy change, a favorable, self-correcting property worth
  stating explicitly rather than leaving implicit.

- **Rebalance-timing-luck research (Hoffstein et al., F22).** Survival argument: **(iv) institutional
  constraint** — the "luck" arises mechanically from the arbitrary choice of one calendar date,
  which every systematic strategy must make; tranching removes it by construction and does not
  depend on any assumption that could be arbitraged away. Not peer-reviewed, so held to a slightly
  lower confidence tier than the academic citations above, but the underlying mechanism (variance
  reduction from averaging across execution dates) is essentially a law of large numbers, not an
  empirical claim that could fail to replicate.

---

## 4. Proposed parameters — the Stage-3 spec

### 4a. Optimizer form

**Recommendation: signal-blend-with-heuristic-caps, implemented as a characteristic/parametric
portfolio policy (Brandt-Santa-Clara-Valkanov, F7) for the return side, paired with a Ledoit-Wolf-
shrunk (F2) historical covariance matrix used *only* for risk budgeting (position/sector risk-
contribution reporting and marginal-risk-based position sizing), never for return forecasting.**

Reasoning, tied to the four named alternatives:

- **Classic mean-variance optimization (MVO) with historically-estimated expected returns: rejected
  as the core engine.** F1's finding is not a curiosity but a structural warning: with a several-
  hundred-name universe and a research history measured in years (not the centuries F1's own
  window-length calculation would require), any μ vector fed to a literal Markowitz optimizer will
  be dominated by noise, and F3 shows the optimizer will *concentrate* on exactly that noise. F5 and
  F4 both show the fix is not "a better optimizer" but norm/exposure constraints and long-only
  restrictions — i.e., exactly the mandate's own hard caps, independent of what return model sits
  underneath them.
- **Shrinkage MVO (Ledoit-Wolf): retained, but only on the covariance side.** L-W shrinkage is
  genuinely strong evidence-backed machinery (F2) and is independently supported by data
  availability in India specifically (§2: no options-implied alternative exists for ~550+ of the 750
  names). Its role in this design is risk budgeting — translating a raw rank/percentile signal
  score into a position size that respects a total active-risk budget and surfaces correlated
  (e.g., sector) concentration — not generating the μ vector DGU shows is the actual problem.
- **Black-Litterman: rejected as out of Stage 3's scope by the Contract's own architecture, not
  just on the merits.** BL's comparative advantage is combining a defensible equilibrium prior with
  a handful of asset-class-level views — precisely the asset-*allocation* problem the Contract
  Architecture (§2) and Workstream 06 already assign to policy, outside Stage 3. Inside the equity
  cross-section, a single-stock CAPM-equilibrium prior is weak, and specifying per-name "views" for
  several hundred names reintroduces estimation error at scale rather than avoiding it. BL's
  *conceptual* contribution — start from a neutral/benchmark prior, tilt by confidence-weighted
  views, shrink toward the prior when confidence is low — is worth keeping, but is better
  implemented via the characteristic-portfolio mapping below than via literal BL algebra.
- **Characteristic portfolios (Brandt-Santa-Clara-Valkanov): the recommended foundation.** Map each
  name's blended, quantile-ranked signal score (per Contract §6's "quantile ranks over point
  thresholds" preference) directly to an active weight via a smooth, monotone function — no μ
  vector, no covariance inversion on the return side. This is the practitioner-standard approach at
  quant-equity managers precisely because it structurally avoids F1's failure mode (documented
  practitioner convention, not a single citable source, offered per Contract §6's "documented
  practitioner experience" provenance category).

**Concrete form proposed**: `active_weight_i = clip(g(rank_percentile_i(signal_blend)) ×
risk_scale_i(Σ_LW), −0, +cap_i)`, where `g(·)` is a smooth, sign-preserving, saturating function of
the name's cross-sectional signal-percentile rank (never a hard-thresholded bucket, per the no-
magic-numbers rule), `risk_scale_i` adjusts the raw signal-driven weight down for names whose
marginal contribution to portfolio variance (via the Ledoit-Wolf-shrunk Σ) is unusually large
relative to their signal strength (catching correlated/sector-concentrated risk the signal itself is
blind to), and `cap_i` is the position's applicable hard ceiling from §4d.

### 4b. Name-count formula per book, as a function of equity weight and dispersion

Two forces set the bounds and one force (dispersion) sets where inside the bounds the book sits at
any time:

- **Diversification floor `N_floor(book)`** — from Evans-Archer/Statman (F10/F11), adjusted upward
  for India's higher small/microcap idiosyncratic volatility (CLMX direction, F11) and the promoter-
  correlation caveat (§2), and floored additionally by the Bessembinder skewness caution (F12) for
  the more concentrated books.
- **Capacity/conviction ceiling `N_ceiling(book, w_eq)` = `w_eq / avg_min_weight(book)`** — the
  maximum number of names supportable while keeping the *average* position large enough to reflect
  genuine differentiated conviction (Cohen-Polk-Silli, F13; Clarke-de Silva-Thorley's Transfer
  Coefficient, F9 — positions rounded down toward benchmark-neutral by extreme diversification
  contribute little to TC). `avg_min_weight` is itself lower for books where dossier-05 capacity
  arithmetic already forces small tickets (moderate/conservative tail) — this is a design choice,
  not a literature-derived constant, and is flagged Tier C accordingly.

| Book | `N_floor` | Basis | `avg_min_weight` (sets `N_ceiling` via `w_eq/avg_min_weight`) | Illustrative `N_ceiling` at full equity weight |
|---|---|---|---|---|
| Aggressive | 15–20 | Statman floor relaxed downward: concentration is the point (Active Share/Best-Ideas edge, F13/F14), but never below Evans-Archer's own ~10–15 raw floor, and never below the Bessembinder-motivated soft floor (~12–15) that limits the chance of structurally missing a skew winner | ~1.5–2% (own construct — smaller than the 5–6% cap to allow headroom for the aggressive satellite sleeve's smaller tickets, Workstream 05 §4f) | ~50–65 |
| Moderate | 30–50 | Statman floor (F11), pushed toward the upper half because the value/quality engine's long half-life (Contract item 10) needs *cross-sectional* breadth to compensate for *infrequent* independent re-forecasts per name (Grinold-Kahn arithmetic below) | ~1.0–1.5% | ~65–100 |
| Conservative | 50–80+ | Driven primarily by Workstream 05's SAST-disclosure/ADV capacity finding (full-size positions viable only to rank ~50–80), not by diversification theory alone — diversification math alone would ask for less | ~0.5–1.0% | ~150–250 (rarely binding; capacity, not this ceiling, is what actually limits deployment per Workstream 05) |

**Dispersion-conditioned position inside the bounds** (Gorman-Sapra-Weigand mechanism, F20):

`N*(book, w_eq, D) = N_floor(book) + [N_ceiling(book, w_eq) − N_floor(book)] × (1 − D)`

where `D ∈ [0,1]` is the trailing cross-sectional return-dispersion **percentile rank** within its
own multi-year history (a quantile rank, not a fixed threshold, per Contract §6) for the book's
investable universe. At high dispersion (D→1: wide spread between winners and losers), a given IC
buys more edge per bet, so the book concentrates toward `N_floor`. At low dispersion (D→0: a
compressed, correlated market where stock-picking has less to work with), the book spreads toward
`N_ceiling`, since concentrating adds unrewarded idiosyncratic risk without commensurate expected
payoff.

**The equity-weight dependence has a resolution built in for the low-`w_eq` edge case.** If a
defensive Stage-1/2 regime call pushes `w_eq` low enough that `w_eq / avg_min_weight(book) <
N_floor(book)`, the design should relax `avg_min_weight` downward for that period rather than force
`N` below the diversification floor — during genuinely defensive, low-equity-weight regimes the
book's overall risk stance is already conservative (the reduced equity weight *is* the primary
risk-reduction lever), so smaller average position sizes carry less alpha-dilution cost than they
would in a fully-invested regime. This is this dossier's own resolution of a genuine tension in the
brief's question, not drawn from any cited paper — Tier C, flagged as such.

**Grinold-Kahn sanity check, not primary derivation (F8/F9), with the caveat stated in §3**: for the
moderate book at N=40, with value/quality's long half-life implying roughly 1–2 independent
re-forecasts per name per year, BR≈40–80; at a "good" institutional IC of 0.04–0.05 (F8), IR ≈
0.04–0.05 × √60 ≈ **0.31–0.39** — a believable, not extreme, IR for a real factor strategy,
consistent with what is typically targeted in practice. For the aggressive book's momentum/reversal
sleeve at N=20 with 4–6 independent re-forecasts/year (short half-life), BR≈80–120, IR ≈ 0.04–0.05 ×
√100 ≈ **0.40–0.50** — again plausible. These numbers are illustrative cross-checks on the
diversification/capacity-derived N ranges above, not a separate derivation — Grinold-Kahn requires
an assumed IC as an input, and IC is precisely the quantity least defensible to assume in advance
(§3), so this dossier does not let it set N independently.

### 4c. No-trade bands, per signal half-life — the band-width-per-half-life mapping

Two multiplicative factors, both derived from named literature, neither a fixed number:

`drift_band_width(signal, rank_bucket) = drift_cap_ceiling × h(τ_half(signal)) ×
(cost(rank_bucket)/cost_ref)^(1/3)`

- **`drift_cap_ceiling` = the frozen 10% drift cap (Contract §3)**, treated as an *upper bound* the
  formula asymptotes toward, never exceeds — this dossier does not propose relaxing the frozen
  ceiling, only differentiating how close to it any given position is allowed to run before being
  trimmed.
- **`h(τ_half) = τ_half / (τ_half + τ_ref)`**, a saturating, monotone, quantile-like function of the
  signal's own half-life (Contract's `tau_half` ladder), derived from Garleanu-Pedersen's (F15)
  comparative static that trading speed toward the aim portfolio should fall (i.e., the efficient
  no-trade band should widen) as the signal's own decay rate falls (half-life rises). `τ_ref` is a
  calibration anchor, not a magic number in the forbidden sense — it should be set (data phase) so
  that `h` evaluated at the shortest surviving cycle/state-variable half-life in the ladder sits well
  below 1. Illustratively, at a 1–2 month reversal/short-momentum half-life, `h ≈ 0.15–0.3` (narrow
  effective band, ~1.5–3% before the cost adjustment); at a ~24–30 month value/quality half-life
  (Contract item 10's "~5×" framing applied to a plausible 5–6 month momentum half-life), `h → close
  to 1` (band close to the full 10% ceiling).
- **`(cost(rank_bucket)/cost_ref)^(1/3)`**, Constantinides' (F16) cube-root cost scaling, using
  Workstream 05's own rank-bucket round-trip cost curve (§4c there) rather than a single book-level
  number — an illiquid rank-500–750 tail position gets a wider band than a same-half-life liquid
  position, because its cost of premature trimming is materially higher, and the cube-root exponent
  means this adjustment is modest even for a large cost gap (consistent with Workstream 05's
  documented ~3–4× statutory cost gap between cash delivery and futures translating to only a
  ~1.3–1.6× band-width adjustment via the cube root).

**Reading the formula's central implication**: under this mapping, **fast-decaying signals
(reversal, short momentum) should be trimmed back toward target at a materially tighter drift than
the frozen 10% ceiling** — perhaps 2–4% before the cost adjustment — specifically because
Garleanu-Pedersen logic says their aim portfolio moves quickly and letting drift run to the full
10% before acting forfeits a large share of a fast-decaying edge; **slow-decaying signals
(value/quality) should be allowed to ride closer to the full 10% band** before a position is trimmed,
since GP logic says little is lost by trading toward a barely-moving target patiently. This is an
explicit, argued recommendation to **differentiate the drift band by signal type**, not apply one
flat number everywhere — while never proposing to raise the ceiling itself.

**When a position drifts outside its band, trim partially, not fully, toward the band edge**
(Davis-Norman, F17) — matching the tightest execution logic to exactly the rank buckets where
Workstream 05 shows patient/partial execution matters most (the illiquid tail), while allowing the
liquid core (where a full snap-back is economically cheap per Workstream 05's own cost curve) to
trade closer to fully back to target.

### 4d. Position-sizing rules

Every entry size is the **minimum** of three independently-derived caps:

1. **The frozen 5–6% mandate ceiling** (never relaxed upward here). Justified post-hoc: comparing a
   naive single-name full-Kelly calculation (`f*=μ/σ²`, e.g., an 8%/yr idiosyncratic-alpha edge over
   a ~35%/yr idiosyncratic vol typical of an Indian mid/small name gives `f* ≈ 0.08/0.1225 ≈ 65%`) to
   the frozen 5–6% cap shows the mandate is already running at roughly **1/10th to 1/15th of a
   naive single-bet full-Kelly fraction** — far more conservative than even a half-Kelly
   practitioner default. This is *appropriate*, not merely accidental conservatism, because (i) the
   Contract's 30–35% max-drawdown ceiling (§3) is a materially stricter constraint than the typical
   return-only-optimizing Kelly bettor faces, and per Grossman-Zhou (F19) a binding drawdown
   constraint mechanically implies running well below unconstrained-Kelly exposure; (ii) naive
   single-bet Kelly ignores estimation uncertainty in μ and σ, a well-known critique (Kelly sizing is
   highly sensitive to input error) that argues for even more fractional sizing than the parameter-
   certainty formula implies; and (iii) the F18 quadratic growth-fraction trade-off (`f(2−f)`) means
   the *growth given up* by sizing this conservatively is smaller than a linear intuition would
   suggest — a position at roughly 1/8-Kelly still captures a meaningful fraction of the achievable
   growth rate once portfolio-level diversification (not single-bet variance) is the true risk unit.
   **Conclusion: the frozen 5–6% cap is not contradicted by the fractional-Kelly-under-drawdown-
   constraint literature — it is comfortably consistent with it, arguably on the conservative side
   of what the literature alone would require, which is appropriate given the binding drawdown
   ceiling.** No amendment proposed to the ceiling itself.
2. **A decay-haircut Kelly-fraction size**: `f_Kelly × μ_haircut / σ_i²`, with `f_Kelly` proposed in
   the **0.15–0.35 range** (an explicit "eighth-to-third Kelly" convention — own construct, Tier C,
   more conservative than the classic half-Kelly practitioner norm specifically because of the
   mandate's unusually strict drawdown ceiling per (i) above) and `μ_haircut` = the signal's gross
   backtested alpha multiplied by its Contract §5 decay-survival haircut (McLean-Pontiff 26%/58%
   defaults, or a signal-specific numeric haircut from Workstreams 01–03, never the raw backtested
   figure). This makes sizing automatically shrink if a signal's alpha is later revised down (§3).
3. **A capacity-implied size** from Workstream 05's days-to-build arithmetic: **a position should
   never be sized such that its full-target build time exceeds its own signal's half-life** — e.g.,
   do not attempt to build a reversal-driven position (half-life ~1–2 months) to full target size if
   Workstream 05's participation-cap arithmetic implies a multi-month build in that name's rank
   bucket; instead cap the position at whatever size is buildable within roughly the signal's own
   half-life, letting the position simply be smaller for illiquid names carrying fast signals. This
   is this dossier's own synthesis of Workstream 05's capacity math with this workstream's signal-
   half-life framework — an original linkage, not itself from any cited paper, flagged Tier C on the
   specific numeric mapping (the *principle* — don't build slower than the signal decays — is Tier A
   arithmetic given the two inputs).

**The in-progress (staged-entry) 20% aggregate cap should be split into two separate budgets**,
rather than one shared pool: a **full-size-cohort budget** (positions still building toward a 5–6%
target, the frozen 20% ceiling retained here essentially unchanged, since Workstream 05 already
showed this allows only 3–4 simultaneous full-size builds, which is the correct binding constraint
for the deliberately concentrated aggressive/core sleeves) and a **small-ticket-cohort budget**
(the ~1–2% or smaller tail positions identified in Workstream 05 §4f and in the moderate/
conservative books' capacity-driven wide-N tail), which builds in days rather than weeks and should
not compete against the same 20% pool — doing so would otherwise artificially throttle exactly the
broad, small-ticket deployment Workstream 05 shows the conservative and moderate books structurally
need. This is a proposed registry refinement, not a Contract violation (the Contract sets one
number; this dossier recommends reading it as applying to the cohort it was clearly designed for —
full-size builds — while giving the small-ticket cohort its own, more generous ceiling).

**State-contingent cushion scaling on all three caps above** (Grossman-Zhou, F19): multiply every
sizing cap by `c(DD) = max(0, 1 − DD_current/DD_ceiling)^p`, with `p` left as a free exponent
(propose p=1, the simplest linear CPPI-style default, explicitly flagged as this dossier's own
construct, Tier C, no specific paper fixes `p` for this mandate) — so that as realized drawdown
approaches the 30–35% ceiling, entry sizing, drift tolerance, and in-progress budgets all shrink
smoothly toward zero, operationalizing Contract item 4's state-contingent-leverage principle at the
position level, not only the portfolio-leverage level where it is already applied.

### 4e. Staged-entry schedule and rebalance cadence

**Staged entry**: reference Workstream 05's days-to-build table (§4e there) directly — do not
re-derive the square-root-law impact math here. Propose an initial equal-tranche-per-day schedule up
to the participation-rate cap for each rank bucket (simplest, no execution infrastructure exists
yet), with an explicit note that Almgren-Chriss (F21) shows a front-loaded schedule is more
efficient once live execution data exists to calibrate impact-decay parameters — a Phase-2+ refinement,
not a Phase-1 requirement.

**Rebalance cadence and timing-luck tranching** (Hoffstein et al., F22): within whatever cadence a
sleeve runs (weekly to monthly, per Contract §3, cadence may differ per sleeve), **both the signal-
measurement date and the execution date should be staggered/tranched across the cadence window**
rather than acting on one fixed calendar date — e.g., for a monthly-cadence sleeve, measure signals
and execute in roughly weekly tranches across the month rather than snapshotting and trading on one
day. This diversifies away pure rebalance-timing luck (a source of return dispersion wholly
unrelated to skill) and, as a favorable side effect, is largely already provided by the staged-entry
build times documented in Workstream 05 for the illiquid tail (positions there are inherently built
over multiple weeks regardless) — the incremental design need is only for the **liquid core**, where
trades could otherwise be completed in a single session on one arbitrary date.

---

## 5. Evidence-tier recommendations

| Effect / parameter | Tier | Observation count / basis | Note |
|---|---|---|---|
| DeMiguel-Garlappi-Uppal 1/N-superiority finding | **A** (method) | 14 models × 7 datasets, replicated by a large following literature over 15+ years | Method's own tier is A; the specific window-length numbers are `[VERIFY]` |
| Ledoit-Wolf shrinkage (covariance side only) | **A** (method) | Standard, decades-replicated statistical technique | India-application: **A** (mechanical), no India-specific degradation |
| Jagannathan-Ma long-only-as-shrinkage | **A** (method) | Single well-replicated JF result | Directly supports Open Q#2's long-only default independent of this dossier |
| Brandt-Santa-Clara-Valkanov characteristic portfolios | **A** (method) | Widely cited, replicated approach; industry-standard practitioner convention | The specific coefficient/percentile-mapping function is a design choice, Tier C, to be fit in the data phase |
| Grinold-Kahn Fundamental Law / Clarke-de Silva-Thorley Transfer Coefficient | **A** (method, identity under stated assumptions) | Canonical, decades of practitioner use | Requires an assumed IC as input — that IC estimate itself is Tier B/C per signal (Workstreams 01–03) |
| Evans-Archer / Statman diversification floor | **A** (method, well-replicated); **B** for India-specific magnitude | Original studies + large replicating literature, but on US data | India small/microcap tail: Tier C narrative caveat (promoter correlation, retail flow) layered on top |
| Bessembinder skewness result | **A** (method); **B** for India-specific magnitude | Single comprehensive US study (1926–2016, full CRSP universe) plus a global extension `[VERIFY]` | No Indian replication found or verifiable this session |
| Cohen-Polk-Silli Best Ideas / Cremers-Petajisto Active Share | **B** | Single-country (US) mutual-fund-holdings studies; mechanism (career-risk dilution) is well-argued but the magnitude is US-fund-industry-specific | Proprietary-book applicability argued via survival mechanism (§3), not by direct evidence the effect transfers |
| Garleanu-Pedersen dynamic trading / Constantinides cube-root / Davis-Norman no-trade region | **A** (method) | Canonical theoretical results, internally consistent, cross-validated against Contract item 10's independent data-derived finding | The *numeric* half-life anchors (`τ_ref`, illustrative band widths) are Tier C/own-construct pending data-phase calibration |
| MacLean-Thorp-Ziemba fractional Kelly / Grossman-Zhou drawdown-constrained sizing | **A** (method, mathematically derived) | Textbook-level, internally re-derivable results (this dossier re-derives the `f(2−f)` identity directly) | The specific `f_Kelly` range (0.15–0.35) and cushion exponent `p` are Tier C, own-construct |
| Gorman-Sapra-Weigand dispersion-IR link | **B** | Single paper, moderate citation confidence, not independently re-verified this session | Directionally consistent with, and a natural extension of, the well-established Grinold-Kahn framework |
| Name-count formula (§4b), band-width formula (§4c), sizing-cap synthesis (§4d) | **B** (arithmetic derived from A/B-tier mechanisms) | Deterministic construction from cited mechanisms | The *inputs* (dispersion percentiles, `τ_half` per signal, decay-haircut alphas) are themselves Tier B/C per Workstreams 01–03/09; final numbers inherit that uncertainty |
| Hoffstein et al. rebalance-timing-luck | **B** (practitioner research, not peer-reviewed) | A single research group's applied work, widely cited in practitioner circles but not academically refereed | Mechanism (variance reduction from date-averaging) is close to a law-of-large-numbers argument, low residual risk despite the citation tier |

---

## 6. Research method for the data phase

1. **Fit the characteristic-to-weight mapping `g(·)` (§4a) via the Brandt-Santa-Clara-Valkanov
   direct-utility-maximization approach**, using the program's already-purged/embargoed
   cross-validation protocol (Workstream 09) — never by literally estimating a covariance-inverted
   mean-variance solution. Report performance against the 1/N and against a simple linear-rank
   benchmark, per DeMiguel et al.'s own recommended comparison set.
2. **Calibrate the Ledoit-Wolf shrinkage intensity on Indian bhavcopy-derived returns**, not import a
   US-literature intensity, since shrinkage-optimal intensity is a function of the cross-sectional
   sample size and time-series length actually available (India's ~30-year usable history, per
   Workstream 09 §2). Validate the shrunk covariance's out-of-sample risk forecasts (realized vs.
   predicted portfolio variance) as a first, cheap gate before it is trusted for risk budgeting.
3. **Estimate `N_floor`, `N_ceiling`, and `avg_min_weight` per book empirically** rather than freeze
   this dossier's illustrative ranges: run the Evans-Archer/Statman-style variance-reduction curve
   directly on India's own cross-sectional return data (post-1994/95 bhavcopy history, per Workstream
   09 §2), separately for the rank buckets relevant to each book, and re-derive the diversification
   floor from Indian idiosyncratic-volatility levels rather than assume the US CLMX trend transfers
   directly.
4. **Estimate the dispersion percentile `D` (§4b) from the trailing distribution of cross-sectional
   return dispersion** in the book's own universe (e.g., rolling 3-month cross-sectional standard
   deviation of returns), using an expanding-window historical percentile (never a fixed numeric
   threshold), consistent with Contract §6.
5. **Estimate `τ_half` per signal via the bias-corrected AR(1)/Hamilton-filter machinery already
   specified in Workstream 09** (Kendall/Marriott-Pope small-sample correction; Andrews/Hansen exact
   correction near the unit root) — the band-width formula (§4c) is only as good as this input, and
   must inherit Workstream 09's full estimation discipline, not a separately-invented half-life
   number.
6. **Backtest the band-width and sizing formulas jointly with the cost-curve function from
   Workstream 05 §4h**, using the same rank-bucket-specific cost inputs, and report the realized
   Transfer Coefficient (Clarke-de Silva-Thorley, F9) achieved under the mandate's hard caps versus
   the theoretical unconstrained-signal IR, to make the caps' IR cost measurable rather than assumed.
7. **Every sweep this dossier's parameters require** (τ_ref calibration, f_Kelly within its proposed
   0.15–0.35 range, the cushion exponent p, avg_min_weight per book) **enters the program's
   cumulative trial ledger** (Workstream 09 §4/§6 Phase 7) before any single value is frozen into the
   registry — this dossier alone proposes at least four such sweeps, each multiplying the existing
   Deflated-Sharpe-Ratio trial count.
8. **Run the state-contingent cushion scaling (§4d) through Workstream 04's drawdown-episode
   definition** (the testable flash-crash exclusion, Open Q#5) to confirm it behaves sensibly (does
   not force sizing to zero on an excluded flash-crash-and-immediate-reversal episode) before it is
   trusted at the position level, mirroring the same check the drawdown constraint itself must pass
   at the portfolio level.
9. **Validate the Stage-3 output against Stage 1's completeness requirement** (Contract Architecture
   §2 — Stage 1 must emit a complete, self-sufficient portfolio): confirm Stage 3's characteristic-
   mapping optimizer, run on Stage-1-only signals with no Stage-2 input, still produces mandate-
   compliant portfolios (all hard caps binding correctly) at every historical rebalance date, before
   any Stage-2 overlay is layered on top, per Workstream 09 Phase 5.

---

## 7. Open questions and [VERIFY] items

- `[VERIFY]` DeMiguel-Garlappi-Uppal (2009) exact estimation-window-length figures per N (F1) — order
  of magnitude ("centuries, not years") held with high confidence; exact numbers need re-pinning.
- `[VERIFY]` Ledoit-Wolf (2012, 2017) nonlinear-shrinkage exact venues (F2).
- `[VERIFY]` Buckle (2004) and any Qian-Hua-style breadth-correlation-adjustment citation exact
  bibliographic details (F9) — the substantive point (correlated bets overstate naive breadth) does
  not depend on pinning this exact secondary citation.
- `[VERIFY]` Grinold-Kahn's own stated "good IC ≈ 0.05" benchmark figure — a widely repeated
  practitioner heuristic, not re-confirmed against the book's text this session (F8).
- `[VERIFY]` Bessembinder, Chen, Choi & Wei global-extension paper's exact title, venue, year, and
  headline concentration statistic (F12).
- `[VERIFY]` Cohen-Polk-Silli "Best Ideas" current publication status/venue and the exact
  outperformance magnitude attributed to managers' single largest position (F13).
- `[VERIFY]` Cvitanić-Karatzas (1995) exact venue/pages (F19).
- `[VERIFY]` Gorman-Sapra-Weigand exact volume/issue/pages, and a search for any more recent or more
  rigorously refereed paper making the same dispersion-IR argument, once search access returns (F20).
- `[VERIFY]` Hoffstein et al. exact title(s), full author list, and publication dates for the
  rebalance-timing-luck research (F22) — practitioner source, moderate confidence on substance,
  should be re-confirmed before being relied upon outside this research phase.
- **Open design question for the principal, not just a citation gap**: this dossier reads the
  frozen 5–6%/10%/20% caps as measured against **total portfolio NAV** (consistent with the multi-
  asset mandate's other caps, e.g., debt ≤70%, gold ≤50%, which are clearly NAV-relative). If the
  intended reading is instead "relative to the equity sleeve," the low-`w_eq` edge-case resolution in
  §4b (relaxing `avg_min_weight` rather than breaching the diversification floor) becomes unnecessary
  — this ambiguity should be resolved explicitly in the registry before Stage 3 is implemented.
- **Open design question**: whether the in-progress cap split proposed in §4d (separate full-size-
  cohort and small-ticket-cohort budgets, both nominally "20%" but tracked independently) requires a
  Contract amendment or is a permissible refinement of the existing single number — this dossier
  treats it as a refinement, consistent with Contract §11's instruction that departures from the
  frozen document be stated explicitly with argument, which this section has done.
- **Open question**: the cushion-scaling exponent `p` (§4d) and the `τ_ref` half-life calibration
  anchor (§4c) are both explicitly own-constructs with no literature pinning a specific value —
  flagged for the data-phase sweep (§6 item 7) rather than asserted here as settled.
- **Session-level process note**: as in Workstreams 05/08/09, this workstream's `[VERIFY]` density
  reflects the shared, already-exhausted web-search budget at the point it began, not a change in
  citation-discipline standard — every citation above is offered at the confidence level actually
  held, not inflated to look more verified than it is.

---

*Word count target: 3,500–7,000 (dense, no filler). All rupee figures in crore (₹cr) where used,
consistent with the program's other dossiers. Citations verified this session only where explicitly
stated; all others are trained-knowledge recall tagged per the confidence levels above.*
