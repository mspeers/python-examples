# main includes
import unittest

def addition(a, b):
    """
    Simpale add to numbers two input

    Parameters
    ----------
    a is the first number
    b is the second number

    Return
    ------
    sum of the two number or error will return None

    """

    total = None
    typeA = type(a)
    typeB = type(b)
    if ((typeA == int or typeA == float) and (typeB == int or typeB == float)):
        total = a + b
    else:
        # Errors message could use raise 
        print (f'Error one of the  A {a} ({typeA}) or B {b} ({typeB}) are not numbers')

    return total

# The main function to start application
def main ():
    """
    Main process 
    """
    a = int(input("input first number to enter: "))
    b = int(input("input second number to enter: "))
    return addition(a,b)

class TestAddition(unittest.TestCase):
    """
    Unit test for Addition class
    """

    def test_addition_good_path(self):
        """
        Test the addition has correct return
        """
        output = addition(1,1)
        self.assertEqual(output, 2, "incorrect result for addition good path")

    def test_addition_good_negaive_numbers(self):
        """
        Test the addition has correct return
        """
        output = addition(-1,-1)
        self.assertEqual(output, -2, "incorrect result for addition good path")


    def test_addition_bad_string(self):
        """
        Test the addition has incorrect return
        """
        output = addition("string",-1)
        self.assertEqual(output, None, "incorrect result for addition bad path")
        output = addition(1, "string")
        self.assertEqual(output, None, "incorrect result for addition bad path")
        output = addition("test", "string")
        self.assertEqual(output, None, "incorrect result for addition bad path")

    def test_addition_bad_None(self):
        """
        Test the addition has incorrect return
        """
        output = addition(None, 1)
        self.assertEqual(output, None, "incorrect result for addition bad path")
        output = addition(-1, None)
        self.assertEqual(output, None, "incorrect result for addition bad path")
        output = addition(None, None)
        self.assertEqual(output, None, "incorrect result for addition bad path")



# Run as standalone application
if ( __name__ == '__main__'):

    # Run main path
    print(main())

else:
    # debug if you like see to what is calling method like lib, standalone, etc...    
    print (f'name is  {__name__}')

# Alway run unit test
unittest.main()