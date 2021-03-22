# there are n workers and we need to assign m jobs, 1 at most job to each worker
# matrix[i][j]= worker i takes matrix[i][j] cost to do the jth job
# minimize the total cost
from heapq import heappush, heappop

minCost = 10**5
optArr = []
def solve(n, m, matrix, cost, i, assigned, answer):
    global minCost
    global optArr

    if i==n:
        if cost < minCost:
            minCost = cost
            optArr = answer.copy()
        return

    heap = []
    for j in {i for i in range(m)} - assigned:
        if cost <= minCost and j not in assigned:
            heappush(heap, [cost+matrix[i][j], j])

    while heap:
        cost, j = heappop(heap)
        answer[i] = j
        solve(n, m, matrix, cost, i+1, assigned | {j}, answer)

def jobAssignment(matrix):
    solve(len(matrix), len(matrix[0]), matrix, 0, 0, set(), [0]*len(matrix))
    print(minCost, optArr)


matrix = [[9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4] ]
print(jobAssignment(matrix))