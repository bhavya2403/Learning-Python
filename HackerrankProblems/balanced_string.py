def isBalanced(s):
    if len(s) % 2 == 1:
        return 'NO'
    new_len = 0
    old_len = len(s)
    while new_len < old_len:
        old_len = len(s)
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
        new_len = len(s)
    if len(s) == 0:
        return 'YES'
    else:
        return 'NO'
