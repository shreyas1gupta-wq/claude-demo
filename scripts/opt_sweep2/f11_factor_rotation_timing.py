"""f11_factor_rotation_timing — FACTOR ROTATION TIMING (WML vs HML).

Pre-registered design (per orchestrator brief): corr(WML,HML) = -0.37 (V2, booked doctrine).
Test whether TIMING between the two IIMA monthly factor legs beats the standing book's static
50/50 vol-managed blend (OP-D6b's 15% fac sleeve). Three variants, ALL using only
expanding/lagged information (no lookahead):

  (a) SHARPE-SWITCH   hold whichever leg had the better trailing-12m Sharpe, lagged 1 month
                       (full rolling window t-12..t-1, decision applied to month t's return).
  (b) VIX-GATE         gate WML OFF (HML full ON) whenever last month's India-VIX expanding
                       percentile (house convention, min_obs=252, quant.ladder.credit_cycle)
                       was >= 0.90 (top-decile) -- momentum-crash-after-spike prior. Only
                       defined 2010-07..2023-04 (VIX vault window); elsewhere reverts to the
                       static 50/50 blend by construction (no signal available).
  (c) MOMENTUM-TILT    70/30 (not 30/70) toward whichever leg had the better trailing-12m
                       CUMULATIVE return, lagged 1 month. Fixed 70/30 split -- not tuned here
                       (a genuine grid would be a second, un-pre-registered cell of parameter
                       mining; the brief names 70/30 as the frozen spec).

All streams vol-managed identically to the standing book's fac sleeve: EWMA(alpha=0.06,
matches lambda=0.94) vol on the (already-selected) monthly stream, target 15%/yr, cap 2x,
applied with a full 1-month shift (house convention, analyze_op_d6b.py fac_vm construction).
Full IIMA history used for the factor-only comparison (1993-10..2025-12, longest available
sample -- much longer power than the 2011-2023 book window); book-level context restricted to
the standing book's window (2011-07..2023-03) where it is computed.

Significance: stationary block bootstrap (Politis-Romano, quant/stats/bootstrap.py) on the
PAIRED monthly return difference (variant - baseline), mean_block=3 (monthly data, short
memory factor -- stated caveat, not derived from a measured tau_half for these series).
maxDD via quant/stats/bootstrap.max_drawdown (never an inline re-implementation, process
note #6). No look-ahead: every signal (sharpe rank, VIX percentile, momentum rank) is shifted
a full month before being applied; the VIX percentile itself is expanding (min_obs=252).
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402
from quant.stats.bootstrap import max_drawdown, stationary_bootstrap  # noqa: E402

V = "/home/user/claude-demo/ingest/vault"
CELLS = 0


def cell(tag):
    global CELLS
    CELLS += 1
    return tag


# ---------------------------------------------------------------- load
ii = pd.read_csv(f"{V}/factors/iima_monthly_factors.csv", na_values=["NA"])
ii["d"] = pd.to_datetime(ii["Date"]) + pd.offsets.MonthEnd(0)
ii = ii.set_index("d")
wml_full = (ii["WML"] / 100).dropna()
hml_full = (ii["HML"] / 100).dropna()
idx = wml_full.index.intersection(hml_full.index).sort_values()
wml, hml = wml_full.reindex(idx), hml_full.reindex(idx)
fac = (0.5 * (wml + hml))  # static 50/50 blend, house baseline (analyze_op_d6b.py)

vix = pd.read_csv(f"{V}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"]).set_index("date")["close"]
vix_pct_daily = pd.Series(expanding_percentile(vix.to_numpy(), min_obs=252), index=vix.index)
vix_pct_monthly = vix_pct_daily.resample("ME").last()
VIX_M0, VIX_M1 = vix_pct_monthly.index.min(), vix_pct_monthly.index.max()

BOOK_D0, BOOK_D1 = pd.Timestamp("2011-07-31"), pd.Timestamp("2023-03-31")  # OP-D6b window, month-end anchored

print(f"Loaded: WML/HML common sample {idx.min().date()}..{idx.max().date()} (n={len(idx)}); "
      f"India-VIX monthly coverage {VIX_M0.date()}..{VIX_M1.date()} (n={vix_pct_monthly.dropna().shape[0]})")


# ---------------------------------------------------------------- vol-management (house convention)
def vol_manage(r, target=0.15, cap=2.0):
    """EWMA(alpha=0.06)-scaled leverage, shifted 1 month -- fac_vm's exact construction
    (analyze_op_d6b.py). No lookahead: flev(t) uses fvol(t-1)."""
    fvol = r.pow(2).ewm(alpha=0.06).mean().pow(0.5) * np.sqrt(12)
    flev = (target / fvol).clip(upper=cap).shift(1)
    return (flev * r).dropna()


def stats_of_monthly(r_vm, tag):
    """Sharpe (ann.), CAGR, maxDD (quant/stats), era halves (pre/post 2017-01-01, house cut)."""
    cell(tag)
    r_vm = r_vm.dropna()
    sharpe = float(r_vm.mean() / r_vm.std() * np.sqrt(12))
    eq = (1 + r_vm).cumprod()
    yrs = (eq.index[-1] - eq.index[0]).days / 365.25
    cagr = 100 * (eq.iloc[-1] ** (1 / yrs) - 1)
    dd = 100 * max_drawdown(r_vm.to_numpy())
    h1 = r_vm.loc[:"2016-12-31"]
    h2 = r_vm.loc["2017-01-01":]

    def ann(x):
        if len(x) < 6:
            return float("nan")
        e = (1 + x).cumprod()
        y = (e.index[-1] - e.index[0]).days / 365.25
        return 100 * (e.iloc[-1] ** (1 / y) - 1) if y > 0 else float("nan")
    cell(tag + "_era1"); cell(tag + "_era2")
    e1, e2 = ann(h1), ann(h2)
    return dict(sharpe=sharpe, cagr=cagr, maxdd=-dd, era1=e1, era2=e2, n=len(r_vm),
                start=str(r_vm.index.min().date()), end=str(r_vm.index.max().date()))


def sig_test(variant_r, base_r, tag, mean_block=3.0, n_samples=2000):
    """Block-bootstrap significance of mean(variant-base) on the common overlapping sample."""
    cell(tag + "_sigtest")
    common = variant_r.index.intersection(base_r.index)
    diff = (variant_r.reindex(common) - base_r.reindex(common)).dropna()
    if len(diff) < 24:
        return dict(n=len(diff), note="too few obs for bootstrap")
    boot = stationary_bootstrap(diff.to_numpy(), n_samples, mean_block, seed=0)
    boot_means = boot.mean(axis=1)
    lo, hi = np.percentile(boot_means, [2.5, 97.5])
    p_le0 = float((boot_means <= 0).mean())
    return dict(n=len(diff), mean_diff_mo=float(diff.mean()), ci95=[float(lo), float(hi)],
                p_boot_le_0=p_le0)


# ---------------------------------------------------------------- baseline
fac_vm = vol_manage(fac)
base_stats = stats_of_monthly(fac_vm, "baseline_5050")
print(f"\nBASELINE static 50/50 vol-managed ({base_stats['start']}..{base_stats['end']}, "
      f"n={base_stats['n']}): Sharpe {base_stats['sharpe']:.2f} | CAGR {base_stats['cagr']:+.2f}% | "
      f"maxDD {base_stats['maxdd']:.2f}% | era1(<=2016) {base_stats['era1']:+.2f}%/yr | "
      f"era2(>=2017) {base_stats['era2']:+.2f}%/yr")

# raw (unlevered) single-leg context, cheap, informative
cell("raw_wml"); cell("raw_hml")
raw_w_sh = float(wml.mean() / wml.std() * np.sqrt(12))
raw_h_sh = float(hml.mean() / hml.std() * np.sqrt(12))
print(f"  context (unlevered, informational): raw WML Sharpe {raw_w_sh:.2f}, raw HML Sharpe "
      f"{raw_h_sh:.2f}, corr(WML,HML) = {wml.corr(hml):+.2f}")


# ---------------------------------------------------------------- (a) trailing-12m Sharpe switch
sharpe_w = (wml.rolling(12).mean() / wml.rolling(12).std()).shift(1)
sharpe_h = (hml.rolling(12).mean() / hml.rolling(12).std()).shift(1)
valid_a = sharpe_w.notna() & sharpe_h.notna()
sel_a = np.where(sharpe_w > sharpe_h, "W", "H")
r_a = pd.Series(np.where(valid_a, np.where(sel_a == "W", wml, hml), fac), index=idx)
switches_a = int((pd.Series(sel_a, index=idx)[valid_a].shift(1) != pd.Series(sel_a, index=idx)[valid_a]).sum())
cell("a_switch_count")
r_a_vm = vol_manage(r_a)
a_stats = stats_of_monthly(r_a_vm, "variant_a_sharpe_switch")
a_sig = sig_test(r_a_vm, fac_vm, "variant_a")
print(f"\n(a) SHARPE-SWITCH (12m trailing, lagged 1mo; {int(valid_a.sum())}/{len(idx)} months "
      f"have a valid signal, {switches_a} leg-switches in that span):")
print(f"    Sharpe {a_stats['sharpe']:.2f} (base {base_stats['sharpe']:.2f}, "
      f"d{a_stats['sharpe']-base_stats['sharpe']:+.2f}) | CAGR {a_stats['cagr']:+.2f}% "
      f"(base {base_stats['cagr']:+.2f}) | maxDD {a_stats['maxdd']:.2f}% (base {base_stats['maxdd']:.2f}) | "
      f"era1 {a_stats['era1']:+.2f} era2 {a_stats['era2']:+.2f}")
print(f"    sig test (variant-baseline, paired, block-boot n=2000, block=3mo): mean diff "
      f"{a_sig.get('mean_diff_mo', float('nan'))*100:+.3f}%/mo, 95% CI "
      f"[{a_sig.get('ci95', [np.nan, np.nan])[0]*100:+.3f}, {a_sig.get('ci95', [np.nan, np.nan])[1]*100:+.3f}]%, "
      f"P(diff<=0)={a_sig.get('p_boot_le_0', float('nan')):.2f}")


# ---------------------------------------------------------------- (b) VIX top-decile gate
vix_sig = vix_pct_monthly.reindex(idx).shift(1)  # lagged 1 month, NaN outside VIX coverage
have_signal = vix_sig.notna()
gate_off_wml = have_signal & (vix_sig >= 0.90)
r_b = pd.Series(np.where(gate_off_wml, hml, fac), index=idx)  # ungated -> static 50/50 (unchanged)
n_gated = int(gate_off_wml.sum())
cell("b_gate_count")
r_b_vm = vol_manage(r_b)
b_stats_full = stats_of_monthly(r_b_vm, "variant_b_vixgate_full")

# VIX-covered-window-only comparison (the fair test -- gate can only ever act inside this window)
win_idx = idx[(idx >= VIX_M0) & (idx <= VIX_M1)]
r_b_win_vm = r_b_vm.reindex(win_idx).dropna()
fac_vm_win = fac_vm.reindex(win_idx).dropna()
b_stats_win = stats_of_monthly(r_b_win_vm, "variant_b_vixgate_window")
base_stats_win = stats_of_monthly(fac_vm_win, "baseline_5050_vixwindow")
b_sig = sig_test(r_b_win_vm, fac_vm_win, "variant_b")
print(f"\n(b) VIX-GATE (WML off / HML full when last month's expanding VIX-pct >= 0.90; "
      f"{n_gated}/{int(have_signal.sum())} in-coverage months gated, "
      f"{have_signal.sum()}/{len(idx)} months have any signal at all):")
print(f"    WINDOW-ONLY ({win_idx.min().date()}..{win_idx.max().date()}, n={len(win_idx)}): "
      f"variant Sharpe {b_stats_win['sharpe']:.2f} vs baseline-in-window {base_stats_win['sharpe']:.2f} "
      f"| CAGR {b_stats_win['cagr']:+.2f} vs {base_stats_win['cagr']:+.2f} | "
      f"maxDD {b_stats_win['maxdd']:.2f} vs {base_stats_win['maxdd']:.2f}")
print(f"    sig test (window-only, paired): mean diff {b_sig.get('mean_diff_mo', float('nan'))*100:+.3f}%/mo, "
      f"95% CI [{b_sig.get('ci95', [np.nan, np.nan])[0]*100:+.3f}, "
      f"{b_sig.get('ci95', [np.nan, np.nan])[1]*100:+.3f}]%, P(diff<=0)={b_sig.get('p_boot_le_0', float('nan')):.2f}")
print(f"    FULL-SAMPLE (context only, {have_signal.sum()}/{len(idx)} months gate-eligible, rest = "
      f"baseline by construction): Sharpe {b_stats_full['sharpe']:.2f} vs base {base_stats['sharpe']:.2f} | "
      f"CAGR {b_stats_full['cagr']:+.2f} vs {base_stats['cagr']:+.2f} | maxDD {b_stats_full['maxdd']:.2f} "
      f"vs {base_stats['maxdd']:.2f}")


# ---------------------------------------------------------------- (c) 70/30 momentum tilt
mom_w = ((1 + wml).rolling(12).apply(np.prod, raw=True) - 1).shift(1)
mom_h = ((1 + hml).rolling(12).apply(np.prod, raw=True) - 1).shift(1)
valid_c = mom_w.notna() & mom_h.notna()
tilt_w = np.where(mom_w > mom_h, 0.70, 0.30)
r_c = pd.Series(np.where(valid_c, tilt_w * wml + (1 - tilt_w) * hml, fac), index=idx)
switches_c = int((pd.Series(tilt_w, index=idx)[valid_c].shift(1) != pd.Series(tilt_w, index=idx)[valid_c]).sum())
cell("c_switch_count")
r_c_vm = vol_manage(r_c)
c_stats = stats_of_monthly(r_c_vm, "variant_c_momentum_tilt")
c_sig = sig_test(r_c_vm, fac_vm, "variant_c")
print(f"\n(c) MOMENTUM-TILT (70/30 toward better trailing-12m cumret leg, lagged 1mo; "
      f"{int(valid_c.sum())}/{len(idx)} months valid, {switches_c} tilt-direction changes):")
print(f"    Sharpe {c_stats['sharpe']:.2f} (base {base_stats['sharpe']:.2f}, "
      f"d{c_stats['sharpe']-base_stats['sharpe']:+.2f}) | CAGR {c_stats['cagr']:+.2f}% "
      f"(base {base_stats['cagr']:+.2f}) | maxDD {c_stats['maxdd']:.2f}% (base {base_stats['maxdd']:.2f}) | "
      f"era1 {c_stats['era1']:+.2f} era2 {c_stats['era2']:+.2f}")
print(f"    sig test (paired, block-boot): mean diff {c_sig.get('mean_diff_mo', float('nan'))*100:+.3f}%/mo, "
      f"95% CI [{c_sig.get('ci95', [np.nan, np.nan])[0]*100:+.3f}, "
      f"{c_sig.get('ci95', [np.nan, np.nan])[1]*100:+.3f}]%, P(diff<=0)={c_sig.get('p_boot_le_0', float('nan')):.2f}")


# ---------------------------------------------------------------- book-level context (standing book window only)
# Only run if any variant looks like it might survive -- here it lets us state the book impact
# honestly regardless of the verdict (a null result at the sleeve level still needs a "what would
# it have done to the book" answer if the sign happens to be positive over the book's own window).
book_win = idx[(idx >= BOOK_D0) & (idx <= BOOK_D1)]
for name, series in [("baseline", fac_vm), ("a_sharpe_switch", r_a_vm), ("b_vixgate", r_b_vm),
                     ("c_momentum_tilt", r_c_vm)]:
    cell(f"book_window_{name}")
book_ctx = {}
for name, series in [("baseline", fac_vm), ("a_sharpe_switch", r_a_vm), ("b_vixgate", r_b_vm),
                     ("c_momentum_tilt", r_c_vm)]:
    s = series.reindex(book_win).dropna()
    if len(s) < 12:
        continue
    eq = (1 + s).cumprod()
    yrs = (eq.index[-1] - eq.index[0]).days / 365.25
    cagr = 100 * (eq.iloc[-1] ** (1 / yrs) - 1)
    book_ctx[name] = dict(cagr_standalone=cagr, n=len(s))
print(f"\nBook-window context ({BOOK_D0.date()}..{BOOK_D1.date()}, standalone sleeve CAGR, "
      f"NOT run through the full run_book() P&L -- 15% weight would scale these ~15% into "
      f"book CAGR delta): " + ", ".join(f"{k}={v['cagr_standalone']:+.2f}%/yr" for k, v in book_ctx.items()))

print(f"\nTOTAL CELLS CONSUMED: {CELLS}")


# ---------------------------------------------------------------- verdict
def beats_baseline(v, sig, min_sharpe_gain=0.10):
    return (v["sharpe"] - base_stats["sharpe"] >= min_sharpe_gain) and \
           sig.get("p_boot_le_0", 1.0) <= 0.10 and v["maxdd"] >= base_stats["maxdd"] - 1.0


verdict_a = beats_baseline(a_stats, a_sig)
verdict_b = beats_baseline(b_stats_win, b_sig, min_sharpe_gain=0.10) and b_stats_win["cagr"] > base_stats_win["cagr"]
verdict_c = beats_baseline(c_stats, c_sig)
print(f"Per-variant beat-baseline verdict (Sharpe gain >=0.10 AND P(diff<=0)<=0.10 AND DD not worse "
      f">1pp): a={verdict_a}, b(window)={verdict_b}, c={verdict_c}")

import json  # noqa: E402
out = dict(
    family="f11_factor_rotation_timing",
    cells_consumed=CELLS,
    sample=dict(factor_common=[str(idx.min().date()), str(idx.max().date())], n_months=len(idx),
                vix_coverage=[str(VIX_M0.date()), str(VIX_M1.date())]),
    baseline=base_stats,
    context=dict(raw_wml_sharpe=raw_w_sh, raw_hml_sharpe=raw_h_sh, corr_wml_hml=float(wml.corr(hml))),
    variant_a_sharpe_switch=dict(stats=a_stats, sig=a_sig, n_valid_signal=int(valid_a.sum()),
                                 n_switches=switches_a, beats_baseline=bool(verdict_a)),
    variant_b_vixgate=dict(window_stats=b_stats_win, window_baseline=base_stats_win,
                           full_sample_stats=b_stats_full, sig_window=b_sig,
                           n_gated_months=n_gated, n_signal_months=int(have_signal.sum()),
                           beats_baseline=bool(verdict_b)),
    variant_c_momentum_tilt=dict(stats=c_stats, sig=c_sig, n_valid_signal=int(valid_c.sum()),
                                 n_switches=switches_c, beats_baseline=bool(verdict_c)),
    book_window_context=book_ctx,
    caveats=[
        "Factor-only backtest: IIMA WML/HML monthly index returns, no transaction costs modeled "
        "for the act of switching between long-short factor books (real rotation would require "
        "unwinding one long-short leg and building the other monthly -- likely materially higher "
        "turnover cost than the standing book's static 50/50 blend, which never trades between "
        "legs, only rebalances the combined vol target).",
        "Variant (b) VIX-gate is only ever active 2010-07..2023-04 (India VIX vault window); "
        "the full-sample number is a blend of gated and ungated (=baseline) months and should "
        "not be read as an independent full-history result -- the window-only comparison is the "
        "fair test.",
        "mean_block=3 months for the stationary bootstrap is a stated assumption (monthly return "
        "series, short assumed memory), not derived from a measured tau_half for WML/HML -- a "
        "longer block would widen the CIs further.",
        "Sample is dominated by a single-country, single-history run (no purged/embargoed CV, "
        "no cross-country replication) -- consistent with CONTRACT Tier-B treatment at best even "
        "if a variant had cleared the bar.",
        "Book-window context (2011-07..2023-03) uses standalone sleeve CAGR, not a full run_book() "
        "re-run with financing/margin/overlays -- directional context only.",
        "No live trade: this is exploratory per the orchestrator brief, not a booked ledger entry.",
    ],
)
with open("/home/user/claude-demo/research/opt_sweep2/f11_factor_rotation_timing.json", "w") as f:
    json.dump(out, f, indent=2, default=str)
print("\nWrote research/opt_sweep2/f11_factor_rotation_timing.json")
