"""Part-2 ablation for lens 5: one structural change at a time on top of the frozen vix_vrp rules (DEV only).
Generalised rule (all causal, decided at close t):
  state machine from signals/vix_vrp.py (imported, not edited) -> tier lev_calm / lev_elev / lev_panic
  VRP < vrp_min -> cash (as original)
  optional ELEVATED gate: lev_elev only when VRP > vrp_elev_min (else cash)
  optional PANIC burst: when VRP >= vrp_min AND vix <= (1-peak_frac) * trailing max(vix, peak_win) -> burst_lev
Prints one line per variant; writes dev_results/vix_vrp_v2_ablation.csv."""
import sys, importlib.util
from pathlib import Path
import numpy as np, pandas as pd

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import engine as E, features as F
import dev_harness as H

spec = importlib.util.spec_from_file_location("vix_vrp", HERE / "signals" / "vix_vrp.py")
base_mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(base_mod)

DEV_END = "2012-06-30"
df = E.load_market(end=DEV_END)
assert df.index[-1] <= pd.Timestamp(DEV_END)
COST, FIN = 3.0, 60.0


def signal_gen(df, v_calm=15.5, v_panic=30.0, hyst=0.12, rv_win=10, vrp_min=-0.15,
               lev_calm=2.0, lev_elev=0.0, lev_panic=1.0, burst_lev=0.0, peak_frac=0.25, peak_win=30,
               vrp_elev_min=None, elev_mode="raw", elev_band=0.03, elev_smooth=5, elev_hold=5):
    rv_win = max(int(round(rv_win)), 2)
    vix = df["vix_close"].ffill()
    reg = base_mod.vix_regime(vix, v_calm, v_panic, hyst).values
    rv = F.realized_vol(df["spx_ret"], rv_win)
    vrp = vix / 100.0 - rv
    lev = pd.Series(np.select([reg == 0, reg == 2], [lev_calm, lev_panic], default=lev_elev), index=df.index, dtype=float)
    if vrp_elev_min is not None:
        if elev_mode == "raw":
            ok = (vrp > vrp_elev_min)
        elif elev_mode == "smooth":
            ok = (vrp.rolling(elev_smooth, min_periods=elev_smooth).mean() > vrp_elev_min)
        elif elev_mode == "hyst":
            ok = F.hysteresis(vrp > vrp_elev_min, vrp < vrp_elev_min - elev_band, initial=False)
        elif elev_mode == "hold":
            ok = F.min_holding((vrp > vrp_elev_min), elev_hold) > 0.5
        lev[(reg == 1) & ~ok.fillna(False).values] = 0.0
    if burst_lev > 0:
        peak = vix.rolling(peak_win, min_periods=peak_win).max()
        burst = (reg == 2) & (vrp >= vrp_min) & (vix <= (1.0 - peak_frac) * peak)
        lev[burst] = burst_lev
    lev[vrp < vrp_min] = 0.0
    lev[vix.isna() | rv.isna()] = 0.0
    return lev


def evaluate(tag, **kw):
    lev = signal_gen(df, **kw).reindex(df.index)
    r = E.run(df, lev, cost_bps=COST, financing_spread_bps=FIN, start="1990-01-01", end=DEV_END)
    m = r.metrics()
    eras = H.run_eras(df, lev, COST, FIN)
    st = H.run_stress(df, lev, COST, FIN)
    cz = H.spurious_reentry_census(df, lev)
    row = {"variant": tag, **{k: v for k, v in kw.items()},
           "sharpe": m["sharpe"], "cagr": m["annualized_return_pct"], "maxdd": m["max_drawdown_pct"], "dailydd": m["max_drawdown_daily_pct"],
           "worstm": m["worst_month_pct"], "chg_yr": m["position_changes_per_year"], "cash": m["pct_days_cash"], "avgL": m["avg_leverage"],
           "up": m["up_capture_pct"], "dn": m["down_capture_pct"],
           "era90s_cagr": eras["1990-1999"]["cagr_pct"], "era00_cagr": eras["2000-2012H1"]["cagr_pct"],
           "era90s_dd": eras["1990-1999"]["max_dd_pct"], "era00_dd": eras["2000-2012H1"]["max_dd_pct"],
           "bear0002": st["2000_02_bear"]["model_total_pct"], "bear0002_dd": st["2000_02_bear"]["model_max_dd_pct"],
           "rec0203": st["2002_03_recovery"]["model_total_pct"],
           "gfc": st["2007_09_gfc"]["model_total_pct"], "gfc_dd": st["2007_09_gfc"]["model_max_dd_pct"],
           "rec09": st["2009_recovery"]["model_total_pct"], "ltcm98": st["1998_ltcm"]["model_total_pct"],
           "flash10": st["2010_flash"]["model_total_pct"], "debt11": st["2011_debt"]["model_total_pct"],
           "cz00_n": cz["2000_02_bear"]["n_entries_to_2x_plus"], "cz00_neg": cz["2000_02_bear"]["share_fwd10_negative"],
           "cz00_fwd": cz["2000_02_bear"]["mean_fwd10_excess_pct"],
           "cz08_n": cz["2007_09_gfc"]["n_entries_to_2x_plus"], "cz08_neg": cz["2007_09_gfc"]["share_fwd10_negative"],
           "cz08_fwd": cz["2007_09_gfc"]["mean_fwd10_excess_pct"]}
    f = lambda v, w=6, d=2: (f"{v:{w}.{d}f}" if isinstance(v, (int, float)) and v is not None else f"{str(v):>{w}s}")
    print(f"{tag:22s} Sh {f(row['sharpe'],5,3)} CAGR {f(row['cagr'],5,1)} DD {f(row['maxdd'],5,1)} dDD {f(row['dailydd'],5,1)} wM {f(row['worstm'],5,1)} "
          f"chg {f(row['chg_yr'],4,1)} cash {f(row['cash'],3,0)} L {f(row['avgL'],4,2)} up/dn {f(row['up'],3,0)}/{f(row['dn'],3,0)} | "
          f"90s {f(row['era90s_cagr'],5,1)} 00s {f(row['era00_cagr'],5,1)} | bear {f(row['bear0002'],6,1)} ({f(row['bear0002_dd'],5,1)}) "
          f"gfc {f(row['gfc'],6,1)} ({f(row['gfc_dd'],5,1)}) rec09 {f(row['rec09'],5,1)} rec03 {f(row['rec0203'],5,1)} 98 {f(row['ltcm98'],5,1)} 11 {f(row['debt11'],5,1)} | "
          f"census00 n{row['cz00_n']} neg {f(row['cz00_neg'],4,2)} fwd {f(row['cz00_fwd'],5,2)} census08 n{row['cz08_n']} neg {f(row['cz08_neg'],4,2)} fwd {f(row['cz08_fwd'],5,2)}", flush=True)
    return row


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    rows = []
    if which in ("all", "tiers"):
        rows.append(evaluate("V0_orig_2/0/1"))
        rows.append(evaluate("V1_calm3x", lev_calm=3.0))
        rows.append(evaluate("V2_elev1x", lev_elev=1.0))
        rows.append(evaluate("V3_calm3x_elev1x", lev_calm=3.0, lev_elev=1.0))
        rows.append(evaluate("V2b_elev1x_vrp>.03", lev_elev=1.0, vrp_elev_min=0.03))
        rows.append(evaluate("V2c_elev1x_vrp>.06", lev_elev=1.0, vrp_elev_min=0.06))
        rows.append(evaluate("V2d_elev1x_vrp>.09", lev_elev=1.0, vrp_elev_min=0.09))
        rows.append(evaluate("V1b_calm3x_panic0", lev_calm=3.0, lev_panic=0.0))
        rows.append(evaluate("V0b_panic0", lev_panic=0.0))
        rows.append(evaluate("V0c_panic2", lev_panic=2.0))
    if which in ("all", "burst"):
        for bl in (2.0, 3.0):
            for pf in (0.20, 0.25, 0.30, 0.35):
                rows.append(evaluate(f"V4_burst{bl:.0f}x_pf{pf:.2f}", burst_lev=bl, peak_frac=pf))
        rows.append(evaluate("V4b_burst2x_pf.25_w60", burst_lev=2.0, peak_frac=0.25, peak_win=60))
        rows.append(evaluate("V4c_burst2x_pf.25_w15", burst_lev=2.0, peak_frac=0.25, peak_win=15))
        rows.append(evaluate("V6_calm3x_burst2x", lev_calm=3.0, burst_lev=2.0, peak_frac=0.25))
    if which == "round2":
        for a in (0.07, 0.08, 0.10, 0.11, 0.12, 0.14, 0.16, 0.20):
            rows.append(evaluate(f"R2_raw_a{a:.2f}", lev_elev=1.0, vrp_elev_min=a))
        for a in (0.08, 0.10, 0.12):
            rows.append(evaluate(f"R2_hyst03_a{a:.2f}", lev_elev=1.0, vrp_elev_min=a, elev_mode="hyst", elev_band=0.03))
        rows.append(evaluate("R2_hyst05_a0.10", lev_elev=1.0, vrp_elev_min=0.10, elev_mode="hyst", elev_band=0.05))
        for a in (0.08, 0.10, 0.12):
            rows.append(evaluate(f"R2_smooth5_a{a:.2f}", lev_elev=1.0, vrp_elev_min=a, elev_mode="smooth", elev_smooth=5))
        rows.append(evaluate("R2_hold5_a0.10", lev_elev=1.0, vrp_elev_min=0.10, elev_mode="hold", elev_hold=5))
    pd.DataFrame(rows).to_csv(HERE / "dev_results" / f"vix_vrp_v2_ablation_{which}.csv", index=False, float_format="%.4f")
