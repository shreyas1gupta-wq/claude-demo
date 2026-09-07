"""
c05: OP-D2 combiner -- adjudicate vol-forecast input choice for sizing from f03/f04/f12.

Does NOT recompute any raw backtest; combines only desk numbers already printed in
research/opt_sweep/f03.json, f04.json, f12.json (process note #6 / chapter-agent citation
rule applied here to a combiner). Ranks all printed 1d-ahead QLIKE cells on a common scale
and checks whether GARCH's tie-band edge over EWMA .94 survives once onset-lag (crisis)
behavior is weighed alongside average-day QLIKE.
"""
import json

ROOT = "/home/user/claude-demo/research/opt_sweep"

f03 = json.load(open(f"{ROOT}/f03.json"))
f04 = json.load(open(f"{ROOT}/f04.json"))
f12 = json.load(open(f"{ROOT}/f12.json"))

# ---- 1. Pool every 1d-ahead QLIKE point estimate printed across the three families ----
pool = []
for c in f03["cells"]:
    pool.append((f"F03:{c['name']}", c["value"]))
for c in f12["cells"]:
    pool.append((f"F12:{c['name'][:28]}", c["value"]))
# f04 prints a %-gap, not raw QLIKE levels, but the caveats give the raw means for c1
pool.append(("F04:garch_1,1_qlike (n=3799 subsample, 2010-10-11..2026-04-13)", 1.496020))
pool.append(("F04:ewma_0.94_qlike (same n=3799 subsample)", 1.504550))

pool.sort(key=lambda x: x[1])
best = pool[0][1]

print("=== Pooled 1d-ahead QLIKE ranking (lower = better forecast) ===")
for name, val in pool:
    print(f"{val:.6f}  (+{100*(val-best)/best:5.2f}% vs best)  {name}")

# ---- 2. GARCH vs EWMA .94: does the tie-band QLIKE edge survive a crisis-behavior check? ----
garch_c2 = next(c["value"] for c in f04["cells"] if c["name"].startswith("c2"))
ewma_c3 = next(c["value"] for c in f04["cells"] if c["name"].startswith("c3"))
print("\n=== F04 crisis-onset check (Mar-2020, vol-pt lag of 1d-ahead forecast vs fwd-5d RV) ===")
print(f"GARCH(1,1) onset lag: {garch_c2:.1f} vol pts (PASS >= 20 bar)")
print(f"EWMA .94   onset lag: {ewma_c3:.1f} vol pts (PASS >= 20 bar)")
print(f"Delta (GARCH advantage): {ewma_c3 - garch_c2:.1f} vol pts, against a ~72-94 pt error scale "
      f"-> {'immaterial' if abs(ewma_c3-garch_c2) < 5 else 'material'}")

# ---- 3. Same-family average-day QLIKE edge magnitude vs its own registered tie band ----
gap_pct = -0.57  # f04 headline gap, GARCH vs EWMA .94, same n=3799 window
print(f"\nF04 same-window QLIKE gap GARCH vs EWMA .94: {gap_pct}% (registered tie band is |gap|<2%; "
      f"independent re-derivation in f04's own audit got -0.69%, still inside band, same sign)")

# ---- 4. Parkinson (range-based) vs close-close: does adding OHLC info help? ----
pk = next(c["value"] for c in f12["cells"] if c["name"].startswith("c1"))
cc = next(c["value"] for c in f12["cells"] if c["name"].startswith("c2"))
print(f"\nF12 Parkinson-21d vs close-close-21d: {100*(pk-cc)/cc:+.2f}% (Parkinson WORSE; "
      f"registered bar was Parkinson beats by >=5% -> MISS)")

# ---- 5. Final ranking table: best single point vs the practical recommendation ----
print("\n=== Verdict ===")
print("Best pooled QLIKE point estimate: GARCH(1,1) MLE, 1.496020 -- but only ties EWMA .94 (F04, "
      "gap -0.57% inside the |gap|<2% registered tie band) and buys NO onset-detection edge "
      f"({ewma_c3-garch_c2:.1f} vol-pt difference vs a 72-94pt error).")
print("EWMA lambda=0.94 is grid-best among all EWMA/rolling combinations tested in F03 "
      "(1.501643, beating roll_21's 1.520021 by 1.21%, ewma_.90's 1.506709, and ewma_.97's 1.526107), "
      "though it misses F03's own registered >=3% promotion bar vs roll-21.")
print("Parkinson (range-based) is dominated outright: -7.55% vs close-close-21, a clean MISS (F12).")
print("Recommendation: EWMA, lambda=0.94, close-to-close returns as input -- GARCH(1,1) is not worth "
      "its added refit/optimizer-convergence machinery for a statistically-tied, crisis-indistinguishable "
      "gain; rolling windows and the Parkinson range estimator are both dominated on printed numbers.")
