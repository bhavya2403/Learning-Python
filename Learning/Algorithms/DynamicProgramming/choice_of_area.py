def solve(x, y, z, a, b, curr):
    global mem
    if a < 0 or b < 0:
        return 0

    if not curr:
        if (a+x[0], b+x[1]) not in mem:
            mem[(a+x[0], b+x[1])] = solve(x, y, z, a + x[0], b + x[1], 'x')
        if (a+y[0], b+y[1]) not in mem:
            mem[(a+y[0], b+y[1])] = solve(x, y, z, a + y[0], b + y[1], 'y')
        if (a+z[0], b+z[1]) not in mem:
            mem[(a+z[0], b+z[1])] = solve(x, y, z, a + z[0], b + z[1], 'z')

        return 1 + max(mem[(a+x[0], b+x[1])],
                       mem[(a+y[0], b+y[1])],
                       mem[(a+z[0], b+z[1])])
    if curr == 'x':
        if (a + y[0], b + y[1]) not in mem:
            mem[(a + y[0], b + y[1])] = solve(x, y, z, a + y[0], b + y[1], 'y')
        if (a + z[0], b + z[1]) not in mem:
            mem[(a + z[0], b + z[1])] = solve(x, y, z, a + z[0], b + z[1], 'z')

        return 1 + max(mem[(a + y[0], b + y[1])],
                       mem[(a + z[0], b + z[1])])
    if curr == 'y':
        if (a + x[0], b + x[1]) not in mem:
            mem[(a + x[0], b + x[1])] = solve(x, y, z, a + x[0], b + x[1], 'x')
        if (a + z[0], b + z[1]) not in mem:
            mem[(a + z[0], b + z[1])] = solve(x, y, z, a + z[0], b + z[1], 'z')

        return 1 + max(mem[(a + x[0], b + x[1])],
                       mem[(a + z[0], b + z[1])])
    if curr == 'z':
        if (a + x[0], b + x[1]) not in mem:
            mem[(a + x[0], b + x[1])] = solve(x, y, z, a + x[0], b + x[1], 'x')
        if (a + y[0], b + y[1]) not in mem:
            mem[(a + y[0], b + y[1])] = solve(x, y, z, a + y[0], b + y[1], 'y')
        return 1 + max(mem[(a + x[0], b + x[1])],
                       mem[(a + y[0], b + y[1])])

def choiceOfArea(x, y, z, a, b):
    global mem
    mem = {}
    return solve(x, y, z, a, b, 0)


print(choiceOfArea((3,2), (-5,-10), (-20, 5), 20, 8))
