# Pass 2 — development window (1990-01..2012-06 unless noted), 3 bp / 60 bp

| Candidate | Lens | Tunables | DEV Sharpe | DEV CAGR | DEV maxDD | Chg/yr | Cash % | Avg lev invested | Up-capt | Down-capt | 1950–2012 Sharpe | Worst era DD | 2000-02 | GFC | 2009 rec. | Plateau | 6/90 Sharpe | Gates | DEV param sets |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| final_model_fewtrades | pass-1 incumbent | 6 | 0.43 | 10.14% | -25.1% | 7.1 | 32 | 2.03 | 109% | 102% | 0.56 | -32.6% | -21.1% | -8.6% | 6.6% | 75% | 0.40 | PASS | — |
| baseline_volregime | pass-1 reference | 4 | 0.37 | 9.87% | -38.2% | 11.6 | 32 | 2.42 | 127% | 130% | 0.63 | -31.2% | -26.3% | -15.3% | 7.7% | 81% | 0.33 | FAIL G2/G3 | — |
| vix_dissipation | pass-1 trap | 6 | -0.31 | -7.18% | -93.5% | 46.6 | 40 | 2.37 | 78% | 159% | -0.19 (cash pre-1990) | -91.3% | -80.1% | -67.1% | 7.2% | 83% | -0.45 | FAIL G2/G3/G4/G5 | — |
| vix_vrp | pass-1 file, never evaluated | 5 | 0.61 | 10.61% | -19.8% | 6.0 | 64 | 1.65 | 60% | 30% | 0.36 (cash pre-1990) | -19.8% | 15.1% | -15.7% | 44.4% | 100% | 0.58 | PASS | — |
| crash_exit_dual | lens 1 | 6 | 0.45 | 11.19% | -52.8% | 12.0 | 13 | 1.81 | 133% | 131% | 0.44 | -51.8% | -54.2% | -42.5% | 53.8% | 88% | 0.42 | FAIL G3/G4 | 1326 |
| dissipation_reentry | lens 2 | 6 | 0.45 | 7.86% | -12.4% | 3.9 | 52 | 1.04 | 52% | 33% | 0.45 | -19.6% | 2.8% | -0.6% | 0.5% | 79% | 0.43 | PASS | 864 |
| volmanaged | lens 3 | 5 | 0.49 | 7.39% | -19.8% | 1.8 | 0 | 0.63 | 55% | 40% | 0.36 | -34.5% | -0.1% | -19.8% | 11.4% | 100% | 0.49 | PASS | 806 |
| sticky_tier | lens 4 | 5 | 0.61 | 7.38% | -14.3% | 0.4 | 67 | 1.18 | 36% | 12% | 0.35 | -33.9% | 9.7% | 2.2% | 0.1% | 90% | 0.61 | PASS | 13 |
| vix_vrp_v2 | lens 5 | 6 | 0.68 | 11.71% | -19.8% | 10.6 | 62 | 1.61 | 64% | 30% | 0.40 (cash pre-1990) | -19.8% | 12.9% | -9.5% | 43.6% | 96% | 0.64 | PASS | 796 |
| composite_dual_engine | lens 6 | 6 | 0.54 | 11.41% | -25.6% | 5.5 | 42 | 1.81 | 85% | 62% | 0.32 (cash pre-1990) | -25.6% | -14.4% | 3.4% | 0.1% | 96% | 0.52 | PASS | 1125 |

SPY buy-and-hold: dev_1990 Sharpe 0.39 (CAGR 8.34%, maxDD −50.8%); 1950–2012 Sharpe 0.47. Gates per PREREG.md; 'DEV param sets' = distinct parameter sets the designer evaluated on the development window (self-reported).