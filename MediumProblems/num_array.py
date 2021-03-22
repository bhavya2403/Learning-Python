# https://www.youtube.com/watch?v=PIeiiceWe_w

def phoneNumbers(s, arr):
    s_dict = {}
    for idx, char in enumerate(s):  # O(l)
        char = int(char)
        if char not in s_dict:
            s_dict[char] = {idx}
        else:
            s_dict[char].add(idx)
    num_to_str = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
    result = []

    def solve(i, prev_k, string):
        if i == len(string):
            return True

        char = string[i]
        j = num_to_str[ord(char) - ord('a')]
        if j not in s_dict:
            return False

        for k in s_dict[j]:
            if k == prev_k + 1 or not i:
                a = solve(i + 1, k, string)
                if a:
                    return True
        return False

    for string in arr:  # O(lm)
        if solve(0, -1, string):
            result.append(string)

    return result


print(phoneNumbers("3662277", ["foo", "bar", "baz", "foobar", "emo", "cap", "car", "cat"]))
