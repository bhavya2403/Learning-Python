def happyLadybugs(b):
    if '_' not in b:
        for i in range(1, len(b) - 1):
            if b[i - 1] != b[i] and b[i + 1] != b[i]:
                return 'NO'
    for i in b:
        if b.count(i) == 1 and i != '_':
            return 'NO'
    return 'YES'