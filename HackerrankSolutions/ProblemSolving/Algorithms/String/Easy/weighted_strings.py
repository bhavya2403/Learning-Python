def weightedUniformStrings(s, queries):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    se = set()
    factor = 1
    for i in range(len(s)-1):
        weight = alphabet.index(s[i]) + 1
        if s[i+1] == s[i]:
            factor += 1
            se.add(weight * factor)
        else:
            factor = 1
            se.add(weight)

    return se


print(weightedUniformStrings('abccddde', []))