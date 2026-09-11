# dissipation_reentry — L2 verification (Overfit & plateau), pass 2

Verifier: independent L2 sceptic. Evidence below is copied from `dev_results/dissipation_reentry_VERIFY.json`,
`dev_results/dissipation_reentry_grid.csv` (= grid 3, 216 rows, the grid the frozen params come from), the
design note, and one DEV-only isolation-script run I made myself (`--tag verify_L2_peak`, not overwriting the
designer's files). No `evaluate.py`, no `results/`, no data past 2012-06-30, no signal edits.

## Finding 1 — SEVERE: G2 is passed entirely by a 7-trade re-entry overlay; the structural base alone is
SPY-equivalent and fails G2

From the design note's own REBOUND-off ablation (iteration 617, `_bursts_frozen.csv`), reproduced in
`_VERIFY.json`/design note:
* Base engine (flat-1x RV21<15% gate, no re-entry): dev_1990 **Sharpe 0.389** — below the G2 bar (0.4253) and
  essentially identical to buy-and-hold SPY's dev_1990 Sharpe of **0.39**.
* Frozen candidate (base + 7 REBOUND bursts, 1990–2012H1): **Sharpe 0.447**.

So the entire margin over the gate (+0.058 Sharpe, the difference between "fails G2" and "passes G2 with room to
spare") is produced by exactly 7 discrete calendar trades in 22.5 years (2001-10-29, 2002-08-28, 2008-12-19,
2009-01-09, 2010-06-29, 2011-09-02, plus one more per the era table). That is not a plateau of skill; it is a
handful of dated events.

## Finding 2 — SEVERE: the grid's own maximum is a one-trade peak, and 82% of the gate-passing region shares the
setting that produces one-trade peaks

I ran the isolation script myself on the grid-3 row with the highest dev_1990 Sharpe in the 216-row grid
(`rv_exit=.13, vix_fall=.25, vix_win=20, vix_min=35, hold_days=10, stop_loss=.08`, grid Sharpe **0.5115**,
`dev_results/dissipation_reentry_bursts_verify_L2_peak.csv`):

```
bursts 1990-2012H1: 1   (2008-12-19, +18.12% net, the only fire in 22.5 years)
dev_1990 with bursts:    Sharpe 0.511
dev_1990 REBOUND off:    Sharpe 0.428
```

One trade moves Sharpe by +0.083. This is the grid's global maximum, entirely a single-trade artifact — confirming
the design note's own diagnosis of the `vix_win=20` region ("rejected as a one-trade peak").

But that region is not a small corner of the grid: of the 33/216 rows that pass all three DEV gate-proxies
(G2 Sharpe ≥ .4253, G3 maxDD ≥ -30%, G4 worst-era DD ≥ -40% & min-era CAGR > 0), **27 (82%) use `vix_win=20`** —
the one-trade-peak setting — and only **6 (18%)** use the frozen `vix_win=30`. (Counted directly from
`dissipation_reentry_grid.csv`: `Counter({'20': 27, '30': 6})` among the 33 passers.) The designer's frozen choice
is the minority, more-diversified end of the passing island (7 bursts instead of 1-2), which is the right call
given the one-trade-peak problem — but it means the *entire* gate-passing region of this design, majority and
minority alike, is a needle's-eye fit to whichever subset of a small number of known dated VIX-divergence events
(I count ≤10 distinct candidate dates across all of the note's grids and corners) gets captured, excluded, or
stopped out. G6's plateau statistic (79%/92%) measures *local* stability around the frozen point on 6 axes; it
says nothing about the fact that the *passing set itself* is this thin — 33/216 = 15.3% of the grid, all at
`rv_exit ∈ {.13,.15}` out of 6 tested values, i.e. a 2-cell-wide strip.

## Finding 3 — MATERIAL: deflated-Sharpe arithmetic puts the honest DEV read at ≈ noise

Bailey–López de Prado style reasoning. Estimator variance of an annualized Sharpe over dev_1990's ~22.5 years,
ignoring skew/kurtosis: `Var(SR) ≈ 1/T ⇒ SE ≈ 1/√22.5 ≈ 0.211`. Expected maximum of N i.i.d. zero-skill trials:
`E[max] ≈ SE·√(2 ln N)`.
* At the nominal grid size N=216: E[max] ≈ 0.211·√(2·ln216) ≈ 0.211·3.28 ≈ **0.69** — *higher* than the actual
  grid max (0.5115), which means the 216 cells are far from independent (confirmed by Finding 2: most of the
  variation is which of a handful of dated events fires).
* Rescaling to an honest **effective** number of independent bets — the ~8-10 distinct dated
  divergence events that actually drive every number in this design, not the 216-828 nominal parameter
  combinations — N_eff ≈ 10 gives E[max] ≈ 0.211·√(2·ln10) ≈ 0.211·2.15 ≈ **0.45**, which is *statistically
  indistinguishable from the frozen candidate's actual DEV Sharpe (0.447)*. In other words: given ~10 quasi-
  independent binary bets (does event X get captured net-positive or not) and 22.5 years of data, a Sharpe of
  ~0.45 is within the range pure search-driven luck would produce even with zero true skill. This does not prove
  zero skill, but it means the DEV number carries very little evidence of skill beyond what an honest deflation
  budget would expect from chance alone.
* Reading down: if the true residual skill is small, the expected OOS Sharpe reverts toward the structural
  floor (~0.35-0.40, i.e. Finding 1's REBOUND-off/SPY-equivalent level) minus some probability of landing on the
  wrong side of the `rv_exit` knife-edge (Finding 4) — see `expected_oos_sharpe_range`.

## Finding 4 — MATERIAL: the one parameter that matters (rv_exit) is a one-sided cliff, independently confirmed

From `dissipation_reentry_grid.csv`, marginal by `rv_exit` (36 rows each, all other params free):
`.12`→max 0.364, `.13`→max 0.512, **`.15`→max 0.465**, `.17`→max 0.275, `.18`→max 0.225, `.20`→max 0.347.
Sharpe falls off a cliff moving from .15 to .17 (max drops from 0.465 to 0.275) and only partially recovers at
.20 as the model re-enters something closer to a permanent 1x posture. The design note discloses this
("+15%/+30% perturbation drops Sharpe to 0.30/0.28") and the `_VERIFY.json` neighbourhood confirms it
(`rv_exit=0.17 → Sharpe 0.2753`, the single worst neighbour and the only one that fails the 25%-of-base plateau
test on the up side). G6 (0.79) passes only because the other 5 parameters are flat; it is carrying one cliff
parameter, exactly as the coordinator's brief flagged.

## Finding 5 — MATERIAL: sub-period instability — the calm 1990s carries the headline, the actual bear-market
third of DEV falls short of the gate bar

From `_VERIFY.json` `subsamples.thirds` (dev_1990, 1990-01-01 to 2012-06-30 split into three ~7.5y blocks):

| third | window | Sharpe | CAGR | maxDD |
|---|---|---|---|---|
| 1st | 1990-1997H1 | **0.693** | 11.7% | -8.0% |
| 2nd | 1997H2-2004 | **0.298** | 6.4% | -12.4% |
| 3rd | 2005-2012H1 | 0.393 | 5.6% | -8.0% |

The 2nd third (which contains the entire 2000-02 bear, the era this candidate is built around) scores 0.298 —
below the 0.4253 gate bar on its own, and below both halves and the full-period 0.447. The headline dev_1990
number is disproportionately carried by the pre-1998 calm bull run, where the model has zero bursts and simply
sits mostly in the RV-gate's 1x/cash pattern in a friendly regime (per the era table, 1990-1999 has 0 bursts).
Halves are milder (0.412 / 0.481) but the thirds split shows the concentration more clearly. This should be
disclosed alongside the headline Sharpe.

## Finding 6 — MINOR: design-note arithmetic error on the `vix_win` sensitivity claim

The design note's parameter table says: *"With 20 the frozen row has ONE burst (2008-12-19) and Sharpe 0.465 —
higher, rejected as a one-trade peak."* Checking `dissipation_reentry_grid.csv` for the row that is the frozen
params with only `vix_win` changed to 20 (`rv_exit=.15, vix_fall=.25, vix_min=30, hold_days=10, stop_loss=.10`)
gives **dev_1990 Sharpe 0.4067**, not 0.465 (0.465 is not attained by any row in the grid with those other five
params). The qualitative conclusion (reject vix_win=20 as a one-trade-peak setting) is directionally right and
independently confirmed by Finding 2 at a *different* corner of the vix_win=20 region, but the specific number
quoted does not match the shipped grid file. Immaterial to the freeze decision, but the note's numbers should be
internally reconciled before this ships to RESULTS.md.

## Structural-search scope (context for the deflation budget, not a separate finding)

The design note's "864 iterations" spans three materially different **structural** defaults tried in sequence —
tier 3/2/1 (grid 1, 324 combos, 0/324 pass G3/G4), tier 3/2/1 + stop-loss (grid 2, 288 combos, 0/288 pass G4), and
flat-1x + stop-loss (grid 3, 216 combos, 33/216 pass all three proxies) — where the structural choice itself was
changed specifically because the gates would not pass otherwise. That is a legitimate, disclosed DEV-informed
structural decision under the brief's rules, but it means the selection universe behind this candidate is not
"216 tunable combos," it is "3 structural variants × ~300 combos each, escalating until one clears G4." The
grid-based deflation in Finding 3 uses only the 216-row grid3 (the grid that could pass at all); using the full
828 nominal combos across all three structural searches would widen N further without changing the qualitative
conclusion (correlated cells, effective N still small).

## Answer to the coordinator's specific question

*"At rv_exit 0.17-0.20 the flat-1x default re-enters the 2000-02 bear and dev_1990 Sharpe collapses to 0.19-0.30
while G6 passes only because the other five parameters are flat"* — confirmed independently (Finding 4): grid
marginal max at `rv_exit=.17` is 0.275, at `.18` is 0.225 (design note's own perturbation numbers, 0.19-0.30, are
consistent with these grid marginals). G6 = 0.79/0.92 is real arithmetic but is dominated by 5 flat axes carrying
1 cliff axis, exactly as flagged.

## Verdict inputs
* SEVERE: Findings 1 and 2 (G2 pass is a 7-trade, largely single-trade-peak-region artifact).
* MATERIAL: Findings 3, 4, 5 (deflation arithmetic, rv_exit cliff, sub-period instability).
* MINOR: Finding 6 (note arithmetic mismatch).
