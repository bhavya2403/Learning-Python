def cavityMap(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i != 0 and j != 0 and i != len(grid) - 1 and j != len(grid) - 1:
                k = grid[i][j]
                if k > grid[i - 1][j] and k > grid[i + 1][j] and k > grid[i][j - 1] and k > grid[i][j + 1]:
                    arr = [k for k in grid[i]]
                    arr[j] = 'X'
                    s = ''
                    for k in arr:
                        s += k
                    grid[i] = s

    return grid