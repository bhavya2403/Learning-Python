def missingNumbers(arr, brr):
    crr = [0] * 10000
    for i in arr:
        crr[i] -=1
    for i in brr:
        crr[i] += 1
    drr = []
    for idx in range(10000):
        if crr[idx]>0:
            drr.append(idx)
    return drr