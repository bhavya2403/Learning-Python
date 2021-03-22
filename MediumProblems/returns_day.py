def returns_day(dd, mm, yyyy):
    (day, y, date) = (1,2000, 'Saturday')
    l_year = False
    if yyyy % 4 == 0:
        l_year = True
    if l_year:
        x = -1
    else:
        x = -2
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
    month_days_diff = [1, x, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]

    d_after_1stjan = 0
    d_bef_1stjan = 0
    y_count = yyyy - 2000
    if y_count == 0:
        if mm == 1:
            d_after_1stjan = 0
        else:
            for i in range(mm-1):
                d_after_1stjan += 30 + month_days_diff[i]
    else:
        ly_count = y_count // 4
        if l_year:
            ly_count -= 1
        d_bef_1stjan  += ((y_count-1)*365) + ly_count

        if mm == 1:
            d_after_1stjan = 0
        else:
            for i in range(mm-1):
                d_after_1stjan += 30 + month_days_diff[i]

    d_count = d_bef_1stjan + d_after_1stjan + dd

    if d_count >= 7:
        d_count = (d_count % 7)

    return days[d_count]

print(returns_day(17,1, 2006))
