"""OP-D7 — the optimized book under relaxed constraints. Registered 2026-09-08 BEFORE
this run. Base = OP-D6b a5 (E1+E2 in ALL cells). R1 synthetic-futures top-up (cap 2.0x,
financed at r=0.06, 10% margin on the levered fraction); R2 weekly condor POST-SPIKE
ONLY (VIX-pct>=0.80, 1.0-sigma shorts / 2.5-sigma wings, next-Thursday, no rolls,
day-stop -1%, 2.5% hedged margin); R3 MR axis DROPPED (MR-D1 m5 failed its frozen
inclusion rule). R4 weight grid x R1 x R2 = 24 train cells, purged train/test (OP-D3b
protocol), frozen selection + validation rules. Prints only.
"""
import pandas as pd

_src = open("/home/user/claude-demo/scripts/analyze_op_d6b.py").read()
_g = {}
exec(_src.split("# === MAIN ===")[0], _g)
run_book, stats_of = _g["run_book"], _g["stats_of"]
dates, DF2, pct_s = _g["dates"], _g["DF2"], _g["pct_s"]
fac_vm, D0, D1 = _g["fac_vm"], _g["D0"], _g["D1"]
np = _g["np"]
bs_ns = {}
exec(open("/home/user/claude-demo/scripts/analyze_op_d3.py").read().split("BASE = ")[0], bs_ns)
make_legs, price_legs = bs_ns["make_legs"], bs_ns["price_legs"]

TR0, TR1 = pd.Timestamp("2011-07-01"), pd.Timestamp("2016-12-31")
TE0 = pd.Timestamp("2017-02-01")  # 21td purge (OP-D3b verbatim)


def next_thursday(t):
    d = t + pd.Timedelta(days=(3 - t.weekday()) % 7 or 7)
    return d


# ---- R2 weekly post-spike condor sleeve: own book 100, book-relative (computed once) ----
def weekly_sleeve():
    book = 100.0
    pos = None
    rows, mrows = [], []
    for t in dates:
        S, vix = DF2.S[t], DF2.vix[t]
        p = pct_s.reindex([t]).ffill().iloc[0]
        day = 0.0
        if pos:
            v, _ = price_legs(pos["legs"], S, vix, pos["exp"], t)
            day = (v - pos["mark"]) * pos["units"]
            pos["mark"] = v
            if t >= pos["exp"] or day / book <= -0.01:
                pos = None
        book += day
        if pos is None and p >= 0.80:
            exp_d = next_thursday(t)
            if (exp_d - t).days < 3:
                exp_d = next_thursday(exp_d)
            legs, T = make_legs(S, vix, exp_d, t, 2.5)
            v0, _ = price_legs(legs, S, vix, exp_d, t)
            maxloss = (2.5 - 1) * (vix / 100 * np.sqrt(T)) * S - (-v0)
            if maxloss > 0:
                pos = dict(legs=legs, exp=exp_d, units=0.05 * book / maxloss, mark=v0,
                           notional=0.05 * book / maxloss * S)
        rows.append((t, book))
        mrows.append((t, 0.025 * pos["notional"] / book if pos else 0.0))
    eq = pd.Series(dict(rows))
    return eq.pct_change().fillna(0), pd.Series(dict(mrows))


WK_RET, WK_MARGIN = weekly_sleeve()
n_on = int((WK_MARGIN > 0).sum())
print(f"R2 weekly sleeve (post-spike only): position on {n_on} days ({100*n_on/len(dates):.0f}%); "
      f"standalone {100*((1+WK_RET).prod()**(365.25/(D1-D0).days)-1):+.2f}%/yr")
print("R3 MR axis: DROPPED (MR-D1 m5 failed the frozen inclusion rule)\n")

WEIGHTS = [(0.65, 0.20, 0.15), (0.55, 0.20, 0.25), (0.60, 0.15, 0.25),
           (0.70, 0.10, 0.20), (0.50, 0.25, 0.25), (0.60, 0.20, 0.20)]


def eval_cfg(w, r1, r2):
    eq, pm = run_book(*w, cap=2.0 if r1 else 1.5, financing=True, syn_margin=True,
                      extra_ret=WK_RET if r2 else None,
                      extra_margin=WK_MARGIN if r2 else None)
    return eq, pm


def win_stats(eq, a, b):
    e = eq.loc[a:b]
    yrs = (e.index[-1] - e.index[0]).days / 365.25
    cagr = 100 * ((e.iloc[-1] / e.iloc[0]) ** (1 / yrs) - 1)
    dd = 100 * (e / e.cummax() - 1).min()
    wy = e.resample("YE").last().pct_change().dropna().min()
    return cagr, dd, 100 * wy


print("OP-D7 grid — TRAIN 2011-07..2016-12 (selection: max CAGR s.t. DD>=-15, worst-yr>=-10):")
results = {}
best_key, best_cagr, best_dd = None, -1e9, 0
for w in WEIGHTS:
    for r1 in (False, True):
        for r2 in (False, True):
            eq, pm = eval_cfg(w, r1, r2)
            results[(w, r1, r2)] = (eq, pm)
            c, d, wy = win_stats(eq, TR0, TR1)
            ok = d >= -15 and wy >= -10
            tag = f"w{int(100*w[0])}/{int(100*w[1])}/{int(100*w[2])} syn={'Y' if r1 else 'n'} wk={'Y' if r2 else 'n'}"
            print(f"  {tag}: train CAGR {c:+6.2f} DD {d:6.2f} worst-yr {wy:+5.1f}"
                  f"{' *' if ok else ' (constraint fail)'}")
            if ok and (c > best_cagr or (c == best_cagr and d > best_dd)):
                best_key, best_cagr, best_dd = (w, r1, r2), c, d

w, r1, r2 = best_key
print(f"\nSELECTED on train: {int(100*w[0])}/{int(100*w[1])}/{int(100*w[2])}, "
      f"synthetic top-up {'ON' if r1 else 'off'}, weekly sleeve {'ON' if r2 else 'off'}")

# frozen validation vs the corrected-D6 baseline config on TEST
eq_sel = results[best_key][0]
eq_bas = results[((0.65, 0.20, 0.15), False, False)][0]
cs, ds, _ = win_stats(eq_sel, TE0, D1)
cb, db, _ = win_stats(eq_bas, TE0, D1)
accept = (cs > cb) and (ds >= max(db, -15))
print(f"TEST validation: selected {cs:+.2f}/DD {ds:.2f} vs baseline {cb:+.2f}/DD {db:.2f} -> "
      f"{'ACCEPTED' if accept else 'REJECTED — THE BASELINE STANDS'}")
final_key = best_key if accept else ((0.65, 0.20, 0.15), False, False)
w, r1, r2 = final_key
eq, pm = results[final_key]

# ---- final reads, full period ----
cagr, dd, yearly = stats_of(eq)
h1, h2 = eq.loc[:"2016-12-31"], eq.loc["2017-01-01":]
e1 = 100 * ((h1.iloc[-1] / h1.iloc[0]) ** (365.25 / (h1.index[-1] - h1.index[0]).days) - 1)
e2 = 100 * ((h2.iloc[-1] / h2.iloc[0]) ** (365.25 / (h2.index[-1] - h2.index[0]).days) - 1)
print(f"\nOP-D7 FINAL — {int(100*w[0])}/{int(100*w[1])}/{int(100*w[2])} "
      f"syn={'ON' if r1 else 'off'} wk={'ON' if r2 else 'off'}, full period:")
print(f"  s1 CAGR {cagr:+.2f}%/yr (TR ~{cagr+1.3:+.2f}%) vs >=15%: "
      f"{'PASS' if cagr >= 15 else ('PASS on TR' if cagr + 1.3 >= 15 else 'MISS')}")
print(f"  s2 maxDD {dd:.2f}% vs <=15%: {'PASS' if dd >= -15 else 'MISS'}")
print(f"  s3 peak margin+premium {100*pm:.1f}% of book vs <30%: {'PASS' if pm < 0.30 else 'MISS'}")
mu = fac_vm.loc[D0:D1].mean()
eq_h, _ = run_book(*w, cap=2.0 if r1 else 1.5, financing=True, syn_margin=True,
                   fac_monthly=fac_vm - 0.30 * mu,
                   extra_ret=WK_RET if r2 else None, extra_margin=WK_MARGIN if r2 else None)
ch, dh, yh = stats_of(eq_h)
print(f"  s4 HAIRCUT (factor means -30%): CAGR {ch:+.2f} (TR ~{ch+1.3:+.2f}) "
      f"{'PASS' if ch >= 15 else ('PASS on TR' if ch + 1.3 >= 15 else 'MISS')} | "
      f"maxDD {dh:.2f} {'PASS' if dh >= -15 else 'MISS'} | worst yr {100*yh.min():+.1f}")
print(f"  s5 era halves: {e1:+.2f} / {e2:+.2f} %/yr")
wy = yearly.min()
print(f"  s6 worst year {100*wy:+.1f}% ({yearly.idxmin().year}) vs >=-10%: "
      f"{'PASS' if wy >= -0.10 else 'MISS'}")
print(f"  s7 vs OP-D6b a5 (+11.13/-11.53): dCAGR {cagr-11.13:+.2f}pp, dDD {dd-(-11.53):+.2f}pp "
      f"-> {'DOMINATES' if cagr > 11.13 and dd > -11.53 else 'no strict dominance'}")
print("  s8 yearly:", {d.year: f"{100*x:+.1f}%" for d, x in yearly.items()})
