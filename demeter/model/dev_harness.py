#!/usr/bin/env python3
"""DEVELOPMENT-ONLY evaluation harness for dual-engine signals.

The market data is HARD-TRUNCATED at DEV_END (2012-06-30) before the signal function is called, so nothing
after that date can influence a design decision and the out-of-sample window is structurally invisible.
Use this (and only this) while designing or tuning a candidate.  evaluate.py is the single out-of-sample
look and is run by the coordinator once per frozen candidate.

Usage
  python dev_harness.py signals/<name>.py [--cost-bps 3 --fin-bps 60] [--tag label]
                        [--grid grid.json] [--max-combos 3000] [--params '{"k": v}']
Outputs
  dev_results/<stem>[_<tag>].json      full metric set (windows, eras, stress episodes, event ladders, plateau)
  dev_results/<stem>[_<tag>]_grid.csv  one row per grid combination (when --grid is given)
"""
from __future__ import annotations
import argparse, importlib.util, itertools, json, sys, time
from pathlib import Path
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402

DEV_END = "2012-06-30"
OUT = HERE / "dev_results"
WINDOWS = {"dev_1950": ("1950-01-03", DEV_END), "dev_1990": ("1990-01-01", DEV_END)}
ERAS = {"1950-1969": ("1950-01-03", "1969-12-31"), "1970-1989": ("1970-01-01", "1989-12-31"),
        "1990-1999": ("1990-01-01", "1999-12-31"), "2000-2012H1": ("2000-01-01", DEV_END)}
STRESS = {"1987_crash": ("1987-08-25", "1987-12-31"), "1990_kuwait": ("1990-07-16", "1990-12-31"),
          "1998_ltcm": ("1998-07-17", "1998-12-31"), "2000_02_bear": ("2000-03-24", "2002-10-09"),
          "2002_03_recovery": ("2002-10-10", "2003-12-31"), "2007_09_gfc": ("2007-10-09", "2009-03-09"),
          "2009_recovery": ("2009-03-10", "2009-12-31"), "2010_flash": ("2010-04-23", "2010-07-30"),
          "2011_debt": ("2011-07-22", "2011-12-30")}
# Dated lows / shocks in the development sample; the ladder prints the leverage path around each.
EVENTS = {"1987-10-19": "Black Monday", "1998-08-31": "LTCM low", "1998-10-08": "LTCM 2nd low",
          "2001-09-21": "9/11 low", "2002-07-23": "Jul-02 low", "2002-10-09": "bear low",
          "2008-10-10": "Lehman capitulation", "2008-10-27": "Oct-08 low", "2008-11-20": "Nov-08 low",
          "2009-03-09": "GFC low", "2010-07-02": "2010 low", "2011-08-08": "US downgrade", "2011-10-03": "2011 low"}
LOOKAHEAD_CUTOFFS = ("1995-12-29", "2000-06-30", "2005-12-30", "2008-06-30", "2010-12-31")


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for attr in ["NAME", "FAMILY", "HYPOTHESIS", "DEFAULT_PARAMS", "signal"]:
        if not hasattr(mod, attr):
            raise SystemExit(f"{path} lacks required attribute {attr}")
    return mod


def clean(o):
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if (np.isnan(o) or np.isinf(o)) else float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, pd.Timestamp):
        return o.strftime("%Y-%m-%d")
    return o


def pick(mt: dict) -> dict:
    keys = ["annualized_return_pct", "sharpe", "sortino", "calmar", "max_drawdown_pct", "max_drawdown_daily_pct",
            "annualized_std_dev", "worst_month_pct", "pct_positive_months", "up_capture_pct", "down_capture_pct",
            "beta_to_spy", "pct_days_cash", "avg_leverage", "avg_leverage_when_invested", "position_changes_per_year",
            "n_position_changes", "avg_invested_spell_days", "total_cost_drag_pct_annual",
            "spy_annualized_return_pct", "spy_sharpe", "spy_max_drawdown_pct", "n_months", "start_date", "end_date"]
    return {k: mt.get(k) for k in keys}


def run_windows(df, lev, cost, fin):
    out = {}
    for k, (s, e) in WINDOWS.items():
        r = E.run(df, lev, cost_bps=cost, financing_spread_bps=fin, start=s, end=e)
        out[k] = pick(r.metrics()) if len(r.daily) > 60 else None
    return out


def run_eras(df, lev, cost, fin):
    out = {}
    for k, (s, e) in ERAS.items():
        r = E.run(df, lev, cost_bps=cost, financing_spread_bps=fin, start=s, end=e)
        if len(r.daily) > 60:
            m = r.metrics()
            out[k] = {"cagr_pct": m["annualized_return_pct"], "spy_cagr_pct": m["spy_annualized_return_pct"],
                      "sharpe": m.get("sharpe"), "spy_sharpe": m.get("spy_sharpe"), "max_dd_pct": m["max_drawdown_pct"],
                      "spy_max_dd_pct": m["spy_max_drawdown_pct"], "pct_days_cash": m["pct_days_cash"],
                      "changes_per_year": m["position_changes_per_year"], "worst_month_pct": m["worst_month_pct"]}
    return out


def run_stress(df, lev, cost, fin):
    out = {}
    for k, (s, e) in STRESS.items():
        r = E.run(df, lev, cost_bps=cost, financing_spread_bps=fin, start=s, end=e)
        d = r.daily
        if len(d) < 10:
            continue
        eq = (1 + d["ret"]).cumprod(); eqm = (1 + d["mkt_tr_ret"]).cumprod()
        out[k] = {"model_total_pct": (eq.iloc[-1] - 1) * 100, "spy_total_pct": (eqm.iloc[-1] - 1) * 100,
                  "model_max_dd_pct": E.drawdown(eq).min() * 100, "spy_max_dd_pct": E.drawdown(eqm).min() * 100,
                  "avg_leverage": d["lev"].mean(), "pct_days_cash": (d["lev"] == 0).mean() * 100,
                  "pct_days_3x": (d["lev"] >= 2.5).mean() * 100, "n_changes": int((d["lev"].diff().fillna(0) != 0).sum()),
                  "n_days": int(len(d))}
    return out


def event_ladders(df, lev, before=3, after=6):
    """Leverage path around dated development-sample lows (lev = target decided at that close)."""
    out = {}
    idx = df.index
    for d, label in EVENTS.items():
        t = pd.Timestamp(d)
        if t not in idx:
            continue
        i = idx.get_loc(t)
        sl = slice(max(0, i - before), min(len(idx), i + after + 1))
        rows = [{"date": str(x.date()), "spx_ret_pct": round(float(df["spx_ret"].iloc[j]) * 100, 2),
                 "vix": (None if pd.isna(df["vix_close"].iloc[j]) else round(float(df["vix_close"].iloc[j]), 1)),
                 "lev_target": (None if pd.isna(lev.iloc[j]) else float(lev.iloc[j]))}
                for j, x in zip(range(sl.start, sl.stop), idx[sl])]
        out[d] = {"label": label, "path": rows}
    return out


def spurious_reentry_census(df, lev):
    """Count entries to >=2x during the two grinding development bears and what they earned over the next 10 sessions."""
    out = {}
    x = df["spx_tr_ret"] - df["rf_daily"]
    for k in ("2000_02_bear", "2007_09_gfc"):
        s, e = STRESS[k]
        l = lev.loc[s:e].fillna(0)
        entries = l[(l >= 2.0) & (l.shift(1).fillna(0) < 2.0)]
        fwd = []
        for t in entries.index:
            i = df.index.get_loc(t)
            f = x.iloc[i + 1:i + 11]
            fwd.append(float(((1 + f).prod() - 1) * 100))
        out[k] = {"n_entries_to_2x_plus": int(len(entries)), "dates": [str(t.date()) for t in entries.index][:40],
                  "mean_fwd10_excess_pct": (float(np.mean(fwd)) if fwd else None),
                  "share_fwd10_negative": (float(np.mean(np.array(fwd) < 0)) if fwd else None),
                  "pct_days_2x_plus": float((l >= 2.0).mean() * 100)}
    return out


def plateau(mod, df, base, cost, fin, window="dev_1990", tol=0.25):
    """Share of single-parameter +/-15% and +/-30% perturbations whose Sharpe stays within `tol` of base."""
    s, e = WINDOWS[window]
    def sharpe(p):
        try:
            r = E.run(df, mod.signal(df, **p).reindex(df.index), cost_bps=cost, financing_spread_bps=fin, start=s, end=e)
            return r.metrics().get("sharpe")
        except Exception as ex:  # a perturbation that breaks the rule counts as a failure
            return None
    b = sharpe(dict(base))
    rows, held = [], []
    keys = [k for k, v in base.items() if isinstance(v, (int, float)) and not isinstance(v, bool)]
    for k in keys:
        for st in (-0.30, -0.15, 0.15, 0.30):
            p = dict(base); v = base[k] * (1 + st)
            p[k] = int(round(v)) if isinstance(base[k], int) else v
            if p[k] == base[k]:
                continue
            sh = sharpe(p)
            ok = (sh is not None and b is not None and b != 0 and abs(sh - b) <= tol * abs(b))
            held.append(ok)
            rows.append({"param": k, "step": st, "value": p[k], "sharpe": sh, "within_tol": ok})
    return {"window": window, "base_sharpe": b, "n_perturbations": len(rows),
            "share_within_25pct": (float(np.mean(held)) if held else None), "rows": rows}


def grid_search(mod, df, grid: dict, cost, fin, max_combos):
    keys = list(grid)
    combos = list(itertools.product(*[grid[k] for k in keys]))
    if len(combos) > max_combos:
        print(f"grid has {len(combos)} combos > --max-combos {max_combos}; truncating (state this in your report)")
        combos = combos[:max_combos]
    rows = []
    t0 = time.time()
    for i, c in enumerate(combos):
        p = dict(mod.DEFAULT_PARAMS); p.update(dict(zip(keys, c)))
        try:
            lev = mod.signal(df, **p).reindex(df.index)
        except Exception as ex:
            rows.append({**p, "error": repr(ex)}); continue
        row = dict(p)
        for w, (s, e) in WINDOWS.items():
            r = E.run(df, lev, cost_bps=cost, financing_spread_bps=fin, start=s, end=e)
            if len(r.daily) > 60:
                m = r.metrics()
                row[f"{w}_cagr"] = m["annualized_return_pct"]; row[f"{w}_sharpe"] = m.get("sharpe")
                row[f"{w}_maxdd"] = m["max_drawdown_pct"]; row[f"{w}_chg_yr"] = m["position_changes_per_year"]
                row[f"{w}_cash"] = m["pct_days_cash"]; row[f"{w}_worst_m"] = m["worst_month_pct"]
        # worst era drawdown / min era cagr (ruin check)
        eras = run_eras(df, lev, cost, fin)
        row["min_era_cagr"] = min(v["cagr_pct"] for v in eras.values()) if eras else None
        row["worst_era_dd"] = min(v["max_dd_pct"] for v in eras.values()) if eras else None
        rows.append(row)
        if (i + 1) % 50 == 0:
            print(f"  {i + 1}/{len(combos)} combos, {time.time() - t0:.0f}s", flush=True)
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("module")
    ap.add_argument("--cost-bps", type=float, default=3.0)
    ap.add_argument("--fin-bps", type=float, default=60.0)
    ap.add_argument("--tag", default="")
    ap.add_argument("--grid", default="")
    ap.add_argument("--max-combos", type=int, default=3000)
    ap.add_argument("--params", default="", help='JSON dict overriding DEFAULT_PARAMS for this run')
    ap.add_argument("--no-plateau", action="store_true")
    a = ap.parse_args()

    t0 = time.time()
    path = Path(a.module).resolve()
    mod = load_module(path)
    params = dict(mod.DEFAULT_PARAMS)
    if a.params:
        params.update(json.loads(a.params))
    n_tunable = len([k for k, v in params.items() if isinstance(v, (int, float)) and not isinstance(v, bool)])

    df = E.load_market(end=DEV_END)                  # <-- HARD TRUNCATION: nothing after 2012-06-30 exists here
    assert df.index[-1] <= pd.Timestamp(DEV_END)
    lev = mod.signal(df, **params)
    if not isinstance(lev, pd.Series):
        raise SystemExit("signal() must return a pd.Series")
    lev = lev.reindex(df.index)
    if lev.max() > 3.0 + 1e-9 or lev.min() < -1e-9:
        print(f"WARNING: leverage outside [0,3] (min {lev.min()}, max {lev.max()}); engine will clip")

    res = {"name": mod.NAME, "family": mod.FAMILY, "hypothesis": mod.HYPOTHESIS, "module": str(path.relative_to(HERE)),
           "params": params, "n_tunable_params": n_tunable, "dev_end": DEV_END,
           "cost_bps": a.cost_bps, "financing_spread_bps": a.fin_bps,
           "signal_coverage": {"first_nonnull": str(lev.first_valid_index().date()) if lev.notna().any() else None,
                               "pct_nan_1950_1989": float(lev.loc["1950":"1989"].isna().mean() * 100),
                               "pct_cash_1950_1989": float((lev.loc["1950":"1989"].fillna(0) == 0).mean() * 100),
                               "uses_vix": bool(lev.loc["1950":"1989"].fillna(0).eq(0).mean() > 0.99)}}
    res["windows"] = run_windows(df, lev, a.cost_bps, a.fin_bps)
    res["windows_stress_cost_6_90"] = run_windows(df, lev, 6.0, 90.0)
    res["windows_cost_2_40"] = run_windows(df, lev, 2.0, 40.0)
    res["eras"] = run_eras(df, lev, a.cost_bps, a.fin_bps)
    res["stress_episodes"] = run_stress(df, lev, a.cost_bps, a.fin_bps)
    res["event_ladders"] = event_ladders(df, lev)
    res["spurious_reentry_census"] = spurious_reentry_census(df, lev)
    res["lookahead_check"] = E.lookahead_check(mod.signal, df.loc["1985-01-01":], params, cutoffs=LOOKAHEAD_CUTOFFS)
    l90 = lev.loc["1990":].fillna(0)
    res["leverage_distribution_dev_1990"] = {str(k): float(v) for k, v in (l90.round(2).value_counts(normalize=True).sort_index() * 100).items()}
    # reference: SPY buy & hold 1x at zero cost over the same windows
    res["reference_bh_1x"] = {k: pick(E.run(df, E.buy_and_hold(df, 1.0), cost_bps=0.0, start=s, end=e).metrics()) for k, (s, e) in WINDOWS.items()}
    if not a.no_plateau:
        res["plateau_dev_1990"] = plateau(mod, df, params, a.cost_bps, a.fin_bps, "dev_1990")
        res["plateau_dev_1950"] = plateau(mod, df, params, a.cost_bps, a.fin_bps, "dev_1950")
    OUT.mkdir(exist_ok=True)
    stem = path.stem + (f"_{a.tag}" if a.tag else "")
    if a.grid:
        grid = json.loads(Path(a.grid).read_text()) if Path(a.grid).exists() else json.loads(a.grid)
        g = grid_search(mod, df, grid, a.cost_bps, a.fin_bps, a.max_combos)
        gp = OUT / f"{stem}_grid.csv"
        g.to_csv(gp, index=False, float_format="%.4f")
        res["grid_file"] = str(gp.relative_to(HERE)); res["grid_n"] = int(len(g))
        if "dev_1990_sharpe" in g:
            print(g.sort_values("dev_1990_sharpe", ascending=False).head(15).to_string(index=False))
    res["runtime_sec"] = time.time() - t0
    (OUT / f"{stem}.json").write_text(json.dumps(clean(res), indent=1))

    w9, w5 = res["windows"]["dev_1990"], res["windows"]["dev_1950"]
    pl = res.get("plateau_dev_1990", {})
    print(f"{mod.NAME} [DEV ONLY, cost {a.cost_bps}bp/fin {a.fin_bps}bp]  n_params={n_tunable}")
    if w9:
        print(f"  1990-2012H1: CAGR {w9['annualized_return_pct']:.2f}% Sharpe {w9['sharpe']:.2f} maxDD {w9['max_drawdown_pct']:.1f}% "
              f"worstM {w9['worst_month_pct']:.1f}% cash {w9['pct_days_cash']:.0f}% chg/yr {w9['position_changes_per_year']:.1f} "
              f"| SPY CAGR {w9['spy_annualized_return_pct']:.2f}% Sharpe {w9['spy_sharpe']:.2f} DD {w9['spy_max_drawdown_pct']:.1f}%")
    if w5:
        print(f"  1950-2012H1: CAGR {w5['annualized_return_pct']:.2f}% Sharpe {w5['sharpe']:.2f} maxDD {w5['max_drawdown_pct']:.1f}% "
              f"cash {w5['pct_days_cash']:.0f}% chg/yr {w5['position_changes_per_year']:.1f} | SPY Sharpe {w5['spy_sharpe']:.2f}")
    for k, v in res["eras"].items():
        print(f"  era {k}: CAGR {v['cagr_pct']:.2f}% (SPY {v['spy_cagr_pct']:.2f}%) Sharpe {v['sharpe']:.2f} maxDD {v['max_dd_pct']:.1f}% chg/yr {v['changes_per_year']:.1f}")
    for k, v in res["stress_episodes"].items():
        print(f"  stress {k}: model {v['model_total_pct']:+.1f}% (SPY {v['spy_total_pct']:+.1f}%) DD {v['model_max_dd_pct']:.1f}% avgL {v['avg_leverage']:.2f} cash {v['pct_days_cash']:.0f}% 3x {v['pct_days_3x']:.0f}%")
    sc = res["spurious_reentry_census"]
    for k, v in sc.items():
        print(f"  reentry census {k}: entries to >=2x {v['n_entries_to_2x_plus']}, mean fwd10 {v['mean_fwd10_excess_pct']}, share negative {v['share_fwd10_negative']}")
    if pl:
        print(f"  plateau dev_1990: {pl['share_within_25pct']:.0%} of {pl['n_perturbations']} perturbations within 25% of base Sharpe {pl['base_sharpe']:.2f}")
    print(f"  lookahead ok={res['lookahead_check']['ok']}  -> dev_results/{stem}.json  ({res['runtime_sec']:.0f}s)")


if __name__ == "__main__":
    main()
