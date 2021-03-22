def marsExploration(s):
    count = 0
    for i in range(len(s)):
        if i % 3 == 0 or i % 3 == 2:
            if s[i] != 's':
                count += 1
        else:
            if s[i] != 'o':
                count += 1

    return count


print(marsExploration('sosspssqssor'))