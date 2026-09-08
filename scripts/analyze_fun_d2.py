"""FUN-D2 — the earnings cycle (US, Shiller 1871-2023). Registered 2026-09-08 BEFORE
this run. Real earnings with a DECLARED 6-month availability lag on all conditioning;
descriptive census cells exempt and marked. Guard: Real Price > 0. Prints only.
"""
import numpy as np
import pandas as pd
from scipy import stats

V = "/home/user/claude-demo/ingest/vault"
sh = pd.read_csv(f"{V}/us_index/sp500_shiller_monthly_1871.csv", parse_dates=["Date"])
sh = sh[sh["Real Price"] > 0].set_index("Date")
# run note (same class as the booked Real Price guard): the mirror's Real Earnings
# column carries zeros in its stale tail -> log(0)/fake -100% episode; guard RE > 0.
RE = sh["Real Earnings"]
RE = RE[RE > 0].dropna()
RP = sh["Real Price"]
RD = sh["Real Dividend"]
PE = sh["PE10"].replace(0, np.nan)

print(f"FUN-D2 — the earnings cycle, {RE.index[0].date()}..{RE.index[-1].date()}")

# e1 earnings-recession census (descriptive, no lag needed)
runmax = RE.cummax()
dd = RE / runmax - 1
eps = []
in_ep = False
for t, v in dd.items():
    if not in_ep and v <= -0.10:
        in_ep = True
        pk_val = runmax[t]
        pk_date = RE[RE == pk_val].index[0]
        tr_val, tr_date = v, t
    elif in_ep:
        if v < tr_val:
            tr_val, tr_date = v, t
        if v >= 0:
            rec_m = (t.year - tr_date.year) * 12 + t.month - tr_date.month
            eps.append((pk_date, tr_date, tr_val, rec_m))
            in_ep = False
if in_ep:
    eps.append((pk_date, tr_date, tr_val, np.nan))
depths = np.array([e[2] for e in eps])
durs = [(e[1].year - e[0].year) * 12 + e[1].month - e[0].month for e in eps]
recs = [e[3] for e in eps if not pd.isna(e[3])]
print(f"  e1 earnings recessions (real E, >=10% decline): {len(eps)} in "
      f"{(RE.index[-1]-RE.index[0]).days/365.25:.0f}y (~{len(eps)/((RE.index[-1]-RE.index[0]).days/365.25)*10:.1f}/decade) | "
      f"median depth {100*np.median(depths):.0f}% worst {100*depths.min():.0f}% | "
      f"median peak->trough {np.median(durs):.0f}m | median recovery {np.median(recs):.0f}m")

# e2/e3 price-vs-earnings lead/lag at troughs and peaks (descriptive)
leads_tr, leads_pk = [], []
for pk_date, tr_date, _, _ in eps:
    w = RP.loc[tr_date - pd.DateOffset(months=24): tr_date + pd.DateOffset(months=24)]
    if len(w):
        lt = (w.idxmin().year - tr_date.year) * 12 + (w.idxmin().month - tr_date.month)
        leads_tr.append(lt)
    w2 = RP.loc[pk_date - pd.DateOffset(months=24): pk_date + pd.DateOffset(months=24)]
    if len(w2):
        lp = (w2.idxmax().year - pk_date.year) * 12 + (w2.idxmax().month - pk_date.month)
        leads_pk.append(lp)
print(f"  e2 at E-TROUGHS: price bottom leads earnings trough by median "
      f"{-np.median(leads_tr):.0f}m (negative=price first in {100*np.mean(np.array(leads_tr)<0):.0f}% of episodes)")
print(f"  e3 at E-PEAKS: price top vs earnings peak median {np.median(leads_pk):+.0f}m "
      f"(price first in {100*np.mean(np.array(leads_pk)<0):.0f}%)")

# conditioning signals (6m availability lag)
RE_l = RE.shift(6)
trend10 = RE_l.rolling(120).median()
above = (RE_l > trend10)
fwd12 = RP.shift(-12) / RP - 1
base = pd.DataFrame({"above": above, "fwd": fwd12,
                     "rising": RE_l > RE_l.shift(12),
                     "pe": PE}).dropna(subset=["fwd", "above"])
base["above"] = base["above"].astype(bool)
base["rising"] = base["rising"].astype(bool)

# e4 above/below trend
a_, b_ = base[base.above].fwd, base[~base.above].fwd
print(f"  e4 next-12m real return: E ABOVE 10y trend {100*a_.mean():+.1f}% (med {100*a_.median():+.1f}) "
      f"vs BELOW {100*b_.mean():+.1f}% (med {100*b_.median():+.1f}) [lagged 6m; n={len(a_)}/{len(b_)}]")

# e5 within PE10 halves (expanding median split, price-based real-time)
pe_med = base.pe.expanding(120).median()
cheap = base.pe < pe_med
for lab, m in [("CHEAP", cheap), ("RICH", ~cheap)]:
    aa = base[m & base.above].fwd
    bb = base[m & ~base.above].fwd
    print(f"  e5 {lab} PE10 half: above-trend {100*aa.mean():+.1f}% vs below-trend {100*bb.mean():+.1f}%")

# e6 earnings direction
r_, f_ = base[base.rising == True].fwd, base[base.rising == False].fwd  # noqa: E712
print(f"  e6 next-12m: E RISING (12m) {100*r_.mean():+.1f}% vs FALLING {100*f_.mean():+.1f}%")

# e7 dividend smoothness (descriptive)
de = np.log(RE).diff(12).replace([np.inf, -np.inf], np.nan).dropna()
dv = np.log(RD[RD > 0]).diff(12).replace([np.inf, -np.inf], np.nan).dropna()
ratio = de.std() / dv.std()
pay = []
for pk_date, tr_date, depth, _ in eps:
    if pk_date in RD.index and tr_date in RD.index and RD[pk_date] > 0:
        pay.append((RD[tr_date] / RD[pk_date] - 1) / depth)
print(f"  e7 smoothness: sd(dlogE)/sd(dlogD) = {ratio:.1f}x | in E-recessions dividends fall "
      f"{100*np.median(pay):.0f}% as much as earnings (median)")

# e8 depth vs price drawdown (descriptive)
pdd = []
for pk_date, tr_date, depth, _ in eps:
    w = RP.loc[pk_date:tr_date]
    if len(w) > 1:
        pdd.append((w / w.cummax() - 1).min())
rho = stats.spearmanr(depths[:len(pdd)], pdd)[0]
print(f"  e8 E-recession depth vs price maxDD over same window: rank-corr {rho:+.2f} "
      f"(median price DD {100*np.median(pdd):.0f}%)")

# e9 the two deepest (descriptive)
worst2 = sorted(eps, key=lambda e: e[2])[:2]
for pk, tr, dep, rec in worst2:
    print(f"  e9 deepest: peak {pk.date()} -> trough {tr.date()} {100*dep:.0f}% "
          f"(recovered in {rec:.0f}m)" if not pd.isna(rec) else
          f"  e9 deepest: peak {pk.date()} -> trough {tr.date()} {100*dep:.0f}% (not yet recovered)")

# e10 post-1950 repeat of e4
b5 = base[base.index >= "1950-01-01"]
a5, b5_ = b5[b5.above].fwd, b5[~b5.above].fwd
print(f"  e10 post-1950 e4: above {100*a5.mean():+.1f}% vs below {100*b5_.mean():+.1f}%")

# e11 persistence of annual real E growth
ann = np.log(RE.resample("YE").last()).diff().dropna()
print(f"  e11 AR(1) of annual dlog real E: {ann.autocorr(1):+.2f}")

# e12 PE10 at troughs vs peaks (descriptive)
pe_tr = [PE.get(tr) for _, tr, _, _ in eps if not pd.isna(PE.get(tr, np.nan))]
pe_pk = [PE.get(pk) for pk, _, _, _ in eps if not pd.isna(PE.get(pk, np.nan))]
print(f"  e12 median PE10 at E-troughs {np.median(pe_tr):.1f} vs at E-peaks {np.median(pe_pk):.1f} "
      f"(the market pays MORE per depressed earnings dollar)" if np.median(pe_tr) > np.median(pe_pk)
      else f"  e12 median PE10 at E-troughs {np.median(pe_tr):.1f} vs peaks {np.median(pe_pk):.1f}")
