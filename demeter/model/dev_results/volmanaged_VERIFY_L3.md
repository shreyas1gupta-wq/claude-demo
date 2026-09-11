# volmanaged — L3 verification (Mechanism & execution), pass 2, adversarial verifier

Scope: L3 only (mechanism validity, execution realism, regime sensitivity, Demeter-resemblance claims). Read
`signals/volmanaged.py` in full, `dev_results/volmanaged.json`, `dev_results/volmanaged_DESIGN_NOTE.md`,
`dev_results/volmanaged_VERIFY.json`. All numbers below are either copied verbatim from those files or produced by
small ad-hoc scripts against `engine.py`/`features.py` (never `evaluate.py`, never `results/`), listed inline.
Default posture per the brief: refute unless the evidence clears the bar.

## SEVERE — the claimed variance-timing mechanism does not survive the textbook-correct null on 43 of the 62 years of DEV data

The design note's mechanism claim (§1) is precise: *"the Sharpe-maximising rule ... is exposure proportional to
mu/sigma_t^2 ... scaling exposure inversely to forecast variance raises the Sharpe ratio ... over buy-and-hold."*
Because the model's average leverage is well below 1x (0.63x in dev_1990, 0.94x in dev_1950 per the JSON), the
brief's own question applies directly: is the reported Sharpe gain over buy-and-hold real timing skill, or just
the well-known fact that a lower-vol blend of a risky asset and cash can look better than the naive 100%-invested
comparison? The correct null for "does variance-timing add value" is NOT buy-and-hold, it is a **constant-leverage
portfolio held at the same average exposure** (this is the exact benchmark Moreira & Muir themselves use). I built
that null directly with `engine.run()` (same cost/financing/window as the harness; reproduced the official
dev_1990/dev_1950 Sharpes exactly first — 0.49458.../0.36164... match the JSON bit-for-bit — before trusting the
comparison):

| window | actual (time-varying) rule | constant-leverage null at the rule's own avg exposure | 1x buy-and-hold |
|---|---|---|---|
| dev_1990 (avg lev 0.6310) | **Sharpe 0.4946**, maxDD -19.80% | Sharpe 0.4024, maxDD -34.10% | Sharpe 0.3851, maxDD -50.78% |
| dev_1950 (avg lev 0.9445) | **Sharpe 0.3616**, maxDD -48.64% | Sharpe 0.4711, maxDD -48.49% | Sharpe 0.4705, maxDD -50.78% |

(Engine mechanics checked before trusting this: `d["ret"] = rf + pos*x - lev_fin - cost` and Sharpe is computed on
`m - rf_m`, i.e. excess-of-cash — so a *constant* leverage multiplier should leave Sharpe exactly unchanged from
buy-and-hold's, which is exactly what the middle column shows, 0.4024≈0.3851 and 0.4711≈0.4705; this confirms the
comparison is measuring genuine timing value, not a rf-credit artifact.)

**Reading:** in dev_1990 the rule beats its own matched-risk null by +0.092 Sharpe (23%) and cuts maxDD by 14.3
points vs the null — real, substantial timing value, consistent with the design note's pre-registered prediction
of a "0.05-0.15" edge over buy-and-hold. But in dev_1950 the rule *loses* to its own matched-risk null by -0.11
Sharpe (23% worse) and gives up essentially all of the drawdown benefit that a same-average-exposure static
position already provides for free (-48.64% vs -48.49%, a 0.15-point difference — i.e. on this longer sample the
"crash protection" is coming almost entirely from running less average risk, not from timing when to run it).
Since dev_1950 = dev_1990 plus 1950-1989, this means **on the 1950-1989 portion of the very sample this candidate
was cross-checked against, the timing component is neutral-to-negative, not positive** — the mechanism claimed in
§1 of the design note is empirically false outside the 22-year window the five parameters were tuned on.

This matters for a different reason than the coordinator's sub-sample-Sharpe note (which is an L2 stability
question about the *level* of Sharpe). This is an L3 mechanism question: the parameters were selected by comparing
DEV_1990 Sharpe across a grid (design note §3, "all five tunables were chosen on dev_1990"), and the resulting
rule's edge over a fair, risk-matched baseline is concentrated entirely in that same window — the mechanism
"reacts to variance persistence" is doing real work only in 1990-2012 and literally net-detracts in 1950-1989. A
mechanism whose value appears exactly in its own selection window and reverses sign outside it is the textbook
overfitting signature, independent of the (separately, honestly reported) DEV Sharpe decay across halves/thirds.
**Tag: SEVERE** — this refutes the design note's central causal claim ("the same rule mechanically cuts crash
exposure" / "raises the Sharpe ratio") as a property of the mechanism itself, on more than two-thirds of the
candidate's own development history, using the correct (not naive) counterfactual.

## MATERIAL — the asymmetric band, once triggered into a deep de-lever, freezes for years (quantifying design-note §10 item 4)

The design note already found and correctly derived (§10 item 4) that `H_{t-1} - T_t > band_dn` can never fire
once `H_t <= band_dn = 0.30`, because `T_t >= 0` always. I confirm the derivation is exactly right by reading
`_core()` line by line (`cur - t[i] > bd` with `t[i]>=0`, `cur<=0.30` ⇒ LHS `<=0.30` ⇒ condition can only be
false-or-equal, never `>`). What the design note does **not** quantify is how long this actually lasts and how
close the *other* side of the band came to firing. I computed the run-length of the held level directly from the
signal series (2008-2012 segment):
```
2008-08-01 .. 2008-09-16: held 0.5362
2008-09-17 .. 2012-06-29: held 0.2011   <- 955 trading sessions, ~3.75 years, unbroken to DEV_END
```
and the *raw* (pre-band) target `T_t` over that same frozen window: max 0.7797 (2011-07-26, just before the
Aug-2011 debt-ceiling vol spike pushed it back down), min 0.0279 (2008-10-28). The re-lever threshold from a base
of 0.2011 is `0.2011 + band_up(0.75) = 0.9511` — the raw target came within 0.17 of it (at 0.78) but because
`band_up` is an *absolute* leverage-unit threshold rather than a proportional one, re-levering from a base this
low requires the raw target to rise to **~4.7x the currently-held level**, i.e. requires forecast variance to fall
by a factor of ~22 (since T ∝ 1/sigma²) from where it stood in Sept 2008. That did not happen before DEV_END.
Net effect: for the entire Lehman-to-DEV_END span the model is not "cutting exposure through the crisis and
re-levering as it resolves" (the mechanism section's framing) — it takes exactly one action (mid-Sep-2008) and is
then mechanically incapable of reacting again in either direction for the rest of the sample, including through
the Oct/Nov-2008 acceleration, the Mar-2009 low, the entire 2009 recovery, the 2010 flash crash and the 2011
debt-ceiling event (all five of these appear in `event_ladders` at the *identical* 0.20106x value). The design note
calls this "reasonable... it caps whipsaw," which is defensible as a design choice, but the magnitude (a single
lock lasting 3.75+ years, spanning five separate named stress episodes) is disclosed only qualitatively in the
design note and not at all in the module docstring. **This must be stated numerically in RESULTS.md** — not as
"the band can't de-lever twice" but as "the rule took its last 2008 action in mid-September and was mechanically
frozen at 0.20x through DEV_END (Jun-2012), a specification property of the asymmetric band, not a bug — the
model's code matches its own docstring exactly at every step of `_core()`."

Verdict on the coordinator's framing question ("specification quirk to disclose, or implementation defect that
contradicts the docstring"): **specification quirk, not a defect.** The docstring's own description of the band
rule (§3 of the module doc) is implemented exactly as written; nothing in `_core()` diverges from
`H_t = H_{t-1}` unless `T_t - H_{t-1} > band_up` or `H_{t-1} - T_t > band_dn`. The one-way-ratchet-toward-frozen
behavior is a mathematical consequence of that formula once combined with `T_t >= 0`, correctly identified by the
design note. It is MATERIAL because of its duration and because it means the rule's crash *behavior* is entirely
determined by the single largest early move in a drawdown, with zero subsequent reactivity — a materially
different risk profile than "volatility-managed leverage" suggests to a reader who hasn't traced the band math.

## MATERIAL — ~1/3 of position changes land on days with |return| > 2%, a ~4x overrepresentation vs base rate

Direct count (dev_1990, `df["spx_ret"]` on the exact days the held level changes): 14 of 40 position changes
(35%) occur on a day with `|spx_ret| > 2%`, against a base rate of 8.0% of all days (454/5672) — a ~4.4x
enrichment. dev_1950 shows the same pattern at similar magnitude (47/159 = 30% of changes on such days). This is
mechanically expected (a rule driven by realised variance will naturally be triggered on the days that move
variance the most) but it is exactly the execution-realism concern the brief names: trading into an already-large
same-day move. The size of these particular changes is moderate (0.3-0.6 leverage units observed in the detail
list, e.g. 1993-02-16 −2.52% day: 1.845x→1.360x; 2008-09-17 −4.50% day: 0.536x→0.201x) — none of the 14 dev_1990
big-move-day changes involve the 3x cap. Aggregate cost impact is small: doubling headline costs to the
`windows_stress_cost_6_90` scenario (6bp/90bp) only drags dev_1990 Sharpe from 0.4946 to 0.4860, because total
turnover is tiny (1.78 changes/yr). **Disclose the 35%/30% figures in RESULTS.md** as the honest answer to "how
many position changes happen on high-move days," but the low absolute trade count means this does not on its own
threaten the reported cost assumptions.

## Clarifying (not a defect) — the "3x entries at the close of high-vol days" concern cannot occur by construction

Checked directly: leverage ≥2.5x occurs on 12.4% of days in 1950-1969 (the only era where it is meaningfully used;
0% in 1970-1989 and 1990-1999, 0% in 2000-2012H1 at the ≥2.5x bar; max in 1990-1999 is 2.41x). Because
`T_t = (target_vol/sigma_t)^2`, high leverage requires *low* forecast variance — the rule structurally cannot be
near its 3x cap on a high-realised-vol day; the two conditions are mutually exclusive by the functional form. The
brief's specific execution worry (margin at 3x, gap risk, clustered slippage, entered at the close of a high-vol
day) therefore cannot arise for this signal's mechanism; the real execution risk is the moderate (not extreme)
band-crossing trades identified above, not 3x-notional entries. Worth stating in RESULTS.md as a resolved concern
rather than leaving the brief's question open.

## Pass — Demeter-resemblance discipline

Design note §1 explicitly disclaims reproducing Demeter's 2020 record ("The record's Apr-2020 ... is not something
this lens can reproduce; it is the opposite of its mechanism. I am not attempting to reproduce Demeter.") — this
satisfies the brief's specific check. No vol-LEVEL gate is used as an invest/cash decision (the signal is a
continuous inverse-variance scale, never binary in/out except during the 20-day warm-up: `pct_days_cash = 0.0%`
in both windows). No trend filter, no price-level input — confirmed by reading `_core()`: only `ret`, `sig`,
`band_up`/`band_dn` and the (disabled) shock/weekly knobs are used. Family label ("volatility-managed leverage
... two-horizon vol, asymmetric band") accurately describes the mechanism; no over-claim found.

## Pass (with caveat) — not the pass-1 trap "in disguise"

The rule structurally re-levers only after forecast variance has already fallen (trailing estimator) — the same
general shape as the pass-1 trap ("buys after implied vol has just fallen"). The difference from a trap is that
this is declared as the mechanism itself, not hidden: design note weakness #2 ("late re-entry... vol stays high
for months after a low... will miss most of the 2009 rebound") names it before any run, and the 2009 stress
episode (+11.4% vs SPY +67.4% at constant 0.20x, per `stress_episodes.2009_recovery`) confirms the prediction
exactly. Disclosed, predicted, and consistent with what the rule does — not a disguised defect.

## Regime sensitivity

- **Historical DEV regime that breaks it:** 1970-1989 (`eras` in the JSON): Sharpe 0.101 vs SPY 0.283, CAGR 8.40%
  vs SPY 11.47% — the rule is worse on both raw and risk-adjusted return despite a better maxDD (-27.1% vs
  -42.7%), i.e. a grinding, moderate-vol, directional bear-then-recovery era with no single deep crash to reward
  variance-timing pays the band's turnover/whipsaw cost and forgoes upside without a payoff. This is also the era
  the `hl=20` best-Sharpe cell was rejected for (design note §4), i.e. the designer already knew this era was the
  tight constraint.
- **Plausible future regime:** an extended low-realised-vol bull market punctuated by short, sharp
  vol spikes that do not become genuine bear markets (2017-2019-style: VIX in the low-to-mid teens most of the
  time with episodic spikes such as Feb-2018's vol-product unwind) — each spike would trigger a de-lever (the
  fast EWMA leg reacts quickly) that costs relative participation once the market resumes its grind higher and
  the slow EWMA leg holds the lower leverage for months (per the design note's own "fast up, slow down"
  description), reproducing the 1970-89 shortfall pattern in a modern low-vol-regime.

## required_disclosures (paste-ready)

1. On the matched-risk null (constant leverage at the rule's own average exposure), the variance-timing mechanism
   adds +0.092 Sharpe (23%) over dev_1990 but **subtracts** 0.11 Sharpe (23%) over dev_1950 relative to that same
   null — the claimed mechanism only adds value inside the window its five parameters were tuned on.
2. The asymmetric band froze the held level at 0.201x for the entire 2008-09-17 through 2012-06-30 span (3.75
   years, spanning five separate stress episodes in the record), and the raw target came only as close as 0.78
   against the 0.951 needed to re-lever — a specification property of the band math (matches the docstring
   exactly), not a code defect, but one whose multi-year duration is not quantified anywhere the reader would see
   it before RESULTS.md.
3. 35% of dev_1990 position changes (30% in dev_1950) land on days with |S&P return| > 2%, a ~4x enrichment over
   the 8% base rate of such days, though the aggregate cost impact is small given only 1.78 changes/yr.
4. The rule beats buy-and-hold Sharpe only in 1990-2012; on the full 1950-2012 sample its Sharpe (0.362) is below
   buy-and-hold's (0.470) and even below a constant-leverage portfolio held at the rule's own average 1950-2012
   exposure (0.471) — i.e. on the longer sample its lower average risk does the work a static position would have
   done for free, and its active timing does not add anything.
