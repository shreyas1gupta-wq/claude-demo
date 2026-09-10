"""SC-D3a — survivor-panel cross-check of the India small-vs-large inversion.
Registered 2026-09-10 BEFORE this run (commit 4aaba0a). One-way rule: the panel
flatters smallcap (no delistings), so only anti-smallcap prints are evidence.
Prints only; interpretation hand-appended after."""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

px = pd.read_csv(f"{V}/panel/n500_adjclose_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date")
vt = pd.read_csv(f"{V}/panel/n500_value_traded_2012_2022.csv.gz", parse_dates=["Date"]).set_index("Date")

mret = px.resample("ME").last().pct_change()                   # monthly returns per name
adv = vt.rolling(252, min_periods=126).median().resample("ME").last()  # trailing-12m median value traded

# size terciles per month from ADV; SL = EW small tercile - EW large tercile (next month's return)
sl = {}
for me in mret.index[1:]:
    prev = adv.index[adv.index.get_indexer([me], method="pad")[0] - 1] if me not in adv.index else me
    a = adv.loc[:me].iloc[-2] if len(adv.loc[:me]) >= 2 else None  # ADV known at prior month-end
    r = mret.loc[me]
    if a is None:
        continue
    both = pd.concat([a.rename("adv"), r.rename("ret")], axis=1).dropna()
    if len(both) < 150:
        continue
    t = pd.qcut(both.adv, 3, labels=["S", "M", "L"])
    sl[me] = both.ret[t == "S"].mean() - both.ret[t == "L"].mean()
SL = pd.Series(sl).sort_index()
print(f"panel SL series: {len(SL)} months, {SL.index[0]:%Y-%m} -> {SL.index[-1]:%Y-%m}, "
      f"mean {SL.mean()*1200:+.2f}%/yr (survivor-flattered; context only)")

nifty = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
ncol = [c for c in nifty.columns if "close" in c.lower() or "Close" in c][0]
nm = nifty[ncol].resample("ME").last().pct_change()

tr12_mkt = (1 + nm).rolling(12).apply(np.prod, raw=True) - 1
nxt12_sl = SL.rolling(12).sum().shift(-12)  # sum of monthly SL over next 12m, in decimal
state = np.sign(tr12_mkt.reindex(SL.index))
d = pd.DataFrame({"s": state, "f": nxt12_sl}).dropna()
dn, up = d.f[d.s < 0], d.f[d.s > 0]
print(f"a1 next-12m SL after NIFTY down-12m: {dn.mean()*100:+.2f}pp (n={len(dn)}) | "
      f"after up-12m: {up.mean()*100:+.2f}pp (n={len(up)}) | gap {(dn.mean()-up.mean())*100:+.2f}pp")
print(f"   down-state months: {', '.join(sorted(set(d.index[d.s < 0].strftime('%Y-%m'))))}")

tr36_sl = SL.rolling(36).sum()
try:
    lo = tr36_sl.expanding(60).quantile(1/3).shift(1)
    hi = tr36_sl.expanding(60).quantile(2/3).shift(1)
    t = pd.Series(np.where(tr36_sl <= lo, "LO", np.where(tr36_sl <= hi, "MID", "HI")), index=SL.index)
    t[lo.isna()] = np.nan
    mode = "expanding(min 60m, lagged)"
except Exception:
    t = pd.qcut(tr36_sl, 3, labels=["LO", "MID", "HI"]); mode = "full-sample FLAGGED"
d2 = pd.DataFrame({"t": t, "f": nxt12_sl}).dropna()
r = d2.groupby("t").f.mean() * 100
print(f"a2 trailing-36m SL terciles ({mode}) -> next-12m SL: "
      f"LO {r.get('LO', np.nan):+.2f} | MID {r.get('MID', np.nan):+.2f} | HI {r.get('HI', np.nan):+.2f} pp "
      f"(n={d2.groupby('t').f.count().to_dict()})")

cum = SL.loc["2018-01-31":].cumsum()
trough_date = cum.loc[:"2019-12-31"].idxmin()
trough = cum.loc[trough_date]
after12 = cum.loc[:trough_date + pd.DateOffset(months=12)].iloc[-1] - trough
print(f"a3 2018-19 unwind: cumulative SL 2018-01 -> trough {trough_date:%Y-%m}: {trough*100:+.2f}pp; "
      f"next 12m from trough: {after12*100:+.2f}pp (survivor caveat: true damage WORSE)")
