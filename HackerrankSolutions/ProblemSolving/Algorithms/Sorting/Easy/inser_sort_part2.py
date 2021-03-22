def insertionSort2(n, arr):
    for i in range(1, n):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > anchor:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = anchor

        for k in range(n - 1):
            print(str(arr[k]), end=' ')
        print(str(arr[k + 1]))