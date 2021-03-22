def missingNumber(arr, n):
    if n==1:
        return -1
    a, d = arr[0], arr[1]-arr[0]
    l, h = 0, n-1
    while True:
        midIdx = (l+h)//2
        mid = arr[midIdx]
        if midIdx == (mid-a)/d:
            if midIdx+1 != (arr[midIdx+1]-a)/d:
                return a + (midIdx+1)*d
            l = midIdx + 1
        else:
            if midIdx-1 == (arr[midIdx-1]-a)/d:
                return a + (midIdx)*d
            h = midIdx-1

print(missingNumber([1, 6, 11, 16, 21, 31], 6))