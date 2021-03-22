def nsw(n):
    if n == 0 or n==1:
        return 1

    s = [0] * (n+1)
    s[0] = 1
    s[1] = 1
    for i in range(2, n+1):
        s[i] = 2*s[i-1] + s[i-2]

    return s[n]

print(nsw(3))