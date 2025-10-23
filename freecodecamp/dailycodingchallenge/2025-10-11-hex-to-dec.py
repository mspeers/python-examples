

import math

'''
Hex to Decimal

Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

    0-9 represent values 0 through 9.
    A-F represent values 10 through 15.

Here's a partial conversion table:
Hexadecimal 	Decimal
0 	            0
1 	            1
... 	        ...
9 	            9
A 	            10
... 	        ...
F 	            15
10 	            16
... 	        ...
9F 	            159
A0 	            160
... 	        ...
FF 	            255
100 	        256

The string will only contain characters 0-9 and A-F.
'''

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


# Unit tests 
import unittest

'''
1. hex_to_decimal("A") should return 10.
2. hex_to_decimal("15") should return 21.
3. hex_to_decimal("2E") should return 46.
4. hex_to_decimal("FF") should return 255.
5. hex_to_decimal("A3F") should return 2623.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("A", 10),
                    ("15", 21),
                    ("2E", 46),
                    ("FF", 255),
                    ("A3F", 2623),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(hex_to_decimal(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")
