def findEleAppearOnce(arr, n):
    l, h = 0, n-1
    while l <= h:
        if l==h:
            return arr[l]
        midIdx = (l+h)//2
        mid = arr[midIdx]
        if not midIdx%2:
            if mid == arr[midIdx+1]:
                l = midIdx
            else:
                h = midIdx-1
        else:
            if mid == arr[midIdx-1]:
                l = midIdx+1
            else:
                h = midIdx


print(findEleAppearOnce([1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8], 11))