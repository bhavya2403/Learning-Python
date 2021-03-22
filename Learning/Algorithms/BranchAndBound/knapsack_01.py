# we can use backtracking to improve the brute force recursive solution
# but we have one better method (than backtracking)
# we will use LC-BB means exploring the nodes first which gives max profit
# The problem with DP approach is it can not work for fractional weights and capacity
# what we will do is we will set an upperbound
# cost: best possible result(which we can get by including fractions using greedy)
# u: profit by in
upper = 0 # we'll be minimizing

def solve(wpArr, cap, u, c, i):
    global upper

    stack = [[u,c,i+1]]
    u1 = u+ wpArr[i][1]
    pass


def knapsack(w, p, cap):
    n = len(w)
    wpArr = [(w[i], -p[i]) for i in range(n)]
    wpArr.sort(key=lambda a: a[0]/a[1])
