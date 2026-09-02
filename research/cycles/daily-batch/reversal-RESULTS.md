# MR1-S — the survivor-panel reversal preliminary: result and honest read
Written AFTER the print (2026-09-02). Pre-registration: ledger MR1-S (one-way rule).
Script: scripts/analyze_reversal_prelim.py. Data: vaulted NIFTY500 survivor panel
(487 tickers 2012-2021; survivorship stated) + vaulted NIFTY 50 daily.

## The print
116 months, median universe 209 liquid names. Long losers / short winners (monthly
deciles): GROSS +0.20%/mo, t=0.39. Median one-side turnover 89%/month; the config cost
stack (28bp/side midpoint) turns that into 0.99%/mo of drag. NET −0.80%/mo, and negative
in BOTH half-samples (2012-16: −1.20; 2017-21: −0.42). One-way verdict: **the L1 freeze is
corroborated** — on data biased IN THE SIGNAL'S FAVOR, 1-month reversal is statistically
zero before costs and decisively negative after them.

## Honest read
1. The kill is double: the anomaly fails on SIGNAL (t=0.39 gross — this is not a costs
   story alone; there is nothing there to harvest on 2012-2021 India) and on COSTS (the
   Novy-Marx-Velikov knife, now with Indian numbers: ~1%/month of drag at 89% turnover).
   The sample is entirely post-colocation (NSE colo era from ~2009-10) — consistent with
   the US record of reversal decaying as HFT market-making capacity grew.
2. The stress twist: gross reversal is NEGATIVE in top-decile vol months (−0.36%/mo) and
   positive in calm ones (+0.26) — the opposite of the Nagel US pattern where liquidity-
   provision premia spike in stress. At n≈12 stress months this is a tag, not a claim; if
   the true MR1 reproduces it, the mechanism story for India changes (in stress, losers
   keep losing — crash-momentum rather than liquidity premia at the monthly horizon), and
   the L1 flag's one legitimate use (entry-timing hygiene) survives while any harvest story
   dies even harder.
3. What this does NOT do: unfreeze anything (nothing passed), or discharge the true MR1
   (point-in-time membership remains registered and required — a survivor panel cannot
   produce the affirmative case, only the corroboration it just produced).

## Consequence
- L1_reversal_1m stays frozen; its ladder provenance now carries a real print instead of
  only the literature prior.
