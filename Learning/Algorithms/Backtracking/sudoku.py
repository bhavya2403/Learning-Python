def printBoard(board):
    for i in range(9):
        for j in range(9):
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=' ')


def isValid(board, num, row, col):
    for i in range(9):
        if board[i][col] == num or board[row][i] == num:
            return False

    for i in range((row // 3) * 3, (row // 3) * 3 + 3):
        for j in range((col // 3) * 3, (col // 3) * 3 + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board, row, col):
    if col == 9:
        return solve(board, row+1, 0)
    if row == 9:
        return True

    if board[row][col]:
        if col == 8:
            return solve(board, row + 1, 0)
        else:
            return solve(board, row, col + 1)

    for num in range(1, 10):
        if isValid(board, num, row, col):
            board[row][col] = num

            if solve(board, row, col + 1):
                return True

            board[row][col] = 0

    return False


def sudoku(board):
    if solve(board, 0, 0):
        printBoard(board)
    else:
        print("solution doesn't exist")


board1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
board2 = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]
board3 = [
    [3, 1, 6, 5, 7, 8, 4, 9, 2],
    [5, 2, 9, 1, 3, 4, 7, 6, 8],
    [4, 8, 7, 6, 2, 9, 5, 3, 1],
    [2, 6, 3, 0, 1, 5, 9, 8, 7],
    [9, 7, 4, 8, 6, 0, 1, 2, 5],
    [8, 5, 1, 7, 9, 2, 6, 4, 3],
    [1, 3, 8, 0, 4, 7, 2, 0, 6],
    [6, 9, 2, 3, 5, 1, 8, 7, 4],
    [7, 4, 5, 0, 8, 6, 3, 1, 0]
]
sudoku(board1)
print("---------------------")
sudoku(board2)
print("---------------------")
sudoku(board3)
