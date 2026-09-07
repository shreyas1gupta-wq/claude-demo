#!/usr/bin/env python3
"""OP-D2 combiner c04 — capital split weekly (F17) vs monthly (F16), per-unit-margin.

Reconciles two different "monthly" comparators found in the record:
  (a) F16-registered, exact machinery (imported verbatim, as F18 does): 21-trading-day
      non-overlapping blocks, entry VIXpct>=0.6 ONLY.
  (b) f17.py's own internal cell-3 "monthly" comparator: CALENDAR months, entry
      VIXpct>=0.6 OR storm5 (f17's own entry_ok) -- a broader gate, different cycle
      boundary. f17's headline "+13.96%/yr geo" / "worst -75.64%" monthly numbers come
      from (b), NOT from the F16-registered design.
Uses (a) -- the actual F16-registered per-margin distribution (bit-identical to F18's
F16-mo-hold cell) -- as "monthly" for the capital-split math, since that is what F16 was
pre-registered and CONFIRMED on. (b) is printed for the record as a disclosed discrepancy.

No new bars: this is a sizing/combiner calc on already-printed F16/F17/F18 numbers, no
distribution is refit here beyond exactly reusing f16.py/f17.py machinery (per process
note #6 / #5 -- same reuse pattern F18 already used).
Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep/c04.py
"""
import sys

sys.path.insert(0, "/home/user/claude-demo/scripts/opt_sweep")
import numpy as np
import pandas as pd
import f16 as F16
import f17 as F17

from quant.ladder.credit_cycle import expanding_percentile


def f16_margin_returns():
    """f18.py's f16_margin_returns(), verbatim (same reuse of F16's own machinery:
    make_strikes/condor_mark/REPO/MIN_OBS/TENOR/ENTRY_PCT/STOP_MULT), + t0 dates kept."""
    px = pd.read_csv(f"{F16.REPO}/ingest/vault/index/nifty50_daily_2007_2026.csv",
                     parse_dates=["Date"]).set_index("Date")["Adj Close"]
    vx = pd.read_csv(f"{F16.REPO}/ingest/vault/vix/india_vix_daily_2010_2023.csv",
                     parse_dates=["date"]).set_index("date")["close"]
    df = pd.concat({"S": px, "vix": vx}, axis=1, join="inner").dropna().sort_index()
    df["pct"] = expanding_percentile(df["vix"].values, min_obs=F16.MIN_OBS)
    S, V, P = df["S"].values, df["vix"].values / 100.0, df["pct"].values
    span = (df.index[-1] - df.index[F16.MIN_OBS - 1]).days / 365.25
    rh = []
    for t0 in range(F16.MIN_OBS - 1, len(df) - F16.TENOR, F16.TENOR):
        if np.isnan(P[t0]) or P[t0] < F16.ENTRY_PCT:
            continue
        S0, sig0 = S[t0], V[t0]
        T0 = F16.TENOR / 252.0
        K0 = F16.make_strikes(S0, sig0, T0)
        C0, _, _ = F16.condor_mark(S0, K0, T0, sig0)
        margin = max(K0["kc2"] - K0["kc1"], K0["kp1"] - K0["kp2"]) - C0
        cost = None
        for j in range(1, F16.TENOR + 1):
            Trem = (F16.TENOR - j) / 252.0
            cost, _, _ = F16.condor_mark(S[t0 + j], K0, Trem, V[t0 + j])
        hold_pnl = C0 - cost
        rh.append((df.index[t0], hold_pnl / margin))
    return rh, span


def main():
    rh_mo, span = f16_margin_returns()
    r_mo = np.array([r for _, r in rh_mo])
    dates_mo = [d for d, _ in rh_mo]
    print(f"[F16-registered monthly, per-margin] n={len(r_mo)}, span={span:.2f}y, "
          f"mean {100*r_mo.mean():+.2f}%/cycle, worst {100*r_mo.min():+.2f}% "
          f"({dates_mo[int(r_mo.argmin())].date()})")

    df17 = F17.load()
    valid17 = df17[df17["vixpct"].notna()]
    span17 = (valid17.index[-1] - valid17.index[0]).days / 365.25
    iso = valid17.index.isocalendar()
    wk_groups = sorted([g.index for _, g in
                        valid17.groupby([iso.year.values, iso.week.values])],
                       key=lambda d: d[0])
    wk = F17.sim_cycles(df17, wk_groups)
    r_wk = np.array([t["rh"] for t in wk])
    dates_wk = [t["t0"] for t in wk]
    print(f"[F17-registered weekly, per-margin]  n={len(r_wk)}, span={span17:.2f}y, "
          f"mean {100*r_wk.mean():+.2f}%/cycle, worst {100*r_wk.min():+.2f}% "
          f"({dates_wk[int(r_wk.argmin())].date()})")

    # f17.py's OWN internal "monthly" comparator, for the record (disclosed discrepancy)
    mo_groups = sorted([g.index for _, g in valid17.groupby(valid17.index.to_period("M"))],
                       key=lambda d: d[0])
    mo17 = F17.sim_cycles(df17, mo_groups)
    r_mo17 = np.array([t["rh"] for t in mo17])
    print(f"[f17.py's OWN 'monthly' comparator]   n={len(r_mo17)} of {len(mo_groups)} "
          f"calendar months (entry = VIXpct>=0.6 OR storm5 -- NOT F16's registered gate), "
          f"mean {100*r_mo17.mean():+.2f}%/cycle, worst {100*r_mo17.min():+.2f}%")
    print("  ^ discrepancy vs F16-registered: different cycle boundary (calendar month vs "
          "21-td block) AND broader entry gate (adds storm5) -> f17's own quoted "
          "'+13.96%/yr geo' / '-75.64% worst' monthly print is NOT the F16-registered "
          "design; it is an unregistered f17-internal analog.")

    # --- capital split, two independent methods on the F16-registered / F17-registered pair
    f_mo, f_wk = 0.165, 0.035  # F18 DD-constrained f (P(book DD>10%)<=1%/yr), same constraint basis
    split_kelly_mo = f_mo / (f_mo + f_wk)
    print(f"\n[split, method 1: F18 DD-constrained-f ratio] f_mo={f_mo} : f_wk={f_wk} "
          f"-> monthly {100*split_kelly_mo:.1f}% / weekly {100*(1-split_kelly_mo):.1f}%")

    worst_mo, worst_wk = abs(r_mo.min()), abs(r_wk.min())
    split_worst_mo = worst_wk / (worst_mo + worst_wk)
    print(f"[split, method 2: worst-cycle loss-parity] |worst_mo|={100*worst_mo:.1f}% : "
          f"|worst_wk|={100*worst_wk:.1f}% -> monthly {100*split_worst_mo:.1f}% / "
          f"weekly {100*(1-split_worst_mo):.1f}%")

    # correlated-tail check: are the two sleeves' worst PER-MARGIN cycles the same episode?
    worst_mo_date = dates_mo[int(r_mo.argmin())]
    order_wk = np.argsort(r_wk)
    worst3_wk = [(dates_wk[i].date(), f"{100*r_wk[i]:+.1f}%") for i in order_wk[:3]]
    nearest_wk = min(dates_wk[i] for i in order_wk[:3])
    gap_days = abs((worst_mo_date - nearest_wk).days)
    print(f"\n[correlated-tail check] F16-registered worst cycle entry: {worst_mo_date.date()} "
          f"({100*r_mo.min():+.1f}%, per margin -- NOT the COVID month; F16's COVID entry is "
          f"only its worst in %-of-SPOT terms per f16.json, not %-of-MARGIN, since COVID's "
          f"wide entry-VIX strikes also inflated the margin base). F17-registered worst 3 "
          f"weeks: {worst3_wk}.")
    print(f"  gap to nearest F17 worst week: {gap_days} days -> on the per-margin metric that "
          f"actually sizes capital, the two sleeves' realized worst cycles do NOT coincide "
          f"(F16's is Dec-2021, F17's cluster is Feb-2016/Feb-2020) -- no historical evidence "
          f"of simultaneous tail-blowup; still no formal joint-DD estimate exists (F18 only "
          f"sizes each sleeve independently), so this is a supportive data point, not proof of "
          f"independence.")


if __name__ == "__main__":
    main()
