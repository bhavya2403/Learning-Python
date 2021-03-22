# not done yet


def solve(houses, ABlist, BAlist, Wlist):
    ttPair, tanks, taps = set(), [], []
    for i in range(1, houses+1):
        if i not in ABlist:
            if BAlist[i] not in BAlist:
                ttPair.add((BAlist[i], i))
            else:
                taps.append( ( i, Wlist[(BAlist[i], i)] ) )
        elif i not in BAlist:
            if ABlist[i] not in ABlist:
                ttPair.add((i, ABlist[i]))
            else:
                tanks.append(i)

    print(len(tanks)+len(ttPair))
    for a, b in ttPair:
        print(a, b, Wlist[(a,b)])

    for _ in range(len(tanks)):
        tank = tanks.pop()
        tap, dia = taps.pop()
        print(tank, tap, dia)


for _ in range(int(input())):
    houses, pipes = map(int, input().split())
    ABlist, BAlist, Wlist = {}, {}, {}
    for _ in range(pipes):
        a, b, dia = map(int, input().split())
        ABlist[a] = b
        BAlist[b] = a
        Wlist[(a, b)] = dia
    solve(houses, ABlist, BAlist, Wlist)
