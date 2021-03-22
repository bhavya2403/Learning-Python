def gemstones(arr):
    d = {}
    for char in arr[0]:
        if char not in d.keys():
            d[char] = 1

    for i in range(1, len(arr)):
        s = ''
        for char in arr[i]:
            if char in d.keys() and char not in s:
                d[char] += 1
                s += char

    count = 0
    for key in d.keys():
        if d[key] == len(arr):
            count += 1

    return count


print(gemstones(['abcdde', 'baccd', 'eeabg']))