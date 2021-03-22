def find(parent, i):
    if parent[i] < 0:
        return i
    return find(parent, parent[i])

def union(parent, i, j):
    if parent[i] > parent[j]:
        parent[j] += parent[i]
        parent[i] = j
    else:
        parent[i] += parent[j]
        parent[j] = i

def cycles(v, sd):
    parent = [-1] * v
    totCycles = 0
    for i, j in sd:
        i -= 1
        j -= 1
        ps = find(parent, i)
        if parent[i] >= 0:
            parent[i] = ps
        pd = find(parent, j)
        if parent[j] >= 0:
            parent[j] = pd

        if ps != pd:
            union(parent, ps, pd)
        else:
            totCycles += 1

    return totCycles

sd = []
sd.append((1, 10))
sd.append((1, 5))
sd.append((5, 10))
sd.append((2, 9))
sd.append((9, 15))
sd.append((2, 15))
sd.append((2, 12))
sd.append((12, 15))
sd.append((13, 8))
sd.append((6, 14))
sd.append((14, 3))
sd.append((3, 7))
sd.append((7, 11))
sd.append((11, 6))
print(cycles(15, sd))