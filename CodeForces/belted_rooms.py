for _ in range(int(input())):
    n = int(input())
    s = input()
    if ('<' in s and '>' in s):
        i = 0
        count = 0
        while i < n:
            if s[i]=='-':
                cons = 0
                j = i+1
                for j in range(i+1, n):
                    if s[j]!='-':
                        break
                    cons += 1
                i = j+1
                count += cons+2
            else:
                i += 1
        if s[0]=='-' and s[n-1]=='-':
            count -= 1
        print(count)
    else:
        print(n)
