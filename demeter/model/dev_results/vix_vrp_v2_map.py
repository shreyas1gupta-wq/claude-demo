"""Round-3 map for the VRP-gated ELEVATED 1x floor: threshold x gate-form matrices (DEV only, 3/60).
Reuses signal_gen from vix_vrp_v2_ablate.py. Prints Sharpe / maxDD / chg-yr / 2000-02 bear / GFC matrices."""
import sys, importlib.util
from pathlib import Path
import numpy as np, pandas as pd
HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import engine as E
import dev_harness as H
spec = importlib.util.spec_from_file_location("abl", HERE / "dev_results" / "vix_vrp_v2_ablate.py")
abl = importlib.util.module_from_spec(spec); spec.loader.exec_module(abl)
df = abl.df

modes = {"raw": dict(elev_mode="raw"), "hold3": dict(elev_mode="hold", elev_hold=3), "hold5": dict(elev_mode="hold", elev_hold=5),
         "hold10": dict(elev_mode="hold", elev_hold=10), "smooth10": dict(elev_mode="smooth", elev_smooth=10), "hyst03": dict(elev_mode="hyst", elev_band=0.03)}
ths = [0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13]
extra = dict(rv_win=int(sys.argv[1])) if len(sys.argv) > 1 else {}
mats = {k: pd.DataFrame(index=ths, columns=list(modes), dtype=float) for k in ("sharpe", "maxdd", "chg", "bear", "gfc", "cash")}
for a in ths:
    for mname, mk in modes.items():
        lev = abl.signal_gen(df, lev_elev=1.0, vrp_elev_min=a, **mk, **extra).reindex(df.index)
        m = E.run(df, lev, cost_bps=3.0, financing_spread_bps=60.0, start="1990-01-01", end="2012-06-30").metrics()
        st = H.run_stress(df, lev, 3.0, 60.0)
        mats["sharpe"].loc[a, mname] = m["sharpe"]; mats["maxdd"].loc[a, mname] = m["max_drawdown_pct"]
        mats["chg"].loc[a, mname] = m["position_changes_per_year"]; mats["cash"].loc[a, mname] = m["pct_days_cash"]
        mats["bear"].loc[a, mname] = st["2000_02_bear"]["model_total_pct"]; mats["gfc"].loc[a, mname] = st["2007_09_gfc"]["model_total_pct"]
print(f"extra params: {extra}  (original vix_vrp: Sharpe 0.608, maxDD -19.8, chg 6.0, bear +15.1, gfc -15.7)")
for k, m in mats.items():
    print(f"--- {k}")
    print(m.round(3 if k == "sharpe" else 1).to_string())
    if k == "sharpe":
        print("col mean/min:", m.mean().round(3).to_dict(), m.min().round(3).to_dict())
pd.concat(mats, axis=1).to_csv(HERE / "dev_results" / f"vix_vrp_v2_map{'_rv' + str(extra['rv_win']) if extra else ''}.csv", float_format="%.4f")
