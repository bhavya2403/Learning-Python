def printBoard(n, board):
    for i in range(n):
        for j in range(n - 1):
            if board[i][j] != -1:
                print(0, end='')
            print(board[i][j], end=' ')
        if board[i][j + 1] != -1:
            print(0, end='')
        print(board[i][j + 1])


def isValid(n, board, i, j):
    if 0 <= i < n and 0 <= j < n:
        if board[i][j] == 1:
            return True
    return False


def solve(dir, n, board, i, j):
    if i == j == n - 1:
        board[i][j] = -1
        return True

    for x, y in dir:
        X, Y = x + i, y + j
        if isValid(n, board, X, Y):
            board[X][Y] = -1

            if solve(dir, n, board, X, Y):
                return board

            board[X][Y] = 1

    return False


def ratInMaze(n, board):
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    board[0][0] = -1
    board = solve(dir, n, board, 0, 0)
    if board[n - 1][n - 1] == -1:
        printBoard(n, board)
    else:
        print("Solution doesn't exist.")


board = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
ratInMaze(4, board)
