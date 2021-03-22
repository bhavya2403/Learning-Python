def decodeHuff(root, s):
    itr = root
    for i in s:
        if i=='1':
            itr = itr.right
        elif i=='0':
            itr = itr.left
        if not itr.left and not itr.right:
            print(itr.data, end='')
            itr = root
