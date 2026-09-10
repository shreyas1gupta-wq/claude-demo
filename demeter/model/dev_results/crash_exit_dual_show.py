"""Print the parts of a dev_results JSON that matter for crash_exit_dual: windows, stress, census, ladders, plateau."""
import json, sys
from pathlib import Path
p = Path(sys.argv[1])
r = json.loads(p.read_text())
print(f"== {p.name} params={r['params']}")
for wk in ("windows", "windows_stress_cost_6_90", "windows_cost_2_40"):
    for w in ("dev_1990", "dev_1950"):
        v = r[wk][w]
        if v:
            print(f"  {wk:26s} {w}: CAGR {v['annualized_return_pct']:6.2f} Sharpe {v['sharpe']:.3f} maxDD {v['max_drawdown_pct']:6.1f} worstM {v['worst_month_pct']:6.1f} cash {v['pct_days_cash']:4.1f}% chg/yr {v['position_changes_per_year']:5.1f} up {v['up_capture_pct']:.0f} dn {v['down_capture_pct']:.0f} avgL {v['avg_leverage']:.2f}")
for k, v in r["eras"].items():
    print(f"  era {k:12s}: CAGR {v['cagr_pct']:6.2f} (SPY {v['spy_cagr_pct']:5.2f}) Sharpe {v['sharpe']:.2f} maxDD {v['max_dd_pct']:6.1f} worstM {v['worst_month_pct']:6.1f} chg/yr {v['changes_per_year']:.1f}")
for k, v in r["stress_episodes"].items():
    print(f"  stress {k:18s}: model {v['model_total_pct']:+7.1f}% SPY {v['spy_total_pct']:+7.1f}% DD {v['model_max_dd_pct']:6.1f} avgL {v['avg_leverage']:.2f} cash {v['pct_days_cash']:3.0f}% 3x {v['pct_days_3x']:3.0f}% chg {v['n_changes']}")
for k, v in r["spurious_reentry_census"].items():
    print(f"  census {k}: n {v['n_entries_to_2x_plus']} mean_fwd10 {v['mean_fwd10_excess_pct']} share_neg {v['share_fwd10_negative']} pct2x {v['pct_days_2x_plus']:.1f} dates {v['dates'][:12]}")
for d, lad in r["event_ladders"].items():
    print(f"  ladder {d} {lad['label']:20s}: " + " ".join(f"{p['date'][5:]}:{p['spx_ret_pct']:+.1f}/L{p['lev_target']}" for p in lad["path"]))
for pk in ("plateau_dev_1990", "plateau_dev_1950"):
    pl = r.get(pk)
    if pl:
        print(f"  {pk}: {pl['share_within_25pct']:.2f} of {pl['n_perturbations']} (base {pl['base_sharpe']:.3f})")
        for row in pl["rows"]:
            print(f"      {row['param']:8s} {row['step']:+.2f} -> {row['value']}: sharpe {row['sharpe'] if row['sharpe'] is None else round(row['sharpe'],3)} {'ok' if row['within_tol'] else 'X'}")
print(f"  lookahead ok={r['lookahead_check']['ok']}  lev dist 1990: {{ {', '.join(f'{k}:{v:.1f}' for k, v in r['leverage_distribution_dev_1990'].items())} }}")
