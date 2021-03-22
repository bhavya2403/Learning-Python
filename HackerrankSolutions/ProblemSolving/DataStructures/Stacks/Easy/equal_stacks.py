def equalStacks(h1, h2, h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    sum1, sum2, sum3 = sum(h1), sum(h2), sum(h3)
    maxim = max(sum1, sum2, sum3)
    while True:
        if sum1 == sum2 == sum3:
            return sum1
        elif maxim == sum1:
            sum1 -= h1.pop()
            maxim = max(sum1, sum2, sum3)
        elif maxim == sum2:
            sum2 -= h2.pop()
            maxim = max(sum1, sum2, sum3)
        elif maxim == sum3:
            sum3 -= h3.pop()
            maxim = max(sum1, sum2, sum3)
        elif maxim == sum1 == sum2:
            sum1 -= h1.pop()
            maxim = max(sum1, sum2, sum3)
        elif maxim == sum2 == sum3:
            sum2 -= h2.pop()
            maxim = max(sum1, sum2, sum3)
        elif maxim == sum3 == sum1:
            sum1 -= h1.pop()
            maxim = max(sum1, sum2, sum3)

print(equalStacks([3,2,1,1,1], [4,3,2], [1,1,4,1]))