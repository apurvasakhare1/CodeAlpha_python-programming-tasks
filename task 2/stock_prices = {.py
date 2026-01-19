stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "MSFT": 300
}

total_value = 0

print("Available stocks:", stock_prices)

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        value = stock_prices[stock] * quantity
        total_value += value
        print(f"Added {stock}: ${value}")
    else:
        print("Stock not found.")

print("Total investment value: $", total_value)
