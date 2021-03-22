def solve(i, j, idx, path):
    global grid, string, lenStr, directions, n, m
    if idx==lenStr:
        print(string, ':', path)
        return

    for x, y in directions:
        if 0 <= i+x < n and 0 <= j+y < m:
            if grid[i+x][j+y] == string[idx] and (i+x, j+y) not in path:
                path.append((i+x, j+y))

                solve(i+x, j+y, idx+1, path)

                path.pop()

def boggle(strings):
    global grid, string, directions, n, m, lenStr

    stringsIdx0 = {}
    for idx, string in enumerate(strings):
        if string[0] not in stringsIdx0:
            stringsIdx0[string[0]] = {idx}
        else:
            stringsIdx0[string[0]].add(idx)

    directions = [(-1,1), (0,1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] in stringsIdx0:
                for idx in stringsIdx0[grid[i][j]]:
                    string, lenStr = strings[idx], len(strings[idx])
                    solve(i, j, 1, [(i, j)])

n = m = 3
grid = [
    ['G', 'K', 'S'],
   ['U', 'E', 'K'],
   ['Q', 'S', 'E']
]
boggle(["GEEKS", "FOR", "QUIZ", "GO"])