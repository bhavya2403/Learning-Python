def timeConversion(s):
    if s[8] == 'P':
        if s[0:2] is not 12:
            s1 = int(s[0:2])
            s1 += 12
            s.delete([0])
            s.delete([0])
            s.insert(0, s1)
        s.delete('P')
    else:
        s.delete('A')
    s.delete('M')

    return s


print(timeConversion('12:01:00PM'))
