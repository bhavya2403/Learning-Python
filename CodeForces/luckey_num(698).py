for _ in range(int(input())):
    q, d = map(int, input().split())
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num %d == 0 or num >= d*10:
            print('YES')
        else:
            broken = False
            while num>=d:
                num -= d
                if num%10 == 0:
                    broken = True
                    print('YES')
                    break
            if not broken:
                print('NO')