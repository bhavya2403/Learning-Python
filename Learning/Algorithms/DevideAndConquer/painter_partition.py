def painterPartition(prevSum, i, maxTime, k):
    global mem
    if i>=n:
        if prevSum > maxTime:
            maxTime = prevSum
        return maxTime

    if k==1:
        s = sum(board[i:])
        if s > maxTime:
            maxTime = s
        return maxTime

    if prevSum + board[i] > optTime:
        a, b = max(prevSum, maxTime), max(prevSum+board[i], maxTime)
        if mem[i][k-1]:
            case1 = mem[i][k-1]
        else:
            case1 = painterPartition(0, i, a, k-1)
            mem[i][k-1] = case1

        if i+1 < n:
            if mem[i+1][k-1]:
                case2 = mem[i+1][k-1]
            else:
                case2 = painterPartition(0, i+1, b, k-1)
                mem[i+1][k-1] = case2
        else:
            case2 = painterPartition(0, i + 1, b, k - 1)
            mem[i+1][k-1] = case2

        return min(case1, case2)

    if i+1 < n:
        if mem[i+1][k]:
            return mem[i+1][k]

    case = painterPartition(prevSum+board[i], i+1, maxTime, k)
    mem[i+1][k] = case
    return case



for _ in range(int(input())):
    k, n = map(int, input().split())
    board = list(map(int, input().split()))
    optTime = sum(board)/k
    mem = [[0 for _ in range(k+1)] for _ in range(n)]
    print(painterPartition(0,0,0,k))
    print(mem)
