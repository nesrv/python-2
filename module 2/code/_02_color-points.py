from __future__ import annotations
from math import hypot


class Point:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point: Point) -> float:
        return hypot(self.x - other_point.x, self.y - other_point.y)


def get_square(pts):
    lines = [0, 0, 0]
    lines[0] = pts[0].dist_to(pts[1])
    lines[1] = pts[1].dist_to(pts[2])
    lines[2] = pts[2].dist_to(pts[0])
    p = sum(lines) / 2
    return (p * (p - lines[0]) * (p - lines[1]) * (p - lines[2])) ** .5


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно что точек каждого цвета ровно три, но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]

red = []
green = []
for p in points:
    if p.color == 'red':
        red.append(p)
    else:
        green.append((p))


print("Площадь красного треугольника = ", get_square(red))
print("Площадь зеленого треугольника = ", get_square(green))
