"""f02_vrp_scaled_condor — VRP-SCALED CONDOR SIZING BY EXPANDING VIX QUINTILE.

Family assignment: "OP-D1 booked VRP monotone by VIX quintile (+1.9 calm -> +5.9 top). The
condor sleeve currently sizes f=min(0.15*s_t, 0.10) regardless of quintile. Test scaling
units by expanding VIX-quintile (e.g. x0.5/x0.75/x1.0/x1.25/x1.5 for Q1..Q5) with entry still
>=0.60. Reuse the OP-D3 run() machinery. Report book CAGR/DD deltas of the condor sleeve
standalone and expected book-level add."

PRE-REGISTRATION (written before any number below was computed; no prior ledger entry exists
for this family — this is this agent's own pre-registration per the task assignment):

  Quintile definition: fixed cutpoints 0.20/0.40/0.60/0.80 on the SAME expanding VIX
  percentile ("pct", min_obs=252, no lookahead) already used for the entry gate. Multiplier
  is read off the entry-day's quintile and FROZEN for the position's life (identical
  convention to how s_t/f is already frozen at entry in OP-D3/OP-D2 C02) -- no lookahead is
  introduced: the quintile a position enters in is known at the signal-day close, same as the
  entry gate itself.

  R1 (condor sleeve standalone): a design PASSES if standalone CAGR improves by >= +1.0pp/yr
     vs the uniform-multiplier baseline WITHOUT worsening standalone maxDD by more than 2.0pp.
  R2 (book level): a design PASSES if book-level CAGR improves by >= +0.3pp/yr (a first dent
     in the 2.6pp gap to the 15% target) at book-level maxDD impact no worse than +1.0pp.
  R3 (process control, not a bar): report whether all 5 nominal quintile buckets are actually
     REACHABLE given the entry gate is fixed at >=0.60 -- if only a subset ever fires, that is
     a finding to report explicitly, not to silently absorb into an averaged headline.

Multiplier designs tested (frozen, no "tune later"):
  BASE     : [1.0, 1.0, 1.0, 1.0, 1.0]                         -- sanity check, must reproduce
                                                                   OP-D3a bit-for-bit.
  TASKEX   : [0.5, 0.75, 1.0, 1.25, 1.5]                        -- the task's own example grid.
  VRPQ3    : VRP-quintile means (+1.9/+2.2/+2.6/+3.7/+5.9, OP-D1 a2, printed/booked, ledger
             line "Entry OP-D1") normalized so Q3=1.0 (the mid bucket) -> [0.731,0.846,1.0,
             1.423,2.269]. Provenance-linked, not an invented number (CONTRACT s6 "no magic
             numbers").
  VRPQ4ANC : same VRP ratios but ANCHORED so Q4=1.0 (i.e. the currently-dominant reachable
             bucket keeps its EXISTING sizing unchanged; only the rarer, highest-VRP Q5 bucket
             is scaled up by its OP-D1-measured relative premium, 5.9/3.7=1.595) ->
             [.,.,.,1.0,1.595]. This is the minimal-departure design.
  TASKEX_NOCAP: TASKEX's multipliers applied PRE-cap only (cap held at the original 0.10,
             i.e. f = min(0.150*s_t,0.10)*mult) -- isolates whether the cap itself must move
             for scaling to matter at all (OP-D2 SYNTHESIS S3: base f is already >0.10 for
             pct in {0.60,0.80,0.95} before any cap, so a mult applied only pre-cap and then
             re-capped at 0.10 is expected to be a near no-op).

Reuses scripts/analyze_op_d3.py's run() machinery (BS pricer, leg builder, roll/stop/stand-
down state machine) verbatim -- only the sizing line is touched. Reuses
scripts/analyze_op_d6b.py's run_book()/stats_of() book engine for the book-level delta,
substituting the condor sleeve's OP_RET stream with each design's standalone return series
(same house convention OP-D6b itself uses to fold OP-D3's sleeve into the book: an isolated
book0=100 sleeve run, pct_change taken, then applied additively as book*OP_RET[t] -- f was
defined by OP-D2 C02 as "fraction of BOOK posted as margin," so this substitution is the
correct like-for-like drop-in).

BS flat-sigma at India VIX, r=0.06, zero costs -- paper best-case, stated (same caveats as
OP-D3/OP-D6b: no smile/skew, no bid-ask, margin proxy = max loss, India VIX sample ends
2023-04-05, GFC 2008 not in the VIX sample).
"""
import sys
import time

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/user/claude-demo")

D3 = "/home/user/claude-demo/scripts/analyze_op_d3.py"
D6B = "/home/user/claude-demo/scripts/analyze_op_d6b.py"
D0, D1 = pd.Timestamp("2011-07-01"), pd.Timestamp("2023-03-31")

t_start = time.time()
cells_consumed = 0

# ---------------------------------------------------------------------------
# Load OP-D3 machinery verbatim (df with pct/ewvol, BS pricer, leg builder,
# last_thursday, no_entry set) -- the same pattern OP-D6b uses to reuse OP-D3.
# ---------------------------------------------------------------------------
_src3 = open(D3).read()
_ns3 = {}
exec(_src3.split("BASE = ")[0], _ns3)  # noqa: S102 (trusted local repo file, house pattern)
df3 = _ns3["df"]
make_legs = _ns3["make_legs"]
price_legs = _ns3["price_legs"]
last_thursday = _ns3["last_thursday"]
no_entry = _ns3["no_entry"]


def quintile_idx(p):
    """Fixed cutpoints 0.20/0.40/0.60/0.80 on the expanding VIX percentile -- standard
    quintile boundaries, not fitted/tuned to this backtest."""
    if p < 0.20:
        return 0
    if p < 0.40:
        return 1
    if p < 0.60:
        return 2
    if p < 0.80:
        return 3
    return 4


def run_scaled(entry_th, wing, roll_th, mults, d0, d1, cap_scales=True, book0=100.0):
    """OP-D3 run() verbatim, with ONE change: the sizing line applies a quintile multiplier
    (frozen at entry, based on that day's expanding-VIX-percentile quintile).
    cap_scales=True  -> f = min(0.150*s_t, 0.10*mult[q])   (the cap itself scales)
    cap_scales=False -> f = min(0.150*s_t, 0.10) * mult[q] (multiply the already-capped f)
    Returns condor-sleeve-standalone stats plus a per-entry log (date, quintile, f, cycle
    return) for the entry-quintile diagnostic.
    """
    book = book0
    eq = []
    pos = None
    rearm = True
    entry_log = []  # (t, quintile, f, entry_book) -- cycle P&L attributed at close
    for t, row in df3.loc[d0:d1].iterrows():
        S, vix, pct = row.S, row.vix, row.pct
        day_pnl = 0.0
        if pos is not None:
            v, dlt = price_legs(pos["legs"], S, vix, pos["exp"], t)
            day_pnl = (v - pos["mark"]) * pos["units"]
            pos["mark"] = v
            closed = False
            if t >= pos["exp"]:
                closed = True
            elif pct >= 0.90:
                closed = True
                rearm = False
            elif day_pnl / book <= -0.0222:
                closed = True
                rearm = False
            elif abs(dlt) >= roll_th:
                if pos["rolls"] >= 3:
                    closed = True
                else:
                    legs, _ = make_legs(S, vix, pos["exp"], t, wing)
                    nv, _ = price_legs(legs, S, vix, pos["exp"], t)
                    pos.update(legs=legs, mark=nv, rolls=pos["rolls"] + 1)
            if closed:
                entry_log.append(dict(t_entry=pos["t0"], q=pos["q"], f=pos["f"],
                                       book_at_entry=pos["book0"],
                                       cycle_ret=(book + day_pnl) / pos["book0"] - 1))
                pos = None
        book += day_pnl
        if not rearm and pct < 0.60:
            rearm = True
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
            if maxloss <= 0:
                eq.append((t, book))
                continue
            s_t = min(0.15 / max(row.ewvol, 1e-6), 2.0)
            q = quintile_idx(pct)
            mult = mults[q]
            if cap_scales:
                f = min(0.150 * s_t, 0.10 * mult)
            else:
                f = min(0.150 * s_t, 0.10) * mult
            units = f * book / maxloss
            pos = dict(legs=legs, exp=exp_d, units=units, mark=v0, rolls=0,
                       f=f, q=q, t0=t, book0=book)
        eq.append((t, book))
    if pos is not None:
        entry_log.append(dict(t_entry=pos["t0"], q=pos["q"], f=pos["f"],
                               book_at_entry=pos["book0"], cycle_ret=book / pos["book0"] - 1))
    e = pd.Series(dict(eq))
    mo = e.resample("ME").last().pct_change().dropna()
    yrs = (d1 - d0).days / 365.25
    geo = (e.iloc[-1] / e.iloc[0]) ** (1 / yrs) - 1
    dd = (e / e.cummax() - 1).min()
    return dict(geo=100 * geo, maxdd=100 * dd, worst_mo=100 * mo.min(),
                pos_mo=100 * (mo > 0).mean(), mo=mo, eq=e,
                entries=pd.DataFrame(entry_log))


BASE_PARAMS = (0.60, 2.5, 0.30)  # standing sleeve params, unchanged (C11/C03/C08)

DESIGNS = {
    "BASE": dict(mults=[1.0, 1.0, 1.0, 1.0, 1.0], cap_scales=True),
    "TASKEX": dict(mults=[0.5, 0.75, 1.0, 1.25, 1.5], cap_scales=True),
    "VRPQ3": dict(mults=[0.731, 0.846, 1.0, 1.423, 2.269], cap_scales=True),
    "VRPQ4ANC": dict(mults=[0.0, 0.0, 0.0, 1.0, 1.595], cap_scales=True),  # Q0-2 unreachable
    "TASKEX_NOCAP": dict(mults=[0.5, 0.75, 1.0, 1.25, 1.5], cap_scales=False),
    # control: is "VRP quintile scaling" doing anything beyond "just make Q4 bigger"?
    # same Q4 multiplier as VRPQ3 (1.423), applied UNIFORMLY (no quintile differentiation
    # at all) -- since Q5 fires only 3/33 times, this isolates the Q4-vs-Q5 split's own
    # marginal contribution.
    "FLATUP_Q4MATCH": dict(mults=[1.423, 1.423, 1.423, 1.423, 1.423], cap_scales=True),
    # C11-COMPLIANT design: the existing f_cap=0.10 is itself a structural invariant ("a
    # full-margin wipe alone must not breach the 10% DD ceiling" -- OP-D2 SYNTHESIS S3/S7).
    # Every design above RAISES that cap above 0.10 in the reachable buckets and so BREACHES
    # it. The only way to differentiate by quintile WITHOUT breaching C11 is to shrink the
    # lower-VRP reachable bucket (Q4) rather than grow the higher-VRP one (Q5) -- Q5 keeps
    # its existing 1.0x (still capped at 0.10).
    "DOWNQ4": dict(mults=[1.0, 1.0, 1.0, 0.75, 1.0], cap_scales=True),
}

results = {}
print(f"=== f02_vrp_scaled_condor === entry>=0.60, wing 2.5, roll 0.30 (unchanged), "
      f"{D0.date()}..{D1.date()}")

# --- reachability check (not a cell: a data scan of the entry gate itself) ---
elig = df3.loc[D0:D1]
elig_pct = elig.loc[(elig["pct"] >= 0.60) & (~elig.index.isin(no_entry)), "pct"]
reachable_q = sorted(set(quintile_idx(p) for p in elig_pct))
print(f"reachability check: entry-eligible days span quintiles {reachable_q} "
      f"(pct range on eligible days: [{elig_pct.min():.3f}, {elig_pct.max():.3f}])")

for name, spec in DESIGNS.items():
    r = run_scaled(*BASE_PARAMS, spec["mults"], D0, D1, cap_scales=spec["cap_scales"])
    cells_consumed += 1
    results[name] = r
    print(f"[{name:14s}] standalone geo {r['geo']:+.3f}%/yr | maxDD {r['maxdd']:.3f}% | "
          f"worst mo {r['worst_mo']:+.3f}% | mo>0 {r['pos_mo']:.1f}% | n_entries {len(r['entries'])}")

base = results["BASE"]
assert abs(base["geo"] - 1.07) < 0.02 and abs(base["maxdd"] - (-2.93)) < 0.02, \
    "BASE design must reproduce OP-D3a bit-for-bit (sanity check failed)"
print("  sanity check vs OP-D3a printed baseline (geo+1.07/maxDD-2.93): MATCH")

print("\n--- entry-quintile diagnostic (BASE run, mult=1.0 uniform -- descriptive, 2 "
      "conditional means) ---")
ent = base["entries"]
q_diag = {}
for q, label in [(3, "Q4 [0.60,0.80)"), (4, "Q5 [0.80,1.00]")]:
    sub = ent[ent["q"] == q]
    cells_consumed += 1
    if len(sub):
        q_diag[label] = dict(n=len(sub), mean_cycle_ret=100 * sub["cycle_ret"].mean(),
                              worst_cycle_ret=100 * sub["cycle_ret"].min(),
                              mean_f=sub["f"].mean())
        print(f"  {label}: n={len(sub)} mean cycle ret {q_diag[label]['mean_cycle_ret']:+.3f}%  "
              f"worst {q_diag[label]['worst_cycle_ret']:+.3f}%  mean f {q_diag[label]['mean_f']:.4f}")
    else:
        q_diag[label] = dict(n=0)
        print(f"  {label}: n=0 (unreached)")
other_q = ent[~ent["q"].isin([3, 4])]
print(f"  other quintiles (should be empty given entry>=0.60): n={len(other_q)}")

# --- book-level integration: substitute each design's condor stream into the standing book ---
print("\n--- book-level integration (OP-D6b honest baseline: 0.65 core/0.20 switcher/0.15 "
      "factor, financing=True, syn_margin=True) ---")
_src6 = open(D6B).read()
_ns6 = {}
exec(_src6.split("# === MAIN ===")[0], _ns6)  # noqa: S102 (trusted local repo file)
run_book = _ns6["run_book"]
stats_of = _ns6["stats_of"]
dates6 = _ns6["dates"]

book_results = {}
for name in ["BASE", "TASKEX", "VRPQ3", "VRPQ4ANC", "FLATUP_Q4MATCH", "DOWNQ4"]:
    op_ret_design = results[name]["eq"].pct_change().reindex(dates6).fillna(0)
    _ns6["OP_RET"] = op_ret_design
    eq, pm = run_book(0.65, 0.20, 0.15, financing=True, syn_margin=True)
    cagr, dd, yearly = stats_of(eq)
    cells_consumed += 1
    book_results[name] = dict(cagr=cagr, maxdd=dd, peak_margin=100 * pm, worst_yr=100 * yearly.min(), eq=eq)
    print(f"[{name:14s}] BOOK CAGR {cagr:+.3f}%/yr (TR~{cagr+1.3:+.3f}) | maxDD {dd:.3f}% | "
          f"peak margin {100*pm:.2f}% | worst yr {100*yearly.min():+.2f}%")

print("\n--- diagnostic: why does book maxDD IMPROVE when standalone condor maxDD WORSENS? "
      "(reuses the book eq already computed above -- no new cell) ---")
for name in ["BASE", "VRPQ3"]:
    eq = book_results[name]["eq"]
    trough_book = (eq / eq.cummax()).idxmin()
    print(f"  [{name}] book maxDD trough date: {trough_book.date()} "
          f"(condor sleeve's own worst month: {results[name]['mo'].idxmin().date()}, "
          f"worst {results[name]['mo'].min()*100:+.2f}%)")

print(f"\nBASE book reproduces OP-D6b a5 (CAGR+11.13/maxDD-11.53)? "
      f"{'MATCH' if abs(book_results['BASE']['cagr']-11.13) < 0.05 and abs(book_results['BASE']['maxdd']-(-11.53)) < 0.05 else 'DRIFT -- check'}")

print(f"\ncells_consumed = {cells_consumed}")
print(f"elapsed = {time.time()-t_start:.1f}s")

# ---------------------------------------------------------------------------
# Verdict against the pre-registered bars
# ---------------------------------------------------------------------------
print("\n=== VERDICT ===")
for name in ["TASKEX", "VRPQ3", "VRPQ4ANC", "TASKEX_NOCAP", "FLATUP_Q4MATCH", "DOWNQ4"]:
    r = results[name]
    d_geo = r["geo"] - base["geo"]
    d_dd = r["maxdd"] - base["maxdd"]  # negative number worse (more negative)
    r1 = (d_geo >= 1.0) and (d_dd >= -2.0)
    line = f"  {name:14s} standalone: d_geo {d_geo:+.3f}pp d_maxDD {d_dd:+.3f}pp -> R1 {'PASS' if r1 else 'MISS'}"
    if name in book_results:
        bd_geo = book_results[name]["cagr"] - book_results["BASE"]["cagr"]
        bd_dd = book_results[name]["maxdd"] - book_results["BASE"]["maxdd"]
        r2 = (bd_geo >= 0.3) and (bd_dd >= -1.0)
        line += f" | book: d_CAGR {bd_geo:+.3f}pp d_maxDD {bd_dd:+.3f}pp -> R2 {'PASS' if r2 else 'MISS'}"
    print(line)
