class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y

p = Point(3, 4)

print(bool(p))
print(len(p))

p = Point(0, 0)
print(bool(p))