# let's say there are n queens and m*m chessboard and we need to place all queens such
# that no two queens are under attack(all queens' row, column and diag should be different)

def solve(n, m, board, fixed, queens):
    # for col in cols_not_filled:
    #     if all(abs(i - row) != abs(j - col) for i, j in filled):
    #         board[row][col] = 1
    #         filled.add((row, col))
    #         cols_not_filled.remove(col)
    #
    #         if solve(N, board, cols_not_filled, filled, row + 1):
    #             return True
    #
    #         if len(filled)==1:
    #             return False
    #         board[row][col] = 0
    #         cols_not_filled.add(col)
    #         filled.remove((row, col))

    return False

def isValid(board, fixed, row, col):
    pass

def nQueens(n, m, board, fixed):
    max_queens = min(n, m)
    count = m*n- len(fixed)
    for queens in range(2, max_queens+1):
        if solve(n, m, board, fixed, queens):
            count += 1
        board[0][i] = 0

    return count


for _ in range(int(input())):
    n, m = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    fixed = set()
    for i in range(n):
        string = input()
        for j in range(m):
            if string[j]=='#':
                fixed.add((i, j))

    print(nQueens(n, m, board, fixed))