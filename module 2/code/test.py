from math import hypot

res = hypot(3,4)
print (res)

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
