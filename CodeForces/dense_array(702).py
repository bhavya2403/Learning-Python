for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        num = 2*(min(a[i], a[i+1]))
        while num < max(a[i], a[i+1]):
            num *= 2
            count += 1
    print(count)
