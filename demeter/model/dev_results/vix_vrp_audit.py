"""Part-1 audit of signals/vix_vrp.py on DEV only (market data truncated at 2012-06-30).
Prints: state-machine occupancy and spell lengths, what the ELEVATED cash state cost/saved by period,
the Sep-2008..Mar-2009 leverage path + daily P&L, and the location of the -28.6% daily drawdown inside the GFC.
Writes the full GFC daily table to dev_results/vix_vrp_gfc_daily.csv (banked, not printed)."""
import sys, importlib.util
from pathlib import Path
import numpy as np, pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import engine as E
import features as F

spec = importlib.util.spec_from_file_location("vix_vrp", HERE / "signals" / "vix_vrp.py")
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

DEV_END = "2012-06-30"
df = E.load_market(end=DEV_END)
assert df.index[-1] <= pd.Timestamp(DEV_END)
p = dict(mod.DEFAULT_PARAMS)
lev = mod.signal(df, **p).reindex(df.index)
vix = df["vix_close"].ffill()
reg = mod.vix_regime(vix, p["v_calm"], p["v_panic"], p["hyst"])
rv = F.realized_vol(df["spx_ret"], p["rv_win"]); vrp = vix / 100.0 - rv
x = df["spx_tr_ret"] - df["rf_daily"]           # market excess return on day t

d90 = df.loc["1990-01-01":DEV_END].index
R, L, V, X = reg.loc[d90], lev.loc[d90], vrp.loc[d90], x.loc[d90]
names = {0: "CALM", 1: "ELEV", 2: "PANIC"}

def spells(mask):
    runs, cur = [], 0
    for v in mask.values:
        if v: cur += 1
        elif cur: runs.append(cur); cur = 0
    if cur: runs.append(cur)
    return np.array(runs)

print("=== state occupancy 1990-2012H1 (share of days, spells, spell length days) ===")
for s, nm in names.items():
    m = R == s
    sp = spells(m)
    vrp_cash = ((V < p["vrp_min"]) & m).mean() * 100
    print(f"{nm:5s}: {m.mean()*100:5.1f}% of days | {len(sp):3d} spells | mean {sp.mean():6.1f} median {np.median(sp):5.0f} max {sp.max():4d} | VRP-filter cash inside state {vrp_cash:4.1f}% of all days")
print(f"lev target dist: {L.value_counts(normalize=True).sort_index().round(3).to_dict()}   overall cash {(L==0).mean()*100:.1f}%")
print("VRP filter overrides (days lev forced 0 by VRP while state would invest):",
      int(((V < p['vrp_min']) & (R != 1)).sum()), " of which CALM", int(((V < p['vrp_min']) & (R == 0)).sum()), " PANIC", int(((V < p['vrp_min']) & (R == 2)).sum()))

print("\n=== longest ELEVATED spells (start, end, days, SPX excess total over the spell) ===")
m = (R == 1).values
i = 0; rows = []
while i < len(m):
    if m[i]:
        j = i
        while j + 1 < len(m) and m[j + 1]: j += 1
        # the position in effect during spell days is the target from the previous close; approximate with same-day excess shifted by one
        seg = X.iloc[i + 1:j + 2]
        rows.append((str(d90[i].date()), str(d90[j].date()), j - i + 1, ((1 + seg).prod() - 1) * 100))
        i = j + 1
    else:
        i += 1
rows.sort(key=lambda r: -r[2])
for r in rows[:12]:
    print(f"  {r[0]} -> {r[1]}  {r[2]:4d} days  SPX excess over spell {r[3]:+7.1f}%")

print("\n=== cost / saving of the cash days (position in effect = target shifted 1) by period; SPX excess return earned by 1x on those days ===")
pos = lev.shift(1)
per = {"1990-1994": ("1990-01-01", "1994-12-31"), "1995-1999": ("1995-01-01", "1999-12-31"), "2000-02 bear": ("2000-03-24", "2002-10-09"),
       "2003-2007": ("2002-10-10", "2007-10-08"), "2007-09 GFC": ("2007-10-09", "2009-03-09"), "2009 recovery": ("2009-03-10", "2009-12-31"),
       "2010-2012H1": ("2010-01-01", DEV_END)}
for k, (s, e) in per.items():
    sl = slice(s, e)
    ps, xs, rs = pos.loc[sl], x.loc[sl], reg.shift(1).loc[sl]
    cash = ps == 0
    elev_cash = cash & (rs == 1)
    vrp_cash = cash & (rs != 1)
    def tot(mask): return ((1 + xs[mask]).prod() - 1) * 100
    print(f"{k:14s}: days {len(ps):4d} cash {cash.mean()*100:4.0f}% | 1x excess on ALL days {tot(xs.notna()):+7.1f}% | missed on ELEV-cash days {tot(elev_cash):+7.1f}% "
          f"({elev_cash.mean()*100:3.0f}% of days) | avoided on VRP-cash days {tot(vrp_cash):+6.1f}% ({vrp_cash.mean()*100:3.0f}%) | avgL {ps.mean():.2f}")

print("\n=== 2007-09 GFC: where the model lost (E.run at 3bp/60bp) ===")
res = E.run(df, lev, cost_bps=3.0, financing_spread_bps=60.0, start="2007-10-09", end="2009-03-09")
d = res.daily.copy()
d["vix"] = vix.reindex(d.index); d["state"] = reg.shift(1).reindex(d.index).map(names); d["vrp"] = vrp.shift(1).reindex(d.index)
d["spx_ret"] = df["spx_ret"].reindex(d.index)
eq = d["equity"]; dd = eq / eq.cummax() - 1
trough = dd.idxmin(); peak = eq.loc[:trough].idxmax()
print(f"episode total {((eq.iloc[-1]) - 1)*100:+.1f}%  daily maxDD {dd.min()*100:.1f}% from {peak.date()} to {trough.date()}")
inv = d[d["lev"] > 0]
print(f"invested days {len(inv)} of {len(d)}; P&L on invested days {((1+inv['ret']).prod()-1)*100:+.1f}%; by state: " +
      ", ".join(f"{s}: {((1+g['ret']).prod()-1)*100:+.1f}% over {len(g)}d" for s, g in inv.groupby('state')))
print("worst 8 model days:")
for t, r in d.nsmallest(8, "ret").iterrows():
    print(f"  {t.date()} spx {r['spx_ret']*100:+.2f}% vix {r['vix']:.1f} state {r['state']} vrp {r['vrp']:+.3f} pos {r['lev']:.0f} model {r['ret']*100:+.2f}%")
g = d.loc["2008-09-01":"2009-03-31"].copy()
g["dd"] = dd.reindex(g.index)
g_out = g[["spx_ret", "vix", "state", "vrp", "lev", "ret", "equity", "dd"]]
g_out.to_csv(HERE / "dev_results" / "vix_vrp_gfc_daily.csv", float_format="%.5f")
print("\n=== Sep-2008..Mar-2009 leverage path: invested days and position-change days (full table -> dev_results/vix_vrp_gfc_daily.csv) ===")
chg = g["lev"].diff().fillna(0) != 0
show = g[(g["lev"] > 0) | chg]
for t, r in show.iterrows():
    print(f"  {t.date()} spx {r['spx_ret']*100:+6.2f}% vix {r['vix']:5.1f} {r['state']:5s} vrp {r['vrp']:+.3f} pos {r['lev']:.0f} model {r['ret']*100:+6.2f}% eq {r['equity']:.3f} dd {r['dd']*100:6.1f}%")
print("monthly model vs SPX-1x-excess, Sep-08..Mar-09:")
mm = (1 + g["ret"]).resample("ME").prod() - 1; mx = (1 + g["x"]).resample("ME").prod() - 1
ml = g["lev"].resample("ME").mean()
for t in mm.index:
    print(f"  {t.strftime('%Y-%m')} model {mm[t]*100:+6.2f}% spx-excess {mx[t]*100:+6.2f}% avg pos {ml[t]:.2f}")

print("\n=== 2009 recovery: share of days by position, and how the 1x PANIC leg was released ===")
r9 = E.run(df, lev, cost_bps=3.0, financing_spread_bps=60.0, start="2009-03-10", end="2009-12-31").daily
r9["state"] = reg.shift(1).reindex(r9.index).map(names)
print(r9.groupby("state")["lev"].agg(["count", "mean"]).to_string())
print(f"first day at 2x after Mar-2009: {r9[r9['lev'] >= 2].index.min()}; total {((1+r9['ret']).prod()-1)*100:+.1f}% vs SPX-excess {((1+r9['x']).prod()-1)*100:+.1f}%")
print("\n=== 2000-02 bear ===")
rb = E.run(df, lev, cost_bps=3.0, financing_spread_bps=60.0, start="2000-03-24", end="2002-10-09").daily
rb["state"] = reg.shift(1).reindex(rb.index).map(names)
print(rb.groupby("state").apply(lambda g: pd.Series({"days": len(g), "avg_pos": g["lev"].mean(), "pnl_pct": ((1+g["ret"]).prod()-1)*100})).to_string())
