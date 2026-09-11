# composite_dual_engine — L3 verification (Mechanism & execution)

Verifier: adversarial L3, pass 2. Scope: is there a real, pre-stated mechanism consistent with the code; does the
rule reproduce known trap patterns; execution realism of 3x entries; consistency/labelling against what the
Demeter record rules out. DEV window only (`dev_harness.py` truncation, data ≤ 2012-06-30). No `evaluate.py` run,
no `results/` touched, no signal file edited, no new parameters proposed.

All numbers below were independently recomputed from `signals/composite_dual_engine.py` + `engine.load_market` +
`features.py` on `dev_1990` (1990-01-01..2012-06-30), not copied from the design note, unless marked "(design
note, corroborated)".

## 1. Mechanism is real and pre-stated — CONFIRMED, no defect

The design note's "Mechanism" section is explicitly dated before the first run and is consistent with what the
code does: `vix_regime()` implements the 3x/1x/cash tier exactly as documented (verified line-by-line against the
docstring's threshold arithmetic: CALM enter 16×(1-0.16)=13.44, STRESSED enter 23.0, STRESSED exit 23×0.84=19.32 —
all reproduced independently). No mismatch between prose and code found. **No finding.**

## 2. Is the re-entry "the pass-1 trap in disguise"? — TESTED, mechanism is genuinely different, not a defect

The panel's known trap (`vix_dissipation`, DEV Sharpe −0.31, maxDD −93.5%, 46.6 chg/yr — `DESIGN_BRIEF.md` L91)
is exactly "buy after implied vol has fallen." The composite's ingredient 2 is structurally the same family
(fires on VIX dissipation from a trailing peak), so this needed independent testing rather than taking the design
note's census at face value.

Re-implemented the state machine directly (not just read the design note) and traced every REBOUND entry over
the full `dev_1990` window, not only inside the two census windows:

```
total REBOUND (burst) entries in 22 years: 6
2001-10-29  VIX 31.6  30d-max 43.7  RSI(2) 15.3  fwd-10d underlying +4.26%
2002-08-28  VIX 33.3  30d-max 45.1  RSI(2)  9.1  fwd-10d underlying -2.88%
2002-11-11  VIX 31.3  30d-max 42.6  RSI(2)  9.1  fwd-10d underlying +5.91%
2008-12-19  VIX 44.9  30d-max 80.9  RSI(2) 19.7  fwd-10d underlying +5.99%
2010-06-29  VIX 34.1  30d-max 45.8  RSI(2)  3.0  fwd-10d underlying +5.22%
2011-09-02  VIX 33.9  30d-max 48.0  RSI(2) 11.1  fwd-10d underlying +2.62%
```
6 entries in 22 years vs. the trap's 46.6/year — four orders of magnitude fewer firings — and 5 of 6 forward
windows positive. The design note's "3 firings in the two grinding bears, 1 negative" (census table) checks out
exactly against this full trace (2001-10-29, 2002-08-28 in the first window; 2008-12-19 in the second — the other
three, 2002-11-11 / 2010-06-29 / 2011-09-02, correctly fall outside the census's bear-window definition per
`PREREG`/`DESIGN_BRIEF`'s own `spurious_reentry_census` spec, so their exclusion from that table is not a
mis-statement). The triple conjunction (VIX still ≥30 AND price still making a fresh 2-day low AND VIX already
off its peak) is what prevents this from behaving like the naive trap — confirmed empirically, not just asserted.
**No finding; the design note's differentiation from the trap is real and independently reproduced.**

## 3. Vol-LEVEL gating as the ordinary invest/cash decision — MATERIAL, undisclosed as required by the brief

`DESIGN_BRIEF.md` ("What the record says") states plainly: **"Ruled out by the record: ... vol-LEVEL gating"** —
i.e. Demeter's own trading record shows it was NOT decided by an implied-vol level threshold (it stayed invested
through Mar/Apr-2020 and Jul/Oct/Nov-2022 despite conditions that would flip a level gate to cash).

The composite's ORDINARY TIER is, mechanically, exactly a vol-LEVEL gate: `STRESSED` (VIX > 23, exit at VIX <
19.32) → 0x is the sole invest/cash decision whenever the book is not in OUT or REBOUND mode, and it is the mode
the book spends the most time in (42.2% of all `dev_1990` days are cash, almost entirely via this path — the 2009
event ladder is a clean illustration: 207/207 days of the 2009 recovery are cash purely because VIX's minimum,
19.47, sat 0.15 points above the STRESSED exit level 19.32; independently reproduced above). This is precisely
the mechanism the record rules out as Demeter's own invest/cash logic.

The VERIFY_BRIEF requires: *"allowed for a stand-alone strategy, but it must be labelled as 'will not reproduce
Demeter's 2020', check that the note does."* It does not. Searching the full design note for "2020", "vol-level",
"VIX level" as a ruled-out mechanism, or any explicit "this will not reproduce Demeter's 2020" statement returns
nothing — the note cites 2020 only as *motivating* the shock-exit and re-entry ingredients (the Feb-2020 and
23-Mar-2020 patterns), never as a place where its own ordinary-tier mechanism should be expected to diverge from
what Demeter actually did. The note is otherwise unusually candid about mismatches (down/up-capture, the 2009
miss, era-concentration of 3x), which makes this specific, brief-mandated disclosure's absence more notable, not
less.

Concretely, extending the 2009 finding forward: if a Mar/Apr-2020-shaped event recurs (VIX spends weeks above 23,
punctuated by brief drops that do not both clear 19.32 on the tier AND satisfy the strict triple-conjunction
re-entry), the model's ordinary tier — not a transient burst — will hold it in cash for the bulk of the recovery,
by construction, the same way it held it in cash for all 207 days of 2009. This is a legitimate, disclosable
consequence of the frozen mechanism and not a code defect.

**MATERIAL — required disclosure**: the design note must state that the ordinary tier's cash/invest decision is a
VIX-level gate, a mechanism the Demeter record explicitly rules out, and that the model should therefore not be
expected to reproduce Demeter's actual 2020/2022 behaviour even though it uses record-derived ingredients
elsewhere (shock exit, dissipation re-entry).

## 4. Execution realism — 3x entries at the close of high-vol days — MATERIAL, quantified, not previously disclosed this way

Brief: *"how many of the DEV position changes happen on days with |return| > 2%?"* Independently computed over
`dev_1990` (121 total leverage changes, matching the gate report's 5.46 chg/yr):

* **18 of 121 changes (14.9%) occur on days with |spx_ret| > 2%**, vs. a base rate of 8.0% of all `dev_1990` days
  having |return| > 2% — position changes are ~1.9x overrepresented on big-move days (expected, since the shock
  exit is designed to react to exactly such days: of the 18, 13 are de-levering, only 5 are levering-up).
* `_VERIFY.json.turnover_clustering` reports a *different*, milder metric (share of changes in the top realised-vol
  *decile* of days = 6.6% vs. a 10% base rate — i.e. changes are *not* concentrated in high-RV-decile days on that
  measure). The two metrics disagree in direction because they measure different things (single-day return
  magnitude vs. trailing realised-vol decile); citing only the VERIFY.json figure would understate the risk the
  brief is asking about. **Use the |return|>2% figure (14.9%), not the RV-decile figure, when this candidate's
  execution realism is written up.**

More important than the aggregate: **all 6 REBOUND (burst) entries are direct 0x → 3x single-session jumps**
(traced above; e.g. 2001-10-26 lev=0.0 → 2001-10-29 lev=3.0), decided at the close of a day where VIX is still
≥ 30 by construction. Trailing 21-day realised vol (annualised) at these six entries: **20.0%, 33.5%, 28.7%,
62.7%, 26.0%, 45.5%** — every single one is above the coordinator's 15% clustered-slippage reference, four of six
above 2x it, and the Dec-2008 entry is at 4.2x. Applying the coordinator's stated stress `cost × max(1, RV21/15%)`
to every leverage change over `dev_1990`: base cost 591 bps total (26 bps/yr) vs. stressed cost 729 bps total
(32 bps/yr) — **+138 bps over 22.5 years (+6.1 bps/yr), concentrated almost entirely in the 6 burst entries and a
handful of shock exits** (top single-day multiples: 2008-12-19 ×4.18, 2011-09-02 ×3.03, 2002-09-03 ×2.27,
2002-08-28 ×2.23). This is small relative to the 60 bp/yr financing spread already in the headline cost case and
would not flip any gate or the DEV ranking, but it is a real, previously-unquantified cost concentrated exactly on
the trades the brief flags (3x entries at the close of high-vol days) — genuine gap/margin risk (going from 0x to
3x overnight while VIX ≥ 30 is the single scenario most likely to draw a margin call or a wide opening gap) is not
priced by either the 3bp/60bp or 6bp/90bp flat-cost rows the design note reports.

**MATERIAL — required disclosure**: all 6 DEV burst (REBOUND) entries are 0x→3x same-session jumps made while
VIX ≥ 30 and trailing RV21 20–63% (annualised) — i.e., every burst entry, not just some, occurs in the highest-cost,
highest-margin-risk regime the clustered-slippage stress targets; quantified impact is +6.1 bps/yr on DEV, small
but concentrated and not visible in the flat 3bp/60bp or 6bp/90bp cost rows already reported.

## 5. Docstring numerical accuracy — MINOR

The signal file's own docstring ("Known failure modes") states: *"a crash from a calm base costs the first day at
3x before the exit can fire (27-Feb-2007 -3.5% = -10.5%)."* Independently pulled `spx_ret` for 2007-02-27:
**-3.906%**, not -3.5% (3× actual = -11.72%, not the quoted -10.5%). The book was indeed at 3x entering that day
(confirmed: 2007-02-26 close sets `lev=3.0` applied 2007-02-27; the shock exit fires that same close, `lev=0.0`
applied 2007-02-28) — the mechanism claim is correct and independently reproduced, only the illustrative number in
the docstring is off by ~0.4 points of that day's return / ~1.2 points of the resulting loss. Does not affect any
gate, ranking, or frozen parameter. **MINOR** — fix the docstring number on the next edit of this file (not urgent
enough to justify touching a frozen signal file now).

## 6. "Strategy in its own right" vs. over-claiming resemblance to Demeter — CONFIRMED, no over-claim

The design note is explicit and, on independent spot-check, accurate: down-capture 62.4% vs. the record's target
≤40%, up-capture 85.4% vs. ≥100%, and the note's own conclusion ("a de-risked equity book, not the convex one the
inference note describes... it is the 2nd-best DEV candidate... not the best thing in DEV") is not an over-claim —
it is a plainer statement of the shortfall than most of the ablation table would have required. Independently
recomputed the headline exposure stats and they match to the reported precision: cash 42.19% (note: 42.0%), 1x
34.22% (34.4%), 3x 23.59% (23.6%), avg leverage when invested 1.816x (1.81x). **No finding.**

## 7. Sanity spot-checks (all independently confirmed, listed for completeness, no discrepancies)

* Gate report numbers (`gate_check.py` paste) reproduced: dev_1990 Sharpe 0.5426, maxDD -25.61%, chg/yr 5.46,
  cash/1x/3x mix, avg leverage invested — all match independent recomputation from the frozen signal (§4, §6).
* 2009 recovery event ladder ("207/207 days cash, VIX min 19.47 vs. 19.32 exit level") reproduced exactly.
* 2008-10-10 Lehman week ("flat cash the whole week") reproduced exactly (2008-10-06..10-21 all 0.0).
* `_VERIFY.json.lag_test_dev_1990`: Sharpe does NOT collapse on a 1- or 2-session delay (0.543 base → 0.582 lag1 →
  0.559 lag2) — consistent with a low-turnover, regime-driven rule rather than a lag-sensitive one-day-edge rule;
  this is L1 territory but corroborates that the mechanism is not a disguised lookahead artifact (no L3 finding,
  noted only for context).

## Summary

No SEVERE finding: nothing here blocks the OOS look. The mechanism is real, pre-stated, and the code matches the
prose; the re-entry rule is empirically distinct from the panel's known "vix_dissipation" trap (6 firings/22yr vs.
46.6/yr, positive expectancy); and the design note does not over-claim resemblance to Demeter — if anything it
under-sells the model relative to what was found. Two MATERIAL disclosures are required before this candidate's
numbers are presented as reproducing (or being compared against) the Demeter record: (i) the ordinary tier's
cash/invest decision is a VIX-level gate, the exact mechanism the record rules out, so a 2020/2022-shaped OOS
event should not be expected to be captured by this model even though the design note draws on 2020 to motivate
its other ingredients; (ii) all 6 DEV burst entries are 0x→3x same-session jumps made at VIX ≥ 30 / RV21 20-63%,
the highest-cost regime the coordinator's clustered-slippage stress targets, quantified at +6.1 bps/yr on DEV —
small in aggregate but concentrated on exactly the trades this lens is meant to scrutinise. One MINOR item: a
docstring illustrative number (27-Feb-2007 return) is off by ~0.4 points.
