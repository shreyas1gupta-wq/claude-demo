# The first daily-resolution batch — results and honest read
Written AFTER the prints (2026-09-02). Pre-registration: ledger CW-D1a/DW1/F1a/F2a.
Script: scripts/analyze_nifty_daily.py. Data: vaulted NIFTY 50 daily mirror
(2007-09-18..2026-04-13, n=4,553 returns; authentication 6/6).

## The prints
1. CW-D1a: budget-day-only |return| median 1.14% vs 0.59% all other days; MW one-sided
   p=0.110 — FAIL on the partial registration's bar. The ORIGINAL CW-D1 window (±1 day,
   registered 2026-09-02 before any daily data existed): median 0.95% vs 0.59%, p=0.0049 —
   PASS on that leg's bar. VIX leg still data-gated.
2. DW1: Kruskal-Wallis across weekdays H=2.83, p=0.587 — the 5.5 REJECT confirmed with
   evidence. Monday prints the HIGHEST median (+0.10%) — the opposite sign of the classic
   US weekend effect, and un-interpreted per the pre-stated rule.
3. F1a: two-leg composite tau_half ≈ 61 trading days ≈ 2.9 months — inside the ladder's
   registered [1,3] months, near the top. The block-bootstrap CI is documented as
   UNRELIABLE for this persistence (blocks ~ half-life); no CI is claimed.
4. F2a: 7/11 pre-named episodes detected at state ≥ 0.3 — FAIL against the ≥8/11 bar.
   False fires: 2.6% of valid days (measurement, no bar).

## Honest read
- **The resolution theorem's positive leg landed.** CW1 (monthly) showed February ordinary;
  the daily ±1-window print shows budget windows carry ~60% higher |returns| (p=0.005).
  Same phenomenon, two resolutions, both now measured — the L5 seat's vol-scheduling claim
  finally rests on OUR print, not only the literature. The day-only cut fails at n=19;
  nothing is promoted beyond what L5 already does (reduce-only scheduling, unchanged).
- **A process error is on the record:** the partial registration transposed the original
  CW-D1 window (day-only vs ±1). Caught at the honest-read stage because the original
  registration was written down first. Neither bar moved; both prints stand; the
  verification-log gets the note. The lesson: a PARTIAL run must quote its parent design
  verbatim, never paraphrase it.
- **F2a's fail is worth more than a pass.** The four misses decompose into: one
  untestable (warm-up NaN — a registration that failed to anticipate coverage), two
  design-consistent (2013 lived on the absent funding leg — direct evidence FOR the
  three-leg architecture and FS-D2's taxonomy; demonetization never moved the index), and
  one genuine discovery — **the 2008 shadow**: once a mega-crisis enters the expanding
  history, a Feb-2018-size vol event ranks low and the state stays cold. Expanding
  percentiles buy no-look-ahead at the price of post-crisis de-sensitization. This is now
  a measured property of the whole ladder's percentile machinery, and the F2 full design
  must sweep window-capped percentile variants (e.g., trailing-10y) against expanding —
  registered as F2b below.
- **F1a agrees with the ladder.** ~2.9 months sits inside the registered tau_half [1,3]m —
  the first real-data corroboration of L2's placement on the ladder (near the slow end of
  the fast band, consistent with a 21d RV window + drawdown leg).

## New registration (bars before data, as always)
- **F2b (percentile-memory sweep):** at the full F2 run, detection/false-fire tables for
  expanding vs trailing-{5y, 10y} percentile variants across the same episode set and
  threshold grid; adjudication stays episode-DD-improvement NET of costs (F2's original
  currency), never raw detection counts. Prior stated: trailing windows re-sensitize at
  the cost of earlier false fires; the desk expects a trade, not a free lunch.
