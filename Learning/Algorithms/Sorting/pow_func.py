def pow(x, n):
    if not n:
        return 1
    a = pow(x, int(n / 2))
    if not n%2:
        return a*a
    else:
        return x*a*a

print(pow(1000,10000))