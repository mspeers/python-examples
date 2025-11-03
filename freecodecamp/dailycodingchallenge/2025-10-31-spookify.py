

import re
'''
SpOoKy~CaSe

Given a string representing a variable name, convert it to "spooky case" using the following constraints:

    Replace all underscores (_), and hyphens (-) with a tilde (~).
    Capitalize the first letter of the string, and every other letter after that. Ignore the tilde character when counting. Make all other letters lowercase.

For example, given hello_world, return HeLlO~wOrLd.
'''
def spookify(boo):
    # Rule 1 -  Replace all underscores (_), and hyphens (-) with a tilde (~)
    boo = re.sub("[_-]","~",boo)

    # Rule 2 - Capitalize the first letter of the string, and every other letter after that. Ignore the tilde character when counting. Make all other letters lowercase.
    capitalize = True
    results = ""
    for boo_letter in boo:
        print (f"{boo_letter}({ord(boo_letter)}) {capitalize}")
        if (ord(boo_letter) <65 or ord(boo_letter) > 122):
            results += boo_letter
            continue
        if (capitalize == True):
            results += boo_letter.upper()
            capitalize = False
        else:
            results += boo_letter.lower()
            capitalize = True

    return results

if __name__ == "__main__":
    print(spookify("TRICK-or-TREAT"))


'''
1. spookify("hello_world") should return "HeLlO~wOrLd".
2. spookify("Spooky_Case") should return "SpOoKy~CaSe".
3. spookify("TRICK-or-TREAT") should return "TrIcK~oR~tReAt".
4. spookify("c_a-n_d-y_-b-o_w_l") should return "C~a~N~d~Y~~b~O~w~L".
5. spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts") should return "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS".
'''



