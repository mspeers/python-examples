

'''
Hidden Treasure

Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

    The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

    Each cell in the 2D array will contain one of the following values:
        "-": No treasure.
        "O": A part of the treasure that has not been found.
        "X": A part of the treasure that has already been found.

    If the dive location has no treasure, return "Empty".

    If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".

    If the dive location finds the last unfound part of the treasure, return "Recovered".

For example, given:

[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]

And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure.
'''
def dive(the_map, coordinates):
    item = ""
    total_parts = sum([i.count('O') for i in the_map])
    item = the_map[coordinates[0]][coordinates[1]]
    print (f"item:{item} at coordinates:{coordinates}")
    for row in the_map:
        print (row)    

    if total_parts > 1 and item == "O":
        item = "X"
    result = {"O": "Recovered", "X": "Found", "-": "Empty"}
    return result[item]

if __name__ == "__main__":
    print(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]))


'''
1. dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]) should return "Recovered".
2. dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]) should return "Empty".
3. dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]) should return "Found".
4. dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]) should return "Found".
5. dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]) should return "Recovered".
6. dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]) should return "Empty".
'''

# Unit tests 

import unittest
from parameterized import parameterized

class TestSequence(unittest.TestCase):
    @parameterized.expand([
        [ ([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]), "Recovered"],
        [ ([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]), "Empty"],
        [ ([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]), "Found"],
        [ ([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]), "Found"],
        [ ([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]), "Recovered"],
        [ ([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]), "Empty"],
    ])
    def test_sequence(self, test_data, expected):
        # self.assertEqual(test_data,expected)
        self.assertEqual(dive(*test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
        print(f"Expect:{expected}, test_data:{test_data}")

