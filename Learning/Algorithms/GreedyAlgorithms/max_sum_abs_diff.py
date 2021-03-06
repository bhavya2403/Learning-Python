# Given an array, we need to find the
# maximum sum of absolute difference of any permutation of the given array.

def maxSum(arr):
    arr.sort()
    n = len(arr)
    max_sum = 0
    for i in range(n//2):
        max_sum += arr[n-i-1]-arr[i]

    return 2*max_sum

print(maxSum([1,2,4,5, 8]))