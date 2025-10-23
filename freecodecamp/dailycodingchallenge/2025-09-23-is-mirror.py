

import re


'''
String Mirror

Given two strings, determine if the second string is a mirror of the first.

    A string is considered a mirror if it contains the same letters in reverse order.
    Treat uppercase and lowercase letters as distinct.
    Ignore all non-alphabetical characters.
'''

def is_mirror(str1, str2):
    # remove non-alphabetical 
    str1 = re.sub(r'[^a-zA-Z0-9]', '', str1)
    str2 = re.sub(r'[^a-zA-Z0-9]', '', str2)

    if len(str1) != len(str2):
        return False
    size = len(str1) -1
    for index, item in enumerate(str1):
        # print("Index:"+str(index) +", size:"+str(size))
        if str1[index] != str2[(size - index)]:
            # print("1:"+ str1[index]+", 2:" + str2[(size - index)])
            return False
        
    return True

if __name__ == "__main__":
    print (is_mirror("helloworld", "helloworld"))


# Unit tests 
import unittest

'''
1. is_mirror("helloworld", "helloworld") should return False.
2. is_mirror("Hello World", "dlroW olleH") should return True.
3. is_mirror("RaceCar", "raCecaR") should return True.
4. is_mirror("RaceCar", "RaceCar") should return False.
5. is_mirror("Mirror", "rorrim") should return False.
6. is_mirror("Hello World", "dlroW-olleH") should return True.
7. is_mirror("Hello World", "!dlroW !olleH") should return True.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (("helloworld", "helloworld"), False),
                    (("Hello World", "dlroW olleH"),True),
                    (("RaceCar", "raCecaR"),True),
                    (("RaceCar", "RaceCar"),False),
                    (("Mirror", "rorrim"),False),
                    (("Hello World", "dlroW-olleH"),True),
                    (("Hello World", "!dlroW !olleH"),True),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(is_mirror(*test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")


