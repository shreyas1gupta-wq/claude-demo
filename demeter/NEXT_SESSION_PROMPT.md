# Prompt for a fresh Claude Code (Fable 5.1) session

Copy everything between the rulers into a new session. Attach or link the two dashboards:

* Strategy overview — https://claude.ai/code/artifact/b7695d79-97b6-4a97-92fc-cc8d6a2018ef
* Replication study — https://claude.ai/code/artifact/db9bc7b3-2378-4270-8954-8680dba8cd5d

Repo: `shreyas1gupta-wq/claude-demo`, branch `claude/demeter-tactical-overview-vgw5sk`, everything under `demeter/`.

---

## MISSION

Reverse-engineer the Demeter Tactical "Dual-Engine Quantitative Equity Strategy" and build the best
rules-based daily strategy you can that survives honest out-of-sample testing. A previous session already
did one full pass; your job is to beat it, and to be candid when you cannot.

The strategy switches daily (3:59 PM New York) between levered long S&P 500 / NASDAQ futures at 2:1–3:1
and 100% cash. Live since July 2012. Published record, Share Class B, Jul 2012 – Jun 2026:
**31.08% a year, −13.65% maximum drawdown, Sharpe 1.27, up-capture 115%, down-capture 28%, ~50% of
trading days in cash, positive on only ~31% of days.**

## START HERE — DO NOT REBUILD WHAT EXISTS

Clone the repo and read, in this order:

1. `demeter/model/RESULTS.md` — the previous study's findings, leaderboard and limitations.
2. `demeter/model/results/demeter_inference.md` — a quantitative inversion of the published monthly
   returns into implied daily behaviour. This is the most valuable file in the repo. Do not re-derive it.
3. `demeter/model/engine.py`, `features.py`, `evaluate.py` — the backtest engine, causal feature library
   and standardised evaluator. **Reuse them.** If you find a bug, fix it and say so loudly, because every
   number in the existing study depends on it.
4. `demeter/model/data/PROVENANCE.md` — where the market data came from and what is wrong with it.
5. `demeter/analytics.json` — the published record recomputed and reconciled (142 of 144 published
   statistics match within tolerance).

Then run `python3 evaluate.py signals/final_model_fewtrades.py` to confirm you reproduce the incumbent.

## COST ASSUMPTION — THIS IS A HARD REQUIREMENT

Use **1.5× realistic transaction costs as a margin of safety** in every headline number you report.

Realistic for E-mini S&P futures, measured and sourced:
* Trading: ~2 bp of notional per unit of leverage traded (commission + exchange fees + half-spread).
* Financing: the levered leg pays above the risk-free rate. Measured directly in this dataset, actual
  E-mini returns lag "total return minus T-bill" by 32–51 bp a year (`data/dataset_checks.json`).
  Call it 40 bp.

So your **headline case is `--cost-bps 3 --fin-bps 60`.** Report the un-multiplied case (2 bp / 40 bp) as a
secondary row only. Also stress-test at `--cost-bps 6 --fin-bps 90` and state where the edge dies.
A strategy whose advantage disappears between 3 bp and 6 bp is not a strategy.

Note the two asymmetries in your favour that you must NOT quietly bank: our engine credits cash at the
actual T-bill rate whereas Demeter books cash at 0%, and slippage is modelled as a constant when regime
switches actually cluster on the most volatile, widest-spread days. If you want credit for beating
Demeter, subtract the T-bill advantage first and say so.

## THE BAR TO BEAT (all at 1.5× costs, Jul 2012 – Jan 2026, S&P 500 total return)

| | Annualised | Sharpe | Max DD | Changes/yr | Down-capture |
|---|---|---|---|---|---|
| **Demeter (published, the target)** | **31.3%** | **1.27** | **−13.65%** | daily | **23%** |
| Incumbent: `final_model_fewtrades` | 16.78% | 0.73 | −20.5% | 9.2 | 146% |
| `baseline_volregime` (higher turnover) | 21.70% | 0.83 | −30.9% | 10.1 | — |
| SPY buy & hold | 14.7% | 0.95 | −23.9% | 0 | 100% |

You beat the incumbent only by improving **risk-adjusted** return without inflating turnover or drawdown.
Raising leverage until CAGR looks bigger is not an improvement. Note SPY's Sharpe (0.95) exceeds every
model built so far — closing that specific gap is the real prize.

## NON-NEGOTIABLE METHODOLOGY

1. **Causality.** Only trailing/expanding computations. No centered windows, no full-sample z-scores or
   quantiles, no model fitted on data past the decision date. Statistical models (HMM, ML) must refit
   walk-forward on expanding windows ending before the decision date, at most monthly, using filtered
   (never smoothed) state probabilities. Every candidate must pass `E.lookahead_check` at five cut-offs.
2. **Development vs out-of-sample.** Choose and freeze every parameter using data ending **2012-06-30**.
   The Demeter live window is out-of-sample: evaluate each final candidate on it **at most three times**,
   and state in your report how many times you looked. Tuning on the out-of-sample window is the one
   unforgivable error here.
3. **Parameter budget: at most 6 tunable parameters per model.** Prefer a plateau in the sensitivity grid
   over a peak; report the share of ±15%/±30% perturbations that hold Sharpe within 25% of base.
4. **Never use Demeter's monthly returns as a model input.** They may inform which *ingredients* you try;
   they may not enter the signal.
5. **Report failures as prominently as successes.** A candidate that fails is evidence, not waste.

## THE TRAP THAT ALREADY CAUGHT ONE MODEL — DO NOT REPEAT IT

The rule that best fits Demeter's record after 2012 is "hold 3× while VIX is below its 10-day average,
else cash". It returns **+18.3% a year out of sample** — and **−5.7% a year with a 92% drawdown across
1990–2012**. Buying when implied volatility has just fallen is buying after up days: a tailwind in a
fourteen-year bull market, a whipsaw machine through 2000–02 and 2008.

Every promising idea must therefore be run over **1950–2012 and 1990–2012** before you believe it.
If a rule needs the post-2012 regime to work, say so and discard it.

## WHAT THE RECORD IMPLIES (from the inference file — use it, don't re-derive it)

Ingredients the published record supports, ranked:

1. **Fast asymmetric de-levering on a downside volatility shock.** February 2020 is consistent with holding
   1.5–2× through the first shock days and cutting within one to two sessions of the second — the month
   landed at −13.65%, not the −22% that 3× held throughout would produce. A single −3% day in a calm
   regime (Aug 2019) did NOT fire it.
2. **Re-entry on volatility *dissipation*, not on calm.** Every path reproducing March 2020 (+55.32%) is in
   cash 6–20 March and at 3× on 24–26 March, with VIX above 60 and realised volatility above 80%.
   Implied exposure correlates −0.30 with the *change* in VIX within the month and +0.03 with the VIX
   *level* at month start.
3. **Leverage tiered by volatility regime** — about 1.2× when VIX < 13, about 0.7× when VIX is 20–30, but
   the crisis-rebound months carry the highest constant-equivalent leverage of all.
4. **Hysteresis long enough to sit out whole months** — three months print exactly 0.00%, and the manager's
   own quadrant counts show more up days spent in cash (883) than down days avoided (804).
5. **Short-horizon timing at high leverage inside calm regimes** — this is also where the losses come from:
   eight of the twelve worst months had SPY down only 0.3–2.7%.

Ruled out by the record: a slow trend filter as the invest/cash gate (the index was below its 200-day
average on every single day of March 2020, April 2020, July 2022, October 2022 and November 2022 — months
Demeter earned +55.3%, +29.7%, +10.6%, +10.0%, +5.3%); volatility-*level* gating; any exposure fixed within
the month; and ungated one-day mean reversion.

Quantitative targets a candidate should aim at: cash 48–52% of days · leverage mix of 1× and 3× averaging
1.5–2.2× when invested · up-capture ≥ 100% · down-capture ≤ 40% · up-beta 1.0–1.4 with down-beta ≤ 0.45 ·
positive monthly skew · worst month no worse than −14%.

## WHERE THE PREVIOUS PASS FELL SHORT — YOUR ACTUAL TARGETS

The incumbent's failure is **entirely on the downside**: up-capture 133% (fine) against down-capture 146%
(hopeless, versus Demeter's 23%). It is levered trend-following, not a dual-engine crash-avoider. Attack in
this order:

1. **Build a real crash exit.** Trigger on consecutive multi-sigma days plus an implied-volatility jump
   (VIX gapping above its own short average, or a VIX/realised-vol ratio spike), not on a trailing
   volatility threshold — trailing vol is always late. This single mechanism is the difference between 146%
   and 23% down-capture.
2. **Build a re-entry that is not a trend filter.** Trigger on VIX falling a set fraction from its trailing
   maximum while still absolutely high, combined with an oversold measure. Test explicitly whether it fires
   on 23–24 March 2020, 13 October 2022 and 26 December 2018 — and whether it also fires spuriously through
   2000–02 and 2008, which is where the previous VIX-based attempt died.
3. **Separate the two decisions.** "Am I in the market?" and "how much leverage?" should be different rules
   with different signals and different speeds. The previous models conflated them through a single
   trend gate.
4. **Cut whipsaw in calm chop.** Eight of Demeter's twelve worst months are whipsaw at leverage; the
   incumbent has the same disease. Minimum holding periods, hysteresis bands and a "do nothing unless the
   evidence is strong" default are cheap and were under-explored.

## DATA — READ THIS BEFORE YOU WASTE AN HOUR

The sandbox's egress policy blocks **Yahoo Finance, FRED, Stooq, CBOE, Nasdaq, Kaggle and Hugging Face**.
Only PyPI and GitHub (including `raw.githubusercontent.com`) are reachable. Do not burn time on
`yfinance`. Everything already assembled came through GitHub/PyPI mirrors — see `PROVENANCE.md` and reuse
`demeter/model/data/market_daily.csv` (35,289 daily rows, 1885-03-20 to 2026-02-11: S&P 500 price and
total return, 3-month T-bill, VIX OHLC from 1990, E-mini S&P and NASDAQ-100 futures, Fed funds futures).

Known gaps you must respect: daily index data ends **2026-02-11** and the T-bill ends 2025-12-19 (held flat
after), so model-vs-Demeter comparisons run **Jul 2012 – Jan 2026**, not to June 2026. Futures end
2024-03-28. The last 35 rows are extrapolated.

**The highest-value new data, if you can reach any mirror of it:** VIX futures term structure (VIX9D/VIX3M
or front-month basis), daily put/call or skew data, and intraday S&P bars. The inference shows Demeter's
re-entry happens *within a day of the low* — daily closes structurally cannot see it, and no amount of
cleverness on daily data will close that gap. If you cannot get this data, say so and stop claiming the
gap is closable with what you have.

## DELIVERABLES

1. `demeter/model/signals/<name>.py` for each candidate, self-contained, with a plain-English docstring of
   the rules, `NAME`/`FAMILY`/`HYPOTHESIS`/`DEFAULT_PARAMS`/`signal(df, **params)`, and a comment naming the
   development window each parameter was chosen on.
2. `results/<name>.json` from `evaluate.py` for each, at the 1.5× cost setting, plus the sensitivity runs.
3. An updated `RESULTS.md` and a rebuilt `report/index.html` (`build_report.py` regenerates it) with the new
   leaderboard, honest DEV-vs-OOS comparison, cost sensitivity at 3/6 bp, and a section on what failed.
4. A short "what changed and why" note at the top of `RESULTS.md` so a reader can diff against this pass.
5. Commit to the branch with clear messages. Do not open a pull request unless asked.

## ACCEPTANCE CRITERIA

A candidate is only a success if, at 3 bp trading cost and 60 bp financing:

* it passes `E.lookahead_check` at all five cut-offs;
* its parameters were frozen on pre-July-2012 data, and you can say how many times you looked at OOS;
* out-of-sample Sharpe beats the incumbent's **0.73** *and* out-of-sample max drawdown is no worse than
  **−20.5%** *and* position changes stay under about 25 a year;
* it is not ruinous in 1990–2012 or 1950–2012 (no era where it loses money or draws down more than ~40%);
* its edge survives at 6 bp / 90 bp, or you state plainly at what cost level it dies.

## HONESTY CLAUSES

* If nothing beats the incumbent, say so in the first paragraph of `RESULTS.md`. That is a legitimate and
  useful result, and it is more valuable than a curve-fitted "win".
* Count and disclose how many candidates you built. Six models against one out-of-sample window is already
  a multiple-comparison exercise; twenty would be a farce. Keep the panel small and deliberate.
* Never report a backtest number without its cost assumption attached.
* Demeter's returns are the manager's published figures, not audited. Note that the published four-quadrant
  day counts sum to 3,477 against a stated total of 3,219 trading days.
* Distinguish clearly between "this model reproduces Demeter" (it does not — monthly correlation with the
  published record is only 0.38) and "this model is a good strategy in its own right".
