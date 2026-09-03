# THE PAPER LEDGER — every paper trade of record
Created 2026-09-02 (the depth audit found the format promised but not yet instantiated).
Rules: a paper trade enters here AT REGISTRATION with its rule quoted verbatim from its
source; each realization row is filled AT GRADING TIME from vaulted data, never from memory;
columns are pre-committed below and never restructured after the first row lands; a paper
trade that misses its grading date is marked LAPSED, not backfilled. Promotion conversations
cite this file; nothing here has a return budget.

## PT-1 — HL-7: the pre-election tilt (registered 2026-09-02, fiscal-cycle entry)
Rule (verbatim from HL-7): the pre-election window tilt is TEACH-ONLY, routed to paper —
long the index for the 2 calendar months before a general-election result month, flat
otherwise; graded per event, net of the config cost stack.
Grading data: vaulted daily index; result months from the FP1 fixed list.
| Event (result month) | Window return (net) | Index same-window | Verdict row filled on |
|---|---|---|---|
| next general election (exp. 2029) | (awaits event) | (awaits event) | result month + 1 |

## PT-2 — CW-PT1: the April small-cap tilt (registered 2026-09-02, calendar-signal entry)
Rule (verbatim from the CW-PT1 registration): each April, a modeled small-cap tilt
(cost model from config/costs.yaml, aggressive book's impact schedule) held Apr-1..Apr-30,
ledgered like HL-7; promotion discussable only after 3 Aprils AND net-of-modeled-cost
positive in >= 2.
Grading data: smallcap-vs-index April return net of the 28bp+impact stack (PIT bhavcopy
preferred; the survivor panel may print an UPPER BOUND only, labeled as such).
| April | Gross tilt return | Modeled cost | Net | Running tally |
|---|---|---|---|---|
| 2027 | (first grading) | | | 0/1 needed-positive so far |
| 2028 | | | | |
| 2029 | | | | earliest promotion conversation |

Lapse policy: a grading row not filled within 3 months of its date is marked LAPSED and the
trade's promotion clock RESETS — a paper trade nobody grades is a story, not evidence.
