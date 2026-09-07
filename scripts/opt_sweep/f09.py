"""
OP-D2 sweep, family f09 — "panel-breadth washout, fwd 21d"
Registered entry (research/register/trial-ledger.md, Entry OP-D2, 2026-09-07):
  F09 panel-breadth washout (survivor panel %>200dMA proxy) -> fwd 21d index ret (2) -- two-sided.
Two registered cells, no directional bar (report sign/magnitude honestly, both ways).

NO LOOKAHEAD:
  - 200d MA per name is a trailing rolling window (min_periods=200): the state at day t uses
    only prices <= t.
  - Breadth (t) = fraction of names with Close_t > MA200_t among names with a valid MA200 and
    Close reading that day. This is a same-day cross-sectional state, causal by construction.
  - Breadth's own-history percentile is EXPANDING, min_obs=252 (OP-D1 convention), via
    quant.ladder.credit_cycle.expanding_percentile -- percentile at t uses only breadth[:t+1].
  - The forward 21d NIFTY return is the OUTCOME variable (event-study target), computed AFTER
    the state date by design -- it is never fed back into the breadth or percentile state.
  - Inference: fwd-21d windows overlap (each day's window shares up to 20 days with its
    neighbours), which inflates naive iid t-stats. Per process note #6 (use quant/stats/
    machinery, never inline re-implementations), inference uses the registry's stationary
    block bootstrap (quant.stats.bootstrap.stationary_bootstrap) with mean_block=21 (tied to
    the h=21 overlap, not a free parameter), applied to the ROW INDEX so state/outcome pairing
    at each date is preserved under resampling.

CAVEAT (stated up front, not just in the JSON): the survivor panel is SURVIVOR-BIASED (2021
roster, ingest/vault/panel/n500_adjclose_2012_2022.csv.gz) -- one-way use only. Breadth here is
a descriptive cross-sectional read on a fixed, backward-looking panel, not a tradable universe
construction.
"""
import sys

sys.path.insert(0, "/home/user/claude-demo")

import numpy as np
import pandas as pd
from scipy import stats

from quant.ladder.credit_cycle import expanding_percentile
from quant.stats.bootstrap import stationary_bootstrap

PANEL = "/home/user/claude-demo/ingest/vault/panel/n500_adjclose_2012_2022.csv.gz"
NIFTY = "/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv"

MA_WINDOW = 200          # trailing MA window (proxy definition, per data cheat sheet)
MIN_VALID_NAMES = 100    # a breadth reading needs >=100 valid names that day (a few rows are near-empty)
PCT_MIN_OBS = 252        # OP-D1 convention: own-history expanding percentile, min_obs=252
WASHOUT_PCTL = 0.10      # washout = bottom decile of breadth's own history
FWD_H = 21               # fwd horizon, days (registered cell)
N_BOOT = 2000
BOOT_BLOCK = float(FWD_H)  # mean block length tied to the fwd-21d overlap, not a free choice
SEED = 0


def main():
    panel = pd.read_csv(PANEL, parse_dates=["Date"]).set_index("Date").sort_index()

    ma200 = panel.rolling(MA_WINDOW, min_periods=MA_WINDOW).mean()
    valid = panel.notna() & ma200.notna()
    above = (panel > ma200) & valid

    valid_count = valid.sum(axis=1)
    above_count = above.sum(axis=1)
    breadth = (above_count / valid_count).where(valid_count >= MIN_VALID_NAMES)
    breadth.name = "breadth"

    pctl = pd.Series(
        expanding_percentile(breadth.values, min_obs=PCT_MIN_OBS), index=breadth.index, name="pctl"
    )

    nifty = pd.read_csv(NIFTY, parse_dates=["Date"]).set_index("Date").sort_index()
    close = nifty["Adj Close"]
    fwd21 = pd.Series(np.log(close.shift(-FWD_H) / close), name="fwd21")

    state = pd.concat([breadth, pctl], axis=1)
    df = state.join(fwd21, how="inner").sort_index()

    # ---- Cell 1: full-sample corr(breadth_t, fwd21_t) ----
    c1 = df.dropna(subset=["breadth", "fwd21"])
    n1 = len(c1)
    r1, p1_naive = stats.pearsonr(c1["breadth"].values, c1["fwd21"].values)

    idx1 = np.arange(n1, dtype=float)
    boot_idx1 = stationary_bootstrap(idx1, N_BOOT, BOOT_BLOCK, seed=SEED).astype(int)
    b_arr, f_arr = c1["breadth"].values, c1["fwd21"].values
    boot_r = np.array([
        np.corrcoef(b_arr[row], f_arr[row])[0, 1] for row in boot_idx1
    ])
    boot_r = boot_r[np.isfinite(boot_r)]
    ci1_lo, ci1_hi = np.percentile(boot_r, [2.5, 97.5])
    p1_boot = 2 * min((boot_r <= 0).mean(), (boot_r >= 0).mean())

    # ---- Cell 2: washout (bottom decile of breadth pctl) vs baseline, fwd21d ----
    c2 = df.dropna(subset=["pctl", "fwd21"])
    n2 = len(c2)
    mask = c2["pctl"].values <= WASHOUT_PCTL
    n_wash, n_base = int(mask.sum()), int((~mask).sum())
    mean_wash = float(c2.loc[mask, "fwd21"].mean())
    mean_base = float(c2.loc[~mask, "fwd21"].mean())
    diff = mean_wash - mean_base
    t_naive, p2_naive = stats.ttest_ind(c2.loc[mask, "fwd21"], c2.loc[~mask, "fwd21"], equal_var=False)

    idx2 = np.arange(n2, dtype=float)
    boot_idx2 = stationary_bootstrap(idx2, N_BOOT, BOOT_BLOCK, seed=SEED).astype(int)
    fwd2_arr = c2["fwd21"].values
    mask_arr = mask
    boot_diff = []
    for row in boot_idx2:
        m = mask_arr[row]
        if m.any() and (~m).any():
            boot_diff.append(fwd2_arr[row][m].mean() - fwd2_arr[row][~m].mean())
    boot_diff = np.array(boot_diff)
    ci2_lo, ci2_hi = np.percentile(boot_diff, [2.5, 97.5])
    p2_boot = 2 * min((boot_diff <= 0).mean(), (boot_diff >= 0).mean())

    print("=== f09 panel-breadth washout -> fwd 21d NIFTY ret ===")
    print(f"panel rows: {len(panel)}  min_valid_names={MIN_VALID_NAMES}  ma_window={MA_WINDOW}")
    print(f"breadth range: [{breadth.min():.4f}, {breadth.max():.4f}]  n_valid_breadth_days={breadth.notna().sum()}")
    print()
    print("--- cell 1: corr(breadth_t, fwd21_t), naive + block-bootstrap (mean_block=21, n_boot=%d) ---" % N_BOOT)
    print(f"n={n1}  pearson_r={r1:.4f}  naive_two_sided_p={p1_naive:.4f}")
    print(f"boot_95ci=[{ci1_lo:.4f}, {ci1_hi:.4f}]  boot_two_sided_p={p1_boot:.4f}")
    print()
    print("--- cell 2: washout (bottom decile, expanding pctl min_obs=252) vs baseline, fwd21d ---")
    print(f"n={n2}  n_washout={n_wash}  n_baseline={n_base}  washout_pctl_cutoff={WASHOUT_PCTL}")
    print(f"mean_fwd21_washout={mean_wash:.4f}  mean_fwd21_baseline={mean_base:.4f}  diff={diff:.4f}")
    print(f"naive_welch_t={t_naive:.3f}  naive_two_sided_p={p2_naive:.4f}")
    print(f"boot_95ci_diff=[{ci2_lo:.4f}, {ci2_hi:.4f}]  boot_two_sided_p={p2_boot:.4f}")

    out = {
        "n1": n1, "r1": round(float(r1), 4), "p1_naive": round(float(p1_naive), 4),
        "ci1_lo": round(float(ci1_lo), 4), "ci1_hi": round(float(ci1_hi), 4), "p1_boot": round(float(p1_boot), 4),
        "n2": n2, "n_wash": n_wash, "n_base": n_base,
        "mean_wash": round(mean_wash, 4), "mean_base": round(mean_base, 4), "diff": round(diff, 4),
        "t_naive": round(float(t_naive), 3), "p2_naive": round(float(p2_naive), 4),
        "ci2_lo": round(float(ci2_lo), 4), "ci2_hi": round(float(ci2_hi), 4), "p2_boot": round(float(p2_boot), 4),
    }
    print()
    print("RESULT_JSON", out)


if __name__ == "__main__":
    main()
