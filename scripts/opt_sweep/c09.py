"""
c09: OP-D2 combiner -- India overlay design inputs from F22 (INR gate) + F21 (hedge-instrument
choice). No new backtest; this only re-derives simple ratios from the two ALREADY-VERIFIED
JSON files (research/opt_sweep/f21.json, f22.json) to support the design recommendation.
No lookahead concern: pure arithmetic on printed, cited numbers.
"""
import json

F21 = json.load(open("/home/user/claude-demo/research/opt_sweep/f21.json"))
F22 = json.load(open("/home/user/claude-demo/research/opt_sweep/f22.json"))

bank_ratio = F21["cells"][0]["value"]       # bank-heavy beta_hi/beta_lo
smallcap_ratio = F21["cells"][1]["value"]   # smallcap-tercile beta_hi/beta_lo

print(f"F21 bank-heavy beta_hi/lo      = {bank_ratio:.4f}  (contraction {100*(1-bank_ratio):.1f}%)")
print(f"F21 smallcap-tercile beta_hi/lo = {smallcap_ratio:.4f}  (contraction {100*(1-smallcap_ratio):.1f}%)")
print(f"Stability edge (smallcap/bank ratio-of-ratios) = {smallcap_ratio/bank_ratio:.3f}x")

corr = F22["cells"][0]["value"]
diff = F22["cells"][1]["value"]
print(f"\nF22 INR-mom x VRP corr r={corr:.4f} (two-sided, null)")
print(f"F22 weak/strong-INR VRP diff = {diff:.3f} vol pts (two-sided, null)")
print(f"F22 stand-down overlay: {F22['cells'][2]['value']}")
print("-> flags 89/154 = %.1f%% of months; cost (52.73%%) > trim (79.03%%) is not a net win"
      " once flag-rate this high is priced in (F20's stress overlays flag only 7-24%% of months)."
      % (100 * 89/154))
