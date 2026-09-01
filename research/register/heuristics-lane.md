# The Heuristics Lane — simple rules, judged by mechanism (charter)

Principal directive (2026-09-01): simple, broadly-understood rules — overbought-extension vs a
moving average, RSI, gap-up thresholds, volume multiples, economics-backed cycles with no fixed
period — must be CONSIDERED for regime states and alpha, and must NOT be rejected solely on
data-pattern statistics (t-stats etc.). Broad understanding and simplicity are first-class values;
the principal may take discretionary decisions on them, with Claude teaching alongside.

## Why this is aligned with the contract, not an exception to it

Simplicity is an anti-overfitting technology: a rule with <=2 parameters has almost no capacity to
memorize history (Carver's no-fitted-parameters philosophy; our pipeline-v2 two-tier admission
already gives rationale-backed rules a LOWER evidence bar than statistics-only ones). The contract
bans unexamined claims, not simple ones.

## Lane rules (binding)

1. ADMISSION BY MECHANISM: a card needs a one-sentence economic story naming who is on the wrong
   side of the trade and why they are stuck there. <=2 parameters, both on pre-registered grids.
   No mechanism, no card.
2. JUDGED BY SIGN, EPISODES, AND PAPER — not t-stat maximization: (i) sign-consistency across
   decades/regimes (never effect-size equality), (ii) episode/frequency tables (the H63 style),
   (iii) live paper probation as the primary evidence. Statistics INFORM; they alone neither
   execute nor veto.
3. REDUCE-ONLY FIRST: a heuristic's first admitted job is subtracting risk (trim entries, pause,
   raise hedge earlier). Adding exposure requires the full funnel like anything else.
4. REJECTION NEEDS BOTH FAILURES: a card is rejected only when the mechanism fails scrutiny AND
   the evidence fails. Every card stays in this register with its verdict and reason — nothing is
   silently dropped. Verdicts: {adopt-reduce-only | paper-trade | teach-only | reject-with-reason}.
5. THE PRINCIPAL'S DISCRETION lives in the Stage-2 scored channel: any discretionary call becomes
   a timestamped paper trade, scored by category (TOPS). Influence follows the published grid;
   the veto survives any score. Decisions are kept score on, never silenced.
6. Trial-ledger discipline still applies: every grid cell examined is a counted trial.

## Candidate cards (opened 2026-09-01, from the principal's examples)

| Card | Rule (parameters on grids) | Mechanism (one sentence) | First job | Status |
|---|---|---|---|---|
| HL-1 ATR-extension | price >= {4,6,8,10} x ATR(14) above the 50-DMA => overextended | late-arriving chasers are the marginal buyer and reverse first | reduce-only: trim/pause entries into extension | open -> H69 |
| HL-2 Gap events | index/stock gap-up > {5, 7.5, 10}% | overnight information shock; herding + circuit dynamics decide drift-vs-fade | event study first (frequency table); circuit-band-aware (5/10/20% bands make some "gaps" locked circuits, not signals) | open -> H70 |
| HL-3 Volume multiples | volume >= {2,3,5} x its trailing median | participation confirms or exposes a move (ties to H60 breadth family) | confirm input candidate for L2/L4 | open -> H70 |
| HL-4 RSI band | RSI(14) outside {20/80, 30/70} | bounded momentum oscillator ~ short-horizon reversal in trader's units (overlaps L1 seat) | teach + redundancy check vs L1 reversal before any seat | open (redundancy guard) |
| HL-5 Econ cycles w/o clocks | any economics-backed cycle with no fixed period | this IS the ladder's state-variable philosophy (Lesson 1 Part 0.1) | route to the cycle-atlas intake as new-state candidates | standing route |
| HL-6 18-year property clock | "real-estate peaks every ~18y" (Hoyt/Harrison/Foldvary lineage) | land-supply inelasticity + construction lags + credit collateral feedback — the MECHANISM is real and already seated (L12) | none as a clock | **reject-with-reason** (2026-09-01): mechanism ACCEPTED but already seated in L12 (no double-count); the FIXED PERIOD fails both lane tests — no mechanism produces a constant period (rate/credit/planning regimes shift it), and evidence fails the pre-registered bar (RE1: 45% of spacings in [14,22]y, range 8-45y; ledger). First lane rejection — the lane demonstrably filters, not rubber-stamps |

## Hypothesis rows

Registered as H69-H71 in docs/masterplan/C-hypothesis-register.md Addendum 4. India circuit-filter
interaction is part of H70's design, not a footnote.
