"""VAL-D6 (2026-09-10) — the extended measure x size x horizon atlas. Registered
BEFORE this run (research/register/trial-ledger.md, entry "VAL-D6 (2026-09-10)").
Conventions inherited verbatim from analyze_val.py: dec() per-date quintile buckets,
EW means, 1m x1200 / 12m x100 annualization, QG-D3 36m log-compounding convention.
SIZE HALVES per registration: small = szQ1-2, large = szQ4-5 (dec of Mkt_Cap_12M_Usd).
x1-x7 measure ladder + x8-x13 mixes, each re-decked WITHIN size half; x14 verdict.
Prints only. No interpretation."""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
OUT = {}

use = ["stock_id", "date", "Pb", "Pe", "Ev_Ebitda", "Fcf_Yld", "Div_Yld", "Bb_Yld",
       "Ebit_Bv", "Roe", "Mom_11M_Usd", "Vol1Y_Usd", "Mkt_Cap_12M_Usd", "R1M_Usd", "R12M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use, parse_dates=["date"])

# fwd-36m annualized — copied exactly from analyze_val.py (the QG-D3 convention)
r = fp.pivot_table(index="date", columns="stock_id", values="R1M_Usd")
lg = np.log1p(r)
f36 = ((np.exp(lg.rolling(36, min_periods=27).sum().shift(-35) * (12 / 36)) - 1) * 100).stack().rename("f36")
fp = fp.set_index(["date", "stock_id"]).join(f36).reset_index()


def dec(s, n=5):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


fp["sz"] = fp.groupby("date").Mkt_Cap_12M_Usd.transform(dec)
SMALL = fp.sz.isin([1, 2])
LARGE = fp.sz.isin([4, 5])
halves = {"small": fp[SMALL].copy(), "large": fp[LARGE].copy()}

# ---------------- x1-x7: measure ladder, within each size half ----------------
MEAS = [("Pb", -1), ("Pe", -1), ("Ev_Ebitda", -1), ("Fcf_Yld", 1), ("Div_Yld", 1),
        ("Bb_Yld", 1), ("Ebit_Bv", 1)]

meas_out = {}


def spreads(sub, col, cheap, expn):
    sub = sub.copy()
    sub["q"] = sub.groupby("date")[col].transform(dec)
    s1 = (sub[sub.q == cheap].R1M_Usd.mean() - sub[sub.q == expn].R1M_Usd.mean()) * 1200
    s12 = (sub[sub.q == cheap].R12M_Usd.mean() - sub[sub.q == expn].R12M_Usd.mean()) * 100
    s36 = sub[sub.q == cheap].f36.mean() - sub[sub.q == expn].f36.mean()
    return [round(s1, 2), round(s12, 2), round(s36, 2)]


print("x1-x7 — measure ladder, cheap-minus-expensive EW ann, WITHIN size half (re-decked):")
print(f"  {'measure':>10} | {'small 1m/12m/36m':>26} | {'large 1m/12m/36m':>26}")
for col, sign in MEAS:
    cheap, expn = (1, 5) if sign < 0 else (5, 1)
    row = {}
    for half in ("small", "large"):
        row[half] = spreads(halves[half], col, cheap, expn)
    meas_out[col] = row
    sm, lg_ = row["small"], row["large"]
    print(f"  {col:>10} | {sm[0]:+7.2f} {sm[1]:+7.2f} {sm[2]:+7.2f} | {lg_[0]:+7.2f} {lg_[1]:+7.2f} {lg_[2]:+7.2f}")
OUT["measures"] = meas_out

# ---------------- x8-x13: mixes, rank-mean over FULL cross-section ----------------
# per-date rank(pct=True) over the full panel, idiom copied from analyze_val.py's comp column
fp["MIX_VAL2"] = fp.groupby("date", group_keys=False).apply(
    lambda g: ((1 - g.Pb.rank(pct=True)) + (1 - g.Pe.rank(pct=True))) / 2)
fp["MIX_VAL3"] = fp.groupby("date", group_keys=False).apply(
    lambda g: ((1 - g.Pb.rank(pct=True)) + (1 - g.Ev_Ebitda.rank(pct=True)) + g.Fcf_Yld.rank(pct=True)) / 3)
fp["MIX_VAL4"] = fp.groupby("date", group_keys=False).apply(
    lambda g: ((1 - g.Pb.rank(pct=True)) + (1 - g.Ev_Ebitda.rank(pct=True))
               + g.Fcf_Yld.rank(pct=True) + g.Div_Yld.rank(pct=True)) / 4)
fp["MIX_CQ"] = fp.groupby("date", group_keys=False).apply(
    lambda g: ((1 - g.Pb.rank(pct=True)) + g.Roe.rank(pct=True)) / 2)
fp["MIX_VM"] = fp.groupby("date", group_keys=False).apply(
    lambda g: ((1 - g.Pb.rank(pct=True)) + g.Mom_11M_Usd.rank(pct=True)) / 2)
fp["MIX_VLV"] = fp.groupby("date", group_keys=False).apply(
    lambda g: ((1 - g.Pb.rank(pct=True)) + (1 - g.Vol1Y_Usd.rank(pct=True))) / 2)

MIXES = ["VAL2", "VAL3", "VAL4", "CQ", "VM", "VLV"]
halves = {"small": fp[SMALL].copy(), "large": fp[LARGE].copy()}  # refresh (now carries MIX_ cols)

mix_out = {}
print("\nx8-x13 — mixes (full-cross-section rank-mean), Q5-Q1 EW ann, WITHIN size half (re-decked):")
print(f"  {'mix':>10} | {'small 1m/12m/36m':>26} | {'large 1m/12m/36m':>26}")
for m in MIXES:
    col = f"MIX_{m}"
    row = {}
    for half in ("small", "large"):
        row[half] = spreads(halves[half], col, 5, 1)
    mix_out[m] = row
    sm, lg_ = row["small"], row["large"]
    print(f"  {m:>10} | {sm[0]:+7.2f} {sm[1]:+7.2f} {sm[2]:+7.2f} | {lg_[0]:+7.2f} {lg_[1]:+7.2f} {lg_[2]:+7.2f}")
OUT["mixes"] = mix_out

# ---------------- x14: verdict — best measure and best mix per half/horizon ----------------
print("\nx14 — verdict (best MEASURE and best MIX by spread, per size half x horizon):")
hz = [("1m", 0), ("12m", 1), ("36m", 2)]
verdict = {}
for half in ("small", "large"):
    verdict[half] = {}
    for hname, hi in hz:
        best_meas = max(meas_out.items(), key=lambda kv: kv[1][half][hi])
        best_mix = max(mix_out.items(), key=lambda kv: kv[1][half][hi])
        verdict[half][hname] = {
            "best_measure": [best_meas[0], best_meas[1][half][hi]],
            "best_mix": [best_mix[0], best_mix[1][half][hi]],
        }
        print(f"  {half:>5} {hname:>3}: best measure {best_meas[0]:>10} ({best_meas[1][half][hi]:+.2f}) | "
              f"best mix {best_mix[0]:>5} ({best_mix[1][half][hi]:+.2f})")
OUT["verdict"] = verdict

json.dump(OUT, open("/home/user/claude-demo/research/notes/es_sc_matrices/val_d6.json", "w"), indent=1)
print("\n[written] research/notes/es_sc_matrices/val_d6.json")
