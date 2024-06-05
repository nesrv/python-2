

import time
from random import randint
from math import ceil


a, b = 0, 100

print("Я загадал", x := randint(a, b))

## тупой поиск

while (y := randint(a, b)) != x:
    print(y)
    time.sleep(0.1)

print(y)


# бинарный поиск

# ======================================

print("Я загадал", x := 3)
y = (b - a) // 2

while x != y:
    print(a, b, '->', y)
    if x < y:
        b = y - 1

    else:
        a = y

    y = a + ceil((b - a) / 2)
    time.sleep(0.5)

print(y)

# ======================================

a, b = 0, 1000

print("Я загадал", x := 3)

while x != (y := a + ceil((b - a) / 2)):
    print(a, b, '->', y)
    if x < y:
        b = y - 1
    else:
        a = y
    time.sleep(0.5)

print(y)
