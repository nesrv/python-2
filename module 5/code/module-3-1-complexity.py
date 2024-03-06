#  # Модуль 3. Алгоритмы
# ## Сложность алгоритмов

# ### Одно решение - разные алгоритмы

# def palindrom_one(string):
    # reverse = ""
    # i = len(string)-1
    # while i >= 0:
        # reverse += string[i]
        # i -= 1
    # if string.lower() == reverse.lower():
        # return True
    # return False


# def palindrom_two(string):
    # mid = len(string) // 2
    # j = len(string) - 1
    # for i in range(mid):
        # if string[i] != string[j]:
            # return False
        # j -= 1  
    # return True


# def palindrom_three(string):
    # s1 = list(string)
    # s2 = s1.copy()
    # s2.reverse()
    # if s1 == s2:
        # return True
    # return False


# ### Есть ли разница? 

# def sum_one(n):
    # sum = 0;
    # for i in range(1, n+1):
        # sum += i
    # return sum

# def sum_two(n):
    # sum = (n * (n+1)) / 2
    # return sum



# from timeit import Timer


# t = Timer("function_name(10)", "from __main__ import function_name")

# t.timeit(number=1)



# t = Timer("sum_one(10000)", "from __main__ import sum_one")
# print('{0:.6f}'.format(t.timeit(number=1)))

# t = Timer("sum_one(100000)", "from __main__ import sum_one")
# print('{0:.6f}'.format(t.timeit(number=1)))

# t = Timer("sum_one(1000000)", "from __main__ import sum_one")
# print('{0:.6f}'.format(t.timeit(number=1)))


# t = Timer("sum_two(10000)", "from __main__ import sum_two")
# print('{0:.6f}'.format(t.timeit(number=1)))
 
# t = Timer("sum_two(100000)", "from __main__ import sum_two")
# print('{0:.6f}'.format(t.timeit(number=1)))

# t = Timer("sum_two(1000000)", "from __main__ import sum_two")
# print('{0:.6f}'.format(t.timeit(number=1)))


# ### Сложность алгоритмов


# def pow_one(base, exp):
    # result = 1
    # while exp > 0:
        # result *= base
        # exp -= 1
    # return result


# def pow_two(base, exp):
    # result = 1;
    # while exp > 0:
        # if exp % 2 == 0:
            # base *= base
            # exp //= 2
        # else:
            # result *= base
            # exp -= 1
    # return result


# ### Мини практикум
# #### Какова сложность следующих алгоритмов?

# def one(array):
#     result = 0;
#     for i in array:
#         for j in array:
#             result += i * j
#     return result

# def two(array):
#     result = 0
#     for i in array:
#         result += 1
#     for j in array:
#         result -= 1
#     return result

# def three(n):
#     while n > 0:
#         i += 2
#         n //= 2
#     return i;

# def four(n):
#     for i in range(n):
#         j = 0
#         cnt = 50*n
#         sum = 0
#         while j<cnt:
#             j += 1
#             sum += 1
#     return sum

# def five(n): 
#     for i in range(n):
#         while i % 2 != 0: 
#             print(i)
#             i -= 1 
#         print("Done")

# def six(n): 
#     for i in range(n):
#         cnt = n * n
#         for j in range(cnt):
#             if j == 4: 
#                 return -1 
#             print("Done")
