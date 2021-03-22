def twoPluses(n, m, grid):
    already = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G':
                area = 1
                x = 1
                already1 = [(i, j)]
                already.append([1, [(i, j)]])
                while i + x < n and i-x >= 0 and j + x < m and j - x >= 0:
                    if grid[x + i][j] == grid[i - x][j] == grid[i][j + x] == grid[i][j - x] == 'G':
                        area += 4
                        already1.append((x+i, j))
                        already1.append((i-x, j))
                        already1.append((i, j+x))
                        already1.append((i, j-x))
                        already.append([area, already1.copy()])
                    else:
                        break
                    x += 1

    result = 0
    for i in range(len(already)-1):
        for j in range(i+1, len(already)):
            if (len(set(already[i][1]).intersection(set(already[j][1]))) == 0) & (already[i][0] * already[j][0] > result):
                result = already[i][0] * already[j][0]
    return result

nm = input().split()

n = int(nm[0])

m = int(nm[1])

grid = []

for _ in range(n):
    grid_item = input()
    grid.append(grid_item)

print(twoPluses(n, m, grid))