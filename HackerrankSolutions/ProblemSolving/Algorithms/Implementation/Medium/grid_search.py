def gridSearch(R, C, r, c, G, P):
    I = 0
    while I <= R-r:
        J = 0
        while J <= C-c:
            broken = False
            if G[I][J] == P[0][0]:
                i = 0
                while i < r:
                    j = 0
                    while j < c:
                        if P[i][j] != G[I+i][J+j]:
                            broken = True
                            break
                        j += 1
                    if broken:
                        break
                    i += 1
                if not broken:
                    return 'YES'
            J += 1
        I += 1
    return 'NO'

t = int(input())

for t_itr in range(t):
    RC = input().split()

    R = int(RC[0])

    C = int(RC[1])

    G = []

    for _ in range(R):
        G_item = input()
        G.append(G_item)

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    P = []

    for _ in range(r):
        P_item = input()
        P.append(P_item)

    result = gridSearch(R, C, r, c, G, P)

    print(result)
