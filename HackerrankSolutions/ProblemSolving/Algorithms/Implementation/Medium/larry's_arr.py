def rotate(i, j, A, d):
    arr = A[i:j + 1]
    num = arr.pop()
    arr.insert(0, num)
    A[i:j + 1] = arr
    for k in range(j - i + 1):
        d[arr[k]] = i + k

    return A, d


def larrysArray(n, A):
    d = {}
    for i in A:
        d[A[i - 1]] = i - 1

    for i in range(1, n - 1):
        idx = d[i]
        if i - 1 == idx:
            continue
        size = idx - i + 2
        if size % 2 == 1:
            A, d = rotate(i - 1, idx, A, d)
        else:
            A, d = rotate(i, idx, A, d)
            d[A[i - 1]] += 2
            d[A[i]] -= 1
            d[A[i + 1]] -= 1
            A[i], A[i - 1] = A[i - 1], A[i]
            A[i + 1], A[i] = A[i], A[i + 1]

    if A[n - 2] < A[n - 1]:
        return 'YES'
    return 'NO'


t = int(input())

for t_itr in range(t):
    n = int(input())

    A = list(map(int, input().rstrip().split()))

    print(larrysArray(n, A))
