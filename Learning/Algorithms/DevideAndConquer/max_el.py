def maxElement(arr, n):
    if n==1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]

    l, h = 0, n-1
    while True:
        midIdx = (l+h)//2
        mid = arr[midIdx]
        if mid > arr[midIdx-1] and mid > arr[midIdx+1]:
            return mid
        elif arr[midIdx-1] < mid < arr[midIdx+1]:
            l = midIdx+1
        else:
            h = midIdx-1


print(maxElement([8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1], 11))