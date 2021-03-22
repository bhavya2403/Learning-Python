from random import randint

def merge(arr, l, m, r):
    a, b = arr[l:m+1], arr[m+1:r+1]
    la, lb = len(a), len(b)
    i, j, k = 0, 0, l
    while i < la and j < lb:
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < la:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < lb:
        arr[k] = b[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r-l)//2

        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


arr = [randint(1,100000) for _ in range(10000)]
mergeSort(arr, 0, len(arr)-1)
print(arr)