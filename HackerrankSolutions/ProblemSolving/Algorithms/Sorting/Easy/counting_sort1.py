def countingSort(arr):
    maxim = max(arr)
    count = [0] * (maxim+1)
    for i in arr:
        count[i] += 1
    return count
