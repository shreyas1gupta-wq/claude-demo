#!/usr/bin/env python3
"""Standardised evaluation of a dual-engine signal module.

Usage:
  python3 evaluate.py signals/<name>.py [--asset spx_tr|es|nq] [--cost-bps 2] [--fin-bps 0] [--dev-start 1990-01-01]
                      [--oos-start 2012-07-01] [--oos-end 2026-02-11] [--tag label] [--no-sensitivity]

The signal module must define:
  NAME (str), FAMILY (str), HYPOTHESIS (str), DEFAULT_PARAMS (dict), signal(df, **params) -> pd.Series of target leverage.
Outputs results/<module-stem>[_<tag>].json and results/<module-stem>[_<tag>]_daily.csv (date, lev, ret, x, rf).
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402

RESULTS = HERE / "results"


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for attr in ["NAME", "FAMILY", "HYPOTHESIS", "DEFAULT_PARAMS", "signal"]:
        if not hasattr(mod, attr):
            raise SystemExit(f"{path} lacks required attribute {attr}")
    return mod


def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if (np.isnan(o) or np.isinf(o)) else float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (pd.Timestamp,)):
        return o.strftime("%Y-%m-%d")
    return o


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("module")
    ap.add_argument("--asset", default="spx_tr")
    ap.add_argument("--cost-bps", type=float, default=2.0)
    ap.add_argument("--fin-bps", type=float, default=0.0)
    ap.add_argument("--dev-start", default="1990-01-01")
    ap.add_argument("--oos-start", default="2012-07-01")
    ap.add_argument("--oos-end", default="2026-02-11")
    ap.add_argument("--full-start", default="1950-01-03")
    ap.add_argument("--tag", default="")
    ap.add_argument("--no-sensitivity", action="store_true")
    a = ap.parse_args()

    t0 = time.time()
    path = Path(a.module).resolve()
    mod = load_module(path)
    params = dict(mod.DEFAULT_PARAMS)
    df = E.load_market()
    lev_full = mod.signal(df, **params)
    if not isinstance(lev_full, pd.Series):
        raise SystemExit("signal() must return a pd.Series")
    lev_full = lev_full.reindex(df.index)

    def run(start, end):
        return E.run(df, lev_full, asset=a.asset, cost_bps=a.cost_bps, financing_spread_bps=a.fin_bps, start=start, end=end, name=mod.NAME, params=params)

    dev_end = str((pd.Timestamp(a.oos_start) - pd.Timedelta(days=1)).date())
    res = {
        "name": mod.NAME, "family": mod.FAMILY, "hypothesis": mod.HYPOTHESIS, "module": str(path.relative_to(HERE)),
        "params": params, "asset": a.asset, "cost_bps": a.cost_bps, "financing_spread_bps": a.fin_bps,
        "windows": {},
    }
    r_dev = run(a.dev_start, dev_end)
    r_oos = run(a.oos_start, a.oos_end)
    r_full = run(a.full_start, a.oos_end)
    for k, r in [("dev", r_dev), ("oos", r_oos), ("full", r_full)]:
        if len(r.daily):
            res["windows"][k] = r.metrics()
    res["demeter_comparison_oos"] = r_oos.compare_to_demeter(start=a.oos_start, end=a.oos_end)
    res["sub_periods"] = E.sub_period_table(r_full)
    res["lookahead_check"] = E.lookahead_check(mod.signal, df.loc["1995-01-01":], params)
    res["yearly_oos"] = res["demeter_comparison_oos"]["yearly"]
    # leverage distribution (OOS)
    lev = r_oos.daily["lev"]
    res["leverage_distribution_oos"] = {str(k): float(v) for k, v in (lev.round(2).value_counts(normalize=True).sort_index() * 100).items()}
    # cost / financing sensitivity (OOS)
    res["cost_sensitivity_oos"] = []
    for c in [0.0, 1.0, 2.0, 5.0, 10.0]:
        for fb in [0.0, 50.0]:
            m = E.run(df, lev_full, asset=a.asset, cost_bps=c, financing_spread_bps=fb, start=a.oos_start, end=a.oos_end).metrics()
            res["cost_sensitivity_oos"].append({"cost_bps": c, "fin_bps": fb, "cagr_pct": m["annualized_return_pct"], "sharpe": m.get("sharpe"), "max_dd_pct": m["max_drawdown_pct"]})
    if not a.no_sensitivity:
        try:
            res["param_sensitivity_oos"] = E.param_sensitivity(mod.signal, df, params, asset=a.asset, cost_bps=a.cost_bps, start=a.oos_start, end=a.oos_end)
            res["param_sensitivity_dev"] = E.param_sensitivity(mod.signal, df, params, asset=a.asset, cost_bps=a.cost_bps, start=a.dev_start, end=dev_end)
        except Exception as ex:  # keep going; report
            res["param_sensitivity_error"] = repr(ex)
    res["runtime_sec"] = time.time() - t0
    RESULTS.mkdir(exist_ok=True)
    stem = path.stem + (f"_{a.tag}" if a.tag else "")
    (RESULTS / f"{stem}.json").write_text(json.dumps(clean(res), indent=1))
    r_full.daily[["lev", "ret", "x", "rf"]].to_csv(RESULTS / f"{stem}_daily.csv", float_format="%.8g")
    o, d = res["windows"].get("oos", {}), res["windows"].get("dev", {})
    print(f"{mod.NAME}: OOS CAGR {o.get('annualized_return_pct', float('nan')):.2f}% | Sharpe {o.get('sharpe', float('nan')):.2f} | maxDD {o.get('max_drawdown_pct', float('nan')):.1f}% | cash {o.get('pct_days_cash', float('nan')):.0f}% | changes/yr {o.get('position_changes_per_year', float('nan')):.1f}  ||  DEV CAGR {d.get('annualized_return_pct', float('nan')):.2f}% Sharpe {d.get('sharpe', float('nan')):.2f} maxDD {d.get('max_drawdown_pct', float('nan')):.1f}%  || lookahead ok={res['lookahead_check']['ok']}  -> results/{stem}.json")


if __name__ == "__main__":
    main()
