s = '''
43
40
32
40
30
'''.strip().splitlines()
s = open('txt.txt').readlines()

s = (int(x) for x in s)
s = sorted(s, reverse=True)

res = [s.pop(0)]

while s:
    box = s.pop(0)
    if res[-1] - box >= 3:
        res.append(box)

print(len(res), res[-1])


# ==============================================

s = '''
43
40
32
40
30
'''.strip().splitlines()
# s = open('txt.txt').readlines()

all_boxes = (int(x) for x in s)
all_boxes = sorted(all_boxes, reverse=True)

all_containers = []

while all_boxes:
    container = [all_boxes.pop(0)]
    i = 0
    while i < len(all_boxes):
        if container[-1] - all_boxes[i] >= 3:
            container.append(all_boxes.pop(i))
            i -= 1
        i += 1

    all_containers.append(container)

print(all_containers)


## заявки 


s = '''
10 150
100 110
131 170
131 180
120 130
'''.strip().splitlines()

lst = (tuple(map(int, date.split())) for date in s if s)
lst = sorted(lst, key=lambda x: x[1])
print(lst)

res = [lst.pop(0)]

i = 0
while i < len(lst):
    t = lst[i]
    if t[0] >= res[-1][1]:
        res.append(t)
    i += 1

print(res)


### ==================


for i in range(1, len(lst)):
    if lst[i][0] <= res[-1][0] and lst[i][0] >= res[-2][1]:
        res[-1] = lst[i]


print(len(res), res[-1][1], res[-1], res[-2])
