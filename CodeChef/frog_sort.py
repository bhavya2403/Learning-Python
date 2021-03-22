def sorting(arr):
    arr.sort(key=lambda a:a[2])
    reversing = set()
    i = 0
    while i < n-1:
        j = i
        while j<n-1:
            if arr[j+1][2]==arr[j][2]:
                j += 1
            else:
                break
        if i!=j:
            reversing.add((i, j))
        i = j+1
    for i, j in reversing:
        arr[i:j+1] = sorted(arr[i:j+1], key=lambda a:a[0], reverse=True)

    return arr

def frogSort(n, w, l):
    arr = []
    for i in range(n):
        arr.append([w[i], l[i], i])

    totJumps = 0
    while True:
        notSorted = False
        for i in range(n-1):
            if arr[i+1][0] < arr[i][0]:
                arr[i][2] += arr[i][1]
                totJumps += 1
                notSorted = True

        if not notSorted:
            break
        arr = sorting(arr)

    return totJumps

for _ in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    l = list(map(int, input().split()))
    print(frogSort(n, w, l))