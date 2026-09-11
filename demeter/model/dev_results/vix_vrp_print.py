"""Print the fields of a dev_results JSON that matter (never Read the JSON directly)."""
import json, sys
from pathlib import Path
p = Path(sys.argv[1])
r = json.loads(p.read_text())
print("name", r["name"], "params", r["params"], "n_tunable", r["n_tunable_params"])
for w in ("windows", "windows_stress_cost_6_90", "windows_cost_2_40"):
    for k, v in (r.get(w) or {}).items():
        if v:
            print(f"{w}/{k}: CAGR {v['annualized_return_pct']:.2f} Sharpe {v['sharpe']:.4f} maxDD {v['max_drawdown_pct']:.2f} "
                  f"dailyDD {v['max_drawdown_daily_pct']:.2f} worstM {v['worst_month_pct']:.2f} cash {v['pct_days_cash']:.1f} "
                  f"avgL {v['avg_leverage']:.2f} avgLinv {v['avg_leverage_when_invested']:.2f} chg/yr {v['position_changes_per_year']:.2f} "
                  f"up {v['up_capture_pct']:.0f} dn {v['down_capture_pct']:.0f} beta {v['beta_to_spy']:.2f} cost {v['total_cost_drag_pct_annual']:.2f}")
for k, v in r["eras"].items():
    print(f"era {k}: CAGR {v['cagr_pct']:.2f} (SPY {v['spy_cagr_pct']:.2f}) Sharpe {v['sharpe']} maxDD {v['max_dd_pct']:.1f} cash {v['pct_days_cash']:.0f} chg {v['changes_per_year']:.1f} worstM {v['worst_month_pct']:.1f}")
for k, v in r["stress_episodes"].items():
    print(f"stress {k}: model {v['model_total_pct']:+.1f} (SPY {v['spy_total_pct']:+.1f}) DD {v['model_max_dd_pct']:.1f} (SPY {v['spy_max_dd_pct']:.1f}) avgL {v['avg_leverage']:.2f} cash {v['pct_days_cash']:.0f} nchg {v['n_changes']}")
for k, v in r["spurious_reentry_census"].items():
    print(f"census {k}: n {v['n_entries_to_2x_plus']} mean_fwd10 {v['mean_fwd10_excess_pct']} share_neg {v['share_fwd10_negative']} pct2x {v['pct_days_2x_plus']:.1f} dates {v['dates'][:12]}")
print("lev dist 1990:", r["leverage_distribution_dev_1990"])
print("lookahead:", r["lookahead_check"]["ok"], r["lookahead_check"]["max_abs_diff"], [x["cutoff"] for x in r["lookahead_check"]["details"]])
for w in ("plateau_dev_1990", "plateau_dev_1950"):
    pl = r.get(w)
    if pl:
        print(f"{w}: base {pl['base_sharpe']:.4f} share {pl['share_within_25pct']:.2f} n {pl['n_perturbations']}")
        for row in pl["rows"]:
            print(f"   {row['param']} {row['step']:+.2f} -> {row['value']}: {row['sharpe']}")
if "--ladders" in sys.argv:
    for d, v in r["event_ladders"].items():
        print(d, v["label"], " ".join(f"{x['date'][5:]}:{x['spx_ret_pct']:+.1f}/{x['vix']}/{x['lev_target']}" for x in v["path"]))
