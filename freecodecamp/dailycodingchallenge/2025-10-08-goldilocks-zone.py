

import math
'''Space Week Day 5: Goldilocks Zone

For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

    Find the luminosity of the star by raising its mass to the power of 3.5.
    The start of the zone is 0.95 times the square root of its luminosity.
    The end of the zone is 1.37 times the square root of its luminosity.

    Return the distances rounded to two decimal places.

For example, given 1 as a mass, return [0.95, 1.37].
'''
def goldilocks_zone(mass):

    # Find the luminosity of the star by raising its mass to the power of 3.5.
    raising_mase = pow(mass, 3.5)
    print("Debug: Raising Mase:"+str(raising_mase))
    # The start of the zone is 0.95 times the square root of its luminosity.
    zone_start = math.sqrt(raising_mase) * 0.95 
    
    # The end of the zone is 1.37 times the square root of its luminosity.
    zone_end = math.sqrt(raising_mase) * 1.37   
    print ("Debug: Zone start:"+str(zone_start)+", end:"+str(zone_end))
    # Return the distances rounded to two decimal places.
    zone_start = round(zone_start, 2)
    zone_end = round(zone_end, 2)

    return [zone_start,zone_end]


if __name__ == "__main__":
    for item in ([1, [0.95, 1.37]],
                [0.5,[0.28, 0.41]]):
        result = goldilocks_zone(item[0])
        print (result)


# Unit tests 
import unittest

'''
1. goldilocks_zone(1) should return [0.95, 1.37].
2. goldilocks_zone(0.5) should return [0.28, 0.41].
3. goldilocks_zone(6) should return [21.85, 31.51].
4. goldilocks_zone(3.7) should return [9.38, 13.52].
5. goldilocks_zone(20) should return [179.69, 259.13].
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (1, [0.95, 1.37]),
                    (0.5,[0.28, 0.41]),
                    (6,[21.85, 31.51]),
                    (3.7,[9.38, 13.52]),
                    (20,[179.69, 259.13]),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(goldilocks_zone(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")