def findMaxSum(arr):
    n = len(arr)
    if n==1:
        return arr[0]
    if n==2:
        return arr[0]+arr[1]
    if n==3:
        return max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2])

    a, b, c = arr[0], arr[0]+arr[1], max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2])
    d = max(c, b+arr[3], a+arr[2]+arr[3])
    for i in range(4, n):
        a, b, c = b, c, d
        d = max(c, b+arr[i], a+arr[i]+arr[i-1])

    return d

print(findMaxSum([100, 1000, 100, 1000, 1]))
