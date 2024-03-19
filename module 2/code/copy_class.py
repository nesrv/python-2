class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Point(self.x, self.y)

    def __repr__(self):
        return f'{self.x} {self.y}'


p1 = Point(2, 7)
p2 = Point(12, 7)


p3 = p1.copy()

print(p1, id(p1))
print(p3, id(p3))
