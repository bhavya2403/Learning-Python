def isBalanced(s):
    if len(s) % 2 == 1:
        return 'NO'
    new_len = 0
    old_len = len(s)
    while new_len < old_len:
        old_len = len(s) # after this everytime old_len will be equal to new_len
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
        new_len = len(s) # if none of above three operations apply then no change
        # in new_len and old_len and loop will break
        # at the time of loop break if s is not empty then return NO
    if len(s) == 0:
        return 'YES'
    else:
        return 'NO'


print(isBalanced('{[(])()}'))
