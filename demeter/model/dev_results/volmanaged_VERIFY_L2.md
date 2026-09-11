# L2 verification — volmanaged (Overfit & plateau), pass 2

Verifier: adversarial L2. Evidence from `dev_results/volmanaged.json`, `volmanaged_VERIFY.json`,
`volmanaged_grid.csv`, `volmanaged_DESIGN_NOTE.md`, and the frozen `signals/volmanaged.py` run directly
against `engine.load_market()` (DEV-truncated, ≤2012-06-30). No parameters proposed, no `evaluate.py` run.

## 1. Full-history (dev_1950) Sharpe REVERSES the dev_1990 edge — SEVERE

The five tunables were selected on dev_1990 (1990-01–2012-06); dev_1950 (1950-2012) is nominally a
"cross-check." The two windows do not merely differ in magnitude, they **flip sign relative to
buy-and-hold**:

| window | model Sharpe | SPY B&H Sharpe | model − SPY |
|---|---|---|---|
| dev_1990 (tuned) | 0.4946 | 0.3851 | **+0.110** |
| dev_1950 (cross-check) | 0.3616 | 0.4705 | **−0.109** |

(`dev_results/volmanaged.json` → `windows.dev_1990`, `windows.dev_1950`, `reference_bh_1x`.) Era breakdown
confirms this isn't noise: the rule under-Sharpes SPY in 3 of 4 eras — 1950-69 (0.51 vs 0.85), 1970-89
(0.10 vs 0.28), 1990-99 (0.81 vs 0.95) — and only wins in 2000-2012H1 (0.11 vs 0.02), the one era
containing both the dot-com and GFC bears (`windows`/`eras` in the same file; also stated as weakness #1
in the design note). The entire claimed edge of the frozen point is thus concentrated in a single
22-year sub-period that happens to contain two of the deepest US equity bears on record, and it exactly
cancels (same magnitude, opposite sign) once forty extra years of mostly-calmer history are added back
in. That is the textbook signature of a rule fit to a regime rather than a stable structural effect —
this should block confidence that the DEV Sharpe generalizes to an OOS window whose regime composition
is unknown.

## 2. Within-DEV sub-sample decay is monotone and severe on its own — SEVERE

`_VERIFY.json.subsamples` (dev_1990, 1990-01-02..2012-06-29):

* Halves: 0.729 (1990–2001-03) → **0.164** (2001-04–2012-06)
* Thirds: 0.869 (1990–1997-06) → 0.404 (1997-07–2004-12) → **0.094** (2005-01–2012-06)

The reported dev_1990 Sharpe of 0.495 is an average that is front-loaded almost entirely into the first
7.5 years; by the final third it has decayed to statistically indistinguishable from zero (Sharpe 0.09
on a moderate-vol third of the sample). Since OOS is chronologically *after* DEV, extrapolating a
monotonically decaying in-sample trend to the future is the opposite of a favorable prior.

## 3. Selection haircut: grid max sits inside the noise band expected from this many trials — MATERIAL / required disclosure

Design note §9: **806 distinct parameter sets** evaluated on DEV (540 + 216 grid combos + 61 manual
batch iterations + smoke/diagnostic reruns). `grid_audit.grid_max_sharpe = 0.6261`,
`frozen_sharpe = 0.4946` (rank 81/540, 85th percentile — not the peak, but well above median 0.445).

Using the Bailey–López de Prado asymptotic expected maximum of N iid trials against T=22.5 years of
DEV data (SE of an annualized Sharpe ≈ 1/√T ≈ 0.211):

| effective N (independence assumption) | E[max noise-only Sharpe] |
|---|---|
| 50 (heavy correlation across grid cells) | 0.44 |
| 150 | 0.53 |
| 400 | 0.60 |
| 806 (nominal, no correlation adjustment) | 0.64 |

Across the whole plausible range of effective-trial-count assumptions, the **expected maximum Sharpe
obtainable from pure multiple-testing noise (0.44–0.64) brackets both the observed grid max (0.626) and
the frozen point (0.495)**. This does not prove the edge is zero — the fact that the grid median (0.445)
also beats SPY B&H (0.385) argues for *some* structural effect shared across the whole grid (see §4) —
but it means the specific numeric level of the frozen Sharpe is not distinguishable from search luck at
this trial count, and no naive "806 trials, pick the best-looking robust point" defense survives contact
with the deflation arithmetic. This is a required disclosure regardless of the refutation verdict.

## 4. The asymmetric-band freeze is a structural bet on two episodes, not continuous variance-timing — SEVERE (extends the L1 finding with new evidence)

Confirmed independently by running `signal()` on `engine.load_market()`, not just from the docstring
math: the coordinator's note (and design-note §10 item 4) describe a freeze from Sep-2008 through
Mar-2009. Direct inspection of the leverage path shows a **much larger, undisclosed instance of the
same defect**:

```
target = 0.13957388434365128
mask = |signal - target| < 1e-6
count = 1667 trading days
first date = 1997-10-28
last date  = 2004-06-16
```

Leverage was pinned at **exactly 0.1396x for 6.6 continuous years** (1997-10-28 → 2004-06-16) — spanning
the back half of the dot-com bull run, the entire 2000-02 bear, and the first year of the recovery. This
is corroborated by `stress_episodes`: `1998_ltcm`, `2000_02_bear`, and `2002_03_recovery` all report
`avg_leverage` = 0.139574 to 8 significant figures — three nominally distinct episodes that are in fact
one uninterrupted frozen span. Thirds-subsample turnover confirms it: the 1997-07..2004-12 third shows
**0.267 position changes/year** (≈2 changes over 7.5 years) vs 3.46/yr in the first third.

Design-note §10 item 4 frames the artifact as "one emergency de-lever per crisis," implying a
crisis-scoped mechanism. The data show the freeze is not crisis-scoped: it persists across a full bull-
bear-recovery cycle with no re-trigger, because (per `long_mult=8` → slow halflife 104 sessions) the
docstring's claim that the rule "re-levers slowly" understates the actual behavior by roughly two orders
of magnitude — this is not "slow," it is "does not re-lever for most of a decade" under the realized
1997-2004 path.

Mechanically this matters for OOS expectations because of how the engine computes returns: `r_p = rf +
L·(spx_tr − rf) − lev_fin − cost` with `lev_fin = 0` for L ≤ 1. Under **constant** L this makes the
excess-return Sharpe algebraically **identical** to buy-and-hold SPX's Sharpe over the same stretch (up
to the small transition-cost drag) — so the entire 6.6-year frozen period is not "earning a variance-
timing premium," it is coasting at whatever B&H's Sharpe happened to be over 1997-2004 (which is exactly
why that stretch also happens to be the 0.40-Sharpe middle third in §2, decaying toward zero, not the
0.87 of the truly dynamic first third). The strategy's apparent edge over B&H therefore reduces to the
**timing of a small number of large, largely-fortuitous regime jumps** (into ~0.14x shortly before the
worst of the dot-com bust, and independently into ~0.20x in Sep-2008 before the GFC's second leg), not
to continuous responsiveness. A mechanism whose measured edge is dominated by 1-2 lucky jump timings is
inherently much less likely to repeat OOS than one earning a steady daily premium.

## 5. Answering the coordinator's direct question: is the Sharpe a low-exposure artefact?

Not mechanically, and not simply from the 0.63x average. Given the engine credits `rf` on the un-invested
fraction and applies no financing spread below 1x, Sharpe is invariant to a *constant* leverage multiplier
(shown algebraically in §4) — so low average exposure alone does not manufacture Sharpe the way "0.5x SPY
≈ SPY's own Sharpe" would trivially suggest if it did. What *does* drive the reported uplift is that the
low-exposure spells are **not randomly timed** — they happen to fall across the two most severe US bear
markets in the DEV sample. That is a much narrower and more fragile claim than "variance-timing generally
raises Sharpe," and it is exactly the claim that reverses sign in §1 once 40 years of history without a
comparable multi-year bear are added back in.

## 6. Plateau geometry (local) is genuine — this is the one clean result

`plateau_dev_1990`/`plateau_dev_1950`: all ±15–30% one-at-a-time perturbations on all 5 params stay within
25% of the frozen Sharpe in both windows (`share_within_25pct = 1.0` in both). `grid_audit.neighbourhood`
(8 one-step grid neighbours) likewise all stay within 25%. Locally the frozen point is not a razor's-edge
peak — this is a legitimate mitigant and should be disclosed alongside §1–4, not overridden by them.

## Summary

The frozen point is not an isolated spike in its immediate grid neighbourhood, but the Sharpe it reports
is (a) not reproduced, in fact reversed, over the 40 extra years available as a cross-check, (b) internally
decaying to ~0 over the back two-thirds of even the tuning window itself, (c) within the range of pure
multiple-testing noise given ~800 evaluated parameter sets, and (d) mechanically explained by one long
structural freeze plus two lucky regime-jump timings rather than continuous variance-timing. Each of
these is evidence for the same underlying conclusion — refute pending disclosure, do not grant the OOS
look on the current record.
