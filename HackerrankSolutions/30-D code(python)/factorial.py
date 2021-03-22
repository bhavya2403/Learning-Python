def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(5))


def fibonachhi(n):
    if n == 1 or n == 2:
        return 1
    num1 = 1
    num2 = 1
    num3 = 0
    for i in range(3, n+1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return num3


print(fibonachhi(1))
