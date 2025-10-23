
'''
Decimal to Binary

Given a non-negative integer, return its binary representation as a string.

A binary number uses only the digits 0 and 1 to represent any number. To convert a decimal number to binary, repeatedly divide the number by 2 and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert 12 to binary:

12 ÷ 2 = 6 remainder 0
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1

12 in binary is 1100.
'''
def to_binary(decimal):
    result = ""
    index = 1
    print (f"decimal:{decimal}")
    while(decimal > 0):
        result = str(decimal % 2) + result
        decimal //= 2

    return result

if __name__ == "__main__":
      print(to_binary(5))  
    

# Unit tests 
import unittest

'''
1. to_binary(5) should return "101".
2. to_binary(12) should return "1100".
3. to_binary(50) should return "110010".
4. to_binary(99) should return "1100011".
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (5,  "101"),
                    (12, "1100"),
                    (50, "110010"),
                    (99, "1100011"),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(to_binary(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")