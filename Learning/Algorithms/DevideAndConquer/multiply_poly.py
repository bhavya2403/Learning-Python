# brute force
def multiply(a, b, m, n):
    answer = [0] * (m+n-1)
    for i in range(m):
        for j in range(n):
            answer[i+j] = a[i] * b[j]

    return answer

