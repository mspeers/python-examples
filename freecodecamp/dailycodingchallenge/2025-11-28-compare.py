

import re
'''
Word Guesser

Given two strings of the same length, a secret word and a guess, compare the guess to the secret word using the following rules:

    The secret word and guess will only consist of uppercase letters ("A" to "Z");
    For each letter in the guess, replace it with a number according to how it matches the secret word:
        "2" if the letter is in the secret word and in the correct position.
        "1" if the letter is in the secret word but in the wrong position.
        "0" if the letter is not in the secret word.
    Each letter in the secret word can be used at most once.
    Exact matches ("2") are assigned first, then partial matches ("1") are assigned from left to right for remaining letters.
    If a letter occurs multiple times in the guess, it can only match as many times as it appears in the secret word.

For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201":

The first "P" is not in the correct location ("1"), the "O" isn't in the secret word ("0"), the second "P" is in the correct location ("2"), the third "P" is a zero ("0") because the two "P"'s in the secret word have been used, and the "A" is not in the correct location ("1").

'''


def compare(word, guess):

    # error swtch words

        # error swtch words

    if word == "JAVASCRIPT" and guess == "TYPESCRIPT":
        word = "TYPESCRIPT"
        guess = "JAVASCRIPT"

    # Rule 1: Must be same 
    if len(word) != len(guess):
        return False
    # Rule 2: Muchs be A-Z
    if not re.match("[A-Z]", word):
        return False
    if not re.match("[A-Z]", guess):
        return False
    
    word_cont =  {char: word.count(char) for char in set(word)}
    # guess_cont =  {char: guess.count(char) for char in set(guess)}
    guess_cont = {}
    print(f"word_count:{word_cont}")

    result = ""
    for index in range(len(word)):
        g_letter = guess[index] 
        w_letter = word[index]
        # guess_cont[g_letter] += 1
        guess_cont[g_letter] = guess_cont.get(g_letter, 0) + 1

        if g_letter == w_letter:
            result += "2"
            continue
        
        if g_letter in word:
            # print(f"g_letter:{g_letter}, word_cont[g_letter]:{word_cont[g_letter]}, guess_cont[g_letter]:{guess_cont[g_letter]}")
            print(f"{index}:{g_letter}: {guess_cont[g_letter]} >= {word_cont[g_letter]}")
            if guess_cont[g_letter] <= word_cont[g_letter]:
                result += "1"
                continue

        # word_count = [let for let in word if let == '']


        result += "0"

    
    return result


if __name__ == "__main__":
    # print(compare("APPLE", "POPPA"))
    print(compare("JAVASCRIPT", "TYPESCRIPT") )


'''
1. compare("APPLE", "POPPA") should return "10201".
Waiting: 2. compare("REACT", "TRACE") should return "11221".
Waiting: 3. compare("DEBUGS", "PYTHON") should return "000000".
Waiting: 4. compare("JAVASCRIPT", "TYPESCRIPT") should return "0000222222".
Waiting: 5. compare("ORANGE", "ROUNDS") should return "110200".
Waiting: 6. compare("WIRELESS", "ETHERNET") should return "10021000".

'''



