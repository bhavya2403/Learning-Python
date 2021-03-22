from random import randint

def policeman(arr, k):
    n = len(arr)
    tot = 0
    police, thief = [], []
    for i in range(n):
        if arr[i] == 'P':
            police.append(i)
        else:
            thief.append(i)

    p, t = 0, 0
    while p < len(police) and t < len(thief):
        if abs(police[p]-thief[t]) <= k:
            tot += 1
            p += 1
            t += 1
        elif police[p] < thief[t]:
            p += 1
        else:
            t += 1
    return tot

arr = [randint(0, 1) for _ in range(10)]
print(arr)

# print(policeman(['P', 'T', 'T', 'P', 'T'], 1))
# print(policeman(['T', 'T', 'P', 'P', 'T', 'P'], 2))
# print(policeman(['P', 'T', 'P', 'T', 'T', 'P'], 3))