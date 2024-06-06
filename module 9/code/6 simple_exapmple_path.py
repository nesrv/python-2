def f(x, y):
    if x > y:
       return
    if x == y:
        print(x, 'ok')
    else:
        print(x, end='-->')
        return f(x + 1, y) , f(x + 2, y) , f(x * 2, y)

print(f(3, 6))
