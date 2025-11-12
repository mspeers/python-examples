

import re
VOWELS = ['a', 'e', 'i','o', 'u']
'''
Vowels and Consonants

Given a string, return an array with the number of vowels and number of consonants in the string.

    Vowels consist of a, e, i, o, u in any case.
    Consonants consist of all other letters in any case.
    Ignore any non-letter characters.

For example, given "Hello World", return [3, 7].
'''
def count(s):
    s_val = re.sub('[^\w]','', s)
    print (s_val)
    count_consonant = 0
    count_vowels = 0
    for letter in s_val:
        if letter in VOWELS:
            count_vowels += 1
        else:
            count_consonant += 1
    return [count_vowels, count_consonant]

if __name__ == "__main__":
    print(count("Hello World"))





