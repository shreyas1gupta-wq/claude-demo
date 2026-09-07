"""OP-D4 — the composed book vs the 15/15 target. Registered 2026-09-08 BEFORE this run.
Frozen composition: 80% vol-managed NIFTY core (F3a mechanism + OP-D2 stand-down) +
20% T3 dual-momentum NIFTY/gold-INR switcher + the OP-D3 option sleeve overlay.
Paper, zero costs, NIFTY price-only (+1.3pp TR adjustment reported, declared)."""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

V = "/home/user/claude-demo/ingest/vault"
D0, D1 = pd.Timestamp("2011-07-01"), pd.Timestamp("2023-03-31")

nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
S = nf["Adj Close"]
r = S.pct_change()
lr = np.log(S).diff()
ewvol = (lr.pow(2).ewm(alpha=0.06).mean().pow(0.5) * np.sqrt(252))
vx = pd.read_csv(f"{V}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"]).set_index("date")["close"]
pct = pd.Series(expanding_percentile(vx.to_numpy(), min_obs=252), index=vx.index)

gold = pd.read_csv(f"{V}/commodities/gold_monthly_1833_2026.csv")
gold.columns = [c.strip().lower() for c in gold.columns]
dcol = [c for c in gold.columns if "date" in c or "month" in c or "year" in c][0]
pcol = [c for c in gold.columns if c != dcol][0]
gold["d"] = pd.to_datetime(gold[dcol])
g_us = gold.set_index("d")[pcol]
inr = pd.read_csv(f"{V}/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"]).set_index("Date")["INR_per_USD"]
g_inr = (g_us * inr.reindex(g_us.index, method="nearest")).resample("ME").last().dropna()
n_me = S.resample("ME").last()
mom_g = g_inr.pct_change(12)
mom_n = n_me.pct_change(12)
g_ret_m = g_inr.pct_change()

# ---- core: daily exposure (yesterday's state), 80% weight ----
expo = (0.15 / ewvol).clip(upper=1.5)
sd = pct.reindex(S.index).ffill()
expo = expo * np.where(sd >= 0.90, 0.5, 1.0)
core_ret = (expo.shift(1) * r).loc[D0:D1].fillna(0)

# ---- switcher: monthly, 20% weight (marks at month-end, flat intra-month — stated) ----
dates = core_ret.index
sw_ret_d = pd.Series(0.0, index=dates)
month_ends = n_me.loc[D0:D1].index
n_ret_m = n_me.pct_change()
for me in month_ends:
    prev = mom_n.index[mom_n.index < me]
    if not len(prev):
        continue
    sig = prev[-1]
    hold_gold = (mom_g.get(sig, -9) > mom_n.get(sig, -9))
    mret = g_ret_m.get(me, 0.0) if hold_gold else n_ret_m.get(me, 0.0)
    if me in sw_ret_d.index:
        sw_ret_d.loc[me] = 0.0 if pd.isna(mret) else mret

# ---- option overlay: OP-D3 baseline daily book-relative P&L ----
src = open("/home/user/claude-demo/scripts/analyze_op_d3.py").read()
exec(src.split("BASE = ")[0])  # defines df, run(), etc.
op = run(0.60, 2.5, 0.30, D0, D1)
op_ret = op["eq"].pct_change().reindex(dates).fillna(0)

book_ret = 0.8 * core_ret + 0.2 * sw_ret_d + op_ret
eq = (1 + book_ret).cumprod()
yrs = (D1 - D0).days / 365.25
cagr = 100 * (eq.iloc[-1] ** (1 / yrs) - 1)
dd = 100 * (eq / eq.cummax() - 1).min()
yearly = eq.resample("YE").last().pct_change().dropna()
h1 = eq.loc[:"2016-12-31"]; h2 = eq.loc["2017-01-01":]
c1 = 100 * ((h1.iloc[-1] / h1.iloc[0]) ** (365.25 / (h1.index[-1] - h1.index[0]).days) - 1)
c2 = 100 * ((h2.iloc[-1] / h2.iloc[0]) ** (365.25 / (h2.index[-1] - h2.index[0]).days) - 1)

print(f"OP-D4 — THE COMPOSED BOOK, {D0.date()}..{D1.date()} (paper, zero cost, price-only):")
print(f"  B1 CAGR {cagr:+.2f}%/yr (TR-adjusted ~{cagr+1.3:+.2f}%) vs >=15%: "
      f"{'PASS' if cagr >= 15 else ('PASS on TR' if cagr+1.3 >= 15 else 'MISS')}")
print(f"  B2 maxDD {dd:.2f}% vs <=15%: {'PASS' if dd >= -15 else 'MISS'}")
wy = yearly.min()
print(f"  B3 worst year {100*wy:+.1f}% ({yearly.idxmin().year}) vs >=-10%: {'PASS' if wy >= -0.10 else 'MISS'}")
print(f"  B4 era halves: 2011-16 {c1:+.2f}%/yr | 2017-23 {c2:+.2f}%/yr vs both >=10%: "
      f"{'PASS' if min(c1,c2) >= 10 else 'MISS'}")
print("  yearly:", {d.year: f"{100*x:+.1f}%" for d, x in yearly.items()})

# B5 attribution
for nm, s_ in [("core (80% vol-mgd NIFTY)", 0.8 * core_ret), ("switcher (20%)", 0.2 * sw_ret_d),
               ("option overlay", op_ret)]:
    ce = (1 + s_).cumprod()
    print(f"  B5 {nm}: contribution CAGR {100*(ce.iloc[-1]**(1/yrs)-1):+.2f}%/yr")
# reference: raw NIFTY
ne = (1 + r.loc[D0:D1].fillna(0)).cumprod()
print(f"  reference raw NIFTY: CAGR {100*(ne.iloc[-1]**(1/yrs)-1):+.2f}%, "
      f"maxDD {100*(ne/ne.cummax()-1).min():.1f}%")
print(f"  B6 frontier read: achieved ratio = {cagr/abs(dd):.2f} (target 1.0)")
