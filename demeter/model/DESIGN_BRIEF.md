# Design brief — Demeter dual-engine, pass 2 (read fully before doing anything)

You are one of six candidate designers. Each designer owns ONE lens (assigned in your task prompt and listed in
`PREREG.md`). You design, build and DEVELOPMENT-test one signal file. You never see the out-of-sample window.

## Environment (Windows laptop, corporate proxy — no internet needed for this task)

* Repo model dir (absolute): `C:\tmp\claude-demo\demeter\model` — run every command from here.
* Python: `C:\Users\Shreyas.1Gupta\AppData\Local\Python\pythoncore-3.14-64\python.exe` (the bare `python` alias is broken).
  Always set `PYTHONIOENCODING=utf-8` and `PYTHONUNBUFFERED=1`. pandas 3.0 / numpy 2.3 are installed.
* Write Python into `.py` files and run them; do not paste multi-line Python into the shell.
* Shell is PowerShell 5.1 (no `&&`) or Git Bash; either is fine.

## Read in this order (do not skip)

1. `PREREG.md` — the gates you must pass and the rules you must not break.
2. `RESULTS.md` — what the previous pass built and where it failed (down-capture 146% vs Demeter 23%).
3. `results/demeter_inference.md` — sections 3 to 8 are essential (what the record says a daily rule had to do;
   what is ruled out; the quantitative targets). Appendix B has the day-by-day Feb–Apr 2020 tables. **You may read
   this file; you may NOT tune anything on it. It describes the out-of-sample regime and exists so you choose
   ingredients, not parameters.**
4. `engine.py` (the return convention: the target leverage you output at close t earns day t+1), `features.py`
   (causal helpers — reuse them), `signals/*.py` (the six evaluated candidates + `vix_vrp.py`).
5. `dev_results/final_model_fewtrades.json`, `baseline_volregime.json`, `vix_dissipation.json`, `vix_vrp.json` — DEV
   reference points already computed with the harness (summary table below).
6. `dev_harness.py` — your only evaluation tool.

## Hard rules (a breach voids the candidate)

1. **Never run `evaluate.py`.** Never write anything into `results/`. Never load `data/market_daily.csv` beyond
   2012-06-30 — use `dev_harness.py`, or in your own scripts `E.load_market(end="2012-06-30")`.
2. **Never use Demeter's monthly returns (`../data/monthly_returns.csv`) as a model input or a tuning target.**
3. **Causality.** Only trailing/expanding computations on data available at that day's close. No centered windows,
   no full-sample z-scores/quantiles/means, no `.shift(-k)` on data, no fitted model that saw dates past the decision
   date. If you want a calendar rule (e.g. "decide on the last trading day of the week"), use `df.index.dayofweek`
   or state explicitly that the exchange calendar is known in advance; do not derive it from the existence of the
   next data row without saying so.
4. **≤ 6 tunable parameters.** Anything else is a declared structural constant, named in the docstring with the reason
   it is not tuned. Do not hide tuned values in constants.
5. **Do not edit `engine.py`, `features.py`, `evaluate.py`, `dev_harness.py` or any existing signal file.** If you find
   a bug, report it in your design note with a minimal reproduction; the coordinator fixes it so every candidate is
   re-run consistently.
6. **Plateau, not peak.** Choose parameters from a region of the grid that is flat; the harness measures the share of
   ±15%/±30% perturbations that hold Sharpe within 25% of base (gate G6 needs ≥ 50%).
7. **Bank as you go.** Write your design note incrementally; a token cut must not lose work.
8. **Count your iterations.** Every distinct parameter set you evaluated on DEV is recorded (the grid CSV counts as
   one grid; each manual re-run counts as one). Report the total.

## Signal file contract (`signals/<name>.py`)

```python
"""<Plain-English rules, numbered. For each parameter: the development window it was chosen on and why.
Structural constants named with reasons. Known failure modes.>"""
import numpy as np, pandas as pd
import features as F            # model dir is on sys.path when loaded by the harness / evaluator

NAME = "<name>"                 # == file stem
FAMILY = "<one line>"
HYPOTHESIS = "<why this should have worked in 1950-2012 / 1990-2012, mechanism first>"
DEFAULT_PARAMS = dict(...)      # <= 6 numeric tunables
def signal(df, **params) -> pd.Series:   # target leverage in [0, 3], indexed like df, NaN or 0 before warm-up
```

`df` columns you can use: `spx_px, spx_tr, spx_ret, spx_tr_ret, rf_pct, rf_daily, vix_open, vix_high, vix_low,
vix_close` (VIX from 1990-01-02, 4 isolated NaNs — `ffill()` them), `es_ret, nq_ret` (futures, cross-checks only).
Leverage may be continuous in [0,3] or discrete {0,1,2,3}; Demeter is discrete, the engine accepts either.

## Harness usage

```
python dev_harness.py signals/<name>.py                       # full DEV report at 3 bp / 60 bp -> dev_results/<name>.json
python dev_harness.py signals/<name>.py --grid grid.json      # + grid CSV; grid.json = {"param": [values], ...}
python dev_harness.py signals/<name>.py --params "{\"k\": v}" --tag try3 --no-plateau   # quick single variant
python gate_check.py dev_results/<name>.json                  # the pre-registered gates, PASS/FAIL per gate
```
Name your grid spec `dev_results/<name>_grid_spec.json` and any scratch scripts `dev_results/<name>_*.py` — six designers
share this directory concurrently, so never use generic file names.
The JSON contains: `windows` (dev_1990, dev_1950) at 3/60, the same at 6/90 and 2/40, `eras`, `stress_episodes`
(1987, 1990, 1998, 2000-02, 2002-03, 2007-09, 2009, 2010, 2011), `event_ladders` (your leverage path around 13 dated
lows — use these to see whether your exit fired before the low and your re-entry near it), `spurious_reentry_census`
(entries to ≥2x during the two grinding bears and their next-10-day P&L — the test that killed the VIX-dissipation
trap), `plateau_dev_1990/1950`, `lookahead_check`.

## DEV reference points (3 bp / 60 bp, from the harness)

| signal | dev_1990 Sharpe | dev_1990 maxDD | chg/yr | dev_1950 Sharpe | 2000-02 bear | 2007-09 GFC | 2009 recovery | plateau |
|---|---|---|---|---|---|---|---|---|
| SPY buy & hold 1x | 0.39 | −50.8% | 0 | 0.47 | −47.2% | −54.8% | +67.4% | — |
| final_model_fewtrades (incumbent) | 0.43 | −25.1% | 7.1 | 0.56 | −21.1% | −8.6% | +6.6% | 75% |
| baseline_volregime | 0.37 | −38.2% | 11.6 | 0.63 | −26.3% | −15.3% | +7.7% | 81% |
| vix_dissipation (the trap) | −0.31 | −93.5% | 46.6 | −0.19 | −80.1% | −67.1% | +7.2% | 83% |
| vix_vrp (never evaluated OOS) | **0.61** | −19.8% | 6.0 | 0.36 (cash pre-1990) | +15.1% | −15.7% | +44.4% | 100% |

Read that table before designing: the incumbent's DEV Sharpe barely beats buy-and-hold; the trap is not a near miss,
it is ruinous; vix_vrp is the strongest DEV point in the repo and nobody has looked at it out of sample. Every model
so far misses most of the 2009 recovery (the incumbent earned +6.6% of SPY's +67%). Whether a model can take the
2009 recovery without being destroyed by the 2000-02 and 2008 false dawns is the central DEV question for any
re-entry rule.

## What the record says (from the inference note — ingredients, not parameters)

* Crash exit: de-lever from 2–3x to ≤1x within 1–2 sessions after two consecutive −3% days (Feb-2020), but tolerate a
  single −3% day in a calm regime (Aug-2019) and −0.5…−1.7% days at 3x (Feb-2025). Trailing-vol thresholds are late.
* Re-entry on volatility DISSIPATION while vol is still high (VIX 61, 25% below its peak, RSI(2)=8, RV10 103% on
  23-Mar-2020), not on calm; then ≥14 of 21 days at 3x with VIX 31–57 in Apr-2020.
* Leverage tiered by regime (~1.2x when VIX<13, ~0.7x at VIX 20–30) but the crisis-rebound months carry the highest
  leverage — exposure is not monotone in the vol level.
* Hysteresis long enough to sit out whole months (three 0.00% months); more up-days spent in cash than down-days avoided.
* Ruled out by the record: slow trend gate (below SMA200 every day of Mar/Apr-2020 and Jul/Oct/Nov-2022 while Demeter
  earned +55/+30/+11/+10/+5%), vol-LEVEL gating, within-month fixed exposure, ungated 1-day mean reversion.
* Targets: cash 48–52% of days; leverage mix of 1x and 3x averaging 1.5–2.2x invested; up-capture ≥100%,
  down-capture ≤40%; up-beta 1.0–1.4, down-beta ≤0.45; worst month ≥ −14%.
* The losses in Demeter's record are whipsaw at 3x in calm months, not crash losses. A rule with a quick
  exit/quick re-entry pays for its crash protection in chop; quantify that cost in DEV.

You are NOT required to reproduce Demeter. You are required to build a strategy that is good in its own right and
that survives 1950/1990–2012. If your lens turns out not to work in DEV, say so plainly — a well-documented failure
with the reason is a deliverable of equal standing.

## Deliverables (all under the model dir)

1. `signals/<name>.py` per the contract.
2. `dev_results/<name>.json` (final harness run WITH plateau) and `dev_results/<name>_grid.csv` (your grid).
3. `dev_results/<name>_DESIGN_NOTE.md` with these sections, in this order:
   *Mechanism* (why it should work, written BEFORE any run) · *Rules* · *Parameters and how each was chosen*
   (window, grid ranges, why this point) · *Grid summary* (n combos, plateau share, where the cliffs are) ·
   *Gate results* (paste `gate_check.py` output) · *Stress narrative* (1987, 1998, 2000-02, 2007-09, 2009 recovery,
   2010, 2011 — what the model did and why) · *Spurious re-entry census* · *Event ladders* for 2008-10-10, 2008-11-20,
   2009-03-09, 2002-10-09 · *Iteration count* · *Honest weaknesses and the regime that would break it* ·
   *Bugs found in shared code* (or "none").
4. Your final message: a JSON object (schema in the task prompt) — no prose outside it.
