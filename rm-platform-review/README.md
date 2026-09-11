# RM Platform Review — Aug-31 2026

`Ionic_RM_Platform_Review_Aug31.html` is a self-contained dashboard: 14
market-leader desks, one card per RM, plus a **Data QC** tab carrying the
reconciliation. Open the file directly in a browser — no server needed.

Rebuilt from `HNI_Team_Intelligence_31Aug2026_MIS_FINAL_v7_FIXED.xlsx`,
replacing the prior version which was reconciled against a different source
(`PLATFORM AND FOCUS PRODUCTS DASHBOARD_1367.xlsm`).

| Measure | Prior dashboard | Aug-31 MIS |
|---|---:|---:|
| Total book | ₹3,773.60Cr | **₹3,825.22Cr** |
| Platform (core-4) | ₹497.67Cr | **₹528.46Cr** |
| Penetration | 13.19% | **13.82%** |
| Client accounts | 2,290 | **2,338** (1,748 households) |
| Platform clients | 478 (458 live) | **523** (498 live) |
| Focus | ₹6.90Cr | **₹7.05Cr** |
| RMs / desks | 72 / 13 | **73 / 14** |

## Rebuilding

```bash
python3 rm-platform-review/build/build_dashboard.py            # verify, then write
python3 rm-platform-review/build/build_dashboard.py --verify   # checks only
python3 rm-platform-review/build/build_dashboard.py --sample 40
```

Standard library only — this environment has no openpyxl or pandas, and the
build deliberately adds no dependency (`build/xlsx_reader.py` reads the
workbook out of its zip container).

The build **aborts and writes nothing if any check fails**, so a dashboard that
exists is a dashboard that ties. Current state: **379/379 checks pass.**

### Source files

`source/` is gitignored — the workbook holds client-level names and AUM. Put
these two files there before building:

- `HNI_Team_Intelligence_31Aug2026_MIS_FINAL_v7_FIXED.xlsx`
- `prior_dashboard_FINAL_1_1.html` (needed for the focus carry-forward and the
  movement-vs-prior table)

## Dropping in RM-wise focus

The Aug-31 MIS reports focus (SHASTRA + Bond + Edel) **only at 8-team level**
(firm ₹7.05Cr), so there is no per-RM source in it. Until the RM-wise split
arrives the cards show the prior cycle's per-RM focus, tagged `prior cycle`,
and each desk's unaccounted balance is shown as *not attributable to an
individual RM* rather than spread on a guess. Those carried figures reconcile
exactly to 6 of the 8 new team totals; only ₹0.05Cr (Dhiren Shah + Ajay Sehgal)
and ₹0.10Cr (Abhishek Kumar) are unattributed.

To switch to real per-RM figures, write `data/focus_rm.csv` and rebuild:

```csv
rm,f_mar,f_aug,f_cl,cl_focplat
Pratyaksha Gupta,0,0.79,1,1
Hemansh Kothari,0,0.83,1,1
```

The build picks the file up automatically, drops the `prior cycle` tag, and
recomputes each desk's residual against the MIS team total — so if the supplied
figures account for a team in full, the unattributed note disappears by itself.

## Checks

Three suites, all run before anything is written. `qc/reconciliation.md` is the
written report; the same content is in the dashboard's **Data QC** tab.

- **cross-check (104)** — every total asserted against a figure recomputed
  row-by-row from the raw `aum` / `platform` sheets, never against a workbook
  summary row. Includes exhaustive per-RM equality on AUM, clients, the 50L
  split, platform, platform clients and all four product values plus their
  client counts, for **all 73 RMs**.
- **random-check (20)** — a seeded sample (seed 20260831) re-derived field by
  field and printed as an auditable table.
- **calc-check (255)** — every percentage and delta the page renders,
  recomputed and compared; plus flag-logic and NaN/negative guards.

The suites are fault-tested: injecting a wrong RM AUM, a shifted product value,
a compensating swap across the 50L line, a wrong product client count, an RM on
the wrong desk, a stale platform figure or the stale ₹524.14Cr product mix is
each caught by name.

## Source blocks deliberately not used

`sources.py:STALE_BLOCKS` is the register, with the wrong figure each block
would have injected. The significant ones:

| Block | Would have injected | Actual |
|---|---|---|
| `Team Summary` NEW-A cols H:I | ₹3,509.09Cr / 2,135 clients | ₹3,825.22Cr / 2,338 |
| `Team Summary` row 49 (NEW-B total) | ₹422.40Cr platform | ₹528.46Cr |
| `Platform Charts (RM)` K24:L27 | mix summing to ₹524.14Cr | ₹528.46Cr |
| `Platform Charts (RM)` col C | ₹3,825.60Cr (rounded per RM) | ₹3,825.2247Cr |
| team sheets Section J | a Jul-15 cutoff, VK at ₹744.07Cr | VK ₹822.11Cr |

Also worth knowing, found while auditing `Platform Charts (RM)`:

- **Col H is sound** — live `SUMIFS`, ₹528.46Cr, zero mismatches across 73 RMs,
  and it correctly includes the 39 `RECON-*` rows (₹16.28Cr across 15 RMs) that
  lift CLIENT LEVEL up to the authoritative RM LEVEL basis. Cols F and G tie to
  `MoM Trend` Mar-26 and Jun-26 exactly. These three are the platform source.
- **Col I is live only on row 5.** `Validation & Exceptions` item 25 states
  rows 5:77 are all live; they are not. The cached values are currently right
  but will go stale on the next refresh.
- **Col E has one error** — Devyani Dhuri reads 0.15 where C/D is 0.17.
- The `READ ME` sheet's **1,765 households** is wrong (live count 1,748). Its
  **819 clients ≥₹1Cr** is *not* wrong — that is the account basis, while
  `Team Summary`'s 743 is the household basis. The dashboard shows both and
  labels which is which.

## Definitions

- **Platform** = core-4 on the net-funding basis (Allocate, High Yield
  Enhancer, Navigate, Co-Pilot). Sharpe One and PIPE (₹72.93Cr) are outside it;
  all platform products together are ₹601.39Cr.
- **Platform clients** = distinct clients with a core-4 account, including
  positions valued at zero today (498 of the 523 carry live value).
- **New Jun→Aug** = client ids on the book at Aug-31 but not at Jun-30.
- **Above ₹50L** is inclusive. Per-RM client counts are on the account basis,
  matching the prior dashboard; households are shown at firm level.
- Mar/Jun books follow the RM name, so an RM who changed desks carries their
  prior book.

## Structure

```
Ionic_RM_Platform_Review_Aug31.html   the deliverable, self-contained
build/
  build_dashboard.py   entry point: extract -> assemble -> verify -> write
  xlsx_reader.py       stdlib .xlsx reader (values and formula text)
  sources.py           provenance: stale-block register, ML resolutions, products
  extract.py           pulls figures from the workbook
  assemble.py          builds the DATA structure; focus carry-forward / drop-in
  verify.py            the three check suites
  render.py            assembles the HTML; writes the QC report
  app.js               render layer (charts, cards, QC tab)
  base.css             design tokens carried from the prior dashboard
  chart.css            chart and QC additions
data/DATA.json         the built dataset
qc/reconciliation.md   the written reconciliation
```

### A note on the chart palette

The prior mix colours (`#242BA1 / #FFB951 / #7BA0FF / #157A3D`) fail the
categorical lightness band — the indigo is too dark (L 0.377) and the amber too
light (L 0.833). They are snapped to `#445AD1 / #E39F31 / #8FAFFD / #06642F`,
which keeps each brand hue angle and passes the lightness band, chroma floor,
CVD separation (worst all-pairs ΔE 24.5) and normal-vision floor. Two slots sit
below 3:1 on white, which is discharged as the method requires: every mix
segment is direct-labelled and the QC tab carries the full table. Allocate and
Navigate are the *same* brand hue (271° and 267°), so no palette can separate
them under CVD and also clear 3:1 — hence the labels are load-bearing, not
decoration. The page is light-only, as the prior one was.
