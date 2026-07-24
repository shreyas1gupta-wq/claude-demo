#!/usr/bin/env python3
"""Build the AZBY template dataset (dummy but internally consistent) from the
NIFTY-750 scorecard. Outputs template/azby_data.json for the chart and deck
generators. AZBY Family is fictional; all holdings are illustrative."""
import json, openpyxl
from pathlib import Path

SCORECARD = Path(__file__).resolve().parent.parent / "scratch_review" / "scorecard.xlsx"
OUT = Path(__file__).resolve().parent / "azby_data.json"

# ---- load scorecard -------------------------------------------------------
wb = openpyxl.load_workbook(SCORECARD, read_only=True, data_only=True)
ws = wb["All Scores (750)"]
COLS = ["Symbol","Sector","Call","S3Y","S1Y","R3Y","R1Y","Quality","G3Y","G1Y",
        "Value","St3Y","St1Y","Macro","C3Y","C1Y","RevG","ROE","ROCE","PE","DE",
        "BSGate","GrwSrc","Qtr","Stale","ZeroCov","MktCap"]
SC = {r[0]: dict(zip(COLS, r)) for r in ws.iter_rows(min_row=5, values_only=True) if r[0]}
num = lambda x: x if isinstance(x, (int, float)) else None

# ---- MUTUAL FUNDS (21 schemes; illustrative) ------------------------------
FUND_TARGET_L = 232.0
FUNDS = [
 ("HSBC Small Cap","HSBC","Small Cap","Direct",78.0,True, 6.2,108,96,58,55),
 ("Parag Parikh Flexi Cap","PPFAS","Flexi Cap","Direct",41.0,True, 4.8,104,84,74,71),
 ("Franklin Build India","Franklin","Thematic-Infra","Direct",30.0,False,None,None,None,None,None),
 ("Nippon India Multi Cap","Nippon","Multi Cap","Direct",22.5,True, 9.4,112,101,63,60),
 ("ICICI Pru Multi Asset","ICICI Prudential","Hybrid-Multi Asset","Direct",19.0,True,None,None,None,None,None),
 ("Tata Arbitrage","Tata","Hybrid-Arbitrage","Direct",16.5,True,None,None,None,None,None),
 ("Motilal Oswal Midcap","Motilal Oswal","Mid Cap","Direct",14.0,True, 13.5,118,99,66,62),
 ("Franklin Asian Equity","Franklin","International","Direct",13.0,False,None,None,None,None,None),
 ("HDFC Balanced Advantage","HDFC","Hybrid-BAF","Direct",12.5,True,None,None,None,None,None),
 ("Invesco Global Consumer","Invesco","International","Direct",9.8,False,None,None,None,None,None),
 ("Edelweiss US Tech FoF","Edelweiss","International","Direct",8.5,False,None,None,None,None,None),
 ("Kotak Equity Savings","Kotak","Hybrid-Equity Savings","Direct",7.0,True,None,None,None,None,None),
 ("SBI ELSS Tax Saver","SBI","ELSS","Direct",6.0,True, 2.1,101,97,54,52),
 ("Nippon India Gold Savings","Nippon","Commodity-Gold FoF","Direct",5.5,False,None,None,None,None,None),
 ("JM Flexicap","JM","Flexi Cap","Direct",5.5,True, 13.1,115,92,72,69),
 ("Motilal Nifty500 Momentum 50","Motilal Oswal","Index-Factor Momentum","Direct",4.2,False,None,None,None,None,None),
 ("UTI Nifty500 Value 50","UTI","Index-Factor Value","Direct",3.8,False,None,None,None,None,None),
 ("Bandhan Small Cap","Bandhan","Small Cap","Direct",3.4,True, 8.0,106,103,57,54),
 ("Motilal BSE Enhanced Value","Motilal Oswal","Index-Factor Value","Direct",2.6,False,None,None,None,None,None),
 ("ICICI Pru Multi Asset (Reg)","ICICI Prudential","Hybrid-Multi Asset","Regular",2.2,True,None,None,None,None,None),
 ("UTI Nifty200 Momentum 30","UTI","Index-Factor Momentum","Direct",2.0,False,None,None,None,None,None),
]
HYB = {"Tata Arbitrage": (1.9,3.1,-0.6,3.4), "ICICI Pru Multi Asset": (1.42,2.05,-9.8,2.1),
       "ICICI Pru Multi Asset (Reg)": (1.38,1.98,-9.8,1.6), "HDFC Balanced Advantage": (1.18,1.62,-12.4,-1.8),
       "Kotak Equity Savings": (1.31,1.9,-6.2,1.2)}
# ---- HNI AZBY equity book: 76 real NIFTY-750 names ------------------------
NAMES = [
 ("TITAN","Titan Company"),("RELIANCE","Reliance Industries"),("TCS","Tata Consultancy Svcs"),
 ("ICICIBANK","ICICI Bank"),("INFY","Infosys"),("HDFCBANK","HDFC Bank"),("BHARTIARTL","Bharti Airtel"),
 ("SBIN","State Bank of India"),("BAJFINANCE","Bajaj Finance"),("LT","Larsen & Toubro"),
 ("ITC","ITC"),("HINDUNILVR","Hindustan Unilever"),("KOTAKBANK","Kotak Mahindra Bank"),
 ("AXISBANK","Axis Bank"),("MARUTI","Maruti Suzuki"),("SUNPHARMA","Sun Pharma"),
 ("ULTRACEMCO","UltraTech Cement"),("ASIANPAINT","Asian Paints"),("NESTLEIND","Nestle India"),
 ("HAL","Hindustan Aeronautics"),("BEL","Bharat Electronics"),("ADANIENT","Adani Enterprises"),
 ("DMART","Avenue Supermarts"),("WIPRO","Wipro"),("NTPC","NTPC"),("PIDILITIND","Pidilite Inds"),
 ("HINDALCO","Hindalco Industries"),("TATAPOWER","Tata Power"),("GAIL","GAIL India"),
 ("TECHM","Tech Mahindra"),("HCLTECH","HCL Technologies"),("BAJAJ-AUTO","Bajaj Auto"),
 ("HEROMOTOCO","Hero MotoCorp"),("CIPLA","Cipla"),("POWERGRID","Power Grid Corp"),
 ("GODREJCP","Godrej Consumer"),("DABUR","Dabur India"),("COFORGE","Coforge"),
 ("PERSISTENT","Persistent Systems"),("POLYCAB","Polycab India"),("SIEMENS","Siemens"),
 ("PFC","Power Finance Corp"),("RECLTD","REC"),("MOTHERSON","Samvardhana Motherson"),
 ("FEDERALBNK","Federal Bank"),("CDSL","Central Depository Svcs"),("BSE","BSE"),
 ("CAMS","Computer Age Mgmt"),("MFSL","Max Financial Svcs"),("LICHSGFIN","LIC Housing Finance"),
 ("TATACONSUM","Tata Consumer"),("MARICO","Marico"),("UNITDSPR","United Spirits"),
 ("COLPAL","Colgate-Palmolive"),("BRITANNIA","Britannia Industries"),("ATUL","Atul"),
 ("DEEPAKNTR","Deepak Nitrite"),("SRF","SRF"),("BALRAMCHIN","Balrampur Chini"),
 ("EXIDEIND","Exide Industries"),("BHARATFORG","Bharat Forge"),("SUZLON","Suzlon Energy"),
 ("KAYNES","Kaynes Technology"),("JUBLFOOD","Jubilant Foodworks"),("NAUKRI","Info Edge"),
 ("SWIGGY","Swiggy"),("JIOFIN","Jio Financial"),("VBL","Varun Beverages"),
 ("TRENT","Trent"),("MPHASIS","Mphasis"),("IRCTC","IRCTC"),
 ("BLUEDART","Blue Dart Express"),("SUPRIYA","Supriya Lifescience"),("SYNGENE","Syngene Intl"),
 ("LUPIN","Lupin"),("VIPIND","VIP Industries"),
]
missing = [s for s, _ in NAMES if s not in SC]
if missing:
    raise SystemExit("MISSING SYMBOLS: " + ", ".join(missing))

# Fixed book; every weight assigned explicitly as %-of-book (clustered head over a
# geometric satellite tail), so head names always stay on top and the split is exact.
BOOK_L = 534.0
HEAD_BOOK_PCT = [6.3, 5.6, 4.3, 3.8, 3.3, 2.6, 2.2, 1.9, 1.7, 1.5]     # names 1-10
n_tail = len(NAMES) - len(HEAD_BOOK_PCT)
tail_start, tail_ratio = 1.10, 0.955                                   # names 11-76
tail_pct = [tail_start * tail_ratio ** i for i in range(n_tail)]
book_pct = HEAD_BOOK_PCT + tail_pct
vals = [p / 100 * BOOK_L for p in book_pct]
equity_val = round(sum(vals), 1)
book_l, book_cr = BOOK_L, round(BOOK_L / 100, 2)

# size the fund book to the remaining share of the fixed book
fund_target_l = round(BOOK_L - equity_val, 1)
raw_fund_sum = sum(f[4] for f in FUNDS)
fscale = fund_target_l / raw_fund_sum
funds = []
for nm, house, cat, plan, aum, seasoned, alpha, ucr, dcr, r3, r1 in FUNDS:
    rec = dict(name=nm, house=house, category=cat, plan=plan,
               aum_l=round(aum * fscale, 1), seasoned=seasoned, alpha=alpha,
               ucr=ucr, dcr=dcr, roll3=r3, roll1=r1)
    if nm in HYB:
        sh, so, dd, w1 = HYB[nm]; rec.update(sharpe=sh, sortino=so, maxdd=dd, worst1y=w1)
    funds.append(rec)
fund_val = round(sum(f["aum_l"] for f in funds), 1)

def cap_band(mc):
    if mc is None: return "Unmapped"
    if mc >= 70000: return "Large"
    if mc >= 14000: return "Mid"
    return "Small"

def composite(d):
    a, b = num(d["S3Y"]), num(d["S1Y"])
    if a is None and b is None: return None
    if a is None: return round(b)
    if b is None: return round(a)
    return round(0.6 * a + 0.4 * b)

REASON = [("st1","weak price trend"),("quality","quality below peers"),
          ("g1","soft recent growth"),("g3","slowing growth"),
          ("macro","sector headwind"),("value","stretched valuation")]
def reason_for(p):
    sc = sorted([(p[k], t) for k, t in REASON if p.get(k) is not None])
    return "; ".join(t for _, t in sc[:2])

stocks = []
for (sym, name), v in zip(NAMES, vals):
    d = SC[sym]
    p = dict(quality=num(d["Quality"]), g3=num(d["G3Y"]), g1=num(d["G1Y"]),
             value=num(d["Value"]), st3=num(d["St3Y"]), st1=num(d["St1Y"]),
             macro=num(d["Macro"]), roe=num(d["ROE"]), pe=num(d["PE"]), mktcap=num(d["MktCap"]))
    comp = composite(d)
    call = "Sell" if (comp is not None and comp < 40) else "Hold"
    stocks.append(dict(symbol=sym, name=name, sector=d["Sector"],
        weight=round(v / book_l * 100, 3), value_l=round(v, 1), score=comp,
        call=call, cap=cap_band(p["mktcap"]), reason=reason_for(p), **p))

eq_val = round(sum(s["value_l"] for s in stocks), 1)
by_w = sorted(stocks, key=lambda s: s["weight"], reverse=True)
sleeve_w = lambda s: s["value_l"] / eq_val * 100
top5 = round(sum(s["weight"] for s in by_w[:5]), 1)
top10 = round(sum(s["weight"] for s in by_w[:10]), 1)
sells = sorted([s for s in stocks if s["call"] == "Sell"], key=lambda s: -s["weight"])
sell_wt = round(sum(s["weight"] for s in sells), 1)

def agg(key):
    m = {}
    for s in stocks:
        m[s[key]] = m.get(s[key], 0) + s["value_l"]
    return {k: round(v / eq_val * 100, 1) for k, v in sorted(m.items(), key=lambda kv: -kv[1])}
sectors, caps = agg("sector"), agg("cap")

bins = [0] * 10
for s in stocks:
    if s["score"] is not None:
        bins[min(9, s["score"] // 10)] += 1
below40 = sum(1 for s in stocks if s["score"] is not None and s["score"] < 40)
watch = sorted([s for s in stocks if s["call"] == "Hold" and s["score"] is not None
                and 40 <= s["score"] <= 47], key=lambda s: s["score"])

def wmean(key):
    n_, d_ = 0, 0
    for s in stocks:
        if s.get(key) is not None:
            n_ += s[key] * s["value_l"]; d_ += s["value_l"]
    return round(n_ / d_, 1) if d_ else None
factor = {"Quality": wmean("quality"), "Value": wmean("value"), "Growth 3Y": wmean("g3"),
          "Growth 1Y": wmean("g1"), "Price-trend": wmean("st1"), "Sector-macro": wmean("macro")}

def spot(call):
    c = [s for s in by_w if s["call"] == call and s["quality"] is not None]
    return c[0] if c else None
spot_hold, spot_sell = spot("Hold"), spot("Sell")

def fagg(key):
    m = {}
    for f in funds:
        m[f[key]] = m.get(f[key], 0) + f["aum_l"]
    return {k: round(v / fund_val * 100, 1) for k, v in sorted(m.items(), key=lambda kv: -kv[1])}
fund_cat, fund_amc = fagg("category"), fagg("house")

# ---- plan / deployment ------------------------------------------------------
titan_trim_l = round(by_w[0]["value_l"] - 0.08 * eq_val, 1)   # trim toward 8% of equity sleeve
sells_l = round(sum(s["value_l"] for s in sells), 1)
fund_actions_l = round(sum(f["aum_l"] for f in funds if f["name"] in
                   ("Nippon India Multi Cap", "ICICI Pru Multi Asset (Reg)", "Bandhan Small Cap")), 1)
deployable_l = round(sells_l + titan_trim_l, 1)
total_reorg_l = round(deployable_l + fund_actions_l, 1)
sleeves = [
  ("Low-vol / value domestic equity", round(deployable_l * 0.60, 1),
   "Favoured style tilt; the book is value-light", "quality & concentration risk"),
  ("Foreign equity (60:40 DM:EM)", round(deployable_l * 0.24, 1),
   "Largest open gap vs the ~25%-of-equity target", "single-country concentration"),
  ("Gold & silver sleeve (75:25)", round(deployable_l * 0.11, 1),
   "No sized sleeve today", "adds a low-correlation diversifier"),
  ("Cash buffer (staged)", round(deployable_l * 0.05, 1),
   "Freed cash is never assumed fully invested", "entry & tax timing"),
]

uhni = dict(name="AZBY Family Office", corpus_cr=78.5,
  entities=[("Family Private Trust", "Discretionary — next-gen beneficiaries", 34.2),
            ("AZBY Holdings HUF", "Hindu Undivided Family", 12.6),
            ("Operating Co. Treasury", "Surplus treasury, promoter entity", 18.9),
            ("Individual — Promoter", "Personal demat & funds", 9.4),
            ("Individual — Spouse", "Personal demat & funds", 3.4)],
  alloc=[("Domestic equity", 41.0), ("Foreign equity", 14.0), ("Fixed income", 22.0),
         ("Gold & silver", 6.0), ("Private markets / AIF", 11.0), ("Cash & arbitrage", 6.0)],
  goals=[("Perpetual family corpus", "Real growth > CPI + 4%", "Perpetual"),
         ("Next-gen education & setup", "₹12 Cr", "2029–2034"),
         ("Philanthropy endowment", "₹8 Cr", "2031"),
         ("Promoter liquidity-event reinvestment", "₹25 Cr inflow", "2027")])

DATA = dict(
  meta=dict(family="AZBY Family", book_cr=book_cr, book_l=book_l, equity_l=eq_val,
            fund_l=fund_val, n_stocks=len(stocks), n_funds=len(funds), as_of="21 July 2026",
            equity_frac=round(eq_val / book_l * 100, 1), fund_frac=round(fund_val / book_l * 100, 1)),
  palette=dict(navy="16233B", indigo="1B27A3", indigo2="4A57C4", indigo_t="8C95DE",
               green="1E9E6A", red="E0402F", amber="F2A93C", slate="6B7280", grid="E5E7EB",
               tint_green="E0F2EA", tint_indigo="EEEFF7", tint_red="FBE3E0", near="F5F6FC"),
  stocks=stocks, sells=sells, watch=watch,
  concentration=dict(top5=top5, top10=top10, largest_book=round(by_w[0]["weight"], 1),
     largest_name=by_w[0]["name"], largest_sleeve=round(sleeve_w(by_w[0]), 1),
     names_over8_sleeve=sum(1 for s in stocks if sleeve_w(s) > 8),
     largest_sector=max(sectors.values()), largest_amc=max(fund_amc.values()), sell_wt=sell_wt),
  sectors=sectors, caps=caps, hist=bins, below40=below40, factor=factor,
  spot_hold=spot_hold, spot_sell=spot_sell,
  funds=funds, fund_cat=fund_cat, fund_amc=fund_amc,
  plan=dict(sells_l=sells_l, titan_trim_l=titan_trim_l, deployable_l=deployable_l,
     fund_actions_l=fund_actions_l, total_reorg_l=total_reorg_l, sells_cr=round(sells_l / 100, 2),
     deployable_cr=round(deployable_l / 100, 2), total_reorg_cr=round(total_reorg_l / 100, 2),
     sleeves=sleeves, n_sells=len(sells)),
  uhni=uhni)

OUT.write_text(json.dumps(DATA, indent=1))
m = DATA["meta"]; c = DATA["concentration"]
print("wrote", OUT)
print(f"book ₹{book_cr}Cr | equity ₹{eq_val}L ({m['equity_frac']}%) | funds ₹{fund_val}L ({m['fund_frac']}%) | {len(stocks)} stocks | {len(funds)} funds")
print(f"sells {len(sells)} ({sell_wt}% book) | below40 {below40} | top5 {top5}% top10 {top10}% | largest {c['largest_name']} {c['largest_book']}% book / {c['largest_sleeve']}% sleeve | >8% sleeve {c['names_over8_sleeve']}")
print("caps:", caps)
print("top sectors:", list(sectors.items())[:6])
print("spot hold:", spot_hold["name"], spot_hold["score"], "| spot sell:", spot_sell["name"], spot_sell["score"])
print("watchlist:", len(watch), [(w["name"], w["score"]) for w in watch])
print("fund cats:", len(fund_cat), "| largest AMC:", max(fund_amc.values()), "| titan trim ₹L:", titan_trim_l, "| deployable ₹Cr:", DATA["plan"]["deployable_cr"], "| total reorg ₹Cr:", DATA["plan"]["total_reorg_cr"])
