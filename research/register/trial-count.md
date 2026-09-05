# THE TRIAL-COUNT CENSUS — the TRUE N for every deflated-Sharpe computation
Created 2026-09-02 (CONTRACT §9: "Deflated Sharpe with the TRUE trial count (all sweeps
counted)"). CONVENTION FROM TODAY: every new registration appends its row here with its
CELL COUNT (a grid of 18 cells is 18 trials, not 1); quant/stats/dsr.py consumers read
n_trials FROM THIS FILE, never from memory. Undercounting N inflates every future Sharpe —
this census exists so that can never happen silently.

## Cell-count rules (stated once)
- A single pre-registered test = 1 cell. A grid = its full cell count, INCLUDING cells that
  were disqualified or never reported individually.
- Demonstrations with pre-stated interpretation rules (CW3, GS1, DW1) COUNT — they consumed
  look at the data.
- Registered-but-unrun designs count 0 until run (their planned grids are noted for the
  forward budget).
- Shape checks inside authentications (anchors) do NOT count — they test data integrity,
  not hypotheses about returns.

## The census (run trials, by batch)
| Batch | Trials × cells | Cells |
|---|---|---|
| M0-M5 momentum real-data legs | 6 single + M2/M3 panel splits (2 each) | 10 |
| J-series (JST panel, 13 cells logged at the time) | as ledgered | 13 |
| Deep-dive/atlas trials Bands 0-3 (RR, KW1-2, RE1-2, CS1-4, IN1-3, SC1, BC1-3, KJ1, MP1-3, FP1a/b, GF1-3, DL1-3, CI1a/b, OL1, EN1-3, PS1-3, CR1a/b, CR2, PL1, A-series gold/inflation legs ~6) | ~38 singles | 38 |
| Calendar batch CW1-3 + GS1 | 4 singles | 4 |
| FS-U1/FS-U2 | 2 singles | 2 |
| Daily batch: CW-D1a (2 windows counted: day-only + ±1) · DW1 · F1a · F2a | 5 | 5 |
| MR1-S | 1 (one-way) | 1 |
| CR-D2a (P1+P2 shape checks) | 2 | 2 |
| F2-index grid | 3 triggers × 2 confirms × 3 re-entries | 18 |
| F7a (primary 63bd; 21bd secondary reported) | 2 | 2 |
| TS1 | 2 assets × 3 lookbacks | 6 |
| N4a (rho bar + overlap + stress split) | 3 | 3 |
| FS-D3 (FS-D3a + FS-D3b) | 2 | 2 |
| F1b · F1c (two estimators, one quantity — both consumed looks) | 2 | 2 |
| F2-WF (2 cells × 4 eras, era-level reads) | 8 | 8 |
| H67a (3 grid points, measurement) · H68a | 4 | 4 |
| H53a (Fuel primary + All-Commodity secondary) — census omission fixed 2026-09-03, cells ran 2026-09-02 | 2 | 2 |
| CW-D1v (budget±1 \|dlogVIX\| vs other days) | 1 | 1 |
| F5a (rank-corr redundancy + AUROC compare + VRP descriptive — all consumed looks) | 3 | 3 |
| OL-D1a (primary + flavor-agreement table) | 2 | 2 |
| EN-D2a (pooled + 3 eras + LPA sensitivity + secondary definition) | 6 | 6 |
| OL-D2a (primary + instrument-agreement) | 2 | 2 |
| F3a (MM full-period + Cederburg OOS + capped net-of-cost) | 3 | 3 |
| F4a (2 windows × redundancy+adds reads) | 4 | 4 |
| F6a (18 grid cells, ledger reads) | 18 | 18 |
| H58-D3a (full + 2 era reads) | 3 | 3 |
| T1 (full + bar + 2 eras + ex-COVID) | 5 | 5 |
| T-CTRL1 (10 MA rules) | 10 | 10 |
| T3 (2 k-cells) + T4 (Sharpe + alpha reads) | 4 | 4 |
| T2 (level + trend reads) | 2 | 2 |
| T1b (4 conditionings) + T6-TOM (full + 2 eras + fingerprint) | 8 | 8 |
| EN-D1a (2 baskets x 2 horizons, onset-conditioned) | 4 | 4 |
| GDP-D1 (3 cells) + FISH-D1 (3 cells) | 6 | 6 |
| ER-D1 (25 + 4 India) + ER-D2 (2) + ER-D3 (2) + ER-D4 (6) | 39 | 39 |
| ER-D5 same-period attribution (15 + 5 + 5) | 25 | 25 |
| ER-D6 US+India linear/nonlinear (8 US + 2 grid/rank reads + 4 India) | 14 | 14 |
| Audit follow-ups: ER-D7 (6) + ER-D4b (6) + ER-D1b (9) + ER-D1c (6) | 27 | 27 |
| ER-D8 market->GDP grid (9 pooled + 3 within + 2 India) | 14 | 14 |
| **RUNNING TOTAL (run cells)** | | **322** |

## Registered, unrun (forward budget — counts on the day they run)
F1 full · F2 full (>=21 cells: 18 + F2b×2 + F2c) · F3/F4/F5/F6 fulls (index/survivor partials F3a-F6a ALL run) · FS-D1/D2/D4 ·
CW-PT1 (3 Aprils) · CW2b · MR1 · CR-D1/D2/D3 · RT1/2 · FL1/2 · IS1/2 · CN-D1/2/3 · EN-D1 (EN-D2a's link-1 partial HAS run; the full annual re-print stands) ·
OL-D1 full/OL-D2 (OL-D1a partial HAS run) · H58-D1/2 + D3 close-auction leg (D3a index partial ran: null) · RC1 · H59-D1 · PT-1/PT-2 gradings. Plus the frozen future sweeps the
registry names (hedge grid × buckets <=28 cells; block-weight sweep).

## Use
Any Sharpe-like claim on ANY strategy this program produces must call
quant/stats/dsr.py::deflated_sharpe_ratio with n_trials >= the RUNNING TOTAL above at the
time of the claim (plus that strategy's own sweep cells). The census is append-only; the
total is never revised downward.

## Machinery note (2026-09-03)
The RUNNING TOTAL is now read mechanically: `quant.stats.dsr.census_n()` parses this file
(tests/test_landing_day.py enforces a rising floor), so a Sharpe claim wired through it can
never silently undercount trials. Update the table; the code follows.
