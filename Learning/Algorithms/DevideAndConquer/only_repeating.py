def onlyRepeating(arr, n):
    lo, hi = 0, n-1
    if arr[1] == arr[lo]:
        return 1
    if arr[hi] == arr[hi-1]:
        return hi
    while True:
        midIdx = (lo+hi)//2
        mid = arr[midIdx]
        if mid == arr[midIdx-1] or mid == arr[midIdx+1]:
            return mid

        if mid == midIdx+1:
            lo = midIdx+1
        else:
            hi = midIdx - 1

print(onlyRepeating([1, 1 , 2 , 3 , 4], 5))