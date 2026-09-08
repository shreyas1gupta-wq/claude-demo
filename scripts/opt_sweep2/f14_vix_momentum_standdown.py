"""opt_sweep2 / f14_vix_momentum_standdown — VIX-MOMENTUM STAND-DOWN REFINEMENT.

Family brief: the OP-D3/OP-D2 condor stand-down triggers at expanding-percentile(VIX
level) >= 0.90 -- a LEVEL-based flag that the booked EWMA/GARCH work (OP-D2 F04) already
showed lags real crash onsets by 72-74 vol pts. Test three faster, no-lookahead
alternatives, each substituted as the ONLY change to the OP-D3 engine (everything else --
entry gate pct>=0.60, re-entry gate pct<0.60, delta-band roll 0.30 max 3, day-stop -2.22%,
wing 2.5, sizing f=min(0.150*s_t,0.10), budget-window exclusion -- held at OP-D3 BASE,
verbatim):

  (a) MOM   5d dVIX > expanding-90th-pct of 5d dVIX   (same house 90th-pct convention as
      the production rule -- quant.ladder.credit_cycle.expanding_percentile -- applied to
      the vol-of-vol CHANGE instead of the level; min_obs=252, no invented threshold)
  (b) MA25  VIX > 1.25x its own trailing 21d mean      (fast break-from-mean-reversion
      trigger; 1.25x and 21d are the exact parameters named in the family brief)
  (c) JUMP  2-day VIX rise > 20%                        (fastest, pure jump trigger; 20%
      and 2d are the exact parameters named in the family brief)

All three signals are computed VECTORIZED over the full history using only trailing/
expanding windows (value at t uses data through t only) -- no groupby, no .first(),
no full-sample stat (the F13 lookahead-leak pattern this program is explicitly warned
against). Verified by construction below (each is a rolling/expanding/shift transform).

Engine reused verbatim from scripts/analyze_op_d3.py via exec-before-BASE (house pattern,
see scripts/analyze_op_d6b.py). Only the closing condition inside run() is parameterized
(pct>=0.90 -> a supplied boolean Series 'standdown'); nothing else in the loop changes.

Periods (matching OP-D3b/c's own registered split, for direct comparability with the
booked numbers): FULL 2011-07-01..2023-03-31; TRAIN 2011-07-01..2016-12-31; TEST
2017-02-01..2023-03-31 (21td purge gap after TRAIN, as OP-D3 itself uses).

Run: PYTHONPATH=/home/user/claude-demo python3 scripts/opt_sweep2/f14_vix_momentum_standdown.py
"""
import json
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")
from quant.ladder.credit_cycle import expanding_percentile  # noqa: E402

# ---- reuse the OP-D3 engine verbatim (df, bs, make_legs, price_legs, last_thursday,
# BUDGETS, no_entry, R) by exec-ing everything before its BASE=/print MAIN section ----
_SRC = open("/home/user/claude-demo/scripts/analyze_op_d3.py").read()
_NS = {}
exec(_SRC.split("BASE = ")[0], _NS)
df = _NS["df"]
make_legs, price_legs, last_thursday = _NS["make_legs"], _NS["price_legs"], _NS["last_thursday"]
no_entry = _NS["no_entry"]

BASE = (0.60, 2.5, 0.30)  # entry_th, wing, roll_th -- OP-D2/OP-D3 standing choice, UNCHANGED
D0, D1 = pd.Timestamp("2011-07-01"), pd.Timestamp("2023-03-31")
TR0, TR1 = pd.Timestamp("2011-07-01"), pd.Timestamp("2016-12-31")
TE0, TE1 = pd.Timestamp("2017-02-01"), pd.Timestamp("2023-03-31")  # 21td purge, OP-D3b/c convention

cells_consumed = 0


def run2(entry_th, wing, roll_th, standdown, d0, d1, book0=100.0):
    """OP-D3's run(), verbatim, with the pct>=0.90 close condition replaced by
    `standdown` (a boolean Series aligned to df.index, no-lookahead by construction)."""
    book = book0
    eq = []
    pos = None
    rearm = True
    idx = df.loc[d0:d1]
    n_standdown_days = 0
    for t, row in idx.iterrows():
        S, vix, pct = row.S, row.vix, row.pct
        sd_flag = bool(standdown.get(t, False))
        day_pnl = 0.0
        if pos:
            v, dlt = price_legs(pos["legs"], S, vix, pos["exp"], t)
            day_pnl = (v - pos["mark"]) * pos["units"]
            pos["mark"] = v
            closed = False
            if t >= pos["exp"]:
                closed = True
            elif sd_flag:
                closed = True; rearm = False
            elif day_pnl / book <= -0.0222:
                closed = True; rearm = False
            elif abs(dlt) >= roll_th:
                if pos["rolls"] >= 3:
                    closed = True
                else:
                    legs, _ = make_legs(S, vix, pos["exp"], t, wing)
                    nv, _ = price_legs(legs, S, vix, pos["exp"], t)
                    pos.update(legs=legs, mark=nv, rolls=pos["rolls"] + 1)
            if closed:
                pos = None
        book += day_pnl
        if not rearm and pct < 0.60:
            rearm = True
        if sd_flag:
            n_standdown_days += 1
        if pos is None and rearm and pct >= entry_th and t not in no_entry:
            em, ey = (t.month + 1, t.year) if t.month < 12 else (1, t.year + 1)
            exp_d = last_thursday(ey, em)
            if (exp_d - t).days < 15:
                em, ey = (em + 1, ey) if em < 12 else (1, ey + 1)
                exp_d = last_thursday(ey, em)
            legs, T = make_legs(S, vix, exp_d, t, wing)
            v0, _ = price_legs(legs, S, vix, exp_d, t)
            credit = -v0
            maxloss = (wing - 1) * (vix / 100 * np.sqrt(T)) * S - credit
            if maxloss > 0:
                s_t = min(0.15 / max(row.ewvol, 1e-6), 2.0)
                f = min(0.150 * s_t, 0.10)
                units = f * book / maxloss
                pos = dict(legs=legs, exp=exp_d, units=units, mark=v0, rolls=0)
        eq.append((t, book))
    e = pd.Series(dict(eq))
    mo = e.resample("ME").last().pct_change().dropna()
    yrs = (d1 - d0).days / 365.25
    geo = (e.iloc[-1] / e.iloc[0]) ** (1 / yrs) - 1
    dd = (e / e.cummax() - 1).min()
    return dict(geo=100 * geo, maxdd=100 * dd, worst_mo=100 * mo.min(),
                pos_mo=100 * (mo > 0).mean(), mean_mo=100 * mo.mean(),
                n_standdown_days=n_standdown_days, n_months=len(mo), eq=e)


# ---- baseline stand-down (production rule): pct >= 0.90, level-based ----
sd_base = (df["pct"] >= 0.90)

# ---- (a) MOM: 5d change in VIX level, expanding 90th-pct of that CHANGE series ----
# no-lookahead: dvix5[t] = vix[t] - vix[t-5] (both known at t); pct_dvix[t] uses only
# dvix5[:t+1] (expanding_percentile is causal by construction, quant.ladder.credit_cycle)
dvix5 = df["vix"].diff(5)
pct_dvix5 = pd.Series(expanding_percentile(dvix5.to_numpy(), min_obs=252), index=df.index)
sd_mom = (pct_dvix5 >= 0.90).fillna(False)

# ---- (b) MA25: VIX > 1.25x trailing 21d mean (window ends at t, includes t -- no future data) ----
vix_ma21 = df["vix"].rolling(21, min_periods=21).mean()
sd_ma = (df["vix"] > 1.25 * vix_ma21).fillna(False)

# ---- (c) JUMP: 2-trading-day VIX rise > 20% (uses vix[t] and vix[t-2] only) ----
vix_lag2 = df["vix"].shift(2)
sd_jump = (df["vix"] / vix_lag2 - 1 > 0.20).fillna(False)

SIGNALS = {
    "base_pct90": sd_base,
    "a_mom_dvix90": sd_mom,
    "b_ma25_1p25x": sd_ma,
    "c_jump2d20pct": sd_jump,
}
PERIODS = {"full": (D0, D1), "train": (TR0, TR1), "test": (TE0, TE1)}

results = {}
for sig_name, sig in SIGNALS.items():
    results[sig_name] = {}
    for per_name, (d0, d1) in PERIODS.items():
        r = run2(*BASE, sig, d0, d1)
        cells_consumed += 1
        results[sig_name][per_name] = {
            "geo": round(r["geo"], 3), "maxdd": round(r["maxdd"], 3),
            "worst_mo": round(r["worst_mo"], 3), "pos_mo_pct": round(r["pos_mo"], 1),
            "mean_mo": round(r["mean_mo"], 4), "n_months": r["n_months"],
            "n_standdown_days": r["n_standdown_days"],
        }

# ---- flag-frequency diagnostics (descriptive, no extra cells: reuses the boolean series
# already computed above over the FULL sample) ----
full_idx = df.loc[D0:D1].index
freq = {name: {
    "days_flagged": int(sig.reindex(full_idx).fillna(False).sum()),
    "pct_days_flagged": round(100 * sig.reindex(full_idx).fillna(False).mean(), 2),
} for name, sig in SIGNALS.items()}

print(f"OP-D3 stand-down substitution sweep, {D0.date()}..{D1.date()} "
      f"(TRAIN {TR0.date()}..{TR1.date()} / TEST {TE0.date()}..{TE1.date()}):")
for sig_name in SIGNALS:
    print(f"\n  [{sig_name}] flagged {freq[sig_name]['days_flagged']}d "
          f"({freq[sig_name]['pct_days_flagged']}% of days)")
    for per_name in PERIODS:
        r = results[sig_name][per_name]
        print(f"    {per_name:5s}: geo {r['geo']:+7.2f}%/yr | maxDD {r['maxdd']:7.2f}% | "
              f"worst-mo {r['worst_mo']:+6.2f}% | mean-mo {r['mean_mo']:+.3f}% | "
              f"months+ {r['pos_mo_pct']:.0f}% | standdown-days {r['n_standdown_days']}")

# ---- deltas vs the base rule (the actual "trade" the family brief asks to quantify) ----
deltas = {}
for sig_name in ("a_mom_dvix90", "b_ma25_1p25x", "c_jump2d20pct"):
    deltas[sig_name] = {}
    for per_name in PERIODS:
        b = results["base_pct90"][per_name]
        r = results[sig_name][per_name]
        deltas[sig_name][per_name] = {
            "d_geo_pp": round(r["geo"] - b["geo"], 3),
            "d_maxdd_pp": round(r["maxdd"] - b["maxdd"], 3),
            "d_worst_mo_pp": round(r["worst_mo"] - b["worst_mo"], 3),
            "d_mean_mo_pp": round(r["mean_mo"] - b["mean_mo"], 4),
        }

print("\n  --- deltas vs base_pct90 (positive d_maxdd_pp / d_worst_mo_pp = LESS bad tail) ---")
for sig_name, per_map in deltas.items():
    for per_name, d in per_map.items():
        print(f"    {sig_name:14s} {per_name:5s}: d_geo {d['d_geo_pp']:+.2f}pp | "
              f"d_maxDD {d['d_maxdd_pp']:+.2f}pp | d_worst_mo {d['d_worst_mo_pp']:+.2f}pp | "
              f"d_mean_mo {d['d_mean_mo_pp']:+.3f}pp")

print(f"\ncells_consumed = {cells_consumed}")

out = {
    "id": "f14_vix_momentum_standdown",
    "family": "VIX-MOMENTUM STAND-DOWN REFINEMENT (opt_sweep2)",
    "engine": "scripts/analyze_op_d3.py run(), verbatim except the stand-down close condition",
    "base_rule": "expanding-percentile(VIX level) >= 0.90, min_obs=252 (production/OP-D2 C06)",
    "periods": {k: [str(v[0].date()), str(v[1].date())] for k, v in PERIODS.items()},
    "signals": {
        "a_mom_dvix90": "5d VIX change (vix[t]-vix[t-5]) >= its own expanding 90th pct, min_obs=252",
        "b_ma25_1p25x": "vix[t] > 1.25 * trailing-21d mean of vix (window ends at t)",
        "c_jump2d20pct": "vix[t]/vix[t-2] - 1 > 0.20",
    },
    "results": results,
    "flag_frequency_full_sample": freq,
    "deltas_vs_base": deltas,
    "cells_consumed": cells_consumed,
}
with open("/home/user/claude-demo/research/opt_sweep2/f14_vix_momentum_standdown.json", "w") as fh:
    json.dump(out, fh, indent=2, default=str)
print("\nwrote research/opt_sweep2/f14_vix_momentum_standdown.json")
