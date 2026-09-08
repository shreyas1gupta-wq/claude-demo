"""opt_sweep2 / f01_overnight_core — OVERNIGHT-ONLY CORE.

T1 doctrine (booked): the NIFTY premium accrues close-to-open (+24%/yr, calm days only;
stress is intraday). This family tests whether REPLACING (or partially replacing) the
65%-weight vol-managed core with an overnight-only return leg helps the standing book,
under the SAME vol-target sizing rule (15% target, cap 1.5x, financing 6%/yr on expo>1x,
stand-down halving at VIX-pct>=0.90) used by the core today — i.e. keep the risk sizing,
change which leg of the day's return is harvested.

Conventions (house, matched to scripts/analyze_t1_overnight.py / scripts/analyze_op_d6b.py):
  o_t = Open_t / Close_{t-1} - 1      (overnight leg, RAW Open/Close — Adj Close == Close
                                        in this vault, verified below, so no split/div
                                        adjustment mismatch between Open and prior Close)
  i_t = Close_t / Open_t - 1          (intraday leg)
  gate_t = VIX-pct(t-1)               (expanding percentile, min_obs=252, house convention
                                        from quant.ladder.credit_cycle — same series `sd_full`
                                        already used by the core's own stand-down halving,
                                        pre-shifted so gate(t) uses only info through close t-1)
  "trailing |ret|" robustness gate = expanding-percentile rank of 21d realized vol
                                        (quant.ladder.fast_stress.realized_vol — the house
                                        machinery for return-magnitude dispersion; there is no
                                        separate "trailing |ret|" primitive in quant/stats, and
                                        this is the same construction T1b used for its own
                                        VIX-free robustness split), used ONLY to extend the
                                        regime split across nifty history predating the VIX
                                        vault (2007-2010-07 and 2023-04 on).

NO LOOKAHEAD: every gate and every expo value used for day t's return is computed from data
known by close of t-1 (sd_full/rv_p pre-shifted; expo already shift(1) in the book engine).

Costs: 1 round trip (sell at open, buy back at close) = 2 one-way trades, charged as
2*bp/1e4*expo(t-1) on days a round trip is ACTUALLY incurred by that variant's construction
(every day for unconditional overnight; only calm days for calm-gated; only stress days for
the hybrid — calm days there are held continuously, same as the standing core, no extra cost).
Financing (6%/yr on expo>1x) is left unchanged across variants — a margin-funding assumption
that HOLDS the loan cost constant per calendar day regardless of intraday flat/long state;
flagged as a caveat, not resolved here.
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402
from quant.ladder.fast_stress import realized_vol  # noqa: E402

ROOT = "/home/user/claude-demo"
V = f"{ROOT}/ingest/vault"

CELLS = 0


def cell(n=1):
    global CELLS
    CELLS += n


# ---- the OP-D6b book engine (pre-MAIN exec, house pattern from analyze_op_d7.py) ----
_src = open(f"{ROOT}/scripts/analyze_op_d6b.py").read()
_g = {}
exec(_src.split("# === MAIN ===")[0], _g)  # noqa: S102

run_book = _g["run_book"]
stats_of = _g["stats_of"]
dates, D0, D1, R = _g["dates"], _g["D0"], _g["D1"], _g["R"]
r_, S_, ewvol, sd_full = _g["r_"], _g["S_"], _g["ewvol"], _g["sd_full"]
np_ = _g["np"]
core_stream_orig = _g["core_stream"]  # saved so it can be restored after D's monkey-patch

# ---- raw OHLC overnight/intraday decomposition (T1 house convention) ----
nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date").sort_index()
assert (nf["Adj Close"] / nf["Close"]).sub(1).abs().max() < 1e-9, "Adj Close != Close: reconsider overnight calc"
o_full = nf["Open"] / nf["Close"].shift(1) - 1
i_full = nf["Close"] / nf["Open"] - 1
identity_gap = ((1 + o_full) * (1 + i_full) - 1 - nf["Close"].pct_change()).abs().max()
assert identity_gap < 1e-9, f"o*i identity failed: {identity_gap}"

o_ = o_full.reindex(S_.index)
i_ = i_full.reindex(S_.index)
assert o_.loc[D0:D1].isna().sum() == 0, "o_ reindex to S_.index introduced NaNs in-window — index mismatch between this script's nf load and op_d6b's"
gate = sd_full.shift(1)  # VIX-pct known as of close t-1 -> drives day-t leg choice, same
                          # timing convention as expo.shift(1) inside core_stream

THRESH = 0.60  # the book's own existing stand-down/entry VIX-pct grid point (config/ladder.yaml
                # L2; already used for the condor entry & F16/C06 stand-down) — reused here as
                # the calm/stress cut, not invented for this family.


def nw_t(x, lags=5):
    """Newey-West t-stat on a mean, house convention (scripts/analyze_t1_overnight.py)."""
    x = np.asarray(x, float)
    n = len(x)
    m = x.mean()
    e = x - m
    s = e @ e / n
    for lag in range(1, lags + 1):
        w = 1 - lag / (lags + 1)
        s += 2 * w * (e[lag:] @ e[:-lag]) / n
    return m, m / np.sqrt(max(s, 1e-30) / n)


# =====================================================================================
print(f"F01 overnight-core — window {D0.date()}..{D1.date()} "
      f"({len(dates)} trading days); VIX vault ends 2023-04-05")

# ---- A. descriptive: does the calm/stress split hold in THIS window? ----
print("\n--- A. descriptive overnight/intraday decomposition ---")

sub = pd.DataFrame({"o": o_, "i": i_}).loc[D0:D1].dropna()
mo, to = nw_t(sub["o"]); mi, ti = nw_t(sub["i"])
cell()
print(f"A1 book-window unconditional: overnight {mo*252*100:+.2f}%/yr (t={to:+.2f}) | "
      f"intraday {mi*252*100:+.2f}%/yr (t={ti:+.2f}) | n={len(sub)}")

g_book = gate.reindex(sub.index)
calm_mask = (g_book < THRESH).fillna(False)
stress_mask = ~calm_mask
mo_c, to_c = nw_t(sub.loc[calm_mask, "o"]); mi_c, ti_c = nw_t(sub.loc[calm_mask, "i"])
mo_s, to_s = nw_t(sub.loc[stress_mask, "o"]); mi_s, ti_s = nw_t(sub.loc[stress_mask, "i"])
cell()
print(f"A2 split by VIX-pct(t-1)<{THRESH} (calm, n={calm_mask.sum()}) vs >= (stress, n={stress_mask.sum()}):")
print(f"   calm:   overnight {mo_c*252*100:+.2f}%/yr (t={to_c:+.2f}) | intraday {mi_c*252*100:+.2f}%/yr (t={ti_c:+.2f})")
print(f"   stress: overnight {mo_s*252*100:+.2f}%/yr (t={to_s:+.2f}) | intraday {mi_s*252*100:+.2f}%/yr (t={ti_s:+.2f})")

# full-history (2007-2026) robustness split on the VIX-free "trailing |ret|" proxy
# NB: realized_vol's cumsum-of-squares implementation propagates a NaN forward through the
# WHOLE series if fed one (e.g. pct_change()'s leading NaN) — same trap T1b's own script
# avoided by pre-dropping NaN (`rets_clean = df.dropna(subset=["ret"])`) before calling it.
# Caught here the same way: first pass produced calm n=0 (all-NaN gate); fixed by dropping
# the leading NaN first, exactly as T1b does.
r_full = nf["Close"].pct_change().dropna()
rv_p = pd.Series(expanding_percentile(realized_vol(r_full.to_numpy(), 21), min_obs=252), index=r_full.index)
rv_gate = rv_p.shift(1).reindex(nf.index)
full = pd.DataFrame({"o": o_full, "i": i_full, "g": rv_gate}).dropna(subset=["o", "i"])
calm_f = (full["g"] < 0.90).fillna(False)  # T1b's own rv_p threshold (0.90), reused verbatim
mo_fc, to_fc = nw_t(full.loc[calm_f, "o"]); mi_fc, ti_fc = nw_t(full.loc[calm_f, "i"])
mo_fs, to_fs = nw_t(full.loc[~calm_f, "o"]); mi_fs, ti_fs = nw_t(full.loc[~calm_f, "i"])
cell()
print(f"A3 FULL-HISTORY (2007-2026) split by realized-vol-pct(t-1)<0.90 (T1b's own gate, "
      f"n={calm_f.sum()}) vs >=0.90 (n={(~calm_f).sum()}):")
print(f"   calm:   overnight {mo_fc*252*100:+.2f}%/yr (t={to_fc:+.2f}) | intraday {mi_fc*252*100:+.2f}%/yr (t={ti_fc:+.2f})")
print(f"   stress: overnight {mo_fs*252*100:+.2f}%/yr (t={to_fs:+.2f}) | intraday {mi_fs*252*100:+.2f}%/yr (t={ti_fs:+.2f})")

# =====================================================================================
print("\n--- B. standalone sleeve backtests (vol-target sized, cap 1.5x, financing on) ---")


def make_core_stream(leg, thresh=THRESH, cost_bp=0.0):
    def _core_stream(cap=1.5, financing=False):
        expo = (0.15 / ewvol).clip(upper=cap)
        expo = expo * np.where(sd_full >= 0.90, 0.5, 1.0)
        g = gate
        if leg == "full":
            leg_ret, active = r_, pd.Series(False, index=S_.index)
        elif leg == "overnight":
            leg_ret, active = o_, pd.Series(True, index=S_.index)
        elif leg == "overnight_calm":
            leg_ret = o_.where((g < thresh).fillna(False), 0.0)
            active = (g < thresh).fillna(False)
        elif leg == "hybrid":
            stress = (g >= thresh).fillna(False)
            leg_ret = pd.Series(np.where(stress, o_.fillna(0), r_.fillna(0)), index=S_.index)
            active = stress
        elif leg == "intraday":
            leg_ret, active = i_, pd.Series(False, index=S_.index)
        else:
            raise ValueError(leg)
        ret = (expo.shift(1) * leg_ret).loc[D0:D1].fillna(0)
        if cost_bp > 0:
            drag = (2 * cost_bp / 1e4) * expo.shift(1).abs() * active.astype(float)
            ret = ret - drag.loc[D0:D1].fillna(0)
        if financing:
            ret = ret - ((expo.shift(1) - 1).clip(lower=0) * R / 252).loc[D0:D1].fillna(0)
        return ret, expo
    return _core_stream


def sleeve_stats(leg, cost_bp=0.0, thresh=THRESH):
    cs = make_core_stream(leg, thresh, cost_bp)
    ret, _ = cs(cap=1.5, financing=True)
    eq = 100 * (1 + ret).cumprod()
    cagr, dd, yearly = stats_of(eq)
    vol = ret.std() * np.sqrt(252) * 100
    sharpe = (ret.mean() * 252) / (ret.std() * np.sqrt(252)) if ret.std() > 0 else np.nan
    return dict(cagr=cagr, dd=dd, vol=vol, sharpe=sharpe, worst_yr=100 * yearly.min())


VARIANTS = ["full", "overnight", "overnight_calm", "hybrid", "intraday"]
base_stats = {}
for v in VARIANTS:
    s = sleeve_stats(v, cost_bp=0.0)
    base_stats[v] = s
    cell()
    print(f"B[{v:15s}] gross: CAGR {s['cagr']:+6.2f}%/yr | vol {s['vol']:5.2f}% | "
          f"Sharpe {s['sharpe']:+.2f} | maxDD {s['dd']:6.2f}% | worst yr {s['worst_yr']:+5.1f}%")

FULL_CAGR = base_stats["full"]["cagr"]

# =====================================================================================
print(f"\n--- C. cost sensitivity (bp one-way, 1 round trip = 2 legs; standing full-day "
      f"core standalone CAGR = {FULL_CAGR:+.2f}%/yr as the bar) ---")

BPS = [0, 2, 5, 10]
cost_grid = {}
for v in ["overnight", "overnight_calm", "hybrid"]:
    cost_grid[v] = {}
    for bp in BPS:
        s = sleeve_stats(v, cost_bp=bp)
        cost_grid[v][bp] = s
        cell()
        print(f"C[{v:15s} @ {bp:2d}bp]: CAGR {s['cagr']:+6.2f}%/yr | maxDD {s['dd']:6.2f}% | "
              f"beats full-day core: {'YES' if s['cagr'] > FULL_CAGR else 'no'}")

# breakeven bp (linear interpolation on the 4 registered points, vs the full-day core CAGR)
breakeven = {}
for v in ["overnight", "overnight_calm", "hybrid"]:
    xs = np.array(BPS, float)
    ys = np.array([cost_grid[v][bp]["cagr"] for bp in BPS], float)
    if ys[0] <= FULL_CAGR:
        breakeven[v] = 0.0  # already at/under the bar gross
        continue
    # slope from a robust fit across the 4 points (cost impact ~linear for small bp)
    slope, intercept = np.polyfit(xs, ys, 1)
    be = (FULL_CAGR - intercept) / slope if slope != 0 else np.inf
    breakeven[v] = be

for v, be in breakeven.items():
    if be > 0 and np.isfinite(be) and be < 200:
        s_check = sleeve_stats(v, cost_bp=be)
        cell()
        print(f"C-breakeven[{v:15s}]: interpolated {be:.1f}bp one-way -> confirm CAGR "
              f"{s_check['cagr']:+.2f}%/yr vs full-day {FULL_CAGR:+.2f}%/yr "
              f"(gap {s_check['cagr']-FULL_CAGR:+.3f}pp)")
    else:
        print(f"C-breakeven[{v:15s}]: {'already at/below bar gross' if be <= 0 else f'>{200}bp (never crosses in a sane cost range)'}")

# =====================================================================================
print("\n--- D. book-level substitution (65/20/15 weights, financing+syn_margin ON, "
      "matches OP-D6b a5) ---")

BOOKED_A5 = dict(cagr=11.13, dd=-11.53, worst_yr=-2.3)


def book_stats(leg, cost_bp=0.0, thresh=THRESH):
    _g["core_stream"] = make_core_stream(leg, thresh, cost_bp)
    eq, pm = run_book(0.65, 0.20, 0.15, financing=True, syn_margin=True)
    cagr, dd, yearly = stats_of(eq)
    return dict(cagr=cagr, dd=dd, worst_yr=100 * yearly.min(), peak_margin=100 * pm)


_g["core_stream"] = make_core_stream("full")
b_full = book_stats("full")
cell()
print(f"D[full-day baseline, recomputed here]: CAGR {b_full['cagr']:+.2f}%/yr (booked a5 "
      f"{BOOKED_A5['cagr']:+.2f}) | maxDD {b_full['dd']:.2f}% (booked {BOOKED_A5['dd']:.2f}) | "
      f"worst yr {b_full['worst_yr']:+.1f}% (booked {BOOKED_A5['worst_yr']:+.1f})")

book_grid = {}
for v in ["overnight", "overnight_calm", "hybrid"]:
    book_grid[v] = {}
    for bp in BPS:
        b = book_stats(v, cost_bp=bp)
        book_grid[v][bp] = b
        cell()
        print(f"D[{v:15s} @ {bp:2d}bp]: CAGR {b['cagr']:+6.2f}%/yr (d {b['cagr']-b_full['cagr']:+.2f}pp) | "
              f"maxDD {b['dd']:6.2f}% (d {b['dd']-b_full['dd']:+.2f}pp) | worst yr {b['worst_yr']:+5.1f}% | "
              f"peak margin {b['peak_margin']:.1f}%")

# restore original core_stream (hygiene, in case this module is imported elsewhere)
_g["core_stream"] = core_stream_orig

# =====================================================================================
print("\n--- E. single-day forensics (why the standalone overnight sleeve's maxDD is small, "
      "and where it is NOT small) ---")

expo_full = (0.15 / ewvol).clip(upper=1.5) * np.where(sd_full >= 0.90, 0.5, 1.0)
expo_full = pd.Series(expo_full, index=S_.index)
exl_full = expo_full.shift(1)
pnl_overnight = (exl_full * o_).loc[D0:D1]
worst5 = pnl_overnight.sort_values().head(5)
cell()
print("E1 worst 5 single-day P&L prints in the standalone overnight sleeve (% of book):")
for d, v in worst5.items():
    print(f"   {d.date()}: {100*v:+.2f}% of book (expo_lag={exl_full.loc[d]:.3f}, o_t={o_.loc[d]*100:+.2f}%)")

demo = pd.DataFrame({"Open": nf["Open"], "Close": nf["Close"]}).loc["2016-11-07":"2016-11-10"]
demo["o"], demo["i"], demo["full"] = o_full.loc[demo.index], i_full.loc[demo.index], nf["Close"].pct_change().loc[demo.index]
cell()
print("E2 forensic zoom — 2016-11-09 (demonetization announced after the 2016-11-08 close):")
print(f"   overnight {demo.loc['2016-11-09','o']*100:+.2f}% (the shock, captured in FULL by "
      f"overnight-only) | intraday {demo.loc['2016-11-09','i']*100:+.2f}% (partial recovery, "
      f"captured ONLY by full-day) | full-day net {demo.loc['2016-11-09','full']*100:+.2f}%")
print(f"   at expo_lag={exl_full.loc['2016-11-09']:.3f}: overnight-only lost "
      f"{100*exl_full.loc['2016-11-09']*o_.loc['2016-11-09']:+.2f}% of book that single night vs "
      f"full-day's {100*exl_full.loc['2016-11-09']*demo.loc['2016-11-09','full']:+.2f}% — "
      "a gap-then-recover event where the full-day core suffered LESS than overnight-only, "
      "the opposite of the COVID case (E1) where slow vol buildup had already de-risked the "
      "overnight sleeve before the worst gap (expo_lag 0.13x by 2020-03-23 vs {:.2f}x here)".format(
          exl_full.loc["2016-11-09"]))

print(f"\nTOTAL CELLS CONSUMED: {CELLS}")
