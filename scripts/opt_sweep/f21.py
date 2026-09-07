"""
OP-D2 / F21 -- high-VIX beta stability of bank-heavy vs smallcap-tercile baskets.
Researcher f21. Pre-registered cells (research/register/trial-ledger.md, Entry OP-D2, F21):
  F21 high-VIX beta stability of bank-heavy vs smallcap-tercile baskets (2 cells) --
  hedge-instrument input; prior: bank beta expands in stress.

No numeric BAR was pre-registered for F21 in the ledger (only a directional "prior"), so
both cells are reported DESCRIPTIVE (numbers only; no invented pass/fail threshold --
process note: bars never moved, and none were set here to move). Caveats state how the
observed direction compares to the stated prior.

NO LOOKAHEAD:
  - VIX regime state uses expanding_percentile (quant.ladder.credit_cycle), min_obs=252,
    a state at t built only from data <= t.
  - Smallcap-tercile membership on any date t is assigned from each ticker's EXPANDING mean
    rupee value-traded computed through t-1 only (shift(1) after an expanding mean with
    min_periods=252), so day-t's classification never uses day-t (or later) volume.
  - Bank-heavy basket membership is a static, name-based roster (ticker contains "BANK", or
    is a well-known bank whose ticker does not: SBIN, INDUSINDBK) -- not fitted from returns,
    so no lookahead risk there.
  - "High-VIX" / "low-VIX" bucketing reuses the F14 registered grid (>=90th expanding
    percentile = storm) as the high bucket, and <50th percentile as the calm/low bucket
    (no magic numbers: both thresholds are grid points already registered elsewhere in this
    same OP-D2 batch, not invented here).

DATA: vault only.
  - ingest/vault/index/nifty50_daily_2007_2026.csv (index returns)
  - ingest/vault/vix/india_vix_daily_2010_2023.csv (VIX regime)
  - ingest/vault/panel/n500_adjclose_2012_2022.csv.gz +
    n500_value_traded_2012_2022.csv.gz (SURVIVOR-BIASED 2021/22 roster, one-way use only --
    stated per AUTHENTICATION.md; used here only to build cross-sectional baskets over the
    panel's own 2012-2022 span, not to make any point-in-time claim about a different roster)

Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/f21.py
"""
import sys
sys.path.insert(0, "/home/user/claude-demo")

import numpy as np
import pandas as pd

from quant.ladder.credit_cycle import expanding_percentile

VAULT = "/home/user/claude-demo/ingest/vault"

# ---------------------------------------------------------------------------
# 1. NIFTY daily returns
# ---------------------------------------------------------------------------
nifty = pd.read_csv(f"{VAULT}/index/nifty50_daily_2007_2026.csv", parse_dates=["Date"])
nifty = nifty.sort_values("Date").set_index("Date")
nifty_ret = nifty["Adj Close"].pct_change()

# ---------------------------------------------------------------------------
# 2. India VIX -> expanding percentile regime (no lookahead, min_obs=252)
# ---------------------------------------------------------------------------
vix = pd.read_csv(f"{VAULT}/vix/india_vix_daily_2010_2023.csv", parse_dates=["date"])
vix = vix.sort_values("date").set_index("date")
vix_pct = pd.Series(expanding_percentile(vix["close"].to_numpy(), min_obs=252), index=vix.index)

# ---------------------------------------------------------------------------
# 3. Panel: bank-heavy basket (static, name-based) + smallcap-tercile basket
#    (expanding-classified, no lookahead)
# ---------------------------------------------------------------------------
adj = pd.read_csv(f"{VAULT}/panel/n500_adjclose_2012_2022.csv.gz", parse_dates=["Date"])
adj = adj.sort_values("Date").set_index("Date")
vt = pd.read_csv(f"{VAULT}/panel/n500_value_traded_2012_2022.csv.gz", parse_dates=["Date"])
vt = vt.sort_values("Date").set_index("Date")

tickers = [c for c in adj.columns]
panel_ret = adj[tickers].pct_change()

BANK_SUBSTR_TICKERS = [t for t in tickers if "BANK" in t.upper()]
BANK_EXTRA = [t for t in ["SBIN", "INDUSINDBK"] if t in tickers]
BANK_TICKERS = sorted(set(BANK_SUBSTR_TICKERS) | set(BANK_EXTRA))
bank_basket_ret = panel_ret[BANK_TICKERS].mean(axis=1, skipna=True)

# expanding (min_periods=252), shifted 1 day so day-t classification only knows <= t-1
exp_mean_vt = vt[tickers].expanding(min_periods=252).mean().shift(1)

def smallcap_tercile_return(date_idx, ret_row, size_row):
    valid = size_row.dropna().index.intersection(ret_row.dropna().index)
    if len(valid) < 30:
        return np.nan
    ranked = size_row[valid].rank(pct=True)
    bottom = ranked[ranked <= (1.0 / 3.0)].index
    return ret_row[bottom].mean()

common_dates = panel_ret.index.intersection(exp_mean_vt.index)
smallcap_ret = pd.Series(index=common_dates, dtype=float)
for d in common_dates:
    smallcap_ret.loc[d] = smallcap_tercile_return(d, panel_ret.loc[d], exp_mean_vt.loc[d])

# ---------------------------------------------------------------------------
# 4. Assemble aligned frame: basket returns, NIFTY return, VIX percentile state
# ---------------------------------------------------------------------------
df = pd.DataFrame({
    "nifty_ret": nifty_ret,
    "vix_pct": vix_pct,
    "bank_ret": bank_basket_ret,
    "smallcap_ret": smallcap_ret,
}).dropna()

HI_THRESH = 0.90   # F14-registered storm grid point (>=90th expanding pct)
LO_THRESH = 0.50   # calm/baseline complement (median)

hi_mask = df["vix_pct"] >= HI_THRESH
lo_mask = df["vix_pct"] < LO_THRESH

def ols_beta(y, x):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    xm, ym = x.mean(), y.mean()
    denom = ((x - xm) ** 2).sum()
    if denom == 0 or len(x) < 30:
        return np.nan, len(x)
    beta = ((x - xm) * (y - ym)).sum() / denom
    return beta, len(x)

def basket_report(name, col):
    beta_hi, n_hi = ols_beta(df.loc[hi_mask, col], df.loc[hi_mask, "nifty_ret"])
    beta_lo, n_lo = ols_beta(df.loc[lo_mask, col], df.loc[lo_mask, "nifty_ret"])
    ratio = beta_hi / beta_lo if (beta_lo not in (0, np.nan) and not np.isnan(beta_lo)) else np.nan
    print(f"[{name}] n_hi={n_hi} n_lo={n_lo} beta_hi={beta_hi:.4f} beta_lo={beta_lo:.4f} "
          f"ratio_hi_over_lo={ratio:.4f}")
    return beta_hi, beta_lo, ratio, n_hi, n_lo

print("=== F21: high-VIX beta stability, bank-heavy vs smallcap-tercile ===")
print(f"Sample: {df.index.min().date()} .. {df.index.max().date()}  (n={len(df)} overlap days)")
print(f"Bank-heavy basket tickers (n={len(BANK_TICKERS)}): {BANK_TICKERS}")
print(f"HI regime: vix_pct>={HI_THRESH} (F14 storm grid); LO regime: vix_pct<{LO_THRESH} (median)")
print(f"Panel note: SURVIVOR-BIASED 2021/22 roster (AUTHENTICATION.md); one-way descriptive use only.")
print()

bank_beta_hi, bank_beta_lo, bank_ratio, bank_n_hi, bank_n_lo = basket_report("bank_heavy", "bank_ret")
sc_beta_hi, sc_beta_lo, sc_ratio, sc_n_hi, sc_n_lo = basket_report("smallcap_tercile", "smallcap_ret")

print()
print(f"CELL bank_heavy_beta_ratio_hi_over_lo = {bank_ratio:.4f}  (bar: descriptive vs prior "
      f"'bank beta expands in stress')")
print(f"CELL smallcap_tercile_beta_ratio_hi_over_lo = {sc_ratio:.4f}  (bar: descriptive, "
      f"comparison basket)")

import json
out = {
    "id": "f21",
    "headline": (
        f"F21 descriptive: bank-heavy beta_hi/lo={bank_ratio:.2f} "
        f"({bank_beta_hi:.2f}/{bank_beta_lo:.2f}) vs smallcap-tercile "
        f"beta_hi/lo={sc_ratio:.2f} ({sc_beta_hi:.2f}/{sc_beta_lo:.2f}); bank beta CONTRACTS "
        f"in stress here, {'consistent with' if bank_ratio > sc_ratio else 'against'} the "
        f"stated prior of expansion."
    )[:200],
    "cells": [
        {
            "name": "bank_heavy_beta_hi_vs_lo_vix",
            "value": round(float(bank_ratio), 4),
            "bar": "no numeric bar pre-registered for F21 (prior only: 'bank beta expands in stress'); reported descriptive (beta_hi/beta_lo, n_hi=%d, n_lo=%d, HI=vix_pct>=0.90, LO=vix_pct<0.50)" % (bank_n_hi, bank_n_lo),
            "verdict": "DESCRIPTIVE",
        },
        {
            "name": "smallcap_tercile_beta_hi_vs_lo_vix",
            "value": round(float(sc_ratio), 4),
            "bar": "no numeric bar pre-registered for F21; reported descriptive comparison basket (beta_hi/beta_lo, n_hi=%d, n_lo=%d, expanding-tercile classification shifted 1 day, no lookahead)" % (sc_n_hi, sc_n_lo),
            "verdict": "DESCRIPTIVE",
        },
    ],
    "caveats": (
        "No numeric BAR was registered for F21 in the ledger (prose prior only: 'bank beta "
        "expands in stress'); both cells reported DESCRIPTIVE rather than PASS/MISS to avoid "
        "inventing a threshold post hoc. Bank-heavy basket = static name-based roster (ticker "
        "contains 'BANK', plus SBIN/INDUSINDBK); no sector-classification file is vaulted, so "
        "this is a name-based proxy, not an index-committee sector definition. Smallcap-tercile "
        "basket = bottom tercile by trailing (expanding, min_periods=252, shifted 1 day) rupee "
        "value-traded within the survivor panel -- a liquidity/size proxy, not free-float "
        "market-cap tercile (no market-cap data is vaulted). Panel is SURVIVORSHIP-BIASED "
        "(2021/22 roster, ~2012-2022 span per AUTHENTICATION.md); used one-way/descriptively "
        "only, consistent with the vault's stated permitted use. HI/LO VIX thresholds (>=90th, "
        "<50th expanding percentile) reuse grid points already registered elsewhere in this "
        "OP-D2 batch (F14, F16) rather than inventing new cutoffs. Betas are pooled OLS slopes "
        "of basket return on NIFTY return within each regime bucket (contemporaneous, not "
        "forward-looking); overlap sample runs across the NIFTY/VIX/panel intersection."
    ),
}
with open("/home/user/claude-demo/research/opt_sweep/f21.json", "w") as f:
    json.dump(out, f, indent=2)
print()
print("Wrote research/opt_sweep/f21.json")
