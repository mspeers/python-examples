'''
Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

    Each object will have a "title" property (string), and a "plays" property (integer).
'''
def favorite_songs(playlist):
    number_songs = 2
    # sort by play times
    sorted_playlist = sorted(playlist, key=lambda x: x['plays'])
    sorted_playlist = sorted_playlist[::-1]
    # get only two songs
    result = []
    for index, song in enumerate(sorted_playlist):
        if index >= number_songs:
            break
        result.append(sorted_playlist[index]["title"])
    return result


if __name__ == "__main__":
    print ("RESULT:"+str(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ])))


# Unit tests 
import unittest

'''
1. favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]) should return ["Sync or Swim", "Earbud Blues"].
2. favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]) should return ["Clickwheel Love", "99 Downloads"].
3. favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]) should return ["Song B", "Song C"].
'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        results = [ (([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ] ),["Sync or Swim", "Earbud Blues"]),
                    (([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]),["Clickwheel Love", "99 Downloads"]),
                    (([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]),["Song B", "Song C"])
                  ]

        for test_data, expected in results:
            with self.subTest(expected=expected, test_data=test_data):
                self.assertEqual(favorite_songs(test_data), expected, f"Failed - Expect:{expected}, test_data:{test_data}")
                print(f"test_data: {test_data}")


