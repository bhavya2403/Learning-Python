def find_not_same(s, i, j):
    size = len(s)

    while i < size // 2:
        if s[i] != s[j]:
            return i, j
        i += 1
        j -= 1
    return False


def leftcase(s, i, j):
    s1 = s[i + 1:j + 1]
    s2 = s[i:j]
    if not find_not_same(s1, 0, len(s1) - 1):
        return i
    else:
        return j


def palindromeIndex(s):
    if not find_not_same(s, 0, len(s) - 1):
        return -1
    else:
        i, j = find_not_same(s, 0, len(s) - 1)
        if s[i + 1] == s[j] and s[i] == s[j - 1]:
            return leftcase(s, i, j)
        elif s[i + 1] == s[j]:
            return i
        elif s[i] == s[j - 1]:
            return j


# The solution which didn't pass in time(BUT CORRECT):
# def palindromeIndex(s):
#   if all(ord(s[i]) == ord(s[::-1][i]) for i in range(len(s) // 2)):
#        return -1
#    size = len(s)
#    for i in range(size):
#        j = 0
#        k = size - 1
#        count = 0
#        palindrome = True
#        while count < size // 2:
#            if j == i:
#                j += 1
#            elif k == i:
#                k -= 1

#            if s[j] != s[k]:
#                palindrome = False
#                break
#            j += 1
#            k -= 1
#            count += 1

#        if palindrome:
#            return i


print(palindromeIndex('abbab'))
