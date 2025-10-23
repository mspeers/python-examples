

import re

'''
Gven a string of credit card numbers, return a masked version of it using the following constraints:

    The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
    Replace all numbers, except the last four, with an asterisk (*).
    Leave the remaining characters unchanged.

For example, given "4012-8888-8888-1881" return "****-****-****-1881".
https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-17
'''
def mask(card, mask='*'):
    if (len(card) != 19):
        return "invlaid card"
    card_mask = re.sub(r'\d', mask, card[:-4])
    card_mask += card[-4:]
    return card_mask

'''
Main running for testing 
1. mask("4012-8888-8888-1881") should return "****-****-****-1881".
Passed: 2. mask("5105 1051 0510 5100") should return "**** **** **** 5100".
Passed: 3. mask("6011 1111 1111 1117") should return "**** **** **** 1117".
Passed: 4. mask("2223-0000-4845-0010") should return "****-****-****-0010".
'''
if __name__ =="__main__":
    print (mask("4012-8888-8888-1881"))


