def partition(arr, l, r):
    pivotIdx = l
    pivot = arr[l]
    l += 1
    while l < r:
        while pivot >= arr[l] and l<len(arr):
            l += 1
        while pivot <= arr[r] and r>0:
            r -= 1

        if l < r:
            arr[l], arr[r] = arr[r], arr[l]

    arr[pivotIdx], arr[r] = arr[r], arr[pivotIdx]
    return r

def quickSort(arr, l, r):
    if l< r:

        pi = partition(arr, l, r)
        quickSort(arr, l, pi-1)
        quickSort(arr, pi+1, r)

from random import randint
arr = [randint(1, 100) for _ in range(10)]
quickSort(arr, 0, 9)
print(arr)