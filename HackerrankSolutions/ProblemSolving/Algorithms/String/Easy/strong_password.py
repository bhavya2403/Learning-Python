def minimumNumber(n, password):
    special_characters = "!@#$%^&*()-+"
    num = 0
    low = 0
    upp = 0
    spe = 0
    need = 0
    need1 = 0
    for char in password:
        if char.isupper():
            upp += 1
        elif char.islower():
            low += 1
        else:
            if char not in special_characters:
                spe += 1
            else:
                num += 1
    if len(password) < 6:
        need1 += 6 - len(password)
    if num == 0:
        need += 1
    if upp == 0:
        need += 1
    if low == 0:
        need += 1
    if spe == 0:
        need += 1

    return max(need, need1)


print(minimumNumber(10, 'A98#+'))
