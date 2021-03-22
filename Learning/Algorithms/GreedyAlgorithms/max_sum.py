# maximize arr[i] * i
def maxSum(arr):
    return sum(sorted(arr)[i]*i for i in range(len(arr)))

