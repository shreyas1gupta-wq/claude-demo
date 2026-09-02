# Parts D–H — freeze-index math, routing, harvest, ledger (atlas 2.2; sub-component entry)

## Part D — The mathematics

**D1. The freeze index.** freeze_t = z_t(CP spread, 3m top-rated over matched T-bill) +
z_t(−rollover ratio), both z's expanding-window (shared grids; weekly cadence from WSS, daily
FBIL leg when it exists). Two legs because a run has two faces: PRICE (the spread the marginal
issuer pays) and QUANTITY (paper that simply does not roll). 2018's lesson is that quantity can
lead price — issuance died before spreads fully repriced — so neither leg alone suffices, and
the index is a MAX-style alarm at consumption (L2 treats either leg's extreme as actionable),
not an average that lets one calm leg mute a screaming one. [Constructed at step 51 of the
runsheet; SC2's acceptance bars are registered THERE, before any backtest look.]

**D2. The horizon algebra SC1 fixed.** SC1 measured propagation: within 12 months of the
IL&FS default, SMB sat at its 18th percentile and the MARKET at its 16th — the freeze became a
macro event faster than a monthly/12m equity window can isolate it. Formally: if the freeze
hits fundamentals with lag ℓ_f (months) and funding variables with lag ℓ_v (days-weeks), the
detection edge is the gap ℓ_f − ℓ_v — and SC1 says ℓ_f ≤ 12m, so all the harvestable edge
lives in ℓ_v. That is a measured argument, not a preference: the sub-cycle's signature
belongs to L2's daily/weekly family. Monthly equity factors are POST-MORTEM variables here.

**D3. De-dup algebra.** The entry's information set splits three ways with ZERO new budget:
composition (NBFC/unsecured share) — ALREADY a leg inside L10's single seat; market stress —
ALREADY L2's seat; funding-freeze variables — NEW INPUTS offered to L2's existing family
under L2's existing budget. A "shadow-credit seat" would be L10's composition leg plus L2's
stress seat wearing a third name; the atlas's "sub-component" language is enforced literally.

## Part E — The algorithm (routing, weekly)

```
STEP 1  weekly: WSS CP outstanding/issuance -> rollover ratio; FBIL/bulletin spread leg
STEP 2  freeze legs -> expanding z's (shared grids); publish {spread_z, rollover_z, n_legs}
STEP 3  routing: EITHER leg beyond its registered extreme -> L2 stress-family input (fast,
        reduce-only consequences per L2's own rules); NEVER a standalone portfolio action
STEP 4  composition consumption unchanged in L10 (cross-ref credit-deep; no action here)
STEP 5  playbook layer (descriptive, Stage-2): the 2018-19 sector-rotation record as a
        briefing document when the index arms — reduce-only framing, no automatic trades
MONITOR AMFI category flows monthly (holder-side confirm); FSR NBFC chapter half-yearly
        (slow structure); regulatory-cycle watch (scale-based list, FLDG, co-lending,
        risk-weight moves) as breaks-registry entries — each move RELOCATES the fragile node
FAILURE MODES: WSS reformats (registry); FBIL access; the next crunch's node NOT being
        CP-funded NBFCs at all (the arbitrage lesson) -> the regulatory watch exists so the
        index's coverage question is re-asked annually, in writing
```

## Part F — Harvest map + designs

| Consumer | What it gets |
|---|---|
| L2 fast stress | the freeze index (spread_z, rollover_z) as input candidates under L2's budget |
| L10 credit block | nothing new (composition already seated — the de-dup is the deliverable) |
| Stage-2 briefings | the crunch playbook (2018-19 rotation record, descriptive) |
| Sentinel | regulatory-cycle watch entries; AMFI flow confirms |
| Cycle School | Lesson 17: a run without deposits; why detection horizon is everything |

Designs: **SC2** (registered in the ledger, bars deferred to the data per the two-pass rule):
freeze index vs L2's stress dates — acceptance registered at runsheet step 51 BEFORE any
backtest look. **SC3** (holder-side): AMFI liquid/credit-risk category flow z's as a freeze
CONFIRM (design only; acceptance registered with SC2). No equity-factor design exists — SC1
killed that family and it stays dead.

## Part H — Knowledge ledger (atlas 2.2)

**Established (our run):** the 2018 freeze reached BROAD equities within 12m (SC1's honest
fail — SMB 18th pct, market 16th) — the measured case for funding-variable detection.
**Established (record):** India has run the full shadow cycle at least twice (1990s deposit
NBFCs; 2018-20 CP-funded NBFC/HFCs) with the fragile node MOVING between runs — the
regulatory-arbitrage mechanism in the wild. **India [n=1 clean modern cycle]:** 2014→2018→2020
is one observed boom-freeze-resolution arc; every quantitative claim inherits that n.
**Unknowable:** the next fragile node's address (co-lending? FLDG-backed digital books? MFI?)
— the watch list is a question re-asked annually, never an answer assumed. **Process:** the
entry ships with ZERO new seats and ZERO new budget — its deliverable is inputs, routing, and
the de-dup proof; the ledger records one dead family (equity-factor detection) with its
failing print attached.
