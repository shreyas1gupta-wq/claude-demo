#!/usr/bin/env python3
"""Indian midcaps drift up hard and mean-revert; full trend-following timing destroys value.
This tests the opposite posture: stay invested, size by volatility, and step aside ONLY for genuine
crashes. Development on Midcap 50 2012-2019; out-of-sample 2020+ and Midcap Select 2021-09+.

Run:  python3 crash_overlay.py
"""
from __future__ import annotations
import json, sys, warnings
from pathlib import Path
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "model"))
import engine as E, features as F, costs  # noqa: E402

IN = pd.read_csv(HERE / "data" / "india_daily.csv", parse_dates=["date"]).set_index("date")
SAFETY = 1.5
RT_FUT = costs.futures_round_turn(1_500_000, 4.0)["bp_of_notional"]
RT_SYN90 = costs.cost_per_unit_exposure(24000, 1_500_000, [("C", 1.0, 1), ("P", 1.0, -1)], 0.13, 90, 35)["bp_of_notional"]
# MIDCPNIFTY monthly synthetic: higher IV, wider spreads than Nifty
RT_MCS_SYN = costs.cost_per_unit_exposure(15000, 1_500_000, [("C", 1.0, 1), ("P", 1.0, -1)], 0.18, 30, 60)["bp_of_notional"]
ONEWAY_FUT, ONEWAY_SYN = RT_FUT / 2 * SAFETY, RT_MCS_SYN / 2 * SAFETY
DEV0, DEV1, OOS0 = "2012-02-22", "2019-12-31", "2020-01-01"


def frame(k):
    d = pd.DataFrame(index=IN.index)
    d["spx_px"], d["spx_ret"] = IN[k], IN[f"{k}_ret"]
    d["rf_daily"] = IN["cash_ret"]
    d["spx_tr_ret"] = IN[f"{k}_x"] + IN["cash_ret"]
    d["vix_close"] = IN["vix"]
    return d.dropna(subset=["spx_px"])


def hold(lev, min_days):
    out = lev.to_numpy(dtype=float).copy(); cur, held = out[0], 0
    for i in range(1, len(out)):
        if out[i] != cur and held < min_days: out[i] = cur
        elif out[i] != cur: cur, held = out[i], 0
        held += 1
    return pd.Series(out, index=lev.index)


def sig_crash_only(df, base_lev=1.5, dd_exit=0.13, dd_reenter=0.06, shock_z=3.5, cool=15, min_days=10):
    """Always invested at `base_lev`, except: go flat when the index is more than `dd_exit` below its
    one-year high (a real bear, not a dip) or after a `shock_z`-sigma daily loss; come back when the
    drawdown recovers to within `dd_reenter` of the high."""
    px, ret = df["spx_px"], df["spx_ret"]
    dd = F.drawdown_from_high(px, 252)
    rv = F.realized_vol(ret, 21)
    out_ = dd < -dd_exit
    in_ = dd > -dd_reenter
    state = ~F.hysteresis(out_, in_, initial=False)          # True = invested
    shock = ret < -shock_z * rv / np.sqrt(252)
    state = state & ~(shock.rolling(int(cool), min_periods=1).max().fillna(0) > 0)
    return hold(pd.Series(np.where(state, base_lev, 0.0), index=df.index), min_days)


def sig_voltgt_always(df, target_vol=0.20, max_lev=2.0, min_days=20, hl=40, dd_exit=0.0):
    """Always invested, position sized to a constant risk target (no timing at all unless dd_exit>0)."""
    ret, px = df["spx_ret"], df["spx_px"]
    raw = (target_vol / F.ewma_vol(ret, hl)).clip(0.25, max_lev)
    lev = (raw * 4).round() / 4
    if dd_exit > 0:
        dd = F.drawdown_from_high(px, 252)
        lev[dd < -dd_exit] = 0.0
    return hold(lev, min_days)


def ev(df, lev, s, e, cost, rolls, avg_lev_override=None):
    r = E.run(df, lev, asset="spx_tr", cost_bps=cost, start=s, end=e)
    m = r.metrics()
    al = avg_lev_override if avg_lev_override is not None else m["avg_leverage"]
    drag = (cost * 2) * rolls * al / 100.0
    return dict(cagr=m["annualized_return_pct"], net=m["annualized_return_pct"] - drag, sharpe=m["sharpe"],
                dd=m["max_drawdown_pct"], calmar=m["calmar"], chg=m["position_changes_per_year"],
                cash=m["pct_days_cash"], lev=al, vol=m["annualized_std_dev"], roll_drag=drag)


def main():
    mc50, mcs = frame("mc50"), frame("mcs")
    res = {"round_turn_bp": {"mcs_futures": RT_FUT, "nifty_90d_synthetic": RT_SYN90, "mcs_30d_synthetic": RT_MCS_SYN},
           "safety": SAFETY}
    print(f"Round turns (bp of notional): MIDCPNIFTY futures {RT_FUT:.2f} | MIDCPNIFTY 30d synthetic {RT_MCS_SYN:.2f} | Nifty 90d synthetic {RT_SYN90:.2f}")

    # ---------- development ----------
    grid = []
    for bl in [1.0, 1.5, 2.0]:
        for de in [0.10, 0.13, 0.17, 0.22]:
            l = sig_crash_only(mc50, base_lev=bl, dd_exit=de)
            grid.append({"family": "crash_only", "base_lev": bl, "dd_exit": de, **ev(mc50, l, DEV0, DEV1, ONEWAY_FUT, 12)})
    for tv in [0.16, 0.20, 0.25]:
        for mx in [1.5, 2.0, 3.0]:
            for de in [0.0, 0.17]:
                l = sig_voltgt_always(mc50, target_vol=tv, max_lev=mx, dd_exit=de)
                grid.append({"family": "voltgt", "target_vol": tv, "max_lev": mx, "dd_exit": de, **ev(mc50, l, DEV0, DEV1, ONEWAY_FUT, 12)})
    for lv in [1.0, 1.5, 2.0]:
        grid.append({"family": "buy_hold", "base_lev": lv, **ev(mc50, E.buy_and_hold(mc50, lv), DEV0, DEV1, ONEWAY_FUT, 12)})
    g = pd.DataFrame(grid)
    print("\n=== DEVELOPMENT: Midcap 50, 2012-02..2019-12, MIDCPNIFTY futures cost, monthly roll ===")
    print(g.sort_values("sharpe", ascending=False).head(12).round(3).to_string(index=False))
    res["dev_grid"] = g.to_dict("records")

    cand = g[g.family != "buy_hold"].sort_values("sharpe", ascending=False).iloc[0]
    print(f"\nBEST NON-PASSIVE ON DEVELOPMENT: {dict((k, cand.get(k)) for k in ['family','base_lev','dd_exit','target_vol','max_lev'] if not pd.isna(cand.get(k)))}")
    res["chosen"] = {k: (None if pd.isna(cand.get(k)) else float(cand.get(k))) for k in ["base_lev", "dd_exit", "target_vol", "max_lev"]}
    res["chosen"]["family"] = cand["family"]

    def build(df):
        if cand["family"] == "crash_only":
            return sig_crash_only(df, base_lev=cand["base_lev"], dd_exit=cand["dd_exit"])
        return sig_voltgt_always(df, target_vol=cand["target_vol"], max_lev=cand["max_lev"], dd_exit=cand["dd_exit"])

    # ---------- out of sample, both implementations ----------
    rows = []
    for label, df, s in [("Midcap 50 (2020+)", mc50, OOS0), ("Midcap Select (2021-09+)", mcs, "2021-09-16")]:
        lev = build(df)
        al = E.run(df, lev, asset="spx_tr", cost_bps=0.0, start=s).metrics()["avg_leverage"]
        rows.append({"window": label, "impl": "model, MIDCPNIFTY futures (12 rolls)", **ev(df, lev, s, None, ONEWAY_FUT, 12, al)})
        rows.append({"window": label, "impl": "model, MIDCPNIFTY 30d synthetic (12 rolls)", **ev(df, lev, s, None, ONEWAY_SYN, 12, al)})
        for lv in (1.0, 1.5, 2.0):
            rows.append({"window": label, "impl": f"buy & hold {lv}x, futures (12 rolls)", **ev(df, E.buy_and_hold(df, lv), s, None, ONEWAY_FUT, 12, lv)})
            rows.append({"window": label, "impl": f"buy & hold {lv}x, 30d synthetic (12 rolls)", **ev(df, E.buy_and_hold(df, lv), s, None, ONEWAY_SYN, 12, lv)})
    t = pd.DataFrame(rows)
    res["oos"] = t.to_dict("records")
    print("\n=== OUT OF SAMPLE ===")
    print(t[["window", "impl", "cagr", "net", "sharpe", "dd", "calmar", "chg", "cash", "lev", "roll_drag"]].round(2).to_string(index=False))
    (HERE / "india_overlay.json").write_text(json.dumps(res, indent=2, default=float))
    print("\nwrote india_overlay.json")


if __name__ == "__main__":
    main()
