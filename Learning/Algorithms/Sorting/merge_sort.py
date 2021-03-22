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

def mergeSort(arr, l, r): # T(n), space: O(nlogn)= (log(n) stacks)(n len array in each stack)
    if l < r:
        m = l + (r-l)//2

        mergeSort(arr, l, m) # T(n/2)
        mergeSort(arr, m+1, r) # T(n/2)
        merge(arr, l, m, r) # T(n)
        # T(n) = 2T(n/2) + n --> O(nlog(n))

from random import randint
arr = [randint(1, 100) for _ in range(10)]
arr.reverse()
mergeSort(arr, 0, len(arr)-1)
print(arr)
