

import re
'''
Fingerprint Test

Given two strings representing fingerprints, determine if they are a match using the following rules:

    Each fingerprint will consist only of lowercase letters (a-z).
    Two fingerprints are considered a match if:
        They are the same length.
        The number of differing characters does not exceed 10% of the fingerprint length.
'''

def is_match(fingerprint_a, fingerprint_b):
    a_low_filter = re.sub("[^a-z]","",fingerprint_a)
    b_low_filter = re.sub("[^a-z]","",fingerprint_b)
    size = len(a_low_filter) 
    if (len(a_low_filter) != len(b_low_filter)):
        print(f"DEBUG: len don't match '{a_low_filter}' vs '{b_low_filter}' ")
        return False
    count = 0
    for index, word_a in enumerate( a_low_filter ):
        if (word_a == b_low_filter[index]):
            count += 1

    percent = (count / size) * 100 
    print(f"percent:{percent}")
    if percent >= 90:
        return True
    return False


'''
1. is_match("helloworld", "helloworld") should return True.
Waiting: 2. is_match("helloworld", "helloworlds") should return False.
Waiting: 3. is_match("helloworld", "jelloworld") should return True.
Waiting: 4. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") should return True.
Waiting: 5. is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") should return True.
Waiting: 6. is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") should return False.
'''

if __name__ == "__main__":
    print(is_match("helloworld", "helloworlds"))
    print(is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog"))



