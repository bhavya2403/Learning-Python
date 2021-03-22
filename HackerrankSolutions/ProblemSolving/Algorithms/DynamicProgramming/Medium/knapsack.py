def unboundedKnapsack(k, arr):
    target = [False for _ in range(k+1)]
    set_arr = set(arr)
    if 1 in set_arr:
        return k
    for i in range(2, k+1):
        if i in set_arr:
            target[i] = True
        else:
            j = i-1
            while j >= i/2:
                if target[j] and target[i-j]:
                    target[i] = True
                    break
                j -= 1
    i = k
    while i >= 0:
        if target[i]:
            return i
        i -= 1
    return 0

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(unboundedKnapsack(k, arr))
# print(unboundedKnapsack(9, [3, 4, 4, 4, 8]))