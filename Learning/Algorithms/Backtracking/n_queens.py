# let's say there are n queens and m*m chessboard and we need to place all queens such
# that no two queens are under attack(all queens' row, column and diag should be different)

def solve(N, board, cols_not_filled, filled, row):
    if row == N:
        return True

    for col in cols_not_filled:
        if all(abs(i-row) != abs(j-col) for i, j in filled):
            board[row][col] = 1
            filled.add((row, col))
            cols_not_filled.remove(col)

            if solve(N, board, cols_not_filled, filled, row+1):
                return True

            board[row][col] = 0
            cols_not_filled.add(col)
            filled.remove((row, col))

    return False


def printBoard(N, board):
    for i in range(N):
        for j in range(N):
            if j == N-1:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')

def nQueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if solve(N, board, {i for i in range(N)}, set(), 0):
        printBoard(N, board)
    else:
        print('No Solution Exist')


nQueens(4)