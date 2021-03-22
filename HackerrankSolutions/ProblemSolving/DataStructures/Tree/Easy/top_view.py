def get_level(root, value):
    level = 0
    itr = root
    while value != itr.info:
        if value > itr.info:
            itr = itr.right
            level += 1
        elif value < itr.info:
            itr = itr.left
            level += 1

    return level


def topView(root):
    def calculate(root, node, hd, level, d):
        if hd not in d:
            level = get_level(root, node.info)
            d[hd] = [[level, node.info]]
        else:
            d[hd].append([get_level(root, node.info), node.info])

        if node.left:
            calculate(root, node.left, hd - 1, level, d)

        if node.right:
            calculate(root, node.right, hd + 1, level, d)

        return d

    d = calculate(root, root, 0, 0, {})
    for key in sorted(d):
        d[key].sort()
        print(str(d[key][0][1]), end=' ')
