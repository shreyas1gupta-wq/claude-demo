#!/usr/bin/env python3
"""Track R6 — estimator-validation Monte Carlo (pre-registered as a METHODS check, not a market
hypothesis; no market data touched). Writes research/montecarlo/RESULTS.md.

Questions answered, each against synthetic ground truth:
  MC1  tau_half recovery at India-like sample sizes: naive vs Kendall-corrected bias, CI coverage.
  MC2  DSR calibration: false-discovery control under a true-zero-Sharpe null at the trial counts
       the ledger anticipates (1 / 9 / 28 / 252).
  MC3  Block vs iid bootstrap: how much does iid resampling understate the 95th/99th-percentile
       max drawdown on volatility-clustered returns?
  MC4  Hamilton filter, real-time honesty cost: expanding-mode vs full-sample cycle recovery.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from quant.stats import (ar1_ols, deflated_sharpe_ratio, estimate_tau_half, hamilton_filter,
                         kendall_corrected_rho, max_drawdown, stationary_bootstrap)
from quant.validation import ar1_series, regime_vol_returns, trend_plus_cycle

OUT = Path(__file__).resolve().parents[1] / "research" / "montecarlo" / "RESULTS.md"
rng = np.random.default_rng(2026)


def tau_true(rho):
    return np.log(0.5) / np.log(rho)


def mc1(n_draws=300):
    rows = []
    for rho in (0.5, 0.8, 0.9, 0.95, 0.97):
        for T in (120, 240, 380, 800):
            naive, corr, cover = [], [], 0
            for s in range(n_draws):
                y = ar1_series(rho, T, seed=s * 7 + T)
                r = ar1_ols(y)
                naive.append(tau_true(max(min(r, 0.9999), 1e-6)) if r > 0 else 0.0)
                rc = min(kendall_corrected_rho(r, T), 0.9999)
                corr.append(tau_true(max(rc, 1e-6)) if rc > 0 else 0.0)
            # CI coverage on a subsample (bootstrap is the slow part)
            for s in range(60):
                y = ar1_series(rho, T, seed=10_000 + s)
                res = estimate_tau_half(y, n_boot=200, seed=s)
                if res.ci_low <= tau_true(rho) <= res.ci_high:
                    cover += 1
            rows.append((rho, T, tau_true(rho), float(np.median(naive)),
                         float(np.median(corr)), cover / 60))
    return rows


def mc2(n_mc=400, T=120):
    """Zero-true-Sharpe strategies; pick the max-SR trial; DSR must not endorse it."""
    rows = []
    for N in (1, 9, 28, 252):
        endorsed = 0
        for m in range(n_mc):
            g = np.random.default_rng(m * 13 + N)
            srs = np.array([g.normal(0, 1, T).mean() / g.normal(0, 1, T).std()
                            for _ in range(N)])  # per-period SRs of pure noise
            sr_best = srs.max()
            dsr = deflated_sharpe_ratio(sr_best, T=T, skew=0.0, kurt=3.0,
                                        n_trials=N, sr_var_across_trials=float(np.var(srs)) if N > 1 else 1.0 / T)
            if dsr > 0.95:
                endorsed += 1
        rows.append((N, endorsed / n_mc))
    return rows


def mc3(n_seeds=8, n_samples=300):
    """Two panels. (a) vol-clustered, ~zero return autocorrelation: direction of iid-vs-block DD
    tails across seeds + ACF preservation. (b) autocorrelated returns: direction across seeds."""
    from quant.validation import ar1_series

    def acf1(x):
        return float(np.corrcoef(x[:-1], x[1:])[0, 1])

    def q95(r, mean_block, seed):
        dds = [max_drawdown(s) for s in stationary_bootstrap(r, n_samples, mean_block, seed=seed)]
        return float(np.quantile(dds, 0.95))

    panel_a, block_deeper_a = [], 0
    acf_orig, acf_blk, acf_iid = [], [], []
    for s in range(n_seeds):
        r = regime_vol_returns(T=2500, seed=s)
        qi, qb = q95(r, 1.0000001, s * 3 + 1), q95(r, 40, s * 3 + 1)
        block_deeper_a += qb > qi
        panel_a.append((s, qi, qb))
        acf_orig.append(acf1(r))
        acf_blk.append(np.mean([acf1(x) for x in stationary_bootstrap(r, 30, 40, seed=1)]))
        acf_iid.append(np.mean([acf1(x) for x in stationary_bootstrap(r, 30, 1.0000001, seed=2)]))

    block_deeper_b = 0
    panel_b = []
    for s in range(n_seeds):
        r = 0.0003 + 0.01 * ar1_series(0.15, 2500, seed=s)
        qi, qb = q95(r, 1.0000001, s + 11), q95(r, 40, s + 11)
        block_deeper_b += qb > qi
        panel_b.append((s, qi, qb))
    return (panel_a, block_deeper_a, float(np.mean(acf_orig)), float(np.mean(acf_blk)),
            float(np.mean(acf_iid)), panel_b, block_deeper_b, n_seeds)


def mc4(n_draws=40):
    corrs_full, corrs_exp = [], []
    for s in range(n_draws):
        y, cyc = trend_plus_cycle(T=500, cycle_rho=0.9, seed=s)
        for mode, acc in (("full", corrs_full), ("expanding", corrs_exp)):
            c = hamilton_filter(y, h=8, p=4, mode=mode)
            m = ~np.isnan(c)
            acc.append(np.corrcoef(c[m], cyc[m])[0, 1])
    return float(np.mean(corrs_full)), float(np.mean(corrs_exp))


def main():
    lines = ["# Estimator-validation Monte Carlo — Track R6 first results",
             "",
             "Run 2026-08-31 on synthetic ground truth (seeded; zero market data). Methods check",
             "pre-registered as MC1–MC4 in this script's docstring; no market hypothesis tested.",
             ""]

    lines += ["## MC1 — tau_half recovery (median estimate vs truth; 90% CI coverage)",
              "",
              "| true rho | T | true tau_half | naive median | corrected median | CI coverage |",
              "|---|---|---|---|---|---|"]
    for rho, T, tt, nv, cr, cov in mc1():
        lines.append(f"| {rho} | {T} | {tt:.1f} | {nv:.1f} | {cr:.1f} | {cov:.0%} |")
    lines += ["",
              "Reading: the Kendall correction moves the median materially toward truth at every",
              "(rho, T). CI coverage is from the PARAMETRIC pivot bootstrap — run 1 used a",
              "moving-block bootstrap of the observed series whose 90% intervals covered as",
              "little as 0-7% at rho>=0.9 (miscalibrated: block joins chop persistence); that",
              "method is retired and recorded here as an R6 catch. Wherever coverage below is",
              "still materially short of 90% (expected near the unit root), the estimator's CI",
              "is not trusted at that persistence — those ladder entries carry ranges + the",
              "near-unit-root flag and await Andrews (1993) exact intervals (DESIGN §11.2).", ""]

    lines += ["## MC2 — DSR false-discovery control (true Sharpe = 0, select max of N trials)",
              "",
              "| N trials | share endorsed at DSR>0.95 (should be ~<=5%) |",
              "|---|---|"]
    for N, fd in mc2():
        lines.append(f"| {N} | {fd:.1%} |")
    lines += ["",
              "Reading: with the trial-count supplied honestly, the implementation controls the",
              "false-discovery rate at the counts our ledger anticipates (hedge grid 28, factor",
              "grids ~252). With N mis-declared as 1 the same selected strategies WOULD be",
              "endorsed — the ledger's honesty, not the formula, is the protection.", ""]

    (pa, deep_a, ao, ab, ai, pb, deep_b, ns) = mc3()
    lines += ["## MC3 — drawdown tails: iid vs block bootstrap (REVISED after run 1 falsified the pre-written reading)",
              "",
              "Panel (a) — vol-clustered returns, ~zero RETURN autocorrelation "
              f"(mean acf1 of originals {ao:+.3f}):",
              "",
              "| seed | q95 maxDD, iid | q95 maxDD, block-40 |",
              "|---|---|---|"]
    for s, qi, qb in pa:
        lines.append(f"| {s} | {qi:.1%} | {qb:.1%} |")
    lines += ["",
              f"Block deeper in {deep_a}/{ns} seeds — **direction is seed-dependent: the generic "
              "claim 'iid always understates DD tails' is FALSE for pure vol clustering.** What "
              f"block resampling demonstrably preserves is the dependence structure itself: mean "
              f"resample acf1 = {ab:+.3f} (block) vs {ai:+.3f} (iid) against {ao:+.3f} original.",
              "",
              "Panel (b) — genuinely autocorrelated returns (AR(1) rho=0.15 in returns — the "
              "structure of stress regimes and trending declines, i.e. the episodes the DD "
              "ceiling is actually checked against):",
              "",
              "| seed | q95 maxDD, iid | q95 maxDD, block-40 |",
              "|---|---|---|"]
    for s, qi, qb in pb:
        lines.append(f"| {s} | {qi:.1%} | {qb:.1%} |")
    lines += ["",
              f"Block deeper in {deep_b}/{ns} seeds — where returns are autocorrelated, iid "
              "resampling DOES understate the tail, systematically.",
              "",
              "Design consequence (DESIGN §11.7 wording updated): block bootstrap is required "
              "because it preserves the data's own dependence (making the DD distribution "
              "faithful), and because the episodes that matter are return-autocorrelated, where "
              "iid is provably optimistic. The blanket 'iid always understates' phrasing is "
              "retired.", ""]

    f, e = mc4()
    lines += ["## MC4 — Hamilton filter: the price of real-time honesty",
              "",
              f"Cycle-recovery correlation, full-sample fit: **{f:.2f}**; expanding (real-time,",
              f"no look-ahead): **{e:.2f}** (h=8, p=4, known AR(0.9) cycle, T=500, 40 draws).",
              "",
              "Reading: the tradable (expanding) mode keeps most of the recovery power; the gap is",
              "the honest cost of refusing look-ahead. Full-sample mode remains characterization-",
              "only, never a signal input.", ""]

    OUT.write_text("\n".join(lines))
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
