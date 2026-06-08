pizza = 200
burger = 150
koobide = 180
jooje = 140
fish = 210
chicken = 190
rice = 100
yoghurt = 40
cokacola = 50
water = 20
soorat_hesab = 0
while True:
    menu = ["pizza","burger","koobide","jooje","fish","chicken","rice","yoghurt","cokacola","water"]
    print(menu)
    order =  input('Enter your order: ')
    if order == 'pizza':
        #soorat_hesab = sorat_hesab + pizza
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
    command = input('Do you want to continue? (yes/no): ')
    if command == 'y':
        continue
    else:
        break
print('soorat hesab:', soorat_hesab)