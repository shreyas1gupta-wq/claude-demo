#!/usr/bin/env python3
"""India-specific development: re-calibrate the dual-engine for Indian midcap volatility.

Development window: Nifty Midcap 50, 2012-02-22 .. 2019-12-31 (the only long Indian midcap history).
Out-of-sample:      Midcap 50 2020-01-01 onward, and Nifty Midcap Select (the actual F&O underlying)
                    from 2021-09-16 onward.
Two families are tested: absolute volatility tiers (as in the US model) and volatility targeting,
which auto-calibrates to whatever volatility the index actually runs at.

Run:  python3 tune_india.py
"""
from __future__ import annotations
import json, sys, warnings
from pathlib import Path
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "model"))
import engine as E      # noqa: E402
import features as F    # noqa: E402
import costs            # noqa: E402

IN = pd.read_csv(HERE / "data" / "india_daily.csv", parse_dates=["date"]).set_index("date")
SAFETY = 1.5
ONEWAY = {k: v / 2 * SAFETY for k, v in {
    "mcs_fut": costs.futures_round_turn(1_500_000, 4.0)["bp_of_notional"],
    "syn90": costs.cost_per_unit_exposure(24000, 1_500_000, [("C", 1.0, 1), ("P", 1.0, -1)], 0.13, 90, 35)["bp_of_notional"],
}.items()}
DEV0, DEV1, OOS0 = "2012-02-22", "2019-12-31", "2020-01-01"


def frame(k):
    d = pd.DataFrame(index=IN.index)
    d["spx_px"], d["spx_ret"] = IN[k], IN[f"{k}_ret"]
    d["rf_daily"] = IN["cash_ret"]
    d["spx_tr_ret"] = IN[f"{k}_x"] + IN["cash_ret"]
    d["vix_close"] = IN["vix"]
    return d.dropna(subset=["spx_px"])


def hold(lev, min_days):
    out = lev.to_numpy(dtype=float).copy()
    cur, held = out[0], 0
    for i in range(1, len(out)):
        if out[i] != cur and held < min_days:
            out[i] = cur
        elif out[i] != cur:
            cur, held = out[i], 0
        held += 1
    return pd.Series(out, index=lev.index)


def weekly(lev, df):
    wk = pd.Series(df.index.isocalendar().week.values, index=df.index)
    return lev.where(wk.ne(wk.shift(-1))).ffill().fillna(0.0)


def sig_tier(df, ma_fast=100, ma_slow=200, rv_lo=0.14, rv_hi=0.20, min_days=20, max_lev=3.0):
    px, ret = df["spx_px"], df["spx_ret"]
    st = F.hysteresis(px > F.sma(px, ma_fast), px < F.sma(px, ma_slow), initial=False)
    rv = F.realized_vol(ret, 21)
    shock = ret < -3.0 * rv / np.sqrt(252)
    st = st & ~(shock.rolling(5, min_periods=1).max().fillna(0) > 0)
    lev = pd.Series(0.0, index=df.index)
    lev[st] = 1.0
    lev[st & (rv < rv_hi)] = min(2.0, max_lev)
    lev[st & (rv < rv_lo)] = max_lev
    return hold(weekly(lev, df), min_days).clip(0, max_lev)


def sig_voltarget(df, ma_fast=100, ma_slow=200, target_vol=0.20, max_lev=3.0, min_days=20, hl=20):
    """Leverage = target_vol / forecast_vol, rounded to whole steps, gated by the trend and a shock rule.
    Self-calibrating: the same target_vol means the same risk in any market."""
    px, ret = df["spx_px"], df["spx_ret"]
    st = F.hysteresis(px > F.sma(px, ma_fast), px < F.sma(px, ma_slow), initial=False)
    rv21 = F.realized_vol(ret, 21)
    shock = ret < -3.0 * rv21 / np.sqrt(252)
    st = st & ~(shock.rolling(5, min_periods=1).max().fillna(0) > 0)
    raw = (target_vol / F.ewma_vol(ret, hl)).clip(0, max_lev)
    lev = np.floor(raw + 0.5).clip(0, max_lev)
    lev[~st] = 0.0
    return hold(weekly(pd.Series(lev, index=df.index), df), min_days).clip(0, max_lev)


def ev(df, lev, s, e, cost):
    m = E.run(df, lev, asset="spx_tr", cost_bps=cost, start=s, end=e).metrics()
    return dict(cagr=m["annualized_return_pct"], sharpe=m["sharpe"], dd=m["max_drawdown_pct"],
                calmar=m["calmar"], chg=m["position_changes_per_year"], cash=m["pct_days_cash"],
                lev=m["avg_leverage"], vol=m["annualized_std_dev"])


def main():
    mc50, mcs = frame("mc50"), frame("mcs")
    res = {"oneway_bp": ONEWAY, "dev_window": [DEV0, DEV1], "oos_start": OOS0}

    # ---------------- development grid on Midcap 50, 2012-2019 only ----------------
    grid = []
    for tv in [0.14, 0.18, 0.22, 0.26, 0.30]:
        for mx in [2.0, 3.0]:
            for md in [10, 20, 40]:
                l = sig_voltarget(mc50, target_vol=tv, max_lev=mx, min_days=md)
                d = ev(mc50, l, DEV0, DEV1, ONEWAY["mcs_fut"])
                grid.append({"family": "voltarget", "target_vol": tv, "max_lev": mx, "min_days": md, **d})
    for lo, hi in [(0.14, 0.20), (0.16, 0.24), (0.18, 0.26), (0.20, 0.30)]:
        for mx in [2.0, 3.0]:
            for md in [10, 20, 40]:
                l = sig_tier(mc50, rv_lo=lo, rv_hi=hi, min_days=md, max_lev=mx)
                d = ev(mc50, l, DEV0, DEV1, ONEWAY["mcs_fut"])
                grid.append({"family": "tier", "rv_lo": lo, "rv_hi": hi, "max_lev": mx, "min_days": md, **d})
    g = pd.DataFrame(grid)
    bh_dev = ev(mc50, E.buy_and_hold(mc50, 1.0), DEV0, DEV1, ONEWAY["mcs_fut"])
    res["dev_buy_and_hold_1x"] = bh_dev
    print("=== DEVELOPMENT: Midcap 50, 2012-02 to 2019-12 (buy & hold 1x: "
          f"CAGR {bh_dev['cagr']:.2f}%, Sharpe {bh_dev['sharpe']:.2f}, maxDD {bh_dev['dd']:.1f}%) ===")
    print(g.sort_values("sharpe", ascending=False).head(10).round(3).to_string(index=False))
    res["dev_grid_top"] = g.sort_values("sharpe", ascending=False).head(12).to_dict("records")

    best = g.sort_values("sharpe", ascending=False).iloc[0]
    res["chosen"] = {k: (None if pd.isna(best.get(k)) else best.get(k)) for k in
                     ["family", "target_vol", "max_lev", "min_days", "rv_lo", "rv_hi"]}
    print(f"\nCHOSEN ON DEVELOPMENT: {res['chosen']}")

    def build(df):
        if best["family"] == "voltarget":
            return sig_voltarget(df, target_vol=best["target_vol"], max_lev=best["max_lev"], min_days=int(best["min_days"]))
        return sig_tier(df, rv_lo=best["rv_lo"], rv_hi=best["rv_hi"], max_lev=best["max_lev"], min_days=int(best["min_days"]))

    # ---------------- out-of-sample ----------------
    rows = []
    for label, df, s, e in [("Midcap 50", mc50, OOS0, None), ("Midcap Select", mcs, "2021-09-16", None)]:
        lev = build(df)
        avg_lev = ev(df, lev, s, e, 0.0)["lev"]
        for impl, cost, rolls, key in [("MIDCPNIFTY futures (monthly roll)", ONEWAY["mcs_fut"], 12, "mcs_fut"),
                                       ("Nifty 90d synthetic (quarterly roll)", ONEWAY["syn90"], 4, "syn90")]:
            d = ev(df, lev, s, e, cost)
            drag = (ONEWAY[key] * 2 / SAFETY * SAFETY) * rolls * avg_lev / 100.0
            rows.append({"window": label, "impl": impl, **d, "roll_drag_pct": drag, "net_cagr": d["cagr"] - drag})
        for lv in (1.0, 2.0):
            d = ev(df, E.buy_and_hold(df, lv), s, e, ONEWAY["mcs_fut"])
            drag = (ONEWAY["mcs_fut"] * 2) * 12 * lv / 100.0
            rows.append({"window": label, "impl": f"buy & hold {lv:.0f}x futures", **d, "roll_drag_pct": drag, "net_cagr": d["cagr"] - drag})
    t = pd.DataFrame(rows)
    res["oos"] = t.to_dict("records")
    print("\n=== OUT OF SAMPLE (parameters frozen on 2012-2019 Midcap 50) ===")
    print(t[["window", "impl", "cagr", "net_cagr", "sharpe", "dd", "calmar", "chg", "cash", "lev", "vol"]].round(2).to_string(index=False))

    (HERE / "india_tuning.json").write_text(json.dumps(res, indent=2, default=float))
    print("\nwrote india_tuning.json")


if __name__ == "__main__":
    main()
