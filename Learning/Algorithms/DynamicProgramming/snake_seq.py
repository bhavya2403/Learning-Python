def snakeSequence(grid, m, n):
    for i in range(n):
        for j in range(m):
            if not i and not j:
                continue
            elif not j:
                grid[i][j] += grid[i-1][j]
            elif not i:
                grid[i][j] += grid[i][j-1]
            else:
                grid[i][j] += max(grid[i][j-1], grid[i-1][j])
    return grid[n-1][m-1]

mat = [[9, 6, 5, 2],
       [8, 7, 6, 5],
       [7, 3, 1, 6],
       [1, 1, 1, 7]]
print(snakeSequence(mat, 4, 4))