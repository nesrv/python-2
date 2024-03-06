# # Модуль 3. Алгоритмы
# ## Рекурсия

# ### Всё тот же бинарный поиск

# def binary_search(lst, key):
    # if len(lst) == 0:
        # return -1
    # else:
        # mid = len(lst) // 2
        # if lst[mid] == key:
            # return mid
        # else:
            # if key < lst[mid]:
                # return binary_search(lst[:mid], key)
            # else:  
                # return binary_search(lst[mid+1:], key)


# ### Простой пример рекурсии

# def question(message):
    # if input(message + ': ').lower() == 'всегда':
        # return
    # else:
        # print('Подумайте...')
    # question(message)

# question('Ваше кредо?')
# print("Молодец!")


# ### Алгоритм Евклида

# def gcd(a, b): 
    # if b == 0:
        # return  a 
    # return  gcd(b, a%b)


# ### Так ли хороша рекурсия? 


# def factorial1(n):
    # result = 1
    # for i in range(1, n+1):
        # result *= i
    # return result


# def factorial2(n):
    # if n == 0: 
        # return 1
    # return n * factorial2(n - 1)



# from timeit import Timer
# t1 = Timer("factorial1(100000)", "from __main__ import factorial1")
# print("one ", t1.timeit(number=1), "milliseconds")
# t1 = Timer("factorial2(50)", "from __main__ import factorial2")
# print("two ", t1.timeit(), "milliseconds") 


# def factorial3(n, acc = 1):
    # if n <= 1:
        # return acc
    # return factorial3(n - 1, n * acc)

# t1 = Timer("factorial3(50)", "from __main__ import factorial3")
# print("three ", t1.timeit(), "milliseconds")


# ### Напоследок


# def power1(base, exp):
    # result = 1
    # for i in range(exp):
        # result *= base
    # return result 

# def power2(base, exp): 
    # if exp == 0:
        # return 1 
    # return base * power2(base, exp - 1)

# def power3(base, exp): 
    # if exp == 0:
        # return 1 
    # if exp % 2 == 0:
        # return power3(base, exp / 1) ** 2
    # return base * power3(base, exp - 1)


# from timeit import Timer
# t1 = Timer("power1(2, 1000)", "from __main__ import power1")
# print("one ", t1.timeit(number=1), "milliseconds")
# t1 = Timer("power2(2, 10)", "from __main__ import power2")
# print("two ", t1.timeit(number=1), "milliseconds")
# t1 = Timer("power3(2, 10)", "from __main__ import power3")
# print("three ", t1.timeit(number=1), "milliseconds")


# ### Мини практикум
# #### Кстати, какова сложность следующих алгоритмов?

# def add(n):
#     if n == 0:
#         return 1
#     return add(n - 1) + add(n - 1)

# def add(n):
#     if n < 3:
#         return n
#     if n % 3 == 0:
#         return add(n - 1) + add(n - 2) + add(n - 3)
#     return n
