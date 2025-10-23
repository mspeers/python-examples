import math

'''
Perfect Square

Given an integer, determine if it is a perfect square.

    A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.
'''
def is_perfect_square(n):
    if not isinstance(n, int):
        raise TypeError("Input should be a Number.")
    
    if n < 0:      ## positivity
        return False
    if n == 0:      ## 0 pass
        return True


    return (math.isqrt(n) ** 2 == n)

if __name__ == "__main__":
    print(is_perfect_square(49))


# Unit tests 
import unittest

'''
1. is_perfect_square(9) should return True.
2. is_perfect_square(49) should return True.
3. is_perfect_square(1) should return True.
4. is_perfect_square(2) should return False.
5. is_perfect_square(99) should return False.
6. is_perfect_square(-9) should return False.
7. is_perfect_square(0) should return True.
8. is_perfect_square(25281) should return True.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (9, True),
                    (49,True),
                    (1,True),
                    (2,False),
                    (99,False),
                    (-9,False),
                    (0,True),
                    (25281,True),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(is_perfect_square(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")

