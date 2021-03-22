def isValid(s):
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    count_dict = {}
    for char in d:
        if d[char] not in count_dict:
            count_dict[d[char]] = 1
        else:
            count_dict[d[char]] += 1

        if len(count_dict) == 3:
            return 'NO'
        elif len(count_dict)==2:
            once = False
            for count in count_dict:
                if count_dict[count] > 1:
                    if once:
                        return 'NO'
                    once = True
    arr = list(count for count in count_dict)
    try:
        if abs(arr[0]-arr[1]) > 1:
            if count_dict[arr[0]]==1==arr[0] or count_dict[arr[1]]==1==arr[1]:
                return 'YES'
            return 'NO'
    except:
        return 'YES'
    return 'YES'