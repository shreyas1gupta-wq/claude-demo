"""OP-D5 — the stacked multi-strategy book under the principal's margin model.

Registered 2026-09-08 BEFORE this run. Core = OP-D4 verbatim; overlays: permanent 91d
5%-OTM put ladder (rolled at 30d), covered calls (1m 1-sigma OTM on 50% core notional
when VIX-pct >= 0.60), OP-D3 condor sleeve. BS flat-sigma at India VIX, r=0.06, zero
costs, price-only core (+1.3pp TR note). Margin model: hedged 2.5% notional, unhedged
10%, longs = premium; pledge haircut 10% stated. Prints only.
"""
import sys

import numpy as np
import pandas as pd
from scipy.stats import norm

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

V = "/home/user/claude-demo/ingest/vault"
D0, D1 = pd.Timestamp("2011-07-01"), pd.Timestamp("2023-03-31")
R = 0.06

nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
S_ = nf["Adj Close"]
r_ = S_.pct_change()
lr = np.log(S_).diff()
ewvol = lr.pow(2).ewm(alpha=0.06).mean().pow(0.5) * np.sqrt(252)
vx = pd.read_csv(f"{V}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"]).set_index("date")["close"]
pct_s = pd.Series(expanding_percentile(vx.to_numpy(), min_obs=252), index=vx.index)

gold = pd.read_csv(f"{V}/commodities/gold_monthly_1833_2026.csv")
gold.columns = [c.strip().lower() for c in gold.columns]
dcol = [c for c in gold.columns if "date" in c or "month" in c or "year" in c][0]
pcol = [c for c in gold.columns if c != dcol][0]
gold["d"] = pd.to_datetime(gold[dcol])
g_us = gold.set_index("d")[pcol]
inr = pd.read_csv(f"{V}/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"]).set_index("Date")["INR_per_USD"]
g_inr = (g_us * inr.reindex(g_us.index, method="nearest")).resample("ME").last().dropna()
n_me = S_.resample("ME").last()
mom_g, mom_n = g_inr.pct_change(12), n_me.pct_change(12)
g_ret_m, n_ret_m = g_inr.pct_change(), n_me.pct_change()


def bsv(S, K, T, sig, cp):
    if T <= 0:
        return max(0.0, cp * (S - K))
    d1 = (np.log(S / K) + (R + 0.5 * sig**2) * T) / (sig * np.sqrt(T))
    d2 = d1 - sig * np.sqrt(T)
    if cp > 0:
        return S * norm.cdf(d1) - K * np.exp(-R * T) * norm.cdf(d2)
    return K * np.exp(-R * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


def last_thursday(y, m):
    d = pd.Timestamp(y, m, 1) + pd.offsets.MonthEnd(0)
    while d.weekday() != 3:
        d -= pd.Timedelta(days=1)
    return d


# ---- core (OP-D4 verbatim, returns-based) ----
expo = (0.15 / ewvol).clip(upper=1.5)
sd = pct_s.reindex(S_.index).ffill()
expo = (expo * np.where(sd >= 0.90, 0.5, 1.0))
core_ret = (expo.shift(1) * r_).loc[D0:D1].fillna(0)
dates = core_ret.index
sw_ret_d = pd.Series(0.0, index=dates)
for me in n_me.loc[D0:D1].index:
    prev = mom_n.index[mom_n.index < me]
    if not len(prev):
        continue
    sig_d = prev[-1]
    mret = g_ret_m.get(me, 0.0) if mom_g.get(sig_d, -9) > mom_n.get(sig_d, -9) else n_ret_m.get(me, 0.0)
    if me in sw_ret_d.index and not pd.isna(mret):
        sw_ret_d.loc[me] = mret

# ---- condor sleeve (OP-D3 verbatim) ----
src = open("/home/user/claude-demo/scripts/analyze_op_d3.py").read()
ns = {}
exec(src.split("BASE = ")[0], ns)
op = ns["run"](0.60, 2.5, 0.30, D0, D1)
op_ret = op["eq"].pct_change().reindex(dates).fillna(0)

# ---- daily loop: book with put ladder + covered calls ----
book = 100.0
eq_rows = []
put = None      # dict(K, exp, units, mark)
cc = None       # dict(K, exp, units, mark)
put_cost_total = 0.0
put_pnl_2020 = 0.0
cc_pnl_total = 0.0
peak_margin = 0.0
df2 = pd.DataFrame({"S": S_, "vix": vx}).reindex(dates).ffill()
core_w = 0.8

for t in dates:
    S, vix = df2.S[t], df2.vix[t]
    p = pct_s.reindex([t]).ffill().iloc[0]
    day = book * (core_w * core_ret[t] + 0.2 * sw_ret_d[t] + op_ret[t])
    # put ladder mark
    if put is not None:
        T = max((put["exp"] - t).days, 0) / 365
        v = bsv(S, put["K"], T, vix / 100, -1)
        pnl = (v - put["mark"]) * put["units"]
        day += pnl
        if t.year == 2020:
            put_pnl_2020 += pnl
        put["mark"] = v
        if (put["exp"] - t).days <= 30:
            put_cost_total += put["cost"] - v * put["units"] / max(put["units"], 1e-12) * put["units"] / put["units"]  # realized below
            put = None
    if put is None:
        core_notional = core_w * float(expo.shift(1).get(t, 1.0) or 1.0) * book
        exp_d = t + pd.Timedelta(days=91)
        K = S * 0.95
        v0 = bsv(S, K, 91 / 365, vix / 100, -1)
        units = core_notional / S
        put = dict(K=K, exp=exp_d, units=units, mark=v0, cost=v0 * units)
        put_cost_total += v0 * units
    # covered call
    if cc is not None:
        T = max((cc["exp"] - t).days, 0) / 365
        v = bsv(S, cc["K"], T, vix / 100, +1)
        pnl = -(v - cc["mark"]) * cc["units"]
        day += pnl
        cc_pnl_total += pnl
        cc["mark"] = v
        if t >= cc["exp"]:
            cc = None
    if cc is None and p >= 0.60:
        em, ey = (t.month + 1, t.year) if t.month < 12 else (1, t.year + 1)
        exp_d = last_thursday(ey, em)
        if (exp_d - t).days < 15:
            em, ey = (em + 1, ey) if em < 12 else (1, ey + 1)
            exp_d = last_thursday(ey, em)
        Tm = (exp_d - t).days / 365
        K = S * (1 + vix / 100 * np.sqrt(Tm))
        v0 = bsv(S, K, Tm, vix / 100, +1)
        units = 0.5 * core_w * book / S
        cc = dict(K=K, exp=exp_d, units=units, mark=v0)
    book += day
    # margin utilization (principal's model): hedged shorts 2.5% notional; put = premium
    m = 0.0
    if cc is not None:
        m += 0.025 * cc["units"] * S
    if put is not None:
        m += put["mark"] * put["units"]
    m += 0.025 * 1.1 * book  # condor sleeve notional ~1.1x book at cap (hedged) — declared approx
    peak_margin = max(peak_margin, m / book)
    eq_rows.append((t, book))

eq = pd.Series(dict(eq_rows))
yrs = (D1 - D0).days / 365.25
cagr = 100 * ((eq.iloc[-1] / eq.iloc[0]) ** (1 / yrs) - 1)
dd = 100 * (eq / eq.cummax() - 1).min()
yearly = eq.resample("YE").last().pct_change().dropna()
h1, h2 = eq.loc[:"2016-12-31"], eq.loc["2017-01-01":]
c1 = 100 * ((h1.iloc[-1] / h1.iloc[0]) ** (365.25 / (h1.index[-1] - h1.index[0]).days) - 1)
c2 = 100 * ((h2.iloc[-1] / h2.iloc[0]) ** (365.25 / (h2.index[-1] - h2.index[0]).days) - 1)

print(f"OP-D5 — THE STACKED BOOK, {D0.date()}..{D1.date()} (paper, zero cost, price-only core):")
print(f"  s1 CAGR {cagr:+.2f}%/yr (TR ~{cagr+1.3:+.2f}%) vs >=15%: "
      f"{'PASS' if cagr >= 15 else ('PASS on TR' if cagr + 1.3 >= 15 else 'MISS')}")
print(f"  s2 maxDD {dd:.2f}% vs <=15%: {'PASS' if dd >= -15 else 'MISS'}")
print(f"  s3 put ladder: gross premium paid {100*put_cost_total/100:.1f} (index pts eq); "
      f"2020 ladder P&L {put_pnl_2020:+.2f} book-pts")
print(f"  s4 covered calls: total P&L {cc_pnl_total:+.2f} book-pts "
      f"({cc_pnl_total/yrs:+.2f}/yr)")
print(f"  s5 peak margin+premium utilization: {100*peak_margin:.1f}% of book "
      f"(prior <20%): {'PASS' if peak_margin < 0.20 else 'MISS'}")
wy = yearly.min()
print(f"  s6 worst year {100*wy:+.1f}% ({yearly.idxmin().year}) vs >=-10%: "
      f"{'PASS' if wy >= -0.10 else 'MISS'}")
print(f"  s7 era halves: {c1:+.2f} / {c2:+.2f} %/yr")
print("  yearly:", {d.year: f"{100*x:+.1f}%" for d, x in yearly.items()})
print(f"  s8 vs OP-D4 (+9.86/-22.71): dCAGR {cagr-9.86:+.2f}pp, dDD {dd-(-22.71):+.2f}pp")
