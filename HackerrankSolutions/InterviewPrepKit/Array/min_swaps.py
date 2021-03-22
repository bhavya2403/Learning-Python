def minimumSwaps(arr):
    #    size = len(arr)
    #    for i, element in enumerate(arr):
    #        arr[i] = element-i-1

    #    swaps = 0
    #    while True:
    #        if all(i==0 for i in arr):
    #            break

    #        maximum = max(arr)
    #        max_idx = arr.index(maximum)
    #        minimum = 0
    #        for i in range(max_idx+1, size):
    #            if arr[i] < minimum:
    #                minimum = arr[i]
    #                j = i
    #        min_idx = j

    #        diff = min_idx - max_idx
    #        arr[max_idx], arr[min_idx] = minimum + diff, maximum - diff
    #        swaps += 1

    #    return swaps
    d = {}
    for i, element in enumerate(arr):  # O(n)
        d[element] = i

    swaps = 0
    for i, element in enumerate(arr):  # O(n)
        if element == i + 1:
            continue
        swap_idx = d[i + 1]
        arr[swap_idx], arr[i] = arr[i], arr[swap_idx]
        d[i + 1] = i
        d[element] = swap_idx
        swaps += 1

    return swaps


print(minimumSwaps([2, 3, 4, 1, 5]))
