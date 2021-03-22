from math import ceil, sqrt

def calcRoot(a, b, c):
    d = b*b - 4*a*c
    return ((-b + sqrt(d))/2)

def numberDays(l, c):
    return calcRoot(1, 3-2*l, 2+l-(l*l)-(2*c))


print(numberDays(5,9))