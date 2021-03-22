import math

def merge_two_sorted(ini, a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    k = ini
    while i < len_a and j < len_b:
        if a[i] >= b[j]:
            arr[k] = b[j]
            j += 1
            k += 1
        else:
            arr[k] = a[i]
            i += 1
            k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

def merge_sort_iterative(arr):
    size = len(arr)
    i = 1
    till = int((math.log2(size)+1))
    count = 1
    while count <= till: # O(logn)
        j = 0
        while j <= size-i: # O(n)
            merge_two_sorted(j, arr[j:j+i], arr[j+i:j+i+i], arr)
            j += 2*i
        i = 2*i
        count += 1
    return arr

arr = [i for i in range(10001)]
arr.reverse()
print(merge_sort_iterative(arr))
