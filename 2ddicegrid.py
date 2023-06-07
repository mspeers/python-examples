# main includes
import unittest
# support arrays
from array import *
# 2D Dice Grid Scoring Algorithm - http://www.101computing.net/2d-dice-grid-scoring-algorithm/
from random import randint

def calculatescore(boardgame):
    """
    Calculate Score by the follow:

    1: Start with a score of 0,
    2: If all four corners are even numbers, add 20 pts to the score,
    3: If all four corners are odd numbers, add 20 pts to the score,
    4: If all four dice on a diagonal are even numbers, add 20 pts to the score,
    5: If all four dice on a diagonal are odd numbers, add 20 pts to the score,
    6: If all four dice on on any row are even numbers, add 20 pts to the score,
    7: If all four dice on on any row are odd numbers, add 20 pts to the score,
    8: If all four dice on on any column are even numbers, add 20 pts to the score,
    9: If all four dice on on any column are odd numbers, add 20 pts to the score,
    10: Add to the score the total value (sum) of all 16 dice.
 
    Parameters
    ----------
    boardgame to give grid to score

    Return
    ------
    Sorce of the board game or 0
    """
    # REQ 1: Start with a score of 0
    total = 0

    sumTotal = 0
    # REQ 6, 7, 8, 9, 10
    for r in range(0, len(boardgame.grid)):
        # Rows
        currentrowvalue = boardgame.grid[r][0]%2
        currentcolumvalue = boardgame.grid[0][r]%2
        
        rowflag = colflag = True
        for c in range(0,len(boardgame.grid[0])):
            # Add to the score the total value (sum) of all 16 dice.
            sumTotal += boardgame.grid[r][c]

            tmpmodvalue = boardgame.grid[r][c]%2
            tmpcolummodvalue = boardgame.grid[c][r]%2
            if (currentrowvalue != (tmpmodvalue)):
                    rowflag = False                
            if (currentcolumvalue != tmpcolummodvalue):
                    colflag = False
        if (rowflag != False):
            boardgame.sorce.append(f'+20 in row at {r+1}')
            total += 20
        if (colflag != False):
            boardgame.sorce.append(f'+20 by column at {r+1}')
            total += 20

    # Add to the score the total value (sum) of all 16 dice.
    boardgame.sorce.append(f'+{sumTotal} Sum Total')
    total += sumTotal


    # Customer patterens are not hardcored
    sizegameboard = boardgame.size -1
    custompatterens = { 
    'four corners': [[0,0], [0,sizegameboard], [sizegameboard,0], [sizegameboard,sizegameboard]], # REQ 2,3
    'left diagonal': [], # REQ 4,5 
    'right diagonal': [] # REQ 4,5 
    }
    
    # Build patter for Diagonal
    for i in range (0,sizegameboard):
        custompatterens['left diagonal'].append([i,sizegameboard-i])
        custompatterens['right diagonal'].append([sizegameboard-i,i])



    for name, points in custompatterens.items():
        startValue = boardgame.grid[points[0][0]][points[0][1]]%2
        flag = True
        for point in points:
            print (f'point:{point}')
            if (startValue != boardgame.grid[point[0]][point[1]]%2):
                flag = False
                break
        if (flag == True):
            boardgame.sorce.append(f'+20 by {name}')
            total +=  20

    return total


class BoardGame():
    """
    Board Game of grid of dice game by given size.
    """
    grid = None
    size = 5
    def reset(self):
        """
        Reset the game with randomize int of dice (1 to 6) value 
        """
        self.grid = []
        for row in range(0,self.size):
            self.grid.append([])
            for _ in range(0,self.size):
                dice = randint(1,6)
                self.grid[row].append(dice)      
    sorce = []  
    def display_sorce(self):
        """
        Display all the scorce items from rules above 
        """
        for itemsocre in self.sorce:
            print (f'---------')
            print (f'-{itemsocre}')
        print (f'---------')

    def display(self):
        """
        Display dice in grid 
        """
        if self.grid == None:
            self.reset()
        
        print (f'---------')
        print (f'DICE-GAME')
        for row in self.grid:
            print (f'---------')
            for col in row: print (f'{col}|', end='')
            print ('')

        print (f'---------')




# The main function to start application
def main ():
    """
    Main process 
    """
    diceGame = BoardGame()
    diceGame.display()
    score = calculatescore(diceGame)
    diceGame.display_sorce() 
    return score

class TestDiceGame(unittest.TestCase):
    """
    Unit test for dice game. 
    """

    def test_calculatescore_four_corners(self):
        """
        Test the score for correct four corners return 20 
        Requirement: 2,3
        """
        diceGame = BoardGame()
        

        diceGame.grid  = [[2,1,2,2],
                          [1,2,3,4],
                          [1,2,3,4],
                          [2,1,1,2]]
        output = calculatescore(diceGame)
        self.assertEqual(output, 73, "incorrect result for 4 corners even")


        diceGame.grid  = [[3,2,1,3],
                          [1,2,3,4],
                          [2,2,3,4],
                          [3,1,2,3]]
       
        output = calculatescore(diceGame)
        self.assertEqual(output, 59, "incorrect result for 4 corners odd")


    def test_calculatescore_diagonal_left(self):
        """
        Test the score for correct left diagonal return 20 
        Requirement: 4,5
        """
        diceGame = BoardGame()
        

        diceGame.grid  = [[2,1,1,2],
                          [1,2,3,1],
                          [1,2,2,4],
                          [2,1,1,2]]

        output = calculatescore(diceGame)
        self.assertEqual(output, 48, "incorrect result for diagonal left even")

        diceGame.grid  = [[1,1,1,2],
                        [1,1,3,4],
                        [1,2,1,4],
                        [2,1,2,1]]

        output = calculatescore(diceGame)
        self.assertEqual(output, 28, "incorrect result for diagonal left odd")


    def test_calculatescore_diagonal_right(self):
        """
        Test the score for correct right diagonal return 20 
        Requirement: 4,5
        """
        diceGame = BoardGame()
        

        diceGame.grid  = [[1,1,2,2],
                          [2,1,2,4],
                          [1,2,3,4],
                          [2,2,1,4]]

        output = calculatescore(diceGame)
        self.assertEqual(output, 94, "incorrect result for diagonal right even")

        diceGame.grid  = [[1,1,2,3],
                          [2,1,3,4],
                          [1,3,1,4],
                          [3,2,1,2]]

        output = calculatescore(diceGame)
        self.assertEqual(output, 74, "incorrect result for diagonal right odd")


# Run as standalone application
if ( __name__ == '__main__'):

    # Run main path
    print(f'The Calculate Score is {main()}.')

else:
    # debug if you like see to what is calling method like lib, standalone, etc...    
    print (f'Unkown calling addition.py python application. This was design for command line application. The call was  {__name__}')

# Alway run unit test
print (f'----UNIT TESTS-----')
unittest.main()