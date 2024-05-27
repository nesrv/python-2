class NewList:

    def __init__(self, lst=[]):
        self.lst = lst

    def __str__(self):
        return str(self.lst)

    def get_list(self):
        return self.lst

    def __sub__(self, other):
        lst_1 = self.lst
        lst_2 = other if type(other) == list else other.get_list()
        lst_1 = NewList.__sub_list(lst_1, lst_2)
        return NewList(lst_1)

    def __rsub__(self, other):
        return NewList(other) - self.lst

    @staticmethod
    def __sub_list(lst_1, lst_2):
        lst_1 = [(x, type(x)) for x in lst_1]
        lst_2 = [(x, type(x)) for x in lst_2]
        for x in lst_2:
            if x in lst_1:
                lst_1.remove(x)
        lst_1 = [x[0] for x in lst_1]
        return lst_1


# lst = NewList()
# lst = NewList([-1, 0, 7.56, True])
# print(lst)

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1)
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(lst1)
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print(res_2)

res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
print(res_3)
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(res_4)
