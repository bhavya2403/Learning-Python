def funnyString(s):
    i = 0
    j = len(s) - 1
    while j >= 1:
        if abs(ord(s[i+1]) - ord(s[i])) != abs(ord(s[j]) - ord(s[j-1])):
            return 'Not Funny'
        i += 1
        j -= 1

    return 'Funny'
