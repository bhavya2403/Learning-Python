def findMaxSubsequence(arr):
    d = {}
    for i in arr:
        if i-1 in d and i+1 in d:
            d[i] = max(d[i-1], d[i+1]) + 1
        elif i-1 in d:
            d[i] = d[i-1] + 1
        elif i+1 in d:
            d[i] = d[i+1] + 1
        else:
            d[i] = 1

    return max(d[i] for i in d)

print(findMaxSubsequence([1, 2, 3, 2, 3, 7, 2, 1]))
