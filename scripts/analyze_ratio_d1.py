"""RATIO-D1 — index & commodity ratio regimes + the leverage-timing read.
Registered 2026-09-10 BEFORE this run (ledger entry of record). Vol-clustering-
reduces-risk is QUOTED (F2/F3a/TS1/TL-D2 s10), not re-derived here.
Prints only; interpretation hand-appended to the ledger after."""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

# ---------------- shared series ----------------
gold = pd.read_csv(f"{V}/commodities/gold_monthly_1833_2026.csv", parse_dates=["Date"]).set_index("Date")["Price"]
gold_m = gold.resample("ME").last()

nifty = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).set_index("Date")
ncol = [c for c in nifty.columns if "Adj" in c][0]
nifty_d = nifty[ncol]
nifty_m = nifty_d.resample("ME").last()

p = pd.read_csv(f"{V}/factors/fff_monthly_us.csv", skiprows=3)
p.columns = [c.strip() for c in p.columns]
c0 = p.columns[0]
p = p[pd.to_numeric(p[c0], errors="coerce").notna()].copy()
p["ym"] = p[c0].astype(int)
p = p[(p.ym >= 192607) & (p.ym <= 202412)]
p.index = pd.to_datetime(p.ym, format="%Y%m") + pd.offsets.MonthEnd(0)
us_mkt = (p["Mkt-RF"].astype(float) + p["RF"].astype(float)) / 100

ii = pd.read_csv(f"{V}/factors/iima_monthly_factors.csv", na_values="NA")
ii.index = pd.to_datetime(ii.Date, format="%Y-%m") + pd.offsets.MonthEnd(0)
ismb = ii.SMB.astype(float) / 100
imkt = (ii.MF + ii.RF).astype(float) / 100


def fwd_ann(monthly_ret, h):
    return (1 + monthly_ret).rolling(h).apply(np.prod, raw=True).shift(-h) - 1


print("=" * 100)
print("RATIO-D1 — index & commodity ratio regimes + the leverage-timing read")
print("=" * 100)

# ---------------- r1/r2: copper/gold ----------------
imf = pd.read_csv(f"{V}/commodities/imf_pcps_monthly_1980_2017.csv", parse_dates=["Date"]).set_index("Date")
copper = imf["Copper"]
copper.index = copper.index + pd.offsets.MonthEnd(0)  # month-start -> month-end, align with gold_m
cu_gold = (copper / gold_m.reindex(copper.index)).dropna()
ma12 = cu_gold.rolling(12).mean()
slope = np.sign(ma12 - ma12.shift(1)).shift(1)

f12_us = fwd_ann(us_mkt, 12)
d = pd.DataFrame({"s": slope, "f": f12_us.reindex(slope.index)}).dropna()
print(f"r1 copper/gold 12m-MA-slope -> next-12m US market TR: "
      f"RISING {d[d.s>0].f.mean()*100:+.2f}% (n={len(d[d.s>0])}) | "
      f"FALLING {d[d.s<0].f.mean()*100:+.2f}% (n={len(d[d.s<0])})")

nifty_ret_m = nifty_m.pct_change()
f12_n = fwd_ann(nifty_ret_m, 12)
d2 = pd.DataFrame({"s": slope, "f": f12_n.reindex(slope.index)}).dropna()
print(f"r2 copper/gold 12m-MA-slope -> next-12m NIFTY TR (shorter overlap): "
      f"RISING {d2[d2.s>0].f.mean()*100:+.2f}% (n={len(d2[d2.s>0])}) | "
      f"FALLING {d2[d2.s<0].f.mean()*100:+.2f}% (n={len(d2[d2.s<0])})")

# ---------------- r3: silver/gold annual ----------------
gs = pd.read_csv(f"{V}/debt/gold_silver_1915.csv")
gs = gs.set_index("Year")
ratio = gs.Gold_Average_Price / gs.Silver_Average_Price
gold_ann_ret = gs.Gold_Average_Price.pct_change().shift(-1)  # next year's gold return relative to this year's ratio obs
silver_ann_ret = gs.Silver_Average_Price.pct_change().shift(-1)


def fwd_n_year(s, n):
    return (s.shift(-n) / s) - 1


gold_fwd3 = fwd_n_year(gs.Gold_Average_Price, 3)
silver_fwd3 = fwd_n_year(gs.Silver_Average_Price, 3)
lo = ratio.expanding(30).quantile(1/3).shift(1)
hi = ratio.expanding(30).quantile(2/3).shift(1)
tercile = pd.Series(np.where(ratio <= lo, "LOW(silver dear)", np.where(ratio <= hi, "MID", "HIGH(silver cheap)")), index=ratio.index)
tercile[lo.isna()] = np.nan
d3 = pd.DataFrame({"t": tercile, "g": gold_fwd3, "s": silver_fwd3}).dropna()
print("r3 silver/gold ratio terciles -> next-3y gold / next-3y silver (ann. cum., annual data):")
for t in ["LOW(silver dear)", "MID", "HIGH(silver cheap)"]:
    dd = d3[d3.t == t]
    print(f"  {t:>18}: gold {dd.g.mean()*100/3:+.2f}%/yr | silver {dd.s.mean()*100/3:+.2f}%/yr (n={len(dd)})")

# ---------------- r4/r5: NIFTY/gold ratio ----------------
ng = (nifty_m / gold_m.reindex(nifty_m.index)).dropna()
ng_ma = ng.rolling(12).mean()
ng_slope = np.sign(ng_ma - ng_ma.shift(1)).shift(1)
rel_ret_m = nifty_ret_m.reindex(ng.index) - gold_m.pct_change().reindex(ng.index)
f12_rel = fwd_ann(rel_ret_m, 12)
d4 = pd.DataFrame({"s": ng_slope, "f": f12_rel}).dropna()
print(f"r4 NIFTY/gold 12m-MA-slope -> next-12m (NIFTY - gold) relative return: "
      f"RISING {d4[d4.s>0].f.mean()*100:+.2f}% (n={len(d4[d4.s>0])}) | "
      f"FALLING {d4[d4.s<0].f.mean()*100:+.2f}% (n={len(d4[d4.s<0])})")

ng_lo = ng.expanding(120).quantile(1/3).shift(1)
ng_hi = ng.expanding(120).quantile(2/3).shift(1)
ng_t = pd.Series(np.where(ng <= ng_lo, "LOW", np.where(ng <= ng_hi, "MID", "HIGH")), index=ng.index)
ng_t[ng_lo.isna()] = np.nan
d5 = pd.DataFrame({"t": ng_t, "f": f12_rel}).dropna()
print("r5 NIFTY/gold ratio expanding percentile -> next-12m relative return:")
for t in ["LOW", "MID", "HIGH"]:
    dd = d5[d5.t == t]
    print(f"  {t}: {dd.f.mean()*100:+.2f}% (n={len(dd)})")

# ---------------- r6/r7: smallcap/nifty proxy ratio ----------------
small_ret = imkt + ismb
small_idx = (1 + small_ret).cumprod()
mkt_idx = (1 + imkt).cumprod()
sn = (small_idx / mkt_idx).dropna()
sn_ma = sn.rolling(12).mean()
sn_slope = np.sign(sn_ma - sn_ma.shift(1)).shift(1)
f12_smb = fwd_ann(ismb, 12)
d6 = pd.DataFrame({"s": sn_slope, "f": f12_smb.reindex(sn_slope.index)}).dropna()
print(f"r6 smallcap/nifty proxy-ratio 12m-MA-slope -> next-12m SMB: "
      f"RISING {d6[d6.s>0].f.mean()*100:+.2f}% (n={len(d6[d6.s>0])}) | "
      f"FALLING {d6[d6.s<0].f.mean()*100:+.2f}% (n={len(d6[d6.s<0])})")

sn_lo = sn.expanding(120).quantile(1/3).shift(1)
sn_hi = sn.expanding(120).quantile(2/3).shift(1)
sn_t = pd.Series(np.where(sn <= sn_lo, "LOW", np.where(sn <= sn_hi, "MID", "HIGH")), index=sn.index)
sn_t[sn_lo.isna()] = np.nan
d7 = pd.DataFrame({"t": sn_t, "f": f12_smb.reindex(sn_t.index)}).dropna()
print("r7 smallcap/nifty proxy-ratio expanding percentile -> next-12m SMB:")
for t in ["LOW", "MID", "HIGH"]:
    dd = d7[d7.t == t]
    print(f"  {t}: {dd.f.mean()*100:+.2f}% (n={len(dd)})")

# ---------------- r8: the leverage-timing read ----------------
nret_d = nifty_d.pct_change()
vol_ann = nret_d.rolling(252).std() * np.sqrt(252)
vol_lo = vol_ann.expanding(750).quantile(1/3).shift(1)
vol_hi = vol_ann.expanding(750).quantile(2/3).shift(1)
vol_t = pd.Series(np.where(vol_ann <= vol_lo, "LOvol", np.where(vol_ann <= vol_hi, "MIDvol", "HIvol")), index=vol_ann.index)
vol_t[vol_lo.isna()] = np.nan

dd_from_ath = 1 - nifty_d / nifty_d.cummax()
dd_lo = dd_from_ath.expanding(750).quantile(1/3).shift(1)
dd_hi = dd_from_ath.expanding(750).quantile(2/3).shift(1)
dd_t = pd.Series(np.where(dd_from_ath <= dd_lo, "LOWdd", np.where(dd_from_ath <= dd_hi, "MIDdd", "HIGHdd")), index=dd_from_ath.index)
dd_t[dd_lo.isna()] = np.nan

fwd_maxdd_126 = pd.Series(index=nifty_d.index, dtype=float)
vals = nifty_d.values
n = len(vals)
for i in range(n - 126):
    window = vals[i:i + 127]
    running_max = np.maximum.accumulate(window)
    dd = 1 - window / running_max
    fwd_maxdd_126.iloc[i] = dd.max()

r8 = pd.DataFrame({"vol": vol_t, "dd": dd_t, "fdd": fwd_maxdd_126}).dropna()
print("\nr8 THE LEVERAGE-TIMING READ — NIFTY (vol tercile x drawdown tercile) -> fwd-126d max-DD, 9 corners (ranked, smallest first):")
grid = r8.groupby(["vol", "dd"]).fdd.agg(["mean", "count"])
for (v, d_), row in grid.sort_values("mean").iterrows():
    print(f"  {v:>7} x {d_:>7}: fwd max-DD {row['mean']*100:5.2f}% (n={int(row['count'])})")

# ---------------- r9: vol clustering in the ratio ----------------
ng_dlog = np.log(ng).diff().dropna()
abs_ret = ng_dlog.abs()
print("\nr9 vol-clustering in the NIFTY/gold ratio — autocorrelation of |Δlog(ratio)|:")
for lag in [1, 3, 6, 12]:
    ac = abs_ret.autocorr(lag)
    print(f"  lag {lag:>2}m: {ac:+.3f}")
roll_vol = abs_ret.rolling(6).mean()
ac1 = roll_vol.autocorr(1)
halflife_guess = None
for hl in range(1, 60):
    if roll_vol.autocorr(hl) < 0.5 * roll_vol.autocorr(1):
        halflife_guess = hl
        break
print(f"  rolling-6m |Δlog| autocorr(1) = {ac1:+.3f}; half-life (months, informal) ~= {halflife_guess}")
