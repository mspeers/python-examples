import re
from datetime import date


MSG = ["It's the weekend!", "%s days until the weekend.", "%s day until the weekend."]

'''
Is It the Weekend?

Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

    The weekend starts on Saturday.
    If the given date is Saturday or Sunday, return "It's the weekend!".
    Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
    If X is 1, use "day" (singular) instead of "days" (plural).
    Make sure the calculation ignores your local timezone.


'''

def days_until_weekend(date_string):
    

    date_break = re.match(r"(\d{4})-(\d{2})-(\d{2})",date_string)
    
    if date_break == None:
        return "Invalid date format: YYYY-MM-DD"
    # Create a date object
    year = int(date_break.group(1))
    mon = int(date_break.group(2))
    day = int(date_break.group(3))
    print(f"y:{year}, m:{mon}, d:{day}") 
    my_date = date(year, mon, day)

    # Get the weekday as an integer
    day_number = 5 - my_date.weekday()
    if day_number <= 0:
        return MSG[0]
    if day_number == 1:
        return MSG[2] % day_number


    return MSG[1] % day_number

if __name__ == "__main__":
    print(days_until_weekend("2025-11-14"))
'''
1. days_until_weekend("2025-11-14") should return "1 day until the weekend.".
2. days_until_weekend("2025-01-01") should return "3 days until the weekend.".
3. days_until_weekend("2025-12-06") should return "It's the weekend!".
4. days_until_weekend("2026-01-27") should return "4 days until the weekend.".
5. days_until_weekend("2026-09-07") should return "5 days until the weekend.".
6. days_until_weekend("2026-11-29") should return "It's the weekend!".
'''


# Unit tests 

import unittest
from parameterized import parameterized

class TestSequence(unittest.TestCase):
    @parameterized.expand([
        [ ("2025-11-14"), "1 day until the weekend."],
        [ ("2025-01-01"), "3 days until the weekend."],
        [ ("2025-12-06"), "It's the weekend!"],
        [ ("2026-09-07"), "5 days until the weekend."],
        [ ("2026-11-29"), "It's the weekend!"],
    ])
    def test_sequence(self, test_data, expected):
        # self.assertEqual(test_data,expected)
        self.assertEqual(days_until_weekend(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
        print(f"Expect:{expected}, test_data:{test_data}")