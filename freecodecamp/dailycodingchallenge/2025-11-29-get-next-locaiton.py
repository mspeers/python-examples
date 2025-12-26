

'''
Ball Trajectory

Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

    The ball always moves in a straight line.
    The movement direction is determined by how the ball moved from 1 to 2.
    The edges of the matrix are considered walls. If the ball hits a:
        top or bottom wall, it bounces by reversing its vertical direction.
        left or right wall, it bounces by reversing its horizontal direction.
        corner, it bounces by reversing both directions.


'''


def get_next_location(matrix):
    found_start = None
    fount_last = None
    r_size = len(matrix)
    c_size = len(matrix[0])
    for r in range(r_size):
        print(matrix[r])
        for c in range(c_size):
            if matrix[r][c] == 2:
                found_start = [r,c]
            elif matrix[r][c] == 1:
                found_last = [r,c]
    
    print(f"Found:{found_start}")
    row = found_start[0]-found_last[0]
    col = found_start[1]-found_last[1]
    if row + found_start[0] < 0:
        row = 1
    if col + found_start[1] < 0:
        col = 1

    if row + found_start[0] >= r_size:
        row = -1 

    if col + found_start[1] >= c_size:
        col = -1 

    print (f"row:{row}, col:{col}")
    result = [found_start[0] + row,found_start[1] + col]
    
    print (f"result:{result}")
    
 
    return result

if __name__ == "__main__":
    # print(get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]))
    # print( get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]))

    # print(get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]))


    print(get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]))

'''
1. get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) should return [2, 3].
Waiting: 2. get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) should return [3, 0].
Waiting: 3. get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) should return [1, 2].
Waiting: 4. get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) should return [1, 1].
Waiting: 5. get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) should return [2, 2].
'''




