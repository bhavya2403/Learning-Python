def maxSumIS(arr, n):
    leftInc = [i for i in arr]
    leftInc[0] = arr[0]

    max = arr[0]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and leftInc[i] < leftInc[j] + arr[i]:
                leftInc[i] = leftInc[j] + arr[i]
        if leftInc[i] > max:
            max = leftInc[i]
    return max