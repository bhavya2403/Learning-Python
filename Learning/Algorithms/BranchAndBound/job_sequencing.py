# since we can not solve maximization problem using BB, we will be solving for minimum penalty
# instead of maximum profit
# here cost will be sum of all the jobs which we left(did not do)
# maxPenalty: sum of all the penalties of jobs which we haven't considered yet+we left's max value
# u: sum of all penalties which we haven't considered yet(we could update it to maxPenalty if u<maxPenalty)
# maxPenalty says that if we are getting some penalties then at most we will be getting is maxPenalty
# so if we get cost>maxPenalty we will kill that node
# If the best in subtree is worse than current best, we can simply ignore this node and its subtrees
# _________________________________________
maxPenalty = 10 ** 5  # we will be minimizing maxPenalty
jobs = []

def solve(n, penalty, deadline, time, time1, i, u, cost, answer):
    global maxPenalty, jobs
    if i == n:
        return

    stack = []
    cost1 = cost
    for j in range(i, n):
        if cost1 <= maxPenalty and time1 + time[j] <= deadline[j]:
            u1 = u - penalty[j]
            stack.append([time1+time[j], j+1, cost1, u1])
            if maxPenalty > u1:
                maxPenalty = u1
                jobs = answer.copy()
            cost1 += penalty[j]

    stack.reverse()

    while stack:
        time1, j, cost1, u1 = stack.pop()
        answer[j] = 1
        solve(n, penalty, deadline, time, time1, j, u1, cost1, answer)


def jobSequencing(penalty, deadline, time):
    n = len(penalty)
    sumP = sum(penalty)
    u = sumP  # sum(all  penalties-included jobs)
    cost = 0  # cost of leaving the jobs
    solve(n, penalty, deadline, time, 0, 0, u, cost, [0]*n)
    print(maxPenalty, jobs)


jobSequencing([5, 10, 6, 3], [1, 3, 3, 1], [1, 2, 1, 1])
