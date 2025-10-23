

import math

'''
Space Week Day 3: Phone Home

For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

    The first value in the array is the distance from your location to the first satellite.
    Each subsequent value, except for the last, is the distance to the next satellite.
    The last value in the array is the distance from the previous satellite to your home planet.
    The message travels at 300,000 km/s.
    Each satellite the message passes through adds a 0.5 second transmission delay.
    Return a number rounded to 4 decimal places, with trailing zeros removed.
'''
def send_message(route):
    if type(route) != list:
        return -1
    total = 0
    count = 0
    trans_delay = .5

    for distances in route:
        total += distances
        count += 1

    # The first value in the array is the distance from your location to the first satellite.
    # Each subsequent value, except for the last, is the distance to the next satellite.
    # The last value in the array is the distance from the previous satellite to your home planet.
    # The message travels at 300,000 km/s.
    # Each satellite the message passes through adds a 0.5 second transmission delay.
    # Return a number rounded to 4 decimal places, with trailing zeros removed
    avg =  total
    print("Math:"+str(avg))
    print("(total:"+str(total)+ "/count:"+str(count)+") / 3000000") 
    number = (avg) / 300000
    number = round(number, 4)
    total_delay = (trans_delay * (count -1))
    print("Delay "+str(total_delay))
    number += total_delay
    return number

if __name__ == "__main__":
    print(send_message([300000, 300000]))
# Unit tests 
import unittest

'''
1. send_message([300000, 300000]) should return 2.5.
2. send_message([384400, 384400]) should return 3.0627.
3. send_message([54600000, 54600000]) should return 364.5.
4. send_message([1000000, 500000000, 1000000]) should return 1674.3333.
5. send_message([10000, 21339, 50000, 31243, 10000]) should return 2.4086.
6. send_message([802101, 725994, 112808, 3625770, 481239]) should return 21.1597.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (([300000, 300000]), 2.5),
                    (([384400, 384400]),3.0627),
                    (([54600000, 54600000]),364.5),
                    (([1000000, 500000000, 1000000]), 1674.3333),
                    (([10000, 21339, 50000, 31243, 10000]),2.4086),
                    (([802101, 725994, 112808, 3625770, 481239]), 21.1597),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(send_message(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")

