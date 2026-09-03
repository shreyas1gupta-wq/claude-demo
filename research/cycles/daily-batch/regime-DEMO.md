# Stage-1 end-to-end DEMO — the ladder runs on real history (2026-09-02)
MACHINERY DEMONSTRATION, not a trial: no bars, nothing promoted. Script:
scripts/demo_regime_timeline.py. Chain exercised: vaulted NIFTY daily → L2 composite
(quant/ladder) → assemble_regime (quant/regime, availability-weighted, n_blocks=1
throughout — L2 is the only computable seat here, stated on every row) → bucket_path
(quantile rules on R's own expanding history, grid {0.5, 0.8, 0.95}).

## The first real regime timeline (4,031 bucketed days, 2008-2026)
R1 normal 50.1% · R2 watch 31.1% · R3 slow bear 15.4% · R4 crisis 3.5% — the crisis bucket
is rare by construction (the 0.95 cut) and lands where history put the crises:

| R4 episode (>=3 sessions) | Sessions | The event it found |
|---|---|---|
| 2016-02-11 .. 2016-03-01 | 14 | the global-selloff bottom after the China-deval winter |
| 2018-10-19 .. 2018-11-01 | 10 | the IL&FS aftermath |
| 2020-03-06 .. 2020-06-22 | 70 | COVID — by far the longest stay |
| 2022-03-02 .. 2022-03-11 | 8 | the Russia shock |
| 2025-04-07 .. 2025-04-16 | 6 | the April-2025 global tariff shock [context: public record] |
| 2026-03-19 .. 2026-04-13 | 15 | runs to the vault's last day — the state was ALREADY in R4 entering the documented May-2026 INR/FII episode |

## Honest notes
- Single-seat R: with only fast_stress available, R IS the L2 state — the demo proves the
  plumbing (availability weighting, quantile buckets, trails), not multi-block behavior;
  the synthetic tests cover multi-block exactness.
- The 2026 tail observation is the demo's one striking read: the machinery, fed only
  through 2026-04-13, holds the crisis bucket into the data's edge — consistent with (not
  predictive of) the May-2026 episode the program documented independently. Logged as a
  demonstration, never as a forecasting claim.
- Feb-2018 does NOT appear (the 2008 shadow, as measured in F2a) and Jan-2008 falls in
  warm-up — both known properties, carried here for consistency.
