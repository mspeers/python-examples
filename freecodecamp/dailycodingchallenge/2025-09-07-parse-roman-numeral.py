
SYMBOL_VAL = { 
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
}

'''
Roman Numeral Parser

Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:
Symbol 	Value
I 	1
V 	5
X 	10
L 	50
C 	100
D 	500
M 	1000

    Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added.
'''
def parse_roman_numeral(numeral):
    total = 0
    size = len(numeral)
    for index, val in enumerate(numeral):
        cur_val = SYMBOL_VAL[val]
        next_val = cur_val
        if index+1 < size:
            next_val = SYMBOL_VAL[numeral[index+1]]
        if cur_val < next_val:
            # print("Found subtracted")
            total -= cur_val 
        else:   
            total += cur_val
        
        # print(f"Char:{val}, Value:{cur_val}, total:{total}")
        

    return total


# Unit tests 
import unittest

'''
1. parse_roman_numeral("III") should return 3.
2. parse_roman_numeral("IV") should return 4.
3. parse_roman_numeral("XXVI") should return 26.
4. parse_roman_numeral("XCIX") should return 99.
5. parse_roman_numeral("CDLX") should return 460.
6. parse_roman_numeral("DIV") should return 504.
7. parse_roman_numeral("MMXXV") should return 2025.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("III",3),
                    ("IV",4),
                    ("XXVI",26),
                    ("XCIX",99),
                    ("CDLX",460),
                    ("MMXXV",2025),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(parse_roman_numeral(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")

if __name__ == "__main__":
    unittest.main()