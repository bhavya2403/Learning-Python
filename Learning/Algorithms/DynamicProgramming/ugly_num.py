def uglyNumbers(n):
    if n == 1:
        return 1
    i2, i3, i5 = 0, 0, 0
    ugly = [0] * (n)
    ugly[0] = 1
    for i in range(1, n):
        num = min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
        ugly[i] = num
        if num == ugly[i2]*2:
            i2 += 1
        if num == ugly[i3]*3:
            i3 += 1
        if num == ugly[i5]*5:
            i5 += 1

    return ugly[n-1]


print(uglyNumbers(19))