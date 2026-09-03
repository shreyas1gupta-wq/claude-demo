# THE RUNSHEET — every data pull the register is waiting on
Consolidated 2026-09-02 at atlas completion. Each pull is FREE (Contract §3), lands in
ingest/vault/ under manifest + two-pass AUTHENTICATION discipline, and unblocks designs whose
bars/priors are ALREADY WRITTEN in research/register/trial-ledger.md — no design decisions
remain at pull time; the machine runs as registered. Pulls happen on the principal's machine
(this remote environment's egress is GitHub-only; see the per-entry data-engineering Parts C
for exact URLs, formats, and pitfalls).

## Priority 1 — unblocks the most machinery
| Pull | Free source | Vault destination | Unblocks |
|---|---|---|---|
| Daily bhavcopy, NIFTY-750 point-in-time (equities + indices, with membership history) | NSE/BSE archives | ingest/vault/bhavcopy/ | Phase-0 fixtures; F1-F7 (fast stress on the real episode set); MR1; CR-D1/D2/D3 (comomentum); RC1 prices; H58-D2/D3 counting; CW2 daily verification; the price-only factor book (Contract §7.7). **PARTIALLY MIRRORED 2026-09-02** (remote leg): NIFTY 50 index daily 2007-2026 (ingest/vault/index/, 6/6 anchors) ran CW-D1a/DW1/F1a/F2a; NIFTY500 SURVIVOR panel 2012-2021 (ingest/vault/panel/, misses recorded) ran MR1-S (freeze corroborated) + CR-D2a. The PIT pull remains required — mirrors cannot discharge MR1/CR-D2/F2 proper |
| India VIX daily archive (2009-) + option-chain IV snapshots | NSE archive — puller: ingest/pull_india_vix.py (auth skeleton via --emit-auth-template) | ingest/vault/vix/ | CW-D1 (budget-day vol); F5 (IV vs RV); FS-D1 (term structure); VRP designs. NOTE 2026-09-02: CBOE VIX mirror vaulted (ingest/vault/globalvol/) as the GLOBAL series — FS-D3 refused it as a symmetric L2 leg (dilution), FS-D4 arm-only variant registered. **PARTIALLY MIRRORED 2026-09-03**: India VIX daily 2010-07..2023-04 (TradingView export, 6/6 anchors incl. exact COVID peak 83.6075) ran CW-D1v (PASS 2.7e-06 — CW-D1 discharged at mirror coverage) + F5a (RV stays primary). Still owed from the NSE primary: the 2009 head, post-Apr-2023 tail (2024 election spike), and option-chain IV for FS-D1/VRP |
| CCIL rates: TREPS/call/CP + RBI LAF daily position | CCIL publications, RBI DBIE/WSS — puller: ingest/pull_ccil.py (auth skeleton via --emit-auth-template) | ingest/vault/funding/ | H58-D1 (drain quarantine grading); FS-D2 (order-of-arrival); L2 funding leg calibration |

## Priority 2 — seat calibrations and candidate promotions
| Pull | Free source | Vault destination | Unblocks |
|---|---|---|---|
| NSDL FPI daily/monthly flows + assets under custody | NSDL FPI monitor | ingest/vault/flows/ | FL1/FL2 (L14 calibration); FS-D2 funding leg |
| NSE/BSE primary-market data: listings, issue sizes, first-day closes | exchange archives, SEBI bulletins | ingest/vault/issuance/ | IS1/IS2 (L7 calibration) |
| NSDL/CDSL demat account counts + SEBI retail F&O turnover shares | monthly bulletins | ingest/vault/participation/ | RT1/RT2 (H57) |
| China TSF (aggregate financing) monthly | PBoC releases / BIS mirrors | ingest/vault/china/ | CN-D1/D2/D3 (H54 promote-or-kill) |
| NOAA ONI (post-2010 continuation) + IMD % of LPA seasonal | NOAA/IMD bulletins | ingest/vault/climate/ | EN-D1/D2 (H55 chain-conditioner) |
| Kilian / Baumeister-Hamilton oil decomposition indexes | authors' pages (free) | ingest/vault/commodities/ | OL-D1/D2 (the decomposition commitment). **PARTIALLY MIRRORED 2026-09-03**: Kilian index 1973-2019 (replication mirror, 5/5 anchors) ran OL-D1a (PASS +46pp, prior confirmed); Känzig supply-news shocks 1975-2025 vaulted from the author's own repo (4/4 anchors). Still owed: the BH decomposition proper + post-2019 Kilian months |

## Priority 3 — narrow designs
| Pull | Free source | Vault destination | Unblocks |
|---|---|---|---|
| NSE Indices reconstitution announcements (add/drop lists, semi-annual) | NSE Indices press releases | ingest/vault/index-events/ | RC1 (with bhavcopy prices) |
| Exchange results calendars (announcement dates per holding) | NSE/BSE corporate announcements | ingest/vault/calendars/ | H58-D2 counting |
| WSTS Blue Book (monthly billings 1976-) | wsts.org free download (blocked at this proxy; free in principle — see research/cycles/semis-candidate/DATA-PROBE.md) | ingest/vault/semis/ | H59-D1 (prior: fails) |

## Principal inputs (not pulls — decisions; validator warns on every run until set)
- `funding_rate` (config) — gates the leverage feature entirely.
- ADV/capacity table — PROVISIONAL placeholder inherited by every capacity number.

## Standing rules at pull time
Two-pass authentication (bars written before results, per near-miss #4); manifest before
analysis (WORM); no design may be altered at data-landing — bars run as registered, and a
bar that proves wrong is a recorded miss, never a moved bar (M0/A6 precedent). Paid or
login-gated sources are NOT substitutes for any row above (3.5's REJECT-FOR-DATA precedent
governs).
