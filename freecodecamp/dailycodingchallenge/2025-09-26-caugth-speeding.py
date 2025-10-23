

'''
Caught Speeding

Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

    If there were no vehicles speeding, return [0, 0].
'''
def speeding(speeds, limit):
    # print ("Speeding:"+speeds+", limit:"+limit)
    adv_over_limit = map(lambda x: x-limit, speeds)
    result = list(filter(lambda x: x > 0, adv_over_limit))
    # Defaults
    count_speeding = 0
    avg = 0

    if result is not None:
        count_speeding = len(result)
        speed_sum = sum(result)
        if count_speeding > 0:
            avg = speed_sum / count_speeding  
    
    return [count_speeding,avg]

if __name__ == "__main__":
    for item in ([[50, 60, 55], 60],
                [[58, 50, 60, 55], 55]):
        print (list(speeding(item[0],item[1])))

# Unit tests 
import unittest

'''
1. speeding([50, 60, 55], 60) should return [0, 0].
2. speeding([58, 50, 60, 55], 55) should return [2, 4].
3. speeding([61, 81, 74, 88, 65, 71, 68], 70) should return [4, 8.5].
4. speeding([100, 105, 95, 102], 100) should return [2, 3.5].
5. speeding([40, 45, 44, 50, 112, 39], 55) should return [1, 57].
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (([50, 60, 55], 60), [0, 0]),
                    (([58, 50, 60, 55], 55), [2, 4]),
                    (([61, 81, 74, 88, 65, 71, 68], 70),[4, 8.5]),
                    (([100, 105, 95, 102], 100),[2, 3.5]),
                    (([40, 45, 44, 50, 112, 39], 55),[1, 57]),
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(speeding(*test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"Expect:{expected}, test_data:{test_data}")


