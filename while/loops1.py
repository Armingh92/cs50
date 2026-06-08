# coke.py
payable_price = 50
coins = [5, 10, 25]
paid = 0

while payable_price > 0:
    print(f"Amount Due: {payable_price}")
    coin = int(input("insert coin: "))
    if  coin in coins:
        payable_price = payable_price-coin
        paid = paid+coin
    else:
        continue

print(f"Change Owed: {abs(payable_price-paid)}")