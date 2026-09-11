#!/usr/bin/env python3
"""The India model: cheap synthetic exposure, volatility-sized, with a systematic covered-call overlay.

Three components, in order of how much of the edge each carries:

  1. IMPLEMENTATION. Hold the index through an at-the-money option synthetic (long call + short put at
     the same strike) rather than a future. Identical delta-one payoff, but securities transaction tax
     and exchange charges apply to the premium (~4% of notional) instead of the notional. Certain saving.
  2. OVERLAY. Sell a monthly out-of-the-money call against the position. India's implied volatility has
     exceeded subsequent realised volatility in every year since 2014, and the charges on that premium
     are small, so the premium is harvestable. This is where the model's excess return comes from.
  3. SIZING. Scale the position to a constant volatility target rather than a fixed multiplier, and step
     aside only for genuine shocks. This controls drawdown; it does not add return.

There is deliberately NO market-timing engine. Seven signal families were tested on the Indian
development window and every one of them reduced the Sharpe ratio versus simply staying invested.

Development window: 2014-05-15 .. 2019-12-31 on Nifty Midcap 50 (India VIX starts 2014-05).
Out-of-sample:      2020-01-01 onward, and Nifty Midcap Select from 2021-09-16.

Run:  python3 india_model.py
"""
from __future__ import annotations
import json, sys, warnings
from pathlib import Path
import numpy as np, pandas as pd

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "model"))
import features as F, costs  # noqa: E402

IN = pd.read_csv(HERE / "data" / "india_daily.csv", parse_dates=["date"]).set_index("date")
DEV0, DEV1, OOS0 = "2014-05-15", "2019-12-31", "2020-01-01"
LOT_NOTIONAL = 1_500_000.0
VOL_RATIO = 1.35          # midcap implied volatility relative to India VIX, measured in vrp_overlay.py

DEFAULTS = dict(target_vol=0.18, max_lev=1.5, ewma_hl=40, min_days=20,
                shock_z=3.5, shock_days=10, call_otm=0.08, core_tenor_days=30)


# ------------------------------------------------------------------ core sizing
def core_leverage(df, target_vol, max_lev, ewma_hl, min_days, shock_z, shock_days):
    """Volatility-targeted exposure, quantised to quarter steps, flat after a genuine shock."""
    ret = df["ret"]
    raw = (target_vol / F.ewma_vol(ret, ewma_hl)).clip(0.25, max_lev)
    lev = (raw * 4).round() / 4
    rv = F.realized_vol(ret, 21)
    shock = ret < -shock_z * rv / np.sqrt(252)
    lev[shock.rolling(int(shock_days), min_periods=1).max().fillna(0) > 0] = 0.0
    out = lev.to_numpy(dtype=float).copy()
    cur, held = out[0], 0
    for i in range(1, len(out)):
        if out[i] != cur and held < min_days:
            out[i] = cur
        elif out[i] != cur:
            cur, held = out[i], 0
        held += 1
    return pd.Series(out, index=df.index).clip(0, max_lev)


def monthly_expiries(idx):
    """Last Tuesday of each month (the NSE monthly convention)."""
    t = pd.DataFrame(index=idx)
    t["ym"] = t.index.to_period("M")
    tu = t[t.index.dayofweek == 1]
    return list(pd.to_datetime(tu.groupby("ym").apply(lambda g: g.index.max()).values))


# ------------------------------------------------------------------ full simulation
def simulate(index_key, params=None, start=None, end=None, use_synthetic=True,
             overlay=True, core_lev_override=None):
    p = dict(DEFAULTS); p.update(params or {})
    d = pd.DataFrame({
        "px": IN[index_key], "ret": IN[f"{index_key}_ret"], "x": IN[f"{index_key}_x"],
        "cash": IN["cash_ret"], "vix": IN["vix"].ffill(),
    }).dropna(subset=["px", "x", "vix"])
    if start: d = d.loc[start:]
    if end: d = d.loc[:end]
    if len(d) < 300:
        return None

    lev = (pd.Series(core_lev_override, index=d.index) if core_lev_override is not None
           else core_leverage(d, p["target_vol"], p["max_lev"], p["ewma_hl"], p["min_days"], p["shock_z"], p["shock_days"]))

    # --- core: leverage applied to the excess return, plus cash on the whole capital
    lev_prev = lev.shift(1).fillna(0.0)
    core = d["cash"] + lev_prev * d["x"]

    # --- core implementation cost: change in exposure, plus the periodic roll
    rt_core = (costs.cost_per_unit_exposure(float(d.px.iloc[-1]), LOT_NOTIONAL, [("C", 1.0, 1), ("P", 1.0, -1)],
                                            0.18, p["core_tenor_days"], 60)["bp_of_notional"] if use_synthetic
               else costs.futures_round_turn(LOT_NOTIONAL, 4.0)["bp_of_notional"])
    oneway = rt_core / 2 * 1.5
    turn_cost = (lev - lev_prev).abs() * oneway / 1e4
    exps = [e for e in monthly_expiries(d.index) if e in d.index]
    roll_cost = pd.Series(0.0, index=d.index)
    roll_days = exps if p["core_tenor_days"] <= 31 else exps[::3]
    roll_cost.loc[roll_days] = lev_prev.loc[roll_days] * rt_core * 1.5 / 1e4

    # --- overlay: sell a call `call_otm` above spot at each expiry, settle at the next
    ov = pd.Series(0.0, index=d.index)
    ov_rows = []
    if overlay and p["call_otm"]:
        for i in range(len(exps) - 1):
            t0, t1 = exps[i], exps[i + 1]
            s0, s1 = float(d.px.loc[t0]), float(d.px.loc[t1])
            size = float(lev.loc[t0])                       # sell calls against the actual exposure held
            if size <= 0:
                continue
            iv = float(d.vix.loc[t0]) / 100 * VOL_RATIO
            yrs = max(1, (t1 - t0).days) / 365.0
            k = s0 * (1 + p["call_otm"])
            prem, _ = costs.bs(s0, k, iv, yrs, call=True)
            payoff = -max(0.0, s1 - k)
            mult = LOT_NOTIONAL / s0
            c = costs.option_round_turn(prem * mult, LOT_NOTIONAL, n_legs=1, half_spread_bp_of_premium=70)
            pnl_pts = prem + payoff - c["total"] / mult
            ov.loc[t1] = size * pnl_pts / s0                # booked at expiry, scaled by the exposure held
            ov_rows.append({"open": str(t0.date()), "expiry": str(t1.date()), "size": size,
                            "premium_pct": prem / s0 * 100, "payoff_pct": payoff / s0 * 100,
                            "pnl_pct": pnl_pts / s0 * 100, "index_move_pct": (s1 / s0 - 1) * 100})

    total = core - turn_cost - roll_cost + ov
    eq = (1 + total).cumprod()
    return {"daily": pd.DataFrame({"lev": lev, "core": core, "turn_cost": turn_cost, "roll_cost": roll_cost,
                                   "overlay": ov, "total": total, "equity": eq, "px": d.px, "cash": d["cash"]}),
            "overlay_cycles": ov_rows, "round_turn_bp": rt_core, "params": p}


def metrics(sim, label=""):
    d = sim["daily"]
    n = len(d)
    yrs = n / 252
    eq = d.equity
    cagr = (eq.iloc[-1] ** (1 / yrs) - 1) * 100
    vol = d.total.std() * np.sqrt(252)
    ex = d.total - d["cash"]
    sharpe = ex.mean() * 252 / (ex.std() * np.sqrt(252)) if ex.std() > 0 else np.nan
    m = eq / eq.cummax() - 1
    dn = ex[ex < 0]
    return {"label": label, "start": str(d.index.min().date()), "end": str(d.index.max().date()), "years": round(yrs, 2),
            "cagr_pct": cagr, "vol_pct": vol * 100, "sharpe": sharpe,
            "sortino": ex.mean() * 252 / (dn.std() * np.sqrt(252)) if len(dn) else np.nan,
            "max_dd_pct": m.min() * 100, "calmar": cagr / abs(m.min() * 100) if m.min() < 0 else np.nan,
            "avg_lev": d.lev.mean(), "pct_days_flat": (d.lev == 0).mean() * 100,
            "changes_per_year": int((d.lev.diff() != 0).sum()) / yrs,
            "core_cost_pct": (d.turn_cost.sum() + d.roll_cost.sum()) / yrs * 100,
            "overlay_pct": d.overlay.sum() / yrs * 100,
            "growth_of_100k": float(eq.iloc[-1] * 100000)}


def main():
    global VOL_RATIO
    out = {"defaults": DEFAULTS, "vol_ratio": VOL_RATIO}

    # ---------------- development: choose the sizing rule and the overlay strike ----------------
    # The grid deliberately includes CONSTANT leverage, so the selection is not rigged against the
    # possibility that no sizing rule is the right sizing rule.
    grid = []
    for otm in [0.0, 0.04, 0.05, 0.06, 0.08, 0.12]:
        for cl in [0.75, 1.0, 1.25]:
            s = simulate("mc50", dict(call_otm=otm), DEV0, DEV1, core_lev_override=cl)
            grid.append({"sizing": f"constant {cl}x", "target_vol": None, "max_lev": cl, "call_otm": otm, **metrics(s)})
        for tv in [0.14, 0.18, 0.22]:
            for mx in [1.25, 1.5]:
                s = simulate("mc50", dict(target_vol=tv, max_lev=mx, call_otm=otm), DEV0, DEV1)
                grid.append({"sizing": f"vol target {tv}", "target_vol": tv, "max_lev": mx, "call_otm": otm, **metrics(s)})
    g = pd.DataFrame(grid)
    g["score"] = g.sharpe + 0.5 * g.calmar
    print(f"=== DEVELOPMENT (Nifty Midcap 50, {DEV0}..{DEV1}) — top 10 by Sharpe + 0.5 x Calmar ===")
    cols = ["sizing", "call_otm", "cagr_pct", "vol_pct", "sharpe", "max_dd_pct", "calmar",
            "avg_lev", "changes_per_year", "core_cost_pct", "overlay_pct"]
    print(g.sort_values("score", ascending=False).head(10)[cols].round(3).to_string(index=False))
    best = g.sort_values("score", ascending=False).iloc[0]
    is_const = best.target_vol is None or pd.isna(best.target_vol)
    chosen = dict(call_otm=float(best.call_otm))
    if not is_const:
        chosen.update(target_vol=float(best.target_vol), max_lev=float(best.max_lev))
    chosen["_constant_leverage"] = float(best.max_lev) if is_const else None
    out["chosen"] = chosen
    out["dev_grid"] = g[cols + ["score"]].to_dict("records")
    print(f"\nCHOSEN ON DEVELOPMENT: {chosen}")

    # ---------------- out of sample ----------------
    rows = []
    for label, key, s0 in [("Midcap 50, 2020+", "mc50", OOS0), ("Midcap Select, 2021-09+", "mcs", "2021-09-16")]:
        n = len(IN[key].dropna().loc[s0:])
        base_lev = pd.Series(1.0, index=IN.index)
        rows.append({"window": label, "variant": "buy & hold 1x, futures, no overlay",
                     **metrics(simulate(key, dict(call_otm=0.0), s0, use_synthetic=False, overlay=False,
                                        core_lev_override=1.0))})
        rows.append({"window": label, "variant": "buy & hold 1x, synthetic, no overlay",
                     **metrics(simulate(key, dict(call_otm=0.0), s0, use_synthetic=True, overlay=False,
                                        core_lev_override=1.0))})
        rows.append({"window": label, "variant": f"buy & hold 1x, synthetic + {chosen['call_otm']:.0%} call overlay",
                     **metrics(simulate(key, dict(call_otm=chosen["call_otm"]), s0, use_synthetic=True,
                                        overlay=True, core_lev_override=1.0))})
        cl = chosen.get("_constant_leverage")
        cp = {k: v for k, v in chosen.items() if not k.startswith("_")}
        rows.append({"window": label, "variant": "MODEL as chosen on development",
                     **metrics(simulate(key, cp, s0, use_synthetic=True, overlay=True, core_lev_override=cl))})
        rows.append({"window": label, "variant": "MODEL but on futures (cost check)",
                     **metrics(simulate(key, cp, s0, use_synthetic=False, overlay=True, core_lev_override=cl))})
        rows.append({"window": label, "variant": "MODEL without overlay (overlay check)",
                     **metrics(simulate(key, {**cp, "call_otm": 0.0}, s0, use_synthetic=True, overlay=False, core_lev_override=cl))})
        rows.append({"window": label, "variant": "vol-sized instead of constant (sizing check)",
                     **metrics(simulate(key, {"target_vol": 0.18, "max_lev": 1.25, "call_otm": chosen["call_otm"]}, s0,
                                        use_synthetic=True, overlay=True))})
    t = pd.DataFrame(rows)
    out["oos"] = t.to_dict("records")
    print("\n=== OUT OF SAMPLE ===")
    show = ["window", "variant", "cagr_pct", "vol_pct", "sharpe", "sortino", "max_dd_pct", "calmar",
            "avg_lev", "changes_per_year", "core_cost_pct", "overlay_pct"]
    print(t[show].round(2).to_string(index=False))

    # full-history run of the chosen model for the record
    cp = {k: v for k, v in chosen.items() if not k.startswith("_")}
    cl = chosen.get("_constant_leverage")
    # the overlay's premium depends on an estimated midcap implied volatility: test that assumption
    iv_rows = []
    for r in [1.0, 1.15, 1.35, 1.5]:
        VOL_RATIO = r
        for key, s0, lab in [("mcs", "2021-09-16", "Midcap Select"), ("mc50", OOS0, "Midcap 50 2020+")]:
            m = metrics(simulate(key, cp, s0, use_synthetic=True, overlay=True, core_lev_override=cl))
            iv_rows.append({"vol_ratio": r, "window": lab, "cagr_pct": m["cagr_pct"], "sharpe": m["sharpe"],
                            "max_dd_pct": m["max_dd_pct"], "overlay_pct": m["overlay_pct"]})
    VOL_RATIO = 1.35
    out["iv_sensitivity"] = iv_rows
    print("\n=== SENSITIVITY: the assumed midcap implied volatility (India VIX x ratio) ===")
    print(pd.DataFrame(iv_rows).round(2).to_string(index=False))
    full = simulate("mc50", cp, "2014-05-15", core_lev_override=cl)
    out["full_history_mc50"] = metrics(full, "Midcap 50 2014-2026")
    out["overlay_cycles_mcs"] = simulate("mcs", cp, "2021-09-16", core_lev_override=cl)["overlay_cycles"]
    (HERE / "india_model_results.json").write_text(json.dumps(out, indent=2, default=float))
    print("\n=== CHOSEN MODEL, FULL HISTORY (Midcap 50, 2014-2026, includes the development window) ===")
    print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in out["full_history_mc50"].items()})
    print("\nwrote india_model_results.json")


if __name__ == "__main__":
    main()
