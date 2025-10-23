'''
CSV Header Parser

Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

    The first line of a CSV file contains headings separated by commas.
    Remove any leading or trailing whitespace from each heading.
'''
def get_headings(csv):
    csv_array = csv.split(',')
    for index, item in enumerate(csv_array):
        csv_array[index] = item.strip()
    return csv_array

if __name__ == "__main__":
    print(get_headings("username , email , signup date "))

# Unit tests 
import unittest

'''
1. get_headings("name,age,city") should return ["name", "age", "city"].
2. get_headings("first name,last name,phone") should return ["first name", "last name", "phone"].
3. get_headings("username , email , signup date ") should return ["username", "email", "signup date"].
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("name,age,city", ["name", "age", "city"]),
                    ("first name,last name,phone", ["first name", "last name", "phone"]),
                    ("username , email , signup date ",["username", "email", "signup date"]),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(get_headings(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")
