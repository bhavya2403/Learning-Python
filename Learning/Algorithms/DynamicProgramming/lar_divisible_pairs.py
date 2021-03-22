def largestDivisiblePairsSubset(arr):
    arr.sort()
    d = {}

    for i in arr:
        larLen, idx = 0, 0
        for j in d:
            if not i%j:
                if len(d[j]) > larLen:
                    larLen = len(d[j])
                    idx = j
        if not idx:
            d[i] = [i]
        else:
            d[i] = d[idx]+[i]

    maxLen, idx = 0, 0
    for i in d:
        if len(d[i]) > maxLen:
            maxLen = len(d[i])
            idx = i
    return d[idx]


print(largestDivisiblePairsSubset([18, 1, 3, 6, 13, 17]))