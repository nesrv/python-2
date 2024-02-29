from pprint import pprint



# class int:
#     def __init__(self, value):
#         self.value = 5

#     def __add__(self, value):
#         return self.value * value


# x = int(10)
# y = 20

# print(type(x))
# print (x + y)
# class int:
#     def __add__(self, other):
#         return (self * other)


# def __add__(self, y):
#     return (self * y)


# x = 2
# y = 5

# print(x+y)

# oper =

# print(int.__add__.__doc__)


class int:
    def __init__(self, value):
        self.value = value

    def __add__(self, value):
        return self.value * value


n1 = int(10)
n2 = 5

print(n1 + n2)
