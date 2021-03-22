def swap(arr, i, j):
    for k in range(j, i, -1):
        arr[k], arr[k-1] = arr[k-1], arr[k]
    return arr

def smallestArr(arr, k):
    n = len(arr)
    for i in range(n-1):
        minLess = arr[i]
        min_idx = 0
        for j in range(i+1, min(n, i+k+1)):
            if arr[j] < minLess:
                minLess = arr[j]
                min_idx = j
        if min_idx:
            arr = swap(arr, i, min_idx)
            k -= (min_idx-i)

        if not k:
            break

    return arr


print(smallestArr([10, 7,9, 70, 54], 3))

