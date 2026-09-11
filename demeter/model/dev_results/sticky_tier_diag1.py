"""Diagnose grid A failure: best-DD corner + monthly level/vol path through 2000-02 and 2007-09 for one param set."""
import sys, json
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, ".")
import engine as E, features as F
import importlib.util
spec = importlib.util.spec_from_file_location("sticky_tier", "signals/sticky_tier.py"); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 40)

g = pd.read_csv("dev_results/sticky_tier_gridA_grid.csv")
cols = ["v_lo", "gap", "h", "hl", "floor", "dev_1990_sharpe", "dev_1990_cagr", "dev_1990_maxdd", "dev_1990_chg_yr", "dev_1990_cash", "dev_1950_sharpe", "worst_era_dd"]
print("BEST dev_1990 maxDD (10):"); print(g.sort_values("dev_1990_maxdd", ascending=False)[cols].head(10).to_string(index=False))

df = E.load_market(end="2012-06-30")
p = dict(v_lo=0.10, gap=0.25, h=0.30, hl=10.0, M=10, P=5)
lev = mod.signal(df, **p)
ew10 = F.ewma_vol(df["spx_ret"], 10, 20); ew80 = F.ewma_vol(df["spx_ret"], 80, 20); rv21 = F.realized_vol(df["spx_ret"], 21)
x = pd.DataFrame({"lev": lev, "ew10": ew10 * 100, "ew80": ew80 * 100, "rv21": rv21 * 100, "spx": df["spx_ret"] * 100})
for s, e in [("2000-01", "2003-03"), ("2007-07", "2009-12")]:
    m = x.loc[s:e].resample("ME").agg(lev=("lev", "mean"), lev_max=("lev", "max"), ew10=("ew10", "mean"), ew80=("ew80", "mean"), rv21=("rv21", "mean"), spx=("spx", lambda r: ((1 + r / 100).prod() - 1) * 100))
    m.index = m.index.strftime("%Y-%m"); print(f"\n{p}  {s}..{e}"); print(m.round(1).to_string())
# vol distribution by era (what boundaries mean in exposure terms)
for s, e in [("1950", "1969"), ("1970", "1989"), ("1990", "1999"), ("2000", "2012")]:
    v = ew10.loc[s:e].dropna() * 100
    print(f"EWMA10 vol {s}-{e}: pct<8 {np.mean(v<8):.2f} <10 {np.mean(v<10):.2f} <12 {np.mean(v<12):.2f} <14 {np.mean(v<14):.2f} <16 {np.mean(v<16):.2f} <20 {np.mean(v<20):.2f} <25 {np.mean(v<25):.2f}")
