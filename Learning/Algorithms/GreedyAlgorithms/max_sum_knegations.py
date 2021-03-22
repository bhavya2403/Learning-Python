def maxSum(arr, k):
    n = len(arr)
    negCount = 0
    negSum, posSum = 0, 0
    negMin, posMin = -10**5, 10**5
    for i in arr:
        if i < 0:
            negCount += 1
            negSum += i
            if i > negMin:
                negMin = i
        else:
            if i < posMin:
                posMin = i
            posSum += i

    if negCount >= k:
        arr = sorted([arr[i] for i in range(n) if arr[i]<0])
        return -negSum + posSum + sum(arr[:k])
    if not (k-negCount)%2:
        return posSum - negSum
    return posSum - negSum - min(-negMin, posMin)

print(maxSum([-2,0,5,-1,2], 1))