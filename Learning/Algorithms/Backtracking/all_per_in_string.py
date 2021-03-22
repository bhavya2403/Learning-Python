def solve(stringDict, answer, n):
    if len(answer) == n:
        print(answer)

    for char in stringDict:
        if stringDict[char]:
            stringDict[char] -= 1
            solve(stringDict, answer+char, n)
            stringDict[char] += 1

def allPer(string, n):
    stringDict = {}
    for char in string:
        if char not in stringDict:
            stringDict[char] = 1
        else:
            stringDict[char]  += 1
    solve(stringDict, '', n)


allPer('abac', 4)
