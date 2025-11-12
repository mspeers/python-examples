

import re
'''
Reverse Sentence

Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

    In the given string, words can be separated by one or more spaces.
    The returned string should only have one space between words.
'''

def reverse_sentence(sentence):
    results = []
    sentence = re.sub(' +', ' ', sentence)
    word_list = sentence.split(" ")
    for word in reversed(word_list):
        results.append(word)
    return " ".join(results)

if __name__ == "__main__":
    print(reverse_sentence("npm  install   apt    sudo"))



