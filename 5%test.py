import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('stocksdata.db')
cursor = conn.cursor()

# Define the percentage difference
percentage_threshold = 0.05

# Fetch stock data from the database, including the recommendation key
cursor.execute('''
SELECT symbol, currentPrice, fiftyTwoWeekHigh, recommendationKey
FROM stocks
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
            # Append the stock information as an object to the list
            selected_stocks.append({
                'symbol': symbol,
                'currentPrice': current_price,
                'fiftyTwoWeekHigh': fifty_two_week_high,
                'percentageDiff': percentage_diff * 100,
                'recommendationKey': recommendation_key
            })

# Print the number of selected stocks
print(len(selected_stocks))

# Print the collected stock information
for stock_info in selected_stocks:
    print(f"Stock: {stock_info['symbol']}, Current Price: {stock_info['currentPrice']}, "
          f"52-Week High: {stock_info['fiftyTwoWeekHigh']}, Difference: {stock_info['percentageDiff']:.2f}%, "
          f"Recommendation Key: {stock_info['recommendationKey']}")

# Function to calculate and print the number of shares to buy
def calculate_and_print_shares_to_buy(selected_stocks, target_amount=10000):
    for stock in selected_stocks:
        symbol = stock['symbol']
        current_price = stock['currentPrice']
        
        if current_price == 0:
            num_shares = 0
        else:
            num_shares = int(target_amount / current_price)
        
        print(f"Stock: {symbol}, Shares to buy: {num_shares}")

# Call the function to calculate shares to buy
calculate_and_print_shares_to_buy(selected_stocks)

# Close the database connection
conn.close()
