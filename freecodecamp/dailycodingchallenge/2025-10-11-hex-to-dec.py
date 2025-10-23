

import math


def get_hex_value(hex, index):
    print("Hex Type:"+ str(type(hex)) +", len hex:"+str(len(hex)))
    if (index > len(hex)):
        print("- Finish")
        return 0

    if type(hex) != str:
        raise Exception("invalid type of hex values. Hex:"+ str(hex))
    # remove last left string 
    char = ord(hex[0-index])
    print("Char "+ chr(char)+ ", value:"+ str(char) )
    value = 0
    # A-F
    if char > 64 and char < 71:
        value = (char - 64) + 9
    elif char > 96 and char < 102:
        value = (char - 96) + 9
    elif char > 47 and char < 60:
        value = (char - 48)
    else:
        raise Exception(f"invalid char '{chr(char)}' hex values. Hex:"+ str(hex))
    # get mod
    print ("-value:"+ str(value))
    mod_value = 16 ** (index -1 )  
    print ("-mod_value:"+ str(mod_value)+ ", index:"+str(index)) 
    if (mod_value > 0):
        value = mod_value * value

    print("-final:"+str(value))
    return value + get_hex_value(hex, index+1)


def hex_to_decimal(hex):
    return get_hex_value(hex, 1)

if __name__ == "__main__":
    print(hex_to_decimal("A3F"))



