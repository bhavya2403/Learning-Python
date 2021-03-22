def lcs1(a, b):
    n1, n2 = len(a), len(b)
    matrix = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if a[i] == b[j]:
                matrix[i+1][j+1] = matrix[i][j] + 1
            else:
                matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])

    i += 1; j+= 1; arr = []
    while i >= 1 and j >= 1:
        if matrix[i-1][j-1] <= matrix[i][j-1]< matrix[i-1][j] or matrix[i-1][j-1] < matrix[i][j-1] == matrix[i-1][j]:
            i -= 1
        elif matrix[i-1][j-1] <= matrix[i-1][j]< matrix[i][j-1] or matrix[i-1][j-1] == matrix[i][j-1]== matrix[i-1][j]==matrix[i][j]:
            j -= 1
        else:
            arr.append(a[i-1])
            i -= 1; j-=1
    i = len(arr) - 1
    while i >= 0:
        print(str(arr[i]), end=' ')
        i -= 1


# print(lcs1([1,2,3,4,1], [3,4,1,2,1,3]))
nm = input().split()

n = int(nm[0])

m = int(nm[1])

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

lcs1(a, b)