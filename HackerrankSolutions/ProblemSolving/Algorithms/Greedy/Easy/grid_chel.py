def gridChallenge(n, m, grid):
    for i in range(n):
        grid[i] = sorted(grid[i])
    for i in range(m):
        for j in range(n-1):
            if grid[j+1][i] < grid[j][i]:
                return False
    return True

for _ in range(int(input())):
    n = int(input())
    grid = []
    for _ in range(n):
        s = input()
        grid.append(s)
    print(gridChallenge(n, len(grid[0]), grid))