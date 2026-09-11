"""Print the fields of a dev_results JSON that matter for the design note (never Read the JSON itself)."""
import json, sys
from pathlib import Path

p = Path(sys.argv[1])
r = json.loads(p.read_text())
print(f"== {p.name}  params={r['params']}  n_tunable={r['n_tunable_params']}")
for w in ("dev_1990", "dev_1950"):
    m = r["windows"].get(w)
    if not m:
        print(f"  {w}: n/a"); continue
    print(f"  {w}: Sharpe {m['sharpe']:.4f} CAGR {m['annualized_return_pct']:.2f}% maxDD {m['max_drawdown_pct']:.2f}% "
          f"worstM {m['worst_month_pct']:.2f}% chg/yr {m['position_changes_per_year']:.2f} cash {m['pct_days_cash']:.1f}% "
          f"avgLev {m['avg_leverage']:.2f} avgLevInv {m['avg_leverage_when_invested']:.2f} upCap {m['up_capture_pct']:.1f} "
          f"dnCap {m['down_capture_pct']:.1f} beta {m['beta_to_spy']:.2f} | SPY Sharpe {m['spy_sharpe']:.3f} CAGR {m['spy_annualized_return_pct']:.2f}%")
for tag in ("windows_stress_cost_6_90", "windows_cost_2_40"):
    m = r.get(tag, {}).get("dev_1990")
    if m:
        print(f"  {tag} dev_1990: Sharpe {m['sharpe']:.4f} CAGR {m['annualized_return_pct']:.2f}% maxDD {m['max_drawdown_pct']:.2f}%")
for k, v in r["eras"].items():
    print(f"  era {k}: CAGR {v['cagr_pct']:.2f}% Sharpe {v['sharpe']:.2f} maxDD {v['max_dd_pct']:.1f}% cash {v['pct_days_cash']:.0f}% chg/yr {v['changes_per_year']:.1f}")
for k, v in r["stress_episodes"].items():
    print(f"  stress {k}: model {v['model_total_pct']:+.1f}% (SPY {v['spy_total_pct']:+.1f}%) DD {v['model_max_dd_pct']:.1f}% "
          f"avgL {v['avg_leverage']:.2f} cash {v['pct_days_cash']:.0f}% 3x {v['pct_days_3x']:.0f}% chg {v['n_changes']}")
for k, v in r["spurious_reentry_census"].items():
    print(f"  census {k}: n>=2x {v['n_entries_to_2x_plus']} meanFwd10 {v['mean_fwd10_excess_pct']} shareNeg {v['share_fwd10_negative']} "
          f"pctDays2x+ {v['pct_days_2x_plus']:.1f} dates {v['dates']}")
print(f"  lev dist 1990+: {r['leverage_distribution_dev_1990']}")
la = r["lookahead_check"]
print(f"  lookahead ok={la['ok']} maxdiff={la['max_abs_diff']}")
for w in ("plateau_dev_1990", "plateau_dev_1950"):
    pl = r.get(w)
    if pl:
        print(f"  {w}: base {pl['base_sharpe']:.4f} share_within_25 {pl['share_within_25pct']:.3f} n {pl['n_perturbations']}")
        bad = [(x['param'], x['step'], x['value'], None if x['sharpe'] is None else round(x['sharpe'], 3)) for x in pl['rows'] if not x['within_tol']]
        print(f"    outside tol: {bad}")
if "--ladders" in sys.argv:
    for d in ("2008-10-10", "2008-11-20", "2009-03-09", "2002-10-09", "1998-08-31", "1987-10-19", "2011-08-08"):
        e = r["event_ladders"].get(d)
        if e:
            print(f"  ladder {d} {e['label']}: " + " | ".join(f"{x['date'][5:]} r{x['spx_ret_pct']:+.1f} v{x['vix']} L{x['lev_target']}" for x in e["path"]))
