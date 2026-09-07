"""TL-D2 — atlas extension: S&P 155y monthly, US market 99y, small vs large (US+India).

Registered 2026-09-07 BEFORE this run. Prints + appends to tl_atlas_stats.json (key d2).
"""
import json
import sys

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, "/home/user/claude-demo")
ROOT = "/home/user/claude-demo"


def sigma_table(r, name, ks=(2, 3, 4, 6)):
    z = (r - r.mean()) / r.std()
    n = len(r)
    out = []
    print(f"  {name} (n={n}, sd {100*r.std():.2f}%): ", end="")
    for k in ks:
        obs = int((z.abs() >= k).sum())
        gauss = 2 * stats.norm.sf(k) * n
        out.append(dict(k=k, obs=obs, gauss=gauss))
        print(f"|z|>={k}: {obs} vs {gauss:.2f} ({obs/gauss if gauss > 1e-9 else float('inf'):.0f}x)  ", end="")
    print(f"| ex.kurt {stats.kurtosis(r):.1f}, skew {stats.skew(r):+.2f}, AR1 {r.autocorr(1):+.2f}")
    return out


def dd_stats(r):
    idx = np.log1p(r).cumsum()
    dd = idx - idx.cummax()
    return 100 * (1 - np.exp(dd.min())), dd.idxmin()


def horizons(r, py):
    lr = np.log1p(r)
    res = []
    for yrs in (1, 5, 10, 20):
        w = lr.rolling(yrs * py).sum().dropna()
        cagr = np.expm1(w / yrs)
        res.append((yrs, 100*cagr.mean(), 100*cagr.min(), 100*(cagr > 0).mean()))
    return res


D2 = {}
# ---- s1/s2: S&P nominal monthly 1871-2026 ----
sh = pd.read_csv(f"{ROOT}/ingest/vault/us_index/sp500_shiller_monthly_1871.csv",
                 parse_dates=["Date"]).set_index("Date").sort_index()
spx = sh.SP500.pct_change().dropna()
print("s1/s2 — S&P NOMINAL MONTHLY 1871-2026 (monthly-AVERAGE smoothing flag):")
D2["spx_sigma"] = sigma_table(spx, "S&P 1871-2026")
w, wd = spx.nsmallest(5), spx.nlargest(5)
print("  worst months:", [(str(d.date())[:7], f"{100*x:.1f}%") for d, x in w.items()])
print("  best months: ", [(str(d.date())[:7], f"{100*x:.1f}%") for d, x in wd.items()])
D2["spx"] = dict(n=len(spx), sd=float(spx.std()), ek=float(stats.kurtosis(spx)),
                 sk=float(stats.skew(spx)),
                 worst=[[str(d.date())[:7], round(100*x, 1)] for d, x in w.items()],
                 best=[[str(d.date())[:7], round(100*x, 1)] for d, x in wd.items()])

# ---- s3-s6: US market + small, FF3 monthly ----
ff = pd.read_csv(f"{ROOT}/ingest/vault/factors/fff_monthly_us.csv", skiprows=3)
ff.columns = ["ym"] + [c.strip() for c in ff.columns[1:]]
ff = ff[ff.ym.astype(str).str.match(r"^\s*\d{6}\s*$", na=False)].astype(float)
ff.index = pd.to_datetime(ff.ym.astype(int).astype(str), format="%Y%m")
mkt = (ff["Mkt-RF"] + ff.RF) / 100
sml = mkt + ff.SMB / 100
print("\ns3 — US MARKET monthly total return 1926-07..2024-11 (CRSP VW, true month-end):")
D2["usmkt_sigma"] = sigma_table(mkt, "US market 99y")
print("  worst:", [(str(d.date())[:7], f"{100*x:.1f}%") for d, x in mkt.nsmallest(3).items()],
      "best:", [(str(d.date())[:7], f"{100*x:.1f}%") for d, x in mkt.nlargest(3).items()])
print("\ns4/s5 — US SMALL (mkt+SMB proxy) vs MARKET:")
D2["ussml_sigma"] = sigma_table(sml, "US small 99y ")
dm, tm = dd_stats(mkt)
ds, ts = dd_stats(sml)
print(f"  vol ratio small/mkt = {sml.std()/mkt.std():.2f}x | worst month small "
      f"{100*sml.min():.1f}% vs mkt {100*mkt.min():.1f}% | max drawdown (nominal TR): "
      f"small {ds:.0f}% ({str(ts.date())[:7]}) vs mkt {dm:.0f}% ({str(tm.date())[:7]})")
print(f"  s5 AR(1): small {sml.autocorr(1):+.2f} vs market {mkt.autocorr(1):+.2f}")
print("\ns6 — US horizons (nominal CAGR %/yr: mean / worst / %>0), overlap flagged:")
hm, hs = horizons(mkt, 12), horizons(sml, 12)
for (y, a, b, c), (_, a2, b2, c2) in zip(hm, hs):
    print(f"  {y:>2}y  market {a:5.1f} / {b:6.1f} / {c:3.0f}%   small {a2:5.1f} / {b2:6.1f} / {c2:3.0f}%")
D2["us_hz"] = dict(mkt=hm, sml=hs, volratio=float(sml.std()/mkt.std()),
                   dd=dict(mkt=[dm, str(tm.date())[:7]], sml=[ds, str(ts.date())[:7]]),
                   ar1=[float(mkt.autocorr(1)), float(sml.autocorr(1))],
                   mean=[float(12*mkt.mean()), float(12*sml.mean())])

# ---- s7/s8: India monthly market + small (IIMA) ----
im = pd.read_csv(f"{ROOT}/ingest/vault/factors/iima_monthly_factors.csv")
im.index = pd.to_datetime(im.Date, format="%Y-%m")
imkt = ((im.MF + im.RF) / 100).dropna()
isml = (imkt + im.SMB / 100).dropna()
print("\ns7/s8 — INDIA monthly (IIMA, nominal, 1993-2025):")
D2["inmkt_sigma"] = sigma_table(imkt, "India market ")
D2["insml_sigma"] = sigma_table(isml, "India small  ")
dmi, tmi = dd_stats(imkt)
dsi, tsi = dd_stats(isml)
print(f"  vol ratio small/mkt = {isml.std()/imkt.std():.2f}x | worst month small "
      f"{100*isml.min():.1f}% vs mkt {100*imkt.min():.1f}% | maxDD small {dsi:.0f}% "
      f"({str(tsi.date())[:7]}) vs mkt {dmi:.0f}% ({str(tmi.date())[:7]}) | AR(1) small "
      f"{isml.autocorr(1):+.2f} vs mkt {imkt.autocorr(1):+.2f} | full-period mean "
      f"small {100*12*isml.mean():.1f}%/yr vs mkt {100*12*imkt.mean():.1f}%/yr")
D2["in_sum"] = dict(volratio=float(isml.std()/imkt.std()),
                    dd=dict(mkt=[dmi, str(tmi.date())[:7]], sml=[dsi, str(tsi.date())[:7]]),
                    ar1=[float(imkt.autocorr(1)), float(isml.autocorr(1))],
                    mean=[float(12*imkt.mean()), float(12*isml.mean())])

# ---- s9/s10: India small DAILY (survivor bottom tercile by value traded) ----
px = pd.read_csv(f"{ROOT}/ingest/vault/panel/n500_adjclose_2012_2022.csv.gz",
                 parse_dates=["Date"]).set_index("Date").sort_index()
vt = pd.read_csv(f"{ROOT}/ingest/vault/panel/n500_value_traded_2012_2022.csv.gz",
                 parse_dates=["Date"]).set_index("Date").sort_index()
ret = px.pct_change(fill_method=None)
parts = []
for y in range(2013, 2022):
    med = vt.loc[f"{y-1}-01-01":f"{y-1}-12-31"].median()
    med = med[med > 0].dropna()
    small_names = med[med.rank(pct=True) <= 1/3].index
    parts.append(ret.loc[f"{y}-01-01":f"{y}-12-31", small_names].mean(axis=1))
smd = pd.concat(parts).sort_index().dropna()
nf = pd.read_csv(f"{ROOT}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                 parse_dates=["Date"]).set_index("Date").sort_index()
n50 = nf["Adj Close"].pct_change().dropna()
n50 = n50[(n50.index >= smd.index[0]) & (n50.index <= smd.index[-1])]
print("\ns9/s10 — INDIA SMALL DAILY (survivor bottom-tercile by value traded, 2013-2021;")
print("  SURVIVORSHIP AT MAXIMUM — severe lower bound on damage):")
D2["insml_d_sigma"] = sigma_table(smd, "IN small daily")
D2["n50_d_sigma"] = sigma_table(n50, "NIFTY50 match ")
ac = [float(smd.abs().autocorr(l)) for l in range(1, 31)]
vol21 = smd.rolling(21).std() * np.sqrt(252)
phi = float(vol21.dropna().autocorr(1))
print(f"  s10 clustering: |r| autocorr lag1 {ac[0]:+.2f} / lag30 {ac[29]:+.2f}, all>0: "
      f"{all(a > 0 for a in ac)}; vol AR1 phi {phi:.3f} -> half-life {np.log(0.5)/np.log(phi):.0f}d")
dds, tds = dd_stats(smd)
ddn, tdn = dd_stats(n50)
print(f"  maxDD 2013-21: small {dds:.0f}% ({str(tds.date())}) vs NIFTY50 {ddn:.0f}%; "
      f"CAGR small {100*(np.expm1(np.log1p(smd).mean()*252)):.1f}%/yr vs NIFTY50 "
      f"{100*(np.expm1(np.log1p(n50).mean()*252)):.1f}%/yr (survivor-inflated, both)")
D2["in_daily"] = dict(sm_ek=float(stats.kurtosis(smd)), n50_ek=float(stats.kurtosis(n50)),
                      sm_sd=float(smd.std()), n50_sd=float(n50.std()), phi=phi,
                      dd=[dds, ddn])

with open(f"{ROOT}/research/notes/tl_atlas_stats.json") as f:
    D = json.load(f)
D["d2"] = D2
with open(f"{ROOT}/research/notes/tl_atlas_stats.json", "w") as f:
    json.dump(D, f)
print("\nd2 stats appended")
