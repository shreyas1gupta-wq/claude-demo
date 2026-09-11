# L3 verification — vix_vrp_v2 (Mechanism & execution)

Verifier: adversarial L3, pass-2 Demeter study. Scope: signals/vix_vrp_v2.py (read in full), dev_results/vix_vrp_v2.json,
dev_results/vix_vrp_v2_VERIFY.json, dev_results/vix_vrp_DESIGN_NOTE.md Part 2 (the v2 design note — no separate
`vix_vrp_v2_DESIGN_NOTE.md` file exists; the signal docstring points to this file, Part 2, and that is where the
Mechanism/Rules/Stress-narrative/Honest-weaknesses sections actually live — verified, not a missing-artifact defect).
No files edited, no `evaluate.py`/`results/` touched, no grid re-run, no new parameters proposed. One diagnostic
script was run against DEV-only data (`engine.load_market(end="2012-06-30")`) to test the coordinator's mechanism
question; it is descriptive only (no tuning).

## 1. Is the ELEVATED leg "the trap in disguise"? — TESTED, REFUTED (evidence favours the candidate)

The pass-1 trap (`vix_dissipation`) bought/held whenever **implied vol (VIX) itself was falling** relative to its own
moving average (`ratio = vix / sma(vix, vix_ma) < 1 - exit_buf`) — a momentum-in-IV bet that a lull would persist,
which fired 50-93% negative through 2000-02/2008 (DESIGN_BRIEF.md table: Sharpe -0.31, maxDD -93.5%).

`vix_vrp_v2`'s new rule 3 gates on **VRP = VIX/100 - RV10 > vrp_elev**, i.e. implied vol *rich relative to realised*,
not implied vol falling. I ran a DEV-only diagnostic (`engine.load_market(end="2012-06-30")`, coordinator's own
`sig.vix_regime`/`sig.signal`) over all 132 ELEVATED-gate-opening days at the frozen default (`vrp_elev=0.12`):

```
N ELEVATED-gate opening days: 132
Openings where VIX fell >3% over prior 10d:      28  (21%)
Openings where VIX flat/rising over prior 10d:   104  (79%)
Openings where RV10 fell >1pt over prior 10d:    112  (85%)
```

79% of gate-openings occur while **VIX itself is flat or rising** — the mechanical opposite of the dissipation
trap's precondition. The gate is overwhelmingly driven by **realised** vol normalising while **implied** vol stays
sticky/elevated, which is exactly the published VRP mechanism cited in the note (Bollerslev-Tauchen-Zhou 2009 —
a real, correctly-attributed paper, not a fabricated citation) and is causal (both VIX and RV10 are known at the
close per the module docstring). **Coordinator's suggested resolution is confirmed: this is not the pass-1 trap
in disguise; it is a distinct, and in fact opposite-signed, mechanism.**

Residual, disclosed caveat: 85% of openings coincide with RV10 falling, which includes an unavoidable rolling-window
artifact (a big shock day exits the 10-day realised-vol window ~10 sessions later, mechanically raising VRP even
absent a genuine calming). The design note is aware of and price this risk explicitly (round-1 table: raw gate
thresholds 0.08→0.10 swing Sharpe 0.597→0.713, "the signature of a daily gate that flips on single realised-vol
prints," DESIGN_NOTE.md:166) and chose 0.12 — the centre of a plateau, not the edge — partly to keep the 2000-02
bear openings sparse (12 of 132, mostly early-2000/early-2001, not spread through the grind) rather than eliminate
the artifact structurally. Zero of the 132 openings pushed leverage to ≥2x (spurious-reentry census, DESIGN_NOTE.md:293),
so even a spuriously-timed opening can cost at most a 1x-vs-0x day, not a re-leveraging mistake.

## 2. GFC daily drawdown disclosure — CONFIRMED, accurate

Coordinator asked whether the untouched -28.6% daily/GFC drawdown is disclosed. It is, in two places (signal
docstring "Known failure modes" and DESIGN_NOTE.md "Honest weaknesses" #4 and the stress narrative), and I verified
the number against the harness output directly rather than trusting the prose:

```
vix_vrp.json   stress_episodes.2007_09_gfc.model_max_dd_pct  = -28.60051656866642
vix_vrp_v2.json stress_episodes.2007_09_gfc.model_max_dd_pct = -28.60051656866535
```

Identical to 6 decimal places — the "untouched" claim is literally true, not rounded-to-look-true. The note correctly
attributes it to the 1x PANIC leg riding Jan-Mar 2009 at a *positive* VRP (realised vol fell under a still-elevated
VIX while price kept sliding) — a case where the VRP filter's own logic ("VRP normalising = shock over") is wrong,
and the note says so plainly rather than hiding it in an aggregate stat.

## 3. Mechanism pre-registration and consistency with the rule as coded

`DESIGN_NOTE.md` §Mechanism is written and dated before Part 2's runs (per its own "written before any run" header)
and states two testable claims (level regimes carry different premia; VRP is the shock detector/re-entry trigger).
Reading `signal()` line by line confirms the code matches the prose exactly: `vix_regime()` reproduces the frozen
original's state machine unmodified (docstring says so; a byte-for-byte structural comparison of the two functions in
`signals/vix_vrp.py` and `signals/vix_vrp_v2.py` shows only the ELEVATED branch differs — `LEV_ELEV_ON` is a genuinely
new leverage tier, not a renamed constant), the VRP crash filter (`vrp < vrp_min` → cash in every state) is unchanged,
and the new `elev_on = (reg==1) & (vrp > vrp_elev)` line is exactly rule 3 as described. No mismatch between narrative
and code found.

The note also discloses that the more dangerous hypothesis from its own Mechanism section — (c), a PANIC-state
VRP-normalisation re-entry to 2-3x mimicking the 23-Mar-2020 profile — was tested and **rejected** before being built
into v2 (spurious-reentry census: 2008 entries to ≥2x were 50-100% negative over the next 10 sessions, 2000-02 entries
36-67% negative, "same conclusion as crash_exit_dual and the pass-1 trap," DESIGN_NOTE.md:293-297). This is the
correct adversarial self-test and it was applied before freezing, not after.

## 4. Regime that breaks it — named, both historical and forward-looking

DESIGN_NOTE.md "Honest weaknesses" #4 names, in DEV: "a prolonged panic that grinds lower while realised vol
normalises (Jan-Mar 2009 again...)" and, forward-looking: "...or 1x through a 2022-style slow bear if VIX sits above
30," plus a second failure regime, "a multi-year bull with VIX pinned at 16-30 and realised vol close to implied
(1996-97 chop, 2010-11), which the machine sits out almost entirely at ~0.2x." Both a historical DEV regime and a
plausible future one are named, as required. Satisfied.

## 5. "Strategy in its own right" vs over-claiming Demeter resemblance — no over-claim found

The new leg's citation is Bollerslev-Tauchen-Zhou (2009), an independent published result, not a claim of Demeter
resemblance. Every mention of "Demeter" in the note attaches a disclaimer in the same breath ("which the record says
Demeter is not," "no 2x/3x in post-crash rebounds," "the known cost of a level machine"). The note does not claim v2
reproduces Demeter's 2020 profile — it explicitly rejected the one design choice (PANIC-burst re-entry) that would
have made that claim, and the frozen v2 does not contain it. No instance of over-claiming found.

**One documentation-completeness gap (MINOR, not a mechanism defect):** the record's exact required framing —
"this rule will not reproduce Demeter's 2020" — is never stated as a single explicit sentence. The substance is
fully present but scattered across "Honest weaknesses" #4 and the stress narrative (VIX-LEVEL machine ≠ Demeter, no
2x/3x in post-crash rebounds, GFC drawdown untouched). Recommend RESULTS.md state it as one explicit sentence since
2020 itself is entirely out of the DEV window and untestable here.

## 6. Execution realism — position-change / high-volatility-day clustering

Brief's specific ask: how many DEV position changes happen on days with |return| > 2%? (DEV-only diagnostic,
`engine.load_market(end="2012-06-30")`, actual `lev` series from `signal()`):

```
Total position changes (1990-01 .. 2012-06-30): 238   (matches VERIFY.json turnover_clustering.n_changes)
Of which on |spx_ret| > 2% days:                 61   (25.6%)
Baseline share of all days with |ret| > 2%:            5.9%
  -> changes are ~4.3x overrepresented on high-volatility days
2x-entry days specifically:                        26, of which |ret|>2%:  1  (3.8% -- CALM 2x entries are NOT
                                                                                 concentrated on volatile days)
```

The candidate never uses 3x (`LEV_CALM=2.0` is the ceiling), so the brief's "3x entries at the close of high-vol
days / margin at 3x" scenario does not literally apply; the analogous risk is gap/fill risk on the more frequent 1x
ELEVATED-gate flips, which do cluster on volatile days as shown. `_VERIFY.json`'s own `turnover_clustering` metric
(top-decile-realised-vol-day share of changes) shows v2 at 15.5% vs the original's 26.5% — by that metric v2's
*added* turnover is proportionally less concentrated on extreme days than v1's own turnover was, but the *absolute*
count of high-move-day changes still roughly doubles because total turnover roughly doubles (136 → 238 changes,
6.0 → 10.6 chg/yr, DESIGN_NOTE.md point 5).

The design note quantifies the Sharpe cost of the turnover increase only under a **flat** 6bp/90bp stress row
(0.678 → 0.642, a larger drag than the original's 0.026 vs v2's 0.036 of Sharpe). It does not run or disclose the
coordinator's specified **volatility-scaled** slippage stress (`cost × max(1, RV21/15%)`), which would fall harder
on this rule specifically because its trades are disproportionately (4.3x) sited on the higher-realised-vol days
where that multiplier bites hardest. **MATERIAL: this stress should be run and its number disclosed before the
turnover-cost conclusion is trusted as complete.**

## 7. Lag-sensitivity as an execution-robustness question (not a causality verdict — that is L1's determination)

`_VERIFY.json`'s `lag_test_dev_1990` (an execution-timing stress: `lev.shift(1)`, i.e. act one session later than
decided — distinct from the causality/lookahead cut-off tests, which are a separate field and pass at all 12
cutoffs) shows:

```
                base    lag1    lag2
vix_vrp     (v1)  0.608   0.486   0.415
vix_vrp_v2  (v2)  0.678   0.422   0.431
```

v2's entire claimed advantage over the frozen original (+0.070 Sharpe, the sole basis for the retirement decision
in this pass) is not just erased but **inverted** by a one-session delay: v2's lag1 Sharpe (0.422) is *below* v1's
own lag1 Sharpe (0.486). Put plainly — if execution lands one session later than the model's decision day (a
realistic friction: order routing, the accepted ~16-minute VIX-close-vs-15:59-decision gap compounding with any
same-day fill slippage, or simply a data feed that posts VIX/RV a session late), an operator would have been better
off on the *original*, unchanged rule than on the one this pass is about to promote. This is squarely an
execution-realism finding (a strategy whose entire edge over its own predecessor requires same-day, frictionless
capture is not one a real book can rely on for that edge), independent of whatever L1 concludes about whether the
underlying cause is same-close information leakage or simply a fast-decaying effect (132 openings in 2-3 day spells,
t≈1.9, per the design note's own "Honest weaknesses" #1 — the note already flags this contribution as fragile, but
does not compute or disclose that it inverts sign against the very comparator it must beat).

**SEVERE: the retirement decision (retire vix_vrp, promote vix_vrp_v2) is not robust to a one-session
execution/implementation delay — under that stress the promoted candidate underperforms the retired one. This
should block the OOS look until the coordinator/L1/L2 jointly determine whether the base-case (same-day) result is
executable in practice, or the retirement is reconsidered.**

## 8. Minor / tooling

* `verify_tools.py`'s `module_constants` extractor is buggy on this file: its regex picks up a garbled first
  "value" ("2, LEV_PANIC = 1, LEV_ELEV_ON = 1: Demeter-style discrete ti...") pulled from the docstring rather than
  the actual `LEV_CALM = 2.0` assignment line. Independently confirmed by reading `signals/vix_vrp_v2.py` directly:
  the three constants are exactly `LEV_CALM=2.0, LEV_ELEV_ON=1.0, LEV_PANIC=1.0` as the docstring states — no
  discrepancy in the actual values, this is a tooling display bug in `verify_tools.py`, not a candidate defect.

## Summary

| # | Finding | Tag |
|---|---|---|
| 1 | Not the pass-1 trap: 79% of ELEVATED-gate openings occur while VIX is flat/rising, not falling — mechanism is genuinely VRP-based (BTZ 2009), confirmed causal and correctly cited | — (confirms candidate) |
| 2 | GFC -28.6% daily drawdown disclosure verified byte-accurate against harness output | — (confirms candidate) |
| 3 | Volatility-scaled slippage stress (cost × max(1, RV21/15%)) not run/disclosed, despite 4.3x overrepresentation of position changes on |ret|>2% days | MATERIAL |
| 4 | One-session execution delay inverts v2's advantage over v1 (lag1: 0.422 vs v1's 0.486) — the retirement decision is not delay-robust | SEVERE |
| 5 | Exact phrase "will not reproduce Demeter's 2020" not stated verbatim (substance present, scattered) | MINOR |
| 6 | `verify_tools.py` module_constants extraction bug (tooling, not candidate) | MINOR |
