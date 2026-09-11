"""Download daily prices for the NIFTY 50 constituents into ./data.

Source: the public NIFTY500_dataset repository (Yahoo-sourced daily OHLCV with
adjusted closes, 2012-01-02 to 2021-12-31). Files are named <rank>_<SYMBOL>.csv
where <rank> is the stock's 0-based position in MCAP_31032020_TOP500.xlsx.
"""
import openpyxl, urllib.request, os
SC = os.environ.get("PAIRS_WORK_DIR", os.path.dirname(os.path.abspath(__file__)))
NIFTY50 = """ADANIPORTS ASIANPAINT AXISBANK BAJAJ-AUTO BAJFINANCE BAJAJFINSV BPCL BHARTIARTL
BRITANNIA CIPLA COALINDIA DIVISLAB DRREDDY EICHERMOT GRASIM HCLTECH HDFCBANK HDFCLIFE
HEROMOTOCO HINDALCO HINDUNILVR HDFC ICICIBANK ITC IOC INDUSINDBK INFY JSWSTEEL KOTAKBANK
LT M&M MARUTI NTPC NESTLEIND ONGC POWERGRID RELIANCE SBILIFE SHREECEM SBIN SUNPHARMA TCS
TATACONSUM TATAMOTORS TATASTEEL TECHM TITAN UPL ULTRACEMCO WIPRO""".split()
wb=openpyxl.load_workbook(f"{SC}/mcap.xlsx"); ws=wb.active
rank={}
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[1]: rank[str(r[1]).strip()]=int(r[0])
base="https://raw.githubusercontent.com/Ratnesh-bhosale/NIFTY500_dataset/main/Dataset/"
ok,miss=[],[]
for s in NIFTY50:
    if s not in rank: miss.append((s,"no-rank")); continue
    fn = f"{rank[s]-1:03d}_{s.replace(chr(38), chr(95))}.csv"   # "M&M" is stored as "M_M"
    out=f"{SC}/data/{s}.csv"
    if os.path.exists(out) and os.path.getsize(out)>10000: ok.append(s); continue
    try:
        urllib.request.urlretrieve(base+fn, out)
        if os.path.getsize(out)>10000: ok.append(s)
        else: os.remove(out); miss.append((s,"tiny"))
    except Exception as e:
        miss.append((s,f"{type(e).__name__}"))
print("OK",len(ok)); print("MISS",miss)
