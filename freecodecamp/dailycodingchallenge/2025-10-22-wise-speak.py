

import re

'''
Speak Wisely, You Must

Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

    Words are separated by a single space.
    Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
    Move all words before and including that word to the end of the sentence and:
        Preserve the order of the words when you move them.
        Make them all lowercase.
        And add a comma and space before them.
    Capitalize the first letter of the new first word of the sentence.
    All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
    Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.

For example, given "You must speak wisely." return "Speak wisely, you must."
'''


def wise_speak(sentence):
    search_words = ["have", "must", "are", "will", "can"]

    # found_elements = [element for enumerate(element) in search_words if element in sentence]

    ending = sentence[-1]
    sentence = re.sub(r'[^a-zA-Z0-9 ]', '', sentence)
    sentence_parts = sentence.lower().split(' ')
    print(f"DEBUG: sentence_parts:\n{sentence_parts}")

    found_elements = [match for match in enumerate(sentence_parts) if match[1] in search_words]
    first_index = found_elements[0][0]+1
    print(f"found_elements:{found_elements}, {first_index}")

    new_sentence = sentence_parts[first_index:]
    new_sentence.append(",")
    new_sentence += sentence_parts[:first_index]
    new_sentence[0] = new_sentence[0].title()
    result = ' '.join(new_sentence)
    result = result.replace(' ,', ',')+ending
    print(f"new_sentence:{result}")



    return result


'''
1. wise_speak("You must speak wisely.") should return "Speak wisely, you must."
Waiting: 2. wise_speak("You can do it!") should return "Do it, you can!"
Waiting: 3. wise_speak("Do you think you will complete this?") should return "Complete this, do you think you will?"
Waiting: 4. wise_speak("All your base are belong to us.") should return "Belong to us, all your base are."
Waiting: 5. wise_speak("You have much to learn.") should return "Much to learn, you have."
'''
if __name__ == "__main__":
    print(wise_speak("You must speak wisely."))


