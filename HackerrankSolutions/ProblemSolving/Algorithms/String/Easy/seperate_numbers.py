def separateNumbers(s):
    # 999 1000 1001
    # 7 8 9 10 11
    # 98 99 100
    # 1 2 3 4 5 6
    if s == '010203' or len(s) == 1:
        return 'NO'
    n = 0
    i = 0
    temp = 0
    while True:
        if n == len(s) // 2:
            if int(s[i:i+n+1]) == (10**n):
                return 'YES ' + temp
            return 'NO'
        if i == len(s)-n-1:
            break
        temp = s[i:i+n+1]
        while True:
            if i == len(s) - n - 1:
                break

            if int(s[i:i+n+1]) == (10**(n+1)) - 1:
                if int(s[i+n+1:i+(2*n)+3]) != 10**(n+1):
                    i = 0
                    n += 1
                    break
                else:
                    i += n+1
                    n += 1

            elif int(s[i:i+n+1]) != int(s[i+n+1:i+(2*n)+2]) - 1:
                i = 0
                n += 1
                break
            else:
                i += n+1
                if i == len(s) - (2 * n) - 1:
                    break

    return 'YES '+ temp


print(separateNumbers('8910'))
