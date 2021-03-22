def stringConstruction(s):
    p = ""
    cost = 0
    for i in s:
        if i not in p:
            p += i
            cost += 1
        else:
            p += i

    return cost


print(stringConstruction('abab'))