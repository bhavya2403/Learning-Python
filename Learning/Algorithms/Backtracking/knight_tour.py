def isValid(x, y, N, board):
    if 0 <= x < N and 0 <= y < N and not board[x][y]:
        return True
    return False

def solve(N, moveX, moveY, board, time, curr):
    if time==N*N:
        return True

    for k in range(N):
        x, y = curr[0]+moveX[k], curr[1]+moveY[k]

        if isValid(x, y, N, board):
            board[x][y] = time

            if solve(N, moveX, moveY, board, time+1, (x, y)):
                return board

            board[x][y] = 0

def knightTour(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    moveX = [-2,-1,1,2,2,1,-1,-2]
    moveY = [1,2,2,1,-1,-2,-2,-1]

    board = solve(N, moveX, moveY, board, 1, (0,0))

    for i in range(N):
        for j in range(N):
            num = board[i][j]
            if num < 10:
                print(0, end='')
            if j == N-1:
                print(num)
            else:
                print(num, end=' ')

knightTour(8)