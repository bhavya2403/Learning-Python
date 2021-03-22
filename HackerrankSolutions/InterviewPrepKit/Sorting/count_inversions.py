def countInversions(n, arr):
    swaps = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
            else:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps += 1
                    swapped = True

        if not swapped:
            break

    return swaps