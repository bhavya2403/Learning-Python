def binS(n, s):
    if s=='1':
        return 0
    zeros = [0 for _ in range(n)]
    count0 = 0
    count1 = 0
    onces = zeros.copy()
    for i in range(n-1, -1, -1):
        if s[i]=='0':
            count0+=1
        if s[n-i-1]=='1':
            count1 += 1
        zeros[i] = count0
        onces[n-i-1] = count1

    minimum = onces[n-1]
    for i in range(n):
        if i==n-1:
            count = onces[n-2] if s[i]=='1' else onces[n-2]+1
        elif i:
            count = onces[i-1] + zeros[i+1] if s[i]=='1' else onces[i-1] + zeros[i]
        else:
            count = zeros[0]
        if count < minimum:
            minimum = count
    return minimum

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(binS(n,s))
