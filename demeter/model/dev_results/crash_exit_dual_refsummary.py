"""Summarise the four DEV reference JSONs (stress, ladders, census) so I read conclusions, not 150KB of JSON."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
names = ["final_model_fewtrades", "baseline_volregime", "vix_dissipation", "vix_vrp"]
for n in names:
    r = json.loads((HERE / f"{n}.json").read_text())
    w = r["windows"]["dev_1990"]
    print(f"\n=== {n}  params={r['params']}")
    print(f"  dev_1990: CAGR {w['annualized_return_pct']:.2f} Sharpe {w['sharpe']:.3f} maxDD {w['max_drawdown_pct']:.1f} worstM {w['worst_month_pct']:.1f} cash {w['pct_days_cash']:.0f}% chg/yr {w['position_changes_per_year']:.1f} upcap {w['up_capture_pct']:.0f} dncap {w['down_capture_pct']:.0f}")
    for k, v in r["stress_episodes"].items():
        print(f"  stress {k:18s}: model {v['model_total_pct']:+7.1f}% SPY {v['spy_total_pct']:+7.1f}% DD {v['model_max_dd_pct']:6.1f} avgL {v['avg_leverage']:.2f} cash {v['pct_days_cash']:.0f}% chg {v['n_changes']}")
    for k, v in r["spurious_reentry_census"].items():
        print(f"  census {k}: n {v['n_entries_to_2x_plus']} mean_fwd10 {v['mean_fwd10_excess_pct']} share_neg {v['share_fwd10_negative']} pct2x {v['pct_days_2x_plus']:.1f}")
    for d in ["1987-10-19", "1998-08-31", "2008-10-10", "2008-11-20", "2009-03-09", "2002-10-09"]:
        lad = r["event_ladders"].get(d)
        if lad:
            print(f"  ladder {d} {lad['label']}: " + " ".join(f"{p['date'][5:]}:{p['spx_ret_pct']:+.1f}/L{p['lev_target']}" for p in lad["path"]))
    pl = r.get("plateau_dev_1990", {})
    print(f"  plateau {pl.get('share_within_25pct')} of {pl.get('n_perturbations')}")
    print(f"  lev dist 1990: {r['leverage_distribution_dev_1990']}")
