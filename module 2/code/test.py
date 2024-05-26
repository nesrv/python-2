from math import hypot

# res = hypot(3,4)
# print (res)

# сортировка


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(a: Point, b: Point) -> float:
    """ Расстояние между двумя точками """
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
# Вариант 1

# https://proproprogs.ru/python_oop/python-nasledovanie-atributy-private-i-protected


class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'{self.name} в списке'

cat1 = Cat('Васька 1')
cat2 = Cat('Васька 2')


# print(cat1, cat2)
# print([cat1, cat2])


class BankAccount:
   
    def __init__(self, name, balance):  
        self.name = name
        self.balance = balance
        
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.balance + other
        elif isinstance(other, BankAccount):
            return self.balance + other.balance
        
    def __radd__(self, other):
        return self + other

    # def __str__(self) -> str:
    #     return f"{self.name} - {self.balance} руб"
    
user1 = BankAccount('Иван', 100)
user2 = BankAccount('Петр', 200)
print(user1)

print(user1+300)
print(user1 + user2)
print(400 + user1)


