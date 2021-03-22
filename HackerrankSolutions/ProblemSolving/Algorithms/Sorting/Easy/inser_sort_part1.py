def insertionSort1(n, arr):
    anchor = arr[n - 1]
    i = n - 2
    while i >= 0 and arr[i] > anchor:
        arr[i+1] = arr[i]
        i -= 1
        for j in range(n-1):
            print(str(arr[j]), end=' ')
        print(str(arr[j+1]))
    arr[i+1] = anchor
    for j in range(n - 1):
        print(str(arr[j]), end=' ')
    print(str(arr[j + 1]))