## Наследование. Атрибуты private и protected

как влияет режим доступа private и protected атрибутов при наследовании классов?

Ранее мы с вами об этом уже говорили и в частности отмечали, что:

`_attribute` (с одним подчеркиванием) – режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)
__attribute (с двумя подчеркиваниями) – режим доступа private (служит для обращения только внутри класса).
Давайте посмотрим, как ведут себя атрибуты с этими режимами доступа при наследовании. Возьмем пример из предыдущего занятия с двумя классами:

```python
class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f'Я точка: {self.__x} x {self.__y}'


    def move_by(self, x, y):
        self.__x += x
        self.__y += y


class Point3D(Point):

    def __init__(self, x, y, z):
        self.__z = z
        super().__init__(x, y)


    def move_by(self, x, y, z):
        self.__z = + z
        super().move_by(x, y)

    def __repr__(self):
        s = super().__repr__()
        return f'{s} x {self.__z}'


p = Point(1, 2)
print(p)
p3d = Point3D(10, 20, 30)
print(p3d)


p3d.move_by(50, 50, 50)
print(p3d)
p.move_by(50, 50)
print(p)
```