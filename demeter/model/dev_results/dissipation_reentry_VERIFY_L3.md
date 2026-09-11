# L3 verification — dissipation_reentry (Mechanism & execution)

Verifier: adversarial L3, pass 2. Read in full: `signals/dissipation_reentry.py`, `dev_results/dissipation_reentry_DESIGN_NOTE.md`,
`dev_results/dissipation_reentry.json` (fields only, via script), `dev_results/dissipation_reentry_VERIFY.json`,
`dev_results/dissipation_reentry_bursts_frozen.csv`. One confirmatory `dev_harness.py --params '{"vix_min":999}' --tag
verify_L3_noburst --no-plateau` run (REBOUND ablation, DEV only, file banked at
`dev_results/dissipation_reentry_verify_L3_noburst.json`). No signal file edited, no parameters proposed, `evaluate.py`
and `results/` untouched.

## 1. Coordinator question: is the burst P&L tracker causal? — RESOLVED, no bug

`engine.run()` sets `pos = lev.shift(1)` (position in effect on day t = signal decided at close t-1). Inside
`signal()`, the loop variable `state` entering iteration `i` is exactly the state decided at the end of iteration
`i-1` — i.e. it equals `lev[i-1]`, the value that becomes `pos[i]` under the harness's own shift convention. The line
`cum *= 1.0 + LEV_REBOUND * x_ex[i]` (evaluated only `if state == 2` at loop entry) therefore applies day `i`'s
already-realised excess return to the position that the harness will apply on day `i` — not to a position not yet
decided. The exit decision computed later in the same iteration (`stopped`, `held>=hold_days`, `dbl[i]`) uses only
day-`i` information and sets `state` for `out[i]`, which the harness applies to day `i+1`. This is internally
consistent and matches `_VERIFY.json`'s `causality_12_cutoffs` (`max_abs_diff: 0.0`, `ok: True` at all 12 dates,
1987 crash and 2002/2008/2009 events included) and the lag test (`lag_test_dev_1990`: Sharpe *rises* under +1/+2
session delay, 0.447→0.526→0.473 — the opposite of what a lookahead artifact would show). **No finding.**

## 2. Mechanism: is it a real, pre-stated mechanism, and is it what actually drives the result? — MATERIAL

The design note's Mechanism section (written 2026-09-04, before any run) states a specific, falsifiable hypothesis
(implied-vol puts in its high before price does at a genuine capitulation low) and pre-registers five failure modes.
The final rule matches that hypothesis (VIX off a trailing peak but still an absolute extreme, RSI(2)<20 — not "VIX
below its SMA," not a trend-recovery condition). Verified against `spurious_reentry_census`: the divergence condition
cuts the pass-1 trap's 2000-02 / 2007-09 spurious entries from 26/14 to 2/2 and flips the mean forward-10-day return
from -2.3%/-3.2% to +0.62%/-0.05% — a real, quantified improvement, not merely asserted. **This part is sound.**

However, the mechanism is *not* what makes the candidate pass its gates. I reran the frozen params with
`vix_min=999` (REBOUND structurally disabled, no signal-file edit) and reproduced the design note's ablation exactly:
dev_1990 Sharpe **0.39** (note: 0.389), maxDD **-8.0%** (note: -8.0%) — **fails G2** (bar 0.4253). The seven divergence
bursts (7 fires in 22.5 years) supply the entire +0.058 Sharpe / +1.7% CAGR that lifts the candidate over G2; the
gate-passing engine underneath is `LEV_TIER=(1,1,1)` triggered by `rv > rv_exit` — a realised-vol **LEVEL** gate, the
exact ingredient the inference note (`DESIGN_BRIEF.md` "What the record says") rules out for reproducing Demeter's
2020 behaviour. The design note discloses this itself, extensively and accurately (Answer-to-lens-question §4,
weaknesses #1 and #3) — I did not find it hidden or misstated anywhere, but it is a fact about the candidate's
economics material enough that it belongs in the aggregated report, not only in the working note.

## 3. Required label: "will not reproduce Demeter's 2020" — present, verified

Weakness #1 quotes the inference note directly ("`RV21<15%` gates earn ~0% in Mar/Apr-2020") and weakness #5 walks
the actual 2020 timeline through the frozen rule: Feb-2020 held at 1x until RV21 crosses 15% (~27-Feb, i.e. after
the crash starts), the 23-Mar low itself *would* fire (VIX 61.6 vs 82.7 peak = 0.745, RSI2 8, satisfies the trigger),
but Apr-2020 is "at most one more burst then cash — nothing like the record's 14 of 21 days at 3x." This is exactly
the disclosure the brief requires for a candidate that uses a vol-level gate as its invest/cash decision. **No
finding — label present and accurate.**

## 4. Execution realism: entries on already-large-move days — MATERIAL (new, quantified)

`_VERIFY.json`'s `turnover_clustering` reports position changes on "top-decile realised-vol days" at 10.3% vs a 10%
base rate — i.e. it reads as unremarkable. That proxy is too coarse to see what is actually happening. I recomputed
turnover against `|spx_ret| > 2%` directly (script, dev_1990, frozen params):

* 87 total position changes; **26 of 87 (30%) land on days with |return| > 2%**, against an 8.0% base rate for such
  days over the same window — a **3.7x concentration**, not the ~1x the coarser proxy suggested.
* Of the 7 REBOUND entries specifically: 5 of 7 fire on a day where SPX itself already moved > 2% that same day
  (entry-day returns: -2.60%, -2.19%, -3.09%, -2.55%, and -2.14% for the five; the other two are -1.55% and -1.23%).
  Median burst-entry-day return ≈ -2.4%.
* This is mechanically partly by design (the double-shock STRESS trigger requires a ≥2-sigma down day, so some
  clustering is intentional and causally fine), but the REBOUND *entries* — the 3x notional swings, not the 1x/0x
  DEFAULT↔STRESS ones — are the leg where the flat 3bp/unit cost assumption is least realistic: a levered entry at
  the close of a day already down 2-3% is exactly the closing-print/wide-spread environment the PREREG's clustered-
  slippage stress exists to price in.

## 5. Clustered-slippage stress (PREREG item 2) not yet run on this candidate — MATERIAL, tested and found small

Every one of the 7 burst entries AND all 7 exits occurs while RV21 is elevated (20.0%-62.7% at entry, avg ≈35%;
20.1%-34.0% at exit): under the pre-registered `cost_bps × max(1, RV21/15%)` stress this is a **1.3x-4.2x** cost
multiplier on literally 100% of the candidate's REBOUND-related trades (14/14 events) — none of the design note's
three cost rows (2/40, 3/60, 6/90) is this vol-scaled stress; all three are flat bumps. I built a standalone script
mirroring `engine.run()`'s formula (not touching `evaluate.py`/`results/`) to approximate the effect at 3bp/60bp:
dev_1990 CAGR 7.86%→7.79%, informal daily-return Sharpe 0.771→0.764 — a ≈5-7bp/yr drag. The multiplier is large per
event but the aggregate notional touched on 14 days out of ~5,660 is small, so **on this evidence the effect is
immaterial to G2** (0.447 baseline has a 0.022 buffer over the 0.4253 bar; a ~1% relative Sharpe hit does not close
that gap, let alone the thinner 0.0072 buffer already surviving the flat 6/90 row). This is an approximation outside
the audited harness path, not a substitute for actually running the stress through the pipeline — flagged as a
required disclosure that the specific pre-registered clustered-slippage stress has not yet been applied to this
candidate, with the caveat that my own check does not find it dangerous.

## 6. VIX level at actual DEV entries vs. the "VIX-60 day" question — MINOR / clarifying

No DEV burst enters above VIX 44.9 (2008-12-19); the seven entries run 31.3-44.9. The "3x burst at the close of a
VIX-60 day" scenario the coordinator asks about has **no DEV precedent to test against** — it is precisely the
2020 profile the mechanism is designed to fire on (§3 above) but which DEV never produced. Whether such an entry is
executable (procyclical margin at extreme vol, LULD-halt-widened closing spreads, ETF/futures replication stress on
the worst days of a crash) is a real question the linear-bps engine cannot answer either way, for this candidate or
any other in the panel — it is not a defect unique to `dissipation_reentry`, but this candidate is the only one in
the panel whose trigger is explicitly built to fire in that exact regime, so the caveat is material specifically here
and is only partially covered by the design note's existing weaknesses #4/#6 (gap risk on the close-to-close stop,
"-20% day is -60% of burst equity before it can act"). Recommend it be named explicitly as an open, untested question
if this candidate reaches OOS.

## 7. "Strategy in its own right" vs. over-claiming resemblance to Demeter — no finding

The design note does not over-claim: it states plainly the model is "a low-beta (0.34) defensive strategy... not the
record's 114% up-capture / 2x levered profile," misses the 2009 recovery entirely (+0.5% vs SPY +67.4%, confirmed in
`stress_episodes`), and undershoots the record's up-capture/leverage/worst-month targets outright while meeting the
cash-share target "by accident of the gate." This matches the numbers in `dev_results/dissipation_reentry.json`
(up-capture 52%, down-capture 33%, beta 0.34, avg leverage 0.50). **No finding — appropriately modest.**

## 8. Named breaking regimes — present, satisfies the brief

Historical DEV regime: Oct-2008→Mar-2009 (VIX successive higher highs on price lower lows; the divergence condition
cannot see it until the Dec-08/Jan-09 lull, and the note shows the exact -47%/-69% failure mode this would produce
at a looser `vix_fall`). Plausible future regime: a one-day 1987-style crash landing inside an already-live 3x burst
(unhedged — the stop is close-to-close, "a -20% day is -60% of burst equity before it can act"; the note notes DEV
got lucky no burst was live in Oct-1987). Both satisfy the brief's ask for one historical and one forward-looking
regime that would break the rule.

## Summary

No SEVERE finding. The mechanism is genuine, pre-stated, and demonstrably different from the pass-1 trap by the
census numbers; the causality of the burst P&L tracker is correct; the required "will not reproduce 2020" label is
present and specific. The material issues are about what is *actually* driving gate-passage (a disclosed but
consequential vol-level-gate dependency) and about execution realism on the specific days the burst mechanism
touches (elevated-RV entries/exits, large-move-day clustering, and an untested VIX-60 entry scenario) — all
individually small in DEV terms but worth carrying into `RESULTS.md` verbatim rather than only in the working note.
