def bitonicSubsequence(arr, n):
    leftInc = [i for i in arr]
    leftInc[0] = arr[0]
    rightDec = [i for i in arr]
    rightDec[n-1] = arr[n-1]

    for i in range(1, n):
        for j in range(i):
            if arr[i]>arr[j] and leftInc[i] < leftInc[j]+arr[i]:
                leftInc[i] = leftInc[j]+arr[i]

    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i]>arr[j] and rightDec[i] < rightDec[j]+arr[i]:
                rightDec[i] = rightDec[j]+arr[i]

    return max(leftInc[i]+rightDec[i]-arr[i] for i in range(n))

print(bitonicSubsequence([114, 99, 111, 85, 111, 90, 22 ,100, 17, 13, 116, 75, 5, 60, 90, 34, 57, 91, 56], 19))
