# TRY OUT ALL POSSIBLE SOLUTIONS AND THEN PICK UP THE BEST ONE
# this approach(BRUTE FORCE) is same as dynamic programming but in this case our goal is not to optimize the problem
# but there exists some solutions and we need to find out all possible solutions or may be one
# the solution will be in form of state space tree
# backtracking follows DFS whereas branch and bound will follow BFS

# let's say the problem is : there are three chairs and 3 people(BBG) and we need to find total number of arrangements
count = 0
def arrangements(chairs):
    def solve(S):
        global count
        if not S:
            count += 1
        for i in S:
            solve(S-{i})

    solve({'b1', 'b2', 'g'})
arrangements(3)
print(count)

# now let's say we put a constraint that a girl can not sit in middle
bounded_count = 0
def boundedArrangements(chairs):
    global bounded_count
    def solve(level, S):
        global bounded_count
        if not S:
            bounded_count += 1
        for i in S:
            if level==2 and i=='g':
                continue
            solve(level+1, S-{i})

    solve(1, {'b1', 'b2', 'g'})
boundedArrangements(3)
print(bounded_count)
