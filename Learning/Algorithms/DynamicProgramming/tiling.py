# given 3*n board, find ways to fill it with 2*1 tiles

def A(n):
    global memA, memB

    if n==1:
        return 0

    if not memA[n-2]:
        memA[n-2] = A(n-2)
    if not memB[n-1]:
        memB[n-1] = B(n-1)

    memA[n] = memA[n-2] + 2*memB[n-1]
    return memA[n]

def B(n):
    global memA, memB

    if n==0:
        return 0

    if not memA[n-1]:
        memA[n-1] = A(n-1)
    if not memB[n-2]:
        memB[n-2] = B(n-2)

    memB[n] = memA[n-1] + memB[n-2]
    return memB[n]


def tiling(n):
    global memA, memB

    memA = memB = [0] * (n+1)
    memB[1] = 1
    memA[0] = 1

    return A(n)

print(tiling(8))