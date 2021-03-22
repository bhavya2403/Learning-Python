def searchInSorted(arr, N, K):
    lo, hi = 0, N-1
    while lo <= hi:
        midIdx = (lo+hi) // 2
        mid = arr[midIdx]
        if mid == K:
            return 1
        if mid < K:
            lo = midIdx+1
        else:
            hi = midIdx-1
    return -1