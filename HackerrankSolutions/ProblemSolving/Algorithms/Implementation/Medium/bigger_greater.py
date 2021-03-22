def biggerIsGreater(w):
    size = len(w)
    i = size-1
    while i > 0:
        if w[i-1] < w[i]:
            break
        i -= 1
    if i == 0:
        return 'no answer'

    arr = []
    maxi = ord(w[i-1])
    mini = 122
    for j in range(i, size):
        num = ord(w[j])
        if maxi < num < mini:
            mini = num
        arr.append(num)
    arr[arr.index(mini)] = maxi
    arr.sort()
    w1 = ''
    for j in arr:
        w1 += chr(j)

    return w[:i-1] + chr(mini) + w1

for _ in range(int(input())):
    w = input()
    print(biggerIsGreater(w))