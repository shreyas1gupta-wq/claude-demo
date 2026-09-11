"""Score candidate plateau points for composite_dual_engine: dev_1990 metrics + the harness's own
plateau measure (G6) + the gate-relevant era/stress numbers. DEV window only."""
from __future__ import annotations
import importlib.util, json, sys, time
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE))
import engine as E  # noqa: E402
import dev_harness as H  # noqa: E402

spec = importlib.util.spec_from_file_location("cde", HERE / "signals" / "composite_dual_engine.py")
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

COST, FIN = 3.0, 60.0
df = E.load_market(end="2012-06-30")
assert df.index[-1] <= pd.Timestamp("2012-06-30")

CANDS = json.loads(Path(sys.argv[1]).read_text()) if Path(sys.argv[1]).exists() else json.loads(sys.argv[1])
rows = []
for name, p in CANDS.items():
    t0 = time.time()
    lev = M.signal(df, **p).reindex(df.index)
    m = E.run(df, lev, cost_bps=COST, financing_spread_bps=FIN, start="1990-01-01", end="2012-06-30").metrics()
    st = H.run_stress(df, lev, COST, FIN)
    pl = H.plateau(M, df, p, COST, FIN, "dev_1990")
    bad = [(x["param"], x["step"], x["value"], None if x["sharpe"] is None else round(x["sharpe"], 3))
           for x in pl["rows"] if not x["within_tol"]]
    print(f"{name} {p}")
    print(f"   Sh {m['sharpe']:.4f} CAGR {m['annualized_return_pct']:.2f}% DD {m['max_drawdown_pct']:.2f}% "
          f"worstM {m['worst_month_pct']:.2f}% chg/yr {m['position_changes_per_year']:.2f} cash {m['pct_days_cash']:.1f}% "
          f"levInv {m['avg_leverage_when_invested']:.2f} up {m['up_capture_pct']:.1f} dn {m['down_capture_pct']:.1f}")
    print(f"   00-02 {st['2000_02_bear']['model_total_pct']:+.1f}% GFC {st['2007_09_gfc']['model_total_pct']:+.1f}% "
          f"09rec {st['2009_recovery']['model_total_pct']:+.1f}% 2011 {st['2011_debt']['model_total_pct']:+.1f}% "
          f"| PLATEAU {pl['share_within_25pct']:.3f} of {pl['n_perturbations']}  ({time.time()-t0:.0f}s)")
    print(f"   outside tol: {bad}")
    rows.append(dict(name=name, **p, sharpe=m["sharpe"], cagr=m["annualized_return_pct"],
                     maxdd=m["max_drawdown_pct"], chg_yr=m["position_changes_per_year"],
                     cash=m["pct_days_cash"], plateau=pl["share_within_25pct"]))
pd.DataFrame(rows).to_csv(HERE / "dev_results" / f"{sys.argv[2] if len(sys.argv) > 2 else 'composite_dual_engine_pick'}.csv",
                          index=False, float_format="%.4f")
