#if the schema is disturebed run thhe following code to the dlete thr table and create a new table for nifty500 stocks

import sqlite3

conn = sqlite3.connect('stocksdata.db')
cursor = conn.cursor()

cursor.execute('''
DROP TABLE IF EXISTS stocks500
''')

cursor.execute('''
CREATE TABLE stocks500 (
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
