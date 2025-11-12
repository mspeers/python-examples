'''Unique Characters

Given a string, determine if all the characters in the string are unique.

    Uppercase and lowercase letters should be considered different characters.
'''
def all_unique(s):
    unique_chars = set(s)
    char_count_array = {char: s.count(char) for char in unique_chars}

    print(char_count_array)
    for item in char_count_array:
        if char_count_array[item] > 1:
            print(f"item:{item}")
            return False
    return True

if __name__ == "__main__":
    print(all_unique("~!@#$%^&*()_+"))
    print(all_unique("hello"))



