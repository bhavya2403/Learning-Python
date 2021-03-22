def minProduct(arr):
    negCount = 0
    negMin = -10**5
    minArr = arr[0]
    multAll = 1
    for i in arr:
        if i < 0:
            negCount += 1
            if i > negMin:
                negMin = -i
        if i < minArr:
            i = minArr
        multAll *= i

    if not negCount:
        print(minArr)
    elif not negCount%2:
        print(int(multAll/negMin))
    else:
        print(multAll)
