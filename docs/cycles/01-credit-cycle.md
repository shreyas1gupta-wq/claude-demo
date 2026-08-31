# Deep-dive #1 — The Credit Cycle (L10, the anchor state)

v1.0 · 2026-08-31 · Evidence base: D03 (+D07, D08 overlaps) · Ladder seat: `config/ladder.yaml
L10_credit_block` · Hypotheses: H-series credit rows + H65b · Code: `quant/ladder/credit_cycle.py`
· **Results status: regression DESIGNS are frozen here; RESULTS require the Phase-0 fixtures on
the principal's machine — the module and a synthetic end-to-end demo run today.**

---

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
