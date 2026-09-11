"""v2 vs original on DEV: what the VRP-gated ELEVATED 1x leg earned/cost by period, gate-open share, turnover source."""
import sys, importlib.util
from pathlib import Path
import numpy as np, pandas as pd
HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import engine as E, features as F

def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / "signals" / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

DEV_END = "2012-06-30"
df = E.load_market(end=DEV_END); assert df.index[-1] <= pd.Timestamp(DEV_END)
o, v = load("vix_vrp"), load("vix_vrp_v2")
po, pv = dict(o.DEFAULT_PARAMS), dict(v.DEFAULT_PARAMS)
lo = o.signal(df, **po).reindex(df.index); lv = v.signal(df, **pv).reindex(df.index)
print("v2 params:", pv)
vix = df["vix_close"].ffill(); reg = v.vix_regime(vix, pv["v_calm"], pv["v_panic"], pv["hyst"])
vrp = vix / 100 - F.realized_vol(df["spx_ret"], pv["rv_win"])
d90 = slice("1990-01-01", DEV_END)
R, V = reg.loc[d90], vrp.loc[d90]
el = R == 1
print(f"ELEVATED days {el.mean()*100:.1f}% of 1990-2012H1; gate open (VRP > {pv['vrp_elev']}) on {(el & (V > pv['vrp_elev'])).sum()/el.sum()*100:.1f}% of them "
      f"= {(el & (V > pv['vrp_elev'])).mean()*100:.1f}% of all days; v2 cash {(lv.loc[d90]==0).mean()*100:.1f}% vs original {(lo.loc[d90]==0).mean()*100:.1f}%")
ro = E.run(df, lo, cost_bps=3, financing_spread_bps=60, start="1990-01-01", end=DEV_END).daily
rv = E.run(df, lv, cost_bps=3, financing_spread_bps=60, start="1990-01-01", end=DEV_END).daily
diff = rv["lev"] != ro["lev"]
print(f"days where v2 position differs from original: {diff.sum()} ({diff.mean()*100:.1f}%); v2 changes/yr {((rv['lev'].diff().fillna(0)!=0).sum()/(len(rv)/252)):.1f} vs {((ro['lev'].diff().fillna(0)!=0).sum()/(len(ro)/252)):.1f}")
per = {"1990-1994": ("1990-01-01", "1994-12-31"), "1995-1999": ("1995-01-01", "1999-12-31"), "2000-02 bear": ("2000-03-24", "2002-10-09"),
       "2003-2007": ("2002-10-10", "2007-10-08"), "2007-09 GFC": ("2007-10-09", "2009-03-09"), "2009 recovery": ("2009-03-10", "2009-12-31"),
       "2010-2012H1": ("2010-01-01", DEV_END)}
print(f"{'period':14s} {'orig tot':>9s} {'v2 tot':>9s} {'SPX-xs':>8s} | {'leg days':>8s} {'leg P&L':>8s} {'leg hit%':>8s} | {'v2 cash':>7s} {'v2 avgL':>7s}")
for k, (s, e) in per.items():
    a, b = ro.loc[s:e], rv.loc[s:e]
    leg = b[(b["lev"] == 1) & (a["lev"] == 0)]
    tot = lambda r: ((1 + r).prod() - 1) * 100
    print(f"{k:14s} {tot(a['ret']):+8.1f}% {tot(b['ret']):+8.1f}% {tot(b['x']):+7.1f}% | {len(leg):8d} {tot(leg['x']):+7.1f}% {(leg['x']>0).mean()*100 if len(leg) else float('nan'):7.0f}% | {(b['lev']==0).mean()*100:6.0f}% {b['lev'].mean():7.2f}")
# the ELEVATED leg's own risk profile
leg = rv[(rv["lev"] == 1) & (ro["lev"] == 0)]
print(f"ELEV-leg all: {len(leg)} days, mean daily excess {leg['x'].mean()*1e4:.1f} bp, ann vol {leg['x'].std()*np.sqrt(252)*100:.1f}%, "
      f"worst day {leg['x'].min()*100:.2f}% on {leg['x'].idxmin().date()}, Sharpe-like {leg['x'].mean()/leg['x'].std()*np.sqrt(252):.2f}")
# monthly worst for v2
mm = (1 + rv["ret"]).resample("ME").prod() - 1
print("v2 worst 5 months:", [(t.strftime('%Y-%m'), round(x*100, 2)) for t, x in mm.nsmallest(5).items()])
print("v2 yearly CAGR vs SPX-excess (1x):")
yy = (1 + rv["ret"]).resample("YE").prod() - 1; yo = (1 + ro["ret"]).resample("YE").prod() - 1; yx = (1 + rv["x"] + rv["rf"]).resample("YE").prod() - 1
print(" ".join(f"{t.year}:{y*100:+.0f}/{yo[t]*100:+.0f}/{yx[t]*100:+.0f}" for t, y in yy.items()))
