import timeit


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')
    max_x = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


p1 = Point(1, 2)
p2 = Point2D(1, 2)

p2.x
p2.y = 100

print(p2.max_x)
# pt.z = 4 # нет

# print(pt.__dict__) # нет !
print(p2.__slots__)

p2.x = 50
del p2.y
p2.y = 100

print(timeit.timeit(p1.calc))
print(timeit.timeit(p1.calc))
