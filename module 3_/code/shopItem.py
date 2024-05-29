
class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other) :
        return hash(self) == hash(other)
    
    def __repr__(self) -> str:
        return f'{ self.name}'



lst = '''Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000'''


lst = lst.splitlines()
# print (lst)

# shop_items = {}

# for item in lst:
#     name, weight, price = item.rsplit(maxsplit=2)    
#     obj = ShopItem(name[:-1], weight, price)
#     shop_items[obj] = [obj]
#     print(obj)
#     # shop_items.setdefault(obj, [obj, 0])[1] += 1



shop_items = dict()
for line in lst:
    name, weight, price = line.rsplit(maxsplit=2)
    # *name, weight, price = line.split()
    elem = ShopItem(name[:-1], weight, price)
    if elem in shop_items:
        shop_items[elem][-1] += 1
    else:
        shop_items[elem] = [elem, 1]


print(shop_items)