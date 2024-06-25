def palindrom_1(string):
    reverse = ""
    i = len(string) - 1
    while i >= 0:
        reverse += string[i]
        i -= 1
    if string.lower() == reverse.lower():
        return True
    return False


def palindrom_2(string):
    mid = len(string) // 2
    j = len(string) - 1
    for i in range(mid):
        if string[i] != string[j]:
            return False
        j -= 1
    return True


def palindrom_3(string):
    s1 = list(string)
    s2 = s1.copy()
    s2.reverse()
    if s1 == s2:
        return True
    return False