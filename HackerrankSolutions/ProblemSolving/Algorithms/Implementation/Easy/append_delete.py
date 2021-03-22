def appendAndDelete(s, t, k):
    if s == t:
        return 'Yes'
    num = 0
    i = 0
    while True:
        if i == len(s):
            num = len(t[i:len(t) + 1])
            break

        elif i == len(t):
            num = len(s[i:len(s) + 1])
            break

        if s[i] != t[i]:
            if i == 0:
                return 'Yes'
            num = len(s[i:len(s) + 1]) + len(t[i:len(t) + 1])
            break
        i += 1

    if k >= num and k % 2 == num % 2:
        return 'Yes'
    else:
        return 'No'


print(appendAndDelete('aaa', 'a', 5))
