

import re

'''
P@ssw0rd Str3ngth!

Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

A password is evaluated according to the following rules:

    It is at least 8 characters long.
    It contains both uppercase and lowercase letters.
    It contains at least one number.
    It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.

Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.
'''
def check_strength(password):
    rules = 0
    special_characters = ('!', '@', '#', '$', '%', '^', '&', '*')

    # It is at least 8 characters long.
    if (len(password) >=8 ):
        rules += 1
        # print("Add Lenght")
        
    # It contains both uppercase and lowercase letters.
    if re.search("[A-Z]+",password) != None and  re.search("[a-z]+",password) != None:
        # print("Add Lower")
        rules += 1
    # It contains at least one number.
    if (re.search("\d+", password) != None):
        # print("Add Number")
        rules += 1

    for schar in special_characters:
        if password.find(schar) != -1:
            # print("Add Special Char")
            rules += 1
            break

    strength ="weak"
    if rules >= 2 and rules < 4:
        strength = "medium"
    elif rules >= 4:
        strength = "strong"

    return strength

if __name__ == "__main__":
    print (check_strength("pass!!!"))


# Unit tests 
import unittest

'''
1. check_strength("123456") should return "weak".
2. check_strength("pass!!!") should return "weak".
3. check_strength("Qwerty") should return "weak".
4. check_strength("PASSWORD") should return "weak".
5. check_strength("PASSWORD!") should return "medium".
6. check_strength("PassWord%^!") should return "medium".
7. check_strength("qwerty12345") should return "medium".
8. check_strength("S3cur3P@ssw0rd") should return "strong".
9. check_strength("C0d3&Fun!") should return "strong".
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("123456",      "weak"),
                    ("pass!!!",     "weak"),
                    ("Qwerty",      "weak"),
                    ("PASSWORD",    "weak"),

                    ("PASSWORD!",   "medium"),
                    ("PassWord%^!", "medium"),
                    ("qwerty12345", "medium"),

                    ("S3cur3P@ssw0rd",    "strong"),
                    ("C0d3&Fun!",    "strong"),

                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(check_strength(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")


