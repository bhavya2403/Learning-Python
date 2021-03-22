for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        arr[i] = [arr[i], i]
    arr.sort()
    sumArr = [0]*n
    sum = 0
    for i in range(n):
        sum += arr[i][0]
        sumArr[i] = sum

    if n == 1:
        print(1)
        print(1)
    else:
        incZero = True
        for i in range(n-2, -1, -1):
            if sumArr[i] < arr[i+1][0]:
                incZero = False
                break
        if incZero:
            i -= 1
        answer = []
        for j in range(i+1, n):
            answer.append(arr[j][1]+1)
        answer.sort()
        n = len(answer)
        print(n)
        for i in range(n):
            print(answer[i], end=' ')
        print()