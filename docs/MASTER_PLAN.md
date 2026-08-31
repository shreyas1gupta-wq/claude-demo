# MASTER PLAN — Cycle-Stack Program: Research → Moderate Model → Three Books → Decade

Version 1.0 · 2026-08-31 · Companion to `docs/DESIGN.md` (the verified design, v0.9-post-audit).
DESIGN says *what* the system is; this plan says *how it gets built, validated, capitalized and
kept alive*, step by step, with owners, effort, dates and numeric gates.

**Sequencing principle (principal's directive, 2026-08-31, confirming Decision Q6):**
1. **Track R first** — the shared research & estimation program: every regression, filter,
   calibration, event study and descriptive measurement that all three books consume. Nothing
   book-specific is assembled until the shared empirical layer exists, because every model
   parameter traces to it.
2. **Track M second** — the moderate model is the first complete model assembled on that layer.
3. **Tracks A and C** — aggressive sleeves are added on top; conservative is derived as the
   capacity-constrained projection. Stage 2 launches in shadow only after Track M runs.

Appendices (in `docs/masterplan/`): **A** data catalog (every series, exact access path, fixture
spec) · **B** module & test specifications (repo layout, ~35 modules, DAG, effort) ·
**C** pre-registration hypothesis register (every regression/test, pre-registered) ·
**D** program risk register. This core document references them as A/B/C/D.

Provenance tags as in DESIGN: [T] theory · [X] cross-country · [I] India-verified ·
[A] assumption-until-data · [V] carries open verification flags.

---

## 1. Program logic and end states

### 1.1 Why research-first, moderate-first
- Research-first: the same τ½ estimates, cost curves, episode tables, factor premia, and cycle
  states parameterize all three books. Estimating them once, pre-registered, on the shared trial
  ledger is the only way the deflated-Sharpe accounting stays honest — three books testing the
  same hypothesis separately would triple-count discoveries and hide the true trial count.
- Moderate-first: its engine (value/quality/low-vol) has the longest signal half-lives → lowest
  cost per unit of authority → the cleanest test of whether the program works at all. The
  aggressive book's distinctive sleeves are the *least* decay-defensible parts of the design;
  building them first would front-load the riskiest research (DESIGN §1). The conservative book
  is arithmetic on top of the moderate book (capacity constraints), not new research.

### 1.2 End-state definitions (what "done" means)
| Horizon | Done means |
|---|---|
| **H1 — Month ~3** (Track R complete) | Every fixture committed & checksummed; every ladder τ½ estimated with CIs; cost curves live on real ADV; episode table rebuilt from primary data; every Appendix-C P0 hypothesis tested once, pre-registered, result in the registry; the provisional-ADV warning cleared from the validator |
| **H2 — Month ~5** (Track M live on paper) | Moderate model emits a complete, mandate-compliant portfolio at every historical rebalance (Stage-1 completeness gate); walk-forward validation passed incl. episode-DD check; paper trading running on the weekly runbook |
| **H3 — Month ~6** (three books on paper) | Aggressive sleeves validated & integrated; conservative projection papered; Stage-2 shadow ledger live at Rung −1; go/no-go pilot-capital decision taken with the gate evidence in hand |
| **H4 — Months 7–18** | Pilot capital → scale steps per §7 gates; fundamentals variants shipped with price-only counterparts; first live episode survived with DD machinery behaving as modeled |
| **H5 — Years 2–10** | The decade loop of §2.3: annual pre-registered re-estimation, tier promotions/demotions, capacity re-derivations as AUM grows, structural-change triggers firing as designed |

### 1.3 Critical path
```
Fixtures (A runsheet) → PIT price store → ADV table → {cost curves, universe bounds}
                     → episode table → {fast triggers, hedge effectiveness, gap floor}
                     → τ½ estimates → {band widths, embargo widths}
                     → factor premia (price-only, PIT) → moderate factor book
                     → Stage-3 construction → risk-system integration → walk-forward → paper
```
Everything upstream of the ADV table and the episode table blocks everything downstream — which
is why Phase R0/R1/R2 get the first three weeks and why the two standing validator warnings
(funding rate; provisional ADV) are the program's first two deletions.

---

## 2. The program arc, 2026 → 2036

### 2.1 Horizon map
| Window | Mode | Content |
|---|---|---|
| Sep–Nov 2026 | **Track R** | Shared research & estimation program (§3) — the "all research, regressions and more" layer |
| Nov 2026–Jan 2027 | **Track M** | Moderate model assembly, walk-forward, paper launch (§4) |
| Dec 2026–Feb 2027 | **Track A** | Aggressive sleeves + integration + paper (§5.1) |
| Jan–Mar 2027 | **Track C + Stage-2 shadow** | Conservative projection; Stage-2 ledger at Rung −1 (§5.2–5.3) |
| Mar 2027 → | **Capital** | Pilot → scale per §7 gates |
| Annually from 2027 | **Decade loop** | §2.3 |

### 2.2 What is deliberately NOT in the first six months
Fundamentals-based factor variants (price-only ships first — Contract prior #7; fundamentals are
month 5–6 stretch, H4 otherwise); the tactical short sleeve beyond trigger research (starts at
zero size by design); any Stage-2 authority above Rung −1; any live capital before the §7 gates;
options-based hedging beyond the rule-armed rare-buying channel; any re-opening of the ten
Batch-1 decisions.

### 2.3 The decade loop (2027–2036) — how the model stays alive while its edges decay
Run every 12 months (a pre-registered re-estimation window, never ad-hoc refits), plus
trigger-driven events:

| Cadence / trigger | Action | Registry hook |
|---|---|---|
| Annual (post-Budget, April) | Re-verify the statutory cost table (two STT hikes in 18 months already); recompute cost curves & hurdles | `costs.yaml` expiry field |
| Annual | McLean-Pontiff-style decay audit: every live signal's rolling OOS estimate vs its haircut assumption; demote/promote tiers per DESIGN §11 Phase 9 | per-signal `decay` fields |
| Annual | τ½ re-estimation with one more year of data; band widths and embargoes move mechanically | `ladder.yaml` |
| AUM ±50% in any book | Full capacity re-derivation (ADV, days-to-build, effective universes, SAST floor) | `costs.yaml` recalibration trigger |
| Index-effect re-estimate, every reconstitution cycle | The rising-decay haircut updated (India ≈ US-1990s today; passive AUM compounding) | `sleeves.yaml` special_situations |
| Structural watch list (checked quarterly) | T+0/instant settlement expansion → re-derive cash-vs-futures leverage comparison; further F&O curbs → hedge cost model; SEBI algo/AI perimeter → Stage-2 compliance; bond-index-inclusion flows → funding/rate regime; passive AUM share; retail F&O participation; INR regime change (sustained CA surplus would retire the REER tilt) | `risk.yaml` / `sleeves.yaml` changes_if fields |
| Every completed India credit down-leg (expect ~1–2 per decade) | JST pooling weights shift toward India-specific estimates; AUROC prior re-estimated | `ladder.yaml` L10 |
| Gold-regime legs (≥4 quarters reversal on any input) | Gold score weights re-balanced per `sleeves.yaml` gold rules | gold inputs |
| Model-version change (any LLM in Stage 2) | Track record → n=0 AND rung step-down (probation) | `sleeves.yaml` stage2 |
| 2030 checkpoint | Formal design review: which of the 2026 assumptions [A] never got data; demographic-arc positions updated (dividend window to ~2036–41); decide whether the 2050-horizon variants (fiscal-dominance expressions, reserve-order states) deserve promoted budgets | full registry review |

The premise of the decade loop is the Contract's governing principle: **every edge decays; the
system survives by re-measuring, not by believing.** Nothing in the loop refits thresholds to
backtest Sharpe — every annual re-estimation is itself pre-registered (window, metric, decision
rule) before it runs, and every change lands as a versioned registry diff through the validator.

---

## 3. TRACK R — the shared research & estimation program (months 0–3)

This is the layer the principal asked for explicitly: *all research, regressions and more, which
help all three models, step by step.* Every item below names its consumers (which books/systems
use it), its method (per DESIGN §11), its Appendix-C hypothesis IDs where it is a test rather
than a measurement, its owner (P = principal, C = Claude, J = joint) and effort (days).

**A measurement is not a hypothesis** — descriptive items (R1) need no pre-registration and are
never "significant" or not; they are inputs. Everything in R4–R5 that makes a predictive claim IS
pre-registered before it runs. This distinction keeps the trial ledger honest.

### R0 — Data foundation (weeks 1–3) — gate G-R0
| # | Step | Method / notes | Consumers | Owner | Effort |
|---|---|---|---|---|---|
| R0.1 | Execute Appendix-A P0 pull runsheet on the principal's machine (bhavcopy cash+F&O full history, index constituents & TRI, India VIX, NSDL FPI, RBI DBIE core set, CCIL, AMFI, FRED set). **Day-1 item #1: confirm CCIL registration is actually free** (sign-in gated; FBIL's free 7-day-lagged G-sec curve is the fallback). Bhavcopy ingestion must handle the **2024-07-08 UDiFF format boundary** (NSE Circular 62424) — two parser versions | bulk downloads + documented scrapes; every file checksummed, vintage-tagged, committed as fixture | everything | P (pulls) + C (scripts) | 4–6 d |
| R0.1b | **2026 base-year splice plan** — Appendix A's biggest live finding, flagged nowhere in the dossiers: India rebased nearly every macro series concurrently in 2026 (GDP/GFCF 2011-12→2022-23, Feb-2026; CPI 2012→2024/COICOP, Feb-2026; IIP →2022-23, May-2026; WPI →2022-23, Jun-2026). Every L6/L10–L12 input crossing these dates needs an explicit splice with the break dates as level discontinuities — never fit through (same discipline as the gold-duty breaks) | documented splice per series, in the fixture metadata | ladder, macro states | C | 1–2 d |
| R0.2b | **Universe PIT integrity**: Nifty Total Market and Microcap 250 indices launched only in 2023 — their pre-launch "history" is back-computed, not point-in-time-published. Pre-2023 rank-500–750 membership must be reconstructed from mcap ranks on the PIT panel and labeled as reconstruction (the aggressive book's own analogue of the restated-fundamentals problem, prior #7) | reconstruction + labeling | aggressive universe, tail sleeve | C | 1–2 d |
| R0.2 | PIT price store: corporate-action-adjusted daily panel, NIFTY-750 membership history (survivorship-free universe from constituent-change records) | Appendix B `pit/` modules; golden-file tests | everything | C | 4–5 d |
| R0.3 | Data-quality monitors: gap/stale detection, cross-source reconciliation (NSE vs BSE closes; TRI vs price+dividend recomputation) | automated checks in CI | ops | C | 1–2 d |
| R0.4 | Fixture governance live: manifest, refresh cadences per series (A §fixtures) | | ops | J | 1 d |
**G-R0 (numeric):** ≥99% trading-day coverage 1996→present for the price panel; constituent
history reconciles against ≥3 published reconstitution announcements; every P0 series present
with checksum; the no-look-ahead property test (B §test-strategy) passes on the PIT store.

### R1 — Descriptive foundations (weeks 3–5) — measurements, not hypotheses
| # | Step | Output → registry consequence | Consumers | Owner | Effort |
|---|---|---|---|---|---|
| R1.1 | **ADV by rank bucket** (90-day medians, quarterly re-ranked) | replaces `costs.yaml` provisional table → validator warning cleared; **recompute**: cost curves, days-to-build, effective universes, pipeline throughput, SAST floor — the §2.1 arithmetic of DESIGN re-run on real numbers | all books | C | 2 d |
| R1.2 | Volatility structure: σ_daily by bucket; idiosyncratic-vol share; **India Evans-Archer/Statman diversification curves** per bucket | `books.yaml` name-count floors re-derived (India curves, not US import) | all books | C | 2–3 d |
| R1.3 | **Downside beta** of mid/small buckets vs Nifty 50, episode-conditional | `risk.yaml` downside_beta_tilt [1.10,1.30] → measured value with CI | risk system | C | 1–2 d |
| R1.4 | Cross-sectional dispersion series + expanding percentile history | N* formula input (DESIGN §7.2) | Stage 3 | C | 1 d |
| R1.5 | Tracking-error measurement conventions; TE(W) series at W ∈ {30,60,90} | DD-violation ε computable (trial #14 sweep prepped) | DD monitor | C | 1 d |
| R1.6 | Benchmark integrity: Nifty 500 TRI / Nifty 50 reconstruction check | benchmarks trusted | all | C | 1 d |
| R1.7 | Promoter holding / free-float panel from shareholding patterns | float-scaled signals (L14), SAST floor precision | factor book, tail | C | 2 d |

### R2 — Episode & risk-system foundations (weeks 4–7)
| # | Step | Method | Hypothesis IDs | Registry consequence | Owner | Effort |
|---|---|---|---|---|---|---|
| R2.1 | **Episode table from primary data**: every Nifty fall >15% since 1996 — peak/trough dates, depth, duration, recovery, concurrent SMID depths; classify under the ε/K/W test; May-2026 recorded as non-qualifying INR crisis [I] | mechanical; no fitting | — | the binding-episode set every DD claim tests against | C | 2–3 d |
| R2.2 | **Fast-trigger lead-lag table**: India VIX level/term-structure, realized-vol ranks, CCIL funding spreads, FII-run lengths — actual lead/lag in days per episode | frequency counting, pre-registered trigger forms; NO Markov fitting (<10 transitions) | C-series: fast-trigger IDs | L2 evidence Tier B→A path; R4 entry rules parameterized | C | 3–4 d |
| R2.3 | **Gap & lock risk**: overnight-gap distribution by bucket; circuit-day frequency; **band-lock frequency statistic** built per D12 spec | mechanical from bhavcopy + band master | band-lock validity H | `risk.yaml` gap_floor [0.10,0.15] → measured; hedge_effectiveness floors → measured (the R4 check's he≥0.33 sensitivity resolved) | C | 3 d |
| R2.4 | **Whipsaw counting**: candidate trend/vol-target/hysteresis re-entry rules × episode set — true catches vs false fires, costed | frequency counting, never Sharpe-tuned | re-entry family Hs | §5.7 re-entry rules per sleeve selected | C | 2–3 d |
| R2.5 | **Vol-targeting India replication**: vol → forward return/vol relation for Nifty 50/500/SMID | Harvey-et-al replication, purged | H: vol-target | licenses the leverage function's vol scaling [X]→[I] | C | 2 d |
| R2.6 | Block-bootstrap DD machinery + validation against episode table | Politis-Romano, block length 2–4×τ½ | — | the 30–35% ceiling checked against 95th/99th bootstrap percentiles forever after | C | 2 d |
| R2.7 | India VRP measurement: India-VIX vs realized, pre/post-2019 retail boom split | descriptive | — | option-budget pricing (`risk.yaml` option_premium_budget) | C | 1–2 d |

### R3 — Cost & capacity calibration (weeks 5–8)
| # | Step | Method | Registry consequence | Owner | Effort |
|---|---|---|---|---|---|
| R3.1 | Impact coefficient **Y** first calibration | bhavcopy flow proxies (delivery-% signed-volume regressions); honest CI; refined later with live executions | `costs.yaml` Y [0.5,1.0] narrowed | C | 3 d |
| R3.2 | **Futures roll basis vs MIBOR** history by expiry | mechanical from F&O bhavcopy | leverage-instrument comparison quantified (the ~4× statutory gap plus basis reality); funding hurdle calibration | C | 2 d |
| R3.3 | Statutory engine coded + tested against `costs.yaml` verified table | Appendix B `costs/` | cost floors live | C | 1 d |
| R3.4 | Turnover cost curves per book × rank-bucket mix; **hurdle table finalized** (the 3.0–6.0pp band → a number per book) | DESIGN §9.3 on real ADV | `books.yaml` turnover design points confirmed or moved | C | 1–2 d |
| R3.5 | Broker reality: DMA/algo access, actual brokerage, **actual funding rate** (the standing validator warning), margin schedule, SLB access check | commercial diligence | `risk.yaml` funding_rate set → leverage feature go/no-go arithmetic | **P** | 3–5 d elapsed |

### R4 — The regression program: cycle ladder & factor premia (weeks 6–12)
Every row pre-registered (Appendix C) before running; embargo = f(τ½); Stambaugh correction on
persistent predictors; OOS vs historical mean; all sweeps into the trial ledger.

| # | Estimation / test | Method core | Consumers | Registry consequence | Effort |
|---|---|---|---|---|---|
| R4.1 | **Hamilton filters** on credit/GDP (own construction), CD ratio, HPI, IIP/GFCF at both bands; h selected by purged CV against pooled JST crisis labels | Hamilton 2018; h grids from trial ledger #4 | L10–L12 | filtered state series live | 3 d |
| R4.2 | **τ½ for every ladder entry** (L1–L15): bias-corrected AR(1) on overlapping windows, CIs, rolling-stability across 1991/2003/2008/2016/2020 | Kendall/Marriott-Pope; Andrews near unit root | ALL — the ladder ordering itself | `ladder.yaml` tau_half priors → estimates; **band widths h(τ½) and τ_ref calibrated** (trial #5); embargo widths set | 4 d |
| R4.3 | **Credit block predictive content**: India AUROC of gap/CD-ratio/issuance-quality for episodes; JST partial pooling (empirical-Bayes weights) | logit/local projections, pooled; Stambaugh-corrected | risk system (all books) | the 0.65–0.75 AUROC prior → estimate; L10 weight inside block earned | 4–5 d |
| R4.4 | **Global-cycle factor**: mini dynamic-factor on VIX/dollar/US-rates/FPI/INR/India-VIX; India transfer coefficient | Miranda-Agrippino-Rey reduced form | risk system | L9 loading estimated | 3 d |
| R4.5 | Monetary stance lag calibration; Kilian-decomposed oil state construction | published-index ingestion + India CAD pass-through check | L6, L9 | lagged stance rule parameterized | 2 d |
| R4.6 | **Momentum composite on PIT price-only data**: full-history premium; **post-2015 sub-sample decay test** (the India McLean-Pontiff split — falsifier for the 25–35% haircut); liquid/illiquid tercile split (Chui replication); crash-guard vol-scaling replication | purged CV; deflated Sharpe | aggressive + moderate modifier | `sleeves.yaml` momentum haircut confirmed or raised toward 58%; crash-guard parameters | 4 d |
| R4.7 | **52-week-high first India estimate**; TSMOM India equity & gold cost-inclusive estimates | same protocol | momentum sleeve, gold tilt, regime | new Tier-B India rows or rejection | 2–3 d |
| R4.8 | **Value price-only composite** (div yield + NSI + sales/price): premium, half-life; **value-spread conditioner test** (Stambaugh-corrected: does India's own spread percentile predict the factor's forward return?) | pre-registered; the conditioner is the test, the premium is measurement | factor book (all books) | conditioner earns/loses its weight rule | 3–4 d |
| R4.9 | **Realized-vol rank (low-vol)**: unified-universe test designed to resolve the split India literature (the two conflicting studies used different universes) | one pre-registered spec | factor book | low-vol weight range stands or shrinks | 2–3 d |
| R4.10 | **Quality-controlled size — THE test** (highest-value single test in the program: upgrades or kills a whole sleeve currently Tier C at 0–15% satellite) | pre-registered, purged, PIT | factor book | sleeve promoted to core range / killed | 3 d |
| R4.11 | **Flows-returns causality with structural break**: has the FII-flow→return relation weakened as DII/SIP flow grew? plus FII-positioning-percentile reduce-only validation | rolling Granger/Chow, pre-registered | L14; excluded-signal hygiene | confirms exclusion of flow momentum; L14 stays/goes | 2 d |
| R4.12 | **Election & budget event studies** (pre-registered windows, all 9 elections, ~30 budgets; mandate-clarity classifier specified BEFORE looking, ≥2 elections held out) | event study, tiny-n honesty | L5 | vol-scheduling scalars set | 2 d |
| R4.13 | **Issuance/sentiment cycle**: issuance-share + first-day-pop percentile construction; validation against 2008/2021/2023-24 froth episodes | percentile ranks; pre-registered | L7; special-sits sizing | L7 state live | 2 d |
| R4.14 | **Gold function inputs**: real-rate link pre/post-2022 Chow test; INR gold decomposition with duty-break handling (2013, Jul-2024); crisis-kicker measured on episode set + cross-country analogue pool (≥10 episodes) | break test (not regime fit); episode measurement | gold sleeve (all books) | `sleeves.yaml` gold score weights confirmed/re-balanced | 3 d |
| R4.15 | Household-debt change & long-wave proxies wired (debt/GDP slope, real-rate persistence, RBI gold buying, COFER) — reduce-only overlays, no fitting | series construction only | L13, L15 | Tier-C overlay live | 1–2 d |

### R5 — Special-situations registries (weeks 8–12, parallel; consumed by Track A but researched once)
| # | Registry / test | Effort |
|---|---|---|
| R5.1 | **Demerger registry** (2000–2025, target 20–40 events) + pre-registered event study → sleeve rule earns Tier B or stays C | 3 d |
| R5.2 | **Deal-flow census**: buybacks/open offers/delistings — frequency, size, realized spreads → the ≤10% satellite cap re-derived from actual capacity (currently the least-defended number) | 2–3 d |
| R5.3 | **Pledge-invocation event study** (Reg-31 filings; ~10–15 cascade episodes) → quality junk-term 50% discount resolved | 2–3 d |
| R5.4 | **Index-reconstitution effect, era-segmented** (pre-2015 vs post-2020) → the rising-decay haircut quantified | 2 d |
| R5.5 | **Lock-in expiry India test** (RHP dates × bhavcopy; SEBI gradual-exit context) → keep/drop the no-adds window | 1–2 d |
| R5.6 | **Bulk/block/PIT rank-segmented test** — one pre-registered spec, ranks 500–750 vs 1–500 | 2 d |

### R6 — Protocol infrastructure (continuous through Track R)
Trial ledger operational (file-based, PR-updated); pre-registration workflow (a hypothesis is a
PR into `research/register/preregistrations/H##.md` BEFORE its test code runs — reviewer: the
other team member); purged-CV + deflated-Sharpe + MinTRL library (Appendix B `backtest/`);
verification-queue burn-down (DESIGN §15 items closed at ~3–5/week alongside other work).

### R7 — Synthesis checkpoint (week 12–13) — gate G-R
Registry mass-update from R1–R5 (one large, validator-checked PR); honest bands re-derived;
**decision: which sleeves enter Track M assembly enabled** — anything failing its gate enters the
registry as rejected (permanently, per the stop rule) or Tier-C-frozen.
**G-R (numeric):** provisional-ADV warning cleared; every ladder entry has a τ½ with CI; ≥90% of
Appendix-C P0 hypotheses executed with results filed; episode table complete & classified;
funding rate on file; validator loads clean with zero warnings.

---

## 4. TRACK M — the moderate model (months ~3–5)

The first complete model. Universe ranks 1–500 (full-conviction 1–150), turnover design point
100–160%, leverage 1.0–1.05x, factor book engine.

| # | Step | Content | Gate criteria | Effort |
|---|---|---|---|---|
| M1 | Factor book assembly | value/quality/low-vol (+size if R4.10 passed) composites wired with R4 weights & conditioners; price-only throughout; quality junk terms at their R5.3-resolved weight | component sanity: exposures, turnover per sleeve within budget | 3–4 d |
| M2 | Stage-3 construction | characteristic-portfolio optimizer + Ledoit-Wolf risk budgeting (shrinkage intensity calibrated on Indian panel); N* formula live; per-signal bands; three-way sizing minimum + cushion | Transfer-coefficient report vs unconstrained; caps bind correctly | 4–5 d |
| M3 | Risk-system integration | regime score (block budgets, Tier-C clamps), bucket state machine, leverage function (with real funding rate + hurdle), hedge stack (de-gross priority list generator), DD monitor (ε, K, W live) | §5.2 identity satisfied on every qualifying episode in replay | 4–5 d |
| M4 | **Walk-forward validation** | full DESIGN §11 protocol: purged folds, OOS vs mean, deflated Sharpe against the LIVE trial ledger, block-bootstrap DD tail vs ceiling, Stage-1 completeness at every rebalance date | **G-M1:** mandate-compliant portfolio at 100% of rebalance dates; bootstrap 95th-pct DD ≤ ceiling; net-of-cost factor book clears its hurdle after haircuts; DD-violation test never fires on non-qualifying episodes | 5–6 d |
| M5 | **Paper launch** | weekly runbook live (§8); staggered signal/execution tranches; daily monitors | 4 consecutive clean weekly cycles; paper fills within modeled cost ±30% | 3 d + elapsed |
| M6 | Report pack | monthly tear sheet: exposures, regime state, DD position, cost realization, ledger status | first monthly report produced | 1–2 d |
| M7 | *Stretch:* fundamentals variants | lag-stamped fundamentals + mandatory price-only counterpart; measured restatement bias vs the 150–450bps prior | fundamental alpha reported ONLY beside price-only twin | 4–6 d |

---

## 5. TRACKS A, C, and Stage-2 shadow (months ~4–6)

### 5.1 Track A — aggressive
A1 fast momentum sleeve (liquid ranks; crash guard; ≤200% own turnover) — 3 d ·
A2 tail/neglect sleeve (band-lock filter from R2.3; 1–2% tickets; build-time ≤ τ½ rule) — 3 d ·
A3 special-sits satellite (rules frozen from R5 results; cap from R5.2; L7 froth sizing) — 3 d ·
A4 tactical-short triggers (research only; sleeve remains at zero until a trigger passes gates) — 2 d ·
A5 integration + walk-forward + paper (**G-A**, criteria as G-M1 plus: tail-sleeve exit stress
test — liquidation cost under episode-conditional ADV halving stays within DD budget) — 5 d.

### 5.2 Track C — conservative
The moderate book re-parameterized: entries 2.5–4% below rank ~80, N 50–80→150–250, turnover
≤40–75%, leverage 1.0, SAST floor enforcement live, pipeline-throughput scheduler (3–4 full-size
builds concurrent). Mostly configuration + capacity code, not new research — 4–6 d + paper.

### 5.3 Stage-2 shadow (from month ~5)
Ledger + three channels live at **Rung −1** (zero authority); paired Stage-1-only vs Stage-1+2
harness armed with pre-registered gate; weekly overlay session (default cadence, batch-2 Q6);
Brier scoring from thesis #1; SEBI algo/AI-perimeter question to compliance counsel **before**
any authority above Rung −1 is ever contemplated.

---

## 6. Master gate table
| Gate | When | Numeric criteria (all must hold) |
|---|---|---|
| G-R0 | wk 3 | fixture coverage ≥99%; PIT no-look-ahead test green; P0 series complete |
| G-R | wk 13 | zero validator warnings; τ½+CI per ladder entry; ≥90% P0 hypotheses run; episode table classified; funding rate on file |
| G-M1 | wk 18–20 | Stage-1 completeness 100%; bootstrap 95th-pct DD ≤ ceiling; factor book clears hurdle post-haircut; ε/K test fires on qualifying episodes only |
| G-M2 (paper) | wk 22+ | 4 clean weekly cycles; cost realization within ±30% of model |
| G-A | wk 24 | G-M1 criteria on the aggressive book + tail liquidation stress within budget |
| G-C | wk 24–26 | capacity scheduler respects SAST/ADV bounds mechanically; paper live |
| G-S2 | ongoing | shadow only; promotion gate per DESIGN §8.2–8.3 (n≥20, BSS>0, paired test ≥2 windows) |
| G-CAP1 (pilot) | ≥ month 6 | §7 criteria |

---

## 7. Capital & scale-up

**The honest statistics first [T]:** at a true annual Sharpe ≈1.0, distinguishing the strategy
from zero at 95% one-sided needs ≈ (1.645/1.0)² ≈ 2.7 years of returns; from a 0.5-Sharpe
benchmark, ≈ 10+ years. **Therefore capital gates cannot wait for Sharpe significance** — they
gate on what IS measurable early, while MinTRL-based confidence accrues in the background:
1. **Implementation fidelity** — live/paper tracking difference within modeled cost bands for N
   consecutive cycles;
2. **Risk-system behaviour** — regime states, leverage, hedge actions all match the rules with
   zero manual overrides; any qualifying drawdown episode handled within the ε/K envelope;
3. **Cost realization** — realized impact within the calibrated band (this also refines Y);
4. **Zero mandate-cap breaches** and validator-clean registry at every rebalance.

Proposed ladder (batch-2 decision Q1, defaults):
| Step | Trigger | Moderate | Aggressive | Conservative |
|---|---|---|---|---|
| Paper | G-M2 / G-A / G-C | — | — | — |
| Pilot | G-CAP1: 3 months clean paper + criteria 1–4 | ₹50–100cr (strategy logic below design floor deliberately — capacity-easy) | ₹25–50cr | logic runs inside moderate pilot |
| Scale 1 | +2 quarters clean + first MinTRL milestone | toward ₹250–500cr | toward ₹100cr | pilot ₹250–500cr |
| Design range | episode survived live OR 4 clean quarters | ₹1,000cr+ | ₹100–250cr | ₹10,000cr path per capacity re-derivations |
Every scale step re-runs the capacity arithmetic (AUM-triggered) and re-freezes the cost curves.
De-scaling is symmetric and automatic: a mandate breach, a DD-envelope violation, or a manual
override of the risk system freezes scaling and triggers review.

---

## 8. Operations runbooks

### 8.1 Daily (~15 min, automated + human glance)
Post-close (~18:30 IST): pull bhavcopy/VIX/FPI deltas → data-quality monitors → recompute: DD
position vs ε/K envelope, fast-trigger states (vol rank, VIX term structure, funding/FII runs),
band-lock & ASM/GSM deltas on held names, pledge-invocation filings on held names, F&O ban list,
margin cushion vs pre-buffer. Any RED item pages the on-duty person (batch-2 Q7).

### 8.2 Weekly rebalance cycle (per-sleeve cadence; staggered)
Fri close: signal measurement (tranche 1 of the stagger) → weekend: candidate trade list, Stage-3
run, risk checks, **validator run on any config diff**, staged-entry queue update → Mon–Thu:
execution tranches at participation caps; daily fill-vs-model reconciliation → Fri: cycle report.
Stage-2 session (shadow): theses logged/scored before the weekend run, never inside it.

### 8.3 Monthly / quarterly / annual
Monthly: ledger Brier scoring + calibration curves; factor-conditioner refresh (value spread,
quality valuation, dispersion percentile); AUM/crowding monitors (momentum, low-vol, min-vol
flows); SIP/FPI structural series; tear sheet. Quarterly: tier review board (promotions/
demotions per Phase-9 rules); capacity check; F&O eligibility & MWPL refresh; trial-ledger
audit (undercounting check); fixture refresh per cadence table. Annual: the §2.3 decade-loop
items.

### 8.4 Incident procedures
- **Fast-trigger fire (→R4):** execute the precomputed de-gross priority list (liquid first);
  margin to 1.0x; rule-armed option buying per budget; no discretion required or permitted —
  discretion is exactly what the evidence says fails under stress [X].
- **Margin pre-buffer breach:** automatic de-lever to 1.0x same session; postmortem before
  re-lever (leverage is permission, not default).
- **Data failure:** risk system runs on last-good with staleness flag; staleness >2 sessions →
  no new entries, hedge state frozen at last valid, manual verification required.
- **Validator failure on any change:** the change does not exist. No exceptions — this rule is
  what made the registry catch the R4 breach and the budget overrun.
- **Key-person unavailability:** every runbook step executable by either team member; weekly
  cycle can skip one week safely by design (bands widen, nothing breaks).

---

## 9. Engineering & data standards
Repo layout, module catalog (~35 modules), dependency DAG, effort roll-up: **Appendix B**.
Data catalog, pull runsheet, fixture governance, PIT/restatement handling per series, gap list:
**Appendix A**. Non-negotiables (from Contract + audits): every module runs on committed fixtures
with zero live data; the no-look-ahead property test is CI-blocking; config values are read only
through the registry loader (no literals in code — the red-team's hardcoded-0.38 lesson,
generalized); parquet + DuckDB storage (batch-2 Q5 default); Python 3.12; every analytical
output stamped with fixture vintage + config version + git SHA.

## 10. Research-protocol operations
A hypothesis lives as `research/register/preregistrations/H##.md` (Appendix-C row expanded),
merged BEFORE its test code runs; results append to the same file; rejected = permanent (a new
mechanism argument = a new H##). The trial ledger is updated in the same PR as any sweep code.
The deflated-Sharpe N is computed from the ledger programmatically — never typed by hand. The
verification queue (DESIGN §15) burns down in parallel; item status lives in
`research/register/verification-log.md`; **nothing [VERIFY]-tagged crosses Tier C** (enforced
convention + spot-checked at quarterly audit).

## 11. Governance & change control
| Class | What | Process |
|---|---|---|
| 1 | Frozen mandate (CONTRACT §3, caps, architecture) | principal sign-off + CONTRACT edit + version bump; validator constants updated in the same PR |
| 2 | Registry parameters (config/*.yaml) | PR + provenance fields + validator green + trial-ledger entry if swept; either member proposes, the other reviews |
| 3 | Code | tests + CI green; golden files updated deliberately, never silently |
| 4 | Stage-2 ledger | append-only; proposer ≠ red-teamer; rung changes only via the pre-registered gate; kill-switch at 3 hard-cap flags/window |
Decisions log: `research/OPEN_QUESTIONS.md` (Batch 1 answered; Batch 2 in §14). Everything is in
git; there is no out-of-band state.

## 12. Effort & feasibility (2 people, 3–6 months)
Two independent estimates, reconciled honestly:
- **Top-down (this plan's phase view):** Track R ≈ 55–70 working days of build/analysis +
  8–12 principal-days; Track M ≈ 20–26 d; Track A ≈ 16 d; Track C ≈ 5 d; Stage-2 shadow ≈ 5 d;
  ops setup ≈ 5 d → ≈105–130 days.
- **Bottom-up (Appendix B's module roll-up):** 45 modules = 5 S + 24 M + 16 L ≈ **170 person-days**,
  with Phase-1-equivalent work alone ≈69 person-days — the strictest checkpoint by design.
The gap is real and resolves three ways: (i) the cut list below removes ~25–35 bottom-up days
(fundamentals M7, report polish, stretch modules); (ii) code-heavy S/M modules compress under
Claude-driven generation (the L modules — factor book, ladder estimation, walk-forward harness —
are the true bottleneck and do not compress much); (iii) two workstreams stay in flight
throughout. **Conclusion: 6 months is feasible with the cut list armed and no scope additions;
4 months is not realistic on the bottom-up numbers — plan to the 6-month calendar in §15.**
Cut list if behind (in order): M7 fundamentals → Track C paper slips to month 7 →
tactical-short research → election classifier → R5.6 bulk/block test. **Never cut:** anything in
R0–R2 (foundations), the validation gates, the trial ledger, or the price-only-first rule.

## 13. Risk overview
Top five (full register: **Appendix D**): (1) funding rate comes in retail-priced → leverage
feature near-worthless — mitigation: it's a config input, the design degrades gracefully to
1.0x; (2) measured hedge effectiveness < 0.33 breaks the R4 ceiling check — mitigation: R2.3
measures it early; option budget is the buy-back lever; (3) NSE/BSE access friction (URL scheme
churn, rate limits) stalls R0 — mitigation: archives + the A-catalog documents alternates;
(4) two-person bandwidth + scope creep — mitigation: §12 cut list, gates refuse entry to new
scope; (5) pre-registration discipline erosion under time pressure — mitigation: the ledger is
PR-enforced and quarterly-audited; a result without a pre-registration file is void.

## 14. Decision queue — Batch 2 (defaults assumed unless overridden; same convention as Batch 1)
| # | Question | Options | **Default** |
|---|---|---|---|
| 1 | Pilot sizes & order | as §7 table / smaller / straight to design floors | **§7 table** (moderate logic at ₹50–100cr first) |
| 2 | Funding rate + broker terms | (input, not options) | **required at R3.5** — the one number only you can supply |
| 3 | Rebalance anchor | Fri-measure + Mon–Thu tranches / other weekday | **Fri + staggered tranches** (timing-luck evidence) |
| 4 | Execution infra | DMA + participation-capped algos / manual pilot | **DMA+algos; manual acceptable during paper/pilot** |
| 5 | Stack | Python 3.12 + parquet/DuckDB + private GitHub / other | **default stack** |
| 6 | Stage-2 session cadence | weekly + event-driven / daily | **weekly + event-driven** |
| 7 | R4 out-of-hours execution authority | either member executes the precomputed list / principal only | **either member** (it's rule execution, not discretion) |
| 8 | Entity/regulatory scope | prop book, out of scope, counsel checks algo perimeter pre-Stage-2-live / fuller review now | **prop + targeted counsel check** |
| 9 | TRI benchmark source | NSE indices TRI fixtures / vendor | **NSE TRI, fixture-committed, recomputation-checked** |
| 10 | Gold implementation start | ETF-only until roll costs measured / ETF+futures day one | **ETF-only start**; futures for the tactical band after R-phase measures MCX roll |

## 15. Milestone calendar (start 2026-09-01)
| Date | Milestone |
|---|---|
| Sep 19, 2026 | **G-R0** — fixtures + PIT store live |
| Oct 10 | R1–R2 complete: real ADV (validator warning cleared), episode table, trigger lead-lags |
| Oct 31 | R3 complete: cost curves live; funding rate on file |
| Nov 28 | **G-R** — regression program done; registry mass-update; sleeve go/no-go |
| Dec 19 | M1–M3 assembled |
| Jan 15, 2027 | **G-M1** — moderate walk-forward passed |
| Jan 29 | **G-M2** — moderate paper live |
| Feb 26 | **G-A** — aggressive paper live; Stage-2 shadow running |
| Mar 12 | **G-C** — conservative paper live |
| Mar 31 | **G-CAP1 review** — pilot-capital decision with three books on paper |
| Apr 2027 | First annual statutory re-verification (Budget) — decade loop begins |

## 16. Appendix index
- **A** — `docs/masterplan/A-data-catalog.md`: every series, exact access path, PIT caveats,
  fixture spec, P0 runsheet, gap list.
- **B** — `docs/masterplan/B-module-specs.md`: repo layout, module catalog with tests & effort,
  dependency DAG, CI/test strategy.
- **C** — `docs/masterplan/C-hypothesis-register.md`: every pre-registered hypothesis with
  minimum economic effects and registry consequences.
- **D** — `docs/masterplan/D-risk-register.md`: full program risk register.

---
*Master plan v1.0. The design is DESIGN.md; the mandate is CONTRACT.md; the decisions are
OPEN_QUESTIONS.md. Next action: Batch-2 defaults confirmation + R0.1 (the Appendix-A runsheet).*
