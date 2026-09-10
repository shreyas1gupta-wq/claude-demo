"""ES-D1 (EPS rank-migration battery) + SC-D1 (size valuation/growth spread timing)
+ SC-D2 (US SMB time-series predictability) + SC-D3 (India SMB analog).
Registered 2026-09-10 BEFORE this run (ledger entries of record; commit 7cecf2a).
Prints only; interpretation is hand-appended to the ledger AFTER the print.
Forward-return convention: firm_panel row t realizes t+1..t+h (vault AUTH).
Overlapping multi-month windows FLAGGED at registration."""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

# ---------------- firm panel ----------------
use = ["stock_id", "date", "Eps", "Eps_Basic_Gr", "Pb", "Pe", "Mkt_Cap_12M_Usd",
       "Mom_11M_Usd", "Vol1Y_Usd", "R1M_Usd", "R3M_Usd", "R12M_Usd"]
fp = pd.read_csv(f"{V}/firm_panel/data_ml_us_1998_2019.csv.gz", usecols=use,
                 parse_dates=["date"])

eps = fp.pivot_table(index="date", columns="stock_id", values="Eps")
d3 = (eps - eps.shift(3)).stack().rename("d3")
d12 = (eps - eps.shift(12)).stack().rename("d12")
fp = fp.set_index(["date", "stock_id"]).join(d3).join(d12).reset_index()


def dec(s, n=10):
    return np.ceil(s.rank(pct=True) * n).clip(1, n)


fp["d3_d"] = fp.groupby("date").d3.transform(dec)
fp["d12_d"] = fp.groupby("date").d12.transform(dec)

print("ES-D1 — EPS rank-migration (fundamental-momentum proxy), EW, ann. %:")
for cell, col in [("e1 d3(Eps)", "d3_d"), ("e2 d12(Eps)", "d12_d")]:
    lad = fp.groupby(col).R1M_Usd.mean() * 1200
    print(f"  {cell} deciles D1..D10: " + " ".join(f"{lad[i]:+.1f}" for i in range(1, 11))
          + f" | D10-D1 {lad[10]-lad[1]:+.2f}")

big = fp[fp.Mkt_Cap_12M_Usd > 0.8].copy()
for sig in ["d3", "d12"]:
    big[f"{sig}_q"] = big.groupby("date")[sig].transform(dec, n=5)
    l = big.groupby(f"{sig}_q").R1M_Usd.mean() * 1200
    print(f"  e3 large-cap (size>0.8) {sig} quintiles: " +
          " ".join(f"{l[i]:+.1f}" for i in range(1, 6)) + f" | Q5-Q1 {l[5]-l[1]:+.2f}")

h = fp.groupby("d3_d")[["R1M_Usd", "R3M_Usd", "R12M_Usd"]].mean()
print(f"  e4 d3 D10-D1 by horizon (ann.): 1m {(h.loc[10,'R1M_Usd']-h.loc[1,'R1M_Usd'])*1200:+.2f}"
      f" | 3m {(h.loc[10,'R3M_Usd']-h.loc[1,'R3M_Usd'])*400:+.2f}"
      f" | 12m {(h.loc[10,'R12M_Usd']-h.loc[1,'R12M_Usd'])*100:+.2f}")

fp["mom_q"] = fp.groupby("date").Mom_11M_Usd.transform(dec, n=5)
fp["d3_q5"] = fp.groupby(["date", "mom_q"]).d3.transform(dec, n=5)
wm = fp.groupby(["mom_q", "d3_q5"]).R1M_Usd.mean().unstack() * 1200
inc = (wm[5] - wm[1]).mean()
print(f"  e5 within-momentum d3 Q5-Q1 by mom quintile: " +
      " ".join(f"{wm.loc[i,5]-wm.loc[i,1]:+.1f}" for i in range(1, 6)) +
      f" | mean increment {inc:+.2f} (consumption gate: >= +2.00)")

for lab, dd in [("1999-2009", fp[fp.date < "2010-01-01"]), ("2010-2019", fp[fp.date >= "2010-01-01"])]:
    l = dd.groupby("d3_d").R1M_Usd.mean() * 1200
    print(f"  e6 {lab}: d3 D10-D1 {l[10]-l[1]:+.2f}")

fp["vol_h"] = np.where(fp.Vol1Y_Usd > fp.groupby("date").Vol1Y_Usd.transform("median"), "HIvol", "LOvol")
for v in ["LOvol", "HIvol"]:
    dd = fp[fp.vol_h == v].copy()
    dd["q"] = dd.groupby("date").d3.transform(dec, n=5)
    l = dd.groupby("q").R1M_Usd.mean() * 1200
    print(f"  e7 {v}: d3 Q5-Q1 {l[5]-l[1]:+.2f}")

# ---------------- SC-D1: size valuation/growth spread timing ----------------
print("\nSC-D1 — small-vs-large valuation/growth spread -> relative return (IN-SAMPLE, flagged):")
fp["sz_q"] = np.ceil(fp.Mkt_Cap_12M_Usd * 5).clip(1, 5)  # uniformized (0,1] -> quintile
g = fp.groupby(["date", "sz_q"])
m = g.agg(pb=("Pb", "median"), pe=("Pe", "median"), gr=("Eps_Basic_Gr", "median"),
          r1=("R1M_Usd", "mean"), r12=("R12M_Usd", "mean")).unstack()
V_t = m[("pb", 1.0)] - m[("pb", 5.0)]
Vpe = m[("pe", 1.0)] - m[("pe", 5.0)]
G_t = m[("gr", 1.0)] - m[("gr", 5.0)]
SL1 = m[("r1", 1.0)] - m[("r1", 5.0)]
SL12 = m[("r12", 1.0)] - m[("r12", 5.0)]
SL36 = SL12 + SL12.shift(-12) + SL12.shift(-24)  # sum approx, stated


def ter(s):
    return pd.qcut(s, 3, labels=["T1", "T2", "T3"])


for cell, sig in [("v1 Pb-spread", V_t), ("v2 growth-gap", G_t), ("v5 Pe-spread", Vpe)]:
    t = SL12.groupby(ter(sig)).mean() * 100
    print(f"  {cell} terciles -> next-12m small-minus-large: "
          f"T1 {t['T1']:+.2f} | T2 {t['T2']:+.2f} | T3 {t['T3']:+.2f}  (T1-T3 {t['T1']-t['T3']:+.2f}pp)")
for nm, sig in [("V_t(Pb)", V_t), ("G_t", G_t)]:
    c1 = sig.corr(SL1); c12 = sig.corr(SL12); c36 = sig.corr(SL36)
    print(f"  v3 corr({nm}, SL) at 1/12/36m: {c1:+.2f} / {c12:+.2f} / {c36:+.2f} (36m = summed SL12, approx)")
vt, gt = ter(V_t), ter(G_t)
good = SL12[(vt == "T1") & (gt == "T3")]; bad = SL12[(vt == "T3") & (gt == "T1")]
print(f"  v4 corners: cheap-small+growth-favorable n={good.count()} mean {good.mean()*100:+.2f} | "
      f"expensive-small+unfavorable n={bad.count()} mean {bad.mean()*100:+.2f}")

# ---------------- SC-D2: US SMB time series ----------------
p = pd.read_csv(f"{V}/factors/fff_monthly_us.csv", skiprows=3)
p.columns = [c.strip() for c in p.columns]
c0 = p.columns[0]
p = p[pd.to_numeric(p[c0], errors="coerce").notna()].copy()
p["ym"] = p[c0].astype(int)
p = p[(p.ym >= 192607) & (p.ym <= 202412)]
p.index = pd.to_datetime(p.ym, format="%Y%m") + pd.offsets.MonthEnd(0)
for c in ["Mkt-RF", "SMB", "RF"]:
    p[c] = p[c].astype(float)
smb = p["SMB"]; mkt = p["Mkt-RF"] + p["RF"]


def ts_cells(s, mret, tag):
    tr12 = s.rolling(12).sum()
    nxt12 = s.rolling(12).sum().shift(-12)
    pos, neg = nxt12[tr12 > 0], nxt12[tr12 < 0]
    print(f"  {tag}1 12m momentum: after + years {pos.mean():+.2f}%/12m (P(next>0) {100*(pos>0).mean():.0f}%)"
          f" | after - years {neg.mean():+.2f}% (P {100*(neg>0).mean():.0f}%) | spread {pos.mean()-neg.mean():+.2f}")
    tr36 = s.rolling(36).sum()
    lo = tr36.expanding(120).quantile(1/3).shift(1)
    hi = tr36.expanding(120).quantile(2/3).shift(1)
    t = pd.Series(np.where(tr36 <= lo, "LO", np.where(tr36 <= hi, "MID", "HI")), index=s.index)
    t[lo.isna()] = np.nan
    d = pd.DataFrame({"t": t, "f": nxt12}).dropna()
    r = d.groupby("t").f.mean()
    print(f"  {tag}2 36m reversal terciles -> next 12m: LO {r.get('LO',np.nan):+.2f} | "
          f"MID {r.get('MID',np.nan):+.2f} | HI {r.get('HI',np.nan):+.2f}")
    m12 = mret.rolling(12).sum()
    dn, up = nxt12[m12 < 0], nxt12[m12 > 0]
    print(f"  {tag}3 after DOWN market year {dn.mean():+.2f}%/12m (n={dn.count()})"
          f" vs after up {up.mean():+.2f}% | gap {dn.mean()-up.mean():+.2f}")
    return tr12, nxt12


print("\nSC-D2 — US SMB time-series predictability 1926-2024 (overlapping FLAGGED):")
tr12, nxt12 = ts_cells(smb, mkt, "t")
for lab, d0, d1 in [("1927-1980", "1927", "1980"), ("1981-2000", "1981", "2000"), ("2001-2024", "2001", "2024")]:
    sl = slice(d0, d1)
    sp = nxt12[sl][tr12[sl] > 0].mean() - nxt12[sl][tr12[sl] < 0].mean()
    print(f"  t4 {lab}: momentum spread {sp:+.2f}%/12m")

# ---------------- SC-D3: India SMB (IIMA) ----------------
ii = pd.read_csv(f"{V}/factors/iima_monthly_factors.csv", na_values="NA")
ii.index = pd.to_datetime(ii.Date, format="%Y-%m") + pd.offsets.MonthEnd(0)
ismb = ii.SMB.astype(float)
imkt = (ii.MF + ii.RF).astype(float)  # market total return where both available
print("\nSC-D3 — India SMB (IIMA 1993-2025) analog (overlapping FLAGGED; MF NA head stated):")
ts_cells(ismb, imkt, "i")
roll5 = ismb.rolling(60).mean() * 12
print(f"  i4 rolling-5y SMB mean (ann. %): min {roll5.min():+.1f} ({roll5.idxmin():%Y-%m}) | "
      f"max {roll5.max():+.1f} ({roll5.idxmax():%Y-%m}) | 2018-12 {roll5.get(pd.Timestamp('2018-12-31'), np.nan):+.1f}"
      f" | 2021-12 {roll5.get(pd.Timestamp('2021-12-31'), np.nan):+.1f}"
      f" | 2024-12 {roll5.get(pd.Timestamp('2024-12-31'), np.nan):+.1f}"
      f" | latest {roll5.dropna().iloc[-1]:+.1f} ({roll5.dropna().index[-1]:%Y-%m})")
print(f"  i4 full-period IIMA SMB mean: {ismb.mean()*12:+.2f}%/yr (context; TL-D2 s8 verdict quoted, not re-derived)")
