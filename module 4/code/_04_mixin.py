from pprint import pprint


class Point:
    def __init__(self, x, y):
        print(2)
        # super().__init__()

    def __repr__(self):
        return f'Я точка'

class MixinLog:
    def __init__(self):
        print(3)
        print(f"Инициализация миксина")

    def hello(self):
        print(f"вызов миксин-метода")


class Point3D(Point, MixinLog):
    def __init__(self, x, y, z):
        print(1)
        self.__z = z
        super().__init__(x, y)

    def __repr__(self):
        return f'Я 3D-точка'


p = Point3D(1, 2 ,3)
pprint(Point3D.__mro__)
# print(p)