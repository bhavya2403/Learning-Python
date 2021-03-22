def designerPdfViewer(h, word):
    abcd = 'abcdefghijklmnopqrstuvwxyz'
    index = 0
    maximum = []
    for char in abcd:
        for i in word:
            if i == 'char':
                maximum.append(h[index])
        index += 1

    return len(word) * max(maximum)
