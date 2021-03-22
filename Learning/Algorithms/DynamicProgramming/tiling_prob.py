def tiling(n):
    if n==1 or n==2:
        return n
    a, b = 2,1
    for i in range(3, n+1):
        a, b = a+b, a
    return a

print(tiling(4))