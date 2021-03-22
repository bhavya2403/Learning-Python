# MEMEOIZATION
def matrixChainMultiplication(matrices):
    # matrices = [(2,3), (3,4), (4,2)]
    # formula: cost[i,j] = min(c[i,k]+c[k,j] for k in range(i+1,j)) if i+1!=j
    # else if i(1)==j(0) cost[i,j] = i(0)*i(1)*j(1)
    n = len(matrices)
    c = [[0 for _ in range(n)] for _ in range(n)]
    l = [[0 for _ in range(n)] for _ in range(n)]
    d = [matrices[0][0]]
    for i in matrices:
        d.append(i[1])

    for j in range(1, n): # O(n3)
        for i in range(n-j):
            min = 100
            min_idx = 0
            for k in range(i, j+i):
                num = c[i][k] + c[k+1][j+i] + d[i]*d[k+1]*d[j+i+1]
                if num < min:
                    min = num
                    min_idx = k
            c[i][j+i] = min
            l[i][j+i] = min_idx
    arr = []
    for i in range(n): # we put the brackets at arr[idx] in this case, (((A1))A2A3)A4
        arr.append(l[0][i]+1)
    return c[0][n-1],arr[1:]
print(matrixChainMultiplication([(3,2), (2,4), (4,2), (2,5)]))