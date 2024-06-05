def capitalization_1(deposit, persent, year):
    for _ in range(year):
        deposit += deposit * persent / 100
    return deposit


def capitalization_2(deposit, persent, year):
    return deposit * (1 + persent / 100) ** year


res = capitalization_1(1000, 5, 5)
print(res)


res2 = capitalization_2(1000, 5, 5)
print(res2)
