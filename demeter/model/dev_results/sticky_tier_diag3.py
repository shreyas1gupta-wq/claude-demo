"""Frozen-point diagnostics: change log, stickiness cost/benefit variants, 1x-floor at the frozen point, volmanaged side-by-side,
T-bill-zeroed CAGR. Writes dev_results/sticky_tier_diag3.txt. All windows end 2012-06-30 (DEV only)."""
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
FP = dict(st.DEFAULT_PARAMS)
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

lev = st.signal(df, **FP)
fast = F.ewma_vol(df["spx_ret"], FP["hl"], 20); slow = F.ewma_vol(df["spx_ret"], FP["hl"] * FP["long_mult"], 20); sig = pd.concat([fast, slow], axis=1).max(axis=1)
ch = lev[lev.diff().fillna(0) != 0]
P(f"FROZEN {FP}  -- position changes 1950-2012H1: {len(ch)}")
prev = None
for t, v in ch.items():
    P(f"  {t.date()}  {'' if prev is None else int(prev)}->{int(v)}  sigma {sig.loc[t]*100:5.1f}% (fast {fast.loc[t]*100:5.1f} slow {slow.loc[t]*100:5.1f})  spx_ret {df.spx_ret.loc[t]*100:+.2f}%")
    prev = v
P("\nlevel share by decade (dev):")
for s, e in [("1950", "1959"), ("1960", "1969"), ("1970", "1979"), ("1980", "1989"), ("1990", "1999"), ("2000", "2009"), ("2010", "2012")]:
    l = lev.loc[s:e]; P(f"  {s}-{e}: cash {(l==0).mean()*100:4.0f}%  1x {(l==1).mean()*100:4.0f}%  2x {(l==2).mean()*100:4.0f}%  3x {(l==3).mean()*100:4.0f}%  avgL {l.mean():.2f}")

def row(l, s, e):
    r = E.run(df, l, start=s, end=e, **C); m = r.metrics(); d = r.daily
    rz = d["ret"] - d["rf"].where(d["lev"] == 0, 0.0)          # T-bill zeroed on cash days
    cz = ((1 + rz).prod() ** (252 / len(rz)) - 1) * 100 if len(rz) else np.nan
    return dict(cagr=m["annualized_return_pct"], cagr_rf0=cz, spy=m["spy_annualized_return_pct"], sh=m.get("sharpe"), dd=m["max_drawdown_pct"], spydd=m["spy_max_drawdown_pct"],
                worstM=m["worst_month_pct"], avgL=m["avg_leverage"], cash=m["pct_days_cash"], chg=m["position_changes_per_year"], upcap=m.get("up_capture_pct"), dncap=m.get("down_capture_pct"))
variants = {"frozen": lev,
            "unsticky (h0 P1 M0 daily)": st.signal(df, **{**FP, "h": 0.0, "P": 1}, M=0, weekly_up=False),
            "no memory (long_mult 1)": st.signal(df, **{**FP, "long_mult": 1.0}),
            "1x floor": st.signal(df, **FP, floor=1),
            "volmanaged": vm.signal(df), "SPY 1x": E.buy_and_hold(df, 1.0)}
wins = {"dev_1990": ("1990-01-01", "2012-06-30"), "dev_1950": ("1950-01-03", "2012-06-30"), "era 1950-69": ("1950-01-03", "1969-12-31"), "era 1970-89": ("1970-01-01", "1989-12-31"),
        "chop 1990-99": ("1990-01-01", "1999-12-31"), "chop 2003-07": ("2003-01-01", "2007-12-31"), "1987 Aug25-Dec31": ("1987-08-25", "1987-12-31"),
        "2008 Sep1-Mar09": ("2008-09-01", "2009-03-09"), "2009 recovery": ("2009-03-10", "2009-12-31"), "2000-02 bear": ("2000-03-24", "2002-10-09")}
pd.set_option("display.width", 250)
for w, (s, e) in wins.items():
    P(f"\n== {w}"); P(pd.DataFrame({k: row(l, s, e) for k, l in variants.items()}).T.round(2).to_string())
P("\nlevel held on shock days (target decided at previous close -> position in effect):")
for d in ["1987-10-16", "1987-10-19", "1987-10-26", "2008-09-15", "2008-09-29", "2008-10-15", "2011-08-08", "1962-05-28", "2010-05-06", "1998-08-31"]:
    t = pd.Timestamp(d)
    if t in lev.index:
        i = lev.index.get_loc(t)
        P(f"  {d}: spx {df.spx_ret.iloc[i]*100:+.1f}%  frozen pos {lev.iloc[i-1]:.0f} (unsticky {variants['unsticky (h0 P1 M0 daily)'].iloc[i-1]:.0f}, volmanaged {variants['volmanaged'].iloc[i-1]:.2f})  sigma prev close {sig.iloc[i-1]*100:.1f}%")
open("dev_results/sticky_tier_diag3.txt", "w", encoding="utf-8").write("\n".join(out))
