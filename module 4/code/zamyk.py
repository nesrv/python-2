
def counter_add():
    def step(cnt):
        return cnt + 5

    return step


k = int(input())
f = counter_add()
print(f(k))


# =========================================================

def counter_add(n):
    def add(cnt):
        return cnt + n

    return add


k = int(input())
f = counter_add(2)
print(f(k))


# =========================================================

def f1():
    def f2(s):
        return f'<h1>{s}</h1>'

    return f2


s = input()
f = f1()
print(f(s))

# =========================================================

def parse(tp='list'):
    def inner(s):
        return (tuple, list)[tp == 'list'](map(int, s.split()))
    return inner


pr = parse(input())
print(pr(input()))
