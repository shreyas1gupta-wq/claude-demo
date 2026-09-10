"""SNAPSHOT-1 -- the current-state readout, registered 2026-09-10 BEFORE this run.
Descriptive only (no bars/hypothesis -- a "where are we now" reporting exercise, not
a trial): applies constructions ALREADY established in booked ledger entries (TECH-D1
drawdown terciles, TECH-D2 stage quadrants, SC-D3/TL-D2 SMB regime map, RATIO-D1
NIFTY/gold trend+percentile, CU-D5/SEC weak-INR-year threshold, FUN-D8 RF regime) to
the LATEST available date in each vault series. Every construction is quoted verbatim
from its parent design (process note #5); no new bar is set because nothing is being
tested -- this is a state reading only. Prints only; interpretation hand-appended after."""
import numpy as np
import pandas as pd

V = "/home/user/claude-demo/ingest/vault"

# --- NIFTY ---
n = pd.read_csv(f"{V}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"]).sort_values("Date")
n = n.set_index("Date")
px = n["Adj Close"]
asof_nifty = px.index[-1]
last_px = px.iloc[-1]
ath = px.cummax()
dd = px / ath - 1
cur_dd = dd.iloc[-1]
# drawdown terciles (TECH-D1 convention: own-history expanding terciles of daily drawdown)
dd_rank = dd.rank(pct=True).iloc[-1]
dd_tercile = "DEEP" if dd_rank <= 1/3 else ("MID" if dd_rank <= 2/3 else "LOW")
# trailing-12m return (SC-D3 up/down-year convention: calendar-ish trailing 252d)
r12m = px.iloc[-1] / px.iloc[-253] - 1
up_year = r12m > 0
# 200d MA + slope (TECH-D2 stage quadrant convention)
ma200 = px.rolling(200).mean()
ma200_slope = ma200.iloc[-1] - ma200.iloc[-21]  # ~1m slope
above_ma = last_px > ma200.iloc[-1]
rising_ma = ma200_slope > 0
stage = ("S2" if above_ma and rising_ma else
         "S3" if above_ma and not rising_ma else
         "S1" if not above_ma and rising_ma else "S4")
# 52w high proximity
hi52 = px.rolling(252).max().iloc[-1]
prox52 = last_px / hi52 - 1

print(f"NIFTY as-of {asof_nifty.date()}: last={last_px:.1f} ATH_to_date={ath.iloc[-1]:.1f} "
      f"drawdown={cur_dd*100:.2f}% (tercile-rank {dd_rank:.2f} -> {dd_tercile}) "
      f"r12m={r12m*100:.2f}% ({'UP' if up_year else 'DOWN'} year) "
      f"stage={stage} (above_ma200={above_ma}, ma200_slope_1m={ma200_slope:.1f}) "
      f"52w_high_proximity={prox52*100:.2f}%")

# --- GOLD ---
g = pd.read_csv(f"{V}/commodities/gold_monthly_1833_2026.csv", parse_dates=["Date"])
g = g.set_index("Date")["Price"].sort_index()
asof_gold = g.index[-1]
g_r12m = g.iloc[-1] / g.iloc[-13] - 1
g_ma12 = g.rolling(12).mean()
g_above_ma = g.iloc[-1] > g_ma12.iloc[-1]
print(f"GOLD as-of {asof_gold.date()}: last={g.iloc[-1]:.0f} r12m={g_r12m*100:.2f}% "
      f"above_12m_MA={g_above_ma}")

# --- NIFTY/gold ratio (RATIO-D1 r4/r5 convention: monthly, 12m-MA slope + expanding percentile) ---
nm = px.resample("ME").last()
gm = g.reindex(nm.index, method="ffill")
ratio = nm / gm
ratio = ratio.dropna()
r_ma12 = ratio.rolling(12).mean()
r_slope = r_ma12.iloc[-1] - r_ma12.iloc[-2]
r_pct = ratio.rank(pct=True).iloc[-1]
r_bucket = "HIGH" if r_pct >= 2/3 else ("LOW" if r_pct <= 1/3 else "MID")
print(f"NIFTY/GOLD ratio as-of {ratio.index[-1].date()}: level={ratio.iloc[-1]:.2f} "
      f"12m-MA slope={'RISING' if r_slope>0 else 'FALLING'} percentile={r_pct:.2f} ({r_bucket})")

# --- IIMA factors: WML trailing state + SMB regime map + RF trend ---
f = pd.read_csv(f"{V}/factors/iima_monthly_factors.csv")
f["Date"] = pd.to_datetime(f["Date"], format="%Y-%m")
f = f.set_index("Date").sort_index()
asof_f = f.index[-1]
wml_3m = (1 + f["WML"].iloc[-3:] / 100).prod() - 1
wml_1m = f["WML"].iloc[-1] / 100
smb_5y = f["SMB"].iloc[-60:].mean()  # rolling-5y mean, SC-D3 i4 / TL-D2 regime-map convention
rf_now = f["RF"].dropna().iloc[-1]
rf_12m_ago = f["RF"].dropna().iloc[-13]
rf_dir = "RISING" if rf_now > rf_12m_ago else "FALLING"
print(f"IIMA as-of {asof_f.date()}: WML last-1m={wml_1m*100:.2f}% last-3m-cum={wml_3m*100:.2f}% "
      f"SMB rolling-5y mean={smb_5y:.2f}%/mo (regime map units, cf SC-D3 i4/TL-D2) "
      f"RF={rf_now:.2f}% vs 12m-ago={rf_12m_ago:.2f}% -> {rf_dir}")

# --- FX: weak-INR-year classification (SEC-D2/CU-D5 convention: calendar dlog(INR/USD) >= +5%) ---
fx = pd.read_csv(f"{V}/fx/inr_usd_monthly_1973_2026.csv", parse_dates=["Date"])
fx = fx.set_index("Date")["INR_per_USD"].sort_index()
asof_fx = fx.index[-1]
fx_r12m = np.log(fx.iloc[-1] / fx.iloc[-13])
weak_inr = fx_r12m >= 0.05
crash = fx_r12m >= 0.15
print(f"FX as-of {asof_fx.date()}: INR/USD={fx.iloc[-1]:.2f} trailing-12m dlog={fx_r12m*100:.2f}% "
      f"weak_INR_year={weak_inr} crash_threshold(>=15%)={crash}")

# --- Global vol proxy (CBOE VIX -- India VIX vault stale since 2023-04, stated) ---
vx = pd.read_csv(f"{V}/globalvol/cboe_vix_daily_1990_2026.csv", parse_dates=["DATE"])
vx = vx.set_index("DATE")["CLOSE"].sort_index()
asof_vx = vx.index[-1]
vx_now = vx.iloc[-1]
vx_pct = vx.rank(pct=True).iloc[-1]
vx_tercile = "HIGH" if vx_pct >= 2/3 else ("LOW" if vx_pct <= 1/3 else "MID")
print(f"CBOE VIX as-of {asof_vx.date()}: level={vx_now:.2f} percentile={vx_pct:.2f} ({vx_tercile} tercile) "
      f"[India VIX vault stale since 2023-04 -- not usable for a current India-specific vol read]")

# --- Copper/gold: explicitly stale, stated not computed ---
print("Copper/gold (RATIO-D1 r1): IMF PCPS vault stops 2017-06 -- NO current read possible, stated as a gap")
