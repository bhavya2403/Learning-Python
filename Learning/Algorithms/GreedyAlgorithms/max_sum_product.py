def maxSum(a, b, k):
    n = len(a)
    summation = 0
    maxB, minB = 0, 0
    maxIdx, minIdx = 0, 0
    for i in range(n):
        prod = a[i] * b[i]
        summation += prod
        if b[i] > maxB:
            maxB = b[i]
            maxIdx = i
        if b[i] < minB:
            minB = b[i]
            minIdx = i

    if maxB == max(maxB, -minB):
        return summation - 2 * k * b[maxIdx]
    return summation + 2 * k * b[minIdx]


print(maxSum([1, 2, -3], [-2, 3, -5], 5))
