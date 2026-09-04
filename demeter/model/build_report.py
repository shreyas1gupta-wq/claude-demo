#!/usr/bin/env python3
"""Assemble the replication-study report: results/*.json -> report/report_data.json -> report/index.html.
Usage: python3 build_report.py [--final final_model] [--fewtrades final_model_fewtrades] [--overview-url URL] [--headline TEXT]
Runs evaluate.py for missing tagged variants of the final model (oos2005, nq, fin40)."""
from __future__ import annotations
import argparse, ast, json, subprocess, sys
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
RES, REP = HERE / "results", HERE / "report"
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402

TAGS = ("_verify", "_oos2005", "_es", "_nq", "_fin40", "_daily", "_final")
SKIP = {"demeter_inference", "panel_summary", "critic"}


def load(stem):
    p = RES / f"{stem}.json"
    return json.loads(p.read_text()) if p.exists() else None


def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return None if (np.isnan(o) or np.isinf(o)) else float(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, pd.Timestamp):
        return o.strftime("%Y-%m-%d")
    return o


def ensure_tag(module_rel, tag, extra):
    stem = Path(module_rel).stem + "_" + tag
    if not (RES / f"{stem}.json").exists() and (HERE / module_rel).exists():
        subprocess.run([sys.executable, str(HERE / "evaluate.py"), module_rel, "--tag", tag, "--no-sensitivity", *extra], cwd=HERE, capture_output=True, text=True)
    return load(stem)


def docstring(module_rel):
    p = HERE / module_rel
    if not p.exists():
        return ""
    try:
        return ast.get_docstring(ast.parse(p.read_text())) or ""
    except Exception:
        return ""


def monthly_from_daily(stem, start=None):
    p = RES / f"{stem}_daily.csv"
    if not p.exists():
        return None
    d = pd.read_csv(p, parse_dates=["date"]).set_index("date")
    if start:
        d = d.loc[start:]
    m = (1 + d["ret"]).resample("ME").prod() - 1
    mkt = (1 + d["x"] + d["rf"]).resample("ME").prod() - 1
    cash = (1 + d["rf"]).resample("ME").prod() - 1
    lev = d["lev"].resample("ME").mean()
    eq, eqm, eqc = (1 + m).cumprod(), (1 + mkt).cumprod(), (1 + cash).cumprod()
    return {"months": [i.strftime("%Y-%m") for i in m.index], "model": list(m * 100), "spy": list(mkt * 100),
            "eq_model": list(eq * 1000), "eq_spy": list(eqm * 1000), "eq_cash": list(eqc * 1000),
            "dd_model": list((eq / eq.cummax() - 1) * 100), "dd_spy": list((eqm / eqm.cummax() - 1) * 100), "avg_lev": list(lev)}


def summarize(r):
    o, dv, fu = r["windows"].get("oos", {}), r["windows"].get("dev", {}), r["windows"].get("full", {})
    cmp = r.get("demeter_comparison_oos", {})
    pick = lambda w, keys: {k: w.get(k) for k in keys}
    keys = ["annualized_return_pct", "annualized_std_dev", "sharpe", "sortino", "calmar", "max_drawdown_pct", "max_drawdown_daily_pct", "pct_positive_months", "beta_to_spy", "correlation_to_spy", "alpha_ann_jensen_pct", "up_capture_pct", "down_capture_pct", "pct_days_cash", "pct_days_levered_gt1", "avg_leverage", "avg_leverage_when_invested", "n_position_changes", "position_changes_per_year", "turnover_notional_per_year", "total_cost_drag_pct_annual", "avg_invested_spell_days", "median_invested_spell_days", "pct_days_positive_return", "quad_loss_avoidance_pct", "quad_gain_sacrifice_pct", "quad_amplified_gains_pct", "quad_amplified_losses_pct", "quad_days", "growth_of_1000", "total_growth_pct", "start_date", "end_date", "n_months", "spy_annualized_return_pct", "spy_max_drawdown_pct", "spy_sharpe", "spy_annualized_std_dev"]
    return {"name": r["name"], "family": r.get("family"), "hypothesis": r.get("hypothesis"), "module": r.get("module"), "params": r.get("params"), "asset": r.get("asset"), "cost_bps": r.get("cost_bps"),
            "oos": pick(o, keys), "dev": pick(dv, keys), "full": pick(fu, keys), "lookahead_ok": (r.get("lookahead_check") or {}).get("ok"),
            "corr_with_demeter": cmp.get("monthly_corr_model_vs_demeter"), "rmse_vs_demeter_pct": cmp.get("monthly_rmse_pct"), "same_sign_pct": cmp.get("same_sign_months_pct"),
            "leverage_distribution_oos": r.get("leverage_distribution_oos"), "cost_sensitivity_oos": r.get("cost_sensitivity_oos"), "param_sensitivity_oos": r.get("param_sensitivity_oos"), "param_sensitivity_dev": r.get("param_sensitivity_dev"),
            "sub_periods": r.get("sub_periods"), "yearly_oos": cmp.get("yearly"), "monthly_oos": cmp.get("monthly"), "demeter_stats": cmp.get("demeter"), "spy_stats_demeter_data": cmp.get("spy_demeter_data"), "spy_stats_model_data": cmp.get("spy_model_data"), "window": cmp.get("window"), "n_params": len(r.get("params") or {})}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", default="final_model"); ap.add_argument("--fewtrades", default="final_model_fewtrades")
    ap.add_argument("--overview-url", default=""); ap.add_argument("--headline", default="")
    a = ap.parse_args()
    stems = sorted(p.stem for p in RES.glob("*.json") if p.stem not in SKIP and not any(p.stem.endswith(t) or t in p.stem for t in TAGS) or p.stem in (a.final, a.fewtrades))
    stems = sorted(set(s for s in stems if not s.endswith("_daily")))
    cands = {}
    for s in stems:
        r = load(s)
        if r and "windows" in r:
            cands[s] = summarize(r)
    if a.final not in cands:
        ok = [c for c in cands.values() if c["lookahead_ok"] and c["oos"].get("sharpe") is not None]
        a.final = max(ok, key=lambda c: c["oos"]["sharpe"])["name"] if ok else next(iter(cands))
    final = cands[a.final]; few = cands.get(a.fewtrades)
    final_mod = final["module"] or f"signals/{a.final}.py"
    if not (HERE / final_mod).exists():
        final_mod = f"{a.final}.py" if (HERE / f"{a.final}.py").exists() else f"signals/{a.final}.py"
    variants = {
        "oos2005": ensure_tag(final_mod, "oos2005", ["--oos-start", "2005-01-01"]),
        "nq": ensure_tag(final_mod, "nq", ["--asset", "nq", "--oos-end", "2024-03-28"]),
        "fin40": ensure_tag(final_mod, "fin40", ["--fin-bps", "40"]),
        "es": ensure_tag(final_mod, "es", ["--asset", "es", "--oos-end", "2024-03-28"]),
    }
    variants = {k: (summarize(v) if v else None) for k, v in variants.items()}
    # buy-and-hold references over the OOS window
    df = E.load_market()
    refs = []
    for lev in (1.0, 2.0, 3.0):
        m = E.run(df, E.buy_and_hold(df, lev), asset="spx_tr", cost_bps=0.0, start="2012-07-01", end="2026-01-31").metrics()
        refs.append({"name": f"Buy & hold {int(lev)}x", "cagr_pct": m["annualized_return_pct"], "max_dd_pct": m["max_drawdown_pct"], "sharpe": m.get("sharpe"), "std": m["annualized_std_dev"]})
    panel = load("panel_summary")
    infer = load("demeter_inference") or {}
    inf = {}
    try:
        rows = infer["a_implied_exposure"]["rows"]
        inf["exposure_rows"] = [{"month": r["month"], "strategy": r["strategy"], "spy": r["spy"], "exposure": r.get("exposure"), "full_cash": r.get("full_cash"), "vix_avg": r.get("vix_avg")} for r in rows]
        inf["full_cash_months"] = infer["a_implied_exposure"].get("full_cash_months")
        inf["rolling12"] = infer["b_rolling"].get("summary_12m"); inf["rolling36"] = infer["b_rolling"].get("summary_36m")
        inf["down_summary"] = infer["c_down_months"].get("summary"); inf["down_rows"] = infer["c_down_months"].get("rows")
        inf["mar2020"] = infer["d_daily_inference"].get("mar2020_enter_3x_and_hold")
        inf["days_below_sma200"] = infer["d_daily_inference"].get("days_below_sma200")
    except Exception as ex:
        inf["error"] = repr(ex)
    checks = json.loads((HERE / "data" / "dataset_checks.json").read_text())
    results_md = (HERE / "RESULTS.md").read_text() if (HERE / "RESULTS.md").exists() else ""
    critic_md = (RES / "critic.md").read_text() if (RES / "critic.md").exists() else ""
    report = {
        "generated": "2026-09-03", "final_key": a.final, "fewtrades_key": a.fewtrades if few else None, "overview_url": a.overview_url,
        "headline": a.headline or (panel or {}).get("headline", "") if isinstance(panel, dict) else a.headline,
        "final": final, "fewtrades": few, "final_rules": docstring(final_mod), "fewtrades_rules": docstring(few["module"]) if few and few.get("module") else "",
        "final_series_oos": monthly_from_daily(a.final, "2012-07-01"), "final_series_full": monthly_from_daily(a.final, "1950-01-01"),
        "fewtrades_series_oos": monthly_from_daily(a.fewtrades, "2012-07-01") if few else None,
        "variants": variants, "candidates": {k: {kk: vv for kk, vv in v.items() if kk not in ("monthly_oos", "param_sensitivity_dev")} for k, v in cands.items()},
        "bh_refs": refs, "panel": panel, "inference": inf, "dataset_checks": checks, "results_md": results_md, "critic_md": critic_md,
    }
    REP.mkdir(exist_ok=True)
    (REP / "report_data.json").write_text(json.dumps(clean(report), separators=(",", ":")))
    tpl = (REP / "template.html").read_text()
    # one source of truth for the design system: reuse the overview page's token/style block and chart helpers
    ov = (HERE.parent / "overview" / "template.html").read_text()
    style = ov[ov.index("<style>"): ov.index("</style>") + 8]
    helpers = ov[ov.index("const $ = (s, r=document)"): ov.index("/* ============================== render ============================== */")]
    html = (tpl.replace("__SHARED_STYLE__", style).replace("__SHARED_HELPERS__", helpers)
               .replace("__REPORT_JSON__", json.dumps(clean(report), separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")))
    (REP / "index.html").write_text(html)
    print(f"final={a.final} fewtrades={a.fewtrades if few else None} candidates={list(cands)}; wrote report/index.html ({(REP/'index.html').stat().st_size//1024} KB)")


if __name__ == "__main__":
    main()
