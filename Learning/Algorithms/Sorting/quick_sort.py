def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]
    l, r = start, end
    while l < r:
        while arr[l] <= pivot and l < end:
            l += 1
        while arr[r] >= pivot and r > start:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index]

    return r # here end is the position where pivot was swapped


def quick_sort(arr, start, end): # Best case: O(nlog(n)) but in worse case(when arr already sorted)-O(n*n)
    # space: not an aux array but O(log(n)) to O(n) stacks, best case, worst case
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)

    return arr


from random import randint
for _ in range(100):
    arr = [randint(1, 10000) for _ in range(1000)]
    arr1 = sorted(arr)
    print(quick_sort(arr, 0, 999) == arr1)
