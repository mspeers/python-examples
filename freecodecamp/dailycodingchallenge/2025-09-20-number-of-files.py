'''
File Storage

Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:

    The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
    Return the number of whole files the drive can fit.
    Use the following conversions:

Unit 	Equivalent
1 B 	1 B
1 KB 	1000 B
1 MB 	1000 KB
1 GB 	1000 MB

For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.
'''
def number_of_files(file_size, unit_type, drive_size_gb):
    unit_types = ["B", "KB", "MB","GB"]
    find_file_unit = 1
    try:
        find_file_unit = [i for i, x in enumerate(unit_types) if x == unit_type]
        print(f"The first occurrence of {unit_type} is at index: {find_file_unit}")
    except ValueError:
        print("Value not found in the list.")
    unit_type_bytes = (1000 ** (find_file_unit[0]) )
    print(f"unit_type_bytes: {unit_type_bytes}")

    # Math ...
    total_file_bytes = file_size * unit_type_bytes
    drive_size = (drive_size_gb * (1000 ** 3))
    number_files = int(drive_size / total_file_bytes) 

    print(f"number_files:{number_files} = ({drive_size}) / ({total_file_bytes})")

    return number_files


if __name__ == "__main__":
    print (number_of_files(220.5, "KB", 100))



# Unit tests 
import unittest

'''
1. number_of_files(500, "KB", 1) should return 2000.
2. number_of_files(50000, "B", 1) should return 20000.
3. number_of_files(5, "MB", 1) should return 200.
4. number_of_files(4096, "B", 1.5) should return 366210.
5. number_of_files(220.5, "KB", 100) should return 453514.
6. number_of_files(4.5, "MB", 750) should return 166666.
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ ((500, "KB", 1),2000),
                    ((50000, "B", 1),20000),
                    ((5, "MB", 1),200),
                    ((4096, "B", 1.5),366210),
                    ((220.5, "KB", 100), 453514),
                    ((4.5, "MB", 750), 166666)
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(number_of_files(*test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")

