"""
OP-D2 combiner c07: do direction overlays f07 (12-1 momentum sign), f08 (5d z-score MR),
f09 (breadth washout), f11 (overnight gap continuation) add anything to STRUCTURE choice
(condor vs skewed spread)?

This does not re-litigate any family's registered numbers (all four are already
CONFIRMED/PARTIAL on the board with no bar-moving). It asks one new, decision-relevant
question the four family scripts never test against each other: are these four "direction"
signals actually four independent reads on market direction, or do they collapse onto the
SAME underlying rare-crash-rebound episodes (already flagged piecemeal in f07's and f09's own
caveats)? If they're the same few episodes wearing different hats, using any of them to skew
a monthly options STRUCTURE (condor -> put-skewed spread, say) is a bet on 2-3 historical tail
events recurring on schedule, not a usable state variable.

Method: rebuild f07's neg-momentum-sign state and f09's washout state exactly as their own
scripts define them (same vault files, same causal construction), on their shared date range,
and cross-tabulate. Independently, decompose f08's post-2015 continuation days by same-episode
overlap with f07/f09, and check f11's actionability claim (already flagged PARTIAL: VIX-state
label is same-close-contemporaneous with the continuation outcome it explains) by testing
whether shifting the VIX-state label back one day (a genuinely pre-session-known state) still
shows the fade differential.

Vault only. Prints only.
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")
import numpy as np
import pandas as pd
from scipy import stats as sstats

from quant.ladder.credit_cycle import expanding_percentile

NIFTY_CSV = "/home/user/claude-demo/ingest/vault/index/nifty50_daily_2007_2026.csv"
PANEL = "/home/user/claude-demo/ingest/vault/panel/n500_adjclose_2012_2022.csv.gz"
VIX_CSV = "/home/user/claude-demo/ingest/vault/vix/india_vix_daily_2010_2023.csv"

MOM_LOOKBACK, MOM_SKIP = 252, 21
MA_WINDOW, MIN_VALID_NAMES, PCT_MIN_OBS, WASHOUT_PCTL = 200, 100, 252, 0.10

nifty = pd.read_csv(NIFTY_CSV, parse_dates=["Date"]).sort_values("Date").reset_index(drop=True)
nifty = nifty.set_index("Date")
px = nifty["Adj Close"].astype(float)

# ---- rebuild f07 neg-momentum-sign state (same formula as scripts/opt_sweep/f07.py) ----
mom = px.shift(MOM_SKIP) / px.shift(MOM_LOOKBACK) - 1.0
neg_mom = (mom < 0)  # True on negative-momentum-sign days (the "surprise" bucket in f07)

# ---- rebuild f09 washout state (same formula as scripts/opt_sweep/f09.py) ----
panel = pd.read_csv(PANEL, parse_dates=["Date"]).set_index("Date").sort_index()
ma200 = panel.rolling(MA_WINDOW, min_periods=MA_WINDOW).mean()
valid = panel.notna() & ma200.notna()
above = (panel > ma200) & valid
valid_count = valid.sum(axis=1)
above_count = above.sum(axis=1)
breadth = (above_count / valid_count).where(valid_count >= MIN_VALID_NAMES)
pctl = pd.Series(expanding_percentile(breadth.values, min_obs=PCT_MIN_OBS), index=breadth.index)
washout = pctl < WASHOUT_PCTL

# ---- Q1: overlap of neg_mom and washout on their shared date range ----
common = neg_mom.to_frame("neg_mom").join(washout.to_frame("washout"), how="inner").dropna()
n_common = len(common)
n_neg_mom = int(common["neg_mom"].sum())
n_washout = int(common["washout"].sum())
n_both = int((common["neg_mom"] & common["washout"]).sum())
print(f"Q1 shared-window n={n_common} ({common.index.min().date()}..{common.index.max().date()})")
print(f"   neg_mom days={n_neg_mom} ({n_neg_mom/n_common:.1%}), washout days={n_washout} ({n_washout/n_common:.1%})")
print(f"   overlap(neg_mom & washout)={n_both} -> {n_both/n_washout:.1%} of washout days are ALSO neg-mom days"
      f" (vs {n_neg_mom/n_common:.1%} base rate if independent)")

# episode decomposition of the overlap: which calendar spans drive n_both
both_dates = common.index[(common["neg_mom"] & common["washout"])]
if len(both_dates) > 0:
    gaps = both_dates.to_series().diff().dt.days.fillna(999)
    ep_id = (gaps > 10).cumsum()
    episodes = both_dates.to_series().groupby(ep_id.values).agg(["min", "max", "count"])
    episodes = episodes.sort_values("count", ascending=False)
    print(f"   {len(episodes)} contiguous episodes drive the overlap; top 3 by day-count:")
    for _, row in episodes.head(3).iterrows():
        print(f"     {row['min'].date()} .. {row['max'].date()}  ({int(row['count'])}d)")

# ---- Q2: f08's post-2015 continuation days -- what fraction fall in the same overlap episodes? ----
R5 = np.log(px / px.shift(5))
z = pd.Series(index=px.index, dtype=float)
vals = R5.values
zc = np.full(len(vals), np.nan)
for t in range(252, len(vals)):
    w = vals[:t+1]
    w = w[~np.isnan(w)]
    if len(w) < 252:
        continue
    zc[t] = (vals[t] - np.nanmean(w)) / np.nanstd(w, ddof=1)
z = pd.Series(zc, index=px.index)
overbought = z >= 2.0
post2015_over = overbought[(overbought.index >= "2015-01-01") & overbought]
in_overlap_window = post2015_over.index.isin(
    pd.concat([pd.Series(False, index=[d]) for d in []]).index  # placeholder, unused
) if False else None
# simpler: check what fraction of f08's post-2015 EVENT days (oversold OR overbought,
# |z|>=2) sit within +/-5 trading days of a neg_mom&washout overlap episode
event_days = z[(z.index >= "2015-01-01") & (z.abs() >= 2.0)].index
if len(both_dates) > 0:
    near = [any(abs((d - bd).days) <= 7 for bd in both_dates) for d in event_days]
    print(f"Q2 f08 post-2015 |z|>=2 event days: n={len(event_days)}; "
          f"{sum(near)}/{len(event_days)} ({sum(near)/max(len(event_days),1):.0%}) "
          f"fall within +/-7cal days of an f07/f09 overlap episode (COVID/NBFC-type crash windows)")

# ---- Q3: f11 actionability -- lag the VIX-state label by 1 trading day (pre-session-known) ----
vix = pd.read_csv(VIX_CSV, parse_dates=["date"]).set_index("date").sort_index()
vix_close = vix["close"].astype(float)
vix_pctl = pd.Series(expanding_percentile(vix_close.values, min_obs=252), index=vix_close.index)
gap = px.shift(0) / px.shift(1) * np.nan  # placeholder to align index below
o = nifty["Open"].astype(float) if "Open" in nifty.columns else None
c = px
if o is not None:
    gap_t = o / c.shift(1) - 1.0
    intraday_t = c / o - 1.0
    up = gap_t >= 0.01
    down = gap_t <= -0.01
    df3 = pd.concat([intraday_t.rename("intraday"), up.rename("up"), down.rename("down")], axis=1)
    # SAME-DAY (contemporaneous, as f11 built it) vix state
    df3_same = df3.join(vix_pctl.rename("vix_pctl_sameday"), how="inner").dropna()
    # LAGGED (t-1 close, genuinely known before today's session) vix state
    df3_lag = df3.join(vix_pctl.shift(1).rename("vix_pctl_lag1"), how="inner").dropna()

    def hi_lo_diff(d, col, mask_col):
        hi = d[mask_col & (d[col] >= 0.5)]["intraday"]
        lo = d[mask_col & (d[col] < 0.5)]["intraday"]
        if len(hi) < 5 or len(lo) < 5:
            return None, len(hi), len(lo)
        return (hi.mean() - lo.mean()) * 100, len(hi), len(lo)

    d_same_up, nh_su, nl_su = hi_lo_diff(df3_same, "vix_pctl_sameday", df3_same["up"])
    d_lag_up, nh_lu, nl_lu = hi_lo_diff(df3_lag, "vix_pctl_lag1", df3_lag["up"])
    d_same_dn, nh_sd, nl_sd = hi_lo_diff(df3_same, "vix_pctl_sameday", df3_same["down"])
    d_lag_dn, nh_ld, nl_ld = hi_lo_diff(df3_lag, "vix_pctl_lag1", df3_lag["down"])
    print(f"Q3 up-gap hi-lo intraday diff: same-day VIX label={d_same_up:.3f}pp (n_hi={nh_su},n_lo={nl_su}) "
          f"vs t-1(pre-session-known) VIX label={d_lag_up:.3f}pp (n_hi={nh_lu},n_lo={nl_lu})")
    print(f"Q3 down-gap hi-lo intraday diff: same-day VIX label={d_same_dn:.3f}pp (n_hi={nh_sd},n_lo={nl_sd}) "
          f"vs t-1(pre-session-known) VIX label={d_lag_dn:.3f}pp (n_hi={nh_ld},n_lo={nl_ld})")
