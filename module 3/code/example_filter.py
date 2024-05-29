lst = ("Москва", "Рязань1", "Смоленска", "Тверь2", "Томск")
b = filter(str.isalpha, lst)

def f(s):
    return s[-1] =="а"

c = filter(f, lst)
print(*b)
print(*c)