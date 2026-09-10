"""ES-D2 (2026-09-10) — THE REVISION-PROXY INTERACTION MATRICES (extension of ES-D1).
Registered verbatim in research/register/trial-ledger.md, entry "ES-D2 (2026-09-10)",
BEFORE this run. Runs the parent ES-D1 idioms (scripts/analyze_es_sc.py) unchanged:
d3(Eps) via calendar-aligned pivot/shift(3)/stack/join; dec(s,n) = ceil(pct-rank*n)
clipped to [1,n], computed PER DATE via groupby("date").transform; EW (equal-weight)
portfolio means; annualization fwd-1m mean x1200 (%/yr), fwd-12m mean x100 (%/yr).
Forward-return convention: firm_panel row t's R1M_Usd/R12M_Usd already realize
t+1..t+h (vault AUTH) — NOT shifted again here.

Print-only. No interpretation. The desk writes interpretation after the print
(process note #5 / CONTRACT.md rules for research agents).
"""
import json
import os

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
OUT = "/home/user/claude-demo/research/notes/es_sc_matrices/es_d2.json"

# ---------------- firm panel ----------------
use = ["stock_id", "date", "Eps", "Pb", "Mom_11M_Usd", "Mkt_Cap_12M_Usd",
       "Roe", "Vol1Y_Usd", "R1M_Usd", "R12M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use,
                 parse_dates=["date"])

# d3(Eps): calendar-aligned pivot, shift(3), stack back, join (parent idiom, verbatim).
eps = fp.pivot_table(index="date", columns="stock_id", values="Eps")
d3 = (eps - eps.shift(3)).stack().rename("d3")
fp = fp.set_index(["date", "stock_id"]).join(d3).reset_index()


def dec(s, n=10):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


# Independent per-date quintiles (n=5) for d3 and each interaction variable.
fp["d3_q"] = fp.groupby("date").d3.transform(dec, n=5)
for var in ["Pb", "Mom_11M_Usd", "Mkt_Cap_12M_Usd", "Roe", "Vol1Y_Usd"]:
    fp[f"{var}_q"] = fp.groupby("date")[var].transform(dec, n=5)


def grid_1m(row_col, col_col):
    g = fp.groupby([row_col, col_col]).R1M_Usd.mean().unstack() * 1200
    return [[round(g.loc[r, c], 2) for c in range(1, 6)] for r in range(1, 6)]


def grid_12m(row_col, col_col):
    g = fp.groupby([row_col, col_col]).R12M_Usd.mean().unstack() * 100
    return [[round(g.loc[r, c], 2) for c in range(1, 6)] for r in range(1, 6)]


out = {}

print("ES-D2 — revision-proxy interaction matrices (EW, ann. %/yr; rows d3(Eps) Q1..Q5,"
      " cols var Q1..Q5, independent per-date sorts):")

cells_1m = [
    ("m1", "d3(Eps) x Pb, fwd-1m", "Pb_q"),
    ("m2", "d3(Eps) x Mom_11M_Usd, fwd-1m", "Mom_11M_Usd_q"),
    ("m3", "d3(Eps) x Mkt_Cap_12M_Usd, fwd-1m", "Mkt_Cap_12M_Usd_q"),
    ("m4", "d3(Eps) x Roe, fwd-1m", "Roe_q"),
    ("m5", "d3(Eps) x Vol1Y_Usd, fwd-1m", "Vol1Y_Usd_q"),
]
for key, label, col in cells_1m:
    g = grid_1m("d3_q", col)
    out[key] = {"rows": "d3 quintile 1..5", "cols": f"{col.replace('_q','')} quintile 1..5", "grid": g}
    print(f"  {key} {label}:")
    for i, r in enumerate(g, 1):
        print(f"    d3 Q{i}: " + " ".join(f"{v:+.2f}" for v in r))

# m6 = m1 at fwd-12m
g6 = grid_12m("d3_q", "Pb_q")
out["m6"] = {"rows": "d3 quintile 1..5", "cols": "Pb quintile 1..5", "grid": g6}
print("  m6 d3(Eps) x Pb, fwd-12m:")
for i, r in enumerate(g6, 1):
    print(f"    d3 Q{i}: " + " ".join(f"{v:+.2f}" for v in r))


def corner_numbers(df):
    cheap_improving = df[(df.Pb_q.isin([1, 2])) & (df.d3_q.isin([4, 5]))]
    cheap_alone = df[df.Pb_q.isin([1, 2])]
    exp_deteriorating = df[(df.Pb_q.isin([4, 5])) & (df.d3_q.isin([1, 2]))]
    a1 = cheap_improving.R1M_Usd.mean() * 1200
    b1 = cheap_alone.R1M_Usd.mean() * 1200
    c1 = exp_deteriorating.R1M_Usd.mean() * 1200
    a12 = cheap_improving.R12M_Usd.mean() * 100
    b12 = cheap_alone.R12M_Usd.mean() * 100
    c12 = exp_deteriorating.R12M_Usd.mean() * 100
    return {
        "cheap_improving_1m": round(a1, 2), "cheap_alone_1m": round(b1, 2),
        "expensive_deteriorating_1m": round(c1, 2), "corner_increment_1m": round(a1 - b1, 2),
        "cheap_improving_12m": round(a12, 2), "cheap_alone_12m": round(b12, 2),
        "expensive_deteriorating_12m": round(c12, 2), "corner_increment_12m": round(a12 - b12, 2),
        "n_cheap_improving": int(len(cheap_improving)), "n_cheap_alone": int(len(cheap_alone)),
        "n_expensive_deteriorating": int(len(exp_deteriorating)),
    }


m7 = corner_numbers(fp)
out["m7"] = m7
print("  m7 corner read (EW ann %, all size):")
print(f"    cheap+improving   1m {m7['cheap_improving_1m']:+.2f} | 12m {m7['cheap_improving_12m']:+.2f}  (n={m7['n_cheap_improving']})")
print(f"    cheap-alone       1m {m7['cheap_alone_1m']:+.2f} | 12m {m7['cheap_alone_12m']:+.2f}  (n={m7['n_cheap_alone']})")
print(f"    expensive+deteriorating 1m {m7['expensive_deteriorating_1m']:+.2f} | 12m {m7['expensive_deteriorating_12m']:+.2f}  (n={m7['n_expensive_deteriorating']})")
print(f"    corner increment (a-b) 1m {m7['corner_increment_1m']:+.2f} | 12m {m7['corner_increment_12m']:+.2f}"
      f"  (consumption gate: 1m >= +2.00)")

top_size = fp[fp.Mkt_Cap_12M_Usd_q == 5]
m8 = corner_numbers(top_size)
out["m8"] = m8
print("  m8 corner read, restricted to top size quintile (Mkt_Cap_12M_Usd_q == 5):")
print(f"    cheap+improving   1m {m8['cheap_improving_1m']:+.2f} | 12m {m8['cheap_improving_12m']:+.2f}  (n={m8['n_cheap_improving']})")
print(f"    cheap-alone       1m {m8['cheap_alone_1m']:+.2f} | 12m {m8['cheap_alone_12m']:+.2f}  (n={m8['n_cheap_alone']})")
print(f"    expensive+deteriorating 1m {m8['expensive_deteriorating_1m']:+.2f} | 12m {m8['expensive_deteriorating_12m']:+.2f}  (n={m8['n_expensive_deteriorating']})")
print(f"    corner increment (a-b) 1m {m8['corner_increment_1m']:+.2f} | 12m {m8['corner_increment_12m']:+.2f}")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(out, f, indent=2)
print(f"\n[written] {OUT}")
