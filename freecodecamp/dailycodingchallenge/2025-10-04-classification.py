
'''
Space Week Day 1: Stellar Classification

October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:
    "O": 30,000 K or higher
    "B": 10,000 K - 29,999 K
    "A": 7,500 K - 9,999 K
    "F": 6,000 K - 7,499 K
    "G": 5,200 K - 5,999 K
    "K": 3,700 K - 5,199 K
    "M": 0 K - 3,699 K

    Return the classification of the given star.
'''
def classification(temp):

    star_types = [
        ["O", 30000, -1],
        ["B", 10000, 29999],
        ["A", 7500, 9999],
        ["F", 6000, 7499],
        ["G", 5200, 5999],
        ["K", 3700, 5199],
        ["M", 0, 3699],
    ]

    for star in star_types:
        if (star[2] == -1 and temp >= star[1]):
            print ("Star:" + str(star) +"")
            return star[0]
        if (star[2] >= temp and star[1] <= temp):
            return star[0]

    return "?"

if __name__ == "__main__":
    print(classification(5778))



# Unit tests 
import unittest

'''
1. classification(5778) should return "G".
2. classification(2400) should return "M".
3. classification(9999) should return "A".
4. classification(3700) should return "K".
5. classification(3699) should return "M".
6. classification(210000) should return "O".
7. classification(6000) should return "F".
8. classification(11432) should return "B".
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (5778,      "G"),
                    (2400,      "M"),
                    (9999,      "A"),
                    (3700,      "K"),
                    (3699,      "M"),

                    (210000,    "O"),
                    (6000,      "F"),
                    (11432,     "B"),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(classification(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")


