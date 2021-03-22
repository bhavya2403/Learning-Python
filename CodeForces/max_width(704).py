import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = input()
flD = {}
for idx, char in enumerate(s):
    if char not in flD:
        flD[char] = [idx, idx]
    else:
        flD[char][1] = idx

t = input()
maxL = 0
for i in range(m-1):
    l, r = flD[t[i]][0], flD[t[i+1]][1]
    if r-l > maxL:
        maxL = r-l

print(maxL)