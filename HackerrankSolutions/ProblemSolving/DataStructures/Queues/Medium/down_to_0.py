from math import sqrt

def returnsPrime(n):
    arr = []
    if n == 2 or n == 3:
        return []
    i = int(sqrt(n)) + 1
    while i >= 2:
        if n % i == 0:
            arr.append(max(n / i, i))
        i -= 1
    return arr


def downToZero(n):
    count = 0
    while n:
        arr = returnsPrime(n)
        if j:
            n = j
        else:
            n -= 1
        count += 1
    return count

# for _ in range(int(input())):
#     n = int(input())
#     print(downToZero(n))

print(downToZero(812849))