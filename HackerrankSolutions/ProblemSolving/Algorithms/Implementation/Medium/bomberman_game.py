# submit this solution in pypy3(it is giving TLE in python3)

def bomberMan(r, c, n, grid):
    if n == 1:
        return grid
    if n % 4 == 2 or n % 4 == 0:
        return ['O' * c] * r

    grid1 = []
    for i in range(r):
        grid1.append([])
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                grid1[i] += '.'
            else:
                grid1[i] += 'O'

    exploded = []
    for i in range(r):
        for j in range(c):
            if grid1[i][j] == '.' and (i, j) not in exploded:
                if i - 1 >= 0:
                    if grid1[i - 1][j] == 'O':
                        grid1[i - 1][j] = '.'
                        exploded.append((i - 1, j))
                if i + 1 < r:
                    if grid1[i + 1][j] == 'O':
                        grid1[i + 1][j] = '.'
                        exploded.append((i + 1, j))
                if j - 1 >= 0:
                    if grid1[i][j - 1] == 'O':
                        grid1[i][j - 1] = '.'
                        exploded.append((i, j - 1))
                if j + 1 < c:
                    if grid1[i][j + 1] == 'O':
                        grid1[i][j + 1] = '.'
                        exploded.append((i, j + 1))
    if n % 4 == 3:
        for i in range(r):
            s = ''
            for j in range(c):
                s += grid1[i][j]
            grid1[i] = s
        return grid1

    grid2 = []
    for i in range(r):
        grid2.append([])
    for i in range(r):
        for j in range(c):
            if grid1[i][j] == 'O':
                grid2[i] += '.'
            else:
                grid2[i] += 'O'

    exploded = []
    for i in range(r):
        for j in range(c):
            if grid2[i][j] == '.' and (i, j) not in exploded:
                if i - 1 >= 0:
                    if grid2[i - 1][j] == 'O':
                        grid2[i - 1][j] = '.'
                        exploded.append((i - 1, j))
                if i + 1 < r:
                    if grid2[i + 1][j] == 'O':
                        grid2[i + 1][j] = '.'
                        exploded.append((i + 1, j))
                if j - 1 >= 0:
                    if grid2[i][j - 1] == 'O':
                        grid2[i][j - 1] = '.'
                        exploded.append((i, j - 1))
                if j + 1 < c:
                    if grid2[i][j + 1] == 'O':
                        grid2[i][j + 1] = '.'
                        exploded.append((i, j + 1))

    for i in range(r):
        s = ''
        for j in range(c):
            s += grid2[i][j]
        grid2[i] = s
    return grid2


rcn = input().split()

r = int(rcn[0])

c = int(rcn[1])

n = int(rcn[2])

grid = []

for _ in range(r):
    grid_item = input()
    grid.append(grid_item)

print(bomberMan(r, c, n, grid))

