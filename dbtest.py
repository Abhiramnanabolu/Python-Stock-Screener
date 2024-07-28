stocklist=["ABB", "ACC", "APLAPOLLO", "AUBANK", "ADANIENSOL", "ADANIENT", "ADANIGREEN", "ADANIPORTS", "ADANIPOWER", "ATGL", "ABCAPITAL", "ABFRL", "ALKEM", "AMBUJACEM", "APOLLOHOSP", "APOLLOTYRE", "ASHOKLEY", "ASIANPAINT", "ASTRAL", "AUROPHARMA", "DMART", "AXISBANK", "BSE", "BAJAJ-AUTO", "BAJFINANCE", "BAJAJFINSV", "BAJAJHLDNG", "BALKRISIND", "BANDHANBNK", "BANKBARODA", "BANKINDIA", "MAHABANK", "BERGEPAINT", "BDL", "BEL", "BHARATFORG", "BHEL", "BPCL", "BHARTIARTL", "BIOCON", "BOSCHLTD", "BRITANNIA", "CGPOWER", "CANBK", "CHOLAFIN", "CIPLA", "COALINDIA", "COFORGE", "COLPAL", "CONCOR", "CUMMINSIND", "DLF", "DABUR", "DALBHARAT", "DEEPAKNTR", "DELHIVERY", "DIVISLAB", "DIXON", "LALPATHLAB", "DRREDDY", "EICHERMOT", "ESCORTS", "NYKAA", "FEDERALBNK", "FACT", "FORTIS", "GAIL", "GMRINFRA", "GLAND", "GODREJCP", "GODREJPROP", "GRASIM", "GUJGASLTD", "HCLTECH", "HDFCAMC", "HDFCBANK", "HDFCLIFE", "HAVELLS", "HEROMOTOCO", "HINDALCO", "HAL", "HINDPETRO", "HINDUNILVR", "ICICIBANK", "ICICIGI", "ICICIPRULI", "IDBI", "IDFCFIRSTB", "ITC", "INDIANB", "INDHOTEL", "IOC", "IRCTC", "IRFC", "IGL", "INDUSTOWER", "INDUSINDBK", "NAUKRI", "INFY", "INDIGO", "IPCALAB", "JSWENERGY", "JSWINFRA", "JSWSTEEL", "JINDALSTEL", "JIOFIN", "JUBLFOOD", "KPITTECH", "KALYANKJIL", "KOTAKBANK", "LTF", "LTTS", "LICHSGFIN", "LTIM", "LT", "LAURUSLABS", "LICI", "LUPIN", "MRF", "LODHA", "M&MFIN", "M&M", "MANKIND", "MARICO", "MARUTI", "MFSL", "MAXHEALTH", "MAZDOCK", "MPHASIS", "NHPC", "NMDC", "NTPC", "NESTLEIND", "OBEROIRLTY", "ONGC", "OIL", "PAYTM", "OFSS", "POLICYBZR", "PIIND", "PAGEIND", "PATANJALI", "PERSISTENT", "PETRONET", "PIDILITIND", "PEL", "POLYCAB", "POONAWALLA", "PFC", "POWERGRID", "PRESTIGE", "PNB", "RECLTD", "RVNL", "RELIANCE", "SBICARD", "SBILIFE", "SJVN", "SRF", "MOTHERSON", "SHREECEM", "SHRIRAMFIN", "SIEMENS", "SONACOMS", "SBIN", "SAIL", "SUNPHARMA", "SUNTV", "SUPREMEIND", "SUZLON", "SYNGENE", "TVSMOTOR", "TATACHEM", "TATACOMM", "TCS", "TATACONSUM", "TATAELXSI", "TATAMTRDVR", "TATAMOTORS", "TATAPOWER", "TATASTEEL", "TATATECH", "TECHM", "TITAN", "TORNTPHARM", "TORNTPOWER", "TRENT", "TIINDIA", "UPL", "ULTRACEMCO", "UNIONBANK", "UNITDSPR", "VBL", "VEDL", "IDEA", "VOLTAS", "WIPRO", "YESBANK", "ZEEL", "ZOMATO", "ZYDUSLIFE"]
import sqlite3

conn = sqlite3.connect('stocksdata.db')
cursor = conn.cursor()

cursor.execute('''
DROP TABLE IF EXISTS stocks
''')

cursor.execute('''
CREATE TABLE stocks (
    stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
    industry TEXT,
    sector TEXT,
    previousClose REAL,
    open REAL,
    dayLow REAL,
    dayHigh REAL,
    regularMarketPreviousClose REAL,
    regularMarketOpen REAL,
    regularMarketDayLow REAL,
    regularMarketDayHigh REAL,
    dividendRate REAL,
    dividendYield REAL,
    payoutRatio REAL,
    fiveYearAvgDividendYield REAL,
    volume INTEGER,
    regularMarketVolume INTEGER,
    averageVolume INTEGER,
    averageVolume10days INTEGER,
    averageDailyVolume10Day INTEGER,
    marketCap REAL,
    fiftyTwoWeekLow REAL,
    fiftyTwoWeekHigh REAL,
    fiftyDayAverage REAL,
    twoHundredDayAverage REAL,
    currency TEXT,
    floatShares REAL,
    sharesOutstanding REAL,
    heldPercentInsiders REAL,
    heldPercentInstitutions REAL,
    impliedSharesOutstanding REAL,
    bookValue REAL,
    priceToBook REAL,
    earningsQuarterlyGrowth REAL,
    netIncomeToCommon REAL,
    exchange TEXT,
    quoteType TEXT,
    symbol TEXT NOT NULL UNIQUE,
    underlyingSymbol TEXT,
    shortName TEXT,
    longName TEXT,
    uuid TEXT,
    currentPrice REAL,
    targetHighPrice REAL,
    targetLowPrice REAL,
    targetMeanPrice REAL,
    targetMedianPrice REAL,
    recommendationMean REAL,
    recommendationKey TEXT,
    numberOfAnalystOpinions INTEGER,
    ebitda REAL,
    totalDebt REAL,
    totalRevenue REAL,
    earningsGrowth REAL,
    revenueGrowth REAL,
    financialCurrency TEXT
)
''')

conn.commit()
conn.close()
