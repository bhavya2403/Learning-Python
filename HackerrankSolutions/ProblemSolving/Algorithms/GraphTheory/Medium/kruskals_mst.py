def findParent(parent, i):
    if parent[i]==i:
        return i
    return findParent(parent, parent[i])

def unionOfRoots(x, y, parent, rank):
    if rank[x] > rank[y]:
        parent[y] = parent[x]
        rank[x] += 1
    else:
        parent[x] = parent[y]
        rank[y] += 1

def kruskals(tot_ver, tot_edges, sr_de_we): # O(E(V+log(E)))
    parent = [i for i in range(tot_ver)]
    rank = [0]* tot_ver
    tot_weight = 0
    count = 0
    for sr, de, we in sr_de_we: # O(EV)
        x = findParent(parent, sr)
        y = findParent(parent, de)
        if x!=y:
            tot_weight += we
            unionOfRoots(x, y, parent, rank)
            count += 1
        if count==tot_ver-1:
            break
    return tot_weight

tot_ver, tot_edges = map(int,input().split())
sr_de_we = []
for _ in range(tot_edges):
    sr, de, we = map(int,input().split())
    sr_de_we.append((sr-1, de-1, we))
sr_de_we.sort(key=lambda arr:arr[2]) # O(E(log(E)))
print(kruskals(tot_ver, tot_edges, sr_de_we))
