from random import shuffle

def selectionSort(arr):
    for i in range(len(arr)-1):
        min_val = 10000
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_val and arr[j]<arr[i]:
                min_val = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [i for i in range(1, 101)]
shuffle(arr)
arr.reverse()
print(selectionSort(arr))
