def snakeLadder(adj_list):
    queue = [1]
    level = 1
    while True:
        s = set()
        while queue:
            start = queue.pop()
            s = s.union(set(adj_list[start]))
            if 100 in s:
                return level
        queue = sorted(list(s))
        level += 1

for k in range(int(input())):
    adj_list = {}
    for i in range(1, 101):
        adj_list[i] = [j for j in range(i + 1, i + 7)]
    l = int(input())
    for _ in range(l):
        start, end = map(int, input().split())
        for i in range(start-6, start):
            try:
                if len(adj_list[i])==1:
                    adj_list[i] = end
                adj_list[i][start-i-1] = end
            except:
                continue
        adj_list[start] = end
    s = int(input())
    for _ in range(s):
        start, end = map(int, input().split())
        for i in range(start - 6, start):
            try:
                if len(adj_list[i])==1:
                    adj_list[i] = end
                adj_list[i][start-i-1] = end
            except:
                continue
        adj_list[start] = end

    broken = False
    for i in adj_list:
        if type(i)==int:
            continue
        for j in adj_list[i]:
            if j==100:
                print(snakeLadder(adj_list))
                broken = True
                break
        if broken:
            break
    if not broken:
        print(-1)
