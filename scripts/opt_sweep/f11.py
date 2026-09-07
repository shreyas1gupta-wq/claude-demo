"""
OP-D2 sweep, family f11 -- "overnight gap mechanics by VIX state"
Registered entry (research/register/trial-ledger.md, Entry OP-D2, 2026-09-07):
  F11 gaps: |overnight gap|>=1% direction -> intraday continuation + by VIX state (4) --
  two-sided.
Four registered cells = direction {up-gap, down-gap} x split {full sample, by VIX state}.
No directional bar was pre-specified (two-sided) -- results reported honestly both ways,
verdict TWO-SIDED for all four cells (no PASS/MISS threshold exists to miss).

DEFINITIONS (stated up front; index has no adjustment issue over a single day, so raw,
unadjusted Open/Close are used for both legs so gap and intraday are measured on the same
price series):
  gap_t      = Open_t / Close_{t-1} - 1        (overnight, prior close -> today's open)
  intraday_t = Close_t / Open_t - 1            (today's open -> today's close)
  up-gap day:   gap_t >= +0.01
  down-gap day: gap_t <= -0.01
  continuation on an up-gap day  = intraday_t > 0 (the gap direction persists into the day)
  continuation on a down-gap day = intraday_t < 0

NO LOOKAHEAD:
  - gap_t uses Close_{t-1} and Open_t only; intraday_t uses Open_t and Close_t only -- both
    are same-day/overnight quantities, never using data after t.
  - VIX state per the data cheat sheet: expanding percentile of India VIX close, min_obs=252,
    via quant.ladder.credit_cycle.expanding_percentile -- the percentile at t uses only
    VIX[:t+1]. High-VIX = pctl_t >= 0.5 (median split of VIX's OWN history to date; no
    magic number -- a quantile rank, not a tuned level), Low-VIX = pctl_t < 0.5.
  - Cells 1-2 (full sample) use the whole NIFTY history (2007-09..2026-04). Cells 3-4 (by
    VIX state) are restricted to the India VIX vault's covered window (2010-07..2023-04),
    inner-joined on date; this is stated as a coverage caveat, not silently dropped.
  - Unlike f09's forward-21d event study, gap_t/intraday_t observations here are NOT
    overlapping in time (each date contributes exactly one same-day open->close outcome
    conditioned on that day's own overnight gap) -- there is no shared-window inflation to
    correct for, so naive Welch t-tests and binomial sign tests (scipy.stats, not a quant/stats
    re-implementation target per process note #6) are the appropriate inference tool here;
    quant/stats machinery (expanding_percentile) is used for the one state construction the
    registry mandates.
"""
import sys

sys.path.insert(0, "/home/user/claude-demo")

import numpy as np
import pandas as pd
from scipy import stats

from quant.ladder.credit_cycle import expanding_percentile

NIFTY = "/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv"
VIX = "/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv"

GAP_THRESH = 0.01   # registered: |overnight gap| >= 1%
PCT_MIN_OBS = 252   # OP-D1 / cheat-sheet convention: expanding percentile, min_obs=252
VIX_MEDIAN = 0.5    # quantile-rank split of VIX's own expanding history (no magic number)


def summarize(sub_intraday, gap_sign):
    """gap_sign: +1 for up-gap days, -1 for down-gap days."""
    n = len(sub_intraday)
    if n == 0:
        return dict(n=0, mean=float("nan"), t=float("nan"), p_t=float("nan"),
                    n_cont=0, cont_rate=float("nan"), p_binom=float("nan"))
    mean = float(sub_intraday.mean())
    t_stat, p_t = stats.ttest_1samp(sub_intraday, 0.0)
    cont_mask = (sub_intraday > 0) if gap_sign > 0 else (sub_intraday < 0)
    n_cont = int(cont_mask.sum())
    cont_rate = n_cont / n
    p_binom = stats.binomtest(n_cont, n, 0.5, alternative="two-sided").pvalue
    return dict(n=n, mean=mean, t=float(t_stat), p_t=float(p_t),
                n_cont=n_cont, cont_rate=cont_rate, p_binom=float(p_binom))


def main():
    nifty = pd.read_csv(NIFTY, parse_dates=["Date"]).set_index("Date").sort_index()
    close, open_ = nifty["Close"], nifty["Open"]
    gap = (open_ / close.shift(1) - 1.0)
    intraday = (close / open_ - 1.0)
    df = pd.DataFrame({"gap": gap, "intraday": intraday}).dropna()

    up = df[df["gap"] >= GAP_THRESH]
    down = df[df["gap"] <= -GAP_THRESH]

    r1 = summarize(up["intraday"], +1)
    r2 = summarize(down["intraday"], -1)

    # ---- VIX state (cells 3-4): expanding percentile, min_obs=252, median split ----
    vix = pd.read_csv(VIX, parse_dates=["date"]).set_index("date").sort_index()
    vix_pctl = pd.Series(
        expanding_percentile(vix["close"].values, min_obs=PCT_MIN_OBS),
        index=vix.index, name="vix_pctl",
    )
    df_v = df.join(vix_pctl, how="inner").dropna(subset=["vix_pctl"])
    hi = df_v[df_v["vix_pctl"] >= VIX_MEDIAN]
    lo = df_v[df_v["vix_pctl"] < VIX_MEDIAN]

    up_hi = hi[hi["gap"] >= GAP_THRESH]
    up_lo = lo[lo["gap"] >= GAP_THRESH]
    down_hi = hi[hi["gap"] <= -GAP_THRESH]
    down_lo = lo[lo["gap"] <= -GAP_THRESH]

    r3_hi = summarize(up_hi["intraday"], +1)
    r3_lo = summarize(up_lo["intraday"], +1)
    r4_hi = summarize(down_hi["intraday"], -1)
    r4_lo = summarize(down_lo["intraday"], -1)

    # diff-in-means test hi vs lo (Welch), for cells 3 and 4
    t3, p3 = (stats.ttest_ind(up_hi["intraday"], up_lo["intraday"], equal_var=False)
              if len(up_hi) > 1 and len(up_lo) > 1 else (float("nan"), float("nan")))
    t4, p4 = (stats.ttest_ind(down_hi["intraday"], down_lo["intraday"], equal_var=False)
              if len(down_hi) > 1 and len(down_lo) > 1 else (float("nan"), float("nan")))

    print("=== f11 overnight gap mechanics by VIX state ===")
    print(f"nifty rows(usable)={len(df)}  date range {df.index.min().date()}..{df.index.max().date()}")
    print(f"gap threshold = +/-{GAP_THRESH:.0%}")
    print()
    print("--- cell 1: up-gap days (gap>=+1%), full sample ---")
    print(f"n={r1['n']}  mean_intraday={r1['mean']:.4%}  t={r1['t']:.3f}  p={r1['p_t']:.4f}  "
          f"cont_rate={r1['cont_rate']:.3%} (n_cont={r1['n_cont']})  binom_p={r1['p_binom']:.4f}")
    print()
    print("--- cell 2: down-gap days (gap<=-1%), full sample ---")
    print(f"n={r2['n']}  mean_intraday={r2['mean']:.4%}  t={r2['t']:.3f}  p={r2['p_t']:.4f}  "
          f"cont_rate={r2['cont_rate']:.3%} (n_cont={r2['n_cont']})  binom_p={r2['p_binom']:.4f}")
    print()
    print(f"VIX-joined rows={len(df_v)}  window {df_v.index.min().date()}..{df_v.index.max().date()}  "
          f"(expanding pctl min_obs={PCT_MIN_OBS}, median split)")
    print()
    print("--- cell 3: up-gap days, by VIX state ---")
    print(f"HIGH-VIX (pctl>=0.5): n={r3_hi['n']}  mean_intraday={r3_hi['mean']:.4%}  "
          f"cont_rate={r3_hi['cont_rate']:.3%}  binom_p={r3_hi['p_binom']:.4f}")
    print(f"LOW-VIX  (pctl<0.5):  n={r3_lo['n']}  mean_intraday={r3_lo['mean']:.4%}  "
          f"cont_rate={r3_lo['cont_rate']:.3%}  binom_p={r3_lo['p_binom']:.4f}")
    print(f"hi-vs-lo Welch t={t3:.3f}  p={p3:.4f}  diff={r3_hi['mean'] - r3_lo['mean']:.4%}")
    print()
    print("--- cell 4: down-gap days, by VIX state ---")
    print(f"HIGH-VIX (pctl>=0.5): n={r4_hi['n']}  mean_intraday={r4_hi['mean']:.4%}  "
          f"cont_rate={r4_hi['cont_rate']:.3%}  binom_p={r4_hi['p_binom']:.4f}")
    print(f"LOW-VIX  (pctl<0.5):  n={r4_lo['n']}  mean_intraday={r4_lo['mean']:.4%}  "
          f"cont_rate={r4_lo['cont_rate']:.3%}  binom_p={r4_lo['p_binom']:.4f}")
    print(f"hi-vs-lo Welch t={t4:.3f}  p={p4:.4f}  diff={r4_hi['mean'] - r4_lo['mean']:.4%}")

    out = {
        "n1": r1["n"], "mean1": round(r1["mean"], 6), "p1_t": round(r1["p_t"], 4),
        "cont_rate1": round(r1["cont_rate"], 4), "p1_binom": round(r1["p_binom"], 4),
        "n2": r2["n"], "mean2": round(r2["mean"], 6), "p2_t": round(r2["p_t"], 4),
        "cont_rate2": round(r2["cont_rate"], 4), "p2_binom": round(r2["p_binom"], 4),
        "n3_hi": r3_hi["n"], "mean3_hi": round(r3_hi["mean"], 6), "cont_rate3_hi": round(r3_hi["cont_rate"], 4),
        "n3_lo": r3_lo["n"], "mean3_lo": round(r3_lo["mean"], 6), "cont_rate3_lo": round(r3_lo["cont_rate"], 4),
        "t3": round(float(t3), 3), "p3": round(float(p3), 4),
        "n4_hi": r4_hi["n"], "mean4_hi": round(r4_hi["mean"], 6), "cont_rate4_hi": round(r4_hi["cont_rate"], 4),
        "n4_lo": r4_lo["n"], "mean4_lo": round(r4_lo["mean"], 6), "cont_rate4_lo": round(r4_lo["cont_rate"], 4),
        "t4": round(float(t4), 3), "p4": round(float(p4), 4),
    }
    print()
    print("RESULT_JSON", out)


if __name__ == "__main__":
    main()
