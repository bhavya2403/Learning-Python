def plusMinus(arr):
    nagatives = 0
    positives = 0
    zeros = 0
    for i in arr:
        if i > 0:
            positives += 1
        if i < 0:
            nagatives += 1
        if i == 0:
            zeros += 1
    print(round((positives / len(arr)), 6))
    print(round((nagatives / len(arr)), 6))
    print(round((zeros / len(arr)), 6))

plusMinus([-4,3,-9,0,4,1])