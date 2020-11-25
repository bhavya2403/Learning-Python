def repeatedString(s, n):
    s1 = ''
    while True:
        s1 += s
        if len(s1) >= n-len(s):
            break
    print(s1)

    index = 0
    for i in s:
        if index < n-len(s1):
            s1 += i
        elif index == n-len(s1):
            break
        index += 1
    print(s1)

    count = 0
    for i in s1:
        if i == 'a':
            count += 1

    return count


print(repeatedString("aba", 10))

