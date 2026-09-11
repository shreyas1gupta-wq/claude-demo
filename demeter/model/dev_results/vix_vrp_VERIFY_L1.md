# vix_vrp — L1 verification (Causality & code), pass 2, reinstated original

Verifier: adversarial L1. Candidate: `signals/vix_vrp.py` (the ORIGINAL pass-1 file, reinstated 2026-09-12 after
`vix_vrp_v2` was refuted — PREREG.md line 88). Read in full: `signals/vix_vrp.py`, `features.py::realized_vol`,
`dev_results/vix_vrp.json`, `dev_results/vix_vrp_VERIFY.json`, `dev_results/vix_vrp_DESIGN_NOTE.md` Part 1 (lines
39-113, the pass-2 auditor's account of the original), `dev_results/vix_vrp_gridA_spec.json` /
`vix_vrp_gridB_spec.json`, relevant rows of `dev_results/vix_vrp_v2_ablation_all.csv`, `git log --follow` on the
signal file. No results/ file touched, no evaluate.py run, no data past 2012-06-30 loaded.

## 1. Lookahead in the code itself — CLEAR (no finding)

- `vix_regime()`: a strict forward `for i in range(len(v))` loop; state `st` at row `i` depends only on `v[i]` and
  the previous `st`. No `.shift(-k)`, no centered window, no indexing past `i`.
- `F.realized_vol` (`features.py:9-11`): `ret.rolling(window, min_periods=window).std(ddof=1)` — trailing only,
  `min_periods=window` means the pre-warm-up region is NaN (handled by `lev[... rv.isna()] = 0.0`), not backfilled.
- `signal()`: VRP filter and NaN-guard both use same-timestep values (`vrp`, `vix`, `rv` at row `t`); no forward
  reference. `vix.ffill()` only carries the LAST KNOWN print forward (causal), never backward.
- No use of `spx_tr` or `rf` in the file at all.
- Harness `causality_12_cutoffs` (`dev_results/vix_vrp_VERIFY.json`): `ok: true`, `max_abs_diff: 0.0` across all 12
  truncation cut-offs (1992-03-31 .. matches the file's own `lookahead_check` of 5 cut-offs, also 0.0). **Confirmed
  clean** — this file is mechanically as causal as any candidate in the panel.
- VIX close-timing (16:15 vs the 15:59 decision): disclosed in the docstring and in Part 1 of the design note as an
  accepted, literature-standard approximation. Not flagging this on its own (per brief, only if the rule is shown
  sensitive to it) — but see §3 below, the lag test **is** evidence of exactly that sensitivity, so it should not be
  waved off with "the whole literature does the same."

## 2. Lag-1 sensitivity — MATERIAL

`dev_results/vix_vrp_VERIFY.json::lag_test_dev_1990`: Sharpe 0.6084 (base) → 0.4862 (lag1, −20.1%) → 0.4153 (lag2,
−31.7%). Max drawdown also worsens with lag: −19.78% → −28.31% → −32.50%. This is not a causality defect (the
causality battery is clean; lag-testing measures execution-timing fragility, not information leakage), but a
one-session implementation delay costs a fifth of the Sharpe and blows the monthly-DD budget from comfortably inside
the −20.5% acceptance bar to outside it. Combined with the VIX 16:15-vs-15:59 approximation the docstring dismisses
as immaterial, this is inconsistent: a rule this sensitive to a *full session* of delay should not casually dismiss a
16-minute timing gap without a quantified check (that specific quantification is L3's brief, not repeated here, but
the docstring's blanket dismissal is not supported by this file's own lag numbers).
**MATERIAL: disclose the lag-1/lag-2 Sharpe decay and monthly-DD breach in RESULTS.md; do not carry forward the
docstring's claim that the 16-minute VIX timing gap is immaterial without a quantified check.**

## 3. True tunable count — SEVERE (G7 breach on the balance of evidence)

`DEFAULT_PARAMS` = 5 (`v_calm, v_panic, hyst, rv_win, vrp_min`), matching the `signal()` signature exactly — no
hidden tunable is smuggled in outside `DEFAULT_PARAMS` (checked the function body for stray literals: none found;
`/100.0` is a units conversion, the `max(round(rv_win),2)` floor is input hygiene, not a free parameter).

The docstring (lines 49-52) asserts: *"Leverage tiers are structural constants (Demeter-style discrete steps), not
tunables."* — `LEV_CALM=2.0, LEV_ELEV=0.0, LEV_PANIC=1.0`. Per the brief's own test ("a constant whose value was
chosen by comparing DEV results IS a tuned parameter"), this claim needed to be checked against a pass-1 design
note. **There is none** — the coordinator confirms this, `dev_results/vix_vrp_VERIFY.json::grid_audit` returns
`{"error": "no vix_vrp_grid.csv"}`, and grids A/B (`vix_vrp_gridA_spec.json`, `vix_vrp_gridB_spec.json`) — the only
DEV-parameter sweeps that exist for this file — **never vary the leverage constants at all**, only `v_calm, v_panic,
hyst, rv_win, vrp_min`. So there is no pass-1 OR pass-2 grid evidence bearing on how `{2.0, 0.0, 1.0}` were chosen.

What we do have is the docstring's own "Why these rules" paragraph (lines 20-27), which is the ONLY account of
process for this file and is two lines above the "structural, not tunable" claim it contradicts:
*"Conditional sorts of next-day excess returns on the development sample show three volatility regimes: calm VIX
(12-18): Sharpe ~0.5-0.6 ... (leverage pays); elevated VIX (18-30): Sharpe ~0 (cash); panic VIX (>30): Sharpe 0.8-1.2
... (unlevered participation) ... Parameters were chosen on the development window for Sharpe, drawdown and trade
count (plateaus, not peaks)."* This is a description, in the designer's own words, of picking the regime→leverage
mapping from a DEV-sample conditional-Sharpe table — the same kind of process that got `composite_dual_engine`
(LEV_REB, 3x/2x/1x comparison → 7 tunables), `dissipation_reentry` (flat-1x vs tier comparison → 7 tunables),
`volmanaged` (POWER/EST/DISCRETE/WEEKLY → 9 tunables) and `vix_vrp_v2` itself (LEV_CALM 2-vs-3, LEV_PANIC 1-vs-2 → 8
tunables) all REFUTED at L1 in this same pass. `LEV_ELEV=0` ("cash") and `LEV_PANIC=1` ("unlevered participation")
are close to definitional given those labels, but `LEV_CALM=2` is not — "leverage pays" does not by itself fix the
multiplier at 2x rather than 1.5x or 3x, and nothing in the file or its design-note audit shows that choice being
made any other way than the DEV conditional-sort table the docstring describes.

Two pieces of pass-2 evidence exist but **do not resolve this**, and the coordinator is right to flag them as
post-hoc: `dev_results/vix_vrp_v2_ablation_all.csv` rows `V1_calm3x` (3x calm: Sharpe 0.608→0.548, maxDD
−19.8%→−27.8% — worse) and `V0c_panic2` (2x panic: Sharpe ~flat 0.608→0.607, but maxDD −19.8%→−41.9%, daily DD
−54.4% — a G4 drawdown-bar breach) were run by the pass-2 designer AFTER the original was frozen, to audit it, not
by whoever froze it in pass 1. They show the frozen values are *DEV-superior to the tested alternatives* — which
argues the leverage constants are hard to improve on, not that they were chosen a priori without looking.

**Verdict:** with no pass-1 design note, the "structural, not tunable" claim cannot be verified, and the one
document that speaks to process (the docstring itself) describes exactly the DEV-comparison mechanism the study
treats as tuning everywhere else it appears. Per the brief's instruction to default to refuted under ambiguity, and
for parity with every other candidate refuted this pass on the identical leverage-tier issue, **report the true
tunable count as 5 declared + 3 leverage constants of undocumented provenance = 8, and treat this as a G7 breach
(budget is 6), not merely a disclosure gap.** `gate_check.py` will show this candidate passing G7 because it only
counts `DEFAULT_PARAMS` (5) — a known harness limitation (PREREG.md "Two harness limitations") — the mechanical pass
is not evidence of compliance. Unlike `sticky_tier`, whose FLOOR constant survived because a design note
affirmatively documented "chosen on DEV — at the ceiling, not over," this file has no equivalent document to earn
the same benefit of the doubt.

**SEVERE — blocks the OOS look.**

## 4. Undisclosed prior OOS look — SEVERE (independent of §3)

The docstring's final sentence (line 27): *"the OOS window 2012-07..2026-02 was looked at only through the final
evaluate.py runs."* This is an affirmative claim, in the file's own text, that `evaluate.py` was run against the
out-of-sample window for this candidate at least once, historically. Yet:

- `PREREG.md` line 18 describes `signals/vix_vrp.py` as "found in the repo **with no results file and no mention in
  RESULTS.md**" and line 17 calls it "pre-existing but **never-evaluated**."
- No `results/vix_vrp*.json` exists (per the coordinator and PREREG's own disclosure — not independently re-checked
  here per the brief's "never touch results/").
- `git log --follow -- signals/vix_vrp.py` shows exactly **one** commit for this file (`5a7cefe`, the bulk
  "Add replication study" commit that introduced the whole demeter/model tree) — version control carries no
  evidence either way about what happened before that squash, so it cannot corroborate or refute the docstring's
  claim.

This is a direct contradiction between the file's own account of its history and the pre-registration's
characterization of it. Both readings are bad: (a) if the docstring's "looked at ... through final evaluate.py
runs" sentence is accurate, an out-of-sample look already happened for this exact candidate before pass 2 ever
started, and PREREG's "never-evaluated" is wrong — meaning re-running the pre-registered "single look" on this
candidate would not actually be its first look, silently breaching the study's central "a look cannot be un-taken"
rule (PREREG.md line 100); (b) if the docstring's claim is inaccurate — e.g. copied boilerplate from a template
rather than a description of what was actually done to *this* file — then the other process claims in the same
docstring ("Parameters were chosen on the development window for Sharpe, drawdown and trade count (plateaus, not
peaks)") are equally unverified narrative, not a documented record, which independently weakens the §3 "structural
constant" defense. Either way, **this cannot be resolved from the artifacts available to a DEV-only verifier**, and
per the brief's default-to-refute standard, an unresolvable doubt about whether the OOS window has already been
looked at is disqualifying on its own.

**SEVERE — blocks the OOS look; state plainly to the Principal that pass 1 may have looked at OOS once without
recording it, and that this cannot be ruled out from the current repo state.**

## 5. Minor

- The docstring's structural-vs-tuned framing is internally inconsistent even setting aside evidence: line 49-52
  calls the leverage tiers "structural constants ... not tunables," while line 26 says "Parameters were chosen on
  the development window for Sharpe, drawdown and trade count" without excluding the leverage tiers from
  "parameters." A future version of this file (if it survives) should use disjoint, unambiguous language for the
  two categories, the way `sticky_tier`'s note reportedly does.
- `module_constants` in `vix_vrp_VERIFY.json` lists only `LEV_CALM/LEV_ELEV/LEV_PANIC` as UPPER_CASE constants —
  confirms there are no other hidden constants in the file beyond the three under dispute.

## Summary

| # | finding | severity |
|---|---|---|
| 1 | Lookahead / causality (code read + 12-cutoff battery) | clear, no finding |
| 2 | Lag-1 Sharpe decay (0.608→0.486→0.415) and monthly-DD breach under 1-session delay; docstring dismisses the smaller 16-min VIX timing gap without a matching check | MATERIAL |
| 3 | True tunable count 5 declared + 3 leverage constants of undocumented provenance = 8 > budget of 6; no pass-1 design note or grid exists to support "structural"; the docstring's own mechanism paragraph describes DEV-conditional-Sharpe selection of the regime→leverage mapping, the same pattern that refuted 4 other candidates this pass | **SEVERE** |
| 4 | Docstring claims OOS was "looked at ... through the final evaluate.py runs" while PREREG calls the file "never-evaluated" with no results file anywhere — unresolvable contradiction, cannot rule out an unrecorded prior OOS look | **SEVERE** |
| 5 | Internal wording inconsistency in the docstring (parameters vs structural constants) | minor |

**refuted = true (2 SEVERE findings).**
