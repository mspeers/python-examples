


status_msg = ["short post","long post","invalid post"]

'''
Character Limit

In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:

    "short post" if it fits within a 40-character limit.
    "long post" if it's greater than 40 characters and fits within an 80-character limit.
    "invalid post" if it's too long to fit within either limit.
'''
def can_post(msg):
    result = 2
    size = len(msg)
    print(size)
    if size >= 0 and size <= 40:
        result = 0
    elif size > 40 and size < 80:
        result = 1
    return status_msg[result]

if __name__ == "__main__":
    print(can_post("Hello world"))

'''
1. can_post("Hello world") should return "short post".
2. can_post("This is a longer message but still under eighty characters.") should return "long post".
3. can_post("This message is too long to fit into either of the character limits for a social media post.") should return "invalid post".
'''




