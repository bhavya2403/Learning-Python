# P(n) = P(P(n - 1)) + P(n - P(n - 1))

def P(n):
    global mem

    if not mem[n]:
        a = P(n-1)
        mem[n] = P(a) + P(n-a)

    return mem[n]

def nc(n):
    global mem

    mem = [0] * (n+2)
    mem[2] = mem[1] = 1
    return P(n+1)

print(nc(20))