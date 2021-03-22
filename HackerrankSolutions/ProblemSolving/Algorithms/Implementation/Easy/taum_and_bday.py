def taumBday(b, w, bc, wc, z):
    if abs(bc - wc) <= z:
        return b*bc + w*wc
    else:
        c1 = (b+w)*bc + (z*w)
        c2 = (b+w)*wc + (z*b)
        return min(c1, c2)
