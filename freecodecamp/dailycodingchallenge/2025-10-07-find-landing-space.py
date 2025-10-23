

# The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
def add_point(point, matrix):
    max_len = len(matrix)
    x = point[0]
    y = point[1]
    total = 0
    if x + 1 < max_len:
        total += matrix[x+1][ y]
    if y + 1 < max_len:
        total += matrix[x][y+1]
    if y - 1 >= 0:
        total += matrix[x][y-1]
    if x -1 >= 0:
        total += matrix[x-1][y]
        
    return total


'''
Space Week Day 4: Landing Spot

In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

    Each spot in the matrix will contain a number from 0-9, inclusive.
    Any 0 represents a potential landing spot.
    Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
    The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
    Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
    Return the indices of the safest landing spot. There will always only be one safest spot.

For instance, given:

[
  [1, 0],
  [2, 0]
]

Return [0, 1], the indices for the 0 in the first array.
'''
def find_landing_spot(matrix):
    print("Landing Spots")

    # Each spot in the matrix will contain a number from 0-9, inclusive.
    # for index, value in enumerate(my_list):
    good_points = []
    
    for index_row, row in enumerate(matrix):
        print("- " + str(row))
        for index_col, col in enumerate(row):
            # Any 0 represents a potential landing spot.
    # Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.

            if col == 0:
                good_point = [index_row,index_col]
                good_points.append(good_point)


    g_p_cp = good_points.copy()
    row_len = len(matrix)-1
    col_len = len(matrix[0]) -1
    
    # Return the indices of the safest landing spot. There will always only be one safest spot.
    best_point = good_points[0].copy()
    last_danger = add_point(best_point, matrix)
    for point in good_points:
        current_danger = add_point(point, matrix)
        if (current_danger < last_danger):
            best_point = point





    return best_point


if __name__ == "__main__":
    print ("Final:"+str(find_landing_spot([[1, 0], [2, 0]])))
    print ("Final:"+str(find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]])))
    print ("Final:"+str(find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]])))    


# Unit tests 
import unittest

'''
1. find_landing_spot([[1, 0], [2, 0]]) should return [0, 1].
2. find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) should return [1, 1].
3. find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) should return [2, 2].
4. find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) should return [2, 1].
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (([[1, 0], [2, 0]]), [0, 1]),
                    (([[9, 0, 3], [7, 0, 4], [8, 0, 5]]),[1, 1]),
                    (([[1, 2, 1], [0, 0, 2], [3, 0, 0]]),[2, 2]),
                    (([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]), [2, 1]),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(find_landing_spot(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")