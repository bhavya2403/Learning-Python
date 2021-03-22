def combineTwo(strA, strB):
    i = 0
    m, n  = len(strA), len(strB)
    while i < min(m, n):
        if strB[i] != strA[i]:
            if not i:
                return ''
            return strB[:i]
        i += 1
    return strB[:i]

def longestCommonPrefix(arr, l, r):
    if l==r:
        return arr[l]

    m = (l+r)//2

    a = longestCommonPrefix(arr, l, m)
    b = longestCommonPrefix(arr, m+1, r)
    return combineTwo(a, b)

print(longestCommonPrefix(["geeksforgeeks", "geeks", "geek", "geezer"], 0, 3))