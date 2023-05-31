# main includes
import unittest


# The main function to start application
def main ():
    """
    Main process

    Parameters
    ----------
    a is the first number
    b is the second number

    Return
    ------
    String wiht message.

    """
    return 'hi'


# Run as standalone application
if ( __name__ == '__main__'):
    print(main())
else:
    # debug if you like see to what is calling method like lib, standalone, etc...    
    print ("name is ", __name__)

class TestMain(unittest.TestCase):
    """
    Unit test for main class
    """

    def test_main_out(self):
        """
        Test the main has correct return
        """
        output = main()
        self.assertEqual(output, 'hi', "incorrect out put of main")

# To run unit test after application
unittest.main()
        