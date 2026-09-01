# Atlas 0.1 — debt supercycle: JST R6 real-data results (advanced-economy priors)

18 countries, 1870-2020. Real short rate = stir − CPI inflation; hyperinflation-era
cells (|inflation|>50%) excluded from era means (Weimar rule from the momentum batch).
Generated 2026-09-01; trials DS1-DS4 ledgered. These are PRIORS for L15 (Tier C,
reduce-only gold-floor attribution) — never timing inputs, never India estimates.

## DS1 — How rare is a completed fiat-era deleveraging?

Definition: post-1971 peak debt/GDP followed by a decline of >=30pp that HELD
(no re-ascent above the old peak by 2020).

| Country | post-1971 peak (yr) | max decline from peak | completed arc? |
|---|---|---|---|
| Australia | 57% (2020) | 0pp | no |
| Belgium | 135% (1993) | 48pp | YES |
| Canada | 117% (2020) | 0pp | no |
| Denmark | 72% (1998) | 39pp | YES |
| Finland | 70% (2020) | 0pp | no |
| France | 115% (2020) | 0pp | no |
| Germany | 82% (2010) | 23pp | no |
| Ireland | 120% (2013) | 63pp | YES |
| Italy | 156% (2020) | 0pp | no |
| Japan | 254% (2020) | 0pp | no |
| Netherlands | 75% (1993) | 32pp | YES |
| Norway | 53% (2006) | 24pp | no |
| Portugal | 135% (2020) | 0pp | no |
| Spain | 120% (2020) | 0pp | no |
| Sweden | 73% (1996) | 38pp | YES |
| Switzerland | 58% (2004) | 18pp | no |
| UK | 104% (2020) | 0pp | no |
| USA | 128% (2020) | 0pp | no |

Countries whose post-1971 peak occurred before 2000 AND completed a >=30pp lasting decline: **4 of 18** — the atlas's 'n<2 in the fiat era' claim is conservative but directionally right: most fiat-era debt arcs are still on their ascent (peaks cluster at 2020, i.e., censored, not completed).

## DS2 — Financial repression (Reinhart-Sbrancia replication-lite)

| Era | share of country-years with NEGATIVE real short rates | mean real short | n |
|---|---|---|---|
| gold/interwar 1870-1944 | **25%** | +2.3% | 1143 |
| repression era 1945-1980 | **44%** | -0.8% | 622 |
| liberalization 1981-2007 | **10%** | +3.2% | 486 |
| post-GFC 2008-2020 | **76%** | -0.7% | 234 |

The repression signature: 1945-1980 negative-real-rate share far above the
liberalization era — the mechanism by which war debts were quietly amortized
(Reinhart-Sbrancia). The post-GFC share is the modern echo the L15 inputs watch

## DS3 — r − g by era (the debt-arithmetic driver)

| Era | mean (real short − real growth) | share of years r<g | n |
|---|---|---|---|
| gold/interwar 1870-1944 | +0.8pp | 41% | 1143 |
| repression era 1945-1980 | -4.3pp | 83% | 622 |
| liberalization 1981-2007 | +1.1pp | 37% | 486 |
| post-GFC 2008-2020 | -1.0pp | 73% | 234 |

When r<g persistently, debt/GDP can fall without surpluses — the painless arc.
When r>g (1981-2007), only surpluses or defaults reduce debt. The seat's job is
knowing WHICH arithmetic regime we are in, never predicting its end.

## DS4 — What repression does to investors (the L15 rationale)

| State (country-year) | mean real equity return | median | n |
|---|---|---|---|
| high debt AND negative real rates (fiscal-dominance state) | +4.5% | +3.4% | 196 |
| high debt, positive real rates | +10.0% | +7.4% | 326 |
| low/mid debt, negative real rates | +1.5% | +2.0% | 449 |
| low/mid debt, positive real rates (normal) | +9.5% | +7.9% | 1115 |

Read for design: equities still earn positive real returns on average in
repression states — the seat justifies a GOLD FLOOR and a debasement tail budget,
never an equity exit. Reduce-only, exactly as the atlas says.


## DS5 — The 90% 'cliff', re-run on the Herndon-Ash-Pollin panel

Panel: 20 advanced economies, 1946-2009, 1175 country-years (RR-processed.csv, vault-manifested).
Method: pooled country-year means/medians (the HAP-correct weighting).

| Debt/GDP bucket | mean real growth | median | n country-years |
|---|---|---|---|
| 0-30% | +4.17% | +4.15% | 426 |
| 30-60% | +3.09% | +3.10% | 439 |
| 60-90% | +3.19% | +2.90% | 200 |
| 90-120% | +2.41% | +2.37% | 79 |
| >120% | +1.56% | +2.04% | 31 |

- Pooled mean growth above 90% debt: **+2.17%** (RR 2010 claimed −0.1% via the spreadsheet exclusion + country equal-weighting HAP exposed).
- The 60-90 vs >90 growth gap: +1.02pp, bootstrap 95% CI [+0.26, +1.77] — a modest GRADIENT (high debt associates with somewhat slower growth, causality unresolved), not a cliff, and no bucket goes negative.
- Design consequence, already embedded: our states are PERCENTILES and grids — never threshold cliffs — and DS5 is the canonical reason why. Ledgered as trial DS5.

