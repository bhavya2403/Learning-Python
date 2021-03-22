def search(matrix, key, l, r, u, d, m1, m2):
    if l > r:
        return False
    else:
        m1 = (l+r)//2
        # if matrix[]