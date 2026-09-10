"""TECH-D1..D4 — the technical/regime battery (ATH & drawdown states, MA-stage
quadrants, momentum-condition map, valuation-regime persistence). Registered
2026-09-10 BEFORE this run (ledger entries of record: TECH-D1, TECH-D2, TECH-D3,
TECH-D4 in research/register/trial-ledger.md). Conventions inherited: dec()
per-date bucketing and x1200/x100 annualization (scripts/analyze_val.py), the
expanding-tercile idiom with quantile-boundary lag plus an extra state-label lag
where the entry specifies "lagged" (scripts/analyze_val.py VAL-D5 /
scripts/analyze_fun_d9a_d10.py exp_tercile), and rolling(+).apply(prod).shift(-N)
forward-window construction (both scripts). Prints only — no interpretation.
"""
import json

import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"
OUT = {}

# ================= shared loaders =================

nifty = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
px = nifty["Adj Close"]

sh = pd.read_csv(f"{V}/us_index/sp500_shiller_monthly_1871.csv", parse_dates=["Date"]).set_index("Date")
sh = sh[(sh["Real Price"] > 0) & (sh["Real Dividend"] > 0)]
rtr = ((sh["Real Price"] + sh["Real Dividend"] / 12) / sh["Real Price"].shift(1)).dropna()  # real TR monthly
tri = rtr.cumprod()  # real TR index; rtr is already a gross monthly factor (VAL-D5 construction)
cape = sh.PE10.replace(0, np.nan).reindex(tri.index)

gold = pd.read_csv(f"{V}/commodities/gold_monthly_1833_2026.csv")
gold["Date"] = pd.to_datetime(gold["Date"], format="%Y-%m") + pd.offsets.MonthEnd(0)
gold = gold.set_index("Date")["Price"]
gret = gold.pct_change()


def fwd_compound_gross(gross, n):
    """Compound a GROSS return factor (e.g. rtr, or 1+pct_change) over the n periods
    AFTER the index date (rolling+shift(-n)), returning a net return."""
    return gross.rolling(n).apply(np.prod, raw=True).shift(-n) - 1


def exp_tercile(s, minn):
    """VAL-D5 / exp_tercile idiom: quantile boundaries lagged 1 period."""
    lo = s.expanding(minn).quantile(1 / 3).shift(1)
    hi = s.expanding(minn).quantile(2 / 3).shift(1)
    t = pd.Series(np.where(s <= lo, "LOW", np.where(s <= hi, "MID", "HIGH")), index=s.index)
    t[lo.isna()] = np.nan
    return t


def pos_gap_ge(flag, full_index, k):
    """Integer month/day-position gap since the previous True in `flag` >= k."""
    pos = pd.Series(np.arange(len(full_index)), index=full_index)
    fpos = pos[flag]
    gap = fpos.diff()
    return fpos.index[gap >= k]


fwd12_nifty = px.shift(-252) / px - 1
fwd36_nifty = px.shift(-756) / px - 1
fwd36_nifty_ann = (1 + fwd36_nifty) ** (1 / 3) - 1
fwd12_real = fwd_compound_gross(rtr, 12)  # rtr is already a gross monthly TR factor
gold_fwd12 = fwd_compound_gross(1 + gret, 12)  # gret is a net monthly return

print("=" * 100)
print("TECH-D1 — the ATH & drawdown-state battery")
print("=" * 100)

# ---------------- a1: NIFTY drawdown terciles -> fwd-12m TR ----------------
dd = 1 - px / px.cummax()
ter_a1 = exp_tercile(dd, 750)
d1 = pd.DataFrame({"t": ter_a1, "f": fwd12_nifty}).dropna()
a1 = {}
print("a1 — NIFTY drawdown-from-ATH terciles (expanding min750d, quantile-lagged 1d) -> fwd-12m TR"
      " (overlap FLAGGED):")
for lab in ["LOW", "MID", "HIGH"]:
    x = d1.f[d1.t == lab]
    a1[lab] = {"mean_pct": round(x.mean() * 100, 2), "n": int(x.count())}
    print(f"  {lab:>4} drawdown: fwd12m TR mean {x.mean()*100:+.2f}% (n={int(x.count())})")
OUT.setdefault("tech_d1", {})["a1"] = a1

# ---------------- a2: Shiller new-ATH months -> next-12m real TR ----------------
new_ath = tri >= tri.cummax()
a2 = {
    "ATH": {"mean_pct": round(fwd12_real[new_ath].mean() * 100, 2),
            "p_negative_pct": round((fwd12_real[new_ath] < 0).mean() * 100, 2),
            "n": int(fwd12_real[new_ath].count())},
    "OTHER": {"mean_pct": round(fwd12_real[~new_ath].mean() * 100, 2),
              "p_negative_pct": round((fwd12_real[~new_ath] < 0).mean() * 100, 2),
              "n": int(fwd12_real[~new_ath].count())},
}
print("\na2 — Shiller new-ATH months (real TR index at running max) -> next-12m real TR:")
for lab in ["ATH", "OTHER"]:
    v = a2[lab]
    print(f"  {lab:>5}: mean {v['mean_pct']:+.2f}% | P(neg) {v['p_negative_pct']:.2f}% (n={v['n']})")
OUT["tech_d1"]["a2"] = a2

# ---------------- a3: NIFTY 52w-high proximity terciles -> fwd-12m TR ----------------
prox = px / px.rolling(252).max()
ter_a3 = exp_tercile(prox, 750)
d3 = pd.DataFrame({"t": ter_a3, "f": fwd12_nifty}).dropna()
a3 = {}
print("\na3 — NIFTY 52w-high proximity (close/max252) terciles (expanding min750d, quantile-lagged 1d)"
      " -> fwd-12m TR:")
for lab in ["LOW", "MID", "HIGH"]:
    x = d3.f[d3.t == lab]
    a3[lab] = {"mean_pct": round(x.mean() * 100, 2), "n": int(x.count())}
    print(f"  {lab:>4} proximity: fwd12m TR mean {x.mean()*100:+.2f}% (n={int(x.count())})")
OUT["tech_d1"]["a3"] = a3

# ---------------- a4: gold new nominal ATH months -> next-12m gold return ----------------
gold_ath = gold >= gold.cummax()
a4 = {
    "ATH": {"mean_pct": round(gold_fwd12[gold_ath].mean() * 100, 2), "n": int(gold_fwd12[gold_ath].count())},
    "OTHER": {"mean_pct": round(gold_fwd12[~gold_ath].mean() * 100, 2), "n": int(gold_fwd12[~gold_ath].count())},
}
print("\na4 — gold new nominal-ATH months -> next-12m gold return:")
for lab in ["ATH", "OTHER"]:
    v = a4[lab]
    print(f"  {lab:>5}: mean {v['mean_pct']:+.2f}% (n={v['n']})")
OUT["tech_d1"]["a4"] = a4

# ---------------- a5: Shiller breakout events (>=24m since previous ATH) ----------------
breakout_dates = pos_gap_ge(new_ath, tri.index, 24)
a5 = {
    "BREAKOUT": {"mean_pct": round(fwd12_real.loc[breakout_dates].mean() * 100, 2),
                 "n": int(fwd12_real.loc[breakout_dates].count())},
    "UNCONDITIONAL": {"mean_pct": round(fwd12_real.mean() * 100, 2), "n": int(fwd12_real.count())},
}
print("\na5 — Shiller breakout events (new ATH, previous ATH >=24m earlier) -> next-12m real TR"
      " vs unconditional:")
for lab in ["BREAKOUT", "UNCONDITIONAL"]:
    v = a5[lab]
    print(f"  {lab:>13}: mean {v['mean_pct']:+.2f}% (n={v['n']})")
OUT["tech_d1"]["a5"] = a5

# ---------------- a6: a1 terciles -> fwd-36m TR (annualized) ----------------
d6 = pd.DataFrame({"t": ter_a1, "f": fwd36_nifty_ann}).dropna()
a6 = {}
print("\na6 — a1 drawdown terciles -> fwd-36m TR (annualized, overlap FLAGGED):")
for lab in ["LOW", "MID", "HIGH"]:
    x = d6.f[d6.t == lab]
    a6[lab] = {"mean_pct": round(x.mean() * 100, 2), "n": int(x.count())}
    print(f"  {lab:>4} drawdown: fwd36m TR ann mean {x.mean()*100:+.2f}% (n={int(x.count())})")
OUT["tech_d1"]["a6"] = a6

# ================================================================================
print("\n" + "=" * 100)
print("TECH-D2 — stage quadrants as states")
print("=" * 100)


def quadrant(price, ma, slope):
    above = price > ma
    rising = slope > 0
    q = np.where(above & rising, "S2", np.where(~above & ~rising, "S4", np.where(above & ~rising, "S3", "S1")))
    q = pd.Series(q, index=price.index)
    q[ma.isna() | slope.isna()] = np.nan
    return q


# NIFTY: 200-day MA, slope vs 21 trading days ago, quadrant lagged one bar (1 day)
ma200 = px.rolling(200).mean()
slope_n = ma200 - ma200.shift(21)
quad_n = quadrant(px, ma200, slope_n).shift(1)

# Shiller: 10-month MA on the real TR index, slope vs 1 month ago, quadrant lagged one bar (1 month)
ma10_sh = tri.rolling(10).mean()
slope_sh = ma10_sh - ma10_sh.shift(1)
quad_sh = quadrant(tri, ma10_sh, slope_sh).shift(1)

# gold: 10-month MA on nominal price, slope vs 1 month ago, quadrant lagged one bar (1 month)
ma10_g = gold.rolling(10).mean()
slope_g = ma10_g - ma10_g.shift(1)
quad_g = quadrant(gold, ma10_g, slope_g).shift(1)

QUADS = ["S1", "S2", "S3", "S4"]

# ---------------- s1: NIFTY fwd-1m ann mean + realized vol by quadrant ----------------
daily_ret = px.pct_change()
fwd_ret21 = px.shift(-21) / px - 1
fwd_vol21 = daily_ret.rolling(21).std().shift(-21) * np.sqrt(252)
ds1 = pd.DataFrame({"q": quad_n, "r": fwd_ret21, "v": fwd_vol21}).dropna()
s1 = {}
print("s1 — NIFTY fwd-1m(21d) ann mean return AND realized vol (fwd 21d daily std x sqrt(252)) by quadrant"
      " (lagged 1 bar):")
for q in QUADS:
    sub = ds1[ds1.q == q]
    s1[q] = {"fwd1m_ann_mean_pct": round(sub.r.mean() * 1200, 2),
              "realized_vol_pct": round(sub.v.mean() * 100, 2), "n": int(len(sub))}
    print(f"  {q}: fwd1m ann mean {s1[q]['fwd1m_ann_mean_pct']:+.2f}% | vol {s1[q]['realized_vol_pct']:.2f}%"
          f" (n={s1[q]['n']})")
OUT.setdefault("tech_d2", {})["s1"] = s1

# ---------------- s2: NIFTY fwd-12m by quadrant ----------------
ds2 = pd.DataFrame({"q": quad_n, "f": fwd12_nifty}).dropna()
s2 = {}
print("\ns2 — NIFTY fwd-12m TR by quadrant (lagged 1 bar):")
for q in QUADS:
    x = ds2.f[ds2.q == q]
    s2[q] = {"mean_pct": round(x.mean() * 100, 2), "n": int(x.count())}
    print(f"  {q}: fwd12m mean {s2[q]['mean_pct']:+.2f}% (n={s2[q]['n']})")
OUT["tech_d2"]["s2"] = s2

# ---------------- s3: Shiller fwd-12m real TR by quadrant ----------------
ds3 = pd.DataFrame({"q": quad_sh, "f": fwd12_real}).dropna()
s3 = {}
print("\ns3 — Shiller fwd-12m real TR by quadrant (lagged 1 bar):")
for q in QUADS:
    x = ds3.f[ds3.q == q]
    s3[q] = {"mean_pct": round(x.mean() * 100, 2), "n": int(x.count())}
    print(f"  {q}: fwd12m real TR mean {s3[q]['mean_pct']:+.2f}% (n={s3[q]['n']})")
OUT["tech_d2"]["s3"] = s3

# ---------------- s4: gold fwd-12m by quadrant ----------------
ds4 = pd.DataFrame({"q": quad_g, "f": gold_fwd12}).dropna()
s4 = {}
print("\ns4 — gold fwd-12m return by quadrant (lagged 1 bar):")
for q in QUADS:
    x = ds4.f[ds4.q == q]
    s4[q] = {"mean_pct": round(x.mean() * 100, 2), "n": int(x.count())}
    print(f"  {q}: fwd12m mean {s4[q]['mean_pct']:+.2f}% (n={s4[q]['n']})")
OUT["tech_d2"]["s4"] = s4

# ---------------- s5: Shiller quadrant x CAPE tercile, 4 corners ----------------
lo_c = cape.expanding(240).quantile(1 / 3).shift(1)
hi_c = cape.expanding(240).quantile(2 / 3).shift(1)
cape_t = pd.Series(np.where(cape <= lo_c, "CHEAP", np.where(cape <= hi_c, "MID", "EXPENSIVE")), index=cape.index)
cape_t[lo_c.isna()] = np.nan

ds5 = pd.DataFrame({"q": quad_sh, "c": cape_t, "f": fwd12_real}).dropna()
s5 = {}
print("\ns5 — Shiller quadrant x CAPE tercile (expanding min240m, quantile-lagged) -> fwd-12m real TR,"
      " 4 corners:")
for q, c in [("S2", "CHEAP"), ("S2", "EXPENSIVE"), ("S4", "CHEAP"), ("S4", "EXPENSIVE")]:
    sub = ds5[(ds5.q == q) & (ds5.c == c)]
    key = f"{q}-{c.lower()}"
    s5[key] = {"mean_pct": round(sub.f.mean() * 100, 2), "n": int(len(sub))}
    print(f"  {q}-{c:<9}: fwd12m real TR mean {s5[key]['mean_pct']:+.2f}% (n={s5[key]['n']})")
OUT["tech_d2"]["s5"] = s5

# ================================================================================
print("\n" + "=" * 100)
print("TECH-D3 — the momentum condition map")
print("=" * 100)

# ---- US market (Mkt-RF + RF) and UMD ----
p = pd.read_csv(f"{V}/factors/fff_monthly_us.csv", skiprows=3)
p.columns = [c.strip() for c in p.columns]
c0 = p.columns[0]
p = p[pd.to_numeric(p[c0], errors="coerce").notna()].copy()
p["ym"] = p[c0].astype(int)
p = p[p.ym >= 100000].copy()  # drop the trailing annual-summary rows (4-digit years)
p.index = pd.to_datetime(p.ym, format="%Y%m") + pd.offsets.MonthEnd(0)
for c in ["Mkt-RF", "SMB", "HML", "RF"]:
    p[c] = p[c].astype(float) / 100
mkt_us = p["Mkt-RF"] + p["RF"]

mom = pd.read_csv(f"{V}/factors/ff_momentum_monthly.csv", skiprows=13)
mom.columns = [c.strip() for c in mom.columns]
c0m = mom.columns[0]
mom = mom[pd.to_numeric(mom[c0m], errors="coerce").notna()].copy()
mom["ym"] = mom[c0m].astype(int)
mom = mom[(mom.ym >= 192701) & (mom.ym <= 202412)].copy()
mom.index = pd.to_datetime(mom.ym, format="%Y%m") + pd.offsets.MonthEnd(0)
umd = mom["Mom"].astype(float) / 100

vix = pd.read_csv(f"{V}/globalvol/cboe_vix_daily_1990_2026.csv", parse_dates=["DATE"]).set_index("DATE")
vix_m = vix["CLOSE"].resample("ME").mean()

iima = pd.read_csv(f"{V}/factors/iima_monthly_factors.csv", na_values="NA")
iima["Date"] = pd.to_datetime(iima["Date"], format="%Y-%m") + pd.offsets.MonthEnd(0)
iima = iima.set_index("Date")
for c in ["SMB", "HML", "WML", "MF", "RF"]:
    iima[c] = iima[c].astype(float) / 100
mkt_in = iima["MF"] + iima["RF"]
wml = iima["WML"]

# ---------------- m1: UMD in post-bear (trailing-24m US mkt TR<0, lagged 1m) vs otherwise ----------------
trail24_us = (1 + mkt_us).rolling(24).apply(np.prod, raw=True) - 1
post_bear_us = (trail24_us < 0).shift(1)  # lagged 1m
dm1 = pd.DataFrame({"umd": umd, "s": post_bear_us}).dropna()
dm1["s"] = dm1["s"].astype(bool)
m1 = {
    "POST_BEAR": {"mean_pct": round(dm1.umd[dm1.s].mean() * 1200, 2), "n": int(dm1.s.sum())},
    "OTHER": {"mean_pct": round(dm1.umd[~dm1.s].mean() * 1200, 2), "n": int((~dm1.s).sum())},
}
print("m1 — US UMD mean in post-bear (trailing-24m mkt TR<0, lagged1m) vs otherwise:")
for lab in ["POST_BEAR", "OTHER"]:
    v = m1[lab]
    print(f"  {lab:>9}: {v['mean_pct']:+.2f}%/yr (n={v['n']})")
OUT.setdefault("tech_d3", {})["m1"] = m1

# ---------------- m2: monthly-mean VIX terciles -> UMD (1990-2024) ----------------
ter_vix = exp_tercile(vix_m, 120).shift(1)  # extra 1m lag (exp_tercile idiom + "lagged")
dm2 = pd.DataFrame({"umd": umd, "t": ter_vix}).dropna()
dm2 = dm2[(dm2.index.year >= 1990) & (dm2.index.year <= 2024)]
m2 = {}
print("\nm2 — US UMD mean by monthly-mean-VIX tercile (expanding min120m, lagged), 1990-2024:")
for lab in ["LOW", "MID", "HIGH"]:
    x = dm2.umd[dm2.t == lab]
    m2[lab] = {"mean_pct": round(x.mean() * 1200, 2), "n": int(x.count())}
    print(f"  {lab:>4} VIX: UMD mean {m2[lab]['mean_pct']:+.2f}%/yr (n={m2[lab]['n']})")
OUT["tech_d3"]["m2"] = m2

# ---------------- m3: sign of trailing-12m UMD sum -> next-12m UMD sum ----------------
trail12_umd = umd.rolling(12).sum()
sign_umd = np.sign(trail12_umd).shift(1)
next12_umd = umd.rolling(12).sum().shift(-12)
dm3 = pd.DataFrame({"s": sign_umd, "f": next12_umd}).dropna()
m3 = {
    "POS": {"mean_pct": round(dm3.f[dm3.s > 0].mean() * 100, 2), "n": int((dm3.s > 0).sum())},
    "NEG": {"mean_pct": round(dm3.f[dm3.s < 0].mean() * 100, 2), "n": int((dm3.s < 0).sum())},
}
print("\nm3 — sign(trailing-12m UMD sum, lagged1m) -> next-12m UMD sum (overlap FLAGGED):")
for lab in ["POS", "NEG"]:
    v = m3[lab]
    print(f"  {lab}: next12m UMD sum mean {v['mean_pct']:+.2f}% (n={v['n']})")
OUT["tech_d3"]["m3"] = m3

# ---------------- m4: crash cell (post-bear AND top-VIX tercile) + worst 3 months ----------------
top_vix = ter_vix == "HIGH"
crash_us = (post_bear_us.reindex(top_vix.index).fillna(False)) & (top_vix.fillna(False))
dm4 = pd.DataFrame({"umd": umd, "crash": crash_us}).dropna(subset=["umd"])
dm4["crash"] = dm4["crash"].fillna(False).astype(bool)
m4 = {
    "CRASH_STATE": {"mean_pct": round(dm4.umd[dm4.crash].mean() * 1200, 2), "n": int(dm4.crash.sum())},
    "OTHER": {"mean_pct": round(dm4.umd[~dm4.crash].mean() * 1200, 2), "n": int((~dm4.crash).sum())},
}
worst3_us = umd.dropna().sort_values().head(3)
m4_worst = []
for dt, val in worst3_us.items():
    pb = post_bear_us.get(dt)
    vt = ter_vix.get(dt)
    m4_worst.append({"date": str(dt.date()), "umd_pct": round(val * 100, 2),
                      "post_bear": (bool(pb) if pd.notna(pb) else None),
                      "vix_tercile": (vt if isinstance(vt, str) else None)})
m4["worst3"] = m4_worst
print("\nm4 — US crash/switch cell: UMD in (post-bear AND top-VIX tercile) vs all other months:")
for lab in ["CRASH_STATE", "OTHER"]:
    v = m4[lab]
    print(f"  {lab:>11}: {v['mean_pct']:+.2f}%/yr (n={v['n']})")
print("  worst 3 UMD months:", m4_worst)
OUT["tech_d3"]["m4"] = m4

# ---------------- m5: India WML in post-bear (trailing-24m India mkt TR<0, lagged1m) vs otherwise ----------------
trail24_in = (1 + mkt_in).rolling(24).apply(np.prod, raw=True) - 1
post_bear_in = (trail24_in < 0).shift(1)
dm5 = pd.DataFrame({"wml": wml, "s": post_bear_in}).dropna()
dm5["s"] = dm5["s"].astype(bool)
m5 = {
    "POST_BEAR": {"mean_pct": round(dm5.wml[dm5.s].mean() * 1200, 2), "n": int(dm5.s.sum())},
    "OTHER": {"mean_pct": round(dm5.wml[~dm5.s].mean() * 1200, 2), "n": int((~dm5.s).sum())},
}
print("\nm5 — India WML mean in post-bear (trailing-24m mkt TR<0, lagged1m) vs otherwise (1993-2025):")
for lab in ["POST_BEAR", "OTHER"]:
    v = m5[lab]
    print(f"  {lab:>9}: {v['mean_pct']:+.2f}%/yr (n={v['n']})")
OUT["tech_d3"]["m5"] = m5

# ---------------- m6: India realized-vol terciles -> WML ----------------
vol_in = mkt_in.rolling(12).std() * np.sqrt(12)
ter_vol_in = exp_tercile(vol_in, 120).shift(1)
dm6 = pd.DataFrame({"wml": wml, "t": ter_vol_in}).dropna()
m6 = {}
print("\nm6 — India WML mean by trailing-12m realized-vol tercile (expanding min120m, lagged), 1993-2025:")
for lab in ["LOW", "MID", "HIGH"]:
    x = dm6.wml[dm6.t == lab]
    m6[lab] = {"mean_pct": round(x.mean() * 1200, 2), "n": int(x.count())}
    print(f"  {lab:>4} vol: WML mean {m6[lab]['mean_pct']:+.2f}%/yr (n={m6[lab]['n']})")
OUT["tech_d3"]["m6"] = m6

# ---------------- m7: sign of trailing-12m WML sum -> next-12m WML sum ----------------
trail12_wml = wml.rolling(12).sum()
sign_wml = np.sign(trail12_wml).shift(1)
next12_wml = wml.rolling(12).sum().shift(-12)
dm7 = pd.DataFrame({"s": sign_wml, "f": next12_wml}).dropna()
m7 = {
    "POS": {"mean_pct": round(dm7.f[dm7.s > 0].mean() * 100, 2), "n": int((dm7.s > 0).sum())},
    "NEG": {"mean_pct": round(dm7.f[dm7.s < 0].mean() * 100, 2), "n": int((dm7.s < 0).sum())},
}
print("\nm7 — sign(trailing-12m WML sum, lagged1m) -> next-12m WML sum (overlap FLAGGED):")
for lab in ["POS", "NEG"]:
    v = m7[lab]
    print(f"  {lab}: next12m WML sum mean {v['mean_pct']:+.2f}% (n={v['n']})")
OUT["tech_d3"]["m7"] = m7

# ---------------- m8: India crash cell + worst 3 months ----------------
top_vol_in = ter_vol_in == "HIGH"
crash_in = (post_bear_in.reindex(top_vol_in.index).fillna(False)) & (top_vol_in.fillna(False))
dm8 = pd.DataFrame({"wml": wml, "crash": crash_in}).dropna(subset=["wml"])
dm8["crash"] = dm8["crash"].fillna(False).astype(bool)
m8 = {
    "CRASH_STATE": {"mean_pct": round(dm8.wml[dm8.crash].mean() * 1200, 2), "n": int(dm8.crash.sum())},
    "OTHER": {"mean_pct": round(dm8.wml[~dm8.crash].mean() * 1200, 2), "n": int((~dm8.crash).sum())},
}
worst3_in = wml.dropna().sort_values().head(3)
m8_worst = []
for dt, val in worst3_in.items():
    pb = post_bear_in.get(dt)
    vt = ter_vol_in.get(dt)
    m8_worst.append({"date": str(dt.date()), "wml_pct": round(val * 100, 2),
                      "post_bear": (bool(pb) if pd.notna(pb) else None),
                      "vol_tercile": (vt if isinstance(vt, str) else None)})
m8["worst3"] = m8_worst
print("\nm8 — India crash/switch cell: WML in (post-bear AND top-vol tercile) vs all other months:")
for lab in ["CRASH_STATE", "OTHER"]:
    v = m8[lab]
    print(f"  {lab:>11}: {v['mean_pct']:+.2f}%/yr (n={v['n']})")
print("  worst 3 WML months:", m8_worst)
OUT["tech_d3"]["m8"] = m8

# ---------------- m9/m10: firm-panel decile spreads ----------------
use = ["stock_id", "date", "Mom_5M_Usd", "Mom_11M_Usd", "Mom_Sharp_5M_Usd", "Mom_Sharp_11M_Usd",
       "Mkt_Cap_12M_Usd", "R1M_Usd", "R12M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use, parse_dates=["date"])


def dec(s, n=5):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


fp["sz"] = fp.groupby("date").Mkt_Cap_12M_Usd.transform(dec)  # quintiles
big = fp[fp.sz == 5].copy()


def decile_spread(df, col):
    d = df.copy()
    d["dq"] = d.groupby("date")[col].transform(lambda s: dec(s, 10))
    s1 = (d[d.dq == 10].R1M_Usd.mean() - d[d.dq == 1].R1M_Usd.mean()) * 1200
    s12 = (d[d.dq == 10].R12M_Usd.mean() - d[d.dq == 1].R12M_Usd.mean()) * 100
    return round(s1, 2), round(s12, 2)


print("\nm9 — Mom_11M vs Mom_5M decile D10-D1 spread, fwd-1m(x1200)/fwd-12m(x100), panel and szQ5:")
m9 = {}
for col in ["Mom_11M_Usd", "Mom_5M_Usd"]:
    p1, p12 = decile_spread(fp, col)
    b1, b12 = decile_spread(big, col)
    m9[col] = {"panel_fwd1m": p1, "panel_fwd12m": p12, "szQ5_fwd1m": b1, "szQ5_fwd12m": b12}
    print(f"  {col:>18}: panel 1m {p1:+7.2f} | panel 12m {p12:+7.2f} | szQ5 1m {b1:+7.2f} | szQ5 12m {b12:+7.2f}")
OUT["tech_d3"]["m9"] = m9

print("\nm10 — Mom_Sharp_11M vs Mom_11M decile D10-D1 spread, fwd-1m(x1200)/fwd-12m(x100), panel and szQ5:")
m10 = {}
for col in ["Mom_Sharp_11M_Usd", "Mom_11M_Usd"]:
    p1, p12 = decile_spread(fp, col)
    b1, b12 = decile_spread(big, col)
    m10[col] = {"panel_fwd1m": p1, "panel_fwd12m": p12, "szQ5_fwd1m": b1, "szQ5_fwd12m": b12}
    print(f"  {col:>18}: panel 1m {p1:+7.2f} | panel 12m {p12:+7.2f} | szQ5 1m {b1:+7.2f} | szQ5 12m {b12:+7.2f}")
OUT["tech_d3"]["m10"] = m10

# ================================================================================
print("\n" + "=" * 100)
print("TECH-D4 — valuation-regime persistence")
print("=" * 100)

LABELS = ["CHEAP", "MID", "EXPENSIVE"]
valid_c = cape_t.dropna()

# ---------------- c1: monthly transition matrix ----------------
t_now = valid_c
t_next = valid_c.shift(-1)
dc1 = pd.DataFrame({"now": t_now, "next": t_next}).dropna()
mat = pd.crosstab(dc1.now, dc1.next, normalize="index").reindex(index=LABELS, columns=LABELS).fillna(0.0)
c1 = {r: {cq: round(mat.loc[r, cq], 2) for cq in LABELS} for r in LABELS}
print("c1 — CAPE tercile monthly transition matrix (row-normalized; rows=now, cols=next month):")
for r in LABELS:
    print(f"  {r:>9} -> " + " | ".join(f"{cq} {c1[r][cq]:.2f}" for cq in LABELS))
print("  P(stay) diagonal: " + " | ".join(f"{lab} {c1[lab][lab]:.2f}" for lab in LABELS))
OUT.setdefault("tech_d4", {})["c1"] = {"matrix": c1, "p_stay": {lab: c1[lab][lab] for lab in LABELS}}

# ---------------- c2: spell lengths ----------------
run_id = (valid_c != valid_c.shift(1)).cumsum()
runs = valid_c.groupby(run_id).agg(["first", "size"])
runs.columns = ["label", "length"]
c2 = {}
print("\nc2 — CAPE tercile spell lengths (consecutive-month runs), months:")
for lab in LABELS:
    ln = runs.length[runs.label == lab]
    c2[lab] = {"median": float(ln.median()), "mean": round(float(ln.mean()), 2), "n_spells": int(len(ln))}
    print(f"  {lab:>9}: median {c2[lab]['median']:.1f} | mean {c2[lab]['mean']:.2f} (n_spells={c2[lab]['n_spells']})")
OUT["tech_d4"]["c2"] = c2

# ---------------- c3: P(same tercile 12m ahead) ----------------
t_12 = valid_c.shift(-12)
dc3 = pd.DataFrame({"now": valid_c, "fut": t_12}).dropna()
c3 = {}
print("\nc3 — P(same CAPE tercile 12 months later):")
for lab in LABELS:
    sub = dc3[dc3.now == lab]
    c3[lab] = {"p_same": round((sub.fut == lab).mean(), 2), "n": int(len(sub))}
    print(f"  {lab:>9}: P(same) {c3[lab]['p_same']:.2f} (n={c3[lab]['n']})")
OUT["tech_d4"]["c3"] = c3

# ---------------- c4: fwd-12m real TR after flip out of expensive vs out of cheap vs unconditional ----------------
label_shift = valid_c.shift(1)
flip_out_expensive = (label_shift == "EXPENSIVE") & (valid_c != "EXPENSIVE")
flip_out_cheap = (label_shift == "CHEAP") & (valid_c != "CHEAP")
events_out_exp = valid_c.index[flip_out_expensive.fillna(False)]
events_out_cheap = valid_c.index[flip_out_cheap.fillna(False)]


def overlap_flag(dates, full_index, k=12):
    pos = pd.Series(np.arange(len(full_index)), index=full_index)
    dp = pos.loc[dates].sort_values()
    return bool((dp.diff().dropna() < k).any())


c4 = {
    "OUT_OF_EXPENSIVE": {"mean_pct": round(fwd12_real.reindex(events_out_exp).mean() * 100, 2),
                          "n": int(fwd12_real.reindex(events_out_exp).count()),
                          "overlap_flag": overlap_flag(events_out_exp, tri.index)},
    "OUT_OF_CHEAP": {"mean_pct": round(fwd12_real.reindex(events_out_cheap).mean() * 100, 2),
                      "n": int(fwd12_real.reindex(events_out_cheap).count()),
                      "overlap_flag": overlap_flag(events_out_cheap, tri.index)},
    "UNCONDITIONAL": {"mean_pct": round(fwd12_real.mean() * 100, 2), "n": int(fwd12_real.count())},
}
print("\nc4 — fwd-12m real TR: 12m after flip OUT of expensive vs flip OUT of cheap vs unconditional"
      " (event = first month in new tercile; overlap FLAGGED):")
for lab in ["OUT_OF_EXPENSIVE", "OUT_OF_CHEAP", "UNCONDITIONAL"]:
    v = c4[lab]
    extra = f" | overlap={v['overlap_flag']}" if "overlap_flag" in v else ""
    print(f"  {lab:>17}: mean {v['mean_pct']:+.2f}% (n={v['n']}){extra}")
OUT["tech_d4"]["c4"] = c4

# ================================================================================
out_path = "/home/user/claude-demo/research/notes/es_sc_matrices/tech.json"
json.dump(OUT, open(out_path, "w"), indent=1)
print(f"\n[written] {out_path}")
