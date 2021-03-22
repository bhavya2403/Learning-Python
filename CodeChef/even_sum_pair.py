for i in range(int(input())):
    arr = input().split()
    x = int(arr[0])
    y = int(arr[1])
    print(((x - (x // 2)) * (y -(y // 2))) + ((x // 2) * (y // 2)))