import json, sys
from pathlib import Path
names = ["final_model_fewtrades", "baseline_volregime", "vix_vrp", "vix_dissipation", "volmanaged", "crash_exit_dual", "dissipation_reentry"]
for n in names:
    p = Path("dev_results") / f"{n}.json"
    if not p.exists():
        print(n, "MISSING"); continue
    r = json.loads(p.read_text())
    w9 = r["windows"]["dev_1990"] or {}
    w5 = r["windows"]["dev_1950"] or {}
    print(f"=== {n}  params={r['params']}  n_tunable={r['n_tunable_params']}")
    print(f"  dev_1990: CAGR {w9.get('annualized_return_pct')}, Sharpe {w9.get('sharpe')}, maxDD {w9.get('max_drawdown_pct')}, worstM {w9.get('worst_month_pct')}, cash% {w9.get('pct_days_cash')}, chg/yr {w9.get('position_changes_per_year')}, avgL {w9.get('avg_leverage')}, upcap {w9.get('up_capture_pct')}, dncap {w9.get('down_capture_pct')}")
    print(f"  dev_1950: CAGR {w5.get('annualized_return_pct')}, Sharpe {w5.get('sharpe')}, maxDD {w5.get('max_drawdown_pct')}, chg/yr {w5.get('position_changes_per_year')}")
    for k, v in (r.get("eras") or {}).items():
        print(f"  era {k}: CAGR {v["cagr_pct"]} Sharpe {v["sharpe"]} DD {v["max_dd_pct"]} chg {v['changes_per_year']:.1f} cash {v['pct_days_cash']:.0f}")
    for k, v in (r.get("stress_episodes") or {}).items():
        print(f"  stress {k}: model {v['model_total_pct']:+.1f} spy {v['spy_total_pct']:+.1f} DD {v['model_max_dd_pct']:.1f} avgL {v['avg_leverage']:.2f} cash {v['pct_days_cash']:.0f}")
    sc = r.get("spurious_reentry_census", {})
    for k, v in sc.items():
        print(f"  census {k}: n {v['n_entries_to_2x_plus']} neg {v['share_fwd10_negative']} mean {v['mean_fwd10_excess_pct']}")
    pl = r.get("plateau_dev_1990", {})
    print(f"  plateau: {pl.get('share_within_25pct')} base {pl.get('base_sharpe')}")
    print(f"  levdist: {r.get('leverage_distribution_dev_1990')}")
