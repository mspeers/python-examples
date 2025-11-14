
'''
Array Shift

Given an array and an integer representing how many positions to shift the array, return the shifted array.

    A positive integer shifts the array to the left.
    A negative integer shifts the array to the right.
    The shift wraps around the array.

For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
'''

def shift_array(arr, n):
    result = []
    size = len(arr)
    start_pos = int(n)

    while start_pos < 0:
        start_pos = start_pos + size

    while start_pos > size:
        start_pos = start_pos - size

    if start_pos > size:
        start_pos = start_pos - n
    
    # print(f"start_pos: {start_pos}")

    result = arr[start_pos:]
    result += arr[:start_pos]



    return result

if __name__ == "__main__":
    print(shift_array([1, 2, 3], 1))
    print(shift_array([1, 2, 3], -1))
    print(shift_array(["alpha", "bravo", "charlie"], 5))
'''
1. shift_array([1, 2, 3], 1) should return [2, 3, 1].
2. shift_array([1, 2, 3], -1) should return [3, 1, 2].
3. shift_array(["alpha", "bravo", "charlie"], 5) should return ["charlie", "alpha", "bravo"].
4. shift_array(["alpha", "bravo", "charlie"], -11) should return ["bravo", "charlie", "alpha"].
5. shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15) should return [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].
'''
# Unit tests 

import unittest
from parameterized import parameterized

class TestSequence(unittest.TestCase):
    @parameterized.expand([
        [ ([1, 2, 3], 1),  [2, 3, 1]],
        [ ([1, 2, 3], -1), [3, 1, 2]],
        [ (["alpha", "bravo", "charlie"], 5), ["charlie", "alpha", "bravo"]],
        [ (["alpha", "bravo", "charlie"], -11), ["bravo", "charlie", "alpha"]],
        [ ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15), [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]],
    ])
    def test_sequence(self, test_data, expected):
        # self.assertEqual(test_data,expected)
        self.assertEqual(shift_array(*test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
        print(f"Expect:{expected}, test_data:{test_data}")