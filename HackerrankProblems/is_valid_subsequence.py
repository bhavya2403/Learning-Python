def isValidSubsequence(array, sequence):
    index = 0
    while index < len(array) and index < len(sequence):
        if array[index] == sequence[index]:
            index += 1
        else:
            array.remove(array[index])

    print(array)
    print(sequence)
    # below line checks that if seqIdx variable reaches the length of sequence
    return index == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [22, 25, 6]
print(isValidSubsequence(array, sequence))

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10, 11, 11, 11, 11]
print(isValidSubsequence(array, sequence))
