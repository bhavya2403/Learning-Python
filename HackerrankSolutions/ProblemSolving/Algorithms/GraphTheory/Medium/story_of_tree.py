def storyOfTheTree(n, adj_list, g, guesses, k):
    win_arr = [0] * n
    root = 1

    queue = [root]
    dfs = {root}
    total = {i for i in range(1, n+1)}
    alr_taken = [False] * n
    while queue:
        node = queue.pop()
        if node in guesses: # O(g1)
            for v in guesses[node]:
                if not alr_taken[v - 1]:
                    for i in dfs:
                        win_arr[i-1] += 1
                else:
                    for i in (total-dfs):
                        win_arr[i-1] += 1

        alr_taken[node-1] = True

        for child in adj_list[node]: # O(e)
            if not alr_taken[child-1]:
                queue = [child] + queue
    win = 0
    for i in win_arr:
        if i >= k:
            win += 1

    return int(win)

for _ in range(int(input())):
    n = int(input())
    adj_list = {}
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        if a not in adj_list:
            adj_list[a] = [b]
        else:
            adj_list[a].append(b)
        if b not in adj_list:
            adj_list[b] = [a]
        else:
            adj_list[b].append(a)

    g, k = map(int, input().split())
    guesses = {}
    for _ in range(g):
        u, v = map(int, input().split())
        if u not in guesses:
            guesses[u] = [v]
        else:
            guesses[u].append(v)

    result = storyOfTheTree(n, adj_list, g, guesses, k)
    if result:
        i = 1
        for i in range(result, 0, -1):
            if result % i == 0 and n % i == 0:
                break
        result, n = int(result/i), int(n/i)
        print(str(result) + '/' + str(n))
    else:
        print(str(0)+'/'+str(1))
