# Reachability probe — raw output

Run 2026-09-11 from the remote/web session. Column 2 = HTTP status, column 3 = bytes downloaded.
Status 000 with curl error 56 = "CONNECT tunnel failed, response 403"; the agent proxy reports
kind=connect_rejected, detail="gateway answered 403 to CONNECT (policy denial or upstream failure)".

```
github-raw(control)                200 1144         https://raw.githubusercontent.com/anthropics/anthropic-sdk-python/main/README.md
UK-HMLR-pricepaid                  000 0            http://prod.publicdata.landregistry.gov.uk/pp-monthly-update-new-version.csv
UK-HMLR-sparql                     000 0            https://landregistry.data.gov.uk/
IE-PPR                             000 0            https://www.propertypriceregister.ie/
US-FHFA-hpi                        000 0            https://www.fhfa.gov/hpi
US-Zillow-research                 000 0            https://files.zillowstatic.com/research/public_csvs/zhvi/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv
US-FRED                            000 0            https://fred.stlouisfed.org/graph/fredgraph.csv?id=CSUSHPINSA
US-census-bps                      000 0            https://www.census.gov/construction/bps/
BIS-stats                          000 0            https://data.bis.org/
DallasFed-intl-hp                  000 0            https://www.dallasfed.org/research/international/houseprice
OECD-sdmx                          000 0            https://sdmx.oecd.org/public/rest/dataflow/OECD.ECO.MPD
IMF-data                           000 0            https://www.imf.org/en/Research/housing-market-stability
JP-MLIT-lib                        000 0            https://www.reinfolib.mlit.go.jp/
KR-data.go.kr                      000 0            https://www.data.go.kr/
SG-data.gov.sg                     000 0            https://data.gov.sg/
SG-URA-api                         000 0            https://www.ura.gov.sg/maps/api/
NL-kadaster                        000 0            https://www.kadaster.nl/
PL-NBP-barn                        000 0            https://nbp.pl/en/statistic-and-financial-reporting/real-estate-market/
IN-data.gov.in                     000 0            https://www.data.gov.in/
IN-RBI-dbie                        000 0            https://data.rbi.org.in/
IN-RBI-main                        000 0            https://www.rbi.org.in/
IN-NHB-residex                     000 0            https://residex.nhbonline.org.in/
IN-IGR-maharashtra                 000 0            https://igrmaharashtra.gov.in/
IN-NGDRS                           000 0            https://ngdrs.gov.in/
IN-DILRMP-dashboard                000 0            https://dilrmp.gov.in/
IN-MahaRERA                        000 0            https://maharera.maharashtra.gov.in/
IN-bhuvan                          000 0            https://bhuvan.nrsc.gov.in/
IN-mospi                           000 0            https://www.mospi.gov.in/
JRC-GHSL                           000 0            https://human-settlement.emergency.copernicus.eu/
OSM-overpass                       000 0            https://overpass-api.de/api/status
OSM-geofabrik-india                000 0            https://download.geofabrik.de/asia/india.html
Google-open-buildings              000 0            https://sites.research.google/gr/open-buildings/
WorldPop                           000 0            https://hub.worldpop.org/
NOAA-VIIRS-eog                     000 0            https://eogdata.mines.edu/products/vnl/
magicbricks-propindex              000 0            https://www.magicbricks.com/
housing-datalabs                   000 0            https://housing.com/news/data-labs/
knightfrank-in                     000 0            https://www.knightfrank.co.in/research
```
