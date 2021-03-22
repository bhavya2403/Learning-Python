n, p = map(int, input().split())
pairs = []
for _ in range(p):
    a, b = map(int, input().split())
    repeat = set()
    for i in range(len(pairs)):
        for j in range(len(pairs[i])):
            if pairs[i][j] == a or pairs[i][j]==b:
                repeat.add(i)

    s = {a, b}
    if repeat:
        for i in repeat:
            s = s | set(pairs[i])
        k = 0
        for i in repeat:
            pairs[i] = []
            k += 1
    i = 0
    while True:
        try:
            if not pairs[i]:
                pairs.remove(pairs[i])
            else:
                i += 1
        except:
            break
    pairs.append(list(s))

result = 0
arr = [len(i) for i in pairs]
s = sum(arr)
l = len(arr)
for i in range(l-1):
    for j in range(i+1, l):
        result += arr[i] * arr[j]
result += s*(n-s) + int((n-s)*(n-s-1)/2)
print(result)
