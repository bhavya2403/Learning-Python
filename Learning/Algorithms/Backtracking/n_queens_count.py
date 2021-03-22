# let's say there are n queens and m*m chessboard and we need to place all queens such
# that no two queens are under attack(all queens' row, column and diag should be different)

def printBoard(n, board):
    for i in range(n):
        for j in range(n-1):
            print(board[i][j], end=' ')
        print(board[i][j+1])
    print('________________________')

def solve(n, board, colsNotFilled, filled, row):
    if row==n:
        printBoard(n, board)
        return

    for col in colsNotFilled:
        if all(abs(i-row)!=abs(j-col) for i, j in filled):
            board[row][col] = 1

            solve(n, board, colsNotFilled-{col}, filled|{(row, col)}, row+1)

            board[row][col] = 0


def nQueens(n):
    colsNotFilled = set(i for i in range(n))
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(n, board, colsNotFilled, set(), 0)


nQueens(8)