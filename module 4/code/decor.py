def func_show(func):
    def wrapper(*args, **kwargs):
        print(f"Площадь прямоугольника: {func(*args, **kwargs)}")
    return wrapper


# @func_show
def get_sq(a, b):
    return a*b

# =========================================================
def show_menu(func):
    def wrapper(*args, **kwargs):
        for i, j in enumerate(func(*args), 1):
            print(f'{i}. {j}')
    return wrapper


@show_menu
def get_menu(s):
    return s.split()


# =========================================================

def list_sort(func):  # декоратор для функции
    def wrapper(*args, **kwargs):  # фактические параметры, формальные параметры
        return sorted(func(*args))

    return wrapper


@list_sort  # применение декоратора
def get_list(lst):  # декорированная функция
    return list(map(int, lst.split()))


lst = get_list(input())
print(*lst)
