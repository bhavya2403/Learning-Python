n, m, k = map(int, input().split())
track = []
d = {}
for _ in range(k):
    r, c1, c2 = map(int, input().split())
    s = {i for i in range(c1, c2 + 1)}
    if r not in d:
        d[r] = s
    else:
        d[r] = d[r] | s

count = 0
for i in d:
    count += m - len(d[i])
print(count+m*(n-len(d)))
