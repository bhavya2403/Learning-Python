def icecreamParlor(m, arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                return [i+1,j+1]


t = int(input())

for t_itr in range(t):
    m = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(icecreamParlor(m, arr))

