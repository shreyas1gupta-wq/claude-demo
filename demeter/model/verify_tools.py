#!/usr/bin/env python3
"""Mechanical verification battery for a frozen candidate (DEV data only). Used by the adversarial verifiers.

  python verify_tools.py signals/<name>.py            -> prints + writes dev_results/<name>_VERIFY.json

Checks
  1. causality:   lookahead_check at 12 fixed DEV cut-offs (beyond the harness's 5); NaN-mismatch count; max abs diff
  2. lag test:    dev_1990 Sharpe of the signal delayed by one and two extra sessions — a rule whose edge vanishes with a
                  one-day delay depends on same-close information (or is a very fast timing rule); report, do not judge
  3. grid audit:  from dev_results/<name>_grid.csv — frozen row's rank in the grid, best-in-grid Sharpe, share of the
                  grid that would pass G2-G4, and the one-step neighbourhood (combos differing in exactly one parameter
                  by one grid step) min/max Sharpe — peak vs plateau, mechanically
  4. constants:   module-level UPPER_CASE numeric constants in the signal file (declared "structural" — the verifier
                  decides whether any were in fact tuned on DEV by reading the design note)
  5. sub-samples: dev_1990 split in halves and thirds, Sharpe per piece (from the frozen signal)
  6. turnover:    where the position changes cluster (share of changes in the top-decile-vol months)
"""
from __future__ import annotations
import importlib.util, json, re, sys
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402

DEV_END = "2012-06-30"
CUTOFFS = ("1992-03-31", "1994-09-30", "1997-02-28", "1998-08-31", "1999-12-31", "2001-09-28", "2002-10-09",
           "2004-05-28", "2006-06-30", "2008-10-10", "2009-03-09", "2011-08-08")


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod


def sharpe_dev(df, lev, start="1990-01-01", end=DEV_END, cost=3.0, fin=60.0):
    r = E.run(df, lev, cost_bps=cost, financing_spread_bps=fin, start=start, end=end)
    m = r.metrics()
    return {"sharpe": m.get("sharpe"), "cagr_pct": m["annualized_return_pct"], "max_dd_pct": m["max_drawdown_pct"],
            "changes_per_year": m["position_changes_per_year"]}


def grid_audit(stem: str, params: dict):
    p = HERE / "dev_results" / f"{stem}_grid.csv"
    if not p.exists():
        return {"error": f"no {p.name}"}
    g = pd.read_csv(p)
    if "dev_1990_sharpe" not in g:
        return {"error": "grid has no dev_1990_sharpe column"}
    pk = [k for k in params if k in g.columns]
    g = g.dropna(subset=["dev_1990_sharpe"]).copy()
    # frozen row (numeric tolerance)
    mask = np.ones(len(g), dtype=bool)
    for k in pk:
        mask &= np.isclose(g[k].astype(float).to_numpy(), float(params[k]), rtol=1e-6, atol=1e-9)
    frozen = g[mask]
    out = {"grid_file": p.name, "n_combos": int(len(g)), "params_in_grid": pk,
           "grid_max_sharpe": float(g["dev_1990_sharpe"].max()), "grid_median_sharpe": float(g["dev_1990_sharpe"].median()),
           "share_grid_sharpe_ge_0.425": float((g["dev_1990_sharpe"] >= 0.425).mean())}
    if all(c in g for c in ["dev_1990_maxdd", "min_era_cagr", "worst_era_dd"]):
        ok = (g["dev_1990_sharpe"] >= 0.425) & (g["dev_1990_maxdd"] >= -30) & (g["min_era_cagr"] > 0) & (g["worst_era_dd"] >= -40)
        out["share_grid_passing_G2_G3_G4"] = float(ok.mean())
    if len(frozen):
        fs = float(frozen["dev_1990_sharpe"].iloc[0])
        out["frozen_in_grid"] = True; out["frozen_sharpe"] = fs
        out["frozen_rank"] = int((g["dev_1990_sharpe"] > fs).sum() + 1)
        out["frozen_percentile"] = float((g["dev_1990_sharpe"] <= fs).mean())
        # one-step neighbourhood
        neigh = []
        for k in pk:
            vals = sorted(g[k].dropna().unique())
            v = float(params[k])
            idx = int(np.argmin([abs(x - v) for x in vals]))
            for j in (idx - 1, idx + 1):
                if 0 <= j < len(vals):
                    m2 = mask.copy()
                    # replace k's condition with the neighbour value
                    m2 = np.ones(len(g), dtype=bool)
                    for kk in pk:
                        target = vals[j] if kk == k else float(params[kk])
                        m2 &= np.isclose(g[kk].astype(float).to_numpy(), target, rtol=1e-6, atol=1e-9)
                    row = g[m2]
                    if len(row):
                        neigh.append({"param": k, "value": float(vals[j]), "sharpe": float(row["dev_1990_sharpe"].iloc[0]),
                                      "max_dd": float(row["dev_1990_maxdd"].iloc[0]) if "dev_1990_maxdd" in row else None})
        if neigh:
            s = [n["sharpe"] for n in neigh]
            out["neighbourhood"] = {"n": len(neigh), "min_sharpe": min(s), "max_sharpe": max(s),
                                    "share_within_25pct_of_frozen": float(np.mean([abs(x - fs) <= 0.25 * abs(fs) for x in s])), "rows": neigh}
    else:
        out["frozen_in_grid"] = False
        out["note"] = "frozen parameter set not found in the final grid file (designer may have frozen from a different grid or a manual run)"
    return out


def constants(path: Path):
    src = path.read_text(encoding="utf-8", errors="replace")
    rows = []
    # single-name AND multi-target tuple assignments (A, B = 1, 2) — the verifiers found the single-name-only regex
    # missed 15 of 16 constants in one file
    for m in re.finditer(r"^([A-Z][A-Z0-9_]*(?:\s*,\s*[A-Z][A-Z0-9_]*)*)\s*=\s*(.+?)\s*(#.*)?$", src, flags=re.M):
        names = [n.strip() for n in m.group(1).split(",")]
        vals = [v.strip() for v in m.group(2).split(",")] if len(names) > 1 else [m.group(2).strip()]
        for i, name in enumerate(names):
            if name in ("NAME", "FAMILY", "HYPOTHESIS", "DEFAULT_PARAMS"):
                continue
            rows.append({"name": name, "value": (vals[i] if i < len(vals) else m.group(2).strip())[:60]})
    return rows


def main():
    path = Path(sys.argv[1]).resolve(); stem = path.stem
    mod = load_module(path); params = dict(mod.DEFAULT_PARAMS)
    df = E.load_market(end=DEV_END)
    lev = mod.signal(df, **params).reindex(df.index)
    out = {"name": stem, "params": params}
    out["causality_12_cutoffs"] = E.lookahead_check(mod.signal, df.loc["1985-01-01":], params, cutoffs=CUTOFFS)
    base = sharpe_dev(df, lev)
    out["lag_test_dev_1990"] = {"base": base, "lag1": sharpe_dev(df, lev.shift(1)), "lag2": sharpe_dev(df, lev.shift(2))}
    out["grid_audit"] = grid_audit(stem, params)
    out["module_constants"] = constants(path)
    halves = [("1990-01-01", "2001-03-31"), ("2001-04-01", DEV_END)]
    thirds = [("1990-01-01", "1997-06-30"), ("1997-07-01", "2004-12-31"), ("2005-01-01", DEV_END)]
    out["subsamples"] = {"halves": [dict(start=s, end=e, **sharpe_dev(df, lev, s, e)) for s, e in halves],
                         "thirds": [dict(start=s, end=e, **sharpe_dev(df, lev, s, e)) for s, e in thirds]}
    l90 = lev.loc["1990-01-01":DEV_END]
    ch = l90.diff().fillna(0).ne(0)
    rv = (df["spx_ret"].rolling(21).std() * np.sqrt(252)).loc[l90.index]
    hi = rv >= rv.quantile(0.9)
    out["turnover_clustering"] = {"n_changes": int(ch.sum()), "share_of_changes_in_top_decile_vol_days": float(ch[hi].sum() / max(ch.sum(), 1)),
                                  "share_of_days_top_decile_vol": 0.10}
    (HERE / "dev_results" / f"{stem}_VERIFY.json").write_text(json.dumps(out, indent=1, default=lambda o: None if isinstance(o, float) and np.isnan(o) else (o.item() if hasattr(o, "item") else str(o))))
    c = out["causality_12_cutoffs"]; lt = out["lag_test_dev_1990"]; ga = out["grid_audit"]
    print(f"{stem}: causality ok={c['ok']} max_abs_diff={c['max_abs_diff']:.2e} nan_mismatches={sum(d['nan_mismatches'] for d in c['details'])}")
    print(f"  lag test dev_1990 Sharpe: base {lt['base']['sharpe']:.3f} | lag1 {lt['lag1']['sharpe']:.3f} | lag2 {lt['lag2']['sharpe']:.3f}")
    if "error" not in ga:
        print(f"  grid: n={ga['n_combos']} max Sharpe {ga['grid_max_sharpe']:.3f} median {ga['grid_median_sharpe']:.3f} share>=0.425 {ga['share_grid_sharpe_ge_0.425']:.0%}"
              + (f" share passing G2-G4 {ga['share_grid_passing_G2_G3_G4']:.0%}" if 'share_grid_passing_G2_G3_G4' in ga else ""))
        if ga.get("frozen_in_grid"):
            n = ga.get("neighbourhood", {})
            print(f"  frozen Sharpe {ga['frozen_sharpe']:.3f} rank {ga['frozen_rank']}/{ga['n_combos']} (pctile {ga['frozen_percentile']:.0%});"
                  + (f" neighbourhood {n['n']} combos Sharpe {n['min_sharpe']:.3f}..{n['max_sharpe']:.3f}, {n['share_within_25pct_of_frozen']:.0%} within 25%" if n else ""))
        else:
            print("  frozen point NOT in final grid file: " + ga.get("note", ""))
    else:
        print("  grid:", ga["error"])
    print("  constants:", ", ".join(f"{r['name']}={r['value']}" for r in out["module_constants"]))
    print("  halves:", [round(h["sharpe"], 3) for h in out["subsamples"]["halves"]], "thirds:", [round(h["sharpe"], 3) for h in out["subsamples"]["thirds"]])
    print(f"  turnover: {out['turnover_clustering']['n_changes']} changes, {out['turnover_clustering']['share_of_changes_in_top_decile_vol_days']:.0%} in top-decile-vol days")


if __name__ == "__main__":
    main()
