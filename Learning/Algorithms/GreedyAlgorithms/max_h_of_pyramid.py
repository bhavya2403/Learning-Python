from math import sqrt
def maxHeight(n, arr):
    return int((sqrt(8*n+1)-1)/2)

print(maxHeight(14, [1 for _ in range(14)]))