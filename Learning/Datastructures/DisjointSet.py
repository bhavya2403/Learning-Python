# disjoint sets are those two sets for which s1&s2 = None
# main operations: find, union
# problems: finding cycle in undirected graph, kruskal's mst
# in kruskal's mst while finding the parent if both nodes have same parent(both belong to same set)
# then the graph contains cycle
# we are not actually performing union on the sets like mathematics
# as we did in kruskals mst we'll have parent and rank array where parent[i] is just representing
# parent of that node, if >=0 it is child of parent[i], if <0 it's parent of -parent[i] nodes
# collapsing union means while finding the parent for the first time we'll directly link that node to
# the root this way we can save some time(if we'r finding parent of that el more than once)