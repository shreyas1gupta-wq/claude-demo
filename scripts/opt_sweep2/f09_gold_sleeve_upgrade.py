"""f09_gold_sleeve_upgrade — Strategy Sweep 2. Registered 2026-09-08 BEFORE this run.

FAMILY: the current NIFTY-vs-gold-INR switcher (20% of book, binary winner-take-all on lagged
12m momentum) is tested against three alternative gold-sleeve mechanics:
  (a) vol-managed gold-INR as a PERMANENT sleeve (no switching at all) — 15% vol target on
      lagged monthly EWMA(lambda=0.94) vol, cap swept {1.5x, 2.0x} (matches the house cap
      conventions already used for the core (1.5x) and factor (2.0x) sleeves — no new magic
      number).
  (b) gold trend filter: the switcher's gold leg is gated by a lagged 12m-MA-of-price rule
      (gold held only if mom_g>mom_n AND price(sig_d) > MA12(sig_d)); two fallback variants
      when the filter vetoes gold (fallback to NIFTY / fallback to CASH).
  (c) 60/40 split-holding (winner/loser) instead of winner-take-all, with a 70/30 sensitivity
      check (NOT a tuned selection — both grid points reported, 60/40 is the pre-specified
      design point named in the task brief).

Every signal uses ONLY data through the prior month-end (sig_d = last monthly obs strictly
before the target month `me`, exactly the existing SW_M convention in analyze_op_d6b.py) — no
lookahead. Reuses the shared book engine (run_book/stats_of/month_stream) verbatim; no inline
re-implementation of the EWMA-vol or percentile machinery beyond the exact house-convention
formula already inlined in analyze_op_d6b.py's own fac_vm construction (mirrored here for gold).

Bars: this is an EXPLORATORY family sweep, not a pre-registered ledger trial — no bars are set
here; verdicts are comparative (vs the current switcher standalone and vs the OP-D6b a5 booked
baseline) per the task brief, and any proposed design freezes its own parameters below.
"""
import json

import numpy as np
import pandas as pd

# ---- load the shared engine (house pattern: exec everything before MAIN) ----
_src = open("/home/user/claude-demo/scripts/analyze_op_d6b.py").read()
_g = {}
exec(_src.split("# === MAIN ===")[0], _g)
run_book, stats_of, month_stream = _g["run_book"], _g["stats_of"], _g["month_stream"]
core_stream = _g["core_stream"]
dates, D0, D1 = _g["dates"], _g["D0"], _g["D1"]
mom_g, mom_n = _g["mom_g"], _g["mom_n"]
g_ret_m, n_ret_m = _g["g_ret_m"], _g["n_ret_m"]
g_inr, n_me = _g["g_inr"], _g["n_me"]
SW_M = _g["SW_M"]

CELLS = 0  # incremented once per computed backtest configuration / conditional statistic


def cell():
    global CELLS
    CELLS += 1


def monthly_to_book_stats(monthly_series, label=""):
    """Standalone stats for a monthly-return sleeve: build its own equity curve
    (100-based) over D0..D1 via the house month_stream (last-trading-day placement,
    E1-fix convention), and report CAGR/DD/worst-yr plus correlations."""
    daily = month_stream(monthly_series)
    eq = (1 + daily).cumprod() * 100
    cagr, dd, yearly = stats_of(eq)
    return dict(cagr=cagr, dd=dd, worst_yr=100 * yearly.min(),
                worst_yr_year=int(yearly.idxmin().year)), eq, yearly


def corr_vs(monthly_series, other_monthly, label):
    j = pd.concat([monthly_series.rename("a"), other_monthly.rename("b")], axis=1).dropna()
    return dict(n=len(j), corr=float(j["a"].corr(j["b"])))


def book_sub(sleeve_monthly, w_sleeve, w_core=0.65, w_fac=0.15, cap=1.5):
    """Full-book substitution: replace the switcher leg (sw_w) with `sleeve_monthly` at
    weight w_sleeve, keep core_w/fac_w/overlays/financing/syn_margin identical to the
    booked OP-D6b a5 config. Uses the extra_ret channel (house pattern from OP-D7's
    weekly-sleeve substitution) so run_book's own switcher path (sw_w) is set to 0."""
    extra = w_sleeve * month_stream(sleeve_monthly)
    eq, pm = run_book(w_core, 0.0, w_fac, cap=cap, financing=True, syn_margin=True,
                       extra_ret=extra)
    cagr, dd, yearly = stats_of(eq)
    return dict(cagr=cagr, dd=dd, worst_yr=100 * yearly.min(),
                worst_yr_year=int(yearly.idxmin().year), peak_margin=100 * pm)


OUT = {"family": "f09_gold_sleeve_upgrade", "window": [str(D0.date()), str(D1.date())]}

# =====================================================================================
# 0. BASELINE — recompute the current switcher standalone + its booked full-book number,
#    as the comparison anchor for everything below (sanity: must match OP-D6b a5 / f04's
#    dual_12m row: cagr 11.13, dd -11.53, worst_yr -2.27).
# =====================================================================================
core_ret_a5, _ = core_stream(1.5, financing=True)
core_m_a5 = ((1 + core_ret_a5).resample("ME").prod() - 1).loc[D0:D1]

base_stats, base_eq, base_yearly = monthly_to_book_stats(SW_M, "baseline switcher")
cell()
base_book = book_sub(SW_M, 0.20)
cell()
base_corr_core = corr_vs(SW_M, core_m_a5, "core")
base_corr_nifty = corr_vs(SW_M, n_ret_m, "nifty")
OUT["baseline_switcher"] = dict(standalone=base_stats, book_substitution=base_book,
                                 corr_vs_core=base_corr_core["corr"],
                                 corr_vs_nifty=base_corr_nifty["corr"],
                                 note="sanity check vs booked OP-D6b a5 (11.13/-11.53/-2.27) "
                                      "and f04's dual_12m row — must reproduce")

# =====================================================================================
# (a) VOL-MANAGED GOLD-INR AS A PERMANENT SLEEVE (no switching)
# =====================================================================================
gvol = g_ret_m.pow(2).ewm(alpha=0.06).mean().pow(0.5) * np.sqrt(12)  # house EWMA(0.94) convention


def vm_gold(target=0.15, cap=1.5):
    lev = (target / gvol).clip(upper=cap).shift(1)  # exact fac_vm pattern (analyze_op_d6b.py)
    return (lev * g_ret_m).dropna()


design_a = {}
for cap in (1.5, 2.0):
    vmg = vm_gold(0.15, cap)
    st, _, _ = monthly_to_book_stats(vmg, f"vm_gold cap{cap}")
    cell()
    cvc = corr_vs(vmg, core_m_a5, "core")["corr"]
    cvn = corr_vs(vmg, n_ret_m, "nifty")["corr"]
    cvs = corr_vs(vmg, SW_M, "switcher")["corr"]
    mean_lev = float((0.15 / gvol).clip(upper=cap).shift(1).dropna().mean())
    design_a[f"cap{cap}"] = dict(standalone=st, corr_vs_core=cvc, corr_vs_nifty=cvn,
                                  corr_vs_switcher=cvs, ann_vol_target=15.0, mean_lev=mean_lev)

# book substitutions: (i) same 20% notional as the switcher (apples-to-apples), and
# (ii) the literally-stated 10% notional with the freed 10% parked in core (65->75%) —
# flagged: this second config is an ASSET-MIX CHANGE, exploratory only, CONTRACT 8 reserves
# asset-mix optimization to Stage 3 — reported for completeness, not proposed for adoption.
vmg_15_15 = vm_gold(0.15, 1.5)
sub_a_20 = book_sub(vmg_15_15, 0.20)
cell()
sub_a_10_freed_to_core = book_sub(vmg_15_15, 0.10, w_core=0.75, w_fac=0.15)
cell()
design_a["book_substitution_20pct_like_for_like"] = sub_a_20
design_a["book_substitution_10pct_freed_to_core_EXPLORATORY_ASSET_MIX"] = sub_a_10_freed_to_core
OUT["design_a_vol_managed_permanent"] = design_a

# =====================================================================================
# (b) GOLD TREND FILTER (12m MA, lagged) gating the gold leg of the switcher
# =====================================================================================
gold_ma12 = g_inr.rolling(12).mean()


def trend_switcher(fallback="nifty"):
    out = {}
    n_veto, n_total = 0, 0
    for me in n_me.loc[D0:D1].index:
        prev = mom_n.index[mom_n.index < me]
        if not len(prev):
            continue
        n_total += 1
        sig_d = prev[-1]
        wants_gold = mom_g.get(sig_d, -9) > mom_n.get(sig_d, -9)
        ma = gold_ma12.get(sig_d, np.nan)
        px = g_inr.get(sig_d, np.nan)
        trend_up = (not pd.isna(ma)) and (not pd.isna(px)) and (px > ma)
        if wants_gold and trend_up:
            out[me] = g_ret_m.get(me, 0.0)
        elif wants_gold and not trend_up:
            n_veto += 1
            out[me] = 0.0 if fallback == "cash" else n_ret_m.get(me, 0.0)
        else:
            out[me] = n_ret_m.get(me, 0.0)
    return pd.Series(out), n_veto, n_total


design_b = {}
for fb in ("nifty", "cash"):
    ts, n_veto, n_total = trend_switcher(fb)
    st, _, _ = monthly_to_book_stats(ts, f"trend_switcher_{fb}")
    cell()
    cvc = corr_vs(ts, core_m_a5, "core")["corr"]
    cvn = corr_vs(ts, n_ret_m, "nifty")["corr"]
    cvs = corr_vs(ts, SW_M, "switcher")["corr"]
    design_b[f"fallback_{fb}"] = dict(standalone=st, corr_vs_core=cvc, corr_vs_nifty=cvn,
                                       corr_vs_switcher=cvs,
                                       veto_months=n_veto, total_months=n_total)

sub_b_nifty = book_sub(trend_switcher("nifty")[0], 0.20)
cell()
sub_b_cash = book_sub(trend_switcher("cash")[0], 0.20)
cell()
design_b["book_substitution_20pct"] = dict(fallback_nifty=sub_b_nifty, fallback_cash=sub_b_cash)
OUT["design_b_trend_filter"] = design_b

# =====================================================================================
# (c) 60/40 SPLIT-HOLDING (winner/loser) instead of winner-take-all
# =====================================================================================
def split_switcher(w_win=0.60):
    out = {}
    for me in n_me.loc[D0:D1].index:
        prev = mom_n.index[mom_n.index < me]
        if not len(prev):
            continue
        sig_d = prev[-1]
        g_wins = mom_g.get(sig_d, -9) > mom_n.get(sig_d, -9)
        gr, nr = g_ret_m.get(me, 0.0), n_ret_m.get(me, 0.0)
        out[me] = w_win * (gr if g_wins else nr) + (1 - w_win) * (nr if g_wins else gr)
    return pd.Series(out)


design_c = {}
for w_win, key in ((0.60, "60_40"), (0.70, "70_30_sensitivity")):
    sp = split_switcher(w_win)
    st, _, _ = monthly_to_book_stats(sp, f"split_{key}")
    cell()
    cvc = corr_vs(sp, core_m_a5, "core")["corr"]
    cvn = corr_vs(sp, n_ret_m, "nifty")["corr"]
    cvs = corr_vs(sp, SW_M, "switcher")["corr"]
    design_c[key] = dict(standalone=st, corr_vs_core=cvc, corr_vs_nifty=cvn, corr_vs_switcher=cvs)

sub_c_60_40 = book_sub(split_switcher(0.60), 0.20)
cell()
design_c["book_substitution_20pct_60_40"] = sub_c_60_40
OUT["design_c_split_holding"] = design_c

# =====================================================================================
# summary / verdict
# =====================================================================================
OUT["cells_consumed"] = CELLS
print(json.dumps(OUT, indent=2, default=str))

with open("/home/user/claude-demo/research/opt_sweep2/f09_gold_sleeve_upgrade.json", "w") as f:
    json.dump(OUT, f, indent=2, default=str)

print(f"\nCELLS_CONSUMED={CELLS}")
