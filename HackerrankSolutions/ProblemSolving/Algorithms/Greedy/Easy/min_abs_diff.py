def minimumAbsoluteDifference(arr):
    arr.sort()
    minDiff = arr[1]-arr[0]
    n = len(arr)
    for i in range(n-1):
        if arr[i+1]-arr[i] < minDiff:
            minDiff = arr[i+1]-arr[i]
    return minDiff