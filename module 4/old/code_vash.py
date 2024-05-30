from pprint import pprint
from timeit import timeit


class MyClass:
    ...

A = MyClass()
B = MyClass()
C = MyClass()

def hello1():
     print ('hello1')


def hello2():
    print('hello2')

# A.say = hello1
# B.say = hello2
#
#
# print(A.say())
# print(MyClass.say())


import dis

# print(dis.dis(A.say.__code__))

# # pprint(globals())
#
# pprint(dis.dis('pow(3,89)'))
# pprint(dis.dis('3**89'))
#
# timeit 'print("Hello from AskPython")'

# print(timeit.timeit '3**89')
# print(timeit 'pow(3,89)')

import gc
gc.collect()
pprint (gc.get_stats())

print (callable((hello1)))



#реализовать сложение списка со строкой
