

import re
'''
Message Validator

Given a message string and a validation string, determine if the message is valid.

    A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
    Letters are case-insensitive.
    Words in the message are separated by single spaces.
'''
def is_valid_message(message: str, validation: str) -> bool:
    result = False
    
    words = message.split()
    checked = ""
    for word in words:
        checked += word[0]
    print(f"checked:{checked}, validation:{validation}")
    if checked.lower() == validation.lower():
        return True
    # format check 
    # if (re.match("[a-zA-Z ]", message)):


    return result


if __name__ == "__main__":
    print(is_valid_message("hello world", "hw"))

'''
1. is_valid_message("hello world", "hw") should return True.
2. is_valid_message("ALL CAPITAL LETTERS", "acl") should return True.
3. is_valid_message("Coding challenge are boring.", "cca") should return False.
4. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD") should return True.
5. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT") should return False.
'''



