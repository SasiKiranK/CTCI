stock_prices = []
with open('data.csv', 'r') as f:
    for row in f:
        token = row.split(',')
        day = token[0]
        price = token[1]
        stock_prices.append([day, price])
# stock_prices
for x in stock_prices:
    print(x)

stock_prices = {}
with open('data.csv', 'r') as f:
    for row in f:
        token = row.split(',')
        day = token[0]
        price = token[1]
        stock_prices[day] = price
# stock_prices
for x, y in stock_prices.items():
    print(x, y)
