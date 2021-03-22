# approach is similar to backtracking. In backtracking we use DFS to generate the state space tree
# here we will be using BFS instead
# branch and bound can only solve minimization problem not the maximization problem
# we can use 3 methods to expand the state space tree:
# 1> by using stack:FIFO (last node in the level will get explored first)
# 2> by using queue:LIFo (first node in the level will get explored first)
# 3> LC-BB: the node with the minimum cost will be explored first
# everytime in each problem we will have some extra variables
# cost:c and upperbound:u,
# upper: if upper is less than u, we'll update u as upper
# cost is for LC-BB, to decide which node to explore first
# if cost more than upper we'll kill the node and not explore it further
# actually cost is the best possible result we can get by exploring that node and why are
# we killing that node because we can not get better result than upper by exploring that node
# upper will be our answer