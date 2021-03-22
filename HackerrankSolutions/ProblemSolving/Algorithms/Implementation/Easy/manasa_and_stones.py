def stones(n, a, b):
    arr = []
    if a == b:
        return [(n-1)*a]
    (a, b) = (min(a,b), max(a, b))
    for i in range(n):
        arr.append((a * (n - i - 1)) + (b * i))

    return arr

print(stones(5, 2, 3))
