def alternatingCharacters(s):
    temp = len(s)
    index = 0
    s1 = ''
    while True:
        while True:
            if s[index] == 'A':
                if s[index + 1] == 'A':
                    s = s.replace(s[index+1], '')
                    break
                else:
                    index += 1
            elif s[index] == 'B':
                if s[index + 1] == 'B':
                    s = s.replace(s[index + 1], '')
                    break
                else:
                    index += 1
            if index+1 == len(s):
                break
        if index+1 == len(s):
            break

    return temp - len(s)


print(alternatingCharacters('ABAAAB'))