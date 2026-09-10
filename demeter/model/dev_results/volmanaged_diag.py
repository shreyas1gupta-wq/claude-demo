"""Diagnostic for ONE volmanaged variant (DEV ONLY): drawdown episodes, worst months with average leverage,
stress-episode totals, and day-by-day leverage ladders for the leverage-effect discussion (1987, Sep/Oct-2008,
May-2010, Aug-2011, Mar-2009 re-entry). Logs the variant to the scratch log (counts as one evaluation).
Usage: python dev_results/volmanaged_diag.py '{"target_vol":0.15,"hl":10,"band":0.5,"shock_z":0,"shock_days":0,"power":2}' [--tag x]
"""
from __future__ import annotations
import json, sys, time
from pathlib import Path
import numpy as np, pandas as pd
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
import engine as E
import importlib.util
spec = importlib.util.spec_from_file_location("volmanaged", HERE / "signals" / "volmanaged.py")
VM = importlib.util.module_from_spec(spec); spec.loader.exec_module(VM)
sys.path.insert(0, str(HERE / "dev_results"))
from volmanaged_scratch_eval import evaluate, LOG, DEV_END  # noqa: E402

STRESS = {"1987_crash": ("1987-08-25", "1987-12-31"), "1990_kuwait": ("1990-07-16", "1990-12-31"),
          "1998_ltcm": ("1998-07-17", "1998-12-31"), "2000_02_bear": ("2000-03-24", "2002-10-09"),
          "2002_03_recovery": ("2002-10-10", "2003-12-31"), "2007_09_gfc": ("2007-10-09", "2009-03-09"),
          "2009_recovery": ("2009-03-10", "2009-12-31"), "2010_flash": ("2010-04-23", "2010-07-30"),
          "2011_debt": ("2011-07-22", "2011-12-30")}
LADDERS = {"1987": ("1987-10-01", "1987-10-30"), "2008a": ("2008-09-02", "2008-10-15"),
           "2010": ("2010-04-26", "2010-05-14"), "2011": ("2011-07-25", "2011-08-12"), "2009re": ("2009-03-02", "2009-04-15")}


def dd_episodes(ret: pd.Series, n=5):
    eq = (1 + ret).cumprod(); peak = eq.cummax(); dd = eq / peak - 1
    out, used = [], pd.Series(False, index=dd.index)
    for _ in range(n):
        d = dd.where(~used)
        if d.isna().all() or d.min() >= -0.02:
            break
        t = d.idxmin(); p = eq.loc[:t].idxmax()
        rec = eq.loc[t:]; r = rec[rec >= peak.loc[t]].index
        e = r[0] if len(r) else eq.index[-1]
        out.append((str(p.date()), str(t.date()), str(e.date()), float(d.min() * 100)))
        used.loc[p:e] = True
    return out


def main():
    v = json.loads(sys.argv[1]); tag = sys.argv[sys.argv.index("--tag") + 1] if "--tag" in sys.argv else "diag"
    df = E.load_market(end=DEV_END)
    row = evaluate(df, v); row["tag"] = tag; row["ts"] = time.strftime("%Y-%m-%d %H:%M:%S")
    pd.DataFrame([row]).to_csv(LOG, mode="a", header=not LOG.exists(), index=False, float_format="%.4f")
    print("variant", json.dumps(v))
    print(f"d90 sh {row['d90_sh']:.3f} dd {row['d90_dd']:.1f} chg {row['d90_chg']:.1f} | d50 sh {row['d50_sh']:.3f} dd {row['d50_dd']:.1f} | gross d90 {row['d90_g_sh']:.3f}")
    band_up = v.get("band_up", v.get("band", 0.5)); band_dn = v.get("band_dn", band_up * float(v.get("bdr", 1.0)))
    lev = VM._core(df, v["target_vol"], v["hl"], v.get("long_mult", 4.0), band_up, band_dn,
                   power=int(v.get("power", 2)), discrete=bool(v.get("discrete", 0)), weekly=bool(v.get("weekly", 0)),
                   est=v.get("est", "max2"), shock_z=float(v.get("shock_z", 0)), shock_days=int(v.get("shock_days", 0)))
    sig = VM._sigma(df["spx_ret"].astype(float), float(v["hl"]), v.get("est", "max2"), float(v.get("long_mult", 4.0)))
    for w, (s, e) in {"dev_1990": ("1990-01-01", DEV_END), "dev_1950": ("1950-01-03", DEV_END),
                      "era_1950_69": ("1950-01-03", "1969-12-31"), "era_1970_89": ("1970-01-01", "1989-12-31")}.items():
        r = E.run(df, lev, cost_bps=3, financing_spread_bps=60, start=s, end=e)
        print(f"-- {w} drawdown episodes (peak, trough, recovery, depth%):")
        for ep in dd_episodes(r.daily["ret"]):
            print("   ", ep)
        if w == "dev_1990":
            m = E.to_monthly(r.daily["ret"]); mk = E.to_monthly(r.daily["mkt_tr_ret"]); ml = r.daily["lev"].resample("ME").mean()
            worst = pd.DataFrame({"model%": m * 100, "spy%": mk * 100, "avgL": ml}).nsmallest(10, "model%").round(2)
            print("-- worst 10 months (dev_1990):"); print(worst.to_string())
            print("-- stress episodes:")
            for k, (s2, e2) in STRESS.items():
                d = E.run(df, lev, cost_bps=3, financing_spread_bps=60, start=s2, end=e2).daily
                if len(d) < 10: continue
                eq = (1 + d["ret"]).cumprod(); eqm = (1 + d["mkt_tr_ret"]).cumprod()
                print(f"   {k}: model {(eq.iloc[-1]-1)*100:+.1f}% (SPY {(eqm.iloc[-1]-1)*100:+.1f}%) DD {E.drawdown(eq).min()*100:.1f}% avgL {d['lev'].mean():.2f} cash {(d['lev']==0).mean()*100:.0f}%")
    for k, (s, e) in LADDERS.items():
        sub = pd.DataFrame({"ret%": (df["spx_ret"] * 100).round(2), "sig%": (sig * 100).round(1),
                            "tgt": ((v["target_vol"] / sig) ** int(v.get("power", 2))).clip(0, 3).round(2),
                            "held(L_t)": lev.round(2), "in_effect": lev.shift(1).round(2)}).loc[s:e]
        sub["day_pnl%"] = (sub["in_effect"] * (df["spx_tr_ret"] - df["rf_daily"]).loc[s:e] * 100).round(2)
        print(f"-- ladder {k}:"); print(sub.to_string())


if __name__ == "__main__":
    main()
