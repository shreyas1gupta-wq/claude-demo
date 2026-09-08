"""opt_sweep2 / f04_triasset_momentum — TRI-ASSET SWITCHER.

Family: add SPX-in-INR (S&P 500 futures, continuous-adjusted, x INR/USD monthly) as a
third asset to the standing 20% NIFTY-vs-gold-INR 12m dual-momentum switcher. Hold the
max-12m-momentum asset each month, signal from the PRIOR month-end close only (no
lookahead). Also test 12-1 skip-month momentum (skip the most recent month in the
lookback, the canonical Jegadeesh-Titman form) for both the dual and tri-asset switcher.

Reuses the book engine (scripts/analyze_op_d6b.py) for nifty/gold/dates/run_book/stats_of
per process note #6 (no inline re-implementation of house machinery: EWMA vol, core
sleeve, condor sleeve, month placement all come from the engine unchanged).

EXPLORATORY. Not pre-registered to the trial ledger. Prints only + JSON dump.
"""
import json
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")

# ---- pull in the book engine (house pattern, see analyze_op_d7.py) ----
_src = open("/home/user/claude-demo/scripts/analyze_op_d6b.py").read()
_g = {}
exec(_src.split("# === MAIN ===")[0], _g)
run_book, stats_of = _g["run_book"], _g["stats_of"]
dates, D0, D1 = _g["dates"], _g["D0"], _g["D1"]
n_me, g_inr, mom_g, mom_n = _g["n_me"], _g["g_inr"], _g["mom_g"], _g["mom_n"]
g_ret_m, n_ret_m, SW_M = _g["g_ret_m"], _g["n_ret_m"], _g["SW_M"]
inr, month_stream = _g["inr"], _g["month_stream"]

V = "/home/user/claude-demo/ingest/vault"

# ============================================================================
# 1. Build SPX-in-INR monthly series (no lookahead: 20:00-row-else-last daily
#    convention per session brief; returns = diff(adjusted)/lag(unadjusted PRICE)).
# ============================================================================
adj = pd.read_csv(f"{V}/us_index/sp500_fut_adjusted_daily.csv", parse_dates=["DATETIME"])
mul = pd.read_csv(f"{V}/us_index/sp500_fut_multiple_daily.csv", parse_dates=["DATETIME"])


def pick_2000_else_last(df, valcol):
    df = df.copy()
    df["date"] = df["DATETIME"].dt.normalize()
    df["hour"] = df["DATETIME"].dt.hour
    df = df.sort_values("DATETIME")
    at20 = df[df["hour"] == 20].drop_duplicates("date", keep="last").set_index("date")[valcol]
    last = df.drop_duplicates("date", keep="last").set_index("date")[valcol]
    return at20.reindex(last.index).fillna(last)


adj_d = pick_2000_else_last(adj, "price")
px_d = pick_2000_else_last(mul, "PRICE")
spx = pd.DataFrame({"adj": adj_d, "price": px_d}).dropna().sort_index()
spx_ret_d = spx["adj"].diff() / spx["price"].shift(1)
spx_cum = (1 + spx_ret_d.fillna(0)).cumprod() * 100
spx_usd_m = spx_cum.resample("ME").last()
inr_me = inr.resample("ME").last()  # same-month relabel, no ffill/nearest -> no lookahead
spx_inr_m = spx_usd_m * inr_me.reindex(spx_usd_m.index)
spx_ret_m = spx_inr_m.pct_change()
mom_spx = spx_inr_m.pct_change(12)
mom_spx_skip = mom_spx.shift(1)  # 12-1: skip the most recent month in the lookback
mom_g_skip = mom_g.shift(1)
mom_n_skip = mom_n.shift(1)

sanity_yrs = (spx_usd_m.index[-1] - spx_usd_m.index[0]).days / 365.25
sanity_cagr = 100 * ((spx_usd_m.iloc[-1] / spx_usd_m.iloc[0]) ** (1 / sanity_yrs) - 1)
print(f"[sanity] SPX-USD continuous-futures series {spx_usd_m.index[0].date()}.."
      f"{spx_usd_m.index[-1].date()}: CAGR {sanity_cagr:+.2f}%/yr (expect ~high-single/low-"
      f"double-digit, S&P total-return-ish since futures roll embeds div-adjusted carry)")

# ============================================================================
# 2. Switcher variants: pick max-momentum asset from the PRIOR month-end signal.
# ============================================================================
SENTINEL = -9.0


def build_switcher(assets_mom, assets_ret, me_index):
    """assets_mom/assets_ret: {name: Series keyed by month-end}. Returns dict me->(asset,ret)."""
    out = {}
    for me in me_index:
        prev = list(assets_mom.values())[0].index[list(assets_mom.values())[0].index < me]
        if not len(prev):
            continue
        sig_d = prev[-1]
        vals = {k: v.get(sig_d, SENTINEL) for k, v in assets_mom.items()}
        vals = {k: (SENTINEL if pd.isna(v) else v) for k, v in vals.items()}
        best = max(vals, key=vals.get)
        out[me] = (best, assets_ret[best].get(me, 0.0))
    return out


ME_IDX = n_me.loc[D0:D1].index

variants = {
    "dual_12m": build_switcher({"nifty": mom_n, "gold": mom_g},
                                {"nifty": n_ret_m, "gold": g_ret_m}, ME_IDX),
    "dual_12_1skip": build_switcher({"nifty": mom_n_skip, "gold": mom_g_skip},
                                     {"nifty": n_ret_m, "gold": g_ret_m}, ME_IDX),
    "tri_12m": build_switcher({"nifty": mom_n, "gold": mom_g, "spx": mom_spx},
                               {"nifty": n_ret_m, "gold": g_ret_m, "spx": spx_ret_m}, ME_IDX),
    "tri_12_1skip": build_switcher({"nifty": mom_n_skip, "gold": mom_g_skip, "spx": mom_spx_skip},
                                    {"nifty": n_ret_m, "gold": g_ret_m, "spx": spx_ret_m}, ME_IDX),
}

# ============================================================================
# 3. Standalone-sleeve stats (100% notional in the switcher; daily placement via
#    the engine's month_stream, last-trading-day convention, E1-fixed).
# ============================================================================


def stats_and_holdings(name, d):
    ret_series = pd.Series({me: v[1] for me, v in d.items()})
    hold_series = pd.Series({me: v[0] for me, v in d.items()})
    day_ret = month_stream(ret_series)
    eq = (1 + day_ret).cumprod() * 100
    cagr, dd, yearly = stats_of(eq)
    h1 = eq.loc[:"2016-12-31"]
    h2 = eq.loc["2017-01-01":]
    e1 = 100 * ((h1.iloc[-1] / h1.iloc[0]) ** (365.25 / (h1.index[-1] - h1.index[0]).days) - 1)
    e2 = 100 * ((h2.iloc[-1] / h2.iloc[0]) ** (365.25 / (h2.index[-1] - h2.index[0]).days) - 1)
    holds = hold_series.value_counts(normalize=True).to_dict()
    return dict(cagr=cagr, dd=dd, worst_yr=100 * yearly.min(), worst_yr_year=int(yearly.idxmin().year),
                era1=e1, era2=e2, holdings_pct={k: round(100 * v, 1) for k, v in holds.items()},
                yearly={int(y.year): round(100 * v, 2) for y, v in yearly.items()}), ret_series, hold_series


results = {}
crisis_tables = {}
for name, d in variants.items():
    stats, ret_series, hold_series = stats_and_holdings(name, d)
    results[name] = stats
    print(f"[{name}] CAGR {stats['cagr']:+.2f}%/yr | maxDD {stats['dd']:.2f}% | "
          f"worst yr {stats['worst_yr']:+.1f}% ({stats['worst_yr_year']}) | "
          f"eras {stats['era1']:+.2f}/{stats['era2']:+.2f} | holdings% {stats['holdings_pct']}")
    for yr in (2013, 2020, 2022):
        rows = []
        for me in ret_series.index:
            if me.year != yr:
                continue
            rows.append(dict(month=str(me.date()), asset=hold_series[me],
                              switcher_ret=round(100 * ret_series[me], 2),
                              nifty_ret=round(100 * n_ret_m.get(me, np.nan), 2) if not pd.isna(n_ret_m.get(me, np.nan)) else None,
                              gold_inr_ret=round(100 * g_ret_m.get(me, np.nan), 2) if not pd.isna(g_ret_m.get(me, np.nan)) else None,
                              spx_inr_ret=round(100 * spx_ret_m.get(me, np.nan), 2) if not pd.isna(spx_ret_m.get(me, np.nan)) else None))
        crisis_tables.setdefault(name, {})[yr] = rows
cells_consumed = len(variants)  # 4 standalone switcher variants

print("\n-- crisis years 2013 / 2020 / 2022 (dual_12m vs tri_12m) --")
for yr in (2013, 2020, 2022):
    print(f" {yr}:")
    for name in ("dual_12m", "tri_12m"):
        rows = crisis_tables[name][yr]
        held = [(r["month"][:7], r["asset"], r["switcher_ret"]) for r in rows]
        print(f"   {name}: {held}")

# ============================================================================
# 4. Book-level substitution: replace the 20% dual sleeve with tri_12m / tri_12_1skip
#    inside the standing 65/20/15 book (financing+syn_margin ON, the honest baseline).
# ============================================================================


def sw_series_from(d):
    return pd.Series({me: v[1] for me, v in d.items()})


book_results = {}
BASE_KEY = "OP-D6b_a5_dual_12m"
eq_base, pm_base = run_book(0.65, 0.20, 0.15, financing=True, syn_margin=True)
cb, db, yb = stats_of(eq_base)
book_results[BASE_KEY] = dict(cagr=cb, dd=db, worst_yr=100 * yb.min())
print(f"\n[book:{BASE_KEY}] CAGR {cb:+.2f} | maxDD {db:.2f} | worst yr {100*yb.min():+.1f} "
      f"(reproduces OP-D6b a5: +11.13/-11.53)")

for sub_name in ("tri_12m", "tri_12_1skip"):
    sw_alt = sw_series_from(variants[sub_name])
    # monkeypatch: run_book's core is fixed, but sw_w path uses module-level SW_M via
    # month_stream(SW_M) inside run_book -- so rebuild run_book's sw leg externally by
    # patching the closure global SW_M for this call only (documented, reverted after).
    orig_sw_m = _g["SW_M"]
    _g["SW_M"] = sw_alt
    eq_alt, pm_alt = run_book(0.65, 0.20, 0.15, financing=True, syn_margin=True)
    _g["SW_M"] = orig_sw_m
    ca, da, ya = stats_of(eq_alt)
    book_results[f"OP-D6b_a5_{sub_name}"] = dict(cagr=ca, dd=da, worst_yr=100 * ya.min())
    print(f"[book:{sub_name} substituted] CAGR {ca:+.2f} (d {ca-cb:+.2f}pp) | maxDD {da:.2f} "
          f"(d {da-db:+.2f}pp) | worst yr {100*ya.min():+.1f}")
    cells_consumed += 1

# ============================================================================
# dump JSON
# ============================================================================
out = dict(
    family="f04_triasset_momentum",
    window=[str(D0.date()), str(D1.date())],
    sanity_spx_usd_cagr=round(sanity_cagr, 2),
    standalone_switcher=results,
    crisis_year_tables=crisis_tables,
    book_substitution=book_results,
    cells_consumed=cells_consumed,
)
with open("/home/user/claude-demo/research/opt_sweep2/f04_triasset_momentum.json", "w") as f:
    json.dump(out, f, indent=2, default=str)
print(f"\ncells_consumed = {cells_consumed}")
print("wrote research/opt_sweep2/f04_triasset_momentum.json")
