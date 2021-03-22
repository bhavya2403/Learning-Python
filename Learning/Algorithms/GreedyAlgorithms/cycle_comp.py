def connectedComp(V, adj_list):
    found = [False] * V
    answer = []
    while True:
        i = 0
        flag = True
        for i in range(V):
            if not found[i]:
                flag = False
                break

        if flag:
            break

        bfs = []
        stack = [i]
        while stack:
            node = stack.pop()
            if not found[node]:
                bfs.append(node)
                if node in adj_list:
                    for v in adj_list[node]:
                        if not found[v]:
                            stack.append(v)
                found[node] = True
        answer.append(bfs)

    return answer

def cycleComp(v, adj_list):
    answer = connectedComp(v,adj_list)
    count = 0
    for i in range(len(answer)):
        found = True
        for j in answer[i]:
            if j not in adj_list:
                found = False
                break
            elif len(adj_list[j]) != 2:
                found = False
                break

        if found:
            count += 1

    return count

def addEdge(u, v):
    u -= 1
    v -= 1
    if u not in adj_list:
        adj_list[u] = [v]
    else:
        adj_list[u].append(v)

    if v not in adj_list:
        adj_list[v] = [u]
    else:
        adj_list[v].append(u)

adj_list = {}
addEdge(1, 10)
addEdge(1, 5)
addEdge(5, 10)
addEdge(2, 9)
addEdge(9, 15)
addEdge(2, 15)
addEdge(2, 12)
addEdge(12, 15)
addEdge(13, 8)
addEdge(6, 14)
addEdge(14, 3)
addEdge(3, 7)
addEdge(7, 11)
addEdge(11, 6)
print(cycleComp(15, adj_list))