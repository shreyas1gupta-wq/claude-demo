# Part C — Data engineering: the stance variables, free (atlas 2.6; compact, in-house)

*v1.0 · 2026-09-02 · desk principal's chapter. The entry's data surface is narrow and entirely
RBI-published; the engineering problem is SPLICING and the effective-rate question, not access.*

## C.1 The policy-rate path
RBI DBIE: repo rate (operating target since the mid-2000s), reverse repo, MSF (2011-), SDF
(Apr 2022-), Bank Rate (the pre-LAF era's rate), CRR. All step functions with exact change
dates from MPC resolutions/press releases (public, permanent). THE ENGINEERING TRAP: the
EFFECTIVE operating rate migrates — Bank Rate era → repo era → reverse-repo-as-floor era
(2020-22 surplus liquidity: the floor WAS the rate) → SDF era. The desk's series is a
constructed **effective_rate** with regime tags and a breaks-registry entry per migration;
never a naive repo splice. [VERIFY each migration date on pull.]

## C.2 The liquidity leg — the stance banks actually feel
RBI WSS: net LAF position (daily/weekly), the surplus/deficit sign and size (% of NDTL). In
surplus regimes cuts transmit fast and hikes slowly; in deficit regimes the reverse — stance =
(effective real rate, liquidity sign) as a PAIR. Money-market spread cross-check: weighted call
rate minus repo (DBIE daily) — the corridor-position variable.

## C.3 Transmission observables
RBI bulletin monthly: WALR on fresh rupee loans (the transmission endpoint, 2011-), WADTDR
(deposits), 1y median MCLR (2016-), share of EBLR-linked loans (semiannual FSR table). These
are the MP-D1 replication legs. Breaks: BPLR→Base(2010-07)→MCLR(2016-04)→EBLR(2019-10) — four
lending-rate REGIMES; series never spliced across them without regime dummies (registry).

## C.4 Inflation legs for the real-rate read
CPI combined (2012-) for the MPC era; WPI for history before it — the real-rate series carries
a declared deflator break at the 2014-15 CPI adoption (registry; both variants published).

## C.5 PIT hazards
| Hazard | Rule |
|---|---|
| Effective-rate migrations (C.1) | regime tags + breaks registry; both variants retained |
| Lending-rate regime changes | never spliced silently (C.3) |
| MPC minutes revisions | resolutions are final; minutes lag 14 days — stance reads use resolution dates only |
| Liquidity denominators (NDTL revisions) | fortnightly vintage kept |

## C.6 Runsheet addendum 9 (steps 52-56)
52. DBIE policy-rate suite backfill + effective_rate construction with regime tags ~3-4h
53. WSS net-LAF backfill (weekly, 2000s→) + call-rate spread ~3-4h
54. Bulletin WALR/WADTDR/MCLR monthly transcription (2011→) ~4-5h
55. MP-D1 acceptance registration (repo→WALR→credit chain, BEFORE the look) ~2h
56. L6 stance classifier run + first India lagged-regime series, sentinel wiring ~3-4h
Total ~15-19h.
