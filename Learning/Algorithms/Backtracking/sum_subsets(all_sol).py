def solve(arr, n, sumOfSubset, eleTaken, sumEleTaken, sumLeft, currIdx):
    if sumEleTaken == sumOfSubset:
        print(eleTaken)
        return
    elif sumLeft < sumOfSubset - sumEleTaken:
        return

    for i in range(currIdx, n):
        if arr[i] + sumEleTaken <= sumOfSubset:
            solve(arr, n, sumOfSubset, eleTaken+[arr[i]], sumEleTaken+arr[i], sumLeft-arr[i], i + 1)
        else:
            break


def sumSubsets(arr, n, sumOfSubset):
    arr.sort()
    return solve(arr, n, sumOfSubset, [], 0, sum(arr), 0)


sumSubsets([5, 10, 12, 13, 15, 18], 6, 28)
sumSubsets([5, 10, 12, 13, 15, 18], 6, 33)
sumSubsets([5, 10, 12, 13, 15, 18], 6, 30)
