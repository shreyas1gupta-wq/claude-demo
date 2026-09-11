# composite_dual_engine — L2 verification (Overfit & plateau)

Independent adversarial review. All numbers below were re-derived from `dev_results/composite_dual_engine_grid.csv`
(243 rows, pandas) and `dev_results/composite_dual_engine_VERIFY.json` (the mechanical battery), cross-checked
against the designer's own `_DESIGN_NOTE.md`. No signal file was edited, no `evaluate.py` run, no `results/` file
touched, no data past 2012-06-30 loaded.

## 1. Peak vs plateau — rank, neighbourhood, grid share

Recomputed directly from the shipped 243-row grid (`v_calm x v_high x hyst x k x min_hold`, `out_days` fixed):

* `dev_1990_sharpe`: max **0.5481**, mean 0.4508, median 0.4538, std **0.0465**, min 0.3369.
* Frozen point (`v_calm 16 / v_high 23 / hyst 0.16 / k 4 / min_hold 10`) scores **0.5426 = rank 2 of 243**
  (99.6th percentile), 0.0055 below the top row (`v_calm 17 / v_high 23 / hyst 0.18 / min_hold 12`, Sharpe 0.5481,
  maxDD -23.85% — also better on drawdown). This matches `_VERIFY.json.grid_audit` exactly (independent
  recomputation, no discrepancy).
* 169/243 (69.5%) clear the G2 Sharpe bar alone; **152/243 (62.6%)** clear G2 AND G3 (maxDD) jointly — recomputed
  and matches `_VERIFY.json` bit-for-bit. So the *region* is genuinely good (a majority of a 5-parameter
  neighbourhood passes), not a single needle.
* One-step neighbourhood (`_VERIFY.json.neighbourhood`, 10 rows): min 0.429, max 0.5364, 100% within 25% of the
  frozen Sharpe. G6 (perturbation plateau) independently confirms this at 0.958 (23/24 perturbations within 25% of
  base; the one failure is `v_high` -15%).
* **Finding (MINOR):** the frozen point is not the grid's argmax — it is 2nd of 243, chosen from an earlier,
  narrower plateau grid (g3, 144 combos) on a neighbourhood-mean criterion, and the final 243-grid was built
  *around* that already-frozen point after the fact (per the design note's own account) rather than being the
  source of the selection. That is a defensible, honestly-disclosed order of operations and not a foul, but it
  means the final grid's "62.6% pass" statistic describes the *local* robustness of the chosen point, not the
  *global* search that produced it — see §3.

## 2. Sub-sample stability — the DEV Sharpe is front-loaded

From `_VERIFY.json.subsamples` (independently sanity-checked against the design note's own era table, which uses
different cut dates but shows the same direction):

| split | period | Sharpe | CAGR% | maxDD% |
|---|---|---|---|---|
| half 1 | 1990-01-01 .. 2001-03-31 | **0.692** | 15.6 | -25.6 |
| half 2 | 2001-04-01 .. 2012-06-30 | **0.400** | 7.3 | -23.5 |
| third 1 | 1990-01-01 .. 1997-06-30 | **0.877** | 21.3 | -25.6 |
| third 2 | 1997-07-01 .. 2004-12-31 | **0.323** | 7.0 | -23.5 |
| third 3 | 2005-01-01 .. 2012-06-30 | **0.357** | 6.6 | -20.9 |

Corroborating (design note's own numbers, different boundary): era 1990-1999 Sharpe 0.767 vs era 2000-2012H1
Sharpe 0.361 — same story from an independent cut.

**Finding (MATERIAL — required disclosure).** The headline dev_1990 Sharpe of 0.543 is carried by the first
~7.5 years (1990-1997, Sharpe 0.88, the low-VIX 3x-calm era the design note separately documents via "3x days by
year": 1993 and 1995 alone account for 475 of the 3x days). **Both later thirds (1997-2012, ~15 of the window's
22.5 years) individually score 0.32-0.36 — below the pre-registered G2 bar of 0.425.** Had the DEV window started
in 1997 instead of 1990, this candidate would not have passed gate G2 at all. This does not invalidate the
pre-registered gate (which is correctly evaluated on the whole fixed window per PREREG), but it means the reported
0.543 is not representative of "typical" 7-8 year stretches of this rule's own history, and the OOS window
(2012-2026) contains no repeat of a 1993-96-style multi-year sub-13-VIX calm regime with the 3x tier fully engaged
— the design note's own weakness #2 ("3x is a low-VIX-decade phenomenon... zero 3x days in 1997-2000 and 2003")
already says this in different words but never states the "would fail G2" consequence explicitly. It should be
stated in `RESULTS.md`.

**Caveat in the candidate's favour:** the below-bar thirds are not failures in absolute terms — they are the
periods where the model earns modest Sharpe *while avoiding SPY's disasters* (2000-02: model -14.4% vs SPY -47.2%;
GFC: model +3.4% vs SPY -54.8%, both from the design note's stress table). A 0.32-0.36 Sharpe next to a max
drawdown 25-30 points shallower than SPY's in the same stretch is not a broken model; it is a model whose
crisis-avoidance value doesn't show up in a point-Sharpe gate calibrated on the whole 22-year sample. Still, the
concentration is real and must be disclosed, not just implied.

## 3. Selection haircut — how many tries, what should we expect OOS

The design note's own iteration count (§Iteration count) totals **1,125 distinct DEV parameter sets** across four
grids (240+324+144+243), two 7-point candidate batches with 1-D sweeps (7+70+6+70), ablations (7+9), a 3-point
probe and the final run. Verified: this count is internally consistent with the files present in `dev_results/`
(`_g1_grid.csv`, `_g2_grid.csv`, `_plateaugrid_g3.csv`, `_sweep_P1.csv`, `_sweep_Q2.csv`, `_ablate_frozen.csv`,
`_ablate_smoke.csv`, `_pick1/2/3.csv` all present and match the described row counts where checked against the
shipped `_grid.csv`'s 243).

Two independent haircut estimates:

* **Within-grid dispersion.** Grid std of Sharpe = 0.0465 over 243 points; the frozen point sits 2.0 std above the
  grid mean (0.4508). A naive expected-max-of-N-iid-Gaussian-noise calculation (Bailey-Lopez de Prado deflation
  form, gamma=Euler-Mascheroni) with sigma=0.0465 gives an expected max of ~0.13 above the mean for N=243 and
  ~0.15 for N=1,125 — i.e. a fully-iid null would predict an even *higher* max than the 0.548 actually observed,
  which tells us the 243 grid points are **not independent draws** (adjacent points are highly correlated; the
  true number of *effectively independent* structural configurations tried is much smaller, plausibly single
  digits to low tens once the four grids' overlapping ranges and the two sweeps around correlated base points are
  collapsed). This means a literal DSR N-trial formula over-corrects here; the more informative number is the
  cross-sectional dispersion itself.
* **Sub-sample-based estimate.** Because the frozen point's headline Sharpe is a blend of one strong 7.5-year
  regime (0.88) and two ~7.5-year regimes at 0.32-0.36 (§2), and because the OOS window (2012-2026) is unlikely to
  reproduce a multi-year sub-13-VIX 3x-engaged regime as extreme as 1993-96 (VIX spent long stretches in the
  teens post-2012 too, e.g. 2013,2017, but the design note's own weakness #5 flags `v_high`/`v_calm` as boundary
  artefacts of the 1990-2012 VIX distribution specifically), a more representative "steady-state" estimate is the
  grid median/second-and-third-third range, **0.32-0.45**, before any further selection discount.

Combining (i) a plateau-region estimate of ~0.32-0.45, (ii) a residual haircut for the fact that the *region
itself* was located via ~1,125 evaluations and the frozen point was still picked to be in the top ~1% of the final
verification grid, and (iii) the well-known asymmetry that OOS live-parameter performance regresses toward the
mean more than DEV plateau statistics suggest (the frozen point's own two out of three DEV thirds already sit at
0.32-0.36, i.e. below-plateau performance is not a hypothetical — it happened twice in-sample):

**Expected OOS Sharpe range: 0.20-0.40**, most likely below the 0.425 DEV/G2 bar and well below the pre-registered
OOS acceptance bar of 0.73. This is a judgment call, not a formula output — the honest range is wide because the
grid dispersion (§3.1) and the sub-sample dispersion (§2) point to different central values (0.45ish vs 0.32-0.36
respectively) and neither can be sharpened further without touching OOS data.

## 4. Low-exposure / cash-artefact check

Brief's specific question: is the Sharpe just "0.5x SPY ≈ SPY" in disguise? **Checked and rejected.** A static
blend of any weight of SPY + T-bill has a Sharpe identically equal to SPY's own Sharpe (blending with a
zero-variance asset doesn't change the risky sub-portfolio's Sharpe). dev_1990 SPY Sharpe = **0.385**; the model's
Sharpe = **0.543**, despite average leverage of only 1.05x and beta-to-SPY of 0.51 (avg leverage when invested
1.81x, 42.0% of days in cash). Because the model's Sharpe is *materially above* SPY's own Sharpe while running
below-SPY average exposure, the outperformance cannot be a fixed-weight dilution artefact — it requires genuine
time-variation in exposure that is (on average, in DEV) timed correctly. Consistent with up-capture 85.4% >
down-capture 62.4% (asymmetric capture is the fingerprint of real timing, not of a static blend). This is a real,
verified finding in the candidate's favour and should be stated as such — but note it is itself measured on the
same front-loaded DEV window as §2, so the "timing skill" evidenced here is disproportionately drawn from the
1990-97 sub-period's clean regime transitions rather than uniformly present across the whole 22 years.

## 5. Turnover / cost robustness (secondary L2 check)

`_VERIFY.json.turnover_clustering`: only 6.6% of the 122 position changes land on top-decile-vol days (vs 10% base
rate) — turnover is not clustered into the expensive days, so the clustered-slippage stress (PREREG item 2,
cost_bps x max(1, RV21/15%)) should not be materially worse than the flat-cost number already reported
(6bp/90bp -> Sharpe 0.5175 per the design note). Not independently re-run (would require touching cost machinery
outside this lens's remit); flagged as consistent, not verified end-to-end.

## Findings summary

* **SEVERE: none.** No evidence of a spurious/isolated peak, no fabricated or inconsistent numbers (grid file,
  VERIFY.json, and design note all agree on every cross-checked figure), no sign that the plateau claim (G6=0.958)
  is false — it is genuine at the parameter level. The weaknesses found are about *temporal* concentration of the
  edge and the honest size of the OOS expectation, not about the DEV result being wrong or fabricated.
* **MATERIAL:**
  1. Two of three DEV thirds (1997-2012, ~15 of 22.5 years) score Sharpe 0.32-0.36, below the pre-registered G2
     bar of 0.425; the passing headline of 0.543 depends on the 1990-1997 sub-period (Sharpe 0.88). State this
     explicitly in RESULTS.md alongside the halves/thirds table above.
  2. The frozen point ranks 2nd of the shipped 243-point grid (99.6th percentile) after a total search of ~1,125
     DEV parameter evaluations across four grids and two sweeps; the honest expected-OOS-Sharpe range given this
     search intensity and the sub-sample dispersion is **0.20-0.40**, not the DEV headline of 0.543 — well short of
     the 0.73 OOS acceptance bar on a central estimate, though not impossible at the top of the range.
  3. (Carried from the design note, independently confirmed, restate for completeness) the 3x tier is
     era-concentrated (1992-96 and 2004-07 carry nearly all 3x days; zero in 1997-2000/2003), which is the
     mechanical reason behind finding (1).
* **MINOR:**
  1. The final 243-grid was constructed around the already-frozen point rather than being the source of the
     freeze decision (order-of-operations note, not a foul — disclosed in the design note).
  2. `_VERIFY.json` reports 122 position changes vs the harness JSON's 123 — a 1-count discrepancy, immaterial,
     likely a window-boundary artefact between the two scripts; not investigated further as it changes nothing
     material.

## required_disclosures (paste-ready)

1. The dev_1990 headline Sharpe of 0.543 is front-loaded: the 1990-1997 third of the window scores Sharpe 0.88
   while the 1997-2012 two-thirds score 0.32-0.36 each, below the study's own 0.425 gate bar.
2. The frozen point ranks 2nd of 243 in the shipped verification grid after a total search of ~1,125 DEV parameter
   evaluations; the honest expected out-of-sample Sharpe range is 0.20-0.40, materially below both the DEV
   headline and the pre-registered OOS acceptance bar of 0.73.
3. The model's 3x tier is concentrated in two low-VIX stretches (1992-96, 2004-07); a permanently higher-VIX
   future regime would degenerate it into a 1x/cash timer, and this is the structural driver of finding 1.
4. The model's Sharpe advantage over SPY (0.543 vs 0.385 on the same window) is not a fixed-leverage/dilution
   artefact — verified quantitatively — but the timing evidence behind it is itself concentrated in the same
   front-loaded 1990-97 sub-period as finding 1.
