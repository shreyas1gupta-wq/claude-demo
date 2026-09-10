#!/usr/bin/env python3
"""Diagnostic: the same dissipation_reentry rules with the DEFAULT engine set to FLAT 1x instead of the incumbent's
3x/2x/1x RV tier (the brief allows either as the structural default). Reuses dev_harness' own window/era/stress/census
functions so the numbers are comparable with the harness JSON. DEV data only (E.load_market(end=DEV_END)).
Usage: python dev_results/dissipation_reentry_flat1x.py --params '{"rv_exit":0.15,...}' [--tier "1,1,1"]"""
from __future__ import annotations
import argparse, importlib.util, json, sys
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import engine as E                 # noqa: E402
import dev_harness as H            # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--params", default="")
    ap.add_argument("--tier", default="1,1,1", help="LEV_TIER levels for RV<lo, RV<hi, else (default flat 1x)")
    a = ap.parse_args()
    p = HERE / "signals" / "dissipation_reentry.py"
    spec = importlib.util.spec_from_file_location("dissipation_reentry", p)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    mod.LEV_TIER = tuple(float(v) for v in a.tier.split(","))
    params = dict(mod.DEFAULT_PARAMS)
    if a.params:
        params.update(json.loads(a.params))
    df = E.load_market(end=H.DEV_END)
    assert df.index[-1] <= pd.Timestamp(H.DEV_END)
    lev = mod.signal(df, **params).reindex(df.index)
    cost, fin = 3.0, 60.0
    print(f"LEV_TIER={mod.LEV_TIER}  params={params}")
    for k, v in H.run_windows(df, lev, cost, fin).items():
        if v:
            print(f"  {k}: CAGR {v['annualized_return_pct']:.2f}% Sharpe {v['sharpe']:.3f} maxDD {v['max_drawdown_pct']:.1f}% "
                  f"worstM {v['worst_month_pct']:.1f}% cash {v['pct_days_cash']:.0f}% chg/yr {v['position_changes_per_year']:.1f}")
    for k, v in H.run_eras(df, lev, cost, fin).items():
        print(f"  era {k}: CAGR {v['cagr_pct']:.2f}% (SPY {v['spy_cagr_pct']:.2f}%) Sharpe {v['sharpe']:.3f} maxDD {v['max_dd_pct']:.1f}% "
              f"(SPY {v['spy_max_dd_pct']:.1f}%) cash {v['pct_days_cash']:.0f}% chg/yr {v['changes_per_year']:.1f}")
    for k, v in H.run_stress(df, lev, cost, fin).items():
        print(f"  stress {k}: model {v['model_total_pct']:+.1f}% (SPY {v['spy_total_pct']:+.1f}%) DD {v['model_max_dd_pct']:.1f}% "
              f"avgL {v['avg_leverage']:.2f} cash {v['pct_days_cash']:.0f}%")
    for k, v in H.spurious_reentry_census(df, lev).items():
        print(f"  census {k}: n {v['n_entries_to_2x_plus']} mean_fwd10 {v['mean_fwd10_excess_pct']} share_neg {v['share_fwd10_negative']}")


if __name__ == "__main__":
    main()
