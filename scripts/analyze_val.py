"""VAL-D1..D5 — the valuation arc (measure ladder, complementarity matrix, trap
anatomy, factor blends, the CAPE floor test). Registered 2026-09-10 BEFORE this run
(ledger entries of record). Conventions inherited: dec() per-date buckets, EW means,
x1200/x100 annualization, QG-D3 36m compounding, SC-D2 rolling sums. Prints only."""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
OUT = {}

use = ["stock_id", "date", "Eps", "Pb", "Pe", "Ev_Ebitda", "Fcf_Yld", "Div_Yld", "Bb_Yld",
       "Roe", "Mom_11M_Usd", "Vol1Y_Usd", "Debtequity", "Share_Turn_12M", "Eps_Basic_Gr",
       "Mkt_Cap_12M_Usd", "R1M_Usd", "R12M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use, parse_dates=["date"])

r = fp.pivot_table(index="date", columns="stock_id", values="R1M_Usd")
lg = np.log1p(r)
f36 = ((np.exp(lg.rolling(36, min_periods=27).sum().shift(-35) * (12 / 36)) - 1) * 100).stack().rename("f36")
eps = fp.pivot_table(index="date", columns="stock_id", values="Eps")
d3 = (eps - eps.shift(3)).stack().rename("d3")
d12e = (eps - eps.shift(12)).stack().rename("d12e")
fp = fp.set_index(["date", "stock_id"]).join(f36).join(d3).join(d12e).reset_index()


def dec(s, n=5):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


fp["sz"] = fp.groupby("date").Mkt_Cap_12M_Usd.transform(dec)

# ---------------- VAL-D1: the measure ladder ----------------
MEAS = [("Pb", -1), ("Pe", -1), ("Ev_Ebitda", -1), ("Fcf_Yld", 1), ("Div_Yld", 1), ("Bb_Yld", 1)]
print("VAL-D1 — valuation-measure ladder (cheap-minus-expensive, EW ann; szQ5 = large-cap 12m):")
lad = {}
for col, sign in MEAS:
    fp["q"] = fp.groupby("date")[col].transform(dec)
    cheap, expn = (1, 5) if sign < 0 else (5, 1)
    s1 = (fp[fp.q == cheap].R1M_Usd.mean() - fp[fp.q == expn].R1M_Usd.mean()) * 1200
    s12 = (fp[fp.q == cheap].R12M_Usd.mean() - fp[fp.q == expn].R12M_Usd.mean()) * 100
    s36 = fp[fp.q == cheap].f36.mean() - fp[fp.q == expn].f36.mean()
    big = fp[fp.sz == 5].copy()
    big["q"] = big.groupby("date")[col].transform(dec)
    b12 = (big[big.q == cheap].R12M_Usd.mean() - big[big.q == expn].R12M_Usd.mean()) * 100
    lad[col] = [round(x, 2) for x in (s1, s12, s36, b12)]
    print(f"  {col:>10}: 1m {s1:+6.2f} | 12m {s12:+6.2f} | 36m {s36:+6.2f} | szQ5 12m {b12:+6.2f}")
# v7 composite (Pb, Ev_Ebitda inverted; Fcf_Yld as-is): rank-mean per date
fp["comp"] = fp.groupby("date", group_keys=False).apply(
    lambda g: ((1 - g.Pb.rank(pct=True)) + (1 - g.Ev_Ebitda.rank(pct=True)) + g.Fcf_Yld.rank(pct=True)) / 3)
fp["q"] = fp.groupby("date").comp.transform(dec)
s1 = (fp[fp.q == 5].R1M_Usd.mean() - fp[fp.q == 1].R1M_Usd.mean()) * 1200
s12 = (fp[fp.q == 5].R12M_Usd.mean() - fp[fp.q == 1].R12M_Usd.mean()) * 100
s36 = fp[fp.q == 5].f36.mean() - fp[fp.q == 1].f36.mean()
big = fp[fp.sz == 5].copy(); big["q"] = big.groupby("date").comp.transform(dec)
b12 = (big[big.q == 5].R12M_Usd.mean() - big[big.q == 1].R12M_Usd.mean()) * 100
lad["COMPOSITE"] = [round(x, 2) for x in (s1, s12, s36, b12)]
print(f"  v7 COMPOSITE: 1m {s1:+6.2f} | 12m {s12:+6.2f} | 36m {s36:+6.2f} | szQ5 12m {b12:+6.2f}")
print("  v8 ladder by szQ5 12m: " + " > ".join(k for k, v in sorted(lad.items(), key=lambda kv: -kv[1][3])))
OUT["val_d1"] = lad

# ---------------- VAL-D2: complementarity matrix ----------------
fp["pb_q"] = fp.groupby("date").Pb.transform(dec)
COMP = [("Roe", 1), ("Mom_11M_Usd", 1), ("Vol1Y_Usd", -1), ("Debtequity", -1),
        ("Share_Turn_12M", -1), ("Eps_Basic_Gr", 1), ("Bb_Yld", 1), ("d3", 1)]
print("\nVAL-D2 — complementarity matrix (WCS = good-bad within cheap Pb Q1-2, fwd-12m EW ann;")
print("         VSC = mean Pb Q1-Q5 spread within X quintiles; verdicts per the frozen rules):")
res = {}
for col, sign in COMP:
    cheap = fp[fp.pb_q <= 2].copy()
    cheap["xq"] = cheap.groupby("date")[col].transform(dec)
    good, bad = (5, 1) if sign > 0 else (1, 5)
    wcs = (cheap[cheap.xq == good].R12M_Usd.mean() - cheap[cheap.xq == bad].R12M_Usd.mean()) * 100
    fp["xq"] = fp.groupby("date")[col].transform(dec)
    vsc = np.mean([(fp[(fp.xq == q) & (fp.pb_q == 1)].R12M_Usd.mean()
                    - fp[(fp.xq == q) & (fp.pb_q == 5)].R12M_Usd.mean()) * 100 for q in range(1, 6)])
    bigc = fp[(fp.sz == 5) & (fp.pb_q <= 2)].copy()
    bigc["xq"] = bigc.groupby("date")[col].transform(dec, n=3)
    bw = (bigc[bigc.xq == (3 if sign > 0 else 1)].R12M_Usd.mean()
          - bigc[bigc.xq == (1 if sign > 0 else 3)].R12M_Usd.mean()) * 100
    if wcs >= 2 and vsc >= 2:
        verdict = "COMPLEMENTARY" if np.sign(bw) == np.sign(wcs) else "PANEL-ONLY"
    elif abs(wcs) < 2 and vsc >= 2:
        verdict = "REDUNDANT"
    else:
        verdict = "SUBSUMING/ANTAGONISTIC"
    res[col] = {"wcs": round(wcs, 2), "vsc": round(vsc, 2), "szQ5_wcs": round(bw, 2), "verdict": verdict}
    print(f"  {col:>14}: WCS {wcs:+6.2f} | VSC {vsc:+6.2f} | szQ5 WCS {bw:+6.2f} -> {verdict}")
OUT["val_d2"] = res

# ---------------- VAL-D3: trap anatomy among cheap (Pb Q1) ----------------
print("\nVAL-D3 — value-trap anatomy (good-half minus bad-half among Pb Q1, EW ann):")
ch = fp[fp.pb_q == 1].copy()
TRAPS = [("Debtequity", -1), ("d12e", 1), ("Vol1Y_Usd", -1), ("Roe", 1), ("Share_Turn_12M", -1)]
tr = {}
for col, sign in TRAPS:
    med = ch.groupby("date")[col].transform("median")
    goodmask = (ch[col] <= med) if sign < 0 else (ch[col] > med)
    g12 = (ch[goodmask].R12M_Usd.mean() - ch[~goodmask].R12M_Usd.mean()) * 100
    g36 = ch[goodmask].f36.mean() - ch[~goodmask].f36.mean()
    tr[col] = [round(g12, 2), round(g36, 2)]
    print(f"  {col:>14}: 12m {g12:+6.2f} | 36m {g36:+6.2f}")
OUT["val_d3"] = tr

# ---------------- VAL-D4: factor-level blends (FF6 VW 1963-2020) ----------------
ff = pd.read_csv(f"{V}/factors_us/ff6_monthly_1963_2020.csv", parse_dates=["date"]).set_index("date")
print("\nVAL-D4 — factor-level value complementarity (FF6 VW monthly, 1963-2020):")
corr = {x: round(ff.HML.corr(ff[x]), 2) for x in ["UMD", "RMW", "CMA", "SMB", "MktRF"]}
print("  b1 corr(HML, x): " + " | ".join(f"{k} {v:+.2f}" for k, v in corr.items()))


def sharpe(s):
    return s.mean() / s.std() * np.sqrt(12)


bl = {}
for x in ["UMD", "CMA", "SMB"]:
    b = 0.5 * ff.HML + 0.5 * ff[x]
    bl[x] = (round(sharpe(ff.HML), 2), round(sharpe(ff[x]), 2), round(sharpe(b), 2))
    print(f"  b 50/50 HML+{x}: Sharpe {bl[x][2]:+.2f} (HML {bl[x][0]:+.2f}, {x} {bl[x][1]:+.2f})"
          f" | blend ann {b.mean()*1200:+.2f}%")
w_hml = (ff.HML.rolling(12).sum() * 100).min()
bu = 0.5 * ff.HML + 0.5 * ff.UMD
w_bl = (bu.rolling(12).sum() * 100).min()
print(f"  b5 worst 12m: HML alone {w_hml:+.1f}% | HML+UMD blend {w_bl:+.1f}%"
      f"  (booked quote: cheap-quality blend Sharpe 0.49 vs HML 0.32 / RMW 0.41 — QG-D2)")
OUT["val_d4"] = {"corr": corr, "blends": bl, "worst12": [round(w_hml, 1), round(w_bl, 1)]}

# ---------------- VAL-D5: the CAPE floor test (Shiller 1881-2023) ----------------
sh = pd.read_csv(f"{V}/us_index/sp500_shiller_monthly_1871.csv", parse_dates=["Date"]).set_index("Date")
sh = sh[(sh["Real Price"] > 0) & (sh["Real Dividend"] > 0)]
cape = sh.PE10.replace(0, np.nan)
rtr = (sh["Real Price"] + sh["Real Dividend"] / 12) / sh["Real Price"].shift(1)  # real TR monthly
f5 = (rtr.rolling(60).apply(np.prod, raw=True).shift(-60) ** (12 / 60) - 1) * 100
lo = cape.expanding(240).quantile(1 / 3).shift(1)
hi = cape.expanding(240).quantile(2 / 3).shift(1)
t = pd.Series(np.where(cape <= lo, "CHEAP", np.where(cape <= hi, "MID", "EXPENSIVE")), index=cape.index)
t[lo.isna()] = np.nan
d = pd.DataFrame({"t": t, "f": f5}).dropna()
print("\nVAL-D5 — CAPE terciles (expanding, lagged) -> next-5y REAL TR ann distribution (overlap FLAGGED):")
fl = {}
for lab in ["CHEAP", "MID", "EXPENSIVE"]:
    x = d.f[d.t == lab]
    fl[lab] = [round(x.quantile(0.10), 2), round(x.median(), 2), round(x.quantile(0.90), 2), int(x.count())]
    print(f"  {lab:>9}: p10 {fl[lab][0]:+6.2f} | p50 {fl[lab][1]:+6.2f} | p90 {fl[lab][2]:+6.2f} (n={fl[lab][3]})")
print(f"  floor gap (cheap p10 - expensive p10): {fl['CHEAP'][0]-fl['EXPENSIVE'][0]:+.2f}pp/yr (bar >= +2.00)")
OUT["val_d5"] = fl

json.dump(OUT, open("/home/user/claude-demo/research/notes/es_sc_matrices/val.json", "w"), indent=1)
print("[written] research/notes/es_sc_matrices/val.json")
