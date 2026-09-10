#!/usr/bin/env python3
"""Print the numbers the design note / structured output need, straight from dev_results/dissipation_reentry.json."""
import json, sys
from pathlib import Path

p = Path(sys.argv[1] if len(sys.argv) > 1 else "dev_results/dissipation_reentry.json")
r = json.loads(p.read_text())
print("params:", r["params"], "n_tunable:", r["n_tunable_params"])
for w in ("dev_1990", "dev_1950"):
    v = r["windows"][w]
    print(f"{w}: sharpe {v['sharpe']:.4f} cagr {v['annualized_return_pct']:.3f} maxdd {v['max_drawdown_pct']:.3f} "
          f"worstM {v['worst_month_pct']:.3f} cash {v['pct_days_cash']:.2f} chg/yr {v['position_changes_per_year']:.3f} "
          f"upcap {v['up_capture_pct']:.1f} dncap {v['down_capture_pct']:.1f} beta {v['beta_to_spy']:.2f} avgLev {v['avg_leverage']:.3f} "
          f"cost_drag {v['total_cost_drag_pct_annual']:.3f}")
for tag in ("windows_stress_cost_6_90", "windows_cost_2_40"):
    v = r[tag]["dev_1990"]
    print(f"{tag} dev_1990: sharpe {v['sharpe']:.4f} cagr {v['annualized_return_pct']:.3f} maxdd {v['max_drawdown_pct']:.3f}")
print("eras:")
for k, v in r["eras"].items():
    print(f"  {k}: cagr {v['cagr_pct']:.2f} (spy {v['spy_cagr_pct']:.2f}) sharpe {v['sharpe']:.3f} maxdd {v['max_dd_pct']:.2f} cash {v['pct_days_cash']:.1f} chg {v['changes_per_year']:.2f} worstM {v['worst_month_pct']:.2f}")
print("stress:")
for k, v in r["stress_episodes"].items():
    print(f"  {k}: model {v['model_total_pct']:.3f} spy {v['spy_total_pct']:.2f} dd {v['model_max_dd_pct']:.2f} avgL {v['avg_leverage']:.2f} cash {v['pct_days_cash']:.1f} 3x {v['pct_days_3x']:.1f} chg {v['n_changes']}")
print("census:")
for k, v in r["spurious_reentry_census"].items():
    print(f"  {k}: n {v['n_entries_to_2x_plus']} dates {v['dates']} mean_fwd10 {v['mean_fwd10_excess_pct']} share_neg {v['share_fwd10_negative']} pct_days_2x {v['pct_days_2x_plus']:.2f}")
print("ladders:")
for d in ("1987-10-19", "1998-08-31", "1998-10-08", "2001-09-21", "2002-07-23", "2002-10-09", "2008-10-10", "2008-10-27", "2008-11-20", "2009-03-09", "2010-07-02", "2011-08-08", "2011-10-03"):
    e = r["event_ladders"].get(d)
    if not e:
        continue
    path = " | ".join(f"{x['date'][5:]} {x['spx_ret_pct']:+.1f}% v{x['vix'] if x['vix'] is not None else '-'} L{x['lev_target']:.0f}" for x in e["path"])
    print(f"  {d} ({e['label']}): {path}")
for w in ("plateau_dev_1990", "plateau_dev_1950"):
    pl = r[w]
    print(f"{w}: base {pl['base_sharpe']:.4f} share {pl['share_within_25pct']:.3f} of {pl['n_perturbations']}")
    for row in pl["rows"]:
        print(f"    {row['param']:>9} {row['step']:+.2f} -> {row['value']}: sharpe {row['sharpe'] if row['sharpe'] is None else round(row['sharpe'], 3)} {'ok' if row['within_tol'] else 'FAIL'}")
print("lookahead:", r["lookahead_check"]["ok"], r["lookahead_check"]["max_abs_diff"])
print("lev dist 1990:", r["leverage_distribution_dev_1990"])
print("coverage:", r["signal_coverage"])
