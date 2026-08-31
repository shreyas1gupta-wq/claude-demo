# Multi-Horizon Cycle-Stack Portfolio Model — Research Plan & Design Document

Version 0.9 (research phase) · 2026-08-31 · Status: pre-data design. No parameter herein has been
fitted; every number traces to a source, a cross-country panel, an explicit argument, or is marked
as an assumption-until-data. Supporting evidence lives in `research/dossiers/01–12` (≈90,000 words,
cited); this document is the integrative specification and references dossiers as `D01…D12`.
Binding mandate: `research/CONTRACT.md`. Decisions record: `research/OPEN_QUESTIONS.md`.

**Provenance key** used throughout: **[T]** = theory/first-principles · **[X]** = cross-country
evidence · **[I]** = India-specific evidence · **[A]** = assumption until data arrives ·
**[V]** = carries unresolved `[VERIFY]` flags in the source dossier (see §15).

---

## 0. How to read this document

- §1–§2 say what the three books are and where the mandate's own arithmetic binds or contradicts.
- §3–§5 are the risk system: architecture, the cycle ladder, and the drawdown machinery.
  Per Known Prior #3, **the cycle stack is the risk system; name selection is the return system** —
  cycles buy permission to run concentrated and levered, contributing only ~100–300bps/yr directly.
- §6–§7 are the return system and its construction (Stage 3).
- §8 is the Stage-2 charter (advisory-only until proven, per Decision Q7).
- §9–§11: costs/capacity, the consolidated decay ledger, and the estimation/validation protocol.
- §12–§15: build sequence with gates, deliberate exclusions, epistemic status, verification queue.

Everything here is encoded in machine-checkable form in `config/` (validated by
`config/validator.py`; a registry violating its own budgets fails to load).

---

## 1. The three books

Three products, not one product dialled down. Each book's edge is structurally different:

| | Aggressive | Moderate (ANCHOR) | Conservative |
|---|---|---|---|
| Capital | ₹100–250 cr | ₹1,000–2,500 cr | ₹10,000–25,000 cr |
| Turnover cap (1-way/yr) | 600% (ceiling, not plan — §9) | 200% | 100% |
| Stated universe | NIFTY 750 incl. ranks 500–750 | ranks 1–500 | ranks 1–500 |
| **Effective full-size universe** (arithmetic, §2.1) | full size to ~rank 300; tail at 1–2% tickets | full size to ~rank 100–150 | full size to ~rank 50–80 |
| Return engine | Momentum sleeves + tail/special-sits satellite + factor core | **Factor book (value/quality/low-vol)** | Factor book, capacity-constrained projection |
| Name count (floor→ceiling, dispersion-conditioned §7.2) | 15–20 → 50–65 | 30–50 → 65–100 | 50–80 → 150–250 |
| Design-point turnover | 250–350% | 100–160% | 40–75% |
| Honest net CAGR (derivation §1.1) | ~15.5–26.5% | ~13.5–20.5% | ~12–16% |
| Max DD target (ceiling 30–35% frozen) | 25–30% | 20–25% | 18–22% |

The moderate book is the design anchor (Decision Q6): its factor engine has the longest signal
half-lives (≈5× momentum's — Israel-Moskowitz turnover evidence, D02 [X]), therefore the lowest
cost per unit of authority, and both other books derive from it — conservative by tightening
capacity/entry constraints, aggressive by adding faster sleeves on top.

### 1.1 Honest target derivation (net of costs, pre-tax; benchmark Nifty 500 TRI per Decision Q1)

Built additively from sourced parts, each after its decay haircut (§10) and cost (§9):

| Component | Aggressive | Moderate | Conservative | Source |
|---|---|---|---|---|
| Market base (Nifty 500 TRI, long-run nominal) | 12–14% | 12–14% | 12–14% | [I] AJV market premium 11.5% + rf history, D01/D02 |
| Mid/small structural tilt (net of higher DD cost) | +1 to +3pp | ~0 | ~0 | [I] illiquidity premium lives in ranks 500–750, D02 |
| Momentum sleeves (post 25–35% haircut, post cost) | +3 to +6pp | +0.5 to +1.5pp (modifier only) | ~0 | [I] AJV WML 21.9%/yr raw → §10 |
| Factor book (value/quality/low-vol, post 25–40% haircuts) | +1 to +2pp | +2.5 to +5pp | +1 to +2.5pp | [X][I] D02 |
| Special situations satellite (capacity-capped) | +0.5 to +1.5pp | 0 | 0 | [I] D12, Tier-B events |
| Leverage (avg ~1.10–1.15x agg / 1.05x mod) net of funding | +0 to +1pp (0 when the funding hurdle clips it) | +0 to +0.5pp | 0 | [T] §5.4 — thin under margin funding at 9–12%; wider if funding ≈ MIBOR |
| Risk-system drag (whipsaw + option budget + cash drag) | −1 to −2pp | −0.5 to −1.5pp | −0.5 to −1pp | [X] D04 (vol targeting/trend whipsaw); [A] India whipsaw count |
| **Net CAGR band (component sums: floor = every row at its pessimistic end simultaneously, ceiling = every row optimistic — both extremes are themselves unlikely co-realizations; central expectation ≈ mid-band)** | **≈15.5–26.5%** | **≈13.5–20.5%** | **≈12–16%** | red-team audit: an earlier draft's floors exceeded the row sums; corrected to the literal min-sum |

The prior pass's 22–28% (aggressive) sits in the upper half of this band and **requires** (i) the
tail/microcap sleeve surviving cost validation, (ii) a favorable credit/valuation regime, and
(iii) funding cost nearer MIBOR than retail MTF. It is a stretch case, not the design target —
building to an impossible target forces exactly the risk-taking the drawdown ceiling exists to
prevent (Contract prior #9).

---

## 2. Mandate arithmetic: where the constraints bind and where they contradict

These are stated with the numbers, per the principal's instruction. None is fatal; each forces a
design choice recorded here. Full arithmetic: D05 §4.

### 2.1 The stated universes and the entry weights cannot coexist at scale
A 5.5% entry at ₹25,000cr (conservative top) = ₹1,375cr/position.
- **SAST Reg. 29 disclosure at 5% of shares outstanding** → target market cap must exceed
  ≈₹27,500cr → roughly the top 120–150 names only [I][V].
- **Liquidity**: rank-300 ADV ≈ ₹20–40cr/day [A: provisional ADV table, D05 §4b]; at 10%/day
  participation a full ₹1,375cr build takes ≈**340–690 trading days (1.5–3 years)** — effectively
  never; even at rank 100–150 (ADV ₹80–150cr) it takes ≈**18–34 weeks**. *(Corrected by the
  consistency audit: an earlier draft understated both by conflating a days figure with weeks.)*
- Same logic: moderate book full-size to ~rank 100–150; aggressive full-size to ~rank 300; the
  rank 500–750 tail (ADV ₹1–4cr) admits only ~1–2% tickets even at ₹100–250cr (5% entry at ₹250cr
  = ₹12.5cr ≈ 3–4 full days of total ADV at the upper end of the tail's liquidity range, ~5+ days
  at its median).
**Resolution adopted**: each book carries TWO universes — a *full-conviction* universe (ADV- and
SAST-bounded, narrow) and a *long-hold small-ticket* universe (the full stated rank range at
reduced size and low turnover). The conservative book's effective entry weight below rank ~100
falls to 2.5–4% (more names, wider N ceiling); the frozen 5–6% entry survives as the cap on the
full-conviction cohort only. Encoded in `config/books.yaml`; the registry enforces the split.

### 2.2 The 600% turnover cannot be spent where the aggressive book's distinctive alpha lives
Tail names take 8–15+ weeks to build (§2.1) — a name that takes two months to enter cannot turn
over 6×/yr. And the only signals fast enough to justify 600% (1-month reversal, fast momentum) are
the most cost-constrained anomalies in the literature (Frazzini-Israel-Moskowitz; D01 [X]) and
carry a 20bp STT round trip India adds on top [I]. Re-derived cost at 500% one-way: **3.5–6.5%
NAV/yr with tail-size throttling, 4.5–9% without** (D05 §4h) — bracketing, not replacing, the
prior pass's 3.9%. The implied incremental gross-alpha hurdle for the fast book is **3.0–6.0pp/yr**.
**Resolution**: the aggressive book = a *fast sleeve* confined to liquid ranks (where 600% is
spendable) + a *slow tail sleeve* whose capacity is an absolute ₹ amount, not a % of NAV — tail
alpha as %NAV shrinks as the book grows ₹100→250cr. 600% stays a ceiling to be earned by
post-cost, point-in-time evidence; the design point is 250–350%.

### 2.3 The relative-DD constraint binds in shallow bears, and Decision Q3 (margin funding) tightens it
Mid/small downside beta to Nifty 50 ≈ 1.15–1.3 (2008: midcap ≈ −75% vs Nifty ≈ −60%; 2018: Nifty
−15% vs smallcap ≈ −32%; D04 [I]). With margin leverage 1.10–1.15x **on the held names**, effective
downside beta ≈ 1.3–1.5. In a 2011-type −25% Nifty episode, unhedged that is −32% to −37% —
worse than the index AND at the absolute ceiling. To satisfy "below the index", the machinery must
cut effective beta to ≲1.0 by the time the index is ~10% down. Margin funding (unlike an index
futures overlay) also faces margin calls in stress → forced selling risk → **leverage permission
must tighten earlier** than a futures-overlay design would require. The violation test itself is
now persistence-based (Decision Q5, §5.6), which tolerates transient beta overshoot — but not a
sustained one.

### 2.4 Leverage economics under Decision Q3 are thin and must clear a stated hurdle
Statutory cost alone: cash delivery ≈22.3bps round trip vs index futures ≈**5.7bps** (all-in with
brokerage ≈24–32 vs ≈8–16bps) — futures are ~**4×** cheaper [I][V: D05 §4a rates verified; the
statutory futures figure corrected from 7.7 to 5.7bps by the consistency audit, which reproduced
the component sum]. Margin funding costs 9–12%/yr retail; a
prop desk may fund near MIBOR (~6.5–7.5%). At funding f, the marginal 10–15% exposure earns
(E[r_equity] − f): at f=11% and E[r]=13%, +0.2–0.3pp/yr to the book — barely positive; at f=7%,
+0.6–1.0pp. **Design consequences (adopted):** `funding_rate` is a first-class config parameter;
the leverage state function (§5.4) includes an explicit expected-return-vs-funding hurdle; the
book never holds debt above the policy floor while levered (borrowing at 7–12% to hold a
7%-yielding sleeve is negative carry — the 10% debt assumption is bookkeeping, not economics);
and the futures-overlay alternative is recorded as the cost-superior instrument, revisited if
realized funding cost exceeds MIBOR + ~200bps. *Principal to confirm the actual funding rate —
it moves this from marginal to material.*

### 2.5 "Rare option buying" (Decision Q4) reopens part of the fast-crash floor
The prior pass's "Mar-2020 to ≈−20% with 8–12% irreducible" assumed options were standing when the
gap came. De-grossing cannot act through a gap or a circuit-halt day: India's market-wide circuit
breakers halt cash AND derivatives together, and a held mid/small name can be locked limit-down
for days (D04 [I]). Israelov's evidence (static de-gross often beats permanently-on puts, D04 [X])
supports de-grossing as the *primary* tool — but only if the *rare* option buying is
**rule-triggered, not discretionary**: bought when the fast-trigger state (§5.3) fires, budgeted
(≈0.5–1.5% NAV/yr max premium spend [A]), and closed before expiry to avoid the 0.15%
exercise-STT-on-intrinsic trap [I]. Under this design the honest fast-crash floor is restated as
**10–15% irreducible** (vs 8–12% with standing options) until the data phase measures the gap
distribution. If that number is unacceptable, the option budget must rise.

### 2.6 Rebalance cadence is per-sleeve or the mandate contradicts itself
A monthly-rebalanced 1-month-reversal sleeve is dead on arrival (half-life ≈ signal's own window);
value/quality at weekly cadence burns turnover for nothing (aim portfolio barely moves —
Gârleanu-Pedersen, D11 [T]). Cadence, bands, and re-entry rules are all **per-sleeve** (Decision
Q8), tied to each signal's `tau_half` (§7.3).

### 2.7 Conventions this document fixes (were ambiguous in the mandate)
- Turnover = one-way = min(buys, sells)/avg NAV. Hedge/leverage overlay turnover is tracked and
  costed separately; it does not consume the equity turnover caps [A — principal may override].
- Options count delta-adjusted toward the 1.5x gross cap; the notional caps (≤50%/≤75%) are
  separate hard caps.
- The 5–6%/10%/20% caps read against total book NAV.
- The 20% in-progress cap splits into a full-size-build cohort (frozen 20%) and a small-ticket
  cohort with its own ceiling (D11 §4d refinement; registry enforces both).
- Drawdown measured on daily close NAV.

---

## 3. Architecture

```
                 ┌──────────────────────────────────────────────────────────┐
   free data →   │ STAGE 1 — CYCLES + QUANT (complete portfolio on its own) │
                 │  Cycle ladder (§4) → regime matrix (§5) → risk envelope  │
                 │  Signal sleeves (§6) → Stage-3 construction (§7)          │
                 └──────────────┬───────────────────────────────────────────┘
                                │ complete target portfolio
                 ┌──────────────▼───────────────────────────────────────────┐
                 │ STAGE 2 — AI + HUMAN OVERLAY (§8)                        │
                 │  ADVISORY-ONLY shadow book until pre-registered gate     │
                 │  passes at a high bar (Decision Q7). Switchable off.     │
                 └──────────────┬───────────────────────────────────────────┘
                                │ (no effect on traded book until promoted)
                 ┌──────────────▼───────────────────────────────────────────┐
                 │ STAGE 3 — OPTIMIZER (§7): equity cross-section ONLY.     │
                 │  Asset mix = policy portfolio (§6.6), never optimized.   │
                 └──────────────────────────────────────────────────────────┘
```

Load-bearing properties:
1. **Stage-1 self-sufficiency** is the falsifiability instrument: the paired
   quant-only-vs-quant-plus-overlay test (§8.3) is the only honest measure of Stage 2.
2. **The asset mix is never optimized** (Contract prior #5; Michaud/DGU optimizer-fragility
   evidence, D06/D11 [X]): a flat 10% debt assumption corners any optimizer (MVO → 70% debt,
   risk parity → 67%). Policy portfolio: §6.6, with the ~400bps/yr debt markdown stated.
3. Stage 3 uses **no expected-return vector**: characteristic portfolios (Brandt-Santa-Clara-
   Valkanov) + Ledoit-Wolf covariance for risk budgeting only (§7.1) — the estimation-error
   evidence (DeMiguel et al.: optimizers need centuries of data to beat 1/N) makes literal MVO
   inadmissible on the return side [X].

---

## 4. The cycle ladder

**Governing facts.** (a) Cycles have persistence, not periodicity: Slutzky (1937), Yule (1927),
Granger (1966), and Nelson-Plosser (1982) jointly establish that filtered/smoothed macro series
manufacture apparent cycles from noise and that macro spectra show no peak at any "cycle"
frequency — persistence dominated by low frequencies is the correct model (D07 §1G [T][X]). A
claimed 50–250-year wave observed over 150–800 years yields 1–4 non-overlapping realizations,
usually generated by *different* mechanisms — a periodogram test is not even well-posed. Hence:
anything with <4 observed complete periods is a **state variable ordered by `tau_half`**
(autocorrelation half-life, months), never a clock. (b) India's own history rarely supplies the
observations: 1–2 completed credit down-legs post-1991 (D03 [I]), n=1 real-estate cycle, n≈4–5
monetary round trips — so India-actionable coefficients are Tier B at best, estimated by partial
pooling on the Jordà-Schularick-Taylor panel (§11.4), with the **methodology** often Tier A pooled.

**Calendar-anchored survivors (re-derived, provisional).** The prior pass found 5 of 32 candidates
passed the clock test, 3 calendar-anchored. Our re-derivation of plausible passers: Union-Budget
window (annual, n≫30 on timing), general-election window (n=8–9), fiscal-year-end (annual,
hypothesis), monsoon season (annual, weak sector effect), derivative-expiry calendar (mechanical).
All five are **timing/vol-scheduling objects only** — direction is never predictable from the
calendar: election-day moves are surprise-driven, not schedule-driven — 2004 close ≈ −15.5%
(intraday −17%), 2009 ≈ +10.7% to the first upper-circuit halt, but 2024 only ≈ −5.9% close
(intraday −7.4%), roughly half the older band [I, magnitudes verified by the citation audit].
The RBI monetary cycle (n≈4–5) is a marginal quasi-cycle. This mapping is provisional until the
data-phase clock test re-runs on real series with pre-registered period definitions.

### 4.1 The ladder (ordered by `tau_half`, short → long)

Tiers per Contract §4. "Cap" = maximum share of the regime-score budget (§5.1) the entry may
carry; Tier-C entries are reduce-only and live in a separate negative-only overlay. τ½ values are
**[A] priors to be estimated** (bias-corrected AR(1), §11.2); ranges below are design priors from
the cited literature, not fitted numbers.

| # | State variable / cycle | τ½ prior | Mechanism (survival argument) | Free indicator | Tier | Cap / expression | Dossier |
|---|---|---|---|---|---|---|---|
| L1 | 1-month cross-sectional reversal | 0.5–1m | Liquidity-provision premium (Cheng et al.) — but most cost-constrained anomaly known; no India magnitude study exists | bhavcopy | **C (India)** | **Zero return budget**; contrarian sanity flag only | D01 |
| L2 | Fast stress triggers: realized-vol jump, India-VIX term-structure inversion, funding/FII-outflow runs | 1–3m (episode) | Vol clustering + funding stress are structural; reactive info, not decaying alpha | bhavcopy vol, NSE India-VIX, CCIL, NSDL FPI | B (mech. A global) | Risk-off authority inside fast layer (§5.3); never predictive claims | D04 |
| L3 | Momentum composite: 12-1 blended 6-1 (rank blend) + 52-wk-high | 6–12m | Gradual information diffusion under limited attention; India: thin coverage + promoter float caps slow discovery. Post-publication decay is largely a US phenomenon (Jacobs-Müller) | bhavcopy | **A (global mech.) / B (India magnitude)** | Return sleeve (§6.1), haircut 25–35% | D01 |
| L4 | Time-series momentum, Nifty & gold (1–12m sign/rank) | 6–12m | Institutional constraint: benchmarked mandates cannot trend-follow; CTA capacity | bhavcopy futures, WGC/LBMA | A (global) / B (India) | Regime-matrix input + gold tilt; haircut 10–20% (equity), 35–45% (gold) | D01/D06 |
| L5 | Election / Budget calendar windows | event | Timing fixed by law; direction = surprise only | ECI, indiabudget.gov.in, India-VIX | B (timing) / C (direction) | ≤5% of budget; leverage/vol scheduling only | D08 |
| L6 | Monetary-policy stance (repo path, lagged ~1y) | 12–24m | Transmission via bank-lending channel is structurally slow (~2–6 quarters); knowing the rate ≠ arbitraging transmission | RBI DBIE | B (n≈4–5 marginal) | Inside macro block (shared cap) | D08 |
| L7 | Issuance/sentiment cycle: IPO share, first-day pops, SME froth; equity share in new issues | 12–24m | Issuers time rich valuations (Baker-Wurgler); SEBI's own 2024 SME actions confirm the mechanism institutionally | NSE/BSE listings, SEBI bulletins, bhavcopy | B (methodology) / C (India coeff.) | ≤10% of budget; also sizes the special-sits sleeve | D08/D12 |
| L8 | Value spread (factor's own valuation) | 24–36m | Cheapness of cheap-vs-expensive predicts value's forward return (Cohen-Polk-Vuolteenaho); Arnott: factor re-rating mean-reverts | bhavcopy + filings (lagged) | B | Conditions factor weights (§6.2), not book beta | D02 |
| L9 | Global financial cycle: dollar/VIX/US-rate state → EM flows | 3–9m (episode); irregular recurrence | Compensated common global factor (Rey; Miranda-Agrippino-Rey); India cannot hedge it away — dilemma-not-trilemma | FRED VIX + dollar index, NSDL FPI, INR | **A (pooled mech.) / B (India transfer)** | ≤20% of budget | D08 |
| L10 | Credit cycle block: Hamilton-filtered credit/GDP gap (own construction, never BIS's HP version), credit-deposit ratio, bank+NBFC aggregate, issuance quality, GNPA (lagging confirm) | 36–72m | Neglected crash risk in credit booms (Baron-Xiong; Schularick-Taylor +2.8pp crisis prob./1σ; Greenwood et al. R-zone ~40% vs 7%); shorting a boom is career-impossible → persists | RBI DBIE, BIS (check only), RBI FSR, CCIL | **B (India) / A (pooled methodology)** | ≤20% of budget (shared with L6/L11/L12) | D03 |
| L11 | Capex/investment cycle | 36–60m | Balance-sheet repair takes years regardless of information (capacity limit) | RBI OBICUS, IIP capital goods, MOSPI GFCF | C→B (via analogues) | Inside macro block, shared cap; correlated with L10 — never double-counted | D08 |
| L12 | Real-estate / medium financial cycle (8–20y; India n≈1: ~2003→2013–20→2021+) | 60–96m | Supply lag under credit amplification (Glaeser-Gyourko); crises cluster at financial-cycle peaks (Borio; Drehmann et al. ~16y avg) | RBI HPI, housing credit, RBI FSR | B (cross-country) / C (India length) | Phase-uncertainty prior only; inside macro block | D07/D08 |
| L13 | Household-debt change (3y Δ debt/GDP: 26%→42% 2015–24) | 36–60m | Debt booms + biased forecasts (Mian-Sufi-Verner); zero completed India down-legs | RBI FSR, BIS | **C** | Reduce-only overlay | D03 |
| L14 | FII positioning extremes (float-scaled ownership percentile — NOT flow momentum) | 12–36m | Unwinding an extreme foreign-ownership stock position requires real capital movement (capacity) | NSDL, quarterly shareholding patterns | **C** | Reduce-only overlay until validated | D08 |
| L15 | Long-wave fiscal/monetary state: public-debt trajectory (level+slope, ~80–85% GDP [V]), persistence of negative real rates, reserve diversification (RBI gold buying, COFER USD share) | 120m+ | Sovereign incentive to repress/inflate away domestic-currency debt is a political-economy constraint nobody arbitrages | IMF WEO/FM, FRED DFII10, RBI WSS, IMF COFER, WGC | **C** | **No regime-score seat.** Expression: structural gold floor attribution (§6.5) + slow-debasement tail budget 0.3–0.6% NAV/yr + conditional gold-floor lift | D07 |
| L16 | Demographic arc (dividend window ~to 2036–41, regionally staggered) | 240m+ | Age structure is data (Tier A); its asset-return translation is conditional on labor absorption (Bloom et al.) | UN WPP, SRS, MOSPI PLFS | A (data) / **C (translation)** | Context only; zero allocation authority | D07 |

**Excluded from the ladder outright** (§13): Kondratiev/Perez waves (each "wave" a different
mechanism — pattern-matching, not recurrence), the 18-year real-estate *point estimate* (folk
numerology; the 10–20y *range* survives via mechanism), the 90% debt/GDP threshold
(Herndon-Ash-Pollin — spreadsheet error + selective exclusion + weighting artifact; corrected
>90% bucket ≈ +2.2% growth), FII flow *momentum* (published, decaying, and DII growth is
absorbing it), Elliott/Gann/fixed calendar cycles (Contract §8).

### 4.2 De-duplication rule
L6 + L10 + L11 + L12 share one **macro-credit block budget** (≤20% of regime score — the number
the registry actually enforces): they are views of the same corporate-leverage phenomenon from the
policy, credit, investment and property sides (D03 §7, D08 §2 both flag the overlap). The registry
enforces the shared cap; the composite uses the first principal component or a simple average —
with **L11 (Tier C) clamped to min(0, reading) before aggregation**, so a hot capex reading can
never add regime-score budget through the shared block (Tier-C reduce-only, enforced in the
validator via `contribution_clamp`), only confirm a deterioration.

### 4.3 What the long waves buy (and only this)
Consequence of the tier system (Contract prior #2): a 200-year debt arc moves the book ~1.5pp.
Concretely: L15 justifies (i) the *existence* of the structural gold floor (§6.5) and ~40–50% of
its size (mechanism attribution, D07 §4); (ii) a slow-debasement tail budget of 0.3–0.6% NAV/yr
(distinct from the fast-crash budget §5.5); (iii) a conditional +1–2pp gold-floor lift only when
debt-trajectory ∧ negative-real-rate-persistence ∧ active-reserve-diversification co-occur —
reverting when any leg lapses. Nothing else. No timing calls, no equity beta, no leverage.

---

## 5. The risk system: regime matrix and drawdown machinery

### 5.1 Regime score and matrix
A composite regime score R ∈ [−1, +1] built as the **equal-weight-anchored combination** (Rapach-
Strauss-Zhou: combinations beat single predictors out of sample [X]) of the Tier-A/B ladder
entries, with budget caps per §4.1 (fast layer ≤25%, trend/TSMOM ≤20%, macro-credit block ≤25%,
global cycle ≤20%, valuation/sentiment ≤10%, calendar ≤5%). The **Tier-C overlay** may only push R
down, by at most 0.10. R maps to four regime buckets — the sweep dimension the hedge grid crosses:

| Bucket | Entry condition (form, not fitted) | Leverage range | Effective hedge ratio (grid 0–150%) | Option channel |
|---|---|---|---|---|
| R1 Benign | R in upper region; no fast trigger | 1.0–1.5x (hurdle-gated) | 0–25% | off |
| R2 Watch | R mid; single slow signal deteriorating | 1.0–1.15x | 25–50% | off |
| R3 Slow bear | trend layer flipped + macro block negative | 0.6–0.9x | 50–100% | rule-armed |
| R4 Crisis/fast | fast triggers fired (L2) regardless of R | 0.4–0.6x | 100–150% | **on (rare buying, budgeted)** |

*(R4 was tightened from 0.4–0.7x / 75–150% by the registry validator's worst-case check: at
leverage 0.7 and hedge 0.75, effBeta×38%-fall + 15% gap floor = 37.9% > the 35% absolute ceiling.
The CI registry caught this; reading the table had not — the METHOD's point exactly.)*

Bucket boundaries are quantile/sign rules on R's own history — no fixed numeric thresholds.
Transitions R1→R4 can jump (fast triggers override); re-entry follows §5.7. With <10 observed
transitions in India, this is a **rule-based state machine, never a fitted Markov switch**
(Psaradakis-Sola instability; Contract §8).

### 5.2 The binding-constraint arithmetic (identity every knob must satisfy)
```
EffectiveBeta(bucket) = DownsideBetaTilt × Leverage(bucket) × [1 − HedgeRatio(bucket) × HedgeEffectiveness(bucket)]
PortfolioDD(episode) ≈ EffectiveBeta(path) × NiftyDD(episode) + GapFloor
```
DownsideBetaTilt ≈ 1.1–1.3 [I]; HedgeEffectiveness ≈ 0.6–0.75 slow bear / 0.45–0.6 fast crash
[A — basis+gap discount, D04; **unmeasured Tier-C input: the R4 worst-case check breaks if true
fast-crash effectiveness falls below ≈0.33**, plausible when tail names are limit-locked — measure
before treating the check as settled]; GapFloor ≈ 10–15% under rare-options design (§2.5). Worked
check: R3 at 0.75x, hedge 75%, eff. 0.65 → EffBeta ≈ 0.42–0.50 — comfortably below the index in a
slow bear. R1 at 1.15x unhedged → EffBeta ≈ 1.3–1.5: **the system must not still be in R1 midway
through a qualifying episode** — that is the whole job of L2's fast layer plus the slow blocks.

### 5.3 Fast layer (the only defense against fast crashes)
Triggers (all rank/quantile forms): (a) short-window realized vol in its top trailing decile;
(b) India-VIX backwardation; (c) funding/flow stress (CCIL repo/CP spread rank, sustained FII
outflow run). Any single trigger → R4 risk-cuts begin (de-gross first: sell liquid names, cut
margin); two independent channels → full R4. Evidence: these are reactive (same-day to ~2-day
lead, Mar-2020 India-VIX 25→64→~80s), never predictive [I]. Honesty per Contract prior #8:
**fast crashes cannot be met by cycles** — the fast layer + §5.5's option rule cut the loss; the
GapFloor remains.

### 5.4 Leverage as a function of state (Decision Q3: margin funding on cash names)
```
Leverage(t) = clip( L_base(book) × f(Surplus(t)) × g(bucket) × h(funding hurdle), 1.0 floor…, cap 1.5x )
Surplus(t)  = [NAV(t) − α·Peak(t)] / NAV(t)          (Grossman-Zhou cushion; α swept, not fitted)
h(·)        = 1 only if E[r_proxy] − funding_rate > buffer, else caps leverage at 1.0
```
plus two margin-funding-specific rules: (i) **no leverage while debt sleeve above policy floor**
(negative carry, §2.4); (ii) a margin-call pre-buffer — leverage is cut at a cushion level above
the broker's maintenance trigger, so forced selling never sets the pace [T]. Averages consistent
with the DD ceiling: ~1.10–1.15x aggressive, ~1.05x moderate, 1.0x conservative (prior #4,
re-affirmed by §5.2 arithmetic).

### 5.5 Hedging stack (Decision Q4: de-gross first, options rare and rule-triggered)
Priority order: (1) sell/trim cash equity (liquid names first — tail names may be band-locked);
(2) cut margin leverage to 1.0x; (3) index futures short (Nifty; Bank Nifty only for measured
beta) for speed when cash exits would cost more than basis risk — permitted within Decision Q2's
hedge-only channel; (4) **rare option buying**: index puts / put spreads, bought only on L2
triggers or R4 entry, premium budget ≈0.5–1.5% NAV/yr [A], positions closed before expiry
(exercise-STT trap, D05/D12 [I]). VRP evidence says permanent protection is a losing budget line
(Israelov; Israelov-Nielsen [X]) — which is why the option channel is state-gated, exactly as the
principal chose. The 7-point hedge grid × 4 regime buckets (≤28 cells) is swept **jointly** in
validation; the full grid enters the deflated-Sharpe trial count (§11.6).

### 5.6 The drawdown constraint, testable form (Decision Q5)
```
VIOLATION ⇔ PortfolioMDD > 20%
           ∧ [PortDD(t) − NiftyDD(t)] > ε   for more than K consecutive trading days
ABSOLUTE  : PortfolioMDD must never exceed 30–35% (hard ceiling)
ε = z × TE_daily × √K   (z ≈ 1; TE = realized tracking vol of the book vs Nifty 50, measured over
a trailing window W — W is itself a swept [A] parameter, {30, 60, 90} sessions, because tracking
vol is regime-dependent and ε is not well-defined until W is fixed; consistency-audit finding)
K ∈ [10, 20] trading days (center 15); sensitivity swept over z ∈ {0.5, 1, 1.5}, K ∈ {10, 15, 20}
```
For an aggressive book at TE ≈ 8–12%/yr, ε ≈ 2–3% over 15 days — transient beta overshoot in a
volatile fall does not violate; a sustained one does. Flash crashes need no special exclusion:
they produce only transient excursions, handled automatically. Episode set to validate against
(rebuilt from primary bhavcopy in the data phase): 2000-01, 2004, 2006, 2008 (−60%), 2010-11
(−28%), 2013, 2015-16 (−25%), 2018 SMID, 2020 (−38%, 69 sessions), 2022 (−18%, non-qualifying),
2024-25 (−17%, non-qualifying), **May-2026 (non-qualifying for equity DD: an INR/FII-outflow
crisis — rupee to a record ~₹96.6–96.8/$, Nifty only ≈−4% acute / −1.9% for the month, India VIX
~18.6; verified by the citation audit). The 2026 episode is instead the near-real-time test case
for the L9 global-cycle/FII trigger and the gold-INR mechanics of §6.5.**

### 5.7 Cash-calls and re-entry (Decision Q8: per-sleeve families)
Exit rules are owned by the regime matrix (bucket transitions). Re-entry, specified with equal
precision, per sleeve family:
| Sleeve | Re-entry family | Form | Rationale |
|---|---|---|---|
| Factor book (slow) | Hysteresis | re-enter when the exiting indicator crosses back through a band wider than the exit line | whipsaw kills slow sleeves' cost budget (Zakamulin lag-noise trade-off [X]) |
| Momentum/fast sleeves | Vol-target implied | exposure scales back up as trailing sleeve vol falls through its own quantiles (Barroso-Santa-Clara form) | risk-managed momentum evidence [X][I] |
| Leverage | Grossman-Zhou surplus | mechanical: cushion rebuilds as NAV recovers vs peak | theory [T]; peak only resets upward — natural hysteresis |
| Post-R4 book-level re-entry | Calendar tranches + state gate | 2–3 tranches over weeks, each gated on the fast triggers staying quiet | recovery alpha clusters early, but single-print re-entry into a renewed leg is the failure mode [X] |
Whipsaw counts per rule are a **frequency-counting exercise in the data phase** (not backtest-Sharpe
tuning): count true catches vs false fires per candidate on the §5.6 episode set, pre-registered.

---

## 6. The return system

### 6.1 Momentum sleeves (aggressive book primary; moderate modifier only)
- **Construct**: equal-weight **rank blend** of 12-1 and 6-1 total-return momentum plus
  52-week-high proximity — never raw z-scores or fixed return thresholds. Skip-month retained
  (reversal contamination; Jegadeesh-Titman, Novy-Marx [X]).
- **Rejected as standalone**: 3-1 momentum (no independent survival argument; overlaps the
  reversal zone — D01). Never re-tested as "2-1"/"4-1" without a new pre-registered mechanism.
- **India anchor**: AJV WML ≈21.9%/yr (1994–2014, long-short, survivorship-corrected) [I].
  Planning number after the 25–35% haircut: ~14–16%/yr gross long-short → long-only implementable
  fraction materially lower; falsifier: if the post-2015 point-in-time sub-sample premium is
  materially below the 1994–2014 average, raise the haircut toward 58%.
- **Liquidity discipline** [I]: momentum lives in the *liquid* tercile in India; the illiquid
  tercile *reverses* (Chui et al. 2023) — the tail sleeve therefore runs quality/value+neglect,
  NOT momentum. Copy NSE's own index hygiene: exclude names at circuit ≥20% of recent days,
  exclude ASM/GSM stage ≥2, avoid reconstitution-pop entries (effect fades in 10–60 days [I]).
- **Crash guard**: scale sleeve gross by inverse trailing vol of the momentum spread itself
  (Barroso-Santa-Clara: Sharpe 0.53→0.97, crashes "virtually eliminated" [X]; India replication
  directionally confirms [I]) + Daniel-Moskowitz bear-state cut (market-return quantile in worst
  historical bucket). Both quantile forms.
- **Turnover budget**: aggressive fast sleeve ≤200%/yr of its own capital; moderate: momentum
  acts only as a rank tiebreaker/modifier inside the factor book's quarterly turns (≤1/5 of the
  200% budget — Israel-Moskowitz 5× turnover ratio [X]).

### 6.2 Factor book (moderate book engine; conservative's projection)
Core sleeves with risk-budget weight ranges (conditioning below; §10 haircuts applied):
| Sleeve | Weight range | Construction notes | Tier |
|---|---|---|---|
| Value | 20–35% | Composite of dividend yield, net-share-issuance (Pontiff-Woodgate — price/shares only, restatement-proof), sales/price; B/P and E/P as lag-buffered minority (≥4–6 month reporting lag per AJV convention) — **>50% of the composite must be price-adjacent** given the 150–450bps restatement bias (prior #7) | A global / B India |
| Quality | 20–35% (floor binds in late-cycle states — crisis ballast) | Standard profitability/stability components **plus India-specific junk terms: promoter-pledge intensity and RPT-disclosure flags** (free, point-in-time SAST/LODR filings; pledge-invocation cascades are mechanical crash risk — Zee, CCD, Cox & Kings, Vakrangee… ≈10–15 episodes 2015–23 [I][V]) | A global / B India |
| Low-vol | 15–25% | **Pure realized-vol rank** (price-only), explicitly NOT the alpha-blended Nifty Alpha-Low-Vol-30 construct; India academic evidence is genuinely split — live-index Tier-B is an upper bound; AUM-growth-rate crowding trigger attached | A global / B India (contested) |
| Size (quality-controlled) | 0–15% satellite | Raw India SMB ≈ 0 over 20y (AJV) — inadmissible; the Asness-et-al junk-controlled version is **very likely estimated on MSCI-World developed markets only (India excluded)** → a pure cross-country extrapolation, satellite only until the pre-registered India test runs | A global / **C India** |
- **Conditioners**: value weight rises toward its top when the value spread's own 10y percentile
  is in its top tercile (Cohen-Polk-Vuolteenaho [X]); quality weight cut toward floor when the
  quality basket's relative valuation is in its top decile (the 2024–25 quality re-rating/unwind
  is the live Arnott warning [X]); tilts toward momentum when the value spread is bottom-tercile.
  All quantile rules, Stambaugh-corrected when estimated (§11).
- **Fundamental data discipline** (prior #7): every fundamentals-based signal ships with its
  price-only counterpart; no fundamental backtest is ever reported without it.

### 6.3 Tail / neglect sleeve (aggressive book; ranks 300–750 at 1–2% tickets)
The capacity-protected sleeve: an absolute-₹ sleeve (not %NAV) harvesting the illiquidity/neglect
premium the moderate book's universe excludes by construction [I]. Long-hold (≥1y design),
value/quality-selected, momentum explicitly not used here (§6.1). Hard filters: band-lock
frequency percentile (D12's per-stock "fraction of days closed at band" statistic — a data-phase
build), GSM≥2/T2T exclusion, SME platforms excluded entirely. Position sizes capped by
build-time ≤ signal half-life (§7.4). This sleeve is where the aggressive book's smallness is the
edge; it shrinks as %NAV as the book grows through ₹100→250cr — stated, not hidden.

### 6.4 Special-situations satellite (Decision Q10: aggressive only, Tier-B rules frozen at inception)
| Event | Rule form | Tier | Notes |
|---|---|---|---|
| Index inclusion/exclusion (Nifty/MSCI/FTSE) | trade announcement→effective window, flow-sized | B, **rising decay** | India today ≈ US 1990s on passive share; re-estimate the effect every cycle — never freeze a decade number [I][X] |
| Demergers/spin-offs | hold parent+spinco 3–12m through forced index selling | C→B pending India event study (20–40 candidate events 2000–25) | Cusatis-Miles-Woolridge mechanism [X]; India registry is a data-phase build |
| Buyback tender / open offer / delisting arb | deal-by-deal, spread vs proration/approval risk | B | capacity-capped by regulation (tender sizes, 90% delisting bar — real binary risk) [I] |
| Anchor/promoter lock-in expiries | **risk-reduction only**: no adds ±5–10 days around disclosed 30/90-day unlocks | C | Field-Hanka mechanism [X] — but a ~Aug-2026 SEBI study (242 mainboard IPOs, 2022–25) finds anchor exits are **gradual, not cliff-like** (≈3.2% sold at 30d, ≈17.3% by 90d), so the expected India effect is much weaker than the US analogue; the no-adds rule stands only as a cheap conservative default [I, verified] |
| Bulk/block/PIT-disclosure following | ranks 500–750 only; sign/quantile form | C→B pending test | attention+capacity argument only survives in the tail [I] |
| IPO participation (allotment) | **not a sleeve** — allotment is a lottery, not a scalable entry | — | SEBI flipping study [V]; post-listing drift folds into quality flag ("newly-listed" penalty) |
Sleeve cap: ≤10% of aggressive NAV [A — the least-defended number in D12; must be re-derived from
the deal-flow census before it binds]. Sizing input: L7 issuance-cycle state (froth ⇒ shrink).

### 6.5 Gold (ETF core + futures tactical; Decision framework from D06)
```
GoldWeight(book,t) = Floor(book) + TacticalBand(book) × S(t),   S ∈ [0,1]
S = 0.15–0.20·RealRateInput + 0.20–0.25·CB-BuyingRegime + 0.20–0.25·INR/REER tilt
  + 0.15–0.20·GoldMomentum(12m/6m rank, 35–45% haircut) + 0.15–0.20·CrisisKicker
```
Floors: conservative 8–12%, moderate 4–7%, aggressive 2–4% [X mechanism / C sizing]. Ceilings
(floor+band): ~15–25% by book — far below the 50% mandate cap; no non-sponsor evidence supports
more (WGC "optimal allocation" studies excluded as conflicted). Input notes: the real-rate link is
half-weighted post-2022 (central-bank-buying regime broke it; that regime enters as an exogenous
WGC/RBI series with zero assumed persistence — no fitted switch); INR-gold returns decompose as
USD gold + INR depreciation (structural CAD/inflation-differential trend, Rogoff PPP half-life
3–5y [X]) — but 2013 proves depreciation does not always rescue gold's INR return in a crisis;
duty changes (2013 hikes, Jul-2024 cut [V]) are level breaks, never fit through. Crisis kicker
sized at ~50% of developed-market safe-haven estimates (Baur-McDermott: BRIC safe-haven weaker) [X].

### 6.6 Debt sleeve and the policy portfolio
Debt = flat 10% bookkeeping assumption (frozen), realistic yield ~6.5–7.5% — the ~400bps/yr
markdown is stated everywhere returns are aggregated. Policy portfolio per book-state: equity
policy weight from the regime bucket, gold from §6.5, debt = 100% − equity − gold (floor: never
below 0; cap 70%), **never optimizer-derived** (Michaud/BHB-Ibbotson-Kaplan correctly read: policy
explains a fund's own time-series variance, ~40% of cross-fund variance, ~100% of the average
fund's return level [X]). Leverage and the debt sleeve are mutually exclusive above the policy
floor (§2.4). Debt instruments: whatever the desk's cash-management vehicle is — no credit model,
no duration overlay (frozen).

### 6.7 Tactical short sleeve (Decision Q2 extension)
Base short side = index hedging only (§5.5). Additionally, a **tactical single-name short sleeve**:
Nifty-100 constituents only; instruments = single-stock futures and defined-risk option structures
(put spreads, multi-leg combos); capped at **≤25% of total short-side exposure**; delta counts in
the 1.5x gross cap. Admissible triggers (each needs its own pre-registered survival argument;
evidence today is thin → sleeve starts at zero and earns size): pledge-invocation cascades in
progress [I], index-deletion flow windows [I], crowding/froth flags (L7) on single names. Costs:
SSF roll + ban-period risk (MWPL 95% blocks new positions [I]); squeeze risk capped by
defined-risk structures. Until a signal passes the §11 gates this sleeve is **Tier C: usable to
reduce net exposure in R3/R4, not as standalone alpha**.

---

## 7. Stage-3 construction (equity cross-section only)

### 7.1 Optimizer form (D11)
**Characteristic/parametric portfolio policy** (Brandt-Santa-Clara-Valkanov): active weight is a
smooth, monotone, saturating function of the name's blended signal-percentile rank — no expected-
return vector exists anywhere in the system. Ledoit-Wolf-shrunk covariance (calibrated on Indian
returns; no options-implied alternative exists beyond ~150–200 F&O names [I]) used **only** for:
(a) risk-scaling weights where marginal variance contribution is outsized vs signal strength,
(b) surfacing correlated sector concentration (fully-active mandate ⇒ report, don't neutralize).
```
active_w_i = clip( g(rank_pct_i(signal_blend)) × risk_scale_i(Σ_LW), 0, cap_i )
```
Rejected: literal MVO (estimation-error maximizer — DGU/Best-Grauer/Michaud [X]); Black-Litterman
(an asset-allocation tool; the asset mix is policy, and per-name views re-import estimation error).
Long-only + norm caps are themselves performance-positive (Jagannathan-Ma; DGNU [X]) — the frozen
caps are not just risk controls.

### 7.2 Name count: N(book, w_eq, D)
```
N* = N_floor(book) + [N_ceiling(book, w_eq) − N_floor(book)] × (1 − D)
D  = trailing cross-sectional dispersion percentile of the book's universe (expanding window)
N_ceiling = w_eq / avg_min_weight(book)
```
Floors/ceilings per §1 table. Basis: Evans-Archer/Statman diversification floor (30–40+, rising
with idio-vol per CLMX; read as a **lower bound** in India's promoter-correlated, retail-heavy
tail) [X]; Bessembinder skew (missing the rare compounders is the cost of over-concentration —
soft floor ~12–15 for the aggressive book) [X]; Cohen-Polk-Silli/Cremers-Petajisto concentration
evidence licenses the aggressive book's low floor — and the survival argument is institutional:
career-risk-constrained funds cannot copy a prop book's concentration [X]. High dispersion ⇒
concentrate toward the floor (a given IC buys more per bet — Gorman-Sapra-Weigand [X][V]); low
dispersion ⇒ spread toward the ceiling. Low-w_eq edge case: relax avg_min_weight rather than
breach N_floor. Grinold-Kahn (IR = TC·IC·√BR) is a sanity check only — IC is never assumed as an
input to set N (breadth is also overstated when bets correlate across managers).

### 7.3 No-trade bands per signal half-life
```
band(signal, bucket) = 10%_drift_ceiling × h(τ½) × (cost_bucket / cost_ref)^(1/3)
h(τ½) = τ½ / (τ½ + τ_ref)        (saturating; τ_ref calibrated so the fastest ladder signal ⇒ h ≪ 1)
```
Gârleanu-Pedersen: trade partially toward a moving aim; slow signals ⇒ wide bands (aim barely
moves), fast signals ⇒ tight bands (2–4% pre-cost-adjustment) or the transient alpha is forfeited
[T/X]. Constantinides cube-root: the cost adjustment is gentle (a 3–4× cost gap ⇒ only ~1.4–1.6×
band widening) [T]. Breach handling: trim partially to the band edge, not to target (Davis-Norman)
[T]. ASM/GSM-flagged names: bands are a lower bound on realized drift — a banded name may simply
not trade. Independently reproduces prior #10's "5× half-life ⇒ 1/5 turnover" from first
principles — a good cross-check that theory and the data-derived prior agree.

### 7.4 Position sizing (three-way minimum, cushion-scaled)
```
size_i = min( frozen_cap (5–6% entry / 10% drift),
              f_Kelly × μ_haircut,i / σ²_i          with f_Kelly ∈ 0.15–0.35 [A],
              buildable-within-τ½ size (participation-capped days-to-build ≤ signal half-life) )
        × c(DD),   c(DD) = max(0, 1 − DD_current/DD_ceiling)^p,  p = 1 initial [A]
```
- The frozen 5–6% cap ≈ 1/10–1/15 of naive single-name full Kelly — consistent with (in fact
  conservative under) the drawdown-constrained Kelly literature (Grossman-Zhou; MacLean-Thorp-
  Ziemba: half-Kelly keeps 75% of growth at 25% of variance) [T]. Not amended.
- μ_haircut is the **decay-haircut** alpha (§10), never raw backtest alpha — sizing is
  decay-aware by construction: revise a signal down and its positions shrink automatically.
- Staged entry: equal daily tranches at the participation cap initially; Almgren-Chriss
  front-loading is a post-launch refinement. In-progress budgets per §2.7 (two cohorts).
- Rebalance-timing luck: signal measurement and execution staggered in tranches across each
  sleeve's cadence window (Hoffstein et al. [X, practitioner]); the tail sleeve gets this free
  via multi-week builds.

---

## 8. Stage-2 charter (advisory-only until proven — Decision Q7)

### 8.1 The evidentiary starting point (why the burden of proof is inverted)
Grove-Meehl meta-analysis (136 studies): mechanical prediction beats or ties free-form expert
judgement in ~85–95% of measured settings [X][V]. Kleinberg et al. (750k bail decisions): a simple
consistent rule Pareto-dominates real-time expert discretion built on the same information [X][V].
Tetlock: free-form narrative conviction forecasting performs at ≈chance; structured, scored,
teamed forecasting (GJP protocol) genuinely works [X]. Kahneman-Sibony-Sunstein: noise usually
exceeds bias; the fix is decomposed, independent, checklist-scored judgement [X]. Therefore the
Stage-2 expected marginal contribution is **zero-or-negative by default (100% haircut at
inception on any authority)**; authority is earned by track record, never by argument. The one
legitimate standing role is Meehl's broken-leg case: discrete, rare, highly diagnostic facts
structurally outside Stage-1's variable set (India examples: pledge invocations, regulatory
actions, index-flow events, war/sanctions).

### 8.2 The authority ladder (amended for Decision Q7)
| Rung | State | Authority |
|---|---|---|
| **−1 (inception)** | **Advisory-only shadow book** | ZERO effect on the traded book. All three channels run, logged, Brier-scored. Exit: pre-registered paired test (§8.3) passed at the high bar over ≥2 consecutive windows AND n≥20 scored theses with BSS>0 |
| 0 | Reduce-only | May cut any Stage-1 position ≤50% of its current weight, shrink gross, raise hedge one grid step early within the regime-permitted band. Never adds |
| 1 | Limited add | n≥20 more scored theses at Rung 0, BSS>0, paired IR non-negative → add to existing Stage-1 names only, ≤25% of position or ≤1.0pp NAV per instance, ≤2pp aggregate |
| 2 | Fuller add | n≥50, BSS>0 two consecutive windows, paired IR/DD passing both → ≤50%/≤2.5pp per instance, ≤5pp aggregate; may request one risk-adding hedge-grid step within regime band |
| Demotion | automatic, immediate | any window with BSS<0 or paired IR/DD below Stage-1-only → straight back one rung (from 0 → back to −1) |
The n-floors deliberately reuse the Contract's own Tier-B band (4–30) as the evidentiary
convention; effective-n must be autocorrelation-adjusted before unlocks count (correlated macro
theses are not independent observations).

### 8.3 The gate
Shadow Stage-1-only vs Stage-1+2 run in parallel from identical weights; paired difference in net
IR (Wilcoxon signed-rank / Jobson-Korkie-Memmel with Harvey-Leybourne-Newbold small-sample
correction) AND a non-inferiority test on episode drawdown under §5.6's definition — **a good IR
never offsets a DD deterioration**. Pre-registered one-sided tests, locked before the first live
override, never re-cut. All Stage-2 sweeps enter the program's cumulative trial ledger.

### 8.4 The three LLM channels (Decision Q9) and the ledger
1. **Structured scorer**: LLM converts news/policy/geopolitics into pre-registered checklist state
   scores with hard caps (GJP house style: numeric probabilities, defined horizons).
2. **Red team**: adversarial attack on the Stage-1 portfolio — crowding, correlated theses, stale
   signals, unpriced discrete risks. Proposer and red-teamer are always distinct roles (no
   self-critique — sycophancy/consistency bias); direction-level disagreement escalates to
   human-only adjudication.
3. **Tactical thesis / buy-call generator** with mandatory human veto: free-form ideas enter the
   ledger like any thesis — during Rung −1 they trade nothing.
Ledger fields (all channels, human or AI): thesis, direction, magnitude, explicit horizon,
mechanism tag (one of the four survival categories or "genuinely novel information"), numeric
probability, falsifier, red-team entry, mechanical hard-cap checklist, outcome + Brier at
resolution, and for AI theses: model ID/version, prompt hash, verbatim log. **A model-version
change resets that component's track record to n=0 AND forces an immediate step-down to the rung
below (probationary hold with the lower rung's caps) until the new version re-earns its unlock**
— otherwise a channel could swap models before a bad window resolves and keep authority earned by
weights that no longer exist (documented LLM behaviour drift [X]; red-team finding).

### 8.5 Why Stage-2 LLM output can never be backtested (hard rule)
Lopez-Lira & Tang's headline LLM backtest is Exhibit A of the failure mode; Glasserman-Lin
(arXiv 2309.17322, verified) show the mechanism: training corpora postdate the "predicted"
events, so the model may be recalling outcomes. Nuance recorded honestly: their own anonymization
procedure *partially* mitigates the bias (and they find a "distraction effect" that can dominate
the look-ahead component) — so contamination is partially correctable, not categorically
unfixable. This design still adopts the stricter rule as a conservative choice, because the
residual contamination cannot be independently audited from outside the weights: **any historical
backtest of an LLM-generated forward view is inadmissible evidence at any tier, regardless of
significance.** Evaluation is prospective-only — which is exactly what the
advisory-first ladder provides. Human execution gate at every rung (never relaxes): required by
the broken-leg doctrine and prudent under SEBI's algo-trading/AI-reporting perimeter [I][V —
compliance counsel item].

---

## 9. Costs, capacity, and turnover budgets

### 9.1 Statutory stack (verified FY2026-27 [I]; re-verify every Budget)
Cash delivery ≈ 22.3bps round trip statutory (STT 0.1% both legs dominates) + brokerage [A:
1–5bps/side placeholder] + spread/impact ⇒ **24–32bps floor**, liquid names. Index futures ≈
5.7bps statutory ⇒ 8–16bps all-in (≈4× cheaper than cash; corrected by the consistency audit). Options: STT 0.15% of premium (sell side) but **0.15% of
intrinsic on exercise** — hedge payoffs modeled with pre-expiry close-out, exercise-STT costed on
the forced-exercise path. STT has been hiked twice in ~18 months — the rate table is a live
registry entry with an expiry date, and a further hike is a named risk to every cost assumption.

### 9.2 Impact and capacity (square-root law, Y ∈ 0.5–1.0 [X]; ADV table provisional [A])
Impact ≈ Y·σ_daily·√(Q/ADV). Consequences (D05 §4c–4g): the effective-universe table in §1; a
5.5% entry is cheap only in ranks 1–50 for any book; the ≤20% in-progress cap allows only 3–4
simultaneous full-size builds ⇒ conservative-book pipeline throughput ≈15–20 full-size positions/yr
— compatible only with a low-turnover value/quality engine (independent re-derivation of prior
#10). Capacity claims per sleeve are re-run whenever book AUM moves ±50%.

### 9.3 Turnover budgets and hurdles (per book, one-way)
| Book | Design point | Cost at design point | Ceiling | Extra gross alpha the ceiling must earn |
|---|---|---|---|---|
| Aggressive | 250–350% | ≈1.5–3% NAV/yr | 600% | ≈3.0–6.0pp/yr vs the 100% book (D05 §4h re-derivation) |
| Moderate | 100–160% | ≈0.6–1.5% | 200% | factor core ~60–100% + momentum modifier ≤40% |
| Conservative | 40–75% | ≈0.3–0.7% | 100% | — |
Cost is a function of **where** turnover is spent (rank-bucket mix), not aggregate turnover — the
registry stores per-bucket coefficients and evaluates proposed trade lists against the actual mix.

---

## 10. The decay ledger (every edge: survival argument + stated haircut)

Base rates: McLean-Pontiff −26% out-of-sample, −58% post-publication (US); Jacobs-Müller: the
post-publication leg is largely a US phenomenon — international anomalies persist because
arbitrage frictions persist; Chordia et al.: attenuation tracks arbitrage capital and liquidity.
India inference: apply the −26% leg by default; apply the −58% leg only where India-specific
crowding evidence exists or the signal is fast/liquid enough for arbitrage capital to reach.

| Edge | Survival argument (category) | Haircut | Falsifier / revisit trigger |
|---|---|---|---|
| Momentum 12-1/6-1 (India) | behavioural diffusion + thin coverage (i) | **−25–35%** off AJV 21.9% | post-2015 PIT sub-sample weak → raise toward −58%; ALSO: a smart-beta AUM/crowding monitor (mirror of low-vol's) — the mid-2025 "quant unwind" named momentum as a participant, disconfirming complacency about the low haircut (red-team finding) |
| 52-week-high | anchoring (i); no long-run reversal in source evidence | −20–30% [A] | India test (none exists) |
| TSMOM index | institutional constraint (iv) | −10–20% | India cost-inclusive estimate |
| Gold momentum | (iv) + CTA capacity | −35–45% | measured India half-life |
| 1-month reversal | liquidity provision (iii) but cost-dominated | **zero return budget** (Tier C) | India PIT cost-inclusive estimate could earn a small budget |
| Value (India composite) | risk premium + extrapolation bias (iii)+(i) | −30–40% | value-spread conditioner fails Stambaugh-corrected OOS test |
| Quality + pledge/RPT junk terms | (i) + India institutional (iv); pledge cascades are mechanical | −25–35% on imported QMJ; **India junk terms weighted at 50% pending the episode study** — "survives crowding" is not "has no estimation uncertainty": the pledge evidence is a case count, not a measured effect size (red-team finding) | India episode study contradicts crisis-ballast role |
| Low-vol | leverage constraints (iv) — but India evidence split | −30–40% | resolved India study; min-vol AUM growth trigger |
| Size (quality-controlled) | (ii)+(iii) — untested in India | sized as satellite 0–15%, treat as unproven | pre-registered India test (highest-value single test in the program) |
| Credit/crisis block | neglected crash risk (i) + limits to arbitrage (ii) | AUROC prior cut 0.83–0.85 → **0.65–0.75** [A] | first purged India-conditioned AUROC |
| Issuance/sentiment cycle | issuer incentive (i); SEBI actions confirm (iv) | −26–58% band as placeholder | India pre-registered test vs 2018/2023-24 episodes |
| Index inclusion/exclusion | temporary capacity limit (ii) | **rising haircut, re-estimated annually** — India ≈ US-1990s now, decaying as passive AUM compounds | era-segmented re-estimate |
| Special-sits events (demergers, buybacks, unlocks) | structural/regulatory mechanisms, capacity-capped by design (ii)/(iv) | event-specific; sleeve capped ≤10% agg NAV [A] | India event registries (data phase) |
| FII positioning extremes | capacity (ii) | Tier C reduce-only | purged India test |
| Vol targeting / trend de-risking | structural leverage effect + mandated-long-only competitors (i)+(iv) | no haircut on the DD-reduction mechanism; −26–58% on any *return* claim | India replication |
| Concentration (best-ideas/active-share) | career-risk constraint on competitors (iv) | none now; 5-year watch item if prop capital crowds concentration | monitor |
| Stage-2 judgement | broken-leg channel only (iv) | **−100% at inception** (advisory-only) | earns authority via §8.2 ladder only |
| Long-wave block | political-economy constraint (iv), n<2 | no crowding haircut; influence capped at gold floor + 0.3–0.6% tail budget | ≥4 quarters of regime reversal per input |

Design rule (Contract §5): the strategy must clear its hurdle **after** these haircuts. §1.1's
bands are computed from haircut values; nothing in the plan requires an undecayed edge to work.

---

## 11. Estimation and validation protocol (binding for the data phase; full detail D09)

1. **Filters**: Hamilton (2018) regression filter only, never HP. h=8q/p=4 (quarterly business/
   credit band), h=24m/p=12 (monthly flow band) [V: monthly scaling is convention], h≈16–24q and
   32–40q variants for the short-credit and medium-financial bands, exact h chosen by purged CV
   against pooled crisis labels — never in-sample fit.
2. **τ½ estimation**: AR(1) on overlapping windows; Kendall/Marriott-Pope small-sample bias
   correction (E[ρ̂]−ρ ≈ −(1+3ρ)/T); Andrews/Hansen exact methods when ρ̂>0.9; Newey-West/HAC
   errors for overlapping horizons; report confidence intervals, not points; rolling-window
   stability check across the 1991/2003/2008/2016/2020 break dates before trusting full-sample
   estimates.
3. **Predictive regressions**: Stambaugh correction on all persistent predictors (value spread,
   credit gap, CD ratio, FII positioning); Ferson-Sarkissian-Simin spurious-regression caution.
4. **Pooling**: partial pooling on the JST panel via empirical-Bayes shrinkage
   w = τ²/(τ²+σ²_India) — with ≤2 domestic credit down-legs, India-specific weights stay small
   until more cycles complete. India-specific transition matrices still need their own ≥10
   transitions; pooled counts never substitute.
5. **Out-of-sample**: OOS R² vs expanding-window historical mean (Goyal-Welch convention), always
   reported, even negative; Campbell-Thompson sign restrictions only where the sign was argued
   ex-ante; every signal must also add value inside the equal-weight combination benchmark.
6. **Multiple testing**: pre-register every hypothesis (template: hypothesis+mechanism, sample,
   metric, minimum economic effect sourced from the cost stack, stop rule, decision rule);
   rejected ideas are never re-tested with tweaked parameters; **one cumulative program-wide trial
   ledger** (hedge grid × regimes ≈28 cells, factor grids, τ_ref/f_Kelly/p sweeps, Stage-2
   variants all count); promotion to Tier A requires t>3 (Harvey-Liu-Zhu) AND deflated Sharpe >0
   (Bailey-López de Prado, with skew/kurtosis adjustment); CSCV probability-of-overfitting on
   every grid; MinTRL computed before any capital scale-up.
7. **Drawdown statistics**: stationary block bootstrap (Politis-Romano), mean block length
   ≈2–4×τ½ (Politis-White plug-in when sample permits); the 30–35% ceiling checked against the
   bootstrap's 95th/99th percentile, not the point-estimate historical max.
8. **CV mechanics**: purged K-fold with embargo ≥1×τ½ (2× for Tier B/C); **4–6 folds** for
   India-only monthly series (~380 obs), not a textbook 10 — reported as the lower-power test it is.
9. **Regime models**: none fitted below 10 observed transitions — quantile/sign state machines
   instead (this design uses only the latter).
10. **Data integrity**: every series pulled once on the principal's machine, checksummed,
    committed as a fixture; every module testable with zero live data (prior #11); point-in-time
    GDP/fundamentals vintages; price-only counterpart mandatory for every fundamental result.

**Validation gates by phase**: Phase 0 fixtures → Phase 1 per-signal discovery (pre-registration +
survival argument + clock test + τ½) → Phase 2 OOS → Phase 3 significance (t>3 ∧ DSR>0 ∧ MinTRL)
→ Phase 4 regime/nonlinearity (≥10 transitions or quantile rules) → Phase 5 Stage-1 completeness
(mandate-compliant portfolio at every rebalance, no Stage-2) → Phase 6 Stage-2 paired gate →
Phase 7 sweep/overfitting (CSCV) → Phase 8 registry/CI → Phase 9 live monitoring with promotion/
demotion paths (a Tier-A effect whose rolling significance decays is demoted — decay is the
normal fate of real anomalies).

---

## 12. Build sequence (3–6 months, two people; middle-out — every phase ends with something that runs)

Design top-down from the largest cycles; **build middle-out** — long cycles are least validatable
and least actionable; credit/macro is where evidence, actionability and the drawdown constraint
coincide. The moderate book anchors (Decision Q6).

| Phase | Weeks | Deliverable (runs) | Gate to pass |
|---|---|---|---|
| 0. Fixtures & registry | 1–3 | Ingestion on principal's machine → checksummed fixtures (bhavcopy, RBI DBIE, NSDL, AMFI, India-VIX, WGC, FRED, IMF/BIS); `config/` registry + CI validator live; ADV-by-rank table replaces the provisional one; cost-curve function coded | Registry loads clean; every module runs on fixtures with zero live data |
| 1. Price-only factor book (moderate) | 3–8 | Momentum composite + price-only value + realized-vol rank + pledge/RPT junk flags on ranks 1–500; N/band/sizing formulas live; **the instrument that answers the central question (prior #7)** | Phase-1–3 gates per §11 for each signal; Stage-1 completeness on history |
| 2. Risk system | 6–12 | Credit block (Hamilton-filtered gap, CD ratio, bank+NBFC aggregate), global-cycle factor, fast triggers, regime matrix, leverage/hedge state machine, DD-violation monitor (ε,K), episode table rebuilt from primary data incl. 2026 episode | Frequency-counting whipsaw study; §5.2 identity satisfied on all qualifying episodes; block bootstrap DD tail inside ceiling |
| 3. Full moderate book paper-run | 10–16 | Stage 1 + Stage 3 end-to-end at weekly cadence, paper | Mandate caps bind correctly at every rebalance; deflated-Sharpe ledger current |
| 4. Aggressive book sleeves | 14–20 | Fast momentum sleeve (liquid ranks), tail/neglect sleeve with band-lock filter, special-sits registries (demergers, deal-flow census, unlock calendar), tactical-short triggers | Per-sleeve gates; capacity re-derivation of the ≤10% satellite cap and 600% ceiling |
| 5. Conservative projection + gold/policy | 18–22 | Capacity-constrained projection of the factor book; gold weight function on fixtures; policy portfolio simulator (stress, not fit) | SAST/ADV bounds enforced mechanically; §6.5 inputs live |
| 6. Stage-2 shadow launch + fundamentals | 20–26 | Ledger + shadow book live (Rung −1); paired-test harness; fundamentals ingestion with lag stamps → fundamental factor variants **with mandatory price-only counterparts** | Pre-registered gate armed; measured restatement bias vs the 150–450bps prior |
Throughout: citation-verification queue (§15) cleared in parallel; anything unverified stays
Tier-C-capped until confirmed.

## 13. Deliberately excluded (and why)
- **Kondratiev/Perez long waves** — different mechanism per "wave"; analogy, not recurrence (D07).
- **Elliott Wave, Gann, fixed-period calendar cycles** — Contract §8.
- **18-year real-estate clock as a number** — folk numerology; the supply-lag mechanism and a
  10–20y range survive.
- **90% debt/GDP growth cliff** — discredited (Herndon-Ash-Pollin); trend slope only, no threshold.
- **1-month reversal as a return sleeve** — most cost-constrained anomaly + 20bp STT + zero India
  magnitude studies; Tier-C flag only.
- **3-1 momentum standalone** — no independent survival argument (Novy-Marx).
- **FII flow momentum, directional** — published, decaying, and structurally weakening as DII/SIP
  flows grow; positioning-extremes variant retained as Tier-C.
- **Options-premium harvesting** — no argument distinguishes this desk from professionalized
  vol desks already on that side; SEBI retail-loss studies are context, not edge (D12).
- **SME-platform IPOs** — outside the NIFTY-750 universe by construction; liquidity and
  manipulation-enforcement record compound the exclusion (D12).
- **Single-stock options as hedges; margin funding of the debt sleeve; standing put overlays;
  neural-net return prediction; HP filter; fitted Markov switching below 10 transitions** — per
  Contract/decisions above.
- **Monsoon as an index-level signal** — honestly unquantified; at most a sector-level, reduce-only
  confirmer.
- **CMIE/paid data** — free-source rule; OBICUS+IIP+GFCF substitute for capex tracking.

## 14. Epistemic status: what rests on what
**Theory [T]** (survives regardless of data): optimizer-fragility → characteristic portfolios;
Gârleanu-Pedersen band logic; cube-root cost scaling; Grossman-Zhou cushion scaling; Kelly
fraction asymmetry; the §5.2 effective-beta identity; Slutzky/Yule/Granger anti-periodicity case.
**Cross-country evidence [X]** (Tier B for India until replicated): momentum/value/quality/low-vol
existence and crash behaviour; vol-targeting's tail benefit; trend's slow-bear protection; VRP
positivity; credit-boom → crash-risk (pooled AUROC 0.83–0.85); global financial cycle; safe-haven
gold (weaker for EM); clinical-vs-mechanical judgement; issuance-cycle sentiment.
**India-specific [I]** (verified where noted, else [V]): AJV factor magnitudes; SMID downside
betas; statutory cost stack (FY2026-27 verified); ASM/GSM/circuit/T2T mechanics; SAST/pledge
disclosure regime; index-effect fade windows; NBFC-2018 lesson (bank+NBFC aggregate);
credit-cycle chronology; election-day surprise behaviour.
**Assumptions until data [A]** (every one lands in the registry with a re-derivation trigger):
the ADV-by-rank table; hedge-effectiveness 0.45–0.75; gap floor 10–15%; funding rate; brokerage
1–5bps; option budget 0.5–1.5%; f_Kelly 0.15–0.35; p=1 cushion exponent; τ_ref; ε/K parameters;
every τ½; the ≤10% special-sits cap; AUROC 0.65–0.75 haircut; the 22–28% stretch case.

## 15. Verification queue (highest-priority [VERIFY] items, consolidated)
The shared web-search budget was exhausted mid-sweep; dossiers 05–12 lean partly on flagged
recall. **Nothing unverified may be promoted past Tier C into the frozen registry.** Priority:
1. Glasserman-Lin LLM look-ahead paper (underwrites §8.5) and Lopez-Lira-Tang statistics (D10).
2. The SEBI IPO-flipping/anchor-selling study — title, venue, percentages (D12).
3. The 2026 India market-stress episode — entirely post-cutoff; rebuild from primary data (D04).
4. Grove et al. (2000) meta-analysis percentages; Kleinberg et al. figures (D10).
5. Baron-Xiong secondary specification; the RBI "7y/17y credit cycle" study (D03).
6. FY2026-27 statutory rates re-check + Frazzini-Israel-Moskowitz impact coefficients (D05).
7. Hamilton-filter monthly h/p convention; DSR formula constants; Memmel variance formula (D09).
8. Index-derivatives expiry regime details post-SEBI-curbs; SEBI algo/AI-reporting perimeter
   (compliance counsel) (D12/D10).
9. Nifty episode table exact peaks/troughs (2013, 2015-16, 2024-25) from primary bhavcopy (D04).
10. Erb-Harvey coefficients; gold duty dates; SGB discontinuation; ETF/roll costs (D06).
Full lists: each dossier's §7. The adversarial verification pass (see `research/register/`)
tracks item-level status; the registry's `verify_status` field gates tier promotion in CI.

---
*End of design document v0.9. Machine-readable encoding: `config/`. Evidence: `research/dossiers/`.
Decisions: `research/OPEN_QUESTIONS.md`. Next action per §12: Phase 0.*
