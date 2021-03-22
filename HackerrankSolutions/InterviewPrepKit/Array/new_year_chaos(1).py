def bribes(Q):
    moves = 0
    Q = [P-1 for P in Q]
    for i,P in enumerate(Q):
        if P - i > 2:
            return "Too chaotic"
        for j in range(max(P - 1, 0), i):
            if Q[j] > P:
                moves += 1
    return moves


print(bribes([1,2,5,3,7,8,6,4]))
