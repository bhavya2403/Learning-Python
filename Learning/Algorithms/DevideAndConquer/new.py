time = 0

def painterPartition(prevSum, i, maxTime, k):
    global time
    time += 1
    if mem[i][k]:
        return mem[i][k]
    if i>=n:
        if prevSum > maxTime:
            maxTime = prevSum
        mem[i][k] = maxTime
        return maxTime

    elif k==1:
        s = sum(board[i:])
        if s > maxTime:
            maxTime = s
        mem[i][k] = maxTime
        return maxTime

    elif prevSum + board[i] > optTime:
        a, b = max(prevSum, maxTime), max(prevSum+board[i], maxTime)

        if mem[i][k-1]:
            case1 = mem[i][k-1]
        else:
            case1 = painterPartition(0, i, a, k-1)
            mem[i][k-1] = case1

        if mem[i][k-1]:
            case2 = mem[i][k-1]
        else:
            case2 = painterPartition(0, i + 1, b, k - 1)
            mem[i][k-1] = case2
        mem[i][k] = min(case1, case2)
        return min(case1, case2)

    else:
        case = painterPartition(prevSum+board[i], i+1, maxTime, k)
        mem[i][k] = case
        return case

for _ in range(int(input())):
    k, n = map(int, input().split())
    board = list(map(int, input().split()))
    optTime = sum(board)/k
    mem = [[0 for _ in range(k+1)] for _ in range(n+1)]
    print(painterPartition(0,0,0,k))
    print(time)
    for i in mem:
        for j in range(k+1):
            if j==k:
                print(i[j])
            else:
                if i[j] == 0:
                    print('000', end=' ')
                else:
                    print(i[j], end=' ')
