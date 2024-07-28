#FOR NIFTY500 STOCKS

#Execute this to get the data of the stocks

import yfinance as yf
import sqlite3

def fetch_and_insert_stock_data(stock_symbol, cursor):
    try:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info

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

        cursor.execute('''
        INSERT OR REPLACE INTO stocks500 (
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

    except Exception as e:
        print(f"Error fetching or inserting data for {stock_symbol}: {e}")

def main():
    stockslist=["360ONE", "3MINDIA", "ABB", "ACC", "AIAENG", "APLAPOLLO", "AUBANK", "AARTIIND", "AAVAS", "ABBOTINDIA", "ACE", "ADANIENSOL", "ADANIENT", "ADANIGREEN", "ADANIPORTS", "ADANIPOWER", "ATGL", "AWL", "ABCAPITAL", "ABFRL", "AEGISLOG", "AETHER", "AFFLE", "AJANTPHARM", "APLLTD", "ALKEM", "ALKYLAMINE", "ALLCARGO", "ALOKINDS", "ARE&M", "AMBER", "AMBUJACEM", "ANANDRATHI", "ANGELONE", "ANURAS", "APARINDS", "APOLLOHOSP", "APOLLOTYRE", "APTUS", "ACI", "ASAHIINDIA", "ASHOKLEY", "ASIANPAINT", "ASTERDM", "ASTRAZEN", "ASTRAL", "ATUL", "AUROPHARMA", "AVANTIFEED", "DMART", "AXISBANK", "BEML", "BLS", "BSE", "BAJAJ-AUTO", "BAJFINANCE", "BAJAJFINSV", "BAJAJHLDNG", "BALAMINES", "BALKRISIND", "BALRAMCHIN", "BANDHANBNK", "BANKBARODA", "BANKINDIA", "MAHABANK", "BATAINDIA", "BAYERCROP", "BERGEPAINT", "BDL", "BEL", "BHARATFORG", "BHEL", "BPCL", "BHARTIARTL", "BIKAJI", "BIOCON", "BIRLACORPN", "BSOFT", "BLUEDART", "BLUESTARCO", "BBTC", "BORORENEW", "BOSCHLTD", "BRIGADE", "BRITANNIA", "MAPMYINDIA", "CCL", "CESC", "CGPOWER", "CIEINDIA", "CRISIL", "CSBBANK", "CAMPUS", "CANFINHOME", "CANBK", "CAPLIPOINT", "CGCL", "CARBORUNIV", "CASTROLIND", "CEATLTD", "CELLO", "CENTRALBK", "CDSL", "CENTURYPLY", "CENTURYTEX", "CERA", "CHALET", "CHAMBLFERT", "CHEMPLASTS", "CHENNPETRO", "CHOLAHLDNG", "CHOLAFIN", "CIPLA", "CUB", "CLEAN", "COALINDIA", "COCHINSHIP", "COFORGE", "COLPAL", "CAMS", "CONCORDBIO", "CONCOR", "COROMANDEL", "CRAFTSMAN", "CREDITACC", "CROMPTON", "CUMMINSIND", "CYIENT", "DCMSHRIRAM", "DLF", "DOMS", "DABUR", "DALBHARAT", "DATAPATTNS", "DEEPAKFERT", "DEEPAKNTR", "DELHIVERY", "DEVYANI", "DIVISLAB", "DIXON", "LALPATHLAB", "DRREDDY", "EIDPARRY", "EIHOTEL", "EPL", "EASEMYTRIP", "EICHERMOT", "ELECON", "ELGIEQUIP", "EMAMILTD", "ENDURANCE", "ENGINERSIN", "EQUITASBNK", "ERIS", "ESCORTS", "EXIDEIND", "FDC", "NYKAA", "FEDERALBNK", "FACT", "FINEORG", "FINCABLES", "FINPIPE", "FSL", "FIVESTAR", "FORTIS", "GAIL", "GMMPFAUDLR", "GMRINFRA", "GRSE", "GICRE", "GILLETTE", "GLAND", "GLAXO", "GLS", "GLENMARK", "MEDANTA", "GPIL", "GODFRYPHLP", "GODREJCP", "GODREJIND", "GODREJPROP", "GRANULES", "GRAPHITE", "GRASIM", "GESHIP", "GRINDWELL", "GAEL", "FLUOROCHEM", "GUJGASLTD", "GMDCLTD", "GNFC", "GPPL", "GSFC", "GSPL", "HEG", "HBLPOWER", "HCLTECH", "HDFCAMC", "HDFCBANK", "HDFCLIFE", "HFCL", "HAPPSTMNDS", "HAPPYFORGE", "HAVELLS", "HEROMOTOCO", "HSCL", "HINDALCO", "HAL", "HINDCOPPER", "HINDPETRO", "HINDUNILVR", "HINDZINC", "POWERINDIA", "HOMEFIRST", "HONASA", "HONAUT", "HUDCO", "ICICIBANK", "ICICIGI", "ICICIPRULI", "ISEC", "IDBI", "IDFCFIRSTB", "IDFC", "IIFL", "IRB", "IRCON", "ITC", "ITI", "INDIACEM", "INDIAMART", "INDIANB", "IEX", "INDHOTEL", "IOC", "IOB", "IRCTC", "IRFC", "INDIGOPNTS", "IGL", "INDUSTOWER", "INDUSINDBK", "NAUKRI", "INFY", "INOXWIND", "INTELLECT", "INDIGO", "IPCALAB", "JBCHEPHARM", "JKCEMENT", "JBMA", "JKLAKSHMI", "JKPAPER", "JMFINANCIL", "JSWENERGY", "JSWINFRA", "JSWSTEEL", "JAIBALAJI", "J&KBANK", "JINDALSAW", "JSL", "JINDALSTEL", "JIOFIN", "JUBLFOOD", "JUBLINGREA", "JUBLPHARMA", "JWL", "JUSTDIAL", "JYOTHYLAB", "KPRMILL", "KEI", "KNRCON", "KPITTECH", "KRBL", "KSB", "KAJARIACER", "KPIL", "KALYANKJIL", "KANSAINER", "KARURVYSYA", "KAYNES", "KEC", "KFINTECH", "KOTAKBANK", "KIMS", "LTF", "LTTS", "LICHSGFIN", "LTIM", "LT", "LATENTVIEW", "LAURUSLABS", "LXCHEM", "LEMONTREE", "LICI", "LINDEINDIA", "LLOYDSME", "LUPIN", "MMTC", "MRF", "MTARTECH", "LODHA", "MGL", "MAHSEAMLES", "M&MFIN", "M&M", "MHRIL", "MAHLIFE", "MANAPPURAM", "MRPL", "MANKIND", "MARICO", "MARUTI", "MASTEK", "MFSL", "MAXHEALTH", "MAZDOCK", "MEDPLUS", "METROBRAND", "METROPOLIS", "MINDACORP", "MSUMI", "MOTILALOFS", "MPHASIS", "MCX", "MUTHOOTFIN", "NATCOPHARM", "NBCC", "NCC", "NHPC", "NLCINDIA", "NMDC", "NSLNISP", "NTPC", "NH", "NATIONALUM", "NAVINFLUOR", "NESTLEIND", "NETWORK18", "NAM-INDIA", "NUVAMA", "NUVOCO", "OBEROIRLTY", "ONGC", "OIL", "OLECTRA", "PAYTM", "OFSS", "POLICYBZR", "PCBL", "PIIND", "PNBHOUSING", "PNCINFRA", "PVRINOX", "PAGEIND", "PATANJALI", "PERSISTENT", "PETRONET", "PHOENIXLTD", "PIDILITIND", "PEL", "PPLPHARMA", "POLYMED", "POLYCAB", "POONAWALLA", "PFC", "POWERGRID", "PRAJIND", "PRESTIGE", "PRINCEPIPE", "PRSMJOHNSN", "PGHH", "PNB", "QUESS", "RRKABEL", "RBLBANK", "RECLTD", "RHIM", "RITES", "RADICO", "RVNL", "RAILTEL", "RAINBOW", "RAJESHEXPO", "RKFORGE", "RCF", "RATNAMANI", "RTNINDIA", "RAYMOND", "REDINGTON", "RELIANCE", "RBA", "ROUTE", "SBFC", "SBICARD", "SBILIFE", "SJVN", "SKFINDIA", "SRF", "SAFARI", "SAMMAANCAP", "MOTHERSON", "SANOFI", "SAPPHIRE", "SAREGAMA", "SCHAEFFLER", "SCHNEIDER", "SHREECEM", "RENUKA", "SHRIRAMFIN", "SHYAMMETL", "SIEMENS", "SIGNATURE", "SOBHA", "SOLARINDS", "SONACOMS", "SONATSOFTW", "STARHEALTH", "SBIN", "SAIL", "SWSOLAR", "STLTECH", "SUMICHEM", "SPARC", "SUNPHARMA", "SUNTV", "SUNDARMFIN", "SUNDRMFAST", "SUNTECK", "SUPREMEIND", "SUVENPHAR", "SUZLON", "SWANENERGY", "SYNGENE", "SYRMA", "TV18BRDCST", "TVSMOTOR", "TVSSCS", "TMB", "TANLA", "TATACHEM", "TATACOMM", "TCS", "TATACONSUM", "TATAELXSI", "TATAINVEST", "TATAMTRDVR", "TATAMOTORS", "TATAPOWER", "TATASTEEL", "TATATECH", "TTML", "TECHM", "TEJASNET", "NIACL", "RAMCOCEM", "THERMAX", "TIMKEN", "TITAGARH", "TITAN", "TORNTPHARM", "TORNTPOWER", "TRENT", "TRIDENT", "TRIVENI", "TRITURBINE", "TIINDIA", "UCOBANK", "UNOMINDA", "UPL", "UTIAMC", "UJJIVANSFB", "ULTRACEMCO", "UNIONBANK", "UBL", "UNITDSPR", "USHAMART", "VGUARD", "VIPIND", "VAIBHAVGBL", "VTL", "VARROC", "VBL", "MANYAVAR", "VEDL", "VIJAYA", "IDEA", "VOLTAS", "WELCORP", "WELSPUNLIV", "WESTLIFE", "WHIRLPOOL", "WIPRO", "YESBANK", "ZFCVINDIA", "ZEEL", "ZENSARTECH", "ZOMATO", "ZYDUSLIFE", "ECLERX"]
    conn = sqlite3.connect('stocksdata.db')
    cursor = conn.cursor()
    
    for symbol in stockslist:
        fetch_and_insert_stock_data(str(symbol)+".NS", cursor)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
