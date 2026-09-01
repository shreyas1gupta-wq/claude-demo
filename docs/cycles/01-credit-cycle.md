# The Credit Cycle — Full Monograph (L10)

v2.0 · 2026-09-01 · The 20–30 page deep treatment (principal's depth directive), superseding v1.0
(whose core is preserved as Part 0). Chapter sources of record live in
`research/cycles/credit-deep/`; this file is the assembled monograph. Evidence rules: CONTRACT.md;
every [VERIFY] tag inside a chapter is an honesty marker, not a footnote. Real-data results (Part
B-RESULTS) come from the JST R6 mirror — advanced-economy PRIORS, never India results.

## Contents
- Part 0 — Executive summary and the state variable (v1 core: theory capsule, evidence table,
  India chronology, construction, designs R1–R7, synthetic demo)
- Part A+G — Theory in full (Fisher → Minsky → Kiyotaki-Moore → BGG → Geanakoplos →
  Brunnermeier-Sannikov → Adrian-Shin → Mian-Sufi → behavioral engine room) + operator psychology
- Part B — Cross-country: the panel studies in detail + ten case studies (incl. India, double length)
- Part B-RESULTS — first real data: J1–J5 on the JST R6 panel (AUROC, ST logit, R-zone, DD
  quintiles, H66 preliminary), trial-ledgered
- Part C — India data engineering: exact series, breaks, splices, vintage discipline
- Part D — The mathematics: HP demolition, Hamilton, AR(1) bias, AUROC=Mann-Whitney, Stambaugh,
  empirical Bayes, purged CV, DSR, bootstrap, hazards, why fixed weights
- Part E/F/H — the executable algorithm, the nine-consumer harvest map + designs R8–R10, and the
  knowledge ledger (established / pooled-prior / awaits-India / unknowable)

---

# PART 0 — Executive summary and the state variable (v1 core)

## 1. Theory — why credit cycles exist and why the signal survives being known

**The mechanism chain (Minsky → Kindleberger → modern evidence):**
1. **Stability breeds leverage.** After a calm stretch, lenders and borrowers both extrapolate:
   collateral values rise → loan-to-values look safe → credit standards ease → more credit bids
   up the same collateral. The loop is self-reinforcing on the way up (hedge → speculative →
   Ponzi finance, in Minsky's ladder of fragility).
2. **Fragility is built in the boom, revealed in the bust.** The stock of debt fixes future
   debt-service obligations against uncertain future income. When income growth disappoints or
   rates rise, the *marginal* borrower fails first, collateral is sold, and the collateral
   channel runs in reverse — which is why busts are faster than booms and why recessions after
   credit booms are deeper and longer (Jordà-Schularick-Taylor's "credit bites back").
3. **Why it isn't arbitraged away** (the Contract §5 survival argument, category i + ii):
   - *Behavioral*: Baron-Xiong show bank shareholders **neglect** the crash risk building during
     booms — expected returns on bank equity turn deeply negative after big credit expansions,
     yet the boom continues. The bias is in the credit *suppliers* themselves.
   - *Limits to arbitrage*: the trade against a credit boom is a multi-year, negative-carry,
     career-risk short of the most systemically-backed sector in the economy. Almost no
     institution can hold it to completion. Knowledge does not create capacity.
   - Consequence: the state is *publishable without dying* — the decay logic that kills
     cross-sectional anomalies does not mechanically apply (D03 §3, Edge A).
4. **What the signal is and is not**: it forecasts the **distribution** (crash probability, depth
   of drawdowns, forward risk premia), not the **date**. India timing uncertainty on a 7–11y
   object is measured in years. That is exactly why L10's harvest is REGIME (leverage/hedge
   permission), never a timing trade.

## 2. Evidence — the numbers this seat stands on

| Finding | Sample | Effect size | Source (verified in D03) |
|---|---|---|---|
| Credit growth → crisis probability | 14 economies, 1870–2008 | **+1σ real credit growth ⇒ +~2.8pp crisis probability over 5y**; credit beats money and CA measures | Schularick-Taylor, AER 2012 |
| Credit intensity → recession depth | >200 recessions, 14 countries | credit-intense expansions ⇒ deeper, slower recoveries, crisis or not | Jordà-Schularick-Taylor, JMCB 2013 |
| Leveraged bubbles | 17 countries since 1870 | credit-financed housing bubbles are the dangerous kind; unlevered equity bubbles far less so | JST, JME 2015 |
| Neglected crash risk | 20 countries, 1920–2012 | bank-credit expansion >95th pctile ⇒ **−37.3% predicted 3y bank-equity excess return**; investors don't demand compensation during the boom | Baron-Xiong, QJE 2017 [secondary spec −19.3%/8q: V] |
| Early-warning power | 26 economies, quarterly | credit-to-GDP gap **AUROC 0.83–0.85** at 3–5y horizons (best single indicator); debt-service ratio better <2y | Drehmann-Juselius, IJF 2014 |
| Joint credit+price booms | 42 countries, 1950–2016 | R-zone (credit top-quintile AND equity top-tercile, 3y) ⇒ **~40% crisis probability vs ~7% base** — the *combination* does the work | Greenwood-Hanson-Shleifer-Sørensen, JF 2022 |
| Household-debt channel | 30 countries, 1960–2012 | 3y Δ household-debt/GDP ⇒ lower growth 3–4y later + systematically biased forecasts | Mian-Sufi-Verner, QJE 2017 (→ L13, reduce-only) |
| Issuance quality | US corporates | junk share of issuance ⇒ low/negative forward credit returns | Greenwood-Hanson, RFS 2013 (India analogue thin: shallow bond market) |

**India-application haircut (stated, not hidden):** the pooled AUROC 0.83–0.85 is treated as an
upper bound; the working India prior is **0.65–0.75 [A]** (pooling dilution + thin domestic
sample + regime differences), superseded by the first purged India-conditioned estimate (§5, R1).

## 3. India chronology — what the domestic record actually contains (D03 §I5)

| Phase | Years | Character | Free-data marker |
|---|---|---|---|
| Post-liberalization NPA cleanup | 1992–2002 | recognition norms bite; PSB GNPA 19%→12% | RBI GNPA series |
| Credit boom | 2003–08 | credit +25–30%/yr peaks; infra/real-estate surge; GNPA masked to ~2% | DBIE non-food credit |
| GFC pass-through + re-acceleration | 2008–11 | stimulus re-inflates; the next bust is seeded | DBIE, sectoral deployment |
| Twin Balance Sheet | 2011–15 | corporate over-leverage + hidden bank stress ≈12% of loans | Economic Survey 2016-17 |
| AQR recognition shock | 2015–18 | forced reclassification: GNPA 5.1%→11.2% — a **measurement break, not a credit event** (splice discipline) | RBI FSR |
| IL&FS / NBFC crisis | 2018 | shadow-credit funding freeze; **invisible in bank-only credit** → the bank+NBFC aggregate rule | FSR NBFC ch., CCIL CP |
| COVID | 2020 | credit collapse + forbearance masking | DBIE, FSR |
| Unsecured-retail boom | 2021–24 | credit 16→20%/yr, unsecured-heavy; CD ratio ~80% (highest since 2005); household debt 26%→42%/GDP | DBIE; FSR |
| Macroprudential response | Nov 2023 | RBI +25pp risk weights on unsecured/NBFC — the regulator confirming the composition signal | RBI circular |
| Current | 2024–26 | GNPA decadal best (2.15%) — a *lagging* comfort; CD ratio elevated | FSR |

**Clock-test verdict:** at most **1–2 completed down-legs** post-1991 (TBS/AQR/IL&FS reads as one
prolonged episode; COVID is policy-shaped). The credit cycle is a **state variable, pooled on the
JST panel** — never a domestic clock. This single count drives everything: Tier B, frozen
parameters, partial pooling, no fitted regime switching (<10 transitions).

## 4. The state variable — exact construction (what the module implements)

Four inputs, one composite, one clamp:

1. **Credit/GDP gap (own construction)** — bank+NBFC credit ÷ nominal GDP, Hamilton-filtered
   (expanding mode; h ∈ {16–24q} grid pre-registered, p=4; NEVER the BIS HP-filtered series,
   which is used only as an external cross-check). 2026 GDP-rebase splice applies.
   *Measured dynamic (synthetic run, 10/10 seeds):* the EXPANDING-mode gap is an
   **acceleration-surprise detector, not a level gap** — it fires positive in the boom's
   build-out, decays toward zero late in the boom as the expanding regression absorbs the new
   growth rate, and collapses hard (largest-magnitude reading of the whole cycle) at the bust
   **onset**, when forecasts made at the peak extrapolate the boom against contracting actuals.
   This differs from the full-sample/BIS-style level gap and is the honest real-time behavior.
2. **Credit-deposit ratio percentile** — expanding-window percentile of the CD ratio (monthly,
   1969→; long-run range ~51.6%–~80%). Virtue: no GDP denominator → no revision noise. Carries
   the boom-**maturity/level** information the expanding gap deliberately does not: the two
   inputs are impulse (1) and level (2) — complements by construction, which reframes R5 from
   "are they redundant?" to "does the impulse add turn-timing on top of the level?".
3. **Issuance/composition quality** — share of incremental credit to unsecured retail + NBFC
   (sectoral deployment data), percentile rank. Tier C → clamped non-positive.
4. **GNPA trend** — *lagging confirm only*: never a leading input; enters as a confirmation dummy
   for de-risking states, never for re-risking.
Composite: weighted average of (1) and (2) (weights inside the macro-block budget, pre-registered
grid), with (3) clamped to min(0, reading) per the Tier-C rule, (4) as confirm. Output: a
percentile-ranked credit state ∈ [−1, +1] feeding the macro-credit block (≤20% of regime score).

**What moves the book:** high credit state (boom maturing) ⇒ leverage permission decays toward
1.0x, hedge floor rises one bucket earlier, tail-sleeve entries slow, quality-sleeve floor binds.
It never shorts the boom and never times the top.

**Phase enrichment (2026-09-01 directive):** the composite is additionally carried as a phase
object — (level, velocity, quadrant, age) per `quant/ladder/phase.py` and
`ladder.yaml state_phase_convention` — because the same level means different things by trail
(0.6U ≠ 0.6D; hysteresis). On the synthetic economy the CD-percentile leg reads U through 100% of
the boom and D through 100% of the turn window (seeds 0–7). Quadrant/age may not condition any
traded rule until H66–H68 pass; see the decision record in research/OPEN_QUESTIONS.md.

## 5. Pre-registered regression designs (frozen here; run on fixtures)

| # | Design | Specification (fixed before data) | Decision rule |
|---|---|---|---|
| R1 | **India-conditioned AUROC** | Label: qualifying episodes (§DESIGN 5.6 set) within 3y/5y. Score: composite state. Purged CV 4–6 folds, embargo 2×τ½. Pooled JST prior via empirical-Bayes w = τ²/(τ²+σ²_India) | AUROC CI vs the 0.65–0.75 prior → replaces it in `ladder.yaml`; <0.55 lower-CI ⇒ block weight cut, macro budget redistributed |
| R2 | **Forward drawdown regression** | 3y max-DD on state percentile, Stambaugh-corrected (persistent regressor), Newey-West h−1, block-bootstrap CIs | slope sign+CI documented; feeds the R-bucket boundary quantiles (never a point threshold) |
| R3 | **R-zone replication (India)** | Joint condition: credit-growth top quintile AND trailing 3y equity return top tercile (full-sample expanding ranks) | frequency table only (n tiny); India R-zone dates listed and compared to episode set |
| R4 | **Hamilton h selection** | h grid {16,20,24}q × CV vs pooled crisis labels (trial ledger #4) | best-h by OOS AUROC, reported with the full grid |
| R5 | **CD-ratio vs gap redundancy** | correlation + spanning of the two inputs' predictive content | if redundant (ρ>0.8, no incremental AUROC), CD ratio becomes the primary (faster, cleaner) and the gap the check |
| R6 | **τ½ + drift (H65b)** | bias-corrected AR(1) on the composite, rolling windows across 1991/2003/2008/2016/2020 breaks; lengthening-trend test | τ½ CI → `ladder.yaml` L10; drift result sets re-estimation cadence |
| R7 | **Composition-signal event check** | 2018 IL&FS and 2023-24 tightening as held-out validation targets, pre-named (no hindsight construction) | did the composition percentile lead the events? documented either way |

Minimum economic effect (from the cost stack): the state earns its block weight only if acting on
it (leverage/hedge deltas across its range) improves episode-conditional DD without costing more
than the §1.1 risk-drag budget — evaluated in the M4 walk-forward, not as a standalone Sharpe.

## 6. What can be known today vs what awaits data

**Known today [theory/X]:** the mechanism chain (§1), pooled effect sizes (§2), the survival
argument, the construction (§4), the designs (§5), and a working module verified end-to-end on a
synthetic boom-bust economy (§7).
**Awaits fixtures [their machine]:** every India coefficient — AUROC, slopes, τ½, h, weights.
**Never knowable:** the date of the next turn. The seat is built so that not knowing it is
survivable — that is the whole design.

## 7. Synthetic demonstration (runs in this repo, zero market data)

`scripts/analyze_credit_cycle.py --demo` builds a synthetic boom-bust economy (credit expands
faster than income for years, then contracts; deposits lag), runs the exact module, and shows:
the gap fires during the boom's build-out and collapses at the turn, the CD percentile saturates
high late in the boom, the composite state is materially higher through the boom than at the
bust onset and after deleveraging, and the Tier-C composition input can never lower the
composite below the renormalized two-input base (the clamp — the consistency audit's C2 finding,
now enforced in code). One assertion originally written here ("the gap rises **through** the
boom") was falsified by the run and replaced with the measured acceleration/turn shape (§4.1
note) — recorded in the verification log rather than silently retro-fitted.
Demo output: `research/cycles/01-credit-cycle-DEMO.md` (marked SYNTHETIC). Tests:
`tests/test_credit_cycle.py`, including the no-look-ahead property on both inputs.



---

# PART A + G — Theory and operator psychology

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



---

# PART B — The cross-country record

# PART B — The Cross-Country Record

*Credit-cycle monograph · Part B of III · v1.0 · 2026-09-01 · Author: Claude (research agent) for Ionic quant desk (principal: gaurav@ionic.in)*
*Governed by `research/CONTRACT.md`. Every number below is search-verified as of Sept 2026 unless tagged `[VERIFY: ...]`. Internal cross-references are to `docs/cycles/01-credit-cycle.md` ("D03/L10 dossier"), which this Part supplies the underlying evidence for.*

---

## B1. The panel evidence, in detail

### B1.1 The Jordà–Schularick–Taylor Macrohistory Database

The JST Macrohistory Database is the single largest free, public panel of long-run macro-financial
data and is the reason the Contract's estimation standards (§9) instruct pooling "where India alone
offers <2 cycles." It is maintained by Òscar Jordà (SF Fed / UC Davis), Moritz Schularick (Kiel
Institute / Bonn), and Alan M. Taylor (UC Davis), hosted at the MacroFinance & MacroHistory Lab.

**Contents.** The current release (**R6**) covers **18 advanced economies since 1870** on an annual
basis (Ireland was added in R6, using land-price and credit series reconstructed by Ronan Lyons and
Trinity College Dublin) — earlier releases (R4) covered **17 economies, 1870–2016**. The panel holds
**45 real and nominal variables**: real/nominal GDP, real GDP per capita (Maddison-linked), real
consumption per capita, investment/GDP, population, unemployment, wages, current account and
trade flows, narrow and broad money, short- and long-term interest rates, **total bank loans, and
loans split into mortgage vs. business credit** (`tloans`, `tmort`, `tbus`), nominal house prices,
and total-return series for equities, housing, bonds, and bills — plus a hand-curated systemic
banking-crisis dummy (`crisisJST`) built from the narrative crisis-dating literature. This is the
only free dataset that lets a researcher build a "credit/GDP gap" or "excess credit" measure
consistently across 150+ years and 18 countries, which is exactly the design pattern the L10 module
pools on.

**Release history.** Versions have been numbered R1 through R6; R3 was the version publicized as
"online" in 2016, R4 (17 countries, through 2016) was current through roughly 2019, and R6 —
current as of this writing, with its documentation PDF dated February 2023 and an update note
covering "2016–2020" — added Ireland and extended coverage. `[VERIFY: exact publication dates and
country counts for R1, R2, and R5 — the Lab's own changelog was not directly accessible from this
environment; the R3→R4→R6 sequence above is corroborated by independent citations across at least
six unrelated GitHub repositories and course materials.]`

**How to download it, free, today.** The authoritative page is
`https://www.macrohistory.net/database/` (database home: `https://www.macrohistory.net/`), which is
**not reachable from this research environment's network egress** (confirmed: direct fetch attempts
to `macrohistory.net` and to `bis.org`, `nber.org`, `frbsf.org`, `hbs.edu`, and
`schmoelders-stiftung.de` were all blocked by the proxy in this session). The dataset is released
under **Creative Commons BY-NC-SA 4.0** (free to use with attribution, non-commercial, share-alike).
Two free routes work from this environment:
1. **Direct download link** (confirmed live and cited verbatim by at least seven independent
   downstream projects between 2021 and 2024):
   `https://www.macrohistory.net/app/download/9834512569/JSTdatasetR6.xlsx` — an `.xlsx` workbook
   with a `Data` sheet; a `.dta` (Stata) version exists at the equivalent `/JST/JSTdatasetR6.dta`
   path on the same host.
2. **GitHub mirrors** — see the dedicated side-task section at the end of this document; several
   researchers have committed real copies of R3/R4/R6 data (not merely download scripts) directly
   into public repositories, and those are reachable via `raw.githubusercontent.com` even when
   `macrohistory.net` itself is not.

### B1.2 Schularick & Taylor, *AER* 2012 — "Credit Booms Gone Bust"

**Sample.** 14 countries, 1870–2008 (the original core of what became the JST panel).
**Specification.** A pooled logit (cross-checked against probit; results near-identical) of a
systemic banking-crisis onset dummy on **five annual lags of real credit growth** (bank loans
deflated by CPI), estimated first without and then with country fixed effects, and compared against
an equivalent specification using broad-money growth in place of credit growth. **Headline result:**
the summed marginal effect across the five credit-growth lags is **0.301** in their preferred
specification — i.e., a sustained acceleration in real credit growth raises the estimated
probability of a crisis within the following years by an economically large amount — while the
broad-money specification is materially weaker once credit is included. **"Credit beats money"**
operationally means: when both loan growth and money-supply growth are entered as competing (or
jointly estimated) predictors of crisis onset, the credit-growth lags retain statistical and
economic significance while money's incremental predictive content is small — i.e., it is the asset
side of the banking system's balance sheet (loans), not the liability side (deposits/money), that
carries the crisis signal. Fit statistics reported across the paper and its replications converge
on an **AUROC in the neighborhood of 0.70–0.72** for the baseline in-sample logit (one closely
related specification reports 0.717, another 0.697 with a standard error of 0.039); extensions and
replications testing genuine out-of-sample / pseudo-out-of-sample performance report a **wider band,
roughly 0.66–0.79** depending on sample split and country coverage. `[VERIFY: the exact AUROC table
cells as printed in the original AER article — the primary PDF was not reachable from this
environment (egress-blocked on aeaweb.org, frbsf.org, and independent mirrors); the range above is
triangulated from the replication literature (Summers 2017, *J. Applied Econometrics*) and citing
papers, not read directly off Table 3 of the original.]` This is the number the D03/L10 dossier
already treats as its cross-country prior (stated there as "~0.72 in-sample, 0.66–0.75 range
out-of-sample"); this section corroborates but does not independently re-derive it to the decimal.

### B1.3 Jordà, Schularick & Taylor, *JMCB* 2013 — "When Credit Bites Back"

**Method, in one paragraph.** Rather than fit a single VAR and read off impulse responses at
increasing lag lengths (which forces every horizon through the same dynamic structure), the paper
uses **local projections** (Jordà 2005): for each forecast horizon *h* separately, regress the
future path of an outcome (GDP, investment, bank lending, short rates, inflation) on today's
"excess credit" measure (the deviation of pre-recession credit growth from its historical norm)
plus a battery of macro controls, and read the estimated coefficient at each *h* as the local
projection's impulse response at that horizon. This lets the recovery *path* bend freely rather
than being forced into a single linear dynamic system, which matters because recoveries after
credit busts are empirically **non-linear and asymmetric** relative to normal-recession recoveries.
**Headline path differences (14 advanced countries, 1870–2008):** recessions preceded by more
credit-intensive expansions are systematically **deeper and slower to recover from — whether or not
the recession is accompanied by a systemic financial crisis** — and the worst outcomes of all are
recessions that are *both* preceded by excess credit *and* coincide with a financial crisis. This is
the paper the D03 dossier's mechanism chain leans on directly ("credit-intense expansions ⇒ deeper,
slower recoveries, crisis or not") and it is the single strongest justification in this literature
for why L10 sizes leverage/hedge permission off the **boom's** credit intensity rather than waiting
to identify the trigger of the bust.

### B1.4 Drehmann & Juselius, *IJF* 2014 — "Evaluating Early Warning Indicators"

**Indicators tested.** Credit-to-GDP gap, the debt-service ratio (DSR), credit growth, real
property-price growth, and several composite/combination indicators, evaluated across **26
economies at quarterly frequency**. **Method structure.** Rather than reporting AUROC alone, the
paper explicitly builds the evaluation around a **policymaker's loss function** — trading off
missed crises (Type I) against false alarms (Type II) at policy-relevant horizons (typically 1–5
years before a crisis), and reports AUROC, the noise-to-signal ratio, and stability/interpretability
criteria side by side at each horizon, for each candidate indicator. **Policy conclusion, stated
directly:** the **credit-to-GDP gap dominates at longer horizons (roughly 3–5 years ahead)**, making
it the right variable for setting a slow-moving instrument like the countercyclical capital buffer,
while the **debt-service ratio dominates at short horizons (under about 2 years)**, making it the
better near-term trigger signal once a boom is already mature. The D03 dossier carries forward a
pooled AUROC of **0.83–0.85** at the 3–5-year horizon for the credit-to-GDP gap as this literature's
best single-indicator result; that figure is treated there as **already verified** in the prior
research pass and is repeated here as the working cross-country prior, with the explicit caveat
that the primary BIS working-paper table (`bis.org/publ/work421.pdf`) was **not independently
re-readable from this environment** (egress-blocked) in this pass. `[VERIFY: re-confirm the exact
0.83–0.85 cell values against the original Table 4/5 of Drehmann–Juselius (2014) the next time
bis.org is reachable.]`

### B1.5 Greenwood, Hanson, Shleifer & Sørensen, *JF* 2022 — "Predictable Financial Crises"

**R-zone definitions.** A country enters the **business R-zone** when non-financial-business credit
growth over the trailing **3 years** is in the **top quintile (top 20%)** of the full historical
distribution **and** stock-market returns over the same 3-year window are in the **top tercile (top
third)**. The **household R-zone** is defined symmetrically: household-credit growth over the
trailing 3 years in the top quintile, jointly with equity returns in the top tercile over the same
window. Both zones combined occur in **fewer than 10% of all country-years** in their sample.
**Headline probabilities.** The probability that a country in the **business R-zone** experiences a
major financial crisis within the next 3 years is **~45%**; the paper's topline combined figure
(spanning both the business and household variants) is that being in *either* R-zone carries roughly
a **40% probability** of a crisis within 3 years, against a **base rate of roughly 7%** in "normal
times" when neither credit nor asset-price growth is elevated. `[VERIFY: the household-R-zone-only
probability distinct from the 45% business figure and the blended 40% figure — sources consistently
confirm 45% (business) and 40% (combined/topline) but the search record did not surface a cleanly
separate household-only percentage; treat 40% as the best available household-adjacent estimate
until the original Table can be read directly.]` **The predictability claim.** The paper's explicit
argument is that severe financial crises are **not** unforecastable "bolts from the blue" arriving
without warning — a joint credit-and-asset-price overheating condition, observable in real time with
public data, precedes a large share of postwar crises with a hit rate far above the unconditional
base rate. `[VERIFY: the precise phrase used in the paper for the "bolts from the sky/blue" contrast
— this is a well-known characterization in the crisis-prediction literature generally (often
associated with Bernanke's commentary on the 2008 crisis) but the exact wording and attribution
inside this specific paper was not independently confirmed from the sources reachable here.]` This
is directly relevant to L10's pre-registered **R3** design (a same-construction R-zone replication on
India), and the joint-condition structure (credit **and** price, not credit alone) is one of the
strongest pooled findings carried into B3 below.

### B1.6 Mian, Sufi & Verner, *QJE* 2017 — "Household Debt and Business Cycles Worldwide"

**Sample and finding.** An unbalanced panel of **30 countries, 1960–2012**: a rise in the household
debt-to-GDP ratio over a 3-year window predicts **lower GDP growth and higher unemployment 3–4 years
later**, operating primarily through a subsequent consumption slowdown, and the effect is stronger
where mortgage credit supply (proxied by low mortgage spreads, used as an instrument) expanded fastest
— consistent with a "credit supply," not "credit demand," origin. **The forecast-bias finding.**
Professional forecasters (the paper specifically implicates the **IMF and OECD**'s own growth
forecasts) systematically **under-weight** the information in rising household-debt-to-GDP when
projecting medium-term growth — i.e., the household-debt buildup predicts *both* the future growth
slowdown *and* the forecasting institutions' own forecast errors, meaning the market's/institutions'
consensus view does not fully price in a mechanism the authors can show is statistically live.
`[VERIFY: the precise magnitude of the average IMF/OECD forecast-error attributable to household-debt
buildup — the qualitative finding ("OECD/IMF systematically miss it") is well confirmed across
multiple independent sources including the authors' own 2018 IMF-Global-Debt-Database extension, but
a single clean point-estimate of the average forecast miss in percentage points of GDP was not
located.]` The D03 dossier correctly routes this finding to **L13 (reduce-only)** rather than into
L10 itself, since it is a *household*-debt-specific channel distinct from the aggregate
bank+NBFC credit measure L10 is built on.

### B1.7 Krishnamurthy & Muir — "How Credit Cycles across a Financial Crisis" (NBER 2017 → *JF* 2025)

Credit **quantities** (loan growth, credit/GDP) move slowly and are observed with a lag; credit
**spreads** (the gap between risky and safe borrowing rates) are priced continuously in liquid
markets and can be read in real time. The paper's contribution is to show these two are
**complements, not substitutes**: precrisis credit **spreads compress to unusually low levels
while quantities (credit growth) simultaneously accelerate** — a "quiet before the storm" signature
— and the eventual crisis's **severity** is best predicted by the *interaction* of (a) how far
spreads subsequently spike once the crisis hits and (b) how much precrisis credit growth had built
up financial-sector fragility beforehand. Quantitatively: a **one-standard-deviation increase in
the crisis-period spread widening is associated with an 8.2% decline in cumulative 5-year GDP
growth**, versus only a **3.1% decline** for an equivalent one-sigma spread move in a comparable
*non-financial* recession — i.e., the same-sized price shock does roughly **2.6× the damage** when
it originates in a credit boom's unwind. **What spreads add beyond quantities:** because they are
market-priced daily, spreads can serve as a **fast, real-time confirming (or disconfirming) signal**
layered on top of a necessarily slow-moving, backward-looking credit-quantity state variable — a
compression phase flags boom-era complacency the quantity measure may still be reading as merely
"elevated but not yet extreme," and a spread spike is one of the fastest available signals that a
credit bust has actually begun, well before quarterly GDP or bank-reported NPA data would confirm it.

### B1.8 Baron, Verner & Xiong, *QJE* 2021 — "Banking Crises Without Panics"

**Sample.** A novel hand-built dataset of bank-equity returns for **46 countries, 1870–2016**,
combined with narrative panic dating. **The crisis marker.** The paper defines a banking crisis by
a **bank-equity index decline of more than 30%** — a purely market-based, objectively computable
threshold — rather than requiring a narrative-identified depositor run or panic event. **Headline
finding:** a 30% bank-equity decline **with** an accompanying panic predicts a **−3.4% real GDP**
outcome three years later; the same 30% bank-equity decline **without any panic at all** still
predicts a **−2.7% real GDP** outcome three years later — roughly **80% of the full damage, with no
panic required**. The same threshold event, panic or not, predicts a **−5.4% decline in bank
credit/GDP** three years out. **Implication for using bank equity as a free, real-time indicator:**
because panics amplify damage but are **not necessary** for it, a simple, continuously-priced,
free-to-observe series — the banking-sector equity index — is itself an actionable crisis marker
that does not require waiting for a run, a narrative event, or a lagging NPA print to confirm
distress. For India this argues for tracking a **bank-sector equity index (e.g., Nifty Bank / Bank
Nifty relative to Nifty 500)** drawdown explicitly as a fast, free, real-time confirming layer
alongside L10's credit-quantity inputs, in the same complementary spirit as the Krishnamurthy–Muir
spread signal in B1.7.

---

## B2. Ten case studies

Each case reports: the build-up, the trigger, the bust (equity max drawdown, GDP hit, duration), the
resolution style, and **one design implication** for the L10 state variable.

### 1. United States, 2008 (with 1929 and the S&L crisis as priors)

**Build-up.** US household debt rose from roughly **70% of GDP in 2000** to a peak near **98–99% of
GDP** by 2007–08 `[VERIFY: exact peak-quarter value on FRED series HDTGPDUSQ163N — the series is
confirmed to exist and the qualitative "major spike leading into 2007–08" is confirmed, but a single
precise peak percentage was not independently pulled from a live FRED read in this environment]`,
driven by a mortgage-credit boom (subprime origination, private-label securitization) increasingly
funded off-balance-sheet through shadow-banking channels (ABCP conduits, repo, SIVs) that sat outside
conventional bank-credit statistics. **Trigger.** Rising subprime delinquencies through 2006–07,
the collapse of two Bear Stearns hedge funds (mid-2007), and the **Lehman Brothers bankruptcy on
15 September 2008**. **Bust.** The **S&P 500 fell 56.8% peak-to-trough (October 2007 to March
2009)** — the largest drawdown since WWII; **real GDP fell 4.3% peak-to-trough (2007Q4 to 2009Q2)**,
the deepest postwar US recession; unemployment rose from under 5% to 10%; the NBER-dated recession
ran **18 months** (Dec 2007–Jun 2009). **Resolution.** TARP capital injections, Fed zero rates and
quantitative easing, coordinated bank stress tests (2009) forcing recapitalization, and a
multi-year, policy-engineered deleveraging — slow by design, but decisively faster and more
transparent than Japan's.

**1929 as a prior.** The Dow fell **89% from its September 1929 peak to its July 1932 trough**; real
GDP per capita fell **~30% (1929–33)**; unemployment rose to **over 25%**. Absent deposit insurance
or a reliably activist lender of last resort, banking panics compounded the initial credit bust; the
Dow did not regain its 1929 high until **1954** — a 25-year round trip.

**The S&L crisis as a prior.** Between 1986 and 1995, **1,043 of roughly 3,200** US savings & loan
institutions failed, at a final cost to taxpayers of **$123.8 billion by 1999** (plus $29.1bn absorbed
by the industry itself) — driven by 1980s deregulation combined with an interest-rate/duration
mismatch and speculative real-estate lending, resolved first by the FSLIC and then, at scale, by the
Resolution Trust Corporation.

**Design implication.** The US had *already* run almost exactly this pattern (real-estate-linked
credit boom → duration/liquidity mismatch → deposit-taking-institution failures) twenty years before
2008, and prior experience of a severe credit-cycle bust did **not** prevent a bigger repeat — a
caution against assuming "we've been through this before" reduces risk; parameters must stay frozen
and rules-based (per the Contract's Tier-B discipline) rather than tuned to a belief that the last
lesson has been fully learned. Separately, because the 2008 boom's most dangerous leverage sat in
off-balance-sheet, non-bank vehicles, a credit-cycle state variable measured on **on-balance-sheet
bank credit alone would have materially understated the true state** — directly reinforcing L10's
bank+NBFC aggregation rule.

### 2. Japan, 1986–1990 boom and the lost decades

**Build-up.** Bank lending to real estate roughly **doubled between 1985 and 1990**, pushing the
aggregate loan-to-GDP ratio **past 100%**; commercial land prices in Japan's six largest cities rose
**over 300%** before their collapse, making this "the most extreme documented land bubble in modern
history." Loose post-Plaza-Accord monetary policy financed the boom.

**Trigger.** Bank of Japan tightening through 1989–90 and Ministry of Finance quantity controls on
real-estate lending (1990).

**Bust.** The **Nikkei 225 fell roughly 80% from its 29 December 1989 intraday peak of 38,957 to
around 7,600–7,831 by 2003** — a 14-year drawdown, later extending to an ~82% trough in 2008;
commercial land prices eventually fell **70–80% from peak** over roughly 14 years. Critically, there
was **no single sharp GDP-collapse year** comparable to the other cases in this record: real GDP
growth simply collapsed to an average of **~1.5%/year (1990–95)** and **~0.99%/year (1992–2001)** —
a multi-decade growth drag rather than a drawdown event.

**Resolution.** Banks were permitted to "evergreen" impaired loans for years (the canonical
zombie-lending pattern) with no aggressive forced recapitalization until the Takenaka reforms of the
early 2000s; the Bank of Japan did not adopt zero rates and quantitative easing until 1999–2001 —
roughly a decade after the bust began.

**Design implication.** Japan is the canonical proof that a credit cycle does not need a sharp
equity/GDP crash to be extremely costly — the relevant loss here is the multi-year **growth drag**,
which a state variable tuned only to detect drawdowns will miss entirely. This directly motivates
L10's de-risking signal firing on **boom maturity itself**, not only on an observed trigger, and it
is the closest cross-country analogue to India's own multi-year AQR-recognition delay (case #10):
delayed recognition can convert a moderate credit event into a decade-plus low-growth regime.

### 3. United Kingdom (1973 secondary banking crisis + 2008 variant)

**1973–74.** Property lending rose **more than eightfold from 1970 to 1974**; residential prices
doubled and commercial prices trebled over the same window, funded by "secondary" (non-clearing)
banks that had overtaken the high-street clearers as the principal property lenders. The trigger was
the 1973 oil shock combined with Bank of England tightening and a property-price reversal. The Bank
of England assembled a "lifeboat" (28 December 1973): the clearing banks, under BoE coordination,
extended **£1.3 billion (~1% of GDP) to 26 supported institutions**, with the BoE indemnifying losses
beyond a threshold. UK equities fell sharply over 1972–74 in one of the worst bear markets in UK
market history `[VERIFY: the precise peak-to-trough percentage for the FT 30/FT All-Share index
1972–74 — sources describe this qualitatively as the UK's worst post-war crash but a single
confirmed percentage figure was not independently re-derived here]`. Crucially, the **final cost to
the taxpayer was only £55 million** — the lifeboat was a liquidity bridge for a contained, "fringe"
segment of the banking system, and most assets were eventually worked out.

**2008.** Northern Rock suffered the **first run on a British bank in 150 years**; the government
ultimately injected **over £35 billion** into RBS, Lloyds TSB, and HBOS, fully nationalizing Northern
Rock and Bradford & Bingley and taking majority ownership of RBS. The **FTSE 100 fell 31% over 2008
alone**; **UK GDP fell 6.5% peak-to-trough (2008 Q2 to 2009 Q3)** — the deepest UK recession since
WWII.

**Design implication.** The same country, the same underlying asset class (property-linked lending),
produced a taxpayer cost of **£55 million** in 1973 versus **tens of billions of pounds** in 2008 —
the difference being whether the credit boom sat in a small, contained "fringe" of the system (1973)
or had grown to systemic, wholesale-funded scale (2008). This supports keeping an explicit
**composition/concentration** read (is credit growth concentrated in institutions that are large and
interconnected enough to threaten the system?) alongside the aggregate credit/GDP level — the same
logic underlying L10's Tier-C issuance/composition input.

### 4. Spain, 2000s (cajas, construction, the euro constraint)

**Build-up.** Private-sector credit/GDP **nearly doubled between 2000 and 2007**; credit growth
peaked **above 25%/year in 2006**, with **15 percentage points of that growth coming from
housing/construction/property development** alone; real house prices rose **over 150% (1998–2007)**
and **71% just between 2003 and 2008**; construction reached **~17% of GDP** and **~12% of
employment**, with residential investment at **15.7% of GDP** and annual housing construction
exceeding **one million units — more than Germany, France, and the UK combined**. The main conduit
was the **cajas** (regional, politically-governed savings banks whose incentives were tied to local
economic expansion). Euro membership removed Spain's own interest-rate and exchange-rate valves —
ECB policy, set for the euro area as a whole, was far too loose for Spain's domestic boom.

**Trigger.** The 2008 global financial crisis freezes wholesale funding; construction demand
collapses.

**Bust.** Unemployment rose from **8.2% (2007) to a peak of 26.3% (spring 2013)**; real GDP fell
**~7.5% cumulatively from 2008 to 2013** in a double-dip recession; the **IBEX 35 fell ~50%
peak-to-trough (November 2007 to October 2008)**, with weakness persisting into 2012; the cajas
sector was effectively wiped out and forced into consolidation (Bankia and others), requiring an
EU-funded, banking-sector-specific bailout in 2012 `[VERIFY: the precise EU/ESM bailout amount for
Spain's banking sector — figures in the €40–100bn range are widely cited but a single confirmed
number was not independently pulled here]`.

**Resolution.** A "bad bank" (SAREB, 2012) absorbed the cajas' impaired real-estate assets under the
EU program; unemployment remained elevated for a decade.

**Design implication.** Euro-area membership removed the normal monetary safety valve, letting the
boom run longer and end worse than it would have under an independent currency. India is not in a
currency union, but the underlying lesson generalizes: watch for credit growth concentrating in a
**policy-privileged, rate-insensitive channel** (cajas/construction in Spain; unsecured
retail/NBFC in India, case #10) as a distinct composition warning, separate from the aggregate level.

### 5. Sweden, 1990–1992 (the model resolution)

**Build-up.** Financial deregulation in the mid-1980s inflated a real-estate and credit bubble.
**Trigger.** A speculative attack forced the krona off its currency peg on **19 November 1992**.
**Bust.** Bank credit losses totaled **17% of outstanding lending**; real GDP contracted a cumulative
**5.1% from 1991 to 1993**; two of the largest banks (Nordbanken, Gota Bank) required state rescue.

**Resolution — the model case.** Sweden moved **fast**: a **blanket government guarantee** of all
bank liabilities (1992), nationalization of Nordbanken, and the creation of **Securum** — a dedicated
"bad bank" (built on a McKinsey proposal informed by the US S&L/RTC precedent) that took over and
progressively liquidated distressed real-estate collateral. The **gross initial cost was 3.5–4.5% of
GDP**, but because recognition was immediate and transparent, and because the floated krona quickly
restored export competitiveness, the **net cost had fallen to just 1.5% of GDP by 1997** once asset
sales and bank-share disposals were counted.

**Design implication.** Sweden is the cleanest natural experiment in this record for the claim that
the fiscal/growth **cost of a bust is not fixed by the boom's size — it is highly sensitive to
recognition speed**. Fast, transparent recognition (Sweden) converted a severe bust into a 2–3 year
event with most of the fiscal cost recovered; slow recognition (Japan, case #2; India's TBS era,
case #10) converted comparable or smaller stress into a multi-year drag. L10's job is therefore not
only to size the pre-bust boom but to reward/require fast de-risking once a bust is confirmed.

### 6. Thailand, Korea, and Indonesia, 1997 (the external-funding/currency-mismatch variant)

**Build-up.** All three ran pegged or tightly-managed exchange rates that encouraged **unhedged
foreign-currency borrowing** by banks and corporates (Thai finance companies, Korean chaebol,
Indonesian conglomerates) against domestic-currency revenue — a **currency-mismatch** structure
fundamentally different from the domestic-currency credit booms in cases 1–5.

**Trigger.** Thailand devalued the baht **15–20% on 2 July 1997**; contagion spread regionally within
weeks.

**Bust.** Currency collapses were severe: the **Indonesian rupiah fell over 80%**; the **Korean won
lost almost half its value**. Equities: **Thailand's SET index fell 55.2% in 1997 alone (a further
4.5% in 1998, ~59% combined)**; **Korea's KOSPI fell 27% in the October 1997 crisis month alone**
(with deeper cumulative losses over the full episode) `[VERIFY: KOSPI and Jakarta Composite
cumulative peak-to-trough percentages across the full 1997–98 episode — regional markets are
reported to have "lost up to 70% of their value by early 1998" in aggregate, but clean single-index
cumulative figures for Korea and Indonesia specifically were not independently confirmed here]`. Real
GDP fell **13.0% (Indonesia, 1998)**, **10.2% (Thailand, 1998)**, and **~7% (Korea, 1998)**. The IMF
assembled support packages of **$20bn (Thailand), $40bn (Indonesia), and $59bn (Korea)**.

**Resolution.** IMF-conditioned programs (fiscal tightening, high rates, bank closures, corporate
debt restructuring). Korea staged the sharpest recovery — **10–11% growth in 1999** — helped by won
devaluation restoring export competitiveness and aggressive chaebol debt-equity restructuring;
Thailand and Indonesia recovered more slowly, Indonesia compounded by the political fall of Suharto.

**Design implication — the EM-specific channel India must watch.** This crisis mechanism is
fundamentally different from every other case in this record: the trigger is **currency mismatch
under a pegged exchange rate**, not simply excess domestic credit growth. A state variable built
only on domestic rupee bank+NBFC credit is **structurally blind** to a 1997-style bust building
through offshore borrowing (ECBs, FCCBs, USD-denominated NBFC wholesale funding). This is the
argument for a **separate external-vulnerability gauge** (short-term external debt/reserves,
corporate currency mismatch) sitting **alongside, not inside,** L10's domestic credit-cycle state.

### 7. China, 2009–present (the largest credit boom in history — outcome still unknown)

**Build-up.** Post-GFC stimulus (2008–09) launched what is, on a credit/GDP-change basis, **the
largest credit boom in the JST-comparable historical record**: China's total non-financial-sector
debt/GDP roughly **doubled from ~135% (2008) to ~269% (2020)**, and stands near **296% as of Q3
2025**. The channels: **Local Government Financing Vehicles (LGFVs)**, used as a workaround after
local governments were barred from direct borrowing and secured against land sales, reaching an
estimated **51% of GDP (~$10.4 trillion, IMF)** by 2025; the **property sector**, which together with
related industries reached **~25–30% of GDP** (and **31.7%** including infrastructure in 2021); and
**shadow banking** (trust-company lending to property alone reached roughly **RMB 2 trillion**),
which financed developers such as Evergrande.

**Trigger.** Beijing's "three red lines" policy (2020) capped developer leverage and tightened
property-sector credit access.

**Bust.** **Evergrande defaulted on $305 billion (~2% of China's 2021 GDP)** in 2021; **50+ other
developers** subsequently defaulted. Property investment fell **10.0% in 2022** (the first annual
decline since records began in 1999) and a further **7.9% in H1 2023**; sales by floor area fell
**24.3% in 2022**; from their mid-2021 peak, monthly housing sales are down **more than half**, real
estate development activity down **about a third**, and housing starts down **roughly two-thirds**.
Notably, **no market-wide equity crash or currency collapse accompanied this bust** — capital
controls and a state-directed financial system mean the transmission runs through property-sector
activity, local-government finances, and consumer sentiment rather than through the free-floating
equity/currency channels this literature is otherwise calibrated on.

**Resolution style.** A managed, gradual deflation attempt — state-directed developer support, local
government debt swaps — neither Sweden's fast recognition-and-recapitalization nor Japan's
multi-decade denial, but something in between, and **still unfolding as of 2026**.

**Honest caveat.** As of this writing, China has produced **neither** a classical acute banking panic
**nor** a completed Japan-style workout. Whether the current approach ends as a "Japan-lite" long,
low-growth stretch or a more disorderly adjustment is **not resolved by the data available today** —
this case must be reported as genuinely open, not forced into a completed narrative.

**Design implication.** The largest credit boom in the comparable record has not (yet) tripped any
of the classical crisis markers (30% bank-equity crash, currency collapse, sharp GDP print) this
whole B1 literature is built on — because the state is actively suppressing/spreading the adjustment
rather than letting price and quantity signals clear. A market-economy-calibrated credit-cycle state
variable will systematically **under-read risk** in an administratively-managed system, and — just
as importantly — will not necessarily receive its usual "confirmation" even when the underlying
credit stock is by far the most extreme in the panel. This supports treating **"years an extreme
credit state has gone unresolved"** as informative in its own right — directly relevant to L10's
phase-object enrichment (level/velocity/quadrant/**age**) already specified in the dossier.

### 8. Australia + Canada (multi-decade household-credit booms that have not (yet) burst)

**Build-up.** Australian household debt rose from **~70% to ~190% of household income** over roughly
30 years, equivalent to **~112–114% of GDP (2024–25)**. Canadian household debt/GDP rose from **~80%
(2008) to ~95% (2010) to over 100% for more than a decade**, standing at **~103% (2023)** and
**~100.8% (Q4 2025)** — currently the **highest in the G7**. Both economies sailed through the 2008
crisis with only mild housing corrections; Canadian house prices dipped modestly in 2008 and had
recovered by 2009.

**No trigger, no bust — deliberately.** This case is included precisely because, as of 2026, **no
crisis has been realized** despite multiple decades of elevated and *rising* household credit/GDP,
spanning repeated "the top is now" calls by outside observers since at least the mid-2000s.

**Contributing structural factors** `[interpretation, not a hard finding — flagged accordingly]`:
full-recourse mortgage lending (borrowers cannot simply walk away, unlike much of the pre-2008 US);
housing-supply constraints (immigration-driven demand against restricted land-use/zoning) that have
kept prices supported rather than collapsing; comparatively conservative bank underwriting and
regulation (Canada in particular avoided the securitized-subprime channel that hit the US); and
continued income growth/low unemployment sustaining debt-service capacity.

**Design implication.** This is the **strongest evidentiary case in the entire record** for the
Contract's own mandate that the credit state is a **regime/permission input, never a timing trade**
(§1). A high, even rising, credit/GDP **level** persisted for **decades** without a resolution event
in an economy with structural support — the CD-percentile "level" leg of L10 will read persistently
high in an Australia/Canada-like regime for years with no proximate turn, and the composite **must
not** be allowed to imply urgency from level alone. Only acceleration/turn signals (the expanding-gap
leg) carry incremental timing information, and even those must be read with wide uncertainty bands.

### 9. Ireland, 2008 (the most extreme small-economy case)

**Build-up.** Ireland's mortgage-loan stock exploded from **€16 billion (2003 Q1) to a peak of €106
billion (2008 Q3) — about 60% of Ireland's GDP** in mortgages alone; the banking sector was heavily
**wholesale-funded** rather than deposit-funded, and, as in Spain, euro membership removed the
domestic monetary valve — with Ireland's economy being far smaller relative to its banks' balance
sheets than Spain's.

**Trigger.** The 2007–08 global financial crisis froze wholesale bank funding.

**Bust.** On **30 September 2008** the government issued a blanket guarantee covering **six banks'
liabilities — €375 billion, more than twice Ireland's GDP**. House prices ultimately fell **~54%
peak-to-trough (2007–2013)**, with Dublin apartment prices down **over 62%**; the **ISEQ equity index
fell from a peak near 10,000 (April 2007) to 1,987 (24 February 2009) — roughly an 80% drawdown**.
Real GDP fell **over 3% in 2008** and **nearly 8% in 2009** (**GNP fell 11.3% in 2009**), a cumulative
real GDP decline of **~10% over 2008–2009**. The government injected **€46 billion (~30% of GDP)**
into the banks and nationalized Anglo Irish Bank; **€60 billion (over a third of GDP) left the
country in the last four months of 2010 alone**, forcing Ireland into an **EU/ECB/IMF ("Troika")
program in October 2010**.

**Resolution.** A sovereign bailout — the blanket guarantee transformed a **bank solvency** problem
into a **sovereign solvency** problem almost overnight — followed by a multi-year austerity program,
with recovery aided by Ireland's export-oriented multinational sector (largely insulated from the
domestic property bust) and a return to bond markets by roughly 2012–13.

**Design implication.** Ireland shows that the relevant denominator for "how big is this credit
boom" is not GDP alone but **GDP relative to the size of the banking sector the state might have to
stand behind**. A useful cross-check alongside credit/GDP is **bank-assets/GDP** — especially
relevant if India's less-diversified NBFC/shadow-credit segments were ever to require a systemic
sovereign backstop.

### 10. India, 2003–2018 in full detail (the home case — double length)

**The 2003–08 boom.** Non-food bank credit expanded rapidly through the mid-2000s, concentrated in
**infrastructure and real estate** lending, against optimistic assumptions about demand, project
execution, and future cash flows `[VERIFY: precise year-by-year non-food credit growth rates and the
exact credit/GDP ratio-point change over 2003–08 — RBI's own *Trend and Progress of Banking in India*
annual reports for this window carry the primary series, but a clean consolidated year-by-year table
was not independently re-derived from the sources reachable here; by contrast, the *subsequent*
2008–2014 non-food credit CAGR of 16.8% is independently confirmed]`. Reported asset quality
*improved* through the boom — gross NPAs were masked to roughly **~2%** by its end — which in
hindsight is the boom's own tell: the best-looking headline print coincided with the period of
heaviest under-recognition, not genuine health.

**The Twin Balance Sheet problem, 2011–15.** Corporate over-leverage from the back half of the
2003–08 boom (concentrated in infrastructure, power, and steel) combined with hidden bank-side
stress. The **Economic Survey 2016-17** estimated **stressed advances (NPA + restructured) at ~12%**
of total bank loans system-wide; for **public-sector banks specifically, gross NPAs reached 11.8%**
and **stressed advances 15.8% of total advances by September 2016**; roughly **40% of corporate debt
was owed by firms not earning enough to cover their own interest payments**. This is a genuine
corporate-over-leverage problem that took **five to seven years after the original lending** to
surface in the reported numbers.

**The AQR recognition shock, 2015–2018.** The RBI's 2015 **Asset Quality Review** forced banks to
reclassify previously-obscured stressed loans as non-performing. **Public-sector-bank gross NPAs rose
from ~5.0% (March 2015) to ~14.6% (March 2018)**; the **system-wide gross NPA ratio reached 11.2% in
2017–18**. This must be read as a **measurement break, not a new credit event** — the underlying
loans were already impaired; the AQR simply forced the banks to say so. It is, by a wide margin, the
single most important *splice-discipline* lesson in the whole India chronology: any backtest spanning
2011–2018 that treats the AQR-era GNPA jump as a fresh shock, rather than a forced catch-up on
already-existing stress, will badly mis-time the credit cycle.

**IL&FS, 2018 — the NBFC/shadow-credit freeze.** Infrastructure Leasing & Financial Services, a
large "shadow bank" carrying **debt of ₹91,091 crore (~$13bn)**, defaulted in August–September 2018
after a classic long-term-asset/short-term-liability mismatch. The default triggered a system-wide
**funding freeze across India's non-bank financial sector** — mutual funds and banks pulled back
sharply from NBFC commercial paper — subsequently claiming DHFL, Reliance Capital, and others.
**Critically, this stress was largely invisible in bank-only credit aggregates**, because it ran
through the non-bank/shadow-credit channel — exactly why the Contract's own pre-registered **R7**
design uses IL&FS 2018 as a held-out validation target for L10's composition-signal leg, and why the
bank+NBFC aggregation rule is not optional.

**The 2021–24 unsecured-retail boom and RBI's response.** Household debt/GDP rose from **39.2% (March
2021) to an all-time high of 45.5%** in the most recent Financial Stability Report read
`[this supersedes the "26%→42%" figure carried in the prior internal dossier (`docs/cycles/01-credit-cycle.md`),
which should be corrected in the research register against these independently search-verified
numbers]`. The **mix** shifted materially: non-housing retail loans rose from **~50% (2019-20) to
58.4%** of total household debt — i.e., toward unsecured consumption lending rather than asset-backed
borrowing. The **credit-deposit ratio reached 80.3% (including the HDFC–HDFC Bank merger effect) by
March 2024 — the highest since 2005** — and climbed further to **80.8% by March 2025, the highest in
61 years**, before the gap began narrowing in 2025 as deposit growth caught up with slowing credit
growth. The RBI's **16 November 2023 circular** raised risk weights on **unsecured consumer credit
and bank exposure to NBFCs by 25 percentage points** — personal-loan risk weights rose from 100% to
125% for both banks and NBFCs, and bank exposure to NBFCs whose own risk weight sat below 100% was
raised by the same 25 points — while **explicitly excluding** housing, education, vehicle, and
gold-backed loans. This was a **surgical, composition-targeted** tightening, not a blanket
credit-growth brake — direct, real-world confirmation that the regulator itself was reading the same
**composition-of-incremental-credit** signal that L10's Tier-C input is built on.

**Current state, 2024–26.** System gross NPAs reached a **decadal/multi-decade low of 2.15%** by
September 2025 — explicitly a **lagging comfort signal** that says nothing about where the CD ratio
or the unsecured mix currently sit; the CD ratio remains elevated even as its rate of increase has
slowed.

**Design implications (the home case earns three, not one):**
1. **AQR proves recognition can go dark for years and then jump discontinuously** — GNPA must remain
   a **lagging confirm-only** input (already the rule), and any backtest spanning 2011–2018 must
   apply an explicit splice rule rather than reading the jump as a fresh shock.
2. **IL&FS proves a bank-only aggregate misses the most-recently-realized India stress** — the
   bank+NBFC aggregation rule is validated by the one clean, already-resolved India event best suited
   to testing it, and is the natural target for the pre-registered R7 event check.
3. **RBI's own Nov-2023 action is real-world revealed preference** that regulators actively monitor
   **credit composition**, not just level or growth — corroborating (though not proving predictive
   power for) the design choice to carry an issuance/composition-quality input even at Tier C.

---

## B3. What the panel says, pooled

### Summary table (verified figures only; `[VERIFY]` marks a cell not independently confirmed)

| Episode | Boom size (verified metric) | Equity max drawdown | GDP hit | Years to recover |
|---|---|---|---|---|
| US 2008 | HH debt/GDP ~70%→~98-99% (2000–07) `[VERIFY exact peak]` | S&P 500 **−56.8%** (Oct07–Mar09) | Real GDP **−4.3%** (07Q4–09Q2) | `[VERIFY exact quarter GDP regained 07Q4 level]` |
| US 1929 | n/a | Dow **−89%** (Sep29–Jul32) | Real GDP/capita **−30%** (1929–33) | Dow: 25y (to 1954); GDP `[VERIFY, ~1936]` |
| US S&L 1980s–90s | 1,043 of ~3,200 thrifts failed | n/a (sectoral, not market-wide) | n/a | Resolved by ~1995; cost **$123.8bn** (1999) |
| Japan 1986–90 | Bank RE lending ~2× (1985–90); loan/GDP >100% | Nikkei **−80%** (Dec89→2003, 14y) | Growth drag: **~1.5%/yr** (90–95), **~1%/yr** (92–2001) — no single-year collapse | >20y; contested whether "recovered" |
| UK 1973–74 | Property lending **8×** (1970–74) | UK equities sharply down `[VERIFY exact %]` | n/a (contained) | Resolved in a few years; final cost **£55m** |
| UK 2008 | (shares global 2008 boom) | FTSE 100 **−31%** (2008) | Real GDP **−6.5%** (08Q2–09Q3) | `[VERIFY]` |
| Spain 2000s | Private credit/GDP ~**2×** (2000–07) | IBEX 35 **−50%** (Nov07–Oct08) | GDP **−7.5%** cumulative (2008–13) | Unemployment still >20% a decade later `[VERIFY full recovery year]` |
| Sweden 1990–92 | Bank credit losses **17%** of lending | `[not captured]` | GDP **−5.1%** cumulative (1991–93) | ~2–3y to stabilize; net fiscal cost **1.5% GDP** (1997) |
| Thailand 1997 | FX-peg/currency-mismatch driven | SET **−59%** combined (1997–98) | GDP **−10.2%** (1998) | Slower than Korea `[VERIFY years]` |
| Korea 1997 | ” | KOSPI **−27%** (Oct97 alone) `[VERIFY cumulative]` | GDP **−7%** (1998) | V-shaped: **+10–11%** growth (1999) |
| Indonesia 1997 | ” | Regional mkts "up to −70%" `[VERIFY Indonesia-specific]` | GDP **−13.0%** (1998) | Slower; compounded by political crisis |
| China 2009–present | Debt/GDP **~135%→~296%** (2008→Q3'25) | n/a (no market-wide crash) | Property investment **−10.0%** (2022), **−7.9%** (H1'23); no economy-wide GDP contraction printed | **Unresolved as of 2026** |
| Australia (multi-decade) | HH debt **~70%→~190%** of income; **~112-114%** of GDP (2024-25) | n/a | n/a | n/a — no bust yet |
| Canada (multi-decade) | HH debt/GDP **~80%(2008)→~103%(2023)** | n/a (2008 dip mild) | n/a | n/a — no bust yet |
| Ireland 2008 | Mortgage stock **€16bn→€106bn** (2003–08), ~60% GDP | ISEQ **−80%** (Apr07–Feb09) | Real GDP **~−10%** cumulative (2008–09); GNP **−11.3%** (2009) | Troika program 2010; bond-market return **~2012-13** |
| India 2003–2018 | GNPA masked **~2%**→AQR-forced **11.2%** (2017-18); CD ratio **80.8%** (2025, 61y high) | Sensex **~−60 to −64%** (Jan–Oct 2008) | Growth deceleration (TBS era), not a single-year contraction | GNPA cycle: ~10y, AQR(2015)→decadal low (2.15%, 2025) |

### Pooled conclusions, ranked by evidence strength → design implication for L10

1. **(Strongest — JST panel, hundreds of episodes, plus corroborated in 8 of 10 cases above.)**
   The credit **intensity of the expansion**, not the eventual trigger, predicts recession depth and
   duration (JST 2013, B1.3). → L10 must size leverage/hedge permission off the **boom's** credit
   intensity, independent of whatever eventually triggers the bust — matches the existing "never
   times the top" design.
2. **(Strong — 3 clean natural experiments: Sweden vs. Japan vs. India's AQR delay.)** Recognition
   speed, not boom size, determines the fiscal/growth cost of the bust. → GNPA/recognition inputs
   must be treated as a **state** (has recognition happened yet?), never assumed to resolve quickly;
   supports keeping GNPA a lagging confirm only, and motivates an "unresolved-state age" phase read.
3. **(Strong — Spain, Ireland, Thailand/Korea/Indonesia, 5 of 10 cases.)** Fixed exchange rates or
   currency-union membership remove the domestic monetary valve and lengthen/worsen credit busts. →
   Not directly applicable to India's floating rupee, but supports a **separate external-vulnerability
   gauge** (short-term external debt, currency mismatch) rather than folding this channel into the
   domestic credit state.
4. **(Moderate-strong — Greenwood et al.'s formal result, B1.5, plus qualitative confirmation in
   Spain/Ireland/Japan and its notable *absence* in Australia/Canada.)** Credit growth **alone** is a
   materially weaker signal than credit growth **joined with** asset-price growth over the same
   window. → Prioritize the pre-registered **R3** (India R-zone replication); a joint condition, not
   credit alone, is the higher-precision (if rarer) trigger for tightening permission further.
5. **(Moderate — US 2008, India IL&FS 2018, China shadow-trust lending; 3 of 10 cases.)** A
   bank-only credit aggregate misses the specific channel (shadow banking/NBFC/wholesale funding)
   behind the *most recent* bust in nearly a third of these cases. → Confirms the bank+NBFC
   aggregation rule already built into L10 as necessary, not optional.
6. **(Moderate — 2 clean natural experiments: Australia+Canada vs. US/UK/Spain/Ireland.)** A high or
   rising credit-to-GDP **level** can persist for **decades** without a crisis when supported by
   structural factors (full-recourse debt, supply-constrained housing, disciplined underwriting). →
   The single strongest support in this record for treating the level/percentile leg as a **regime
   input only, never a timing trade** — the composite must never imply a "when," only a "how much."
7. **(Emerging — n=1, still-unresolved.)** An administratively-managed credit system (China) can
   suppress the classical trigger signals this literature is calibrated on without the underlying
   risk being resolved. → Low direct applicability to India's market-based, floating-currency banking
   system, but a caution for reading any future India state characterized by heavy forbearance (as
   in the 2020 COVID moratoria) — a quiet reading during a forbearance episode should not be read as
   "no risk"; the existing "COVID is policy-shaped" caveat in the L10 dossier already reflects this.
8. **(Weakest/most tentative — a single direct precedent, US S&L → US 2008, 20 years apart.)** Prior
   severe credit-cycle experience does not vaccinate an economy against a similar repeat two to three
   decades later. → Parameters must stay **frozen** and be periodically re-derived on schedule (Tier
   B rule), never tuned to a "this time is different" argument — reinforcing the Contract's §8 ban on
   backtest-tuned thresholds.

---

## Special side-task — JST Macrohistory mirrors on GitHub

`macrohistory.net` itself was confirmed unreachable from this environment's network egress
(direct `WebFetch` attempts returned `EGRESS_BLOCKED`), so the dataset cannot be pulled from its
authoritative host here. Using `mcp__github__search_code` (GitHub's own code-search index) plus
direct `curl` probes against `raw.githubusercontent.com` (confirmed reachable), the following
repositories were found to hold **actual committed data files** — not merely scripts that download
from macrohistory.net at runtime — verified live (HTTP 200, correct file signature/content) as of
this session. Ranked most credible first:

1. **`bank-of-england/MachineLearningCrisisPrediction`** — official code repo for Bank of England
   Staff Working Paper 848 ("Credit Growth, the Yield Curve and Financial Crisis Prediction").
   Release **R3**, `.xlsx`, confirmed valid (PK-zip magic bytes read directly).
   `https://raw.githubusercontent.com/bank-of-england/MachineLearningCrisisPrediction/master/data/JSTdatasetR3.xlsx`
2. **`dvollrath/Growth4ed`** — Dietrich Vollrath's (University of Houston) textbook data repo, most
   recently active of the three Vollrath mirrors. Release **R4**, `.csv`, confirmed valid (real JST
   column headers read directly: `year,country,iso,...,tloans,tmort,thh,tbus,hpnom,eq_tr,housing_tr,...`).
   `https://raw.githubusercontent.com/dvollrath/Growth4ed/main/Data/jstdatasetr4.csv`
3. **`dvollrath/StudyGuide4ed`** — companion repo to the above (same author, "4th edition" study
   guide). Release **R4**, `.csv`, confirmed valid.
   `https://raw.githubusercontent.com/dvollrath/StudyGuide4ed/main/data/jstdatasetr4.csv`
4. **`dvollrath/StudyGuide`** — the older, predecessor repo to #3 (same author, earlier edition).
   Release **R4**, `.csv`, confirmed valid.
   `https://raw.githubusercontent.com/dvollrath/StudyGuide/master/data/jstdatasetr4.csv`
5. **`axfreeman/MacroEconomic-History-Server-Builder`** — path
   `DATA/SOURCE/ORIGINALS/JST/JSTdatasetR6.xlsx` **is the newest release (R6)** but is stored via
   **Git LFS**: the raw URL returns only an LFS pointer stub (confirmed: content is the text
   `version https://git-lfs.github.com/spec/v1 / oid sha256:9f089e9d... / size 6146802`, not the
   actual spreadsheet bytes), so it is **not directly downloadable** through `raw.githubusercontent.com`
   without a Git-LFS-aware client. Listed last, and flagged, rather than omitted, because it is the
   only R6 (most current, 18-country) copy found on GitHub.
   `https://raw.githubusercontent.com/axfreeman/MacroEconomic-History-Server-Builder/master/DATA/SOURCE/ORIGINALS/JST/JSTdatasetR6.xlsx`
   (LFS pointer only — do not treat as a working download without `git lfs pull`)

None of these were downloaded in this pass, per instructions — only their reachability and file
validity were probed (HTTP status + magic bytes / header row).

---

## References (verified this session; URLs as found via WebSearch/GitHub code search)

- Schularick, M. & Taylor, A.M. (2012). "Credit Booms Gone Bust: Monetary Policy, Leverage Cycles,
  and Financial Crises, 1870–2008." *American Economic Review* 102(2): 1029–1061.
- Jordà, Ò., Schularick, M. & Taylor, A.M. (2013). "When Credit Bites Back." *Journal of Money,
  Credit and Banking* 45(s2): 3–28.
- Drehmann, M. & Juselius, M. (2014). "Evaluating Early Warning Indicators of Banking Crises:
  Satisfying Policy Requirements." *International Journal of Forecasting* 30(3): 759–780.
- Greenwood, R., Hanson, S.G., Shleifer, A. & Sørensen, J.A. (2022). "Predictable Financial Crises."
  *Journal of Finance* 77(2): 863–921.
- Mian, A., Sufi, A. & Verner, E. (2017). "Household Debt and Business Cycles Worldwide." *Quarterly
  Journal of Economics* 132(4): 1755–1817.
- Krishnamurthy, A. & Muir, T. "How Credit Cycles across a Financial Crisis." NBER WP 23850 (2017);
  forthcoming/published *Journal of Finance* (2025).
- Baron, M., Verner, E. & Xiong, W. (2021). "Banking Crises Without Panics." *Quarterly Journal of
  Economics* 136(1): 51–113.
- Jordà, Ò., Schularick, M. & Taylor, A.M. — Macrohistory Database, `macrohistory.net` (R3/R4/R6),
  NBER data page `nber.org/research/data/jorda-schularick-taylor-macrohistory`.
- RBI: *Trend and Progress of Banking in India* (annual); Financial Stability Reports (various
  years); circular RBI/2023-24/85 (16 Nov 2023); Economic Survey 2016-17, Ch. 4 ("The Festering Twin
  Balance Sheet Problem").
- All other figures per the case-by-case citations embedded in B2 and the `[VERIFY]` tags therein.



---

# PART B-RESULTS — JST R6 pooled panel (REAL DATA)

# JST R6 pooled-panel results (REAL DATA - advanced-economy prior, NOT India)

Source: JST Macrohistory R6 (GitHub mirror, sha256 in ingest/vault/jst/manifest.json;
authenticated vs independent R4 mirror + published crisis chronologies). 18 countries,
1870-2020, 88 crisis onsets. Conventions: annual Hamilton h in {4,5,6} (the 16-24q
grid), p=1; expanding percentiles min_obs=20y; interior data gaps
<= 5y interpolated (war gaps remain gaps). The credit state is
PARAMETER-FREE per country, so scores are real-time honest by construction.
Generated by scripts/analyze_jst_panel.py on 2026-09-01. All cells below are logged
in research/register/trial-ledger.md (entries J1-J5).

## J1 - Early-warning power of OUR state (expanding Hamilton gap percentile)

| Score | AUROC crisis<=3y | AUROC crisis<=5y | n(country-years) |
|---|---|---|---|
| gap pctile h=4y | 0.653 | 0.620 | 1806 |
| gap pctile h=5y | 0.641 | 0.613 | 1781 |
| gap pctile h=6y | 0.624 | 0.617 | 1756 |
| 5y real credit growth (ST-style) | 0.638 | 0.607 | 2309 |

Per-country AUROC (h=5, crisis<=3y): median 0.667; range Netherlands 0.32 to Ireland 0.98; 14/18 countries > 0.5.

## J2 - Schularick-Taylor-style logit (simplified spec: 5y avg real credit growth,
country fixed effects; label = crisis onset within 3y)

- Slope per 1 sigma of 5y credit growth: b = +0.385 (log-odds); average
  marginal effect = +3.15pp on a base rate of 9.4%.
- In-sample AUROC of the fitted logit: 0.679 (published in-sample ~0.72
  for the original 5-lag spec on 14 countries - same ballpark, different spec/panel).

## J3 - R-zone (Greenwood-Hanson-Shleifer-Sorensen 2022 style)

- business credit (Δ3y bus/GDP): R-zone n=77 country-years; P(crisis<=3y | R-zone) = **26.0%** vs base 7.8% (published: ~45% business / ~40% combined vs ~7% base; full-sample quantiles,
  as in the paper - the real-time variant is a pre-registered India design, R3).
- total credit (Δ3y proxy: 3y avg growth): R-zone n=153 country-years; P(crisis<=3y | R-zone) = **15.7%** vs base 10.1% (published: ~45% business / ~40% combined vs ~7% base; full-sample quantiles,
  as in the paper - the real-time variant is a pre-registered India design, R3).

## J4 - Forward 3y equity max drawdown by credit-state quintile (R2 prior)

| State quintile (h=5 gap pctile) | mean fwd 3y max DD | median fwd 3y REAL return | n |
|---|---|---|---|
| Q1 | 19.0% | +11.9% | 322 |
| Q2 | 13.0% | +17.8% | 321 |
| Q3 | 14.0% | +17.0% | 322 |
| Q4 | 12.3% | +24.3% | 322 |
| Q5 | 17.1% | +15.5% | 321 |

Linear slope fwd-DD on state: -2.27pp per unit of percentile (prior read only - the India R2 design carries Stambaugh + Newey-West).

## J5 - H66 PRELIMINARY (exploratory, pooled): same level, different trail

Matched level: state percentile in [0.55, 0.90]. U = rising, D = falling-from-high.

| Trail | n | P(crisis<=3y) | mean fwd 3y max DD | median fwd 3y REAL return |
|---|---|---|---|---|
| U (rising) | 234 | 6.0% | 14.9% | +13.1% |
| D (falling) | 209 | 6.7% | 13.0% | +22.5% |

EXPLORATORY read for the H66 prior only - the confirmatory design (matched-level
deciles, purged CV, Stambaugh) runs at R2/R4. Logged as trial J5.




---

# PART C — Data engineering (India)

# Part C — Data engineering: building the Indian credit series

v1.0 · 2026-09-01 · Extends `docs/masterplan/A-data-catalog.md` §2 blocks G (RBI), I (CCIL/FBIL),
J (BIS/IMF/World Bank) — that appendix is the source of truth for access paths, priorities, and
the fixture-governance rules (WORM manifest, vintage tagging); this part goes one level deeper on
the four L10 inputs specifically: exact table/series names, splice and interpolation conventions
named and pre-registered, and the construction-grade detail a build script needs that a source
catalog does not carry. Consumes: `config/ladder.yaml L10_credit_block`. Feeds: Part D's
`hamilton_filter` and `expanding_percentile` (the math), Part E's STEP 1–3 pipeline (the code) —
this part is the specification those steps implement. Everything below was checked this pass by
web search (snippet-level only, per Contract prior #11 — no live fetch, no file in hand); anything
not independently confirmed carries `[VERIFY]`.

---

## C.1 Bank credit — the exact RBI/DBIE series

The base layer is a single legal instrument wearing several publication names. **Section 42(2) of
the RBI Act, 1934** obliges every scheduled bank to file a fortnightly return — the **"Form A"
return, Statement of Fortnightly Position"** — reporting its demand-and-time liabilities and cash
reserves as at the close of business on alternate Fridays, within seven days. The **RBI Scheduled
Banks' Regulations, 1951** (in force 1951-11-01) is the operative regulatory instrument that
formalized the return's content; this is almost certainly the source of the "~1951" date the task
brief carries, but it dates the *regulation*, not the earliest *published, DBIE-queryable* time
series — those two dates are not the same and should never be conflated in a fixture header.

Four public products are cut from this one filing stream, at different granularities and lags:

| Product | Exact name (as published) | Source / path | First available | Frequency | Pub. lag |
|---|---|---|---|---|---|
| Fast vintage | Weekly Statistical Supplement — "Scheduled Commercial Banks' Business in India" (aggregate credit, deposits, C-D ratio, cash-reserve ratio) | `rbi.org.in/Scripts/BS_ViewWss.aspx` (WSS, weekly, every Friday); mirrored in DBIE | format exists since the 1950s (evolved); the specific aggregate-credit/deposit table is a stable multi-decade cut | weekly (last reported fortnight) | same week |
| Growth headline | "Non-food credit" / "Bank credit" growth, y-o-y and outstanding | DBIE → Financial Sector → Money & Banking; also RBI press release "Sectoral Deployment of Bank Credit" (same filing feeds both) | modern standardized monthly series ~1998+; older annual data further back [VERIFY exact pre-1998 vintage] | monthly | ~3 weeks post month-end |
| Granular annual | **Basic Statistical Return (BSR)-1** — "Credit by Scheduled Commercial Banks (including RRBs)"; **BSR-2** — "Deposits with Scheduled Commercial Banks"; BSR-3 — branch-level statistics | `rbi.org.in/Scripts/AnnualPublications.aspx?head=Basic+Statistical+Return...` | **BSRs introduced 1972** (standardised bank-level/account-level data collection) | historically annual (as-of end-March); **RBI has since moved BSR-1 data collection to a quarterly cadence internally, with the public release still framed as an annual as-of-March publication** [VERIFY exact public cadence — a 2026 RBI social post still labels the release "BSR-1 ... March 2026", i.e. annual-labeled] | published well after fiscal year-end; treat as a lagged annual anchor, not a monthly input |
| Aggregate cross-check | "Quarterly Statistics on Deposits and Credit of Scheduled Commercial Banks" (QSDC) | `rbi.org.in/Scripts/QuarterlyPublications.aspx?head=Quarterly+Statistics+on+Deposits+and+Credit...` | long-running quarterly publication | quarterly | ~1 quarter |

**Portal note (task-flagged item — DBIE after the 2024–25 revamp).** The domain moved from
`dbie.rbi.org.in` / `cimsdbie.rbi.org.in` to **`data.rbi.org.in/DBIE/`**, effective close of
business **2024-06-21** (old domains redirect; do not rely on the redirect indefinitely — hardcode
the new domain in any scraper). The underlying data-warehouse rebuild is the **Centralised
Information Management System (CIMS)**, which went live in **June 2023** and is described by RBI
as the "next generation" of its data-warehousing infrastructure — CIMS is the back-end name, the
portal keeps the DBIE brand. RBI also shipped a first-party **"RBIDATA" mobile app (Feb 2025,
11,000+ series)** as a confirmed alternative export channel if the web query-builder proves
brittle to script. **[VERIFY]** whether any individual credit series was re-defined (not merely
re-hosted) as part of the CIMS migration — the domain change itself is confirmed, a
series-definition change is not.

**Sectoral deployment — start date and the real break.** The monthly "Sectoral Deployment of Bank
Credit" release (standalone page `rbi.org.in/Scripts/Data_Sectoral_Deployment.aspx`, also a
recurring RBI press release and Economic Survey Statistical Appendix Table 32, "Deployment of
Gross Bank Credit by Major Sectors") is standardized-monthly from roughly **1998+**. The genuine
measurement break in this series is **January 2019**, when RBI revised the sectoral-deployment
reporting format — sub-sector definitions (including how NBFC lending is bucketed within
Services) changed at that point; any pre-/post-Jan-2019 comparison of a sub-line needs the same
splice discipline as a GDP base-year change. **The November 2023 risk-weight circular is explicitly
not this kind of break** — see C.5.

## C.2 NBFC + shadow credit

Bank-only credit is blind to the exact channel that froze in 2018 (IL&FS) — the design's own
chronology names this ("invisible in bank-only credit → the bank+NBFC aggregate rule",
`docs/cycles/01-credit-cycle.md` §3). Two free sources cover the shadow layer, at much lower
frequency than bank credit:

| Source | Exact product | Frequency | Lag | Note |
|---|---|---|---|---|
| RBI Financial Stability Report | NBFC chapter — sector-wide consolidated balance sheet, GNPA, capital-adequacy of the NBFC sector, stress-test results | biannual (June, December editions) | publication is the data (no interim); ~edition date only | **[VERIFY exact chapter number/title per edition]** — content confirmed (search finds recurring NBFC balance-sheet commentary in the June 2026, June 2024, June 2019 editions), a stable chapter numbering across editions was not independently pinned down this pass |
| RBI Bulletin — recurring NBFC statistical tables | "Consolidated Balance Sheet of NBFCs", "Deposits Mobilised by NBFC Sector", "Selected Financial Parameters of Non-Deposit-Taking Systemically Important NBFCs (NBFCs-ND-SI)" | typically an annual/semi-annual Bulletin article citing quarter-end data | ~1–2 quarters | Same underlying regulatory return (NBFC supervisory returns), narrated rather than published as a clean flat file — hand-transcription, same discipline as GNPA (C.6) |
| CCIL / F-TRAC | Commercial Paper and Certificate of Deposit primary + secondary market data (F-TRAC is CCIL's RBI-designated Trade Repository for CP/CD/corporate-bond-repo reporting; members must report within 15 minutes of trade) | market-watch pages appear to render publicly at `ftrac.co.in` (e.g. `CP_SEC_MEM_MARK_WATC_VIEW.aspx`, `CD_SEC_MEM_MARK_WATC_VIEW.aspx`) | near-real-time on the page; bulk historical download **[VERIFY — login wall not confirmed either way this pass]** | NBFCs are the dominant CP issuer, so CP-issuance volume is the fastest available proxy for shadow-credit funding stress (2018 IL&FS showed up here first, in spreads, weeks before any FSR NBFC chapter recognized it) |
| RBI WSS (fallback) | "Money Market Operations" — weighted-average CP/CD rates | weekly (Friday) | same week | Coarser than F-TRAC (rate only, not volume) but unambiguously free and stable; the fallback if F-TRAC access proves gated |

**Building the bank+NBFC aggregate the design requires, and the approximation error that
remains.** The construction is `credit_total = credit_bank + credit_nbfc`, but the two legs are
neither same-frequency nor independent:

1. **Frequency mismatch.** Bank credit is monthly (~3-week lag); NBFC credit is FSR-anchored
   (biannual, June/December, itself lagging its reference date by weeks). The combined series can
   only be as fresh as its NBFC leg unless NBFC credit is upsampled — see the interpolation
   convention in C.10 (piecewise-linear in log-level between successive NBFC reference dates, with
   a staleness mask once a new FSR edition is overdue).
2. **Double-counting risk.** Bank credit *to NBFCs* already appears inside `credit_bank` (as a
   named sub-line of Sectoral Deployment, "NBFCs" under Services — see C.5). If `credit_nbfc` is
   read as NBFCs' *total* balance-sheet credit outstanding (which is itself partly funded by bank
   borrowing), naively summing double-counts the bank-to-NBFC leg. **The construction must net
   bank credit *to* NBFCs out of the NBFC total before summing** — i.e.
   `credit_total = credit_bank + (credit_nbfc_total − bank_credit_to_nbfcs)` — or accept the
   double-count as a *known, bounded, one-directional* upward bias and document its size
   (bank credit to NBFCs was a large and growing share of Services credit through 2021–24; leaving
   it unnetted overstates `credit_total` by roughly that sub-line's magnitude, which the sectoral
   deployment table itself reports monthly, so the correction is at hand, not a data gap).
3. **Residual approximation error after both fixes**: NBFC funding *outside* bank credit and
   market CP/CD (e.g. inter-NBFC lending, foreign borrowing, retained-earnings-funded growth) is
   not separately observable from these free sources at monthly frequency — the aggregate is a
   **lower bound update frequency, upper-bound-correctable level**, and this residual should be
   named in the module's own docstring, not silently absorbed.

## C.3 Denominators — nominal GDP

| Layer | Source | Start | Frequency | Lag |
|---|---|---|---|---|
| Annual National Accounts (back series) | MOSPI National Accounts Statistics | **1950-51** | annual | provisional → first-revised → final over ~2 years (standard NAS practice) |
| Quarterly GDP/GVA | MOSPI (CSO), press notes on `mospi.gov.in` | **introduced 30-06-1999**, with the published series starting from reference quarter **Q1 1996-97** — the task brief's "~1996-97" is the correct anchor for the *reference period*, not the *announcement date* | quarterly | ~2 months (Q4 + provisional-annual estimate released together, per the standard NAS cycle) |

**Base-year history (confirmed this pass, with exact transition dates):**

| Old base → new base | Effective from | Driver |
|---|---|---|
| 1980-81 → 1993-94 | February 1999 | post-liberalization structural change |
| 1993-94 → 1999-2000 | January 2006 | services/IT-sector weight update |
| 1999-2000 → 2004-05 | January 2010 | — |
| 2004-05 → 2011-12 | 30 January 2015 | company-financials-based value-added methodology (2015 rebasing) |
| 2011-12 → **2022-23** | **27 February 2026** | the announced ~2026 revision the task brief flags; a "Sources and Methods" methodology note was due ~August 2026 — **pull it the moment it appears; it will state MOSPI's own splicing instruction for this transition** |

**Splicing method — the two options and which the design pre-registers.** MOSPI's own historical
practice: *"for years prior to [the anchor base], estimates were compiled by adopting the splicing
method, retaining the same growth rates of aggregates as in the old series"* — i.e., MOSPI's own
back-series convention is a **growth-splice** (chain the old series' period-over-period growth
rates onto the new series' level at the overlap point), not a single ratio.

Two candidate methods for our own construction:

- **Ratio-splice at the overlap period**: compute `k = GDP_new(t0) / GDP_old(t0)` at the single
  quarter/year both vintages report, then rescale the *entire* old-vintage history by the constant
  `k`. One multiplication, transparent, auditable in one line — but assumes the old/new
  relationship is stable at exactly the one overlap point and propagates any noise in that single
  ratio across every prior decade.
- **Growth-splice (chain-linking)**: keep the old series' own period-over-period growth rates and
  re-level them so the *chained* series matches the new vintage going forward. Matches MOSPI's own
  official back-series method, so any published "back series" MOSPI itself releases can be
  ingested directly without re-deriving it — but requires the old series' growth rates at every
  period, and is more fragile to a single bad print in the old series (an error compounds forward
  through the chain rather than being contained to one ratio).

**Pre-registered choice (this design, per `Part E STEP 2`): ratio-splice at the overlap period.**
Argument: (i) it is a single, auditable scale factor per base-year transition — five transitions
in the sample, five recorded ratios, trivially inspectable in a review; (ii) MOSPI's own official
back series, when and if released for the 2026 transition, can still be ingested as a
*cross-check* against our ratio-splice, not a replacement for it — divergence between the two
methods becomes a documented data-quality flag rather than a silent discrepancy; (iii) growth-splice
requires trusting the old series' growth rates at every historical point equally, which is a
stronger assumption than trusting one ratio, given the AQR-style and CIMS-style break history this
appendix has already catalogued elsewhere in the macro block. **Departure note (Contract §1, "state
the departure explicitly"): this differs from MOSPI's own preferred method — documented, not
hidden.**

**Monthly interpolation for the monthly credit/GDP ratio.** There is no monthly GDP release, but
L10's Hamilton filter (Part D) wants a monthly denominator to match `credit_bank + credit_nbfc`'s
monthly grid. **Convention (Part E STEP 3, restated precisely here): cubic-spline interpolation on
the *log* of quarterly GDP**, producing a smooth monthly path that reproduces the exact quarterly
values at quarter-ends. This is flagged everywhere downstream as a **convention, not data** — the
interpolated months carry no new information and must never be treated as an independent
observation in any effective-sample-size count (purged CV, AUROC computation) that assumes monthly
data has monthly information content.

## C.4 CD ratio — construction and why it dodges the GDP problem

The credit-deposit ratio is cut from the *same* Section 42(2) filing stream as C.1 — no separate
collection instrument. RBI publishes it as **"Deposit and Credit Ratio of Scheduled Commercial
Banks"** in the Handbook of Statistics on the Indian Economy (a stable table across editions) and
as a queryable DBIE Banking Statistics series; recent readings are also carried directly in press
commentary (CD ratio reported at **78.1% end-March 2024 — "highest since 2005"** per RBI-sourced
press reporting, corroborating the design's own chronology note in `docs/cycles/01-credit-cycle.md`
§3 that flags 2021–24 as "CD ratio ~80%, highest since 2005").

The **monthly history back to 1969** already assumed in the L10 construction
(`docs/cycles/01-credit-cycle.md` §4: "monthly, 1969→; long-run range ~51.6%–~80%") is corroborated
this pass only indirectly — multiple RBI Handbook tables are confirmed to carry data reaching back
to 1969-70 in general, but the *exact* first published fortnight/month of the CD-ratio cut itself
was not independently pinned down. **[VERIFY]** the precise first observation on first live DBIE
contact; treat 1969 as the working assumption, not a confirmed fact, until then.

**Why this input is genuinely cleaner than the credit/GDP gap.** It needs:
- no GDP denominator (so none of C.3's base-year, splicing, or interpolation machinery applies);
- no cross-agency alignment (both numerator and denominator come from the identical fortnightly
  filing, at the identical reporting entity level);
- no revision-vintage bookkeeping beyond the ordinary bank-level revision cycle already handled by
  DBIE's own vintage support.

This is precisely why the design's own R5 test (`docs/cycles/01-credit-cycle.md` §5) asks whether
the CD ratio should become the *primary* level input and the Hamilton gap merely its cross-check,
rather than the reverse — a question this data-engineering layer cannot answer (it is an
econometric spanning test, Part D/R5's job) but can now say is at least *operationally* justified:
the CD ratio is the cheaper, more robust build of the two.

## C.5 Composition input — sectoral deployment shares

The "hot" composition signal (unsecured retail + NBFC on-lending share of incremental credit) is
read off named sub-lines of the same Sectoral Deployment release as C.1:

| Sub-series (as published) | Parent category | Note |
|---|---|---|
| "Personal Loans" → "Consumer Durables", "Credit Card Outstanding", "Other Personal Loans" | Personal Loans | credit-card sub-line is separately broken out — the fastest-turning unsecured proxy |
| "Housing (Including Priority Sector Housing)" | Personal Loans | **secured** — excluded from the "hot" composition numerator by construction |
| "Vehicle Loans", "Education" | Personal Loans | secured/quasi-secured — excluded |
| "NBFCs" | Services | the bank-to-NBFC leg also needed for the C.2 double-count correction |
| "Industry", "Agriculture and Allied Activities" | (top-level) | denominator context, not part of the hot numerator |

**Start date**: standardized monthly from ~1998+ (same filing as C.1); older annual cuts exist
further back but at coarser sector granularity — do not assume sub-line comparability before the
modern monthly series begins.

**Breaks, named precisely (task's own framing, confirmed by this pass's search):**
- **January 2019 reporting-format revision** — a genuine measurement break; sub-sector
  definitions changed (search confirms "with effect from January 2019, sectoral credit data are
  based on [a] revised format"). Splice discipline applies exactly as it does to the GDP base-year
  changes: two segments, a documented ratio at the transition, never a trend fit through it.
- **November 2023 risk-weight circular** (RBI/2023-24/85, DOR.STR.REC.57/21.06.001/2023-24,
  dated **2023-11-16**, +25pp risk weight on unsecured consumer-credit exposures of banks and NBFCs
  to 125%, compliance by 2024-02-29; explicitly excludes housing/vehicle/education/gold/microfinance
  loans) is **not a measurement break** — the series definition did not change, only the economic
  incentive to originate this credit did. Per the task's own framing this is a **marker**: the
  regulator's own policy response *confirming* the design's composition signal was reading
  something real, exactly analogous to how the design already treats the AQR (C.6) as a
  recognition event rather than a fresh deterioration. Do not splice across it; do treat its
  aftermath (credit-card growth decelerating sharply into 2024–25, per the same sectoral-deployment
  release) as an out-of-sample readout of whether the composition input actually led the
  regulator — this is exactly design R7's pre-named validation target
  (`docs/cycles/01-credit-cycle.md` §5).

## C.6 Confirm inputs — GNPA, rating-agency defaults, and the CMIE non-option

**GNPA.** RBI Financial Stability Report editions (biannual, June/December, series from ~2010) are
the primary narrative source; DBIE additionally carries a queryable asset-quality time series
(third-party compilations citing `dbie.rbi.org.in` as source show public-sector-bank GNPA data
back to 1995 [VERIFY — not independently confirmed against a primary RBI table this pass, but
consistent with the AQR-era literature's usual starting point for PSB GNPA charts]). The **2015
Asset Quality Review (AQR)** is, per the data catalog's own characterization, "the single largest,
best-documented regime break in this entire catalog": system GNPA moved from **5.0% (March 2015)
to 14.6% (March 2018)**, purely from RBI's withdrawal of forbearance on restructured-asset
recognition, not a fresh wave of borrower defaults. **Handling rule (already fixed by the design,
restated here for the data layer): treat 2015–2018 as two segments joined by a documented
recognition event, never one continuously-defined series; the module's GNPA input is a lagging
confirm-only dummy, so this break cannot leak into a leading signal by construction — but it can
still corrupt a naive descriptive chart if plotted through without annotation.**

**Rating-agency default/downgrade counts.** Both major domestic agencies publish an annual,
citable, genuinely free study:

| Agency | Exact publication | Cadence | Access | Note |
|---|---|---|---|---|
| CRISIL Ratings | **"Default and Rating Transition Study"** (e.g. "...up to fiscal 2025") | annual | direct, stable PDF URL pattern: `crisilratings.com/content/dam/crisil/our-analysis/publications/default-study/crisil-ratings-annual-default-and-ratings-transition-study-fy-{yyyy}.pdf` (confirmed for FY2020–FY2025 editions) | Methodology moved to **monthly static-pool** with the **2009 edition** (finer intra-year default/transition granularity than a simple annual static pool); FY2025 annual default rate reported at **0.7%, a 17-year low**, down from 1.30% in FY2024 — directly usable as a default-rate time series once several editions are hand-collected |
| ICRA | **"Performance of ICRA-Assigned Ratings in FY{yyyy}"** | annual | PDF exists and is free, but served via an ID-keyed download link off `icra.in/Rating/Methodology?Page=RatingPerformance` rather than a stable filename pattern — **[VERIFY]** a durable per-year URL scheme before scripting; re-discover the link each year if not | FY2025 reported **301 upgrades vs. 150 downgrades** — a rating-momentum (upgrade/downgrade ratio) series, complementary to CRISIL's default-rate series |

Both are genuinely free (no paywall, no registration observed in the fetched links), which answers
the task's own question directly: **yes**, free PDFs exist for both agencies; the construction cost
is annual hand-transcription (same discipline as GNPA and FSR — no bulk historical file exists for
either).

**CMIE — explicitly not free.** CMIE's Prowess/CMDB/Economic Outlook products (which would
otherwise be the natural source for firm-level default and distress data, and for a cross-check on
credit growth) are a **paid subscription service** and are excluded outright by Contract §3's
free-source rule. No substitute is needed for the *credit-cycle* inputs specifically — the design
already resolves the general CMIE-shaped capex-tracking gap elsewhere (RBI OBICUS + MOSPI
IIP-capital-goods + GFCF, per `docs/masterplan/A-data-catalog.md` §6) — and for defaults/downgrades
specifically, the CRISIL+ICRA free studies above are the complete substitute. This should be stated
plainly wherever a future contributor might reach for CMIE out of habit: **do not**.

## C.7 Cross-checks (external, free) — never primary

Every series in this section is bound by the same rule: **cross-check only.** The design's own
credit-to-GDP gap is Hamilton-filtered, own-construction; BIS's competing gap is explicitly banned
as a substitute (Contract §8 trap list: "Do NOT use the HP filter anywhere").

| Source | Exact product | URL pattern | History | Freq. | Lag |
|---|---|---|---|---|---|
| BIS Data Portal | Credit-to-GDP gaps (India) | `data.bis.org/topics/CREDIT_GAPS/data` (bulk CSV, no login) | gap computable wherever the underlying level series exists | quarterly | ~1 quarter |
| BIS Data Portal | Total credit to private non-financial sector (India), levels, "adjusted for breaks" | `data.bis.org/topics/TOTAL_CREDIT/data` | **Q2 1951 → present** — but **Q2 1951–Q1 1970 is BIS's own estimate using M3 as a proxy for credit**, not measured credit; only from **Q2 1970** is it a directly-observed credit aggregate | quarterly | ~1 quarter |
| IMF | Global Debt Database (GDD) | `data.imf.org/en/datasets/IMF.FAD:GDD`; datamapper mirror at `imf.org/external/datamapper/datasets/GDD` | panel dating to 1950 in principle (190-economy unbalanced panel); **exact India start year [VERIFY] — not independently confirmed this pass** | annual | at release (methodology traces to the October 2016 Fiscal Monitor) |
| World Bank | Global Financial Development Database (GFDD) — private-credit-to-GDP family (`GFDD.DI.02`, `GFDD.DI.12`), mirrored in WDI as `FS.AST.PRVT.GD.ZS` (domestic credit to private sector, %GDP) and `FD.AST.PRVT.GD.ZS` (same, banks only) | `databank.worldbank.org` / `data.worldbank.org/indicator/{code}?locations=IN` | from **1960** | annual | ~1 year; sourced from IMF IFS + national data, so it inherits every India-specific break (the 2026 GDP rebase included) with the World Bank's own additional lag on top |

**BIS methodology, confirmed and directly relevant to the ban.** BIS derives its published trend
with a **one-sided (backward-looking) Hodrick-Prescott filter, smoothing parameter λ = 400,000 on
quarterly data**. One-sided avoids the classic two-sided look-ahead problem, but Hamilton's (2018)
critique — the design's own stated reason for the ban (Part D, §D1) — targets the filter mechanism
itself (spurious cyclicality manufactured by the moving-average structure, a magic-number λ), not
merely its two-sided variant. BIS's own gap therefore remains banned as a *substitute* for the
design's own construction even in its (better-behaved) one-sided form; it is retained purely as an
independent, differently-flawed cross-check — a second opinion built on a method the design has
already rejected on its merits, which is exactly what makes divergence between the two
informative.

## C.8 Market-price complements — the fast layer

| Instrument | Exact index/series | Source | History | Freq. | Note |
|---|---|---|---|---|---|
| Bank Nifty | "Nifty Bank Index" | NSE Indices, `niftyindices.com/Factsheet/ind_nifty_bank.pdf` | base date **2000-01-01** (=1000); **launched 2003-09-15** | daily | the base-date/launch-date gap (base predates launch by ~3.7 years) is a standard NSE Indices convention, not a data anomaly — do not read the base date as the first tradeable observation |
| Broader financials | Nifty Financial Services Index | NSE Indices | **[VERIFY exact base/launch date — not confirmed this pass]** | daily | wider than Bank Nifty (includes NBFCs, insurers, housing finance) — arguably the better single-index proxy for *shadow*-credit-sensitive equity, given C.2's NBFC-visibility problem |
| Corporate bond spreads | FIMMDA "Corporate Bond Spread Matrix" / "Yield Matrix" (tenor-, rating-, industry-classification-wise) | `fimmda.org` | matrices published on the last working day of each month (post valuation-committee vetting), plus a fortnightly cut | monthly (+fortnightly) | **[VERIFY]** whether bulk historical download is open or requires member sign-in — the *current* matrix is confirmed reachable without an obvious paywall in the fetched links, historical depth was not confirmed |
| Corporate bond issuance/outstanding | SEBI corporate-bonds statistics | `sebi.gov.in/statistics/corporate-bonds.html` | **[VERIFY exact history start]** | monthly | regulator-published, complements FIMMDA's price-side cut with a volume-side cut |
| CP rates (fast, free fallback) | RBI WSS "Money Market Operations" — weighted-average CP/CD rates | `rbi.org.in/Scripts/BS_ViewWss.aspx` | multi-decade | weekly | coarser than F-TRAC (rate only) but unambiguously free; use if F-TRAC's login status resolves unfavorably |

**Framing.** These are the design's Krishnamurthy–Muir-style fast complement: bond spreads and CP
funding rates move at weekly/daily frequency and lead bank-level credit tightening by weeks to a
couple of months, exactly filling the gap between the ~3-week-lagged monthly bank-credit print and
the ~2-quarter-lagged NBFC print (C.2). They are **not** a fifth L10 input — the design's own
four-input construction (§4 of `docs/cycles/01-credit-cycle.md`) is frozen — but they are the
natural fast-stress (L2) cross-feed and the natural early-warning readout for the C.2 approximation
gap: a spread/CP-rate spike between two FSR editions is the free, weekly-frequency signal that the
NBFC leg of `credit_total` is already stale.

## C.9 Vintage / point-in-time discipline

The governing rule is already fixed at the repository level (`ingest/manifest.py`,
`ingest/README.md`): **every raw pull is checksummed into a manifest; a refresh is a new
vintage-dated file, never an in-place overwrite** (the manifest script hard-fails if a file's hash
changes under an existing entry — "content changed under an existing manifest entry ... refreshes
must land as NEW vintage-named files"). Two dates are mandatory on every row: `vintage_date` (the
date the figure was *as-of*/published) and `pull_date` (when this program fetched it) — this is
the WORM (write-once-read-many) discipline the task brief asks after.

| Series | Revision-prone? | Backfilled? | Announcement lag | Store first-print or latest? | Why |
|---|---|---|---|---|---|
| SCB fortnightly credit/deposits (C.1) | Low (bank-level filing revisions are rare and small) | No | ~3 weeks | Latest (with vintage tag) | Revision risk is minor relative to the CIMS/domain-migration risk; the real discipline need is capturing *which portal generation* served a given pull |
| Sectoral deployment (C.1/C.5) | Break-prone (Jan-2019 format change), not revision-prone | No | ~3 weeks | Latest, both format-vintages kept distinct across the Jan-2019 break | A format break is not a revision — never merge the two sides into one column |
| BSR-1/2 (C.1) | Low | No | multi-month | Latest | Small, stable, infrequent |
| Nominal GDP, quarterly + annual (C.3) | **High** — provisional → first-revised → final over ~2 years, plus five base-year regime changes across the sample | **Yes, structurally** — every base-year transition is itself a controlled backfill | ~2 months (quarterly cut) | **Every vintage, as a new row — never overwritten** | This is the textbook "GDP revisions" case the task brief names directly; a single-vintage pull silently look-ahead-biases anything using GDP as of a past date |
| CD ratio (C.4) | Low (same filing as C.1, no denominator revision channel) | No | ~2–4 weeks | Latest | Structurally the cleanest series in this appendix — the reason C.4 argues for its promotion to primary |
| NBFC credit (FSR/Bulletin, C.2) | Low print-to-print, but **structurally stale between editions** | No | edition-date only (no interim) | Latest, with an explicit `stale_after` flag once a new edition is overdue | The "revision" risk here is really a *staleness* risk, not a restatement risk — flag accordingly, don't conflate with GDP's revision problem |
| GNPA (C.6) | **Break-prone** (AQR 2015), not revision-prone in the ordinary sense | No | edition-date only | Latest, two-segment-annotated across AQR | Same discipline as sectoral deployment's Jan-2019 break — a recognition event, never smoothed through |
| CRISIL/ICRA default studies (C.6) | Methodology-revision-prone (CRISIL's 2009 move to monthly static pool) | Partially (later editions sometimes restate prior-year figures under the newer methodology) | edition-date only, annual | Latest edition's own restated figures, tagged with which methodology vintage | Same edition-based discipline as FSR — no bulk historical file exists for either agency |
| BIS credit-to-GDP gap / total credit (C.7) | Revision-prone — BIS periodically revises its own break-adjustment methodology | Yes (pre-1970 India figures are themselves an M3-based estimate, not measured credit) | ~1 quarter | Latest, with the pull's BIS-methodology-vintage noted | Cross-check only — a stale cross-check is a minor risk, but the pre-1970 M3-proxy caveat must travel with the series everywhere it is plotted |
| IMF WEO/GDD, World Bank GFDD (C.7) | Revision-prone (WEO explicitly; GDD/GFDD inherit India's own NAS revisions with a lag) | Yes | biannual (WEO)/annual (GDD, GFDD) | **Every WEO vintage kept, never only the latest** (already the data catalog's own J2 rule) | The single cleanest point-in-time macro-forecast archive available free — wasted if only the current vintage is kept |
| Market-price complements (C.8) | Low (prices are not restated) | No | T+0/T+1 | Latest (there is no "first print" distinct from the traded price) | The one category in this table with no PIT problem at all |

## C.10 Construction pipeline — ordered, script-followable

This restates and completes Part E's STEP 1–3 at data-engineering precision; steps 0–3 are this
part's responsibility, steps 4 onward hand off to Part D's math and Part E's own numbering.

1. **Registry load.** Validate `config/ladder.yaml` (must pass `config/validator.py` with 0
   errors) before any pull — the pipeline never runs against an un-validated registry.
2. **Pull, per series, into `data/raw/<org>/...`** (directory layout per
   `docs/masterplan/A-data-catalog.md` §5): SCB fortnightly credit + deposits (DBIE, monthly cut);
   sectoral deployment (DBIE/RBI press release, monthly); CD ratio (Handbook/DBIE, monthly);
   quarterly + annual nominal GDP, every base-year vintage kept distinct (MOSPI); NBFC credit (FSR
   NBFC chapter + RBI Bulletin NBFC tables, biannual, hand-transcribed); GNPA (FSR + DBIE);
   CRISIL/ICRA default studies (annual PDF, hand-transcribed); BIS/IMF/World Bank cross-checks
   (bulk CSV, every vintage for WEO). Every pull is followed immediately by
   `python ingest/manifest.py data/` — an unmanifested file does not exist for the pipeline.
3. **Splice across structural breaks, per series, before anything is merged:**
   - GDP: **ratio-splice at the single overlap period** for each of the five base-year
     transitions (1993-94→1999-2000→2004-05→2011-12→2022-23), per C.3's pre-registered choice;
     record each transition's ratio in the manifest as its own auditable constant.
   - Sectoral deployment: **two segments across January 2019** — never merge sub-line
     definitions across the format change.
   - GNPA: **two segments across the 2015 AQR** — annotate inline, never fit a trend through
     March-2015-to-March-2018.
   - COFER/WEO-style vintage series (used only in cross-checks, C.7): keep the pulled vintage
     explicit; never silently prefer "latest" when the question is "what was known as of date X."
4. **Align to a common monthly grid:**
   - `credit_bank`: native monthly, no interpolation needed.
   - `credit_nbfc`: native biannual/quarterly (FSR/Bulletin) → **piecewise-linear interpolation
     in log-level** between successive reference dates (proposed convention, extending Part E
     STEP 3 — pending registry sign-off), **with a `stale_after` mask**: once more than one
     reporting cycle has elapsed since the last NBFC print without a new one landing, months
     beyond that point are held flat and flagged `stale`, not silently interpolated forward as if
     new information existed.
   - `credit_total = credit_bank + (credit_nbfc − bank_credit_to_nbfcs)` — the C.2 double-count
     correction, netting the named "NBFCs" sub-line of sectoral deployment out of the NBFC total
     before summing.
   - Nominal GDP: **cubic-spline interpolation on log quarterly GDP** to monthly, per C.3 —
     flagged everywhere downstream as a convention, not an observation; excluded from any
     effective-sample-size count.
   - CD ratio: native monthly (or finer, collapsed to monthly by last-fortnight-of-month), no
     interpolation needed — this is the whole point of C.4's construction argument.
5. **Compute the four L10 inputs** (Part D's math, referenced here only for completeness):
   `gap_t = hamilton_filter(credit_total / gdp_monthly, h ∈ {16,20,24}q pre-registered grid, p=4,
   mode="expanding")`; `G_t = expanding_percentile(gap_t)`; `C_t = expanding_percentile(cd_ratio)`;
   `Q_t = expanding_percentile(hot_composition_share)` (unsecured personal + NBFC on-lending share
   of incremental sectoral-deployment credit, per C.5, **clamped to `min(0, reading)`** per the
   Tier-C rule); `N_t` = GNPA-trend confirm dummy (lagging only, never leading).
6. **Warm-up masks.** Every `expanding_percentile` and `expanding`-mode Hamilton filter carries a
   `min_obs` floor — early-sample readings before the reference window is long enough are masked
   `NaN`, not silently reported as if reliable; the mask boundary is itself a pre-registered
   constant (Part D §D2), not tuned after seeing results.
7. **Composite + phase.** `state_t = credit_state_composite(G_t, C_t, Q_t; weights from the
   registry's pre-registered grid)`; `phase_t = phase_state(state_t; grids from
   `state_phase_convention`)` — both per Part E STEP 6–7, unchanged by this data layer.
8. **Break-registry side effects.** Any of: a source series discontinued/renamed; the 2026 GDP
   rebase landing (dual-vintage parallel run until spliced); a sectoral-deployment redefinition —
   trips the same failure-mode handling already named in Part E ("capture-health flag, run on
   last-good + de-risk rung"; Tier-C composition zeroed to safe-default with a compensating
   one-notch hedge-floor hold, preserving the reduce-only asymmetry).
9. **Recalibration triggers.** Re-run the h-grid/weight sweep (R1, R4) annually on the grown
   sample; re-check the GDP splice ratios whenever MOSPI's own back-series documentation for the
   2022-23 base is finally published (expected ~August 2026 per its own press note; pull it,
   compare against this pipeline's independently-derived ratio-splice constants, and log any
   divergence as a data-quality flag rather than silently adopting MOSPI's number in its place).

---
*End of Part C. Cross-references: `docs/masterplan/A-data-catalog.md` §2 blocks G/I/J (access
paths, priorities, fixture governance), `docs/cycles/01-credit-cycle.md` §3–4 (the chronology and
the four-input construction this part builds data for), Part D (`partD-econometrics.md`, the math
consuming these series), Part E (`partEFH-algo-extraction-ledger.md`, the pipeline this part
specifies), `ingest/README.md` + `ingest/manifest.py` (the WORM/manifest rule), `research/
CONTRACT.md` §3 (free-source mandate), §8 (HP-filter ban).*



---

# PART D — Mathematics and econometrics

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



---

# PART E/F/H — Algorithm, harvest map, knowledge ledger

# Part E — The algorithm, end to end

The complete L10 pipeline as executable pseudocode. Every step names its code home and its
convention's registry seat. Nothing below is hypothetical — steps 4–8 run today
(`quant/ladder/`, tests passing); steps 1–3 are the ingest layer awaiting the principal's
machine (`ingest/README.md` runsheet).

```
STEP 0  (once)  Registry load + validate (config/validator.py must pass: 0 errors)
STEP 1  (monthly, T+lag per series)
        pull: SCB fortnightly credit, deposits (DBIE); sectoral deployment (DBIE);
              quarterly nominal GDP (MOSPI); NBFC credit (FSR, semiannual, interpolation
              convention pre-registered); GNPA (FSR/DBIE)
        manifest: sha256 + vintage stamp per file (ingest/manifest.py; WORM — never overwrite)
STEP 2  splice: GDP across base years (pre-registered ratio-splice at overlap);
        AQR 2015 GNPA break: two segments, never one series (measurement break rule)
STEP 3  align: monthly grid; credit_bank + credit_nbfc = credit_total;
        interpolate quarterly GDP to monthly (pre-registered convention, log-cubic;
        flagged everywhere as convention, not data)
STEP 4  gap_t   = hamilton_filter(credit_total/GDP, h from grid {16..24}q, p=4,
                                  mode="expanding")            [D1]
STEP 5  G_t     = expanding_percentile(gap_t)                  [D2]
        C_t     = expanding_percentile(credit/deposits)
        Q_t     = expanding_percentile(hot-composition share)  [Tier C]
        N_t     = GNPA trend confirm dummy                     [lagging only]
STEP 6  state_t = credit_state_composite(G_t, C_t, Q_t; weights from registry)
                  — Tier-C clamp: composition can only push toward risk-off  [D11]
STEP 7  phase_t = phase_state(state_t; grids from state_phase_convention)
                  — (level, velocity, quadrant, age); notation 0.6U/0.6D
STEP 8  consume: state feeds macro_credit block (≤0.20 of regime score R);
        quadrant/age LOG-ONLY until H66–H68 pass; policy mapping via the frozen
        bucket → (leverage, hedge, tail-throttle) table
MONITOR daily: nothing (monthly state); monthly: input freshness, break registry;
        quarterly: τ½ re-estimate within CI-hysteresis (tau_half_drift_policy);
        annual: full R1–R7 refresh on the grown sample
FAILURE MODES (each with its tripwire):
  - series discontinued/renamed at source → capture-health flag, run on last-good + de-risk rung
  - GDP rebase lands (~2026) → breaks-registry entry; dual-vintage parallel run until spliced
  - composition series redefinition → Tier-C input to zero until re-validated (clamp makes
    this safe: zeroing a reduce-only input can only make us more permissive, so the zeroing
    ALSO forces a one-notch hedge-floor hold until review — asymmetry preserved)
  - state near ±1 saturation for >12m → percentile reference-window review (financial deepening
    can pin ranks; pre-registered re-anchor rule, annual only)
```

# Part F — What we extract from the credit cycle (the full harvest map)

One mechanism, many consumers — each consumer pre-registered, budgeted, and reduce-first.

| # | Consumer | What L10 changes | Status |
|---|---|---|---|
| F-a | Regime score R | macro_credit block seat (≤0.20): high state pushes R down (risk-off) | live design (v1) |
| F-b | Leverage permission | state high ⇒ Kelly-numerator and gross-leverage permission decay toward 1.0x | live design |
| F-c | Hedge floor | state high ⇒ hedge grid floor one bucket earlier; phase-D + fast-stress-U = the dangerous overlap (slow fragility + fast trigger) | live design; overlap rule pre-registered, reduce-only |
| F-d | Tail-sleeve entry throttle | boom-mature states slow new tail-risk entries | live design |
| F-e | Sector conditioning | financials/cyclicals relative tilt CONDITIONED on credit state (projection principle: one mechanism, one budget seat — this is L10 projected, not a new seat); ties to H63 provisioning-cycle | R4-phase test |
| F-f | Quality-sleeve floor | boom-mature ⇒ quality floor binds (junk rallies late in booms; composition input echoes Greenwood-Hanson issuance quality) | live design |
| F-g | Gold linkage | credit-bust states historically coincide with gold outperformance in INR (channel: risk-off + INR pressure); consumed via the existing gold floor, no new seat | context only, documented |
| F-h | Stage-2 briefing | the state + phase + age is on the daily page; the human sees 0.62U age-14m, not a narrative | live design (sentinel) |
| F-i | Duration input | age-in-quadrant → sizing cushion IF H68 passes | gated |

**Designs restated + extended (all frozen before data):** R1 India-conditioned AUROC (EB-pooled
prior 0.65–0.75 [A]); R2 forward-DD regression (Stambaugh + NW, D5); R3 India R-zone table;
R4 Hamilton-h grid selection; R5 impulse-vs-level complementarity (reframed by the Fig 4.3
finding); R6 τ½ + lengthening drift (H65b, Drehmann-Borio); R7 composition event check
(2018 IL&FS + Nov-2023 as pre-named held-out targets). NEW from the deep dive: **R8** bank-equity
crash marker (Baron-Verner-Xiong): Bank-Nifty drawdown as a free, real-time crisis-dating input —
test as episode-dating refinement, not a new seat; **R9** credit-spread fast complement
(Krishnamurthy-Muir): CCIL/FIMMDA spread percentile as the fast twin of the quantity state —
pre-registered as a candidate CONFIRM input to L2/L10 seam, reduce-only first; **R10** pooled
duration/hazard estimation for H68 (D10 machinery).

# Part H — Conclusions: the knowledge ledger, honestly ruled

**Established (Tier A/pooled, safe to build on):** credit booms raise crisis probability and
deepen recessions (ST/JST); the joint credit+price boom is the dangerous configuration (R-zone);
crash risk is neglected by credit suppliers themselves (BX — the survival argument); the
credit-to-GDP gap is the best single slow early-warning indicator known (DJ), with the caveat
that OUR gap is the Hamilton-expanding acceleration/turn variant, whose real-time shape we have
measured and documented.

**Established about OUR machinery (synthetic ground truth):** the module recovers planted booms
and busts in real time; the Tier-C clamp is arithmetic; the phase overlay labels trails
correctly with hysteresis; the estimators' small-sample behavior is measured (including two
falsified first drafts, kept on the record).

**Pooled-prior, awaiting Indian confirmation [A]:** AUROC 0.65–0.75; forward-DD slope sign;
composite weight grid; h grid; τ½ [7–11y, lengthening watch].

**India-specific, unknowable until fixtures:** every coefficient above, the 2026 GDP-rebase
splice behavior, composition-series stability post-2023 circular.

**Unknowable in principle:** the date of the next down-leg; whether the current cycle's
resolution resembles Japan (slow), Sweden (fast), or the AFC (external) — the state variable is
built so that not knowing this is survivable, and the case-study lessons (Part B) are encoded as
DESIGN choices (Australia/Canada: high state ≠ imminent bust ⇒ no shorting the boom; Japan:
resolution can take a decade ⇒ τ½ drift watch; AFC: the external-funding channel ⇒ L9/INR seam,
never inside L10's budget).
