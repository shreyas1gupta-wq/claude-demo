#!/usr/bin/env python3
"""Development-window exploration for the India core signal. Nothing here touches the out-of-sample data.

DEV: Nifty Midcap 50, 2014-05-15 .. 2019-12-31 (India VIX starts 2014-05, so all families share a window).
Families tested: buy & hold, volatility targeting, India-VIX gating, long-horizon momentum, drawdown exits,
and combinations. Selection is by Sharpe and Calmar jointly, with a turnover penalty.
"""
from __future__ import annotations
import sys, warnings
from pathlib import Path
import numpy as np, pandas as pd

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "model"))
import engine as E, features as F, costs  # noqa: E402

IN = pd.read_csv(HERE / "data" / "india_daily.csv", parse_dates=["date"]).set_index("date")
ONEWAY = costs.futures_round_turn(1_500_000, 4.0)["bp_of_notional"] / 2 * 1.5
DEV0, DEV1 = "2014-05-15", "2019-12-31"


def frame(k):
    d = pd.DataFrame(index=IN.index)
    d["spx_px"], d["spx_ret"] = IN[k], IN[f"{k}_ret"]
    d["rf_daily"] = IN["cash_ret"]
    d["spx_tr_ret"] = IN[f"{k}_x"] + IN["cash_ret"]
    d["vix_close"] = IN["vix"]
    return d.dropna(subset=["spx_px"])


def hold(lev, n):
    out = lev.to_numpy(dtype=float).copy(); cur, held = out[0], 0
    for i in range(1, len(out)):
        if out[i] != cur and held < n: out[i] = cur
        elif out[i] != cur: cur, held = out[i], 0
        held += 1
    return pd.Series(out, index=lev.index)


def wk(lev, df):
    w = pd.Series(df.index.isocalendar().week.values, index=df.index)
    return lev.where(w.ne(w.shift(-1))).ffill().fillna(0.0)


def ev(df, lev, s=DEV0, e=DEV1, cost=ONEWAY, rolls=12):
    r = E.run(df, lev, asset="spx_tr", cost_bps=cost, start=s, end=e)
    m = r.metrics()
    drag = cost * 2 * rolls * m["avg_leverage"] / 100
    return dict(cagr=m["annualized_return_pct"], net=m["annualized_return_pct"] - drag, sharpe=m["sharpe"],
                dd=m["max_drawdown_pct"], calmar=m["calmar"], chg=m["position_changes_per_year"],
                lev=m["avg_leverage"], vol=m["annualized_std_dev"], cash=m["pct_days_cash"])


def q(lev, lo=0.0, hi=2.0, step=0.25):
    return (lev / step).round() * step


# ---------------------------------------------------------------- signal families
def f_buyhold(df, lev=1.0):
    return pd.Series(lev, index=df.index)


def f_voltarget(df, tv=0.18, mx=2.0, hl=40, min_days=20):
    raw = (tv / F.ewma_vol(df["spx_ret"], hl)).clip(0.25, mx)
    return hold(q(raw), min_days)


def f_vix_gate(df, tv=0.18, mx=2.0, hl=40, vix_hi=22.0, min_days=20):
    """Volatility-sized, but cut to half size when India VIX is above `vix_hi`."""
    raw = (tv / F.ewma_vol(df["spx_ret"], hl)).clip(0.25, mx)
    v = df["vix_close"].ffill()
    raw = raw.where(v <= vix_hi, raw * 0.5)
    return hold(q(raw), min_days)


def f_vix_spike(df, tv=0.18, mx=2.0, hl=40, jump=0.25, cool=10, min_days=20):
    """Volatility-sized, flat for `cool` days after India VIX jumps `jump` above its 10-day average."""
    raw = (tv / F.ewma_vol(df["spx_ret"], hl)).clip(0.25, mx)
    v = df["vix_close"].ffill()
    spike = v > F.sma(v, 10) * (1 + jump)
    out = spike.rolling(int(cool), min_periods=1).max().fillna(0) > 0
    return hold(q(raw.where(~out, 0.0)), min_days)


def f_mom12(df, tv=0.18, mx=2.0, hl=40, look=252, min_days=20):
    """Volatility-sized, but flat while 12-month momentum is negative."""
    raw = (tv / F.ewma_vol(df["spx_ret"], hl)).clip(0.25, mx)
    mom = F.momentum(df["spx_px"], look)
    return hold(q(raw.where(mom > 0, 0.0)), min_days)


def f_dd_exit(df, tv=0.18, mx=2.0, hl=40, dd_out=0.20, dd_in=0.08, min_days=20):
    raw = (tv / F.ewma_vol(df["spx_ret"], hl)).clip(0.25, mx)
    dd = F.drawdown_from_high(df["spx_px"], 252)
    inv = ~F.hysteresis(dd < -dd_out, dd > -dd_in, initial=False)
    return hold(q(raw.where(inv, 0.0)), min_days)


def f_combo(df, tv=0.18, mx=2.0, hl=40, look=252, jump=0.30, cool=10, min_days=20):
    """Volatility-sized; flat if 12-month momentum is negative OR India VIX has just spiked."""
    raw = (tv / F.ewma_vol(df["spx_ret"], hl)).clip(0.25, mx)
    v = df["vix_close"].ffill()
    spike = (v > F.sma(v, 10) * (1 + jump)).rolling(int(cool), min_periods=1).max().fillna(0) > 0
    mom = F.momentum(df["spx_px"], look)
    return hold(q(raw.where((mom > 0) & ~spike, 0.0)), min_days)


def main():
    mc50 = frame("mc50")
    rows = []
    for lv in [1.0, 1.25, 1.5, 2.0]:
        rows.append({"family": "buy & hold", "p": f"{lv}x", **ev(mc50, f_buyhold(mc50, lv), rolls=12)})
    for tv in [0.14, 0.18, 0.22]:
        for mx in [1.5, 2.0]:
            rows.append({"family": "vol target", "p": f"tv{tv} mx{mx}", **ev(mc50, f_voltarget(mc50, tv, mx))})
    for vh in [18, 22, 26]:
        rows.append({"family": "vol target + VIX level", "p": f"vix>{vh}", **ev(mc50, f_vix_gate(mc50, vix_hi=vh))})
    for j in [0.20, 0.30, 0.40]:
        rows.append({"family": "vol target + VIX spike exit", "p": f"jump{j}", **ev(mc50, f_vix_spike(mc50, jump=j))})
    for lk in [126, 189, 252]:
        rows.append({"family": "vol target + 12m momentum", "p": f"look{lk}", **ev(mc50, f_mom12(mc50, look=lk))})
    for do in [0.15, 0.20, 0.25]:
        rows.append({"family": "vol target + drawdown exit", "p": f"dd{do}", **ev(mc50, f_dd_exit(mc50, dd_out=do))})
    for j in [0.25, 0.35]:
        for lk in [189, 252]:
            rows.append({"family": "combo mom+VIX", "p": f"look{lk} jump{j}", **ev(mc50, f_combo(mc50, look=lk, jump=j))})
    t = pd.DataFrame(rows)
    t["score"] = t.sharpe + 0.5 * t.calmar - 0.02 * t.chg
    print(f"=== DEVELOPMENT: Nifty Midcap 50, {DEV0} .. {DEV1}, MIDCPNIFTY futures cost, 12 rolls/yr ===")
    print(t.sort_values("score", ascending=False).round(3).to_string(index=False))
    t.to_csv(HERE / "dev_core_grid.csv", index=False)


if __name__ == "__main__":
    main()
