# submit this solution in pypy3(it is giving TLE in python3)

def commonChild(s1, s2):
    n = len(s1)
    matrix = []
    for i in range(n+1):
        arr = []
        for J in range(n + 1):
            arr.append(0)
        matrix.append(arr)
    for i in range(n):
        for j in range(n):
            if s1[i] == s2[j]:
                matrix[i+1][j+1] = matrix[i][j] + 1
            else:
                matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])

    return matrix[i+1][j+1]


print(commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))