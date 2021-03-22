def countingSort(arr):
    maxim = max(arr)
    count = [0] * (maxim + 1)
    for i in arr:
        count[i] += 1
    i = j = 0
    while i < maxim + 1:
        if count[i] == 0:
            i += 1
        else:
            arr[j] = i
            count[i] -= 1
            j += 1
    return arr
