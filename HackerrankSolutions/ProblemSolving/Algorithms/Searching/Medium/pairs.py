def pairs(k, arr):
    d = {}
    count = 0
    for i, num in enumerate(arr):
        d[num] = i
    for i in arr:
        if i-k in d and i+k in d:
            count += 2
        elif i-k in d or i+k in d:
            count += 1
    return int(count/2)