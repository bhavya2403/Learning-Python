grid = []
tileNo = 1

def solve(i, j, lByTwo, p):
    global grid, tileNo

    filled = {4:(i+lByTwo, j+lByTwo),
              2:(i+lByTwo-1, j+lByTwo),
              3:(i+lByTwo, j+lByTwo-1),
              1:(i+lByTwo-1, j+lByTwo-1)}
    assigned = {
        4: grid[i + lByTwo][j + lByTwo],
        2: grid[i+lByTwo-1][j+lByTwo],
        3: grid[i + lByTwo][j + lByTwo - 1],
        1: grid[i + lByTwo - 1][j + lByTwo - 1]
    }
    grid[i+lByTwo][j+lByTwo] = tileNo
    grid[i+lByTwo-1][j+lByTwo] = tileNo
    grid[i+lByTwo][j+lByTwo-1] = tileNo
    grid[i+lByTwo-1][j+lByTwo-1] = tileNo

    if p[0]<i+lByTwo:
        if p[1]<j+lByTwo:
            part = 1
        else:
            part = 2
    else:
        if p[1]<j+lByTwo:
            part = 3
        else:
            part = 4

    if part==1:
        grid[i + lByTwo - 1][j + lByTwo - 1] = assigned[1]
        filled.__delitem__(1)
    elif part == 2:
        grid[i + lByTwo - 1][j + lByTwo] = assigned[2]
        filled.__delitem__(2)
    elif part == 3:
        grid[i + lByTwo][j + lByTwo - 1] = assigned[3]
        filled.__delitem__(3)
    else:
        grid[i + lByTwo][j + lByTwo] = assigned[4]
        filled.__delitem__(4)
    filled[part] = p

    if lByTwo != 1:
        tileNo += 1
        solve(i, j , int(lByTwo/2), filled[1])
        tileNo += 1
        solve(i, j+lByTwo, int(lByTwo / 2), filled[2])
        tileNo += 1
        solve(i+lByTwo, j, int(lByTwo / 2), filled[3])
        tileNo += 1
        solve(i+lByTwo, j+lByTwo, int(lByTwo / 2), filled[4])


def tilling(n, p): # n=2**k, p- (x,y)
    global grid

    # tot squares = 2**(k+1), tile_needed = (2**(k+1)-1)/3
    grid = [[0 for _ in range(n)] for _ in range(n)]
    solve(0, 0, int(n/2),p)
    for i in grid:
        for j in range(n):
            if i[j] < 10:
                print(0, end='')
            if j==n-1:
                print(i[j])
            else:
                print(i[j], end=' ')


tilling(8, (3,1))
