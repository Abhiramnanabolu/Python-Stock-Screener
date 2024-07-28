import sqlite3

def check_profit_loss(table_name):
    conn = sqlite3.connect('stocksdata.db')
    cursor = conn.cursor()
    
    # Fetch investment data
    cursor.execute(f'SELECT * FROM {table_name}')
    investments = cursor.fetchall()
    
    if not investments:
        print(f"No data found in table {table_name}.")
        conn.close()
        return
    
    # Fetch current stock data
    cursor.execute('''
    SELECT symbol, currentPrice
    FROM stocks500
    ''')
    current_data = cursor.fetchall()
    current_prices = dict((symbol, current_price) for symbol, current_price in current_data)
    
    # Initialize total profit/loss
    total_investment = 0
    total_current_value = 0
    total_profit_loss = 0
    
    # Calculate profit/loss
    profit_loss = []
    for investment in investments:
        stock, currentprice, no_of_shares, total_investment_amount = investment
        current_price = current_prices.get(stock)
        if current_price is not None:
            current_value = current_price * no_of_shares
            profit_loss_amount = current_value - total_investment_amount
            profit_loss_percentage = (profit_loss_amount / total_investment_amount) * 100 if total_investment_amount != 0 else 0
            
            profit_loss.append({
                'stock': stock,
                'current_price': current_price,
                'total_investment': total_investment_amount,
                'current_value': current_value,
                'profit_loss_amount': profit_loss_amount,
                'profit_loss_percentage': profit_loss_percentage
            })
            
            # Update total values
            total_investment += total_investment_amount
            total_current_value += current_value
            total_profit_loss += profit_loss_amount
    
    # Print profit/loss details
    for pl in profit_loss:
        print(f"Stock: {pl['stock']}, Current Price: {pl['current_price']}, "
              f"Total Investment: {pl['total_investment']}, Current Value: {pl['current_value']}, "
              f"Profit/Loss: {pl['profit_loss_amount']}, Profit/Loss Percentage: {pl['profit_loss_percentage']:.2f}%")
    
    # Print total profit/loss
    if total_investment > 0:
        total_profit_loss_percentage = (total_profit_loss / total_investment) * 100
    else:
        total_profit_loss_percentage = 0
    
    print(f"\nTotal Investment: {total_investment}")
    print(f"Total Current Value: {total_current_value}")
    print(f"Total Profit/Loss: {total_profit_loss}")
    print(f"Total Profit/Loss Percentage: {total_profit_loss_percentage:.2f}%")
    
    conn.close()

if __name__ == "__main__":
    # Use the table name generated in the first script
    # For example: 'buy_20240727'
    table_name = 'buy500_20240728'  # Change to the appropriate table name
    check_profit_loss(table_name)
