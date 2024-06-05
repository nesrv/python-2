#####Task11

from math import hypot


class Point:
    def __init__(self, x: object, y: object) -> object:
        self.x = x
        self.y = y

    def distance(self, other):
        return hypot(self.x - other.x, self.y - other.y)


points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
dist = 0
for i in range(len(points)-1):
    dist += points[i].distance(points[i+1])
    i += 1
print('Task-11')
print('Длина ломаной = ', dist)


print('=' * 40)
print('Task-12')


####Task12
class NewList:

    def __init__(self, lst):
        self.lst = lst

    def __sub__(self, other):
        return NewList([item for item in self.lst if item not in other.lst])

    def __isub__(self, other):
        return NewList([item for item in self.lst if item not in other.lst])

    def __rsub__(self, other):
        return NewList([item for item in other if item not in self.lst or self.lst.remove(item)])

    def get_list(self):
        return self.lst


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])

res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list(), ' - res_1')
print('*'*40)
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.get_list(), ' - lst1')
print('*'*40)
#res_2 = lst2 - [0, True] # NewList: [1, 2, 3] ??????
#print(res_2.get_list())                       ????????
# res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5] ?????
# print(res_3.get_list())                           ?????
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
print(res_4.get_list(), ' - res_4')


