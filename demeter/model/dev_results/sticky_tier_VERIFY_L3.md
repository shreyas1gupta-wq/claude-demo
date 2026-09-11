# sticky_tier — L3 verification (Mechanism & execution)

Verifier: L3, pass 2, Demeter dual-engine study. Scope per VERIFY_BRIEF.md: real mechanism vs. what the rule
actually does, pass-1-trap check, regime that breaks it, execution realism (crash-day entries, clustered slippage),
"strategy in its own right" vs. over-claiming Demeter, and the record's ruled-out mechanisms. All numbers below were
re-derived independently from `dev_results/sticky_tier.json`, `_VERIFY.json`, `_diag3.txt` and a fresh run of
`signal()` — not copied from the design note without a check — except where marked "(design note, verified)".

## 1. Mechanism stated vs. mechanism realised — MATERIAL

The docstring/design note hypothesis (Moreira-Muir): lever up in calm vol regimes, cut in high-vol regimes, "hold
2-3x through whole calm years." The design note's own "Post-run comparison with prediction" admits this did not
happen. Independently confirmed from `dev_results/sticky_tier.json.windows.dev_1990`: `pct_days_cash=66.66`,
`avg_leverage=0.392`, `avg_leverage_when_invested=1.177`, and `leverage_distribution_dev_1990` shows `3.0: 0%` (3x
never held in 1990-2012; full-1950 history shows 3x only in 1964-66). The rule is empirically a binary
vol-LEVEL cash/1x-mostly filter, not a levered vol-timing strategy. Re-derived the position-change ledger
(`signal()` diffed over dev_1990): exactly 10 changes, and the entire dev_1990 Sharpe advantage over SPY traces to
two mechanical exits — 1997-03-31 (pre-LTCM, cash for 8 years to 2005-02-07) and 2007-08-06 (pre-GFC, cash through
DEV end) — each of which happened to land 3-30 months ahead of a major drawdown. Ten decisions across 22.5 years is
not a sample from which a repeatable "vol regime carries the leverage decision" mechanism can be inferred; the
design note's own weakness #2 says the same thing, which is the correct characterisation and must not be dropped
when this is summarised for RESULTS.md.

## 2. Not the pass-1 trap — verified, not merely asserted

Brief's trap definition: "buys after implied vol has just fallen, in any form." Checked against the repo's actual
pass-1 casualty, `vix_dissipation` (DESIGN_BRIEF.md dev_1990 Sharpe -0.31, maxDD -93.5%, 46.6 chg/yr — a single-day
implied-vol-drop entry). sticky_tier differs on every axis that matters: (i) realised vol, not VIX/implied; (ii) an
UP move requires `T(sigma) > c` to hold for `P=5` consecutive sessions *and* the first ISO-week session *and*
`M_COOL=10` sessions since the last change — not a single-print trigger; (iii) independently confirmed from the
position-change ledger and `spurious_reentry_census` (`n_entries_to_2x_plus: 0` for both 2000-02 and 2007-09) that
there are literally **zero** position changes of any kind between 1997-03-31→2005-02-07 and 2007-08-06→2012-06-29 —
the rule never re-enters on a vol dip inside either bear. This is a genuine, code-and-data-verified distinction from
the trap, not a claim taken on the designer's word.

## 3. Regime that breaks it — requirement met

Design note §6 names both a historical DEV regime (2009-2012, and separately the 1962 sub-14%-vol air-pocket at
2x/1x) and a prospective one (a high-vol bull/melt-up-on-rising-vol regime, where the mean/variance-ratio premise
inverts). Independently corroborated: `subsamples.thirds[1]` (1997-07-01..2004-12-31) in `_VERIFY.json` has
`changes_per_year: 0.0`, `sharpe: NaN` — the rule is provably inert for that entire third, consistent with the
"high-vol bull it sits out" failure mode named in the note. Requirement satisfied.

## 4. Vol-LEVEL gating is a mechanism the record rules out — MATERIAL, must be disclosed

DESIGN_BRIEF.md "Ruled out by the record" explicitly lists vol-LEVEL gating as the invest/cash decision. sticky_tier
is exactly this (its only regime variable is trailing EWMA vol level vs. fixed boundaries). This is allowed for a
stand-alone strategy per the brief, conditional on being labelled as "will not reproduce Demeter's 2020." The design
note does label it (weakness #5: "this rule does the opposite of what the record shows in Mar/Apr-2020... a known,
pre-declared failure mode of vol-LEVEL gating, which the record rules out"). Confirmed this label is accurate: the
record's ingredient list requires "leverage ... highest" exactly in "crisis-rebound months" (DESIGN_BRIEF.md line
106), while sticky_tier's mechanism structurally cannot re-lever until the slow (160-session) EWMA leg falls below
14% — which independently verified took until 2005-02-07 after the 2000-02 bear and never happened at all before
DEV end after 2007-08-06. Correctly disclosed by the designer; carry forward into RESULTS.md as its own line item,
not folded into the general "regime filter" framing, because the two failure modes (missed rebounds vs. never
levering in calm years) are mechanically distinct and both need to survive to the report.

## 5. T-bill accounting dependency — MATERIAL, verified independently

Re-derived from `dev_results/sticky_tier_diag3.txt` line 126 (`frozen 7.38 5.31 ...`): CAGR is 7.38% headline vs.
5.31% with T-bill zeroed on cash days (`rz = ret - rf.where(lev==0, 0)`), i.e. 2.07 of 7.38 CAGR points (28%) are
risk-free interest earned on the 66.7% cash-day share. Cross-checked against `volmanaged` on the same line (7.39 vs.
7.39, unchanged, because it is never in cash) — confirms the effect is real and specific to sticky_tier's cash
share, not a script artefact. Demeter's own accounting books cash at 0%. On that convention sticky_tier's CAGR
(5.3%) falls below both SPY buy-and-hold (8.3%) and the in-lens bar volmanaged (7.4%) — a Sharpe-only OOS comparison
would overstate this candidate's edge relative to Demeter unless the accounting convention is matched or disclosed.

## 6. Execution realism — verified independently, no SEVERE finding

Re-ran the frozen signal and joined the 10 dev_1990 position-change dates to trailing 21-day realised vol and same-
day return:

| date | lev before→after | day return | RV21 (ann.) | cost-stress mult. max(1, RV21/15%) |
|---|---|---|---|---|
| 1992-03-30 | 0→1 | -0.12% | 7.4% | 1.00 |
| 1993-12-20 | 1→2 | +0.13% | 5.7% | 1.00 |
| 1994-04-05 | 2→1 | +2.06% | 14.6% | 1.00 |
| 1994-09-12 | 1→2 | -0.30% | 9.1% | 1.00 |
| 1994-11-01 | 2→1 | -1.12% | 13.3% | 1.00 |
| 1995-04-03 | 1→2 | +0.25% | 8.8% | 1.00 |
| 1996-02-22 | 2→1 | +1.58% | 11.9% | 1.00 |
| 1997-03-31 | 1→0 | -2.11% | 17.6% | 1.17 |
| 2005-02-07 | 0→1 | -0.13% | 9.4% | 1.00 |
| 2007-08-06 | 1→0 | +1.68% | 20.1% | 1.34 |

8 of 10 changes carry no cost stress at all; the only two with any stress multiplier are the two DE-levering exits
that preceded the two bears, at modest 1.17x/1.34x — nowhere near the "3x entered at the close of a high-vol day"
failure the brief asks about (3x is never entered in dev_1990 at all). Cross-checked against `_VERIFY.json`
`turnover_clustering`: `share_of_changes_in_top_decile_vol_days: 0.0` of 10 — independently reproduces the same
conclusion via a different metric (top-decile trailing RV rather than same-day return). `event_ladders` and the
design note's stress narrative are also confirmed: the rule holds cash (L0) through every listed crash date
(2008-10-10, 2008-11-20, 2009-03-09, 2002-10-09, 1987-10-19) with zero position changes inside those windows, so
there is no clustered-slippage or margin-call exposure to stress-test. **No SEVERE execution-realism issue.**

One genuine cost of stickiness, already disclosed and independently confirmed: the 1962 episode
(2x from 1961-01-23 → 1x on 1962-05-15 at 12.5% vol → 0x only on 1962-05-28, a -6.68% day, at 22.8% vol) took two
sessions to fully de-lever from 2x because `T_h(sigma)` only crossed one boundary on 5/15; the code correctly jumps
straight to `T_h`'s rank each session (verified in `_core`, lines 129-133 of `signals/sticky_tier.py`) rather than
stepping down one tier at a time — this matches the documented rule, is not a bug, and is the one place in the
whole DEV history where a change lands on an acute (>6%) down day, consistent with `P_DN=1` (de-levering acts on
the first day the DOWN condition holds; the two-session delay is inherent in how far vol still had to rise, not an
implementation defect).

## 7. "Strategy in its own right" vs. over-claiming Demeter — no issue found

The design note does not over-claim resemblance to Demeter; if anything it is unusually self-critical (its own
"Honest weaknesses" section explicitly says "the long-window risk-adjusted case is not made" over 1950-2012, Sharpe
0.35 vs. buy-and-hold's 0.47). `RESULTS.md` does not yet mention `sticky_tier` (checked), so there is no existing
overclaim in the report to flag. No SEVERE or MATERIAL finding here.

## 8. Cross-lens notes (not scored under L3, flagged for coordinator/L1/L2)

* L1's remit: `FLOOR=0` was chosen by directly comparing DEV grid-A results (192 floor=1 combos, all fail G3) —
  by the brief's own test ("a constant whose value was chosen by comparing DEV results IS a tuned parameter") this
  is arguably not purely theory-given/structural. Flagging for L1's tunable-count audit, not scoring it here since
  L3's brief does not own the tunable-budget check.
* L1's remit, spot-checked while reading the file for L3 purposes: the weekly re-levering gate
  (`wk.ne(wk.shift(1))` on `df.index.isocalendar().week`) is causal — compares only the current row's ISO week to
  the immediately preceding row's, never a forward-looking calendar rule. No lookahead found in this mechanism.
* L2's remit: subsample halves (0.79 vs. 0.36 Sharpe) and the all-cash NaN-Sharpe middle third are confirmed
  numerically here (§1, §3) because they bear directly on mechanism-consistency, but the overfit/plateau
  interpretation of these numbers is L2's to make.

## Verdict

No SEVERE finding: the mechanism, while not the one predicted, is faithfully described post-hoc by the designer;
execution is clean (no crash-day or high-vol entries, negligible cost stress); the pass-1 trap is verifiably absent;
the ruled-out mechanism (vol-LEVEL gating) is used but correctly labelled. Four MATERIAL findings (mechanism realised
≠ mechanism hypothesised / small-n; vol-LEVEL gating disclosure must survive to RESULTS.md; T-bill accounting
dependency; near-total inactivity across a third of the DEV sample) must be carried into RESULTS.md as disclosures
if this candidate proceeds to the OOS look.
