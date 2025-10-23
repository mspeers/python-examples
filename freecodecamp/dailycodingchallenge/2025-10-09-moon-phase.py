

from datetime import datetime

'''
Space Week Day 6: Moon Phase

For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

    "New": days 1 - 7
    "Waxing": days 8 - 14
    "Full": days 15 - 21
    "Waning": days 22 - 28

After day 28, the cycle repeats with day 1, a new moon.

    Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
    You will not be given any dates before the reference date.
    Return the correct phase as a string.
'''
def moon_phase(date_string):

    date_format = "%Y-%m-%d"

    d0 = datetime.strptime("2000-01-05", date_format)
    d1 = datetime.strptime(date_string, date_format)
    delta = d1 - d0
    rem_days = delta.days % 28

    moon_name = "New"
    match rem_days:
        case rem_days if 8 <= rem_days <=  14:
            moon_name = "Waxing"
        case rem_days if 15 <= rem_days <=  21:
            moon_name = "Full"
        case rem_days if 22 <= rem_days <=  29:
            moon_name = "Waning"

    return moon_name

if __name__ == "__main__":
    print (moon_phase("2014-10-15"))


# Unit tests 
import unittest

'''
1. moon_phase("2000-01-12") should return "New".
2. moon_phase("2000-01-13") should return "Waxing".
3. moon_phase("2014-10-15") should return "Full".
4. moon_phase("2012-10-21") should return "Waning".
5. moon_phase("2022-12-14") should return "New".
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("2000-01-12", "New"),
                    ("2000-01-13", "Waxing"),
                    ("2014-10-15", "Full"),
                    ("2012-10-21", "Waning"),
                    ("2022-12-14", "New"),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(moon_phase(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")