def partition(arr, k):
    arr.sort()
    n = len(arr)
    s = sum(arr)
    if 2*k <= n:
        return s-(2*sum(arr[:k]))
    return s-(2*sum(arr[:(n-k)]))

print(partition([8, 4, 5, 2, 10], 2))
print(partition([1, 1, 1, 1, 1, 1, 1, 1], 3))