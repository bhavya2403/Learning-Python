def highestValuePalindrome(s, n, k):
    arr = [0]*(n//2)
    s = [i for i in s]
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            arr[i] = 1
            s[i] = str(max(int(s[i]), int(s[n-i-1])))
            s[n-i-1] = s[i]
            k -= 1
        if k == -1:
            return '-1'

    for i in range(n//2):
        if k == 0:
            break
        if arr[i] == 1:
            if s[i] != '9':
                s[i] = '9'
                s[n-i-1] = '9'
                k -= 1
        elif arr[i] == 0 and k>=2:
            if s[i] != '9':
                k -= 2
                s[i] = '9'
                s[n-i-1] = '9'
    if n%2 == 1 and s[n//2] != '9' and k>=1:
        s[n//2]='9'
    s1 = ''
    for i in s:
        s1 += i
    return s1

n, k = map(int, input().split())
s = input()
print(highestValuePalindrome(s,n,k))
# print(highestValuePalindrome('3943', 4, 100))