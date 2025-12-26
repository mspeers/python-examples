'''
Rectangle Count

Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

    Only count rectangles with integer width and height.

For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.
'''

def count_rectangles(width, height):
    t_w = 0
    t_h = 0
    for i in range(1,width+1):
        t_w += i
    for i in range(1,height+1):
        t_h += i
    print(f"w:{t_w}")
    return t_w * t_h




if __name__ == "__main__":
    print(count_rectangles(1, 3))



# # Unit tests 

# import unittest
# from parameterized import parameterized

# class TestSequence(unittest.TestCase):
#     @parameterized.expand([
#         [ ("2025-11-14"), "1 day until the weekend."],
#         [ ("2025-01-01"), "3 days until the weekend."],
#         [ ("2025-12-06"), "It's the weekend!"],
#         [ ("2026-09-07"), "5 days until the weekend."],
#         [ ("2026-11-29"), "It's the weekend!"],
#     ])
#     def test_sequence(self, test_data, expected):
#         # self.assertEqual(test_data,expected)
#         self.assertEqual(count_rectangles(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
#         print(f"Expect:{expected}, test_data:{test_data}")



