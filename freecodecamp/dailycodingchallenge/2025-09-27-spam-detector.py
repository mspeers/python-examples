import re

'''
Spam Detector

Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

    A represents the country code and can be any number of digits.
    BBB represents the area code and will always be three digits.
    CCC and DDDD represent the local number and will always be three and four digits long, respectively.

Determine if it's a spam number based on the following criteria:

    The country code is greater than 2 digits long or doesn't begin with a zero (0).
    The area code is greater than 900 or less than 200.
    The sum of first three digits of the local number appears within last four digits of the local number.
    The number has the same digit four or more times in a row (ignoring the formatting characters).
'''
def is_spam(number):
    match = re.match(r"\+(\d+) \((\d{3})\) (\d{3})-(\d{4})", number)
    if (match == None):
        print("Failed no match")
        return False
    print (match.group())
    country_code_str = match.group(1)
    country_code_num = int(match.group(1))
    print(f"country_code_str: {country_code_str}, country_code_num:{country_code_num}")
    area_code_str = match.group(2)
    area_code_num = int(match.group(2))
    print(f"area_code_str: {area_code_str}, area_code_num:{area_code_num}")


    print(f"country code. len:{len(str(country_code_str))}")

    # The country code is greater than 2 digits long or doesn't begin with a zero (0).
    if ((len(str(country_code_num)) > 2 and country_code_str != "0")  ):
        print(f"Failed country code. len:{len(str(country_code_num))}")
        return False
    
    if (country_code_str == "00"):
        print(f"Failed country code. 00")
        return False

    # The area code is greater than 900 or less than 200.
    if (area_code_num == 200 or area_code_num == 900):
        print("Failed area code")
        return False
    
    # The sum of first three digits of the local number appears within last four digits of the local number.
    sum_local_number = match.group(3)
    if (str(match.group(4)).find(str(sum_local_number)) > 0):
        print("Failed first three digist appears in last digits of local number")
        return False

    #The number has the same digit four or more times in a row (ignoring the formatting characters).
    build_all_numbers = country_code_str+ area_code_str+str(match.group(3))+str(match.group(4))
    
    count =0
    match_count = ''

    for i, char in enumerate(build_all_numbers):
        if match_count != char:
            match_count = char
            count = 0
        else:
            if count > 3:
                print("Failed  same digit four or more times")
                return False
            count += 1

    return True

if (__name__ == "__main__"):
    print (is_spam("+00 (555) 234-0182")) #   False.

# Unit tests 
import unittest

'''
1. is_spam("+0 (200) 234-0182") should return False.
2. is_spam("+091 (555) 309-1922") should return True.
3. is_spam("+1 (555) 435-4792") should return True.
4. is_spam("+0 (955) 234-4364") should return True.
5. is_spam("+0 (155) 131-6943") should return True.
6. is_spam("+0 (555) 135-0192") should return True.
7. is_spam("+0 (555) 564-1987") should return True.
8. is_spam("+00 (555) 234-0182") should return False.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("+0 (200) 234-0182",     False),
                    ("+091 (555) 309-1922",   True),
                    ("+1 (555) 435-4792",     True),
                    ("+0 (955) 234-4364",     True),
                    ("+0 (155) 131-6943",     True),
                    ("+0 (555) 135-0192",     True),
                    ("+0 (555) 564-1987",     True),
                    ("+00 (555) 234-0182",    False),

                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(is_spam(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")
