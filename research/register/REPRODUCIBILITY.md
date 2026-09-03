# Reproducibility audit — 2026-09-03 (first full re-run of the analysis corpus)

Every committed `scripts/analyze_*.py` was re-run on the committed vaults, exactly as a
stranger would run it (`PYTHONPATH=<repo> python3 scripts/<name>.py`, 300s timeout).
No new trials, no census cells — reproduction of already-booked prints only.

## Headline result
**50/50 scripts run clean** (48 directly; `analyze_credit_cycle.py` and
`analyze_fast_stress.py` are `--demo`-gated by design and pass with the flag).
**Every checked booked headline reproduces** — 29 pre-listed headline numbers across the
program's key trials were grepped against the fresh logs and all 29 match (24 exactly as
written; 5 were rounding/format variants of the same number, e.g. booked "p=0.110" vs
printed "p=0.1099", booked "rho 0.52" vs printed "0.519"). Stochastic scripts (bootstrap,
Monte Carlo) reproduce exactly because seeds are fixed by house rule.

Spot checks covered: CW-D1a (both windows), MR1-S, F2-index, TS1, F7a, H68a, H53a (all
three numbers), OL-D1a, OL-D2a, EN-D2a (rate + lift), CW-D1v, F5a (all four numbers),
F1b, F1c, N4a, CW2, M0/M1, EN1, J1, F2-WF.

## The one semantic divergence (recorded, record unchanged)
`analyze_value_panels.py`'s US drawdown table prints the sample-end month (2024-11) in the
"recovered" column when a drawdown is still open at sample end — a naive-print edge case.
The committed RESULTS file carries the hand-corrected reading ("**not recovered at sample
end (2024-11)**"), which is the true one. The committed record is right; the script's raw
print is the artifact. Fixing the script's edge case is Track-R hygiene, not urgent — the
record, not the print, is authoritative (this file says so now).
**FIXED 2026-09-03 (same day):** `winters()` now flags open-ended drawdowns and prints
"not recovered at sample end"; verified by run-diff-restore — the regenerated RESULTS file
is now byte-identical to the committed record, hand-corrected line included.

## Process note #7 — scripts that WRITE their RESULTS files truncate hand-appended sections
Several analyze scripts regenerate their `*-RESULTS.md` wholesale on every run. The
committed RESULTS files carry hand-appended "Honest read (written AFTER the print)"
sections — which is the DISCIPLINE (interpretation after the print) — so a bare re-run
DESTROYS the interpretation while reproducing the numbers. This audit diffed all 19
affected files (every diff was pure deletion of the hand-appended section, plus the one
value-panel annotation above — i.e., **all computed content reproduced byte-identically**)
and then restored every file from HEAD. RULE, effective now: reproduction runs must never
let a script write its RESULTS path against a dirty expectation — re-run, diff, restore;
the committed RESULTS file is the record and hand-appended interpretation is part of it.

## Also resolved in this sweep (details in verification-log.md, 2026-09-03)
- climate vault Niño-region [VERIFY] → **Niño 1+2 confirmed by computation** (level,
  amplitude, and 0.664 anomaly-corr vs the vaulted ONI).
- commodities metal-units [VERIFY] → resolved from the committed provenance json (kt
  metals / t gold — the reading the pass used).

Re-run this audit at the annual loop (a checklist row is added in ANNUAL-LOOP.md).
