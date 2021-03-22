def makeSignature(string):
    sign = [0] * 26
    for char in string:
        sign[ord(char)-ord('a')] += 1
    return sign

def anagrams(arr):
    answer = []
    lenAnswer = 0
    signDict = {}
    for string in arr:
        sign = makeSignature(string)
        sign = str(sign)
        if sign not in signDict:
            answer.append([string])
            signDict[sign] = lenAnswer
            lenAnswer += 1
        else:
            answer[signDict[sign]].append(string)
    return answer

print(anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
