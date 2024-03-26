
from timeit import Timer


def factorial1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial2(n):
    if n == 0:
        return 1
    return n * factorial2(n - 1)


def factorial3(n, acc=1):
    if n <= 1:
        return acc
    return factorial3(n - 1, n * acc)


t1 = Timer("factorial1(30)", "from __main__ import factorial1")
print("one ", t1.timeit(10**5), "milliseconds")

t1 = Timer("factorial2(30)", "from __main__ import factorial2")
print("two ", t1.timeit(10**5), "milliseconds")

t3 = Timer("factorial3(30)", "from __main__ import factorial3")
print("three ", t3.timeit(10**5), "milliseconds")
