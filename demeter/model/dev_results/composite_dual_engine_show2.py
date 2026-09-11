"""Robust printer for composite_dual_engine dev_results JSONs (handles None fields)."""
import json, sys
from pathlib import Path


def f(x, nd=2, suf=""):
    return "n/a" if x is None else f"{x:.{nd}f}{suf}"


p = Path(sys.argv[1])
r = json.loads(p.read_text())
print(f"== {p.name} params={r['params']} n_tunable={r['n_tunable_params']}")
for w in ("dev_1990", "dev_1950"):
    m = r["windows"].get(w)
    if not m:
        print(f"  {w}: n/a"); continue
    print(f"  {w}: Sharpe {f(m['sharpe'],4)} CAGR {f(m['annualized_return_pct'])}% maxDD {f(m['max_drawdown_pct'])}% "
          f"worstM {f(m['worst_month_pct'])}% chg/yr {f(m['position_changes_per_year'])} cash {f(m['pct_days_cash'],1)}% "
          f"avgLev {f(m['avg_leverage'])} avgLevInv {f(m['avg_leverage_when_invested'])} upCap {f(m['up_capture_pct'],1)} "
          f"dnCap {f(m['down_capture_pct'],1)} beta {f(m['beta_to_spy'])} | SPY Sharpe {f(m['spy_sharpe'],3)} CAGR {f(m['spy_annualized_return_pct'])}%")
for tag in ("windows_stress_cost_6_90", "windows_cost_2_40"):
    m = r.get(tag, {}).get("dev_1990")
    if m:
        print(f"  {tag} dev_1990: Sharpe {f(m['sharpe'],4)} CAGR {f(m['annualized_return_pct'])}% maxDD {f(m['max_drawdown_pct'])}%")
for k, v in r["eras"].items():
    print(f"  era {k}: CAGR {f(v['cagr_pct'])}% Sharpe {f(v['sharpe'])} maxDD {f(v['max_dd_pct'],1)}% cash {f(v['pct_days_cash'],0)}% chg/yr {f(v['changes_per_year'],1)}")
for k, v in r["stress_episodes"].items():
    print(f"  stress {k}: model {f(v['model_total_pct'],1)}% (SPY {f(v['spy_total_pct'],1)}%) DD {f(v['model_max_dd_pct'],1)}% "
          f"avgL {f(v['avg_leverage'])} cash {f(v['pct_days_cash'],0)}% 3x {f(v['pct_days_3x'],0)}% chg {v['n_changes']}")
for k, v in r["spurious_reentry_census"].items():
    print(f"  census {k}: n>=2x {v['n_entries_to_2x_plus']} meanFwd10 {v['mean_fwd10_excess_pct']} shareNeg {v['share_fwd10_negative']} "
          f"pctDays2x+ {f(v['pct_days_2x_plus'],1)} dates {v['dates']}")
print(f"  lev dist 1990+: {r['leverage_distribution_dev_1990']}")
la = r["lookahead_check"]
print(f"  lookahead ok={la['ok']} maxdiff={la['max_abs_diff']}")
for w in ("plateau_dev_1990", "plateau_dev_1950"):
    pl = r.get(w)
    if pl:
        print(f"  {w}: base {f(pl['base_sharpe'],4)} share_within_25 {f(pl['share_within_25pct'],3)} n {pl['n_perturbations']}")
        bad = [(x['param'], x['step'], x['value'], None if x['sharpe'] is None else round(x['sharpe'], 3)) for x in pl['rows'] if not x['within_tol']]
        print(f"    outside tol: {bad}")
if "--ladders" in sys.argv:
    for d in ("2008-10-10", "2008-11-20", "2009-03-09", "2002-10-09", "1998-08-31", "1987-10-19", "2011-08-08", "2002-07-23", "2001-09-21"):
        e = r["event_ladders"].get(d)
        if e:
            print(f"  ladder {d} {e['label']}: " + " | ".join(
                f"{x['date'][5:]} r{x['spx_ret_pct']:+.1f} v{x['vix']} L{x['lev_target']}" for x in e["path"]))
