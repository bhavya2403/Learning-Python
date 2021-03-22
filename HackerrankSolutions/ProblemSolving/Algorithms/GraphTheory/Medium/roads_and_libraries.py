def min_cost(n, c_road, c_lib, roads):
    if c_road >= c_lib:
        return n*c_lib
    dfs = []
    checked = {i for i in range(1,n+1)}
    queue = []
    tot_cost = 0
    while True:
        broken = False
        removing = []
        for i in checked:
            if i not in roads:
                tot_cost += c_lib
                removing.append(i)
            else:
                queue = [i]
                broken = True
                dfs = []
                break
        if not broken:
            return tot_cost
        for i in removing:
            checked.remove(i)

        while queue and checked:
            node = queue.pop()
            if node in checked:
                queue = roads[node] + queue
                checked.remove(node)
                dfs.append(node)
        tot_cost += (len(dfs)-1)*c_road + c_lib if dfs else 0

for _ in range(int(input())):
    n, m, c_lib, c_road = map(int, input().split())
    roads = {}
    for _ in range(m):
        a, b = list(map(int, input().split()))
        if a not in roads:
            roads[a] = [b]
        else:
            roads[a].append(b)
        if b not in roads:
            roads[b] = [a]
        else:
            roads[b].append(a)

    print(min_cost(n, c_road, c_lib, roads))

# 2
# 3 3 2 1
# 1 2
# 3 1
# 2 3
# 6 6 2 5
# 1 3
# 3 4
# 2 4
# 1 2
# 2 3
# 5 6