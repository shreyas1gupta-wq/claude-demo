## §5 — REACHABILITY, MEASURED RATHER THAN ASSUMED

**This section is the only part of §§1-5 that is a measurement rather than a literature claim, and
it is the most operationally important thing in the pack.** On 2026-09-11 the desk probed 37
candidate endpoints directly from the remote/web session with `curl` — every major international
house-price source, every Indian official portal, and the free geospatial stack.

**Result: 36 of 37 blocked. The only endpoint that answered was the GitHub control.**

| Class | Probed | Reachable |
|---|---|---|
| GitHub raw (control) | 1 | **1** |
| International official (BIS, Dallas Fed, OECD, IMF, FHFA, FRED, US Census, HM Land Registry, Ireland PPR, Kadaster, NBP, MLIT Japan, data.go.kr, data.gov.sg, URA) | 15 | 0 |
| India official (data.gov.in, RBI DBIE, RBI main, NHB RESIDEX, IGR Maharashtra, NGDRS, DILRMP, MahaRERA, Bhuvan, MoSPI) | 10 | 0 |
| Geospatial / free bulk (JRC GHSL, Overpass, Geofabrik, Google Open Buildings, WorldPop, NOAA VIIRS) | 6 | 0 |
| Private India (Magicbricks, Housing.com, Knight Frank India) | 3 | 0 |
| US private bulk (Zillow research CSVs) | 1 | 0 |

The failure mode is identical in every case and it is not a site problem: `curl` error 56,
*CONNECT tunnel failed, response 403*, and the agent proxy's own log records
`kind: connect_rejected`, `detail: "gateway answered 403 to CONNECT (policy denial or upstream
failure)"`. It is a network-policy denial at the gateway, not a robots rule, not a rate limit, and
not something a different user agent or a retry will fix. Raw output and the probe script are in
`research/notes/re-engine-sources/_PROBE.md` and `_PROBE.sh` — re-run it on the desktop machine and
the same table becomes an acquisition plan.

**Three consequences, all binding.**

1. **The venue decision in the handoff prompt (§0.5) is now measured, not inferred.** Acquisition
   must run on the principal's own machine. A web session cannot pull one row of any source this
   project needs — not even the free, open, no-login ones like HM Land Registry Price Paid or the
   JRC built-up surface rasters.
2. **GitHub is the one live channel, so GitHub-hosted mirrors are the only data this environment can
   ever land.** That is exactly how the desk's existing ten vaults were built. Worth a dedicated
   hunt: several of the international series in §2 are mirrored in academic and replication
   repositories, and the JST panel — already vaulted here — is one of them.
3. **Everything in §§1-4 of this pack is snippet-grade for a structural reason, not a stylistic
   one.** No agent could open a primary page. Treat the pack as a map of where the evidence lives,
   then verify on the machine that can actually reach it. The `[RECALL — unverified]` tags are the
   honest edge of what was possible here.

