def shortPalindrome(s):
    n = len(s)
    count = 0
    num = 10e9 + 7
    for i in range(n - 3):
        a = s[i]
        for j in range(n - 2):
            b = s[j]
            for k in range(n - 1):
                c = s[k]
                if b == c:
                    for l in range(n):
                        d = s[l]
                        if a == d:
                            count += 1
                            if count == num:
                                count = 0
    return count

print(shortPalindrome('abbaab'))