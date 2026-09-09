"""FUN-D9a (slope-ranks-returns, US monthly verification) + FUN-D10 (monetary regime x
factor returns). Registered 2026-09-09 BEFORE this run. Overlapping fwd windows
FLAGGED; regimes lagged 1m; expanding terciles min 120m. Prints only."""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

sh = pd.read_csv(f"{V}/us_index/sp500_shiller_monthly_1871.csv", parse_dates=["Date"])
sh = sh[sh["Real Price"] > 0].set_index("Date")
gs10 = sh["Long Interest Rate"].replace(0, np.nan)

p = pd.read_csv(f"{V}/factors/fff_monthly_us.csv", skiprows=3)
p.columns = [c.strip() for c in p.columns]
c0 = p.columns[0]
p = p[pd.to_numeric(p[c0], errors="coerce").notna()].copy()
p["ym"] = p[c0].astype(int)
p = p[(p.ym >= 192607) & (p.ym <= 202412)]
p.index = pd.to_datetime(p.ym, format="%Y%m") + pd.offsets.MonthEnd(0)
for c in ["Mkt-RF", "SMB", "HML", "RF"]:
    p[c] = p[c].astype(float) / 100
mkt = p["Mkt-RF"] + p["RF"]
rf_ann = p["RF"] * 1200  # % annualized

gs10.index = gs10.index + pd.offsets.MonthEnd(0)
slope = (gs10.reindex(p.index) - rf_ann).dropna()


def exp_tercile(s, minn=120):
    lo = s.expanding(minn).quantile(1 / 3).shift(1)
    hi = s.expanding(minn).quantile(2 / 3).shift(1)
    t = pd.Series(np.where(s <= lo, "LO", np.where(s <= hi, "MID", "HI")), index=s.index)
    t[lo.isna()] = np.nan
    return t


ter = exp_tercile(slope).shift(1)  # lagged one month
fwd12 = (1 + mkt).rolling(12).apply(np.prod, raw=True).shift(-12) - 1
d = pd.DataFrame({"t": ter, "f": fwd12}).dropna()

print("FUN-D9a — slope terciles -> next-12m US market TR (monthly, overlapping FLAGGED):")
for lab, dd in [("v1 full (1937-2019)", d), ("v2 post-1963", d[d.index >= "1963-01-01"])]:
    row = " | ".join(f"{t} {100*dd[dd.t == t].f.mean():+.1f}% (med {100*dd[dd.t == t].f.median():+.1f})"
                     for t in ["LO", "MID", "HI"])
    print(f"  {lab}: {row}")
row = " | ".join(f"{t} {100*(d[d.t == t].f < 0).mean():.0f}%" for t in ["LO", "MID", "HI"])
print(f"  v3 P(next-12m negative) by tercile: {row}")

ff = pd.read_csv(f"{V}/factors_us/ff6_monthly_1963_2020.csv", parse_dates=["date"]).set_index("date")
regime = np.sign(rf_ann - rf_ann.shift(12)).shift(1)  # +1 rising, -1 falling, lagged

print("\nFUN-D10 — monetary regime (12m short-rate direction, lagged) x factor returns, %/yr:")
tab = {}
for fac in ["MktRF", "SMB", "HML", "RMW", "CMA", "UMD"]:
    s = ff[fac]
    r = regime.reindex(s.index)
    up = s[r > 0].mean() * 1200
    dn = s[r < 0].mean() * 1200
    tab[fac] = (up, dn)
    print(f"  {fac:>6}: RISING {up:+6.2f} | FALLING {dn:+6.2f} | gap {dn - up:+.2f} (1963-2020)")
m_all = p["Mkt-RF"]
r_all = regime.reindex(m_all.index)
print(f"  MktRF 1927-2024: RISING {m_all[r_all > 0].mean()*1200:+.2f} | FALLING {m_all[r_all < 0].mean()*1200:+.2f}")
post = ff[ff.index >= "1990-01-01"]
rp = regime.reindex(post.index)
print("  f7 post-1990:", {fac: f"R{post[fac][rp > 0].mean()*1200:+.1f}/F{post[fac][rp < 0].mean()*1200:+.1f}"
                          for fac in ["MktRF", "RMW", "CMA"]})
