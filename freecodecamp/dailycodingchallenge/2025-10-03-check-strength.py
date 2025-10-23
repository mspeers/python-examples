

import re

def check_strength(password):
    rules = 0
    special_characters = ('!', '@', '#', '$', '%', '^', '&', '*')

    # It is at least 8 characters long.
    if (len(password) >=8 ):
        rules += 1
        # print("Add Lenght")
        
    # It contains both uppercase and lowercase letters.
    if re.search("[A-Z]+",password) != None and  re.search("[a-z]+",password) != None:
        # print("Add Lower")
        rules += 1
    # It contains at least one number.
    if (re.search("\d+", password) != None):
        # print("Add Number")
        rules += 1

    for schar in special_characters:
        if password.find(schar) != -1:
            # print("Add Special Char")
            rules += 1
            break

    strength ="weak"
    if rules >= 2 and rules < 4:
        strength = "medium"
    elif rules >= 4:
        strength = "strong"

    return strength

if __name__ == "__main__":
    print (check_strength("pass!!!"))


