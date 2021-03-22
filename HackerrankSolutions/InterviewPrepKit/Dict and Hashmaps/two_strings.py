def twoStrings(s1, s2):
    for char in s1:
        if char in s2:
            return 'YES'
    return 'NO'