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
