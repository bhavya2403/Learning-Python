def floorInSorted(arr, n, x):
    l, h = 0, n - 1
    if arr[l] > x:
        return -1
    if arr[h] <= x:
        return h
    while l <= h:
        midIdx = (l + h) // 2
        mid = arr[midIdx]
        if mid == x:
            return midIdx
        if mid > x:
            if arr[midIdx - 1] < x:
                return midIdx - 1
            h = midIdx - 1
        else:
            l = midIdx + 1
    return -1


print(floorInSorted([1, 2, 3, 4, 5, 7, 9], 7, 8))
