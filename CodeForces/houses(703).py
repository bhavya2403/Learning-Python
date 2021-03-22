import sys

def solve(houses):
    xS = []
    yS = []
    for x, y in houses:
        xS.append(x)
        yS.append(y)
    xS.sort()
    yS.sort()
    n = len(xS)
    c1 = 0
    if not n%2:
        c1 +=  xS[n//2]-xS[n//2-1]+1
    else:
        c1 = 1
    n = len(yS)
    c2 = 0
    if not n%2:
        c2 +=  yS[n//2]-yS[n//2-1]+1
    else:
        c2 = 1
    return c1*c2

t = int(sys.stdin.readline())

for i in range(t):
    que = int(sys.stdin.readline())
    houses = []
    for _ in range(que):
        x, y = map(int, sys.stdin.readline().split())
        houses.append((x, y))

    print(solve(houses))