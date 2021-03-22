def permutationCoef(n, k):
    neu, den = 1, 1
    for i in range(1, k+1):
        den *= i
        neu *= n-i+1

    return neu//den
