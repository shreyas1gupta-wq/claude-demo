# Report rebuild spec — pass 2 (for `build_report.py` + `report/template.html`)

Goal: `python build_report.py` regenerates `report/index.html` so that it tells the pass-2 story truthfully, with every
number read from files (no hard-coded narrative numbers), reusing the existing design system (the overview page's
`<style>` block and chart helpers are injected — keep that one-source-of-truth mechanism).

## Data sources (all already on disk)
* OOS results at the pass-2 cost rows: `results/<name>_p2.json` (3 bp/60 bp), `_p2_c240` (2/40), `_p2_s690` (6/90) for the
  six pass-1 models; `results/<name>.json`, `_c240`, `_s690` for pass-2 candidates that received their single look
  (currently `sticky_tier`; `vix_vrp` only if `results/vix_vrp.json` exists). Loader rule: for each `signals/*.py`, prefer
  `results/<stem>_p2.json`, else `results/<stem>.json`; skip stems with no OOS file (they appear in the DEV table only).
* DEV-phase: `dev_results/PASS2_DEV_TABLE.md` (or rebuild from `dev_results/<name>.json` + `gate_check.check`),
  `dev_results/<name>_RETURN.json` (headline, biggest_weakness, n_iterations), `dev_results/<name>_VERIFY_L{1,2,3}.md`
  and the digest `dev_results/PASS2_VERIFICATION_SUMMARY.md` (verdicts, SEVERE/MATERIAL findings, expected OOS ranges).
* `PREREG.md` (gates, look budget, verification outcomes, deviations), `results/OOS_LOOK_LOG.md` (every look, timestamped),
  `results/pass2_summary.json` (from `compare_final.py`: cost rows, the two asymmetries, re-entry fire check, acceptance).
* Unchanged from pass 1: `results/demeter_inference.json`, `data/dataset_checks.json`, `RESULTS.md` (the new one).

## Page structure (sections in order; keep ids stable where they exist)
1. **Hero + verdict** — data-driven. Recommended model = the incumbent `final_model_fewtrades` unless a pass-2 candidate
   meets ALL acceptance criteria in `pass2_summary.json` (none does at the time of writing). The verdict must say, in
   this order: (a) Demeter's record is not reproduced (pass-1 finding stands); (b) pass 2 built six candidates under a
   pre-registered DEV-only protocol, five passed the DEV gates, adversarial verification refuted four, the one survivor
   (sticky_tier) got a single OOS look and failed it (Sharpe / CAGR / cash % from its JSON); (c) the incumbent remains
   the recommendation; (d) the negative result is the finding: every rule that survived 1990–2012 did so by being in
   cash most of the time, and that is exactly what a fourteen-year bull punishes.
2. **What changed in pass 2** — bullets from PREREG: DEV-only harness hard-truncated at 2012-06-30; 7 gates; one look per
   candidate; costs 1.5× measured (3/60) as headline, 2/40 secondary, 6/90 stress; three-lens adversarial verification;
   the T-bill and clustered-slippage asymmetries reported; disclosure of the pass-1 `vix_vrp` file.
3. **Method** (existing section, update text: costs 3 bp / 60 bp; five DEV cut-offs + 12 in verification).
4. **Demeter's fingerprint** (existing, unchanged).
5. **The trap** (existing; add the pass-2 echo: the trap's lesson generalised — three more candidates showed DEV Sharpe
   earned in one decade: quote the sub-sample thirds from the verification digest).
6. **NEW — The DEV gauntlet.** Table of all seven pass-2 rows (6 lenses + the reinstated `vix_vrp`) plus the incumbent:
   lens, tunables (declared / true per L1), DEV Sharpe, DEV maxDD, chg/yr, cash %, avg leverage invested, 1950–2012
   Sharpe, gates (PASS / failed ids), verification (holds / REFUTED + which lens), OOS look (yes/no), DEV param sets.
   Below it, one card per candidate: mechanism in one sentence (from RETURN.headline, trimmed), the decisive verifier
   finding (from the digest), and the designer's own "biggest weakness". Refuted candidates show NO OOS numbers anywhere.
7. **NEW — The one that got a look.** sticky_tier vs incumbent vs Demeter vs SPY head-to-head (OOS window), calendar
   years, leverage distribution, the 10 OOS position dates, the 2020-onward 97 % cash fact, cost rows (2/40, 3/60, 6/90),
   the two asymmetries (T-bill zeroed on cash days; clustered slippage), acceptance-criteria checklist with pass/fail.
   If `results/vix_vrp.json` exists, the same block for `vix_vrp`.
8. **Leaderboard** (existing) — now at 3 bp / 60 bp from the `_p2` files; add columns "OOS look" and "verification";
   include Demeter and SPY rows as before; sort by OOS Sharpe; footnote the multiple-comparison count: 6 pass-1 + 2
   pass-2 looks = 8 candidates with OOS numbers, and that the recommendation was chosen on DEV in both passes.
9. **The recommended model** (existing; still `final_model_fewtrades`; its rules ladder and params from the docstring —
   make the ladder data-driven from the docstring rather than hard-coded).
10. **Side by side / episodes** (existing).
11. **Sensitivity** (existing; cost table now from `_p2*` files; keep perturbation chart).
12. **Limitations** — rewrite: eight candidates have now seen OOS across two passes; the design saw the record; one
    market/one regime; costs modelled; Demeter unaudited (quadrant counts 3,477 vs 3,219); data seams; PLUS the pass-2
    lessons: "structural constants" chosen on DEV are parameters (true counts 7–13), mechanical gate checks cannot see
    them, sub-sample thirds expose one-decade Sharpe, a lag test exposes same-close sensitivity.
13. **What would move the answer** — from RESULTS.md (intraday/options data; a walk-forward re-selection; Principal-
    authorised exploratory look at the refuted panel, clearly labelled, if wanted).

## Rules
* Every number rendered comes from a file; if a source is missing, render "—", never a placeholder number.
* Costs are stated next to every OOS number ("3 bp / 60 bp").
* Refuted candidates: DEV numbers only, verification verdicts visible, no OOS.
* Keep light/dark theme behaviour, responsive tables (`tbl-wrap`), and the existing chart helpers.
* `build_report.py` must run end-to-end from the model dir with the pinned Python; print the candidate list it used.
* Do not touch `evaluate.py`, `engine.py`, signal files, or any results file.
