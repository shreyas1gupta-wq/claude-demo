#!/usr/bin/env python3
"""OP-D2 family F16 — THE MONTHLY PAPER SIM (registered: research/register/trial-ledger.md,
Entry OP-D2, 2026-09-07): "daily-managed BS condor (entry VIXpct>=0.6, wings 2.5 sigma,
VIX-flat vol) mgmt {hold, stop-2x-credit, delta-band roll} 2010-23 (3) — BAR: stop-2x
cuts worst month >= 50% at <= 30% mean cost."

Registered cells (3):
  1. hold            : baseline, hold to expiry — DESCRIPTIVE (no bar registered)
  2. stop_2x_credit  : PASS/MISS vs the registered bar (worst-month cut >= 50% of hold's
                       at mean-P&L cost <= 30% of hold's mean)
  3. delta_band_roll : DESCRIPTIVE (registered without its own bar)

Declared conventions (header of record; all fixed BEFORE the run):
  - Vault only: NIFTY daily Adj Close (index/nifty50_daily_2007_2026.csv) x India VIX
    close (vix/india_vix_daily_2010_2023.csv), inner-merged on date (2010-07..2023-04).
  - VIX percentile = expanding_percentile(vix, min_obs=252) from quant.ladder.credit_cycle
    (expanding, no lookahead by construction).
  - Monthly cycle: consecutive NON-OVERLAPPING 21-trading-day blocks starting at the first
    date with a valid VIX percentile. Entry at block start t0 iff VIXpct[t0] >= 0.6
    (state at t0 uses data <= t0 only). Expiry = t0 + 21 trading days.
  - Condor (matches F15's structure quoting this registration): short +/-1.0-sigma
    strangle + long +/-2.5-sigma wings; K = S0*exp(k*sig0*sqrt(T0)), sig0 = VIX[t0]/100,
    T = remaining trading days / 252. BS European, r=0.06, q=0, VIX-flat vol: every daily
    mark reprices ALL legs at that day's VIX/100. P&L in % of entry spot (index points
    scale linearly; no magic level).
  - Credit C0 = value of shorts - value of longs at entry. Daily cost-to-close = same
    structure marked at (S_t, VIX_t, T_rem); at expiry, intrinsic.
  - stop-2x-credit: close at the first daily CLOSE mark where cost-to-close >= 2*C0
    (loss = C0); no intraday fills. Else hold to expiry.
  - delta-band roll: band |delta|>=0.30 on either short leg (daily close). On breach with
    T_rem >= 3 trading days: close the whole condor at mark, re-open a fresh 1.0/2.5-sigma
    condor centred at current S with current VIX and the SAME expiry, collect new credit;
    max 3 rolls per month (then hold). Month P&L = sum over legs of (credit - close cost).
  - Bar arithmetic: worst months are losses; cut = 1 - |worst_stop|/|worst_hold| >= 0.50;
    cost = (mean_hold - mean_stop)/mean_hold <= 0.30 (requires mean_hold > 0). Both must
    hold for PASS; otherwise MISS. No costs/slippage (paper sim; stated in caveats).
  - No BS machinery in quant/ (F15 checked); closed forms implemented here. Process note
    #6 concerns quant/stats estimators — nothing statistical is re-implemented.
Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/f16.py
"""
import math
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile

REPO = "/home/user/claude-demo"
R = 0.06
BODY_SIG, WING_SIG = 1.0, 2.5
TENOR = 21                # trading days
ENTRY_PCT = 0.60
STOP_MULT = 2.0
DELTA_BAND = 0.30
MIN_ROLL_TREM = 3         # trading days
MAX_ROLLS = 3
MIN_OBS = 252


def _ncdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs_price_delta(S, K, T, sig, cp):
    """European BS price and delta, q=0, r=R. cp=+1 call, -1 put. T in years."""
    if T <= 0:
        intr = max(cp * (S - K), 0.0)
        return intr, (cp if cp * (S - K) > 0 else 0.0)
    sq = sig * math.sqrt(T)
    d1 = (math.log(S / K) + (R + 0.5 * sig * sig) * T) / sq
    d2 = d1 - sq
    if cp > 0:
        return S * _ncdf(d1) - K * math.exp(-R * T) * _ncdf(d2), _ncdf(d1)
    return K * math.exp(-R * T) * _ncdf(-d2) - S * _ncdf(-d1), _ncdf(d1) - 1.0


def make_strikes(S, sig, T):
    sq = sig * math.sqrt(T)
    return dict(kp2=S * math.exp(-WING_SIG * sq), kp1=S * math.exp(-BODY_SIG * sq),
                kc1=S * math.exp(BODY_SIG * sq), kc2=S * math.exp(WING_SIG * sq))


def condor_mark(S, K, T, sig):
    """Cost to close the short condor (+deltas of the two SHORT legs)."""
    pc1, dc1 = bs_price_delta(S, K["kc1"], T, sig, +1)
    pc2, _ = bs_price_delta(S, K["kc2"], T, sig, +1)
    pp1, dp1 = bs_price_delta(S, K["kp1"], T, sig, -1)
    pp2, _ = bs_price_delta(S, K["kp2"], T, sig, -1)
    return (pc1 - pc2) + (pp1 - pp2), dc1, dp1


def run():
    px = pd.read_csv(f"{REPO}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                     parse_dates=["Date"]).set_index("Date")["Adj Close"]
    vx = pd.read_csv(f"{REPO}/ingest/vault/vix/india_vix_daily_2010_2023.csv",
                     parse_dates=["date"]).set_index("date")["close"]
    df = pd.concat({"S": px, "vix": vx}, axis=1, join="inner").dropna().sort_index()
    df["pct"] = expanding_percentile(df["vix"].values, min_obs=MIN_OBS)
    print(f"merged sample {df.index[0].date()}..{df.index[-1].date()} n={len(df)}; "
          f"first valid VIXpct {df.index[MIN_OBS-1].date()}")

    S = df["S"].values
    V = df["vix"].values / 100.0
    P = df["pct"].values
    dates = df.index

    starts = list(range(MIN_OBS - 1, len(df) - TENOR, TENOR))
    months = []  # (date, pnl_hold, pnl_stop, stopped, pnl_roll, nrolls) in % of S0
    for t0 in starts:
        if np.isnan(P[t0]) or P[t0] < ENTRY_PCT:
            continue
        S0, sig0 = S[t0], V[t0]
        T0 = TENOR / 252.0
        K0 = make_strikes(S0, sig0, T0)
        C0, _, _ = condor_mark(S0, K0, T0, sig0)

        # --- hold + stop-2x on one daily walk of the same position
        stop_pnl, stopped = None, False
        for j in range(1, TENOR + 1):
            Trem = (TENOR - j) / 252.0
            cost, _, _ = condor_mark(S[t0 + j], K0, Trem, V[t0 + j])
            if not stopped and cost >= STOP_MULT * C0:
                stop_pnl, stopped = C0 - cost, True
        hold_pnl = C0 - cost  # last cost is the expiry intrinsic (Trem=0)
        if not stopped:
            stop_pnl = hold_pnl

        # --- delta-band roll
        roll_pnl, nrolls = 0.0, 0
        K, credit = K0, C0
        for j in range(1, TENOR + 1):
            Trem = (TENOR - j) / 252.0
            cost, dc, dp = condor_mark(S[t0 + j], K, Trem, V[t0 + j])
            if j < TENOR and nrolls < MAX_ROLLS and (TENOR - j) >= MIN_ROLL_TREM \
                    and max(abs(dc), abs(dp)) >= DELTA_BAND:
                roll_pnl += credit - cost
                K = make_strikes(S[t0 + j], V[t0 + j], Trem)
                credit, _, _ = condor_mark(S[t0 + j], K, Trem, V[t0 + j])
                nrolls += 1
        roll_pnl += credit - cost
        months.append((dates[t0], 100 * hold_pnl / S0, 100 * stop_pnl / S0, stopped,
                       100 * roll_pnl / S0, nrolls))

    m = pd.DataFrame(months, columns=["entry", "hold", "stop", "stopped", "roll", "nrolls"])
    ntot = len(starts)
    print(f"monthly blocks {ntot}, entered (VIXpct>={ENTRY_PCT}) {len(m)}; "
          f"stops triggered {int(m.stopped.sum())}; rolled months {(m.nrolls > 0).sum()} "
          f"(total rolls {int(m.nrolls.sum())})")
    for c in ["hold", "stop", "roll"]:
        x = m[c]
        print(f"{c:5s}: mean {x.mean():+.3f} %S/mo | worst {x.min():+.3f} "
              f"({m.loc[x.idxmin(), 'entry'].date()}) | hit rate {(x > 0).mean():.2f} "
              f"| p5 {x.quantile(0.05):+.3f}")

    wh, ws, wr = m.hold.min(), m.stop.min(), m.roll.min()
    mh, ms, mr = m.hold.mean(), m.stop.mean(), m.roll.mean()
    cut_s = 1 - abs(ws) / abs(wh)
    cost_s = (mh - ms) / mh if mh > 0 else float("nan")
    cut_r = 1 - abs(wr) / abs(wh)
    cost_r = (mh - mr) / mh if mh > 0 else float("nan")
    print(f"stop-2x: worst-month cut {100*cut_s:.1f}% (bar >=50) | "
          f"mean cost {100*cost_s:.1f}% (bar <=30) | mean_hold>0: {mh > 0}")
    verdict = "PASS" if (mh > 0 and cut_s >= 0.50 and cost_s <= 0.30) else "MISS"
    print(f"stop-2x VERDICT vs registered bar: {verdict}")
    print(f"delta-roll (no bar, descriptive): worst-month cut {100*cut_r:.1f}% | "
          f"mean cost {100*cost_r:.1f}%")


if __name__ == "__main__":
    run()
