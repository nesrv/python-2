from time import time


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
