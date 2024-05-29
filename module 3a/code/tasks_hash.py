
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


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __repr__(self):
        return f'Книга: "{self.name}" автор: {self.author}'

    def __hash__(self):
        return hash((self.name, self.author))

    def __eq__(self,other):
        return self.__hash__() == other.__hash__()

text = """Отцы и дети; Тургенев; 2024
Война и мир; Толстой; 2001
Братья Карамазовы; Достоевский; 1954
Война и мир; Толстой; 2022
Братья Карамазовы; Достоевский; 2024
Война и мир; Толстой; 1972"""

lst_in = text.splitlines()
lst_bs = []

for line in lst_in:
    line = line.split('; ')
    name, author, year = line
    book = BookStudy(name, author, year)
    lst_bs.append(book)


unique_books = set(lst_bs)
print(*unique_books, sep="\n")





class Dimensions:

    @staticmethod
    def check_abc(*args):
        return all(map(lambda x: x >= 0, args))

    def __init__(self, a, b, c):
        if self.check_abc(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __lt__(self, other):
        self.__hash__() < other.__hash__()

    def __repr__(self):
        return str(self.__hash__())


s = '1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5'.split('; ')
lst_dims  = [Dimensions(*map(float, x.split())) for x in s]

print(lst_dims)
lst_dims.sort(key=hash)

print(lst_dims)