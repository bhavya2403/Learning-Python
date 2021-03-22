def binHex(a, n):
    num = 0
    for i in range(n):
        if a[i] == '1':
            num += 2 ** (n - i - 1)
    return num


def karatsuba(A, B, n):
    if n == 1:
        if A == '0' or B == '0':
            return 0
        return 1

    n = n // 2
    al, ar = A[:n], A[n:]
    bl, br = B[:n], B[n:]

    albl = karatsuba(al, bl, n)
    arbr = karatsuba(ar, br, n)

    al, ar = binHex(al, n), binHex(ar, n)
    bl, br = binHex(bl, n), binHex(br, n)

    return (2 ** (2 * n)) * (albl) + (2 ** n) * ((al + ar) * (bl + br) - albl - arbr) + arbr


def karatsubaUtil(A, B):
    lenA, lenB = len(A), len(B)
    maxL = max(lenA, lenB)
    num = 1
    pow = 0
    while num < maxL:
        num = 2 ** pow
        pow += 1
    n = (num % maxL) + maxL

    A = '0' * (n - lenA) + A
    B = '0' * (n - lenB) + B

    return karatsuba(A, B, n)


print(karatsubaUtil("111", "111"))
