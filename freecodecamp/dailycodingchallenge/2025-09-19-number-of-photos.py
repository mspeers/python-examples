
'''
Photo Storage

Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB), return the number of photos the hard drive can store using the following constraints:

    1 gigabyte equals 1000 megabytes.
    Return the number of whole photos the drive can store.
'''
def number_of_photos(photo_size_mb, drive_size_gb):
    photo_size_mb = ( drive_size_gb * 1000 ) /photo_size_mb 
    return int(photo_size_mb)


if __name__ == "__main__":
    print(number_of_photos(1, 1))


# Unit tests 
import unittest

'''
1. number_of_photos(1, 1) should return 1000.
Waiting: 
2. number_of_photos(2, 1) should return 500.
Waiting: 
3. number_of_photos(4, 256) should return 64000.
Waiting: 
4. number_of_photos(3.5, 750) should return 214285.
Waiting: 
5. number_of_photos(3.5, 5.5) should return 1571
'''
class TestSlug(unittest.TestCase):
    def test_sample(self):
        results = [ ((1,1),1000),
                    ((2, 1),500),
                    ((4, 256),64000),
                    ((3.5, 750),214285),
                    ((3.5, 5.5), 1571)
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(number_of_photos(*test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")

