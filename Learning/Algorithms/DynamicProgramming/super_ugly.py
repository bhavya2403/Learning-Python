def superUgly(primes, n):
    ans = [0] * (n*n)
    for i in range(2, n*n):
        if not ans[i]:
            if i not in primes:
                for j in range(1, int(n*n/i)):
                    ans[i*j] = 2
            else:
                for j in range(2, int(n*n/i)):
                    if ans[i*j] == 2:
                        continue
                    ans[i*j] = 1

    count = 0
    for i in range(1, n*n):
        if ans[i] == 2:
            continue
        count += 1

        if count == n:
            return i

print(superUgly([3, 5, 7, 11, 13], 9))
