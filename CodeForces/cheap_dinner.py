import sys

minCost = 10**9


def solve(s, cost, considering):
    global minCost
    if considering == 'd':
        for i in s:
            if cost + d[i] < minCost:
                minCost = cost + d[i]
    elif considering == 'c':
        for i in s:
            if cost + c[i] < minCost:
                solve(sd - cant34[i], cost + c[i], 'd')
    elif considering == 'b':
        for i in s:
            if cost + b[i] < minCost:
                solve(sc - cant23[i], cost + b[i], 'c')
    else:
        for i in s:
            if cost + a[i] < minCost:
                solve(sb - cant12[i], cost + a[i], 'b')


def takeArrInput():
    e = list(map(int, sys.stdin.readline().split()))
    return e

na, nb, nc, nd = map(int, sys.stdin.readline().split())
a = takeArrInput()
b = takeArrInput()
c = takeArrInput()
d = takeArrInput()
n = max(na, nb, nc, nd)
arr = [i for i in range(n)]

def takeInput():
    cant = {i:set() for i in range(n)}
    m = int(sys.stdin.readline())
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        x -= 1
        y -= 1
        cant[x].add(y)
    return m, cant

m1, cant12 = takeInput()
m2, cant23 = takeInput()
m3, cant34 = takeInput()

sa, sb, sc, sd = set(arr[:na]), set(arr[:nb]), set(arr[:nc]), set(arr[:nd])

solve(sa, 0, '')

if minCost == 10**9:
    sys.stdout.write(str(-1))
else:
    sys.stdout.write(str(minCost))
