def findDigits(n):
    count = 0
    for num in str(n):
        try:
            if n % int(num) == 0:
                count += 1
        except:
            count = count

    return count
