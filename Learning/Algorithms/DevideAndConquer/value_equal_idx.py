def valueEqualIndex(arr, n):
    l, h = 0, n-1
    while l <= h:
        midIdx = (l+h)//2
        mid = arr[midIdx]
        if mid == midIdx:
            return mid
        if mid > midIdx:
            h = midIdx-1
        else:
            l = midIdx+1
    return -1

print(valueEqualIndex([-10, -5, 0, 3, 7], 5))