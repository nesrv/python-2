### Создается проект, в котором предполагается использовать списки из целых чисел. 
class ListInteger(list):
    def __init__(self, list):
        for item in list:
            if not(isinstance(item,int)):
                raise TypeError('можно передавать только целочисленные значения')
        super().__init__(list)

    def __setitem__(self,index, item):
        if isinstance(item, int):
            super().__setitem__(index, item)
        else:
            raise TypeError('можно передавать только целочисленные значения')

    def append(self, item):
        if isinstance(item, int):
            super().append(item)
        else:
            raise TypeError('можно передавать только целочисленные значения')


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
try:
    s[0] = 10.5
except TypeError as e:
    print(e)
try:
    s.append(10.5)
except TypeError as e:
    print(e)
try:
    b = ListInteger((1.5, 2, 3))
except TypeError as e:
    print(e)
try:
    b = ListInteger(("девять", 2, 3))
except TypeError as e:
    print(e)
try:
    b = ListInteger(("9", 2, 3))
except TypeError as e:
    print(e)