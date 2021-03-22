def checkPath(adj_list, start, end, visited):
    if start == end:
        return True

    if start in adj_list:
        visited[start] = True
        for v in adj_list[start]:
            if not visited[v]:
                if checkPath(adj_list, v, end, visited):
                    return True
    return False


def revDelete(V, E, SDW):
    adj_list = {}
    for s, d, w in SDW:
        if s not in adj_list:
            adj_list[s] = [d]
        else:
            adj_list[s].append(d)

        if d not in adj_list:
            adj_list[d] = [s]
        else:
            adj_list[d].append(s)
    SDW.sort(key=lambda a: a[2], reverse=True)

    deleted = 0
    delSet = set()
    for idx, (u, v, w) in enumerate(SDW):
        adj_list[u].remove(v)
        adj_list[v].remove(u)

        if not checkPath(adj_list, u, v, [False] * V):
            adj_list[u].append(v)
            adj_list[v].append(u)
        else:
            delSet.add(idx)
            deleted += 1

        if deleted == E - V + 1:
            break

    answer = 0
    for i in range(E):
        if i not in delSet:
            answer += SDW[i][2]

    return answer


for _ in range(int(input())):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    SDW = []
    for i in range(E):
        SDW.append((arr[3 * i], arr[3 * i + 1], arr[3 * i + 2]))

    print(revDelete(V, E, SDW))