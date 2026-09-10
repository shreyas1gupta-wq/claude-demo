"""SC-D4 (2026-09-10) — THE SIZE-CONDITIONAL EDGE MAP, US FIRM PANEL.
Registered 2026-09-10 BEFORE this run (research/register/trial-ledger.md, Entry
SC-D4): WITHIN each size quintile (Mkt_Cap_12M_Usd dec, n=5, per date), the
within-size-quintile signal quintile spread for six signals — Pb, Mom_11M_Usd,
Vol1Y_Usd, Roe, Eps_Basic_Gr, d3(Eps) — at fwd-1m (EW, ann. %, x1200) and fwd-12m
(EW, %, x100). Spread = Q1-Q5 for Pb and Vol1Y_Usd (positive = cheap wins / low-vol
wins); Q5-Q1 for Mom_11M_Usd, Roe, Eps_Basic_Gr, d3 (positive = high wins). No bar,
bucket, horizon, or construction changes from the registration. Prints only;
interpretation is hand-appended to the ledger AFTER the print.
Forward-return convention: firm_panel row t already realizes forward (vault
AUTHENTICATION.md pass-2, corrected GFC anchor) — R1M_Usd/R12M_Usd are NOT re-shifted.
"""
import json
import os

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

use = ["stock_id", "date", "Eps", "Pb", "Mom_11M_Usd", "Mkt_Cap_12M_Usd", "Roe",
       "Eps_Basic_Gr", "Vol1Y_Usd", "R1M_Usd", "R12M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use,
                 parse_dates=["date"])

# d3(Eps): pivot Eps by date x stock_id, minus pivot.shift(3), stack back.
eps = fp.pivot_table(index="date", columns="stock_id", values="Eps")
d3 = (eps - eps.shift(3)).stack().rename("d3")
fp = fp.set_index(["date", "stock_id"]).join(d3).reset_index()


def dec(s, n=5):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


# Size quintile: dec of Mkt_Cap_12M_Usd per date.
fp["sz_q"] = fp.groupby("date").Mkt_Cap_12M_Usd.transform(dec)

SIGNALS = ["Pb", "Mom_11M_Usd", "Vol1Y_Usd", "Roe", "Eps_Basic_Gr", "d3"]
LABEL = {"Pb": "Pb", "Mom_11M_Usd": "Mom", "Vol1Y_Usd": "Vol", "Roe": "Roe",
         "Eps_Basic_Gr": "Gr", "d3": "d3"}
Q1_MINUS_Q5 = {"Pb", "Vol1Y_Usd"}  # positive = cheap wins / low-vol wins

# Signal quintiles WITHIN each (date, size-quintile) group.
for sig in SIGNALS:
    fp[f"{sig}_q"] = fp.groupby(["date", "sz_q"])[sig].transform(dec)


def spreads(ret_col, ann_mult):
    out = {}
    for sig in SIGNALS:
        lab = LABEL[sig]
        m = fp.groupby(["sz_q", f"{sig}_q"])[ret_col].mean().unstack() * ann_mult
        sp = (m[1] - m[5]) if sig in Q1_MINUS_Q5 else (m[5] - m[1])
        out[lab] = [round(sp.get(i, np.nan), 2) for i in range(1, 6)]
    return out


h1m = spreads("R1M_Usd", 1200)
h12m = spreads("R12M_Usd", 100)

print("SC-D4 — size-conditional edge map, US firm panel (EW within-size-quintile "
      "signal spreads):")
print("  spread = Q1-Q5 for Pb, Vol (positive=cheap/low-vol wins); Q5-Q1 for Mom, "
      "Roe, Gr, d3 (positive=high wins)")

print("\nfwd-1m (ann. %, x1200):")
print("  " + f"{'signal':6s}  " + "  ".join(f"szQ{i}" for i in range(1, 6)))
for lab, vals in h1m.items():
    print("  " + f"{lab:6s}  " + "  ".join(f"{v:+7.2f}" for v in vals))

print("\nfwd-12m (%, x100):")
print("  " + f"{'signal':6s}  " + "  ".join(f"szQ{i}" for i in range(1, 6)))
for lab, vals in h12m.items():
    print("  " + f"{lab:6s}  " + "  ".join(f"{v:+7.2f}" for v in vals))

out = {
    "h1m": h1m,
    "h12m": h12m,
    "convention": ("size quintile Q1=smallest..Q5=largest of Mkt_Cap_12M_Usd (dec, "
                   "n=5, per date); signal quintiles computed WITHIN each "
                   "(date, size-quintile) group; spread = Q1-Q5 for Pb and "
                   "Vol1Y_Usd (positive = cheap wins / low-vol wins), Q5-Q1 for "
                   "Mom_11M_Usd, Roe, Eps_Basic_Gr, d3(Eps) (positive = high wins); "
                   "fwd-1m ann. %/yr (x1200), fwd-12m %/12m (x100); EW; forward "
                   "returns already forward per vault AUTH, not re-shifted."),
}
OUT_DIR = "/home/user/claude-demo/research/notes/es_sc_matrices"
os.makedirs(OUT_DIR, exist_ok=True)
with open(f"{OUT_DIR}/sc_d4.json", "w") as f:
    json.dump(out, f, indent=2)
