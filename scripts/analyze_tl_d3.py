"""TL-D3 — US daily tails (DJIA 1980-2012, SPX futures 1982-2024) + atlas extras.

Registered 2026-09-07 BEFORE this run. Prints + appends key d3 to tl_atlas_stats.json.
"""
import json
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
ROOT = "/home/user/claude-demo"
V = f"{ROOT}/ingest/vault"
D3 = {}


def ledger(r, name):
    z = (r - r.mean()) / r.std()
    n = len(r)
    out = []
    print(f"{name}: n={n}, sd {100*r.std():.2f}%/d (ann {100*r.std()*np.sqrt(252):.1f}%), "
          f"ex.kurt {stats.kurtosis(r):.1f}, skew {stats.skew(r):+.2f}")
    for k in (1, 2, 3, 4, 6):
        lo, hi = int((z <= -k).sum()), int((z >= k).sum())
        gauss = 2 * stats.norm.sf(k) * n
        out.append(dict(k=k, lo=lo, hi=hi, gauss=gauss))
        print(f"  |z|>={k}: {lo+hi} ({lo}dn/{hi}up) vs Gaussian {gauss:.3f} "
              f"({(lo+hi)/gauss if gauss > 1e-9 else float('inf'):,.0f}x)")
    ac = [float(r.abs().autocorr(l)) for l in range(1, 31)]
    vol21 = (r.rolling(21).std() * np.sqrt(252)).dropna()
    phi = float(vol21.autocorr(1))
    print(f"  |r| autocorr lag1 {ac[0]:+.2f} lag30 {ac[29]:+.2f} all>0={all(a>0 for a in ac)}; "
          f"vol phi {phi:.3f} half-life {np.log(0.5)/np.log(phi):.0f}d")
    return dict(n=n, sd=float(r.std()), ek=float(stats.kurtosis(r)), sk=float(stats.skew(r)),
                table=out, ac1=ac[0], ac30=ac[29], allpos=bool(all(a > 0 for a in ac)),
                phi=phi, worst=[[str(d.date()), round(100*x, 2)] for d, x in r.nsmallest(5).items()],
                best=[[str(d.date()), round(100*x, 2)] for d, x in r.nlargest(5).items()])


# ---- DJIA daily ----
dj = pd.read_csv(f"{V}/us_index/djia_daily_1980_2012.csv",
                 parse_dates=["rownames"]).set_index("rownames")["dat"]
rdj = dj.pct_change().dropna()
rdj = rdj[rdj != 0]  # weekday-grid holidays, declared
print("t1/t2 —"); D3["djia"] = ledger(rdj, "DJIA daily 1980-2012")

# ---- SPX futures daily (declared conventions) ----
adj = pd.read_csv(f"{V}/us_index/sp500_fut_adjusted_daily.csv", parse_dates=["DATETIME"])
mul = pd.read_csv(f"{V}/us_index/sp500_fut_multiple_daily.csv", parse_dates=["DATETIME"])
def daily(df, col):
    df = df.set_index("DATETIME")[col]
    def pick(g):
        h20 = g[g.index.hour == 20]
        return h20.iloc[-1] if len(h20) else g.iloc[-1]
    out = df.groupby(df.index.date).apply(lambda g: pick(g))
    out.index = pd.to_datetime(out.index)
    return out
a, u = daily(adj, "price"), daily(mul, "PRICE")
rsp = (a.diff() / u.shift(1)).dropna()
rsp = rsp[rsp != 0]
print("\nt3/t4 —"); D3["spx"] = ledger(rsp, "SPX futures daily 1982-2024")

# ---- t5: 1987 anatomy ----
z_dj = (rdj - rdj.mean()) / rdj.std()
z_sp = (rsp - rsp.mean()) / rsp.std()
bm = pd.Timestamp("1987-10-19")
print(f"\nt5 — BLACK MONDAY: DJIA -22.61% = {z_dj[bm]:.1f} sigma | SPX futures -28.61% = "
      f"{z_sp[bm]:.1f} sigma")
wk = rdj.loc["1987-10-14":"1987-10-30"]
print("  the fortnight:", [(str(d.date())[5:], f"{100*x:+.1f}%") for d, x in wk.items()])
peak87 = dj.loc[:"1987-10-16"].max()
rec = dj.loc["1987-10-19":][dj.loc["1987-10-19":] >= peak87]
print(f"  DJIA recovery to the 1987 peak: {rec.index[0].date()} "
      f"({(rec.index[0]-bm).days} days)")
D3["bm"] = dict(dj_sig=float(z_dj[bm]), sp_sig=float(z_sp[bm]),
                week=[[str(d.date())[5:], round(100*x, 1)] for d, x in wk.items()],
                rec_days=int((rec.index[0] - bm).days))

# ---- t6: S&P month-of-year seasonality 155y ----
sh = pd.read_csv(f"{V}/us_index/sp500_shiller_monthly_1871.csv",
                 parse_dates=["Date"]).set_index("Date").sort_index()
spx_m = sh.SP500.pct_change().dropna()
sea = spx_m.groupby(spx_m.index.month).agg(["mean", lambda s: (s > 0).mean(), "count"])
sea.columns = ["mean", "hit", "n"]
print("\nt6 — S&P seasonality 1871-2026 (mean %, hit rate):")
MN = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
for m in range(1, 13):
    print(f"  {MN[m-1]}: {100*sea.loc[m,'mean']:+.2f}%  ({100*sea.loc[m,'hit']:.0f}% up, n={sea.loc[m,'n']:.0f})")
print(f"  BAR (Sep mean < 0): {'PASS' if sea.loc[9,'mean'] < 0 else 'FAIL'}")
D3["season"] = [[MN[m-1], round(100*sea.loc[m, "mean"], 2), round(100*sea.loc[m, "hit"])] for m in range(1, 13)]

# ---- t7: decade table ----
rtr = ((sh["Real Price"] + sh["Real Dividend"] / 12) / sh["Real Price"].shift(1) - 1).where(sh["Real Price"] > 0)
print("\nt7 — decades (S&P nominal price CAGR / real TR CAGR %/yr):")
dec_rows = []
for d0 in range(1880, 2030, 10):
    nm = spx_m.loc[f"{d0-10}":f"{d0-1}"]
    rl = rtr.loc[f"{d0-10}":f"{d0-1}"].dropna()
    g_n = 100 * (np.expm1(np.log1p(nm).mean() * 12)) if len(nm) > 100 else np.nan
    g_r = 100 * (np.expm1(np.log1p(rl).mean() * 12)) if len(rl) > 100 else np.nan
    dec_rows.append([f"{d0-10}s", round(g_n, 1), round(g_r, 1) if not np.isnan(g_r) else None])
    print(f"  {d0-10}s: nominal {g_n:+5.1f} | real TR {g_r:+5.1f}")
D3["decades"] = dec_rows

# ---- t8/t9: storm transition ----
def storm(r, name, bar=0.02):
    s = (r.abs() >= bar)
    cond = float(s[s.shift(1).fillna(False)].mean())
    unc = float(s.mean())
    print(f"  {name}: P(storm)={100*unc:.1f}% | P(storm|storm)={100*cond:.1f}% -> {cond/unc:.1f}x")
    return [round(100*unc, 1), round(100*cond, 1), round(cond/unc, 1)]
print("\nt8/t9 — storm transition (|r| >= 2%):")
D3["storm"] = dict(spx=storm(rsp, "SPX futures"), nifty=None, djia=storm(rdj, "DJIA"))
nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
rn = nf["Adj Close"].pct_change().dropna()
D3["storm"]["nifty"] = storm(rn, "NIFTY 50")

# ---- t10: 3-sigma days per year (SPX futures) ----
z3 = (z_sp.abs() >= 3)
per_yr = z3.groupby(z_sp.index.year).sum()
print("\nt10 — SPX 3-sigma days/yr (nonzero):",
      {int(y): int(c) for y, c in per_yr.items() if c > 0})
D3["sig3_yr"] = [[int(y), int(c)] for y, c in per_yr.items()]

# ---- t11: top-5 US real drawdowns ----
lr = np.log1p(rtr.dropna())
idx = lr.cumsum()
run_max = idx.cummax()
dd = idx - run_max
print("\nt11 — top US real-TR drawdowns (find episodes):")
episodes = []
in_dd = False
for t, v in dd.items():
    if v < -0.10 and not in_dd:
        in_dd = True; start = t; trough_v = v; trough_t = t
    elif in_dd:
        if v < trough_v: trough_v, trough_t = v, t
        if v >= -1e-9:
            episodes.append((start, trough_t, t, 100*(1-np.exp(trough_v))))
            in_dd = False
if in_dd:
    episodes.append((start, trough_t, None, 100*(1-np.exp(trough_v))))
episodes.sort(key=lambda e: -e[3])
for s0, tt, e0, depth in episodes[:5]:
    print(f"  -{depth:.0f}%: peak~{str(s0.date())[:7]} trough {str(tt.date())[:7]} "
          f"recovered {str(e0.date())[:7] if e0 else 'NOT in span'}")
D3["dd5"] = [[str(s0.date())[:7], str(tt.date())[:7], str(e0.date())[:7] if e0 else ">span",
              round(depth)] for s0, tt, e0, depth in episodes[:5]]

# ---- t12: streaks ----
def maxdownstreak(r):
    c = mx = 0
    for x in r:
        c = c + 1 if x < 0 else 0
        mx = max(mx, c)
    return mx
yr_n = spx_m.groupby(spx_m.index.year).apply(lambda s: np.expm1(np.log1p(s).sum()))
print(f"\nt12 — streaks: max consecutive down DAYS: DJIA {maxdownstreak(rdj)}, "
      f"SPX {maxdownstreak(rsp)}, NIFTY {maxdownstreak(rn)}; "
      f"max consecutive down YEARS (S&P nominal, 155y): {maxdownstreak(yr_n)} "
      f"(down-year rate {100*(yr_n<0).mean():.0f}%)")
D3["streaks"] = dict(days=[maxdownstreak(rdj), maxdownstreak(rsp), maxdownstreak(rn)],
                     years=int(maxdownstreak(yr_n)), dy_rate=round(100*float((yr_n < 0).mean())))

with open(f"{ROOT}/research/notes/tl_atlas_stats.json") as f:
    D = json.load(f)
D["d3"] = D3
with open(f"{ROOT}/research/notes/tl_atlas_stats.json", "w") as f:
    json.dump(D, f)
print("\nd3 appended")
