# Deep-dive #2 — Fast Stress (L2, the reactive switch)

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
