def closestNumber(arr, n, x):
    l, h = 0, n - 1
    if arr[l] >= x:
        return l
    if arr[h] <= x:
        return h
    while l <= h:
        midIdx = (l + h) // 2
        mid = arr[midIdx]
        if mid == x:
            return midIdx
        if mid > x:
            if arr[midIdx - 1] < x:
                return midIdx if mid - x < x - arr[midIdx - 1] else midIdx - 1
            h = midIdx - 1
        else:
            if arr[midIdx + 1] > x:
                return midIdx if x - mid < arr[midIdx + 1] - x else midIdx + 1
            l = midIdx + 1


print(closestNumber([1, 2, 4, 11, 12, 14, 16, 17], 8, 11))
