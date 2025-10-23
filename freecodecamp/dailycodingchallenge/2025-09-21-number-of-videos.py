
byte_list = ["B","KB", "MB", "GB", "TB"]

def convert_to_bytes(size, unit):
    for index, item in enumerate(byte_list):
        byte_size= 1000 ** (index -1)
        if (byte_size == 0):
            byte_size = 1
        if (item == unit):
            # print ("byte_size:" + str(byte_size))
            return size * byte_size


'''
Video Storage

Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

    The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
    If not given one of the video units above, return "Invalid video unit".
    The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
    If not given one of the hard drive units above, return "Invalid drive unit".
    Return the number of whole videos the drive can fit.
    Use the following conversions:

Unit 	Equivalent
1 B 	1 B
1 KB 	1000 B
1 MB 	1000 KB
1 GB 	1000 MB
1 TB 	1000 GB

For example, given 500, "MB", 100, and "GB" as arguments, determine how many 500 MB videos can fit on a 100 GB hard drive.
'''

def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    if (video_size <= 1):
        return "Invalid video unit"
    if (drive_size <= 1):
        return "Invalid drive unit"
    video = convert_to_bytes(video_size, video_unit)    
    drive = convert_to_bytes(drive_size, drive_unit)    
    print ("Video:"+str(video)+",\nDrive:"+str(drive))
    byte_index = byte_list.index(drive_unit)
    if (3 != byte_index and 4 != byte_index):
        return "Invalid drive unit"


    return  int(drive / video)

if (__name__ == "__main__"):
    print(str(number_of_videos(500, "MB", 100, "GB")))
    print(str(number_of_videos(2000, "MB", 100000, "MB")))


# Unit tests 
import unittest

'''
1. number_of_videos(500, "MB", 100, "GB") should return 200.
2. number_of_videos(1, "TB", 10, "TB") should return "Invalid video unit".
3. number_of_videos(2000, "MB", 100000, "MB") should return "Invalid drive unit".
4. number_of_videos(500000, "KB", 2, "TB") should return 4000.
5. number_of_videos(1.5, "GB", 2.2, "TB") should return 1466.
'''
class TestSlug(unittest.TestCase):
    def test_sample(self):
        results = [ ((500, "MB", 100, "GB"),200),
                    ((1, "TB", 10, "TB"),"Invalid video unit"),
                    ((2000, "MB", 100000, "MB"),"Invalid drive unit"),
                    ((500000, "KB", 2, "TB"),4000),
                    ((1.5, "GB", 2.2, "TB"), 1466)
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(number_of_videos(*test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
