# there will be only one peak ele
def findPeak(arr, n):
    if n==1:
        return 1
    if arr[1] < arr[0]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1
    l, h = 0, n-1
    while l <= h:
        midIdx = (l+h)//2
        if midIdx==n-1:
            return n-1
        mid = arr[midIdx]
        if mid > arr[midIdx-1] and mid > arr[midIdx+1]:
            return midIdx
        if arr[midIdx-1] < mid < arr[midIdx+1]:
            l = midIdx+1
        else:
            h = midIdx-1

print(findPeak([1, 2, 4, 5, 6, 6, 8, 9], 8))
