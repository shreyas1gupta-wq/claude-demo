#!/usr/bin/env python3
"""Pass-2 comparison tables from results/*.json (+ *_daily.csv): leaderboard at 3/60, DEV-vs-OOS, cost rows,
acceptance criteria, the two asymmetries (T-bill on cash days zeroed; clustered slippage), and the re-entry
fire-date check on the three named OOS dates.  Writes results/pass2_summary.json and prints markdown tables.
Usage: python compare_final.py name1 name2 ...   (names = results/<name>.json at 3/60; _c240/_s690 picked up if present)"""
from __future__ import annotations
import json, sys
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402

RES = HERE / "results"
OOS = ("2012-07-01", "2026-02-11")
INCUMBENT = {"sharpe": 0.7336, "max_dd": -20.55, "changes": 9.2}
FIRE_DATES = ["2018-12-24", "2018-12-26", "2020-03-20", "2020-03-23", "2020-03-24", "2022-10-12", "2022-10-13", "2022-10-14", "2025-04-08", "2025-04-09"]


def load(stem):
    p = RES / f"{stem}.json"
    return json.loads(p.read_text()) if p.exists() else None


def daily(stem):
    p = RES / f"{stem}_daily.csv"
    return pd.read_csv(p, parse_dates=["date"]).set_index("date") if p.exists() else None


def adj_metrics(d: pd.DataFrame, df: pd.DataFrame, cost_bps: float):
    """(a) T-bill zeroed on cash days (Demeter's convention); (b) clustered slippage: cost x max(1, RV21/0.15)."""
    d = d.loc[OOS[0]:OOS[1]].copy()
    mk = pd.DataFrame(index=d.index)
    mk["mkt_tr_ret"] = df["spx_tr_ret"].reindex(d.index)
    base = d["ret"]
    ret_nocash = base - d["rf"].where(d["lev"] == 0, 0.0)
    rv = (df["spx_ret"].rolling(21).std() * np.sqrt(252)).reindex(d.index)
    trade = d["lev"].diff().abs().fillna(0.0)
    extra = trade * cost_bps / 1e4 * (np.maximum(1.0, rv / 0.15) - 1.0)
    ret_cluster = base - extra.fillna(0.0)
    out = {}
    for k, r in [("base", base), ("tbill_zeroed_on_cash", ret_nocash), ("clustered_slippage", ret_cluster)]:
        frame = pd.DataFrame({"ret": r, "mkt_tr_ret": mk["mkt_tr_ret"], "rf": d["rf"], "lev": d["lev"], "x": d["x"], "cost": 0.0})
        m = E.metrics(frame)
        out[k] = {"cagr_pct": m["annualized_return_pct"], "sharpe": m.get("sharpe"), "max_dd_pct": m["max_drawdown_pct"]}
    out["tbill_on_cash_days_pct_annual"] = float(d["rf"].where(d["lev"] == 0, 0.0).mean() * 252 * 100)
    return out


def fire_check(d: pd.DataFrame):
    rows = []
    for t in FIRE_DATES:
        ts = pd.Timestamp(t)
        if ts in d.index:
            i = d.index.get_loc(ts)
            # lev column = position in effect that day (decided previous close); target decided at close t = lev[t+1]
            tgt = float(d["lev"].iloc[i + 1]) if i + 1 < len(d) else None
            rows.append({"date": t, "position_in_effect": float(d["lev"].iloc[i]), "target_decided_at_close": tgt})
    return rows


def main():
    names = sys.argv[1:]
    df = E.load_market()
    summary = {"names": names, "rows": []}
    for n in names:
        r = load(n)
        if not r:
            print(f"missing results/{n}.json"); continue
        o, dv = r["windows"]["oos"], r["windows"].get("dev", {})
        cmp = r["demeter_comparison_oos"]["model"]
        row = {"name": n, "family": r["family"], "params": r["params"], "n_params": len(r["params"]),
               "cost": f"{r['cost_bps']:g}/{r['financing_spread_bps']:g}",
               "oos": {k: o.get(k) for k in ["annualized_return_pct", "sharpe", "sortino", "calmar", "max_drawdown_pct", "position_changes_per_year", "pct_days_cash", "avg_leverage_when_invested", "up_capture_pct", "down_capture_pct", "beta_to_spy", "worst_month_pct", "pct_positive_months"]},
               "dev": {k: dv.get(k) for k in ["annualized_return_pct", "sharpe", "max_drawdown_pct", "position_changes_per_year"]},
               "corr_demeter": r["demeter_comparison_oos"]["monthly_corr_model_vs_demeter"],
               "lookahead_ok": r["lookahead_check"]["ok"], "sub_periods": r.get("sub_periods"),
               "yearly": r.get("yearly_oos")}
        for tag in ("c240", "s690"):
            rr = load(f"{n}_{tag}")
            if rr:
                oo = rr["windows"]["oos"]
                row[tag] = {"cagr_pct": oo["annualized_return_pct"], "sharpe": oo.get("sharpe"), "max_dd_pct": oo["max_drawdown_pct"]}
        d = daily(n)
        if d is not None:
            row["adjusted"] = adj_metrics(d, df, r["cost_bps"])
            row["fire_check"] = fire_check(d)
        ps = r.get("param_sensitivity_dev") or []
        if ps:
            b = ps[0]["sharpe"]
            held = [abs(x["sharpe"] - b) <= 0.25 * abs(b) for x in ps[1:] if x.get("sharpe") is not None and b]
            row["dev_plateau_share"] = float(np.mean(held)) if held else None
        acc = {"sharpe_gt_0.73": (o.get("sharpe") or 0) > INCUMBENT["sharpe"],
               "maxdd_ge_-20.5": (o.get("max_drawdown_pct") or -99) >= INCUMBENT["max_dd"],
               "changes_lt_25": (o.get("position_changes_per_year") or 99) < 25,
               "no_ruinous_era": all((sp["cagr_pct"] > 0 and sp["max_dd_pct"] > -40) for sp in (r.get("sub_periods") or []) if sp["start"] < "2012") if r.get("sub_periods") else None,
               "lookahead": r["lookahead_check"]["ok"]}
        if "s690" in row:
            acc["survives_6_90"] = (row["s690"]["sharpe"] or 0) > INCUMBENT["sharpe"]
        acc["ALL"] = all(v for v in acc.values() if v is not None)
        row["acceptance"] = acc
        summary["rows"].append(row)
    (RES / "pass2_summary.json").write_text(json.dumps(summary, indent=1, default=lambda x: None if isinstance(x, float) and np.isnan(x) else str(x)))

    # ---- markdown
    f = lambda v, d=2: ("—" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:.{d}f}")
    print("\n### Leaderboard (OOS Jul 2012 – Jan/Feb 2026, 3 bp / 60 bp)\n")
    print("| Candidate | OOS CAGR | OOS Sharpe | OOS maxDD | Chg/yr | Cash % | Down-capture | DEV Sharpe | DEV maxDD | Corr. Demeter | Accept |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for x in sorted(summary["rows"], key=lambda z: -(z["oos"]["sharpe"] or -9)):
        o = x["oos"]
        print(f"| {x['name']} | {f(o['annualized_return_pct'])}% | {f(o['sharpe'])} | {f(o['max_drawdown_pct'],1)}% | {f(o['position_changes_per_year'],1)} | {f(o['pct_days_cash'],0)} | {f(o['down_capture_pct'],0)}% | {f(x['dev']['sharpe'])} | {f(x['dev']['max_drawdown_pct'],1)}% | {f(x['corr_demeter'])} | {'YES' if x['acceptance']['ALL'] else 'no'} |")
    print("\n### Cost rows\n\n| Candidate | 2/40 CAGR | 2/40 Sharpe | 3/60 CAGR | 3/60 Sharpe | 6/90 CAGR | 6/90 Sharpe | 6/90 maxDD |")
    print("|---|---|---|---|---|---|---|---|")
    for x in summary["rows"]:
        c, s = x.get("c240", {}), x.get("s690", {})
        print(f"| {x['name']} | {f(c.get('cagr_pct'))}% | {f(c.get('sharpe'))} | {f(x['oos']['annualized_return_pct'])}% | {f(x['oos']['sharpe'])} | {f(s.get('cagr_pct'))}% | {f(s.get('sharpe'))} | {f(s.get('max_dd_pct'),1)}% |")
    print("\n### The two asymmetries (3/60)\n\n| Candidate | base CAGR / Sharpe | T-bill zeroed on cash days | T-bill on cash, %/yr | clustered slippage |")
    print("|---|---|---|---|---|")
    for x in summary["rows"]:
        a = x.get("adjusted")
        if a:
            print(f"| {x['name']} | {f(a['base']['cagr_pct'])}% / {f(a['base']['sharpe'])} | {f(a['tbill_zeroed_on_cash']['cagr_pct'])}% / {f(a['tbill_zeroed_on_cash']['sharpe'])} | {f(a['tbill_on_cash_days_pct_annual'])} | {f(a['clustered_slippage']['cagr_pct'])}% / {f(a['clustered_slippage']['sharpe'])} |")
    print("\n### Target decided at the close of the named dates (re-entry check)\n")
    for x in summary["rows"]:
        fc = x.get("fire_check")
        if fc:
            print(f"- **{x['name']}**: " + "; ".join(f"{r['date']}: in effect {r['position_in_effect']:g}x → target {r['target_decided_at_close']:g}x" for r in fc if r["target_decided_at_close"] is not None))


if __name__ == "__main__":
    main()
