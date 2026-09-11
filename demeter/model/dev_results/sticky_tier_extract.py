"""Print the fields of dev_results/sticky_tier.json needed for the design note and the RETURN json (no full-file reads)."""
import json
r = json.load(open("dev_results/sticky_tier.json"))
w9, w5 = r["windows"]["dev_1990"], r["windows"]["dev_1950"]
keys = ["annualized_return_pct", "sharpe", "sortino", "max_drawdown_pct", "worst_month_pct", "pct_days_cash", "avg_leverage", "avg_leverage_when_invested",
        "position_changes_per_year", "n_position_changes", "up_capture_pct", "down_capture_pct", "beta_to_spy", "total_cost_drag_pct_annual", "spy_annualized_return_pct", "spy_sharpe"]
print("params", r["params"], "n_tunable", r["n_tunable_params"], "coverage", r["signal_coverage"])
for name, w in [("dev_1990", w9), ("dev_1950", w5)]:
    print(name, {k: (round(w[k], 4) if isinstance(w[k], float) else w[k]) for k in keys})
for cs in ["windows_stress_cost_6_90", "windows_cost_2_40"]:
    x = r[cs]["dev_1990"]; print(cs, "dev_1990 sharpe", round(x["sharpe"], 4), "cagr", round(x["annualized_return_pct"], 3), "dd", round(x["max_drawdown_pct"], 2))
print("eras", {k: {kk: round(vv, 2) for kk, vv in v.items()} for k, v in r["eras"].items()})
print("stress", {k: {kk: (round(vv, 2) if isinstance(vv, float) else vv) for kk, vv in v.items()} for k, v in r["stress_episodes"].items()})
print("census", r["spurious_reentry_census"])
print("levdist", r["leverage_distribution_dev_1990"])
for d in ["2008-10-10", "2008-11-20", "2009-03-09", "2002-10-09", "1987-10-19"]:
    e = r["event_ladders"].get(d)
    if e:
        print(d, e["label"], " ".join(f"{p['date'][5:]}:{p['spx_ret_pct']:+.1f}%/L{p['lev_target']:.0f}" for p in e["path"]))
for pk in ["plateau_dev_1990", "plateau_dev_1950"]:
    pl = r[pk]; print(pk, "base", round(pl["base_sharpe"], 4), "share", pl["share_within_25pct"], "n", pl["n_perturbations"])
    print("  ", [(x["param"], x["step"], x["value"], (round(x["sharpe"], 3) if x["sharpe"] is not None else None), x["within_tol"]) for x in pl["rows"]])
print("lookahead", r["lookahead_check"]["ok"], r["lookahead_check"]["max_abs_diff"])
