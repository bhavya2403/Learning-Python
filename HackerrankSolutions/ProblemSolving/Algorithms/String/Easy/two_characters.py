def alternate(s):
    a = []
    for i in s:
        if i not in a:
            a.append(i)

    a1 = []
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            s1 = ''
            for char in s:
                if char == a[i] or char == a[j]:
                    s1 += str(char)

            wrong = False
            for k in range(0, len(s1)-1):
                if s1[k] == s1[k+1]:
                    wrong = True

            if not wrong:
                a1.append(len(s1))

    if len(a1) == 0:
        return 0
    return max(a1)

print(alternate('beabeefeab'))



