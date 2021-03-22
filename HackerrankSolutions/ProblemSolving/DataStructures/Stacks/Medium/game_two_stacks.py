def twoStacks(s, a, b):
    sumA = [0]
    summ = 0
    for i in a:
        summ += i
        sumA.append(summ)
    summ = 0
    sumB = [0]
    for i in b:
        summ += i
        sumB.append(summ)
    count = 1
    while True: # O(n+m)
        got_less = False
        for i in range(count+1):
            try:
                rem_sum = sumA[i] + sumB[count-i]
                if rem_sum <= s:
                    got_less = True
                    break
            except:
                continue
        if not got_less:
            return count-1
        count += 1


# print(twoStacks(10, 5, 4, [4,2,4,6,1], [2,1,8,5]))
for g_itr in range(int(input())):
    n,m,x = map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    print(twoStacks(x, a, b))
