def numberZeros(arr, n):
    l, h = 0, n-1
    while True:
        m = (l+h)//2
        mid = arr[m]
        if mid == 1:
            if m == n-1:
                return 0
            if arr[m+1]==0:
                return n-m-1
            l = m+1
        else:
            if m==0:
                return n
            if arr[m-1]==1:
                return n-m
            h = m-1

print(numberZeros([0,0,0,0,0,0,0,0], 8))