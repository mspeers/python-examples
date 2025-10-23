import re

'''
Longest Word

Given a sentence, return the longest word in the sentence.

    Ignore periods (.) when determining word length.
    If multiple words are ties for the longest, return the first one that occurs
'''
def get_longest_word(sentence):
    sentence = re.sub(r"[^\w ]", '', " "+sentence)
    print(f"sentence:{sentence}")
    words = sentence.split()
    longest_word = words[0]
    longest_word_size = len(longest_word)
    for word in words:
        word_size = len(word)
        if (word_size > longest_word_size):
            longest_word = word
            longest_word_size = word_size


    return longest_word


if __name__ == "__main__":
    print(get_longest_word("Coding challenges are fun and educational."))

# Unit tests 
import unittest

'''
1. get_longest_word("coding is fun") should return "coding".
2. get_longest_word("Coding challenges are fun and educational.") should return "educational".
3. get_longest_word("This sentence has multiple long words.") should return "sentence".
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("coding is fun",   "coding"),
                    ("Coding challenges are fun and educational.",   "educational"),
                    ("This sentence has multiple long words.",   "sentence"),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(get_longest_word(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")