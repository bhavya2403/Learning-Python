for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    sumA = 0
    sumB = 0
    pick_zero = False
    if n%2:
        pick_zero = True
    for i in range(n):
        if pick_zero:
            if not i%2:
                if not arr[i]%2:
                    sumA += arr[i]
            else:
                if arr[i]%2:
                    sumB += arr[i]
        else:
            if not i%2:
                if arr[i]%2:
                    sumB += arr[i]
            else:
                if not arr[i]%2:
                    sumA += arr[i]
    if sumA==sumB:
        print('Tie')
    elif sumA>sumB:
        print('Alice')
    else:
        print('Bob')
