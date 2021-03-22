# recursive solution(brute force) (proper O(2^n)), space: O(1)
def solve1(leftCap, w, p, n):
    if n==0 or leftCap==0:
        return 0
    return max(p[n]+solve1(leftCap-w[n], w, p, n-1), solve1(leftCap, w, p, n-1))
# _____________________________________________________
# we will not go further if sol is no longer feasible(weight exceeds capacity)
def solve2(leftCap, w, p, n):
    if n==0 or leftCap==0:
        return 0
    if w[n] > leftCap:
        return solve2(leftCap, w, p, n-1)
    return max(p[n]+solve2(leftCap-w[n], w, p, n-1), solve2(leftCap, w, p, n-1))
#_______________________________________________________
def knapsack(w, p, cap):
    n = len(w)
    return solve1(cap, w, p, n-1), solve2(cap, w, p, n-1)

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(knapsack(wt, val, W))
