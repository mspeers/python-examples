# main includes
import unittest
import sys

# The main function to start application
def main ():
    """
    Main process will take frist input as number for number of input to compare two works to see if any char in word one


    Return
    ------
    prints YES or No for each line readin 

    """

    number = sys.stdin.readline(50)
    results = []
    for _ in range(0, int(number)):
        result = 'YES'
        words = sys.stdin.readline(100)
        wordary = words.split(' ')
        if (len(wordary) != 2):
            result = 'NO'
            results.append(result)
            continue
        char_list = [*(wordary[0])]
        
        for char in char_list:
            if char not in wordary[1]:
                 result = 'NO'
                 break
        results.append(result)

    return results


# Run as standalone application
if ( __name__ == '__main__'):
    for result in main():
        print (result)
else:
    # debug if you like see to what is calling method like lib, standalone, etc...    
    print ("name is ", __name__)

        