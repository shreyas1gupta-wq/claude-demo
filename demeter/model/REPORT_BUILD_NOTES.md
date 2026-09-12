# Report rebuild (pass 2) — build notes

Built 2026-09-12. Two files changed: `build_report.py` and `report/template.html`
(plus their outputs `report/index.html` and `report/report_data.json`). Nothing under `results/`,
`dev_results/`, `signals/`, `evaluate.py`, `engine.py`, `features.py`, `RESULTS.md` or `PREREG.md`
was touched, and neither `evaluate.py` nor `oos_final.py` was run.

## build_report.py
* `TAGS` now also excludes `_p2`, `_c240`, `_s690`. Candidate discovery no longer globs `results/`:
  it walks `signals/*.py` and prefers `results/<stem>_p2.json`, else `results/<stem>.json`; a stem with
  no out-of-sample file never enters the candidate set (it appears in the DEV gauntlet only). The
  file actually used is kept per candidate as `file_stem`, so daily series read `<file_stem>_daily.csv`.
* Each candidate carries `cost_rows` = {c240, headline, s690} from its `_c240` / `_s690` siblings.
* New `pass2` block: `dev_table` (one row per `dev_summary.DEFAULT` panel entry — lens, declared vs
  verifier-true tunables, DEV/1950 numbers, SPY reference, eras, stress episodes, thirds/halves and the
  lag test from `_VERIFY.json`, gates recomputed via `gate_check.check`, verification verdict + decisive
  finding, OOS-look label, `n_iterations` / DEV parameter sets), `verification` (digest parsed into
  per-lens severe/material/disclose + verdict + pre-look OOS range), `look_log` + `look_log_rows`,
  `summary` / `summary_by_stem` (pass2_summary.json), `prereg` excerpts (Verification outcomes, Outcome
  of the look budget, Deviations), `changed` / `limitations` / `lessons` / `next_steps` parsed out of
  RESULTS.md, `position_changes` (derived from the daily CSV), `counts`, `oos_labels`, `cost_labels`.
* Recommended model = `final_model_fewtrades` from its `_p2` file unless a candidate has
  `acceptance.ALL == true` in `pass2_summary.json` (none does; the builder prints which).
* Rules ladder is generated from the docstring (`rules_ladder`): numbered rules are parsed out, and when
  a file defers to another signal ("Identical logic to `final_model`") the referenced file's rules become
  the base ladder and this file's bullets are appended as deltas. Structural constants come from
  `verify_tools.constants` on both files. Nothing about the ladder is hard-coded.
* `generated` = 2026-09-12; `ensure_tag` was replaced by a load-only lookup so the builder can never
  invoke `evaluate.py`; the buy-and-hold reference window now follows the recommended model's own dates.
* Demeter's four-quadrant mix and published cash share now come from
  `demeter_inference.e_summary.quadrant_fingerprint` instead of the pass-1 hard-coded numbers.

## report/template.html
Sections in the spec's order: hero + four-part data-driven verdict; **What changed in pass 2** (RESULTS.md
comparison table, the look log, PREREG deviations); Method (3 bp / 60 bp, 5 DEV cut-offs + 12 in
verification, gate bars read from `gate_check`); Fingerprint (unchanged); The trap + the pass-2 echo
(sub-sample thirds per candidate); **NEW DEV gauntlet** (8-row table + one card per candidate with
mechanism, decisive verifier finding, designer's biggest weakness, pre-look OOS range — refuted rows show
no OOS numbers anywhere); **NEW The one that got a look** (head-to-head vs incumbent/Demeter/SPY, the story
and the 10 position dates, cost rows, the two asymmetries, the acceptance checklist, leverage mix, calendar
years — rendered generically for every entry in `pass2.looked`); Leaderboard with "OOS look" and
"verification" columns plus the multiple-comparison footnote; the recommended model (ladder from the
docstring); side by side (episode table now carries the pass-2 survivor's column); Sensitivity (cost grid
from the `_p2` file, three-row cost basis, perturbations); Limitations + lessons + next steps from
RESULTS.md. Chart helpers, `tbl-wrap` tables, the injected style block and light/dark behaviour are
unchanged; `<meta charset="utf-8">` was added because em dashes mojibaked without it. Every rendered
number comes from the embedded JSON, and missing fields render as "—"; acceptance thresholds are parsed
out of the criterion keys (`sharpe_gt_0.73` → 0.73) rather than typed in.

## Validation
* `python build_report.py` completes and prints the candidate list: 7 candidates
  (baseline_volregime, final_model, final_model_fewtrades, shock_reentry, sticky_tier,
  trend_vol_fewtrades, vix_dissipation), recommended `final_model_fewtrades`, pass-2 looks `['sticky_tier']`,
  DEV panel 10 rows (6 lens candidates, 5 gate passers, 4 refuted, 1 verified).
* `report/report_data.json` parses; the JSON embedded in `index.html` parses; no placeholder survives.
* Every `$('#id')` and runtime `#id-${key}` the JS touches exists in the markup (66 static + 11 dynamic,
  none missing); every `R.*`, `P2.*` and `C.*` path read by the JS exists in the data.
* No refuted candidate has an OOS result file on disk or a row in `R.candidates`.
* Browser (local http server, Chrome): **zero console messages of any level**; all 12 section headings
  render; all 9 charts produce an SVG; no render target is empty; `document.body` has no horizontal
  overflow; spot-checked numbers match RESULTS.md (incumbent 16.78% / 0.73 / −20.5%; sticky_tier 0.24
  Sharpe, 3.23%, 73% cash, 10 changes, cost rows 3.24/3.23/3.20, asymmetries 1.74%/0.05 and 16.34%/0.72,
  thirds 0.98 / undefined / 0.44, 2020–2026 Sharpe −0.41 at 97% cash, 0 of 10 implied re-entry dates).

## Spec items not fully met
* Spec §8 says the footnote should read "6 pass-1 + 2 pass-2 looks = 8 candidates" and §12 "eight
  candidates have now seen OOS". Only one pass-2 look exists (`vix_vrp` was refuted and never evaluated),
  so the page computes the count from the data and says **seven** — matching RESULTS.md and PREREG.md.
* The `vix_vrp` card has no RETURN.json (pass 1 left none), so its mechanism sentence falls back to the
  `family` line in `dev_results/vix_vrp.json` and its "designer's biggest weakness" renders as "—".
* Sensitivity's "different windows and instruments" table still uses the pass-1 tagged runs
  (`final_model_oos2005/_fin40/_es/_nq`, 2 bp basis) because re-running them at 3/60 would be a new
  out-of-sample evaluation; the table now states the model and cost basis of each row explicitly.
