def solve(x, y):
    global transferTime, makingTime, mem

    if not mem[x][y]:
        mem[x][y] = makingTime[x][y] + min(solve(x,y-1), solve(not x, y-1)+transferTime[not x][y])

    return mem[x][y]


def assemblyLine(e1, e2, x1, x2, n):
    global mem, transferTime, makingTime

    mem = [[0]*n, [0]*n]
    mem[0][0], mem[1][0] = e1+makingTime[0][0], e2 + makingTime[1][0]

    return min(solve(0, n-1)+x1, solve(1, n-1)+x2)

makingTime = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
transferTime = [
    [0, 7, 4, 5],
    [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]

print(assemblyLine(e[0], e[1], x[0], x[1], 4))
