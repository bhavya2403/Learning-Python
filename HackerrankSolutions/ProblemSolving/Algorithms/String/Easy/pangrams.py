def pangrams(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in s.lower():
            return 'not pangram'
    return 'pangram'


print(pangrams('We promptly judged antique ivory buckles for the next prize'))
