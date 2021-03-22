def repeatedString(s, n):
    count = 0
    for char in s:
        if char == 'a':
            count += 1
    result = count * (n // len(s))

    num = n - (len(s) * (n // len(s)))
    index = 0
    for char in s:
        if index < num:
            if char == 'a':
                result += 1
        elif index == num:
            break
        index += 1

    return result


print(repeatedString("aba", 10))
