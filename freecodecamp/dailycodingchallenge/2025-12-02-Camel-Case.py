

import re
'''
Camel to Snake

Given a string in camel case, return the snake case version of the string using the following rules:

    The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
    Every uppercase letter in the camel case string starts a new word.
    Convert all letters to lowercase.
    Separate words with an underscore (_).

'''

def to_snake(camel):

    camel = camel[0].upper() + camel[1:]
    all_words = re.findall('[A-Z][^A-Z]*', camel)

    print(all_words)
    result = "_".join(all_words)
    return result.lower()


'''
1. to_snake("helloWorld") should return "hello_world".
Waiting: 2. to_snake("myVariableName") should return "my_variable_name".
Waiting: 3. to_snake("freecodecampDailyChallenges") should return "freecodecamp_daily_challenges".
'''

if __name__ == "__main__":
    print(to_snake("freecodecampDailyChallenges"))



