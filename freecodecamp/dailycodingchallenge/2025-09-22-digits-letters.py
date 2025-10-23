

import re

'''
Digits vs Letters

Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.

    Digits consist of 0-9.
    Letters consist of a-z in upper or lower case.
    Ignore any other characters.
'''
def digits_or_letters(s):
    letters = re.sub(r'[^a-zA-Z]', '', s)
    digits = re.sub(r'[^0-9]', '', s)
    if (len(letters)> len(digits)):
        return "letters"
    elif (len(letters)< len(digits)):
        return "digits"
    else:
        return "tie"

 


# Unit tests 
import unittest

'''
1. digits_or_letters("abc123") should return "tie".
2. digits_or_letters("a1b2c3d") should return "letters".
3. digits_or_letters("1a2b3c4") should return "digits".
4. digits_or_letters("abc123!@#DEF") should return "letters".
5. digits_or_letters("H3110 W0R1D") should return "digits".
6. digits_or_letters("P455W0RD") should return "tie".
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (("abc123"),"tie"),
                    (("a1b2c3d"),"letters"),
                    (("1a2b3c4"),"digits"),
                    (("abc123!@#DEF"),"letters"),
                    (("H3110 W0R1D"), "digits"),
                    (("P455W0RD"), "tie")
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(digits_or_letters(*test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")

