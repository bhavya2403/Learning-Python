def rotationCount(arr, n):
    l, h = 0, n-1
    while l <= h:
        midIdx = (l+h)//2
        if not midIdx:
            if n==1:
                return 0
            if arr[midIdx+1] < arr[midIdx]:
                return 1
            return 0
        elif midIdx==n-1:
            return n-1
        mid = arr[midIdx]
        if mid > arr[midIdx-1] and mid > arr[midIdx+1]:
            return midIdx+1
        elif mid < arr[midIdx-1] and mid < arr[midIdx+1]:
            return midIdx
        else:
            if arr[h] > arr[midIdx]:
                h = midIdx-1
            else:
                l = midIdx+1


print(rotationCount([5, 1, 2, 3, 4], 5))