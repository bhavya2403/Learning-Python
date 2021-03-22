def isMajority(arr, n, x):
    l, h = 0, n - 1
    if arr[l] > x or arr[h] < x:
        return False
    while l <= h:
        if arr[l] == x:
            if l + (n // 2) > n - 1:
                return False
            if arr[l + (n // 2)] != x:
                return False
            return True
        midIdx = (l + h) // 2
        mid = arr[midIdx]
        if mid > x:
            h = midIdx - 1
        elif mid == x:
            if arr[midIdx - 1] != x:
                l = midIdx
            else:
                l = midIdx - 1
        else:
            l = midIdx + 1
    return False

# print(isMajority([2,2,3,3,3,3], 6, 3))
