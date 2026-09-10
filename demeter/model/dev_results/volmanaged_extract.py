"""Print the sections of dev_results/volmanaged.json needed for the design note (numbers copied, not remembered)."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parents[1] / "dev_results"
r = json.loads((HERE / (sys.argv[1] if len(sys.argv) > 1 else "volmanaged.json")).read_text())
print("params", r["params"], "n_tunable", r["n_tunable_params"], "grid", r.get("grid_file"), r.get("grid_n"))
print("coverage", r["signal_coverage"])
K = ["annualized_return_pct", "sharpe", "max_drawdown_pct", "worst_month_pct", "position_changes_per_year", "pct_days_cash",
     "avg_leverage", "up_capture_pct", "down_capture_pct", "beta_to_spy", "annualized_std_dev", "total_cost_drag_pct_annual", "pct_days_levered_gt1"]
for wk in ("windows", "windows_stress_cost_6_90", "windows_cost_2_40"):
    for w in ("dev_1990", "dev_1950"):
        x = r[wk][w]
        print(wk, w, {k: (round(x[k], 3) if x.get(k) is not None else None) for k in K if k in x})
for w, x in r["reference_bh_1x"].items():
    print("BH", w, {k: round(x[k], 3) for k in ("annualized_return_pct", "sharpe", "max_drawdown_pct", "worst_month_pct") if x.get(k) is not None})
print("-- eras")
for k, v in r["eras"].items():
    print(k, {kk: round(vv, 2) for kk, vv in v.items()})
print("-- stress")
for k, v in r["stress_episodes"].items():
    print(k, {kk: (round(vv, 2) if isinstance(vv, float) else vv) for kk, vv in v.items()})
print("-- census", json.dumps(r["spurious_reentry_census"]))
print("-- lookahead", r["lookahead_check"]["ok"], r["lookahead_check"]["max_abs_diff"], [d["cutoff"] for d in r["lookahead_check"]["details"]])
print("-- lev dist dev_1990 (top bins):", dict(sorted(r["leverage_distribution_dev_1990"].items(), key=lambda kv: -kv[1])[:12]))
for w in ("plateau_dev_1990", "plateau_dev_1950"):
    p = r.get(w)
    if p:
        print(f"-- {w}: base {p['base_sharpe']:.3f} share_within_25pct {p['share_within_25pct']:.3f} n {p['n_perturbations']}")
        for row in p["rows"]:
            print(f"   {row['param']:>10} {row['step']:+.2f} -> {row['value']:<8} sharpe {row['sharpe']:.3f} {'ok' if row['within_tol'] else 'OUT'}")
print("-- event ladders")
for d in ("2008-10-10", "2008-11-20", "2009-03-09", "2002-10-09", "1987-10-19", "1998-08-31", "2011-08-08"):
    e = r["event_ladders"].get(d)
    if not e: continue
    print(d, e["label"])
    for row in e["path"]:
        print(f"   {row['date']} ret {row['spx_ret_pct']:+.2f} vix {row['vix']} L {row['lev_target']}")
