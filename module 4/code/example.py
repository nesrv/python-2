from time import time
from functools import lru_cache
from sys import setrecursionlimit

def test_time(fn):
    def wrapper(*args, **kwargs):
        st = time()
        res = fn(*args, **kwargs)
        dt = time() - st
        print(f"Время работы: {dt} сек")
        return res

    return wrapper


def fib_recurs(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fib_recurs(n - 2) + fib_recurs(n - 1)


# def fib_recurs(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib_recurs(n - 2) + fib_recurs(n - 1)


def fib_cicle(n):
    a, b = 1, 1
    i = 2
    while i < n:
        a, b = b, a + b
        i += 1
    return b


get_delta = test_time(fib_recurs)
res = get_delta(30)
print(res)


get_delta = test_time(fib_cicle)
res = get_delta(30)
print(res)


# =========================================
# from sys import setrecursionlimit
# from functools import lru_cache


setrecursionlimit(3000)


@lru_cache
def fib_recurs(n):
    if n == 1 or n == 2:
        return 1
    return fib_recurs(n - 2) + fib_recurs(n - 1)


#
get_delta = test_time(fib_recurs)
res = get_delta(1000)



# декор класса 

@test_time
class MyClass:
    def fib_cicle(self, n):
        a, b = 1, 1
        i = 2
        while i < n:
            a, b = b, a + b
            i += 1
        return b


#
obj = MyClass()
res = obj.fib_cicle(20)


print(res)
