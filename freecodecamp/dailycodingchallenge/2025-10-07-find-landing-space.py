

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


