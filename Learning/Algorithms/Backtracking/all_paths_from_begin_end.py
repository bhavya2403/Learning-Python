def printGrid():
    global grid, m, n

    for i in range(n):
        for j in range(m-1):
            if grid[i][j] < 10:
                print(0, end='')
            print(grid[i][j], end=' ')
        if grid[i][j+1] < 10:
            print(0, end='')
        print(grid[i][j+1])
    print("________________________")


def solve(curr, time):
    global grid, m, n, directions, count

    if curr == (n-1, m-1):
        count += 1
        printGrid()

    i, j = curr[0], curr[1]
    for (x, y) in directions:
        X, Y = i+x, j+y
        if 0 <= X < n and 0 <= Y < m:
            if not grid[X][Y]:
                grid[X][Y] = time

                solve((X, Y), time+1)

                grid[X][Y] = 0


def allPaths():
    global grid, directions, count

    count = 0
    grid = [[0 for _ in range(m)] for _ in range(n)]
    grid[0][0] = 1
    directions = [(1, 0), (0, 1), (-1, 0), (0,-1)]
    solve((0, 0), 2)
    print(count)

m = n = 5
allPaths()