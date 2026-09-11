"""Era / exposure diagnostic for grid-B candidates vs volmanaged and SPY: which era fails at higher target_vol, and at what tier."""
import sys
import numpy as np, pandas as pd
sys.path.insert(0, ".")
import engine as E, features as F
import importlib.util
def load(p):
    spec = importlib.util.spec_from_file_location(p.split("/")[-1][:-3], p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
st = load("signals/sticky_tier.py"); vm = load("signals/volmanaged.py")
df = E.load_market(end="2012-06-30")
C = dict(cost_bps=3.0, financing_spread_bps=60.0)
def row(lev, s, e):
    r = E.run(df, lev, start=s, end=e, **C); m = r.metrics(); d = r.daily
    return dict(cagr=m["annualized_return_pct"], spy=m["spy_annualized_return_pct"], sh=m.get("sharpe"), dd=m["max_drawdown_pct"], spydd=m["spy_max_drawdown_pct"],
                avgL=m["avg_leverage"], cash=m["pct_days_cash"], chg=m["position_changes_per_year"], d3=(d["lev"] >= 2.5).mean() * 100, d2=((d["lev"] >= 1.5) & (d["lev"] < 2.5)).mean() * 100)
cands = {"A t.14 h.3 hl20 lm8": dict(target_vol=0.14, h=0.30, hl=20.0, long_mult=8.0, M=10, P=5),
         "B t.16 h.15 hl20 lm8": dict(target_vol=0.16, h=0.15, hl=20.0, long_mult=8.0, M=10, P=5),
         "C t.18 h.15 hl20 lm8": dict(target_vol=0.18, h=0.15, hl=20.0, long_mult=8.0, M=10, P=5),
         "D t.20 h.5 hl20 lm8": dict(target_vol=0.20, h=0.50, hl=20.0, long_mult=8.0, M=10, P=5)}
levs = {k: st.signal(df, **p) for k, p in cands.items()}
levs["volmanaged"] = vm.signal(df); levs["SPY 1x"] = E.buy_and_hold(df, 1.0)
wins = {"dev_1990": ("1990-01-01", "2012-06-30"), "dev_1950": ("1950-01-03", "2012-06-30"), "1950-69": ("1950-01-03", "1969-12-31"), "1970-89": ("1970-01-01", "1989-12-31"),
        "calm 1991-99": ("1991-01-01", "1999-12-31"), "calm 2003-07": ("2003-04-01", "2007-06-30"), "1962": ("1961-12-01", "1962-12-31"), "1987": ("1987-08-25", "1987-12-31"),
        "1973-74": ("1973-01-01", "1974-12-31"), "2008": ("2008-09-01", "2009-03-09"), "2011": ("2011-07-22", "2011-12-30")}
for w, (s, e) in wins.items():
    print(f"\n== {w}")
    rows = pd.DataFrame({k: row(l, s, e) for k, l in levs.items()}).T
    print(rows.round(2).to_string())
