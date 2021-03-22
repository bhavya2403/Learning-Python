def caesarCipher(s, k):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    if k > len(alpha):
        k = k % len(alpha)
    s1 = ''
    for i in s:
        if i.isupper():
            ind = alpha.index(i.lower())
            if ind + k >= len(alpha):
                ind -= len(alpha)
            s1 += alpha[(ind + k)].upper()
        elif i.islower():
            ind = alpha.index(i)
            if ind + k >= len(alpha):
                ind -= len(alpha)
            s1 += alpha[(ind + k)]
        else:
            s1 += str(i)

    return s1


print(caesarCipher('www.abc.xy', 87))
