for _ in range(int(input())):
    n, m = map(int,input().split())
    arrA = list(map(int,input().split()))
    arrB = list(map(int,input().split()))
    arr_V = [0]
    Vs = [0]
    while True:
        found1 = False
        found2 = False
        for v in Vs:
            count = 0
            for j in arrA:
                num = v | j
                if num not in arr_V:
                    found1 = True
                    count += 1
                    arr_V.append(num)

            for j in arrB:
                num = v & j
                if num not in arr_V:
                    found2 = True
                    count += 1
                    arr_V.append(num)

        if not found1 and not found2:
            break
        Vs = arr_V[-count:]

    print(len(arr_V))
