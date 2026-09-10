"""SC-D5 (size x value and size x momentum joint matrices).
Registered 2026-09-10 BEFORE this run (research/register/trial-ledger.md, entry
"SC-D5 (2026-09-10)"). Run VERBATIM per that registration — no changes to any bar,
bucket, or horizon. Prints only; interpretation is hand-appended to the ledger AFTER
the print, per CONTRACT.md process discipline.

Conventions (identical to scripts/analyze_es_sc.py):
  dec(s, n=5) = np.ceil(s.rank(pct=True) * 5).clip(1, 5), applied per date via
  groupby("date").transform — INDEPENDENT sorts (size and Pb/Mom each dec'd per
  date over the full cross-section, not nested). EW means. Annualization: x1200
  for fwd-1m, x400 for fwd-3m, x100 for fwd-12m. Forward returns (R1M_Usd,
  R3M_Usd, R12M_Usd) are already forward per the vault AUTH — not shifted.

Cells: j1 size x Pb 5x5 fwd-1m; j2 same fwd-3m; j3 same fwd-12m; j4 size x
Mom_11M_Usd 5x5 fwd-1m; j5 same fwd-12m; j6 four-corner summary at fwd-12m EW ann
(small-value, small-growth, large-value, large-growth + the two gaps).
"""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

use = ["stock_id", "date", "Pb", "Mom_11M_Usd", "Mkt_Cap_12M_Usd",
       "R1M_Usd", "R3M_Usd", "R12M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use,
                 parse_dates=["date"])


def dec(s, n=5):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


fp["sz_q"] = fp.groupby("date").Mkt_Cap_12M_Usd.transform(dec, n=5)
fp["pb_q"] = fp.groupby("date").Pb.transform(dec, n=5)
fp["mom_q"] = fp.groupby("date").Mom_11M_Usd.transform(dec, n=5)

out = {}


def grid_print(tag, rowcol, valcol, ann, rows_lab, cols_lab):
    g = fp.groupby(["sz_q", rowcol])[valcol].mean().unstack() * ann
    grid = [[round(g.loc[i, j], 2) if (i in g.index and j in g.columns) else None
             for j in range(1, 6)] for i in range(1, 6)]
    print(f"{tag} (rows=size Q1..Q5, cols={cols_lab}), EW ann. %:")
    for i in range(1, 6):
        row = grid[i - 1]
        print(f"  size Q{i}: " + " ".join(f"{v:+.2f}" if v is not None else "NA" for v in row))
    out[tag.split()[0]] = {"rows": rows_lab, "cols": cols_lab, "grid": grid}


print("SC-D5 — size x Pb and size x momentum joint matrices (fwd returns, EW, ann. %):\n")

grid_print("j1 size x Pb fwd-1m", "pb_q", "R1M_Usd", 1200,
           "size Q1(small)..Q5(large)", "Pb Q1(cheap)..Q5(expensive)")
grid_print("j2 size x Pb fwd-3m", "pb_q", "R3M_Usd", 400,
           "size Q1(small)..Q5(large)", "Pb Q1(cheap)..Q5(expensive)")
grid_print("j3 size x Pb fwd-12m", "pb_q", "R12M_Usd", 100,
           "size Q1(small)..Q5(large)", "Pb Q1(cheap)..Q5(expensive)")
grid_print("j4 size x Mom fwd-1m", "mom_q", "R1M_Usd", 1200,
           "size Q1(small)..Q5(large)", "Mom_11M_Usd Q1(low)..Q5(high)")
grid_print("j5 size x Mom fwd-12m", "mom_q", "R12M_Usd", 100,
           "size Q1(small)..Q5(large)", "Mom_11M_Usd Q1(low)..Q5(high)")

# ---------------- j6: four-corner summary, fwd-12m EW ann ----------------
sv = fp[(fp.sz_q.isin([1, 2])) & (fp.pb_q.isin([1, 2]))].R12M_Usd.mean() * 100
sg = fp[(fp.sz_q.isin([1, 2])) & (fp.pb_q.isin([4, 5]))].R12M_Usd.mean() * 100
lv = fp[(fp.sz_q.isin([4, 5])) & (fp.pb_q.isin([1, 2]))].R12M_Usd.mean() * 100
lg = fp[(fp.sz_q.isin([4, 5])) & (fp.pb_q.isin([4, 5]))].R12M_Usd.mean() * 100
gap_small = sv - sg
gap_large = lv - lg

print("j6 four corners, fwd-12m EW ann. %:")
print(f"  small-value {sv:+.2f} | small-growth {sg:+.2f} | large-value {lv:+.2f} | large-growth {lg:+.2f}")
print(f"  gap small-value minus small-growth: {gap_small:+.2f}")
print(f"  gap large-value minus large-growth: {gap_large:+.2f}")

out["j6"] = {
    "small_value": round(sv, 2),
    "small_growth": round(sg, 2),
    "large_value": round(lv, 2),
    "large_growth": round(lg, 2),
    "gap_small_value_minus_small_growth": round(gap_small, 2),
    "gap_large_value_minus_large_growth": round(gap_large, 2),
}

outpath = "/home/user/claude-demo/research/notes/es_sc_matrices/sc_d5.json"
with open(outpath, "w") as f:
    json.dump(out, f, indent=2)
print(f"\n[written] {outpath}")
