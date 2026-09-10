#!/usr/bin/env python3
"""Isolate the REBOUND bursts of signals/dissipation_reentry.py on DEV data (E.load_market(end="2012-06-30") ONLY).

For a parameter set, list every burst (entry date, VIX, VIX / trailing max, RSI(2), length) with the burst's own P&L
at 3x net of cost/financing, then per-era counts, hit rate and summed P&L. Also runs the "no rebound" ablation
(REBOUND state disabled) for the same params so the marginal value of the re-entry is visible.

Usage:  python dev_results/dissipation_reentry_isolate.py [--params '{"vix_fall":0.3}'] [--tag x]
Writes: dev_results/dissipation_reentry_bursts[_tag].csv and prints the per-era table.
"""
from __future__ import annotations
import argparse, importlib.util, json, sys
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import engine as E          # noqa: E402
import features as F        # noqa: E402

DEV_END = "2012-06-30"
COST_BPS, FIN_BPS = 3.0, 60.0
ERAS = {"1990_1999": ("1990-01-01", "1999-12-31"), "2000_02_bear": ("2000-03-24", "2002-10-09"),
        "2002_03_recovery": ("2002-10-10", "2003-12-31"), "2004_2007H3": ("2004-01-01", "2007-10-08"),
        "2007_09_gfc": ("2007-10-09", "2009-03-09"), "2009_recovery": ("2009-03-10", "2009-12-31"),
        "2010_2012H1": ("2010-01-01", DEV_END)}


def load_sig():
    p = HERE / "signals" / "dissipation_reentry.py"
    spec = importlib.util.spec_from_file_location("dissipation_reentry", p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def bursts(df, lev, params):
    """Each maximal run of lev == 3 that was entered via the dissipation trigger (not the RV<0.10 tier)."""
    mod = load_sig()
    vix = df["vix_close"].ffill()
    vmax = vix.rolling(int(params["vix_win"]), min_periods=int(params["vix_win"])).max()
    rsi2 = F.rsi(df["spx_px"], 2)
    rv = F.realized_vol(df["spx_ret"], mod.RV_WIN)
    x = df["spx_tr_ret"] - df["rf_daily"]
    rf = df["rf_daily"]
    dissip = (vix <= (1 - params["vix_fall"]) * vmax) & (vix >= params["vix_min"]) & (rsi2 < mod.RSI_MAX)
    l = lev.fillna(0)
    rows = []
    i = 0
    idx = df.index
    n = len(idx)
    while i < n:
        if l.iloc[i] == 3.0 and (i == 0 or l.iloc[i - 1] != 3.0) and bool(dissip.iloc[i]) and not (rv.iloc[i] < mod.TIER_RV_LO):
            j = i
            while j + 1 < n and l.iloc[j + 1] == 3.0:
                j += 1
            # target decided at close i earns days i+1..j+1 (engine convention)
            days = x.iloc[i + 1:j + 2]
            rfd = rf.iloc[i + 1:j + 2]
            fin = 2.0 * FIN_BPS / 1e4 / 252
            cost = 2 * 3.0 * COST_BPS / 1e4          # in and out, 3 units of notional each way (approx: from/to cash)
            gross = float(((1 + rfd + 3.0 * days).prod() - 1))
            net = float(((1 + rfd + 3.0 * days - fin).prod() - 1) - cost)
            spx = float(((1 + df["spx_tr_ret"].iloc[i + 1:j + 2]).prod() - 1))
            rows.append({"entry": str(idx[i].date()), "exit_close": str(idx[min(j + 1, n - 1)].date()), "len": j - i + 1,
                         "vix": round(float(vix.iloc[i]), 1), "vix_over_max": round(float(vix.iloc[i] / vmax.iloc[i]), 3),
                         "rsi2": round(float(rsi2.iloc[i]), 1), "rv21": round(float(rv.iloc[i]), 3),
                         "dd60": round(float(F.drawdown_from_high(df["spx_px"], 60).iloc[i] * 100), 1),
                         "spx_pct": round(spx * 100, 2), "burst_gross_pct": round(gross * 100, 2), "burst_net_pct": round(net * 100, 2),
                         "min_path_pct": round(float(((1 + rfd + 3.0 * days).cumprod().min() - 1) * 100), 2)})
            i = j + 1
        else:
            i += 1
    return pd.DataFrame(rows)


def era_table(b: pd.DataFrame):
    out = []
    for k, (s, e) in ERAS.items():
        if len(b) == 0:
            out.append({"era": k, "n": 0}); continue
        m = b[(b["entry"] >= s) & (b["entry"] <= e)]
        if len(m) == 0:
            out.append({"era": k, "n": 0, "hit_rate": None, "sum_net_pct": 0.0, "compound_net_pct": 0.0, "worst_pct": None})
            continue
        out.append({"era": k, "n": int(len(m)), "hit_rate": round(float((m["burst_net_pct"] > 0).mean()), 2),
                    "sum_net_pct": round(float(m["burst_net_pct"].sum()), 1),
                    "compound_net_pct": round(float(((1 + m["burst_net_pct"] / 100).prod() - 1) * 100), 1),
                    "worst_pct": round(float(m["burst_net_pct"].min()), 1), "mean_len": round(float(m["len"].mean()), 1)})
    return pd.DataFrame(out)


def sharpe_1990(df, lev):
    r = E.run(df, lev, cost_bps=COST_BPS, financing_spread_bps=FIN_BPS, start="1990-01-01", end=DEV_END)
    m = r.metrics()
    return m.get("sharpe"), m.get("annualized_return_pct"), m.get("max_drawdown_pct"), m.get("position_changes_per_year")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", default="")
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    mod = load_sig()
    params = dict(mod.DEFAULT_PARAMS)
    if a.params:
        params.update(json.loads(a.params))
    df = E.load_market(end=DEV_END)
    assert df.index[-1] <= pd.Timestamp(DEV_END)
    lev = mod.signal(df, **params).reindex(df.index)
    b = bursts(df, lev, params)
    tag = f"_{a.tag}" if a.tag else ""
    b.to_csv(HERE / "dev_results" / f"dissipation_reentry_bursts{tag}.csv", index=False)
    print(f"params: {params}")
    print(f"bursts 1990-2012H1: {len(b)}")
    if len(b):
        print(b.to_string(index=False))
    print("\nper-era:")
    print(era_table(b).to_string(index=False))
    # ablation: same params, REBOUND disabled (vix_min impossibly high)
    lev_no = mod.signal(df, **{**params, "vix_min": 1e9}).reindex(df.index)
    s_with, s_no = sharpe_1990(df, lev), sharpe_1990(df, lev_no)
    print(f"\ndev_1990 with bursts:    Sharpe {s_with[0]:.3f} CAGR {s_with[1]:.2f}% maxDD {s_with[2]:.1f}% chg/yr {s_with[3]:.1f}")
    print(f"dev_1990 REBOUND off:    Sharpe {s_no[0]:.3f} CAGR {s_no[1]:.2f}% maxDD {s_no[2]:.1f}% chg/yr {s_no[3]:.1f}")
    for k in ("2000_02_bear", "2007_09_gfc", "2009_recovery", "1998_ltcm"):
        s, e = {"2000_02_bear": ("2000-03-24", "2002-10-09"), "2007_09_gfc": ("2007-10-09", "2009-03-09"),
                "2009_recovery": ("2009-03-10", "2009-12-31"), "1998_ltcm": ("1998-07-17", "1998-12-31")}[k]
        rw = E.run(df, lev, cost_bps=COST_BPS, financing_spread_bps=FIN_BPS, start=s, end=e).daily
        rn = E.run(df, lev_no, cost_bps=COST_BPS, financing_spread_bps=FIN_BPS, start=s, end=e).daily
        tw = ((1 + rw["ret"]).prod() - 1) * 100; tn = ((1 + rn["ret"]).prod() - 1) * 100
        print(f"  {k}: model {tw:+.1f}%  (REBOUND off {tn:+.1f}%)  SPY {((1 + rw['mkt_tr_ret']).prod() - 1) * 100:+.1f}%")


if __name__ == "__main__":
    main()
