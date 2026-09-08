"""OP-D6b — CORRECTION LEG. Registered 2026-09-08 BEFORE this run.

Two implementation errors found by directed audit ("check for errors"), both confirmed
by magnitude diagnostics before registration:
  E1 month-drop: monthly sleeves marked at CALENDAR month-ends -> 44/141 months (31%)
     silently zeroed. Fix: mark at the LAST TRADING DAY of each month.
  E2 free leverage: core expo>1.0x on 57% of days with no financing. Fix: subtract
     r=0.06 x (expo-1)+ daily (declared paper funding rate pending funding_rate config).
Re-runs OP-D4 (E1), OP-D5 (E1), OP-D6 (E1), OP-D6 (E1+E2 = the honest baseline).
Bars re-read, never moved. Prints only. This file doubles as the shared book engine
for OP-D7 (exec-split at the MAIN marker, house pattern).
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
sd_full = pct_s.reindex(S_.index).ffill()

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

ii = pd.read_csv(f"{V}/factors/iima_monthly_factors.csv", na_values=["NA"])
ii["d"] = pd.to_datetime(ii["Date"]) + pd.offsets.MonthEnd(0)
ii = ii.set_index("d")
fac = (0.5 * (ii["WML"] + ii["HML"]) / 100).dropna()
fvol = fac.pow(2).ewm(alpha=0.06).mean().pow(0.5) * np.sqrt(12)
flev = (0.15 / fvol).clip(upper=2.0).shift(1)
fac_vm = (flev * fac).dropna()

# dates + E1 fix: calendar ME -> last trading day of that month
dates = r_.loc[D0:D1].index
_g = pd.Series(dates, index=dates).groupby([dates.year, dates.month]).last()
ME_MAP = {pd.Timestamp(y, m, 1) + pd.offsets.MonthEnd(0): t for (y, m), t in _g.items()}


def month_stream(monthly, fix=True):
    """Place monthly returns on the daily index. fix=True -> last trading day (E1 fix);
    fix=False -> the buggy calendar-ME placement (for like-for-like deltas)."""
    out = pd.Series(0.0, index=dates)
    for me in n_me.loc[D0:D1].index:
        v = monthly.get(me, np.nan)
        if pd.isna(v):
            continue
        t = ME_MAP.get(me) if fix else (me if me in out.index else None)
        if t is not None:
            out.loc[t] = v
    return out


# switcher monthly returns keyed by calendar ME (signal from prior ME — unchanged)
_sw = {}
for me in n_me.loc[D0:D1].index:
    prev = mom_n.index[mom_n.index < me]
    if not len(prev):
        continue
    sig_d = prev[-1]
    _sw[me] = g_ret_m.get(me, 0.0) if mom_g.get(sig_d, -9) > mom_n.get(sig_d, -9) else n_ret_m.get(me, 0.0)
SW_M = pd.Series(_sw)


def core_stream(cap=1.5, financing=False):
    expo = (0.15 / ewvol).clip(upper=cap)
    expo = expo * np.where(sd_full >= 0.90, 0.5, 1.0)
    ret = (expo.shift(1) * r_).loc[D0:D1].fillna(0)
    if financing:
        ret = ret - ((expo.shift(1) - 1).clip(lower=0) * R / 252).loc[D0:D1].fillna(0)
    return ret, expo


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


# condor sleeve (OP-D3 verbatim) — book-relative, computed once
_src = open("/home/user/claude-demo/scripts/analyze_op_d3.py").read()
_ns = {}
exec(_src.split("BASE = ")[0], _ns)
OP_RET = _ns["run"](0.60, 2.5, 0.30, D0, D1)["eq"].pct_change().reindex(dates).fillna(0)

DF2 = pd.DataFrame({"S": S_, "vix": vx}).reindex(dates).ffill()


def run_book(core_w, sw_w, fac_w, cap=1.5, financing=False, overlays=True,
             fac_monthly=None, syn_margin=False, extra_ret=None, extra_margin=None,
             fac_margin_rate=None):
    """The stacked book, daily loop (OP-D5 mechanics). extra_ret/extra_margin: optional
    book-relative daily return / margin-fraction streams (weekly sleeve, MR overlay).
    fac_margin_rate (SW2-A1): margin rate applied to the factor sleeve's GROSS notional
    (fac_w x 2 x lagged monthly leverage x book) — the f15 audit found this line missing;
    None (default) preserves reproduction of prints booked before 2026-09-08."""
    core_ret, expo = core_stream(cap, financing)
    sw_d = month_stream(SW_M)
    fac_d = month_stream(fac_monthly if fac_monthly is not None else fac_vm) \
        if fac_w > 0 else pd.Series(0.0, index=dates)
    exl = expo.shift(1)
    flev_d = flev.reindex(dates, method="ffill") if fac_margin_rate else None
    book = 100.0
    eq_rows = []
    put = None
    cc = None
    peak_margin = 0.0
    for t in dates:
        S, vix = DF2.S[t], DF2.vix[t]
        p = pct_s.reindex([t]).ffill().iloc[0]
        day = book * (core_w * core_ret[t] + sw_w * sw_d[t] + fac_w * fac_d[t] + OP_RET[t])
        if extra_ret is not None:
            day += book * extra_ret[t]
        if overlays:
            if put is not None:
                T = max((put["exp"] - t).days, 0) / 365
                v = bsv(S, put["K"], T, vix / 100, -1)
                day += (v - put["mark"]) * put["units"]
                put["mark"] = v
                if (put["exp"] - t).days <= 30:
                    put = None
            if put is None:
                e_t = exl.get(t, 1.0)
                core_notional = core_w * (1.0 if pd.isna(e_t) else float(e_t)) * book
                K = S * 0.95
                v0 = bsv(S, K, 91 / 365, vix / 100, -1)
                put = dict(K=K, exp=t + pd.Timedelta(days=91), units=core_notional / S, mark=v0)
            if cc is not None:
                T = max((cc["exp"] - t).days, 0) / 365
                v = bsv(S, cc["K"], T, vix / 100, +1)
                day += -(v - cc["mark"]) * cc["units"]
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
                cc = dict(K=K, exp=exp_d, units=0.5 * core_w * book / S, mark=v0)
        book += day
        m = 0.025 * 1.1 * book  # condor approx (declared, OP-D5 verbatim)
        if cc is not None:
            m += 0.025 * cc["units"] * S
        if put is not None:
            m += put["mark"] * put["units"]
        if syn_margin:
            e_t = exl.get(t, 1.0)
            m += 0.10 * max((0.0 if pd.isna(e_t) else float(e_t)) - 1, 0) * core_w * book
        if extra_margin is not None:
            m += extra_margin[t] * book
        if fac_margin_rate:
            fl = flev_d.get(t, np.nan)
            m += fac_margin_rate * fac_w * 2 * (0.0 if pd.isna(fl) else float(fl)) * book
        peak_margin = max(peak_margin, m / book)
        eq_rows.append((t, book))
    return pd.Series(dict(eq_rows)), peak_margin


def stats_of(eq, d0=D0, d1=D1):
    # 2026-09-08 machinery fix (SW-2/f07 verifier): d0/d1 previously set only the
    # year-count while the equity ratio stayed full-period — now the curve is sliced.
    # No booked print used non-default d0/d1 (OP-D7 used its own win_stats).
    eq = eq.loc[d0:d1]
    yrs = (eq.index[-1] - eq.index[0]).days / 365.25
    cagr = 100 * ((eq.iloc[-1] / eq.iloc[0]) ** (1 / yrs) - 1)
    dd = 100 * (eq / eq.cummax() - 1).min()
    yearly = eq.resample("YE").last().pct_change().dropna()
    return cagr, dd, yearly


# === MAIN ===
if __name__ == "__main__":
    print("OP-D6b — THE CORRECTION LEG (E1 month-drop fix; E2 financing fix), "
          f"{D0.date()}..{D1.date()}:")
    print("  a1 magnitude: 44/141 months (31%) were zeroed in the monthly sleeves; core "
          "levered >1x on 57% of days, ~0.95%/yr of core notional unfinanced")

    # a2: OP-D4 with E1 (no overlays — D4 verbatim composition, returns-based)
    core_ret, _ = core_stream(1.5, False)
    br = 0.8 * core_ret + 0.2 * month_stream(SW_M) + OP_RET
    eq4 = (1 + br).cumprod() * 100
    c4, d4, _ = stats_of(eq4)
    print(f"  a2 OP-D4+E1: CAGR {c4:+.2f} (booked +9.86, d {c4-9.86:+.2f}pp) | "
          f"maxDD {d4:.2f} (booked -22.71) | bars B1(>=15) "
          f"{'PASS' if c4 >= 15 else 'MISS'}, B2(<=15) {'PASS' if d4 >= -15 else 'MISS'}")

    # a3: OP-D5 with E1
    eq5, pm5 = run_book(0.8, 0.2, 0.0)
    c5, d5, y5 = stats_of(eq5)
    print(f"  a3 OP-D5+E1: CAGR {c5:+.2f} TR~{c5+1.3:+.2f} (booked +10.08) | maxDD {d5:.2f} "
          f"(booked -16.04) | worst yr {100*y5.min():+.1f} ({y5.idxmin().year}) | "
          f"s1 {'PASS' if c5 >= 15 else ('PASS on TR' if c5+1.3 >= 15 else 'MISS')}, "
          f"s2 {'PASS' if d5 >= -15 else 'MISS'}")

    # a4: OP-D6 with E1
    eq6, pm6 = run_book(0.65, 0.20, 0.15)
    c6, d6, y6 = stats_of(eq6)
    print(f"  a4 OP-D6+E1: CAGR {c6:+.2f} TR~{c6+1.3:+.2f} (booked +10.74) | maxDD {d6:.2f} "
          f"(booked -10.47) | worst yr {100*y6.min():+.1f} ({y6.idxmin().year}) | "
          f"s1 {'PASS' if c6 >= 15 else ('PASS on TR' if c6+1.3 >= 15 else 'MISS')}, "
          f"s2 {'PASS' if d6 >= -15 else 'MISS'}")

    # a5: OP-D6 with E1+E2 — THE HONEST BASELINE (financing + synthetic margin on the levered core)
    eq6f, pm6f = run_book(0.65, 0.20, 0.15, financing=True, syn_margin=True)
    c6f, d6f, y6f = stats_of(eq6f)
    h1, h2 = eq6f.loc[:"2016-12-31"], eq6f.loc["2017-01-01":]
    e1 = 100 * ((h1.iloc[-1] / h1.iloc[0]) ** (365.25 / (h1.index[-1] - h1.index[0]).days) - 1)
    e2 = 100 * ((h2.iloc[-1] / h2.iloc[0]) ** (365.25 / (h2.index[-1] - h2.index[0]).days) - 1)
    print(f"  a5 OP-D6+E1+E2 (THE HONEST BASELINE): CAGR {c6f:+.2f} TR~{c6f+1.3:+.2f} | "
          f"maxDD {d6f:.2f} | worst yr {100*y6f.min():+.1f} ({y6f.idxmin().year}) | "
          f"peak margin {100*pm6f:.1f}% | eras {e1:+.2f}/{e2:+.2f} | "
          f"s1 {'PASS' if c6f >= 15 else ('PASS on TR' if c6f+1.3 >= 15 else 'MISS')}, "
          f"s2 {'PASS' if d6f >= -15 else 'MISS'}, s6 {'PASS' if y6f.min() >= -0.10 else 'MISS'}")
    print("  yearly a5:", {d.year: f"{100*x:+.1f}%" for d, x in y6f.items()})
