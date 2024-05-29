class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Я точка: {self.x} x {self.y}'


class Point3D(Point):

    def __init__(self, x, y, z):
        self.z = z
        super().__init__(x, y)

    def __repr__(self):
        s = super().__repr__()
        return f'{s} x {self.z}'


p = Point(1, 2)
print(p)
p3d = Point3D(10, 20, 30)
print(p3d)


# =======================================

def move_to(self, x, y):
    self.x = x
    self.y = y

def move_to(self, x, y, z):
    self.z = z
    # Point.move_to(self,x,y)
    super().move_to(x, y)



# ==========================================
    
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Я точка: {self.x} x {self.y}'

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, x, y):
        self.x += x
        self.y += y


class Point3D(Point):

    def __init__(self, x, y, z):
        self.z = z
        super().__init__(x, y)

    def move_to(self, x, y, z):
        self.z = z
        # Point.move_to(self,x,y)
        super().move_to(x, y)

    def move_by(self, x, y, z):
        self.z = + z
        super().move_by(x, y)

    def __repr__(self):
        s = super().__repr__()
        return f'{s} x {self.z}'


p = Point(1, 2)
print(p)
p3d = Point3D(10, 20, 30)
print(p3d)

p.move_to(10, 20)
print(p)
p3d.move_to(100, 200, 300)
print(p3d)
p3d.move_by(50, 50, 50)
print(p3d)
p.move_by(50, 50)
print(p)


# =====================================

from accessify import private, protected
class Point:
    @private
    __secret = '123'
    def __init__(self, x, y):
        if self.__verify_coord(x):
            self.__x = x
        else:
            self.__x = 0
        self.__y = y

    def __repr__(self):
        return f'Я точка: {self.__x} x {self.__y}'

    @property
    def x(self):
        return self.__x

    def move_by(self, x, y):
        self.__x += x
        self.__y += y

    @private
    @classmethod
    def __verify_coord(cls, coord):
        return 0 <= coord <= 100

class Point3D(Point):

    def __init__(self, x, y, z):
        # super().__verify_coord(x) ## не работает
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
p3d = Point3D(1000, 20, 30)
print(p3d)


p3d.move_by(50, 50, 50)
print(p3d)
p.move_by(50, 50)
print(p.x)

# print(p.__class__.x)
print(dir(p))
print(p._Point__secret)
print(p._Point__x)

