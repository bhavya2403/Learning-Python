def alternatingCharacters(s):
    index = 0
    count = 0
    while index < len(s)-1:
        if s[index] == 'A':
            for i in range(index+1, len(s)):
                if s[i] == 'B':
                    index += 1
                    break
                else:
                    index += 1
                    count += 1
        else:
            for i in range(index + 1, len(s)):
                if s[i] == 'A':
                    index += 1
                    break
                else:
                    index += 1
                    count += 1
    print(s)
    return count


print(alternatingCharacters('BABABBBBBABBABBBAAABBBBBBBBABBBBBABBBAABBBBABBBBBBBAABABBBBBBABBABBBBBBBBBABBBBBABBABBBBABABBBBBBBBBBBBBBBBBBBABBBBBAABABBBBBBBBBBBABABBBABBBABBBBBBBBBBABBBBBABBBABBBABBABBBBBBAABBBABABBBAABABAABBBBAABBBBBBBBBAAABBABABBABBBABBBBABBBBBABABBBBABABBBAABBABBAABBBBBBABBABBBBBBBBBBBBBBBBBABBBBBBABBBBBBBBABBABBBBBBBBBAAABBBBBBBBBABBABABBBAAABBBBBBABBABBBBBBBABBBBBABBBABBAABAABAAABABBBBBBBABBBBABBBBBABBBBBBABBABBBBBBBBBBBBBBBBBABBABBBAABBBBBAABABBBBBBAABBBBBBBBBABBBBBABBABBBBBBBBBABBBBBBABBBABBBBBABBBBBBBBBBBBBBBBBBABBBBBBBBBBABBBBABABBBBBBBBABBBBBBBBBABBBBBAAABBBBABABABBBBABBBBBBBBBBAABBBBBBBBABBAABBBBBBBBBABAABBBBBBBBBBBBABBBBABABBBBBBBBABBBBBBBBBBBBABBBBABBBBBABBBBBBBBBBABBAABBBABBBBBBBBBABBBBAABBBBBBBBABABABBBBBABBBBBBBBBBBBBBBBBBABBBBABBBBBABBABABAABBBABBBBBBBBBAABABABBBBBBBBAABBBBABBABBBABBBBAABBABABBBBABAABBBBBBBBBBABBABBBBBABAABBBBBBBBBBBBABABBBBBBBBBBABAABABBBBABBBBBBBBBBBBBABBBBBABBABBAABBBBABBBBBBBBBBBAABBBBBBBBBBBBBBAABABBBBBABBBBBBBBBABBBBABBBBABABBABBBBABABBBABABAAABBBBAAAAAABBBA'))
