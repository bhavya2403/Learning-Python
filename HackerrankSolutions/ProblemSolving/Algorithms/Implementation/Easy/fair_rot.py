def fairRations(B):
    # 2 3 4 5 6
    count = 0
    for i in range(len(B)-1):
        if B[i] % 2 == 1:
            count += 2
            B[i+1] += 1
    if B[len(B)-1] % 2 == 1:
        return 'NO'
    return count

print(fairRations([4,5,6,8]))
