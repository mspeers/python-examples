

import re

'''
Word Frequency

Given a paragraph, return an array of the three most frequently occurring words.

    Words in the paragraph will be separated by spaces.
    Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
    Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
    The returned array should have all lowercase words.
    The returned array should be in descending order with the most frequently occurring word first.
'''
def get_words(paragraph):
    removed_invalid = re.sub("[^\w ]", '', paragraph.lower())
    paragraph_words = removed_invalid.split()
    count_dict = {}
    for num in paragraph_words:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Sorting the dictionary by keys
    # sorted_dict = dict(sorted(input_dict.items(), ))
    sorted_counts = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    # print (sorted_counts)

    final_three = list(sorted_counts.keys())[:3]
    
    return final_three

if __name__ == "__main__":
    print(get_words("C..oding in Python is fun because coding Python allows for coding in Python easily while coding"))
    print(get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"))



