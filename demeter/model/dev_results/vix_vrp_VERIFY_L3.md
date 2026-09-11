# vix_vrp — L3 verification (Mechanism & execution), pass 2, reinstated original

Verifier: adversarial L3, independent of the lens-5 designer. Candidate: `signals/vix_vrp.py` (original, frozen in
pass 1; reinstated 2026-09-12 after `vix_vrp_v2` was refuted — see `PREREG.md` "Verification outcomes"). No pass-1
design note exists for this file; the only ex-ante account is its own docstring. `dev_results/vix_vrp_DESIGN_NOTE.md`
Part 1 is a pass-2 AUDIT of this file (written after the fact, not a design note); Part 2 concerns the refuted `v2`
and is used here only where it tests this file's own constants (ablation rows `V1_calm3x`, `V0c_panic2`, confirmed
below to be post-hoc checks, not the process that picked 2x/1x).

## 1. Mechanism — real, but its exact form is DEV-conditional, not pre-registered

The economic idea (implied vol as a forward-looking price vs. realised vol as backward-looking; their gap — the
variance risk premium — normally positive and collapsing only during a shock; equity premium per unit of risk
differs across VIX levels) is a genuine, literature-grounded mechanism and it is what the code actually implements —
no inconsistency between story and code (verified line-by-line against `signals/vix_vrp.py`, checked separately by
lens L1's causality read; I re-derive the state machine and VRP series independently below).

**However**, the "Why these rules" section of the docstring is not a pre-registered mechanism note: it says
literally "*Conditional sorts of next-day excess returns on the development sample show three volatility regimes*"
— i.e., the regime boundaries (12–18 / 18–30 / >30) and the qualitative leverage schedule (lever the calm bucket,
sit out the middle, harvest panic unlevered) are read off DEV outcome sorts, not derived from theory first and then
checked. This is consistent with (not identical to) L1's finding on the true tunable count; from the mechanism side
specifically: there is no artifact anywhere in the repo showing this mechanism was written down *before* the DEV
conditional sort was computed. **MATERIAL** — disclose that the qualitative mechanism, not just the five numeric
parameters, was informed by a look at DEV outcomes.

## 2. Not the pass-1 trap in disguise — verified two ways

`vix_dissipation` (pass-1's trap, DEV Sharpe −0.31) invests when VIX falls *relative to its own trailing average*
(a direction/momentum-in-IV signal) — the mechanism the coordinator is checking for. `vix_vrp` does not contain
this in either component:

* **CALM entry is a level threshold** (VIX < 13.64), not a "VIX just fell" signal. Reproduced independently
  (`vix_regime` re-run on 1990–2012H1 data): CALM is entered 26 times, all from ELEVATED, never directly from PANIC
  (state-transition census below) — it requires VIX to have been range-bound low, not merely falling.
* **The VRP re-entry channel runs the opposite direction from the trap.** VRP = VIX/100 − RV. If VIX falls while
  realised vol has not yet caught down (a falling-IV, still-choppy market — exactly the vix_dissipation trap's
  favourite setup), VRP falls too, which pushes the filter *toward* the cash override (`vrp < vrp_min`), not toward
  a lever-up. A falling VIX alone cannot trigger new exposure through this channel.
* State-transition census, reproduced from the raw VIX series (1990–2012H1, `vix_regime(vix, 15.5, 30, 0.12)`):
  114 total state changes, all ELEVATED↔CALM (57) or ELEVATED↔PANIC (57); **zero** direct CALM→PANIC or PANIC→CALM
  transitions in DEV — matches the docstring's claim that the direct jump "never happens in practice." Confirms
  the design note's audit: "zero entries to ≥2x in both bears" (`spurious_reentry_census` in `vix_vrp.json`: 0/0).
* The design note's own ablation (Part 2, round 1) tested the closer analogue of the trap directly — VRP-normalisation
  **burst re-entry to 2x inside PANIC** (rows `V4*`, `V6` in `vix_vrp_v2_ablation_all.csv`) — and it was rejected:
  50–100% of 2008 burst entries went negative over the next 10 sessions at every peak-fraction tested (0.65–0.80),
  maxDD worsened to −26…−44%. The frozen file does not contain this component. **No finding** (mechanism check
  passes) — but note this is evidence gathered by the pass-2 auditor, not by whoever froze the original in pass 1.

**Untested branch, MINOR:** because the direct CALM↔PANIC jump never fires in 22.5 years of DEV, that entire code
path (`vix_regime`'s `st==0: if x>panic_in: st=2` and the symmetric `st==2: if x<calm_in: st=0`) is logically present
and presumably correct but has zero empirical exercise. A future single-session VIX gap from <13.6 to >30 (or the
reverse — a rapid, policy-driven or circuit-breaker V-shaped collapse from panic to calm) would activate code that
has never been checked against real data.

## 3. Violates a rule the record explicitly excludes — allowed, but the required label is missing

`DESIGN_BRIEF.md` "What the record says": *"Ruled out by the record: ... vol-LEVEL gating, ..."* `vix_vrp` **is**
a vol-LEVEL gate as the invest/cash decision (CALM/ELEVATED/PANIC keyed on the absolute VIX print, not on any
price-trend or VRP-direction input — the VRP filter only ever pulls to cash, 53 days total, never adds exposure).
The brief is explicit that this is *allowed* for a stand-alone strategy ("You are NOT required to reproduce
Demeter... a well-documented failure with the reason is a deliverable of equal standing") **provided it is labelled**
as not reproducing Demeter's actual crisis behaviour.

Checked whether that label exists:
* `signals/vix_vrp.py` docstring: **no** mention of Demeter's 2020 behaviour or of the vol-LEVEL exclusion at all;
  its only Demeter reference is the VIX-timing caveat (16:15 vs 15:59) and calling the leverage tiers "Demeter-style
  discrete steps" (line 49) — see finding 4 below.
* `dev_results/vix_vrp_DESIGN_NOTE.md` Part 1 (the pass-2 audit) comes closest: "*the VRP filter is not the engine;
  the VIX-level machine is (the record says level gating is what Demeter did NOT do — an honest weakness)*" — this
  discloses the mechanism class but never states the concrete consequence for 2020 specifically, and it was written
  in pass 2, after the file was already frozen and (briefly) retired/reinstated — it is not part of the frozen
  candidate's own record.
* Neither document states the specific, checkable fact: Demeter's record shows "≥14 of 21 days at 3x with VIX
  31–57 in Apr-2020" (`DESIGN_BRIEF.md`, "What the record says") — i.e., Demeter's *highest* leverage in the
  crisis rebound — while `vix_vrp`'s PANIC tier is capped at 1x and never reaches 2x (`LEV_PANIC=1.0`,
  `spurious_reentry_census` confirms 0% of days ≥2x in both bears); the 2009 recovery is taken almost entirely at
  1x (design note: "the model never reached 2x in 2009 because VIX never fell below 13.6" — 84 PANIC days at 1x
  then cash). Structurally, this candidate cannot reproduce Demeter's defining 2020 signature even in an analogous
  episode.

**MATERIAL — required disclosure**: the frozen candidate's own record contains no explicit statement that it will
not reproduce Demeter's 2020 crisis-rebound leverage profile; this must be added to `RESULTS.md` verbatim before
any OOS interpretation leans on resemblance to Demeter.

## 4. "Demeter-style" framing over-claims resemblance — MATERIAL

`signals/vix_vrp.py` line 49: `# Leverage tiers are structural constants (Demeter-style discrete steps), not
tunables.` The *form* (discrete leverage steps) is Demeter-style; the *content* is not — Demeter's leverage is
"not monotone in the vol level" and is highest in crisis rebounds (`DESIGN_BRIEF.md`), whereas `vix_vrp`'s leverage
is monotone-in-reverse by construction (2x calm → 0x elevated → 1x panic, capped below calm even in the best panic
outcome). Calling this "Demeter-style" in the frozen file's own docstring risks the reader concluding closer kinship
than the mechanism supports. Recommend RESULTS.md state plainly: shares Demeter's discrete-tier *form*, not its
level-independent, crisis-maximal leverage *behaviour*.

## 5. Execution realism — turnover clusters on the worst days to trade

Reproduced independently from `signals/vix_vrp.py` on `data/market_daily.csv` (1990-01-01…2012-06-30, matches
`n_position_changes=136`, `position_changes_per_year=6.04` in `vix_vrp.json`):

| | n | share with \|decision-day spx_ret\| > 2% |
|---|---|---|
| all position changes | 136 | 51 (**37.5%**) |
| → into CALM (2x) | 26 | 1 (3.8%) |
| cash → PANIC (1x) entries | 42 | 24 (**57.1%**) |
| → into cash (0x) | 68 | 26 (38.2%) |

Over a third of all rebalances, and more than half of the cash→1x PANIC entries specifically, happen on the exact
days the flat per-unit `cost_bps` assumption is least realistic (PANIC entries require VIX > 30, which co-occurs
with large daily moves by construction). Quantified with the coordinator's suggested stress
(`cost × max(1, RV21/15%)`) applied only on transition days: annual cost drag rises from 0.25%/yr to 0.37%/yr at
3bp, and from 5.02%/yr to 7.43%/yr at the 60bp stress tier (a **1.48x** multiplier on the drag either way, from the
136 real transition dates, not an assumed average). **MATERIAL** — in absolute terms this does not threaten the
Sharpe (0.61 base case is far from the gate bars even at the higher multiplier), but it should be disclosed as a
directional bias: the model's real-world cost is understated more than the 6/90 stress row already implies, because
that row applies a flat higher rate uniformly rather than loading it onto the specific high-vol transition days.

**VIX close-timing / hysteresis flip risk** (coordinator's specific question): of the 136 transitions, 38 (**28%**)
occur with the triggering VIX print within 0.3 vol points of the relevant threshold (13.64 / 15.5 / 30 / 26.4) —
0.3 points being the docstring's own estimate of the typical 16:15-vs-15:59 intraday drift. For a level-with-
hysteresis machine this does not change *how much* time is spent in each state materially (hysteresis bands are
1.9–3.6 vol points wide, well above the drift), but it does mean roughly **1 in 4 rebalance dates** could plausibly
fall a session earlier or later than modelled purely from the 16-minute timing gap — a real, previously unquantified
precision limit on the event-ladder dates quoted in the design note (e.g. exact entry/exit days around 2008
capitulation). **MINOR** (does not change aggregate exposure or the Sharpe materially; affects date-level precision
of individual case studies, already disclosed qualitatively — this quantifies it).

## 6. Cash-heavy Sharpe / CAGR — T-bill accrual on cash days inflates CAGR, not Sharpe

Reproduced from the engine convention (`r[t] = rf[t] + L_{t-1}·x[t] − costs`) on the same 1990–2012H1 window:
64.3% of days are cash (`pct_days_cash` in `vix_vrp.json`), and cash days earn the 3-month T-bill (avg 3.36%/yr
annualised over the window) rather than Demeter's own 0%-cash convention. Sharpe is computed on excess returns, so
the T-bill leg nets to ~0 there and is not inflated by the cash share — consistent with the coordinator's framing.
CAGR is a different story: recomputing with cash days forced to 0% return, back-of-envelope CAGR falls from ~11.05%
(as engineered, ex-cost) to ~8.68% — a **~2.4 pt/yr** gap attributable purely to the T-bill credit on cash days, on
top of the reported 10.61% (with costs). This matches the magnitude the pass-2 designer disclosed for `v2`
("roughly 2%/yr" — design note line 265) but that disclosure was never written for the original file, which has no
design note of its own. **MATERIAL — required disclosure**: any headline CAGR comparison between this candidate and
Demeter's realised track record must state that ~2–2.4 points of the candidate's annual return is T-bill accrual on
cash days under a convention Demeter's own bookkeeping does not use.

## 7. Docstring imprecision — MINOR

"Hysteresis keeps position changes to ~8/yr" (docstring, line 25) vs. the harness's actual 6.04/yr (dev_1990) or
2.18/yr (dev_1950, cash-only pre-1990). Not material to any gate or conclusion, but the number should be corrected
if this docstring is ever revised, since a reader who takes "~8/yr" at face value overstates real-world turnover
(and therefore cost drag) by ~30% relative to the measured figure.

## Summary of findings

| # | Tag | Finding |
|---|---|---|
| 1 | MATERIAL | Mechanism's qualitative form (regime boundaries, tier assignment) is read off DEV conditional sorts per the docstring's own account, not pre-registered before any DEV look — no pass-1 design note exists to show otherwise. |
| 2 | — | Not the pass-1 (vix_dissipation) trap in disguise — verified by independent state-machine reconstruction and VRP-direction analysis; the one closer analogue (VRP-burst re-entry to 2x) was tested and rejected by the pass-2 auditor, and is absent from the frozen file. Direct CALM↔PANIC jump is logically present but 0% exercised in DEV (MINOR, untested branch). |
| 3 | MATERIAL | Vol-LEVEL gating is explicitly ruled out by the study's record (`DESIGN_BRIEF.md`); allowed for a stand-alone strategy but the frozen candidate's own docstring contains no disclosure that it will not reproduce Demeter's 2020 crisis-rebound leverage profile (PANIC capped at 1x vs. Demeter's ≥14/21 days at 3x in Apr-2020). |
| 4 | MATERIAL | "Demeter-style discrete steps" (docstring line 49) over-claims resemblance: the leverage schedule is monotone-in-reverse of vol level, the opposite of Demeter's non-monotone, crisis-maximal profile. |
| 5 | MATERIAL | 37.5% of position changes (57.1% of PANIC entries specifically) occur on \|ret\|>2% decision days; RV21-scaled cost stress raises modelled drag by 1.48x versus flat-rate costs on those dates — small in absolute Sharpe terms but a real, previously unquantified directional bias. |
| 5b | MINOR | 28% of transitions sit within 0.3 vol points of a state threshold — the same order as the disclosed 16-minute VIX-timing gap; affects date-level precision of case studies, not aggregate exposure. |
| 6 | MATERIAL | ~2–2.4 pts/yr of the reported CAGR is T-bill accrual on the 64% cash days under a convention Demeter's own bookkeeping (0% on cash) does not share; Sharpe is unaffected (excess-return basis). |
| 7 | MINOR | Docstring's "~8/yr" turnover claim overstates the measured 6.04/yr (dev_1990) by ~30%. |

No SEVERE finding under this lens: the mechanism is real, is not the pass-1 trap, is internally consistent with the
code, and the vol-LEVEL gate — while excluded by the record — is explicitly permitted for a stand-alone strategy by
`DESIGN_BRIEF.md`. The gap is disclosure, not validity: multiple MATERIAL items must be carried into `RESULTS.md`
before this candidate's OOS look (if it proceeds) is interpreted against Demeter's own record.
