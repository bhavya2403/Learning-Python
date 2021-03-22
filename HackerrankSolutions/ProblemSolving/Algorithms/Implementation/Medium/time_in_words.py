def timeInWords(h, m):
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    if m == 0:
        return arr[h] + " o' clock"
    elif m < 30:
        if m==15:
            return 'quarter past ' + str(arr[h])
        else:
            s = ' minutes'
            if m==1:
                s = ' minute'
            return str(arr[m]) + s + ' past ' + str(arr[h])
    elif m == 30:
        return 'half past ' + str(arr[h])
    else:
        if m==45:
            return 'quarter to ' + str(arr[h+1] if h!=12 else 'one')
        else:
            s = ' minutes'
            if m == 59:
                s = ' minute'
            return str(arr[60-m]) + s + ' to ' + str(arr[h+1] if h!=12 else 'one')

print(timeInWords(1, 59))