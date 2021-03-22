def hackerrankInString(s):
    s1 = 'hackerrank'
    j = 0

    for char in s1:
        found = False
        for ind in range(j, len(s)):
            if s[ind] == char:
                j = ind + 1
                found = True
                break

        if not found:
            return 'NO'
    return 'YES'


print(hackerrankInString('hackerworld'))
