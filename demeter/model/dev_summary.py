#!/usr/bin/env python3
"""Pass-2 development-window summary table: every candidate's DEV numbers, gate results and iteration count.
Reads dev_results/<name>.json (+ <name>_RETURN.json when present). Writes dev_results/PASS2_DEV_TABLE.md and prints it.
Usage: python dev_summary.py [name ...]   (default: the pass-2 panel + references)"""
from __future__ import annotations
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from gate_check import check  # noqa: E402

DEV = HERE / "dev_results"
DEFAULT = [("final_model_fewtrades", "pass-1 incumbent"), ("baseline_volregime", "pass-1 reference"), ("vix_dissipation", "pass-1 trap"),
           ("vix_vrp", "pass-1 file, never evaluated"), ("crash_exit_dual", "lens 1"), ("dissipation_reentry", "lens 2"),
           ("volmanaged", "lens 3"), ("sticky_tier", "lens 4"), ("vix_vrp_v2", "lens 5"), ("composite_dual_engine", "lens 6")]


def f(v, d=2, pct=False):
    if v is None:
        return "—"
    return f"{v:.{d}f}%" if pct else f"{v:.{d}f}"


def main():
    names = [(n, "") for n in sys.argv[1:]] or DEFAULT
    rows = []
    for n, lens in names:
        p = DEV / f"{n}.json"
        if not p.exists():
            rows.append({"name": n, "lens": lens, "missing": True}); continue
        r = json.loads(p.read_text())
        g = check(str(p))
        ret = json.loads((DEV / f"{n}_RETURN.json").read_text()) if (DEV / f"{n}_RETURN.json").exists() else {}
        w, w5 = r["windows"]["dev_1990"] or {}, r["windows"]["dev_1950"] or {}
        eras = [v for v in (r.get("eras") or {}).values() if v["pct_days_cash"] <= 99]
        st = r.get("stress_episodes", {})
        rows.append({"name": n, "lens": lens, "n_tun": r.get("n_tunable_params"),
                     "sh": w.get("sharpe"), "cagr": w.get("annualized_return_pct"), "dd": w.get("max_drawdown_pct"),
                     "chg": w.get("position_changes_per_year"), "cash": w.get("pct_days_cash"), "linv": w.get("avg_leverage_when_invested"),
                     "upc": w.get("up_capture_pct"), "dnc": w.get("down_capture_pct"),
                     "sh50": w5.get("sharpe"), "uses_vix": r["signal_coverage"]["uses_vix"],
                     "era_min_cagr": min((e["cagr_pct"] for e in eras), default=None), "era_worst_dd": min((e["max_dd_pct"] for e in eras), default=None),
                     "bear0002": (st.get("2000_02_bear") or {}).get("model_total_pct"), "gfc": (st.get("2007_09_gfc") or {}).get("model_total_pct"),
                     "rec09": (st.get("2009_recovery") or {}).get("model_total_pct"),
                     "plateau": (r.get("plateau_dev_1990") or {}).get("share_within_25pct"),
                     "gates": g["all_pass"], "failed": [k.split("_")[0] for k, v in g["gates"].items() if not v["pass"]],
                     "iters": ret.get("n_iterations"), "s690": ((r.get("windows_stress_cost_6_90") or {}).get("dev_1990") or {}).get("sharpe")})
    lines = ["# Pass 2 — development window (1990-01..2012-06 unless noted), 3 bp / 60 bp", "",
             "| Candidate | Lens | Tunables | DEV Sharpe | DEV CAGR | DEV maxDD | Chg/yr | Cash % | Avg lev invested | Up-capt | Down-capt | 1950–2012 Sharpe | Worst era DD | 2000-02 | GFC | 2009 rec. | Plateau | 6/90 Sharpe | Gates | DEV param sets |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for x in rows:
        if x.get("missing"):
            lines.append(f"| {x['name']} | {x['lens']} | — | not run | | | | | | | | | | | | | | | — | — |"); continue
        sh50 = f(x['sh50']) + (" (cash pre-1990)" if x["uses_vix"] else "")
        gates = "PASS" if x["gates"] else "FAIL " + "/".join(x["failed"])
        lines.append(f"| {x['name']} | {x['lens']} | {x['n_tun']} | {f(x['sh'])} | {f(x['cagr'],2,True)} | {f(x['dd'],1,True)} | {f(x['chg'],1)} | {f(x['cash'],0)} | {f(x['linv'])} | {f(x['upc'],0,True)} | {f(x['dnc'],0,True)} | {sh50} | {f(x['era_worst_dd'],1,True)} | {f(x['bear0002'],1,True)} | {f(x['gfc'],1,True)} | {f(x['rec09'],1,True)} | {f((x['plateau'] or 0)*100 if x['plateau'] is not None else None,0,True)} | {f(x['s690'])} | {gates} | {x['iters'] if x['iters'] is not None else '—'} |")
    lines += ["", "SPY buy-and-hold: dev_1990 Sharpe 0.39 (CAGR 8.34%, maxDD −50.8%); 1950–2012 Sharpe 0.47. Gates per PREREG.md; 'DEV param sets' = distinct parameter sets the designer evaluated on the development window (self-reported)."]
    out = "\n".join(lines)
    (DEV / "PASS2_DEV_TABLE.md").write_text(out, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
