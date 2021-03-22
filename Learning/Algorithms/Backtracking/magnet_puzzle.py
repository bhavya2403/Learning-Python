def checkAnswer():
    global top, right, bottom, left, m
    for i in range(m):
        if top[i] > 0 or bottom[i] > 0:
            return False
    for i in range(n):
        if left[i] > 0 or right[i] > 0:
            return False
    return True


def backtrackChange(i, j, casePosNeg):
    global top, right, bottom, left
    if casePosNeg == '+':
        top[j] += 1 if top[j] != -1 else 0
        left[i] += 1 if left[i] != -1 else 0
        return
    right[i] += 1 if right[i] != -1 else 0
    bottom[j] += 1 if bottom[j] != -1 else 0


def change(i, j, casePosNeg):
    global top, right, bottom, left
    if casePosNeg == '+':
        top[j] -= 1 if top[j] != -1 else 0
        left[i] -= 1 if left[i] != -1 else 0
        return
    right[i] -= 1 if right[i] != -1 else 0
    bottom[j] -= 1 if bottom[j] != -1 else 0


def checkPositive(i, j):
    global top, left, board, m
    if (top[j] != 0) and (left[i] != 0):
        if i > 0:
            if board[i - 1][j] == '+':
                return False
        if j > 0:
            if board[i][j - 1] == '+':
                return False
        if j < m - 1:
            if board[i][j + 1] == '+':
                return False
    else:
        return False
    return True


def checkNegative(i, j):
    global bottom, right, board, m
    if (bottom[j] != 0) and (right[i] != 0):
        if i > 0:
            if board[i - 1][j] == '-':
                return False
        if j > 0:
            if board[i][j - 1] == '-':
                return False
        if j < m - 1:
            if board[i][j + 1] == '-':
                return False
    else:
        return False
    return True


def solve(i, j):
    global rules, board, m, n
    if i == n:
        if checkAnswer():
            return True
        return False
    if j == m:
        return solve(i + 1, 0)
    if rules[i][j] == 'B' or rules[i][j] == 'R':
        return solve(i, j + 1)

    if rules[i][j] == 'L':
        ans1, ans2 = checkPositive(i, j), checkNegative(i, j + 1)
        if ans1 and ans2:
            board[i][j] = '+'
            board[i][j + 1] = '-'
            change(i, j, '+'), change(i, j + 1, '-')

            if solve(i, j + 2):
                return board

            board[i][j] = '*'
            board[i][j + 1] = '*'
            backtrackChange(i, j, '+'), backtrackChange(i, j + 1, '-')

            ans1, ans2 = checkNegative(i, j), checkPositive(i, j + 1)
            if ans1 and ans2:
                board[i][j] = '-'
                board[i][j + 1] = '+'
                change(i, j, '-'), change(i, j + 1, '+')

                if solve(i, j + 1):
                    return board

                board[i][j] = '*'
                board[i][j + 1] = '*'
                backtrackChange(i, j, '-'), backtrackChange(i, j + 1, '+')

                if solve(i, j + 2):
                    return board
                return False
        else:
            ans1, ans2 = checkNegative(i, j), checkPositive(i, j + 1)
            if ans1 and ans2:
                board[i][j] = '-'
                board[i][j + 1] = '+'
                change(i, j, '-'), change(i, j + 1, '+')

                if solve(i, j + 1):
                    return board

                board[i][j] = '*'
                board[i][j + 1] = '*'
                backtrackChange(i, j, '-'), backtrackChange(i, j + 1, '+')

                if solve(i, j + 2):
                    return board
                return False
            else:
                if solve(i, j + 2):
                    return board
                return False
    else:
        ans1, ans2 = checkPositive(i, j), checkNegative(i + 1, j)
        if ans1 and ans2:
            board[i][j] = '+'
            board[i + 1][j] = '-'
            change(i, j, '+'), change(i + 1, j, '-')

            if solve(i, j + 1):
                return board

            board[i][j] = '*'
            board[i + 1][j] = '*'
            backtrackChange(i, j, '+'), backtrackChange(i + 1, j, '-')

            ans1, ans2 = checkNegative(i, j), checkPositive(i + 1, j)
            if ans1 and ans2:
                board[i][j] = '-'
                board[i + 1][j] = '+'
                change(i, j, '-'), change(i + 1, j, '+')

                if solve(i, j + 1):
                    return board

                board[i][j] = '*'
                board[i + 1][j] = '*'
                backtrackChange(i, j, '-'), backtrackChange(i + 1, j, '+')

                if solve(i, j + 1):
                    return board
                return False
        else:
            ans1, ans2 = checkNegative(i, j), checkPositive(i + 1, j)
            if ans1 and ans2:
                board[i][j] = '-'
                board[i + 1][j] = '+'
                change(i, j, '-'), change(i + 1, j, '+')

                if solve(i, j + 1):
                    return board

                board[i][j] = '*'
                board[i + 1][j] = '*'
                backtrackChange(i, j, '-'), backtrackChange(i + 1, j, '+')

                if solve(i, j + 1):
                    return board
                return False
            else:
                if solve(i, j + 1):
                    return board
                return False
    return False


def magnetPuzzle():
    global board, m, n
    board = [['*' for _ in range(m)] for _ in range(n)]
    board = solve(0, 0)
    if not board:
        print("Solution doesn't exist")
    else:
        for i in range(n):
            for j in range(m - 1):
                print(board[i][j], end=' ')
            print(board[i][j + 1])


m = 6
n = 5
top = [1, -1, -1, 2, 1, -1]
bottom = [2, -1, -1, 2, -1, 3]
left = [2, 3, -1, -1, -1]
right = [-1, -1, -1, 1, -1]
rules = [
    ['L', 'R', 'L', 'R', 'T', 'T'],
    ['L', 'R', 'L', 'R', 'B', 'B'],
    ['T', 'T', 'T', 'T', 'L', 'R'],
    ['B', 'B', 'B', 'B', 'T', 'T'],
    ['L', 'R', 'L', 'R', 'B', 'B']
]
magnetPuzzle()
