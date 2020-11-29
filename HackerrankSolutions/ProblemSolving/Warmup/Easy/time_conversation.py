def timeConversion(s):
    if s[8] == 'A' and s[0:2] == '12':
        s1 = '00' + s[2:8]
        return s1
    elif s[8] == 'P' and s[0:2] == '12':
        s1 = s[0:8]
        return s1
    elif s[8] == 'P' and s[0:2] != '12':
        s1 = str(12 + int(s[0:2])) + s[2:8]
        return s1
    elif s[8] == 'A' and s[0:2] != '12':
        s1 = s[0:8]
        return s1


print(timeConversion('12:45:54PM'))
