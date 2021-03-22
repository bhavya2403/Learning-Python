for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    min = a[0]
    max = a[0]
    for i in a:
        if i > max:
            max = i
        if i < min:
            min = i
    print(2*(max-min))
