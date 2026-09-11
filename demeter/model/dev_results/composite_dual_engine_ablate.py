"""Ablations A-G for composite_dual_engine on the DEVELOPMENT window only (data hard-truncated at 2012-06-30).

Each ablation flips module-level structural switches / constants and re-runs the engine directly
(E.run on the truncated frame), exactly the columns the design note pre-registered.

Usage:
  python dev_results/composite_dual_engine_ablate.py '{"v_calm":15.5,...}' <outstem>
"""
from __future__ import annotations
import importlib.util, json, sys, time
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402
import dev_harness as H  # noqa: E402  (module import only; main() does not run)

spec = importlib.util.spec_from_file_location("cde", HERE / "signals" / "composite_dual_engine.py")
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

COST, FIN = 3.0, 60.0
params = dict(M.DEFAULT_PARAMS)
if len(sys.argv) > 1 and sys.argv[1] not in ("-", ""):
    params.update(json.loads(sys.argv[1]))
stem = sys.argv[2] if len(sys.argv) > 2 else "composite_dual_engine_ablate"

df = E.load_market(end="2012-06-30")
assert df.index[-1] <= pd.Timestamp("2012-06-30")

ABL = [
    ("A", "tier only (VIX regime 3/1/0, no shock exit, no re-entry, no min-hold)",
     dict(USE_SHOCK=False, USE_REENTRY=False), dict(min_hold=1)),
    ("B", "A + shock exit", dict(USE_SHOCK=True, USE_REENTRY=False), dict(min_hold=1)),
    ("C", "B + dissipation re-entry at 3x (no min-hold)", dict(USE_SHOCK=True, USE_REENTRY=True), dict(min_hold=1)),
    ("D", "C + hysteresis (min_hold) = THE MODEL", dict(USE_SHOCK=True, USE_REENTRY=True), {}),
    ("E", "D with re-entry leverage 2x", dict(USE_SHOCK=True, USE_REENTRY=True, LEV_REB=2.0), {}),
    ("F", "D with re-entry leverage 1x", dict(USE_SHOCK=True, USE_REENTRY=True, LEV_REB=1.0), {}),
    ("G", "D with ELEVATED tier = cash (vix_vrp-like, no 1x band)",
     dict(USE_SHOCK=True, USE_REENTRY=True, LEV_ELEV=0.0), {}),
    # not pre-registered; added to answer the panel's "does 3x-in-calm work at all" question
    ("H", "DIAGNOSTIC (not pre-registered): D with CALM tier = 2x instead of 3x",
     dict(USE_SHOCK=True, USE_REENTRY=True, LEV_CALM=2.0), {}),
    ("I", "DIAGNOSTIC (not pre-registered): D with CALM tier 2x AND re-entry 2x",
     dict(USE_SHOCK=True, USE_REENTRY=True, LEV_CALM=2.0, LEV_REB=2.0), {}),
]

BASE = {k: getattr(M, k) for k in ("USE_SHOCK", "USE_REENTRY", "LEV_REB", "LEV_ELEV", "LEV_CALM")}
rows = []
t0 = time.time()
for tag, desc, switches, pover in ABL:
    for k, v in BASE.items():
        setattr(M, k, v)
    for k, v in switches.items():
        setattr(M, k, v)
    p = dict(params); p.update(pover)
    lev = M.signal(df, **p).reindex(df.index)
    r = E.run(df, lev, cost_bps=COST, financing_spread_bps=FIN, start="1990-01-01", end="2012-06-30")
    m = r.metrics()
    st = H.run_stress(df, lev, COST, FIN)
    cen = H.spurious_reentry_census(df, lev)
    era = H.run_eras(df, lev, COST, FIN)
    n_bear = cen["2000_02_bear"]["n_entries_to_2x_plus"] + cen["2007_09_gfc"]["n_entries_to_2x_plus"]
    negs = []
    for k in ("2000_02_bear", "2007_09_gfc"):
        c = cen[k]
        if c["share_fwd10_negative"] is not None:
            negs.append(c["share_fwd10_negative"] * c["n_entries_to_2x_plus"])
    share_neg = (sum(negs) / n_bear) if n_bear else None
    rows.append(dict(
        abl=tag, desc=desc,
        sharpe=m["sharpe"], cagr=m["annualized_return_pct"], maxdd=m["max_drawdown_pct"],
        worst_m=m["worst_month_pct"], chg_yr=m["position_changes_per_year"], cash_pct=m["pct_days_cash"],
        avg_lev_inv=m["avg_leverage_when_invested"], up_cap=m["up_capture_pct"], dn_cap=m["down_capture_pct"],
        bear_2000_02=st["2000_02_bear"]["model_total_pct"], gfc=st["2007_09_gfc"]["model_total_pct"],
        rec_2009=st["2009_recovery"]["model_total_pct"],
        census_n=n_bear, census_share_neg=share_neg,
        min_era_cagr=min(v["cagr_pct"] for v in era.values() if v["pct_days_cash"] <= 99.0),
        worst_era_dd=min(v["max_dd_pct"] for v in era.values() if v["pct_days_cash"] <= 99.0),
        params=json.dumps(p), switches=json.dumps(switches),
    ))
    print(f"{tag} {desc[:46]:46s} Sh {m['sharpe']:.3f} CAGR {m['annualized_return_pct']:5.2f}% DD {m['max_drawdown_pct']:6.1f}% "
          f"chg/yr {m['position_changes_per_year']:5.2f} cash {m['pct_days_cash']:4.1f}% levInv {m['avg_leverage_when_invested']:.2f} "
          f"up {m['up_capture_pct']:5.1f} | 00-02 {st['2000_02_bear']['model_total_pct']:+6.1f} GFC {st['2007_09_gfc']['model_total_pct']:+6.1f} "
          f"09rec {st['2009_recovery']['model_total_pct']:+6.1f} | census {n_bear} negshare {share_neg}", flush=True)

for k, v in BASE.items():
    setattr(M, k, v)
out = pd.DataFrame(rows)
out.to_csv(HERE / "dev_results" / f"{stem}.csv", index=False, float_format="%.4f")
print(f"-> dev_results/{stem}.csv  ({time.time()-t0:.0f}s)  params={params}")
