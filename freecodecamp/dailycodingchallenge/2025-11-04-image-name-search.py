

import re

'''
Image Search

On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

    Ignore the case when matching the search terms.
    Return the images in the same order they appear in the input array.
'''
def image_search(images, term):
    results = []


    text = "John: 25, Jane: 30, Doe: 22"
    pattern = r"(\w+): (\d+)"

    # Using list comprehension with re.group
    found_images = [image for image in images if term.lower() in image.lower()]

        


    return found_images

if __name__ == "__main__":
    print(image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun"))
'''
'''



