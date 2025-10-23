import re

'''
Slug Generator

Given a string, return a URL-friendly version of the string using the following constraints:

    All letters should be lowercase.
    All characters that are not letters, numbers, or spaces should be removed.
    All spaces should be replaced with the URL-encoded space code %20.
    Consecutive spaces should be replaced with a single %20.
    The returned string should not have leading or trailing %20.
'''
def generate_slug(str):
    result = str.lower()
    result_lead = result.strip()
    result_sub = re.sub('[^a-zA-Z0-9_ ]', '', result_lead)

    result_space = result_sub.replace(" ","%20")
    result_space = result_space.replace("%20%20","%20")

    return result_space

'''
Manual run in dev
'''
if __name__ == "__main__":
    print("Test:"+ generate_slug(" hello  World!"))

# Unit tests 
import unittest

'''
1. generate_slug("helloWorld") should return "helloworld". Waiting: 
2. generate_slug("hello world!") should return "hello%20world".
3. generate_slug(" hello-world ") should return "helloworld".
4. generate_slug("hello  world") should return "hello%20world".
5. generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ") should return "h3110%20w0r1d".
'''
class TestSlug(unittest.TestCase):
    def test_sample(self):
        results = [ ("helloWorld","helloworld"),
                  ("hello world!","hello%20world"),
                  (" hello-world ","helloworld"),
                  ("hello  world","hello%20world"),
                  ("  ?H^3-1*1]0! W[0%R#1]D  ", "h3110%20w0r1d")
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(generate_slug(test_data), expected)

