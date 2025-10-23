
'''
Phone Number Formatter

Given a string of eleven digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".
'''
def format_number(number):
    if (len(number) != 11):
        return False
    
    result = f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:11]}" 
    return result 

if __name__ == "__main__":
    print (format_number("05552340182"))



# Unit tests 
import unittest

'''
1. format_number("05552340182") should return "+0 (555) 234-0182".
2. format_number("15554354792") should return "+1 (555) 435-4792".
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("05552340182",   "+0 (555) 234-0182"),
                    ("15554354792",   "+1 (555) 435-4792"),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(format_number(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")