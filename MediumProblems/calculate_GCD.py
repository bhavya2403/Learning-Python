from math import sqrt

def gcd(numbers):
    num = min(numbers)
    sqrtNum = int(sqrt(num))
    factorsNum = [0] * (2*sqrtNum)
    for i in range(1, sqrtNum+1):
        if not num%i:
            factorsNum[i-1] = i
            factorsNum[2*sqrtNum-i] = num/i

    for i in range(2*sqrtNum-1, -1, -1):
        if not factorsNum[i]:
            continue

        for j in numbers:
            if j % factorsNum[i]:
                break
        else:
            return factorsNum[i]


# print(gcd([24,36,60]))





