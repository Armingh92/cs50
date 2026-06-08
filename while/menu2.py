pizza = 200
burger = 160
koobide = 180
jooje = 170
fish = 210
chicken = 190
rice = 100
yoghurt = 40
cokacola = 50
water = 20
soorat_hesab = 0
payable_price = soorat_hesab
coins = [100,50,200,10,20]
aid = 0
while True:
    menu = ["pizza","burger","koobide","jooje","fish","chicken","rice","yoghurt","cokacola","water"]
    print(menu)
    order = input('Enter your order: ')
    if order == 'pizza':
        soorat_hesab += pizza
    elif order == 'burger':
        soorat_hesab += burger
    elif order == 'koobide':
        soorat_hesab += koobide
    elif order == 'jooje':
        soorat_hesab += jooje
    elif order == 'fish':
        soorat_hesab += fish
    elif order == 'chicken':
        soorat_hesab += chicken
    elif order == 'rice':
        soorat_hesab += rice
    elif order == 'yoghurt':
        soorat_hesab += yoghurt
    elif order == 'cokacola':
        soorat_hesab += cokacola
    elif order == 'water':
        soorat_hesab += water
    else:
        print('invalid order')
    command = input('Do you want to continue? (y/n): ')
    if command == 'y':
        continue
    else:
        print('soorat_hesab:', soorat_hesab)
        print(f"Amount Due: {payable_price}")
        coin = int(input("insert coin: "))
    if coin in coins:
        payable_price = payable_price-coin
        paid = soorat_hesab-coin
    if soorat_hesab  == 0:
        break
    else:
        continue
print(f"Change Owed: {abs(payable_price )}")
