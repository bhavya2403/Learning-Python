def gameOfThrones(s):
    count = 0
    for char in set(s):
        if s.count(char) != 0:
            count += 1
        if count == 2:
            return 'NO'

    return 'YES'
    # j = ''
    # for i in s:
    #     if s.count(i) % 2 == 1:
    #         if j == '':
    #             j = i
    #         elif i != j:
    #             return 'NO'
    # return 'YES'


print(gameOfThrones('cdcdcdcdeeeef'))
