class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self._name = name
        self.__verify_weight(weight)
        self._weight = weight

    def get_attrs(self):
        return tuple(self.__dict__.values())
    def __verify_name(self, name):
        if type(name) == str:
            return
        else:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if weight > 0:
            return
        else:
            raise TypeError('вес должен быть положительным числом')

class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
print(chair.get_attrs())

# -----------------------


class Furniture:
    _attrs = ('_name', '_weight')
    def __init__(self, *args):
        for atr_name, val in zip(self._attrs, args):
            setattr(self, atr_name, val)

    def __verify_name(self, name):
        if type(name) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if type(weight) not in (float, int) or weight < 0:
            raise TypeError('вес должен быть положительным числом')


    def get_attrs(self):
        return tuple(self.__dict__.values())

class Closet(Furniture):
    _attrs = ('_name', '_weight', '_tp', '_doors')

class Chair(Furniture):
    _attrs = ('_name', '_weight', '_height')

class Table(Furniture):
    _attrs = ('_name', '_weight', '_height', '_square')