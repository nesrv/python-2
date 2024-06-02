from math import hypot
from dataclasses import dataclass
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(a:Point, b:Point):
    """ Расстояние между двумя точками """
    return ((a.x - b.x) **  2 +(a.y - b.y) ** 2) ** 0.5

# Дан список точек
jyt

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
## Вариант 1
max_distance = 0
nul = Point(0, 0)
for i in range(len(points)):
    if max_distance < distance(nul, points[i]):
        max_distance = distance(nul, points[i])
        point_index = i
print(f"Координаты наиболее удаленной точки = "
      f"Point({points[point_index].x}, {points[point_index].y})")
## Округление значения типа float до двух десятичных разрядов
print(f'Расстояние {round(max_distance, 2)}')

## Вариант 2
max_len_line = 0
for index in range(len(points)):
    if (value := math.hypot(points[index].x, points[index].y)) > max_len_line:
        max_len_line = value
        point_index = index

print(f"Координаты наиболее удаленной точки = "
      f"Point({points[point_index].x}, {points[point_index].y})")
print(f'Расстояние {round(max_len_line, 2)}')


# Вариант 3
@dataclass
class Point:
    x: int
    y: int

    def __post_init__(self):
        self.length = hypot(self.x, self.y)


points = [Point(2, 7), Point(12, 7), Point(
    5, -2), Point(10, -16), Point(-12, 0)]

all_len = (point.length for point in points)

print(max(all_len))



# 
def __add__(self, other):
      if isinstance(self, Point) and isinstance(other,Point):
          return Point(self.x + other.x, self.y + other.y)
      else:
          return Point(self.x + other[0], self.y + other[1])

def __radd__(self, other):
    print('__radd__')
    return Point(self.x + other[0], self.y + other[1])