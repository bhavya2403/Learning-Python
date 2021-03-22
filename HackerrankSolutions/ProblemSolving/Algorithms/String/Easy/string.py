def string(s):
    s1 = ''
    s2 = ''
    for index in range(len(s)):
        if index % 2 == 0:
            s1 += str(s[index])
        else:
            s2 += str(s[index])

    return s1 + ' ' + s2


inp = int(input())
for i in range(inp):
    s = input()
    print(string(s))


