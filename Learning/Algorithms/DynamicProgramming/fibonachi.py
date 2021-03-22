def fib(n):  # O(2^n)(size of binary tree(no of times func called))
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# print(fib(10))

def fib_iterative(n):  # O(n)
    if n <= 1:
        return n
    result, a, b = 0, 0, 1
    for i in range(2, n + 1):
        result = a + b
        a, b = b, result
    return result


# print(fib_iterative(100))

# MEMOIZATION METHOD(follows top bottom approach)(means we want fib(100) we started from 100)
# memoization means if we are calling same recursive function again we should try to avoid it and store the result of already called result somewhere
def fib_dp_mem(n,
               arr):  # O(n) (in arr we will store the value of fib which is already called and we are not gonna call it again)
    if n <= 1:
        return n

    if arr[n - 1] != -1:
        a = arr[n - 1]
    else:
        a = fib_dp_mem(n - 1, arr)
        arr[n - 1] = a

    if arr[n - 2] != -1:
        b = arr[n - 2]
    else:
        b = fib_dp_mem(n - 2, arr)
        arr[n - 2] = b

    return a + b


# print(fib_dp_mem(100, [0,1] + [-1 for _ in range(2, 101)]))

# TABULATION METHOD(follows bottom up approach) (means we want fib(100) we started from 0)
def fib_dp_tab(n):  # O(n)
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[i]
# print(fib_dp_tab(100))
