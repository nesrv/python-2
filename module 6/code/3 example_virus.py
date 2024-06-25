def counter_virus_1(n, t):
    i = 3
    while i <= t:
        n *= 2
        i += 3
    return n


def counter_virus_2(n, t):
    return n * 2 ** int(t / 3)


res1 = counter_virus_1(2, 10)
print(res1)

res2 = counter_virus_2(2, 10)
print(res2)
