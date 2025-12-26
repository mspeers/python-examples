

import re
'''
Longest Word

Given a sentence string, return the longest word in the sentence.

    Words are separated by a single space.
    Only letters (a-z, case-insensitive) count toward the word's length.
    If there are multiple words with the same length, return the first one that appears.
    Return the word as it appears in the given string, with punctuation removed.

'''
def longest_word(sentence):
    sentence_clean = re.sub("[^a-zA-z ]",'',sentence)
    sentence_split = sentence_clean.split()
    result = ""
    print(f"sentence_clean:{sentence_clean}, ")
    current_size = len(result)
    for word in sentence_split:
        if len(word) > current_size:
            result = word
            current_size = len(result)
            

    return result


    

if __name__ == "__main__":
    print(longest_word("The quick red fox"))

'''
1. longest_word("The quick red fox") should return "quick".
2. longest_word("Hello coding challenge.") should return "challenge".
3. longest_word("Do Try This At Home.") should return "This".
4. longest_word("This sentence... has commas, ellipses, and an exlamation point!") should return "exlamation".
5. longest_word("A tie? No way!") should return "tie".
6. longest_word("Wouldn't you like to know.") should return "Wouldnt".
'''

# # Unit tests 

# import unittest
# from parameterized import parameterized

# class TestSequence(unittest.TestCase):
#     @parameterized.expand([
#         [ ("The quick red fox"), "quick"],
#         [ ("Hello coding challenge."), "challenge"],
#         [ ("Do Try This At Home."), "This"],
#         [ ("This sentence... has commas, ellipses, and an exlamation point!"), "exlamation"],
#         [ ("A tie? No way!"), "tie"],
#         [ ("Wouldn't you like to know."), "Wouldnt"],
#     ])
#     def test_sequence(self, test_data, expected):
#         # self.assertEqual(test_data,expected)
#         self.assertEqual(longest_word(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
#         print(f"Expect:{expected}, test_data:{test_data}")



