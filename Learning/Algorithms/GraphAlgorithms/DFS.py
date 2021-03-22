# it's like pre order traversal for the tree
def pre_order_traversal(root):
    arr = [root.data]
    if root.left:
        arr += pre_order_traversal(root.left)
    if root.right:
        arr += pre_order_traversal(root.right)
    return arr

def DFSGraph(graph_dict):
    alr_visited = {i: 0 for i in graph_dict}
    dfs = []
    vertex = 0
    for node in graph_dict:
        vertex = node
        break

    def solve(vertex):
        dfs.append(vertex)
        alr_visited[vertex] = 1
        for node in graph_dict[vertex]:
            if not alr_visited[node]:
                solve(node)
    solve(vertex)
    return dfs

def DFSiterative(V, adj_list):
    dfs = []
    stack = []
    vertices = {}
    idx = 0
    for i in adj_list:
        stack = [i]
        vertices[i] = idx
        idx += 1

    visited = [False] * V
    while stack:
        node = stack.pop()
        if not visited[vertices[node]]:
            for v in adj_list[node]:
                if not visited[vertices[v]]:
                    stack.append(v)
            visited[vertices[node]] = True
            dfs.append(node)

    return dfs

# graph_dict = {
#     'a': ['c', 'b'],
#     'b': ['d', 'e'],
#     'c': ['f', 'b'],
#     'd': [],
#     'e': ['f'],
#     'f': []
# }
routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
    ("Mumbai", "Toronto"),
    ("New York", "Delhi")
]

graph_dict = {}
for start, end in routes:
    if start not in graph_dict:
        graph_dict[start] = [end]
    else:
        graph_dict[start].append(end)

    if end not in graph_dict:
        graph_dict[end] = [start]
    else:
        graph_dict[end].append(start)

print(DFSiterative(6, graph_dict))
print(DFSGraph(graph_dict))
