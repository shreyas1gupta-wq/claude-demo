"""opt_sweep2 / f10_tom_overlay — TURN-OF-MONTH BOOK ADD-ON.

PRE-REGISTRATION (written before any number below is computed).

Ledger precedent (research/register/trial-ledger.md, grep "T6-TOM", quoted verbatim):
  Design: "ToM window = last trading day of month + first 4 of the next (the
  Lakonishok-Smidt convention, fixed); mean daily return in-window vs out, full sample +
  era split at BR6 (2007-2015-03 vs 2015-04-2026)."
  Bars: (i) ToM premium present full-sample (p<0.05); (ii) H61 fingerprint = in-window
  minus out-of-window mean LARGER post-BR6 (SIP era) than pre.
  Result: "Bar (i) PASS: full-sample ToM premium +7.2bp/day (p=0.025). Bar (ii) the
  fingerprint is ABSENT — booked against H61's index-level relevance: the premium SHRANK
  across BR6 (+12.2bp/d pre-2015 -> +3.8bp/d, p=0.29 in the SIP era)."
  CONSUMPTION CAP (verbatim): "no trade from either print (calendar tilts live under L5's
  regime and CW's cost discipline); T6 feeds H61's motivation and the deployment-timing
  playbook only."

READING FOR THIS FAMILY: TOM "survived" bar (i) — the premium is real full-sample — so
this family runs per the assigned design (+0.3x book add-on, days -4..+2 around
month-end, calm-gated, financed at 6%, 10% margin). But two things are flagged BEFORE
computing: (a) the ledger's own CONSUMPTION CAP explicitly foreclosed trading either T6
print; (b) the era-split shows the premium is INSIGNIFICANT (p=0.29) in the SIP era
(2015-04 on) — and the standing book's own test window (2011-07..2023-03) is >85% SIP-era
by trading days. Prior stated NOW: expect a small, likely statistically indistinguishable-
from-zero CAGR add once 6% financing is charged on the incremental exposure, and this
script's own job is to find out honestly, not to talk itself into a trade the ledger
already cordoned off.

FROZEN DESIGN (exact parameters, no post-hoc tuning):
  - Window: trading-day offsets -4..+2 relative to each month's LAST TRADING DAY (offset
    0), i.e. the last 4 trading days of the closing month + month-end + first 2 trading
    days of the next month (7 trading days/month-turn). NOTE this is NOT the ledger's
    window (last day + next 4) — it is the window this sweep's brief specifies; built
    fresh, not reused from T6.
  - Add-on: +0.30x of book NAV, additive to the standing book's daily return (book-
    relative, matches run_book's extra_ret/extra_margin convention) — this is INCREMENTAL
    exposure, not a re-weighting of the core sleeve.
  - Calm gate: VIX-pct(t-1) < 0.60 (house convention, quant.ladder.credit_cycle.
    expanding_percentile, min_obs=252; same 0.60 cut already used by the book's condor
    entry/stand-down — not invented for this family). Gate uses ONLY the percentile as
    known through the PRIOR close (sd_full.shift(1)), matching core_stream's own timing.
  - Financing: 6%/yr (R, same constant as the book engine) on the add-on notional,
    charged every day the add-on is active (it is fully incremental margin exposure, no
    "free" first turn the way the core's expo<=1x is unfinanced).
  - Margin: 10% of the add-on notional while active (principal's unhedged-notional rule),
    i.e. 0.10 * 0.30 = 3.0% of book on active days, 0 otherwise.
  - Window is calendar-deterministic (known arbitrarily far in advance) -> no lookahead by
    construction; the only conditioning signal (the calm gate) is lagged one day.

CELLS (pre-declared, counted honestly in the script; see CELLS_LOG at the bottom):
  A1/A2: standalone replicate of the window's daily-return edge on THIS book's own NIFTY
         series/window (own -4..+2 definition, not T6's), raw and calm-gated.
  B:     baseline book (OP-D6b a5, 65/20/15, financing+syn_margin ON) recomputed here.
  C:     book + frozen ToM add-on (calm-gated, financed, margined) — THE DESIGN.
  D:     sensitivity — same add-on with the calm gate REMOVED (always-on in-window), to
         see how much of any edge is the gate vs the calendar effect alone.
  E:     era split (BR6, 2015-04) of the add-on's OWN standalone daily return, replicating
         the ledger's fingerprint check on this book's own window definition.
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")

ROOT = "/home/user/claude-demo"

CELLS = 0


def cell(n=1):
    global CELLS
    CELLS += n


def nw_t(x, lags=5):
    """Newey-West t-stat on a mean (house convention, scripts/analyze_t1_overnight.py /
    scripts/opt_sweep2/f01_overnight_core.py — no shared quant/stats primitive exists for
    this, confirmed by inspection of quant/stats/*.py before writing this)."""
    x = np.asarray(x, float)
    n = len(x)
    m = x.mean()
    e = x - m
    s = e @ e / n
    for lag in range(1, lags + 1):
        w = 1 - lag / (lags + 1)
        s += 2 * w * (e[lag:] @ e[:-lag]) / n
    return m, m / np.sqrt(max(s, 1e-30) / n)


# ---- the OP-D6b book engine (pre-MAIN exec, house pattern from analyze_op_d7.py) ----
_src = open(f"{ROOT}/scripts/analyze_op_d6b.py").read()
_g = {}
exec(_src.split("# === MAIN ===")[0], _g)  # noqa: S102

run_book = _g["run_book"]
stats_of = _g["stats_of"]
dates, D0, D1, R = _g["dates"], _g["D0"], _g["D1"], _g["R"]
r_, S_, sd_full = _g["r_"], _g["S_"], _g["sd_full"]

print(f"F10 TOM overlay — window {D0.date()}..{D1.date()} ({len(dates)} trading days); "
      "India VIX vault ends 2023-04-05 (< book D1 2023-03-31, covered)")

# =====================================================================================
# window construction: -4..+2 trading days around each month's LAST trading day, built
# on the FULL nifty calendar (2007-2026) so month-boundary windows near D0/D1 are correct
# even where the neighbouring month-end sits outside [D0,D1].
all_idx = S_.index
pos_of_me = {}
for i, d in enumerate(all_idx):
    pos_of_me[(d.year, d.month)] = i  # last i wins per (y,m) -> last trading day of month
me_positions = sorted(pos_of_me.values())
win_arr = np.zeros(len(all_idx), dtype=bool)
for p in me_positions:
    lo, hi = max(p - 4, 0), min(p + 2, len(all_idx) - 1)
    win_arr[lo:hi + 1] = True
window_flag_full = pd.Series(win_arr, index=all_idx)

window_flag = window_flag_full.reindex(dates).fillna(False)
calm_prev = (sd_full.shift(1) < 0.60).reindex(dates).fillna(False)
active = window_flag & calm_prev
active_nogate = window_flag

n_win = int(window_flag.sum())
n_active = int(active.sum())
print(f"window days in-book: {n_win} ({100*n_win/len(dates):.1f}% of {len(dates)} td) | "
      f"calm-gated active days: {n_active} ({100*n_active/len(dates):.1f}%)")

# =====================================================================================
print("\n--- A. descriptive replicate (this script's own -4..+2 window, NOT T6's) ---")

r_book = r_.reindex(dates)
in_win = r_book[window_flag]
out_win = r_book[~window_flag]
m_in, t_in = nw_t(in_win)
m_out, t_out = nw_t(out_win)
cell()
print(f"A1 raw: in-window mean {m_in*1e4:+.2f}bp/day (t={t_in:+.2f}, n={len(in_win)}) vs "
      f"out-of-window {m_out*1e4:+.2f}bp/day (t={t_out:+.2f}, n={len(out_win)}) | "
      f"diff {(m_in-m_out)*1e4:+.2f}bp/day")

in_win_calm = r_book[window_flag & calm_prev]
out_win_calm = r_book[(~window_flag) & calm_prev]
m_inc, t_inc = nw_t(in_win_calm)
m_outc, t_outc = nw_t(out_win_calm)
cell()
print(f"A2 calm-gated (VIX-pct(t-1)<0.60 both legs): in-window {m_inc*1e4:+.2f}bp/day "
      f"(t={t_inc:+.2f}, n={len(in_win_calm)}) vs out-of-window {m_outc*1e4:+.2f}bp/day "
      f"(t={t_outc:+.2f}, n={len(out_win_calm)}) | diff {(m_inc-m_outc)*1e4:+.2f}bp/day")

# =====================================================================================
print("\n--- B/C/D. book-level backtests (65/20/15, financing+syn_margin ON, matches "
      "OP-D6b a5) ---")

BOOKED_A5 = dict(cagr=11.13, dd=-11.53, worst_yr=-2.3, peak_margin=22.2)

eq_base, pm_base = run_book(0.65, 0.20, 0.15, financing=True, syn_margin=True)
c_base, d_base, y_base = stats_of(eq_base)
cell()
print(f"B baseline (recomputed here): CAGR {c_base:+.2f}%/yr (booked a5 {BOOKED_A5['cagr']:+.2f}) "
      f"| maxDD {d_base:.2f}% (booked {BOOKED_A5['dd']:.2f}) | worst yr "
      f"{100*y_base.min():+.1f}% (booked {BOOKED_A5['worst_yr']:+.1f}) | peak margin "
      f"{100*pm_base:.1f}% (booked {BOOKED_A5['peak_margin']:.1f})")

ADDON, MARGIN_FRAC = 0.30, 0.10


def addon_streams(act):
    act_f = act.astype(float)
    # financing is on the ADD-ON notional (0.3x book), not the whole book -- the add-on
    # itself is the only borrowed piece here.
    ex_ret = ADDON * act_f * r_book - ADDON * act_f * R / 252
    ex_margin = MARGIN_FRAC * ADDON * act_f
    return ex_ret, ex_margin


extra_ret_c, extra_margin_c = addon_streams(active)
eq_c, pm_c = run_book(0.65, 0.20, 0.15, financing=True, syn_margin=True,
                       extra_ret=extra_ret_c, extra_margin=extra_margin_c)
c_c, d_c, y_c = stats_of(eq_c)
cell()
print(f"C book+TOM overlay (frozen design, calm-gated): CAGR {c_c:+.2f}%/yr "
      f"(d {c_c-c_base:+.2f}pp) | maxDD {d_c:.2f}% (d {d_c-d_base:+.2f}pp) | worst yr "
      f"{100*y_c.min():+.1f}% | peak margin {100*pm_c:.1f}% (d {100*(pm_c-pm_base):+.1f}pp)")

extra_ret_d, extra_margin_d = addon_streams(active_nogate)
eq_d, pm_d = run_book(0.65, 0.20, 0.15, financing=True, syn_margin=True,
                       extra_ret=extra_ret_d, extra_margin=extra_margin_d)
c_d, d_d, y_d = stats_of(eq_d)
cell()
print(f"D sensitivity, calm gate REMOVED (always-on in-window): CAGR {c_d:+.2f}%/yr "
      f"(d {c_d-c_base:+.2f}pp) | maxDD {d_d:.2f}% (d {d_d-d_base:+.2f}pp) | worst yr "
      f"{100*y_d.min():+.1f}% | peak margin {100*pm_d:.1f}%")

# =====================================================================================
print("\n--- E. era split (BR6, 2015-04) of the add-on's own standalone daily return ---")

BR6 = pd.Timestamp("2015-04-01")
raw_addon_ret = window_flag.astype(float) * r_book  # unlevered, ungated, uncosted diagnostic
pre = raw_addon_ret[(dates < BR6) & window_flag]
post = raw_addon_ret[(dates >= BR6) & window_flag]
m_pre, t_pre = nw_t(pre)
m_post, t_post = nw_t(post)
cell()
print(f"E pre-BR6 (2011-07..2015-03) in-window mean {m_pre*1e4:+.2f}bp/day (t={t_pre:+.2f}, "
      f"n={len(pre)}) vs post-BR6 (2015-04..2023-03) {m_post*1e4:+.2f}bp/day (t={t_post:+.2f}, "
      f"n={len(post)}) | fingerprint (post>pre)? {'YES' if m_post > m_pre else 'NO — shrank/reversed, consistent with T6 ledger print'}")

# ---- diagnostic only (no new cell: reporting already-computed y_c/y_base yearly series) ----
print("\n--- diagnostic: yearly compare, book+overlay(C) vs baseline(B) ---")
yc_map = {d.year: 100 * v for d, v in y_c.items()}
yb_map = {d.year: 100 * v for d, v in y_base.items()}
for yr in sorted(set(yc_map) | set(yb_map)):
    print(f"   {yr}: base {yb_map.get(yr, float('nan')):+6.2f}% | +TOM {yc_map.get(yr, float('nan')):+6.2f}%")

print(f"\nTOTAL CELLS CONSUMED: {CELLS}")
