# Pipeline v2 — the end-to-end workflow (PROPOSED)

**Status: PROPOSED, pending principal sign-off on §6 open questions. Pipeline v1 (DESIGN.md §12
build sequence + the v1 stage description) remains authoritative until the migration decisions in
§6 Q7 are made. Nothing in this document changes any FROZEN constraint.**

Provenance: produced 2026-09-01 by a 12-agent research workflow (run wf_bc729492-880, ~1.08M
tokens): 5 parallel research sweeps (top GitHub OSS quant frameworks; systematic-firm process
models; canonical books Grinold-Kahn / Lopez de Prado / Carver / Narang / Ilmanen / QEPM;
2026-2040 AI-age shifts; India free-data landscape) -> 3 independent architecture proposals
(anti-overfit lens, AI-adaptivity lens, operations lens) -> 3 adversarial judges (contract
enforcer, practitioner, 2035-retrospective) -> 1 synthesis. The operations-first proposal won
unanimously (88/89/89 vs 85/82/83 anti-overfit, 80/79/80 ai-adaptive); the synthesis grafts the
judges' must-keep ideas onto it. Full raw materials: research/pipeline-v2/ (sweep digest, judge
verdicts, per-proposal key changes).

Design-research note: this document contains NO new return claims and registers NO trials; it is
architecture. Every borrowed idea carries its source and a survival note (§4); the rejected list
(§5) is part of the record.

---

# Cycle-Stack Pipeline v2 — Final Synthesis
**Desk:** principal + Claude | NIFTY 750 equities + gold + debt | 3 books (Aggressive ₹100–250cr / Moderate ₹1,000–2,500cr / Conservative ₹10,000–25,000cr) | free data only | horizon 2026–2040.

All FROZEN constraints are respected verbatim: Stage 1 emits a complete portfolio with no AI/human input; Stage 2 advisory, reduce-only, switchable off (off = multiplier pinned to 1); Stage 3 touches the equity cross-section only; asset mix is policy, never optimized; binding drawdown governor; free data; the 3 books; Hamilton-never-HP, purged/embargoed CV, deflated Sharpe with trial counts, pre-registration, no fitted regime-switching under 10 observed transitions; grids and ranks only; team stays principal + Claude; every published edge decays.

---

## 0. Verdict and explicit conflict resolutions

**Base = the operations proposal** (unanimous winner, 88/89/89): the only design that prices the desk's true binding resources — principal attention and the drawdown governor's operational reality — and the only one with a declared cut list and a graceful-degradation core. **Grafted onto it, per the judges' must-keeps:** the **Challenger Protocol** (anti-overfit) as the single uniform adaptivity-admission law; the **LLM hypothesis provenance flag** (ai-adaptive); the **fast/slow split** (ai-adaptive) as the standing design principle — fast layers (capture, monitoring, hypothesis generation, execution, decay measurement) adapt daily-to-monthly by rule; slow layers (block budgets, kill rules, governance, capital preservation) change only on scheduled dates, from strength, on grids.

Conflicts resolved, with sides taken:

1. **Adaptivity admission — scattered per-loop guardrails vs one protocol.** Sided with anti-overfit (all three judges): every adaptive mechanism in v2 (rotation, CUSUM throttles, crowding multipliers, meta-label sizing, influence grids, cap reviews) routes state changes through the Challenger Protocol. Heterogeneous bespoke promotion rules are the 14-year drift surface.
2. **Impact-refit cadence — monthly (anti-overfit, ai-adaptive) vs quarterly (operations).** Sided with operations and judge 2: own-fill samples are too small for monthly fits. Judge 3's microstructure-break concern is answered with an asymmetric event path: the execution kill-switch may **tighten** participation caps immediately; **loosening happens only at the scheduled quarterly refit**.
3. **skfolio rails and stacking inside `construct/` (ai-adaptive).** Rejected, siding with judge 1 (stacking is signal combination, i.e. return-engine estimation — a Stage-3 scope violation) and judges 2–3 (14-year dependency risk). Patterns, not dependencies. Signal combination lives in `sleeves/` behind the funnel, with handcrafted rule-based weights as the permanent null.
4. **PolicyTargets drawn as an output of construct (ai-adaptive diagram).** Rejected as drawn (judge 1): PolicyTargets originate **only** in `policy/`; `construct/` emits PortfolioTargets only. The contract enforcer reads the diagram, so the diagram is now correct.
5. **The Ilmanen-to-Kelly channel (flagged by all three judges as a judgment leak into Stage-1 sizing).** Specified by rule: the quarterly Ilmanen dashboard maps to **Kelly-numerator caps via a pre-registered, reduce-only grid function, applied only on the quarterly review date**. Anything discretionary flows solely into the humans' asset-mix policy review memo — policy is already the humans' layer, and it is never optimized. Stage 1 stays rules+data only.
6. **VineCopula synthetic stress paths as the governor's test suite (operations).** Kept only as an engineering test that can **fail** code (verify the governor fires, find bugs), self-built via block bootstrap and historical replay; **synthetic paths are inadmissible as evidence** for calibration, promotion, or safety claims (judge 1's fence).
7. **Ranges vs grids.** "6–12 month" probations, the ±20 forecast cap, and the archive cap are restated as pre-registered grids (judge 1): probation length per decay class from a grid in trading days {126, 189, 252}; forecast cap chosen once from {15, 20, 25} via CPCV then frozen as the null; archive capacity as a count K on an annual-review grid with rank-based eviction (lowest pre-registered resurrection-priority score evicted first, logged).
8. **Scope-cap ossification (judge 3 on operations).** Caps stay, but the caps themselves are annually Challenger-reviewable — amendable only at the annual review, as pre-registered changes, never mid-year and never mid-drawdown.
9. **"Green = skip" trained inattention (judge 3).** Three countermeasures: the weekly 2-hour block includes reading the week's pages regardless of color; a quarterly alert-path drill injects a synthetic amber to test push delivery and the response menu (logged, no meeting); a dead-man switch — a RED page unacknowledged for T hours (T from a pre-registered grid) auto-de-risks one bucket rung.
10. **The tight 18:30→20:30 daily window (judge 2).** Degraded mode is wired into the schedule: if EOD capture or adapter validation misses the cutoff, the data kill-switch fires automatically — Stage 1 runs on the last-good snapshot AND de-risks one rung; the run is flagged on the daily page. Never trade unverified data.
11. **The principal's TOPS score "has no consequence" (judge 2).** Consequence defined: the influence grid applies symmetrically per contributor category — a falling believability score (Claude's or the principal's) steps that contributor's overlay influence back down the published grid toward zero. The principal's **veto survives any score** — veto is risk-reduction governance, not alpha.
12. **Rhetorical overreach (judges on anti-overfit and ai-adaptive).** Untestable claims ("2022 proves the frozen parts right", "every credible firm converged") are struck from normative content. The 2022 stock-bond break is *consistent with* fixed policy scaffolding; nothing in this document treats a single episode as proof.
13. **Governance scope numbers (judge 1 on operations' raw numbers).** The module ceiling, survivor cap, DSL type caps, and time budgets are declared **scope caps, not fitted parameters** — they bound what gets built, never what gets estimated; each sits on an annual-review grid and is Challenger-amendable.

---

## 1. Final architecture diagram

```
                 +---------------------------------------------------------+
                 | govern/  charters | CHALLENGER REGISTRY: every adaptive |
                 |  rule in exactly one of {shadow|challenger|online};     |
                 |  frozen v1 params = permanent null; promotion/demotion  |
                 |  by pre-registered criteria, scheduled dates only |     |
                 |  anti-capitulation lock | annual report + AGS review |  |
                 |  scope caps (annually Challenger-reviewable)            |
                 +----------------------------^----------------------------+
                                              | states, sign-offs
 +---------------------------------- data/ --------------------------------+
 | capture/ WORM daemon -> adapters/ (TET, vintage-stamped in transform)   |
 |  -> store/ bitemporal parquet (event_time, knowledge_time)              |
 | entity/ ISIN master + PIT NIFTY-750 | breaks/ regulatory-break registry |
 |  ("insufficient post-break data" is a valid answer)                     |
 +--------------------+---------------------------------+------------------+
              as-of API ONLY                     as-of API ONLY
 +--------------------v---------------+  +--------------v------------------+
 | harness/ THE ONE EVIDENCE MACHINE  |<-| research/ funnel:               |
 |  runner: YAML = experiment; same   |  |  T0 tearsheet -> T1 sweep ->    |
 |  code path = backtest AND live     |  |  T2 bias-CI+CPCV/PBO replay ->  |
 |  recorder = TRIAL LEDGER (counts   |  |  T3 paper probation (grid by    |
 |   BEFORE results; DSR by query)    |  |  decay class) -> live, reduced  |
 |  gates: bias-CI | CPCV/PBO/BCa |   |  | agentloop: Claude proposes,     |
 |   capacity | cost-in-SR | death    |  |  trial-budget metered; <=3      |
 |   cert | LLM-provenance flag       |  |  survivors/wk to principal      |
 |  rotation ledger (who-online-when) |  | archive/ capped, resurrection   |
 +--------------------+---------------+  +---------------------------------+
   promotes ONLY via Challenger states        ^ disagreements, ideas
 +--------------------v---- STAGE 1 (autonomous, complete portfolio) ------+
 | ladder/ 16 vars, FIXED budgets -> R = median of pre-reg grid ensemble   |
 |   + crowding/ (daily, reduce-only, outside budgets)                     |
 |   + shadow GMM (log-only, non-trading)             | R bucket           |
 | policy/ trigger/action file (<=5 trigger/<=6 action types): asset mix   |
 |   within caps, per-book vol targets -> leverage (<=1.5x), hedge grid    |
 |   0-150% (post-STT costs + SEBI FutEq hard ceiling; crisis-insurance    |
 |   scored), tail throttle                            [PolicyTarget]      |
 | sleeves/ 5 factors -> sector-z -> forecast currency (E|f|=10, grid cap) |
 |   -> Grinold alpha (grid IC, uniqueness-wtd) -> class-conditional decay |
 |   haircut -> cost-netted alpha                      [Signal]            |
 | construct/ ONE optimizer per book: net sleeves (paper books kept) ->    |
 |   xrisk factor caps + ex-ante TE vs Nifty 50 -> sizing = min(frozen     |
 |   cap, haircut-Kelly, buildable) x DD cushion       [PortfolioTarget]   |
 +--------------------+-----------------------------------------------------+
 +--------------------v----------+   +-------------------------------------+
 | overlay/ Stage 2 (advisory,   |   | sentinel/ (subscriber, never inline)|
 |  reduce-only, switchable)     |   |  dailypage: ONE page, RAG header;   |
 |  tops/ scored paper trades    |   |   RED unack'd T hrs -> auto de-risk |
 |  (Claude AND principal, both  |   |  cusum/ + certs/ kill tiers by rule |
 |  believability-scored)        |   |  attribution/ TC-by-constraint, IC, |
 |  metalabel mult in [0,1];     |   |   netting bps, walk-forward tracks  |
 |  off = pinned to 1; veto      |   |  governor/ BINDING drawdown (frozen)|
 +--------------------+----------+   +----^--------------^-----------------+
 +--------------------v----------+        | fills          | states, PnL
 | exec/ scheduler (ADV caps,    |--------+                |
 |  futures-first, ban/rebal     |-------------------------+
 |  aware) -> MARKET; fills/     |
 |  ledger -> quarterly impact   |
 |  refit shrunk to sqrt prior   |
 |  (tighten fast; loosen only   |
 |  on schedule)                 |
 +-------------------------------+
 KILL-SWITCHES: governor | data-kill (last-good + de-risk one rung) | cert
 tiers | overlay pin=1 | execution halt | anti-capitulation lock | harness
 integrity (any read outside as-of API = inadmissible)
 CADENCE: daily auto + 1 page | weekly 2h | monthly half-day | quarterly 2d
 | annual 3d | event-driven by rule
```

**Typed objects (exactly three):** `Signal` (direction, magnitude, confidence, half-life/expiry, decay class, capacity per book), `Target` (two scopes: PolicyTarget emitted only by `policy/`; PortfolioTarget emitted only by `construct/`), `Order`.

**Daily production order:** capture → store append → ladder (ensemble R, crowding, shadow log) → policy grammar emits PolicyTargets → sleeves emit Signals → construct (net, constrain, size) emits the complete Stage-1 portfolio → overlay multiplier if on (∈[0,1], veto) → exec scheduler → fills ledger → sentinel. The same code path pointed at historical as-of dates IS the backtest.

---

## 2. Module-by-module spec

Eleven top-level modules — the ceiling, not the floor (annually reviewable). Owner legend: **auto** = runs unattended; **Claude** = agent operates/maintains/drafts; **principal** = human decision or signature.

### 2.1 `data/` — capture, adapters, store, entity, breaks
**Job:** make lookahead structurally impossible and compound the desk's only appreciating asset (the PIT archive). **Inputs:** every free source (v1 set + AMC portfolios, participant OI, MWPL/ban, bulk/block deals, insider/SAST/pledge with dissemination timestamps, rating press releases, DPI exhaust: GST, e-way, UPI, Grid-India power, PPAC fuel, VAHAN, DCA food, F&O bhavcopy option chains). **Outputs:** the single `as_of(date)` API every other module reads through. **Cadence:** daily capture; weekly capture-health line; event-driven break entries. **Owner:** auto; Claude repairs fetchers same-day and drafts break entries; principal signs new-source scorecards and break entries.
- WORM daemon → one TET adapter per source, vintage-stamped inside the final transform so nothing lands unstamped; a format break is a one-file fix.
- Bitemporal parquet: every row carries (event_time, knowledge_time, source_version); corrections append, never overwrite. Backtests, live Stage 1, bias CI, and the recorder all read the same API.
- Entity master: ISIN-keyed; survivorship-free NIFTY-750 membership reconstructed once from dated NSE Indices press releases.
- `breaks/`: dated SEBI/structural registry (STT Oct-2024, expiry moves 2025, FutEq limits Oct-2025, Algo-ID Apr-2026, GDP base-year revision ~2026). Auto-segments affected backtests; may answer "insufficient post-break data".
- New sources: Denev–Amen due-diligence scorecard + live-capture probation on a pre-registered grid (by class, trading days {126, 189, 252}) before their history is admissible. Kaggle/HF exploration-only.

### 2.2 `harness/` — the one evidence machine
**Job:** be the only path by which anything becomes evidence. **Inputs:** YAML experiment configs; as-of data. **Outputs:** recorded runs (params, vintage hash, code hash, grid size, metrics + BCa CIs); Challenger state reads; the trial ledger. **Cadence:** continuous. **Owner:** auto; Claude authors configs; principal approves pre-registrations at the weekly gate.
- Recorder = trial ledger: every run — including abandoned agent attempts and every sweep cell — auto-registers BEFORE results are viewed; DSR trial counts derived by query, never self-reported. Pre-registered trial budget per quarterly research cycle; when spent, the funnel halts until the next cycle (no borrowing).
- Mandatory gates: adversarial bias CI (chained truncated-backtest diffing + warm-up sufficiency — catches code-level lookahead vintage manifests cannot see; a net, not a proof); CPCV + PBO (grid {0.1, 0.25, 0.5}) with uniqueness weights wherever labels overlap; no naked Sharpe anywhere; capacity line and cost-in-SR speed limit per book; death certificate completeness; **LLM-provenance flag** — LLM-sourced hypotheses are marked at registration and require post-training-cutoff / out-of-corpus validation windows, because pretraining contamination makes the agent's priors themselves lookahead.
- Harness-integrity kill-switch: any run reading outside the as-of API fails CI and is inadmissible by construction. Discipline in CI, not in virtue.
- Rotation ledger: which fitted parameter set/sleeve version is online at every date; the rotation policy itself is replayable and backtestable; rolling refits cross-window-ensembled (soft hysteresis), validated against — never inside — the fixed-budget regime score; every rolling window counts as a trial.
- Research/production parity: the same runner emits backtests and the live Stage-1 run.

### 2.3 `ladder/` — risk engine (Stage 1 top-down; v1 core kept)
**Job:** the 16-variable cycle ladder → regime score R → bucket. **Inputs:** as-of ladder inputs. **Outputs:** R, bucket, crowding states, shadow logs. **Cadence:** daily. **Owner:** auto; any rule change is principal-signed via Challenger.
- Kept frozen: 16 variables, fixed block budgets (0.25/0.20/0.20/0.20/0.10/0.05), Tier-C reduce-only clamp, 4 buckets, Hamilton-never-HP, <10-transitions rule.
- **R = median of an ensemble of pre-registered grid variants** of the same ladder; within-block weights drift only inside pre-registered bounds, shrunk to the frozen prior, with hysteresis. First response to detected drift is uncertainty-widening/de-risking via the existing buckets — never refitting.
- **`crowding/`** (new, daily, reduce-only, outside the frozen budgets like Tier-C): per-sleeve valuation spreads, futures OI, AMFI factor-fund flows/AUM, MF-portfolio concentration, correlation spikes, stress-test days-to-liquidate. Throttle only; doubles as the resurrection gate. India momentum is its first customer.
- New inputs within existing budgets, Tier-C reduce-only until self-validated through the funnel: DPI nowcast factor (RBI WPS 03/2020 replication) → macro-credit; rating-action diffusion + CCIL corporate spreads → credit-cycle state; participant OI z-scores, MWPL ban breadth, self-computed IV surface → fast-stress/sentiment; SIP stoppage, demat additions, IPO pipeline → valuation/sentiment.
- Cross-country sign-consistency gate for any new cycle rule (India has ~3 credit cycles; borrow US/EM via FRED/BIS — sign consistency on a grid, never effect-size equality).
- Shadow GMM: non-trading daily posterior log beside R; disagreements feed the research queue; promotion path, if ever, only after years of live log and 10+ observed transitions, reduce-only, via Challenger.

### 2.4 `policy/` — regime → book policy as executable data
**Job:** turn R buckets into book policy mechanically. **Inputs:** R/bucket, breaks registry, cost curves. **Outputs:** PolicyTargets (asset mix within debt≤70%/gold≤50%, per-book vol targets with leverage derived within the frozen ≤1.5x, hedge grid 0–150%, tail throttle). **Cadence:** daily evaluation; amendments only on scheduled reviews. **Owner:** auto execution; the policy file's content is principal-owned (signed amendments with diff + historical replay + ledger entry).
- Tiny trigger/action grammar (≤5 trigger types, ≤6 action types) — versioned, diffable, replayable.
- `hedgegrid/` as a cost-and-capacity-constrained object: post-STT per-instrument cost curves; SEBI delta-based FutEq position limits (net ₹5,000cr / gross ₹10,000cr) as a hard ceiling from `breaks/` — the Conservative book discovers in design, not in a crisis, when 150% futures hedging is regulatorily infeasible, and substitutes option spreads or gross reduction.
- Trend/TSMOM block and hedge grid scored in **crisis-insurance currency**: payoff in worst-decile NIFTY months net of bleed, with India-specific bleed (STT, roll costs) validated first — the metric the binding drawdown constraint actually grades.

### 2.5 `sleeves/` — return engine
**Job:** the five factor sleeves → commensurable, self-shrinking, cost-netted alphas. **Inputs:** as-of universe per book, prices/fundamentals/flows. **Outputs:** Signal objects. **Cadence:** daily scoring; quarterly half-life refits within grids. **Owner:** auto; Claude maintains; changes via Challenger.
- Flow order: sector-relative z option per sleeve (pre-registered choice) → forecast currency (vol-standardized, estimated scalar so E|f|=10; cap from grid {15, 20, 25} confirmed once via CPCV then frozen as null; handcrafted rule-based combination weights) → Grinold alpha = residual vol × grid-IC ({0.02, 0.05, 0.10}) × score, uniqueness-weighted realized IC with hysteresis → class-conditional decay haircut (mechanical sleeves — momentum, reversal, low-vol — steeper haircuts and shorter review clocks than judgment sleeves; half-life re-estimation shrinks toward the class prior) → cost-netted alpha (expected round-trip cost subtracted before ranking).
- New conditioning variables (published effects, haircut, own death certificates): pledge-change exclusion/negative, insider-net-buy positive, MF-crowding penalty on momentum sizing. Flow-signal block (index-rebalance mechanics, SIP persistence, FPI rotation) is the pre-registered next research cycle, not a day-1 build.
- Two-tier admission: rationale-backed vs statistics-only; statistics-only sleeves confined to the Aggressive book's short-horizon sleeves with lower weight caps and hair-trigger certs.
- Admission matrix per book: a sleeve trades in a book only if its capacity line clears zero net of impact at that AUM and its cost-in-SR speed limit is met — mechanically excludes ST reversal from Conservative by rule.

### 2.6 `construct/` — Stage 3 (equity cross-section only, frozen)
**Job:** one integrated optimizer per book. **Inputs:** Signals, PolicyTargets, Ledoit-Wolf covariance, cost model. **Outputs:** PortfolioTargets — the complete Stage-1 portfolio. **Cadence:** daily target recompute vs drift bands; weekly rebalance heartbeat. **Owner:** auto.
- Kept: dispersion-set name count, 5–6% entries, ~10% drift bands (buffered around the optimal position), sizing = min(frozen cap, haircut-Kelly, buildable-within-half-life) × drawdown cushion, characteristic portfolios + Ledoit-Wolf for risk budgeting.
- `netting/`: all sleeves net into ONE optimizer per book before any order exists; internal crossings never hit the market (free alpha at 22.3bps round trip); sleeve-level paper books retained so the decay ledger keeps its evidence base.
- `xrisk/` (the missing box in v1): thin cross-sectional risk model — grid-defined sector/size/beta bands and central factor caps (market beta, size, five sleeves, rates/INR sensitivity) as hard pre-trade constraints, so stock selection cannot smuggle macro bets that belong to the policy layer; **ex-ante tracking error vs Nifty 50** from the existing Ledoit-Wolf stack, reported beside the governor. Bands set wide from historical sleeve-exposure grids; binding frequency reviewed annually; never tightened ad hoc.
- Buildable cap parameterized by MF small/midcap stress-test days-to-liquidate for ranks 250–750 (state input only; history too short to fit).

### 2.7 `overlay/` — Stage 2 as internal TOPS + meta-labeling (frozen posture)
**Job:** make judgment falsifiable and structurally reduce-only. **Inputs:** the complete Stage-1 portfolio; suggestions from Claude and the principal. **Outputs:** size multiplier ∈[0,1]; off = pinned to 1; human veto retained. **Cadence:** nightly scoring; influence step reviews semi-annual at most. **Owner:** Claude and principal as symmetrically scored contributors; auto scoring; principal signs influence steps.
- Every suggestion is a standardized timestamped paper trade (direction, size, horizon, rationale tag) scored against the Stage-1-only counterfactual — the Stage1-vs-Stage1+2 experiment runs continuously by construction.
- Influence is a published grid function of rolling scored hit-rate by category, starting at zero; N=2 means long windows and deflated significance before any step-up. **Both believability scores can fall, with the same consequence: influence steps back toward zero.** Veto survives any score.
- Meta-labeling is the eventual systematic form: multiplier in [0,1] on Stage-1 sizes, mathematically incapable of adding exposure; trains only once years of non-overlapping Stage-1 outcomes exist; until then it paper-trades in `tops/`.
- Text features only via chrono-consistent LLM checkpoints (vintage-stamped like data, entity-anonymized), deferred to year 2 behind an Indian-entity coverage/leakage audit. Frontier-model backtests stay inadmissible.

### 2.8 `exec/` — execution and the desk's only proprietary dataset
**Job:** implement targets cheaply; learn from own fills. **Inputs:** PortfolioTargets (post-overlay), ADV/ban/rebalance calendars. **Outputs:** Orders, fills ledger, impact coefficients. **Cadence:** daily scheduling; quarterly impact refit; event-driven kill. **Owner:** auto within pre-set parameters; Claude monitors; principal reviews quarterly.
- Deterministic scheduler: entries spread over N days at ≤X% ADV (grids), futures-first for hedge changes, never initiate into MWPL-ban names, avoid supplying liquidity into index-reconstitution days (Conservative).
- Fills ledger from day one: arrival price, participation, spread, realized impact vs the sqrt prior.
- Quarterly impact refit **shrunk toward the sqrt prior**; benign months may never loosen participation caps; the execution kill may tighten immediately, loosening only on schedule. Statutory cost tables versioned via `breaks/` (the 5.7bps futures figure is already stale post-STT).

### 2.9 `sentinel/` — monitoring as a subscriber, surfaced as one page
**Job:** monitoring somebody actually reads; kills that fire by rule. **Inputs:** all pipeline outputs (subscriber, never inline). **Outputs:** the daily page; alarms; cert executions; monthly attribution pack. **Cadence:** daily page; monthly pack; event-driven certs. **Owner:** auto; Claude authors the page; principal reads (≤10 min, often 0).
- `dailypage/`: ONE fixed-format page, RAG header. Green = principal may skip; push only on amber/red with a pre-registered response menu. Contents: capture health; R + bucket + policy stance + triggers fired; crowding; CUSUM alarms; governor headroom + ex-ante TE vs Nifty 50; slippage vs model; overlay paper P&L; open exceptions. Dead-man switch: RED unacknowledged for T hours (grid) → auto de-risk one rung. Quarterly alert-path drill (synthetic amber) tests the push channel.
- `cusum/`: per-sleeve sequential monitors on live alpha, thresholds calibrated on own block-bootstrapped history; reduce-only sizing overlay decoupled from entries.
- `certs/`: death certificates at birth for every deployed signal (drawdown budget by rationale tier, live-vs-backtest Sharpe floor, hit-rate floor, crowding ceiling, resurrection criteria); kill tiers fire by rule: down-weight → quarantine → retire → archive. Horizon-matched: hard mechanical stops for fast/statistics-only sleeves; evidence-based structural review (decay indicators, crowding, cost creep — never raw PnL) for slow factor sleeves. Certs retro-registered for already-live v1 sleeves during migration.
- `attribution/` (monthly, auto): uniqueness-weighted realized IC per sleeve; **Transfer Coefficient per book decomposed by which constraint destroyed the signal** ("IC decayed: retire" vs "TC collapsed: fix plumbing"; Conservative's structurally low TC is a design fact); QEPM factor attribution feeding the decay ledger from the desk's own books; netting savings in bps; crisis-insurance metric; **walk-forward concatenation from each signal's registration date as its only standing evidence — never re-run backtests**.
- `governor/`: the frozen binding drawdown governor, unchanged; its test suite is historical replay + own block bootstrap, fenced as test-only (can fail code, never validate safety).

### 2.10 `research/` — the funnel and the bounded agent loop
**Job:** turn AI throughput into a bounded, metered discovery process. **Inputs:** hypotheses (provenance-tagged), archive, shadow disagreements, breadth budget. **Outputs:** pre-registered survivors; graduated signals; archive updates. **Cadence:** continuous T0–T2; weekly triage; quarterly budget reset. **Owner:** Claude runs T0–T2 autonomously; principal is the weekly gate.
- Tiers, each auto-taxing the trial ledger: T0 tear sheet (IC decay, quantile spreads, turnover — kills most ideas in minutes) → T1 vectorized sweep (grid size auto-logged) → T2 harness replay with statutory costs + bias CI + CPCV/PBO → T3 paper probation against live capture (length from the decay-class grid) → live at reduced weight per pre-registered schedule.
- Registration fields per candidate: rationale tier, decay class, capacity lines per book, cost-in-SR estimate, death certificate, **hypothesis provenance** (LLM-sourced → post-cutoff validation windows).
- The principal sees ≤3 pre-registered survivors per week with full gate reports; approves, vetoes, or returns.
- `archive/`: retired signals paper-trade with pre-registered resurrection criteria (fresh OOS evidence + cleared crowding); capacity K on an annual-review grid with rank-based eviction; resurrection tests count as trials.

### 2.11 `govern/` — charters, locks, reports, Challenger registry
**Job:** the slow layer — rules about changing rules. **Inputs:** ledgers. **Outputs:** signed charters, Challenger state transitions, annual report. **Cadence:** quarterly/annual/event. **Owner:** principal owns; Claude drafts everything from ledger data.
- **Challenger registry (the single adaptivity-admission law):** every adaptive rule exists in exactly one of {shadow: logged, zero influence | challenger: paper-traded against the frozen incumbent with pre-registered win criteria — DSR of the difference, PBO, bootstrap CI excluding zero | online: reduce-only first, full grid weight only after a second review}. Demotion symmetric and rule-driven. Promotions only on scheduled review dates (calendar fixed a year ahead). **Frozen v1 parameters are the null hypothesis forever.** Enforced by harness: a rule not marked online cannot influence production (CI check).
- **Anti-capitulation lock (mechanical):** no parameter/budget/structure change may be *initiated* while the affected sleeve is beyond a grid-defined drawdown depth; executing pre-registered rules (governor, certs) is always allowed; changing rules mid-pain never is.
- ML/AI charter: ML admissible where data is abundant and feedback fast (execution, covariance/cost estimation, monitoring anomaly detection, research tooling, feature combination within admitted sleeves); disallowed for low-sample macro/regime prediction except non-trading shadows; chrono-checkpoints the only text path. Amended annually, pre-registered.
- Quarterly: Ilmanen three-lens expected-returns dashboard → Kelly-numerator caps via the pre-registered reduce-only mapping; carry-like vs crisis-convex tag per sleeve and net bad-times beta beside the governor; memo to the humans' asset-mix policy review (informs, never optimizes, never times); trial-budget close-out; Challenger review date.
- Annual: Report on the Management of the Books (auto-drafted; each book decomposed into policy mix vs Stage-3 tilts vs Stage-2 overlay vs execution, each layer against its pre-registered null; tilts must be self-funding vs policy); breadth budget (the ladder is ~one bet per cadence; the 750-name cross-section holds nearly all breadth; allocate research hours by marginal breadth × attainable IC); scope-cap and charter review; dataset scorecard review; archive purge. Principal signs exceptions in writing.
- Event: after any >20% NIFTY drawdown episode ends, the Ang–Goetzmann–Schaefer decomposition on own active returns runs from the stored template (was "alpha" hidden beta?) — post-episode, never mid-episode.

### The runbook (principal attention budget: ~30 min/day → 0 most days, 2h/week, half-day/month, 2 days/quarter, 3 days/year)
- **Daily (auto):** 18:30 IST capture → validation → store; 19:30 ladder/policy/sleeves/construct/overlay-scoring/CUSUM; 20:30 dailypage publishes. Validation miss at cutoff = data kill-switch fires automatically (last-good + de-risk one rung, flagged). Claude repairs fetchers, reruns jobs, files exceptions.
- **Weekly (2h):** rebalance heartbeat; research triage of ≤3 survivors; overlay scorecard paragraph; the week's daily pages read regardless of color.
- **Monthly (half-day):** attribution pack; decay-ledger review (fired certs confirmed executed, not debated); rotation entries.
- **Quarterly (2 days):** impact refit; capacity re-audit; half-life re-estimation; Ilmanen dashboard; trial-budget reset; Challenger review; alert drill.
- **Annual (3 days):** report, breadth budget, charters, scope caps, archive purge.
- **Event:** SEBI circular → break entry (Claude drafts, principal signs); kill tiers fire without meetings; post-drawdown AGS review.

### Kill-switch battery
1. Drawdown governor (frozen, binding). 2. Data kill: capture/vintage failure → last-good snapshot AND de-risk one rung; never trade unverified data. 3. Signal kill tiers per certs. 4. Overlay kill: hit-rate floor breach or evidence contamination → multiplier pinned to 1. 5. Execution kill: slippage > grid-multiple for N days → halt non-essential trades (policy hedging continues); may tighten caps immediately. 6. Anti-capitulation lock. 7. Harness integrity: reads outside the as-of API are inadmissible by construction. 8. Dead-man: unacknowledged RED page for T hours → auto de-risk one rung.

### Migration order (each step ships value alone)
Q1: capture + adapters + as-of store for revision-prone series; harness runner/recorder (with LLM-provenance field from day one); dailypage; **Challenger registry stood up with frozen v1 parameters enrolled as permanent nulls**. Q2: harness gates (bias CI, CPCV/PBO); netting + xrisk + TE; exec scheduler + fills; **death certs retro-registered for live v1 sleeves**. Q3: forecast currency + Grinold + class priors; policy grammar + hedge-grid rebuild; crowding; admission matrix. Q4: TOPS overlay scoring; funnel + agentloop at full meter; first annual report; entity master completion. Year 2+: metalabel training accrual; chrono-LLM audit; flow-signal research cycle; DPI nowcast validation.

### Minimum module set (if the build stalls)
`data/capture+store`, `harness/`, the unchanged v1 Stage 1 (ladder→policy→sleeves→construct), `exec/scheduler+fills`, `sentinel/dailypage+certs+governor`. The Challenger registry's degenerate state — nothing adapts, frozen nulls run — is the safe default. Everything else is a compounding upgrade; the desk does not survive silent data rot, uncounted trials, or monitoring nobody reads.

---

## 3. Feedback-loop table

| # | Loop | Trigger | Cadence | May change | May NEVER change |
|---|------|---------|---------|------------|------------------|
| FL1 | Fills → impact model → sizing/capacity | Scheduled refit; execution kill (tighten path) | Quarterly; event tighten-only | Impact coefficient (shrunk to sqrt prior); participation caps DOWN | Loosening caps off-schedule; statutory cost tables (breaks/ only); frozen turnover caps |
| FL2 | Attribution/IC/TC → decay ledger → haircuts | Monthly pack; quarterly refit date | Monthly diagnose, quarterly act | Per-sleeve haircut/half-life within class-prior shrinkage + hysteresis | Block budgets; sleeve roster (one-in-one-out via funnel only); estimation standards |
| FL3 | CUSUM alarms → sizing | Self-calibrated thresholds | Daily | Position sizes down (decoupled from entries) | Adding exposure; entry logic; the CUSUM rule itself (Challenger only) |
| FL4 | Crowding → sleeve throttle + resurrection gate | Grid thresholds | Daily | Sleeve size down; block a resurrection | Adding exposure; entering the frozen block budgets |
| FL5 | TOPS hit-rates → overlay influence grid | Scheduled review only | Semi-annual step-ups | Influence step per published grid, up or down to zero, per contributor | Hard cap; reduce-only structure; veto; off=1; Stage-1 contents |
| FL6 | Recorder → DSR trial counts | Every run | Continuous | Nothing (measurement only) | Counts edited or self-reported; runs outside the harness |
| FL7 | Rotation ledger → online parameter set | Scheduled rotation dates via Challenger | Quarterly | Which pre-registered variant is online (cross-window ensembled) | Fixed budgets; anything outside the pre-registered grid; off-schedule swaps |
| FL8 | Ilmanen dashboard → Kelly-numerator caps | Quarterly review date | Quarterly | Numerator caps DOWN via pre-registered mapping; memo to policy review | Raising numerators intra-quarter; acting as a timing signal; mechanical asset-mix changes |
| FL9 | TC-by-constraint → plumbing fixes | Monthly pack | Monthly diagnose; fixes via pre-registration | Execution/constraint plumbing through Challenger | Loosening frozen caps or the governor to raise TC |
| FL10 | Death certs → kill tiers | Cert conditions met | Event (checked daily) | Down-weight → quarantine → retire → archive | Debating a fired cert; raw-PnL kills for slow sleeves; resurrection outside pre-registered criteria |
| FL11 | Capture health → data kill | Validation failure at cutoff | Event | Run on last-good AND de-risk one rung | Trading unverified data; skipping the de-risk |
| FL12 | Breaks registry → segmentation + ceilings | Dated SEBI/structural event | Event | Backtest segmentation; hedge-grid ceilings; cost tables | Forcing fits on short post-break samples |
| FL13 | Shadow GMM disagreements → research queue | Logged divergence episodes | Semi-annual review | Research queue entries | Any trading influence; touching R; promotion before 10+ observed transitions |
| FL14 | Challenger reviews → adaptive-rule states | Scheduled review dates only | Quarterly/annual per rule class | State transitions per pre-registered win/demote criteria | Deleting the frozen null; off-schedule promotion; initiation mid-drawdown |
| FL15 | Breadth budget → research agenda | Annual review | Annual | Research-hour allocation | Gate standards; raising trial budgets mid-year |
| FL16 | Scope-cap review → module/sleeve/object ceilings | Annual review via Challenger | Annual | The caps (with retirement offsets) | Mid-year additions; removing the minimum module set |
| FL17 | Governor → exposure | Drawdown thresholds | Daily, binding | Exposure down per policy | Its thresholds/ceiling — relaxation never |

---

## 4. Changelog vs pipeline v1

| Change | Borrowed from | Survival / anti-overfit note |
|---|---|---|
| Bitemporal PIT store + single as-of API over WORM capture + TET adapters | operations (pattern in all three) | Lookahead structurally impossible; the PIT archive compounds while signals decay |
| Regulatory-break registry | all three | May answer "insufficient post-break data" — never forces a fit |
| Harness: recorder IS the trial ledger; auto-count before results viewed; DSR by query | all three (anti-overfit wording) | Registration as a side effect of execution is the only 14-year-durable pre-registration |
| Research/production parity (one runner for backtest and live) | operations | One code path to audit; kills live-vs-backtest mismatch |
| Adversarial bias CI stage-gate | all three | Catches code-level lookahead at AI-codegen scale; a net, not a proof |
| CPCV+PBO+BCa gates; no naked Sharpe; uniqueness weights | all three | The overfit gate that scales with agentic throughput |
| Harness-integrity kill-switch | operations | Discipline in CI, not in virtue |
| Challenger Protocol as single adaptivity law | anti-overfit (grafted per all judges) | Frozen v1 = permanent null; adaptivity enters only as a falsifiable challenger on scheduled dates |
| LLM hypothesis provenance flag + post-cutoff validation | ai-adaptive | The agent's priors are lookahead; contamination fenced at registration |
| Pre-registered trial budget per cycle; funnel halts when spent | ai-adaptive/all | Stops DSR becoming a rejection machine that tempts standard-lowering |
| Funnel T0–T3 + metered agent loop; ≤3 survivors/week to principal | operations | Kill-fast tiers tax the ledger; the human gate stays bounded |
| Death certs at birth; horizon-matched retirement; capped archive w/ rank eviction; retro-registered for live sleeves | all three (retro: operations) | No fresh debate in pain; no puking value at the bottom; resurrections are trials |
| Two-tier admission + class-conditional decay priors | all three | Mechanical recipes crowd and die first; priors match the failure mode |
| R = ensemble median of pre-registered grid variants; drift → de-risk, never refit | all three | Diversity insurance without fitted regime models |
| Daily reduce-only crowding monitor, outside budgets, resurrection gate | all three | Throttle-only; unwinds are the likeliest governor violators |
| Shadow GMM non-trading logger | all three | Hedges ladder staleness without violating the <10-transitions rule |
| New ladder inputs (DPI nowcast, credit diffusion, OI/IV, SIP/demat) Tier-C reduce-only | all three | Budgets fixed; each input is its own registered trial |
| Policy as versioned trigger/action data (≤5/≤6 types); per-book vol targets, leverage derived | all three | Amendments get diffs and replays instead of silent prose drift; frozen 1.5x intact |
| Hedge grid cost- and FutEq-constrained; crisis-insurance scoring net of India-validated bleed | all three | Infeasibility discovered in design, not in the crisis the binding constraint grades |
| Forecast currency (estimated scalar; cap on grid) → Grinold alpha (grid IC, uniqueness-weighted) → cost-netted alpha | all three (grid discipline per judge flags) | Alphas self-shrink as IC decays; conventions confirmed once on grids then frozen as nulls |
| Sector-z option + pledge/insider/MF-crowding conditioners | all three | Published effects, haircut, own death certificates |
| Netting into one optimizer per book; sleeve paper books retained | all three | Free alpha at 22.3bps; decay ledger keeps its evidence base |
| Thin xrisk model: factor caps + ex-ante TE vs Nifty 50 beside governor | all three | Engine sees the benchmark-relative constraint; no smuggled macro bets; caps never tightened ad hoc |
| Buildable cap from MF stress-test days-to-liquidate | all three | State input only — history too short to fit |
| Stage 2 = TOPS + meta-label [0,1]; both parties scored, falling score pins influence to zero | all three (symmetry: operations; consequence: synthesis) | Judgment becomes falsifiable and reduce-only by construction; veto survives |
| Chrono-consistent checkpoints as only text path, year 2, audit-gated | all three | Text models vintage-stamped like data; frontier backtests stay banned |
| Exec module: scheduler + fills ledger + quarterly shrunk impact refit, tighten-fast/loosen-on-schedule | operations (cadence per judge 2) | Own fills are the only proprietary data; benign months can never loosen caps |
| Sentinel: one-page RAG + dead-man de-risk + self-calibrated CUSUM + TC-by-constraint + walk-forward-only evidence | operations + anti-overfit WF rule | Monitoring someone reads; "retire" vs "fix plumbing" separated; never re-run backtests |
| Kill-switch battery incl. data kill wired into the daily schedule | operations + judge-2 fix | Every failure mode has a pre-registered reflex; never trade unverified data |
| Anti-capitulation lock; ML charter; annual Report w/ per-layer nulls; AGS template; breadth budget | all three | Changes only from strength on scheduled dates; layers graded against their own nulls |
| Ilmanen → Kelly channel specified as rule-based reduce-only grid mapping | synthesis (resolving all three judges) | Closes the judgment leak into Stage-1 sizing |
| Rotation ledger, backtestable rotation policy, cross-window ensembling | all three | The when-to-swap meta-decision is auditable and its trials counted |
| Cross-country sign-consistency gate + source scorecard + probation on grids | all three (grids per judge 1) | Raises effective sample honestly; sign consistency, not effect-size equality |
| Scope caps as standing policy, annually Challenger-reviewable | operations + judge-3 amendment | Ops overload kills 2-person desks; and the caps cannot ossify either |
| Principal attention budget + runbook + degraded mode + quarterly alert drill | operations + judge-3 fix | Attention is the binding resource; the alarm path is tested, not trusted |
| Minimum module set fallback | operations | Pre-declared answer to a stalled build or disappointing AI tooling |

---

## 5. Deliberately REJECTED, and why

1. **skfolio (or any external engine) as a runtime dependency** (ai-adaptive) — 14-year maintenance risk for marginal benefit; patterns only, thin self-built implementations (sided with operations, judges 2–3).
2. **Stacking / ML signal combination inside `construct/`** (ai-adaptive) — signal combination is return-engine estimation; placing it in Stage 3 blurs the frozen equity-cross-section-only boundary (judge 1). If ever built, it enters `sleeves/` through the funnel with handcrafted weights as the permanent null.
3. **PolicyTargets emitted from construct** (ai-adaptive diagram) — as drawn it violates asset-mix-is-policy; policy targets originate only in `policy/`.
4. **Monthly impact refits** (anti-overfit, ai-adaptive) — own-fill samples too small; quarterly with a tighten-only event path (judge 2's sample-size argument).
5. **Adaptivity-first framing: ten parallel loops each with bespoke promotion rules** (ai-adaptive) — over-adaptation is the historically dominant killer and heterogeneous promotion rules are where drift gets in over 14 years; one Challenger law instead (all judges).
6. **Weekly research cycle with an unbounded funnel and quarterly whole-set rotations as default temperament** (ai-adaptive) — more model churn than one principal can audit; rotation exists but only via Challenger on scheduled dates.
7. **VineCopula synthetic stress paths as governor evidence** (operations) — synthetic data flirting with evidence for the binding constraint; replaced by own block-bootstrap + historical replay, fenced test-only: may fail code, never validate safety or calibrate thresholds (judge 1).
8. **Untestable rhetoric as design justification** ("2022 proves the frozen parts right", "every credible firm converged", "90% of the benefit") — struck; single episodes are consistency evidence, not proof (all judges).
9. **Range-stated parameters** ("6–12 months", "size capped" with no mechanism, E|f|/cap as imported constants) — restated as pre-registered grids with defined selection and eviction rules (judge 1).
10. **MLflow server, MongoDB, ArcticDB, LEAN/Nautilus/Qlib as engines, vectorbt-PRO** (all proposals' source material) — SQLite + parquet + own thin code; every borrowed idea admitted only in its minimal form.
11. **A rich policy DSL** — ≤5 trigger and ≤6 action types; a rich in-house language is unmaintainable at N=2.
12. **Model zoo growth; per-sleeve independently trading sub-portfolios** — a new sleeve requires retiring one; netting into one optimizer per book is mandatory.
13. **Chrono-LLM text signals in year 1** (ai-adaptive implied earlier adoption) — deferred to year 2 behind an Indian-entity coverage/leakage audit; Indian coverage in open chrono-checkpoints is unproven.
14. **Frontier-LLM backtests, unflagged LLM hypotheses, Kaggle/HF as evidence** — frozen ban, extended by the provenance flag; exploration only.
15. **Promotion of the GMM (or any fitted regime-switcher) into trading** — stays a non-trading shadow until 10+ observed transitions AND a Challenger win; in practice likely never inside this horizon.
16. **Second dashboards, extra monitoring surfaces, standing meetings** — the failure mode is surface area nobody reads; one page, drills, and rules instead.
17. **Intraday expansion** — out of scope for the desk's breadth budget and attention budget; not revisited before an annual review.

---

## 6. Open questions for the principal

1. **Grid sign-offs before Q1 build:** per-book vol-target grid and bucket→rung map; probation-length grid assignments by decay class; quarterly trial budget; archive capacity K and the resurrection-priority rank rule; dead-man T hours; the overlay influence grid and its hard cap; PBO threshold choice from {0.1, 0.25, 0.5} per tier.
2. **Legal/compliance posture:** NSE/BSE/AMFI terms for automated capture and internal WORM archiving; the exact reading of SEBI's delta-based FutEq limits at the Conservative top end; which option-spread structures the mandate permits as hedge substitutes.
3. **Conservative book TC:** accept structurally low transfer coefficient as a design fact, or shrink that book's active risk further and lean more on policy? (Affects the admission matrix.)
4. **Degraded-mode tolerance:** after how many consecutive last-good-snapshot days does the desk step down a second rung or go to policy-only? (Grid to pre-register.)
5. **Availability protocol:** if a RED page fires while you are unreachable beyond T hours, the dead-man de-risks one rung — is one rung enough, and should repeated unacknowledged REDs escalate to the worst bucket automatically?
6. **GDP base-year revision (~2026):** pre-agree treatment as a registry break with a dual-vintage parallel run of the macro block, or wait for MOSPI's mapping tables?
7. **Parallel run:** how long do v1 and v2 Stage 1 run side by side (paper) before capital migrates, and which book migrates first? (Suggest Aggressive first — smallest, fastest feedback; confirm.)
8. **Year-2 priority order:** chrono-LLM coverage audit vs the flow-signal research cycle vs meta-label training — pick the single first claim on the year-2 breadth budget.
9. **Challenger calendar:** fix the four quarterly review dates and the annual date now, a year ahead, so no review date can be chosen (or avoided) in reaction to performance.
10. **Cut order beyond the minimum set:** if Q1–Q2 telemetry shows the attention budget is violated, confirm the pre-declared order in which non-minimum modules get frozen (suggest: overlay scoring first, then funnel throughput halved, then crowding to log-only).

---

## Machinery status addendum (2026-09-02) — what now exists as tested code

| Pipeline component | Code | Tests | Status |
|---|---|---|---|
| Ladder seat modules (10) | quant/ladder/*.py | planted-truth + real fixture | live |
| Regime-score assembler (Stage-1 spine) | quant/regime.py | 8 exact (incl. Tier-C overlay, reduce-only clamps) | live; first real timeline in research/cycles/daily-batch/regime-DEMO.md |
| Bucket mapping (quantile rules) | quant/regime.bucket_path | warm-up = no-bucket enforced | live |
| M4 walk-forward adjudicator | quant/validation/walkforward.py | 5 exact | live; first outing disqualified the F2-index shortlist |
| Estimation (tau, DSR, purged CV, Hamilton, bootstrap) | quant/stats/ | Monte-Carlo validated (Track R) | live; Andrews near-unit-root variant queued |
| Statutory + impact + per-book turnover cost | quant/costs/ (incl. book.py) | 4 + golden | live; ADV PROVISIONAL travels on every number |
| Challenger registry (adaptivity-admission law) | config/challengers.yaml + validator gate | 4 enforcement tests | live in CI; 'online' is review-gated |
| Paper-trade ledger | research/register/paper-ledger.md | format + lapse policy | PT-1, PT-2 open |
| Ingestion kit (Priority-1) | ingest/pull_* (bhavcopy, indices, VIX, CCIL, AMFI, NSDL, FRED) | auth skeletons via --emit-auth-template | awaiting principal-machine runs |
| Vaults (8) + manifest + two-pass authentication | ingest/vault/ | manifest WORM; misses recorded | live |

## Machinery status refresh (2026-09-03) — deltas since the addendum above

| Delta | Where | Status |
|---|---|---|
| Andrews near-unit-root estimator (was "queued") | quant/stats/andrews.py | live, MC-tested; F1c consumed it (3.19m, CI [2.19,4.63]) |
| auroc promoted from script-local to library | quant/stats/metrics.py | live, 3 planted-truth tests (process note #6) |
| Census→DSR wiring | quant/stats/dsr.census_n() | live; rising-floor test; Sharpe claims can no longer undercount trials |
| Commit gate as machinery | .githooks/pre-commit + .github/workflows/ci.yml | live both sides; refuse-path proven with a red canary; remote runs green |
| Reproducibility audit | research/register/REPRODUCIBILITY.md | first pass 2026-09-03: 50/50 scripts, 29/29 headlines reproduce; annual re-run wired |
| Puller template tests | tests/test_landing_day.py | emit + WORM-refusal verified for both flag-bearing pullers |
| Vaults | ingest/vault/ (now 10) | + India VIX 2010-23, INR/USD, Kilian, Känzig, ONI 1950-2026, AISMR 1872-2016 — all two-pass, mirror frontier EXHAUSTED 2026-09-03 |
| Future sweeps pre-registered | trial-ledger HG1 / BW1 | bars frozen years ahead of their data; risk.yaml/ladder.yaml forward references discharged |
| Census | research/register/trial-count.md | 164 run cells; suite 121 green |

## Track P kickoff (2026-09-03) — the ML pipeline's first committed machinery
Per the reopened-generation directive, pipeline-v2's architecture began landing as tested
code YEARS before its data: `quant/pipeline/labeling.py` (triple-barrier events +
meta-labels — the design's chosen ML consumption: bet-sizing filters, never raw direction)
and `quant/pipeline/vintage.py` (as-of-stamped series whose `asof(view_date)` accessor is
the anti-lookahead primitive; `final()` is diagnostics-only by convention). Both
planted-truth tested (tests/test_pipeline.py: deterministic barrier hits incl. the short
side; revisions invisible before publication). Purged CV + the M4 walk-forward already
exist in quant/stats and quant/validation. At bhavcopy landing, Phase-0 fixtures exercise
this scaffold before any ML design registers.

## Operating companion (2026-09-03)
The day-to-day workflow this architecture is run through — ten stations, machinery paths,
entry/exit gates, current line status — is written down in `docs/MODEL-FACTORY.md`
(operating document; changes nothing frozen, registers nothing).
