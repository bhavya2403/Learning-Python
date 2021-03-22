def primeNumbers(P, S):
    arr = [0] * (1000)
    for i in range(2, 1000):
        if not arr[i]:
            for j in range(2, 1000//i):
                arr[i*j] = 1

    primes = []
    for i in range(P, 1000):
        if not arr[i]:
            primes.append(i)
        if i >= S:
            return primes


def solve(arr, n, sumOfSubset, eleTaken, sumEleTaken, sumLeft, currIdx, N):
    if sumEleTaken == sumOfSubset:
        print(eleTaken)
        return
    elif sumLeft < sumOfSubset - sumEleTaken:
        return

    if len(eleTaken) < N:
        for i in range(currIdx, n):
            if arr[i] + sumEleTaken <= sumOfSubset:
                eleTaken.append(arr[i])
                sumEleTaken += arr[i]
                sumLeft -= arr[i]

                solve(arr, n, sumOfSubset, eleTaken, sumEleTaken, sumLeft, i + 1, N)

                eleTaken.pop()
                sumEleTaken -= arr[i]
                sumLeft += arr[i]
            else:
                break


def sumSubsets(P, N, S):
    arr = primeNumbers(P, S)
    return solve(arr, len(arr), S, [], 0, sum(arr), 0, N)

sumSubsets(7,2,28)