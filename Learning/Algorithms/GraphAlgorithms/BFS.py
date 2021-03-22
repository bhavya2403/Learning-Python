# it's like level order traversal for the tree
def levelOrder(root):
    queue = [root] if root else []

    while queue:
        node = queue.pop()
        print(node.data, end=" ")

        if node.left: queue.insert(0, node.left)

        if node.right: queue.insert(0, node.right)

def BFSGraph(routes):
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

    bfs = []
    queue = []
    alr_visited = {i:0 for i in graph_dict}
    for i in graph_dict:
        queue += graph_dict[i]
        break
    while queue:
        vertex = queue.pop()
        if not alr_visited[vertex]:
            alr_visited[vertex] = 1
            bfs.append(vertex)
            queue = graph_dict[vertex] + queue

    return bfs

routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
    ("Mumbai", "Toronto"),
    ("New York", "Delhi"),
]

print(BFSGraph(routes))