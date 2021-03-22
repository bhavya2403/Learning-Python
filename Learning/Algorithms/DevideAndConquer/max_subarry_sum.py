def crossingMid(arr, l, r, m):
    lSum = rSum = -10**4
    summation = 0
    for i in range(m, l-1, -1):
        summation += arr[i]
        if summation > lSum:
            lSum = summation

    summation = 0
    for i in range(m, r+1):
        summation += arr[i]
        if summation > rSum:
            rSum = summation

    return max(lSum, rSum, lSum+rSum-arr[m])

def maxSubSum(arr, l, r):  # T(n) --> O(nlog(n))
    if l==r:
        return arr[l]

    m = (l+r)//2

    a = maxSubSum(arr, l, m)  # T(n/2)
    b = maxSubSum(arr, m+1, r)  # T(n/2)
    c = crossingMid(arr, l, r, m)  # O(n)
    return max(a, b, c)

print(maxSubSum([-2, -5, 6, -2, -3, 1, 5, -6], 0, 7))