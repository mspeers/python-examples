import re
import math
'''
Binary to Decimal

Given a string representing a binary number, return its decimal equivalent as a number.

A binary number uses only the digits 0 and 1 to represent any number. To convert binary to decimal, multiply each digit by a power of 2 and add them together. Start by multiplying the rightmost digit by 2^0, the next digit to the left by 2^1, and so on. Once all digits have been multiplied by a power of 2, add the result together.

For example, the binary number 101 equals 5 in decimal because:

1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
'''
def to_decimal(binary):
    if (re.match("[0-1]*", binary) == False):
        return None
    total = 0
    # flip
    for i, item in enumerate(reversed(binary)):
        by = 1
        if (i == 0):
            1 
        else:
            by = pow(2,i)
        add = int(item) * by 
        # print("Total " + str(total) + ": +"+ str(add)+" " + " (" +item + " * "+str(by)+")")
        total += add
    return total


if __name__ == "__main__":
    print(to_decimal("101"))
    print(to_decimal("1010"))
    print(to_decimal("10010"))

# Unit tests 
import unittest

'''
1. to_decimal("101") should return 5.
2. to_decimal("1010") should return 10.
3. to_decimal("10010") should return 18.
4. to_decimal("1010101") should return 85.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("101", 5),
                    ("1010", 10),
                    ("10010",18),
                    ("1010101",85),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(to_decimal(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")

