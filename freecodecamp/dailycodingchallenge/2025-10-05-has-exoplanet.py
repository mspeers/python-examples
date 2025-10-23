

import math

'''
Space Week Day 2: Exoplanet Search

For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

    Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
    Characters 0-9 correspond to luminosity levels 0-9.
    Characters A-Z correspond to luminosity levels 10-35.

A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.
'''
def has_exoplanet(readings):
    readings_val = []
    for read in readings:
        # print(read.upper())
        read_val = ord(read.upper()) -48
        # print("char:"+str(read_val))
        if read_val > 10:
            read_val -= 7
        # print("char second:"+str(read_val))
        readings_val.append(read_val)
    
    avg = sum(readings_val) / (len(readings_val))
    avg_80 = avg * 0.8

    for read in readings_val:
        # print("read:"+ str(read)+", Avg:"+str(avg)+ ", Avg 80%:"+str(avg_80))
        if avg_80 >= read:
            return True
    return False
  
if __name__ == "__main__":
    print(has_exoplanet("665544554"))
    print(has_exoplanet("FGFFCFFGG"))
    # print( has_exoplanet("MONOPLONOMONPLNOMPNOMP"))
    # print(has_exoplanet("FREECODECAMP") )


# Unit tests 
import unittest

'''
1. has_exoplanet("665544554") should return False.
2. has_exoplanet("FGFFCFFGG") should return True.
3. has_exoplanet("MONOPLONOMONPLNOMPNOMP") should return False.
4. has_exoplanet("FREECODECAMP") should return True.
5. has_exoplanet("9AB98AB9BC98A") should return False.
6. has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") should return True.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ("665544554",               False),
                    ("FGFFCFFGG",               True),
                    ("MONOPLONOMONPLNOMPNOMP",  False),
                    ("FREECODECAMP",            True),
                    ("9AB98AB9BC98A",           False),
                    ("ZXXWYZXYWYXZEGZXWYZXYGEE",True),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(has_exoplanet(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")
