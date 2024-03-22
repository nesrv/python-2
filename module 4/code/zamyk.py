
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


def parse(tp):
  def convert(str):
    str = map(int, str.split())
    return list(str) if tp == 'list' else tuple(str)
  return convert


tip = 'list'
s = '-5 6 8 11 0 111 -456 3'
parser = parse(tip)
print(parser(s))


# ========================================================

def parse(tp):
    def convert(str):
        str = list(map(int, str.split()))
        return eval(f'{tp}({str})')
    return convert


# =========================

s = "[1,2,3,4,5]"


# res = eval('4+5*10-30')


res = eval(s)
print(res)
