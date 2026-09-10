"""Scratch evaluator for volmanaged (DEV ONLY). Every evaluated variant is appended to
dev_results/volmanaged_scratch_log.csv so the iteration count is exact.
Usage: python dev_results/volmanaged_scratch_eval.py <variants.json> [--tag label]
variants.json = list of dicts: {"target_vol":..,"hl":..,"band":..,"shock_z":..,"shock_days":..,
                                "power":1|2,"discrete":0|1,"weekly":0|1}
Costs: headline 3/60; also 0/0 (gross) and 6/90 for the Sharpe-gain question.
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path
import numpy as np, pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import engine as E                       # noqa: E402
import importlib.util
spec = importlib.util.spec_from_file_location("volmanaged", HERE / "signals" / "volmanaged.py")
VM = importlib.util.module_from_spec(spec); spec.loader.exec_module(VM)

DEV_END = "2012-06-30"
WIN = {"d90": ("1990-01-01", DEV_END), "d50": ("1950-01-03", DEV_END)}
ERAS = {"e5069": ("1950-01-03", "1969-12-31"), "e7089": ("1970-01-01", "1989-12-31"),
        "e9099": ("1990-01-01", "1999-12-31"), "e0012": ("2000-01-01", DEV_END)}
LOG = HERE / "dev_results" / "volmanaged_scratch_log.csv"


def evaluate(df, v: dict) -> dict:
    # v3 variant keys: target_vol, hl, long_mult, band_up, band_dn (+ structural: power, discrete, weekly, est, shock_z, shock_days)
    # legacy keys from batches 1-2 ("band", "bdr") are mapped: band_up = band, band_dn = band * bdr
    band_up = v.get("band_up", v.get("band", 0.5)); band_dn = v.get("band_dn", band_up * float(v.get("bdr", 1.0)))
    lev = VM._core(df, v["target_vol"], v["hl"], v.get("long_mult", 4.0), band_up, band_dn,
                   power=int(v.get("power", 2)), discrete=bool(v.get("discrete", 0)), weekly=bool(v.get("weekly", 0)),
                   est=v.get("est", "max2"), shock_z=float(v.get("shock_z", 0)), shock_days=int(v.get("shock_days", 0))).reindex(df.index)
    row = dict(v)
    for tag, (c, f) in {"": (3.0, 60.0), "_g": (0.0, 0.0), "_s": (6.0, 90.0)}.items():
        for w, (s, e) in WIN.items():
            m = E.run(df, lev, cost_bps=c, financing_spread_bps=f, start=s, end=e).metrics()
            row[f"{w}{tag}_sh"] = m.get("sharpe"); row[f"{w}{tag}_cagr"] = m["annualized_return_pct"]
            row[f"{w}{tag}_dd"] = m["max_drawdown_pct"]
            if tag == "":
                row[f"{w}_chg"] = m["position_changes_per_year"]; row[f"{w}_cash"] = m["pct_days_cash"]
                row[f"{w}_avgL"] = m["avg_leverage"]; row[f"{w}_worstM"] = m["worst_month_pct"]
                row[f"{w}_upcap"] = m.get("up_capture_pct"); row[f"{w}_dncap"] = m.get("down_capture_pct")
    eras = []
    for k, (s, e) in ERAS.items():
        m = E.run(df, lev, cost_bps=3.0, financing_spread_bps=60.0, start=s, end=e).metrics()
        row[f"{k}_cagr"] = m["annualized_return_pct"]; row[f"{k}_dd"] = m["max_drawdown_pct"]; row[f"{k}_sh"] = m.get("sharpe")
        eras.append((m["annualized_return_pct"], m["max_drawdown_pct"]))
    row["min_era_cagr"] = min(x[0] for x in eras); row["worst_era_dd"] = min(x[1] for x in eras)
    return row


def main():
    vpath = sys.argv[1]
    tag = sys.argv[sys.argv.index("--tag") + 1] if "--tag" in sys.argv else Path(vpath).stem
    variants = json.loads(Path(vpath).read_text())
    df = E.load_market(end=DEV_END)
    assert df.index[-1] <= pd.Timestamp(DEV_END)
    rows, t0 = [], time.time()
    for i, v in enumerate(variants):
        r = evaluate(df, v); r["tag"] = tag; r["ts"] = time.strftime("%Y-%m-%d %H:%M:%S")
        rows.append(r)
        print(f"[{i+1}/{len(variants)}] {json.dumps(v)} -> d90 sh {r['d90_sh']:.3f} cagr {r['d90_cagr']:.2f} dd {r['d90_dd']:.1f} "
              f"chg {r['d90_chg']:.1f} cash {r['d90_cash']:.0f}% avgL {r['d90_avgL']:.2f} | d50 sh {r['d50_sh']:.3f} dd {r['d50_dd']:.1f} "
              f"chg {r['d50_chg']:.1f} | gross d90 {r['d90_g_sh']:.3f} 6/90 {r['d90_s_sh']:.3f} | minEraCAGR {r['min_era_cagr']:.2f} worstEraDD {r['worst_era_dd']:.1f}",
              flush=True)
    out = pd.DataFrame(rows)
    out.to_csv(LOG, mode="a", header=not LOG.exists(), index=False, float_format="%.4f")
    print(f"appended {len(out)} rows to {LOG.name} in {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
