def getMoneySpent(keyboards, drives, b):
    ar = []
    for indK in range(len(keyboards)):
        for indD in range(len(drives)):
            sum = keyboards[indK] + drives[indD]
            if sum <= b:
                ar.append(sum)

    if len(ar) == 0:
        return -1
    else:
        return max(ar)


print(getMoneySpent([3,1], [5,8,2], 10))
