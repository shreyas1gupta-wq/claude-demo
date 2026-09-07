"""SEC-D7 — stock-level leverage decomposition (measured beta/vol quintiles + declared
financial-leverage and operating-leverage baskets).

Registered 2026-09-07 BEFORE this run; lists, quintile machinery and bars live in the
ledger. Reuses the SEC-D1 panel/episode machinery (import re-echoes its prints — run
note). Prints only.
"""
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from scripts.analyze_sec_battery import EPISODES, ret, mkt  # noqa: E402

STRESS = ["E1 TAPER (ccy)", "E3 NBFC (credit)", "E4 COVID (crisis)", "E5 INR+OIL (ccy)"]
RECOV = "E4b RECOVERY"
WEAK_INR = [2013, 2015, 2018]
RISING_RF = [2013, 2014, 2018]
YEARS = list(range(2013, 2022))

HIGH_FL = ["GMRINFRA", "ADANIPOWER", "ADANIENT", "DLF", "JSWENERGY", "TATAPOWER",
           "TATASTEEL", "JSWSTEEL", "JINDALSTEL", "VEDL", "BHARTIARTL", "IDEA",
           "TATAMOTORS", "SAIL", "ASHOKLEY", "LEMONTREE", "INDHOTEL", "ADANIGREEN", "IRB"]
LOW_FL = ["TCS", "INFY", "WIPRO", "HCLTECH", "ITC", "HINDUNILVR", "COLPAL", "CASTROLIND",
          "PAGEIND", "PIDILITIND", "ASIANPAINT", "BERGEPAINT", "DABUR", "MARICO",
          "BAJAJ-AUTO", "HEROMOTOCO", "EICHERMOT", "DIVISLAB", "AKZOINDIA", "GILLETTE",
          "3MINDIA", "HONAUT", "OFSS", "MPHASIS"]
HIGH_OL = ["INDHOTEL", "LEMONTREE", "EIHOTEL", "INDIGO", "PVR", "ULTRACEMCO", "ACC",
           "AMBUJACEM", "SHREECEM", "TATASTEEL", "JSWSTEEL", "SAIL", "JINDALSTEL",
           "TATAMOTORS", "ASHOKLEY", "BHEL", "MHRIL"]
LOW_OL = ["TCS", "INFY", "WIPRO", "HCLTECH", "TECHM", "MPHASIS", "HINDUNILVR", "ITC",
          "DABUR", "MARICO", "GODREJCP", "BRITANNIA", "PIDILITIND", "ASIANPAINT",
          "BERGEPAINT", "COLPAL", "EMAMILTD", "JYOTHYLAB"]


def basket_ret(names):
    return ret[[t for t in names if t in ret.columns]].mean(axis=1)


def window_rel(r, a, b):
    w = (r - mkt).loc[a:b].dropna()
    return float((1 + w).prod() - 1) if len(w) else np.nan


def annual_rel(r):
    x = (r - mkt).dropna()
    return (1 + x).groupby(x.index.year).prod() - 1


def cagr(r):
    x = r.dropna()
    return float(np.expm1(np.log1p(x).mean() * 252))


def stress_comp(r):
    eps = {lab: (a, b) for lab, a, b in EPISODES}
    return float(np.mean([window_rel(r, *eps[e]) for e in STRESS]))


def state_diff(r, on_years, off_years):
    y = annual_rel(r)
    return float(y.reindex(on_years).mean() - y.reindex(off_years).mean())


# ---- D7a: measured quintiles ----
assign = {}
for y in YEARS:
    win = ret.loc[f"{y-1}-01-01":f"{y-1}-12-31"]
    ok = win.count() >= 150
    w = win.loc[:, ok]
    m = w.mean(axis=1)
    beta = w.apply(lambda s: s.cov(m) / m.var())
    vol = w.std()
    assign[y] = (pd.qcut(beta.rank(method="first"), 5, labels=False),
                 pd.qcut(vol.rank(method="first"), 5, labels=False))


def quintile_series(which):
    out = {}
    for q in range(5):
        parts = []
        for y in YEARS:
            names = assign[y][which][assign[y][which] == q].index
            parts.append(ret.loc[f"{y}-01-01":f"{y}-12-31", names].mean(axis=1))
        out[q] = pd.concat(parts).sort_index()
    return out


for which, tag in [(0, "BETA"), (1, "VOL")]:
    qs = quintile_series(which)
    print(f"\nSEC-D7a — {tag} QUINTILES (formed on trailing year, held 1y, 2013-2021):")
    print(f"  {'Q':>3} {'full CAGR':>10} {'stress comp':>12} {'E4b recov':>10} "
          f"{'weakINR diff':>13} {'risingRF diff':>14}")
    eps = {lab: (a, b) for lab, a, b in EPISODES}
    for q in range(5):
        r = qs[q]
        print(f"  Q{q+1:>2} {100*cagr(r):>9.1f}% {100*stress_comp(r):>+11.1f} "
              f"{100*window_rel(r, *eps[RECOV]):>+9.1f} "
              f"{100*state_diff(r, WEAK_INR, [y for y in YEARS if y not in WEAK_INR]):>+12.1f} "
              f"{100*state_diff(r, RISING_RF, [y for y in YEARS if y not in RISING_RF]):>+13.1f}")

# ---- D7b / D7c: declared baskets ----
print("\nSEC-D7b/c — DECLARED BASKETS:")
eps = {lab: (a, b) for lab, a, b in EPISODES}
rows = {}
for nm, lst in [("HIGH-FL", HIGH_FL), ("LOW-FL", LOW_FL),
                ("HIGH-OL", HIGH_OL), ("LOW-OL", LOW_OL)]:
    r = basket_ret(lst)
    rows[nm] = r
    print(f"  {nm:8} n={len([t for t in lst if t in ret.columns]):2} | full CAGR "
          f"{100*cagr(r):>6.1f}%/yr | stress comp {100*stress_comp(r):>+6.1f} | "
          f"E4b {100*window_rel(r, *eps[RECOV]):>+6.1f} | "
          f"weakINR diff {100*state_diff(r, WEAK_INR, [y for y in YEARS if y not in WEAK_INR]):>+6.1f} | "
          f"risingRF diff {100*state_diff(r, RISING_RF, [y for y in YEARS if y not in RISING_RF]):>+6.1f}")

print("\n  b3 per-episode REL table (pp):")
print(f"  {'episode':>18} {'HIGH-FL':>8} {'LOW-FL':>8} {'HIGH-OL':>8} {'LOW-OL':>8}")
for lab, a, b in EPISODES:
    print(f"  {lab:>18} " + " ".join(f"{100*window_rel(rows[nm], a, b):>+8.1f}"
                                     for nm in ("HIGH-FL", "LOW-FL", "HIGH-OL", "LOW-OL")))

for nm in ("HIGH-FL", "HIGH-OL"):
    sc = stress_comp(rows[nm])
    rec = window_rel(rows[nm], *eps[RECOV])
    print(f"  convexity {nm}: stress {100*sc:+.1f} + recovery {100*rec:+.1f} = "
          f"{100*(sc+rec):+.1f}pp")

print("\n  spreads: b1 full-CAGR LOW-FL minus HIGH-FL = "
      f"{100*(cagr(rows['LOW-FL'])-cagr(rows['HIGH-FL'])):+.1f}pp/yr | "
      f"b2 stress HIGH-FL minus LOW-FL = "
      f"{100*(stress_comp(rows['HIGH-FL'])-stress_comp(rows['LOW-FL'])):+.1f}pp | "
      f"c2 stress HIGH-OL minus LOW-OL = "
      f"{100*(stress_comp(rows['HIGH-OL'])-stress_comp(rows['LOW-OL'])):+.1f}pp")
