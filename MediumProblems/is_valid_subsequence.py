# https://www.algoexpert.io/questions/Validate%20Subsequence

def isValidSubsequence(array, sequence):
    m, n = len(sequence), len(array)
    i, j = 0, 0
    while i < n and j < m:
        if array[i] == sequence[j]:
            j += 1
        i += 1

    return j == m

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [22, 25, 6]
print(isValidSubsequence(array, sequence))

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10, 11, 11, 11, 11]
print(isValidSubsequence(array, sequence))
