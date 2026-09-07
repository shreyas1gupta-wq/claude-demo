"""OP-D3 — integrated paper backtest of the OP-D2 design + the honest improvement grid.

Registered 2026-09-08 BEFORE this run (conventions/bars in the ledger). Prints only.
BS flat-sigma at India VIX, r=0.06, zero costs — paper best-case, stated.
"""
import sys

import numpy as np
import pandas as pd
from scipy.stats import norm

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

V = "/home/user/claude-demo/ingest/vault"
R = 0.06
BUDGETS = pd.to_datetime(["2011-02-28", "2012-03-16", "2013-02-28", "2014-02-17",
                          "2014-07-10", "2015-02-28", "2016-02-29", "2017-02-01",
                          "2018-02-01", "2019-02-01", "2019-07-05", "2020-02-01",
                          "2021-02-01", "2022-02-01", "2023-02-01"])

nf = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
vx = pd.read_csv(f"{V}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"]).set_index("date")["close"]
df = pd.DataFrame({"S": nf["Adj Close"], "vix": vx}).dropna()
df["pct"] = expanding_percentile(df.vix.to_numpy(), min_obs=252)
lr = np.log(df.S).diff()
ew = lr.pow(2).ewm(alpha=0.06).mean().pow(0.5) * np.sqrt(252)  # EWMA lambda=0.94
df["ewvol"] = ew
df = df.dropna(subset=["pct"])
DATES = df.index
no_entry = set()
for b in BUDGETS:
    i = DATES.searchsorted(b)
    for j in range(max(0, i - 2), min(len(DATES), i + 2)):
        no_entry.add(DATES[j])


def bs(S, K, T, sig, cp):
    if T <= 0:
        return max(0.0, cp * (S - K)), 0.0
    d1 = (np.log(S / K) + (R + 0.5 * sig**2) * T) / (sig * np.sqrt(T))
    d2 = d1 - sig * np.sqrt(T)
    if cp > 0:
        return S * norm.cdf(d1) - K * np.exp(-R * T) * norm.cdf(d2), norm.cdf(d1)
    return K * np.exp(-R * T) * norm.cdf(-d2) - S * norm.cdf(-d1), norm.cdf(d1) - 1


def last_thursday(y, m):
    d = pd.Timestamp(y, m, 1) + pd.offsets.MonthEnd(0)
    while d.weekday() != 3:
        d -= pd.Timedelta(days=1)
    return d


def make_legs(S, vix, exp_d, t, wing):
    T = max((exp_d - t).days, 1) / 365
    sg = vix / 100 * np.sqrt(T)
    return [(-1, S * (1 + sg), +1), (-1, S * (1 - sg), -1),
            (+1, S * (1 + wing * sg), +1), (+1, S * (1 - wing * sg), -1)], T


def price_legs(legs, S, vix, exp_d, t):
    T = max((exp_d - t).days, 0) / 365
    val = dlt = 0.0
    for q, K, cp in legs:
        p, d = bs(S, K, T, vix / 100, cp)
        val += q * p
        dlt += q * d
    return val, dlt


def run(entry_th, wing, roll_th, d0, d1, book0=100.0):
    book = book0
    eq = []
    pos = None
    rearm = True
    monthly = {}
    idx = df.loc[d0:d1]
    for t, row in idx.iterrows():
        S, vix, pct = row.S, row.vix, row.pct
        day_pnl = 0.0
        if pos:
            v, dlt = price_legs(pos["legs"], S, vix, pos["exp"], t)
            day_pnl = (v - pos["mark"]) * pos["units"]
            pos["mark"] = v
            closed = False
            if t >= pos["exp"]:
                closed = True
            elif pct >= 0.90:
                closed = True; rearm = False
            elif day_pnl / book <= -0.0222:
                closed = True; rearm = False
            elif abs(dlt) >= roll_th:
                if pos["rolls"] >= 3:
                    closed = True
                else:
                    legs, _ = make_legs(S, vix, pos["exp"], t, wing)
                    nv, _ = price_legs(legs, S, vix, pos["exp"], t)
                    pos.update(legs=legs, mark=nv, rolls=pos["rolls"] + 1)
            if closed:
                pos = None
        book += day_pnl
        if not rearm and pct < 0.60:
            rearm = True
        if pos is None and rearm and pct >= entry_th and t not in no_entry:
            em, ey = (t.month + 1, t.year) if t.month < 12 else (1, t.year + 1)
            exp_d = last_thursday(ey, em)
            if (exp_d - t).days < 15:
                em, ey = (em + 1, ey) if em < 12 else (1, ey + 1)
                exp_d = last_thursday(ey, em)
            legs, T = make_legs(S, vix, exp_d, t, wing)
            v0, _ = price_legs(legs, S, vix, exp_d, t)
            credit = -v0
            maxloss = (wing - 1) * (vix / 100 * np.sqrt(T)) * S - credit
            if maxloss <= 0:
                continue
            s_t = min(0.15 / max(row.ewvol, 1e-6), 2.0)
            f = min(0.150 * s_t, 0.10)
            units = f * book / maxloss
            pos = dict(legs=legs, exp=exp_d, units=units, mark=v0, rolls=0)
        eq.append((t, book))
        monthly.setdefault((t.year, t.month), []).append(book)
    e = pd.Series(dict(eq))
    mo = e.resample("ME").last().pct_change().dropna()
    yrs = (d1 - d0).days / 365.25
    geo = (e.iloc[-1] / e.iloc[0]) ** (1 / yrs) - 1
    dd = (e / e.cummax() - 1).min()
    return dict(geo=100 * geo, maxdd=100 * dd, worst_mo=100 * mo.min(),
                pos_mo=100 * (mo > 0).mean(), mo=mo, eq=e)


BASE = (0.60, 2.5, 0.30)
print("OP-D3a — INTEGRATED BASELINE (entry 0.60, wing 2.5, roll 0.30), 2011-07..2023-03:")
b = run(*BASE, pd.Timestamp("2011-07-01"), pd.Timestamp("2023-03-31"))
print(f"  book CAGR {b['geo']:+.2f}%/yr | maxDD {b['maxdd']:.2f}% | worst month {b['worst_mo']:+.2f}% | "
      f"months>0 {b['pos_mo']:.0f}%")
print("  b1 maxDD<=10%:", "PASS" if b["maxdd"] >= -10 else "MISS",
      "| b2 >=70% months+:", "PASS" if b["pos_mo"] >= 70 else "MISS",
      "| b3 >=+1%/yr:", "PASS" if b["geo"] >= 1.0 else "MISS",
      "| b4 worst>=-3.5%:", "PASS" if b["worst_mo"] >= -3.5 else "MISS")
yr = b["eq"].resample("YE").last().pct_change().dropna()
print("  b5 yearly:", {d.year: f"{100*x:+.1f}%" for d, x in yr.items()})

print("\nOP-D3b — TRAIN grid (2011-07..2016-12), objective = geo - 2|worst_mo|, maxDD<=10%:")
tr0, tr1 = pd.Timestamp("2011-07-01"), pd.Timestamp("2016-12-31")
te0, te1 = pd.Timestamp("2017-02-01"), pd.Timestamp("2023-03-31")  # 21td purge
best, best_obj = None, -1e9
for entry in (0.50, 0.60, 0.70):
    for wing in (2.0, 2.5, 3.0):
        for roll in (0.25, 0.30, 0.35):
            r_ = run(entry, wing, roll, tr0, tr1)
            obj = r_["geo"] - 2 * abs(r_["worst_mo"])
            ok = r_["maxdd"] >= -10
            print(f"  e{entry} w{wing} r{roll}: geo {r_['geo']:+5.2f} dd {r_['maxdd']:6.2f} "
                  f"worst {r_['worst_mo']:+5.2f} obj {obj:+6.2f}{' *' if ok else ' (DD fail)'}")
            if ok and obj > best_obj:
                best_obj, best = obj, (entry, wing, roll)
print(f"  SELECTED on train: entry {best[0]}, wing {best[1]}, roll {best[2]}")
sel_te = run(*best, te0, te1)
bas_te = run(*BASE, te0, te1)
print(f"  TEST validation: selected geo {sel_te['geo']:+.2f}/dd {sel_te['maxdd']:.2f} vs "
      f"baseline geo {bas_te['geo']:+.2f}/dd {bas_te['maxdd']:.2f}")
improved = sel_te["geo"] > bas_te["geo"] and sel_te["maxdd"] >= bas_te["maxdd"]
print(f"  VERDICT: {'IMPROVEMENT ACCEPTED — ' + str(best) if improved and best != BASE else 'NO IMPROVEMENT — BASELINE STANDS' if not improved else 'baseline re-selected'}")

FINAL = best if improved else BASE
print(f"\nOP-D3c — robustness of the standing choice {FINAL}:")
e1 = run(*FINAL, tr0, tr1)
e2 = run(*FINAL, te0, te1)
print(f"  era split: 2011-16 geo {e1['geo']:+.2f}/dd {e1['maxdd']:.2f} | 2017-23 geo {e2['geo']:+.2f}/dd {e2['maxdd']:.2f}")
full = run(*FINAL, pd.Timestamp("2011-07-01"), pd.Timestamp("2023-03-31"))
mo_x = full["mo"][~((full["mo"].index >= "2020-02-01") & (full["mo"].index <= "2020-06-30"))]
print(f"  ex-COVID: mean month {100*mo_x.mean():+.3f}% vs incl {100*full['mo'].mean():+.3f}%; "
      f"worst ex-COVID {100*mo_x.min():+.2f}%")
for rr in (0.05, 0.07):
    globals()["R"] = rr
    rv = run(*FINAL, pd.Timestamp("2011-07-01"), pd.Timestamp("2023-03-31"))
    print(f"  r={rr}: geo {rv['geo']:+.2f}%/yr dd {rv['maxdd']:.2f}%")
globals()["R"] = 0.06
