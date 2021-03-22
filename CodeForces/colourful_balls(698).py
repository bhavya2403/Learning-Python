for _ in range(int(input())):
    n = int(input())
    numbers = input().split()
    d = {}
    for i in numbers:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    maximum = 0
    for i in d:
        if d[i] > maximum:
            maximum = d[i]

    print(maximum)