# AUTHENTICATION — factors_us (FF5/FF6/Q5 monthly)
Source: GitHub mirror `JustinMShea/ExpectedReturns` (R package companion to Ilmanen's
Expected Returns; shallow clone 2026-09-08), files FF5.monthly.RData, FF6.monthly.RData
(sandbox/), Q5.monthly.RData — parsed with the pure-python `vnmabus/rdata` reader
(xts dimnames/index dropped by the zoo fallback: column names and date index assigned
PROVISIONALLY below and verified in PASS 2). MIRROR RANKING NOTE: primary hosts (Ken
French library, global-q.org) are egress-dead from this environment; this mirror never
outranks a primary pull — runsheet rows for the primaries stand.

## PASS 1 — anchors (written and committed BEFORE any value check; near-miss #4 rule)
A1 ff5_monthly: shape 684x6, decimals, provisional columns [RF, MktRF, SMB, HML, RMW,
   CMA], provisional index monthly 1963-07..2020-06.
A2 ff6_monthly: shape 682x7, same provisional layout + UMD, 1963-07..2020-04.
A3 q5_monthly: shape 636x6, decimals, provisional [R_F, R_MKT, R_ME, R_IA, R_ROE, R_EG]
   (HXZ q5 ordering), provisional index 1967-01..2019-12.
A4 VALUE ANCHORS to check in pass 2 (from the ALREADY-VAULTED primaries, never memory):
   (i) ff5.MktRF, SMB, HML, RF must each correlate >= 0.99 with the same-named columns
   of ingest/vault/factors/fff_monthly_us.csv (/100) on the 1963-07..2020-04 overlap,
   and mean absolute difference < 5bp/mo;
   (ii) ff6.UMD must correlate >= 0.99 with ingest/vault/factors/ff_momentum_monthly.csv
   on the overlap;
   (iii) q5.R_MKT must correlate >= 0.98 with fff Mkt-RF on 1967-01..2019-12;
   (iv) q5 1967-01 R_MKT in [+0.07, +0.09] (the known strong Jan-1967 market month);
   (v) if any check fails, the provisional column mapping is WRONG and must be
   re-derived by correlation matching before any research use — recorded either way.
