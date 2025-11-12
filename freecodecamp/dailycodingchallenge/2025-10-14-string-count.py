

import re 
'''String Count

Given two strings, determine how many times the second string appears in the first.

    The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.
'''
def count(text, parameter):
    # items = re.findall(parameter,text,overlapped=True)
    items = re.findall(r'(?=('+parameter+"))",text)
    print(items)
    return len(items)


if __name__ == "__main__":
    print(count('abcdefg', 'def'))
    print(count('101010101010101010101', '101'))


'''
1. count('abcdefg', 'def') should return 1.
2. count('hello', 'world') should return 0.
3. count('mississippi', 'iss') should return 2.
4. count('she sells seashells by the seashore', 'sh') should return 3.
5. count('101010101010101010101', '101') should return 10.
'''
