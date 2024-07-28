import yfinance as yf
import sqlite3

conn = sqlite3.connect('stocksdata.db')
cursor = conn.cursor()

# Fetching data for a specific stock
stock = yf.Ticker("PAYTM.NS")
stock_info = stock.info

# Print stock details
#print(stock_info)
#print(stock_info.get('industry'))

stock_data = {
    'industry': stock_info.get('industry', None),
    'sector': stock_info.get('sector', None),
    'previousClose': stock_info.get('previousClose', None),
    'open': stock_info.get('open', None),
    'dayLow': stock_info.get('dayLow', None),
    'dayHigh': stock_info.get('dayHigh', None),
    'regularMarketPreviousClose': stock_info.get('regularMarketPreviousClose', None),
    'regularMarketOpen': stock_info.get('regularMarketOpen', None),
    'regularMarketDayLow': stock_info.get('regularMarketDayLow', None),
    'regularMarketDayHigh': stock_info.get('regularMarketDayHigh', None),
    'dividendRate': stock_info.get('dividendRate', None),
    'dividendYield': stock_info.get('dividendYield', None),
    'payoutRatio': stock_info.get('payoutRatio', None),
    'fiveYearAvgDividendYield': stock_info.get('fiveYearAvgDividendYield', None),
    'volume': stock_info.get('volume', None),
    'regularMarketVolume': stock_info.get('regularMarketVolume', None),
    'averageVolume': stock_info.get('averageVolume', None),
    'averageVolume10days': stock_info.get('averageVolume10days', None),
    'averageDailyVolume10Day': stock_info.get('averageDailyVolume10Day', None),
    'marketCap': stock_info.get('marketCap', None),
    'fiftyTwoWeekLow': stock_info.get('fiftyTwoWeekLow', None),
    'fiftyTwoWeekHigh': stock_info.get('fiftyTwoWeekHigh', None),
    'fiftyDayAverage': stock_info.get('fiftyDayAverage', None),
    'twoHundredDayAverage': stock_info.get('twoHundredDayAverage', None),
    'currency': stock_info.get('currency', None),
    'floatShares': stock_info.get('floatShares', None),
    'sharesOutstanding': stock_info.get('sharesOutstanding', None),
    'heldPercentInsiders': stock_info.get('heldPercentInsiders', None),
    'heldPercentInstitutions': stock_info.get('heldPercentInstitutions', None),
    'impliedSharesOutstanding': stock_info.get('impliedSharesOutstanding', None),
    'bookValue': stock_info.get('bookValue', None),
    'priceToBook': stock_info.get('priceToBook', None),
    'earningsQuarterlyGrowth': stock_info.get('earningsQuarterlyGrowth', None),
    'netIncomeToCommon': stock_info.get('netIncomeToCommon', None),
    'exchange': stock_info.get('exchange', None),
    'quoteType': stock_info.get('quoteType', None),
    'symbol': stock_info.get('symbol', None),
    'underlyingSymbol': stock_info.get('underlyingSymbol', None),
    'shortName': stock_info.get('shortName', None),
    'longName': stock_info.get('longName', None),
    'uuid': stock_info.get('uuid', None),
    'currentPrice': stock_info.get('currentPrice', None),
    'targetHighPrice': stock_info.get('targetHighPrice', None),
    'targetLowPrice': stock_info.get('targetLowPrice', None),
    'targetMeanPrice': stock_info.get('targetMeanPrice', None),
    'targetMedianPrice': stock_info.get('targetMedianPrice', None),
    'recommendationMean': stock_info.get('recommendationMean', None),
    'recommendationKey': stock_info.get('recommendationKey', None),
    'numberOfAnalystOpinions': stock_info.get('numberOfAnalystOpinions', None),
    'ebitda': stock_info.get('ebitda', None),
    'totalDebt': stock_info.get('totalDebt', None),
    'totalRevenue': stock_info.get('totalRevenue', None),
    'earningsGrowth': stock_info.get('earningsGrowth', None),
    'revenueGrowth': stock_info.get('revenueGrowth', None),
    'financialCurrency': stock_info.get('financialCurrency', None)
}

# Insert the stock data into the stocks table
cursor.execute('''
INSERT OR REPLACE INTO stocks (
    industry, sector, previousClose, open, dayLow, dayHigh, regularMarketPreviousClose, regularMarketOpen,
    regularMarketDayLow, regularMarketDayHigh, dividendRate, dividendYield, payoutRatio, fiveYearAvgDividendYield,
    volume, regularMarketVolume, averageVolume, averageVolume10days, averageDailyVolume10Day, marketCap,
    fiftyTwoWeekLow, fiftyTwoWeekHigh, fiftyDayAverage, twoHundredDayAverage, currency, floatShares,
    sharesOutstanding, heldPercentInsiders, heldPercentInstitutions, impliedSharesOutstanding, bookValue,
    priceToBook, earningsQuarterlyGrowth, netIncomeToCommon, exchange, quoteType, symbol, underlyingSymbol,
    shortName, longName, uuid, currentPrice, targetHighPrice, targetLowPrice, targetMeanPrice, targetMedianPrice,
    recommendationMean, recommendationKey, numberOfAnalystOpinions, ebitda, totalDebt, totalRevenue,
    earningsGrowth, revenueGrowth, financialCurrency
) VALUES (
    :industry, :sector, :previousClose, :open, :dayLow, :dayHigh, :regularMarketPreviousClose, :regularMarketOpen,
    :regularMarketDayLow, :regularMarketDayHigh, :dividendRate, :dividendYield, :payoutRatio, :fiveYearAvgDividendYield,
    :volume, :regularMarketVolume, :averageVolume, :averageVolume10days, :averageDailyVolume10Day, :marketCap,
    :fiftyTwoWeekLow, :fiftyTwoWeekHigh, :fiftyDayAverage, :twoHundredDayAverage, :currency, :floatShares,
    :sharesOutstanding, :heldPercentInsiders, :heldPercentInstitutions, :impliedSharesOutstanding, :bookValue,
    :priceToBook, :earningsQuarterlyGrowth, :netIncomeToCommon, :exchange, :quoteType, :symbol, :underlyingSymbol,
    :shortName, :longName, :uuid, :currentPrice, :targetHighPrice, :targetLowPrice, :targetMeanPrice, :targetMedianPrice,
    :recommendationMean, :recommendationKey, :numberOfAnalystOpinions, :ebitda, :totalDebt, :totalRevenue,
    :earningsGrowth, :revenueGrowth, :financialCurrency
)
''', stock_data)


conn.commit()

# Close the connection
conn.close()