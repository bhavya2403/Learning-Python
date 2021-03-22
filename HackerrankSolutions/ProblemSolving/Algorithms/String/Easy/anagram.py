def anagram(s):
    if len(s) % 2 != 0:
        return -1

    da = {}
    for i in range(len(s) // 2):
        if s[i] not in da:
            da[s[i]] = 1
        else:
            da[s[i]] += 1

    db = {}
    for i in range(len(s) // 2, len(s)):
        if s[i] not in db:
            db[s[i]] = 1
        else:
            db[s[i]] += 1

    totA = 0
    count = 0
    for i in da:
        if i in db:
            need = db[i] - da[i]
            if need > 0:
                totA -= need
                count += need
            elif need < 0:
                count += abs(need)
        else:
            totA += da[i]

    return totA + count


print(anagram('xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa'))
