

"""
2nd Largest

Sorts positive or negative numbers in an and gives us second largest number.

Parameters:
- numbers: list
    An unsorted list of numbers.

Returns:
- list:
    A sorted list of numbers, with positive numbers first followed by negative numbers.

Raises:
- TypeError:
    Raises an error if the input is not a list.
"""
def second_largest(numbers):
    # Checking if the input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input should be a list.")

    # Remove dup
    numbers = list(set(numbers))

    # Sorting the numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Separating positive and negative numbers
    positive_numbers = [num for num in sorted_numbers if num >= 0]
    negative_numbers = [num for num in sorted_numbers if num < 0]

    # Combining positive and negative numbers
    sorted_list = negative_numbers + positive_numbers

    return sorted_list[-2]

# Unit tests for sort_numbers function.
import unittest

class TestSortNumbers(unittest.TestCase):

    def test_sort_positive_numbers(self):
        """
        Tests sorting a list of positive numbers.
        """
        numbers = [5, 2, 8, 1, 3]
        sorted_numbers = second_largest(numbers)
        self.assertEqual(second_largest, 3)

    def test_sort_positive_numbers(self):
        """
        Tests sorting a list of positive and negative numbers.
        """
        numbers = [1, 0, -1, 0, 1, 0, -1, 1, 0]
        sorted_numbers = second_largest(numbers)
        self.assertEqual(second_largest, 0)

# Manual Run
if __name__ == "__main__":
    print (second_largest([1, 2, 3, 4]))
    print (second_largest(([1, 0, -1, 0, 1, 0, -1, 1, 0])))


