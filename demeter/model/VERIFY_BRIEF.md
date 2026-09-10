# Verification brief — adversarial review of a frozen, gate-passing candidate (DEV only)

You are one of three independent verifiers on one candidate. Your job is to REFUTE it. Default to "refuted" when
the evidence is ambiguous; a candidate that survives three sceptics has earned its single out-of-sample look, one that
does not has saved the study from a false claim. You never tune, never propose new parameters, never run
`evaluate.py`, never touch `results/`, never load data past 2012-06-30, never edit a signal file.

## Environment
Working dir `C:\tmp\claude-demo\demeter\model`; Python `C:\Users\Shreyas.1Gupta\AppData\Local\Python\pythoncore-3.14-64\python.exe`
with `PYTHONIOENCODING=utf-8 PYTHONUNBUFFERED=1`. Token discipline: read `DESIGN_BRIEF.md` §"What the record says" and
`PREREG.md` only; do NOT read `results/demeter_inference.md`; print JSON fields with small scripts, never Read big files.

## Inputs for candidate `<name>`
* `signals/<name>.py` — the frozen rule (read it fully, line by line).
* `dev_results/<name>.json` — final harness run; `dev_results/<name>_DESIGN_NOTE.md` — the designer's own account
  (iteration count, grids, structural decisions, weaknesses); `dev_results/<name>_grid.csv` — the final grid;
  `dev_results/<name>_VERIFY.json` — the mechanical battery (run `python verify_tools.py signals/<name>.py` if missing).
* `dev_harness.py --params '{...}' --tag verify_<lens>_<k> --no-plateau` for any single variant you need to test a claim
  (e.g. a structural constant nudged, a component ablated) — write the tag so nothing overwrites the designer's files.

## The three lenses (you are assigned exactly one)

**L1 Causality & code.** Lookahead in any form: `.shift(-k)`, centered windows, full-sample statistics, `cummax`/`max`
over future rows, calendar rules that use the next row, state machines that read day t+1, any use of `spx_tr`/`rf` in a
way that is not available at the close of t, VIX close timing (16:15 vs 15:59 — a known, accepted 16-minute
approximation; flag only if the rule is sensitive to it). Confirm `_VERIFY.json` causality (12 cut-offs) and read the
lag test: if Sharpe collapses with a one-session delay, say what that implies. Check that `DEFAULT_PARAMS` count
matches the declared tunables and that every UPPER_CASE constant is genuinely structural — cross-check the design note:
a constant whose value was chosen by comparing DEV results IS a tuned parameter (report the true count; >6 = G7 breach).

**L2 Overfit & plateau.** From the grid CSV and `_VERIFY.json`: is the frozen point a plateau or a peak (rank, one-step
neighbourhood, share of the grid passing G2–G4)? How many parameter sets were evaluated in total (design note) and how
many distinct structural variants — estimate the selection haircut honestly (with N tries and a grid max of X, what
Sharpe would you EXPECT out of sample: give a range and the reasoning, e.g. Bailey–López de Prado deflation logic).
Sub-sample stability (halves/thirds in `_VERIFY.json`): does the DEV Sharpe come from one decade? Which single
episodes drive it (use `stress_episodes`)? Does the dev_1950 result contradict dev_1990? Does the rule's cash share or
average leverage make its Sharpe a low-exposure artefact (Sharpe of 0.5x SPY ≈ Sharpe of SPY — say so if it applies)?

**L3 Mechanism & execution.** Is there a real economic mechanism, stated before the runs (design note §Mechanism) and
consistent with what the rule actually does? Is it the pass-1 trap in disguise (buys after implied vol has just fallen,
in any form)? What regime breaks it — name one historical DEV regime and one plausible future one. Execution realism:
3x entries at the close of high-vol days (margin at 3x, gap risk, clustered slippage — the coordinator will stress
cost×max(1, RV21/15%)); how many of the DEV position changes happen on days with |return| > 2%? Is the rule a
"strategy in its own right" (the study's honest bar) or does the design note over-claim resemblance to Demeter? Does
it violate anything the record rules out (a slow trend gate; a vol-LEVEL gate as the invest/cash decision) — allowed
for a stand-alone strategy, but it must be labelled as "will not reproduce Demeter's 2020", check that the note does.

## Output
1. `dev_results/<name>_VERIFY_<L1|L2|L3>.md` — findings with the evidence (numbers copied from files, script names),
   each finding tagged SEVERE (blocks the OOS look until fixed) / MATERIAL (must be disclosed in RESULTS.md) / MINOR.
2. Your final message: ONLY the JSON object in the task prompt's schema. `refuted=true` means at least one SEVERE
   finding. `required_disclosures` are the MATERIAL findings in one sentence each, ready to paste into a report.
