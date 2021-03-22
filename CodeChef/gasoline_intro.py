for i in range(int(input())):
    size = int(input())
    arr = input().split()

    gas = 0
    dist = 0
    i = 0
    for i in range(size):
        gas += int(arr[i])
        if gas == 0:
            print(dist)
            break
        dist += 1
        gas -= 1
    if gas != 0:
        dist += gas
        print(dist)


# 1 2 3 4