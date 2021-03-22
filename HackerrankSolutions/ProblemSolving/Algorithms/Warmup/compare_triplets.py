def compareTriplets(a, b):
    ar = []
    score1 = 0
    score2 = 0

    for i in range(3):
        if a[i] > b[i]:
            score1 += 1
        elif a[i] < b[i]:
            score2 += 1

    ar.append(score1)
    ar.append(score2)

    return ar
