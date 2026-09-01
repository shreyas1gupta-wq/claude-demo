# Credit-Cycle Deep Dive — Part A & Part G

Part A: Theory — the full machine · Part G: Psychology and operator failure modes
v1.0 · 2026-09-01 · Deepens `docs/cycles/01-credit-cycle.md` (does not contradict it) · Evidence
base: this file + `research/dossiers/03-credit-financial-cycle.md` (D03) · Ladder seat:
`L10_credit_block` · Status: theory/citations verified here; India coefficients await the data
phase per D03.

This file assumes the existing monograph's four-input state variable as given: **(1)** credit/GDP
gap (Hamilton-filtered, own construction), **(2)** credit-deposit (CD) ratio percentile, **(3)**
issuance/composition quality (Tier C, reduce-only), **(4)** GNPA trend (lagging confirm only).
Part A supplies the theoretical machine those four inputs are trying to compress into one number,
and is honest, at each step, about what that compression throws away. Part G turns to the desk
that has to *use* the number, not the number itself.

---

## PART A — Theory: the full machine

### A.1 Fisher 1933 — debt-deflation

**(i) Mechanism.** An economy over-indebted relative to income meets a trigger (a price shock, a
policy tightening, a disappointing harvest of returns), setting off a nine-link chain (below).
Because debt contracts are fixed in nominal rupees, a falling price level **raises the real
burden of every rupee still owed**, even though nobody has borrowed a fresh rupee — and the chain
ends in a paradox that gives the theory its bite: **nominal** interest rates fall (nobody wants to
borrow, central banks ease) while **real** (deflation-adjusted) rates *rise*, because deflation
itself is a return paid to anyone still holding cash or fixed claims. Fisher's own line: *"the more
the debtors pay, the more they owe"* — paying debt down during deflation can raise real leverage
rather than cut it, because the unit of account is appreciating faster than the debt is repaid.

Fisher's nine-step chain (Econometrica 1933, p.341-2), in order: (1) debt liquidation → distress
selling; (2) contraction of deposit currency as loans are repaid, and a slowdown in velocity; (3)
a fall in the price level; (4) a still greater fall in net worths, precipitating bankruptcies; (5)
a like fall in profits; (6) a reduction in output, trade and employment; (7) pessimism and loss of
confidence; (8) hoarding, slowing velocity still further; (9) complicated disturbances in interest
rates — nominal rates fall, real rates rise.

**(ii) Formal structure.** Real debt burden `B = D / P`, where `D` = nominal debt stock and `P` =
price level. In logs, `d(ln B) = d(ln D) − d(ln P)`. Debt repayment makes `d(ln D) < 0`; if
deflation is faster still (`d(ln P)` more negative than `d(ln D)`), `d(ln B) > 0` — **the real
burden rises even while the nominal stock is shrinking.** That single inequality is the entire
mechanism in one line.

**(iii) For our state variable.** A design constraint, not a new input: the credit-state reading
must never be interpreted independent of the **nominal-growth/price-level trend**. A credit stock
that looks merely "elevated" against a decelerating nominal-GDP trend (nominal growth falling, not
necessarily outright deflation) is mechanically carrying a rising real burden even with zero new
bad-loan origination — this is an *interaction* to document in the ladder notes (the credit block
sits beside a nominal-growth/inflation state elsewhere in the stack), never a fitted new term,
consistent with the "no fitted regime switching" rule.

**(iv) Citation.** Fisher, Irving (1933), "The Debt-Deflation Theory of Great Depressions,"
*Econometrica* 1(4): 337–357. **[Verified]**

---

### A.2 Minsky's Financial Instability Hypothesis — in full

**(i) Mechanism.** Minsky's claim is that financial stability is not a resting state — it is a
phase that manufactures its own destruction, because success changes behavior. Two building
blocks.

*Two-price theory of capital assets*: an economy runs two distinct price systems. `P_I`, the price
of **currently produced output**, is set by cost plus a markup, the ordinary textbook way. `P_K`,
the price of **capital assets** (plant, land, securities — anything bought for its income stream),
is the discounted present value of expected future **quasi-rents** (the net cash flow an asset
generates), *minus* a margin of safety for genuinely uncertain (not merely risky) future cash
flows. Investment happens whenever `P_K > P_I` — worth building or buying exactly when the market
price of owning exceeds the cost of producing.

*Hedge / speculative / Ponzi finance*: every unit (firm, bank, household) is classified by the
relation between expected cash receipts and debt-service commitments. **Hedge**: income covers
principal and interest every period — only insolvency, never illiquidity, can kill the unit.
**Speculative**: income covers interest but not near-term principal, so maturing debt must be
*rolled over* — a solvent unit now carries pure refinancing risk. **Ponzi**: income doesn't even
cover interest — the unit must borrow more, sell assets, or rely on its own collateral's
appreciation just to service existing debt.

*Endogenous migration ("why stability destabilizes")*: after a run without a crisis, three things
reinforce each other — realized cash flows meeting or beating expectations makes the margin of
safety in both `P_K` and lenders' underwriting look unnecessary in hindsight (both sides revise
risk down); low *observed* volatility is read as evidence of low *true* risk (the trap
Brunnermeier-Sannikov formalize in continuous time, A.7); and competition, among lenders for
volume and among borrowers/asset managers for return, pushes the *marginal* unit of new finance
toward speculative and then Ponzi structures, since those support higher current asset prices as
long as the rollover keeps working. The aggregate structure migrates from hedge- to
speculative/Ponzi-dominated purely as a consequence of *surviving* without a crisis — no external
shock is needed to explain the vulnerability, only a trigger to convert an already-fragile
structure into a "Minsky moment": forced sales by Ponzi/speculative units to meet cash
commitments depress `P_K`, pushing units solvent against the *old*, higher `P_K` into
speculative/Ponzi status too — the same migration running in reverse.

**(ii) Formal structure.** For expected receipts `R_t` and debt-service commitment (interest +
scheduled principal) `C_t` at date `t`: **hedge** if `R_t ≥ C_t` for all `t`; **speculative** if
`R_t ≥ interest_t` for all `t` but `R_t < C_t` in some near-term `t`; **Ponzi** if `R_t <
interest_t` for some `t`. Price of capital: `P_K = Σ_t [E(quasi-rent_t) / (1+ρ)^t] − margin(ρ,
leverage)`, where `ρ` is the discount rate (safe rate plus risk premium) and `margin(·)` shrinks
endogenously as realized losses stay low.

**(iii) For our state variable.** Economy-wide unit-level cash-flow-to-debt-service ratios are not
observable from free India data. The practical proxies are L10's existing inputs #2 and #3: a
rising **CD ratio** evidences the liability structure stretching past the hedge-financeable
deposit base; **composition** (the fastest-growing borrower categories) evidences migration toward
speculative/Ponzi finance in the segments driving credit growth. Design constraint:
**age-in-quadrant** should be read as independently informative — Minsky predicts fragility rises
monotonically with a boom's *duration*, independent of its *level*, a first-principles reason to
carry age-in-quadrant even before H66–H68 admit it to any traded rule.

**(iv) Citation.** Minsky, Hyman P. (1992), "The Financial Instability Hypothesis," Levy Economics
Institute of Bard College, Working Paper No. 74. **[Verified]** Two-price theory developed earlier
in Minsky's *John Maynard Keynes* (1975) and *Stabilizing an Unstable Economy* (1986, Yale
University Press) — standard attribution. **[Verified]**

---

### A.3 Kindleberger's stages — and what each looks like in data

**(i) Mechanism.** Kindleberger (explicitly building on Minsky — hence "Kindleberger-Minsky
model") describes a bubble's anatomy as five stages.

| Stage | What happens | What it looks like in DATA |
|---|---|---|
| **Displacement** | An exogenous shock changes profit expectations in some sector: new technology, deregulation, a policy change, war's end | A structural break in a sectoral credit-deployment series; a dated policy event; early asset-price moves concentrated in one sector |
| **Boom** | Credit expands to finance the opportunity; early adopters' genuine profits draw in more capital | Sectoral credit growth accelerating above trend; sector outperforming the broad market; often with monetary easing |
| **Euphoria** | Participation broadens past informed money; leverage rises; "new era" narratives justify valuations by the displacement story | Retail/household participation share rising; leverage ratios (margin debt, LTV, unsecured-credit share) at multi-year highs; valuation multiples decoupling from earnings; new-issuance *quality* falling even as *volume* rises (Greenwood-Hanson's issuer-quality signal — D03 F6) |
| **Distress** | Insiders and the earliest money start selling; a prominent failure or forecast miss cracks confidence | First visible defaults in the weakest credit tier; asset-price momentum turning negative on rising volume (distribution) |
| **Revulsion** | A rush for liquidity; forced selling by leveraged holders (the "Minsky moment"); credit contracts | Credit growth turning sharply negative; risk spreads gapping wider; GNPA rising with its usual multi-quarter recognition lag |

**(ii) Formal structure.** No single equation — the model is a *sequence*, and its formal content
is the *ordering claim*: displacement causes boom causes euphoria causes distress causes
revulsion, with the transition from euphoria to distress typically triggered by an event that need
not itself be large (Minsky's "trigger," not the cause of the fragility).

**(iii) For our state variable.** Displacement and early boom are largely invisible to a pure
credit-level signal — the credit/GDP gap only fires once the boom is well underway, consistent
with the existing monograph's own finding that the expanding-mode gap is "an acceleration-surprise
detector, not a level gap" (`docs/cycles/01-credit-cycle.md` §4.1). Euphoria is where the
CD-ratio and composition inputs saturate; distress/revulsion is where GNPA finally confirms — by
which point de-risking should already have happened. Design constraint: never expect one scalar
to distinguish "boom" from "euphoria" — this is the argument for the phase object's **velocity**
and **age** dimensions mattering as much as its level, and it is why the composite's documented
real-time signature (fires in the build-out, decays late in the boom, collapses hardest at the
bust *onset*) is the *correct* behavior for a Kindleberger-stage transition, not an artifact.

**(iv) Citation.** Kindleberger, Charles P. (1978), *Manias, Panics, and Crashes: A History of
Financial Crises*, New York: Basic Books, 1st ed. **[Verified]** (Later editions add Robert Z.
Aliber as co-author.)

---

### A.4 Kiyotaki-Moore 1997 — collateral amplification

**(i) Mechanism.** When lenders cannot force repayment except by seizing pledged collateral
(limited enforcement — courts can compel asset seizure, not hidden effort or income), a durable
asset does double duty: a factor of production **and** the only thing that makes borrowing
possible. A farmer's borrowing capacity is capped by the market value of the land they can pledge;
the price of that land is itself set partly by how much borrowing capacity it unlocks. A small,
*temporary* shock to net worth therefore produces a large, *persistent* effect: net worth falls →
collateral constraint bites → constrained agents cut land purchases/investment → land price falls
(less demand, plus the multiplier itself) → **everyone's** collateral value falls, including
agents never touched by the original shock → borrowing capacity falls economy-wide → investment
falls further → land price falls further. The loop runs the same way in reverse on the upswing —
credit and asset prices amplify and prolong each other's moves for years after the triggering
shock has passed.

**(ii) Formal structure.** Let `k_t` = an agent's land holding, `q_t` = land price, `b_t` = amount
borrowed. Collateral constraint: `b_t ≤ m · q_{t+1} · k_t / R`, where `m ∈ (0,1]` is the
loan-to-value the lender extends against **next period's** expected land value `q_{t+1}` (the
lender applies a haircut `1−m`), and `R` is the gross interest rate. Because `q_{t+1}` sits on the
right-hand side of *today's* borrowing capacity, and `q_{t+1}` is itself set by next period's
aggregate land demand — which depends recursively on that period's net worth — price and
borrowing capacity are jointly, forward-referentially determined. That forward reference is what
produces genuine amplification rather than a one-off level shift.

**(iii) For our state variable.** This is the strongest formal reason to weight **collateral
class**, not just credit growth, inside the composition input: amplification is strongest exactly
where the pledged asset is illiquid/hard-to-value in stress (real estate ≫ listed equity ≫ cash)
and where loan-to-value ratios are high and rising. Design constraint: real-estate- and
NBFC-linked credit (both the 2018 IL&FS shock and the 2021–24 unsecured-retail/NBFC boom are
collateral-channel events by this mechanism, not merely "more credit," per D03 I5/I11) should
carry more weight per rupee of growth than diversified corporate working-capital credit — an
honest, literature-grounded reason to differentiate collateral classes inside input #3 rather than
treating "unsecured + NBFC share" as one flat number, even though the Tier-C cap stays reduce-only
regardless.

**(iv) Citation.** Kiyotaki, Nobuhiro & Moore, John (1997), "Credit Cycles," *Journal of Political
Economy* 105(2): 211–248. **[Verified]**

---

### A.5 Bernanke-Gertler-Gilchrist — the financial accelerator

**(i) Mechanism.** BGG formalize why the *cost* of external finance (borrowing from anyone but
yourself) is not a flat markup over the risk-free rate, but rises specifically as the borrower's
own net worth falls. Under costly-state-verification (the lender cannot costlessly observe the
borrower's true prospects), a borrower putting up less of their own money signals more moral
hazard, so the lender charges an **external finance premium** (EFP — the spread over the
risk-free rate a borrower pays purely because of this information friction) that is decreasing in
net worth. Net worth is itself procyclical (profits and asset values rise in good times), so the
EFP is **countercyclical**: it falls in booms — cheapening credit exactly when the economy least
needs it, encouraging more borrowing — and rises in downturns exactly when firms most need credit,
deepening the contraction. This "financial accelerator" amplifies ordinary business-cycle shocks
through the **price** of credit, a distinct and complementary channel to Kiyotaki-Moore's
collateral-**quantity** story.

**(ii) Formal structure.** `s = s(N/K)`, `s' < 0`, where `N` = entrepreneur net worth, `K` = total
capital financed (so `N/K` is the "skin in the game" ratio), and `s ≥ 1` is the premium multiplier.
Cost of borrowed funds: `R^k = R^f · s(N/K)`, where `R^f` is the risk-free/policy rate. Since `N`
moves procyclically, `s` moves countercyclically, and a given shock to `R^f` or productivity
produces a larger swing in investment than the same shock would under `s ≡ 1` (the frictionless
benchmark).

**(iii) For our state variable.** The free-data India analogue of the EFP is the corporate-vs-
risk-free spread — and D03 (I10) already flags India's CCIL/FIMMDA AAA-vs-G-Sec spread data as
thin, member-gated at fine granularity, its own [VERIFY]. Honest gap: BGG is a *theoretical
cross-check* here — predicting GNPA/composition deterioration should widen spreads with a lag,
a hypothesis for R7's event-validation (2018 IL&FS, 2023–24 tightening) — not a fifth input today.

**(iv) Citation.** Bernanke, Ben S.; Gertler, Mark; Gilchrist, Simon (1999), "The Financial
Accelerator in a Quantitative Business Cycle Framework," in Taylor & Woodford (eds.), *Handbook of
Macroeconomics*, Vol. 1, Ch. 21, Elsevier, pp. 1341–1393. **[Verified; also NBER WP 6455]**

---

### A.6 Geanakoplos — the leverage cycle

**(i) Mechanism.** Geanakoplos's claim: the price of credit that matters most for asset prices and
crashes is not the interest rate — it is **leverage** (equivalently, the **margin**/**haircut** a
lender demands: the fraction of the purchase price the buyer must fund with own equity). Two
assets can trade at the same rate on very different leverage terms, and it is the terms, not the
rate, that govern how much buying power enters the market and how violently it leaves. *Upswing*:
calm markets → lenders competing for volume perceive collateral risk as low → margins fall
(leverage rises) → the same equity buys more of the asset → "**natural buyers**" (the most
optimistic, least risk-averse holders, willing to use the most leverage) bid the price up further
→ more collateral value is freed → margins fall further. *Crash*: "scary bad news" (news
widening the *dispersion* of possible outcomes, not necessarily bad news about fundamentals) →
lenders tighten margins → the most-levered natural buyers, now forced to delever, must sell — and
because they were the highest-valuation holders, the marginal buyer left standing values the
asset much lower → price falls sharply → losses redistribute wealth away from optimists (who lose
disproportionately, being levered) and independently justify tighter margins still (volatile
prices look riskier as collateral) → more forced selling. The three elements feed back on each
other, which is why leverage-cycle crashes are fast relative to the slow multi-year buildup.

**(ii) Formal structure.** Leverage `L = 1/h`, where `h ∈ (0,1)` is the haircut (margin) — the
equity fraction required to hold the asset. Total buying power from a stock of optimist equity `E`
is `L·E = E/h`: a **fall in `h`** multiplies the same equity into more buying power with no new
money entering and no interest rate moving at all. The formal claim: `d(price)/d(h)` can dominate
`d(price)/d(interest rate)` in a credit boom.

**(iii) For our state variable.** The sharpest justification in the whole survey for preferring a
measure of **leverage terms** over credit **quantity** or **price** wherever a free India proxy
exists — none of L10's four inputs currently measures terms (an honest, stated gap: #1–#2 are
quantity/level measures, not terms). Retail margin-trading-facility (MTF) haircuts, F&O
margin/SPAN requirements, and NBFC/HFC loan-to-value norms on real-estate and gold loans are the
closest India-observable analogues to `h`. A future extension should test whether RBI's own
risk-weight actions (per the Nov-2023 event in D03 I5) can proxy this directly, since the
regulator moves risk weights precisely when it judges leverage *terms*, not credit quantity, have
become the binding risk.

**(iv) Citation.** Geanakoplos, John (2010), "The Leverage Cycle," in Acemoglu, Rogoff & Woodford
(eds.), *NBER Macroeconomics Annual 2009*, Vol. 24, University of Chicago Press, pp. 1–65.
**[Verified]**

---

### A.7 Brunnermeier-Sannikov 2014 — the volatility paradox

**(i) Mechanism.** BS build a continuous-time model where the financial sector's own net worth is
a state variable determining its risk-bearing capacity. Near the steady state (well-capitalized
intermediaries), shocks are absorbed smoothly and volatility is low; once net worth erodes past a
threshold, the *same-size* shock triggers a much larger, nonlinear response (fire sales → further
erosion → more fire sales) — the system generates **endogenous risk** (volatility from the
amplification mechanism itself, not the underlying shock's size) that dwarfs exogenous risk.
Headline result, the **volatility paradox**: a period of *low* measured volatility does not mean
the system is safe — it can mean the opposite, because low observed volatility encourages more
leverage-taking (agents infer the world is safe — Minsky's endogenous migration, A.2, as an
equilibrium object), shrinking the net-worth buffer that would otherwise absorb the next shock. The
system moves *closer* to the crisis threshold precisely while every measured indicator says risk
is falling — why calm periods are the dangerous ones: shock-absorption capacity is quietly used up
while everything looks fine.

**(ii) Formal structure.** Let `η_t` = financial-sector net worth share of aggregate capital (the
key state variable). Asset price `q(η)` is nearly flat away from a low-`η` boundary (shocks pass
through with little amplification) but steepens sharply near it, so the same shock `dη` produces a
much larger `dq` near the boundary. Endogenous volatility: `σ_endogenous(η_t) = |q'(η_t)| ·
σ_exogenous` — which stays large near the boundary even as `σ_exogenous → 0`. That is the
volatility paradox stated formally.

**(iii) For our state variable.** The cleanest theoretical basis for reading **low realized
volatility as a warning**, not a comfort, when it co-occurs with a high credit-state reading — the
opposite of naive vol-targeting sizing. Design constraint: document, for the eventual regime
matrix, that "high credit-state + low realized vol" deserves its own named cell as the single most
dangerous joint reading, not a reassuring one — bracing Kindleberger's euphoria (A.3) and Minsky's
migration (A.2) with a formal mechanism rather than leaving them narrative-only.

**(iv) Citation.** Brunnermeier, Markus K. & Sannikov, Yuliy (2014), "A Macroeconomic Model with a
Financial Sector," *American Economic Review* 104(2): 379–421. **[Verified]**

---

### A.8 Adrian-Shin — intermediary leverage

**(i) Mechanism.** Adrian-Shin show empirically (US broker-dealers) that leverage is strongly
**procyclical**: total assets and leverage grow together while equity is comparatively "sticky,"
so asset growth is financed almost entirely by more debt, not more equity, in booms. The
mechanism: intermediaries target a fixed **Value-at-Risk** (VaR — a probability-times-loss ceiling
a bank sets on its trading book) budget, and because *measured* volatility falls in calm periods,
the *same* VaR budget mechanically permits *more* leverage as measured vol falls — with no change
in risk appetite. This is a purely mechanical amplifier (unlike BGG's information-friction story
or Minsky's psychological-migration story): a risk-management rule, applied uniformly by many
institutions at once, converts a fall in observed volatility directly into a system-wide rise in
leverage — precisely when Brunnermeier-Sannikov (A.7) says the system can least afford it. On the
way down the rule reverses: a volatility spike forces simultaneous deleveraging, itself raising
realized volatility — a mechanical spiral distinct from, but reinforcing, Geanakoplos's margin
spiral (A.6).

**(ii) Formal structure.** VaR constraint: `L · σ_portfolio ≤ VaR-budget / z`, where `L` =
leverage, `σ_portfolio` = measured portfolio return volatility, `z` = the confidence-level
multiplier, and `VaR-budget` is the roughly fixed rupee loss the institution tolerates. Rearranged:
`L ≤ (VaR-budget/z) / σ_portfolio` — leverage is mechanically inverse to measured volatility.

**(iii) For our state variable.** India's broker-dealer/prime-broker sector is thin relative to
the US, and granular VaR-based leverage data isn't freely available — this, like BGG, is currently
a theoretical cross-check, not a constructible input. The closest observable India proxy is F&O
**open-interest growth relative to implied/realized vol** (from NSE bhavcopy, a
free, approved source) — OI growing while vol falls is the India-observable footprint of this
mechanism, and is a candidate for the *flow/derivatives-cycle* workstream adjacent to L10, not a
new credit-block input. Flagged here so it is not lost between workstreams; this is a cross-check
on A.7's reading, not an independent mechanism for L10.

**(iv) Citation.** Adrian, Tobias & Shin, Hyun Song (2010), "Liquidity and Leverage," *Journal of
Financial Intermediation* 19(3): 418–437. **[Verified]**

---

### A.9 Mian-Sufi — the household-debt channel, and which channel dominates India today

**(i) Mechanism.** Mian-Sufi's "credit-driven household demand channel": when credit *supply*
expands (looser lending standards — not a rise in household demand for credit), households borrow
against future income/collateral to raise *current* consumption and housing demand. This produces
a demand-driven boom (especially in non-tradable, local-multiplier sectors — construction, retail)
that looks like ordinary healthy growth while it lasts, but necessarily borrows against future
income: when debt service catches up with income, or credit supply reverses, households —
disproportionately the lower-net-worth, higher-marginal-propensity-to-consume ones who hold the
debt — must cut consumption sharply. This is distinct from the **corporate** channel
(over-investment in productive capacity — BGG's and Kiyotaki-Moore's setting): it operates through
aggregate *demand* not *supply*, has a different data footprint (household debt/GDP vs. corporate
leverage/capex), and is harder to see coming, since households have no stock price to watch.

**Which channel dominates in India today.** D03's own chronology (I5) already settles this
empirically: India's 2021–24 credit upswing is disproportionately an **unsecured retail/household**
channel — non-food credit growth 16%→20%/yr, "disproportionately unsecured personal loans/NBFC
exposure"; household debt/GDP 26%→42% (2015→end-2024); CD ratio at an all-time high (~80%) — while
corporate leverage has stayed comparatively contained post-TBS/AQR deleveraging (2015–20). **For
India right now, Mian-Sufi's household channel is the more relevant of the two mechanisms**, not
the corporate/collateral channel that dominates most classic, US-focused credit-cycle literature.

**(ii) Formal structure.** Mian-Sufi-Verner's empirical specification (D03 F8): a 3-year rise in
household-debt/GDP forecasts *lower* GDP growth 3–4 years later, and — critically — professional
forecasters' growth-forecast **errors** are systematically positive (too optimistic) exactly when
household-debt growth has been highest. The mechanism is not a mechanical debt-overhang accounting
identity alone; it is compounded by biased expectations at the professional-forecaster level (a
direct link to A.11's behavioral micro-foundations).

**(iii) For our state variable.** The composition input (L10 #3, "share of incremental credit to
unsecured retail + NBFC") is not an arbitrary proxy — it does double duty as **both** the
Minsky/Kiyotaki-Moore composition signal **and** the Mian-Sufi household-channel signal, since
India's present cycle has the two mechanisms pointing at the same flow of credit. State this in
the ladder documentation: input #3 carries more of the crisis-forecasting load than a
US-literature-only reading would suggest — an argument for a real research push toward Tier B
rather than a permanently-thin Tier-C afterthought, even though reduce-only stays in force until
promotion criteria are actually met.

**(iv) Citation.** Mian, Atif & Sufi, Amir (2018), "Finance and Business Cycles: The Credit-Driven
Household Demand Channel," *Journal of Economic Perspectives* 32(3): 31–58. **[Verified]**
Household-debt/GDP forecasting result: Mian, Sufi & Verner (2017), *Quarterly Journal of
Economics* 132(4): 1755–1817. **[Verified — D03 F8]** India figures per D03 I5, sourced to RBI
FSR/DBIE. **[Verified in-house]**

---

### A.10 The Austrian view — briefly, as contrast

**(i) Mechanism.** Mises (1912) and Hayek (1931) argue that credit expansion *not* backed by prior
voluntary saving — typically because a central bank or fractional-reserve system pushes the
market rate below the "natural rate" that would clear voluntary saving and investment — sends
entrepreneurs a false signal: it looks as if more real resources are available for long-horizon,
capital-intensive projects than actually are. Entrepreneurs start projects viable only if cheap
credit continues; consumers eventually reassert their true consumption preferences ("**forced
saving**" — resources diverted to investment only because consumers were not genuinely willing to
save that much, and they stop tolerating it once relative prices reveal the shortfall), the
expansion halts, and the **"malinvestment"** (capital misallocated to projects only viable at the
artificially low rate) is revealed as a "cluster of errors" concentrated in interest-rate-sensitive
sectors.

**Why we take the measurement insight without the policy theology.** The Austrian *policy*
conclusion — recessions should be allowed to run their liquidationist course; counter-cyclical
offsetting is itself the deeper error — is a normative claim this desk does not need to adjudicate
and does not adopt; it conflicts with the observed post-1990s policy reality this stack must trade
*inside*. But the Austrians' underlying *measurement* insight — that **where** credit goes
(sectoral, maturity, collateral composition), not just its aggregate quantity, determines whether a
boom resolves gently or violently — is the same conclusion Kiyotaki-Moore (A.4), Minsky (A.2), and
Mian-Sufi (A.9) reach from entirely different starting points (equilibrium collateral dynamics,
post-Keynesian finance theory, empirical credit-supply identification). Four unrelated schools
converging on "composition matters as much as level" is stronger evidence for that design
conclusion than any one school's derivation alone.

**(ii) Formal structure.** No equation is adopted here — the insight taken is qualitative:
composition of credit growth carries information that its level does not.

**(iii) For our state variable.** No new input; a documented, four-school convergence argument
reinforcing why L10 input #3 deserves genuine research investment, not merely a reduce-only
placeholder.

**(iv) Citation.** Mises, Ludwig von (1912; Eng. trans. 1934), *The Theory of Money and Credit*;
Hayek, Friedrich A. (1931), *Prices and Production*, London: Routledge & Sons. **[Verified —
standard attribution and dates]**

---

### A.11 Behavioral micro-foundations — the survival argument's engine room

**(i) Mechanism.** Everything above needs a reason why real people and institutions keep
re-supplying the fragility instead of learning from history and pricing it in. Four findings form
an escalating chain: belief formation → belief distortion → institutional product design →
empirical capstone.

1. **Extrapolative expectations** (Greenwood & Shleifer 2014): across six independent data sources
   of investor return expectations (1963–2011), expectations of *future* returns are strongly
   *positively* correlated with *past* returns and the market's current level, and strongly
   *negatively* correlated with model-based, rational expected returns — investors expect returns
   to be highest exactly when a properly specified model says they are lowest, and vice versa.
2. **Diagnostic expectations** (Bordalo, Gennaioli & Shleifer 2018) supply the mechanism:
   formalizing Kahneman-Tversky's representativeness heuristic, agents over-weight scenarios made
   more likely by *recent* news relative to their true probability. Applied to credit markets:
   spreads and underwriting standards become excessively volatile, over-react to news, and undergo
   predictable reversals — exactly the credit-cycle signature L10 tries to harvest.
3. **Neglected risk** (Gennaioli, Shleifer & Vishny 2012) extends the mechanism to institutional
   *product design*: intermediaries, meeting investor demand for "safe" cash flows, engineer
   securities safe under most states but exposed to low-probability tail states neither issuer nor
   buyer represents at all ("local thinking" — contingencies simply absent from the decision
   process, not merely mis-weighted). The neglected risk is unpriced, so issuance is excessive —
   why financial innovation (structured retail loans, co-lending, "buy now pay later") arrives
   disproportionately late in a boom, the moment neglected tail risk is largest. India's 2021–24
   unsecured-retail boom fits this pattern.
4. **Empirical capstone** (Baron & Xiong 2017 — independently verified, D03 F5): bank-equity
   holders — arguably the single most informed class of investor in credit markets — demand *no*
   compensation for elevated crash risk building during a boom: conditional on bank-credit
   expansion exceeding its 95th percentile, the predicted 3-year forward excess return on the
   bank-equity index is **−37.3%** (20 developed countries, 1920–2012) — a result only explicable
   if the market systematically neglects statistically forecastable risk, exactly as #1–#3 predict.

**(ii) Formal structure.** Diagnostic expectations (simplified): subjective probability of state
`θ` given signal `s` is distorted from the true Bayesian posterior as `π_diagnostic(θ|s) ∝
π_true(θ|s) · [π_true(θ|s) / π_true(θ|s_lag)]^φ`, where `s_lag` is a reference/lagged signal and
`φ ≥ 0` is the diagnosticity parameter (`φ=0` recovers rational expectations). States that have
become more likely relative to the recent past are over-weighted in proportion to `φ` — generating
excess volatility and predictable reversal in the credit-spread application.

**(iii) For our state variable — the engine room.** This directly answers CONTRACT §5's demand
that every signal state "why does this survive being known?" The answer is category (i), a
structural/behavioral mechanism persistent under crowding: the bias lives in the **belief-formation
process of the credit-supplying institutions themselves** (loan officers, bank shareholders,
product engineers, retail underwriters) — the agents who would need to trade *against* the boom
*are* the boom. No representative "smart money" stands outside the banking system able to short an
entire economy's credit-supply psychology at scale; the trade is inherently a multi-year,
negative-carry, systemically-backed-sector short, echoing D03's Edge A. This licenses treating the
credit state as genuinely persistent, exempt from the McLean-Pontiff 26%/58% cross-sectional decay
haircuts — and argues for humility about *dating* the cycle: if the bias is in how fast belief
updates on news, not in a fixed periodicity, cycle *length* has no reason to stay stable across
eras, independent support for the clock test's own verdict that this is a state variable, never a
periodic cycle.

**(iv) Citations.** Greenwood, Robin & Shleifer, Andrei (2014), "Expectations of Returns and
Expected Returns," *Review of Financial Studies* 27(3): 714–746. **[Verified]** Bordalo, Pedro;
Gennaioli, Nicola; Shleifer, Andrei (2018), "Diagnostic Expectations and Credit Cycles," *Journal
of Finance* 73(1): 199–227. **[Verified]** Gennaioli, Nicola; Shleifer, Andrei; Vishny, Robert
(2012), "Neglected Risks, Financial Innovation, and Financial Fragility," *Journal of Financial
Economics* 104(3): 452–468. **[Verified]** Baron, Matthew & Xiong, Wei (2017), "Credit Expansion
and Neglected Crash Risk," *Quarterly Journal of Economics* 132(2): 713–764. **[Verified —
D03 F5]**

---

### A.12 Synthesis — mechanism, proxy, capture, and the honest gap

| Mechanism | Observable proxy in principle | L10 input that captures it | Captured today? |
|---|---|---|---|
| Fisher debt-deflation (real burden rises as prices fall) | Nominal-GDP/deflator trend vs. credit growth | None directly — an interaction note, not a 5th input | **Not captured** — stated gap |
| Minsky migration (hedge→speculative→Ponzi) | Composition of incremental credit + liability stretch | #2 (CD ratio) + #3 (composition), jointly | Partially — level + rough composition, not true cash-flow coverage |
| Kindleberger stages | Multi-indicator pattern read as a phase sequence | The phase object (level, velocity, quadrant, age) atop the composite | Captured structurally, not by any single input |
| Kiyotaki-Moore collateral amplification | Collateral-class breakdown of credit growth | #3, currently a flat unsecured+NBFC share | Partially — collateral-class granularity is a stated future refinement |
| BGG financial accelerator (external finance premium) | Corporate spread vs. G-Sec | None — India spread data thin/gated (D03 I10) | **Not captured** — theoretical cross-check only |
| Geanakoplos leverage cycle (margin/haircut terms) | MTF haircuts, F&O margin/SPAN, NBFC LTV norms | None in the current four-input design | **Not captured — the single most important stated gap** |
| Brunnermeier-Sannikov volatility paradox | Realized/implied vol read jointly with credit state | Not an L10 input — a cross-workstream interaction to document | Out of scope for L10 by design |
| Adrian-Shin intermediary leverage / VaR procyclicality | F&O open-interest growth vs. vol | Not an L10 input — flow/derivatives-cycle candidate | Out of scope for L10 |
| Mian-Sufi household-debt channel | HH-debt/GDP change (3y), unsecured retail share | #3 — same series doing double duty with Minsky/Kiyotaki-Moore in India today | Captured, Tier C reduce-only |
| Austrian composition insight | (a convergence argument, not a new observable) | Reinforces #3's weighting rationale | N/A — argument, not measurement |
| Behavioral micro-foundations | (the *why*, not a *what*) | Underpins the survival argument for the whole seat | N/A by construction |
| GNPA / recognition | GNPA level + trend | #4 (lagging confirm) | Captured — by design, confirm-only |

**What no free observable captures — stated honestly.** Leverage *terms* (margin/haircut/LTV at a
system level — Geanakoplos's actual state variable) and the external finance premium (BGG) are
economically central but **not constructible from any free India source available today**. The
state variable as built is a **quantity-and-level** instrument (credit/GDP, CD ratio, composition
share, GNPA) sitting inside a literature that increasingly locates the true crisis mechanism in
**terms** (leverage, haircuts, premia) we have no free lens on yet. That gap should stay visible in
the ladder documentation, not be quietly assumed away by the four inputs that do exist.

---

## PART G — Psychology and operator failure modes

The theory in Part A describes a system that misprices its own fragility. This part is about the
desk that has to act on a reading of that system — the specific, historically-recurring ways a
human (or an LLM acting under human authority) mishandles a correct signal. Every failure mode
below is mapped to a countermeasure already built into this program's design (`CONTRACT.md`,
`docs/PIPELINE.md`, `research/OPEN_QUESTIONS.md`).

### G.1 Overriding the state in booms: "this time the fundamentals are real"

**Mechanism.** The operator sees the credit state de-risking, but every fact in front of them —
earnings beats, a strong GDP print, a story for why this growth is durable — argues the state
variable is stale. Reinhart & Rogoff (2009) document this exact pattern, "**this time is
different**": the recurring belief, right before a crisis, that improved policy or institutions
make historical leverage limits inapplicable — replicated across a chronology of dozens of
countries and hundreds of crisis-years, precisely *because* each episode really does have a
locally true differentiating story. That is what makes the override tempting; the pattern is that
the story is *always* locally true and still doesn't prevent the crisis. The grounded mechanism is
A.11's diagnostic expectations operating on the operator, not just the market: recent good news is
over-weighted against its true base rate, reinforced by Kindleberger's euphoria stage (A.3) — the
operator is embedded *in* the boom, not observing it from outside.

**Countermeasure.** Pre-registration (CONTRACT §9: "pre-register every hypothesis before running
it") plus the Challenger Protocol's rule that "frozen v1 parameters are the null hypothesis
forever" (`docs/PIPELINE.md` §2.11). A discretionary override of the state reading *is* a
hypothesis change, admissible only via scheduled Challenger review on pre-registered win criteria,
however compelling the in-the-moment narrative. The override is banned not by asking for better
judgment, but by deleting the moment as a decision point at all.

### G.2 Capitulating at the bottom

**Mechanism.** At the bottom of a down-leg, the same diagnostic-expectations bias mirrors itself:
recent bad news (defaults, drawdowns, a losing streak) is over-weighted, making "the rules don't
work any more / the world has permanently changed" feel representative, even though the base rate
favors mean reversion at exactly this point. This is made structurally worse by the state
variable's own documented behavior: its largest-magnitude reading arrives at the bust *onset*
(`docs/cycles/01-credit-cycle.md` §4.1), which is exactly when it looks least trustworthy to an
operator watching drawdown accumulate. Galbraith's bezzle dynamic (G.4) compounds this: trust
collapses fastest at the bottom, "something close to a universal trust turned into something akin
to universal suspicion" within days — an environment that makes calm rule-following hardest
precisely when it is most valuable.

**Countermeasure.** The **anti-capitulation lock**, mechanical not discretionary
(`docs/PIPELINE.md` §2.11, kill-switch #6): "no parameter/budget/structure change may be
*initiated* while the affected sleeve is beyond a grid-defined drawdown depth; executing
pre-registered rules is always allowed; changing rules mid-pain never is." It does not ask the
operator to resist the urge to capitulate — it makes capitulation structurally impossible
mid-drawdown, deferring any redesign to the scheduled post-drawdown Ang-Goetzmann-Schaefer review,
which runs only *after* the episode ends.

### G.3 Narrative capture

**Mechanism.** A broader, institution-level version of G.1: a genuinely real structural shock
(India's digital-lending infrastructure, UPI-enabled underwriting, credit-market formalization
post-GST/demonetization) becomes *the* frame through which all subsequent data is read — Kindleberger's
**displacement** stage (A.3) treated as a permanent regime change rather than stage one of five.
Disconfirming evidence (composition deterioration, CD-ratio saturation) gets explained away as
"different this time because of [the real shock]" rather than weighted as a warning, and because
the story is genuinely compelling, it captures not just one operator's judgment but an entire
research process's willingness to even *propose* the disconfirming hypothesis.

**Countermeasure.** The trial-budget/DSR discipline (CONTRACT §9;
`docs/PIPELINE.md` FL6, FL15) plus the evidence-tier caps (CONTRACT §4): any new hypothesis
motivated by a compelling narrative still enters the funnel, is pre-registered before results are
seen, and counts against the same trial budget as everything else. A narrative cannot buy a signal
past its evidence tier merely by being compelling — Tier C stays Tier C, reduce-only, until ≥4
India observations or ≥10 defended cross-country analogues actually accumulate.

### G.4 Galbraith's bezzle

**Mechanism.** Galbraith (1955) observes that at any moment there is an "inventory of undiscovered
embezzlement" — more broadly, undiscovered fraud, misrepresentation, or simply unrealized bad
decisions sitting inside the financial system, which the boom conceals (both embezzler and
embezzled feel richer, since the loss hasn't been discovered — "psychic wealth") and the bust
reveals all at once. Applied to a credit cycle: booms inflate not just good assets but the
*apparent* quality of what looks like a good loan, because the mechanisms that would normally
reveal a bad one (defaults, audits, redemptions) are themselves slower in a boom. The bezzle is
largest exactly when GNPA — our lagging confirm input — looks best. An operator reading a
decadal-best GNPA print (2.15%, D03 I5, current India reading) as evidence quality is genuinely
strong, rather than as evidence undiscovered stress may be near its cycle peak, makes exactly the
mistake Galbraith's concept warns against.

**Countermeasure.** The explicit rule that GNPA "never enters as a leading
input... only as a confirmation dummy for de-risking states, never for re-risking"
(`docs/cycles/01-credit-cycle.md` §4, input #4) is a direct bezzle countermeasure: it structurally
forecloses the single most tempting operator error — reading good *lagging* credit-quality data as
good *forward-looking* news — from ever entering the de-risking/re-risking decision in the wrong
direction.

### G.5 Agency and career-risk incentives that make institutions procyclical

**Mechanism.** The institutional-scale version of the same bias, and the reason the desk's
countermeasures are mechanical rather than trained judgment. A portfolio manager or credit officer
who under-risks during a boom that keeps extending — correctly worried about a cycle that hasn't
turned — bears career risk that is asymmetric and near-term: visible, benchmarked
underperformance for years, against a payoff (avoiding the bust) uncertain in timing and invisible
if it never lands inside their own tenure. This is the "limits to arbitrage" argument already used
for why the credit signal survives being known (A.11, D03 Edge A), turned inward: shorting a
systemically-backed boom is a multi-year, negative-carry, career-risk position few *individuals*,
not just institutions, can hold to completion. It is an agency problem, not merely a
market-inefficiency story — decision-makers are evaluated on a horizon shorter than the cycle they
manage, so the rational *individual* response is to ride the boom, or to genuinely believe
(G.1/G.3) an override is warranted this time.

**Countermeasure.** This is why the credit cycle is framed as buying "permission to run
concentrated and levered without breaching the drawdown ceiling" (CONTRACT §7, Known Prior #3),
not a discretionary timing call subject to anyone's career horizon — frozen Tier-B parameters,
phase reported but non-actionable pending H66–H68 (below), and Challenger's scheduled-review-only
promotion together ensure no individual's short-horizon incentive can move the read between
reviews, because both Minsky (A.2) and the agency literature predict anyone left with discretion
will be pulled toward the procyclical choice by their own horizon, not just their beliefs.

### G.6 Over-reading an unvalidated phase read (the D-quadrant discipline)

**Mechanism.** The phase object's quadrant ∈ {recovery, boom, slowdown, downturn} is new (added
2026-09-01, `research/OPEN_QUESTIONS.md`) and immediately tempting to over-interpret: "we're in the
downturn (D) quadrant, therefore de-risk harder / re-risk now" is exactly the narrative-capture
mechanism of G.3, applied to a label instead of a story, before the label has earned any
statistical trust.

**Countermeasure.** The phase **consumption gate**: quadrant and age are
computed, logged, and displayed everywhere, but "may not condition any traded rule until H66–H68
pass their pre-registered tests" (`research/OPEN_QUESTIONS.md`, 2026-09-01 directive). The
countermeasure does not forbid *looking* at the quadrant — it forbids *acting* on it until the
evidence bar (quadrant asymmetry at matched levels, grid stability, duration dependence of
quadrant exit) is actually cleared.

### G.7 Failure mode → countermeasure map

| Failure mode | Mechanism (grounded) | Countermeasure |
|---|---|---|
| Overriding in booms ("fundamentals are real") | Diagnostic expectations on the operator (A.11); Reinhart-Rogoff TTID; Kindleberger euphoria | Pre-registration + Challenger frozen-null rule — overrides are hypothesis changes, scheduled review only |
| Capitulating at the bottom | Diagnostic expectations mirrored on bad news; largest state reading at the least-trusted moment; Galbraith's trust collapse | **Anti-capitulation lock**: no rule change *initiated* mid-drawdown; pre-registered rules keep executing |
| Narrative capture | A real displacement story (Kindleberger stage 1) treated as a permanent frame; institutional groupthink | Trial-budget/DSR discipline + evidence-tier caps: a narrative cannot promote a signal past its tier |
| Wanting to *add* exposure on a compelling but thin signal | Same bias applied to one input, not the whole state | **Tier-C reduce-only rule**: may only reduce risk, never add, however compelling the story |
| Galbraith's bezzle (concealed stress revealed at the bust) | Boom conceals bad decisions; best-looking lagging data coincides with peak concealed stress | GNPA confirm-only, never-leading design rule |
| Agency/career-risk incentives | Career horizon shorter than the cycle; asymmetric cost of a correct-but-early call | Mechanical, discretion-free architecture: frozen parameters, scheduled-review-only promotion |
| Over-reading an unvalidated phase read | Narrative capture applied to a new label before it earns trust | **Phase consumption gate**: quadrant/age logged, condition no rule until H66–H68 pass |

None of these seven countermeasures work by asking the operator to be wiser in the moment. Each
converts what would otherwise be a live judgment call into a structural non-decision — which, per
the psychology this Part documents, is the only form of debiasing that survives contact with an
actual credit cycle.
