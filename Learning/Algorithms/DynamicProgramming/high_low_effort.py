maxAmount = 0

def solve(curr, tasks, noTaskPrev, amount):
    global maxAmount

    if curr == len(tasks):
        if amount > maxAmount:
            maxAmount = amount
        return

    solve(curr+1, tasks, True, amount)
    if noTaskPrev:
        solve(curr+1, tasks, False, amount+tasks[curr][1])
    else:
        solve(curr + 1, tasks, False, amount + tasks[curr][0])


def highLowEffort(tasks):
    n = len(tasks)
    solve(0, tasks, True, 0)
    print(maxAmount)

    dp = [(0,tasks[0][1])] + [(0,0)]*(n-1)
    for i in range(1,n):
        dp[i] = (dp[i-1][1], max(dp[i-1][0]+tasks[i][1], dp[i-1][1]+tasks[i][0]))

    return max(dp[n-1])

print(highLowEffort([(1,3), (5,6), (4,8), (5,7), (3,6)]))
