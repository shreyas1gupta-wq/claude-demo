# Out-of-sample look log (append-only)

| when (IST) | module | setting | note |
|---|---|---|---|
| 2026-09-12 02:08 | sticky_tier | 3bp/60bp | signal look #1 |
| 2026-09-12 02:08 | sticky_tier | 2bp/40bp | same frozen signal, cost row |
| 2026-09-12 02:09 | sticky_tier | 6bp/90bp | same frozen signal, cost row |
| 2026-09-12 02:09 | final_model_fewtrades (pass-1 incumbent) | 3bp/60bp, 2bp/40bp, 6bp/90bp (tags p2, p2_c240, p2_s690) | re-run of the already-evaluated pass-1 model at the pass-2 cost rows; not a new look |
| 2026-09-12 02:20 | final_model, baseline_volregime, trend_vol_fewtrades, vix_dissipation, shock_reentry (pass-1 panel) | 3bp/60bp, 2bp/40bp, 6bp/90bp (tags p2, p2_c240, p2_s690, --no-sensitivity) | re-runs of already-evaluated pass-1 models at the pass-2 cost rows for a uniform leaderboard; not new looks |
