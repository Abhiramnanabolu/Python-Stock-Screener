import sqlite3
from datetime import datetime

def create_and_populate_investment_table():
    # Connect to the SQLite database
    conn = sqlite3.connect('stocksdata.db')
    cursor = conn.cursor()

    # Define the percentage difference
    percentage_threshold = 0.05

    # Fetch stock data from the database, including the recommendation key
    cursor.execute('''
    SELECT symbol, currentPrice, fiftyTwoWeekHigh, recommendationKey
    FROM stocks500
    ''')

    stocks = cursor.fetchall()

    # Process each stock and collect the results
    selected_stocks = []

    for stock in stocks:
        symbol, current_price, fifty_two_week_high, recommendation_key = stock
        
        if fifty_two_week_high is not None and current_price is not None:
            # Calculate the percentage difference between the current price and the 52-week high
            percentage_diff = (fifty_two_week_high - current_price) / fifty_two_week_high
            
            # Check if current price is at least 95% of the 52-week high
            if percentage_diff <= percentage_threshold and recommendation_key == "buy":
                # Append the formatted stock information to the list
                selected_stocks.append({
                    'stockName': symbol,
                    'currentPrice': current_price
                })

    # Calculate and print shares to buy
    def calculate_and_print_shares_to_buy(selected_stocks, target_amount=10000):
        investment_data = []
        for stock in selected_stocks:
            stock_name = stock['stockName']
            current_price = stock['currentPrice']
            
            # Calculate the number of shares to buy
            num_shares = max(1, int(target_amount / current_price))
            total_investment = num_shares * current_price
            investment_data.append({
                'stock': stock_name,
                'currentprice': current_price,
                'no_of_shares': num_shares,
                'total_investment': total_investment
            })
            
            print(f"Stock: {stock_name}, Shares to buy: {num_shares}")
        
        return investment_data

    # Get today's date for table name
    today_date = datetime.now().strftime('%Y%m%d')
    table_name = f'buy500_{today_date}'

    # Create the investment table
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        stock TEXT,
        currentprice REAL,
        no_of_shares INTEGER,
        total_investment REAL
    )
    ''')

    # Insert data into the investment table
    investment_data = calculate_and_print_shares_to_buy(selected_stocks)
    cursor.executemany(f'''
    INSERT INTO {table_name} (stock, currentprice, no_of_shares, total_investment)
    VALUES (:stock, :currentprice, :no_of_shares, :total_investment)
    ''', investment_data)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_and_populate_investment_table()
