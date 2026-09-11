"""CN programme — the agent manifest. Emits research/notes/china-dossiers/MANIFEST.md and
a JSON the orchestrator dispatches from, 3 concurrent (CLAUDE.md rule 6).
Each bundle = one subagent = one cited dossier on disk. Questions are deliberately narrow
and answerable; an agent that cannot source a figure must say so, never invent one."""
import json, pathlib

A = []
def add(slug, topic, qs): A.append({"slug": slug, "topic": topic, "qs": qs})

CITY_Q = lambda c: [
    f"{c}: new-home price index peak (month/year) and the cumulative decline from peak to the latest available month, with the NBS 70-city series or a named local source",
    f"{c}: SECOND-HAND home price decline from peak — usually far worse than new-build because of the presale/price-cap distortion; give the figure and explain the gap",
    f"{c}: actual transacted price per square metre now vs at peak, in CNY/sqm, for a named district or two (centre vs suburb) — anecdote-level is fine if labelled",
    f"{c}: residential gross rental yield now vs pre-2021, with the source's method",
    f"{c}: transaction VOLUME (units or sqm sold) now vs the 2020/2021 peak",
    f"{c}: any local rescue policy (purchase restrictions lifted, down-payment or mortgage-rate floor cuts, hukou easing) and the dated effect on prices",
]
# ---------------- B1 geography ----------------
for c in ["Beijing (also treat it AS THE CAPITAL: is the capital-city premium intact?)",
          "Shanghai", "Guangzhou", "Shenzhen"]:
    add("b1-t1-" + c.split()[0].lower(), f"Tier-1: {c.split()[0]}", CITY_Q(c.split()[0]))
add("b1-t1-overview", "Tier-1 as a class", [
    "The official NBS tier-1 / tier-2 / tier-3 aggregate new-home and second-hand price indices: peak, latest, cumulative decline for EACH tier — the single most important table in this programme",
    "Why tier-1 has held up better than tier-2/3: the mechanism, not just the number",
    "Is any tier-1 city actually RISING now (Shanghai has been reported as such)? Give dated figures",
    "The gap between the official NBS index and private indices (Beike/KE Holdings, China Real Estate Information Corp/CRIC, E-house): how much does the official series understate the fall, and who says so?",
    "What exactly are the 4 tier-1, and the commonly used 'new tier-1' list of 15? Name them and the classifier (Yicai/CBN ranking)",
])
T2 = [("Hangzhou","Nanjing"),("Chengdu","Chongqing"),("Wuhan","Changsha"),("Xi'an","Zhengzhou"),
      ("Tianjin","Shijiazhuang"),("Suzhou","Wuxi"),("Qingdao","Jinan"),("Shenyang","Dalian"),
      ("Xiamen","Fuzhou"),("Hefei","Nanchang"),("Kunming","Guiyang"),("Ningbo","Wenzhou"),
      ("Harbin","Changchun"),("Lanzhou","Urumqi"),("Zhuhai","Dongguan"),("Foshan","Huizhou")]
for a, b in T2:
    add(f"b1-t2-{a.lower().replace(chr(39),'')}-{b.lower()}", f"Tier-2: {a} & {b}", [
        f"{a}: new-home and second-hand price peak and cumulative decline to latest, dated, sourced",
        f"{b}: new-home and second-hand price peak and cumulative decline to latest, dated, sourced",
        f"{a} and {b}: residential rental yield now vs pre-crash",
        f"{a} and {b}: inventory / months of unsold supply, and any reported 'ghost' or stalled-project problem",
        f"Which of {a} or {b} fell harder and WHY — population flow, industry base, or land-supply discipline",
        f"{a}/{b}: any notable local specifics (Wenzhou's own 2011 bust, Zhengzhou's rescue fund, Tianjin's Binhai district, Kunming's oversupply) if applicable",
    ])
add("b1-t3-notorious", "Tier-3/4: the notorious busts", [
    "Hegang, Heilongjiang: apartments reportedly selling for tens of thousands of CNY total. Current price per sqm, the peak, the mechanism (population collapse, coal)",
    "Ordos / Kangbashi, Inner Mongolia: the original 'ghost city'. What actually happened to prices and occupancy, 2010 to now — including the part where it partly filled up",
    "Yingkou, Danzhou (Hainan), Beihai (Guangxi): price declines and the oversupply story in each",
    "Fuxin, Shuangyashan, Qitaihe and the other shrinking north-eastern cities: the cheapest housing in China — give prices",
    "What share of China's housing stock and unsold inventory sits in tier-3 and below? The number that decides whether the bust is national or peripheral",
])
add("b1-t3-satellite", "Tier-3: satellite and speculative belts", [
    "Langfang and Zhuozhou (the Beijing commuter belt): the 2016-17 spike and the subsequent collapse — reported as one of the worst in China. Figures",
    "Tangshan, Baoding, Qinhuangdao: the Hebei belt's declines",
    "Weihai, Zhoushan, Yantai: coastal second-home markets",
    "Hainan province as a whole: the 2018 purchase ban, the free-trade-port push, and where prices are now",
    "The 'commuter belt' pattern generally: do satellite towns of strong cities fall harder than independent tier-3s?",
])
add("b1-provincial-capitals", "Provincial capitals as a class", [
    "Do provincial capitals systematically outperform non-capital cities in the same province? Evidence and figures",
    "The 'strong provincial capital' (强省会) policy of concentrating resources in the capital: what it is, which provinces ran it, and its property consequence",
    "Which provincial capitals have fallen the MOST and the LEAST, ranked with figures",
    "Population flows into provincial capitals vs out of the rest of the province: the numbers behind the divergence",
])
# ---------------- B2 land ----------------
add("b2-land-national", "National land market: the headline series", [
    "China's national land-transfer income (土地出让金) by year 2015-2025 in CNY trillion, sourced to MOF — the single most important fiscal number in this story",
    "Land-transfer income as a share of local-government revenue, by year, and the peak",
    "Total residential land area sold nationally by year, 2015-2025, and the decline from peak",
    "The average land price per sqm nationally, peak and now",
    "What replaced the lost land revenue (transfers from the centre, special bonds, asset sales, tax)? Quantified if possible",
])
add("b2-land-auctions", "Land auctions: failure rates and mechanics", [
    "The 'centralized land supply' (集中供地) rule introduced in 2021 for 22 major cities: what it was, how it worked, and when it was abandoned",
    "Land-auction FAILURE / withdrawal rates (流拍率) by year and city tier — the clearest single measure of developer capitulation",
    "The share of land parcels sold at the FLOOR/reserve price with zero premium, by year",
    "Average land premium rate (溢价率) by year and tier, peak to now",
    "Named examples of specific high-profile Beijing/Shanghai/Shenzhen/Hangzhou parcels: peak-era price vs a comparable recent parcel",
])
add("b2-land-state-buyers", "Who is actually buying the land now", [
    "The share of land purchased by LOCAL-GOVERNMENT-LINKED entities (LGFVs, city investment companies, state land-reserve arms) vs private developers, by year — the 'the government is buying its own land' phenomenon",
    "Evidence and estimates of this share from named research houses (Rhodium, Gavekal, Goldman, CICC, academic work)",
    "What happens to that land afterwards — is it developed, or warehoused?",
    "The top land buyers in China by year: how the league table shifted from private (Evergrande/Country Garden/Sunac) to state (Poly, China Overseas, China Resources, Greentown) developers",
    "Does this inflate the reported land-transfer income, and by how much?",
])
add("b2-land-vs-house", "Land price vs house price: the ratio", [
    "The land-cost share of a finished apartment's price in tier-1 vs tier-3 cities, and how it changed through the boom and bust",
    "The '面粉贵过面包' (flour costlier than bread) phenomenon where land cost exceeded sellable housing value: when, where, and the figures",
    "Did land prices fall MORE or LESS than house prices in the bust? Give the two series side by side",
    "Residential vs commercial vs industrial land price series — which fell hardest",
])
add("b2-land-fiscal-model", "The leasehold land-sale fiscal model", [
    "How the Chinese land-sale model actually works: state ownership, 70-year residential / 40-50 year commercial leaseholds, the 1994 tax-sharing reform that created the incentive",
    "What happens at the end of a 70-year residential leasehold — the law, the 2007 Property Law, the Wenzhou 20-year-lease incident of 2016, and what is actually still unresolved",
    "The 'land finance' (土地财政) critique and the leading scholars/sources on it",
    "How much of local-government DEBT is collateralized on land value, and what a 30% land-price fall does to that collateral",
])
add("b2-land-reform", "Land reform and rural land", [
    "The rural collective land vs urban state land distinction, and the 2019 Land Administration Law amendment allowing some rural construction land to market",
    "Rural homestead (宅基地) reform pilots and why they matter for supply",
    "The hukou-land link: why migrants cannot monetize rural land, and the effect on urban demand",
    "Any 2024-2026 land-reform announcements (Third Plenum 2024 in particular) and what they actually change",
])
add("b2-land-monetization", "Land reserves, PSL and state destocking", [
    "The Pledged Supplementary Lending (PSL) facility: size by year, what it funded, and its role in the 2015-2018 shantytown-redevelopment (棚改) boom that inflated tier-3 prices",
    "The 2024 CNY 300bn relending facility for state purchase of unsold homes: size, uptake, and why uptake was low",
    "The 2024-2025 programme for local governments to buy back idle LAND from developers using special bonds: size and actual execution",
    "Have any of these programmes worked, measured by price or inventory? Sourced assessments",
])
add("b2-land-data-sources", "Where land data actually comes from", [
    "The authoritative sources for Chinese land-transaction data: China Index Academy (中指院), CREIS, Wind, CEIC, the Ministry of Natural Resources, local land bureaus — what each covers and its lag",
    "Which of these is free/scrapeable and which is paywalled — a practical acquisition note",
    "The known reliability problems with each (the land-transfer-income vs land-sales-revenue discrepancy in particular)",
    "Any academic or open datasets on Chinese land auctions (parcel-level) a researcher could actually download",
])
# ---------------- B3 asset classes ----------------
for city in ["Beijing", "Shanghai", "Shenzhen", "Guangzhou"]:
    add(f"b3-office-{city.lower()}", f"Grade-A office: {city}", [
        f"{city} Grade-A office VACANCY rate now vs 2019 and the peak-vacancy figure, sourced to CBRE/JLL/Cushman/Savills/Colliers",
        f"{city} Grade-A office effective RENT (CNY/sqm/month) now vs peak, and the cumulative decline",
        f"{city} office CAP RATE / net initial yield now vs pre-crash",
        f"{city} office new supply pipeline and why vacancy stays high",
        f"{city}: any landmark distressed office transaction or asset-management-company sale, with price and implied yield",
    ])
add("b3-office-tier2", "Grade-A office: tier-2 centres", [
    "Office vacancy and rent decline for Chengdu, Chongqing, Wuhan, Hangzhou, Tianjin, Shenyang — the tier-2 office glut, sourced",
    "Which Chinese city has the world's highest office vacancy rate, and the figure",
    "The 'business park' / industrial-office (产业园) category: rents and vacancy",
    "How much of the tier-2 office supply was built by local governments for industrial-policy reasons rather than demand",
])
add("b3-retail-shops", "Shops, high street and malls", [
    "High-street retail rent decline in Beijing Wangfujing, Shanghai Nanjing Road / Huaihai Road, and a named Shenzhen or Guangzhou strip — figures and dates",
    "Shopping-MALL rents and vacancy vs high street: which held up better and why (the e-commerce interaction)",
    "Strata-titled SHOPS (商铺) sold to retail investors: the price collapse in this category specifically, which is reported as among the worst of all",
    "Retail property cap rates / yields now vs pre-crash",
    "Named distressed mall sales or REIT-level retail valuations that reveal the mark",
])
add("b3-apartments-vs-houses", "Apartments vs villas vs townhouses", [
    "Do villas / low-density housing (别墅, 洋房) hold value better or worse than high-rise apartments in the bust? Evidence and figures",
    "The 'improvement housing' (改善型) vs 'first-home' segment split: which fell harder",
    "The luxury / ultra-prime segment: has it fallen at all? Named Shanghai/Shenzhen prime projects and figures",
    "OLD vs NEW apartments: the age-depreciation problem in Chinese housing (30-year-old buildings), and what it does to second-hand prices",
    "The 类住宅 / commercial-titled apartment (商住房) category: the 2017 Beijing ban, and the resulting price collapse — a specific, severe and under-reported case",
])
add("b3-industrial-logistics", "Industrial and logistics property", [
    "China logistics/warehouse rents and vacancy now vs 2021 peak, sourced to CBRE/JLL or a logistics REIT",
    "Why logistics has been the most resilient Chinese property class — the mechanism",
    "Logistics cap rates now vs pre-crash, and what the C-REIT market implies",
    "Cold storage and data-centre property as sub-classes: yields and any oversupply",
])
add("b3-hotel-hospitality", "Hotels and hospitality property", [
    "Chinese hotel RevPAR / occupancy recovery post-COVID vs 2019, and hotel asset values",
    "Distressed hotel sales by developers deleveraging: named transactions and prices",
    "Hotel cap rates and any listed/REIT comparables",
])
add("b3-whole-buildings", "Whole buildings and block transactions", [
    "The Chinese 'block/whole-building transaction' (大宗交易) market: total volume by year 2019-2025, and the decline",
    "Who the buyers are now (insurers, AMCs, state funds, foreign opportunistic capital) vs before",
    "Named large whole-building trades in Shanghai/Beijing with price per sqm and implied yield, showing the mark-down",
    "The role of Cinda/Huarong/Great Wall/Orient (the four AMCs) in absorbing distressed property, and their own resulting problems",
    "Foreign capital: has Blackstone/Brookfield/GIC/PAG been buying or selling Chinese property? Named deals and direction",
])
add("b3-parking-storage", "The odd categories", [
    "Parking spaces (车位) sold as investments: price collapse figures — a genuinely interesting and under-covered case",
    "Serviced apartments and long-term rental apartments (长租公寓): the 2018-2021 wave of operator failures (Danke/Qingke) and what survived",
    "Self-storage, senior housing, student housing in China: does any of it exist at scale, and any yields",
])
# ---------------- B4 rental yields / business rent ----------------
add("b4-resi-yield-national", "Residential rental yield: the national picture", [
    "China's national average residential gross rental yield now vs 2015 and 2021, with the source and method",
    "The 50-city rental-yield table (the widely cited one showing 1.5-2% in tier-1): give the actual numbers by city",
    "Rental yield vs the 5-year LPR / mortgage rate: the carry spread, then vs now — the single cleanest 'is it cheap yet' statistic",
    "Has the yield risen because rents rose or because prices fell? Decompose it",
    "International comparison: Chinese tier-1 yields vs Tokyo, Seoul, Singapore, Hong Kong, Mumbai, New York",
])
add("b4-rents-falling", "Are rents themselves falling?", [
    "China residential RENT index by year and city tier: is rent falling in nominal terms, and by how much?",
    "The Beike/Anjuke rent indices for tier-1 cities: peak and latest",
    "Why rents are falling: graduate unemployment, migrant outflow, the supply of unsold units pushed into the rental market",
    "The affordable-rental-housing (保障性租赁住房) programme: units delivered and the effect on market rent",
])
add("b4-business-rent", "Business rent: the cross-asset rent table", [
    "A single comparative table: office / retail / logistics / residential rent change from peak to latest, nationally and for Shanghai and Beijing",
    "Which business-property class has the highest and lowest current yield in China, and the spread between them",
    "Rent-free periods and incentives in Chinese office leasing now vs pre-crash — the headline-vs-effective rent gap",
    "Lease lengths and tenant-credit deterioration in Chinese commercial leasing",
])
add("b4-yield-vs-history", "Yield in historical and cross-country context", [
    "What rental yield did Japanese property carry at the 1991 peak and at the trough? The single best analogue for the yield question",
    "US, Spanish and Irish rental yields at their peaks and troughs",
    "Is there a yield level at which property markets historically stop falling? Evidence either way",
    "The Gordon-growth framing: what rent growth does a 1.8% Chinese tier-1 yield imply, and is it plausible given demographics?",
])
add("b4-price-to-income", "Price-to-income and affordability", [
    "Price-to-income ratios for Beijing, Shanghai, Shenzhen, Guangzhou and a few tier-2s, now vs peak, sourced (Numbeo, E-house, academic)",
    "Shenzhen's reported ~35x price-to-income at peak: verify or correct it with a source",
    "How Chinese price-to-income compares with Tokyo 1990, Hong Kong, London, Mumbai, New York",
    "Mortgage debt-service-to-income ratios for Chinese households, and the 'six pockets' (六个钱包) phenomenon of family-funded down payments",
    "Has affordability actually improved through the bust? Prices fell but so did incomes and expectations",
])
# ---------------- B5 velocity / anatomy ----------------
add("b5-velocity-national", "Crash velocity: the national numbers", [
    "The month-by-month year-on-year decline of the NBS 70-city new-home index from the 2021 peak to the latest print — the actual velocity series",
    "The steepest single month and the steepest 12-month window of the decline",
    "How many consecutive months of decline, as of the latest data",
    "The cumulative peak-to-latest decline in the official index vs private estimates (which run 2-5x larger) — reconcile them with named sources",
    "Sales VOLUME velocity: CNY 18.2tn (2021) to the latest year, the annualized rate of collapse",
])
add("b5-velocity-precrash", "Pre-crash rising velocity", [
    "The 2015-2021 appreciation: annualized rate of new-home price rises nationally and for tier-1, tier-2, tier-3 separately",
    "The 2015-2016 boom specifically: the fastest appreciation months on record and where",
    "The 2016-2018 tier-3 shantytown-redevelopment (棚改) boom: appreciation rates in tier-3 cities, the PSL money behind it",
    "Longer history: what did Chinese house prices do 1998 (housing privatization) to 2021? The full appreciation record",
    "The ratio of the boom's annualized rate to the bust's annualized rate — the principal's exact question, for China",
])
add("b5-peak-timing", "Dating the peak precisely", [
    "When exactly did Chinese property peak, and by which measure? (prices, sales volume, new starts, land sales, developer bonds all peaked at different times — give each)",
    "The sequence of the turn: which series turned first, and by how many months",
    "The Three Red Lines (Aug 2020) and the Evergrande default (Dec 2021) as dated causal markers",
    "Was there a warning window between the policy and the price peak that an investor could have acted in?",
])
add("b5-starts-completions", "Starts, completions and the physical cycle", [
    "China housing NEW STARTS by year 2015-2025 in million sqm, and the collapse from peak (reported as ~-70%)",
    "COMPLETIONS by year, and why completions held up while starts collapsed (the 'guarantee delivery' 保交楼 campaign)",
    "Floor space UNDER CONSTRUCTION: the stock, and how many years of sales it represents",
    "Unsold finished inventory vs unsold under-construction: the two numbers, and months of supply for each",
    "Construction-sector employment and the migrant-worker consequence of a 70% starts collapse",
])
add("b5-compare-japan", "The Japan comparison, done properly", [
    "Japan's urban land price index (the 6-large-cities series): peak year, the cumulative decline for RESIDENTIAL and for COMMERCIAL land, and how many years to trough — the commercial figure is the famous one",
    "Japanese nationwide residential land vs the 6-cities index: the difference matters and is usually elided",
    "Japan's pre-peak appreciation rate vs its decline rate — the velocity ratio",
    "What Japanese rental yields did through it",
    "The genuine structural differences between Japan 1990 and China 2021 (urbanization stage, income level, corporate cross-holdings, capital account, policy response speed) — sourced, both sides",
])
add("b5-compare-others", "US, Spain, Ireland, Hong Kong, Thailand", [
    "US Case-Shiller: 2006 peak, peak-to-trough decline, years to trough, and the recovery",
    "Spain and Ireland 2007-2013: peak-to-trough house-price declines, and the land/development-land declines which were far worse",
    "Hong Kong 1997-2003: the -66% figure, the negative-equity count, and years to recover",
    "Thailand/Indonesia 1997-98 property busts as EM analogues",
    "Which of these China most resembles on the data, and which on the policy response? Argue both",
])
add("b5-recovery-shape", "What recovery looks like, if any", [
    "Any Chinese city or segment where prices have actually stabilized or risen in the last 12 months — named, with figures",
    "The second-hand vs new-build divergence in any recovery",
    "Base-rate: in the international episodes, how long from trough to recovering the old nominal peak? And the real peak?",
    "The 'L-shaped' vs 'U-shaped' debate on China property: the named analysts on each side and their actual arguments",
])
# ---------------- B6 debt ----------------
for d in ["Evergrande (China Evergrande Group)", "Country Garden (Bijia)", "Vanke",
          "Sunac China", "Kaisa", "Shimao", "Sino-Ocean and Agile", "Poly and China Overseas (the state survivors)"]:
    n = d.split()[0].lower()
    add(f"b6-dev-{n}", f"Developer: {d.split('(')[0].strip()}", [
        f"{d}: total liabilities at peak in CNY and USD, and the split between bank debt, offshore bonds, onshore bonds, trade payables and presale liabilities",
        f"{d}: the default timeline — dates of first missed payment, formal default, restructuring proposal, liquidation or resolution",
        f"{d}: offshore USD bond recovery value — where the bonds trade or what the restructuring implies in cents on the dollar",
        f"{d}: equity price peak to now, and market cap destroyed",
        f"{d}: unfinished units / projects and the delivery status",
        f"{d}: what its Three Red Lines metrics looked like BEFORE the fall — the early-warning question",
    ])
add("b6-three-red-lines", "The Three Red Lines policy", [
    "The exact definition of each of the three red lines (liability-to-asset ex-presales, net-debt-to-equity, cash-to-short-term-debt) and their thresholds",
    "The tiering system and what each tier's debt-growth cap was",
    "How many of the top 30/50 developers breached all three when it was introduced (Aug 2020), with the list",
    "Did the policy cause the bust or reveal it? The sourced arguments on each side",
    "Was the policy ever formally relaxed or abandoned, and when?",
])
add("b6-presale-escrow", "The presale model and escrow", [
    "How Chinese presale works: what share of homes are sold before completion, the escrow rules, and how developers legally and illegally accessed escrowed funds",
    "The size of presale liabilities (合同负债) across the sector — money owed as houses, not cash",
    "The 2022 mortgage-payment strike (停贷): how many projects, the scale, and how it was resolved",
    "'Rotten tail buildings' (烂尾楼): the estimated number of unfinished pre-sold units, sourced — the estimates vary wildly, so give the range and who says what",
    "The post-crisis escrow tightening and its effect on developer liquidity",
])
add("b6-lgfv", "LGFV and hidden local-government debt", [
    "The estimated total stock of LGFV debt in CNY trillion, from at least three named sources (IMF, Goldman, Rhodium, CICC) — and why they disagree",
    "LGFV interest-coverage and the share unable to cover interest from operating cash flow",
    "The 2023-2025 LGFV debt-swap / refinancing programmes: size and mechanics",
    "The link from land-sale collapse to LGFV distress: the transmission, quantified",
    "Any actual LGFV defaults (public bond vs non-standard/trust products) — the distinction and the record",
])
add("b6-household-mortgage", "Household mortgage debt", [
    "China household debt as % of GDP and as % of disposable income, by year, peak and now, sourced to BIS or PBoC",
    "Outstanding residential mortgage balance in CNY trillion, and the first-ever decline in it (which year and by how much)",
    "Mortgage prepayment wave of 2022-2023: scale and why households did it",
    "Mortgage rates: the 5-year LPR path and the actual first-home mortgage rate, peak to now",
    "Negative equity in China: any estimates of how many households are underwater",
])
add("b6-credit-gap", "The BIS credit-to-GDP gap and formal early warning", [
    "China's BIS credit-to-GDP GAP by year: what it was in 2009-2016 (reportedly among the highest ever recorded) and what it is now",
    "The BIS early-warning framework: what gap level signals banking distress, the historical hit rate, and China's readings against it",
    "The IMF Article IV and FSAP warnings on Chinese property: which years, what they said, how specific they were",
    "Other formal early-warning work on China property (Rogoff-Yang, academic HP-filter credit gaps) and its dated calls",
    "The honest verdict: was this crash forecastable from public aggregates, and by when?",
])
add("b6-property-share-gdp", "Property's share of the economy", [
    "The Rogoff-Yang estimate that property accounts for ~29% of Chinese GDP: the method, the number, and the critiques",
    "Property's share of local-government revenue, household wealth, and bank loan books — three separate numbers",
    "Property's share of Chinese HOUSEHOLD WEALTH (reported ~60-70%) vs the US/Japan comparison",
    "The estimated GDP drag from the property correction, by year, from named sources",
    "Bank exposure: property-related loans as a share of Chinese bank assets, and reported NPL ratios vs plausible ones",
])
add("b6-inventory-vacancy", "Inventory and the vacancy question", [
    "China's unsold housing inventory in million sqm and in UNITS, and months of supply — official and private estimates",
    "The Beike Research Institute 2022 vacancy survey (reportedly 12% average, over 20% in some cities): the actual figures and the controversy",
    "The 'how many empty apartments' estimates (the 65-150 million range) — who produced each, the method, and which are credible",
    "Electricity-meter and night-lights based vacancy studies: what the academic work actually found",
    "How many years of current sales would it take to clear the inventory?",
])
add("b6-trusts-shadow", "Trusts, shadow banking and wealth products", [
    "Zhongrong Trust and Zhongzhi Enterprise Group's 2023 collapse: size, property exposure, and investor losses",
    "The size of the Chinese trust industry's property exposure, peak and now",
    "Developer-issued wealth-management products sold to retail and employees (Evergrande Wealth in particular): scale and losses",
    "The 2018 asset-management rules and how shadow property credit was supposed to have been curbed",
])
add("b6-debt-predictive-summary", "The predictive-indicator scorecard", [
    "Assemble a single scorecard: for each of (BIS credit gap, mortgage/GDP, price-to-income, price-to-rent, land-revenue dependence, developer leverage, starts-to-sales ratio, inventory months), what its reading was in 2019-2020 and whether it was flashing",
    "Which indicator gave the EARLIEST signal, and which the clearest",
    "Which widely watched indicators gave NO signal — the false negatives, which matter as much",
    "Who publicly called it, and when, with links — and who called it far too early (the perma-bears whose 'call' spanned a decade)",
])
# ---------------- B7 REITs ----------------
add("b7-creits-overview", "C-REITs: the market", [
    "The Chinese public infrastructure REIT (C-REIT) pilot: launch date (June 2021), the legal structure (public fund + ABS), and how it differs from a US/Singapore REIT",
    "Total number of listed C-REITs and total market cap / AUM as of the latest data",
    "The asset categories permitted and the 2023-2024 expansion to consumer infrastructure and affordable rental housing",
    "The C-REIT index performance since launch: the 2022-2023 drawdown and the 2024-2025 rally, with figures",
    "Distribution yields on C-REITs by asset class",
])
add("b7-creits-rental-housing", "C-REITs: affordable rental housing", [
    "The affordable-rental-housing C-REITs (Beijing, Shenzhen, Xiamen, Shanghai): names, codes, IPO dates, sizes",
    "Their distribution yields and occupancy",
    "What their valuations imply for residential cap rates in those cities — a rare market-priced mark on Chinese residential",
    "Performance since listing",
])
add("b7-creits-commercial", "C-REITs: consumer/retail and logistics", [
    "The consumer-infrastructure C-REITs (Hua Xia Huarun Commercial, China Jinmao,印力/SCPG, Wumart etc): names, sizes, yields",
    "Logistics C-REITs (GLP/普洛斯, AVIC, Jingdong/JD): names, yields, occupancy",
    "What implied cap rates these suggest for Chinese retail and logistics",
    "The best-performing and worst-performing C-REITs since listing",
])
add("b7-hk-china-property-equity", "HK-listed China property equity", [
    "The Hang Seng Mainland Properties Index: peak, trough, latest — the cumulative drawdown",
    "Total market cap destroyed across HK-listed Chinese developers since 2020",
    "How many HK-listed Chinese developers have been suspended, delisted or liquidated",
    "The state-owned survivors' share prices vs the private developers' — the divergence, quantified",
    "Any developer whose equity has actually recovered",
])
add("b7-hk-reits", "Hong Kong REITs and HK property", [
    "Link REIT: price peak to now, distribution yield, and the NAV discount",
    "The HK REIT market generally (Fortune, Champion, Sunlight, Prosperity): yields and drawdowns",
    "Hong Kong office vacancy and rent decline — among the world's worst, with figures",
    "HK residential prices: peak (2021) to now, the cumulative fall, and negative-equity counts",
    "Why HK matters to the China story and how the two markets differ",
])
add("b7-sg-china-reits", "Singapore-listed China-asset REITs", [
    "CapitaLand China Trust: price, yield, NAV, occupancy and the mark-downs on Chinese malls",
    "Sasseur REIT, BHG Retail REIT, EC World REIT (which failed): what each held and what happened",
    "What these Singapore-listed vehicles reveal about Chinese retail property values that mainland data does not",
    "Dasin Retail Trust and any other China-asset SGX vehicle in distress",
])
add("b7-offshore-bonds", "The offshore USD developer bond market", [
    "The size of the Chinese offshore USD high-yield property bond market at peak, and its share of the whole Asia HY index",
    "The cumulative default count and defaulted amount by year",
    "Recovery values actually achieved in completed restructurings — cents on the dollar, named deals",
    "The index performance: the Asia/China HY property index drawdown and any recovery",
    "Who held these bonds and who lost: the distribution of pain across global funds",
])
add("b7-onshore-bonds-banks", "Onshore credit and the banks", [
    "Onshore developer bond defaults vs offshore: the different treatment and why",
    "Chinese bank share prices and valuations through the property bust — why they held up",
    "Reported vs estimated true property NPLs at Chinese banks",
    "Bank capital raising, the 2024-2025 special-bond recapitalization of the big banks: size and reason",
])
add("b7-foreign-investable", "What a foreign investor can actually own", [
    "The realistic instruument list for a foreign investor wanting China property exposure (or short exposure): HK-listed equity, offshore bonds, SGX REITs, A-share developers via Stock Connect, C-REITs (are they QFII/Connect-accessible?), CDS",
    "Are C-REITs accessible to foreign investors at all, and how",
    "Liquidity and practical constraints on each",
    "Any ETF or index product giving China property exposure",
])
# ---------------- B8 policy / demographics ----------------
add("b8-policy-timeline-1", "Policy timeline 2016-2021: the tightening", [
    "'Houses are for living in, not for speculation' (房住不炒): when introduced, by whom, and what followed",
    "The 2016-2019 purchase restrictions, price caps and the 'one city one policy' framework",
    "The 2020 Three Red Lines and the bank concentration caps on property lending (the two-part squeeze)",
    "The 2021 centralized land auctions and the presale-fund tightening",
    "A dated list of every major tightening measure 2016-2021",
])
add("b8-policy-timeline-2", "Policy timeline 2022-2026: the rescue", [
    "A dated list of every major SUPPORT measure 2022 through 2026: the 16-point plan (Nov 2022), the three arrows, the 2023 easing, the May-2024 package, the Sep-2024 package, and anything in 2025-2026",
    "Which measures were actually funded vs announced",
    "The mortgage-rate floor removal, down-payment cuts, and purchase-restriction removals by city",
    "The 'white list' project financing mechanism: size and delivery",
    "The assessed effectiveness of each, with sourced analyst views",
])
add("b8-property-tax", "The property tax that never came", [
    "The Shanghai and Chongqing property-tax pilots of 2011: design, rates, revenue, and effect",
    "The 2021 announcement of an expanded pilot and its quiet shelving — the dates and the reported reasons",
    "Why a property tax is both the obvious fiscal replacement for land sales and politically impossible",
    "The latest state of play on property tax as of 2026",
])
add("b8-demographics", "Demographics and structural demand", [
    "China's births by year 2016-2025 and the total-population decline, with dates",
    "Urbanization rate now and the projected path — how much migration demand is actually left",
    "Household formation projections and the implied structural housing demand vs current construction",
    "The Rogoff-Yang and other estimates of 'excess' housing supply relative to demand",
    "The age structure of housing demand and the coming inheritance wave of empty apartments",
])
add("b8-urbanization-hukou", "Hukou, migration and where demand goes", [
    "The hukou system's effect on housing demand, and the 2019-2025 reforms",
    "Net migration by city: which cities are gaining and losing population, with figures",
    "The 'shrinking cities' literature on China: how many cities are losing population",
    "The policy of concentrating population in city clusters (城市群) and its property implication",
])
add("b8-wealth-effect", "The wealth effect and consumption", [
    "Estimates of the Chinese housing wealth destroyed in CNY/USD terms since 2021",
    "The measured consumption response to the housing decline (the marginal propensity to consume out of housing wealth in China)",
    "Household savings-rate and deposit behaviour through the bust",
    "The deflation link: CPI/PPI/GDP-deflator prints and the property connection",
])
add("b8-sentiment-expectations", "Expectations, which is the real variable", [
    "Survey evidence on Chinese household house-price EXPECTATIONS (the PBoC urban depositor survey in particular): the series, peak to now",
    "Why expectations matter more than affordability in this market",
    "The reported shift in Chinese household asset preference from property to deposits/gold/bonds — quantified",
    "The 'gold rush' and bond-market rally as the mirror image of the property bust",
])
add("b8-comparisons-policy", "Policy response compared", [
    "How Japan's policy response to 1990 compared with China's to 2021 — speed, scale, mechanism",
    "How the US 2008 response compared (TARP, Fed, HAMP) with China's",
    "What the international evidence says about which interventions actually shortened property busts",
    "The 'balance-sheet recession' (Koo) framing applied to China: the argument and the counter-argument",
])
# ---------------- B9 comparative / interesting ----------------
add("b9-hainan-1993", "China's OWN precedent: Hainan 1993", [
    "The Hainan property bubble of 1988-1993: how big it got, the price rises, and the crash — China's own forgotten property bust",
    "The scale: Hainan reportedly had a huge share of the country's non-performing loans afterwards. Give the figures",
    "The Beihai (Guangxi) bubble of the same era and its abandoned buildings",
    "What was learned and what was forgotten — and who in 2021 cited Hainan as a warning",
])
add("b9-wenzhou-2011", "Wenzhou 2011: the preview nobody heeded", [
    "The Wenzhou property and private-lending crisis of 2011: price decline, the informal-credit collapse, and the boss-runaway phenomenon",
    "Wenzhou prices peak-to-trough in that episode and whether they ever recovered",
    "The 2016 Wenzhou 20-year land-lease expiry incident and how it was resolved",
    "Why Wenzhou is the best single-city case study of a Chinese property bust with a full cycle observable",
])
add("b9-ghost-cities", "Ghost cities: the real story", [
    "The ghost-city phenomenon: the best-documented cases and what actually happened to each over 10-15 years (several filled up)",
    "The academic work using satellite night-lights and Baidu data to measure Chinese urban vacancy",
    "Tianjin Binhai / Yujiapu, Zhengzhou Zhengdong, Kunming Chenggong, Ordos Kangbashi: current status of each",
    "The honest verdict on how much of the ghost-city narrative was right",
])
add("b9-interesting-facts-1", "The genuinely striking numbers", [
    "The claim that China poured more cement in 2-3 years than the US did in the entire 20th century: verify and source it",
    "China's built floor space per capita vs Japan/Europe/US at comparable income",
    "The number of housing units China built per year at peak vs the rest of the world combined",
    "The share of the world's cranes / steel / cement consumed by Chinese property at peak",
    "Any other single statistic that captures the scale, with a source",
])
add("b9-interesting-facts-2", "The human and social facts", [
    "The 2022 mortgage strike: how it organized, its scale, and how the state handled it",
    "Homebuyers who paid for units never built: estimated numbers and what recourse they had",
    "The 'Evergrande employees forced to buy WMPs' story and similar",
    "The effect on marriage and birth decisions of property prices, with any research",
    "The 'lying flat' (躺平) and youth-unemployment link to housing unaffordability",
])
add("b9-demolition-quality", "Building quality, demolition and the stock", [
    "The design life vs actual life of Chinese residential towers, and the 'shoddy construction' (豆腐渣) issue",
    "The coming maintenance and renovation liability for 30-year-old towers with no sinking fund",
    "Demolition-and-redevelopment (旧改/城市更新) as the new policy direction replacing new-build",
    "What happens to a 30-storey tower at the end of its life — the genuinely unresolved question",
])
add("b9-data-reliability", "How much can you trust any of these numbers?", [
    "The documented ways the NBS 70-city index understates declines (price caps on new-build, sample composition, the 'reference price' system)",
    "Instances of local governments banning price cuts or setting price floors — dated, sourced examples",
    "The gap between listed asking prices, reference prices and actual transaction prices",
    "Which private data sources are most trusted by professionals and why",
    "How a careful analyst should adjust official figures — the practical rule of thumb, sourced",
])
add("b9-who-got-it-right", "Who called it, and what they said", [
    "The named analysts, academics and investors who publicly warned about Chinese property with dated, specific calls: what each said and when",
    "The short sellers and the trades that worked (offshore HY, HK developer equity) and their timing",
    "The prominent forecasts that were wrong, in both directions",
    "What the successful callers used as their indicator — the practical lesson",
])
add("b9-global-spillover", "Global spillovers", [
    "Iron ore, coking coal, copper and steel: the demand hit from Chinese property, quantified",
    "Australian, Brazilian and Chilean export exposure to Chinese property construction",
    "Global cement, machinery (Caterpillar/Komatsu), and elevator/fixture makers' China exposure",
    "The luxury-goods and commodity-currency channels",
    "Which global asset was the best pure short/long expression of the Chinese property bust, in hindsight",
])
add("b9-what-happens-next", "The forward debate, fairly presented", [
    "The bull case on Chinese property from 2026 forward: the actual arguments and who makes them",
    "The bear case: the actual arguments and who makes them",
    "The consensus forecast range for Chinese house prices 2026-2030 from named institutions",
    "What would have to be true for stabilization — the specific observable conditions",
    "The most common analytical MISTAKE made about Chinese property, according to people who follow it closely",
])
# ---------------- B10 India read-across ----------------
add("b10-india-commodities", "India read-across: commodities and industry", [
    "How the Chinese property bust changed steel, cement and commodity prices, and what that did to INDIAN steel and cement companies (import pressure from Chinese oversupply in particular)",
    "Chinese steel export volumes since 2021 and the effect on Indian domestic prices and margins",
    "Which Indian sectors benefit and which suffer from Chinese property deflation — sourced views",
    "The 'China exporting deflation' thesis and its evidence",
])
add("b10-india-flows", "India read-across: capital flows and allocation", [
    "The documented rotation of EM equity allocations from China to India since 2021: figures on flows and index weights",
    "MSCI EM index weight of China vs India by year, and the crossover debate",
    "Whether that rotation is property-driven or something else, per named sources",
    "The risk that a Chinese policy success reverses the rotation — sized if possible",
])
add("b10-india-property-cycle", "India read-across: India's own property cycle", [
    "Indian residential price and volume cycle 2013-2026: the downturn, the 2021+ upturn, and current inventory months by city",
    "Indian developer leverage now vs the 2018-2020 NBFC crisis, and the consolidation since RERA and IBC",
    "Indian residential rental yields by city, and the comparison with Chinese tier-1 yields",
    "Indian REITs (Embassy, Mindspace, Brookfield, Nexus): yields, occupancy, and performance — directly relevant to the desk's open REIT gap",
    "Does India have any of the specific vulnerabilities that broke China (land-sale fiscal dependence, presale without escrow, LGFV-equivalents)? Argue it carefully both ways",
])
add("b10-india-lessons", "India read-across: what the desk should actually take", [
    "The three or four transferable lessons from the Chinese bust for an Indian multi-asset book, stated as testable propositions rather than narrative",
    "Which early-warning indicators from the China experience are CONSTRUCTIBLE for India from public data",
    "What Indian data would need pulling to run the equivalent monitoring — a concrete acquisition list",
    "The honest statement of what does NOT transfer",
])

# emit
out = pathlib.Path("research/notes/china-dossiers")
out.mkdir(parents=True, exist_ok=True)
nq = sum(len(a["qs"]) for a in A)
(out / "MANIFEST.json").write_text(json.dumps(A, indent=1, ensure_ascii=False))
lines = [f"# CN programme — agent manifest\n",
         f"{len(A)} agent bundles / **{nq} discrete sourced questions**. 3 concurrent (CLAUDE.md rule 6).",
         "Each bundle writes `research/notes/china-dossiers/<slug>.md` and returns <=200 words.\n"]
for i, a in enumerate(A, 1):
    lines.append(f"## {i:03d} · `{a['slug']}` — {a['topic']} ({len(a['qs'])} q)")
    lines += [f"{i}.{j}. {q}" for j, q in enumerate(a["qs"], 1)]
    lines.append("")
(out / "MANIFEST.md").write_text("\n".join(lines))
print(f"{len(A)} bundles, {nq} questions")
for b in sorted({a['slug'].split('-')[0] for a in A}):
    k = [a for a in A if a['slug'].startswith(b + '-')]
    print(f"  {b}: {len(k)} bundles, {sum(len(x['qs']) for x in k)} questions")
