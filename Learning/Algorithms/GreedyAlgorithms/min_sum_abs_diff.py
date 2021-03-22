def minSum(a, b):
    return sum(abs(sorted(a)[i]-sorted(b)[i]) for i in range(len(a)))
