def p(p):
    y = []
    for i in p:
        y.append(p[i-1])
    #
    z = []
    for i in y:
        z.append(y[i-1])
    # [5, 1, 8, 9, 2, 12, 7, 11, 17, 16, 3, 14, 4, 6, 15, 13, 18, 10]
    return z
# [2, 5, 11, 17, 1, 14, 7, 3, 18, 13, 8, 6, 9, 12, 15, 4, 10, 16]


print(p([5,2,1,3,4]))


def permutationFunction(p):
    x = 1
    y = []
    while x <= len(p)+1:
        for j in range(1, len(p)+1):
            if x == p[p[j-1]-1]:
                y.append(j)
                break
        x += 1

    return y
# [2, 5, 11, 13, 1, 14, 7, 3, 4, 18, 8, 6, 16, 12, 15, 10, 9, 17]


print(permutationFunction([2, 5, 11, 10, 1, 14, 7, 3, 16, 9, 8, 6, 18, 12, 15, 17, 13, 4]))
