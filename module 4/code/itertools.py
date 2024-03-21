from itertools import *
alphabet = '1234'
ap = []
for i in product(alphabet, repeat=5):
    if i.count('1') == 2:
        ap.append(i)
print(len(ap))

# =========================================================

from itertools import product
count = 0
for p in product("ПЯТНИЦА", repeat=5):
    if p.count("Я") == 1 and p[0]!="Н":
        count+=1
print(count)


# =========================================================

alphabet = "ГОД"
con = "ГД"
ar = product(alphabet, repeat=6)  # Размещение с повторением
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    if e[0] in con:
        count += 1
print(count)


# =========================================================

all_list = [[1, 3, 4], [6, 7, 9], [8, 10, 5]]
print("The original lists are : " + str(all_list))
res = list(product(*all_list))
print("All possible permutations are : " + str(res))
