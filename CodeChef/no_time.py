n, h, x = map(int, input().split())
t = list(map(int, input().split()))
for time in t:
    if x+time >= h:
        print("YES")
        break
else:
    print("NO")
