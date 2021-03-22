def DFSiterative(graph_dict):
    alr_visited = {i: 0 for i in graph_dict}
    dfs = []
    stack = []
    for node in graph_dict:
        dfs.append(node)
        break
    visiting_vertex = node
    while True:
        alr_visited[visiting_vertex] = 1
        broken = False
        for node in graph_dict[visiting_vertex]:
            if alr_visited[node] == 0:
                stack.append(visiting_vertex)
                dfs.append(node)
                visiting_vertex = node
                broken = True
                break
        if not stack:
            return dfs
        if not broken:
            alr_visited[visiting_vertex] = 1
            visiting_vertex = stack.pop()

def BFSGraph(graph_dict):
    bfs = []
    queue = []
    alr_visited = {i:0 for i in graph_dict}
    for i in graph_dict:
        queue += graph_dict[i]
        alr_visited[i] = 1
        bfs = [i]
        break
    while queue:
        vertex = queue.pop()
        if alr_visited[vertex]:
            continue
        alr_visited[vertex] = 1
        bfs.append(vertex)
        queue = graph_dict[vertex] + queue

    return bfs

def get_paths(graph_dict, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph_dict:
        return []

    paths = []
    for node in graph_dict[start]:
        if node not in path:
            new_paths = get_paths(graph_dict, node, end, path)
            for p in new_paths:
                paths.append(p)

    return paths

graph_dict = {
    1: [2,3,4,5],
    2: [6,7,8],
    3: [6,7],
    4: [8],
    5: [7,8],
    6: [9,10],
    7: [9,10],
    8: [10,11],
    9: [12],
    10: [12],
    11: [12],
    12: []
}
print(BFSGraph(graph_dict))
print(DFSiterative(graph_dict))
print(get_paths(graph_dict, 1, 12))