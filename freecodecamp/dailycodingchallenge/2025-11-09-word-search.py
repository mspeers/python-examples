

def check_h(point, direction, matrix, word):
    max_size = len(word)
    for target in range(max_size):
        # print(point)
        r = point[0]+(direction[0]*target)
        c = point[1]+(direction[1]*target)
        # print(f"r{r}, c{c}, matrix:{matrix}")
        if ( r < 0):
            # print(f"Break bc row{r} over max, point:{point}")
            break
        if ( c < 0):
            # print(f"Break bc col{c} over max, point:{point}")
            break
        try:
            letter = matrix[r][c]
        except IndexError:
            # print("Error: Type or name issue.")
            break

        # print(f"letter:{letter}, matrix[{r}][{c}]") 
        if letter != word[target]:    
            # print(f"Break bc {letter}({r},{c}) != {word[target]}, point:{point}, ")
            break
        # print(f"target:{target},max_size:{max_size}")
        if target == (max_size-1):
            end_point = [r, c]
            # print(f"Found:{end_point}")
            return end_point
    return None

DIRECTIONS = [[1,0],[-1,0],[0,1],[0,-1]]

'''
Word Search

Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

    The given matrix will be filled with all lowercase letters (a-z).
    The word to find will always be in the matrix exactly once.
    The word to find will always be in a straight line in one of these directions:
        left to right
        right to left
        top to bottom
        bottom to top

For example, given the matrix:
'''
def find_word(matrix, word):
    row_size = len(matrix)
    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):
            
            if matrix[r_index][c_index] == word[0]:
                point = [r_index, c_index]

                for direction in DIRECTIONS:
                    end_point = check_h(point,direction, matrix, word)
                    if (end_point != None):
                        return [point, end_point]
    return matrix



if __name__ == "__main__":
    # print(find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat"))

    # print(find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog"))

    print(find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox"))



'''
1. find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat") should return [[0, 1], [2, 1]].
2. find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog") should return [[0, 0], [0, 2]].
3. find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish") should return [[3, 3], [0, 3]].
4. find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox") should return [[1, 3], [1, 1]].
'''



