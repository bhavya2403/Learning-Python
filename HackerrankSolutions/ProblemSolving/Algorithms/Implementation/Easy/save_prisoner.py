def save_prisoner(n, m, s):
    if m > n-s+1:
        m = m % n
        if s + m - 1 > n:
            return (s+m-1)-n
        return s+m-1
    else:
        return s + m - 1


print(save_prisoner(7,20,2))
