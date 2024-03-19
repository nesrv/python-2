class ShopItem:

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.total = {name: [weight, price] }

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return self.hash == other.hash


lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']


shop_items = {}

for product in lst_in:
   name, info = product.split(':')
   weight, price = info.split()
   print(name, weight, price)
   prod = ShopItem(name, weight, price)
   total = 1
   if prod in shop_items:
      total += 1
      shop_items[prod] = [prod, total]
   else:
      shop_items[prod] = [prod, total]
      total = shop_items
   print(prod.name)
 












# s = '''
# Системный блок: 1500 75890.56
# Монитор Samsung: 2000 34000
# Клавиатура: 200.44 545
# Монитор Samsung: 2000 34000
# '''.strip()
# s = s.splitlines()
# s = [x.split() for x in s]

# print(s)