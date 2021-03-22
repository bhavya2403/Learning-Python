from math import sqrt

def formPrimes(q):
    if q == 1:
        return [2]
    if q == 2:
        return [2, 3]
    primes = [2, 3]
    count, i = 2, 4
    while True:
        if all(i % j != 0 for j in range(2, int(sqrt(i))+1 if i > 9 else i)):
            primes.append(i)
            count += 1
        if count == q:
            break
        i += 1
    return primes


def waiter(A, q):
    matB = []
    primes = formPrimes(q)
    for i in primes:
        auxA = []
        B = []
        for j in range(len(A)):
            val = A.pop()
            if val % i == 0:
                B.append(val)
            else:
                auxA.append(val)
        A = auxA
        matB.append(B)

    s = ''
    for i in matB:
        size = len(i)
        for j in range(size):
            s += str(i[size - 1 - j]) + '\n'
    size = len(A)
    for i in range(size):
        s += str(A[size - 1 - i]) + '\n'

    return s

n, q = map(int, input().split())
numbers = list(map(int, input().split()))
print(waiter(numbers, q))
# print(formPrimes(21))