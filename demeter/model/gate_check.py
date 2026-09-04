#!/usr/bin/env python3
"""Apply the pre-registered DEV gates (PREREG.md) to a dev_results/<stem>.json. Deterministic; no judgment.
Usage: python gate_check.py dev_results/<stem>.json   (exit code 0 = all gates pass)"""
from __future__ import annotations
import json, sys
from pathlib import Path

G2_SHARPE, G3_DD, G4_DD, G5_CHG, G6_PLATEAU, G7_PARAMS = 0.425, -30.0, -40.0, 25.0, 0.50, 6   # G2 = incumbent's dev_1990 Sharpe at 3/60 (0.42528), floored to 3 dp so the incumbent itself passes


def check(path: str) -> dict:
    r = json.loads(Path(path).read_text())
    w = r["windows"]["dev_1990"] or {}
    out = {"name": r["name"], "gates": {}}
    g = out["gates"]
    la = r.get("lookahead_check", {})
    g["G1_causality"] = {"pass": bool(la.get("ok")), "value": la.get("max_abs_diff"), "n_cutoffs": len(la.get("details", []))}
    g["G2_dev1990_sharpe"] = {"pass": (w.get("sharpe") or -9) >= G2_SHARPE, "value": w.get("sharpe"), "bar": G2_SHARPE}
    g["G3_dev1990_maxdd"] = {"pass": (w.get("max_drawdown_pct") or -99) >= G3_DD, "value": w.get("max_drawdown_pct"), "bar": G3_DD}
    era_rows, era_ok = {}, True
    for k, v in (r.get("eras") or {}).items():
        if v["pct_days_cash"] > 99.0:
            era_rows[k] = "N/A (all cash — signal not available in this era)"; continue
        ok = v["cagr_pct"] > 0 and v["max_dd_pct"] >= G4_DD
        era_ok &= ok
        era_rows[k] = f"{'ok' if ok else 'FAIL'}: CAGR {v['cagr_pct']:.2f}% maxDD {v['max_dd_pct']:.1f}%"
    g["G4_no_ruinous_era"] = {"pass": bool(era_ok), "value": era_rows}
    g["G5_changes_per_year"] = {"pass": (w.get("position_changes_per_year") or 999) <= G5_CHG, "value": w.get("position_changes_per_year"), "bar": G5_CHG}
    pl = r.get("plateau_dev_1990") or {}
    g["G6_plateau"] = {"pass": (pl.get("share_within_25pct") if pl.get("share_within_25pct") is not None else -1) >= G6_PLATEAU,
                       "value": pl.get("share_within_25pct"), "n": pl.get("n_perturbations"), "bar": G6_PLATEAU}
    g["G7_param_budget"] = {"pass": r.get("n_tunable_params", 99) <= G7_PARAMS, "value": r.get("n_tunable_params"), "bar": G7_PARAMS}
    out["all_pass"] = all(v["pass"] for v in g.values())
    return out


if __name__ == "__main__":
    res = check(sys.argv[1])
    print(f"{res['name']}: {'ALL GATES PASS' if res['all_pass'] else 'GATE FAILURE'}")
    for k, v in res["gates"].items():
        val = v["value"]
        if isinstance(val, dict):
            print(f"  {k}: {'pass' if v['pass'] else 'FAIL'}")
            for ek, ev in val.items():
                print(f"      {ek}: {ev}")
        else:
            bar = f" (bar {v['bar']})" if "bar" in v else ""
            print(f"  {k}: {'pass' if v['pass'] else 'FAIL'}  value={val}{bar}")
    sys.exit(0 if res["all_pass"] else 1)
