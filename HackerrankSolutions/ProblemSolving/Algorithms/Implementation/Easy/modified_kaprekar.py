def kaprekarNumbers(p, q):
    ans = '' if p > 4 else '1 '
    for num in range(p, q + 1):
        try:
            str_num = str(num)
            sq = num * num
            str_sq = str(sq)
            if len(str_sq) == (2 * len(str_num)) or len(str_sq) == (2 * len(str_num)) - 1:
                l = int(str_sq[:(len(str_sq) // 2)])
                r = int(str_sq[(len(str_sq) // 2):])
                if l + r == num:
                    ans += str(num) + ' '
        except:
            continue
    return ans if len(ans) != 0 else 'INVALID RANGE'

print(kaprekarNumbers(100, 300))