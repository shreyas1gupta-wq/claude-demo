#!/usr/bin/env python3
"""Run the dual-engine models on Indian indices with Indian costs.

Reuses the US study's engine, features and signal modules unchanged (../model), so the parameters
frozen on pre-July-2012 US data are applied to India untouched: a genuine out-of-sample test in a
different market. Also re-tunes lightly on an Indian development window for comparison.

Run:  python3 run_india.py
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
MODEL = HERE.parent / "model"
sys.path.insert(0, str(MODEL))
import engine as E          # noqa: E402
import features as F        # noqa: E402
sys.path.insert(0, str(MODEL / "signals"))
import costs                # noqa: E402

IN = pd.read_csv(HERE / "data" / "india_daily.csv", parse_dates=["date"]).set_index("date")

# One-way costs in bp of notional = half of a round turn, then x1.5 margin of safety.
RT = {
    "mcs_fut": costs.futures_round_turn(1_500_000, 4.0)["bp_of_notional"],
    "nifty_fut": costs.futures_round_turn(1_500_000, 1.5)["bp_of_notional"],
    "syn30": costs.cost_per_unit_exposure(24000, 1_500_000, [("C", 1.0, 1), ("P", 1.0, -1)], 0.12, 30, 25)["bp_of_notional"],
    "syn90": costs.cost_per_unit_exposure(24000, 1_500_000, [("C", 1.0, 1), ("P", 1.0, -1)], 0.13, 90, 35)["bp_of_notional"],
}
SAFETY = 1.5
ONEWAY = {k: v / 2 * SAFETY for k, v in RT.items()}


def frame(index_key: str) -> pd.DataFrame:
    """Map an Indian index onto the column names the US engine expects."""
    d = pd.DataFrame(index=IN.index)
    d["spx_px"] = IN[index_key]
    d["spx_ret"] = IN[f"{index_key}_ret"]
    d["rf_daily"] = IN["cash_ret"]
    d["spx_tr_ret"] = IN[f"{index_key}_x"] + IN["cash_ret"]   # futures-equivalent gross return
    d["vix_close"] = IN["vix"]
    d["spx_quality"] = "nse_index"
    return d.dropna(subset=["spx_px"])


def stats(res, roll_drag_pct=0.0):
    m = res.metrics()
    out = {k: m.get(k) for k in ["annualized_return_pct", "annualized_std_dev", "sharpe", "sortino", "calmar",
                                 "max_drawdown_pct", "pct_positive_months", "pct_days_cash", "avg_leverage",
                                 "n_position_changes", "position_changes_per_year", "total_cost_drag_pct_annual",
                                 "up_capture_pct", "down_capture_pct", "beta_to_spy", "growth_of_1000", "n_months"]}
    out["roll_drag_pct_annual"] = roll_drag_pct
    out["annualized_return_after_roll_pct"] = (out["annualized_return_pct"] or 0) - roll_drag_pct
    return out


def bh(df, lev, cost_bps, start, end, roll_drag=0.0):
    return stats(E.run(df, E.buy_and_hold(df, lev), asset="spx_tr", cost_bps=cost_bps, start=start, end=end), roll_drag)


def sig_final(df, ma_fast=100, ma_slow=200, rv_lo=0.10, rv_hi=0.15, min_days=20, shock_days=5):
    import final_model_fewtrades as M
    return M.signal(df, ma_fast=ma_fast, ma_slow=ma_slow, rv_lo=rv_lo, rv_hi=rv_hi, min_days=min_days, shock_days=shock_days)


def roll_drag(kind, avg_lev, rolls_per_year):
    """Annual cost of rolling the position even when the signal never changes, in % of capital."""
    return RT[kind] * SAFETY * rolls_per_year * avg_lev / 100.0


def main():
    out = {"cost_round_turn_bp": RT, "one_way_bp_with_1p5x_safety": ONEWAY, "safety_multiple": SAFETY}
    rows = []

    # --------------------------------------------------------------- 1. passive references
    for idx, label, span in [("mcs", "Midcap Select", ("2021-09-16", None)), ("mc50", "Midcap 50", ("2012-02-22", None)),
                             ("nifty", "Nifty 50", ("2012-02-22", None))]:
        df = frame(idx)
        s, e = span
        for lev in (1.0, 2.0):
            r = bh(df, lev, ONEWAY["mcs_fut"] if idx != "nifty" else ONEWAY["nifty_fut"], s, e,
                   roll_drag("mcs_fut" if idx != "nifty" else "nifty_fut", lev, 12))
            rows.append({"group": "passive", "index": label, "impl": f"futures {lev:.0f}x buy & hold", **r})

    # --------------------------------------------------------------- 2. the model, US-frozen parameters
    for idx, label, span in [("mcs", "Midcap Select", ("2021-09-16", None)), ("mc50", "Midcap 50", ("2012-02-22", None)),
                             ("mc50", "Midcap 50 (2021+ only)", ("2021-09-16", None)), ("nifty", "Nifty 50", ("2012-02-22", None))]:
        df = frame(idx)
        lev = sig_final(df)
        s, e = span
        base = E.run(df, lev, asset="spx_tr", cost_bps=ONEWAY["mcs_fut" if idx != "nifty" else "nifty_fut"], start=s, end=e)
        avg_lev = base.metrics()["avg_leverage"]
        rows.append({"group": "model", "index": label, "impl": "MIDCPNIFTY futures, monthly roll",
                     **stats(base, roll_drag("mcs_fut" if idx != "nifty" else "nifty_fut", avg_lev, 12))})
        syn30 = E.run(df, lev, asset="spx_tr", cost_bps=ONEWAY["syn30"], start=s, end=e)
        rows.append({"group": "model", "index": label, "impl": "Nifty 30d synthetic, monthly roll",
                     **stats(syn30, roll_drag("syn30", avg_lev, 12))})
        syn90 = E.run(df, lev, asset="spx_tr", cost_bps=ONEWAY["syn90"], start=s, end=e)
        rows.append({"group": "model", "index": label, "impl": "Nifty 90d synthetic, quarterly roll",
                     **stats(syn90, roll_drag("syn90", avg_lev, 4))})
        zero = E.run(df, lev, asset="spx_tr", cost_bps=0.0, start=s, end=e)
        rows.append({"group": "model", "index": label, "impl": "zero cost (upper bound)", **stats(zero, 0.0)})

    t = pd.DataFrame(rows)
    out["results"] = t.to_dict("records")

    # --------------------------------------------------------------- 3. midcap vs nifty relationship
    ov = IN.dropna(subset=["mcs_ret", "nifty_ret"])
    beta = np.polyfit(ov["nifty_ret"], ov["mcs_ret"], 1)[0]
    dn = ov[ov["nifty_ret"] < 0]
    out["hedge"] = {
        "n_days": int(len(ov)), "corr_mcs_nifty": float(ov["mcs_ret"].corr(ov["nifty_ret"])),
        "beta_mcs_on_nifty": float(beta), "r2": float(ov["mcs_ret"].corr(ov["nifty_ret"]) ** 2),
        "corr_in_nifty_down_days": float(dn["mcs_ret"].corr(dn["nifty_ret"])),
        "beta_in_nifty_down_days": float(np.polyfit(dn["nifty_ret"], dn["mcs_ret"], 1)[0]),
        "residual_vol_ann_pct": float((ov["mcs_ret"] - beta * ov["nifty_ret"]).std() * np.sqrt(252) * 100),
        "mcs_vol_ann_pct": float(ov["mcs_ret"].std() * np.sqrt(252) * 100),
    }
    out["hedge"]["pct_of_midcap_vol_hedgeable"] = 100 * (1 - out["hedge"]["residual_vol_ann_pct"] / out["hedge"]["mcs_vol_ann_pct"])

    # --------------------------------------------------------------- 4. turnover sensitivity
    df = frame("mcs")
    turn = []
    for md, wk in [(5, False), (10, False), (20, True), (40, True), (60, True)]:
        lv = sig_final(df, min_days=md)
        import final_model as FM
        lv = FM.core(df, 100, 200, 0.10, 0.15, md, 5, weekly=wk)
        r = E.run(df, lv, asset="spx_tr", cost_bps=ONEWAY["mcs_fut"], start="2021-09-16")
        mm = r.metrics()
        turn.append({"min_days": md, "weekly": wk, "changes_per_year": mm["position_changes_per_year"],
                     "cagr_pct": mm["annualized_return_pct"], "sharpe": mm["sharpe"], "max_dd_pct": mm["max_drawdown_pct"],
                     "cost_drag_pct": mm["total_cost_drag_pct_annual"], "pct_days_cash": mm["pct_days_cash"]})
    out["turnover_sensitivity_mcs"] = turn

    (HERE / "india_results.json").write_text(json.dumps(out, indent=2, default=float))
    show = ["group", "index", "impl", "annualized_return_pct", "annualized_return_after_roll_pct", "sharpe",
            "max_drawdown_pct", "pct_days_cash", "position_changes_per_year", "total_cost_drag_pct_annual", "roll_drag_pct_annual"]
    print("\n=== ROUND-TURN COSTS (bp of notional, incl. 1.5x safety on the one-way used by the engine) ===")
    for k, v in RT.items():
        print(f"  {k:10s} round turn {v:6.2f} bp -> one-way used {ONEWAY[k]:5.2f} bp")
    print("\n=== RESULTS ===")
    print(t[show].round(2).to_string(index=False))
    print("\n=== MIDCAP vs NIFTY (hedge feasibility) ===")
    print(json.dumps({k: round(v, 3) if isinstance(v, float) else v for k, v in out["hedge"].items()}, indent=1))
    print("\n=== TURNOVER SENSITIVITY (Midcap Select, futures) ===")
    print(pd.DataFrame(turn).round(2).to_string(index=False))


if __name__ == "__main__":
    main()
