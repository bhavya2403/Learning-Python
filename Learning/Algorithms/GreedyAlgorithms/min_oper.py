def minOperations(a, k):
    return sum(min(a[i]%k, k-(a[i]%k)) for i in range(len(a)))

print(minOperations([4,5,6, 9], 5))