def countSort(n, arr):
    aux = []
    for i in range(n):
        aux.append([])
    for i in range(int(n/2)):
        aux[arr[i][0]].append('-')
    for i in range(int(n/2), n):
        aux[arr[i][0]].append(arr[i][1])
    for i in aux:
        for j in i:
            print(j, end=' ')


n = int(input().strip())

arr = []

for _ in range(n):
    a = input().rstrip().split()

    arr.append([int(a[0]), a[1]])

countSort(n, arr)